---
content-id: MA-BCH-0278
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-019
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
title: Capítulo 19 — De lo local a lo global
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C19.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-19)

En C18, una derivada positiva permitía comparar los valores cercanos con el de un centro fijo. Para afirmar que una función crece entre dos entradas cualesquiera necesitamos relacionar ese incremento completo con alguna de sus pendientes locales. El intervalo conserva todas las entradas que hay entre ambas; sobre ese segmento, continuidad y derivabilidad harán posible encontrar una pendiente interior exactamente igual a la secante.

Los prerrequisitos centrales son continuidad de C14 y diferenciabilidad de C18. Se usan explícitamente los extremos alcanzados sobre segmentos compactos de C16 para Rolle y Darboux, y el valor intermedio de C15 para existencia de una raíz. Límites, acumulación, raíces y finitud son interfaces heredadas. La cadena lógica es Fermat, Rolle y valor medio, seguida de consecuencias sobre signos, cotas, dos funciones, valores intermedios de derivadas y ceros. No suponemos continuidad de la función derivada ni usamos convexidad, segunda derivada, Taylor, integrales o L’Hôpital.

## 19.1. Un extremo interior obliga a detenerse

[]{#MA-SEC-ANM-01-019-001}

Comenzaremos por un extremo local. Cerca de un mínimo, los cambios de salida son no negativos, pero los incrementos de entrada cambian de signo al cruzar el centro. Si las secantes de ambos lados tienen un mismo límite, sus signos opuestos sólo podrán conciliarse en cero. La disponibilidad de entradas a izquierda y derecha será una hipótesis efectiva de la prueba.

**R1 — Fermat.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a$ interior a $D$. Si $f$ tiene un máximo o mínimo local en $a$ y es derivable allí, entonces $f'(a)=0$. Un mínimo local significa que existe $r>0$ tal que $f(x)\ge f(a)$ para $x\in D$ con $|x-a|<r$; un máximo invierte la desigualdad. La interioridad proporciona $\rho>0$ con $B(a,\rho)\subseteq D$, y por tanto acumulación desde ambos lados.

Supongamos que el extremo es un mínimo y llamemos $L=f'(a)$. Dentro del radio $r$ de ese mínimo, el numerador $f(x)-f(a)$ es no negativo: los cocientes son no positivos a la izquierda y no negativos a la derecha. Si $L>0$, la tolerancia $L/2$ proporciona un radio $\delta$ donde $q_{f,a}>L/2$. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Los tres radios aseguran, respectivamente, la comparación de mínimo, la pertenencia al dominio y el control de pendiente; ese cociente izquierdo tendría que ser a la vez positivo y no positivo.

Si $L<0$, la tolerancia $|L|/2$ proporciona un radio $\delta$ donde $q_{f,a}<L/2<0$. Con este radio ponemos $t=\min(r,\rho,\delta)/2$ y la entrada $x=a+t$ contradice ahora el signo derecho. Sólo queda $L=0$. Para un máximo aplicamos el caso probado a $-f$: conserva dominio e interioridad, convierte el máximo en mínimo y tiene derivada $-L$ por C18. Cada contradicción utiliza una entrada explícita, sin construir una sucesión.

![El cuadrado tiene mínimo interior en cero y derivada cero. La identidad en \[0,1\] tiene mínimo y máximo de frontera con derivadas relativas uno. Fermat necesita interioridad o acumulación por ambos lados además de extremo y derivabilidad; las figuras no sustituyen la prueba por signos.](../../assets/books/anm/C19/C19-F01.svg){#fig-anm-c19-f01 fig-alt="Dos gráficos comparan un mínimo interior con tangente horizontal y una identidad con extremos en bordes y pendiente no nula."}

La identidad en $[0,1]$ tiene mínimo en cero y máximo en uno, y sus derivadas relativas valen uno también en esos bordes. Allí sólo está disponible un lado del dominio, de modo que no podemos repetir las dos contradicciones anteriores. El valor absoluto tiene un mínimo interior en cero, pero sus cocientes de ambos lados impiden una derivada bilateral. El cubo, por su parte, tiene derivada cero en cero y valores de ambos signos arbitrariamente cerca. Estos ejemplos distinguen la necesidad de interioridad y derivabilidad para aplicar Fermat de la insuficiencia de una pendiente nula para clasificar el punto.

La prueba también funciona si el centro acumula desde ambos lados en un dominio con huecos: en cada caso basta encontrar una entrada del lado necesario dentro de los radios fijados. La interioridad garantiza esa disponibilidad mediante una bola real completa. En el extremo opuesto, un centro aislado puede ser máximo y mínimo local a la vez, pero no tiene derivada según la definición de C18. Los cocientes y las entradas admitidas deciden qué parte del argumento es aplicable.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-019-001}

¿Qué es un mínimo local relativo?

[]{#MA-MSOL-ANM-01-019-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

Un centro $a\in D$ y un radio donde todas las entradas del dominio tienen valores al menos $f(a)$; no se exige desigualdad fuera de ese radio.

El radio fija una región de comparación y se recorta por el dominio real de la función. El valor central existe y sirve de cota inferior en esa región. No se exige que sea único ni que todos los valores del dominio sean mayores; esas condiciones corresponderían a conclusiones distintas.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-019-002}

¿Qué aporta interioridad a Fermat?

[]{#MA-MSOL-ANM-01-019-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

Entradas admisibles a ambos lados del centro dentro de cualquier radio suficientemente pequeño.

Una bola real contenida en el dominio permite construir entradas a izquierda y derecha dentro del radio del extremo y del radio de derivabilidad. Sus incrementos tienen signos opuestos. Esa disponibilidad geométrica es el paso que fuerza a la pendiente límite a ser simultáneamente no negativa y no positiva.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-019-003}

¿Qué signo tienen las secantes a la izquierda de un mínimo?

[]{#MA-MSOL-ANM-01-019-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

No positivo: el numerador es no negativo y el denominador negativo.

La condición de mínimo controla el numerador, mientras la posición de la entrada controla el denominador. Dividir un número no negativo por uno estrictamente negativo produce una secante no positiva. La conclusión incluye la posibilidad de numerador cero, importante en mínimos no estrictos.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-019-004}

¿Qué signo tienen las secantes a la derecha de un mínimo?

[]{#MA-MSOL-ANM-01-019-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

No negativo: tanto el numerador como el denominador son no negativos, y el segundo es positivo.

A la derecha el incremento es estrictamente positivo y la condición de mínimo hace no negativo el numerador. La secante es por ello no negativa. Junto al signo del lado izquierdo, este control obliga a la derivada a ser cero cuando ambas aproximaciones están disponibles.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-019-005}

¿Por qué una derivada positiva contradice un mínimo interior?

[]{#MA-MSOL-ANM-01-019-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

Fuerza cocientes positivos cerca del centro, incluidos argumentos de la izquierda donde el mínimo exige cocientes no positivos.

La tolerancia igual a media pendiente mantiene todas las secantes suficientemente próximas por encima de cero. Interioridad aporta una entrada izquierda dentro del mínimo de los radios necesarios. Su secante debería ser a la vez positiva y no positiva, contradicción. Una derivada negativa se descarta usando el lado derecho.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-019-006}

¿Qué ocurre con la identidad en los bordes de $[0,1]$?

[]{#MA-MSOL-ANM-01-019-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

Tiene extremos globales y derivadas relativas uno; los bordes no son interiores y no satisfacen la premisa geométrica de Fermat.

En los bordes la aproximación relativa sólo dispone de un lado. Sus secantes valen uno y no contradicen las comparaciones de extremo en ese único lado. Fermat necesita ambas clases de entradas para excluir los signos no nulos. El ejemplo conserva derivadas relativas válidas y muestra la función exacta de interioridad.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-019-007}

¿Pendiente cero basta para un extremo?

[]{#MA-MSOL-ANM-01-019-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

No: el cubo tiene derivada cero en cero y valores de ambos signos arbitrariamente cerca.

La derivada describe el término lineal del comportamiento local. El cubo tiene un término lineal nulo, pero conserva valores positivos y negativos a ambos lados. Por eso no es ni mínimo ni máximo local. Fermat es una condición necesaria para un extremo interior derivable, no una equivalencia.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-019-008}

¿Se usa valor medio para probar Fermat?

[]{#MA-MSOL-ANM-01-019-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

No. Se emplean directamente signos de cocientes, radios de derivabilidad y entradas de ambos lados.

Los radios de derivabilidad controlan secantes centradas en el extremo. La condición de extremo les impone signos, y el dominio permite encontrar entradas de ambos lados. Estos datos bastan para excluir pendientes positivas y negativas. No se utiliza todavía una relación global entre puntos diferentes.

</details>

### Ejercicios de la sección 19.1

[]{#ejercicios-19}

#### Ejercicio 1. Signos en un mínimo

[]{#MA-EX-ANM-01-019-001}

Prueba Fermat para un mínimo interior usando signos de secantes y dos casos para el signo de la derivada.

[]{#MA-SOL-ANM-01-019-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

En un radio del mínimo, $f(x)-f(a)\ge0$; las secantes izquierdas son no positivas y las derechas no negativas. Interioridad da una bola dentro del dominio. Si $L>0$, la tolerancia $L/2$ fuerza pendientes positivas en algún radio: elegir $x=a-\min(r,\rho,\delta)/2$ contradice el signo izquierdo. Si $L<0$, tolerancia $|L|/2$ fuerza pendientes negativas y la entrada derecha con ese mismo mínimo contradice el signo derecho. Los radios son positivos y las entradas distintas del centro. Por tricotomía sólo queda $L=0$.

Los tres radios cumplen obligaciones distintas: mantener el extremo local, permanecer dentro del dominio y controlar el error de pendiente. Su mínimo positivo proporciona una entrada válida en el lado que contradice cada signo propuesto. Así se descartan ambas posibilidades no nulas sin usar valor medio ni seleccionar una sucesión.

</details>

#### Ejercicio 2. El borde no es un centro interior

[]{#MA-EX-ANM-01-019-002}

Analiza los extremos y derivadas relativas de $f(x)=x$ sobre $[0,1]$. Explica por qué no contradicen Fermat.

[]{#MA-SOL-ANM-01-019-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

El orden da mínimo global en cero y máximo global en uno. En cualquier centro acumulante del segmento el cociente perforado vale uno, también en los dos bordes, así sus derivadas relativas son uno. Cada bola centrada en cero contiene entradas negativas fuera del dominio y cada bola centrada en uno contiene entradas mayores que uno, por lo que ninguno es interior. Fermat no se aplica allí; su prueba necesita ambas clases de entradas admisibles, que faltan en los bordes.

**Retorno visual.** Véase [C19-F01](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Los extremos globales también son locales relativos, pero sus centros no contienen una bola real del dominio. La derivada relativa sigue estando definida porque cada borde acumula desde su lado disponible. El ejemplo no invalida Fermat: muestra por qué su hipótesis de ambas direcciones debe mantenerse.

</details>

#### Ejercicio 3. Una esquina y un punto estacionario

[]{#MA-EX-ANM-01-019-003}

Compara $|x|$, $x^2$ y $x^3$ en cero: extremo local, derivabilidad y suficiencia de pendiente nula.

[]{#MA-SOL-ANM-01-019-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

El valor absoluto tiene mínimo global cero, pero secantes de pendientes menos uno y uno, por lo que no es derivable allí. El cuadrado tiene mínimo global y cociente centrado en cero igual a $x$, así derivada cero. El cubo tiene cociente $x^2$ y derivada cero, pero entradas positivas y negativas arbitrariamente cercanas dan valores de signos opuestos: no hay extremo local. Por tanto un extremo interior no crea derivabilidad y una derivada nula no garantiza extremo.

Los tres objetos mantienen continuidad en cero, pero sus secantes y valores vecinos responden a preguntas distintas. La esquina no tiene derivada, el cuadrado tiene mínimo y pendiente nula, y el cubo sólo tiene pendiente nula. Estos casos separan necesidad de derivabilidad para aplicar Fermat y falta de suficiencia de su conclusión.

</details>

#### Ejercicio 4. Dos lados sin un intervalo completo

[]{#MA-EX-ANM-01-019-004}

Prueba que en Fermat puede reemplazarse interioridad por acumulación a ambos lados, manteniendo extremo local y derivada relativa existentes.

[]{#MA-SOL-ANM-01-019-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Sea $L$ la derivada relativa. Para un mínimo, las pendientes de la izquierda son no positivas y las de la derecha no negativas dentro del radio del extremo. Si $L>0$, el radio de error $L/2$ obliga a pendientes positivas; acumulación izquierda entrega una entrada dentro del mínimo de ambos radios, contradicción. Si $L<0$, acumulación derecha y error $|L|/2$ dan la contradicción opuesta. No hace falta una bola completa del dominio, sino entradas de ambos lados en todo radio. Para máximo se aplica el resultado a $-f$. No se infiere esa acumulación sólo de que el centro sea de acumulación por uno de los lados.

Para excluir el signo positivo basta un testigo izquierdo en cada ventana, y para excluir el negativo basta uno derecho. Esa disponibilidad es más débil que contener una bola real completa. La derivada relativa debe controlar también esas entradas y el extremo aportar sus signos. Acumulación de un único lado no alcanza para las dos contradicciones.

</details>

#### Ejercicio 5. Transformar el máximo

[]{#MA-EX-ANM-01-019-005}

Deduce Fermat para un máximo a partir del caso mínimo y verifica las condiciones de la función auxiliar.

[]{#MA-SOL-ANM-01-019-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

Si $f$ alcanza un máximo local en $a$, la función $g=-f$ sobre el mismo dominio alcanza un mínimo local con el mismo radio. El centro sigue siendo interior y C18 da derivabilidad $g\prime(a)=-f\prime(a)$. El caso mínimo implica $g\prime(a)=0$, así $f\prime(a)=0$. La transformación conserva tipos y dominio y sólo invierte el orden de valores; no se utiliza un resultado global o valor medio.

Multiplicar por menos uno convierte la comparación superior del máximo en la inferior del mínimo. No cambia qué entradas están disponibles ni el radio del extremo. La regla de derivación conserva el signo opuesto de la pendiente y permite volver a la igualdad cero para la función original.

</details>

## 19.2. Rolle: volver a la misma altura

[]{#MA-SEC-ANM-01-019-002}

Fermat permite anular la derivada de un extremo interior ya localizado. Para producir ese extremo sobre un segmento usaremos C16: una función continua en el segmento cerrado no vacío alcanza máximo y mínimo. Si los dos bordes tienen la misma altura y la función toma otro valor, al menos uno de esos extremos alcanzados tendrá que quedar dentro.

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, el punto $c=(a+b)/2$ pertenece al interior y sus cocientes son cero. En otro caso hay un $y$ con $f(y)\ne k$, y C16 proporciona puntos $m,M\in[a,b]$ donde $f(m)\le f(x)\le f(M)$ para todo $x$. Cuando $f(y)>k$, el máximo satisface $f(M)>k$ y su punto no puede ser ninguno de los bordes; Fermat en $M$ da la derivada nula. Cuando $f(y)<k$, el mínimo $m$ queda por debajo de ambos bordes y Fermat se aplica allí.

La continuidad permitió alcanzar los extremos; la igualdad de borde situó uno de ellos en el interior, y la derivabilidad hizo posible aplicar Fermat en ese punto. El otro extremo global puede permanecer en la frontera. La prueba sólo necesita que uno de los dos satisfaga las condiciones interiores.

![Para x(1−x) en \[0,1\], los bordes valen cero y el máximo interior en 1/2 tiene valor 1/4 y derivada cero. Este ejemplo tiene un único punto estacionario por la fórmula 1−2x; Rolle en general sólo garantiza existencia, sin unicidad ni un cero adicional de la función.](../../assets/books/anm/C19/C19-F02.svg){#fig-anm-c19-f02 fig-alt="Un arco con bordes a igual altura, un máximo interior marcado y una tangente horizontal por encima de los ceros."}

Podemos comprobar por separado qué ocurre al perder cada hipótesis. La función $u(x)=x$ para $0\le x<1$, con $u(1)=0$, conserva los bordes iguales y la derivada interior uno, pero rompe continuidad en el borde derecho y no tiene una derivada interior nula. La función $v(x)=|x-1/2|$ en $[0,1]$ conserva continuidad e igualdad de borde; en el centro no es derivable y todas las otras derivadas interiores valen uno o menos uno. La identidad conserva continuidad y derivabilidad, pero sus bordes difieren y su pendiente tampoco se anula. Cada ejemplo descarta una garantía universal al omitir una condición; no afirma que toda función que tenga algún punto estacionario deba satisfacer las hipótesis de Rolle.

Una constante satisface la conclusión en todos los puntos interiores y muestra que Rolle no da unicidad. Para una función y un segmento fijados podemos usar un testigo de la existencia, sin reunir elecciones para todos los intervalos simultáneamente. Si los valores iguales de borde son ceros de $f$, el testigo es un cero de $f'$ entre ellos. Su altura puede ser distinta de cero: en $x(1-x)$, la derivada se anula en $1/2$ y la función vale $1/4$.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-019-009}

¿Dónde se exige continuidad en Rolle?

[]{#MA-MSOL-ANM-01-019-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

En todo $[a,b]$, incluidos sus extremos con continuidad relativa al segmento.

La continuidad relativa en los extremos permite aplicar Weierstrass al segmento completo. Una discontinuidad de borde podría impedir que el valor que domina las salidas se alcance. La derivabilidad interior garantiza continuidad allí, pero no sustituye esa comprobación en los bordes incluidos.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-019-010}

¿Dónde se exige derivabilidad en Rolle?

[]{#MA-MSOL-ANM-01-019-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

En todos los puntos de $(a,b)$; no se piden derivadas en los bordes.

Cada centro interior dispone de las dos direcciones necesarias para Fermat. En los bordes Rolle sólo necesita continuidad y la igualdad de valores, no una pendiente. Así el teorema puede utilizarse aunque no existan derivadas en esos dos puntos. Las regiones de sus dos premisas son diferentes y deben declararse.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-019-011}

¿Qué herramienta asegura extremos alcanzados?

[]{#MA-MSOL-ANM-01-019-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

El teorema de extremos sobre compactos de C16, aplicado al segmento cerrado no vacío y la función continua.

El segmento cerrado es compacto y, como $a<b$, no es vacío. La continuidad de la función permite que su imagen tenga máximo y mínimo alcanzados. Después se localiza alguno de sus argumentos dentro del interior. Sólo en esa localización se aplica Fermat; acotación de valores sola no bastaría.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-019-012}

¿Por qué una altura mayor que la de los bordes produce un extremo interior?

[]{#MA-MSOL-ANM-01-019-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

El máximo alcanzado tiene valor mayor que ambos valores de borde, así su punto no puede ser ninguno de ellos.

Los extremos tienen el mismo valor $k$. Si algún valor supera $k$, el máximo global es también mayor que $k$ y no puede producirse en esos bordes. Su argumento interior es un extremo local y tiene derivada cero por Fermat. Si hay un valor menor, se usa el mínimo con la misma lógica.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-019-013}

¿Qué punto sirve si la función es constante?

[]{#MA-MSOL-ANM-01-019-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

El punto medio, que es interior para $a<b$; sus cocientes son cero.

Para $a<b$ el punto $(a+b)/2$ pertenece a $(a,b)$. Todas las secantes de una constante tienen numerador cero y pendiente cero. Esto resuelve el caso que no ofrece ningún valor diferente del de los bordes. La prueba general distingue ese caso antes de localizar un extremo de altura distinta.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-019-014}

¿Rolle exige que ambos extremos globales sean interiores?

[]{#MA-MSOL-ANM-01-019-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

No. Basta uno interior en el caso no constante; el argumento distingue si hay valor superior o inferior al de los bordes.

Un único valor diferente de la altura de borde decide qué extremo global conviene utilizar. Si está por encima, sirve el máximo; si está por debajo, sirve el mínimo. El otro extremo puede permanecer en el borde sin afectar la prueba. Rolle sólo requiere encontrar al menos un centro interior de pendiente cero.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-019-015}

¿Un cero de la derivada entre dos ceros es necesariamente otro cero de la función?

[]{#MA-MSOL-ANM-01-019-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

No. Por ejemplo, $x(1-x)$ tiene ceros en cero y uno y derivada cero en un medio, donde su valor es un cuarto.

Rolle transforma igualdad de valores en una conclusión sobre la pendiente de algún punto interior. No exige que la altura de ese punto coincida con la de los bordes. En la parábola, resolver la ecuación de derivada da medio y evaluar allí da un cuarto. Son preguntas diferentes sobre el mismo testigo.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-019-016}

¿La conclusión de Rolle identifica un punto único?

[]{#MA-MSOL-ANM-01-019-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

No. Asegura al menos uno, y las constantes satisfacen la igualdad en todos los puntos interiores.

La existencia permite varios centros válidos y no prescribe cuál debe tomarse. Para una constante todos los puntos interiores satisfacen la conclusión. El teorema tampoco produce una elección simultánea para una familia infinita de funciones o segmentos. En cada aplicación basta un testigo para los datos fijados.

</details>

### Ejercicios de la sección 19.2

#### Ejercicio 6. Localizar un extremo interior

[]{#MA-EX-ANM-01-019-006}

Si una continua en $[a,b]$ tiene bordes iguales $k$ y algún valor distinto, prueba que alcanza un extremo global interior.

[]{#MA-SOL-ANM-01-019-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

C16 entrega un máximo y un mínimo alcanzados en el segmento. Si el valor distinto es mayor que $k$, el máximo tiene valor al menos tan grande y por tanto mayor que ambos bordes; su punto no puede ser ninguno de ellos y queda en $(a,b)$. Si es menor que $k$, el mínimo queda estrictamente por debajo de ambos bordes y también es interior. Tricotomía cubre los dos casos. No se afirma que ambos extremos globales tengan esa posición ni que la función sea derivable, pues este paso sólo localiza un extremo desde continuidad.

La continuidad y compacidad se usan para alcanzar el extremo, mientras el valor distinto de los bordes se usa para ubicarlo dentro. En este paso no se necesita todavía derivabilidad. Rolle la añadirá sólo cuando aplique Fermat al extremo interior ya localizado. Separar las dos tareas evita atribuir a continuidad una conclusión sobre pendientes.

</details>

#### Ejercicio 7. Una parábola que vuelve al borde

[]{#MA-EX-ANM-01-019-007}

Aplica Rolle a $f(x)=x(1-x)$ en $[0,1]$. Halla todos los puntos de derivada cero y comprueba si son ceros de la función.

[]{#MA-SOL-ANM-01-019-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

El polinomio es continuo y derivable, con bordes cero. C18 da $f\prime(x)=1-2x$, que sólo se anula en $c=1/2$, interior al segmento. Su valor es $1/4$, no cero. Rolle predice existencia de un cero de la derivada entre los dos ceros de la función y en este ejemplo es único por la ecuación explícita; no predice un tercer cero de la función.

**Retorno visual.** Véase [C19-F02](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Resolver $1-2c=0$ prueba unicidad del punto estacionario en este ejemplo concreto. Evaluar la función allí responde a otra pregunta y da un cuarto. Rolle no asegura que el testigo tenga la misma altura que los bordes ni que siempre sea único. Ambas conclusiones aquí se investigan por la fórmula explícita.

</details>

#### Ejercicio 8. Perder continuidad en un borde

[]{#MA-EX-ANM-01-019-008}

Para $u(x)=x$ si $0\le x<1$ y $u(1)=0$, audita Rolle en $[0,1]$ y prueba que la continuidad interior no basta.

[]{#MA-SOL-ANM-01-019-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Los bordes valen cero. Cada punto interior tiene una vecindad donde $u$ es identidad, por lo que su derivada es uno y nunca cero. En uno, las entradas $1-1/(n+2)$ tienen salidas tendentes a uno, distintas del valor cero; no hay continuidad relativa. Se cumplen derivabilidad interior e igualdad de borde, pero falla precisamente continuidad del segmento cerrado. La hipótesis interior por sí sola no garantiza los extremos alcanzados necesarios para la prueba de Rolle.

La restricción interior coincide localmente con la identidad y sus pendientes permanecen en uno. El valor asignado al borde derecho hace coincidir los bordes, pero rompe continuidad relativa allí. Es una sola premisa ausente y la conclusión falla. La auditoría debe revisar todo el segmento cerrado antes de aplicar Rolle.

</details>

#### Ejercicio 9. Omitir la derivabilidad

[]{#MA-EX-ANM-01-019-009}

Analiza Rolle para $|x-1/2|$ en $[0,1]$ y contrasta con eliminar igualdad de borde en la identidad.

[]{#MA-SOL-ANM-01-019-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

La función de valor absoluto trasladada es continua y tiene valores $1/2$ en ambos bordes. A la izquierda de un medio su derivada es menos uno y a la derecha uno; en un medio no existe. Así no hay ninguna derivada interior nula y falla derivabilidad en todo el interior. Para la identidad, continuidad y derivabilidad se cumplen pero los bordes cero y uno son diferentes y su derivada siempre vale uno. Los ejemplos eliminan una sola hipótesis cada vez y muestran que no puede omitirse del enunciado universal.

La esquina interior conserva continuidad e igualdad de bordes, pero elimina la derivada exactamente en el centro que sería candidato. La identidad conserva continuidad y derivabilidad, pero pierde igualdad de bordes. Cada ejemplo conserva las demás premisas y muestra por qué la omitida es necesaria para la garantía universal.

</details>

#### Ejercicio 10. Muchos puntos posibles

[]{#MA-EX-ANM-01-019-010}

Explica por qué Rolle no da unicidad ni una selección simultánea. Trata una función constante y el segmento degenerado.

[]{#MA-SOL-ANM-01-019-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

En una constante sobre un segmento no degenerado todas las pendientes interiores son cero, por lo que cualquier punto interior sirve. La conclusión existencial no designa uno de ellos; su uso fija una función y un segmento y toma un testigo para esa instancia. Para $a=b$, el interior es vacío y no podría existir tal punto, aunque la igualdad de borde sea automática. Por eso se exige $a<b$. Ninguna de estas conclusiones construye un selector para una familia infinita de intervalos.

En un segmento no degenerado una constante tiene muchos testigos interiores. La afirmación existencial permite utilizar alguno en una aplicación, sin identificar una regla preferida global. En un singleton no hay interior y la conclusión de existencia es imposible. Eso justifica la desigualdad estricta de los extremos en el enunciado.

</details>

## 19.3. Restar la secante para encontrar una tangente

[]{#MA-SEC-ANM-01-019-003}

Cuando los bordes tienen alturas diferentes, Rolle no se aplica directamente a la función. La recta secante tiene exactamente ese mismo desnivel, así que restarla hará coincidir los bordes de una nueva función. Una derivada nula de esa diferencia señalará una pendiente original igual a la de la secante.

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

![En \[1,3\], la secante del cuadrado tiene pendiente cuatro y recta 4x−3. La tangente en dos tiene igual pendiente. Restar la secante da H=(x−1)(x−3), con bordes cero y H′(2)=0. El punto medio funciona aquí por el cuadrado; no es un punto prescrito por el teorema general.](../../assets/books/anm/C19/C19-F03.svg){#fig-anm-c19-f03 fig-alt="Parábola con secante y tangente paralelas; al lado, el residuo tiene ceros de borde y mínimo interior horizontal."}

Para usar el resultado con una función original $f:D\to\mathbb R$ entre $u<v$, debemos tener $[u,v]\subseteq D$, continuidad sobre ese segmento y derivabilidad en su interior. La restricción conserva continuidad por C14 y las derivadas por C18: cada centro interior acumula también en el segmento restringido. La igualdad obtenida utiliza entonces las derivadas originales. La sola pertenencia de $u$ y $v$ al dominio no proporciona las evaluaciones intermedias si hay un hueco entre ellos.

En el cuadrado sobre $[a,b]$, la secante tiene pendiente $a+b$ y la ecuación $2c=a+b$ determina el único testigo $c=(a+b)/2$. Esa ubicación no es general. Para el cubo en $[0,1]$, la pendiente secante es uno y $3c^2=1$ da el punto interior $c=1/\sqrt3$, distinto de un medio. En una afín, cualquier punto interior sirve. La existencia de Lagrange no prescribe una receta para encontrar el testigo de una función arbitraria, ni promete que el mismo centro resuelva dos aplicaciones a funciones distintas.

La condición $a<b$ mantiene no nulo el denominador de la secante y no vacío el interior donde debe encontrarse el testigo. Para $a=b$ fallarían ambas obligaciones. Respecto de Rolle sólo hemos retirado la igualdad de borde; la continuidad en todo el segmento y la derivabilidad interior siguen siendo necesarias para la garantía y conservan los contraejemplos ya examinados. La igualdad que obtenemos es exacta aunque no sepamos localizar su punto.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-019-017}

¿Qué pendiente se resta en la prueba de Lagrange?

[]{#MA-MSOL-ANM-01-019-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

La pendiente secante $m=[f(b)-f(a)]/(b-a)$, fijada antes del argumento variable.

La condición $a<b$ asegura que el denominador es positivo y la secante está definida. Su pendiente es un número fijo en la construcción de la auxiliar. Restar la recta de esa pendiente hace coincidir las alturas de los bordes sin alterar continuidad ni derivabilidad interior. Esto permite aplicar Rolle.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-019-018}

¿Qué función tiene bordes cero?

[]{#MA-MSOL-ANM-01-019-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

$H(x)=f(x)-f(a)-m(x-a)$ en el mismo segmento.

En $a$ se anulan directamente las dos diferencias. En $b$, el término $m(b-a)$ coincide con el incremento de salida por definición de $m$. Así ambos valores son cero. La identidad no se supone a partir del gráfico: se calcula usando los bordes y un denominador válido.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-019-019}

¿Cuánto vale $H\prime$ en el interior?

[]{#MA-MSOL-ANM-01-019-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

$f\prime-m$, por la regla algebraica de C18.

La recta que se resta tiene pendiente constante $m$ y la función central $f(a)$ también es constante respecto del argumento. La regla de suma de C18 entrega la diferencia de derivadas en cada centro interior. No se supone continuidad de esas derivadas. La igualdad algebraica basta para traducir la conclusión de Rolle.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-019-020}

¿Qué convierte Rolle en la igualdad de valor medio?

[]{#MA-MSOL-ANM-01-019-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

$H\prime(c)=0$ implica $f\prime(c)=m$ para algún centro interior.

Rolle se aplica a la auxiliar de bordes iguales y da un punto, sin fijar su posición exacta. Anular su derivada equivale a igualar la pendiente original con la secante. Como ese punto es interior, su derivada estaba incluida en las hipótesis. El teorema establece existencia y no una fórmula universal para el centro.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-019-021}

¿Por qué no se admite $a=b$?

[]{#MA-MSOL-ANM-01-019-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

La secante dividiría por cero y el interior sería vacío.

Aunque una función esté definida en el singleton, no hay secante entre extremos distintos ni centro interior. La fórmula de pendiente requeriría un denominador no nulo y la conclusión un punto del interior. Ambas obligaciones fallan en el segmento degenerado. Por eso el enunciado conserva $a<b$.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-019-022}

¿Qué debe comprobarse antes de restringir al par $u<v$?

[]{#MA-MSOL-ANM-01-019-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

Que todo $[u,v]$ está en el dominio, con continuidad sobre él y derivabilidad en su interior.

Que los extremos sean entradas no obliga al dominio a incluir lo que hay entre ellos. La inclusión del segmento permite restringir y aplicar los teoremas de intervalos. Deben conservarse continuidad en los extremos y derivabilidad en todos los centros interiores. Una función en dos piezas separadas puede fallar precisamente esa inclusión.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-019-023}

¿El punto de valor medio del cubo en $[0,1]$ es un medio?

[]{#MA-MSOL-ANM-01-019-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

No. Es $1/\sqrt3$, porque $3c^2=1$ y $c>0$.

La secante del cubo entre cero y uno tiene pendiente uno. Su derivada interior es $3c^2$, así la igualdad exige $c^2=1/3$. Interioridad selecciona la raíz positiva y excluye la negativa. En medio la derivada vale tres cuartos, por lo que esa ubicación no satisface el teorema.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-019-024}

¿Hace falta continuidad de $f\prime$?

[]{#MA-MSOL-ANM-01-019-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

No. Las hipótesis requieren continuidad de $f$ y existencia de sus derivadas interiores.

La prueba utiliza continuidad de la función auxiliar para alcanzar un extremo y derivabilidad interior para aplicar Fermat. Ningún paso requiere que la función derivada sea continua. El ejemplo de bultos cumple todas esas premisas aunque su derivada sea discontinua. Diferenciar ambas funciones evita añadir una hipótesis innecesaria.

</details>

### Ejercicios de la sección 19.3

#### Ejercicio 11. Construir el residuo de la secante

[]{#MA-EX-ANM-01-019-011}

Construye la función auxiliar de Lagrange y verifica todas las hipótesis de Rolle antes de aplicarlo.

[]{#MA-SOL-ANM-01-019-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

Con $a<b$, $m=[f(b)-f(a)]/(b-a)$ es real. La recta $\ell(x)=f(a)+m(x-a)$ comparte los valores de borde y $H=f-\ell$ vive en $[a,b]$. Continuidad de $f$ y de la recta hace continua $H$ en todo el segmento; C18 da derivada $H\prime=f\prime-m$ en su interior. Ambos bordes de $H$ valen cero. Rolle entrega $c$ interior con $H\prime(c)=0$, y la identidad de derivadas implica $f\prime(c)=m$. No se ha aplicado Rolle directamente a $f$, cuyos bordes pueden ser distintos.

La auxiliar conserva dominio, continuidad y derivabilidad mediante reglas ya probadas. La secante resta exactamente el incremento total y produce dos bordes iguales. Rolle se aplica sólo después de esas comprobaciones. Su conclusión se traduce por la identidad de derivadas, sin prescribir de antemano el centro obtenido.

</details>

#### Ejercicio 12. Tangente paralela en el cuadrado

[]{#MA-EX-ANM-01-019-012}

Halla el punto de Lagrange para $x^2$ en $[1,3]$ y calcula la función auxiliar que resta la secante.

[]{#MA-SOL-ANM-01-019-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

La pendiente secante es $(9-1)/(3-1)=4$. La recta es $\ell(x)=1+4(x-1)=4x-3$. El residuo $H(x)=x^2-4x+3=(x-1)(x-3)$ tiene ambos bordes cero y derivada $2x-4$. Se anula sólo en $c=2$, interior al segmento; allí la derivada original vale cuatro. La igualdad de pendientes se verifica exactamente, sin localizar el punto leyendo una figura.

**Retorno visual.** Véase [C19-F03](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El cuadrado produce una secante de pendiente cuatro en ese segmento y la recta correspondiente pasa por ambos bordes. Su resto factorizado verifica las dos anulaciones y su derivada lineal localiza un único centro interior. El punto medio funciona por esa expresión particular, no por una condición general de Lagrange.

</details>

#### Ejercicio 13. El punto medio no es universal

[]{#MA-EX-ANM-01-019-013}

Una aplicación de Lagrange al cubo en $[0,1]$ usa automáticamente $c=1/2$. Corrígela y explica el origen del error.

[]{#MA-SOL-ANM-01-019-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

El incremento de valores y el de entrada son uno, así la pendiente secante es uno. La derivada del cubo es $3c^2$; en un medio vale $3/4$, por lo que no cumple la igualdad. Resolver $3c^2=1$ y exigir $c\in(0,1)$ da $c=1/\sqrt3$. El punto medio funciona para el cuadrado por su fórmula específica, sin ser un dato del teorema. Lagrange asegura existencia interior, no una localización predeterminada.

El testigo de valor medio se identifica resolviendo una ecuación de pendientes y exigiendo pertenencia al interior. La raíz positiva cumple ambas obligaciones; medio no cumple la igualdad. Pasar de un ejemplo simétrico a una regla universal de ubicación omitiría la parte existencial del teorema.

</details>

#### Ejercicio 14. Restringir sin llenar un hueco

[]{#MA-EX-ANM-01-019-014}

Explica qué se necesita para aplicar Lagrange a $f:D\to\mathbb R$ entre $u<v$. Usa un dominio de dos piezas para refutar que basten los extremos.

[]{#MA-SOL-ANM-01-019-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Hace falta $[u,v]\subseteq D$, continuidad en ese segmento y derivabilidad en su interior. La restricción conserva continuidad y, porque cada centro interior acumula en el segmento, también las derivadas originales. En $D=[0,1]\cup[2,3]$, tomar $u=1,v=2$ sólo da dos argumentos válidos y no una función definida en $(1,2)$. La función cero en la primera pieza y uno en la segunda tiene todas sus derivadas relativas cero, mientras la secante entre esos bordes tiene pendiente uno. Lagrange no se aplica: falta su dominio intervalar completo.

La inclusión de los extremos sólo acredita dos evaluaciones, no todas las entradas del segmento. La función por piezas tiene derivadas relativas cero, pero una secante entre sus piezas de pendiente uno. Ese contraste identifica el gasto de intervalaridad. Restringir conserva derivadas donde haya acumulación, pero no rellena un hueco ausente.

</details>

#### Ejercicio 15. Igualdad sin continuidad de derivada

[]{#MA-EX-ANM-01-019-015}

Explica si Lagrange se aplica a la función de bultos de C18 en un segmento cerrado que cruce cero, aunque su derivada sea discontinua allí.

[]{#MA-SOL-ANM-01-019-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

C18 demuestra que F es derivable en toda la recta y por tanto continua en cada punto. Su restricción al segmento es continua, y las derivadas de los centros interiores se conservan. Así Lagrange entrega un punto donde la derivada coincide con la pendiente secante. La discontinuidad de $F'$ en cero no elimina ninguna hipótesis del teorema, porque sólo se exige existencia de las derivadas interiores. No se afirma que el punto de valor medio sea cero o que pueda identificarse por una muestra de bultos.

La derivabilidad global de los bultos aporta continuidad de la función y todas las derivadas interiores de cualquier segmento. Son exactamente las premisas de Lagrange. La discontinuidad de la nueva función derivada en cero no interviene en la prueba. No se deduce por ello una ubicación específica del testigo de valor medio.

</details>

## 19.4. El intervalo convierte signos en orden

[]{#MA-SEC-ANM-01-019-004}

Fijado cualquier par de entradas de un intervalo, el segmento entre ellas sigue dentro del dominio. Podemos aplicar Lagrange a esa restricción y traducir un signo conocido en todos los centros interiores a una comparación entre los valores del par. Así dejamos de comparar únicamente con un centro privilegiado.

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

Sean $x<y$ dos entradas de $I$. Por ser intervalo, $[x,y]\subseteq I$, y las restricciones conservan continuidad y derivadas interiores. R3 proporciona $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El factor $y-x$ es positivo; una derivada no negativa da una diferencia no negativa, y una derivada positiva da una diferencia positiva. Los signos opuestos producen de la misma forma las comparaciones decrecientes. La prueba sirve para un par arbitrario usando un testigo de esa instancia, sin elegir una familia de centros.

En un intervalo abierto, la derivabilidad en cada punto ya da continuidad por C18. Si hay bordes incluidos, conservamos allí la hipótesis de continuidad para poder usar los segmentos que lleguen a ellos.

En la dirección recíproca, supongamos que $f$ es no decreciente y que existe su derivada en un centro interior $a$. Todos sus cocientes centrados en $a$ son no negativos: a la derecha numerador y denominador son no negativos, con denominador positivo; a la izquierda ambos son no positivos, con denominador negativo. Si el límite $L$ fuera negativo, la tolerancia $|L|/2$ y una entrada perforada próxima forzarían un cociente negativo, contradicción. Por tanto $f'(a)\ge0$, sin deducir la existencia de esa derivada sólo del orden.

La monotonía estricta tampoco obliga a una derivada positiva en cada centro. El cubo tiene $f'(0)=0$ y es estrictamente creciente: para $x<y$,
$$y^3-x^3=(y-x)(x^2+xy+y^2)>0,$$
porque $x^2+xy+y^2=(x+y/2)^2+3y^2/4$ sólo podría anularse con $x=y=0$, incompatible con ese par ordenado.

![En un intervalo, continuidad y derivada interior cero fuerzan constancia por Lagrange. En \[0,1\]∪\[2,3\], la función cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto, incluidos bordes, pero no es constante en todo el dominio. El hueco no se rellena y el valor medio no se aplica a través de él.](../../assets/books/anm/C19/C19-F04.svg){#fig-anm-c19-f04 fig-alt="Una constante sobre un segmento completo frente a dos segmentos horizontales a alturas distintas, separados por un hueco sombreado."}

Si $f'=0$ en todo el interior, la identidad de Lagrange hace $f(y)-f(x)=0$ para cada par distinto y prueba constancia en $I$. Una constante tiene a su vez cocientes cero y satisface la condición derivada. Si dos funciones cumplen las mismas hipótesis y $f'=g'$ en el interior, aplicamos el resultado a $f-g$: su diferencia es constante en todo el intervalo. Coincidir en una entrada fija esa constante en cero y permite identificar ambas funciones.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en todas sus entradas, incluidos los bordes, porque cerca de cada una sólo se visita su propia pieza constante. Sin embargo, sus dos alturas son diferentes. Entre uno y dos falta $(1,2)$ y no podemos aplicar Lagrange para compararlas. Derivadas positivas dentro de piezas separadas tampoco ordenan automáticamente las salidas a través del hueco. Incluso sobre un intervalo, asignar un salto a un borde incluido puede invalidar la conclusión si sólo conservamos la derivabilidad interior y perdemos la continuidad de borde.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-019-025}

¿Qué propiedad del dominio conecta dos entradas por Lagrange?

[]{#MA-MSOL-ANM-01-019-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

Ser un intervalo: todo el segmento entre las entradas pertenece al dominio.

Para un par ordenado del intervalo, el segmento que los une sigue dentro del dominio. Su interior dispone de derivadas y la restricción cumple continuidad de bordes. Lagrange relaciona entonces el incremento con una derivada interior. Los huecos de un dominio separado impedirían esa aplicación entre piezas distintas.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-019-026}

¿Qué conclusión da $f\prime\ge0$ en el interior?

[]{#MA-MSOL-ANM-01-019-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

Que $f$ es no decreciente, si también se verifican continuidad en el intervalo y derivabilidad interior.

Fijado $x<y$, el valor medio expresa la diferencia como $f\prime(c)(y-x)$. La derivada es no negativa y el incremento positivo, así la diferencia es no negativa. Como el par era arbitrario, se obtiene orden global en el intervalo. No se afirma crecimiento estricto si la derivada puede anularse.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-019-027}

¿Qué condición suficiente da crecimiento estricto?

[]{#MA-MSOL-ANM-01-019-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

$f\prime>0$ en todo el interior bajo las mismas hipótesis de intervalo y continuidad.

En cada par ordenado, el punto de valor medio tiene derivada estrictamente positiva. Multiplicarla por el incremento positivo produce una diferencia de salida estrictamente positiva. Esta condición es suficiente para todos los pares, pero no necesaria en todos los centros de una función estrictamente creciente.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-019-028}

¿Una función estrictamente creciente tiene siempre derivada positiva?

[]{#MA-MSOL-ANM-01-019-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

No: el cubo es estrictamente creciente y su derivada vale cero en el origen.

El cubo aumenta entre cualquier par ordenado porque su diferencia factoriza en un incremento positivo y otro factor estrictamente positivo. Sin embargo, su derivada en cero es cero. El ejemplo refuta la recíproca de la condición suficiente de crecimiento estricto. Donde una creciente tiene derivada, la condición necesaria sólo es no negatividad.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-019-029}

¿Qué da derivada idénticamente cero en un intervalo?

[]{#MA-MSOL-ANM-01-019-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

Constancia, por aplicar valor medio a cada par; se conserva continuidad en extremos incluidos.

Para dos entradas distintas, Lagrange multiplica el incremento por una derivada interior cero y fuerza igualdad de salidas. Los pares iguales no requieren el teorema. En extremos incluidos se conserva continuidad para aplicar la restricción correspondiente. En un dominio desconexo, las constantes pueden diferir entre piezas.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-019-030}

¿Qué da igualdad de dos derivadas en el interior?

[]{#MA-MSOL-ANM-01-019-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

La diferencia de las funciones es constante sobre el intervalo, bajo sus condiciones de continuidad.

La diferencia $f-g$ es continua y derivable donde corresponde, y su derivada interior vale cero. El resultado de constancia se aplica a esa función en el mismo intervalo. Si además ambas coinciden en una entrada, el valor de la constante se determina como cero. Igualar derivadas sin ese dato deja una diferencia constante posible.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-019-031}

¿Qué falla para constantes diferentes en dos piezas separadas?

[]{#MA-MSOL-ANM-01-019-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

No existe el segmento completo entre puntos de piezas distintas, así el valor medio no permite comparar sus constantes.

Cada pieza permite secantes de numerador cero y derivada relativa cero. Una entrada de una pieza y otra de la segunda no tienen entre ellas un segmento de dominio completo. Por eso no puede aplicarse valor medio a ese par. La constancia local por piezas no obliga a igualdad de sus alturas.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-019-032}

¿Se selecciona un punto $c$ para todos los pares a la vez?

[]{#MA-MSOL-ANM-01-019-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

No. Se fija un par arbitrario y se usa la existencia de un punto para esa instancia.

La demostración de orden o de cota empieza fijando un par arbitrario. El teorema proporciona un testigo para ese segmento y las hipótesis globales controlan su derivada. Después se concluye la desigualdad para el par. No se construye una función que elija testigos para todas las parejas simultáneamente.

</details>

### Ejercicios de la sección 19.4

#### Ejercicio 16. Del signo a cada par

[]{#MA-EX-ANM-01-019-016}

Prueba que $f\prime\ge0$ en el interior de un intervalo, con continuidad de $f$ y derivabilidad interior, implica que $f$ es no decreciente.

[]{#MA-SOL-ANM-01-019-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Fijemos $x<y$ en $I$. Intervalaridad da $[x,y]\subseteq I$, continuidad se conserva en la restricción y cada centro de $(x,y)$ pertenece al interior de $I$. Lagrange entrega $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Como $f\prime(c)\ge0$ y $y-x>0$, resulta $f(x)\le f(y)$. El par era arbitrario, así la función es no decreciente. El testigo se usa sólo para ese par; no se requiere continuidad de la derivada ni seleccionarlo simultáneamente para todas las parejas.

</details>

#### Ejercicio 17. Crecimiento estricto con una derivada nula

[]{#MA-EX-ANM-01-019-017}

Prueba que el cubo es estrictamente creciente y tiene derivada nula en cero. ¿Qué recíproca se refuta?

[]{#MA-SOL-ANM-01-019-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

Para $x<y$, $y^3-x^3=(y-x)(x^2+xy+y^2)$. El segundo factor es $(x+y/2)^2+3y^2/4$, no negativo y sólo cero si $x=y=0$, incompatible con $x<y$. Por tanto la diferencia es estrictamente positiva y el cubo es estrictamente creciente. Su derivada es $3x^2$ y vale cero en el origen. El ejemplo refuta que crecimiento estricto exija derivada positiva en cada centro; la condición necesaria donde existe derivada es sólo no negatividad.

</details>

#### Ejercicio 18. Derivadas iguales, valores fijados

[]{#MA-EX-ANM-01-019-018}

Sean f,g continuas en un intervalo y derivables en su interior, con derivadas iguales. Prueba que su diferencia es constante y determina qué ocurre si coinciden en un punto.

[]{#MA-SOL-ANM-01-019-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Sea $H=f-g$ en el mismo intervalo. Es continua y derivable interiormente, con $H\prime=0$. Para un par $x<y$, Lagrange da $H(y)-H(x)=H\prime(c)(y-x)=0$; los pares iguales son triviales y los inversos se intercambian. Así todas las salidas de $H$ son iguales. Si existe $a$ con $f(a)=g(a)$, esa salida común es $H(a)=0$ y $f=g$ en todo el dominio. El argumento usa sólo diferencias y valor medio, sin introducir integrales ni primitivas.

</details>

#### Ejercicio 19. Constantes distintas en un dominio roto

[]{#MA-EX-ANM-01-019-019}

Construye una función con derivada relativa cero en todos los puntos de $[0,1]\cup[2,3]$ que no sea constante. Revisa también los bordes.

[]{#MA-SOL-ANM-01-019-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Definimos $f=0$ en $[0,1]$ y $f=1$ en $[2,3]$. Una bola relativa de radio $1/2$ alrededor de cualquier entrada sólo toca su propia pieza, y allí las secantes perforadas valen cero. Todas las entradas, incluidos los cuatro bordes, acumulan en el dominio al menos desde un lado; por ello sus derivadas relativas existen y son cero. Sin embargo, $f(0)=0\ne1=f(2)$. El segmento entre piezas falta y no se puede aplicar Lagrange a ese par. La conclusión de constancia requiere intervalo completo, no sólo derivadas relativas nulas.

**Retorno visual.** Véase [C19-F04](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Signo de una derivada existente

[]{#MA-EX-ANM-01-019-020}

Si una función es no decreciente y tiene derivada en un punto interior a su intervalo, prueba que esa derivada es no negativa sin aplicar Lagrange.

[]{#MA-SOL-ANM-01-019-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

En un centro interior $a$, toda secante de una función no decreciente es no negativa. A la derecha, numerador y denominador son no negativos y el denominador es positivo; a la izquierda, ambos son no positivos y el denominador es negativo. Si el límite $L$ fuera negativo, la tolerancia $|L|/2$ forzaría secantes menores que $L/2<0$ en algún radio. Acumulación aporta una entrada perforada allí y contradice el signo establecido. Por tanto $L\ge0$. No se deduce existencia de derivada a partir de monotonía: esa existencia era una premisa.

</details>

## 19.5. De cotas de derivadas a cotas de incrementos

[]{#MA-SEC-ANM-01-019-005}

Lagrange entrega un punto cuya posición puede desconocerse, pero sabemos que está entre las dos entradas. Una barrera válida para todas las derivadas interiores se aplica también a la suya. Podremos así acotar el incremento sin localizar el testigo ni pedir que la función derivada alcance un máximo.

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

![Para el cubo en \[1,2\], 3≤f′≤12 en el interior. R5 da 3(y−x)≤f(y)−f(x)≤12(y−x) para cualquier par ordenado. El panel derecho representa el caso de centro uno, con bandas 1+3(x−1) y 1+12(x−1). Las fórmulas prueban las cotas universales; un muestreo de la derivada no bastaría.](../../assets/books/anm/C19/C19-F05.svg){#fig-anm-c19-f05 fig-alt="La derivada cúbica entre dos cotas horizontales y, al lado, el cubo dentro de dos rectas que controlan sus incrementos desde uno."}

Para el cubo en $[-A,A]$, con $A>0$, la derivada $3t^2$ queda entre cero y $3A^2$. Por R5, cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Si $A=0$, el dominio es un singleton y la uniformidad se verifica directamente. La raíz en $[\alpha,\beta]$, con $0<\alpha<\beta$, es continua y tiene derivada $1/(2\sqrt t)$ en el interior; el denominador está separado de cero y da la barrera $1/(2\sqrt\alpha)$. Sobre $[0,1]$ no hay una constante Lipschitz finita para la raíz, pues los cocientes $1/\sqrt y$ respecto de cero superan cualquier cota. El radio cuadrático de C17 sigue demostrando continuidad uniforme en ese dominio.

Podemos aplicar la misma herramienta al error de una recta. Si su pendiente es $A$ y conocemos $|f'(t)-A|\le\eta$ en todos los puntos interiores entre $a$ y $x$, definimos $H(t)=f(t)-f(a)-A(t-a)$. Con continuidad en ese segmento y derivabilidad en su interior, R5 da
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
En efecto, $H(a)=0$ y $|H'|\le\eta$ en todo el interior; si $x=a$, el error se comprueba directamente y es cero. La derivada conocida sólo en $a$ no da por sí sola esta barrera de derivadas en otros centros. El certificado requiere ese control adicional, sin afirmar una tasa cuadrática ni recurrir a Taylor o a una segunda derivada.

Si partimos de una cota Lipschitz $L$ y existe $f'(a)$ en un centro acumulante, todos sus cocientes perforados tienen magnitud a lo sumo $L$. C13 conserva esa cota al tomar el límite y obtenemos $|f'(a)|\le L$. La existencia del límite sigue siendo una premisa: el valor absoluto es Lipschitz y tiene secantes de pendientes incompatibles en cero. Del mismo modo, una tabla finita de pendientes no acredita una barrera sobre todos los centros que pueda usarse en R5.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-019-033}

¿Qué desigualdad producen $m\le f\prime\le M$?

[]{#MA-MSOL-ANM-01-019-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

Para $x<y$, $m(y-x)\le f(y)-f(x)\le M(y-x)$ bajo las hipótesis del intervalo.

El punto de valor medio pertenece al interior del segmento entre las entradas y cumple las dos cotas de derivada. Su pendiente multiplicada por el incremento reproduce la diferencia de salidas. Como el incremento es positivo, se conservan las desigualdades. La conclusión puede controlar todas las parejas sin conocer el testigo concreto.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-019-034}

¿Por qué no se invierte el orden al multiplicar?

[]{#MA-MSOL-ANM-01-019-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

El incremento de entrada $y-x$ es positivo.

Para entradas ordenadas distintas, la distancia dirigida $y-x$ es estrictamente positiva. Multiplicar por ella conserva el sentido de las dos cotas. Si se invierte el par hay que ordenar primero o pasar a magnitudes con simetría. Si las entradas coinciden, el incremento de salidas es cero y no se aplica Lagrange.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-019-035}

¿Qué controla una cota $|f\prime|\le L$?

[]{#MA-MSOL-ANM-01-019-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

Todos los pares: $|f(y)-f(x)|\le L|y-x|$, sin exigir continuidad de la derivada.

La cota simétrica de derivada controla el valor de cualquier testigo interior que produzca Lagrange. Tomar magnitudes en la identidad da la cota de incremento. Así se obtiene una constante Lipschitz global en el intervalo. No se utiliza un máximo de la derivada ni se requiere su continuidad.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-019-036}

¿Cómo se trata $L=0$?

[]{#MA-MSOL-ANM-01-019-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

La función es constante y cualquier radio prueba uniformidad; no se divide por cero.

La cota de pares se vuelve $|f(y)-f(x)|\le0$ y fuerza igualdad de todas las salidas. El error uniforme es entonces cero para cualquier tolerancia y cualquier radio positivo. Este caso debe separarse antes de usar la fórmula $\varepsilon/L$. La afirmación conserva las hipótesis de intervalo y continuidad.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-019-037}

¿Qué radio uniforme da $L>0$?

[]{#MA-MSOL-ANM-01-019-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

$\varepsilon/L$, a partir del control Lipschitz de todos los pares.

La barrera de derivadas se ha convertido primero en una cota de todos los pares mediante valor medio. A partir de ella, una distancia estrictamente menor que $\varepsilon/L$ produce error estrictamente menor que $\varepsilon$. El radio se fija antes de conocer los puntos. Esta es la conexión entre cotas de derivada y continuidad uniforme.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-019-038}

¿Qué cota funciona para el cubo en $[-A,A]$?

[]{#MA-MSOL-ANM-01-019-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

$L=3A^2$, pues su derivada es $3t^2$.

La magnitud del centro interior no supera $A$, por lo que $3t^2\le3A^2$. Esa barrera vale en todos los interiores y da el control de pares. Para $A>0$ se puede dividir el presupuesto por ella. Para $A=0$ el dominio es singleton y se verifica uniformidad directamente.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-019-039}

¿Lipschitz implica existencia de derivada en cada punto?

[]{#MA-MSOL-ANM-01-019-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

No. Sólo acota las derivadas donde existen; $|x|$ tiene cota Lipschitz uno y no es derivable en cero.

Una cota Lipschitz limita las magnitudes de las secantes y de sus límites si existen. No obliga a que esas secantes tengan un único destino. La esquina del valor absoluto mantiene magnitud uno pero tiene valores laterales opuestos. Así el control global de pares no asegura derivabilidad en cada centro.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-019-040}

¿Basta la derivada en un centro para acotar las derivadas vecinas?

[]{#MA-MSOL-ANM-01-019-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

No. La cota sobre otros centros es una hipótesis adicional, distinta del error normalizado de C18.

La derivada en un centro controla secantes que conservan ese centro fijo. Acotar una familia de derivadas de otros centros es una obligación universal adicional. El capítulo aplica valor medio cuando esa familia ya está controlada. No se deduce esa barrera vecina únicamente de un modelo de primer orden puntual.

</details>

### Ejercicios de la sección 19.5

#### Ejercicio 21. Dos cotas de incrementos

[]{#MA-EX-ANM-01-019-021}

Deriva las cotas $m(y-x)\le f(y)-f(x)\le M(y-x)$ desde cotas de derivada en un intervalo. Indica cómo tratar pares no ordenados para una cota absoluta.

[]{#MA-SOL-ANM-01-019-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Para $x<y$, Lagrange da $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Sustituir $m\le f\prime(c)\le M$ y multiplicar por $y-x>0$ conserva el orden, obteniendo las dos cotas de incremento. Si $-L\le f\prime\le L$ con $L\ge0$, se concluye $|f(y)-f(x)|\le L(y-x)$. Para $y<x$ intercambiamos entradas y usamos simetría de magnitudes; para $x=y$ ambos lados son cero. Así la cota absoluta vale para todos los pares. Continuidad en bordes incluidos permite usar segmentos que los contengan.

</details>

#### Ejercicio 22. Cubo y radio común

[]{#MA-EX-ANM-01-019-022}

Da una constante Lipschitz y un radio uniforme para $x^3$ en $[-2,2]$ usando la derivada.

[]{#MA-SOL-ANM-01-019-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

El cubo es continuo en $[-2,2]$ y derivable en su interior. Allí $f\prime(t)=3t^2$ satisface $0\le f\prime(t)\le12$, porque $|t|\le2$. La cota de incrementos da $|y^3-x^3|\le12|y-x|$ para cualquier par del segmento. Para $\varepsilon>0$, el radio $\delta=\varepsilon/12$ convierte distancia estrictamente menor que él en error menor que $\varepsilon$. La constante controla toda la región antes de conocer el par. No se afirma esa barrera global en la recta no acotada.

**Retorno visual.** Véase [C19-F05](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 23. Una frontera rompe el certificado

[]{#MA-EX-ANM-01-019-023}

Para la función de E008, prueba que la derivada interior acotada por uno no da ninguna cota Lipschitz finita en todo $[0,1]$.

[]{#MA-SOL-ANM-01-019-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

En cada centro interior la función $u$ coincide localmente con la identidad y $u\prime=1$. Supongamos una constante Lipschitz finita $L\ge0$ en todo $[0,1]$. Tomemos $x=(L+1)/(L+2)\in(0,1)$ y $y=1$. Como $u(y)=0$ y $u(x)=x$, tenemos $|u(y)-u(x)|=(L+1)/(L+2)>L/(L+2)=L|y-x|$, contradicción. La discontinuidad del borde invalida Lagrange en esos segmentos. Una cota interior de derivada no sustituye continuidad de la función en los bordes.

</details>

#### Ejercicio 24. La raíz lejos de cero

[]{#MA-EX-ANM-01-019-024}

Da una constante Lipschitz para la raíz en $[1/4,4]$ y explica por qué no puede extenderse una cota finita a $[0,1]$.

[]{#MA-SOL-ANM-01-019-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

La raíz es continua en $[1/4,4]$ y tiene derivada $1/(2\sqrt t)$ en los centros interiores. Como $\sqrt t\ge1/2$, esa derivada tiene magnitud a lo sumo uno. Valor medio da $|\sqrt y-\sqrt x|\le|y-x|$, así sirve constante Lipschitz uno. En $[0,1]$, dado $L>0$, un $0<y<\min(1,1/(L+1)^2)$ cumple $\sqrt y/y=1/\sqrt y>L$, refutando la cota con el par $(0,y)$. Para $L=0$ también falla cualquier $y>0$. La raíz sigue siendo uniforme mediante el radio cuadrático de C17.

</details>

#### Ejercicio 25. Una pendiente cercana en todos los centros

[]{#MA-EX-ANM-01-019-025}

Si $|f\prime(t)-A|\le\eta$ en el interior de un segmento con centro a y extremo x, prueba error de modelo a lo sumo $\eta|x-a|$. ¿Qué dato no basta?

[]{#MA-SOL-ANM-01-019-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

En el segmento entre $a$ y $x$, definimos $H(t)=f(t)-f(a)-A(t-a)$. Es continua y derivable donde corresponde, con $|H\prime(t)|=|f\prime(t)-A|\le\eta$ en todo el interior. La cota de pares da $|H(x)-H(a)|\le\eta|x-a|$, y $H(a)=0$ produce el error solicitado. Si $x=a$, la igualdad de valor se verifica directamente. Saber sólo $f\prime(a)=A$ no acredita la premisa sobre las otras derivadas. El certificado utiliza ese control adicional y no Taylor.

</details>

## 19.6. Comparar dos variaciones en el mismo punto

[]{#MA-SEC-ANM-01-019-006}

Para comparar dos variaciones podríamos aplicar Lagrange a cada función, pero obtendríamos dos testigos que no tienen por qué coincidir. Si queremos relacionar sus derivadas en un mismo centro, debemos combinar las dos variaciones antes de aplicar Rolle. Los incrementos de borde proporcionan los coeficientes de esa combinación.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

Para pasar a cocientes añadimos la condición $g'(t)\ne0$ en todo $(a,b)$. Si los bordes de $g$ fueran iguales, Rolle produciría una derivada nula interior y contradiría esa premisa; por tanto $\Delta g\ne0$. El punto $c$ entregado por R6 también cumple $g'(c)\ne0$. Con ambos denominadores justificados podemos dividir la igualdad cruzada y obtener
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin la no anulación, la igualdad de productos permanece definida aunque algún cociente no exista. Cuando $g$ es constante, por ejemplo, su incremento y su derivada son cero y la forma cruzada dice $0=0$.

![Para f=x² y g=x³ en \[0,1\], ambos incrementos valen uno y Cauchy se satisface en c=2/3. El par (g(c),f(c))=(8/27,4/9) tiene tangente de pendiente f′/g′=1, paralela a la secante de bordes. El gráfico representa el par por su argumento x, sin introducir una regla nueva para curvas. Los puntos de Lagrange separados son 1/2 y 1/√3.](../../assets/books/anm/C19/C19-F06.svg){#fig-anm-c19-f06 fig-alt="El par de valores recorre una curva con secante y tangente paralelas; al lado las dos derivadas coinciden en dos tercios."}

En $[0,1]$, las funciones $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Sus aplicaciones separadas de Lagrange dan los puntos únicos $1/2$ y $1/\sqrt3$, que son distintos. La condición de Cauchy es otra ecuación: $3c^2=2c$ y, como $c>0$, su testigo es $c=2/3$. Allí ambas derivadas valen $4/3$ y su razón es uno, igual a la de incrementos. El par $(g(x),f(x))$ permite representar esa comparación intercambiando las coordenadas de salida; el argumento sigue siendo la aplicación de Rolle a una función real auxiliar y no necesita teoría de curvas parametrizadas.

Un incremento no nulo tampoco basta por sí solo para dividir en cualquier testigo. Para $f=g=x^3$ en $[-1,1]$, ambos incrementos valen dos y el producto cruzado se cumple en todo el interior. En cero, sin embargo, las dos derivadas valen cero y su razón no existe. Podríamos verificar una derivada no nula en un testigo concreto o usar la premisa universal anterior. Tomando $g(x)=x$, cuyo incremento $b-a$ es positivo y cuya derivada es uno, ambas divisiones están protegidas y recuperamos Lagrange.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-019-041}

¿Qué forma de Cauchy permite incrementos nulos?

[]{#MA-MSOL-ANM-01-019-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

La igualdad de productos cruzados $\Delta f\,g\prime(c)=\Delta g\,f\prime(c)$.

Los productos cruzados están definidos incluso si una derivada o un incremento vale cero. La auxiliar de Rolle produce la igualdad antes de hacer cualquier división. Una forma de cocientes exige comprobar luego sus denominadores. Mantener la forma inicial permite tratar casos que esa segunda forma excluiría.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-019-042}

¿Qué coeficientes tiene la función auxiliar?

[]{#MA-MSOL-ANM-01-019-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

Los incrementos de borde de la otra función: $\Delta g$ multiplica $f-f(a)$ y $-\Delta f$ multiplica $g-g(a)$.

Los incrementos de borde son números fijos y no dependen del argumento de la auxiliar. Elegirlos cruzados hace que los valores de la auxiliar se anulen en ambos bordes. Las reglas algebraicas dan su derivada sin cambiar el dominio. Rolle relaciona después las dos derivadas en un mismo centro.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-019-043}

¿Por qué sus bordes coinciden?

[]{#MA-MSOL-ANM-01-019-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

Ambos son cero: en el primer borde se anulan las diferencias y en el segundo se cancelan los productos cruzados.

En $a$ los factores $f(x)-f(a)$ y $g(x)-g(a)$ son cero. En $b$ se obtiene $\Delta g\,\Delta f-\Delta f\,\Delta g=0$. La cancelación no divide por ningún incremento y conserva el caso de incrementos nulos. Esa identidad verifica la premisa de igualdad de bordes para Rolle.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-019-044}

¿Qué condición evita todos los denominadores nulos en la forma de cocientes?

[]{#MA-MSOL-ANM-01-019-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

$g\prime(t)\ne0$ en todo el interior; Rolle también fuerza $\Delta g\ne0$.

Si los valores de borde de $g$ fueran iguales, Rolle produciría una derivada nula interior, contradiciendo la premisa. Así el incremento de $g$ es no nulo. El testigo de Cauchy también tiene derivada de $g$ no nula porque la premisa vale en todo el interior. Sólo entonces se dividen los productos cruzados.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-019-045}

¿Por qué dos aplicaciones separadas de Lagrange no bastan?

[]{#MA-MSOL-ANM-01-019-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

Pueden producir puntos diferentes; Cauchy necesita relacionar ambas derivadas en un mismo centro.

Cada aplicación de Lagrange responde al incremento de una función y puede localizar una pendiente en un centro diferente. Dividir esas dos igualdades daría una razón de derivadas en centros distintos. La auxiliar de Cauchy combina ambas variaciones antes de aplicar Rolle. Así se obtiene un testigo compartido, que es la obligación nueva.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-019-046}

¿Qué punto sirve para $f=x^2$, $g=x^3$ en $[0,1]$?

[]{#MA-MSOL-ANM-01-019-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

$c=2/3$, porque sus incrementos son uno y $3c^2=2c$ con $c>0$.

Los dos incrementos son uno y la igualdad cruzada exige $3c^2=2c$. Factorizar da $c(3c-2)=0$ y la pertenencia a $(0,1)$ excluye cero. El valor restante es dos tercios. La ubicación no coincide con los puntos separados que proporcionarían las dos aplicaciones de Lagrange.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-019-047}

¿Qué ocurre si $g$ es constante?

[]{#MA-MSOL-ANM-01-019-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

El producto cruzado sigue siendo válido como $0=0$, pero la razón por $\Delta g$ y $g\prime$ no existe.

La derivada y el incremento de una constante son cero. La igualdad cruzada no se altera y no necesita información adicional sobre $f$. En cambio, ambas posibles razones tienen denominador cero. La forma cruzada es el enunciado general válido; la división es una consecuencia condicional.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-019-048}

¿Cómo se recupera Lagrange?

[]{#MA-MSOL-ANM-01-019-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

Tomando $g(x)=x$, con incremento $b-a>0$ y derivada uno.

La identidad tiene incremento positivo $b-a$ y derivada uno en todo centro interior. Sustituirla en la igualdad cruzada da $\Delta f=(b-a)f\prime(c)$. Dividir por la longitud no nula recupera la pendiente secante. Así Lagrange es un caso particular de la comparación de dos variaciones.

</details>

### Ejercicios de la sección 19.6

#### Ejercicio 26. Productos cruzados antes de cocientes

[]{#MA-EX-ANM-01-019-026}

Construye la auxiliar de Cauchy y prueba la forma sin divisiones del valor medio.

[]{#MA-SOL-ANM-01-019-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

Fijemos $\Delta f=f(b)-f(a)$ y $\Delta g=g(b)-g(a)$. La auxiliar $H(x)=\Delta g(f(x)-f(a))-\Delta f(g(x)-g(a))$ es continua en $[a,b]$ y derivable en $(a,b)$. Sus bordes son cero y su derivada es $H\prime=\Delta g\,f\prime-\Delta f\,g\prime$, pues los coeficientes están fijados. Rolle proporciona $c$ interior con $H\prime(c)=0$, equivalente a $\Delta f\,g\prime(c)=\Delta g\,f\prime(c)$. No se divide por incrementos ni derivadas, por lo que la identidad incluye sus posibles anulaciones.

</details>

#### Ejercicio 27. Tres puntos diferentes

[]{#MA-EX-ANM-01-019-027}

Para $f=x^2,g=x^3$ en $[0,1]$, compara sus dos puntos de Lagrange con el punto de Cauchy.

[]{#MA-SOL-ANM-01-019-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Para $f=x^2$ y $g=x^3$ en $[0,1]$, ambos incrementos son uno. Lagrange para la primera resuelve $2c=1$ y da $c=1/2$; para la segunda resuelve $3c^2=1$ y da $c=1/\sqrt3$. Son distintos porque $1/4\ne1/3$. Cauchy exige $3c^2=2c$ y la interioridad excluye cero, dejando $c=2/3$. Allí las dos derivadas valen $4/3$. Dos existencias separadas no garantizaban un centro compartido; la auxiliar cruzada sí lo proporciona.

**Retorno visual.** Véase [C19-F06](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 28. Legitimar ambas divisiones

[]{#MA-EX-ANM-01-019-028}

Bajo $g\prime(t)\ne0$ en todo $(a,b)$, prueba que la forma de cocientes de Cauchy está definida.

[]{#MA-SOL-ANM-01-019-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

Si $\Delta g=0$, la igualdad de bordes y las demás premisas permitirían aplicar Rolle a $g$, produciendo una derivada nula interior. Eso contradice $g\prime(t)\ne0$ para todo $t\in(a,b)$, así $\Delta g\ne0$. El testigo $c$ de Cauchy también cumple $g\prime(c)\ne0$. Ahora se divide la igualdad cruzada por $\Delta g\,g\prime(c)$ y se obtiene $f\prime(c)/g\prime(c)=\Delta f/\Delta g$. Las dos divisiones se justifican por separado: un incremento no nulo por sí solo no protege toda derivada.

</details>

#### Ejercicio 29. Un incremento nulo

[]{#MA-EX-ANM-01-019-029}

Aplica la forma cruzada a $f(x)=x$, $g(x)=x(1-x)$ en $[0,1]$. Localiza el punto y explica por qué la razón de incrementos no está definida.

[]{#MA-SOL-ANM-01-019-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Para $f(x)=x$ y $g(x)=x(1-x)$, se tiene $\Delta f=1$ y $\Delta g=0$. La igualdad cruzada exige $g\prime(c)=0$. Como $g\prime(c)=1-2c$, el único centro interior válido es $c=1/2$. Allí $f\prime(c)=1$ y $g\prime(c)=0$, de modo que los productos cruzados son ambos cero. Las razones por $\Delta g$ o por $g\prime(c)$ no están definidas. La forma general conserva una conclusión correcta que la división no puede expresar aquí.

</details>

#### Ejercicio 30. Un testigo donde no se puede dividir

[]{#MA-EX-ANM-01-019-030}

Para $f=g=x^3$ en $[-1,1]$, explica por qué $\Delta g\ne0$ no autoriza dividir la identidad de Cauchy en cualquier punto que la satisfaga.

[]{#MA-SOL-ANM-01-019-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Si $f=g=x^3$ en $[-1,1]$, ambos incrementos valen dos y ambas derivadas son $3c^2$. Por ello la igualdad cruzada se satisface en cualquier centro interior. En $c=0$, las dos derivadas valen cero y su razón sería $0/0$, indefinida, aunque $\Delta g=2\ne0$. Un centro interior no nulo sí permite dividir en este ejemplo, pero un testigo arbitrario no ofrece esa garantía. Para hacerlo se verifica su derivada concreta o se usa la premisa universal de no anulación.

</details>

## 19.7. Darboux: discontinuidad sin saltar valores

[]{#MA-SEC-ANM-01-019-007}

La derivada discontinua construida en C18 conserva una propiedad que una función arbitraria discontinua puede perder: entre dos de sus valores alcanza todos los niveles intermedios. Para demostrarlo volveremos a los extremos de una función continua auxiliar. La continuidad disponible será la de la función original derivable, sin suponer continuidad de su derivada.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. La ecuación buscada equivale a $H'(c)=0$, y en los bordes del segmento tenemos $H'(u)<0<H'(v)$. El signo negativo en $u$ proporciona un radio $\delta_u$ con cocientes negativos. La entrada $t=u+\min(\delta_u,v-u)/2$ pertenece a $(u,v)$ y satisface $H(t)<H(u)$, porque su incremento es positivo. En $v$, el signo positivo da un radio $\delta_v$; la entrada $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y cociente positivo, de donde $H(s)<H(v)$. Por tanto ninguno de los bordes minimiza $H$ sobre $[u,v]$.

Por C18, $H$ es continua en todos los puntos del segmento y su restricción también lo es. C16 garantiza un mínimo alcanzado, y las dos comparaciones anteriores obligan a que alguno de sus argumentos sea $c\in(u,v)$. Este mínimo sobre el segmento es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$ y, por ello, $f'(c)=\lambda$. Si los valores están en el orden opuesto, $f'(u)>\lambda>f'(v)$, aplicamos el caso probado a $-f$ y al nivel $-\lambda$, o usamos un máximo de la misma auxiliar. Un minimizador para este segmento basta; no reunimos una familia de ellos.

![En un bulto de C18, F′=−4u(1−u²) y entre u=0 y u=1/2 aparecen todos los valores entre cero y −3/2. La familia completa tiene F′(0)=0 y F′(x_n)=−3/2 con x_n→0, así no es continua en cero. Se representan cinco términos; R7 garantiza todos los valores intermedios entre los centros por una prueba de extremos, sin suponer continuidad de F′.](../../assets/books/anm/C19/C19-F07.svg){#fig-anm-c19-f07 fig-alt="Perfil derivado de una pieza que cruza una altura intermedia y, al lado, una muestra de pendientes persistentes cerca de cero donde el valor derivado es cero."}

Si $f'$ nunca se anula en $I$, tampoco puede tomar valores de signos opuestos: cero sería un nivel estrictamente intermedio y Darboux obligaría a alcanzarlo. En un intervalo no vacío fijamos un punto y su signo no nulo; el opuesto queda excluido en todos los demás. R4 convierte ese signo común en monotonía estricta de $f$. La no anulación no proporciona por sí sola una barrera positiva uniforme para $|f'|$.

La familia de bultos de C18 es derivable en toda la recta y cumple $F'(0)=0$, mientras $F'(x_n)=-3/2$ para puntos $x_n\to0$. Darboux obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas de esa ruta sigan separadas del valor central. Dentro de un bulto, el perfil $-4u(1-u^2)$ permite reconocer esa variación; la propiedad para toda la función se obtiene de R7, no de una pieza dibujada. Así pueden coexistir discontinuidad y valores intermedios. Un escalón que sólo tome $-1$ y $1$ omitiendo cero no podría ser una derivada existente en todos los puntos de un intervalo que contenga ambos lados.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-019-049}

¿Darboux presupone continuidad de la derivada?

[]{#MA-MSOL-ANM-01-019-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

No. Prueba sus valores intermedios usando continuidad de la función auxiliar, extremos y Fermat.

La auxiliar $f-\lambda x$ es continua porque la función original es derivable. Los signos de sus derivadas de borde excluyen un mínimo allí y Weierstrass lo coloca dentro. Fermat anula su derivada y entrega el nivel solicitado. La continuidad utilizada corresponde a la auxiliar, no a la función derivada.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-019-050}

¿Qué resta se usa para buscar $f\prime(c)=\lambda$?

[]{#MA-MSOL-ANM-01-019-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

$H(x)=f(x)-\lambda x$, cuya derivada es $f\prime(x)-\lambda$.

Restar la recta de pendiente $\lambda$ convierte la ecuación buscada en derivada cero de la auxiliar. Sus pendientes de borde tienen signos opuestos cuando $\lambda$ es intermedio. Eso permite localizar un extremo interior y aplicar Fermat. El dominio intervalar conserva el segmento y los centros donde se desarrolla el argumento.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-019-051}

¿Por qué $H\prime(u)<0$ impide mínimo en el borde izquierdo?

[]{#MA-MSOL-ANM-01-019-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

Una entrada próxima a la derecha tiene cociente negativo y por tanto valor menor que $H(u)$.

El límite negativo de secantes permite un radio donde éstas siguen siendo negativas. Una entrada derecha dentro de ese radio y del segmento tiene incremento positivo y diferencia de valor negativa. Su altura es menor que la del borde izquierdo. Ese borde no puede ser minimizador global del segmento.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-019-052}

¿Por qué $H\prime(v)>0$ impide mínimo en el borde derecho?

[]{#MA-MSOL-ANM-01-019-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

Una entrada próxima a la izquierda tiene incremento negativo y cociente positivo, así su valor es menor que $H(v)$.

La secante izquierda es positiva y su incremento negativo. Multiplicar ambos da una diferencia de valor negativa respecto del borde derecho. Una entrada izquierda suficientemente cercana está dentro del segmento y alcanza una altura menor. Así tampoco ese borde puede minimizar, dejando un minimizador interior.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-019-053}

¿Qué ocurre si se invierte el orden de los dos valores de derivada?

[]{#MA-MSOL-ANM-01-019-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

Se aplica el mismo argumento a $-f$ y $-\lambda$, o se busca un máximo de la función auxiliar.

Cambiar $f$ por $-f$ invierte las dos alturas de derivada y cambia el nivel buscado a $-\lambda$. La regla de signo de C18 conserva derivabilidad. Aplicar el caso ya probado y volver a multiplicar por menos uno entrega el nivel original. No se necesita un nuevo supuesto de continuidad de la derivada.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-019-054}

¿Qué garantiza una derivada que nunca se anula en un intervalo abierto?

[]{#MA-MSOL-ANM-01-019-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

Su signo es constante; dos signos opuestos obligarían por Darboux a alcanzar cero entre ellos.

En un intervalo no vacío se fija una entrada y su derivada tiene un signo porque no es cero. Si otra entrada tuviera el signo opuesto, cero sería un nivel estrictamente intermedio. Darboux lo produciría entre ambas, contradicción. El argumento prueba signo común, pero no un margen uniforme positivo de magnitudes.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-019-055}

¿Valores intermedios implican continuidad?

[]{#MA-MSOL-ANM-01-019-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

No. La derivada discontinua de los bultos de C18 satisface Darboux aunque sus valores no converjan al central.

Darboux garantiza que entre dos valores se alcanzan los niveles intermedios. Continuidad exige además que salidas próximas al centro se aproximen a su valor central. La ruta de bultos mantiene derivadas menos tres medios frente al valor cero, aunque entre esos centros también aparezcan los demás niveles. Las dos propiedades pueden separarse.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-019-056}

¿Puede una derivada saltar directamente de menos uno a uno omitiendo cero?

[]{#MA-MSOL-ANM-01-019-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

No en un intervalo donde sea la derivada de una función derivable en todos sus puntos; Darboux fuerza ese valor intermedio.

Si ambos signos aparecen en dos centros del intervalo, el nivel cero debe alcanzarse en el segmento intermedio por Darboux. Omitirlo contradice que la función propuesta sea una derivada existente en todo el intervalo. Esto descarta un escalón directo, sin afirmar que todas las derivadas sean continuas.

</details>

### Ejercicios de la sección 19.7

#### Ejercicio 31. Excluir los bordes de un mínimo

[]{#MA-EX-ANM-01-019-031}

Si $H\prime(u)<0<H\prime(v)$ y H es derivable en un intervalo abierto que contiene $[u,v]$, prueba que alcanza un mínimo interior en ese segmento.

[]{#MA-SOL-ANM-01-019-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

El límite negativo de secantes en $u$ entrega $\delta_u>0$ con cocientes negativos. La entrada $t=u+\min(\delta_u,v-u)/2$ está dentro del segmento y cumple $H(t)<H(u)$. En $v$, el límite positivo entrega $\delta_v>0$; la entrada $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y secante positiva, así $H(s)<H(v)$. Derivabilidad implica continuidad y Weierstrass da un mínimo alcanzado en $[u,v]$. Ningún borde puede alcanzarlo, de modo que un minimizador $c$ es interior y también un mínimo local de la función original.

</details>

#### Ejercicio 32. Una derivada intermedia sin suponer continuidad

[]{#MA-EX-ANM-01-019-032}

Prueba Darboux para $f\prime(u)<\lambda<f\prime(v)$ y explica cómo tratar el orden opuesto.

[]{#MA-SOL-ANM-01-019-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Sea $H(x)=f(x)-\lambda x$. Cuando $f\prime(u)<\lambda<f\prime(v)$, sus derivadas de borde cumplen $H\prime(u)<0<H\prime(v)$. El argumento anterior localiza un mínimo interior de $H$ en $[u,v]$; Fermat da $H\prime(c)=0$ y por ello $f\prime(c)=\lambda$. La continuidad usada es la de $H$, consecuencia de derivabilidad de $f$, sin suponer continuidad de $f\prime$. Si las derivadas están en orden opuesto, aplicamos el caso probado a $-f$ y $-\lambda$ y traducimos la igualdad al signo original.

</details>

#### Ejercicio 33. Continuidad y ausencia de saltos

[]{#MA-EX-ANM-01-019-033}

Usa la familia de bultos de C18 para distinguir continuidad de derivada y propiedad de Darboux. Explica qué valores deben aparecer entre cero y cada $x_n$.

[]{#MA-SOL-ANM-01-019-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La función de bultos es derivable en toda la recta, con $F\prime(0)=0$ y $F\prime(x_n)=-3/2$ para una ruta $x_n\to0$. Esta ruta refuta continuidad de $F\prime$ en cero. Sin embargo, Darboux se aplica entre cero y cada $x_n>0$: para cualquier $\lambda\in(-3/2,0)$ existe un centro estrictamente entre ambos con $F\prime=\lambda$. El testigo puede depender del nivel y del índice. Alcanzar esos valores intermedios no obliga a que las derivadas de la ruta converjan al valor central.

**Retorno visual.** Véase [C19-F07](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Una derivada sin ceros tiene un signo

[]{#MA-EX-ANM-01-019-034}

Prueba que una derivada no nula en un intervalo abierto tiene signo constante, sin asumir continuidad de esa derivada.

[]{#MA-SOL-ANM-01-019-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

Si hubiera una derivada positiva y otra negativa en el intervalo abierto, cero estaría estrictamente entre sus valores. Darboux produciría un centro intermedio de derivada cero, contradiciendo la premisa. Para el intervalo no vacío fijamos un centro y su signo no nulo; el opuesto queda excluido en todos los demás. Por las reglas de signo, la función es estrictamente creciente o decreciente según ese signo. No se obtiene automáticamente una separación uniforme de las magnitudes de la derivada respecto de cero.

</details>

#### Ejercicio 35. Un escalón no puede ser una derivada

[]{#MA-EX-ANM-01-019-035}

En $(-1,1)$, sea h menos uno para $x<0$ y uno para $x\ge0$. Prueba que no existe una función derivable en todo ese intervalo con derivada h.

[]{#MA-SOL-ANM-01-019-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

Supongamos una función derivable en $(-1,1)$ con derivada $h$. En $u=-1/2$ su derivada sería menos uno y en $v=1/2$ sería uno. Darboux aplicado al nivel cero entregaría $c\in(-1/2,1/2)$ con derivada cero. Pero $h$ sólo toma menos uno y uno, contradicción. No se ha supuesto continuidad de $h$ ni se ha utilizado el gráfico de su salto; se infringe una propiedad necesaria de toda derivada en un intervalo.

</details>

## 19.8. Certificar ceros y soluciones únicas

[]{#MA-SEC-ANM-01-019-008}

Para certificar una raíz necesitaremos tareas diferentes: asegurar que existe, impedir que haya otra y medir cuánto dista de un aproximante. Rolle puede descartar valores repetidos y contar ceros a partir de los de la derivada; la existencia de una raíz vendrá de continuidad y valor intermedio. Las cotas de incrementos convertirán después el residuo en un error de posición.

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

Consideremos $p(x)=x^3+x-1$ en $[0,1]$. El polinomio es continuo y sus valores $p(0)=-1$ y $p(1)=1$ permiten aplicar el valor intermedio de C15 para obtener una raíz $r\in(0,1)$. Su derivada $3x^2+1\ge1$ nunca se anula: R8 descarta otra raíz y R4 da crecimiento estricto. La raíz se obtuvo por continuidad; Rolle y el signo de derivada aportan unicidad y orden.

Los valores exactos $p(1/2)=-3/8$ y $p(3/4)=11/64$ sitúan la única raíz en $(1/2,3/4)$: el valor intermedio produce una raíz en ese subsegmento y la unicidad la identifica con $r$. Para el aproximante $x=2/3$ tenemos $p(x)=-1/27$; como $p$ crece y $p(r)=0$, resulta $x<r$. Todos los puntos del segmento entre ellos están en $[1/2,3/4]$, donde $1/4\le t^2\le9/16$ y, por tanto,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
R5 aplica esas dos barreras al incremento entre $x$ y $r$:
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
y al dividir por constantes positivas obtenemos
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
La cota superior de derivada da aquí la cota inferior de distancia, y la inferior da la superior. En general, si $f'\ge m>0$ en el interior del segmento entre un aproximante $x$ y una raíz $r$, con continuidad y derivabilidad donde corresponde, la cota de incrementos implica $m|x-r|\le|f(x)-f(r)|=|f(x)|$. Así $|x-r|\le|f(x)|/m$, sin localizar el punto de valor medio ni extraer cifras de un gráfico.

![C15 garantiza la raíz r y Rolle su unicidad. Los signos exactos en 1/2 y 3/4 la encierran; p(2/3)=−1/27 la sitúa a la derecha del aproximante. Las cotas 7/4≤p′≤43/16 en ese segmento dan 16/1161≤r−2/3≤4/189. Los extremos de la banda son cotas cerradas, sin atribuir a r una coordenada numérica extraída del dibujo.](../../assets/books/anm/C19/C19-F08.svg){#fig-anm-c19-f08 fig-alt="Polinomio con una horquilla de signos y aproximante señalado; una banda aparte encierra la distancia de su raíz mediante dos fracciones exactas."}

El número máximo de ceros permitido por R8 puede alcanzarse. Para $q(x)=x^3-3x$, la derivada $3x^2-3$ tiene exactamente los dos ceros $-1,1$, así que $q$ tiene a lo sumo tres ceros distintos. La factorización $q(x)=x(x^2-3)$ y las raíces de C10 exhiben precisamente $-\sqrt3,0,\sqrt3$. El conteo sólo utiliza finitos segmentos de Rolle y no necesita derivadas de orden superior.

Para convertir estos argumentos en un certificado, la barrera de derivadas debe valer en todos los centros interiores pertinentes. Una tabla finita no impide que el punto de valor medio caiga en un centro no controlado. Del mismo modo, antes de aplicar Rolle entre dos valores iguales debemos conservar el segmento completo del dominio. La conclusión sobre ceros tiene una dirección precisa: de dos ceros de la función obtenemos uno de su derivada entre ellos; dos puntos estacionarios no aseguran por sí solos nuevas raíces de la función.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-019-057}

¿Qué da Rolle si dos entradas tienen el mismo valor?

[]{#MA-MSOL-ANM-01-019-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

Un punto interior de derivada cero, siempre que su segmento esté en el dominio y se verifiquen continuidad y derivabilidad.

El teorema se aplica a igualdad de dos valores cualesquiera, no sólo a ceros de la función. El segmento completo y sus condiciones de continuidad y derivabilidad son premisas necesarias. Si la derivada nunca se anula, esa igualdad resulta imposible para entradas distintas. Se obtiene inyectividad, pero aún no existencia de una solución para un nivel dado.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-019-058}

¿Qué cota de ceros de $f$ da a lo sumo $k$ ceros de $f\prime$?

[]{#MA-MSOL-ANM-01-019-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

A lo sumo $k+1$ ceros distintos de $f$, usando los segmentos entre una lista finita de ceros ordenados.

Si hubiera $k+2$ ceros distintos, se ordenaría esa lista finita. Los $k+1$ segmentos vecinos aportarían por Rolle otros tantos ceros de derivada en interiores separados. Eso infringiría la cota $k$. El argumento cuenta raíces distintas y no sus multiplicidades.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-019-059}

¿Por qué los ceros de derivada de los segmentos vecinos son distintos?

[]{#MA-MSOL-ANM-01-019-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

Cada uno está en un interior diferente, y esos interiores no se solapan.

Cada testigo queda estrictamente entre los extremos de su propio segmento. Los interiores de segmentos consecutivos no se intersectan, aunque compartan un extremo de borde. Por ello sus testigos no pueden coincidir. Esa localización permite convertir aplicaciones de Rolle en un recuento de ceros distintos.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-019-060}

¿Qué herramienta garantiza existencia del cero de $x^3+x-1$?

[]{#MA-MSOL-ANM-01-019-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

Continuidad y valor intermedio de C15, con signos opuestos en cero y uno; Rolle sólo prueba unicidad.

El valor intermedio convierte signos opuestos de una continua en existencia de raíz. La derivada positiva permite después descartar una segunda mediante Rolle o crecimiento. Son pasos lógicamente diferentes. Ausencia de derivadas nulas por sí sola no asegura que el nivel cero se alcance.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-019-061}

¿Qué cota inferior de derivada vale en $[0,1]$ para ese polinomio?

[]{#MA-MSOL-ANM-01-019-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

Uno, porque $p\prime(t)=3t^2+1\ge1$.

El cuadrado es no negativo en todo centro y por ello $3t^2+1$ es al menos uno. La barrera es global en el segmento, no una estimación basada en muestras. Valor medio la convierte en una cota inferior de incrementos. Esa cota permite traducir un residual conocido en distancia a la raíz.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-019-062}

¿Qué residuo tiene el aproximante $2/3$?

[]{#MA-MSOL-ANM-01-019-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

$p(2/3)=-1/27$; la raíz única queda a su derecha por crecimiento estricto.

Sustituir dos tercios produce $8/27+18/27-27/27=-1/27$. Como el polinomio es estrictamente creciente y en la raíz vale cero, la entrada de valor negativo queda a su izquierda. El signo del residual determina así el sentido del error. Su magnitud y una cota inferior de derivada controlarán después su tamaño.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-019-063}

¿Qué error da una cota $f\prime\ge m>0$ entre $x$ y un cero $r$?

[]{#MA-MSOL-ANM-01-019-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

$|x-r|\le|f(x)|/m$, obtenido de la cota de incrementos en ese segmento.

La raíz tiene valor cero, así la magnitud del incremento de salida entre ella y $x$ es $|f(x)|$. La barrera positiva da al menos $m|x-r|$ para ese incremento. Dividir por $m>0$ produce la cota posicional. Se necesitan las hipótesis en todo el segmento entre ambos, no sólo en el aproximante.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-019-064}

¿Qué falta cuando sólo se han muestreado unas pocas derivadas?

[]{#MA-MSOL-ANM-01-019-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

Una cota válida para todos los puntos interiores pertinentes; la tabla finita no certifica esa premisa universal.

Los valores muestreados no excluyen una pendiente menor, mayor o nula entre las muestras. El certificado de valor medio utiliza una cota válida para cualquier testigo interior posible. Esa obligación debe demostrarse mediante fórmulas o estimaciones sobre toda la región. La tabla finita por sí sola no justifica el paso de residual a distancia.

</details>

### Ejercicios de la sección 19.8

#### Ejercicio 36. Inyectividad desde Rolle

[]{#MA-EX-ANM-01-019-036}

Prueba inyectividad de una función continua y derivable interiormente en un intervalo si su derivada nunca se anula. Trata la diferencia entre igualdad de valores y cero de la función.

[]{#MA-SOL-ANM-01-019-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

Supongamos $f(x)=f(y)$ con $x<y$. Intervalaridad conserva todo $[x,y]$ en el dominio, continuidad se hereda y su interior dispone de derivadas. Rolle produce $c\in(x,y)$ con $f\prime(c)=0$, contradicción. Así entradas distintas no tienen la misma salida y la función es inyectiva. El valor repetido no necesitaba ser cero. La conclusión sólo garantiza a lo sumo una solución por nivel; existencia de una solución requiere otro dato.

</details>

#### Ejercicio 37. Contar ceros por segmentos vecinos

[]{#MA-EX-ANM-01-019-037}

Si $f'$ tiene a lo sumo k ceros en el interior de un intervalo, prueba que f tiene a lo sumo k+1 ceros distintos bajo las hipótesis de R8.

[]{#MA-SOL-ANM-01-019-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Si hubiera $k+2$ ceros distintos, ordenamos esa lista finita como $x_0<\cdots<x_{k+1}$. Cada segmento vecino cumple Rolle y entrega $c_j\in(x_j,x_{j+1})$ con $f\prime(c_j)=0$, para $j=0,\ldots,k$. Sus interiores son disjuntos, así los $k+1$ testigos son distintos y contradicen la cota $k$. Sólo se usan finitas aplicaciones, no una selección numerable de puntos. El recuento corresponde a raíces distintas y no a multiplicidades.

</details>

#### Ejercicio 38. Existencia, unicidad y primera horquilla

[]{#MA-EX-ANM-01-019-038}

Para $p(x)=x^3+x-1$ en $[0,1]$, prueba existencia y unicidad de un cero y enciérralo entre $1/2$ y $3/4$.

[]{#MA-SOL-ANM-01-019-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

El polinomio $p=x^3+x-1$ es continuo, con $p(0)=-1$ y $p(1)=1$. Valor intermedio da una raíz interior. Su derivada $p\prime(x)=3x^2+1\ge1$ no se anula, así Rolle descarta dos raíces distintas y la raíz $r$ es única. Además $p(1/2)=-3/8<0$ y $p(3/4)=11/64>0$. Valor intermedio en ese subsegmento da una raíz en $(1/2,3/4)$, que por unicidad es $r$. Existencia y localización proceden de continuidad; Rolle aporta la parte de unicidad.

</details>

#### Ejercicio 39. Un máximo de tres ceros que se alcanza

[]{#MA-EX-ANM-01-019-039}

Usa la derivada de $q(x)=x^3-3x$ para acotar sus ceros y comprueba cuántos tiene. ¿Dos ceros de $f'$ garantizan tres de f?

[]{#MA-SOL-ANM-01-019-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

Para $q=x^3-3x$, la derivada $q\prime=3x^2-3$ se anula exactamente en menos uno y uno. El recuento por Rolle limita a tres los ceros distintos de $q$. La factorización $q=x(x^2-3)$ muestra que $-\sqrt3,0,\sqrt3$ son esos tres ceros. La recíproca no vale: $Q=q+10$ en $[-2,2]$ conserva dos ceros interiores de derivada, pero $Q(-2)=8$, $Q(-1)=12$, $Q(1)=8$, $Q(2)=12$. Los signos de $Q\prime$ en las tres piezas y las reglas de orden aseguran $Q\ge8$ en todo ese dominio, sin ninguna raíz.

</details>

#### Ejercicio 40. Residuo convertido en distancia

[]{#MA-EX-ANM-01-019-040}

Para la raíz única r de E038 y el aproximante $x=2/3$, demuestra las cotas racionales $16/1161\le r-x\le4/189$.

[]{#MA-SOL-ANM-01-019-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

La raíz $r$ y $x=2/3$ están en $(1/2,3/4)$. Sustituir da $p(x)=-1/27$; el crecimiento estricto y $p(r)=0$ implican $r>x$. En el segmento entre ambos, $1/4\le t^2\le9/16$, así $7/4\le p\prime(t)\le43/16$. La cota de incrementos entrega $(7/4)(r-x)\le1/27\le(43/16)(r-x)$. Dividir por las constantes positivas produce $16/1161\le r-x\le4/189$. Las barreras de derivada se probaron para todos los centros pertinentes, sin identificar el testigo de valor medio ni usar cifras de un gráfico.

**Retorno visual.** Véase [C19-F08](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-19)

[← Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Capítulo 20 →](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html)

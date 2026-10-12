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
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C19.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-19)

Una derivada describe un centro. Este capítulo demuestra cuándo las pendientes locales gobiernan valores separados: el intervalo conserva el segmento que une dos entradas, y las hipótesis de continuidad y derivabilidad permiten encontrar una pendiente interior que transporta su incremento.

Los prerrequisitos centrales son continuidad de C14 y diferenciabilidad de C18. Se usan explícitamente los extremos alcanzados sobre segmentos compactos de C16 para Rolle y Darboux, y el valor intermedio de C15 para existencia de una raíz. Límites, acumulación, raíces y finitud son interfaces heredadas. La cadena lógica es Fermat, Rolle y valor medio, seguida de consecuencias sobre signos, cotas, dos funciones, valores intermedios de derivadas y ceros. No suponemos continuidad de la función derivada ni usamos convexidad, segunda derivada, Taylor, integrales o L’Hôpital.

## 19.1. Un extremo interior obliga a detenerse

[]{#MA-SEC-ANM-01-019-001}

Una derivada describe el comportamiento cerca de un centro. Para obtener información en un intervalo completo necesitaremos que las condiciones valgan en todos sus puntos pertinentes. El primer puente es local: una función derivable no puede alcanzar un extremo interior con pendiente distinta de cero.

**R1 — Fermat.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a$ interior a $D$. Si $f$ tiene un máximo o mínimo local en $a$ y es derivable allí, entonces $f'(a)=0$. Un mínimo local significa que existe $r>0$ tal que $f(x)\ge f(a)$ para $x\in D$ con $|x-a|<r$; un máximo invierte la desigualdad. La interioridad proporciona $\rho>0$ con $B(a,\rho)\subseteq D$, y por tanto acumulación desde ambos lados.

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

![El cuadrado tiene mínimo interior en cero y derivada cero. La identidad en \[0,1\] tiene mínimo y máximo de frontera con derivadas relativas uno. Fermat necesita interioridad o acumulación por ambos lados además de extremo y derivabilidad; las figuras no sustituyen la prueba por signos.](../../assets/books/anm/C19/C19-F01.svg){#fig-anm-c19-f01 fig-alt="El cuadrado tiene mínimo interior en cero y derivada cero. La identidad en \[0,1\] tiene mínimo y máximo de frontera con derivadas relativas uno. Fermat necesita interioridad o acumulación por ambos lados además de extremo y derivabilidad; las figuras no sustituyen la prueba por signos."}

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-019-001}

¿Qué es un mínimo local relativo?

[]{#MA-MSOL-ANM-01-019-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

**Respuesta.**

Un centro $a\in D$ y un radio donde todas las entradas del dominio tienen valores al menos $f(a)$; no se exige desigualdad fuera de ese radio.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-019-002}

¿Qué aporta interioridad a Fermat?

[]{#MA-MSOL-ANM-01-019-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

**Respuesta.**

Entradas admisibles a ambos lados del centro dentro de cualquier radio suficientemente pequeño.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-019-003}

¿Qué signo tienen las secantes a la izquierda de un mínimo?

[]{#MA-MSOL-ANM-01-019-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

**Respuesta.**

No positivo: el numerador es no negativo y el denominador negativo.

**Fundamento en la sección 19.1.**

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-019-004}

¿Qué signo tienen las secantes a la derecha de un mínimo?

[]{#MA-MSOL-ANM-01-019-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

**Respuesta.**

No negativo: tanto el numerador como el denominador son no negativos, y el segundo es positivo.

**Fundamento en la sección 19.1.**

**R1 — Fermat.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a$ interior a $D$. Si $f$ tiene un máximo o mínimo local en $a$ y es derivable allí, entonces $f'(a)=0$. Un mínimo local significa que existe $r>0$ tal que $f(x)\ge f(a)$ para $x\in D$ con $|x-a|<r$; un máximo invierte la desigualdad. La interioridad proporciona $\rho>0$ con $B(a,\rho)\subseteq D$, y por tanto acumulación desde ambos lados.

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-019-005}

¿Por qué una derivada positiva contradice un mínimo interior?

[]{#MA-MSOL-ANM-01-019-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

**Respuesta.**

Fuerza cocientes positivos cerca del centro, incluidos argumentos de la izquierda donde el mínimo exige cocientes no positivos.

**Fundamento en la sección 19.1.**

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-019-006}

¿Qué ocurre con la identidad en los bordes de $[0,1]$?

[]{#MA-MSOL-ANM-01-019-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

**Respuesta.**

Tiene extremos globales y derivadas relativas uno; los bordes no son interiores y no satisfacen la premisa geométrica de Fermat.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-019-007}

¿Pendiente cero basta para un extremo?

[]{#MA-MSOL-ANM-01-019-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

**Respuesta.**

No: el cubo tiene derivada cero en cero y valores de ambos signos arbitrariamente cerca.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-019-008}

¿Se usa valor medio para probar Fermat?

[]{#MA-MSOL-ANM-01-019-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

**Respuesta.**

No. Se emplean directamente signos de cocientes, radios de derivabilidad y entradas de ambos lados.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

### Ejercicios de la sección 19.1

[]{#ejercicios-19}

#### Ejercicio 1. Signos en un mínimo

[]{#MA-EX-ANM-01-019-001}

Prueba Fermat para un mínimo interior usando signos de secantes y dos casos para el signo de la derivada.

[]{#MA-SOL-ANM-01-019-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

**Respuesta.**

En un radio del mínimo, $f(x)-f(a)\ge0$; las secantes izquierdas son no positivas y las derechas no negativas. Interioridad da una bola dentro del dominio. Si $L>0$, la tolerancia $L/2$ fuerza pendientes positivas en algún radio: elegir $x=a-\min(r,\rho,\delta)/2$ contradice el signo izquierdo. Si $L<0$, tolerancia $|L|/2$ fuerza pendientes negativas y la entrada derecha con ese mismo mínimo contradice el signo derecho. Los radios son positivos y las entradas distintas del centro. Por tricotomía sólo queda $L=0$.

**Fundamento en la sección 19.1.**

**Estrategia y prueba para un mínimo.** En la vecindad del extremo, las pendientes secantes son no negativas a la derecha y no positivas a la izquierda. Sea $L=f'(a)$. Si $L>0$, tolerancia $L/2$ da $\delta$ con $q_{f,a}>L/2$ cerca. Tomamos $t=\min(r,\rho,\delta)/2>0$ y $x=a-t$. Este argumento pertenece al dominio, está a la izquierda y su cociente debería ser no positivo: contradicción. Si $L<0$, tolerancia $|L|/2$ fuerza $q_{f,a}<L/2<0$; el argumento explícito $x=a+t$ contradice el signo de la derecha. Sólo queda $L=0$. Para un máximo se aplica el resultado a $-f$, cuya derivada es $-L$ por C18. Se usaron dos lados y un testigo por caso, sin fabricar una sucesión.

</details>

#### Ejercicio 2. El borde no es un centro interior

[]{#MA-EX-ANM-01-019-002}

Analiza los extremos y derivadas relativas de $f(x)=x$ sobre $[0,1]$. Explica por qué no contradicen Fermat.

[]{#MA-SOL-ANM-01-019-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

El orden da mínimo global en cero y máximo global en uno. En cualquier centro acumulante del segmento el cociente perforado vale uno, también en los dos bordes, así sus derivadas relativas son uno. Cada bola centrada en cero contiene entradas negativas fuera del dominio y cada bola centrada en uno contiene entradas mayores que uno, por lo que ninguno es interior. Fermat no se aplica allí; su prueba necesita ambas clases de entradas admisibles, que faltan en los bordes.

**Retorno visual.** Véase [C19-F01](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 3. Una esquina y un punto estacionario

[]{#MA-EX-ANM-01-019-003}

Compara $|x|$, $x^2$ y $x^3$ en cero: extremo local, derivabilidad y suficiencia de pendiente nula.

[]{#MA-SOL-ANM-01-019-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

**Respuesta.**

El valor absoluto tiene mínimo global cero, pero secantes de pendientes menos uno y uno, por lo que no es derivable allí. El cuadrado tiene mínimo global y cociente centrado en cero igual a $x$, así derivada cero. El cubo tiene cociente $x^2$ y derivada cero, pero entradas positivas y negativas arbitrariamente cercanas dan valores de signos opuestos: no hay extremo local. Por tanto un extremo interior no crea derivabilidad y una derivada nula no garantiza extremo.

**Fundamento en la sección 19.1.**

**Dónde se gastan las hipótesis.** En $[0,1]$, la identidad tiene mínimo en cero y máximo en uno, pero sus derivadas relativas valen uno: son extremos de frontera. $|x|$ tiene mínimo interior en cero, pero no derivada bilateral. El cubo tiene derivada cero en cero y ningún extremo local allí. Por tanto la condición de Fermat es necesaria bajo sus hipótesis, sin ser suficiente para clasificar un punto estacionario.

Una acumulación por ambos lados basta para el argumento de signos aunque el dominio esté roto; la interioridad es una garantía simple de ella. Un centro aislado puede ser a la vez máximo y mínimo local por vacuidad, pero C18 no le asigna derivada. La gráfica ayuda a reconocer estas situaciones; la prueba se apoya en cocientes y entradas verificadas.

</details>

#### Ejercicio 4. Dos lados sin un intervalo completo

[]{#MA-EX-ANM-01-019-004}

Prueba que en Fermat puede reemplazarse interioridad por acumulación a ambos lados, manteniendo extremo local y derivada relativa existentes.

[]{#MA-SOL-ANM-01-019-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Sea $L$ la derivada relativa. Para un mínimo, las pendientes de la izquierda son no positivas y las de la derecha no negativas dentro del radio del extremo. Si $L>0$, el radio de error $L/2$ obliga a pendientes positivas; acumulación izquierda entrega una entrada dentro del mínimo de ambos radios, contradicción. Si $L<0$, acumulación derecha y error $|L|/2$ dan la contradicción opuesta. No hace falta una bola completa del dominio, sino entradas de ambos lados en todo radio. Para máximo se aplica el resultado a $-f$. No se infiere esa acumulación sólo de que el centro sea de acumulación por uno de los lados.

</details>

#### Ejercicio 5. Transformar el máximo

[]{#MA-EX-ANM-01-019-005}

Deduce Fermat para un máximo a partir del caso mínimo y verifica las condiciones de la función auxiliar.

[]{#MA-SOL-ANM-01-019-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

**Respuesta.**

Si $f$ alcanza un máximo local en $a$, la función $g=-f$ sobre el mismo dominio alcanza un mínimo local con el mismo radio. El centro sigue siendo interior y C18 da derivabilidad $g\prime(a)=-f\prime(a)$. El caso mínimo implica $g\prime(a)=0$, así $f\prime(a)=0$. La transformación conserva tipos y dominio y sólo invierte el orden de valores; no se utiliza un resultado global o valor medio.

**Fundamento en la sección 19.1.**

Una derivada describe el comportamiento cerca de un centro. Para obtener información en un intervalo completo necesitaremos que las condiciones valgan en todos sus puntos pertinentes. El primer puente es local: una función derivable no puede alcanzar un extremo interior con pendiente distinta de cero.

**R1 — Fermat.** Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a$ interior a $D$. Si $f$ tiene un máximo o mínimo local en $a$ y es derivable allí, entonces $f'(a)=0$. Un mínimo local significa que existe $r>0$ tal que $f(x)\ge f(a)$ para $x\in D$ con $|x-a|<r$; un máximo invierte la desigualdad. La interioridad proporciona $\rho>0$ con $B(a,\rho)\subseteq D$, y por tanto acumulación desde ambos lados.

</details>
## 19.2. Rolle: volver a la misma altura

[]{#MA-SEC-ANM-01-019-002}

Fermat convierte un extremo interior en una pendiente nula. Todavía falta garantizar un extremo que no esté en la frontera. Aquí entra una herramienta heredada: C16 asegura que una continua en un segmento cerrado no vacío alcanza máximo y mínimo.

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

![Para x(1−x) en \[0,1\], los bordes valen cero y el máximo interior en 1/2 tiene valor 1/4 y derivada cero. Este ejemplo tiene un único punto estacionario por la fórmula 1−2x; Rolle en general sólo garantiza existencia, sin unicidad ni un cero adicional de la función.](../../assets/books/anm/C19/C19-F02.svg){#fig-anm-c19-f02 fig-alt="Para x(1−x) en \[0,1\], los bordes valen cero y el máximo interior en 1/2 tiene valor 1/4 y derivada cero. Este ejemplo tiene un único punto estacionario por la fórmula 1−2x; Rolle en general sólo garantiza existencia, sin unicidad ni un cero adicional de la función."}

**Auditar una hipótesis a la vez.** Sin continuidad de borde, $u(x)=x$ para $0\le x<1$ y $u(1)=0$ tiene valores de borde iguales, pero derivada uno en todo el interior. Sin derivabilidad interior, $v(x)=|x-1/2|$ en $[0,1]$ tiene bordes iguales y es continua, pero ninguna derivada interior existente vale cero. Sin igualdad de borde, la identidad continua y derivable tampoco se detiene. Estos ejemplos prueban que no puede eliminarse cada condición del enunciado universal; no que las condiciones sean necesarias para toda función particular que casualmente tenga una derivada nula.

**Existencia no es selección ni unicidad.** La función constante satisface la conclusión en todos los puntos interiores. Una curva puede tener varios puntos de derivada nula. Rolle entrega al menos uno, sin elegir un punto para todos los intervalos simultáneamente. Si dos ceros de $f$ delimitan un segmento con las hipótesis, existe entre ellos un cero de $f'$; no tiene por qué ser otro cero de $f$.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-019-009}

¿Dónde se exige continuidad en Rolle?

[]{#MA-MSOL-ANM-01-019-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

**Respuesta.**

En todo $[a,b]$, incluidos sus extremos con continuidad relativa al segmento.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-019-010}

¿Dónde se exige derivabilidad en Rolle?

[]{#MA-MSOL-ANM-01-019-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

**Respuesta.**

En todos los puntos de $(a,b)$; no se piden derivadas en los bordes.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-019-011}

¿Qué herramienta asegura extremos alcanzados?

[]{#MA-MSOL-ANM-01-019-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

**Respuesta.**

El teorema de extremos sobre compactos de C16, aplicado al segmento cerrado no vacío y la función continua.

**Fundamento en la sección 19.2.**

Fermat convierte un extremo interior en una pendiente nula. Todavía falta garantizar un extremo que no esté en la frontera. Aquí entra una herramienta heredada: C16 asegura que una continua en un segmento cerrado no vacío alcanza máximo y mínimo.

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-019-012}

¿Por qué una altura mayor que la de los bordes produce un extremo interior?

[]{#MA-MSOL-ANM-01-019-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

**Respuesta.**

El máximo alcanzado tiene valor mayor que ambos valores de borde, así su punto no puede ser ninguno de ellos.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-019-013}

¿Qué punto sirve si la función es constante?

[]{#MA-MSOL-ANM-01-019-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

**Respuesta.**

El punto medio, que es interior para $a<b$; sus cocientes son cero.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-019-014}

¿Rolle exige que ambos extremos globales sean interiores?

[]{#MA-MSOL-ANM-01-019-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

**Respuesta.**

No. Basta uno interior en el caso no constante; el argumento distingue si hay valor superior o inferior al de los bordes.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-019-015}

¿Un cero de la derivada entre dos ceros es necesariamente otro cero de la función?

[]{#MA-MSOL-ANM-01-019-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

**Respuesta.**

No. Por ejemplo, $x(1-x)$ tiene ceros en cero y uno y derivada cero en un medio, donde su valor es un cuarto.

**Fundamento en la sección 19.2.**

**Auditar una hipótesis a la vez.** Sin continuidad de borde, $u(x)=x$ para $0\le x<1$ y $u(1)=0$ tiene valores de borde iguales, pero derivada uno en todo el interior. Sin derivabilidad interior, $v(x)=|x-1/2|$ en $[0,1]$ tiene bordes iguales y es continua, pero ninguna derivada interior existente vale cero. Sin igualdad de borde, la identidad continua y derivable tampoco se detiene. Estos ejemplos prueban que no puede eliminarse cada condición del enunciado universal; no que las condiciones sean necesarias para toda función particular que casualmente tenga una derivada nula.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-019-016}

¿La conclusión de Rolle identifica un punto único?

[]{#MA-MSOL-ANM-01-019-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

**Respuesta.**

No. Asegura al menos uno, y las constantes satisfacen la igualdad en todos los puntos interiores.

**Fundamento en la sección 19.2.**

**Existencia no es selección ni unicidad.** La función constante satisface la conclusión en todos los puntos interiores. Una curva puede tener varios puntos de derivada nula. Rolle entrega al menos uno, sin elegir un punto para todos los intervalos simultáneamente. Si dos ceros de $f$ delimitan un segmento con las hipótesis, existe entre ellos un cero de $f'$; no tiene por qué ser otro cero de $f$.

</details>

### Ejercicios de la sección 19.2

#### Ejercicio 6. Localizar un extremo interior

[]{#MA-EX-ANM-01-019-006}

Si una continua en $[a,b]$ tiene bordes iguales $k$ y algún valor distinto, prueba que alcanza un extremo global interior.

[]{#MA-SOL-ANM-01-019-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

C16 entrega un máximo y un mínimo alcanzados en el segmento. Si el valor distinto es mayor que $k$, el máximo tiene valor al menos tan grande y por tanto mayor que ambos bordes; su punto no puede ser ninguno de ellos y queda en $(a,b)$. Si es menor que $k$, el mínimo queda estrictamente por debajo de ambos bordes y también es interior. Tricotomía cubre los dos casos. No se afirma que ambos extremos globales tengan esa posición ni que la función sea derivable, pues este paso sólo localiza un extremo desde continuidad.

</details>

#### Ejercicio 7. Una parábola que vuelve al borde

[]{#MA-EX-ANM-01-019-007}

Aplica Rolle a $f(x)=x(1-x)$ en $[0,1]$. Halla todos los puntos de derivada cero y comprueba si son ceros de la función.

[]{#MA-SOL-ANM-01-019-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

**Respuesta.**

El polinomio es continuo y derivable, con bordes cero. C18 da $f\prime(x)=1-2x$, que sólo se anula en $c=1/2$, interior al segmento. Su valor es $1/4$, no cero. Rolle predice existencia de un cero de la derivada entre los dos ceros de la función y en este ejemplo es único por la ecuación explícita; no predice un tercer cero de la función.

**Retorno visual.** Véase [C19-F02](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 19.2.**

**R2 — Rolle.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo el segmento, derivable en cada punto de $(a,b)$, con $f(a)=f(b)$. Entonces existe $c\in(a,b)$ tal que $f'(c)=0$. La continuidad en los extremos es relativa al segmento; no se piden derivadas allí ni continuidad de la función derivada.

**Metas y prueba.** Escribamos $k=f(a)=f(b)$. Si todos los valores son $k$, elegimos $c=(a+b)/2$ y sus cocientes son cero. Si no, existe $y$ con $f(y)\ne k$. Los extremos alcanzados de C16 son $m,M\in[a,b]$ con $f(m)\le f(x)\le f(M)$ para todo $x$ del segmento. Si $f(y)>k$, entonces $f(M)>k$ y $M$ no puede ser ninguno de los bordes; Fermat en $M$ da la conclusión. Si $f(y)<k$, el mínimo $m$ es interior y Fermat se aplica allí. La continuidad asegura extremos alcanzados; la igualdad de borde desplaza al menos uno al interior; la derivabilidad permite detener su pendiente. No se supone que los dos extremos sean interiores.

</details>

#### Ejercicio 8. Perder continuidad en un borde

[]{#MA-EX-ANM-01-019-008}

Para $u(x)=x$ si $0\le x<1$ y $u(1)=0$, audita Rolle en $[0,1]$ y prueba que la continuidad interior no basta.

[]{#MA-SOL-ANM-01-019-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

**Respuesta.**

Los bordes valen cero. Cada punto interior tiene una vecindad donde $u$ es identidad, por lo que su derivada es uno y nunca cero. En uno, las entradas $1-1/(n+2)$ tienen salidas tendentes a uno, distintas del valor cero; no hay continuidad relativa. Se cumplen derivabilidad interior e igualdad de borde, pero falla precisamente continuidad del segmento cerrado. La hipótesis interior por sí sola no garantiza los extremos alcanzados necesarios para la prueba de Rolle.

**Fundamento en la sección 19.2.**

**Auditar una hipótesis a la vez.** Sin continuidad de borde, $u(x)=x$ para $0\le x<1$ y $u(1)=0$ tiene valores de borde iguales, pero derivada uno en todo el interior. Sin derivabilidad interior, $v(x)=|x-1/2|$ en $[0,1]$ tiene bordes iguales y es continua, pero ninguna derivada interior existente vale cero. Sin igualdad de borde, la identidad continua y derivable tampoco se detiene. Estos ejemplos prueban que no puede eliminarse cada condición del enunciado universal; no que las condiciones sean necesarias para toda función particular que casualmente tenga una derivada nula.

</details>

#### Ejercicio 9. Omitir la derivabilidad

[]{#MA-EX-ANM-01-019-009}

Analiza Rolle para $|x-1/2|$ en $[0,1]$ y contrasta con eliminar igualdad de borde en la identidad.

[]{#MA-SOL-ANM-01-019-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

La función de valor absoluto trasladada es continua y tiene valores $1/2$ en ambos bordes. A la izquierda de un medio su derivada es menos uno y a la derecha uno; en un medio no existe. Así no hay ninguna derivada interior nula y falla derivabilidad en todo el interior. Para la identidad, continuidad y derivabilidad se cumplen pero los bordes cero y uno son diferentes y su derivada siempre vale uno. Los ejemplos eliminan una sola hipótesis cada vez y muestran que no puede omitirse del enunciado universal.

</details>

#### Ejercicio 10. Muchos puntos posibles

[]{#MA-EX-ANM-01-019-010}

Explica por qué Rolle no da unicidad ni una selección simultánea. Trata una función constante y el segmento degenerado.

[]{#MA-SOL-ANM-01-019-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

**Respuesta.**

En una constante sobre un segmento no degenerado todas las pendientes interiores son cero, por lo que cualquier punto interior sirve. La conclusión existencial no designa uno de ellos; su uso fija una función y un segmento y toma un testigo para esa instancia. Para $a=b$, el interior es vacío y no podría existir tal punto, aunque la igualdad de borde sea automática. Por eso se exige $a<b$. Ninguna de estas conclusiones construye un selector para una familia infinita de intervalos.

**Fundamento en la sección 19.2.**

**Existencia no es selección ni unicidad.** La función constante satisface la conclusión en todos los puntos interiores. Una curva puede tener varios puntos de derivada nula. Rolle entrega al menos uno, sin elegir un punto para todos los intervalos simultáneamente. Si dos ceros de $f$ delimitan un segmento con las hipótesis, existe entre ellos un cero de $f'$; no tiene por qué ser otro cero de $f$.

</details>
## 19.3. Restar la secante para encontrar una tangente

[]{#MA-SEC-ANM-01-019-003}

Una curva que termina a otra altura no cumple la igualdad de bordes de Rolle. Restar la recta secante transforma el problema en uno que sí vuelve a la misma altura.

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

![En \[1,3\], la secante del cuadrado tiene pendiente cuatro y recta 4x−3. La tangente en dos tiene igual pendiente. Restar la secante da H=(x−1)(x−3), con bordes cero y H′(2)=0. El punto medio funciona aquí por el cuadrado; no es un punto prescrito por el teorema general.](../../assets/books/anm/C19/C19-F03.svg){#fig-anm-c19-f03 fig-alt="En \[1,3\], la secante del cuadrado tiene pendiente cuatro y recta 4x−3. La tangente en dos tiene igual pendiente. Restar la secante da H=(x−1)(x−3), con bordes cero y H′(2)=0. El punto medio funciona aquí por el cuadrado; no es un punto prescrito por el teorema general."}

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

Si $a=b$, la expresión secante divide por cero y el interior es vacío: ese caso no se incorpora al enunciado. Las hipótesis son las de Rolle salvo la igualdad de borde; se conservan los contraejemplos de continuidad o derivabilidad omitidas. La igualdad es exacta para algún punto, aunque no conozcamos cuál.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-019-017}

¿Qué pendiente se resta en la prueba de Lagrange?

[]{#MA-MSOL-ANM-01-019-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

**Respuesta.**

La pendiente secante $m=[f(b)-f(a)]/(b-a)$, fijada antes del argumento variable.

**Fundamento en la sección 19.3.**

Una curva que termina a otra altura no cumple la igualdad de bordes de Rolle. Restar la recta secante transforma el problema en uno que sí vuelve a la misma altura.

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-019-018}

¿Qué función tiene bordes cero?

[]{#MA-MSOL-ANM-01-019-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

**Respuesta.**

$H(x)=f(x)-f(a)-m(x-a)$ en el mismo segmento.

**Fundamento en la sección 19.3.**

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-019-019}

¿Cuánto vale $H\prime$ en el interior?

[]{#MA-MSOL-ANM-01-019-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

**Respuesta.**

$f\prime-m$, por la regla algebraica de C18.

**Fundamento en la sección 19.3.**

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-019-020}

¿Qué convierte Rolle en la igualdad de valor medio?

[]{#MA-MSOL-ANM-01-019-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

**Respuesta.**

$H\prime(c)=0$ implica $f\prime(c)=m$ para algún centro interior.

**Fundamento en la sección 19.3.**

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

Si $a=b$, la expresión secante divide por cero y el interior es vacío: ese caso no se incorpora al enunciado. Las hipótesis son las de Rolle salvo la igualdad de borde; se conservan los contraejemplos de continuidad o derivabilidad omitidas. La igualdad es exacta para algún punto, aunque no conozcamos cuál.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-019-021}

¿Por qué no se admite $a=b$?

[]{#MA-MSOL-ANM-01-019-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

**Respuesta.**

La secante dividiría por cero y el interior sería vacío.

**Fundamento en la sección 19.3.**

Si $a=b$, la expresión secante divide por cero y el interior es vacío: ese caso no se incorpora al enunciado. Las hipótesis son las de Rolle salvo la igualdad de borde; se conservan los contraejemplos de continuidad o derivabilidad omitidas. La igualdad es exacta para algún punto, aunque no conozcamos cuál.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-019-022}

¿Qué debe comprobarse antes de restringir al par $u<v$?

[]{#MA-MSOL-ANM-01-019-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

**Respuesta.**

Que todo $[u,v]$ está en el dominio, con continuidad sobre él y derivabilidad en su interior.

**Fundamento en la sección 19.3.**

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-019-023}

¿El punto de valor medio del cubo en $[0,1]$ es un medio?

[]{#MA-MSOL-ANM-01-019-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

**Respuesta.**

No. Es $1/\sqrt3$, porque $3c^2=1$ y $c>0$.

**Fundamento en la sección 19.3.**

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

Si $a=b$, la expresión secante divide por cero y el interior es vacío: ese caso no se incorpora al enunciado. Las hipótesis son las de Rolle salvo la igualdad de borde; se conservan los contraejemplos de continuidad o derivabilidad omitidas. La igualdad es exacta para algún punto, aunque no conozcamos cuál.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-019-024}

¿Hace falta continuidad de $f\prime$?

[]{#MA-MSOL-ANM-01-019-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

**Respuesta.**

No. Las hipótesis requieren continuidad de $f$ y existencia de sus derivadas interiores.

**Fundamento en la sección 19.3.**

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

</details>

### Ejercicios de la sección 19.3

#### Ejercicio 11. Construir el residuo de la secante

[]{#MA-EX-ANM-01-019-011}

Construye la función auxiliar de Lagrange y verifica todas las hipótesis de Rolle antes de aplicarlo.

[]{#MA-SOL-ANM-01-019-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

**Respuesta.**

Con $a<b$, $m=[f(b)-f(a)]/(b-a)$ es real. La recta $\ell(x)=f(a)+m(x-a)$ comparte los valores de borde y $H=f-\ell$ vive en $[a,b]$. Continuidad de $f$ y de la recta hace continua $H$ en todo el segmento; C18 da derivada $H\prime=f\prime-m$ en su interior. Ambos bordes de $H$ valen cero. Rolle entrega $c$ interior con $H\prime(c)=0$, y la identidad de derivadas implica $f\prime(c)=m$. No se ha aplicado Rolle directamente a $f$, cuyos bordes pueden ser distintos.

**Fundamento en la sección 19.3.**

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

</details>

#### Ejercicio 12. Tangente paralela en el cuadrado

[]{#MA-EX-ANM-01-019-012}

Halla el punto de Lagrange para $x^2$ en $[1,3]$ y calcula la función auxiliar que resta la secante.

[]{#MA-SOL-ANM-01-019-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

**Respuesta.**

La pendiente secante es $(9-1)/(3-1)=4$. La recta es $\ell(x)=1+4(x-1)=4x-3$. El residuo $H(x)=x^2-4x+3=(x-1)(x-3)$ tiene ambos bordes cero y derivada $2x-4$. Se anula sólo en $c=2$, interior al segmento; allí la derivada original vale cuatro. La igualdad de pendientes se verifica exactamente, sin localizar el punto leyendo una figura.

**Retorno visual.** Véase [C19-F03](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 19.3.**

Una curva que termina a otra altura no cumple la igualdad de bordes de Rolle. Restar la recta secante transforma el problema en uno que sí vuelve a la misma altura.

**R3 — Valor medio de Lagrange.** Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en el segmento y derivable en su interior. Existe $c\in(a,b)$ con
$$f'(c)=\frac{f(b)-f(a)}{b-a},\qquad f(b)-f(a)=f'(c)(b-a).$$
**Objeto auxiliar y prueba.** El incremento de entrada $b-a$ es positivo. Definimos el número $m=[f(b)-f(a)]/(b-a)$, la recta $\ell(x)=f(a)+m(x-a)$ y $H(x)=f(x)-\ell(x)$ sobre el mismo segmento. Por C14/C18, $H$ es continua en todo él, derivable dentro y $H'(x)=f'(x)-m$. Además $H(a)=H(b)=0$. Rolle aplicado a $H$ da $H'(c)=0$, por lo que $f'(c)=m$. La recta auxiliar tiene pendiente fijada por los dos bordes y su resta elimina exactamente el desnivel. Lo que se anula en los bordes es $H$, no necesariamente $f$.

</details>

#### Ejercicio 13. El punto medio no es universal

[]{#MA-EX-ANM-01-019-013}

Una aplicación de Lagrange al cubo en $[0,1]$ usa automáticamente $c=1/2$. Corrígela y explica el origen del error.

[]{#MA-SOL-ANM-01-019-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

**Respuesta.**

El incremento de valores y el de entrada son uno, así la pendiente secante es uno. La derivada del cubo es $3c^2$; en un medio vale $3/4$, por lo que no cumple la igualdad. Resolver $3c^2=1$ y exigir $c\in(0,1)$ da $c=1/\sqrt3$. El punto medio funciona para el cuadrado por su fórmula específica, sin ser un dato del teorema. Lagrange asegura existencia interior, no una localización predeterminada.

**Fundamento en la sección 19.3.**

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

</details>

#### Ejercicio 14. Restringir sin llenar un hueco

[]{#MA-EX-ANM-01-019-014}

Explica qué se necesita para aplicar Lagrange a $f:D\to\mathbb R$ entre $u<v$. Usa un dominio de dos piezas para refutar que basten los extremos.

[]{#MA-SOL-ANM-01-019-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

**Respuesta.**

Hace falta $[u,v]\subseteq D$, continuidad en ese segmento y derivabilidad en su interior. La restricción conserva continuidad y, porque cada centro interior acumula en el segmento, también las derivadas originales. En $D=[0,1]\cup[2,3]$, tomar $u=1,v=2$ sólo da dos argumentos válidos y no una función definida en $(1,2)$. La función cero en la primera pieza y uno en la segunda tiene todas sus derivadas relativas cero, mientras la secante entre esos bordes tiene pendiente uno. Lagrange no se aplica: falta su dominio intervalar completo.

**Fundamento en la sección 19.3.**

**Restricciones verificadas.** Para una función original $f:D\to\mathbb R$, sólo se aplica el resultado al par $u<v$ si $[u,v]\subseteq D$, con continuidad en ese segmento y derivabilidad dentro. La restricción a $[u,v]$ conserva continuidad por C14 y derivadas en puntos interiores por C18, porque todos ellos acumulan en el segmento. Así la conclusión usa las derivadas de la función original. Tener sólo los dos extremos en $D$ no basta si falta el segmento entre ellos.

**El punto no es predeterminado.** Para $x^2$ en $[a,b]$, la pendiente secante es $a+b$, de modo que el único punto es $(a+b)/2$. Para $x^3$ en $[0,1]$, la pendiente es uno y la igualdad $3c^2=1$ da $c=1/\sqrt3$, que es interior y no el punto medio. Para una afín, cualquier punto interior sirve. El teorema no promete una receta para localizar el punto en una función arbitraria, ni que un mismo punto sirva para dos funciones distintas.

</details>

#### Ejercicio 15. Igualdad sin continuidad de derivada

[]{#MA-EX-ANM-01-019-015}

Explica si Lagrange se aplica a la función de bultos de C18 en un segmento cerrado que cruce cero, aunque su derivada sea discontinua allí.

[]{#MA-SOL-ANM-01-019-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

C18 demuestra que F es derivable en toda la recta y por tanto continua en cada punto. Su restricción al segmento es continua, y las derivadas de los centros interiores se conservan. Así Lagrange entrega un punto donde la derivada coincide con la pendiente secante. La discontinuidad de $F'$ en cero no elimina ninguna hipótesis del teorema, porque sólo se exige existencia de las derivadas interiores. No se afirma que el punto de valor medio sea cero o que pueda identificarse por una muestra de bultos.

</details>
## 19.4. El intervalo convierte signos en orden

[]{#MA-SEC-ANM-01-019-004}

Ahora sí podemos transformar signos en comparaciones entre dos entradas cualesquiera. El segmento que une esas entradas es el lugar donde se transporta la información.

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

**Recíproca con alcance.** Si $f$ es no decreciente y tiene derivada en un punto interior $a$, todos sus cocientes centrados allí son no negativos: a la derecha ambos incrementos son no negativos, a la izquierda ambos son no positivos. Un límite negativo sería contradicho por tolerancia $|L|/2$ y un argumento suficientemente cercano. Por tanto $f'(a)\ge0$. La estricta monotonía no fuerza $f'(a)>0$: $x^3$ es estrictamente creciente y $f'(0)=0$. Para justificar su crecimiento directamente, si $x<y$,
$$y^3-x^3=(y-x)(x^2+xy+y^2)>0,$$
pues $x^2+xy+y^2=(x+y/2)^2+3y^2/4$ sólo se anula con $x=y=0$, imposible para ese par.

![En un intervalo, continuidad y derivada interior cero fuerzan constancia por Lagrange. En \[0,1\]∪\[2,3\], la función cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto, incluidos bordes, pero no es constante en todo el dominio. El hueco no se rellena y el valor medio no se aplica a través de él.](../../assets/books/anm/C19/C19-F04.svg){#fig-anm-c19-f04 fig-alt="En un intervalo, continuidad y derivada interior cero fuerzan constancia por Lagrange. En \[0,1\]∪\[2,3\], la función cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto, incluidos bordes, pero no es constante en todo el dominio. El hueco no se rellena y el valor medio no se aplica a través de él."}

**Derivada nula y constantes.** Si $f'=0$ en todo el interior, R3 aplicado a cada par prueba que $f$ es constante en $I$. La recíproca sigue de cocientes cero. Si $f'=g'$ bajo las mismas condiciones, $f-g$ tiene derivada cero y es constante: $f(x)-g(x)$ no depende de $x$. Un valor común en un centro fija esa constante en cero.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-019-025}

¿Qué propiedad del dominio conecta dos entradas por Lagrange?

[]{#MA-MSOL-ANM-01-019-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

**Respuesta.**

Ser un intervalo: todo el segmento entre las entradas pertenece al dominio.

**Fundamento en la sección 19.4.**

Ahora sí podemos transformar signos en comparaciones entre dos entradas cualesquiera. El segmento que une esas entradas es el lugar donde se transporta la información.

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-019-026}

¿Qué conclusión da $f\prime\ge0$ en el interior?

[]{#MA-MSOL-ANM-01-019-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

**Respuesta.**

Que $f$ es no decreciente, si también se verifican continuidad en el intervalo y derivabilidad interior.

**Fundamento en la sección 19.4.**

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-019-027}

¿Qué condición suficiente da crecimiento estricto?

[]{#MA-MSOL-ANM-01-019-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

**Respuesta.**

$f\prime>0$ en todo el interior bajo las mismas hipótesis de intervalo y continuidad.

**Fundamento en la sección 19.4.**

**Derivada nula y constantes.** Si $f'=0$ en todo el interior, R3 aplicado a cada par prueba que $f$ es constante en $I$. La recíproca sigue de cocientes cero. Si $f'=g'$ bajo las mismas condiciones, $f-g$ tiene derivada cero y es constante: $f(x)-g(x)$ no depende de $x$. Un valor común en un centro fija esa constante en cero.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-019-028}

¿Una función estrictamente creciente tiene siempre derivada positiva?

[]{#MA-MSOL-ANM-01-019-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

**Respuesta.**

No: el cubo es estrictamente creciente y su derivada vale cero en el origen.

**Fundamento en la sección 19.4.**

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-019-029}

¿Qué da derivada idénticamente cero en un intervalo?

[]{#MA-MSOL-ANM-01-019-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

**Respuesta.**

Constancia, por aplicar valor medio a cada par; se conserva continuidad en extremos incluidos.

**Fundamento en la sección 19.4.**

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-019-030}

¿Qué da igualdad de dos derivadas en el interior?

[]{#MA-MSOL-ANM-01-019-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

**Respuesta.**

La diferencia de las funciones es constante sobre el intervalo, bajo sus condiciones de continuidad.

**Fundamento en la sección 19.4.**

**Derivada nula y constantes.** Si $f'=0$ en todo el interior, R3 aplicado a cada par prueba que $f$ es constante en $I$. La recíproca sigue de cocientes cero. Si $f'=g'$ bajo las mismas condiciones, $f-g$ tiene derivada cero y es constante: $f(x)-g(x)$ no depende de $x$. Un valor común en un centro fija esa constante en cero.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-019-031}

¿Qué falla para constantes diferentes en dos piezas separadas?

[]{#MA-MSOL-ANM-01-019-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

**Respuesta.**

No existe el segmento completo entre puntos de piezas distintas, así el valor medio no permite comparar sus constantes.

**Fundamento en la sección 19.4.**

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-019-032}

¿Se selecciona un punto $c$ para todos los pares a la vez?

[]{#MA-MSOL-ANM-01-019-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

**Respuesta.**

No. Se fija un par arbitrario y se usa la existencia de un punto para esa instancia.

**Fundamento en la sección 19.4.**

**Derivada nula y constantes.** Si $f'=0$ en todo el interior, R3 aplicado a cada par prueba que $f$ es constante en $I$. La recíproca sigue de cocientes cero. Si $f'=g'$ bajo las mismas condiciones, $f-g$ tiene derivada cero y es constante: $f(x)-g(x)$ no depende de $x$. Un valor común en un centro fija esa constante en cero.

En $D=[0,1]\cup[2,3]$, la función que vale cero en la primera pieza y uno en la segunda tiene derivada relativa cero en cada punto del dominio, pero no es constante en $D$. No se puede aplicar R3 entre uno y dos porque falta $(1,2)$. Similarmente, derivadas positivas en piezas separadas no ordenan automáticamente salidas a través del hueco. Si se incluye una frontera con salto de valor, derivabilidad en todo el interior tampoco basta para concluir constancia o monotonía en el dominio completo.

</details>

### Ejercicios de la sección 19.4

#### Ejercicio 16. Del signo a cada par

[]{#MA-EX-ANM-01-019-016}

Prueba que $f\prime\ge0$ en el interior de un intervalo, con continuidad de $f$ y derivabilidad interior, implica que $f$ es no decreciente.

[]{#MA-SOL-ANM-01-019-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

**Respuesta.**

Fijamos $x<y$ de I. El intervalo contiene todo $[x,y]$ y su interior está en el de I. La restricción es continua y derivable donde corresponde. Lagrange da algún $c\in(x,y)$ con $f(y)-f(x)=f\prime(c)(y-x)$. Como la derivada es no negativa y el incremento positivo, la diferencia es no negativa. Para todo par ordenado se obtiene $f(x)\le f(y)$, sin necesitar un mismo punto c para todos los pares o continuidad de la derivada.

**Fundamento en la sección 19.4.**

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

</details>

#### Ejercicio 17. Crecimiento estricto con una derivada nula

[]{#MA-EX-ANM-01-019-017}

Prueba que el cubo es estrictamente creciente y tiene derivada nula en cero. ¿Qué recíproca se refuta?

[]{#MA-SOL-ANM-01-019-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

**Respuesta.**

Para $x<y$, la diferencia es $(y-x)(x^2+xy+y^2)$. El primer factor es positivo y el segundo es $(x+y/2)^2+3y^2/4$, no negativo y sólo cero si $x=y=0$, imposible aquí. La diferencia es positiva. C18 da derivada $3x^2$, cero en el origen. Se refuta que crecimiento estricto implique derivada estrictamente positiva en cada punto; la conclusión necesaria donde existe es sólo no negatividad.

**Fundamento en la sección 19.4.**

**Recíproca con alcance.** Si $f$ es no decreciente y tiene derivada en un punto interior $a$, todos sus cocientes centrados allí son no negativos: a la derecha ambos incrementos son no negativos, a la izquierda ambos son no positivos. Un límite negativo sería contradicho por tolerancia $|L|/2$ y un argumento suficientemente cercano. Por tanto $f'(a)\ge0$. La estricta monotonía no fuerza $f'(a)>0$: $x^3$ es estrictamente creciente y $f'(0)=0$. Para justificar su crecimiento directamente, si $x<y$,
$$y^3-x^3=(y-x)(x^2+xy+y^2)>0,$$
pues $x^2+xy+y^2=(x+y/2)^2+3y^2/4$ sólo se anula con $x=y=0$, imposible para ese par.

</details>

#### Ejercicio 18. Derivadas iguales, valores fijados

[]{#MA-EX-ANM-01-019-018}

Sean f,g continuas en un intervalo y derivables en su interior, con derivadas iguales. Prueba que su diferencia es constante y determina qué ocurre si coinciden en un punto.

[]{#MA-SOL-ANM-01-019-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

**Respuesta.**

H=f-g es continua y derivable en el mismo dominio con $H'$=0. Para cualesquiera x<y, Lagrange en su segmento da H(y)-H(x)=$H'(c)$(y-x)=0. Los pares iguales son triviales y los inversos se intercambian, así H es constante. Si f(a)=g(a) en algún a del intervalo, H(a)=0 identifica esa constante y las funciones coinciden en todo el dominio. No se necesita integrar ni introducir una primitiva.

**Fundamento en la sección 19.4.**

Ahora sí podemos transformar signos en comparaciones entre dos entradas cualesquiera. El segmento que une esas entradas es el lugar donde se transporta la información.

**R4 — Monotonía en un intervalo.** Sea $I\subseteq\mathbb R$ un intervalo no degenerado y $f:I\to\mathbb R$ continua en $I$, derivable en $\operatorname{int}(I)$. Si $f'\ge0$ en el interior, $f$ es no decreciente. Si $f'>0$ en el interior, es estrictamente creciente. Las desigualdades opuestas dan los resultados decrecientes.

**Prueba y gasto de la geometría.** Fijados $x<y$ de $I$, su carácter intervalar garantiza $[x,y]\subseteq I$. C18 conserva las derivadas interiores al restringir. R3 entrega algún $c\in(x,y)$ con $f(y)-f(x)=f'(c)(y-x)$. El segundo factor es positivo, así el signo del primero es el de $f'(c)$; si la cota era débil, la comparación es débil. Los puntos $c$ pueden depender del par: no se selecciona una familia de ellos. En intervalos abiertos, la continuidad ya sigue de la diferenciabilidad en cada punto por C18; en extremos incluidos debe conservarse explícitamente.

</details>

#### Ejercicio 19. Constantes distintas en un dominio roto

[]{#MA-EX-ANM-01-019-019}

Construye una función con derivada relativa cero en todos los puntos de $[0,1]\cup[2,3]$ que no sea constante. Revisa también los bordes.

[]{#MA-SOL-ANM-01-019-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Ponemos f=0 en la primera pieza y f=1 en la segunda. Cada punto tiene una vecindad relativa que sólo toca su pieza y allí todos los valores son iguales, así el cociente perforado es cero. Todos los puntos, incluidos los cuatro bordes, acumulan en el dominio por al menos un lado, por lo que las derivadas relativas existen y valen cero. Sin embargo f(0)=0 y f(2)=1. El segmento entre piezas falta; la conclusión de constancia requiere el intervalo, no sólo derivabilidad en todos los puntos válidos.

**Retorno visual.** Véase [C19-F04](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 20. Signo de una derivada existente

[]{#MA-EX-ANM-01-019-020}

Si una función es no decreciente y tiene derivada en un punto interior a su intervalo, prueba que esa derivada es no negativa sin aplicar Lagrange.

[]{#MA-SOL-ANM-01-019-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

**Respuesta.**

Todos los cocientes perforados centrados en a son no negativos: a la derecha numerador y denominador son no negativos; a la izquierda ambos son no positivos y el denominador es negativo. Si el límite L fuera negativo, tolerancia |L|/2 obligaría a cocientes menores que L/2<0 en un radio. Acumulación en el centro proporciona un argumento perforado dentro de él, contradicción. Sólo se usan orden y definición de derivada; no se deriva existencia de la pendiente desde monotonía.

**Fundamento en la sección 19.4.**

**Recíproca con alcance.** Si $f$ es no decreciente y tiene derivada en un punto interior $a$, todos sus cocientes centrados allí son no negativos: a la derecha ambos incrementos son no negativos, a la izquierda ambos son no positivos. Un límite negativo sería contradicho por tolerancia $|L|/2$ y un argumento suficientemente cercano. Por tanto $f'(a)\ge0$. La estricta monotonía no fuerza $f'(a)>0$: $x^3$ es estrictamente creciente y $f'(0)=0$. Para justificar su crecimiento directamente, si $x<y$,
$$y^3-x^3=(y-x)(x^2+xy+y^2)>0,$$
pues $x^2+xy+y^2=(x+y/2)^2+3y^2/4$ sólo se anula con $x=y=0$, imposible para ese par.

</details>
## 19.5. De cotas de derivadas a cotas de incrementos

[]{#MA-SEC-ANM-01-019-005}

Aunque el punto de valor medio sea desconocido, una cota válida para todas las derivadas pertinentes también vale para la derivada de ese punto. Esto convierte existencia en un certificado cuantitativo.

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

![Para el cubo en \[1,2\], 3≤f′≤12 en el interior. R5 da 3(y−x)≤f(y)−f(x)≤12(y−x) para cualquier par ordenado. El panel derecho representa el caso de centro uno, con bandas 1+3(x−1) y 1+12(x−1). Las fórmulas prueban las cotas universales; un muestreo de la derivada no bastaría.](../../assets/books/anm/C19/C19-F05.svg){#fig-anm-c19-f05 fig-alt="Para el cubo en \[1,2\], 3≤f′≤12 en el interior. R5 da 3(y−x)≤f(y)−f(x)≤12(y−x) para cualquier par ordenado. El panel derecho representa el caso de centro uno, con bandas 1+3(x−1) y 1+12(x−1). Las fórmulas prueban las cotas universales; un muestreo de la derivada no bastaría."}

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

**Lo inverso.** Si $f$ satisface una cota Lipschitz $L$ y existe $f'(a)$ en un centro acumulante, cada cociente perforado tiene magnitud a lo sumo $L$. C13 conserva la cota en el límite, así $|f'(a)|\le L$. La existencia no se deduce: el valor absoluto es Lipschitz y falla derivabilidad en cero. Unas pocas pendientes muestreadas tampoco demuestran una cota que deba valer en todos los centros.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-019-033}

¿Qué desigualdad producen $m\le f\prime\le M$?

[]{#MA-MSOL-ANM-01-019-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

**Respuesta.**

Para $x<y$, $m(y-x)\le f(y)-f(x)\le M(y-x)$ bajo las hipótesis del intervalo.

**Fundamento en la sección 19.5.**

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-019-034}

¿Por qué no se invierte el orden al multiplicar?

[]{#MA-MSOL-ANM-01-019-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

**Respuesta.**

El incremento de entrada $y-x$ es positivo.

**Fundamento en la sección 19.5.**

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-019-035}

¿Qué controla una cota $|f\prime|\le L$?

[]{#MA-MSOL-ANM-01-019-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

**Respuesta.**

Todos los pares: $|f(y)-f(x)|\le L|y-x|$, sin exigir continuidad de la derivada.

**Fundamento en la sección 19.5.**

Aunque el punto de valor medio sea desconocido, una cota válida para todas las derivadas pertinentes también vale para la derivada de ese punto. Esto convierte existencia en un certificado cuantitativo.

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-019-036}

¿Cómo se trata $L=0$?

[]{#MA-MSOL-ANM-01-019-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

**Respuesta.**

La función es constante y cualquier radio prueba uniformidad; no se divide por cero.

**Fundamento en la sección 19.5.**

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-019-037}

¿Qué radio uniforme da $L>0$?

[]{#MA-MSOL-ANM-01-019-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

**Respuesta.**

$\varepsilon/L$, a partir del control Lipschitz de todos los pares.

**Fundamento en la sección 19.5.**

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-019-038}

¿Qué cota funciona para el cubo en $[-A,A]$?

[]{#MA-MSOL-ANM-01-019-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

**Respuesta.**

$L=3A^2$, pues su derivada es $3t^2$.

**Fundamento en la sección 19.5.**

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-019-039}

¿Lipschitz implica existencia de derivada en cada punto?

[]{#MA-MSOL-ANM-01-019-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

**Respuesta.**

No. Sólo acota las derivadas donde existen; $|x|$ tiene cota Lipschitz uno y no es derivable en cero.

**Fundamento en la sección 19.5.**

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

**Lo inverso.** Si $f$ satisface una cota Lipschitz $L$ y existe $f'(a)$ en un centro acumulante, cada cociente perforado tiene magnitud a lo sumo $L$. C13 conserva la cota en el límite, así $|f'(a)|\le L$. La existencia no se deduce: el valor absoluto es Lipschitz y falla derivabilidad en cero. Unas pocas pendientes muestreadas tampoco demuestran una cota que deba valer en todos los centros.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-019-040}

¿Basta la derivada en un centro para acotar las derivadas vecinas?

[]{#MA-MSOL-ANM-01-019-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

**Respuesta.**

No. La cota sobre otros centros es una hipótesis adicional, distinta del error normalizado de C18.

**Fundamento en la sección 19.5.**

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

</details>

### Ejercicios de la sección 19.5

#### Ejercicio 21. Dos cotas de incrementos

[]{#MA-EX-ANM-01-019-021}

Deriva las cotas $m(y-x)\le f(y)-f(x)\le M(y-x)$ desde cotas de derivada en un intervalo. Indica cómo tratar pares no ordenados para una cota absoluta.

[]{#MA-SOL-ANM-01-019-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

**Respuesta.**

Para x<y, Lagrange proporciona c interior con diferencia $f'(c)$(y-x). Sustituir m≤$f'(c)$≤M y multiplicar por y-x>0 preserva el orden. Si las cotas son -L,L, esto equivale a magnitud a lo sumo L(y-x). Para y<x se intercambian argumentos y se usa simetría de valores absolutos; para x=y ambos lados son cero. La cota final vale para todos los pares, y la continuidad en extremos incluidos permite restringir a segmentos que los contengan.

**Fundamento en la sección 19.5.**

Aunque el punto de valor medio sea desconocido, una cota válida para todas las derivadas pertinentes también vale para la derivada de ese punto. Esto convierte existencia en un certificado cuantitativo.

**R5 — Cotas de incrementos.** Bajo las condiciones de R4, si $m\le f'(t)\le M$ en $\operatorname{int}(I)$, entonces, para $x<y$ en $I$,
$$m(y-x)\le f(y)-f(x)\le M(y-x).$$
R3 entrega el valor $f'(c)$ dentro de esas cotas y multiplicar por $y-x>0$ conserva el orden. No hace falta que $f'$ sea continua ni alcance un máximo. Si $|f'|\le L$, $L\ge0$, se obtiene para todos los pares
$$|f(y)-f(x)|\le L|y-x|.$$
Para $x=y$ ambos lados son cero; si $y<x$ se intercambian las entradas. Ésta es una cota Lipschitz de pares, más fuerte que el control con un único centro de C18. Para $L>0$, el radio $\varepsilon/L$ prueba continuidad uniforme; si $L=0$, la función es constante y cualquier radio sirve.

</details>

#### Ejercicio 22. Cubo y radio común

[]{#MA-EX-ANM-01-019-022}

Da una constante Lipschitz y un radio uniforme para $x^3$ en $[-2,2]$ usando la derivada.

[]{#MA-SOL-ANM-01-019-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

La derivada es 3t², entre cero y doce para t interior. R5 da |y³-x³|≤12|y-x| para todos los pares del segmento, porque el polinomio es continuo y derivable. Para tolerancia ε>0, δ=ε/12 asegura que distancia de entrada menor que δ da error menor que ε. No se elige un radio según el centro; el mismo doce controla toda la familia de derivadas interiores. Esta prueba no afirma esa misma cota global en toda la recta.

**Retorno visual.** Véase [C19-F05](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 23. Una frontera rompe el certificado

[]{#MA-EX-ANM-01-019-023}

Para la función de E008, prueba que la derivada interior acotada por uno no da ninguna cota Lipschitz finita en todo $[0,1]$.

[]{#MA-SOL-ANM-01-019-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

**Respuesta.**

En todo el interior $u'$=1. Si un L≥0 controlara todos los pares, elegir x=(L+1)/(L+2) y y=1 daría |u(y)-u(x)|=x y |y-x|=1/(L+2). Pero x=(L+1)/(L+2)>L/(L+2)=L|y-x|, contradicción. Los dos argumentos están en el dominio y x<1. La discontinuidad en el borde impide aplicar Lagrange a esos segmentos y explica por qué la cota interior por sí sola no basta.

**Fundamento en la sección 19.5.**

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

</details>

#### Ejercicio 24. La raíz lejos de cero

[]{#MA-EX-ANM-01-019-024}

Da una constante Lipschitz para la raíz en $[1/4,4]$ y explica por qué no puede extenderse una cota finita a $[0,1]$.

[]{#MA-SOL-ANM-01-019-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

**Respuesta.**

En centros positivos la derivada es 1/(2√t), a lo sumo uno cuando t≥1/4. La función es continua en el segmento y R5 da |√y-√x|≤|y-x|. En [0,1], cualquier constante L>0 fallaría en el par cero e y positivo tan pequeño que y<min(1,1/(L+1)²), pues √y/y=1/√y>L. Para L=0 también falla cualquier y>0. La raíz sigue siendo uniforme con control no lineal de C17; falta una cota Lipschitz, sin perder continuidad uniforme.

**Fundamento en la sección 19.5.**

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

</details>

#### Ejercicio 25. Una pendiente cercana en todos los centros

[]{#MA-EX-ANM-01-019-025}

Si $|f\prime(t)-A|\le\eta$ en el interior de un segmento con centro a y extremo x, prueba error de modelo a lo sumo $\eta|x-a|$. ¿Qué dato no basta?

[]{#MA-SOL-ANM-01-019-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

**Respuesta.**

La función H(t)=f(t)-f(a)-A(t-a) es continua sobre ese segmento, derivable dentro y satisface |$H'$|≤η. Aplicar la cota de pares entre a y x, con H(a)=0, da |H(x)|≤η|x-a|. Si x=a el error es cero sin aplicación de Lagrange. Saber sólo $f'(a)$=A no acota las derivadas de los otros centros ni proporciona esa premisa universal, aunque C18 garantice un resto menor que lineal alrededor de a. El certificado se apoya en la cota adicional y no usa Taylor.

**Fundamento en la sección 19.5.**

**Primera reutilización.** Para el cubo en $[-A,A]$, $A>0$, su derivada $3t^2$ está entre cero y $3A^2$: cualquier par tiene error de salida a lo sumo $3A^2$ veces su distancia. Para la raíz en $[\alpha,\beta]$, $0<\alpha<\beta$, la derivada es $1/(2\sqrt t)$ y no supera $1/(2\sqrt\alpha)$. En $[0,1]$ no hay una constante Lipschitz finita para la raíz, como muestra el cociente $1/\sqrt y$ centrado en cero. Su continuidad uniforme de C17 permanece válida: la cota lineal es suficiente, sin ser necesaria.

**Modelo con una cota de pendiente.** Si una recta tiene pendiente $A$ y se sabe $|f'(t)-A|\le\eta$ en los puntos interiores entre $a$ y $x$, aplicamos R5 a $H(t)=f(t)-f(a)-A(t-a)$ y obtenemos
$$|f(x)-f(a)-A(x-a)|\le\eta|x-a|.$$
Hay que verificar continuidad en el segmento y derivabilidad en su interior. Una derivada conocida sólo en $a$ no suministra por sí sola una cota para las derivadas de los otros centros. Esta herramienta no afirma una tasa cuadrática ni usa Taylor o una segunda derivada.

</details>
## 19.6. Comparar dos variaciones en el mismo punto

[]{#MA-SEC-ANM-01-019-006}

Aplicar Lagrange por separado a dos funciones puede producir dos puntos diferentes. Para comparar sus variaciones en un mismo punto debemos construir una sola función auxiliar.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

![Para f=x² y g=x³ en \[0,1\], ambos incrementos valen uno y Cauchy se satisface en c=2/3. El par (g(c),f(c))=(8/27,4/9) tiene tangente de pendiente f′/g′=1, paralela a la secante de bordes. El gráfico representa el par por su argumento x, sin introducir una regla nueva para curvas. Los puntos de Lagrange separados son 1/2 y 1/√3.](../../assets/books/anm/C19/C19-F06.svg){#fig-anm-c19-f06 fig-alt="Para f=x² y g=x³ en \[0,1\], ambos incrementos valen uno y Cauchy se satisface en c=2/3. El par (g(c),f(c))=(8/27,4/9) tiene tangente de pendiente f′/g′=1, paralela a la secante de bordes. El gráfico representa el par por su argumento x, sin introducir una regla nueva para curvas. Los puntos de Lagrange separados son 1/2 y 1/√3."}

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

Si $\Delta g\ne0$ pero la derivada de $g$ se anula en algunos centros, no se puede dividir en un testigo arbitrario sin verificarlo. Con $f=g=x^3$ en $[-1,1]$, el producto cruzado vale en todos los puntos, incluido cero donde ambas derivadas son cero. Lagrange se recupera tomando $g(x)=x$, cuyo incremento $b-a$ y derivada uno son no nulos.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-019-041}

¿Qué forma de Cauchy permite incrementos nulos?

[]{#MA-MSOL-ANM-01-019-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

**Respuesta.**

La igualdad de productos cruzados $\Delta f\,g\prime(c)=\Delta g\,f\prime(c)$.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-019-042}

¿Qué coeficientes tiene la función auxiliar?

[]{#MA-MSOL-ANM-01-019-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

**Respuesta.**

Los incrementos de borde de la otra función: $\Delta g$ multiplica $f-f(a)$ y $-\Delta f$ multiplica $g-g(a)$.

**Fundamento en la sección 19.6.**

Aplicar Lagrange por separado a dos funciones puede producir dos puntos diferentes. Para comparar sus variaciones en un mismo punto debemos construir una sola función auxiliar.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-019-043}

¿Por qué sus bordes coinciden?

[]{#MA-MSOL-ANM-01-019-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

**Respuesta.**

Ambos son cero: en el primer borde se anulan las diferencias y en el segundo se cancelan los productos cruzados.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-019-044}

¿Qué condición evita todos los denominadores nulos en la forma de cocientes?

[]{#MA-MSOL-ANM-01-019-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

**Respuesta.**

$g\prime(t)\ne0$ en todo el interior; Rolle también fuerza $\Delta g\ne0$.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-019-045}

¿Por qué dos aplicaciones separadas de Lagrange no bastan?

[]{#MA-MSOL-ANM-01-019-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

**Respuesta.**

Pueden producir puntos diferentes; Cauchy necesita relacionar ambas derivadas en un mismo centro.

**Fundamento en la sección 19.6.**

Aplicar Lagrange por separado a dos funciones puede producir dos puntos diferentes. Para comparar sus variaciones en un mismo punto debemos construir una sola función auxiliar.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-019-046}

¿Qué punto sirve para $f=x^2$, $g=x^3$ en $[0,1]$?

[]{#MA-MSOL-ANM-01-019-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

**Respuesta.**

$c=2/3$, porque sus incrementos son uno y $3c^2=2c$ con $c>0$.

**Fundamento en la sección 19.6.**

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

Si $\Delta g\ne0$ pero la derivada de $g$ se anula en algunos centros, no se puede dividir en un testigo arbitrario sin verificarlo. Con $f=g=x^3$ en $[-1,1]$, el producto cruzado vale en todos los puntos, incluido cero donde ambas derivadas son cero. Lagrange se recupera tomando $g(x)=x$, cuyo incremento $b-a$ y derivada uno son no nulos.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-019-047}

¿Qué ocurre si $g$ es constante?

[]{#MA-MSOL-ANM-01-019-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

**Respuesta.**

El producto cruzado sigue siendo válido como $0=0$, pero la razón por $\Delta g$ y $g\prime$ no existe.

**Fundamento en la sección 19.6.**

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

Si $\Delta g\ne0$ pero la derivada de $g$ se anula en algunos centros, no se puede dividir en un testigo arbitrario sin verificarlo. Con $f=g=x^3$ en $[-1,1]$, el producto cruzado vale en todos los puntos, incluido cero donde ambas derivadas son cero. Lagrange se recupera tomando $g(x)=x$, cuyo incremento $b-a$ y derivada uno son no nulos.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-019-048}

¿Cómo se recupera Lagrange?

[]{#MA-MSOL-ANM-01-019-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

**Respuesta.**

Tomando $g(x)=x$, con incremento $b-a>0$ y derivada uno.

**Fundamento en la sección 19.6.**

Si $\Delta g\ne0$ pero la derivada de $g$ se anula en algunos centros, no se puede dividir en un testigo arbitrario sin verificarlo. Con $f=g=x^3$ en $[-1,1]$, el producto cruzado vale en todos los puntos, incluido cero donde ambas derivadas son cero. Lagrange se recupera tomando $g(x)=x$, cuyo incremento $b-a$ y derivada uno son no nulos.

</details>

### Ejercicios de la sección 19.6

#### Ejercicio 26. Productos cruzados antes de cocientes

[]{#MA-EX-ANM-01-019-026}

Construye la auxiliar de Cauchy y prueba la forma sin divisiones del valor medio.

[]{#MA-SOL-ANM-01-019-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

**Respuesta.**

Fijamos Δf=f(b)-f(a), Δg=g(b)-g(a), y H=Δg(f-f(a))-Δf(g-g(a)) sobre [a,b]. Sus dos bordes son cero, por cancelación de productos. Es continua y derivable donde corresponde, con $H'$=Δg $f'$-Δf $g'$, porque los coeficientes son números fijos. Rolle entrega c interior con $H'(c)$=0, que equivale a Δf $g'(c)$=Δg $f'(c)$. Cada expresión existe aunque algún incremento o derivada se anule; ningún paso dividió por ellos.

**Fundamento en la sección 19.6.**

Aplicar Lagrange por separado a dos funciones puede producir dos puntos diferentes. Para comparar sus variaciones en un mismo punto debemos construir una sola función auxiliar.

**R6 — Valor medio de Cauchy, sin divisiones.** Sean $f,g:[a,b]\to\mathbb R$, $a<b$, continuas en el segmento y derivables en su interior. Existe $c\in(a,b)$ con
$$[f(b)-f(a)]g'(c)=[g(b)-g(a)]f'(c).$$
Escribamos los incrementos determinados por los bordes como $\Delta f,\Delta g$. Definimos
$$H(x)=\Delta g\,[f(x)-f(a)]-\Delta f\,[g(x)-g(a)].$$
Entonces $H(a)=H(b)=0$, es continua en todo el segmento y derivable dentro, con $H'(x)=\Delta g f'(x)-\Delta f g'(x)$ por C18. Los coeficientes son constantes, no funciones del argumento. Rolle aplicado a $H$ produce la igualdad. La construcción no divide por ningún incremento o derivada y admite los casos nulos.

</details>

#### Ejercicio 27. Tres puntos diferentes

[]{#MA-EX-ANM-01-019-027}

Para $f=x^2,g=x^3$ en $[0,1]$, compara sus dos puntos de Lagrange con el punto de Cauchy.

[]{#MA-SOL-ANM-01-019-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

**Respuesta.**

Ambos incrementos son uno. Lagrange para f resuelve 2c=1 y da 1/2; para g resuelve 3c²=1 y da 1/√3. Son distintos porque el cuadrado de 1/2 no es 1/3. Cauchy exige 3c²=2c; la interioridad c>0 elimina la solución cero y da c=2/3. En ese punto las dos derivadas valen 4/3 y su razón es uno. Aplicar dos existencias separadas no había garantizado un centro común.

**Retorno visual.** Véase [C19-F06](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Ejercicio 28. Legitimar ambas divisiones

[]{#MA-EX-ANM-01-019-028}

Bajo $g\prime(t)\ne0$ en todo $(a,b)$, prueba que la forma de cocientes de Cauchy está definida.

[]{#MA-SOL-ANM-01-019-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

**Respuesta.**

Si Δg=0, g tendría valores de borde iguales, continuidad en el segmento y derivabilidad dentro; Rolle daría un punto con $g'$=0, contradicción. Por tanto Δg≠0. El testigo c de Cauchy también cumple $g'(c)$≠0 por la premisa universal. Dividir la igualdad cruzada por Δg $g'(c)$, no nulo, da $f'(c)$/$g'(c)$=Δf/Δg. Se verifican las dos divisiones después de sus condiciones, sin asumir que un incremento no nulo haga no nula toda derivada.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Ejercicio 29. Un incremento nulo

[]{#MA-EX-ANM-01-019-029}

Aplica la forma cruzada a $f(x)=x$, $g(x)=x(1-x)$ en $[0,1]$. Localiza el punto y explica por qué la razón de incrementos no está definida.

[]{#MA-SOL-ANM-01-019-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

**Respuesta.**

Δf=1 y Δg=0. La identidad exige $g'(c)$=0; su derivada es 1-2c y el único punto interior es c=1/2. Allí $f'$=1 y $g'$=0, de modo que la igualdad cruzada es cero igual a cero. Las razones Δf/Δg y $f'$/$g'$ no existen. La forma cruzada contiene información correcta sobre la anulación, mientras la formulación por cocientes sería ilegítima en este ejemplo.

**Fundamento en la sección 19.6.**

**Forma de cocientes con hipótesis añadida.** Si $g'(t)\ne0$ para todo $t\in(a,b)$, Rolle impide $g(b)=g(a)$, porque esa igualdad daría un punto interior de derivada nula. En el punto entregado por R6 también $g'(c)\ne0$, y ahora sí podemos dividir:
$$\frac{f'(c)}{g'(c)}=\frac{\Delta f}{\Delta g}.$$
Sin esa condición, la igualdad de productos sigue siendo válida y un cociente puede carecer de significado. Por ejemplo, si $g$ es constante, ambos lados del producto cruzado son cero, sin que exista un cociente por $\Delta g$.

**Un mismo punto no sale de dos existencias.** En $[0,1]$, $f(x)=x^2$ y $g(x)=x^3$ tienen incrementos uno. Lagrange por separado da los puntos únicos $1/2$ y $1/\sqrt3$, diferentes. Cauchy da $3c^2=2c$; como $c>0$, resulta $c=2/3$. Allí la razón de las derivadas es uno, igual a la razón de incrementos. El dato geométrico puede representarse parametrizando el par $(g(x),f(x))$, con coordenadas intercambiadas respecto del argumento original; el teorema sigue siendo una prueba por Rolle, sin requerir teoría de curvas parametrizadas.

</details>

#### Ejercicio 30. Un testigo donde no se puede dividir

[]{#MA-EX-ANM-01-019-030}

Para $f=g=x^3$ en $[-1,1]$, explica por qué $\Delta g\ne0$ no autoriza dividir la identidad de Cauchy en cualquier punto que la satisfaga.

[]{#MA-SOL-ANM-01-019-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Los dos incrementos son dos y las derivadas iguales, así la igualdad cruzada es cierta para todo punto interior. En c=0 ambas derivadas valen cero. Aunque Δg=2≠0, la razón de derivadas sería 0/0 allí y no está definida. Se puede escoger otro punto no nulo en este ejemplo y obtener la razón uno, pero la sola identidad cruzada con un testigo arbitrario no garantiza esa división. Para una garantía universal se usa $g'$≠0 en todo el interior o se verifica expresamente la derivada en el testigo concreto.

</details>
## 19.7. Darboux: discontinuidad sin saltar valores

[]{#MA-SEC-ANM-01-019-007}

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

![En un bulto de C18, F′=−4u(1−u²) y entre u=0 y u=1/2 aparecen todos los valores entre cero y −3/2. La familia completa tiene F′(0)=0 y F′(x_n)=−3/2 con x_n→0, así no es continua en cero. Se representan cinco términos; R7 garantiza todos los valores intermedios entre los centros por una prueba de extremos, sin suponer continuidad de F′.](../../assets/books/anm/C19/C19-F07.svg){#fig-anm-c19-f07 fig-alt="En un bulto de C18, F′=−4u(1−u²) y entre u=0 y u=1/2 aparecen todos los valores entre cero y −3/2. La familia completa tiene F′(0)=0 y F′(x_n)=−3/2 con x_n→0, así no es continua en cero. Se representan cinco términos; R7 garantiza todos los valores intermedios entre los centros por una prueba de extremos, sin suponer continuidad de F′."}

**Consecuencia de signo.** Si $f'$ no se anula en $I$, no puede tener un valor positivo y otro negativo: Darboux con $\lambda=0$ daría una anulación entre ellos. Su signo es constante; si el intervalo es no vacío, fijar un punto y su signo determina cuál. R4 convierte ese signo en monotonía estricta. La premisa $f'\ne0$ no significa una cota positiva uniforme de $|f'|$.

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-019-049}

¿Darboux presupone continuidad de la derivada?

[]{#MA-MSOL-ANM-01-019-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

**Respuesta.**

No. Prueba sus valores intermedios usando continuidad de la función auxiliar, extremos y Fermat.

**Fundamento en la sección 19.7.**

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-019-050}

¿Qué resta se usa para buscar $f\prime(c)=\lambda$?

[]{#MA-MSOL-ANM-01-019-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

**Respuesta.**

$H(x)=f(x)-\lambda x$, cuya derivada es $f\prime(x)-\lambda$.

**Fundamento en la sección 19.7.**

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-019-051}

¿Por qué $H\prime(u)<0$ impide mínimo en el borde izquierdo?

[]{#MA-MSOL-ANM-01-019-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

**Respuesta.**

Una entrada próxima a la derecha tiene cociente negativo y por tanto valor menor que $H(u)$.

**Fundamento en la sección 19.7.**

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-019-052}

¿Por qué $H\prime(v)>0$ impide mínimo en el borde derecho?

[]{#MA-MSOL-ANM-01-019-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

**Respuesta.**

Una entrada próxima a la izquierda tiene incremento negativo y cociente positivo, así su valor es menor que $H(v)$.

**Fundamento en la sección 19.7.**

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-019-053}

¿Qué ocurre si se invierte el orden de los dos valores de derivada?

[]{#MA-MSOL-ANM-01-019-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

**Respuesta.**

Se aplica el mismo argumento a $-f$ y $-\lambda$, o se busca un máximo de la función auxiliar.

**Fundamento en la sección 19.7.**

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-019-054}

¿Qué garantiza una derivada que nunca se anula en un intervalo abierto?

[]{#MA-MSOL-ANM-01-019-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

**Respuesta.**

Su signo es constante; dos signos opuestos obligarían por Darboux a alcanzar cero entre ellos.

**Fundamento en la sección 19.7.**

**Consecuencia de signo.** Si $f'$ no se anula en $I$, no puede tener un valor positivo y otro negativo: Darboux con $\lambda=0$ daría una anulación entre ellos. Su signo es constante; si el intervalo es no vacío, fijar un punto y su signo determina cuál. R4 convierte ese signo en monotonía estricta. La premisa $f'\ne0$ no significa una cota positiva uniforme de $|f'|$.

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-019-055}

¿Valores intermedios implican continuidad?

[]{#MA-MSOL-ANM-01-019-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

**Respuesta.**

No. La derivada discontinua de los bultos de C18 satisface Darboux aunque sus valores no converjan al central.

**Fundamento en la sección 19.7.**

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-019-056}

¿Puede una derivada saltar directamente de menos uno a uno omitiendo cero?

[]{#MA-MSOL-ANM-01-019-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

**Respuesta.**

No en un intervalo donde sea la derivada de una función derivable en todos sus puntos; Darboux fuerza ese valor intermedio.

**Fundamento en la sección 19.7.**

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

</details>

### Ejercicios de la sección 19.7

#### Ejercicio 31. Excluir los bordes de un mínimo

[]{#MA-EX-ANM-01-019-031}

Si $H\prime(u)<0<H\prime(v)$ y H es derivable en un intervalo abierto que contiene $[u,v]$, prueba que alcanza un mínimo interior en ese segmento.

[]{#MA-SOL-ANM-01-019-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

**Respuesta.**

La pendiente negativa en u fuerza cocientes negativos cerca y una entrada explícita t=u+min(δu,v-u)/2 produce H(t)<H(u). La pendiente positiva en v fuerza cocientes positivos, y s=v-min(δv,v-u)/2 tiene incremento negativo, dando H(s)<H(v). Derivabilidad da continuidad de H en todo el segmento; C16 asegura un mínimo alcanzado. Ninguno de sus bordes puede minimizar por las comparaciones, así un minimizador c está en (u,v). Una bola pequeña de c queda en el segmento y convierte ese mínimo global restringido en mínimo local de la función original.

**Fundamento en la sección 19.7.**

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

C18 da continuidad de $H$ en cada punto del segmento; su restricción es continua allí. C16 entrega un mínimo alcanzado, que las dos comparaciones sitúan en algún $c\in(u,v)$. Ese mínimo es local para la función original: una bola suficientemente pequeña de $c$ queda en $(u,v)$. Fermat da $H'(c)=0$, luego $f'(c)=\lambda$. Si $f'(u)>\lambda>f'(v)$, se aplica el caso anterior a $-f$ y $-\lambda$, o se usa un máximo para la misma función auxiliar. No se elige una familia de minimizadores.

</details>

#### Ejercicio 32. Una derivada intermedia sin suponer continuidad

[]{#MA-EX-ANM-01-019-032}

Prueba Darboux para $f\prime(u)<\lambda<f\prime(v)$ y explica cómo tratar el orden opuesto.

[]{#MA-SOL-ANM-01-019-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

**Respuesta.**

H=f-λx tiene derivadas negativas y positivas en los dos bordes, respectivamente. E031 localiza un mínimo interior; Fermat implica $H'(c)$=0 y por tanto $f'(c)$=λ. La continuidad empleada es la de H, deducida de derivabilidad de f y de la recta, no la de $f'$. Si los valores derivados aparecen en orden opuesto, la función -f y el número -λ tienen el orden ya probado, y su conclusión se traduce de nuevo a $f'(c)$=λ. El punto está estrictamente entre u y v.

**Fundamento en la sección 19.7.**

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

</details>

#### Ejercicio 33. Continuidad y ausencia de saltos

[]{#MA-EX-ANM-01-019-033}

Usa la familia de bultos de C18 para distinguir continuidad de derivada y propiedad de Darboux. Explica qué valores deben aparecer entre cero y cada $x_n$.

[]{#MA-SOL-ANM-01-019-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

C18 prueba derivabilidad de F en toda la recta, $F'$(0)=0 y $F'$(x_n)=-3/2 con x_n→0. Por tanto $F'$ no es continua en cero. Darboux se aplica entre cero y cada x_n>0 y obliga a que cualquier λ de (-3/2,0) aparezca en algún centro interior a ese segmento. No se necesita un mismo centro para diferentes n o λ. Los valores intermedios son compatibles con las pendientes persistentes de la ruta, pues no implican convergencia al valor central.

**Retorno visual.** Véase [C19-F07](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

#### Ejercicio 34. Una derivada sin ceros tiene un signo

[]{#MA-EX-ANM-01-019-034}

Prueba que una derivada no nula en un intervalo abierto tiene signo constante, sin asumir continuidad de esa derivada.

[]{#MA-SOL-ANM-01-019-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

**Respuesta.**

Si hubiera un valor positivo y otro negativo, se ordenan sus centros como u<v. El cero queda estrictamente entre las dos derivadas y Darboux da un c intermedio con $f'(c)$=0, contradicción. En un intervalo no vacío se fija un centro; tricotomía y ausencia de ceros determinan su signo y excluyen el opuesto en todos los demás. R4 hace a f estrictamente creciente o decreciente según ese signo. No se deduce una separación uniforme de la derivada respecto de cero.

**Fundamento en la sección 19.7.**

**Consecuencia de signo.** Si $f'$ no se anula en $I$, no puede tener un valor positivo y otro negativo: Darboux con $\lambda=0$ daría una anulación entre ellos. Su signo es constante; si el intervalo es no vacío, fijar un punto y su signo determina cuál. R4 convierte ese signo en monotonía estricta. La premisa $f'\ne0$ no significa una cota positiva uniforme de $|f'|$.

**Discontinuidad y valores intermedios son compatibles.** La familia de bultos de C18 es derivable en toda la recta, tiene $F'(0)=0$ y puntos $x_n\to0$ con $F'(x_n)=-3/2$. R7 obliga a alcanzar cada valor de $(-3/2,0)$ entre cero y cada $x_n$, aunque las derivadas no converjan al valor central. En el perfil de cada bulto, la fórmula $-4u(1-u^2)$ también muestra variación continua dentro de esa pieza. Representar sólo una pieza no prueba toda la propiedad; ésta sigue de R7 aplicado a la función completa. Una función escalón que pase directamente de $-1$ a $1$ y omita cero no puede ser la derivada de una función derivable en un intervalo que contenga ambos lados.

</details>

#### Ejercicio 35. Un escalón no puede ser una derivada

[]{#MA-EX-ANM-01-019-035}

En $(-1,1)$, sea h menos uno para $x<0$ y uno para $x\ge0$. Prueba que no existe una función derivable en todo ese intervalo con derivada h.

[]{#MA-SOL-ANM-01-019-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

**Respuesta.**

Si existiera f, los centros u=-1/2 y v=1/2 tendrían derivadas menos uno y uno. Darboux con λ=0 entregaría un c∈(-1/2,1/2) donde $f'(c)$=0. Pero h sólo toma los valores -1 y 1 en todo el dominio, contradicción. El argumento usa el valor intermedio de derivadas existentes, sin asumir que h sea continua y sin discutir únicamente la apariencia de su salto en un gráfico.

**Fundamento en la sección 19.7.**

C18 mostró una función derivable cuya derivada no es continua. Sin embargo, una derivada en un intervalo no puede omitir un valor situado entre dos de sus valores. No lo demostraremos suponiendo continuidad de $f'$.

**R7 — Darboux.** Sea $f:I\to\mathbb R$ derivable en todos los puntos de un intervalo abierto $I$. Para $u<v$ en $I$ y un real $\lambda$ estrictamente entre $f'(u)$ y $f'(v)$, existe $c\in(u,v)$ con $f'(c)=\lambda$.

**Objeto auxiliar y prueba.** Supongamos primero $f'(u)<\lambda<f'(v)$ y pongamos $H(x)=f(x)-\lambda x$. Entonces $H'(u)<0<H'(v)$. El signo de las pendientes centradas en $u$ da un radio $\delta_u$ donde los cocientes son negativos. Para
$t=u+\min(\delta_u,v-u)/2\in(u,v)$ resulta $H(t)<H(u)$. En $v$, los cocientes son positivos en algún radio $\delta_v$; el argumento $s=v-\min(\delta_v,v-u)/2$ tiene incremento negativo y produce $H(s)<H(v)$. Así ninguno de los bordes minimiza $H$ sobre $[u,v]$.

</details>
## 19.8. Certificar ceros y soluciones únicas

[]{#MA-SEC-ANM-01-019-008}

Rolle y las cotas de incrementos producen certificados de número de soluciones y de error. Es necesario distinguir la existencia de una raíz, su unicidad y la precisión de un aproximante.

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

**Existencia por una herramienta diferente.** Para $p(x)=x^3+x-1$ en $[0,1]$, $p(0)=-1$ y $p(1)=1$. La continuidad y el valor intermedio de C15 dan un cero $r\in(0,1)$. Su derivada $3x^2+1\ge1$ hace imposible otro cero por R8, y también prueba crecimiento estricto por R4. El valor medio no creó la raíz: asegura su unicidad y cuantifica cambios una vez que C15 la garantiza.

**Certificado de posición y error.** Los valores $p(1/2)=-3/8$ y $p(3/4)=11/64$ encierran la única raíz en $(1/2,3/4)$. En $x=2/3$, $p(x)=-1/27$, así el crecimiento la sitúa a la derecha. Dentro de $[1/2,3/4]$,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
Aplicar R5 al par $x,r$ da
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
por lo que
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
Estas son cotas racionales demostradas, no cifras leídas de un gráfico. En general, una cota $f'\ge m>0$ sobre el segmento entre un aproximante $x$ y un cero $r$ da $|x-r|\le|f(x)|/m$, siempre que el cero y el segmento satisfagan las hipótesis.

![C15 garantiza la raíz r y Rolle su unicidad. Los signos exactos en 1/2 y 3/4 la encierran; p(2/3)=−1/27 la sitúa a la derecha del aproximante. Las cotas 7/4≤p′≤43/16 en ese segmento dan 16/1161≤r−2/3≤4/189. Los extremos de la banda son cotas cerradas, sin atribuir a r una coordenada numérica extraída del dibujo.](../../assets/books/anm/C19/C19-F08.svg){#fig-anm-c19-f08 fig-alt="C15 garantiza la raíz r y Rolle su unicidad. Los signos exactos en 1/2 y 3/4 la encierran; p(2/3)=−1/27 la sitúa a la derecha del aproximante. Las cotas 7/4≤p′≤43/16 en ese segmento dan 16/1161≤r−2/3≤4/189. Los extremos de la banda son cotas cerradas, sin atribuir a r una coordenada numérica extraída del dibujo."}

**Un número máximo puede alcanzarse.** Para $q(x)=x^3-3x$ sobre la recta, $q'(x)=3x^2-3$ tiene exactamente dos ceros, $-1,1$. R8 permite a lo sumo tres ceros de $q$. La factorización $q(x)=x(x^2-3)$ y las raíces de C10 muestran tres: $-\sqrt3,0,\sqrt3$. El conteo es finito y no usa un teorema sobre derivadas de orden superior.

**Lo que debe quedar certificado.** Una cota de derivada tiene que valer en todos los puntos interiores pertinentes, no sólo en una tabla de pendientes. Un par de valores iguales no autoriza Rolle sobre un dominio con huecos, ni una raíz garantiza otras entre cada par de puntos estacionarios. Disponemos ya de los puentes entre pendientes locales y orden, incrementos, valores intermedios de la derivada y soluciones sobre intervalos. Convexidad y modelos de orden superior tendrán sus propias hipótesis en los capítulos siguientes.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-019-057}

¿Qué da Rolle si dos entradas tienen el mismo valor?

[]{#MA-MSOL-ANM-01-019-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

**Respuesta.**

Un punto interior de derivada cero, siempre que su segmento esté en el dominio y se verifiquen continuidad y derivabilidad.

**Fundamento en la sección 19.8.**

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-019-058}

¿Qué cota de ceros de $f$ da a lo sumo $k$ ceros de $f\prime$?

[]{#MA-MSOL-ANM-01-019-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

**Respuesta.**

A lo sumo $k+1$ ceros distintos de $f$, usando los segmentos entre una lista finita de ceros ordenados.

**Fundamento en la sección 19.8.**

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-019-059}

¿Por qué los ceros de derivada de los segmentos vecinos son distintos?

[]{#MA-MSOL-ANM-01-019-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

**Respuesta.**

Cada uno está en un interior diferente, y esos interiores no se solapan.

**Fundamento en la sección 19.8.**

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-019-060}

¿Qué herramienta garantiza existencia del cero de $x^3+x-1$?

[]{#MA-MSOL-ANM-01-019-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

**Respuesta.**

Continuidad y valor intermedio de C15, con signos opuestos en cero y uno; Rolle sólo prueba unicidad.

**Fundamento en la sección 19.8.**

**Existencia por una herramienta diferente.** Para $p(x)=x^3+x-1$ en $[0,1]$, $p(0)=-1$ y $p(1)=1$. La continuidad y el valor intermedio de C15 dan un cero $r\in(0,1)$. Su derivada $3x^2+1\ge1$ hace imposible otro cero por R8, y también prueba crecimiento estricto por R4. El valor medio no creó la raíz: asegura su unicidad y cuantifica cambios una vez que C15 la garantiza.

**Certificado de posición y error.** Los valores $p(1/2)=-3/8$ y $p(3/4)=11/64$ encierran la única raíz en $(1/2,3/4)$. En $x=2/3$, $p(x)=-1/27$, así el crecimiento la sitúa a la derecha. Dentro de $[1/2,3/4]$,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
Aplicar R5 al par $x,r$ da
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
por lo que
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
Estas son cotas racionales demostradas, no cifras leídas de un gráfico. En general, una cota $f'\ge m>0$ sobre el segmento entre un aproximante $x$ y un cero $r$ da $|x-r|\le|f(x)|/m$, siempre que el cero y el segmento satisfagan las hipótesis.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-019-061}

¿Qué cota inferior de derivada vale en $[0,1]$ para ese polinomio?

[]{#MA-MSOL-ANM-01-019-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

**Respuesta.**

Uno, porque $p\prime(t)=3t^2+1\ge1$.

**Fundamento en la sección 19.8.**

**Un número máximo puede alcanzarse.** Para $q(x)=x^3-3x$ sobre la recta, $q'(x)=3x^2-3$ tiene exactamente dos ceros, $-1,1$. R8 permite a lo sumo tres ceros de $q$. La factorización $q(x)=x(x^2-3)$ y las raíces de C10 muestran tres: $-\sqrt3,0,\sqrt3$. El conteo es finito y no usa un teorema sobre derivadas de orden superior.

**Lo que debe quedar certificado.** Una cota de derivada tiene que valer en todos los puntos interiores pertinentes, no sólo en una tabla de pendientes. Un par de valores iguales no autoriza Rolle sobre un dominio con huecos, ni una raíz garantiza otras entre cada par de puntos estacionarios. Disponemos ya de los puentes entre pendientes locales y orden, incrementos, valores intermedios de la derivada y soluciones sobre intervalos. Convexidad y modelos de orden superior tendrán sus propias hipótesis en los capítulos siguientes.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-019-062}

¿Qué residuo tiene el aproximante $2/3$?

[]{#MA-MSOL-ANM-01-019-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

**Respuesta.**

$p(2/3)=-1/27$; la raíz única queda a su derecha por crecimiento estricto.

**Fundamento en la sección 19.8.**

**Existencia por una herramienta diferente.** Para $p(x)=x^3+x-1$ en $[0,1]$, $p(0)=-1$ y $p(1)=1$. La continuidad y el valor intermedio de C15 dan un cero $r\in(0,1)$. Su derivada $3x^2+1\ge1$ hace imposible otro cero por R8, y también prueba crecimiento estricto por R4. El valor medio no creó la raíz: asegura su unicidad y cuantifica cambios una vez que C15 la garantiza.

**Certificado de posición y error.** Los valores $p(1/2)=-3/8$ y $p(3/4)=11/64$ encierran la única raíz en $(1/2,3/4)$. En $x=2/3$, $p(x)=-1/27$, así el crecimiento la sitúa a la derecha. Dentro de $[1/2,3/4]$,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
Aplicar R5 al par $x,r$ da
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
por lo que
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
Estas son cotas racionales demostradas, no cifras leídas de un gráfico. En general, una cota $f'\ge m>0$ sobre el segmento entre un aproximante $x$ y un cero $r$ da $|x-r|\le|f(x)|/m$, siempre que el cero y el segmento satisfagan las hipótesis.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-019-063}

¿Qué error da una cota $f\prime\ge m>0$ entre $x$ y un cero $r$?

[]{#MA-MSOL-ANM-01-019-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

**Respuesta.**

$|x-r|\le|f(x)|/m$, obtenido de la cota de incrementos en ese segmento.

**Fundamento en la sección 19.8.**

**Certificado de posición y error.** Los valores $p(1/2)=-3/8$ y $p(3/4)=11/64$ encierran la única raíz en $(1/2,3/4)$. En $x=2/3$, $p(x)=-1/27$, así el crecimiento la sitúa a la derecha. Dentro de $[1/2,3/4]$,
$$\frac74\le p'(t)\le\frac{43}{16}.$$
Aplicar R5 al par $x,r$ da
$$\frac74(r-x)\le p(r)-p(x)=\frac1{27}\le\frac{43}{16}(r-x),$$
por lo que
$$\frac{16}{1161}\le r-\frac23\le\frac4{189}.$$
Estas son cotas racionales demostradas, no cifras leídas de un gráfico. En general, una cota $f'\ge m>0$ sobre el segmento entre un aproximante $x$ y un cero $r$ da $|x-r|\le|f(x)|/m$, siempre que el cero y el segmento satisfagan las hipótesis.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-019-064}

¿Qué falta cuando sólo se han muestreado unas pocas derivadas?

[]{#MA-MSOL-ANM-01-019-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

**Respuesta.**

Una cota válida para todos los puntos interiores pertinentes; la tabla finita no certifica esa premisa universal.

**Fundamento en la sección 19.8.**

**Lo que debe quedar certificado.** Una cota de derivada tiene que valer en todos los puntos interiores pertinentes, no sólo en una tabla de pendientes. Un par de valores iguales no autoriza Rolle sobre un dominio con huecos, ni una raíz garantiza otras entre cada par de puntos estacionarios. Disponemos ya de los puentes entre pendientes locales y orden, incrementos, valores intermedios de la derivada y soluciones sobre intervalos. Convexidad y modelos de orden superior tendrán sus propias hipótesis en los capítulos siguientes.

</details>

### Ejercicios de la sección 19.8

#### Ejercicio 36. Inyectividad desde Rolle

[]{#MA-EX-ANM-01-019-036}

Prueba inyectividad de una función continua y derivable interiormente en un intervalo si su derivada nunca se anula. Trata la diferencia entre igualdad de valores y cero de la función.

[]{#MA-SOL-ANM-01-019-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

**Respuesta.**

Si f(x)=f(y) para x<y, el segmento está en el intervalo y su restricción cumple Rolle, que produce c∈(x,y) con $f'(c)$=0, contradicción. Por tanto dos entradas distintas no tienen el mismo valor y f es inyectiva. No es necesario que esos valores comunes sean cero: Rolle sólo requiere igualdad de borde. La ausencia de derivadas nulas no prueba existencia de ninguna solución f(x)=b; únicamente permite a lo sumo una por valor de salida.

**Fundamento en la sección 19.8.**

Rolle y las cotas de incrementos producen certificados de número de soluciones y de error. Es necesario distinguir la existencia de una raíz, su unicidad y la precisión de un aproximante.

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

</details>

#### Ejercicio 37. Contar ceros por segmentos vecinos

[]{#MA-EX-ANM-01-019-037}

Si $f'$ tiene a lo sumo k ceros en el interior de un intervalo, prueba que f tiene a lo sumo k+1 ceros distintos bajo las hipótesis de R8.

[]{#MA-SOL-ANM-01-019-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

**Respuesta.**

Supongamos k+2 ceros distintos y ordenemos esa lista finita x0<…<x(k+1). En cada segmento vecino [xj,x(j+1)], continuidad, derivabilidad e igualdad de bordes cero permiten Rolle. Se obtienen k+1 puntos c_j en sus interiores con derivada cero; son distintos porque los interiores no se solapan. Esto contradice la cota k. Las aplicaciones son finitas, no una selección numerable de testigos. La prueba se refiere a ceros distintos, sin contar multiplicidad.

**Fundamento en la sección 19.8.**

**R8 — Ceros separados y unicidad.** Bajo las hipótesis de continuidad y derivabilidad sobre los segmentos de un intervalo $I$, si $f'$ nunca vale cero en su interior, $f$ es inyectiva. En efecto, $f(x)=f(y)$ con $x<y$ permitiría aplicar Rolle a $[x,y]$ y daría un cero de $f'$ entre ellos. Si $f'$ tiene a lo sumo $k$ ceros distintos, $k\ge0$ entero, $f$ tiene a lo sumo $k+1$ ceros distintos. Si hubiera $k+2$, ordenamos esa lista finita; Rolle en cada uno de sus $k+1$ segmentos vecinos entrega un cero de $f'$ en el respectivo interior. Son distintos porque esos interiores son disjuntos, contradicción. Sólo se instancian finitas existencias, sin una selección numerable.

</details>

#### Ejercicio 38. Existencia, unicidad y primera horquilla

[]{#MA-EX-ANM-01-019-038}

Para $p(x)=x^3+x-1$ en $[0,1]$, prueba existencia y unicidad de un cero y enciérralo entre $1/2$ y $3/4$.

[]{#MA-SOL-ANM-01-019-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

El polinomio es continuo y tiene valores -1 y 1 en los bordes; C15 da al menos un cero interior. Su derivada 3x²+1≥1 nunca se anula, así E036 prueba inyectividad y a lo sumo un cero. Se combinan ambos resultados para una raíz única r. Los valores exactos p(1/2)=-3/8 y p(3/4)=11/64 tienen signos opuestos y el mismo argumento de continuidad en ese subsegmento sitúa el cero en (1/2,3/4); la unicidad identifica ese cero con r. Rolle no reemplaza al valor intermedio en la parte de existencia.

</details>

#### Ejercicio 39. Un máximo de tres ceros que se alcanza

[]{#MA-EX-ANM-01-019-039}

Usa la derivada de $q(x)=x^3-3x$ para acotar sus ceros y comprueba cuántos tiene. ¿Dos ceros de $f'$ garantizan tres de f?

[]{#MA-SOL-ANM-01-019-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

**Respuesta.**

$q'$=3x²-3 se anula exactamente en -1 y 1, así R8 limita q a tres ceros distintos. Factorizar q=x(x²-3) muestra los tres valores -√3,0,√3, que efectivamente anulan q. La cota se alcanza en este ejemplo. La recíproca general es falsa: para Q=q+10 sobre [-2,2], la derivada conserva esos dos ceros interiores, pero sus valores se controlan por R4 en las piezas: Q(-2)=8,Q(-1)=12,Q(1)=8,Q(2)=12 y los signos de 3x²-3 dan mínimos al menos ocho, sin ceros. Dos puntos estacionarios no obligan a tres raíces.

**Fundamento en la sección 19.8.**

**Un número máximo puede alcanzarse.** Para $q(x)=x^3-3x$ sobre la recta, $q'(x)=3x^2-3$ tiene exactamente dos ceros, $-1,1$. R8 permite a lo sumo tres ceros de $q$. La factorización $q(x)=x(x^2-3)$ y las raíces de C10 muestran tres: $-\sqrt3,0,\sqrt3$. El conteo es finito y no usa un teorema sobre derivadas de orden superior.

**Lo que debe quedar certificado.** Una cota de derivada tiene que valer en todos los puntos interiores pertinentes, no sólo en una tabla de pendientes. Un par de valores iguales no autoriza Rolle sobre un dominio con huecos, ni una raíz garantiza otras entre cada par de puntos estacionarios. Disponemos ya de los puentes entre pendientes locales y orden, incrementos, valores intermedios de la derivada y soluciones sobre intervalos. Convexidad y modelos de orden superior tendrán sus propias hipótesis en los capítulos siguientes.

</details>

#### Ejercicio 40. Residuo convertido en distancia

[]{#MA-EX-ANM-01-019-040}

Para la raíz única r de E038 y el aproximante $x=2/3$, demuestra las cotas racionales $16/1161\le r-x\le4/189$.

[]{#MA-SOL-ANM-01-019-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Por E038, r∈(1/2,3/4). El aproximante también está ahí y p(x)=8/27+2/3-1=-1/27. El crecimiento estricto de p da r>x. En el segmento que contiene ambos, 1/4≤t²≤9/16, así 7/4≤$p'(t)$≤43/16. R5 produce (7/4)(r-x)≤p(r)-p(x)=1/27≤(43/16)(r-x). Dividir por las constantes positivas da r-x≤4/189 y r-x≥16/1161. Se acota el error sin conocer el punto de valor medio ni tomar una cifra decimal de la gráfica. Las cotas de derivada se probaron en todos los centros del segmento.

**Retorno visual.** Véase [C19-F08](analisis-para-matematicos-capitulo-19-de-lo-local-a-lo-global.html#fig-anm-c19-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-19)

[← Capítulo 18](analisis-para-matematicos-capitulo-18-diferenciabilidad-mirar-cada-vez-mas-cerca.html) · [Capítulo 20 →](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html)

---
content-id: MA-BCH-0286
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-021
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
title: 'Capítulo 21 — Taylor: modelos locales y error'
date-modified: '2026-10-12'
provenance:
  type: original
  sources:
  - ANM-C21.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-21)

Una aproximación no queda certificada al escribir sus coeficientes. Este capítulo construye el polinomio central finito, demuestra lo que deja fuera y precisa cómo controlar ese resto. Se distinguen datos centrales, información en un segmento y cotas sobre una región completa.

C18 aporta diferenciabilidad y reglas; C19 Rolle, Lagrange y Cauchy; C20 bandas y alcance de convexidad. Inducción, sumas finitas, tipos, límites, continuidad y raíces son interfaces heredadas. No se usan integrales, sumas infinitas ni reglas nuevas para potencias reales generales. El polinomio vive en toda la recta, pero el error se evalúa sólo donde la función original existe.

## 21.1. Un polinomio para los datos de un centro

[]{#MA-SEC-ANM-01-021-001}

La recta de C18 conserva el valor y la primera derivada de una función en un centro. Si conocemos más derivadas, ¿qué polinomio conserva exactamente esos datos? Primero resolvamos este problema finito; todavía no afirmamos nada sobre el error fuera del centro.

Fijemos $n\ge0$ y un centro $c$. Escribimos $f^{(0)}=f$ y $f^{(k+1)}=(f^{(k)})'$ donde esas derivadas existen en el dominio indicado. El factorial se define por $0!=1$ y $(k+1)!=(k+1)k!$. Inducción demuestra su positividad. En fórmulas reales, $k!$ abrevia su copia real positiva mediante la incrustación de naturales; no identificamos silenciosamente los dos tipos. La potencia de exponente cero es la función constante1, también en el centro.

Busquemos $P(t)=\sum_{k=0}^n a_k(t-c)^k$. Las reglas de C18 para productos finitos dan, por inducción, que la derivada de orden $j$ del término de grado $k$ es cero si $j>k$, y es $k!/(k-j)!\,(t-c)^{k-j}$ si $j\le k$. Al evaluar en $c$, sólo sobrevive el término $k=j$. Por tanto

$$P^{(j)}(c)=j!a_j,\qquad 0\le j\le n.$$

Para imponer $P^{(j)}(c)=f^{(j)}(c)$ no hay elección libre: $a_j=f^{(j)}(c)/j!$. Queda determinado el **polinomio de Taylor de orden $n$**:

$$T_{n,c}f(t)=\sum_{k=0}^n\frac{f^{(k)}(c)}{k!}(t-c)^k.$$

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

La igualdad de datos centrales tampoco determina toda una función. Para un $n$ fijo, los polinomios $P(t)$ y $P(t)+A(t-c)^{n+1}$ tienen los mismos valores derivados de órdenes0 a$n$ en $c$, para cualquier real $A$, pero difieren fuera del centro si $A\ne0$. La unicidad afirmada sólo afecta a polinomios de grado a lo sumo $n$.

![El cubo centrado en1 tiene T₁=1+3h y T₂=1+3h+3h². El resto de orden2 es h³, no cero fuera del centro. Las identidades finitas prueban estos valores; la coincidencia central no determina una función completa.](../../assets/books/anm/C21/C21-F01.svg){#fig-anm-c21-f01 fig-alt="El cubo centrado en1 tiene T₁=1+3h y T₂=1+3h+3h². El resto de orden2 es h³, no cero fuera del centro. Las identidades finitas prueban estos valores; la coincidencia central no determina una función completa."}

En el resto del capítulo escribiremos $R_{n,c}(x)=f(x)-T_{n,c}f(x)$. Es una función del dominio de $f$, mientras el polinomio está definido en toda $\mathbb R$. Cada comparación se hace en entradas donde la función original existe.

### Microcontroles

#### Microcontrol 1

[]{#MA-MIC-ANM-01-021-001}

¿Qué datos conserva el polinomio de Taylor de orden $n$?

[]{#MA-MSOL-ANM-01-021-001}

<details class="anm-solution">
<summary>Ver solución del microcontrol 1</summary>

**Respuesta.**

El valor y las derivadas de órdenes1 a$n$ en el centro, si están definidos; orden0 significa el propio valor.

**Fundamento en la sección 21.1.**

Busquemos $P(t)=\sum_{k=0}^n a_k(t-c)^k$. Las reglas de C18 para productos finitos dan, por inducción, que la derivada de orden $j$ del término de grado $k$ es cero si $j>k$, y es $k!/(k-j)!\,(t-c)^{k-j}$ si $j\le k$. Al evaluar en $c$, sólo sobrevive el término $k=j$. Por tanto

$$P^{(j)}(c)=j!a_j,\qquad 0\le j\le n.$$

Para imponer $P^{(j)}(c)=f^{(j)}(c)$ no hay elección libre: $a_j=f^{(j)}(c)/j!$. Queda determinado el **polinomio de Taylor de orden $n$**:

$$T_{n,c}f(t)=\sum_{k=0}^n\frac{f^{(k)}(c)}{k!}(t-c)^k.$$

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

</details>

#### Microcontrol 2

[]{#MA-MIC-ANM-01-021-002}

¿Cuál es el valor de $0!$ y por qué importa?

[]{#MA-MSOL-ANM-01-021-002}

<details class="anm-solution">
<summary>Ver solución del microcontrol 2</summary>

**Respuesta.**

Es1. Su copia real positiva permite el coeficiente de orden0 y evita un denominador nulo.

**Fundamento en la sección 21.1.**

Fijemos $n\ge0$ y un centro $c$. Escribimos $f^{(0)}=f$ y $f^{(k+1)}=(f^{(k)})'$ donde esas derivadas existen en el dominio indicado. El factorial se define por $0!=1$ y $(k+1)!=(k+1)k!$. Inducción demuestra su positividad. En fórmulas reales, $k!$ abrevia su copia real positiva mediante la incrustación de naturales; no identificamos silenciosamente los dos tipos. La potencia de exponente cero es la función constante1, también en el centro.

Busquemos $P(t)=\sum_{k=0}^n a_k(t-c)^k$. Las reglas de C18 para productos finitos dan, por inducción, que la derivada de orden $j$ del término de grado $k$ es cero si $j>k$, y es $k!/(k-j)!\,(t-c)^{k-j}$ si $j\le k$. Al evaluar en $c$, sólo sobrevive el término $k=j$. Por tanto

</details>

#### Microcontrol 3

[]{#MA-MIC-ANM-01-021-003}

¿Qué significa $k!$ cuando aparece en un cociente real?

[]{#MA-MSOL-ANM-01-021-003}

<details class="anm-solution">
<summary>Ver solución del microcontrol 3</summary>

**Respuesta.**

La copia real del factorial natural mediante la incrustación declarada; no se identifican tácitamente naturales y reales.

**Fundamento en la sección 21.1.**

Fijemos $n\ge0$ y un centro $c$. Escribimos $f^{(0)}=f$ y $f^{(k+1)}=(f^{(k)})'$ donde esas derivadas existen en el dominio indicado. El factorial se define por $0!=1$ y $(k+1)!=(k+1)k!$. Inducción demuestra su positividad. En fórmulas reales, $k!$ abrevia su copia real positiva mediante la incrustación de naturales; no identificamos silenciosamente los dos tipos. La potencia de exponente cero es la función constante1, también en el centro.

Busquemos $P(t)=\sum_{k=0}^n a_k(t-c)^k$. Las reglas de C18 para productos finitos dan, por inducción, que la derivada de orden $j$ del término de grado $k$ es cero si $j>k$, y es $k!/(k-j)!\,(t-c)^{k-j}$ si $j\le k$. Al evaluar en $c$, sólo sobrevive el término $k=j$. Por tanto

</details>

#### Microcontrol 4

[]{#MA-MIC-ANM-01-021-004}

¿Qué coeficiente corresponde a la derivada de orden $j$?

[]{#MA-MSOL-ANM-01-021-004}

<details class="anm-solution">
<summary>Ver solución del microcontrol 4</summary>

**Respuesta.**

$a_j=f^{(j)}(c)/j!$, porque $P^{(j)}(c)=j!a_j$.

**Fundamento en la sección 21.1.**

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

</details>

#### Microcontrol 5

[]{#MA-MIC-ANM-01-021-005}

¿El orden $n$ obliga a grado exactamente $n$?

[]{#MA-MSOL-ANM-01-021-005}

<details class="anm-solution">
<summary>Ver solución del microcontrol 5</summary>

**Respuesta.**

No. El último coeficiente puede ser cero, y el grado sólo está acotado superiormente por$n$.

**Fundamento en la sección 21.1.**

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

</details>

#### Microcontrol 6

[]{#MA-MIC-ANM-01-021-006}

¿Dónde está definido el polinomio y dónde el resto?

[]{#MA-MSOL-ANM-01-021-006}

<details class="anm-solution">
<summary>Ver solución del microcontrol 6</summary>

**Respuesta.**

El polinomio está en toda la recta; el resto $f-T_{n,c}f$ sólo en el dominio de$f$.

**Fundamento en la sección 21.1.**

La igualdad de datos centrales tampoco determina toda una función. Para un $n$ fijo, los polinomios $P(t)$ y $P(t)+A(t-c)^{n+1}$ tienen los mismos valores derivados de órdenes0 a$n$ en $c$, para cualquier real $A$, pero difieren fuera del centro si $A\ne0$. La unicidad afirmada sólo afecta a polinomios de grado a lo sumo $n$.

En el resto del capítulo escribiremos $R_{n,c}(x)=f(x)-T_{n,c}f(x)$. Es una función del dominio de $f$, mientras el polinomio está definido en toda $\mathbb R$. Cada comparación se hace en entradas donde la función original existe.

</details>

#### Microcontrol 7

[]{#MA-MIC-ANM-01-021-007}

¿Qué resto tiene $t^3$ a orden2 y centro1?

[]{#MA-MSOL-ANM-01-021-007}

<details class="anm-solution">
<summary>Ver solución del microcontrol 7</summary>

**Respuesta.**

Con $t=1+h$, el polinomio es $1+3h+3h^2$ y el resto exacto es$h^3$.

**Fundamento en la sección 21.1.**

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

</details>

#### Microcontrol 8

[]{#MA-MIC-ANM-01-021-008}

¿Los datos centrales hasta orden $n$ determinan una función completa?

[]{#MA-MSOL-ANM-01-021-008}

<details class="anm-solution">
<summary>Ver solución del microcontrol 8</summary>

**Respuesta.**

No. Añadir $A(t-c)^{n+1}$ conserva todos esos datos y puede cambiar la función fuera del centro.

**Fundamento en la sección 21.1.**

La igualdad de datos centrales tampoco determina toda una función. Para un $n$ fijo, los polinomios $P(t)$ y $P(t)+A(t-c)^{n+1}$ tienen los mismos valores derivados de órdenes0 a$n$ en $c$, para cualquier real $A$, pero difieren fuera del centro si $A\ne0$. La unicidad afirmada sólo afecta a polinomios de grado a lo sumo $n$.

En el resto del capítulo escribiremos $R_{n,c}(x)=f(x)-T_{n,c}f(x)$. Es una función del dominio de $f$, mientras el polinomio está definido en toda $\mathbb R$. Cada comparación se hace en entradas donde la función original existe.

</details>

### Ejercicios de la sección 21.1

[]{#ejercicios-21}

#### Ejercicio 1. Los coeficientes no se eligen a ojo

[]{#MA-EX-ANM-01-021-001}

Para $P(t)=\sum_{k=0}^n a_k(t-c)^k$, demuestra $P^{(j)}(c)=j!a_j$ y deduce existencia y unicidad del polinomio que conserva los datos de órdenes0 a$n$.

[]{#MA-SOL-ANM-01-021-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

**Respuesta.**

Derivamos cada monomio con la regla de producto finito. Si $j>k$, su derivada es cero; si $j\le k$, es $k!/(k-j)!\,(t-c)^{k-j}$. En el centro se anulan los términos con $k>j$ y el término $k=j$ vale $j!$, incluida la potencia de exponente cero definida como1. Así $P^{(j)}(c)=j!a_j$. El factorial tiene copia real positiva por inducción, luego $a_j=f^{(j)}(c)/j!$ es el único valor posible. La suma finita con esos coeficientes existe como polinomio y cumple los datos al sustituir. La unicidad se limita a grado a lo sumo$n$.

**Fundamento en la sección 21.1.**

La recta de C18 conserva el valor y la primera derivada de una función en un centro. Si conocemos más derivadas, ¿qué polinomio conserva exactamente esos datos? Primero resolvamos este problema finito; todavía no afirmamos nada sobre el error fuera del centro.

Fijemos $n\ge0$ y un centro $c$. Escribimos $f^{(0)}=f$ y $f^{(k+1)}=(f^{(k)})'$ donde esas derivadas existen en el dominio indicado. El factorial se define por $0!=1$ y $(k+1)!=(k+1)k!$. Inducción demuestra su positividad. En fórmulas reales, $k!$ abrevia su copia real positiva mediante la incrustación de naturales; no identificamos silenciosamente los dos tipos. La potencia de exponente cero es la función constante1, también en el centro.

</details>

#### Ejercicio 2. El cubo visto desde uno

[]{#MA-EX-ANM-01-021-002}

Construye los polinomios de Taylor de órdenes1,2,3 de $t^3$ en$c=1$, usando$h=t-1$. Calcula sus restos exactos.

[]{#MA-SOL-ANM-01-021-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

**Respuesta.**

Los datos son1,3,6,6 para órdenes0 a3. Por tanto $T_1=1+3h$, $T_2=1+3h+3h^2$ y $T_3=1+3h+3h^2+h^3$. La expansión finita de $(1+h)^3$ da restos $R_1=3h^2+h^3$, $R_2=h^3$ y $R_3=0$. Cada factorial convierte derivada en coeficiente; en orden3 se divide6 por6. Los órdenes bajos conservan sus datos aunque no igualen la función fuera del centro.

**Retorno visual.** Véase [C21-F01](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f01), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.1.**

Para imponer $P^{(j)}(c)=f^{(j)}(c)$ no hay elección libre: $a_j=f^{(j)}(c)/j!$. Queda determinado el **polinomio de Taylor de orden $n$**:

$$T_{n,c}f(t)=\sum_{k=0}^n\frac{f^{(k)}(c)}{k!}(t-c)^k.$$

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

</details>

#### Ejercicio 3. Orden mayor que el grado

[]{#MA-EX-ANM-01-021-003}

Encuentra el Taylor de orden4 de$2-3t+t^2$ en cero y explica por qué la palabra orden no exige grado4.

[]{#MA-SOL-ANM-01-021-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

**Respuesta.**

Las derivadas centrales son2,−3,2 y luego0 para órdenes3 y4. El Taylor es $2-3t+t^2$, pues el coeficiente cuadrático es2/2=1 y los superiores son cero. Su grado es2, menor que4. Orden4 exige conservar los datos hasta ese orden, no que el último coeficiente sea no nulo. El resto es cero porque la función ya es ese polinomio.

**Fundamento en la sección 21.1.**

Para imponer $P^{(j)}(c)=f^{(j)}(c)$ no hay elección libre: $a_j=f^{(j)}(c)/j!$. Queda determinado el **polinomio de Taylor de orden $n$**:

$$T_{n,c}f(t)=\sum_{k=0}^n\frac{f^{(k)}(c)}{k!}(t-c)^k.$$

Es el único polinomio de grado a lo sumo $n$ que reproduce todos esos datos en el centro. «Orden $n$» no significa grado exactamente $n$: el coeficiente superior puede ser cero. Para $n=0$ sólo retenemos el valor; para $n=1$ recuperamos la recta; para $n=2$ aparece $f''(c)(t-c)^2/2$. La definición usa datos finitos, no infinitas derivadas ni una suma infinita.

Si $f(t)=t^3$ y $c=1$, tenemos $f(c)=1$, $f'(c)=3$ y $f''(c)=6$. Así $T_{2,1}f(1+h)=1+3h+3h^2$. La identidad $(1+h)^3=1+3h+3h^2+h^3$ muestra en este caso un resto exacto $h^3$. No hemos probado todavía que todas las funciones tengan un resto semejante.

</details>

#### Ejercicio 4. Mismos datos, salidas diferentes

[]{#MA-EX-ANM-01-021-004}

Para$n$ fijo y un polinomio$P$ de grado a lo sumo$n$, prueba que$P+A(t-c)^{n+1}$ conserva sus datos centrales hasta orden$n$ y puede alcanzar cualquier valor prescrito en una entrada$x\ne c$.

[]{#MA-SOL-ANM-01-021-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

**Respuesta.**

Cada derivada de la potencia de órdenes0 a$n$ contiene un factor positivo de grado al menos1 en$t-c$ y se anula en$c$. Así se conservan los datos. En$x\ne c$, el factor $(x-c)^{n+1}$ es no cero. Para imponer una salida$b$, tomamos $A=(b-P(x))/(x-c)^{n+1}$. La función resultante es un polinomio y tiene valor$b$ en$x$. No contradice la unicidad de Taylor porque su grado puede superar$n$.

**Fundamento en la sección 21.1.**

La igualdad de datos centrales tampoco determina toda una función. Para un $n$ fijo, los polinomios $P(t)$ y $P(t)+A(t-c)^{n+1}$ tienen los mismos valores derivados de órdenes0 a$n$ en $c$, para cualquier real $A$, pero difieren fuera del centro si $A\ne0$. La unicidad afirmada sólo afecta a polinomios de grado a lo sumo $n$.

En el resto del capítulo escribiremos $R_{n,c}(x)=f(x)-T_{n,c}f(x)$. Es una función del dominio de $f$, mientras el polinomio está definido en toda $\mathbb R$. Cada comparación se hace en entradas donde la función original existe.

</details>

#### Ejercicio 5. Centro, dominio y factorial

[]{#MA-EX-ANM-01-021-005}

Explica los tres controles necesarios para escribir Taylor de$1/(1-t)$ en$c=0$ y por qué la definición del polinomio no certifica su error cerca de$t=1$.

[]{#MA-SOL-ANM-01-021-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

**Respuesta.**

El centro0 pertenece al dominio declarado$t<1$; las derivadas centrales usadas deben existir, lo que aquí dan las reglas del cociente e inducción. Los denominadores$k!$ se leen como sus copias reales positivas, incluido0!=1. El polinomio puede evaluarse en cualquier real, pero el resto sólo en el dominio original. La definición únicamente iguala datos en0: para controlar el error fuera se necesita una fórmula o cota adicional. Cerca de la singularidad1, el margen del denominador puede ser arbitrariamente pequeño.

**Fundamento en la sección 21.1.**

La igualdad de datos centrales tampoco determina toda una función. Para un $n$ fijo, los polinomios $P(t)$ y $P(t)+A(t-c)^{n+1}$ tienen los mismos valores derivados de órdenes0 a$n$ en $c$, para cualquier real $A$, pero difieren fuera del centro si $A\ne0$. La unicidad afirmada sólo afecta a polinomios de grado a lo sumo $n$.

En el resto del capítulo escribiremos $R_{n,c}(x)=f(x)-T_{n,c}f(x)$. Es una función del dominio de $f$, mientras el polinomio está definido en toda $\mathbb R$. Cada comparación se hace en entradas donde la función original existe.

</details>
## 21.2. Rolle se repite sin perder sus hipótesis

[]{#MA-SEC-ANM-01-021-002}

Para convertir coincidencias de derivadas en una identidad del resto necesitamos una herramienta de C19 repetida un número finito de veces. Sea $x\ne c$ y $K=[\min(c,x),\max(c,x)]$. Supongamos que hay funciones $H_0,\ldots,H_n$ continuas en $K$, con $H_k'=H_{k+1}$ en su interior para $k<n$, y que $H_n$ también es derivable en el interior. Exijamos

$$H_k(c)=0\quad(0\le k\le n),\qquad H_0(x)=0.$$

No exigimos continuidad de $H_n'$ ni su existencia en los bordes.

Empezamos con $z_0=x$. Rolle aplicado a $H_0$ entre $c$ y $z_0$ da un $z_1$ estrictamente entre ambos con $H_0'(z_1)=0$. Si $n\ge1$, la identidad de la cadena dice $H_1(z_1)=0$; además $H_1(c)=0$. Ahora Rolle aplicado a $H_1$ entre $c$ y $z_1$ da $z_2$ estrictamente entre ambos. Repetimos.

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

$$H_n'(z_{n+1})=0,\qquad z_{n+1}\text{ estrictamente entre }c\text{ y }x.$$

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

Cuando una función $H$ tiene derivadas continuas hasta orden $n$ en ese segmento, tomamos $H_k=H^{(k)}$ y leemos la hipótesis como un cero central repetido, más otro cero en $x$. La continuidad de los primeros miembros es exactamente lo que permite cada Rolle; la derivada final no necesita ser continua.

Por ejemplo $H(t)=t^3(1-t)$, con $c=0$ y $x=1$, cumple $H(0)=H'(0)=H''(0)=0$ y $H(1)=0$. Una elección es $z_1=3/4$, $z_2=1/2$ y $z_3=1/4$: $H'(3/4)=0$, $H''(1/2)=0$ y $H'''(1/4)=0$. Cada nuevo punto queda dentro del segmento anterior. Estas coordenadas son particulares de este polinomio; el lema general sólo asegura existencia.

![Para H=t³(1−t), con n=2, una cadena válida usa z₁=3/4, z₂=1/2 y z₃=1/4. Cada paso conserva un cero en el centro0 y obtiene el otro en el segmento anterior. Hay n+1=3 aplicaciones; los puntos exactos son particulares del ejemplo.](../../assets/books/anm/C21/C21-F02.svg){#fig-anm-c21-f02 fig-alt="Para H=t³(1−t), con n=2, una cadena válida usa z₁=3/4, z₂=1/2 y z₃=1/4. Cada paso conserva un cero en el centro0 y obtiene el otro en el segmento anterior. Hay n+1=3 aplicaciones; los puntos exactos son particulares del ejemplo."}

No se supone una elección simultánea de puntos para todas las entradas o todos los órdenes. Para un $n$ y un $x$ fijados, una inducción finita construye las existencias necesarias. Tampoco se confunde el número de ceros de $H$ con el de sus derivadas: las igualdades centrales de cada miembro suministran un borde reutilizable en cada paso.

### Microcontroles

#### Microcontrol 9

[]{#MA-MIC-ANM-01-021-009}

¿Qué igualdades centrales se necesitan para Rolle repetido de orden $n$?

[]{#MA-MSOL-ANM-01-021-009}

<details class="anm-solution">
<summary>Ver solución del microcontrol 9</summary>

**Respuesta.**

$H_k(c)=0$ para $0\le k\le n$, más $H_0(x)=0$ con $x\ne c$.

**Fundamento en la sección 21.2.**

Cuando una función $H$ tiene derivadas continuas hasta orden $n$ en ese segmento, tomamos $H_k=H^{(k)}$ y leemos la hipótesis como un cero central repetido, más otro cero en $x$. La continuidad de los primeros miembros es exactamente lo que permite cada Rolle; la derivada final no necesita ser continua.

Por ejemplo $H(t)=t^3(1-t)$, con $c=0$ y $x=1$, cumple $H(0)=H'(0)=H''(0)=0$ y $H(1)=0$. Una elección es $z_1=3/4$, $z_2=1/2$ y $z_3=1/4$: $H'(3/4)=0$, $H''(1/2)=0$ y $H'''(1/4)=0$. Cada nuevo punto queda dentro del segmento anterior. Estas coordenadas son particulares de este polinomio; el lema general sólo asegura existencia.

</details>

#### Microcontrol 10

[]{#MA-MIC-ANM-01-021-010}

¿Cuántas aplicaciones de Rolle produce la última derivada nula?

[]{#MA-MSOL-ANM-01-021-010}

<details class="anm-solution">
<summary>Ver solución del microcontrol 10</summary>

**Respuesta.**

$n+1$ aplicaciones, incluida una sola cuando$n=0$.

**Fundamento en la sección 21.2.**

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

$$H_n'(z_{n+1})=0,\qquad z_{n+1}\text{ estrictamente entre }c\text{ y }x.$$

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

</details>

#### Microcontrol 11

[]{#MA-MIC-ANM-01-021-011}

¿Qué invariante permite continuar el paso $k$?

[]{#MA-MSOL-ANM-01-021-011}

<details class="anm-solution">
<summary>Ver solución del microcontrol 11</summary>

**Respuesta.**

$H_k(c)=H_k(z_k)=0$, con $z_k\ne c$ y continuidad/derivabilidad en el subsegmento correspondiente.

**Fundamento en la sección 21.2.**

Empezamos con $z_0=x$. Rolle aplicado a $H_0$ entre $c$ y $z_0$ da un $z_1$ estrictamente entre ambos con $H_0'(z_1)=0$. Si $n\ge1$, la identidad de la cadena dice $H_1(z_1)=0$; además $H_1(c)=0$. Ahora Rolle aplicado a $H_1$ entre $c$ y $z_1$ da $z_2$ estrictamente entre ambos. Repetimos.

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

</details>

#### Microcontrol 12

[]{#MA-MIC-ANM-01-021-012}

¿Qué relación enlaza los miembros de la cadena?

[]{#MA-MSOL-ANM-01-021-012}

<details class="anm-solution">
<summary>Ver solución del microcontrol 12</summary>

**Respuesta.**

$H_k\prime=H_{k+1}$ en el interior para $k<n$; la derivada del último miembro también debe existir interiormente.

**Fundamento en la sección 21.2.**

Para convertir coincidencias de derivadas en una identidad del resto necesitamos una herramienta de C19 repetida un número finito de veces. Sea $x\ne c$ y $K=[\min(c,x),\max(c,x)]$. Supongamos que hay funciones $H_0,\ldots,H_n$ continuas en $K$, con $H_k'=H_{k+1}$ en su interior para $k<n$, y que $H_n$ también es derivable en el interior. Exijamos

$$H_k(c)=0\quad(0\le k\le n),\qquad H_0(x)=0.$$

No exigimos continuidad de $H_n'$ ni su existencia en los bordes.

Empezamos con $z_0=x$. Rolle aplicado a $H_0$ entre $c$ y $z_0$ da un $z_1$ estrictamente entre ambos con $H_0'(z_1)=0$. Si $n\ge1$, la identidad de la cadena dice $H_1(z_1)=0$; además $H_1(c)=0$. Ahora Rolle aplicado a $H_1$ entre $c$ y $z_1$ da $z_2$ estrictamente entre ambos. Repetimos.

</details>

#### Microcontrol 13

[]{#MA-MIC-ANM-01-021-013}

¿Se pide continuidad de la derivada final?

[]{#MA-MSOL-ANM-01-021-013}

<details class="anm-solution">
<summary>Ver solución del microcontrol 13</summary>

**Respuesta.**

No. Se necesita que exista en el interior para el último Rolle; los miembros anteriores sí son continuos sobre los segmentos.

**Fundamento en la sección 21.2.**

Cuando una función $H$ tiene derivadas continuas hasta orden $n$ en ese segmento, tomamos $H_k=H^{(k)}$ y leemos la hipótesis como un cero central repetido, más otro cero en $x$. La continuidad de los primeros miembros es exactamente lo que permite cada Rolle; la derivada final no necesita ser continua.

Por ejemplo $H(t)=t^3(1-t)$, con $c=0$ y $x=1$, cumple $H(0)=H'(0)=H''(0)=0$ y $H(1)=0$. Una elección es $z_1=3/4$, $z_2=1/2$ y $z_3=1/4$: $H'(3/4)=0$, $H''(1/2)=0$ y $H'''(1/4)=0$. Cada nuevo punto queda dentro del segmento anterior. Estas coordenadas son particulares de este polinomio; el lema general sólo asegura existencia.

</details>

#### Microcontrol 14

[]{#MA-MIC-ANM-01-021-014}

¿Cómo se ordena el segmento si $x<c$?

[]{#MA-MSOL-ANM-01-021-014}

<details class="anm-solution">
<summary>Ver solución del microcontrol 14</summary>

**Respuesta.**

Con extremos $\min(c,x)$ y $\max(c,x)$; los puntos sucesivos quedan entre$c$ y el punto anterior por el lado izquierdo.

**Fundamento en la sección 21.2.**

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

$$H_n'(z_{n+1})=0,\qquad z_{n+1}\text{ estrictamente entre }c\text{ y }x.$$

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

</details>

#### Microcontrol 15

[]{#MA-MIC-ANM-01-021-015}

¿Qué punto intermedio se afirma si $x=c$?

[]{#MA-MSOL-ANM-01-021-015}

<details class="anm-solution">
<summary>Ver solución del microcontrol 15</summary>

**Respuesta.**

Ninguno. No hay segmento con extremos distintos y el caso se resuelve por la igualdad central.

**Fundamento en la sección 21.2.**

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

Cuando una función $H$ tiene derivadas continuas hasta orden $n$ en ese segmento, tomamos $H_k=H^{(k)}$ y leemos la hipótesis como un cero central repetido, más otro cero en $x$. La continuidad de los primeros miembros es exactamente lo que permite cada Rolle; la derivada final no necesita ser continua.

</details>

#### Microcontrol 16

[]{#MA-MIC-ANM-01-021-016}

¿Se selecciona una familia infinita de testigos?

[]{#MA-MSOL-ANM-01-021-016}

<details class="anm-solution">
<summary>Ver solución del microcontrol 16</summary>

**Respuesta.**

No. Para un orden y una entrada fijados, la inducción realiza sólo un número finito de pasos existenciales.

**Fundamento en la sección 21.2.**

No se supone una elección simultánea de puntos para todas las entradas o todos los órdenes. Para un $n$ y un $x$ fijados, una inducción finita construye las existencias necesarias. Tampoco se confunde el número de ceros de $H$ con el de sus derivadas: las igualdades centrales de cada miembro suministran un borde reutilizable en cada paso.

</details>

### Ejercicios de la sección 21.2

#### Ejercicio 6. El invariante de Rolle repetido

[]{#MA-EX-ANM-01-021-006}

Escribe una prueba por inducción finita del lema de21.2, declarando el invariante y el número de aplicaciones.

[]{#MA-SOL-ANM-01-021-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

**Respuesta.**

Ponemos $z_0=x$. En el paso$k$, $H_k(c)=H_k(z_k)=0$ y$z_k\ne c$. La restricción al segmento de esos extremos es continua, y su derivada existe interiormente y coincide con la original. Rolle da$z_{k+1}$ estrictamente entre ambos con$H_k\prime(z_{k+1})=0$. Si$k<n$, la cadena convierte esa igualdad en$H_{k+1}(z_{k+1})=0$, mientras$H_{k+1}(c)=0$ era dato, y permite continuar. En el paso$n$ se obtiene la derivada final nula. Hay$n+1$ pasos, de0 a$n$. La longitud es finita y fijada de antemano.

**Fundamento en la sección 21.2.**

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

$$H_n'(z_{n+1})=0,\qquad z_{n+1}\text{ estrictamente entre }c\text{ y }x.$$

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

</details>

#### Ejercicio 7. Una cadena de tres puntos

[]{#MA-EX-ANM-01-021-007}

Para$H(t)=t^3(1-t)$ entre0 y1, comprueba los ceros centrales hasta orden2 y la cadena de puntos$3/4,1/2,1/4$ de Rolle.

[]{#MA-SOL-ANM-01-021-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

**Respuesta.**

Expandimos$H=t^3-t^4$. Sus derivadas son$H\prime=3t^2-4t^3$, $H\prime\prime=6t-12t^2$ y$H^{(3)}=6-24t$. En0, $H,H\prime,H\prime\prime$ valen0 y$H(1)=0$. Evaluar da$H\prime(3/4)=0$, $H\prime\prime(1/2)=0$ y$H^{(3)}(1/4)=0$. Se cumple$0<1/4<1/2<3/4<1$, de modo que cada punto está entre el centro y el punto anterior. La cadena realiza tres aplicaciones para$n=2$; sus valores exactos no son prescritos por el lema general.

**Retorno visual.** Véase [C21-F02](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f02), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.2.**

Por ejemplo $H(t)=t^3(1-t)$, con $c=0$ y $x=1$, cumple $H(0)=H'(0)=H''(0)=0$ y $H(1)=0$. Una elección es $z_1=3/4$, $z_2=1/2$ y $z_3=1/4$: $H'(3/4)=0$, $H''(1/2)=0$ y $H'''(1/4)=0$. Cada nuevo punto queda dentro del segmento anterior. Estas coordenadas son particulares de este polinomio; el lema general sólo asegura existencia.

No se supone una elección simultánea de puntos para todas las entradas o todos los órdenes. Para un $n$ y un $x$ fijados, una inducción finita construye las existencias necesarias. Tampoco se confunde el número de ceros de $H$ con el de sus derivadas: las igualdades centrales de cada miembro suministran un borde reutilizable en cada paso.

</details>

#### Ejercicio 8. Un dato central que no puede perderse

[]{#MA-EX-ANM-01-021-008}

Para$n=1$, muestra que$H(0)=H(1)=0$ sin exigir$H\prime(0)=0$ no garantiza un cero de$H\prime\prime$ interior.

[]{#MA-SOL-ANM-01-021-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

**Respuesta.**

Tomamos$H(t)=t(1-t)$. Tiene bordes0 y0, y Rolle da un cero de$H\prime=1-2t$ en1/2. Sin embargo$H\prime(0)=1$, no cero, y$H\prime\prime=-2$ no se anula en el interior. Falta el borde central nulo del segundo miembro de la cadena, así no se puede repetir Rolle entre0 y1/2. La igualdad de valores de la función no basta para toda la cadena.

**Fundamento en la sección 21.2.**

Cuando una función $H$ tiene derivadas continuas hasta orden $n$ en ese segmento, tomamos $H_k=H^{(k)}$ y leemos la hipótesis como un cero central repetido, más otro cero en $x$. La continuidad de los primeros miembros es exactamente lo que permite cada Rolle; la derivada final no necesita ser continua.

Por ejemplo $H(t)=t^3(1-t)$, con $c=0$ y $x=1$, cumple $H(0)=H'(0)=H''(0)=0$ y $H(1)=0$. Una elección es $z_1=3/4$, $z_2=1/2$ y $z_3=1/4$: $H'(3/4)=0$, $H''(1/2)=0$ y $H'''(1/4)=0$. Cada nuevo punto queda dentro del segmento anterior. Estas coordenadas son particulares de este polinomio; el lema general sólo asegura existencia.

</details>

#### Ejercicio 9. Rolle hacia la izquierda

[]{#MA-EX-ANM-01-021-009}

Aplica el esquema de$n=1$ a$H(t)=t^2(t+1)$ entre$c=0$ y$x=-1$. Calcula una cadena de testigos y explica la orientación.

[]{#MA-SOL-ANM-01-021-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

**Respuesta.**

Tenemos$H(0)=H\prime(0)=0$ y$H(-1)=0$. La primera derivada$3t^2+2t=t(3t+2)$ se anula interiormente en$z_1=-2/3$. La segunda$6t+2$ se anula en$z_2=-1/3$, estrictamente entre−2/3 y0. La cadena cumple$-1<-2/3<-1/3<0$: se acerca al centro por la izquierda. Cada aplicación usa el segmento con extremos ordenados mediante mínimo y máximo; no se invierte una hipótesis de continuidad o interioridad.

**Fundamento en la sección 21.2.**

El invariante del paso $k$ es $H_k(c)=H_k(z_k)=0$, con $z_k\ne c$; continuidad en el subsegmento y derivabilidad en su interior permiten obtener $z_{k+1}$ con $H_k'(z_{k+1})=0$. Para $k<n$ se convierte en $H_{k+1}(z_{k+1})=0$ y permite continuar. En el paso final obtenemos

$$H_n'(z_{n+1})=0,\qquad z_{n+1}\text{ estrictamente entre }c\text{ y }x.$$

Se han usado $n+1$ aplicaciones de Rolle, no $n$. El caso $n=0$ consiste en una sola. Si $x<c$, todos los segmentos se ordenan mediante mínimo y máximo; los nuevos puntos siguen acercándose a $c$ por el lado izquierdo. La derivada de una restricción interior coincide con la original, y cada subsegmento mantiene extremos distintos. Si $x=c$, no hay segmento no degenerado y no se afirma un punto intermedio.

</details>

#### Ejercicio 10. Qué continuidad consume cada paso

[]{#MA-EX-ANM-01-021-010}

Distingue las hipótesis de continuidad de$H_0,\ldots,H_n$ y la hipótesis sobre$H_n\prime$. Explica por qué no hace falta una familia infinita de puntos.

[]{#MA-SOL-ANM-01-021-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

**Respuesta.**

Cada$H_k$ se usa como función de un Rolle sobre un subsegmento, así necesita continuidad incluyendo sus extremos. Para$k<n$ su derivabilidad interior y la igualdad$H_k\prime=H_{k+1}$ permiten enlazar el próximo miembro. El último$H_n$ necesita derivabilidad interior, pero Rolle no exige continuidad de$H_n\prime$ ni su existencia en bordes. El proceso fija$n$ y construye sólo$n+1$ existencias, mediante inducción finita; no define un selector para todas las entradas o todos los órdenes simultáneamente.

**Fundamento en la sección 21.2.**

No se supone una elección simultánea de puntos para todas las entradas o todos los órdenes. Para un $n$ y un $x$ fijados, una inducción finita construye las existencias necesarias. Tampoco se confunde el número de ceros de $H$ con el de sus derivadas: las igualdades centrales de cada miembro suministran un borde reutilizable en cada paso.

</details>
## 21.3. Forzar el resto: la fórmula de Lagrange

[]{#MA-SEC-ANM-01-021-003}

Tomemos una función $f$ derivable hasta orden $n+1$ en un intervalo abierto $J$, y un centro $c$ y una entrada $x$ de $J$. La existencia de cada derivada hasta orden $n+1$ hace continuas a las funciones $f,\ldots,f^{(n)}$ sobre cada segmento interior. No se supone continuidad de $f^{(n+1)}$.

Para $x=c$, $R_{n,c}(c)=0$ por construcción. Sea ahora $x\ne c$ y fijemos el coeficiente

$$A=\frac{R_{n,c}(x)}{(x-c)^{n+1}}.$$

El denominador es no nulo. El coeficiente depende de la entrada que acabamos de fijar; no representa un único valor válido para todas las entradas. Definamos en el segmento que une $c$ y $x$

$$H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}.$$

La elección de $A$ fuerza $H(x)=0$. En el centro, la coincidencia de datos de Taylor y el exponente $n+1$ dan $H^{(k)}(c)=0$ para $0\le k\le n$. Los miembros hasta orden $n$ son continuos sobre el segmento y enlazan sus derivadas. El lema de Rolle repetido produce un $\xi$ estrictamente entre $c$ y $x$ con $H^{(n+1)}(\xi)=0$.

La derivada de orden $n+1$ del polinomio de Taylor es cero; la de $(t-c)^{n+1}$ es la constante $(n+1)!$. Entonces

$$0=f^{(n+1)}(\xi)-A(n+1)!.$$

Despejar $A$ y recuperar su definición demuestra la igualdad exacta

$$f(x)=T_{n,c}f(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.$$

Es Taylor finito con **resto de Lagrange**. Para $n=0$ recupera el valor medio de C19; para $n=1$ convierte la diferencia respecto de la tangente en una segunda derivada intermedia por $(x-c)^2/2$. El testigo puede depender de $f,n,c,x$ y no tiene por qué ser único o el punto medio. No se lo usa como una constante al variar esos datos.

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

![Para t³ en centro0, entrada1 y orden1, R=1 y A=1. El auxiliar H=t³−t² tiene los ceros centrales requeridos y otro en1. La derivada final H′′=6t−2 se anula en ξ=1/3 y devuelve R=f′′(ξ)/2=1.](../../assets/books/anm/C21/C21-F03.svg){#fig-anm-c21-f03 fig-alt="Para t³ en centro0, entrada1 y orden1, R=1 y A=1. El auxiliar H=t³−t² tiene los ceros centrales requeridos y otro en1. La derivada final H′′=6t−2 se anula en ξ=1/3 y devuelve R=f′′(ξ)/2=1."}

Para $f(t)=t^3$, centro1 y orden2, $f'''=6$ y el resto es $6h^3/3!=h^3$, coincidente con la expansión exacta de21.1. No hay un punto distinguido: todos los puntos interiores dan el mismo valor de tercera derivada. Para el cuadrado y orden1 ocurre lo mismo con la segunda derivada constante.

### Microcontroles

#### Microcontrol 17

[]{#MA-MIC-ANM-01-021-017}

¿Qué coeficiente fuerza la anulación del auxiliar en $x\ne c$?

[]{#MA-MSOL-ANM-01-021-017}

<details class="anm-solution">
<summary>Ver solución del microcontrol 17</summary>

**Respuesta.**

$A=R_{n,c}(x)/(x-c)^{n+1}$; el incremento no nulo permite dividir.

**Fundamento en la sección 21.3.**

El denominador es no nulo. El coeficiente depende de la entrada que acabamos de fijar; no representa un único valor válido para todas las entradas. Definamos en el segmento que une $c$ y $x$

$$H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}.$$

La elección de $A$ fuerza $H(x)=0$. En el centro, la coincidencia de datos de Taylor y el exponente $n+1$ dan $H^{(k)}(c)=0$ para $0\le k\le n$. Los miembros hasta orden $n$ son continuos sobre el segmento y enlazan sus derivadas. El lema de Rolle repetido produce un $\xi$ estrictamente entre $c$ y $x$ con $H^{(n+1)}(\xi)=0$.

</details>

#### Microcontrol 18

[]{#MA-MIC-ANM-01-021-018}

¿Qué función auxiliar se usa en la prueba de Lagrange?

[]{#MA-MSOL-ANM-01-021-018}

<details class="anm-solution">
<summary>Ver solución del microcontrol 18</summary>

**Respuesta.**

$H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}$.

**Fundamento en la sección 21.3.**

Es Taylor finito con **resto de Lagrange**. Para $n=0$ recupera el valor medio de C19; para $n=1$ convierte la diferencia respecto de la tangente en una segunda derivada intermedia por $(x-c)^2/2$. El testigo puede depender de $f,n,c,x$ y no tiene por qué ser único o el punto medio. No se lo usa como una constante al variar esos datos.

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

</details>

#### Microcontrol 19

[]{#MA-MIC-ANM-01-021-019}

¿Por qué se anulan sus datos centrales hasta orden $n$?

[]{#MA-MSOL-ANM-01-021-019}

<details class="anm-solution">
<summary>Ver solución del microcontrol 19</summary>

**Respuesta.**

Taylor conserva los datos y la potencia adicional tiene todas esas derivadas nulas en$c$.

**Fundamento en la sección 21.3.**

El denominador es no nulo. El coeficiente depende de la entrada que acabamos de fijar; no representa un único valor válido para todas las entradas. Definamos en el segmento que une $c$ y $x$

$$H(t)=f(t)-T_{n,c}f(t)-A(t-c)^{n+1}.$$

La elección de $A$ fuerza $H(x)=0$. En el centro, la coincidencia de datos de Taylor y el exponente $n+1$ dan $H^{(k)}(c)=0$ para $0\le k\le n$. Los miembros hasta orden $n$ son continuos sobre el segmento y enlazan sus derivadas. El lema de Rolle repetido produce un $\xi$ estrictamente entre $c$ y $x$ con $H^{(n+1)}(\xi)=0$.

</details>

#### Microcontrol 20

[]{#MA-MIC-ANM-01-021-020}

¿Qué igualdad deja el último Rolle?

[]{#MA-MSOL-ANM-01-021-020}

<details class="anm-solution">
<summary>Ver solución del microcontrol 20</summary>

**Respuesta.**

$f^{(n+1)}(\xi)-A(n+1)!=0$, pues el polinomio de orden$n$ ya tiene derivada$n+1$ nula.

**Fundamento en la sección 21.3.**

La derivada de orden $n+1$ del polinomio de Taylor es cero; la de $(t-c)^{n+1}$ es la constante $(n+1)!$. Entonces

$$0=f^{(n+1)}(\xi)-A(n+1)!.$$

Despejar $A$ y recuperar su definición demuestra la igualdad exacta

$$f(x)=T_{n,c}f(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.$$

Es Taylor finito con **resto de Lagrange**. Para $n=0$ recupera el valor medio de C19; para $n=1$ convierte la diferencia respecto de la tangente en una segunda derivada intermedia por $(x-c)^2/2$. El testigo puede depender de $f,n,c,x$ y no tiene por qué ser único o el punto medio. No se lo usa como una constante al variar esos datos.

</details>

#### Microcontrol 21

[]{#MA-MIC-ANM-01-021-021}

¿Qué posición tiene $\xi$?

[]{#MA-MSOL-ANM-01-021-021}

<details class="anm-solution">
<summary>Ver solución del microcontrol 21</summary>

**Respuesta.**

Está estrictamente entre$c$ y$x$, para$x\ne c$; no se predetermina como punto medio.

**Fundamento en la sección 21.3.**

La derivada de orden $n+1$ del polinomio de Taylor es cero; la de $(t-c)^{n+1}$ es la constante $(n+1)!$. Entonces

$$0=f^{(n+1)}(\xi)-A(n+1)!.$$

Despejar $A$ y recuperar su definición demuestra la igualdad exacta

$$f(x)=T_{n,c}f(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.$$

Es Taylor finito con **resto de Lagrange**. Para $n=0$ recupera el valor medio de C19; para $n=1$ convierte la diferencia respecto de la tangente en una segunda derivada intermedia por $(x-c)^2/2$. El testigo puede depender de $f,n,c,x$ y no tiene por qué ser único o el punto medio. No se lo usa como una constante al variar esos datos.

</details>

#### Microcontrol 22

[]{#MA-MIC-ANM-01-021-022}

¿De qué datos puede depender el testigo?

[]{#MA-MSOL-ANM-01-021-022}

<details class="anm-solution">
<summary>Ver solución del microcontrol 22</summary>

**Respuesta.**

De la función, el orden, el centro y la entrada; no se conserva como una constante al variarlos.

**Fundamento en la sección 21.3.**

Tomemos una función $f$ derivable hasta orden $n+1$ en un intervalo abierto $J$, y un centro $c$ y una entrada $x$ de $J$. La existencia de cada derivada hasta orden $n+1$ hace continuas a las funciones $f,\ldots,f^{(n)}$ sobre cada segmento interior. No se supone continuidad de $f^{(n+1)}$.

Para $x=c$, $R_{n,c}(c)=0$ por construcción. Sea ahora $x\ne c$ y fijemos el coeficiente

$$A=\frac{R_{n,c}(x)}{(x-c)^{n+1}}.$$

El denominador es no nulo. El coeficiente depende de la entrada que acabamos de fijar; no representa un único valor válido para todas las entradas. Definamos en el segmento que une $c$ y $x$

</details>

#### Microcontrol 23

[]{#MA-MIC-ANM-01-021-023}

¿Es necesaria continuidad de $f^{(n+1)}$ para la prueba por Rolle?

[]{#MA-MSOL-ANM-01-021-023}

<details class="anm-solution">
<summary>Ver solución del microcontrol 23</summary>

**Respuesta.**

No. Basta su existencia interior y la continuidad de los miembros hasta orden$n$ sobre el segmento.

**Fundamento en la sección 21.3.**

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

</details>

#### Microcontrol 24

[]{#MA-MIC-ANM-01-021-024}

¿Qué se usa como dato central en el contrato cerrado?

[]{#MA-MSOL-ANM-01-021-024}

<details class="anm-solution">
<summary>Ver solución del microcontrol 24</summary>

**Respuesta.**

Los valores de las extensiones continuas dadas $f_k(c)$; no se presupone derivar en un borde.

**Fundamento en la sección 21.3.**

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

</details>

### Ejercicios de la sección 21.3

#### Ejercicio 11. El auxiliar que obliga a la igualdad

[]{#MA-EX-ANM-01-021-011}

Demuestra Taylor–Lagrange a orden$n$ mediante$H=f-T_{n,c}f-A(t-c)^{n+1}$, justificando cada división y el caso$x=c$.

[]{#MA-SOL-ANM-01-021-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

**Respuesta.**

Si$x=c$, el resto es0 por los datos centrales y no se pide testigo interior. Si$x\ne c$, definimos$A=R(x)/(x-c)^{n+1}$, con denominador no cero. Esto hace$H(x)=0$. Los datos de Taylor y la potencia de grado$n+1$ dan$H^{(k)}(c)=0$ para$k\le n$. Bajo el contrato diferencial, los primeros miembros son continuos y sus derivadas enlazan; Rolle repetido da$H^{(n+1)}(\xi)=0$. La derivada final del polinomio es0 y la de la potencia es$(n+1)!$, así$A=f^{(n+1)}(\xi)/(n+1)!$. Este factorial real es positivo, por lo que se puede despejar. Sustituimos$A$ para obtener la fórmula.

**Fundamento en la sección 21.3.**

La elección de $A$ fuerza $H(x)=0$. En el centro, la coincidencia de datos de Taylor y el exponente $n+1$ dan $H^{(k)}(c)=0$ para $0\le k\le n$. Los miembros hasta orden $n$ son continuos sobre el segmento y enlazan sus derivadas. El lema de Rolle repetido produce un $\xi$ estrictamente entre $c$ y $x$ con $H^{(n+1)}(\xi)=0$.

La derivada de orden $n+1$ del polinomio de Taylor es cero; la de $(t-c)^{n+1}$ es la constante $(n+1)!$. Entonces

$$0=f^{(n+1)}(\xi)-A(n+1)!.$$

Despejar $A$ y recuperar su definición demuestra la igualdad exacta

</details>

#### Ejercicio 12. Un testigo que no es el medio

[]{#MA-EX-ANM-01-021-012}

Para$f(t)=t^3$, centro0, entrada1 y Taylor de orden1, calcula el testigo de Lagrange y compáralo con el punto medio.

[]{#MA-SOL-ANM-01-021-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

**Respuesta.**

$T_{1,0}=0$, así$R(1)=1$. La fórmula dice$1=f\prime\prime(\xi)/2=6\xi/2=3\xi$, de donde$\xi=1/3$. Pertenece estrictamente a$(0,1)$ pero no es el medio1/2. Este caso tiene un único testigo porque la segunda derivada es estrictamente creciente. No se infiere unicidad del teorema general.

**Retorno visual.** Véase [C21-F03](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.3.**

Para $f(t)=t^3$, centro1 y orden2, $f'''=6$ y el resto es $6h^3/3!=h^3$, coincidente con la expansión exacta de21.1. No hay un punto distinguido: todos los puntos interiores dan el mismo valor de tercera derivada. Para el cuadrado y orden1 ocurre lo mismo con la segunda derivada constante.

</details>

#### Ejercicio 13. Una derivada constante deja muchos testigos

[]{#MA-EX-ANM-01-021-013}

Para$t^3$ a orden2 y centro1, muestra que cualquier punto interior entre1 y$x\ne1$ verifica el resto. ¿Qué demuestra sobre la unicidad?

[]{#MA-SOL-ANM-01-021-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

**Respuesta.**

La expansión exacta da$R=(x-1)^3$. La tercera derivada es6 en cada punto, de modo que$[f^{(3)}(\xi)/3!](x-1)^3=(x-1)^3$ para cualquier$\xi$ estrictamente interior. Hay infinitos puntos posibles en ese segmento y ninguna unicidad. El teorema garantiza uno; una fórmula constante puede hacer válidos todos.

**Fundamento en la sección 21.3.**

Para $f(t)=t^3$, centro1 y orden2, $f'''=6$ y el resto es $6h^3/3!=h^3$, coincidente con la expansión exacta de21.1. No hay un punto distinguido: todos los puntos interiores dan el mismo valor de tercera derivada. Para el cuadrado y orden1 ocurre lo mismo con la segunda derivada constante.

</details>

#### Ejercicio 14. Un centro fronterizo sin última derivada

[]{#MA-EX-ANM-01-021-014}

En$[0,1]$, usa$f(t)=t^{5/2}=t^2\sqrt t$ para Taylor de orden2 y centro0 mediante el contrato cerrado. Verifica los miembros continuos y explica qué pasa con la tercera derivada en el borde.

[]{#MA-SOL-ANM-01-021-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

**Respuesta.**

Los miembros son$f_0=t^2\sqrt t$, $f_1=(5/2)t\sqrt t$ y$f_2=(15/4)\sqrt t$, con valores0 en el borde. Son continuos sobre$[0,1]$ y las relaciones de derivación se cumplen en$(0,1)$. La derivada$f_2\prime=(15/8)/\sqrt t$ existe interiormente aunque no es finita en0. El contrato cerrado legitima Taylor de orden2 para$x>0$, usando los valores centrales dados; la derivada final se evalúa sólo en un testigo interior. No se obtiene por eso una cota uniforme de tercera derivada cerca de0.

**Fundamento en la sección 21.3.**

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

</details>

#### Ejercicio 15. El caso de orden cero

[]{#MA-EX-ANM-01-021-015}

Reduce Taylor–Lagrange de orden0 al valor medio de C19 y señala las hipótesis que siguen siendo necesarias.

[]{#MA-SOL-ANM-01-021-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

**Respuesta.**

El polinomio es$T_{0,c}=f(c)$ y1!=1, de modo que$f(x)-f(c)=f\prime(\xi)(x-c)$. Para$x\ne c$ esto es exactamente Lagrange sobre el segmento. Se conserva continuidad incluyendo ambos extremos y derivabilidad interior; el carácter intervalar asegura que el segmento está en el dominio. Para$x=c$ hay igualdad de valores sin testigo entre extremos coincidentes. La reducción no elimina ninguna de esas condiciones.

**Fundamento en la sección 21.3.**

Despejar $A$ y recuperar su definición demuestra la igualdad exacta

$$f(x)=T_{n,c}f(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-c)^{n+1}.$$

Es Taylor finito con **resto de Lagrange**. Para $n=0$ recupera el valor medio de C19; para $n=1$ convierte la diferencia respecto de la tangente en una segunda derivada intermedia por $(x-c)^2/2$. El testigo puede depender de $f,n,c,x$ y no tiene por qué ser único o el punto medio. No se lo usa como una constante al variar esos datos.

La prueba también admite un contrato sobre un segmento cerrado: una cadena dada $f_0,\ldots,f_n$ continua incluyendo los bordes, con $f_k'=f_{k+1}$ en el interior, y $f_n'$ existente en todo el interior. El polinomio usa los valores $f_k(c)$ de esas extensiones continuas; la derivada final sólo se evalúa en $\xi$. No se presupone un operador de derivación en los bordes. Las identidades para $H_k$ y Rolle son las mismas. Este contrato incluye centros fronterizos y no pide la derivada final en el propio centro.

</details>
## 21.4. Un punto desconocido, una cota verificable

[]{#MA-SEC-ANM-01-021-004}

La fórmula exacta contiene un punto desconocido. Para certificar error conviene eliminarlo mediante una cota que controle todas sus ubicaciones posibles. Bajo el contrato anterior, si $|f^{(n+1)}(t)|\le M$ en todo el interior del segmento, con $M\ge0$, obtenemos

$$|R_{n,c}(x)|\le\frac{M}{(n+1)!}|x-c|^{n+1}.$$

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

Cuando la misma $M$ sirve en el interior de $[c-\rho,c+\rho]$, el mismo número $M\rho^{n+1}/(n+1)!$ acota todos los errores de ese segmento. El orden lógico es región, cota universal, entrada y testigo; tomar un máximo sobre puntos desconocidos sin justificarlo no resuelve el problema.

También hay una forma exacta de Cauchy. En el contrato abierto de21.3, fijemos $x$ y dejemos variar el centro auxiliar $t$:

$$G(t)=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k.$$

En el extremo $t=x$, el término de grado cero da $G(x)=0$; en $t=c$ tenemos $G(c)=R_{n,c}(x)$. Al derivar, la parte que deriva $f^{(k)}$ cancela con la que deriva la potencia del término siguiente. Los dos sumatorios finitos dejan

$$G'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n.$$

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

$$R_{n,c}(x)=\frac{f^{(n+1)}(\eta)}{n!}(x-\eta)^n(x-c).$$

El signo procede de $G(x)-G(c)=-R_{n,c}(x)$ y del signo negativo de $G'$. Para $n=0$ la potencia vale1, sin un cociente nulo. Como $|x-\eta|\le|x-c|$, una cota absoluta da $|R|\le M|x-c|^{n+1}/n!$. Es válida aunque, con una cota constante, suele ser menos ajustada que Lagrange. Las dos formas pueden tener testigos diferentes.

Si $m\le f^{(n+1)}\le M$, el coeficiente $R/(x-c)^{n+1}$ de Lagrange está entre $m/(n+1)!$ y $M/(n+1)!$. Para transformarlo en una banda del resto hay que atender al signo de $(x-c)^{n+1}$. Si es negativo, el orden de las cotas se invierte. Una cota absoluta evita este cambio; una banda firmada conserva información direccional.

![Con f=t³, c=0, x=1 y n=1, G=1−3t²+2t³ y G′=−6t(1−t). La secante de G tiene pendiente−1 y dos testigos η=(1±1/√3)/2. Ambos dan R=6η(1−η)=1, distintos del ξ=1/3 de Lagrange.](../../assets/books/anm/C21/C21-F04.svg){#fig-anm-c21-f04 fig-alt="Con f=t³, c=0, x=1 y n=1, G=1−3t²+2t³ y G′=−6t(1−t). La secante de G tiene pendiente−1 y dos testigos η=(1±1/√3)/2. Ambos dan R=6η(1−η)=1, distintos del ξ=1/3 de Lagrange."}

Con $n=1$, el exponente2 siempre es no negativo y recuperamos las bandas cuadráticas de C20. Si $n=2$ y $f'''$ es positiva, el resto es positivo a la derecha del centro y negativo a su izquierda. «Error pequeño» y «error de signo conocido» son conclusiones diferentes.

### Microcontroles

#### Microcontrol 25

[]{#MA-MIC-ANM-01-021-025}

¿Qué cota elimina el testigo de Lagrange?

[]{#MA-MSOL-ANM-01-021-025}

<details class="anm-solution">
<summary>Ver solución del microcontrol 25</summary>

**Respuesta.**

Una cota $|f^{(n+1)}|\le M$ válida en todo el interior donde puede estar el testigo.

**Fundamento en la sección 21.4.**

La fórmula exacta contiene un punto desconocido. Para certificar error conviene eliminarlo mediante una cota que controle todas sus ubicaciones posibles. Bajo el contrato anterior, si $|f^{(n+1)}(t)|\le M$ en todo el interior del segmento, con $M\ge0$, obtenemos

$$|R_{n,c}(x)|\le\frac{M}{(n+1)!}|x-c|^{n+1}.$$

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

</details>

#### Microcontrol 26

[]{#MA-MIC-ANM-01-021-026}

¿Qué hacer si $M=0$?

[]{#MA-MSOL-ANM-01-021-026}

<details class="anm-solution">
<summary>Ver solución del microcontrol 26</summary>

**Respuesta.**

La cota obliga al resto a ser cero; no se divide por$M$.

**Fundamento en la sección 21.4.**

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

Cuando la misma $M$ sirve en el interior de $[c-\rho,c+\rho]$, el mismo número $M\rho^{n+1}/(n+1)!$ acota todos los errores de ese segmento. El orden lógico es región, cota universal, entrada y testigo; tomar un máximo sobre puntos desconocidos sin justificarlo no resuelve el problema.

</details>

#### Microcontrol 27

[]{#MA-MIC-ANM-01-021-027}

¿Qué número controla todos los errores si $|x-c|\le\rho$?

[]{#MA-MSOL-ANM-01-021-027}

<details class="anm-solution">
<summary>Ver solución del microcontrol 27</summary>

**Respuesta.**

$M\rho^{n+1}/(n+1)!$, siempre que la misma cota de derivada valga en toda la región.

**Fundamento en la sección 21.4.**

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

Cuando la misma $M$ sirve en el interior de $[c-\rho,c+\rho]$, el mismo número $M\rho^{n+1}/(n+1)!$ acota todos los errores de ese segmento. El orden lógico es región, cota universal, entrada y testigo; tomar un máximo sobre puntos desconocidos sin justificarlo no resuelve el problema.

</details>

#### Microcontrol 28

[]{#MA-MIC-ANM-01-021-028}

¿Qué función permite derivar telescópicamente la forma de Cauchy?

[]{#MA-MSOL-ANM-01-021-028}

<details class="anm-solution">
<summary>Ver solución del microcontrol 28</summary>

**Respuesta.**

$G(t)=f(x)-\sum_{k=0}^n f^{(k)}(t)(x-t)^k/k!$, con$x$ fijado.

**Fundamento en la sección 21.4.**

También hay una forma exacta de Cauchy. En el contrato abierto de21.3, fijemos $x$ y dejemos variar el centro auxiliar $t$:

$$G(t)=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k.$$

En el extremo $t=x$, el término de grado cero da $G(x)=0$; en $t=c$ tenemos $G(c)=R_{n,c}(x)$. Al derivar, la parte que deriva $f^{(k)}$ cancela con la que deriva la potencia del término siguiente. Los dos sumatorios finitos dejan

$$G'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n.$$

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

</details>

#### Microcontrol 29

[]{#MA-MIC-ANM-01-021-029}

¿Cuál es su derivada después de cancelar términos?

[]{#MA-MSOL-ANM-01-021-029}

<details class="anm-solution">
<summary>Ver solución del microcontrol 29</summary>

**Respuesta.**

$G\prime(t)=-f^{(n+1)}(t)(x-t)^n/n!$.

**Fundamento en la sección 21.4.**

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

$$R_{n,c}(x)=\frac{f^{(n+1)}(\eta)}{n!}(x-\eta)^n(x-c).$$

El signo procede de $G(x)-G(c)=-R_{n,c}(x)$ y del signo negativo de $G'$. Para $n=0$ la potencia vale1, sin un cociente nulo. Como $|x-\eta|\le|x-c|$, una cota absoluta da $|R|\le M|x-c|^{n+1}/n!$. Es válida aunque, con una cota constante, suele ser menos ajustada que Lagrange. Las dos formas pueden tener testigos diferentes.

</details>

#### Microcontrol 30

[]{#MA-MIC-ANM-01-021-030}

¿Qué forma tiene el resto de Cauchy?

[]{#MA-MSOL-ANM-01-021-030}

<details class="anm-solution">
<summary>Ver solución del microcontrol 30</summary>

**Respuesta.**

$R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$, con$\eta$ estrictamente interior.

**Fundamento en la sección 21.4.**

También hay una forma exacta de Cauchy. En el contrato abierto de21.3, fijemos $x$ y dejemos variar el centro auxiliar $t$:

$$G(t)=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k.$$

En el extremo $t=x$, el término de grado cero da $G(x)=0$; en $t=c$ tenemos $G(c)=R_{n,c}(x)$. Al derivar, la parte que deriva $f^{(k)}$ cancela con la que deriva la potencia del término siguiente. Los dos sumatorios finitos dejan

$$G'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n.$$

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

</details>

#### Microcontrol 31

[]{#MA-MIC-ANM-01-021-031}

¿Los testigos de Lagrange y Cauchy tienen que coincidir?

[]{#MA-MSOL-ANM-01-021-031}

<details class="anm-solution">
<summary>Ver solución del microcontrol 31</summary>

**Respuesta.**

No. Son existencias obtenidas de auxiliares diferentes.

**Fundamento en la sección 21.4.**

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

$$R_{n,c}(x)=\frac{f^{(n+1)}(\eta)}{n!}(x-\eta)^n(x-c).$$

El signo procede de $G(x)-G(c)=-R_{n,c}(x)$ y del signo negativo de $G'$. Para $n=0$ la potencia vale1, sin un cociente nulo. Como $|x-\eta|\le|x-c|$, una cota absoluta da $|R|\le M|x-c|^{n+1}/n!$. Es válida aunque, con una cota constante, suele ser menos ajustada que Lagrange. Las dos formas pueden tener testigos diferentes.

</details>

#### Microcontrol 32

[]{#MA-MIC-ANM-01-021-032}

¿Qué ocurre al multiplicar la banda de coeficientes por un incremento elevado negativo?

[]{#MA-MSOL-ANM-01-021-032}

<details class="anm-solution">
<summary>Ver solución del microcontrol 32</summary>

**Respuesta.**

Se invierte el orden de las cotas; una banda firmada exige controlar paridad y lado del centro.

**Fundamento en la sección 21.4.**

Si $m\le f^{(n+1)}\le M$, el coeficiente $R/(x-c)^{n+1}$ de Lagrange está entre $m/(n+1)!$ y $M/(n+1)!$. Para transformarlo en una banda del resto hay que atender al signo de $(x-c)^{n+1}$. Si es negativo, el orden de las cotas se invierte. Una cota absoluta evita este cambio; una banda firmada conserva información direccional.

Con $n=1$, el exponente2 siempre es no negativo y recuperamos las bandas cuadráticas de C20. Si $n=2$ y $f'''$ es positiva, el resto es positivo a la derecha del centro y negativo a su izquierda. «Error pequeño» y «error de signo conocido» son conclusiones diferentes.

</details>

### Ejercicios de la sección 21.4

#### Ejercicio 16. Una cota que no necesita máximo

[]{#MA-EX-ANM-01-021-016}

Deriva la cota absoluta de resto desde Lagrange con$|f^{(n+1)}|\le M$. Incluye$x=c$ y$M=0$ y explica por qué no se requiere derivada final continua.

[]{#MA-SOL-ANM-01-021-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

**Respuesta.**

Para$x\ne c$, tomamos valores absolutos en$R=f^{(n+1)}(\xi)(x-c)^{n+1}/(n+1)!$ y aplicamos la cota universal en$\xi$. Resulta$|R|\le M|x-c|^{n+1}/(n+1)!$. Si$x=c$, ambos lados son0. Si$M=0$, la desigualdad fuerza$R=0$ sin dividir por$M$. Una cota suministrada controla todos los valores posibles del testigo; no se necesita obtenerla como máximo alcanzado ni presuponer continuidad de la derivada final.

**Fundamento en la sección 21.4.**

La fórmula exacta contiene un punto desconocido. Para certificar error conviene eliminarlo mediante una cota que controle todas sus ubicaciones posibles. Bajo el contrato anterior, si $|f^{(n+1)}(t)|\le M$ en todo el interior del segmento, con $M\ge0$, obtenemos

$$|R_{n,c}(x)|\le\frac{M}{(n+1)!}|x-c|^{n+1}.$$

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

</details>

#### Ejercicio 17. La cancelación de Cauchy

[]{#MA-EX-ANM-01-021-017}

Calcula la derivada de$G(t)=f(x)-\sum_{k=0}^n f^{(k)}(t)(x-t)^k/k!$ con$x$ fijado y deduce su forma de resto.

[]{#MA-SOL-ANM-01-021-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

**Respuesta.**

Derivamos la suma finita. La parte que deriva$f^{(k)}$ es$\sum_{k=0}^n f^{(k+1)}(t)(x-t)^k/k!$; la que deriva la potencia es$-\sum_{k=1}^n f^{(k)}(t)(x-t)^{k-1}/(k-1)!$. Tras reindexar la segunda, se cancelan todos salvo el término superior de la primera. Como$G$ es negativo de la suma más una constante,$G\prime=-f^{(n+1)}(t)(x-t)^n/n!$. Se tiene$G(x)=0$ y$G(c)=R$. Lagrange sobre$G$ da$-R=G\prime(\eta)(x-c)$; sustituir produce$R=f^{(n+1)}(\eta)(x-\eta)^n(x-c)/n!$.

**Retorno visual.** Véase [C21-F04](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.4.**

También hay una forma exacta de Cauchy. En el contrato abierto de21.3, fijemos $x$ y dejemos variar el centro auxiliar $t$:

$$G(t)=f(x)-\sum_{k=0}^n\frac{f^{(k)}(t)}{k!}(x-t)^k.$$

En el extremo $t=x$, el término de grado cero da $G(x)=0$; en $t=c$ tenemos $G(c)=R_{n,c}(x)$. Al derivar, la parte que deriva $f^{(k)}$ cancela con la que deriva la potencia del término siguiente. Los dos sumatorios finitos dejan

$$G'(t)=-\frac{f^{(n+1)}(t)}{n!}(x-t)^n.$$

Esta cancelación puede comprobarse término a término; para $n=0$ sólo hay $G'=-f'$. Lagrange aplicado a $G$ en el segmento, o Cauchy de C19 con la segunda función $t$, produce un $\eta$ estrictamente interior con

</details>

#### Ejercicio 18. Una banda que cambia de orientación

[]{#MA-EX-ANM-01-021-018}

Si$2\le f^{(3)}\le6$ entre$c$ y$x$, escribe las bandas firmadas para el resto de orden2 cuando$x>c$ y cuando$x<c$.

[]{#MA-SOL-ANM-01-021-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

**Respuesta.**

El coeficiente$R/(x-c)^3$ queda entre2/6=1/3 y6/6=1. Si$x>c$, la potencia es positiva y$(x-c)^3/3\le R\le(x-c)^3$. Si$x<c$, la potencia es negativa y se invierte el orden:$(x-c)^3\le R\le(x-c)^3/3$. En el centro$R=0$. En ambos lados la cota absoluta$|R|\le|x-c|^3$ sigue siendo válida, pero la banda firmada retiene el signo.

**Fundamento en la sección 21.4.**

Si $m\le f^{(n+1)}\le M$, el coeficiente $R/(x-c)^{n+1}$ de Lagrange está entre $m/(n+1)!$ y $M/(n+1)!$. Para transformarlo en una banda del resto hay que atender al signo de $(x-c)^{n+1}$. Si es negativo, el orden de las cotas se invierte. Una cota absoluta evita este cambio; una banda firmada conserva información direccional.

Con $n=1$, el exponente2 siempre es no negativo y recuperamos las bandas cuadráticas de C20. Si $n=2$ y $f'''$ es positiva, el resto es positivo a la derecha del centro y negativo a su izquierda. «Error pequeño» y «error de signo conocido» son conclusiones diferentes.

</details>

#### Ejercicio 19. Testigos diferentes para el mismo error

[]{#MA-EX-ANM-01-021-019}

Para$t^3$, centro0, entrada1 y orden1, encuentra un testigo de Cauchy y compáralo con el de Lagrange. Compara sus cotas con$|f\prime\prime|\le6$.

[]{#MA-SOL-ANM-01-021-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

**Respuesta.**

El resto es1. Lagrange dio$\xi=1/3$. Cauchy exige$1=6\eta(1-\eta)$; las soluciones$\eta=(1\pm1/\sqrt3)/2$ pertenecen a$(0,1)$ y ambas sirven. Ninguna es1/3. Con$M=6$, Lagrange da$|R|\le6/2=3$, mientras la estimación constante de Cauchy da$|R|\le6/1=6$. Ambas cotas son correctas aunque poco ajustadas frente al error exacto1; sus puntos y factores no se intercambian.

**Fundamento en la sección 21.4.**

El signo procede de $G(x)-G(c)=-R_{n,c}(x)$ y del signo negativo de $G'$. Para $n=0$ la potencia vale1, sin un cociente nulo. Como $|x-\eta|\le|x-c|$, una cota absoluta da $|R|\le M|x-c|^{n+1}/n!$. Es válida aunque, con una cota constante, suele ser menos ajustada que Lagrange. Las dos formas pueden tener testigos diferentes.

Si $m\le f^{(n+1)}\le M$, el coeficiente $R/(x-c)^{n+1}$ de Lagrange está entre $m/(n+1)!$ y $M/(n+1)!$. Para transformarlo en una banda del resto hay que atender al signo de $(x-c)^{n+1}$. Si es negativo, el orden de las cotas se invierte. Una cota absoluta evita este cambio; una banda firmada conserva información direccional.

</details>

#### Ejercicio 20. Una región antes de una entrada

[]{#MA-EX-ANM-01-021-020}

Supón$|f^{(n+1)}|\le M$ en el interior de$[c-\rho,c+\rho]$ bajo el contrato cerrado. Demuestra un control uniforme y explica por qué una muestra de esa derivada no lo sustituye.

[]{#MA-SOL-ANM-01-021-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

**Respuesta.**

Para cada entrada$x$ del segmento, la prueba de Lagrange se aplica a su subsegmento con$c$. Su testigo pertenece al interior de la región completa, donde vale la misma$M$. Así$|R(x)|\le M|x-c|^{n+1}/(n+1)!\le M\rho^{n+1}/(n+1)!$. El caso central es0. La cota se eligió antes de$x$ y sirve para todas las entradas, sin seleccionar sus testigos simultáneamente. Una muestra finita sólo acota valores muestreados, no cualquier ubicación interior que puede producir el teorema.

**Fundamento en la sección 21.4.**

La fórmula exacta contiene un punto desconocido. Para certificar error conviene eliminarlo mediante una cota que controle todas sus ubicaciones posibles. Bajo el contrato anterior, si $|f^{(n+1)}(t)|\le M$ en todo el interior del segmento, con $M\ge0$, obtenemos

$$|R_{n,c}(x)|\le\frac{M}{(n+1)!}|x-c|^{n+1}.$$

Para $x=c$ los dos lados son cero; para $x\ne c$ aplicamos la cota en un testigo suministrado por Lagrange. No hace falta que la derivada final alcance un máximo o sea continua. Si $M=0$, el resto es cero y no se divide por $M$.

</details>
## 21.5. Peano: lo que desaparece al cambiar de escala

[]{#MA-SEC-ANM-01-021-005}

La cota anterior gasta una derivada adicional. Existe una conclusión local bajo menos información: para $n\ge1$, si $f$ tiene derivadas hasta orden $n-1$ en un intervalo abierto alrededor de $c$, y la función $f^{(n-1)}$ es derivable en $c$, entonces

$$R_{n,c}(c+h)=o(|h|^n)\qquad(h\to0).$$

Para $n=1$ la hipótesis significa solamente que $f$ es derivable en $c$; no pide derivabilidad en otros centros. Para $n\ge2$ las derivadas inferiores existen en un entorno, pero la de orden $n$ se exige sólo en el centro. El símbolo $o$ abrevia la condición: para cada $\varepsilon>0$ existe $\delta>0$ tal que

$$0<|h|<\delta\ \Longrightarrow\ |R_{n,c}(c+h)|<\varepsilon|h|^n.$$

El radio se mantiene dentro del dominio. La forma de **Peano** dice que el error normalizado desaparece; no suministra por sí sola una constante para $|h|^{n+1}$ ni un radio numérico calculable.

Demostremos por inducción. Para $n=1$ es exactamente la definición de derivada en $c$, multiplicada por $|h|$. Para el paso $n\ge2$, pongamos $H=f-T_{n,c}f$. El polinomio conserva todos los datos centrales, por lo que $H^{(k)}(c)=0$ para $0\le k\le n$. Aplicamos la hipótesis inductiva a $H'$ con orden $n-1$: su polinomio central es cero y

$$H'(c+u)=o(|u|^{n-1}).$$

Fijada $\varepsilon>0$, elegimos un radio donde $|H'(c+u)|<n\varepsilon|u|^{n-1}$ para toda entrada perforada. Para $0<|h|$ dentro de ese radio, Cauchy de C19 entre $c$ y $c+h$, con funciones $H(t)$ y $(t-c)^n$, da un $\xi$ interior:

$$\frac{H(c+h)}{h^n}=
\frac{H'(\xi)}{n(\xi-c)^{n-1}}.$$

Ambas funciones son continuas en el segmento y derivables en su interior: para $n\ge2$ se dispone de $H'$ en el entorno. El denominador de la derivada no es cero porque $\xi\ne c$. El incremento de la potencia es $h^n\ne0$. La cota inductiva en $\xi$ hace que el valor absoluto del cociente sea menor que $\varepsilon$. Así termina la inducción sin derivada de orden $n+1$ ni continuidad supuesta de la derivada de orden $n$ en un entorno.

Para $n=0$, la afirmación $f(c+h)-f(c)=o(1)$ es continuidad en $c$ y se trata separadamente. Tampoco se deriva un resto pequeño: de $r(h)=o(|h|^n)$ no se puede inferir una fórmula para $r'(h)$ sin hipótesis adicionales.

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

![Para R=h²√|h|, el cociente por |h|² es √|h| y tiende a cero, mientras el cociente por |h|³ es1/√|h| y no está acotado cerca de cero. Se representan distancias positivas con escala logarítmica y se excluye la entrada0. Las identidades y radios, no el dibujo, prueban ambos comportamientos.](../../assets/books/anm/C21/C21-F05.svg){#fig-anm-c21-f05 fig-alt="Para R=h²√|h|, el cociente por |h|² es √|h| y tiende a cero, mientras el cociente por |h|³ es1/√|h| y no está acotado cerca de cero. Se representan distancias positivas con escala logarítmica y se excluye la entrada0. Las identidades y radios, no el dibujo, prueban ambos comportamientos."}

La escala correcta es parte del enunciado: un error que tiende a cero en valor absoluto puede seguir siendo enorme al dividirlo por $|h|^n$. El zoom muestra una regla normalizada ya demostrada y no sustituye el radio que controla todas las entradas.

### Microcontroles

#### Microcontrol 33

[]{#MA-MIC-ANM-01-021-033}

¿Qué significa $R(c+h)=o(|h|^n)$?

[]{#MA-MSOL-ANM-01-021-033}

<details class="anm-solution">
<summary>Ver solución del microcontrol 33</summary>

**Respuesta.**

Para cada$\varepsilon>0$ hay un radio que hace$|R(c+h)|<\varepsilon|h|^n$ en todas las entradas perforadas de ese radio.

**Fundamento en la sección 21.5.**

Fijada $\varepsilon>0$, elegimos un radio donde $|H'(c+u)|<n\varepsilon|u|^{n-1}$ para toda entrada perforada. Para $0<|h|$ dentro de ese radio, Cauchy de C19 entre $c$ y $c+h$, con funciones $H(t)$ y $(t-c)^n$, da un $\xi$ interior:

$$\frac{H(c+h)}{h^n}=
\frac{H'(\xi)}{n(\xi-c)^{n-1}}.$$

Ambas funciones son continuas en el segmento y derivables en su interior: para $n\ge2$ se dispone de $H'$ en el entorno. El denominador de la derivada no es cero porque $\xi\ne c$. El incremento de la potencia es $h^n\ne0$. La cota inductiva en $\xi$ hace que el valor absoluto del cociente sea menor que $\varepsilon$. Así termina la inducción sin derivada de orden $n+1$ ni continuidad supuesta de la derivada de orden $n$ en un entorno.

</details>

#### Microcontrol 34

[]{#MA-MIC-ANM-01-021-034}

¿Qué caso de Peano corresponde a$n=1$?

[]{#MA-MSOL-ANM-01-021-034}

<details class="anm-solution">
<summary>Ver solución del microcontrol 34</summary>

**Respuesta.**

La definición de derivada en el centro; no exige derivabilidad de la función en otros centros.

**Fundamento en la sección 21.5.**

La cota anterior gasta una derivada adicional. Existe una conclusión local bajo menos información: para $n\ge1$, si $f$ tiene derivadas hasta orden $n-1$ en un intervalo abierto alrededor de $c$, y la función $f^{(n-1)}$ es derivable en $c$, entonces

$$R_{n,c}(c+h)=o(|h|^n)\qquad(h\to0).$$

Para $n=1$ la hipótesis significa solamente que $f$ es derivable en $c$; no pide derivabilidad en otros centros. Para $n\ge2$ las derivadas inferiores existen en un entorno, pero la de orden $n$ se exige sólo en el centro. El símbolo $o$ abrevia la condición: para cada $\varepsilon>0$ existe $\delta>0$ tal que

</details>

#### Microcontrol 35

[]{#MA-MIC-ANM-01-021-035}

¿Dónde se exige la derivada de orden$n$ en el contrato de Peano?

[]{#MA-MSOL-ANM-01-021-035}

<details class="anm-solution">
<summary>Ver solución del microcontrol 35</summary>

**Respuesta.**

Sólo en el centro, como derivada de$f^{(n-1)}$; las inferiores necesarias están definidas en un entorno.

**Fundamento en la sección 21.5.**

Para $n=1$ la hipótesis significa solamente que $f$ es derivable en $c$; no pide derivabilidad en otros centros. Para $n\ge2$ las derivadas inferiores existen en un entorno, pero la de orden $n$ se exige sólo en el centro. El símbolo $o$ abrevia la condición: para cada $\varepsilon>0$ existe $\delta>0$ tal que

$$0<|h|<\delta\ \Longrightarrow\ |R_{n,c}(c+h)|<\varepsilon|h|^n.$$

El radio se mantiene dentro del dominio. La forma de **Peano** dice que el error normalizado desaparece; no suministra por sí sola una constante para $|h|^{n+1}$ ni un radio numérico calculable.

</details>

#### Microcontrol 36

[]{#MA-MIC-ANM-01-021-036}

¿Qué herramienta recupera$H$ desde una cota para$H\prime$ en la inducción?

[]{#MA-MSOL-ANM-01-021-036}

<details class="anm-solution">
<summary>Ver solución del microcontrol 36</summary>

**Respuesta.**

Cauchy sobre$H$ y$(t-c)^n$, cuyo cociente de derivadas divide por$n(\xi-c)^{n-1}\ne0$.

**Fundamento en la sección 21.5.**

Fijada $\varepsilon>0$, elegimos un radio donde $|H'(c+u)|<n\varepsilon|u|^{n-1}$ para toda entrada perforada. Para $0<|h|$ dentro de ese radio, Cauchy de C19 entre $c$ y $c+h$, con funciones $H(t)$ y $(t-c)^n$, da un $\xi$ interior:

$$\frac{H(c+h)}{h^n}=
\frac{H'(\xi)}{n(\xi-c)^{n-1}}.$$

Ambas funciones son continuas en el segmento y derivables en su interior: para $n\ge2$ se dispone de $H'$ en el entorno. El denominador de la derivada no es cero porque $\xi\ne c$. El incremento de la potencia es $h^n\ne0$. La cota inductiva en $\xi$ hace que el valor absoluto del cociente sea menor que $\varepsilon$. Así termina la inducción sin derivada de orden $n+1$ ni continuidad supuesta de la derivada de orden $n$ en un entorno.

</details>

#### Microcontrol 37

[]{#MA-MIC-ANM-01-021-037}

¿Peano proporciona una constante para$|h|^{n+1}$?

[]{#MA-MSOL-ANM-01-021-037}

<details class="anm-solution">
<summary>Ver solución del microcontrol 37</summary>

**Respuesta.**

No. Describe un error normalizado que tiende a cero, sin garantizar una cota del siguiente orden.

**Fundamento en la sección 21.5.**

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

La escala correcta es parte del enunciado: un error que tiende a cero en valor absoluto puede seguir siendo enorme al dividirlo por $|h|^n$. El zoom muestra una regla normalizada ya demostrada y no sustituye el radio que controla todas las entradas.

</details>

#### Microcontrol 38

[]{#MA-MIC-ANM-01-021-038}

¿Qué cociente tiende a cero para$h^2\sqrt{|h|}$ a orden2?

[]{#MA-MSOL-ANM-01-021-038}

<details class="anm-solution">
<summary>Ver solución del microcontrol 38</summary>

**Respuesta.**

$f(h)/|h|^2=\sqrt{|h|}\to0$.

**Fundamento en la sección 21.5.**

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

</details>

#### Microcontrol 39

[]{#MA-MIC-ANM-01-021-039}

¿Por qué ese ejemplo no tiene una cota$C|h|^3$ en un radio?

[]{#MA-MSOL-ANM-01-021-039}

<details class="anm-solution">
<summary>Ver solución del microcontrol 39</summary>

**Respuesta.**

Su cociente por$|h|^3$ es$1/\sqrt{|h|}$, no acotado cerca de cero.

**Fundamento en la sección 21.5.**

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

</details>

#### Microcontrol 40

[]{#MA-MIC-ANM-01-021-040}

¿Puede derivarse un símbolo$o$ sin hipótesis adicionales?

[]{#MA-MSOL-ANM-01-021-040}

<details class="anm-solution">
<summary>Ver solución del microcontrol 40</summary>

**Respuesta.**

No. Un control de valores del resto no proporciona automáticamente un control de su derivada.

**Fundamento en la sección 21.5.**

Para $n=0$, la afirmación $f(c+h)-f(c)=o(1)$ es continuidad en $c$ y se trata separadamente. Tampoco se deriva un resto pequeño: de $r(h)=o(|h|^n)$ no se puede inferir una fórmula para $r'(h)$ sin hipótesis adicionales.

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

</details>

### Ejercicios de la sección 21.5

#### Ejercicio 21. Peano por Cauchy e inducción

[]{#MA-EX-ANM-01-021-021}

Prueba el paso inductivo de Peano de orden$n\ge2$ a partir del resultado para$H\prime$, con$H=f-T_{n,c}f$. Declara el denominador no nulo.

[]{#MA-SOL-ANM-01-021-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

**Respuesta.**

Los datos centrales de$H$ hasta orden$n$ son0. El resultado de orden$n-1$ aplicado a$H\prime$ da$H\prime(c+u)=o(|u|^{n-1})$. Para$\varepsilon>0$ tomamos un radio donde$|H\prime(c+u)|<n\varepsilon|u|^{n-1}$. Para$0<|h|$ dentro del radio, Cauchy en$H$ y$(t-c)^n$ da$H(c+h)/h^n=H\prime(\xi)/[n(\xi-c)^{n-1}]$. El testigo no es$c$, así la derivada del denominador no se anula; el incremento$h^n$ tampoco. La cota inductiva hace al valor absoluto del cociente menor que$\varepsilon$. Se requiere que$H\prime$ exista en el segmento, garantizado por las hipótesis inferiores para$n\ge2$.

**Fundamento en la sección 21.5.**

Fijada $\varepsilon>0$, elegimos un radio donde $|H'(c+u)|<n\varepsilon|u|^{n-1}$ para toda entrada perforada. Para $0<|h|$ dentro de ese radio, Cauchy de C19 entre $c$ y $c+h$, con funciones $H(t)$ y $(t-c)^n$, da un $\xi$ interior:

$$\frac{H(c+h)}{h^n}=
\frac{H'(\xi)}{n(\xi-c)^{n-1}}.$$

Ambas funciones son continuas en el segmento y derivables en su interior: para $n\ge2$ se dispone de $H'$ en el entorno. El denominador de la derivada no es cero porque $\xi\ne c$. El incremento de la potencia es $h^n\ne0$. La cota inductiva en $\xi$ hace que el valor absoluto del cociente sea menor que $\varepsilon$. Así termina la inducción sin derivada de orden $n+1$ ni continuidad supuesta de la derivada de orden $n$ en un entorno.

</details>

#### Ejercicio 22. Peano sin un orden cúbico de error

[]{#MA-EX-ANM-01-021-022}

Para$f(h)=h^2\sqrt{|h|}$, verifica los datos centrales hasta orden2 y demuestra$o(|h|^2)$ pero ausencia de cota$C|h|^3$ cerca de cero.

[]{#MA-SOL-ANM-01-021-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

**Respuesta.**

$f(0)=0$ y$f(h)/h=\operatorname{sgn}(h)|h|^{3/2}\to0$, así$f\prime(0)=0$. Fuera de0,$f\prime(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$. Dividir por$h$ da$(5/2)\sqrt{|h|}\to0$, luego$f\prime\prime(0)=0$. El Taylor de orden2 es cero. El cociente$f(h)/|h|^2=\sqrt{|h|}$ tiende a0, pero$f(h)/|h|^3=1/\sqrt{|h|}$ excede cualquier constante finita tomando entradas suficientemente pequeñas. El resultado es Peano sin una cota uniforme del siguiente orden.

**Retorno visual.** Véase [C21-F05](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f05), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.5.**

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

</details>

#### Ejercicio 23. Error absoluto y error normalizado

[]{#MA-EX-ANM-01-021-023}

Para$n\ge1$, compara$r(h)=h^n$ y$s(h)=h^{n+1}$ cerca de cero. Decide qué errores son$o(|h|^n)$ y muestra por qué tender a cero no basta.

[]{#MA-SOL-ANM-01-021-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

**Respuesta.**

Ambas funciones tienden a0 en valor absoluto. Pero$|r(h)|/|h|^n=1$ en todas las entradas perforadas, así no tiende a0 y$r$ no es$o(|h|^n)$. En cambio$|s(h)|/|h|^n=|h|\to0$, y$s$ sí tiene esa propiedad. Peano mide error respecto de una escala, no sólo tamaño absoluto.

**Fundamento en la sección 21.5.**

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

La escala correcta es parte del enunciado: un error que tiende a cero en valor absoluto puede seguir siendo enorme al dividirlo por $|h|^n$. El zoom muestra una regla normalizada ya demostrada y no sustituye el radio que controla todas las entradas.

</details>

#### Ejercicio 24. Un modelo asintótico también es único

[]{#MA-EX-ANM-01-021-024}

Si$P,Q$ tienen grado a lo sumo$n$ y$f-P=o(|h|^n)$ y$f-Q=o(|h|^n)$ en centro0, demuestra$P=Q$ sin derivar los restos.

[]{#MA-SOL-ANM-01-021-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

**Respuesta.**

La resta y la triangular dan$P-Q=o(|h|^n)$. Si el polinomio diferencia fuera no cero, tendría un término de menor grado$j\le n$ con coeficiente$a\ne0$: $P-Q=h^j(a+hB(h))$. Por continuidad del polinomio$B$, el factor interior tiende a$a$ y su valor absoluto es al menos$|a|/2$ en un radio. Dividir por$|h|^n$ da al menos$(|a|/2)|h|^{j-n}$, que no tiende a0: si$j=n$ es constante positiva y si$j<n$ crece sin cota. Contradicción. No se utilizó una regla de derivación para$o$.

**Fundamento en la sección 21.5.**

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

La escala correcta es parte del enunciado: un error que tiende a cero en valor absoluto puede seguir siendo enorme al dividirlo por $|h|^n$. El zoom muestra una regla normalizada ya demostrada y no sustituye el radio que controla todas las entradas.

</details>

#### Ejercicio 25. Un radio para un error de raíz

[]{#MA-EX-ANM-01-021-025}

Para el ejemplo de E022, produce un radio explícito que haga$|f(h)|<\varepsilon|h|^2$. Explica qué no prueba ese radio sobre una cota cúbica.

[]{#MA-SOL-ANM-01-021-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

**Respuesta.**

Como$|f(h)|/|h|^2=\sqrt{|h|}$, tomamos$\delta=\varepsilon^2$ o el mínimo con un radio de dominio. Para$0<|h|<\delta$ se cumple$\sqrt{|h|}<\varepsilon$ y la desigualdad requerida. Esto prueba Peano de orden2 con radio explícito para este ejemplo. No produce una constante cúbica: el cociente por$|h|^3$ sigue siendo$1/\sqrt{|h|}$, arbitrariamente grande.

**Fundamento en la sección 21.5.**

Un ejemplo distingue órdenes. Sea $f(h)=h^2\sqrt{|h|}$. En cero, $f'(0)=f''(0)=0$; fuera de cero, $f'(h)=(5/2)\operatorname{sgn}(h)|h|^{3/2}$ y $f''(h)=(15/4)\sqrt{|h|}$. Estas fórmulas se obtienen por producto y derivada de raíz en cada lado; los cocientes centrales verifican los dos valores nulos. Su polinomio de orden2 es cero y

$$\frac{f(h)}{|h|^2}=\sqrt{|h|}\to0,\qquad
\frac{f(h)}{|h|^3}=\frac1{\sqrt{|h|}}.$$

El segundo cociente es no acotado cerca de cero. Hay resto de Peano de orden2, pero no una cota $C|h|^3$ con constante finita en un radio. La derivada tercera fuera de cero es no acotada; que existan testigos de Lagrange en segmentos unilaterales no crea una cota uniforme.

</details>
## 21.6. La primera derivada que no se anula

[]{#MA-SEC-ANM-01-021-006}

Taylor local puede decidir la forma de una función cerca de un centro, incluso cuando las primeras pendientes no distinguen el caso. Supongamos las hipótesis de Peano de orden $m\ge1$, que $f^{(k)}(c)=0$ para $1\le k<m$, y que $f^{(m)}(c)\ne0$. Con $a=f^{(m)}(c)/m!$,

$$f(c+h)-f(c)=ah^m+r(h),\qquad r(h)=o(|h|^m).$$

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

Si todos los datos hasta orden $n$ se anulan, el criterio guarda silencio. Los polinomios $h^{2(n+1)}$, $-h^{2(n+1)}$ y $h^{2(n+1)+1}$ tienen los mismos datos hasta ese orden, incluidos el valor cero, y respectivamente presentan mínimo, máximo y ausencia de extremo en cero. No se dice que sus primeras derivadas no nulas sean las mismas: precisamente esa información está fuera del paquete de datos fijado.

La conclusión es local, no global. $q(h)=h^2-h^4$ tiene un mínimo local estricto en cero por el primer término no nulo positivo de orden2. Pero $q(2)=-12<q(0)=0$, de modo que cero no es un mínimo global. C20 podía pasar de pendiente cero a mínimo global porque añadía convexidad en todo el intervalo. No intercambiamos esa hipótesis con un desarrollo central.

Para un error de signo conocido también importa la paridad. Si $f^{(n+1)}$ tiene signo positivo en todo el segmento y no es cero en el testigo, el resto de Lagrange tiene el signo de $(x-c)^{n+1}$. En cambio Peano no ofrece un signo del resto; permite controlar su tamaño relativo frente a un término principal no nulo.

![En cero, h⁴ tiene primer coeficiente no nulo positivo de orden4 y mínimo estricto; h³ lo tiene de orden3 y cambia de signo. El criterio usa un radio donde el resto no supera la mitad del término principal y exige un centro interior con ambos lados.](../../assets/books/anm/C21/C21-F06.svg){#fig-anm-c21-f06 fig-alt="En cero, h⁴ tiene primer coeficiente no nulo positivo de orden4 y mínimo estricto; h³ lo tiene de orden3 y cambia de signo. El criterio usa un radio donde el resto no supera la mitad del término principal y exige un centro interior con ambos lados."}

Cuando el centro es borde, sólo hay un lado admisible y el caso impar puede comportarse como un extremo relativo. La función $x$ en $[0,1]$ tiene mínimo en cero. Antes de aplicar un criterio de paridad hay que fijar el dominio y sus entradas admisibles.

### Microcontroles

#### Microcontrol 41

[]{#MA-MIC-ANM-01-021-041}

¿Qué término decide el criterio de la primera derivada no nula?

[]{#MA-MSOL-ANM-01-021-041}

<details class="anm-solution">
<summary>Ver solución del microcontrol 41</summary>

**Respuesta.**

$ah^m$, con$a=f^{(m)}(c)/m!\ne0$, tras anular las derivadas anteriores.

**Fundamento en la sección 21.6.**

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

</details>

#### Microcontrol 42

[]{#MA-MIC-ANM-01-021-042}

¿Qué tolerancia evita que el resto cambie el signo principal?

[]{#MA-MSOL-ANM-01-021-042}

<details class="anm-solution">
<summary>Ver solución del microcontrol 42</summary>

**Respuesta.**

$|r(h)|<(|a|/2)|h|^m$ en un radio perforado.

**Fundamento en la sección 21.6.**

Taylor local puede decidir la forma de una función cerca de un centro, incluso cuando las primeras pendientes no distinguen el caso. Supongamos las hipótesis de Peano de orden $m\ge1$, que $f^{(k)}(c)=0$ para $1\le k<m$, y que $f^{(m)}(c)\ne0$. Con $a=f^{(m)}(c)/m!$,

$$f(c+h)-f(c)=ah^m+r(h),\qquad r(h)=o(|h|^m).$$

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

</details>

#### Microcontrol 43

[]{#MA-MIC-ANM-01-021-043}

¿Qué da un primer orden no nulo par con coeficiente positivo?

[]{#MA-MSOL-ANM-01-021-043}

<details class="anm-solution">
<summary>Ver solución del microcontrol 43</summary>

**Respuesta.**

Un mínimo local estricto en un centro interior, porque el término principal es positivo en ambos lados.

**Fundamento en la sección 21.6.**

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

</details>

#### Microcontrol 44

[]{#MA-MIC-ANM-01-021-044}

¿Qué da un primer orden no nulo impar?

[]{#MA-MSOL-ANM-01-021-044}

<details class="anm-solution">
<summary>Ver solución del microcontrol 44</summary>

**Respuesta.**

No hay extremo local interior: el incremento de la función cambia de signo entre ambos lados.

**Fundamento en la sección 21.6.**

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

</details>

#### Microcontrol 45

[]{#MA-MIC-ANM-01-021-045}

¿Qué concluye el criterio si todas las derivadas disponibles son cero?

[]{#MA-MSOL-ANM-01-021-045}

<details class="anm-solution">
<summary>Ver solución del microcontrol 45</summary>

**Respuesta.**

No clasifica el centro; datos de orden mayor pueden producir mínimo, máximo o ninguna de esas alternativas.

**Fundamento en la sección 21.6.**

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

Si todos los datos hasta orden $n$ se anulan, el criterio guarda silencio. Los polinomios $h^{2(n+1)}$, $-h^{2(n+1)}$ y $h^{2(n+1)+1}$ tienen los mismos datos hasta ese orden, incluidos el valor cero, y respectivamente presentan mínimo, máximo y ausencia de extremo en cero. No se dice que sus primeras derivadas no nulas sean las mismas: precisamente esa información está fuera del paquete de datos fijado.

</details>

#### Microcontrol 46

[]{#MA-MIC-ANM-01-021-046}

¿Un mínimo local de Taylor es automáticamente global?

[]{#MA-MSOL-ANM-01-021-046}

<details class="anm-solution">
<summary>Ver solución del microcontrol 46</summary>

**Respuesta.**

No. $h^2-h^4$ tiene mínimo local en cero y valores negativos lejos; convexidad global era una hipótesis adicional en C20.

**Fundamento en la sección 21.6.**

La conclusión es local, no global. $q(h)=h^2-h^4$ tiene un mínimo local estricto en cero por el primer término no nulo positivo de orden2. Pero $q(2)=-12<q(0)=0$, de modo que cero no es un mínimo global. C20 podía pasar de pendiente cero a mínimo global porque añadía convexidad en todo el intervalo. No intercambiamos esa hipótesis con un desarrollo central.

Para un error de signo conocido también importa la paridad. Si $f^{(n+1)}$ tiene signo positivo en todo el segmento y no es cero en el testigo, el resto de Lagrange tiene el signo de $(x-c)^{n+1}$. En cambio Peano no ofrece un signo del resto; permite controlar su tamaño relativo frente a un término principal no nulo.

</details>

#### Microcontrol 47

[]{#MA-MIC-ANM-01-021-047}

¿Qué cambia al aplicar paridad en una frontera?

[]{#MA-MSOL-ANM-01-021-047}

<details class="anm-solution">
<summary>Ver solución del microcontrol 47</summary>

**Respuesta.**

Puede faltar uno de los lados; por ejemplo la identidad tiene mínimo de borde en$[0,1]$.

**Fundamento en la sección 21.6.**

Cuando el centro es borde, sólo hay un lado admisible y el caso impar puede comportarse como un extremo relativo. La función $x$ en $[0,1]$ tiene mínimo en cero. Antes de aplicar un criterio de paridad hay que fijar el dominio y sus entradas admisibles.

</details>

#### Microcontrol 48

[]{#MA-MIC-ANM-01-021-048}

¿Peano determina por sí solo el signo del resto?

[]{#MA-MSOL-ANM-01-021-048}

<details class="anm-solution">
<summary>Ver solución del microcontrol 48</summary>

**Respuesta.**

No. Lo hace pequeño frente a un término principal no nulo; una cota firmada de Lagrange añade otra información.

**Fundamento en la sección 21.6.**

Para un error de signo conocido también importa la paridad. Si $f^{(n+1)}$ tiene signo positivo en todo el segmento y no es cero en el testigo, el resto de Lagrange tiene el signo de $(x-c)^{n+1}$. En cambio Peano no ofrece un signo del resto; permite controlar su tamaño relativo frente a un término principal no nulo.

Cuando el centro es borde, sólo hay un lado admisible y el caso impar puede comportarse como un extremo relativo. La función $x$ en $[0,1]$ tiene mínimo en cero. Antes de aplicar un criterio de paridad hay que fijar el dominio y sus entradas admisibles.

</details>

### Ejercicios de la sección 21.6

#### Ejercicio 26. Dominar el resto para decidir un signo

[]{#MA-EX-ANM-01-021-026}

Demuestra el criterio de la primera derivada no nula usando$ah^m+o(|h|^m)$ y una tolerancia explícita.

[]{#MA-SOL-ANM-01-021-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

**Respuesta.**

Como$a\ne0$, elegimos$\varepsilon=|a|/2$ en la condición$o$. En el radio resultante el error tiene magnitud menor que la mitad del término principal. Si$m$ es par, éste tiene signo$a$ en ambos lados, y la suma conserva ese signo: mínimo estricto para$a>0$ y máximo estricto para$a<0$. Si$m$ es impar, el principal cambia de signo de un lado a otro y el error no puede invertirlo; hay salidas mayores y menores arbitrariamente próximas. El centro debe ser interior para disponer de ambos lados.

**Fundamento en la sección 21.6.**

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

</details>

#### Ejercicio 27. Cuarto poder frente a cubo

[]{#MA-EX-ANM-01-021-027}

Compara$x^4$ y$x^3$ en cero por el primer orden diferencial no nulo y verifica las conclusiones directamente.

[]{#MA-SOL-ANM-01-021-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

**Respuesta.**

Para$x^4$, las primeras tres derivadas centrales son0 y la cuarta vale24; su coeficiente es24/4!=1. El orden par positivo da mínimo local estricto, y directamente$x^4>0$ para$x\ne0$. Para$x^3$, las primeras dos son0 y la tercera6, de coeficiente1. El orden impar da ausencia de extremo interior; directamente$x^3$ es negativo a la izquierda y positivo a la derecha. Una pendiente central cero común no distingue estos casos.

**Retorno visual.** Véase [C21-F06](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.6.**

Elegimos un radio donde $|r(h)|<(|a|/2)|h|^m$. Para entradas no nulas dentro de él, el término principal domina: el error no puede cambiar su signo. Si $m$ es par, $h^m=|h|^m$ en ambos lados. Con $a>0$ hay un mínimo local estricto; con $a<0$, un máximo local estricto. Si $m$ es impar, el término principal cambia de signo al cambiar el lado y por ello no hay extremo local. Se requieren entradas por ambos lados; el criterio se afirma en un centro interior.

Este argumento incluye el criterio de segunda derivada en un punto estacionario, pero no necesita que $f''$ sea continua en un entorno. También explica $x^4$ y $x^3$ en cero: el primer orden no nulo es4, positivo y par en el primer caso;3, positivo e impar en el segundo. Las funciones tienen derivada primera nula en cero, pero comportamientos distintos.

</details>

#### Ejercicio 28. Datos nulos con tres respuestas

[]{#MA-EX-ANM-01-021-028}

Para$n$ fijo, construye tres polinomios con iguales datos centrales hasta orden$n$ en0 y con mínimo, máximo y ningún extremo local allí.

[]{#MA-SOL-ANM-01-021-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

**Respuesta.**

Tomamos$p=h^{2(n+1)}$, $q=-h^{2(n+1)}$ y$r=h^{2(n+1)+1}$. Todos los exponentes superan$n$, por lo que el valor y las derivadas hasta ese orden se anulan en0. El primero es positivo en entradas no nulas y tiene mínimo estricto; el segundo negativo y tiene máximo estricto; el tercero cambia de signo y no tiene extremo interior. La falta de datos no nulos disponibles impide aplicar el criterio, no demuestra que no exista un extremo.

**Fundamento en la sección 21.6.**

Si todos los datos hasta orden $n$ se anulan, el criterio guarda silencio. Los polinomios $h^{2(n+1)}$, $-h^{2(n+1)}$ y $h^{2(n+1)+1}$ tienen los mismos datos hasta ese orden, incluidos el valor cero, y respectivamente presentan mínimo, máximo y ausencia de extremo en cero. No se dice que sus primeras derivadas no nulas sean las mismas: precisamente esa información está fuera del paquete de datos fijado.

La conclusión es local, no global. $q(h)=h^2-h^4$ tiene un mínimo local estricto en cero por el primer término no nulo positivo de orden2. Pero $q(2)=-12<q(0)=0$, de modo que cero no es un mínimo global. C20 podía pasar de pendiente cero a mínimo global porque añadía convexidad en todo el intervalo. No intercambiamos esa hipótesis con un desarrollo central.

</details>

#### Ejercicio 29. El mínimo que no gobierna toda la recta

[]{#MA-EX-ANM-01-021-029}

Para$q(h)=h^2-h^4$, prueba mínimo local estricto en0 y falla de mínimo global. Compara con la hipótesis de C20.

[]{#MA-SOL-ANM-01-021-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

**Respuesta.**

El primer orden no nulo es2, con$q\prime\prime(0)=2>0$, por lo que el criterio local da mínimo estricto. Directamente$q=h^2(1-h^2)>0$ para$0<|h|<1$. Pero$q(2)=4-16=-12<0$, así0 no es mínimo global. La segunda derivada$2-12h^2$ se vuelve negativa; no hay convexidad global que permita utilizar el soporte horizontal de C20. Un dato central positivo no reemplaza esa propiedad en todo el intervalo.

**Fundamento en la sección 21.6.**

Si todos los datos hasta orden $n$ se anulan, el criterio guarda silencio. Los polinomios $h^{2(n+1)}$, $-h^{2(n+1)}$ y $h^{2(n+1)+1}$ tienen los mismos datos hasta ese orden, incluidos el valor cero, y respectivamente presentan mínimo, máximo y ausencia de extremo en cero. No se dice que sus primeras derivadas no nulas sean las mismas: precisamente esa información está fuera del paquete de datos fijado.

La conclusión es local, no global. $q(h)=h^2-h^4$ tiene un mínimo local estricto en cero por el primer término no nulo positivo de orden2. Pero $q(2)=-12<q(0)=0$, de modo que cero no es un mínimo global. C20 podía pasar de pendiente cero a mínimo global porque añadía convexidad en todo el intervalo. No intercambiamos esa hipótesis con un desarrollo central.

</details>

#### Ejercicio 30. El orden impar en una frontera

[]{#MA-EX-ANM-01-021-030}

Explica por qué el criterio impar no excluye un mínimo de$x$ en0 sobre$[0,1]$. Declara una versión unilateral de la comparación de signos.

[]{#MA-SOL-ANM-01-021-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

**Respuesta.**

La función tiene primer coeficiente1 y orden1 impar, pero el dominio sólo ofrece incrementos$h\ge0$ desde el centro0. Para$h>0$, el término principal$h$ es positivo y no hay entradas negativas que produzcan el signo contrario. En$[0,1]$, la función alcanza mínimo único en0. Un desarrollo unilateral con error menor que la mitad del término principal certifica el signo en el lado disponible; la conclusión de ausencia de extremo del criterio impar requería centro interior y acumulación bilateral.

**Fundamento en la sección 21.6.**

Para un error de signo conocido también importa la paridad. Si $f^{(n+1)}$ tiene signo positivo en todo el segmento y no es cero en el testigo, el resto de Lagrange tiene el signo de $(x-c)^{n+1}$. En cambio Peano no ofrece un signo del resto; permite controlar su tamaño relativo frente a un término principal no nulo.

Cuando el centro es borde, sólo hay un lado admisible y el caso impar puede comportarse como un extremo relativo. La función $x$ en $[0,1]$ tiene mínimo en cero. Antes de aplicar un criterio de paridad hay que fijar el dominio y sus entradas admisibles.

</details>
## 21.7. Aproximantes con certificados racionales

[]{#MA-SEC-ANM-01-021-007}

Un número escrito en un aproximante no es todavía un certificado. Debemos identificar el dominio de todas las derivadas usadas y una cota válida en el segmento completo.

Primero tomemos $f(h)=1/(1-h)$ para $h<1$, centro0. Inducción con la regla del cociente da $f^{(k)}(h)=k!/(1-h)^{k+1}$ y por ello $T_{n,0}f(h)=\sum_{k=0}^n h^k$. La identidad geométrica finita proporciona un resto más preciso que un testigo:

$$(1-h)\sum_{k=0}^n h^k=1-h^{n+1},\qquad
R_{n,0}(h)=\frac{h^{n+1}}{1-h}.$$

Es una identidad de sumas finitas; no se ha usado una serie. En $|h|\le\rho<1$, $1-h\ge1-\rho>0$ y por tanto $|R|\le\rho^{n+1}/(1-\rho)$. La distancia a la singularidad es parte de la cota. No vale cruzar $h=1$ ni omitir ese margen.

Para una raíz, sea $g(h)=\sqrt{1+h}$, $h>-1$. C18 da

$$g'(h)=\frac1{2\sqrt{1+h}},\quad
g''(h)=-\frac1{4(1+h)^{3/2}},\quad
g'''(h)=\frac3{8(1+h)^{5/2}}.$$

Aquí $(1+h)^{3/2}$ y $(1+h)^{5/2}$ abrevian productos de potencias enteras por la raíz positiva; las fórmulas proceden de producto, cociente y cadena, no de una regla nueva para exponentes reales. En cero, el aproximante de orden2 es

$$T_{2,0}g(h)=1+\frac h2-\frac{h^2}8.$$

Para $|h|\le1/4$, $1+h\ge3/4$ y $\sqrt{1+h}\ge3/4$: la raíz de un número al menos3/4 es al menos3/4 por comparación de cuadrados y positividad. Así

$$0<g'''(h)\le\frac3{8(3/4)^2(3/4)}=\frac89.$$

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

![Para la raíz, T₂=1+h/2−h²/8 y en |h|≤1/4 vale |R₂|≤(4/27)|h|³. En h=1/4 el aproximante143/128 es inferior a √(5/4); Taylor acota su error por1/432 y racionalización por31/34688. Los extremos izquierdos abiertos indican error estrictamente positivo; no se infiere una coordenada de raíz desde la figura.](../../assets/books/anm/C21/C21-F07.svg){#fig-anm-c21-f07 fig-alt="Para la raíz, T₂=1+h/2−h²/8 y en |h|≤1/4 vale |R₂|≤(4/27)|h|³. En h=1/4 el aproximante143/128 es inferior a √(5/4); Taylor acota su error por1/432 y racionalización por31/34688. Los extremos izquierdos abiertos indican error estrictamente positivo; no se infiere una coordenada de raíz desde la figura."}

Ni el polinomio central ni unas pocas muestras detectan por sí solos el margen de dominio o el valor máximo posible de una derivada. El certificado reúne aproximante, región, hipótesis y cota; conserva el error como parte de la respuesta.

### Microcontroles

#### Microcontrol 49

[]{#MA-MIC-ANM-01-021-049}

¿Qué polinomio central tiene$1/(1-h)$ a orden$n$?

[]{#MA-MSOL-ANM-01-021-049}

<details class="anm-solution">
<summary>Ver solución del microcontrol 49</summary>

**Respuesta.**

$\sum_{k=0}^n h^k$, por$f^{(k)}(0)=k!$.

**Fundamento en la sección 21.7.**

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

Ni el polinomio central ni unas pocas muestras detectan por sí solos el margen de dominio o el valor máximo posible de una derivada. El certificado reúne aproximante, región, hipótesis y cota; conserva el error como parte de la respuesta.

</details>

#### Microcontrol 50

[]{#MA-MIC-ANM-01-021-050}

¿Cuál es su resto exacto finito?

[]{#MA-MSOL-ANM-01-021-050}

<details class="anm-solution">
<summary>Ver solución del microcontrol 50</summary>

**Respuesta.**

$h^{n+1}/(1-h)$, siempre que$h\ne1$ y dentro del dominio declarado.

**Fundamento en la sección 21.7.**

Un número escrito en un aproximante no es todavía un certificado. Debemos identificar el dominio de todas las derivadas usadas y una cota válida en el segmento completo.

Primero tomemos $f(h)=1/(1-h)$ para $h<1$, centro0. Inducción con la regla del cociente da $f^{(k)}(h)=k!/(1-h)^{k+1}$ y por ello $T_{n,0}f(h)=\sum_{k=0}^n h^k$. La identidad geométrica finita proporciona un resto más preciso que un testigo:

$$(1-h)\sum_{k=0}^n h^k=1-h^{n+1},\qquad
R_{n,0}(h)=\frac{h^{n+1}}{1-h}.$$

Es una identidad de sumas finitas; no se ha usado una serie. En $|h|\le\rho<1$, $1-h\ge1-\rho>0$ y por tanto $|R|\le\rho^{n+1}/(1-\rho)$. La distancia a la singularidad es parte de la cota. No vale cruzar $h=1$ ni omitir ese margen.

</details>

#### Microcontrol 51

[]{#MA-MIC-ANM-01-021-051}

¿Qué margen protege el denominador en$|h|\le\rho<1$?

[]{#MA-MSOL-ANM-01-021-051}

<details class="anm-solution">
<summary>Ver solución del microcontrol 51</summary>

**Respuesta.**

$1-h\ge1-\rho>0$, que produce$|R|\le\rho^{n+1}/(1-\rho)$.

**Fundamento en la sección 21.7.**

Primero tomemos $f(h)=1/(1-h)$ para $h<1$, centro0. Inducción con la regla del cociente da $f^{(k)}(h)=k!/(1-h)^{k+1}$ y por ello $T_{n,0}f(h)=\sum_{k=0}^n h^k$. La identidad geométrica finita proporciona un resto más preciso que un testigo:

$$(1-h)\sum_{k=0}^n h^k=1-h^{n+1},\qquad
R_{n,0}(h)=\frac{h^{n+1}}{1-h}.$$

Es una identidad de sumas finitas; no se ha usado una serie. En $|h|\le\rho<1$, $1-h\ge1-\rho>0$ y por tanto $|R|\le\rho^{n+1}/(1-\rho)$. La distancia a la singularidad es parte de la cota. No vale cruzar $h=1$ ni omitir ese margen.

Para una raíz, sea $g(h)=\sqrt{1+h}$, $h>-1$. C18 da

$$g'(h)=\frac1{2\sqrt{1+h}},\quad
g''(h)=-\frac1{4(1+h)^{3/2}},\quad
g'''(h)=\frac3{8(1+h)^{5/2}}.$$

</details>

#### Microcontrol 52

[]{#MA-MIC-ANM-01-021-052}

¿Qué polinomio de orden2 aproxima$\sqrt{1+h}$ en cero?

[]{#MA-MSOL-ANM-01-021-052}

<details class="anm-solution">
<summary>Ver solución del microcontrol 52</summary>

**Respuesta.**

$1+h/2-h^2/8$.

**Fundamento en la sección 21.7.**

Aquí $(1+h)^{3/2}$ y $(1+h)^{5/2}$ abrevian productos de potencias enteras por la raíz positiva; las fórmulas proceden de producto, cociente y cadena, no de una regla nueva para exponentes reales. En cero, el aproximante de orden2 es

$$T_{2,0}g(h)=1+\frac h2-\frac{h^2}8.$$

Para $|h|\le1/4$, $1+h\ge3/4$ y $\sqrt{1+h}\ge3/4$: la raíz de un número al menos3/4 es al menos3/4 por comparación de cuadrados y positividad. Así

$$0<g'''(h)\le\frac3{8(3/4)^2(3/4)}=\frac89.$$

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

</details>

#### Microcontrol 53

[]{#MA-MIC-ANM-01-021-053}

¿Qué cota racional de tercera derivada sirve en$|h|\le1/4$?

[]{#MA-MSOL-ANM-01-021-053}

<details class="anm-solution">
<summary>Ver solución del microcontrol 53</summary>

**Respuesta.**

$0<g^{(3)}\le8/9$, usando$1+h\ge3/4$ y$\sqrt{1+h}\ge3/4$.

**Fundamento en la sección 21.7.**

Para $|h|\le1/4$, $1+h\ge3/4$ y $\sqrt{1+h}\ge3/4$: la raíz de un número al menos3/4 es al menos3/4 por comparación de cuadrados y positividad. Así

$$0<g'''(h)\le\frac3{8(3/4)^2(3/4)}=\frac89.$$

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

</details>

#### Microcontrol 54

[]{#MA-MIC-ANM-01-021-054}

¿Qué certificado da Taylor para$\sqrt{5/4}$?

[]{#MA-MSOL-ANM-01-021-054}

<details class="anm-solution">
<summary>Ver solución del microcontrol 54</summary>

**Respuesta.**

$143/128<\sqrt{5/4}\le143/128+1/432$; el resto es positivo y está acotado.

**Fundamento en la sección 21.7.**

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

</details>

#### Microcontrol 55

[]{#MA-MIC-ANM-01-021-055}

¿Qué diferencia de cuadrados permite un cotejo independiente?

[]{#MA-MSOL-ANM-01-021-055}

<details class="anm-solution">
<summary>Ver solución del microcontrol 55</summary>

**Respuesta.**

$5/4-(143/128)^2=31/16384$; racionalizar y usar raíz al menos1 da error$\le31/34688$.

**Fundamento en la sección 21.7.**

Para $|h|\le1/4$, $1+h\ge3/4$ y $\sqrt{1+h}\ge3/4$: la raíz de un número al menos3/4 es al menos3/4 por comparación de cuadrados y positividad. Así

$$0<g'''(h)\le\frac3{8(3/4)^2(3/4)}=\frac89.$$

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

</details>

#### Microcontrol 56

[]{#MA-MIC-ANM-01-021-056}

¿Una muestra de derivada basta para certificar el error?

[]{#MA-MSOL-ANM-01-021-056}

<details class="anm-solution">
<summary>Ver solución del microcontrol 56</summary>

**Respuesta.**

No. La cota debe controlar todo el segmento donde puede encontrarse el testigo.

**Fundamento en la sección 21.7.**

Un número escrito en un aproximante no es todavía un certificado. Debemos identificar el dominio de todas las derivadas usadas y una cota válida en el segmento completo.

Primero tomemos $f(h)=1/(1-h)$ para $h<1$, centro0. Inducción con la regla del cociente da $f^{(k)}(h)=k!/(1-h)^{k+1}$ y por ello $T_{n,0}f(h)=\sum_{k=0}^n h^k$. La identidad geométrica finita proporciona un resto más preciso que un testigo:

$$(1-h)\sum_{k=0}^n h^k=1-h^{n+1},\qquad
R_{n,0}(h)=\frac{h^{n+1}}{1-h}.$$

Es una identidad de sumas finitas; no se ha usado una serie. En $|h|\le\rho<1$, $1-h\ge1-\rho>0$ y por tanto $|R|\le\rho^{n+1}/(1-\rho)$. La distancia a la singularidad es parte de la cota. No vale cruzar $h=1$ ni omitir ese margen.

</details>

### Ejercicios de la sección 21.7

#### Ejercicio 31. Una identidad geométrica todavía finita

[]{#MA-EX-ANM-01-021-031}

Demuestra$T_{n,0}(1/(1-h))=\sum_{k=0}^n h^k$ y calcula su resto exacto sin usar series.

[]{#MA-SOL-ANM-01-021-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

**Respuesta.**

Inducción con cociente y producto da$f^{(k)}=k!/(1-h)^{k+1}$; al evaluar en0 el coeficiente de Taylor es1. Multiplicar la suma finita por$1-h$ cancela términos vecinos y deja$1-h^{n+1}$. Como$1-h\ne0$ en el dominio$h<1$, despejamos la función y obtenemos resto$h^{n+1}/(1-h)$. No se tomó un límite de sumas ni se identificó una serie infinita.

**Fundamento en la sección 21.7.**

Un número escrito en un aproximante no es todavía un certificado. Debemos identificar el dominio de todas las derivadas usadas y una cota válida en el segmento completo.

Primero tomemos $f(h)=1/(1-h)$ para $h<1$, centro0. Inducción con la regla del cociente da $f^{(k)}(h)=k!/(1-h)^{k+1}$ y por ello $T_{n,0}f(h)=\sum_{k=0}^n h^k$. La identidad geométrica finita proporciona un resto más preciso que un testigo:

$$(1-h)\sum_{k=0}^n h^k=1-h^{n+1},\qquad
R_{n,0}(h)=\frac{h^{n+1}}{1-h}.$$

Es una identidad de sumas finitas; no se ha usado una serie. En $|h|\le\rho<1$, $1-h\ge1-\rho>0$ y por tanto $|R|\le\rho^{n+1}/(1-\rho)$. La distancia a la singularidad es parte de la cota. No vale cruzar $h=1$ ni omitir ese margen.

</details>

#### Ejercicio 32. La raíz y su tercera derivada

[]{#MA-EX-ANM-01-021-032}

Calcula$T_{2,0}\sqrt{1+h}$ y justifica la cota$0<g^{(3)}\le8/9$ en$|h|\le1/4$ con productos y raíces.

[]{#MA-SOL-ANM-01-021-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

**Respuesta.**

Por C18, $g\prime=1/(2\sqrt{1+h})$, $g\prime\prime=-1/[4(1+h)\sqrt{1+h}]$ y$g^{(3)}=3/[8(1+h)^2\sqrt{1+h}]$. En0 se obtienen1,1/2,−1/4, luego$T_2=1+h/2-h^2/8$. En el segmento$1+h\ge3/4$ y su raíz positiva es al menos3/4, pues$(3/4)^2\le3/4$. El denominador de la tercera derivada es al menos$8(3/4)^3=27/8$; el cociente queda a lo sumo8/9 y es positivo. No usamos derivación de una potencia real general.

**Fundamento en la sección 21.7.**

Para una raíz, sea $g(h)=\sqrt{1+h}$, $h>-1$. C18 da

$$g'(h)=\frac1{2\sqrt{1+h}},\quad
g''(h)=-\frac1{4(1+h)^{3/2}},\quad
g'''(h)=\frac3{8(1+h)^{5/2}}.$$

Aquí $(1+h)^{3/2}$ y $(1+h)^{5/2}$ abrevian productos de potencias enteras por la raíz positiva; las fórmulas proceden de producto, cociente y cadena, no de una regla nueva para exponentes reales. En cero, el aproximante de orden2 es

$$T_{2,0}g(h)=1+\frac h2-\frac{h^2}8.$$

Para $|h|\le1/4$, $1+h\ge3/4$ y $\sqrt{1+h}\ge3/4$: la raíz de un número al menos3/4 es al menos3/4 por comparación de cuadrados y positividad. Así

$$0<g'''(h)\le\frac3{8(3/4)^2(3/4)}=\frac89.$$

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

</details>

#### Ejercicio 33. Un intervalo racional para una raíz

[]{#MA-EX-ANM-01-021-033}

Usa E032 y Taylor–Lagrange para certificar$\sqrt{5/4}$ por un intervalo racional. Explica la inclusión estricta o débil de cada borde.

[]{#MA-SOL-ANM-01-021-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

**Respuesta.**

En$h=1/4$, $T_2=1+1/8-1/128=143/128$. La cota de tercera derivada8/9 da$|R_2|\le(8/9)(1/4)^3/6=1/432$. Como la tercera derivada es positiva en todo el segmento y el incremento cúbico es positivo, $R_2>0$. Así$143/128<\sqrt{5/4}\le143/128+1/432$. La primera desigualdad es estricta por signo; la segunda sólo es una cota superior no estricta. No se extrajo una raíz aproximada del dibujo.

**Retorno visual.** Véase [C21-F07](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

**Fundamento en la sección 21.7.**

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

</details>

#### Ejercicio 34. Un cotejo por racionalización

[]{#MA-EX-ANM-01-021-034}

Calcula un certificado de error para$143/128$ como aproximante de$\sqrt{5/4}$ mediante diferencia de cuadrados, y compáralo con$1/432$.

[]{#MA-SOL-ANM-01-021-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

**Respuesta.**

La diferencia es$5/4-20449/16384=31/16384>0$, por lo que el aproximante es inferior a la raíz positiva. Racionalizar da error$31/[16384(\sqrt{5/4}+143/128)]$. Como la raíz es al menos1, el denominador es al menos$16384(271/128)=34688$, y el error es a lo sumo31/34688. Para comparar, $31\cdot432=13392<34688$, así31/34688<1/432. La cota algebraica es más ajustada; ambas certifican el mismo aproximante con premisas distintas.

**Fundamento en la sección 21.7.**

Lagrange da $|R_2(h)|\le(4/27)|h|^3$. En $h=1/4$, el resto es positivo y

$$\frac{143}{128}<\sqrt{\frac54}\le\frac{143}{128}+\frac1{432}.$$

El primer número es el polinomio evaluado; la cantidad1/432 es un límite superior de error, no una cifra estimada desde una gráfica. La positividad estricta de la tercera derivada y $h>0$ justifican el extremo inferior abierto.

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

</details>

#### Ejercicio 35. La singularidad impone el margen

[]{#MA-EX-ANM-01-021-035}

Para$1/(1-h)$ con centro0 y$n$ fijo, demuestra la cota en$|h|\le\rho<1$ y explica por qué no se conserva una cota uniforme al acercarse a$h=1$.

[]{#MA-SOL-ANM-01-021-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

**Respuesta.**

El resto exacto es$h^{n+1}/(1-h)$. En la región declarada, $1-h\ge1-\rho>0$ y$|h|^{n+1}\le\rho^{n+1}$, así$|R|\le\rho^{n+1}/(1-\rho)$. Para$n$ fijo, si$h\uparrow1$, el numerador tiende a1 y el denominador positivo a0. Por ejemplo, para$h$ suficientemente próximo el numerador supera1/2, y tomar$1-h$ menor que$1/(2B)$ hace al resto mayor que cualquier$B>0$. El margen de dominio no puede borrarse.

**Fundamento en la sección 21.7.**

Podemos cotejar el certificado con un mecanismo algebraico independiente. La diferencia de cuadrados es $5/4-(143/128)^2=31/16384>0$. Racionalizar da

$$\sqrt{\frac54}-\frac{143}{128}
=\frac{31}{16384\left(\sqrt{5/4}+143/128\right)}
\le\frac{31}{34688}.$$

La última cota usa $\sqrt{5/4}\ge1$, así el denominador es al menos $16384(271/128)=34688$. Es más ajustada que1/432. La comparación no invalida Taylor: dos mecanismos pueden certificar la misma cantidad con eficiencias distintas.

Ni el polinomio central ni unas pocas muestras detectan por sí solos el margen de dominio o el valor máximo posible de una derivada. El certificado reúne aproximante, región, hipótesis y cota; conserva el error como parte de la respuesta.

</details>
## 21.8. Combinar modelos y elegir la resolución

[]{#MA-SEC-ANM-01-021-008}

Los modelos locales también pueden combinarse. Para un $n\ge1$ fijo y centro0, supongamos $f(h)=P(h)+u(h)$ y $g(h)=Q(h)+v(h)$, con polinomios de grado a lo sumo$n$ y $u,v=o(|h|^n)$. La suma tiene modelo $P+Q$ porque la triangular suma los dos errores normalizados.

Para el producto,

$$fg=PQ+Pv+Qu+uv.$$

Los polinomios son acotados en un radio por continuidad en cero. Dividir $Pv$ y $Qu$ por $|h|^n$ deja un factor acotado por otro que tiende a cero. Además $v(h)\to0$, y $|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Por tanto el error del producto respecto de $PQ$ es $o(|h|^n)$. Si $PQ$ tiene términos de grado mayor que$n$, los eliminamos: su suma finita es $h^{n+1}$ por otro polinomio, y al normalizar por $|h|^n$ tiende a cero. La parte truncada es un modelo del mismo orden, sin derivar el resto.

La sustitución exige conservar dominio y escala. Por ejemplo

$$F(h)=\frac1{1-h-h^2}.$$

En $|h|\le1/4$, el denominador es al menos $1-1/4-1/16=11/16>0$. Un cálculo exacto da

$$(1+h+2h^2)(1-h-h^2)=1-3h^3-2h^4,$$

y así

$$F(h)=1+h+2h^2+\frac{3h^3+2h^4}{1-h-h^2}.$$

El resto queda acotado por $(56/11)|h|^3$ en ese segmento. Además $F(0)=1$, $F'(0)=1$ y $F''(0)=4$, por cociente y cadena, de modo que el polinomio mostrado es realmente su Taylor de orden2. Sustituir una expresión en un modelo sin comprobar denominadores podría haber perdido precisamente esta garantía.

Para elegir un grado no basta pensar «más términos, menos error». Se fija primero una región y una tolerancia, y se prueba una cota en función del grado. Para $1/(1-h)$ en $|h|\le1/4$,21.7 da

$$|R_n(h)|\le\frac{(1/4)^{n+1}}{3/4}=\frac1{3\cdot4^n}.$$

El orden4 produce1/768, mayor que1/1000; el orden5 produce1/3072, menor. Esta cota uniforme certifica el objetivo1/1000 con orden5. Es además el menor orden que funciona con esta cota: los números decrecen al multiplicar por1/4, y en $h=1/4$ la igualdad del resto hace fallar cada orden hasta4. En esa entrada el polinomio de orden5 vale1365/1024 y su error frente a4/3 es exactamente1/3072.

![Para1/(1−h) en |h|≤1/4, el resto finito da cota1/(3·4ⁿ). El orden4 falla la tolerancia1/1000 porque en1/4 su error es1/768; orden5 la satisface con1/3072, que se alcanza allí. El panel izquierdo representa ocho grados finitos y no afirma una expansión infinita.](../../assets/books/anm/C21/C21-F08.svg){#fig-anm-c21-f08 fig-alt="Para1/(1−h) en |h|≤1/4, el resto finito da cota1/(3·4ⁿ). El orden4 falla la tolerancia1/1000 porque en1/4 su error es1/768; orden5 la satisface con1/3072, que se alcanza allí. El panel izquierdo representa ocho grados finitos y no afirma una expansión infinita."}

Cambiar el centro también cambia todos los datos. Para una función polinómica conocida se puede reexpandir exactamente; para una función general no se trasladan los coeficientes centrales sin nueva información o un control del error de traslado. Aquí cada expansión conserva su centro declarado.

Finalmente, un paquete finito de derivadas y de valores muestreados no impone una función completa ni un error universal fuera de la región certificada. Si $h_1,\ldots,h_m$ son muestras no nulas y $P$ un modelo central de orden$n$, los polinomios

$$P(h)+A\,h^{n+1}\prod_{j=1}^m(h-h_j)^2$$

conservan los datos centrales hasta orden$n$ y los valores en todas las muestras. En otra entrada no nula distinta de ellas, el factor multiplicador es no cero y variar $A$ permite modificar el valor arbitrariamente. El producto vacío, si no hay muestras, vale1. Esta construcción finita muestra el límite de la información disponible.

El radio que se reduce para un orden fijo y el grado que aumenta en una región fija son controles distintos. Este capítulo demuestra polinomios finitos, residuos y certificados; no declara que una expansión infinita represente a una función. La teoría de sumas infinitas necesitará sus propias condiciones y su propia justificación del resto.

### Microcontroles

#### Microcontrol 57

[]{#MA-MIC-ANM-01-021-057}

¿Qué errores aparecen al multiplicar$P+u$ por$Q+v$?

[]{#MA-MSOL-ANM-01-021-057}

<details class="anm-solution">
<summary>Ver solución del microcontrol 57</summary>

**Respuesta.**

$Pv+Qu+uv$, además de eliminar términos del producto polinómico que superen el orden fijado.

**Fundamento en la sección 21.8.**

Los modelos locales también pueden combinarse. Para un $n\ge1$ fijo y centro0, supongamos $f(h)=P(h)+u(h)$ y $g(h)=Q(h)+v(h)$, con polinomios de grado a lo sumo$n$ y $u,v=o(|h|^n)$. La suma tiene modelo $P+Q$ porque la triangular suma los dos errores normalizados.

Para el producto,

$$fg=PQ+Pv+Qu+uv.$$

Los polinomios son acotados en un radio por continuidad en cero. Dividir $Pv$ y $Qu$ por $|h|^n$ deja un factor acotado por otro que tiende a cero. Además $v(h)\to0$, y $|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Por tanto el error del producto respecto de $PQ$ es $o(|h|^n)$. Si $PQ$ tiene términos de grado mayor que$n$, los eliminamos: su suma finita es $h^{n+1}$ por otro polinomio, y al normalizar por $|h|^n$ tiende a cero. La parte truncada es un modelo del mismo orden, sin derivar el resto.

</details>

#### Microcontrol 58

[]{#MA-MIC-ANM-01-021-058}

¿Por qué un polinomio de términos de grado mayor que$n$ es$o(|h|^n)$?

[]{#MA-MSOL-ANM-01-021-058}

<details class="anm-solution">
<summary>Ver solución del microcontrol 58</summary>

**Respuesta.**

Se factoriza como$h^{n+1}$ por un polinomio acotado cerca de cero; tras normalizar queda un factor$|h|\to0$.

**Fundamento en la sección 21.8.**

Para el producto,

$$fg=PQ+Pv+Qu+uv.$$

Los polinomios son acotados en un radio por continuidad en cero. Dividir $Pv$ y $Qu$ por $|h|^n$ deja un factor acotado por otro que tiende a cero. Además $v(h)\to0$, y $|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Por tanto el error del producto respecto de $PQ$ es $o(|h|^n)$. Si $PQ$ tiene términos de grado mayor que$n$, los eliminamos: su suma finita es $h^{n+1}$ por otro polinomio, y al normalizar por $|h|^n$ tiende a cero. La parte truncada es un modelo del mismo orden, sin derivar el resto.

</details>

#### Microcontrol 59

[]{#MA-MIC-ANM-01-021-059}

¿Qué margen tiene$1-h-h^2$ en$|h|\le1/4$?

[]{#MA-MSOL-ANM-01-021-059}

<details class="anm-solution">
<summary>Ver solución del microcontrol 59</summary>

**Respuesta.**

Al menos$11/16>0$.

**Fundamento en la sección 21.8.**

La sustitución exige conservar dominio y escala. Por ejemplo

$$F(h)=\frac1{1-h-h^2}.$$

En $|h|\le1/4$, el denominador es al menos $1-1/4-1/16=11/16>0$. Un cálculo exacto da

$$(1+h+2h^2)(1-h-h^2)=1-3h^3-2h^4,$$

y así

$$F(h)=1+h+2h^2+\frac{3h^3+2h^4}{1-h-h^2}.$$

El resto queda acotado por $(56/11)|h|^3$ en ese segmento. Además $F(0)=1$, $F'(0)=1$ y $F''(0)=4$, por cociente y cadena, de modo que el polinomio mostrado es realmente su Taylor de orden2. Sustituir una expresión en un modelo sin comprobar denominadores podría haber perdido precisamente esta garantía.

</details>

#### Microcontrol 60

[]{#MA-MIC-ANM-01-021-060}

¿Qué Taylor de orden2 tiene$1/(1-h-h^2)$ en cero?

[]{#MA-MSOL-ANM-01-021-060}

<details class="anm-solution">
<summary>Ver solución del microcontrol 60</summary>

**Respuesta.**

$1+h+2h^2$; el resto exacto es$(3h^3+2h^4)/(1-h-h^2)$.

**Fundamento en la sección 21.8.**

La sustitución exige conservar dominio y escala. Por ejemplo

$$F(h)=\frac1{1-h-h^2}.$$

En $|h|\le1/4$, el denominador es al menos $1-1/4-1/16=11/16>0$. Un cálculo exacto da

$$(1+h+2h^2)(1-h-h^2)=1-3h^3-2h^4,$$

y así

$$F(h)=1+h+2h^2+\frac{3h^3+2h^4}{1-h-h^2}.$$

El resto queda acotado por $(56/11)|h|^3$ en ese segmento. Además $F(0)=1$, $F'(0)=1$ y $F''(0)=4$, por cociente y cadena, de modo que el polinomio mostrado es realmente su Taylor de orden2. Sustituir una expresión en un modelo sin comprobar denominadores podría haber perdido precisamente esta garantía.

</details>

#### Microcontrol 61

[]{#MA-MIC-ANM-01-021-061}

¿Qué orden certifica error menor que$1/1000$ para$1/(1-h)$ en$|h|\le1/4$?

[]{#MA-MSOL-ANM-01-021-061}

<details class="anm-solution">
<summary>Ver solución del microcontrol 61</summary>

**Respuesta.**

Orden5, con cota$1/3072$; orden4 tiene error$1/768$ en$h=1/4$ y falla.

**Fundamento en la sección 21.8.**

Para elegir un grado no basta pensar «más términos, menos error». Se fija primero una región y una tolerancia, y se prueba una cota en función del grado. Para $1/(1-h)$ en $|h|\le1/4$,21.7 da

$$|R_n(h)|\le\frac{(1/4)^{n+1}}{3/4}=\frac1{3\cdot4^n}.$$

El orden4 produce1/768, mayor que1/1000; el orden5 produce1/3072, menor. Esta cota uniforme certifica el objetivo1/1000 con orden5. Es además el menor orden que funciona con esta cota: los números decrecen al multiplicar por1/4, y en $h=1/4$ la igualdad del resto hace fallar cada orden hasta4. En esa entrada el polinomio de orden5 vale1365/1024 y su error frente a4/3 es exactamente1/3072.

</details>

#### Microcontrol 62

[]{#MA-MIC-ANM-01-021-062}

¿Qué dos procesos no deben confundirse?

[]{#MA-MSOL-ANM-01-021-062}

<details class="anm-solution">
<summary>Ver solución del microcontrol 62</summary>

**Respuesta.**

Reducir el radio con un orden fijo y aumentar el grado sobre una región fija; cada uno necesita su propio control del resto.

**Fundamento en la sección 21.8.**

El radio que se reduce para un orden fijo y el grado que aumenta en una región fija son controles distintos. Este capítulo demuestra polinomios finitos, residuos y certificados; no declara que una expansión infinita represente a una función. La teoría de sumas infinitas necesitará sus propias condiciones y su propia justificación del resto.

</details>

#### Microcontrol 63

[]{#MA-MIC-ANM-01-021-063}

¿Cómo preservar datos centrales y un número finito de muestras mientras se cambia otra salida?

[]{#MA-MSOL-ANM-01-021-063}

<details class="anm-solution">
<summary>Ver solución del microcontrol 63</summary>

**Respuesta.**

Añadiendo$A h^{n+1}\prod_j(h-h_j)^2$; su factor se anula en las muestras y hasta el orden central indicado.

**Fundamento en la sección 21.8.**

Finalmente, un paquete finito de derivadas y de valores muestreados no impone una función completa ni un error universal fuera de la región certificada. Si $h_1,\ldots,h_m$ son muestras no nulas y $P$ un modelo central de orden$n$, los polinomios

$$P(h)+A\,h^{n+1}\prod_{j=1}^m(h-h_j)^2$$

conservan los datos centrales hasta orden$n$ y los valores en todas las muestras. En otra entrada no nula distinta de ellas, el factor multiplicador es no cero y variar $A$ permite modificar el valor arbitrariamente. El producto vacío, si no hay muestras, vale1. Esta construcción finita muestra el límite de la información disponible.

</details>

#### Microcontrol 64

[]{#MA-MIC-ANM-01-021-064}

¿Qué representación infinita se ha probado en este capítulo?

[]{#MA-MSOL-ANM-01-021-064}

<details class="anm-solution">
<summary>Ver solución del microcontrol 64</summary>

**Respuesta.**

Ninguna. Se prueban polinomios finitos, residuos y cotas; una expansión infinita exige justificar por separado su suma y su resto.

**Fundamento en la sección 21.8.**

El radio que se reduce para un orden fijo y el grado que aumenta en una región fija son controles distintos. Este capítulo demuestra polinomios finitos, residuos y certificados; no declara que una expansión infinita represente a una función. La teoría de sumas infinitas necesitará sus propias condiciones y su propia justificación del resto.

</details>

### Ejercicios de la sección 21.8

#### Ejercicio 36. Multiplicar modelos sin derivar errores

[]{#MA-EX-ANM-01-021-036}

Si$f=P+u$ y$g=Q+v$ con$u,v=o(|h|^n)$ y$n\ge1$, demuestra que el producto truncado de$PQ$ a grado$n$ es un modelo del mismo orden.

[]{#MA-SOL-ANM-01-021-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

**Respuesta.**

El producto exacto es$PQ+Pv+Qu+uv$. Los polinomios están acotados cerca de0; por ello los cocientes normalizados de$Pv$ y$Qu$ tienden a0. También$v\to0$ y$|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Eliminar términos de grado mayor que$n$ de$PQ$ añade un error$h^{n+1}B(h)$ con$B$ polinómico acotado; normalizar deja un factor$|h|$ y tiende a0. La triangular reúne esos errores. No se derivaron$u,v$ ni se supuso que sus derivadas fueran pequeñas.

**Fundamento en la sección 21.8.**

Los modelos locales también pueden combinarse. Para un $n\ge1$ fijo y centro0, supongamos $f(h)=P(h)+u(h)$ y $g(h)=Q(h)+v(h)$, con polinomios de grado a lo sumo$n$ y $u,v=o(|h|^n)$. La suma tiene modelo $P+Q$ porque la triangular suma los dos errores normalizados.

Para el producto,

$$fg=PQ+Pv+Qu+uv.$$

Los polinomios son acotados en un radio por continuidad en cero. Dividir $Pv$ y $Qu$ por $|h|^n$ deja un factor acotado por otro que tiende a cero. Además $v(h)\to0$, y $|uv|/|h|^n=(|u|/|h|^n)|v|\to0$. Por tanto el error del producto respecto de $PQ$ es $o(|h|^n)$. Si $PQ$ tiene términos de grado mayor que$n$, los eliminamos: su suma finita es $h^{n+1}$ por otro polinomio, y al normalizar por $|h|^n$ tiende a cero. La parte truncada es un modelo del mismo orden, sin derivar el resto.

</details>

#### Ejercicio 37. Sustitución con denominador protegido

[]{#MA-EX-ANM-01-021-037}

Construye el Taylor de orden2 de$F(h)=1/(1-h-h^2)$ y una cota cúbica válida en$|h|\le1/4$.

[]{#MA-SOL-ANM-01-021-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

**Respuesta.**

Pongamos$d=1-h-h^2$, que es al menos11/16 en la región. Por cociente,$F\prime=(1+2h)/d^2$, de valor1 en0; derivar da$F\prime\prime=2/d^2+2(1+2h)^2/d^3$, de valor4 en0. Así$T_2=1+h+2h^2$. La identidad$(1+h+2h^2)d=1-3h^3-2h^4$ da resto$(3h^3+2h^4)/d$. Su magnitud es a lo sumo$(3+2/4)|h|^3/(11/16)=(56/11)|h|^3$. El margen protege tanto la función como su certificado.

**Fundamento en la sección 21.8.**

En $|h|\le1/4$, el denominador es al menos $1-1/4-1/16=11/16>0$. Un cálculo exacto da

$$(1+h+2h^2)(1-h-h^2)=1-3h^3-2h^4,$$

y así

$$F(h)=1+h+2h^2+\frac{3h^3+2h^4}{1-h-h^2}.$$

El resto queda acotado por $(56/11)|h|^3$ en ese segmento. Además $F(0)=1$, $F'(0)=1$ y $F''(0)=4$, por cociente y cadena, de modo que el polinomio mostrado es realmente su Taylor de orden2. Sustituir una expresión en un modelo sin comprobar denominadores podría haber perdido precisamente esta garantía.

Para elegir un grado no basta pensar «más términos, menos error». Se fija primero una región y una tolerancia, y se prueba una cota en función del grado. Para $1/(1-h)$ en $|h|\le1/4$,21.7 da

</details>

#### Ejercicio 38. Elegir el menor grado certificado

[]{#MA-EX-ANM-01-021-038}

Para$1/(1-h)$ en$|h|\le1/4$, encuentra el menor orden que garantiza error menor que$1/1000$ usando la fórmula geométrica. Comprueba el valor en$h=1/4$.

[]{#MA-SOL-ANM-01-021-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

**Respuesta.**

La cota exacta uniforme es$1/(3\cdot4^n)$ y se alcanza en$h=1/4$. Para$n=4$ vale1/768>1/1000; para$n=5$ vale1/3072<1/1000. Como cada aumento divide por4, ningún orden menor que4 puede servir, y4 tampoco: el mínimo es5. El polinomio en1/4 es la suma de seis términos$1+1/4+1/16+1/64+1/256+1/1024=1365/1024$. La función vale4/3; la diferencia es$(4096-4095)/3072=1/3072$.

**Fundamento en la sección 21.8.**

Para elegir un grado no basta pensar «más términos, menos error». Se fija primero una región y una tolerancia, y se prueba una cota en función del grado. Para $1/(1-h)$ en $|h|\le1/4$,21.7 da

$$|R_n(h)|\le\frac{(1/4)^{n+1}}{3/4}=\frac1{3\cdot4^n}.$$

El orden4 produce1/768, mayor que1/1000; el orden5 produce1/3072, menor. Esta cota uniforme certifica el objetivo1/1000 con orden5. Es además el menor orden que funciona con esta cota: los números decrecen al multiplicar por1/4, y en $h=1/4$ la igualdad del resto hace fallar cada orden hasta4. En esa entrada el polinomio de orden5 vale1365/1024 y su error frente a4/3 es exactamente1/3072.

</details>

#### Ejercicio 39. Trasladar un centro conocido

[]{#MA-EX-ANM-01-021-039}

Reexpande$t^3$ en centro2 y compara con centro1. Explica por qué este traslado exacto no autoriza trasladar sin datos los coeficientes de una función general.

[]{#MA-SOL-ANM-01-021-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

**Respuesta.**

En centro2, con$u=t-2$, la identidad$(2+u)^3=8+12u+6u^2+u^3$ da los datos y todos los coeficientes. En centro1, con$h=t-1$, eran$1+3h+3h^2+h^3$. Se relacionan sustituyendo$h=1+u$, porque conocemos la función polinómica completa y el resto de orden3 es0. Para una función general, el modelo central finito conserva sólo datos en su centro y lleva un resto fuera de él. Trasladarlo sin controlar ese resto puede cambiar incluso el valor y las derivadas en el nuevo centro.

**Fundamento en la sección 21.8.**

Cambiar el centro también cambia todos los datos. Para una función polinómica conocida se puede reexpandir exactamente; para una función general no se trasladan los coeficientes centrales sin nueva información o un control del error de traslado. Aquí cada expansión conserva su centro declarado.

Finalmente, un paquete finito de derivadas y de valores muestreados no impone una función completa ni un error universal fuera de la región certificada. Si $h_1,\ldots,h_m$ son muestras no nulas y $P$ un modelo central de orden$n$, los polinomios

</details>

#### Ejercicio 40. Muestras y datos que no determinan otra salida

[]{#MA-EX-ANM-01-021-040}

Prueba que$P(h)+A h^{n+1}\prod_{j=1}^m(h-h_j)^2$ conserva datos centrales hasta orden$n$ y valores en muestras no nulas$h_j$. Muestra que en otra entrada$h_*\ne0$ distinta de ellas puede imponerse cualquier salida.

[]{#MA-SOL-ANM-01-021-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

El producto es polinómico. Multiplicarlo por$h^{n+1}$ garantiza un factor de grado al menos$n+1$ en0, de modo que todas las derivadas centrales hasta$n$ se anulan. En cada$h_j$ hay un factor cero y se conserva$P(h_j)$. En$h_*$ distinto de0 y de todas las muestras, el factor$B=h_*^{n+1}\prod_j(h_*-h_j)^2$ es no cero. Para imponer salida$b$, elegimos$A=(b-P(h_*))/B$. Es una construcción finita, también con producto vacío1 si$m=0$. Conservar esos datos no certifica por sí solo un error en una región completa ni una representación infinita.

**Retorno visual.** Véase [C21-F08](analisis-para-matematicos-capitulo-21-taylor-modelos-locales-y-error.html#fig-anm-c21-f08), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-21)

[← Capítulo 20](analisis-para-matematicos-capitulo-20-convexidad-y-control-por-tangentes-y-secantes.html) · [Capítulo 22 →](analisis-para-matematicos-capitulo-22-partir-refinar-acumular.html)

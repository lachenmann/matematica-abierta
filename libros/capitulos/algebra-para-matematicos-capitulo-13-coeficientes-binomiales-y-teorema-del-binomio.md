---
{
  "title": "Coeficientes binomiales y teorema del binomio",
  "description": "Capítulo 13 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0188",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C13",
  "editorial-id": "MA-BCH-APM-01-013",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0187"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

C11 mostró cómo una afirmación que depende de un número natural puede propagarse mediante inducción. C12 convirtió las sumas y productos finitos en objetos que podemos reindexar, separar, recombinar y comparar con precisión. En este capítulo esas dos líneas se encuentran en una familia de números que aparece, a primera vista, en contextos diferentes: el triángulo de Pascal, la elección de subconjuntos y la expansión de una potencia como $(x+y)^n$.

La coincidencia no es accidental. Los mismos números aparecen porque las tres situaciones describen una misma estructura finita desde puntos de vista distintos. Aprenderemos a pasar de una lectura a otra y a elegir, para cada identidad, el método que mejor explica por qué es verdadera.

> **Un coeficiente binomial no es sólo una fórmula factorial. Es, al mismo tiempo, una entrada del triángulo de Pascal, un número de elecciones y un coeficiente en una expansión.**

***
## 13.1. De las expansiones pequeñas a un patrón triangular {#apm-c13-s01}

Comencemos sin una fórmula general. Expandamos las primeras potencias de una suma:

$$
(x+y)^0=1,
$$

$$
(x+y)^1=x+y,
$$

$$
(x+y)^2=x^2+2xy+y^2,
$$

$$
(x+y)^3=x^3+3x^2y+3xy^2+y^3,
$$

y

$$
(x+y)^4=x^4+4x^3y+6x^2y^2+4xy^3+y^4.
$$

Si miramos sólo los coeficientes, aparecen las filas

$$
1,
$$

$$
1,\qquad 1,
$$

$$
1,\qquad 2,\qquad 1,
$$

$$
1,\qquad 3,\qquad 3,\qquad 1,
$$

$$
1,\qquad 4,\qquad 6,\qquad 4,\qquad 1.
$$

La escritura con pequeños espacios sólo busca hacer visible la disposición triangular. El patrón importante no es gráfico sino aritmético: cada fila comienza y termina en $1$, es simétrica, y cada número interior puede obtenerse sumando dos números contiguos de la fila anterior.

Por ejemplo, el $6$ de la quinta fila visible aparece porque

$$
3+3=6,
$$

y los dos $4$ aparecen porque

$$
1+3=4
$$

y

$$
3+1=4.
$$

También hay un patrón en los exponentes. En cada término de $(x+y)^4$, la suma de los exponentes de $x$ e $y$ es $4$:

$$
4+0,
\qquad 3+1,
\qquad 2+2,
\qquad 1+3,
\qquad 0+4.
$$

Esto sugiere que en $(x+y)^n$ deberíamos esperar términos de la forma

$$
x^{n-k}y^k,
$$

con $k$ recorriendo los enteros desde $0$ hasta $n$. Lo que todavía falta explicar es el coeficiente que acompaña a cada uno.

La pregunta que guiará buena parte del capítulo es entonces:

> **¿Qué mecanismo produce los números $1,4,6,4,1$ y, en general, los coeficientes de $(x+y)^n$?**

Antes de responder mediante una fórmula cerrada, conviene estudiar el patrón por sí mismo.

***
## 13.2. El triángulo de Pascal {#apm-c13-s02}

Numeremos las filas comenzando en $n=0$. La fila $0$ contiene sólo un $1$; la fila $1$ contiene dos unos; la fila $2$ contiene $1,2,1$, etc. Podemos construir cada nueva fila mediante dos reglas:

1. los extremos son $1$;
2. cada entrada interior es la suma de las dos entradas situadas inmediatamente encima.

Así obtenemos

$$
\begin{array}{ccccccccc}
&&&&1\\
&&&1&&1\\
&&1&&2&&1\\
&1&&3&&3&&1\\
1&&4&&6&&4&&1
\end{array}
$$

La entrada situada en la fila $n$ y en la posición $k$, contando desde $k=0$, se denotará por

$$
\binom{n}{k}.
$$

Con esta notación, la regla de construcción del triángulo se convierte en la **identidad de Pascal**:

$$
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-1}{k},
$$

para posiciones interiores, es decir, cuando $1\le k\le n-1$.

Los extremos satisfacen

$$
\binom{n}{0}=\binom{n}{n}=1.
$$

Por ejemplo,

$$
\binom{5}{2}
=
\binom{4}{1}+\binom{4}{2}
=4+6
=10.
$$

La identidad de Pascal puede leerse, por ahora, como una regla recursiva: para calcular una entrada de una fila nueva necesitamos dos entradas de la fila anterior. Más adelante veremos dos demostraciones diferentes de esta identidad. Una será puramente algebraica; la otra explicará la suma mediante una partición de un conjunto de elecciones.

El triángulo ya muestra dos rasgos que conviene separar conceptualmente:

- **recurrencia:** cada fila se obtiene de la anterior;
- **simetría:** las entradas equidistantes de los extremos coinciden.

La recurrencia explica cómo construir. La simetría exigirá explicar por qué

$$
\binom{n}{k}=\binom{n}{n-k}.
$$

***
## 13.3. Coeficientes binomiales: notación, rango y bordes {#apm-c13-s03}

Para un entero no negativo $n$ y un entero $k$ con

$$
0\le k\le n,
$$

el símbolo

$$
\binom{n}{k}
$$

se lee “$n$ sobre $k$” o “$n$ elige $k$”. Lo llamamos **coeficiente binomial**.

Es importante que los dos índices desempeñan papeles diferentes. El índice superior $n$ fija la fila del triángulo y, más adelante, el tamaño del conjunto del cual elegimos. El índice inferior $k$ fija la posición dentro de la fila y el número de elementos seleccionados.

Por ejemplo,

$$
\binom{6}{0}=1,
\qquad
\binom{6}{1}=6,
\qquad
\binom{6}{2}=15,
\qquad
\binom{6}{3}=20.
$$

La simetría de la fila completa da

$$
1,6,15,20,15,6,1.
$$

Los casos extremos tienen una interpretación natural:

$$
\binom{n}{0}=1
$$

y

$$
\binom{n}{n}=1.
$$

Más adelante leeremos estas igualdades como afirmaciones de conteo: hay exactamente una manera de elegir ningún elemento y exactamente una manera de elegir todos los elementos.

### Convención fuera de rango

En algunas identidades resulta útil extender la notación y declarar

$$
\binom{n}{k}=0
$$

cuando $k<0$ o $k>n$, siempre con $n\ge0$.

Esta convención permite escribir ciertas fórmulas sin separar continuamente los extremos. Por ejemplo, para $n\ge1$ la identidad de Pascal puede expresarse de forma uniforme como

$$
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
$$

incluso en $k=0$ y $k=n$, si interpretamos los coeficientes fuera de rango como $0$.

Para $k=0$:

$$
\binom{n}{0}
=
\binom{n-1}{-1}+\binom{n-1}{0}
=0+1
=1.
$$

Para $k=n$:

$$
\binom{n}{n}
=
\binom{n-1}{n-1}+\binom{n-1}{n}
=1+0
=1.
$$

La convención es una herramienta de uniformización. No elimina la obligación de controlar los rangos: cuando una prueba depende de los extremos, éstos deben seguir siendo visibles.

### Nota pedagógica — Un cero convencional no crea factoriales negativos

La convención fuera de rango extiende el **valor del coeficiente**, no la fórmula factorial. Para $m\ge0$, se puede escribir $\binom{m}{-1}=0$, pero no sustituir $-1$ en $m!/[k!(m-k)!]$: aquí $(-1)!$ no está definido. Tampoco se ha definido un coeficiente con índice superior negativo. Por eso Pascal en su forma uniforme exige $n\ge1$, aunque el índice inferior pueda ser cualquier entero.

Elige primero qué escritura necesitas: una fórmula con términos nulos convencionales o una suma que enumere sólo elecciones posibles. Ambas pueden dar el mismo resultado, pero cada término debe tener una interpretación controlada.

**Control resuelto.** En $\sum_{k=0}^{5}\binom{2}{k}\binom{3}{5-k}$, el primer factor requiere $0\le k\le2$ y el segundo $2\le k\le5$. Su intersección es el único valor $k=2$. Por tanto, la suma vale $\binom22\binom33=1$: elegir cinco elementos de dos grupos disjuntos de tamaños dos y tres obliga a elegirlos todos. Los demás términos valen cero por convención, sin evaluar ningún factorial negativo. En cambio, intentar Pascal con $n=0$ introduciría índices superiores $-1$; ese caso no queda autorizado por esta convención.

**Antes de continuar.** Si una expresión contiene factoriales, comprueba sus argumentos antes de cancelarlos. Si contiene coeficientes fuera de rango, declara qué convención les da significado.

***
## 13.4. Factorial y fórmula cerrada {#apm-c13-s04}

Para $n\ge1$ definimos

$$
n!=1\cdot2\cdot3\cdots n.
$$

También adoptamos

$$
0!=1.
$$

Esta última igualdad no es un parche. Es la convención que hace compatibles las fórmulas generales con los casos de borde. Por ejemplo, la expresión factorial del coeficiente binomial es

$$
\boxed{
\binom{n}{k}
=
\frac{n!}{k!(n-k)!}
}
$$

para $0\le k\le n$.

Cuando $k=0$,

$$
\binom{n}{0}
=
\frac{n!}{0!n!}
=1,
$$

y cuando $k=n$,

$$
\binom{n}{n}
=
\frac{n!}{n!0!}
=1.
$$

La igualdad con las entradas definidas por Pascal quedará justificada en [§13.7](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s07): el conteo de subconjuntos y la expresión factorial satisfacen los mismos bordes y la misma recurrencia. No estamos introduciendo una segunda familia de números sin relacionarla con la primera.

La fórmula debe simplificarse por **cancelación estructurada**, no expandiendo factoriales más de lo necesario. Por ejemplo,

$$
\binom{10}{3}
=
\frac{10!}{3!7!}
=
\frac{10\cdot9\cdot8}{3\cdot2\cdot1}
=120.
$$

Del mismo modo, para $n\ge2$,

$$
\binom{n}{2}
=
\frac{n!}{2!(n-2)!}
=
\frac{n(n-1)}{2}.
$$

Y, para $n\ge1$,

$$
\binom{n}{1}=n.
$$

La fórmula factorial es muy eficaz para calcular y transformar expresiones, pero todavía no explica por qué el resultado cuenta algo ni por qué estos números aparecen en $(x+y)^n$. Esa explicación vendrá de la interpretación combinatoria.

***
## 13.5. Interpretación combinatoria: elegir $k$ objetos de $n$ {#apm-c13-s05}

Sea $S$ un conjunto con $n$ elementos. Queremos contar cuántos subconjuntos de $S$ tienen exactamente $k$ elementos.

La respuesta es

$$
\binom{n}{k}.
$$

Esta lectura convierte la notación en una afirmación concreta:

> **$\binom{n}{k}$ es el número de maneras de elegir $k$ elementos distintos de un conjunto de $n$ elementos, sin importar el orden.**

Veamos por qué aparece la fórmula factorial.

Primero contemos elecciones **ordenadas** de $k$ elementos distintos. Para la primera posición hay $n$ opciones; para la segunda quedan $n-1$; para la tercera, $n-2$; y así sucesivamente. El número total es

$$
n(n-1)(n-2)\cdots(n-k+1)
=
\frac{n!}{(n-k)!}.
$$

Pero una misma selección no ordenada de $k$ elementos ha sido contada una vez por cada orden posible de esos $k$ elementos. Hay

$$
k!
$$

ordenaciones de cada selección. Por tanto, al olvidar el orden debemos dividir por $k!$:

$$
\binom{n}{k}
=
\frac{1}{k!}\frac{n!}{(n-k)!}
=
\frac{n!}{k!(n-k)!}.
$$

La fórmula factorial ya no aparece como una manipulación aislada: refleja dos operaciones de conteo.

### Primer ejemplo

De un conjunto de $5$ elementos, los subconjuntos de tamaño $2$ son

$$
\binom{5}{2}=10.
$$

Si los cinco elementos son $a,b,c,d,e$, cada par no ordenado, como $\{a,c\}$, corresponde a dos selecciones ordenadas: $(a,c)$ y $(c,a)$. Por eso el conteo ordenado $5\cdot4=20$ debe dividirse por $2!=2$.

### El principio de doble conteo

Una técnica que usaremos varias veces consiste en identificar un conjunto finito de objetos y contarlo de dos maneras distintas. Si ambos procedimientos cuentan exactamente los mismos objetos, los resultados deben coincidir.

No basta escribir dos expresiones y declarar que “cuentan lo mismo”. Una prueba por doble conteo debe especificar:

1. cuál es el conjunto de objetos;
2. qué clasifica o decide el primer conteo;
3. qué clasifica o decide el segundo;
4. por qué cada objeto aparece exactamente una vez en cada procedimiento.

Esta disciplina será esencial en Pascal, Vandermonde y otras identidades.

***
## 13.6. Simetría por complemento {#apm-c13-s06}

El triángulo de Pascal sugiere

$$
\boxed{
\binom{n}{k}=\binom{n}{n-k}
}.
$$

Hay al menos dos razones independientes para que esto sea cierto.

### Prueba factorial

Usando la fórmula cerrada,

$$
\binom{n}{n-k}
=
\frac{n!}{(n-k)!(n-(n-k))!}
=
\frac{n!}{(n-k)!k!}
=
\binom{n}{k}.
$$

La igualdad resulta de que el denominador contiene los mismos dos factores, sólo en orden invertido.

### Prueba por complemento

Sea $S$ un conjunto con $n$ elementos. A cada subconjunto $A\subseteq S$ de tamaño $k$ le asociamos su complemento

$$
S\setminus A.
$$

Como $A$ contiene $k$ elementos, su complemento contiene $n-k$.

Además, la operación es reversible: si conocemos $S\setminus A$, recuperamos $A$ tomando nuevamente el complemento. Por tanto, existe una biyección entre

- los subconjuntos de tamaño $k$;
- los subconjuntos de tamaño $n-k$.

En consecuencia,

$$
\binom{n}{k}=\binom{n}{n-k}.
$$

Las dos pruebas establecen la misma identidad, pero revelan cosas distintas. La prueba factorial es una verificación algebraica inmediata. La prueba por complemento explica la simetría como una correspondencia entre elecciones.

Ésta será una idea recurrente: **cuando una identidad tiene una interpretación combinatoria natural, la fórmula factorial puede verificarla, pero no siempre explica su estructura con la misma claridad.**

***
## 13.7. Identidad de Pascal: dos pruebas {#apm-c13-s07}

Para $1\le k\le n-1$ queremos demostrar

$$
\boxed{
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
}.
$$

### Prueba algebraica

Partimos del lado derecho:

$$
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$

Usando factoriales,

$$
\frac{(n-1)!}{(k-1)!(n-k)!}
+
\frac{(n-1)!}{k!(n-k-1)!}.
$$

Llevamos ambas fracciones al denominador común $k!(n-k)!$:

$$
\frac{k(n-1)!}{k!(n-k)!}
+
\frac{(n-k)(n-1)!}{k!(n-k)!}.
$$

Sumando numeradores,

$$
\frac{(k+n-k)(n-1)!}{k!(n-k)!}
=
\frac{n(n-1)!}{k!(n-k)!}
=
\frac{n!}{k!(n-k)!}.
$$

Por tanto,

$$
\binom{n-1}{k-1}
+
\binom{n-1}{k}
=
\binom{n}{k}.
$$

### Prueba combinatoria

Sea $S$ un conjunto de $n$ elementos y fijemos un elemento distinguido $a\in S$. Queremos contar los subconjuntos de $S$ que tienen tamaño $k$.

Hay dos clases disjuntas.

**Clase 1: subconjuntos que contienen a $a$.**

Si $a$ ya está incluido, debemos elegir los otros $k-1$ elementos entre los $n-1$ elementos de $S\setminus\{a\}$. Hay

$$
\binom{n-1}{k-1}
$$

posibilidades.

**Clase 2: subconjuntos que no contienen a $a$.**

Entonces los $k$ elementos deben elegirse enteramente entre los otros $n-1$ elementos. Hay

$$
\binom{n-1}{k}
$$

posibilidades.

Las dos clases son disjuntas y cubren todos los subconjuntos de tamaño $k$. Por la regla de adición,

$$
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$

Ahora la regla del triángulo de Pascal deja de ser una receta misteriosa: expresa una partición de las elecciones según incluyan o no un elemento distinguido.

Esta prueba cierra también la identificación de nuestras representaciones. Hay una única elección de tamaño cero y una única elección de todos los elementos; el conteo satisface Pascal por la partición anterior. La fila cero queda fijada en $1$. Si una fila está determinada, los bordes y las sumas de parejas vecinas determinan de manera única la siguiente. Por inducción, el conteo coincide con todas las entradas del triángulo construido en [§13.2](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s02). El conteo ordenado de [§13.5](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s05) demuestra su fórmula factorial. Así, triángulo, conteo y fórmula describen efectivamente la misma familia.

***
## 13.8. El teorema del binomio {#apm-c13-s08}

Las expansiones iniciales de este capítulo sugieren una fórmula general. Para todo entero $n\ge0$,

$$
\boxed{
(x+y)^n
=
\sum_{k=0}^{n}
\binom{n}{k}x^{n-k}y^k
}.
$$

Éste es el **teorema del binomio**.

El término correspondiente a un valor fijo de $k$ es

$$
\binom{n}{k}x^{n-k}y^k.
$$

Hay cuatro controles que conviene realizar siempre:

1. el índice satisface $0\le k\le n$;
2. el coeficiente es $\binom{n}{k}$;
3. el exponente de $y$ es $k$;
4. el exponente de $x$ es $n-k$, de modo que la suma de exponentes es $n$.

### Los extremos

Para $k=0$ obtenemos

$$
\binom{n}{0}x^ny^0=x^n.
$$

Para $k=n$ obtenemos

$$
\binom{n}{n}x^0y^n=y^n.
$$

Por eso la expansión comienza con $x^n$ y termina con $y^n$.

### El caso $n=0$

Para incluir uniformemente $n=0$, interpretamos la potencia cero en esta identidad algebraica como el **producto vacío**, cuyo valor es $1$. Así, el caso $n=0$ se entiende dentro de la identidad polinómica sin imponer aquí una convención numérica general para la expresión $0^0$. Cuando $n=0$, la suma contiene un único término:

$$
\sum_{k=0}^{0}\binom{0}{k}x^{0-k}y^k
=
\binom{0}{0}
=1.
$$

Esto coincide con

$$
(x+y)^0=1
$$

de modo que el caso base queda incorporado a la misma escritura que los demás exponentes.

### Ejemplo de lectura

En $(x+y)^7$, el término que contiene $y^3$ corresponde a $k=3$:

$$
\binom{7}{3}x^{7-3}y^3
=
35x^4y^3.
$$

No hace falta expandir toda la potencia para encontrarlo. El teorema da acceso directo a cualquier término.

También podemos sustituir expresiones más complejas. Por ejemplo,

$$
(x-2y)^4
=
\sum_{k=0}^{4}\binom{4}{k}x^{4-k}(-2y)^k.
$$

Al simplificar,

$$
(x-2y)^4
=
x^4-8x^3y+24x^2y^2-32xy^3+16y^4.
$$

Los signos alternan porque el segundo sumando es negativo y la potencia $(-2y)^k$ cambia de signo según la paridad de $k$.

***
## 13.9. Prueba inductiva del teorema del binomio {#apm-c13-s09}

Esta demostración reúne tres herramientas ya estudiadas: inducción, distributividad y reindexación de sumas.

Queremos probar, para todo $n\ge0$,

$$
P(n):
\qquad
(x+y)^n
=
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$

### Caso base

Para $n=0$,

$$
(x+y)^0=1
$$

y

$$
\sum_{k=0}^{0}\binom{0}{k}x^{0-k}y^k
=
\binom{0}{0}=1.
$$

Así, $P(0)$ es verdadera.

### Hipótesis inductiva

Supongamos que para cierto $n\ge0$ se cumple

$$
(x+y)^n
=
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$

### Paso inductivo

Multiplicamos por $(x+y)$:

$$
(x+y)^{n+1}
=
(x+y)\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$

Distribuyendo,

$$
(x+y)^{n+1}
=
\sum_{k=0}^{n}\binom{n}{k}x^{n+1-k}y^k
+
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k+1}.
$$

Las dos sumas todavía no están alineadas: en la primera la potencia de $y$ es $k$, mientras que en la segunda es $k+1$. Reindexemos la segunda suma con

$$
j=k+1.
$$

Entonces

$$
k=j-1.
$$

Los límites cambian:

$$
k=0\Rightarrow j=1,
\qquad
k=n\Rightarrow j=n+1.
$$

El sumando se transforma en

$$
\binom{n}{j-1}x^{n-(j-1)}y^j
=
\binom{n}{j-1}x^{n+1-j}y^j.
$$

Por tanto,

$$
(x+y)^{n+1}
=
\sum_{k=0}^{n}\binom{n}{k}x^{n+1-k}y^k
+
\sum_{j=1}^{n+1}\binom{n}{j-1}x^{n+1-j}y^j.
$$

Ahora renombramos el índice $j$ como $k$ en la segunda suma. Este paso sí es sólo un cambio de nombre:

$$
(x+y)^{n+1}
=
\sum_{k=0}^{n}\binom{n}{k}x^{n+1-k}y^k
+
\sum_{k=1}^{n+1}\binom{n}{k-1}x^{n+1-k}y^k.
$$

Para combinar correctamente, debemos separar los extremos. El término $k=0$ sólo aparece en la primera suma:

$$
\binom{n}{0}x^{n+1}=x^{n+1}.
$$

El término $k=n+1$ sólo aparece en la segunda:

$$
\binom{n}{n}y^{n+1}=y^{n+1}.
$$

En el rango interior $1\le k\le n$, ambas sumas contienen el mismo monomio $x^{n+1-k}y^k$, y sus coeficientes se suman:

$$
\binom{n}{k}+\binom{n}{k-1}.
$$

Por Pascal,

$$
\binom{n}{k}+\binom{n}{k-1}
=
\binom{n+1}{k}.
$$

Así,

$$
\begin{aligned}
(x+y)^{n+1}
&=x^{n+1}
+
\sum_{k=1}^{n}\binom{n+1}{k}x^{n+1-k}y^k
+
y^{n+1}\\
&=
\sum_{k=0}^{n+1}\binom{n+1}{k}x^{n+1-k}y^k.
\end{aligned}
$$

Hemos demostrado $P(n+1)$. Por inducción, el teorema vale para todo $n\ge0$.

### Qué revela esta prueba

La demostración no sólo verifica la fórmula. Muestra por qué la recurrencia de Pascal es exactamente la que necesitamos al multiplicar una expansión por $(x+y)$: cada término interior de la nueva potencia recibe una contribución desde dos términos vecinos de la fila anterior.

También muestra por qué reindexar es una operación matemática y no tipográfica: si no se transforman simultáneamente índice, límites y sumando, los dos bloques no pueden alinearse correctamente.

### Nota pedagógica — Reindexar conserva contribuciones y controla extremos

La reindexación de C12 se aplica aquí a una lista de monomios. Para revisar el desplazamiento $j=k+1$, sigue una contribución completa:

$$
(k,\ \binom nkx^{n-k}y^{k+1})
\longmapsto
(j,\ \binom n{j-1}x^{n+1-j}y^j).
$$

El coeficiente y ambos exponentes cambian juntos; el grado total sigue siendo $n+1$. El intervalo $0\le k\le n$ pasa a $1\le j\le n+1$. Sólo después de esa sustitución se puede cambiar la letra $j$ por $k$ sin modificar nada más.

**Control resuelto.** Para $n=2$, multiplicar $(x+y)^2$ por $x$ da $x^3+2x^2y+xy^2$, y multiplicarlo por $y$ da $x^2y+2xy^2+y^3$. En la segunda lista, el término antiguo $k=0$ ahora tiene índice $j=1$; el antiguo $k=2$ tiene $j=3$. Las contribuciones interiores son $(2+1)x^2y$ y $(1+2)xy^2$; los extremos son $x^3$ e $y^3$. Así se recupera $x^3+3x^2y+3xy^2+y^3$.

También podríamos usar la convención de [§13.3](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s03) para escribir una sola suma desde $0$ hasta $n+1$ con coeficiente $\binom nk+\binom n{k-1}$. Aquí todos los exponentes son no negativos y los ceros completan los coeficientes faltantes. No conviene extender primero los productos originales: escribir un coeficiente cero junto a una potencia negativa puede introducir una expresión indefinida cuando la base es cero. Se completa la lista de **coeficientes** después de alinear los monomios.

**Autocontrol.** Conserva el grado, transforma los dos límites y localiza la contribución que produce cada extremo. Si alguno de esos tres controles falla, el desplazamiento aún no está justificado.

***
## 13.10. Prueba por elección de factores {#apm-c13-s10}

Existe una explicación más directa de por qué aparecen los coeficientes binomiales.

Escribamos

$$
(x+y)^n
=
\underbrace{(x+y)(x+y)\cdots(x+y)}_{n\text{ factores}}.
$$

Al expandir por distributividad, cada término final se obtiene escogiendo de cada factor una de dos posibilidades: $x$ o $y$.

Para producir

$$
x^{n-k}y^k,
$$

exactamente $k$ de los $n$ factores deben aportar un $y$, y los $n-k$ restantes deben aportar un $x$.

Por tanto, la pregunta “¿cuántas veces aparece $x^{n-k}y^k$?” equivale a

> “¿De cuántas maneras podemos elegir cuáles $k$ de los $n$ factores aportarán $y$?”

La respuesta es

$$
\binom{n}{k}.
$$

Así, el coeficiente de $x^{n-k}y^k$ es precisamente $\binom{n}{k}$ y obtenemos

$$
(x+y)^n
=
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k.
$$

Esta prueba explica conceptualmente la conexión que motivó el capítulo. El mismo número aparece como coeficiente y como número de subconjuntos porque **producir un término de la expansión consiste en elegir un subconjunto de factores**.

### Dos pruebas, dos estructuras

La prueba inductiva organiza el teorema fila por fila y muestra cómo Pascal permite pasar de $n$ a $n+1$. La prueba por elección de factores mira una potencia fija y explica el coeficiente directamente.

La primera enfatiza **recurrencia**. La segunda enfatiza **selección**.

Ninguna invalida a la otra. Compararlas nos enseña a distinguir entre demostrar que una fórmula se propaga correctamente y explicar por qué sus coeficientes tienen la forma que tienen.

***
## 13.11. Consecuencias por sustitución {#apm-c13-s11}

Una identidad importante puede contener muchas otras como casos particulares. El teorema del binomio es un ejemplo especialmente fértil.

### Suma de una fila

Tomemos $x=1$ e $y=1$:

$$
(1+1)^n
=
\sum_{k=0}^{n}\binom{n}{k}1^{n-k}1^k.
$$

Por tanto,

$$
\boxed{
\sum_{k=0}^{n}\binom{n}{k}=2^n
}.
$$

La misma identidad admite una lectura combinatoria. Un conjunto con $n$ elementos tiene $2^n$ subconjuntos porque para cada elemento hay dos decisiones: incluirlo o no. Si, en cambio, clasificamos los subconjuntos por tamaño, hay

$$
\binom{n}{0}
+
\binom{n}{1}
+
\cdots
+
\binom{n}{n}
$$

subconjuntos. Ambos conteos deben coincidir.

### Suma alternada

Tomemos $x=1$ e $y=-1$. Para $n\ge1$,

$$
(1-1)^n=0.
$$

El teorema da

$$
0
=
\sum_{k=0}^{n}\binom{n}{k}(-1)^k.
$$

Así,

$$
\boxed{
\sum_{k=0}^{n}(-1)^k\binom{n}{k}=0
}
\qquad(n\ge1).
$$

Separando términos pares e impares,

$$
\sum_{\substack{0\le k\le n\\ k\text{ par}}}\binom{n}{k}
=
\sum_{\substack{0\le k\le n\\ k\text{ impar}}}\binom{n}{k}.
$$

Como la suma total es $2^n$, para $n\ge1$ cada una de estas dos sumas vale

$$
2^{n-1}.
$$

Esta deducción muestra una estrategia general:

> **Antes de atacar una suma binomial término a término, conviene preguntar si es la expansión de $(x+y)^n$ evaluada en valores especialmente simples.**

***
## 13.12. Identidades ponderadas sin cálculo {#apm-c13-s12}

Consideremos la identidad

$$
\boxed{
k\binom{n}{k}
=
n\binom{n-1}{k-1}
}
$$

para $1\le k\le n$.

### Prueba algebraica

Usando la fórmula factorial,

$$
k\binom{n}{k}
=
k\frac{n!}{k!(n-k)!}
=
\frac{n!}{(k-1)!(n-k)!}.
$$

Por otra parte,

$$
n\binom{n-1}{k-1}
=
n\frac{(n-1)!}{(k-1)!(n-k)!}
=
\frac{n!}{(k-1)!(n-k)!}.
$$

Luego ambos lados son iguales.

### Prueba por un elemento distinguido

Sea $S$ un conjunto de $n$ elementos. Contemos pares $(A,a)$ tales que

- $A\subseteq S$;
- $|A|=k$;
- $a\in A$ es un elemento distinguido dentro de $A$.

Primer método: elegimos primero $A$. Hay $\binom{n}{k}$ posibilidades y luego $k$ opciones para distinguir un elemento de $A$. Total:

$$
k\binom{n}{k}.
$$

Segundo método: elegimos primero el elemento distinguido $a$. Hay $n$ opciones. Después elegimos los otros $k-1$ elementos de $A$ entre los $n-1$ restantes. Total:

$$
n\binom{n-1}{k-1}.
$$

Como ambos procedimientos cuentan los mismos pares $(A,a)$, obtenemos la identidad.

### Una suma ponderada

Ahora sumemos sobre $k$:

$$
\sum_{k=0}^{n}k\binom{n}{k}.
$$

El término $k=0$ vale $0$, así que podemos comenzar en $k=1$. Usamos la identidad local:

$$
\sum_{k=1}^{n}k\binom{n}{k}
=
n\sum_{k=1}^{n}\binom{n-1}{k-1}.
$$

Reindexamos con $j=k-1$:

$$
n\sum_{j=0}^{n-1}\binom{n-1}{j}.
$$

La suma de una fila del triángulo vale $2^{n-1}$. Por tanto,

$$
\boxed{
\sum_{k=0}^{n}k\binom{n}{k}
=
n\,2^{n-1}
}
$$

para $n\ge1$.

No fue necesario derivar ninguna función. La identidad surge de una transformación combinatoria local seguida de una suma de fila.

También puede interpretarse por doble conteo: el lado izquierdo cuenta pares $(A,a)$ donde $A$ es un subconjunto de $S$ y $a\in A$ está distinguido; el lado derecho elige primero $a$ y luego decide libremente cuáles de los otros $n-1$ elementos acompañan a $a$.

***
## 13.13. Identidad del palo de hockey {#apm-c13-s13}

Para enteros $0\le r\le n$ se cumple

$$
\boxed{
\sum_{j=r}^{n}\binom{j}{r}
=
\binom{n+1}{r+1}
}.
$$

La disposición de estos términos en el triángulo de Pascal forma visualmente una figura parecida a un palo de hockey, de donde proviene el nombre tradicional de la identidad.

### Prueba por Pascal y telescopaje discreto

De la identidad de Pascal,

$$
\binom{j+1}{r+1}
=
\binom{j}{r}+
\binom{j}{r+1}.
$$

Despejamos

$$
\binom{j}{r}
=
\binom{j+1}{r+1}
-
\binom{j}{r+1}.
$$

Sumamos desde $j=r$ hasta $n$:

$$
\sum_{j=r}^{n}\binom{j}{r}
=
\sum_{j=r}^{n}
\left(
\binom{j+1}{r+1}
-
\binom{j}{r+1}
\right).
$$

Al expandir,

$$
\begin{aligned}
&\left(\binom{r+1}{r+1}-\binom{r}{r+1}\right)
+\left(\binom{r+2}{r+1}-\binom{r+1}{r+1}\right)\\
&\qquad+\cdots
+\left(\binom{n+1}{r+1}-\binom{n}{r+1}\right).
\end{aligned}
$$

Los términos interiores se cancelan. Además, por la convención fuera de rango,

$$
\binom{r}{r+1}=0.
$$

Queda

$$
\sum_{j=r}^{n}\binom{j}{r}
=
\binom{n+1}{r+1}.
$$

Esta prueba conecta directamente Pascal con el telescopaje de C12.

### Prueba combinatoria

Contemos los subconjuntos de tamaño $r+1$ del conjunto

$$
\{1,2,\ldots,n+1\}.
$$

Directamente hay

$$
\binom{n+1}{r+1}
$$

tales subconjuntos.

Ahora clasifiquémoslos por su elemento máximo. Si el máximo es $j+1$, entonces los otros $r$ elementos deben elegirse entre

$$
\{1,2,\ldots,j\},
$$

lo que puede hacerse de

$$
\binom{j}{r}
$$

maneras.

El máximo posible va desde $r+1$ hasta $n+1$, es decir, $j$ va desde $r$ hasta $n$. Sumando las clases:

$$
\sum_{j=r}^{n}\binom{j}{r}
=
\binom{n+1}{r+1}.
$$

La prueba algebraica ve una cancelación. La combinatoria ve una clasificación por máximo. Ambas describen la misma identidad desde estructuras diferentes.

***
## 13.14. Identidad de Vandermonde {#apm-c13-s14}

Sean $A$ y $B$ conjuntos disjuntos, sean $r$ y $s$ enteros no negativos y sea $n$ un entero con $0\le n\le r+s$. Supongamos

$$
|A|=r,
\qquad
|B|=s.
$$

Queremos elegir $n$ elementos de la unión $A\cup B$. Como la unión es disjunta,

$$
|A\cup B|=r+s,
$$

de modo que el número total de elecciones es

$$
\binom{r+s}{n}.
$$

Podemos contar las mismas elecciones de otra manera. Supongamos que elegimos exactamente $k$ elementos de $A$. Entonces debemos elegir $n-k$ elementos de $B$. El número de posibilidades para ese valor de $k$ es

$$
\binom{r}{k}\binom{s}{n-k}.
$$

Sumando sobre todos los valores posibles de $k$ obtenemos la **identidad de Vandermonde**:

$$
\boxed{
\sum_k
\binom{r}{k}
\binom{s}{n-k}
=
\binom{r+s}{n}
}.
$$

Si usamos la convención $\binom{m}{t}=0$ fuera de rango, podemos sumar sobre todos los enteros $k$ sin daño. Si preferimos escribir sólo el rango efectivo, las condiciones son

$$
0\le k\le r
$$

y

$$
0\le n-k\le s.
$$

Equivalente a

$$
\max(0,n-s)
\le k\le
\min(n,r).
$$

Así, una forma completamente explícita es

$$
\sum_{k=\max(0,n-s)}^{\min(n,r)}
\binom{r}{k}
\binom{s}{n-k}
=
\binom{r+s}{n}.
$$

### Una consecuencia central

Tomemos $r=s=n$ y elijamos $n$ elementos de una unión disjunta de dos conjuntos de tamaño $n$. Vandermonde da

$$
\sum_{k=0}^{n}
\binom{n}{k}
\binom{n}{n-k}
=
\binom{2n}{n}.
$$

Por simetría,

$$
\binom{n}{n-k}=\binom{n}{k}.
$$

Por tanto,

$$
\boxed{
\sum_{k=0}^{n}\binom{n}{k}^2
=
\binom{2n}{n}
}.
$$

Esta identidad puede parecer sorprendente si se mira sólo como suma de cuadrados. Desde el doble conteo, en cambio, dice algo sencillo: para elegir $n$ elementos de dos grupos disjuntos de tamaño $n$, podemos clasificar la elección según cuántos elementos provienen del primer grupo.

Vandermonde resume una estrategia poderosa: cuando aparece un producto de dos coeficientes binomiales dentro de una suma, conviene preguntar si cada factor corresponde a una elección en una parte distinta de un conjunto mayor.

### Nota pedagógica — Qué debe probar una partición de elecciones

En Vandermonde, el objeto contado es un subconjunto $T$ de tamaño $n$ de $A\cup B$. La clase de índice $k$ contiene exactamente los objetos con $|T\cap A|=k$. Esa definición permite comprobar tres obligaciones: todo objeto pertenece a alguna clase, no pertenece a dos clases distintas y cada elección dentro de una clase se reconstruye de manera única.

La reconstrucción es $(U,V)\mapsto U\cup V$, donde $U\subseteq A$, $V\subseteq B$, $|U|=k$ y $|V|=n-k$. Como $A$ y $B$ son disjuntos, la unión tiene tamaño $n$ y recuperamos $U=T\cap A$, $V=T\cap B$. Éste es el motivo preciso para multiplicar los dos coeficientes y luego sumar las clases. Una frase como «elegimos por separado» necesita esta garantía de reconstrucción.

**Control resuelto.** Si $|A|=2$, $|B|=3$ y $n=4$, los únicos índices posibles son $k=1,2$. La primera clase tiene $\binom21\binom33=2$ objetos; la segunda tiene $\binom22\binom32=3$. La suma es $5=\binom54$. No puede haber una clase $k=0$, porque exigiría cuatro elementos de $B$; tampoco una clase $k=3$, porque $A$ sólo tiene dos elementos.

**Pregunta de diagnóstico.** ¿Qué falla si los grupos comparten un elemento? Las elecciones separadas pueden seleccionar dos veces el mismo elemento, y la unión deja de conservar el tamaño. Hay que cambiar el modelo —por ejemplo, usar copias etiquetadas disjuntas— o dividir la unión original en partes realmente disjuntas. El ejercicio 87 desarrolla esa reparación. En cualquier doble conteo, explica el objeto, la clasificación y la reconstrucción antes de identificar la suma.

***
## 13.15. Del binomio al multinomio {#apm-c13-s15}

El mecanismo del teorema del binomio no depende esencialmente de tener sólo dos opciones por factor. Consideremos

$$
(x+y+z)^n
=
\underbrace{(x+y+z)\cdots(x+y+z)}_{n\text{ factores}}.
$$

Para producir un término

$$
x^a y^b z^c
$$

necesitamos elegir

- $a$ factores que aporten $x$;
- $b$ factores que aporten $y$;
- $c$ factores que aporten $z$;

con

$$
a+b+c=n.
$$

¿Cuántas elecciones producen ese término?

Primero elegimos los $a$ factores que aportan $x$:

$$
\binom{n}{a}.
$$

De los $n-a$ factores restantes elegimos los $b$ que aportarán $y$:

$$
\binom{n-a}{b}.
$$

Los $c=n-a-b$ factores restantes aportan $z$. Multiplicando,

$$
\binom{n}{a}\binom{n-a}{b}
=
\frac{n!}{a!(n-a)!}
\frac{(n-a)!}{b!c!}
=
\frac{n!}{a!b!c!}.
$$

Por tanto, el coeficiente de $x^a y^b z^c$ en $(x+y+z)^n$ es

$$
\boxed{
\frac{n!}{a!b!c!}
}
$$

cuando $a+b+c=n$.

El desarrollo completo puede escribirse como una suma sobre todas las ternas no negativas $(a,b,c)$ cuya suma sea $n$:

$$
(x+y+z)^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}
x^a y^b z^c.
$$

No necesitamos desarrollar aquí una teoría general de multiíndices. Lo importante es reconocer el patrón: el coeficiente cuenta cuántas maneras hay de repartir $n$ posiciones entre varias categorías de tamaños prescritos.

Para un número fijo de opciones, el mismo razonamiento conduce a coeficientes de la forma

$$
\frac{n!}{k_1!k_2!\cdots k_m!},
$$

con

$$
k_1+k_2+\cdots+k_m=n.
$$

El caso binomial corresponde a $m=2$. El trinomial muestra que el teorema del binomio es el primer caso de un principio de selección más amplio.

Como comprobación estructural, si sustituimos $x=y=z=1$, obtenemos

$$
3^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}\frac{n!}{a!b!c!},
$$

que expresa que cada una de las $n$ posiciones puede asignarse independientemente a una de tres categorías.

***
## 13.16. Cierre — protocolo para identidades binomiales {#apm-c13-s16}

A lo largo del capítulo hemos visto que una identidad binomial puede ser accesible desde varias direcciones. Frente a una expresión nueva, conviene evitar el reflejo de expandir factoriales inmediatamente.

Un protocolo eficaz es:

```text
1. IDENTIFICAR EL RANGO DE CADA COEFICIENTE.
2. CONTROLAR LOS CASOS DE BORDE k=0 Y k=n.
3. PREGUNTAR SI LA SIMETRÍA k ↔ n-k SIMPLIFICA LA EXPRESIÓN.
4. PREGUNTAR SI PASCAL COMBINA O DESCOMPONE LOS TÉRMINOS.
5. SI HAY SUMAS DESPLAZADAS, REINDEXAR ÍNDICE, LÍMITES Y SUMANDO.
6. IDENTIFICAR SI LA SUMA PROVIENE DEL TEOREMA DEL BINOMIO POR SUSTITUCIÓN.
7. BUSCAR UNA INTERPRETACIÓN COMO ELECCIONES DE SUBCONJUNTOS.
8. SI APARECE UNA SUMA DE PRODUCTOS, PROBAR DOBLE CONTEO.
9. USAR FACTORIALES CUANDO ACLAREN LA ESTRUCTURA, NO POR REFLEJO.
10. COMPARAR QUÉ EXPLICA CADA PRUEBA, NO SÓLO SI LLEGA AL RESULTADO.
```

### Errores frecuentes

**Intercambiar los índices.** En general,

$$
\binom{n}{k}
$$

no significa lo mismo que

$$
\binom{k}{n}.
$$

**Olvidar $0!=1$.** Esto rompe precisamente los casos extremos que deben encajar mejor con las fórmulas generales.

**Reindexar sólo la letra.** Si $j=k+1$, deben cambiar también límites y sumando. Cambiar el símbolo sin transformar la expresión produce una suma distinta.

**Aplicar Pascal con índices incompatibles.** La pareja correcta tiene el mismo índice superior $n-1$ y posiciones inferiores consecutivas:

$$
\binom{n-1}{k-1}+\binom{n-1}{k}.
$$

**Perder los extremos en una prueba inductiva.** Cuando dos sumas tienen rangos $0\le k\le n$ y $1\le k\le n+1$, sólo el rango interior puede combinarse directamente.

**Usar una prueba combinatoria sin decir qué se cuenta.** El doble conteo requiere un conjunto finito bien definido y dos particiones o procedimientos exhaustivos y sin solapamiento.

**Escribir exponentes incompatibles con el grado.** En el término del binomio

$$
\binom{n}{k}x^{n-k}y^k,
$$

los exponentes siempre suman $n$.

### Qué queda cerrado y qué viene después

C11, C12 y C13 forman ahora un bloque coherente:

- C11 proporcionó inducción, buen orden y recursión;
- C12 proporcionó el lenguaje de sumas, productos y reindexaciones finitas;
- C13 mostró cómo esas técnicas interactúan con conteos, recurrencias e identidades binomiales.

El siguiente capítulo cambia el centro de gravedad. Dejaremos de estudiar identidades finitas principalmente por su forma combinatoria y comenzaremos a examinar la estructura aritmética de los enteros: qué significa que un número divida a otro, cómo se comportan los divisores y qué propiedades se conservan bajo las operaciones.

No necesitábamos divisibilidad para desarrollar este capítulo. Esa separación es deliberada: las propiedades aritméticas de los coeficientes binomiales, sus congruencias y su comportamiento módulo primos pertenecen a etapas posteriores.

Por ahora, el resultado conceptual central es éste:

> **El triángulo de Pascal, las elecciones de subconjuntos y el teorema del binomio son tres representaciones de una misma estructura finita. Saber cambiar de representación es más poderoso que memorizar una lista de identidades.**

***
# Ejercicios

Los ejercicios están organizados de modo que el lector pase de la lectura y el cálculo directo a la demostración, el doble conteo y la elección autónoma del método. Salvo indicación contraria, se supone que los índices binomiales satisfacen los rangos naturales en que las expresiones están definidas.

## A. Leer el triángulo y la notación


**1.** **Nivel A.** Construye las filas $0$ a $7$ del triángulo de Pascal. En cada fila, comprueba que los extremos son $1$ y que cada entrada interior se obtiene sumando las dos entradas situadas encima.


**2.** **Nivel A.** Lee directamente del triángulo de Pascal y calcula:
$$
\binom{7}{0},\qquad
\binom{7}{1},\qquad
\binom{7}{3},\qquad
\binom{7}{6},\qquad
\binom{7}{7}.
$$


**3.** **Nivel A.** Completa la fila
$$
1,\ 8,\ \square,\ 56,\ \square,\ 56,\ \square,\ 8,\ 1
$$
del triángulo de Pascal e identifica el número de fila.


**4.** **Nivel B.** Explica qué significan, respectivamente, el índice superior y el índice inferior en $\binom{n}{k}$. Ilustra tu explicación con $\binom{9}{4}$.


**5.** **Nivel B.** Usando la convención fuera de rango, calcula
$$
\binom{6}{-1},\qquad
\binom{6}{0},\qquad
\binom{6}{6},\qquad
\binom{6}{7}.
$$
Explica por qué la convención es útil pero no reemplaza el control de los rangos.


**6.** **Nivel B.** Un estudiante afirma que $\binom{4}{9}=\binom{9}{4}$ “por simetría”. Localiza el error conceptual y formula correctamente la simetría de los coeficientes binomiales.

## B. Factoriales y fórmula cerrada


**7.** **Nivel A.** Calcula mediante factoriales:
$$
\binom{9}{4},\qquad
\binom{10}{2},\qquad
\binom{12}{3}.
$$
Simplifica cancelando antes de desarrollar factoriales completos.


**8.** **Nivel B.** Deduce a partir de la fórmula factorial expresiones cerradas para
$$
\binom{n}{1},\qquad
\binom{n}{2},\qquad
\binom{n}{3}.
$$


**9.** **Nivel B.** Sustituye $k=0$ y $k=n$ en
$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$
y explica por qué la convención $0!=1$ permite que ambos casos extremos queden incluidos en una sola fórmula.


**10.** **Nivel C.** Para $0\le k<n$, demuestra que
$$
\frac{\binom{n}{k+1}}{\binom{n}{k}}
=
\frac{n-k}{k+1}.
$$
Explica qué información ofrece esta razón para comparar dos coeficientes consecutivos de una misma fila.


**11.** **Nivel B.** Comprueba factorialmente que
$$
\binom{10}{7}=\binom{10}{3},
$$
y después explica por qué la igualdad era previsible antes de calcular.


**12.** **Nivel C.** Determina todos los enteros $n\ge2$ que satisfacen
$$
\binom{n}{2}=45.
$$
Justifica cada transformación.

## C. Interpretación combinatoria y simetría


**13.** **Nivel A.** ¿Cuántos comités de $3$ personas pueden formarse a partir de un grupo de $8$ personas? Explica por qué el orden de elección no debe contarse.


**14.** **Nivel B.** A partir de $7$ objetos distintos, cuenta primero las selecciones ordenadas de $4$ objetos y luego deduce el número de selecciones no ordenadas. Explica con precisión por qué aparece el factor $4!$.


**15.** **Nivel B.** En un conjunto de $10$ elementos, compara el problema “elegir $4$ elementos” con el problema “decidir cuáles $6$ elementos quedan fuera”. Usa esta comparación para justificar una igualdad binomial concreta.


**16.** **Nivel C.** Demuestra combinatoriamente, mediante complementos, que
$$
\binom{n}{k}=\binom{n}{n-k}.
$$
Identifica explícitamente la biyección utilizada.


**17.** **Nivel C.** Sea $S$ un conjunto de $9$ elementos. Describe una biyección entre sus subconjuntos de tamaño $2$ y sus subconjuntos de tamaño $7$. Explica por qué la construcción es invertible.


**18.** **Nivel B.** Calcula el número total de subconjuntos de un conjunto de $6$ elementos sumando
$$
\binom{6}{0}+\binom{6}{1}+\cdots+\binom{6}{6}.
$$
Después obtén el mismo número razonando directamente sobre las dos posibilidades de pertenencia de cada elemento.


**19.** **Nivel C.** De un conjunto de $n$ elementos se quieren elegir $k$ elementos con la condición de que un elemento fijo $a$ esté incluido. ¿Cuántas elecciones hay? ¿Y cuántas hay si $a$ debe quedar excluido? Expresa ambas respuestas con coeficientes binomiales.


**20.** **Nivel C.** En un curso de $12$ estudiantes se forma un equipo de $5$. Demuestra que contar los equipos posibles es equivalente a contar los grupos de $7$ estudiantes que no quedan en el equipo. Formula la identidad binomial general que expresa este argumento.

## D. Pascal y recurrencia


**21.** **Nivel A.** Verifica numéricamente la identidad de Pascal para $(n,k)=(8,3)$ y para $(n,k)=(10,6)$.


**22.** **Nivel C.** Demuestra algebraicamente, usando factoriales, que para $1\le k\le n-1$,
$$
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$


**23.** **Nivel C.** Demuestra la identidad de Pascal por doble conteo: fija un elemento distinguido de un conjunto de $n$ elementos y separa los subconjuntos de tamaño $k$ según lo contengan o no.


**24.** **Nivel B.** Partiendo de la fila
$$
1,\ 7,\ 21,\ 35,\ 35,\ 21,\ 7,\ 1,
$$
construye la fila siguiente sin usar factoriales.


**25.** **Nivel C.** Usa únicamente los bordes y la recurrencia de Pascal para calcular $\binom{12}{5}$. Organiza los cálculos de modo que quede claro qué valores previos se necesitan.


**26.** **Nivel D.** Explica por qué las condiciones
$$
\binom{n}{0}=\binom{n}{n}=1
$$
y la identidad de Pascal determinan de manera única todas las entradas del triángulo. Formula el argumento como una inducción sobre $n$.


**27.** **Nivel C.** Un estudiante escribe
$$
\binom{n}{k}
=
\binom{n-1}{k-1}
+
\binom{n-2}{k}.
$$
Da un contraejemplo numérico, explica qué índice superior debe coincidir y repara la fórmula.


**28.** **Nivel D.** Demuestra, para los rangos en que todos los términos son significativos,
$$
\binom{n}{k-1}
+
2\binom{n}{k}
+
\binom{n}{k+1}
=
\binom{n+2}{k+1}.
$$
Hazlo en **dos etapas sucesivas de Pascal**: primero combina los dos pares de coeficientes de la fila $n$ y después combina los dos resultados de la fila $n+1$.

## E. Teorema del binomio y lectura de términos


**29.** **Nivel A.** Expande completamente $(x+y)^5$ mediante el teorema del binomio.


**30.** **Nivel B.** Expande completamente $(2x-y)^4$. Controla por separado el coeficiente numérico y el signo de cada término.


**31.** **Nivel B.** Determina el coeficiente de $x^5y^3$ en $(x+y)^8$ sin escribir la expansión completa.


**32.** **Nivel B.** Determina el coeficiente de $x^6$ en $(1+x)^{10}$ y explica qué valor de $k$ estás usando en el término general.


**33.** **Nivel B.** Identifica el término central de $(a+b)^{12}$ y justifica por qué es único.


**34.** **Nivel C.** Determina el término que contiene $x^4$ en $(3+x)^9$. Escribe tanto su coeficiente como la potencia completa.


**35.** **Nivel C.** Halla el coeficiente de $t^3$ en $(1-2t)^7$ sin expandir los demás términos.


**36.** **Nivel C.** Evalúa sin desarrollar término a término:
$$
\sum_{k=0}^{6}\binom{6}{k}2^{6-k}3^k.
$$
Indica qué sustitución en el teorema del binomio estás utilizando.


**37.** **Nivel C.** En la expansión de $(x+y)^7$, empareja cada término con el término simétrico correspondiente. Explica cómo la simetría $\binom{7}{k}=\binom{7}{7-k}$ se refleja simultáneamente en coeficientes y exponentes.


**38.** **Nivel C.** Obtén una fórmula en $n$ para el coeficiente de $x^{n-2}y^2$ en $(x+y)^n$, con $n\ge2$, y simplifícala.

## F. Pruebas del teorema


**39.** **Nivel B.** Partiendo de la expansión de $(x+y)^4$, multiplica por $(x+y)$ y reorganiza los términos hasta recuperar la fila de coeficientes de $(x+y)^5$. Señala en qué paso aparece Pascal.


**40.** **Nivel C.** En el paso inductivo del teorema del binomio aparece
$$
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k+1}.
$$
Haz la sustitución $j=k+1$ y escribe correctamente el nuevo índice, los nuevos límites y el nuevo sumando.


**41.** **Nivel C.** Explica por qué, después de alinear las dos sumas del paso inductivo, los términos de los extremos $k=0$ y $k=n+1$ deben tratarse separadamente antes de aplicar Pascal al rango interior.


**42.** **Nivel D.** Demuestra el teorema del binomio por inducción para todo $n\ge0$. Tu prueba debe mostrar explícitamente la reindexación y los términos extremos.


**43.** **Nivel C.** Da una prueba del teorema del binomio por elección de factores: explica por qué el coeficiente de $x^{n-k}y^k$ es exactamente $\binom{n}{k}$.


**44.** **Nivel D.** Compara la prueba inductiva y la prueba por elección de factores. Indica qué explica mejor cada una: la recurrencia de Pascal, la aparición de los coeficientes y el control formal de los índices.


**45.** **Nivel D.** Un estudiante transforma
$$
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k+1}
$$
en
$$
\sum_{k=0}^{n}\binom{n}{k-1}x^{n-k}y^k.
$$
Explica por qué la transformación no es una reindexación correcta y escribe la versión correcta.


**46.** **Nivel C.** Deduce del teorema del binomio una fórmula para $(x-y)^n$. Explica de dónde proviene el factor $(-1)^k$.

## G. Consecuencias e identidades ponderadas


**47.** **Nivel B.** Sustituye valores apropiados en el teorema del binomio para demostrar
$$
\sum_{k=0}^{n}\binom{n}{k}=2^n.
$$


**48.** **Nivel B.** Demuestra, para $n\ge1$,
$$
\sum_{k=0}^{n}(-1)^k\binom{n}{k}=0
$$
mediante una sustitución en el teorema del binomio.


**49.** **Nivel C.** Usa los dos ejercicios anteriores para demostrar que, para $n\ge1$, la suma de los coeficientes de índice par es igual a la suma de los coeficientes de índice impar y que ambas valen $2^{n-1}$.


**50.** **Nivel C.** Demuestra algebraicamente
$$
k\binom{n}{k}
=
n\binom{n-1}{k-1},
\qquad 1\le k\le n.
$$


**51.** **Nivel D.** Demuestra combinatoriamente la identidad del ejercicio anterior contando pares $(A,a)$ donde $A$ es un subconjunto de tamaño $k$ y $a$ es un elemento distinguido de $A$.


**52.** **Nivel D.** Sin usar cálculo, deduce
$$
\sum_{k=0}^{n}k\binom{n}{k}
=
n2^{n-1}.
$$
Usa primero una identidad local y luego una suma de fila.


**53.** **Nivel D.** Demuestra
$$
\sum_{k=0}^{n}(n-k)\binom{n}{k}
=
n2^{n-1}
$$
de dos maneras: usando simetría y usando directamente la identidad local correspondiente.


**54.** **Nivel D.** Deduce, para $n\ge1$,
$$
\sum_{k=0}^{n}(2k-n)\binom{n}{k}=0.
$$
Explica por qué el resultado también es compatible con la simetría de la fila.

## H. Hockey-stick y Vandermonde


**55.** **Nivel B.** Verifica numéricamente la identidad del palo de hockey para $r=2$ y $n=6$:
$$
\sum_{j=2}^{6}\binom{j}{2}
=
\binom{7}{3}.
$$


**56.** **Nivel D.** Demuestra, usando Pascal como telescopaje discreto, que
$$
\sum_{j=r}^{n}\binom{j}{r}
=
\binom{n+1}{r+1}.
$$


**57.** **Nivel D.** Da una prueba combinatoria del palo de hockey contando subconjuntos de tamaño $r+1$ de $\{1,\dots,n+1\}$ según su elemento máximo.


**58.** **Nivel C.** Verifica numéricamente Vandermonde para $r=4$, $s=5$ y $n=3$:
$$
\sum_k\binom{4}{k}\binom{5}{3-k}
=
\binom{9}{3}.
$$
Escribe sólo los valores de $k$ que contribuyen de forma no nula.


**59.** **Nivel D.** Para enteros no negativos $r,s,n$, determina el rango efectivo de $k$ en
$$
\binom{r}{k}\binom{s}{n-k}.
$$
Demuestra que puede escribirse como
$$
\max(0,n-s)\le k\le \min(r,n).
$$


**60.** **Nivel D.** Demuestra la identidad de Vandermonde
$$
\sum_k\binom{r}{k}\binom{s}{n-k}
=
\binom{r+s}{n}
$$
por doble conteo sobre la unión disjunta de dos conjuntos de tamaños $r$ y $s$.


**61.** **Nivel D.** Usa Vandermonde y simetría para demostrar
$$
\sum_{k=0}^{n}\binom{n}{k}^2
=
\binom{2n}{n}.
$$


**62.** **Nivel E.** Demuestra
$$
\sum_k\binom{r}{k}\binom{s}{k}
=
\binom{r+s}{r}
$$
transformando uno de los coeficientes por simetría y aplicando Vandermonde. Explicita el rango efectivo de la suma.

## I. Multinomio elemental


**63.** **Nivel B.** Determina el coeficiente de $x^2yz^3$ en $(x+y+z)^6$.


**64.** **Nivel C.** Expande completamente $(x+y+z)^3$ agrupando términos iguales y justificando cada coeficiente mediante elecciones de posiciones.


**65.** **Nivel C.** ¿Cuántas palabras de longitud $7$ pueden formarse con exactamente $3$ letras A, $2$ letras B y $2$ letras C? Expresa la respuesta como un coeficiente multinomial y calcula su valor.


**66.** **Nivel D.** Usa la expansión multinomial de $(x+y+z)^n$ y la sustitución $x=y=z=1$ para demostrar que la suma de todos los coeficientes trinomiales de orden $n$ es $3^n$.

## J. Diagnóstico y comparación de métodos


**67.** **Nivel C.** Un estudiante intenta probar simetría escribiendo
$$
\binom{n}{n-k}
=
\frac{n!}{(n-k)!(n-n-k)!}.
$$
Localiza exactamente el error de paréntesis y completa una prueba correcta.


**68.** **Nivel C.** Diagnostica el error en
$$
\binom{n}{k}
=
\binom{n-1}{k}
+
\binom{n}{k-1}.
$$
Explica por qué “tener dos términos parecidos” no basta para aplicar Pascal.


**69.** **Nivel C.** Un estudiante afirma que el término general de $(x+y)^n$ es
$$
\binom{n}{k}x^{n-k}y^{n+k}.
$$
Refuta la fórmula usando el grado total y escribe el término correcto.


**70.** **Nivel D.** Para cada una de las siguientes tareas, elige el método que consideres más natural entre factoriales, Pascal, sustitución en el binomio y doble conteo, y justifica tu elección:
$$
\binom{n}{k}=\binom{n}{n-k},
$$
$$
\sum_{k=0}^{n}\binom{n}{k}=2^n,
$$
$$
\sum_k\binom{r}{k}\binom{s}{n-k}=\binom{r+s}{n}.
$$


**71.** **Nivel D.** Compara una prueba factorial y una prueba combinatoria de la identidad de Pascal. Indica qué pasos son puramente algebraicos y qué estructura conceptual sólo se hace visible en el argumento combinatorio.


**72.** **Nivel E.** Se propone la siguiente reindexación:
$$
\sum_{k=0}^{n}a_k
=
\sum_{j=1}^{n+1}a_j.
$$
Explica por qué es falsa en general. Repara la igualdad y aplica la corrección al tipo de reindexación que aparece en la prueba inductiva del teorema del binomio.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra, para $0\le r\le n$,
$$
\sum_{j=r}^{n}\binom{j}{r}
=
\binom{n+1}{r+1}
$$
por dos métodos independientes:

a) reescribe cada término mediante Pascal de modo que la suma telescopie;

b) cuenta los subconjuntos de tamaño $r+1$ de $\{1,\dots,n+1\}$ clasificándolos por su elemento máximo.

Compara finalmente qué representa cada sumando en las dos pruebas y explica cuál de ellas hace más transparente la identidad.


**74.** **Nivel F.** Sean $r,s,n$ enteros no negativos. Demuestra la identidad de Vandermonde
$$
\sum_{k=\max(0,n-s)}^{\min(r,n)}
\binom{r}{k}\binom{s}{n-k}
=
\binom{r+s}{n}.
$$

Tu prueba principal debe ser de doble conteo y debe identificar con precisión el conjunto que se cuenta. Después, usando simetría y una reindexación adecuada, deduce como corolario
$$
\sum_k\binom{r}{k}\binom{s}{k}
=
\binom{r+s}{r}.
$$
Explica por qué escribir “$\sum_k$” exige o bien declarar la convención fuera de rango o bien conocer el rango efectivo.


**75.** **Nivel F.** Para $n\ge1$, demuestra
$$
\sum_{k=0}^{n}k\binom{n}{k}
=
n2^{n-1}
$$
sin usar derivadas.

Primero usa
$$
k\binom{n}{k}
=
n\binom{n-1}{k-1}
$$
y una reindexación completa. Después da una segunda prueba contando pares $(A,a)$ donde $A$ es un subconjunto de $\{1,\dots,n\}$ y $a\in A$ es distinguido. Compara las dos pruebas.


**76.** **Nivel F.** Sean $n\ge1$ y $0\le m<n$. Demuestra
$$
\sum_{k=0}^{m}(-1)^k\binom{n}{k}
=
(-1)^m\binom{n-1}{m}.
$$

Debes usar Pascal y reindexación. Separa con cuidado los extremos de las sumas y explica por qué la hipótesis $m<n$ evita confundir esta identidad con la suma alternada completa de una fila.


**77.** **Nivel F.** Para $0\le r\le k\le n$, demuestra
$$
\binom{n}{k}\binom{k}{r}
=
\binom{n}{r}\binom{n-r}{k-r}
$$
de dos maneras:

a) mediante factoriales;

b) contando pares de subconjuntos anidados $R\subseteq K\subseteq N$ con $|N|=n$, $|K|=k$ y $|R|=r$.

Explica qué orden de construcción corresponde a cada miembro.


**78.** **Nivel F.** Desarrolla conceptualmente el caso trinomial. Para enteros no negativos $a,b,c$ con $a+b+c=n$:

a) demuestra que el coeficiente de $x^ay^bz^c$ en $(x+y+z)^n$ es
$$
\frac{n!}{a!b!c!};
$$

b) explica el resultado mediante reparto de las $n$ posiciones entre tres categorías;

c) deduce, sustituyendo $x=y=z=1$, que la suma de todos los coeficientes trinomiales de orden $n$ es $3^n$.


**79.** **Nivel G.** Un estudiante propone la siguiente “prueba” inductiva. Supone
$$
(x+y)^n
=
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k
$$
y continúa:
$$
\begin{aligned}
(x+y)^{n+1}
&=
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^k(x+y)\\
&=
\sum_{k=1}^{n+1}\binom{n}{k}x^{n+1-k}y^k
+
\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k+1}\\
&=
\sum_{k=0}^{n+1}
\left(
\binom{n}{k-1}+\binom{n}{k+1}
\right)
x^{n+1-k}y^k\\
&=
\sum_{k=0}^{n+1}\binom{n+1}{k}x^{n+1-k}y^k.
\end{aligned}
$$

Localiza y explica **todos** los errores: rangos, reindexación, términos extremos, exponentes y uso de Pascal. Después reconstruye una demostración correcta completa.


**80.** **Nivel G.** Demuestra
$$
\sum_{k=0}^{n}\binom{n}{k}^2
=
\binom{2n}{n}
$$
por dos métodos:

a) transforma uno de los factores mediante simetría y aplica Vandermonde, controlando el rango;

b) divide un conjunto de $2n$ elementos en dos bloques de $n$ elementos y cuenta los subconjuntos de tamaño $n$ según cuántos elementos se eligen del primer bloque.

Compara qué información estructural aporta cada prueba.
***
## N. Construcción, traducción y revisión de pruebas

Todos los tamaños de conjuntos y posiciones son enteros no negativos, con las restricciones indicadas en cada problema. Se usa la convención de [§13.3](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s03) para los índices inferiores fuera de rango; no se admiten índices superiores negativos.


**81.** **Nivel C.** Sean $S$ un conjunto de $n\ge0$ elementos y $D\subseteq S$ con $|D|=m$, donde $0\le m\le n$. Para $0\le k\le n$, cuenta las elecciones $T$ de tamaño $k$ que contienen una cantidad **par** de elementos de $D$. Construye una suma binomial clasificando por $j=|T\cap D|$, deriva el rango efectivo y resuelve los casos $m=0$, $m=1$ y $m=n$. Para $m=2$, expresa el resultado con sólo dos términos.


**82.** **Nivel D.** Para $2\le k\le n$, clasifica los subconjuntos de tamaño $k$ de $\{1,\ldots,n\}$ según su **segundo elemento mayor** $j$. Construye la identidad resultante, determina todos los valores de $j$ y compruébala para $(n,k)=(5,3)$. Explica qué distingue esta clasificación de la clasificación por máximo.


**83.** **Nivel D.** Sean $n\ge1$, $1\le m\le n$ y $0\le k\le n$. En cada subconjunto $T\subseteq\{1,\ldots,n\}$ de tamaño $k$, examina $1,\ldots,m$ en ese orden. Clasifica $T$ por el **primer elemento ausente** de esa lista, o por el caso de que estén todos presentes. Construye una identidad binomial, usando la convención fuera de rango. Verifica el caso $k=0$ y explica por qué no basta sumar las clases «$j$ está ausente».


**84.** **Nivel C.** Interpreta
$$
\sum_{j=\max(0,q-s)}^{\min(r,q)}\binom rj\binom s{q-j}=\binom{r+s}{q}
$$
como un conteo de palabras de longitud $r+s$ formadas con $0$ y $1$ y con exactamente $q$ unos, donde $r,s\ge0$ y $0\le q\le r+s$. Identifica una biyección con elecciones de posiciones; comprueba el caso $(r,s,q)=(2,3,4)$ y explica qué ocurre si una palabra tiene longitud cero.


**85.** **Nivel D.** En un grupo de $n\ge2$ personas se elige un equipo de cualquier tamaño y, dentro de él, una presidencia y una secretaría ocupadas por personas distintas. Traduce este problema a una suma binomial y demuestra
$$
\sum_{k=0}^{n}k(k-1)\binom nk=n(n-1)2^{n-2}
$$
sin cálculo. Explica por qué no se divide por $2$ y verifica $n=2$.


**86.** **Nivel D.** En $n\ge0$ posiciones se marcan exactamente $\ell$ como reservadas, con $0\le\ell\le n$, y se selecciona un subconjunto cualquiera de las restantes. Traduce el conteo a
$$
\sum_{k=0}^{n-\ell}\binom nk\binom{n-k}{\ell}=\binom n\ell2^{n-\ell}.
$$
Describe los objetos que cuentan ambos lados y comprueba los extremos $\ell=0$ y $\ell=n$.


**87.** **Nivel E.** Se elimina la hipótesis de que $A$ y $B$ sean disjuntos en la prueba de Vandermonde. Para $A=\{a,b\}$, $B=\{b,c\}$ y elecciones de tamaño dos, muestra que sumar $\binom2j\binom2{2-j}$ no cuenta los subconjuntos de $A\cup B$. Después repara el argumento cuando $|A|=r$, $|B|=s$ y $|A\cap B|=t$, usando las tres partes disjuntas de la unión. Escribe una fórmula válida para todo $0\le q\le r+s-t$.


**88.** **Nivel C.** La igualdad entre las cantidades de subconjuntos de tamaño par e impar exige un conjunto con $n\ge1$ elementos. Examina qué pasa al retirar esa hipótesis. Para $n\ge1$, construye una correspondencia reversible que cambie sólo la pertenencia de un elemento fijo y justifique la igualdad. Para $n=0$, cuenta ambos tipos y explica exactamente qué paso de la construcción falla.


**89.** **Nivel D.** En el conteo de pares $(T,a)$ de [§13.12](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s12) se elimina la condición $a\in T$: ahora $T$ es cualquier subconjunto de un conjunto $S$ de tamaño $n\ge1$ y $a$ cualquier elemento de $S$. Construye el nuevo conteo y sepáralo en las clases $a\in T$ y $a\notin T$. Explica por qué conservar el peso $|T|$ daría una respuesta incorrecta.


**90.** **Nivel E.** Sean $r,s,t\ge0$ y $0\le q\le r+s+t$. Demuestra
$$
\sum_{i=0}^{r}\sum_{j=0}^{s}\binom ri\binom sj\binom t{q-i-j}=\binom{r+s+t}{q}
$$
con la convención fuera de rango, por dos vías: partición directa en tres bloques disjuntos y dos aplicaciones sucesivas de Vandermonde. Compara qué paso permite abarcar todos los tamaños de los bloques, incluidos los vacíos.


**91.** **Nivel E.** Define $W_n=\sum_{k=0}^{n}(-1)^k k\binom nk$ para $n\ge0$. Determina su valor para $n=0$, $n=1$ y $n\ge2$. Para $n\ge2$, compara una prueba con identidad local y reindexación con otra que empareje pares $(T,a)$, $a\in T$, de signos opuestos cambiando la pertenencia de un elemento distinto de $a$. Explica qué condición permite esa segunda elección.


**92.** **Nivel D.** Para $n\ge0$, demuestra $\sum_{k=0}^{n}2^k\binom nk=3^n$ por sustitución en el binomio y contando asignaciones de tres etiquetas a $n$ posiciones. En la segunda prueba, elige primero las posiciones cuya etiqueta será distinta de la primera. Compara qué paso garantiza la generalidad para cualquier $n$ y comprueba el caso vacío.

***
# Soluciones razonadas

## A. Leer el triángulo y la notación


### 1

Las filas $0$ a $7$ son

$$
\begin{aligned}
n=0:&\quad 1,\\
n=1:&\quad 1,\ 1,\\
n=2:&\quad 1,\ 2,\ 1,\\
n=3:&\quad 1,\ 3,\ 3,\ 1,\\
n=4:&\quad 1,\ 4,\ 6,\ 4,\ 1,\\
n=5:&\quad 1,\ 5,\ 10,\ 10,\ 5,\ 1,\\
n=6:&\quad 1,\ 6,\ 15,\ 20,\ 15,\ 6,\ 1,\\
n=7:&\quad 1,\ 7,\ 21,\ 35,\ 35,\ 21,\ 7,\ 1.
\end{aligned}
$$

Cada fila comienza y termina en $1$. Para una entrada interior se verifica la regla de Pascal: por ejemplo,

$$
21=6+15,\qquad 35=15+20.
$$

Así, cada entrada interior de la fila $n$ es la suma de las dos entradas adyacentes de la fila $n-1$.


### 2

De la fila $n=7$,

$$
1,\ 7,\ 21,\ 35,\ 35,\ 21,\ 7,\ 1,
$$

leemos

$$
\binom70=1,\qquad
\binom71=7,\qquad
\binom73=35,\qquad
\binom76=7,\qquad
\binom77=1.
$$


### 3

La fila que comienza por $1,8,\ldots$ es la fila $n=8$. Usando Pascal o la fila conocida,

$$
1,\ 8,\ 28,\ 56,\ 70,\ 56,\ 28,\ 8,\ 1.
$$

Por tanto, los espacios son

$$
28,\qquad 70,\qquad 28.
$$


### 4

En $\binom nk$, el índice superior $n$ indica el tamaño del conjunto de partida —y también la fila del triángulo de Pascal—. El índice inferior $k$ indica cuántos elementos se eligen —y también la posición dentro de esa fila, comenzando en $k=0$—.

Así,

$$
\binom94
$$

es el número de maneras de elegir $4$ elementos de un conjunto de $9$ elementos, y es la entrada de la fila $9$ situada en la posición $4$.


### 5

Con la convención fuera de rango,

$$
\binom6{-1}=0,\qquad
\binom60=1,\qquad
\binom66=1,\qquad
\binom67=0.
$$

La convención permite escribir identidades como Pascal sin separar continuamente los extremos. Sin embargo, no reemplaza el control de rangos: en una prueba debemos saber cuándo un coeficiente es genuinamente una elección $0\le k\le n$ y cuándo estamos usando deliberadamente el valor convencional $0$.


### 6

La simetría correcta mantiene fijo el índice superior:

$$
\binom nk=\binom n{n-k}.
$$

Por tanto,

$$
\binom94=\binom95,
$$

no $\binom49=\binom94$.

De hecho, $\binom49$ está fuera del rango natural porque $9>4$; con la convención fuera de rango vale $0$, mientras que

$$
\binom94=126.
$$

El error consiste en intercambiar los índices superior e inferior, cosa que la simetría no autoriza.

## B. Factoriales y fórmula cerrada


### 7

Cancelamos factoriales antes de expandirlos:

$$
\binom94
=
\frac{9!}{4!5!}
=
\frac{9\cdot8\cdot7\cdot6}{4\cdot3\cdot2\cdot1}
=126.
$$

Además,

$$
\binom{10}{2}
=
\frac{10\cdot9}{2}
=45,
$$

y

$$
\binom{12}{3}
=
\frac{12\cdot11\cdot10}{3\cdot2\cdot1}
=220.
$$


### 8

Las derivaciones factoriales siguientes se realizan respectivamente para $n\ge1$, $n\ge2$ y $n\ge3$, para que todos los argumentos factoriales sean no negativos.

A partir de

$$
\binom nk=\frac{n!}{k!(n-k)!},
$$

obtenemos

$$
\binom n1
=
\frac{n!}{(n-1)!}
=n,
$$

$$
\binom n2
=
\frac{n!}{2!(n-2)!}
=
\frac{n(n-1)}2,
$$

y

$$
\binom n3
=
\frac{n!}{3!(n-3)!}
=
\frac{n(n-1)(n-2)}6.
$$


### 9

Si $k=0$,

$$
\binom n0
=
\frac{n!}{0!(n-0)!}
=
\frac{n!}{0!\,n!}.
$$

Para que este caso valga $1$, necesitamos $0!=1$. Entonces

$$
\binom n0=1.
$$

Si $k=n$,

$$
\binom nn
=
\frac{n!}{n!(n-n)!}
=
\frac{n!}{n!\,0!}
=1.
$$

Así, la convención $0!=1$ permite que una sola fórmula factorial incluya ambos extremos sin excepciones.


### 10

Usando la fórmula factorial,

$$
\frac{\binom{n}{k+1}}{\binom nk}
=
\frac{\dfrac{n!}{(k+1)!(n-k-1)!}}
{\dfrac{n!}{k!(n-k)!}}.
$$

Multiplicando por el recíproco,

$$
=
\frac{k!(n-k)!}{(k+1)!(n-k-1)!}
=
\frac{n-k}{k+1}.
$$

Por tanto,

$$
\boxed{
\frac{\binom{n}{k+1}}{\binom nk}
=
\frac{n-k}{k+1}
}.
$$

Esta razón permite comparar coeficientes consecutivos. Si $n-k>k+1$, el cociente es mayor que $1$ y los coeficientes aumentan; si $n-k<k+1$, disminuyen; y si son iguales, dos coeficientes consecutivos coinciden.


### 11

Factorialmente,

$$
\binom{10}{7}
=
\frac{10!}{7!3!}
=
\frac{10!}{3!7!}
=
\binom{10}{3}.
$$

La igualdad era previsible por simetría:

$$
\binom{10}{7}
=
\binom{10}{10-7}
=
\binom{10}{3}.
$$

Elegir $7$ elementos equivale a decidir cuáles $3$ quedan fuera.


### 12

Usamos

$$
\binom n2=\frac{n(n-1)}2.
$$

La ecuación es

$$
\frac{n(n-1)}2=45.
$$

Multiplicando por $2$,

$$
n(n-1)=90,
$$

de modo que

$$
n^2-n-90=0.
$$

Factorizamos:

$$
(n-10)(n+9)=0.
$$

Las soluciones algebraicas son $n=10$ y $n=-9$, pero se exige $n\ge2$. Por tanto,

$$
\boxed{n=10}.
$$

Comprobación:

$$
\binom{10}{2}=\frac{10\cdot9}{2}=45.
$$

## C. Interpretación combinatoria y simetría


### 13

Un comité de $3$ personas se obtiene eligiendo $3$ personas de un grupo de $8$, sin importar el orden:

$$
\binom83
=
\frac{8\cdot7\cdot6}{3\cdot2\cdot1}
=56.
$$

El orden no debe contarse porque el comité $\{A,B,C\}$ es el mismo tanto si las personas se nombran como $A,B,C$ como si se nombran en cualquiera de sus otras $3!$ ordenaciones.


### 14

Las selecciones ordenadas de $4$ objetos distintos tomados de $7$ son

$$
7\cdot6\cdot5\cdot4=840.
$$

Cada conjunto no ordenado de $4$ objetos aparece exactamente $4!$ veces en ese conteo, una por cada ordenación posible de sus cuatro elementos. Por tanto,

$$
\frac{840}{4!}
=
\frac{840}{24}
=35.
$$

Así,

$$
\binom74=35.
$$


### 15

Elegir $4$ elementos de un conjunto de $10$ determina automáticamente cuáles $6$ quedan fuera, y viceversa. La correspondencia es tomar complemento.

Por eso ambos problemas tienen el mismo número de soluciones:

$$
\boxed{\binom{10}{4}=\binom{10}{6}}.
$$

Numéricamente,

$$
\binom{10}{4}=\binom{10}{6}=210.
$$


### 16

Sea $S$ un conjunto con $n$ elementos. Consideremos la aplicación

$$
\Phi(A)=S\setminus A.
$$

Si $|A|=k$, entonces

$$
|\Phi(A)|=n-k.
$$

Además, $\Phi$ es invertible porque

$$
\Phi(\Phi(A))
=
S\setminus(S\setminus A)
=A.
$$

Por tanto, $\Phi$ es una biyección entre los subconjuntos de tamaño $k$ y los subconjuntos de tamaño $n-k$. Luego ambos conjuntos tienen la misma cardinalidad:

$$
\boxed{\binom nk=\binom n{n-k}}.
$$


### 17

Sea $S$ un conjunto de $9$ elementos. A cada subconjunto $A\subseteq S$ con $|A|=2$ le asociamos

$$
S\setminus A.
$$

El complemento tiene tamaño $9-2=7$. La operación es invertible, pues el complemento del complemento devuelve $A$:

$$
S\setminus(S\setminus A)=A.
$$

Así obtenemos una biyección entre subconjuntos de tamaño $2$ y subconjuntos de tamaño $7$, lo que explica

$$
\binom92=\binom97.
$$


### 18

La suma por tamaños es

$$
\sum_{k=0}^{6}\binom6k
=
1+6+15+20+15+6+1
=64.
$$

Directamente, cada uno de los $6$ elementos tiene dos posibilidades independientes: pertenecer o no pertenecer al subconjunto. Por tanto hay

$$
2^6=64
$$

subconjuntos.

Ambos razonamientos cuentan el mismo conjunto de objetos, luego

$$
\sum_{k=0}^{6}\binom6k=2^6.
$$


### 19

Si el elemento fijo $a$ debe estar incluido, ya hemos elegido uno de los $k$ elementos. Los otros $k-1$ se eligen entre los $n-1$ elementos restantes:

$$
\boxed{\binom{n-1}{k-1}}.
$$

Si $a$ debe quedar excluido, los $k$ elementos deben elegirse entre los otros $n-1$:

$$
\boxed{\binom{n-1}{k}}.
$$

Estas dos clases son precisamente las que aparecen en la prueba combinatoria de Pascal.


### 20

El número de equipos de $5$ estudiantes formados desde un curso de $12$ es

$$
\binom{12}{5}.
$$

Cada equipo determina exactamente el grupo complementario de $7$ estudiantes que quedan fuera, y cada grupo de $7$ excluidos determina el equipo de los otros $5$. Por complemento,

$$
\binom{12}{5}=\binom{12}{7}.
$$

En general, para $0\le k\le n$,

$$
\boxed{\binom nk=\binom n{n-k}}.
$$

## D. Pascal y recurrencia


### 21

Para $(n,k)=(8,3)$,

$$
\binom83=56,
$$

mientras que

$$
\binom72+\binom73
=
21+35
=56.
$$

Para $(n,k)=(10,6)$,

$$
\binom{10}{6}=210,
$$

y

$$
\binom95+\binom96
=
126+84
=210.
$$

En ambos casos se verifica

$$
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$


### 22

Partimos del lado derecho:

$$
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$

Usando factoriales,

$$
=
\frac{(n-1)!}{(k-1)!(n-k)!}
+
\frac{(n-1)!}{k!(n-k-1)!}.
$$

Llevamos ambas fracciones al denominador común $k!(n-k)!$:

$$
=
\frac{k(n-1)!}{k!(n-k)!}
+
\frac{(n-k)(n-1)!}{k!(n-k)!}.
$$

Entonces

$$
=
\frac{[k+(n-k)](n-1)!}{k!(n-k)!}
=
\frac{n!}{k!(n-k)!}
=
\binom nk.
$$

Por tanto,

$$
\boxed{
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
}.
$$


### 23

Sea $S$ un conjunto con $n$ elementos y fijemos $a\in S$. Contamos los subconjuntos de tamaño $k$ de $S$.

Se dividen en dos clases disjuntas:

- los que contienen a $a$;
- los que no contienen a $a$.

Si contienen a $a$, faltan $k-1$ elementos por elegir entre los $n-1$ restantes, de modo que hay

$$
\binom{n-1}{k-1}
$$

posibilidades.

Si no contienen a $a$, debemos elegir los $k$ elementos entre los otros $n-1$, y hay

$$
\binom{n-1}{k}
$$

posibilidades.

Como las dos clases son disjuntas y exhaustivas,

$$
\boxed{
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
}.
$$


### 24

La fila dada es la fila $n=7$. La siguiente comienza y termina en $1$, y cada entrada interior es suma de dos entradas contiguas:

$$
\begin{aligned}
1,\;&1+7,\;7+21,\;21+35,\;35+35,\\
&35+21,\;21+7,\;7+1,\;1.
\end{aligned}
$$

Por tanto, la fila $n=8$ es

$$
\boxed{
1,\ 8,\ 28,\ 56,\ 70,\ 56,\ 28,\ 8,\ 1
}.
$$


### 25

Usamos únicamente la recurrencia de Pascal. Para llegar a $\binom{12}{5}$ basta construir sucesivamente las entradas necesarias:

$$
\binom55=1.
$$

Después,

$$
\binom64=\binom53+\binom54=10+5=15,
$$

pero es más transparente avanzar por filas completas alrededor de la zona necesaria:

$$
\begin{aligned}
n=7:&\quad 1,\ 7,\ 21,\ 35,\ldots\\
n=8:&\quad 1,\ 8,\ 28,\ 56,\ 70,\ldots\\
n=9:&\quad 1,\ 9,\ 36,\ 84,\ 126,\ 126,\ldots\\
n=10:&\quad 1,\ 10,\ 45,\ 120,\ 210,\ 252,\ldots\\
n=11:&\quad 1,\ 11,\ 55,\ 165,\ 330,\ 462,\ldots\\
n=12:&\quad 1,\ 12,\ 66,\ 220,\ 495,\ 792,\ldots
\end{aligned}
$$

Por tanto,

$$
\boxed{\binom{12}{5}=792}.
$$

Cada valor se obtiene exclusivamente sumando dos entradas de la fila anterior.


### 26

Demostramos por inducción sobre la fila $n$ que las reglas determinan una única fila.

**Caso base.** Para $n=0$, la condición de borde obliga a que la única entrada sea

$$
\binom00=1.
$$

Por tanto, la fila $0$ está determinada de manera única.

**Paso inductivo.** Supongamos determinada de manera única toda la fila $n-1$. En la fila $n$, los extremos están fijados:

$$
\binom n0=\binom nn=1.
$$

Para cada posición interior $1\le k\le n-1$, Pascal obliga a definir

$$
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$

Por hipótesis inductiva, las dos entradas del lado derecho ya tienen valores únicos. Luego cada entrada interior de la fila $n$ también queda determinada de manera única.

Así, por inducción, los bordes junto con Pascal determinan todas las entradas del triángulo.


### 27

Tomemos, por ejemplo, $n=5$ y $k=2$. La fórmula propuesta daría

$$
\binom52
\stackrel{?}{=}
\binom41+\binom32.
$$

Pero

$$
10\ne4+3=7.
$$

El error es que en Pascal los dos términos del lado derecho deben tener el mismo índice superior $n-1$ y los índices inferiores deben ser consecutivos.

La fórmula correcta es

$$
\boxed{
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
}.
$$


### 28

Agrupamos los cuatro términos para aplicar Pascal en dos etapas:

$$
\binom n{k-1}
+
2\binom nk
+
\binom n{k+1}
$$

$$
=
\left(
\binom n{k-1}+\binom nk
\right)
+
\left(
\binom nk+\binom n{k+1}
\right).
$$

En la primera etapa aplicamos Pascal a cada par,

$$
=
\binom{n+1}{k}
+
\binom{n+1}{k+1}.
$$

En la segunda etapa aplicamos Pascal a los dos resultados,

$$
=
\boxed{\binom{n+2}{k+1}}.
$$

Por ejemplo, la identidad vale directamente para $1\le k\le n-1$; con la convención fuera de rango puede extenderse uniformemente a los bordes apropiados.

## E. Teorema del binomio y lectura de términos


### 29

El teorema del binomio da

$$
(x+y)^5
=
\sum_{k=0}^{5}\binom5k x^{5-k}y^k.
$$

La fila $5$ es $1,5,10,10,5,1$. Por tanto,

$$
\boxed{
(x+y)^5
=
x^5+5x^4y+10x^3y^2+10x^2y^3+5xy^4+y^5
}.
$$


### 30

Escribimos

$$
(2x-y)^4
=
\sum_{k=0}^{4}
\binom4k(2x)^{4-k}(-y)^k.
$$

Calculando término a término,

$$
\begin{aligned}
(2x-y)^4
&=16x^4
-32x^3y
+24x^2y^2
-8xy^3
+y^4.
\end{aligned}
$$

Así,

$$
\boxed{
(2x-y)^4
=
16x^4-32x^3y+24x^2y^2-8xy^3+y^4
}.
$$

El signo viene de $(-1)^k$ y el factor numérico de $\binom4k2^{4-k}$.


### 31

En el término general

$$
\binom8k x^{8-k}y^k,
$$

queremos $y^3$, así que $k=3$. Entonces automáticamente el exponente de $x$ es $8-3=5$.

El coeficiente es

$$
\binom83=56.
$$

Por tanto, el coeficiente de $x^5y^3$ es

$$
\boxed{56}.
$$


### 32

En

$$
(1+x)^{10}
=
\sum_{k=0}^{10}\binom{10}{k}1^{10-k}x^k,
$$

la potencia de $x$ es precisamente $k$. Para obtener $x^6$, tomamos $k=6$.

Por tanto, el coeficiente es

$$
\binom{10}{6}=210.
$$

Así, la respuesta es

$$
\boxed{210}.
$$


### 33

En $(a+b)^{12}$ los términos son

$$
\binom{12}{k}a^{12-k}b^k.
$$

Un término central debe tener los mismos exponentes de $a$ y $b$:

$$
12-k=k.
$$

De aquí,

$$
k=6.
$$

Como $12$ es par, existe un único valor entero medio. El término central es

$$
\boxed{
\binom{12}{6}a^6b^6
=
924a^6b^6
}.
$$


### 34

En

$$
(3+x)^9
=
\sum_{k=0}^{9}\binom9k3^{9-k}x^k,
$$

el término con $x^4$ corresponde a $k=4$. Por tanto,

$$
\binom94 3^5x^4.
$$

Como

$$
\binom94=126,\qquad 3^5=243,
$$

el coeficiente es

$$
126\cdot243=30618.
$$

Así, el término pedido es

$$
\boxed{30618x^4}.
$$


### 35

En

$$
(1-2t)^7
=
\sum_{k=0}^{7}\binom7k(-2t)^k,
$$

el término con $t^3$ corresponde a $k=3$. Su coeficiente es

$$
\binom73(-2)^3
=
35(-8)
=
-280.
$$

Por tanto,

$$
\boxed{-280}.
$$


### 36

La suma tiene exactamente la forma binomial

$$
\sum_{k=0}^{6}
\binom6k
2^{6-k}3^k
=
(2+3)^6.
$$

Entonces

$$
(2+3)^6=5^6=15625.
$$

Por tanto,

$$
\boxed{15625}.
$$


### 37

El término de índice $k$ es

$$
\binom7k x^{7-k}y^k.
$$

Su término simétrico corresponde al índice $7-k$:

$$
\binom7{7-k}x^ky^{7-k}.
$$

Como

$$
\binom7k=\binom7{7-k},
$$

los coeficientes coinciden, mientras que los exponentes de $x$ e $y$ se intercambian.

Los emparejamientos son

$$
k=0\leftrightarrow7,\quad
1\leftrightarrow6,\quad
2\leftrightarrow5,\quad
3\leftrightarrow4.
$$

Así, la simetría de la fila se refleja en una simetría de la expansión bajo el intercambio $x\leftrightarrow y$.


### 38

El término general es

$$
\binom nk x^{n-k}y^k.
$$

Para obtener $x^{n-2}y^2$ debemos tomar $k=2$. El coeficiente es entonces

$$
\binom n2
=
\frac{n(n-1)}2.
$$

Por tanto,

$$
\boxed{\frac{n(n-1)}2}.
$$

## F. Pruebas del teorema


### 39

Partimos de

$$
(x+y)^4
=
x^4+4x^3y+6x^2y^2+4xy^3+y^4.
$$

Multiplicamos por $(x+y)$:

$$
\begin{aligned}
(x+y)^5
&=
x(x+y)^4+y(x+y)^4\\
&=
x^5+4x^4y+6x^3y^2+4x^2y^3+xy^4\\
&\quad+x^4y+4x^3y^2+6x^2y^3+4xy^4+y^5.
\end{aligned}
$$

Reagrupando monomios iguales,

$$
\begin{aligned}
(x+y)^5
&=
x^5+(4+1)x^4y+(6+4)x^3y^2\\
&\quad +(4+6)x^2y^3+(1+4)xy^4+y^5\\
&=
x^5+5x^4y+10x^3y^2+10x^2y^3+5xy^4+y^5.
\end{aligned}
$$

Pascal aparece exactamente al sumar coeficientes vecinos de la fila anterior:

$$
4+1=5,\qquad
6+4=10,\qquad
4+6=10,\qquad
1+4=5.
$$


### 40

Hacemos

$$
j=k+1,
\qquad
k=j-1.
$$

Si $k=0$, entonces $j=1$; si $k=n$, entonces $j=n+1$.

Además,

$$
\binom nk x^{n-k}y^{k+1}
=
\binom n{j-1}
x^{n-(j-1)}y^j
=
\binom n{j-1}
x^{n+1-j}y^j.
$$

Por tanto,

$$
\boxed{
\sum_{k=0}^{n}\binom nk x^{n-k}y^{k+1}
=
\sum_{j=1}^{n+1}
\binom n{j-1}
x^{n+1-j}y^j
}.
$$


### 41

Después de reindexar, las dos sumas tienen rangos

$$
0\le k\le n
$$

y

$$
1\le k\le n+1.
$$

Por tanto, el término $k=0$ aparece sólo en la primera suma y el término $k=n+1$ sólo en la segunda. Sólo para

$$
1\le k\le n
$$

aparecen simultáneamente ambos coeficientes que deben combinarse mediante Pascal.

En concreto, los extremos son

$$
\binom n0x^{n+1}=x^{n+1}
$$

y

$$
\binom nny^{n+1}=y^{n+1}.
$$

En el rango interior aparecen

$$
\left(
\binom nk+\binom n{k-1}
\right)x^{n+1-k}y^k
=
\binom{n+1}{k}x^{n+1-k}y^k.
$$

Separar los extremos evita introducir términos inexistentes o aplicar Pascal fuera del par correcto.


### 42

Sea

$$
P(n):
\qquad
(x+y)^n
=
\sum_{k=0}^{n}\binom nkx^{n-k}y^k.
$$

**Caso base.** Para $n=0$,

$$
(x+y)^0=1
$$

y

$$
\sum_{k=0}^{0}\binom0k x^{0-k}y^k
=
\binom00=1.
$$

Luego $P(0)$ es verdadera.

**Hipótesis inductiva.** Supongamos

$$
(x+y)^n
=
\sum_{k=0}^{n}\binom nkx^{n-k}y^k.
$$

Multiplicando por $(x+y)$,

$$
\begin{aligned}
(x+y)^{n+1}
&=
\sum_{k=0}^{n}\binom nkx^{n+1-k}y^k\\
&\quad+
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1}.
\end{aligned}
$$

En la segunda suma hacemos $j=k+1$:

$$
\sum_{j=1}^{n+1}
\binom n{j-1}
x^{n+1-j}y^j.
$$

Renombrando $j$ como $k$,

$$
\begin{aligned}
(x+y)^{n+1}
&=
\sum_{k=0}^{n}\binom nkx^{n+1-k}y^k\\
&\quad+
\sum_{k=1}^{n+1}\binom n{k-1}x^{n+1-k}y^k.
\end{aligned}
$$

Separamos extremos. Para $k=0$ queda $x^{n+1}$ y para $k=n+1$ queda $y^{n+1}$. En $1\le k\le n$,

$$
\binom nk+\binom n{k-1}
=
\binom{n+1}{k}.
$$

Por tanto,

$$
\begin{aligned}
(x+y)^{n+1}
&=
x^{n+1}
+
\sum_{k=1}^{n}
\binom{n+1}{k}x^{n+1-k}y^k
+
y^{n+1}\\
&=
\sum_{k=0}^{n+1}
\binom{n+1}{k}x^{n+1-k}y^k.
\end{aligned}
$$

Así $P(n+1)$ es verdadera. Por inducción, el teorema del binomio vale para todo $n\ge0$.


### 43

Escribimos

$$
(x+y)^n
=
\underbrace{(x+y)\cdots(x+y)}_{n\text{ factores}}.
$$

Al expandir, en cada factor debemos elegir $x$ o $y$. Para producir exactamente

$$
x^{n-k}y^k,
$$

debemos elegir $y$ en exactamente $k$ de los $n$ factores. Los restantes $n-k$ factores aportan $x$.

El número de maneras de escoger cuáles $k$ factores aportan $y$ es

$$
\binom nk.
$$

Por eso el coeficiente de $x^{n-k}y^k$ es precisamente $\binom nk$, y

$$
(x+y)^n
=
\sum_{k=0}^{n}\binom nkx^{n-k}y^k.
$$


### 44

Las dos pruebas establecen el mismo teorema, pero iluminan estructuras distintas.

La **prueba inductiva** explica especialmente bien la recurrencia de Pascal. Al pasar de $(x+y)^n$ a $(x+y)^{n+1}$, cada monomio interior recibe dos contribuciones provenientes de coeficientes vecinos:

$$
\binom nk+\binom n{k-1}
=
\binom{n+1}{k}.
$$

También obliga a controlar formalmente reindexación, límites y términos extremos.

La **prueba por elección de factores** explica mejor por qué aparece $\binom nk$: producir $x^{n-k}y^k$ equivale a elegir exactamente $k$ de los $n$ factores que aportarán $y$.

En resumen:

- recurrencia de Pascal: más visible en la prueba inductiva;
- aparición conceptual de los coeficientes: más visible en la prueba combinatoria;
- control formal de índices: más exigente y explícito en la prueba inductiva.


### 45

La transformación propuesta falla en tres lugares: no modifica correctamente los límites, no transforma todos los exponentes y cambia el coeficiente sin justificar la sustitución.

Si hacemos

$$
j=k+1,
\qquad k=j-1,
$$

entonces $j$ recorre desde $1$ hasta $n+1$, y

$$
\binom nkx^{n-k}y^{k+1}
=
\binom n{j-1}x^{n+1-j}y^j.
$$

La reindexación correcta es

$$
\boxed{
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1}
=
\sum_{j=1}^{n+1}
\binom n{j-1}x^{n+1-j}y^j
}.
$$

Sólo después puede renombrarse $j$ como $k$.


### 46

Aplicamos el teorema del binomio a $x+(-y)$:

$$
(x-y)^n
=
\sum_{k=0}^{n}
\binom nkx^{n-k}(-y)^k.
$$

Como

$$
(-y)^k=(-1)^ky^k,
$$

obtenemos

$$
\boxed{
(x-y)^n
=
\sum_{k=0}^{n}
(-1)^k\binom nkx^{n-k}y^k
}.
$$

El factor $(-1)^k$ proviene exclusivamente de elevar el segundo sumando negativo a la potencia $k$.

## G. Consecuencias e identidades ponderadas


### 47

En el teorema del binomio tomamos $x=y=1$:

$$
(1+1)^n
=
\sum_{k=0}^{n}
\binom nk1^{n-k}1^k.
$$

Entonces

$$
2^n
=
\sum_{k=0}^{n}\binom nk.
$$

Por tanto,

$$
\boxed{
\sum_{k=0}^{n}\binom nk=2^n
}.
$$


### 48

Tomamos $x=1$ e $y=-1$. Para $n\ge1$,

$$
(1-1)^n=0.
$$

Por el teorema del binomio,

$$
0
=
\sum_{k=0}^{n}
\binom nk1^{n-k}(-1)^k
=
\sum_{k=0}^{n}
(-1)^k\binom nk.
$$

Así,

$$
\boxed{
\sum_{k=0}^{n}
(-1)^k\binom nk=0
}.
$$


### 49

Sea

$$
E=\sum_{\substack{0\le k\le n\\k\text{ par}}}\binom nk,
\qquad
O=\sum_{\substack{0\le k\le n\\k\text{ impar}}}\binom nk.
$$

Del ejercicio 47,

$$
E+O=2^n.
$$

Del ejercicio 48,

$$
E-O=0.
$$

Por tanto,

$$
E=O.
$$

Sustituyendo en la primera ecuación,

$$
2E=2^n,
$$

de modo que

$$
E=O=2^{n-1}.
$$

Así, para $n\ge1$,

$$
\boxed{
\sum_{k\text{ par}}\binom nk
=
\sum_{k\text{ impar}}\binom nk
=
2^{n-1}
}.
$$


### 50

Usando factoriales,

$$
k\binom nk
=
k\frac{n!}{k!(n-k)!}.
$$

Como $k!=k(k-1)!$,

$$
k\binom nk
=
\frac{n!}{(k-1)!(n-k)!}.
$$

Por otra parte,

$$
n\binom{n-1}{k-1}
=
n\frac{(n-1)!}{(k-1)!(n-k)!}
=
\frac{n!}{(k-1)!(n-k)!}.
$$

Por tanto,

$$
\boxed{
k\binom nk
=
n\binom{n-1}{k-1}
}.
$$


### 51

Sea $S$ un conjunto de $n$ elementos. Contemos pares $(A,a)$ tales que

$$
A\subseteq S,\qquad |A|=k,\qquad a\in A
$$

y $a$ está distinguido.

**Primer conteo.** Elegimos primero $A$: hay $\binom nk$ posibilidades. Dentro de $A$ elegimos el elemento distinguido: hay $k$ opciones. Total:

$$
k\binom nk.
$$

**Segundo conteo.** Elegimos primero $a$: hay $n$ posibilidades. Después elegimos los otros $k-1$ elementos de $A$ entre los $n-1$ restantes:

$$
n\binom{n-1}{k-1}.
$$

Ambos procedimientos cuentan exactamente los mismos pares, de modo que

$$
\boxed{
k\binom nk
=
n\binom{n-1}{k-1}
}.
$$


### 52

Para $n=0$, ambos lados valen cero: la suma contiene $0\binom00=0$ y $n2^{n-1}=0\cdot2^{-1}=0$. Este caso se comprueba directamente; no requiere una fila de índice superior $-1$. En lo que sigue suponemos $n\ge1$.

El término $k=0$ es nulo, así que

$$
\sum_{k=0}^{n}k\binom nk
=
\sum_{k=1}^{n}k\binom nk.
$$

Usamos la identidad local

$$
k\binom nk
=
n\binom{n-1}{k-1}:
$$

$$
\sum_{k=1}^{n}k\binom nk
=
n\sum_{k=1}^{n}\binom{n-1}{k-1}.
$$

Reindexamos con $j=k-1$. Entonces $j$ recorre $0,\ldots,n-1$:

$$
=
n\sum_{j=0}^{n-1}\binom{n-1}{j}.
$$

La suma de la fila $n-1$ es $2^{n-1}$. Por tanto,

$$
\boxed{
\sum_{k=0}^{n}k\binom nk
=
n2^{n-1}
}.
$$


### 53

Para $n=0$, ambos lados valen cero por evaluación directa. Las dos pruebas siguientes se realizan para $n\ge1$, de modo que la fila $n-1$ existe.

**Primera prueba: simetría.**

Hacemos $j=n-k$. Entonces

$$
(n-k)\binom nk
=
j\binom n{n-j}
=
j\binom nj.
$$

Al recorrer $k=0,\ldots,n$, el nuevo índice $j$ recorre los mismos valores en orden inverso. Por tanto,

$$
\sum_{k=0}^{n}(n-k)\binom nk
=
\sum_{j=0}^{n}j\binom nj
=
n2^{n-1}.
$$

**Segunda prueba: identidad local.**

Factorialmente o por doble conteo,

$$
(n-k)\binom nk
=
n\binom{n-1}{k}.
$$

Entonces

$$
\sum_{k=0}^{n}(n-k)\binom nk
=
n\sum_{k=0}^{n}\binom{n-1}{k}.
$$

El término $k=n$ vale $0$ bajo la convención fuera de rango, por lo que

$$
=
n\sum_{k=0}^{n-1}\binom{n-1}{k}
=
n2^{n-1}.
$$

Así,

$$
\boxed{
\sum_{k=0}^{n}(n-k)\binom nk=n2^{n-1}
}.
$$


### 54

Por linealidad,

$$
\sum_{k=0}^{n}(2k-n)\binom nk
=
2\sum_{k=0}^{n}k\binom nk
-
n\sum_{k=0}^{n}\binom nk.
$$

Usando

$$
\sum_{k=0}^{n}k\binom nk=n2^{n-1}
$$

y

$$
\sum_{k=0}^{n}\binom nk=2^n,
$$

obtenemos

$$
2n2^{n-1}-n2^n
=
n2^n-n2^n
=0.
$$

Por tanto,

$$
\boxed{
\sum_{k=0}^{n}(2k-n)\binom nk=0
}.
$$

La simetría también lo explica: los términos de índices $k$ y $n-k$ tienen el mismo coeficiente binomial, mientras que sus pesos son opuestos:

$$
2(n-k)-n=-(2k-n).
$$

Por eso se cancelan por pares.

## H. Hockey-stick y Vandermonde


### 55

Calculamos

$$
\sum_{j=2}^{6}\binom j2
=
\binom22+\binom32+\binom42+\binom52+\binom62.
$$

Esto vale

$$
1+3+6+10+15=35.
$$

Por otra parte,

$$
\binom73=35.
$$

Así,

$$
\boxed{
\sum_{j=2}^{6}\binom j2=\binom73
}.
$$


### 56

De Pascal,

$$
\binom{j+1}{r+1}
=
\binom jr+\binom j{r+1}.
$$

Despejamos

$$
\binom jr
=
\binom{j+1}{r+1}
-
\binom j{r+1}.
$$

Sumando desde $j=r$ hasta $n$,

$$
\sum_{j=r}^{n}\binom jr
=
\sum_{j=r}^{n}
\left(
\binom{j+1}{r+1}
-
\binom j{r+1}
\right).
$$

Al expandir, todos los términos interiores se cancelan:

$$
\begin{aligned}
&\left(\binom{r+1}{r+1}-\binom r{r+1}\right)
+\left(\binom{r+2}{r+1}-\binom{r+1}{r+1}\right)\\
&\qquad+\cdots+
\left(\binom{n+1}{r+1}-\binom n{r+1}\right).
\end{aligned}
$$

Como $\binom r{r+1}=0$, queda

$$
\boxed{
\sum_{j=r}^{n}\binom jr
=
\binom{n+1}{r+1}
}.
$$


### 57

Contemos los subconjuntos de tamaño $r+1$ de

$$
\{1,2,\ldots,n+1\}.
$$

Directamente hay

$$
\binom{n+1}{r+1}
$$

subconjuntos.

Ahora los clasificamos por su elemento máximo. Si el máximo es $j+1$, los otros $r$ elementos deben elegirse entre

$$
\{1,\ldots,j\},
$$

lo que puede hacerse de

$$
\binom jr
$$

formas.

El máximo puede ser $r+1,r+2,\ldots,n+1$, es decir, $j$ recorre $r,\ldots,n$. Sumando todas las clases,

$$
\sum_{j=r}^{n}\binom jr
=
\binom{n+1}{r+1}.
$$

Así queda demostrada combinatoriamente la identidad del palo de hockey.


### 58

Para que ambos factores sean no nulos necesitamos

$$
0\le k\le4
$$

y

$$
0\le3-k\le5.
$$

Aquí los valores efectivos son $k=0,1,2,3$. Entonces

$$
\begin{aligned}
\sum_k\binom4k\binom5{3-k}
&=
\binom40\binom53
+\binom41\binom52
+\binom42\binom51
+\binom43\binom50\\
&=
1\cdot10+4\cdot10+6\cdot5+4\cdot1\\
&=
10+40+30+4\\
&=84.
\end{aligned}
$$

Además,

$$
\binom93=84.
$$

Por tanto se verifica Vandermonde.


### 59

Para que

$$
\binom rk\binom s{n-k}
$$

sea no nulo, deben cumplirse simultáneamente

$$
0\le k\le r
$$

y

$$
0\le n-k\le s.
$$

La segunda doble desigualdad equivale a

$$
n-s\le k\le n.
$$

Combinando ambas condiciones obtenemos

$$
k\ge0,\qquad k\ge n-s,
$$

es decir,

$$
k\ge\max(0,n-s),
$$

y también

$$
k\le r,\qquad k\le n,
$$

es decir,

$$
k\le\min(r,n).
$$

Por tanto, el rango efectivo es

$$
\boxed{
\max(0,n-s)\le k\le\min(r,n)
}.
$$


### 60

Sean $A$ y $B$ conjuntos disjuntos con

$$
|A|=r,\qquad |B|=s.
$$

Contemos los subconjuntos de tamaño $n$ de $A\cup B$.

Directamente, como

$$
|A\cup B|=r+s,
$$

hay

$$
\binom{r+s}{n}
$$

elecciones.

Ahora clasificamos cada subconjunto según cuántos elementos contiene de $A$. Si contiene exactamente $k$ elementos de $A$, debemos elegir

$$
\binom rk
$$

elementos de $A$ y

$$
\binom s{n-k}
$$

elementos de $B$. Para ese $k$ hay

$$
\binom rk\binom s{n-k}
$$

posibilidades.

Sumando sobre todos los valores efectivos de $k$,

$$
\boxed{
\sum_k
\binom rk\binom s{n-k}
=
\binom{r+s}{n}
}.
$$

Las clases son disjuntas y exhaustivas porque cada subconjunto de tamaño $n$ tiene un número único de elementos procedentes de $A$.


### 61

Aplicamos Vandermonde con $r=s=n$ y tamaño total elegido igual a $n$:

$$
\sum_{k=0}^{n}
\binom nk
\binom n{n-k}
=
\binom{2n}{n}.
$$

Por simetría,

$$
\binom n{n-k}=\binom nk.
$$

Entonces

$$
\boxed{
\sum_{k=0}^{n}\binom nk^2
=
\binom{2n}{n}
}.
$$


### 62

Por simetría,

$$
\binom sk=\binom s{s-k}.
$$

Entonces

$$
\sum_k\binom rk\binom sk
=
\sum_k\binom rk\binom s{s-k}.
$$

Vandermonde, con tamaño total elegido $s$, da

$$
\sum_k\binom rk\binom s{s-k}
=
\binom{r+s}{s}.
$$

Finalmente, por simetría,

$$
\binom{r+s}{s}
=
\binom{r+s}{r}.
$$

Así,

$$
\boxed{
\sum_k\binom rk\binom sk
=
\binom{r+s}{r}
}.
$$

El rango efectivo exige simultáneamente $0\le k\le r$ y $0\le k\le s$, por lo que

$$
\boxed{0\le k\le\min(r,s)}.
$$

## I. Multinomio elemental


### 63

El monomio $x^2yz^3$ tiene exponentes

$$
2+1+3=6,
$$

como corresponde a $(x+y+z)^6$.

Su coeficiente multinomial es

$$
\frac{6!}{2!1!3!}
=
\frac{720}{2\cdot1\cdot6}
=
60.
$$

Por tanto, el coeficiente es

$$
\boxed{60}.
$$


### 64

En $(x+y+z)^3$ cada término corresponde a repartir las tres posiciones entre $x,y,z$.

Los casos son:

- una sola variable aparece tres veces: coeficiente $1$;
- una variable aparece dos veces y otra una vez: coeficiente
  $3!/(2!1!)=3$;
- aparecen las tres variables una vez: coeficiente $3!=6$.

Por tanto,

$$
\boxed{
\begin{aligned}
(x+y+z)^3
&=x^3+y^3+z^3\\
&\quad+3x^2y+3x^2z+3xy^2+3xz^2+3y^2z+3yz^2\\
&\quad+6xyz.
\end{aligned}
}
$$

Por ejemplo, el coeficiente de $x^2y$ es $3$ porque debemos elegir cuál de las tres posiciones aporta $y$; las otras dos aportan $x$.


### 65

Debemos ordenar un multiconjunto con $3$ letras A, $2$ letras B y $2$ letras C. El número de palabras es

$$
\frac{7!}{3!2!2!}.
$$

Calculando,

$$
\frac{5040}{6\cdot2\cdot2}
=
\frac{5040}{24}
=
210.
$$

Por tanto,

$$
\boxed{210}.
$$


### 66

La expansión multinomial es

$$
(x+y+z)^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}x^ay^bz^c.
$$

Sustituyendo

$$
x=y=z=1,
$$

obtenemos

$$
(1+1+1)^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}.
$$

Por tanto,

$$
\boxed{
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}
=
3^n
}.
$$

El lado izquierdo es precisamente la suma de todos los coeficientes trinomiales de orden $n$.

## J. Diagnóstico y comparación de métodos


### 67

El error está en desarrollar

$$
n-(n-k).
$$

No es

$$
n-n-k,
$$

sino

$$
n-(n-k)=n-n+k=k.
$$

La prueba correcta es

$$
\begin{aligned}
\binom n{n-k}
&=
\frac{n!}{(n-k)![n-(n-k)]!}\\
&=
\frac{n!}{(n-k)!k!}\\
&=
\frac{n!}{k!(n-k)!}\\
&=
\binom nk.
\end{aligned}
$$

Así,

$$
\boxed{\binom n{n-k}=\binom nk}.
$$


### 68

La identidad escrita es, en general, falsa:

$$
\binom nk
\ne
\binom{n-1}{k}
+
\binom n{k-1}.
$$

Por ejemplo, con $n=5$ y $k=2$,

$$
\binom52=10,
$$

mientras que

$$
\binom42+\binom51
=
6+5
=11.
$$

Pascal exige que los dos términos del lado derecho tengan el mismo índice superior $n-1$ y posiciones inferiores consecutivas:

$$
\boxed{
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}
}.
$$

La semejanza visual de los términos no basta: deben coincidir exactamente con la estructura de la recurrencia.


### 69

En una expansión de $(x+y)^n$, todo monomio tiene grado total $n$. La fórmula propuesta tiene grado

$$
(n-k)+(n+k)=2n,
$$

Para $n\ge1$, este grado no es $n$ y refuta la fórmula general. Por ejemplo, con $n=1,k=0$ se propondría $xy$ en vez de $x$. Para $n=0,k=0$, ambas propuestas dan el término constante $1$; esa coincidencia aislada no demuestra la fórmula para todos los exponentes.

El término correcto es

$$
\boxed{
\binom nkx^{n-k}y^k
},
$$

pues sus exponentes satisfacen

$$
(n-k)+k=n.
$$


### 70

Una elección natural de método es la siguiente.

Para

$$
\binom nk=\binom n{n-k},
$$

el **doble conteo por complemento** es especialmente informativo: elegir $k$ elementos equivale a decidir cuáles $n-k$ quedan fuera. La prueba factorial también es corta, pero explica menos.

Para

$$
\sum_{k=0}^{n}\binom nk=2^n,
$$

la **sustitución en el teorema del binomio** con $x=y=1$ es inmediata:

$$
(1+1)^n=2^n.
$$

También existe una lectura combinatoria contando todos los subconjuntos.

Para

$$
\sum_k\binom rk\binom s{n-k}=\binom{r+s}{n},
$$

el **doble conteo** es el método más natural: se eligen $n$ elementos de una unión disjunta de bloques de tamaños $r$ y $s$, clasificando según cuántos provienen del primero.

La elección no es única; se justifica por la estructura que cada método hace visible.


### 71

En la prueba factorial de Pascal se parte de

$$
\binom{n-1}{k-1}
+
\binom{n-1}{k}
$$

y se transforman fracciones hasta obtener

$$
\binom nk.
$$

Los pasos son puramente algebraicos: expansión factorial, denominador común, suma y simplificación.

En la prueba combinatoria se cuenta el conjunto de subconjuntos de tamaño $k$ de un conjunto de $n$ elementos. Fijando un elemento $a$, esos subconjuntos se dividen en dos clases:

- los que contienen a $a$;
- los que no lo contienen.

Las cantidades respectivas son

$$
\binom{n-1}{k-1}
\quad\text{y}\quad
\binom{n-1}{k}.
$$

La estructura conceptual que sólo aparece claramente aquí es la **partición de un conjunto de elecciones en dos clases disjuntas y exhaustivas**. La prueba factorial verifica la igualdad; la combinatoria explica por qué hay una suma de esos dos términos.


### 72

La igualdad propuesta

$$
\sum_{k=0}^{n}a_k
=
\sum_{j=1}^{n+1}a_j
$$

es falsa en general porque las listas de términos son distintas. El lado izquierdo contiene

$$
a_0,a_1,\ldots,a_n,
$$

mientras que el derecho contiene

$$
a_1,a_2,\ldots,a_{n+1}.
$$

Si queremos hacer el cambio

$$
j=k+1,
$$

entonces

$$
k=j-1,
$$

y la igualdad correcta es

$$
\boxed{
\sum_{k=0}^{n}a_k
=
\sum_{j=1}^{n+1}a_{j-1}
}.
$$

En la prueba inductiva del binomio,

$$
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1}
$$

se convierte en

$$
\boxed{
\sum_{j=1}^{n+1}
\binom n{j-1}
x^{n+1-j}y^j
}.
$$

Cambian simultáneamente índice, límites y sumando.

## M. Problemas avanzados tipo prueba


### 73

Queremos demostrar

$$
\sum_{j=r}^{n}\binom jr
=
\binom{n+1}{r+1}.
$$

### a) Pascal y telescopaje

Pascal da

$$
\binom{j+1}{r+1}
=
\binom jr+\binom j{r+1}.
$$

Por tanto,

$$
\binom jr
=
\binom{j+1}{r+1}
-
\binom j{r+1}.
$$

Sustituyendo en la suma,

$$
\sum_{j=r}^{n}\binom jr
=
\sum_{j=r}^{n}
\left(
\binom{j+1}{r+1}
-
\binom j{r+1}
\right).
$$

Al expandir,

$$
\begin{aligned}
&\left(\binom{r+1}{r+1}-\binom r{r+1}\right)
+\left(\binom{r+2}{r+1}-\binom{r+1}{r+1}\right)\\
&\qquad+\cdots+
\left(\binom{n+1}{r+1}-\binom n{r+1}\right).
\end{aligned}
$$

Todos los términos interiores se cancelan. Como

$$
\binom r{r+1}=0,
$$

queda

$$
\sum_{j=r}^{n}\binom jr
=
\binom{n+1}{r+1}.
$$

### b) Doble conteo

Contemos los subconjuntos de tamaño $r+1$ de

$$
\{1,\ldots,n+1\}.
$$

Directamente hay

$$
\binom{n+1}{r+1}.
$$

Ahora los clasificamos por su máximo. Si el máximo es $j+1$, los otros $r$ elementos deben elegirse entre $\{1,\ldots,j\}$, lo que produce

$$
\binom jr
$$

subconjuntos.

Como $j$ recorre $r,\ldots,n$, el conteo por clases da

$$
\sum_{j=r}^{n}\binom jr.
$$

Ambos conteos se refieren al mismo conjunto, así que la identidad queda demostrada.

### Comparación

En la prueba telescópica, cada $\binom jr$ aparece como una **diferencia** entre dos entradas consecutivas de una columna diagonal de Pascal; la estructura visible es la cancelación.

En la prueba combinatoria, cada $\binom jr$ cuenta los subconjuntos cuyo máximo es exactamente $j+1$; la estructura visible es una partición por máximo.

La segunda prueba hace más transparente por qué la suma completa debe ser un único coeficiente binomial; la primera muestra cómo Pascal produce algebraicamente esa acumulación.


### 74

Sean $A$ y $B$ conjuntos disjuntos con

$$
|A|=r,\qquad |B|=s.
$$

Contemos los subconjuntos $T\subseteq A\cup B$ con

$$
|T|=n.
$$

Directamente hay

$$
\binom{r+s}{n}
$$

posibilidades.

Si fijamos

$$
k=|T\cap A|,
$$

entonces debemos elegir $k$ elementos de $A$ y $n-k$ de $B$. Para ese valor de $k$ hay

$$
\binom rk\binom s{n-k}
$$

elecciones.

Para que ambos coeficientes sean no nulos,

$$
0\le k\le r
$$

y

$$
0\le n-k\le s.
$$

La segunda condición equivale a

$$
n-s\le k\le n.
$$

Por tanto,

$$
\max(0,n-s)\le k\le\min(r,n).
$$

Las clases según $k$ son disjuntas y exhaustivas. Así,

$$
\boxed{
\sum_{k=\max(0,n-s)}^{\min(r,n)}
\binom rk\binom s{n-k}
=
\binom{r+s}{n}
}.
$$

### Corolario

Queremos transformar

$$
\sum_k\binom rk\binom sk.
$$

Por simetría,

$$
\binom sk=\binom s{s-k}.
$$

Entonces

$$
\sum_k\binom rk\binom sk
=
\sum_k\binom rk\binom s{s-k}.
$$

Aplicando Vandermonde con tamaño total elegido $s$,

$$
=
\binom{r+s}{s}
=
\binom{r+s}{r}.
$$

Por tanto,

$$
\boxed{
\sum_k\binom rk\binom sk
=
\binom{r+s}{r}
}.
$$

Aquí el rango efectivo es

$$
0\le k\le\min(r,s).
$$

Escribir simplemente $\sum_k$ es legítimo si previamente adoptamos la convención de que los coeficientes fuera de rango valen $0$; si no, hay que escribir explícitamente el intervalo efectivo.


### 75

Queremos demostrar, para $n\ge1$,

$$
\sum_{k=0}^{n}k\binom nk
=
n2^{n-1}.
$$

### Primera prueba: identidad local y reindexación

El término $k=0$ vale $0$, de modo que

$$
\sum_{k=0}^{n}k\binom nk
=
\sum_{k=1}^{n}k\binom nk.
$$

Usamos

$$
k\binom nk
=
n\binom{n-1}{k-1}:
$$

$$
\sum_{k=1}^{n}k\binom nk
=
n\sum_{k=1}^{n}\binom{n-1}{k-1}.
$$

Hacemos

$$
j=k-1.
$$

Entonces

$$
k=1\Rightarrow j=0,
\qquad
k=n\Rightarrow j=n-1,
$$

y

$$
n\sum_{k=1}^{n}\binom{n-1}{k-1}
=
n\sum_{j=0}^{n-1}\binom{n-1}{j}.
$$

La suma de la fila $n-1$ es $2^{n-1}$, por lo que

$$
\boxed{
\sum_{k=0}^{n}k\binom nk
=
n2^{n-1}
}.
$$

### Segunda prueba: pares $(A,a)$

Sea $N=\{1,\ldots,n\}$. Contemos los pares

$$
(A,a)
$$

donde $A\subseteq N$ y $a\in A$ está distinguido.

Si clasificamos por $|A|=k$, hay $\binom nk$ elecciones para $A$ y luego $k$ elecciones para $a$. Sumando:

$$
\sum_{k=0}^{n}k\binom nk.
$$

Alternativamente, elegimos primero el elemento distinguido $a$: hay $n$ opciones. Para cada uno de los otros $n-1$ elementos decidimos independientemente si pertenece o no a $A$, lo que da

$$
2^{n-1}
$$

posibilidades. Total:

$$
n2^{n-1}.
$$

### Comparación

La primera prueba transforma la suma mediante una identidad local y exhibe reindexación + suma de fila. La segunda identifica directamente el objeto global contado. Ambas explican el mismo factor $n$: en una aparece algebraicamente al extraerlo; en la otra corresponde a elegir primero el elemento distinguido.


### 76

Definamos

$$
S_m=
\sum_{k=0}^{m}(-1)^k\binom nk,
\qquad
0\le m<n.
$$

Aplicamos Pascal:

$$
\binom nk
=
\binom{n-1}{k-1}
+
\binom{n-1}{k}.
$$

Entonces

$$
S_m
=
\sum_{k=0}^{m}
(-1)^k\binom{n-1}{k-1}
+
\sum_{k=0}^{m}
(-1)^k\binom{n-1}{k}.
$$

En la primera suma, el término $k=0$ es

$$
\binom{n-1}{-1}=0.
$$

Por tanto,

$$
\sum_{k=0}^{m}
(-1)^k\binom{n-1}{k-1}
=
\sum_{k=1}^{m}
(-1)^k\binom{n-1}{k-1}.
$$

Reindexamos con

$$
j=k-1.
$$

Entonces $j=0,\ldots,m-1$ y

$$
(-1)^k=(-1)^{j+1}=-(-1)^j.
$$

Así,

$$
\sum_{k=1}^{m}
(-1)^k\binom{n-1}{k-1}
=
-
\sum_{j=0}^{m-1}
(-1)^j\binom{n-1}{j}.
$$

Por consiguiente,

$$
S_m
=
-
\sum_{j=0}^{m-1}
(-1)^j\binom{n-1}{j}
+
\sum_{k=0}^{m}
(-1)^k\binom{n-1}{k}.
$$

Renombrando el índice de la primera suma como $k$, los términos desde $k=0$ hasta $m-1$ se cancelan. Sólo queda el último término de la segunda suma:

$$
\boxed{
S_m
=
(-1)^m\binom{n-1}{m}
}.
$$

Es decir,

$$
\boxed{
\sum_{k=0}^{m}(-1)^k\binom nk
=
(-1)^m\binom{n-1}{m}
}.
$$

La hipótesis $m<n$ mantiene el resultado en el régimen de **suma parcial**, donde el término final $\binom{n-1}{m}$ está dentro del rango natural. Si se toma la fila completa $m=n$, la identidad relevante estudiada antes es

$$
\sum_{k=0}^{n}(-1)^k\binom nk=0.
$$


### 77

Queremos demostrar, para $0\le r\le k\le n$,

$$
\binom nk\binom kr
=
\binom nr\binom{n-r}{k-r}.
$$

### a) Prueba factorial

El lado izquierdo es

$$
\binom nk\binom kr
=
\frac{n!}{k!(n-k)!}
\frac{k!}{r!(k-r)!}.
$$

Cancelando $k!$,

$$
=
\frac{n!}{r!(k-r)!(n-k)!}.
$$

El lado derecho es

$$
\binom nr\binom{n-r}{k-r}
=
\frac{n!}{r!(n-r)!}
\frac{(n-r)!}{(k-r)!(n-k)!},
$$

que se simplifica a

$$
\frac{n!}{r!(k-r)!(n-k)!}.
$$

Por tanto, ambos lados son iguales.

### b) Doble conteo

Sea $N$ un conjunto con $n$ elementos. Contemos pares anidados

$$
R\subseteq K\subseteq N
$$

con

$$
|R|=r,\qquad |K|=k.
$$

**Primer orden de construcción.** Elegimos primero $K$: hay

$$
\binom nk
$$

opciones. Luego elegimos dentro de $K$ el subconjunto $R$ de tamaño $r$:

$$
\binom kr.
$$

Total:

$$
\binom nk\binom kr.
$$

**Segundo orden de construcción.** Elegimos primero $R$: hay

$$
\binom nr
$$

opciones. Para completar $K$, debemos elegir otros $k-r$ elementos entre los $n-r$ elementos de $N\setminus R$:

$$
\binom{n-r}{k-r}.
$$

Total:

$$
\binom nr\binom{n-r}{k-r}.
$$

Ambos métodos construyen exactamente los mismos pares $(R,K)$, de modo que

$$
\boxed{
\binom nk\binom kr
=
\binom nr\binom{n-r}{k-r}
}.
$$


### 78

Consideremos

$$
(x+y+z)^n
=
\underbrace{(x+y+z)\cdots(x+y+z)}_{n\text{ factores}}.
$$

### a) Coeficiente de $x^ay^bz^c$

Para obtener $x^ay^bz^c$, con

$$
a+b+c=n,
$$

debemos decidir qué factores aportan $x$, cuáles aportan $y$ y cuáles aportan $z$.

Primero elegimos los $a$ factores que aportan $x$:

$$
\binom na.
$$

De los $n-a$ restantes elegimos los $b$ que aportan $y$:

$$
\binom{n-a}{b}.
$$

Los restantes $c$ factores aportan $z$. Por tanto, el número de contribuciones es

$$
\binom na\binom{n-a}{b}.
$$

Factorialmente,

$$
\binom na\binom{n-a}{b}
=
\frac{n!}{a!(n-a)!}
\frac{(n-a)!}{b!c!}
=
\boxed{\frac{n!}{a!b!c!}}.
$$

### b) Interpretación como reparto de posiciones

Las $n$ posiciones de los factores se reparten en tres categorías:

- $a$ posiciones etiquetadas $x$;
- $b$ posiciones etiquetadas $y$;
- $c$ posiciones etiquetadas $z$.

El coeficiente multinomial cuenta exactamente esos repartos.

### c) Suma de coeficientes

La expansión completa es

$$
(x+y+z)^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}x^ay^bz^c.
$$

Tomando $x=y=z=1$,

$$
3^n
=
\sum_{\substack{a,b,c\ge0\\a+b+c=n}}
\frac{n!}{a!b!c!}.
$$

Así, la suma de todos los coeficientes trinomiales de orden $n$ es

$$
\boxed{3^n}.
$$


### 79

La supuesta prueba contiene varios errores distintos.

### 1. Primer producto distribuido: rangos y exponentes

Desde la hipótesis inductiva,

$$
(x+y)^n
=
\sum_{k=0}^{n}\binom nkx^{n-k}y^k,
$$

tenemos

$$
\begin{aligned}
(x+y)^{n+1}
&=
\sum_{k=0}^{n}\binom nkx^{n+1-k}y^k\\
&\quad+
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1}.
\end{aligned}
$$

En la propuesta, la primera suma aparece con rango $1\le k\le n+1$ sin una reindexación que lo justifique. Además, si se cambia el índice, deben cambiar también coeficiente y exponentes.

### 2. Reindexación correcta de la segunda suma

En

$$
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1},
$$

hacemos

$$
j=k+1.
$$

Entonces

$$
k=j-1,
$$

los límites pasan de $0,n$ a $1,n+1$, y el sumando se transforma en

$$
\binom n{j-1}x^{n+1-j}y^j.
$$

Por tanto,

$$
\sum_{k=0}^{n}\binom nkx^{n-k}y^{k+1}
=
\sum_{j=1}^{n+1}
\binom n{j-1}x^{n+1-j}y^j.
$$

Después podemos renombrar $j$ como $k$.

### 3. Los términos extremos no pueden combinarse como si ambas sumas tuvieran el mismo rango

Tras la reindexación correcta obtenemos

$$
\begin{aligned}
(x+y)^{n+1}
&=
\sum_{k=0}^{n}\binom nkx^{n+1-k}y^k\\
&\quad+
\sum_{k=1}^{n+1}\binom n{k-1}x^{n+1-k}y^k.
\end{aligned}
$$

El término $k=0$ aparece sólo en la primera suma:

$$
\binom n0x^{n+1}=x^{n+1}.
$$

El término $k=n+1$ aparece sólo en la segunda:

$$
\binom nny^{n+1}=y^{n+1}.
$$

Sólo en el rango interior $1\le k\le n$ se pueden sumar coeficientes.

### 4. Pascal fue aplicado al par equivocado

La propuesta usa

$$
\binom n{k-1}+\binom n{k+1},
$$

pero Pascal combina índices inferiores consecutivos:

$$
\binom n{k-1}+\binom nk
=
\binom{n+1}{k}.
$$

El término $\binom n{k+1}$ no pertenece al par correcto.

### 5. Reconstrucción correcta

La base $n=0$ es $1=\binom00$, con las potencias cero interpretadas como productos vacíos según [§13.8](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s08). Suponemos ahora la identidad para un $n\ge0$. La distribución y la reindexación ya justificadas producen las dos sumas de rangos $0,\ldots,n$ y $1,\ldots,n+1$.

En el rango interior,

$$
\binom nk+\binom n{k-1}
=
\binom{n+1}{k}.
$$

Por tanto,

$$
\begin{aligned}
(x+y)^{n+1}
&=
x^{n+1}
+
\sum_{k=1}^{n}
\binom{n+1}{k}x^{n+1-k}y^k
+
y^{n+1}\\
&=
\sum_{k=0}^{n+1}
\binom{n+1}{k}x^{n+1-k}y^k.
\end{aligned}
$$

Éste es exactamente el enunciado para $n+1$. La base y el paso inductivo demuestran la identidad para todos los enteros $n\ge0$. Si $n=0$ en el paso, la suma interior es vacía y los extremos dan $x+y$.

Los errores de la prueba defectuosa son, por tanto: cambiar rangos sin reindexar, no transformar simultáneamente índice/límites/sumando, perder los extremos, desajustar exponentes y aplicar Pascal a coeficientes que no forman el par requerido.


### 80

Queremos demostrar

$$
\sum_{k=0}^{n}\binom nk^2
=
\binom{2n}{n}.
$$

### a) Vandermonde + simetría

Vandermonde con $r=s=n$ y tamaño total elegido igual a $n$ da

$$
\sum_{k=0}^{n}
\binom nk
\binom n{n-k}
=
\binom{2n}{n}.
$$

Por simetría,

$$
\binom n{n-k}=\binom nk.
$$

Entonces

$$
\boxed{
\sum_{k=0}^{n}\binom nk^2
=
\binom{2n}{n}
}.
$$

El rango es exactamente $0\le k\le n$, pues ambos bloques tienen tamaño $n$ y estamos eligiendo $n$ elementos en total.

### b) Doble conteo directo

Dividamos un conjunto de $2n$ elementos en dos bloques disjuntos $A$ y $B$, cada uno con $n$ elementos.

Queremos contar los subconjuntos de tamaño $n$ del total. Directamente hay

$$
\binom{2n}{n}.
$$

Ahora clasificamos esos subconjuntos según el número $k$ de elementos que contienen de $A$. Si elegimos $k$ elementos de $A$, debemos elegir los otros $n-k$ de $B$. Para un $k$ fijo hay

$$
\binom nk\binom n{n-k}
$$

posibilidades.

Por simetría,

$$
\binom n{n-k}=\binom nk,
$$

así que la clase correspondiente a $k$ tiene

$$
\binom nk^2
$$

elementos.

Sumando para $k=0,\ldots,n$,

$$
\sum_{k=0}^{n}\binom nk^2
=
\binom{2n}{n}.
$$

### Comparación

La prueba con Vandermonde es compacta y muestra que la identidad es una especialización de una convolución general. La prueba de doble conteo expone directamente qué significa cada cuadrado $\binom nk^2$: una elección de $k$ elementos del primer bloque junto con una elección complementaria de $n-k$ elementos del segundo. La segunda hace más visible la estructura combinatoria; la primera sitúa la identidad dentro de una familia más amplia.

## N. Construcción, traducción y revisión de pruebas


### 81

Los objetos son subconjuntos $T\subseteq S$ con $|T|=k$ y $|T\cap D|$ par. Fijado ese valor $j$, las partes en $D$ y $S\setminus D$ tienen tamaños $j$ y $k-j$. Se eligen de $\binom mj\binom{n-m}{k-j}$ maneras; las dos partes son disjuntas y reconstruyen $T$ de manera única. Las restricciones dan $\max(0,k-n+m)\le j\le\min(m,k)$. Por tanto, la cantidad buscada es

$$
\boxed{\sum_{\substack{\max(0,k-n+m)\le j\le\min(m,k)\\j\text{ par}}}\binom mj\binom{n-m}{k-j}}.
$$

Cada objeto tiene un único $j$ par, así que las clases son disjuntas y exhaustivas dentro de la familia restringida. Si no hay ningún índice par viable, la suma es vacía y vale cero. Para $m=0$, $j=0$ y todos los $\binom nk$ subconjuntos son aptos. Para $m=1$, sólo sirve $j=0$: deben excluir al único elemento de $D$, y la cantidad es $\binom{n-1}{k}$, cero si $k=n$. Para $m=n$, necesariamente $j=k$: hay $\binom nk$ elecciones si $k$ es par y ninguna si es impar. Esto incluye $n=m=k=0$, con una elección vacía.

Si $m=2$, los únicos valores pares posibles son cero y dos. Usando coeficientes cero fuera de rango, la cantidad es $\binom{n-2}{k}+\binom{n-2}{k-2}$, pues $\binom20=\binom22=1$. Se eligen ninguno o ambos elementos de $D$. Aquí $n\ge2$, de modo que los índices superiores son no negativos. No se ha contado toda la familia de tamaño $k$: la restricción de paridad determina qué clases se pueden sumar.


### 82

Si el segundo elemento mayor es $j$, se incluye $j$, se eligen los $k-2$ elementos menores entre $1,\ldots,j-1$ y se elige exactamente un elemento mayor entre $j+1,\ldots,n$. Hay

$$
\binom{j-1}{k-2}(n-j)
$$

elecciones. La primera elección es posible si $j\ge k-1$; la segunda si $j\le n-1$. Cada conjunto de tamaño al menos dos tiene un único segundo elemento mayor, de modo que las clases son disjuntas y exhaustivas. Además, las tres partes reconstruyen el conjunto de forma única. Luego

$$
\boxed{\sum_{j=k-1}^{n-1}(n-j)\binom{j-1}{k-2}=\binom nk}.
$$

Para $n=5$, $k=3$, las clases $j=2,3,4$ aportan $3\cdot1$, $2\cdot2$, $1\cdot3$, respectivamente: $3+4+3=10=\binom53$. Clasificar por máximo fija el último elemento y deja todos los restantes debajo; aquí se fija el penúltimo y todavía se debe elegir el máximo, lo que explica el factor $n-j$. En $k=2$, el factor binomial es $\binom{j-1}{0}=1$, y en $k=n$ sólo queda $j=n-1$; ambos extremos dan la cuenta correcta.


### 83

Si $j$ es el primer ausente, los elementos $1,\ldots,j-1$ están presentes y $j$ no está. Los otros $k-j+1$ se eligen de $j+1,\ldots,n$, por lo que esa clase contiene $\binom{n-j}{k-j+1}$ objetos. Si los primeros $m$ están todos presentes, faltan $k-m$ elementos entre los $n-m$ restantes. La identidad es

$$
\boxed{\binom nk=\sum_{j=1}^{m}\binom{n-j}{k-j+1}+\binom{n-m}{k-m}}.
$$

Todos los índices superiores son no negativos. Los índices inferiores imposibles dan cero por la convención declarada. Una elección tiene exactamente un primer ausente o no tiene ninguno entre los primeros $m$; por ello las clases son disjuntas y exhaustivas. Sus elementos fijados y su parte libre reconstruyen la elección de modo único. Para $k=0$, sólo la clase $j=1$ contribuye $\binom{n-1}{0}=1$; todos los demás términos son cero. Las clases «$j$ está ausente» se solapan: el conjunto vacío pertenece a todas ellas si $m>1$. Exigir que sea el **primer** ausente elimina esa multiplicidad.


### 84

A una palabra le asociamos el conjunto de posiciones donde aparece $1$. Su inversa pone $1$ en las posiciones elegidas y $0$ en las demás, así que las palabras con $q$ unos son $\binom{r+s}{q}$. Partimos la palabra después de sus primeras $r$ posiciones. Si ese bloque contiene $j$ unos, el segundo contiene $q-j$. Hay $\binom rj\binom s{q-j}$ palabras, porque cada elección en los dos bloques determina exactamente una palabra por concatenación. Las clases son disjuntas y exhaustivas por el número único de unos del primer bloque. La viabilidad exige $0\le j\le r$ y $0\le q-j\le s$, que produce el rango indicado.

Para $(2,3,4)$, $j=1,2$ da $2\cdot1+1\cdot3=5=\binom54$. Un bloque de longitud cero tiene una única palabra, la palabra vacía, y contiene cero unos. Si ambos bloques son vacíos, necesariamente $q=0$ y ambos lados valen uno. La traducción mantiene las posiciones distintas aunque los símbolos se repitan.


### 85

Los objetos son ternas $(T,a,b)$ con $T\subseteq S$, $a,b\in T$ y $a\ne b$; los cargos dan orden al par $(a,b)$. Para $|T|=k$, hay $\binom nk$ equipos y $k(k-1)$ asignaciones de cargos. Si $k=0$ o $1$, no hay asignaciones y el término es cero. Sumando tamaños se obtiene el lado izquierdo.

Si elegimos primero a la presidencia y luego a la secretaría, hay $n(n-1)$ pares ordenados. Cada una de las otras $n-2$ personas puede pertenecer o no al equipo; hay $2^{n-2}$ posibilidades. Cada terna se construye exactamente una vez en ambos órdenes, de donde resulta la identidad. No se divide por dos: intercambiar los cargos produce un objeto distinto. Para $n=2$, el único equipo apto contiene ambas personas y admite dos asignaciones; la fórmula da $2\cdot1\cdot2^0=2$.

La identidad local correspondiente, para $2\le k\le n$, es $k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}$. Al reindexar $j=k-2$ en la suma de los términos aptos se recupera también la suma de la fila $n-2$.


### 86

Contamos pares $(R,T)$ de subconjuntos disjuntos de las $n$ posiciones, con $|R|=\ell$ y sin tamaño fijado para $T$. Si $|T|=k$, elegimos primero $T$ de $\binom nk$ maneras y luego $R$ entre las posiciones restantes, de $\binom{n-k}{\ell}$ maneras. Los valores posibles son $0\le k\le n-\ell$. Cada par pertenece a una única clase por $k$, y el orden de construcción no cambia el objeto.

Si elegimos primero $R$, hay $\binom n\ell$ elecciones. Las $n-\ell$ posiciones libres deciden independientemente si pertenecen a $T$, por lo que hay $2^{n-\ell}$ posibilidades. Ambos métodos son exhaustivos y no repiten pares; queda demostrada la identidad.

Si $\ell=0$, $R$ es vacío y la igualdad se reduce a $\sum_{k=0}^n\binom nk=2^n$. Si $\ell=n$, $R$ contiene todas las posiciones y $T$ debe ser vacío: el único término $k=0$ vale uno. Esto incluye $n=0$, donde existe exactamente el par de conjuntos vacíos.


### 87

La suma defectuosa vale $1+4+1=6$, mientras que $A\cup B=\{a,b,c\}$ tiene sólo $\binom32=3$ subconjuntos de tamaño dos. Una elección separada puede tomar $b$ en ambos grupos y producir la unión $\{b\}$, de tamaño uno. También puede producir el mismo subconjunto de varias maneras: $\{a,b\}$ resulta de tomar ambos elementos de $A$ o de tomar $a$ en $A$ y $b$ en $B$. Fallan tanto el tamaño como la unicidad.

Dividimos ahora la unión en $A\setminus B$, $A\cap B$ y $B\setminus A$, de tamaños $r-t$, $t$ y $s-t$. Aquí $0\le t\le\min(r,s)$. Para una elección de tamaño $q$, sean $i$ y $j$ las cantidades tomadas de las primeras dos partes; la tercera aporta $q-i-j$. Con coeficientes cero fuera de rango,

$$
\boxed{\binom{r+s-t}{q}=\sum_{i=0}^{r-t}\sum_{j=0}^{t}\binom{r-t}{i}\binom tj\binom{s-t}{q-i-j}}.
$$

Cada elección determina un único par $(i,j)$ y tres intersecciones; las partes disjuntas reconstruyen la elección de tamaño $q$. Así las clases son disjuntas y exhaustivas. En el ejemplo, las tres partes son unitarias y elegir dos de ellas da las tres elecciones correctas. No hemos corregido la fórmula cambiando sólo su lado derecho: se necesita reparar el objeto y su construcción.


### 88

Sea $S$ no vacío y fijemos $a\in S$. A un subconjunto $T$ le asociamos $T\setminus\{a\}$ si contiene $a$, y $T\cup\{a\}$ si no lo contiene. La transformación cambia el tamaño en uno, por lo que intercambia paridad. Al aplicarla dos veces recuperamos $T$; es una biyección entre los subconjuntos de tamaño par y los de tamaño impar. Como el total es $2^n$, cada familia tiene $2^{n-1}$ elementos.

Para $n=0$, $S$ es vacío y su único subconjunto es vacío, de tamaño par. Las cantidades son uno y cero. No existe un elemento $a$ cuya pertenencia se pueda cambiar; precisamente la elección inicial de $a$ deja de estar disponible. También la suma alternada vale $\binom00=1$, no cero. Por tanto, retirar $n\ge1$ cambia el resultado, además de invalidar la construcción. El argumento prueba la igualdad por una correspondencia concreta, en vez de deducirla únicamente por sustitución.


### 89

Para cada uno de los $2^n$ subconjuntos $T$ hay $n$ opciones de $a$, pertenezca o no a $T$. La nueva cantidad es $n2^n$. Clasificando por $|T|=k$, el peso correcto es $n$, de modo que la suma es $\sum_{k=0}^n n\binom nk=n2^n$.

En la clase $a\in T$, fijar $T$ da $k$ opciones; en la clase $a\notin T$ da $n-k$. Son clases disjuntas y exhaustivas porque cada elemento pertenece o no al subconjunto. Para contar cada clase también podemos elegir primero $a$: los otros $n-1$ elementos se deciden libremente, y la pertenencia del propio $a$ queda fijada. Cada clase tiene $n2^{n-1}$ pares. Por tanto,

$$
\sum_{k=0}^n k\binom nk+\sum_{k=0}^n(n-k)\binom nk=n2^n.
$$

Conservar el peso $k$ seguiría contando sólo la primera clase y perdería todos los pares con $a$ fuera de $T$. Para $n=1$, los nuevos pares son $(\varnothing,a)$ y $(\{a\},a)$; el conteo antiguo sólo incluía el segundo. Si se examina aparte $n=0$, no hay pares de ninguna clase: esta conclusión directa no requiere una fórmula que use una fila de índice superior $-1$.


### 90

Tomamos bloques disjuntos $R,S,T$ de tamaños $r,s,t$. Los objetos son subconjuntos de tamaño $q$ de su unión. Fijar las cantidades $i$ en $R$ y $j$ en $S$ obliga a tomar $q-i-j$ en $T$. Las elecciones en los tres bloques se multiplican porque sus intersecciones reconstruyen el subconjunto de manera única. Las clases por $(i,j)$ son disjuntas y exhaustivas. Las cantidades imposibles dan cero; sumando las clases obtenemos la identidad.

Para la otra prueba, fijamos $i$. Si $u=q-i$ satisface $0\le u\le s+t$, Vandermonde da

$$
\sum_{j=0}^{s}\binom sj\binom t{u-j}=\binom{s+t}{u}.
$$

Si $u<0$ o $u>s+t$, todos los productos son cero y el lado derecho también lo es: la igualdad interior sigue siendo válida por la convención. Así la doble suma se reduce a $\sum_{i=0}^r\binom ri\binom{s+t}{q-i}=\binom{r+s+t}{q}$, por Vandermonde aplicado a tamaños $r$ y $s+t$.

La prueba directa obtiene la generalidad de la reconstrucción para tamaños arbitrarios, sin depender de ejemplos numéricos. La prueba sucesiva la obtiene de las hipótesis de Vandermonde y de la comprobación explícita de los valores imposibles de $u$. Si algún bloque es vacío, su única elección es el subconjunto vacío; el coeficiente correspondiente sólo contribuye en índice cero. Ambas pruebas lo incluyen. Para $r=s=t=q=0$, hay un único subconjunto vacío y ambos lados valen uno.


### 91

Directamente, $W_0=0$ y $W_1=-1$. Para $n\ge2$, la identidad local $k\binom nk=n\binom{n-1}{k-1}$, aplicada desde $k=1$, permite escribir

$$
W_n=n\sum_{k=1}^{n}(-1)^k\binom{n-1}{k-1}
=-n\sum_{j=0}^{n-1}(-1)^j\binom{n-1}{j}=0.
$$

En la reindexación $j=k-1$ cambian los límites a $0,n-1$ y el signo a $(-1)^{j+1}=-(-1)^j$. La última suma vale cero porque $n-1\ge1$. Para $n=1$ esa suma vale uno, lo que también produce $-1$.

En la prueba por emparejamiento, asignamos a cada par $(T,a)$ el signo $(-1)^{|T|}$. Tomamos $S=\{1,\ldots,n\}$ y, para cada $a$, fijamos $b_a$ como el menor elemento de $S\setminus\{a\}$. Existe porque $n\ge2$ y depende sólo de $a$. Cambiar la pertenencia de $b_a$ en $T$ mantiene $a\in T$, cambia la paridad y, al repetirse, recupera el mismo par. No hay pares fijos, de modo que los signos se cancelan dos a dos. La suma de signos por tamaños es exactamente $W_n$.

La prueba algebraica hace visible el signo perdido al desplazar el índice y utiliza la fila $n-1$. La prueba por pares explica la cancelación y por qué debe existir un segundo elemento. Para $n=1$, no hay tal elemento y queda el único par de signo negativo; para $n=0$, no hay pares. El resultado completo es $W_n=-1$ si $n=1$ y $W_n=0$ en los demás casos.


### 92

Sustituir $x=1$ e $y=2$ en el teorema del binomio da directamente

$$
(1+2)^n=\sum_{k=0}^{n}\binom nk1^{n-k}2^k=\sum_{k=0}^{n}2^k\binom nk.
$$

Para la prueba de conteo, llamemos a las etiquetas A, B y C. Hay $3^n$ asignaciones porque cada posición decide independientemente una de tres etiquetas. Si exactamente $k$ posiciones tienen etiqueta distinta de A, se eligen esas posiciones de $\binom nk$ maneras y cada una decide entre B y C, dando $2^k$ opciones. Las restantes están obligadas a recibir A. Cada asignación determina un único conjunto de posiciones distintas de A y sus etiquetas; la reconstrucción es única. Las clases por $k$ son exhaustivas y disjuntas, por lo que su suma cuenta todas las asignaciones.

La prueba por sustitución hereda la generalidad del teorema demostrado para todo entero no negativo. La prueba de conteo la establece directamente con elecciones independientes y una partición válida para un número arbitrario de posiciones. Unos pocos ejemplos numéricos no reemplazan ninguno de esos pasos. Si $n=0$, hay una única asignación vacía y la suma contiene el término $2^0\binom00=1=3^0$.

***

***

[← Capítulo 12](algebra-para-matematicos-capitulo-12-sumas-productos-e-identidades-finitas.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 14 →](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md)

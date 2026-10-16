---
content-id: MA-BCH-0250
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-012
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
title: Capítulo 12 — Qué hace una función
date-modified: '2026-10-16'
provenance:
  type: original
  sources:
  - ANM-C12.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-12)

Al elevar al cuadrado, las entradas $-2$ y $2$ llegan a la misma salida $4$. Si sólo conocemos ese resultado, hemos perdido la posibilidad de reconocer cuál de las dos entradas se utilizó. Pero la regla también deja salidas sin alcanzar: ningún real tiene cuadrado negativo. Para describir ambas cosas necesitamos saber dónde se permiten las entradas y dónde se declaran las salidas; la expresión $x^2$ por sí sola no contiene esos datos.

Las sucesiones que hemos estudiado son funciones cuyo dominio es el conjunto de los naturales. Al admitir otros dominios podremos transportar intervalos, seleccionar entradas por sus salidas y encadenar transformaciones. Las bolas y vecindades de C04 servirán para medir conjuntos de entradas próximos a un punto. Las preguntas iniciales son algebraicas y conjuntistas: qué se alcanza, qué se identifica y qué puede deshacerse, antes de introducir límites de funciones o continuidad.

## 12.1. Una función tiene un tipo

[]{#MA-SEC-ANM-01-012-001}

Consideremos dos maneras de declarar la regla del cuadrado:

$$
f:\mathbb R\to\mathbb R,\quad f(x)=x^2,
\qquad g:[0,\infty)\to[0,\infty),\quad g(x)=x^2.
$$

En ambas podemos introducir $2$ y obtener $4$, pero $-2$ sólo está admitido en la primera. También difieren los conjuntos declarados de salidas. La coincidencia de algunos cálculos no identifica esos objetos: cada evaluación debe hacerse dentro del dominio de la función que estamos utilizando.

Una función $f:D\to E$ consta de un dominio $D$, un codominio $E$ y una asignación que a cada $x\in D$ hace corresponder exactamente un $f(x)\in E$. «Cada» impide dejar entradas sin salida; «exactamente un» impide asignar dos salidas distintas a una misma entrada. No impide que entradas distintas compartan salida.

Su **grafo** es el conjunto

$$
G_f=\{(x,f(x)):x\in D\}\subseteq D\times E.
$$

Adoptamos la convención tipada: dos funciones son iguales cuando sus dominios, sus codominios y sus asignaciones coinciden. El grafo registra todas las evaluaciones, pero puede dejar invisible una parte del codominio. Por ejemplo, las aplicaciones $\mathbb R\to\mathbb R$ y $\mathbb R\to[0,\infty)$ dadas por $x^2$ tienen los mismos pares $(x,x^2)$. La primera declara además las salidas negativas, aunque no las alcance; la segunda declara únicamente salidas que sí alcanza. Bajo nuestra convención son funciones distintas, y esa diferencia será decisiva al pedir una inversa.

La unicidad de la definición se comprueba después de fijar una entrada. Si se permiten simultáneamente los dos valores $\pm\sqrt x$ para $x>0$, esa entrada recibe dos salidas y la regla no define una función real. En $f(x)=x^2$, en cambio, tanto $2$ como $-2$ reciben una sola salida, aunque sea la misma. La propiedad de impedir esa coincidencia entre entradas distintas se llama inyectividad; no forma parte de la definición de función.

La notación también distingue niveles: $f$ es la asignación completa, $f(2)=4$ es un valor cuando $2$ pertenece al dominio y $G_f$ es un conjunto de pares. La gráfica cartesiana representa ese conjunto cuando dominio y codominio están en $\mathbb R$. Una tabla o un dibujo de flechas pueden mostrar las mismas evaluaciones desde otra perspectiva, pero una tabla parcial deja abiertas las entradas que no aparecen en ella.

Si fijamos el mismo tipo $f,g:D\to E$, la igualdad se prueba comparando $f(x)$ y $g(x)$ para toda entrada $x\in D$. Cada par de un grafo pertenecerá entonces al otro; recíprocamente, si los grafos coinciden, el par $(x,f(x))$ también pertenece al de $g$ y su salida única obliga a $f(x)=g(x)$. Tres evaluaciones sólo prueban tres igualdades. Si las entradas observadas son $r_1,r_2,r_3$, las funciones reales $f(x)=0$ y $g(x)=(x-r_1)(x-r_2)(x-r_3)$ coinciden en ellas y difieren en cualquier real distinto de las tres.

Para una sucesión $a:\mathbb N\to\mathbb R$, $a_n=n^2$, el grafo contiene $(0,0),(1,1),(2,4),\ldots$. La entrada $1/2$ no está autorizada y el par $(1/2,1/4)$ no pertenece a ese grafo. Sí pertenece al de la función real $x\mapsto x^2$. Una curva que una los puntos de la sucesión puede ayudar a compararlos, pero añade evaluaciones de otra función; no amplía el dominio original.

El dominio también impide evaluar fórmulas en entradas prohibidas. Para $h:\mathbb R\setminus\{0\}\to\mathbb R$, $h(x)=1/x$, la expresión $h(0)$ no designa un valor. Asignar un número en cero supondría construir otra función, con nuevo dominio y una regla adicional en esa entrada. La función ya declarada no se modifica al escribir una evaluación que su tipo excluye.

El dibujo de flechas del cuadrado en un dominio finito permite ver las dos cuestiones que estudiaremos: hay salidas compartidas y hay salidas declaradas sin entrada. Para pasar de unas pocas evaluaciones a conjuntos enteros, necesitamos definir con precisión qué significa reunir todas las salidas o seleccionar todas las entradas que cumplen una condición.

![En el dominio finito {-2,0,2}, el cuadrado asigna una salida a cada entrada; dos entradas comparten 4 y el codominio {-1,0,4} contiene una salida no alcanzada.](../../assets/books/anm/C12/C12-F01.svg){#fig-anm-c12-f01 fig-alt="Dos conjuntos finitos: las entradas menos dos y dos apuntan ambas a cuatro, cero apunta a cero y la salida menos uno no recibe flecha."}

### Ejercicios de la sección 12.1

[]{#ejercicios-12}

#### Ejercicio 1. La misma regla, tres objetos

[]{#MA-EX-ANM-01-012-001}

Compara $f:\mathbb R\to\mathbb R$, $g:[0,\infty)\to\mathbb R$ y $h:[0,\infty)\to[0,\infty)$, todas dadas por $x^2$. Determina cuáles tienen el mismo grafo y cuáles son iguales como funciones tipadas.

[]{#MA-SOL-ANM-01-012-001}

<details class="anm-solution">
<summary>Ver solución del ejercicio 1</summary>

$g$ y $h$ tienen exactamente los pares $(x,x^2)$ con $x\ge0$, luego el mismo grafo. Sus codominios difieren, así que no son iguales. El grafo de $f$ contiene además, por ejemplo, $(-1,1)$, ausente de los otros dos. $f$ tiene distinto dominio de $g$ y $h$. Ningún par es igual como función tipada. Todas coinciden numéricamente en entradas no negativas.

Conviene comparar los datos uno por uno. Las funciones $g$ y $h$ tienen el mismo dominio y los mismos valores, por lo que sus grafos coinciden, pero sus codominios no. La función $f$ tiene otro dominio y admite pares con primera coordenada negativa. La igualdad numérica $f(x)=g(x)=h(x)$ para $x\ge0$ sólo compara evaluaciones compartidas. Bajo la convención tipada del capítulo, ninguna pareja coincide en los tres datos necesarios para ser el mismo objeto.

</details>

#### Ejercicio 2. Una relación que debe repararse

[]{#MA-EX-ANM-01-012-002}

En $D=\{0,1,2\}$ y $E=\{0,1,4\}$ considera $R=\{(0,0),(1,1),(1,4)\}$. Explica por qué no es el grafo de una función $D\to E$ y construye una reparación eliminando un par y añadiendo otro.

[]{#MA-SOL-ANM-01-012-002}

<details class="anm-solution">
<summary>Ver solución del ejercicio 2</summary>

La entrada $1$ tiene dos salidas distintas y la entrada $2$ no tiene ninguna. Eliminamos $(1,4)$ y añadimos $(2,4)$; quedan $(0,0),(1,1),(2,4)$. Cada entrada de $D$ tiene exactamente una salida en $E$. Sólo borrar o sólo añadir no repararía las dos deficiencias.

Hay dos fallos independientes: falta existencia de salida para la entrada dos y falta unicidad para la entrada uno. Eliminar $(1,4)$ deja una sola salida para uno; añadir $(2,4)$ proporciona la salida ausente. La relación reparada es $\{(0,0),(1,1),(2,4)\}$. Verificar que cada primera coordenada de $D$ aparece una vez acredita ambas condiciones. También hay otras reparaciones posibles; no se exige que la nueva función sea sobreyectiva.

</details>

#### Ejercicio 3. Ninguna tabla finita decide toda la función

[]{#MA-EX-ANM-01-012-003}

Dado un conjunto finito $A\subseteq\mathbb R$, construye dos funciones distintas $\mathbb R\to\mathbb R$ que coincidan en todas las entradas de $A$.

[]{#MA-SOL-ANM-01-012-003}

<details class="anm-solution">
<summary>Ver solución del ejercicio 3</summary>

Como $A$ es finito y $\mathbb R$ infinito, existe $t\in\mathbb R\setminus A$. Por ejemplo, si $A$ no es vacío, $t=1+\sum_{a\in A}|a|$ supera todo elemento de $A$; si es vacío, sirve $t=0$. Definimos $f(x)=0$ para todo real y $g(x)=1$ cuando $x=t$, $g(x)=0$ en otro caso. Son funciones del mismo tipo, coinciden en $A$ y difieren en $t$. La tabla de $A$ no determina sus valores restantes.

La elección explícita de $t$ evita depender de una tabla concreta. Si $A$ no es vacío, cada $a\in A$ satisface $a\le|a|\le\sum_{z\in A}|z|<t$, por lo que $t$ está fuera de $A$. Las funciones construidas asignan una salida única a cada real y tienen el mismo tipo. Para toda entrada observada ambas valen cero, pero en $t$ valen cero y uno. Incluso una tabla con muchísimas entradas finitas deja sin determinar otras evaluaciones.

</details>

#### Ejercicio 4. Identidad extensional

[]{#MA-EX-ANM-01-012-004}

Prueba que para $f,g:D\to E$ la igualdad $G_f=G_g$ equivale a $f(x)=g(x)$ para todo $x\in D$. Explica por qué deben fijarse los tipos para concluir $f=g$.

[]{#MA-SOL-ANM-01-012-004}

<details class="anm-solution">
<summary>Ver solución del ejercicio 4</summary>

Si los grafos coinciden, $(x,f(x))\in G_g$, de modo que por unicidad de salida de $g$, $f(x)=g(x)$. Recíprocamente, igualdad de valores para toda entrada hace que cada par $(x,f(x))$ sea $(x,g(x))$ y viceversa; los grafos coinciden. Con dominio y codominio iguales, la convención tipada da $f=g$. Con codominios diferentes, la igualdad de grafos no basta, como muestran las dos versiones del cuadrado.

Para deducir igualdad de valores desde igualdad de grafos, el par $(x,f(x))$ debe aparecer también en el grafo de $g$. Como su primera coordenada es la misma entrada $x$ y $g$ tiene salida única, su segunda coordenada sólo puede ser $g(x)$. La dirección contraria compara cada par en ambos sentidos. El grafo no registra elementos del codominio que nunca se alcanzan; por eso hay que fijar también los codominios para concluir igualdad de objetos tipados.

</details>

#### Ejercicio 5. Discreto frente a real

[]{#MA-EX-ANM-01-012-005}

Para $a:\mathbb N\to\mathbb R$, $a_n=2n+1$, y $f:\mathbb R\to\mathbb R$, $f(x)=2x+1$, determina la relación entre sus grafos. ¿Es la sucesión una recta?

[]{#MA-SOL-ANM-01-012-005}

<details class="anm-solution">
<summary>Ver solución del ejercicio 5</summary>

$G_a=\{(n,2n+1):n\in\mathbb N\}\subsetneq G_f$. La inclusión es estricta porque $(1/2,2)$ pertenece a $G_f$ y no a $G_a$. La sucesión tiene dominio $\mathbb N=\{0,1,\ldots\}$ y grafo discreto; la recta representa el grafo de $f$. El mismo cálculo en entradas naturales no identifica los dos objetos.

Cada índice natural también es real, y ambas asignaciones producen $2n+1$ allí; esto prueba la inclusión de grafos. La entrada $1/2$ demuestra que la inclusión es propia. Un dibujo que una los puntos de la sucesión añade evaluaciones para entradas que no pertenecen a $\mathbb N$. Esos puntos intermedios forman parte del grafo de la función real, no del grafo de la sucesión. La expresión algebraica compartida no elimina la diferencia de dominios.

</details>

## 12.2. Imagen: transportar un conjunto

[]{#MA-SEC-ANM-01-012-002}

Si introducimos un conjunto $A$ de entradas permitidas, podemos reunir las salidas que produce alguna de ellas. Para $f:D\to E$ y $A\subseteq D$, la **imagen directa** es

$$
f[A]=\{y\in E:\text{existe }x\in A\text{ con }f(x)=y\}.
$$

Los corchetes distinguen una operación sobre conjuntos de la evaluación en un elemento. Por ejemplo, $f(2)$ es una salida, mientras $f[\{2\}]=\{f(2)\}$ es el conjunto que contiene esa salida. La imagen total $f[D]$ está contenida en el codominio $E$, pero puede dejar fuera elementos declarados: una cosa es permitir una salida y otra encontrar una entrada que la produzca.

Pertenecer a $f[A]$ exige un testigo: una entrada $x\in A$ con $f(x)=y$. Resolver la ecuación sólo cumple una parte de la tarea; el testigo debe estar en el conjunto de entradas considerado. Para determinar exactamente una imagen probamos dos inclusiones: que toda salida producida está en el conjunto anunciado y que cada elemento de ese conjunto se produce realmente.

Sea $q:\mathbb R\to\mathbb R$, $q(x)=x^2$, y $A=[-2,1]$. Afirmamos $q[A]=[0,4]$. Si $x\in A$, entonces $|x|\le2$ y $0\le x^2\le4$, de modo que $q[A]\subseteq[0,4]$. Recíprocamente, para $y\in[0,4]$, la raíz real no negativa $\sqrt y$ existe y satisface $0\le\sqrt y\le2$. La entrada $x=-\sqrt y$ está en $[-2,0]\subseteq A$ y $x^2=y$. Por tanto $[0,4]\subseteq q[A]$. La existencia y unicidad de la raíz no negativa se acreditaron en §10.7; no las deducimos de un teorema posterior sobre funciones.

La elección de la raíz negativa conserva el testigo dentro de $A$. La candidata positiva $\sqrt4=2$ quedaría fuera de $[-2,1]$, mientras que $-\sqrt4=-2$ sí pertenece. La misma ecuación puede tener varias soluciones reales y sólo algunas ser entradas admitidas en el problema. Ese recorte explica por qué la imagen depende del conjunto de partida.

![El cuadrado transporta \[-2,1\] a \[0,4\]. Seleccionar las salidas (1,4\] recupera dos ramas: \[-2,-1) y (1,2\]. Imagen y preimagen responden preguntas distintas.](../../assets/books/anm/C12/C12-F02.svg){#fig-anm-c12-f02 fig-alt="Dos paneles del cuadrado: [-2,1] tiene imagen [0,4]; la banda de salidas (1,4] selecciona [-2,-1) y (1,2]. Extremos abiertos y cerrados diferenciados."}

En $A=\{-2,-1,1,2\}$, las cuatro evaluaciones del cuadrado sólo producen $q[A]=\{1,4\}$. Todo valor de la imagen está en esa lista y ambos se alcanzan, por ejemplo en $-1$ y $-2$. Los conjuntos no conservan multiplicidades: que $1$ tenga dos entradas no crea dos elementos llamados uno. La pérdida de información aparece al reunir las salidas.

La operación de imagen conserva inclusiones: si $A\subseteq C\subseteq D$ y $y\in f[A]$, un testigo $x\in A$ también pertenece a $C$, de modo que $y\in f[C]$. Es una monotonía respecto del orden de inclusión entre conjuntos. No requiere que $f$ preserve el orden numérico: el cuadrado cumple esta propiedad aunque no sea creciente en toda la recta.

Además,

$$
f[\varnothing]=\varnothing,\qquad f[\{x\}]=\{f(x)\}.
$$

En el vacío no hay entradas que puedan servir de testigo, por lo que su imagen es vacía. En $\{x\}$ sólo está permitida la entrada $x$, que alcanza exactamente $f(x)$. Estas afirmaciones incluyen el dominio vacío: la asignación vacía $\varnothing\to E$ es una función y su imagen es vacía para cualquier $E$.

Los extremos de un intervalo tampoco bastan para transportar sus puntos. Si intentáramos escribir $q[(-2,2)]=(q(-2),q(2))$, obtendríamos $(4,4)=\varnothing$, aunque cero está en la imagen. Las entradas extremas ni siquiera pertenecen a ese intervalo. El cálculo correcto es $[0,4)$: de $-2<x<2$ se sigue $0\le x^2<4$, y para cada $0\le y<4$ la entrada $\sqrt y\in[0,2)\subset(-2,2)$ alcanza $y$. Cero se incluye porque se alcanza; cuatro se excluye porque sus únicas entradas son $\pm2$, ambas prohibidas.

### Ejercicios de la sección 12.2

#### Ejercicio 6. Imagen exacta de un intervalo

[]{#MA-EX-ANM-01-012-006}

Calcula la imagen de $[-3,2)$ por $q:\mathbb R\to\mathbb R$, $q(x)=x^2$, probando ambas inclusiones.

[]{#MA-SOL-ANM-01-012-006}

<details class="anm-solution">
<summary>Ver solución del ejercicio 6</summary>

La imagen es $[0,9]$. Toda entrada tiene $|x|\le3$, así que su cuadrado está en ese intervalo. Para $0\le y\le9$, la entrada $x=-\sqrt y\in[-3,0]\subseteq[-3,2)$ alcanza $y$. En particular $9$ se alcanza en $-3$, aunque $3$ no esté disponible; y cero se alcanza en cero.

La inclusión hacia $[0,9]$ usa que toda entrada del intervalo tiene magnitud a lo sumo tres. Para la vuelta, elegimos la raíz negativa, no la positiva: $-\sqrt y$ está siempre entre menos tres y cero, incluso para salidas mayores o iguales que cuatro. Así evita el extremo dos excluido del dominio. Nueve sí se alcanza gracias al extremo menos tres incluido. Calcular la imagen exige considerar todas las ramas disponibles, no transportar sólo los dos extremos por orden.

</details>

#### Ejercicio 7. Unión con dos piezas

[]{#MA-EX-ANM-01-012-007}

Calcula $q[[-2,-1]\cup(0,1)]$ para el cuadrado real. Justifica extremos y huecos.

[]{#MA-SOL-ANM-01-012-007}

<details class="anm-solution">
<summary>Ver solución del ejercicio 7</summary>

La primera pieza tiene imagen $[1,4]$: sus cuadrados están allí y $-\sqrt y$ alcanza cada $y$ de ese intervalo. La segunda tiene imagen $(0,1)$, con testigo $\sqrt y$. Por tanto la imagen de la unión es $(0,4]$. El valor $1$ sí se alcanza en $-1$, cero no se alcanza porque ninguna entrada es cero, y $4$ sí se alcanza en $-2$.

La unión de imágenes es $[1,4]\cup(0,1)=(0,4]$. No queda un hueco en uno, porque la rama negativa lo incluye aunque la positiva lo excluya. Cero queda fuera porque las dos piezas excluyen la entrada cero; cuatro queda dentro porque menos dos pertenece al dominio seleccionado. Para cualquier salida intermedia elegimos una raíz en la pieza adecuada. Esta comprobación de testigos explica por qué los extremos de cada pieza pueden compensarse al reunir las imágenes.

</details>

#### Ejercicio 8. Imagen y cardinalidad finita

[]{#MA-EX-ANM-01-012-008}

Si $A\subseteq D$ es finito y $f:D\to E$, prueba que $|f[A]|\le|A|$ y que hay igualdad si y sólo si $f|_A$ es inyectiva.

[]{#MA-SOL-ANM-01-012-008}

<details class="anm-solution">
<summary>Ver solución del ejercicio 8</summary>

Enumeramos $A=\{a_1,\ldots,a_n\}$ con entradas distintas. Su imagen consta de los $n$ valores listados, eliminando repeticiones, por lo que tiene a lo sumo $n$ elementos. Si la restricción es inyectiva, todos son distintos y hay $n$. Si no lo es, dos valores de la lista coinciden, y tras eliminar esa repetición quedan a lo sumo $n-1$. Para $A=\varnothing$, ambas cardinalidades son cero y la restricción es inyectiva de manera vacua.

La lista de salidas tiene tantos lugares como entradas, pero varios lugares pueden contener el mismo valor. El conjunto imagen elimina esas repeticiones. Si existe una colisión entre dos entradas distintas, al menos un lugar de la lista no aporta un elemento nuevo y la cardinalidad baja. Si no hay colisiones, cada entrada aporta un elemento distinto y las cardinalidades coinciden. La afirmación trata la inyectividad de la restricción a $A$, no exige inyectividad en todo $D$.

</details>

#### Ejercicio 9. La inclusión no estudia el orden

[]{#MA-EX-ANM-01-012-009}

Construye una función real que no sea no decreciente ni no creciente y demuestra que su operación de imagen conserva inclusiones de conjuntos.

[]{#MA-SOL-ANM-01-012-009}

<details class="anm-solution">
<summary>Ver solución del ejercicio 9</summary>

Sirve $q(x)=x^2$. No es no decreciente porque $-2<-1$ pero $4>1$; no es no creciente porque $1<2$ pero $1<4$. Sin embargo, para $A\subseteq C$, cada salida de $q[A]$ tiene testigo $x\in A\subseteq C$, luego pertenece a $q[C]$. Son propiedades distintas: inclusión de conjuntos frente a comparación de valores.

Los dos pares elegidos refutan por separado los dos sentidos de monotonía. Después, para cualquier inclusión de conjuntos $A\subseteq C$, la prueba de inclusión de imágenes sólo reutiliza el testigo de cada salida. No compara qué entrada es mayor ni cómo se ordenan sus salidas. La operación $A\mapsto f[A]$ conserva el orden dado por inclusión para cualquier función, aunque $x\mapsto f(x)$ no conserve ninguno de los órdenes numéricos de la recta.

</details>

#### Ejercicio 10. Imagen de una diferencia

[]{#MA-EX-ANM-01-012-010}

Prueba $f[A]\setminus f[C]\subseteq f[A\setminus C]$ para $A,C\subseteq D$ y da un ejemplo en que la inclusión sea estricta.

[]{#MA-SOL-ANM-01-012-010}

<details class="anm-solution">
<summary>Ver solución del ejercicio 10</summary>

Si $y\in f[A]\setminus f[C]$, existe $a\in A$ con $f(a)=y$. Ese $a$ no puede estar en $C$, pues entonces $y\in f[C]$. Así $a\in A\setminus C$, que prueba la inclusión. Para $q(x)=x^2$, $A=\{-1,1\}$ y $C=\{1\}$, el lado izquierdo es vacío y el derecho es $q[\{-1\}]=\{1\}$. Una entrada fuera de $C$ puede compartir salida con otra dentro de $C$.

La condición $y\notin f[C]$ impide que cualquier testigo de esa salida pertenezca a $C$. Por eso un testigo en $A$ debe estar fuera de $C$. La vuelta puede fallar: una entrada fuera de $C$ puede compartir su salida con otra dentro de $C$. En el ejemplo, menos uno está en $A\setminus C$, pero su salida uno también es producida por la entrada uno de $C$, y se elimina al restar los conjuntos de salidas.

</details>

## 12.3. Preimagen: seleccionar por la salida

[]{#MA-SEC-ANM-01-012-003}

Podemos invertir la pregunta sin intentar invertir la función. En lugar de dar entradas y reunir salidas, fijemos un conjunto de salidas aceptables $B\subseteq E$ y conservemos las entradas que llegan a él. Para $f:D\to E$, la **preimagen** es

$$
f^{-1}[B]=\{x\in D:f(x)\in B\}.
$$

El resultado vive en $D$. Para decidir si una entrada pertenece, la evaluamos y comprobamos si su salida está en $B$. Este procedimiento funciona aunque una salida tenga varias entradas o ninguna. La notación $f^{-1}[B]$ nombra una selección de entradas y no supone todavía la existencia de una función inversa.

La preimagen $f^{-1}[\{y\}]$ se llama **fibra sobre $y$**. Para $q:\mathbb R\to\mathbb R$, $q(x)=x^2$,

$$
q^{-1}[\{4\}]=\{-2,2\},\qquad
q^{-1}[\{0\}]=\{0\},\qquad
q^{-1}[\{-1\}]=\varnothing.
$$

La fibra sobre cuatro tiene dos entradas: $x^2=4$ equivale a $(x-2)(x+2)=0$, así que sólo pueden ser $-2$ y $2$, y ambas sirven. Sobre cero sólo está cero; sobre menos uno no hay entrada porque todo cuadrado real es no negativo. Son tres resultados compatibles con una función: cada entrada conserva una única salida. Escribir $q^{-1}(4)$ como evaluación de una inversa, en cambio, no está autorizado para $q:\mathbb R\to\mathbb R$, que no es biyectiva.

Las fibras sobre salidas diferentes son disjuntas. Una entrada común a las fibras de $y$ y $z$ cumpliría simultáneamente $f(x)=y$ y $f(x)=z$; la unicidad de su salida obliga a $y=z$. Las fibras sobre los elementos de $f[D]$ son además no vacías y cubren $D$, pues cada $x$ pertenece a la fibra de $f(x)$. Si se indexaran por todo $E$, podrían aparecer fibras vacías correspondientes a salidas no alcanzadas.

Para el mismo cuadrado,

$$
q^{-1}[(1,4]]=\{x\in\mathbb R:1<x^2\le4\}
=[-2,-1)\cup(1,2].
$$

Resolver $1<x^2\le4$ equivale a $1<|x|\le2$. La rama positiva da $(1,2]$ y la negativa $[-2,-1)$. Los puntos $\pm2$ se incluyen por el extremo cerrado cuatro de las salidas; $\pm1$ se excluyen por el extremo abierto uno. Las dos ramas satisfacen la misma condición y ambas deben conservarse.

Si cambiamos la función a $r:[0,\infty)\to\mathbb R$, $r(x)=x^2$, la misma condición produce

$$
r^{-1}[(1,4]]=(1,2].
$$

La desigualdad sobre la salida no ha cambiado. Lo que cambia es el lugar donde buscamos entradas: intersectamos $[-2,-1)\cup(1,2]$ con $[0,\infty)$ y queda $(1,2]$. Resolver una condición y recortarla por el dominio son obligaciones distintas. Una solución real fuera del dominio no entra en la preimagen de la función restringida.

Para toda función $f:D\to E$,

$$
f^{-1}[E]=D,\qquad f^{-1}[\varnothing]=\varnothing.
$$

Toda entrada tiene salida en $E$, lo que prueba $D\subseteq f^{-1}[E]$; la inclusión contraria forma parte de la definición de preimagen. Ninguna entrada tiene salida en el vacío. Si $B\subseteq H\subseteq E$, la condición $f(x)\in B$ implica $f(x)\in H$ para la misma entrada, luego $f^{-1}[B]\subseteq f^{-1}[H]$. La selección hacia atrás conserva inclusiones sin ninguna condición de inyectividad o sobreyectividad.

Para entender cuánto recuperamos al seleccionar hacia atrás y volver hacia delante, calculemos

$$
f[f^{-1}[B]]=B\cap f[D].
$$

Si $y$ está a la izquierda, existe $x\in f^{-1}[B]$ con $f(x)=y$. Esa entrada está en $D$ y su salida pertenece a $B$, así que $y\in B\cap f[D]$. Para la inclusión inversa, partimos de $y\in B\cap f[D]$: la pertenencia a la imagen ofrece un testigo $x\in D$ con $f(x)=y$, y la pertenencia a $B$ hace que ese testigo esté en $f^{-1}[B]$. Así vuelve a producir $y$ al tomar imagen. La operación recupera las salidas solicitadas que realmente podían alcanzarse.

Por ejemplo, para el cuadrado y $B=\{-1,4\}$, la selección da $\{-2,2\}$ y su imagen es $\{4\}$. La salida imposible $-1$ no reaparece. Si exigiéramos recuperar exactamente todo $B$ para cualquier subconjunto del codominio, estaríamos exigiendo sobreyectividad; basta tomar $B=E$ para ver esa obligación.

### Ejercicios de la sección 12.3

#### Ejercicio 11. Selección de dos bandas

[]{#MA-EX-ANM-01-012-011}

Calcula $q^{-1}[[0,1)\cup\{4\}]$ para $q:\mathbb R\to\mathbb R$, $q(x)=x^2$.

[]{#MA-SOL-ANM-01-012-011}

<details class="anm-solution">
<summary>Ver solución del ejercicio 11</summary>

La condición $0\le x^2<1$ equivale a $|x|<1$, y $x^2=4$ equivale a $x=-2$ o $x=2$. Por tanto la preimagen es $(-1,1)\cup\{-2,2\}$. Se excluyen $\pm1$ por la desigualdad estricta, y se incluyen cero y las dos raíces de cuatro.

La preimagen conserva la unión, así que podemos resolver las dos condiciones por separado. Para la banda $[0,1)$, la no negatividad del cuadrado ya es automática y la condición restante es $|x|<1$. Para la salida aislada cuatro, las entradas son dos y menos dos. Estos puntos están separados de la banda central y permanecen aislados en la respuesta. No debemos rellenar los intervalos entre ellos: sus cuadrados no pertenecen al conjunto de salidas solicitado.

</details>

#### Ejercicio 12. El dominio recorta la respuesta

[]{#MA-EX-ANM-01-012-012}

Sea $f:[-1,3)\to\mathbb R$, $f(x)=x^2$. Calcula $f^{-1}[(1,4]]$.

[]{#MA-SOL-ANM-01-012-012}

<details class="anm-solution">
<summary>Ver solución del ejercicio 12</summary>

En toda la recta la condición da $[-2,-1)\cup(1,2]$. Intersectando con el dominio $[-1,3)$ desaparece la rama negativa, incluido $-1$ que además no cumple $x^2>1$. Queda $(1,2]$. Ambas inclusiones siguen de resolver la condición y exigir pertenencia al dominio.

Primero resolvemos la desigualdad $1<x^2\le4$ sin el recorte de dominio; después intersectamos el resultado con $[-1,3)$. La rama negativa $[-2,-1)$ queda totalmente fuera de ese dominio. El punto menos uno, aunque está en el dominio, tampoco cumple la condición estricta de la salida. La rama positiva $(1,2]$ sí queda completa dentro. Resolver la condición algebraica y verificar el dominio son dos obligaciones distintas y ambas son necesarias.

</details>

#### Ejercicio 13. Las fibras particionan el dominio

[]{#MA-EX-ANM-01-012-013}

Para $f:D\to E$, demuestra que las fibras sobre los elementos de $f[D]$ son no vacías, disjuntas dos a dos y su unión es $D$.

[]{#MA-SOL-ANM-01-012-013}

<details class="anm-solution">
<summary>Ver solución del ejercicio 13</summary>

Cada $y\in f[D]$ tiene un testigo de entrada, así que su fibra no es vacía. Si una entrada pertenece a las fibras de $y,z$, su única salida es tanto $y$ como $z$, luego $y=z$. Cada $x\in D$ pertenece a la fibra sobre $f(x)\in f[D]$, y toda fibra es subconjunto de $D$; su unión es exactamente $D$. Si $D$ es vacío, la familia es vacía y su unión también.

La familia se indexa por la imagen $f[D]$, no por todo el codominio: así cada pieza tiene al menos una entrada. Dos fibras distintas no pueden compartir una entrada, porque ésta tendría dos salidas distintas. Para cubrir el dominio basta escoger, para cada entrada $x$, la fibra cuyo índice es su propia salida $f(x)$. No se necesita elegir una entrada representativa en cada fibra. Cada entrada pertenece a exactamente una pieza y las piezas pueden contener varias entradas.

</details>

#### Ejercicio 14. Recuperar todas las salidas solicitadas

[]{#MA-EX-ANM-01-012-014}

Prueba que $f[f^{-1}[B]]=B$ para todo $B\subseteq E$ si y sólo si $f:D\to E$ es sobreyectiva.

[]{#MA-SOL-ANM-01-012-014}

<details class="anm-solution">
<summary>Ver solución del ejercicio 14</summary>

Si es sobreyectiva, $f[D]=E$ y la identidad del texto da $f[f^{-1}[B]]=B\cap E=B$. Recíprocamente, aplicamos la hipótesis a $B=E$: como $f^{-1}[E]=D$, obtenemos $f[D]=E$, que es sobreyectividad. No se necesita inyectividad: puede haber varias entradas para cada salida.

La dirección directa usa que una función sobreyectiva no deja salidas imposibles en $E$, por lo que intersectar $B$ con su imagen no elimina nada. Para la recíproca no necesitamos probar la identidad con todos los subconjuntos uno por uno: la hipótesis universal permite escoger el subconjunto concreto $B=E$. Recuperar todas sus salidas obliga a $f[D]=E$. La unicidad de sus entradas no interviene, así que no hace falta inyectividad.

</details>

#### Ejercicio 15. La preimagen conoce la función

[]{#MA-EX-ANM-01-012-015}

Sean $f,g:D\to E$. Si $f^{-1}[B]=g^{-1}[B]$ para todo $B\subseteq E$, demuestra que $f=g$.

[]{#MA-SOL-ANM-01-012-015}

<details class="anm-solution">
<summary>Ver solución del ejercicio 15</summary>

Para una entrada cualquiera $x\in D$, tomamos $B=\{f(x)\}$. Entonces $x\in f^{-1}[B]=g^{-1}[B]$, luego $g(x)\in\{f(x)\}$ y $g(x)=f(x)$. Vale para toda entrada y los tipos coinciden, así que las funciones son iguales. Si $D$ es vacío, los dos grafos son vacíos y la conclusión también vale. El conjunto de prueba puede elegirse después de fijar la entrada porque la hipótesis cubre todos los subconjuntos.

El conjunto $B$ se elige después de fijar una entrada $x$, y eso es legítimo porque la hipótesis cubre todos los subconjuntos del codominio. En el conjunto unitario $\{f(x)\}$ sólo hay un valor disponible. La igualdad de preimágenes obliga a que la salida de $g$ para esa misma entrada sea ese valor. Repetimos el razonamiento para una entrada arbitraria, no para una muestra finita. Con tipos iguales, la coincidencia de todas las evaluaciones identifica ambas funciones.

</details>

## 12.4. Qué operaciones sobreviven al transporte

[]{#MA-SEC-ANM-01-012-004}

Las imágenes de una unión pueden reunirse sin perder salidas: un testigo pertenece a una pieza o a la otra. Al intersectar imágenes aparece una dificultad distinta: la misma salida puede tener un testigo en cada pieza sin que esas entradas coincidan. Esa diferencia entre uno y dos testigos decide qué operaciones se conservan.

Fijemos $f:D\to E$, $A,C\subseteq D$ y $B,H\subseteq E$.

Tenemos

$$
f[A\cup C]=f[A]\cup f[C],\qquad
f[A\cap C]\subseteq f[A]\cap f[C].
$$

Para la unión, tomemos $y\in f[A\cup C]$ y una entrada $x\in A\cup C$ con $f(x)=y$. Si $x\in A$, entonces $y\in f[A]$; si $x\in C$, entonces $y\in f[C]$. En la dirección contraria, cualquier testigo en una de las piezas también pertenece a la unión. El mismo testigo acredita las dos implicaciones y prueba la igualdad.

Un testigo en $A\cap C$ sirve a la vez en ambas imágenes, lo que prueba la inclusión de la segunda fórmula. Para intentar la vuelta, $y\in f[A]\cap f[C]$ sólo ofrece $a\in A$ y $c\in C$ con $f(a)=f(c)=y$. Nos falta una razón para que $a=c$: dos pertenencias a imágenes no proporcionan por sí solas una entrada común.

En el cuadrado, $A=\{-1\}$ y $C=\{1\}$ no comparten entrada, pero ambas imágenes son $\{1\}$. La inclusión es estricta. Si $f$ es **inyectiva**, es decir, si $f(a)=f(c)$ implica $a=c$, los dos testigos de una salida común coinciden y pertenecen a $A\cap C$; entonces hay igualdad. Esta hipótesis resuelve exactamente el paso que faltaba. A la inversa, exigir esa igualdad para todos los pares de conjuntos prohíbe cualquier colisión, como se comprobará con conjuntos unitarios en los problemas.

![Una salida en ambas imágenes puede tener dos testigos diferentes. Para convertirlos en una entrada común se necesita inyectividad.](../../assets/books/anm/C12/C12-F03.svg){#fig-anm-c12-f03 fig-alt="Dos paneles: los conjuntos unitarios {-1} y {1} son disjuntos pero ambos tienen imagen {1}; dos testigos distintos apuntan a la misma salida."}

En una preimagen la entrada $x\in D$ permanece fija. Cada condición consulta su única salida $f(x)$, de modo que podemos combinar las condiciones lógicas sobre ella:

$$
\begin{aligned}
x\in f^{-1}[B\cup H]&\iff f(x)\in B\text{ o }f(x)\in H,\\
x\in f^{-1}[B\cap H]&\iff f(x)\in B\text{ y }f(x)\in H,\\
x\in f^{-1}[E\setminus B]&\iff f(x)\notin B.
\end{aligned}
$$

La alternativa de la primera fila selecciona $f^{-1}[B]\cup f^{-1}[H]$; la conjunción de la segunda selecciona $f^{-1}[B]\cap f^{-1}[H]$; negar la pertenencia en la tercera selecciona $D\setminus f^{-1}[B]$. Las equivalencias valen para toda entrada de $D$ y proporcionan ambas inclusiones de cada identidad. Por extensionalidad,

$$
\begin{aligned}
f^{-1}[B\cup H]&=f^{-1}[B]\cup f^{-1}[H],\\
f^{-1}[B\cap H]&=f^{-1}[B]\cap f^{-1}[H],\\
f^{-1}[E\setminus B]&=D\setminus f^{-1}[B].
\end{aligned}
$$

No hemos reunido testigos distintos ni pedido que toda salida tenga entrada. Por eso las leyes no requieren inyectividad o sobreyectividad. Los complementos sí deben respetar sus universos: $E\setminus B$ es un conjunto de salidas y $D\setminus f^{-1}[B]$ un conjunto de entradas. La condición $f(x)\in B\setminus H$ dice $f(x)\in B$ y $f(x)\notin H$; al traducir esas dos exigencias a preimágenes obtenemos también

$$
f^{-1}[B\setminus H]=f^{-1}[B]\setminus f^{-1}[H].
$$

El viaje en el otro sentido conserva todas las entradas originales: $A\subseteq f^{-1}[f[A]]$, porque $f(a)\in f[A]$ para cada $a\in A$. Puede recuperar otras entradas que compartan sus salidas. Con el cuadrado y $A=\{1\}$ obtenemos $f^{-1}[f[A]]=\{-1,1\}$. Llamaremos a este conjunto la **saturación de $A$ por las fibras**: reúne cada fibra que toca $A$ con todas sus entradas.

Si $f$ es inyectiva, una entrada $x$ de esa saturación comparte salida con algún $a\in A$ y debe coincidir con él. La inclusión se convierte en igualdad. Para una función cualquiera, saturar puede ampliar $A$, pero no produce salidas nuevas: la identidad de §12.3 da $f[f^{-1}[f[A]]]=f[A]$. Una segunda saturación seleccionaría las mismas fibras completas.

Los complementos de imágenes también pueden fallar por una colisión. Para el cuadrado, quitar la entrada $1$ no elimina su salida, porque $-1$ todavía produce uno: $q[\mathbb R\setminus\{1\}]=[0,\infty)$. En cambio, $\mathbb R\setminus q[\{1\}]=\mathbb R\setminus\{1\}$, que excluye uno e incluye negativos. La identificación de entradas y las salidas no alcanzadas del codominio son dos obstáculos diferentes a una ley de complementos.

### Ejercicios de la sección 12.4

#### Ejercicio 16. Álgebra de una selección

[]{#MA-EX-ANM-01-012-016}

Prueba directamente $f^{-1}[(B\cup H)\setminus K]=(f^{-1}[B]\cup f^{-1}[H])\setminus f^{-1}[K]$ para $B,H,K\subseteq E$.

[]{#MA-SOL-ANM-01-012-016}

<details class="anm-solution">
<summary>Ver solución del ejercicio 16</summary>

Para $x\in D$, pertenecer al lado izquierdo significa $(f(x)\in B\text{ o }f(x)\in H)$ y $f(x)\notin K$. Esto equivale a $(x\in f^{-1}[B]\text{ o }x\in f^{-1}[H])$ y $x\notin f^{-1}[K]$, exactamente el lado derecho. Como la equivalencia vale para toda entrada, extensionalidad da igualdad. No se han supuesto inyectividad o sobreyectividad.

La prueba traduce operaciones de conjuntos a condiciones lógicas: unión se convierte en «o» y diferencia en «y no». La preimagen evalúa siempre la misma entrada $x$, de modo que esas condiciones pueden combinarse sin elegir testigos diferentes. Al traducirlas de vuelta obtenemos exactamente el conjunto del segundo miembro. La equivalencia para cada entrada acredita ambas inclusiones de una sola vez y evita suponer reglas de imágenes que no siempre son válidas.

</details>

#### Ejercicio 17. La intersección detecta inyectividad

[]{#MA-EX-ANM-01-012-017}

Prueba que $f[A\cap C]=f[A]\cap f[C]$ para todos $A,C\subseteq D$ si y sólo si $f$ es inyectiva.

[]{#MA-SOL-ANM-01-012-017}

<details class="anm-solution">
<summary>Ver solución del ejercicio 17</summary>

La dirección inyectiva está probada en el texto: los dos testigos de una salida común coinciden. Para la recíproca, supongamos $f(a)=f(c)$ y $a\ne c$. Tomando $A=\{a\}$, $C=\{c\}$, la imagen de su intersección es vacía, mientras que la intersección de imágenes es $\{f(a)\}$, contradicción. Luego no hay entradas distintas con igual salida.

**Retorno visual.** Véase [C12-F03](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f03), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Para la vuelta, los conjuntos unitarios permiten detectar cualquier colisión. Si dos entradas distintas comparten salida, sus conjuntos unitarios son disjuntos, pero sus imágenes se intersectan en esa salida. La identidad exigida para todos los conjuntos no puede tolerar esta diferencia. En la dirección directa, la inyectividad junta los dos testigos de una salida común en una sola entrada de la intersección. Por eso la ley universal caracteriza exactamente la ausencia de colisiones.

</details>

#### Ejercicio 18. Saturar dos veces

[]{#MA-EX-ANM-01-012-018}

Define $S(A)=f^{-1}[f[A]]$. Prueba $A\subseteq S(A)$, que $A\subseteq C$ implica $S(A)\subseteq S(C)$ y que $S(S(A))=S(A)$.

[]{#MA-SOL-ANM-01-012-018}

<details class="anm-solution">
<summary>Ver solución del ejercicio 18</summary>

Cada $a\in A$ tiene salida en $f[A]$, luego está en $S(A)$. Si $A\subseteq C$, las inclusiones conservadas por imagen y preimagen dan $S(A)\subseteq S(C)$. Finalmente $f[S(A)]=f[f^{-1}[f[A]]]=f[A]\cap f[D]=f[A]$. Tomando preimagen, $S(S(A))=f^{-1}[f[S(A)]]=f^{-1}[f[A]]=S(A)$. La saturación añade fibras completas una sola vez.

La saturación reúne todas las entradas que comparten alguna salida con una entrada de $A$. La primera aplicación puede añadir entradas nuevas, pero no añade salidas nuevas: $f[S(A)]=f[A]$. Por eso una segunda aplicación selecciona las mismas fibras completas y no cambia el resultado. Las tres propiedades se comprueban con inclusiones y la identidad de imagen de una preimagen; no exigen que $f$ sea inyectiva. Si lo fuera, no habría nada que añadir y $S(A)=A$.

</details>

#### Ejercicio 19. Complementos y biyectividad

[]{#MA-EX-ANM-01-012-019}

Prueba que $f[D\setminus A]=E\setminus f[A]$ para todo $A\subseteq D$ si y sólo si $f:D\to E$ es biyectiva.

[]{#MA-SOL-ANM-01-012-019}

<details class="anm-solution">
<summary>Ver solución del ejercicio 19</summary>

Si $f$ es biyectiva, toda $y\in E$ tiene una única entrada $x$; está en la imagen de $D\setminus A$ exactamente cuando $x\notin A$, lo que equivale a $y\notin f[A]$. Para la recíproca, usar $A=\varnothing$ da $f[D]=E$, sobreyectividad. Si $a\ne c$ y $f(a)=f(c)$, tomando $A=\{a\}$, la salida común pertenece a $f[D\setminus A]$ por el testigo $c$ y también a $f[A]$, contradiciendo la igualdad con el complemento. Por tanto es inyectiva.

La igualdad de complementos impone dos cosas a la vez. Usar el conjunto vacío obliga a alcanzar todo el codominio. Después, cualquier par de entradas distintas con la misma salida haría que esa salida apareciera tanto en $f[A]$ como en $f[D\setminus A]$ para un $A$ adecuado, lo que un complemento prohíbe. A la inversa, para una biyectiva cada salida tiene una entrada única, que está exactamente en una de las dos partes del dominio. Esto prueba la identidad y explica las dos hipótesis necesarias.

</details>

#### Ejercicio 20. Seleccionar una partición

[]{#MA-EX-ANM-01-012-020}

Sea $E=B_1\cup\cdots\cup B_k$ una partición finita en piezas no vacías. Prueba que sus preimágenes cubren $D$ y son disjuntas, y explica por qué pueden no formar una partición en piezas no vacías.

[]{#MA-SOL-ANM-01-012-020}

<details class="anm-solution">
<summary>Ver solución del ejercicio 20</summary>

Toda entrada tiene salida en alguna pieza, de modo que pertenece a alguna preimagen. Si pertenece a dos, su salida está en ambas piezas; la disjunción de las $B_i$ lo impide cuando los índices son distintos. Pero una pieza puede no contener salidas alcanzadas. Por ejemplo, para el cuadrado real, las piezas $(-\infty,0)$ y $[0,\infty)$ particionan $\mathbb R$ y la primera tiene preimagen vacía. Tras eliminar piezas vacías, las restantes sí particionan $D$ si éste no es vacío.

Cubrir todo $E$ garantiza que cada salida esté en alguna pieza y, por tanto, cada entrada en alguna preimagen. La disjunción garantiza que una entrada no caiga en dos preimágenes distintas. Pero que una pieza de salidas sea no vacía no obliga a que contenga una salida alcanzada. Para el cuadrado, la pieza negativa existe y tiene preimagen vacía. El transporte hacia atrás conserva cobertura y disjunción, pero puede perder la no vacuidad de las piezas.

</details>

## 12.5. Componer, restringir y deshacer

[]{#MA-SEC-ANM-01-012-005}

Una transformación puede entregar las entradas de otra. Si $f:D\to E$ y $g:E\to F$, definimos $g\circ f:D\to F$ por $(g\circ f)(x)=g(f(x))$. Primero $x\in D$ produce un elemento de $E$ y después $g$ puede evaluarse en él. Más generalmente basta que $f[D]$ esté contenido en el dominio de $g$, aunque no coincidan los conjuntos intermedios declarados; hay que comprobarlo y declarar el tipo de la composición. Una fórmula como $1/(x-1)$ no autoriza la entrada $x=1$ si la segunda etapa consiste en invertir $x-1$.

Si $A\subseteq D$ y $C\subseteq F$,

$$
(g\circ f)[A]=g[f[A]],\qquad
(g\circ f)^{-1}[C]=f^{-1}[g^{-1}[C]].
$$

Para transportar $A$ hacia delante, cada salida compuesta tiene forma $g(f(x))$ con $x\in A$ y, por tanto, pertenece a $g[f[A]]$. Recíprocamente, un testigo intermedio $y\in f[A]$ de una salida $z=g(y)$ tiene a su vez una entrada $x\in A$ con $f(x)=y$; sustituir da $z=g(f(x))$. Para seleccionar hacia atrás fijamos $x\in D$: $g(f(x))\in C$ equivale a que $f(x)$ esté en $g^{-1}[C]$, es decir, a que $x$ esté en $f^{-1}[g^{-1}[C]]$. La última etapa de evaluación es la primera condición que resolvemos al regresar.

En $f(x)=x^2$ y $g(y)=y+1$, ambas de $\mathbb R$ a $\mathbb R$, la composición es $x^2+1$. Para seleccionar salidas en $(2,5]$, empezamos con $2<y+1\le5$, equivalente a $1<y\le4$. Después resolvemos $1<x^2\le4$ y recuperamos $[-2,-1)\cup(1,2]$. La exclusión de las raíces de uno y la inclusión de las de cuatro vienen de los extremos de las salidas finales. Ninguna etapa ha requerido una inversa del cuadrado.

Para $A\subseteq D$, la **restricción** $f|_A:A\to E$ conserva las asignaciones en $A$. Su imagen es $f[A]$ y, para $B\subseteq E$,

$$
(f|_A)^{-1}[B]=A\cap f^{-1}[B].
$$

Pertenecer a cualquiera de los dos lados exige exactamente $x\in A$ y $f(x)\in B$. La restricción conserva los valores y el codominio $E$; no lo sustituye automáticamente por la imagen. Para el cuadrado, restringir entradas a $[0,\infty)$ elimina las colisiones y da inyectividad, pero con codominio $\mathbb R$ siguen faltando entradas para todas las salidas negativas. Sólo al declarar además codominio $[0,\infty)$ obtenemos sobreyectividad, gracias a la existencia y unicidad de la raíz no negativa de §10.7.

$f:D\to E$ es **sobreyectiva** si $f[D]=E$, y **biyectiva** si además es inyectiva. Sólo entonces existe una función inversa $h:E\to D$ que deshace $f$ en ambas direcciones:

$$
h\circ f=\operatorname{id}_D,\qquad f\circ h=\operatorname{id}_E.
$$

La sobreyectividad proporciona, para cada $y\in E$, alguna entrada $x\in D$ con $f(x)=y$; la inyectividad impide que haya dos. Definimos $h(y)$ como esa única entrada. Para $x\in D$, la entrada que produce $f(x)$ sólo puede ser $x$, luego $h(f(x))=x$. Para $y\in E$, la propia definición da $f(h(y))=y$. Si otra función $k:E\to D$ deshiciera $f$, entonces $f(k(y))=y=f(h(y))$ y la inyectividad daría $k(y)=h(y)$ para todo $y$. Así la inversa existe y es única; la definición por entrada única no obliga a escoger arbitrariamente entre varias candidatas.

Las dos identidades también obligan a las hipótesis. Si $f(x)=f(z)$, aplicar $h$ y usar $h\circ f=\operatorname{id}_D$ da $x=z$. Para una salida cualquiera $y\in E$, la identidad $f\circ h=\operatorname{id}_E$ proporciona la entrada $h(y)$ que la alcanza. La primera recupera entradas y fuerza inyectividad; la segunda alcanza salidas y fuerza sobreyectividad. Se necesitan ambas para deshacer la función en los dos sentidos.

Tras probarlo, escribimos $h=f^{-1}$. La evaluación $f^{-1}(y)$ es entonces una entrada única. Para $B\subseteq E$, su imagen por $h$ coincide con la preimagen ya definida: si $f(x)\in B$, entonces $x=h(f(x))\in h[B]$; si $x=h(y)$ con $y\in B$, entonces $f(x)=y\in B$. Por tanto $f^{-1}[B]=h[B]$. Esta coincidencia explica la notación, pero la selección de preimágenes estaba disponible incluso cuando no existía $h$.

Para $f:\mathbb R\to\mathbb R$, $f(x)=2x+1$, despejar $y=2x+1$ da $x=(y-1)/2$, una entrada real única para cualquier $y$. La candidata $h(y)=(y-1)/2$ verifica $h(f(x))=x$ y $f(h(y))=y$ por sustitución. El cuadrado en toda la recta carece de inversa; como aplicación $[0,\infty)\to[0,\infty)$ sí la tiene, dada por la raíz no negativa. El mismo cálculo de una raíz cambia de función cuando cambian los tipos.

### Ejercicios de la sección 12.5

#### Ejercicio 21. La última etapa se filtra primero

[]{#MA-EX-ANM-01-012-021}

Para $f(x)=x^2$ y $g(y)=3-y$, ambas reales, calcula $(g\circ f)^{-1}[[1,3)]$ por etapas.

[]{#MA-SOL-ANM-01-012-021}

<details class="anm-solution">
<summary>Ver solución del ejercicio 21</summary>

Primero $1\le3-y<3$ equivale a $0<y\le2$, luego $g^{-1}[[1,3)]=(0,2]$. Después $0<x^2\le2$ da $[-\sqrt2,0)\cup(0,\sqrt2]$. Cero se excluye porque su salida compuesta es $3$; ambas raíces de dos se incluyen porque su salida es $1$.

La última etapa se resuelve primero: $1\le3-y$ da $y\le2$, y $3-y<3$ da $y>0$. Así el conjunto intermedio es $(0,2]$. Aplicar luego el cuadrado exige $0<x^2\le2$, que admite las dos ramas y excluye cero. El extremo tres abierto de las salidas finales explica esa exclusión; el extremo uno cerrado explica que se incluyan las raíces de dos. El procedimiento mantiene los extremos correctos en cada etapa.

</details>

#### Ejercicio 22. Una composición sin tipo

[]{#MA-EX-ANM-01-012-022}

Sea $f:\mathbb R\to\mathbb R$, $f(x)=x-1$, y $g:\mathbb R\setminus\{0\}\to\mathbb R$, $g(y)=1/y$. ¿Define $g\circ f$ una función en todo $\mathbb R$? Declara la composición válida y su regla.

[]{#MA-SOL-ANM-01-012-022}

<details class="anm-solution">
<summary>Ver solución del ejercicio 22</summary>

No: $f(1)=0$ no pertenece al dominio de $g$. Las entradas admisibles son $f^{-1}[\mathbb R\setminus\{0\}]=\mathbb R\setminus\{1\}$. Restringiendo $f$ a ese dominio, la composición válida es $h:\mathbb R\setminus\{1\}\to\mathbb R$, $h(x)=1/(x-1)$. Cada evaluación de la segunda etapa está ahora autorizada.

El problema no es calcular una fórmula formal, sino comprobar que cada evaluación intermedia está permitida. En la entrada uno, la primera etapa entrega cero y la segunda no está definida allí. El dominio máximo admitido por esa fórmula compuesta es el conjunto de entradas con $x-1\ne0$. La restricción debe además declarar que sus salidas intermedias pertenecen a $\mathbb R\setminus\{0\}$, el dominio de $g$. Con esos datos, la regla $1/(x-1)$ queda bien definida.

</details>

#### Ejercicio 23. Dos identidades distintas

[]{#MA-EX-ANM-01-012-023}

Para $f:D\to E$ y $h:E\to D$, prueba que $h\circ f=\operatorname{id}_D$ implica inyectividad de $f$ y que $f\circ h=\operatorname{id}_E$ implica sobreyectividad de $f$. Da un ejemplo donde sólo se cumpla la primera.

[]{#MA-SOL-ANM-01-012-023}

<details class="anm-solution">
<summary>Ver solución del ejercicio 23</summary>

Si $f(x)=f(z)$, aplicar $h$ y la primera identidad da $x=z$. Con la segunda, cada $y\in E$ tiene entrada $h(y)$ y $f(h(y))=y$. Para distinguirlas, sea $f:[0,\infty)\to\mathbb R$ la inclusión $f(x)=x$, y $h:\mathbb R\to[0,\infty)$, $h(y)=\max(y,0)$. Para $x\ge0$, $h(f(x))=x$. Pero $f(h(-1))=0\ne-1$, así que no hay segunda identidad y $f$ no es sobreyectiva.

La primera identidad permite recuperar cualquier entrada después de aplicar $f$; por eso dos entradas con salida común tendrían que recuperarse como la misma. La segunda identidad asegura que toda salida se produce a partir de la entrada $h(y)$; por eso garantiza sobreyectividad. En el ejemplo, las entradas no negativas sí se recuperan, pero las salidas negativas se reemplazan por cero y no pueden recuperarse. Una identidad por sí sola no demuestra que $h$ sea una inversa en ambos sentidos.

</details>

#### Ejercicio 24. Inversa sobre la imagen

[]{#MA-EX-ANM-01-012-024}

Si $f:D\to E$ es inyectiva, demuestra que cambiando el codominio a $f[D]$ se obtiene una biyectiva. ¿Por qué su inversa no tiene necesariamente dominio $E$?

[]{#MA-SOL-ANM-01-012-024}

<details class="anm-solution">
<summary>Ver solución del ejercicio 24</summary>

La asignación $\widetilde f:D\to f[D]$ es válida y mantiene inyectividad. Es sobreyectiva por definición de imagen: cada $y\in f[D]$ tiene una entrada. Luego tiene inversa $f[D]\to D$. Si hay $y\in E\setminus f[D]$, no existe entrada que alcance $y$, por lo que esa inversa no puede deshacer la asignación en tal salida. Ejemplo: inclusión $[0,\infty)\to\mathbb R$, cuya imagen es $[0,\infty)$.

Cambiar el codominio a la imagen no modifica las evaluaciones ni el grafo, pero sí el objeto tipado. La nueva función alcanza todo lo declarado por definición, y la inyectividad original proporciona unicidad. Su inversa acepta únicamente salidas alcanzadas. Si el codominio original contenía salidas sin testigo, una inversa definida allí no podría cumplir $f(f^{-1}(y))=y$. La construcción distingue una inversa sobre la imagen de una inversa sobre todo el codominio original.

</details>

#### Ejercicio 25. La inversa de una composición

[]{#MA-EX-ANM-01-012-025}

Sean $f:D\to E$ y $g:E\to F$ biyectivas. Prueba que $g\circ f$ es biyectiva y su inversa es $f^{-1}\circ g^{-1}$.

[]{#MA-SOL-ANM-01-012-025}

<details class="anm-solution">
<summary>Ver solución del ejercicio 25</summary>

La candidata $h=f^{-1}\circ g^{-1}:F\to D$ está tipada. Para $x\in D$, $h(g(f(x)))=f^{-1}(g^{-1}(g(f(x))))=f^{-1}(f(x))=x$. Para $z\in F$, $g(f(h(z)))=g(f(f^{-1}(g^{-1}(z))))=g(g^{-1}(z))=z$. Las dos identidades probadas en el texto garantizan biyectividad y unicidad de la inversa. El orden se invierte porque primero debe deshacerse la última etapa.

Una salida final $z\in F$ se deshace primero mediante $g^{-1}$, que la lleva al conjunto intermedio $E$. Después $f^{-1}$ la lleva a la entrada inicial en $D$. Invertir ese orden daría, en general, una composición sin tipos compatibles. Las dos identidades verificadas garantizan tanto recuperar todas las entradas como producir todas las salidas; juntas prueban biyectividad. La comprobación debe hacerse para variables arbitrarias de ambos conjuntos, no para ejemplos puntuales.

</details>

## 12.6. Transportar el orden no rellena los huecos

[]{#MA-SEC-ANM-01-012-006}

Ya sabemos transportar conjuntos. En la recta podemos preguntar además si una transformación conserva la comparación entre entradas. Sea $f:D\to\mathbb R$, $D\subseteq\mathbb R$. Diremos que es **no decreciente** cuando

$$
x,y\in D,\quad x\le y\quad\Longrightarrow\quad f(x)\le f(y).
$$

Es **estrictamente creciente** cuando $x<y$ implica $f(x)<f(y)$. «No creciente» y «estrictamente decreciente» invierten las desigualdades entre salidas. Siempre declaramos cuál sentido usamos: algunas convenciones llaman creciente al caso no estricto.

Una función estrictamente creciente es inyectiva. Dos entradas distintas se ordenan por tricotomía: si $x<y$, sus salidas satisfacen $f(x)<f(y)$, y si $y<x$ sucede lo contrario; no pueden coincidir. El mismo argumento sirve para una función estrictamente decreciente y no requiere que el dominio sea un intervalo. Una constante es no decreciente y no creciente a la vez; en un dominio con al menos dos entradas distintas no es inyectiva.

Si $f$ es no decreciente y $a,b\in D$ con $a\le b$, entonces

$$
f[D\cap[a,b]]\subseteq[f(a),f(b)].
$$

Para cada $x\in D\cap[a,b]$, las dos comparaciones $a\le x$ y $x\le b$ dan $f(a)\le f(x)\le f(b)$. Esto sitúa todas las salidas producidas entre las extremas. Para convertir la inclusión en igualdad faltaría producir una entrada para cada número intermedio; la prueba de monotonía todavía no ha ofrecido esos testigos.

Definamos $s:\mathbb R\to\mathbb R$ por

$$
s(x)=\begin{cases}x,&x<0,\\x+1,&x\ge0.\end{cases}
$$

Para demostrar que es estrictamente creciente debemos comprobar todos los pares $x<y$. Si ambos son negativos, las salidas conservan esas entradas; si ambos son no negativos, sumar uno conserva su orden estricto. En el caso que cruza cero, $x<0\le y$ da $s(x)=x<0<1\le y+1=s(y)$. Los tres casos agotan las posiciones posibles y prueban el crecimiento en toda la recta.

Sin embargo,

$$
s[[-1,1]]=[-1,0)\cup[1,2].
$$

La rama de entradas $[-1,0)$ mantiene exactamente esas salidas, mientras $[0,1]$ se traslada a $[1,2]$. Cada valor de la primera pieza se alcanza en sí mismo y cada valor $t$ de la segunda en $t-1$. El número $1/2$ está entre $s(-1)=-1$ y $s(1)=2$, pero ninguna rama lo alcanza. Ordenar estrictamente las salidas existentes permite un hueco en la imagen. Para garantizar todas las salidas intermedias hará falta otra hipótesis.

![El salto conserva el orden estricto entre todas las entradas, pero la imagen de \[-1,1\] es \[-1,0) unión \[1,2\]. Ordenar salidas existentes no produce las que faltan.](../../assets/books/anm/C12/C12-F04.svg){#fig-anm-c12-f04 fig-alt="Gráfica de s(x)=x para x negativo y s(x)=x+1 para x no negativo en [-1,1]: punto abierto en (0,0), cerrado en (0,1); la imagen omite [0,1)."}

En una aplicación afín $h(x)=mx+b$, la diferencia $h(y)-h(x)=m(y-x)$ decide el orden. Para $x<y$, el factor $y-x$ es positivo: si $m>0$ la diferencia es positiva y hay crecimiento estricto; si $m<0$ es negativa y hay decrecimiento estricto; si $m=0$ todas las salidas coinciden. La constante de traslación se cancela.

Escribamos el término independiente como $c$ al calcular la imagen de $[a,b]$, para no confundirlo con el extremo derecho. Para $a\le b$ obtenemos

$$
h[[a,b]]=[ma+c,mb+c]\quad(m>0),
$$

$$
h[[a,b]]=[mb+c,ma+c]\quad(m<0).
$$

El orden prueba la inclusión de cada imagen en el intervalo indicado. Para la vuelta, fijamos una salida $t$ entre las extremas y despejamos $x=(t-c)/m$. Si $m>0$, dividir mantiene las desigualdades; si $m<0$, las invierte. En ambos casos obtenemos $a\le x\le b$ y $h(x)=t$, que acredita todas las salidas del intervalo. La misma resolución con desigualdades estrictas trata intervalos abiertos o semiabiertos y decide cuál extremo se incluye. Cuando $m=0$, la fórmula de despeje no se usa: todo intervalo no vacío tiene imagen $\{c\}$.

Las dos ramas del cuadrado muestran por qué el dominio importa también para el orden. Si $0\le x<y$, entonces $y-x>0$ y $y+x>0$, de modo que $y^2-x^2=(y-x)(y+x)>0$. Si $x<y\le0$, el primer factor sigue siendo positivo y el segundo es negativo, luego $y^2-x^2<0$. Así el cuadrado crece estrictamente en $[0,\infty)$ y decrece estrictamente en $(-\infty,0]$, con cero incluido en ambas ramas, pero no tiene un mismo sentido de monotonía en toda la recta.

### Ejercicios de la sección 12.6

#### Ejercicio 26. Imagen con orientación invertida

[]{#MA-EX-ANM-01-012-026}

Calcula la imagen de $[-1,2)$ por $h(x)=-3x+2$ con codominio real. Justifica ambas inclusiones.

[]{#MA-SOL-ANM-01-012-026}

<details class="anm-solution">
<summary>Ver solución del ejercicio 26</summary>

De $-1\le x<2$, al multiplicar por $-3$ y sumar $2$, resulta $-4<h(x)\le5$. Para $t\in(-4,5]$, $x=(2-t)/3$ satisface $-1\le x<2$ y $h(x)=t$. La imagen es $(-4,5]$. El extremo abierto de entrada pasa a extremo inferior abierto, y el cerrado a superior cerrado.

La pendiente negativa invierte las desigualdades al multiplicar por menos tres. El extremo izquierdo incluido menos uno produce la salida superior cinco incluida; el extremo derecho excluido dos correspondería a la salida inferior menos cuatro excluida. Para la inclusión contraria, despejamos $x=(2-t)/3$ y comprobamos directamente que cada salida $-4<t\le5$ da una entrada válida. Así calculamos toda la imagen sin depender de la apariencia de una gráfica.

</details>

#### Ejercicio 27. Dos sentidos estrictos

[]{#MA-EX-ANM-01-012-027}

Si $f:D\to E\subseteq\mathbb R$ y $g:E\to\mathbb R$ son estrictamente decrecientes, prueba que $g\circ f$ es estrictamente creciente.

[]{#MA-SOL-ANM-01-012-027}

<details class="anm-solution">
<summary>Ver solución del ejercicio 27</summary>

Para $x<y$ en $D$, $f(x)>f(y)$. Como $f(y)<f(x)$ y ambas salidas pertenecen a $E$, el decrecimiento estricto de $g$ da $g(f(y))>g(f(x))$. Así $(g\circ f)(x)<(g\circ f)(y)$. La compatibilidad de dominios permite aplicar la segunda hipótesis.

El primer decrecimiento invierte el orden de las entradas y el segundo vuelve a invertirlo. Para $x<y$, las salidas intermedias cumplen $f(y)<f(x)$; al aplicar $g$ a ese par ordenado obtenemos $g(f(x))<g(f(y))$. Las desigualdades siguen siendo estrictas, por lo que la composición es estrictamente creciente. La compatibilidad de tipos es indispensable para usar la segunda hipótesis con esas salidas intermedias.

</details>

#### Ejercicio 28. La inclusión de extremos puede ser propia

[]{#MA-EX-ANM-01-012-028}

Para la función $s$ de §12.6, prueba que $s[[-2,2]]$ es un subconjunto propio de $[s(-2),s(2)]$ aun siendo $s$ estrictamente creciente.

[]{#MA-SOL-ANM-01-012-028}

<details class="anm-solution">
<summary>Ver solución del ejercicio 28</summary>

El transporte por ramas da $[-2,0)\cup[1,3]$ y los valores extremos dan $[s(-2),s(2)]=[-2,3]$. Hay inclusión y es propia porque $1/2$ pertenece al segundo conjunto y no al primero. La prueba del crecimiento estricto en el texto incluye el caso que cruza cero; el hueco no lo contradice, pues crecimiento compara salidas existentes sin construir nuevas.

**Retorno visual.** Véase [C12-F04](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f04), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

La rama negativa conserva $[-2,0)$ y la no negativa traslada $[0,2]$ a $[1,3]$. Los extremos originales producen menos dos y tres, de modo que el intervalo entre ellos es $[-2,3]$. Una salida como $1/2$ acredita que la inclusión es propia. El crecimiento estricto sigue válido al cruzar cero, porque toda salida de la rama izquierda es negativa y toda salida de la derecha es al menos uno. Ese orden no garantiza que se alcancen los valores del hueco.

</details>

#### Ejercicio 29. Orden de la inversa

[]{#MA-EX-ANM-01-012-029}

Si $f:D\to E$ es estrictamente creciente y biyectiva, con $D,E\subseteq\mathbb R$, prueba que $f^{-1}$ es estrictamente creciente.

[]{#MA-SOL-ANM-01-012-029}

<details class="anm-solution">
<summary>Ver solución del ejercicio 29</summary>

Para $u<v$ en $E$, sean $x=f^{-1}(u)$, $y=f^{-1}(v)$. Si $x=y$, entonces $u=v$, imposible. Si $x>y$, crecimiento estricto da $u=f(x)>f(y)=v$, también imposible. Por tricotomía queda $x<y$. Así la inversa conserva el orden estricto en su propio dominio $E$.

La biyectividad asegura que las entradas inversas $x,y$ existen y son únicas. Para determinar su orden, descartamos las otras dos posibilidades de la tricotomía: igualdad daría salidas iguales y orden inverso daría salidas en orden inverso por el crecimiento de $f$. Queda necesariamente $x<y$. No se supone que $D$ o $E$ sean intervalos; basta que sus elementos hereden el orden real y que la función preserve estrictamente ese orden.

</details>

#### Ejercicio 30. Inyectividad no decide monotonía

[]{#MA-EX-ANM-01-012-030}

Construye una biyectiva $\mathbb R\to\mathbb R$ que no sea no decreciente ni no creciente.

[]{#MA-SOL-ANM-01-012-030}

<details class="anm-solution">
<summary>Ver solución del ejercicio 30</summary>

Intercambiamos $0$ y $1$ y fijamos todo otro real: $f(0)=1$, $f(1)=0$, $f(x)=x$ para $x\notin\{0,1\}$. Aplicarla dos veces devuelve cada entrada, así que es biyectiva. No es no decreciente porque $0<1$ pero $f(0)>f(1)$. No es no creciente porque $2<3$ y $f(2)<f(3)$. Reversibilidad y orden son propiedades independientes.

La asignación intercambia dos entradas y deja todas las demás fijas. Aplicarla dos veces restaura cada real, lo que proporciona una inversa igual a ella misma y prueba biyectividad. Un par de entradas prueba el fallo del crecimiento no estricto y otro prueba el fallo del decrecimiento no estricto. La conclusión no se deriva sólo de que la función parezca irregular: cada propiedad universal se refuta mediante testigos explícitos.

</details>

## 12.7. Distancia y escala: medir la deformación

[]{#MA-SEC-ANM-01-012-007}

La función $x\mapsto-x$ invierte el orden y conserva todas las distancias; $x\mapsto2x$ conserva el orden y duplica las distancias. Para distinguir esos efectos debemos comparar separaciones, además de posiciones relativas. Las aplicaciones afines permiten calcular ambos cambios exactamente.

Si $h(x)=mx+c$, entonces para todo $x,y\in\mathbb R$,

$$
|h(x)-h(y)|=|m(x-y)|=|m|\,|x-y|.
$$

La constante $c$ desaparece al restar. La magnitud $|m|$ fija la escala métrica y el signo de $m$ fija la orientación. Con $m=-1$ las salidas se ordenan al revés y mantienen su distancia; con $m=2$ mantienen el orden y duplican la separación; con $m=0$ las distancias se anulan. El factor $|m|$ es además la menor cota no negativa posible en toda la recta: cualquier cota debe funcionar para las entradas cero y uno y, por tanto, ser al menos $|m|$.

![La traslación cambia posición, el signo de m cambia orientación y |m| cambia distancia. Los tres papeles se separan en h(x)=mx+c.](../../assets/books/anm/C12/C12-F05.svg){#fig-anm-c12-f05 fig-alt="Tres transportes de las entradas cero y uno: x+2 conserva distancia uno; -x+2 invierte orientación y conserva distancia uno; 2x+2 duplica distancia a dos."}

Una función $f:D\to\mathbb R$ tiene **cota de expansión $L$**, o es $L$-Lipschitz, si $L\ge0$ y

$$
|f(x)-f(y)|\le L|x-y|\qquad\text{para todos }x,y\in D.
$$

La constante $L$ puede depender de la función y del dominio, pero se fija antes de elegir el par y debe servir para todos sus elementos. La estimación también incluye $x=y$, donde ambos miembros valen cero; formularla sin cocientes evita dividir por esa distancia nula. Si $0\le L<1$, expresa contracción; si $L=1$, prohíbe expansión, aunque algunas distancias puedan disminuir. Una muestra de pares comprueba esos casos particulares y deja pendiente la afirmación universal.

Por la desigualdad triangular, $|x|\le|x-y|+|y|$ y $|y|\le|x-y|+|x|$. Restando obtenemos

$$
\bigl||x|-|y|\bigr|\le|x-y|.
$$

Así $x\mapsto|x|$ tiene cota de expansión uno. Esa cota es óptima: las entradas cero y uno conservan distancia uno. Sin embargo, las entradas $x$ y $-x$ comparten salida. Un control superior limita cuánto pueden separarse las salidas y permite que dos de ellas colapsen en una sola.

Para $q(x)=x^2$,

$$
|q(x)-q(y)|=|x-y|\,|x+y|.
$$

La fórmula contiene un factor variable $|x+y|$. Si el dominio es $[-R,R]$ con $R>0$, la triangular da $|x+y|\le|x|+|y|\le2R$. Al sustituir, obtenemos $|q(x)-q(y)|\le2R|x-y|$ para todos los pares del intervalo. La restricción del dominio proporciona la misma cota para ese factor antes de conocer las entradas.

En toda la recta no existe tal cota finita. Recibamos cualquier $L\ge0$ propuesto y elijamos después $x=L+1$, $y=L+2$. Las entradas distan uno y sus cuadrados distan $(L+2)^2-(L+1)^2=2L+3>L$, contra la estimación. Como el par se construye ante cualquier constante, refuta la existencia de una cota global. El argumento es algebraico y no utiliza derivadas.

Si además existe $c>0$ con

$$
c|x-y|\le|f(x)-f(y)|\qquad(x,y\in D),
$$

entonces $f$ es inyectiva. En efecto, si dos salidas coinciden, el lado derecho es cero y obliga a $c|x-y|=0$; la positividad de $c$ da $x=y$. Para construir la inversa declaramos codominio $f[D]$, que contiene exactamente las salidas con entrada, y obtenemos $h:f[D]\to D$. Dado cualquier par $u,v\in f[D]$, sus entradas únicas $x=h(u)$, $y=h(v)$ satisfacen $c|h(u)-h(v)|\le|u-v|$. Dividir por $c>0$ da $|h(u)-h(v)|\le|u-v|/c$. La cota inferior original se convierte en una cota superior de la recuperación; la inversa sólo se evalúa en la imagen, aunque el codominio original fuese mayor.

Si $f:D\to E\subseteq\mathbb R$ tiene cota de expansión $L$ y $g:E\to\mathbb R$ tiene cota $M$, las salidas intermedias $f(x),f(y)$ pertenecen al dominio donde se aplica la segunda estimación. Por ello,

$$
|g(f(x))-g(f(y))|\le M|f(x)-f(y)|\le ML|x-y|.
$$

Los factores se multiplican: la segunda etapa actúa sobre una distancia ya controlada por la primera. Si uno vale cero, la composición tiene cota cero y las mismas desigualdades siguen siendo válidas. Estas estimaciones se han obtenido comparando valores mediante álgebra; no hemos invocado una teoría posterior de límites o continuidad.

### Ejercicios de la sección 12.7

#### Ejercicio 31. La mejor escala afín

[]{#MA-EX-ANM-01-012-031}

Para $h(x)=mx+c$ en toda $\mathbb R$, prueba que $|m|$ es la menor cota de expansión no negativa.

[]{#MA-SOL-ANM-01-012-031}

<details class="anm-solution">
<summary>Ver solución del ejercicio 31</summary>

La identidad $|h(x)-h(y)|=|m||x-y|$ muestra que $|m|$ sirve. Si $L$ es otra cota, usamos $x=0$, $y=1$ y obtenemos $|m|\le L$. Vale también para $m=0$: la menor cota no negativa es cero. La traslación no influye en el resultado.

Para demostrar que una cota es la menor hay que probar dos afirmaciones: que sirve para todos los pares y que cualquier otra cota debe ser al menos esa. La identidad exacta de distancias prueba la primera. El par cero y uno, separado por una unidad, convierte la condición de otra cota $L$ en $|m|\le L$. El caso $m=0$ queda incluido y alcanza la menor cota no negativa cero. La constante $c$ desaparece al restar salidas.

</details>

#### Ejercicio 32. Una cota sin reversibilidad

[]{#MA-EX-ANM-01-012-032}

Prueba que $f(x)=\max(x,0)$ tiene cota de expansión $1$ en $\mathbb R$ y no es inyectiva.

[]{#MA-SOL-ANM-01-012-032}

<details class="anm-solution">
<summary>Ver solución del ejercicio 32</summary>

Si ambas entradas son no negativas, la distancia de salidas es $|x-y|$; si ambas son no positivas, es cero. Si $x<0<y$, es $y\le y-x=|x-y|$; el caso invertido es simétrico. Los extremos cero están incluidos en los primeros casos. Así la cota es $1$. Pero $f(-1)=f(-2)=0$, por lo que no es inyectiva.

La verificación separa las regiones donde cambia la fórmula. En la región positiva la función es la identidad, en la negativa es constante cero y entre regiones la distancia de salidas sólo recoge la parte positiva de la separación original. En todos los casos no aumenta distancias. Sin embargo, muchas entradas negativas comparten la salida cero. Una cota superior de distancias limita la expansión, pero no impide colapsar entradas distintas; para eso haría falta otro argumento.

</details>

#### Ejercicio 33. La cota del cuadrado depende del radio

[]{#MA-EX-ANM-01-012-033}

Prueba que $2R$ es la menor cota de expansión del cuadrado en $[-R,R]$, $R>0$, sin derivadas.

[]{#MA-SOL-ANM-01-012-033}

<details class="anm-solution">
<summary>Ver solución del ejercicio 33</summary>

La factorización del texto prueba la cota $2R$. Para refutar $0\le L<2R$, elegimos $t=\min(R,(2R-L)/2)>0$, $x=R$, $y=R-t\in[0,R)$. El cociente de distancias, permitido porque $t>0$, es $x+y=2R-t>L$: si $t=(2R-L)/2$, el resultado es $(2R+L)/2>L$; si $t=R$, esta rama exige $L\le0$ y, como $L\ge0$, $L=0<R$. Se viola la cota. Por tanto ninguna menor sirve.

La cota superior viene de $|x+y|\le2R$. Para mostrar optimalidad, buscamos pares muy próximos al extremo $R$, cuyos cocientes de distancias son $x+y$ y se aproximan a $2R$. Ante cualquier $L<2R$, la elección de $t>0$ hace $2R-t>L$ sin salir del intervalo. No necesitamos un par que alcance exactamente el cociente $2R$: basta refutar cada factor menor con un par admisible. La prueba usa desigualdades algebraicas y no derivadas.

</details>

#### Ejercicio 34. Deshacer con control de distancia

[]{#MA-EX-ANM-01-012-034}

Supón $c|x-y|\le|f(x)-f(y)|\le L|x-y|$ para $x,y\in D$, con $0<c\le L$. Prueba las cotas de la inversa sobre la imagen.

[]{#MA-SOL-ANM-01-012-034}

<details class="anm-solution">
<summary>Ver solución del ejercicio 34</summary>

La cota inferior hace inyectiva a $f$, así que existe $h:f[D]\to D$. Para $u=f(x)$, $v=f(y)$, las desigualdades dan $c|h(u)-h(v)|\le|u-v|\le L|h(u)-h(v)|$. Dividiendo por constantes positivas, $(1/L)|u-v|\le|h(u)-h(v)|\le(1/c)|u-v|$. Todo par de la imagen tiene entradas únicas, así que las cotas cubren el dominio completo de $h$. No se exige sobreyectividad hacia el codominio original.

La cota inferior positiva impide que dos entradas distintas compartan salida, por lo que permite definir la inversa sobre $f[D]$. Sustituir $x=h(u)$ y $y=h(v)$ convierte las cotas originales en cotas para la distancia de entradas recuperadas. Al dividir, el factor superior original produce una cota inferior $1/L$ para la inversa, y el factor inferior original produce una cota superior $1/c$. Controlar expansión y colapso permite deshacer la transformación con control cuantitativo.

</details>

#### Ejercicio 35. Cota compuesta con restricción

[]{#MA-EX-ANM-01-012-035}

Sean $q:[-2,2]\to[0,4]$, $q(x)=x^2$, y $h:[0,4]\to\mathbb R$, $h(y)=3y-1$. Obtén una cota para $h\circ q$ y demuestra si es la menor posible.

[]{#MA-SOL-ANM-01-012-035}

<details class="anm-solution">
<summary>Ver solución del ejercicio 35</summary>

$q$ tiene cota $4$ y $h$ tiene escala exacta $3$, luego la composición tiene cota $12$. Si $0\le L<12$, tomamos $t=\min(1,(12-L)/6)>0$, $x=2$, $y=2-t\in[1,2)$. El cociente de distancias de salidas es $3(x+y)=12-3t$. Como $t\le(12-L)/6$, ese valor es al menos $(12+L)/2>L$. Se contradice la cota $L$. Así $12$ es la menor.

El factor cuatro del cuadrado en $[-2,2]$ se multiplica por la escala exacta tres de la segunda etapa, dando doce. Que el producto sea una cota no demuestra por sí solo optimalidad; ésta requiere otro argumento. Los pares cercanos al extremo dos tienen cociente de distancias $3(x+y)$ próximo a doce. La elección indicada mantiene ambas entradas en el dominio y supera cualquier factor menor propuesto. Así la cota compuesta resulta óptima en este caso concreto.

</details>

## 12.8. Representaciones y ventanas de control

[]{#MA-SEC-ANM-01-012-008}

Un dibujo del grafo coloca una entrada real en el eje horizontal y su salida en el vertical. Una transformación de una rejilla hace algo diferente: recibe un punto del plano entero y devuelve otro punto. Aunque ambos objetos puedan dibujarse en una hoja, sus tipos y el papel de las coordenadas no coinciden.

Para transformar una rejilla declaramos una función entre planos:

$$
T:\mathbb R^2\to\mathbb R^2,\qquad T(u,v)=(u+v,v).
$$

La salida $(u+v,v)$ es un único elemento de $\mathbb R^2$, con dos coordenadas; no son dos resultados alternativos. Para recuperar la entrada a partir de $(a,b)$, las ecuaciones $a=u+v$, $b=v$ dan $v=b$ y $u=a-b$. La candidata $S:\mathbb R^2\to\mathbb R^2$, $S(a,b)=(a-b,b)$, verifica $S(T(u,v))=(u,v)$ y $T(S(a,b))=(a,b)$. Así se prueba la inversa para todo punto, sin deducirla de la apariencia del dibujo.

En la horizontal $v=k$, los puntos se transforman en $(u+k,k)$: la segunda coordenada permanece fija y la primera recorre todos los reales, por lo que se obtiene toda la misma horizontal. En la vertical $u=j$, las salidas $(j+v,v)$ cumplen $a-b=j$. Recíprocamente, cualquier punto con $a-b=j$ proviene de $(j,b)$, así que se obtiene toda esa recta oblicua. El cuadrado de vértices $(0,0),(1,0),(1,1),(0,1)$ tiene vértices imagen $(0,0),(1,0),(2,1),(1,1)$. De hecho, toda su imagen se describe por $0\le b\le1$ y $b\le a\le b+1$: las desigualdades equivalen a que su entrada recuperada $(a-b,b)$ esté en $[0,1]^2$. Así se controla también el interior y la frontera del paralelogramo.

![T:R²→R² transporta el cuadrado unitario a un paralelogramo. Su inversa (a,b)↦(a−b,b) recupera las entradas; la escala depende de la dirección.](../../assets/books/anm/C12/C12-F06.svg){#fig-anm-c12-f06 fig-alt="Rejilla cuadrada antes y después de T(u,v)=(u+v,v), con cuadrado unitario sombreado y su paralelogramo imagen; horizontales conservadas, verticales oblicuas."}

La distancia euclídea entre $(a,b)$ y $(c,d)$ es $\sqrt{(a-c)^2+(b-d)^2}$. El segmento horizontal de $(0,0)$ a $(1,0)$ conserva longitud uno bajo $T$; el vertical de $(0,0)$ a $(0,1)$ pasa al segmento de $(0,0)$ a $(1,1)$ y tiene longitud $\sqrt2$. Un factor exacto común tendría que ser uno por el primer segmento y $\sqrt2$ por el segundo, lo que es imposible. Las fórmulas de las rectas y la inversa justifican el transporte de la rejilla entera; la muestra finita sólo lo representa.

Regresemos a $f:D\to E$, con $D,E\subseteq\mathbb R$. Para $A\subseteq D$ y $B\subseteq E$,

$$
f[A]\subseteq B\quad\Longleftrightarrow\quad A\subseteq f^{-1}[B].
$$

En la primera dirección, $x\in A$ implica $f(x)\in f[A]\subseteq B$ y, por definición, $x\in f^{-1}[B]$. En la vuelta, una salida $y\in f[A]$ tiene un testigo $x\in A$; la inclusión de entradas lo sitúa en $f^{-1}[B]$ y da $y=f(x)\in B$. La equivalencia expresa el mismo control en dos conjuntos distintos y no exige que $f$ sea invertible.

Con $x_0\in D$ y radios $r,\rho>0$, podemos aplicar esta equivalencia a

$$
U=D\cap B(x_0,r),\qquad V=E\cap B(f(x_0),\rho).
$$

La ventana $U$ sólo contiene entradas donde podemos evaluar $f$. Si, por ejemplo, $D=[0,\infty)$ y $x_0=0$, una bola real también contiene negativos y es necesario recortarla por $D$. De modo análogo, $V$ conserva las salidas permitidas por $E$. La equivalencia dice que transportar toda $U$ dentro de $V$ es lo mismo que incluir $U$ en $f^{-1}[V]$. Los radios son fijos: todavía no se ha formulado una condición de límite ni asegurado que la inclusión valga para una función arbitraria.

Para el cuadrado real, tomemos $x_0=1$, $r=1/4$ y $\rho=1$. La ventana de entrada es $U=(3/4,5/4)$ y la de salida $(0,2)$. Si $|x-1|<1/4$, la triangular da $|x+1|=|(x-1)+2|<9/4$. Factorizar la diferencia de cuadrados aprovecha precisamente ese control:

$$
|q(x)-q(1)|=|x-1|\,|x+1|<\frac14\frac94=\frac9{16}<1.
$$

La estimación vale para cada entrada de $U$, de modo que certifica $q[U]\subseteq(0,2)$ y, equivalentemente, $U\subseteq q^{-1}[(0,2)]$. La preimagen completa es $(-\sqrt2,0)\cup(0,\sqrt2)$; $U$ ocupa sólo una parte de ella. Para asegurar la inclusión basta una cota de todos sus puntos, sin calcular ni observar por separado infinitas evaluaciones.

La función de salto de §12.6 ofrece una selección de otro tipo. Como $s(0)=1$, consideremos $B(1,1/4)=(3/4,5/4)$. Ninguna entrada negativa sirve: su salida es negativa. Para las no negativas, la condición $3/4<x+1<5/4$ equivale a $-1/4<x<1/4$, y recortarla por $x\ge0$ deja $s^{-1}[B(1,1/4)]=[0,1/4)$.

La preimagen contiene cero, pero no es una vecindad real de cero. Para cualquier radio $r>0$, la entrada $-r/2$ pertenece a $B(0,r)$ y queda fuera de $[0,1/4)$. Por tanto ninguna bola real centrada en cero está contenida en esa selección. El universo importa: una vecindad relativa a un dominio restringido a los no negativos respondería a otra pregunta. Aquí seguimos en toda la recta, como en C04.

La comparación entre las dos ventanas termina en una diferencia precisa. En el cuadrado hemos encerrado las salidas de toda una bola alrededor de la entrada; la preimagen del salto contiene el centro y excluye todas las entradas negativas, por próximas que estén a él. Para estudiar cómo se comporta una función cerca de un punto tendremos que seguir controlando conjuntos completos de entradas próximas, conservando los dominios y los radios en cada afirmación.

![En el cuadrado, una estimación certifica que una ventana completa cabe en la preimagen. En el salto, la preimagen contiene el centro pero no es vecindad. La pertenencia y el margen alrededor del centro son datos distintos.](../../assets/books/anm/C12/C12-F07.svg){#fig-anm-c12-f07 fig-alt="Comparación de ventanas: para el cuadrado alrededor de uno, la ventana (3/4,5/4) está dentro de la preimagen de (0,2); para el salto, la preimagen de (3/4,5/4) es [0,1/4) y no rodea cero."}

### Ejercicios de la sección 12.8

#### Ejercicio 36. Transportar el cuadrado entero

[]{#MA-EX-ANM-01-012-036}

Para $T(u,v)=(u+v,v)$, calcula la imagen de $[0,1]^2$ mediante desigualdades en las coordenadas de salida $(a,b)$; prueba ambas inclusiones.

[]{#MA-SOL-ANM-01-012-036}

<details class="anm-solution">
<summary>Ver solución del ejercicio 36</summary>

La imagen es $P=\{(a,b):0\le b\le1,\ b\le a\le b+1\}$. Si $0\le u,v\le1$, entonces $b=v$ y $a=u+v$, de donde las desigualdades. Si $(a,b)\in P$, la entrada $(u,v)=(a-b,b)$ satisface $0\le u,v\le1$ y $T(u,v)=(a,b)$. Los vértices son los del paralelogramo mostrado en el texto; el argumento cubre también su interior y frontera.

**Retorno visual.** Véase [C12-F06](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f06), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Las desigualdades de salida no se obtienen sólo enviando los cuatro vértices. La coordenada $b=v$ queda entre cero y uno, y $a-b=u$ también queda entre cero y uno, lo que describe todos los puntos enviados. Para la vuelta, esas mismas condiciones garantizan que la entrada recuperada $(a-b,b)$ está en el cuadrado. Al comprobar las dos direcciones incluimos toda la región y su frontera, y no únicamente su contorno dibujado.

</details>

#### Ejercicio 37. Una rejilla no es un grafo escalar

[]{#MA-EX-ANM-01-012-037}

Explica por qué la imagen por $T$ de la recta $v=0$ puede ser una parte de un dibujo de rejilla y también el grafo de una función escalar, pero $T$ no es esa función escalar.

[]{#MA-SOL-ANM-01-012-037}

<details class="anm-solution">
<summary>Ver solución del ejercicio 37</summary>

Para $v=0$, $T(u,0)=(u,0)$, así que la imagen es la recta horizontal de pares $(a,0)$. Ese conjunto es el grafo de la función escalar $f:\mathbb R\to\mathbb R$, $f(a)=0$. Sin embargo, $T$ recibe pares $(u,v)$ y devuelve pares; $f$ recibe un real y devuelve cero. Su tipo, asignación y dominio difieren. Un mismo conjunto dibujado puede representar objetos en papeles distintos.

La recta horizontal es un conjunto de pares del plano. Puede describirse como imagen de un conjunto bajo una transformación del plano o como grafo de una función de una variable real. En el primer papel, cada punto de la recta inicial es una entrada completa de $T$; en el segundo, la primera coordenada es la entrada y la segunda la salida de la función constante. Coincidir en el conjunto representado no identifica las funciones que lo producen ni sus tipos.

</details>

#### Ejercicio 38. Ventana certificada para una afín

[]{#MA-EX-ANM-01-012-038}

Sea $f(x)=mx+c$ en $\mathbb R$, $x_0\in\mathbb R$ y $\rho>0$. Si $m\ne0$, calcula $f^{-1}[B(f(x_0),\rho)]$ y decide para qué $r>0$ vale $f[B(x_0,r)]\subseteq B(f(x_0),\rho)$. Trata $m=0$.

[]{#MA-SOL-ANM-01-012-038}

<details class="anm-solution">
<summary>Ver solución del ejercicio 38</summary>

Para $m\ne0$, la condición es $|m||x-x_0|<\rho$, por lo que la preimagen es $B(x_0,\rho/|m|)$. La inclusión de ventanas vale exactamente para $r\le\rho/|m|$: con esa condición todo punto de la bola menor satisface la desigualdad; si $r$ es mayor, la entrada $x=x_0+\rho/|m|$ está dentro de la primera bola pero su salida tiene distancia exactamente $\rho$, excluida de la segunda. Si $m=0$, la salida es siempre $c=f(x_0)$, la preimagen es toda $\mathbb R$ y cualquier $r>0$ sirve.

**Retorno visual.** Véase [C12-F07](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

El caso frontera $r=\rho/|m|$ sí funciona: pertenecer a una bola abierta da $|x-x_0|<r$, y al multiplicar se conserva una distancia de salida estrictamente menor que $\rho$. Si $r$ es mayor, el punto situado exactamente a distancia $\rho/|m|$ de $x_0$ está dentro de la ventana de entrada, pero su salida cae en la frontera excluida. Para $m=0$ no se divide por cero; se comprueba directamente que todas las salidas coinciden con el centro solicitado.

</details>

#### Ejercicio 39. Pertenencia sin vecindad

[]{#MA-EX-ANM-01-012-039}

Define $p:\mathbb R\to\mathbb R$ por $p(0)=0$ y $p(x)=1$ si $x\ne0$. Calcula $p^{-1}[B(0,1/2)]$ y prueba que no es vecindad de cero.

[]{#MA-SOL-ANM-01-012-039}

<details class="anm-solution">
<summary>Ver solución del ejercicio 39</summary>

$B(0,1/2)=(-1/2,1/2)$ contiene cero y no contiene uno. Por tanto la preimagen es $\{0\}$. Para cualquier $r>0$, el punto $r/2$ es distinto de cero y pertenece a $B(0,r)$, pero no a la preimagen. Ninguna bola positiva centrada en cero cabe en ella. Contener el centro no garantiza ser vecindad.

**Retorno visual.** Véase [C12-F07](analisis-para-matematicos-capitulo-12-que-hace-una-funcion.html#fig-anm-c12-f07), después del argumento completo: la figura permite reconocer el mecanismo y no sustituye la prueba.

Sólo la entrada cero produce una salida dentro de $(-1/2,1/2)$; todas las otras entradas producen uno, que queda fuera. El conjunto seleccionado es entonces un punto aislado. Para ser vecindad real de cero tendría que contener alguna bola de radio positivo, pero cualquier radio propuesto admite una entrada no nula todavía más cercana. El testigo $r/2$ muestra ese fallo para todos los radios, no sólo para una ventana particular.

</details>

#### Ejercicio 40. Reconstruir imagen desde todas las selecciones

[]{#MA-EX-ANM-01-012-040}

Sean $A\subseteq D$ y $C\subseteq E$. Supón que para todo $B\subseteq E$ se cumple $C\subseteq B$ si y sólo si $A\subseteq f^{-1}[B]$. Prueba que $C=f[A]$.

[]{#MA-SOL-ANM-01-012-040}

<details class="anm-solution">
<summary>Ver solución del ejercicio 40</summary>

Por la equivalencia del manuscrito, la segunda condición equivale a $f[A]\subseteq B$. Así $C$ y $f[A]$ tienen exactamente los mismos conjuntos que los contienen. Tomando $B=C$, la inclusión $C\subseteq C$ implica $f[A]\subseteq C$. Tomando $B=f[A]$, la inclusión $f[A]\subseteq f[A]$ implica $C\subseteq f[A]$. Las dos inclusiones dan igualdad. La caracterización recupera el transporte hacia delante a partir de su relación con todas las selecciones hacia atrás, incluidos los casos vacíos.

La hipótesis describe qué conjuntos contienen a $C$ y los compara con una selección de entradas. La equivalencia entre imagen y preimagen convierte esa selección en la condición de contener a $f[A]$. Para recuperar la igualdad elegimos dos conjuntos de prueba: $C$ y $f[A]$. Cada uno se contiene a sí mismo, y la equivalencia obliga a que contenga al otro. Las dos inclusiones concluyen la prueba sin escoger elementos concretos y abarcan también los casos vacíos.

</details>

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Ejercicios de este capítulo](#ejercicios-12)

[← Capítulo 11](analisis-para-matematicos-capitulo-11-series-como-laboratorio-de-convergencia.html) · [Capítulo 13 →](analisis-para-matematicos-capitulo-13-limites-de-funciones-control-de-dos-escalas.html)

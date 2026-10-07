---
title: "Soluciones — Capítulo 5"
content-id: MA-BCH-0181
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-005-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, sucesiones, eventualidad]
prerequisites: [MA-BCH-0083]
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "ANM-C05_SOLUCIONES.md, fuente canónica ANM; paquete C05 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)

## §5.1. Una sucesión es una función: índice y término

[]{#MA-SOL-ANM-01-005-001}

[]{#MA-EX-ANM-01-005-001}

### 1. Entrada, salida y repetición

La sucesión está dada por

$$
a_n=(n-2)^2-1.
$$

Sustituyendo cada índice obtenemos

$$
a_0=4-1=3,
$$

$$
a_1=1-1=0,
$$

$$
a_2=0-1=-1,
$$

$$
a_3=1-1=0,
$$

y

$$
a_5=9-1=8.
$$

Ahora separamos los tipos:

- $a$ es la función completa $a:\mathbb N\to\mathbb R$;
- $5$ es un índice, es decir, un elemento de $\mathbb N$;
- $a_5$ es el término real seleccionado por el índice $5$;
- $a(5)$ es otra notación para ese mismo término.

Por tanto,

$$
a_5=a(5)=8,
$$

pero el índice sigue siendo $5$ y el término sigue siendo $8$.

Además,

$$
a_1=0=a_3,
$$

aunque

$$
1\ne3.
$$

Esto no contradice la definición de función. Una función exige que cada entrada tenga una única salida; no exige que entradas distintas tengan salidas distintas. Aquí el índice $1$ tiene una sola imagen, $0$, y el índice $3$ también tiene una sola imagen, $0$.

[]{#MA-SOL-ANM-01-005-002}

[]{#MA-EX-ANM-01-005-002}

### 2. La misma regla no determina la misma función

En el índice o argumento $3$ las tres reglas producen el mismo valor:

$$
f(3)=2\cdot3+1=7,
$$

$$
a_3=2\cdot3+1=7,
$$

y

$$
c(3)=2\cdot3+1=7.
$$

Sin embargo, $f$, $a$ y $c$ no son iguales como funciones. Sus dominios son distintos:

$$
\operatorname{Dom}(f)=\mathbb R,
\qquad
\operatorname{Dom}(a)=\mathbb N,
\qquad
\operatorname{Dom}(c)=\mathbb Z.
$$

La fórmula algebraica no determina por sí sola el objeto función; el dominio forma parte de él.

Revisemos ahora las cuatro expresiones propuestas.

Como $-1\notin\mathbb N$, la expresión

$$
a_{-1}
$$

no está definida para la sucesión $a$.

En cambio, $-1\in\mathbb Z$, de modo que

$$
c(-1)=2(-1)+1=-1.
$$

Como $1/2\in\mathbb R$,

$$
f\!\left(\frac12\right)=2\cdot\frac12+1=2.
$$

Pero $1/2\notin\mathbb N$, así que

$$
a_{1/2}
$$

no está definido.

La relación correcta entre $f$ y $a$ es ésta: para todo $n\in\mathbb N$, ambos objetos pueden evaluarse en $n$ y dan el mismo valor,

$$
a_n=f(n)=2n+1.
$$

Eso no convierte a $a$ y $f$ en la misma función, porque sus dominios siguen siendo distintos.

[]{#MA-SOL-ANM-01-005-003}

[]{#MA-EX-ANM-01-005-003}

### 3. Tres registros para una misma sucesión

La definición depende del resto de $n$ al dividir por $3$. Para $0\le n\le8$ obtenemos:

| $n$ | $b_n$ |
|---:|---:|
| $0$ | $4$ |
| $1$ | $-1$ |
| $2$ | $0$ |
| $3$ | $4$ |
| $4$ | $-1$ |
| $5$ | $0$ |
| $6$ | $4$ |
| $7$ | $-1$ |
| $8$ | $0$ |

La lista ordenada correspondiente es

$$
(4,-1,0,4,-1,0,4,-1,0).
$$

Las mismas nueve evaluaciones pueden escribirse como

$$
\begin{aligned}
0&\longmapsto4,\\
1&\longmapsto-1,\\
2&\longmapsto0,\\
3&\longmapsto4,\\
4&\longmapsto-1,\\
5&\longmapsto0,\\
6&\longmapsto4,\\
7&\longmapsto-1,\\
8&\longmapsto0.
\end{aligned}
$$

La tabla muestra directamente qué índice corresponde a cada término. La lista conserva esa correspondencia porque sus posiciones están ordenadas como $0,1,2,\ldots$. Las asignaciones $n\mapsto b_n$ hacen explícita la evaluación de la función.

En los tres registros se conserva la asociación entre posición y valor. La repetición de $4$, $-1$ y $0$ no crea ambigüedad: cada índice sigue teniendo exactamente una salida. Por ejemplo,

$$
b_0=b_3=b_6=4,
$$

pero cada uno de los índices $0$, $3$ y $6$ tiene una imagen única.

[]{#MA-SOL-ANM-01-005-004}

[]{#MA-EX-ANM-01-005-004}

### 4. Una fórmula, tres errores de tipo

El argumento mezcla tres cuestiones diferentes: igualdad numérica, igualdad de objetos y pertenencia al dominio.

El primer error aparece en la frase

> «Como $c_3=3$, el índice $3$ y el término $c_3$ son el mismo objeto».

Es verdad que

$$
c_3=3,
$$

pero el primer $3$ cumple el papel de entrada y el segundo es el valor de salida. Más precisamente,

$$
3\in\mathbb N
$$

es el índice, mientras que

$$
c_3=3\in\mathbb R
$$

es el término. La coincidencia numérica no elimina la diferencia de tipo.

El segundo error consiste en afirmar que $g$ y $c$ son la misma función porque comparten la expresión $2x-3$. No lo son, pues

$$
g:\mathbb R\to\mathbb R
$$

y

$$
c:\mathbb N\to\mathbb R
$$

tienen dominios distintos. Lo que sí es correcto es que para cada $n\in\mathbb N$,

$$
g(n)=2n-3=c_n.
$$

El tercer error es introducir un supuesto término $c_{3.5}$. Como

$$
3.5\notin\mathbb N,
$$

$3.5$ no es un índice permitido de $c$. La expresión $g(3.5)$ sí está definida y vale

$$
g(3.5)=2(3.5)-3=4,
$$

pero ese valor pertenece a una evaluación de $g$ y no a un término de $c$ con índice $3.5$.

Una versión corregida del razonamiento es:

$$
c_3=3,
$$

de modo que el índice $3$ y el término correspondiente tienen el mismo valor numérico, aunque desempeñan papeles distintos. La función $g$ y la sucesión $c$ obedecen a la misma regla algebraica en los índices naturales, pero no son la misma función porque sus dominios difieren. Por eso $g(3.5)=4$ está definido, mientras que $c_{3.5}$ no lo está.

Finalmente, si

$$
u,v:\mathbb N\to\mathbb R,
$$

entonces para afirmar que son la misma sucesión debemos comprobar igualdad índice por índice:

$$
\boxed{
\forall n\in\mathbb N,
\quad
u_n=v_n.
}
$$

## §5.2. El orden de las visitas importa

[]{#MA-SOL-ANM-01-005-005}

[]{#MA-EX-ANM-01-005-005}

### 5. Los valores y los índices que los visitan

La definición depende del resto de $n$ módulo $4$.

Los valores posibles son únicamente $0$, $2$ y $-1$, y cada uno aparece: $a_0=0$, $a_1=2$ y $a_3=-1$. Por tanto,

$$
\boxed{a(\mathbb N)=\{-1,0,2\}.}
$$

Los índices que producen $0$ son exactamente los múltiplos de $4$:

$$
\boxed{I_a(0)=\{4k:k\in\mathbb N\}.}
$$

El valor $2$ aparece en los índices congruentes con $1$ o $2$ módulo $4$:

$$
\boxed{
I_a(2)
=
\{4k+1:k\in\mathbb N\}
\cup
\{4k+2:k\in\mathbb N\}.
}
$$

Finalmente,

$$
\boxed{I_a(-1)=\{4k+3:k\in\mathbb N\}.}
$$

Los tipos son distintos:

- $a$ es la función completa $\mathbb N\to\mathbb R$;
- $a(\mathbb N)$ es un subconjunto de $\mathbb R$;
- $I_a(2)$ es un subconjunto de $\mathbb N$;
- $a_6$ es un número real, y como $6\equiv2\pmod4$, vale $2$.

El conjunto de valores sólo dice **qué** números aparecen. Los conjuntos $I_a(x)$ dicen además **dónde** aparecen. Por ejemplo, de $a(\mathbb N)=\{-1,0,2\}$ no puede recuperarse que $0$ aparezca exactamente en los múltiplos de $4$ ni que $2$ ocupe dos clases de congruencia distintas.

[]{#MA-SOL-ANM-01-005-006}

[]{#MA-EX-ANM-01-005-006}

### 6. Recuperar la sucesión a partir de sus índices de aparición

Supongamos primero que

$$
a=b.
$$

Entonces, para todo $n\in\mathbb N$,

$$
a_n=b_n.
$$

Fijemos $x\in\mathbb R$. Para cualquier $n\in\mathbb N$,

$$
n\in I_a(x)
\iff
a_n=x
\iff b_n=x
\iff n\in I_b(x).
$$

Por extensionalidad,

$$
I_a(x)=I_b(x).
$$

Como $x$ era arbitrario,

$$
\forall x\in\mathbb R,\ I_a(x)=I_b(x).
$$

Probemos la conversa. Supongamos ahora que

$$
\forall x\in\mathbb R,\ I_a(x)=I_b(x).
$$

Fijemos un índice arbitrario $n\in\mathbb N$ y pongamos

$$
x=a_n.
$$

Entonces $n\in I_a(x)$. Por la igualdad de conjuntos de índices,

$$
n\in I_b(x),
$$

y, por definición de $I_b(x)$,

$$
b_n=x=a_n.
$$

Como esto vale para todo $n\in\mathbb N$,

$$
a=b.
$$

Hemos demostrado

$$
\boxed{
a=b
\iff
\forall x\in\mathbb R,\ I_a(x)=I_b(x).
}
$$

Para la segunda identidad, un real $x$ pertenece al conjunto de valores si y sólo si aparece en al menos un índice:

$$
\begin{aligned}
x\in a(\mathbb N)
&\iff \exists n\in\mathbb N:\ a_n=x\\
&\iff I_a(x)\ne\varnothing.
\end{aligned}
$$

Por tanto,

$$
\boxed{
a(\mathbb N)
=
\{x\in\mathbb R:I_a(x)\ne\varnothing\}.
}
$$

El conjunto de valores conserva solamente cuáles conjuntos $I_a(x)$ son vacíos o no vacíos. Conocer cada $I_a(x)$ conserva además todos los índices en los que aparece cada valor, y esa información basta incluso para reconstruir la sucesión completa.

[]{#MA-SOL-ANM-01-005-007}

[]{#MA-EX-ANM-01-005-007}

### 7. Dos existencias no alinean los índices

La igualdad de conjuntos de valores

$$
a(\mathbb N)=b(\mathbb N)
$$

implica dos afirmaciones correctas:

$$
\forall n\in\mathbb N\ \exists m\in\mathbb N:
\ a_n=b_m,
$$

y

$$
\forall m\in\mathbb N\ \exists n\in\mathbb N:
\ b_m=a_n.
$$

Estas fórmulas dicen que cada valor visitado por una sucesión aparece **en algún índice** de la otra.

Para concluir igualdad de sucesiones necesitaríamos algo distinto:

$$
\boxed{
\forall n\in\mathbb N:\ a_n=b_n.
}
$$

El error consiste en sustituir

$$
\forall n\ \exists m
$$

por una afirmación en la que el testigo $m$ queda forzado a ser el mismo índice $n$. La existencia de algún $m$ no garantiza $m=n$; además, el índice testigo puede depender del valor de $n$.

En el ejemplo

$$
a=(0,1,0,1,\ldots),
\qquad
b=(1,0,1,0,\ldots),
$$

ambas sucesiones tienen conjunto de valores $\{0,1\}$. Si $a_n=0$, ese valor aparece en $b$ en índices pares desplazados respecto de $a$; si $a_n=1$, también aparece en $b$ en otros índices. Por tanto las afirmaciones existenciales son verdaderas.

Sin embargo, en el índice $0$,

$$
a_0=0
\qquad\text{y}\qquad
b_0=1,
$$

de modo que

$$
a\ne b.
$$

La conclusión correcta es únicamente:

> si dos sucesiones tienen el mismo conjunto de valores, cada valor tomado por una de ellas es tomado también por la otra, quizá en índices distintos.

No puede recuperarse la igualdad índice por índice a partir de esa información.

[]{#MA-SOL-ANM-01-005-008}

[]{#MA-EX-ANM-01-005-008}

### 8. Ningún prefijo finito fija el orden completo

Fijemos $M\in\mathbb N$. Definimos

$$
a_n=n
$$

para todo $n\in\mathbb N$ y construimos $b$ intercambiando únicamente los valores situados en los índices $M+1$ y $M+2$:

$$
b_n=
\begin{cases}
M+2, & n=M+1,\\
M+1, & n=M+2,\\
n, & \text{en cualquier otro caso}.
\end{cases}
$$

Para todo $0\le n\le M$ no se ha modificado nada, así que

$$
a_n=b_n.
$$

La sucesión $a$ visita cada número natural exactamente una vez. La sucesión $b$ hace lo mismo: sólo hemos permutado las posiciones de $M+1$ y $M+2$. Por tanto,

$$
a(\mathbb N)=b(\mathbb N)=\mathbb N,
$$

y cada valor aparece exactamente una vez en ambas.

Pero en el índice $M+1$ tenemos

$$
a_{M+1}=M+1
$$

mientras que

$$
b_{M+1}=M+2.
$$

Luego

$$
\boxed{a\ne b.}
$$

Como $M$ era arbitrario, el acuerdo puede hacerse tan largo como queramos sin forzar igualdad global. Incluso conocer el conjunto completo de valores y cualquier cantidad finita prefijada de términos iniciales deja abierta la posibilidad de reorganizar valores en índices posteriores.

El ejemplo separa dos clases de información: el conjunto de valores registra qué números aparecen; la sucesión registra además en qué índice aparece cada uno.

[]{#MA-SOL-ANM-01-005-009}

[]{#MA-EX-ANM-01-005-009}

### 9. El mismo conjunto de valores, muchos ritmos de repetición

Para $r=1$ obtenemos ciclos de longitud $3$:

$$
b^{(1)}=(0,1,2,0,1,2,0,1,2,0,1,2,\ldots).
$$

Para $r=2$ los valores aparecen en bloques de longitud $2$:

$$
b^{(2)}=(0,0,1,1,2,2,0,0,1,1,2,2,\ldots).
$$

Para $r=3$ aparecen en bloques de longitud $3$:

$$
b^{(3)}=(0,0,0,1,1,1,2,2,2,0,0,0,\ldots).
$$

Fijemos ahora $r\ge1$. Por definición, todos los términos de $b^{(r)}$ pertenecen a $\{0,1,2\}$. Además, tomando $q=0$ y $j=0$ obtenemos

$$
b^{(r)}_0=0,
\qquad
b^{(r)}_r=1,
\qquad
b^{(r)}_{2r}=2.
$$

Por tanto los tres valores aparecen y no aparece ningún otro:

$$
\boxed{b^{(r)}(\mathbb N)=\{0,1,2\}.}
$$

Sean ahora $1\le r<s$. En la sucesión $b^{(r)}$, el primer bloque de ceros ocupa los índices

$$
0,1,\ldots,r-1,
$$

de modo que el índice $r$ ya pertenece al primer bloque de unos. Así,

$$
b^{(r)}_r=1.
$$

En cambio, para $b^{(s)}$ el primer bloque de ceros ocupa

$$
0,1,\ldots,s-1.
$$

Como $r<s$,

$$
b^{(s)}_r=0.
$$

Luego

$$
b^{(r)}_r\ne b^{(s)}_r,
$$

y por tanto

$$
\boxed{b^{(r)}\ne b^{(s)}}
$$

siempre que $r\ne s$.

Los índices en los que aparece $0$ forman, para cada ciclo $q$, el bloque

$$
\{3rq,3rq+1,\ldots,3rq+r-1\}.
$$

Por tanto,

$$
\boxed{
I_{b^{(r)}}(0)
=
\bigcup_{q\in\mathbb N}
\{3rq+j:0\le j\le r-1\}.
}
$$

Al variar $r$ cambia la longitud de los bloques y, con ella, el patrón de repetición y el orden local de las visitas. El conjunto de valores no registra ninguna de esas diferencias: para todos los parámetros colapsa al mismo conjunto $\{0,1,2\}$.

La familia muestra de forma paramétrica que conservar los valores visitados no equivale a conservar la organización indexada de esas visitas.

## §5.3. Ver una sucesión sin perder el índice

[]{#MA-SOL-ANM-01-005-010}

[]{#MA-EX-ANM-01-005-010}

### 10. Del conjunto de puntos a tres registros coordinados

Cada punto $(n,a_n)$ contiene simultáneamente el índice y el término. La tabla es, por tanto,

| $n$ | $a_n$ |
|---:|---:|
| $0$ | $3$ |
| $1$ | $1$ |
| $2$ | $3$ |
| $3$ | $-1$ |
| $4$ | $1$ |
| $5$ | $3$ |
| $6$ | $-1$ |
| $7$ | $1$ |

El bloque ordenado correspondiente es

$$
(a_0,a_1,\ldots,a_7)
=
(3,1,3,-1,1,3,-1,1).
$$

Sobre la recta real sólo aparecen tres posiciones. Para conservar la información indexada debemos añadir las etiquetas:

$$
-1:\ \{3,6\},
\qquad
1:\ \{1,4,7\},
\qquad
3:\ \{0,2,5\}.
$$

La igualdad $a_5=3$ aparece en el conjunto de puntos como

$$
(5,3)\in G_7,
$$

en la tabla como la fila cuya primera entrada es $5$, y en la recta etiquetada mediante la presencia del índice $5$ junto a la posición $3$.

Si borramos todas las etiquetas de índice, sólo queda el conjunto

$$
\{-1,1,3\}.
$$

Ese registro conserva qué valores aparecen en el bloque, pero ya no indica en qué posiciones aparecen, en qué orden se recorren ni cuántas veces aparece cada uno dentro de los ocho términos observados. La pérdida se produce precisamente al eliminar la asociación

$$
n\longmapsto a_n.
$$

[]{#MA-SOL-ANM-01-005-011}

[]{#MA-EX-ANM-01-005-011}

### 11. Una codificación fiel que no es la gráfica estándar

Los primeros valores son

$$
a_0=1,
\quad
a_1=-2,
\quad
a_2=3,
\quad
a_3=-4,
\quad
a_4=5.
$$

Por tanto, los primeros cinco puntos de la gráfica estándar son

$$
(0,1),\ (1,-2),\ (2,3),\ (3,-4),\ (4,5),
$$

y los primeros cinco puntos de $H$ son

$$
(1,1),\ (3,-2),\ (5,3),\ (7,-4),\ (9,5).
$$

El conjunto

$$
G=\{(n,a_n):n\in\mathbb N\}
$$

es la gráfica estándar porque su primera coordenada es literalmente el índice $n$ de la sucesión.

En $H$ la primera coordenada ha sido reemplazada por

$$
x=2n+1.
$$

La transformación es reversible sobre las coordenadas que aparecen en $H$: si conocemos $x$, recuperamos el índice mediante

$$
n=\frac{x-1}{2}.
$$

Por ejemplo, el término $a_3$ corresponde al punto cuya primera coordenada es

$$
2\cdot3+1=7.
$$

Como

$$
(7,-4)\in H,
$$

recuperamos

$$
a_3=-4.
$$

Así, $H$ conserva toda la asociación índice–término siempre que la regla de decodificación forme parte de la representación. No es, sin embargo, la gráfica estándar de $a$, porque sus puntos no tienen la forma $(n,a_n)$: la coordenada horizontal es $2n+1$, no $n$.

Si borramos la coordenada horizontal, en cualquiera de los dos registros quedan sólo las alturas

$$
\{1,-2,3,-4,5,-6,\ldots\}.
$$

Se pierde la correspondencia explícita entre cada índice y su valor. El hecho de que en este ejemplo los valores sean distintos no cambia el tipo de información eliminada: la proyección vertical ya no registra por sí misma la función $n\mapsto a_n$.

[]{#MA-SOL-ANM-01-005-012}

[]{#MA-EX-ANM-01-005-012}

### 12. Dos curvas distintas, una sola sucesión

Para todo $n\in\mathbb N$, el número $n$ es entero y por tanto

$$
\sin(\pi n)=0.
$$

De aquí se obtiene

$$
b_n=g(n)=n+\sin(\pi n)=n.
$$

Además,

$$
a_n=f(n)=n.
$$

Luego, para todo $n\in\mathbb N$,

$$
a_n=b_n.
$$

Como ambas sucesiones tienen el mismo dominio $\mathbb N$, la igualdad índice por índice implica

$$
\boxed{a=b.}
$$

Las funciones reales $f$ y $g$ sí son distintas. Por ejemplo, para

$$
x=\frac12
$$

tenemos

$$
f\!\left(\frac12\right)=\frac12,
$$

mientras que

$$
g\!\left(\frac12\right)
=
\frac12+\sin\!\left(\frac\pi2\right)
=
\frac32.
$$

El error del estudiante consiste en identificar las funciones de variable real $f,g:\mathbb R\to\mathbb R$ con sus restricciones al dominio discreto $\mathbb N$. Las curvas completas pueden ser distintas aunque coincidan en cada índice natural.

La gráfica discreta común de las dos sucesiones es

$$
\boxed{
\{(n,n):n\in\mathbb N\}.
}
$$

Los valores de $f(x)$ y $g(x)$ para $x\notin\mathbb N$ pertenecen a las funciones reales auxiliares, no a las sucesiones $a$ y $b$. Unir los puntos naturales mediante una curva añade información que la definición de sucesión no contiene.

[]{#MA-SOL-ANM-01-005-013}

[]{#MA-EX-ANM-01-005-013}

### 13. Cuánto puede cambiar una representación sin perder la sucesión

La sucesión comienza

$$
a=(2,0,1,2,0,1,2,0,1,\ldots).
$$

El registro 1 permite reconstruirla directamente: para cada índice $n$, el único punto de primera coordenada $n$ tiene segunda coordenada $a_n$.

El registro 2 también conserva toda la sucesión. Reordenar físicamente las filas no modifica los pares etiquetados

$$
(n,a_n).
$$

Mientras la columna del índice permanezca, podemos buscar la fila con etiqueta $n$ y recuperar su término. El orden de presentación de las filas no debe confundirse con el orden matemático de los índices.

El registro 3 también es fiel porque la codificación horizontal es reversible. El punto correspondiente al índice $n$ tiene primera coordenada

$$
x=n+10.
$$

Dado ese punto, la regla declarada permite recuperar

$$
n=x-10,
$$

y su segunda coordenada es precisamente $a_n$.

En cambio, el registro 4 es

$$
V=\{0,1,2\}.
$$

No conserva la asociación entre índices y valores. Por ejemplo, definamos

$$
b_n=
\begin{cases}
0, & n\equiv0\pmod 3,\\
1, & n\equiv1\pmod 3,\\
2, & n\equiv2\pmod 3.
\end{cases}
$$

Entonces

$$
b(\mathbb N)=\{0,1,2\}=a(\mathbb N),
$$

pero

$$
a_0=2\ne0=b_0.
$$

Por tanto,

$$
a\ne b.
$$

Los tres primeros registros admiten una reconstrucción exacta de la correspondencia

$$
n\longmapsto a_n;
$$

el cuarto no.

Un criterio general es:

> **Un cambio de representación conserva la sucesión cuando mantiene, de manera directa o mediante una codificación invertible declarada, información suficiente para recuperar cada par $(n,a_n)$. Si esa asociación deja de ser recuperable, la representación ha colapsado la sucesión a un objeto más pobre.**

## §5.4. Colas: olvidar un comienzo finito

[]{#MA-SOL-ANM-01-005-014}

[]{#MA-EX-ANM-01-005-014}

### 14. Tres objetos después del mismo corte

Como $4\equiv1\pmod3$, desde el índice $4$ los valores se repiten según el patrón

$$
-1,2,5,-1,2,5,\ldots
$$

La cola restringida es

$$
R=a|_{\mathbb N_{\ge4}}:\mathbb N_{\ge4}\to\mathbb R,
$$

y la cola reindexada es

$$
T=a^{\langle4\rangle}:\mathbb N\to\mathbb R.
$$

Las primeras seis asignaciones de $R$ son

$$
4\mapsto-1,
\quad
5\mapsto2,
\quad
6\mapsto5,
\quad
7\mapsto-1,
\quad
8\mapsto2,
\quad
9\mapsto5.
$$

Los primeros seis términos de $T$ son

$$
T=(-1,2,5,-1,2,5,\ldots).
$$

Por tanto,

$$
V_4=\{-1,2,5\}.
$$

Además,

$$
R(6)=a_6=5
$$

y

$$
T_2=a^{\langle4\rangle}_2=a_{4+2}=a_6=5.
$$

Los valores coinciden porque el nuevo índice $2$ de la cola reindexada corresponde al índice original $6$. Sin embargo, las funciones no son iguales: sus dominios son distintos,

$$
\operatorname{Dom}(R)=\mathbb N_{\ge4},
\qquad
\operatorname{Dom}(T)=\mathbb N.
$$

Finalmente, $R$ y $T$ son funciones con valores reales, mientras que $V_4$ es un subconjunto de $\mathbb R$. El conjunto $V_4$ ya no conserva ni índices ni repeticiones.

[]{#MA-SOL-ANM-01-005-015}

[]{#MA-EX-ANM-01-005-015}

### 15. Reparar una igualdad mal tipada

Introduzcamos

$$
R_N=a|_{\mathbb N_{\ge N}},
\qquad
T_N=a^{\langle N\rangle},
\qquad
V_N=\{a_n:n\ge N\}.
$$

Sus tipos son

$$
R_N:\mathbb N_{\ge N}\to\mathbb R,
$$

$$
T_N:\mathbb N\to\mathbb R,
$$

y

$$
V_N\subseteq\mathbb R.
$$

La primera igualdad escrita por el estudiante confunde dos funciones con dominios diferentes. La segunda intenta identificar una función con un conjunto de números reales. En ambos casos se han borrado tipos matemáticos esenciales.

La relación correcta entre las dos funciones usa el corrimiento

$$
\tau_N(k)=N+k.
$$

Para todo $k\in\mathbb N$,

$$
\begin{aligned}
\left(R_N\circ\tau_N\right)(k)
&=R_N(N+k)\\
&=a_{N+k}\\
&=a^{\langle N\rangle}_k\\
&=T_N(k).
\end{aligned}
$$

Como ambas funciones tienen dominio $\mathbb N$ y codominio $\mathbb R$ después de la composición, obtenemos

$$
\boxed{T_N=R_N\circ\tau_N.}
$$

Veamos ahora sus imágenes. Un real $x$ pertenece a $R_N(\mathbb N_{\ge N})$ si y sólo si existe $n\ge N$ tal que

$$
x=a_n.
$$

Por tanto,

$$
R_N(\mathbb N_{\ge N})=V_N.
$$

Análogamente, $x\in T_N(\mathbb N)$ si y sólo si existe $k\in\mathbb N$ con

$$
x=a_{N+k}.
$$

Como $N+k$ recorre exactamente $\mathbb N_{\ge N}$,

$$
T_N(\mathbb N)=V_N.
$$

Luego

$$
\boxed{
R_N(\mathbb N_{\ge N})
=
T_N(\mathbb N)
=
V_N.
}
$$

La igualdad correcta aparece al comparar **imágenes**, no al identificar objetos de tipos distintos.

[]{#MA-SOL-ANM-01-005-016}

[]{#MA-EX-ANM-01-005-016}

### 16. Una misma cola en cuatro registros

Para $5\le n\le10$ tenemos:

| $n$ | $a_n$ |
|---:|---:|
| $5$ | $-1$ |
| $6$ | $2$ |
| $7$ | $-1$ |
| $8$ | $3$ |
| $9$ | $-1$ |
| $10$ | $2$ |

Como parte inicial de la cola restringida, la misma información se escribe

$$
5\mapsto-1,
\quad
6\mapsto2,
\quad
7\mapsto-1,
\quad
8\mapsto3,
\quad
9\mapsto-1,
\quad
10\mapsto2.
$$

Al reindexar desde $5$, los nuevos índices son $k=0,1,\ldots$. Los primeros seis términos quedan

| $k$ | $a^{\langle5\rangle}_k=a_{5+k}$ |
|---:|---:|
| $0$ | $-1$ |
| $1$ | $2$ |
| $2$ | $-1$ |
| $3$ | $3$ |
| $4$ | $-1$ |
| $5$ | $2$ |

La gráfica discreta de este bloque de la cola reindexada contiene los puntos

$$
(0,-1),
(1,2),
(2,-1),
(3,3),
(4,-1),
(5,2).
$$

El patrón continúa periódicamente. Desde $n=5$ siguen apareciendo los tres valores $-1$, $2$ y $3$, de modo que

$$
\boxed{\{a_n:n\ge5\}=\{-1,2,3\}.}
$$

La tabla, la cola restringida y la cola reindexada conservan la organización de las visitas. El conjunto de valores tardíos sólo conserva cuáles números aparecen: pierde los índices, el orden de aparición y las repeticiones.

[]{#MA-SOL-ANM-01-005-017}

[]{#MA-EX-ANM-01-005-017}

### 17. Reconstruir el corte desde las nuevas posiciones

En una cola reindexada desde $N$, el nuevo índice $r$ corresponde al índice original

$$
N+r.
$$

Por tanto, la exigencia

$$
3\longleftrightarrow14
$$

obliga a

$$
N+3=14,
$$

de donde

$$
N=11.
$$

La segunda exigencia da

$$
N+9=20,
$$

y produce el mismo valor

$$
N=11.
$$

Así, las dos correspondencias son compatibles y el corte es único:

$$
\boxed{N=11.}
$$

En efecto,

$$
a^{\langle11\rangle}_3=a_{14},
\qquad
a^{\langle11\rangle}_9=a_{20}.
$$

Si añadimos

$$
4\longleftrightarrow16,
$$

la nueva condición exige

$$
N+4=16,
$$

o sea,

$$
N=12.
$$

Esto contradice el valor $N=11$ impuesto por las dos correspondencias anteriores. Por tanto, las tres exigencias no pueden satisfacerse simultáneamente.

En general,

$$
r\longleftrightarrow p
$$

y

$$
s\longleftrightarrow q
$$

significan

$$
p=N+r,
\qquad
q=N+s.
$$

Restando,

$$
p-r=N
\qquad\text{y}\qquad
q-s=N.
$$

Por tanto, una condición necesaria es

$$
p-r=q-s\ge0.
$$

Recíprocamente, si

$$
p-r=q-s\ge0,
$$

definimos

$$
N=p-r=q-s.
$$

Entonces $N\in\mathbb N$ y se cumplen

$$
N+r=p,
\qquad
N+s=q.
$$

Así,

$$
\boxed{
\exists N\in\mathbb N\text{ compatible con ambas correspondencias}
\iff
p-r=q-s\ge0.
}
$$

Cuando existe, el corte es necesariamente

$$
\boxed{N=p-r=q-s,}
$$

y por ello es único.

[]{#MA-SOL-ANM-01-005-018}

[]{#MA-EX-ANM-01-005-018}

### 18. Componer reindexaciones

Fijemos $j\in\mathbb N$. Por definición de cola reindexada,

$$
\left(a^{\langle N\rangle}\right)^{\langle K\rangle}_j
=
a^{\langle N\rangle}_{K+j}.
$$

Aplicando nuevamente la definición,

$$
a^{\langle N\rangle}_{K+j}
=
a_{N+(K+j)}.
$$

Por asociatividad de la suma,

$$
a_{N+(K+j)}=a_{(N+K)+j}.
$$

Pero el miembro derecho es precisamente

$$
a^{\langle N+K\rangle}_j.
$$

Hemos probado que, para todo $j\in\mathbb N$,

$$
\left(a^{\langle N\rangle}\right)^{\langle K\rangle}_j
=
a^{\langle N+K\rangle}_j.
$$

Ambos objetos son funciones $\mathbb N\to\mathbb R$. Por igualdad índice a índice,

$$
\boxed{
\left(a^{\langle N\rangle}\right)^{\langle K\rangle}
=
a^{\langle N+K\rangle}.
}
$$

La cadena

$$
j\longmapsto K+j\longmapsto N+K+j
$$

se interpreta así: $j$ es el índice de la segunda reindexación; $K+j$ es el índice correspondiente dentro de la primera cola reindexada; $N+K+j$ es el índice original en $a$.

Si $M\ge N$, entonces

$$
K=M-N\in\mathbb N.
$$

La identidad general produce

$$
\left(a^{\langle N\rangle}\right)^{\langle M-N\rangle}
=
a^{\langle N+(M-N)\rangle}
=
a^{\langle M\rangle}.
$$

Por tanto,

$$
\boxed{
a^{\langle M\rangle}
=
\left(a^{\langle N\rangle}\right)^{\langle M-N\rangle}.
}
$$

No se están eliminando dos bloques independientes. El segundo corte actúa **dentro de la primera cola ya reindexada**: descarta sus primeros $K$ términos, que corresponden exactamente a los índices originales $N,N+1,\ldots,N+K-1$. El efecto acumulado es un único corte original en $N+K$.

[]{#MA-SOL-ANM-01-005-019}

[]{#MA-EX-ANM-01-005-019}

### 19. Cuándo deja de encogerse el conjunto de valores tardíos

Definimos

$$
V_N(a)=\{a_n:n\ge N\}.
$$

Como $M\ge N$, todo índice $m\ge M$ satisface también $m\ge N$. Si $x\in V_M(a)$, existe $m\ge M$ tal que

$$
x=a_m.
$$

Entonces $m\ge N$, y por tanto $x\in V_N(a)$. Así,

$$
\boxed{V_M(a)\subseteq V_N(a).}
$$

Probemos ahora la equivalencia.

Supongamos primero que

$$
V_N(a)=V_M(a).
$$

Sea

$$
n\in\{N,N+1,\ldots,M-1\}.
$$

Como $n\ge N$, tenemos $a_n\in V_N(a)$. Por la igualdad de conjuntos,

$$
a_n\in V_M(a).
$$

Por definición de $V_M(a)$, existe $m\ge M$ tal que

$$
a_m=a_n.
$$

Por tanto,

$$
\forall n\in\{N,\ldots,M-1\}\;\exists m\ge M:\ a_n=a_m.
$$

Para la conversa, supongamos esta última condición y tomemos $x\in V_N(a)$. Existe $n\ge N$ con

$$
x=a_n.
$$

Hay dos casos.

Si $n\ge M$, entonces directamente

$$
x\in V_M(a).
$$

Si $N\le n<M$, la hipótesis proporciona un índice $m\ge M$ tal que

$$
a_m=a_n=x.
$$

De nuevo $x\in V_M(a)$. Hemos probado

$$
V_N(a)\subseteq V_M(a).
$$

Junto con la inclusión siempre válida de la primera parte, obtenemos

$$
\boxed{
V_N(a)=V_M(a)
\iff
\forall n\in\{N,\ldots,M-1\}\;\exists m\ge M:\ a_n=a_m.
}
$$

La condición dice: **ningún valor que aparezca en el bloque eliminado entre $N$ y $M-1$ desaparece definitivamente al mover el corte hasta $M$; cada uno reaparece en algún índice posterior**.

Si $M=N$, el bloque

$$
\{N,N+1,\ldots,M-1\}
$$

es vacío. La condición universal sobre ese bloque es vacuamente verdadera y, naturalmente,

$$
V_N(a)=V_N(a).
$$

Para una inclusión estricta, tomemos

$$
a=(0,1,1,1,1,\ldots),
\qquad N=0,
\qquad M=1.
$$

Entonces

$$
V_0(a)=\{0,1\},
\qquad
V_1(a)=\{1\},
$$

de modo que

$$
V_1(a)\subsetneq V_0(a).
$$

Para un caso de igualdad con $M>N$, tomemos

$$
a_n=(-1)^n,
\qquad N=0,
\qquad M=1.
$$

Tenemos

$$
V_0(a)=V_1(a)=\{-1,1\},
$$

porque el valor $a_0=1$ reaparece en índices pares posteriores a $1$.

Finalmente, la igualdad de conjuntos de valores tardíos no convierte las colas restringidas en la misma función. Si $M>N$, sus dominios son distintos:

$$
\mathbb N_{\ge N}\ne\mathbb N_{\ge M}.
$$

Además, aun cuando sus imágenes coincidan, los índices originales y el orden de las visitas siguen siendo información propia de cada cola. La igualdad

$$
V_N(a)=V_M(a)
$$

es una igualdad de subconjuntos de $\mathbb R$, no una igualdad de funciones restringidas.

## §5.5. «A partir de cierto momento»: propiedades eventuales

[]{#MA-SOL-ANM-01-005-020}

[]{#MA-EX-ANM-01-005-020}

### 20. Todos los testigos de una desigualdad eventual

La propiedad es

$$
4n-13\ge7.
$$

Si elegimos $N=5$ y tomamos un índice arbitrario $n\ge5$, entonces

$$
4n\ge20,
$$

y por tanto

$$
a_n=4n-13\ge7.
$$

Así, $N=5$ es un testigo.

Caractericemos ahora todos los testigos. Si $N\ge5$ y $n\ge N$, entonces también $n\ge5$, de modo que el argumento anterior da $a_n\ge7$. Por tanto todo $N\ge5$ funciona.

En cambio, si $N\le4$, el propio índice $n=N$ pertenece a la cola que comienza en $N$, pero

$$
a_N=4N-13\le4\cdot4-13=3<7.
$$

Luego ningún $N\le4$ es testigo. El conjunto completo de testigos es

$$
\boxed{\{N\in\mathbb N:N\ge5\}=\mathbb N_{\ge5}.}
$$

Para demostrar eventualidad bastaba exhibir un único elemento de este conjunto, por ejemplo $N=5$ o $N=100$. La definición exige existencia de un testigo, no minimalidad.

[]{#MA-SOL-ANM-01-005-021}

[]{#MA-EX-ANM-01-005-021}

### 21. Un intervalo fijo y el conjunto exacto de testigos

El denominador $n+2$ es positivo para todo $n\in\mathbb N$. Para la cota superior,

$$
2n+1<2n+4=2(n+2),
$$

de modo que

$$
\boxed{b_n<2}
$$

para todo $n\in\mathbb N$.

Para la cota inferior queremos

$$
\frac{2n+1}{n+2}>\frac32.
$$

Como $2(n+2)>0$, podemos multiplicar sin invertir la desigualdad:

$$
2(2n+1)>3(n+2).
$$

Esto equivale a

$$
4n+2>3n+6,
$$

y por tanto a

$$
n>4.
$$

Así, si $n\ge5$,

$$
\frac32<b_n<2.
$$

Por ello $N=5$ es un testigo de que $b_n\in I$ eventualmente.

Más aún, todo $N\ge5$ es testigo: si $n\ge N$, entonces $n\ge5$ y la doble desigualdad anterior vale. Si $N\le4$, podemos tomar $n=N$. En ese caso $n\le4$, luego

$$
b_n\le\frac32,
$$

por lo que $b_n\notin I$. Así,

$$
\boxed{
\{N:\forall n\ge N,\ b_n\in I\}
=
\mathbb N_{\ge5}.
}
$$

El orden de elecciones es esencial. Primero se fijó

$$
I=\left(\frac32,2\right).
$$

Después se buscó $N$. Una vez elegido el umbral, el índice $n\ge N$ quedó arbitrario y la prueba tuvo que cubrir todos esos índices.

[]{#MA-SOL-ANM-01-005-022}

[]{#MA-EX-ANM-01-005-022}

### 22. El conjunto de testigos y la cola reindexada

Por definición,

$$
P(n)\text{ ocurre eventualmente}
$$

significa

$$
\exists N\in\mathbb N\;\forall n\ge N:\ P(n).
$$

Pero afirmar que existe tal $N$ es exactamente afirmar que existe un elemento de

$$
W_P
=
\{N\in\mathbb N:\forall n\ge N,\ P(n)\}.
$$

Por tanto,

$$
\boxed{
P\text{ eventual}
\iff
W_P\ne\varnothing.
}
$$

Para la segunda afirmación, supongamos que $N\in W_P$ y $M\ge N$. Entonces

$$
\forall n\ge N:\ P(n).
$$

Tomemos un índice arbitrario $n\ge M$. Como

$$
n\ge M\ge N,
$$

tenemos $n\ge N$ y, por la propiedad de $N$, se cumple $P(n)$. Como esto vale para todo $n\ge M$,

$$
M\in W_P.
$$

Así, cuando $W_P$ no es vacío, queda cerrado hacia índices posteriores.

Probemos ahora la equivalencia reindexada. Si $N\in W_P$, entonces $P(n)$ vale para todo $n\ge N$. Para cualquier $k\in\mathbb N$, el índice

$$
n=N+k
$$

satisface $n\ge N$, luego $P(N+k)$ es verdadera.

Recíprocamente, supongamos

$$
\forall k\in\mathbb N:\ P(N+k).
$$

Sea $n\ge N$. Entonces

$$
k=n-N\in\mathbb N
$$

y $n=N+k$. Por hipótesis, $P(N+k)$ es verdadera; es decir, $P(n)$ es verdadera. Por tanto $N\in W_P$.

Hemos demostrado

$$
\boxed{
N\in W_P
\iff
\forall k\in\mathbb N:\ P(N+k).
}
$$

La parte derecha es la lectura de la misma cola después de reiniciar sus índices en $0$: cada nuevo índice $k$ representa el índice original $N+k$.

[]{#MA-SOL-ANM-01-005-023}

[]{#MA-EX-ANM-01-005-023}

### 23. Un millón de verificaciones no produce un cuantificador universal

Para que $N=1000$ sea un testigo, el estudiante debe demostrar

$$
\boxed{
\forall n\ge1000:\ P(n).
}
$$

Sin embargo, sólo verificó la afirmación en el conjunto finito

$$
\{1000,1001,\ldots,10^6\}.
$$

Faltan todos los índices mayores que $10^6$. La conclusión universal sobre la cola completa no se sigue de una cantidad finita de casos.

Un contraejemplo explícito es

$$
P(n):\quad n\le10^6.
$$

Esta propiedad es verdadera para cada índice entre $1000$ y $10^6$, exactamente como exige la comprobación del estudiante.

No obstante, $P$ no es eventual. En efecto, sea $N\in\mathbb N$ cualquier umbral propuesto. Tomemos

$$
n=N+10^6+1.
$$

Entonces $n\ge N$ y además $n>10^6$. Por tanto $P(n)$ es falsa. Como esto puede hacerse para cualquier $N$, no existe un umbral después del cual $P$ sea siempre verdadera.

El argumento original se repararía sustituyendo la lista finita de verificaciones por una razón general que cubra **todo** índice $n\ge1000$: por ejemplo, una desigualdad, una identidad o una definición por casos que permita deducir $P(n)$ a partir de la hipótesis arbitraria $n\ge1000$.

[]{#MA-SOL-ANM-01-005-024}

[]{#MA-EX-ANM-01-005-024}

### 24. Mover una única excepción mueve el umbral

Fijemos primero $r\in\mathbb N$. La única falla de la propiedad

$$
P_r(n):\quad d^{(r)}_n=1
$$

ocurre en el índice $r$.

Si elegimos

$$
N=r+1,
$$

y tomamos cualquier $n\ge N$, entonces $n\ge r+1$, de modo que $n\ne r$. Por definición,

$$
d^{(r)}_n=1.
$$

Luego $P_r$ es eventual.

Todo $N\ge r+1$ también es testigo por el mismo argumento. En cambio, si $N\le r$, el índice $n=r$ satisface $n\ge N$, pero

$$
d^{(r)}_r=0\ne1.
$$

Por tanto ningún $N\le r$ funciona y el conjunto exacto de testigos es

$$
\boxed{
\{N:\forall n\ge N,\ d^{(r)}_n=1\}
=
\mathbb N_{\ge r+1}.
}
$$

La propiedad no es global, porque falla precisamente en $n=r$.

Si reemplazamos $r$ por $r+10$, la excepción se desplaza diez lugares hacia la derecha y el conjunto de testigos pasa de

$$
\mathbb N_{\ge r+1}
$$

a

$$
\mathbb N_{\ge r+11}.
$$

Lo que no cambia es la arquitectura lógica: primero se fija el parámetro de la sucesión, después se elige un umbral y, finalmente, la propiedad debe verificarse para todo índice posterior.

[]{#MA-SOL-ANM-01-005-025}

[]{#MA-EX-ANM-01-005-025}

### 25. Tres lenguajes para la misma eventualidad

La primera afirmación significa, por definición,

$$
\exists N\in\mathbb N\;\forall n\ge N:\ a_n\in I.
$$

Para cada $N$, la imagen del segmento final es

$$
a(\mathbb N_{\ge N})
=
\{a_n:n\ge N\}.
$$

Por tanto,

$$
\forall n\ge N:\ a_n\in I
$$

es equivalente a

$$
a(\mathbb N_{\ge N})\subseteq I.
$$

Esto prueba la equivalencia entre 1 y 2.

Comparemos ahora 1 y 3. Si existe $N$ tal que $a_n\in I$ para todo $n\ge N$, entonces para cada $k\in\mathbb N$ el índice $N+k$ satisface $N+k\ge N$. Por tanto,

$$
a^{\langle N\rangle}_k
=
a_{N+k}
\in I.
$$

Recíprocamente, supongamos que para cierto $N$,

$$
\forall k\in\mathbb N:\ a^{\langle N\rangle}_k\in I.
$$

Sea $n\ge N$. Entonces $k=n-N\in\mathbb N$ y

$$
a_n
=
a_{N+k}
=
a^{\langle N\rangle}_k
\in I.
$$

Luego 3 implica 1. En consecuencia,

$$
\boxed{
1\iff2\iff3.
}
$$

Si $a_n\in I$ para todo $n\in\mathbb N$, podemos elegir inmediatamente $N=0$.

La conversa falla. Por ejemplo, toma

$$
a_0=0,
\qquad
a_n=2\quad(n\ge1),
$$

y

$$
I=(1,3).
$$

Entonces $a_0\notin I$, de modo que la propiedad no es global, pero para todo $n\ge1$ tenemos $a_n=2\in I$. Así, $N=1$ es un testigo de eventualidad.

El intervalo $I$ debe estar fijado antes de buscar $N$: la afirmación estudia si **una misma región previamente elegida** contiene todos los términos de alguna cola. Una vez fijados $I$ y $N$, sólo el índice recorre la cola.

La cadena conceptual puede escribirse así:

$$
\boxed{
\mathbb N_{\ge N}
\longleftrightarrow
\text{cola desde }N
\longleftrightarrow
\forall n\ge N
\longleftrightarrow
\text{propiedad eventual}.
}
$$

La cola reindexada expresa la misma estructura sustituyendo cada índice original $n\ge N$ por $k=n-N$.

## §5.6. Eventualmente no significa infinitas veces

[]{#MA-SOL-ANM-01-005-026}

[]{#MA-EX-ANM-01-005-026}

### 26. El conjunto de ocurrencias visto desde cada cola

Por definición,

$$
A_P=\{n\in\mathbb N:P(n)\}.
$$

La propiedad $P$ ocurre infinitas veces si y sólo si

$$
\forall N\in\mathbb N\;\exists n\ge N:\ P(n).
$$

Para un $N$ fijo, afirmar que existe $n\ge N$ con $P(n)$ equivale a afirmar que existe un índice perteneciente simultáneamente a $A_P$ y a $\mathbb N_{\ge N}$. Por tanto,

$$
\exists n\ge N:\ P(n)
\iff
A_P\cap\mathbb N_{\ge N}\ne\varnothing.
$$

Como la equivalencia vale para cada $N$,

$$
\boxed{
P\text{ ocurre infinitas veces}
\iff
\forall N:\ A_P\cap\mathbb N_{\ge N}\ne\varnothing.
}
$$

Análogamente, $P$ ocurre eventualmente si y sólo si existe $N$ tal que

$$
\forall n\ge N:\ P(n).
$$

Esto significa exactamente que cada elemento de $\mathbb N_{\ge N}$ pertenece a $A_P$; es decir,

$$
\boxed{
P\text{ ocurre eventualmente}
\iff
\exists N:\ \mathbb N_{\ge N}\subseteq A_P.
}
$$

Supongamos ahora que $P$ es eventual. Existe $N_0$ con

$$
\mathbb N_{\ge N_0}\subseteq A_P.
$$

Tomemos un umbral arbitrario $N$. El índice

$$
n=N+N_0
$$

satisface $n\ge N$ y $n\ge N_0$. Por tanto,

$$
n\in\mathbb N_{\ge N}\cap\mathbb N_{\ge N_0}
$$

y, como $\mathbb N_{\ge N_0}\subseteq A_P$,

$$
n\in A_P\cap\mathbb N_{\ge N}.
$$

Así, toda cola corta a $A_P$, de modo que $P$ ocurre infinitas veces.

La diferencia entre las dos condiciones es estructural. La eventualidad exige una inclusión completa:

$$
\mathbb N_{\ge N_0}\subseteq A_P.
$$

Desde $N_0$ no queda ningún fallo. En cambio, «infinitas veces» sólo exige

$$
A_P\cap\mathbb N_{\ge N}\ne\varnothing
$$

para cada $N$. Puede haber muchos índices de la cola que no pertenezcan a $A_P$; basta con que siempre sobreviva alguna nueva ocurrencia más allá del corte. Por eso esta segunda condición permite fallos arbitrariamente tardíos.

[]{#MA-SOL-ANM-01-005-027}

[]{#MA-EX-ANM-01-005-027}

### 27. Apariciones arbitrariamente tardías no llenan una cola

La afirmación correcta de que $P$ ocurre infinitas veces es

$$
\boxed{
\forall N\in\mathbb N\;\exists n\ge N:\ n=2^k
\text{ para algún }k\in\mathbb N.
}
$$

Fijemos un umbral arbitrario $N$. Podemos tomar

$$
n=2^{N+1}.
$$

Entonces $n$ es una potencia de $2$. Además,

$$
2^{N+1}\ge N
$$

para todo $N\in\mathbb N$, de modo que $n\ge N$. Hemos construido una ocurrencia de $P$ después de cualquier corte; por tanto $P$ ocurre infinitas veces.

El estudiante transforma indebidamente

$$
\forall N\;\exists n\ge N:\ P(n)
$$

en

$$
\exists N\;\forall n\ge N:\ P(n).
$$

En la primera fórmula, el índice testigo $n$ puede depender del umbral $N$ y sólo se exige **alguna** ocurrencia posterior. En la segunda debe existir un único corte después del cual **todos** los índices satisfagan $P$. No hay ninguna regla lógica que permita intercambiar esos cuantificadores.

Veamos directamente que $P$ no es eventual. Sea $N\in\mathbb N$ arbitrario y define

$$
m=2^{N+1}+1.
$$

Claramente $m\ge N$. Además,

$$
2^{N+1}<m<2^{N+2},
$$

porque $1<2^{N+1}$. Por tanto $m$ queda estrictamente entre dos potencias consecutivas de $2$ y no puede ser una potencia de $2$. Así, después de cualquier umbral aparece todavía un fallo de $P$.

La conclusión correcta es:

$$
\boxed{
P\text{ ocurre infinitas veces, pero no ocurre eventualmente}.
}
$$

El argumento original sí demostraba la existencia de potencias de $2$ arbitrariamente tardías; lo único falso era convertir esas apariciones aisladas en una cola completa de éxitos.

[]{#MA-SOL-ANM-01-005-028}

[]{#MA-EX-ANM-01-005-028}

### 28. Bloques cada vez más largos sin estabilización

Para $k=1$ tenemos un bloque verdadero en $n=1$ y un bloque falso en $n=2,3$. Para $k=2$, $P$ es verdadera en $4,5$ y falsa en $6,7,8$. Para $k=3$, es verdadera en $9,10,11$ y falsa en $12,13,14,15$. Para $k=4$, es verdadera en $16,17,18,19$ y falsa desde $20$ hasta $24$.

Así, entre $0$ y $20$ el patrón puede registrarse como

$$
\begin{array}{c|l}
\text{valor lógico} & \text{índices}\\
\hline
\text{falso} & 0\\
\text{verdadero} & 1\\
\text{falso} & 2,3\\
\text{verdadero} & 4,5\\
\text{falso} & 6,7,8\\
\text{verdadero} & 9,10,11\\
\text{falso} & 12,13,14,15\\
\text{verdadero} & 16,17,18,19\\
\text{falso} & 20.
\end{array}
$$

Probemos que $P$ ocurre infinitas veces. Sea $N\in\mathbb N$ arbitrario. Elijamos

$$
k=N+1
$$

y tomemos

$$
n=k^2.
$$

Entonces $n\ge N$ y, por definición,

$$
k^2\le n<k^2+k,
$$

de modo que $P(n)$ es verdadera. Como esto funciona para todo $N$, $P$ ocurre infinitas veces.

Para $\neg P$ usamos el mismo $k=N+1$ y tomamos

$$
m=k^2+k.
$$

Se cumple $m\ge N$ y además

$$
k^2+k\le m<(k+1)^2,
$$

pues

$$
k^2+k<k^2+2k+1=(k+1)^2.
$$

Por tanto $P(m)$ es falsa. Así, $\neg P$ también ocurre infinitas veces.

Como $\neg P$ ocurre infinitas veces, $P$ no puede ser eventual. Simétricamente, como $P$ ocurre infinitas veces, $\neg P$ no puede ser eventual. En consecuencia,

$$
\boxed{
P\text{ y }\neg P\text{ ocurren infinitas veces, y ninguna es eventual}.
}
$$

Veamos ahora la longitud de los bloques. El bloque verdadero correspondiente a $k$ contiene

$$
k^2,k^2+1,\ldots,k^2+k-1,
$$

exactamente $k$ índices. El bloque falso siguiente contiene

$$
k^2+k,k^2+k+1,\ldots,(k+1)^2-1,
$$

y su longitud es

$$
(k+1)^2-(k^2+k)=k+1.
$$

Dado $L\ge1$, basta elegir $k\ge L$. Entonces aparece un bloque verdadero de longitud al menos $L$ y un bloque falso de longitud al menos $L$.

El ejemplo destruye la inferencia

> «si una propiedad aparece en bloques consecutivos cada vez más largos, entonces termina por hacerse eventual».

La eventualidad no pide bloques finitos muy largos. Pide una **cola infinita completa** sin nuevas excepciones.

[]{#MA-SOL-ANM-01-005-029}

[]{#MA-EX-ANM-01-005-029}

### 29. Tricotomía del comportamiento tardío de una propiedad

Usaremos dos equivalencias de §5.6:

$$
\neg(P\text{ eventual})
\iff
\neg P\text{ ocurre infinitas veces},
$$

y, aplicando la misma equivalencia a $\neg P$,

$$
\neg(\neg P\text{ eventual})
\iff
P\text{ ocurre infinitas veces}.
$$

Primero probemos exclusión mutua.

Si $P$ ocurre eventualmente, entonces $\neg P$ **no** ocurre infinitas veces. Por tanto no puede darse la situación 3. Tampoco puede ocurrir $\neg P$ eventualmente, porque toda propiedad eventual ocurre infinitas veces; eso obligaría a que $\neg P$ ocurriera infinitas veces, contradicción. Así, la situación 1 excluye a 2 y 3.

El mismo argumento, intercambiando $P$ y $\neg P$, muestra que la situación 2 excluye a 1 y 3.

Finalmente, si ocurre la situación 3, entonces $\neg P$ ocurre infinitas veces, de modo que $P$ no es eventual; y $P$ ocurre infinitas veces, de modo que $\neg P$ no es eventual. Por tanto 3 excluye a 1 y 2.

Probemos ahora que alguna de las tres situaciones siempre ocurre.

- Si $P$ es eventual, estamos en la situación 1.
- Supongamos que $P$ no es eventual. Entonces, por la primera equivalencia, $\neg P$ ocurre infinitas veces.
  - Si $\neg P$ es eventual, estamos en la situación 2.
  - Si $\neg P$ no es eventual, la segunda equivalencia implica que $P$ ocurre infinitas veces. Como ya sabíamos que $\neg P$ ocurre infinitas veces, estamos en la situación 3.

Hemos demostrado que las tres situaciones son exhaustivas y mutuamente excluyentes. Por tanto,

$$
\boxed{
\text{exactamente una de 1, 2 o 3 ocurre.}
}
$$

Como corolario, al menos una de $P$ o $\neg P$ ocurre infinitas veces. En efecto, en la situación 1, $P$ es eventual y por tanto ocurre infinitas veces; en la situación 2, ocurre infinitas veces $\neg P$; y en la situación 3 ocurren infinitas veces ambas.

La tricotomía es más precisa que la división «eventual / no eventual» porque el caso no eventual se separa en dos mecanismos diferentes: o bien la negación termina estabilizándose, o bien continúan reapareciendo arbitrariamente tarde tanto éxitos como fallos.

[]{#MA-SOL-ANM-01-005-030}

[]{#MA-EX-ANM-01-005-030}

### 30. Cuando el testigo depende de otro parámetro

Fijemos primero $r\ge1$ y un umbral arbitrario $N\in\mathbb N$. Definimos

$$
n=r(N+1).
$$

Entonces $r\mid n$ por construcción. Además, como $r\ge1$,

$$
n=r(N+1)\ge N+1>N.
$$

Por tanto $n\ge N$. Hemos mostrado que, para cada $r$ fijo y para todo umbral $N$, existe un índice posterior divisible por $r$. Así,

$$
\boxed{
\forall r\ge1\;\forall N\in\mathbb N\;\exists n\ge N:\ r\mid n.
}
$$

El testigo obtenido es

$$
n(r,N)=r(N+1),
$$

y depende explícitamente de los dos datos elegidos antes.

Consideremos ahora la afirmación

$$
\forall N\in\mathbb N\;\exists n\ge N\;\forall r\ge1:\ r\mid n.
$$

Tomemos $N=1$. Si existiera un $n\ge1$ divisible por todo entero positivo, podríamos elegir

$$
r=n+1.
$$

Entonces la condición exigiría

$$
n+1\mid n.
$$

Pero un entero positivo estrictamente mayor que $n$ no puede dividir a $n$. Contradicción. Por tanto la afirmación es falsa.

La diferencia lógica está en la dependencia del testigo. En

$$
\forall r\;\forall N\;\exists n,
$$

el valor de $n$ puede cambiar cuando cambia $r$ o cuando cambia $N$. La fórmula no produce un mismo índice válido para todos los $r$. En cambio,

$$
\forall N\;\exists n\;\forall r
$$

exige que, después de fijar $N$, se encuentre **un único** $n$ que satisfaga simultáneamente todas las divisibilidades. Es una obligación mucho más fuerte.

Fijemos finalmente $m\ge1$ y restrinjamos la familia a

$$
1\le r\le m.
$$

Para un umbral arbitrario $N$, tomemos

$$
n=m!(N+1).
$$

Entonces $n\ge N$ y, para cada $r\in\{1,\ldots,m\}$, se tiene $r\mid m!$, luego

$$
r\mid n.
$$

Por tanto,

$$
\boxed{
\forall N\;\exists n\ge N\;\forall r\in\{1,\ldots,m\}:\ r\mid n.
}
$$

Al pasar de la familia infinita a una familia finita apareció un múltiplo común explícito, $m!$, que permite satisfacer simultáneamente todas las condiciones. El punto lógico no es que los testigos anteriores pudieran fusionarse automáticamente, sino que la nueva familia finita admite una construcción aritmética común que la familia de **todos** los enteros positivos no admite para ningún $n\ge1$.

## §5.7. Sincronizar colas y olvidar perturbaciones finitas

[]{#MA-SOL-ANM-01-005-031}

[]{#MA-EX-ANM-01-005-031}

### 31. Un solo corte para tres obligaciones

Tomamos

$$
N=\max\{4,9,6\}=9.
$$

Si $n\ge9$, entonces

$$
n\ge9\ge4,
\qquad
n\ge9,
\qquad
n\ge9\ge6.
$$

Por las tres hipótesis se siguen simultáneamente

$$
P(n),\qquad Q(n),\qquad R(n).
$$

Por tanto, $9$ es un testigo común para

$$
P\land Q\land R.
$$

Más generalmente, todo $M\ge9$ está garantizado como testigo común. En efecto, si $n\ge M\ge9$, entonces $n$ queda también por encima de $4$ y $6$, de modo que las tres propiedades están disponibles.

Así, a partir de la información dada, el conjunto de umbrales **garantizados** es

$$
\boxed{\mathbb N_{\ge9}.}
$$

Esto no significa que $9$ sea necesariamente el menor testigo real de la conjunción. Las hipótesis sólo dicen que $4$, $9$ y $6$ funcionan para las propiedades por separado; no dicen que sean sus umbrales mínimos. Podría ocurrir, por ejemplo, que $Q$ ya fuera verdadera desde $7$ aunque sólo se nos haya informado que vale desde $9$.

La función del máximo es lógica: sincroniza tres colas. No mejora las estimaciones disponibles; descarta suficiente prefijo para entrar en una cola en la que las tres obligaciones ya están simultáneamente activas.

[]{#MA-SOL-ANM-01-005-032}

[]{#MA-EX-ANM-01-005-032}

### 32. Intersecar conjuntos de testigos

Por definición,

$$
N\in W_{P_1\land\cdots\land P_k}
$$

si y sólo si

$$
\forall n\ge N:\ P_1(n)\land\cdots\land P_k(n).
$$

Una conjunción es verdadera exactamente cuando lo son todos sus componentes. Por tanto, la afirmación anterior equivale a

$$
\forall i\in\{1,\ldots,k\}\;\forall n\ge N:\ P_i(n).
$$

Eso significa precisamente

$$
N\in W_{P_i}
$$

para cada $i$. Luego

$$
\boxed{
W_{P_1\land\cdots\land P_k}
=
\bigcap_{i=1}^k W_{P_i}.
}
$$

Supongamos ahora que cada $P_i$ es eventual. Entonces cada $W_{P_i}$ es no vacío. Elijamos

$$
N_i\in W_{P_i}
$$

para $i=1,\ldots,k$ y definamos

$$
N=\max\{N_1,\ldots,N_k\}.
$$

Como $N\ge N_i$ para todo $i$, y los conjuntos de testigos son estables hacia índices posteriores, se tiene

$$
N\in W_{P_i}
$$

para cada $i$. Así,

$$
N\in\bigcap_{i=1}^k W_{P_i}
=
W_{P_1\land\cdots\land P_k}.
$$

La conjunción finita es, por tanto, eventual.

La finitud se usa al formar un máximo de la lista

$$
N_1,\ldots,N_k.
$$

Para una familia infinita, este argumento concreto ya no proporciona automáticamente un natural que domine todos los testigos. Nada de lo demostrado aquí autoriza a extender sin más la conclusión a una familia infinita.

[]{#MA-SOL-ANM-01-005-033}

[]{#MA-EX-ANM-01-005-033}

### 33. Encadenar coincidencias eventuales

Definimos

$$
M=\max\{N_{ab},N_{bc}\}.
$$

Sea $n\ge M$. Entonces

$$
n\ge M\ge N_{ab}
$$

y

$$
n\ge M\ge N_{bc}.
$$

Por las hipótesis,

$$
a_n=b_n
$$

y

$$
b_n=c_n.
$$

Por transitividad de la igualdad,

$$
a_n=c_n.
$$

Como esto vale para todo $n\ge M$, $a$ y $c$ coinciden eventualmente. Más aún, para todo $n\ge M$,

$$
\boxed{a_n=b_n=c_n.}
$$

Pasemos a las colas reindexadas. Para cualquier $k\in\mathbb N$, el índice original

$$
M+k
$$

satisface $M+k\ge M$. Por tanto,

$$
a_{M+k}=b_{M+k}=c_{M+k}.
$$

Usando la definición de cola reindexada,

$$
a^{\langle M\rangle}_k
=
a_{M+k},
$$

$$
b^{\langle M\rangle}_k
=
b_{M+k},
$$

y

$$
c^{\langle M\rangle}_k
=
c_{M+k}.
$$

Luego las tres funciones $\mathbb N\to\mathbb R$ coinciden índice por índice:

$$
\boxed{
a^{\langle M\rangle}
=
b^{\langle M\rangle}
=
c^{\langle M\rangle}.
}
$$

Nada de esto obliga a que las sucesiones originales sean iguales en los índices menores que $M$. La igualdad de funciones $a=b=c$ exigiría igualdad para **todo** $n\in\mathbb N$, no sólo sobre una cola común.

[]{#MA-SOL-ANM-01-005-034}

[]{#MA-EX-ANM-01-005-034}

### 34. «Cambiar finitos términos no cambia nada»

Las sucesiones no son iguales como funciones. Ya en el índice $0$,

$$
a_0=0
\ne
9=b_0.
$$

Por tanto,

$$
\boxed{a\ne b.}
$$

Sin embargo, desde el índice $1$ coinciden:

$$
\forall n\ge1:\ a_n=b_n=1.
$$

Así, $N_E=1$ es un testigo de coincidencia eventual.

Una propiedad sensible al prefijo es

$$
a_0=0.
$$

Es verdadera para $a$ y falsa para $b$. También cambiaría cualquier afirmación que mencione explícitamente el primer término.

En cambio, la propiedad término a término

$$
x=1
$$

aplicada a los términos es eventual en ambas sucesiones:

$$
\forall n\ge1:\ a_n=1
$$

y

$$
\forall n\ge1:\ b_n=1.
$$

El mismo umbral $N=1$ funciona para las dos.

La afirmación correcta es:

> Si dos sucesiones coinciden desde algún índice en adelante, entonces comparten las propiedades que dependen exclusivamente de una cola suficientemente tardía; en particular, los predicados término a término que son eventuales se transfieren entre ellas.

No se preservan necesariamente las propiedades que miran el prefijo modificado.

Por eso «los primeros términos son irrelevantes» es una frase incompleta. Los primeros términos son irrelevantes **para propiedades de cola**; pueden ser decisivos para propiedades globales o localizadas en índices iniciales.

[]{#MA-SOL-ANM-01-005-035}

[]{#MA-EX-ANM-01-005-035}

### 35. Mismos valores tardíos en cada corte, pero sin cola común

Tomemos

$$
a_n=(-1)^n
$$

y

$$
b_n=(-1)^{n+1}.
$$

Las sucesiones son

$$
a=(1,-1,1,-1,\ldots)
$$

y

$$
b=(-1,1,-1,1,\ldots).
$$

Fijemos un $N\in\mathbb N$ arbitrario. Entre los índices $N$ y $N+1$ hay uno par y uno impar. Por tanto, en la cola de $a$ aparecen tanto $1$ como $-1$. No aparece ningún otro valor, de modo que

$$
\{a_n:n\ge N\}=\{-1,1\}.
$$

El mismo argumento vale para $b$:

$$
\{b_n:n\ge N\}=\{-1,1\}.
$$

Así, para todo $N$,

$$
\boxed{
\{a_n:n\ge N\}
=
\{b_n:n\ge N\}
=
\{-1,1\}.
}
$$

No obstante, las sucesiones nunca coinciden en un mismo índice. Para todo $n$,

$$
b_n=(-1)^{n+1}=-(-1)^n=-a_n.
$$

Como $a_n\in\{-1,1\}$, se tiene

$$
a_n\ne b_n
$$

para todo $n\in\mathbb N$. En particular, dado cualquier $M$, basta elegir $n=M$ para obtener un índice $n\ge M$ en el que difieren.

Por tanto no existe una cola común y las sucesiones no coinciden eventualmente.

El contraejemplo muestra que incluso conocer **todos** los conjuntos de valores tardíos puede ser insuficiente: esos conjuntos registran qué valores aparecen después de cada corte, pero siguen sin registrar qué valor corresponde a cada índice. La coincidencia eventual exige precisamente esa información indexada.

[]{#MA-SOL-ANM-01-005-036}

[]{#MA-EX-ANM-01-005-036}

### 36. Sincronizar primero o transferir primero

Tenemos tres umbrales:

$$
N_E,
\qquad
N_P,
\qquad
N_Q.
$$

La coincidencia eventual proporciona

$$
\forall n\ge N_E:\ a_n=b_n,
$$

mientras que las dos propiedades sobre $a$ están disponibles desde $N_P$ y $N_Q$.

#### Ruta A: sincronizar en $a$ y luego transferir

Primero sincronizamos $P(a_n)$ y $Q(a_n)$ con

$$
N_A=\max\{N_P,N_Q\}.
$$

Entonces

$$
\forall n\ge N_A:\ P(a_n)\land Q(a_n).
$$

Ahora sincronizamos esta cola con la cola de coincidencia entre $a$ y $b$:

$$
M_A=\max\{N_E,N_A\}.
$$

Si $n\ge M_A$, entonces $a_n=b_n$ y además $P(a_n)\land Q(a_n)$. Como los predicados se aplican al mismo número real,

$$
P(b_n)\land Q(b_n).
$$

Por tanto la conjunción ocurre eventualmente en $b$.

#### Ruta B: transferir por separado y luego sincronizar

Transferimos primero $P$. Un umbral válido es

$$
M_P=\max\{N_E,N_P\}.
$$

Desde $M_P$ tenemos $a_n=b_n$ y $P(a_n)$, de donde $P(b_n)$.

Análogamente,

$$
M_Q=\max\{N_E,N_Q\}
$$

es un testigo para $Q(b_n)$.

Sincronizamos ambas propiedades ya transferidas mediante

$$
M_B=\max\{M_P,M_Q\}.
$$

Entonces, para todo $n\ge M_B$,

$$
P(b_n)\land Q(b_n).
$$

Comparemos los cortes. En la ruta A,

$$
M_A
=
\max\{N_E,\max\{N_P,N_Q\}\}.
$$

En la ruta B,

$$
M_B
=
\max\{\max\{N_E,N_P\},\max\{N_E,N_Q\}\}.
$$

Ambos números son simplemente el mayor de los tres umbrales originales:

$$
\boxed{
M_A=M_B=\max\{N_E,N_P,N_Q\}.
}
$$

La diferencia entre las rutas es organizativa, no matemática: ambas construyen una cola común en la que ya están activas la coincidencia y las dos propiedades.

Para una familia finita $P_1,\ldots,P_k$, con testigos $N_1,\ldots,N_k$ sobre $a$, basta tomar

$$
\boxed{
M=\max\{N_E,N_1,\ldots,N_k\}.
}
$$

Si $n\ge M$, entonces $a_n=b_n$ y cada $P_i(a_n)$ es verdadera. Por sustitución de iguales,

$$
P_i(b_n)
$$

para todo $i=1,\ldots,k$. Así, todas las propiedades se transfieren simultáneamente a una sola cola de $b$.

El argumento no sirve para una propiedad como

$$
a_0=0,
$$

porque esa afirmación no depende de una cola tardía: mira específicamente el índice $0$. La coincidencia eventual puede comenzar mucho después y no proporciona ninguna información sobre ese término inicial.

## §5.8. Captura eventual: la puerta a $\varepsilon$–$N$

[]{#MA-SOL-ANM-01-005-037}

[]{#MA-EX-ANM-01-005-037}

### 37. El último escape determina todos los testigos

Como $F$ es finito y no vacío, existe

$$
m=\max F.
$$

Para todo índice $n\ge m+1$ se tiene $n>m$. Por definición de máximo, ningún elemento de $F$ puede ser mayor que $m$, así que

$$
n\notin F.
$$

Por la definición de la sucesión,

$$
a_n=u\in U.
$$

Por tanto,

$$
\forall n\ge m+1:\ a_n\in U,
$$

y $N=m+1$ es un testigo de captura eventual.

Caractericemos ahora todos los testigos. Si $N\ge m+1$, el argumento anterior muestra que todo $n\ge N$ queda fuera de $F$, y por tanto $a_n=u\in U$. Así, todo $N\ge m+1$ pertenece a $W_U(a)$.

Recíprocamente, si $N\le m$, entonces el índice $m$ satisface

$$
m\ge N.
$$

Pero $m\in F$, luego

$$
a_m=v\notin U.
$$

Por tanto, ningún $N\le m$ es testigo. Hemos probado

$$
\boxed{
W_U(a)=\mathbb N_{\ge m+1}.
}
$$

La misma afirmación puede escribirse en lenguaje de valores tardíos:

$$
N\in W_U(a)
\iff
\{a_n:n\ge N\}\subseteq U.
$$

En este ejemplo, para todo $N\ge m+1$ el conjunto de valores tardíos es incluso

$$
\{a_n:n\ge N\}=\{u\}\subseteq U.
$$

El dato decisivo no es $|F|$, sino la posición del último escape. Un conjunto $F$ puede tener muchos elementos concentrados al principio o pocos elementos muy separados; la captura sólo puede comenzar después del mayor índice en que aparece el valor exterior $v$.

Si $F=\varnothing$, entonces $a_n=u\in U$ para todo $n\in\mathbb N$. En ese caso todo umbral funciona y

$$
\boxed{W_U(a)=\mathbb N.}
$$

[]{#MA-SOL-ANM-01-005-038}

[]{#MA-EX-ANM-01-005-038}

### 38. Cálculo con conjuntos de testigos de captura

Supongamos primero que $U\subseteq V$ y toma $N\in W_U(a)$. Entonces

$$
\forall n\ge N:\ a_n\in U.
$$

Como $U\subseteq V$, se sigue que

$$
\forall n\ge N:\ a_n\in V.
$$

Por tanto $N\in W_V(a)$ y

$$
\boxed{W_U(a)\subseteq W_V(a).}
$$

Para la intersección de dos conjuntos, fijemos $N\in\mathbb N$. Tenemos

$$
\begin{aligned}
N\in W_{U\cap V}(a)
&\iff \forall n\ge N:\ a_n\in U\cap V\\
&\iff \bigl(\forall n\ge N:\ a_n\in U\bigr)
     \text{ y }
     \bigl(\forall n\ge N:\ a_n\in V\bigr)\\
&\iff N\in W_U(a)\cap W_V(a).
\end{aligned}
$$

Por extensionalidad,

$$
\boxed{W_{U\cap V}(a)=W_U(a)\cap W_V(a).}
$$

El mismo argumento, repetido para una familia finita, da

$$
\boxed{
W_{\bigcap_{j=1}^kU_j}(a)
=
\bigcap_{j=1}^kW_{U_j}(a).
}
$$

Supongamos ahora que cada $W_{U_j}(a)$ es no vacío y elijamos

$$
N_j\in W_{U_j}(a).
$$

Definimos

$$
N=\max\{N_1,\ldots,N_k\}.
$$

Si $n\ge N$, entonces $n\ge N_j$ para cada $j$. Por la elección de $N_j$,

$$
a_n\in U_j
$$

para todos los $j$. Luego

$$
a_n\in\bigcap_{j=1}^kU_j.
$$

Así,

$$
N\in W_{\bigcap_{j=1}^kU_j}(a).
$$

Esto recupera, en lenguaje de conjuntos de testigos, el lema de sincronización.

Finalmente, si $U\cap V=\varnothing$ y una sucesión estuviera eventualmente en ambos, entonces $W_U(a)$ y $W_V(a)$ serían no vacíos. El argumento anterior produciría un testigo en

$$
W_{U\cap V}(a)=W_\varnothing(a).
$$

Pero ningún $N$ puede satisfacer

$$
\forall n\ge N:\ a_n\in\varnothing,
$$

porque el propio índice $n=N$ pertenece al segmento final. Contradicción.

Aquí aparecen dos niveles de objetos que no deben confundirse: $U,V$ son subconjuntos de $\mathbb R$ que contienen valores de la sucesión; $W_U(a),W_V(a)$ son subconjuntos de $\mathbb N$ que contienen umbrales válidos.

[]{#MA-SOL-ANM-01-005-039}

[]{#MA-EX-ANM-01-005-039}

### 39. Una cola común atrapada por dos regiones

Tomamos

$$
M=\max\{N_E,N_U,N_V\}.
$$

Sea $n\ge M$. Entonces, simultáneamente,

$$
n\ge N_E,
\qquad
n\ge N_U,
\qquad
n\ge N_V.
$$

Por la primera hipótesis,

$$
a_n=b_n.
$$

Por la segunda,

$$
a_n\in U,
$$

y por la tercera,

$$
b_n\in V.
$$

Como $a_n=b_n$, el mismo número real pertenece a ambos conjuntos. Por tanto,

$$
\boxed{a_n=b_n\in U\cap V}
$$

para todo $n\ge M$.

Se siguen dos conclusiones a la vez:

$$
\forall n\ge M:\ a_n\in U\cap V
$$

y

$$
\forall n\ge M:\ b_n\in U\cap V.
$$

Así, **ambas** sucesiones están eventualmente en $U\cap V$.

Si $U\cap V=\varnothing$, esto exigiría que para todo $n\ge M$ el valor común perteneciera al conjunto vacío, lo cual es imposible. Por tanto las tres hipótesis no pueden coexistir cuando $U$ y $V$ son disjuntos.

La coincidencia eventual es esencial. Sin ella no hay razón para que los valores capturados por $U$ y los capturados por $V$ tengan que ser los mismos. Por ejemplo, toma

$$
U=\{0\},
\qquad
V=\{1\},
$$

$$
a_n=0,
\qquad
b_n=1
\quad\text{para todo }n.
$$

Entonces $a$ está siempre en $U$ y $b$ está siempre en $V$, aunque

$$
U\cap V=\varnothing.
$$

No hay contradicción, porque

$$
a_n\ne b_n
$$

para todo $n$; las sucesiones no coinciden eventualmente.

El mecanismo reusable es, por tanto, una sincronización de **tres** obligaciones: cola común de $a$ y $b$, captura de $a$ en $U$ y captura de $b$ en $V$. Una vez comprimidas mediante el máximo, todas actúan sobre los mismos índices tardíos.

[]{#MA-SOL-ANM-01-005-040}

[]{#MA-EX-ANM-01-005-040}

### 40. Una batería finita de bolas sigue siendo una exigencia fija

Como

$$
r_*=\min\{r_1,\ldots,r_k\},
$$

tenemos

$$
r_*\le r_j
$$

para cada $j$. Por tanto, si $x\in B(0,r_*)$, entonces

$$
|x|<r_*\le r_j,
$$

y así $x\in B(0,r_j)$ para todo $j$. Esto prueba

$$
B(0,r_*)\subseteq\bigcap_{j=1}^kB(0,r_j).
$$

La inclusión inversa se obtiene usando un índice $j_*$ para el cual $r_{j_*}=r_*$. Si

$$
x\in\bigcap_{j=1}^kB(0,r_j),
$$

entonces en particular

$$
|x|<r_{j_*}=r_*,
$$

de modo que $x\in B(0,r_*)$. Así,

$$
\boxed{
\bigcap_{j=1}^kB(0,r_j)=B(0,r_*).
}
$$

Consideremos ahora

$$
c_n=\frac{r_*}{2}.
$$

Para todo índice $n$,

$$
|c_n|=\frac{r_*}{2}<r_*\le r_j
$$

para cada $j$. Por tanto,

$$
c_n\in B(0,r_j)
$$

para todo $n$ y para todo $j\in\{1,\ldots,k\}$. De hecho, el mismo testigo $N=0$ sirve para cada una de las $k$ capturas fijas.

Sin embargo,

$$
|c_n|=\frac{r_*}{2}>\frac{r_*}{4}
$$

para todo $n$. Luego

$$
c_n\notin B\!\left(0,\frac{r_*}{4}\right)
$$

para ningún índice. Esa bola más pequeña no captura ninguna cola de $c$.

La conclusión conceptual es importante. Una lista finita de radios prefijados puede comprimirse en una sola exigencia fija: la bola de menor radio $B(0,r_*)$. Superar esa batería finita sólo significa permanecer eventualmente dentro de **esa** región fija. No garantiza capacidad para responder a una exigencia nueva más pequeña, como $B(0,r_*/4)$.

El cambio que C06 introducirá no consiste simplemente en añadir muchas bolas a una lista. Cambiará el orden de las elecciones: primero podrá fijarse una tolerancia, y sólo después se permitirá elegir un umbral que responda a esa exigencia; a partir de ese umbral deberán obedecer todos los índices posteriores. C05, en cambio, sólo ha trabajado con conjuntos ya fijados antes de buscar el testigo.

Nada de lo anterior constituye todavía una definición de límite ni autoriza una notación de límite. En a)–d) sólo hemos usado una familia **finita** de conjuntos fijos y las reglas de captura eventual, intersección finita y sincronización ya disponibles en C05.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 5](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual.md) · [Ejercicios](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-5-sucesiones-y-comportamiento-eventual-microcontroles.md)

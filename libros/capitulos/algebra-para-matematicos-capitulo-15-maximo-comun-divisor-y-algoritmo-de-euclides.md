---
{
  "title": "Máximo común divisor y algoritmo de Euclides",
  "description": "Capítulo 15 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0190",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C15",
  "editorial-id": "MA-BCH-APM-01-015",
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
    "MA-BCH-0189"
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

En el capítulo anterior vimos que una ecuación como $18x+30y=c$ está sometida a restricciones aritméticas: cualquier divisor común de $18$ y $30$ debe dividir también a $c$ si existe una solución entera. Pero esa observación deja una pregunta abierta. Los números $18$ y $30$ tienen varios divisores comunes; entre ellos aparecen $1$, $2$, $3$ y $6$. ¿Debemos comprobarlos uno por uno? ¿Hay uno que contenga toda la información relevante?

La respuesta es el **máximo común divisor**. Sin embargo, el interés del concepto no está únicamente en elegir el mayor número de una lista de divisores. En este capítulo veremos que el mismo entero aparece desde cuatro puntos de vista distintos:

- como divisor común que concentra a todos los demás;
- como último resto no nulo de un algoritmo;
- como combinación lineal de los números iniciales;
- como generador de todas sus combinaciones lineales enteras.

Esa coincidencia es una de las primeras experiencias plenamente estructurales de la aritmética elemental. Un problema de divisibilidad, un procedimiento de cálculo y una ecuación diofántica terminan describiendo el mismo objeto.

La idea central será:

> **El máximo común divisor no es sólo un resultado que se calcula: es el entero positivo que organiza todos los divisores comunes y todas las combinaciones lineales de dos enteros.**

Para llegar a esa afirmación necesitaremos un segundo ingrediente: la **división con resto**. Ella permitirá reemplazar un par de enteros por otro más pequeño sin cambiar sus divisores comunes. La repetición de ese paso es el algoritmo de Euclides.

Todavía no utilizaremos factorización prima ni congruencias. Precisamente queremos descubrir cuánto puede obtenerse antes de disponer de esas herramientas.

***
## 15.1. Del divisor común decisivo al máximo común divisor {#apm-c15-s01}

Volvamos a la ecuación

$$
18x+30y=c.
$$

En C14 vimos que si $d$ divide simultáneamente a $18$ y a $30$, entonces $d$ divide a toda combinación lineal $18x+30y$. Por tanto, si la ecuación tiene una solución entera, necesariamente $d\mid c$.

Los divisores comunes positivos de $18$ y $30$ son

$$
1,2,3,6.
$$

No todos proporcionan una obstrucción igualmente fuerte. Saber que $2\mid c$ elimina ciertos valores de $c$, pero saber que $6\mid c$ elimina más. Además, si $6\mid c$, entonces automáticamente $1\mid c$, $2\mid c$ y $3\mid c$.

El número $6$ parece, por tanto, concentrar la información de los demás divisores comunes.

Esta observación sugiere dos maneras de describir al entero que buscamos.

La primera es cuantitativa:

> buscar el **mayor divisor común positivo**.

La segunda es estructural:

> buscar un divisor común positivo que sea divisible por **todo** divisor común.

En los enteros ambas perspectivas terminarán coincidiendo, pero no conviene confundirlas desde el principio. La segunda propiedad es más fuerte y será especialmente útil cuando estudiemos combinaciones lineales.

Por ejemplo, para $18$ y $30$ el número $6$ cumple:

$$
6\mid18,
\qquad
6\mid30,
$$

y, además, cada divisor común de $18$ y $30$ divide a $6$.

Queremos construir un procedimiento que encuentre ese número sin tener que listar primero todos los divisores. El algoritmo de Euclides hará exactamente eso.

***
## 15.2. Definición del MCD, signos y casos cero {#apm-c15-s02}

Sean $a,b\in\mathbb Z$, no ambos nulos. Llamaremos **máximo común divisor** de $a$ y $b$ al entero positivo $d$ que satisface las siguientes condiciones:

1. $d\mid a$;
2. $d\mid b$;
3. si $c$ divide simultáneamente a $a$ y a $b$, entonces $c\mid d$.

Cuando existe, escribimos

$$
d=\gcd(a,b).
$$

La tercera condición dice que $d$ es un divisor común **universal**: todo divisor común de $a$ y $b$ debe dividirlo.

Esta formulación contiene inmediatamente la idea de “máximo”. En efecto, si $c>0$ es un divisor común, entonces $c\mid d$. Como $d>0$, la propiedad de tamaño estudiada en C14 implica

$$
c\le d.
$$

Por tanto, un entero que satisface las tres condiciones anteriores es necesariamente el mayor divisor común positivo.

El recíproco —que el mayor divisor común positivo satisface siempre la propiedad universal— no se dará por supuesto. Lo justificaremos constructivamente en este capítulo mediante Euclides y Bézout. De este modo evitamos esconder dentro de la definición precisamente la estructura que queremos descubrir.

### Unicidad

Si $d$ y $e$ fueran dos enteros positivos que satisfacen la propiedad universal para el mismo par $(a,b)$, entonces, como $d$ es divisor común, tendríamos $d\mid e$; y como $e$ también es divisor común, tendríamos $e\mid d$. Al ser ambos positivos, la divisibilidad mutua implica

$$
d=e.
$$

Así, si el MCD existe, es único.

### Signos

Los signos no cambian los divisores comunes esenciales. Puesto que $c\mid a$ si y sólo si $c\mid(-a)$, los pares $(a,b)$, $(-a,b)$, $(a,-b)$ y $(-a,-b)$ tienen exactamente los mismos divisores comunes. Por tanto,

$$
\boxed{\gcd(a,b)=\gcd(|a|,|b|)}.
$$

Esta igualdad nos permitirá normalizar signos antes de ejecutar el algoritmo.

### El caso de un cero

Si $a\ne0$, entonces los divisores comunes de $a$ y $0$ son exactamente los divisores de $a$, porque todo entero no nulo divide a $0$. El entero positivo $|a|$ divide a $a$ y a $0$, y todo divisor de $a$ divide a $|a|$. Por consiguiente,

$$
\boxed{\gcd(a,0)=|a|}.
$$

Análogamente,

$$
\gcd(0,b)=|b|
$$

cuando $b\ne0$.

En este tomo dejamos $\gcd(0,0)$ **sin definir**. El par $(0,0)$ no contiene un divisor común positivo privilegiado por tamaño: todo entero no nulo divide a ambos componentes.

Para pares no nulos, todavía debemos demostrar que el entero especificado por nuestra definición existe siempre. Esa deuda se saldará con el algoritmo de Euclides.

### Nota pedagógica — Normalizar signos sin borrar los casos de borde

El MCD es positivo aunque sus argumentos tengan signos distintos. Pasar de $a$ a $|a|$ conserva exactamente sus divisores: $c\mid a$ equivale a $c\mid(-a)$. La normalización sirve para calcular el MCD; al reconstruir una identidad de Bézout hay que devolver los signos originales. Una identidad para $|a|,|b|$ no tiene automáticamente los mismos coeficientes para $a,b$.

**Control resuelto.** De $6=-84+3\cdot30$ obtenemos $6=(-84)\cdot1+30\cdot3$. Por tanto $\gcd(-84,30)=6$, pero el coeficiente de la primera entrada ahora es uno, no menos uno. Para $(-18,0)$, el MCD es dieciocho: éste divide ambas entradas y cualquier divisor común divide a $-18$, luego a dieciocho. El cero no obliga a que el MCD sea cero.

Si ambas entradas son cero, todos los enteros no nulos las dividen. No hay un divisor común positivo que absorba a todos los demás: para cualquier candidato $d>0$, el divisor común $2d$ no divide a $d$. En este capítulo $\gcd(0,0)$ queda sin definir. La ecuación $0x+0y=c$ se estudia directamente: todas las parejas enteras si $c=0$, ninguna si $c\ne0$. Esta clasificación no requiere introducir un MCD fuera de su dominio.

***
## 15.3. Divisores comunes y combinaciones lineales {#apm-c15-s03}

C14 estableció una propiedad que ahora se vuelve decisiva: si $d\mid a$ y $d\mid b$, entonces $d$ divide cualquier combinación lineal entera de $a$ y $b$.

Es decir, para todos $x,y\in\mathbb Z$,

$$
\boxed{d\mid a,
\quad d\mid b
\Longrightarrow
 d\mid(ax+by).}
$$

La demostración es inmediata desde los testigos. Si $a=du$ y $b=dv$, entonces

$$
ax+by=d(ux+vy),
$$

y $ux+vy$ es un entero.

Si $d=\gcd(a,b)$, obtenemos una consecuencia importante:

> **toda combinación lineal de $a$ y $b$ es múltiplo de su MCD.**

En símbolos,

$$
\gcd(a,b)\mid(ax+by)
$$

para todos $x,y\in\mathbb Z$.

Ésta es la dirección fácil de la relación entre MCD y combinaciones lineales. La dirección profunda será demostrar que el propio MCD puede obtenerse como una de esas combinaciones:

$$
\gcd(a,b)=ax_0+by_0
$$

para ciertos enteros $x_0,y_0$.

Antes de poder construir esos coeficientes necesitamos un mecanismo para reducir los números sin alterar sus divisores comunes.

Supongamos, por ejemplo, que $d$ divide a $84$ y a $30$. Entonces también divide a

$$
84-2\cdot30=24,
$$

y por tanto divide a

$$
30-24=6.
$$

Toda la información sobre los divisores comunes de $84$ y $30$ parece ir sobreviviendo mientras reemplazamos números grandes por diferencias más pequeñas. El algoritmo de Euclides formalizará esta intuición, pero para hacerlo de manera eficiente necesitamos dividir con resto.

***
## 15.4. El algoritmo de división {#apm-c15-s04}

La división con resto es una afirmación de existencia **y** unicidad.

### Teorema del algoritmo de división

Sean $a\in\mathbb Z$ y $b\in\mathbb Z$ con $b>0$. Entonces existen únicos enteros $q$ y $r$ tales que

$$
\boxed{a=bq+r,
\qquad
0\le r<b.}
$$

El entero $q$ se llama **cociente** y $r$ se llama **resto**.

Es importante que el teorema incluya enteros negativos. Por ejemplo,

$$
-17=5(-4)+3,
$$

por lo que al dividir $-17$ por $5$ el cociente canónico es $-4$ y el resto es $3$. La expresión

$$
-17=5(-3)-2
$$

es una igualdad correcta, pero no es la forma exigida por el algoritmo de división porque el resto debe satisfacer $0\le r<5$.

### Existencia: una aplicación del buen orden

Fijemos $a\in\mathbb Z$ y $b>0$. Consideremos el conjunto

$$
S=\{a-bk:k\in\mathbb Z,\ a-bk\ge0\}.
$$

El conjunto $S$ no es vacío. Si $a\ge0$, basta tomar $k=0$. Si $a<0$, podemos tomar, por ejemplo, $k=-|a|$; entonces

$$
a-b(-|a|)=a+b|a|\ge0.
$$

Como $S$ es un conjunto no vacío de enteros no negativos, el principio del buen orden garantiza que posee un elemento mínimo. Llamemos $r$ a ese mínimo. Por definición de $S$, existe un entero $q$ tal que

$$
r=a-bq,
$$

o equivalentemente,

$$
a=bq+r.
$$

Sólo falta probar que $r<b$. Supongamos, por contradicción, que $r\ge b$. Entonces

$$
r-b\ge0,
$$

y además

$$
r-b=a-bq-b=a-b(q+1).
$$

Por tanto, $r-b\in S$. Pero $r-b<r$, contradiciendo que $r$ era el menor elemento de $S$. Luego

$$
0\le r<b.
$$

La existencia queda demostrada.

### Unicidad

Supongamos que existen dos representaciones válidas:

$$
a=bq+r,
\qquad
0\le r<b,
$$

y

$$
a=bq'+r',
\qquad
0\le r'<b.
$$

Restando,

$$
b(q-q')=r'-r.
$$

El lado derecho satisface

$$
-(b-1)\le r'-r\le b-1,
$$

por lo que

$$
|r'-r|<b.
$$

Pero el lado izquierdo es múltiplo de $b$. El único múltiplo de $b$ cuyo valor absoluto es menor que $b$ es $0$. Así,

$$
r'-r=0,
$$

y entonces $r=r'$ y $q=q'$.

El algoritmo de división proporciona, por tanto, un reemplazo canónico de $a$ por un resto estrictamente menor que $b$. Ésta será la fuente del descenso que hace finito al algoritmo de Euclides.

***
## 15.5. Un paso euclidiano conserva los divisores comunes {#apm-c15-s05}

Supongamos que el algoritmo de división produce

$$
a=bq+r.
$$

La identidad puede reescribirse como

$$
r=a-bq.
$$

Estas dos formas permiten pasar de $(a,b)$ a $(b,r)$ y volver, usando únicamente combinaciones lineales.

### Lema del paso euclidiano

Los pares $(a,b)$ y $(b,r)$ tienen exactamente los mismos divisores comunes.

### Demostración

Supongamos primero que $d$ divide a $a$ y a $b$. Como

$$
r=a-bq,
$$

el cierre por combinaciones lineales implica $d\mid r$. Por tanto, $d$ divide a $b$ y a $r$.

Recíprocamente, supongamos que $d$ divide a $b$ y a $r$. Como

$$
a=bq+r,
$$

se sigue que $d\mid a$. Por tanto, $d$ divide a $a$ y a $b$.

Así, un entero no nulo es divisor común de $a$ y $b$ si y sólo si es divisor común de $b$ y $r$.

En consecuencia, ambos pares deben tener el mismo MCD siempre que lo expresemos con la normalización positiva:

$$
\boxed{\gcd(a,b)=\gcd(b,r)}.
$$

Como $r=a-qb$, también podemos escribir la forma más general

$$
\boxed{\gcd(a,b)=\gcd(b,a-qb)}.
$$

Esta identidad es el motor de Euclides. No dice simplemente que dos MCD resultan iguales por casualidad: dice que el **conjunto completo de divisores comunes permanece inalterado**.

Por ejemplo,

$$
\gcd(84,30)=\gcd(30,24)
$$

porque $24=84-2\cdot30$. Luego

$$
\gcd(30,24)=\gcd(24,6),
$$

porque $6=30-24$. Finalmente,

$$
\gcd(24,6)=6.
$$

Lo que en C14 aparecía como una técnica de reducción se ha convertido ahora en un principio algorítmico.

***
## 15.6. El algoritmo de Euclides {#apm-c15-s06}

Tomemos dos enteros positivos $a\ge b>0$. Aplicamos repetidamente el algoritmo de división:

$$
a=bq_1+r_1,
\qquad
0\le r_1<b.
$$

Si $r_1=0$, el proceso termina. Si no, dividimos $b$ por $r_1$:

$$
b=r_1q_2+r_2,
\qquad
0\le r_2<r_1.
$$

Si $r_2\ne0$, continuamos:

$$
r_1=r_2q_3+r_3,
\qquad
0\le r_3<r_2,
$$

y así sucesivamente.

Éste es el **algoritmo de Euclides**.

### Ejemplo: $662$ y $414$

Comenzamos con

$$
662=414\cdot1+248.
$$

Luego,

$$
414=248\cdot1+166,
$$

$$
248=166\cdot1+82,
$$

$$
166=82\cdot2+2,
$$

y finalmente

$$
82=2\cdot41+0.
$$

El último resto no nulo es $2$. Por tanto,

$$
\boxed{\gcd(662,414)=2.}
$$

El algoritmo no requiere listar los divisores de $662$ ni los de $414$. Reduce sistemáticamente el problema hasta llegar a un par cuya estructura es transparente.

Podemos leer la cadena de MCD asociada:

$$
\gcd(662,414)
=\gcd(414,248)
=\gcd(248,166)
=\gcd(166,82)
=\gcd(82,2)
=2.
$$

Cada igualdad está respaldada por el lema de la sección anterior.

Esto explica **qué** devuelve el procedimiento. Pero un algoritmo matemático exige responder dos preguntas adicionales:

1. ¿por qué debe terminar?;
2. ¿por qué el resultado final es correcto?

Son preguntas distintas y requieren argumentos distintos.

***
## 15.7. Por qué Euclides termina y por qué es correcto {#apm-c15-s07}

### Terminación

En una ejecución no trivial de Euclides, los restos satisfacen

$$
b>r_1>r_2>\cdots\ge0.
$$

Cada resto no nulo es un entero no negativo estrictamente menor que el anterior.

No puede existir una sucesión infinita estrictamente decreciente de enteros no negativos. Esto es una consecuencia del principio del buen orden: si existiera una colección infinita de restos sucesivos, el conjunto de sus valores tendría un mínimo; pero el paso siguiente produciría un entero no negativo aún menor.

Por tanto, en algún momento aparece un resto igual a $0$.

Así queda demostrada la **terminación**.

### Corrección

La terminación, por sí sola, no nos dice que el último resto no nulo sea el MCD. Para eso usamos el lema del paso euclidiano.

Cada división

$$
r_{k-2}=r_{k-1}q_k+r_k
$$

conserva exactamente los divisores comunes:

$$
\gcd(r_{k-2},r_{k-1})
=
\gcd(r_{k-1},r_k).
$$

Cuando el proceso termina, tenemos una última igualdad de la forma

$$
r_{n-2}=r_{n-1}q_n+0.
$$

Por tanto, el par terminal es $(r_{n-1},0)$. Su MCD es

$$
\gcd(r_{n-1},0)=|r_{n-1}|.
$$

Como todos los pasos conservaron los divisores comunes, ese mismo entero es el MCD del par inicial.

Por consiguiente:

> **El algoritmo de Euclides termina y su último resto no nulo es el máximo común divisor de los dos enteros iniciales.**

Esta demostración hace algo más: establece constructivamente la existencia del MCD para todo par de enteros no ambos nulos. Si los enteros tienen signos, primero pasamos a sus valores absolutos; si uno es cero, ya conocemos el resultado; si ambos son no nulos, Euclides produce el MCD.

Así queda saldada la deuda de existencia dejada en la sección 15.2.

### Nota pedagógica — Tres obligaciones distintas en una prueba algorítmica

Una ejecución exige comprobar **invariancia**, **terminación** e **identificación del resultado**. La igualdad $a=bq+r$ conserva los divisores comunes entre $(a,b)$ y $(b,r)$ para cualquier entero $q$. Esta propiedad no garantiza que los nuevos números sean menores. El descenso procede de elegir $0\le r<b$ con divisor positivo; el buen orden descarta una cadena infinita de restos positivos estrictamente decrecientes.

**Control resuelto.** Con $q=0$, $(19,7)$ pasa a $(7,19)$ y después vuelve a $(19,7)$. Ambas identidades son verdaderas y el MCD se conserva, pero la ejecución nunca termina. Con divisiones canónicas, $19=2\cdot7+5$, $7=5+2$, $5=2\cdot2+1$, $2=2\cdot1+0$. Aquí el descenso garantiza terminación. Al llegar a $(1,0)$, los divisores comunes son exactamente los divisores de uno: el invariante identifica el resultado como MCD del par inicial.

Un certificado independiente también puede cerrar la corrección: $1=3\cdot19-8\cdot7$. Uno divide las dos entradas y cualquier divisor común divide esta combinación. Verificarlo confirma el resultado, pero no demuestra que una regla defectuosa termine en otros ejemplos. Al auditar, indica qué afirmación falla en vez de llamar «incorrecta» a toda igualdad no canónica.

***
## 15.8. Sustitución hacia atrás y Euclides extendido {#apm-c15-s08}

El algoritmo de Euclides calcula el MCD, pero conserva más información de la que parece. Cada resto es una combinación lineal de los dos números anteriores y, por sustitución sucesiva, termina siendo una combinación lineal de los dos números originales.

Volvamos al ejemplo:

$$
662=414+248,
$$

$$
414=248+166,
$$

$$
248=166+82,
$$

$$
166=2\cdot82+2.
$$

Empezamos por la última igualdad no nula:

$$
2=166-2\cdot82.
$$

Como

$$
82=248-166,
$$

sustituimos:

$$
2
=166-2(248-166)
=3\cdot166-2\cdot248.
$$

Ahora usamos

$$
166=414-248:
$$

$$
2
=3(414-248)-2\cdot248
=3\cdot414-5\cdot248.
$$

Finalmente,

$$
248=662-414,
$$

de modo que

$$
2
=3\cdot414-5(662-414)
=8\cdot414-5\cdot662.
$$

Hemos obtenido la identidad

$$
\boxed{2=(-5)\cdot662+8\cdot414.}
$$

El MCD no sólo ha sido calculado: ha sido **certificado** como combinación lineal de los datos iniciales.

El procedimiento de llevar simultáneamente el control del MCD y de los coeficientes que lo expresan como combinación lineal recibe el nombre de **algoritmo de Euclides extendido**.

Una forma de organizarlo consiste en mantener, para cada resto $r_k$, coeficientes $s_k,t_k$ tales que

$$
r_k=s_ka+t_kb.
$$

Para iniciar esta recurrencia, fijamos $r_{-1}=a$ y $r_0=b$, con coeficientes $(s_{-1},t_{-1})=(1,0)$ y $(s_0,t_0)=(0,1)$. Así las dos identidades iniciales ya representan los datos. Se calcula la fila siguiente sólo mientras el divisor actual sea no nulo.

Si

$$
r_{k-2}=q_kr_{k-1}+r_k,
$$

entonces

$$
r_k=r_{k-2}-q_kr_{k-1},
$$

y por tanto los coeficientes satisfacen

$$
s_k=s_{k-2}-q_k s_{k-1}
$$

$$
t_k=t_{k-2}-q_k t_{k-1}.
$$

No necesitamos memorizar una tabla específica. Lo esencial es comprender el invariante: **cada resto permanece expresado como combinación lineal de los números originales**.

### Nota pedagógica — Unicidad del resto y libertad de los coeficientes

La división canónica tiene cociente y resto únicos bajo la condición $0\le r<b$. Esa unicidad no se transfiere a los coeficientes de Bézout. Una sustitución hacia atrás entrega una pareja; otras ejecuciones o la adición de una combinación nula pueden dar otra pareja válida.

**Control resuelto.** La identidad $6=-84+3\cdot30$ y la identidad $6=4\cdot84-11\cdot30$ son ambas ciertas. La diferencia de sus parejas es $(5,-14)$ y $84\cdot5+30(-14)=0$. Así, para todo $t\in\mathbb Z$,

$$
6=84(-1+5t)+30(3-14t).
$$

Los parámetros distintos dan primeras coordenadas distintas. La comprobación anterior prueba generación; que esta familia sea completa se justificará mediante el argumento de exhaustividad de [§15.14](algebra-para-matematicos-capitulo-15-maximo-comun-divisor-y-algoritmo-de-euclides.md#apm-c15-s14). No basta la no unicidad para concluir que una lista arbitraria contiene todas las representaciones.

Si una entrada es cero y la otra es $a\ne0$, en $ax+0y=|a|$ la coordenada $x$ está fijada en $a/|a|$, mientras $y$ es cualquier entero. También hay infinitas parejas. Lo único único en todas estas situaciones es el valor positivo del MCD, no el certificado que lo representa.

***
## 15.9. Identidad de Bézout {#apm-c15-s09}

La observación anterior se convierte en uno de los teoremas centrales de la aritmética elemental.

### Teorema de Bézout

Sean $a,b\in\mathbb Z$, no ambos nulos, y sea

$$
d=\gcd(a,b).
$$

Entonces existen enteros $x,y$ tales que

$$
\boxed{d=ax+by.}
$$

### Demostración mediante Euclides extendido

Si uno de los números es cero, el resultado es inmediato. Por ejemplo, si $b=0$ y $a\ne0$, entonces $d=|a|$ y podemos escribir $d=a(1)+0(0)$ cuando $a>0$, o $d=a(-1)+0(0)$ cuando $a<0$.

Supongamos ahora que ambos son no nulos. Tras normalizar signos, ejecutamos el algoritmo de Euclides. El último resto no nulo es $d$. Como cada resto se obtiene restando un múltiplo entero del resto anterior al precedente, una sustitución hacia atrás expresa $d$ como combinación lineal de los dos datos iniciales.

Así existen $x,y\in\mathbb Z$ con

$$
d=ax+by.
$$

### Los coeficientes no son únicos

Bézout afirma existencia, no unicidad.

Si

$$
d=ax_0+by_0,
$$

entonces para cualquier $t\in\mathbb Z$ tenemos

$$
a\left(x_0+\frac{b}{d}t\right)
+b\left(y_0-\frac{a}{d}t\right)
=d,
$$

porque los términos adicionales se cancelan:

$$
a\frac{b}{d}t-b\frac{a}{d}t=0.
$$

Como $d\mid a$ y $d\mid b$, los cocientes $a/d$ y $b/d$ son enteros.

En el ejemplo anterior,

$$
2=(-5)\cdot662+8\cdot414.
$$

Por tanto, además de $(-5,8)$, existen infinitos pares de coeficientes de Bézout.

### Cierre de la caracterización universal

Bézout permite ahora cerrar la relación entre la definición universal y la expresión “mayor divisor común positivo”. Si $d=\gcd(a,b)$, ya sabemos que $d$ es el mayor divisor común positivo.

Recíprocamente, supongamos que $m$ es el mayor divisor común positivo de $a$ y $b$. El algoritmo de Euclides produce un entero $d$ que satisface la propiedad universal y, por tanto, es un divisor común positivo. Como $m$ es el mayor, $d\le m$. Pero $m$ es divisor común y la propiedad universal de $d$ da $m\mid d$, de donde $m\le d$. Así $m=d$.

Por tanto, en los enteros las dos descripciones coinciden.

***
## 15.10. Todas las combinaciones lineales forman $d\mathbb Z$ {#apm-c15-s10}

La identidad de Bézout permite describir de una sola vez **todas** las combinaciones lineales de dos enteros.

Definamos

$$
L(a,b)=\{ax+by:x,y\in\mathbb Z\}.
$$

Sea $d=\gcd(a,b)$. Afirmamos que

$$
\boxed{L(a,b)=d\mathbb Z.}
$$

La igualdad de conjuntos exige demostrar dos inclusiones.

### Primera inclusión: $L(a,b)\subseteq d\mathbb Z$

Como $d\mid a$ y $d\mid b$, el número $d$ divide cualquier combinación lineal $ax+by$. Por tanto, cada elemento de $L(a,b)$ es un múltiplo de $d$:

$$
L(a,b)\subseteq d\mathbb Z.
$$

### Segunda inclusión: $d\mathbb Z\subseteq L(a,b)$

Por Bézout existen $x_0,y_0\in\mathbb Z$ tales que

$$
d=ax_0+by_0.
$$

Sea ahora $m\in d\mathbb Z$. Entonces existe $k\in\mathbb Z$ tal que

$$
m=dk.
$$

Multiplicando la identidad de Bézout por $k$,

$$
m
=k(ax_0+by_0)
=a(kx_0)+b(ky_0).
$$

Como $kx_0,ky_0\in\mathbb Z$, se tiene $m\in L(a,b)$. Por tanto,

$$
d\mathbb Z\subseteq L(a,b).
$$

Las dos inclusiones prueban la igualdad.

Este resultado condensa el capítulo:

> **las combinaciones lineales de $a$ y $b$ son exactamente los múltiplos de su MCD.**

Por ejemplo, como $\gcd(84,30)=6$,

$$
\{84x+30y:x,y\in\mathbb Z\}=6\mathbb Z.
$$

Esto significa dos cosas simultáneamente:

- ninguna combinación $84x+30y$ puede producir un entero que no sea múltiplo de $6$;
- todo múltiplo de $6$ puede producirse mediante alguna combinación $84x+30y$.

C14 había demostrado sólo la primera afirmación. Bézout proporciona la segunda.

***
## 15.11. Coprimalidad y criterio de Bézout {#apm-c15-s11}

Dos enteros $a$ y $b$, no ambos nulos, se llaman **coprimos** cuando

$$
\gcd(a,b)=1.
$$

La identidad de Bézout produce una caracterización especialmente útil.

### Criterio de Bézout para coprimalidad

$$
\boxed{
\gcd(a,b)=1
\iff
\exists x,y\in\mathbb Z:\ ax+by=1.
}
$$

### Demostración

Si $\gcd(a,b)=1$, Bézout garantiza enteros $x,y$ con

$$
1=ax+by.
$$

Recíprocamente, supongamos que existen $x,y\in\mathbb Z$ tales que

$$
ax+by=1.
$$

Sea $d$ un divisor común de $a$ y $b$. Entonces $d$ divide cualquier combinación lineal, y en particular

$$
d\mid1.
$$

Los únicos divisores de $1$ son $1$ y $-1$. Por tanto, el MCD positivo de $a$ y $b$ es $1$.

Esta caracterización transforma una afirmación sobre divisores en un **certificado explícito**.

Por ejemplo,

$$
35=2\cdot12+11,
$$

$$
12=1\cdot11+1.
$$

Sustituyendo,

$$
1=12-11=12-(35-2\cdot12)=3\cdot12-35.
$$

Así,

$$
1=(-1)\cdot35+3\cdot12,
$$

y por tanto

$$
\gcd(35,12)=1.
$$

La combinación que produce $1$ es más que una comprobación numérica: certifica que cualquier divisor común de los dos números debe ser una unidad $\pm1$.

***
## 15.12. Cancelación bajo coprimalidad {#apm-c15-s12}

En C14 vimos que la inferencia

$$
a\mid bc
\Longrightarrow
 a\mid c
$$

es falsa en general. Por ejemplo,

$$
6\mid2\cdot3,
$$

pero $6\nmid3$.

La identidad de Bézout revela una hipótesis que sí permite cancelar.

### Proposición de cancelación coprima

Sean $a,b,c\in\mathbb Z$, con $a\ne0$. Si

$$
\gcd(a,b)=1
$$

y

$$
a\mid bc,
$$

entonces

$$
\boxed{a\mid c.}
$$

### Demostración

Como $\gcd(a,b)=1$, existen $x,y\in\mathbb Z$ tales que

$$
ax+by=1.
$$

Multiplicamos por $c$:

$$
acx+bcy=c.
$$

El entero $a$ divide a $acx$. Además, por hipótesis $a\mid bc$, y por tanto $a\mid bcy$. Como $a$ divide a ambos sumandos del lado izquierdo, divide a su suma. Luego

$$
a\mid c.
$$

La hipótesis de coprimalidad es esencial. En el contraejemplo anterior,

$$
\gcd(6,2)=2\ne1.
$$

Por eso no puede aplicarse la proposición.

Este resultado prepara una propiedad que reaparecerá con especial fuerza cuando estudiemos números primos, pero todavía no necesitamos definirlos. Aquí todo se deduce de Bézout.

***
## 15.13. Criterio completo para $ax+by=c$ {#apm-c15-s13}

Estamos en condiciones de cerrar la pregunta dejada abierta en C14.

Sean $a,b,c\in\mathbb Z$ con $(a,b)\ne(0,0)$ y sea

$$
d=\gcd(a,b).
$$

### Teorema de solvencia diofántica lineal

La ecuación

$$
ax+by=c
$$

tiene una solución entera si y sólo si

$$
\boxed{d\mid c.}
$$

### Necesidad

Si $(x,y)$ es una solución, entonces

$$
c=ax+by.
$$

Como $d\mid a$ y $d\mid b$, se sigue que $d$ divide cualquier combinación lineal. Por tanto,

$$
d\mid c.
$$

Ésta era precisamente la obstrucción obtenida en C14.

### Suficiencia

Supongamos ahora que

$$
d\mid c.
$$

Entonces existe $m\in\mathbb Z$ tal que

$$
c=dm.
$$

Por Bézout existen $x_0,y_0\in\mathbb Z$ con

$$
d=ax_0+by_0.
$$

Multiplicando por $m$,

$$
c
=dm
=a(mx_0)+b(my_0).
$$

Por tanto,

$$
x=mx_0,
\qquad
y=my_0
$$

es una solución entera.

### Ejemplo

Consideremos

$$
84x+30y=c.
$$

El algoritmo de Euclides da

$$
84=2\cdot30+24,
$$

$$
30=1\cdot24+6,
$$

$$
24=4\cdot6.
$$

Luego

$$
\gcd(84,30)=6.
$$

Por tanto,

$$
84x+30y=c
$$

tiene solución entera **exactamente** para los enteros $c$ divisibles por $6$.

Además,

$$
6=30-24=30-(84-2\cdot30)=3\cdot30-84.
$$

Así,

$$
6=(-1)\cdot84+3\cdot30.
$$

Si, por ejemplo, $c=18=3\cdot6$, multiplicamos por $3$:

$$
18=(-3)\cdot84+9\cdot30.
$$

Una solución es

$$
(x,y)=(-3,9).
$$

El teorema distingue con precisión tres niveles lógicos:

- encontrar un divisor común que no divide a $c$ demuestra imposibilidad;
- Bézout permite construir una solución cuando el MCD sí divide a $c$;
- todavía falta describir **todas** las soluciones.

Ése es el siguiente paso.

***
## 15.14. Todas las soluciones de una ecuación diofántica lineal {#apm-c15-s14}

Supongamos que

$$
ax+by=c
$$

tiene al menos una solución entera $(x_0,y_0)$ y que

$$
d=\gcd(a,b).
$$

Cuando $a$ y $b$ son ambos no nulos, afirmamos que todas las soluciones están dadas por

$$
\boxed{
 x=x_0+\frac{b}{d}t,
 \qquad
 y=y_0-\frac{a}{d}t,
 \qquad
 t\in\mathbb Z.
}
$$

Como $d\mid a$ y $d\mid b$, los números $a/d$ y $b/d$ son enteros.

### Verificación

Tomemos cualquier $t\in\mathbb Z$. Entonces

$$
a\left(x_0+\frac{b}{d}t\right)
+b\left(y_0-\frac{a}{d}t\right)
$$

es igual a

$$
ax_0+by_0
+\frac{ab}{d}t
-\frac{ab}{d}t
=c.
$$

Por tanto, toda pareja de la forma indicada es solución.

### Exhaustividad

Ahora sea $(x,y)$ una solución cualquiera. Restando las ecuaciones

$$
ax+by=c
$$

y

$$
ax_0+by_0=c,
$$

obtenemos

$$
a(x-x_0)+b(y-y_0)=0.
$$

Dividimos por $d$ y escribimos

$$
a'=\frac{a}{d},
\qquad
b'=\frac{b}{d}.
$$

Entonces

$$
a'(x-x_0)=-b'(y-y_0).
$$

Además,

$$
\gcd(a',b')=1.
$$

¿Por qué? Si un entero positivo dividiera a $a'$ y a $b'$, al multiplicarlo por $d$ produciría un divisor común de $a$ y $b$ mayor que el permitido por la propiedad universal de $d$, salvo que ese entero fuera $1$.

De la igualdad anterior se deduce que $b'$ divide a $a'(x-x_0)$. Como $a'$ y $b'$ son coprimos, la cancelación coprima implica

$$
b'\mid(x-x_0).
$$

Por tanto, existe $t\in\mathbb Z$ tal que

$$
x-x_0=b't=\frac{b}{d}t.
$$

Sustituyendo en

$$
a'(x-x_0)+b'(y-y_0)=0,
$$

obtenemos

$$
y-y_0=-a't=-\frac{a}{d}t.
$$

Así, toda solución pertenece a la familia anunciada.

### Ejemplo

Para

$$
84x+30y=6,
$$

una solución particular es

$$
(x_0,y_0)=(-1,3),
$$

porque

$$
84(-1)+30(3)=6.
$$

Como $d=6$,

$$
\frac{30}{6}=5,
\qquad
\frac{84}{6}=14.
$$

Todas las soluciones son

$$
\boxed{
 x=-1+5t,
 \qquad
 y=3-14t,
 \qquad
 t\in\mathbb Z.
}
$$

### Coeficientes cero

Si uno de los coeficientes es cero, conviene tratar el caso directamente en lugar de forzar la demostración anterior.

Si $a=0$ y $b\ne0$, la ecuación es

$$
by=c.
$$

Tiene solución si y sólo si $b\mid c$; cuando existe, $y=c/b$ queda fijado y $x$ puede ser cualquier entero.

Si $b=0$ y $a\ne0$, ocurre lo simétrico: $x=c/a$ queda fijado y $y$ es libre.

El caso $a=b=0$ queda fuera del teorema principal y debe analizarse aparte: $0x+0y=c$ tiene todas las parejas enteras como soluciones si $c=0$, y ninguna si $c\ne0$.

### Nota pedagógica — La dirección primitiva evita perder soluciones

Comprobar una familia por sustitución sólo prueba que sus parejas son soluciones. La exhaustividad empieza con una pareja arbitraria, resta una solución particular y usa los coeficientes reducidos $a/d,b/d$. Por ser coprimos, éstos fuerzan el desplazamiento entero $(b/d,-a/d)$. Usar $(b,-a)$ también genera soluciones, pero puede saltarse algunas cuando $d>1$.

**Control resuelto.** Para $6x+10y=2$, una solución es $(2,-1)$ y la familia completa es $(2+5t,-1-3t)$, $t\in\mathbb Z$. En efecto, restar la solución particular da $3(x-2)=-5(y+1)$; la cancelación coprima obliga a $x-2=5t$, y entonces $y+1=-3t$. La familia $(2+10s,-1-6s)$ sólo selecciona los parámetros pares. Pierde $(7,-4)$, que sí satisface la ecuación: exigiría $10s=5$ con $s$ entero.

Con un coeficiente cero conviene clasificar directamente. En $0x-8y=24$, $y=-3$ y $x$ queda libre, de modo que todas las parejas son $(t,-3)$. La familia $(2t,-3)$ produce soluciones, pero pierde $(1,-3)$. Tras obtener una familia completa, una restricción adicional se traduce en condiciones sobre el parámetro. Hay que probar las dos direcciones: toda solución restringida aporta un parámetro permitido, y todo parámetro permitido produce una solución restringida.

***
## 15.15. Problemas paramétricos y elección del algoritmo {#apm-c15-s15}

El algoritmo de Euclides no sirve sólo para calcular MCD de números concretos. También permite simplificar expresiones con parámetros.

### Ejemplo 1

Consideremos

$$
\gcd(n+1,2n+3).
$$

Un paso euclidiano produce

$$
(2n+3)-2(n+1)=1.
$$

Todo divisor común de $n+1$ y $2n+3$ divide a $1$. Por tanto,

$$
\boxed{\gcd(n+1,2n+3)=1}
$$

para todo $n\in\mathbb Z$.

No fue necesario factorizar ninguna expresión ni estudiar casos.

### Ejemplo 2

Consideremos

$$
\gcd(3n+2,5n+3).
$$

Una combinación lineal cuidadosamente elegida elimina el parámetro:

$$
5(3n+2)-3(5n+3)=1.
$$

Así, cualquier divisor común debe dividir a $1$, y por tanto

$$
\boxed{\gcd(3n+2,5n+3)=1.}
$$

### Ejemplo 3

Ahora tomemos

$$
\gcd(2n+4,4n+6).
$$

Tenemos

$$
2(2n+4)-(4n+6)=2.
$$

Por tanto, cualquier divisor común divide a $2$. Por otra parte, ambos números son pares, de modo que $2$ divide a los dos. En consecuencia,

$$
\boxed{\gcd(2n+4,4n+6)=2.}
$$

Estos ejemplos muestran un principio general: al enfrentarnos a un MCD paramétrico no siempre conviene ejecutar mecánicamente muchas divisiones. A veces basta una combinación lineal que reduzca el problema a una constante pequeña.

Podemos organizar la elección de método así:

```text
¿LOS NÚMEROS SON PEQUEÑOS Y SUS DIVISORES SON EVIDENTES?
        ↓ sí
LISTAR PUEDE SER SUFICIENTE
        ↓ no
¿UNA COMBINACIÓN LINEAL ELIMINA EL PARÁMETRO?
        ↓ sí
USAR UN PASO EUCLIDIANO ESTRATÉGICO
        ↓ no
EJECUTAR EUCLIDES
        ↓
¿SE NECESITA UNA COMBINACIÓN QUE PRODUZCA EL MCD?
        ↓ sí
USAR EUCLIDES EXTENDIDO
        ↓
¿SE ESTUDIA ax+by=c?
        ↓
APLICAR EL CRITERIO d|c Y, SI CORRESPONDE, CLASIFICAR SOLUCIONES
```

La habilidad matemática no consiste en aplicar siempre el procedimiento más largo, sino en reconocer qué información se necesita y qué versión del método la produce con mayor claridad.

***
## 15.16. Cierre — protocolo euclidiano y puente hacia los primos {#apm-c15-s16}

El capítulo comenzó preguntando cuál de los divisores comunes de dos enteros concentra toda la información. La respuesta resultó mucho más rica que una simple selección por tamaño.

Si

$$
d=\gcd(a,b),
$$

entonces:

- $d$ divide a $a$ y a $b$;
- todo divisor común de $a$ y $b$ divide a $d$;
- el algoritmo de Euclides encuentra $d$ como último resto no nulo;
- Euclides extendido produce enteros $x,y$ tales que $d=ax+by$;
- todas las combinaciones lineales de $a$ y $b$ forman exactamente $d\mathbb Z$;
- la ecuación $ax+by=c$ es soluble exactamente cuando $d\mid c$;
- una vez encontrada una solución particular, todas las soluciones pueden parametrizarse.

La cadena conceptual completa es:

```text
DIVISORES COMUNES
        ↓
MCD
        ↓
DIVISIÓN CON RESTO
        ↓
PASO EUCLIDIANO
        ↓
EUCLIDES
        ↓
ÚLTIMO RESTO NO NULO
        ↓
SUSTITUCIÓN HACIA ATRÁS
        ↓
BÉZOUT
        ↓
L(a,b)=dZ
        ↓
COPRIMALIDAD
        ↓
CRITERIO DE ax+by=c
        ↓
TODAS LAS SOLUCIONES
```

Ante un nuevo problema, conviene aplicar el siguiente protocolo:

```text
1. NORMALIZAR SIGNOS CUANDO SEA ÚTIL.
2. IDENTIFICAR SI SE BUSCA MCD, BÉZOUT O SOLVENCIA DIOFÁNTICA.
3. PARA EL MCD, USAR DIVISIÓN CON RESTO Y PASOS EUCLIDIANOS.
4. DISTINGUIR TERMINACIÓN DE CORRECCIÓN.
5. SI SE NECESITA UNA COMBINACIÓN LINEAL, HACER SUSTITUCIÓN HACIA ATRÁS.
6. PARA PROBAR COPRIMALIDAD, BUSCAR UNA COMBINACIÓN QUE PRODUZCA 1.
7. PARA ax+by=c, CALCULAR d=gcd(a,b) Y COMPROBAR d|c.
8. SI d|c, ESCALAR UNA IDENTIDAD DE BÉZOUT PARA OBTENER UNA SOLUCIÓN.
9. SI SE PIDEN TODAS LAS SOLUCIONES, DEMOSTRAR LA FAMILIA PARAMÉTRICA Y SU EXHAUSTIVIDAD.
10. EN PROBLEMAS CON PARÁMETROS, BUSCAR COMBINACIONES LINEALES QUE ELIMINEN EL PARÁMETRO ANTES DE HACER CÁLCULOS LARGOS.
```

Hay una idea adicional que merece quedar registrada. La propiedad

$$
\gcd(a,b)=1,
\qquad
a\mid bc
\Longrightarrow
a\mid c
$$

muestra que la coprimalidad permite recuperar cierta forma de cancelación multiplicativa. Pero todavía no hemos identificado qué enteros poseen un comportamiento multiplicativo especialmente rígido ni cómo se descomponen los enteros en piezas elementales.

La siguiente pregunta es, por tanto:

> **Si el MCD organiza los divisores comunes, ¿cuáles son los bloques multiplicativos elementales a partir de los cuales se construyen los enteros?**

Ésa será la entrada al capítulo 16: **Números primos y factorización**.

***
# Ejercicios

Los ejercicios están organizados para pasar del cálculo y la definición del MCD a la comprensión algorítmica de Euclides, la construcción de certificados de Bézout y la clasificación completa de ecuaciones diofánticas lineales. En todo el capítulo se mantiene la convención de que $\gcd(a,b)$ está definido para $(a,b)\ne(0,0)$ y es siempre positivo. No se requiere factorización prima ni aritmética modular.

## A. Definición, signos y propiedades del MCD


**1.** **Nivel A.** Calcula $\gcd(a,b)$ en cada caso y explica qué convención de signos o de cero utilizas:
$$
(18,30),\qquad (-42,30),\qquad (0,-27),\qquad (35,64).
$$


**2.** **Nivel B.** Verifica directamente, usando la definición universal del MCD, que
$$
\gcd(42,30)=6.
$$
Debes comprobar que $6$ divide a ambos números y que todo divisor común de $42$ y $30$ divide a $6$.


**3.** **Nivel B.** Demuestra que, para $(a,b)\ne(0,0)$,
$$
\gcd(a,b)=\gcd(|a|,|b|).
$$
No apeles a factorización: compara los conjuntos de divisores comunes.


**4.** **Nivel B.** Sea $a\ne0$. Demuestra desde la definición universal que
$$
\gcd(a,0)=|a|.
$$
Explica por qué $\gcd(0,0)$ queda fuera de la convención de este capítulo.


**5.** **Nivel C.** Sea $a\ne0$. Demuestra
$$
\gcd(a,a)=|a|
\qquad\text{y}\qquad
\gcd(a,-a)=|a|.
$$
Haz explícita la propiedad universal en ambos casos.


**6.** **Nivel C.** Supón que $d>0$, que $d\mid a$ y $d\mid b$, y que existen $x,y\in\mathbb Z$ tales que
$$
d=ax+by.
$$
Demuestra que necesariamente
$$
d=\gcd(a,b).
$$
Este ejercicio debe resolverse sólo con divisibilidad y combinaciones lineales.


**7.** **Nivel C.** Sean $(a,b)\ne(0,0)$ y $k\ne0$. Conjetura y demuestra una fórmula para
$$
\gcd(ka,kb)
$$
en términos de $|k|$ y $\gcd(a,b)$. No uses factorización prima.


**8.** **Nivel D.** Un estudiante define el MCD de $a$ y $b$ como “el mayor divisor común positivo” y otro lo define como “el divisor común positivo divisible por todo divisor común”. Explica qué dirección de la equivalencia es inmediata y qué dirección requiere una justificación adicional. Formula una prueba válida usando los resultados disponibles en C15.

## B. Algoritmo de división


**9.** **Nivel A.** Encuentra el cociente y el resto canónicos en
$$
137=12q+r,\qquad 0\le r<12,
$$
y luego haz lo mismo para
$$
-137=12q+r,\qquad 0\le r<12.
$$


**10.** **Nivel A.** Para cada par $(a,b)$ con $b>0$, encuentra los únicos $q,r\in\mathbb Z$ tales que $a=bq+r$ y $0\le r<b$:
$$
(73,9),\qquad (-73,9),\qquad (240,16),\qquad (-1,7).
$$


**11.** **Nivel B.** Decide cuáles de las siguientes escrituras son divisiones con resto válidas en el sentido del algoritmo de división. Corrige las inválidas:
$$
41=7\cdot5+6,
$$
$$
41=7\cdot6-1,
$$
$$
-41=7(-6)+1,
$$
$$
25=5\cdot4+5.
$$


**12.** **Nivel C.** Demuestra la unicidad del cociente y del resto. Parte de
$$
a=bq+r=bq'+r',
\qquad
0\le r,r'<b,
$$
y demuestra primero que $r-r'$ es un múltiplo de $b$ cuyo valor absoluto es menor que $b$.


**13.** **Nivel D.** Reconstruye la prueba de existencia del algoritmo de división mediante el principio del buen orden. Debes justificar cuidadosamente que el conjunto
$$
S=\{a-bk:k\in\mathbb Z,\ a-bk\ge0\}
$$
es no vacío y que su menor elemento es estrictamente menor que $b$.


**14.** **Nivel C.** Sea $b>0$. Demuestra que el resto de dividir $a$ por $b$ es $0$ si y sólo si
$$
b\mid a.
$$
Relaciona explícitamente el algoritmo de división con la definición de divisibilidad de C14.


**15.** **Nivel C.** Supón
$$
a=bq+r,\qquad 0\le r<b.
$$
Determina el cociente y el resto canónicos de $-a$ al dividirlo por $b$ en los dos casos $r=0$ y $r>0$. Demuestra tus fórmulas.


**16.** **Nivel D.** Un estudiante afirma que en una división con resto basta exigir $|r|<b$. Explica por qué esa condición no garantiza unicidad y exhibe un mismo par $(a,b)$ con dos representaciones distintas que cumplan $|r|<b$. Luego explica qué corrige la condición $0\le r<b$.

## C. Paso euclidiano e invariancia del MCD


**17.** **Nivel B.** Usa un solo paso euclidiano para demostrar
$$
\gcd(252,105)=\gcd(105,42).
$$
No calcules todavía el valor final del MCD.


**18.** **Nivel B.** Demuestra que
$$
\gcd(84,30)=\gcd(30,24)=\gcd(24,6).
$$
En cada igualdad escribe la combinación lineal que muestra que ambos pares tienen los mismos divisores comunes.


**19.** **Nivel C.** Demuestra el lema del paso euclidiano: si
$$
a=bq+r,
$$
entonces $(a,b)$ y $(b,r)$ tienen exactamente los mismos divisores comunes.


**20.** **Nivel C.** Deduce, para $q\in\mathbb Z$,
$$
\gcd(a,b)=\gcd(b,a-qb).
$$
Explica por qué esta igualdad sigue siendo válida aunque $a-qb$ sea negativo.


**21.** **Nivel C.** Demuestra, para todo $n\in\mathbb Z$,
$$
\gcd(n+1,2n+3)=1.
$$
Elige una combinación lineal que elimine el parámetro.


**22.** **Nivel C.** Demuestra, para todo $n\in\mathbb Z$,
$$
\gcd(3n+2,5n+3)=1.
$$
Tu argumento debe producir explícitamente una combinación lineal igual a $1$.


**23.** **Nivel D.** Demuestra, para todo $n\in\mathbb Z$,
$$
\gcd(2n+4,4n+6)=2.
$$
Debes probar tanto que $2$ es divisor común como que cualquier divisor común divide a $2$.


**24.** **Nivel D.** Sean $a,b,k\in\mathbb Z$ con $(a,b)\ne(0,0)$. Demuestra
$$
\gcd(a,b)=\gcd(a,b+ka).
$$
Después explica cómo esta forma del paso euclidiano permite escoger combinaciones lineales estratégicas en problemas con parámetros.

## D. Algoritmo de Euclides


**25.** **Nivel B.** Calcula $\gcd(662,414)$ mediante el algoritmo de Euclides. Escribe todas las divisiones y señala el último resto no nulo.


**26.** **Nivel B.** Calcula
$$
\gcd(1001,391)
$$
mediante Euclides. Después verifica el resultado comprobando que el último resto no nulo divide a los dos restos inmediatamente anteriores.


**27.** **Nivel B.** Calcula
$$
\gcd(1071,462)
$$
mediante Euclides. No uses factorización.


**28.** **Nivel C.** Calcula
$$
\gcd(12345,6789)
$$
mediante Euclides y registra la cadena completa de pares
$$
(a,b)\to(b,r_1)\to(r_1,r_2)\to\cdots.
$$


**29.** **Nivel C.** Calcula
$$
\gcd(-987,610).
$$
Explica primero cómo normalizas los signos y luego ejecuta Euclides únicamente con divisores positivos.


**30.** **Nivel D.** Demuestra que el algoritmo de Euclides termina. Tu prueba debe usar el descenso estricto de los restos y el principio del buen orden, y debe evitar cualquier afirmación sobre corrección.


**31.** **Nivel D.** Demuestra la corrección del algoritmo de Euclides suponiendo ya conocida su terminación. Debes justificar por qué cada paso conserva los divisores comunes y por qué el último resto no nulo es el MCD.


**32.** **Nivel E.** Compara dos procedimientos para hallar $\gcd(119,34)$:
a) restar repetidamente el menor del mayor;
b) usar división con resto.
Explica por qué ambos se apoyan en la misma invariancia de divisores comunes y por qué el segundo comprime varios pasos del primero.

## E. Euclides extendido y Bézout


**33.** **Nivel C.** Calcula $\gcd(252,198)$ por Euclides y realiza sustitución hacia atrás hasta obtener una identidad
$$
\gcd(252,198)=252x+198y.
$$
Verifica numéricamente tu identidad.


**34.** **Nivel C.** A partir de la cadena euclidiana de $662$ y $414$, recupera por sustitución hacia atrás una identidad de Bézout. Comprueba que llegas a
$$
2=8\cdot414-5\cdot662
$$
o a otra identidad equivalente.


**35.** **Nivel C.** Calcula $\gcd(84,30)$ y encuentra enteros $x,y$ tales que
$$
\gcd(84,30)=84x+30y.
$$
Verifica directamente el resultado.


**36.** **Nivel D.** Supón que
$$
d=ax_0+by_0
$$
y que $d=\gcd(a,b)$. Demuestra que, para todo $t\in\mathbb Z$,
$$
d=a\left(x_0+\frac{b}{d}t\right)
+b\left(y_0-\frac{a}{d}t\right).
$$
Concluye que los coeficientes de Bézout no son únicos.


**37.** **Nivel D.** Usa Euclides extendido para encontrar $x,y\in\mathbb Z$ tales que
$$
35x+64y=1.
$$
Después produce dos pares distintos adicionales que también den $1$.


**38.** **Nivel D.** Sea
$$
L(a,b)=\{ax+by:x,y\in\mathbb Z\},
\qquad
d=\gcd(a,b).
$$
Demuestra la inclusión
$$
L(a,b)\subseteq d\mathbb Z
$$
sin usar todavía Bézout.


**39.** **Nivel D.** Usa la identidad de Bézout para demostrar la inclusión inversa
$$
d\mathbb Z\subseteq L(a,b).
$$
Concluye
$$
L(a,b)=d\mathbb Z.
$$


**40.** **Nivel E.** Sea $d>0$ un divisor común de $a$ y $b$. Supón además que logras construir enteros $x,y$ con
$$
d=ax+by.
$$
Demuestra que este solo certificado basta para concluir que $d=\gcd(a,b)$. Explica por qué esta técnica puede evitar ejecutar Euclides hasta el final cuando una combinación conveniente ya es visible.

## F. Coprimalidad y cancelación


**41.** **Nivel B.** Decide cuáles de los siguientes pares son coprimos y justifica cada respuesta mediante Euclides:
$$
(14,25),\qquad (21,35),\qquad (55,34),\qquad (0,1).
$$


**42.** **Nivel C.** Demuestra el criterio de Bézout para coprimalidad:
$$
\gcd(a,b)=1
\iff
\exists x,y\in\mathbb Z:\ ax+by=1.
$$
Debes demostrar ambas implicaciones.


**43.** **Nivel C.** Encuentra una identidad de Bézout que demuestre directamente que $89$ y $55$ son coprimos. No basta con indicar que su MCD es $1$: exhibe los coeficientes.


**44.** **Nivel D.** Demuestra el lema de cancelación coprima:
$$
\gcd(a,b)=1,
\qquad
a\mid bc
\Longrightarrow
a\mid c.
$$
Parte de una identidad $ax+by=1$, multiplícala por $c$ y justifica cada divisibilidad.


**45.** **Nivel C.** Da un contraejemplo concreto a
$$
a\mid bc\Longrightarrow a\mid c
$$
cuando no se supone $\gcd(a,b)=1$. Explica exactamente qué paso de la demostración del ejercicio anterior deja de estar disponible.


**46.** **Nivel D.** Demuestra que, si
$$
\gcd(a,b)=1,
$$
entonces
$$
\gcd(a,a+b)=1.
$$
Da dos pruebas: una comparando divisores comunes y otra transformando una identidad de Bézout.


**47.** **Nivel E.** Supón
$$
\gcd(a,b)=1
\qquad\text{y}\qquad
\gcd(a,c)=1.
$$
Demuestra, sin usar teoría de primos, que
$$
\gcd(a,bc)=1.
$$
Una estrategia posible es combinar dos identidades de Bézout.


**48.** **Nivel D.** Demuestra que la coprimalidad se conserva bajo un paso euclidiano:
$$
\gcd(a,b)=1
\iff
\gcd(a,b+ka)=1
$$
para todo $k\in\mathbb Z$.

## G. Criterio diofántico de existencia


**49.** **Nivel B.** Decide si la ecuación
$$
18x+30y=7
$$
tiene soluciones enteras. Tu respuesta debe ser un certificado basado en el MCD.


**50.** **Nivel C.** Decide si
$$
18x+30y=42
$$
tiene soluciones enteras y construye una solución particular a partir de una identidad de Bézout para $18$ y $30$.


**51.** **Nivel C.** Resuelve el problema de existencia para
$$
84x+30y=6.
$$
Calcula primero el MCD y construye luego una solución particular.


**52.** **Nivel C.** Demuestra que
$$
84x+30y=15
$$
no tiene soluciones enteras. Distingue claramente entre “no encontré una solución” y “puedo demostrar que ninguna existe”.


**53.** **Nivel D.** Demuestra el criterio completo de solvencia:
$$
ax+by=c
\text{ tiene solución entera}
\iff
\gcd(a,b)\mid c,
$$
para $(a,b)\ne(0,0)$. Separa explícitamente necesidad y suficiencia.


**54.** **Nivel C.** Analiza los casos con un coeficiente cero:
a) $0x+12y=c$;
b) $15x+0y=c$.
Caracteriza exactamente los valores de $c$ para los cuales existe solución y describe qué variable queda libre.


**55.** **Nivel D.** Caracteriza todos los enteros $c$ para los que
$$
24x+36y=c
$$
tiene solución entera. Tu respuesta debe tener la forma de una condición de divisibilidad necesaria y suficiente.


**56.** **Nivel D.** Sea $c\in\mathbb Z$. Caracteriza la solvencia de
$$
28x+42y=c.
$$
Cuando exista solución, escribe una solución particular directamente en términos de $c$.

## H. Clasificación de todas las soluciones


**57.** **Nivel D.** Sea $(x_0,y_0)$ una solución de
$$
ax+by=c
$$
y sea $d=\gcd(a,b)$. Verifica que, para todo $t\in\mathbb Z$,
$$
x=x_0+\frac{b}{d}t,
\qquad
y=y_0-\frac{a}{d}t
$$
también es solución.


**58.** **Nivel D.** Encuentra todas las soluciones enteras de
$$
18x+30y=42.
$$
Debes dar una solución particular, la familia paramétrica y una demostración de que no existen otras.


**59.** **Nivel D.** Encuentra todas las soluciones enteras de
$$
84x+30y=6.
$$
Verifica la familia obtenida por sustitución directa.


**60.** **Nivel D.** Usa la identidad
$$
1=11\cdot35-6\cdot64
$$
para describir todas las soluciones enteras de
$$
35x+64y=1.
$$


**61.** **Nivel E.** Encuentra todas las soluciones enteras de
$$
-21x+15y=3.
$$
Controla cuidadosamente los signos en la fórmula general.


**62.** **Nivel C.** Describe todas las soluciones enteras de
$$
0x+7y=21.
$$
Explica por qué la fórmula general del caso $ab\ne0$ no debe aplicarse mecánicamente cuando un coeficiente es cero.


**63.** **Nivel E.** Encuentra todas las soluciones enteras no negativas de
$$
18x+30y=96.
$$
Primero obtiene la familia completa de soluciones enteras y luego impón las desigualdades $x\ge0$, $y\ge0$ sobre el parámetro.


**64.** **Nivel F.** Demuestra la **exhaustividad** de la fórmula general. Si $(x,y)$ y $(x_0,y_0)$ son dos soluciones de $ax+by=c$, prueba que
$$
a(x-x_0)=-b(y-y_0),
$$
reduce por $d=\gcd(a,b)$ y usa coprimalidad para demostrar que la diferencia entre ambas soluciones tiene exactamente la forma parametrizada.

## I. Diagnóstico y elección de método


**65.** **Nivel D.** Audita la supuesta división
$$
317=52\cdot5+57.
$$
Explica por qué no es un paso válido del algoritmo de división aunque la igualdad sea correcta, y reemplázala por la división canónica.


**66.** **Nivel D.** Un estudiante calcula correctamente $\gcd(252,198)=18$, pero escribe después
$$
18=3\cdot252-4\cdot198.
$$
Comprueba la igualdad, diagnostica el error y reconstruye una identidad de Bézout correcta mediante sustitución hacia atrás.


**67.** **Nivel D.** Para cada tarea, indica el método más eficiente entre: inspección de divisores, un paso euclidiano, Euclides completo, Euclides extendido, criterio diofántico o clasificación paramétrica. Justifica tu elección:
a) calcular $\gcd(84,30)$;
b) demostrar $\gcd(7n+3,5n+2)=1$;
c) decidir si $24x+36y=50$ es soluble;
d) encontrar todas las soluciones de $35x+64y=1$.


**68.** **Nivel D.** Demuestra, para todo $n\in\mathbb Z$,
$$
\gcd(7n+3,5n+2)=1.
$$
Busca una combinación lineal constante antes de ejecutar Euclides simbólicamente.


**69.** **Nivel E.** Demuestra, para todo $n\in\mathbb Z$,
$$
\gcd(6n+9,4n+6)=|2n+3|.
$$
Tu prueba debe mostrar que $2n+3$ es divisor común y que cualquier divisor común lo divide.


**70.** **Nivel D.** Demuestra
$$
\gcd(4n+1,6n+1)=1
$$
para todo $n\in\mathbb Z$ mediante una combinación lineal que elimine $n$.


**71.** **Nivel E.** Analiza la afirmación:
> “Si la ecuación $ax+by=1$ tiene una solución entera, entonces $a$ y $b$ son coprimos.”

Determina si es verdadera y da una demostración o un contraejemplo. Explica qué papel cumple la propiedad de que todo divisor común divide toda combinación lineal.


**72.** **Nivel F.** Un estudiante encuentra una pareja $(x_0,y_0)$ que satisface $ax_0+by_0=c$ y concluye: “ya he resuelto completamente la ecuación”. Explica qué ha demostrado realmente, qué falta para describir **todas** las soluciones y qué resultados de C15 permiten cerrar esa brecha.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra, para $a,b,q\in\mathbb Z$ con $b\ne0$,
$$
\gcd(a,b)=\gcd(b,a-qb).
$$
Trata cuidadosamente los signos y demuestra que ambos pares tienen **exactamente** los mismos divisores comunes. Explica por qué esta identidad contiene el mecanismo local completo del algoritmo de Euclides.


**74.** **Nivel F.** Formaliza el algoritmo de Euclides para $a\ge b>0$ y demuestra por separado:
1. que la sucesión de restos termina;
2. que cada paso conserva el conjunto de divisores comunes;
3. que el último resto no nulo es el MCD.
Tu solución debe distinguir explícitamente **terminación** de **corrección**.


**75.** **Nivel F.** Calcula $\gcd(252,198)$ mediante Euclides, recupera una identidad
$$
d=252x+198y,
$$
y produce al menos **tres pares distintos** de coeficientes de Bézout. Después demuestra estructuralmente por qué los coeficientes no son únicos.


**76.** **Nivel F.** Sea $d=\gcd(a,b)$. Demuestra directamente
$$
\{ax+by:x,y\in\mathbb Z\}=d\mathbb Z.
$$
Tu prueba debe contener ambas inclusiones y señalar con precisión en cuál de ellas se usa la identidad de Bézout.


**77.** **Nivel F.** Demuestra
$$
\gcd(a,b)=1,
\qquad
a\mid bc
\Longrightarrow
a\mid c
$$
mediante Bézout. Después da un contraejemplo cuando se elimina la hipótesis $\gcd(a,b)=1$ y explica por qué esta propiedad prepara, pero no sustituye, la teoría multiplicativa que se desarrollará en C16.


**78.** **Nivel G.** Considera
$$
84x+30y=c.
$$
a) Calcula $\gcd(84,30)$.
b) Caracteriza exactamente los $c\in\mathbb Z$ para los que existe solución.
c) Construye una solución particular en función de $c$ cuando sea posible.
d) Describe todas las soluciones.
e) Demuestra la exhaustividad de tu parametrización.


**79.** **Nivel G.** Audita la siguiente “solución” del algoritmo de Euclides:
$$
662=414\cdot1+248,
$$
$$
414=248\cdot2-82,
$$
$$
248=82\cdot1+166,
$$
$$
166=82\cdot2+2,
$$
$$
82=2\cdot41+0.
$$
El estudiante concluye que $\gcd(662,414)=2$ y, al sustituir hacia atrás, afirma
$$
2=3\cdot414-2\cdot662,
$$
añadiendo que esos coeficientes de Bézout son únicos.

Localiza y corrige **todos** los errores: restos fuera del rango canónico, signos, orden de las divisiones, identidad que no verifica y afirmación de unicidad. Reconstruye finalmente una ejecución válida y una identidad de Bézout correcta.


**80.** **Nivel G.** Realiza una síntesis euclidiana completa con $662$ y $414$:
1. calcula el MCD mediante Euclides;
2. demuestra por qué el algoritmo termina y conserva divisores comunes;
3. recupera una identidad de Bézout;
4. decide la solvencia de
$$
414x+662y=2;
$$
5. construye una solución particular;
6. describe todas las soluciones;
7. demuestra su exhaustividad;
8. explica qué partes del procedimiento dependen sólo de divisibilidad y combinaciones lineales y qué nueva perspectiva multiplicativa queda abierta para C16.

***
## N. Certificados, restricciones y auditoría algorítmica

Todas las variables y parámetros son enteros. El MCD se usa sólo para pares distintos de $(0,0)$; no se necesitan primos ni congruencias.


**81.** **Nivel C.** Se entregan $A=3535$, $B=2222$ y el certificado $-A+2B=909$. Decide si este certificado determina por sí solo el MCD. Después audita $7A-11B=303$ y busca un certificado mejor que permita determinarlo sin ejecutar Euclides. Explica qué comprobación adicional necesita cada combinación.


**82.** **Nivel C.** Para $n\in\mathbb Z$, sean $A=12n+8$ y $B=18n+12$. Determina el MCD usando un certificado y decide cuándo el par sale del dominio de definición. Explica por qué eliminar el parámetro para obtener cero no sería suficiente.


**83.** **Nivel D.** Se conoce $1=5\cdot23-6\cdot19$. Sin repetir Euclides, clasifica todas las soluciones enteras de $23x+19y=-7$ y determina cuál cumple $-10\le x\le8$. Justifica la exhaustividad.


**84.** **Nivel D.** Para $(a,b)=(221,91)$ se propone $13=a-2b$. Audita el certificado, calcula el MCD y exhibe una identidad correcta. Indica si la divisibilidad de ambas entradas por trece bastaría para cerrar la prueba.


**85.** **Nivel C.** Para enteros $n,c$, clasifica todas las soluciones de $nx+0y=c$. Separa $n=0$ antes de aplicar cualquier criterio de MCD e indica qué cambia si se exige $x=y$.


**86.** **Nivel D.** Clasifica todas las soluciones enteras de $-28x-42y=14$. Decide cuáles satisfacen simultáneamente $x\ge0$ e $y\ge0$, y cuáles satisfacen $x\le0$ e $y\le0$.


**87.** **Nivel D.** Para $n,c\in\mathbb Z$, clasifica $nx-ny=c$ y después impón $x,y\ge0$. Incluye $n=0$ y explica si la no negatividad puede eliminar todas las soluciones cuando $n\ne0$ y $n\mid c$.


**88.** **Nivel C.** Determina todas las soluciones de $0x-9y=27$ sujetas a $-2\le x+y\le2$. Compara con $0x+0y=27$ y $0x+0y=0$ bajo la misma restricción.


**89.** **Nivel D.** Clasifica todas las soluciones no negativas de $14x+9y=126$. Obtén primero una familia completa sobre los enteros y demuestra que el intervalo final de parámetros es exacto.


**90.** **Nivel D.** Clasifica las soluciones de $10x-6y=4$ con $x,y\ge0$. Después exige además $x+y\le20$ y explica por qué una restricción produce infinitas parejas y la otra sólo finitas.


**91.** **Nivel D.** Para cada entero $m$, determina todas las soluciones de $15x+21y=3m$ que satisfacen $x+y=1$. Da una condición exacta sobre $m$ y expresa los parámetros admitidos sin usar congruencias.


**92.** **Nivel E.** Para $6x+10y=2$, un estudiante propone la familia $(2+10s,-1-6s)$, $s\in\mathbb Z$, y pide soluciones con $0\le x\le12$. Audita la generación, repara la exhaustividad y determina exactamente cuáles pierde la propuesta dentro de ese intervalo.


**93.** **Nivel D.** Audita la cadena $43=12\cdot4-5$, $12=(-5)(-2)+2$, $-5=2(-3)+1$, $2=1\cdot2+0$. ¿Son ciertas las identidades? ¿Es Euclides canónico? Determina si, a pesar de ello, la cadena certifica el MCD y reconstruye Bézout.


**94.** **Nivel E.** Una regla reemplaza $(a,b)$ por $(b,a)$ usando siempre cociente cero. Aplícala a $(26,15)$ y audita identidad, invariancia y terminación. Repara la regla y determina un certificado final para el mismo par.


**95.** **Nivel E.** Sea $b>0$ y $a=bq+r$ con $q,r\in\mathbb Z$, sin condición sobre el resto. Divide $r=bk+s$, $0\le s<b$, y repara la división de $a$. Demuestra que se conserva el MCD y aplica la reparación a $-47=9(-3)-20$.


**96.** **Nivel E.** En Euclides extendido para $(56,15)$ se registran $11=56-3\cdot15$, $4=15-11=-56+4\cdot15$ y $3=11-2\cdot4=3\cdot56-10\cdot15$. Localiza la primera fila incoherente, repara los coeficientes restantes y compara dos certificados finales distintos.

***
# Soluciones razonadas

## A. Definición, signos y propiedades del MCD


### 1

Usamos que el MCD es siempre positivo, que los signos no alteran los divisores comunes y que $\gcd(0,b)=|b|$ para $b\ne0$.

$$
\gcd(18,30)=6.
$$

Para el segundo par,

$$
\gcd(-42,30)=\gcd(42,30)=6.
$$

Para el tercero,

$$
\gcd(0,-27)=|-27|=27.
$$

Finalmente, Euclides da

$$
64=35+29,\qquad
35=29+6,\qquad
29=4\cdot6+5,\qquad
6=5+1,
$$

de modo que

$$
\gcd(35,64)=1.
$$

Por tanto,

$$
\boxed{6,\ 6,\ 27,\ 1}.
$$


### 2

Primero,

$$
42=6\cdot7,\qquad 30=6\cdot5,
$$

así que $6$ es divisor común de $42$ y $30$.

Sea ahora $c$ cualquier divisor común. Entonces $c\mid42$ y $c\mid30$. Por cierre bajo combinaciones lineales,

$$
c\mid(42-30)=12,
$$

y luego

$$
c\mid(30-2\cdot12)=6.
$$

Así, todo divisor común de $42$ y $30$ divide a $6$. Como $6>0$, satisface exactamente la definición universal del MCD. Por consiguiente,

$$
\boxed{\gcd(42,30)=6}.
$$


### 3

Para cualquier entero no nulo $d$,

$$
d\mid a \iff d\mid |a|.
$$

En efecto, $|a|$ es $a$ o $-a$, y cambiar el signo del dividendo no altera la divisibilidad. Lo mismo vale para $b$.

Por tanto,

$$
d\mid a\text{ y }d\mid b
\iff
d\mid |a|\text{ y }d\mid |b|.
$$

Los pares $(a,b)$ y $(|a|,|b|)$ tienen exactamente el mismo conjunto de divisores comunes. El entero positivo que satisface la propiedad universal es, por unicidad, el mismo para ambos pares. Luego

$$
\boxed{\gcd(a,b)=\gcd(|a|,|b|)}.
$$


### 4

Sea $a\ne0$. El número $|a|$ divide a $a$, porque $a=\pm|a|$, y también divide a $0$, pues

$$
0=|a|\cdot0.
$$

Sea $c$ cualquier divisor común de $a$ y $0$. La condición relevante es $c\mid a$; de ella se sigue también $c\mid|a|$. Por tanto, todo divisor común divide a $|a|$.

Como $|a|>0$,

$$
\boxed{\gcd(a,0)=|a|}.
$$

Para $(0,0)$ no hay un divisor común positivo privilegiado: todo entero no nulo divide a ambos componentes. Por la convención adoptada en este capítulo, $\gcd(0,0)$ queda sin definir.


### 5

El entero $|a|$ divide a $a$ y, por tanto, divide también al segundo componente tanto en $(a,a)$ como en $(a,-a)$.

Si $c$ es divisor común de $a$ y $a$, entonces $c\mid a$, y de aquí $c\mid|a|$. Por la definición universal,

$$
\gcd(a,a)=|a|.
$$

Si $c$ es divisor común de $a$ y $-a$, vuelve a cumplirse $c\mid a$, por lo que $c\mid|a|$. Así,

$$
\gcd(a,-a)=|a|.
$$

En conclusión,

$$
\boxed{\gcd(a,a)=\gcd(a,-a)=|a|}.
$$


### 6

Sabemos que $d>0$ y que $d\mid a$, $d\mid b$, así que $d$ es un divisor común positivo.

Sea $c$ cualquier divisor común de $a$ y $b$. Entonces $c$ divide toda combinación lineal entera de $a$ y $b$. En particular,

$$
c\mid(ax+by).
$$

Pero por hipótesis

$$
ax+by=d.
$$

Por tanto,

$$
c\mid d.
$$

Así, $d$ es divisor común positivo y todo divisor común divide a $d$. Esa es precisamente la caracterización universal del MCD. Luego

$$
\boxed{d=\gcd(a,b)}.
$$


### 7

La fórmula es

$$
\boxed{\gcd(ka,kb)=|k|\gcd(a,b)}.
$$

Sea $d=\gcd(a,b)$. Como $d\mid a$ y $d\mid b$,

$$
|k|d\mid ka,\qquad |k|d\mid kb,
$$

de modo que $|k|d$ es divisor común positivo de $ka$ y $kb$.

Por Bézout existen $x,y\in\mathbb Z$ tales que

$$
d=ax+by.
$$

Multiplicando por $|k|$ y usando $|k|=\varepsilon k$ con $\varepsilon\in\{-1,1\}$,

$$
|k|d=(ka)(\varepsilon x)+(kb)(\varepsilon y).
$$

Si $c$ divide a $ka$ y a $kb$, entonces divide esa combinación lineal; por tanto,

$$
c\mid |k|d.
$$

Así, $|k|d$ satisface la propiedad universal para el par $(ka,kb)$, y queda demostrada la fórmula.


### 8

Supongamos primero que $u>0$ es un divisor común de $a$ y $b$ y que todo divisor común divide a $u$. Si $c>0$ es cualquier divisor común, entonces $c\mid u$. Como ambos son positivos,

$$
c\le u.
$$

Por tanto, $u$ es el mayor divisor común positivo. Esta dirección es inmediata una vez conocida la propiedad de tamaño de la divisibilidad.

Para la dirección inversa, supongamos ahora que $m$ es el **mayor divisor común positivo** de $a$ y $b$. Ejecutemos el algoritmo de Euclides y llamemos $d$ al último resto no nulo. Por la corrección de Euclides, $d$ es divisor común positivo y, además, todo divisor común de $a$ y $b$ divide a $d$.

Como $m$ es el mayor divisor común positivo y $d$ es un divisor común positivo,

$$
d\le m.
$$

Por otra parte, $m$ también es divisor común, y la propiedad universal de $d$ da

$$
m\mid d.
$$

Como $m,d>0$, se sigue que

$$
m\le d.
$$

Por tanto,

$$
m=d.
$$

Como todo divisor común divide a $d$, también divide a $m$. Así, el mayor divisor común positivo satisface la caracterización universal.

En consecuencia, en $\mathbb Z$ ambas definiciones son equivalentes. La primera dirección usa sólo la relación entre divisibilidad y tamaño; la segunda necesita la estructura proporcionada por Euclides —equivalentemente, puede cerrarse mediante Bézout— y no se deduce únicamente del orden de los enteros.



### 9

Para $137$,

$$
137=12\cdot11+5,
$$

y $0\le5<12$. Por tanto,

$$
\boxed{q=11,\ r=5}.
$$

Para $-137$ no podemos usar resto negativo. Tomamos

$$
-137=12(-12)+7,
$$

y $0\le7<12$. Luego

$$
\boxed{q=-12,\ r=7}.
$$


### 10

Aplicamos la condición canónica $0\le r<b$:

$$
73=9\cdot8+1,
$$

por lo que $(q,r)=(8,1)$.

$$
-73=9(-9)+8,
$$

por lo que $(q,r)=(-9,8)$.

$$
240=16\cdot15+0,
$$

por lo que $(q,r)=(15,0)$.

Finalmente,

$$
-1=7(-1)+6,
$$

de modo que $(q,r)=(-1,6)$.

Así,

$$
\boxed{(8,1),\ (-9,8),\ (15,0),\ (-1,6)}.
$$


### 11

La escritura

$$
41=7\cdot5+6
$$

es válida porque $0\le6<7$.

La igualdad

$$
41=7\cdot6-1
$$

es cierta, pero el resto $-1$ no es canónico. La corrección es

$$
41=7\cdot5+6.
$$

La igualdad

$$
-41=7(-6)+1
$$

es válida, pues $0\le1<7$.

Finalmente,

$$
25=5\cdot4+5
$$

no es válida como división canónica porque el resto debe satisfacer $r<5$. La forma correcta es

$$
25=5\cdot5+0.
$$


### 12

Supongamos

$$
a=bq+r=bq'+r',
\qquad
0\le r,r'<b.
$$

Restando,

$$
b(q-q')=r'-r.
$$

Por tanto, $r'-r$ es múltiplo de $b$. Además,

$$
-(b-1)\le r'-r\le b-1,
$$

así que

$$
|r'-r|<b.
$$

El único múltiplo de $b$ cuyo valor absoluto es estrictamente menor que $b$ es $0$. Luego

$$
r'-r=0,
$$

es decir,

$$
r=r'.
$$

Sustituyendo en las dos expresiones de $a$,

$$
bq=bq'.
$$

Como $b>0$, se sigue que $q=q'$. El cociente y el resto son, por tanto, únicos.


### 13

Sea

$$
S=\{a-bk:k\in\mathbb Z,\ a-bk\ge0\},
$$

con $b>0$.

Primero probamos que $S$ no es vacío. Si $a\ge0$, basta tomar $k=0$, pues $a\in S$. Si $a<0$, tomamos por ejemplo $k=-|a|$. Entonces

$$
a-b(-|a|)=a+b|a|\ge0,
$$

pues $b\ge1$ y $a=-|a|$.

Por el principio del buen orden, $S$ tiene un menor elemento $r$. Por definición de $S$, existe $q\in\mathbb Z$ tal que

$$
r=a-bq,
$$

es decir,

$$
a=bq+r.
$$

Ya sabemos que $r\ge0$. Si $r\ge b$, entonces

$$
r-b\ge0
$$

y

$$
r-b=a-b(q+1),
$$

de modo que $r-b\in S$. Pero $r-b<r$, contradicción con la minimalidad de $r$. Por tanto,

$$
0\le r<b.
$$

Esto prueba la existencia de la división canónica.


### 14

Si el resto es $0$, entonces

$$
a=bq
$$

para algún $q\in\mathbb Z$. Por definición,

$$
b\mid a.
$$

Recíprocamente, si $b\mid a$, existe $q\in\mathbb Z$ tal que

$$
a=bq.
$$

Esto ya es una división con resto con $r=0$, y cumple $0\le0<b$. Por unicidad del algoritmo de división, el resto canónico debe ser $0$.

Así,

$$
\boxed{r=0\iff b\mid a}.
$$


### 15

Partimos de

$$
a=bq+r,\qquad 0\le r<b.
$$

Si $r=0$, entonces

$$
-a=b(-q)+0.
$$

Por tanto, el cociente y resto de $-a$ son

$$
\boxed{-q,\ 0}.
$$

Si $r>0$, entonces

$$
-a=-bq-r=b(-q-1)+(b-r).
$$

Como $0<r<b$,

$$
0<b-r<b.
$$

Así, la forma canónica es

$$
\boxed{-a=b(-q-1)+(b-r)}.
$$

Por tanto, para $r>0$ el cociente es $-q-1$ y el resto es $b-r$.


### 16

La condición $|r|<b$ permite restos negativos y, por ello, puede admitir dos representaciones.

Por ejemplo, con $a=5$ y $b=3$,

$$
5=3\cdot1+2
$$

y también

$$
5=3\cdot2-1.
$$

En ambos casos,

$$
|2|<3,\qquad |-1|<3,
$$

pero los cocientes y restos son distintos.

La condición canónica

$$
0\le r<b
$$

elige exactamente uno de los representantes posibles del resto y elimina esa ambigüedad. Para $5$ dividido por $3$, la única forma canónica es

$$
5=3\cdot1+2.
$$

## C. Paso euclidiano e invariancia del MCD


### 17

Dividimos $252$ por $105$:

$$
252=105\cdot2+42.
$$

Por el lema del paso euclidiano, los pares $(252,105)$ y $(105,42)$ tienen exactamente los mismos divisores comunes. Por tanto,

$$
\boxed{\gcd(252,105)=\gcd(105,42)}.
$$

No es necesario calcular todavía que ambos MCD valen $21$.


### 18

Tenemos

$$
84=30\cdot2+24,
$$

de modo que

$$
24=84-2\cdot30.
$$

Si $d$ divide a $84$ y a $30$, divide a $24$. Recíprocamente, si divide a $30$ y a $24$, entonces divide a

$$
84=2\cdot30+24.
$$

Por tanto,

$$
\gcd(84,30)=\gcd(30,24).
$$

Luego,

$$
30=24\cdot1+6,
\qquad
6=30-24.
$$

El mismo argumento muestra que $(30,24)$ y $(24,6)$ tienen exactamente los mismos divisores comunes. Así,

$$
\boxed{\gcd(84,30)=\gcd(30,24)=\gcd(24,6)}.
$$


### 19

Supongamos

$$
a=bq+r.
$$

Si $d\mid a$ y $d\mid b$, entonces

$$
r=a-bq
$$

es una combinación lineal de $a$ y $b$, por lo que $d\mid r$. Así, $d$ es divisor común de $b$ y $r$.

Recíprocamente, si $d\mid b$ y $d\mid r$, entonces

$$
a=bq+r,
$$

por lo que $d\mid a$. Así, $d$ es divisor común de $a$ y $b$.

Hemos probado

$$
d\mid a,\ d\mid b
\iff
d\mid b,\ d\mid r.
$$

Los dos pares tienen exactamente los mismos divisores comunes y, por tanto, el mismo MCD.


### 20

Tomamos

$$
r=a-qb.
$$

Entonces

$$
a=bq+r.
$$

El lema del paso euclidiano da inmediatamente

$$
\boxed{\gcd(a,b)=\gcd(b,a-qb)}.
$$

Si $a-qb<0$, no hay problema: cambiar el signo de un componente no cambia sus divisores comunes. En particular,

$$
\gcd(b,a-qb)=\gcd(b,|a-qb|).
$$

La identidad es válida para todo $q\in\mathbb Z$.



### 21

Sea $d$ un divisor común de $n+1$ y $2n+3$. Entonces $d$ divide cualquier combinación lineal de ambos. En particular,

$$
2(n+1)-(2n+3)=-1.
$$

Por tanto,

$$
d\mid1.
$$

Todo divisor común es entonces $\pm1$. Como el MCD es positivo,

$$
\boxed{\gcd(n+1,2n+3)=1}.
$$

La combinación lineal que elimina el parámetro es precisamente

$$
2(n+1)-(2n+3)=-1.
$$


### 22

Calculamos una combinación lineal constante:

$$
3(5n+3)-5(3n+2)
=
15n+9-15n-10
=
-1.
$$

Sea $d$ un divisor común de $3n+2$ y $5n+3$. Entonces $d$ divide el miembro izquierdo y, por tanto,

$$
d\mid1.
$$

Así, el único divisor común positivo posible es $1$. Luego

$$
\boxed{\gcd(3n+2,5n+3)=1}.
$$


### 23

Observamos primero que

$$
2n+4=2(n+2),
\qquad
4n+6=2(2n+3).
$$

Por tanto,

$$
2\mid(2n+4),
\qquad
2\mid(4n+6),
$$

así que $2$ es divisor común.

Sea ahora $d$ cualquier divisor común. Entonces

$$
d\mid 2(2n+4)-(4n+6).
$$

Pero

$$
2(2n+4)-(4n+6)=4n+8-4n-6=2.
$$

Así,

$$
d\mid2.
$$

Por la definición universal,

$$
\boxed{\gcd(2n+4,4n+6)=2}.
$$


### 24

Sea $d$ divisor común de $a$ y $b$. Entonces

$$
d\mid b+ka,
$$

porque $b+ka$ es una combinación lineal de $a$ y $b$. Así, todo divisor común de $(a,b)$ es divisor común de $(a,b+ka)$.

Recíprocamente, si $d\mid a$ y $d\mid b+ka$, entonces

$$
b=(b+ka)-ka,
$$

de modo que $d\mid b$. Por tanto, $d$ es divisor común de $(a,b)$.

Los dos pares tienen exactamente los mismos divisores comunes y, por tanto,

$$
\boxed{\gcd(a,b)=\gcd(a,b+ka)}.
$$

La utilidad estratégica es que podemos escoger $k$ para cancelar términos o reducir tamaños. En expresiones con parámetros, una combinación adecuada puede eliminar el parámetro y producir un divisor común constante.

## D. Algoritmo de Euclides


### 25

Aplicamos Euclides:

$$
662=414\cdot1+248,
$$

$$
414=248\cdot1+166,
$$

$$
248=166\cdot1+82,
$$

$$
166=82\cdot2+2,
$$

$$
82=2\cdot41+0.
$$

El último resto no nulo es $2$. Por tanto,

$$
\boxed{\gcd(662,414)=2}.
$$


### 26

La cadena euclidiana es

$$
1001=391\cdot2+219,
$$

$$
391=219\cdot1+172,
$$

$$
219=172\cdot1+47,
$$

$$
172=47\cdot3+31,
$$

$$
47=31\cdot1+16,
$$

$$
31=16\cdot1+15,
$$

$$
16=15\cdot1+1,
$$

$$
15=1\cdot15+0.
$$

El último resto no nulo es $1$, así que

$$
\boxed{\gcd(1001,391)=1}.
$$

En el penúltimo paso aparece

$$
1=16-15,
$$

por lo que $1$ divide a $16$ y a $15$, los dos restos inmediatamente anteriores. Esto es consistente con que todos los divisores comunes de la cadena terminen concentrados en el último resto no nulo.


### 27

Ejecutamos Euclides:

$$
1071=462\cdot2+147,
$$

$$
462=147\cdot3+21,
$$

$$
147=21\cdot7+0.
$$

El último resto no nulo es $21$. Luego

$$
\boxed{\gcd(1071,462)=21}.
$$


### 28

La cadena es

$$
12345=6789\cdot1+5556,
$$

$$
6789=5556\cdot1+1233,
$$

$$
5556=1233\cdot4+624,
$$

$$
1233=624\cdot1+609,
$$

$$
624=609\cdot1+15,
$$

$$
609=15\cdot40+9,
$$

$$
15=9\cdot1+6,
$$

$$
9=6\cdot1+3,
$$

$$
6=3\cdot2+0.
$$

Por tanto,

$$
\boxed{\gcd(12345,6789)=3}.
$$

La cadena de pares puede registrarse como

$$
(12345,6789)\to(6789,5556)\to(5556,1233)\to(1233,624)
$$

$$
\to(624,609)\to(609,15)\to(15,9)\to(9,6)\to(6,3)\to(3,0).
$$


### 29

Primero normalizamos signos:

$$
\gcd(-987,610)=\gcd(987,610).
$$

Ahora aplicamos Euclides:

$$
987=610+377,
$$

$$
610=377+233,
$$

$$
377=233+144,
$$

$$
233=144+89,
$$

$$
144=89+55,
$$

$$
89=55+34,
$$

$$
55=34+21,
$$

$$
34=21+13,
$$

$$
21=13+8,
$$

$$
13=8+5,
$$

$$
8=5+3,
$$

$$
5=3+2,
$$

$$
3=2+1,
$$

$$
2=2\cdot1+0.
$$

El último resto no nulo es $1$. Por tanto,

$$
\boxed{\gcd(-987,610)=1}.
$$


### 30

En cada paso del algoritmo, con divisor positivo, el algoritmo de división produce

$$
r_{i-1}=q_i r_i+r_{i+1},
\qquad
0\le r_{i+1}<r_i.
$$

Mientras el resto sea no nulo, obtenemos una sucesión estrictamente decreciente de enteros positivos:

$$
r_1>r_2>r_3>\cdots>0.
$$

Supongamos que el algoritmo no terminara. Entonces existiría un conjunto no vacío de restos positivos producidos por la ejecución. Por el principio del buen orden, ese conjunto tendría un menor elemento $m>0$.

Pero si $m$ aparece como divisor en un nuevo paso y la ejecución continúa, el algoritmo de división produce un resto $r$ con

$$
0\le r<m.
$$

Como la ejecución supuestamente no termina, ese resto sería positivo, de modo que

$$
0<r<m,
$$

contradicción con la minimalidad de $m$.

Por tanto, el algoritmo debe alcanzar un resto $0$ después de un número finito de pasos.

Esta prueba establece solamente **terminación**. No demuestra aún que el último resto no nulo sea el MCD.


### 31

Suponemos conocida la terminación. La ejecución tiene entonces la forma

$$
r_{i-1}=q_i r_i+r_{i+1}
$$

hasta llegar a

$$
r_{m-2}=q_{m-1}r_{m-1}+r_m,
$$

$$
r_{m-1}=q_m r_m+0.
$$

Por el lema del paso euclidiano, cada reemplazo

$$
(r_{i-1},r_i)\longmapsto(r_i,r_{i+1})
$$

conserva exactamente el conjunto de divisores comunes. Por tanto, el par inicial $(a,b)$ tiene los mismos divisores comunes que el último par no trivial $(r_{m-1},r_m)$.

En el último paso,

$$
r_m\mid r_{m-1},
$$

porque $r_{m-1}=q_mr_m$. Así, los divisores comunes de $r_{m-1}$ y $r_m$ son exactamente los divisores de $r_m$. El entero positivo $r_m$ divide a ambos y todo divisor común divide a $r_m$.

Luego

$$
\boxed{\gcd(a,b)=r_m}.
$$

Esto prueba la **corrección** del algoritmo, distinta de su terminación.


### 32

Por restas repetidas:

$$
119-34=85,
$$

$$
85-34=51,
$$

$$
51-34=17,
$$

y

$$
34-17=17.
$$

Así se llega a

$$
\gcd(119,34)=17.
$$

Con división con resto,

$$
119=34\cdot3+17,
$$

$$
34=17\cdot2+0.
$$

También obtenemos

$$
\boxed{\gcd(119,34)=17}.
$$

Los dos procedimientos se basan en la misma invariancia:

$$
\gcd(a,b)=\gcd(a-b,b)
$$

o, más generalmente,

$$
\gcd(a,b)=\gcd(a-qb,b).
$$

La división con resto elige de una sola vez un cociente $q$ que resume varias restas sucesivas. Por eso Euclides es una compresión sistemática del método de restas.

## E. Euclides extendido y Bézout


### 33

Aplicamos Euclides:

$$
252=198+54,
$$

$$
198=54\cdot3+36,
$$

$$
54=36+18,
$$

$$
36=18\cdot2.
$$

Por tanto,

$$
\gcd(252,198)=18.
$$

Sustituimos hacia atrás:

$$
18=54-36,
$$

y como

$$
36=198-3\cdot54,
$$

tenemos

$$
18=54-(198-3\cdot54)=4\cdot54-198.
$$

Además,

$$
54=252-198.
$$

Así,

$$
18=4(252-198)-198
=4\cdot252-5\cdot198.
$$

Por tanto,

$$
\boxed{18=4\cdot252-5\cdot198}.
$$

Verificación:

$$
4\cdot252-5\cdot198=1008-990=18.
$$


### 34

Partimos de la cadena

$$
662=414+248,
$$

$$
414=248+166,
$$

$$
248=166+82,
$$

$$
166=2\cdot82+2.
$$

Entonces

$$
2=166-2\cdot82.
$$

Como

$$
82=248-166,
$$

obtenemos

$$
2=166-2(248-166)=3\cdot166-2\cdot248.
$$

A su vez,

$$
166=414-248,
$$

por lo que

$$
2=3(414-248)-2\cdot248
=3\cdot414-5\cdot248.
$$

Finalmente,

$$
248=662-414.
$$

Así,

$$
2=3\cdot414-5(662-414)
=8\cdot414-5\cdot662.
$$

Por tanto,

$$
\boxed{2=8\cdot414-5\cdot662}.
$$


### 35

Euclides da

$$
84=30\cdot2+24,
$$

$$
30=24+6,
$$

$$
24=6\cdot4.
$$

Por tanto,

$$
\gcd(84,30)=6.
$$

Sustituyendo,

$$
6=30-24,
$$

y

$$
24=84-2\cdot30.
$$

Luego

$$
6=30-(84-2\cdot30)
=-84+3\cdot30.
$$

Así,

$$
\boxed{6=84(-1)+30(3)}.
$$

Los coeficientes pueden tomarse como

$$
\boxed{x=-1,\ y=3}.
$$


### 36

Partimos de

$$
d=ax_0+by_0,
$$

con $d=\gcd(a,b)$. Como $d\mid a$ y $d\mid b$, los números $a/d$ y $b/d$ son enteros.

Para cualquier $t\in\mathbb Z$,

$$
a\left(x_0+\frac bd t\right)
+b\left(y_0-\frac ad t\right)
$$

es igual a

$$
ax_0+by_0+\frac{ab}{d}t-\frac{ab}{d}t
=d.
$$

Por tanto,

$$
\boxed{
d=a\left(x_0+\frac bd t\right)
+b\left(y_0-\frac ad t\right)
}.
$$

Al variar $t$ obtenemos, en general, infinitos pares de coeficientes distintos. Por eso una identidad de Bézout no tiene coeficientes únicos.


### 37

Reconstruimos el certificado mediante Euclides extendido. Las divisiones son $64=35+29$, $35=29+6$, $29=4\cdot6+5$, $6=5+1$ y $5=5\cdot1+0$. Hacia atrás,

$$
\begin{aligned}
1&=6-5=6-(29-4\cdot6)=5\cdot6-29\\
 &=5(35-29)-29=5\cdot35-6\cdot29\\
 &=5\cdot35-6(64-35)=11\cdot35-6\cdot64.
\end{aligned}
$$

La sustitución verifica $385-384=1$. Por tanto, la identidad obtenida es

$$
1=11\cdot35-6\cdot64.
$$

Así, una solución es

$$
(x_0,y_0)=(11,-6).
$$

Como $\gcd(35,64)=1$, todos los pares de Bézout que representan $1$ se obtienen mediante

$$
x=11+64t,
\qquad
y=-6-35t,
\qquad t\in\mathbb Z.
$$

Tomando $t=1$,

$$
(x,y)=(75,-41).
$$

Tomando $t=-1$,

$$
(x,y)=(-53,29).
$$

Por tanto, tres pares distintos son

$$
\boxed{(11,-6),\ (75,-41),\ (-53,29)}.
$$


### 38

Sea

$$
z=ax+by\in L(a,b).
$$

Como $d=\gcd(a,b)$, tenemos

$$
d\mid a,\qquad d\mid b.
$$

Por cierre bajo combinaciones lineales,

$$
d\mid(ax+by)=z.
$$

Entonces $z$ es múltiplo de $d$, es decir,

$$
z\in d\mathbb Z.
$$

Como $z$ era arbitrario,

$$
\boxed{L(a,b)\subseteq d\mathbb Z}.
$$

En esta inclusión no se usa Bézout; sólo que $d$ divide a $a$ y a $b$.


### 39

Por Bézout existen $x_0,y_0\in\mathbb Z$ tales que

$$
d=ax_0+by_0.
$$

Sea $z\in d\mathbb Z$. Entonces existe $m\in\mathbb Z$ con

$$
z=dm.
$$

Multiplicando la identidad de Bézout por $m$,

$$
z=dm=a(mx_0)+b(my_0).
$$

Como $mx_0,my_0\in\mathbb Z$,

$$
z\in L(a,b).
$$

Por tanto,

$$
d\mathbb Z\subseteq L(a,b).
$$

Combinando con el ejercicio anterior,

$$
\boxed{L(a,b)=d\mathbb Z}.
$$


### 40

Sabemos que $d>0$, $d\mid a$, $d\mid b$ y que

$$
d=ax+by.
$$

Sea $c$ cualquier divisor común de $a$ y $b$. Entonces $c$ divide toda combinación lineal de $a$ y $b$, en particular

$$
c\mid(ax+by)=d.
$$

Así, $d$ es divisor común positivo y todo divisor común divide a $d$. Por definición universal,

$$
\boxed{d=\gcd(a,b)}.
$$

Este argumento muestra que una identidad lineal adecuada actúa como un **certificado** del MCD. Si ya encontramos una combinación que produce un divisor común positivo, no es necesario completar una larga ejecución de Euclides para verificar la propiedad universal.


## F. Coprimalidad y cancelación


### 41

Aplicamos Euclides en cada caso.

Para $(14,25)$,

$$
25=14+11,\qquad
14=11+3,\qquad
11=3\cdot3+2,\qquad
3=2+1,
$$

de modo que

$$
\gcd(14,25)=1.
$$

Para $(21,35)$,

$$
35=21+14,\qquad
21=14+7,\qquad
14=2\cdot7,
$$

así que

$$
\gcd(21,35)=7.
$$

Para $(55,34)$,

$$
55=34+21,\qquad
34=21+13,\qquad
21=13+8,\qquad
13=8+5,
$$

$$
8=5+3,\qquad
5=3+2,\qquad
3=2+1,
$$

por lo que

$$
\gcd(55,34)=1.
$$

Finalmente,

$$
\gcd(0,1)=1.
$$

Por tanto, los pares coprimos son

$$
\boxed{(14,25),\ (55,34),\ (0,1)}.
$$


### 42

Supongamos primero que

$$
\gcd(a,b)=1.
$$

Por la identidad de Bézout existen $x,y\in\mathbb Z$ tales que

$$
ax+by=\gcd(a,b)=1.
$$

Esto prueba una implicación.

Recíprocamente, supongamos que existen $x,y$ tales que

$$
ax+by=1.
$$

Sea $d$ un divisor común de $a$ y $b$. Entonces $d$ divide toda combinación lineal, y por tanto

$$
d\mid1.
$$

Así, todo divisor común es $\pm1$, de modo que el MCD positivo es $1$:

$$
\gcd(a,b)=1.
$$

En conclusión,

$$
\boxed{
\gcd(a,b)=1
\iff
\exists x,y\in\mathbb Z:\ ax+by=1
}.
$$


### 43

Euclides para $89$ y $55$ produce la cadena de Fibonacci:

$$
89=55+34,\quad
55=34+21,\quad
34=21+13,
$$

$$
21=13+8,\quad
13=8+5,\quad
8=5+3,\quad
5=3+2,\quad
3=2+1.
$$

La sustitución hacia atrás da, por ejemplo,

$$
1=-21\cdot89+34\cdot55.
$$

Verificación:

$$
-21\cdot89+34\cdot55=-1869+1870=1.
$$

Por el criterio de Bézout,

$$
\boxed{\gcd(89,55)=1}.
$$


### 44

Como $\gcd(a,b)=1$, Bézout garantiza enteros $x,y$ tales que

$$
ax+by=1.
$$

Multiplicamos por $c$:

$$
acx+bcy=c.
$$

Por hipótesis,

$$
a\mid bc.
$$

Luego $a$ divide a $bcy$. También es evidente que

$$
a\mid acx.
$$

Por tanto, $a$ divide la suma

$$
acx+bcy=c.
$$

Así,

$$
\boxed{a\mid c}.
$$

La coprimalidad es exactamente lo que permite producir la identidad $ax+by=1$ usada en la cancelación.


### 45

Tomemos

$$
a=6,\qquad b=3,\qquad c=2.
$$

Entonces

$$
bc=6,
$$

por lo que

$$
6\mid bc.
$$

Sin embargo,

$$
6\nmid2.
$$

Por tanto, la implicación falla sin coprimalidad.

En la demostración del ejercicio anterior necesitábamos una identidad

$$
ax+by=1.
$$

Aquí

$$
\gcd(6,3)=3\ne1,
$$

así que no existen enteros $x,y$ con $6x+3y=1$. Ese es exactamente el paso que deja de estar disponible.


### 46

**Primera prueba: divisores comunes.**

Sea $d$ divisor común de $a$ y $a+b$. Entonces

$$
d\mid(a+b)-a=b.
$$

Por tanto, $d$ es divisor común de $a$ y $b$. Como $\gcd(a,b)=1$, se sigue que $d\mid1$. Luego

$$
\gcd(a,a+b)=1.
$$

**Segunda prueba: Bézout.**

Como $\gcd(a,b)=1$, existen $x,y$ con

$$
ax+by=1.
$$

Escribimos $b=(a+b)-a$:

$$
1=ax+y[(a+b)-a]
=a(x-y)+(a+b)y.
$$

Hemos obtenido una identidad de Bézout para $a$ y $a+b$. Por tanto,

$$
\boxed{\gcd(a,a+b)=1}.
$$


### 47

Como $\gcd(a,b)=1$, existen $x,y$ tales que

$$
ax+by=1.
$$

Como $\gcd(a,c)=1$, existen $u,v$ tales que

$$
au+cv=1.
$$

Multiplicamos ambas identidades:

$$
1=(ax+by)(au+cv).
$$

Expandiendo,

$$
1=a^2xu+acxv+abuy+bc\,yv.
$$

Los tres primeros términos contienen un factor $a$:

$$
1=a(axu+cxv+buy)+bc(yv).
$$

Así hemos construido una identidad

$$
1=aX+bcY
$$

con $X,Y\in\mathbb Z$. Por el criterio de Bézout,

$$
\boxed{\gcd(a,bc)=1}.
$$

No se utilizó teoría de números primos.


### 48

Por el paso euclidiano,

$$
\gcd(a,b)=\gcd(a,b+ka)
$$

para todo $k\in\mathbb Z$.

Por tanto,

$$
\gcd(a,b)=1
\iff
\gcd(a,b+ka)=1.
$$

Así,

$$
\boxed{
\gcd(a,b)=1
\iff
\gcd(a,b+ka)=1
}.
$$

La coprimalidad se conserva porque el conjunto completo de divisores comunes se conserva bajo esa transformación.

## G. Criterio diofántico de existencia


### 49

Calculamos

$$
\gcd(18,30)=6.
$$

Si existieran enteros $x,y$ con

$$
18x+30y=7,
$$

entonces $6$, al dividir a $18$ y a $30$, dividiría también a toda combinación lineal de ellos. En particular, tendría que cumplirse

$$
6\mid7,
$$

lo cual es falso.

Por tanto,

$$
\boxed{18x+30y=7\text{ no tiene soluciones enteras}}.
$$

El certificado de imposibilidad es $\gcd(18,30)=6\nmid7$.


### 50

Tenemos

$$
\gcd(18,30)=6,
$$

y

$$
6\mid42.
$$

Por tanto, el criterio diofántico garantiza solvencia.

Una identidad de Bézout es

$$
6=2\cdot18-1\cdot30.
$$

Como $42=7\cdot6$, multiplicamos por $7$:

$$
42=14\cdot18-7\cdot30.
$$

Así, una solución particular es

$$
\boxed{x=14,\ y=-7}.
$$


### 51

Euclides da

$$
84=2\cdot30+24,
$$

$$
30=24+6,
$$

de modo que

$$
\gcd(84,30)=6.
$$

Como $6\mid6$, existe solución.

Además,

$$
6=30-(84-2\cdot30)
=-84+3\cdot30.
$$

Por tanto,

$$
\boxed{x=-1,\ y=3}
$$

es una solución particular de

$$
84x+30y=6.
$$


### 52

Ya sabemos que

$$
\gcd(84,30)=6.
$$

Si existieran enteros $x,y$ tales que

$$
84x+30y=15,
$$

entonces, como $6$ divide a $84$ y a $30$, tendría que dividir también al miembro izquierdo y, por igualdad, a $15$.

Pero

$$
6\nmid15.
$$

Por tanto,

$$
\boxed{84x+30y=15\text{ no tiene soluciones enteras}}.
$$

No se trata de que una búsqueda haya fallado: la divisibilidad por el MCD constituye una obstrucción que descarta todas las parejas enteras posibles.


### 53

Sea

$$
d=\gcd(a,b),
\qquad
(a,b)\ne(0,0).
$$

**Necesidad.** Supongamos que existe una solución $(x,y)$:

$$
ax+by=c.
$$

Como $d\mid a$ y $d\mid b$, se tiene

$$
d\mid(ax+by)=c.
$$

Por tanto,

$$
d\mid c.
$$

**Suficiencia.** Supongamos ahora que

$$
d\mid c.
$$

Entonces existe $m\in\mathbb Z$ tal que

$$
c=dm.
$$

Por Bézout existen $x_0,y_0$ con

$$
d=ax_0+by_0.
$$

Multiplicando por $m$,

$$
c=dm=a(mx_0)+b(my_0).
$$

Así,

$$
x=mx_0,\qquad y=my_0
$$

es una solución entera.

En conclusión,

$$
\boxed{
ax+by=c\text{ tiene solución entera}
\iff
\gcd(a,b)\mid c
}.
$$


### 54

**a)** La ecuación

$$
0x+12y=c
$$

se reduce a

$$
12y=c.
$$

Existe $y\in\mathbb Z$ si y sólo si

$$
12\mid c.
$$

Cuando esto ocurre,

$$
y=\frac c{12},
$$

mientras que $x$ puede ser cualquier entero. Así,

$$
\boxed{(x,y)=\left(t,\frac c{12}\right),\quad t\in\mathbb Z}
$$

cuando $12\mid c$.

**b)** La ecuación

$$
15x+0y=c
$$

se reduce a

$$
15x=c.
$$

Es soluble si y sólo si

$$
15\mid c.
$$

En ese caso,

$$
x=\frac c{15},
$$

y $y$ queda libre:

$$
\boxed{(x,y)=\left(\frac c{15},t\right),\quad t\in\mathbb Z}.
$$


### 55

Calculamos

$$
\gcd(24,36)=12.
$$

Por el criterio diofántico,

$$
24x+36y=c
$$

tiene solución entera si y sólo si

$$
\boxed{12\mid c}.
$$

Por tanto, los valores posibles de $c$ son exactamente los múltiplos de $12$:

$$
c\in12\mathbb Z.
$$


### 56

Tenemos

$$
\gcd(28,42)=14.
$$

Por tanto,

$$
28x+42y=c
$$

es soluble si y sólo si

$$
\boxed{14\mid c}.
$$

Supongamos entonces

$$
c=14m
$$

con $m\in\mathbb Z$. Como

$$
14=-28+42,
$$

multiplicando por $m$ obtenemos

$$
c=-28m+42m.
$$

Así, una solución particular es

$$
\boxed{x=-m=-\frac c{14},\qquad y=m=\frac c{14}}.
$$

## H. Clasificación de todas las soluciones


### 57

Sea

$$
(x_0,y_0)
$$

una solución de

$$
ax+by=c.
$$

Tomamos

$$
x=x_0+\frac bd t,
\qquad
y=y_0-\frac ad t,
$$

donde $d=\gcd(a,b)$ y $t\in\mathbb Z$.

Entonces

$$
ax+by
=
a\left(x_0+\frac bd t\right)
+b\left(y_0-\frac ad t\right).
$$

Al expandir,

$$
ax+by
=
ax_0+by_0+\frac{ab}{d}t-\frac{ab}{d}t
=c.
$$

Por tanto, cada valor entero de $t$ produce otra solución.


### 58

La ecuación es

$$
18x+30y=42.
$$

Como

$$
d=\gcd(18,30)=6,
$$

una solución particular sencilla es

$$
(x_0,y_0)=(4,-1),
$$

pues

$$
18\cdot4+30(-1)=72-30=42.
$$

La fórmula general da

$$
x=4+\frac{30}{6}t=4+5t,
$$

$$
y=-1-\frac{18}{6}t=-1-3t.
$$

Así,

$$
\boxed{
x=4+5t,\qquad y=-1-3t,\qquad t\in\mathbb Z
}.
$$

Para probar exhaustividad, sea $(x,y)$ otra solución. Restando la ecuación de $(4,-1)$,

$$
18(x-4)+30(y+1)=0.
$$

Dividiendo por $6$,

$$
3(x-4)=-5(y+1).
$$

Como $\gcd(3,5)=1$, la cancelación coprima implica que $5\mid(x-4)$. Por tanto,

$$
x-4=5t
$$

para algún $t\in\mathbb Z$. Sustituyendo,

$$
3(5t)=-5(y+1),
$$

de donde

$$
y+1=-3t.
$$

Por tanto, toda solución pertenece a la familia dada.


### 59

Ya sabemos que

$$
\gcd(84,30)=6
$$

y que una solución particular es

$$
(x_0,y_0)=(-1,3).
$$

Por tanto,

$$
x=-1+\frac{30}{6}t=-1+5t,
$$

$$
y=3-\frac{84}{6}t=3-14t.
$$

Así,

$$
\boxed{
x=-1+5t,\qquad y=3-14t,\qquad t\in\mathbb Z
}.
$$

Verificamos:

$$
84(-1+5t)+30(3-14t)
=-84+420t+90-420t
=6.
$$

La familia satisface la ecuación para todo $t\in\mathbb Z$. La exhaustividad sigue del teorema general de clasificación: cualquier otra solución difiere de $(-1,3)$ en un múltiplo de $(5,-14)$, porque $30/6=5$ y $84/6=14$.


### 60

La identidad dada es

$$
1=11\cdot35-6\cdot64.
$$

Por tanto, una solución particular es

$$
(x_0,y_0)=(11,-6).
$$

Como $\gcd(35,64)=1$, la fórmula general es

$$
x=11+64t,
$$

$$
y=-6-35t,
$$

con $t\in\mathbb Z$.

Así,

$$
\boxed{
(x,y)=(11+64t,\,-6-35t),
\qquad t\in\mathbb Z
}.
$$

La sustitución directa produce

$$
35(11+64t)+64(-6-35t)=385-384=1.
$$

La exhaustividad sigue de la clasificación general con $d=1$: toda solución difiere de $(11,-6)$ en un múltiplo entero de $(64,-35)$.



### 61

Consideramos

$$
-21x+15y=3.
$$

El MCD de $-21$ y $15$ es

$$
d=3.
$$

Una solución particular es

$$
(x_0,y_0)=(2,3),
$$

pues

$$
-21\cdot2+15\cdot3=-42+45=3.
$$

La fórmula general debe respetar el signo de $a=-21$:

$$
x=x_0+\frac{b}{d}t=2+5t,
$$

$$
y=y_0-\frac{a}{d}t
=3-(-7)t
=3+7t.
$$

Por tanto,

$$
\boxed{
x=2+5t,\qquad y=3+7t,\qquad t\in\mathbb Z
}.
$$

Verificación:

$$
-21(2+5t)+15(3+7t)
=-42-105t+45+105t
=3.
$$


### 62

La ecuación

$$
0x+7y=21
$$

se reduce a

$$
7y=21.
$$

Por tanto,

$$
y=3.
$$

La variable $x$ no aparece en la ecuación y queda completamente libre. Así,

$$
\boxed{(x,y)=(t,3),\qquad t\in\mathbb Z}.
$$

La fórmula general usada cuando ambos coeficientes son no nulos no debe aplicarse mecánicamente aquí, porque expresiones como

$$
\frac{a}{d}
$$

pueden ser $0$ y la deducción de exhaustividad basada en cancelar coeficientes reducidos cambia de naturaleza. El caso con un coeficiente cero se resuelve directamente.


### 63

La ecuación es

$$
18x+30y=96.
$$

Como

$$
\gcd(18,30)=6
$$

y $6\mid96$, hay soluciones. Dividimos por $6$:

$$
3x+5y=16.
$$

Una solución particular es

$$
(x_0,y_0)=(2,2),
$$

pues

$$
3\cdot2+5\cdot2=16.
$$

La familia completa de soluciones enteras es

$$
x=2+5t,
\qquad
y=2-3t,
\qquad t\in\mathbb Z.
$$

Ahora imponemos no negatividad:

$$
2+5t\ge0
$$

implica, para $t\in\mathbb Z$,

$$
t\ge0.
$$

Por otra parte,

$$
2-3t\ge0
$$

implica

$$
t\le0.
$$

Luego necesariamente

$$
t=0.
$$

La única solución entera no negativa es

$$
\boxed{(x,y)=(2,2)}.
$$


### 64

Sean $(x,y)$ y $(x_0,y_0)$ dos soluciones de

$$
ax+by=c.
$$

Restando,

$$
a(x-x_0)+b(y-y_0)=0,
$$

por lo que

$$
a(x-x_0)=-b(y-y_0).
$$

Sea

$$
d=\gcd(a,b),
\qquad
a=da',
\qquad
b=db'.
$$

Entonces

$$
a'(x-x_0)=-b'(y-y_0),
$$

y

$$
\gcd(a',b')=1.
$$

De

$$
a'\mid b'(y-y_0)
$$

y la coprimalidad $\gcd(a',b')=1$, el lema de cancelación coprima da

$$
a'\mid(y-y_0).
$$

Así existe $t\in\mathbb Z$ tal que

$$
y-y_0=-a't
=-\frac ad t.
$$

Sustituyendo en la igualdad reducida,

$$
a'(x-x_0)=b'a't,
$$

y, como $a'\ne0$ en el caso $ab\ne0$,

$$
x-x_0=b't
=\frac bd t.
$$

Por tanto, cuando $ab\ne0$,

$$
\boxed{
x=x_0+\frac bd t,\qquad
y=y_0-\frac ad t
}.
$$

Quedan los casos con un coeficiente cero. Si $a=0$, entonces $b\ne0$ y dos soluciones deben tener la misma coordenada $y=c/b$, mientras $x$ es libre; como $d=|b|$, la fórmula anterior se reduce precisamente a variar $x$ en pasos de $b/d=\pm1$. Si $b=0$, el argumento es simétrico: $x=c/a$ queda fijado y $y$ es libre. Así, también en los casos degenerados la descripción paramétrica, interpretada con cuidado, es exhaustiva.

Toda solución tiene exactamente la forma correspondiente. Esto prueba la exhaustividad.

## I. Diagnóstico y elección de método


### 65

La igualdad

$$
317=52\cdot5+57
$$

es aritméticamente correcta porque

$$
260+57=317.
$$

Sin embargo, no es una división con resto canónica: el resto debe satisfacer

$$
0\le r<52,
$$

y aquí

$$
57>52.
$$

Dividimos correctamente:

$$
317=52\cdot6+5.
$$

Como

$$
0\le5<52,
$$

la división canónica es

$$
\boxed{317=52\cdot6+5}.
$$


### 66

Primero verificamos la identidad propuesta:

$$
3\cdot252-4\cdot198
=756-792
=-36.
$$

Por tanto, no es igual a $18$.

Reconstruimos Bézout desde Euclides:

$$
252=198+54,
$$

$$
198=3\cdot54+36,
$$

$$
54=36+18.
$$

Entonces

$$
18=54-36.
$$

Como

$$
36=198-3\cdot54,
$$

se sigue que

$$
18=54-(198-3\cdot54)
=4\cdot54-198.
$$

Y como

$$
54=252-198,
$$

obtenemos

$$
18=4(252-198)-198
=4\cdot252-5\cdot198.
$$

La identidad correcta es

$$
\boxed{18=4\cdot252-5\cdot198}.
$$

El error del estudiante consiste en haber escrito coeficientes que no verifican la igualdad; una identidad de Bézout debe comprobarse por sustitución.


### 67

**a) Calcular $\gcd(84,30)$.**

El método más eficiente es **Euclides completo**:

$$
84=2\cdot30+24,\qquad
30=24+6,\qquad
24=4\cdot6.
$$

Da rápidamente $6$.

**b) Demostrar $\gcd(7n+3,5n+2)=1$.**

Lo más eficiente es buscar **una combinación lineal estratégica**, es decir, un paso euclidiano simbólico:

$$
5(7n+3)-7(5n+2)=1.
$$

No conviene ejecutar un Euclides largo con parámetros.

**c) Decidir si $24x+36y=50$ es soluble.**

Usamos el **criterio diofántico**. Como

$$
\gcd(24,36)=12
$$

y

$$
12\nmid50,
$$

no hay solución.

**d) Encontrar todas las soluciones de $35x+64y=1$.**

Se necesita primero **Euclides extendido** para obtener una solución particular y luego **clasificación paramétrica** para describir todas. Una identidad es

$$
1=11\cdot35-6\cdot64,
$$

y de ella resulta

$$
x=11+64t,\qquad y=-6-35t.
$$

La elección del método depende de si buscamos un valor del MCD, un certificado de coprimalidad, una decisión de existencia o la familia completa de soluciones.


### 68

Buscamos una combinación que elimine $n$:

$$
5(7n+3)-7(5n+2)
=
35n+15-35n-14
=
1.
$$

Sea $d$ un divisor común de $7n+3$ y $5n+2$. Entonces $d$ divide cualquier combinación lineal de ambos, en particular $1$. Por tanto,

$$
d\mid1.
$$

Así,

$$
\boxed{\gcd(7n+3,5n+2)=1}.
$$


### 69

Observamos que

$$
6n+9=3(2n+3)
$$

y

$$
4n+6=2(2n+3).
$$

Por tanto,

$$
2n+3
$$

divide a ambos números, y así $|2n+3|$ es un divisor común positivo.

Sea $d$ cualquier divisor común de $6n+9$ y $4n+6$. Entonces

$$
d\mid(6n+9)-(4n+6)=2n+3.
$$

Así, todo divisor común divide a $|2n+3|$. Por la definición universal,

$$
\boxed{\gcd(6n+9,4n+6)=|2n+3|}.
$$

Como $n\in\mathbb Z$, nunca ocurre $2n+3=0$, de modo que el lado derecho es siempre positivo.


### 70

Calculamos

$$
3(4n+1)-2(6n+1)
=
12n+3-12n-2
=
1.
$$

Sea $d$ un divisor común de $4n+1$ y $6n+1$. Entonces $d$ divide esa combinación lineal, y por tanto

$$
d\mid1.
$$

Así,

$$
\boxed{\gcd(4n+1,6n+1)=1}
$$

para todo $n\in\mathbb Z$.


### 71

La afirmación es verdadera.

Supongamos que existen enteros $x,y$ tales que

$$
ax+by=1.
$$

Sea $d$ cualquier divisor común de $a$ y $b$. Como todo divisor común divide toda combinación lineal,

$$
d\mid(ax+by).
$$

Por tanto,

$$
d\mid1.
$$

Así, los únicos divisores comunes posibles son $\pm1$, y el MCD positivo es

$$
\boxed{\gcd(a,b)=1}.
$$

El papel decisivo de la propiedad de combinaciones lineales es convertir una sola igualdad $ax+by=1$ en un certificado universal: fuerza a todos los divisores comunes a dividir a $1$.


### 72

Primero separamos $a=b=0$. Una pareja que satisface la ecuación implica entonces $c=0$, y todas las parejas de $\mathbb Z^2$ son soluciones; no se introduce $\gcd(0,0)$. La existencia de una pareja tampoco basta por sí sola como explicación de esa clasificación, que se obtiene directamente de $0=0$. En lo que sigue suponemos $(a,b)\ne(0,0)$.

Encontrar una pareja

$$
(x_0,y_0)
$$

con

$$
ax_0+by_0=c
$$

demuestra dos cosas:

1. que la ecuación es soluble;
2. que $(x_0,y_0)$ es una solución particular.

Pero no describe necesariamente todas las soluciones.

Para completar el problema hay que demostrar que toda otra solución $(x,y)$ difiere de $(x_0,y_0)$ por

$$
x-x_0=\frac bd t,
\qquad
y-y_0=-\frac ad t
$$

para algún $t\in\mathbb Z$, donde

$$
d=\gcd(a,b).
$$

Así, la familia completa es

$$
\boxed{
x=x_0+\frac bd t,\qquad
y=y_0-\frac ad t,\qquad
t\in\mathbb Z
}.
$$

La verificación de que esta familia produce soluciones usa cancelación algebraica. Si $ab\ne0$, la exhaustividad usa la ecuación homogénea obtenida al restar dos soluciones y el lema de cancelación coprima. Si $a=0$, la ecuación fija $y=c/b$ y deja $x$ libre; el paso $b/d=\pm1$ recorre todos los enteros. Si $b=0$, se fija $x=c/a$ y el paso $-a/d=\pm1$ recorre todos los valores de $y$. Así también se justifican las familias con un único coeficiente cero.

## M. Problemas avanzados tipo prueba


### 73

Sean $a,b,q\in\mathbb Z$ con $b\ne0$. Definamos

$$
r=a-qb.
$$

Queremos comparar los divisores comunes de $(a,b)$ y $(b,r)$.

Supongamos que $d$ divide a $a$ y a $b$. Entonces

$$
r=a-qb
$$

es una combinación lineal de $a$ y $b$, por lo que

$$
d\mid r.
$$

Así, $d$ divide a $b$ y a $r$.

Recíprocamente, supongamos que $d$ divide a $b$ y a $r$. Como

$$
a=qb+r,
$$

se sigue que

$$
d\mid a.
$$

Por tanto,

$$
d\mid a,\ d\mid b
\iff
d\mid b,\ d\mid(a-qb).
$$

Los dos pares tienen exactamente el mismo conjunto de divisores comunes. El posible signo de $a-qb$ no altera nada, porque

$$
d\mid(a-qb)
\iff
d\mid-(a-qb).
$$

Como el MCD es el divisor común positivo que satisface la propiedad universal,

$$
\boxed{\gcd(a,b)=\gcd(b,a-qb)}.
$$

Esta identidad contiene el mecanismo local completo de Euclides: cada paso reemplaza el par actual por otro con exactamente los mismos divisores comunes, pero con un segundo componente menor que el divisor positivo cuando, después de normalizar los signos, $q$ es el cociente de la división canónica. La identidad de MCD es válida con $b$ negativo; el teorema de división canónica de [§15.4](algebra-para-matematicos-capitulo-15-maximo-comun-divisor-y-algoritmo-de-euclides.md#apm-c15-s04) se aplica con divisor positivo.


### 74

Sea

$$
a\ge b>0.
$$

Fijamos $r_{-1}=a$ y $r_0=b$; la división de índice $i\ge1$ es $r_{i-2}=q_i r_{i-1}+r_i$, con $i\ge1$. Sólo se realiza un nuevo paso mientras su divisor sea positivo.

Aplicamos sucesivamente el algoritmo de división:

$$
a=q_1b+r_1,
\qquad
0\le r_1<b,
$$

$$
b=q_2r_1+r_2,
\qquad
0\le r_2<r_1,
$$

y así sucesivamente.

**1. Terminación.**

Mientras los restos sean no nulos,

$$
b>r_1>r_2>\cdots>0.
$$

No puede existir una sucesión infinita estrictamente decreciente de enteros positivos. En efecto, si existiera, el conjunto de sus valores tendría por buen orden un mínimo $m>0$, pero el paso siguiente produciría un resto positivo menor que $m$. Contradicción.

Por tanto, existe un índice $s\ge0$ tal que $r_s>0$ y el primer resto cero es

$$
r_{s+1}=0.
$$

**2. Conservación de divisores comunes.**

Cada división satisface $r_{i-2}=q_i r_{i-1}+r_i$ y, por tanto, $r_i=r_{i-2}-q_i r_{i-1}$. Si un entero no nulo $d$ divide a $r_{i-2}$ y $r_{i-1}$, la segunda igualdad prueba que divide a $r_i$. Si divide a $r_{i-1}$ y $r_i$, la primera prueba que divide a $r_{i-2}$. Así los pares $(r_{i-2},r_{i-1})$ y $(r_{i-1},r_i)$ tienen exactamente los mismos divisores comunes. La afirmación vale también cuando el nuevo resto es cero. Por repetición, el par inicial y el terminal comparten todos sus divisores comunes.

**3. Identificación del MCD.**

El algoritmo termina con

$$
r_{s-1}=q_{s+1}r_s+0.
$$

Por tanto,

$$
r_s\mid r_{s-1}.
$$

Así, $r_s$ divide a ambos elementos del último par y todo divisor común del último par divide a $r_s$. Como $r_s>0$,

$$
r_s=\gcd(r_{s-1},r_s).
$$

Por invariancia de los divisores comunes,

$$
\boxed{\gcd(a,b)=r_s}.
$$

La prueba de **terminación** usa únicamente el descenso de restos y buen orden. La prueba de **corrección** usa la invariancia de divisores comunes y la estructura del último paso. Son afirmaciones lógicamente distintas.


### 75

Aplicamos Euclides:

$$
252=198+54,
$$

$$
198=3\cdot54+36,
$$

$$
54=36+18,
$$

$$
36=2\cdot18.
$$

Por tanto,

$$
d=\gcd(252,198)=18.
$$

Sustituyendo hacia atrás,

$$
18=54-36,
$$

$$
36=198-3\cdot54,
$$

de modo que

$$
18=4\cdot54-198.
$$

Como

$$
54=252-198,
$$

obtenemos

$$
\boxed{18=4\cdot252-5\cdot198}.
$$

Así, un par de coeficientes es

$$
(x_0,y_0)=(4,-5).
$$

Como

$$
\frac{198}{18}=11,
\qquad
\frac{252}{18}=14,
$$

todos los pares que representan $18$ tienen la forma

$$
x=4+11t,
\qquad
y=-5-14t.
$$

Tomando $t=0,1,-1$ obtenemos, por ejemplo,

$$
\boxed{(4,-5),\ (15,-19),\ (-7,9)}.
$$

Verificación del segundo:

$$
252\cdot15+198(-19)=3780-3762=18.
$$

Verificación del tercero:

$$
252(-7)+198\cdot9=-1764+1782=18.
$$

Estructuralmente, si

$$
18=252x_0+198y_0,
$$

entonces para cualquier $t$

$$
252(x_0+11t)+198(y_0-14t)
$$

añade

$$
252\cdot11t-198\cdot14t=2772t-2772t=0.
$$

Por eso los coeficientes de Bézout no son únicos.


### 76

Sea

$$
L=\{ax+by:x,y\in\mathbb Z\},
\qquad
d=\gcd(a,b).
$$

Demostraremos las dos inclusiones.

**Primera inclusión: $L\subseteq d\mathbb Z$.**

Como

$$
d\mid a
\qquad\text{y}\qquad
d\mid b,
$$

se tiene

$$
d\mid(ax+by)
$$

para todos $x,y\in\mathbb Z$. Por tanto, cada elemento de $L$ es múltiplo de $d$:

$$
L\subseteq d\mathbb Z.
$$

Aquí no se usa Bézout.

**Segunda inclusión: $d\mathbb Z\subseteq L$.**

Por Bézout existen $x_0,y_0\in\mathbb Z$ tales que

$$
d=ax_0+by_0.
$$

Sea $dm$ un múltiplo arbitrario de $d$. Multiplicando por $m$,

$$
dm=a(mx_0)+b(my_0).
$$

Como $mx_0,my_0\in\mathbb Z$,

$$
dm\in L.
$$

Por tanto,

$$
d\mathbb Z\subseteq L.
$$

Concluimos

$$
\boxed{\{ax+by:x,y\in\mathbb Z\}=d\mathbb Z}.
$$

La identidad de Bézout se usa exactamente en la segunda inclusión.


### 77

Supongamos

$$
\gcd(a,b)=1
\qquad\text{y}\qquad
a\mid bc.
$$

Por Bézout existen $x,y\in\mathbb Z$ tales que

$$
ax+by=1.
$$

Multiplicando por $c$,

$$
acx+bcy=c.
$$

El primer término es divisible por $a$. El segundo también lo es porque $a\mid bc$, y entonces

$$
a\mid bcy.
$$

Por cierre bajo suma,

$$
a\mid c.
$$

Así,

$$
\boxed{
\gcd(a,b)=1,\ a\mid bc
\Longrightarrow
a\mid c
}.
$$

Si eliminamos la coprimalidad, la afirmación puede fallar. Por ejemplo,

$$
6\mid3\cdot2,
$$

pero

$$
6\nmid2.
$$

Aquí

$$
\gcd(6,3)=3\ne1.
$$

La propiedad anticipa una idea central de la teoría multiplicativa: bajo hipótesis adecuadas, ciertos factores pueden cancelarse dentro de una relación de divisibilidad. Sin embargo, todavía no hemos introducido primos ni factorización; por eso este lema prepara C16 pero no sustituye su teoría.


### 78

Consideramos

$$
84x+30y=c.
$$

**a) MCD.**

Euclides da

$$
84=2\cdot30+24,
$$

$$
30=24+6,
$$

$$
24=4\cdot6.
$$

Luego

$$
\boxed{\gcd(84,30)=6}.
$$

**b) Criterio de existencia.**

La ecuación tiene solución entera si y sólo si

$$
\boxed{6\mid c}.
$$

Escribamos entonces

$$
c=6m.
$$

**c) Solución particular.**

Como

$$
6=-84+3\cdot30,
$$

multiplicando por $m$ obtenemos

$$
c=-84m+30(3m).
$$

Una solución particular es

$$
\boxed{x_0=-m,\qquad y_0=3m}.
$$

Equivalente, en función de $c$,

$$
x_0=-\frac c6,
\qquad
y_0=\frac c2.
$$

**d) Todas las soluciones.**

Como

$$
\frac{30}{6}=5,
\qquad
\frac{84}{6}=14,
$$

la familia es

$$
\boxed{
x=-m+5t,\qquad
y=3m-14t,\qquad
t\in\mathbb Z
}.
$$

**e) Exhaustividad.**

Sea $(x,y)$ cualquier otra solución. Restamos la ecuación satisfecha por $(x_0,y_0)$:

$$
84(x-x_0)+30(y-y_0)=0.
$$

Dividiendo por $6$,

$$
14(x-x_0)=-5(y-y_0).
$$

Como

$$
\gcd(14,5)=1,
$$

de

$$
5\mid14(x-x_0)
$$

se sigue, por cancelación coprima,

$$
5\mid(x-x_0).
$$

Por tanto,

$$
x-x_0=5t
$$

para algún $t\in\mathbb Z$. Sustituyendo,

$$
14(5t)=-5(y-y_0),
$$

de donde

$$
y-y_0=-14t.
$$

Así, toda solución pertenece a la familia anterior. La parametrización es exhaustiva.


### 79

La supuesta ejecución contiene varios errores.

La primera división,

$$
662=414\cdot1+248,
$$

es correcta y canónica porque

$$
0\le248<414.
$$

La segunda línea es

$$
414=248\cdot2-82.
$$

Aunque la igualdad es correcta,

$$
496-82=414,
$$

el resto $-82$ es negativo y no satisface la condición canónica

$$
0\le r<248.
$$

La división correcta es

$$
\boxed{414=248\cdot1+166}.
$$

La línea siguiente,

$$
248=82\cdot1+166,
$$

también es aritméticamente cierta, pero no es un paso euclidiano válido: el resto $166$ no cumple

$$
166<82.
$$

Además, se ha cambiado indebidamente el divisor de $248$ a $82$ sin que $82$ sea el resto canónico de la línea anterior.

Desde la división correcta

$$
414=248+166
$$

debemos continuar con

$$
\boxed{248=166\cdot1+82}.
$$

Luego,

$$
\boxed{166=82\cdot2+2}
$$

y

$$
\boxed{82=2\cdot41+0}.
$$

Por tanto, la ejecución válida completa es

$$
662=414+248,
$$

$$
414=248+166,
$$

$$
248=166+82,
$$

$$
166=2\cdot82+2,
$$

$$
82=41\cdot2+0.
$$

El último resto no nulo es $2$, así que la conclusión

$$
\gcd(662,414)=2
$$

sí era correcta, pero estaba apoyada en una cadena defectuosa.

Ahora auditamos la supuesta identidad

$$
2=3\cdot414-2\cdot662.
$$

El lado derecho vale

$$
1242-1324=-82,
$$

no $2$. Por tanto, la identidad es falsa.

Hacemos sustitución hacia atrás:

$$
2=166-2\cdot82,
$$

$$
82=248-166,
$$

por lo que

$$
2=3\cdot166-2\cdot248.
$$

Como

$$
166=414-248,
$$

obtenemos

$$
2=3\cdot414-5\cdot248.
$$

Finalmente,

$$
248=662-414,
$$

y así

$$
\boxed{2=8\cdot414-5\cdot662}.
$$

Los coeficientes de Bézout tampoco son únicos. Como

$$
d=2,
$$

si una representación es

$$
2=414\cdot8+662(-5),
$$

entonces para cualquier $t\in\mathbb Z$,

$$
x=8+\frac{662}{2}t=8+331t,
$$

$$
y=-5-\frac{414}{2}t=-5-207t
$$

produce otra representación:

$$
2=414(8+331t)+662(-5-207t).
$$

Por tanto, la afirmación de unicidad es falsa.


### 80

Trabajamos con $662$ y $414$.

**1. Cálculo del MCD.**

Euclides da

$$
662=414+248,
$$

$$
414=248+166,
$$

$$
248=166+82,
$$

$$
166=2\cdot82+2,
$$

$$
82=41\cdot2+0.
$$

Por tanto,

$$
\boxed{\gcd(662,414)=2}.
$$

**2. Terminación e invariancia.**

En cada división canónica,

$$
r_{i-1}=q_i r_i+r_{i+1},
\qquad
0\le r_{i+1}<r_i.
$$

Mientras los restos sean positivos forman una sucesión estrictamente decreciente de enteros positivos, que debe terminar por el principio del buen orden.

Además,

$$
r_{i+1}=r_{i-1}-q_i r_i.
$$

Por ello, todo divisor común de $r_{i-1}$ y $r_i$ divide a $r_{i+1}$. Recíprocamente,

$$
r_{i-1}=q_i r_i+r_{i+1},
$$

de modo que todo divisor común de $r_i$ y $r_{i+1}$ divide a $r_{i-1}$. Así, cada paso conserva exactamente los divisores comunes. El último resto no nulo es entonces el MCD.

**3. Identidad de Bézout.**

Partimos de

$$
2=166-2\cdot82.
$$

Como

$$
82=248-166,
$$

$$
2=3\cdot166-2\cdot248.
$$

Como

$$
166=414-248,
$$

$$
2=3\cdot414-5\cdot248.
$$

Y como

$$
248=662-414,
$$

$$
\boxed{2=8\cdot414-5\cdot662}.
$$

**4. Solvencia de $414x+662y=2$.**

El MCD de $414$ y $662$ es $2$, y

$$
2\mid2.
$$

Por el criterio diofántico, la ecuación es soluble.

**5. Solución particular.**

La identidad de Bézout ya proporciona una:

$$
\boxed{x_0=8,\qquad y_0=-5}.
$$

**6. Todas las soluciones.**

Como

$$
\frac{662}{2}=331,
\qquad
\frac{414}{2}=207,
$$

la familia completa es

$$
\boxed{
x=8+331t,\qquad
y=-5-207t,\qquad
t\in\mathbb Z
}.
$$

Verificamos:

$$
414(8+331t)+662(-5-207t)
$$

$$
=3312+137034t-3310-137034t
=2.
$$

**7. Exhaustividad.**

Sea $(x,y)$ otra solución. Restando la ecuación de $(8,-5)$,

$$
414(x-8)+662(y+5)=0.
$$

Dividimos por $2$:

$$
207(x-8)=-331(y+5).
$$

Como

$$
\gcd(207,331)=1,
$$

de

$$
331\mid207(x-8)
$$

y la cancelación coprima se deduce

$$
331\mid(x-8).
$$

Por tanto,

$$
x-8=331t
$$

para algún $t\in\mathbb Z$. Sustituyendo,

$$
207(331t)=-331(y+5),
$$

y cancelando $331$,

$$
y+5=-207t.
$$

Así,

$$
x=8+331t,\qquad y=-5-207t.
$$

No existen otras soluciones.

**8. Balance conceptual.**

Todo el procedimiento usado hasta aquí descansa en:

- la definición de divisibilidad;
- el cierre de la divisibilidad bajo combinaciones lineales;
- el algoritmo de división;
- la invariancia de divisores comunes bajo el paso euclidiano;
- el principio del buen orden para garantizar terminación;
- la identidad de Bézout;
- la cancelación coprima;
- el criterio diofántico y la clasificación paramétrica.

Nada de esto exige todavía factorización prima ni congruencias. La perspectiva nueva que queda abierta para C16 es **multiplicativa**: estudiar enteros que no pueden descomponerse en factores no triviales, entender cómo los primos controlan los productos y analizar la factorización de los enteros. Ese será el siguiente nivel estructural.

## N. Certificados, restricciones y auditoría algorítmica


### 81

Las identidades son ciertas: $-3535+4444=909$ y $24745-24442=303$. Todo divisor común divide a 909, pero esto no convierte a 909 en divisor común: $3535=909\cdot3+808$, luego $909\nmid3535$. El primer certificado sólo acota los divisores comunes.

El segundo certificado tampoco produce un divisor común: $3535=303\cdot11+202$. Las dos combinaciones son verdaderas, pero por sí solas no certifican el MCD. Podemos buscar una combinación menor sin ejecutar la cadena de Euclides: $8B-5A=17776-17675=101$.

Ahora sí, $A=35\cdot101$ y $B=22\cdot101$. Por tanto 101 es divisor común positivo, y cualquier divisor común divide a $8B-5A=101$. La propiedad universal prueba $\gcd(A,B)=101$. Se han comprobado tanto la identidad como las dos divisibilidades. Una combinación verdadera puede producir un múltiplo del MCD; es el certificado completo el que identifica su valor.


### 82

Escribimos $u=3n+2$, de modo que $A=4u$ y $B=6u$. Como $n$ es entero, $u\ne0$: la igualdad $3n=-2$ no tiene solución entera. Así el par nunca es $(0,0)$. El número positivo $2|u|$ divide a ambas entradas, con testigos $2u/|u|$ y $3u/|u|$, ambos enteros.

Además $B-A=2u$. Todo divisor común divide a $2u$ y, por cambio de signo, a $2|u|$. Esto prueba la propiedad universal y da $\gcd(A,B)=2|3n+2|$. No necesitamos Euclides con parámetros. La identidad $3A-2B=0$ también es verdadera, pero no restringe los divisores comunes: todo entero no nulo divide a cero. El certificado útil produce el candidato positivo, o su opuesto, y se acompaña de la verificación de divisor común.


### 83

El certificado es cierto, $115-114=1$, y prueba que el MCD es uno. Multiplicar por menos siete entrega $(-35,42)$. La familia completa es

$$
(x,y)=(-35+19t,42-23t),\qquad t\in\mathbb Z.
$$

La sustitución da menos siete. Si $(x,y)$ es cualquier solución, $23(x+35)=-19(y-42)$; la coprimalidad de 23 y 19 obliga a $19\mid(x+35)$. Escribimos $x+35=19t$ y obtenemos $y-42=-23t$. Así no quedan parejas fuera de la familia.

La restricción equivale a $25\le19t\le43$, de donde $t=2$ es el único entero posible: $t\le1$ da $19t\le19$ y $t\ge3$ da $19t\ge57$. La única pareja restringida es $(3,-4)$, y $69-76=-7$. Una identidad ya disponible permite pasar directamente a la clasificación.


### 84

El lado derecho es $221-182=39$, no trece: la identidad propuesta es falsa. Aunque $221=17\cdot13$ y $91=7\cdot13$, estas dos igualdades sólo prueban que trece es divisor común.

Euclides da $221=2\cdot91+39$, $91=2\cdot39+13$, $39=3\cdot13$. Por invariancia y terminación, el MCD es trece. Hacia atrás, $13=91-2(221-2\cdot91)=-2\cdot221+5\cdot91$. La verificación es $-442+455=13$. Esta identidad correcta hace que todo divisor común divida a trece y completa el certificado universal. Un candidato que divide ambas entradas puede ser menor que el MCD; por ejemplo, uno también divide ambas, pero no es su MCD.


### 85

Si $n=0$, el lado izquierdo es cero. Para $c=0$ las soluciones son todas las parejas de $\mathbb Z^2$; bajo $x=y$, son $(t,t)$ con $t\in\mathbb Z$. Para $c\ne0$ no hay solución con ninguna de las dos condiciones. No se invoca $\gcd(0,0)$.

Si $n\ne0$, existe solución exactamente cuando $n\mid c$. En ese caso $q=c/n$ es entero y la ecuación fuerza $x=q$, mientras $y$ es libre: $(q,t)$, $t\in\mathbb Z$. Estas condiciones son necesarias por la igualdad $nx=c$ y suficientes por sustitución. Con $x=y$ queda sólo $(q,q)$. El signo de $n$ no cambia la divisibilidad; sí determina el signo del cociente. Si $n\nmid c$, no hay pareja entera.


### 86

Dividir la igualdad por menos catorce da $2x+3y=-1$. La pareja $(1,-1)$ la satisface. Como $\gcd(2,3)=1$, la familia completa es $(1+3t,-1-2t)$, $t\in\mathbb Z$. Para la exhaustividad, una solución arbitraria cumple $2(x-1)=-3(y+1)$, luego $3\mid x-1$ y se recupera ese parámetro. La sustitución verifica la ecuación original, con desplazamiento que respeta los signos.

Si $x,y\ge0$, el miembro original es no positivo y no puede valer catorce. También la familia exigiría $t\ge0$ y $t\le-1$ simultáneamente. Si $x,y\le0$, de $1+3t\le0$ resulta $t\le-1$, y de $-1-2t\le0$ resulta $t\ge0$; de nuevo no hay entero permitido. Por tanto hay infinitas soluciones enteras, pero ninguna en esos dos cuadrantes. Los signos iguales de los coeficientes no justifican cambiar el signo del término independiente sin cambiar toda la igualdad.


### 87

Si $n=0$, hay todas las parejas enteras para $c=0$ y ninguna para $c\ne0$. Con no negatividad, la primera alternativa se reduce a todas las parejas de enteros no negativos. No se define un MCD para las dos entradas cero.

Si $n\ne0$, la igualdad es $n(x-y)=c$, de modo que es soluble exactamente cuando $n\mid c$. Sea $m=c/n\in\mathbb Z$. Todas las parejas son $(m+t,t)$, $t\in\mathbb Z$: la sustitución prueba generación y una pareja arbitraria tiene necesariamente $t=y$ y $x=m+y$, lo que prueba exhaustividad.

Para no negatividad se necesita y basta $t\ge0$ y $t\ge-m$, es decir, $t\ge\max(0,-m)$. Este conjunto de enteros nunca es vacío y es infinito. Por tanto aquí la no negatividad no destruye la solvencia; permite desplazar ambas coordenadas hacia arriba. La conclusión vale para ambos signos de $n$ y de $c$.


### 88

En la primera ecuación, $y=-3$ y $x$ es libre antes de imponer restricciones. La desigualdad se convierte en $-2\le x-3\le2$, esto es, $1\le x\le5$. Las soluciones son $(1,-3),(2,-3),(3,-3),(4,-3),(5,-3)$. Son todas porque la ecuación fuerza la segunda coordenada y la desigualdad fuerza exactamente ese intervalo de enteros para la primera.

La ecuación $0x+0y=27$ no tiene soluciones. En cambio $0x+0y=0$ no fija ninguna coordenada. Bajo la restricción, todas sus parejas se describen como $(t,k-t)$, donde $t\in\mathbb Z$ y $k\in\{-2,-1,0,1,2\}$. Cada pareja tiene suma $k$; recíprocamente, dada una solución restringida, elegimos $t=x$ y $k=x+y$. Aquí se necesitan un parámetro libre y cinco elecciones de suma, no una familia que fije arbitrariamente una coordenada.


### 89

El MCD es uno: $1=2\cdot14-3\cdot9$, y uno divide ambas entradas. Una solución particular es $(9,0)$. Todas las soluciones enteras son $(9+9t,-14t)$, $t\in\mathbb Z$. La sustitución da 126. Restar la solución particular da $14(x-9)=-9y$; por coprimalidad, $9\mid x-9$, y la misma igualdad fuerza $y=-14t$. Esto prueba exhaustividad.

No negatividad exige $9+9t\ge0$ y $-14t\ge0$, equivalentes a $t\ge-1$ y $t\le0$. Los únicos enteros son $-1,0$. Obtenemos $(0,14)$ y $(9,0)$, que verifican $9\cdot14=126$ y $14\cdot9=126$. Las dos equivalencias sobre el parámetro prueban que no se omite ni se añade ninguna pareja.


### 90

Reducimos a $5x-3y=2$, con solución $(1,1)$ y coeficientes coprimos. Todas las soluciones son $(1+3t,1+5t)$, $t\in\mathbb Z$. La sustitución da cuatro en la ecuación original. Para probar exhaustividad, restar $(1,1)$ da $5(x-1)=3(y-1)$; por cancelación coprima, $3\mid x-1$, y luego $y-1=5t$.

La no negatividad de ambas coordenadas equivale, para parámetros enteros, a $t\ge0$: cualquier $t\le-1$ hace ambas negativas, y cualquier $t\ge0$ las hace positivas. Hay infinitas parejas. La suma es $2+8t$; exigir que sea a lo sumo veinte añade $8t\le18$, es decir, $t\le2$ para enteros. Quedan $t=0,1,2$, con parejas $(1,1),(4,6),(7,11)$. Las dos restricciones se impusieron sobre una familia ya exhaustiva, por lo que la lista también lo es.


### 91

La restricción obliga a $y=1-x$. Sustituir da $15x+21(1-x)=3m$, luego $21-6x=3m$ y $2x=7-m$. Por tanto existe una pareja entera exactamente cuando $7-m$ es par. Escribimos esta condición como $m=7-2k$ con $k\in\mathbb Z$. En ese caso la única pareja es $(k,1-k)$.

La sustitución comprueba $15k+21(1-k)=21-6k=3(7-2k)$ y la suma uno. El argumento comenzó con una solución arbitraria, así que demuestra exhaustividad y unicidad bajo la restricción. Sin ella, la ecuación es soluble para todo entero $m$, pues $\gcd(15,21)=3$ y $3\mid3m$. El obstáculo de paridad procede de la restricción añadida, no del criterio general de existencia.


### 92

La familia propuesta genera soluciones, porque $6(2+10s)+10(-1-6s)=2$. Pero el desplazamiento $(10,-6)$ es dos veces la dirección reducida $(5,-3)$. La familia completa es $(2+5t,-1-3t)$, $t\in\mathbb Z$. Para una solución arbitraria, $3(x-2)=-5(y+1)$ fuerza $5\mid x-2$, y después $y+1=-3t$; así la reparación es exhaustiva.

La restricción equivale a $-2\le5t\le10$, cuyos enteros posibles son $t=0,1,2$. Las parejas son $(2,-1),(7,-4),(12,-7)$. La propuesta selecciona $t=2s$, de modo que sólo obtiene las dos con parámetros cero y dos; pierde exactamente $(7,-4)$. Esta pareja verifica $42-40=2$, pero exigiría $s=1/2$. La falla es de exhaustividad, no de sustitución ni de solvencia.


### 93

Las cuatro igualdades son verdaderas: $48-5=43$, $10+2=12$, $-6+1=-5$ y $2=2$. No es una ejecución canónica: el primer resto es negativo y el segundo paso usa divisor negativo. Sin embargo, cada identidad conserva exactamente los divisores comunes del par consecutivo, pues los cocientes son enteros. Esta cadena concreta termina en $(1,0)$, por lo que certifica $\gcd(43,12)=1$.

Hacia atrás, $1=-5+3\cdot2$, $2=12+2(-5)$ y $-5=43-4\cdot12$. Así $1=7(-5)+3\cdot12=7\cdot43-25\cdot12$. Verificar $301-300=1$ confirma el certificado. La ejecución canónica sería $43=3\cdot12+7$, $12=7+5$, $7=5+2$, $5=2\cdot2+1$, $2=2\cdot1$. Que esta cadena alternativa termine no prueba que cualquier elección no canónica lo haga: el descenso debe justificarse por separado.


### 94

Las identidades $26=0\cdot15+26$ y $15=0\cdot26+15$ son verdaderas; intercambiar entradas conserva los divisores comunes. Pero la sucesión alterna $(26,15)$ y $(15,26)$ indefinidamente. No hay resto cero ni descenso. La invariancia no basta para demostrar terminación.

Con división canónica: $26=15+11$, $15=11+4$, $11=2\cdot4+3$, $4=3+1$, $3=3\cdot1+0$. Los restos positivos descienden y el par terminal identifica el MCD como uno. Hacia atrás, $1=4-3=3\cdot4-11=3\cdot15-4\cdot11=7\cdot15-4\cdot26$. Verificar $105-104=1$ prueba el certificado universal. La reparación impone una regla de progreso para todas las entradas normalizadas; no consiste sólo en detener manualmente el ciclo.


### 95

Sustituir la segunda igualdad en la primera entrega $a=b(q+k)+s$. El cociente reparado es $q+k\in\mathbb Z$ y el resto $s$ cumple $0\le s<b$, por lo que ésta es la división canónica; su unicidad procede del teorema de división. No se ha declarado falsa la igualdad original: se ha reparado la condición de resto.

Los pares $(b,r)$ y $(b,s)$ tienen los mismos divisores comunes porque $r=bk+s$ y $s=r-bk$. Además $(a,b)$ y $(b,r)$ los comparten. Como $b>0$, ninguno de estos pares es $(0,0)$, y sus MCD están definidos e iguales.

En el ejemplo, $-20=9(-3)+7$, así que $k=-3$, $s=7$ y $q+k=-6$. La división reparada es $-47=9(-6)+7$, cierta y con $0\le7<9$. Euclides sobre $(9,7)$ da $9=7+2$, $7=3\cdot2+1$, $2=2\cdot1$. Por tanto $\gcd(-47,9)=1$. La normalización del resto conserva la aritmética y añade el descenso que faltaba.


### 96

Las dos primeras filas verifican sus valores. En la tercera, la operación con restos da $11-2\cdot4=3$, pero los coeficientes registrados dan $168-150=18$. La recurrencia correcta resta dos veces cada coeficiente de la fila anterior: $(1,-3)-2(-1,4)=(3,-11)$. Así $3=3\cdot56-11\cdot15=168-165$.

La cadena canónica continúa con $4=3+1$ y $3=3\cdot1$. Entonces $1=4-3=(-1,4)-(3,-11)$ como combinación, y se obtiene $1=-4\cdot56+15\cdot15=-224+225$. El MCD es uno. Otro certificado es $1=11\cdot56-41\cdot15=616-615$, cuya pareja difiere por $(15,-56)$. Esa diferencia representa cero, por lo que ambos certificados son válidos. La no unicidad de Bézout permite parejas distintas que verifican la identidad; no permite aceptar una fila que representa un valor falso. Se auditó cada resto y cada combinación por separado.

***

[← Capítulo 14](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 16 →](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md)

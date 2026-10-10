---
{
  "title": "Los enteros y la divisibilidad",
  "description": "Capítulo 14 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0189",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C14",
  "editorial-id": "MA-BCH-APM-01-014",
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
    "MA-BCH-0188"
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

Hasta ahora hemos trabajado con expresiones, demostraciones, relaciones, funciones, inducción, sumas finitas y coeficientes binomiales. En todos esos temas los enteros aparecieron como objetos familiares sobre los cuales podíamos calcular. A partir de este capítulo cambia el punto de vista: comenzaremos a estudiar la aritmética de los enteros como una estructura matemática en sí misma.

El concepto inicial será elemental: que un entero **divida** a otro. Pero la familiaridad puede engañar. En matemáticas, escribir $a\mid b$ no significa que una calculadora pueda efectuar una división decimal; significa que existe un entero que sirve de cociente exacto. Esa condición de existencia convierte la divisibilidad en una relación apta para demostrar teoremas, construir contraejemplos, estudiar ecuaciones y organizar conjuntos de múltiplos.

La idea central del capítulo puede resumirse así:

> **Una afirmación de divisibilidad es una afirmación de existencia. Para demostrarla debemos producir, explícita o implícitamente, un testigo entero.**

Esta perspectiva nos permitirá pasar de preguntas como “¿$6$ divide a $42$?” a cuestiones más estructurales: ¿qué operaciones conservan la divisibilidad?, ¿qué puede deducirse de varios divisores comunes?, ¿qué relación hay entre $a\mid b$ y los conjuntos $a\mathbb Z$ y $b\mathbb Z$?, ¿cuándo una ecuación puede tener soluciones enteras?, ¿cómo puede una identidad algebraica fabricar divisibilidades?

Todavía no desarrollaremos el máximo común divisor, el algoritmo de Euclides, los números primos ni las congruencias. El objetivo es más básico y, a la vez, más profundo: obtener todo lo posible directamente de la definición de divisibilidad y de las combinaciones lineales.

***
## 14.1. Una ecuación que puede no tener solución entera {#apm-c14-s01}

Consideremos las ecuaciones

$$
6x=42
$$

y

$$
6x=43.
$$

Si el dominio es $\mathbb R$, ambas tienen solución:

$$
x=7
$$

y

$$
x=\frac{43}{6}.
$$

Pero si exigimos $x\in\mathbb Z$, la situación cambia. La primera ecuación conserva la solución $x=7$, mientras que la segunda no tiene solución entera.

La diferencia no está en que una ecuación sea “más difícil” que la otra. Está en una propiedad aritmética precisa: $42$ puede escribirse como $6$ multiplicado por un entero, mientras que $43$ no.

En efecto,

$$
42=6\cdot7,
$$

pero no existe ningún $q\in\mathbb Z$ tal que

$$
43=6q.
$$

Esto sugiere que, cuando trabajamos sobre los enteros, una ecuación de la forma

$$
ax=b
$$

no debe analizarse solamente mediante la operación formal “dividir ambos lados por $a$”. La pregunta decisiva es otra:

> **¿Existe un entero $x$ tal que $b=ax$?**

Ese problema de existencia es exactamente el que codificará la relación de divisibilidad.

Obsérvese el cambio de perspectiva. En álgebra elemental solemos interpretar

$$
x=\frac{b}{a}
$$

como una expresión válida siempre que $a\ne0$. En aritmética entera, en cambio, el número $b/a$ puede existir como racional y, sin embargo, no pertenecer a $\mathbb Z$. Por eso el dominio forma parte esencial del problema.

Por ejemplo,

$$
8x=-56
$$

tiene la solución entera $x=-7$, pero

$$
8x=-55
$$

no la tiene. Los signos no son el obstáculo: lo relevante es si el término independiente es un múltiplo entero del coeficiente.

Esta observación proporciona la puerta de entrada al concepto fundamental del capítulo.

***
## 14.2. Definición de divisibilidad y testigos {#apm-c14-s02}

Sean $a,b\in\mathbb Z$ con $a\ne0$. Diremos que **$a$ divide a $b$** si existe un entero $q$ tal que

$$
b=aq.
$$

Lo escribimos

$$
a\mid b.
$$

Formalmente,

$$
\boxed{
a\mid b
\iff
\exists q\in\mathbb Z:\ b=aq
}
$$

con la convención, fijada para este tomo, de que el divisor $a$ es siempre no nulo.

El entero $q$ es un **testigo de divisibilidad**. Si queremos demostrar que $a\mid b$, basta exhibir un entero que cumpla la ecuación requerida.

Por ejemplo,

$$
7\mid42
$$

porque

$$
42=7\cdot6.
$$

Aquí $6$ es un testigo.

También

$$
-7\mid42
$$

porque

$$
42=(-7)(-6),
$$

y

$$
7\mid(-42)
$$

porque

$$
-42=7(-6).
$$

La definición no privilegia los enteros positivos. El testigo puede ser positivo, negativo o cero.

En cambio,

$$
5\nmid18,
$$

porque no existe $q\in\mathbb Z$ tal que $18=5q$. El cociente $18/5$ existe en $\mathbb Q$, pero no es un entero. Por tanto, no sirve como testigo.

Conviene mantener simultáneamente tres lecturas de una misma afirmación:

$$
a\mid b;
$$

“$a$ divide a $b$”;

$$
b=aq\quad\text{para algún }q\in\mathbb Z;
$$

y

“existe un testigo entero que expresa a $b$ como múltiplo de $a$”.

Esta tercera lectura será especialmente útil en las demostraciones. Cuando una hipótesis diga $a\mid b$, casi siempre el primer paso será **desplegar la definición** y escribir

$$
b=aq
$$

para algún $q\in\mathbb Z$.

Análogamente, para demostrar una conclusión del tipo $a\mid c$, tendremos que llegar a una igualdad

$$
c=ar
$$

con $r\in\mathbb Z$.

La divisibilidad será, por tanto, un entrenamiento continuo en el uso matemático de los cuantificadores existenciales estudiados en C6.

### Nota pedagógica — El dominio del testigo es parte de la afirmación

Para $a\ne0$, la igualdad $b=aq$ determina un único candidato $q=b/a$. Encontrarlo en $\mathbb Q$ todavía no prueba $a\mid b$: falta demostrar que pertenece a $\mathbb Z$. Si se permitieran testigos racionales, cualquier entero no nulo dividiría a cualquier entero y desaparecería la distinción que estamos estudiando.

Hay dos formas de cerrar una prueba. Para afirmar divisibilidad, escribe $b=aQ$ y explica por qué $Q$ es entero. Para negarla, descarta el único candidato o demuestra que ninguna posición de la lista de múltiplos puede dar $b$. No hace falta probar infinitos cocientes uno a uno.

**Control resuelto.** Para $m\in\mathbb Z$, $7\mid(14m-7)$ porque $14m-7=7(2m-1)$. El testigo $2m-1$ es entero incluso si $m$ es negativo. En cambio, $7\nmid(14m-4)$: una igualdad $14m-4=7q$ obligaría a $7[q-(2m-1)]=3$. El entero entre corchetes no puede ser cero, porque el lado derecho no lo es; si fuera no nulo, el valor absoluto del lado izquierdo sería al menos siete. Como $|3|<7$, hay contradicción.

**Qué revisar al dividir.** La división puede conservar una igualdad racional y perder la condición de testigo entero. Incluso si el resultado final es entero, su cociente por el divisor puede no serlo: $6/2=3$ es entero, pero no es múltiplo de seis. La condición decisiva debe comprobarse después de la transformación.

***
## 14.3. Múltiplos y divisores {#apm-c14-s03}

Si $a\mid b$, utilizamos tres expresiones equivalentes:

- $a$ **divide** a $b$;
- $a$ es un **divisor** de $b$;
- $b$ es un **múltiplo** de $a$.

Por ejemplo, como

$$
30=5\cdot6,
$$

podemos decir que $5$ divide a $30$, que $5$ es un divisor de $30$ o que $30$ es un múltiplo de $5$.

Para un entero no nulo $a$, sus múltiplos forman la sucesión bilateral

$$
\ldots,-3a,-2a,-a,0,a,2a,3a,\ldots
$$

que más adelante escribiremos de forma compacta como $a\mathbb Z$.

Por ejemplo, los múltiplos de $4$ son

$$
\ldots,-12,-8,-4,0,4,8,12,\ldots
$$

y los múltiplos de $-4$ son exactamente los mismos números. Esto anticipa una propiedad importante: cambiar el signo del divisor no cambia el conjunto de sus múltiplos.

Los divisores de un entero fijo se comportan de manera diferente. Para $12$, por ejemplo, los divisores son

$$
\pm1,\ \pm2,\ \pm3,\ \pm4,\ \pm6,\ \pm12.
$$

En cambio, $5$ no es divisor de $12$ porque $12/5$ no es entero.

Un entero no nulo tiene sólo una cantidad finita de divisores. Más adelante probaremos formalmente la razón: si $d\mid n$ y $n\ne0$, entonces

$$
|d|\le |n|.
$$

Por tanto, cualquier divisor de $n$ debe encontrarse dentro del conjunto finito de enteros comprendidos entre $-|n|$ y $|n|$.

Esta observación también ayuda a evitar una confusión frecuente. Ser divisor no significa simplemente ser menor en valor absoluto. Por ejemplo,

$$
4<10,
$$

pero

$$
4\nmid10.
$$

La divisibilidad no es una comparación de tamaños; es una condición de multiplicación exacta.

Tampoco debemos confundir “$a$ divide a $b$” con “$b$ divide a $a$”. Por ejemplo,

$$
3\mid12,
$$

pero

$$
12\nmid3.
$$

La relación tiene una dirección, y esa dirección será crucial cuando la estudiemos como relación matemática.

***
## 14.4. Signos, cero y divisores universales {#apm-c14-s04}

La definición permite controlar los signos sin necesidad de memorizar reglas separadas.

Supongamos que $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Pero también

$$
b=(-a)(-q),
$$

de modo que

$$
(-a)\mid b.
$$

Además,

$$
-b=a(-q),
$$

por lo que

$$
a\mid(-b).
$$

En consecuencia, para $a\ne0$,

$$
\boxed{
a\mid b
\iff
(-a)\mid b
\iff
 a\mid(-b)
}.
$$

El signo no altera la divisibilidad esencial; sólo modifica el signo del testigo.

Hay dos divisores que aparecen en todos los enteros. Para cualquier $n\in\mathbb Z$,

$$
n=1\cdot n
$$

y

$$
n=(-1)(-n).
$$

Por tanto,

$$
1\mid n
\qquad\text{y}\qquad
-1\mid n
$$

para todo entero $n$.

El cero exige más cuidado. Si $a\ne0$, entonces

$$
0=a\cdot0,
$$

de modo que

$$
\boxed{a\mid0\quad\text{para todo }a\ne0.}
$$

Así, todo entero no nulo divide a $0$.

Pero en este tomo **no admitimos a $0$ como divisor**. Nuestra definición de $a\mid b$ incluye explícitamente la hipótesis $a\ne0$. Por tanto, expresiones del tipo

$$
0\mid b
$$

quedan fuera de la relación definida aquí.

Esta convención evita mezclar dos cuestiones distintas. Si uno permitiera formalmente $0\mid0$, la ecuación $0=0q$ tendría infinitos testigos; si $b\ne0$, la ecuación $b=0q$ no tendría ninguno. Algunos textos adoptan convenciones diferentes. Nosotros mantendremos una sola regla estable en C14–C17:

> **el divisor de una expresión $a\mid b$ debe ser no nulo.**

Así, cada vez que usemos divisibilidad podremos contar con esa hipótesis sin tener que reabrir la convención.

***
## 14.5. El cálculo elemental de la divisibilidad {#apm-c14-s05}

Las primeras propiedades de la divisibilidad se obtienen directamente construyendo testigos.

### Reflexividad

Si $a\ne0$, entonces

$$
a=a\cdot1.
$$

Como $1\in\mathbb Z$,

$$
\boxed{a\mid a.}
$$

La relación de divisibilidad es, por tanto, reflexiva sobre los enteros no nulos.

### Multiplicar un múltiplo

Si $a\mid b$, existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Para cualquier $c\in\mathbb Z$,

$$
bc=(aq)c=a(qc).
$$

Como $qc\in\mathbb Z$,

$$
\boxed{a\mid bc.}
$$

El nuevo testigo es $qc$.

### Transitividad

Supongamos

$$
a\mid b
\qquad\text{y}\qquad
b\mid c,
$$

con $a,b\ne0$. Entonces existen $r,s\in\mathbb Z$ tales que

$$
b=ar
$$

y

$$
c=bs.
$$

Sustituyendo,

$$
c=(ar)s=a(rs).
$$

Como $rs\in\mathbb Z$,

$$
\boxed{a\mid c.}
$$

### Suma y resta de múltiplos

Si

$$
a\mid b
\qquad\text{y}\qquad
 a\mid c,
$$

podemos escribir

$$
b=ar,
\qquad
c=as
$$

con $r,s\in\mathbb Z$. Entonces

$$
b+c=a(r+s)
$$

y

$$
b-c=a(r-s).
$$

Como $r+s$ y $r-s$ son enteros,

$$
\boxed{a\mid(b+c)}
$$

y

$$
\boxed{a\mid(b-c)}.
$$

Estas demostraciones ilustran el patrón que debe hacerse automático:

1. desplegar la hipótesis de divisibilidad;
2. nombrar los testigos;
3. operar algebraicamente;
4. identificar un nuevo testigo entero.

La frase “es obvio que sigue siendo divisible” puede ocultar precisamente el paso que una demostración debe justificar.

***
## 14.6. Combinaciones lineales {#apm-c14-s06}

La propiedad de suma y resta admite una forma mucho más potente.

Supongamos que $d\mid a$ y $d\mid b$. Entonces existen $u,v\in\mathbb Z$ tales que

$$
a=du,
\qquad
b=dv.
$$

Sean ahora $r,s\in\mathbb Z$. Consideremos la combinación

$$
ra+sb.
$$

Sustituyendo las expresiones anteriores,

$$
ra+sb
=r(du)+s(dv)
=d(ru+sv).
$$

Como $ru+sv\in\mathbb Z$, obtenemos

$$
\boxed{
d\mid a\ \text{y}\ d\mid b
\Longrightarrow
 d\mid(ra+sb)
}
$$

para cualesquiera $r,s\in\mathbb Z$.

La expresión $ra+sb$ se llama una **combinación lineal entera** de $a$ y $b$.

Esta propiedad contiene varios resultados anteriores como casos particulares. Si elegimos

$$
r=s=1,
$$

obtenemos $d\mid(a+b)$. Si elegimos

$$
r=1,
\qquad
s=-1,
$$

obtenemos $d\mid(a-b)$. Si tomamos $s=0$, recuperamos que cualquier múltiplo entero de $a$ sigue siendo divisible por $d$.

La utilidad real aparece cuando escogemos los coeficientes de manera estratégica. Supongamos, por ejemplo, que sabemos

$$
d\mid 84
$$

y

$$
d\mid 30.
$$

Entonces también

$$
d\mid(84-2\cdot30)=24,
$$

y luego

$$
d\mid(30-24)=6.
$$

Sin haber identificado todavía cuál es el “mejor” divisor común, hemos reducido dos números grandes a uno mucho menor usando únicamente combinaciones lineales.

La misma idea se extiende a cualquier cantidad finita de enteros. Si $d$ divide a cada uno de

$$
a_1,a_2,\ldots,a_n,
$$

entonces, para cualesquiera enteros $r_1,\ldots,r_n$,

$$
\boxed{
d\mid(r_1a_1+\cdots+r_na_n).}
$$

La demostración es idéntica: escribir $a_i=dq_i$ y factorizar $d$.

Esta propiedad será una de las herramientas longitudinales del bloque de aritmética. En C15 veremos que las combinaciones lineales no sólo producen nuevas divisibilidades: también permiten localizar un divisor común especialmente importante.

***
## 14.7. Cancelación, tamaño y divisibilidad mutua {#apm-c14-s07}

La divisibilidad permite ciertas cancelaciones, pero sólo bajo hipótesis controladas.

### Cancelación de un factor común

Sean $a,b,c\in\mathbb Z$ con $a\ne0$ y $c\ne0$. Supongamos

$$
ca\mid cb.
$$

Por definición, existe $q\in\mathbb Z$ tal que

$$
cb=(ca)q=c(aq).
$$

Como $c\ne0$, podemos cancelar $c$ en la igualdad de enteros y obtener

$$
b=aq.
$$

Por tanto,

$$
\boxed{ca\mid cb\Longrightarrow a\mid b}
$$

cuando el factor cancelado $c$ es no nulo.

Obsérvese que no estamos cancelando dentro del símbolo $\mid$ de forma puramente visual. Primero traducimos la divisibilidad a una igualdad y sólo entonces aplicamos una ley de cancelación válida.

### El tamaño de un divisor

Supongamos que

$$
a\mid b
$$

y que $b\ne0$. Entonces

$$
b=aq
$$

para algún $q\in\mathbb Z$. Como $b\ne0$, necesariamente $q\ne0$. Por tanto,

$$
|q|\ge1.
$$

Tomando valores absolutos,

$$
|b|=|a||q|\ge|a|.
$$

Luego

$$
\boxed{a\mid b,\ b\ne0\Longrightarrow |a|\le|b|.}
$$

Ésta es la razón formal por la cual un entero no nulo tiene sólo finitos divisores.

### Divisibilidad mutua

Supongamos ahora que $a,b\ne0$ y

$$
a\mid b
\qquad\text{y}\qquad
b\mid a.
$$

La primera divisibilidad da

$$
|a|\le|b|,
$$

y la segunda,

$$
|b|\le|a|.
$$

Por antisimetría del orden usual,

$$
|a|=|b|.
$$

Así,

$$
\boxed{a\mid b\ \text{y}\ b\mid a\Longrightarrow a=\pm b.}
$$

El signo es esencial. De

$$
2\mid(-2)
$$

y

$$
-2\mid2
$$

no podemos concluir $2=-2$.

Este detalle anticipa por qué la divisibilidad será un orden parcial sobre los enteros positivos, pero no sobre todos los enteros no nulos.

***
## 14.8. Divisibilidad como relación {#apm-c14-s08}

En C8 estudiamos relaciones mediante propiedades como reflexividad, simetría, antisimetría y transitividad. Podemos aplicar ahora ese lenguaje a la divisibilidad.

Consideremos primero la relación $\mid$ sobre

$$
\mathbb Z^*=\mathbb Z\setminus\{0\}.
$$

Ya sabemos que es **reflexiva**:

$$
a\mid a.
$$

También es **transitiva**:

$$
a\mid b,
\quad
b\mid c
\Longrightarrow
 a\mid c.
$$

No es simétrica. Por ejemplo,

$$
2\mid6,
$$

pero

$$
6\nmid2.
$$

Tampoco es antisimétrica sobre $\mathbb Z^*$. En efecto,

$$
2\mid(-2)
$$

y

$$
-2\mid2,
$$

pero $2\ne-2$.

El obstáculo es exactamente el signo. Si restringimos la relación al conjunto de enteros positivos

$$
\mathbb Z_{>0},
$$

la situación cambia.

Sean $a,b>0$ y supongamos

$$
a\mid b
\qquad\text{y}\qquad
b\mid a.
$$

Por divisibilidad mutua,

$$
a=\pm b.
$$

Como ambos son positivos, sólo es posible

$$
a=b.
$$

Así, sobre $\mathbb Z_{>0}$, la divisibilidad es reflexiva, antisimétrica y transitiva. Por tanto:

$$
\boxed{\mid\ \text{es un orden parcial sobre }\mathbb Z_{>0}.}
$$

No es un orden total. Por ejemplo, entre $2$ y $3$ no se cumple ni

$$
2\mid3
$$

ni

$$
3\mid2.
$$

Los dos elementos son incomparables respecto de la divisibilidad.

En un conjunto pequeño, como

$$
\{1,2,3,4,6,12\},
$$

podemos visualizar esta relación observando qué números dividen a cuáles. El $1$ está por debajo de todos en el orden de divisibilidad, mientras que $12$ recibe divisibilidad de varios elementos. Sin embargo, no desarrollaremos aquí teoría de retículos ni diagramas más generales; nos basta reconocer que una noción aritmética familiar posee una estructura relacional precisa.

***
## 14.9. El conjunto $a\mathbb Z$ y la inclusión invertida {#apm-c14-s09}

Para un entero no nulo $a$, definimos

$$
a\mathbb Z=\{ak:k\in\mathbb Z\}.
$$

Este conjunto contiene exactamente todos los múltiplos enteros de $a$.

Por ejemplo,

$$
2\mathbb Z
=
\{\ldots,-6,-4,-2,0,2,4,6,\ldots\}
$$

y

$$
6\mathbb Z
=
\{\ldots,-12,-6,0,6,12,\ldots\}.
$$

Se observa que

$$
6\mathbb Z\subseteq2\mathbb Z.
$$

La razón es que todo múltiplo de $6$ también es múltiplo de $2$.

Esta observación se generaliza.

### Proposición

Para $a,b\ne0$,

$$
\boxed{
a\mid b
\iff
b\mathbb Z\subseteq a\mathbb Z.
}
$$

### Demostración

Supongamos primero que $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Sea $x\in b\mathbb Z$. Por definición, existe $t\in\mathbb Z$ tal que

$$
x=bt.
$$

Sustituyendo $b=aq$,

$$
x=(aq)t=a(qt).
$$

Como $qt\in\mathbb Z$, se tiene $x\in a\mathbb Z$. Por tanto,

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

Recíprocamente, supongamos

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

Como

$$
b=b\cdot1,
$$

tenemos $b\in b\mathbb Z$. Por la inclusión, $b\in a\mathbb Z$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq,
$$

y por definición $a\mid b$.

La equivalencia queda demostrada.

Hay una inversión conceptual interesante:

$$
a\mid b
$$

significa que $b$ está “por encima” de $a$ en el orden de divisibilidad, pero al pasar a conjuntos de múltiplos obtenemos

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

La dirección se invierte.

También podemos caracterizar cuándo dos conjuntos de múltiplos son iguales. Si

$$
a\mathbb Z=b\mathbb Z,
$$

entonces tenemos simultáneamente

$$
a\mathbb Z\subseteq b\mathbb Z
$$

y

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

Por la equivalencia anterior,

$$
b\mid a
$$

y

$$
a\mid b.
$$

Luego

$$
a=\pm b.
$$

El recíproco es inmediato, pues $a$ y $-a$ tienen los mismos múltiplos. Así,

$$
\boxed{
a\mathbb Z=b\mathbb Z
\iff
 a=\pm b.
}
$$

Más adelante, en álgebra abstracta, conjuntos como $a\mathbb Z$ adquirirán interpretaciones adicionales. Aquí sólo necesitamos verlos como conjuntos de múltiplos y explotar la relación entre divisibilidad e inclusión.

### Nota pedagógica — Una inclusión requiere todos los múltiplos

La inversión de [§14.9](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md#apm-c14-s09) se controla siguiendo un elemento arbitrario. Si $b=aq$, entonces un múltiplo $bt$ de $b$ se convierte en $a(qt)$; éste es un múltiplo de $a$ porque $qt$ es entero. Para el sentido contrario basta examinar el generador $b=b\cdot1$. La palabra «todos» en la inclusión y la elección de un elemento concreto en el converso cumplen funciones distintas.

**Control parametrizado resuelto.** Sea $a\ne0$ y $m\ne0$. Todo elemento de $(am)\mathbb Z$ tiene forma $amt=a(mt)$, así que $(am)\mathbb Z\subseteq a\mathbb Z$. Si $m=1$ o $m=-1$, los conjuntos son iguales: cambiar el signo del parámetro del múltiplo recupera cualquier elemento. Si $|m|\ge2$, la inclusión es estricta. En efecto, $a\in a\mathbb Z$, pero una igualdad $a=amq$ exigiría $1=mq$ tras cancelar $a$. Ningún entero $q$ puede satisfacerla, pues $q=0$ da cero y $q\ne0$ da $|mq|\ge2$.

Por ejemplo, $(-15)\mathbb Z\subsetneq5\mathbb Z$, y el elemento $5$ prueba la estrictitud. Compartir algunos elementos, como cero o quince, no establece una inclusión. Tampoco un signo negativo cambia la dirección: son los testigos enteros, no el orden usual entre los números, los que deciden la relación.

El caso $m=0$ queda fuera de esta comparación entre generadores no nulos. Aunque el conjunto de productos $0t$ podría describirse como $\{0\}$, eso no autoriza a usar cero como divisor bajo la convención del capítulo.

***
## 14.10. Cómo demostrar una afirmación de divisibilidad {#apm-c14-s10}

Las pruebas de divisibilidad suelen ser cortas cuando se identifica correctamente el objetivo. El método fundamental es traducir el símbolo $\mid$ a una ecuación con un testigo entero.

Supongamos que queremos demostrar

$$
a\mid F
$$

para cierta expresión entera $F$. El objetivo equivale a construir un entero $q$ tal que

$$
F=aq.
$$

Un protocolo útil es el siguiente:

```text
1. IDENTIFICAR QUÉ DIVISIBILIDAD SE QUIERE PROBAR.
2. ESCRIBIR LA DEFINICIÓN EXISTENCIAL.
3. DESPLEGAR LAS HIPÓTESIS DE DIVISIBILIDAD COMO IGUALDADES.
4. CONSTRUIR UN NUEVO TESTIGO ENTERO.
5. SI HAY VARIAS HIPÓTESIS, PROBAR UNA COMBINACIÓN LINEAL.
6. SI LA AFIRMACIÓN PARECE FALSA, BUSCAR UN CONTRAEJEMPLO PEQUEÑO.
7. CONTROLAR SIGNOS Y CASOS CERO.
```

### Ejemplo de prueba directa

Supongamos

$$
6\mid n.
$$

Queremos demostrar

$$
3\mid n.
$$

La hipótesis significa que existe $q\in\mathbb Z$ tal que

$$
n=6q.
$$

Entonces

$$
n=3(2q).
$$

Como $2q\in\mathbb Z$, concluimos

$$
3\mid n.
$$

El testigo para la conclusión es $2q$.

### Un converso falso

El converso sería:

> si $3\mid n$, entonces $6\mid n$.

Es falso. Basta tomar

$$
n=3.
$$

Entonces $3\mid3$, pero $6\nmid3$.

No hace falta una teoría compleja para refutar una afirmación universal: un único contraejemplo basta.

### Contraposición

A veces una afirmación puede demostrarse mediante contraposición. Por ejemplo, la implicación

$$
6\mid n\Longrightarrow 2\mid n
$$

es equivalente a

$$
2\nmid n\Longrightarrow6\nmid n.
$$

Sin embargo, en divisibilidad elemental la prueba directa suele ser más transparente porque exhibe el testigo. Conviene elegir el método que haga visible la estructura, no el que simplemente parezca más sofisticado.

***
## 14.11. La ecuación $ax=b$ {#apm-c14-s11}

La definición de divisibilidad puede reinterpretarse exactamente como un criterio de solvencia para una ecuación lineal de una variable sobre los enteros.

Sea $a\ne0$. Consideremos

$$
ax=b,
\qquad x\in\mathbb Z.
$$

Afirmamos que

$$
\boxed{
ax=b\text{ tiene solución entera}
\iff
 a\mid b.
}
$$

### Demostración

Si la ecuación tiene una solución $x_0\in\mathbb Z$, entonces

$$
b=ax_0.
$$

Por definición,

$$
a\mid b.
$$

Recíprocamente, si $a\mid b$, existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Entonces $x=q$ es una solución entera de

$$
ax=b.
$$

La equivalencia está probada.

Esta formulación muestra que el “testigo” de la divisibilidad y la “solución” de la ecuación son exactamente el mismo entero.

Por ejemplo,

$$
15x=90
$$

tiene solución entera porque $15\mid90$, y el testigo $6$ proporciona

$$
x=6.
$$

En cambio,

$$
15x=92
$$

no tiene solución entera porque $15\nmid92$.

Además, cuando $a\ne0$, la solución entera —si existe— es única. Si

$$
ax_1=b
$$

y

$$
ax_2=b,
$$

entonces

$$
a(x_1-x_2)=0.
$$

Como $a\ne0$, se sigue que

$$
x_1-x_2=0,
$$

y por tanto

$$
x_1=x_2.
$$

Así, una ecuación $ax=b$ sobre los enteros tiene exactamente una de dos posibilidades: ninguna solución entera o una única solución entera.

En problemas con parámetros conviene separar tres preguntas:

1. ¿existe una solución entera?;
2. si existe, ¿cuál es?;
3. ¿para qué valores del parámetro existe?

La divisibilidad responde primero a la cuestión de existencia.

***
## 14.12. Ecuaciones diofánticas lineales de dos variables {#apm-c14-s12}

Una **ecuación diofántica** es, en términos generales, una ecuación en la que buscamos soluciones enteras. En este capítulo sólo utilizaremos como laboratorio las ecuaciones lineales de dos variables:

$$
ax+by=c,
\qquad x,y\in\mathbb Z.
$$

No intentaremos todavía resolver el problema general. Nuestro objetivo es descubrir qué obstrucciones pueden deducirse directamente de la divisibilidad.

Supongamos que un entero no nulo $d$ divide simultáneamente a $a$ y a $b$:

$$
d\mid a,
\qquad
 d\mid b.
$$

Entonces, para cualesquiera $x,y\in\mathbb Z$, la combinación lineal

$$
ax+by
$$

es divisible por $d$. En efecto, ése es precisamente el resultado de la sección 14.6.

Por tanto, si la ecuación

$$
ax+by=c
$$

tuviera una solución entera, necesariamente tendría que cumplirse

$$
d\mid c
$$

para **todo** divisor común no nulo $d$ de $a$ y $b$.

Esto nos da una condición necesaria:

$$
\boxed{
\text{si }d\mid a,\ d\mid b\text{ y }d\nmid c,
\text{ entonces }ax+by=c\text{ no tiene soluciones enteras.}
}
$$

Por ejemplo, consideremos

$$
4x+6y=7.
$$

Como

$$
2\mid4
$$

y

$$
2\mid6,
$$

el lado izquierdo es divisible por $2$ para cualesquiera $x,y\in\mathbb Z$. Pero

$$
2\nmid7.
$$

Por tanto, la ecuación no puede tener soluciones enteras.

La demostración puede escribirse como contradicción. Si existieran $x,y\in\mathbb Z$ tales que

$$
4x+6y=7,
$$

entonces $2$ dividiría al lado izquierdo y, por igualdad, tendría que dividir a $7$, lo cual es falso.

Es fundamental comprender el alcance lógico de este argumento. Hemos encontrado una **obstrucción**. No hemos demostrado que, cuando todos los divisores comunes de los coeficientes dividen a $c$, siempre exista una solución. Convertir esta condición necesaria en un criterio completo requerirá herramientas de C15.

***
## 14.13. Certificados de existencia y familias concretas {#apm-c14-s13}

Para demostrar que una ecuación diofántica tiene solución basta exhibir una solución concreta.

Consideremos

$$
18x+30y=6.
$$

La pareja

$$
(x,y)=(2,-1)
$$

es un certificado de existencia porque

$$
18(2)+30(-1)=36-30=6.
$$

No hace falta, para demostrar existencia, clasificar todas las soluciones.

Una vez que conocemos una solución, a veces podemos construir otras mediante una transformación que no cambie el lado izquierdo. En este ejemplo,

$$
18\cdot5+30(-3)=90-90=0.
$$

Por tanto, si sumamos

$$
(5,-3)
$$

a una solución, el valor de $18x+30y$ permanece inalterado.

Partiendo de $(2,-1)$ obtenemos, para cualquier $t\in\mathbb Z$,

$$
x=2+5t,
$$

$$
y=-1-3t.
$$

En efecto,

$$
18(2+5t)+30(-1-3t)
=36+90t-30-90t
=6.
$$

Así hemos construido una familia infinita de soluciones:

$$
\boxed{
(x,y)=(2+5t,-1-3t),
\qquad t\in\mathbb Z.
}
$$

Este procedimiento es completamente verificable con las herramientas actuales. Sin embargo, debemos ser cuidadosos con la conclusión.

Hemos demostrado que **todas las parejas de esa forma son soluciones**. No hemos demostrado todavía que **toda solución posible tenga esa forma**.

Ésta es una distinción lógica importante:

- exhibir una solución demuestra existencia;
- exhibir una familia demuestra existencia de muchas soluciones;
- clasificar todas las soluciones exige una demostración adicional.

En C15 obtendremos un procedimiento sistemático para decidir cuándo una ecuación lineal diofántica es soluble y para describir su estructura general. Aquí basta entender cómo la divisibilidad produce obstrucciones y cómo una identidad puede producir certificados positivos.

### Nota pedagógica — Generación y exhaustividad son dos pruebas

Para una familia propuesta $F(t)$, verificar que cada $t\in\mathbb Z$ produce una solución prueba **generación**. Para afirmar que son todas, hay que comenzar con una solución arbitraria y demostrar que existe un entero $t$ que la representa. Son implicaciones en sentidos opuestos. Una lista de comprobaciones, por extensa que sea, sólo atiende a la primera.

**Control resuelto.** Considera $2x+y=1$. La familia $(t,1-2t)$ produce soluciones para todo entero $t$, pues $2t+1-2t=1$. Además es exhaustiva: si $(x,y)$ es una solución entera cualquiera, la ecuación obliga a $y=1-2x$; al tomar $t=x\in\mathbb Z$ recuperamos la pareja. El parámetro es único porque coincide con la primera coordenada.

Ahora compara la familia $(2t,1-4t)$. Todas sus parejas también son soluciones, pero no contiene $(1,-1)$: exigiría $2t=1$, imposible para un entero $t$. Hemos generado una subfamilia infinita, sin haber clasificado todas las soluciones. El salto en el parámetro ha perdido las soluciones cuya primera coordenada es impar.

La familia de $18x+30y=6$ presentada arriba tiene una verificación de generación. Para afirmar exhaustividad habría que estudiar la ecuación que cumplen las diferencias entre una solución arbitraria y $(2,-1)$, y demostrar la forma de esas diferencias; esa conclusión no se añade mediante otra sustitución. La clasificación sistemática queda para C15. En ecuaciones concretas más sencillas, como el control anterior o un problema con una restricción adicional, se puede probar exhaustividad directamente con las herramientas actuales.

***
## 14.14. Identidades algebraicas como máquinas de divisibilidad {#apm-c14-s14}

Una identidad algebraica puede demostrar una divisibilidad si exhibe el factor que necesitamos.

Consideremos la conocida factorización

$$
u^n-v^n
=(u-v)
\left(
\sum_{j=0}^{n-1}u^{n-1-j}v^j\right),
$$

válida para todo entero $n\ge1$. La suma tiene $n$ términos y todos sus exponentes son no negativos. Como en las identidades polinómicas de C13, una potencia de exponente cero representa el producto vacío $1$, incluso al evaluar la base en cero.

Para demostrar la factorización, multiplica la suma por $u-v$. La parte multiplicada por $u$ es $\sum_{j=0}^{n-1}u^{n-j}v^j$; la multiplicada por $v$ se reindexa como $\sum_{j=1}^{n}u^{n-j}v^j$. Los términos con índices $1,\ldots,n-1$ se cancelan y quedan $u^n-v^n$. Para $n=1$, el rango interior es vacío y el testigo es el único término $u^0v^0=1$. Así la prueba no necesita interpretar una lista que contenga exponentes negativos.

Si $u,v\in\mathbb Z$ y $u\ne v$, el segundo factor es un entero. Por tanto,

$$
\boxed{
u-v\mid u^n-v^n.}
$$

La factorización no sólo demuestra la divisibilidad: produce directamente el testigo

$$
\sum_{j=0}^{n-1}u^{n-1-j}v^j.
$$

El requisito $u\ne v$ no es decorativo. Bajo la convención de este tomo, si $u=v$ el supuesto divisor $u-v$ sería $0$, y la expresión $0\mid0$ queda fuera de nuestra relación.

Como caso particular, tomemos

$$
u=N,
\qquad
v=1.
$$

Si $N\ne1$ y $m\ge1$, obtenemos

$$
\boxed{
N-1\mid N^m-1.
}
$$

Por ejemplo,

$$
9-1=8
$$

divide a

$$
9^4-1.
$$

No necesitamos calcular $9^4-1$; la factorización ya contiene el testigo:

$$
9^4-1=(9-1)(9^3+9^2+9+1).
$$

Existe una idea análoga para sumas de potencias impares. Aplica la identidad demostrada a $u$ y $-v$: si $n\ge1$ es impar, entonces $u^n-(-v)^n=u^n+v^n$ y el factor $u-(-v)$ es $u+v$. El testigo entero es $\sum_{j=0}^{n-1}u^{n-1-j}(-v)^j$. Por tanto, si $n$ es impar y positivo,

$$
u^n+v^n
$$

posee el factor $u+v$. Siempre que $u+v\ne0$,

$$
\boxed{
u+v\mid u^n+v^n\quad(n\text{ impar}).}
$$

Lo esencial es aprender a reconocer una factorización como una **máquina de testigos**. El objetivo no es desarrollar todavía teoría formal de polinomios; es aprovechar identidades algebraicas ya conocidas para producir afirmaciones aritméticas.

***
## 14.15. Parámetros, conversos falsos y diagnóstico {#apm-c14-s15}

Los problemas de divisibilidad con parámetros suelen simplificarse cuando transformamos una expresión mediante combinaciones lineales.

Consideremos la condición

$$
n+1\mid n^2+1.
$$

Queremos determinar para qué enteros $n$ puede ocurrir. Primero debemos excluir

$$
n=-1,
$$

porque entonces el supuesto divisor $n+1$ sería $0$.

Ahora observemos que

$$
n^2+1-(n-1)(n+1)=2.
$$

Si

$$
n+1\mid n^2+1,
$$

y, evidentemente,

$$
n+1\mid(n-1)(n+1),
$$

entonces, por resta,

$$
n+1\mid2.
$$

Recíprocamente, si $n+1\mid2$, la identidad

$$
n^2+1=(n-1)(n+1)+2
$$

muestra que $n+1\mid n^2+1$.

Así, el problema se ha reducido a clasificar los divisores enteros no nulos de $2$:

$$
n+1\in\{-2,-1,1,2\}.
$$

Por tanto,

$$
\boxed{
n\in\{-3,-2,0,1\}.
}
$$

Este tipo de reducción es una aplicación directa de las combinaciones lineales: reemplazamos una expresión grande por una constante mucho más pequeña.

### Conversos y generalizaciones falsas

La aritmética está llena de afirmaciones plausibles que son falsas. Conviene entrenar el reflejo de probar casos pequeños antes de aceptar un converso.

#### Falso 1

$$
a\mid bc\Longrightarrow a\mid b.
$$

Contraejemplo:

$$
6\mid(2\cdot3),
$$

pero

$$
6\nmid2.
$$

#### Falso 2

$$
a\mid bc\Longrightarrow a\mid b\ \text{o}\ a\mid c.
$$

El mismo ejemplo sirve:

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2
$$

y

$$
6\nmid3.
$$

Más adelante veremos que, bajo hipótesis adicionales relacionadas con números primos, aparece un resultado de aspecto parecido. Precisamente por eso es importante no anticiparlo sin sus hipótesis.

#### Falso 3

$$
a\mid b
\ \text{y}\
c\mid d
\Longrightarrow
 a+c\mid b+d.
$$

Tomemos

$$
a=2,
\quad b=2,
\quad c=3,
\quad d=6.
$$

Entonces $2\mid2$ y $3\mid6$, pero

$$
5\nmid8.
$$

#### Falso 4

$$
a\mid(b+c)
\Longrightarrow
 a\mid b\ \text{y}\ a\mid c.
$$

Tomemos

$$
a=3,
\quad b=1,
\quad c=2.
$$

Entonces

$$
3\mid(1+2),
$$

pero $3$ no divide ni a $1$ ni a $2$.

Los contraejemplos no son anomalías. Señalan exactamente dónde una propiedad necesita hipótesis adicionales. Registrar esos fallos prepara el terreno para C16, donde estudiaremos qué cambia cuando el divisor es primo.

***
## 14.16. Cierre — protocolo para problemas de divisibilidad {#apm-c14-s16}

La divisibilidad comenzó como una reformulación de una pregunta muy sencilla: ¿cuándo tiene solución entera la ecuación $ax=b$? A lo largo del capítulo vimos que esa noción organiza mucho más que una operación de cociente.

Una afirmación

$$
a\mid b
$$

es una proposición existencial. Afirma que existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Esa lectura permite demostrar propiedades básicas, construir combinaciones lineales, comparar tamaños, estudiar la divisibilidad como relación, interpretar los conjuntos $a\mathbb Z$ y detectar obstrucciones en ecuaciones diofánticas.

Ante un nuevo problema de divisibilidad, el siguiente protocolo resume las decisiones principales:

```text
1. TRADUCIR a | b COMO b = aq CON q ENTERO.
2. BUSCAR O CONSTRUIR EL TESTIGO.
3. SI HAY VARIAS HIPÓTESIS, FORMAR COMBINACIONES LINEALES.
4. CONTROLAR SIGNOS Y CASOS CERO.
5. USAR TRANSITIVIDAD O CANCELACIÓN SÓLO BAJO SUS HIPÓTESIS.
6. PARA ax=b, PREGUNTAR SI a | b.
7. PARA ax+by=c, BUSCAR DIVISORES COMUNES QUE PRODUZCAN OBSTRUCCIONES.
8. SI SE PROPONE UN CONVERSO, PROBAR CASOS PEQUEÑOS ANTES DE CREERLO.
9. SI APARECEN POTENCIAS, BUSCAR UNA FACTORIZACIÓN QUE EXHIBA EL TESTIGO.
10. DISTINGUIR ENTRE EXISTENCIA, IMPOSIBILIDAD Y CLASIFICACIÓN COMPLETA.
```

Hay tres tipos de argumento que conviene reconocer de inmediato.

**Prueba de existencia.** Se exhibe un testigo. Para $a\mid b$, se construye $q$ con $b=aq$; para una ecuación diofántica, se exhibe una solución.

**Prueba de imposibilidad.** Se muestra que una propiedad necesaria no puede cumplirse. Si todo valor de $ax+by$ es divisible por $d$ y $d\nmid c$, entonces $ax+by=c$ es imposible en enteros.

**Clasificación.** Se pretende describir todos los casos posibles o todas las soluciones. Este objetivo es más fuerte que exhibir ejemplos y requiere demostrar exhaustividad.

El capítulo también ha mostrado una tensión que todavía no sabemos resolver de manera sistemática. Si dos enteros tienen varios divisores comunes, podemos usar cualquiera de ellos para producir combinaciones lineales y obstrucciones. Pero surge una pregunta natural:

> **¿Existe un divisor común que concentre toda la información relevante y pueda encontrarse mediante un procedimiento sistemático?**

La respuesta conduce al siguiente capítulo: **máximo común divisor y algoritmo de Euclides**.

***
# Ejercicios

Los ejercicios están organizados para pasar de la lectura directa de la definición a la construcción autónoma de testigos, combinaciones lineales, contraejemplos y certificados de existencia o imposibilidad. En todo el capítulo se mantiene la convención de que en una expresión $a\mid b$ el divisor $a$ es no nulo.

## A. Definición, testigos, múltiplos y divisores


**1.** **Nivel A.** Decide cuáles de las siguientes afirmaciones son verdaderas. Cuando una sea verdadera, exhibe un testigo entero; cuando sea falsa, explica por qué no puede existir:
$$
7\mid 56,\qquad
-6\mid 42,\qquad
8\mid 54,\qquad
9\mid(-72),\qquad
11\mid0.
$$


**2.** **Nivel A.** Reescribe cada afirmación como una ecuación de la forma $b=aq$ con $q\in\mathbb Z$:
$$
5\mid35,\qquad
-4\mid28,\qquad
12\mid(-84).
$$
Identifica el testigo en cada caso.


**3.** **Nivel A.** Lista los múltiplos de $6$ comprendidos entre $-40$ y $40$. Después lista los múltiplos de $-6$ en el mismo intervalo y compara ambos conjuntos.


**4.** **Nivel A.** Determina todos los divisores enteros de $18$. Explica por qué cada divisor positivo aparece acompañado de uno negativo.


**5.** **Nivel B.** Decide si cada frase expresa correctamente una relación de divisibilidad:
a) “$4$ es múltiplo de $20$”;
b) “$5$ es divisor de $20$”;
c) “$21$ es múltiplo de $7$”;
d) “$9$ divide a $3$”.
Corrige las frases falsas.


**6.** **Nivel B.** Para cada entero
$$
n\in\{-3,-2,-1,0,1,2,3\},
$$
determina si $4\mid 12n$. No calcules cocientes decimales: construye directamente el testigo.


**7.** **Nivel B.** Explica, usando la definición, por qué todo entero no nulo divide a $0$. Después explica por qué, bajo la convención de este tomo, una expresión con $0$ como divisor queda fuera de la relación definida.


**8.** **Nivel C.** Sea $n\ne0$. Demuestra que el conjunto de divisores enteros de $n$ es finito usando únicamente el hecho de que, si $d\mid n$, entonces $n=dq$ para algún entero $q$ y que $q\ne0$.

## B. Propiedades básicas de la divisibilidad


**9.** **Nivel B.** Demuestra directamente desde la definición que $a\mid a$ para todo entero no nulo $a$. Identifica el testigo.


**10.** **Nivel B.** Demuestra que si $a\mid b$, entonces $a\mid bc$ para todo $c\in\mathbb Z$. Tu prueba debe construir explícitamente el nuevo testigo.


**11.** **Nivel C.** Demuestra la transitividad: si $a\mid b$ y $b\mid c$, entonces $a\mid c$. Nombra por separado los dos testigos iniciales y el testigo final.


**12.** **Nivel C.** Si $a\mid b$ y $a\mid c$, demuestra
$$
a\mid(b+c)
\qquad\text{y}\qquad
a\mid(b-c).
$$
Explica por qué la clausura de $\mathbb Z$ bajo suma y resta es parte de la prueba.


**13.** **Nivel B.** Sabiendo que
$$
7\mid 84
\qquad\text{y}\qquad
7\mid35,
$$
deduce sin dividir que
$$
7\mid119,\qquad
7\mid49,\qquad
7\mid(-133).
$$
En cada caso indica qué propiedad usaste.


**14.** **Nivel C.** Supón que $a\mid b$. Demuestra que, para cualesquiera $r,s\in\mathbb Z$,
$$
a\mid(rb+sab).
$$
Da el testigo final en términos de un testigo de $a\mid b$.


**15.** **Nivel C.** Si $a\mid b$ y $c\mid d$, demuestra que
$$
ac\mid bd.
$$
Escribe $b=ar$ y $d=cs$ y construye el testigo correspondiente.


**16.** **Nivel C.** Si
$$
3\mid n
\qquad\text{y}\qquad
5\mid m,
$$
demuestra que
$$
15\mid 5n+3m.
$$
No uses factorización prima ni congruencias.


**17.** **Nivel D.** Sea $a\ne0$. Demuestra que si
$$
a\mid b_1,\quad a\mid b_2,\quad\dots,\quad a\mid b_r,
$$
entonces, para cualesquiera $c_1,\dots,c_r\in\mathbb Z$,
$$
a\mid(c_1b_1+\cdots+c_rb_r).
$$
Hazlo construyendo un único testigo.


**18.** **Nivel D.** Analiza el siguiente razonamiento:
> “Si $a\mid b$ y $a\mid c$, entonces $a\mid bc$ porque $a$ divide a cada factor.”

La conclusión es verdadera. Determina si la justificación dada es suficiente y proporciona una prueba correcta desde la definición que use sólo una de las dos hipótesis si es posible.

## C. Signos, cancelación, tamaño y divisibilidad mutua


**19.** **Nivel B.** Demuestra que, para $a\ne0$,
$$
a\mid b
\iff
(-a)\mid b
\iff
a\mid(-b).
$$
Describe cómo cambia el testigo en cada paso.


**20.** **Nivel C.** Demuestra que si $c\ne0$ y
$$
ca\mid cb,
$$
entonces
$$
a\mid b.
$$
Indica exactamente dónde se utiliza la hipótesis $c\ne0$.


**21.** **Nivel C.** Sean $a,b\ne0$. Demuestra que
$$
a\mid b
\Longrightarrow
|a|\le |b|.
$$
Parte de $b=aq$ y justifica por qué $|q|\ge1$.


**22.** **Nivel D.** Sean $a,b\ne0$. Si
$$
a\mid b
\qquad\text{y}\qquad
b\mid a,
$$
demuestra que
$$
a=\pm b.
$$
Haz explícito el uso de las cotas de valor absoluto.


**23.** **Nivel C.** Determina todos los enteros no nulos $d$ tales que
$$
d\mid 15
\qquad\text{y}\qquad
|d|\ge5.
$$
Justifica que tu lista es exhaustiva sin usar factorización prima.


**24.** **Nivel D.** Un estudiante afirma:
> “De $ca\mid cb$ siempre puedo cancelar $c$.”

Explica por qué una prueba formal debe controlar que $c\ne0$ dentro de la convención adoptada. Reformula la regla de cancelación con todas sus hipótesis y demuéstrala.

## D. Combinaciones lineales


**25.** **Nivel B.** Demuestra que si
$$
d\mid a
\qquad\text{y}\qquad
d\mid b,
$$
entonces
$$
d\mid(ra+sb)
$$
para cualesquiera $r,s\in\mathbb Z$.


**26.** **Nivel B.** Sabiendo que
$$
6\mid 48
\qquad\text{y}\qquad
6\mid30,
$$
elige coeficientes enteros $r,s$ para demostrar mediante una combinación lineal que
$$
6\mid18
$$
y que
$$
6\mid6.
$$


**27.** **Nivel C.** Si $d\mid a$ y $d\mid b$, demuestra que para todo $k\in\mathbb Z$,
$$
d\mid(a-kb).
$$
Explica por qué esta forma es útil para eliminar parte de una expresión.


**28.** **Nivel C.** Supón que
$$
d\mid(5n+2)
\qquad\text{y}\qquad
d\mid(3n+1).
$$
Construye una combinación lineal que elimine $n$ y demuestra que $d\mid1$. ¿Qué valores puede tomar entonces $d$?


**29.** **Nivel C.** Si
$$
d\mid(7n+4)
\qquad\text{y}\qquad
d\mid(5n+3),
$$
encuentra una combinación lineal que produzca una constante no nula. Deduce una restricción sobre $d$.


**30.** **Nivel D.** Demuestra que todo divisor común de $14n+9$ y $8n+5$ divide a $2$. Debes exhibir explícitamente la combinación lineal utilizada.


**31.** **Nivel D.** Sea $d$ un entero no nulo que divide a $a$ y a $b$. Demuestra que $d$ divide a
$$
(a+b)^2-(a-b)^2.
$$
Simplifica primero la expresión y después compara dos pruebas posibles.


**32.** **Nivel D.** Si $d\mid a$ y $d\mid b$, demuestra que $d$ divide a cualquier expresión de la forma
$$
r_1a+r_2b+r_3(a-b)+r_4(2a+3b),
$$
con $r_1,r_2,r_3,r_4\in\mathbb Z$. Reduce toda la expresión a una sola combinación lineal de $a$ y $b$.


**33.** **Nivel D.** Supón que un entero no nulo $d$ divide simultáneamente a
$$
4n+1
\qquad\text{y}\qquad
6n+1.
$$
Demuestra que $d\mid1$ y determina todos los valores posibles de $d$.


**34.** **Nivel E.** Sean $u,v\in\mathbb Z$ y $d\ne0$. Supón que
$$
d\mid(2u+3v)
\qquad\text{y}\qquad
d\mid(5u+7v).
$$
Encuentra combinaciones lineales que permitan concluir que $d\mid u$ y $d\mid v$. No invoques matrices ni determinantes: construye las combinaciones directamente.

## E. Relación de divisibilidad y conjuntos $a\mathbb Z$


**35.** **Nivel B.** Sobre $\mathbb Z\setminus\{0\}$, decide si la divisibilidad es reflexiva, simétrica y transitiva. Prueba las propiedades verdaderas y da contraejemplos para las falsas.


**36.** **Nivel C.** Da un ejemplo que muestre que la divisibilidad no es antisimétrica sobre $\mathbb Z\setminus\{0\}$. Explica por qué el problema desaparece al restringir la relación a $\mathbb Z_{>0}$.


**37.** **Nivel C.** Demuestra que la divisibilidad es un orden parcial sobre $\mathbb Z_{>0}$. Debes verificar por separado reflexividad, antisimetría y transitividad.


**38.** **Nivel B.** Escribe explícitamente los elementos de
$$
4\mathbb Z,\qquad 6\mathbb Z,\qquad (-4)\mathbb Z
$$
que se encuentran entre $-25$ y $25$. ¿Qué igualdades o inclusiones sugieren las listas?


**39.** **Nivel C.** Demuestra, para $a,b\ne0$, que
$$
a\mid b
\Longrightarrow
b\mathbb Z\subseteq a\mathbb Z.
$$
Toma un elemento arbitrario de $b\mathbb Z$ y demuestra que pertenece a $a\mathbb Z$.


**40.** **Nivel C.** Demuestra el converso del ejercicio anterior:
$$
b\mathbb Z\subseteq a\mathbb Z
\Longrightarrow
a\mid b.
$$
Indica qué elemento particular de $b\mathbb Z$ conviene elegir.


**41.** **Nivel D.** Para $a,b\ne0$, demuestra
$$
a\mathbb Z=b\mathbb Z
\Longleftrightarrow
a=\pm b.
$$
Tu prueba debe usar la equivalencia entre divisibilidad e inclusión y la divisibilidad mutua.


**42.** **Nivel D.** Ordena por inclusión los conjuntos
$$
2\mathbb Z,\qquad 4\mathbb Z,\qquad 8\mathbb Z.
$$
Después ordena $2,4,8$ por divisibilidad y explica por qué las dos direcciones parecen invertidas.

## F. Ecuaciones $ax=b$


**43.** **Nivel A.** Decide cuáles de las ecuaciones tienen solución entera y resuélvelas cuando sea posible:
$$
6x=48,\qquad
6x=50,\qquad
-7x=35,\qquad
9x=-54.
$$


**44.** **Nivel B.** Demuestra, para $a\ne0$, que
$$
ax=b
$$
tiene solución entera si y sólo si
$$
a\mid b.
$$


**45.** **Nivel B.** Determina todos los enteros $m$ para los cuales la ecuación
$$
5x=20m+15
$$
tiene solución entera. Cuando exista, expresa una solución en función de $m$.


**46.** **Nivel C.** Determina los enteros $n$ para los cuales
$$
4x=6n+2
$$
tiene una solución entera. Resuelve el problema usando sólo la definición de divisibilidad y una clasificación elemental de los enteros pares e impares, sin notación de congruencias.


**47.** **Nivel C.** Sea $a\ne0$. Demuestra que si $ax=b$ tiene una solución entera, entonces esa solución es única. Explica por qué esta afirmación es muy distinta de lo que ocurrirá con ecuaciones lineales en dos variables.


**48.** **Nivel D.** Supón que $a,b,c\in\mathbb Z$, $a\ne0$, y que
$$
a\mid b
\qquad\text{y}\qquad
a\mid c.
$$
Demuestra que las ecuaciones $ax=b$ y $ax=c$ tienen soluciones enteras y usa esas soluciones para construir una solución entera de
$$
ax=b+c.
$$
Relaciona el argumento con el cierre de la divisibilidad bajo suma.

## G. Ecuaciones diofánticas lineales


**49.** **Nivel B.** Decide si cada pareja propuesta es solución de la ecuación indicada:
a) $(x,y)=(2,-1)$ para $18x+30y=6$;
b) $(x,y)=(1,1)$ para $4x+6y=10$;
c) $(x,y)=(-2,3)$ para $5x+7y=11$.


**50.** **Nivel C.** Demuestra que la ecuación
$$
4x+6y=7
$$
no tiene soluciones enteras. Usa el hecho de que $2$ divide a cada término del lado izquierdo, pero no al lado derecho.


**51.** **Nivel C.** Demuestra que
$$
6x+10y=15
$$
no tiene solución entera. Identifica un divisor común de los coeficientes que produce la obstrucción.


**52.** **Nivel C.** Exhibe una solución entera de cada ecuación:
$$
8x+12y=4,
\qquad
15x+21y=6.
$$
Explica por qué una pareja concreta es un certificado suficiente de existencia.


**53.** **Nivel D.** Supón que $d\mid a$ y $d\mid b$. Demuestra que cualquier solución entera de
$$
ax+by=c
$$
obliga a
$$
d\mid c.
$$
Tu prueba debe funcionar para cualquier divisor común $d$, no sólo para un ejemplo numérico.


**54.** **Nivel D.** La ecuación
$$
12x+18y=c
$$
tiene una solución entera para cierto $c$. Demuestra que necesariamente $6\mid c$. Explica por qué esta conclusión es sólo una condición necesaria y no has demostrado aún un criterio completo.


**55.** **Nivel C.** Partiendo de la solución
$$
18(2)+30(-1)=6,
$$
demuestra que para todo $m\in\mathbb Z$ la ecuación
$$
18x+30y=6m
$$
tiene al menos una solución entera. Exhibe una fórmula concreta para una solución.


**56.** **Nivel D.** Si $(x_0,y_0)$ satisface
$$
18x+30y=c,
$$
demuestra que, para todo $t\in\mathbb Z$,
$$
(x_0+5t,\ y_0-3t)
$$
también es solución. Verifica directamente que el lado izquierdo no cambia.


**57.** **Nivel D.** Un estudiante encuentra tres soluciones distintas de
$$
8x+12y=4
$$
y concluye: “éstas son todas las soluciones”. Explica por qué la conclusión no se sigue de los datos. ¿Qué habría que demostrar adicionalmente para justificar una clasificación completa?


**58.** **Nivel E.** Para cada ecuación, da un certificado de existencia o un certificado de imposibilidad usando únicamente divisibilidad elemental:
$$
10x+14y=6,
$$
$$
10x+14y=5,
$$
$$
9x+15y=12.
$$
Cuando afirmes existencia, exhibe una solución concreta; cuando afirmes imposibilidad, identifica un divisor común que no divide al término independiente.

## H. Identidades de divisibilidad y factorización


**59.** **Nivel B.** Factoriza
$$
u^2-v^2
$$
y usa la factorización para demostrar
$$
u-v\mid u^2-v^2
$$
cuando $u-v\ne0$.


**60.** **Nivel C.** Demuestra, para $m\ge1$,
$$
u-v\mid u^m-v^m
$$
si $u-v\ne0$. Exhibe explícitamente el factor que funciona como testigo.


**61.** **Nivel C.** Deduce del ejercicio anterior que, para $n\ne1$ y $m\ge1$,
$$
n-1\mid n^m-1.
$$
Explica por qué la restricción $n\ne1$ aparece bajo la convención del capítulo.


**62.** **Nivel C.** Demuestra que, para $n\ne-1$ y $m\ge1$,
$$
n+1\mid n^{2m}-1.
$$
Usa una diferencia de potencias apropiada, sin notación de congruencias.


**63.** **Nivel D.** Demuestra que, para todo entero $n$ y todo $m\ge1$ para los cuales el divisor indicado sea no nulo,
$$
n^m-1\mid n^{2m}-1.
$$
Identifica el cociente exacto.


**64.** **Nivel D.** Demuestra que, si $a-b\ne0$,
$$
a-b\mid a^3-3a^2b+3ab^2-b^3.
$$
Primero reconoce la expresión y después exhibe el testigo.


**65.** **Nivel D.** Determina todos los enteros $n\ne-1$ tales que
$$
n+1\mid n+7.
$$
Reduce el problema a que $n+1$ divida una constante y clasifica los divisores enteros posibles.


**66.** **Nivel E.** Determina todos los enteros $n\ne2$ tales que
$$
n-2\mid n^2-3n+5.
$$
Resta un múltiplo adecuado de $n-2$ hasta obtener una constante. No uses algoritmo de Euclides ni congruencias.

## I. Diagnóstico y elección de método


**67.** **Nivel C.** Refuta mediante un contraejemplo la afirmación
$$
a\mid bc
\Longrightarrow
a\mid b.
$$
Explica por qué el hecho de que $bc=aq$ no permite, por sí solo, expresar $b$ como múltiplo de $a$.


**68.** **Nivel C.** Refuta mediante un contraejemplo
$$
a\mid bc
\Longrightarrow
a\mid b\ \text{o}\ a\mid c.
$$
Elige números pequeños y verifica todas las divisibilidades involucradas.


**69.** **Nivel C.** Refuta
$$
a\mid b,\quad c\mid d
\Longrightarrow
a+c\mid b+d.
$$
Después explica por qué sumar dos relaciones de divisibilidad con divisores diferentes no produce automáticamente una nueva relación.


**70.** **Nivel C.** Refuta
$$
a\mid(b+c)
\Longrightarrow
a\mid b\ \text{y}\ a\mid c.
$$
Luego formula una hipótesis adicional sencilla que sí permita deducir una de las dos divisibilidades a partir de la otra y de $a\mid(b+c)$.


**71.** **Nivel D.** Para cada problema, elige el método que consideres más natural —definición con testigo, combinación lineal, inclusión de conjuntos de múltiplos o factorización— y justifica tu elección:
a) demostrar $7\mid(35n+14)$;
b) demostrar $a\mid b\iff b\mathbb Z\subseteq a\mathbb Z$;
c) demostrar $u-v\mid u^5-v^5$;
d) decidir qué puede deducirse de un divisor común de $12n+7$ y $8n+5$.


**72.** **Nivel E.** Audita la afirmación:
> “Si $d$ divide a dos expresiones, entonces divide a cualquier cosa obtenida al combinarlas.”

Reformula la frase como un teorema correcto. Especifica qué significa “combinarlas”, qué coeficientes están permitidos y por qué el resultado deja de estar justificado si se introducen operaciones que no producen combinaciones lineales enteras.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra que la relación de divisibilidad define un orden parcial sobre $\mathbb Z_{>0}$: verifica reflexividad, antisimetría y transitividad. Después explica exactamente por qué la antisimetría falla sobre $\mathbb Z\setminus\{0\}$ si $a$ y $-a$ se consideran elementos distintos. Da un contraejemplo mínimo y relaciona el fallo con la conclusión $a=\pm b$ obtenida de la divisibilidad mutua.


**74.** **Nivel F.** Sean $a,b\ne0$. Demuestra
$$
a\mid b
\iff
b\mathbb Z\subseteq a\mathbb Z.
$$
A partir de esta equivalencia, demuestra
$$
a\mathbb Z=b\mathbb Z
\iff
a=\pm b.
$$
Finalmente explica con precisión por qué la dirección de la inclusión de conjuntos de múltiplos es inversa a la dirección intuitiva de “ser múltiplo”.


**75.** **Nivel F.** Demuestra que si $a\mid b$, entonces, para todo $k\in\mathbb Z$,
$$
a\mid(b+ka).
$$
Demuestra también el recíproco en la forma:
$$
a\mid(b+ka)
\Longrightarrow
a\mid b.
$$
Usa esta equivalencia para reducir, sin efectuar divisiones largas, las siguientes preguntas:
a) ¿$37$ divide a $37\cdot 125+74$?;
b) si $d$ divide a $101n+37$ y a $100n+36$, ¿qué entero pequeño debe dividir también?;
c) si $d$ divide a $53n+18$ y a $52n+17$, demuestra que $d\mid35$ y describe la restricción resultante sobre $d$.
En cada apartado exhibe la combinación lineal o el testigo correspondiente.


**76.** **Nivel F.** Para $m\ge1$ y $u-v\ne0$, demuestra
$$
u-v\mid u^m-v^m
$$
mediante una factorización explícita. Deduce, bajo las condiciones que hacen no nulos los divisores,
$$
n-1\mid n^m-1
$$
y
$$
n+1\mid n^{2m}-1.
$$
Tu solución no puede usar congruencias. Compara los dos corolarios e identifica qué sustitución produce cada uno.


**77.** **Nivel F.** Determina todos los enteros $n\ne-1$ tales que
$$
n+1\mid n^2+1.
$$
La prueba debe transformar la condición mediante una combinación lineal hasta obtener
$$
n+1\mid2.
$$
Clasifica después todos los divisores enteros no nulos de $2$, recupera los valores posibles de $n$ y verifica cada candidato en la condición original.


**78.** **Nivel F.** Sean $a_1,\dots,a_m$ enteros no nulos tales que
$$
a_1\mid a_2\mid\cdots\mid a_m.
$$
a) Demuestra que
$$
|a_1|\le|a_2|\le\cdots\le|a_m|.
$$
b) Supón además que $|a_1|=|a_m|$. Demuestra que todos los valores absolutos son iguales y que, para cada $i$,
$$
a_i=\pm a_1.
$$
c) Explica qué parte del argumento usa transitividad y qué parte usa la cota asociada a la divisibilidad.


**79.** **Nivel G.** Un estudiante intenta demostrar
$$
a\mid bc
\Longrightarrow
a\mid b\ \text{o}\ a\mid c
$$
del siguiente modo:
> Como $a\mid bc$, existe $q\in\mathbb Z$ con $bc=aq$. Si $c\ne0$, dividimos por $c$ y obtenemos $b=a(q/c)$. Por tanto $a\mid b$. Si $c=0$, entonces $a\mid c$.

Audita la prueba completa:
1. identifica el paso inválido;
2. explica por qué $q/c$ no tiene por qué ser entero;
3. da un contraejemplo numérico a la afirmación;
4. explica por qué la definición de divisibilidad no permite la cancelación realizada;
5. registra qué tipo de hipótesis adicionales habrá que estudiar más adelante para obtener resultados de esta clase, sin usarlas todavía.


**80.** **Nivel G.** Estudia la ecuación diofántica
$$
18x+30y=c.
$$
Debes realizar cinco tareas:
a) demuestra que si existe una solución entera, entonces necesariamente $6\mid c$;
b) verifica el certificado
$$
18(2)+30(-1)=6;
$$
c) deduce que si $c=6m$, con $m\in\mathbb Z$, entonces existe al menos una solución, y exhibe una;
d) partiendo de una solución $(x_0,y_0)$, demuestra que
$$
(x_0+5t,\ y_0-3t),
\qquad t\in\mathbb Z,
$$
produce infinitas soluciones;
e) explica por qué este ejemplo plantea una nueva pregunta general: dado $ax+by=c$, ¿cómo identificar de manera sistemática el divisor común que contiene la información decisiva y cómo relacionarlo con combinaciones lineales?

No enuncies ni utilices todavía un criterio general basado en resultados del capítulo siguiente.

***
## N. Testigos, dominios y certificados

En cada problema, todas las variables son enteras salvo los cocientes racionales que se examinan expresamente. Se mantiene la convención de divisor no nulo.


**81.** **Nivel D.** Sean $n\ge0$ y $0\le k\le n$ enteros. Construye un testigo entero de $k!(n-k)!\mid n!$ usando C13. Determina además cuándo se cumple la divisibilidad inversa $n!\mid k!(n-k)!$. Justifica la clasificación sin factorización prima y trata $n=0$.


**82.** **Nivel C.** Para todo $n\in\mathbb Z$, construye un testigo explícito de $2\mid n(n+1)$. Escríbelo mediante $n=2t$ y $n=2t+1$, y explica por qué el argumento incluye enteros negativos. Un estudiante propone usar siempre $q=n^2/2$; decide si ese candidato cumple la igualdad requerida.


**83.** **Nivel D.** Determina todos los enteros $n\ne3$ para los que $n-3\mid2n+5$. Exhibe el testigo en cada caso y demuestra que no hay otros. Evita cocientes decimales y el algoritmo de Euclides.


**84.** **Nivel D.** Supón $a,c\ne0$, $a\mid b$ y $c\mid b$, y escribe $b=aq$ con $q\in\mathbb Z$. Se afirma que $a\mid b/c$ porque «se cancela $c$». Construye contraejemplos para cada entero $m\ge2$ tomando $a=c=m$ y $b=m(m+1)$. Después demuestra la reparación exacta: $a\mid b/c$ si y sólo si $c\mid q$.


**85.** **Nivel D.** Sean $a\ne0$, $u=as$ y $v=at$, con $s,t\in\mathbb Z$, y supón que $h=(u+v)/2$ es entero. ¿Debe cumplirse $a\mid h$? Construye una familia de contraejemplos con $a=2r$, $r\ge1$, y demuestra que la condición exacta es que $s+t$ sea par.


**86.** **Nivel D.** Sean $d\ne0$ y $a,b\in\mathbb Z$ tales que $a+b=du$ y $a-b=dv$, con $u,v\in\mathbb Z$. Un argumento concluye $d\mid a$ y $d\mid b$ al sumar, restar y dividir por dos. Refútalo con una familia de ejemplos y demuestra que ambas conclusiones son válidas exactamente cuando $u$ y $v$ tienen la misma paridad.


**87.** **Nivel C.** Para $a,m\in\mathbb Z\setminus\{0\}$, estudia por inclusión los conjuntos $a\mathbb Z$, $(am)\mathbb Z$ y $(am^2)\mathbb Z$. Determina cuándo las dos inclusiones son estrictas y cuándo hay igualdad. En los casos estrictos exhibe un elemento que falte en cada conjunto menor; incluye $m$ negativo.


**88.** **Nivel E.** Sean $a,b\ne0$. Demuestra que $a\mathbb Z\cup b\mathbb Z$ puede ser el conjunto de múltiplos de un entero no nulo exactamente cuando $a\mid b$ o $b\mid a$. Determina el conjunto unión en esos casos. Para probar necesidad, estudia el elemento $a+b$ sin introducir MCD, MCM ni teoría de ideales.


**89.** **Nivel D.** Sean $a\ne0$ y $b\in\mathbb Z$. Define $L=\{b+ak:k\in\mathbb Z\}$. Demuestra que si $a\mid b$, entonces $L=a\mathbb Z$, y si $a\nmid b$, entonces $L\cap a\mathbb Z=\varnothing$. Explica por qué bastaría un elemento en la intersección para decidir la divisibilidad. No uses clases de congruencia.


**90.** **Nivel D.** Verifica el certificado $35(-1)+22(2)=9$. Para $m\in\mathbb Z$, fabrica a partir de él una familia infinita de soluciones de $35x+22y=9m$. Después impón la restricción $x+y=m$ y determina todas las parejas que cumplen ambas ecuaciones. Distingue qué parte prueba generación y qué parte prueba exhaustividad.


**91.** **Nivel D.** Considera $26x+39y=c$ con $x,y\in\mathbb Z$. Usando únicamente el divisor común trece y el certificado $39-26=13$, demuestra que hay solución exactamente cuando $13\mid c$ y exhibe una para cada $c=13m$. Después decide si existe una solución con $x,y\ge0$ para $c=13,26,39$, justificando los casos imposibles.


**92.** **Nivel E.** Sean $a\ne0$ y $b\in\mathbb Z$. Si $a\mid14b$ y $a\mid9b$, ¿qué puedes concluir sobre $b$? Construye un testigo a partir de los dos testigos iniciales. Repite la pregunta sustituyendo $9b$ por $10b$: obtén una conclusión válida y decide si todavía se puede afirmar $a\mid b$. No uses propiedades de primos ni un criterio general de MCD.

***
# Soluciones razonadas

## A. Definición, testigos, múltiplos y divisores


### 1

Analizamos cada caso directamente desde la definición.

- $7\mid56$ es verdadera porque
  $$
  56=7\cdot 8,
  $$
  y $8\in\mathbb Z$ es un testigo.
- $-6\mid42$ es verdadera porque
  $$
  42=(-6)(-7),
  $$
  de modo que el testigo es $-7$.
- $8\mid54$ es falsa. Si fuese verdadera existiría $q\in\mathbb Z$ con $54=8q$. Pero $q=54/8=27/4$ no es entero.
- $9\mid(-72)$ es verdadera porque
  $$
  -72=9(-8).
  $$
- $11\mid0$ es verdadera porque
  $$
  0=11\cdot0.
  $$

El último caso recuerda que todo entero no nulo divide a $0$ bajo la convención del capítulo.


### 2

Las ecuaciones que exhiben los testigos son

$$
35=5\cdot7,
$$

$$
28=(-4)(-7),
$$

y

$$
-84=12(-7).
$$

Por tanto, los testigos son respectivamente $7$, $-7$ y $-7$.


### 3

Los múltiplos de $6$ entre $-40$ y $40$ son

$$
-36,-30,-24,-18,-12,-6,0,6,12,18,24,30,36.
$$

Los múltiplos de $-6$ son exactamente los mismos, porque

$$
(-6)k=6(-k)
$$

para todo $k\in\mathbb Z$. Por tanto,

$$
6\mathbb Z=(-6)\mathbb Z.
$$

Cambiar el signo del generador no cambia su conjunto de múltiplos.


### 4

Los divisores positivos de $18$ son

$$
1,2,3,6,9,18.
$$

Por tanto, todos los divisores enteros son

$$
\boxed{\pm1,\ \pm2,\ \pm3,\ \pm6,\ \pm9,\ \pm18}.
$$

Si $d\mid18$, entonces $18=dq$ para algún $q\in\mathbb Z$. También

$$
18=(-d)(-q),
$$

de modo que $-d\mid18$. Por eso cada divisor positivo aparece acompañado de su opuesto.


### 5

**a)** “$4$ es múltiplo de $20$” es falsa, porque exigiría $20\mid4$. La corrección natural es: **$20$ es múltiplo de $4$**, ya que $20=4\cdot5$.

**b)** “$5$ es divisor de $20$” es verdadera porque $20=5\cdot4$.

**c)** “$21$ es múltiplo de $7$” es verdadera porque $21=7\cdot3$.

**d)** “$9$ divide a $3$” es falsa. La relación correcta es $3\mid9$, pues $9=3\cdot3$.

La distinción esencial es que “$a$ es divisor de $b$” significa $a\mid b$, mientras que “$b$ es múltiplo de $a$” expresa exactamente la misma relación con el lenguaje invertido.


### 6

Para cualquier $n\in\mathbb Z$,

$$
12n=4(3n).
$$

Como $3n\in\mathbb Z$, se tiene

$$
4\mid12n
$$

para todos los valores indicados, incluido $n=0$.

Los testigos son $3n$. Para

$$
n=-3,-2,-1,0,1,2,3,
$$

obtenemos respectivamente

$$
-9,-6,-3,0,3,6,9.
$$


### 7

Sea $a\in\mathbb Z$ con $a\ne0$. Entonces

$$
0=a\cdot0,
$$

y el testigo $0\in\mathbb Z$ demuestra

$$
a\mid0.
$$

En cambio, la relación de divisibilidad adoptada en este tomo se define sólo cuando el divisor es no nulo. Por ello una expresión como

$$
0\mid b
$$

no se evalúa aquí como verdadera o falsa dentro de la relación: queda fuera de su dominio de definición. Esta convención será mantenida de forma uniforme en C14–C17.


### 8

Sea $n\ne0$ y sea $d$ un divisor de $n$. Entonces existe $q\in\mathbb Z$ tal que

$$
n=dq.
$$

Como $n\ne0$, necesariamente $d\ne0$ y $q\ne0$. En particular,

$$
|q|\ge1.
$$

Tomando valores absolutos,

$$
|n|=|d||q|\ge|d|.
$$

Por tanto,

$$
|d|\le|n|.
$$

Todo divisor entero de $n$ debe pertenecer al conjunto finito

$$
\{-|n|,-|n|+1,\ldots,-1,1,\ldots,|n|-1,|n|\}.
$$

Luego el conjunto de divisores enteros de $n$ es finito.

## B. Propiedades básicas de la divisibilidad


### 9

Sea $a\ne0$. Tenemos

$$
a=a\cdot1.
$$

Como $1\in\mathbb Z$, la definición da

$$
\boxed{a\mid a}.
$$

El testigo es $1$.


### 10

Supongamos $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Para cualquier $c\in\mathbb Z$,

$$
bc=(aq)c=a(qc).
$$

Como $qc\in\mathbb Z$, concluimos

$$
\boxed{a\mid bc}.
$$

El nuevo testigo es $qc$.


### 11

De $a\mid b$ existe $r\in\mathbb Z$ con

$$
b=ar.
$$

De $b\mid c$ existe $s\in\mathbb Z$ con

$$
c=bs.
$$

Sustituyendo la primera igualdad en la segunda,

$$
c=(ar)s=a(rs).
$$

Como $rs\in\mathbb Z$, obtenemos

$$
\boxed{a\mid c}.
$$

Los testigos iniciales son $r$ y $s$; el testigo final es $rs$.


### 12

Sean

$$
b=ar,
\qquad
c=as
$$

con $r,s\in\mathbb Z$. Entonces

$$
b+c=a(r+s)
$$

y

$$
b-c=a(r-s).
$$

Como $\mathbb Z$ es cerrado bajo suma y resta,

$$
r+s\in\mathbb Z,
\qquad
r-s\in\mathbb Z.
$$

Por definición,

$$
\boxed{a\mid(b+c)}
\qquad\text{y}\qquad
\boxed{a\mid(b-c)}.
$$

La clausura de los enteros es lo que garantiza que los nuevos cocientes siguen siendo testigos válidos.


### 13

Como $7\mid84$ y $7\mid35$:

- por suma,
  $$
  7\mid(84+35)=119;
  $$
- por resta,
  $$
  7\mid(84-35)=49;
  $$
- para $-133$, observamos
  $$
  -133=-(84+49).
  $$
  Ya sabemos que $7\mid84$ y $7\mid49$, luego $7\mid133$, y cambiar el signo del múltiplo conserva la divisibilidad. Por tanto,
  $$
  7\mid(-133).
  $$

También puede verse directamente que $-133=7(-19)$.


### 14

Supongamos que $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Para $r,s\in\mathbb Z$,

$$
rb+sab
=r(aq)+sa(aq)
=a(rq+saq).
$$

Como

$$
rq+saq=q(r+sa)\in\mathbb Z,
$$

se concluye

$$
\boxed{a\mid(rb+sab)}.
$$

Un testigo final es

$$
q(r+sa).
$$


### 15

Escribamos

$$
b=ar,
\qquad
d=cs
$$

con $r,s\in\mathbb Z$. Entonces

$$
bd=(ar)(cs)=ac(rs).
$$

Como $rs\in\mathbb Z$,

$$
\boxed{ac\mid bd}.
$$

El testigo es $rs$.


### 16

De $3\mid n$ existe $r\in\mathbb Z$ con

$$
n=3r.
$$

De $5\mid m$ existe $s\in\mathbb Z$ con

$$
m=5s.
$$

Entonces

$$
5n+3m
=5(3r)+3(5s)
=15(r+s).
$$

Como $r+s\in\mathbb Z$,

$$
\boxed{15\mid(5n+3m)}.
$$

No se usó ninguna propiedad de números primos; sólo se construyó un testigo entero.


### 17

Para cada $i=1,\ldots,r$, la hipótesis $a\mid b_i$ permite escribir

$$
b_i=aq_i
$$

con $q_i\in\mathbb Z$. Entonces

$$
\begin{aligned}
c_1b_1+\cdots+c_rb_r
&=c_1(aq_1)+\cdots+c_r(aq_r)\\
&=a(c_1q_1+\cdots+c_rq_r).
\end{aligned}
$$

El número

$$
Q=c_1q_1+\cdots+c_rq_r
$$

es entero porque es una suma finita de productos de enteros. Por tanto,

$$
\boxed{a\mid(c_1b_1+\cdots+c_rb_r)}.
$$

El único testigo final es $Q$.


### 18

La conclusión es verdadera, pero la frase “porque $a$ divide a cada factor” no es una justificación precisa y además usa más hipótesis de las necesarias.

Basta suponer $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Multiplicando por $c$,

$$
bc=(aq)c=a(qc).
$$

Como $qc\in\mathbb Z$,

$$
a\mid bc.
$$

La hipótesis $a\mid c$ es redundante para esta conclusión. La propiedad correcta es: **si $a\mid b$, entonces $a\mid bc$ para todo entero $c$**.

## C. Signos, cancelación, tamaño y divisibilidad mutua


### 19

Supongamos $a\mid b$. Entonces

$$
b=aq
$$

para algún $q\in\mathbb Z$. Como

$$
b=(-a)(-q),
$$

obtenemos $(-a)\mid b$. Y como

$$
-b=a(-q),
$$

obtenemos $a\mid(-b)$.

Los mismos argumentos pueden recorrerse en sentido inverso. Por tanto,

$$
\boxed{a\mid b\iff(-a)\mid b\iff a\mid(-b)}.
$$

Cambiar el signo del divisor o del múltiplo cambia el signo del testigo.


### 20

Supongamos $c\ne0$ y

$$
ca\mid cb.
$$

Entonces existe $q\in\mathbb Z$ tal que

$$
cb=(ca)q=c(aq).
$$

Como $c\ne0$, la ley de cancelación en $\mathbb Z$ permite deducir

$$
b=aq.
$$

Por definición,

$$
\boxed{a\mid b}.
$$

La hipótesis $c\ne0$ se usa exactamente al cancelar $c$ en la igualdad. Además, bajo la convención del capítulo, si $c=0$ la expresión $ca\mid cb$ tendría divisor $0$ y ni siquiera pertenecería a la relación definida.


### 21

Sea $a\mid b$ con $a,b\ne0$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Como $b\ne0$, el producto $aq$ es no nulo y, en particular, $q\ne0$. Por tanto,

$$
|q|\ge1.
$$

Tomando valores absolutos,

$$
|b|=|a||q|\ge|a|.
$$

Así,

$$
\boxed{|a|\le|b|}.
$$


### 22

De $a\mid b$ y $b\ne0$, por el ejercicio anterior,

$$
|a|\le|b|.
$$

De $b\mid a$ y $a\ne0$,

$$
|b|\le|a|.
$$

Luego

$$
|a|=|b|.
$$

Dos enteros no nulos con el mismo valor absoluto son iguales o opuestos. Por tanto,

$$
\boxed{a=\pm b}.
$$

El signo no puede eliminarse en general: por ejemplo, $2\mid(-2)$ y $-2\mid2$, pero $2\ne-2$.


### 23

Si $d\mid15$, entonces, por la cota de divisibilidad,

$$
|d|\le15.
$$

Además se exige $|d|\ge5$. Basta entonces probar los enteros con valor absoluto entre $5$ y $15$.

Los divisores positivos de $15$ en ese rango son $5$ y $15$, porque

$$
15=5\cdot3=15\cdot1.
$$

Ninguno de $6,7,8,9,10,11,12,13,14$ divide a $15$: el cociente correspondiente no es entero. Por simetría de signos, también dividen $-5$ y $-15$.

Así,

$$
\boxed{d\in\{-15,-5,5,15\}}.
$$

La exhaustividad proviene de la cota $|d|\le15$, no de una factorización prima.


### 24

La regla correcta es:

> Si $a,b,c\in\mathbb Z$, $a\ne0$, $c\ne0$ y $ca\mid cb$, entonces $a\mid b$.

La hipótesis $c\ne0$ es indispensable para aplicar cancelación a una igualdad de enteros. En efecto, de

$$
ca\mid cb
$$

obtenemos un $q\in\mathbb Z$ tal que

$$
cb=caq.
$$

Como $c\ne0$,

$$
b=aq,
$$

y así $a\mid b$.

Si $c=0$, además, el supuesto divisor $ca$ es $0$, y la expresión queda fuera de la relación de divisibilidad definida en este capítulo. Por eso no es correcto afirmar que se puede “cancelar siempre” sin revisar las hipótesis.

## D. Combinaciones lineales


### 25

Sean

$$
a=du,
\qquad
b=dv
$$

con $u,v\in\mathbb Z$. Para cualesquiera $r,s\in\mathbb Z$,

$$
ra+sb=rdu+sdv=d(ru+sv).
$$

Como $ru+sv\in\mathbb Z$,

$$
\boxed{d\mid(ra+sb)}.
$$

El testigo final es $ru+sv$.


### 26

Para obtener $18$ podemos elegir

$$
18=48-30.
$$

Así, con $r=1$ y $s=-1$,

$$
6\mid(48-30)=18.
$$

Para obtener $6$, por ejemplo,

$$
6=2\cdot30-48.
$$

Con $r=-1$ y $s=2$,

$$
6\mid(-48+2\cdot30)=6.
$$

En ambos casos la conclusión proviene del cierre de la divisibilidad bajo combinaciones lineales enteras.


### 27

Si $d\mid a$ y $d\mid b$, entonces para $k\in\mathbb Z$ la expresión

$$
a-kb
$$

es la combinación lineal

$$
1\cdot a+(-k)b.
$$

Por el teorema de combinaciones lineales,

$$
\boxed{d\mid(a-kb)}.
$$

Esta forma es útil porque puede escogerse $k$ para cancelar términos dependientes de un parámetro y reducir una pregunta de divisibilidad a otra mucho más simple.


### 28

Sea

$$
A=5n+2,
\qquad
B=3n+1.
$$

Como $d\mid A$ y $d\mid B$, también divide cualquier combinación lineal. Elegimos coeficientes que eliminen $n$:

$$
3A-5B
=3(5n+2)-5(3n+1)
=15n+6-15n-5
=1.
$$

Por tanto,

$$
d\mid1.
$$

Los únicos divisores enteros no nulos de $1$ son $1$ y $-1$. Luego

$$
\boxed{d=\pm1}.
$$


### 29

Tomemos

$$
A=7n+4,
\qquad
B=5n+3.
$$

Eliminamos $n$ mediante

$$
5A-7B
=5(7n+4)-7(5n+3)
=35n+20-35n-21
=-1.
$$

Así,

$$
d\mid(-1),
$$

y por tanto

$$
\boxed{d=\pm1}.
$$

La restricción es máxima: ningún otro entero no nulo puede dividir simultáneamente a las dos expresiones.


### 30

Sea $d$ un divisor común de

$$
14n+9
$$

y

$$
8n+5.
$$

Una combinación que elimina $n$ es

$$
4(14n+9)-7(8n+5)
=56n+36-56n-35
=1.
$$

Luego $d\mid1$. En particular, multiplicando por $2$,

$$
\boxed{d\mid2}.
$$

De hecho, hemos obtenido la conclusión más fuerte $d=\pm1$.


### 31

Primero simplificamos:

$$
(a+b)^2-(a-b)^2
=a^2+2ab+b^2-(a^2-2ab+b^2)
=4ab.
$$

Como $d\mid a$, existe $q\in\mathbb Z$ con $a=dq$. Entonces

$$
4ab=4(dq)b=d(4qb),
$$

de modo que

$$
\boxed{d\mid[(a+b)^2-(a-b)^2]}.
$$

Esta prueba usa sólo $d\mid a$.

Otra vía usa ambas hipótesis: de $d\mid a$ y $d\mid b$ se deduce $d\mid(a+b)$ y $d\mid(a-b)$; por compatibilidad con productos, $d$ divide sus cuadrados, y por resta divide la diferencia de cuadrados. La primera prueba es más corta; la segunda muestra cómo se encadenan propiedades de divisibilidad.


### 32

Agrupamos coeficientes de $a$ y $b$:

$$
\begin{aligned}
&r_1a+r_2b+r_3(a-b)+r_4(2a+3b)\\
&=(r_1+r_3+2r_4)a+(r_2-r_3+3r_4)b.
\end{aligned}
$$

Los dos nuevos coeficientes son enteros. Como $d\mid a$ y $d\mid b$, el teorema de combinaciones lineales implica

$$
\boxed{d\mid r_1a+r_2b+r_3(a-b)+r_4(2a+3b)}.
$$


### 33

Sea

$$
A=4n+1,
\qquad
B=6n+1.
$$

Como $d$ divide a ambos, divide también

$$
3A-2B
=3(4n+1)-2(6n+1)
=12n+3-12n-2
=1.
$$

Así,

$$
d\mid1,
$$

y los únicos valores posibles son

$$
\boxed{d=\pm1}.
$$


### 34

Definamos

$$
A=2u+3v,
\qquad
B=5u+7v.
$$

Por hipótesis, $d\mid A$ y $d\mid B$.

Para aislar $u$:

$$
7A-3B
=7(2u+3v)-3(5u+7v)
=14u+21v-15u-21v
=-u.
$$

Así, $d\mid(-u)$ y por cambio de signo

$$
\boxed{d\mid u}.
$$

Para aislar $v$:

$$
5A-2B
=5(2u+3v)-2(5u+7v)
=10u+15v-10u-14v
=v.
$$

Por tanto,

$$
\boxed{d\mid v}.
$$

No fue necesario invocar determinantes: las dos conclusiones surgieron de escoger directamente combinaciones lineales que cancelan una variable.

## E. Relación de divisibilidad y conjuntos $a\mathbb Z$


### 35

Sobre $\mathbb Z\setminus\{0\}$:

- **Reflexiva:** sí. Para todo $a\ne0$,
  $$
  a=a\cdot1,
  $$
  luego $a\mid a$.
- **Simétrica:** no. Por ejemplo,
  $$
  2\mid6,
  $$
  pero $6\nmid2$.
- **Transitiva:** sí. Si $b=ar$ y $c=bs$, entonces
  $$
  c=a(rs),
  $$
  y por tanto $a\mid c$.

Así, la divisibilidad es reflexiva y transitiva, pero no simétrica.


### 36

Tomemos $a=2$ y $b=-2$. Entonces

$$
2\mid(-2)
$$

y

$$
-2\mid2,
$$

pero $2\ne-2$. Por tanto, la divisibilidad no es antisimétrica sobre $\mathbb Z\setminus\{0\}$.

Si restringimos a $\mathbb Z_{>0}$ y $a\mid b$, $b\mid a$, la divisibilidad mutua da

$$
a=\pm b.
$$

Como $a,b>0$, la opción negativa es imposible, de modo que $a=b$. Así se recupera la antisimetría.


### 37

Sobre $\mathbb Z_{>0}$ verificamos las tres propiedades de un orden parcial.

**Reflexividad.** Para todo $a>0$,

$$
a=a\cdot1,
$$

luego $a\mid a$.

**Antisimetría.** Si $a\mid b$ y $b\mid a$, entonces $a=\pm b$. Como ambos son positivos,

$$
a=b.
$$

**Transitividad.** Si $a\mid b$ y $b\mid c$, existen $r,s\in\mathbb Z$ con $b=ar$ y $c=bs$. Entonces

$$
c=a(rs),
$$

y por tanto $a\mid c$.

En consecuencia,

$$
\boxed{\mid\ \text{ es un orden parcial sobre }\mathbb Z_{>0}}.
$$


### 38

Entre $-25$ y $25$:

$$
4\mathbb Z:
-24,-20,-16,-12,-8,-4,0,4,8,12,16,20,24;
$$

$$
6\mathbb Z:
-24,-18,-12,-6,0,6,12,18,24;
$$

y

$$
(-4)\mathbb Z:
-24,-20,-16,-12,-8,-4,0,4,8,12,16,20,24.
$$

Las listas sugieren correctamente que

$$
\boxed{4\mathbb Z=(-4)\mathbb Z}.
$$

En cambio, no hay inclusión entre $4\mathbb Z$ y $6\mathbb Z$: por ejemplo, $4\in4\mathbb Z$ pero $4\notin6\mathbb Z$, mientras que $6\in6\mathbb Z$ pero $6\notin4\mathbb Z$.


### 39

Supongamos $a\mid b$. Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Sea $x\in b\mathbb Z$. Por definición, existe $t\in\mathbb Z$ con

$$
x=bt.
$$

Sustituyendo,

$$
x=(aq)t=a(qt).
$$

Como $qt\in\mathbb Z$, se tiene $x\in a\mathbb Z$. Como $x$ fue arbitrario,

$$
\boxed{b\mathbb Z\subseteq a\mathbb Z}.
$$


### 40

Supongamos

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

El elemento clave es $b$ mismo. Como

$$
b=b\cdot1,
$$

se tiene $b\in b\mathbb Z$. Por la inclusión,

$$
b\in a\mathbb Z.
$$

Entonces existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Por definición,

$$
\boxed{a\mid b}.
$$


### 41

Supongamos primero

$$
a\mathbb Z=b\mathbb Z.
$$

Entonces

$$
a\mathbb Z\subseteq b\mathbb Z
\qquad\text{y}\qquad
b\mathbb Z\subseteq a\mathbb Z.
$$

Por la equivalencia entre divisibilidad e inclusión,

$$
b\mid a
\qquad\text{y}\qquad
a\mid b.
$$

La divisibilidad mutua implica

$$
a=\pm b.
$$

Recíprocamente, si $a=b$, es inmediato que $a\mathbb Z=b\mathbb Z$. Si $a=-b$, entonces todo múltiplo $ak$ puede escribirse como

$$
ak=(-b)k=b(-k),
$$

y viceversa. Por tanto los conjuntos coinciden. Concluimos

$$
\boxed{a\mathbb Z=b\mathbb Z\iff a=\pm b}.
$$


### 42

Como todo múltiplo de $8$ es múltiplo de $4$, y todo múltiplo de $4$ es múltiplo de $2$,

$$
\boxed{8\mathbb Z\subseteq4\mathbb Z\subseteq2\mathbb Z}.
$$

En cambio, por divisibilidad,

$$
\boxed{2\mid4\mid8}.
$$

La dirección se invierte porque si $a\mid b$, entonces $b$ es un múltiplo de $a$, de modo que **todo múltiplo de $b$** es automáticamente un múltiplo de $a$. Así,

$$
a\mid b\Longrightarrow b\mathbb Z\subseteq a\mathbb Z.
$$

## F. Ecuaciones $ax=b$


### 43

- $6x=48$: como $48=6\cdot8$, hay solución entera y
  $$
  x=8.
  $$
- $6x=50$: $6\nmid50$, de modo que no hay solución entera.
- $-7x=35$: como $35=(-7)(-5)$,
  $$
  x=-5.
  $$
- $9x=-54$: como $-54=9(-6)$,
  $$
  x=-6.
  $$


### 44

Sea $a\ne0$.

Si $ax=b$ tiene una solución entera $x_0$, entonces

$$
b=ax_0
$$

con $x_0\in\mathbb Z$. Por definición,

$$
a\mid b.
$$

Recíprocamente, si $a\mid b$, existe $q\in\mathbb Z$ tal que

$$
b=aq.
$$

Tomando $x=q$, obtenemos una solución entera de $ax=b$.

Por tanto,

$$
\boxed{ax=b\text{ tiene solución entera }\iff a\mid b}.
$$


### 45

Tenemos

$$
20m+15=5(4m+3).
$$

Como $4m+3\in\mathbb Z$ para todo $m\in\mathbb Z$, se cumple

$$
5\mid(20m+15)
$$

para **todo** entero $m$. Por tanto la ecuación tiene solución entera para cada $m\in\mathbb Z$, y una solución es

$$
\boxed{x=4m+3}.
$$


### 46

La ecuación

$$
4x=6n+2
$$

tiene solución entera exactamente cuando

$$
4\mid(6n+2).
$$

Factorizamos $2$:

$$
6n+2=2(3n+1).
$$

Por tanto necesitamos que $3n+1$ sea par.

Si $n$ es par, escribimos $n=2k$. Entonces

$$
3n+1=6k+1,
$$

que es impar; no hay solución.

Si $n$ es impar, escribimos $n=2k+1$. Entonces

$$
3n+1=6k+4=2(3k+2),
$$

que es par. En ese caso

$$
6n+2=4(3k+2),
$$

y existe solución.

Así, la condición exacta es

$$
\boxed{n\text{ impar}}.
$$

Cuando $n$ es impar,

$$
\boxed{x=\frac{3n+1}{2}}.
$$


### 47

Supongamos que $x_1$ y $x_2$ son dos soluciones enteras de

$$
ax=b,
$$

con $a\ne0$. Entonces

$$
ax_1=b=ax_2.
$$

Restando,

$$
a(x_1-x_2)=0.
$$

Como $a\ne0$, podemos escribir

$$
a(x_1-x_2)=a\cdot0
$$

y cancelar el factor no nulo $a$. Así,

$$
x_1-x_2=0,
$$

luego

$$
\boxed{x_1=x_2}.
$$

Por tanto, si una ecuación $ax=b$ tiene solución entera, ésta es única. Esto contrasta con ecuaciones lineales en dos variables, donde una misma ecuación puede admitir infinitas parejas enteras; en C14 ya hemos visto ejemplos construidos mediante transformaciones que preservan el lado izquierdo.


### 48

De $a\mid b$ existe $x_1\in\mathbb Z$ tal que

$$
ax_1=b.
$$

De $a\mid c$ existe $x_2\in\mathbb Z$ tal que

$$
ax_2=c.
$$

Sumando las igualdades,

$$
a(x_1+x_2)=b+c.
$$

Como $x_1+x_2\in\mathbb Z$, una solución entera de

$$
ax=b+c
$$

es

$$
\boxed{x=x_1+x_2}.
$$

El argumento es exactamente la traducción, en lenguaje de ecuaciones, de la propiedad

$$
a\mid b,
\quad a\mid c
\Longrightarrow
 a\mid(b+c).
$$

## G. Ecuaciones diofánticas lineales


### 49

**a)**

$$
18(2)+30(-1)=36-30=6,
$$

por tanto $(2,-1)$ sí es solución.

**b)**

$$
4(1)+6(1)=10,
$$

por tanto $(1,1)$ sí es solución.

**c)**

$$
5(-2)+7(3)=-10+21=11,
$$

por tanto $(-2,3)$ sí es solución.

Las tres parejas propuestas satisfacen exactamente sus respectivas ecuaciones.


### 50

Para cualesquiera $x,y\in\mathbb Z$,

$$
4x+6y=2(2x+3y).
$$

Así,

$$
2\mid(4x+6y).
$$

Si existiera una solución de

$$
4x+6y=7,
$$

entonces tendría que cumplirse $2\mid7$, lo cual es falso. Por tanto,

$$
\boxed{4x+6y=7\text{ no tiene soluciones enteras}}.
$$


### 51

El entero $2$ divide a ambos coeficientes:

$$
2\mid6,
\qquad
2\mid10.
$$

Por tanto, para todos $x,y\in\mathbb Z$,

$$
2\mid(6x+10y).
$$

Pero

$$
2\nmid15.
$$

Luego la igualdad

$$
6x+10y=15
$$

es imposible en enteros. Así,

$$
\boxed{\text{no hay solución entera}}.
$$


### 52

Para

$$
8x+12y=4,
$$

podemos tomar

$$
(x,y)=(2,-1),
$$

porque

$$
8(2)+12(-1)=16-12=4.
$$

Para

$$
15x+21y=6,
$$

podemos tomar

$$
(x,y)=(-1,1),
$$

porque

$$
15(-1)+21(1)=6.
$$

Una sola pareja que satisface la ecuación basta para demostrar existencia. No es necesario, para ese objetivo, describir todas las soluciones.


### 53

Supongamos que $(x,y)\in\mathbb Z^2$ satisface

$$
ax+by=c.
$$

Como $d\mid a$ y $d\mid b$, existen $r,s\in\mathbb Z$ tales que

$$
a=dr,
\qquad
b=ds.
$$

Entonces

$$
c=ax+by
=drx+dsy
=d(rx+sy).
$$

Como $rx+sy\in\mathbb Z$,

$$
\boxed{d\mid c}.
$$

El argumento funciona para cualquier divisor común no nulo $d$ de $a$ y $b$.


### 54

Como

$$
6\mid12
\qquad\text{y}\qquad
6\mid18,
$$

cualquier combinación

$$
12x+18y
$$

con $x,y\in\mathbb Z$ es divisible por $6$. Si existe una solución de

$$
12x+18y=c,
$$

entonces necesariamente

$$
\boxed{6\mid c}.
$$

Esto es sólo una **condición necesaria**: hemos demostrado

$$
\text{solución}\Longrightarrow6\mid c,
$$

pero no el converso. Para tener un criterio completo habría que demostrar además que cada $c$ que cumpla la condición produce una solución, algo que no se sigue de este argumento y que se estudiará sistemáticamente en C15.


### 55

Partimos de

$$
18(2)+30(-1)=6.
$$

Multiplicamos toda la igualdad por un entero arbitrario $m$:

$$
18(2m)+30(-m)=6m.
$$

Por tanto, para todo $m\in\mathbb Z$ una solución concreta de

$$
18x+30y=6m
$$

es

$$
\boxed{(x,y)=(2m,-m)}.
$$


### 56

Supongamos

$$
18x_0+30y_0=c.
$$

Para $t\in\mathbb Z$ calculamos

$$
\begin{aligned}
18(x_0+5t)+30(y_0-3t)
&=18x_0+90t+30y_0-90t\\
&=18x_0+30y_0\\
&=c.
\end{aligned}
$$

Luego

$$
\boxed{(x_0+5t,\ y_0-3t)}
$$

es solución para todo $t\in\mathbb Z$. La transformación suma al lado izquierdo

$$
18(5t)+30(-3t)=90t-90t=0,
$$

de modo que no altera su valor.


### 57

Encontrar tres soluciones demuestra sólo que la ecuación tiene **al menos** tres soluciones. No demuestra que no existan otras.

Para justificar la frase “éstas son todas las soluciones” habría que probar **exhaustividad**: tomar una solución arbitraria $(x,y)$ de

$$
8x+12y=4
$$

y demostrar que necesariamente pertenece a la lista o a una familia paramétrica previamente descrita.

Es decir, una clasificación completa requiere una implicación del tipo

$$
(x,y)\text{ solución}
\Longrightarrow
(x,y)\text{ tiene una forma determinada}.
$$

Exhibir ejemplos sólo prueba la implicación contraria para esos ejemplos. La clasificación general de ecuaciones lineales diofánticas se reserva para C15.


### 58

**Primera ecuación:**

$$
10x+14y=6.
$$

Hay existencia. Por ejemplo,

$$
10(2)+14(-1)=20-14=6.
$$

Luego $(2,-1)$ es un certificado.

**Segunda ecuación:**

$$
10x+14y=5.
$$

El entero $2$ divide a $10$ y a $14$, luego divide a todo $10x+14y$. Pero $2\nmid5$. Por tanto no hay soluciones enteras.

**Tercera ecuación:**

$$
9x+15y=12.
$$

Hay existencia. Por ejemplo,

$$
9(3)+15(-1)=27-15=12.
$$

Luego $(3,-1)$ es un certificado.

Así, la primera y la tercera son solubles por exhibición directa; la segunda es imposible por una obstrucción de divisibilidad.

## H. Identidades de divisibilidad y factorización


### 59

Usamos la diferencia de cuadrados:

$$
u^2-v^2=(u-v)(u+v).
$$

Si $u-v\ne0$, el divisor está admitido por la convención del capítulo, y como $u+v\in\mathbb Z$ obtenemos

$$
\boxed{u-v\mid u^2-v^2}.
$$

El testigo es $u+v$.


### 60

La identidad se demuestra multiplicando la suma por $u-v$: las dos sumas resultantes se cancelan en los índices interiores, como en [§14.14](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md#apm-c14-s14). Para $m=1$ la suma del testigo tiene un único término, $1$, y da $u-v=(u-v)\cdot1$.

Para $m\ge1$ se cumple la identidad

$$
u^m-v^m
=(u-v)
\left(\sum_{j=0}^{m-1}u^{m-1-j}v^j\right).
$$

El factor entre paréntesis es un entero si $u,v\in\mathbb Z$. Por tanto, siempre que $u-v\ne0$,

$$
\boxed{u-v\mid u^m-v^m}.
$$

El testigo explícito es

$$
\boxed{\sum_{j=0}^{m-1}u^{m-1-j}v^j}.
$$


### 61

Aplicamos el ejercicio anterior con

$$
u=n,
\qquad
v=1.
$$

Entonces

$$
n^m-1=(n-1)
\left(\sum_{j=0}^{m-1}n^j\right).
$$

Si $n\ne1$, el divisor $n-1$ es no nulo y, como el segundo factor es entero,

$$
\boxed{n-1\mid n^m-1}.
$$

La restricción $n\ne1$ aparece únicamente porque, bajo la convención del capítulo, $0$ no se admite como divisor. Si $n=1$, la expresión que aparecería a la izquierda sería $0\mid0$, que queda fuera de la relación definida.


### 62

Escribimos

$$
n^{2m}-1=(n^2)^m-1^m.
$$

Por diferencia de potencias,

$$
(n^2)^m-1
=(n^2-1)
\left(\sum_{j=0}^{m-1}n^{2j}\right).
$$

Además,

$$
n^2-1=(n-1)(n+1).
$$

Por tanto,

$$
n^{2m}-1
=(n+1)(n-1)
\left(\sum_{j=0}^{m-1}n^{2j}\right).
$$

Si $n\ne-1$, el divisor $n+1$ es no nulo, y el factor restante es entero. Luego

$$
\boxed{n+1\mid n^{2m}-1}.
$$

No se usaron congruencias, sólo factorizaciones.


### 63

Usamos la diferencia de cuadrados con

$$
A=n^m.
$$

Entonces

$$
n^{2m}-1=(n^m)^2-1^2=(n^m-1)(n^m+1).
$$

Siempre que $n^m-1\ne0$, la definición de divisibilidad permite concluir

$$
\boxed{n^m-1\mid n^{2m}-1}.
$$

El cociente exacto es

$$
\boxed{n^m+1}.
$$


### 64

Reconocemos el cubo de una diferencia:

$$
a^3-3a^2b+3ab^2-b^3=(a-b)^3.
$$

Así,

$$
(a-b)^3=(a-b)(a-b)^2.
$$

Si $a-b\ne0$, el segundo factor $(a-b)^2$ es un entero y sirve como testigo. Por tanto,

$$
\boxed{a-b\mid a^3-3a^2b+3ab^2-b^3}.
$$


### 65

Queremos

$$
n+1\mid n+7.
$$

Como evidentemente

$$
n+1\mid n+1,
$$

por resta la condición implica

$$
n+1\mid(n+7)-(n+1)=6.
$$

Recíprocamente, si $n+1\mid6$, entonces

$$
n+7=(n+1)+6
$$

es suma de dos múltiplos de $n+1$, así que $n+1\mid n+7$. Por tanto las condiciones son equivalentes:

$$
n+1\mid n+7
\iff
n+1\mid6.
$$

Los divisores enteros no nulos de $6$ son

$$
\pm1,\ \pm2,\ \pm3,\ \pm6.
$$

Así,

$$
n+1\in\{-6,-3,-2,-1,1,2,3,6\},
$$

y por tanto

$$
\boxed{n\in\{-7,-4,-3,-2,0,1,2,5\}}.
$$

Todos estos valores satisfacen la condición porque $n+1$ divide a $6$ y, por la equivalencia demostrada, divide a $n+7$.


### 66

Buscamos reducir

$$
n^2-3n+5
$$

por un múltiplo de $n-2$. Observamos que

$$
(n-2)(n-1)=n^2-3n+2.
$$

Por tanto,

$$
n^2-3n+5=(n-2)(n-1)+3.
$$

Así,

$$
n-2\mid n^2-3n+5
\iff
n-2\mid3,
$$

siempre con $n\ne2$.

Los divisores enteros no nulos de $3$ son

$$
\pm1,\ \pm3.
$$

Entonces

$$
n-2\in\{-3,-1,1,3\},
$$

de donde

$$
\boxed{n\in\{-1,1,3,5\}}.
$$

La equivalencia garantiza también el recíproco: para cada uno de esos valores, $n-2$ divide a la expresión original.

## I. Diagnóstico y elección de método


### 67

Tomemos

$$
a=6,
\qquad
b=2,
\qquad
c=3.
$$

Entonces

$$
bc=6,
$$

de modo que

$$
6\mid bc.
$$

Pero

$$
6\nmid2.
$$

Por tanto, la implicación es falsa.

La razón lógica del fallo es que de

$$
bc=aq
$$

no podemos concluir que $b=a(q/c)$ con un **testigo entero**: aunque $c\ne0$, el cociente $q/c$ puede no ser entero. La divisibilidad requiere un cociente en $\mathbb Z$, no sólo una igualdad válida en $\mathbb Q$.


### 68

Usamos nuevamente

$$
a=6,
\qquad b=2,
\qquad c=3.
$$

Entonces

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2
\qquad\text{y}\qquad
6\nmid3.
$$

Por tanto,

$$
\boxed{a\mid bc\nRightarrow a\mid b\text{ o }a\mid c}.
$$

Este contraejemplo será importante más adelante: resultados de apariencia semejante requieren hipótesis adicionales que todavía no forman parte de C14.


### 69

Tomemos

$$
a=2,
\quad b=2,
\quad c=3,
\quad d=6.
$$

Entonces

$$
2\mid2
\qquad\text{y}\qquad
3\mid6.
$$

Sin embargo,

$$
a+c=5,
\qquad
b+d=8,
$$

y

$$
5\nmid8.
$$

Por tanto la afirmación es falsa.

La razón es que las dos divisibilidades tienen **divisores diferentes**. Escribir $b=ar$ y $d=cs$ produce

$$
b+d=ar+cs,
$$

pero no existe en general un factor común $a+c$ que pueda extraerse. La propiedad de combinación lineal exige un mismo divisor común.


### 70

Tomemos

$$
a=3,
\quad b=1,
\quad c=2.
$$

Entonces

$$
3\mid(1+2),
$$

pero

$$
3\nmid1
\qquad\text{y}\qquad
3\nmid2.
$$

Así, la implicación es falsa.

Una hipótesis adicional sencilla que sí permite recuperar una de las divisibilidades es, por ejemplo, suponer además $a\mid b$. Si

$$
a\mid(b+c)
\qquad\text{y}\qquad
a\mid b,
$$

entonces por resta

$$
a\mid[(b+c)-b]=c.
$$

Simétricamente, si sabemos $a\mid c$, entonces de $a\mid(b+c)$ deducimos $a\mid b$.


### 71

**a) $7\mid(35n+14)$.** El método más natural es la **definición con testigo** o una factorización inmediata:

$$
35n+14=7(5n+2).
$$

Como $5n+2\in\mathbb Z$, el testigo está a la vista.

**b) $a\mid b\iff b\mathbb Z\subseteq a\mathbb Z$.** El método natural es la **inclusión de conjuntos de múltiplos**, porque la afirmación compara directamente divisibilidad con pertenencia a $a\mathbb Z$ y $b\mathbb Z$.

**c) $u-v\mid u^5-v^5$.** El método natural es la **factorización**:

$$
u^5-v^5=(u-v)(u^4+u^3v+u^2v^2+uv^3+v^4).
$$

**d) Divisor común de $12n+7$ y $8n+5$.** El método natural es una **combinación lineal** que elimine $n$:

$$
2(12n+7)-3(8n+5)
=24n+14-24n-15
=-1.
$$

Por tanto todo divisor común $d$ satisface

$$
d\mid1,
$$

y así $d=\pm1$.

La elección de método depende de la estructura visible en cada problema, no de una jerarquía fija de técnicas.


### 72

La frase correcta es:

> Si $d\ne0$, $d\mid A$ y $d\mid B$, entonces para cualesquiera $r,s\in\mathbb Z$ se cumple
> $$
> d\mid(rA+sB).
> $$

Aquí “combinarlas” significa formar una **combinación lineal entera**: multiplicar cada expresión por un coeficiente entero y sumar los resultados. Si

$$
A=du,
\qquad
B=dv,
$$

entonces

$$
rA+sB=d(ru+sv),
$$

y $ru+sv$ sigue siendo entero.

La formulación original “cualquier cosa obtenida al combinarlas” es demasiado amplia. Por ejemplo, operaciones como dividir una de las expresiones por un entero arbitrario pueden destruir la existencia de un testigo entero. Si $d\mid A$, no se sigue en general que $d$ divida $A/2$, incluso cuando $A/2$ sea entero. También una operación no lineal puede necesitar una justificación distinta: algunos productos conservan divisibilidad, pero eso proviene de otra propiedad, no del teorema de combinaciones lineales.

La garantía automática de esta sección se limita a expresiones

$$
rA+sB
$$

con $r,s\in\mathbb Z$.

## M. Problemas avanzados tipo prueba


### 73

Queremos demostrar que la relación $\mid$ es un orden parcial sobre $\mathbb Z_{>0}$.

**Reflexividad.** Para todo $a>0$,

$$
a=a\cdot1,
$$

por lo que $a\mid a$.

**Antisimetría.** Supongamos $a,b>0$ y

$$
a\mid b,
\qquad
b\mid a.
$$

Por la propiedad de divisibilidad mutua para enteros no nulos,

$$
a=\pm b.
$$

Como $a$ y $b$ son positivos, la posibilidad $a=-b$ queda excluida. Por tanto,

$$
a=b.
$$

**Transitividad.** Si $a\mid b$ y $b\mid c$, existen $r,s\in\mathbb Z$ tales que

$$
b=ar,
\qquad
c=bs.
$$

Entonces

$$
c=a(rs),
$$

y por tanto $a\mid c$.

Así, $\mid$ es reflexiva, antisimétrica y transitiva sobre $\mathbb Z_{>0}$; luego define un orden parcial.

Ahora consideremos $\mathbb Z\setminus\{0\}$. La antisimetría falla porque los signos producen pares distintos que se dividen mutuamente. El contraejemplo mínimo en valor absoluto es

$$
1\mid(-1)
\qquad\text{y}\qquad
-1\mid1,
$$

pero

$$
1\ne-1.
$$

Esto concuerda exactamente con el teorema general de divisibilidad mutua:

$$
a\mid b,
\quad b\mid a
\Longrightarrow
 a=\pm b.
$$

Sobre los positivos, el signo negativo desaparece y se obtiene $a=b$; sobre los enteros no nulos, $a=-b$ sigue siendo una posibilidad legítima. Ésa es la razón precisa del fallo de antisimetría.


### 74

Primero probamos

$$
a\mid b
\iff
b\mathbb Z\subseteq a\mathbb Z.
$$

**$(\Rightarrow)$** Supongamos $a\mid b$. Existe $q\in\mathbb Z$ con

$$
b=aq.
$$

Sea $x\in b\mathbb Z$. Entonces $x=bt$ para algún $t\in\mathbb Z$. Sustituyendo,

$$
x=(aq)t=a(qt).
$$

Como $qt\in\mathbb Z$, se tiene $x\in a\mathbb Z$. Por tanto,

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

**$(\Leftarrow)$** Supongamos

$$
b\mathbb Z\subseteq a\mathbb Z.
$$

Como $b=b\cdot1$, tenemos $b\in b\mathbb Z$. La inclusión implica $b\in a\mathbb Z$, de modo que existe $q\in\mathbb Z$ con

$$
b=aq.
$$

Así, $a\mid b$.

Queda demostrada la equivalencia.

Ahora supongamos

$$
a\mathbb Z=b\mathbb Z.
$$

Entonces se tienen las dos inclusiones, por lo que la equivalencia anterior da

$$
a\mid b
\qquad\text{y}\qquad
b\mid a.
$$

Por divisibilidad mutua,

$$
a=\pm b.
$$

Recíprocamente, si $a=b$ es trivial que los conjuntos coinciden. Si $a=-b$, entonces

$$
ak=b(-k),
$$

de modo que cada múltiplo de $a$ es múltiplo de $b$, y viceversa. Por tanto,

$$
\boxed{a\mathbb Z=b\mathbb Z\iff a=\pm b}.
$$

La dirección de la inclusión parece invertida porque “$b$ es múltiplo de $a$” significa que $b$ contiene al factor $a$. Por ello, cualquier nuevo múltiplo de $b$ contiene también ese factor $a$. Cuanto más arriba está un número en el orden de divisibilidad, más restrictivo es ser múltiplo suyo; por eso su conjunto de múltiplos es más pequeño por inclusión.


### 75

Primero demostremos la equivalencia básica. Si $a\mid b$, existe $q\in\mathbb Z$ con $b=aq$. Entonces

$$
b+ka=a(q+k),
$$

y como $q+k\in\mathbb Z$,

$$
a\mid(b+ka).
$$

Recíprocamente, si $a\mid(b+ka)$, entonces también $a\mid ka$. Restando el múltiplo $ka$ obtenemos

$$
a\mid[(b+ka)-ka]=b.
$$

Así,

$$
\boxed{a\mid b\iff a\mid(b+ka)}
$$

para todo $k\in\mathbb Z$.

**a)**

$$
37\cdot125+74
=37\cdot125+2\cdot37
=37(127).
$$

Por tanto,

$$
\boxed{37\mid37\cdot125+74}.
$$

**b)** Sea

$$
A=101n+37,
\qquad
B=100n+36.
$$

Si $d\mid A$ y $d\mid B$, entonces por resta

$$
d\mid(A-B)=n+1.
$$

Como también $d\mid B$, podemos eliminar $n$:

$$
B-100(n+1)
=100n+36-100n-100
=-64.
$$

Por tanto,

$$
\boxed{d\mid64}.
$$

**c)** Sea

$$
C=53n+18,
\qquad
D=52n+17.
$$

Por resta,

$$
d\mid(C-D)=n+1.
$$

Luego, usando $D$,

$$
52(n+1)-D
=52n+52-(52n+17)
=35.
$$

Así,

$$
\boxed{d\mid35}.
$$

La restricción resultante es que $d$ debe ser uno de los divisores enteros no nulos de $35$:

$$
\boxed{d\in\{\pm1,\pm5,\pm7,\pm35\}}.
$$

No afirmamos que todos ellos dividan necesariamente a ambas expresiones para un $n$ dado; afirmamos sólo que cualquier divisor común posible debe pertenecer a esa lista.


### 76

La factorización de [§14.14](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md#apm-c14-s14) se obtiene por distributividad y telescopaje: al multiplicar el testigo por $u$ y por $v$, las contribuciones interiores coinciden y se restan, dejando $u^m-v^m$. Para $m=1$ el testigo es $1$; en los dos corolarios, las sumas con un solo término también valen $1$.

Para $m\ge1$ usamos la identidad

$$
u^m-v^m
=(u-v)
\left(\sum_{j=0}^{m-1}u^{m-1-j}v^j\right).
$$

Si $u-v\ne0$, el factor de la derecha entre paréntesis es un entero y actúa como testigo. Luego

$$
\boxed{u-v\mid u^m-v^m}.
$$

**Primer corolario.** Tomamos

$$
u=n,
\qquad
v=1.
$$

Entonces, si $n\ne1$,

$$
\boxed{n-1\mid n^m-1}.
$$

**Segundo corolario.** Queremos un factor $n+1$. Aplicamos la diferencia de potencias a

$$
u=n^2,
\qquad
v=1.
$$

Así,

$$
n^{2m}-1
=(n^2-1)
\left(\sum_{j=0}^{m-1}n^{2j}\right).
$$

Como

$$
n^2-1=(n-1)(n+1),
$$

obtenemos, si $n\ne-1$,

$$
\boxed{n+1\mid n^{2m}-1}.
$$

La diferencia conceptual entre ambos corolarios es la sustitución. El primero usa directamente $u=n$, $v=1$; el segundo usa $u=n^2$, $v=1$ y luego factoriza $n^2-1$. En ningún paso se necesitan congruencias.


### 77

Queremos determinar los enteros $n\ne-1$ que satisfacen

$$
n+1\mid n^2+1.
$$

La clave es la identidad

$$
n^2+1-(n-1)(n+1)=2.
$$

Si $n+1\mid n^2+1$, entonces $n+1$ divide también a $(n-1)(n+1)$. Por cierre bajo resta,

$$
\boxed{n+1\mid2}.
$$

Recíprocamente, si $n+1\mid2$, entonces

$$
n^2+1=(n-1)(n+1)+2
$$

es suma de dos múltiplos de $n+1$, y por tanto $n+1\mid n^2+1$. Así, para $n\ne-1$,

$$
n+1\mid n^2+1
\iff
n+1\mid2.
$$

Los divisores enteros no nulos de $2$ son

$$
-2,-1,1,2.
$$

Por tanto,

$$
n+1\in\{-2,-1,1,2\},
$$

de donde

$$
\boxed{n\in\{-3,-2,0,1\}}.
$$

Verificamos:

- $n=-3$: $n+1=-2$ y $n^2+1=10$, luego $-2\mid10$;
- $n=-2$: $n+1=-1$ y $n^2+1=5$, luego $-1\mid5$;
- $n=0$: $n+1=1$ y $n^2+1=1$;
- $n=1$: $n+1=2$ y $n^2+1=2$.

Todos los candidatos funcionan, y la equivalencia demuestra que no hay otros.


### 78

Supongamos

$$
a_1\mid a_2\mid\cdots\mid a_m
$$

con todos los $a_i$ no nulos.

**a)** Cada relación consecutiva

$$
a_i\mid a_{i+1}
$$

permite aplicar la cota de divisibilidad:

$$
|a_i|\le|a_{i+1}|.
$$

Encadenando,

$$
\boxed{|a_1|\le|a_2|\le\cdots\le|a_m|}.
$$

**b)** Supongamos además

$$
|a_1|=|a_m|.
$$

Tenemos una cadena de números reales

$$
|a_1|\le|a_2|\le\cdots\le|a_m|=|a_1|.
$$

No puede haber una desigualdad estricta intermedia, porque entonces el último valor sería estrictamente mayor que el primero. Por tanto,

$$
|a_1|=|a_2|=\cdots=|a_m|.
$$

Así, para cada $i$,

$$
|a_i|=|a_1|,
$$

y por tanto

$$
\boxed{a_i=\pm a_1}.
$$

También puede verse mediante la divisibilidad: por transitividad, $a_1\mid a_i$; como tienen el mismo valor absoluto, el cociente sólo puede ser $1$ o $-1$.

**c)** La **transitividad** permite pasar de la cadena local a relaciones como

$$
a_1\mid a_i
\qquad\text{y}\qquad
a_i\mid a_m.
$$

La **cota** $a\mid b\Rightarrow|a|\le|b|$ produce la monotonía de los valores absolutos. En la prueba más directa de la parte b), esa monotonía y la igualdad de los extremos fuerzan la igualdad de todos los valores intermedios.


### 79

La supuesta prueba parte correctamente de

$$
a\mid bc
\Longrightarrow
bc=aq
$$

para algún $q\in\mathbb Z$. El error aparece cuando se divide por $c$ y se escribe

$$
b=a\left(\frac qc\right)
$$

como si $q/c$ fuese automáticamente un entero.

**1. Paso inválido.** La división por $c$ puede ser válida como igualdad racional cuando $c\ne0$, pero no conserva necesariamente la condición que exige la divisibilidad: un **testigo entero**.

**2. Por qué $q/c$ puede no ser entero.** Nada en $bc=aq$ obliga a que $c\mid q$. Por ejemplo, si

$$
a=6,
\quad b=2,
\quad c=3,
$$

entonces

$$
bc=6=6\cdot1,
$$

así que podemos tomar $q=1$. Pero

$$
\frac qc=\frac13\notin\mathbb Z.
$$

**3. Contraejemplo.** Con esos mismos valores,

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2
\qquad\text{y}\qquad
6\nmid3.
$$

Por tanto la afirmación completa es falsa.

**4. Por qué la definición no permite la cancelación.** Para demostrar $a\mid b$ necesitamos producir un entero $r$ tal que

$$
b=ar.
$$

La manipulación sólo produce el candidato racional $r=q/c$; mientras no se demuestre que $q/c\in\mathbb Z$, no existe un testigo válido. La cancelación legítima estudiada antes tenía la forma

$$
ca\mid cb\Longrightarrow a\mid b,
$$

porque la igualdad asociada es

$$
cb=caq,
$$

y al cancelar $c\ne0$ queda directamente

$$
b=aq
$$

con el mismo testigo entero $q$. Aquí la situación algebraica es distinta.

**5. Qué falta estudiar.** Para obtener resultados de la forma “un divisor de un producto debe dividir a uno de los factores” hacen falta hipótesis adicionales sobre el divisor y sobre la estructura aritmética de los enteros. Esas hipótesis se estudiarán más adelante, especialmente al introducir números primos en C16. En C14 no debemos usarlas ni anticipar un teorema que sin ellas es falso.


### 80

Estudiamos

$$
18x+30y=c.
$$

**a) Condición necesaria.** Como

$$
6\mid18
\qquad\text{y}\qquad
6\mid30,
$$

para cualesquiera $x,y\in\mathbb Z$ se tiene

$$
6\mid(18x+30y).
$$

Por tanto, si existe una solución de

$$
18x+30y=c,
$$

necesariamente

$$
\boxed{6\mid c}.
$$

**b) Certificado para $c=6$.** Calculamos

$$
18(2)+30(-1)=36-30=6.
$$

Así,

$$
\boxed{(2,-1)}
$$

es una solución de $18x+30y=6$.

**c) Existencia cuando $c=6m$.** Sea $m\in\mathbb Z$. Multiplicamos el certificado anterior por $m$:

$$
18(2m)+30(-m)=6m.
$$

Por tanto, una solución explícita es

$$
\boxed{(x,y)=(2m,-m)}.
$$

Esto demuestra que, para esta ecuación concreta, la condición $6\mid c$ no sólo es necesaria: también basta para producir al menos una solución.

**d) Familia infinita a partir de una solución.** Supongamos que $(x_0,y_0)$ satisface

$$
18x_0+30y_0=c.
$$

Para $t\in\mathbb Z$,

$$
\begin{aligned}
18(x_0+5t)+30(y_0-3t)
&=18x_0+90t+30y_0-90t\\
&=18x_0+30y_0\\
&=c.
\end{aligned}
$$

Así,

$$
\boxed{(x_0+5t,\ y_0-3t)}
$$

es solución para todo $t\in\mathbb Z$.

Además, si $t_1\ne t_2$, las primeras coordenadas

$$
x_0+5t_1
\qquad\text{y}\qquad
x_0+5t_2
$$

son distintas. Por tanto esta construcción produce infinitas soluciones diferentes.

**e) Puente conceptual hacia C15.** En este ejemplo encontramos un entero, $6$, con dos propiedades decisivas:

1. divide simultáneamente a los coeficientes $18$ y $30$;
2. además puede escribirse como una combinación lineal de ellos:
   $$
   6=18(2)+30(-1).
   $$

La primera propiedad produce la obstrucción $6\mid c$; la segunda permite convertir cualquier múltiplo $6m$ en una combinación lineal de $18$ y $30$, fabricando una solución.

Esto sugiere la pregunta general correcta para el capítulo siguiente: dados dos coeficientes $a$ y $b$, ¿cómo encontrar sistemáticamente un divisor común que concentre toda la información relevante y, al mismo tiempo, pueda obtenerse mediante combinaciones lineales de $a$ y $b$?

C14 no responde todavía esa pregunta en general. Sólo muestra, mediante este ejemplo, por qué necesitamos una herramienta nueva.

## N. Testigos, dominios y certificados


### 81

C13 proporciona el entero $\binom nk$, que cuenta los subconjuntos de tamaño $k$ de un conjunto de $n$ elementos. La fórmula factorial se reescribe como $n!=k!(n-k)!\binom nk$. Como los factoriales son positivos, el divisor es no nulo y $\binom nk$ es el testigo buscado.

Si también $n!\mid k!(n-k)!$, existiría un entero $q$ con $k!(n-k)!=n!q$. Al sustituir y cancelar el factorial no nulo obtenemos $1=\binom nk q$. Como $\binom nk$ es positivo, esto obliga a $\binom nk=1$ y $q=1$. En $k=0$ o $k=n$ hay un único subconjunto, de modo que los dos factoriales son iguales y la divisibilidad inversa sí se cumple. Si $0<k<n$, hay al menos dos subconjuntos distintos: toma uno de tamaño $k$ y reemplaza uno de sus elementos por otro que esté fuera. Por tanto $\binom nk\ge2$ y la inversa no se cumple. La clasificación completa es $k=0$ o $k=n$; para $n=0$ ambos casos coinciden en $k=0$, y los dos números valen $0!=1$.


### 82

Si $n=2t$, entonces $n(n+1)=2[t(2t+1)]$, con testigo entero $t(2t+1)$. Si $n=2t+1$, entonces $n(n+1)=(2t+1)(2t+2)=2[(2t+1)(t+1)]$, con testigo entero $(2t+1)(t+1)$. Las dos formas de los enteros pares e impares cubren todos los enteros, también negativos, y en ambas el testigo es un producto de enteros. Para $n=0$ y $n=-1$, el producto y el testigo son cero.

El candidato $n^2/2$ falla primero en la igualdad: $2(n^2/2)=n^2$, que sólo coincide con $n(n+1)=n^2+n$ cuando $n=0$. Además, para $n$ impar ni siquiera es entero. Por ejemplo, para $n=2$ el candidato es entero pero da $4$ en vez de $6$; para $n=1$ no es entero y da $1$ en vez de $2$. Un testigo válido debe satisfacer simultáneamente la igualdad y el dominio. El testigo único puede escribirse uniformemente como $n(n+1)/2$ después de que los dos casos hayan probado que esa expresión es entera.


### 83

La identidad $2n+5=2(n-3)+11$ permite reducir la condición. Si $n-3$ divide a $2n+5$, también divide a $2(n-3)$ y, por resta, a once. Si divide a once, por suma divide a $2n+5$. Luego, para $n\ne3$, las dos condiciones son equivalentes.

Los divisores enteros de once son $\pm1$ y $\pm11$. Se puede verificar la lista sin teoría de primos: la cota de [§14.7](algebra-para-matematicos-capitulo-14-los-enteros-y-la-divisibilidad.md#apm-c14-s07) reduce los valores absolutos a $1,\ldots,11$, y la comprobación de esos once candidatos deja sólo uno y once. Así $n-3\in\{-11,-1,1,11\}$ y

$$
\boxed{n\in\{-8,2,4,14\}}.
$$

Los testigos para la expresión original son, respectivamente, $1,-9,13,3$: $-11=(-11)\cdot1$, $9=(-1)(-9)$, $13=1\cdot13$ y $33=11\cdot3$. La equivalencia y la lista finita de divisores prueban exhaustividad. El valor $n=3$ se excluyó antes de operar porque produciría un divisor cero.


### 84

Como $c\mid b$, el número $b/c$ es entero; eso asegura que la conclusión propuesta tiene sentido, pero no que sea verdadera. Para $a=c=m$, $b=m(m+1)$, ambas hipótesis tienen testigo $m+1$. Sin embargo $b/c=m+1$ y $m\nmid(m+1)$: si $m+1=mr$, entonces $1=m(r-1)$, imposible para $m\ge2$. El cociente candidato $q/c=(m+1)/m$ es racional y no entero.

Si $c\mid q$, escribimos $q=cs$ con $s\in\mathbb Z$. Entonces $b=acs$ y $b/c=as$, por lo que $a\mid b/c$. Recíprocamente, si $b/c=as$ para un entero $s$, multiplicamos por $c$ y comparamos con $b=aq$: $aq=acs$. Al cancelar $a\ne0$ resulta $q=cs$, que prueba $c\mid q$. La reparación exige que el **testigo** sea divisible por $c$; saber que el dividendo $b$ lo es no basta. Los signos de $a$ y $c$ no afectan la demostración.


### 85

La respuesta general es negativa. Para $a=2r$, $u=0$ y $v=2r$, ambos números son múltiplos de $a$ y su promedio es $h=r\in\mathbb Z$. Pero $2r\nmid r$: un testigo entero $Q$ exigiría $1=2Q$ tras cancelar $r\ne0$. El promedio puede ser entero sin pertenecer al conjunto de múltiplos del divisor original.

Para obtener el criterio exacto, observamos $2h=u+v=a(s+t)$. Si $a\mid h$, escribimos $h=aQ$ con $Q\in\mathbb Z$; al sustituir y cancelar $a\ne0$, $2Q=s+t$, así que $s+t$ es par. Recíprocamente, si $s+t=2Q$ para un entero $Q$, entonces $h=aQ$, que proporciona el testigo. La condición de pertenencia de $h$ a $\mathbb Z$ no reemplaza la condición de pertenencia de $(s+t)/2$ a $\mathbb Z$. Cuando $s+t$ es par, el testigo es exactamente $(s+t)/2$.


### 86

Sumar y restar da $2a=d(u+v)$ y $2b=d(u-v)$; por sí solo esto prueba divisibilidad de $2a$ y $2b$. Para $d=2r$, $a=b=r$, $r\ge1$, los testigos iniciales son $u=1$, $v=0$, pues $a+b=2r$ y $a-b=0$. Sin embargo $d$ no divide a $a$ ni a $b$, porque $r=2rQ$ exigiría $1=2Q$. La división por dos ha perdido el dominio de los testigos.

Si $u$ y $v$ tienen la misma paridad, tanto $u+v$ como $u-v$ son pares. Los enteros $(u+v)/2$ y $(u-v)/2$ son entonces testigos de $d\mid a$ y $d\mid b$. Recíprocamente, si ambas conclusiones son verdaderas, escribimos $a=dA$, $b=dB$. Al comparar con las igualdades iniciales y cancelar $d$, obtenemos $u=A+B$ y $v=A-B$; su diferencia es $2B$, así que tienen la misma paridad. Esto prueba necesidad y suficiencia. Incluso una sola conclusión, $d\mid a$, obligaría a que $u+v$ fuese par y permitiría obtener la otra.


### 87

Un elemento $am^2t$ se escribe $am(mt)$, y un elemento $amt$ se escribe $a(mt)$. Por tanto,

$$
(am^2)\mathbb Z\subseteq(am)\mathbb Z\subseteq a\mathbb Z.
$$

Si $|m|=1$, multiplicar el generador por $m$ sólo conserva o cambia su signo, y los tres conjuntos coinciden. Si $|m|\ge2$, el elemento $a$ pertenece al conjunto mayor pero no a $(am)\mathbb Z$, porque $a=amq$ implicaría $1=mq$. A su vez $am$ pertenece al conjunto intermedio pero no a $(am^2)\mathbb Z$, porque $am=am^2q$ implicaría otra vez $1=mq$. Esa igualdad es imposible para un entero $q$: si no es cero, $|mq|\ge2$. Las dos inclusiones son estrictas. Todo entero no nulo $m$ cae en uno de esos casos, lo que completa la clasificación. Los signos negativos sólo modifican los testigos; no la dirección de la inclusión.


### 88

Si $a\mid b$, entonces $b\mathbb Z\subseteq a\mathbb Z$, de modo que la unión es $a\mathbb Z$. Si $b\mid a$, la unión es $b\mathbb Z$. Queda probada la suficiencia.

Para la necesidad, supongamos que la unión es $c\mathbb Z$, con $c\ne0$. Como $a$ y $b$ pertenecen a la unión, ambos son múltiplos de $c$; su suma también pertenece a $c\mathbb Z$ y, por la igualdad de conjuntos, a $a\mathbb Z\cup b\mathbb Z$. Si $a+b\in a\mathbb Z$, entonces $a\mid(a+b)$ y, al restar $a$, $a\mid b$. Si $a+b\in b\mathbb Z$, análogamente $b\mid a$. La pertenencia a una unión obliga a una de esas dos alternativas, aunque pueda cumplir ambas. Esto incluye $a+b=0$, caso en que $a=-b$ y los conjuntos ya coinciden.

Por ejemplo, $4\mathbb Z\cup6\mathbb Z$ no es $c\mathbb Z$ para ningún $c\ne0$: el número $10=4+6$ no pertenece a la unión, aunque todo conjunto de múltiplos es cerrado bajo suma. No se necesita encontrar un generador común para probar la imposibilidad.


### 89

Si $b=aq$ para un entero $q$, entonces $b+ak=a(q+k)$ y todo elemento de $L$ pertenece a $a\mathbb Z$. Para el sentido inverso, cualquier $at\in a\mathbb Z$ se escribe $b+a(t-q)$; como $t-q$ es entero, pertenece a $L$. Así se obtiene igualdad, no sólo inclusión.

Si existiera un elemento $x\in L\cap a\mathbb Z$, habría enteros $k,t$ con $x=b+ak=at$. Por resta, $b=a(t-k)$, lo que probaría $a\mid b$. Por tanto, cuando $a\nmid b$, la intersección es vacía. Este argumento también explica por qué un solo elemento compartido basta para decidir la divisibilidad: produce el testigo $t-k$. El caso $b=0$ pertenece a la primera alternativa con testigo cero. Por ejemplo, $5+3\mathbb Z$ y $3\mathbb Z$ no comparten elementos porque $3\nmid5$; en cambio, $6+3\mathbb Z=3\mathbb Z$. La descripción se obtiene directamente con igualdades enteras.


### 90

El certificado es correcto: $-35+44=9$. Al multiplicar por $m$, obtenemos una solución $(-m,2m)$. Como $35\cdot22+22(-35)=0$, podemos añadir cualquier múltiplo entero del desplazamiento $(22,-35)$:

$$
(x,y)=(-m+22t,\ 2m-35t),\qquad t\in\mathbb Z.
$$

La sustitución da $35x+22y=9m$ para todo $t$, y distintos parámetros producen primeras coordenadas distintas. Esto prueba generación de infinitas soluciones, sin afirmar que sean todas las de la ecuación sin restricción.

Para clasificar las que además satisfacen $x+y=m$, partimos de una pareja arbitraria con ambas propiedades. De $y=m-x$ resulta $35x+22(m-x)=9m$, es decir, $13x=-13m$. Cancelar trece da $x=-m$ y luego $y=2m$. Esta pareja cumple ambas ecuaciones para todo entero $m$, así que es la única. Dentro de la familia construida, la suma es $m-13t$ y la restricción selecciona $t=0$; la exhaustividad no depende de suponer que esa familia era completa, porque se probó desde una pareja arbitraria.


### 91

El lado izquierdo es $13(2x+3y)$, así que cualquier solución obliga a $13\mid c$. Recíprocamente, si $c=13m$, el certificado multiplicado por $m$ da $26(-m)+39m=13m$; por ello $(-m,m)$ es una solución entera. Esto demuestra el criterio para estos coeficientes concretos, sin invocar un teorema general de MCD ni afirmar una familia exhaustiva.

La condición de no negatividad exige una revisión adicional. Para $c=13$, cancelar trece da $2x+3y=1$. Si $x\ge1$, el lado izquierdo es al menos dos; si $y\ge1$, es al menos tres. Si ambos son cero, es cero. Las alternativas cubren todas las parejas no negativas, y ninguna da uno. Por tanto no hay solución no negativa, aunque $(-1,1)$ sí es una solución entera.

Para $c=26$, la pareja $(1,0)$ es un certificado no negativo; para $c=39$, lo es $(0,1)$. La existencia sobre $\mathbb Z^2$ y la existencia bajo restricciones adicionales son preguntas distintas. La condición $13\mid c$ por sí sola no garantiza satisfacer dichas restricciones.


### 92

Escribimos $14b=au$ y $9b=av$ con $u,v\in\mathbb Z$. La identidad $2\cdot14-3\cdot9=1$ permite recuperar

$$
b=2(14b)-3(9b)=a(2u-3v).
$$

El testigo $2u-3v$ es entero, de modo que $a\mid b$. El certificado numérico asegura el dominio del testigo y evita una división por un factor cuya divisibilidad no está establecida.

En la segunda pregunta escribimos $14b=au$ y $10b=aw$. Ahora $3\cdot14-4\cdot10=2$, así que $2b=a(3u-4w)$ y concluimos $a\mid2b$. No se puede dividir por dos y afirmar automáticamente $a\mid b$. Con $a=2$ y $b=1$, las dos hipótesis son verdaderas, con testigos siete y cinco, pero $2\nmid1$. El testigo construido para $2b$ es $3\cdot7-4\cdot5=1$, cuya mitad no es entera. Las dos preguntas muestran qué cambia cuando una combinación conocida produce uno o produce dos. No se ha supuesto que exista una combinación con valor uno para coeficientes arbitrarios.

***

[← Capítulo 13](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 15 →](algebra-para-matematicos-capitulo-15-maximo-comun-divisor-y-algoritmo-de-euclides.md)

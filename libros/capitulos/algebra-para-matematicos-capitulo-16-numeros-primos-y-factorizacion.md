---
{
  "title": "Números primos y factorización",
  "description": "Capítulo 16 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0191",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C16",
  "editorial-id": "MA-BCH-APM-01-016",
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
    "MA-BCH-0190"
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

En los dos capítulos anteriores estudiamos la divisibilidad desde dos perspectivas complementarias. Primero aprendimos a leer $a\mid b$ como una afirmación de existencia: existe un entero que actúa como testigo de que $b$ es múltiplo de $a$. Después vimos que el máximo común divisor organiza todas las combinaciones lineales de dos enteros y que el algoritmo de Euclides permite calcularlo sin factorizar.

Ahora cambia la pregunta. Ya no preguntaremos principalmente qué divisores comparten dos números, sino **de qué piezas multiplicativas está construido un entero**.

Consideremos, por ejemplo,

$$
84=2\cdot42=2\cdot2\cdot21=2^2\cdot3\cdot7.
$$

Podemos descomponer $84$ de muchas maneras intermedias, pero el proceso parece terminar siempre en los mismos bloques: $2$, $3$ y $7$. Lo mismo ocurre con

$$
360=2^3\cdot3^2\cdot5.
$$

La afirmación de que esto no es una coincidencia exige dos teoremas diferentes. Debemos probar, primero, que toda descomposición termina efectivamente en números primos y, segundo, que no puede terminar en una colección esencialmente distinta de primos.

La idea central del capítulo será:

> **Los números primos son los bloques multiplicativos elementales de los enteros porque todo entero no nulo y no unidad se descompone, salvo una unidad de signo, en primos positivos, y el lema de Euclides obliga a que esa descomposición sea esencialmente única.**

No utilizaremos congruencias, clases residuales ni inversos modulares. La teoría de este capítulo se construirá únicamente con divisibilidad, MCD, Bézout, inducción y razonamiento sobre productos.

***
## 16.1. De los divisores comunes a los bloques multiplicativos {#apm-c16-s01}

En C15 la pregunta decisiva para dos enteros $a$ y $b$ era encontrar un entero positivo que concentrara la información de todos sus divisores comunes. Esa pregunta conducía al máximo común divisor.

Para estudiar la estructura interna de un solo entero necesitamos otro tipo de análisis. Si $n$ puede escribirse como

$$
n=ab,
$$

entonces $a$ y $b$ revelan una descomposición multiplicativa de $n$. Pero esa escritura puede ser poco informativa. Por ejemplo,

$$
60=6\cdot10
$$

y tanto $6$ como $10$ todavía pueden descomponerse. En cambio,

$$
60=2^2\cdot3\cdot5
$$

parece haber llegado a una etapa en la que ninguno de los factores puede seguir rompiéndose en factores positivos mayores que $1$.

Esto sugiere distinguir entre dos clases de enteros positivos mayores que $1$:

- aquellos que admiten una descomposición no trivial;
- aquellos que no la admiten.

La segunda clase será la de los **números primos**.

Hay aquí una diferencia metodológica importante respecto de los capítulos anteriores. Saber calcular algunas factorizaciones no demuestra que toda factorización exista ni que sea única. Por ejemplo, observar

$$
12=2^2\cdot3,
\qquad
18=2\cdot3^2,
\qquad
45=3^2\cdot5
$$

sólo proporciona ejemplos. El objetivo del capítulo es establecer un teorema universal para **todo** entero positivo mayor que $1$.

Además, debemos cuidar una posible circularidad. Sería tentador demostrar propiedades de los primos usando ya la unicidad de la factorización y luego utilizar esas mismas propiedades para probar la unicidad. No lo haremos. La secuencia lógica será:

```text
EXISTENCIA: PRIMOS Y COMPUESTOS + INDUCCIÓN FUERTE
UNICIDAD: BÉZOUT Y COPRIMALIDAD DE C15 → LEMA DE EUCLIDES → PRODUCTOS FINITOS
TEOREMA FUNDAMENTAL: EXISTENCIA + UNICIDAD
CONSECUENCIAS SOBRE EXPONENTES: TEOREMA FUNDAMENTAL
```

Esta dirección será esencial durante todo el capítulo.

***
## 16.2. Primos, compuestos, unidades y casos frontera {#apm-c16-s02}

Trabajaremos primero con enteros positivos.

Un entero $p$ se llama **primo** si

$$
p>1
$$

y sus únicos divisores positivos son $1$ y $p$.

Equivalentemente, si $d>0$ y $d\mid p$, entonces

$$
d=1
\qquad\text{o}\qquad
d=p.
$$

Los primeros primos son

$$
2,3,5,7,11,13,17,19,23,\ldots
$$

Un entero positivo $n>1$ se llama **compuesto** si existen enteros positivos $a,b$ tales que

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Por ejemplo,

$$
21=3\cdot7,
$$

por lo que $21$ es compuesto. En cambio, si intentamos factorizar $13$ como producto de dos enteros positivos, necesariamente uno de ellos debe ser $1$.

Para $n>1$, las categorías primo y compuesto son complementarias. En efecto, si $n$ no es primo, existe un divisor positivo $d$ de $n$ distinto de $1$ y de $n$. Escribiendo $n=dq$, tenemos $1<d<n$ y también $1<q<n$; por tanto, $n$ es compuesto. Recíprocamente, si $n=ab$ con $1<a,b<n$, entonces $a$ es un divisor positivo no trivial de $n$, de modo que $n$ no es primo.

### Por qué $1$ no es primo

El entero $1$ posee un solo divisor positivo: él mismo. La definición de primo exige dos divisores positivos distintos, $1$ y $p$, con $p>1$. Por tanto, $1$ no es primo.

Esta exclusión no es una convención ornamental. Si permitiéramos que $1$ fuera primo, una factorización nunca sería única en un sentido razonable, pues podríamos escribir

$$
6=2\cdot3=1\cdot2\cdot3=1^2\cdot2\cdot3=\cdots.
$$

### Por qué $0$ no es primo

Todo entero no nulo divide a $0$. Por tanto, $0$ tiene demasiados divisores y no puede satisfacer la definición de primo. Tampoco es compuesto en el sentido que acabamos de fijar, porque la categoría de compuesto se reserva a enteros positivos mayores que $1$.

### Las unidades de $\mathbb Z$

Un entero $u$ es una **unidad** cuando posee inverso multiplicativo entero: existe $v\in\mathbb Z$ tal que

$$
uv=1.
$$

En los enteros esto obliga a

$$
|u|=|v|=1.
$$

Por tanto, las únicas unidades de $\mathbb Z$ son

$$
1\quad\text{y}\quad -1.
$$

Las unidades permiten cambiar el signo de una factorización sin alterar sus factores primos esenciales. Por ejemplo,

$$
-30=(-1)\cdot2\cdot3\cdot5.
$$

En este capítulo llamaremos **primos** únicamente a los primos positivos. Así, $-5$ no se llamará primo en la exposición elemental; diremos que $-5$ y $5$ difieren por multiplicación por la unidad $-1$.

Esta decisión nos permitirá formular la unicidad sin ambigüedades de signo.

***
## 16.3. Irreducibles en $\mathbb Z$ y relación con los primos {#apm-c16-s03}

La palabra “primo” está formulada mediante divisores. Existe otra manera de describir la misma rigidez multiplicativa en los enteros.

Diremos que un entero $a$ es **irreducible en $\mathbb Z$** si:

1. $a\ne0$;
2. $a$ no es una unidad;
3. siempre que
   $$
   a=bc,
   $$
   con $b,c\in\mathbb Z$, al menos uno de los factores $b$ o $c$ es una unidad.

Por ejemplo, $5$ es irreducible. Si

$$
5=bc,
$$

entonces, tomando valores absolutos,

$$
5=|b||c|.
$$

Como $5$ no posee divisores positivos intermedios, uno de $|b|,|c|$ debe ser $1$.

En $\mathbb Z$, para enteros positivos mayores que $1$, “primo” e “irreducible” describen exactamente los mismos números.

### Proposición

Sea $p>1$. Entonces

$$
\boxed{
p\text{ es primo}
\iff
p\text{ es irreducible en }\mathbb Z.
}
$$

### Demostración

Supongamos primero que $p$ es primo y que

$$
p=ab.
$$

Entonces $|a|$ es un divisor positivo de $p$. Como $p$ es primo,

$$
|a|=1
\qquad\text{o}\qquad
|a|=p.
$$

En el primer caso $a$ es una unidad. En el segundo, como $|a||b|=p$, necesariamente $|b|=1$, de modo que $b$ es una unidad. Por tanto, $p$ es irreducible.

Recíprocamente, supongamos que $p$ es irreducible y sea $d>0$ un divisor de $p$. Entonces existe $q\in\mathbb Z$ tal que

$$
p=dq.
$$

Como $p>0$ y $d>0$, resulta $q>0$. Por irreducibilidad, uno de $d$ o $q$ debe ser una unidad. Al ser positivos, esto significa que uno de ellos es $1$. Si $d=1$, obtenemos el divisor trivial inferior; si $q=1$, entonces $d=p$. Por tanto, los únicos divisores positivos de $p$ son $1$ y $p$.

Luego $p$ es primo.

Esta equivalencia es propia de la estructura de los enteros que estamos estudiando. Más adelante, cuando aparezcan otros anillos, será importante no suponer sin prueba que “primo” e “irreducible” siguen siendo conceptos equivalentes. Aquí, sin embargo, la equivalencia queda completamente demostrada.

***
## 16.4. Todo entero mayor que $1$ tiene un divisor primo {#apm-c16-s04}

Antes de demostrar que todo entero factoriza como producto de primos, necesitamos un resultado más elemental: todo entero mayor que $1$ posee **al menos un** divisor primo.

### Teorema

Para todo entero $n>1$, existe un primo $p$ tal que

$$
p\mid n.
$$

### Demostración por inducción fuerte

Definamos la proposición $P(n)$:

> el entero $n>1$ posee un divisor primo.

**Base.** Para $n=2$, el propio $2$ es primo y $2\mid2$.

**Paso inductivo fuerte.** Supongamos que $P(m)$ es verdadera para todo entero $m$ con

$$
2\le m<n.
$$

Queremos demostrar $P(n)$.

Si $n$ es primo, entonces $n$ es un divisor primo de sí mismo y terminamos.

Si $n$ no es primo, como $n>1$ debe ser compuesto. Por tanto, existen $a,b$ tales que

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Por la hipótesis inductiva aplicada a $a$, existe un primo $p$ con

$$
p\mid a.
$$

Como $a\mid n$, por transitividad de la divisibilidad obtenemos

$$
p\mid n.
$$

Así $n$ posee un divisor primo.

La inducción fuerte queda completada.

### Qué hemos demostrado y qué no

El teorema garantiza sólo la existencia de **un** divisor primo. Todavía no hemos demostrado que podamos continuar descomponiendo hasta obtener una factorización completa, y mucho menos que esa factorización sea única.

Sin embargo, este resultado tendrá dos usos inmediatos:

- permitirá demostrar más adelante el criterio de primalidad hasta $\sqrt n$;
- garantizará que cualquier entero $N>1$ construido en la prueba de infinitud de los primos posee algún divisor primo, incluso si $N$ no es primo.

Esta distinción será crucial.

***
## 16.5. El lema de Euclides para primos {#apm-c16-s05}

Llegamos ahora al resultado que hará posible demostrar la unicidad de la factorización.

En C14 vimos que la inferencia

$$
a\mid bc
\Longrightarrow
 a\mid b\text{ o }a\mid c
$$

es falsa para un divisor arbitrario. Por ejemplo,

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2
\qquad\text{y}\qquad
6\nmid3.
$$

Los primos, en cambio, sí poseen esa rigidez.

### Lema de Euclides

Sea $p$ un número primo. Si

$$
p\mid ab,
$$

entonces

$$
\boxed{
p\mid a
\quad\text{o}\quad
p\mid b.
}
$$

### Demostración desde C15

Si $p\mid a$, la conclusión ya está satisfecha.

Supongamos entonces que

$$
p\nmid a.
$$

Como $p$ es primo, sus únicos divisores positivos son $1$ y $p$. Todo divisor común positivo de $p$ y $a$ debe dividir a $p$, así que sólo podría ser $1$ o $p$. Pero $p$ no divide a $a$ por hipótesis. Por tanto,

$$
\gcd(p,a)=1.
$$

C15 demostró la cancelación bajo coprimalidad:

$$
\gcd(p,a)=1,
\qquad
p\mid ab
\Longrightarrow
p\mid b.
$$

Así, si $p$ no divide a $a$, necesariamente divide a $b$. En todos los casos,

$$
p\mid a\text{ o }p\mid b.
$$

### Control de dependencia

La prueba acaba de usar:

- la definición de primo;
- el MCD;
- la caracterización de coprimalidad;
- la cancelación coprima derivada de Bézout en C15.

No hemos utilizado factorización prima ni su unicidad. Esto es esencial, porque el lema de Euclides será precisamente la herramienta que usaremos para demostrar la unicidad.

Podemos resumir la nueva propiedad así:

> **Un primo no puede “aparecer” como divisor de un producto sin aparecer ya como divisor de al menos uno de sus factores.**

Esta frase será el mecanismo de comparación entre dos factorizaciones.

### Nota pedagógica — La hipótesis que permite pasar del producto al factor

La prueba de Euclides tiene un punto decisivo: si $p$ es primo y $p\nmid a$, entonces $\gcd(p,a)=1$. Para un divisor compuesto, no dividir a $a$ no excluye compartir con él un divisor no trivial. La cancelación coprima de C15 sigue siendo válida para cualquier divisor no nulo; lo que falla es deducir su hipótesis sólo a partir de la no divisibilidad.

**Control resuelto.** Tenemos $12\mid8\cdot3$, pero $12\nmid8$ y $12\nmid3$. Aquí $\gcd(12,8)=4$, no uno. En cambio, si $12\mid5b$, podemos concluir $12\mid b$ aunque doce no sea primo: $1=5\cdot5-12\cdot2$, y multiplicar por $b$ convierte la información sobre $5b$ en divisibilidad de $b$ por doce. Por ejemplo, con $b=12$, el producto es sesenta y la conclusión se verifica.

Son dos preguntas diferentes. Para garantizar la disyunción sobre cualquier producto, la primalidad resulta decisiva. Para cancelar un factor concreto dentro de una divisibilidad, basta la coprimalidad correspondiente. No debe sustituirse $\gcd(d,a)=1$ por $\gcd(a,b)=1$: seis divide a $2\cdot3$ y dos y tres son coprimos, pero seis no divide a ninguno. La hipótesis siempre debe referirse a los dos números que se pretende cancelar.

***
## 16.6. Primos que dividen productos finitos {#apm-c16-s06}

El lema de Euclides trata un producto de dos factores. Para comparar factorizaciones necesitaremos una versión para un número arbitrario de factores.

### Proposición

Sea $p$ primo y sean $a_1,\ldots,a_n\in\mathbb Z$. Si

$$
p\mid a_1a_2\cdots a_n,
$$

entonces existe algún índice $j$ con $1\le j\le n$ tal que

$$
p\mid a_j.
$$

### Demostración por inducción en $n$

Para $n=1$, la conclusión es la propia hipótesis $p\mid a_1$. Para $n=2$ es exactamente el lema de Euclides.

Supongamos el resultado verdadero para productos de $n$ factores y consideremos

$$
p\mid a_1a_2\cdots a_n a_{n+1}.
$$

Agrupamos los primeros $n$ factores:

$$
p\mid (a_1\cdots a_n)a_{n+1}.
$$

Por el lema de Euclides,

$$
p\mid a_1\cdots a_n
\qquad\text{o}\qquad
p\mid a_{n+1}.
$$

En el segundo caso terminamos. En el primero, la hipótesis inductiva implica que $p$ divide alguno de $a_1,\ldots,a_n$. Por tanto, el resultado vale para $n+1$ factores.

### Consecuencia para potencias

Si $m\ge1$ y

$$
p\mid a^m,
$$

entonces, escribiendo

$$
a^m=\underbrace{a\cdot a\cdots a}_{m\text{ factores}},
$$

la proposición anterior implica

$$
\boxed{p\mid a.}
$$

Es importante observar la dirección. Si $p\mid a$, entonces trivialmente $p\mid a^m$. La afirmación nueva es el converso bajo la hipótesis de que el divisor $p$ es primo.

Por ejemplo, $4\mid2^2$ pero $4\nmid2$. Esto muestra nuevamente que no podemos reemplazar “primo” por “entero mayor que $1$” en estas propiedades.

***
## 16.7. Existencia de la factorización prima {#apm-c16-s07}

Ya sabemos que todo entero $n>1$ tiene algún divisor primo. Ahora probaremos una afirmación más fuerte: todo entero $n>1$ puede escribirse **completamente** como producto de primos.

### Teorema de existencia

Para todo entero $n>1$, existen primos $p_1,\ldots,p_r$ tales que

$$
\boxed{n=p_1p_2\cdots p_r.}
$$

No afirmamos todavía que los $p_i$ sean únicos.

### Demostración por inducción fuerte

Sea $P(n)$ la afirmación “$n$ puede escribirse como producto finito de primos”.

**Base.** $2$ es primo, de modo que ya es un producto de un solo primo.

**Paso inductivo fuerte.** Supongamos que todo entero $m$ con

$$
2\le m<n
$$

puede escribirse como producto de primos.

Consideremos $n$.

Si $n$ es primo, la factorización está terminada:

$$
n=n.
$$

Si $n$ es compuesto, existen enteros $a,b$ con

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Por hipótesis inductiva, existen primos $p_1,\ldots,p_r$ y $q_1,\ldots,q_s$ tales que

$$
a=p_1\cdots p_r,
\qquad
b=q_1\cdots q_s.
$$

Multiplicando,

$$
n=p_1\cdots p_r q_1\cdots q_s,
$$

que es una factorización de $n$ en primos.

Por inducción fuerte, todo entero $n>1$ admite una factorización prima.

### Por qué el proceso no puede descender indefinidamente

La inducción fuerte formaliza una intuición de descenso: cada vez que un número compuesto se descompone como $n=ab$ con $a,b>1$, ambos factores son estrictamente menores que $n$. No podemos producir una cadena infinita estrictamente decreciente de enteros positivos mayores que $1$.

Así, la existencia no depende de “probar divisores hasta que funcione”. Es un teorema general.

Todavía queda abierta la pregunta más delicada:

> ¿puede un mismo entero poseer dos factorizaciones en primos realmente diferentes?

***
## 16.8. Unicidad de la factorización {#apm-c16-s08}

Supongamos que un entero $n>1$ admite dos factorizaciones primas:

$$
n=p_1p_2\cdots p_r
$$

y

$$
n=q_1q_2\cdots q_s,
$$

donde todos los $p_i$ y $q_j$ son primos.

Queremos demostrar que ambas listas contienen exactamente los mismos factores, contando repeticiones, salvo el orden.

### Primer factor

Como

$$
p_1\mid n
$$

y

$$
n=q_1q_2\cdots q_s,
$$

se tiene

$$
p_1\mid q_1q_2\cdots q_s.
$$

Por la versión finita del lema de Euclides, $p_1$ divide a alguno de los factores $q_j$.

Pero $q_j$ es primo. Sus únicos divisores positivos son $1$ y $q_j$. Como $p_1>1$, concluimos

$$
p_1=q_j.
$$

Reordenando la segunda factorización podemos suponer $q_j=q_1$. Entonces

$$
p_1p_2\cdots p_r=p_1q_2\cdots q_s.
$$

Como $p_1\ne0$, cancelamos en la igualdad de enteros y obtenemos

$$
p_2\cdots p_r=q_2\cdots q_s.
$$

### Repetición del argumento

Aplicamos el mismo razonamiento a $p_2$. Debe coincidir con alguno de los primos restantes del lado derecho. Reordenamos y cancelamos otra vez.

El proceso continúa. Como las factorizaciones contienen un número finito de factores, no puede continuar indefinidamente.

Si una lista se agotara antes que la otra, terminaríamos con una igualdad de la forma

$$
1=q_{k}q_{k+1}\cdots q_s,
$$

imposible porque cada $q_j>1$. Por tanto,

$$
r=s,
$$

y, tras una reordenación,

$$
p_i=q_i
$$

para todo $i$.

Hemos demostrado:

### Teorema de unicidad

Toda factorización de un entero $n>1$ como producto de primos es única salvo el orden de los factores.

### Dónde se usó cada hipótesis

La prueba depende de tres puntos concretos:

1. **primalidad de $p_1$**, para aplicar el lema de Euclides al producto;
2. **primalidad de $q_j$**, para pasar de $p_1\mid q_j$ a $p_1=q_j$;
3. **finitud de las listas**, para que la cancelación repetida termine.

Sin el lema de Euclides no dispondríamos del paso que fuerza a un primo de una factorización a aparecer en la otra.

### Nota pedagógica — Qué queda después de cada cancelación

Al comparar dos listas de primos, conserva como invariante la igualdad entre los productos restantes. El lema de Euclides localiza un primo igual en la otra lista; reordenar no cambia el producto, y cancelar el factor común no nulo conserva la igualdad. Cada paso retira una entrada de cada lista, incluidas las repeticiones. No estamos cancelando factores distintos sólo porque ambos sean primos.

**Control resuelto.** Compara $2\cdot2\cdot3\cdot7$ con $7\cdot3\cdot2\cdot2$. Localiza el primer dos, colócalo delante en la segunda lista y cancela; quedan $2\cdot3\cdot7=7\cdot3\cdot2$. Repite con el segundo dos, luego con tres y siete. Al final queda $1=1$: el producto vacío se interpreta como uno. No se ha perdido la multiplicidad del dos.

Si una lista se agotara mientras la otra conserva $h\ge1$ primos, la igualdad restante sería $1=q_1\cdots q_h$. Cada factor es al menos dos, así que el producto es al menos $2^h>1$. Esta contradicción prueba que las longitudes coinciden; la finitud sólo asegura que podemos llegar a ese punto. El mismo cierre vale si la primera lista se vacía antes que la segunda o a la inversa.

La igualdad $6\cdot35=10\cdot21$ muestra por qué no se aplica este procedimiento a listas de factores compuestos: ningún factor de la primera lista coincide con uno de la segunda. Hay que llegar a primos antes de invocar la comparación uno a uno. La cancelación ordinaria en una igualdad requiere un factor común no nulo, mientras la localización de ese factor utiliza primalidad.

***
## 16.9. Teorema fundamental de la aritmética y forma canónica {#apm-c16-s09}

Podemos reunir los dos resultados anteriores.

### Teorema fundamental de la aritmética

Todo entero $n>1$ puede escribirse como producto de números primos, y esa factorización es única salvo el orden de los factores.

En lugar de repetir factores, agrupamos los iguales. Si los primos distintos que aparecen son

$$
p_1<p_2<\cdots<p_r,
$$

podemos escribir de manera canónica

$$
\boxed{
n=p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_r^{\alpha_r},
\qquad
\alpha_i\ge1.
}
$$

Por ejemplo,

$$
756=2^2\cdot3^3\cdot7.
$$

La forma canónica contiene más información que una simple lista de divisores: registra exactamente **qué primos aparecen** y **con qué multiplicidad**.

### Enteros negativos

Si $n<-1$, factorizamos $|n|$ y separamos la unidad $-1$:

$$
n=-p_1^{\alpha_1}\cdots p_r^{\alpha_r}.
$$

La única ambigüedad de signo queda absorbida por la unidad.

### Los casos $1$, $-1$ y $0$

- $1$ no tiene factores primos; cuando sea útil puede entenderse como producto vacío.
- $-1$ es una unidad y tampoco posee factores primos.
- $0$ no tiene factorización prima: cualquier primo divide a $0$, y no existe una lista finita canónica de primos que desempeñe el papel anterior.

La unicidad de la factorización transforma desde ahora muchas preguntas multiplicativas en preguntas sobre exponentes. Éste será el siguiente paso estructural.

***
## 16.10. Divisibilidad como comparación de exponentes {#apm-c16-s10}

Sean $a,b>0$. Para compararlos mediante sus factorizaciones, escribimos ambos usando una misma colección de primos. Permitimos exponente $0$ cuando un primo no aparece.

Así podemos representar

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p},
$$

donde sólo finitos exponentes son distintos de $0$.

No estamos introduciendo una nueva teoría ni una notación de valuaciones; simplemente estamos organizando las factorizaciones canónicas.

### Teorema

Para $a,b>0$,

$$
\boxed{
a\mid b
\iff
\alpha_p\le\beta_p
\quad\text{para todo primo }p.
}
$$

### Demostración

Supongamos primero que

$$
\alpha_p\le\beta_p
$$

para todo primo $p$. Entonces cada diferencia $\beta_p-\alpha_p$ es un entero no negativo. Definimos

$$
c=\prod_p p^{\beta_p-\alpha_p}.
$$

Por las leyes de los exponentes,

$$
ac
=
\prod_p p^{\alpha_p}
\prod_p p^{\beta_p-\alpha_p}
=
\prod_p p^{\beta_p}
=b.
$$

Por tanto, $a\mid b$.

Recíprocamente, supongamos que $a\mid b$. Entonces existe $c>0$ tal que

$$
b=ac.
$$

Factorizamos también $c$:

$$
c=\prod_p p^{\gamma_p}.
$$

Así,

$$
b=ac=\prod_p p^{\alpha_p+\gamma_p}.
$$

Por unicidad de la factorización,

$$
\beta_p=\alpha_p+\gamma_p
$$

para todo primo $p$. Como $\gamma_p\ge0$,

$$
\alpha_p\le\beta_p.
$$

### Ejemplo

Consideremos

$$
72=2^3\cdot3^2
$$

y

$$
540=2^2\cdot3^3\cdot5.
$$

Como el exponente de $2$ en $72$ es $3$ y en $540$ es $2$, no puede ocurrir

$$
72\mid540.
$$

No fue necesario efectuar una división: la comparación de exponentes ya contiene la respuesta.

***
## 16.11. MCD, MCM y coprimalidad desde la factorización {#apm-c16-s11}

La aritmética de exponentes permite releer conceptos de C15 desde una perspectiva nueva.

Sean

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p},
$$

con $a,b>0$.

### MCD: tomar mínimos

Un divisor común $d$ de $a$ y $b$ debe tener, para cada primo $p$, un exponente que no supere ni $\alpha_p$ ni $\beta_p$. El mayor exponente posible compatible con ambas restricciones es

$$
\min(\alpha_p,\beta_p).
$$

Por tanto,

$$
\boxed{
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)}.
}
$$

Esta fórmula satisface exactamente la caracterización universal de C15: el número construido divide a $a$ y a $b$, y cualquier divisor común tiene, primo por primo, exponentes no mayores que esos mínimos; por ello divide al número construido.

### MCM: tomar máximos

Definimos el **mínimo común múltiplo** de $a$ y $b$, denotado

$$
\operatorname{lcm}(a,b),
$$

como el menor entero positivo que es múltiplo de ambos.

Para que un número sea múltiplo de $a$ y de $b$, el exponente de cada primo debe ser al menos $\alpha_p$ y al menos $\beta_p$. El menor exponente que satisface ambas condiciones es

$$
\max(\alpha_p,\beta_p).
$$

Así,

$$
\boxed{
\operatorname{lcm}(a,b)
=
\prod_p p^{\max(\alpha_p,\beta_p)}.
}
$$

El número construido es múltiplo de $a$ y de $b$. Además, si $m>0$ es cualquier múltiplo común, sus exponentes primos deben ser al menos $\alpha_p$ y al menos $\beta_p$, y por tanto al menos $\max(\alpha_p,\beta_p)$. De aquí que $\operatorname{lcm}(a,b)\mid m$; como ambos son positivos, también $\operatorname{lcm}(a,b)\le m$. Esto justifica realmente el calificativo “mínimo”.

### Relación entre MCD y MCM

Para cualesquiera enteros no negativos $r,s$,

$$
\min(r,s)+\max(r,s)=r+s.
$$

Aplicando esta identidad primo por primo,

$$
\gcd(a,b)\operatorname{lcm}(a,b)
=
\prod_p p^{\alpha_p+\beta_p}
=ab.
$$

Por tanto,

$$
\boxed{
\gcd(a,b)\operatorname{lcm}(a,b)=ab
}
$$

para $a,b>0$.

### Coprimalidad

También obtenemos:

$$
\boxed{
\gcd(a,b)=1
\iff
\text{$a$ y $b$ no comparten ningún factor primo.}
}
$$

En efecto, el MCD es $1$ exactamente cuando

$$
\min(\alpha_p,\beta_p)=0
$$

para todo primo $p$.

Esta descripción no reemplaza al algoritmo de Euclides. Para números grandes, factorizar puede ser mucho más difícil que calcular un MCD mediante Euclides. Lo que ganamos aquí no es necesariamente eficiencia computacional, sino una descripción estructural distinta.

***
## 16.12. Cómo reconocer un primo: la barrera $\sqrt n$ {#apm-c16-s12}

La definición de primo parece exigir revisar todos los divisores entre $2$ y $n-1$. Podemos reducir drásticamente esa búsqueda.

### Teorema

Si $n>1$ es compuesto, entonces posee un divisor primo $p$ tal que

$$
\boxed{p\le\sqrt n.}
$$

### Demostración

Como $n$ es compuesto, existen enteros $a,b$ con

$$
n=ab,
\qquad
1<a\le b<n.
$$

Podemos suponer $a\le b$ intercambiando los factores si es necesario. Entonces

$$
a^2\le ab=n,
$$

de donde

$$
a\le\sqrt n.
$$

Por el teorema de la sección 16.4, el entero $a>1$ posee un divisor primo $p$. Por tanto,

$$
p\le a\le\sqrt n,
$$

y, como $p\mid a$ y $a\mid n$,

$$
p\mid n.
$$

### Criterio práctico

Para demostrar que un entero $n>1$ es primo basta comprobar que ningún primo

$$
p\le\sqrt n
$$

lo divide.

Por ejemplo, para decidir si $97$ es primo observamos que

$$
\sqrt{97}<10.
$$

Sólo necesitamos probar divisibilidad por los primos menores que $10$:

$$
2,3,5,7.
$$

Ninguno divide a $97$, de modo que $97$ es primo.

El criterio no afirma que debamos factorizar $n$ completamente. Basta descartar divisores primos hasta la raíz cuadrada.

***
## 16.13. Existen infinitos números primos {#apm-c16-s13}

Los primos no forman una lista finita. La demostración clásica de Euclides es un modelo notable de argumento por contradicción y construcción.

### Teorema

Existen infinitos números primos.

### Demostración

Supongamos, por contradicción, que sólo existen finitos primos. Los enumeramos:

$$
p_1,p_2,\ldots,p_k.
$$

Construimos el entero

$$
N=p_1p_2\cdots p_k+1.
$$

Como $N>1$, la sección 16.4 garantiza que $N$ posee algún divisor primo $q$.

Bajo nuestra suposición, $q$ debe ser uno de los primos de la lista, digamos

$$
q=p_j.
$$

Entonces $q$ divide el producto

$$
p_1p_2\cdots p_k.
$$

También divide a $N$. Por cierre de la divisibilidad bajo diferencias, tendría que dividir

$$
N-p_1p_2\cdots p_k=1.
$$

Pero ningún primo divide a $1$. Contradicción.

Por tanto, la lista de primos no puede ser finita.

### El error que debemos evitar

La prueba **no** demuestra que

$$
N=p_1p_2\cdots p_k+1
$$

sea primo.

Puede ser primo o compuesto. Lo único necesario es que $N>1$ tenga **algún divisor primo** $q$, y que ese divisor no pueda pertenecer a la lista inicial.

Por ejemplo, si tomamos algunos primos y construimos un número del tipo producto más uno, el resultado puede descomponerse. La fuerza del argumento no depende de la primalidad de $N$, sino de la existencia de un divisor primo nuevo.

Esta precisión lógica distingue la demostración correcta de una versión frecuente pero injustificada del argumento.

***
## 16.14. Potencias perfectas y consecuencias de la unicidad {#apm-c16-s14}

La factorización única permite reconocer potencias perfectas mirando únicamente los exponentes.

Sea

$$
n=\prod_p p^{\alpha_p}>0.
$$

### Cuadrados perfectos

Si $n=m^2$ y

$$
m=\prod_p p^{\beta_p},
$$

entonces

$$
n=m^2=\prod_p p^{2\beta_p}.
$$

Por unicidad,

$$
\alpha_p=2\beta_p
$$

para todo primo $p$. Por tanto, todos los exponentes de $n$ son pares.

Recíprocamente, si todos los exponentes $\alpha_p$ son pares, escribimos

$$
\alpha_p=2\beta_p
$$

y obtenemos

$$
n=
\prod_p p^{2\beta_p}
=
\left(\prod_p p^{\beta_p}\right)^2.
$$

Así,

$$
\boxed{
n\text{ es cuadrado perfecto}
\iff
\alpha_p\text{ es par para todo }p.
}
$$

### Cubos y $k$-ésimas potencias

El mismo argumento produce

$$
\boxed{
n\text{ es cubo perfecto}
\iff
3\mid\alpha_p\text{ para todo }p.
}
$$

Más generalmente, para $k\ge2$,

$$
\boxed{
n\text{ es una }k\text{-ésima potencia perfecta}
\iff
k\mid\alpha_p\text{ para todo primo }p.
}
$$

### Un producto coprimo que es cuadrado

Sean $a,b>0$. Supongamos que

$$
\gcd(a,b)=1
$$

y que $ab$ es un cuadrado perfecto.

Como $a$ y $b$ no comparten factores primos, los exponentes de cada primo en $ab$ proceden enteramente de uno de los dos factores. Si todos los exponentes de $ab$ son pares, entonces los exponentes que aparecen en $a$ son pares y los que aparecen en $b$ también son pares. Por tanto, $a$ y $b$ son cuadrados perfectos.

La coprimalidad es esencial. Por ejemplo,

$$
2\cdot8=16
$$

es un cuadrado perfecto, pero ni $2$ ni $8$ es cuadrado.

Este tipo de argumento muestra la potencia de la unicidad: una igualdad multiplicativa se convierte en una condición componente a componente sobre exponentes.

### Nota pedagógica — Un certificado de potencia necesita todas las componentes

Para $N>0$ y $k\ge2$, comprobar que cada exponente primo de $N$ es múltiplo de $k$ permite construir una raíz entera positiva: se dividen los exponentes por $k$ y se multiplican las potencias resultantes. El converso utiliza unicidad para identificar esos exponentes con los de una raíz elevada a $k$. La suma de los exponentes o el tamaño del número no sustituyen el control primo por primo.

**Control resuelto.** Para $N=2^6\cdot3^9$, ambos exponentes son múltiplos de tres y $N=(2^2\cdot3^3)^3=108^3$. No es cuadrado, porque nueve es impar; seis par no compensa esa falla. Tampoco es sexta potencia, porque nueve no es múltiplo de seis. Para $N=1$, todos los exponentes son cero y $1=1^k$ para cualquier $k\ge2$.

La condición $N>0$ fija el dominio del criterio expuesto. Para un entero negativo se deben controlar por separado el signo y los exponentes de su valor absoluto: $-64=(-4)^3$, pero no es cuadrado de un entero, aunque $64$ tenga exponente primo par. Cero tampoco tiene la factorización prima utilizada aquí, aunque $0=0^k$.

Al separar un producto coprimo que es cuadrado, también se exige que sus factores sean positivos. La coprimalidad evita que un primo reparta exponentes entre ellos; no controla sus signos. El ejemplo $(-1)(-1)=1$ tiene factores coprimos y producto cuadrado, pero ninguno de esos factores es cuadrado entero. La comprobación de dominio precede a la comparación de exponentes.

***
## 16.15. Diagnóstico: qué depende de ser primo y qué depende de factorización única {#apm-c16-s15}

A esta altura conviene separar propiedades que pueden parecer similares pero tienen fundamentos distintos.

### Afirmación 1

$$
p\mid ab
\Longrightarrow
p\mid a\text{ o }p\mid b.
$$

Es verdadera cuando $p$ es primo. Su prueba depende de Bézout y coprimalidad, no de la factorización única.

Si eliminamos la primalidad, falla. Ya vimos:

$$
6\mid2\cdot3,
$$

pero $6$ no divide a ninguno de los factores.

### Afirmación 2

$$
p\mid a^m
\Longrightarrow
p\mid a.
$$

También depende de que $p$ sea primo; se obtiene aplicando repetidamente el lema de Euclides.

### Afirmación 3

“Si $a\mid b$, entonces cada exponente primo de $a$ es menor o igual que el correspondiente exponente primo de $b$.”

Esta afirmación depende de la **unicidad de la factorización**. Antes de demostrar el teorema fundamental no teníamos derecho a comparar exponentes de esa manera.

### Afirmación 4

Para $a,b>0$, consideramos la afirmación siguiente.

“Si $ab$ es cuadrado, entonces $a$ y $b$ son cuadrados.”

Es falsa sin hipótesis adicionales:

$$
2\cdot8=16.
$$

Se vuelve verdadera si añadimos

$$
\gcd(a,b)=1.
$$

La razón no es una regla aislada, sino la ausencia de primos compartidos y la paridad de los exponentes en la factorización única.

### Afirmación 5

“Si $p_1,\ldots,p_k$ son primos, entonces $p_1\cdots p_k+1$ es primo.”

Es falsa en general. En la prueba de infinitud sólo necesitamos que el número construido tenga un divisor primo que no esté en la lista.

### Protocolo de diagnóstico

Ante una afirmación multiplicativa, conviene preguntar:

```text
¿EL DIVISOR ES PRIMO?
        ↓
¿SE QUIERE USAR EL LEMA DE EUCLIDES?
        ↓
¿LA AFIRMACIÓN HABLA DE EXPONENTES DE FACTORES PRIMOS?
        ↓
ENTONCES DEBE HABERSE ESTABLECIDO UNICIDAD
        ↓
¿APARECE UN PRODUCTO DE FACTORES COPRIMOS?
        ↓
SEPARAR LOS PRIMOS QUE PUEDEN APARECER EN CADA FACTOR
        ↓
¿SE AFIRMA QUE PRODUCTO + 1 ES PRIMO?
        ↓
NO: SÓLO SE GARANTIZA LA EXISTENCIA DE UN DIVISOR PRIMO
```

La disciplina principal consiste en identificar **qué teorema autoriza cada paso**.

***
## 16.16. Cierre — protocolo de factorización y puente hacia congruencias {#apm-c16-s16}

El capítulo comenzó preguntando cuáles son los bloques multiplicativos elementales de los enteros. La respuesta no es simplemente “los primos”, sino una cadena de resultados que explica por qué los primos cumplen ese papel.

Primero distinguimos unidades, primos, compuestos e irreducibles. Después probamos que todo entero mayor que $1$ tiene un divisor primo. A partir de Bézout y la cancelación coprima de C15 demostramos el lema de Euclides:

$$
p\mid ab
\Longrightarrow
p\mid a\text{ o }p\mid b.
$$

Luego separamos las dos mitades del teorema fundamental:

$$
\text{existencia de factorización}
\qquad\text{y}\qquad
\text{unicidad de factorización}.
$$

La cadena completa es:

```text
PRIMOS Y COMPUESTOS
        ↓
UNIDADES E IRREDUCIBLES
        ↓
DIVISOR PRIMO DE TODO n>1
        ↓
BÉZOUT + COPRIMALIDAD
        ↓
LEMA DE EUCLIDES
        ↓
PRODUCTOS FINITOS
        ↓
UNICIDAD DE FACTORIZACIÓN

EXISTENCIA DE FACTORIZACIÓN: INDUCCIÓN FUERTE, EN UNA RAMA INDEPENDIENTE
EXISTENCIA + UNICIDAD
        ↓
TEOREMA FUNDAMENTAL DE LA ARITMÉTICA
        ↓
EXPONENTES PRIMOS
        ↓
DIVISIBILIDAD / MCD / MCM
        ↓
PRIMALIDAD HASTA sqrt(n)
        ↓
INFINITUD DE LOS PRIMOS
        ↓
POTENCIAS PERFECTAS
```

Ante un nuevo problema de esta clase, podemos aplicar el siguiente protocolo:

```text
1. IDENTIFICAR SI EL ENTERO ES PRIMO, COMPUESTO O UNA UNIDAD.
2. SI SE TRATA DE UN PRODUCTO DIVISIBLE POR UN PRIMO, CONSIDERAR EL LEMA DE EUCLIDES.
3. SI APARECEN VARIOS FACTORES, EXTENDER EL LEMA POR INDUCCIÓN.
4. SI SE NECESITA FACTORIZAR TEÓRICAMENTE, SEPARAR EXISTENCIA DE UNICIDAD.
5. PARA COMPARAR DIVISIBILIDAD DESPUÉS DEL TFA, COMPARAR EXPONENTES PRIMO A PRIMO.
6. PARA MCD Y MCM, TOMAR RESPECTIVAMENTE MÍNIMOS Y MÁXIMOS DE EXPONENTES.
7. PARA PROBAR PRIMALIDAD, BASTA DESCARTAR DIVISORES PRIMOS HASTA sqrt(n).
8. EN LA PRUEBA DE INFINITUD, NO SUPONER QUE EL PRODUCTO + 1 ES PRIMO.
9. PARA POTENCIAS PERFECTAS, TRADUCIR LA CONDICIÓN A DIVISIBILIDAD DE EXPONENTES.
10. AUDITAR SI CADA PASO DEPENDE DE PRIMALIDAD, COPRIMALIDAD O UNICIDAD.
```

Hemos aprendido a describir un entero mediante sus factores primos. Pero todavía hay otra manera de organizar la aritmética: en lugar de preguntar **qué factores contiene un entero**, podemos preguntar cuándo dos enteros deben considerarse equivalentes porque dejan la misma diferencia respecto de un múltiplo fijo.

Esa pregunta conducirá al capítulo 17, donde estudiaremos **congruencias y aritmética modular**. Allí la divisibilidad reaparecerá con una forma nueva: no como descomposición multiplicativa, sino como criterio para comparar enteros dentro de clases de equivalencia.

***
# Ejercicios

Los ejercicios están organizados para pasar de la identificación elemental de primos y compuestos a la comprensión estructural del teorema fundamental de la aritmética y sus consecuencias. En todo el banco se mantiene la convención de que “primo” significa primo positivo mayor que $1$. Los ejercicios no requieren congruencias, inversos modulares ni resultados de C17.

## A. Primos, compuestos, unidades e irreducibles


**1.** **Nivel A.** Clasifica cada entero de la lista como **unidad**, **primo**, **compuesto** o **ninguna de esas categorías** según las convenciones de C16:
$$
-17,-1,0,1,2,15,37,49.
$$
Justifica los casos $-17$, $0$ y $1$ sin limitarte a citar la lista de definiciones.


**2.** **Nivel A.** Determina cuáles de los siguientes enteros positivos son primos y cuáles compuestos. Para cada compuesto exhibe una factorización no trivial; para cada primo explica por qué no basta con “no haber encontrado” un divisor:
$$
29,35,51,67,77,91.
$$


**3.** **Nivel B.** Demuestra que las únicas unidades de $\mathbb Z$ son $1$ y $-1$. Parte de la ecuación
$$
uv=1
$$
con $u,v\in\mathbb Z$ y usa valores absolutos.


**4.** **Nivel B.** Explica por qué $1$ no debe ser primo si queremos que la factorización en primos tenga una formulación de unicidad razonable. Construye explícitamente una familia infinita de “factorizaciones” de $30$ que aparecería si $1$ fuese admitido como primo.


**5.** **Nivel C.** Sea $p>1$ primo. Demuestra que $-p$ es irreducible en $\mathbb Z$. Explica por qué, bajo la convención del capítulo, esto no obliga a llamar “primo” a $-p$.


**6.** **Nivel C.** Decide si cada una de las siguientes afirmaciones es verdadera o falsa. Demuestra las verdaderas y da un contraejemplo para las falsas.

a) Todo irreducible de $\mathbb Z$ es positivo.

b) Si $a$ es irreducible, entonces $-a$ es irreducible.

c) Todo primo positivo es irreducible en $\mathbb Z$.

d) Toda unidad es irreducible.


**7.** **Nivel C.** Sea $n>1$. Demuestra que son equivalentes:

- $n$ es compuesto;
- existen enteros positivos $a,b$ tales que $n=ab$ y $1<a,b<n$;
- $n$ posee un divisor positivo $d$ con $1<d<n$.


**8.** **Nivel D.** Un estudiante afirma: “un entero $a$ es irreducible si sólo puede escribirse como $a=1\cdot a$”. Diagnostica qué falta en esa frase cuando se trabaja en $\mathbb Z$. Formula una caracterización correcta que contemple signos y unidades, y úsala para analizar $7$ y $-7$.

## B. Divisores primos y descenso


**9.** **Nivel A.** Para cada entero, encuentra al menos un divisor primo y explica cómo verificas que el divisor elegido es efectivamente primo:
$$
84,143,221,391.
$$


**10.** **Nivel B.** Demuestra directamente que si $n>1$ es compuesto, entonces posee un divisor $d$ con
$$
1<d<n.
$$
Explica por qué este hecho es el descenso que hace posible una prueba por inducción fuerte.


**11.** **Nivel C.** Prueba por inducción fuerte que todo entero $n>1$ tiene un divisor primo. Tu demostración debe separar los casos “$n$ primo” y “$n$ compuesto” y señalar exactamente dónde se aplica la hipótesis inductiva.


**12.** **Nivel C.** Da una segunda prueba del ejercicio anterior mediante **mínimo contraejemplo**: supone que existe algún entero mayor que $1$ sin divisor primo, elige el menor y deriva una contradicción.


**13.** **Nivel C.** Sea $n>1$ y sea $d>1$ el menor divisor positivo de $n$ mayor que $1$. Demuestra que $d$ es primo. No uses todavía factorización única.


**14.** **Nivel C.** Supón que $n=ab$ con $a,b>1$. Demuestra que cualquier divisor primo de $a$ es también divisor primo de $n$. Usa el resultado para explicar por qué factorizar parcialmente un entero compuesto siempre permite encontrar algún primo que lo divide.


**15.** **Nivel D.** Considera el siguiente argumento: “si $n>1$ no es primo, entonces $n=ab$ con $1<a,b<n$; como $a<n$, podemos repetir indefinidamente la descomposición y eventualmente aparecerá un primo”. Explica por qué “repetir indefinidamente” no es una justificación. Reescribe el argumento como una prueba válida usando inducción fuerte o buen orden.


**16.** **Nivel D.** Sea $S$ un conjunto no vacío de enteros mayores que $1$ cerrado hacia divisores no triviales en el siguiente sentido: si $n\in S$ es compuesto, existe un divisor $d\in S$ con $1<d<n$. Demuestra que $S$ contiene un primo. Identifica el principio lógico utilizado.

## C. Lema de Euclides


**17.** **Nivel B.** Sea $p$ primo y $a\in\mathbb Z$. Demuestra que exactamente una de las siguientes situaciones puede ocurrir:
$$
p\mid a
$$
o
$$
\gcd(p,a)=1.
$$
Justifica el resultado usando sólo la definición de primo y el MCD de C15.


**18.** **Nivel C.** Demuestra el lema de Euclides a partir de la cancelación coprima de C15:
$$
p\text{ primo},\qquad p\mid ab
\Longrightarrow
p\mid a\text{ o }p\mid b.
$$
Tu prueba no puede usar factorización prima ni el teorema fundamental de la aritmética.


**19.** **Nivel C.** Da un contraejemplo a cada generalización falsa:

a) si $d>1$ y $d\mid ab$, entonces $d\mid a$ o $d\mid b$;

b) si $d$ es compuesto y $d\mid a^2$, entonces $d\mid a$.

Explica qué propiedad especial de los primos falta.


**20.** **Nivel C.** Sea $p$ primo. Si $p\mid a$ y $p\mid(a+b)$, demuestra que $p\mid b$. Después explica por qué este ejercicio usa sólo propiedades básicas de divisibilidad y no necesita el lema de Euclides.


**21.** **Nivel C.** Sea $p$ primo y supón que
$$
p\mid ab,
\qquad
p\nmid a.
$$
Demuestra que $p\mid b$ escribiendo explícitamente una identidad de Bézout para $p$ y $a$ y multiplicándola por $b$.


**22.** **Nivel D.** Sea $p$ primo y sean $a,b,c\in\mathbb Z$. Demuestra que
$$
p\mid abc,
\qquad
p\nmid a,
\qquad
p\nmid b
\Longrightarrow
p\mid c.
$$
Haz explícito en qué orden aplicas el lema de Euclides.


**23.** **Nivel D.** Supón que $p$ y $q$ son primos distintos. Demuestra que
$$
p\nmid q
$$
y que
$$
\gcd(p,q)=1.
$$
Luego, si $pq\mid ab$ y $p\nmid b$, demuestra que $p\mid a$. ¿Puede deducirse necesariamente $q\mid a$? Justifica tu respuesta sin usar factorización única.


**24.** **Nivel D.** Audita la prueba falsa: “si $6\mid ab$, entonces como $6=2\cdot3$ y $2,3$ son primos, el lema de Euclides implica $6\mid a$ o $6\mid b$”. Localiza exactamente el salto inválido y da un ejemplo que lo refute.

## D. Productos finitos y potencias


**25.** **Nivel C.** Demuestra por inducción que si $p$ es primo y
$$
p\mid a_1a_2\cdots a_n,
$$
entonces $p$ divide al menos uno de los factores $a_j$.


**26.** **Nivel C.** Sea $p$ primo y $m\ge1$. Demuestra
$$
p\mid a^m
\Longrightarrow
p\mid a.
$$
Indica con precisión qué resultado previo se aplica al producto de $m$ copias de $a$.


**27.** **Nivel C.** Sean $p$ primo y $a,b\in\mathbb Z$. Demuestra que si
$$
p\mid a^3b^2,
$$
entonces $p\mid a$ o $p\mid b$. Después explica por qué la conclusión no dice cuál de los dos factores debe ser divisible por $p$.


**28.** **Nivel D.** Sean $p_1,\ldots,p_r$ primos y sea $a\in\mathbb Z$. Demuestra que si
$$
p_1p_2\cdots p_r\mid a
$$
y los $p_i$ son distintos, entonces cada $p_i\mid a$. ¿Necesitas el lema de Euclides para esta dirección? Justifica.


**29.** **Nivel D.** Sean $p$ y $q$ primos distintos. Demuestra que si
$$
p^2q^3\mid a^5,
$$
entonces $p\mid a$ y $q\mid a$. No uses todavía comparación sistemática de exponentes de factorización prima.


**30.** **Nivel D.** Sea $p$ primo. Demuestra que si
$$
p\mid a_1^2a_2^2\cdots a_n^2,
$$
entonces $p$ divide alguno de los $a_j$. Tu argumento debe combinar la versión finita del lema de Euclides con el caso de potencias.


**31.** **Nivel D.** Decide si es verdadero o falso:
$$
p\mid a^m b^n
\Longrightarrow
p\mid ab
$$
para $p$ primo y $m,n\ge1$. Si es verdadero, demuéstralo sin usar el teorema fundamental de la aritmética.


**32.** **Nivel D.** Sea $p$ primo y supón que $p\nmid a_i$ para $i=1,\ldots,n$. Demuestra que
$$
p\nmid a_1a_2\cdots a_n.
$$
Formula la prueba como contraposición de un teorema ya establecido.

## E. Existencia y unicidad de factorización


**33.** **Nivel C.** Factoriza completamente en primos:
$$
756,
\qquad
1386,
\qquad
2310.
$$
Escribe cada resultado en forma canónica con primos crecientes y exponentes positivos.


**34.** **Nivel C.** Construye dos árboles de factorización distintos para $360$ que comiencen con descomposiciones no triviales diferentes. Lleva ambos hasta primos y compara los factores finales. Explica qué parte del teorema fundamental interpreta esta coincidencia.


**35.** **Nivel D.** Demuestra por inducción fuerte que todo entero $n>1$ puede escribirse como producto finito de primos. No utilices unicidad en ningún paso.


**36.** **Nivel D.** Da una prueba alternativa de la existencia de factorización mediante mínimo contraejemplo. Debes justificar por qué un supuesto contraejemplo mínimo no puede ser primo ni compuesto.


**37.** **Nivel E.** Supón
$$
n=p_1p_2\cdots p_r=q_1q_2\cdots q_s
$$
con todos los factores primos. Demuestra que $p_1$ coincide con alguno de los $q_j$. Señala exactamente dónde se usa el lema de Euclides y dónde se usa la primalidad de $q_j$.


**38.** **Nivel E.** Completa la prueba de unicidad de la factorización: a partir del ejercicio anterior, reordena, cancela y repite el argumento. Demuestra además que una lista de factores no puede agotarse antes que la otra.


**39.** **Nivel D.** Explica por qué la afirmación “todo entero $n>1$ tiene un divisor primo” no basta por sí sola para establecer el teorema fundamental de la aritmética. Distingue claramente las tres afirmaciones: existencia de un divisor primo, existencia de una factorización completa y unicidad.


**40.** **Nivel E.** Audita la siguiente prueba circular: “la factorización es única porque si un primo divide un producto debe dividir un factor; esto último es evidente porque en la factorización prima del producto el primo tiene que aparecer en uno de los factores”. Explica la circularidad y reconstruye el orden correcto de dependencias desde C15.

## F. Forma canónica y divisibilidad por exponentes


**41.** **Nivel B.** Escribe en forma canónica las factorizaciones de
$$
900,
\qquad
13860,
\qquad
-1260.
$$
Separa explícitamente la unidad $-1$ en el caso negativo.


**42.** **Nivel C.** Sean
$$
a=2^3 3^2 5,
\qquad
b=2^5 3^2 5^4 7.
$$
Decide si $a\mid b$, $b\mid a$, $2^4 3^2 5\mid b$ y $2^5 3^3\mid b$. Justifica cada respuesta comparando exponentes.


**43.** **Nivel D.** Demuestra el criterio de divisibilidad por exponentes. Si
$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p},
$$
demuestra que
$$
a\mid b
\iff
\alpha_p\le\beta_p
$$
para todo primo $p$. Identifica dónde se usa unicidad de factorización en la implicación no trivial.


**44.** **Nivel C.** Encuentra todos los divisores positivos de
$$
72=2^3 3^2
$$
usando únicamente las posibilidades para los exponentes de $2$ y $3$. Después cuenta cuántos divisores positivos tiene $72$.


**45.** **Nivel D.** Sea
$$
n=p_1^{\alpha_1}\cdots p_r^{\alpha_r}.
$$
Demuestra que todo divisor positivo $d$ de $n$ tiene la forma
$$
d=p_1^{\beta_1}\cdots p_r^{\beta_r},
\qquad
0\le\beta_i\le\alpha_i.
$$
Demuestra también el converso.


**46.** **Nivel D.** Si
$$
a\mid b
\qquad\text{y}\qquad
b\mid a
$$
para $a,b>0$, demuestra nuevamente que $a=b$, pero esta vez usando las factorizaciones primas y la comparación de exponentes. Compara esta prueba con la de C14 basada en tamaño.


**47.** **Nivel D.** Sea $a>0$. Demuestra que
$$
a\mid a^m
$$
para todo $m\ge1$ mediante exponentes primos. Luego determina para qué $m\ge1$ se cumple
$$
a^m\mid a
$$
cuando $a>1$.


**48.** **Nivel E.** Sean $a,b,c>0$ y supón
$$
a\mid bc,
\qquad
\gcd(a,b)=1.
$$
Reprueba que $a\mid c$ usando factorización prima y exponentes. Después explica en qué sentido esta demostración es posterior y estructuralmente distinta de la prueba de C15 mediante Bézout.

## G. MCD, MCM y factorización


**49.** **Nivel B.** Usando factorización prima, calcula el MCD y el MCM de cada par:
$$
(360,840),
\qquad
(756,630),
\qquad
(1001,1430).
$$


**50.** **Nivel C.** Sean
$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$
Demuestra que
$$
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)}.
$$
Tu prueba debe justificar que el entero de la derecha es divisor común y que todo divisor común lo divide.


**51.** **Nivel C.** Define el MCM positivo mediante exponentes máximos y demuestra que
$$
\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$
Verifica explícitamente la propiedad universal correspondiente a “múltiplo común mínimo” en términos de divisibilidad.


**52.** **Nivel D.** Demuestra para $a,b>0$ que
$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab
$$
usando la identidad
$$
\min(r,s)+\max(r,s)=r+s
$$
para cada exponente primo.


**53.** **Nivel C.** Demuestra que
$$
\gcd(a,b)=1
$$
si y sólo si no existe ningún primo que divida simultáneamente a $a$ y a $b$, para $a,b>0$.


**54.** **Nivel D.** Supón $a,b>0$ y $\gcd(a,b)=1$. Demuestra
$$
\operatorname{lcm}(a,b)=ab.
$$
Da después un ejemplo con $\gcd(a,b)>1$ donde el producto $ab$ no sea el MCM.


**55.** **Nivel D.** Si $a\mid b$, demuestra que
$$
\gcd(a,b)=a
\qquad\text{y}\qquad
\operatorname{lcm}(a,b)=b
$$
para $a,b>0$, usando exponentes. Explica cómo esta afirmación refleja el orden de divisibilidad.


**56.** **Nivel E.** Sean $a,b>0$. Demuestra que todo primo que divide a $ab$ divide a $\operatorname{lcm}(a,b)$, y que todo primo que divide al MCD divide a ambos. Reformula ambas afirmaciones en términos de exponentes y explica por qué una no es simplemente el converso de la otra.

## H. Primalidad e infinitud de los primos


**57.** **Nivel C.** Demuestra que si $n>1$ es compuesto, entonces existen enteros $a,b$ con
$$
n=ab,
\qquad
1<a\le b<n,
$$
y deduce que $a\le\sqrt n$.


**58.** **Nivel C.** Demuestra que todo entero compuesto $n>1$ posee un divisor primo $p$ tal que
$$
p\le\sqrt n.
$$
Separa los dos pasos: encontrar un factor no trivial pequeño y extraer de él un divisor primo.


**59.** **Nivel C.** Decide si $97$, $127$ y $221$ son primos usando únicamente el criterio de división por primos no mayores que la raíz cuadrada correspondiente. Registra qué divisores primos es necesario comprobar en cada caso.


**60.** **Nivel D.** Un estudiante intenta demostrar que $173$ es primo probando que no es divisible por $2,3,5$ ni $7$. Decide si el control es suficiente. Si no lo es, indica exactamente qué primos faltan comprobar y completa el diagnóstico.


**61.** **Nivel D.** Reconstruye la prueba de Euclides de que existen infinitos primos. Supón finita la lista $p_1,\ldots,p_k$, construye
$$
N=p_1p_2\cdots p_k+1,
$$
y demuestra que un divisor primo de $N$ no puede pertenecer a la lista.


**62.** **Nivel D.** Explica por qué en la prueba del ejercicio anterior **no** es necesario que $N$ sea primo. Da un ejemplo de una lista finita de primos para la cual el producto más $1$ sea compuesto, y muestra que el argumento de Euclides sigue funcionando con un divisor primo nuevo.


**63.** **Nivel D.** Sea $p_1,\ldots,p_k$ cualquier colección finita de primos distintos y sea
$$
N=p_1p_2\cdots p_k-1>1.
$$
¿Puede usarse siempre $N$ de la misma manera que el producto más $1$ para producir un primo fuera de la lista? Analiza cuidadosamente y da un contraejemplo si la afirmación falla.


**64.** **Nivel E.** Sea $n>1$. Supón que ningún primo $p\le\sqrt n$ divide a $n$. Demuestra directamente que $n$ es primo por contraposición del criterio de divisor primo pequeño. Explica por qué no hace falta probar divisibilidad por números compuestos.

## I. Potencias perfectas y diagnóstico


**65.** **Nivel C.** Demuestra que un entero positivo
$$
n=\prod_p p^{\alpha_p}
$$
es un cuadrado perfecto si y sólo si todos los exponentes $\alpha_p$ son pares.


**66.** **Nivel C.** Demuestra que $n>0$ es un cubo perfecto si y sólo si todos los exponentes de su factorización prima son múltiplos de $3$.


**67.** **Nivel D.** Generaliza los dos ejercicios anteriores: para $k\ge2$, demuestra que $n>0$ es una $k$-ésima potencia perfecta si y sólo si todos sus exponentes primos son múltiplos de $k$.


**68.** **Nivel C.** Decide cuáles de los siguientes números son cuadrados, cubos o sextas potencias perfectas, justificando mediante exponentes:
$$
2^6 3^{12},
\qquad
2^4 3^6 5^2,
\qquad
2^{12}3^{18}5^6.
$$


**69.** **Nivel D.** Sean $a,b>0$ con $\gcd(a,b)=1$. Si $ab$ es un cubo perfecto, demuestra que $a$ y $b$ son cubos perfectos. Indica dónde se usa la coprimalidad.


**70.** **Nivel D.** Sean $a,b>0$. Da un contraejemplo a la afirmación “si $ab$ es cuadrado, entonces $a$ y $b$ son cuadrados”. Luego formula una hipótesis adicional suficiente y explica, mediante exponentes primos, por qué repara la afirmación.


**71.** **Nivel E.** En b) y c), toma $a,b>0$; en d), toma $m\ge1$. Audita las siguientes inferencias y clasifícalas según la herramienta que las justifica: definición de primo, lema de Euclides, unicidad de factorización o ninguna.

a) $p\mid ab\Rightarrow p\mid a$ o $p\mid b$ para $p$ primo.

b) $a\mid b\Rightarrow$ cada exponente primo de $a$ no supera al correspondiente de $b$.

c) $ab$ cuadrado $\Rightarrow a,b$ cuadrados.

d) $p\mid a^m\Rightarrow p\mid a$ para $p$ primo.

Corrige las afirmaciones falsas.


**72.** **Nivel E.** Un estudiante dice: “como $a^2=b^3$, basta extraer raíz cuadrada y raíz cúbica para concluir que existe $c$ con $a=c^3$ y $b=c^2$”. Explica por qué esa frase no constituye una prueba aritmética en enteros. Formula un plan de demostración válido mediante factorización única y comparación de exponentes, sin completarlo todavía.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra rigurosamente que para $p>1$ son equivalentes:
$$
p\text{ es primo}
\qquad\text{e}\qquad
p\text{ es irreducible en }\mathbb Z.
$$
Tu prueba debe tratar factorizaciones con signos y explicar el papel de las unidades $\pm1$.


**74.** **Nivel F.** Demuestra por inducción fuerte que todo entero $n>1$ admite una factorización prima. Debes separar los casos primo y compuesto, justificar que los factores del caso compuesto son estrictamente menores que $n$ y explicar por qué esta prueba establece **existencia**, pero no todavía **unicidad**.


**75.** **Nivel F.** Demuestra desde Bézout/cancelación coprima de C15 que, si $p$ es primo,
$$
p\mid ab
\Longrightarrow
p\mid a\text{ o }p\mid b.
$$
La prueba no puede usar factorización única. Después explica por qué el resultado falla para divisores compuestos arbitrarios y exhibe un contraejemplo.


**76.** **Nivel G.** Supón que
$$
n=p_1\cdots p_r=q_1\cdots q_s
$$
son dos factorizaciones de $n>1$ en primos. Usando exclusivamente el lema de Euclides, primalidad y cancelación en $\mathbb Z$, demuestra que, tras reordenar los factores, ambas listas coinciden. Debes justificar por qué ninguna lista puede agotarse antes que la otra.


**77.** **Nivel F.** Sean
$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$
Demuestra:
$$
a\mid b
\iff
\alpha_p\le\beta_p\quad\text{para todo }p,
$$
$$
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)},
$$
$$
\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$
Deduce
$$
\gcd(a,b)\operatorname{lcm}(a,b)=ab.
$$
Señala en qué pasos se usa unicidad de factorización.


**78.** **Nivel F.** Reconstruye la demostración de Euclides de que existen infinitos números primos. En tu prueba, parte de una supuesta lista completa $p_1,\ldots,p_k$ y considera
$$
N=p_1\cdots p_k+1.
$$
Demuestra sólo lo necesario: que $N$ posee un divisor primo que no está en la lista. Después diagnostica con precisión por qué la afirmación “$N$ es primo” es innecesaria y, en general, falsa.


**79.** **Nivel G.** Sean $a,b>0$ con
$$
\gcd(a,b)=1
$$
y supón que $ab$ es un cuadrado perfecto. Demuestra que $a$ y $b$ son cuadrados perfectos. Tu prueba debe usar factorización única y explicar cómo la coprimalidad impide que un mismo primo reparta exponentes impares entre ambos factores. Finalmente, da un contraejemplo cuando se elimina la hipótesis de coprimalidad.


**80.** **Nivel G.** Sean $a,b,m,n>0$, con
$$
\gcd(m,n)=1
$$
y
$$
a^m=b^n.
$$
Demuestra que existe $c>0$ tal que
$$
a=c^n,
\qquad
b=c^m.
$$
Trabaja primo a primo: si $\alpha_p$ y $\beta_p$ son los exponentes de $p$ en $a$ y $b$, parte de
$$
m\alpha_p=n\beta_p
$$
y usa la coprimalidad de $m$ y $n$ para demostrar que $n\mid\alpha_p$ y $m\mid\beta_p$. Construye después $c$ y verifica las dos igualdades. Identifica exactamente dónde intervienen la unicidad de factorización y la cancelación coprima de C15.


***
## N. Hipótesis, exponentes y certificados

Las variables son enteras y se mantienen las restricciones de dominio de cada enunciado. Los problemas no requieren aritmética modular.


**81.** **Nivel E.** Sea $d>1$. Demuestra, sin factorización única, que la propiedad «para todos $a,b\in\mathbb Z$, si $d\mid ab$, entonces $d\mid a$ o $d\mid b$» equivale a que $d$ sea primo. En el sentido contrario, fabrica un contraejemplo a partir de cualquier descomposición no trivial de $d$.


**82.** **Nivel D.** Sean $p,q$ primos distintos y $d=pq$. Construye una familia infinita de productos $ab$ con $\gcd(a,b)=1$, $d\mid ab$ y $d\nmid a,b$. Después prueba que $\gcd(d,a)=1$, junto con $d\mid ab$, sí fuerza $d\mid b$. No uses unicidad de factorización en esta reparación.


**83.** **Nivel E.** Sea $p$ primo y $k\ge2$. Clasifica todos los pares $r,s\ge0$ para los cuales $p^rp^s$ es una $k$-ésima potencia, pero ninguno de los dos factores lo es. Expresa la clasificación mediante cocientes y restos enteros y construye infinitos ejemplos para cada $k$.


**84.** **Nivel D.** Audita esta comparación: «$2\cdot2\cdot3\cdot7=2\cdot3\cdot14$ son dos factorizaciones primas de longitudes distintas, luego falla la unicidad». Repara la segunda lista y compara ambas sin invocar el teorema de unicidad como argumento. Explica qué pasaría si, tras las cancelaciones legítimas, quedara una lista no vacía de primos.


**85.** **Nivel E.** Para $n>1$, sea $D$ su mayor divisor positivo estrictamente menor que $n$. Demuestra que $n/D$ es primo sin usar unicidad de factorización. Incluye el caso $D=1$ y explica por qué $D$ mismo no tiene que ser primo.


**86.** **Nivel E.** Para cada entero $n\ge2$, prueba que $N=n!+1$ tiene un divisor primo mayor que $n$. No supongas que $N$ es primo ni uses unicidad. Verifica el argumento para $n=5$, donde $N$ es compuesto.


**87.** **Nivel E.** Sea $N=2^7\cdot3^5\cdot7^2$. Determina el menor entero positivo $C$ para el cual $NC$ es cubo perfecto. Después clasifica todos los multiplicadores positivos con esa propiedad y construye la raíz cúbica entera de cada producto.


**88.** **Nivel D.** Determina todos los enteros $k\ge2$ para los cuales $N=2^{12}\cdot3^{18}\cdot5^{30}$ es una $k$-ésima potencia perfecta. Construye las raíces positivas correspondientes. Repite la pregunta para $N=1$ y explica por qué exige un caso separado.


**89.** **Nivel E.** Sea $N=2^6\cdot3^9\cdot5^{15}$. Clasifica los enteros $h\ge1$ para los cuales $N^h$ es una duodécima potencia perfecta. Construye una raíz entera positiva para cada valor permitido y demuestra que no falta ninguno.


**90.** **Nivel C.** Decide si 251 y 253 son primos. Para el primero registra todas las divisiones necesarias según la barrera de la raíz cuadrada; para el segundo detén el examen cuando dispongas de un certificado suficiente. Justifica por qué ambos certificados tienen alcances distintos.


**91.** **Nivel D.** Se informa que el entero $N=1000003$ tiene restos no nulos al dividirlo por $2,3,5,7,11,13,17,19$. ¿Es una certificación completa de primalidad por el criterio de [§16.12](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md#apm-c16-s12)? Indica exactamente el intervalo que todavía falta examinar. Compara con el certificado $1000005=3\cdot333335$, sin decidir por otros métodos si $N$ es primo.


**92.** **Nivel E.** Para $m\ge2$, audita la inferencia «$m!+1$ no tiene divisor primo menor o igual que $m$, luego es primo». Construye un contraejemplo con $m=5$. Si se añade un certificado $m!+1=ab$ con $1<a\le b$, demuestra sin unicidad que algún divisor primo $q$ cumple $m<q\le\sqrt{m!+1}$.

***
# Soluciones razonadas

## A. Primos, compuestos, unidades e irreducibles


### 1

Recordemos las convenciones del capítulo: las unidades de $\mathbb Z$ son $\pm1$; llamamos primo sólo a un entero **positivo** mayor que $1$ cuyos únicos divisores positivos son $1$ y él mismo; y llamamos compuesto sólo a un entero positivo mayor que $1$ que admite una factorización no trivial.

Por tanto:

- $-17$: **ninguna de esas categorías**. No es unidad y, por la convención del capítulo, los primos y compuestos son positivos. Aunque $-17$ es irreducible en $\mathbb Z$, eso es otra categoría.
- $-1$: **unidad**.
- $0$: **ninguna**. No es unidad, primo ni compuesto.
- $1$: **unidad**; no es primo.
- $2$: **primo**.
- $15$: **compuesto**, pues $15=3\cdot5$.
- $37$: **primo**. Como $\sqrt{37}<7$, basta descartar los primos $2,3,5$, y ninguno divide a $37$. Las divisiones que completan el descarte son $37=2\cdot18+1=3\cdot12+1=5\cdot7+2$; cada resto es no nulo y menor que el divisor.
- $49$: **compuesto**, pues $49=7^2$.

En particular, $0$ pertenece a la categoría «ninguna»: no es unidad, primo ni compuesto. No posee inverso multiplicativo, y las nociones de primo y compuesto se restringen aquí a enteros positivos mayores que $1$.


### 2

Analizamos uno por uno.

Para $29$, como $\sqrt{29}<6$, sólo habría que probar los primos $2,3,5$. Ninguno divide a $29$, así que $29$ es primo. Las divisiones que completan el descarte son $29=2\cdot14+1=3\cdot9+2=5\cdot5+4$; cada resto es no nulo y menor que el divisor.

$$
35=5\cdot7,
$$

por lo que $35$ es compuesto.

$$
51=3\cdot17,
$$

así que $51$ es compuesto.

Para $67$, como $\sqrt{67}<9$, basta probar $2,3,5,7$. Las divisiones
$$
67=2\cdot33+1=3\cdot22+1=5\cdot13+2=7\cdot9+4
$$
tienen restos positivos menores que sus respectivos divisores. Por tanto, ninguno divide a $67$ y $67$ es primo. Este certificado no presupone reglas de divisibilidad por las cifras.

$$
77=7\cdot11,
\qquad
91=7\cdot13,
$$

así que ambos son compuestos.

En conclusión,

$$
\boxed{29,67\text{ son primos};\qquad 35,51,77,91\text{ son compuestos}.}
$$

Para certificar primalidad no basta con decir “no encontré un divisor”: hay que justificar que se han descartado **todos los divisores primos que podrían existir**, lo que aquí se hace mediante la barrera $\sqrt n$.


### 3

Si $u$ es una unidad, existe $v\in\mathbb Z$ tal que

$$
uv=1.
$$

Tomando valores absolutos,

$$
|u||v|=1.
$$

Como $|u|$ y $|v|$ son enteros no negativos, el único modo de que su producto sea $1$ es

$$
|u|=|v|=1.
$$

Por tanto,

$$
u=1\quad\text{o}\quad u=-1.
$$

Recíprocamente,

$$
1\cdot1=1,
\qquad
(-1)(-1)=1,
$$

así que ambos poseen inverso entero. Luego

$$
\boxed{U(\mathbb Z)=\{1,-1\}.}
$$


### 4

La unicidad de la factorización pretende identificar, salvo orden, una lista finita bien determinada de factores primos. Si $1$ fuera declarado primo, podríamos insertar arbitrariamente tantos factores $1$ como quisiéramos.

Por ejemplo, para todo $k\ge0$,

$$
30=1^k\cdot2\cdot3\cdot5.
$$

Así obtendríamos las “factorizaciones”

$$
30=2\cdot3\cdot5
=1\cdot2\cdot3\cdot5
=1^2\cdot2\cdot3\cdot5
=\cdots,
$$

que tienen distinto número de factores y no se relacionan sólo por reordenación.

La condición $p>1$ en la definición de primo elimina exactamente esta proliferación. Por eso $1$ no se excluye por capricho: su exclusión es necesaria para una formulación limpia del teorema fundamental de la aritmética.


### 5

Sea $p>1$ primo. Queremos probar que $-p$ es irreducible en $\mathbb Z$.

Supongamos

$$
-p=ab,
\qquad a,b\in\mathbb Z.
$$

Tomando valores absolutos,

$$
p=|a||b|.
$$

Como $p$ es primo, sus únicos divisores positivos son $1$ y $p$. Por tanto, uno de los números $|a|,|b|$ debe ser $1$. En consecuencia, uno de $a,b$ es una unidad $\pm1$.

Esto demuestra que $-p$ es irreducible.

Sin embargo, en este capítulo la palabra **primo** se reserva a enteros positivos mayores que $1$. Por ello $-p$ es irreducible, pero no se denomina primo. Los enteros $p$ y $-p$ son asociados: difieren por la unidad $-1$.


### 6

**a) Falsa.** Por ejemplo, $-2$ es irreducible en $\mathbb Z$: si $-2=ab$, entonces $2=|a||b|$, de modo que uno de los factores tiene valor absoluto $1$. Sin embargo, $-2$ no es positivo.

**b) Verdadera.** Si $a$ es irreducible y

$$
-a=bc,
$$

entonces

$$
a=(-b)c.
$$

Por irreducibilidad de $a$, uno de $-b$ o $c$ es una unidad. Pero $-b$ es unidad si y sólo si $b$ lo es. Por tanto, $-a$ es irreducible.

**c) Verdadera.** Si $p>1$ es primo y $p=ab$, entonces $|a|\mid p$. Como $p$ sólo tiene los divisores positivos $1$ y $p$, uno de $|a|,|b|$ vale $1$. Luego uno de $a,b$ es unidad.

**d) Falsa.** Una unidad no es irreducible por definición: la irreducibilidad exige explícitamente que el elemento no sea una unidad.


### 7

Sea $n>1$.

Supongamos primero que $n$ es compuesto. Por definición existen enteros positivos $a,b$ con

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Así obtenemos inmediatamente la segunda condición. Además, $a\mid n$ y $1<a<n$, de modo que $n$ posee un divisor positivo no trivial.

Ahora supongamos que existe $d$ con

$$
1<d<n,
\qquad
d\mid n.
$$

Entonces $n=dq$ para algún entero positivo $q$. Como $d<n$ y $n=dq$, no puede ser $q=1$; por tanto $q>1$. También $q<n$, pues $d>1$. De este modo,

$$
n=dq,
\qquad
1<d,q<n,
$$

y $n$ es compuesto.

Así, las tres formulaciones son equivalentes.


### 8

La frase “$a$ es irreducible si sólo puede escribirse como $a=1\cdot a$” es incompleta porque en $\mathbb Z$ existen dos unidades, $1$ y $-1$, y las factorizaciones pueden contener signos.

La formulación correcta es:

> Un entero $a$ es irreducible si $a\ne0$, $a$ no es una unidad y, siempre que $a=bc$ con $b,c\in\mathbb Z$, al menos uno de $b,c$ es una unidad, es decir, vale $\pm1$.

Para $7$, cualquier factorización entera satisface

$$
7=|b||c|.
$$

Como $7$ es primo, uno de $|b|,|c|$ es $1$. Por ejemplo,

$$
7=1\cdot7=(-1)(-7).
$$

Para $-7$ ocurre lo mismo:

$$
-7=(-1)\cdot7=1\cdot(-7),
$$

y cualquier otra factorización tiene un factor de valor absoluto $1$. Por tanto, tanto $7$ como $-7$ son irreducibles.

## B. Divisores primos y descenso


### 9

Podemos elegir los siguientes divisores primos:

$$
2\mid84,
\qquad
11\mid143,
\qquad
13\mid221,
\qquad
17\mid391.
$$

En efecto,

$$
84=2\cdot42,
\qquad
143=11\cdot13,
$$

$$
221=13\cdot17,
\qquad
391=17\cdot23.
$$

Falta certificar que los divisores elegidos son primos. $2$ es primo por definición. Para $11$, basta descartar $2$ y $3$, pues $\sqrt{11}<4$. Para $13$, basta descartar $2$ y $3$, pues $\sqrt{13}<4$. Para $17$, basta descartar $2$ y $3$, pues $\sqrt{17}<5$; tampoco es divisible por ninguno de ellos. Así, todos los divisores exhibidos son efectivamente primos.


### 10

Si $n>1$ es compuesto, por definición existe una factorización

$$
n=ab
$$

con

$$
1<a<n,
\qquad
1<b<n.
$$

Por tanto, $a$ es un divisor de $n$ que satisface

$$
1<a<n.
$$

Este hecho es exactamente el descenso necesario para una inducción fuerte: cuando $n$ es compuesto, podemos reemplazar el problema sobre $n$ por un problema sobre un entero estrictamente menor, como $a$. La hipótesis inductiva puede aplicarse a $a$ porque $2\le a<n$.


### 11

Sea $P(n)$ la afirmación: “$n>1$ posee un divisor primo”. Demostraremos $P(n)$ para todo $n\ge2$ por inducción fuerte.

**Base.** Para $n=2$, el propio $2$ es primo y $2\mid2$.

**Paso inductivo.** Supongamos que $P(m)$ vale para todo $m$ con

$$
2\le m<n.
$$

Consideremos $n$.

- Si $n$ es primo, entonces $n\mid n$, y el propio $n$ es el divisor primo buscado.
- Si $n$ es compuesto, existen $a,b$ con
  $$
  n=ab,
  \qquad
  1<a<n.
  $$
  Como $2\le a<n$, la hipótesis inductiva aplicada a $a$ proporciona un primo $p$ tal que $p\mid a$. Como $a\mid n$, por transitividad
  $$
  p\mid n.
  $$

En ambos casos $n$ posee un divisor primo. Por inducción fuerte, el resultado vale para todo $n>1$.


### 12

Supongamos, por contradicción, que existe algún entero mayor que $1$ sin divisor primo. Sea $n$ el menor de todos ellos; el principio de buen orden garantiza su existencia.

El número $n$ no puede ser primo, pues entonces él mismo sería un divisor primo de $n$. Por tanto, $n$ es compuesto. Existen entonces $a,b$ tales que

$$
n=ab,
\qquad
1<a<n.
$$

Como $a<n$ y $a>1$, la minimalidad de $n$ implica que $a$ **sí** posee un divisor primo $p$. Así,

$$
p\mid a.
$$

Pero $a\mid n$, luego

$$
p\mid n,
$$

contradiciendo que $n$ no tenía divisor primo.

Por tanto, no existe contraejemplo: todo entero $n>1$ posee un divisor primo.


### 13

Sea $d>1$ el menor divisor positivo de $n$ mayor que $1$. Supongamos, para obtener una contradicción, que $d$ es compuesto.

Entonces existen enteros positivos $r,s$ tales que

$$
d=rs,
\qquad
1<r<d,
\qquad
1<s<d.
$$

Como $r\mid d$ y $d\mid n$, la transitividad de la divisibilidad da

$$
r\mid n.
$$

Pero $r>1$ y $r<d$, lo que contradice que $d$ era el menor divisor positivo de $n$ mayor que $1$.

Luego $d$ no puede ser compuesto. Como $d>1$, debe ser primo.


### 14

Supongamos

$$
n=ab,
\qquad a,b>1,
$$

y sea $p$ un divisor primo de $a$. Entonces

$$
p\mid a
\qquad\text{y}\qquad
a\mid n.
$$

Por transitividad,

$$
p\mid n.
$$

Así, cualquier primo que aparezca como divisor de un factor no trivial de $n$ es automáticamente divisor de $n$.

Esto explica por qué una factorización parcial es suficiente para encontrar divisores primos: si logramos escribir $n=ab$ con $1<a<n$, basta encontrar un divisor primo de $a$; ese mismo primo divide a $n$.


### 15

La frase “podemos repetir indefinidamente” no demuestra que el proceso termine. Precisamente hay que excluir la posibilidad de una cadena infinita de descomposiciones sin llegar a un primo.

Una formulación válida usa inducción fuerte. Sea $P(n)$ la afirmación “$n>1$ posee un divisor primo”. Suponemos $P(m)$ para todos los enteros $2\le m<n$.

Si $n$ es primo, terminamos. Si es compuesto, escribimos

$$
n=ab,
\qquad
1<a<n.
$$

La hipótesis inductiva aplicada a $a$ produce un primo $p$ con $p\mid a$, y entonces $p\mid n$.

También puede usarse buen orden: un supuesto contraejemplo mínimo tendría que ser compuesto y poseer un factor no trivial menor, que por minimalidad ya tendría un divisor primo. En ambos enfoques, la terminación queda respaldada por una propiedad bien fundada de los enteros positivos, no por una repetición informal.


### 16

Como $S$ es no vacío y todos sus elementos son enteros mayores que $1$, el principio de buen orden garantiza que $S$ posee un elemento mínimo; llamémoslo $m$.

Supongamos que $m$ es compuesto. Por la propiedad de cierre indicada en el enunciado, existe $d\in S$ tal que

$$
1<d<m.
$$

Pero esto contradice la minimalidad de $m$ dentro de $S$.

Por tanto, $m$ no es compuesto. Como $m>1$, necesariamente es primo.

El principio lógico decisivo es el **principio de buen orden**: todo subconjunto no vacío de los enteros positivos posee un elemento mínimo.

## C. Lema de Euclides


### 17

Sea $p$ primo y $a\in\mathbb Z$.

Si $p\mid a$, entonces $p$ es divisor común de $p$ y $a$. Como todo divisor común de $p$ y $a$ divide a $p$, y los únicos divisores positivos de $p$ son $1$ y $p$, se obtiene

$$
\gcd(p,a)=p.
$$

En particular, en este caso $\gcd(p,a)\ne1$.

Supongamos ahora que

$$
p\nmid a.
$$

Todo divisor común positivo $d$ de $p$ y $a$ debe dividir a $p$. Como $p$ es primo,

$$
d=1\quad\text{o}\quad d=p.
$$

La segunda posibilidad implicaría $p\mid a$, contra la hipótesis. Por tanto, el único divisor común positivo es $1$ y

$$
\gcd(p,a)=1.
$$

Así, exactamente una de las dos situaciones ocurre:

$$
\boxed{p\mid a\quad\text{o}\quad \gcd(p,a)=1.}
$$


### 18

Supongamos que $p$ es primo y

$$
p\mid ab.
$$

Si $p\mid a$, ya tenemos una de las dos conclusiones.

Supongamos entonces que

$$
p\nmid a.
$$

Por el ejercicio anterior,

$$
\gcd(p,a)=1.
$$

La cancelación coprima demostrada en C15 afirma que

$$
\gcd(p,a)=1,
\qquad
p\mid ab
\Longrightarrow
p\mid b.
$$

Por tanto,

$$
\boxed{p\mid a\quad\text{o}\quad p\mid b.}
$$

Esta demostración usa únicamente primalidad, MCD y la cancelación coprima derivada de Bézout. No utiliza factorización prima ni unicidad, lo cual es importante porque el lema de Euclides será después una herramienta para demostrar la unicidad.


### 19

**a)** Tomemos

$$
d=6,
\qquad a=2,
\qquad b=3.
$$

Entonces

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2,
\qquad
6\nmid3.
$$

Por tanto, la generalización es falsa para divisores compuestos arbitrarios.

**b)** Tomemos

$$
d=4,
\qquad a=2.
$$

Entonces

$$
4\mid2^2,
$$

pero

$$
4\nmid2.
$$

Lo que falta en ambos casos es la rigidez multiplicativa de un **primo**. El lema de Euclides garantiza que un primo que divide un producto debe dividir alguno de sus factores; un número compuesto puede repartir sus factores primos entre factores diferentes del producto.


### 20

De

$$
p\mid a
$$

y

$$
p\mid(a+b)
$$

se sigue que $p$ divide cualquier combinación lineal entera de $a$ y $a+b$. En particular,

$$
p\mid[(a+b)-a]=b.
$$

Así,

$$
\boxed{p\mid b.}
$$

La primalidad de $p$ no fue necesaria: el mismo argumento vale para cualquier divisor no nulo $d$. Sólo usamos el cierre elemental de la divisibilidad bajo diferencias, no el lema de Euclides.


### 21

Como $p$ es primo y $p\nmid a$, tenemos

$$
\gcd(p,a)=1.
$$

Por Bézout existen $x,y\in\mathbb Z$ tales que

$$
px+ay=1.
$$

Multiplicamos por $b$:

$$
pbx+aby=b.
$$

Por hipótesis,

$$
p\mid ab,
$$

de modo que $p\mid aby$. Evidentemente también

$$
p\mid pbx.
$$

Por cierre bajo sumas,

$$
p\mid(pbx+aby)=b.
$$

Por tanto,

$$
\boxed{p\mid b.}
$$

Esta es la forma explícita de la prueba de cancelación coprima aplicada al primo $p$.


### 22

Partimos de

$$
p\mid abc.
$$

Aplicamos el lema de Euclides al producto

$$
a\cdot(bc).
$$

Entonces

$$
p\mid a
\quad\text{o}\quad
p\mid bc.
$$

Como $p\nmid a$, necesariamente

$$
p\mid bc.
$$

Aplicamos ahora el lema de Euclides al producto $b\cdot c$:

$$
p\mid b
\quad\text{o}\quad
p\mid c.
$$

Como $p\nmid b$, queda

$$
\boxed{p\mid c.}
$$

El orden es, por tanto, primero separar $a$ del producto $bc$ y después separar $b$ de $c$.


### 23

Sean $p$ y $q$ primos distintos. Si $p\mid q$, como $q$ es primo y $p>1$, necesariamente tendríamos

$$
p=q,
$$

contradicción. Por tanto,

$$
\boxed{p\nmid q.}
$$

Todo divisor común positivo de $p$ y $q$ divide a $p$, así que sólo puede ser $1$ o $p$. Como $p\nmid q$, la segunda posibilidad queda descartada. Luego

$$
\boxed{\gcd(p,q)=1.}
$$

Supongamos ahora

$$
pq\mid ab
$$

y $p\nmid b$. Por transitividad,

$$
p\mid ab.
$$

El lema de Euclides da

$$
p\mid a\quad\text{o}\quad p\mid b.
$$

Como $p\nmid b$,

$$
\boxed{p\mid a.}
$$

No podemos deducir necesariamente $q\mid a$. Por ejemplo, tomando

$$
p=2,
\qquad q=3,
\qquad a=2,
\qquad b=3,
$$

tenemos $6\mid ab$ y $2\nmid3$, pero $3\nmid2$.


### 24

El salto inválido consiste en suponer que, porque $2$ y $3$ son primos y ambos dividen al producto $ab$, necesariamente ambos deben dividir **el mismo** factor.

El lema de Euclides sólo permite concluir por separado:

$$
2\mid a\quad\text{o}\quad2\mid b,
$$

y

$$
3\mid a\quad\text{o}\quad3\mid b.
$$

Es perfectamente posible que $2$ divida a $a$ y $3$ divida a $b$.

El contraejemplo más simple es

$$
a=2,
\qquad b=3.
$$

Entonces

$$
6\mid ab,
$$

pero

$$
6\nmid a,
\qquad
6\nmid b.
$$

Por tanto, el lema de Euclides no se puede aplicar al número compuesto $6$ como si fuera primo.

## D. Productos finitos y potencias


### 25

Demostramos por inducción sobre $n$ que, si $p$ es primo y

$$
p\mid a_1a_2\cdots a_n,
$$

entonces $p$ divide alguno de los factores.

Para $n=1$, la conclusión $p\mid a_1$ coincide con la hipótesis. Para $n=2$, esto es exactamente el lema de Euclides.

Supongamos el resultado válido para productos de $n$ factores y consideremos

$$
p\mid a_1a_2\cdots a_n a_{n+1}.
$$

Agrupamos:

$$
p\mid(a_1\cdots a_n)a_{n+1}.
$$

Por el lema de Euclides,

$$
p\mid a_1\cdots a_n
\quad\text{o}\quad
p\mid a_{n+1}.
$$

En el segundo caso terminamos. En el primero, la hipótesis inductiva garantiza que $p$ divide alguno de $a_1,\ldots,a_n$.

Por inducción, el resultado vale para todo producto finito.


### 26

Escribimos

$$
a^m=\underbrace{a\cdot a\cdots a}_{m\text{ factores}}.
$$

Si

$$
p\mid a^m,
$$

la versión finita del lema de Euclides implica que $p$ divide al menos uno de los $m$ factores del producto. Pero todos esos factores son iguales a $a$. Por tanto,

$$
\boxed{p\mid a.}
$$

El resultado previo utilizado es precisamente: un primo que divide un producto finito divide al menos uno de sus factores.


### 27

De

$$
p\mid a^3b^2
$$

aplicamos el lema de Euclides al producto $a^3\cdot b^2$:

$$
p\mid a^3
\quad\text{o}\quad
p\mid b^2.
$$

En el primer caso, la consecuencia para potencias da $p\mid a$; en el segundo, da $p\mid b$. Por tanto,

$$
\boxed{p\mid a\quad\text{o}\quad p\mid b.}
$$

La conclusión es disyuntiva: la información $p\mid a^3b^2$ no determina cuál de los dos factores contiene a $p$. Incluso puede ocurrir que $p$ divida a ambos.


### 28

Si

$$
p_1p_2\cdots p_r\mid a,
$$

entonces para cada $i$ se cumple

$$
p_i\mid p_1p_2\cdots p_r.
$$

Por transitividad de la divisibilidad,

$$
p_i\mid a.
$$

Así,

$$
\boxed{p_i\mid a\quad\text{para todo }i.}
$$

No necesitamos el lema de Euclides para esta dirección. Tampoco necesitamos que los $p_i$ sean distintos ni primos: si un producto divide a $a$, cualquiera de sus factores divide al producto y, por transitividad, divide a $a$.


### 29

De

$$
p^2q^3\mid a^5
$$

se sigue por transitividad que

$$
p\mid a^5
\qquad\text{y}\qquad
q\mid a^5.
$$

Como $p$ y $q$ son primos, la propiedad de las potencias da

$$
p\mid a
\qquad\text{y}\qquad
q\mid a.
$$

Por tanto,

$$
\boxed{p\mid a\text{ y }q\mid a.}
$$

No fue necesario comparar exponentes de una factorización prima de $a$; bastó usar transitividad y el lema de Euclides aplicado a potencias.


### 30

La hipótesis es

$$
p\mid a_1^2a_2^2\cdots a_n^2.
$$

Por la versión finita del lema de Euclides, existe algún $j$ tal que

$$
p\mid a_j^2.
$$

Como $p$ es primo, la propiedad de las potencias implica

$$
p\mid a_j.
$$

Por tanto, $p$ divide al menos uno de los enteros $a_1,\ldots,a_n$.


### 31

La afirmación es verdadera.

Supongamos

$$
p\mid a^m b^n.
$$

Por el lema de Euclides,

$$
p\mid a^m
\quad\text{o}\quad
p\mid b^n.
$$

La propiedad de potencias da

$$
p\mid a
\quad\text{o}\quad
p\mid b.
$$

En cualquiera de los dos casos, $p$ divide al producto $ab$. Luego

$$
\boxed{p\mid a^m b^n\Longrightarrow p\mid ab.}
$$

No se utilizó el teorema fundamental de la aritmética.


### 32

El teorema para productos finitos afirma:

$$
p\mid a_1a_2\cdots a_n
\Longrightarrow
\exists j\; p\mid a_j.
$$

Su contraposición es

$$
\left(p\nmid a_j\text{ para todo }j\right)
\Longrightarrow
p\nmid a_1a_2\cdots a_n.
$$

Ésta es exactamente la afirmación solicitada. Por tanto, si $p$ no divide a ninguno de los factores, no puede dividir su producto.

## E. Existencia y unicidad de factorización


### 33

Factorizamos cada número.

Para $756$:

$$
756=4\cdot189=2^2\cdot3^3\cdot7.
$$

Para $1386$:

$$
1386=2\cdot693=2\cdot3^2\cdot77
=2\cdot3^2\cdot7\cdot11.
$$

Para $2310$:

$$
2310=231\cdot10
=(3\cdot7\cdot11)(2\cdot5).
$$

Así, en forma canónica,

$$
\boxed{756=2^2\cdot3^3\cdot7,}
$$

$$
\boxed{1386=2\cdot3^2\cdot7\cdot11,}
$$

$$
\boxed{2310=2\cdot3\cdot5\cdot7\cdot11.}
$$


### 34

Podemos iniciar dos árboles distintos para $360$.

Primer árbol:

$$
360=36\cdot10
=(6\cdot6)(2\cdot5)
=(2\cdot3)(2\cdot3)(2\cdot5).
$$

Así,

$$
360=2^3\cdot3^2\cdot5.
$$

Segundo árbol:

$$
360=45\cdot8
=(5\cdot9)(2\cdot4)
=5\cdot3\cdot3\cdot2\cdot2\cdot2.
$$

Nuevamente,

$$
360=2^3\cdot3^2\cdot5.
$$

Los pasos intermedios son diferentes, pero la colección final de factores primos, contando multiplicidades, coincide. Esta coincidencia es precisamente lo que interpreta la **unicidad** del teorema fundamental de la aritmética.


### 35

Sea $P(n)$ la afirmación “$n>1$ puede escribirse como producto finito de primos”. Demostramos $P(n)$ por inducción fuerte.

**Base.** $2$ es primo, de modo que ya es producto de un solo primo.

**Paso inductivo.** Supongamos que $P(m)$ vale para todo entero $m$ con

$$
2\le m<n.
$$

Consideremos $n$.

Si $n$ es primo, entonces

$$
n=n
$$

es ya una factorización prima.

Si $n$ es compuesto, existen $a,b$ con

$$
n=ab,
\qquad
1<a<n,
\qquad
1<b<n.
$$

Por la hipótesis inductiva,

$$
a=p_1\cdots p_r,
\qquad
b=q_1\cdots q_s,
$$

con todos los $p_i,q_j$ primos. Entonces

$$
n=p_1\cdots p_r q_1\cdots q_s,
$$

que es una factorización completa de $n$ en primos.

La prueba establece sólo **existencia**. En ningún punto comparamos dos factorizaciones distintas, por lo que todavía no se ha demostrado unicidad.


### 36

Supongamos que existen enteros mayores que $1$ que no admiten factorización prima, y sea $n$ el menor de ellos.

El número $n$ no puede ser primo, porque entonces él mismo sería una factorización de un solo factor primo.

Tampoco puede ser compuesto. Si lo fuera, escribiríamos

$$
n=ab,
\qquad
1<a,b<n.
$$

Como $a$ y $b$ son menores que el contraejemplo mínimo $n$, ambos sí admiten factorización prima:

$$
a=p_1\cdots p_r,
\qquad
b=q_1\cdots q_s.
$$

Multiplicando,

$$
n=p_1\cdots p_r q_1\cdots q_s,
$$

contradicción.

Por tanto, no existe tal contraejemplo mínimo, y todo entero mayor que $1$ admite factorización prima.


### 37

Tenemos

$$
n=p_1p_2\cdots p_r=q_1q_2\cdots q_s.
$$

Como $p_1$ divide al producto del lado izquierdo, también divide a $n$, y por la segunda expresión de $n$,

$$
p_1\mid q_1q_2\cdots q_s.
$$

La versión finita del lema de Euclides implica que existe algún $j$ tal que

$$
p_1\mid q_j.
$$

Aquí se usa el **lema de Euclides**.

Ahora usamos que $q_j$ es primo. Sus únicos divisores positivos son $1$ y $q_j$. Como $p_1>1$ y $p_1\mid q_j$,

$$
p_1=q_j.
$$

Aquí se usa la **primalidad de $q_j$**.

Así, cada primer factor primo de una factorización debe aparecer también en la otra.


### 38

Partimos de

$$
p_1p_2\cdots p_r=q_1q_2\cdots q_s.
$$

Por el ejercicio anterior, $p_1=q_j$ para algún $j$. Reordenamos la segunda lista y suponemos, sin pérdida de generalidad,

$$
p_1=q_1.
$$

Entonces

$$
p_1p_2\cdots p_r=p_1q_2\cdots q_s.
$$

Como $p_1\ne0$, cancelamos en la igualdad de enteros:

$$
p_2\cdots p_r=q_2\cdots q_s.
$$

Repetimos el argumento. Cada $p_i$ debe coincidir con uno de los primos restantes de la segunda lista; reordenamos y cancelamos.

No puede agotarse una lista antes que la otra. Si, por ejemplo, después de cancelar todos los $p_i$ quedaran factores $q_k,\ldots,q_s$, obtendríamos

$$
1=q_kq_{k+1}\cdots q_s.
$$

Pero cada $q_j>1$, así que el producto del lado derecho es mayor que $1$, contradicción.

Por tanto,

$$
r=s,
$$

y, tras una reordenación,

$$
p_i=q_i
$$

para todo $i$. La factorización prima es única salvo el orden de los factores.


### 39

Las tres afirmaciones son lógicamente distintas.

1. **Existencia de un divisor primo:** para cada $n>1$ existe al menos un primo $p$ con $p\mid n$.
2. **Existencia de una factorización completa:** cada $n>1$ puede escribirse como producto finito de primos.
3. **Unicidad:** dos productos de primos que representan el mismo entero contienen los mismos factores con las mismas multiplicidades, salvo orden.

La primera afirmación sólo garantiza un primer paso. Para llegar a una factorización completa hay que demostrar que el proceso de descomposición termina; esto se hace mediante inducción fuerte o buen orden.

Incluso una vez probada la existencia de una factorización, todavía podría, en principio, haber dos colecciones distintas de primos cuyo producto fuera el mismo. La unicidad exige un argumento adicional basado en el lema de Euclides y cancelación.

Por eso “todo número tiene un divisor primo” no basta para establecer el teorema fundamental de la aritmética.


### 40

La prueba propuesta es circular porque pretende justificar la unicidad mediante la afirmación

$$
p\mid ab\Longrightarrow p\mid a\text{ o }p\mid b,
$$

pero luego justifica esa afirmación diciendo que, en la **factorización prima única** del producto, $p$ debe aparecer en uno de los factores. Es decir, utiliza precisamente la unicidad que pretende demostrar.

El orden correcto de dependencias es:

$$
\text{Bézout y coprimalidad de C15}
\Longrightarrow
\text{cancelación coprima}
$$

$$
\Longrightarrow
\text{lema de Euclides para primos}
$$

$$
\Longrightarrow
\text{lema para productos finitos}
$$

$$
\Longrightarrow
\text{unicidad de la factorización prima}.
$$

Por separado, la existencia de factorización se prueba mediante inducción fuerte y no necesita el lema de Euclides. Sólo después de tener existencia y unicidad podemos hablar legítimamente de “los exponentes” de la factorización prima de un entero.

## F. Forma canónica y divisibilidad por exponentes


### 41

Para $900$,

$$
900=9\cdot100=3^2\cdot2^2\cdot5^2,
$$

así que

$$
\boxed{900=2^2\cdot3^2\cdot5^2.}
$$

Para $13860$,

$$
13860=10\cdot1386
=(2\cdot5)(2\cdot3^2\cdot7\cdot11),
$$

de donde

$$
\boxed{13860=2^2\cdot3^2\cdot5\cdot7\cdot11.}
$$

Finalmente,

$$
1260=126\cdot10
=(2\cdot3^2\cdot7)(2\cdot5),
$$

por lo que

$$
\boxed{-1260=(-1)\cdot2^2\cdot3^2\cdot5\cdot7.}
$$

La unidad $-1$ se separa de los factores primos positivos.


### 42

Tenemos

$$
a=2^3 3^2 5,
\qquad
b=2^5 3^2 5^4 7.
$$

Para $a\mid b$ comparamos exponentes:

$$
3\le5,
\qquad
2\le2,
\qquad
1\le4,
$$

y el exponente de $7$ en $a$ es $0\le1$. Por tanto,

$$
\boxed{a\mid b.}
$$

En cambio $b\nmid a$, pues el exponente de $2$ en $b$ es $5>3$.

Para

$$
2^4 3^2 5,
$$

los exponentes $4,2,1$ no superan a los correspondientes de $b$, luego

$$
\boxed{2^4 3^2 5\mid b.}
$$

Finalmente,

$$
2^5 3^3\nmid b,
$$

porque el exponente de $3$ requerido es $3$, mientras que en $b$ sólo aparece $3^2$.


### 43

Escribamos

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Supongamos primero que

$$
\alpha_p\le\beta_p
$$

para todo primo $p$. Entonces cada diferencia $\beta_p-\alpha_p$ es no negativa. Definimos

$$
c=\prod_p p^{\beta_p-\alpha_p}.
$$

Sólo finitos exponentes son no nulos. Por las leyes de exponentes,

$$
ac=
\prod_p p^{\alpha_p+\beta_p-\alpha_p}
=
\prod_p p^{\beta_p}
=b.
$$

Por tanto, $a\mid b$.

Recíprocamente, supongamos $a\mid b$. Existe $c>0$ con

$$
b=ac.
$$

Factorizamos

$$
c=\prod_p p^{\gamma_p}.
$$

Entonces

$$
b=ac=\prod_p p^{\alpha_p+\gamma_p}.
$$

Por **unicidad de la factorización prima**,

$$
\beta_p=\alpha_p+\gamma_p
$$

para todo $p$. Como $\gamma_p\ge0$,

$$
\alpha_p\le\beta_p.
$$

Así,

$$
\boxed{a\mid b\iff \alpha_p\le\beta_p\text{ para todo primo }p.}
$$


### 44

Como

$$
72=2^3 3^2,
$$

todo divisor positivo tiene la forma

$$
2^i3^j,
\qquad
0\le i\le3,
\qquad
0\le j\le2.
$$

Los divisores son

$$
1,2,3,4,6,8,9,12,18,24,36,72.
$$

Hay $4$ posibilidades para $i$ y $3$ para $j$, de modo que el número total de divisores positivos es

$$
4\cdot3=12.
$$

Por tanto, $72$ tiene exactamente $12$ divisores positivos.


### 45

Sea

$$
n=p_1^{\alpha_1}\cdots p_r^{\alpha_r}
$$

y sea $d>0$ un divisor de $n$. Por el criterio de divisibilidad mediante exponentes, el exponente de cada primo en $d$ no puede superar al exponente correspondiente en $n$. Además, ningún primo que no aparezca en $n$ puede aparecer con exponente positivo en $d$.

Por tanto,

$$
d=p_1^{\beta_1}\cdots p_r^{\beta_r},
\qquad
0\le\beta_i\le\alpha_i.
$$

Recíprocamente, si elegimos enteros $\beta_i$ con

$$
0\le\beta_i\le\alpha_i,
$$

definimos

$$
c=p_1^{\alpha_1-\beta_1}\cdots p_r^{\alpha_r-\beta_r}.
$$

Entonces

$$
dc=n,
$$

de modo que $d\mid n$. Queda demostrado el criterio en ambas direcciones.


### 46

Escribamos

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

De $a\mid b$ obtenemos

$$
\alpha_p\le\beta_p
$$

para todo primo $p$. De $b\mid a$ obtenemos

$$
\beta_p\le\alpha_p.
$$

Por tanto,

$$
\alpha_p=\beta_p
$$

para todo $p$. Por unicidad de la factorización,

$$
\boxed{a=b.}
$$

En C14 la misma conclusión se obtenía mediante la propiedad de tamaño: $a\mid b$ implicaba $a\le b$ y $b\mid a$ implicaba $b\le a$. La prueba actual es distinta: traduce la divisibilidad en una comparación componente a componente de exponentes primos.


### 47

Sea

$$
a=\prod_p p^{\alpha_p}>0.
$$

Entonces

$$
a^m=\prod_p p^{m\alpha_p}.
$$

Como $m\ge1$,

$$
\alpha_p\le m\alpha_p
$$

para todo primo $p$. Por el criterio de exponentes,

$$
\boxed{a\mid a^m.}
$$

Ahora supongamos $a>1$. Entonces existe al menos un primo $p$ con $\alpha_p>0$. Para que

$$
a^m\mid a
$$

se necesitaría

$$
m\alpha_p\le\alpha_p.
$$

Como $\alpha_p>0$, esto implica $m\le1$. Junto con $m\ge1$, resulta

$$
\boxed{m=1.}
$$


### 48

Escribamos

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p},
\qquad
c=\prod_p p^{\gamma_p}.
$$

La condición

$$
\gcd(a,b)=1
$$

significa que

$$
\min(\alpha_p,\beta_p)=0
$$

para todo primo $p$.

Como $a\mid bc$,

$$
\alpha_p\le\beta_p+\gamma_p
$$

para todo $p$.

Si $\alpha_p>0$, la coprimalidad obliga a $\beta_p=0$. Entonces

$$
\alpha_p\le\gamma_p.
$$

Si $\alpha_p=0$, la misma desigualdad es trivial. Por tanto,

$$
\alpha_p\le\gamma_p
$$

para todo $p$, y el criterio de divisibilidad da

$$
\boxed{a\mid c.}
$$

Esta prueba es posterior a la de C15: utiliza la factorización prima única y compara exponentes. La prueba de C15, en cambio, obtenía la cancelación coprima directamente de una identidad de Bézout, sin usar aún teoría de factorización.

## G. MCD, MCM y factorización


### 49

Primero,

$$
360=2^3\cdot3^2\cdot5,
$$

$$
840=2^3\cdot3\cdot5\cdot7.
$$

Tomando mínimos y máximos de exponentes,

$$
\gcd(360,840)=2^3\cdot3\cdot5=120,
$$

$$
\operatorname{lcm}(360,840)=2^3\cdot3^2\cdot5\cdot7=2520.
$$

Para el segundo par,

$$
756=2^2\cdot3^3\cdot7,
$$

$$
630=2\cdot3^2\cdot5\cdot7.
$$

Luego

$$
\gcd(756,630)=2\cdot3^2\cdot7=126,
$$

$$
\operatorname{lcm}(756,630)=2^2\cdot3^3\cdot5\cdot7=3780.
$$

Finalmente,

$$
1001=7\cdot11\cdot13,
$$

$$
1430=2\cdot5\cdot11\cdot13.
$$

Por tanto,

$$
\gcd(1001,1430)=11\cdot13=143,
$$

$$
\operatorname{lcm}(1001,1430)=2\cdot5\cdot7\cdot11\cdot13=10010.
$$


### 50

Sea

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p},
$$

y definamos

$$
d=\prod_p p^{\min(\alpha_p,\beta_p)}.
$$

Como

$$
\min(\alpha_p,\beta_p)\le\alpha_p
$$

y

$$
\min(\alpha_p,\beta_p)\le\beta_p,
$$

el criterio de divisibilidad por exponentes da

$$
d\mid a,
\qquad
d\mid b.
$$

Así, $d$ es divisor común.

Sea ahora $c>0$ cualquier divisor común de $a$ y $b$, con

$$
c=\prod_p p^{\gamma_p}.
$$

Como $c\mid a$ y $c\mid b$,

$$
\gamma_p\le\alpha_p
\qquad\text{y}\qquad
\gamma_p\le\beta_p.
$$

Por tanto,

$$
\gamma_p\le\min(\alpha_p,\beta_p).
$$

De nuevo por el criterio de exponentes,

$$
c\mid d.
$$

Si un divisor común es negativo, aplicamos lo anterior a $|c|$ y cambiamos el signo del testigo; por tanto también divide a $d$. Así $d$ satisface la caracterización universal del MCD y

$$
\boxed{\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)}.}
$$


### 51

Definamos

$$
m=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$

Como

$$
\alpha_p\le\max(\alpha_p,\beta_p),
$$

se tiene $a\mid m$. Del mismo modo, $b\mid m$. Por tanto, $m$ es múltiplo común.

Sea $M>0$ cualquier múltiplo común de $a$ y $b$, y escribamos

$$
M=\prod_p p^{\mu_p}.
$$

De $a\mid M$ y $b\mid M$ obtenemos

$$
\alpha_p\le\mu_p,
\qquad
\beta_p\le\mu_p.
$$

Luego

$$
\max(\alpha_p,\beta_p)\le\mu_p.
$$

Por tanto,

$$
m\mid M.
$$

En particular, como $m,M>0$, también $m\le M$. Así $m$ es el mínimo común múltiplo y

$$
\boxed{\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.}
$$


### 52

Usamos las fórmulas

$$
\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)},
$$

$$
\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$

Multiplicando,

$$
\gcd(a,b)\operatorname{lcm}(a,b)
=
\prod_p p^{\min(\alpha_p,\beta_p)+\max(\alpha_p,\beta_p)}.
$$

Para enteros no negativos $r,s$,

$$
\min(r,s)+\max(r,s)=r+s.
$$

Aplicando esto primo por primo,

$$
\gcd(a,b)\operatorname{lcm}(a,b)
=
\prod_p p^{\alpha_p+\beta_p}.
$$

Pero

$$
\prod_p p^{\alpha_p+\beta_p}
=
\left(\prod_p p^{\alpha_p}\right)
\left(\prod_p p^{\beta_p}\right)
=ab.
$$

Por tanto,

$$
\boxed{\gcd(a,b)\operatorname{lcm}(a,b)=ab.}
$$


### 53

Supongamos primero

$$
\gcd(a,b)=1.
$$

Si existiera un primo $p$ que dividiera a ambos, entonces $p$ sería un divisor común positivo mayor que $1$. Por la propiedad universal del MCD,

$$
p\mid\gcd(a,b)=1,
$$

imposible. Por tanto, ningún primo divide simultáneamente a $a$ y a $b$.

Recíprocamente, supongamos que no existe ningún primo que divida a ambos. Si $\gcd(a,b)>1$, entonces el MCD, por ser un entero mayor que $1$, posee un divisor primo $p$. Como

$$
p\mid\gcd(a,b),
$$

y el MCD divide a $a$ y a $b$, tendríamos

$$
p\mid a,
\qquad
p\mid b,
$$

contradicción.

Luego

$$
\boxed{\gcd(a,b)=1
\iff
\text{$a$ y $b$ no comparten ningún factor primo}.}
$$


### 54

Si $\gcd(a,b)=1$, entonces para cada primo $p$ no pueden ser simultáneamente positivos $\alpha_p$ y $\beta_p$. Por tanto,

$$
\max(\alpha_p,\beta_p)=\alpha_p+\beta_p.
$$

Así,

$$
\operatorname{lcm}(a,b)
=
\prod_p p^{\alpha_p+\beta_p}
=ab.
$$

Luego

$$
\boxed{\gcd(a,b)=1\Longrightarrow \operatorname{lcm}(a,b)=ab.}
$$

Si la coprimalidad falla, el producto suele repetir factores comunes. Por ejemplo,

$$
a=6,
\qquad b=15.
$$

Entonces

$$
\gcd(6,15)=3,
$$

pero

$$
\operatorname{lcm}(6,15)=30\ne90=6\cdot15.
$$


### 55

Si $a\mid b$, entonces

$$
\alpha_p\le\beta_p
$$

para todo primo $p$. En consecuencia,

$$
\min(\alpha_p,\beta_p)=\alpha_p,
$$

y

$$
\max(\alpha_p,\beta_p)=\beta_p.
$$

Por las fórmulas del MCD y del MCM,

$$
\gcd(a,b)=\prod_p p^{\alpha_p}=a,
$$

$$
\operatorname{lcm}(a,b)=\prod_p p^{\beta_p}=b.
$$

Así,

$$
\boxed{a\mid b\Longrightarrow \gcd(a,b)=a,
\quad
\operatorname{lcm}(a,b)=b.}
$$

Esto refleja el orden de divisibilidad: cuando $a$ está por debajo de $b$ en ese orden, el mayor divisor común es precisamente $a$ y el menor múltiplo común es precisamente $b$.


### 56

Supongamos que un primo $p$ divide a $ab$. Entonces el exponente de $p$ en $ab$ es

$$
\alpha_p+\beta_p>0.
$$

Por tanto, al menos uno de $\alpha_p,\beta_p$ es positivo, y entonces

$$
\max(\alpha_p,\beta_p)>0.
$$

Así $p$ divide al MCM:

$$
\boxed{p\mid ab\Longrightarrow p\mid\operatorname{lcm}(a,b).}
$$

Ahora supongamos

$$
p\mid\gcd(a,b).
$$

Entonces

$$
\min(\alpha_p,\beta_p)>0,
$$

por lo que ambos exponentes son positivos. Así,

$$
\boxed{p\mid a\text{ y }p\mid b.}
$$

La primera afirmación se expresa mediante un **máximo** de exponentes; la segunda, mediante un **mínimo**. No son una el converso literal de la otra. El converso de la primera sería $p\mid\operatorname{lcm}(a,b)\Rightarrow p\mid ab$, mientras que el converso de la segunda sería $p\mid a$ y $p\mid b\Rightarrow p\mid\gcd(a,b)$.

## H. Primalidad e infinitud de los primos


### 57

Si $n>1$ es compuesto, existen enteros $a,b>1$ tales que

$$
n=ab.
$$

Intercambiando los factores si es necesario, podemos suponer

$$
a\le b.
$$

Como ambos son mayores que $1$ y su producto es $n$,

$$
1<a\le b<n.
$$

De $a\le b$ obtenemos

$$
a^2\le ab=n.
$$

Como $a>0$,

$$
\boxed{a\le\sqrt n.}
$$

Así todo compuesto posee un factor no trivial no mayor que su raíz cuadrada.


### 58

Sea $n>1$ compuesto. Por el ejercicio anterior existen $a,b$ con

$$
n=ab,
\qquad
1<a\le\sqrt n.
$$

Como $a>1$, el teorema de existencia de divisores primos garantiza un primo $p$ tal que

$$
p\mid a.
$$

Como $p\le a$,

$$
p\le\sqrt n.
$$

Además, $a\mid n$, así que por transitividad

$$
p\mid n.
$$

Por tanto,

$$
\boxed{n\text{ compuesto}\Longrightarrow
\exists p\text{ primo}: p\mid n,
\ p\le\sqrt n.}
$$

Los dos pasos son distintos: primero encontramos un factor no trivial pequeño y después extraemos de él un divisor primo.


### 59

Para $97$,

$$
\sqrt{97}<10.
$$

Sólo hay que comprobar $2,3,5,7$. Ninguno divide a $97$. Las divisiones que completan el descarte son $97=2\cdot48+1=3\cdot32+1=5\cdot19+2=7\cdot13+6$; cada resto es no nulo y menor que el divisor. Por tanto,

$$
\boxed{97\text{ es primo}.}
$$

Para $127$,

$$
\sqrt{127}<12.
$$

Debemos comprobar $2,3,5,7,11$. $127$ no es divisible por ninguno: en particular,

$$
127=7\cdot18+1,
\qquad
127=11\cdot11+6.
$$

Luego

$$
\boxed{127\text{ es primo}.}
$$

Las divisiones que completan el descarte son $127=2\cdot63+1=3\cdot42+1=5\cdot25+2$; cada resto es no nulo y menor que el divisor.

Para $221$,

$$
\sqrt{221}<15.
$$

Probamos $2,3,5,7,11,13$. Encontramos

$$
221=13\cdot17.
$$

Por tanto,

$$
\boxed{221\text{ es compuesto}.}
$$


### 60

Tenemos

$$
\sqrt{173}\approx13.15.
$$

Por tanto, para certificar primalidad hay que descartar todos los primos no mayores que $\sqrt{173}$:

$$
2,3,5,7,11,13.
$$

El estudiante sólo revisó $2,3,5,7$, así que su control no es suficiente.

Completamos:

$$
173=11\cdot15+8,
$$

y

$$
173=13\cdot13+4.
$$

Así, ni $11$ ni $13$ dividen a $173$. Las divisiones que completan el descarte son $173=2\cdot86+1=3\cdot57+2=5\cdot34+3=7\cdot24+5$; cada resto es no nulo y menor que el divisor. Como tampoco lo hacen $2,3,5,7$, no existe divisor primo no mayor que $\sqrt{173}$. Por el criterio de primalidad,

$$
\boxed{173\text{ es primo}.}
$$


### 61

Supongamos, por contradicción, que sólo existen finitos números primos:

$$
p_1,p_2,\ldots,p_k.
$$

Construimos

$$
N=p_1p_2\cdots p_k+1.
$$

Como $N>1$, posee algún divisor primo $q$.

Si la lista fuera completa, $q$ tendría que coincidir con algún $p_j$. Entonces

$$
q\mid p_1p_2\cdots p_k
$$

y también

$$
q\mid N.
$$

Por cierre de la divisibilidad bajo diferencias,

$$
q\mid\left(N-p_1p_2\cdots p_k\right)=1.
$$

Esto es imposible porque $q>1$.

Por tanto, $q$ no pertenece a la supuesta lista completa. Contradicción. Luego

$$
\boxed{\text{existen infinitos números primos}.}
$$


### 62

En la prueba de Euclides sólo se necesita que

$$
N=p_1\cdots p_k+1>1
$$

tenga **algún divisor primo** $q$. No necesitamos que $N$ sea primo.

Un ejemplo clásico es

$$
2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031.
$$

Este número es compuesto:

$$
30031=59\cdot509.
$$

Sin embargo, ni $59$ ni $509$ pertenece a la lista

$$
2,3,5,7,11,13.
$$

En general, cualquier divisor primo $q$ de $N$ no puede coincidir con ninguno de los $p_j$, porque si $q=p_j$, entonces dividiría tanto al producto $p_1\cdots p_k$ como a $N$, y por tanto dividiría a su diferencia $1$.

Así, la prueba funciona aunque $N$ sea compuesto.


### 63

Sí: bajo la hipótesis explícita

$$
N=p_1p_2\cdots p_k-1>1,
$$

el mismo mecanismo produce un primo fuera de la colección.

Como $N>1$, existe un primo $q$ tal que

$$
q\mid N.
$$

Si $q$ coincidiera con alguno de los $p_j$, entonces $q$ dividiría al producto

$$
P=p_1p_2\cdots p_k
$$

y también a

$$
N=P-1.
$$

Por tanto,

$$
q\mid P-(P-1)=1,
$$

imposible.

Así, cualquier divisor primo de $N$ queda fuera de la colección inicial.

La condición $N>1$ es esencial. Por ejemplo, con la colección formada sólo por $2$ se obtiene $2-1=1$, que no tiene divisor primo. Pero ese caso está excluido por el enunciado.


### 64

Demostramos la afirmación por contraposición.

El criterio ya establecido dice:

$$
n\text{ compuesto}
\Longrightarrow
\exists p\text{ primo},
\quad p\le\sqrt n,
\quad p\mid n.
$$

Su contraposición es

$$
\left(\text{ningún primo }p\le\sqrt n\text{ divide a }n\right)
\Longrightarrow
n\text{ no es compuesto}.
$$

Como $n>1$, si no es compuesto debe ser primo. Por tanto,

$$
\boxed{n\text{ es primo}.}
$$

No hace falta probar divisibilidad por números compuestos: si un compuesto dividiera a $n$, alguno de sus divisores primos también dividiría a $n$. El control sobre los primos ya captura todas las posibles obstrucciones.

## I. Potencias perfectas y diagnóstico


### 65

Sea

$$
n=\prod_p p^{\alpha_p}>0.
$$

Supongamos primero que $n$ es un cuadrado perfecto. Entonces existe $m>0$ tal que

$$
n=m^2.
$$

Escribimos

$$
m=\prod_p p^{\beta_p}.
$$

Entonces

$$
n=m^2=\prod_p p^{2\beta_p}.
$$

Por unicidad de la factorización prima,

$$
\alpha_p=2\beta_p
$$

para todo primo $p$. Por tanto, todos los exponentes $\alpha_p$ son pares.

Recíprocamente, supongamos que cada $\alpha_p$ es par. Escribimos

$$
\alpha_p=2\beta_p
$$

con $\beta_p\ge0$. Entonces

$$
n=\prod_p p^{2\beta_p}
=
\left(\prod_p p^{\beta_p}\right)^2.
$$

Así $n$ es un cuadrado perfecto.

Por tanto,

$$
\boxed{n\text{ es cuadrado perfecto}
\iff
\alpha_p\text{ es par para todo }p.}
$$


### 66

Sea

$$
n=\prod_p p^{\alpha_p}>0.
$$

Si $n$ es un cubo perfecto, existe $m>0$ con

$$
n=m^3.
$$

Escribiendo

$$
m=\prod_p p^{\beta_p},
$$

obtenemos

$$
n=\prod_p p^{3\beta_p}.
$$

Por unicidad,

$$
\alpha_p=3\beta_p,
$$

de modo que

$$
3\mid\alpha_p
$$

para todo primo $p$.

Recíprocamente, si cada $\alpha_p$ es múltiplo de $3$, escribimos

$$
\alpha_p=3\beta_p
$$

y entonces

$$
n=
\prod_p p^{3\beta_p}
=
\left(\prod_p p^{\beta_p}\right)^3.
$$

Luego

$$
\boxed{n\text{ es cubo perfecto}
\iff
3\mid\alpha_p\text{ para todo }p.}
$$


### 67

Sea $k\ge2$ y

$$
n=\prod_p p^{\alpha_p}>0.
$$

Si $n$ es una $k$-ésima potencia perfecta, existe $m>0$ tal que

$$
n=m^k.
$$

Escribiendo

$$
m=\prod_p p^{\beta_p},
$$

se obtiene

$$
n=\prod_p p^{k\beta_p}.
$$

Por unicidad de factorización,

$$
\alpha_p=k\beta_p,
$$

y por tanto

$$
k\mid\alpha_p
$$

para todo primo $p$.

Recíprocamente, si

$$
k\mid\alpha_p
$$

para todo $p$, escribimos

$$
\alpha_p=k\beta_p.
$$

Entonces

$$
n=\prod_p p^{k\beta_p}
=
\left(\prod_p p^{\beta_p}\right)^k.
$$

Así,

$$
\boxed{n\text{ es una }k\text{-ésima potencia perfecta}
\iff
k\mid\alpha_p\text{ para todo primo }p.}
$$


### 68

Consideremos

$$
N_1=2^6 3^{12}.
$$

Los exponentes $6$ y $12$ son pares, múltiplos de $3$ y múltiplos de $6$. Por tanto, $N_1$ es cuadrado, cubo y sexta potencia perfecta.

Ahora

$$
N_2=2^4 3^6 5^2.
$$

Todos los exponentes son pares, así que $N_2$ es cuadrado. Pero $4$ y $2$ no son múltiplos de $3$, de modo que no es cubo. Tampoco todos son múltiplos de $6$, así que no es sexta potencia.

Finalmente,

$$
N_3=2^{12}3^{18}5^6.
$$

Los exponentes $12,18,6$ son todos múltiplos de $6$. En particular son pares y múltiplos de $3$. Por tanto, $N_3$ es cuadrado, cubo y sexta potencia perfecta.

En resumen:

$$
\boxed{
\begin{array}{c|ccc}
&\text{cuadrado}&\text{cubo}&\text{sexta potencia}\\
N_1&\text{sí}&\text{sí}&\text{sí}\\
N_2&\text{sí}&\text{no}&\text{no}\\
N_3&\text{sí}&\text{sí}&\text{sí}
\end{array}}
$$


### 69

Escribamos

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Como

$$
\gcd(a,b)=1,
$$

para cada primo $p$ se cumple

$$
\min(\alpha_p,\beta_p)=0.
$$

Es decir, un primo no puede aparecer con exponente positivo en ambos factores.

Como $ab$ es un cubo perfecto,

$$
3\mid(\alpha_p+\beta_p)
$$

para todo primo $p$.

Pero, por coprimalidad, para cada $p$ uno de los exponentes $\alpha_p,\beta_p$ es $0$. Por tanto, si $\alpha_p>0$, entonces $\beta_p=0$ y

$$
3\mid\alpha_p.
$$

Análogamente, si $\beta_p>0$, entonces

$$
3\mid\beta_p.
$$

Así todos los exponentes de $a$ son múltiplos de $3$ y todos los exponentes de $b$ también. Por el criterio de potencias perfectas,

$$
\boxed{a\text{ y }b\text{ son cubos perfectos}.}
$$

La coprimalidad se usa exactamente para impedir que un exponente total múltiplo de $3$ se reparta entre los dos factores.


### 70

La afirmación sin hipótesis adicionales es falsa. Por ejemplo,

$$
2\cdot8=16=4^2,
$$

pero ni $2$ ni $8$ es cuadrado perfecto.

Una hipótesis suficiente es

$$
\gcd(a,b)=1.
$$

En efecto, escribimos

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Si $ab$ es cuadrado, entonces

$$
\alpha_p+\beta_p
$$

es par para todo primo $p$.

La coprimalidad implica que, para cada $p$, al menos uno de $\alpha_p,\beta_p$ es $0$. Por tanto, el exponente no nulo, si existe, debe ser él mismo par. Así todos los exponentes de $a$ y todos los de $b$ son pares.

En consecuencia,

$$
\boxed{\gcd(a,b)=1,
\ ab\text{ cuadrado}
\Longrightarrow
a,b\text{ cuadrados}.}
$$


### 71

**a)**

$$
p\mid ab\Longrightarrow p\mid a\text{ o }p\mid b
$$

para $p$ primo es exactamente el **lema de Euclides**. La primalidad es la hipótesis que permite aplicarlo.

**b)** La afirmación

$$
a\mid b
\Longrightarrow
\alpha_p\le\beta_p
$$

para todos los exponentes primos depende de la **unicidad de la factorización**. Sin unicidad no podríamos identificar de manera bien definida esos exponentes.

**c)** La afirmación

$$
ab\text{ cuadrado}
\Longrightarrow
a,b\text{ cuadrados}
$$

es falsa. Un contraejemplo es

$$
2\cdot8=16.
$$

Se corrige añadiendo, por ejemplo,

$$
\gcd(a,b)=1.
$$

Entonces la conclusión sí se obtiene mediante unicidad de factorización y paridad de exponentes.

**d)**

$$
p\mid a^m\Longrightarrow p\mid a
$$

para $p$ primo se deduce del **lema de Euclides**, aplicado al producto de $m$ copias de $a$.

Así, la herramienta dominante es: lema de Euclides en a) y d), unicidad de factorización en b), y ninguna en c) tal como está formulada porque es falsa.


### 72

La frase “extraemos raíz cuadrada y raíz cúbica” no es una demostración aritmética porque presupone, sin justificarlo, que esas raíces son enteras y que la igualdad fuerza una parametrización común.

El plan correcto usa factorización única y separa primero los casos de dominio. Si $a=0$, la igualdad fuerza $b=0$ y se elige $c=0$. Si $a\ne0$, entonces $b^3=a^2>0$, de modo que $b>0$. Definimos $A=|a|>0$ y $\varepsilon\in\{1,-1\}$ por $a=\varepsilon A$.

Escribimos

$$
A=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Entonces

$$
a^2=b^3
$$

implica, por unicidad de la factorización,

$$
2\alpha_p=3\beta_p
$$

para todo primo $p$.

Como

$$
\gcd(2,3)=1,
$$

la igualdad anterior obliga a

$$
3\mid\alpha_p
\qquad\text{y}\qquad
2\mid\beta_p.
$$

El siguiente paso sería escribir

$$
\alpha_p=3\gamma_p,
\qquad
\beta_p=2\gamma_p
$$

para una misma familia de exponentes $\gamma_p$, construir

$$
C=\prod_p p^{\gamma_p},
$$

y verificar que $A=C^3$ y $b=C^2$. Finalmente se elige $c=\varepsilon C$: como $\varepsilon^3=\varepsilon$ y $\varepsilon^2=1$, quedan $a=c^3$ y $b=c^2$. Éstas son las verificaciones que completarían el plan; no se ha supuesto positividad de $a$ en la consigna.

Ése es el argumento aritmético que debe sustituir la extracción informal de raíces.

## M. Problemas avanzados tipo prueba


### 73

Sea $p>1$. Probaremos

$$
p\text{ es primo}
\iff
p\text{ es irreducible en }\mathbb Z.
$$

#### Primo implica irreducible

Supongamos que $p$ es primo y que

$$
p=ab,
\qquad a,b\in\mathbb Z.
$$

Tomamos valores absolutos:

$$
p=|a||b|.
$$

Como $|a|$ es un divisor positivo de $p$ y $p$ es primo,

$$
|a|=1
\quad\text{o}\quad
|a|=p.
$$

Si $|a|=1$, entonces

$$
a=\pm1,
$$

y $a$ es una unidad.

Si $|a|=p$, entonces de

$$
p=|a||b|=p|b|
$$

se sigue

$$
|b|=1,
$$

de modo que $b=\pm1$ es una unidad.

En cualquier factorización $p=ab$, al menos uno de los factores es una unidad. Como además $p\ne0$ y $p$ no es unidad porque $p>1$, concluimos que $p$ es irreducible.

#### Irreducible implica primo

Supongamos ahora que $p$ es irreducible y sea $d>0$ un divisor de $p$. Entonces existe $q\in\mathbb Z$ tal que

$$
p=dq.
$$

Como $p>0$ y $d>0$, necesariamente $q>0$.

Por irreducibilidad, uno de los factores $d$ o $q$ debe ser una unidad. Pero ambos son positivos, así que la única unidad positiva posible es $1$.

- Si $d=1$, tenemos el divisor trivial inferior.
- Si $q=1$, entonces $d=p$.

Por tanto, los únicos divisores positivos de $p$ son

$$
1\quad\text{y}\quad p.
$$

Luego $p$ es primo.

El papel de las unidades $\pm1$ es esencial en la dirección primo $\Rightarrow$ irreducible: las factorizaciones con signos, como

$$
p=(-1)(-p),
$$

son perfectamente legítimas en $\mathbb Z$ y deben ser consideradas triviales porque $-1$ es una unidad.

Concluimos

$$
\boxed{p\text{ primo}\iff p\text{ irreducible en }\mathbb Z.}
$$


### 74

Sea $P(n)$ la afirmación:

> todo entero $n>1$ puede escribirse como producto finito de números primos.

Demostraremos $P(n)$ por inducción fuerte sobre $n$.

#### Base

Para $n=2$, el número $2$ es primo. Por tanto,

$$
2=2
$$

es ya una factorización prima.

#### Paso inductivo

Fijemos $n>2$ y supongamos que $P(m)$ es verdadera para todo entero $m$ con

$$
2\le m<n.
$$

Debemos demostrar $P(n)$.

Hay dos casos.

**Caso 1: $n$ es primo.** Entonces

$$
n=n
$$

es un producto de un solo primo, y terminamos.

**Caso 2: $n$ es compuesto.** Por definición existen enteros positivos $a,b$ tales que

$$
n=ab,
$$

con

$$
1<a<n,
\qquad
1<b<n.
$$

Estas desigualdades son el punto que habilita la inducción fuerte: ambos factores están estrictamente por debajo de $n$.

Por la hipótesis inductiva existen primos

$$
p_1,\ldots,p_r
$$

y

$$
q_1,\ldots,q_s
$$

tales que

$$
a=p_1p_2\cdots p_r,
$$

$$
b=q_1q_2\cdots q_s.
$$

Multiplicando,

$$
n=ab
=p_1\cdots p_r q_1\cdots q_s.
$$

Así $n$ también es producto finito de primos.

Por inducción fuerte, todo entero $n>1$ admite una factorización prima.

#### Qué se ha probado

La prueba anterior demuestra **existencia**: garantiza que al menos una factorización prima existe para cada $n>1$.

No demuestra **unicidad**, porque nunca compara dos posibles factorizaciones de un mismo entero. Para esa segunda parte hace falta un mecanismo adicional: el lema de Euclides, que permitirá forzar que un primo presente en una factorización también aparezca en la otra.


### 75

Sea $p$ primo y supongamos

$$
p\mid ab.
$$

Queremos demostrar

$$
p\mid a
\quad\text{o}\quad
p\mid b.
$$

Si $p\mid a$, ya hemos terminado.

Supongamos entonces

$$
p\nmid a.
$$

Como $p$ es primo, sus únicos divisores positivos son $1$ y $p$. Todo divisor común positivo de $p$ y $a$ debe dividir a $p$. Pero $p$ no divide a $a$, de modo que el MCD no puede ser $p$. Por tanto,

$$
\gcd(p,a)=1.
$$

Por Bézout existen $x,y\in\mathbb Z$ tales que

$$
px+ay=1.
$$

Multiplicamos por $b$:

$$
pbx+aby=b.
$$

Como

$$
p\mid pbx
$$

y, por hipótesis,

$$
p\mid ab,
$$

también

$$
p\mid aby.
$$

Por cierre bajo sumas,

$$
p\mid(pbx+aby)=b.
$$

Así, si $p$ no divide a $a$, necesariamente divide a $b$. En todos los casos,

$$
\boxed{p\mid ab\Longrightarrow p\mid a\text{ o }p\mid b.}
$$

Esta prueba no usa factorización única. Parte exclusivamente de primalidad y de Bézout/cancelación coprima de C15.

La afirmación falla para un divisor compuesto arbitrario. Por ejemplo,

$$
6\mid2\cdot3,
$$

pero

$$
6\nmid2,
\qquad
6\nmid3.
$$

El número compuesto $6$ puede “repartir” sus factores primos entre factores distintos del producto.


### 76

Supongamos que $n>1$ admite dos factorizaciones en primos:

$$
n=p_1p_2\cdots p_r
=q_1q_2\cdots q_s.
$$

Demostraremos que ambas listas coinciden salvo orden.

#### Paso 1: localizar $p_1$ en la segunda factorización

Como

$$
p_1\mid n
$$

y

$$
n=q_1q_2\cdots q_s,
$$

tenemos

$$
p_1\mid q_1q_2\cdots q_s.
$$

La versión finita del lema de Euclides implica que existe algún índice $j$ tal que

$$
p_1\mid q_j.
$$

Pero $q_j$ es primo. Como $p_1>1$, el único modo de que $p_1$ divida a $q_j$ es

$$
p_1=q_j.
$$

Reordenamos la segunda factorización y suponemos

$$
p_1=q_1.
$$

#### Paso 2: cancelar

La igualdad inicial se convierte en

$$
p_1p_2\cdots p_r
=p_1q_2\cdots q_s.
$$

Como $p_1\ne0$, cancelamos en $\mathbb Z$:

$$
p_2\cdots p_r=q_2\cdots q_s.
$$

#### Paso 3: repetir

Aplicamos el mismo argumento a $p_2$. Debe coincidir con uno de los primos restantes del lado derecho. Reordenamos y cancelamos de nuevo.

Repitiendo finitamente, hacemos corresponder uno a uno los factores de ambas listas.

#### Paso 4: demostrar que las longitudes coinciden

Supongamos, por ejemplo, que $r<s$. Después de cancelar $p_1,\ldots,p_r$, obtendríamos

$$
1=q_{r+1}q_{r+2}\cdots q_s.
$$

Pero cada $q_j>1$, de modo que

$$
q_{r+1}q_{r+2}\cdots q_s>1,
$$

contradicción.

Del mismo modo, $s<r$ es imposible. Por tanto,

$$
r=s.
$$

Tras una reordenación,

$$
p_i=q_i
$$

para todo $i$.

Concluimos que la factorización prima es única salvo el orden de los factores.

Los únicos ingredientes sustantivos usados fueron:

- el lema de Euclides para localizar un factor primo dentro de un producto;
- la primalidad del factor encontrado para convertir divisibilidad en igualdad;
- la cancelación ordinaria en $\mathbb Z$;
- la finitud de ambas listas.


### 77

Sean

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Sólo finitos exponentes son distintos de $0$.

#### Divisibilidad

Supongamos primero

$$
\alpha_p\le\beta_p
$$

para todo $p$. Definimos

$$
c=\prod_p p^{\beta_p-\alpha_p}.
$$

Entonces

$$
ac=
\prod_p p^{\alpha_p}
\prod_p p^{\beta_p-\alpha_p}
=
\prod_p p^{\beta_p}
=b.
$$

Por tanto,

$$
a\mid b.
$$

Recíprocamente, si $a\mid b$, existe $c>0$ con $b=ac$. Escribimos

$$
c=\prod_p p^{\gamma_p}.
$$

Entonces

$$
b=ac=\prod_p p^{\alpha_p+\gamma_p}.
$$

Por **unicidad de la factorización prima**,

$$
\beta_p=\alpha_p+\gamma_p,
$$

y por tanto

$$
\alpha_p\le\beta_p.
$$

Así,

$$
\boxed{a\mid b
\iff
\alpha_p\le\beta_p\text{ para todo }p.}
$$

#### MCD

Definamos

$$
d=\prod_p p^{\min(\alpha_p,\beta_p)}.
$$

Como los mínimos no superan a ninguno de los exponentes originales,

$$
d\mid a,
\qquad
d\mid b.
$$

Si

$$
e=\prod_p p^{\varepsilon_p}
$$

es cualquier divisor común, entonces

$$
\varepsilon_p\le\alpha_p,
\qquad
\varepsilon_p\le\beta_p,
$$

por lo que

$$
\varepsilon_p\le\min(\alpha_p,\beta_p).
$$

Luego $e\mid d$. Así,

$$
\boxed{\gcd(a,b)=\prod_p p^{\min(\alpha_p,\beta_p)}.}
$$

#### MCM

Definimos

$$
m=\prod_p p^{\max(\alpha_p,\beta_p)}.
$$

Como

$$
\alpha_p,\beta_p\le\max(\alpha_p,\beta_p),
$$

tenemos

$$
a\mid m,
\qquad
b\mid m.
$$

Sea

$$
M=\prod_p p^{\mu_p}
$$

cualquier múltiplo común. Entonces

$$
\alpha_p\le\mu_p,
\qquad
\beta_p\le\mu_p,
$$

así que

$$
\max(\alpha_p,\beta_p)\le\mu_p.
$$

Por consiguiente,

$$
m\mid M.
$$

Así,

$$
\boxed{\operatorname{lcm}(a,b)=\prod_p p^{\max(\alpha_p,\beta_p)}.}
$$

#### Producto MCD–MCM

Para enteros no negativos $r,s$,

$$
\min(r,s)+\max(r,s)=r+s.
$$

Aplicando primo por primo,

$$
\gcd(a,b)\operatorname{lcm}(a,b)
=
\prod_p p^{\min(\alpha_p,\beta_p)+\max(\alpha_p,\beta_p)}
$$

$$
=
\prod_p p^{\alpha_p+\beta_p}
=ab.
$$

Por tanto,

$$
\boxed{\gcd(a,b)\operatorname{lcm}(a,b)=ab.}
$$

La unicidad de factorización interviene al identificar los exponentes de un producto con las sumas de exponentes y al garantizar que las representaciones $\alpha_p,\beta_p,\gamma_p$ están bien definidas de manera única.


### 78

Supongamos, por contradicción, que existen sólo finitos primos. Los enumeramos como

$$
p_1,p_2,\ldots,p_k.
$$

Formamos

$$
N=p_1p_2\cdots p_k+1.
$$

Como $N>1$, el teorema de la sección 16.4 garantiza que existe algún primo $q$ tal que

$$
q\mid N.
$$

No necesitamos saber si $N$ es primo o compuesto.

Supongamos que $q$ perteneciera a la lista. Entonces, para algún $j$,

$$
q=p_j.
$$

En ese caso,

$$
q\mid p_1p_2\cdots p_k.
$$

Además, por construcción,

$$
q\mid N.
$$

Por tanto, $q$ divide la diferencia:

$$
q\mid
\left(N-p_1p_2\cdots p_k\right).
$$

Pero

$$
N-p_1p_2\cdots p_k=1.
$$

Así,

$$
q\mid1,
$$

imposible porque $q>1$.

Por consiguiente, el divisor primo $q$ de $N$ no está en la lista inicial. Esto contradice que la lista contenía todos los primos.

Luego existen infinitos números primos.

La afirmación

$$
N\text{ es primo}
$$

no se necesita en ningún paso. Además, es falsa en general. Por ejemplo,

$$
2\cdot3\cdot5\cdot7\cdot11\cdot13+1
=30031
=59\cdot509.
$$

El argumento sigue funcionando porque basta con que $N$ tenga **algún divisor primo nuevo**.


### 79

Sean $a,b>0$ con

$$
\gcd(a,b)=1
$$

y supongamos que

$$
ab
$$

es un cuadrado perfecto.

Escribamos las factorizaciones primas

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Entonces

$$
ab=\prod_p p^{\alpha_p+\beta_p}.
$$

Como $ab$ es cuadrado perfecto, el criterio de la sección 16.14 implica

$$
\alpha_p+\beta_p
$$

es un entero par para todo primo $p$.

Ahora usamos la coprimalidad. La condición

$$
\gcd(a,b)=1
$$

es equivalente a

$$
\min(\alpha_p,\beta_p)=0
$$

para todo primo $p$. Así, para cada $p$, al menos uno de los dos exponentes es $0$.

- Si $\alpha_p>0$, entonces $\beta_p=0$. Como $\alpha_p+\beta_p=\alpha_p$ es par, $\alpha_p$ es par.
- Si $\beta_p>0$, entonces $\alpha_p=0$. Como $\alpha_p+\beta_p=\beta_p$ es par, $\beta_p$ es par.

Por tanto, todos los exponentes primos de $a$ son pares y todos los exponentes primos de $b$ también.

Existen entonces enteros no negativos $r_p,s_p$ tales que

$$
\alpha_p=2r_p,
\qquad
\beta_p=2s_p.
$$

Definimos

$$
x=\prod_p p^{r_p},
\qquad
y=\prod_p p^{s_p}.
$$

Entonces

$$
a=x^2,
\qquad
b=y^2.
$$

Así,

$$
\boxed{a\text{ y }b\text{ son cuadrados perfectos}.}
$$

La coprimalidad es indispensable. Si la eliminamos, un mismo primo puede aportar un exponente impar a cada factor y producir un exponente total par. Por ejemplo,

$$
2\cdot8=16=4^2,
$$

pero ni $2$ ni $8$ es cuadrado perfecto. Aquí el primo $2$ aparece con exponentes $1$ y $3$, ambos impares, cuya suma es $4$.


### 80

Sean

$$
a,b,m,n>0,
$$

con

$$
\gcd(m,n)=1
$$

y

$$
a^m=b^n.
$$

Queremos demostrar que existe $c>0$ tal que

$$
a=c^n,
\qquad
b=c^m.
$$

#### 1. Comparar exponentes primo a primo

Escribimos las factorizaciones canónicas

$$
a=\prod_p p^{\alpha_p},
\qquad
b=\prod_p p^{\beta_p}.
$$

Entonces

$$
a^m=\prod_p p^{m\alpha_p},
$$

y

$$
b^n=\prod_p p^{n\beta_p}.
$$

Como

$$
a^m=b^n,
$$

la unicidad de la factorización prima obliga a que, para cada primo $p$,

$$
\boxed{m\alpha_p=n\beta_p.}
$$

Éste es el punto exacto donde interviene el teorema fundamental de la aritmética.

#### 2. Usar la coprimalidad de $m$ y $n$

De

$$
m\alpha_p=n\beta_p
$$

se sigue

$$
n\mid m\alpha_p.
$$

Como

$$
\gcd(m,n)=1,
$$

la cancelación coprima de C15 da

$$
\boxed{n\mid\alpha_p.}
$$

Por tanto existe $\gamma_p\ge0$ tal que

$$
\alpha_p=n\gamma_p.
$$

Análogamente,

$$
m\mid n\beta_p.
$$

Como $\gcd(m,n)=1$,

$$
\boxed{m\mid\beta_p.}
$$

Existe entonces $\delta_p\ge0$ tal que

$$
\beta_p=m\delta_p.
$$

Sustituyendo en

$$
m\alpha_p=n\beta_p,
$$

obtenemos

$$
m(n\gamma_p)=n(m\delta_p).
$$

Como $mn>0$, cancelamos:

$$
\gamma_p=\delta_p.
$$

Llamemos a este exponente común simplemente $\gamma_p$. Así,

$$
\alpha_p=n\gamma_p,
\qquad
\beta_p=m\gamma_p.
$$

#### 3. Construir el entero común

Definimos

$$
c=\prod_p p^{\gamma_p}.
$$

Este producto es finito porque sólo finitos primos aparecen en $a$ o en $b$.

Entonces

$$
c^n
=
\prod_p p^{n\gamma_p}
=
\prod_p p^{\alpha_p}
=a.
$$

Del mismo modo,

$$
c^m
=
\prod_p p^{m\gamma_p}
=
\prod_p p^{\beta_p}
=b.
$$

Por tanto,

$$
\boxed{a=c^n,
\qquad
b=c^m.}
$$

#### Dependencias exactas

La prueba usa dos herramientas distintas:

1. **Unicidad de factorización**, para pasar de la igualdad global
   $$
   a^m=b^n
   $$
   a las igualdades locales
   $$
   m\alpha_p=n\beta_p
   $$
   para cada primo $p$.
2. **Cancelación coprima de C15**, para deducir de
   $$
   n\mid m\alpha_p,
   \qquad
   \gcd(m,n)=1
   $$
   que
   $$
   n\mid\alpha_p,
   $$
   y simétricamente $m\mid\beta_p$.

El resultado muestra cómo una ecuación entre potencias se convierte, gracias al teorema fundamental de la aritmética, en un sistema independiente de ecuaciones lineales entre exponentes primos.

## N. Hipótesis, exponentes y certificados


### 81

Si $d$ es primo, la propiedad es el lema de Euclides, ya demostrado desde Bézout. Recíprocamente, supongamos que la propiedad vale y que $d$ no es primo. Como $d>1$, es compuesto: $d=uv$ con $1<u,v<d$. Tomamos $a=u$, $b=v$. Entonces $d\mid ab$ con testigo uno, pero $d\nmid u$ y $d\nmid v$: una igualdad $u=dt$ con $u>0$ exigiría $t\ge1$ y, por tanto, $u\ge d$, contradicción. Lo mismo sucede con $v$.

Esto contradice la propiedad universal. Por tanto $d$ es primo. La fabricación funciona incluso si $u=v$, como en $d=9=3\cdot3$. No se presupone una factorización única ni que los factores elegidos sean coprimos. La propiedad sobre todos los productos caracteriza al divisor; un producto particular no bastaría para ello.


### 82

Para cada entero $r\ge1$, tomamos $a=p^r$ y $b=q$. El número $d=pq$ divide a $ab=p^rq$ con testigo $p^{r-1}$. Si $q$ dividiera a $p^r$, el lema de Euclides para potencias daría $q\mid p$, imposible por ser primos distintos. Como todo divisor común positivo de $p^r$ y $q$ es uno o $q$, resulta $\gcd(a,b)=1$.

No ocurre $d\mid a$: implicaría $q\mid p^r$. Tampoco $d\mid b=q$, porque $d=pq>q>0$. Las primeras coordenadas $p^r$ son distintas, así que obtenemos infinitos ejemplos. La coprimalidad entre los factores del producto no permite cancelar el divisor completo.

Para reparar la inferencia, suponemos $\gcd(d,a)=1$. Bézout da $dx+ay=1$ con $x,y\in\mathbb Z$. Multiplicar por $b$ entrega $dbx+aby=b$. Ambos términos del lado izquierdo son divisibles por $d$, el segundo por la hipótesis $d\mid ab$. Luego $d\mid b$. Esta reparación se deduce de C15 y no requiere que $d$ sea primo.


### 83

El producto es $p^{r+s}$, por lo que es una $k$-ésima potencia exactamente cuando $k\mid r+s$. Cada factor lo es exactamente cuando su exponente es múltiplo de $k$, incluido el exponente cero. Dividimos $r=ku+i$ y $s=kv+j$, con $u,v\ge0$ y $0\le i,j<k$.

Para que ninguno sea potencia necesitamos $i,j\ne0$. Entonces $2\le i+j\le2k-2$; el único múltiplo de $k$ posible en ese intervalo es $k$. Por tanto la clasificación completa es

$$
r=ku+i,\qquad s=kv+k-i,\qquad u,v\ge0,\quad 1\le i\le k-1.
$$

Recíprocamente, esas expresiones dan exponentes no divisibles por $k$ y suma $k(u+v+1)$, así que el producto es $(p^{u+v+1})^k$. La división entera de una pareja arbitraria probó exhaustividad. Fijando $i=1$, $v=0$ y variando $u$ se obtienen infinitos ejemplos. Comparten el primo $p$, de modo que falla precisamente la coprimalidad que permite separar las potencias de un producto.


### 84

La igualdad es cierta: ambos productos valen 84. La segunda lista no es una factorización prima porque $14=2\cdot7$ es compuesto. Sustituir ese factor produce $2\cdot3\cdot2\cdot7$. Reordenamos para localizar un dos y cancelarlo frente al primero de la lista izquierda; queda $2\cdot3\cdot7=3\cdot2\cdot7$. Reordenamos otra vez y cancelamos el segundo dos; queda $3\cdot7=3\cdot7$. Cancelamos tres y después siete, y obtenemos $1=1$.

Estas operaciones sólo usan identidades concretas, reordenación y cancelación de factores comunes no nulos. Cada primo de la lista reparada queda emparejado, contando repeticiones. No se usó la unicidad como premisa. En la comparación general, el lema de Euclides permite localizar cada primo en la lista contraria. Si al vaciar un lado quedaran $h\ge1$ primos en el otro, su producto sería al menos $2^h>1$, incompatible con la igualdad restante. Una longitud distinta de listas no primas no contradice el teorema.


### 85

El conjunto de divisores positivos propios de $n$ es no vacío, porque contiene uno, y es finito, porque está contenido en $\{1,\ldots,n-1\}$. Por eso existe $D$. El cociente $q=n/D$ es un entero positivo mayor que uno.

Si $q$ fuera compuesto, escribiríamos $q=uv$ con $1<u,v<q$. Entonces $n=(Du)v$, de modo que $Du$ sería divisor de $n$. Además $Du>D$, porque $u>1$, y $Du<n$, porque $v>1$. Esto contradice la elección de $D$. Por tanto $q$ es primo. Sólo se usó la definición de compuesto y maximalidad entre divisores.

Si $D=1$, la conclusión dice que $n$ mismo es primo. Recíprocamente, si $n$ es primo, su único divisor positivo propio es uno. El número $D$ no necesita ser primo: para $n=36$, el mayor divisor propio es dieciocho, pues $36/D$ es entero al menos dos y obliga a $D\le18$; dieciocho efectivamente divide a 36. Aquí el cociente es dos y $D=18$ es compuesto.


### 86

Como $N>1$, la existencia de un divisor primo de [§16.4](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md#apm-c16-s04) proporciona $q$ primo con $q\mid N$. Si $q\le n$, el entero positivo $q$ aparece entre los factores $1,2,\ldots,n$; por ello $q\mid n!$. Entonces divide también la diferencia $N-n!=1$, imposible para un primo mayor que uno. Luego $q>n$.

Este razonamiento se aplica a cualquier divisor primo de $N$, no sólo a uno seleccionado. No requiere factorizar completamente $N$, ni conocer unicidad, ni declarar primo a $N$. Para $n=5$, $N=120+1=121=11\cdot11$ es compuesto. Once es primo: los únicos primos no mayores que su raíz son dos y tres, que no lo dividen. Tenemos $11>5$ y $11\mid121$, como exige el argumento. El factorial organiza todos los posibles divisores primos pequeños; la diferencia uno los descarta simultáneamente.


### 87

Escribimos $C$ en factores primos. Para que $NC$ sea cubo, el exponente de dos en $C$ debe tener forma $2+3u$, el de tres forma $1+3v$ y el de siete forma $1+3w$, con $u,v,w\ge0$. Todo otro primo sólo puede aparecer en $C$ con exponente múltiplo de tres. Estas condiciones proceden de exigir que $7+\beta_2$, $5+\beta_3$, $2+\beta_7$ y los exponentes restantes sean múltiplos de tres.

Por tanto todos los multiplicadores, y sólo ellos, son

$$
C=2^2\cdot3\cdot7\,t^3=84t^3,\qquad t\in\mathbb Z_{>0}.
$$

La forma se obtiene reuniendo los exponentes excedentes divididos por tres; su necesidad demuestra exhaustividad. Recíprocamente, $NC=2^9\cdot3^6\cdot7^3t^3=(2^3\cdot3^2\cdot7\,t)^3=(504t)^3$. Así cada candidato funciona. Como $t\ge1$, $C\ge84$, con igualdad para $t=1$. El menor multiplicador es 84, y la raíz positiva de cada producto es $504t$. La minimalidad queda probada, no sólo exhibida.


### 88

El criterio de exponentes exige que $k$ divida simultáneamente a doce, dieciocho y treinta. Sus divisores comunes positivos son los divisores de seis: $1,2,3,6$. Se puede comprobar sin una búsqueda abierta: cualquier divisor común divide $18-12=6$, y cualquier divisor de seis divide las tres entradas. Con $k\ge2$, quedan exactamente $2,3,6$.

Las raíces positivas construidas son, respectivamente, $2^6\cdot3^9\cdot5^{15}$, $2^4\cdot3^6\cdot5^{10}$ y $2^2\cdot3^3\cdot5^5$. Elevar cada una al exponente correspondiente recupera $N$ por las leyes de potencias. No existen otros exponentes porque ya clasificamos todos los divisores comunes.

Para uno, todos los exponentes primos son cero y cualquier entero $k\ge2$ divide a cero. Por ello $1=1^k$ para todos esos $k$. No debemos buscar un mayor exponente finito ni aplicar la lista anterior: no hay exponentes positivos que limiten $k$.


### 89

Los exponentes de $N^h$ son $6h,9h,15h$. Se necesita y basta que doce divida a los tres. Si esto ocurre, doce divide a la diferencia $9h-6h=3h$, por lo que $3h=12t$ para algún entero y cancelar tres da $h=4t$. Como $h\ge1$, $t\ge1$.

Recíprocamente, con $h=4t$, los exponentes son $24t,36t,60t$, todos divisibles por doce. La raíz positiva es $R=2^{2t}\cdot3^{3t}\cdot5^{5t}$, y $R^{12}=N^{4t}$. Por tanto la clasificación exhaustiva es $h=4t$, $t\in\mathbb Z_{>0}$. La necesidad empezó con un exponente arbitrario que cumple la condición, y la construcción prueba suficiencia. Probar solamente los primeros valores de $h$ no establecería esta familia completa.


### 90

Como $15^2=225<251<256=16^2$, todos los primos no mayores que su raíz son $2,3,5,7,11,13$. Las divisiones son

$$
251=2\cdot125+1=3\cdot83+2=5\cdot50+1,
$$

$$
251=7\cdot35+6=11\cdot22+9=13\cdot19+4.
$$

Los restos no nulos descartan todos los posibles divisores primos pequeños; por [§16.12](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md#apm-c16-s12), 251 es primo. La lista de primos hasta quince es completa: los otros enteros entre dos y quince son compuestos, como se comprueba con factores dos, tres, cinco o siete.

Para 253 basta la identidad $253=11\cdot23$, cuyos factores son positivos mayores que uno y menores que 253. Esto ya certifica composición; ni siquiera hace falta probar que ambos factores sean primos. La primalidad requiere descartar exhaustivamente los divisores que podrían existir. La composición requiere un único testigo no trivial. No encontrar un divisor en unos pocos intentos no equivale al primer certificado.


### 91

Los controles informados descartan esos ocho primos, pero no completan el criterio. Tenemos $1000^2=1000000<1000003<1002001=1001^2$, de modo que deben descartarse todos los primos no mayores que mil. Los que aún faltan son exactamente los primos $p$ con $19<p\le1000$, empezando por 23. Por ejemplo, comprobar 23 también es necesario dentro de este método, y descartar sólo ese primo adicional seguiría sin cerrar el certificado.

No se concluye de este examen incompleto que $N$ sea compuesto: la ausencia de una prueba no determina el resultado. El problema pide evaluar el alcance del certificado, y con la información dada la primalidad queda sin certificar por el criterio elegido.

Para $1000005$, la igualdad $3\cdot333335=1000005$ exhibe dos factores positivos no triviales. Por tanto es compuesto y no requiere descartar más divisores. Ambos números son del mismo orden de tamaño, pero las obligaciones de prueba son distintas. Un factor hallado cierra composición; para este certificado de primalidad hace falta cubrir la lista completa hasta la barrera.


### 92

La primera afirmación es cierta: si un primo $p\le m$ dividiera a $m!+1$, también dividiría a $m!$ y a su diferencia uno. El salto hacia primalidad es inválido porque la barrera necesaria es $\sqrt{m!+1}$, que puede superar a $m$. Con $m=5$, $5!+1=121=11^2$ no tiene divisor primo no mayor que cinco, pero es compuesto.

Si se conoce $m!+1=ab$ con $1<a\le b$, entonces $a^2\le ab=m!+1$. Por [§16.4](algebra-para-matematicos-capitulo-16-numeros-primos-y-factorizacion.md#apm-c16-s04), $a$ tiene un divisor primo $q$. Así $q\le a\le\sqrt{m!+1}$ y $q\mid m!+1$. El argumento de la diferencia uno prueba además que $q>m$. Por tanto $m<q\le\sqrt{m!+1}$.

El resultado combina un certificado de composición con la exclusión simultánea de divisores pequeños. No usa una factorización única ni presupone que el cofactor sea primo. En el contraejemplo, $q=11$ cumple $5<11\le\sqrt{121}=11$: la desigualdad de la barrera permite igualdad y no debe sustituirse por una desigualdad estricta.

***

[← Capítulo 15](algebra-para-matematicos-capitulo-15-maximo-comun-divisor-y-algoritmo-de-euclides.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 17 →](algebra-para-matematicos-capitulo-17-congruencias-y-aritmetica-modular.md)

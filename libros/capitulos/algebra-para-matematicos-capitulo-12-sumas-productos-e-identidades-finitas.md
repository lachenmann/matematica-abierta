---
{
  "title": "Sumas, productos e identidades finitas",
  "description": "Capítulo 12 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0187",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C12",
  "editorial-id": "MA-BCH-APM-01-012",
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
    "MA-BCH-0186"
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

C11 enseñó a demostrar afirmaciones indexadas por los naturales. En muchos de esos argumentos aparecieron expresiones como

$$
1+2+\cdots+n,
$$

pero hasta ahora las tratamos principalmente como ejemplos para la inducción. En este capítulo cambia el centro de gravedad. Una suma finita deja de ser sólo una lista larga de términos y pasa a ser un objeto algebraico que podemos leer, transformar, reindexar y comparar con otras representaciones.

La misma idea se extenderá a productos finitos y a sumas dobles. El objetivo no es memorizar símbolos. Es adquirir una disciplina de manipulación que permita saber exactamente qué términos se están sumando, cuántas veces aparece cada uno y por qué una transformación conserva el valor de la expresión.

> **Una expresión indexada no se manipula por apariencia. Se transforma controlando simultáneamente índices, rangos y términos.**

***
## 12.1. De una lista de términos a una suma indexada {#apm-c12-s01}

Consideremos una lista finita

$$
a_1+a_2+\cdots+a_n.
$$

La notación sigma la escribe de manera compacta como

$$
\sum_{k=1}^{n} a_k.
$$

En esta expresión intervienen cuatro piezas distintas:

- el símbolo $\sum$, que indica una suma;
- el **índice** $k$;
- el **rango** $1\le k\le n$;
- el **sumando** $a_k$.

La notación no es meramente tipográfica. Indica una regla de generación: sustituimos sucesivamente $k=1,2,\ldots,n$ en el sumando y agregamos los resultados.

Por ejemplo,

$$
\sum_{k=2}^{5}(3k-1)
$$

significa

$$
(3\cdot2-1)+(3\cdot3-1)+(3\cdot4-1)+(3\cdot5-1),
$$

es decir,

$$
5+8+11+14.
$$

El índice no tiene por qué comenzar en $1$. También podemos escribir

$$
\sum_{j=0}^{4}2^j=1+2+4+8+16.
$$

Cuando el límite inferior supera al superior, adoptaremos la convención de que la suma es vacía y vale $0$. Esta convención permite formular identidades sin separar innecesariamente casos extremos.

***
## 12.2. Expandir y comprimir sumas {#apm-c12-s02}

Leer notación sigma exige poder ir en ambas direcciones.

### De sigma a forma expandida

Para

$$
\sum_{k=1}^{5}(2k-1),
$$

sustituimos $k=1,2,3,4,5$:

$$
1+3+5+7+9.
$$

Un error frecuente consiste en mirar sólo la fórmula $2k-1$ y olvidar los extremos. Otra fuente de errores aparece cuando el índice comienza en un valor distinto de $1$.

Por ejemplo,

$$
\sum_{r=3}^{6}r^2=3^2+4^2+5^2+6^2,
$$

no $1^2+2^2+3^2+4^2+5^2+6^2$.

### De forma expandida a sigma

Supongamos ahora que tenemos

$$
4+7+10+13+16.
$$

Los términos forman una progresión aritmética con término general $3k+1$ si dejamos correr $k$ desde $1$ hasta $5$:

$$
4+7+10+13+16
=
\sum_{k=1}^{5}(3k+1).
$$

La representación no es única. La misma suma también puede escribirse como

$$
\sum_{j=0}^{4}(3j+4).
$$

Ambas expresiones generan exactamente la misma lista de términos. Esta no unicidad anticipa una idea central: cambiar el índice no cambia necesariamente la suma.

***
## 12.3. El índice mudo {#apm-c12-s03}

En

$$
\sum_{k=1}^{n} a_k,
$$

la letra $k$ cumple un papel local. Podemos reemplazarla por otra letra, siempre que el reemplazo sea consistente:

$$
\sum_{k=1}^{n}a_k
=
\sum_{j=1}^{n}a_j.
$$

Decimos que $k$ y $j$ son **índices mudos** o variables ligadas.

La situación es análoga a la de una variable ligada por un cuantificador. En

$$
\forall k\in\{1,\ldots,n\},
$$

renombrar $k$ como $j$ no cambia la afirmación si el cambio se hace en todas las apariciones ligadas.

Hay que distinguir el índice de los parámetros libres. En

$$
\sum_{k=1}^{n}(k+m),
$$

$k$ está ligado por la sumatoria, mientras que $m$ y $n$ actúan como parámetros. Por eso podemos escribir

$$
\sum_{j=1}^{n}(j+m),
$$

pero no podemos reemplazar arbitrariamente $m$ o $n$ sin cambiar la expresión.

También debemos evitar colisiones de variables. Si una expresión externa ya utiliza $j$ con otro significado, renombrar el índice interno como $j$ puede volver ambigua la notación. La elección de letras es libre, pero debe preservar la estructura lógica.

***
### Nota pedagógica — Renombrar sin absorber un parámetro

En $S(m)=\sum_{k=1}^{3}(k+m)$, el índice $k$ varía dentro de la suma y el parámetro $m$ permanece fijado. El renombrado correcto es $S(m)=\sum_{r=1}^{3}(r+m)$. Si escribimos en cambio $\sum_{m=1}^{3}(m+m)$, las dos apariciones del sumando quedan ligadas al índice: desapareció el parámetro externo y cambió el problema. Es la misma captura de variable que estudiamos en C6.

**Control resuelto.** Fija $m=5$. La suma original vale $6+7+8=21$; el renombrado con $r$ conserva esos tres términos. La expresión con captura vale $2+4+6=12$ y ya no depende de ese $m=5$. Una letra nueva debe sustituir sólo las apariciones ligadas al índice; los límites y parámetros mantienen su significado. En una suma doble, un índice exterior puede actuar como parámetro de la suma interior, aunque esté ligado en la expresión completa.

***
## 12.4. Linealidad de las sumas finitas {#apm-c12-s04}

Las sumas finitas distribuyen sobre la adición término a término. Si $m\le n$, entonces

$$
\sum_{k=m}^{n}(a_k+b_k)
=
\sum_{k=m}^{n}a_k+
\sum_{k=m}^{n}b_k.
$$

La razón aparece al expandir ambos lados:

$$
(a_m+b_m)+\cdots+(a_n+b_n)
$$

puede reagruparse como

$$
(a_m+\cdots+a_n)+(b_m+\cdots+b_n).
$$

Del mismo modo, si $c$ no depende del índice $k$,

$$
\sum_{k=m}^{n}c a_k
=
c\sum_{k=m}^{n}a_k.
$$

Estas dos propiedades forman la **linealidad** de la sumatoria. Juntas implican, por ejemplo,

$$
\sum_{k=1}^{n}(3k-2)
=
3\sum_{k=1}^{n}k-2\sum_{k=1}^{n}1.
$$

Pero aquí aparece una restricción importante. No podemos extraer un factor que dependa de $k$. En general,

$$
\sum_{k=1}^{n}k a_k
\ne
k\sum_{k=1}^{n}a_k,
$$

porque en el lado derecho el símbolo $k$ ya no está ligado por la suma y ni siquiera tiene un valor único.

La linealidad es poderosa precisamente porque separa una expresión compleja en sumas más simples sin cambiar el rango.

***
## 12.5. Separar y recombinar rangos {#apm-c12-s05}

Una suma finita puede dividirse en bloques. Si $m\le r<n$, entonces

$$
\sum_{k=m}^{n}a_k
=
\sum_{k=m}^{r}a_k+
\sum_{k=r+1}^{n}a_k.
$$

El punto de corte debe respetar los extremos: el término $a_r$ aparece en el primer bloque y $a_{r+1}$ en el segundo, de modo que ningún término se repite ni se pierde.

Un caso especialmente útil es separar el primer término:

$$
\sum_{k=m}^{n}a_k
=
a_m+
\sum_{k=m+1}^{n}a_k.
$$

También podemos separar el último:

$$
\sum_{k=m}^{n}a_k
=
\sum_{k=m}^{n-1}a_k+a_n.
$$

Estas formas aparecen continuamente en inducción, reindexación y telescopaje.

La operación inversa consiste en recombinar sumas contiguas. Por ejemplo,

$$
\sum_{k=1}^{4}a_k+
\sum_{k=5}^{9}a_k
=
\sum_{k=1}^{9}a_k.
$$

Pero no podemos combinar sin más

$$
\sum_{k=1}^{4}a_k+
\sum_{k=6}^{9}a_k,
$$

porque falta el término correspondiente a $k=5$.

***
## 12.6. Cambio de índice por traslación {#apm-c12-s06}

Renombrar un índice no es lo mismo que reindexar. En un cambio de índice real, cambiamos la variable que parametriza la lista de términos.

Partamos de

$$
\sum_{k=m}^{n}a_k
$$

y hagamos la sustitución

$$
j=k+s.
$$

Entonces

$$
k=j-s.
$$

Cuando $k=m$, tenemos $j=m+s$; cuando $k=n$, tenemos $j=n+s$. Por tanto,

$$
\sum_{k=m}^{n}a_k
=
\sum_{j=m+s}^{n+s}a_{j-s}.
$$

La reindexación exige transformar simultáneamente:

1. el índice;
2. el límite inferior;
3. el límite superior;
4. el sumando.

Por ejemplo,

$$
\sum_{k=0}^{n-1}(k+1)^2
$$

puede reescribirse con $j=k+1$. Entonces $j$ corre de $1$ a $n$ y

$$
\sum_{k=0}^{n-1}(k+1)^2
=
\sum_{j=1}^{n}j^2.
$$

Una forma rápida de auditar una reindexación es expandir los primeros y últimos términos antes y después del cambio. Si las listas no coinciden, la reindexación es incorrecta.

***
### Nota pedagógica — La reindexación conserva términos, no sólo extremos

Para reindexar una suma finita necesitamos una correspondencia uno a uno entre los rangos: cada índice antiguo debe tener un índice nuevo distinto y todos los índices nuevos deben proceder de uno antiguo. Bajo esa correspondencia se transforma también el sumando. Una traslación cumple este criterio; una reflexión invierte el recorrido y permite sumar los mismos términos en el orden opuesto.

**Control resuelto.** En $\sum_{k=-2}^{2}a_{3k+1}$, toma $j=k+2$. Los valores antiguos $-2,-1,0,1,2$ corresponden exactamente a $j=0,1,2,3,4$, y $3k+1=3j-5$. Así la nueva suma es $\sum_{j=0}^{4}a_{3j-5}$. Ambas generan $a_{-5},a_{-2},a_1,a_4,a_7$.

Si usamos directamente $r=3k+1$, el nuevo rango es $J=\{-5,-2,1,4,7\}$: podemos escribir $\sum_{r\in J}a_r$, que significa sumar una vez por cada elemento del conjunto finito $J$. No podemos sustituirlo por todos los enteros entre $-5$ y $7$: añadiríamos índices ausentes. Coincidir en los extremos no basta para conservar la lista. Cuando un cambio deja huecos, hay que describirlos en el rango o utilizar otro índice que recorra una lista consecutiva.

***
## 12.7. Sumas aritméticas finitas {#apm-c12-s07}

La fórmula clásica

$$
1+2+\cdots+n
=
\frac{n(n+1)}{2}
$$

puede demostrarse sin inducción mediante apareamiento.

Sea

$$
S=1+2+\cdots+(n-1)+n.
$$

Escribimos la misma suma en orden inverso:

$$
S=n+(n-1)+\cdots+2+1.
$$

Al sumar término a término,

$$
2S=(n+1)+(n+1)+\cdots+(n+1).
$$

Hay $n$ sumandos, de modo que

$$
2S=n(n+1),
$$

y por tanto

$$
S=\frac{n(n+1)}{2}.
$$

La misma idea se extiende a una progresión aritmética

$$
a+(a+d)+(a+2d)+\cdots+(a+(n-1)d).
$$

Hay $n$ términos. El primero es $a$ y el último $a+(n-1)d$. Emparejando extremos obtenemos

$$
\sum_{k=0}^{n-1}(a+kd)
=
\frac{n}{2}\bigl(2a+(n-1)d\bigr).
$$

Esta derivación ilustra una idea que será recurrente: una identidad finita puede tener una prueba estructural más informativa que una verificación por inducción.

***
## 12.8. Sumas geométricas finitas {#apm-c12-s08}

Para esta suma tomamos $n\ge0$ entero y $r\in\mathbb R$. En expresiones polinómicas con exponentes no negativos, el término de exponente cero se interpreta como $1$, también al evaluar la base en cero.

Sea

$$
S=1+r+r^2+\cdots+r^n.
$$

Si $r\ne1$, multiplicamos por $r$:

$$
rS=r+r^2+\cdots+r^n+r^{n+1}.
$$

Restamos:

$$
S-rS=1-r^{n+1}.
$$

Así,

$$
(1-r)S=1-r^{n+1},
$$

y por tanto

$$
S=\frac{1-r^{n+1}}{1-r}.
$$

Equivalentemente,

$$
1+r+\cdots+r^n
=
\frac{r^{n+1}-1}{r-1}
$$

cuando $r\ne1$.

El caso $r=1$ debe separarse porque el denominador anterior se anula. Entonces

$$
1+1+\cdots+1=n+1.
$$

Más generalmente, para enteros $m\le n$ y $r\notin\{0,1\}$,

$$
\sum_{k=m}^{n}r^k
=
r^m\sum_{j=0}^{n-m}r^j
=
r^m\frac{1-r^{n-m+1}}{1-r}.
$$

Aquí combinamos reindexación, extracción de un factor constante respecto del nuevo índice y la fórmula geométrica básica. Si $r=1$, la suma vale $n-m+1$. Si $r=0$ y $m\ge0$, vale $1$ cuando $m=0$ y $0$ cuando $m>0$, con la convención polinómica indicada. Si $m<0$ y $r=0$, la suma no está definida porque contiene una potencia de exponente negativo de cero. Una condición como $r\ne1$ no basta por sí sola para autorizar exponentes negativos.

***
## 12.9. Telescopaje aditivo {#apm-c12-s09}

Una suma telescópica contiene términos que se cancelan en cadena.

Para enteros $m\le n$, y con todos los términos definidos, consideremos

$$
\sum_{k=m}^{n}(b_k-b_{k+1}).
$$

Al expandir,

$$
(b_m-b_{m+1})+(b_{m+1}-b_{m+2})+\cdots+(b_n-b_{n+1}).
$$

Todos los términos interiores aparecen una vez con signo positivo y una vez con signo negativo. Quedan sólo los extremos:

$$
\sum_{k=m}^{n}(b_k-b_{k+1})
=
b_m-b_{n+1}.
$$

El telescopaje es una propiedad de la representación. Una suma puede no parecer telescópica en su forma original y volverse telescópica después de una transformación algebraica adecuada.

También existe la orientación opuesta:

$$
\sum_{k=m}^{n}(b_{k+1}-b_k)
=
b_{n+1}-b_m.
$$

El signo final depende del orden de la diferencia. Por eso conviene expandir algunos términos y no confiar únicamente en una fórmula memorizada.

***
## 12.10. Descomposición para producir telescopaje {#apm-c12-s10}

La suma

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
$$

no muestra cancelaciones de inmediato. Pero la identidad local

$$
\frac{1}{k(k+1)}
=
\frac1k-\frac1{k+1}
$$

revela la estructura.

Entonces

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
\sum_{k=1}^{n}\left(\frac1k-\frac1{k+1}\right).
$$

Al expandir,

$$
\left(1-\frac12\right)
+
\left(\frac12-\frac13\right)
+
\cdots
+
\left(\frac1n-\frac1{n+1}\right),
$$

por lo que

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=
1-\frac1{n+1}
=
\frac{n}{n+1}.
$$

El procedimiento tiene dos etapas conceptualmente distintas:

1. descubrir o verificar una identidad local para el sumando;
2. usar esa identidad para crear una cancelación global.

No necesitamos desarrollar una teoría general de fracciones parciales para aprovechar este mecanismo. Basta reconocer descomposiciones simples que produzcan diferencias consecutivas.

***
## 12.11. Productos finitos {#apm-c12-s11}

La notación

$$
\prod_{k=m}^{n}a_k
$$

representa el producto

$$
a_m a_{m+1}\cdots a_n.
$$

Por ejemplo,

$$
\prod_{k=1}^{4}(k+1)=2\cdot3\cdot4\cdot5.
$$

Adoptaremos la convención de que un producto vacío vale $1$. Esta elección es el análogo multiplicativo de la suma vacía igual a $0$.

Los productos finitos permiten separar rangos:

$$
\prod_{k=m}^{n}a_k
=
\left(\prod_{k=m}^{r}a_k\right)
\left(\prod_{k=r+1}^{n}a_k\right),
$$

si $m\le r<n$.

También permiten extraer una constante, pero la forma cambia respecto de las sumas. Si $c$ no depende de $k$ y hay $n-m+1$ factores, entonces

$$
\prod_{k=m}^{n}(c a_k)
=
c^{n-m+1}\prod_{k=m}^{n}a_k.
$$

No es correcto escribir simplemente

$$
\prod_{k=m}^{n}(c a_k)=c\prod_{k=m}^{n}a_k
$$

salvo en casos especiales.

Esta diferencia muestra por qué no debemos transportar mecánicamente propiedades aditivas al contexto multiplicativo.

***
## 12.12. Productos telescópicos {#apm-c12-s12}

El telescopaje también aparece en productos. Para $n\ge2$ entero, consideremos

$$
\prod_{k=2}^{n}\frac{k}{k-1}.
$$

Al expandir,

$$
\frac21\cdot\frac32\cdot\frac43\cdots\frac{n}{n-1}.
$$

Los factores interiores se cancelan y queda

$$
\prod_{k=2}^{n}\frac{k}{k-1}=n.
$$

Otro ejemplo útil es

$$
\prod_{k=1}^{n}\frac{k+1}{k}
=
n+1.
$$

Aquí la cancelación es multiplicativa: un factor aparece en un numerador y en el denominador del factor siguiente.

La misma precaución que en las sumas telescópicas sigue siendo válida: hay que controlar los factores extremos. La mayor parte de los errores en estos productos no ocurre en la cancelación interior, sino en decidir correctamente qué queda al principio y al final.

***
### Nota pedagógica — Antes de cancelar, comprobar dónde existe el producto

Para $\prod_{k=m}^{n}b_{k+1}/b_k$, con $m\le n$, cada denominador $b_m,\ldots,b_n$ debe ser distinto de cero. Bajo esa condición se cancelan los factores interiores y queda $b_{n+1}/b_m$. El numerador final puede ser cero: eso produce un producto definido igual a cero. Un cero interior que aparezca como denominador, en cambio, impide formar el producto original.

**Control resuelto.** Para $n\ge0$, considera $P_n(t)=\prod_{k=0}^{n}(t+k+1)/(t+k)$. Está definido exactamente cuando $t\notin\{0,-1,\ldots,-n\}$. Allí vale $(t+n+1)/t$. Con $t=-n-1$ todos los denominadores son no nulos, pero el último numerador es cero: el resultado es $0$. Con $n=2,t=-1$, el factor correspondiente a $k=1$ tiene denominador cero. La fórmula abreviada daría $-2$, pero no representa el producto original en ese valor excluido. Simplificar conserva valores dentro del dominio; no borra las exclusiones anteriores.

Un producto vacío vale $1$ y no evalúa ningún factor. Las fórmulas abreviadas obtenidas para rangos no vacíos deben comprobarse por separado antes de extenderlas a un rango vacío.

***
## 12.13. Sumas dobles finitas {#apm-c12-s13}

Una suma doble

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}
$$

puede interpretarse como una suma sobre todos los pares

$$
(i,j)\in\{1,\ldots,m\}\times\{1,\ldots,n\}.
$$

La suma interior recorre $j$ mientras $i$ permanece fijo. Luego la suma exterior cambia $i$.

Como el dominio es un rectángulo finito, podemos recorrer los mismos pares en el orden contrario:

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=1}^{m}a_{ij}.
$$

No hay aquí una cuestión de convergencia: se trata simplemente de una colección finita de términos que puede enumerarse en distinto orden.

Por ejemplo,

$$
\sum_{i=1}^{2}\sum_{j=1}^{3}(i+j)
$$

suma los seis valores correspondientes a los pares

$$
(1,1),(1,2),(1,3),(2,1),(2,2),(2,3).
$$

Invertir el orden produce exactamente el mismo conjunto de seis sumandos.

***
## 12.14. Dominios triangulares y cambio de orden {#apm-c12-s14}

Las sumas dobles se vuelven más delicadas cuando un límite depende del otro índice. Consideremos

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}.
$$

El dominio es

$$
D=\{(i,j):1\le j\le i\le n\}.
$$

Para invertir el orden, fijamos ahora $j$. Si $j$ está fijo, la condición $j\le i\le n$ dice que $i$ recorre desde $j$ hasta $n$. Por tanto,

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=j}^{n}a_{ij}.
$$

El procedimiento correcto no consiste en “intercambiar $i$ y $j$” dentro de los límites. Consiste en describir primero el mismo conjunto de pares y después encontrar otra forma de recorrerlo.

Esta idea permite también contar multiplicidades. Por ejemplo,

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}x_j
$$

puede reorganizarse observando que, para un $j$ fijo, el término $x_j$ aparece cuando

$$
i=j,j+1,\ldots,n.
$$

Aparece, por tanto, $n-j+1$ veces. Así,

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}x_j
=
\sum_{j=1}^{n}(n-j+1)x_j.
$$

***
### Nota pedagógica — Una tabla del dominio, dos recorridos

Para $n=3$, el dominio $1\le j\le i\le3$ se representa así; cada marca indica un par incluido:

| $i\backslash j$ | 1 | 2 | 3 |
|---|---|---|---|
| 1 | Incluido | — | — |
| 2 | Incluido | Incluido | — |
| 3 | Incluido | Incluido | Incluido |

Por filas, los pares son $(1,1)$; después $(2,1),(2,2)$; después $(3,1),(3,2),(3,3)$. Por columnas, son $(1,1),(2,1),(3,1)$; después $(2,2),(3,2)$; después $(3,3)$. Cambia el orden, pero cada par sigue apareciendo exactamente una vez.

**Control resuelto.** Si el sumando es $x_j$, el recorrido por filas da $x_1+(x_1+x_2)+(x_1+x_2+x_3)=3x_1+2x_2+x_3$. Las columnas muestran esas multiplicidades directamente: tres marcas para $j=1$, dos para $j=2$ y una para $j=3$. Para invertir un dominio nuevo, escribe sus desigualdades y resuélvelas para el índice que pasará a ser interior. La tabla pequeña ayuda a detectar extremos omitidos; la justificación general proviene de recorrer el mismo conjunto finito de pares.

***
## 12.15. Identidades finitas y elección del método {#apm-c12-s15}

A esta altura disponemos de varias técnicas. Frente a una identidad finita conviene preguntar qué estructura domina el problema.

### Álgebra directa

Es apropiada cuando ambos lados pueden transformarse mediante distributividad, factorización o fórmulas ya establecidas.

### Reindexación

Es apropiada cuando dos sumas contienen esencialmente los mismos términos, pero numerados de manera diferente.

### Telescopaje

Es apropiado cuando una expresión puede escribirse como diferencias o cocientes consecutivos que cancelan términos interiores.

### Inducción

Es apropiada cuando la identidad tiene una estructura recursiva natural o cuando queremos verificar una fórmula para todos los tamaños $n$ sin disponer de una transformación directa más esclarecedora.

Consideremos nuevamente

$$
1+2+\cdots+n=\frac{n(n+1)}2.
$$

C11 mostró cómo probarla por inducción. En este capítulo vimos una prueba por apareamiento. Ambas son correctas, pero dicen cosas distintas. La inducción muestra que la fórmula se propaga de $n$ a $n+1$; el apareamiento explica por qué el promedio del primer y último término determina la suma.

Elegir el método no es un detalle estilístico. Una buena prueba revela la estructura que hace verdadera a la identidad.

### Diagnóstico de errores

Cinco fallos aparecen con especial frecuencia:

1. desplazar el índice sin desplazar los límites;
2. perder un término extremo al separar rangos;
3. extraer como constante una expresión que depende del índice;
4. declarar telescopaje sin exhibir la cancelación;
5. invertir una suma doble sin describir correctamente el dominio.

Una práctica sólida consiste en expandir algunos términos antes y después de cualquier transformación dudosa.

***
## 12.16. Protocolo de lectura de expresiones indexadas {#apm-c12-s16}

Ante una suma o producto finito, conviene seguir una secuencia de control.

```text
1. IDENTIFICAR EL ÍNDICE.
2. IDENTIFICAR SU RANGO.
3. DISTINGUIR ÍNDICES LIGADOS DE PARÁMETROS LIBRES.
4. EXPANDIR ALGUNOS TÉRMINOS SI LA ESTRUCTURA NO ES TRANSPARENTE.
5. PREGUNTAR SI HAY LINEALIDAD O SEPARACIÓN DE RANGOS.
6. COMPROBAR SI UNA REINDEXACIÓN SIMPLIFICA LA EXPRESIÓN.
7. BUSCAR CANCELACIONES TELESCÓPICAS.
8. SI HAY DOS ÍNDICES, DESCRIBIR EL DOMINIO DE PARES.
9. COMPARAR MÉTODOS POSIBLES.
10. USAR INDUCCIÓN SÓLO SI REFLEJA BIEN LA ESTRUCTURA DEL PROBLEMA.
```

El capítulo comenzó con listas explícitas de términos y terminó con una pequeña teoría de expresiones indexadas. Ya podemos reconocer cuándo dos sumas describen la misma colección de términos, controlar cambios de índice, producir cancelaciones y reorganizar dominios finitos.

El siguiente capítulo estudiará una familia de coeficientes que aparece naturalmente cuando expandimos potencias de sumas. Allí la notación de sumas y productos dejará de ser una herramienta auxiliar para convertirse en parte del lenguaje del teorema del binomio.

***
# Ejercicios

Los ejercicios son originales para *Álgebra para matemáticos* y se calibran con el corpus rector del capítulo. Los identificadores editoriales permanecen en comentarios internos no renderizados.

## A. Leer y expandir notación


**1.** **Nivel A.** En la expresión $\sum_{k=3}^{8}(2k+1)$, identifica el índice, el límite inferior, el límite superior, el sumando y el número de términos.


**2.** **Nivel A.** Expande completamente $\sum_{k=2}^{6}(3k-2)$ y calcula su valor.


**3.** **Nivel A.** Expande $\sum_{j=0}^{5}(-1)^j(j+1)$ sin simplificar primero el patrón de signos.


**4.** **Nivel B.** Para enteros $m\le n$, explica por qué $\sum_{k=m}^{n}a_k$ contiene exactamente $n-m+1$ sumandos. Comprueba tu respuesta con $m=-2$ y $n=3$.


**5.** **Nivel B.** En $\sum_{k=1}^{n}(k+m)^2$, determina cuáles símbolos representan variables ligadas y cuáles actúan como parámetros libres. Explica qué cambia y qué no cambia si se reemplaza $k$ por $r$.


**6.** **Nivel B.** Un estudiante escribe $\sum_{k=3}^{6}k^2=1^2+2^2+3^2+4^2+5^2+6^2$. Localiza el error, escribe la expansión correcta y formula una regla práctica para evitar este tipo de fallo.

## B. Comprimir y renombrar índices


**7.** **Nivel A.** Escribe $5+8+11+14+17+20$ usando una sola sumatoria cuyo índice comience en $1$.


**8.** **Nivel A.** Escribe $4^2+5^2+\cdots+10^2$ en notación sigma de dos maneras distintas.


**9.** **Nivel B.** Da dos representaciones sigma distintas de $1+3+5+\cdots+(2n-1)$ y explica por qué describen la misma lista de términos.


**10.** **Nivel B.** Renombra el índice de $\sum_{k=1}^{n}(k^2+m)$ usando la letra $j$. Después explica por qué el mismo procedimiento no autoriza a reemplazar también el parámetro $m$ por $j$.


**11.** **Nivel B.** Escribe $a+(a+d)+(a+2d)+\cdots+(a+(n-1)d)$ como una sumatoria comenzando en $k=0$ y luego como otra comenzando en $j=1$.


**12.** **Nivel C.** Demuestra, expandiendo ambos miembros, que
$$
\sum_{k=0}^{n}(a+kd)
=
\sum_{j=1}^{n+1}(a+(j-1)d).
$$
Explica por qué ésta es más que una simple sustitución de una letra por otra.

## C. Linealidad


**13.** **Nivel B.** Usa linealidad para reescribir $\sum_{k=1}^{n}(5k-3)$ en términos de $\sum_{k=1}^{n}k$ y $\sum_{k=1}^{n}1$. Luego simplifica hasta obtener una fórmula cerrada.


**14.** **Nivel B.** Simplifica
$$
2\sum_{k=1}^{n}(k+1)-\sum_{k=1}^{n}(k-2)
$$
como una sola sumatoria y luego como una expresión cerrada en $n$.


**15.** **Nivel C.** Decide cuáles extracciones son válidas y justifica cada respuesta:
$$
\sum_{k=1}^{n}m a_k,
\qquad
\sum_{k=1}^{n}k a_k,
\qquad
\sum_{k=1}^{n}(n+1)a_k,
$$
considerando $m$ y $n$ parámetros independientes de $k$.


**16.** **Nivel C.** Demuestra la identidad
$$
\sum_{k=m}^{n}(a_k-b_k)
=
\sum_{k=m}^{n}a_k-
\sum_{k=m}^{n}b_k
$$
partiendo únicamente de la expansión de las sumas y de las leyes asociativa y conmutativa de la adición.


**17.** **Nivel C.** Reduce
$$
3\sum_{k=0}^{n}a_k-2\sum_{k=0}^{n}a_k+\sum_{k=0}^{n}(b_k-a_k)
$$
a la forma más simple posible.


**18.** **Nivel C.** Refuta, mediante un contraejemplo concreto, la afirmación
$$
\sum_{k=1}^{n}a_kb_k
=
\left(\sum_{k=1}^{n}a_k\right)
\left(\sum_{k=1}^{n}b_k\right).
$$
Explica qué términos adicionales aparecen en el producto del lado derecho.

## D. Separar y unir rangos


**19.** **Nivel B.** Separa $\sum_{k=1}^{12}a_k$ en dos sumas cortando después de $k=5$.


**20.** **Nivel B.** Aísla los dos primeros y los dos últimos términos de $\sum_{k=1}^{n}a_k$ para $n\ge4$.


**21.** **Nivel B.** Recombina
$$
\sum_{k=-3}^{2}a_k+
\sum_{k=3}^{9}a_k
$$
en una sola sumatoria.


**22.** **Nivel C.** Explica por qué
$$
\sum_{k=1}^{4}a_k+
\sum_{k=6}^{9}a_k
$$
no puede reemplazarse por $\sum_{k=1}^{9}a_k$. ¿Qué término falta? ¿Qué ocurre, en cambio, si la segunda suma comienza en $k=4$?


**23.** **Nivel C.** Demuestra que, para $m\le n$,
$$
\sum_{k=m}^{n+1}a_k
=
\sum_{k=m}^{n}a_k+a_{n+1}.
$$
Después despeja $\sum_{k=m}^{n}a_k$ y explica la utilidad de esta forma en un paso inductivo.


**24.** **Nivel C.** Si $m\le r<s<n$, demuestra
$$
\sum_{k=m}^{n}a_k
=
\sum_{k=m}^{r}a_k+
\sum_{k=r+1}^{s}a_k+
\sum_{k=s+1}^{n}a_k.
$$
Justifica explícitamente que no se pierde ni se repite ningún índice.

## E. Cambios de índice


**25.** **Nivel B.** Reindexa $\sum_{k=0}^{n-1}(k+1)^3$ usando $j=k+1$.


**26.** **Nivel B.** Reindexa $\sum_{k=4}^{n+3}a_{k-3}$ de manera que el nuevo índice comience en $1$.


**27.** **Nivel C.** Demuestra que
$$
\sum_{k=1}^{n}a_k
=
\sum_{j=1}^{n}a_{n+1-j}
$$
mediante la sustitución $j=n+1-k$. Controla ambos extremos del rango.


**28.** **Nivel C.** Reindexa una de las sumas para simplificar
$$
\sum_{k=0}^{n-1}a_{k+1}-
\sum_{k=1}^{n}a_k.
$$
¿Qué revela la reindexación?


**29.** **Nivel C.** Prueba la fórmula general de traslación
$$
\sum_{k=m}^{n}f(k)
=
\sum_{j=m+s}^{n+s}f(j-s)
$$
para un entero fijo $s$, explicando qué ocurre con índice, límites y sumando.


**30.** **Nivel C.** Para enteros $m\le n$ y una base real $r\ne0$, transforma $\sum_{k=m}^{n}r^k$ en una suma cuyo índice vaya de $0$ a $n-m$. Usa después esa forma para extraer el factor $r^m$.


**31.** **Nivel C.** Un estudiante afirma
$$
\sum_{k=1}^{n}a_{k+2}
=
\sum_{j=1}^{n}a_j
$$
porque «$j=k+2$ es sólo un cambio de índice». Identifica el error y escribe la reindexación correcta.


**32.** **Nivel C.** Reescribe $\sum_{k=1}^{n}a_{k+2}$ como una sumatoria cuyo sumando sea simplemente $a_j$. Verifica la respuesta expandiendo el primer y el último término.


**33.** **Nivel D.** Reindexa
$$
\sum_{k=0}^{n}(2k+1)x^{2k}
$$
con $j=k+1$. Escribe cuidadosamente el nuevo rango y el nuevo exponente de $x$.


**34.** **Nivel D.** Demuestra que
$$
\sum_{k=0}^{n}(2k+1)
=
\sum_{j=1}^{n+1}(2j-1)
$$
mediante una reindexación formal y luego confirma la igualdad expandiendo tres términos al comienzo y el término final.

## F. Sumas aritméticas y geométricas


**35.** **Nivel B.** Deriva nuevamente, mediante apareamiento de extremos, la fórmula
$$
\sum_{k=1}^{n}k=\frac{n(n+1)}2.
$$
Indica dónde se usa que hay exactamente $n$ términos.


**36.** **Nivel B.** Calcula $2+4+6+\cdots+2n$ usando linealidad y la fórmula para $1+2+\cdots+n$.


**37.** **Nivel C.** Demuestra que
$$
1+3+5+\cdots+(2n-1)=n^2
$$
usando la fórmula de una progresión aritmética, no inducción.


**38.** **Nivel C.** Deriva
$$
\sum_{k=0}^{n-1}(a+kd)
=
\frac n2\bigl(2a+(n-1)d\bigr)
$$
por apareamiento del primer y último término, del segundo y penúltimo, etc. Explica por qué la derivación funciona tanto para $n$ par como para $n$ impar.


**39.** **Nivel B.** Calcula $1+3+3^2+\cdots+3^n$ mediante la fórmula de suma geométrica finita.


**40.** **Nivel C.** Para una base real $r\notin\{0,1\}$ y enteros $m\le n$, deriva una fórmula cerrada para
$$
\sum_{k=m}^{n}r^k.
$$
Tu derivación debe comenzar reindexando para que el nuevo índice parta en $0$.


**41.** **Nivel C.** Explica por qué la fórmula $(1-r^{n+1})/(1-r)$ no puede usarse directamente cuando $r=1$. Calcula la suma en ese caso y compara el resultado con la expresión original $1+r+\cdots+r^n$.


**42.** **Nivel D.** Demuestra algebraicamente
$$
\sum_{k=0}^{n}2^k=2^{n+1}-1.
$$
Después verifica la misma identidad por inducción y compara qué estructura hace visible cada prueba.

## G. Telescopaje


**43.** **Nivel B.** Calcula
$$
\sum_{k=1}^{n}\frac1{k(k+1)}
$$
usando $1/[k(k+1)]=1/k-1/(k+1)$. Expande suficientes términos para mostrar la cancelación.


**44.** **Nivel C.** Demuestra
$$
\frac1{k(k+2)}
=
\frac12\left(\frac1k-\frac1{k+2}\right)
$$
y usa esta identidad para evaluar $\sum_{k=1}^{n}1/[k(k+2)]$.


**45.** **Nivel C.** Evalúa
$$
\sum_{k=1}^{n}\bigl(k^2-(k-1)^2\bigr)
$$
por telescopaje. Luego explica por qué el resultado puede anticiparse antes de hacer ninguna expansión algebraica.


**46.** **Nivel C.** Usa
$$
2k+1=(k+1)^2-k^2
$$
para obtener una prueba telescópica de
$$
\sum_{k=0}^{n-1}(2k+1)=n^2.
$$
Compárala con la prueba del ejercicio 37.


**47.** **Nivel C.** Calcula
$$
\sum_{k=0}^{n}\frac1{(k+1)(k+2)}
$$
con una descomposición telescópica y expresa el resultado como una sola fracción.


**48.** **Nivel D.** Verifica la identidad
$$
\frac{3}{(3k+1)(3k+4)}
=
\frac1{3k+1}-\frac1{3k+4}
$$
y úsala para evaluar
$$
\sum_{k=0}^{n}\frac{3}{(3k+1)(3k+4)}.
$$


**49.** **Nivel D.** Descubre una descomposición de la forma
$$
\frac1{k(k+1)(k+2)}
=
C\left(\frac1{k(k+1)}-\frac1{(k+1)(k+2)}\right)
$$
y determina $C$. Después evalúa la suma desde $k=1$ hasta $n$.


**50.** **Nivel D.** La identidad
$$
\sum_{k=1}^{n}\frac1{k(k+1)}=\frac{n}{n+1}
$$
puede verificarse por inducción. Da también una prueba telescópica y argumenta cuál de las dos explica mejor la forma cerrada del resultado.

## H. Productos finitos


**51.** **Nivel A.** Expande $\prod_{k=2}^{5}(k+1)$ y calcula su valor.


**52.** **Nivel B.** Demuestra que, para una constante $c$,
$$
\prod_{k=1}^{n}c=c^n.
$$
¿Qué valor adopta el producto si $n=0$ bajo la convención de producto vacío?


**53.** **Nivel B.** Para $m\le r<n$, demuestra por expansión
$$
\prod_{k=m}^{n}a_k
=
\left(\prod_{k=m}^{r}a_k\right)
\left(\prod_{k=r+1}^{n}a_k\right).
$$


**54.** **Nivel C.** Reindexa $\prod_{k=0}^{n-1}(k+2)$ usando $j=k+2$. Comprueba que el número de factores no cambia.


**55.** **Nivel C.** Evalúa
$$
\prod_{k=2}^{n}\frac{k}{k-1}
$$
mostrando explícitamente la cancelación de factores interiores.


**56.** **Nivel C.** Calcula
$$
\prod_{k=1}^{n}\frac{k+1}{k+2}
$$
y verifica el resultado para $n=1,2,3$ antes de dar la fórmula general.

## I. Sumas dobles


**57.** **Nivel B.** Expande completamente
$$
\sum_{i=1}^{2}\sum_{j=1}^{3}a_{ij}.
$$
¿Cuántos términos aparecen?


**58.** **Nivel B.** Calcula directamente
$$
\sum_{i=1}^{2}\sum_{j=1}^{3}(i+j).
$$
Luego invierte el orden de suma y comprueba que obtienes el mismo valor.


**59.** **Nivel C.** Justifica, describiendo el dominio de pares, que
$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=1}^{m}a_{ij}.
$$
No uses como justificación sólo «porque las sumas conmutan».


**60.** **Nivel C.** Demuestra
$$
\sum_{i=1}^{m}\sum_{j=1}^{n}(a_i+b_j)
=
n\sum_{i=1}^{m}a_i+m\sum_{j=1}^{n}b_j.
$$
Explica el origen de los factores $n$ y $m$.


**61.** **Nivel C.** Simplifica
$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_i
$$
sin expandir todos los términos. Interpreta el resultado como un conteo de multiplicidad.


**62.** **Nivel D.** Demuestra que
$$
\sum_{i=1}^{m}\sum_{j=1}^{n}ij
=
\left(\sum_{i=1}^{m}i\right)
\left(\sum_{j=1}^{n}j\right),
$$
y obtén una fórmula cerrada en $m$ y $n$.

## J. Dominios triangulares


**63.** **Nivel B.** Enumera todos los pares $(i,j)$ que aparecen en
$$
\sum_{i=1}^{4}\sum_{j=1}^{i}a_{ij}.
$$
Dibuja, si te ayuda, el dominio como puntos de una cuadrícula.


**64.** **Nivel C.** Demuestra que
$$
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=j}^{n}a_{ij}
$$
describiendo primero el dominio común $\{(i,j):1\le j\le i\le n\}$.


**65.** **Nivel C.** Evalúa
$$
\sum_{i=1}^{n}\sum_{j=1}^{i}1
$$
de dos maneras: contando directamente cuántos valores de $j$ corresponden a cada $i$ y cambiando el orden de suma.


**66.** **Nivel D.** Demuestra la identidad de multiplicidades
$$
\sum_{i=1}^{n}\sum_{j=1}^{i}x_j
=
\sum_{j=1}^{n}(n-j+1)x_j.
$$
Interpreta el coeficiente $n-j+1$ como el número de veces que aparece $x_j$ en la suma original.

## K. Diagnóstico y comparación de métodos


**67.** **Nivel C.** Diagnostica el error en
$$
\sum_{k=1}^{n}k a_k
=
k\sum_{k=1}^{n}a_k.
$$
Propón una versión correcta de la regla de extracción de constantes.


**68.** **Nivel C.** Un estudiante transforma
$$
\sum_{k=0}^{n-1}(k+1)^2
$$
en $\sum_{j=0}^{n-1}j^2$ usando $j=k+1$. Señala todos los componentes que quedaron sin transformar y escribe la versión correcta.


**69.** **Nivel D.** Explica por qué es incorrecto escribir
$$
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=1}^{j}a_{ij}.
$$
Describe el dominio de cada lado y escribe el cambio de orden correcto.


**70.** **Nivel D.** Para cada problema, elige el método que consideres estructuralmente más adecuado —álgebra directa, reindexación, telescopaje o inducción— y justifica la elección antes de resolverlo:

   a. $\sum_{k=1}^{n}(4k-1)$;

   b. $\sum_{k=1}^{n}\bigl((k+1)^3-k^3\bigr)$;

   c. comparar $\sum_{k=0}^{n-1}a_{k+1}$ con $\sum_{j=1}^{n}a_j$;

   d. verificar una fórmula cerrada ya conjeturada para una familia definida recursivamente.


**71.** **Nivel D.** Compara la prueba por inducción y la prueba por apareamiento de
$$
1+2+\cdots+n=\frac{n(n+1)}2.
$$
No basta con decir que ambas son correctas: explica qué rasgo estructural revela cada una y cuál usarías para descubrir la fórmula desde cero.


**72.** **Nivel D.** Una solución pretende evaluar $\sum_{k=1}^{n}1/[k(k+1)]$ escribiendo «se cancelan casi todos los términos» sin mostrar ninguna descomposición. Explica por qué eso no constituye una prueba completa y reconstruye el argumento mínimo que vuelve visible el telescopaje.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E. Reindexación en varias etapas.** Sea $n\ge1$. Partiendo de
$$
S=\sum_{k=2}^{n+1}(2k-3)a_{k-1},
$$
realiza primero la sustitución $j=k-1$ y luego invierte el orden mediante $r=n+1-j$. Obtén dos representaciones nuevas de $S$. En cada etapa debes registrar explícitamente índice antiguo, índice nuevo, límites transformados y sumando transformado. Finalmente verifica las tres expresiones expandiendo sus dos primeros y sus dos últimos términos.


**74.** **Nivel E. Dos pruebas de una identidad larga.** Demuestra sin inducción que
$$
\sum_{k=1}^{n}k(k+1)
=
\frac{n(n+1)(n+2)}3.
$$
Busca primero una expresión $F(k)$ tal que $F(k)-F(k-1)=k(k+1)$ y usa telescopaje. Después verifica la misma identidad por inducción. Compara ambas pruebas e identifica cuál explica de manera más directa el factor $n(n+1)(n+2)$.


**75.** **Nivel F. Telescopaje no evidente.** Para $n\ge1$, evalúa
$$
\sum_{k=1}^{n}\frac1{k(k+1)(k+2)}.
$$
No uses una fórmula memorizada. Debes descubrir y demostrar una identidad local que convierta cada sumando en una diferencia de dos términos consecutivos de una familia adecuada, exhibir la cancelación y reducir el resultado a una sola fracción racional en $n$.


**76.** **Nivel F. Producto telescópico no trivial.** Para $n\ge2$, demuestra que
$$
\prod_{k=2}^{n}\frac{(k-1)(k+2)}{k(k+1)}
=
\frac{n+2}{3n}.
$$
No canceles «mentalmente»: separa el producto en dos factores telescópicos, muestra cuáles factores sobreviven en cada uno y controla los casos $n=2$ y $n=3$ como auditoría de extremos.


**77.** **Nivel F. Suma rectangular reorganizada de dos maneras.** Sean $x_1,\ldots,x_m$ y $y_1,\ldots,y_n$. Calcula
$$
S=\sum_{i=1}^{m}\sum_{j=1}^{n}(x_i-y_j)
$$
de dos maneras distintas: primero sumando respecto de $j$ y luego respecto de $i$, y después invirtiendo el orden desde el comienzo. Demuestra que ambos caminos conducen a
$$
S=n\sum_{i=1}^{m}x_i-m\sum_{j=1}^{n}y_j.
$$
Explica el resultado como un conteo de multiplicidades sobre el rectángulo de índices.


**78.** **Nivel F. Dominio triangular y simplificación posterior.** Sea $(b_j)$ una familia y define
$$
S_n=\sum_{i=1}^{n}\sum_{j=1}^{i}(b_j-b_{j+1}).
$$
Resuelve el problema de dos maneras. En la primera, telescopa primero la suma interior y luego suma sobre $i$. En la segunda, cambia primero el orden de suma usando el dominio $1\le j\le i\le n$ y simplifica después la suma resultante. Demuestra que ambos métodos producen exactamente la misma expresión final.


**79.** **Nivel G. Elegir el método.** Demuestra, para $n\ge1$,
$$
\sum_{k=1}^{n}(3k^2+3k+1)=(n+1)^3-1.
$$
Antes de empezar, compara al menos tres estrategias posibles entre álgebra directa, reindexación, telescopaje e inducción. Elige una como prueba principal y justifica por qué revela mejor la estructura de la identidad. Después bosqueja cómo funcionaría una segunda estrategia y señala qué información queda más oculta en ella.


**80.** **Nivel G. Reconstrucción de una solución defectuosa.** Se quiere demostrar
$$
\sum_{k=1}^{n}\frac1{k(k+1)}=\frac{n}{n+1}.
$$
Un estudiante escribe:

> «Como $1/[k(k+1)]=1/k-1/(k+1)$,
> $$
> \sum_{k=1}^{n}\frac1{k(k+1)}
> =\sum_{k=1}^{n}\frac1k-\sum_{j=1}^{n}\frac1j
> =0.
> $$
> Si cambiamos el límite superior de la segunda suma a $n+1$, queda $1-1/(n+1)$, así que el resultado es correcto.»

Identifica **todos** los errores lógicos y de indexación de esta argumentación. Después reconstruye una prueba correcta de principio a fin. Tu solución debe distinguir entre renombrar un índice y reindexar una suma, justificar los nuevos límites y hacer visibles los términos extremos que sobreviven.

***
***
## N. Rangos, dominios y cancelación con restricciones


**81.** Sea $n\ge0$ un entero y supón definidos todos los términos utilizados. Reindexa $\sum_{k=-n}^{n}a_{2k+1}$ con un índice que comience en cero. Registra correspondencia, extremos, sumando y número de términos; comprueba $n=0$.


**82.** Para enteros $m\le n$, reescribe $\sum_{k=m}^{n}(k-m)a_k$ invirtiendo el orden mediante $j=m+n-k$. Justifica todos los cambios y comprueba el caso $m=n$.


**83.** Para $n\ge0$, escribe $\sum_{k=0}^{n}a_{3k+2}$ usando directamente como índice el subíndice de $a$. Describe el conjunto finito de índices. Refuta su sustitución por $\sum_{j=2}^{3n+2}a_j$ cuando $n\ge1$.


**84.** Para $n\ge0$, demuestra $\sum_{k=-n}^{n}k a_k=\sum_{j=1}^{n}j(a_j-a_{-j})$. Explica por qué la simetría del rango no basta para concluir que la suma vale cero e indica una condición suficiente para que sí valga cero.


**85.** Para $n\ge1$, cambia el orden de $\sum_{i=1}^{n}\sum_{j=i}^{i+2}a_{ij}$. Describe el dominio por desigualdades y comprueba las columnas extremas. Puedes usar $\max$ y $\min$ para indicar el mayor y el menor de dos extremos.


**86.** Para $n\ge1$, invierte $\sum_{i=1}^{n}\sum_{j=1}^{n-i}a_{ij}$ y cuenta los pares del dominio. Explica qué ocurre con la última fila y con $n=1$.


**87.** Sea $n\ge1$. Cambia el orden de $\sum_{i=1}^{2n}\sum_{j=1}^{\min(i,n)}a_{ij}$ y calcula el número total de pares. Compara el dominio con el triángulo de [§12.14](algebra-para-matematicos-capitulo-12-sumas-productos-e-identidades-finitas.md#apm-c12-s14).


**88.** Para $n\ge1$, invierte el orden de $\sum_{i=1}^{n}[\sum_{j=1}^{i-1}a_{ij}+\sum_{j=i+1}^{n}a_{ij}]$. Describe qué pares se excluyen y prueba que el cambio no duplica términos. Cuenta los pares y trata $n=1$.


**89.** Para $n\ge1$, evalúa $\sum_{k=1}^{n}(2k+3)/[(k+1)^2(k+2)^2]$. Descubre y prueba una diferencia de dos términos consecutivos que produzca telescopaje; no basta anunciar cancelaciones.


**90.** Para $n\ge1$, calcula $\sum_{k=1}^{n}4(k+1)/[k^2(k+2)^2]$. Produce el telescopaje y explica por qué sobreviven dos extremos de cada signo. Comprueba el caso corto $n=1$.


**91.** Sea $n\ge1$. Evalúa $\sum_{k=1}^{n}k(k+1)(k+2)$ construyendo una familia polinómica cuya diferencia consecutiva sea el sumando. Explica cómo escoges la familia y demuestra la identidad local.


**92.** Para $n\ge0$, evalúa $\prod_{k=0}^{n}(1-1/(k+2)^2)$ sin multiplicar todos los factores. Descubre una factorización que produzca dos productos telescópicos y verifica $n=0$.


**93.** Para $n\ge1$ y $t\in\mathbb R$, determina el dominio y los ceros de $P_n(t)=\prod_{k=1}^{n}(k-t)/(k+t)$. ¿Cuándo es legítimo afirmar $P_n(t)P_n(-t)=1$? Trata también $t=0$.


**94.** Para $n\ge1$, estudia $Q_n(t)=\prod_{k=0}^{n}(t+k+2)/(t+k)$. Determina dominio, fórmula cerrada y ceros. Identifica los dos extremos que sobreviven en cada parte y decide qué ocurre con $n=2,t=-1$.


**95.** Para $n\ge0$, estudia $R_n(t)=\prod_{k=1}^{n}(1-t/k)$ sobre los reales: dominio, ceros y valores en $t=0,-1$. Distingue el caso $n=0$ de los casos con factores.


**96.** Sea $n\ge1$. Compara $A_n=\prod_{k=1}^{n}(k^2-1)/(k^2-k)$ con $B_n=\prod_{k=2}^{n}(k^2-1)/(k^2-k)$. Decide cuáles están definidos y evalúa los que lo estén. Diagnostica la propuesta «cancelar $k-1$ en cada factor prueba $A_n=n+1$».

# Soluciones razonadas

## A. Leer y expandir notación


### 1

En

$$
\sum_{k=3}^{8}(2k+1),
$$

el índice es $k$, el límite inferior es $3$, el límite superior es $8$ y el sumando es $2k+1$. Los valores del índice son $3,4,5,6,7,8$, por lo que hay

$$
8-3+1=6
$$

sumandos.


### 2

Sustituimos $k=2,3,4,5,6$:

$$
\sum_{k=2}^{6}(3k-2)
=4+7+10+13+16
=50.
$$


### 3

Sustituyendo sucesivamente $j=0,1,2,3,4,5$ obtenemos

$$
(+1)\cdot1+(-1)\cdot2+(+1)\cdot3+(-1)\cdot4+(+1)\cdot5+(-1)\cdot6,
$$

es decir,

$$
1-2+3-4+5-6.
$$

La expansión muestra primero el patrón de signos; sólo después, si se desea, puede simplificarse a $-3$.


### 4

Los índices enteros desde $m$ hasta $n$, ambos incluidos, son

$$
m,m+1,\ldots,n.
$$

Si restamos $m$ a todos, obtenemos $0,1,\ldots,n-m$, lista que contiene $n-m+1$ enteros. Por eso la suma tiene exactamente $n-m+1$ sumandos.

Para $m=-2$ y $n=3$ aparecen

$$
a_{-2}+a_{-1}+a_0+a_1+a_2+a_3,
$$

seis términos, y en efecto

$$
3-(-2)+1=6.
$$


### 5

En

$$
\sum_{k=1}^{n}(k+m)^2,
$$

$k$ es una variable ligada por la sumatoria. Los símbolos $m$ y $n$ son parámetros libres respecto de esa sumatoria.

Podemos renombrar consistentemente el índice:

$$
\sum_{k=1}^{n}(k+m)^2
=
\sum_{r=1}^{n}(r+m)^2.
$$

No cambia ni la lista de valores recorridos ni el valor de la suma. Sólo cambia el nombre local del índice.


### 6

El límite inferior es $3$, de modo que el primer término es $3^2$, no $1^2$. La expansión correcta es

$$
\sum_{k=3}^{6}k^2
=3^2+4^2+5^2+6^2
=9+16+25+36
=86.
$$

Regla práctica: antes de expandir, escribir explícitamente la lista de valores que recorre el índice. El sumando se evalúa sólo en esos valores.

## B. Comprimir y renombrar índices


### 7

La diferencia entre términos consecutivos es $3$. Si el índice comienza en $1$, el término general $3k+2$ produce $5$ cuando $k=1$. Por tanto,

$$
5+8+11+14+17+20
=
\sum_{k=1}^{6}(3k+2).
$$


### 8

Una forma directa es

$$
\sum_{k=4}^{10}k^2.
$$

Otra, trasladando el índice para comenzar en $0$, es

$$
\sum_{j=0}^{6}(j+4)^2.
$$

Ambas generan $4^2,5^2,\ldots,10^2$.


### 9

Dos representaciones son

$$
\sum_{k=1}^{n}(2k-1)
$$

y

$$
\sum_{j=0}^{n-1}(2j+1).
$$

La primera produce $1,3,\ldots,2n-1$. En la segunda, $j=0$ produce $1$ y $j=n-1$ produce $2n-1$. Las dos recorren la misma lista de $n$ números impares.


### 10

El renombre correcto es

$$
\sum_{k=1}^{n}(k^2+m)
=
\sum_{j=1}^{n}(j^2+m).
$$

Aquí sólo hemos cambiado el nombre de la variable ligada. El parámetro $m$ no está ligado por la sumatoria y conserva su significado externo. Reemplazar también $m$ por $j$ daría

$$
\sum_{j=1}^{n}(j^2+j),
$$

que es otra expresión: el parámetro habría sido sustituido por una cantidad que varía con el índice.


### 11

Comenzando en $0$:

$$
a+(a+d)+\cdots+(a+(n-1)d)
=
\sum_{k=0}^{n-1}(a+kd).
$$

Comenzando en $1$:

$$
a+(a+d)+\cdots+(a+(n-1)d)
=
\sum_{j=1}^{n}(a+(j-1)d).
$$


### 12

El lado izquierdo se expande como

$$
a+(a+d)+(a+2d)+\cdots+(a+nd).
$$

El lado derecho se expande como

$$
(a+0d)+(a+d)+(a+2d)+\cdots+(a+nd),
$$

que es la misma lista.

Formalmente, la sustitución es $j=k+1$, de modo que $k=j-1$. Al pasar de $k=0$ a $k=n$, el nuevo índice pasa de $j=1$ a $j=n+1$, y el sumando $a+kd$ se convierte en $a+(j-1)d$. No es un mero cambio de letra: cambian también los límites y la fórmula del sumando.

## C. Linealidad


### 13

Por linealidad,

$$
\sum_{k=1}^{n}(5k-3)
=5\sum_{k=1}^{n}k-3\sum_{k=1}^{n}1.
$$

Usando

$$
\sum_{k=1}^{n}k=\frac{n(n+1)}2,
\qquad
\sum_{k=1}^{n}1=n,
$$

obtenemos

$$
5\frac{n(n+1)}2-3n
=\frac{5n^2-n}{2}
=\frac{n(5n-1)}2.
$$


### 14

Como ambas sumas tienen el mismo rango,

$$
2\sum_{k=1}^{n}(k+1)-\sum_{k=1}^{n}(k-2)
=
\sum_{k=1}^{n}\bigl(2(k+1)-(k-2)\bigr).
$$

Dentro de la suma,

$$
2(k+1)-(k-2)=k+4.
$$

Por tanto,

$$
\sum_{k=1}^{n}(k+4)
=
\frac{n(n+1)}2+4n
=
\frac{n(n+9)}2.
$$


### 15

Como $m$ no depende de $k$,

$$
\sum_{k=1}^{n}m a_k
=m\sum_{k=1}^{n}a_k
$$

es válido.

En cambio,

$$
\sum_{k=1}^{n}k a_k
$$

no permite extraer $k$, porque $k$ cambia de término en término.

Finalmente, $n+1$ es constante respecto de $k$, así que

$$
\sum_{k=1}^{n}(n+1)a_k
=(n+1)\sum_{k=1}^{n}a_k.
$$

La condición decisiva no es que el símbolo sea una letra, sino que su valor sea independiente del índice de sumación.


### 16

Expandimos el lado izquierdo:

$$
(a_m-b_m)+(a_{m+1}-b_{m+1})+\cdots+(a_n-b_n).
$$

Interpretando cada resta como suma del opuesto y usando asociatividad y conmutatividad, agrupamos los términos $a$ y los términos $-b$:

$$
(a_m+a_{m+1}+\cdots+a_n)
-
(b_m+b_{m+1}+\cdots+b_n).
$$

Esto es precisamente

$$
\sum_{k=m}^{n}a_k-
\sum_{k=m}^{n}b_k.
$$


### 17

Sea

$$
A=\sum_{k=0}^{n}a_k,
\qquad
B=\sum_{k=0}^{n}b_k.
$$

Entonces

$$
3A-2A+\sum_{k=0}^{n}(b_k-a_k)
=A+(B-A)=B.
$$

Por tanto, la expresión se reduce a

$$
\boxed{\sum_{k=0}^{n}b_k}.
$$


### 18

Tomemos $n=2$ y

$$
a_1=a_2=b_1=b_2=1.
$$

Entonces

$$
\sum_{k=1}^{2}a_kb_k=1+1=2,
$$

mientras que

$$
(a_1+a_2)(b_1+b_2)=2\cdot2=4.
$$

Al expandir el producto del lado derecho aparecen

$$
a_1b_1+a_1b_2+a_2b_1+a_2b_2.
$$

La suma original contiene sólo los términos diagonales $a_1b_1$ y $a_2b_2$; el producto añade los términos cruzados $a_1b_2$ y $a_2b_1$.

## D. Separar y unir rangos


### 19

Cortando después de $k=5$:

$$
\sum_{k=1}^{12}a_k
=
\sum_{k=1}^{5}a_k+
\sum_{k=6}^{12}a_k.
$$


### 20

Para $n\ge4$,

$$
\sum_{k=1}^{n}a_k
=
a_1+a_2+
\sum_{k=3}^{n-2}a_k+a_{n-1}+a_n.
$$

Si $n=4$, la suma central es vacía y vale $0$, de acuerdo con la convención adoptada.


### 21

Los rangos son contiguos: el primero termina en $2$ y el segundo comienza en $3$. Por tanto,

$$
\sum_{k=-3}^{2}a_k+
\sum_{k=3}^{9}a_k
=
\sum_{k=-3}^{9}a_k.
$$


### 22

En

$$
\sum_{k=1}^{4}a_k+
\sum_{k=6}^{9}a_k
$$

falta $a_5$. Por eso no podemos sustituirla por $\sum_{k=1}^{9}a_k$ como identidad para una familia arbitraria. La diferencia entre la suma completa y la propuesta es exactamente $a_5$: coinciden si $a_5=0$, pero no en general.

Si la segunda suma comenzara en $k=4$, entonces $a_4$ aparecería dos veces:

$$
\sum_{k=1}^{4}a_k+
\sum_{k=4}^{9}a_k
=
\sum_{k=1}^{9}a_k+a_4.
$$

Así, para recombinar directamente, los rangos deben ser contiguos y no superponerse.


### 23

La suma hasta $n+1$ contiene exactamente los términos de la suma hasta $n$ más el término final $a_{n+1}$:

$$
\sum_{k=m}^{n+1}a_k
=
a_m+\cdots+a_n+a_{n+1}
=
\sum_{k=m}^{n}a_k+a_{n+1}.
$$

Despejando,

$$
\sum_{k=m}^{n}a_k
=
\sum_{k=m}^{n+1}a_k-a_{n+1}.
$$

En inducción, la primera forma permite pasar de una expresión conocida hasta $n$ a la correspondiente hasta $n+1$ aislando exactamente el nuevo término.


### 24

Los tres rangos son

$$
[m,r],\qquad [r+1,s],\qquad [s+1,n].
$$

Son disjuntos y su unión es todo el conjunto de índices $m,m+1,\ldots,n$. Por tanto,

$$
\sum_{k=m}^{n}a_k
=
\sum_{k=m}^{r}a_k+
\sum_{k=r+1}^{s}a_k+
\sum_{k=s+1}^{n}a_k.
$$

El primer bloque termina en $r$ y el siguiente comienza en $r+1$; análogamente, el segundo termina en $s$ y el tercero comienza en $s+1$. No hay huecos ni superposiciones.

## E. Cambios de índice


### 25

Sea $j=k+1$. Entonces $k=j-1$. Cuando $k=0$, $j=1$; cuando $k=n-1$, $j=n$. Además,

$$
(k+1)^3=j^3.
$$

Por tanto,

$$
\sum_{k=0}^{n-1}(k+1)^3
=
\sum_{j=1}^{n}j^3.
$$


### 26

Queremos que el nuevo índice comience en $1$. Tomamos

$$
j=k-3.
$$

Entonces $k=j+3$. Para $k=4$ tenemos $j=1$, y para $k=n+3$ tenemos $j=n$. El sumando se convierte en

$$
a_{k-3}=a_j.
$$

Así,

$$
\sum_{k=4}^{n+3}a_{k-3}
=
\sum_{j=1}^{n}a_j.
$$


### 27

Tomamos

$$
j=n+1-k.
$$

Entonces

$$
k=n+1-j.
$$

Cuando $k=1$, $j=n$; cuando $k=n$, $j=1$. Por tanto, al aumentar $k$, $j$ recorre los valores en orden inverso. Como la suma es finita, podemos escribirlos de nuevo en orden ascendente:

$$
\sum_{k=1}^{n}a_k
=
\sum_{j=1}^{n}a_{n+1-j}.
$$

La segunda suma expande como

$$
a_n+a_{n-1}+\cdots+a_1,
$$

que contiene exactamente los mismos términos que la primera.


### 28

En la primera suma tomamos $j=k+1$. Entonces

$$
\sum_{k=0}^{n-1}a_{k+1}
=
\sum_{j=1}^{n}a_j.
$$

Por tanto,

$$
\sum_{k=0}^{n-1}a_{k+1}-
\sum_{k=1}^{n}a_k
=0.
$$

La reindexación revela que las dos sumas son la misma colección de términos escrita con índices distintos.


### 29

Sea

$$
j=k+s,
$$

con $s$ fijo. Entonces $k=j-s$. Los extremos se transforman así:

$$
k=m\Rightarrow j=m+s,
\qquad
k=n\Rightarrow j=n+s.
$$

El sumando $f(k)$ se convierte en $f(j-s)$. Por tanto,

$$
\sum_{k=m}^{n}f(k)
=
\sum_{j=m+s}^{n+s}f(j-s).
$$

La igualdad es correcta porque la aplicación $k\mapsto j=k+s$ establece una correspondencia uno a uno entre los dos rangos y conserva el valor de cada término bajo la sustitución indicada.


### 30

La hipótesis $r\ne0$ garantiza que todas las potencias de exponente entero están definidas. Tomamos

$$
j=k-m,
$$

es decir, $k=j+m$. Si $k=m$, entonces $j=0$; si $k=n$, entonces $j=n-m$. Luego

$$
\sum_{k=m}^{n}r^k
=
\sum_{j=0}^{n-m}r^{j+m}.
$$

Como $r^m$ no depende de $j$,

$$
\sum_{k=m}^{n}r^k
=
r^m\sum_{j=0}^{n-m}r^j.
$$


### 31

Si $j=k+2$, no basta cambiar el nombre del índice. Cuando $k=1$, $j=3$; cuando $k=n$, $j=n+2$. Además, $a_{k+2}=a_j$. La reindexación correcta es

$$
\sum_{k=1}^{n}a_{k+2}
=
\sum_{j=3}^{n+2}a_j.
$$

La expresión $\sum_{j=1}^{n}a_j$ contiene otra lista de términos: comienza en $a_1$ y termina en $a_n$.


### 32

Con $j=k+2$,

$$
\sum_{k=1}^{n}a_{k+2}
=
\sum_{j=3}^{n+2}a_j.
$$

La expresión original comienza con $a_3$ y termina con $a_{n+2}$. La nueva suma también comienza con $a_3$ y termina con $a_{n+2}$, así que los extremos confirman la reindexación.


### 33

Sea $j=k+1$, por lo que $k=j-1$. El rango $k=0,\ldots,n$ se transforma en $j=1,\ldots,n+1$. Además,

$$
2k+1=2(j-1)+1=2j-1
$$

y

$$
x^{2k}=x^{2(j-1)}=x^{2j-2}.
$$

Por tanto,

$$
\sum_{k=0}^{n}(2k+1)x^{2k}
=
\sum_{j=1}^{n+1}(2j-1)x^{2j-2}.
$$


### 34

Tomamos $j=k+1$. Entonces $k=j-1$, el rango $0\le k\le n$ se convierte en $1\le j\le n+1$ y

$$
2k+1=2j-1.
$$

Así,

$$
\sum_{k=0}^{n}(2k+1)
=
\sum_{j=1}^{n+1}(2j-1).
$$

La primera suma comienza

$$
1+3+5+\cdots+(2n+1),
$$

y la segunda también:

$$
1+3+5+\cdots+(2(n+1)-1).
$$

Como $2(n+1)-1=2n+1$, coinciden también en el término final.

## F. Sumas aritméticas y geométricas


### 35

Sea

$$
S=1+2+\cdots+n.
$$

Escribimos la misma suma en orden inverso:

$$
S=n+(n-1)+\cdots+1.
$$

Sumando término a término,

$$
2S=(n+1)+(n+1)+\cdots+(n+1).
$$

Hay exactamente $n$ columnas, porque la suma original tiene los índices $1,2,\ldots,n$. Por eso

$$
2S=n(n+1)
$$

y

$$
S=\frac{n(n+1)}2.
$$


### 36

Tenemos

$$
2+4+\cdots+2n
=
\sum_{k=1}^{n}2k
=2\sum_{k=1}^{n}k.
$$

Por tanto,

$$
2\frac{n(n+1)}2=n(n+1).
$$


### 37

La sucesión $1,3,5,\ldots,2n-1$ es una progresión aritmética de $n$ términos, con primer término $1$ y último término $2n-1$. La fórmula de una progresión aritmética da

$$
S=\frac n2\bigl(1+(2n-1)\bigr)
=\frac n2(2n)
=n^2.
$$


### 38

Sea

$$
S=a+(a+d)+\cdots+(a+(n-1)d).
$$

En orden inverso,

$$
S=(a+(n-1)d)+(a+(n-2)d)+\cdots+a.
$$

Al sumar columna a columna, cada par vale

$$
2a+(n-1)d.
$$

Hay $n$ columnas, de modo que

$$
2S=n\bigl(2a+(n-1)d\bigr),
$$

y por tanto

$$
S=\frac n2\bigl(2a+(n-1)d\bigr).
$$

El argumento no requiere separar paridad. Si $n$ es impar, la columna central empareja el término medio de una copia con el mismo término medio de la copia invertida; su suma sigue siendo $2a+(n-1)d$.


### 39

Es una suma geométrica con razón $3$:

$$
1+3+3^2+\cdots+3^n
=
\frac{3^{n+1}-1}{3-1}
=
\frac{3^{n+1}-1}{2}.
$$


### 40

La hipótesis $r\ne0$ autoriza los exponentes enteros y $r\ne1$ permitirá dividir por $1-r$. Primero reindexamos con $j=k-m$:

$$
\sum_{k=m}^{n}r^k
=
r^m\sum_{j=0}^{n-m}r^j.
$$

Para $r\ne1$,

$$
\sum_{j=0}^{n-m}r^j
=
\frac{1-r^{n-m+1}}{1-r}.
$$

Por tanto,

$$
\boxed{
\sum_{k=m}^{n}r^k
=
r^m\frac{1-r^{n-m+1}}{1-r}
}.
$$


### 41

Si $r=1$, la fórmula

$$
\frac{1-r^{n+1}}{1-r}
$$

produce $0/0$, así que no está definida y no puede usarse directamente.

La suma original sí está perfectamente definida:

$$
1+1+\cdots+1,
$$

con $n+1$ términos. Por tanto vale

$$
n+1.
$$


### 42

**Prueba algebraica.** Sea

$$
S=1+2+\cdots+2^n.
$$

Entonces

$$
2S=2+2^2+\cdots+2^{n+1}.
$$

Restando la primera ecuación de la segunda,

$$
2S-S=2^{n+1}-1,
$$

de donde

$$
S=2^{n+1}-1.
$$

**Prueba inductiva.** Para $n=0$,

$$
1=2^1-1.
$$

Supongamos

$$
\sum_{k=0}^{n}2^k=2^{n+1}-1.
$$

Entonces

$$
\sum_{k=0}^{n+1}2^k
=(2^{n+1}-1)+2^{n+1}
=2^{n+2}-1.
$$

La prueba algebraica hace visible la cancelación producida al multiplicar toda la suma por la razón $2$. La inducción muestra cómo la fórmula se propaga al añadir un nuevo término, pero no explica tan directamente por qué aparece la resta de $1$.

## G. Telescopaje


### 43

Usamos

$$
\frac1{k(k+1)}=\frac1k-\frac1{k+1}.
$$

Entonces

$$
\begin{aligned}
\sum_{k=1}^{n}\frac1{k(k+1)}
&=\left(1-\frac12\right)
+\left(\frac12-\frac13\right)
+\cdots
+\left(\frac1n-\frac1{n+1}\right)\\
&=1-\frac1{n+1}\\
&=\frac{n}{n+1}.
\end{aligned}
$$

Los términos interiores se cancelan por pares.


### 44

Primero,

$$
\frac12\left(\frac1k-\frac1{k+2}\right)
=
\frac12\frac{(k+2)-k}{k(k+2)}
=
\frac1{k(k+2)}.
$$

Por tanto,

$$
\sum_{k=1}^{n}\frac1{k(k+2)}
=
\frac12\sum_{k=1}^{n}\left(\frac1k-\frac1{k+2}\right).
$$

Para $n\ge2$, al expandir quedan sin cancelar los dos primeros términos positivos y los dos últimos negativos:

$$
\frac12\left(1+\frac12-\frac1{n+1}-\frac1{n+2}\right).
$$

Para $n=1$, la suma original tiene un solo término, $1/3$. La misma expresión de borde sigue siendo válida: $1/2$ y $-1/(n+1)=-1/2$ se cancelan entre sí y queda $\frac12(1-1/3)=1/3$. No se presupone que existan cuatro términos distintos en este caso corto.

Así,

$$
\boxed{
\sum_{k=1}^{n}\frac1{k(k+2)}
=
\frac{n(3n+5)}{4(n+1)(n+2)}
}.
$$


### 45

Tenemos

$$
\begin{aligned}
\sum_{k=1}^{n}\bigl(k^2-(k-1)^2\bigr)
&=(1^2-0^2)+(2^2-1^2)+\cdots+(n^2-(n-1)^2)\\
&=n^2.
\end{aligned}
$$

Antes de expandir ya puede anticiparse el resultado porque el sumando tiene la forma $F(k)-F(k-1)$ con $F(k)=k^2$; una suma de diferencias consecutivas deja sólo $F(n)-F(0)$.


### 46

Como

$$
2k+1=(k+1)^2-k^2,
$$

tenemos

$$
\begin{aligned}
\sum_{k=0}^{n-1}(2k+1)
&=\sum_{k=0}^{n-1}\bigl((k+1)^2-k^2\bigr)\\
&=(1^2-0^2)+(2^2-1^2)+\cdots+(n^2-(n-1)^2)\\
&=n^2.
\end{aligned}
$$

En el ejercicio 37 la fórmula surgía de ver los impares como una progresión aritmética y promediar extremos. Aquí aparece otra estructura: cada impar es una diferencia de cuadrados consecutivos. La prueba telescópica explica directamente la aparición de $n^2$.


### 47

Usamos

$$
\frac1{(k+1)(k+2)}
=
\frac1{k+1}-\frac1{k+2}.
$$

Entonces

$$
\sum_{k=0}^{n}\frac1{(k+1)(k+2)}
=
1-\frac1{n+2}
=
\boxed{\frac{n+1}{n+2}}.
$$


### 48

La identidad se verifica porque

$$
\frac1{3k+1}-\frac1{3k+4}
=
\frac{3}{(3k+1)(3k+4)}.
$$

Por tanto,

$$
\begin{aligned}
\sum_{k=0}^{n}\frac{3}{(3k+1)(3k+4)}
&=\left(1-\frac14\right)+\left(\frac14-\frac17\right)+\cdots\\
&\quad+\left(\frac1{3n+1}-\frac1{3n+4}\right)\\
&=1-\frac1{3n+4}\\
&=\boxed{\frac{3(n+1)}{3n+4}}.
\end{aligned}
$$


### 49

Calculamos la diferencia propuesta:

$$
\frac1{k(k+1)}-
\frac1{(k+1)(k+2)}
=
\frac{2}{k(k+1)(k+2)}.
$$

Así,

$$
C=\frac12.
$$

Entonces

$$
\begin{aligned}
\sum_{k=1}^{n}\frac1{k(k+1)(k+2)}
&=\frac12\sum_{k=1}^{n}\left(
\frac1{k(k+1)}-
\frac1{(k+1)(k+2)}
\right)\\
&=\frac12\left(\frac12-\frac1{(n+1)(n+2)}\right)\\
&=\boxed{\frac{n(n+3)}{4(n+1)(n+2)}}.
\end{aligned}
$$


### 50

**Prueba telescópica.** Por la identidad local

$$
\frac1{k(k+1)}=\frac1k-\frac1{k+1},
$$

se obtiene

$$
\sum_{k=1}^{n}\frac1{k(k+1)}
=1-\frac1{n+1}
=\frac{n}{n+1}.
$$

**Verificación inductiva.** Para $n=1$,

$$
\frac1{1\cdot2}=\frac12.
$$

Supongamos que la fórmula vale para $n$:

$$
\sum_{k=1}^{n}\frac1{k(k+1)}=\frac{n}{n+1}.
$$

Entonces

$$
\begin{aligned}
\sum_{k=1}^{n+1}\frac1{k(k+1)}
&=\frac{n}{n+1}+\frac1{(n+1)(n+2)}\\
&=\frac{n(n+2)+1}{(n+1)(n+2)}\\
&=\frac{(n+1)^2}{(n+1)(n+2)}\\
&=\frac{n+1}{n+2}.
\end{aligned}
$$

La inducción verifica la propagación de la fórmula. El telescopaje explica mejor su forma: el resultado está determinado por los dos extremos que sobreviven a la cancelación.

## H. Productos finitos


### 51

$$
\prod_{k=2}^{5}(k+1)
=3\cdot4\cdot5\cdot6
=360.
$$


### 52

El producto contiene $n$ factores, todos iguales a $c$:

$$
\prod_{k=1}^{n}c
=\underbrace{c\cdot c\cdots c}_{n\text{ factores}}
=c^n.
$$

Si $n=0$, no aparece ningún factor. Bajo la convención adoptada, el producto vacío vale

$$
1.
$$


### 53

Por expansión,

$$
\prod_{k=m}^{n}a_k
=a_m a_{m+1}\cdots a_r a_{r+1}\cdots a_n.
$$

Separando el bloque en el punto $r$,

$$
(a_m\cdots a_r)(a_{r+1}\cdots a_n)
=
\left(\prod_{k=m}^{r}a_k\right)
\left(\prod_{k=r+1}^{n}a_k\right).
$$

Los rangos son contiguos y no se superponen, de modo que cada factor aparece exactamente una vez.


### 54

Tomamos $j=k+2$. Entonces $k=0$ corresponde a $j=2$ y $k=n-1$ a $j=n+1$. Además, $k+2=j$. Por tanto,

$$
\prod_{k=0}^{n-1}(k+2)
=
\prod_{j=2}^{n+1}j.
$$

El primer rango contiene $n$ valores, pues $(n-1)-0+1=n$. El segundo también contiene

$$
(n+1)-2+1=n
$$

valores.


### 55

Expandimos:

$$
\prod_{k=2}^{n}\frac{k}{k-1}
=
\frac21\cdot\frac32\cdot\frac43\cdots\frac{n}{n-1}.
$$

Cada factor interior $2,3,\ldots,n-1$ aparece una vez en un numerador y una vez en un denominador. Sobreviven $n$ en el numerador final y $1$ en el denominador inicial:

$$
\boxed{n}.
$$


### 56

Para $n=1$:

$$
\frac23.
$$

Para $n=2$:

$$
\frac23\cdot\frac34=\frac12.
$$

Para $n=3$:

$$
\frac23\cdot\frac34\cdot\frac45=\frac25.
$$

En general,

$$
\prod_{k=1}^{n}\frac{k+1}{k+2}
=
\frac23\cdot\frac34\cdots\frac{n+1}{n+2}.
$$

Los factores interiores se cancelan y queda

$$
\boxed{\frac{2}{n+2}}.
$$

Los tres casos calculados coinciden con esta fórmula.

## I. Sumas dobles


### 57

La suma es

$$
(a_{11}+a_{12}+a_{13})+(a_{21}+a_{22}+a_{23}).
$$

Aparecen $2\cdot3=6$ términos.


### 58

Sumando primero respecto de $j$:

$$
\begin{aligned}
\sum_{i=1}^{2}\sum_{j=1}^{3}(i+j)
&=(2+3+4)+(3+4+5)\\
&=9+12\\
&=21.
\end{aligned}
$$

Invirtiendo el orden:

$$
\begin{aligned}
\sum_{j=1}^{3}\sum_{i=1}^{2}(i+j)
&=(2+3)+(3+4)+(4+5)\\
&=5+7+9\\
&=21.
\end{aligned}
$$

Se han recorrido los mismos seis pares $(i,j)$.


### 59

El lado izquierdo suma $a_{ij}$ sobre el conjunto

$$
D=\{(i,j):1\le i\le m,\ 1\le j\le n\}.
$$

El lado derecho usa exactamente el mismo conjunto $D$; sólo recorre primero los valores de $i$ para cada $j$, en lugar de recorrer primero los valores de $j$ para cada $i$.

Como $D$ es finito y cada par aparece exactamente una vez en ambos recorridos,

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=1}^{m}a_{ij}.
$$

La justificación es la igualdad del dominio de pares, no una conmutación formal de símbolos de suma.


### 60

Para un $i$ fijo,

$$
\sum_{j=1}^{n}(a_i+b_j)
=na_i+\sum_{j=1}^{n}b_j.
$$

Ahora sumamos respecto de $i$:

$$
\begin{aligned}
\sum_{i=1}^{m}\sum_{j=1}^{n}(a_i+b_j)
&=\sum_{i=1}^{m}\left(na_i+\sum_{j=1}^{n}b_j\right)\\
&=n\sum_{i=1}^{m}a_i
+m\sum_{j=1}^{n}b_j.
\end{aligned}
$$

El factor $n$ aparece porque cada $a_i$ se repite una vez por cada uno de los $n$ valores de $j$. El factor $m$ aparece porque cada $b_j$ se repite una vez por cada uno de los $m$ valores de $i$.


### 61

Para cada $i$ fijo, el sumando $a_i$ no depende de $j$, así que

$$
\sum_{j=1}^{n}a_i=na_i.
$$

Por tanto,

$$
\sum_{i=1}^{m}\sum_{j=1}^{n}a_i
=
\sum_{i=1}^{m}na_i
=
\boxed{n\sum_{i=1}^{m}a_i}.
$$

La interpretación es multiplicativa: cada $a_i$ aparece exactamente $n$ veces en el rectángulo de índices.


### 62

Para $i$ fijo,

$$
\sum_{j=1}^{n}ij
=i\sum_{j=1}^{n}j.
$$

Entonces

$$
\begin{aligned}
\sum_{i=1}^{m}\sum_{j=1}^{n}ij
&=\sum_{i=1}^{m}i\left(\sum_{j=1}^{n}j\right)\\
&=\left(\sum_{i=1}^{m}i\right)
\left(\sum_{j=1}^{n}j\right).
\end{aligned}
$$

Usando la fórmula de la suma de los primeros enteros positivos,

$$
\boxed{
\sum_{i=1}^{m}\sum_{j=1}^{n}ij
=
\frac{m(m+1)n(n+1)}4
}.
$$

## J. Dominios triangulares


### 63

Los pares son

$$
(1,1),
$$

$$
(2,1),(2,2),
$$

$$
(3,1),(3,2),(3,3),
$$

$$
(4,1),(4,2),(4,3),(4,4).
$$

El dominio contiene $1+2+3+4=10$ pares y forma un triángulo bajo la condición $1\le j\le i\le4$.


### 64

La suma original recorre

$$
D=\{(i,j):1\le j\le i\le n\}.
$$

Si fijamos ahora $j$, la condición del dominio dice que $i$ debe satisfacer

$$
j\le i\le n.
$$

Además $j$ puede tomar los valores $1,\ldots,n$. Por tanto, el mismo conjunto $D$ puede recorrerse como

$$
\sum_{j=1}^{n}\sum_{i=j}^{n}a_{ij}.
$$

Así,

$$
\boxed{
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=j}^{n}a_{ij}
}.
$$


### 65

Primero, para un $i$ fijo hay exactamente $i$ valores de $j$. Así,

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}1
=
\sum_{i=1}^{n}i
=
\frac{n(n+1)}2.
$$

Cambiando el orden,

$$
\sum_{i=1}^{n}\sum_{j=1}^{i}1
=
\sum_{j=1}^{n}\sum_{i=j}^{n}1.
$$

Para un $j$ fijo hay $n-j+1$ valores de $i$, de modo que

$$
\sum_{j=1}^{n}(n-j+1).
$$

Esta lista es $n+(n-1)+\cdots+1$, que también vale

$$
\frac{n(n+1)}2.
$$


### 66

El dominio es $1\le j\le i\le n$. Fijado $j$, el índice $i$ puede tomar los valores

$$
j,j+1,\ldots,n.
$$

Hay

$$
n-j+1
$$

posibilidades. Como el sumando es $x_j$, independiente de $i$,

$$
\sum_{i=j}^{n}x_j=(n-j+1)x_j.
$$

Por tanto,

$$
\boxed{
\sum_{i=1}^{n}\sum_{j=1}^{i}x_j
=
\sum_{j=1}^{n}(n-j+1)x_j
}.
$$

El coeficiente cuenta literalmente la multiplicidad con que $x_j$ aparece en la suma triangular original.

## K. Diagnóstico y comparación de métodos


### 67

El símbolo $k$ no es constante: es el índice ligado que toma sucesivamente los valores $1,2,\ldots,n$. Por eso no puede salir de la suma como un único factor.

La regla correcta es: si $c$ no depende de $k$, entonces

$$
\sum_{k=1}^{n}c a_k
=
c\sum_{k=1}^{n}a_k.
$$


### 68

Si $j=k+1$, deben transformarse simultáneamente el índice, los límites y el sumando. El estudiante transformó correctamente el sumando: $(k+1)^2=j^2$. El error está en dejar los límites $0$ y $n-1$ sin transformar; el nuevo índice comienza en $1$ y termina en $n$.

La transformación correcta es

$$
\sum_{k=0}^{n-1}(k+1)^2
=
\sum_{j=1}^{n}j^2.
$$

En efecto, $k=0$ corresponde a $j=1$ y $k=n-1$ a $j=n$.


### 69

El lado izquierdo recorre

$$
D_1=\{(i,j):1\le j\le i\le n\},
$$

es decir, los pares situados en uno de los dos triángulos del cuadrado de índices.

El lado derecho propuesto recorre

$$
D_2=\{(i,j):1\le i\le j\le n\},
$$

el triángulo opuesto. En general $D_1\ne D_2$.

Para recorrer el mismo dominio $D_1$ fijando primero $j$, debemos usar

$$
\boxed{
\sum_{i=1}^{n}\sum_{j=1}^{i}a_{ij}
=
\sum_{j=1}^{n}\sum_{i=j}^{n}a_{ij}
}.
$$


### 70

**a.** La estructura dominante es la linealidad y el álgebra directa:

$$
\sum_{k=1}^{n}(4k-1)
=4\sum_{k=1}^{n}k-\sum_{k=1}^{n}1
=2n(n+1)-n
=\boxed{n(2n+1)}.
$$

**b.** El método natural es telescopaje, porque el sumando ya es una diferencia consecutiva:

$$
\sum_{k=1}^{n}\bigl((k+1)^3-k^3\bigr)
=(2^3-1^3)+\cdots+((n+1)^3-n^3).
$$

Se cancelan los cubos interiores y queda

$$
\boxed{(n+1)^3-1}.
$$

**c.** El método natural es reindexación. Con $j=k+1$,

$$
\sum_{k=0}^{n-1}a_{k+1}
=
\sum_{j=1}^{n}a_j.
$$

Las dos expresiones son exactamente la misma suma.

**d.** Para una fórmula cerrada conjeturada de una familia definida recursivamente, la inducción suele reflejar mejor la estructura: se comprueba el caso o los casos iniciales y se usa la regla recursiva para pasar del índice $k$ al siguiente. Sin una recurrencia y una fórmula concretas no hay aquí una identidad numérica adicional que calcular; el punto es identificar correctamente el método y el esquema de prueba.


### 71

La inducción parte de un caso inicial y demuestra que, si

$$
1+\cdots+k=\frac{k(k+1)}2,
$$

entonces al añadir $k+1$ se obtiene

$$
\frac{(k+1)(k+2)}2.
$$

Revela una estructura **recursiva**: la fórmula correcta para $k$ fuerza la fórmula correcta para $k+1$.

El apareamiento, en cambio, escribe la suma en los dos órdenes y observa que cada columna suma $n+1$. Revela una estructura **simétrica**: el promedio del primer y último término es $(n+1)/2$ y hay $n$ términos.

Para descubrir la fórmula desde cero elegiría el apareamiento, porque explica directamente por qué aparecen los factores $n$ y $n+1$ y por qué se divide por $2$. La inducción es excelente para verificar una fórmula ya conjeturada, pero no muestra con la misma claridad de dónde proviene.


### 72

Decir «se cancelan casi todos» no basta porque todavía no se ha mostrado qué expresión contiene términos opuestos consecutivos. Primero hay que producir la forma telescópica:

$$
\frac1{k(k+1)}
=
\frac1k-\frac1{k+1}.
$$

Entonces

$$
\begin{aligned}
\sum_{k=1}^{n}\frac1{k(k+1)}
&=\left(1-\frac12\right)
+\left(\frac12-\frac13\right)
+\cdots
+\left(\frac1n-\frac1{n+1}\right)\\
&=1-\frac1{n+1}\\
&=\frac{n}{n+1}.
\end{aligned}
$$

La descomposición local y la exhibición de los extremos sobrevivientes son las dos piezas mínimas que hacen completa la prueba.

## M. Problemas avanzados tipo prueba


### 73

Partimos de

$$
S=\sum_{k=2}^{n+1}(2k-3)a_{k-1}.
$$

**Primera reindexación.** Tomamos

$$
j=k-1,
\qquad
k=j+1.
$$

Los extremos cambian como

$$
k=2\Rightarrow j=1,
\qquad
k=n+1\Rightarrow j=n.
$$

El sumando se transforma en

$$
(2(j+1)-3)a_j=(2j-1)a_j.
$$

Así,

$$
\boxed{S=\sum_{j=1}^{n}(2j-1)a_j}.
$$

**Segunda reindexación.** Ahora tomamos

$$
r=n+1-j,
\qquad
j=n+1-r.
$$

Cuando $j=1$, $r=n$; cuando $j=n$, $r=1$. El nuevo parámetro recorre el rango en orden inverso. Reordenándolo de $1$ a $n$, el sumando queda

$$
(2(n+1-r)-1)a_{n+1-r}
=(2n+1-2r)a_{n+1-r}.
$$

Por tanto,

$$
\boxed{S=\sum_{r=1}^{n}(2n+1-2r)a_{n+1-r}}.
$$

Para $n\ge2$, la expresión original comienza y termina como

$$
a_1+3a_2+\cdots+(2n-3)a_{n-1}+(2n-1)a_n.
$$

La primera reindexación produce exactamente la misma secuencia. La segunda la escribe en orden inverso:

$$
(2n-1)a_n+(2n-3)a_{n-1}+\cdots+3a_2+a_1.
$$

Las dos primeras y las dos últimas contribuciones coinciden, salvo por el orden. Para $n=1$ sólo existe un término, $S=a_1$, y las tres representaciones también coinciden.


### 74

Buscamos $F(k)$ con

$$
F(k)-F(k-1)=k(k+1).
$$

Una elección natural es

$$
F(k)=\frac{k(k+1)(k+2)}3.
$$

En efecto,

$$
\begin{aligned}
F(k)-F(k-1)
&=\frac{k(k+1)(k+2)}3-\frac{(k-1)k(k+1)}3\\
&=\frac{k(k+1)}3\bigl((k+2)-(k-1)\bigr)\\
&=k(k+1).
\end{aligned}
$$

Por telescopaje,

$$
\begin{aligned}
\sum_{k=1}^{n}k(k+1)
&=\sum_{k=1}^{n}\bigl(F(k)-F(k-1)\bigr)\\
&=F(n)-F(0)\\
&=\boxed{\frac{n(n+1)(n+2)}3}.
\end{aligned}
$$

**Verificación inductiva.** Para $n=1$,

$$
1\cdot2=2=\frac{1\cdot2\cdot3}{3}.
$$

Supongamos

$$
\sum_{k=1}^{n}k(k+1)=\frac{n(n+1)(n+2)}3.
$$

Al añadir el término $(n+1)(n+2)$,

$$
\begin{aligned}
\sum_{k=1}^{n+1}k(k+1)
&=\frac{n(n+1)(n+2)}3+(n+1)(n+2)\\
&=(n+1)(n+2)\left(\frac n3+1\right)\\
&=\frac{(n+1)(n+2)(n+3)}3.
\end{aligned}
$$

La inducción confirma la fórmula. El telescopaje explica más directamente el producto de tres enteros consecutivos: éste aparece ya en la función $F(k)$ cuya diferencia finita es $k(k+1)$.


### 75

Buscamos una diferencia de términos consecutivos. Observamos que

$$
\frac1{k(k+1)}-\frac1{(k+1)(k+2)}
=
\frac{2}{k(k+1)(k+2)}.
$$

Por tanto,

$$
\boxed{
\frac1{k(k+1)(k+2)}
=
\frac12\left(
\frac1{k(k+1)}-\frac1{(k+1)(k+2)}
\right)
}.
$$

Sumando desde $k=1$ hasta $n$,

$$
\begin{aligned}
\sum_{k=1}^{n}\frac1{k(k+1)(k+2)}
&=\frac12\left[
\left(\frac1{1\cdot2}-\frac1{2\cdot3}\right)
+\cdots
+\left(\frac1{n(n+1)}-\frac1{(n+1)(n+2)}\right)
\right]\\
&=\frac12\left(\frac12-\frac1{(n+1)(n+2)}\right).
\end{aligned}
$$

Llevando a una sola fracción,

$$
\begin{aligned}
\frac14-\frac1{2(n+1)(n+2)}
&=\frac{(n+1)(n+2)-2}{4(n+1)(n+2)}\\
&=\boxed{\frac{n(n+3)}{4(n+1)(n+2)}}.
\end{aligned}
$$


### 76

Separamos el producto:

$$
\prod_{k=2}^{n}\frac{(k-1)(k+2)}{k(k+1)}
=
\left(\prod_{k=2}^{n}\frac{k-1}{k}\right)
\left(\prod_{k=2}^{n}\frac{k+2}{k+1}\right).
$$

El primer factor es

$$
\frac12\cdot\frac23\cdot\frac34\cdots\frac{n-1}{n}
=\frac1n.
$$

El segundo es

$$
\frac43\cdot\frac54\cdot\frac65\cdots\frac{n+2}{n+1}
=\frac{n+2}{3}.
$$

Por tanto,

$$
\boxed{
\prod_{k=2}^{n}\frac{(k-1)(k+2)}{k(k+1)}
=
\frac{n+2}{3n}
}.
$$

**Auditoría de extremos.** Para $n=2$,

$$
\frac{1\cdot4}{2\cdot3}=\frac23,
$$

y la fórmula da $4/6=2/3$.

Para $n=3$,

$$
\frac23\cdot\frac56=\frac59,
$$

y la fórmula da $5/9$.


### 77

**Primer recorrido: sumar respecto de $j$.** Para $i$ fijo,

$$
\sum_{j=1}^{n}(x_i-y_j)
=nx_i-\sum_{j=1}^{n}y_j.
$$

Luego

$$
\begin{aligned}
S
&=\sum_{i=1}^{m}\left(nx_i-\sum_{j=1}^{n}y_j\right)\\
&=n\sum_{i=1}^{m}x_i-m\sum_{j=1}^{n}y_j.
\end{aligned}
$$

**Segundo recorrido: invertir primero el orden.** Como el dominio es el rectángulo

$$
\{1,\ldots,m\}\times\{1,\ldots,n\},
$$

podemos escribir

$$
S=\sum_{j=1}^{n}\sum_{i=1}^{m}(x_i-y_j).
$$

Para $j$ fijo,

$$
\sum_{i=1}^{m}(x_i-y_j)
=\sum_{i=1}^{m}x_i-my_j.
$$

Así,

$$
S=n\sum_{i=1}^{m}x_i-m\sum_{j=1}^{n}y_j.
$$

La interpretación de multiplicidades es inmediata: cada $x_i$ aparece una vez por cada uno de los $n$ valores de $j$, mientras que cada $y_j$ aparece con signo negativo una vez por cada uno de los $m$ valores de $i$.


### 78

Tenemos

$$
S_n=\sum_{i=1}^{n}\sum_{j=1}^{i}(b_j-b_{j+1}).
$$

**Método 1: telescopar primero.** Para cada $i$,

$$
\sum_{j=1}^{i}(b_j-b_{j+1})
=b_1-b_{i+1}.
$$

Por tanto,

$$
\begin{aligned}
S_n
&=\sum_{i=1}^{n}(b_1-b_{i+1})\\
&=nb_1-\sum_{i=1}^{n}b_{i+1}\\
&=\boxed{nb_1-\sum_{r=2}^{n+1}b_r}.
\end{aligned}
$$

**Método 2: cambiar primero el orden.** El dominio es $1\le j\le i\le n$, de modo que

$$
S_n
=
\sum_{j=1}^{n}\sum_{i=j}^{n}(b_j-b_{j+1}).
$$

Para $j$ fijo hay $n-j+1$ valores de $i$, así que

$$
S_n
=
\sum_{j=1}^{n}(n-j+1)(b_j-b_{j+1}).
$$

Separamos las dos sumas y reindexamos la segunda con $r=j+1$:

$$
\begin{aligned}
S_n
&=\sum_{j=1}^{n}(n-j+1)b_j
-\sum_{r=2}^{n+1}(n-r+2)b_r.
\end{aligned}
$$

El coeficiente de $b_1$ es $n$. Para $2\le r\le n$, la diferencia de coeficientes es

$$
(n-r+1)-(n-r+2)=-1,
$$

y $b_{n+1}$ aparece sólo en la segunda suma con coeficiente $-1$. Por tanto,

$$
S_n
=nb_1-b_2-\cdots-b_{n+1}
=\boxed{nb_1-\sum_{r=2}^{n+1}b_r}.
$$

Los dos procedimientos recorren la misma suma finita, pero revelan estructuras distintas: el primero explota cancelación local; el segundo, multiplicidades del dominio triangular.


### 79

Hay varias estrategias posibles.

1. **Telescopaje:** observar que el sumando puede ser una diferencia de cubos consecutivos.
2. **Inducción:** verificar la fórmula para $n=1$ y demostrar el paso $n\to n+1$.
3. **Álgebra directa:** separar $3\sum k^2+3\sum k+\sum1$, pero esto exige además una fórmula cerrada para $\sum k^2$, que no es necesaria si se reconoce la estructura local.

La estrategia más informativa es el telescopaje, porque

$$
(k+1)^3-k^3=3k^2+3k+1.
$$

Por tanto,

$$
\begin{aligned}
\sum_{k=1}^{n}(3k^2+3k+1)
&=\sum_{k=1}^{n}\bigl((k+1)^3-k^3\bigr)\\
&=(2^3-1^3)+(3^3-2^3)+\cdots+((n+1)^3-n^3)\\
&=\boxed{(n+1)^3-1}.
\end{aligned}
$$

La forma cerrada deja de parecer accidental: sólo sobreviven el cubo final y el cubo inicial.

Como segunda estrategia, la inducción comienza con

$$
7=2^3-1.
$$

Si la fórmula vale para $n$, al añadir el término correspondiente a $n+1$ se añade

$$
3(n+1)^2+3(n+1)+1=(n+2)^3-(n+1)^3,
$$

y se obtiene $(n+2)^3-1$. La inducción confirma la fórmula, pero oculta parcialmente la cadena completa de cancelaciones que el telescopaje exhibe de una sola vez.


### 80

La identidad local

$$
\frac1{k(k+1)}=\frac1k-\frac1{k+1}
$$

es correcta. El error comienza al tratar la segunda sumatoria.

Partimos legítimamente de

$$
\sum_{k=1}^{n}\frac1{k(k+1)}
=
\sum_{k=1}^{n}\frac1k-
\sum_{k=1}^{n}\frac1{k+1}.
$$

A partir de aquí hay que distinguir dos operaciones.

**1. Renombrar el índice.** Si sólo cambiamos la letra $k$ por $j$, la segunda suma se convierte en

$$
\sum_{j=1}^{n}\frac1{j+1},
$$

no en $\sum_{j=1}^{n}1/j$. El sumando debe conservar la misma dependencia funcional del índice.

**2. Reindexar para que el sumando sea $1/j$.** Si tomamos

$$
j=k+1,
$$

entonces $k=j-1$. Los límites también cambian:

$$
k=1\Rightarrow j=2,
\qquad
k=n\Rightarrow j=n+1.
$$

Por tanto,

$$
\sum_{k=1}^{n}\frac1{k+1}
=
\sum_{j=2}^{n+1}\frac1j.
$$

El estudiante cambió el sumando como si hubiera reindexado, pero dejó los límites como si sólo hubiera renombrado. Esas dos operaciones no pueden mezclarse.

Además, cambiar después únicamente el límite superior de una suma no es una transformación inocua: añade un término nuevo. Los límites correctos $2$ y $n+1$ deben derivarse de la sustitución $j=k+1$, no elegirse para forzar el resultado.

La prueba correcta es entonces

$$
\begin{aligned}
\sum_{k=1}^{n}\frac1{k(k+1)}
&=\sum_{k=1}^{n}\frac1k-
\sum_{j=2}^{n+1}\frac1j\\
&=\left(1+\frac12+\cdots+\frac1n\right)
-\left(\frac12+\cdots+\frac1n+\frac1{n+1}\right)\\
&=1-\frac1{n+1}\\
&=\boxed{\frac{n}{n+1}}.
\end{aligned}
$$

Los términos interiores se cancelan porque las dos listas coinciden desde $1/2$ hasta $1/n$. Los extremos que no tienen pareja son exactamente $1$ y $-1/(n+1)$.

***
## N. Rangos, dominios y cancelación con restricciones


### 81

Toma $j=k+n$, de modo que $k=j-n$. Los extremos $k=-n,n$ pasan a $j=0,2n$, y $a_{2k+1}=a_{2j-2n+1}$. Por tanto $\sum_{k=-n}^{n}a_{2k+1}=\sum_{j=0}^{2n}a_{2j-2n+1}$. La traslación es uno a uno y cubre exactamente $2n+1$ índices; sus términos extremos son $a_{1-2n}$ y $a_{1+2n}$. Para $n=0$ ambas sumas contienen sólo $a_1$.


### 82

La sustitución tiene inversa $k=m+n-j$. Lleva $k=m$ a $j=n$ y $k=n$ a $j=m$, recorriendo el intervalo entero en sentido contrario. El sumando se convierte en $(n-j)a_{m+n-j}$. Como la suma es finita, puede escribirse en orden ascendente: $\sum_{k=m}^{n}(k-m)a_k=\sum_{j=m}^{n}(n-j)a_{m+n-j}$. El coeficiente cero del primer término original corresponde al último término del nuevo recorrido; no se pierde. Si $m=n$, cada suma tiene un solo sumando, $0a_m=0$.


### 83

El conjunto es $J_n=\{3k+2:0\le k\le n\}=\{2,5,8,\ldots,3n+2\}$, y la suma es $\sum_{j\in J_n}a_j$. La correspondencia $k\mapsto3k+2$ es uno a uno, con inversa $(j-2)/3$ para los $j$ de ese conjunto. Contiene $n+1$ términos. La suma sobre todos los enteros del intervalo añade términos; por ejemplo, fija $a_3=1$ y todos los demás $a_j=0$. Para cualquier $n\ge1$, la suma original vale $0$ y la suma propuesta vale $1$. Para $n=0$, $J_0=\{2\}$ y no hay huecos.


### 84

Separa los índices negativos, cero y positivos. El término $k=0$ vale cero. En la parte negativa usa $j=-k$: $\sum_{k=-n}^{-1}k a_k=-\sum_{j=1}^{n}j a_{-j}$. La parte positiva es $\sum_{j=1}^{n}j a_j$, y la linealidad da la identidad. La simetría empareja índices, pero los valores de la familia pueden ser distintos: con $n=1$, $a_1=1$ y $a_{-1}=0$, el resultado es $1$. Si $a_j=a_{-j}$ para todos los $j=1,\ldots,n$, cada diferencia se anula y la suma vale cero. Para $n=0$, ambas expresiones valen cero por el término nulo y la suma vacía, respectivamente.


### 85

El dominio es $1\le i\le n$, $i\le j\le i+2$. El índice $j$ recorre $1,\ldots,n+2$. Fijado $j$, las dos últimas desigualdades equivalen a $j-2\le i\le j$; combinadas con $1\le i\le n$ dan $\max(1,j-2)\le i\le\min(n,j)$. Así la suma es $\sum_{j=1}^{n+2}\sum_{i=\max(1,j-2)}^{\min(n,j)}a_{ij}$. En la primera columna sólo está $(1,1)$ y en la última sólo $(n,n+2)$. Cada fila original tiene tres pares y el nuevo recorrido conserva exactamente esos $3n$ pares; no intercambia los subíndices del sumando.


### 86

Las condiciones son $i\ge1$, $j\ge1$ e $i+j\le n$. Hay valores de $j$ desde $1$ hasta $n-1$; fijado $j$, $i$ recorre $1,\ldots,n-j$. Por tanto la suma es $\sum_{j=1}^{n-1}\sum_{i=1}^{n-j}a_{ij}$. La fila $i=n$ tiene rango interior vacío y aporta cero. El número de pares es $\sum_{i=1}^{n}(n-i)=n(n-1)/2$. Para $n=1$ el dominio entero es vacío: en el recorrido original la única fila es vacía y en el nuevo la suma exterior también lo es. Ningún término $a_{11}$ aparece.


### 87

El dominio cumple $1\le i\le2n$, $1\le j\le n$ y $j\le i$. Fijado $j\in\{1,\ldots,n\}$, $i$ recorre $j,\ldots,2n$. La suma queda $\sum_{j=1}^{n}\sum_{i=j}^{2n}a_{ij}$. Cada columna tiene $2n-j+1$ pares, por lo que el total es $n(2n+1)-n(n+1)/2=n(3n+1)/2$. Por filas, los primeros $n$ tamaños son $1,2,\ldots,n$ y los siguientes $n$ son todos $n$, lo que da el mismo total. Hay una zona triangular y una rectangular; extender el límite exterior a $2n$ no extiende el límite de $j$ más allá de $n$.


### 88

El dominio es el cuadrado $1\le i,j\le n$ sin la diagonal $i=j$. Para cada $j$, los índices admisibles son $i=1,\ldots,j-1$ y $i=j+1,\ldots,n$. Así obtenemos $\sum_{j=1}^{n}[\sum_{i=1}^{j-1}a_{ij}+\sum_{i=j+1}^{n}a_{ij}]$. Los bloques son disjuntos: uno satisface $i<j$ y el otro $i>j$; todo par no diagonal pertenece exactamente a uno. Hay $n$ filas con $n-1$ pares cada una, en total $n(n-1)$. Para $n=1$, ambos bloques son vacíos y el resultado es cero.


### 89

Los cuadrados del denominador sugieren comparar sus recíprocos. Al restar, $1/(k+1)^2-1/(k+2)^2=[(k+2)^2-(k+1)^2]/[(k+1)^2(k+2)^2]=(2k+3)/[(k+1)^2(k+2)^2]$. Todos los denominadores son positivos. La suma se convierte en $(1/2^2-1/3^2)+(1/3^2-1/4^2)+\cdots+(1/(n+1)^2-1/(n+2)^2)$. Los términos interiores tienen parejas opuestas y quedan $1/4-1/(n+2)^2$. Para $n=1$, el resultado es $5/36$, igual al único sumando. La identidad local muestra por qué el numerador tiene precisamente la forma $2k+3$.


### 90

Se tiene $1/k^2-1/(k+2)^2=[(k+2)^2-k^2]/[k^2(k+2)^2]=4(k+1)/[k^2(k+2)^2]$. Así la suma es $\sum_{k=1}^{n}1/k^2-\sum_{j=3}^{n+2}1/j^2$, tras reindexar la segunda parte con $j=k+2$. Para $n\ge2$ se cancelan los índices comunes y queda $1+1/4-1/(n+1)^2-1/(n+2)^2$. El desplazamiento dos deja dos términos en cada borde. Para $n=1$, la fórmula también es válida: los términos $1/4$ y $-1/(n+1)^2=-1/4$ se anulan entre sí y queda $1-1/9=8/9$, exactamente el sumando original. No se presupone que los bloques interiores existan en ese caso corto.


### 91

El sumando tiene tres factores consecutivos. Probamos $F(k)=c\,k(k+1)(k+2)(k+3)$: al restar $F(k-1)$, los tres factores comunes se conservan y sólo cambia el extremo. En efecto, $F(k)-F(k-1)=c\,k(k+1)(k+2)[(k+3)-(k-1)]=4c\,k(k+1)(k+2)$. Elegimos $c=1/4$. La suma es entonces $\sum_{k=1}^{n}[F(k)-F(k-1)]=F(n)-F(0)=n(n+1)(n+2)(n+3)/4$. La cancelación deja los valores de borde; para $n=1$ se obtiene $6=1\cdot2\cdot3$. La elección de cuatro factores se justifica por el factor constante que aparece al restar sus extremos.


### 92

La diferencia de cuadrados da $1-1/(k+2)^2=(k+1)(k+3)/(k+2)^2$. Por tanto el producto se separa en $[\prod_{k=0}^{n}(k+1)/(k+2)] [\prod_{k=0}^{n}(k+3)/(k+2)]$. El primero deja $1/(n+2)$ y el segundo $(n+3)/2$, pues los factores interiores se cancelan en ambos y todos los denominadores son positivos. El resultado es $(n+3)/[2(n+2)]$. Para $n=0$ hay un factor, no un producto vacío: $1-1/4=3/4$, que coincide con la fórmula.


### 93

El producto está definido exactamente para $t\notin\{-1,-2,\ldots,-n\}$, porque cada denominador es $k+t$. Dentro de ese dominio vale cero exactamente para $t\in\{1,2,\ldots,n\}$: allí hay un numerador cero; fuera de esos valores todos los factores son no nulos y su producto finito no es cero. Para formar también $P_n(-t)$ deben excluirse los valores positivos $1,\ldots,n$. Por ello la identidad recíproca vale para $t\notin\{-n,\ldots,-1,1,\ldots,n\}$: cada pareja de factores $(k-t)/(k+t)$ y $(k+t)/(k-t)$ está definida y su producto es $1$. Para $t=0$ todos los factores valen $1$ y la identidad se cumple. Un cero de $P_n$ no autoriza multiplicarlo por un supuesto recíproco indefinido.


### 94

Deben excluirse $t=0,-1,\ldots,-n$. Para $n\ge1$, el numerador recorre $t+2,\ldots,t+n+2$ y el denominador $t,\ldots,t+n$. Los factores comunes, cuando los hay, son no nulos dentro del dominio. Quedan $Q_n(t)=(t+n+1)(t+n+2)/[t(t+1)]$. En $n=1$ no hay factores comunes: la fórmula representa directamente los dos factores originales. Los únicos ceros admisibles son $t=-n-1$ y $t=-n-2$. Los demás ceros del numerador están en la lista excluida de denominadores. Para $n=2,t=-1$, un denominador original vale cero y el producto no está definido. La identidad local puede separar dos productos de desplazamiento uno, pero antes de hacerlo hay que mantener todas las exclusiones del producto original.


### 95

Ningún denominador depende de $t$ y los índices presentes son enteros positivos. Por ello el dominio es todo $\mathbb R$. Si $n\ge1$, el producto vale cero exactamente para $t=1,\ldots,n$; si ningún factor es cero, un producto finito de reales no nulos tampoco lo es. En $t=0$ todos los factores son $1$. En $t=-1$, $R_n(-1)=\prod_{k=1}^{n}(k+1)/k=n+1$ por telescopaje. Si $n=0$, el rango es vacío, de modo que $R_0(t)=1$ para todo $t$, sin ceros; las dos fórmulas de valores especiales siguen dando $1$. Un dominio vacío de índices no exige evaluar la expresión del factor en un índice inexistente.


### 96

En $A_n$ aparece $k=1$: numerador y denominador valen cero, de modo que ese factor no está definido y tampoco lo está $A_n$. La factorización $(k^2-1)/(k^2-k)=(k-1)(k+1)/[(k-1)k]=(k+1)/k$ sólo es válida para $k\ne0,1$; no permite restaurar el factor excluido. En $B_n$, los índices presentes son $k\ge2$, por lo que la cancelación es legítima. Para $n\ge2$ queda $\prod_{k=2}^{n}(k+1)/k=(n+1)/2$. Para $n=1$, el producto es vacío y vale $1$, que coincide con $(n+1)/2$. La propuesta asigna a $A_n$ el valor de una expresión distinta, obtenida ampliando ilegítimamente el dominio del factor.

***

[← Capítulo 11](algebra-para-matematicos-capitulo-11-induccion-buen-orden-y-recursion.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 13 →](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md)

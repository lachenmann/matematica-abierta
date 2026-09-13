75. Usando $A\triangle B=(A\setminus B)\cup(B\setminus A)$, demuestra que la diferencia simétrica es asociativa:

$$
(A\triangle B)\triangle C=A\triangle(B\triangle C).
$$

Tu demostración debe explicar por qué un elemento pertenece a cualquiera de los dos lados exactamente cuando pertenece a un número impar de los conjuntos $A,B,C$.

76. Sea $U$ un universo fijo y sean $A,B\subseteq U$. Estudia la ecuación de conjuntos

$$
X\cap A=B.
$$

(a) Determina una condición necesaria y suficiente sobre $A$ y $B$ para que exista al menos una solución $X\subseteq U$.  
(b) Bajo esa condición, describe **todas** las soluciones.  
(c) Demuestra que tu descripción es completa.

77. Sea $U$ un universo fijo y sean $A,B\subseteq U$. Estudia la ecuación

$$
X\cup A=B.
$$

(a) Determina una condición necesaria y suficiente para que exista solución.  
(b) Caracteriza todas las soluciones mediante inclusiones.  
(c) Da una parametrización de todas las soluciones usando un subconjunto arbitrario de $A$.

78. Sean $A,B,C,D$ conjuntos. Demuestra que

$$
A\times B\subseteq C\times D
$$

si y sólo si se cumple al menos una de las siguientes condiciones:

- $A=\varnothing$;
- $B=\varnothing$;
- $A\subseteq C$ y $B\subseteq D$.

Tu prueba debe justificar por qué la no vacuidad es indispensable para deducir las dos inclusiones coordenada a coordenada.

79. Supón que

$$
A\cup C=B\cup C
$$

y

$$
A\cap C=B\cap C.
$$

Demuestra que $A=B$. Luego muestra, mediante contraejemplos, que ninguna de las dos hipótesis por separado basta para concluir la igualdad.

80. Para $A,B\subseteq U$, demuestra que las siguientes cinco afirmaciones son equivalentes:

1. $A\subseteq B$;
2. $A\cap B=A$;
3. $A\cup B=B$;
4. $A\setminus B=\varnothing$;
5. $\mathcal P(A)\subseteq\mathcal P(B)$.

Organiza la demostración de manera eficiente, indicando una cadena de implicaciones suficiente para establecer la equivalencia de las cinco condiciones.

# Soluciones


## A. Pertenencia y descripción

### 1
Son verdaderas $4\in A$ y $\{4\}\subseteq A$. Son falsas $5\in A$ y $\{4\}\in A$. El número $4$ es un elemento de $A$; el conjunto $\{4\}$ no aparece como elemento, pero todos sus elementos —sólo $4$— pertenecen a $A$.

### 2
El conjunto es $\{-2,-1,0,1,2\}$.

### 3
Una descripción posible es $\{n^2:n\in\mathbb N,\ 1\le n\le5\}$. Otra es $\{m\in\mathbb N: m=n^2\text{ para algún }n\in\{1,2,3,4,5\}\}$.

### 4
Ambas escrituras contienen exactamente los elementos $1,2,3$. En un conjunto, el orden de enumeración y la repetición no alteran la pertenencia. Por extensionalidad, los conjuntos son iguales.

### 5
Los enteros cuyos cuadrados son menores que $5$ son $-2,-1,0,1,2$, pues sus cuadrados son $4,1,0,1,4$. Por tanto $A=\{-2,-1,0,1,2\}$.

### 6
Si $x\in A$, entonces $x^2=4$, de modo que $(x-2)(x+2)=0$ y $x=2$ o $x=-2$; así $x\in B$. Recíprocamente, si $x\in B$, entonces $x=2$ o $x=-2$, y en ambos casos $x^2=4$. Luego $A=B$.


## B. Vacío, unitarios y notación

### 7
$\varnothing$ tiene $0$ elementos. $\{\varnothing\}$ tiene $1$ elemento, a saber $\varnothing$. $\{\{\varnothing\}\}$ también tiene $1$ elemento, pero ese elemento es $\{\varnothing\}$.

### 8
Ambas son verdaderas, pero por razones distintas. La primera es verdadera porque $\varnothing$ aparece como elemento. La segunda es verdadera porque el conjunto vacío es subconjunto de todo conjunto.

### 9
Las cuatro afirmaciones son verdaderas. $1$ y $\{1\}$ aparecen como elementos; como $1\in A$, el conjunto unitario $\{1\}$ es subconjunto de $A$; y $\varnothing$ también aparece como elemento.

### 10
Por ejemplo $A=\{\varnothing\}$. Entonces $\varnothing\in A$, mientras $\{\varnothing\}$ no es uno de sus elementos: el único elemento de $A$ es $\varnothing$.

### 11
Por ejemplo $A=\{\varnothing,1\}$. Como $\varnothing\in A$, se tiene $\{\varnothing\}\subseteq A$. Pero $\{\varnothing\}$ no es elemento de $A$; los elementos son $\varnothing$ y $1$.

### 12
Por definición, $\varnothing$ no tiene elementos. Por tanto no hay ningún caso que satisfaga el antecedente $x\in\varnothing$. En una afirmación universal $\forall x\,(x\in\varnothing\Rightarrow P(x))$, el antecedente es falso para todo $x$, de modo que la implicación resulta verdadera para cada caso. Ésta es la razón lógica de $\varnothing\subseteq A$ para todo $A$.


## C. Subconjuntos e igualdad

### 13
$A\subseteq B$ es verdadera. $B\subseteq A$ es falsa porque $3\in B$ y $3\notin A$. $A\in B$ es falsa: los elementos de $B$ son números, no el conjunto $A$. La escritura $2\subseteq B$ no es apropiada en este contexto porque $2$ no se está tratando como un conjunto.

### 14
Por definición, necesitaríamos verificar que todo $x\in\varnothing$ pertenece a $A$. Pero no existe ningún $x\in\varnothing$. Por tanto no hay contraejemplo a la implicación $x\in\varnothing\Rightarrow x\in A$, y se concluye $\varnothing\subseteq A$.

### 15
Sea $x\in A$. Como $A\subseteq B$, se sigue $x\in B$. Como $B\subseteq C$, se sigue $x\in C$. Por tanto todo elemento de $A$ pertenece a $C$, es decir, $A\subseteq C$.

### 16
Cada elemento de $A$ es uno de $1,2,3$ y pertenece a $B$, así que $A\subseteq B$. Recíprocamente, cada elemento de $B$ es uno de $1,2,3$ y pertenece a $A$, así que $B\subseteq A$. Por doble inclusión, $A=B$.

### 17
Si $x\in A$, entonces $x$ es un entero entre $-1$ y $2$, de modo que necesariamente $x\in\{-1,0,1,2\}=B$. Recíprocamente, cada elemento de $B$ es entero y satisface $-1\le x\le2$, por lo que pertenece a $A$. Por doble inclusión, $A=B$.

### 18
Toma $A=\{1\}$ y $B=\{1,2\}$. Se cumple $A\subseteq B$, pero $2\in B$ y $2\notin A$, así que $A\ne B$.

### 19
Las dos inclusiones dicen exactamente que todo elemento de $A$ está en $B$ y todo elemento de $B$ está en $A$. Por extensionalidad, ambos conjuntos tienen los mismos elementos, independientemente de cómo estén descritos. Por tanto $A=B$.

### 20
Sí. Sea $x\in A$. De $A\subseteq B$ obtenemos $x\in B$, y de $A\subseteq C$, $x\in C$. Por definición de intersección, $x\in B\cap C$. Luego $A\subseteq B\cap C$.


## D. Conjunto potencia

### 21
Los subconjuntos son $\varnothing$, $\{a\}$, $\{b\}$ y $\{a,b\}$. Por tanto $\mathcal P(\{a,b\})=\{\varnothing,\{a\},\{b\},\{a,b\}\}$.

### 22
Hay $2^3=8$ subconjuntos: $\varnothing$, $\{1\}$, $\{2\}$, $\{3\}$, $\{1,2\}$, $\{1,3\}$, $\{2,3\}$ y $\{1,2,3\}$.

### 23
$1\in\mathcal P(A)$ es falsa porque los elementos de $\mathcal P(A)$ son subconjuntos de $A$, y en este contexto $1$ no es uno de ellos. Las otras tres son verdaderas: $\{1\}\subseteq A$, $A\subseteq A$ y $\varnothing\subseteq A$.

### 24
Sea $X$ un conjunto. $X\in\mathcal P(A\cap B)$ equivale a $X\subseteq A\cap B$. Esto ocurre exactamente cuando $X\subseteq A$ y $X\subseteq B$. A su vez, eso equivale a $X\in\mathcal P(A)$ y $X\in\mathcal P(B)$, es decir, $X\in\mathcal P(A)\cap\mathcal P(B)$. Por extensionalidad, los conjuntos son iguales.

### 25
No. Toma $A=\{1\}$ y $B=\{2\}$. Entonces $\{1,2\}\in\mathcal P(A\cup B)$, pero $\{1,2\}\notin\mathcal P(A)$ y $\{1,2\}\notin\mathcal P(B)$. Por tanto no pertenece a $\mathcal P(A)\cup\mathcal P(B)$.

### 26
Si $|A|=n$, entonces $|\mathcal P(A)|=2^n$. Como $32=2^5$, se sigue $n=5$. Por tanto $A$ tiene $5$ elementos.


## E. Unión e intersección

### 27
$A\cup B=\{1,2,3,4,5\}$ y $A\cap B=\{3,4\}$.

### 28
Un entero pertenece a ambos conjuntos exactamente cuando $0\le x\le2$. Por tanto $A\cap B=\{0,1,2\}$.

### 29
Todo entero satisface al menos una de las condiciones $x\ge0$ o $x\le2$; de hecho, ambas cubren conjuntamente a todos los enteros. Por tanto $A\cup B=\mathbb Z$.

### 30
Si $x\in A\cap B$, entonces por definición $x\in A$, de modo que $A\cap B\subseteq A$. Si $x\in A$, entonces la disyunción $x\in A$ o $x\in B$ es verdadera, así $x\in A\cup B$. Por tanto $A\subseteq A\cup B$.

### 31
Para cualquier $x$, $x\in A\cup\varnothing$ equivale a $(x\in A)\lor(x\in\varnothing)$. La segunda proposición es siempre falsa, así que la condición equivale a $x\in A$. Por extensionalidad, $A\cup\varnothing=A$.

### 32
Para cualquier $x$, $x\in A\cap A$ equivale a $(x\in A)\land(x\in A)$, que es lógicamente equivalente a $x\in A$. Luego $A\cap A=A$.

### 33
Para la unión, todo elemento de $B$ pertenece a $A\cup B$, y si $x\in A\cup B$, entonces $x\in A$ o $x\in B$; en el primer caso $A\subseteq B$ da $x\in B$, y en el segundo ya lo sabemos. Así $A\cup B=B$. Para la intersección, $A\cap B\subseteq A$ siempre, y si $x\in A$, la hipótesis da $x\in B$, por lo que $x\in A\cap B$. Entonces $A\cap B=A$.

### 34
Sí. Si $x\in A$, entonces como $A=A\cap B$, se tiene $x\in A\cap B$. Por definición de intersección, $x\in B$. Por tanto $A\subseteq B$.


## F. Diferencia y complemento

### 35
$A\setminus B=\{1,2\}$ y $B\setminus A=\{5\}$. Esto muestra que la diferencia no es conmutativa.

### 36
Respecto de $U$, $A^c=U\setminus A=\{2,4\}$.

### 37
Con $U=\{1,2,3\}$, $A^c=\{3\}$. Con $V=\{1,2,3,4\}$, $A^c=\{3,4\}$. El símbolo $A^c$ sólo queda determinado cuando el universo está fijado.

### 38
Para cualquier $x$, $x\in A\setminus B$ equivale a $x\in A$ y $x\notin B$. Respecto del universo fijado, $x\notin B$ equivale a $x\in B^c$. Por tanto la condición equivale a $x\in A\cap B^c$. Por extensionalidad, $A\setminus B=A\cap B^c$.

### 39
Para cualquier $x\in U$, $x\in(A^c)^c$ equivale a $x\notin A^c$, que equivale a no ser cierto que $x\notin A$, es decir, $x\in A$. Por extensionalidad, $(A^c)^c=A$.

### 40
Para $x\in U$,
$x\in(A\cup B)^c$ equivale a $x\notin A\cup B$. Esto equivale a negar $[(x\in A)\lor(x\in B)]$, que por De Morgan es $(x\notin A)\land(x\notin B)$. Eso equivale a $x\in A^c\cap B^c$. Por extensionalidad, los conjuntos son iguales.

### 41
Sí. Usando diferencia como intersección con complemento y De Morgan:
$A\setminus(B\cup C)=A\cap(B\cup C)^c=A\cap(B^c\cap C^c)=(A\cap B^c)\cap(A\cap C^c)=(A\setminus B)\cap(A\setminus C)$.

### 42
Toma $A=\{1\}$, $B=\{1\}$ y $C=\{1\}$. Entonces $B\setminus C=\varnothing$, así que $A\setminus(B\setminus C)=A=\{1\}$. En cambio $A\setminus B=\varnothing$, y luego $(A\setminus B)\setminus C=\varnothing$. Los lados son distintos.


## G. Diferencia simétrica

### 43
$A\setminus B=\{1,2\}$ y $B\setminus A=\{4\}$. Por tanto $A\triangle B=\{1,2,4\}$.

### 44
Un elemento pertenece a $A\triangle B$ exactamente cuando pertenece a uno de $A,B$ pero no a ambos. Esto equivale a pertenecer a $A\cup B$ y no pertenecer a $A\cap B$. Por definición, esa condición es pertenecer a $(A\cup B)\setminus(A\cap B)$.

### 45
Por definición, $A\triangle B=(A\setminus B)\cup(B\setminus A)$. Al intercambiar $A$ y $B$ obtenemos los mismos dos conjuntos unidos en orden inverso. Como la unión es conmutativa, $A\triangle B=B\triangle A$.

### 46
$A\triangle B=\varnothing$ exactamente cuando no existe ningún elemento que pertenezca a uno de los conjuntos sin pertenecer al otro. Eso significa $A\subseteq B$ y $B\subseteq A$. Por doble inclusión, equivale a $A=B$.


## H. Leyes y transformaciones

### 47
Por la ley de absorción, $A\cap(A\cup B)=A$. Elemento a elemento: si $x\in A$, entonces ciertamente $x\in A\cup B$; exigir ambas condiciones no añade nada a $x\in A$.

### 48
Por distributividad, $(A\cup B)\cap(A\cup B^c)=A\cup(B\cap B^c)=A\cup\varnothing=A$.

### 49
Factorizando $A$ mediante distributividad: $(A\cap B)\cup(A\cap B^c)=A\cap(B\cup B^c)=A\cap U=A$.

### 50
Para un elemento $x$, la pertenencia al lado izquierdo corresponde a $P\lor(Q\land R)$, donde $P:x\in A$, $Q:x\in B$, $R:x\in C$. La distributividad lógica da $(P\lor Q)\land(P\lor R)$, que corresponde a $x\in(A\cup B)\cap(A\cup C)$. Como la equivalencia vale para todo $x$, los conjuntos son iguales.

### 51
Usamos $B\setminus C=B\cap C^c$:
$A\cap(B\setminus C)=A\cap(B\cap C^c)=(A\cap B)\cap C^c=(A\cap B)\setminus C$.

### 52
Partimos de $(A\cup B)\setminus(A\cap B)$. Esto es $(A\cup B)\cap(A\cap B)^c$. Por De Morgan, $(A\cap B)^c=A^c\cup B^c$. Por tanto $A\triangle B=(A\cup B)\cap(A^c\cup B^c)$.

### 53


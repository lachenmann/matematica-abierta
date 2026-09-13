Por De Morgan, $(A\cup B)^c=A^c\cap B^c$. Entonces la expresión es $(A^c\cap B^c)\cup(A\cap B^c)$. Factorizando $B^c$: $B^c\cap(A^c\cup A)=B^c\cap U=B^c$.

### 54
Siempre $\mathcal P(A)\cup\mathcal P(B)\subseteq\mathcal P(A\cup B)$. Para la igualdad, supongamos primero $A\subseteq B$. Entonces $A\cup B=B$ y $\mathcal P(A)\subseteq\mathcal P(B)$, de modo que ambos lados son $\mathcal P(B)$. Lo mismo si $B\subseteq A$.

Recíprocamente, supongamos la igualdad y que ni $A\subseteq B$ ni $B\subseteq A$. Entonces existen $a\in A\setminus B$ y $b\in B\setminus A$. El conjunto $\{a,b\}$ es subconjunto de $A\cup B$, así que pertenece a $\mathcal P(A\cup B)$; pero no es subconjunto de $A$ ni de $B$, por lo que no pertenece a $\mathcal P(A)\cup\mathcal P(B)$, contradicción. Por tanto debe cumplirse $A\subseteq B$ o $B\subseteq A$.


## I. Demostraciones por elementos y doble inclusión

### 55
Primera inclusión: si $x\in A\setminus(B\cup C)$, entonces $x\in A$, $x\notin B$ y $x\notin C$. Por tanto $x\in A\setminus B$ y $x\in A\setminus C$, así que pertenece a la intersección.

Segunda inclusión: si $x\in(A\setminus B)\cap(A\setminus C)$, entonces $x\in A$, $x\notin B$ y $x\notin C$. Luego $x\notin B\cup C$, de modo que $x\in A\setminus(B\cup C)$.

### 56
Para cualquier $x$, $x\in(A\cap B)\setminus C$ equivale a $x\in A$, $x\in B$ y $x\notin C$. La misma condición equivale a $x\in A$ y $x\in B\setminus C$, es decir, $x\in A\cap(B\setminus C)$. Por extensionalidad, hay igualdad.

### 57
Si $x\in A\triangle B$, pertenece exactamente a uno de $A,B$; por ello está en $A\cup B$ y no en $A\cap B$, de modo que pertenece al lado derecho. Recíprocamente, si $x\in(A\cup B)\setminus(A\cap B)$, pertenece a por lo menos uno de $A,B$ pero no a ambos; entonces pertenece exactamente a uno, por lo que $x\in A\triangle B$.

### 58
Sea $x\in A\cap C^c$. Entonces $x\in A$ y $x\notin C$. Si $x\in B$, tendríamos $x\in A\cap B$, y la hipótesis implicaría $x\in C$, contradicción. Por tanto $x\notin B$, es decir, $x\in B^c$. Luego $A\cap C^c\subseteq B^c$.

### 59
Toma $A=\{1\}$, $B=\varnothing$ y $C=\{1\}$. El lado izquierdo es $\{1\}\cup\varnothing=\{1\}$. El lado derecho es $(\{1\}\cup\varnothing)\setminus\{1\}=\varnothing$. Por tanto la identidad es falsa.

### 60
Método algebraico: es exactamente la distributividad de $\cap$ respecto de $\cup$.

Método por pertenencia: $x\in A\cap(B\cup C)$ equivale a $x\in A$ y $(x\in B$ o $x\in C)$. Por distributividad lógica, esto equivale a $(x\in A$ y $x\in B)$ o $(x\in A$ y $x\in C)$, que equivale a $x\in(A\cap B)\cup(A\cap C)$.


## J. Producto cartesiano

### 61
$A\times B=\{(1,a),(1,b),(1,c),(2,a),(2,b),(2,c)\}$.

### 62
$B\times A=\{(a,1),(a,2),(b,1),(b,2),(c,1),(c,2)\}$. Los pares tienen las coordenadas en orden inverso. Por ejemplo $(1,a)\in A\times B$ pero $(1,a)\notin B\times A$.

### 63
Si existiera $(a,b)\in A\times\varnothing$, entonces $b\in\varnothing$, lo cual es imposible. Por tanto el producto no contiene pares y es el conjunto vacío.

### 64
Un par $(x,y)$ pertenece a $(A\cup B)\times C$ exactamente cuando $x\in A\cup B$ y $y\in C$, es decir, cuando $(x\in A$ o $x\in B)$ y $y\in C$. Esto equivale a $[(x\in A\land y\in C)\lor(x\in B\land y\in C)]$, que significa $(x,y)\in(A\times C)\cup(B\times C)$.

### 65
Si $A=\varnothing$ o $B=\varnothing$, ambos productos son vacíos y son iguales. Supongamos ahora $A$ y $B$ no vacíos y $A\times B=B\times A$. Elige $a_0\in A$ y $b_0\in B$. Para cualquier $a\in A$, $(a,b_0)\in A\times B=B\times A$, luego $a\in B$. Así $A\subseteq B$. Simétricamente $B\subseteq A$, por lo que $A=B$. Recíprocamente, si $A=B$, los productos son iguales. Por tanto la igualdad ocurre exactamente cuando $A=B$ o al menos uno de los conjuntos es vacío.

### 66
Hay $4$ opciones para la primera coordenada y, para cada una, $7$ opciones para la segunda. Por tanto $|A\times B|=4\cdot7=28$.


## K. Diagnóstico y transferencia

### 67
El error es confundir pertenencia con inclusión. Si $1$ es un número, la afirmación correcta es $1\in A$. Si se quiere hablar de inclusión, puede escribirse $\{1\}\subseteq A$, que sí se sigue de $1\in A$.

### 68
Falta especificar el universo. Si el universo es $\mathbb Z$, el complemento son los enteros distintos de $1,2$; si es $\{1,2,3\}$, el complemento es $\{3\}$. Sin universo, $A^c$ no queda determinado.

### 69
Falta demostrar $B\subseteq A$. Por ejemplo $A=\{1\}$ y $B=\{1,2\}$ satisfacen $A\subseteq B$ pero no son iguales. La igualdad requiere doble inclusión.

### 70
El diagrama representa regiones y puede hacer visible la coincidencia para una configuración gráfica. La prueba por pertenencia parte de un elemento arbitrario y usa sólo definiciones y lógica: $x\notin A\cup B$ equivale a $x\notin A$ y $x\notin B$. Esa equivalencia establece la identidad sin depender de una figura particular y hace explícita la razón lógica.

### 71
Es falsa. Toma $C=\{1,2\}$, $A=\{1\}$ y $B=\{2\}$. Entonces $A\cup C=C=B\cup C$, pero $A\ne B$. La unión puede ocultar diferencias entre $A$ y $B$ porque los elementos discrepantes ya están contenidos en $C$; no existe una ley general de cancelación para $\cup$.

### 72
Respuesta modelo: Para estudiar una expresión de conjuntos podemos fijar un elemento arbitrario $x$ y traducir cada afirmación de pertenencia a una proposición. La condición $x\in A\cup B$ corresponde a $(x\in A)\lor(x\in B)$; la intersección corresponde a conjunción y el complemento a negación respecto de un universo. La inclusión $A\subseteq B$ expresa que para todo $x$, $x\in A$ implica $x\in B$. La extensionalidad dice que $A=B$ cuando para todo $x$ son equivalentes las proposiciones $x\in A$ y $x\in B$. Por eso conmutatividad, distributividad, absorción y De Morgan reaparecen en el álgebra de conjuntos: son las mismas formas lógicas aplicadas a predicados de pertenencia. Los conjuntos no son proposiciones, pero su pertenencia está gobernada por la misma estructura lógica.

## L. Problemas tipo prueba

### 73

Sea $X$ un conjunto. Entonces

$$
\begin{aligned}
X\in\mathcal P(A)\cap\mathcal P(B)
&\Longleftrightarrow X\subseteq A\land X\subseteq B\\
&\Longleftrightarrow X\subseteq A\cap B\\
&\Longleftrightarrow X\in\mathcal P(A\cap B).
\end{aligned}
$$

Por extensionalidad,

$$
\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B).
$$

Si $A\subseteq B$ y $X\in\mathcal P(A)$, entonces $X\subseteq A\subseteq B$, de modo que $X\in\mathcal P(B)$. Así $\mathcal P(A)\subseteq\mathcal P(B)$.

Recíprocamente, si $\mathcal P(A)\subseteq\mathcal P(B)$, entonces $A\in\mathcal P(A)$, por lo que $A\in\mathcal P(B)$. Esto significa $A\subseteq B$.

### 74

Si $A\subseteq B$, entonces $\mathcal P(A)\subseteq\mathcal P(B)$ y $A\cup B=B$. Por tanto

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(B)=\mathcal P(A\cup B).
$$

El caso $B\subseteq A$ es simétrico.

Para la recíproca, supongamos

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B)
$$

y que ninguna inclusión vale. Entonces existen

$$
a\in A\setminus B,\qquad b\in B\setminus A.
$$

Como $\{a,b\}\subseteq A\cup B$, tenemos $\{a,b\}\in\mathcal P(A\cup B)$. Pero $\{a,b\}\not\subseteq A$ porque $b\notin A$, y $\{a,b\}\not\subseteq B$ porque $a\notin B$. Por tanto $\{a,b\}$ no pertenece a $\mathcal P(A)\cup\mathcal P(B)$, contradicción.

Luego la igualdad vale exactamente cuando $A\subseteq B$ o $B\subseteq A$.

### 75

La condición $x\in A\triangle B$ significa que $x$ pertenece a exactamente uno de $A$ y $B$.

Por tanto $x\in(A\triangle B)\triangle C$ si y sólo si:

- $x$ pertenece a exactamente uno de $A,B$ y no pertenece a $C$, o
- $x$ pertenece a $C$ y no pertenece a exactamente uno de $A,B$.

Eso ocurre exactamente cuando $x$ pertenece a uno o a tres de los conjuntos $A,B,C$, es decir, a un número impar de ellos.

El mismo criterio describe $x\in A\triangle(B\triangle C)$. Luego, para todo $x$,

$$
x\in(A\triangle B)\triangle C
\Longleftrightarrow
x\in A\triangle(B\triangle C),
$$

y por extensionalidad la diferencia simétrica es asociativa.

### 76

Si $X\cap A=B$, entonces necesariamente $B\subseteq A$.

Recíprocamente, si $B\subseteq A$, existe solución; por ejemplo $X=B$, pues $B\cap A=B$.

Bajo la condición $B\subseteq A$, todas las soluciones son

$$
X=B\cup C,\qquad C\subseteq A^c.
$$

En efecto,

$$
(B\cup C)\cap A=(B\cap A)\cup(C\cap A)=B.
$$

Para demostrar que no falta ninguna, sea $X$ una solución cualquiera. Entonces

$$
X=(X\cap A)\cup(X\cap A^c)=B\cup(X\cap A^c).
$$

Tomando $C=X\cap A^c$ obtenemos exactamente la forma descrita.

### 77

Si $X\cup A=B$, entonces $A\subseteq B$. Esta condición también es suficiente: si $A\subseteq B$, tomar $X=B$ produce una solución.

Supongamos ahora $A\subseteq B$. De $X\cup A=B$ se deduce $X\subseteq B$. Además, todo elemento de $B\setminus A$ debe pertenecer a $X$, porque no puede venir de $A$. Por tanto

$$
B\setminus A\subseteq X\subseteq B.
$$

Estas inclusiones también son suficientes: si se cumplen, entonces $X\cup A\subseteq B$; y si $b\in B$, o $b\in A$, o $b\in B\setminus A\subseteq X$, así que $B\subseteq X\cup A$.

Equivalentemente, todas las soluciones son

$$
X=(B\setminus A)\cup C,\qquad C\subseteq A.
$$

### 78

Si $A=\varnothing$ o $B=\varnothing$, entonces $A\times B=\varnothing$, de modo que la inclusión en $C\times D$ es automática.

Supongamos ahora $A\ne\varnothing$, $B\ne\varnothing$ y

$$
A\times B\subseteq C\times D.
$$

Elige $b_0\in B$. Para cualquier $a\in A$, $(a,b_0)\in A\times B$, luego $(a,b_0)\in C\times D$. Por tanto $a\in C$, y así $A\subseteq C$.

Elige ahora $a_0\in A$. Para cualquier $b\in B$, $(a_0,b)\in A\times B\subseteq C\times D$, de donde $b\in D$. Luego $B\subseteq D$.

Recíprocamente, si $A\subseteq C$ y $B\subseteq D$, todo par de $A\times B$ pertenece a $C\times D$.

La no vacuidad es esencial: si $B=\varnothing$, entonces $A\times B=\varnothing$ cualquiera sea $A$, por lo que la inclusión del producto no permite concluir nada sobre $A\subseteq C$.

### 79

Sea $x$ arbitrario.

Si $x\in C$, entonces

$$
x\in A
\Longleftrightarrow
x\in A\cap C
\Longleftrightarrow
x\in B\cap C
\Longleftrightarrow
x\in B.
$$

Si $x\notin C$, la igualdad $A\cup C=B\cup C$ da

$$
x\in A
\Longleftrightarrow
x\in A\cup C
\Longleftrightarrow
x\in B\cup C
\Longleftrightarrow
x\in B.
$$

Luego $A=B$ por extensionalidad.

Cada hipótesis por separado es insuficiente:

- toma $A=\{1\}$, $B=\{2\}$ y $C=\{1,2\}$. Entonces $A\cup C=B\cup C$, pero $A\ne B$;
- toma $A=\{1\}$, $B=\{2\}$ y $C=\varnothing$. Entonces $A\cap C=B\cap C$, pero $A\ne B$.

### 80

Basta establecer una cadena cíclica entre las primeras cuatro condiciones y conectar una de ellas con la quinta.

**$(1)\Rightarrow(2)$.** Si $A\subseteq B$, entonces los elementos comunes a $A$ y $B$ son exactamente los de $A$, de modo que $A\cap B=A$.

**$(2)\Rightarrow(3)$.** Si $A\cap B=A$, entonces $A\subseteq B$. Por tanto $A\cup B=B$.

**$(3)\Rightarrow(4)$.** Si $A\cup B=B$, todo elemento de $A$ pertenece a $B$, así que $A\setminus B=\varnothing$.

**$(4)\Rightarrow(1)$.** Si $A\setminus B=\varnothing$ y $x\in A$, entonces $x\notin B$ produciría $x\in A\setminus B$, contradicción. Luego $x\in B$, y por tanto $A\subseteq B$.

Finalmente, por el ejercicio 73,

$$
A\subseteq B
\Longleftrightarrow
\mathcal P(A)\subseteq\mathcal P(B).
$$

Así las cinco condiciones son equivalentes.


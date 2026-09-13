**Solución 13.** Es verdadera. No basta una lista de ejemplos; usamos el hecho general de que el cuadrado de todo real, y por tanto de todo entero, es no negativo. La justificación debe cubrir simultáneamente todos los enteros.

**Solución 14.** Toma $n=0$. Entonces $0^2>0$ es $0>0$, falso. Por tanto el universal queda refutado. También $n=1$ funciona como contraejemplo.

**Solución 15.** Basta un par de enteros impares cuya suma sea par. Por ejemplo, $1$ y $3$ son impares y $1+3=4$ es par. En realidad la afirmación correcta es la contraria: la suma de dos impares es par.

**Solución 16.** Comprobar finitos casos no demuestra una afirmación universal sobre todos los enteros no negativos. En $n=16$ se obtiene $16^2+16+17=289=17^2$, que no es primo. Éste es un contraejemplo decisivo.

**Solución 17.** No. La forma lógica es $\forall n\,[E(n)\Rightarrow E(n^2)]$. Para un entero impar, el antecedente $E(n)$ es falso; por tanto la implicación no falla allí. Un contraejemplo tendría que ser un entero par cuyo cuadrado fuera impar.

**Solución 18.** Toma $x=-2$. Se cumple $x^2=4>1$, pero $x=-2$ no es mayor que $1$. Por tanto el antecedente es verdadero y el consecuente falso: exactamente la forma necesaria para refutar una implicación universal.

### Soluciones — D — Existenciales y testigos

**Solución 19.** El entero $n=7$ sirve: $7^2=49$. Con un solo testigo válido queda demostrada la existencia. También $-7$ es testigo, lo que muestra que la afirmación no contiene unicidad.

**Solución 20.** Sería necesario $n=7/2$, pero $7/2$ no es entero. Por tanto ningún $n\in\mathbb Z$ satisface la ecuación y la afirmación es falsa.

**Solución 21.** Toma $x=1/2$. Entonces $0<1/2<1$ y $(1/2)^2=1/4<1/2$. Por tanto $x=1/2$ satisface simultáneamente todas las condiciones.

**Solución 22.** Elige $a=4$ y $b=1$. Entonces $a^2-b^2=16-1=15$. El par $(4,1)$ es un testigo para la existencia conjunta de $a$ y $b$.

**Solución 23.** Por ejemplo $n=1001$ es un testigo. No se necesita encontrar el “mejor” ni el menor testigo salvo que el enunciado lo exija; cualquier elemento del dominio que satisfaga el predicado basta para la existencia.

**Solución 24.** El cuantificador $\exists$ significa “existe al menos uno”, no “existe exactamente uno”. Tener dos testigos refuerza la existencia; no la contradice. La unicidad requeriría $\exists!x\,P(x)$.

### Soluciones — E — Negación de cuantificadores

**Solución 25.** La negación es $\exists x\in\mathbb R\;(x^2<0)$. Cambiamos $\forall$ por $\exists$ y negamos $x^2\ge0$, cuya negación sobre los reales es $x^2<0$.

**Solución 26.** La negación es $\forall n\in\mathbb Z\;(n^2\ne2)$. Cambiamos $\exists$ por $\forall$ y negamos la igualdad.

**Solución 27.** Primero: $\neg\forall n\,A(n)\equiv\exists n\,\neg A(n)$. Luego $\neg(E(n)\Rightarrow E(n^2))\equiv E(n)\land\neg E(n^2)$. La negación completa es $\exists n\in\mathbb Z\;[E(n)\land\neg E(n^2)]$.

**Solución 28.** La negación es $\forall x\in\mathbb R\;\neg(x>0\land x^2<1)$. Por De Morgan, queda $\forall x\in\mathbb R\;(x\le0\lor x^2\ge1)$.

**Solución 29.** Negamos desde afuera: $\exists x\in\mathbb R\;\neg\exists y\in\mathbb R\;(y>x)$. Luego cambia $\exists y$ por $\forall y$: $\exists x\in\mathbb R\;\forall y\in\mathbb R\;\neg(y>x)$. Por tanto, $\exists x\in\mathbb R\;\forall y\in\mathbb R\;(y\le x)$.

**Solución 30.** La negación es $\forall y\in\mathbb R\;\exists x\in\mathbb R\;\neg(y>x)$, es decir, $\forall y\in\mathbb R\;\exists x\in\mathbb R\;(y\le x)$.

**Solución 31.** “No todos” niega un universal: $\neg\forall n\in\mathbb Z\;(n>0)$. En forma positiva equivalente: $\exists n\in\mathbb Z\;(n\le0)$. Por ejemplo $0$ es un testigo.

**Solución 32.** Toma dominio $D=\{1,2\}$ y $P(x)$ = “$x=1$”. Entonces $\neg\forall x\,P(x)$ es verdadera porque no todos los elementos son $1$; concretamente $2$ falla. Pero $\forall x\,\neg P(x)$ es falsa porque $P(1)$ es verdadera. La primera dice “al menos uno falla”; la segunda, “todos fallan”.

### Soluciones — F — Cuantificación restringida

**Solución 33.** La forma conceptual es $\forall n\in D\;[n\in\mathbb Z\Rightarrow P(n)]$. Los elementos de $D$ que no son enteros no deben actuar como contraejemplos; por eso aparece una implicación.

**Solución 34.** La forma es $\exists n\in D\;[n\in\mathbb Z\land n^2=9]$. Un testigo debe cumplir a la vez pertenecer a $\mathbb Z$ y satisfacer la ecuación.

**Solución 35.** La negación es $\exists x\in A\;\neg P(x)$. En palabras: existe al menos un elemento de $A$ que no satisface $P$.

**Solución 36.** La negación es $\forall x\in A\;\neg P(x)$. En palabras: ningún elemento de $A$ satisface $P$.

**Solución 37.** La conjunción exige que **todo elemento del dominio mayor** sea simultáneamente entero y racional, lo cual es mucho más fuerte. La forma correcta es $\forall x\,[x\in\mathbb Z\Rightarrow x\in\mathbb Q]$: sólo los elementos que son enteros activan la condición.

**Solución 38.** En un existencial restringido necesitamos que el testigo sea entero **y** negativo. La implicación puede ser verdadera para un objeto no entero sin demostrar lo deseado. La forma correcta es $\exists x\,[x\in\mathbb Z\land x<0]$.

### Soluciones — G — Alcance y paréntesis

**Solución 39.** Las dos apariciones de $x$, en $P(x)$ y $Q(x)$, están dentro del alcance del cuantificador y por tanto ligadas. $R$ no contiene $x$.

**Solución 40.** Dentro de $P(x,y)$, $x$ está ligada por $\forall x$ y $y$ permanece libre. En $Q(y)$, $y$ también es libre. Por tanto la fórmula completa tiene a $y$ como variable libre.

**Solución 41.** En la primera, todas las apariciones de $x$ están ligadas y la fórmula puede ser cerrada. En la segunda, la $x$ de $Q(x)$ queda fuera del alcance del cuantificador, así que la expresión sigue abierta respecto de $x$. Cambiar los paréntesis cambia el alcance y, por tanto, la estructura lógica.

**Solución 42.** Podemos escribir, por ejemplo, $\exists t\,[t>y\land P(t)]$. El cuantificador y todas las apariciones ligadas de $x$ se sustituyen coherentemente por $t$; $y$ permanece libre.

**Solución 43.** La $y$ original era libre: podía representar un parámetro fijado externamente. Al renombrar $x$ como $y$, el cuantificador $\forall y$ pasa a ligar ambas posiciones. Esa variable libre queda capturada. La transformación no es una mera renominación, sino un cambio de estructura.

**Solución 44.** La primera afirma que cada $x$ satisface simultáneamente $P$ y $Q$. La segunda afirma que todos satisfacen $P$, pero deja $Q(x)$ como condición abierta sobre una $x$ libre. No son expresiones equivalentes ni tienen el mismo estatus lógico.

### Soluciones — H — Orden de cuantificadores

**Solución 45.** (a) Verdadera: dado $x$, elige $y=x+1$. (b) Falsa: si se propone un real fijo $y$, tomando $x=y+1$ obtenemos $y>x$ falso. El cambio de orden altera la dependencia permitida.

**Solución 46.** La primera es verdadera: para cada $x$, elige $y=x+1$. La segunda es falsa: un mismo $y$ no puede ser simultáneamente $x+1$ para todos los reales $x$; por ejemplo exigiría $y=1$ cuando $x=0$ y $y=2$ cuando $x=1$.

**Solución 47.** $\forall n\exists m\;(m=n+2)$ es verdadera: para cada $n$, toma $m=n+2$. $\exists m\forall n\;(m=n+2)$ es falsa: un entero fijo $m$ no puede valer $n+2$ para todos los enteros $n$.

**Solución 48.** Ambas son verdaderas. En (a), el testigo fijo $n=0$ funciona para todo $m$. En (b), para cada $m$ podemos elegir $n=0$; de hecho la elección no necesita depender de $m$. Que ambas sean verdaderas no significa que las formas lógicas sean equivalentes en general.

**Solución 49.** Sobre todo $\mathbb R$ es falsa: para $x=0$ no existe $y$ con $0\cdot y=1$. Si restringimos $x$ a $\mathbb R\setminus\{0\}$, es verdadera: dado $x\ne0$, elige $y=1/x$.

**Solución 50.** (a) Verdadera con $y=1$, pues $1\cdot x=x$ para todo real $x$. (b) También verdadera; incluso puede usarse el mismo $y=1$ para cada $x$. Este ejemplo recuerda que invertir cuantificadores puede cambiar el significado aunque ocasionalmente ambas afirmaciones resulten verdaderas.

**Solución 51.** Dos universales exigen que $P$ sea verdadera para todos los pares $(x,y)$; el orden en que recorremos los componentes no cambia esa exigencia. Dos existenciales sólo piden que exista algún par $(x,y)$ y el orden tampoco cambia eso. En cambio, $\forall x\exists y$ permite que $y$ dependa de $x$, mientras $\exists y\forall x$ exige un único $y$ fijo; por eso no son equivalentes en general.

**Solución 52.** $\forall x\exists y\,R(x,y)$ es verdadera: para $x=1$ elige $y=1$, y para $x=2$ elige $y=2$. En cambio, $\exists y\forall x\,R(x,y)$ es falsa: ningún único $y$ es igual simultáneamente a $1$ y a $2$.

### Soluciones — I — Dependencia y elección de testigos


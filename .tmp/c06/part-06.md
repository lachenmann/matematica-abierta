**Solución 53.** La elección $y=2x$ funciona. El testigo no es un número fijo: depende del valor de $x$ que haya sido dado. Esa dependencia es permitida porque $\exists y$ aparece después de $\forall x$.

**Solución 54.** Si fijamos cualquier real $y$, podemos tomar $x=y+1$ y entonces $y>x$ falla. La afirmación sigue siendo verdadera porque permite elegir un $y$ nuevo después de conocer cada $x$, por ejemplo $y=x+1$.

**Solución 55.** Para cada entero $n$ podemos elegir el testigo $m=n^2$. En general cambia cuando cambia $n$. La afirmación no promete un único entero $m$ que sea igual al cuadrado de todos los enteros.

**Solución 56.** El testigo es $m=0$. Como $\exists m$ aparece primero, debemos elegir un solo entero antes de considerar los distintos $n$. Ese mismo $m=0$ funciona para todos porque $0+n=n$.

**Solución 57.** No. El cuantificador existencial sólo garantiza al menos un testigo. Puede haber varios. Por ejemplo, sobre $\mathbb R$, si $R(x,y)$ significa $y>x$, para cada $x$ hay infinitos valores de $y$ posibles. La unicidad requeriría una condición adicional.

**Solución 58.** (a) $\forall p\exists q\,M(p,q)$. El testigo $q$ puede depender de $p$. (b) $\exists q\forall p\,M(p,q)$. Aquí se exige una sola persona $q$ que satisfaga la relación con todas las personas. Las frases no tienen la misma estructura.

### Soluciones — J — Existencia única

**Solución 59.** Existe: $x=2$ satisface $2+3=5$. Es único porque si $x+3=5$, restando $3$ en ambos lados se obtiene necesariamente $x=2$. Por tanto la afirmación es verdadera.

**Solución 60.** Existe el entero $n=3$. Si $2n=6$, dividir por $2$ obliga a $n=3$, así que no hay otro entero posible. La afirmación es verdadera.

**Solución 61.** Es falsa. Hay existencia, pues $x=2$ funciona, pero también $x=-2$. Como hay dos testigos distintos, falla la unicidad.

**Solución 62.** Una expansión estándar es $\exists x\,[P(x)\land\forall y\,(P(y)\Rightarrow y=x)]$. La primera parte afirma existencia; la segunda fuerza que cualquier otro candidato que cumpla $P$ coincida con el testigo $x$.

### Soluciones — K — Traducción bidireccional

**Solución 63.** $\forall n\in\mathbb Z\;\exists m\in\mathbb Z\;(m>n)$. El orden es universal-existencial porque el entero mayor puede depender del entero inicial.

**Solución 64.** Una forma es $\forall n\in\mathbb Z\;\neg\exists m\in\mathbb Z\;(n<m<n+1)$. Equivalentemente, $\forall n\in\mathbb Z\;\forall m\in\mathbb Z\;\neg(n<m<n+1)$.

**Solución 65.** $\exists x\in\mathbb R\;(x>0\land x^2<x)$. También podría escribirse $\exists x\in\mathbb R\;(0<x<1)$ si ya se ha justificado la equivalencia pertinente para positivos, pero la traducción directa conserva exactamente el enunciado dado.

**Solución 66.** $\neg\forall x\in\mathbb R\;(x>0)$, equivalente a $\exists x\in\mathbb R\;(x\le0)$.

**Solución 67.** “Para todo entero $n$, si $n$ es impar, entonces $n^2$ es impar.” También puede decirse: “el cuadrado de todo entero impar es impar”.

**Solución 68.** “Existe un entero $m$ tal que, para todo entero $n$, se cumple $m+n=n$.” La estructura exige un mismo $m$ para todos los $n$; concretamente ese entero es $0$.

### Soluciones — L — Diagnóstico y síntesis

**Solución 69.** El primer error es conservar el cuantificador universal. Al negar un universal debe aparecer un existencial. La forma correcta es $\exists x\in\mathbb R\;(x^2<0)$. Luego observamos que esta negación es falsa, coherente con la verdad del enunciado original.

**Solución 70.** La traducción propuesta dice que existe **un mismo libro** $b$ elegido por todos los estudiantes. La frase original permite que cada estudiante haya elegido un libro distinto. La forma adecuada es $\forall e\exists b\,E(e,b)$.

**Solución 71.** (a) Verdadera: dado $x$, toma $y=-x$. (b) Falsa: un único $y$ no puede satisfacer $x+y=0$ para todos los reales $x$; por ejemplo, $x=0$ exige $y=0$ y $x=1$ exige $y=-1$. (c) Falsa: basta $x=y=1$, pues $1+1\ne0$. (d) Verdadera: por ejemplo $x=0,y=0$. La negación de (a) es $\exists x\forall y\;(x+y\ne0)$, que es falsa porque para cualquier $x$ siempre podemos elegir $y=-x$.

**Solución 72.** (a) $\forall x\in\mathbb R\;\exists!y\in\mathbb R\;(2y+x=0)$. (b) Es verdadera: dado $x$, la ecuación obliga a $y=-x/2$, que es real. (c) El testigo depende de $x$ mediante la regla $y=-x/2$; no hay un único $y$ global para todos los $x$. (d) Expandiendo unicidad, el original dice que para todo $x$ existe un $y$ con $2y+x=0$ y cualquier $z$ que también satisfaga $2z+x=0$ debe ser igual a $y$. Su negación puede expresarse conceptualmente como: $\exists x\in\mathbb R$ tal que **o bien** no existe ningún $y$ con $2y+x=0$, **o bien** existen dos reales distintos $y,z$ que satisfacen ambos la ecuación. Simbólicamente:

$$
\exists x\in\mathbb R\;\Big([\forall y\in\mathbb R\;(2y+x\ne0)]\lor[\exists y,z\in\mathbb R\;(y\ne z\land 2y+x=0\land 2z+x=0)]\Big).
$$

En este caso la negación es falsa porque para cada $x$ existe exactamente el único valor $-x/2$.

***

### Soluciones — M — Problemas tipo prueba

**Solución 73.**

(a) Es verdadera. Dado $x\ne0$, basta elegir $y=1/x$. Entonces $xy=1$. El testigo depende de $x$.

(b) Es falsa. Si existiera un real fijo $y$ tal que $xy=1$ para todo $x\ne0$, al tomar $x=1$ obtendríamos $y=1$, mientras que con $x=2$ obtendríamos $y=1/2$. Contradicción.

(c) Es verdadera. Para cada $x$ podemos tomar $y=x+1$, y entonces $y>x$.

(d) Es falsa. Si existiera un real $y$ mayor que todo real $x$, tomando $x=y+1$ tendríamos $y>y+1$, contradicción.

En (a) y (c), el existencial está dentro del alcance del universal: el testigo puede variar con la entrada. En (b) y (d), el testigo debe fijarse antes y funcionar para todos los valores universales.

**Solución 74.**

(a) Dice: “Todo real no negativo posee una raíz cuadrada real no negativa”.

(b)

$$
\begin{aligned}
&\neg\forall x\in\mathbb R\;\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\neg\Big[x\ge0\Rightarrow\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\neg\exists y\in\mathbb R\;(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\forall y\in\mathbb R\;\neg(y\ge0\land y^2=x)\Big]\\
&\equiv \exists x\in\mathbb R\;\Big[x\ge0\land\forall y\in\mathbb R\;(y<0\lor y^2\ne x)\Big].
\end{aligned}
$$

(c) La afirmación original es verdadera: si $x\ge0$, existe $y=\sqrt{x}\ge0$ y $y^2=x$. Por tanto su negación es falsa.

(d) Cambiar sólo $\forall$ por $\exists$ niega únicamente la capa externa. También deben negarse la implicación y el existencial interior.

**Solución 75.**

(a)

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;
\Big[(3y-2=x)\land
\forall z\in\mathbb R\,(3z-2=x\Rightarrow z=y)\Big].
$$

(b) Fijado $x$, la ecuación obliga a $y=(x+2)/3$, que es real. Si $z$ también satisface $3z-2=x$, entonces $3z-2=3y-2$, de donde $z=y$. Hay existencia y unicidad.

(c) La negación expresa que existe algún $x$ para el cual o no hay solución o hay dos soluciones distintas:

$$
\exists x\in\mathbb R\;
\Big(
[\forall y\in\mathbb R\;(3y-2\ne x)]
\lor
[\exists y,z\in\mathbb R\;(y\ne z\land 3y-2=x\land 3z-2=x)]
\Big).
$$

(d) $\exists!y\,\forall x\,(3y-2=x)$ es falsa: fijado $y$, $3y-2$ es un solo real y no puede coincidir con todos los reales $x$.

**Solución 76.**

(a) $A$ es verdadera. Dado $m$, elige $n=m+1$. Si $k\ge n$, entonces $k\ge m+1>m$.

(b) $B$ es falsa. Para cualquier candidato fijo $n$, toma $m=n$ y $k=n$. Entonces $k\ge n$ es verdadera, pero $k>m$ se convierte en $n>n$, falsa.

(c)

$$
\begin{aligned}
\neg A
&\equiv \exists m\;\forall n\;\exists k\;\neg(k\ge n\Rightarrow k>m)\\
&\equiv \exists m\;\forall n\;\exists k\;(k\ge n\land k\le m).
\end{aligned}
$$

(d) En $A$, $n$ puede depender de $m$. En $B$, $n$ debe elegirse una sola vez y funcionar para todos los $m$.

**Solución 77.**

(a) Es verdadera en $\mathbb R$: dado $x$, elige $y=\sqrt{x^2+1}$.

(b) Es falsa en $\mathbb Z$. Para $x=1$ se exigiría $y^2=2$, imposible para un entero.

(c)

$$
\exists x\in\mathbb Z\;\forall y\in\mathbb Z\;(y^2\ne x^2+1).
$$

El valor $x=1$ es un testigo.

(d) Los cuantificadores recorren objetos distintos según el dominio. El mismo patrón formal puede ser verdadero en $\mathbb R$ y falso en $\mathbb Z$ porque cambian los testigos permitidos.

**Solución 78.**

(a)

$$
\forall e\in E\;\exists p\in P\;
\Big[
S(e,p)\land
\forall e'\in E\;(e'\ne e\Rightarrow\neg S(e',p))
\Big].
$$

(b)

$$
\begin{aligned}
&\neg\forall e\in E\;\exists p\in P\;
\Big[S(e,p)\land\forall e'\in E\;(e'\ne e\Rightarrow\neg S(e',p))\Big]\\
&\equiv
\exists e\in E\;\forall p\in P\;
\Big[\neg S(e,p)\lor
\exists e'\in E\;(e'\ne e\land S(e',p))\Big].
\end{aligned}
$$


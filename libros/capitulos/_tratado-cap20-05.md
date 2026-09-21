## 20.5. Monotonía y signo de la derivada {#sec-ta-20-5}

El teorema de Lagrange transforma la información local de una derivada en una comparación entre dos valores de una función. Para aprovecharlo correctamente, distinguiremos las desigualdades estrictas de las no estrictas y conservaremos la condición de que el segmento entre los argumentos esté dentro del dominio. La derivada no necesita existir en los extremos de ese segmento.

### Definición 20.5.1 — Monotonía estricta y no estricta sobre un dominio ordenado
Sean $D\subseteq\mathbb R$ y $f:D\to\mathbb R$. Para todo par de argumentos $u,v\in D$ con $u<v$ definimos las siguientes propiedades:

- $f$ es **no decreciente** en $D$ si $f(u)\le f(v)$ para todos esos pares.
- $f$ es **no creciente** en $D$ si $f(u)\ge f(v)$ para todos esos pares.
- $f$ es **estrictamente creciente** en $D$ si $f(u)<f(v)$ para todos esos pares.
- $f$ es **estrictamente decreciente** en $D$ si $f(u)>f(v)$ para todos esos pares.

Llamaremos *monótona* a una función no decreciente o no creciente, y *estrictamente monótona* a una estrictamente creciente o estrictamente decreciente. En lo sucesivo no emplearemos «creciente» o «decreciente» a secas cuando su sentido estricto o amplio pueda causar ambigüedad.

La definición sólo compara argumentos que pertenecen a $D$: tiene sentido incluso si $D$ no es un intervalo. Una función constante es simultáneamente no decreciente y no creciente; en un dominio con dos puntos distintos no es estrictamente monótona. Ninguna de estas propiedades presupone continuidad ni derivabilidad, y no se introduce una nueva función «derivada global».

### Teorema 20.5.2 — Criterios suficientes de monotonía por el signo de la derivada
Sean $a,b\in\mathbb R$ con $a<b$, $I:=[a,b]$ y $f:I\to\mathbb R$. Supongamos que $f$ es continua en todos los puntos de $I$ y derivable en cada punto de $(a,b)$, en ambos casos **relativamente al dominio $I$**. Entonces se verifican las cuatro implicaciones siguientes:

$$
\begin{array}{rcl}
\bigl[\forall x\in(a,b),\ f'(x)\ge0\bigr]&\Longrightarrow&f\text{ es no decreciente en }I;\\
\bigl[\forall x\in(a,b),\ f'(x)\le0\bigr]&\Longrightarrow&f\text{ es no creciente en }I;\\
\bigl[\forall x\in(a,b),\ f'(x)>0\bigr]&\Longrightarrow&f\text{ es estrictamente creciente en }I;\\
\bigl[\forall x\in(a,b),\ f'(x)<0\bigr]&\Longrightarrow&f\text{ es estrictamente decreciente en }I.
\end{array}
\tag{20.5.1}
$$

La cuantificación sobre el signo se refiere al intervalo abierto completo: conocer el signo de la derivada en un solo punto no permite concluir monotonía en $I$. No se supone derivabilidad en $a$ ni en $b$.

**Demostración.**
Fijemos **arbitrariamente** $u,v\in I$ con $u<v$. Puesto que $I=[a,b]$, se tiene $[u,v]\subseteq I$ y $(u,v)\subseteq(a,b)$. La continuidad de $f$ en cada punto de $[u,v]$ relativa a $I$, y la derivabilidad de $f$ en cada punto de $(u,v)$ también relativa a $I$, son restricciones de las hipótesis generales. Aplicamos, por tanto, el corolario de Lagrange sobre el **dominio original** Corolario §20.3.3 — Valor medio en un subintervalo del dominio original: existe $c\in(u,v)$ tal que

$$
f(v)-f(u)=f'(c)(v-u).
\tag{20.5.2}
$$

Como $u<v$, el factor $v-u$ es **estrictamente positivo**. Si $f'(x)\ge0$ para todo $x\in(a,b)$, entonces $f'(c)\ge0$ y (20.5.2) implica $f(v)-f(u)\ge0$, es decir, $f(u)\le f(v)$. Si todas las derivadas interiores son no positivas, el mismo producto es no positivo y $f(u)\ge f(v)$. Si son estrictamente positivas, el producto de dos reales positivos es positivo y $f(u)<f(v)$; si son estrictamente negativas, es negativo y $f(u)>f(v)$.

El par $u<v$ fue arbitrario, así que cada conclusión rige para **todos** los pares ordenados del intervalo. Para cada par se aplica Lagrange una sola vez: el razonamiento por instanciación existencial no define ni necesita una función que elija simultáneamente un punto $c$ para cada par. No se invocan Darboux ni Taylor. $\square$

**Por qué importa el intervalo.** Consideremos $D:=(-1,0)\cup(0,1)$ y $F:D\to\mathbb R$, dada por $F(x)=x$ si $x<0$ y $F(x)=x-1$ si $x>0$. En cada punto de $D$, una bola suficientemente pequeña queda en una sola componente; allí $F$ es afín de pendiente $1$, por lo que $F'(x)=1$. Sin embargo $-\tfrac14<\tfrac14$ y $F(-\tfrac14)=-\tfrac14>-\tfrac34=F(\tfrac14)$: $F$ no es no decreciente en $D$. El segmento que une esos argumentos atraviesa el punto excluido $0$; por eso no podemos aplicar Lagrange al par. Tener derivada positiva en todas las componentes no basta para compararlas sin una hipótesis adicional.

### Proposición 20.5.3 — Signos necesarios de la derivada para la monotonía
Sean $a<b$ y $f:[a,b]\to\mathbb R$. Si $f$ es no decreciente en $[a,b]$ y es derivable en un punto $c\in(a,b)$, entonces $f'(c)\ge0$. Si $f$ es no creciente y derivable en ese punto, entonces $f'(c)\le0$. Estas conclusiones también se aplican, respectivamente, a las funciones estrictamente crecientes y estrictamente decrecientes. **No** se concluye $f'(c)>0$ a partir de crecimiento estricto, ni $f'(c)<0$ a partir de decrecimiento estricto.

**Demostración.**
Pongamos $I=[a,b]$ y fijemos el punto interior $c$ donde la derivada existe. Por Corolario §19.8.5 — Extremos e interior de un intervalo cerrado no degenerado, $c\in\operatorname{Acc}(I)$ y el cociente incremental $q_{f,c}:I\setminus\{c\}\to\mathbb R$ de Definición §19.1.1 — Cociente incremental en un punto está bien tipado. Supongamos primero que $f$ es no decreciente. Para cada $x\in I$ con $x\ne c$:

- si $x>c$, tanto $f(x)-f(c)$ como $x-c$ son no negativos y el denominador es positivo;
- si $x<c$, el numerador y el denominador son no positivos y el segundo es estrictamente negativo.

En los dos casos,

$$
q_{f,c}(x)=\frac{f(x)-f(c)}{x-c}\ge0.
\tag{20.5.3}
$$

Supongamos por contradicción que el límite existente $L:=f'(c)$ fuese negativo. Por la definición cuantificada de derivada, con $\varepsilon:=-L/2>0$, existe $\delta>0$ tal que $x\in I$ y $0<|x-c|<\delta$ implican $|q_{f,c}(x)-L|<\varepsilon$. En particular,

$$
q_{f,c}(x)<L+\varepsilon=L/2<0.
$$

Elijamos el **punto explícito** $x:=c+t$ con $t=\frac12\min\{\delta,b-c\}>0$. Entonces $x\in I$, $0<|x-c|=t<\delta$, y las dos desigualdades para $q_{f,c}(x)$ se contradicen. Así $f'(c)\ge0$.

Si $f$ es no creciente, el mismo análisis de los dos signos de numerador y denominador proporciona $q_{f,c}(x)\le0$ para todo $x\ne c$ en $I$. Si fuera $L=f'(c)>0$, la tolerancia $L/2$ y el mismo testigo explícito obligarían a $q_{f,c}(x)>L/2>0$, contradicción. Resulta $f'(c)\le0$. Las propiedades estrictas implican las no estrictas por el orden real, de modo que sus conclusiones necesarias son exactamente las mismas desigualdades débiles. Ningún argumento ha supuesto continuidad global ni ha aplicado Lagrange. $\square$

**Dirección lógica.** Bajo las hipótesis de continuidad y derivabilidad del teorema anterior, $f'\ge0$ en el interior es **equivalente** a que $f$ sea no decreciente en el intervalo cerrado; análogamente, $f'\le0$ es equivalente a que sea no creciente. Para la monotonía estricta, en cambio, $f'>0$ es una condición suficiente pero no necesaria.

### Corolario 20.5.4 — Derivada idénticamente nula si y sólo si la función es constante
Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo $[a,b]$ y derivable en cada punto de $(a,b)$. Entonces

$$
\boxed{\bigl[\forall x\in(a,b),\ f'(x)=0\bigr]
\iff
\bigl[\forall u,v\in[a,b],\ f(u)=f(v)\bigr].}
\tag{20.5.4}
$$

**Demostración.**
Si todas las derivadas interiores son cero, satisfacen simultáneamente las desigualdades $f'(x)\ge0$ y $f'(x)\le0$. Por las dos primeras implicaciones de Teorema §20.5.2 — Criterios suficientes de monotonía por el signo de la derivada, $f$ es no decreciente y no creciente en el intervalo completo. Para cualesquiera $u<v$ se obtiene $f(u)\le f(v)\le f(u)$, luego igualdad por antisimetría; si $u=v$ la igualdad es inmediata y si $v<u$ intercambiamos los argumentos. Por tanto $f$ es constante en $[a,b]$.

Recíprocamente, una función constante es no decreciente y no creciente por Definición §20.5.1 — Monotonía estricta y no estricta sobre un dominio ordenado. Como la derivabilidad interior está supuesta, Proposición §20.5.3 — Signos necesarios de la derivada para la monotonía proporciona $f'(x)\ge0$ y $f'(x)\le0$ en cada punto interior; por antisimetría, $f'(x)=0$. Equivalentemente, sus cocientes incrementales son exactamente cero. La continuidad de la hipótesis es necesaria para el primer sentido a través de Lagrange, no para este segundo sentido por sí solo. $\square$

### Corolario 20.5.5 — Caracterización de monotonía estricta sin exigir derivada siempre estricta
Bajo las hipótesis de continuidad y derivabilidad de Teorema §20.5.2 — Criterios suficientes de monotonía por el signo de la derivada, la función $f:[a,b]\to\mathbb R$ es **estrictamente creciente** si y sólo si se cumplen **ambas** condiciones:

$$
\forall x\in(a,b),\quad f'(x)\ge0,
\tag{20.5.5}
$$

$$
\forall u,v\in[a,b],\quad u<v\ \Longrightarrow\
\exists c\in(u,v):\ f'(c)>0.
\tag{20.5.6}
$$

Análogamente, $f$ es **estrictamente decreciente** si y sólo si $f'(x)\le0$ para todos los $x\in(a,b)$ y, para cada $u<v$ del intervalo, existe algún $c\in(u,v)$ con $f'(c)<0$.

**Demostración.**
**Necesidad en el caso creciente.** Si $f$ es estrictamente creciente, también es no decreciente. Proposición §20.5.3 — Signos necesarios de la derivada para la monotonía, aplicado a cada punto interior, demuestra (20.5.5). Fijemos ahora $u<v$ cualesquiera en $[a,b]$. La monotonía estricta da $f(v)-f(u)>0$. El valor medio sobre el dominio original Corolario §20.3.3 — Valor medio en un subintervalo del dominio original proporciona un $c\in(u,v)$ con

$$
f'(c)=\frac{f(v)-f(u)}{v-u}>0,
$$

pues ambos números del cociente son positivos. Queda probada (20.5.6).

**Suficiencia en el caso creciente.** Supongamos (20.5.5)–(20.5.6). El primer criterio de Teorema §20.5.2 — Criterios suficientes de monotonía por el signo de la derivada prueba que $f$ es no decreciente. Para $u<v$ arbitrarios, sabemos entonces que $f(u)\le f(v)$. Si hubiera igualdad, para cualquier $z\in[u,v]$ tendríamos

$$
f(u)\le f(z)\le f(v)=f(u),
$$

luego $f$ sería constante en ese subintervalo. Por (20.5.6), sin embargo, existe $c\in(u,v)$ con $f'(c)>0$. El radio $r:=\frac12\min\{c-u,v-c\}>0$ verifica $B_r(c)\subseteq[u,v]$. Para $x\in[a,b]$ con $0<|x-c|<r$, la constancia obliga a que $[f(x)-f(c)]/(x-c)=0$. El límite de estos cocientes —que existe por la derivabilidad ya supuesta— es por tanto $0$, de modo que $f'(c)=0$, contradicción. Así $f(u)<f(v)$ para cualquier $u<v$ y $f$ es estrictamente creciente.

Para el caso decreciente se invierten las desigualdades: la monotonía estricta decreciente da un cociente secante negativo en Lagrange y Proposición §20.5.3 — Signos necesarios de la derivada para la monotonía implica $f'\le0$; recíprocamente, el criterio no creciente y la existencia de un punto con derivada negativa dentro de cada subintervalo excluyen la igualdad de valores extremos por el mismo argumento de constancia local. No se ha supuesto que exista una elección simultánea de los puntos $c$: sólo se usa el testigo correspondiente a cada par fijado. $\square$

**Contraejemplo a la necesidad de $f'(x)>0$ en todos los puntos.** En Proposición §20.1.6 — Dos límites de alcance: frontera y recíproca falsa ya construimos la función tipada $p:\mathbb R\to\mathbb R$, $p(x)=x\cdot x\cdot x$, y demostramos $p'(0)=0$. No obstante, para cualesquiera $u<v$, la factorización algebraica da

$$
p(v)-p(u)=(v-u)(u^2+uv+v^2),\qquad
u^2+uv+v^2=\frac{(v-u)^2+3(u+v)^2}{4}>0.
$$

El último numerador es positivo porque $(v-u)^2>0$ y los otros sumandos son no negativos; el denominador $4$ es positivo en el cuerpo real. Se deduce $p(u)<p(v)$ para todo $u<v$, aunque la derivada se anule en $0$. Esto separa una condición suficiente de una caracterización necesaria y suficiente.

**Transición.** Los resultados anteriores transforman signos locales en comparaciones globales, con hipótesis de dominio precisas, y muestran cómo detectar los casos de igualdad. La siguiente unidad, §20.6, deducirá **cotas de incrementos y estimaciones Lipschitz** a partir de una cota uniforme de $|f'|$ y del valor medio de Lagrange. La sección §20.5 queda estabilizada como unidad humana; el capítulo permanece abierto y no se abre un nuevo checkpoint Lean.

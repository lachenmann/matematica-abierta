## 20.6. Cotas de incrementos y estimaciones Lipschitz {#sec-ta-20-6}

Hasta ahora hemos empleado el signo de la derivada para comparar *el orden* de los valores de una función. Podemos hacer una pregunta cuantitativa: si conocemos una cota de la derivada, ¿cuánto puede variar la función entre dos argumentos? Lagrange proporciona la respuesta porque identifica cada pendiente secante con una derivada en algún punto interior del segmento.

En §17.6 se demostró ya que una desigualdad de tipo Lipschitz implica continuidad uniforme (Proposición §17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme), sin atribuirla entonces a una derivada. Fijaremos aquí la terminología para esa desigualdad, obtendremos su origen diferencial y delimitaremos con precisión la afirmación recíproca.

### Definición 20.6.1 — Condición Lipschitz relativa al dominio
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y un número real $L\ge0$. Diremos que **$f$ satisface la condición Lipschitz con constante $L$ en $D$** si

$$
\boxed{\forall x,y\in D:\quad |f(x)-f(y)|\le L|x-y|.}
\tag{20.6.1}
$$

Diremos que $f$ **es Lipschitz en $D$** si *existe* al menos una constante real $L\ge0$ que satisface (20.6.1). No se asigna una constante privilegiada ni se define por ahora una «mejor constante» mediante un supremo. La condición tiene sentido para cualquier dominio, incluso vacío; con $L=0$ fuerza igualdad de los valores de $f$ para cada par de argumentos y, por ello, constancia sobre $D$ (vacuamente si éste es vacío).

La expresión «Lipschitz con constante $L$» sigue designando una propiedad de la función ya tipada, no un operador nuevo ni una función derivada global $f'$.

### Lema 20.6.2 — Dos cotas de la derivada encierran todos los incrementos
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo $[a,b]$ y derivable en todos los puntos de $(a,b)$, relativamente a su dominio declarado. Si existen números reales $m,M$ tales que

$$
\forall c\in(a,b),\qquad m\le f'(c)\le M,
$$

entonces, para todos $u,v\in[a,b]$ con $u<v$,

$$
\boxed{m(v-u)\le f(v)-f(u)\le M(v-u).}
\tag{20.6.2}
$$

**Demostración.**
Fijemos un par arbitrario $u<v$ del intervalo. Por ser $[a,b]$ un intervalo cerrado, $[u,v]\subseteq[a,b]$ y $(u,v)\subseteq(a,b)$. En consecuencia, las hipótesis de continuidad y derivabilidad del corolario Corolario §20.3.3 — Valor medio en un subintervalo del dominio original se verifican para ese subintervalo **sin cambiar el dominio de la derivada**: existe $c\in(u,v)$ tal que

$$
f(v)-f(u)=f'(c)(v-u).
$$

El punto $c$ pertenece a $(a,b)$, así que $m\le f'(c)\le M$. Como $v-u>0$, multiplicar las dos desigualdades por $v-u$ preserva sus sentidos y sustituir el producto central por $f(v)-f(u)$ da (20.6.2). La pareja fue arbitraria. Hemos utilizado un testigo para cada instancia fijada de Lagrange, no una selección simultánea $c=c(u,v)$. $\square$

**Lectura de la desigualdad.** Los números $m$ y $M$ encierran las pendientes de todas las secantes, pues al dividir (20.6.2) por $v-u>0$ obtenemos

$$
m\le\frac{f(v)-f(u)}{v-u}\le M.
\tag{20.6.3}
$$

Se trata de una conclusión sobre **todas** las parejas de argumentos, aunque el punto intermedio suministrado por Lagrange puede cambiar de una pareja a otra.

### Teorema 20.6.3 — Una derivada uniformemente acotada implica la condición Lipschitz
Sean $a<b$, $I:=[a,b]$ y $f:I\to\mathbb R$ continua en todo $I$ y derivable en cada punto de $(a,b)$, relativamente a $I$. Si existe un número real $L\ge0$ tal que

$$
\forall c\in(a,b),\qquad |f'(c)|\le L,
\tag{20.6.4}
$$

entonces $f$ es Lipschitz **con esa misma constante $L$** sobre todo $I$:

$$
\boxed{\forall u,v\in I:\quad |f(v)-f(u)|\le L|v-u|.}
\tag{20.6.5}
$$

No se exige que $f'$ exista en los extremos, sea continua o alcance un máximo. «Uniformemente acotada» significa aquí que **un mismo número real finito** $L$ acota los valores absolutos de todas las derivadas interiores.

**Demostración.**
La condición $|f'(c)|\le L$ equivale, por la definición de valor absoluto y las reglas de orden real, a $-L\le f'(c)\le L$. Aplicamos Lema §20.6.2 — Dos cotas de la derivada encierran todos los incrementos con los valores determinados $m:=-L$ y $M:=L$. Para $u<v$ en $I$ resulta

$$
-L(v-u)\le f(v)-f(u)\le L(v-u).
$$

Como $v-u>0$ y $L\ge0$, estas desigualdades son equivalentes a $|f(v)-f(u)|\le L(v-u)=L|v-u|$. Si $u=v$, los dos miembros de (20.6.5) valen cero. Si $v<u$, intercambiamos los argumentos y empleamos las simetrías del valor absoluto $|f(v)-f(u)|=|f(u)-f(v)|$ y $|v-u|=|u-v|$. Así se verifican todos los pares de $I\times I$, exactamente como exige Definición §20.6.1 — Condición Lipschitz relativa al dominio.

La constante final es el $L$ de la hipótesis, sin incrementarlo ni extraer el supremo de los valores de $|f'|$. Si $L=0$, (20.6.5) da $f(u)=f(v)$ para cualquier pareja: este caso concuerda con Corolario §20.5.4 — Derivada idénticamente nula si y sólo si la función es constante y no requiere dividir por $L$. $\square$

**Hipótesis de borde.** La continuidad en $a$ y en $b$ no es superflua. La función de Proposición §20.2.4 — Las tres hipótesis de Rolle no son prescindibles definida en $[0,1]$ por $g(x)=x$ cuando $x<1$ y $g(1)=0$ satisface $g'(x)=1$ para todo $x\in(0,1)$, pero $|g(1)-g(u)|=u$ no puede ser menor o igual que $L(1-u)$ con un $L$ fijo y *todos* los $u<1$: para cada $L\ge0$, tomando $u=(L+1)/(L+2)\in(0,1)$, se tiene $u>L(1-u)$. En particular falla la conclusión con $L=1$. La discontinuidad de borde impide aplicar Lagrange a los subintervalos que lo contienen.

### Corolario 20.6.4 — Continuidad uniforme y oscilación controlada
En las hipótesis de Teorema §20.6.3 — Una derivada uniformemente acotada implica la condición Lipschitz, $f:[a,b]\to\mathbb R$ es uniformemente continua en $[a,b]$. Además, para cualesquiera $u,v\in[a,b]$,

$$
\boxed{|f(v)-f(u)|\le L(b-a).}
\tag{20.6.6}
$$

En particular, $f(a)-L(b-a)\le f(x)\le f(a)+L(b-a)$ para todo $x\in[a,b]$.

**Demostración.**
Por Teorema §20.6.3 — Una derivada uniformemente acotada implica la condición Lipschitz existe la cota Lipschitz sobre $I=[a,b]$ con constante $L\ge0$. La proposición cerrada Proposición §17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme proporciona directamente continuidad uniforme, con el radio explícito $\delta=\varepsilon/(L+1)>0$ para cada $\varepsilon>0$; no se necesita invocar Heine–Cantor de nuevo. Para $u,v\in I$, las desigualdades de pertenencia al intervalo dan $|v-u|\le b-a$. Como $L\ge0$, la cota Lipschitz implica $|f(v)-f(u)|\le L|v-u|\le L(b-a)$. Finalmente, para $u=a$ y $v=x$, la definición del valor absoluto permite escribir $-L(b-a)\le f(x)-f(a)\le L(b-a)$; sumar $f(a)$ da la última afirmación. No se ha definido «oscilación» mediante un supremo no demostrado ni se ha escogido un argumento maximizante. $\square$

### Proposición 20.6.5 — Cota necesaria de la derivada y alcance exacto de la recíproca
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $L\ge0$. Si $f$ satisface la condición Lipschitz con constante $L$ y es derivable en algún punto $c\in D$ relativamente a $D$, entonces

$$
\boxed{|f'(c)|\le L.}
\tag{20.6.7}
$$

Por consiguiente, **bajo las hipótesis de continuidad en $[a,b]$ y derivabilidad en $(a,b)$** del teorema anterior, para cualquier $L\ge0$ se tiene la equivalencia

$$
\boxed{\bigl[f\text{ es Lipschitz con constante }L\text{ en }[a,b]\bigr]
\iff\bigl[\forall c\in(a,b),\ |f'(c)|\le L\bigr].}
\tag{20.6.8}
$$

Sin la hipótesis previa de derivabilidad, una función Lipschitz no tiene por qué ser derivable en todos los puntos interiores.

**Demostración.**
Por definición de derivada (Definición §19.1.3 — Derivabilidad en un punto), el punto $c$ pertenece a $D\cap\operatorname{Acc}(D)$ y existe el límite real $d:=f'(c)$ del cociente incremental $q_{f,c}$ de Definición §19.1.1 — Cociente incremental en un punto. Para todo $x\in D$ distinto de $c$, la condición Lipschitz da

$$
|q_{f,c}(x)|=\frac{|f(x)-f(c)|}{|x-c|}\le L,
$$

pues $|x-c|>0$. Supongamos que $|d|>L$ y fijemos $\varepsilon:=(|d|-L)/2>0$. Del límite existe $\delta>0$ tal que, si $x\in D$ y $0<|x-c|<\delta$, entonces $|q_{f,c}(x)-d|<\varepsilon$. Como $c\in\operatorname{Acc}(D)$, el criterio Lema §16.1.1 — Acumulación y aproximación perforada proporciona **un solo** punto $x$ con esas condiciones. Por desigualdad triangular y por la cota de los cocientes,

$$
|d|\le|d-q_{f,c}(x)|+|q_{f,c}(x)|<\varepsilon+L<|d|,
$$

contradicción. Por tricotomía, $|d|\le L$.

Para (20.6.8), la implicación de izquierda a derecha es la recién probada aplicada separadamente a cada $c\in(a,b)$; la de derecha a izquierda es Teorema §20.6.3 — Una derivada uniformemente acotada implica la condición Lipschitz, cuyas condiciones de continuidad y derivabilidad se encuentran expresamente supuestas. No se han invertido esas hipótesis ni inferido continuidad en los extremos a partir de una derivada sólo interior.

Para comprobar la limitación final, reutilicemos $v:[0,1]\to\mathbb R$ de Proposición §20.2.4 — Las tres hipótesis de Rolle no son prescindibles, dada por $v(x)=|x-\tfrac12|$. Por la desigualdad triangular inversa Corolario §4.2.4 — Desigualdad triangular inversa, para todos $x,y\in[0,1]$ se tiene $|v(x)-v(y)|\le|x-y|$, de modo que $v$ es Lipschitz con constante $1$. Sin embargo, la misma proposición previa demuestra que las pendientes izquierda y derecha en $1/2$ son $-1$ y $1$, respectivamente, y por ello $v'(1/2)$ no existe. En este ejemplo, la condición Lipschitz sí implica continuidad uniforme por Proposición §17.6.3 — Una cota de tipo Lipschitz proporciona un radio uniforme, pero no derivabilidad. $\square$

**Transición.** Una cota sobre una derivada existente controla todos los incrementos entre puntos del intervalo y proporciona continuidad uniforme mediante infraestructura anterior. Lo inverso sólo acota las derivadas **allí donde existen**. En §20.7 estudiaremos una propiedad distinta: aunque la derivada no necesite ser continua, satisface la propiedad de los valores intermedios de Darboux. §20.6 queda estabilizada como unidad humana; el Capítulo 20 permanece abierto y no se inicia un checkpoint Lean nuevo.

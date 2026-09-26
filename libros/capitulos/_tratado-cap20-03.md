## 20.3. Teorema del valor medio de Lagrange {#sec-ta-20-3}

Rolle resuelve el caso de una función cuyos valores en los dos extremos coinciden. Para una función general no podemos exigir esa igualdad, pero sí podemos *fabricarla*: sustraeremos a la función la recta afín que pasa por los dos puntos extremos de su gráfica. La diferencia tendrá valores nulos en ambos extremos. Una vez aplicado Rolle, la regla de derivación de una diferencia recuperará la pendiente de aquella recta.

La construcción no postula una «recta tangente» como objeto geométrico independiente. Se trabaja sólo con funciones tipadas, sus valores y sus derivadas previamente definidos.

### Lema 20.3.1 — Sustracción tipada de la secante y reducción a Rolle
Sean $a,b\in\mathbb R$ con $a<b$, $I:=[a,b]$ y $f:I\to\mathbb R$ una función cualquiera. Definamos el número real

$$
m:=\frac{f(b)-f(a)}{b-a},
$$

la función afín $A:\mathbb R\to\mathbb R$, $A(x):=mx+[f(a)-ma]$, su restricción $\ell:=A\upharpoonright I:I\to\mathbb R$ y la función $h:=f-\ell:I\to\mathbb R$. Entonces:

1. $\ell(x)=f(a)+m(x-a)$ para todo $x\in I$ y $h(a)=h(b)=0$.
2. Si $f$ es continua en cada punto de $I$, $h$ es continua en cada punto de $I$.
3. Si $c\in(a,b)$ y $f$ es derivable en $c$ relativamente a $I$, entonces $h$ es derivable en $c$ relativamente a $I$ y

$$
\boxed{h'(c)=f'(c)-m.}
$$

**Demostración.**
Como $a<b$, tenemos $b-a>0$ y, por tanto, $b-a\ne0$: la división que define $m$ es legítima. La función $A$ existe como grafo funcional por Separación en $\mathbb R\times\mathbb R$; su restricción a $I$ existe por Definición §1.3.1 — Restricción de una función y Proposición §1.3.2 — Existencia y unicidad de la restricción, incorporados en la regla de restricciones utilizada aquí. La resta puntual de dos funciones con el mismo dominio $I$ y el mismo codominio $\mathbb R$ existe por Proposición §16.3.2 — Existencia y tipado de las operaciones puntuales. En particular, $h$ no se ha definido en una recta mayor que $I$.

La distributividad del cuerpo real da, para $x\in I$,

$$
A(x)=mx+f(a)-ma=f(a)+m(x-a).
$$

Por consiguiente, $\ell(a)=f(a)$ y

$$
\ell(b)=f(a)+m(b-a)=f(a)+f(b)-f(a)=f(b).
$$

Al restar los valores correspondientes se obtiene $h(a)=h(b)=0$.

Por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática, la función afín $A$ es derivable en cada punto de $\mathbb R$ y $A'(x)=m$. Todo punto real acumula en la recta, hecho comprobado en la demostración de ese resultado. La implicación derivabilidad $\Rightarrow$ continuidad (Teorema §19.2.1 — Toda función derivable en un punto es continua en él) prueba que $A$ es continua en toda la recta. El corolario de restricciones Corolario §17.4.6 — Clausura global, restricciones y cocientes hace continua a $\ell=A\upharpoonright I$ en todo $I$, incluidos $a$ y $b$. Si $f$ es continua en $I$, la estabilidad de la continuidad bajo diferencias, recogida también en Corolario §17.4.6 — Clausura global, restricciones y cocientes, hace continua a $h=f-\ell$ allí.

Finalmente, si $c\in(a,b)$, el intervalo $I$ acumula en $c$ por Corolario §19.8.5 — Extremos e interior de un intervalo cerrado no degenerado. La regla de restricción de derivadas Proposición §19.5.2 — Restricción de una función derivable se aplica a $A$ y a $I$ y da $\ell'(c)=A'(c)=m$. Puesto que $f$ es derivable en $c$ por hipótesis, Corolario §19.4.2 — Multiplicación por escalares, opuestos y diferencias, aplicado a dos funciones de dominio exactamente $I$, demuestra que $h$ es derivable allí y que $h'(c)=f'(c)-\ell'(c)=f'(c)-m$. No se ha usado Rolle ni se han elegido representantes o argumentos para una familia infinita. $\square$

**Lectura de la construcción.** La constante $f(a)-ma$ sitúa correctamente la recta; el cociente que define $m$ fija su pendiente. La función $h$ mide la diferencia vertical entre $f$ y esa recta. Lo que se anula en los extremos son los *valores de $h$*, no los de $f$.

### Teorema 20.3.2 — Teorema del valor medio de Lagrange
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$. Supongamos que $f$ es continua en todo $[a,b]$, relativamente a ese dominio, y derivable en cada punto de $(a,b)$, también relativamente a $[a,b]$. Entonces existe al menos un $c\in(a,b)$ tal que

$$
\boxed{f'(c)=\frac{f(b)-f(a)}{b-a}.}
\tag{20.3.1}
$$

Equivalentemente, para ese mismo punto $c$,

$$
\boxed{f(b)-f(a)=f'(c)(b-a).}
\tag{20.3.2}
$$

El punto $c$ depende, en general, de la función y del intervalo, y no se afirma que sea único. El denominador $b-a$ es positivo; la hipótesis $a<b$ no se sustituye por $a\le b$.

**Demostración.**
Sea $I=[a,b]$ y fijemos el número $m=[f(b)-f(a)]/(b-a)$ y la función auxiliar $h:I\to\mathbb R$ construidos en Lema §20.3.1 — Sustracción tipada de la secante y reducción a Rolle. Este lema prueba, primero, que $h(a)=h(b)=0$ y, segundo, que $h$ es continua en todo $I$, pues $f$ lo es. Para cada $x\in(a,b)$ la hipótesis de derivabilidad de $f$ y la tercera parte del lema prueban que $h$ es derivable en $x$.

Así quedan verificadas, una por una, las tres hipótesis de Rolle Teorema §20.2.2 — Teorema de Rolle para la función $h:I\to\mathbb R$. Existe por tanto $c\in(a,b)$ con $h'(c)=0$. La fórmula para su derivada, obtenida antes de aplicar Rolle, proporciona

$$
0=h'(c)=f'(c)-m.
$$

Por cancelación aditiva, $f'(c)=m=[f(b)-f(a)]/(b-a)$, que es (20.3.1). Multiplicar por el real positivo $b-a$ da (20.3.2). Sólo se obtuvo un testigo existencial de Rolle para una función determinada; no se define una selección $f\mapsto c$, ni se adopta Choice. $\square$

**Interpretación.** El cociente $[f(b)-f(a)]/(b-a)$ es la pendiente de la secante entre los extremos. El teorema asegura que al menos una pendiente derivada interior toma exactamente ese valor. No dice que todas las derivadas interiores sean iguales a la pendiente secante, ni que la igualdad se alcance en un punto predeterminado.

### Corolario 20.3.3 — Valor medio en un subintervalo del dominio original
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $u,v\in D$ con $u<v$ y $[u,v]\subseteq D$. Supongamos que $f$ es continua en cada punto de $[u,v]$ relativamente a $D$ y que es derivable en cada punto de $(u,v)$ relativamente a $D$. Entonces existe $c\in(u,v)$ para el cual la derivada de la función original satisface

$$
\boxed{f(v)-f(u)=f'(c)(v-u).}
$$

**Demostración.**
Pongamos $I:=[u,v]$ y formemos la restricción tipada $g:=f\upharpoonright I:I\to\mathbb R$. Sus valores en cada punto de $I$ coinciden con los de $f$. Como $f$ es continua en cada punto de $I$ respecto de $D$, todo radio de continuidad allí sirve para los argumentos del subconjunto $I$; formalmente, Corolario §17.4.6 — Clausura global, restricciones y cocientes garantiza la continuidad de $g$ en $I$.

Para cada $x\in(u,v)$, Corolario §19.8.5 — Extremos e interior de un intervalo cerrado no degenerado asegura $x\in\operatorname{Acc}(I)$. Por derivabilidad de $f$ en $x$ relativa a $D$ y por el teorema de restricciones Proposición §19.5.2 — Restricción de una función derivable, la función $g$ es derivable en $x$ y $g'(x)=f'(x)$. Aplicamos Teorema §20.3.2 — Teorema del valor medio de Lagrange a $g:I\to\mathbb R$. Obtenemos algún $c\in(u,v)$ con $g(v)-g(u)=g'(c)(v-u)$. Las tres igualdades de valores y derivada justificadas anteriormente convierten esto en la fórmula enunciada para $f$. Se restringió una función ya dada; no se reconstruyó su codominio ni se extendió indebidamente una derivada. $\square$

**Dos comprobaciones concretas.** Para la función $f:\mathbb R\to\mathbb R$ dada por $f(x)=x^2$, Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática da $f'(x)=2x$. En $[a,b]$, con $a<b$, la pendiente secante es

$$
\frac{b^2-a^2}{b-a}=a+b=2\,\frac{a+b}{2}.
$$

El punto $c=(a+b)/2$ pertenece a $(a,b)$ y verifica el teorema; en este ejemplo es el único, porque $2c=a+b$ determina un solo real. Por contraste, para una función constante todos los puntos interiores cumplen la igualdad, de modo que el teorema no puede prometer unicidad en general.

**Alcance de las hipótesis.** Los contraejemplos ya construidos en Proposición §20.2.4 — Las tres hipótesis de Rolle no son prescindibles sirven también para comprobar que continuidad en todo el intervalo y derivabilidad en todo su interior no pueden omitirse del enunciado universal de Lagrange. En ambos, los valores extremos coinciden y la pendiente secante es cero, pero no aparece ninguna derivada interior nula. No se exige, en cambio, que los valores de borde coincidan: ésa era la condición especial de Rolle y precisamente la hemos eliminado mediante la función auxiliar. La desigualdad estricta $a<b$ evita una división por cero y asegura un intervalo interior no degenerado.

**Transición.** La identidad de valor medio relaciona el incremento global con una derivada en algún punto interior. El siguiente paso, §20.4, estudiará el teorema del valor medio de Cauchy para dos funciones. Más adelante se podrán deducir los criterios de monotonía y las cotas de incrementos sin introducirlos retroactivamente aquí. La presente sección está estabilizada como unidad humana; el capítulo 20 permanece abierto. No se abre un nuevo checkpoint Lean.

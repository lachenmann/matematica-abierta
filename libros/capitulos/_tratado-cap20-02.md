## 20.2. Teorema de Rolle {#sec-ta-20-2}

El teorema de Fermat convierte un extremo local interior en una derivada nula, pero no garantiza que exista ese extremo. El teorema de Weierstrass garantiza extremos globales sobre un compacto no vacío, aunque podría situarlos en los extremos del intervalo, donde Fermat no es aplicable. La igualdad de los valores en los extremos resolverá esta dificultad: o bien la función es constante, o bien alguno de sus extremos globales debe alcanzarse en el interior.

### Lema 20.2.1 — Valores extremos iguales y función no constante: existe un extremo global interior
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$ continua en todo su dominio. Supongamos que $f(a)=f(b)=k$ y que existe $y\in[a,b]$ con $f(y)\ne k$. Entonces existe $c\in(a,b)$ en el cual $f$ alcanza **un máximo global o un mínimo global** sobre $[a,b]$.

**Demostración.**
Por $a<b$, el conjunto $I:=[a,b]$ contiene a $a$ y es compacto por Teorema §18.2.1 — Todo intervalo cerrado y acotado es compacto. Aplicamos Teorema §18.5.4 — Teorema del valor extremo: Weierstrass a la función **con dominio exactamente $I$**. Existen puntos $x_-,x_+\in I$ tales que, para todo $x\in I$,

$$
f(x_-)\le f(x)\le f(x_+).
$$

Fijemos el testigo $y\in I$ de la hipótesis. La tricotomía del orden real y $f(y)\ne k$ permiten distinguir dos casos.

Si $f(y)>k$, entonces $f(x_+)\ge f(y)>k=f(a)=f(b)$. Por ello $x_+$ no puede ser ni $a$ ni $b$. Como pertenece a $[a,b]$, necesariamente $a<x_+<b$: es un punto interior en que se alcanza el máximo global.

Si $f(y)<k$, se tiene $f(x_-)\le f(y)<k=f(a)=f(b)$. El mismo argumento sitúa $x_-$ en $(a,b)$, donde se alcanza el mínimo global.

La demostración sólo obtiene los dos puntos cuya existencia afirma Weierstrass y fija el único testigo de desviación dado; no construye una selección de extremos para una familia de funciones. $\square$

**Interpretación.** La coincidencia de los valores de borde no asegura por sí sola que *ambos* extremos globales estén en el interior. Asegura algo más preciso y suficiente: si aparece un valor superior al común de los bordes, el máximo se desplaza al interior; si aparece uno inferior, lo hace el mínimo.

### Teorema 20.2.2 — Teorema de Rolle
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$. Supongamos que:

1. $f$ es **continua en todo** $[a,b]$, con continuidad relativa en los extremos;
2. $f$ es **derivable en cada** $x\in(a,b)$, relativamente al dominio $[a,b]$;
3. $f(a)=f(b)$.

Entonces existe al menos un punto $c\in(a,b)$ tal que

$$
\boxed{f'(c)=0.}
$$

La derivada indicada es la de la función tipada $f:[a,b]\to\mathbb R$. La conclusión es existencial: no asegura unicidad ni selecciona un punto distinguido entre todos los posibles.

**Demostración.**
Escribamos $k:=f(a)=f(b)$ y distingamos si $f(x)=k$ para todos los $x\in[a,b]$.

**Caso constante.** Pongamos $c:=(a+b)/2$. Puesto que $a<b$, las operaciones y el orden del cuerpo real dan $a<c<b$. Como todos los valores de $f$ son $k$, el punto $c$ es simultáneamente máximo y mínimo global. Por hipótesis, $f$ es derivable en $c$; Corolario §20.1.5 — Fermat en puntos interiores de un intervalo cerrado (Fermat sobre un intervalo cerrado) proporciona $f'(c)=0$.

**Caso no constante.** Existe un $y\in[a,b]$ tal que $f(y)\ne k$. Por la continuidad en el intervalo completo, las hipótesis de Lema §20.2.1 — Valores extremos iguales y función no constante: existe un extremo global interior están satisfechas. El lema aporta un punto $c\in(a,b)$ donde $f$ alcanza un máximo o un mínimo global. La derivabilidad en $c$ es una de las hipótesis del presente teorema. Aplicamos de nuevo Corolario §20.1.5 — Fermat en puntos interiores de un intervalo cerrado y obtenemos $f'(c)=0$.

En ambos casos se ha producido un punto interior con derivada nula. Weierstrass aparece únicamente en la prueba anterior del lema; el paso del extremo a la derivada nula es Fermat. No se ha supuesto ningún teorema del valor medio ni se ha hecho una elección simultánea de puntos. $\square$

**Lectura de la prueba.** La continuidad en el intervalo cerrado garantiza extremos alcanzados; la igualdad de los valores de borde y la distinción entre constancia y no constancia garantizan un extremo interior; la derivabilidad allí permite usar Fermat. Cada hipótesis cumple una función diferente, y no es legítimo sustituir continuidad en $[a,b]$ por continuidad sólo en $(a,b)$.

### Corolario 20.2.3 — Entre dos ceros existe un punto de derivada nula
Sean $a<b$ y $f:[a,b]\to\mathbb R$ continua en $[a,b]$ y derivable en cada punto de $(a,b)$. Si $f(a)=f(b)=0$, entonces existe $c\in(a,b)$ con $f'(c)=0$.

**Demostración.**
La igualdad $f(a)=f(b)=0$ implica la tercera hipótesis de Teorema §20.2.2 — Teorema de Rolle; las otras dos están expresamente supuestas y el dominio es exactamente $[a,b]$. Aplicar Rolle proporciona el punto interior requerido. No se afirma que ese punto sea un cero de la función. $\square$

### Proposición 20.2.4 — Las tres hipótesis de Rolle no son prescindibles
En cada ejemplo el dominio y codominio son $[0,1]$ y $\mathbb R$, respectivamente. Si se suprime **una sola** de las tres hipótesis del teorema, las otras dos pueden cumplirse sin que exista un punto interior de derivada nula.

**Demostración.**
**1. Sin continuidad en el intervalo cerrado.** Definamos, mediante el grafo funcional obtenido por Separación en $[0,1]\times\mathbb R$,

$$
u(x)=\begin{cases}x,&0\le x<1,\\0,&x=1.\end{cases}
$$

Se tiene $u(0)=u(1)=0$. Para todo $c\in(0,1)$ tomemos $r:=\frac12\min\{c,1-c\}>0$. Cuando $x\in[0,1]$ y $0<|x-c|<r$, ambos puntos están en $(0,1)$, donde $u(x)=x$ y $u(c)=c$; por tanto, el cociente incremental vale exactamente $1$. De la definición de derivada resulta $u'(c)=1$ para todo $c\in(0,1)$.

Sin embargo, $u$ no es continua en $1$. Dado cualquier $\delta>0$, el argumento explícito $x:=1-\frac12\min\{\delta,1\}$ pertenece a $(0,1)$ y satisface $|x-1|<\delta$, mientras que $|u(x)-u(1)|=x\ge\frac12>\frac14$. La tolerancia $\varepsilon=\frac14$ refuta la continuidad relativa en $1$. Se mantienen la igualdad de valores extremos y la derivabilidad interior, pero falla la conclusión.

**2. Sin derivabilidad en todo el interior.** Definamos $v:[0,1]\to\mathbb R$ por

$$
v(x):=\left|x-\tfrac12\right|.
$$

La desigualdad triangular inversa Corolario §4.2.4 — Desigualdad triangular inversa da $|v(x)-v(z)|\le|x-z|$ para $x,z\in[0,1]$, de modo que $v$ es continua también en los extremos. Además $v(0)=v(1)=1/2$. En cualquier $c\in(0,1/2)$, una bola suficientemente pequeña conserva $x<1/2$, y allí $v(x)=1/2-x$; los cocientes incrementales son $-1$, luego $v'(c)=-1$. Análogamente, para $c\in(1/2,1)$, $v(x)=x-1/2$ localmente y $v'(c)=1$.

En el punto $m:=1/2$, los cocientes de $v$ respecto del dominio $[0,1]$ son exactamente $-1$ a la izquierda y $1$ a la derecha. Ambos lados acumulan en $m$, por lo que el criterio Teorema §19.8.4 — Reconstrucción de la derivada desde los lados activos impide que exista $v'(m)$. Así no hay ningún $c\in(0,1)$ con derivada nula, a pesar de la continuidad y la igualdad de los valores extremos.

**3. Sin igualdad de los valores extremos.** La identidad restringida $w:[0,1]\to\mathbb R$, $w(x)=x$, es continua, derivable en todos los puntos interiores e incluso en los extremos relativamente a su dominio, con $w'(c)=1$ en todo punto de acumulación por Proposición §20.1.6 — Dos límites de alcance: frontera y recíproca falsa. Pero $w(0)=0\ne1=w(1)$; no existe derivada nula interior.

En los tres casos los grafos están determinados unívocamente por las fórmulas indicadas; las pruebas usan radios explícitos y ninguna selección infinita. La independencia de las hipótesis significa que ninguna de las tres puede eliminarse **sin sustitución alguna** del enunciado general; no excluye que puedan encontrarse otras condiciones suficientes. $\square$

**Transición.** Rolle obtiene una pendiente nula cuando los valores de dos extremos coinciden. Para comparar valores extremos *distintos* se introducirá en §20.3 una función auxiliar que sustraiga la recta secante. Aplicaremos Rolle a esa función y deduciremos el teorema del valor medio de Lagrange sin emplearlo retroactivamente en ninguna prueba de este tramo. La sección §20.2 queda estabilizada como unidad humana; el capítulo continúa en borrador y no se abre un checkpoint Lean.

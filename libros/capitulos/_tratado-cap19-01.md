## 19.1. Cociente incremental y definición de derivada {#sec-ta-19-1}

Para $x\ne a$, los puntos $(a,f(a))$ y $(x,f(x))$ determinan una pendiente secante. Su expresión algebraica tiene sentido sin suponer previamente que exista una tangente. La derivada, si existe, será el límite de esas pendientes; no se asignará valor al cociente en $x=a$ para fabricar artificialmente ese límite.

### Definición 19.1.1 — Cociente incremental en un punto
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Pongamos $D_a:=D\setminus\{a\}$. El cociente incremental de $f$ en $a$ es la función tipada

$$
\boxed{q_{f,a}:D_a\longrightarrow\mathbb R,\qquad
q_{f,a}(x):=\frac{f(x)-f(a)}{x-a}\quad(x\in D_a).}
$$

Su grafo es el subconjunto de $D_a\times\mathbb R$ de los pares $\langle x,y\rangle$ que cumplen $(x-a)y=f(x)-f(a)$; existe por Separación. Como $x\ne a$, tenemos $x-a\ne0$ y los axiomas del cuerpo proporcionan un único $y$, luego el grafo define efectivamente una función de dominio $D_a$ y codominio $\mathbb R$. También cuando $D_a=\varnothing$ existe la función vacía con esos tipos; en tal caso no se le atribuirá límite en $a$.

La abreviatura $D_a$ y el nombre $q_{f,a}$ se emplean únicamente respecto de los datos $D,f,a$ fijados. La igualdad del cociente exige $x\ne a$; escribir $q_{f,a}(a)$ sería una evaluación fuera del dominio, no un cociente igual a cero.

### Lema 19.1.2 — Perforar el dominio preserva la acumulación en el centro
Con las hipótesis de la definición anterior, se cumple

$$
\boxed{a\in\operatorname{Acc}(D)\quad\Longleftrightarrow\quad
 a\in\operatorname{Acc}(D_a).}
$$

**Demostración.**
Por Lema §16.1.1 — Acumulación y aproximación perforada, la primera pertenencia equivale a que, para todo $r>0$, exista $x\in D$ tal que $0<|x-a|<r$. La desigualdad estricta $0<|x-a|$ equivale a $x\ne a$ por Proposición §4.2.2 — Propiedades elementales del valor absoluto. Por tanto, esos mismos testigos pertenecen exactamente a $D\setminus\{a\}=D_a$. Aplicando de nuevo Lema §16.1.1 — Acumulación y aproximación perforada, ahora a $D_a$, se obtiene la segunda pertenencia. La equivalencia no selecciona una sucesión de testigos: compara dos condiciones existenciales para cada radio considerado. $\square$

### Definición 19.1.3 — Derivabilidad en un punto
Sean $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Diremos que $f$ es derivable en $a$, relativamente al dominio $D$, si existe $L\in\mathbb R$ tal que

$$
\boxed{\lim_{\substack{x\to a\\x\in D_a}}q_{f,a}(x)=L.}
$$

En forma completamente desarrollada, la condición equivale a

$$
\exists L\in\mathbb R\ \forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\ \Longrightarrow\quad
\left|\frac{f(x)-f(a)}{x-a}-L\right|<\varepsilon.
$$

El lema anterior garantiza que $a$ es punto de acumulación de $D_a$, requisito de la definición de límite del capítulo 16. La función ha de estar definida en $a$ para calcular $f(a)$ y debe admitir otros puntos del dominio arbitrariamente próximos: ambas condiciones son necesarias. La definición no exige que $D$ sea abierto ni que existan puntos a ambos lados de $a$. En un extremo de intervalo puede estudiarse esta derivada relativa al dominio; las derivadas laterales recibirán tratamiento explícito más adelante.

### Proposición 19.1.4 — Unicidad y criterio cuantificado de la derivada
Sean $f:D\to\mathbb R$ y $a\in D\cap\operatorname{Acc}(D)$. Existe a lo sumo un $L\in\mathbb R$ que satisface la condición de derivabilidad. Para un $L$ dado, dicha condición equivale a

$$
\boxed{\forall\varepsilon>0\ \exists\delta>0\ \forall x\in D:\quad
0<|x-a|<\delta\Longrightarrow
|f(x)-f(a)-L(x-a)|<\varepsilon|x-a|.}
$$

**Demostración.**
Por Lema §19.1.2 — Perforar el dominio preserva la acumulación en el centro, $a\in\operatorname{Acc}(D_a)$; el cociente $q_{f,a}$ tiene el tipo requerido por Definición §16.1.2 — Límite real finito de una función relativo a su dominio. Si dos números $L,M$ cumplen la relación de límite para esa misma función y ese mismo dominio, el teorema de unicidad Teorema §16.1.4 — Unicidad del límite finito impone $L=M$.

Para demostrar el criterio, fijemos $x\in D$ con $0<|x-a|<\delta$. Entonces $x-a\ne0$ y $|x-a|>0$. Las propiedades del valor absoluto y las identidades del cuerpo permiten multiplicar una desigualdad estricta por este número positivo sin cambiar su sentido:

$$
\begin{aligned}
\left|\frac{f(x)-f(a)}{x-a}-L\right|<\varepsilon
&\iff \left|\frac{f(x)-f(a)-L(x-a)}{x-a}\right|<\varepsilon\\
&\iff |f(x)-f(a)-L(x-a)|<\varepsilon|x-a|.
\end{aligned}
$$

Cada equivalencia vale para todo argumento admisible y los mismos $\varepsilon,\delta$. Al anteponer los cuantificadores del límite se obtiene la equivalencia afirmada. No se ha definido ni evaluado el cociente en $a$. $\square$

### Notación 19.1.5 — Valor de la derivada
Cuando $f$ sea derivable en $a$, designaremos por $f'(a)$ el único número $L$ de la definición:

$$
\boxed{f'(a):=\lim_{\substack{x\to a\\x\in D_a}}
\frac{f(x)-f(a)}{x-a}.}
$$

Esta notación no declara todavía una función derivada $f'$ sobre todo $D$: el valor $f'(a)$ sólo está definido en puntos donde hemos comprobado la derivabilidad. Más adelante podremos formar, por Separación, el conjunto de esos puntos y construir una función con ese dominio y codominio $\mathbb R$. La prima en $f'(a)$ se refiere a la función; el conjunto derivado de §15.5 continúa escrito $\operatorname{Acc}(A)$ y nunca se denotará $A'$ en este tratado.

### Proposición 19.1.6 — Primeros cálculos: funciones afines y función cuadrática
Si $m,b\in\mathbb R$ y $f:\mathbb R\to\mathbb R$ está dada por $f(x)=mx+b$, entonces $f$ es derivable en cada $a\in\mathbb R$ y $f'(a)=m$. Si $g:\mathbb R\to\mathbb R$ está dada por $g(x)=x^2$, entonces $g$ es derivable en cada $a\in\mathbb R$ y $g'(a)=2a$, donde $2=1+1$ es el numeral real.

**Demostración.**
Las expresiones algebraicas determinan funciones $\mathbb R\to\mathbb R$ mediante grafos funcionales obtenidos por Separación dentro de $\mathbb R\times\mathbb R$. Fijemos $a\in\mathbb R$. La propiedad arquimediana de la recta, o simplemente la posibilidad de tomar $a+r/2$ con $r>0$, demuestra que $a\in\operatorname{Acc}(\mathbb R)$: para cada $r>0$, el punto $x=a+r/2$ satisface $0<|x-a|<r$. No hace falta elegir tales puntos para todos los radios simultáneamente.

**Caso afín.** Para todo $x\ne a$, la distributividad y la cancelación en el cuerpo real dan

$$
q_{f,a}(x)=\frac{mx+b-(ma+b)}{x-a}=m.
$$

Para cualquier $\varepsilon>0$ sirve $\delta=1$: si $0<|x-a|<\delta$, entonces $|q_{f,a}(x)-m|=0<\varepsilon$. De esta manera el límite del cociente es $m$, y su unicidad legitima $f'(a)=m$. La función constante es el caso particular $m=0$; la identidad, el caso $m=1,b=0$.

**Caso cuadrático.** Si $x\ne a$, la factorización algebraica legítima en $\mathbb R$ da

$$
q_{g,a}(x)=\frac{x^2-a^2}{x-a}=x+a.
$$

Para $\varepsilon>0$ elegimos $\delta=\varepsilon$. Entonces $0<|x-a|<\delta$ implica

$$
|q_{g,a}(x)-2a|=|x+a-(a+a)|=|x-a|<\varepsilon.
$$

Luego el límite existe y vale $2a$, como se afirma. La cancelación $x-a$ se efectuó antes de tomar el límite y sólo para $x\ne a$; no se definió una división por cero en el centro. $\square$

**Lectura conceptual.** El límite de pendientes secantes aporta un número —cuando existe— que resume el comportamiento de primer orden de la función alrededor de $a$. En el caso afín no cambia con el punto; para $x^2$ depende de $a$. La caracterización mediante el error $f(x)-f(a)-L(x-a)$ anuncia la aproximación lineal que estudiaremos después, pero todavía no la empleamos como definición alternativa sin prueba.

**Transición.** La siguiente cuestión es si la existencia de esta pendiente límite obliga a la función a ser continua en el punto. Demostraremos esa implicación en §19.2 directamente a partir del cociente incremental, sin usar Rolle ni los teoremas del valor medio.

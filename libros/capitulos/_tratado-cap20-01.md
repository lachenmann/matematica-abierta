## 20.1. Extremos locales y teorema de Fermat {#sec-ta-20-1}

### Definición 20.1.1 — Máximo y mínimo locales relativos al dominio
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Diremos que $f$ tiene un **máximo local en $a$, relativamente a $D$**, si existe $r>0$ tal que

$$
\boxed{\forall x\in D:\ |x-a|<r\Longrightarrow f(x)\le f(a).}
$$

Diremos que tiene un **mínimo local en $a$, relativamente a $D$**, si existe $r>0$ tal que

$$
\boxed{\forall x\in D:\ |x-a|<r\Longrightarrow f(a)\le f(x).}
$$

Un extremo local es cualquiera de esas dos posibilidades. Si, además, la desigualdad correspondiente es estricta para todo $x\in D$ con $0<|x-a|<r$, diremos que el extremo es **estricto**. El radio $r$ puede depender de $a$; las comparaciones se hacen sólo con argumentos del dominio original y no presuponen que $D$ contenga una vecindad completa de $a$.

Estos extremos son propiedades de $f$ **en el punto**: no crean una función derivada ni un nuevo objeto de elección. Un máximo o mínimo global de $f$ es un extremo local, pues su desigualdad vale para todo $x\in D$ y podemos tomar cualquier radio positivo. En un punto aislado del dominio, las dos condiciones locales pueden valer a la vez por vacuidad; ello no hace que exista una derivada allí, conforme a Definición §19.1.3 — Derivabilidad en un punto. El extremo estricto exige comparar sólo con argumentos distintos del centro, sin hacer imposible una igualdad necesaria $f(a)=f(a)$.

### Lema 20.1.2 — Un punto interior acumula desde ambos lados
Si $D\subseteq\mathbb R$ y $a$ es interior a $D$, entonces

$$
\boxed{a\in\operatorname{Acc}(D_a^-)\cap\operatorname{Acc}(D_a^+).}
$$

En particular, $a\in D\cap\operatorname{Acc}(D)$, de manera que la definición de derivada relativa puede aplicarse en $a$ si existe el límite pertinente.

**Demostración.**
Por interioridad (Definición §15.2.1 — Punto interior de un conjunto), existe $\rho>0$ tal que $B_\rho(a)\subseteq D$. Fijemos **un radio arbitrario** $s>0$ y pongamos $t:=\frac12\min\{\rho,s\}>0$. Los puntos explícitos $x_-:=a-t$ y $x_+:=a+t$ cumplen

$$
0<a-x_-=t<s,\qquad 0<x_+-a=t<s,
$$

y $|x_\pm-a|=t<\rho$, por lo que pertenecen a $D$. El primero está en $D_a^-$ y el segundo en $D_a^+$. El criterio de acumulación Lema §16.1.1 — Acumulación y aproximación perforada, aplicado a cada lado, prueba ambas pertenencias. La pertenencia $a\in D$ se deduce de que el centro pertenece a la bola $B_\rho(a)$; la acumulación de $D$ sigue por inclusión de cualquiera de sus lados. Para cada $s$ usamos fórmulas determinadas, no una selección simultánea de testigos. $\square$

### Proposición 20.1.3 — Restricciones de signo para las derivadas laterales en un extremo
Sean $f:D\to\mathbb R$ y $a\in D$. Las afirmaciones siguientes se entienden **únicamente cuando la derivada lateral indicada existe**, con su hipótesis de acumulación ya incluida en Definición §19.8.1 — Derivabilidad por la izquierda y por la derecha:

- Si $f$ tiene un **mínimo local** en $a$, entonces $f'_-(a)\le0$ si existe la derivada izquierda, y $f'_+(a)\ge0$ si existe la derecha.
- Si $f$ tiene un **máximo local** en $a$, entonces $f'_-(a)\ge0$ si existe la derivada izquierda, y $f'_+(a)\le0$ si existe la derecha.

No se afirma la existencia de ninguna derivada lateral a partir del solo extremo local.

**Demostración.**
Supongamos primero que $a$ es un mínimo local y fijemos $r>0$ para el cual $f(x)-f(a)\ge0$ si $x\in D$ y $|x-a|<r$. Para tales $x\ne a$, el cociente incremental $q_{f,a}(x)$ es **no positivo a la izquierda**, pues $x-a<0$, y **no negativo a la derecha**, pues $x-a>0$.

Si existe la derivada izquierda $L_-:=f'_-(a)$ y fuera $L_->0$, el criterio cuantificado de Proposición §19.8.2 — Criterios cuantificados y unicidad lateral, con $\varepsilon=L_-/2$, proporcionaría $\delta_->0$ tal que

$$
0<a-x<\delta_-\Longrightarrow
q_{f,a}(x)>L_-/2>0.
$$

Como la definición de derivada izquierda exige $a\in\operatorname{Acc}(D_a^-)$, existe un único testigo local $x\in D_a^-$ con $0<a-x<\min\{r,\delta_-\}$. Para él, el mínimo local da $q_{f,a}(x)\le0$, contradicción. Por tanto $L_-\le0$.

Si existe la derivada derecha $L_+:=f'_+(a)$ y fuera $L_+<0$, el mismo razonamiento con $\varepsilon=-L_+/2$ y un testigo $x\in D_a^+$ suficientemente próximo daría $q_{f,a}(x)<L_+/2<0$, en contradicción con $q_{f,a}(x)\ge0$. Por consiguiente $L_+\ge0$.

Para un máximo local las diferencias $f(x)-f(a)$ son no positivas. Sus cocientes son, respectivamente, **no negativos a la izquierda** y **no positivos a la derecha**. Si $f'_-(a)<0$, una tolerancia $-f'_-(a)/2$ y un testigo izquierdo obligarían al cociente a ser negativo, contradicción. Si $f'_+(a)>0$, la tolerancia $f'_+(a)/2$ y un testigo derecho lo obligarían a ser positivo, también contradicción. Quedan probadas las dos desigualdades restantes. Sólo se instancian finitamente radios y testigos en cada argumento; no se construye una sucesión de elecciones. $\square$

**Interpretación.** En un mínimo, la pendiente secante que llega desde la izquierda no puede tener límite positivo y la que sale por la derecha no puede tener límite negativo. Las condiciones se invierten para un máximo. Esta descripción conserva el sentido de la derivada relativa en los extremos del dominio: allí puede existir un solo lado activo y nada obliga a que su pendiente sea nula.

### Teorema 20.1.4 — Fermat: derivada nula en un extremo local interior
Sean $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$. Supongamos que:

1. $a$ es un punto **interior** de $D$;
2. $f$ es derivable en $a$ relativamente a $D$;
3. $f$ tiene un máximo local o un mínimo local en $a$, relativamente a $D$.

Entonces

$$
\boxed{f'(a)=0.}
$$

La afirmación es una **condición necesaria** para un extremo local interior en un punto derivable; no afirma que la anulación de la derivada sea suficiente para tener un extremo.

**Demostración.**
Por Lema §20.1.2 — Un punto interior acumula desde ambos lados, ambos lados $D_a^-$ y $D_a^+$ acumulan en $a$; además, $a\in D\cap\operatorname{Acc}(D)$, por lo que la derivada de la hipótesis está bien tipada. El teorema Teorema §19.8.4 — Reconstrucción de la derivada desde los lados activos, aplicado a la función original $f:D\to\mathbb R$, garantiza que existen sus dos derivadas laterales y que

$$
f'_-(a)=f'(a)=f'_+(a).
$$

Si $a$ es un mínimo local, Proposición §20.1.3 — Restricciones de signo para las derivadas laterales en un extremo proporciona $f'_-(a)\le0\le f'_+(a)$. La igualdad común anterior implica a la vez $f'(a)\le0$ y $0\le f'(a)$; por antisimetría del orden real, $f'(a)=0$.

Si $a$ es un máximo local, las desigualdades de la misma proposición se invierten: $f'_-(a)\ge0\ge f'_+(a)$. La igualdad común vuelve a dar $f'(a)=0$. La prueba sólo utiliza el criterio bilateral-lateral cerrado en el capítulo 19 y las desigualdades locales anteriores: no invoca el teorema del valor extremo, Rolle, valor medio ni Taylor. $\square$

**Lectura deductiva.** La interioridad garantiza **dos direcciones disponibles**; la derivabilidad exige que las dos pendientes límite coincidan; la condición de extremo obliga a esas pendientes a quedar en lados opuestos de cero. El único valor compatible con las tres afirmaciones es cero. Sin interioridad desaparece una de las restricciones de signo y el argumento deja de imponer la conclusión.

### Corolario 20.1.5 — Fermat en puntos interiores de un intervalo cerrado
Sean $a,b\in\mathbb R$ con $a<b$ y $f:[a,b]\to\mathbb R$. Si $c\in(a,b)$ es un punto de máximo o mínimo de $f$ **sobre todo $[a,b]$** y $f$ es derivable en $c$ relativamente a ese intervalo, entonces $f'(c)=0$.

**Demostración.**
Como $a<c<b$, el número $\rho:=\frac12\min\{c-a,b-c\}$ es positivo y satisface $B_\rho(c)\subseteq[a,b]$ por las desigualdades que definen el intervalo. En consecuencia, $c$ es interior al dominio $[a,b]$. La desigualdad de máximo o mínimo global vale para **todos** los puntos del intervalo, de modo que también vale en esa bola y constituye un extremo local conforme a Definición §20.1.1 — Máximo y mínimo locales relativos al dominio. La derivabilidad está dada. Aplicamos Teorema §20.1.4 — Fermat: derivada nula en un extremo local interior a la función tipada $f:[a,b]\to\mathbb R$ y obtenemos $f'(c)=0$. No se necesita continuidad sobre todo $[a,b]$ para este corolario: sólo se han utilizado las hipótesis declaradas en el punto $c$. $\square$

### Proposición 20.1.6 — Dos límites de alcance: frontera y recíproca falsa
La interioridad y la dirección de la implicación en Fermat no pueden omitirse:

1. La función $u:[0,1]\to\mathbb R$ dada por $u(x)=x$ tiene un mínimo global en $0$, un máximo global en $1$ y derivadas relativas $u'(0)=u'(1)=1\ne0$.
2. Existe una función derivable $v:\mathbb R\to\mathbb R$ con $v'(0)=0$ que no tiene ni máximo ni mínimo local en $0$.

**Demostración.**
**Primera afirmación.** Sea $i:\mathbb R\to\mathbb R$ la identidad e $I:=[0,1]$. El intervalo está contenido en $\mathbb R$ y la restricción $u:=i\upharpoonright I:I\to\mathbb R$ existe; tiene los valores $u(x)=x$. Para todo $x\in I$, $0\le u(x)\le1$, así que $0$ es un mínimo y $1$ un máximo globales, luego locales. Ambos extremos son puntos de acumulación de $I$: para cada radio $s>0$, los puntos $\frac12\min\{s,1\}$ y $1-\frac12\min\{s,1\}$ proporcionan testigos, respectivamente. La identidad tiene derivada $1$ en todo punto por Proposición §19.1.6 — Primeros cálculos: funciones afines y función cuadrática; su restricción conserva ese valor donde el dominio acumula por Proposición §19.5.2 — Restricción de una función derivable. Por tanto $u'(0)=u'(1)=1$. Ni $0$ ni $1$ son interiores a $I$, pues cualquier bola centrada en uno de ellos contiene puntos exteriores a $I$.

**Segunda afirmación.** Formemos por Separación en $\mathbb R\times\mathbb R$ la función $v:\mathbb R\to\mathbb R$ definida por $v(x)=x\cdot x\cdot x$. No introducimos una notación global de potencias generales. En $0$ se tiene $v(0)=0$ y, para $x\ne0$,

$$
q_{v,0}(x)=\frac{x\cdot x\cdot x}{x}=x\cdot x.
$$

Dado $\varepsilon>0$, tomemos $\delta:=\min\{1,\varepsilon\}>0$. Si $0<|x|<\delta$, entonces $|x\cdot x|=|x|^2<|x|<\varepsilon$. Dado que $0\in\operatorname{Acc}(\mathbb R)$, la definición de derivada permite concluir $v'(0)=0$. Para cada $r>0$, los puntos explícitos $x_-=-r/2$ y $x_+=r/2$ están a distancia estrictamente menor que $r$ de cero y satisfacen

$$
v(x_-)<v(0)=0<v(x_+),
$$

por las reglas de signo del cuerpo ordenado. Ningún radio puede entonces justificar un máximo o mínimo local en $0$. Así, $f'(a)=0$ es necesaria bajo las hipótesis de Fermat, pero no suficiente por sí sola. $\square$

**Transición.** El teorema de Weierstrass asegura la existencia de máximos y mínimos para funciones continuas en un compacto. Fermat convierte un extremo *interior* y derivable en un punto de derivada nula. Para obtener Rolle en §20.2 habrá que combinar ambas piezas y atender separadamente la posibilidad de que los extremos globales estén en los bordes del intervalo. La presente sección está cerrada como unidad humana; el capítulo completo sigue abierto. No se abre un nuevo checkpoint Lean.

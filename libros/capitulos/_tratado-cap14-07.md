## 14.7. Condensación de Cauchy {#sec-ta-14-7}

Comparar términos uno a uno no siempre revela por qué una serie converge. En una sucesión decreciente y no negativa podemos reunir cantidades cada vez mayores de términos sin perder el control de sus valores: dentro de un bloque, todos quedan comprendidos entre sus extremos. Si duplicamos sucesivamente la longitud del bloque, obtenemos una nueva serie que retiene exactamente la información necesaria para decidir la convergencia.

La fórmula usual del criterio presenta términos $2^k a_{2^k}$. Aquí debemos atender a los **tipos**: un subíndice pertenece a $\mathbb N$, mientras que el factor multiplicativo pertenece a $\mathbb R$. La potencia natural de base real ya fue construida en §14.3, pero todavía no hemos definido una operación general de potenciación en $\mathbb N$. Construiremos por recursión los índices diádicos y aplicaremos a ellos la función de numerales reales. Así, el símbolo informal $2^k$ no ocultará una coerción inexistente.

### Definición 14.7.1 — Índices diádicos y sucesión condensada

Definimos la sucesión de **índices diádicos** $d:\mathbb N\to\mathbb N$ como la única función que satisface

$$
\boxed{d_0=1,\qquad d_{k+1}=d_k+d_k\quad(k\in\mathbb N).}
$$

Su existencia y unicidad se siguen del teorema de recursión Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$, aplicado a $X=\mathbb N$, al elemento inicial $1$ y a la función $g(m)=m+m$. Esta última es una función total de $\mathbb N$ en sí mismo; su grafo es un subconjunto definible de $\mathbb N\times\mathbb N$. En particular, $d_0=1$, $d_1=2$, $d_2=4$, $d_3=8$, donde estas cifras son **naturales**, no elementos identificados literalmente con los reales.

Para cada sucesión real $a:\mathbb N\to\mathbb R$ definimos su **sucesión condensada** $\operatorname{Cond}(a)=b:\mathbb N\to\mathbb R$ mediante

$$
\boxed{b_k:=\nu_{\mathbb R}(d_k)\,a_{d_k}\qquad(k\in\mathbb N).}
$$

La aplicación de numerales $\nu_{\mathbb R}:\mathbb N\to\mathbb R$ y la multiplicación real están disponibles. El grafo de $b$ se obtiene por Separación dentro de $\mathbb N\times\mathbb R$, imponiendo para cada $k$ el valor único indicado. Esto construye una sola función completa, sin elecciones de términos. La **serie condensada** es la serie numérica de términos $b$ en el sentido de §14.1; no afirmamos todavía que converja.

> **Control de tipos.** $d_k$ es un índice natural; $\nu_{\mathbb R}(d_k)$ es su numeral real. La expresión usual $2^k a_{2^k}$ abrevia aquí $\nu_{\mathbb R}(d_k)a_{d_k}$, una vez verificada la relación de $d_k$ con las potencias reales de dos. No se declara una inclusión literal $\mathbb N\subseteq\mathbb R$.

### Proposición 14.7.2 — Crecimiento y aritmética de los índices diádicos

Para todo $k\in\mathbb N$ se verifican las siguientes propiedades:

$$
\boxed{1\le d_k,\qquad k+1\le d_k,\qquad d_k<d_{k+1},\qquad
\nu_{\mathbb R}(d_k)=(1+1)^k.}
$$

En la última igualdad, $1+1$ y su potencia son **reales**. En particular, $d_k$ crece sin quedar confinado a ningún segmento inicial de $\mathbb N$: dado $N\in\mathbb N$, el índice $d_{N+1}$ es mayor que $N$.

**Demostración.**

Probemos por inducción que $k+1\le d_k$. Para $k=0$ la igualdad $d_0=1$ lo establece. Supongamos $k+1\le d_k$. En particular $1\le d_k$; la compatibilidad del orden natural con la adición da

$$
(k+1)+1\le d_k+1\le d_k+d_k=d_{k+1}.
$$

El miembro izquierdo es el sucesor de $k+1$. Queda demostrado $(k+1)+1\le d_{k+1}$ y, con ello, la inducción. Se obtiene simultáneamente $1\le d_k$ para todo $k$. El incremento positivo $d_k<d_k+1\le d_{k+1}$ prueba el crecimiento estricto, usando las propiedades naturales de orden ya cerradas.

Apliquemos ahora la compatibilidad de los numerales con la suma (Proposición 4.1.6 — Aritmética y orden de los numerales naturales):

$$
\nu_{\mathbb R}(d_0)=1,\qquad
\nu_{\mathbb R}(d_{k+1})
=\nu_{\mathbb R}(d_k)+\nu_{\mathbb R}(d_k)
=\nu_{\mathbb R}(d_k)(1+1).
$$

Estas son exactamente las ecuaciones recursivas que definen, por Definición 14.3.1 — Potencias naturales de un número real, las potencias reales $(1+1)^k$. La unicidad por inducción da $\nu_{\mathbb R}(d_k)=(1+1)^k$ para cada $k$. Por último, tomando $k=N+1$ en la cota ya probada, $d_{N+1}\ge N+2>N$. ∎

> **Interpretación.** Ahora podemos leer legítimamente $b_k$ como el término convencional $2^k a_{2^k}$, con el subíndice $2^k$ entendido como el natural $d_k$ y el coeficiente como su numeral real. La estricta monotonía impide repetir bloques; la desigualdad $d_k\ge k+1$ garantiza que sus extremos llegan arbitrariamente lejos.

### Lema 14.7.3 — Cotas bilaterales de un bloque diádico

Sea $a:\mathbb N\to\mathbb R$ una sucesión **no negativa y decreciente en sentido no estricto**:

$$
\forall n\in\mathbb N\quad a_n\ge0,
\qquad
\forall m,n\in\mathbb N\quad(m\le n\Longrightarrow a_n\le a_m).
$$

Escribamos $s=\operatorname{PS}(a)$ y $b=\operatorname{Cond}(a)$. Para cada $k$ llamemos $T_k$ a la suma del bloque de índices estrictamente posteriores a $d_k$ y no posteriores a $d_{k+1}$:

$$
T_k:=\sum_{j=d_k+1}^{d_{k+1}}a_j
=s_{d_{k+1}}-s_{d_k}.
$$

La expresión de bloque es lícita porque $d_k<d_{k+1}$. Se cumple

$$
\boxed{0\le\frac12\,b_{k+1}\le T_k\le b_k
\qquad(k\in\mathbb N),}
$$

donde $\frac12$ es el inverso real de $1+1$.

**Demostración.**

Fijemos $k$. Tenemos $d_{k+1}=d_k+d_k$ y $d_k\ne0$ por Proposición 14.7.2 — Crecimiento y aritmética de los índices diádicos. Para cualquier índice $j$ del bloque,

$$
d_k<j\le d_{k+1}
\quad\Longrightarrow\quad
0\le a_{d_{k+1}}\le a_j\le a_{d_k},
$$

por la monotonía decreciente. El bloque posee precisamente $d_k$ términos, en el sentido de que su extremo superior es $d_k+d_k$ y comienza después de $d_k$; no se presupone ninguna noción informal de suma infinita.

Aplicando la cota inferior para bloques Lema 14.2.6 — Cota inferior para un bloque de términos acotados inferiormente, con $n=d_k$, $d=d_k$ y $c=a_{d_{k+1}}$, obtenemos

$$
T_k\ge\nu_{\mathbb R}(d_k)\,a_{d_{k+1}}.
$$

Para la cota superior consideremos la sucesión real $-a$, bien definida por operaciones puntuales. La desigualdad $a_j\le a_{d_k}$ equivale a $-a_j\ge-a_{d_k}$. El mismo lema aplicado al bloque correspondiente de $-a$ da

$$
\sum_{j=d_k+1}^{d_{k+1}}(-a_j)
\ge-\nu_{\mathbb R}(d_k)a_{d_k}.
$$

La identidad de sumas parciales bajo multiplicación por $-1$, válida incluso para este escalar por Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo, y la definición del bloque convierten el miembro izquierdo en $-T_k$. Cambiando de signo resulta

$$
T_k\le\nu_{\mathbb R}(d_k)a_{d_k}=b_k.
$$

La aritmética de numerales demuestra

$$
\nu_{\mathbb R}(d_{k+1})
=\nu_{\mathbb R}(d_k)+\nu_{\mathbb R}(d_k)
=(1+1)\nu_{\mathbb R}(d_k).
$$

Como $1+1$ es un real estrictamente positivo, multiplicar por su inverso proporciona

$$
\nu_{\mathbb R}(d_k)a_{d_{k+1}}
=\frac12\nu_{\mathbb R}(d_{k+1})a_{d_{k+1}}
=\frac12\,b_{k+1}.
$$

Ésta es la cota inferior anunciada. Su no negatividad procede de $b_{k+1}\ge0$ y $\frac12>0$. ∎

> **Pregunta de lectura.** ¿Por qué los extremos de la estimación llevan índices distintos? Dentro del bloque, el término mayor está cerca de su comienzo y el menor en su extremo final; por eso la cota superior utiliza $a_{d_k}$ y la inferior utiliza $a_{d_{k+1}}$. El desplazamiento de un índice en $b_{k+1}$ será esencial al sumar las desigualdades.

### Proposición 14.7.4 — Telescopía y comparación de los bloques

Bajo las hipótesis del lema anterior, sean $s=\operatorname{PS}(a)$ y $B=\operatorname{PS}(b)$; denotemos por $T=(T_k)_{k\in\mathbb N}$ la sucesión de sumas de bloques. Para cada $m\in\mathbb N$,

$$
\boxed{\sum_{k=0}^{m}T_k=s_{d_{m+1}}-s_1,}
$$

$$
\boxed{B_{m+1}=b_0+\sum_{k=0}^{m}b_{k+1},}
$$

y, en consecuencia,

$$
\boxed{
\frac12\bigl(B_{m+1}-b_0\bigr)
\le s_{d_{m+1}}-s_1\le B_m.
}
$$

**Demostración.**

La sucesión $T$ está bien definida: para cada $k$, sus extremos naturales satisfacen $d_k<d_{k+1}$ y, por consiguiente, $T_k=s_{d_{k+1}}-s_{d_k}$ es un real único. Su grafo se forma por Separación en $\mathbb N\times\mathbb R$. De igual modo, $(b_{k+1})_{k\in\mathbb N}$ es una sucesión real total, obtenida componiendo $b$ con la función sucesor. Son, por tanto, legítimas ambas sumas finitas que aparecen en el enunciado.

Para la primera identidad, en $m=0$ tenemos $T_0=s_{d_1}-s_{d_0}=s_{d_1}-s_1$, pues $d_0=1$. Supongamos

$$
\sum_{k=0}^{m}T_k=s_{d_{m+1}}-s_1.
$$

La prolongación de la suma finita y la identidad del bloque siguiente dan

$$
\begin{aligned}
\sum_{k=0}^{m+1}T_k
&=\sum_{k=0}^{m}T_k+T_{m+1}\\
&=(s_{d_{m+1}}-s_1)
  +(s_{d_{m+2}}-s_{d_{m+1}})\\
&=s_{d_{m+2}}-s_1.
\end{aligned}
$$

La segunda identidad se demuestra también por inducción: para $m=0$, $B_1=b_0+b_1$; si $B_{m+1}=b_0+\sum_{k=0}^{m}b_{k+1}$, entonces

$$
\begin{aligned}
B_{m+2}&=B_{m+1}+b_{m+2}\\
&=b_0+\sum_{k=0}^{m}b_{k+1}+b_{m+2}\\
&=b_0+\sum_{k=0}^{m+1}b_{k+1}.
\end{aligned}
$$

Finalmente, el lema precedente establece para **cada** $k$ que $\frac12b_{k+1}\le T_k\le b_k$. La comparación de sumas finitas Proposición 14.5.1 — Comparación de sumas finitas y de bloques, junto con la identidad finita de escalamiento Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo, entrega

$$
\frac12\sum_{k=0}^{m}b_{k+1}
\le\sum_{k=0}^{m}T_k
\le\sum_{k=0}^{m}b_k=B_m.
$$

Sustituyendo las dos identidades recién probadas obtenemos exactamente la estimación final. ∎

> **Qué se ha hecho.** No hemos reordenado una serie infinita ni intercambiado límites: hemos sumado un número finito de bloques consecutivos y cancelado las sumas parciales intermedias. La serie de bloques $T$ es distinta de la serie condensada $b$, y el desplazamiento $b_{k+1}$ no se elimina sin compensarlo mediante el término inicial $b_0$.

### Teorema 14.7.5 — Criterio de condensación de Cauchy

Sea $a:\mathbb N\to\mathbb R$ una sucesión tal que, para todos los naturales $n\le m$,

$$
\boxed{0\le a_m\le a_n.}
$$

Sea $d$ la sucesión de índices diádicos y definamos $b_k=\nu_{\mathbb R}(d_k)a_{d_k}$. Entonces

$$
\boxed{
\sum_{n=0}^{\infty}a_n\text{ converge en }\mathbb R
\quad\Longleftrightarrow\quad
\sum_{k=0}^{\infty}b_k\text{ converge en }\mathbb R.
}
$$

Equivalente en la notación tradicional: una serie de términos no negativos y decrecientes converge si y sólo si converge su condensada $\sum_{k=0}^{\infty}2^k a_{2^k}$, interpretada con los tipos precisados arriba. Ambas series divergen simultáneamente cuando se incumple la condición equivalente.

**Demostración.**

Escribamos $s=\operatorname{PS}(a)$ y $B=\operatorname{PS}(b)$. La hipótesis proporciona $a_n\ge0$; asimismo $b_k\ge0$ porque $\nu_{\mathbb R}(d_k)>0$. Ambos criterios de convergencia se reducen, por Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos, a la existencia de una cota superior para las respectivas sucesiones de sumas parciales. Por Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa, $s$ es creciente. Disponemos además, para todo $m$, de

$$
\boxed{
\frac12(B_{m+1}-b_0)
\le s_{d_{m+1}}-s_1\le B_m.
}
\tag{14.7.1}
$$

**Primera implicación: convergencia de la condensada $\Rightarrow$ convergencia de la original.** Supongamos que la serie de $b$ converge. Existe un real $K$ tal que $B_m\le K$ para todo $m$, por Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos. De la cota derecha de (14.7.1) resulta

$$
s_{d_{m+1}}\le s_1+K
\qquad(m\in\mathbb N).
$$

Debemos acotar **todas** las sumas parciales $s_n$, no sólo las de subíndices diádicos. Fijado cualquier $n\in\mathbb N$, tomemos el índice explícito $m=n$. La proposición 14.7.2 establece $n\le d_{n+1}$. Como $s$ es creciente,

$$
\boxed{s_n\le s_{d_{n+1}}\le s_1+K.}
$$

Por tanto $s$ está acotada superiormente y el criterio de §14.4 demuestra la convergencia de la serie original.

**Segunda implicación: convergencia de la original $\Rightarrow$ convergencia de la condensada.** Supongamos que converge la serie de $a$. Existe un real $M$ con $s_n\le M$ para todos los índices. En particular, $s_1\le M$. De la cota izquierda de (14.7.1),

$$
\frac12(B_{m+1}-b_0)
\le s_{d_{m+1}}-s_1
\le M-s_1.
$$

Multiplicamos por el real positivo $1+1$ y obtenemos

$$
\boxed{B_{m+1}\le b_0+(1+1)(M-s_1)
\qquad(m\in\mathbb N).}
$$

La misma constante acota $B_0=b_0$, pues $M-s_1\ge0$. Por tanto acota **todas** las sumas parciales de la condensada: todo natural es $0$ o el sucesor de otro. El criterio para series no negativas demuestra su convergencia.

Las dos implicaciones establecen la equivalencia. Puesto que divergencia significa ausencia de convergencia real, también comparten la divergencia. ∎

### Corolario 14.7.6 — Nueva demostración de la divergencia armónica

La serie armónica del §14.2, cuyos términos son

$$
h_n:=\nu_{\mathbb R}(n+1)^{-1},
$$

es divergente. Su divergencia se deduce también del criterio de condensación, de manera independiente de la prueba por bloques dada en §14.2.

**Demostración.**

Los numerales $\nu_{\mathbb R}(n+1)$ son positivos y crecen con $n$; invertirlos invierte el orden. Por tanto $h_n>0$ y $h$ es decreciente. Su condensada tiene términos

$$
b_k=\nu_{\mathbb R}(d_k)\,h_{d_k}
=\frac{\nu_{\mathbb R}(d_k)}{\nu_{\mathbb R}(d_k+1)}.
$$

Como $d_k\ge1$, la compatibilidad de la suma con los numerales da

$$
0<\nu_{\mathbb R}(d_k+1)
=\nu_{\mathbb R}(d_k)+1
\le(1+1)\nu_{\mathbb R}(d_k).
$$

Al dividir por el producto positivo correspondiente, obtenemos

$$
\boxed{b_k\ge\frac12>0\qquad(k\in\mathbb N).}
$$

Por la definición de límite, una sucesión cuyos términos están todos por encima de $1/2$ no converge a cero: la tolerancia $\varepsilon=1/2$ contradice cualquier umbral de convergencia. El criterio de divergencia por el término general Corolario 14.2.5 — Criterio de divergencia por el término general muestra que la serie condensada diverge. Por Teorema 14.7.5 — Criterio de condensación de Cauchy, la serie armónica original también diverge. ∎

> **Dos demostraciones, una misma conclusión.** La prueba de §14.2 construía bloques de suma uniformemente grande y violaba el criterio de Cauchy. La condensación reúne esos bloques en una nueva sucesión, cuyos términos ni siquiera tienden a cero. La segunda demostración no reutiliza la *conclusión* de divergencia de Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica.

### Proposición 14.7.7 — La monotonía es una hipótesis esencial

Existen sucesiones de términos no negativos para las que la serie condensada converge y la original diverge. En consecuencia, la hipótesis de monotonía no puede suprimirse del teorema 14.7.5.

**Demostración.**

Definamos el conjunto de índices

$$
E:=\{n\in\mathbb N:\exists k\in\mathbb N\,
(k\ge1\ \text{y}\ n=d_k+1)\}.
$$

Existe por Separación de $\mathbb N$. Definamos la sucesión real $c$ por $c_n=1$ si $n\in E$ y $c_n=0$ en caso contrario. Su grafo es un subconjunto funcional y total de $\mathbb N\times\mathbb R$, obtenido por Separación; la dicotomía de pertenencia es lógica clásica y no es un test efectivo afirmado.

**Ningún índice diádico pertenece a $E$.** Fijemos $k\ge1$. Por la proposición 14.7.2, $d_k\ge k+1\ge2$. Si $j\le k$, el crecimiento de $d$ implica $d_j\le d_k<d_k+1$. Si $j\ge k+1$, el mismo crecimiento da

$$
d_j\ge d_{k+1}=d_k+d_k>d_k+1,
$$

ya que $d_k\ge2$. Por tanto $d_k+1\ne d_j$ para cualquier $j\in\mathbb N$. Se sigue que $E$ no contiene ningún $d_j$: el caso de $d_0=1$ también queda excluido, pues cada elemento de $E$ vale al menos $d_1+1\ge3$. Así, $c_{d_j}=0$ para todo $j$, y su condensada satisface

$$
\operatorname{Cond}(c)_j=\nu_{\mathbb R}(d_j)c_{d_j}=0.
$$

Esta serie condensada converge, pues sus sumas parciales son constantemente cero (Proposición 14.1.6 — Estabilización de sumas parciales cuando los términos tardíos son nulos).

**La serie original diverge.** Para cada $k\ge1$, el índice $d_k+1$ pertenece a $E$ y $c_{d_k+1}=1$. Esos índices superan cualquier umbral natural: dado $N$, el índice explícito $k=N+1$ satisface $d_k+1\ge k+2>N$. En consecuencia, para la tolerancia $\varepsilon=1/2$, después de cualquier supuesto umbral de convergencia a cero aparece un término $c_{d_k+1}=1$ cuyo valor absoluto no es menor que $\varepsilon$. Por tanto $c_n\not\to0$; el criterio Corolario 14.2.5 — Criterio de divergencia por el término general fuerza la divergencia de su serie. Además $c$ no es decreciente, pues $c_{d_1}=0<1=c_{d_1+1}$. ∎

> **Alcance exacto.** La condensación no es un muestreo válido para cualquier sucesión no negativa. Sin monotonía se pueden ocultar términos grandes entre los índices diádicos: la condensada ve ceros, mientras que la serie original conserva infinitos términos de valor uno. La conclusión del criterio se aplica exclusivamente bajo sus hipótesis.

Los bloques diádicos transforman un problema de suma infinita en dos familias de desigualdades finitas, y la completitud decide después la convergencia. Para avanzar convendrá distinguir otra forma de estabilidad: si los términos de una serie pueden cambiar de signo, la convergencia de sus valores absolutos ofrece un control que la mera convergencia no proporciona. Éste será el tema de §14.8, **convergencia absoluta y condicional**.

## 14.10. Reordenamientos y estabilidad de la suma bajo convergencia absoluta {#sec-ta-14-10}

La suma finita de números reales es conmutativa. En cambio, una serie no se define como la suma de un conjunto de términos: se define como el límite de una sucesión de sumas **en un orden fijado**. Un cambio de orden produce, en principio, una nueva sucesión de sumas parciales. ¿Cuándo podemos garantizar que tiene el mismo límite?

La convergencia absoluta proporciona la respuesta. Su condición cuantifica el tamaño total de las colas, de modo que cualquier colección finita de términos tardíos puede ser controlada aunque sus índices se presenten en otro orden. El argumento exigirá primero justificar una identidad **finita** para índices distintos; sólo después tomaremos límites.

### Definición 14.10.1 — Permutación de índices y serie reordenada

Una **permutación de los índices naturales** es una biyección

$$
\pi:\mathbb N\longrightarrow\mathbb N.
$$

Dada una sucesión real $a$, su **sucesión reordenada** es la composición $a\circ\pi$, cuyos términos son

$$
\boxed{b_j:=a_{\pi(j)}\qquad(j\in\mathbb N).}
\tag{14.10.1}
$$

La **serie reordenada** es la serie de términos $b$; sus sumas parciales son

$$
t_m:=\operatorname{PS}(b)_m=\sum_{j=0}^{m}a_{\pi(j)}.
$$

La composición de funciones ya construida hace existir $b$ como elemento de $\mathbb R^{\mathbb N}$. La biyección garantiza que cada término de la sucesión original aparece exactamente una vez, pero **no** garantiza por definición ni la convergencia ni la igualdad de las sumas. Una agrupación de términos consecutivos es una operación distinta: no se definirá aquí como si fuera una permutación.

### Lema 14.10.2 — Identidad de suma finita sobre índices distintos

Sean $m,K\in\mathbb N$ y sea $f:\mathbb N\to\mathbb N$ una función cuyos valores $f(0),\ldots,f(m)$ son **distintos dos a dos** y satisfacen $f(j)\le K$ para $0\le j\le m$. Para cualquier sucesión real $a$ definamos

$$
c_k:=\begin{cases}
a_k,&\text{si existe }j\le m\text{ con }f(j)=k,\\
0,&\text{en caso contrario.}
\end{cases}
$$

Entonces

$$
\boxed{\sum_{j=0}^{m}a_{f(j)}=\sum_{k=0}^{K}c_k.}
\tag{14.10.2}
$$

En particular, se obtiene la estimación

$$
\boxed{\sum_{j=0}^{m}|a_{f(j)}|\le\sum_{k=0}^{K}|a_k|.}
\tag{14.10.3}
$$

**Demostración.**

Comencemos por dos hechos sobre sumas finitas que derivaremos de su recursión. Si $v_k=0$ para todos los $k$ entre $P+1$ y $K$, con $P\le K$, la inducción sobre $K-P$ da $\sum_{k=0}^{K}v_k=\sum_{k=0}^{P}v_k$. Además, si dos sucesiones $v,w$ sólo difieren en un índice $r\le K$, entonces

$$
\sum_{k=0}^{K}w_k-\sum_{k=0}^{K}v_k=w_r-v_r.
\tag{14.10.4}
$$

Para comprobar esta última identidad, una inducción sobre el extremo superior $K$ distingue $K<r$, cuando las sumas coinciden; $K=r$, cuando se incorpora exactamente la diferencia indicada; y $K>r$, cuando se agrega a ambas sumas el mismo término. El caso $K<r$ comienza en $K=0$ con las ecuaciones iniciales; alternativamente puede probarse por inducción directa a partir del índice $0$. Todo ello es aritmética finita del grupo aditivo real.

Demostremos (14.10.2) por inducción sobre la longitud $m+1$ de la lista, para **todos** los $K$ que acoten sus índices. En $m=0$, la sucesión $c$ es nula salvo en $r=f(0)$. Aplicando (14.10.4) a la sucesión nula, cuya suma finita es cero por inducción, obtenemos $\sum_{k=0}^{K}c_k=a_r$, como se requiere.

Supongamos la identidad para $f(0),\ldots,f(m)$ y consideremos un índice adicional $r=f(m+1)$ distinto de todos ellos. Sea $c'$ la sucesión auxiliar correspondiente a los primeros $m+1$ índices, sin incluir $r$, y sea $c$ la correspondiente a la lista ampliada. Por inyectividad, $c'$ y $c$ sólo difieren en $r$: allí sus valores son $0$ y $a_r$. La identidad (14.10.4) proporciona

$$
\sum_{k=0}^{K}c_k
=\sum_{k=0}^{K}c'_k+a_r
=\sum_{j=0}^{m}a_{f(j)}+a_{f(m+1)}
=\sum_{j=0}^{m+1}a_{f(j)}.
$$

Las sucesiones auxiliares existen por Separación en $\mathbb N\times\mathbb R$: cada condición de pertenencia es una fórmula sobre el **conjunto finito** de índices $j\le m$, y el valor asignado es único. No hemos elegido un orden de un conjunto arbitrario ni invocado conmutatividad infinita.

Finalmente, repitamos (14.10.2) con los pesos $|a_k|$. La sucesión auxiliar correspondiente satisface $0\le c_k\le|a_k|$ para todo $k$. La comparación finita Proposición 14.5.1 — Comparación de sumas finitas y de bloques implica $\sum_{k=0}^{K}c_k\le\sum_{k=0}^{K}|a_k|$, que, mediante (14.10.2), es (14.10.3). ∎

> **Punto lógico.** La desigualdad (14.10.3) no afirma que los índices elegidos sean consecutivos. Cada índice aparece como máximo una vez, y los pesos son no negativos. Ambas condiciones intervienen en la demostración.

### Lema 14.10.3 — Captura de un prefijo y cota de la cola reordenada

Sean $a$ una sucesión real, $\pi$ una permutación y $s,t,u$ las sumas parciales, respectivamente, de $a$, $a\circ\pi$ y $\operatorname{Abs}(a)$. Fijado $N\in\mathbb N$, existe $M\in\mathbb N$ tal que para todo $m\ge M$ existe $K\ge N$ con

$$
\boxed{|t_m-s_N|\le u_K-u_N.}
\tag{14.10.5}
$$

Además, podemos tomar $K\ge\pi(j)$ para todos los $j\le m$, y vale $u_K-u_N\ge0$.

**Demostración.**

Por ser biyectiva, $\pi$ tiene inversa funcional Teorema 0.6.7 — Caracterización de las funciones invertibles. Para cada $k\le N$ hay, por tanto, un índice **único** $j_k=\pi^{-1}(k)$. Construimos un límite común $M$ por recursión finita: $M_0=j_0$ y $M_{k+1}$ es el mayor de $M_k$ y $j_{k+1}$, donde el mayor existe y es único por el orden total de $\mathbb N$. Ponemos $M=M_N$. Una inducción muestra que $j_k\le M$ para cada $k\le N$; no se ha escogido simultáneamente ningún testigo no canónico.

Fijemos $m\ge M$. Los índices $\pi(0),\ldots,\pi(m)$ contienen, pues, **todos** los naturales $0,\ldots,N$. Construyamos de la misma manera un máximo finito $K$ de $N,\pi(0),\ldots,\pi(m)$. Definamos $c_k=a_k$ si $k$ está entre esos valores de $\pi$, y $c_k=0$ en otro caso. El lema anterior, aplicado a la lista inyectiva $f(j)=\pi(j)$, da

$$
t_m=\sum_{k=0}^{K}c_k,
\qquad c_k=a_k\quad(0\le k\le N).
$$

Si $K=N$, ambas sumas finitas coinciden y $t_m=s_N$; la cota (14.10.5) es $0\le0$. Si $K>N$, la partición finita Proposición 14.2.2 — Identidades de los bloques de sumación y la desigualdad triangular de bloques Lema 14.8.2 — Desigualdad triangular para sumas finitas y bloques, aplicadas a $c$, dan

$$
|t_m-s_N|
=\left|\sum_{k=N+1}^{K}c_k\right|
\le\sum_{k=N+1}^{K}|c_k|
\le\sum_{k=N+1}^{K}|a_k|
=u_K-u_N.
$$

La penúltima desigualdad usa $|c_k|\le|a_k|$ y la comparación finita de bloques; la última igualdad es la definición de bloque de las magnitudes. La monotonía de $u$ proporciona $u_K-u_N\ge0$. Todos los pasos anteriores son finitos. ∎

> **Interpretación.** Después de cierto lugar de la nueva lista, ya han aparecido *todos* los términos del prefijo original que queríamos conservar. Lo que se añade o se omite hasta un extremo finito $K$ sólo puede proceder de la cola posterior a $N$.

### Teorema 14.10.4 — Invariancia de la suma bajo reordenamientos absolutamente convergentes

Si $a\in\mathcal A_{\mathrm{ser}}$ y $\pi:\mathbb N\to\mathbb N$ es una biyección, entonces $a\circ\pi\in\mathcal A_{\mathrm{ser}}$, y las sumas ordinaria y absoluta se conservan:

$$
\boxed{
\sum_{j=0}^{\infty}a_{\pi(j)}
=\sum_{k=0}^{\infty}a_k,
\qquad
\sum_{j=0}^{\infty}|a_{\pi(j)}|
=\sum_{k=0}^{\infty}|a_k|.
}
\tag{14.10.6}
$$

Las igualdades son numéricas porque **las cuatro series que aparecen convergen**.

**Demostración.**

Escribamos

$$
s_n:=\sum_{k=0}^{n}a_k,
\quad u_n:=\sum_{k=0}^{n}|a_k|,
\quad t_m:=\sum_{j=0}^{m}a_{\pi(j)}.
$$

Por convergencia absoluta y Teorema 14.8.3 — La convergencia absoluta implica convergencia ordinaria, existen números reales $S,A$ tales que $s_n\to S$ y $u_n\to A$. Puesto que $u$ es creciente, $u_n\le A$ para todo $n$: si algún $u_n>A$, la monotonía impediría que su límite fuese $A$ (también se deduce de la conservación del orden bajo límites). Por tanto

$$
0\le u_K-u_N\le A-u_N\qquad(K\ge N).
\tag{14.10.7}
$$

Sea $\varepsilon>0$. La convergencia de ambas sucesiones da un índice común $N$ suficientemente grande para que

$$
|s_N-S|<\varepsilon/2,
\qquad 0\le A-u_N<\varepsilon/2.
$$

El índice común se obtiene tomando el mayor de los dos umbrales naturales; no se construye una función de elección para todas las tolerancias. El lema Lema 14.10.3 — Captura de un prefijo y cota de la cola reordenada entrega $M$ tal que, para todo $m\ge M$, hay $K\ge N$ con $|t_m-s_N|\le u_K-u_N$. En consecuencia,

$$
|t_m-S|
\le |t_m-s_N|+|s_N-S|
\le A-u_N+|s_N-S|<\varepsilon.
$$

Esto prueba directamente $t_m\to S$. En particular, la serie reordenada converge y tiene suma $S$.

Repetimos **el argumento ya demostrado** con la sucesión de términos $x_k:=|a_k|$. La serie de $x$ converge a $A$, y su serie de magnitudes es la misma, pues $||a_k||=|a_k|$. La misma estimación, ahora con $x$, muestra que las sumas parciales de $x\circ\pi$ convergen a $A$. Pero $x_{\pi(j)}=|a_{\pi(j)}|$ para todo $j$, de modo que se obtiene la segunda igualdad y, por definición, la convergencia absoluta de la serie reordenada. No se ha intercambiado ningún límite con una suma infinita ni se ha supuesto que la conmutatividad finita bastaba por sí sola. ∎

> **Lectura estructural.** La absoluta convergencia garantiza una cota para la *masa completa* de cualquier cola. La biyección sólo asegura que cada prefijo finito acaba apareciendo. Al combinar ambos hechos, el nuevo orden se vuelve irrelevante para el límite.

### Proposición 14.10.5 — Una permutación de soporte finito preserva cualquier suma convergente

Sea $\pi$ una permutación para la que existe $N$ con $\pi(n)=n$ para todo $n\ge N$. Entonces, para cualquier serie convergente $\sum a_n$, la serie $\sum a_{\pi(n)}$ converge y tiene **la misma suma**, aunque no se presuponga convergencia absoluta.

**Demostración.**

Aumentemos $N$, si hace falta, para que sea al menos $1$. La biyección lleva el conjunto $\{0,\ldots,N\}$ sobre sí mismo. En efecto, si $j\le N$ y $\pi(j)>N$, el índice $\pi(j)$ está fijo y tendría dos preimágenes distintas, $j$ y $\pi(j)$, contradiciendo la inyectividad; así la imagen está contenida en el prefijo. Recíprocamente, para $k\le N$ su preimagen no puede exceder $N$, pues todo índice superior está fijo y no puede tener imagen $k$. Por tanto la imagen coincide con el prefijo.

El lema de suma finita Lema 14.10.2 — Identidad de suma finita sobre índices distintos, aplicado a la lista $\pi(0),\ldots,\pi(N)$ con $K=N$, da $t_N=s_N$. Como $\pi(n)=n$ para todo $n>N$, las recurrencias de sumas parciales permiten concluir por inducción que $t_m=s_m$ para cada $m\ge N$. Ambas sucesiones tienen, por ello, el mismo límite. ∎

> **Contraste.** Cambiar sólo un número finito de posiciones no modifica el valor de una serie convergente. Lo que exige absoluta convergencia en el teorema anterior es la garantía para **toda** permutación, incluidas las que siguen alterando el orden a índices arbitrariamente grandes.

### Proposición 14.10.6 — Una serie condicional puede cambiar de suma por reordenamiento

Existe una serie condicionalmente convergente cuya suma original es $0$ y una permutación de sus índices cuya serie reordenada converge a un número **estrictamente positivo**. No afirmamos aquí el teorema general que permite prescribir una suma arbitraria a toda serie condicional: basta un contraejemplo explícito para delimitar el teorema anterior.

**Demostración.**

Recuperemos la sucesión positiva $h_k:=\nu_{\mathbb R}(k+1)^{-1}$ de §14.2 y la serie por parejas de Teorema 14.8.6 — Existe una serie condicionalmente convergente:

$$
a_{2k}=h_k,\qquad a_{2k+1}=-h_k.
$$

Ya está demostrado que $\sum a_n=0$ y que $\sum|a_n|$ diverge. Definamos otra enumeración de sus índices:

$$
\boxed{
\pi(3k)=4k,\qquad
\pi(3k+1)=4k+2,\qquad
\pi(3k+2)=2k+1.}
\tag{14.10.8}
$$

Todos los coeficientes e índices de estas tres expresiones son **naturales**. Verifiquemos que (14.10.8) define una biyección, en lugar de suponerlo por su aspecto. Una inducción, que pasa sucesivamente de los residuos $0$ a $1$, de $1$ a $2$ y de $2$ al siguiente múltiplo de $3$, muestra que todo natural es $3k$, $3k+1$ o $3k+2$. La representación es única: si $3k+r=3\ell+s$ con $r,s\in\{0,1,2\}$ y $k<\ell$, entonces $3k+r\le3k+2<3(k+1)\le3\ell\le3\ell+s$, contradicción; el caso simétrico excluye $\ell<k$, y la cancelación da $r=s$. Los tres valores de (14.10.8) pertenecen respectivamente a los índices pares de la forma $4k$, a los pares de la forma $4k+2$ y a los impares. Esas familias son disjuntas y cada una es inyectivamente parametrizada, según las leyes de orden y cancelación naturales. Todo natural impar es $2k+1$; todo par es $2j$, donde la dicotomía de paridad de $j$ escribe $j=2k$ o $j=2k+1$. Así, **cada natural aparece una vez y sólo una vez** como valor de $\pi$. Su grafo, definido por los tres casos exclusivos, existe por Separación en $\mathbb N\times\mathbb N$.

Sea $t_m=\sum_{j=0}^{m}a_{\pi(j)}$ y sea $H_k=\sum_{j=0}^{k}h_j$. Cada triple del nuevo orden contiene dos términos positivos y un término negativo:

$$
b_{3k}=h_{2k},\qquad
b_{3k+1}=h_{2k+1},\qquad
b_{3k+2}=-h_k.
$$

Por inducción sobre $k$ y por partición **finita** de sumas, obtenemos

$$
\boxed{t_{3k+2}=D_k:=H_{2k+1}-H_k
=\sum_{j=k+1}^{2k+1}h_j.}
\tag{14.10.9}
$$

Para $k=0$ los tres términos dan $h_0+h_1-h_0=h_1=H_1-H_0$. Si la identidad vale para $k$, agregar el triple siguiente suma $h_{2k+2}+h_{2k+3}-h_{k+1}$, exactamente la diferencia entre $H_{2k+3}-H_{k+1}$ y $H_{2k+1}-H_k$.

La sucesión $D$ es creciente, pues

$$
D_{k+1}-D_k=h_{2k+2}+h_{2k+3}-h_{k+1}
=\frac1{\nu_{\mathbb R}(2k+3)}-\frac1{\nu_{\mathbb R}(2k+4)}>0.
$$

También está acotada y separada de cero: en el bloque (14.10.9) hay $k+1$ términos, y sus denominadores están entre $k+2$ y $2k+2$. Las comparaciones finitas, con los numerales correctamente tipados, proporcionan

$$
\boxed{\frac12=\frac{\nu_{\mathbb R}(k+1)}{\nu_{\mathbb R}(2k+2)}
\le D_k\le\frac{\nu_{\mathbb R}(k+1)}{\nu_{\mathbb R}(k+2)}<1.}
\tag{14.10.10}
$$

La convergencia monótona Teorema 13.7.3 — Teorema de convergencia monótona garantiza $D_k\to B\in\mathbb R$; al pasar al límite en (14.10.10), $B\ge1/2>0$.

Resta comprobar que converge la sucesión **completa** $t$, no solamente $t_{3k+2}$. Las dos sumas parciales siguientes son

$$
t_{3k+3}=D_k+h_{2k+2},\qquad
t_{3k+4}=D_k+h_{2k+2}+h_{2k+3}.
$$

Como $h_n\to0$, ambos términos añadidos tienden a cero. Todo índice $n\ge2$ es de una de las formas $3k+2$, $3k+3$ o $3k+4$, por una inducción sobre $n$ que recorre cíclicamente esos tres casos; para $n\to\infty$ el correspondiente $k\to\infty$, ya que para cada $K$ los tres índices con $k<K$ son menores que $3K+2$. Dado $\varepsilon>0$, fijamos $K$ para que $|D_k-B|<\varepsilon/3$ y $h_{2k+2},h_{2k+3}<\varepsilon/3$ para todo $k\ge K$; las tres fórmulas muestran entonces $|t_n-B|<\varepsilon$ cuando $n\ge3K+2$. Por tanto la serie reordenada converge a $B>0$, mientras que la original suma $0$. ∎

> **Advertencia conceptual.** Este ejemplo no cambia ni duplica términos: cambia únicamente el orden de aparición. La hipótesis de convergencia absoluta en Teorema 14.10.4 — Invariancia de la suma bajo reordenamientos absolutamente convergentes no puede omitirse de una afirmación universal de invariancia. Eso no significa que *toda* permutación de *toda* serie condicional cambie su suma; las de soporte finito siguen sometidas a la proposición anterior.

La convergencia absoluta garantiza invariancia frente a permutaciones; la convergencia ordinaria, por sí sola, no. En §14.11 estudiaremos un mecanismo diferente de convergencia basado precisamente en la alternancia de signos y el decrecimiento de las magnitudes: el criterio de Leibniz y su estimación del resto.

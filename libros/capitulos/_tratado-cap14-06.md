## 14.6. Criterio de comparación por límite {#sec-ta-14-6}

La comparación directa exige desigualdades entre los términos de dos series. A menudo, sin embargo, las expresiones de sus términos son complicadas y resulta más accesible estudiar su **cociente**. Si éste se aproxima a un número real estrictamente positivo, podremos obtener dos desigualdades eventuales: cada sucesión de términos quedará acotada por un múltiplo positivo de la otra. Este paso, que convierte un límite en cotas útiles para sumas parciales, es el núcleo del criterio.

Hay tres precauciones previas. El cociente $a_n/b_n$ sólo existe cuando $b_n\ne0$; su límite, si se utiliza como número real, debe estar justificado; y la comparación de términos no equivale a una igualdad de las sumas. Separaremos estas cuestiones antes de formular el teorema.

### Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo

Sea $a:\mathbb N\to\mathbb R$ una sucesión y sea $c\in\mathbb R$. Denotemos por $ca$ la sucesión real definida término a término por $(ca)_n:=ca_n$. Entonces, para todo $n\in\mathbb N$,

$$
\boxed{\operatorname{PS}(ca)_n=c\,\operatorname{PS}(a)_n.}
$$

Si $c\ne0$, la serie de términos $ca$ converge **si y sólo si** converge la de términos $a$. En ese caso, ambas sumas están definidas y

$$
\boxed{\sum_{n=0}^{\infty}ca_n
=c\sum_{n=0}^{\infty}a_n.}
$$

**Demostración.**

La definición de operaciones puntuales Definición 13.1.3 — Operaciones puntuales sobre sucesiones reales garantiza que $ca$ es una sucesión real. Escribamos $s=\operatorname{PS}(a)$ y $u=\operatorname{PS}(ca)$. Demostraremos por inducción que $u_n=cs_n$ para todo $n$. En $n=0$ tenemos

$$
u_0=(ca)_0=ca_0=cs_0.
$$

Si $u_n=cs_n$, las ecuaciones recursivas y la distributividad del cuerpo real implican

$$
\begin{aligned}
u_{n+1}&=u_n+(ca)_{n+1}\\
&=cs_n+ca_{n+1}\\
&=c(s_n+a_{n+1})=cs_{n+1}.
\end{aligned}
$$

La identidad finita queda probada, incluso para $c=0$. Supongamos ahora que $c\ne0$. Si la serie de términos $a$ converge a la suma real $A$, entonces $s_n\to A$ y la compatibilidad del límite con la multiplicación por una constante (Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante) da

$$
u_n=cs_n\longrightarrow cA.
$$

Por la definición de suma de una serie y la unicidad del límite, la serie de términos $ca$ converge y su suma es $cA$. Recíprocamente, si la serie de términos $ca$ converge, aplicamos lo ya demostrado a esa serie y al escalar real $c^{-1}$, que existe porque $c\ne0$. Sus términos son $c^{-1}(ca_n)=a_n$, de modo que converge la serie original. La fórmula de las sumas se aplica cuando ambas convergencias están establecidas. ∎

> **Lectura del alcance.** Para $c=0$ sigue siendo correcta la identidad entre sumas parciales, y la serie de términos nulos converge; no es válida la equivalencia de convergencia: multiplicar por cero borra toda información sobre la serie inicial. Utilizaremos únicamente escalares estrictamente positivos al comparar términos no negativos, para conservar la dirección de las desigualdades.

---

### Definición 14.6.2 — Cociente secuencial totalizado y cociente eventual

Para dos sucesiones reales $a,b\in\mathbb R^{\mathbb N}$ definimos su **cociente totalizado** $\operatorname{quo}_0(a,b)\in\mathbb R^{\mathbb N}$, con valores

$$
\boxed{
\operatorname{quo}_0(a,b)_n:=
\begin{cases}
a_n b_n^{-1},& b_n\ne0,\\
0,&b_n=0.
\end{cases}}
$$

La segunda rama es una convención de definición y **no** una división por cero. El grafo se obtiene por Separación dentro de $\mathbb N\times\mathbb R$: para cada índice, la disyunción $b_n=0$ o $b_n\ne0$ determina un único valor real; en el segundo caso el inverso existe por las leyes del cuerpo. No se escoge una sucesión de cocientes mediante Choice: queda definida de forma unívoca. No se afirma que la prueba clásica de igualdad con cero sea un procedimiento efectivo uniforme.

Si existe $N_0\in\mathbb N$ tal que $b_n>0$ para todo $n\ge N_0$, entonces

$$
\operatorname{quo}_0(a,b)_n=\frac{a_n}{b_n}
\qquad(n\ge N_0).
$$

En ese supuesto, la escritura

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\ell
$$

significará exclusivamente que la sucesión real total $\operatorname{quo}_0(a,b)$ converge a $\ell$. La convención $0$ en los índices anteriores a $N_0$ no afecta a la convergencia: cualquier otra sucesión real que coincida con esos cocientes desde $N_0$ es eventualmente igual a $\operatorname{quo}_0(a,b)$, y Proposición 13.3.7 — Invariancia de la convergencia bajo coincidencia eventual conserva exactamente su límite. **No** se interpreta esta notación cuando el denominador pueda anularse arbitrariamente tarde sin una hipótesis adicional que legitime los cocientes.

> **Control de tipos.** $a$, $b$ y $\operatorname{quo}_0(a,b)$ son funciones $\mathbb N\to\mathbb R$; $a_n/b_n$ es un número real únicamente si $b_n\ne0$. La función totalizada facilita formular límites sin dejar indefinido el objeto secuencial, pero no sustituye la condición de denominador eventualmente positivo del criterio que sigue.

---

### Lema 14.6.3 — Un límite positivo proporciona dos cotas multiplicativas

Sean $a,b:\mathbb N\to\mathbb R$ sucesiones reales. Supongamos que existe $N_0$ tal que $b_n>0$ para todo $n\ge N_0$, y que

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=\ell>0.
$$

Entonces existen constantes reales $c,C$ con $0<c<C$ y un índice $N$ tales que

$$
\boxed{cb_n\le a_n\le Cb_n\qquad(n\ge N).}
$$

En concreto, pueden utilizarse $c=\ell/2$ y $C=3\ell/2$.

**Demostración.**

Sea $q=\operatorname{quo}_0(a,b)$. La hipótesis significa $q_n\to\ell$. Como $\ell>0$, el número real $\varepsilon:=\ell/2$ es positivo. Por la definición de convergencia existe un índice $N_1$ tal que

$$
|q_n-\ell|<\frac\ell2\qquad(n\ge N_1).
$$

La caracterización elemental del valor absoluto permite escribir

$$
-\frac\ell2<q_n-\ell<\frac\ell2,
$$

y, sumando $\ell$,

$$
\frac\ell2<q_n<\frac{3\ell}{2}
\qquad(n\ge N_1).
$$

Tomemos $N$ igual al mayor de los dos naturales $N_0,N_1$; su existencia resulta del orden total de $\mathbb N$, sin una elección de infinitos índices. Para $n\ge N$ se cumplen a la vez $b_n>0$ y $q_n=a_nb_n^{-1}$. Multiplicar las desigualdades por $b_n$ **conserva** su sentido, precisamente porque es positivo. Así,

$$
\frac\ell2\,b_n<a_n<\frac{3\ell}{2}\,b_n.
$$

Las desigualdades no estrictas requeridas se deducen inmediatamente. Como $\ell>0$, las constantes $c=\ell/2$ y $C=3\ell/2$ satisfacen $0<c<C$. ∎

> **Por qué importa $\ell>0$.** La cota inferior útil procede de una vecindad del límite que no alcance el cero. Si el límite fuese cero, no existiría por este argumento una constante $c>0$ que garantizase $cb_n\le a_n$; sólo se conservaría la cota superior.

---

### Teorema 14.6.4 — Criterio de comparación por límite positivo

Sean $a,b:\mathbb N\to\mathbb R$ sucesiones cuyos términos son **no negativos**. Supongamos que $b_n>0$ para todo $n$ suficientemente grande y que, en el sentido preciso de la definición anterior,

$$
\boxed{\lim_{n\to\infty}\frac{a_n}{b_n}=\ell,
\qquad \ell\in\mathbb R,\ \ell>0.}
$$

La última expresión significa que $\ell$ es un **número real** positivo y finito; no introduce un elemento $\infty$ en el cuerpo real. Entonces

$$
\boxed{
\sum_{n=0}^{\infty}a_n\ \text{converge}
\quad\Longleftrightarrow\quad
\sum_{n=0}^{\infty}b_n\ \text{converge}.}
$$

Por negación de ambas condiciones equivalentes, las dos series también **divergen simultáneamente**, en el sentido de divergencia real adoptado en §14.1.

**Demostración.**

Aplicamos Lema 14.6.3 — Un límite positivo proporciona dos cotas multiplicativas a la hipótesis de límite positivo. Obtenemos un índice $N$ y constantes reales positivas $c,C$ tales que

$$
\boxed{0\le cb_n\le a_n\le Cb_n
\qquad(n\ge N).}
$$

Las desigualdades son válidas entre términos no negativos; no intentaremos deducir de ellas el orden de las **sumas totales**, pues sólo sabemos que se cumplen desde cierto índice.

**Si converge la serie de términos $b$.** Por Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo, multiplicarla por el escalar no nulo $C$ conserva su convergencia: $\sum Cb_n$ converge. Como $0\le a_n\le Cb_n$ para $n\ge N$, el corolario de comparación eventual Corolario 14.5.3 — Comparación válida a partir de cierto índice establece que converge $\sum a_n$.

**Si converge la serie de términos $a$.** Usamos ahora la cota inferior $0\le cb_n\le a_n$ para $n\ge N$. El mismo corolario demuestra que converge $\sum cb_n$. Puesto que $c>0$ es no nulo, Proposición 14.6.1 — Multiplicación de una serie por un escalar no nulo permite recuperar la convergencia de $\sum b_n$ multiplicando por $c^{-1}$.

Se han demostrado ambas implicaciones. Si una serie divergiese mientras la otra convergiese, contradiría la equivalencia; por tanto la divergencia también se comparte. ∎

> **Qué no afirma el teorema.** El límite $\ell$ compara *términos*, no determina la razón entre las sumas de las series. Tampoco decide por sí solo cuál de las dos series converge: suministra una equivalencia y requiere una serie de referencia cuyo comportamiento ya esté establecido. En particular, si $a_n=b_n=1$ ambas divergen con cociente igual a $1$; si $a_n=b_n=(1/2)^n$, ambas convergen con el mismo cociente, por el criterio geométrico de §14.3.

---

### Corolario 14.6.5 — Límite nulo y comparación unilateral

Sean $a,b$ sucesiones de términos no negativos y supongamos que $b_n>0$ eventualmente. Si

$$
\lim_{n\to\infty}\frac{a_n}{b_n}=0,
$$

entonces

$$
\boxed{
\sum_{n=0}^{\infty}b_n\text{ converge}
\Longrightarrow
\sum_{n=0}^{\infty}a_n\text{ converge}.}
$$

Por contraposición, si la serie de términos $a$ diverge, también diverge la de términos $b$. Sin embargo, de la divergencia de la serie $b$ no puede deducirse la convergencia ni la divergencia de la serie $a$.

**Demostración.**

Sea $q=\operatorname{quo}_0(a,b)$. Tenemos $q_n\to0$. Apliquemos la definición de límite a la tolerancia real $\varepsilon=1$. Existe $N_1$ tal que $|q_n|<1$ para $n\ge N_1$. Elijamos un índice $N$ posterior tanto a $N_1$ como al índice de positividad del denominador. Para todo $n\ge N$,

$$
0\le q_n=\frac{a_n}{b_n}<1,
$$

pues $a_n\ge0$ y $b_n>0$. La multiplicación por $b_n$ produce $0\le a_n<b_n$. En particular, $0\le a_n\le b_n$ eventualmente, de modo que Corolario 14.5.3 — Comparación válida a partir de cierto índice demuestra la implicación de convergencia. La afirmación sobre divergencia de $a$ es su contraposición.

Para comprobar que no existe una conclusión recíproca general, fijemos $b_n=1$ para todos los índices. Su serie diverge porque sus términos constantes no tienden a cero (Corolario 14.2.5 — Criterio de divergencia por el término general). Construyamos dos sucesiones no negativas diferentes:

* **Primera:** $a_n=(1/2)^n$. Por Teorema 14.3.7 — Clasificación completa de la serie geométrica, la serie de $a$ converge. Como $b_n=1$, el cociente es $(1/2)^n\to0$ por Teorema 14.3.4 — Las potencias de una base de módulo menor que uno tienden a cero.
* **Segunda:** $a_n=(\nu_{\mathbb R}(n+1))^{-1}$, cuyos términos constituyen la serie armónica de §14.2. Ésta diverge por Proposición 14.2.7 — La condición $a_n\to0$ no es suficiente: la serie armónica, aunque $a_n\to0$ por Lema 13.10.2 — Los recíprocos de los numerales positivos tienden a cero. Nuevamente, $a_n/b_n=a_n\to0$.

Las dos parejas cumplen las mismas hipótesis del corolario, incluida la divergencia de la serie $b$, pero en un caso la de $a$ converge y en el otro diverge. La afirmación de que no se puede concluir ninguno de los dos comportamientos queda verificada. ∎

> **Mapa lógico del criterio.** Si el cociente tiende a un real estrictamente positivo, hay cotas *superior e inferior* por múltiplos positivos y se obtiene equivalencia. Si tiende a cero, sólo se deduce la comparación eventual $a_n\le b_n$ y queda una implicación de convergencia. Para términos no negativos y denominador eventualmente positivo, un límite real del cociente no puede ser negativo: los cocientes son eventualmente no negativos y el paso al límite conserva ese orden (Teorema 13.6.2 — Preservación del orden en el paso al límite). El caso de cocientes sin límite, o de crecimiento no acotado sin límite real, no entra en este teorema; no anticipamos límites infinitos.

---

Esta distinción entre comparación bilateral y unilateral será esencial al elegir series de referencia. Hemos necesitado sólo el límite real de sucesiones, las reglas de orden y la comparación directa de §14.5. En §14.7 abordaremos la **condensación de Cauchy**, que organiza los términos de una serie monótona no negativa en bloques de longitud creciente y requiere justificar cuidadosamente la indexación de esos bloques antes de comparar sus sumas.
---

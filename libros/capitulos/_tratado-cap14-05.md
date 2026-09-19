## 14.5. Criterio de comparación directa para series {#sec-ta-14-5}

El criterio anterior transforma la convergencia de una serie de términos no negativos en una cuestión sobre cotas de sus sumas parciales. Para aprovecharlo, compararemos dos sucesiones de términos $a=(a_n)$ y $b=(b_n)$, con sus respectivas sucesiones de sumas parciales

$$
s=\operatorname{PS}(a),\qquad t=\operatorname{PS}(b).
$$

Una desigualdad entre términos individuales no es todavía una comparación de series: debemos probar que se conserva al efectuar **cada suma finita**. Sólo después podremos emplear el criterio de §14.4. Además, distinguiremos una desigualdad válida desde el primer término de otra que comienza tras un número finito de términos.

### Proposición 14.5.1 — Comparación de sumas finitas y de bloques

Sean $a,b:\mathbb N\to\mathbb R$ sucesiones reales, y escribamos $s=\operatorname{PS}(a)$ y $t=\operatorname{PS}(b)$. Valen las afirmaciones siguientes, **sin imponer todavía que los términos sean no negativos**.

1. Si $a_k\le b_k$ para todo $k\in\mathbb N$, entonces, para cada $n\in\mathbb N$,

   $$
   \boxed{\sum_{k=0}^{n}a_k\le\sum_{k=0}^{n}b_k,\quad\text{es decir, }s_n\le t_n.}
   $$

2. Si $N\in\mathbb N$ y $a_k\le b_k$ para todo $k\ge N$, entonces, para todo $m\ge N$,

   $$
   \boxed{s_m-s_N\le t_m-t_N.}
   $$

   Cuando $m>N$, la última desigualdad equivale, con la notación de bloques ya definida, a

   $$
   \sum_{k=N+1}^{m}a_k\le\sum_{k=N+1}^{m}b_k.
   $$

**Demostración.**

**Primera afirmación.** Procedemos por inducción sobre $n$. Para $n=0$, las ecuaciones de las sumas parciales dan $s_0=a_0\le b_0=t_0$. Si $s_n\le t_n$, la compatibilidad de la suma con el orden real y la hipótesis $a_{n+1}\le b_{n+1}$ implican

$$
s_{n+1}=s_n+a_{n+1}\le t_n+b_{n+1}=t_{n+1}.
$$

Por inducción, $s_n\le t_n$ para cada $n$. La notación de sumas finitas reproduce exactamente esta desigualdad.

**Segunda afirmación.** Fijemos $N$ como en el enunciado. Demostraremos por inducción en $j\in\mathbb N$ que

$$
s_{N+j}-s_N\le t_{N+j}-t_N.
$$

En $j=0$ ambos miembros son $0$. Supongamos la desigualdad para $j$ y pongamos $m=N+j$. Por la aritmética y el orden naturales, $m+1\ge N$; de hecho, $m+1=N+(j+1)$. La hipótesis permite, por tanto, utilizar $a_{m+1}\le b_{m+1}$. Las identidades recursivas y las leyes aditivas del cuerpo real dan

$$
\begin{aligned}
s_{m+1}-s_N
&=(s_m-s_N)+a_{m+1}\\
&\le(t_m-t_N)+b_{m+1}\\
&=t_{m+1}-t_N.
\end{aligned}
$$

La inducción queda completa. Todo $m\ge N$ puede escribirse $m=N+j$ para algún $j\in\mathbb N$, por la definición del orden natural. Para $m>N$ aplicamos Notación 14.2.1 — Suma de un bloque finito posterior y obtenemos la comparación de bloques; no hemos usado una notación de bloque vacío en el caso $m=N$. ∎

> **Lo que se ha probado, y lo que no.** Las desigualdades entre términos se transfieren a las sumas finitas por inducción. La proposición no supone convergencia ni compara todavía valores de sumas infinitas. Tampoco usa completitud.

---

### Teorema 14.5.2 — Criterio de comparación directa

Sean $a,b:\mathbb N\to\mathbb R$ sucesiones tales que

$$
\boxed{0\le a_n\le b_n\qquad(n\in\mathbb N).}
$$

Entonces:

1. si la serie $\sum_{n=0}^{\infty}b_n$ converge, también converge $\sum_{n=0}^{\infty}a_n$ y sus sumas reales satisfacen

   $$
   \boxed{0\le\sum_{n=0}^{\infty}a_n\le\sum_{n=0}^{\infty}b_n;}
   $$

2. si la serie $\sum_{n=0}^{\infty}a_n$ diverge, también diverge $\sum_{n=0}^{\infty}b_n$.

**Demostración.**

Sean $s=\operatorname{PS}(a)$ y $t=\operatorname{PS}(b)$. La primera parte de Proposición 14.5.1 — Comparación de sumas finitas y de bloques da

$$
\boxed{s_n\le t_n\qquad(n\in\mathbb N).}
$$

Además, todos los términos de ambas sucesiones son no negativos: $a_n\ge0$ por hipótesis y $b_n\ge a_n\ge0$. Por Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa, sus sumas parciales son no negativas y crecientes.

**Primera afirmación.** Supongamos que la serie de términos $b$ converge. El teorema Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos afirma que el conjunto $t[\mathbb N]$ tiene supremo real y que éste es la suma $B:=\sum_{n=0}^{\infty}b_n$. En particular,

$$
0\le s_n\le t_n\le B\qquad(n\in\mathbb N).
$$

Así, $B$ es una cota superior del conjunto no vacío $s[\mathbb N]$. Aplicamos nuevamente Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos, esta vez a los términos $a$, y concluimos que su serie converge. Sólo **ahora**, estando definida su suma real, escribimos

$$
A:=\sum_{n=0}^{\infty}a_n=\sup s[\mathbb N].
$$

Como $0\le s_n\le B$ para cada $n$, tanto $0$ como cota inferior de los valores de $s$ y $B$ como cota superior implican $0\le A\le B$ por las propiedades definitorias del supremo. Se obtiene la primera conclusión.

**Segunda afirmación.** Supongamos que la serie de términos $a$ diverge. Si la serie de términos $b$ convergiera, la primera afirmación demostraría que la de términos $a$ también converge, contradicción. Luego la serie de términos $b$ diverge. Es la contraposición de la implicación de convergencia ya demostrada, no un criterio independiente. ∎

> **Direcciones de uso.** Una *cota superior por una serie convergente* prueba convergencia de la serie menor. Una *cota inferior por una serie divergente* prueba divergencia de la serie mayor. No cabe invertir esas flechas: saber que converge la serie menor o que diverge la mayor, sin otras hipótesis, no resuelve el comportamiento de la otra.

> **Auditoría.** La transferencia de cotas es algebraica y de orden; la conclusión de convergencia utiliza la completitud real exclusivamente a través de Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos. La divergencia se obtiene por contraposición. Ningún paso requiere Choice ni proporciona automáticamente un procedimiento computable para determinar las sumas.

---

### Corolario 14.5.3 — Comparación válida a partir de cierto índice

Sean $a,b:\mathbb N\to\mathbb R$ sucesiones de términos **no negativos**, y supongamos que existe $N\in\mathbb N$ para el cual

$$
a_n\le b_n\qquad\text{para todo }n\ge N.
$$

Entonces siguen siendo válidas las dos implicaciones del criterio directo:

$$
\boxed{
\sum_{n=0}^{\infty}b_n\text{ converge}
\Longrightarrow
\sum_{n=0}^{\infty}a_n\text{ converge},
}
$$

$$
\boxed{
\sum_{n=0}^{\infty}a_n\text{ diverge}
\Longrightarrow
\sum_{n=0}^{\infty}b_n\text{ diverge}.
}
$$

La comparación eventual **no** implica, sin una condición adicional sobre los términos iniciales, que la suma real de $a$ sea menor o igual que la de $b$.

**Demostración.**

Fijemos un testigo $N$ de la hipótesis; esta instanciación de un cuantificador existencial no constituye una selección simultánea ni utiliza Choice. Pongamos $s=\operatorname{PS}(a)$ y $t=\operatorname{PS}(b)$.

Supongamos primero que la serie de términos $b$ converge y llamemos $B$ a su suma real. Puesto que $b$ es no negativa, Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos asegura $t_m\le B$ para todo $m$. Por la segunda parte de Proposición 14.5.1 — Comparación de sumas finitas y de bloques, para $m\ge N$,

$$
s_m-s_N\le t_m-t_N,
$$

luego

$$
s_m\le s_N+B-t_N=:K.
$$

Como $t_N\le B$, tenemos $s_N\le K$. Para los índices $m\le N$, la monotonía Proposición 14.4.1 — Monotonía de las sumas parciales de una serie no negativa de $s$ proporciona $s_m\le s_N\le K$. Si $m\ge N$, ya establecimos $s_m\le K$. La totalidad del orden natural cubre todos los casos: por tanto $K\in\mathbb R$ es una cota superior **global** de $s[\mathbb N]$. El criterio Teorema 14.4.2 — Criterio de convergencia para series de términos no negativos demuestra que la serie de términos $a$ converge.

Si la serie de términos $a$ diverge, la convergencia de la de términos $b$ contradiría la implicación recién probada. Se obtiene la segunda afirmación por contraposición. ∎

**Por qué no se comparan directamente las sumas.** Consideremos las sucesiones definidas por $a_0=1$, $b_0=0$ y $a_n=b_n=0$ para todo $n\ge1$. Existen como funciones mediante separación de los grafos determinados por esos valores. Son no negativas, y la desigualdad $a_n\le b_n$ se cumple para $n\ge1$. Por Proposición 14.1.6 — Estabilización de sumas parciales cuando los términos tardíos son nulos, ambas series convergen, pero

$$
\sum_{n=0}^{\infty}a_n=1>0=\sum_{n=0}^{\infty}b_n.
$$

Los primeros términos pueden alterar el valor total aunque no alteren la conclusión comparativa sobre convergencia. La prueba no ha necesitado definir sumas vacías, asignar un valor $+\infty$ a una serie divergente ni convertir una comparación eventual en una desigualdad global falsa.

---

Las dos versiones del criterio permiten sustituir la búsqueda de una suma exacta por la comparación con una serie conocida. La serie geométrica del §14.3 proporciona ya una familia de referencia cuando su razón tiene módulo menor que uno; el criterio no autoriza, sin embargo, a inferir el resultado inverso a partir de una sola desigualdad. En §14.6 estudiaremos la comparación por límite, que exige precisar cómo una razón entre términos conserva —o deja de conservar— estas cotas.

---

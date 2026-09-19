## 8.3. Convergencia racional {#sec-ta-8-3}

La distancia racional permite sustituir la expresión informal «los términos se acercan a un racional» por una condición cuantificada. La dificultad conceptual está en el orden de los cuantificadores.

No basta exigir que algún término de la sucesión quede cerca del candidato a límite, ni que ocurra esto para una precisión fija. Debemos poder imponer **cualquier precisión racional positiva** y encontrar, a partir de ella, una etapa después de la cual todos los términos permanezcan dentro de esa precisión.

La forma lógica será

$$
\forall\varepsilon>0\;\exists N\;\forall n\geq N.
$$

Pero cada cuantificador debe conservar su tipo. En esta etapa, tanto la precisión como el posible límite son racionales. No interviene ningún elemento de $\mathbb R_D$.

### Definición 8.3.1 — Convergencia racional

Sea

$$
q=(q_n)_{n\in\mathbb N}\in\mathbb Q^{\mathbb N}
$$

y sea $\ell\in\mathbb Q$.

Diremos que **$q$ converge racionalmente a $\ell$** si

$$
\boxed{
\forall\varepsilon\in\mathbb Q\;
\Bigl(
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\leq n
\Longrightarrow
d_{\mathbb Q}(q_n,\ell)<\varepsilon
\bigr)
\Bigr).
}
$$

El racional $\ell$ se llama entonces un **límite racional** de la sucesión $q$.

Diremos que $q$ es **convergente en $\mathbb Q$** si existe algún $\ell\in\mathbb Q$ al cual converge racionalmente.

Hay tres aspectos de la definición que conviene fijar desde ahora.

Primero, $N$ puede depender de $\varepsilon$. Cuanto menor sea la precisión exigida, más lejos puede ser necesario avanzar en la sucesión.

Segundo, una vez elegido $N$, la condición debe valer para **todo** índice posterior: no basta con encontrar términos aislados cercanos a $\ell$.

Tercero, el cuantificador de precisión recorre sólo los racionales positivos. No estamos utilizando una noción previa de distancia real ni la completitud de $\mathbb R_D$.

Llamaremos **módulo de convergencia** para $q_n\to_{\mathbb Q}\ell$ a una función
$$
\mu:\mathbb Q_{>0}\to\mathbb N
$$
tal que, para todo $\varepsilon>0$,
$$
n\geq\mu(\varepsilon)\Longrightarrow d_{\mathbb Q}(q_n,\ell)<\varepsilon.
$$
Si $\mu$ es computable respecto de las representaciones racionales y naturales fijadas, hablaremos de **módulo efectivo de convergencia**.

Clásicamente, cuando la sucesión converge, para cada precisión existe un menor índice que funciona. Esa mínima elección está unívocamente determinada por el buen orden de $\mathbb N$, pero:
$$
\boxed{\text{módulo mínimo canónico}\neq\text{módulo computable}.}
$$

> **Nota fundacional.** La definición no usa Choice. Para cada $\varepsilon$ se afirma la existencia de algún índice $N$; no se forma ni se presupone una función global $\varepsilon\mapsto N$.

---

### Notación 8.3.2 — Flecha de convergencia racional

Cuando $q=(q_n)_{n\in\mathbb N}$ converge racionalmente a $\ell$, escribiremos

$$
\boxed{
q_n\to_{\mathbb Q}\ell.
}
$$

Equivalentemente puede escribirse

$$
(q_n)_{n\in\mathbb N}\to_{\mathbb Q}\ell.
$$

El subíndice $\mathbb Q$ recuerda que tanto la sucesión como el límite pertenecen al sistema racional. No se omitirá mientras la construcción de Cauchy siga siendo independiente de $\mathbb R_D$.

---

### Proposición 8.3.3 — Formulaciones equivalentes de la convergencia racional

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional y sea $\ell\in\mathbb Q$. Son equivalentes:

1. $q_n\to_{\mathbb Q}\ell$;
2. para todo $\varepsilon\in\mathbb Q$ con $0<\varepsilon$, existe $N\in\mathbb N$ tal que, para todo $n\in\mathbb N$,
   $$
   N\leq n
   \Longrightarrow
   |q_n-\ell|<\varepsilon;
   $$
3. para todo $\varepsilon\in\mathbb Q$ con $0<\varepsilon$, existe $N\in\mathbb N$ tal que, para todo $n\in\mathbb N$,
   $$
   N\leq n
   \Longrightarrow
   \ell-\varepsilon<q_n<\ell+\varepsilon.
   $$

**Demostración.**

La definición Definición 8.3.1 — Convergencia racional afirma que, para cada $\varepsilon>0$, existe un mismo índice $N$ a partir del cual

$$
d_{\mathbb Q}(q_n,\ell)<\varepsilon.
$$

Pero Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional, aplicada a $x=q_n$ y $y=\ell$, establece término a término las equivalencias

$$
d_{\mathbb Q}(q_n,\ell)<\varepsilon
\iff
|q_n-\ell|<\varepsilon
$$

y

$$
|q_n-\ell|<\varepsilon
\iff
\ell-\varepsilon<q_n<\ell+\varepsilon.
$$

Por tanto, para cada $\varepsilon>0$, cualquiera de las tres condiciones vale a partir de un índice $N$ si y sólo si valen las otras dos a partir del mismo índice. Los cuantificadores exteriores son idénticos, de modo que las tres formulaciones son equivalentes. ∎

La segunda forma mide el error mediante una diferencia absoluta; la tercera dice que todos los términos suficientemente tardíos quedan atrapados en cualquier ventana racional centrada en $\ell$.

---

### Proposición 8.3.4 — Las sucesiones constantes convergen a su valor

Para todo $c\in\mathbb Q$,

$$
\boxed{
\underline c_n\to_{\mathbb Q}c.
}
$$

**Demostración.**

Sea $\varepsilon\in\mathbb Q$ con $0<\varepsilon$. Tomemos

$$
N:=0\in\mathbb N.
$$

Si $n\in\mathbb N$ y $N\leq n$, entonces, por definición de sucesión constante,

$$
\underline c_n=c.
$$

Por la definitud de la distancia racional (Proposición 8.2.2 — Propiedades fundamentales de la distancia racional),

$$
d_{\mathbb Q}(\underline c_n,c)
=
d_{\mathbb Q}(c,c)
=
0.
$$

Como $0<\varepsilon$,

$$
d_{\mathbb Q}(\underline c_n,c)<\varepsilon.
$$

El mismo índice $N=0$ sirve para la precisión racional positiva arbitraria $\varepsilon$. Por Definición 8.3.1 — Convergencia racional,

$$
\underline c_n\to_{\mathbb Q}c.
$$

∎

Esta proposición no identifica el racional $c$ con la sucesión $\underline c$. Afirma únicamente que el proceso constante asociado a $c$ tiene a $c$ como límite racional.

---

### Teorema 8.3.5 — Unicidad del límite racional

Sea $q=(q_n)_{n\in\mathbb N}$ una sucesión racional. Si

$$
q_n\to_{\mathbb Q}\ell
$$

y

$$
q_n\to_{\mathbb Q}m,
$$

con $\ell,m\in\mathbb Q$, entonces

$$
\boxed{\ell=m.}
$$

**Demostración.**

Por la tricotomía decidible de los racionales (Proposición 3.7.6 — Tricotomía decidible de los racionales), podemos decidir si
$\ell=m$. En ese caso la conclusión ya está demostrada. Supongamos, pues, la rama decidida
$\ell\neq m$ y definamos

$$
\delta:=d_{\mathbb Q}(\ell,m).
$$

Por Proposición 8.2.2 — Propiedades fundamentales de la distancia racional,

$$
0\leq\delta,
\qquad
\delta=0
\iff
\ell=m.
$$

La rama $\ell\neq m$ implica $\delta\neq0$. Aplicando nuevamente la tricotomía decidible en
$\mathbb Q$ a $0$ y $\delta$, y usando $0\leq\delta$, obtenemos

$$
0<\delta.
$$

Para obtener una precisión suficientemente pequeña sin introducir ningún real, trabajamos sólo dentro de $\mathbb Q$. Pongamos

$$
s:=1_{\mathbb Q}+1_{\mathbb Q}.
$$

Como $\mathbb Q$ es un cuerpo ordenado, Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3) da

$$
0<1_{\mathbb Q}.
$$

Sumando $1_{\mathbb Q}$ mediante Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8),

$$
1_{\mathbb Q}<s,
$$

y por transitividad

$$
0<s.
$$

En particular $s\neq0$, por lo que está definida la división por $s$. Sea

$$
\varepsilon:=\frac{\delta}{s}.
$$

La positividad del inverso y del producto en un cuerpo ordenado (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (5),(6)) da

$$
0<\varepsilon.
$$

Además, usando la definición de división y la ley del inverso Proposición 3.6.5 — Ley del inverso multiplicativo,

$$
\begin{aligned}
\varepsilon+\varepsilon
&=\delta s^{-1}+\delta s^{-1}\\
&=\delta(1_{\mathbb Q}+1_{\mathbb Q})s^{-1}\\
&=\delta ss^{-1}\\
&=\delta.
\end{aligned}
$$

Aplicamos ahora las dos hipótesis de convergencia a esta misma precisión $\varepsilon$. Existen $N_\ell,N_m\in\mathbb N$ tales que

$$
N_\ell\leq n
\Longrightarrow
d_{\mathbb Q}(q_n,\ell)<\varepsilon
$$

para todo $n\in\mathbb N$, y

$$
N_m\leq n
\Longrightarrow
d_{\mathbb Q}(q_n,m)<\varepsilon
$$

para todo $n\in\mathbb N$.

El orden de $\mathbb N$ es total por Teorema 1.6.5 — Orden total. Por tanto ocurre uno de los dos casos

$$
N_\ell\leq N_m
$$

o

$$
N_m\leq N_\ell.
$$

Supongamos primero $N_\ell\leq N_m$ y tomemos $n:=N_m$. Entonces

$$
d_{\mathbb Q}(q_n,\ell)<\varepsilon,
\qquad
d_{\mathbb Q}(q_n,m)<\varepsilon.
$$

Por simetría y desigualdad triangular de Proposición 8.2.2 — Propiedades fundamentales de la distancia racional,

$$
\begin{aligned}
\delta
&=d_{\mathbb Q}(\ell,m)\\
&\leq d_{\mathbb Q}(\ell,q_n)+d_{\mathbb Q}(q_n,m)\\
&=d_{\mathbb Q}(q_n,\ell)+d_{\mathbb Q}(q_n,m).
\end{aligned}
$$

De las dos desigualdades estrictas anteriores y la invariancia estricta por traslación (Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8)) se obtiene

$$
d_{\mathbb Q}(q_n,\ell)+d_{\mathbb Q}(q_n,m)
<
\varepsilon+\varepsilon
=
\delta.
$$

Así tendríamos

$$
\delta<\delta,
$$

contradicción con la irreflexividad del orden estricto.

El caso $N_m\leq N_\ell$ es idéntico, tomando $n:=N_\ell$.

Por tanto la rama decidida $\ell\neq m$ es imposible. La única alternativa restante de la
tricotomía racional es

$$
\ell=m.
$$

∎

> **Auditoría de elección.** De cada una de las dos hipótesis de convergencia extraemos un único testigo $N_\ell$ y $N_m$ para la precisión fija $\varepsilon$. Son dos instanciaciones existenciales locales. La comparación de ambos índices se realiza por totalidad del orden natural; no se escoge simultáneamente una familia de índices y no interviene Choice.

---

### Lo que hemos ganado

La noción de aproximación posee ya una forma rigurosa dentro de $\mathbb Q$:

$$
q_n\to_{\mathbb Q}\ell
$$

significa que cualquier ventana racional positiva alrededor de $\ell$ termina conteniendo todos los términos suficientemente tardíos de la sucesión.

Además, si tal racional $\ell$ existe, es único. Por ello tiene sentido hablar de **el** límite racional de una sucesión convergente.

Pero la definición contiene una limitación decisiva: para afirmar convergencia debemos conocer de antemano un candidato $\ell\in\mathbb Q$. Precisamente las aproximaciones que deberían representar los racionales ausentes —como las que se organizan alrededor de la ecuación $x^2=2$— pueden no disponer de tal límite dentro de $\mathbb Q$.

Necesitamos, por tanto, una condición que mida si los términos de una sucesión se estabilizan **entre sí**, sin mencionar todavía ningún objeto exterior a la sucesión. Ése será el papel de **§8.4 — Sucesiones de Cauchy**.

---

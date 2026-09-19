## 13.3. Convergencia de sucesiones reales {#sec-ta-13-3}

La eventualidad aislada en §13.2 permite formular ahora con precisión la idea intuitiva de que los términos de una sucesión se acercan a un número real.

La dificultad no está en escribir una desigualdad como

$$
|a_n-\ell|<\varepsilon.
$$

La dificultad está en **quién puede depender de quién**. Una precisión $\varepsilon$ se impone primero; sólo después podemos elegir un umbral $N$ adaptado a esa precisión; y, una vez fijado ese umbral, la estimación debe valer para todos los índices posteriores.

El patrón lógico fundamental es

$$
\boxed{
\forall \varepsilon>0\;
\exists N\in\mathbb N\;
\forall n\ge N.
}
$$

La definición siguiente es uno de los primeros lugares del tratado en que el orden de los cuantificadores forma parte esencial del contenido matemático.

### Definición 13.3.1 — Convergencia de una sucesión real

Sea

$$
a=(a_n)_{n\in\mathbb N}\in\mathbb R^{\mathbb N}
$$

y sea $\ell\in\mathbb R$.

Diremos que **$a$ converge a $\ell$** si, para todo $\varepsilon\in\mathbb R$ con $0<\varepsilon$, la propiedad

$$
|a_n-\ell|<\varepsilon
$$

vale eventualmente.

Por Definición 13.2.4 — Conjunto eventual y propiedad eventual, esto significa exactamente

$$
\boxed{
\forall\varepsilon\in\mathbb R\;
\Bigl(
0<\varepsilon
\Longrightarrow
\exists N\in\mathbb N\;
\forall n\in\mathbb N\;
\bigl(
N\le n
\Longrightarrow
|a_n-\ell|<\varepsilon
\bigr)
\Bigr).
}
$$

El número $\ell$ se llama entonces **un límite** de la sucesión $a$.

Diremos que $a$ es **convergente** si existe algún $\ell\in\mathbb R$ al cual converge.

La definición contiene tres dependencias lógicas que no deben alterarse:

1. $\varepsilon$ es arbitrario y positivo;
2. el umbral $N$ puede depender de $\varepsilon$;
3. después de fijar $N$, la desigualdad debe valer para **todo** $n\ge N$.

> **Lectura de cuantificadores.** La forma
> $$
> \forall\varepsilon>0\;\exists N\;\forall n\ge N
> $$
> no puede reemplazarse por «para cada $\varepsilon$ aparecen términos arbitrariamente tardíos dentro de la ventana». Esa condición permitiría que la sucesión volviera a alejarse infinitas veces. Convergencia exige permanencia eventual.

> **Prueba de estrés.** Tampoco podemos colocar el cuantificador de $N$ antes del de $\varepsilon$:
> $$
> \exists N\;\forall\varepsilon>0\;\forall n\ge N.
> $$
> Esa condición es mucho más fuerte: en el marco clásico del tratado obligaría a que todos los términos de una cola fueran exactamente iguales a $\ell$.

> **Nota fundacional.** La definición no usa Choice. Para cada precisión positiva se afirma la existencia de un umbral; no se presupone una función global $\varepsilon\mapsto N$. Si más adelante se desea empaquetar umbrales en un módulo de convergencia, eso constituye **datos adicionales**. Para cada $\varepsilon>0$ fijo, el conjunto de umbrales que funcionan existe por Separación, es no vacío y posee un menor elemento por Teorema 1.6.13 — Principio de buen orden. Si se empaquetan esos mínimos para todas las precisiones en una función, Replacement basta porque el valor está unívocamente determinado; no se requiere Choice. De ello no se sigue que el módulo sea computable.

> **Nota estructural.** La completitud de $\mathbb R$ no interviene en la definición. La misma noción tiene sentido en cualquier cuerpo ordenado. La completitud será necesaria después para demostrar que ciertas sucesiones **poseen** un límite, no para explicar qué significa converger a uno ya dado.

---

### Notación 13.3.2 — Flecha de convergencia real

Cuando $a=(a_n)$ converge a $\ell\in\mathbb R$, escribiremos

$$
\boxed{
a_n\to\ell.
}
$$

También podremos escribir

$$
(a_n)_{n\in\mathbb N}\to\ell
$$

cuando convenga hacer visible la sucesión completa.

A diferencia de las notaciones anteriores

$$
q_n\to_{\mathbb Q}\ell
\qquad\text{y}\qquad
x_n\to_C L,
$$

la flecha sin subíndice se reserva desde ahora para la convergencia en el $\mathbb R$ estructural de la Parte II.

---

### Proposición 13.3.3 — Formulaciones equivalentes de la convergencia

Sea $a=(a_n)$ una sucesión real y sea $\ell\in\mathbb R$. Son equivalentes:

1. $a_n\to\ell$;
2. para todo $\varepsilon\in\mathbb R$ con $0<\varepsilon$, el conjunto
   $$
   E_\varepsilon
   :=
   \{n\in\mathbb N:|a_n-\ell|<\varepsilon\}
   $$
   es eventual;
3. para todo $\varepsilon\in\mathbb R$ con $0<\varepsilon$, la propiedad
   $$
   \ell-\varepsilon<a_n<\ell+\varepsilon
   $$
   vale eventualmente;
4. para todo $\varepsilon\in\mathbb R$ con $0<\varepsilon$, la propiedad
   $$
   a_n\in(\ell-\varepsilon,\ell+\varepsilon)
   $$
   vale eventualmente.

**Demostración.**

La equivalencia entre (1) y (2) es exactamente la definición de convergencia junto con la definición de propiedad eventual Definición 13.2.4 — Conjunto eventual y propiedad eventual.

Para comparar (2) y (3), fijemos $\varepsilon>0$ y un índice $n$. Pondremos

$$
x:=a_n-\ell.
$$

Afirmamos que

$$
\boxed{
|x|<\varepsilon
\iff
-\varepsilon<x<\varepsilon.
}
$$

Supongamos primero $|x|<\varepsilon$. Por Proposición 4.2.2 — Propiedades elementales del valor absoluto (4),

$$
-|x|\le x\le|x|.
$$

De $|x|<\varepsilon$ tenemos $|x|\le\varepsilon$ y $|x|\ne\varepsilon$. Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (2),

$$
-\varepsilon\le -|x|.
$$

La igualdad $-\varepsilon=-|x|$ implicaría $\varepsilon=|x|$, contradicción. Por la definición del orden estricto,

$$
-\varepsilon<-|x|.
$$

Por transitividad,

$$
-\varepsilon<x<\varepsilon.
$$

Recíprocamente, supongamos

$$
-\varepsilon<x<\varepsilon.
$$

La totalidad del orden da $0\le x$ o $x\le0$.

Si $0\le x$, por la definición de valor absoluto,

$$
|x|=x<\varepsilon.
$$

Si $x\le0$, entonces $|x|=-x$. De $-\varepsilon<x$ se obtiene $-x\le\varepsilon$ por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (2). La igualdad $-x=\varepsilon$ devolvería $x=-\varepsilon$, contradiciendo la desigualdad estricta; por tanto

$$
-x<\varepsilon,
$$

y nuevamente

$$
|x|<\varepsilon.
$$

Así queda probada la equivalencia puntual. Sumando $\ell$ a las dos desigualdades

$$
-\varepsilon<a_n-\ell<\varepsilon
$$

obtenemos, por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (8),

$$
\ell-\varepsilon<a_n<\ell+\varepsilon.
$$

Por tanto (2) y (3) expresan la misma propiedad eventual para cada $\varepsilon>0$.

Finalmente, por la definición del intervalo abierto Definición 4.3.1 — Intervalos acotados,

$$
a_n\in(\ell-\varepsilon,\ell+\varepsilon)
\iff
\ell-\varepsilon<a_n<\ell+\varepsilon.
$$

Luego (3) y (4) son equivalentes. ∎

Las cuatro formas describen el mismo fenómeno desde perspectivas distintas:

$$
\boxed{
\text{error absoluto}
\;\longleftrightarrow\;
\text{conjunto eventual}
\;\longleftrightarrow\;
\text{ventana alrededor del límite}.
}
$$

La tercera y la cuarta formulación hacen especialmente visible la geometría de la recta: toda ventana abierta centrada en $\ell$, por pequeña que sea, contiene finalmente todos los términos de la sucesión.

---

### Proposición 13.3.4 — Las sucesiones constantes convergen a su valor

Para todo $c\in\mathbb R$,

$$
\boxed{
\underline c_n\to c.
}
$$

**Demostración.**

Sea $\varepsilon\in\mathbb R$ con $0<\varepsilon$. Para todo $n\in\mathbb N$,

$$
\underline c_n=c,
$$

y por tanto

$$
|\underline c_n-c|
=
|0|
=
0
<
\varepsilon.
$$

La propiedad vale para todos los índices y, por Proposición 13.2.5 — Reglas elementales de eventualidad (1), vale eventualmente. Como $\varepsilon>0$ era arbitrario, Definición 13.3.1 — Convergencia de una sucesión real da

$$
\underline c_n\to c.
$$

∎

La proposición no identifica $c$ con $\underline c$. Afirma que el proceso constante asociado a $c$ tiene a $c$ como límite.

---

### Teorema 13.3.5 — Unicidad del límite real

Sea $a=(a_n)$ una sucesión real. Si

$$
a_n\to\ell
$$

y

$$
a_n\to m,
$$

con $\ell,m\in\mathbb R$, entonces

$$
\boxed{
\ell=m.
}
$$

**Demostración.**

Supongamos, buscando una contradicción, que

$$
\ell\ne m.
$$

Definamos

$$
\delta:=|\ell-m|.
$$

Por Proposición 4.2.2 — Propiedades elementales del valor absoluto,

$$
0\le\delta
$$

y

$$
\delta=0
\iff
\ell-m=0
\iff
\ell=m.
$$

La hipótesis $\ell\ne m$ implica $\delta\ne0$. Como el orden estricto asociado satisface

$$
0<\delta
\iff
0\le\delta
\text{ y }
0\ne\delta,
$$

obtenemos

$$
0<\delta.
$$

Pongamos

$$
s:=1+1.
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (3),

$$
0<1.
$$

Usando invariancia estricta por traslación,

$$
1<1+1=s,
$$

y por transitividad,

$$
0<s.
$$

En particular $s\ne0$, de modo que $s^{-1}$ está definido y, por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6),

$$
0<s^{-1}.
$$

Sea

$$
\varepsilon:=\delta s^{-1}.
$$

Por positividad del producto,

$$
0<\varepsilon.
$$

Las leyes del cuerpo dan

$$
\begin{aligned}
\varepsilon+\varepsilon
&=\delta s^{-1}+\delta s^{-1}\\
&=\delta(1+1)s^{-1}\\
&=\delta ss^{-1}\\
&=\delta.
\end{aligned}
$$

Aplicando las dos hipótesis de convergencia a esta misma precisión $\varepsilon$, las propiedades

$$
|a_n-\ell|<\varepsilon
$$

y

$$
|a_n-m|<\varepsilon
$$

valen eventualmente.

Por Proposición 13.2.5 — Reglas elementales de eventualidad (3), ambas valen simultáneamente de manera eventual. Existe entonces un umbral $N\in\mathbb N$ tal que, en particular para $n=N$,

$$
|a_N-\ell|<\varepsilon,
\qquad
|a_N-m|<\varepsilon.
$$

Por la desigualdad triangular Teorema 4.2.3 — Desigualdad triangular y la simetría del valor absoluto,

$$
\begin{aligned}
\delta
&=|\ell-m|\\
&=|(\ell-a_N)+(a_N-m)|\\
&\le |\ell-a_N|+|a_N-m|\\
&=|a_N-\ell|+|a_N-m|.
\end{aligned}
$$

Las dos desigualdades estrictas anteriores implican

$$
|a_N-\ell|+|a_N-m|
<
\varepsilon+\varepsilon
=
\delta.
$$

Por transitividad obtendríamos

$$
\delta<\delta,
$$

contradicción con la irreflexividad del orden estricto.

Hemos demostrado

$$
\neg(\ell\ne m).
$$

Como la lógica ambiente del tratado es clásica, la eliminación de la doble negación concluye

$$
\ell=m.
$$

∎

> **Auditoría fundacional.** La prueba no usa Choice. Sí utiliza lógica clásica en el último paso: a diferencia de lo ocurrido para $\mathbb Q$, no hemos establecido que la igualdad de números reales sea decidible. El argumento anterior produce constructivamente la imposibilidad de que dos candidatos distintos sean límites; convertir $\neg(\ell\ne m)$ en $\ell=m$ usa la lógica clásica declarada en el contrato fundacional.

La unicidad permite pasar ahora de «un límite» a **el límite** de una sucesión convergente.

---

### Notación 13.3.6 — Límite de una sucesión convergente

Si $a=(a_n)$ es convergente, denotaremos por

$$
\boxed{
\lim_{n\to\infty}a_n
}
$$

su único límite. Por tanto,

$$
\boxed{
\lim_{n\to\infty}a_n=\ell
\iff
a_n\to\ell.
}
$$

La expresión $n\to\infty$ pertenece a la notación de límite; **no** afirma que $\infty$ sea un número real ni introduce un nuevo elemento en $\mathbb R$.

La notación sólo se utilizará cuando la convergencia haya sido establecida o cuando aparezca dentro de una afirmación condicional que la suponga.

---

### Proposición 13.3.7 — Invariancia de la convergencia bajo coincidencia eventual

Sean $a,b\in\mathbb R^{\mathbb N}$ y supongamos

$$
a\sim_{\mathrm{ev}}b.
$$

Entonces, para todo $\ell\in\mathbb R$,

$$
\boxed{
a_n\to\ell
\iff
b_n\to\ell.
}
$$

En particular, $a$ es convergente si y sólo si $b$ es convergente y, en ese caso,

$$
\boxed{
\lim_{n\to\infty}a_n
=
\lim_{n\to\infty}b_n.
}
$$

**Demostración.**

Supongamos primero

$$
a_n\to\ell.
$$

Sea $\varepsilon>0$. Por convergencia, la propiedad

$$
|a_n-\ell|<\varepsilon
$$

vale eventualmente.

Por $a\sim_{\mathrm{ev}}b$, también vale eventualmente

$$
a_n=b_n.
$$

La regla de intersección Proposición 13.2.5 — Reglas elementales de eventualidad (3) da un tramo final en el que ambas propiedades son verdaderas simultáneamente. En ese tramo,

$$
|b_n-\ell|
=
|a_n-\ell|
<
\varepsilon.
$$

Por Proposición 13.2.5 — Reglas elementales de eventualidad (2), la propiedad

$$
|b_n-\ell|<\varepsilon
$$

es eventual. Como $\varepsilon>0$ era arbitrario,

$$
b_n\to\ell.
$$

La implicación recíproca se obtiene del mismo argumento usando la simetría de $\sim_{\mathrm{ev}}$, probada en Proposición 13.2.7 — La coincidencia eventual es una relación de equivalencia.

Así, para cada $\ell$,

$$
a_n\to\ell
\iff
b_n\to\ell.
$$

Si una de las sucesiones es convergente, la otra converge al mismo número real. La última igualdad se sigue entonces de la notación introducida en Notación 13.3.6 — Límite de una sucesión convergente. ∎

Esta proposición formaliza una de las ideas centrales del análisis secuencial:

$$
\boxed{
\text{un número finito de términos iniciales no altera la convergencia ni el límite}.
}
$$

El paso siguiente será introducir la **acotación de sucesiones reales** y demostrar que toda sucesión convergente es acotada. Ese resultado proporcionará la infraestructura necesaria para el producto de sucesiones convergentes y para los argumentos de compacidad secuencial posteriores.
---

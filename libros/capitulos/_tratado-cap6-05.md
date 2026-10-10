## 6.5. Extensión del producto a todos los signos {#sec-ta-6-5}

### Definición 6.5.1 — Cortaduras estrictamente negativas

Definimos

$$
\boxed{\mathbb R_D^{<0}:=\{\alpha\in\mathbb R_D:\alpha<_D0_D\}.}
$$

### Proposición 6.5.2 — Tricotomía respecto del cero

Para toda $\alpha\in\mathbb R_D$ ocurre exactamente una de las tres posibilidades

$$
\boxed{
\alpha<_D0_D,
\qquad
\alpha=0_D,
\qquad
0_D<_D\alpha.
}
$$

**Demostración.**

Es la tricotomía del orden estricto asociado al orden total $\le_D$ de Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras. ∎

### Lema 6.5.3 — El opuesto intercambia los signos

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{
\alpha<_D0_D\iff0_D<_D(-_D\alpha),
}
$$

$$
\boxed{
0_D<_D\alpha\iff-_D\alpha<_D0_D,
}
$$

y

$$
\boxed{-_D0_D=0_D.}
$$

**Demostración.**

Supongamos primero $\alpha<_D0_D$, es decir, $\alpha\subsetneq0_D$. Existe entonces $s\in0_D\setminus\alpha$. Como $s<0$, tenemos $0<-s$. El mismo $s$ muestra, por la definición del opuesto, que $0\in-_D\alpha$. Por Lema 6.4.2 — Caracterizaciones de la positividad, $-_D\alpha>_D0_D$.

Supongamos ahora $\alpha>_D0_D$. Entonces $0\in\alpha$, y existe $a\in\alpha$ con $a>0$. Si $q\in-_D\alpha$, existe $s\notin\alpha$ con $q<-s$. Como $0\in\alpha$ y $\alpha$ es inferior, un $s\le0$ pertenecería a $\alpha$; por tanto $s>0$. Así $q<-s<0$ y $-_D\alpha\subseteq0_D$. La inclusión es propia: $-a\in0_D$, pero $-a\notin-_D\alpha$, pues de $-a<-s$ se seguiría $s<a$ y luego $s\in\alpha$. Por tanto $-_D\alpha<_D0_D$.

Para las recíprocas no usamos ningún resultado posterior. Supongamos $-_D\alpha>_D0_D$. Por tricotomía de $\alpha$ respecto de $0_D$, si $\alpha=0_D$, Corolario 6.3.6 — El opuesto prolonga el opuesto racional da $-_D\alpha=0_D$, contradicción; si $\alpha>_D0_D$, la implicación ya demostrada daría $-_D\alpha<_D0_D$, también contradicción. Luego $\alpha<_D0_D$. El razonamiento para $-_D\alpha<_D0_D\Rightarrow\alpha>_D0_D$ es idéntico, descartando los otros dos casos por las implicaciones ya probadas.

Finalmente, Corolario 6.3.6 — El opuesto prolonga el opuesto racional aplicado a $p=0_{\mathbb Q}$ da $-_D0_D=0_D$. ∎

### Definición 6.5.4 — Producto signado candidato

Para $\alpha,\beta\in\mathbb R_D$ definimos

$$
\boxed{
M_D(\alpha,\beta)
=
\begin{cases}
0_D,&\alpha=0_D\text{ o }\beta=0_D,\\[1ex]
\alpha\cdot_D^+\beta,&\alpha>_D0_D,\ \beta>_D0_D,\\[1ex]
(-_D\alpha)\cdot_D^+(-_D\beta),&\alpha<_D0_D,\ \beta<_D0_D,\\[1ex]
-_D\bigl(\alpha\cdot_D^+(-_D\beta)\bigr),&\alpha>_D0_D>_D\beta,\\[1ex]
-_D\bigl((-_D\alpha)\cdot_D^+\beta\bigr),&\beta>_D0_D>_D\alpha.
\end{cases}
}
$$

Proposición 6.5.2 — Tricotomía respecto del cero hace los casos exhaustivos y disjuntos; Lema 6.5.3 — El opuesto intercambia los signos garantiza que cada aparición de $\cdot_D^+$ recibe argumentos positivos.

### Proposición 6.5.5 — Clausura y regla de signos del producto candidato

Para todos $\alpha,\beta\in\mathbb R_D$,

$$
\boxed{M_D(\alpha,\beta)\in\mathbb R_D.}
$$

Además, el producto es cero si alguno de los factores es cero, positivo si los dos factores no nulos tienen el mismo signo y negativo si tienen signos opuestos.

**Demostración.**

En el caso cero el resultado es $0_D$. Si ambos factores son positivos, Proposición 6.4.5 — El producto positivo es una cortadura positiva da un resultado positivo. Si ambos son negativos, sus opuestos son positivos por Lema 6.5.3 — El opuesto intercambia los signos, y el tercer caso de la definición vuelve a dar una cortadura positiva. Si los signos son opuestos, el producto positivo interno es positivo y su opuesto es negativo por Lema 6.5.3 — El opuesto intercambia los signos. ∎

### Definición 6.5.6 — Multiplicación de Dedekind

La construcción anterior determina una función

$$
\boxed{
\cdot_D:\mathbb R_D\times\mathbb R_D\longrightarrow\mathbb R_D,
\qquad
\alpha\cdot_D\beta:=M_D(\alpha,\beta).
}
$$

Si $\alpha,\beta>_D0_D$, entonces $\alpha\cdot_D\beta=\alpha\cdot_D^+\beta$.

> **Nota fundacional.** La operación $\cdot_D$ está perfectamente definida como función extensional en el marco clásico. Su definición por casos no es, sin información adicional, un algoritmo de signo sobre cortaduras arbitrarias:
> $$
> \boxed{
> \text{operación extensional}
> \neq
> \text{algoritmo sobre nombres efectivos}.
> }
> $$

### Proposición 6.5.7 — La multiplicación de Dedekind prolonga la multiplicación racional

Para $p,q\in\mathbb Q$,

$$
\boxed{\iota_D(pq)=\iota_D(p)\cdot_D\iota_D(q).}
$$

**Demostración.**

Si alguno de $p,q$ es cero, ambos miembros son $0_D$. Si ambos son positivos, la afirmación es Proposición 6.4.8 — El producto positivo prolonga el producto racional positivo.

Si $p,q<0$, entonces $-p,-q>0$ y

$$
\begin{aligned}
\iota_D(p)\cdot_D\iota_D(q)
&=(-_D\iota_D(p))\cdot_D^+(-_D\iota_D(q))\\
&=\iota_D(-p)\cdot_D^+\iota_D(-q)\\
&=\iota_D((-p)(-q))\\
&=\iota_D(pq).
\end{aligned}
$$

Si $p>0>q$, entonces

$$
\begin{aligned}
\iota_D(p)\cdot_D\iota_D(q)
&=-_D\bigl(\iota_D(p)\cdot_D^+\iota_D(-q)\bigr)\\
&=-_D\iota_D(p(-q))\\
&=\iota_D(-p(-q))\\
&=\iota_D(pq).
\end{aligned}
$$

El caso $q>0>p$ es simétrico por la propia definición signada. ∎

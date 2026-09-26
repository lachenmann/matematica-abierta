## 9.9. La copia canónica de los racionales {#sec-ta-9-9}

El cuerpo de Cauchy fue construido a partir de sucesiones racionales, pero eso no autoriza a identificar un racional con una clase de sucesiones. El objeto

$$
q\in\mathbb Q
$$

y la sucesión constante

$$
\underline q\in\mathbb Q^{\mathbb N}
$$

son de tipos distintos, y esta última, a su vez, es distinta de su clase

$$
[\underline q]_C\in\mathbb R_C.
$$

La relación entre ambos sistemas debe, por tanto, construirse mediante una función. La elección canónica es la que ya sugiere la interpretación de una sucesión constante: representar el racional $q$ por el proceso que permanece siempre igual a $q$.

### Definición 9.9.1 — Aplicación canónica de $\mathbb Q$ en $\mathbb R_C$

Para cada $q\in\mathbb Q$, la sucesión constante $\underline q$ pertenece a $\mathcal C_{\mathbb Q}$ por Proposición 8.4.4 — Las sucesiones constantes son de Cauchy. Por tanto su clase $[\underline q]_C$ pertenece a $\mathbb R_C$.

Definimos

$$
\boxed{
\iota_C:\mathbb Q\longrightarrow\mathbb R_C,
\qquad
\iota_C(q):=[\underline q]_C.
}
$$

Conjuntistamente, consideramos el grafo

$$
G_{\iota_C}
:=
\left\{
\langle q,x\rangle
\in
\mathbb Q\times\mathbb R_C:
 x=[\underline q]_C
\right\}.
$$

El producto cartesiano existe por Proposición 0.3.7 — Existencia del producto cartesiano y el subconjunto indicado existe por separación. Para cada $q\in\mathbb Q$ existe exactamente un $x\in\mathbb R_C$ que satisface la condición, a saber, la clase $[\underline q]_C$. Por la definición de función, $G_{\iota_C}$ es el grafo de una función con dominio $\mathbb Q$ y codominio $\mathbb R_C$.

> **Nota fundacional.** No se selecciona un representante de cada clase de $\mathbb R_C$. A cada racional fijo se le asigna determinísticamente su propia sucesión constante y luego la clase de esa sucesión. No interviene Choice.

### Proposición 9.9.2 — Igualdad de imágenes e inyectividad de $\iota_C$

Para cualesquiera $q,r\in\mathbb Q$,

$$
\boxed{
\iota_C(q)=\iota_C(r)
\iff
q=r.
}
$$

En particular, $\iota_C$ es inyectiva.

**Demostración.**

Supongamos primero

$$
\iota_C(q)=\iota_C(r).
$$

Por definición,

$$
[\underline q]_C=[\underline r]_C.
$$

El criterio de igualdad de clases Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy implica

$$
\underline q-\underline r
\in
\mathcal N_{\mathbb Q}.
$$

Por Proposición 8.1.5 — Compatibilidad de las sucesiones constantes con las operaciones puntuales,

$$
\underline q-\underline r
=
\underline{q-r}.
$$

La pertenencia a $\mathcal N_{\mathbb Q}$ significa, por definición, que

$$
\underline{q-r}{}_n
\to_{\mathbb Q}
0_{\mathbb Q}.
$$

Pero toda sucesión constante converge racionalmente a su valor (Proposición 8.3.4 — Las sucesiones constantes convergen a su valor), de modo que también

$$
\underline{q-r}{}_n
\to_{\mathbb Q}
q-r.
$$

La unicidad del límite racional Teorema 8.3.5 — Unicidad del límite racional da

$$
q-r=0_{\mathbb Q}.
$$

Por las leyes del grupo aditivo racional,

$$
q=r.
$$

Recíprocamente, si $q=r$, entonces $\underline q=\underline r$ y, por tanto,

$$
[\underline q]_C=[\underline r]_C,
$$

es decir,

$$
\iota_C(q)=\iota_C(r).
$$

La equivalencia queda demostrada, y su implicación directa es precisamente la inyectividad de $\iota_C$. ∎

> **Consecuencia tipológica.** Desde ahora podemos hablar de la copia canónica $\iota_C[\mathbb Q]$ dentro de $\mathbb R_C$, pero todavía no escribiremos $\mathbb Q\subseteq\mathbb R_C$: los racionales y sus imágenes siguen siendo objetos conjuntistas distintos.

### Proposición 9.9.3 — Preservación de la aritmética racional

Para todos $q,r\in\mathbb Q$ se tiene

$$
\boxed{
\iota_C(0_{\mathbb Q})=0_C,
\qquad
\iota_C(1_{\mathbb Q})=1_C,
}
$$

$$
\boxed{
\iota_C(q+r)
=
\iota_C(q)+\iota_C(r),
}
$$

$$
\boxed{
\iota_C(qr)
=
\iota_C(q)\,\iota_C(r),
}
$$

y

$$
\boxed{
\iota_C(-q)=-\iota_C(q).
}
$$

**Demostración.**

Las dos primeras identidades son inmediatas de las definiciones:

$$
\iota_C(0_{\mathbb Q})
=[\underline{0_{\mathbb Q}}]_C
=0_C,
$$

$$
\iota_C(1_{\mathbb Q})
=[\underline{1_{\mathbb Q}}]_C
=1_C.
$$

Para la suma, Proposición 8.1.5 — Compatibilidad de las sucesiones constantes con las operaciones puntuales da

$$
\underline{q+r}
=
\underline q+\underline r.
$$

Por la definición de la suma en el cociente,

$$
\begin{aligned}
\iota_C(q+r)
&=[\underline{q+r}]_C\\
&=[\underline q+\underline r]_C\\
&=[\underline q]_C+[\underline r]_C\\
&=\iota_C(q)+\iota_C(r).
\end{aligned}
$$

Del mismo modo,

$$
\underline{qr}
=
\underline q\,\underline r,
$$

y por tanto

$$
\begin{aligned}
\iota_C(qr)
&=[\underline{qr}]_C\\
&=[\underline q\,\underline r]_C\\
&=[\underline q]_C[\underline r]_C\\
&=\iota_C(q)\iota_C(r).
\end{aligned}
$$

Finalmente,

$$
\underline{-q}=-\underline q,
$$

de donde

$$
\begin{aligned}
\iota_C(-q)
&=[\underline{-q}]_C\\
&=[-\underline q]_C\\
&=-[\underline q]_C\\
&=-\iota_C(q).
\end{aligned}
$$

Todas las identidades provienen de operaciones término a término ya construidas y de sus operaciones inducidas en el cociente. ∎

### Corolario 9.9.4 — Compatibilidad con los recíprocos racionales

Si $q\in\mathbb Q$ y $q\neq0_{\mathbb Q}$, entonces

$$
\boxed{
\iota_C(q^{-1})
=
\iota_C(q)^{-1}.
}
$$

**Demostración.**

Sea $q\neq0_{\mathbb Q}$. Como $\iota_C(0_{\mathbb Q})=0_C$ y $\iota_C$ es inyectiva,

$$
\iota_C(q)\neq0_C.
$$

Por tanto $\iota_C(q)^{-1}$ está definido.

La ley del inverso racional da

$$
qq^{-1}=1_{\mathbb Q}.
$$

Aplicando la preservación del producto y de la unidad,

$$
\begin{aligned}
\iota_C(q)\,\iota_C(q^{-1})
&=\iota_C(qq^{-1})\\
&=\iota_C(1_{\mathbb Q})\\
&=1_C.
\end{aligned}
$$

Por otro lado, Proposición 9.7.9 — Ley del inverso multiplicativo en $\mathbb R_C$ da

$$
\iota_C(q)\,\iota_C(q)^{-1}=1_C.
$$

Usando asociatividad, conmutatividad y la unidad de Teorema 9.6.6 — $\mathbb R_C$ es un anillo conmutativo con identidad,

$$
\begin{aligned}
\iota_C(q^{-1})
&=1_C\,\iota_C(q^{-1})\\
&=\bigl(\iota_C(q)^{-1}\iota_C(q)\bigr)\iota_C(q^{-1})\\
&=\iota_C(q)^{-1}
   \bigl(\iota_C(q)\iota_C(q^{-1})\bigr)\\
&=\iota_C(q)^{-1}1_C\\
&=\iota_C(q)^{-1}.
\end{aligned}
$$

∎

### Proposición 9.9.5 — Preservación y reflexión del orden racional

Para cualesquiera $q,r\in\mathbb Q$,

$$
\boxed{
q<r
\iff
\iota_C(q)<_C\iota_C(r),
}
$$

y

$$
\boxed{
q\le r
\iff
\iota_C(q)\le_C\iota_C(r).
}
$$

**Demostración.**

Comenzamos con el orden estricto.

Supongamos

$$
q<r.
$$

Definamos explícitamente

$$
\delta:=\frac{r-q}{2_{\mathbb Q}}.
$$

Como $q<r$, tenemos $0<r-q$ y, por positividad de $2_{\mathbb Q}^{-1}$,

$$
0<\delta.
$$

Además,

$$
q<q+\delta<r.
$$

En particular,

$$
q+\delta<r.
$$

Para las sucesiones constantes, esto significa que, para todo $n\in\mathbb N$,

$$
\underline q_n+\delta
<
\underline r_n.
$$

Tomando $N=0$, el criterio Proposición 9.8.6 — Criterio de separación eventual para el orden estricto produce

$$
[\underline q]_C
<_C
[\underline r]_C,
$$

es decir,

$$
\iota_C(q)<_C\iota_C(r).
$$

Recíprocamente, supongamos

$$
\iota_C(q)<_C\iota_C(r).
$$

Por Proposición 9.8.6 — Criterio de separación eventual para el orden estricto, existen $\delta\in\mathbb Q$ y $N\in\mathbb N$ tales que

$$
0<\delta
$$

y, para todo $n\ge N$,

$$
\underline q_n+\delta
<
\underline r_n.
$$

Como $N\le N$, al tomar $n=N$ obtenemos

$$
q+\delta<r.
$$

De $0<\delta$, la compatibilidad del orden racional con la suma da

$$
q<q+\delta.
$$

Por transitividad,

$$
q<r.
$$

Así hemos demostrado

$$
q<r
\iff
\iota_C(q)<_C\iota_C(r).
$$

Pasemos al orden no estricto. Como el orden racional es total y $<$ es su orden estricto asociado,

$$
q\le r
\iff
(q<r\ \lor\ q=r).
$$

Del mismo modo, por Teorema 9.8.5 — $\le_C$ es un orden total,

$$
\iota_C(q)\le_C\iota_C(r)
\iff
\bigl(
\iota_C(q)<_C\iota_C(r)
\ \lor\\
\iota_C(q)=\iota_C(r)
\bigr).
$$

La equivalencia estricta recién demostrada y Proposición 9.9.2 — Igualdad de imágenes e inyectividad de $\iota_C$ transforman miembro a miembro la primera disyunción en la segunda. Por tanto

$$
q\le r
\iff
\iota_C(q)\le_C\iota_C(r).
$$

∎

### Lo que hemos ganado

La relación entre el sistema racional ya construido y el nuevo cuerpo de Cauchy está ahora expresada por una función canónica, no por una identificación conjuntista:

$$
\boxed{
\iota_C(q)=[\underline q]_C.
}
$$

La función es inyectiva, preserva $0$, $1$, suma, producto, opuestos y recíprocos cuando éstos existen, y preserva y refleja ambos órdenes:

$$
q\le r
\iff
\iota_C(q)\le_C\iota_C(r),
$$

$$
q<r
\iff
\iota_C(q)<_C\iota_C(r).
$$

Por ello, $\iota_C[\mathbb Q]$ es ya una copia algebraica y ordenada exacta de los racionales dentro del conjunto $\mathbb R_C$.

Hay, sin embargo, una última cautela deductiva. La definición general de incrustación de cuerpos ordenados (Definición 4.8.1 — Incrustación de cuerpos ordenados) exige que tanto el dominio como el codominio sean cuerpos ordenados. Ya sabemos que $\mathbb Q$ lo es y que $\mathbb R_C$ es un cuerpo provisto de un orden total, pero todavía no hemos demostrado que las operaciones de $\mathbb R_C$ sean compatibles con $\le_C$. Por esa razón no aplicaremos todavía formalmente esa denominación a $\iota_C$.

La tarea de §9.10 queda así aislada con precisión: demostrar la compatibilidad de $\le_C$ con la suma y con el producto de elementos no negativos. Una vez hecho esto, $\mathbb R_C$ será un cuerpo ordenado y los resultados de esta sección convertirán inmediatamente a $\iota_C$ en una incrustación de cuerpos ordenados.

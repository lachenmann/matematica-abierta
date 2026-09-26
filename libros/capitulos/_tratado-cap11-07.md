## 11.7. Sobreyectividad {#sec-ta-11-7}

La inyectividad demuestra que dos elementos distintos del modelo de Cauchy no pueden producir la misma cortadura. Falta la dirección opuesta: dada una cortadura arbitraria

$$
\alpha\in\mathbb R_D,
$$

debemos construir un elemento de $\mathbb R_C$ cuya imagen por $\Phi$ sea exactamente $\alpha$.

Aquí aparece un riesgo fundacional real. El lema de aproximación racional de la frontera (Lema 6.3.1 — Aproximación racional de la frontera) afirma que, para cada precisión racional positiva $h$, existe algún $a\in\alpha$ tal que $a+h\notin\alpha$. Elegir uno de esos $a$ para cada precisión de una sucesión produciría una familia numerable de elecciones. Aunque cada elección aislada es inocua, efectuar todas simultáneamente sin una regla definible introduciría precisamente la clase de Choice silencioso que el tratado ha evitado.

La solución ya está disponible en nuestra infraestructura: $e_{\mathbb Q}:\mathbb N\to\mathbb Q$ es una enumeración racional canónica y sobreyectiva. En vez de escoger un aproximante arbitrario, tomaremos el primero según esa enumeración que satisfaga la condición de frontera. El buen orden de $\mathbb N$ convierte así una existencia en una selección funcional determinada.

### Definición 11.7.1 — Selector canónico de frontera de Dedekind

Sean $\alpha\in\mathbb R_D$ y $h\in\mathbb Q$ con $0<h$. Consideremos

$$
K_D(\alpha,h)
:=
\left\{
k\in\mathbb N:
 e_{\mathbb Q}(k)\in\alpha
 \ \land\\
 e_{\mathbb Q}(k)+h\notin\alpha
\right\}.
$$

Por Lema 6.3.1 — Aproximación racional de la frontera existe $a\in\alpha$ tal que $a+h\notin\alpha$. Como $e_{\mathbb Q}$ es sobreyectiva por Proposición 10.2.6 — La enumeración racional es sobreyectiva, existe $k\in\mathbb N$ con

$$
e_{\mathbb Q}(k)=a,
$$

de modo que $k\in K_D(\alpha,h)$. Por el principio de buen orden Teorema 1.6.13 — Principio de buen orden, $K_D(\alpha,h)$ posee un elemento mínimo, y éste es único por Proposición 0.7.6 — Unicidad de máximo y mínimo. Denotemos localmente ese mínimo por $m_D(\alpha,h)$.

Definimos entonces

$$
\boxed{
\operatorname{sel}_D(\alpha,h)
:=
e_{\mathbb Q}\bigl(m_D(\alpha,h)\bigr)
\qquad(0<h).
}
$$

Para obtener una función total en la segunda variable, fijamos además

$$
\operatorname{sel}_D(\alpha,h):=0_{\mathbb Q}
\qquad(h\le 0_{\mathbb Q}).
$$

Así queda determinada una función

$$
\boxed{
\operatorname{sel}_D:
\mathbb R_D\times\mathbb Q
\longrightarrow
\mathbb Q.
}
$$

Conjuntistamente, los conjuntos $K_D(\alpha,h)$ se obtienen por Separación dentro de $\mathbb N$, y el grafo de $\operatorname{sel}_D$ se obtiene por Separación dentro de $(\mathbb R_D\times\mathbb Q)\times\mathbb Q$. La totalidad del orden racional separa de manera exhaustiva los casos $0<h$ y $h\le0$.

La definición no escoge un elemento de cada conjunto $K_D(\alpha,h)$: el buen orden de $\mathbb N$ determina un único índice mínimo. Ésta es la diferencia entre una familia de elecciones y un selector definible.

> **Nota fundacional.** La canonicidad anterior es extensional. Para una cortadura arbitraria no está disponible en general una decisión de
> $$ e_{\mathbb Q}(k)\in\alpha \quad\text{y}\quad e_{\mathbb Q}(k)+h\notin\alpha. $$
> Por tanto, que exista un índice mínimo único no implica que ese índice sea computablemente localizable. El selector resuelve el problema de Choice, no el de efectividad.

### Proposición 11.7.2 — Corrección del selector de frontera

Si $\alpha\in\mathbb R_D$ y $h\in\mathbb Q$ satisfacen $0<h$, entonces

$$
\boxed{
\operatorname{sel}_D(\alpha,h)\in\alpha
\qquad\text{y}\qquad
\operatorname{sel}_D(\alpha,h)+h\notin\alpha.
}
$$

**Demostración.**

Por Definición 11.7.1 — Selector canónico de frontera de Dedekind, el índice $m_D(\alpha,h)$ pertenece a $K_D(\alpha,h)$. Desplegando la definición de este conjunto,

$$
e_{\mathbb Q}\bigl(m_D(\alpha,h)\bigr)\in\alpha
$$

y

$$
e_{\mathbb Q}\bigl(m_D(\alpha,h)\bigr)+h\notin\alpha.
$$

Como

$$
\operatorname{sel}_D(\alpha,h)
=
e_{\mathbb Q}\bigl(m_D(\alpha,h)\bigr),
$$

se obtienen las dos afirmaciones. ∎

### Definición 11.7.3 — Sucesión canónica asociada a una cortadura

Para $n\in\mathbb N$ escribiremos localmente

$$
h_n
:=
\bigl(\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}\bigr)^{-1}.
$$

Es la misma función racional de precisión construida en Definición 10.3.1 — Escala racional canónica; usamos aquí la letra local $h$ para no reactivar fuera de su alcance la notación $\lambda_n$ del Capítulo 10.

Para cada $\alpha\in\mathbb R_D$ definimos la sucesión racional

$$
\boxed{
\operatorname{seq}_D(\alpha)
\in\mathbb Q^{\mathbb N},
\qquad
\bigl(\operatorname{seq}_D(\alpha)\bigr)_n
:=
\operatorname{sel}_D(\alpha,h_n).
}
$$

La funcionalidad de $\operatorname{sel}_D$ determina unívocamente todos los términos. Por tanto la asignación

$$
\boxed{
\operatorname{seq}_D:
\mathbb R_D\longrightarrow\mathbb Q^{\mathbb N}
}
$$

es una función. Su grafo puede obtenerse por Separación dentro de $\mathbb R_D\times\mathbb Q^{\mathbb N}$.

No se ha elegido una sucesión de aproximantes: cada término es el valor de una función previamente determinada. El grafo se obtiene por Separación dentro del producto ya existente; no se necesita Reemplazo en esta construcción concreta.

### Proposición 11.7.4 — La sucesión canónica es de Cauchy

Para toda cortadura $\alpha\in\mathbb R_D$,

$$
\boxed{
\operatorname{seq}_D(\alpha)
\in\mathcal C_{\mathbb Q}.
}
$$

**Demostración.**

Fijemos $\alpha\in\mathbb R_D$ y escribamos

$$
a_n:=\bigl(\operatorname{seq}_D(\alpha)\bigr)_n.
$$

La fórmula que define $h_n$ coincide con la escala de Definición 10.3.1 — Escala racional canónica; por Proposición 10.3.2 — Positividad y nulidad de la escala canónica,

$$
0<h_n
\qquad(n\in\mathbb N)
$$

y, para todo $\varepsilon\in\mathbb Q$ con $0<\varepsilon$, existe $N\in\mathbb N$ tal que

$$
N\le n
\Longrightarrow
h_n<\varepsilon.
$$

Por Proposición 11.7.2 — Corrección del selector de frontera, para todo $n$,

$$
a_n\in\alpha
\qquad\text{y}\qquad
a_n+h_n\notin\alpha.
$$

Sea ahora $\varepsilon>0$ racional y tomemos $N$ como arriba. Si $m,n\ge N$, entonces

$$
h_m<\varepsilon,
\qquad
h_n<\varepsilon.
$$

Como $a_m\in\alpha$ y $a_n+h_n\notin\alpha$, el lema Lema 6.1.1 — Todo punto exterior domina una cortadura aplicado al punto exterior $a_n+h_n$ da

$$
a_m<a_n+h_n,
$$

y por tanto

$$
a_m-a_n<h_n<\varepsilon.
$$

Intercambiando $m$ y $n$ obtenemos también

$$
a_n-a_m<h_m<\varepsilon.
$$

Equivalentemente,

$$
-\varepsilon<a_m-a_n<\varepsilon.
$$

Por la caracterización epsilon-local de la distancia racional Proposición 8.2.3 — Caracterización $\varepsilon$-local de la distancia racional,

$$
d_{\mathbb Q}(a_m,a_n)<\varepsilon.
$$

Esto vale para cualesquiera $m,n\ge N$. Por Definición 8.4.1 — Sucesión racional de Cauchy, $(a_n)$ es de Cauchy, y por Definición 8.4.2 — Conjunto de las sucesiones racionales de Cauchy,

$$
\operatorname{seq}_D(\alpha)\in\mathcal C_{\mathbb Q}.
$$

∎

### Proposición 11.7.5 — Recuperación exacta de la cortadura

Para toda $\alpha\in\mathbb R_D$,

$$
\boxed{
\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr)
=
\alpha.
}
$$

**Demostración.**

Fijemos $\alpha\in\mathbb R_D$ y pongamos

$$
a_n:=\bigl(\operatorname{seq}_D(\alpha)\bigr)_n.
$$

Por Proposición 11.7.4 — La sucesión canónica es de Cauchy, esta sucesión pertenece a $\mathcal C_{\mathbb Q}$, de modo que Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy puede aplicarse a ella.

Demostraremos las dos inclusiones.

**Primera inclusión: $\alpha\subseteq\mathcal L_C(\operatorname{seq}_D(\alpha))$.** Sea $q\in\alpha$. Como una cortadura no tiene máximo, Definición 5.1.1 — Cortadura de Dedekind proporciona localmente un racional $r\in\alpha$ tal que

$$
q<r.
$$

Definamos

$$
\varepsilon
:=
\frac{r-q}{2_{\mathbb Q}}.
$$

Entonces

$$
0<\varepsilon
$$

y

$$
r-\varepsilon=q+\varepsilon.
$$

Por la nulidad de la escala explícita, Proposición 10.3.2 — Positividad y nulidad de la escala canónica proporciona $N\in\mathbb N$ tal que, para todo $n\ge N$,

$$
h_n<\varepsilon.
$$

Fijemos uno de esos $n$. Por Proposición 11.7.2 — Corrección del selector de frontera,

$$
a_n+h_n\notin\alpha.
$$

Como $r\in\alpha$, Lema 6.1.1 — Todo punto exterior domina una cortadura aplicado al punto exterior $a_n+h_n$ da

$$
r<a_n+h_n.
$$

Restando $h_n$ y usando $h_n<\varepsilon$,

$$
a_n>r-h_n>r-\varepsilon=q+\varepsilon.
$$

Por tanto, para todo $n\ge N$,

$$
q+\varepsilon<a_n.
$$

La definición Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy implica

$$
q\in\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr).
$$

**Segunda inclusión: $\mathcal L_C(\operatorname{seq}_D(\alpha))\subseteq\alpha$.** Sea

$$
q\in\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr).
$$

Por Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy, existen $\varepsilon>0$ y $N\in\mathbb N$ tales que

$$
q+\varepsilon<a_n
$$

para todo $n\ge N$. En particular,

$$
q<a_N.
$$

Por Proposición 11.7.2 — Corrección del selector de frontera,

$$
a_N\in\alpha.
$$

Como $\alpha$ es cerrada hacia abajo (Definición 5.1.1 — Cortadura de Dedekind),

$$
q<a_N\in\alpha
\Longrightarrow
q\in\alpha.
$$

Así

$$
\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr)
\subseteq
\alpha.
$$

Por extensionalidad (Teorema 0.2.4 — Criterio extensional por doble inclusión),

$$
\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr)
=
\alpha.
$$

∎

> **Nota fundacional.** La segunda inclusión ya no se prueba por contrapositiva. Una vez construida la sucesión canónica, la recuperación de la cortadura usa directamente un término interior $a_N$ y la clausura inferior. La clasicidad de la dirección Dedekind $\to$ Cauchy permanece concentrada en la construcción previa de Definición 11.7.1 — Selector canónico de frontera de Dedekind, no en esta recuperación.
>

### Teorema 11.7.6 — Sobreyectividad de $\Phi$

La aplicación

$$
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
$$

es sobreyectiva. Más precisamente, para cada $\alpha\in\mathbb R_D$ el elemento

$$
\boxed{
x_\alpha
:=
\left[\operatorname{seq}_D(\alpha)\right]_C
\in\mathbb R_C
}
$$

satisface

$$
\boxed{
\Phi(x_\alpha)=\alpha.
}
$$

**Demostración.**

Sea $\alpha\in\mathbb R_D$. Por Proposición 11.7.4 — La sucesión canónica es de Cauchy,

$$
\operatorname{seq}_D(\alpha)\in\mathcal C_{\mathbb Q},
$$

de modo que su clase

$$
x_\alpha
=
\left[\operatorname{seq}_D(\alpha)\right]_C
$$

pertenece a $\mathbb R_C$.

La fórmula característica de $\Phi$ sobre clases de Cauchy (Proposición 11.3.2 — Caracterización universal de $\Phi$) da

$$
\Phi(x_\alpha)
=
\mathcal L_C\bigl(\operatorname{seq}_D(\alpha)\bigr).
$$

Por Proposición 11.7.5 — Recuperación exacta de la cortadura, el miembro derecho es exactamente $\alpha$. Por tanto

$$
\Phi(x_\alpha)=\alpha.
$$

Como $\alpha$ era arbitraria, todo elemento de $\mathbb R_D$ posee una preimagen. Por Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad, $\Phi$ es sobreyectiva. ∎

### Corolario 11.7.7 — Biyectividad de la aplicación canónica

La aplicación canónica

$$
\boxed{
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
\text{ es biyectiva.}
}
$$

**Demostración.**

Proposición 11.6.1 — Igualdad de imágenes e inyectividad de $\Phi$ demuestra que $\Phi$ es inyectiva y Teorema 11.7.6 — Sobreyectividad de $\Phi$ demuestra que es sobreyectiva. Por Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad, es biyectiva. ∎

La comparación ha alcanzado ahora un punto decisivo: $\Phi$ preserva suma, producto y orden, y además establece una correspondencia uno a uno y sobre entre los dos conjuntos subyacentes. Seguimos sin identificarlos literalmente: una clase de sucesiones de Cauchy continúa siendo un objeto conjuntista distinto de una cortadura de Dedekind.

Aunque la biyectividad ya permitiría considerar la función inversa mediante Teorema 0.6.7 — Caracterización de las funciones invertibles, no necesitaremos todavía activar una notación nueva para ella. Mantendremos Notación 11.9.2 — Inversa de la comparación canónica libre hasta la conclusión estructural del capítulo, donde el isomorfismo completo será empaquetado formalmente.

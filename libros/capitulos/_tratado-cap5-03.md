## 5.3. Una cortadura que no proviene de ningún racional {#sec-ta-5-3}

Las secciones $\delta_q$ muestran que todo racional determina una cortadura. Pero eso no demuestra todavía que $\mathbb R_D$ sea una ampliación genuina de $\mathbb Q$. Podría ocurrir, en principio, que toda cortadura fuera de la forma

$$
\delta_q=\{r\in\mathbb Q:r<q\}.
$$

El conjunto $S_2$ construido en el Capítulo 3 proporciona precisamente el contraejemplo que necesitamos:

$$
S_2
=
\{q\in\mathbb Q:0_{\mathbb Q}\leq q\ \text{y}\ q^2<2_{\mathbb Q}\}.
$$

Sabemos que $S_2$ es no vacío y está acotado superiormente, pero no posee supremo en $\mathbb Q$. Sin embargo, $S_2$ por sí solo no es la forma adecuada de una cortadura: sólo contiene racionales no negativos. Una sección inferior asociada a una frontera positiva debe contener también todos los racionales negativos.

Esto sugiere completar $S_2$ hacia abajo.

### Definición 5.3.1 — Cortadura cuadrática asociada a $2$

Definimos

$$
\boxed{
\alpha_2
:=
\{q\in\mathbb Q:q<0_{\mathbb Q}\ \text{o}\ q\in S_2\}.
}
$$

El conjunto existe por Separación sobre $\mathbb Q$.

Utilizando la definición de $S_2$, podemos escribir equivalentemente

$$
\alpha_2
=
\left\{
q\in\mathbb Q:
q<0_{\mathbb Q}
\ \text{o}\\
\bigl(0_{\mathbb Q}\leq q\ \text{y}\ q^2<2_{\mathbb Q}\bigr)
\right\}.
$$

No hemos introducido ningún número llamado $\sqrt2$. El objeto $\alpha_2$ está definido enteramente mediante racionales y relaciones ya construidas.

Además, la pertenencia a $\alpha_2$ es decidible sobre nombres racionales. En efecto, Proposición 3.7.6 — Tricotomía decidible de los racionales permite decidir el signo de $q$, y la aritmética y el orden de $\mathbb Q$ permiten decidir $q^2<2$. Por tanto
$$
\boxed{
q\in\alpha_2
}
$$
es un predicado decidible para cada $q\in\mathbb Q$. La futura dificultad efectiva de la construcción de Dedekind no reside en esta cortadura concreta, sino en la totalidad de todas las cortaduras.

### Proposición 5.3.2 — $\alpha_2$ es una cortadura de Dedekind

Se tiene

$$
\boxed{
\alpha_2\in\mathbb R_D.
}
$$

**Demostración.**

Verificaremos directamente las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind.

**Habitabilidad.** Se tiene $0_{\mathbb Q}\in\alpha_2$, pues

$$
0_{\mathbb Q}\leq0_{\mathbb Q},
\qquad
0_{\mathbb Q}^2=0_{\mathbb Q}<2_{\mathbb Q}.
$$

En particular, $\alpha_2\neq\varnothing$.

**Propiedad.** El racional $2_{\mathbb Q}$ no pertenece a $\alpha_2$: es positivo y

$$
2_{\mathbb Q}^2=4_{\mathbb Q}\not<2_{\mathbb Q}.
$$

Por tanto $\alpha_2\neq\mathbb Q$.

**Clausura inferior.** Sean $q\in\alpha_2$ y $r<q$. Si $q<0_{\mathbb Q}$, entonces $r<0_{\mathbb Q}$ y $r\in\alpha_2$. Supongamos ahora

$$
0_{\mathbb Q}\leq q,
\qquad
q^2<2_{\mathbb Q}.
$$

La comparación racional decidible Proposición 3.7.6 — Tricotomía decidible de los racionales permite separar $r<0$ de $0\leq r$. En el primer caso $r\in\alpha_2$. En el segundo,

$$
0\leq r<q,
$$

y la estricta monotonía del cuadrado sobre los racionales no negativos (Lema 3.9.6 — Estricta monotonía del cuadrado en los racionales no negativos) da

$$
r^2<q^2<2.
$$

Luego $r\in\alpha_2$.

**Ausencia de máximo.** Sea $q\in\alpha_2$. Si $q<0$, la densidad racional proporciona $r$ con

$$
q<r<0,
$$

y entonces $r\in\alpha_2$.

Supongamos ahora $0\leq q$ y $q^2<2$. Definimos

$$
d:=2-q^2>0,
\qquad
h:=\frac{d}{2(2q+1)}>0,
\qquad
r:=q+h.
$$

Como $q\geq0$, tenemos $2(2q+1)\geq2$ y, puesto que $0<d\leq2$, resulta $0<h\leq1$. En particular,

$$
h^2\leq h.
$$

Por tanto

$$
2qh+h^2
\leq
(2q+1)h
=
\frac d2
<d.
$$

Así,

$$
r^2
=(q+h)^2
=q^2+2qh+h^2
<q^2+d
=2.
$$

Además $q<r$ y $0<r$, de modo que $r\in\alpha_2$. Por consiguiente $\alpha_2$ no posee máximo.

Se cumplen las cuatro condiciones de Definición 5.1.1 — Cortadura de Dedekind; por Definición 5.1.3 — Conjunto subyacente del modelo de Dedekind,

$$
\boxed{\alpha_2\in\mathbb R_D.}
$$

∎

La demostración es completamente local: ya no depende de la inexistencia de un supremo racional para $S_2$.

### Proposición 5.3.3 — $\alpha_2$ no es una cortadura racional

No existe $a\in\mathbb Q$ tal que

$$
\boxed{
\alpha_2=\delta_a.
}
$$

**Demostración.**

Sea $a\in\mathbb Q$. Demostraremos directamente que $\alpha_2\neq\delta_a$.

Si $a\leq0$, entonces $0\in\alpha_2$, mientras que

$$
0\notin\delta_a,
$$

pues $0<a$ es falso.

Supongamos ahora $0<a$. Por la decidibilidad del orden racional aplicada a $a^2$ y $2$, y por Teorema 3.9.5 — No existe una raíz cuadrada racional de $2$, que excluye $a^2=2$, quedan exactamente dos posibilidades.

**Caso 1: $a^2<2$.** Entonces $a\in\alpha_2$, pero por irreflexividad

$$
a\notin\delta_a.
$$

**Caso 2: $2<a^2$.** Pongamos

$$
d:=a^2-2>0,
\qquad
h:=\frac{d}{2(2a+1)}>0,
\qquad
b:=a-h.
$$

Como

$$
d=a^2-2<a^2<a(2a+1),
$$

obtenemos $h<a/2<a$, de modo que

$$
0<b<a.
$$

Además

$$
2ah=\frac{ad}{2a+1}<d.
$$

Por tanto

$$
b^2
=(a-h)^2
=a^2-2ah+h^2
>a^2-d
=2.
$$

Así $b<a$, luego $b\in\delta_a$, pero $b>0$ y $b^2>2$, por lo que $b\notin\alpha_2$.

En todos los casos existe un racional que distingue $\alpha_2$ de $\delta_a$. Como $a$ era arbitrario,

$$
\boxed{
\forall a\in\mathbb Q,\qquad \alpha_2\neq\delta_a.
}
$$

∎

La no racionalidad de $\alpha_2$ queda así reducida a la irracionalidad racional de $\sqrt2$ y a perturbaciones racionales explícitas; no utiliza teoría de supremos.

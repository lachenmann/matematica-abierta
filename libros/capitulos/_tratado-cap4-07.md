## 4.7. Formulaciones equivalentes de completitud {#sec-ta-4-7}

La propiedad del supremo no es la única manera puramente ordenada de expresar que no existen huecos. En este punto ya disponemos de suficiente teoría para demostrar dos equivalencias que no requieren todavía sucesiones ni límites.

### Definición 4.7.1 — Propiedad de separación {#ta-propiedad-separacion}

Diremos que un cuerpo ordenado $F$ tiene la **propiedad de separación** si, siempre que $A,B\subseteq F$ sean no vacíos y satisfagan

$$
a\leq b
\qquad
\text{para todo }a\in A,\ b\in B,
$$

existe $c\in F$ tal que

$$
a\leq c\leq b
\qquad
\text{para todo }a\in A,\ b\in B.
$$

No llamamos todavía a $(A,B)$ una cortadura. La definición formal de cortadura de Dedekind se reservará para el capítulo siguiente.

> **Forma positiva auditada.** Si, además de las condiciones anteriores, se suministran testigos $a_0\in A$ y $b_0\in B$, la propiedad se lee como una afirmación completamente positiva sobre dos conjuntos habitados. Ésta es la interfaz que utilizaremos cuando importe distinguir constructividad de mera no vaciedad clásica.

### Teorema 4.7.2 — Equivalencia entre propiedad del supremo y separación {#ta-supremo-equivale-separacion}

Para un cuerpo ordenado $F$, son equivalentes:

1. $F$ tiene la propiedad del supremo;
2. $F$ tiene la propiedad de separación.

**Demostración.**

Supongamos primero la propiedad del supremo. Sean $A,B$ no vacíos con $a\leq b$ para todo $a\in A$ y $b\in B$. En la formulación positiva, fijemos un testigo $b_0\in B$; en la base clásica actual este testigo se obtiene de la no vaciedad. Entonces $b_0$ es una cota superior de $A$, de modo que existe

$$
c:=\sup A.
$$

Por definición de supremo, $a\leq c$ para todo $a\in A$. Además cada $b\in B$ es cota superior de $A$, por lo que $c\leq b$. Así $c$ separa $A$ y $B$.

Recíprocamente, supongamos la propiedad de separación. Sea $A\subseteq F$ no vacío y acotado superiormente. Sea

$$
U:=\{u\in F:\forall a\in A\;(a\leq u)\}
$$

el conjunto de cotas superiores de $A$. La hipótesis «acotado superiormente» proporciona positivamente al menos una cota, de modo que $U$ está habitado. Por definición,

$$
a\leq u
$$

para todo $a\in A$ y $u\in U$. La propiedad de separación proporciona $c\in F$ tal que

$$
a\leq c\leq u
$$

para todo $a\in A$ y $u\in U$.

La primera desigualdad dice que $c$ es cota superior de $A$; la segunda, que $c$ es menor o igual que cualquier cota superior. Por tanto

$$
c=\sup A.
$$

Así $F$ tiene la propiedad del supremo. ∎

> **Nota fundacional.** Una vez suministrados testigos de habitabilidad para los conjuntos que el enunciado clásico llama «no vacíos», el mecanismo matemático de la equivalencia es constructivamente compatible. La única clasicidad aquí registrada procede de convertir no vaciedad negativa en datos positivos.

### Definición 4.7.3 — Principio de intersección de intervalos cerrados {#ta-principio-interseccion-intervalos-cerrados}

Diremos que un cuerpo ordenado $F$ satisface el **principio de intersección de intervalos cerrados** si para todo conjunto no vacío $I$ y toda pareja de familias

$$
(a_i)_{i\in I},
\qquad
(b_i)_{i\in I}
$$

de elementos de $F$ tales que

$$
a_i\leq b_j
\qquad
\text{para todos }i,j\in I,
$$

se tiene

$$
\boxed{
\bigcap_{i\in I}[a_i,b_i]\neq\varnothing.
}
$$

La hipótesis cruzada $a_i\leq b_j$ es deliberadamente más fuerte que exigir únicamente $a_i\leq b_i$: garantiza que todos los extremos izquierdos quedan a la izquierda de todos los extremos derechos.

> **Forma positiva auditada.** La conclusión anterior puede expresarse sin negación como
> $$
> \boxed{
> \exists c\in F\;\forall i\in I,
> \quad a_i\leq c\leq b_i.
> }
> $$
> Si además $I$ viene con un testigo $i_0\in I$, esta formulación evita convertir una mera no vaciedad en un índice concreto.

### Teorema 4.7.4 — Equivalencia con el principio de intersección de intervalos {#ta-completitud-equivale-interseccion-intervalos}

Para un cuerpo ordenado $F$, son equivalentes:

1. $F$ es completo;
2. $F$ satisface el [principio de intersección de intervalos cerrados](#ta-principio-interseccion-intervalos-cerrados).

**Demostración.**

Supongamos que $F$ es completo. Sean $I$, $(a_i)$ y $(b_i)$ como en la [Definición 4.7.3](#ta-principio-interseccion-intervalos-cerrados). Las imágenes

$$
A:=\{a_i:i\in I\},
\qquad
B:=\{b_i:i\in I\}
$$

existen por separación dentro de $F$. En la forma positiva, un testigo $i_0\in I$ produce directamente $a_{i_0}\in A$ y $b_{i_0}\in B$. La hipótesis cruzada implica $a\leq b$ para todo $a\in A$ y $b\in B$. Por el [Teorema 4.7.2](#ta-supremo-equivale-separacion) existe $c\in F$ con

$$
a_i\leq c\leq b_i
$$

para todo $i\in I$. Por tanto

$$
c\in\bigcap_{i\in I}[a_i,b_i].
$$

Recíprocamente, supongamos el principio de intersección. Para demostrar completitud basta, por el [Teorema 4.7.2](#ta-supremo-equivale-separacion), demostrar la propiedad de separación. Sean $A,B\subseteq F$ no vacíos con $a\leq b$ para todos $a\in A$ y $b\in B$.

En la forma positiva, fijemos testigos $a_0\in A$ y $b_0\in B$. Entonces

$$
I:=A\times B
$$

está habitado por $(a_0,b_0)$. Para $i=(a,b)\in I$ definimos

$$
\alpha_i:=a,
\qquad
\beta_i:=b.
$$

Si $i=(a,b)$ y $j=(a',b')$, la hipótesis de separación da

$$
\alpha_i=a\leq b'=\beta_j.
$$

Por el principio de intersección existe

$$
c\in\bigcap_{i\in I}[\alpha_i,\beta_i].
$$

Para cada $a\in A$, el índice $(a,b_0)\in I$ da $a\leq c$; para cada $b\in B$, el índice $(a_0,b)\in I$ da $c\leq b$. Así $c$ separa $A$ y $B$.

Por el [Teorema 4.7.2](#ta-supremo-equivale-separacion), $F$ es completo. ∎

> **Nota fundacional.** La prueba no construye una función de elección sobre una familia. Sólo utiliza los testigos globales de habitabilidad de $I$ o de $A,B$. En la formulación original por «no vacío», la obtención de esos testigos pertenece a la lógica clásica ambiente.

### Corolario 4.7.5 — Cuatro formulaciones de completitud disponibles en esta etapa {#ta-cuatro-formulaciones-completitud}

Para un cuerpo ordenado $F$, son equivalentes en el desarrollo actual:

1. todo subconjunto no vacío y acotado superiormente posee supremo;
2. todo subconjunto no vacío y acotado inferiormente posee ínfimo;
3. $F$ tiene la propiedad de separación;
4. $F$ satisface el principio de intersección de intervalos cerrados de la [Definición 4.7.3](#ta-principio-interseccion-intervalos-cerrados).

**Demostración.**

Las equivalencias entre $1$, $3$ y $4$ son los [Teoremas 4.7.2](#ta-supremo-equivale-separacion) y [4.7.4](#ta-completitud-equivale-interseccion-intervalos). La [Proposición 4.6.2](#ta-supremo-implica-infimo) da $(1)\Rightarrow(2)$.

Para probar $(2)\Rightarrow(1)$, supongamos que todo subconjunto no vacío y acotado inferiormente posee ínfimo. Sea $A\subseteq F$ no vacío y acotado superiormente. Entonces

$$
-A=\{-a:a\in A\}
$$

es no vacío y está acotado inferiormente: si $u$ es una cota superior de $A$, entonces $-u\leq-a$ para todo $a\in A$. Existe, pues,

$$
t:=\inf(-A).
$$

Para todo $a\in A$, $t\leq-a$, luego $a\leq-t$; así $-t$ es cota superior de $A$. Si $v$ es otra cota superior de $A$, entonces $-v$ es cota inferior de $-A$, por lo que $-v\leq t$, y al invertir signos obtenemos $-t\leq v$. Por tanto

$$
-t=\sup A.
$$

Así $2$ implica $1$, y las cuatro condiciones son equivalentes. ∎

No incluimos todavía equivalencias formuladas mediante sucesiones monótonas, sucesiones de Cauchy o convergencia de intervalos encajados con longitudes tendiendo a cero. Esas formulaciones exigen conceptos que aún no han sido construidos y serán incorporadas en el momento deductivamente correcto.

---

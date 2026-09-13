## Supremo {#gl-supremo}

**Idea.** La menor de todas las cotas superiores de un subconjunto.

**En este tratado.** Si $S\subseteq A$, un elemento $u\in A$ es el **supremo** de $S$ si es cota superior de $S$ y toda cota superior $v$ satisface

$$
u\leq v.
$$

La definición no garantiza existencia. Sólo cuando ésta haya sido demostrada escribiremos $\sup S$.

**En el Tratado:** [Definición 0.7.7 — Supremo e ínfimo](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-supremo-infimo) y [Corolario 0.7.9 — Notación legítima](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-notacion-sup-inf).

**Véase también:** [Cota superior](#gl-cota-superior), [Máximo](#gl-maximo), [Ínfimo](#gl-infimo).

---

## Axioma de infinito {#gl-axioma-infinito}

**Idea.** El principio de ZF que garantiza que existe un conjunto suficientemente grande para iniciar una construcción infinita cerrada bajo sucesores.

**En este tratado.** El axioma de infinito pertenece al fundamento admitido de ZF. Una vez definidos $0:=\varnothing$ y $S(x):=x\cup\{x\}$, garantiza la existencia de al menos un conjunto $I$ tal que

$$
0\in I
\qquad\text{y}\qquad
x\in I\Rightarrow S(x)\in I.
$$

**En el Tratado:** [inventario axiomático del Capítulo 0](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-zf) y [Proposición 1.1.4 — Existencia de un conjunto inductivo](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-existencia-conjunto-inductivo).

**Véase también:** [Conjunto inductivo](#gl-conjunto-inductivo), [Sucesor](#gl-sucesor), [$\omega$](#gl-omega).

---

## Cero {#gl-cero}

**Idea.** El primer número natural, representado conjuntistamente por el conjunto vacío.

**En este tratado.** Se define

$$
0:=\varnothing.
$$

La identificación no presupone aritmética: es la primera convención numérica después de haber construido previamente el conjunto vacío.

**En el Tratado:** [Notación 1.1.1 — Cero](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-cero).

**Véase también:** [Conjunto vacío](#gl-conjunto-vacio), [Sucesor](#gl-sucesor), [Números naturales](#gl-numeros-naturales).

---

## Conjunto inductivo {#gl-conjunto-inductivo}

**Idea.** Un conjunto que contiene el punto inicial $0$ y permanece cerrado al pasar de un elemento a su sucesor.

**En este tratado.** Un conjunto $I$ es **inductivo** si

$$
0\in I
$$

y, para todo $x$,

$$
x\in I\Rightarrow S(x)\in I.
$$

**En el Tratado:** [Definición 1.1.3 — Conjunto inductivo](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-conjunto-inductivo).

**Véase también:** [Axioma de infinito](#gl-axioma-infinito), [Núcleo inductivo](#gl-nucleo-inductivo), [Principio de inducción](#gl-principio-induccion).

---

## Núcleo inductivo {#gl-nucleo-inductivo}

**Idea.** La parte mínima de un conjunto inductivo que está forzada por contener $0$ y ser cerrada bajo sucesor.

**En este tratado.** Si $I$ es inductivo,

$$
\omega_I:=\{x\in I:\forall J\,[(J\subseteq I\text{ y }J\text{ inductivo})\Rightarrow x\in J]\}.
$$

Se demuestra que $\omega_I$ es inductivo, está contenido en todo conjunto inductivo y no depende del conjunto inductivo ambiente elegido.

**En el Tratado:** [Definición 1.1.5 — Núcleo inductivo](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-nucleo-inductivo), [Teorema 1.1.7 — Minimalidad](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-minimalidad-omega) y [Teorema 1.1.8 — Independencia](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-independencia-omega).

**Véase también:** [Conjunto inductivo](#gl-conjunto-inductivo), [$\omega$](#gl-omega), [Números naturales](#gl-numeros-naturales).

---

## Números naturales {#gl-numeros-naturales}

**Idea.** El sistema numérico generado canónicamente desde $0$ mediante sucesores.

**En este tratado.** Los naturales no se presuponen ni se postulan mediante axiomas de Peano. Se construyen en ZF definiendo

$$
\mathbb N:=\omega,
$$

donde $\omega$ es el núcleo inductivo canónico contenido en todo conjunto inductivo.

**En el Tratado:** [Notación 1.1.9 — $\omega$ y $\mathbb N$](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-omega-naturales).

**Véase también:** [$\omega$](#gl-omega), [Cero](#gl-cero), [Sucesor](#gl-sucesor), [Principio de inducción](#gl-principio-induccion).

---

## $\omega$ {#gl-omega}

**Idea.** El menor conjunto inductivo: contiene exactamente lo que cualquier construcción inductiva está obligada a contener.

**En este tratado.** Para cada conjunto inductivo $I$ se construye $\omega_I$ y se demuestra que todos esos núcleos coinciden. El conjunto común se denota por $\omega$ y se adopta

$$
\mathbb N:=\omega.
$$

**En el Tratado:** [Teorema 1.1.8 — Independencia del conjunto inductivo inicial](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-independencia-omega) y [Notación 1.1.9 — $\omega$ y $\mathbb N$](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-omega-naturales).

**Véase también:** [Núcleo inductivo](#gl-nucleo-inductivo), [Números naturales](#gl-numeros-naturales), [Principio de inducción](#gl-principio-induccion).

---

## Principio de inducción {#gl-principio-induccion}

**Idea.** Para probar una propiedad de todos los naturales basta verificarla en $0$ y demostrar que pasa de cada natural a su sucesor.

**En este tratado.** Si $A\subseteq\mathbb N$, $0\in A$ y

$$
n\in A\Rightarrow S(n)\in A,
$$

entonces $A=\mathbb N$. La forma usual para propiedades se obtiene aplicando este resultado al conjunto $\{n\in\mathbb N:P(n)\}$.

**En el Tratado:** [Teorema 1.1.10 — Principio de inducción](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-principio-induccion).

**Véase también:** [Conjunto inductivo](#gl-conjunto-inductivo), [$\omega$](#gl-omega), [Números naturales](#gl-numeros-naturales).

---

## Sucesor {#gl-sucesor}

**Idea.** La operación que produce el siguiente estadio de la construcción de von Neumann.

**En este tratado.** Para todo conjunto $x$,

$$
S(x):=x\cup\{x\}.
$$

En particular, $x\in S(x)$. Esta operación permite formular la noción de conjunto inductivo y, posteriormente, la estructura aritmética de $\mathbb N$.

**En el Tratado:** [Definición 1.1.2 — Sucesor](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-sucesor).

**Véase también:** [Cero](#gl-cero), [Conjunto inductivo](#gl-conjunto-inductivo), [Números naturales](#gl-numeros-naturales).

---

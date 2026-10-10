## Cuerpo {#gl-cuerpo}

**Idea.** Es una estructura algebraica en la que pueden realizarse suma, resta, multiplicación y división por elementos no nulos sin salir del sistema.

**En este tratado.** Un cuerpo es un anillo conmutativo $F$ con $0_F\neq1_F$ tal que todo elemento no nulo posee un inverso multiplicativo. En §3.6 se demuestra que

$$
(\mathbb Q,+,\cdot,0_{\mathbb Q},1_{\mathbb Q})
$$

satisface estas condiciones.

**En el Tratado:** [Convención 3.6.7 — Terminología de cuerpo](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-convencion-cuerpo) y [Teorema 3.6.8 — $\mathbb Q$ es un cuerpo](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-q-es-cuerpo).

**Véase también:** [Anillo conmutativo](#gl-anillo-conmutativo), [Recíproco racional](#gl-reciproco-racional), [División racional](#gl-division-racional).

---

## División racional {#gl-division-racional}

**Idea.** Dividir por un racional no nulo equivale a multiplicar por su recíproco.

**En este tratado.** Para $x\in\mathbb Q$ y $y\in\mathbb Q_{\neq0}$ se define

$$
\boxed{
\frac{x}{y}:=xy^{-1}.
}
$$

Esta definición se demuestra compatible con la notación fraccionaria $a/b$ usada para las clases racionales.

**En el Tratado:** [Definición 3.6.6 — División racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-division-racional).

**Véase también:** [Recíproco racional](#gl-reciproco-racional), [Notación fraccionaria](#gl-notacion-fraccionaria), [Cuerpo](#gl-cuerpo).

---

## Racionales no nulos {#gl-racionales-no-nulos}

**Idea.** Son los números racionales distintos de cero, precisamente aquellos para los que puede definirse un recíproco.

**En este tratado.** Se define

$$
\boxed{
\mathbb Q_{\neq0}
:=
\{q\in\mathbb Q:q\neq0_{\mathbb Q}\}.
}
$$

El criterio de nulidad demuestra que una fracción $a/b$ pertenece a $\mathbb Q_{\neq0}$ exactamente cuando $a\neq0_{\mathbb Z}$.

**En el Tratado:** [Definición 3.6.2 — Racionales no nulos](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-racionales-no-nulos) y [Proposición 3.6.1 — Criterio de nulidad de una fracción](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-criterio-nulidad-fraccion).

**Véase también:** [Número racional](#gl-numero-racional), [Cero racional](#gl-cero-racional), [Recíproco racional](#gl-reciproco-racional).

---

## Recíproco racional {#gl-reciproco-racional}

**Idea.** El recíproco de un racional no nulo es el elemento que, al multiplicarse por él, produce la unidad racional.

**En este tratado.** Para $q\in\mathbb Q_{\neq0}$ se define $q^{-1}$ mediante la única función bien definida que satisface

$$
\boxed{
\left(\frac ab\right)^{-1}
=
\frac ba
}
$$

cuando $a,b\neq0$. Se demuestra que

$$
qq^{-1}=1_{\mathbb Q}=q^{-1}q.
$$

**En el Tratado:** [Proposición 3.6.3 — Construcción del recíproco](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-construccion-reciproco), [Notación 3.6.4](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-reciproco-racional) y [Proposición 3.6.5](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-ley-inverso-multiplicativo-racional).

**Véase también:** [Racionales no nulos](#gl-racionales-no-nulos), [Unidad racional](#gl-unidad-racional), [División racional](#gl-division-racional), [Cuerpo](#gl-cuerpo).

---

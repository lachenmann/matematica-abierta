## Orden entero {#gl-orden-entero}

**Idea.** El orden de los enteros se construye a partir de la estructura aditiva ya disponible: $x$ precede a $y$ cuando $y$ se obtiene sumando a $x$ la imagen de algún natural.

**En este tratado.** Para $x,y\in\mathbb Z$,

$$
\boxed{
x\leq_{\mathbb Z} y
\iff
\exists n\in\mathbb N\;\bigl(y=x+\iota(n)\bigr).
}
$$

Sobre representantes, esta definición equivale a

$$
[(a,b)]\leq_{\mathbb Z}[(c,d)]
\iff
a+d\leq c+b.
$$

La relación $\leq_{\mathbb Z}$ es un orden total, es compatible con la suma y con la multiplicación por enteros no negativos, y la incrustación canónica satisface

$$
m\leq n
\iff
\iota(m)\leq_{\mathbb Z}\iota(n).
$$

**En el Tratado:** [Definición 2.9.1 — Relación de orden entera](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-orden-entero-def), [Teorema 2.9.3 — El orden entero es total](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-orden-entero-total) y [Proposición 2.9.5 — La incrustación preserva y refleja el orden](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-incrustacion-preserva-orden).

**Véase también:** [Orden natural](#gl-orden-natural), [Orden total](#gl-orden-total), [Orden estricto](#gl-orden-estricto), [Incrustación canónica](#gl-incrustacion-canonica).

---

## Tricotomía {#gl-tricotomia}

**Idea.** En un orden total estricto, dos elementos sólo pueden estar en una de tres posiciones mutuamente excluyentes: el primero precede al segundo, son iguales, o el segundo precede al primero.

**En este tratado.** Para cualesquiera $x,y\in\mathbb Z$, exactamente una de las siguientes alternativas es verdadera:

$$
x<_{\mathbb Z}y,
\qquad
x=y,
\qquad
y<_{\mathbb Z}x.
$$

Es una consecuencia inmediata de que $\leq_{\mathbb Z}$ es un orden total y de la definición del orden estricto asociado.

**En el Tratado:** [Corolario 2.9.6 — Tricotomía en $\mathbb Z$](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-tricotomia-enteros).

**Véase también:** [Orden entero](#gl-orden-entero), [Orden total](#gl-orden-total), [Orden estricto](#gl-orden-estricto), [Totalidad (conexidad)](#gl-totalidad).

---

::: {.callout-note title="Glosario vivo"}
Con **§2.9 — Orden de los enteros** se incorporan el orden entero y la tricotomía en $\mathbb Z$. La siguiente ampliación acompañará las secciones de cierre del capítulo cuando aparezca nuevo vocabulario matemático.
:::

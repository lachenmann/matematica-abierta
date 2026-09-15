## Cero racional {#gl-cero-racional}

**Idea.** Es el elemento neutro de la suma racional.

**En este tratado.** Definimos

$$
\boxed{
0_{\mathbb Q}:=\frac{0_{\mathbb Z}}{1_{\mathbb Z}}.
}
$$

Después se demuestra que, para todo $x\in\mathbb Q$,

$$
x+0_{\mathbb Q}=x=0_{\mathbb Q}+x.
$$

**En el Tratado:** [Notación 3.3.4 — Cero racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-cero-racional) y [Proposición 3.3.8 — Leyes del grupo aditivo racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-grupo-aditivo-racional).

**Véase también:** [Número racional](#gl-numero-racional), [Suma racional](#gl-suma-racional), [Opuesto racional](#gl-opuesto-racional).

---

## Opuesto racional {#gl-opuesto-racional}

**Idea.** Es el inverso aditivo de un número racional: el racional que, sumado con él, produce $0_{\mathbb Q}$.

**En este tratado.** La operación se construye primero sobre representantes mediante

$$
(a,b)\longmapsto(-a,b),
$$

y, después de demostrar compatibilidad con $\sim_{\mathbb Q}$, desciende al cociente como

$$
\boxed{
-\frac ab=\frac{-a}{b}.
}
$$

**En el Tratado:** [Definición 3.3.7 — Opuesto en $\mathbb Q$](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-opuesto-racional).

**Véase también:** [Cero racional](#gl-cero-racional), [Suma racional](#gl-suma-racional), [Sustracción racional](#gl-sustraccion-racional).

---

## Suma racional {#gl-suma-racional}

**Idea.** La suma de racionales se obtiene haciendo descender al cociente una operación compatible definida primero sobre representantes fraccionarios.

**En este tratado.** Para representantes $(a,b),(c,d)\in D_{\mathbb Q}$ se define primero

$$
(ad+bc,bd).
$$

La compatibilidad con $\sim_{\mathbb Q}$ permite definir en $\mathbb Q$

$$
\boxed{
\frac ab+\frac cd
=
\frac{ad+bc}{bd}.
}
$$

La operación resultante es asociativa y conmutativa, posee neutro $0_{\mathbb Q}$ y todo racional tiene opuesto aditivo.

**En el Tratado:** [Definición 3.3.3 — Suma en $\mathbb Q$](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-suma-racional) y [Proposición 3.3.8 — Leyes del grupo aditivo racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-grupo-aditivo-racional).

**Véase también:** [Número racional](#gl-numero-racional), [Cero racional](#gl-cero-racional), [Opuesto racional](#gl-opuesto-racional), [Sustracción racional](#gl-sustraccion-racional), [Principio de definición sobre clases](#gl-definicion-sobre-clases).

---

## Sustracción racional {#gl-sustraccion-racional}

**Idea.** Restar un racional consiste en sumar su opuesto aditivo.

**En este tratado.** Para $x,y\in\mathbb Q$ definimos

$$
\boxed{
x-y:=x+(-y).
}
$$

**En el Tratado:** [Definición 3.3.9 — Sustracción racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-sustraccion-racional).

**Véase también:** [Suma racional](#gl-suma-racional), [Opuesto racional](#gl-opuesto-racional), [Sustracción entera](#gl-sustraccion-entera).

---

::: {.callout-note title="Glosario vivo"}
Con **§3.3 — Suma, cero, opuesto y sustracción** quedan incorporadas las primeras operaciones aritméticas propias de $\mathbb Q$. La próxima ampliación acompañará **§3.4 — Producto y estructura de cuerpo**.
:::

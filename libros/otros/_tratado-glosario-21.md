## Clase racional {#gl-clase-racional}

**Idea.** Un racional no es uno de sus pares representantes, sino la clase completa de representantes fraccionarios que expresan el mismo cociente.

**En este tratado.** Para $(a,b)\in D_{\mathbb Q}$, escribimos

$$
[(a,b)]_{\mathbb Q}
$$

para la clase de equivalencia de $(a,b)$ respecto de $\sim_{\mathbb Q}$. Esa clase es un elemento de $\mathbb Q$.

**En el Tratado:** [Notación 3.2.5 — Clases racionales y notación fraccionaria](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-clases-racionales-notacion-fraccionaria).

**Véase también:** [Clase de equivalencia](#gl-clase-equivalencia), [Representante fraccionario](#gl-representante-fraccionario), [Número racional](#gl-numero-racional), [Notación fraccionaria](#gl-notacion-fraccionaria).

---

## Notación fraccionaria {#gl-notacion-fraccionaria}

**Idea.** La expresión $a/b$ se introduce sólo después de construir el cociente racional; no designa el par $(a,b)$, sino su clase de equivalencia.

**En este tratado.** Para $(a,b)\in D_{\mathbb Q}$,

$$
\boxed{
\frac ab
:=
[(a,b)]_{\mathbb Q}.
}
$$

La expresión está definida únicamente cuando $b\neq0_{\mathbb Z}$. Además,

$$
\frac ab=\frac cd
\iff
ad=bc.
$$

**En el Tratado:** [Notación 3.2.5 — Clases racionales y notación fraccionaria](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-clases-racionales-notacion-fraccionaria) y [Proposición 3.2.6 — Criterio de igualdad de racionales](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-criterio-igualdad-racionales).

**Véase también:** [Clase racional](#gl-clase-racional), [Representante fraccionario](#gl-representante-fraccionario), [Número racional](#gl-numero-racional).

---

## Número racional {#gl-numero-racional}

**Idea.** Un número racional es el objeto obtenido al identificar todos los pares de enteros con denominador no nulo que satisfacen la misma proporción cruzada.

**En este tratado.** Definimos

$$
\mathbb Q
:=
D_{\mathbb Q}/{\sim_{\mathbb Q}},
$$

donde

$$
(a,b)\sim_{\mathbb Q}(c,d)
\iff
ad=bc.
$$

Un **número racional** es un elemento de $\mathbb Q$.

**En el Tratado:** [Definición 3.2.4 — Conjunto de los números racionales](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-conjunto-numeros-racionales).

**Véase también:** [Conjunto cociente](#gl-conjunto-cociente), [Relación de equivalencia racional](#gl-relacion-equivalencia-racional), [Clase racional](#gl-clase-racional).

---

## Relación de equivalencia racional {#gl-relacion-equivalencia-racional}

**Idea.** Dos representantes fraccionarios expresan el mismo racional cuando sus productos cruzados coinciden.

**En este tratado.** Sobre

$$
D_{\mathbb Q}=\mathbb Z\times\mathbb Z_{\neq0}
$$

definimos

$$
\boxed{
(a,b)\sim_{\mathbb Q}(c,d)
\iff
ad=bc.
}
$$

Esta relación es reflexiva, simétrica y transitiva, y por tanto permite formar el cociente $\mathbb Q$.

**En el Tratado:** [Definición 3.2.1 — Relación de equivalencia racional](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-relacion-equivalencia-racional) y [Proposición 3.2.2](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-equivalencia-racional-es-equivalencia).

**Véase también:** [Relación de equivalencia](#gl-relacion-equivalencia), [Conjunto de representantes racionales](#gl-conjunto-representantes-racionales), [Número racional](#gl-numero-racional).

---

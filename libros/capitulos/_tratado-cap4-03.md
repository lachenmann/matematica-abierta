## 4.3. Intervalos {#sec-ta-4-3}

La notación de intervalos fue reservada desde la construcción de los enteros precisamente para este momento.

### Definición 4.3.1 — Intervalos acotados {#ta-intervalos-acotados}

*Glosario: [intervalos acotados](../otros/tratado-de-analisis-glosario.md#gl-intervalos-acotados)*

Sean $a,b\in F$. Definimos

$$
[a,b]
:=
\{x\in F:a\leq x\leq b\},
$$

$$
(a,b)
:=
\{x\in F:a<x<b\},
$$

$$
[a,b)
:=
\{x\in F:a\leq x<b\},
$$

y

$$
(a,b]
:=
\{x\in F:a<x\leq b\}.
$$

No se impone $a\leq b$ en la definición. Si los extremos están invertidos, las condiciones de pertenencia determinan automáticamente el conjunto correspondiente.

### Proposición 4.3.2 — Habitabilidad y no vaciedad de intervalos {#ta-habitabilidad-intervalos}

Para $a,b\in F$ se tienen las equivalencias positivas

$$
\boxed{
a\leq b
\iff
\exists x\in F\;(x\in[a,b]),
}
$$

y

$$
\boxed{
a<b
\iff
\exists x\in F\;(x\in(a,b)).
}
$$

En la lógica clásica del tratado esto equivale a escribir, respectivamente,

$$
[a,b]\neq\varnothing
\iff a\leq b,
$$

$$
(a,b)\neq\varnothing
\iff a<b.
$$

**Demostración.**

Si $a\leq b$, el testigo explícito $a$ pertenece a $[a,b]$. Recíprocamente, dado un testigo $x\in[a,b]$, tenemos $a\leq x\leq b$, y la transitividad da $a\leq b$.

Si $a<b$, el [Teorema 4.1.11](#ta-cuerpo-ordenado-denso) proporciona explícitamente un $m$ con $a<m<b$, luego $m\in(a,b)$. Recíprocamente, dado $x\in(a,b)$, la transitividad da $a<b$. ∎

> **Nota fundacional.** La prueba trabaja con testigos de habitabilidad. La formulación por mera desigualdad $S\neq\varnothing$ es su envolvente clásica y no debe confundirse con la disponibilidad efectiva de un elemento de $S$.

### Proposición 4.3.3 — Intervalos centrados y valor absoluto {#ta-intervalos-centrados-valor-absoluto}

*Glosario: [intervalos centrados](../otros/tratado-de-analisis-glosario.md#gl-intervalos-centrados)*

Si $a\in F$ y $r\geq0$, entonces

$$
\boxed{
x\in[a-r,a+r]
\iff
|x-a|\leq r.
}
$$

**Demostración.**

Por definición,

$$
x\in[a-r,a+r]
$$

si y sólo si

$$
a-r\leq x\leq a+r.
$$

Sumando $-a$ en ambas desigualdades obtenemos

$$
-r\leq x-a\leq r.
$$

Como $r\geq0$, la [Proposición 4.2.2(6)](#ta-propiedades-elementales-valor-absoluto) equivale esta condición a $|x-a|\leq r$. ∎

---

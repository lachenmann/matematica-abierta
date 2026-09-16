## Desigualdad triangular {#gl-desigualdad-triangular}

**Idea.** La magnitud de una suma no supera la suma de las magnitudes.

**En este tratado.** En todo cuerpo ordenado $F$, para $x,y\in F$,

$$
|x+y|\leq |x|+|y|.
$$

La demostración se obtiene encajando $x$ e $y$ entre sus valores absolutos y aplicando la caracterización de $|z|\leq r$ mediante las dos desigualdades $-r\leq z\leq r$.

**En el Tratado:** [Teorema 4.2.3 — Desigualdad triangular](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-desigualdad-triangular).

**Véase también:** [Valor absoluto](#gl-valor-absoluto), [Desigualdad triangular inversa](#gl-desigualdad-triangular-inversa).

---

## Desigualdad triangular inversa {#gl-desigualdad-triangular-inversa}

**Idea.** La diferencia entre dos magnitudes no puede exceder la magnitud de la diferencia entre los elementos originales.

**En este tratado.** Para $x,y$ en un cuerpo ordenado,

$$
\bigl||x|-|y|\bigr|\leq |x-y|.
$$

Se deduce de la desigualdad triangular aplicada a $x=(x-y)+y$ y, simétricamente, a $y=(y-x)+x$.

**En el Tratado:** [Corolario 4.2.4 — Desigualdad triangular inversa](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-desigualdad-triangular-inversa).

**Véase también:** [Valor absoluto](#gl-valor-absoluto), [Desigualdad triangular](#gl-desigualdad-triangular).

---

## Valor absoluto {#gl-valor-absoluto}

**Idea.** El valor absoluto mide la magnitud algebraica de un elemento prescindiendo de su signo.

**En este tratado.** Si $F$ es un cuerpo ordenado y $x\in F$, se define sin presuponer decidibilidad del signo mediante

$$
\boxed{|x|:=\max\{x,-x\}.}
$$

La comparabilidad del orden total garantiza que el máximo existe y es único. De esta definición se deduce que $|x|=x$ cuando $0\leq x$ y que $|x|=-x$ cuando $x\leq0$; ambas descripciones coinciden en $x=0$.

Se demuestra además que $|x|\geq0$, que $|x|=0$ exactamente cuando $x=0$, que $|-x|=|x|$, que $|xy|=|x||y|$ y que, para $r\geq0$,

$$
|x|\leq r
\iff
-r\leq x\leq r.
$$

**En el Tratado:** [Definición 4.2.1 — Valor absoluto](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-valor-absoluto) y [Proposición 4.2.2 — Propiedades elementales del valor absoluto](../capitulos/tratado-de-analisis-capitulo-4-cuerpos-ordenados-y-el-problema-de-la-completitud.md#ta-propiedades-elementales-valor-absoluto).

**Véase también:** [Cuerpo ordenado](#gl-cuerpo-ordenado), [Desigualdad triangular](#gl-desigualdad-triangular), [Desigualdad triangular inversa](#gl-desigualdad-triangular-inversa).

---
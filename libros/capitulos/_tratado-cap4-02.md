## 4.2. Valor absoluto {#sec-ta-4-2}

El orden permite medir algebraicamente la magnitud de un elemento sin distinguir de manera permanente entre los dos signos.

### Definición 4.2.1 — Valor absoluto {#ta-valor-absoluto}

*Glosario: [valor absoluto](../otros/tratado-de-analisis-glosario.md#gl-valor-absoluto)*

Sea $F$ un cuerpo ordenado y $x\in F$. Por totalidad,

$$
x\leq -x
\qquad\text{o}\qquad
-x\leq x.
$$

Por tanto el conjunto finito $\{x,-x\}$ posee un máximo; por la unicidad del máximo ese elemento es único. Definimos

$$
\boxed{
|x|:=\max\{x,-x\}.
}
$$

Así, por definición de máximo,

$$
\boxed{
x\leq |x|
\qquad\text{y}\qquad
-x\leq |x|.
}
$$

> **Nota fundacional.** Esta definición usa únicamente la comparabilidad positiva del orden total. No requiere decidir entre $x=0$, $x>0$ y $x<0$. Si además $0\leq x$, entonces $|x|=x$; si $x\leq0$, entonces $|x|=-x$. Las dos conclusiones coinciden cuando $x=0$.

### Proposición 4.2.2 — Propiedades elementales del valor absoluto {#ta-propiedades-elementales-valor-absoluto}

Para $x,y\in F$:

1. $|x|\geq0$;
2. $|x|=0$ si y sólo si $x=0$;
3. $|-x|=|x|$;
4. $-|x|\leq x\leq|x|$;
5. $|xy|=|x||y|$;
6. para $r\geq0$,
   $$
   |x|\leq r
   \iff
   -r\leq x\leq r.
   $$

**Demostración.**

Por la Definición 4.2.1, $|x|$ es el máximo de $\{x,-x\}$.

Para (1), la totalidad da $0\leq x$ o $x\leq0$. En el primer caso $0\leq x\leq|x|$. En el segundo, el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $0\leq -x\leq|x|$. Luego siempre $0\leq|x|$.

Para (4), la propiedad de máximo da directamente $x\leq|x|$ y $-x\leq|x|$. Invirtiendo la segunda desigualdad mediante el Lema 4.1.3 obtenemos $-|x|\leq x$. Por tanto

$$
-|x|\leq x\leq|x|.
$$

Para (2), si $x=0$, entonces $\{x,-x\}=\{0\}$ y $|x|=0$. Recíprocamente, si $|x|=0$, (4) da

$$
0=-|x|\leq x\leq|x|=0,
$$

y la antisimetría implica $x=0$.

Para (3), los conjuntos cuyos máximos se toman son idénticos:

$$
\{-x,-(-x)\}=\{-x,x\}=\{x,-x\}.
$$

Por unicidad del máximo, $|-x|=|x|$.

Para (5), usamos sólo la comparabilidad positiva $0\leq x\lor x\leq0$ y $0\leq y\lor y\leq0$. Si $0\leq x$, entonces $|x|=x$; si $x\leq0$, entonces $|x|=-x$, y análogamente para $y$.

- Si $0\leq x$ y $0\leq y$, entonces $0\leq xy$ y
  $$
  |xy|=xy=|x||y|.
  $$
- Si $x\leq0$ y $y\leq0$, entonces $0\leq -x$ y $0\leq -y$, y
  $$
  xy=(-x)(-y)\geq0,
  $$
  de modo que $|xy|=xy=(-x)(-y)=|x||y|$.
- Si $x\leq0\leq y$, entonces $(-x)y\geq0$ y $xy=-((-x)y)\leq0$, de modo que
  $$
  |xy|=-xy=(-x)y=|x||y|.
  $$
- El caso $y\leq0\leq x$ es simétrico.

Para (6), supongamos primero $|x|\leq r$. Por (4),

$$
-|x|\leq x\leq|x|.
$$

De $|x|\leq r$ y la inversión del orden al tomar opuestos obtenemos $-r\leq-|x|$, luego

$$
-r\leq x\leq r.
$$

Recíprocamente, si $-r\leq x\leq r$, entonces $x\leq r$ y, al invertir $-r\leq x$, también $-x\leq r$. Como $|x|$ es el máximo de $x$ y $-x$, se sigue $|x|\leq r$. ∎

### Teorema 4.2.3 — Desigualdad triangular {#ta-desigualdad-triangular}

*Glosario: [desigualdad triangular](../otros/tratado-de-analisis-glosario.md#gl-desigualdad-triangular)*

*Referencia transversal: [demostraciones, variantes y aplicaciones de la desigualdad triangular](../../teoria/resultados/desigualdad-triangular.qmd#tri-cuerpo-ordenado) (`MA-ART-0002`).*

Para $x,y\in F$,

$$
\boxed{
|x+y|\leq|x|+|y|.
}
$$

**Demostración.**

Por la Proposición 4.2.2,

$$
-|x|\leq x\leq|x|,
\qquad
-|y|\leq y\leq|y|.
$$

Sumando las desigualdades correspondientes,

$$
-(|x|+|y|)
\leq
x+y
\leq
|x|+|y|.
$$

Como $|x|+|y|\geq0$, el criterio de la Proposición 4.2.2(6) da

$$
|x+y|\leq|x|+|y|.
$$

∎

### Corolario 4.2.4 — Desigualdad triangular inversa {#ta-desigualdad-triangular-inversa}

*Glosario: [desigualdad triangular inversa](../otros/tratado-de-analisis-glosario.md#gl-desigualdad-triangular-inversa)*

*Referencia transversal: [desigualdad triangular inversa y su demostración](../../teoria/resultados/desigualdad-triangular.qmd#tri-inversa).*

Para $x,y\in F$,

$$
\boxed{
\bigl||x|-|y|\bigr|
\leq
|x-y|.
}
$$

**Demostración.**

Por la desigualdad triangular,

$$
|x|
=|(x-y)+y|
\leq|x-y|+|y|,
$$

luego

$$
|x|-|y|\leq|x-y|.
$$

Intercambiando $x$ e $y$ y usando $|y-x|=|x-y|$,

$$
|y|-|x|\leq|x-y|.
$$

Por la caracterización del valor absoluto mediante dos desigualdades, se sigue el resultado. ∎

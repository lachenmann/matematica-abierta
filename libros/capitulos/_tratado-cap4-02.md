## 4.2. Valor absoluto {#sec-ta-4-2}

El orden permite medir algebraicamente la magnitud de un elemento sin distinguir de manera permanente entre los dos signos.

### Definición 4.2.1 — Valor absoluto {#ta-valor-absoluto}

*Glosario: [valor absoluto](../otros/tratado-de-analisis-glosario.md#gl-valor-absoluto)*

Sea $F$ un cuerpo ordenado. Para $x\in F$ definimos

$$
\boxed{
|x|
:=
\begin{cases}
x,&0\leq x,\\
-x,&x<0.
\end{cases}
}
$$

La totalidad del orden y la incompatibilidad entre $0\leq x$ y $x<0$ hacen que la definición sea unívoca.

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

Para (1), si $0\leq x$, entonces $|x|=x\geq0$. Si $x<0$, el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $0<-x$, y $|x|=-x>0$.

Para (2), si $x=0$, la primera rama de la definición da $|x|=0$. Recíprocamente, supongamos $|x|=0$. Si $0\leq x$, entonces $|x|=x$, luego $x=0$. Si $x<0$, entonces $|x|=-x=0$ y, tomando opuestos, nuevamente $x=0$; este segundo caso contradice de hecho $x<0$, pero la conclusión basta.

Para (3), si $x=0$ la igualdad es inmediata. Si $0<x$, entonces $-x<0$ por el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado), y

$$
|-x|=-(-x)=x=|x|.
$$

Si $x<0$, entonces $0<-x$ y

$$
|-x|=-x=|x|.
$$

Para (4), si $0\leq x$, entonces $|x|=x$, de modo que $x\leq|x|$ es igualdad; además $-x\leq x$ porque $-x\leq0\leq x$. Si $x<0$, entonces $|x|=-x$ y $-|x|=x$, mientras que $x\leq -x$ se obtiene de $x<0<-x$. Así en ambos casos

$$
-|x|\leq x\leq|x|.
$$

Para (5) consideramos los signos de $x$ e $y$. Si alguno es cero, ambos miembros son cero por el [Lema 4.1.2](#ta-identidades-elementales-cuerpo) y (2). Supongamos, pues, $x,y\neq0$.

Si $x>0$ e $y>0$, el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $xy>0$, por lo que

$$
|xy|=xy=|x||y|.
$$

Si $x<0$ e $y<0$, entonces $-x>0$ y $-y>0$; por el [Lema 4.1.2](#ta-identidades-elementales-cuerpo),

$$
xy=(-x)(-y)>0,
$$

y por tanto

$$
|xy|=xy=(-x)(-y)=|x||y|.
$$

Si $x<0<y$, entonces $-x>0$ y el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $(-x)y>0$. Como el [Lema 4.1.2](#ta-identidades-elementales-cuerpo) afirma $(-x)y=-(xy)$, se sigue $xy<0$. Luego

$$
|xy|=-(xy)=(-x)y=|x||y|.
$$

El caso $y<0<x$ es simétrico.

Para (6), supongamos primero $|x|\leq r$. Por (4),

$$
-|x|\leq x\leq|x|.
$$

De $|x|\leq r$ y la inversión del orden al tomar opuestos obtenemos $-r\leq-|x|$, luego

$$
-r\leq x\leq r.
$$

Recíprocamente, si $-r\leq x\leq r$, distinguimos el signo de $x$. Si $x\geq0$, $|x|=x\leq r$. Si $x<0$, de $-r\leq x$ y la inversión del orden se obtiene $-x\leq r$, y $|x|=-x\leq r$. ∎

### Teorema 4.2.3 — Desigualdad triangular {#ta-desigualdad-triangular}

*Glosario: [desigualdad triangular](../otros/tratado-de-analisis-glosario.md#gl-desigualdad-triangular)*

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

---

::: {.callout-note title="Publicación progresiva"}
Con §4.2 queda construido el valor absoluto en un cuerpo ordenado y demostradas sus desigualdades fundamentales. La siguiente entrega será **§4.3 — Intervalos**.
:::

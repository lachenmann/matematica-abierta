## 4.5. Densidad de un subcuerpo {#sec-ta-4-5}

Todo cuerpo ordenado es denso en sí mismo, pero eso no dice que un subcuerpo dado sea denso en el cuerpo mayor. La arquimedianidad es justamente lo que permite demostrar que el subcuerpo generado por $1$ penetra arbitrariamente entre dos elementos.

### Teorema 4.5.1 — Densidad del subcuerpo primo en un cuerpo arquimediano {#ta-densidad-subcuerpo-primo-arquimediano}

Sea $F$ un cuerpo ordenado arquimediano. Si $x<y$, existe $q\in P_F$ tal que

$$
\boxed{x<q<y.}
$$

**Demostración.**

Sea

$$
\delta:=y-x>0.
$$

Como $0<1_F+1_F$, el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $(1_F+1_F)^{-1}>0$. Definimos

$$
\varepsilon:=\delta(1_F+1_F)^{-1}>0.
$$

Por la [Proposición 4.4.2](#ta-arquimedianidad-reciprocos), existe $n\in\mathbb N$, $n\neq0$, tal que

$$
0<\nu_F(n)^{-1}<\varepsilon.
$$

Escribiremos $N:=\nu_F(n)>0$. La desigualdad elegida implica

$$
(1_F+1_F)N^{-1}<\delta.
$$

Por arquimedianidad aplicada a $-x$, existe $p\in\mathbb N$ con

$$
-x<\nu_F(p).
$$

Por invariancia estricta bajo traslación,

$$
u:=x+\nu_F(p)>0.
$$

Como $N>0$ y $u>0$, el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $Nu>0$. Aplicando arquimedianidad a $Nu$, existe $k\in\mathbb N$ con

$$
Nu<\nu_F(k),
$$

y en particular $Nu\leq\nu_F(k)$. Por tanto el conjunto

$$
A:=\{k\in\mathbb N:Nu\leq\nu_F(k)\}
$$

está habitado. Aplicamos ahora el [Teorema 1.6.13 — Principio de buen orden](tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-principio-buen-orden-naturales): éste es el único paso esencialmente clásico de la prueba, pues la membresía de $A$ no se ha demostrado decidible para un cuerpo ordenado abstracto. Sea $k$ el mínimo de $A$.

Como $Nu>0=\nu_F(0)$, no puede ser $k=0$. Por el [Teorema 1.2.7 — Predecesor de todo natural no nulo](tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-predecesor-natural), existe $j\in\mathbb N$ con $k=S(j)$. Entonces $j<k$, de modo que la minimalidad de $k$ implica $j\notin A$, es decir,

$$
\neg\bigl(Nu\leq\nu_F(j)\bigr).
$$

La totalidad positiva del orden da

$$
\nu_F(j)\leq Nu
\qquad\text{o}\qquad
Nu\leq\nu_F(j).
$$

La segunda alternativa contradice $j\notin A$, por lo que

$$
\nu_F(j)\leq Nu.
$$

Como $k=S(j)$,

$$
\nu_F(k)=\nu_F(j)+1_F,
$$

y por tanto, multiplicando por $N^{-1}>0$,

$$
\nu_F(k)N^{-1}
\leq
u+N^{-1}.
$$

Además $k\in A$ da

$$
u\leq\nu_F(k)N^{-1}.
$$

Tomamos un sucesor adicional y definimos

$$
q:=\nu_F(S(k))N^{-1}-\nu_F(p).
$$

Como $N^{-1}>0$,

$$
u
\leq
\nu_F(k)N^{-1}
<
\nu_F(S(k))N^{-1},
$$

de modo que, restando $\nu_F(p)$,

$$
x<q.
$$

Por otra parte,

$$
\begin{aligned}
\nu_F(S(k))N^{-1}
&=\nu_F(k)N^{-1}+N^{-1}\\
&\leq u+(1_F+1_F)N^{-1}\\
&<u+\delta.
\end{aligned}
$$

Restando $\nu_F(p)$ obtenemos

$$
q<x+\delta=y.
$$

Finalmente, el [Corolario 4.1.10](#ta-numerales-subcuerpo-primo) da $\nu_F(S(k)),N,\nu_F(p)\in P_F$; como $P_F$ es subcuerpo y $N\neq0$, también $N^{-1}\in P_F$, y por clausura bajo las operaciones $q\in P_F$. Así $x<q<y$. ∎

> **Nota fundacional.** El mínimo de $A$ es único y, por tanto, canónico una vez demostrada su existencia; esto no utiliza Choice. Sin embargo, como no disponemos de un procedimiento de decisión para $Nu\leq\nu_F(k)$ en un cuerpo ordenado abstracto, el buen orden aplicado a $A$ no proporciona aquí un algoritmo uniforme para localizar $k$.

### Corolario 4.5.2 — Todo subcuerpo de un cuerpo arquimediano es denso {#ta-todo-subcuerpo-denso-arquimediano}

Sea $K$ un subcuerpo de un cuerpo ordenado arquimediano $F$. Para cualesquiera $x<y$ en $F$ existe $q\in K$ con

$$
x<q<y.
$$

**Demostración.**

Por la [Proposición 4.1.9](#ta-minimalidad-subcuerpo-primo), $P_F\subseteq K$. El elemento $q\in P_F$ proporcionado por el Teorema 4.5.1 pertenece entonces a $K$. ∎

La conclusión explica una característica decisiva de los cuerpos arquimedianos: el subcuerpo primo ya es suficientemente fino para aproximar por orden a cualquier elemento del cuerpo. Esto anticipa la futura densidad de la copia de $\mathbb Q$ en $\mathbb R$.

---

::: {.callout-note title="Publicación progresiva"}
Con §4.5 queda demostrada la densidad del subcuerpo primo —y, por inclusión, de todo subcuerpo— en un cuerpo ordenado arquimediano. La siguiente entrega será **§4.6 — Propiedad del supremo**.
:::

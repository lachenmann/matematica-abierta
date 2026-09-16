## 4.4. Propiedad arquimediana {#sec-ta-4-4}

En $\mathbb Q$ demostramos que los naturales canónicos alcanzan por encima de cualquier racional. La formulación abstracta requiere primero la [aplicación canónica de numerales naturales](#ta-numerales-naturales-cuerpo-ordenado) construida en §4.1.

### Definición 4.4.1 — Cuerpo ordenado arquimediano {#ta-cuerpo-ordenado-arquimediano}

*Glosario: [propiedad arquimediana](../otros/tratado-de-analisis-glosario.md#gl-propiedad-arquimediana)*

Un cuerpo ordenado $F$ es **arquimediano** si para todo $x\in F$ existe $n\in\mathbb N$ tal que

$$
\boxed{
x<\nu_F(n).
}
$$

Ésta es la formulación primaria y positiva de la propiedad.

En la lógica clásica del tratado equivale a afirmar que la imagen $\nu_F[\mathbb N]$ no está acotada superiormente en $F$. Esta equivalencia utiliza negación de cuantificadores y no se tomará como identidad constructiva entre ambas formulaciones.

### Proposición 4.4.2 — Caracterización por recíprocos pequeños {#ta-arquimedianidad-reciprocos}

Un cuerpo ordenado $F$ es arquimediano si y sólo si para todo $\varepsilon>0$ existe $n\in\mathbb N$, $n\neq0$, tal que

$$
\boxed{
0<\nu_F(n)^{-1}<\varepsilon.
}
$$

**Demostración.**

Supongamos primero que $F$ es arquimediano y sea $\varepsilon>0$. Por el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado), $\varepsilon^{-1}>0$. Existe $n$ con

$$
\varepsilon^{-1}<\nu_F(n).
$$

El miembro derecho es positivo, de modo que $n\neq0$. Al invertir la desigualdad entre positivos,

$$
0<\nu_F(n)^{-1}<\varepsilon.
$$

Recíprocamente, supongamos la propiedad de recíprocos pequeños y sea $x\in F$. Por totalidad positiva del orden,

$$
x\leq1_F
\qquad\text{o}\qquad
1_F\leq x.
$$

En el primer caso, la [Proposición 4.1.6](#ta-aritmetica-orden-numerales) aplicada a $1<2$ da

$$
1_F=\nu_F(1)<\nu_F(2),
$$

y por transitividad

$$
x<\nu_F(2).
$$

En el segundo caso, $0<1_F\leq x$, luego $x>0$ y el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado) da $x^{-1}>0$. Aplicamos la hipótesis a $\varepsilon=x^{-1}$ y obtenemos $n\neq0$ con

$$
0<\nu_F(n)^{-1}<x^{-1}.
$$

Como ambos inversos son positivos, la inversión del orden entre positivos, demostrada en el [Lema 4.1.3](#ta-calculo-signos-cuerpo-ordenado), produce

$$
x=(x^{-1})^{-1}
<
(\nu_F(n)^{-1})^{-1}
=
\nu_F(n).
$$

En ambos casos existe un numeral estrictamente mayor que $x$. Por tanto $F$ es arquimediano. ∎

### Proposición 4.4.3 — La formulación abstracta coincide con la arquimedianidad ya probada en $\mathbb Q$ {#ta-arquimedianidad-q-coincide}

Para $F=\mathbb Q$, la aplicación $\nu_F$ de la [Definición 4.1.5](#ta-numerales-naturales-cuerpo-ordenado) coincide con la [incrustación canónica $\nu_{\mathbb N}^{\mathbb Q}$](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-incrustacion-natural-nq) construida en el Capítulo 3. En consecuencia, $\mathbb Q$ es arquimediano en el sentido de la Definición 4.4.1.

**Demostración.**

Ambas funciones toman $0$ en $0_{\mathbb Q}$. Además, para $n\in\mathbb N$,

$$
S(n)=n+1
$$

por la definición recursiva de la suma natural. Como el [Corolario 3.8.2](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-propiedades-incrustacion-natural-nq) afirma que $\nu_{\mathbb N}^{\mathbb Q}$ preserva suma y unidad,

$$
\begin{aligned}
\nu_{\mathbb N}^{\mathbb Q}(S(n))
&=\nu_{\mathbb N}^{\mathbb Q}(n+1)\\
&=\nu_{\mathbb N}^{\mathbb Q}(n)+\nu_{\mathbb N}^{\mathbb Q}(1)\\
&=\nu_{\mathbb N}^{\mathbb Q}(n)+1_{\mathbb Q}.
\end{aligned}
$$

Por la unicidad del [Teorema 1.3.7 — Teorema de recursión sobre $\mathbb N$](tratado-de-analisis-capitulo-1-los-numeros-naturales.md#ta-teorema-recursion-naturales), esta función coincide con $\nu_F$.

Finalmente, el [Teorema 3.8.5 — $\mathbb Q$ es arquimediano](tratado-de-analisis-capitulo-3-los-numeros-racionales.md#ta-q-arquimediano) afirma que para todo $q\in\mathbb Q$ existe $n\in\mathbb N$ con

$$
q<\nu_{\mathbb N}^{\mathbb Q}(n)=\nu_F(n),
$$

que es exactamente la condición de la Definición 4.4.1. ∎

---

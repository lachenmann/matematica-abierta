### Dos sucesiones que parecen iguales durante muchísimo tiempo

Consideremos primero

$$
a_n=\frac{1}{n+1},
\qquad n\in\mathbb N.
$$

Como en este tratado usamos

$$
\mathbb N=\{0,1,2,\dots\},
$$

sus primeros términos son

$$
1,\frac12,\frac13,\frac14,\frac15,\dots
$$

A medida que el índice crece, los términos se hacen pequeños. No estamos formulando todavía qué significa rigurosamente «hacerse pequeños», pero la tendencia visual y aritmética resulta familiar.

Construyamos ahora otra sucesión:

$$
b_n=
\begin{cases}
\dfrac{1}{n+1}, & 0\le n\le 10^6,\\[4pt]
1, & n>10^6.
\end{cases}
$$

Durante todo el tramo

$$
n=0,1,2,\dots,10^6,
$$

las dos sucesiones son exactamente iguales:

$$
a_n=b_n.
$$

Esto significa que podemos inspeccionar más de un millón de términos sin detectar diferencia alguna. Sin embargo, después del índice $10^6$ sus comportamientos se separan por completo.

La primera sigue obedeciendo

$$
a_n=\frac{1}{n+1},
$$

y sus términos continúan disminuyendo en tamaño. La segunda, en cambio, queda fijada para siempre en

$$
b_n=1.
$$

Si nuestro criterio dependiera solo de una muestra finita de términos, por enorme que fuera, no podría distinguir estas dos sucesiones. Podemos hacer que el tramo común tenga diez términos, un millón, un billón o cualquier cantidad finita previamente elegida. Siempre es posible modificar lo que ocurre después.

Este ejemplo contiene la primera dificultad conceptual del capítulo:

$$
\boxed{
\text{ninguna inspección de una cantidad finita de términos determina por sí sola el comportamiento final de una sucesión.}
}
$$

Por eso, cuando más adelante hablemos de límite, la pregunta relevante no será

> ¿qué ocurre en los primeros términos?,

sino

> ¿qué ocurre con **todos los términos suficientemente tardíos**?

Antes de formalizar esa idea necesitamos precisar qué es exactamente una sucesión.

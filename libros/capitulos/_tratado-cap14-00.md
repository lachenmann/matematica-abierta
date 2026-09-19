## 14.0. De una sucesión de términos a una sucesión de sumas {#sec-ta-14-0}

En el capítulo anterior estudiamos cuándo una sucesión real tiene límite. Podemos ahora preguntar qué ocurre al sumar, en orden, los términos de una sucesión

$$
a=(a_n)_{n\in\mathbb N},\qquad a:\mathbb N\longrightarrow\mathbb R.
$$

Para cada índice finito podemos efectuar una suma ordinaria:

$$
a_0,\qquad a_0+a_1,\qquad a_0+a_1+a_2,\quad\ldots
$$

Estas expresiones no constituyen todavía una «suma infinita». Constituyen, para cada índice natural, una operación **finita**, cuya existencia se obtiene de la aritmética real. La cuestión propiamente analítica consiste en estudiar la sucesión formada por esos resultados.

La arquitectura conceptual del capítulo comienza con tres niveles diferentes:

$$
\boxed{
\text{términos }(a_n)
\quad\longrightarrow\quad
\text{sumas parciales }(s_n)
\quad\longrightarrow\quad
\text{posible límite }\ell.
}
$$

Los términos $a_n$ son los datos; los números $s_n$ son sumas finitas; el número $\ell$ sólo podrá llamarse **suma de la serie** después de demostrar que $s_n\to\ell$. Si no hay convergencia, los dos primeros niveles siguen estando perfectamente definidos, pero no aparece una suma real.

> **Pregunta de lectura.** Que todas las sumas parciales existan no significa que exista su límite. ¿En cuál de los tres niveles se formula la convergencia? La respuesta será siempre: en la sucesión de sumas parciales, no en la mera existencia de cada suma finita.

Trabajaremos con la realización estructural de $\mathbb R$ fijada en §12.9 y con la noción de sucesión real cerrada en el Capítulo 13. No identificaremos el conjunto $\mathbb Q$ con un subconjunto literal de $\mathbb R$ ni confundiremos una sucesión de términos con su sucesión de sumas parciales.

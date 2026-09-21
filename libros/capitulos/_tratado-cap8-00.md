## 8.0. De las fronteras a los procesos de aproximación {#sec-ta-8-0}

La primera construcción de los números reales partió de una insuficiencia del orden racional. El cuerpo $\mathbb Q$ contiene subconjuntos no vacíos y acotados superiormente que carecen de supremo racional; las cortaduras de Dedekind convierten esos huecos en objetos matemáticos mediante una frontera en el orden.

La segunda construcción partirá de una insuficiencia distinta.

Un número puede ser buscado mediante aproximaciones racionales cada vez más precisas aun cuando el objeto al que parecen aproximarse no pertenezca a $\mathbb Q$. En ese caso, el dato fundamental ya no es una frontera que separe racionales, sino un proceso ordenado de aproximación racional.

La transición conceptual puede resumirse así:

$$
\boxed{
\text{Dedekind: una frontera en el orden}
\qquad\longrightarrow\qquad
\text{Cauchy: un proceso de aproximación}.
}
$$

La palabra *proceso* debe entenderse aquí de manera estrictamente matemática. No introduciremos todavía límites, convergencia ni números reales nuevos. Nuestro primer objeto será únicamente una sucesión de racionales,

$$
q_0,q_1,q_2,\ldots,
$$

entendida no como una colección informal de valores, sino como una función cuyo dominio es $\mathbb N$.

Esta precisión importa. Una sucesión no queda determinada por el conjunto de valores que aparecen en ella. Por ejemplo, dos procesos pueden recorrer exactamente los mismos racionales y hacerlo en distinto orden, repetirlos con distinta frecuencia o asignarlos a índices diferentes. El índice pertenece a la estructura del objeto.

La construcción que comienza aquí será independiente de la construcción de Dedekind. Aunque ya disponemos del cuerpo completo $\mathbb R_D$, no utilizaremos su completitud, sus cortaduras ni su noción de número real para justificar ningún paso de la construcción por Cauchy.

El punto de partida de este segundo camino será exclusivamente la infraestructura construida antes de Dedekind:

$$
\mathbb N,
\qquad
\mathbb Q,
\qquad
\text{funciones},
\qquad
\text{familias indexadas},
$$

junto con la aritmética y el orden racionales ya demostrados.

En particular, no diremos todavía que una sucesión “se aproxima a un número”. Esa frase sólo adquirirá significado matemático después de definir una noción cuantitativa de cercanía y, posteriormente, los conceptos de convergencia y sucesión de Cauchy.

Nuestro primer objetivo es más elemental: construir rigurosamente el espacio de todos los procesos racionales indexados por los naturales y dotarlo de las operaciones algebraicas que actúan término a término.

## 5.0. Convertir una frontera en un objeto {#sec-ta-5-0}

El capítulo anterior aisló con precisión la deficiencia de $\mathbb Q$. Los racionales forman un cuerpo ordenado arquimediano y densamente ordenado, pero no son completos: existen subconjuntos no vacíos y acotados superiormente que carecen de supremo racional. El ejemplo conductor fue

$$
S_2=\{q\in\mathbb Q:0_{\mathbb Q}\leq q,\ q^2<2_{\mathbb Q}\}.
$$

El problema no es que falten racionales entre racionales. El problema es que ciertas regiones inferiores del orden racional determinan fronteras que no están representadas por ningún racional.

La idea de Dedekind consiste en cambiar el tipo de objeto que representará una posición numérica. En vez de buscar primero un punto nuevo que ocupe una frontera, tomaremos como objeto todo el lado inferior de la frontera. Así, una nueva posición quedará codificada por los racionales que se encuentran estrictamente por debajo de ella.

Esta estrategia tiene una ventaja fundacional decisiva: no presupone la existencia de números reales para construirlos. Los únicos objetos de partida serán racionales, subconjuntos de $\mathbb Q$ y relaciones ya construidas sobre $\mathbb Q$.

Para evitar objetos patológicos exigiremos cuatro condiciones. El lado inferior deberá ser no vacío y propio, deberá contener todo racional situado por debajo de cualquiera de sus elementos y no deberá poseer un elemento máximo.

La construcción de este capítulo seguirá la cadena

$$
\mathbb Q
\longrightarrow
\text{cortaduras}
\longrightarrow
\mathbb R_D
\longrightarrow
\text{orden por inclusión}
\longrightarrow
\iota_D:\mathbb Q\to\mathbb R_D.
$$

No adoptaremos en ningún momento, antes de demostrar la correspondiente incrustación, una identificación conjuntista de la forma

$$
\mathbb Q\subseteq\mathbb R_D.
$$

Los racionales y las cortaduras son objetos construidos de manera diferente. Su relación será establecida mediante una función canónica.

Tampoco definiremos todavía suma ni producto de cortaduras. Al terminar este capítulo, $\mathbb R_D$ será un conjunto totalmente ordenado que contiene una copia ordenada propia de $\mathbb Q$, pero aún no habremos demostrado que sea un cuerpo ordenado ni que sea completo.

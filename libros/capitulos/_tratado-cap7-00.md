## 7.0. El problema que queda {#sec-ta-7-0}

Hemos construido el conjunto de los reales de Dedekind $\mathbb R_D$ y demostrado que

$$
\boxed{(\mathbb R_D,+_D,\cdot_D,\leq_D)}
$$

es un cuerpo ordenado. Además,

$$
\boxed{\iota_D:\mathbb Q\hookrightarrow\mathbb R_D}
$$

es una incrustación de cuerpos ordenados.

Pero ésta no era todavía la propiedad que motivó la construcción. La insuficiencia fundamental de $\mathbb Q$ no consistía en carecer de operaciones algebraicas ni de un orden compatible con ellas: los racionales ya poseían todo eso. Su defecto era que ciertos subconjuntos no vacíos y acotados superiormente carecían de supremo.

Debemos demostrar que esa insuficiencia ha desaparecido.

Sea $\mathcal A\subseteq\mathbb R_D$ una familia no vacía de cortaduras y supongamos que posee una cota superior. Cada elemento de $\mathcal A$ es a su vez un subconjunto de $\mathbb Q$. Por ello existe un candidato extraordinariamente natural a frontera común:

$$
\boxed{\bigcup\mathcal A.}
$$

La idea fundamental de la construcción alcanza aquí su forma más simple: el supremo de una familia de lados inferiores debe ser el lado inferior obtenido reuniéndolos todos.

El trabajo del capítulo consistirá en probar que esta intuición conjuntista coincide exactamente con la propiedad de completitud definida en el Capítulo 4.

## 12.9. Qué significa $\mathbb R$ a partir de ahora {#sec-ta-12-9}

Las construcciones de Dedekind y Cauchy dieron dos conjuntos distintos,

$$
\mathbb R_D
\qquad\text{y}\qquad
\mathbb R_C,
$$

y el Capítulo 11 construyó entre ellos un isomorfismo explícito. El presente capítulo ha demostrado algo más fuerte: **cualquier** completación ordenada de $\mathbb Q$ está unida a cualquier otra por un único isomorfismo de cuerpos ordenados compatible con la copia racional.

Por tanto no escribiremos

$$
\mathbb R_D=\mathbb R_C.
$$

Esa igualdad conjuntista es falsa en las realizaciones construidas.

La conclusión correcta es estructural:

$$
\boxed{
(\mathbb R_D,\iota_D)
\cong
(\mathbb R_C,\iota_C)
}
$$

y, más generalmente,

$$
\boxed{
\text{toda completación ordenada de }\mathbb Q
\text{ es única hasta único isomorfismo sobre }\mathbb Q.
}
$$

Desde este punto, el símbolo

$$
\boxed{\mathbb R}
$$

podrá utilizarse para hablar de **la estructura de cuerpo ordenado completo que completa a $\mathbb Q$**, sin comprometer el argumento con una codificación particular. Cuando una construcción o una afirmación dependa del conjunto subyacente, de representantes concretos o de la forma de codificación, mantendremos las notaciones

$$
\mathbb R_D,
\qquad
\mathbb R_C.
$$

En los desarrollos estructurales posteriores podremos fijar una realización de $\mathbb R$ y transportar resultados a cualquier otra mediante el único isomorfismo compatible con $\mathbb Q$.

Esta convención no identifica cuatro nociones diferentes:

$$
\boxed{
\text{igualdad conjuntista}
\neq
\text{isomorfía}
\neq
\text{único isomorfismo sobre }\mathbb Q
\neq
\text{equivalencia computable de presentaciones}.
}
$$

La tercera afirmación es la que hemos demostrado en este capítulo. La cuarta pertenece a una capa adicional: para convertir efectivamente nombres de Cauchy, cortaduras localizadas u otras representaciones se necesitan datos intensionales y teoremas de computabilidad específicos.

Del mismo modo,

$$
\boxed{
\text{canónico por unicidad}
\neq
\text{computable}.
}
$$

El transporte

$$
\Psi_{E,F}
$$

está matemáticamente determinado de manera única, pero su definición mediante trazas y supremos no constituye, por sí sola, un algoritmo uniforme sobre presentaciones arbitrarias de $E$ y $F$.

> **Cierre fundacional.** Toda la Parte I se desarrolla en ZF con lógica clásica. Ninguna de las construcciones de los reales, de sus operaciones, de las comparaciones Dedekind–Cauchy o del teorema de unicidad estructural ha requerido AC, $AC_\omega$, DC o Zorn. La ausencia de Choice no se confunde con constructividad: los usos clásicos relevantes han quedado registrados en los nodos donde realmente intervienen.

Podemos condensar el resultado de toda la Parte I en la cadena

$$
\boxed{
\mathbb Q
\longrightarrow
\begin{cases}
\mathbb R_D,\\
\mathbb R_C,
\end{cases}
\longrightarrow
\text{cuerpo ordenado completo}
\longrightarrow
\text{unicidad hasta único isomorfismo sobre }\mathbb Q.
}
$$

La construcción conjuntista ha terminado. A partir de aquí, el tratado puede estudiar análisis real sobre $\mathbb R$ distinguiendo, cuando sea necesario, la **estructura matemática** del **modo concreto de representar sus elementos**.

$$
\boxed{
\text{FIN DE LA PARTE I — FUNDAMENTOS Y CONSTRUCCIÓN DE LOS NÚMEROS REALES}
}
$$

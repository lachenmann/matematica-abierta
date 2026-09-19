## 11.8. Compatibilidad con $\mathbb Q$ {#sec-ta-11-8}

La biyección $\Phi$ ya compara globalmente los dos modelos de los reales. Falta comprobar que esa comparación no desplaza la aritmética racional situada dentro de cada uno. Puesto que ambas construcciones partieron del mismo cuerpo $\mathbb Q$ pero introdujeron sus copias mediante aplicaciones distintas,

$$
\iota_C:\mathbb Q\longrightarrow\mathbb R_C,
\qquad
\iota_D:\mathbb Q\longrightarrow\mathbb R_D,
$$

la afirmación correcta no es una identificación literal de elementos, sino la conmutatividad del triángulo

$$
\mathbb Q
\xrightarrow{\ \iota_C\ }
\mathbb R_C
\xrightarrow{\ \Phi\ }
\mathbb R_D,
$$

es decir,

$$
\Phi\circ\iota_C=\iota_D.
$$

Esta compatibilidad no necesita la sobreyectividad demostrada en §11.7. La traza racional de $\Phi$ y la reflexión del orden por $\iota_C$ ya determinan completamente la imagen de cada racional.

### Proposición 11.8.1 — Compatibilidad de $\Phi$ con las copias racionales

Para todo $q\in\mathbb Q$,

$$
\boxed{
\Phi(\iota_C(q))=\iota_D(q).
}
$$

En consecuencia,

$$
\boxed{
\Phi\circ\iota_C=\iota_D.
}
$$

**Demostración.**

Fijemos $q\in\mathbb Q$. Los dos miembros

$$
\Phi(\iota_C(q)),
\qquad
\iota_D(q)
$$

son elementos de $\mathbb R_D$ y, por tanto, subconjuntos de $\mathbb Q$. Para probar que son la misma cortadura basta comparar sus elementos.

Sea $r\in\mathbb Q$. Por la traza racional de $\Phi$, Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
r\in\Phi(\iota_C(q))
\iff
\iota_C(r)<_C\iota_C(q).
$$

La preservación y reflexión del orden racional por $\iota_C$, Proposición 9.9.5 — Preservación y reflexión del orden racional, transforma esta condición en

$$
\iota_C(r)<_C\iota_C(q)
\iff
r<q.
$$

Por la definición de la cortadura principal $\delta_q$,

$$
r<q
\iff
r\in\delta_q,
$$

y Definición 5.5.1 — Aplicación canónica de $\mathbb Q$ en $\mathbb R_D$ define precisamente

$$
\iota_D(q)=\delta_q.
$$

Así, para todo $r\in\mathbb Q$,

$$
r\in\Phi(\iota_C(q))
\iff
r\in\iota_D(q).
$$

El criterio extensional Teorema 0.2.4 — Criterio extensional por doble inclusión da entonces

$$
\Phi(\iota_C(q))=\iota_D(q).
$$

Como $q$ era arbitrario, ambas funciones

$$
\Phi\circ\iota_C,
\qquad
\iota_D
$$

tienen dominio $\mathbb Q$, codominio $\mathbb R_D$ y coinciden en cada argumento. Por Definición 0.6.4 — Identidad y composición de funciones y el criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones,

$$
\Phi\circ\iota_C=\iota_D.
$$

∎

> **Independencia lógica de §11.7.** La prueba no utiliza Teorema 11.7.6 — Sobreyectividad de $\Phi$ ni Corolario 11.7.7 — Biyectividad de la aplicación canónica. En particular, la compatibilidad con $\mathbb Q$ no se obtiene escogiendo preimágenes mediante la sobreyectividad: es una consecuencia directa de la definición de $\Phi$, de su traza racional y de la manera en que cada modelo incorpora el orden de $\mathbb Q$.

La correspondencia canónica no sólo preserva ya las operaciones y el orden y es biyectiva; además fija exactamente la base racional desde la cual fueron construidos ambos modelos. Esto prepara el último paso: empaquetar todas esas propiedades en una sola afirmación estructural, sin confundir por ello los conjuntos subyacentes.

------

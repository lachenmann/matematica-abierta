## 11.2. Buena definición sobre clases {#sec-ta-11-2}

La función $\Lambda_C$ fue construida deliberadamente sobre $\mathcal C_{\mathbb Q}$ y no sobre $\mathbb R_C$. Por tanto, antes de descenderla al cociente debemos demostrar que su valor no depende de la sucesión racional escogida dentro de una misma clase de Cauchy.

Podríamos intentar probarlo rehaciendo directamente las estimaciones con márgenes racionales de Definición 11.1.1 — Lado inferior asociado a una sucesión racional de Cauchy. Sin embargo, §11.1 ya aisló el contenido exacto de esas estimaciones: por Proposición 11.1.2 — Caracterización mediante el orden de $\mathbb R_C$, pertenecer a $\mathcal L_C(a)$ significa que la copia racional correspondiente está estrictamente por debajo de $[a]_C$. Si dos sucesiones son equivalentes, representan el mismo elemento de $\mathbb R_C$; por tanto deben determinar exactamente el mismo lado inferior racional.

Esta observación no presupone la función $\Phi$. Utiliza únicamente el cociente de Cauchy, ya construido en el Capítulo 9, y la caracterización de §11.1.

### Proposición 11.2.1 — Invariancia del lado inferior bajo equivalencia de Cauchy

Sean

$$
a,b\in\mathcal C_{\mathbb Q}.
$$

Si

$$
a\sim_C b,
$$

entonces

$$
\boxed{
\mathcal L_C(a)=\mathcal L_C(b).
}
$$

En consecuencia,

$$
\boxed{
\Lambda_C(a)=\Lambda_C(b).
}
$$

**Demostración.**

Supongamos

$$
a\sim_C b.
$$

Por el criterio de igualdad de clases de Cauchy, Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy,

$$
[a]_C=[b]_C.
$$

Sea ahora $q\in\mathbb Q$. Aplicando Proposición 11.1.2 — Caracterización mediante el orden de $\mathbb R_C$ a $a$,

$$
q\in\mathcal L_C(a)
\iff
\iota_C(q)<_C[a]_C.
$$

Como $[a]_C=[b]_C$, sustitución de iguales da

$$
\iota_C(q)<_C[a]_C
\iff
\iota_C(q)<_C[b]_C.
$$

Aplicando nuevamente Proposición 11.1.2 — Caracterización mediante el orden de $\mathbb R_C$, ahora a $b$,

$$
\iota_C(q)<_C[b]_C
\iff
q\in\mathcal L_C(b).
$$

Por tanto, para todo $q\in\mathbb Q$,

$$
q\in\mathcal L_C(a)
\iff
q\in\mathcal L_C(b).
$$

Ambos lados son subconjuntos de $\mathbb Q$. Por extensionalidad, en la forma de Teorema 0.2.4 — Criterio extensional por doble inclusión,

$$
\mathcal L_C(a)=\mathcal L_C(b).
$$

Finalmente, Definición 11.1.4 — Aplicación de representantes de Cauchy a cortaduras establece

$$
\Lambda_C(a)=\mathcal L_C(a),
\qquad
\Lambda_C(b)=\mathcal L_C(b),
$$

de modo que

$$
\Lambda_C(a)=\Lambda_C(b).
$$

∎

> **Auditoría de elección.** La prueba no selecciona representantes ni testigos. Parte de dos representantes $a,b$ ya dados y utiliza sólo la igualdad de sus clases, equivalencias lógicas y extensionalidad. `choice-use: none`.

La proposición establece exactamente la condición de compatibilidad exigida para descender una función definida sobre representantes a un cociente. A partir de este punto, $\Lambda_C$ es constante sobre cada clase de $\sim_C$.

---
---

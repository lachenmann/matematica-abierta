## 10.6. Conclusión: la completación de Cauchy de $\mathbb Q$ {#sec-ta-10-6}

La construcción iniciada en el capítulo 8 tenía un objetivo preciso. No bastaba con fabricar un cuerpo que contuviera una copia ordenada de $\mathbb Q$; había que demostrar que el nuevo sistema eliminaba efectivamente la insuficiencia que motivó su introducción.

El camino recorrido ha establecido dos formas de completitud. Primero, Corolario 10.4.8 — $\mathbb R_C$ es secuencialmente completo mostró que toda sucesión de Cauchy en $\mathbb R_C$ converge. Después, Teorema 10.5.8 — Propiedad del supremo de $\mathbb R_C$ y Corolario 10.5.9 — $\mathbb R_C$ es un cuerpo ordenado completo demostraron que todo subconjunto no vacío y acotado superiormente posee supremo. Por tanto, la construcción secuencial ha recuperado exactamente la noción de cuerpo ordenado completo fijada abstractamente en el capítulo 4.

Falta únicamente reunir esa estructura con la incrustación racional ya construida.

### Proposición 10.6.1 — $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$

Se tiene

$$
\boxed{
(\mathbb R_C,\iota_C)
\text{ es una completación ordenada de }\mathbb Q.
}
$$

**Demostración.**

La definición Definición 4.8.2 — Completación ordenada de $\mathbb Q$ exige exactamente dos condiciones.

La primera es que el cuerpo ambiente sea un cuerpo ordenado completo. Esto es Corolario 10.5.9 — $\mathbb R_C$ es un cuerpo ordenado completo:

$$
(\mathbb R_C,+_C,\cdot_C,\le_C)
\text{ es un cuerpo ordenado completo}.
$$

La segunda es que la aplicación estructural

$$
\iota_C:\mathbb Q\longrightarrow\mathbb R_C
$$

sea una incrustación de cuerpos ordenados. Esto es precisamente Corolario 9.10.4 — La aplicación racional es una incrustación de cuerpos ordenados.

Se satisfacen, por tanto, las dos cláusulas de Definición 4.8.2 — Completación ordenada de $\mathbb Q$, y concluimos que

$$
(\mathbb R_C,\iota_C)
$$

es una completación ordenada de $\mathbb Q$. ∎

### Corolario 10.6.2 — Densidad de la copia racional en $\mathbb R_C$

Si

$$
x,y\in\mathbb R_C
\qquad\text{y}\qquad
x<_Cy,
$$

entonces existe $q\in\mathbb Q$ tal que

$$
\boxed{
x<_C\iota_C(q)<_Cy.
}
$$

**Demostración.**

Por Proposición 10.6.1 — $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$, el par $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$. La proposición general Proposición 4.8.3 — La imagen racional de una completación es densa afirma que la imagen racional de toda completación ordenada es densa. Aplicándola a esta completación obtenemos un racional $q$ con

$$
x<_C\iota_C(q)<_Cy.
$$

∎

> **Nota conceptual.** En §10.1 sólo habíamos demostrado que dentro de toda escala positiva de $\mathbb R_C$ cabe una escala racional positiva. Ahora obtenemos la densidad global de la copia racional entre dos elementos arbitrarios del cuerpo. No es una hipótesis añadida a la construcción: es una consecuencia de haber alcanzado la estructura de completación ordenada.

## Cierre del capítulo

La segunda construcción de los números reales queda concluida.

Partimos de la falla secuencial de $\mathbb Q$ y formamos el conjunto de sus sucesiones de Cauchy. Identificamos después dos procesos cuando su diferencia es nula,

$$
a\sim_C b
\iff
a-b\in\mathcal N_{\mathbb Q},
$$

y obtuvimos el cociente

$$
\mathbb R_C
=
\mathcal C_{\mathbb Q}/{\sim_C}.
$$

Sobre ese cociente construimos suma, producto, opuestos, inversos y orden; demostramos que constituye un cuerpo ordenado; incorporamos a $\mathbb Q$ mediante

$$
\iota_C(q)=[\underline q]_C;
$$

construimos después, sin selección numerable de representantes, un límite canónico para toda sucesión de Cauchy de elementos de $\mathbb R_C$; y finalmente dedujimos de esa completitud secuencial la propiedad del supremo.

La cadena estructural obtenida puede resumirse así:

$$
\boxed{
\mathbb Q
\xrightarrow{\ \iota_C\ }
\mathbb R_C
\quad\text{con}\quad
\mathbb R_C
\text{ cuerpo ordenado completo}
}
$$

y, más precisamente,

$$
\boxed{
(\mathbb R_C,\iota_C)
\text{ es una completación ordenada de }\mathbb Q.
}
$$

Toda esta construcción se ha desarrollado sin utilizar la completitud de $\mathbb R_D$, sin convertir una cortadura en un número de Cauchy y sin identificar los dos modelos.

Disponemos ahora de dos objetos construidos independientemente,

$$
(\mathbb R_D,\iota_D)
\qquad\text{y}\qquad
(\mathbb R_C,\iota_C),
$$

cada uno de los cuales realiza una completación ordenada de $\mathbb Q$. El problema siguiente ya no es construir números reales, sino comparar las dos realizaciones y demostrar rigurosamente en qué sentido representan una misma estructura.

Ése será el objeto del **Capítulo 11 — Dedekind y Cauchy**.

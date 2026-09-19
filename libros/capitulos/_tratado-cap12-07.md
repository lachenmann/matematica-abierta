## 12.7. Unicidad {#sec-ta-12-7}

La existencia ya está resuelta: Teorema 12.6.8 — El transporte es un isomorfismo de cuerpos ordenados construyó un isomorfismo de cuerpos ordenados

$$
\Psi_{E,F}:E\longrightarrow F
$$

que hace conmutar las copias racionales. Queda demostrar que esa construcción no dejó ninguna libertad residual.

El argumento de unicidad es más austero que la construcción de $\Psi_{E,F}$. No necesitaremos volver a usar la suma, el producto ni los supremos. Bastará observar que una aplicación que preserve y refleje el orden y que envíe cada racional canónico en su correspondiente racional canónico debe conservar, para cada elemento, exactamente el mismo conjunto de racionales situados por debajo de él. Como §12.5 demostró que esa traza determina al elemento, la aplicación queda forzada punto por punto.

### Proposición 12.7.1 — Una aplicación ordenada que fija los racionales preserva las trazas

Sean $E$ y $F$ cuerpos ordenados y sea

$$
T:E\longrightarrow F
$$

una función tal que, para todos $u,v\in E$,

$$
\boxed{
u<v\iff T(u)<T(v),
}
$$

y, para todo $q\in\mathbb Q$,

$$
\boxed{
T\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\jmath_{\mathbb Q}^{F}(q).
}
$$

Entonces, para todo $x\in E$,

$$
\boxed{
L_F(T(x))=L_E(x).
}
$$

**Demostración.**

Fijemos $x\in E$ y $q\in\mathbb Q$. Por la definición de traza racional inferior Definición 12.4.1 — Traza racional inferior de un elemento,

$$
q\in L_E(x)
\iff
\jmath_{\mathbb Q}^{E}(q)<x.
$$

Como $T$ preserva y refleja el orden estricto,

$$
\jmath_{\mathbb Q}^{E}(q)<x
\iff
T\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)<T(x).
$$

La segunda hipótesis transforma el miembro izquierdo de la última desigualdad:

$$
T\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\jmath_{\mathbb Q}^{F}(q).
$$

Por tanto

$$
q\in L_E(x)
\iff
\jmath_{\mathbb Q}^{F}(q)<T(x)
\iff
q\in L_F(T(x)).
$$

La equivalencia vale para todo $q\in\mathbb Q$. Por extensionalidad,

$$
L_E(x)=L_F(T(x)).
$$

Esto es exactamente la afirmación. ∎

> **Auditoría de elección.** La prueba no introduce testigos ni familias auxiliares. Es una cadena de equivalencias válida para un racional arbitrario; por tanto no interviene ninguna forma de elección.

---

### Teorema 12.7.2 — Unicidad del isomorfismo entre completaciones ordenadas

Sean

$$
(E,\iota_E)
\qquad\text{y}\qquad
(F,\iota_F)
$$

dos completaciones ordenadas de $\mathbb Q$. Existe un único isomorfismo de cuerpos ordenados

$$
T:E\longrightarrow F
$$

que satisface

$$
\boxed{
T\circ\iota_E=\iota_F.
}
$$

Ese isomorfismo es precisamente

$$
\boxed{
T=\Psi_{E,F}.
}
$$

Aquí «isomorfismo de cuerpos ordenados» significa, de acuerdo con la infraestructura ya fijada, una incrustación de cuerpos ordenados en el sentido de Definición 4.8.1 — Incrustación de cuerpos ordenados que además es biyectiva.

**Demostración.**

La existencia está dada por Teorema 12.6.8 — El transporte es un isomorfismo de cuerpos ordenados: la función

$$
\Psi_{E,F}:E\to F
$$

es un isomorfismo de cuerpos ordenados y satisface

$$
\Psi_{E,F}\circ\iota_E=\iota_F.
$$

Probemos la unicidad. Sea

$$
T:E\longrightarrow F
$$

cualquier otro isomorfismo de cuerpos ordenados tal que

$$
T\circ\iota_E=\iota_F.
$$

Por Corolario 12.2.9 — La copia racional de toda completación es la copia canónica, las incrustaciones que forman parte de las completaciones coinciden con las copias racionales canónicas:

$$
\iota_E=\jmath_{\mathbb Q}^{E},
\qquad
\iota_F=\jmath_{\mathbb Q}^{F}.
$$

En consecuencia, para todo $q\in\mathbb Q$,

$$
T\bigl(\jmath_{\mathbb Q}^{E}(q)\bigr)
=
\jmath_{\mathbb Q}^{F}(q).
$$

Además, por Definición 4.8.1 — Incrustación de cuerpos ordenados, toda incrustación de cuerpos ordenados preserva y refleja el orden no estricto. Como es inyectiva, la definición del orden estricto asociado implica también, para todos $u,v\in E$,

$$
u<v
\iff
T(u)<T(v).
$$

Podemos aplicar Proposición 12.7.1 — Una aplicación ordenada que fija los racionales preserva las trazas. Para cada $x\in E$ obtenemos

$$
\boxed{
L_F(T(x))=L_E(x).
}
$$

Por otra parte, la propiedad característica del transporte canónico Teorema 12.4.5 — El transporte reconstruye exactamente la misma traza racional da

$$
\boxed{
L_F\bigl(\Psi_{E,F}(x)\bigr)=L_E(x).
}
$$

Luego

$$
L_F(T(x))
=
L_F\bigl(\Psi_{E,F}(x)\bigr).
$$

Como $F$ es completo, Teorema 4.6.3 — Todo cuerpo ordenado completo es arquimediano implica que es arquimediano. Podemos aplicar Proposición 12.5.1 — La inclusión de trazas racionales caracteriza el orden en $F$. La igualdad de trazas contiene ambas inclusiones, por lo que obtenemos simultáneamente

$$
T(x)\le \Psi_{E,F}(x)
$$

y

$$
\Psi_{E,F}(x)\le T(x).
$$

La antisimetría del orden de $F$ da

$$
T(x)=\Psi_{E,F}(x).
$$

Esto vale para todo $x\in E$. Como $T$ y $\Psi_{E,F}$ tienen el mismo dominio y el mismo codominio, el criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones produce

$$
\boxed{
T=\Psi_{E,F}.
}
$$

Por tanto existe exactamente un isomorfismo de cuerpos ordenados entre las dos completaciones que hace conmutar las copias de $\mathbb Q$. ∎

> **Rigidez sobre $\mathbb Q$.** Tomando $E=F$, el mismo argumento da inmediatamente:
> $$ \boxed{ T:E\to E,\quad T\circ\iota_E=\iota_E \Longrightarrow T=\operatorname{id}_E. } $$
> Es decir, una completación ordenada no posee automorfismos ordenados no triviales que fijen su copia racional canónica. Esta rigidez expresa una forma especialmente fuerte de canonicidad estructural; no afirma decidibilidad ni computabilidad del transporte.

El resultado completa la parte de **unicidad** prometida por el capítulo. La palabra «los reales» ya no designa una codificación privilegiada: cualquier completación ordenada de $\mathbb Q$ posee exactamente la misma estructura, hasta el único isomorfismo compatible con la copia racional.

Todavía falta formular esta conclusión como un teorema de caracterización autónomo. §12.8 reunirá existencia y unicidad en una forma abstracta que permita reconocer a los números reales sin mencionar ni cortaduras de Dedekind ni sucesiones de Cauchy.

---

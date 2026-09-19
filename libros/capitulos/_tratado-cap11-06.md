## 11.6. Inyectividad {#sec-ta-11-6}

La preservación y reflexión del orden obtenidas en la sección anterior impiden que la aplicación canónica colapse dos elementos distintos de $\mathbb R_C$ en una misma cortadura. Conviene aislar esta consecuencia como propiedad formal de $\Phi$, porque constituye la primera mitad de la futura biyectividad.

No introduciremos todavía una función inversa. De acuerdo con la convención general del tratado, la notación $f^{-1}$ para funciones se reserva a funciones invertibles; para $\Phi:\mathbb R_C\to\mathbb R_D$ falta aún demostrar que toda cortadura de Dedekind pertenece a su imagen.

### Proposición 11.6.1 — Igualdad de imágenes e inyectividad de $\Phi$

Para cualesquiera $x,y\in\mathbb R_C$,

$$
\boxed{
\Phi(x)=\Phi(y)
\iff
x=y.
}
$$

En particular,

$$
\boxed{
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
\text{ es inyectiva.}
}
$$

**Demostración.**

La implicación

$$
x=y\Longrightarrow \Phi(x)=\Phi(y)
$$

se sigue inmediatamente de la sustitución de iguales.

Para la implicación recíproca, supongamos

$$
\Phi(x)=\Phi(y).
$$

Como $\le_D$ es reflexivo por la estructura de orden total de $\mathbb R_D$ (Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras), la igualdad anterior implica simultáneamente

$$
\Phi(x)\le_D\Phi(y)
$$

y

$$
\Phi(y)\le_D\Phi(x).
$$

La reflexión del orden no estricto demostrada en Corolario 11.5.2 — Preservación y reflexión del orden no estricto proporciona entonces

$$
x\le_C y
$$

y

$$
y\le_C x.
$$

Puesto que $\le_C$ es un orden total por Teorema 9.8.5 — $\le_C$ es un orden total, en particular es antisimétrico. Por tanto,

$$
x=y.
$$

Hemos probado

$$
\Phi(x)=\Phi(y)
\iff
x=y.
$$

Por la definición de inyectividad Definición 0.6.6 — Inyectividad, sobreyectividad y biyectividad, $\Phi$ es inyectiva. ∎

>
> **Nota de decidibilidad.** La equivalencia
> $$ \Phi(x)=\Phi(y)\iff x=y $$
> es un criterio extensional de igualdad y una prueba de inyectividad. No proporciona un algoritmo que decida igualdad ni en $\mathbb R_C$ ni en $\mathbb R_D$.

La inyectividad muestra que la traducción de Cauchy a Dedekind no pierde información: dos elementos del cociente de Cauchy determinan la misma cortadura únicamente cuando ya eran el mismo elemento de $\mathbb R_C$. Todavía no sabemos, sin embargo, si toda cortadura aparece de esta manera.

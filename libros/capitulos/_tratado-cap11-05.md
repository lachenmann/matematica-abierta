## 11.5. Preservación del orden {#sec-ta-11-5}

La aritmética ya ha sido transportada por $\Phi$, pero la comparación entre los dos modelos no estará estructuralmente completa mientras no sepamos que una desigualdad en $\mathbb R_C$ se traduce exactamente en la desigualdad correspondiente entre cortaduras.

El lema de traza racional de §11.4 permite demostrarlo sin recurrir a las operaciones. La idea es puramente ordinal: si $x<_Cy$, todo racional situado bajo $x$ está también bajo $y$; y la densidad de la copia racional proporciona además un racional situado estrictamente entre ambos, que pertenece a $\Phi(y)$ pero no a $\Phi(x)$. Recíprocamente, si las cortaduras están estrictamente incluidas en el orden contrario al que permitiría $x$ y $y$, la totalidad de $\le_C$ produce una contradicción.

### Proposición 11.5.1 — Preservación y reflexión del orden estricto

Para cualesquiera $x,y\in\mathbb R_C$,

$$
\boxed{
x<_Cy
\iff
\Phi(x)<_D\Phi(y).
}
$$

Equivalentemente, puesto que el orden estricto de Dedekind es inclusión propia,

$$
\boxed{
x<_Cy
\iff
\Phi(x)\subsetneq\Phi(y).
}
$$

**Demostración.**

Supongamos primero

$$
x<_Cy.
$$

Demostraremos que

$$
\Phi(x)\subsetneq\Phi(y).
$$

Sea $q\in\Phi(x)$. Por Lema 11.4.1 — Traza racional de $\Phi(x)$,

$$
\iota_C(q)<_Cx.
$$

La transitividad del orden estricto, junto con $x<_Cy$, da

$$
\iota_C(q)<_Cy.
$$

Aplicando de nuevo Lema 11.4.1 — Traza racional de $\Phi(x)$, obtenemos

$$
q\in\Phi(y).
$$

Por tanto,

$$
\Phi(x)\subseteq\Phi(y).
$$

Falta probar que la inclusión es propia. Como $x<_Cy$ y la copia racional es densa en $\mathbb R_C$ por Corolario 10.6.2 — Densidad de la copia racional en $\mathbb R_C$, existe $r\in\mathbb Q$ tal que

$$
x<_C\iota_C(r)<_Cy.
$$

La segunda desigualdad y Lema 11.4.1 — Traza racional de $\Phi(x)$ implican

$$
r\in\Phi(y).
$$

En cambio,

$$
r\notin\Phi(x).
$$

En efecto, si $r\in\Phi(x)$, el mismo lema daría

$$
\iota_C(r)<_Cx,
$$

contradiciendo $x<_C\iota_C(r)$ por asimetría del orden estricto. Luego

$$
\Phi(x)\subsetneq\Phi(y),
$$

y Corolario 5.4.3 — El orden estricto es inclusión propia proporciona

$$
\Phi(x)<_D\Phi(y).
$$

Probemos ahora la recíproca. Supongamos

$$
\Phi(x)<_D\Phi(y)
$$

y, por contradicción,

$$
\neg(x<_Cy).
$$

Como $\le_C$ es un orden total por Teorema 9.8.5 — $\le_C$ es un orden total, las propiedades del orden estricto asociado (Proposición 0.7.3 — Propiedades del orden estricto asociado) dan

$$
y\le_Cx.
$$

Mostraremos entonces

$$
\Phi(y)\subseteq\Phi(x).
$$

Sea $q\in\Phi(y)$. Por la traza racional,

$$
\iota_C(q)<_Cy.
$$

De $y\le_Cx$ se sigue

$$
\iota_C(q)<_Cx,
$$

y una nueva aplicación de Lema 11.4.1 — Traza racional de $\Phi(x)$ da

$$
q\in\Phi(x).
$$

Así,

$$
\Phi(y)\subseteq\Phi(x).
$$

Pero la hipótesis $\Phi(x)<_D\Phi(y)$ equivale por Corolario 5.4.3 — El orden estricto es inclusión propia a

$$
\Phi(x)\subsetneq\Phi(y),
$$

de modo que también

$$
\Phi(x)\subseteq\Phi(y).
$$

Las dos inclusiones implican por Teorema 0.2.4 — Criterio extensional por doble inclusión

$$
\Phi(x)=\Phi(y),
$$

contradiciendo que la primera inclusión fuese propia. Por tanto,

$$
x<_Cy.
$$

Queda demostrada la equivalencia.

∎

La proposición anterior es más fuerte que una mera monotonía: $\Phi$ **refleja** también el orden estricto. Por tanto ninguna desigualdad estricta puede perderse al pasar de un modelo al otro.

### Corolario 11.5.2 — Preservación y reflexión del orden no estricto

Para cualesquiera $x,y\in\mathbb R_C$,

$$
\boxed{
x\le_Cy
\iff
\Phi(x)\le_D\Phi(y).
}
$$

**Demostración.**

Supongamos primero $x\le_Cy$. Si $x=y$, entonces

$$
\Phi(x)=\Phi(y),
$$

y por reflexividad

$$
\Phi(x)\le_D\Phi(y).
$$

Si $x\neq y$, la definición del orden estricto asociado da

$$
x<_Cy.
$$

Por Proposición 11.5.1 — Preservación y reflexión del orden estricto,

$$
\Phi(x)<_D\Phi(y),
$$

y por tanto

$$
\Phi(x)\le_D\Phi(y).
$$

Recíprocamente, supongamos

$$
\Phi(x)\le_D\Phi(y)
$$

y neguemos $x\le_Cy$. Como $\le_C$ es total, se sigue

$$
y<_Cx.
$$

La proposición anterior produce entonces

$$
\Phi(y)<_D\Phi(x).
$$

En particular,

$$
\Phi(y)\le_D\Phi(x)
$$

y

$$
\Phi(y)\neq\Phi(x).
$$

Pero, junto con $\Phi(x)\le_D\Phi(y)$, la antisimetría del orden de Dedekind (Teorema 5.4.2 — La inclusión ordena totalmente las cortaduras) obliga a

$$
\Phi(x)=\Phi(y),
$$

contradicción. Luego

$$
x\le_Cy.
$$

∎

Es importante mantener todavía separado este resultado de la inyectividad formal. La equivalencia de órdenes contiene ya toda la información necesaria para demostrarla, pero la arquitectura del capítulo reserva esa consecuencia como una unidad propia, de modo que preservación de estructura e inyectividad no queden fusionadas en un único paso.

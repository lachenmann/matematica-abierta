## 11.3. Homomorfismo {#sec-ta-11-3}

El encabezado conserva la arquitectura fijada para el capítulo, pero conviene separar dos afirmaciones. En esta sección construiremos la aplicación canónica de las clases de Cauchy a las cortaduras de Dedekind. Que esa aplicación sea un homomorfismo para la suma y el producto será una propiedad demostrada sólo en §11.4.

La situación construida hasta ahora es exactamente la requerida por el principio general de definición sobre clases. Disponemos de la relación de equivalencia

$$
\sim_C
$$

sobre $\mathcal C_{\mathbb Q}$, del cociente

$$
\mathbb R_C=\mathcal C_{\mathbb Q}/{\sim_C},
$$

y de la función

$$
\Lambda_C:\mathcal C_{\mathbb Q}\longrightarrow\mathbb R_D
$$

que, por Proposición 11.2.1 — Invariancia del lado inferior bajo equivalencia de Cauchy, toma el mismo valor en sucesiones equivalentes. No necesitamos, por tanto, escoger una sucesión distinguida dentro de cada clase: la función buscada debe obtenerse directamente por factorización a través de la proyección canónica del cociente.

### Definición 11.3.1 — Aplicación canónica de Cauchy a Dedekind

Por Proposición 9.3.2 — $\sim_C$ es una relación de equivalencia, $\sim_C$ es una relación de equivalencia sobre $\mathcal C_{\mathbb Q}$, y por Definición 9.4.2 — El conjunto de los reales de Cauchy su cociente es $\mathbb R_C$. La función $\Lambda_C$ está definida en Definición 11.1.4 — Aplicación de representantes de Cauchy a cortaduras, y Proposición 11.2.1 — Invariancia del lado inferior bajo equivalencia de Cauchy demuestra que

$$
a\sim_C b
\Longrightarrow
\Lambda_C(a)=\Lambda_C(b).
$$

Aplicando el principio de definición sobre clases, Teorema 0.6.15 — Principio de definición sobre clases, existe una única función

$$
\boxed{
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
}
$$

tal que

$$
\boxed{
\Phi\circ\pi_{\sim_C}=\Lambda_C,
}
$$

donde

$$
\pi_{\sim_C}:\mathcal C_{\mathbb Q}\longrightarrow\mathbb R_C
$$

es la proyección canónica del cociente.

Definimos $\Phi$ como esa única función inducida. Para todo $a\in\mathcal C_{\mathbb Q}$ se tiene entonces

$$
\pi_{\sim_C}(a)=[a]_C,
$$

y por tanto

$$
\boxed{
\Phi([a]_C)
=
\Lambda_C(a)
=
\mathcal L_C(a).
}
$$

La fórmula anterior debe leerse con cuidado. No afirma que una clase $[a]_C$ sea una cortadura, ni que $a$ sea un representante privilegiado. Afirma que la función $\Phi$ envía la clase completa al único lado inferior racional determinado por cualquiera de sus representantes.

### Proposición 11.3.2 — Caracterización universal de $\Phi$

Sea

$$
\Psi:\mathbb R_C\longrightarrow\mathbb R_D
$$

una función. Entonces

$$
\boxed{
\Psi=\Phi
\iff
\forall a\in\mathcal C_{\mathbb Q},
\quad
\Psi([a]_C)=\mathcal L_C(a).
}
$$

**Demostración.**

Si $\Psi=\Phi$, entonces para todo $a\in\mathcal C_{\mathbb Q}$,

$$
\Psi([a]_C)
=
\Phi([a]_C)
=
\mathcal L_C(a)
$$

por Definición 11.3.1 — Aplicación canónica de Cauchy a Dedekind.

Recíprocamente, supongamos que

$$
\forall a\in\mathcal C_{\mathbb Q},
\qquad
\Psi([a]_C)=\mathcal L_C(a).
$$

Para demostrar $\Psi=\Phi$, fijemos un elemento arbitrario

$$
x\in\mathbb R_C.
$$

Por Proposición 9.4.4 — Representantes y criterio de igualdad de clases de Cauchy, existe una sucesión $a\in\mathcal C_{\mathbb Q}$ tal que

$$
x=[a]_C.
$$

Para este representante local,

$$
\Psi(x)
=
\Psi([a]_C)
=
\mathcal L_C(a),
$$

mientras que Definición 11.3.1 — Aplicación canónica de Cauchy a Dedekind da

$$
\Phi(x)
=
\Phi([a]_C)
=
\mathcal L_C(a).
$$

Por consiguiente,

$$
\Psi(x)=\Phi(x).
$$

Como $x\in\mathbb R_C$ era arbitrario, ambas funciones coinciden en todo su dominio. El criterio de igualdad de funciones Proposición 0.6.3 — Criterio de igualdad de funciones proporciona

$$
\Psi=\Phi.
$$

∎

La caracterización universal muestra que $\Phi$ no depende de una presentación particular del cociente. Es la única función $\mathbb R_C\to\mathbb R_D$ cuyo valor sobre una clase de Cauchy es la cortadura producida por cualquiera de sus representantes.

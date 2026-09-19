## 11.9. Conclusión {#sec-ta-11-9}

Las secciones anteriores han establecido por separado todas las propiedades que debe poseer la comparación entre los dos modelos. Conviene ahora reunirlas en una única afirmación estructural. Para hacerlo sin introducir terminología implícita, fijaremos primero qué entenderemos por isomorfismo de cuerpos ordenados.

### Definición 11.9.1 — Isomorfismo de cuerpos ordenados

Sean $F$ y $E$ cuerpos ordenados. Una función

$$
T:F\longrightarrow E
$$

es un **isomorfismo de cuerpos ordenados** si:

1. $T$ es una incrustación de cuerpos ordenados en el sentido de Definición 4.8.1 — Incrustación de cuerpos ordenados;
2. $T$ es biyectiva.

Como una incrustación ya es inyectiva, la segunda condición puede sustituirse equivalentemente por la sobreyectividad de $T$.

Cuando las estructuras de cuerpo y orden estén fijadas sin ambigüedad, escribiremos

$$
F\cong E
$$

para afirmar que existe un isomorfismo de cuerpos ordenados entre $F$ y $E$.

El símbolo $\cong$ expresa equivalencia estructural, no igualdad conjuntista. En particular, de $F\cong E$ no se sigue que $F=E$ como conjuntos.

### Notación 11.9.2 — Inversa de la comparación canónica

Por Corolario 11.7.7 — Biyectividad de la aplicación canónica,

$$
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
$$

es biyectiva. Por la caracterización de las funciones invertibles Teorema 0.6.7 — Caracterización de las funciones invertibles, existe por tanto su función inversa. Activamos desde ahora la notación

$$
\boxed{
\Phi^{-1}:\mathbb R_D\longrightarrow\mathbb R_C.
}
$$

De acuerdo con Notación 0.6.8 — Función inversa, satisface

$$
\Phi^{-1}\circ\Phi=\operatorname{id}_{\mathbb R_C},
\qquad
\Phi\circ\Phi^{-1}=\operatorname{id}_{\mathbb R_D}.
$$

No hay aquí elección de preimágenes: la inversa de una biyección está determinada unívocamente por su grafo inverso.

### Proposición 11.9.3 — Fórmula explícita para la inversa

Para toda cortadura $\alpha\in\mathbb R_D$,

$$
\boxed{
\Phi^{-1}(\alpha)
=
\left[\operatorname{seq}_D(\alpha)\right]_C.
}
$$

**Demostración.**

Fijemos $\alpha\in\mathbb R_D$ y pongamos

$$
x_\alpha
:=
\left[\operatorname{seq}_D(\alpha)\right]_C.
$$

La construcción de §11.7 da, por Teorema 11.7.6 — Sobreyectividad de $\Phi$,

$$
\Phi(x_\alpha)=\alpha.
$$

Aplicando $\Phi^{-1}$ a ambos miembros y usando

$$
\Phi^{-1}\circ\Phi=\operatorname{id}_{\mathbb R_C},
$$

obtenemos

$$
\Phi^{-1}(\alpha)
=
\Phi^{-1}(\Phi(x_\alpha))
=
x_\alpha
=
\left[\operatorname{seq}_D(\alpha)\right]_C.
$$

Esto prueba la fórmula. ∎

### Teorema 11.9.4 — Isomorfismo canónico entre las completaciones de Cauchy y Dedekind

La aplicación canónica

$$
\Phi:\mathbb R_C\longrightarrow\mathbb R_D
$$

es un isomorfismo de cuerpos ordenados. Además, las dos estructuras son cuerpos ordenados completos y la comparación fija la copia racional en el sentido de que

$$
\boxed{
\Phi\circ\iota_C=\iota_D.
}
$$

En consecuencia, las dos construcciones son isomorfas como completaciones ordenadas de $\mathbb Q$:

$$
\boxed{
\mathbb R_C\cong\mathbb R_D
}
$$

mediante un isomorfismo que fija canónicamente a $\mathbb Q$.

**Demostración.**

Por Proposición 10.6.1 — $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$, $(\mathbb R_C,\iota_C)$ es una completación ordenada de $\mathbb Q$; por Proposición 7.5.3 — El modelo de Dedekind es una completación ordenada de $\mathbb Q$, también lo es $(\mathbb R_D,\iota_D)$. En particular, ambos dominios son cuerpos ordenados completos y ambas aplicaciones racionales son incrustaciones de cuerpos ordenados.

Verifiquemos ahora las condiciones de Definición 4.8.1 — Incrustación de cuerpos ordenados para $\Phi$.

**Inyectividad.** Corolario 11.7.7 — Biyectividad de la aplicación canónica afirma incluso que $\Phi$ es biyectiva.

**Cero.** Por Corolario 11.4.3 — Preservación del cero y del opuesto,

$$
\Phi(0_C)=0_D.
$$

**Unidad.** La compatibilidad de $\iota_C$ con la aritmética racional, Proposición 9.9.3 — Preservación de la aritmética racional, da

$$
\iota_C(1_{\mathbb Q})=1_C,
$$

mientras que Definición 6.6.1 — Unidad de Dedekind fija

$$
\iota_D(1_{\mathbb Q})=1_D.
$$

Aplicando Proposición 11.8.1 — Compatibilidad de $\Phi$ con las copias racionales al racional $1_{\mathbb Q}$,

$$
\Phi(1_C)
=
\Phi(\iota_C(1_{\mathbb Q}))
=
\iota_D(1_{\mathbb Q})
=
1_D.
$$

**Suma y producto.** Para todos $x,y\in\mathbb R_C$, Proposición 11.4.2 — Preservación de la suma y Proposición 11.4.5 — Preservación del producto dan

$$
\Phi(x+y)=\Phi(x)+_D\Phi(y),
$$

$$
\Phi(xy)=\Phi(x)\cdot_D\Phi(y).
$$

**Orden.** Por Corolario 11.5.2 — Preservación y reflexión del orden no estricto, para todos $x,y\in\mathbb R_C$,

$$
x\le_Cy
\iff
\Phi(x)\le_D\Phi(y).
$$

Así, $\Phi$ es una incrustación de cuerpos ordenados. Como además es biyectiva, Definición 11.9.1 — Isomorfismo de cuerpos ordenados implica que $\Phi$ es un isomorfismo de cuerpos ordenados.

Finalmente, Proposición 11.8.1 — Compatibilidad de $\Phi$ con las copias racionales ya estableció

$$
\Phi\circ\iota_C=\iota_D.
$$

Por tanto el isomorfismo no sólo compara las estructuras completas: identifica estructuralmente las dos copias del mismo cuerpo racional sin identificar los conjuntos subyacentes. ∎

> **Sobre la palabra «canónico».** En este capítulo significa que $\Phi$ fue construida explícitamente a partir de las dos realizaciones y que conmuta con las incrustaciones racionales. No estamos afirmando todavía un teorema general de unicidad para toda completación ordenada de $\mathbb Q$; ése será precisamente el objetivo del capítulo siguiente.
>
> Tampoco debe confundirse esta canonicidad estructural con una equivalencia computacional automática de códigos:
> $$ \boxed{ \text{isomorfía estructural} \neq \text{conversión computable entre presentaciones arbitrarias}. } $$
> Una equivalencia efectiva entre nombres de Cauchy y cortaduras localizadas requiere datos intensionales adicionales y pertenece a la capa P1.

## Cierre del capítulo

Las dos vías de construcción iniciadas después de la incompletitud de $\mathbb Q$ han convergido finalmente en una misma estructura, pero no en un mismo conjunto.

El modelo de Dedekind representa un real por su **lado inferior racional**. El modelo de Cauchy lo representa por una **clase de procesos racionales de aproximación**. El teorema anterior demuestra que ambas codificaciones transportan exactamente la misma aritmética y el mismo orden, y que la correspondencia entre ellas respeta la copia racional desde la cual fueron construidas.

Por ello, a partir de este punto podemos hablar de **los números reales** estructuralmente sin borrar la historia de sus construcciones. Cuando una afirmación dependa de una realización concreta conservaremos los subíndices $D$ o $C$; cuando dependa sólo de la estructura de cuerpo ordenado completo, el capítulo siguiente explicará por qué esa independencia de modelo puede formularse y demostrarse de manera general.

El problema que queda abierto ya no es comparar estas dos construcciones particulares. Es demostrar que **cualquier** cuerpo ordenado completo que contenga una copia adecuada de $\mathbb Q$ posee, esencialmente, la misma estructura. Éste será el contenido del Capítulo 12: la caracterización y unicidad estructural de los números reales.

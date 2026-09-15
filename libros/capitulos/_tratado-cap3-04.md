## 3.4. Producto y estructura de cuerpo {#sec-ta-3-4}

La multiplicación racional debe construirse con la misma cautela que la suma: primero sobre representantes y sólo después sobre clases. La fórmula esperada

$$
\frac ab\cdot\frac cd
=
\frac{ac}{bd}
$$

sólo será una operación sobre $\mathbb Q$ una vez comprobado que el denominador resultante sigue siendo no nulo y que el valor no depende de los representantes elegidos.

### Definición 3.4.1 — Producto de representantes racionales {#ta-producto-representantes-racionales}

Definimos

$$
\mu_{\mathbb Q}:D_{\mathbb Q}\times D_{\mathbb Q}\to D_{\mathbb Q}
$$

por

$$
\boxed{
\mu_{\mathbb Q}\bigl((a,b),(c,d)\bigr):=(ac,bd).
}
$$

El denominador $bd$ es no nulo porque $b$ y $d$ son no nulos y $\mathbb Z$ carece de divisores de cero.

### Proposición 3.4.2 — Compatibilidad del producto con $\sim_{\mathbb Q}$ {#ta-compatibilidad-producto-racional}

Si

$$
(a,b)\sim_{\mathbb Q}(a',b')
\qquad\text{y}\qquad
(c,d)\sim_{\mathbb Q}(c',d'),
$$

entonces

$$
(ac,bd)\sim_{\mathbb Q}(a'c',b'd').
$$

**Demostración.**  
De

$$
ab'=ba',
\qquad
cd'=dc'
$$

se obtiene

$$
(ac)(b'd')
=
(ab')(cd')
=
(ba')(dc')
=
(bd)(a'c').
$$

Por definición de $\sim_{\mathbb Q}$, los productos son equivalentes. ∎

### Definición 3.4.3 — Multiplicación en $\mathbb Q$ {#ta-multiplicacion-racional}

*Glosario: [multiplicación racional](../otros/tratado-de-analisis-glosario.md#gl-multiplicacion-racional)*

La composición de $\mu_{\mathbb Q}$ con la proyección canónica $D_{\mathbb Q}\to\mathbb Q$ es invariante en ambos representantes por la Proposición 3.4.2. Aplicando sucesivamente a cada variable el [Teorema 0.6.15 — Principio de definición sobre clases](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-definicion-sobre-clases), obtenemos una única función

$$
\cdot_{\mathbb Q}:\mathbb Q\times\mathbb Q\to\mathbb Q
$$

satisfaciendo

$$
\boxed{
\frac ab\cdot\frac cd
=
\frac{ac}{bd}.
}
$$

Cuando el tipo sea inequívoco escribiremos simplemente $xy$ o $x\cdot y$.

### Notación 3.4.4 — Unidad racional {#ta-unidad-racional}

*Glosario: [unidad racional](../otros/tratado-de-analisis-glosario.md#gl-unidad-racional)*

Definimos

$$
\boxed{
1_{\mathbb Q}:=\frac{1_{\mathbb Z}}{1_{\mathbb Z}}.
}
$$

### Proposición 3.4.5 — Leyes multiplicativas y distributivas {#ta-leyes-multiplicativas-distributivas-racionales}

Para $x,y,z\in\mathbb Q$:

1. $(xy)z=x(yz)$;
2. $xy=yx$;
3. $1_{\mathbb Q}x=x=x1_{\mathbb Q}$;
4. $x(y+z)=xy+xz$;
5. $(x+y)z=xz+yz$.

**Demostración.**  
Sean $x=a/b$, $y=c/d$ y $z=e/f$. Asociatividad, conmutatividad y unidad se siguen directamente de las correspondientes leyes enteras:

$$
\left(\frac ab\frac cd\right)\frac ef
=
\frac{ace}{bdf}
=
\frac ab\left(\frac cd\frac ef\right),
$$

$$
\frac ab\frac cd
=
\frac{ac}{bd}
=
\frac{ca}{db}
=
\frac cd\frac ab,
$$

y

$$
1_{\mathbb Q}\frac ab
=
\frac ab.
$$

Para la distributividad,

$$
\frac ab\left(\frac cd+\frac ef\right)
=
\frac ab\frac{cf+de}{df}
=
\frac{acf+ade}{bdf}.
$$

Por otra parte,

$$
\frac{ac}{bd}+
\frac{ae}{bf}
=
\frac{acbf+aebd}{b^2df}.
$$

Para justificar formalmente el cambio de representante, el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) da

$$
\frac{acf+ade}{bdf}
=
\frac{b(acf+ade)}{b(bdf)},
$$

porque

$$
(acf+ade)\,b(bdf)
=
b(acf+ade)\,(bdf)
$$

por asociatividad y conmutatividad en $\mathbb Z$. Con la notación $b^2=bb$ y distribuyendo el numerador,

$$
\frac{b(acf+ade)}{b^2df}
=
\frac{abcf+abde}{b^2df},
$$

que coincide con la segunda fracción por conmutatividad de los factores enteros. La distributividad del otro lado se deduce de la conmutatividad del producto. ∎

### Proposición 3.4.6 — Distinción entre cero y uno {#ta-cero-uno-racionales-distintos}

Se tiene

$$
\boxed{0_{\mathbb Q}\neq1_{\mathbb Q}.}
$$

**Demostración.**  
Si $0_{\mathbb Q}=1_{\mathbb Q}$, el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) daría

$$
0_{\mathbb Z}\cdot1_{\mathbb Z}
=
1_{\mathbb Z}\cdot1_{\mathbb Z}.
$$

Por las [leyes multiplicativas de $\mathbb Z$](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-leyes-multiplicativas-distributivas-enteros), el miembro izquierdo es $0_{\mathbb Z}$ y el derecho es $1_{\mathbb Z}$. Obtendríamos, pues,

$$
0_{\mathbb Z}=1_{\mathbb Z},
$$

contradiciendo la [Proposición 2.8.2 — $0_{\mathbb Z}\neq1_{\mathbb Z}$](tratado-de-analisis-capitulo-2-los-numeros-enteros.md#ta-cero-uno-enteros-distintos). ∎

---

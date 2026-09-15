## 3.3. Suma, cero, opuesto y sustracción {#sec-ta-3-3}

La fórmula heurística

$$
\frac ab+\frac cd=\frac{ad+bc}{bd}
$$

sólo puede convertirse en definición si $bd\neq0$ y si el resultado no depende de los representantes elegidos. Esta sección realiza precisamente ese paso: primero trabajamos en $D_{\mathbb Q}$ y sólo después hacemos descender las construcciones al cociente $\mathbb Q$.

### Definición 3.3.1 — Suma de representantes racionales {#ta-suma-representantes-racionales}

Definimos

$$
\sigma_{\mathbb Q}:D_{\mathbb Q}\times D_{\mathbb Q}\to D_{\mathbb Q}
$$

por

$$
\boxed{
\sigma_{\mathbb Q}\bigl((a,b),(c,d)\bigr)
:=
(ad+bc,\;bd).
}
$$

Como $b,d\neq0_{\mathbb Z}$ y $\mathbb Z$ no tiene divisores de cero, $bd\neq0_{\mathbb Z}$; por tanto la imagen pertenece realmente a $D_{\mathbb Q}$.

### Proposición 3.3.2 — Compatibilidad de la suma con $\sim_{\mathbb Q}$ {#ta-compatibilidad-suma-racional}

Si

$$
(a,b)\sim_{\mathbb Q}(a',b')
\qquad\text{y}\qquad
(c,d)\sim_{\mathbb Q}(c',d'),
$$

entonces

$$
(ad+bc,bd)
\sim_{\mathbb Q}
(a'd'+b'c',b'd').
$$

**Demostración.**  
Las hipótesis dicen

$$
ab'=ba',
\qquad
cd'=dc'.
$$

Debemos demostrar

$$
(ad+bc)(b'd')
=
(bd)(a'd'+b'c').
$$

Por distributividad, asociatividad y conmutatividad en $\mathbb Z$,

$$
\begin{aligned}
(ad+bc)(b'd')
&=ad\,b'd'+bc\,b'd'\\
&=(ab')dd'+bb'(cd')\\
&=(ba')dd'+bb'(dc')\\
&=bd(a'd')+bd(b'c')\\
&=bd(a'd'+b'c').
\end{aligned}
$$

Ésta es exactamente la condición de equivalencia. ∎

### Definición 3.3.3 — Suma en $\mathbb Q$ {#ta-suma-racional}

*Glosario: [suma racional](../otros/tratado-de-analisis-glosario.md#gl-suma-racional)*

La composición de $\sigma_{\mathbb Q}$ con la proyección canónica $D_{\mathbb Q}\to\mathbb Q$ es invariante en ambos representantes por la Proposición 3.3.2. Aplicando sucesivamente a cada variable el [Teorema 0.6.15 — Principio de definición sobre clases](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-definicion-sobre-clases), obtenemos una única función

$$
+_{\mathbb Q}:\mathbb Q\times\mathbb Q\to\mathbb Q
$$

tal que

$$
\boxed{
\frac ab+\frac cd
=
\frac{ad+bc}{bd}.
}
$$

Cuando el tipo sea inequívoco escribiremos simplemente $x+y$.

### Notación 3.3.4 — Cero racional {#ta-cero-racional}

*Glosario: [cero racional](../otros/tratado-de-analisis-glosario.md#gl-cero-racional)*

Definimos

$$
\boxed{
0_{\mathbb Q}:=\frac{0_{\mathbb Z}}{1_{\mathbb Z}}.
}
$$

### Definición 3.3.5 — Opuesto sobre representantes {#ta-opuesto-representantes-racionales}

Definimos

$$
\eta_{\mathbb Q}:D_{\mathbb Q}\to D_{\mathbb Q},
\qquad
\eta_{\mathbb Q}(a,b):=(-a,b).
$$

El denominador no cambia y sigue siendo no nulo.

### Proposición 3.3.6 — Compatibilidad del opuesto {#ta-compatibilidad-opuesto-racional}

Si $(a,b)\sim_{\mathbb Q}(c,d)$, entonces

$$
(-a,b)\sim_{\mathbb Q}(-c,d).
$$

**Demostración.**  
La hipótesis es $ad=bc$. Multiplicando ambos miembros por $-1_{\mathbb Z}$, o equivalentemente usando las leyes del opuesto en el anillo $\mathbb Z$,

$$
(-a)d=b(-c).
$$

Ésta es la condición requerida. ∎

### Definición 3.3.7 — Opuesto en $\mathbb Q$ {#ta-opuesto-racional}

*Glosario: [opuesto racional](../otros/tratado-de-analisis-glosario.md#gl-opuesto-racional)*

Sea

$$
\pi_{\mathbb Q}:D_{\mathbb Q}\to\mathbb Q
$$

la proyección canónica. La composición

$$
\pi_{\mathbb Q}\circ\eta_{\mathbb Q}:D_{\mathbb Q}\to\mathbb Q
$$

es constante sobre clases por la Proposición 3.3.6. Aplicando el [Teorema 0.6.15 — Principio de definición sobre clases](tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md#ta-definicion-sobre-clases) a esta composición —no a $\eta_{\mathbb Q}$ aislada— existe una única función

$$
-:\mathbb Q\to\mathbb Q
$$

tal que

$$
\boxed{
-\frac ab=\frac{-a}{b}.
}
$$

### Proposición 3.3.8 — Leyes del grupo aditivo racional {#ta-grupo-aditivo-racional}

Para $x,y,z\in\mathbb Q$:

1. $(x+y)+z=x+(y+z)$;
2. $x+y=y+x$;
3. $x+0_{\mathbb Q}=x=0_{\mathbb Q}+x$;
4. $x+(-x)=0_{\mathbb Q}=(-x)+x$.

En consecuencia,

$$
\boxed{(\mathbb Q,+,0_{\mathbb Q})\text{ es un grupo abeliano}.}
$$

**Demostración.**  
Sean

$$
x=\frac ab,\qquad
y=\frac cd,\qquad
z=\frac ef.
$$

Para la asociatividad,

$$
(x+y)+z
=
\frac{(ad+bc)f+(bd)e}{bdf},
$$

mientras que

$$
x+(y+z)
=
\frac{a(df)+b(cf+de)}{bdf}.
$$

Los numeradores son iguales por distributividad, asociatividad y conmutatividad en $\mathbb Z$:

$$
adf+bcf+bde
=
adf+bcf+bde.
$$

La conmutatividad se obtiene de

$$
\frac ab+\frac cd
=
\frac{ad+bc}{bd}
=
\frac{cb+da}{db}
=
\frac cd+\frac ab.
$$

Para el neutro,

$$
\frac ab+0_{\mathbb Q}
=
\frac{a1_{\mathbb Z}+b0_{\mathbb Z}}{b1_{\mathbb Z}}
=
\frac ab.
$$

Finalmente,

$$
\frac ab+\left(-\frac ab\right)
=
\frac{ab+b(-a)}{b^2}
=
\frac{0_{\mathbb Z}}{b^2}.
$$

Como $b\neq0_{\mathbb Z}$, la ausencia de divisores de cero en $\mathbb Z$ implica

$$
b^2=bb\neq0_{\mathbb Z}.
$$

Además, el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) da

$$
\frac{0_{\mathbb Z}}{b^2}
=
\frac{0_{\mathbb Z}}{1_{\mathbb Z}},
$$

porque los productos cruzados son ambos $0_{\mathbb Z}$; la absorción del cero se obtiene de las leyes de anillo ya demostradas. Por tanto obtenemos el opuesto aditivo. El otro lado se sigue de conmutatividad. ∎

### Definición 3.3.9 — Sustracción racional {#ta-sustraccion-racional}

*Glosario: [sustracción racional](../otros/tratado-de-analisis-glosario.md#gl-sustraccion-racional)*

Para $x,y\in\mathbb Q$ definimos

$$
\boxed{
x-y:=x+(-y).
}
$$

---

::: {.callout-note title="Publicación progresiva"}
Con §3.3 la suma y el opuesto han descendido rigurosamente desde los representantes al cociente, y $\mathbb Q$ ya posee estructura de **grupo abeliano aditivo**. La siguiente entrega será **§3.4 — Producto y estructura de cuerpo**.
:::

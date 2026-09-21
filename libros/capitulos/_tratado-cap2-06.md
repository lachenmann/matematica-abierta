## 2.6. Estructura algebraica {#sec-ta-2-6}

Ya hemos construido la suma y la multiplicación de enteros como operaciones genuinas sobre clases. Falta demostrar que estas operaciones satisfacen las leyes algebraicas que permitirán reconocer la estructura obtenida.

### Proposición 2.6.1 — Leyes multiplicativas y distributivas {#ta-leyes-multiplicativas-distributivas-enteros}

Para todos $x,y,z\in\mathbb Z$:

1. $(xy)z=x(yz)$;
2. $xy=yx$;
3. $1_{\mathbb Z}x=x=x1_{\mathbb Z}$;
4. $x(y+z)=xy+xz$;
5. $(x+y)z=xz+yz$.

**Demostración.**  
Sean

$$
x=[(a,b)],\qquad y=[(c,d)],\qquad z=[(e,f)].
$$

**Conmutatividad.** Directamente,

$$
xy
=
[(ac+bd,ad+bc)]
=
[(ca+db,cb+da)]
=
yx.
$$

**Unidad.** Tenemos

$$
1_{\mathbb Z}x
=
[(1,0)][(a,b)]
=
[(1a+0b,1b+0a)]
=
[(a,b)]
=
x,
$$

y el otro lado se sigue de conmutatividad.

**Asociatividad.** El primer componente de $(xy)z$ es

$$
(ac+bd)e+(ad+bc)f
=
ace+bde+adf+bcf,
$$

mientras que el primer componente de $x(yz)$ es

$$
a(ce+df)+b(cf+de)
=
ace+adf+bcf+bde.
$$

Son iguales por las leyes de $\mathbb N$.

El segundo componente de $(xy)z$ es

$$
(ac+bd)f+(ad+bc)e
=
acf+bdf+ade+bce,
$$

y el segundo componente de $x(yz)$ es

$$
a(cf+de)+b(ce+df)
=
acf+ade+bce+bdf.
$$

También son iguales. Por tanto las dos clases coinciden.

**Distributividad.** Es suficiente probar la distributividad por un lado; la otra se deducirá de conmutatividad.

Como

$$
y+z=[(c+e,d+f)],
$$

tenemos

$$
x(y+z)
=
[(a(c+e)+b(d+f),\;a(d+f)+b(c+e))].
$$

Distribuyendo en $\mathbb N$,

$$
x(y+z)
=
[(ac+ae+bd+bf,\;ad+af+bc+be)].
$$

Por otra parte,

$$
xy+xz
=
[(ac+bd,ad+bc)]+[(ae+bf,af+be)]
$$

$$
=
[(ac+bd+ae+bf,\;ad+bc+af+be)],
$$

que es la misma clase, incluso con componentes literalmente iguales después de reordenar sumas naturales. La distributividad por el otro lado se sigue de la conmutatividad del producto. ∎

### Convención 2.6.2 — Terminología algebraica {#ta-terminologia-algebraica}

Para evitar que la terminología estructural introduzca hipótesis silenciosas, fijamos aquí las convenciones que se usarán en el tratado.

Un [grupo abeliano](../otros/tratado-de-analisis-glosario.md#gl-grupo-abeliano) es un conjunto $G$ provisto de una operación binaria $+$ y de un elemento $0_G$ tales que la operación es asociativa y conmutativa, $0_G$ es neutro y todo elemento $x\in G$ posee un opuesto aditivo $-x$.

Un [anillo](../otros/tratado-de-analisis-glosario.md#gl-anillo) será un conjunto $R$ provisto de dos operaciones binarias $+$ y $\cdot$, y de elementos $0_R$ y $1_R$, tal que $(R,+,0_R)$ es un grupo abeliano, la multiplicación es asociativa, $1_R$ es unidad multiplicativa y la multiplicación distribuye respecto de la suma por ambos lados. En particular, en este tratado los anillos tienen unidad.

Un [anillo conmutativo](../otros/tratado-de-analisis-glosario.md#gl-anillo-conmutativo) es un anillo cuya multiplicación es conmutativa.

Un [dominio de integridad](../otros/tratado-de-analisis-glosario.md#gl-dominio-integridad) es un anillo conmutativo tal que $0_R\neq1_R$ y

$$
xy=0_R\Longrightarrow x=0_R\ \text{o}\ y=0_R.
$$

La conmutatividad de la multiplicación no queda incluida en la palabra «anillo» y se enunciará cuando corresponda.

### Teorema 2.6.3 — Primera estructura de anillo de $\mathbb Z$ {#ta-anillo-conmutativo-enteros}

Con las operaciones ya construidas, y con $0_{\mathbb Z}$ y $1_{\mathbb Z}$, el sistema

$$
\boxed{
(\mathbb Z,+,\cdot,0_{\mathbb Z},1_{\mathbb Z})
}
$$

es un [anillo conmutativo](../otros/tratado-de-analisis-glosario.md#gl-anillo-conmutativo) con identidad.

**Demostración.**  
Las leyes del grupo aditivo demostradas en §2.4 establecen que $(\mathbb Z,+,0_{\mathbb Z})$ es un grupo abeliano. La Proposición 2.6.1 demuestra asociatividad y conmutatividad del producto, existencia de la unidad multiplicativa y distributividad respecto de la suma. Éstas son exactamente las leyes exigidas por la convención anterior. ∎

Este teorema resume una estructura, pero no reemplaza sus pruebas. La información matemática está en las proposiciones que lo preceden.

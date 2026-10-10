## 2.4. Cero, opuesto y sustracción {#sec-ta-2-4}

### Notación 2.4.1 — Cero entero {#ta-cero-entero}

*Glosario: [cero entero](../otros/tratado-de-analisis-glosario.md#gl-cero-entero)*

Definimos

$$
\boxed{
0_{\mathbb Z}:=[(0,0)].
}
$$

No identificamos todavía este objeto con el $0\in\mathbb N$. Son objetos pertenecientes a sistemas distintos.

### Definición 2.4.2 — Opuesto {#ta-opuesto-enteros}

*Glosario: [opuesto entero](../otros/tratado-de-analisis-glosario.md#gl-opuesto-entero)*

Sobre representantes consideramos la función de intercambio

$$
\tau:\mathbb N\times\mathbb N\to\mathbb N\times\mathbb N,
\qquad
\tau(a,b):=(b,a).
$$

La operación de opuesto en $\mathbb Z$ será la función inducida por $\tau$ después de proyectar al cociente.

### Proposición 2.4.3 — Buena definición del opuesto {#ta-buena-definicion-opuesto}

Si

$$
(a,b)\sim_{\mathbb Z}(c,d),
$$

entonces

$$
(b,a)\sim_{\mathbb Z}(d,c).
$$

Por tanto existe una única función

$$
-:\mathbb Z\to\mathbb Z
$$

satisfaciendo

$$
\boxed{
-[(a,b)]=[(b,a)].
}
$$

**Demostración.**  
La hipótesis

$$
(a,b)\sim_{\mathbb Z}(c,d)
$$

equivale a

$$
a+d=b+c.
$$

La condición

$$
(b,a)\sim_{\mathbb Z}(d,c)
$$

exige

$$
b+c=a+d,
$$

que es la misma igualdad escrita en el orden contrario.

Para aplicar con precisión el principio de definición sobre clases, sea

$$
\pi_{\mathbb Z}:\mathbb N\times\mathbb N\to\mathbb Z,
\qquad
\pi_{\mathbb Z}(a,b):=[(a,b)]
$$

la proyección canónica, y definamos

$$
\varphi:=\pi_{\mathbb Z}\circ\tau.
$$

Entonces

$$
\varphi(a,b)=[(b,a)].
$$

La compatibilidad que acabamos de demostrar dice exactamente que

$$
(a,b)\sim_{\mathbb Z}(c,d)
\quad\Longrightarrow\quad
\varphi(a,b)=\varphi(c,d).
$$

Por el principio general de definición sobre clases existe una única función

$$
-:\mathbb Z\to\mathbb Z
$$

tal que

$$
-([(a,b)])=\varphi(a,b)=[(b,a)].
$$

Ésta es la operación de opuesto anunciada. ∎

### Proposición 2.4.4 — Leyes del grupo aditivo {#ta-grupo-aditivo-enteros}

*Glosario: [grupo abeliano](../otros/tratado-de-analisis-glosario.md#gl-grupo-abeliano)*

Para todos $x,y,z\in\mathbb Z$:

1. $(x+y)+z=x+(y+z)$;
2. $x+y=y+x$;
3. $x+0_{\mathbb Z}=x=0_{\mathbb Z}+x$;
4. $x+(-x)=0_{\mathbb Z}=(-x)+x$.

En consecuencia, la suma convierte a $\mathbb Z$ en un grupo abeliano.

**Demostración.**  
Sean

$$
x=[(a,b)],\qquad y=[(c,d)],\qquad z=[(e,f)].
$$

Para la asociatividad,

$$
(x+y)+z
=
[(a+c,b+d)]+[(e,f)]
=
[(a+c)+e,(b+d)+f],
$$

mientras que

$$
x+(y+z)
=
[(a,b)]+[(c+e,d+f)]
=
[(a+(c+e),b+(d+f))].
$$

Las dos clases son iguales porque la suma natural es asociativa.

Para la conmutatividad,

$$
x+y=[(a+c,b+d)]=[(c+a,d+b)]=y+x.
$$

Para el neutro,

$$
x+0_{\mathbb Z}
=
[(a+0,b+0)]
=
[(a,b)]
=
x,
$$

y el otro lado se sigue de conmutatividad.

Finalmente,

$$
x+(-x)
=
[(a,b)]+[(b,a)]
=
[(a+b,b+a)].
$$

Por conmutatividad natural,

$$
a+b=b+a,
$$

de modo que el criterio de igualdad de clases enteras da

$$
[(a+b,b+a)]=[(0,0)]=0_{\mathbb Z}.
$$

La igualdad $(-x)+x=0_{\mathbb Z}$ se sigue de conmutatividad. ∎

Éste es el primer punto en que la construcción cumple la promesa que motivó al capítulo: todo entero posee un opuesto aditivo construido, no postulado.

### Definición 2.4.5 — Sustracción en $\mathbb Z$ {#ta-sustraccion-enteros}

*Glosario: [sustracción entera](../otros/tratado-de-analisis-glosario.md#gl-sustraccion-entera)*

Para $x,y\in\mathbb Z$ definimos

$$
\boxed{
x-y:=x+(-y).
}
$$

Ahora, y sólo ahora, el símbolo de sustracción queda disponible como operación total sobre $\mathbb Z$.

### Proposición 2.4.6 — Resolución universal de ecuaciones aditivas {#ta-resolucion-ecuaciones-aditivas-enteros}

Para cualesquiera $x,z\in\mathbb Z$ existe un único $y\in\mathbb Z$ tal que

$$
x+y=z.
$$

Ese entero es

$$
\boxed{
y=z-x.
}
$$

**Demostración.**  
Por definición,

$$
z-x=z+(-x).
$$

Entonces, usando asociatividad y conmutatividad,

$$
x+(z-x)
=
x+(z+(-x))
=
z+(x+(-x))
=
z+0_{\mathbb Z}
=
z.
$$

Existe, por tanto, una solución.

Si $x+y=z$, sumamos $-x$ a ambos lados:

$$
(-x)+(x+y)=(-x)+z.
$$

Por asociatividad,

$$
((-x)+x)+y=(-x)+z,
$$

y entonces

$$
y=(-x)+z=z+(-x)=z-x.
$$

La solución es única. ∎

La sustracción ha dejado de ser una operación parcial. Esto es exactamente lo que $\mathbb N$ no podía proporcionar.

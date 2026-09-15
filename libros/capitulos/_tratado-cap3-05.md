## 3.5. Incrustación canónica de $\mathbb Z$ {#sec-ta-3-5}

La construcción de $\mathbb Q$ no identifica automáticamente los enteros con racionales. Antes de utilizar expresiones como «el entero $a$ visto como racional», debemos construir una aplicación concreta de $\mathbb Z$ en $\mathbb Q$ y demostrar que conserva la aritmética ya establecida.

### Definición 3.5.1 — Incrustación entera en los racionales {#ta-incrustacion-entera-racionales}

*Glosario: [incrustación canónica](../otros/tratado-de-analisis-glosario.md#gl-incrustacion-canonica)*

Definimos

$$
\jmath_{\mathbb Z}^{\mathbb Q}:\mathbb Z\to\mathbb Q
$$

por

$$
\boxed{
\jmath_{\mathbb Z}^{\mathbb Q}(a)
:=
\frac{a}{1_{\mathbb Z}}.
}
$$

Abreviaremos $\jmath_{\mathbb Z}^{\mathbb Q}$ a $\jmath$ cuando el contexto determine los sistemas.

### Proposición 3.5.2 — La incrustación preserva la aritmética {#ta-incrustacion-entera-preserva-aritmetica}

La función $\jmath$ es inyectiva y, para $a,c\in\mathbb Z$,

$$
\jmath(0_{\mathbb Z})=0_{\mathbb Q},
\qquad
\jmath(1_{\mathbb Z})=1_{\mathbb Q},
$$

$$
\jmath(a+c)=\jmath(a)+\jmath(c),
$$

$$
\jmath(ac)=\jmath(a)\jmath(c),
$$

y

$$
\jmath(-a)=-\jmath(a).
$$

**Demostración.**  
Supongamos primero

$$
\jmath(a)=\jmath(c).
$$

Entonces

$$
\frac{a}{1_{\mathbb Z}}
=
\frac{c}{1_{\mathbb Z}}.
$$

Por el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales),

$$
a\,1_{\mathbb Z}=1_{\mathbb Z}\,c.
$$

Las leyes de la unidad multiplicativa en $\mathbb Z$ reducen esta igualdad a $a=c$. Por tanto $\jmath$ es inyectiva.

Las identidades para cero y uno son inmediatas de las definiciones:

$$
\jmath(0_{\mathbb Z})
=
\frac{0_{\mathbb Z}}{1_{\mathbb Z}}
=
0_{\mathbb Q},
$$

$$
\jmath(1_{\mathbb Z})
=
\frac{1_{\mathbb Z}}{1_{\mathbb Z}}
=
1_{\mathbb Q}.
$$

Para la suma, usando la [definición de suma racional](#ta-suma-racional),

$$
\begin{aligned}
\jmath(a)+\jmath(c)
&=
\frac a1+\frac c1\\
&=
\frac{a+c}{1}\\
&=
\jmath(a+c).
\end{aligned}
$$

Para el producto, por la [definición de multiplicación racional](#ta-multiplicacion-racional),

$$
\begin{aligned}
\jmath(a)\jmath(c)
&=
\frac a1\frac c1\\
&=
\frac{ac}{1}\\
&=
\jmath(ac).
\end{aligned}
$$

Finalmente, por la [definición del opuesto racional](#ta-opuesto-racional),

$$
-\jmath(a)
=
-\frac a1
=
\frac{-a}{1}
=
\jmath(-a).
$$

Así $\jmath$ conserva $0$, $1$, suma, producto y opuesto, además de ser inyectiva. ∎

### Observación 3.5.3 — No identificación conjuntista {#ta-no-identificacion-z-q}

No escribiremos todavía literalmente

$$
\mathbb Z\subseteq\mathbb Q.
$$

Los sistemas $\mathbb Z$ y $\mathbb Q$ han sido construidos como objetos distintos. La relación estructural canónica entre ambos es, por ahora, la aplicación inyectiva

$$
\boxed{
\jmath_{\mathbb Z}^{\mathbb Q}:\mathbb Z\hookrightarrow\mathbb Q.
}
$$

Cuando más adelante adoptemos identificaciones convencionales, lo haremos apoyándonos en esta incrustación y no en una igualdad conjuntista silenciosa.

---

::: {.callout-note title="Publicación progresiva"}
Con §3.5 los enteros quedan incorporados canónicamente en los racionales mediante una aplicación inyectiva que preserva $0$, $1$, suma, producto y opuesto. La siguiente entrega será **§3.6 — Inversos multiplicativos**, donde se construirá el recíproco de todo racional no nulo y finalmente se demostrará que $\mathbb Q$ es un cuerpo.
:::

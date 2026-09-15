## 3.6. Inversos multiplicativos {#sec-ta-3-6}

La multiplicación racional ya posee unidad, pero todavía falta la propiedad que distingue a un cuerpo de un anillo conmutativo: todo elemento no nulo debe admitir un inverso multiplicativo. Para construirlo rigurosamente necesitamos saber primero cuándo una clase fraccionaria es cero y comprobar después que invertir numerador y denominador no depende del representante elegido.

### Proposición 3.6.1 — Criterio de nulidad de una fracción {#ta-criterio-nulidad-fraccion}

Para $(a,b)\in D_{\mathbb Q}$,

$$
\boxed{
\frac ab=0_{\mathbb Q}
\iff
a=0_{\mathbb Z}.
}
$$

**Demostración.**  
Por el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales),

$$
\frac ab=\frac01
\iff
a\cdot1=b\cdot0.
$$

Las leyes de la unidad dan $a\cdot1=a$. Para el otro miembro, por distributividad,

$$
b\cdot0
=
b(0+0)
=
b0+b0,
$$

y la cancelación aditiva implica $b0=0$. Por tanto la igualdad cruzada equivale exactamente a $a=0$. ∎

### Definición 3.6.2 — Racionales no nulos {#ta-racionales-no-nulos}

*Glosario: [racionales no nulos](../otros/tratado-de-analisis-glosario.md#gl-racionales-no-nulos)*

Definimos

$$
\boxed{
\mathbb Q_{\neq0}
:=
\{q\in\mathbb Q:q\neq0_{\mathbb Q}\}.
}
$$

### Proposición 3.6.3 — Construcción del recíproco {#ta-construccion-reciproco}

Existe una única función

$$
\operatorname{inv}:\mathbb Q_{\neq0}\to\mathbb Q_{\neq0}
$$

tal que, para toda representación $q=a/b$ de un racional no nulo,

$$
\boxed{
\operatorname{inv}(q)=\frac ba.
}
$$

**Demostración.**  
Sea

$$
q=\frac ab\neq0_{\mathbb Q}.
$$

Por la Proposición 3.6.1, $a\neq0_{\mathbb Z}$, de modo que $(b,a)\in D_{\mathbb Q}$ y $b/a$ está definido. Además $b\neq0_{\mathbb Z}$, pues $(a,b)\in D_{\mathbb Q}$; por el mismo criterio de nulidad, el racional $b/a$ es no nulo.

Debemos comprobar que el valor no depende del representante. Si

$$
\frac ab=\frac cd,
$$

entonces, por el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales),

$$
ad=bc.
$$

Para las fracciones invertidas necesitamos

$$
bc=ad,
$$

que es la misma igualdad. Por tanto

$$
\frac ba=\frac dc.
$$

Podemos entonces definir el grafo

$$
G
=
\left\{
\langle q,r\rangle\in
\mathbb Q_{\neq0}\times\mathbb Q_{\neq0}:
\exists(a,b)\in D_{\mathbb Q}\;
\left(q=\frac ab\land r=\frac ba\right)
\right\}.
$$

Este conjunto existe por separación. Lo anterior demuestra que para cada $q\in\mathbb Q_{\neq0}$ existe un único $r\in\mathbb Q_{\neq0}$ con $\langle q,r\rangle\in G$. Por tanto $G$ es el grafo de la función requerida.

Obsérvese que no hemos elegido un representante de cada clase: la definición utiliza todos los representantes posibles y la buena definición demuestra que todos producen el mismo valor. ∎

### Notación 3.6.4 — Recíproco {#ta-reciproco-racional}

*Glosario: [recíproco racional](../otros/tratado-de-analisis-glosario.md#gl-reciproco-racional)*

Para $q\in\mathbb Q_{\neq0}$ escribiremos

$$
q^{-1}:=\operatorname{inv}(q).
$$

Así, si $a\neq0$ y $b\neq0$,

$$
\boxed{
\left(\frac ab\right)^{-1}
=
\frac ba.
}
$$

### Proposición 3.6.5 — Ley del inverso multiplicativo {#ta-ley-inverso-multiplicativo-racional}

Para todo $q\in\mathbb Q_{\neq0}$,

$$
\boxed{
qq^{-1}=1_{\mathbb Q}=q^{-1}q.
}
$$

**Demostración.**  
Escribamos $q=a/b$ con $a,b\neq0$. Entonces

$$
qq^{-1}
=
\frac ab\frac ba
=
\frac{ab}{ba}.
$$

Por conmutatividad de la multiplicación entera,

$$
\frac{ab}{ba}
=
\frac{1_{\mathbb Z}}{1_{\mathbb Z}}
=
1_{\mathbb Q},
$$

pues el [criterio de igualdad de racionales](#ta-criterio-igualdad-racionales) exige precisamente

$$
(ab)1=(ba)1.
$$

La igualdad $q^{-1}q=1_{\mathbb Q}$ se sigue de la conmutatividad del producto racional. ∎

### Definición 3.6.6 — División racional {#ta-division-racional}

*Glosario: [división racional](../otros/tratado-de-analisis-glosario.md#gl-division-racional)*

Para $x\in\mathbb Q$ y $y\in\mathbb Q_{\neq0}$ definimos

$$
\boxed{
\frac{x}{y}:=xy^{-1}.
}
$$

La barra de fracción tiene ahora dos usos compatibles. Cuando $a,b\in\mathbb Z$ y $b\neq0$, la notación de clase $a/b$ introducida en §3.2 coincide con la división entre los racionales canónicamente asociados a $a$ y $b$.

En efecto, por la [inyectividad de la incrustación canónica](#ta-incrustacion-entera-preserva-aritmetica),

$$
\jmath(b)\neq0_{\mathbb Q},
$$

y la construcción del recíproco da

$$
\jmath(b)^{-1}
=
\left(\frac b1\right)^{-1}
=
\frac1b.
$$

Por tanto

$$
\boxed{
\frac{\jmath(a)}{\jmath(b)}
=
\frac a1\cdot\frac1b
=
\frac ab.
}
$$

### Convención 3.6.7 — Terminología de cuerpo {#ta-convencion-cuerpo}

*Glosario: [cuerpo](../otros/tratado-de-analisis-glosario.md#gl-cuerpo)*

Llamaremos **cuerpo** a un anillo conmutativo $F$ con

$$
0_F\neq1_F
$$

tal que todo elemento no nulo de $F$ posee un inverso multiplicativo.

### Teorema 3.6.8 — $\mathbb Q$ es un cuerpo {#ta-q-es-cuerpo}

Con las operaciones construidas,

$$
\boxed{
(\mathbb Q,+,\cdot,0_{\mathbb Q},1_{\mathbb Q})
\text{ es un cuerpo}.
}
$$

**Demostración.**  
La [Proposición 3.3.8](#ta-grupo-aditivo-racional) establece que $(\mathbb Q,+,0_{\mathbb Q})$ es un grupo abeliano. La [Proposición 3.4.5](#ta-leyes-multiplicativas-distributivas-racionales) proporciona asociatividad y conmutatividad del producto, unidad y distributividad. La [Proposición 3.4.6](#ta-cero-uno-racionales-distintos) demuestra

$$
0_{\mathbb Q}\neq1_{\mathbb Q},
$$

y la Proposición 3.6.5 proporciona un inverso multiplicativo para todo racional no nulo. Son exactamente las condiciones de la Convención 3.6.7. ∎

### Corolario 3.6.9 — Ausencia de divisores de cero en $\mathbb Q$ {#ta-sin-divisores-cero-racionales}

Si

$$
xy=0_{\mathbb Q},
$$

entonces

$$
\boxed{
x=0_{\mathbb Q}
\quad\text{o}\quad
y=0_{\mathbb Q}.
}
$$

**Demostración.**  
Primero derivamos la absorción multiplicativa del cero a partir de las leyes ya probadas. Para todo $u\in\mathbb Q$,

$$
u0_{\mathbb Q}
=
u(0_{\mathbb Q}+0_{\mathbb Q})
=
u0_{\mathbb Q}+u0_{\mathbb Q}.
$$

Cancelando aditivamente $u0_{\mathbb Q}$ obtenemos

$$
u0_{\mathbb Q}=0_{\mathbb Q}.
$$

Si $x\neq0_{\mathbb Q}$, multiplicamos $xy=0_{\mathbb Q}$ por $x^{-1}$:

$$
y
=
1_{\mathbb Q}y
=
x^{-1}(xy)
=
x^{-1}0_{\mathbb Q}
=
0_{\mathbb Q}.
$$

Por tanto $x=0_{\mathbb Q}$ o $y=0_{\mathbb Q}$. ∎

---

::: {.callout-note title="Publicación progresiva"}
Con §3.6 la aritmética racional alcanza su estructura de cuerpo: todo racional no nulo posee recíproco, la división queda definida y $\mathbb Q$ carece de divisores de cero. La siguiente entrega será **§3.7 — Orden racional**, donde la comparación se construirá mediante representantes con denominador positivo.
:::

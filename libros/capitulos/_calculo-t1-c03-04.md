## Composición e identidad {#sec-t1-c03-04}

Hasta ahora hemos estudiado una función mirando lo que hace por sí sola. Pero gran parte del cálculo se construye encadenando operaciones: primero transformamos una entrada de una manera y luego aplicamos otra transformación al resultado.

Por ejemplo, para calcular

$$
(3x-1)^2
$$

podemos pensar en dos etapas:

$$
x\longmapsto 3x-1
\longmapsto
(3x-1)^2.
$$

La primera etapa produce un valor intermedio; la segunda toma precisamente ese valor como nueva entrada. La **composición de funciones** formaliza esta idea de encadenamiento.

Pero hay una cuestión que debemos resolver antes de escribir fórmulas: **¿puede la segunda función aceptar todas las salidas que realmente produce la primera?**

### Antes de componer, audita los tipos

Sean

$$
f\colon A\to B
$$

y

$$
g\colon D\to C.
$$

Queremos aplicar primero $f$ y después $g$. Si partimos de $x\in A$, la primera etapa produce

$$
f(x)\in B.
$$

Para que tenga sentido escribir $g(f(x))$, necesitamos además que ese valor $f(x)$ pertenezca al dominio $D$ de $g$.

Por tanto, la condición exacta es

$$
\boxed{f(A)\subseteq D.}
$$

Cuando se cumple, cada salida efectiva de $f$ es una entrada permitida para $g$.

El caso más frecuente se presenta como una cadena tipada

$$
A\xrightarrow{\ f\ }B\xrightarrow{\ g\ }C,
$$

es decir,

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

Aquí la compatibilidad es automática, porque $f(A)\subseteq B$ y $B$ es precisamente el dominio de $g$.

La condición general $f(A)\subseteq D$ es un poco más flexible: el codominio declarado de $f$ no tiene por qué coincidir literalmente con el dominio de $g$ si sabemos que **las salidas que $f$ toma de hecho** sí pertenecen a ese dominio.

::: {.callout-warning title="Error frecuente"}
No basta con que las fórmulas puedan escribirse una junto a la otra de manera informal.

Considera

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y

$$
g\colon(0,\infty)\to\mathbb R,
\qquad
 g(y)=\frac1y.
$$

Para $x\ne0$, la expresión $g(f(x))=1/x^2$ tiene sentido. Pero $f(0)=0$ y $0\notin(0,\infty)$, de modo que $g\circ f$ **no está definida como función sobre todo $\mathbb R$**.

La fórmula $1/x^2$ no corrige silenciosamente el problema de dominio. Habría que restringir la primera etapa a $\mathbb R\setminus\{0\}$ o modificar legítimamente los datos de las funciones.
:::

::: {#def-t1-0023}
**Composición e identidad.** Sean

$$
f\colon A\to B,
\qquad
g\colon D\to C,
$$

funciones tales que

$$
f(A)\subseteq D.
$$

La **composición de $g$ con $f$** es la función

$$
g\circ f\colon A\to C
$$

definida por

$$
(g\circ f)(x)=g(f(x))
\qquad(x\in A).
$$

Para cualquier conjunto $A$, la **función identidad sobre $A$** es

$$
\operatorname{id}_A\colon A\to A
$$

dada por

$$
\operatorname{id}_A(x)=x
\qquad(x\in A).
$$
:::

La notación

$$
g\circ f
$$

debe leerse de derecha a izquierda en el orden de aplicación:

$$
\boxed{
(g\circ f)(x)
=
g(f(x))
=
\text{primero $f$, después $g$}.
}
$$

El símbolo $\circ$ no significa multiplicación. Tampoco autoriza a intercambiar el orden de las funciones.

### Componer es construir una función nueva

Tomemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=3x-1,
$$

y

$$
g\colon\mathbb R\to[0,\infty),
\qquad
 g(y)=y^2.
$$

Entonces

$$
g\circ f\colon\mathbb R\to[0,\infty)
$$

y

$$
(g\circ f)(x)
=g(f(x))
=g(3x-1)
=(3x-1)^2.
$$

La expresión compuesta puede parecer una sola fórmula, pero estructuralmente conserva las dos etapas:

$$
\mathbb R
\xrightarrow{\ x\mapsto 3x-1\ }
\mathbb R
\xrightarrow{\ y\mapsto y^2\ }
[0,\infty).
$$

Esta perspectiva será importante muchas veces: una función complicada puede entenderse descomponiéndola en funciones más simples, y una función nueva puede construirse encadenando transformaciones conocidas.

### El orden importa: la composición no es conmutativa

El hecho de que $g\circ f$ exista no implica que $f\circ g$ exista. Para la segunda composición hay que realizar **otra** auditoría de dominios.

Y aun cuando ambas existan, no tienen por qué ser iguales.

::: {#exm-t1-0024}
**Dos composiciones existentes y distintas.** Sean

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x+1,
$$

y

$$
g\colon\mathbb R\to\mathbb R,
\qquad
 g(x)=x^2.
$$

Ambas composiciones están definidas sobre todo $\mathbb R$. Sin embargo,

$$
(g\circ f)(x)
=g(x+1)
=(x+1)^2,
$$

mientras que

$$
(f\circ g)(x)
=f(x^2)
=x^2+1.
$$

Por ejemplo, en $x=1$,

$$
(g\circ f)(1)=4,
\qquad
(f\circ g)(1)=2.
$$

Por tanto,

$$
\boxed{g\circ f\ne f\circ g.}
$$
:::

Este contraejemplo basta para descartar una supuesta ley de conmutatividad universal. La composición tiene otra propiedad, en cambio, que sí es universal cuando las funciones están tipadas de manera compatible: **la asociatividad**.

### Asociatividad: tres etapas, una sola cadena

Supongamos

$$
f\colon A\to B,
\qquad
g\colon B\to C,
\qquad
h\colon C\to D.
$$

Podemos componer primero $f$ con $g$ y después aplicar $h$:

$$
h\circ(g\circ f).
$$

O podemos componer primero $g$ con $h$ y después anteponer $f$:

$$
(h\circ g)\circ f.
$$

La intuición sugiere que ambas rutas ejecutan las mismas tres etapas

$$
x\longmapsto f(x)\longmapsto g(f(x))\longmapsto h(g(f(x))).
$$

Pero, según nuestra convención de igualdad de funciones, para demostrar que las dos composiciones son iguales no basta con observar que la fórmula final «parece la misma». Debemos comprobar primero que poseen el mismo dominio y codominio, y después que coinciden en cada punto.

::: {#prp-t1-0013}
**Asociatividad de la composición.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C,
\qquad
h\colon C\to D.
$$

Entonces

$$
\boxed{
h\circ(g\circ f)
=
(h\circ g)\circ f.
}
$$
:::

**Idea de la prueba.** Las dos funciones empiezan en $A$ y terminan en $D$. Por tanto, una vez auditados los tipos, basta comprobar que asignan la misma salida a cada $x\in A$.

**Demostración.** Como

$$
g\circ f\colon A\to C,
$$

la composición

$$
h\circ(g\circ f)\colon A\to D
$$

está bien definida. Del mismo modo,

$$
h\circ g\colon B\to D,
$$

por lo que

$$
(h\circ g)\circ f\colon A\to D
$$

también está bien definida.

Así, ambas funciones tienen dominio $A$ y codominio $D$.

Sea ahora $x\in A$. Entonces

$$
\begin{aligned}
\bigl(h\circ(g\circ f)\bigr)(x)
&=h\bigl((g\circ f)(x)\bigr)\\
&=h(g(f(x)))\\
&=(h\circ g)(f(x))\\
&=\bigl((h\circ g)\circ f\bigr)(x).
\end{aligned}
$$

Como las dos funciones tienen el mismo dominio, el mismo codominio y coinciden en cada $x\in A$, son iguales. $\square$

::: {.callout-note title="Después de la prueba"}
La asociatividad permite escribir sin ambigüedad

$$
h\circ g\circ f
$$

cuando los tipos son compatibles. Los paréntesis pueden omitirse porque cualquier agrupación admisible produce la misma función.

Pero **no** podemos alterar el orden:

$$
h\circ g\circ f
$$

significa aplicar primero $f$, después $g$ y finalmente $h$.
:::

### La identidad no transforma nada

La función identidad

$$
\operatorname{id}_A\colon A\to A,
\qquad
\operatorname{id}_A(x)=x,
$$

parece demasiado simple para merecer un nombre. Su función estructural, sin embargo, es importante: actúa como una operación neutra para la composición.

Si

$$
f\colon A\to B,
$$

entonces podemos componer $f$ por la derecha con $\operatorname{id}_A$ y por la izquierda con $\operatorname{id}_B$.

::: {#prp-t1-0014}
**Leyes de identidad.** Para toda función

$$
f\colon A\to B,
$$

se cumple

$$
\boxed{
\operatorname{id}_B\circ f=f
\qquad\text{y}\qquad
f\circ\operatorname{id}_A=f.
}
$$
:::

**Demostración.** Las composiciones están bien definidas porque $f(A)\subseteq B$ y $\operatorname{id}_A(A)=A$.

Además,

$$
\operatorname{id}_B\circ f\colon A\to B,
$$

igual que $f$. Para cada $x\in A$,

$$
(\operatorname{id}_B\circ f)(x)
=
\operatorname{id}_B(f(x))
=
f(x).
$$

Por la convención de igualdad de funciones,

$$
\operatorname{id}_B\circ f=f.
$$

Análogamente,

$$
f\circ\operatorname{id}_A\colon A\to B,
$$

y para cada $x\in A$,

$$
(f\circ\operatorname{id}_A)(x)
=f(\operatorname{id}_A(x))
=f(x).
$$

Por tanto,

$$
f\circ\operatorname{id}_A=f.
$$

$\square$

La posición de la identidad importa para que los tipos coincidan. A la izquierda de $f$ aparece la identidad del **codominio** $B$; a la derecha aparece la identidad del **dominio** $A$.

### Qué sucede con inyectividad y sobreyectividad al componer

La sección anterior separó dos arquitecturas de prueba:

- para inyectividad, partimos de una igualdad de salidas;
- para sobreyectividad, partimos de una salida arbitraria y construimos un antecedente.

La composición permite ver ambas arquitecturas en cadena.

::: {#prp-t1-0015}
**Preservación por composición.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C.
$$

Entonces:

1. si $f$ y $g$ son inyectivas, $g\circ f$ es inyectiva;
2. si $f$ y $g$ son sobreyectivas, $g\circ f$ es sobreyectiva;
3. si $f$ y $g$ son biyectivas, $g\circ f$ es biyectiva.
:::

**Idea de la prueba.** Para la inyectividad, una igualdad al final de la cadena debe retroceder primero a través de $g$ y después a través de $f$. Para la sobreyectividad, comenzamos en el codominio final y construimos antecedentes en sentido contrario al orden de aplicación: primero uno bajo $g$ y luego uno bajo $f$.

**Demostración.**

**1. Inyectividad.** Supongamos que $f$ y $g$ son inyectivas. Sean $x_1,x_2\in A$ y supongamos

$$
(g\circ f)(x_1)=(g\circ f)(x_2).
$$

Por definición de composición,

$$
g(f(x_1))=g(f(x_2)).
$$

Como $g$ es inyectiva,

$$
f(x_1)=f(x_2).
$$

Y como $f$ es inyectiva,

$$
x_1=x_2.
$$

Por tanto, $g\circ f$ es inyectiva.

**2. Sobreyectividad.** Supongamos que $f$ y $g$ son sobreyectivas. Sea $z\in C$ arbitrario.

Como $g$ es sobreyectiva, existe $y\in B$ tal que

$$
g(y)=z.
$$

Como $f$ es sobreyectiva, existe $x\in A$ tal que

$$
f(x)=y.
$$

Entonces

$$
(g\circ f)(x)
=g(f(x))
=g(y)
=z.
$$

Hemos encontrado, para un $z\in C$ arbitrario, un $x\in A$ cuya imagen por $g\circ f$ es $z$. Por tanto, $g\circ f$ es sobreyectiva.

**3. Biyectividad.** Si $f$ y $g$ son biyectivas, ambas son inyectivas y sobreyectivas. Por las partes 1 y 2, $g\circ f$ es inyectiva y sobreyectiva; por tanto, es biyectiva. $\square$

### Leer la composición como una cadena de dependencias

Hay una diferencia instructiva entre calcular y demostrar.

Para **evaluar**

$$
(g\circ f)(x),
$$

avanzamos en el orden natural de la cadena:

$$
x
\xrightarrow{f}
f(x)
\xrightarrow{g}
g(f(x)).
$$

Para demostrar **sobreyectividad**, en cambio, la construcción de testigos recorre la cadena hacia atrás:

$$
z\in C
\xleftarrow{g}
y\in B
\xleftarrow{f}
x\in A.
$$

Y para demostrar **inyectividad**, una igualdad de salidas también retrocede:

$$
g(f(x_1))=g(f(x_2))
\Longrightarrow
f(x_1)=f(x_2)
\Longrightarrow
x_1=x_2.
$$

Esta doble lectura —hacia delante para evaluar, hacia atrás para recuperar información— prepara una pregunta inevitable. Si una función es biyectiva, cada salida corresponde a exactamente una entrada. ¿Podemos convertir sistemáticamente esa correspondencia en una nueva función que deshaga la original?

Esa será la cuestión de §3.5. Por ahora, el mapa conceptual queda ampliado a

$$
\boxed{
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{clasificación}
\to
\text{composición e identidad}.
}
$$

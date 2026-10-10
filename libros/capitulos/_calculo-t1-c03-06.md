## El álgebra de imágenes y preimágenes {#sec-t1-c03-06}

En §3.2 aprendimos a calcular imágenes y preimágenes de conjuntos concretos. Ahora cambia la pregunta. Ya no queremos saber solamente **qué conjunto resulta**, sino **cómo interactúan estas operaciones con las operaciones de conjuntos** construidas en `T1-C01`.

Sea

$$
f\colon A\to B.
$$

Si $E,F\subseteq A$ y $S,T\subseteq B$, podemos preguntar, por ejemplo, si es legítimo escribir

$$
f(E\cup F)=f(E)\cup f(F),
$$

$$
f(E\cap F)=f(E)\cap f(F),
$$

o

$$
f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T).
$$

Las tres fórmulas parecen naturales. Dos de ellas son siempre correctas. La restante puede fallar.

Lo importante de esta sección no será memorizar una tabla de identidades. Queremos aprender algo más útil: **cómo auditar una igualdad de conjuntos hasta descubrir exactamente qué hipótesis le falta**.

### Una primera ley: la inclusión se conserva hacia delante y hacia atrás

Empecemos por una propiedad que no presenta ninguna sorpresa.

Si

$$
E\subseteq F\subseteq A,
$$

entonces todo elemento de $E$ pertenece también a $F$. Por tanto, cualquier valor obtenido usando una entrada de $E$ también se obtiene usando una entrada de $F$:

$$
\boxed{E\subseteq F\Longrightarrow f(E)\subseteq f(F).}
$$

Del mismo modo, si

$$
S\subseteq T\subseteq B,
$$

y $x\in f^{-1}(S)$, entonces $f(x)\in S\subseteq T$, de modo que $x\in f^{-1}(T)$. Por tanto,

$$
\boxed{S\subseteq T\Longrightarrow f^{-1}(S)\subseteq f^{-1}(T).}
$$

Tanto la imagen como la preimagen son, pues, **monótonas respecto de la inclusión de conjuntos**. Aquí la palabra «monótona» se refiere solamente al orden dado por $\subseteq$ entre subconjuntos; no estamos introduciendo todavía la monotonía de funciones reales que estudiaremos en §3.9.

### Una igualdad muy plausible

Probemos ahora algo menos automático. Supongamos que $E,F\subseteq A$. Es tentador afirmar

$$
\boxed{f(E\cap F)=f(E)\cap f(F).}
$$

La igualdad parece razonable: si una entrada pertenece a ambos conjuntos, su imagen pertenece a ambas imágenes. Pero una igualdad de conjuntos exige **dos inclusiones**. Auditémoslas por separado.

#### Primera inclusión

Queremos demostrar

$$
f(E\cap F)\subseteq f(E)\cap f(F).
$$

Sea

$$
y\in f(E\cap F).
$$

Por definición de imagen, existe $x\in E\cap F$ tal que

$$
f(x)=y.
$$

Como $x\in E\cap F$, tenemos simultáneamente

$$
x\in E
\qquad\text{y}\qquad
x\in F.
$$

Por tanto,

$$
y=f(x)\in f(E)
$$

y también

$$
y=f(x)\in f(F).
$$

Así,

$$
y\in f(E)\cap f(F).
$$

Hemos demostrado, sin ninguna hipótesis adicional sobre $f$, que

$$
\boxed{f(E\cap F)\subseteq f(E)\cap f(F).}
$$

Hasta aquí la conjetura sigue viva.

#### Intentemos ahora la inclusión inversa

Queremos probar

$$
f(E)\cap f(F)\subseteq f(E\cap F).
$$

Sea

$$
y\in f(E)\cap f(F).
$$

Entonces

$$
y\in f(E)
\qquad\text{y}\qquad
y\in f(F).
$$

La primera pertenencia nos da **algún** $u\in E$ tal que

$$
f(u)=y.
$$

La segunda nos da **algún** $v\in F$ tal que

$$
f(v)=y.
$$

Por tanto,

$$
f(u)=f(v).
$$

Y aquí la demostración se atasca.

Para concluir que $y\in f(E\cap F)$ necesitaríamos encontrar **una sola entrada** que perteneciera simultáneamente a $E$ y a $F$. Pero lo único que hemos obtenido son dos posibles testigos:

$$
u\in E,
\qquad
v\in F,
\qquad
f(u)=f(v).
$$

Nada de lo demostrado hasta ahora permite afirmar que

$$
u=v.
$$

::: {.callout-note title="La prueba fallida ha descubierto una hipótesis"}
El punto donde la demostración se detiene no es ruido algebraico. Es información matemática precisa.

Necesitamos convertir

$$
f(u)=f(v)
$$

en

$$
u=v.
$$

Pero esa es exactamente la definición de **inyectividad**.

La prueba fallida nos ha dicho qué hipótesis faltaba.
:::

Si $f$ es inyectiva, entonces de $f(u)=f(v)$ obtenemos $u=v$. Llamemos $x$ a ese elemento común. Como

$$
x=u\in E
$$

y

$$
x=v\in F,
$$

tenemos

$$
x\in E\cap F.
$$

Además,

$$
f(x)=y.
$$

Por tanto,

$$
y\in f(E\cap F).
$$

Así, bajo inyectividad, la inclusión inversa sí queda demostrada.

Antes de formular el resultado correcto, debemos comprobar que la hipótesis añadida es realmente necesaria y no solo un artefacto de nuestra estrategia de prueba.

::: {#exm-t1-0026}
**La imagen no conserva siempre las intersecciones.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

y consideremos

$$
E=\{-1\},
\qquad
F=\{1\}.
$$

Como

$$
E\cap F=\varnothing,
$$

tenemos

$$
f(E\cap F)=f(\varnothing)=\varnothing.
$$

Sin embargo,

$$
f(E)=\{1\}
$$

y

$$
f(F)=\{1\}.
$$

Por tanto,

$$
f(E)\cap f(F)=\{1\}.
$$

En consecuencia,

$$
\boxed{
f(E\cap F)
=\varnothing
\subsetneq
\{1\}
=f(E)\cap f(F).
}
$$

El mecanismo del fallo es exactamente el diagnosticado en la prueba: los dos testigos son distintos,

$$
-1\ne1,
$$

pero tienen la misma imagen,

$$
f(-1)=f(1)=1.
$$
:::

Ya podemos registrar la versión correcta de las leyes básicas de imagen.

::: {#prp-t1-0017}
**Leyes básicas de la imagen.** Sea $f\colon A\to B$ y sean $E,F\subseteq A$.

1. Si $E\subseteq F$, entonces
   $$
   f(E)\subseteq f(F).
   $$
2. La imagen conserva uniones:
   $$
   f(E\cup F)=f(E)\cup f(F).
   $$
3. Para intersecciones siempre se tiene
   $$
   f(E\cap F)\subseteq f(E)\cap f(F).
   $$
4. Si además $f$ es inyectiva, entonces
   $$
   f(E\cap F)=f(E)\cap f(F).
   $$
:::

Ya hemos demostrado los apartados 1, 3 y 4. Probemos el apartado 2 para completar la proposición.

**Idea de la prueba de la unión.** Pertenecer a $E\cup F$ significa pertenecer a $E$ **o** a $F$. Esa disyunción pasa sin pérdida a las imágenes porque un mismo testigo $x$ basta para justificar una de las dos alternativas.

**Demostración.** Sea $y\in f(E\cup F)$. Entonces existe $x\in E\cup F$ tal que $f(x)=y$. Como $x\in E$ o $x\in F$, tenemos $y\in f(E)$ o $y\in f(F)$. Por tanto,

$$
y\in f(E)\cup f(F).
$$

Esto demuestra

$$
f(E\cup F)\subseteq f(E)\cup f(F).
$$

Para la inclusión inversa, sea $y\in f(E)\cup f(F)$. Entonces $y\in f(E)$ o $y\in f(F)$. En el primer caso existe $x\in E$ con $f(x)=y$; como $E\subseteq E\cup F$, ese mismo $x$ pertenece a $E\cup F$, y por tanto $y\in f(E\cup F)$. El segundo caso es análogo.

Luego

$$
f(E)\cup f(F)\subseteq f(E\cup F).
$$

y, por doble inclusión,

$$
\boxed{f(E\cup F)=f(E)\cup f(F).}
$$

$\square$

### Qué cambió lógicamente entre unión e intersección

Vale la pena detenerse aquí porque la diferencia es más profunda que una colección de símbolos.

Para la unión,

$$
y\in f(E\cup F)
$$

significa que existe un $x$ tal que

$$
x\in E\cup F
\qquad\text{y}\qquad
f(x)=y.
$$

La condición $x\in E\cup F$ se descompone como

$$
x\in E\quad\text{o}\quad x\in F.
$$

No aparecen dos testigos diferentes.

En cambio,

$$
y\in f(E)\cap f(F)
$$

significa simultáneamente

$$
\exists u\in E\quad f(u)=y
$$

y

$$
\exists v\in F\quad f(v)=y.
$$

Los cuantificadores existenciales pueden producir testigos distintos. Para fusionarlos necesitamos saber que una misma salida no puede proceder de dos entradas diferentes. Esa es exactamente la función estructural de la inyectividad.

Podemos condensarlo así:

$$
\boxed{
\begin{array}{c}
\text{la unión no obliga a identificar testigos;}\\[4pt]
\text{la intersección de imágenes puede exigir identificar dos testigos.}
\end{array}
}
$$

### Las preimágenes se comportan mejor

Pasemos ahora al sentido contrario. Sea $S\subseteq B$. Recordemos la equivalencia elemental

$$
x\in f^{-1}(S)
\iff
f(x)\in S.
$$

Aquí no necesitamos buscar un antecedente: **el punto $x$ ya está fijado**. Solo comprobamos si su imagen satisface una condición de pertenencia.

Esta diferencia hace que las operaciones de conjuntos se transporten con mucha más fidelidad mediante preimágenes.

::: {#prp-t1-0016}
**Leyes de preimagen.** Sea $f\colon A\to B$ y sean $S,T\subseteq B$.

1. Si $S\subseteq T$, entonces
   $$
   f^{-1}(S)\subseteq f^{-1}(T).
   $$
2. La preimagen conserva uniones:
   $$
   f^{-1}(S\cup T)
   =
   f^{-1}(S)\cup f^{-1}(T).
   $$
3. La preimagen conserva intersecciones:
   $$
   f^{-1}(S\cap T)
   =
   f^{-1}(S)\cap f^{-1}(T).
   $$
4. La preimagen conserva diferencias:
   $$
   f^{-1}(S\setminus T)
   =
   f^{-1}(S)\setminus f^{-1}(T).
   $$
5. En particular, para el complemento relativo al codominio,
   $$
   f^{-1}(B\setminus S)
   =
   A\setminus f^{-1}(S).
   $$
6. Si $g\colon B\to C$ y $R\subseteq C$, entonces
   $$
   (g\circ f)^{-1}(R)
   =
   f^{-1}\bigl(g^{-1}(R)\bigr).
   $$
:::

El apartado 1 ya fue demostrado al comienzo de la sección. Los demás pueden probarse de manera muy uniforme siguiendo la pertenencia de un punto arbitrario.

**Demostración de la unión.** Sea $x\in A$. Entonces

$$
\begin{aligned}
x\in f^{-1}(S\cup T)
&\iff f(x)\in S\cup T\\
&\iff \bigl(f(x)\in S\text{ o }f(x)\in T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ o }x\in f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\cup f^{-1}(T).
\end{aligned}
$$

Como la equivalencia vale para todo $x\in A$,

$$
f^{-1}(S\cup T)
=
f^{-1}(S)\cup f^{-1}(T).
$$

**Demostración de la intersección.** Del mismo modo,

$$
\begin{aligned}
x\in f^{-1}(S\cap T)
&\iff f(x)\in S\cap T\\
&\iff \bigl(f(x)\in S\text{ y }f(x)\in T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ y }x\in f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\cap f^{-1}(T).
\end{aligned}
$$

Por tanto,

$$
f^{-1}(S\cap T)
=
f^{-1}(S)\cap f^{-1}(T).
$$

Observa la diferencia con las imágenes: aquí el mismo $x$ aparece durante toda la cadena. No surge ningún problema de «dos antecedentes posiblemente distintos».

**Demostración de la diferencia.** Para $x\in A$,

$$
\begin{aligned}
x\in f^{-1}(S\setminus T)
&\iff f(x)\in S\setminus T\\
&\iff \bigl(f(x)\in S\text{ y }f(x)\notin T\bigr)\\
&\iff \bigl(x\in f^{-1}(S)\text{ y }x\notin f^{-1}(T)\bigr)\\
&\iff x\in f^{-1}(S)\setminus f^{-1}(T).
\end{aligned}
$$

Luego

$$
f^{-1}(S\setminus T)
=
f^{-1}(S)\setminus f^{-1}(T).
$$

Tomando $S=B$ y recordando que $f^{-1}(B)=A$, obtenemos inmediatamente

$$
\boxed{
f^{-1}(B\setminus T)
=
A\setminus f^{-1}(T).
}
$$

**Demostración de la composición de preimágenes.** Sean

$$
f\colon A\to B,
\qquad
g\colon B\to C,
$$

y sea $R\subseteq C$. Para $x\in A$,

$$
\begin{aligned}
x\in(g\circ f)^{-1}(R)
&\iff (g\circ f)(x)\in R\\
&\iff g(f(x))\in R\\
&\iff f(x)\in g^{-1}(R)\\
&\iff x\in f^{-1}\bigl(g^{-1}(R)\bigr).
\end{aligned}
$$

Por tanto,

$$
\boxed{
(g\circ f)^{-1}(R)
=
f^{-1}\bigl(g^{-1}(R)\bigr).
}
$$

$\square$

::: {.callout-note title="Lectura estructural"}
La fórmula anterior tiene el mismo orden inverso que apareció en §3.5:

$$
A\xrightarrow{f}B\xrightarrow{g}C.
$$

Para decidir qué puntos de $A$ terminan dentro de $R\subseteq C$, primero preguntamos qué puntos de $B$ caen en $R$ bajo $g$ y luego qué puntos de $A$ caen en ese conjunto bajo $f$:

$$
R
\xmapsto{\,g^{-1}\,}
g^{-1}(R)
\xmapsto{\,f^{-1}\,}
f^{-1}(g^{-1}(R)).
$$

Aquí los símbolos $g^{-1}$ y $f^{-1}$ designan **preimágenes de conjuntos**; no se supone que $f$ ni $g$ sean biyectivas.
:::

### Por qué la preimagen conserva mejor el álgebra de conjuntos

Podemos explicar todas estas identidades sin volver a demostrarlas una por una.

La afirmación

$$
x\in f^{-1}(S)
$$

es simplemente otra manera de escribir

$$
f(x)\in S.
$$

Por eso, cuando combinamos conjuntos mediante unión, intersección o complemento, las operaciones lógicas correspondientes pasan directamente a través de la preimagen:

$$
\begin{array}{ccl}
\cup &\longleftrightarrow& \text{«o»},\\[4pt]
\cap &\longleftrightarrow& \text{«y»},\\[4pt]
\text{complemento} &\longleftrightarrow& \text{«no»}.
\end{array}
$$

La preimagen no tiene que elegir ni comparar antecedentes. Evalúa siempre el mismo punto $x$ y pregunta dónde cae $f(x)$.

La imagen directa tiene una estructura lógica distinta. Para afirmar

$$
y\in f(E),
$$

necesitamos un testigo:

$$
\exists x\in E\quad f(x)=y.
$$

En una intersección de imágenes pueden aparecer dos testigos distintos para una misma salida. Precisamente ahí puede perderse la igualdad.

La diferencia conceptual puede resumirse así:

$$
\boxed{
\begin{array}{c}
\text{preimagen: sustituir }f(x)\text{ en una condición de pertenencia;}\\[4pt]
\text{imagen: afirmar la existencia de algún antecedente que produzca la salida.}
\end{array}
}
$$

### Un mapa de las leyes obtenidas

Para $f\colon A\to B$, $E,F\subseteq A$ y $S,T\subseteq B$:

$$
\boxed{
\begin{array}{rcl}
f(E\cup F) &=& f(E)\cup f(F),\\[4pt]
f(E\cap F) &\subseteq& f(E)\cap f(F),\\[4pt]
f(E\cap F) &=& f(E)\cap f(F)\quad\text{si $f$ es inyectiva},\\[8pt]
f^{-1}(S\cup T) &=& f^{-1}(S)\cup f^{-1}(T),\\[4pt]
f^{-1}(S\cap T) &=& f^{-1}(S)\cap f^{-1}(T),\\[4pt]
f^{-1}(S\setminus T) &=& f^{-1}(S)\setminus f^{-1}(T),\\[4pt]
f^{-1}(B\setminus S) &=& A\setminus f^{-1}(S).
\end{array}
}
$$

No hay que memorizar este cuadro como una colección arbitraria. La asimetría procede de los cuantificadores: **la imagen introduce existencia de antecedentes; la preimagen no**.

Y, sobre todo, la sección nos deja una técnica reutilizable de investigación matemática:

$$
\boxed{
\text{conjetura}
\to
\text{doble inclusión}
\to
\text{prueba que se atasca}
\to
\text{diagnóstico del paso faltante}
\to
\text{hipótesis correcta}
\to
\text{contraejemplo sin ella}.
}
$$

En §3.7 cambiaremos de representación: estudiaremos la **gráfica** de una función como subconjunto del producto cartesiano. Allí veremos qué información estructural puede leerse de un dibujo y, con igual importancia, qué información no está contenida en la curva por sí sola.

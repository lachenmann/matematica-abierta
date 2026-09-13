(c) “Existe un estudiante tal que, para cada problema, o bien ese estudiante no lo resolvió, o bien algún otro estudiante también lo resolvió.” Es decir, existe un estudiante que no posee ningún problema resuelto exclusivamente por él.

(d) Mover $\exists p$ delante de $\forall e$ obliga a escoger un mismo problema para todos los estudiantes. La frase original permite que el problema dependa del estudiante.

**Solución 79.**

(a) En $\forall x\,[P(x,y)\Rightarrow\exists y\,Q(x,y,z)]$, $x$ está ligada por $\forall$. La $y$ de $P(x,y)$ es libre; la $y$ de $Q(x,y,z)$ está ligada por $\exists$; $z$ es libre.

(b) Una renominación segura es

$$
\forall x\,[P(x,y)\Rightarrow\exists t\,Q(x,t,z)].
$$

(c) Si se reemplaza ingenuamente $\forall x$ por $\forall y$, la $y$ libre que aparece en $P(x,y)$ quedaría bajo el alcance del nuevo cuantificador. Esa captura cambia el significado.

(d) Una clausura universal es

$$
\forall y\;\forall z\;\forall x\;
[P(x,y)\Rightarrow\exists t\,Q(x,t,z)].
$$

(e)

$$
\begin{aligned}
&\neg\forall y\forall z\forall x\,[P(x,y)\Rightarrow\exists t\,Q(x,t,z)]\\
&\equiv
\exists y\exists z\exists x\,[P(x,y)\land\neg\exists t\,Q(x,t,z)]\\
&\equiv
\exists y\exists z\exists x\,[P(x,y)\land\forall t\,\neg Q(x,t,z)].
\end{aligned}
$$

**Solución 80.**

(a) Afirma que para todo real $x$ existe un único real $y$ que es estrictamente mayor que $x$ y que es menor o igual que cualquier otro real estrictamente mayor que $x$. Es decir, afirma que todo real tiene un menor real estrictamente mayor que él.

(b) Es falsa.

(c) Fijemos $x$ y supongamos $y>x$. Toma

$$
z=\frac{x+y}{2}.
$$

Entonces $x<z<y$. Como $z>x$, la condición universal exigiría $y\le z$, contradicción.

(d) Falla ya la existencia: para ningún $x$ existe un $y$ con la propiedad. Por tanto la unicidad ni siquiera llega a entrar en juego.

(e) Una negación exacta es: “Existe un real $x$ para el cual no existe exactamente un real $y$ que sea el menor real estrictamente mayor que $x$”. De hecho hemos probado algo más fuerte: para todo $x$ no existe ninguno.

***

## Autoevaluación de salida

Antes de continuar a C7, deberías poder responder afirmativamente:

- ¿distingo una expresión de un predicado y de una proposición?
- ¿puedo declarar el dominio relevante?
- ¿identifico variables libres y ligadas?
- ¿leo $\forall$, $\exists$ y $\exists!$ sin perder su alcance?
- ¿sé que un contraejemplo refuta un universal?
- ¿sé que un testigo establece una existencia?
- ¿puedo negar cuantificadores cambiando $\forall\leftrightarrow\exists$ y negando el contenido interno?
- ¿distingo $\forall x\exists y$ de $\exists y\forall x$?
- ¿puedo explicar cuándo un testigo depende de una variable previa?
- ¿puedo traducir afirmaciones de complejidad media en ambos sentidos?

Si alguna respuesta es negativa, vuelve primero a las secciones 6.7, 6.9–6.11 y a los ejercicios de los bloques E, G, H y L. Son los puntos de mayor transferencia del capítulo.

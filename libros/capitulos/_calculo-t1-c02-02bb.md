#### Despejar una incógnita es un teorema de existencia y unicidad

Ahora podemos formular rigurosamente dos operaciones que hacemos constantemente.

::: {#thm-t1-0011}
**Ecuaciones elementales en un cuerpo.** Sean $a,b\in F$.

1. La ecuación
   $$
   a+x=b
   $$
   tiene una única solución, dada por
   $$
   x=b+(-a).
   $$
2. Si $a\ne0$, la ecuación
   $$
   ax=b
   $$
   tiene una única solución, dada por
   $$
   x=a^{-1}b.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Cada parte exige los dos trabajos que aprendimos en §1.8:

- **existencia:** exhibir un candidato y comprobar que satisface la ecuación;
- **unicidad:** demostrar que cualquier otra solución debe coincidir con ese candidato.

La fórmula obtenida al «despejar» no sustituye esos dos trabajos: es su conclusión.
:::

**Demostración.**

Para la primera ecuación proponemos

$$
x=b+(-a).
$$

Entonces

$$
\begin{aligned}
a+x
&=a+\bigl(b+(-a)\bigr)\\
&=(a+(-a))+b\\
&=0+b\\
&=b,
\end{aligned}
$$

donde hemos usado asociatividad y conmutatividad para reagrupar. Así, la solución existe.

Supongamos ahora que $y$ es cualquier otra solución. Entonces

$$
a+y=b=a+x.
$$

Por cancelación aditiva,

$$
y=x.
$$

La solución es única.

Para la segunda ecuación supongamos $a\ne0$ y propongamos

$$
x=a^{-1}b.
$$

Entonces

$$
\begin{aligned}
ax
&=a(a^{-1}b)\\
&=(aa^{-1})b\\
&=1b\\
&=b.
\end{aligned}
$$

Por tanto, existe una solución.

Si $y$ es otra solución, entonces

$$
ay=b=ax.
$$

Como $a\ne0$, la cancelación multiplicativa de @prp-t1-0027 da

$$
y=x.
$$

Así, la solución también es única. $\blacksquare$

::: {.callout-note title="Qué significa ahora «hacer la misma operación a ambos lados»"}
Cuando resolvemos

$$
a+x=b
$$

«restando $a$», en realidad estamos sumando el inverso aditivo $-a$ a ambos miembros y usando asociatividad, neutro e inverso.

Cuando resolvemos

$$
ax=b,
\qquad a\ne0,
$$

«dividiendo por $a$», en realidad estamos multiplicando por el inverso $a^{-1}$.

Las reglas escolares son versiones comprimidas de argumentos estructurales.
:::

#### Resta y división: operaciones derivadas

Ya podemos introducir las dos notaciones que hasta ahora parecían operaciones independientes.

::: {#def-t1-0032}
**Resta y división.** Sean $a,b\in F$.

La **diferencia** de $a$ y $b$ se define por

$$
a-b:=a+(-b).
$$

Si $b\ne0$, el **cociente** de $a$ por $b$ se define por

$$
\frac ab:=ab^{-1}.
$$
:::

::: {.callout-note title="Desarrollo optativo: la resta como operación inversa de la suma"}
La definición anterior también puede obtenerse a partir de la idea elemental de que **restar $b$ debe deshacer la suma de $b$**.

En vez de definir de entrada $a-b$, caractericemos provisionalmente la diferencia como el único elemento $x\in F$ que satisface

$$
b+x=a.
$$

Sumamos $-b$ a ambos miembros:

$$
(-b)+(b+x)=(-b)+a.
$$

Por asociatividad,

$$
\bigl((-b)+b\bigr)+x=(-b)+a.
$$

Como $(-b)+b=0$, obtenemos

$$
0+x=(-b)+a,
$$

y, por el neutro aditivo y la conmutatividad,

$$
x=(-b)+a=a+(-b).
$$

Por tanto, la operación caracterizada como «deshacer la suma de $b$» coincide necesariamente con sumar su inverso aditivo:

$$
\boxed{a-b=a+(-b).}
$$

En nuestro desarrollo esta igualdad es, desde ahora, **definicional**; el argumento muestra por qué esa definición captura exactamente la operación inversa de sumar $b$.
:::

::: {.callout-note title="Desarrollo optativo: la división como operación inversa del producto"}
El mismo razonamiento funciona multiplicativamente, con una diferencia esencial: debemos exigir $b\ne0$ para que exista $b^{-1}$.

En vez de definir de entrada $a/b$, caractericemos provisionalmente el cociente como el único elemento $x\in F$ que satisface

$$
bx=a.
$$

Multiplicamos ambos miembros por $b^{-1}$:

$$
b^{-1}(bx)=b^{-1}a.
$$

Por asociatividad,

$$
(b^{-1}b)x=b^{-1}a.
$$

Como $b^{-1}b=1$, obtenemos

$$
1x=b^{-1}a,
$$

y, por el neutro multiplicativo y la conmutatividad,

$$
x=b^{-1}a=ab^{-1}.
$$

Por tanto, la operación caracterizada como «deshacer la multiplicación por $b$» coincide necesariamente con multiplicar por su inverso:

$$
\boxed{\frac ab=ab^{-1}},
\qquad b\ne0.
$$

Así como la resta no introduce una nueva operación primitiva, la división tampoco: ambas se construyen a partir de las operaciones del cuerpo y de sus respectivos inversos.
:::

La resta, por tanto, no es una tercera operación primitiva: es suma con un inverso aditivo.

Del mismo modo, la división no es una cuarta operación primitiva: es multiplicación por un inverso multiplicativo.

Esta última definición explica inmediatamente una restricción que debe acompañarnos siempre:

$$
\boxed{\text{no se divide por }0.}
$$

La razón no es una convención tipográfica. El número $0$ no posee inverso multiplicativo. En efecto, si existiera $c$ tal que

$$
0c=1,
$$

@exm-t1-0040 daría $0c=0$, y obtendríamos

$$
0=1,
$$

contradiciendo la definición de cuerpo.

De la definición de resta y @prp-t1-0026 se obtienen, por ejemplo,

$$
a-(-b)=a+b
$$

y

$$
a-b=0
\iff
a=b.
$$

La segunda equivalencia también puede leerse mediante @thm-t1-0011: la ecuación

$$
a+(-b)=0
$$

determina de manera única la relación entre $a$ y $b$.

#### Las reglas de fracciones también se demuestran

La notación fraccionaria concentra varias aplicaciones de los axiomas. Conviene establecer una vez las reglas esenciales y dejar de tratarlas como recetas sin fundamento.

::: {#prp-t1-0028}
**Reglas básicas de cocientes.** Sean $a,b,c,d\in F$.

1. Para todo $a$,
   $$
   \frac a1=a.
   $$
   Si $a\ne0$, entonces
   $$
   \frac1a=a^{-1},
   \qquad
   \frac aa=1.
   $$
2. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab=\frac cd
   \iff
   ad=bc.
   $$
3. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab\frac cd
   =
   \frac{ac}{bd}.
   $$
4. Si $b\ne0$ y $d\ne0$, entonces
   $$
   \frac ab+\frac cd
   =
   \frac{ad+bc}{bd},
   $$
   y
   $$
   \frac ab-\frac cd
   =
   \frac{ad-bc}{bd}.
   $$
:::

**Demostración.**

Como $1$ es su propio inverso multiplicativo,

$$
1^{-1}=1,
$$

y por tanto

$$
\frac a1=a1^{-1}=a.
$$

Si $a\ne0$, las otras dos identidades iniciales son simplemente

$$
\frac1a=1a^{-1}=a^{-1}
$$

y

$$
\frac aa=aa^{-1}=1.
$$

Para la igualdad de fracciones, supongamos $b,d\ne0$. Si

$$
\frac ab=\frac cd,
$$

entonces, por definición de cociente,

$$
ab^{-1}=cd^{-1}.
$$

Por sustitución de iguales por iguales podemos multiplicar ambos miembros por el mismo elemento $bd$:

$$
(ab^{-1})(bd)=(cd^{-1})(bd).
$$

Ahora reducimos cada miembro por separado. En el izquierdo,

$$
\begin{aligned}
(ab^{-1})(bd)
&=ab^{-1}bd\\
&=a(b^{-1}b)d\\
&=a1d\\
&=ad.
\end{aligned}
$$

En el derecho,

$$
\begin{aligned}
(cd^{-1})(bd)
&=cd^{-1}bd\\
&=cb(d^{-1}d)\\
&=cb\\
&=bc.
\end{aligned}
$$

Aquí hemos usado asociatividad y conmutatividad del producto, las identidades $b^{-1}b=1$ y $d^{-1}d=1$, y el neutro multiplicativo. Por tanto,

$$
ad=bc.
$$

Recíprocamente, supongamos

$$
ad=bc.
$$

Como $b,d\ne0$, existen $b^{-1}$ y $d^{-1}$. De nuevo por sustitución de iguales por iguales, multiplicamos ambos miembros por $b^{-1}d^{-1}$:

$$
(ad)(b^{-1}d^{-1})=(bc)(b^{-1}d^{-1}).
$$

En el miembro izquierdo,

$$
\begin{aligned}
(ad)(b^{-1}d^{-1})
&=adb^{-1}d^{-1}\\
&=ab^{-1}(dd^{-1})\\
&=ab^{-1}.
\end{aligned}
$$

En el derecho,

$$
\begin{aligned}
(bc)(b^{-1}d^{-1})
&=bcb^{-1}d^{-1}\\
&=c(bb^{-1})d^{-1}\\
&=cd^{-1}.
\end{aligned}
$$

Así,

$$
ab^{-1}=cd^{-1},
$$

y, por definición de cociente,

$$
\frac ab=\frac cd.
$$

Para el producto usamos @prp-t1-0026:

$$
\begin{aligned}
\frac ab\frac cd
&=(ab^{-1})(cd^{-1})\\
&=ac(b^{-1}d^{-1})\\
&=ac(bd)^{-1}\\
&=\frac{ac}{bd}.
\end{aligned}
$$

Finalmente,

$$
\frac{ad}{bd}
=
ad(bd)^{-1}
=
ad\,b^{-1}d^{-1}
=
ab^{-1}
=
\frac ab,
$$

y análogamente

$$
\frac{bc}{bd}
=
\frac cd.
$$

Por distributividad,

$$
\frac ab+\frac cd
=
\frac{ad}{bd}+\frac{bc}{bd}
=
(ad+bc)(bd)^{-1}
=
\frac{ad+bc}{bd}.
$$

La fórmula para la resta se obtiene sustituyendo $c$ por $-c$ y usando las reglas de signos ya demostradas. $\blacksquare$

::: {.callout-note title="Qué es realmente la multiplicación cruzada"}
La equivalencia

$$
\frac ab=\frac cd
\iff
ad=bc
\qquad
(b,d\ne0)
$$

no introduce una nueva operación llamada «multiplicar en cruz».

Es una abreviación de un argumento con inversos. Los denominadores no nulos son hipótesis matemáticas, no detalles de notación.
:::

#### Auditar una manipulación algebraica completa

Podemos aplicar ahora todo el repertorio a una cadena que en un curso elemental escribiríamos casi automáticamente.

::: {#exm-t1-0041}
**De una cadena escolar a una prueba auditada.** Sean $a,b,c\in F$ con $b\ne0$. Resolvamos

$$
\frac{x-a}{b}=c.
$$
:::

La cadena habitual es

$$
\frac{x-a}{b}=c
\iff
x-a=bc
\iff
x=a+bc.
$$

El resultado es correcto, pero ahora podemos explicar cada flecha.

**Primer paso.** Por definición de cociente,

$$
\frac{x-a}{b}
=
(x-a)b^{-1}.
$$

La hipótesis $b\ne0$ ya es necesaria para que el cociente original esté definido y garantiza además la existencia de $b^{-1}$. Multiplicar una igualdad por $b$ es legal incluso sin esa hipótesis; la no nulidad será necesaria cuando reduzcamos $b^{-1}b$ a $1$.

Multiplicando ambos miembros por $b$,

$$
\bigl((x-a)b^{-1}\bigr)b=cb.
$$

Reducimos primero el miembro izquierdo:

$$
\begin{aligned}
\bigl((x-a)b^{-1}\bigr)b
&=(x-a)(b^{-1}b) && \text{(asociatividad)}\\
&=(x-a)1 && \text{(inverso multiplicativo)}\\
&=x-a && \text{(neutro multiplicativo)}.
\end{aligned}
$$

En el miembro derecho, por conmutatividad,

$$
cb=bc.
$$

Por tanto,

$$
x-a=bc.
$$

Además, esta flecha es reversible. Si partimos de $x-a=bc$ y multiplicamos ambos miembros por $b^{-1}$, obtenemos

$$
(x-a)b^{-1}=(bc)b^{-1}.
$$

Por asociatividad y por $bb^{-1}=1$,

$$
(bc)b^{-1}
=
c(bb^{-1})
=
c,
$$

de modo que recuperamos

$$
\frac{x-a}{b}=c.
$$

**Segundo paso.** Por definición de resta,

$$
x-a=x+(-a),
$$

así que la ecuación anterior es

$$
x+(-a)=bc.
$$

Sumamos $a$ a ambos miembros:

$$
\bigl(x+(-a)\bigr)+a=bc+a.
$$

El miembro izquierdo se reduce paso a paso:

$$
\begin{aligned}
\bigl(x+(-a)\bigr)+a
&=x+\bigl((-a)+a\bigr) && \text{(asociatividad)}\\
&=x+0 && \text{(inverso aditivo)}\\
&=x && \text{(neutro aditivo)}.
\end{aligned}
$$

Por consiguiente,

$$
x=bc+a.
$$

Finalmente, por conmutatividad de la suma,

$$
bc+a=a+bc,
$$

y obtenemos

$$
\boxed{x=a+bc}.
$$

También esta flecha es reversible: sumando $-a$ a ambos miembros de $x=a+bc$ recuperamos $x-a=bc$. Por tanto, no solo hemos encontrado un candidato; hemos mostrado una cadena de equivalencias. En particular, @thm-t1-0011 garantiza que la solución es única.

Podemos resumir la auditoría así:

| Movimiento escolar | Estructura que realmente utiliza |
|---|---|
| «multiplicar ambos miembros por $b$» | sustitución en una igualdad; por sí sola no exige $b\ne0$ |
| «se cancela $b$» | $b\ne0$, existencia de $b^{-1}$, $b^{-1}b=1$ y neutro multiplicativo |
| «pasar $a$ sumando» | resta $=$ suma con inverso; asociatividad, inverso y neutro aditivos |
| «la solución es la única» | reversibilidad de las equivalencias y @thm-t1-0011 |

La última fila es importante. Encontrar un valor que satisface una ecuación prueba **existencia**; demostrar que ningún otro valor puede satisfacerla prueba **unicidad**.

#### El árbol algebraico que acabamos de construir

La cantidad de fórmulas obtenidas puede dar la impresión de que hemos reemplazado nueve axiomas por una lista todavía más larga. Esa no es la lectura correcta.

Lo que importa es la dependencia:

$$
\boxed{
\begin{aligned}
&\text{axiomas de cuerpo}\\
&\qquad\downarrow\\
&\text{unicidad de neutros e inversos}\\
&\qquad\downarrow\\
&a0=0,\ \text{reglas de signos e inversos}\\
&\qquad\downarrow\\
&\text{cancelación y producto nulo}\\
&\qquad\downarrow\\
&\text{existencia y unicidad en ecuaciones}\\
&\qquad\downarrow\\
&\text{resta y división}\\
&\qquad\downarrow\\
&\text{reglas de fracciones}.
\end{aligned}
}
$$

El árbol importa más que la lista de hojas.

A partir de ahora podremos usar estas consecuencias sin reconstruir cada vez toda su genealogía. Pero cuando una manipulación sea delicada —especialmente si aparece una división, una cancelación o una hipótesis de no nulidad— tendremos un criterio para auditarla.

Hay, además, una conclusión conceptual decisiva. **Nada de lo demostrado hasta aquí utiliza orden.** Todos estos resultados son afirmaciones acerca de cuerpos. Por eso siguen siendo válidos en otros cuerpos que no se comportan como la recta real.

Para desarrollar cálculo necesitamos ahora una segunda capa: el **orden**. Hasta aquí solo hemos utilizado las operaciones del cuerpo. Todavía no hemos explicado qué significa que un elemento esté a la derecha de otro, por qué sumar la misma cantidad conserva una desigualdad ni por qué multiplicar por un número negativo invierte su sentido.

Todas esas afirmaciones pertenecen a la **estructura de orden**.

En lugar de postular de una vez una larga lista de reglas para el símbolo $<$, seguiremos una estrategia más económica: distinguiremos primero qué elementos llamaremos **positivos** y exigiremos tres propiedades básicas. A partir de ellas construiremos el orden y demostraremos sus reglas de manipulación.

Esta elección permite prolongar el mismo principio que guió la capa algebraica:

$$
\boxed{
\text{axiomas mínimos}
\longrightarrow
\text{consecuencias demostradas}
\longrightarrow
\text{reglas de uso cotidiano}.
}
$$

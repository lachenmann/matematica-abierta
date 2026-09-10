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

entonces

$$
ab^{-1}=cd^{-1}.
$$

Multiplicamos ambos miembros por $bd$ y reagrupamos mediante asociatividad y conmutatividad:

$$
ad=bc.
$$

Recíprocamente, si

$$
ad=bc,
$$

multiplicamos ambos miembros por $b^{-1}d^{-1}$. Usando asociatividad, conmutatividad e inversos,

$$
ab^{-1}=cd^{-1},
$$

es decir,

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

La hipótesis $b\ne0$ ya es necesaria para que el cociente original esté definido y garantiza además la existencia de $b^{-1}$. Multiplicar una igualdad por $b$ es legal incluso sin esa hipótesis; la no nulidad será necesaria en el paso siguiente, cuando usemos
$$
b^{-1}b=1.
$$

Multiplicando ambos miembros por $b$,

$$
(x-a)b^{-1}b=cb.
$$

Asociatividad e inverso multiplicativo dan

$$
x-a=bc.
$$

**Segundo paso.** Por definición de resta,

$$
x-a=x+(-a).
$$

Por @thm-t1-0011, la ecuación

$$
x+(-a)=bc
$$

tiene una única solución. Como el inverso aditivo de $-a$ es $a$,

$$
x=bc+a=a+bc.
$$

Por tanto,

$$
\boxed{x=a+bc}
$$

es la única solución.

Podemos resumir la auditoría así:

| Movimiento escolar | Estructura que realmente utiliza |
|---|---|
| «multiplicar ambos miembros por $b$» | sustitución en una igualdad; por sí sola no exige $b\ne0$ |
| «se cancela $b$» | $b\ne0$, existencia de $b^{-1}$, $b^{-1}b=1$ y neutro multiplicativo |
| «pasar $a$ sumando» | resta $=$ suma con inverso y @thm-t1-0011 |
| «la solución es la única» | cancelación / unicidad, no solo sustitución |

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

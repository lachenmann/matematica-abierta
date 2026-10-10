## Inyectividad, sobreyectividad y biyectividad {#sec-t1-c03-03}

La sección anterior terminó con dos preguntas sobre una función

$$
f\colon A\to B.
$$

La primera miraba hacia el codominio:

> ¿todo $y\in B$ es realmente alcanzado por alguna entrada?

La segunda miraba hacia las fibras de un valor:

> si dos entradas producen la misma salida, ¿tienen necesariamente que ser la misma entrada?

Estas preguntas describen dos propiedades diferentes. Una controla **cuántas salidas del codominio se alcanzan**; la otra controla **cuántas entradas pueden compartir una salida**. Conviene aprenderlas por separado antes de combinarlas.

### Tres propiedades y tres preguntas distintas

::: {#def-t1-0022}
**Inyectividad, sobreyectividad y biyectividad.** Sea

$$
f\colon A\to B.
$$

Diremos que $f$ es **inyectiva** si, para cualesquiera $x_1,x_2\in A$,

$$
f(x_1)=f(x_2)
\quad\Longrightarrow\quad
x_1=x_2.
$$

Diremos que $f$ es **sobreyectiva** si cada elemento del codominio es imagen de alguna entrada; es decir, si

$$
\forall y\in B\;\exists x\in A
\quad
f(x)=y.
$$

Equivalentemente,

$$
f(A)=B.
$$

Diremos que $f$ es **biyectiva** si es simultáneamente inyectiva y sobreyectiva.
:::

Las tres palabras responden, por tanto, a preguntas muy concretas:

- **inyectiva:** ¿pueden dos entradas distintas compartir una salida?;
- **sobreyectiva:** ¿queda algún elemento del codominio sin ser alcanzado?;
- **biyectiva:** ¿cada salida del codominio corresponde a una entrada y solo a una?

La última frase debe leerse con precisión. Una función biyectiva establece una correspondencia uno a uno entre el dominio y el codominio. La existencia de una función inversa formalizará esta idea en §3.5; no necesitamos todavía ese resultado para trabajar con la definición.

### Inyectividad: empezar suponiendo igualdad de imágenes

La forma lógica de la inyectividad ya nos indica cómo suele comenzar una demostración.

Queremos probar

$$
\forall x_1,x_2\in A,
\qquad
f(x_1)=f(x_2)\Longrightarrow x_1=x_2.
$$

Por tanto, el esqueleto estándar es:

1. toma $x_1,x_2\in A$ arbitrarios;
2. supone que $f(x_1)=f(x_2)$;
3. usa la regla de la función y las propiedades del dominio para deducir $x_1=x_2$.

Consideremos, por ejemplo,

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=3x-7.
$$

Para probar que $p$ es inyectiva, sean $x_1,x_2\in\mathbb R$ y supongamos

$$
p(x_1)=p(x_2).
$$

Entonces

$$
3x_1-7=3x_2-7.
$$

Sumando $7$ y dividiendo por $3$ obtenemos

$$
x_1=x_2.
$$

Luego $p$ es inyectiva.

Obsérvese que no hemos comenzado escogiendo una salida arbitraria. Para la inyectividad, la información inicial útil es la **igualdad de dos imágenes**.

::: {.callout-warning title="Error frecuente"}
Demostrar que para cada $x\in A$ existe un único valor $f(x)$ **no demuestra inyectividad**.

Eso demuestra que la regla está bien definida como función: una entrada no recibe dos salidas.

La inyectividad exige una afirmación diferente:

$$
f(x_1)=f(x_2)\Longrightarrow x_1=x_2.
$$

Es decir, dos entradas no pueden compartir una misma salida salvo que en realidad sean la misma entrada.
:::

### Cómo demostrar que una función no es inyectiva

Negar la definición produce un criterio muy útil. Una función $f\colon A\to B$ **no** es inyectiva si existen $x_1,x_2\in A$ tales que

$$
x_1\ne x_2
$$

pero

$$
f(x_1)=f(x_2).
$$

Por tanto, para refutar la inyectividad basta un solo par de entradas distintas con la misma imagen.

Para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

tenemos

$$
2\ne-2
$$

pero

$$
f(2)=4=f(-2).
$$

Ese par constituye un contraejemplo completo a la inyectividad.

En el lenguaje de §3.2, la misma observación puede expresarse diciendo que

$$
f^{-1}(\{4\})=\{-2,2\}
$$

contiene más de un elemento.

### Sobreyectividad: comenzar con una salida arbitraria

La forma lógica de la sobreyectividad es diferente:

$$
\forall y\in B\;\exists x\in A
\quad
f(x)=y.
$$

Ahora el procedimiento natural es:

1. toma un $y\in B$ arbitrario;
2. busca o construye una entrada $x\in A$ que pueda producirlo;
3. verifica que esa entrada pertenece realmente al dominio;
4. comprueba que $f(x)=y$.

Volvamos a

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=3x-7.
$$

Sea $y\in\mathbb R$ arbitrario. Queremos resolver

$$
3x-7=y
$$

para $x$. La ecuación sugiere

$$
x=\frac{y+7}{3}.
$$

Como $y\in\mathbb R$, también

$$
\frac{y+7}{3}\in\mathbb R,
$$

de modo que la entrada propuesta pertenece al dominio. Finalmente,

$$
p\left(\frac{y+7}{3}\right)
=
3\left(\frac{y+7}{3}\right)-7
=
y.
$$

Como el argumento funciona para todo $y\in\mathbb R$, la función $p$ es sobreyectiva.

Este ejemplo ilustra un principio general: una prueba de sobreyectividad es, con frecuencia, una **prueba de existencia parametrizada por una salida arbitraria**.

### Cómo demostrar que una función no es sobreyectiva

Para refutar la sobreyectividad debemos exhibir al menos un elemento del codominio que no sea alcanzado.

La negación de

$$
\forall y\in B\;\exists x\in A,
\qquad f(x)=y
$$

es

$$
\exists y\in B\;\forall x\in A,
\qquad f(x)\ne y.
$$

Así, basta encontrar un $y\in B$ tal que

$$
f^{-1}(\{y\})=\varnothing.
$$

Por ejemplo, para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

el número $-1$ pertenece al codominio, pero

$$
f^{-1}(\{-1\})=\varnothing.
$$

Luego $f$ no es sobreyectiva.

La misma conclusión se obtiene a partir del recorrido:

$$
f(\mathbb R)=[0,\infty)\ne\mathbb R.
$$

### Una misma fórmula, las cuatro posibilidades

Ahora podemos volver con plena precisión al contraste que abrió el capítulo.

::: {#exm-t1-0023}
**Cuatro clasificaciones con la regla $x\mapsto x^2$.** Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

$$
g\colon[0,\infty)\to[0,\infty),
\qquad g(x)=x^2,
$$

$$
h\colon\mathbb R\to[0,\infty),
\qquad h(x)=x^2,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad k(x)=x^2.
$$

Entonces:

1. $f$ no es inyectiva ni sobreyectiva;
2. $g$ es biyectiva;
3. $h$ es sobreyectiva pero no inyectiva;
4. $k$ es inyectiva pero no sobreyectiva.
:::

Demostremos cada afirmación, porque las razones son más importantes que la tabla final.

**1. La función $f$ no es inyectiva.** Ya vimos que

$$
f(2)=f(-2)=4
$$

con $2\ne-2$.

**2. La función $f$ no es sobreyectiva.** Ningún real negativo pertenece a su imagen; por ejemplo,

$$
f^{-1}(\{-1\})=\varnothing.
$$

**3. La función $g$ es inyectiva.** Sean $x_1,x_2\in[0,\infty)$ y supongamos

$$
x_1^2=x_2^2.
$$

Entonces

$$
(x_1-x_2)(x_1+x_2)=0.
$$

Si $x_1-x_2=0$, ya tenemos $x_1=x_2$. Si $x_1+x_2=0$, como ambos números son no negativos, necesariamente

$$
x_1=x_2=0.
$$

En ambos casos $x_1=x_2$. Por tanto, $g$ es inyectiva.

**4. La función $g$ es sobreyectiva.** Sea $y\in[0,\infty)$. Por el resultado de existencia de raíces de `T1-C02`, existe $\sqrt y\in[0,\infty)$ y

$$
g(\sqrt y)=(\sqrt y)^2=y.
$$

Así, cada elemento del codominio tiene un antecedente. Luego $g$ es sobreyectiva y, por tanto, biyectiva.

**5. La función $h$ es sobreyectiva.** El mismo argumento con $\sqrt y$ funciona para todo $y\in[0,\infty)$.

**6. La función $h$ no es inyectiva.** De nuevo,

$$
h(2)=h(-2).
$$

**7. La función $k$ es inyectiva.** Su dominio coincide con el de $g$, y el argumento anterior para entradas no negativas demuestra la inyectividad.

**8. La función $k$ no es sobreyectiva.** Su codominio es $\mathbb R$, pero ningún número negativo es un cuadrado real.

La tabla completa es entonces

$$
\boxed{
\begin{array}{c|c|c}
\text{función} & \text{inyectiva} & \text{sobreyectiva}\\
\hline
f\colon\mathbb R\to\mathbb R & \text{no} & \text{no}\\
g\colon[0,\infty)\to[0,\infty) & \text{sí} & \text{sí}\\
h\colon\mathbb R\to[0,\infty) & \text{no} & \text{sí}\\
k\colon[0,\infty)\to\mathbb R & \text{sí} & \text{no}
\end{array}}
$$

Una sola expresión algebraica ha producido las cuatro combinaciones posibles.

### El dominio controla colisiones

Comparemos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

con su restricción

$$
k=f|_{[0,\infty)}.
$$

La primera no es inyectiva y la segunda sí.

¿Qué cambió? No la fórmula. Cambió el conjunto de entradas permitidas. Al eliminar los números negativos, dejamos de tener simultáneamente los pares $x$ y $-x$ que producían la misma salida.

Esto sugiere una operación frecuente:

> cuando una función falla en ser inyectiva porque distintas regiones del dominio repiten valores, puede ser útil restringir el dominio a una región donde esas colisiones desaparezcan.

Pero la palabra «puede» importa. Restringir el dominio no garantiza automáticamente la inyectividad. Si restringimos $x^2$ al dominio

$$
[-2,-1]\cup[1,2],
$$

siguen apareciendo pares $x$ y $-x$ con la misma imagen.

Por tanto, una restricción debe elegirse por una razón matemática concreta.

### El codominio controla la sobreyectividad

Comparemos ahora

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

con

$$
h\colon\mathbb R\to[0,\infty),
\qquad h(x)=x^2.
$$

Dominio y regla son iguales. Sin embargo, $f$ no es sobreyectiva y $h$ sí.

La diferencia está únicamente en el codominio.

Para cualquier función

$$
u\colon A\to B,
$$

si sabemos que su imagen es

$$
u(A)=C\subseteq B,
$$

podemos considerar la misma asignación con codominio ajustado a su imagen:

$$
\widetilde u\colon A\to C,
\qquad
\widetilde u(x)=u(x).
$$

Por construcción,

$$
\widetilde u(A)=C,
$$

así que $\widetilde u$ es sobreyectiva.

No hemos demostrado una propiedad nueva de la antigua función $u$. Hemos definido una función distinta porque, según la convención de §3.1, el codominio forma parte de los datos de una función.

Esta observación evita una frase imprecisa que aparece a veces en cálculos informales: «toda función es sobreyectiva sobre su imagen». La idea es correcta si se entiende que estamos **cambiando el codominio y, por tanto, formando una nueva función**.

### Qué cambia y qué no al modificar dominio o codominio

Conviene reunir las observaciones anteriores.

- **Restringir el dominio** puede eliminar colisiones y convertir una función no inyectiva en inyectiva.
- Restringir el dominio también puede hacer que se pierdan valores antes alcanzados y, por tanto, puede destruir sobreyectividad.
- **Cambiar el codominio**, manteniendo la misma regla y el mismo dominio, no altera si dos entradas producen o no la misma salida; por tanto, no altera la cuestión de la inyectividad mientras el nuevo codominio siga conteniendo todas las imágenes.
- En cambio, el codominio es parte esencial de la sobreyectividad: una misma asignación puntual puede ser sobreyectiva hacia un codominio y no serlo hacia otro mayor.

Esta sensibilidad explica por qué una declaración funcional completa

$$
f\colon A\to B
$$

no puede sustituirse impunemente por una fórmula aislada.

### Dos pruebas, dos arquitecturas lógicas

Supongamos que queremos demostrar que

$$
p\colon\mathbb R\to\mathbb R,
\qquad
p(x)=5x+1
$$

es biyectiva.

No conviene escribir una sola cadena de cálculos sin indicar qué propiedad estamos probando. Una prueba rigurosa tiene dos partes conceptualmente distintas.

**Inyectividad.** Sean $x_1,x_2\in\mathbb R$ y supongamos

$$
p(x_1)=p(x_2).
$$

Entonces

$$
5x_1+1=5x_2+1,
$$

de donde

$$
x_1=x_2.
$$

**Sobreyectividad.** Sea $y\in\mathbb R$ arbitrario. Tomemos

$$
x=\frac{y-1}{5}.
$$

Este $x$ pertenece al dominio y satisface

$$
p(x)
=
5\left(\frac{y-1}{5}\right)+1
=y.
$$

Por tanto, $p$ es inyectiva y sobreyectiva; luego es biyectiva.

La diferencia entre las dos mitades se ve incluso antes de calcular:

$$
\boxed{
\begin{array}{c|c}
\text{inyectividad} & \forall x_1\,\forall x_2\\
\text{sobreyectividad} & \forall y\,\exists x
\end{array}}
$$

En una, comparamos dos entradas arbitrarias. En la otra, debemos construir una entrada que puede depender de una salida arbitraria.

### Negaciones útiles para buscar contraejemplos

Las negaciones también tienen formas diferentes.

Para refutar la inyectividad buscamos

$$
\boxed{
\exists x_1,x_2\in A:
\quad
x_1\ne x_2
\quad\text{y}\quad
f(x_1)=f(x_2).
}
$$

Para refutar la sobreyectividad buscamos

$$
\boxed{
\exists y\in B:
\quad
\forall x\in A,
\quad
f(x)\ne y.
}
$$

En lenguaje de preimágenes:

- no inyectiva: alguna preimagen puntual contiene al menos dos elementos;
- no sobreyectiva: alguna preimagen puntual es vacía.

Esto hace visible una conexión muy útil entre §§3.2 y 3.3. Para cada $y\in B$, observemos el conjunto

$$
f^{-1}(\{y\}).
$$

Entonces:

- la sobreyectividad exige que **ninguno** de esos conjuntos sea vacío;
- la inyectividad exige que **ninguno** tenga más de un elemento;
- la biyectividad exige que cada uno contenga **exactamente un** elemento.

Podemos condensarlo así:

$$
\boxed{
\begin{array}{c|c}
\text{propiedad} & \text{tamaño de }f^{-1}(\{y\})\\
\hline
\text{inyectiva} & \le 1\text{ para todo }y\in B\\
\text{sobreyectiva} & \ge 1\text{ para todo }y\in B\\
\text{biyectiva} & =1\text{ para todo }y\in B
\end{array}}
$$

No estamos usando cardinalidad infinita ni una teoría nueva de tamaños de conjuntos. Solo distinguimos aquí entre vacío, unitario y «más de un elemento».

### Antes de seguir

Cuando leas una afirmación de la forma

> «$f$ es biyectiva»,

no intentes demostrarla de una sola vez. Pregunta primero:

1. ¿cómo probaré la inyectividad?
2. ¿cómo probaré la sobreyectividad?

Y cuando leas

> «$f$ no es biyectiva»,

recuerda que basta con que falle **una** de las dos propiedades. No necesitas demostrar que fallan ambas.

Esta separación será fundamental en §3.4. Allí estudiaremos qué sucede con estas propiedades cuando dos funciones se encadenan mediante composición. Por ahora, el mapa conceptual del capítulo ha avanzado un paso:

$$
\boxed{
\text{función completa}
\to
\text{imagen/preimagen}
\to
\text{inyectividad/sobreyectividad/biyectividad}.
}
$$

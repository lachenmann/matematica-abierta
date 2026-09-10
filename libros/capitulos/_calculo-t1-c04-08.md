## Sucesiones recursivas: fabricar y controlar un límite {#sec-t1-c04-08}

Las sucesiones estudiadas hasta ahora estaban dadas, en su mayoría, por una fórmula que permitía calcular directamente el término de índice $n$. Por ejemplo,

$$
a_n=\frac{1}{n+1}
$$

nos entrega $a_n$ sin necesidad de conocer $a_{n-1}$.

Una **regla recursiva** funciona de otra manera. En lugar de decirnos directamente cuánto vale el término de índice $n$, nos indica cómo fabricar el término siguiente a partir de uno o varios términos anteriores.

Por ejemplo,

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}
$$

produce sucesivamente

$$
a_1=\sqrt3,
$$

$$
a_2=\sqrt{2+\sqrt3},
$$

$$
a_3=\sqrt{2+\sqrt{2+\sqrt3}},
$$

y así indefinidamente, siempre que cada paso esté bien definido.

Esta diferencia cambia también la estrategia de estudio. Una fórmula explícita puede permitirnos comparar directamente $a_n$ con un candidato de límite. En una recurrencia, en cambio, la información principal suele estar escondida en la relación entre términos consecutivos.

La pregunta deja de ser solamente

> ¿qué expresión tiene $a_n$?,

y pasa a ser

> **¿qué propiedades conserva el procedimiento que transforma $a_n$ en $a_{n+1}$?**

Ese cambio de mirada será el centro de esta sección.

### Una regla recursiva no garantiza por sí sola una sucesión real infinita

Es fácil escribir una recurrencia sintácticamente correcta y olvidar que cada término posterior debe existir dentro del sistema numérico en el que estamos trabajando.

Por ejemplo, si intentáramos definir

$$
c_0=-3,
\qquad
c_{n+1}=\sqrt{2+c_n},
$$

el primer paso exigiría

$$
c_1=\sqrt{-1},
$$

que no es un número real.

Por tanto, la expresión

$$
c_{n+1}=\sqrt{2+c_n}
$$

no basta por sí sola para garantizar una sucesión real definida para todo $n\in\mathbb N$. Debemos verificar que, cada vez que aplicamos la regla, el nuevo término vuelve a quedar dentro del dominio donde el siguiente paso tiene sentido.

Esta observación es una versión dinámica de una pregunta ya conocida desde `T1-C03`:

$$
\boxed{
\text{antes de usar una regla, debemos comprobar que está bien definida sobre los objetos que realmente aparecen.}
}
$$

En una recurrencia esa comprobación suele hacerse encontrando una **región invariante**: un conjunto de valores del cual la regla no consigue sacar a la sucesión.

No introduciremos una teoría abstracta de sistemas dinámicos. Nos basta la idea operativa:

> si demostramos que $a_n$ pertenece a cierto intervalo y que esa pertenencia obliga a que $a_{n+1}$ permanezca en el mismo intervalo, la inducción controla todos los términos.

### Cinco preguntas para auditar una recurrencia

A partir de ahora organizaremos muchos problemas recursivos mediante cinco preguntas.

1. **¿Está bien definida?**  
   ¿Cada paso produce un número real permitido?

2. **¿Qué región permanece invariante?**  
   ¿Podemos encerrar todos los términos en un intervalo o encontrar una barrera útil?

3. **¿Es monótona?**  
   ¿Los términos avanzan sistemáticamente en una dirección?

4. **¿Por qué existe un límite?**  
   Si obtenemos monotonía y una cota en la dirección correcta, podemos invocar @thm-t1-0010.

5. **Una vez demostrada la existencia, ¿cómo identificamos el límite?**  
   Aquí utilizaremos desplazamiento de índices y el álgebra de límites de §4.4.

La separación entre las preguntas 4 y 5 es esencial:

$$
\boxed{
\text{demostrar existencia del límite}
\neq
\text{resolver una ecuación que un eventual límite tendría que satisfacer}.
}
$$

Una ecuación puede producir **candidatos**. No produce por sí sola convergencia.

### El ejemplo rector: un radical construido término a término

Analicemos completamente la sucesión

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}.
$$

Los primeros términos son aproximadamente

$$
1,\quad
1.732,\quad
1.932,\quad
1.983,\quad\dots
$$

Esta inspección sugiere dos conjeturas:

- los términos parecen crecer;
- parecen acercarse a $2$ sin superarlo.

Pero una tabla finita no demuestra ninguna de las dos afirmaciones. Nuestro objetivo será convertir esas observaciones en una cadena deductiva completa.

::: {#exm-t1-0038}
**Una recurrencia controlada desde el principio hasta el límite.** Sea $(a_n)$ la sucesión definida por

$$
a_0=1,
\qquad
a_{n+1}=\sqrt{2+a_n}.
$$

Demostraremos, en este orden, que

1. la sucesión está bien definida para todo $n$;
2. 
   $$
   1\le a_n<2
   $$
   para todo $n$;
3. $(a_n)$ es estrictamente creciente;
4. $(a_n)$ converge por el teorema de convergencia monótona;
5. su límite es
   $$
   2.
   $$

**Paso 1 y paso 2: bien definida y región invariante.**

Demostraremos por inducción la afirmación

$$
P(n):\qquad 1\le a_n<2.
$$

**Caso base.** Como

$$
a_0=1,
$$

se cumple inmediatamente

$$
1\le a_0<2.
$$

**Paso inductivo.** Supongamos que para algún $n\in\mathbb N$ tenemos

$$
1\le a_n<2.
$$

Entonces

$$
3\le 2+a_n<4.
$$

En particular,

$$
2+a_n>0,
$$

de modo que la raíz cuadrada real

$$
a_{n+1}=\sqrt{2+a_n}
$$

está bien definida.

Además, como $a_{n+1}\ge0$ y

$$
a_{n+1}^2=2+a_n,
$$

las desigualdades

$$
1<3\le a_{n+1}^2<4=2^2
$$

implican

$$
1<a_{n+1}<2.
$$

Por tanto,

$$
1\le a_{n+1}<2.
$$

La inducción queda cerrada. Hemos demostrado simultáneamente que todos los pasos de la recurrencia tienen sentido en $\mathbb R$ y que

$$
\boxed{
1\le a_n<2
\qquad
\text{para todo }n\in\mathbb N.
}
$$

El intervalo $[1,2)$ es, en este sentido, una región invariante para la recurrencia.

En particular, $2$ es una cota superior de la sucesión.

**Paso 3: monotonía.**

Queremos demostrar que

$$
a_{n+1}>a_n
$$

para todo $n$.

Ya sabemos que ambos números son no negativos. Por tanto, podemos comparar sus cuadrados.

Usando la recurrencia,

$$
a_{n+1}^2-a_n^2
=
(2+a_n)-a_n^2.
$$

Factorizamos:

$$
\begin{aligned}
2+a_n-a_n^2
&=-(a_n^2-a_n-2)\\
&=-(a_n-2)(a_n+1)\\
&=(2-a_n)(a_n+1).
\end{aligned}
$$

Por el paso anterior,

$$
a_n<2
$$

y

$$
a_n\ge1,
$$

así que

$$
2-a_n>0
$$

y

$$
a_n+1>0.
$$

Por consiguiente,

$$
a_{n+1}^2-a_n^2
=
(2-a_n)(a_n+1)
>0.
$$

Luego

$$
a_{n+1}^2>a_n^2.
$$

Como $a_{n+1}\ge0$ y $a_n\ge0$, se sigue que

$$
a_{n+1}>a_n.
$$

Así, $(a_n)$ es estrictamente creciente.

**Paso 4: existencia del límite.**

Hemos demostrado dos propiedades:

$$
(a_n)\text{ es creciente}
$$

y

$$
a_n<2
\qquad
\text{para todo }n.
$$

Por tanto, la sucesión es creciente y está acotada superiormente.

Aplicando @thm-t1-0010, existe un número real $L$ tal que

$$
a_n\to L.
$$

Además, el teorema identifica abstractamente ese número como

$$
L=\sup\{a_n:n\in\mathbb N\}.
$$

Como cada término satisface

$$
1\le a_n<2,
$$

tenemos en particular

$$
1\le L\le2.
$$

Hasta aquí hemos demostrado **existencia**. Todavía no hemos demostrado que $L=2$.

**Paso 5: identificación del límite sin continuidad.**

Como

$$
a_n\to L,
$$

la invariancia por desplazamiento de índices establecida en §4.3 da

$$
a_{n+1}\to L.
$$

La recurrencia satisface, para todo $n$,

$$
a_{n+1}^2=2+a_n.
$$

Ahora utilizamos únicamente el álgebra de límites ya demostrada.

Como

$$
a_{n+1}\to L,
$$

la regla del producto implica

$$
a_{n+1}^2
=
a_{n+1}a_{n+1}
\to
L^2.
$$

Y como

$$
a_n\to L,
$$

las reglas para constantes y sumas dan

$$
2+a_n\to2+L.
$$

Pero las sucesiones

$$
(a_{n+1}^2)
$$

y

$$
(2+a_n)
$$

son idénticas término a término. Por unicidad del límite,

$$
L^2=2+L.
$$

Reordenando,

$$
L^2-L-2=0,
$$

y factorizando,

$$
(L-2)(L+1)=0.
$$

Los candidatos algebraicos son, por tanto,

$$
L=2
$$

o

$$
L=-1.
$$

Sin embargo, ya sabemos que

$$
1\le L\le2.
$$

La segunda posibilidad queda excluida. Luego

$$
\boxed{
\lim_{n\to\infty}a_n=2.
}
$$
:::

La demostración anterior es importante porque ninguna de sus piezas puede intercambiarse libremente de posición.

La ecuación

$$
L^2=L+2
$$

solo aparece **después** de saber que existe un límite $L$.

Antes de ese punto, la letra $L$ no designa todavía un objeto cuya existencia esté demostrada.

### Cómo se descubre la barrera $2$

En una demostración final conviene presentar las ideas en orden lógico. Durante la búsqueda, sin embargo, podemos trabajar hacia atrás.

Los primeros términos sugieren que $2$ podría desempeñar un papel especial. Para comprobar si es una barrera estable, preguntamos:

> si $a_n<2$, ¿la recurrencia obliga a que también $a_{n+1}<2$?

La condición buscada es

$$
\sqrt{2+a_n}<2.
$$

Como ambos lados son no negativos, podemos elevar al cuadrado y obtener la condición equivalente

$$
2+a_n<4,
$$

es decir,

$$
a_n<2.
$$

La desigualdad que queremos conservar reaparece exactamente en el lado derecho.

Este es un indicio muy fuerte de invariancia:

$$
a_n<2
\quad\Longrightarrow\quad
a_{n+1}<2.
$$

La cota no fue entonces una adivinanza gratuita. La propia recurrencia nos permite comprobar si una barrera propuesta se reproduce de un paso al siguiente.

La búsqueda de regiones invariantes suele funcionar así:

1. conjeturamos una región a partir de los primeros términos o de la forma algebraica de la regla;
2. suponemos que $a_n$ pertenece a esa región;
3. utilizamos la recurrencia para demostrar que $a_{n+1}$ vuelve a pertenecer;
4. cerramos el argumento por inducción.

### Cómo se descubre la monotonía

También podemos reconstruir la búsqueda de la desigualdad

$$
a_{n+1}>a_n.
$$

La recurrencia nos dice

$$
a_{n+1}=\sqrt{2+a_n}.
$$

Como ya sabemos que los términos son positivos, podemos comparar cuadrados:

$$
a_{n+1}>a_n
\quad\Longleftrightarrow\quad
a_{n+1}^2>a_n^2.
$$

Sustituyendo la recurrencia,

$$
2+a_n>a_n^2.
$$

Llevando todo a un lado,

$$
2+a_n-a_n^2>0.
$$

Y la factorización

$$
2+a_n-a_n^2=(2-a_n)(a_n+1)
$$

revela por qué la región invariante encontrada en el paso anterior era exactamente la información que necesitábamos.

Dentro de

$$
1\le a_n<2,
$$

ambos factores son positivos.

Así, la prueba de monotonía **reutiliza** la prueba de acotación. Las dos tareas no son independientes: encontrar una región adecuada puede proporcionar simultáneamente dominio, cotas y signo para la comparación entre términos consecutivos.

### La ecuación de punto fijo es una condición necesaria, no una prueba de convergencia

Existe un error particularmente tentador con las recurrencias.

Supongamos que escribimos

$$
x_{n+1}=F(x_n)
$$

y queremos estudiar su comportamiento. Es natural pensar:

> si $x_n\to L$, entonces también $x_{n+1}\to L$; por tanto, tal vez $L$ deba satisfacer $L=F(L)$.

La idea puede ser útil para **encontrar candidatos**, siempre que el paso algebraico utilizado para llegar a la ecuación esté justificado por resultados ya demostrados.

El error consiste en invertir la implicación:

$$
\boxed{
L=F(L)
\centernot\Longrightarrow
x_n\to L.
}
$$

Veamos un ejemplo elemental. Definamos

$$
y_0=1,
\qquad
y_{n+1}=3-y_n.
$$

Si alguien supone sin demostrar que $y_n$ tiene límite $L$, entonces el desplazamiento y el álgebra de límites obligarían a

$$
L=3-L,
$$

de donde

$$
L=\frac32.
$$

Pero calculemos los términos:

$$
y_0=1,
\qquad
y_1=2,
\qquad
y_2=1,
\qquad
y_3=2,
\qquad\dots
$$

La sucesión oscila para siempre.

Más aún, para todo $n$,

$$
\left|y_n-\frac32\right|
=
\frac12.
$$

Tomando, por ejemplo,

$$
\varepsilon=\frac14,
$$

ninguna cola satisface

$$
\left|y_n-\frac32\right|<\varepsilon.
$$

Por tanto,

$$
y_n\not\to\frac32.
$$

Y como cualquier eventual límite tendría que satisfacer necesariamente

$$
L=3-L,
$$

no existe ningún otro candidato posible. La sucesión diverge.

El número $3/2$ es un **punto fijo** de la regla

$$
F(x)=3-x,
$$

pero eso no obliga a que la órbita que comienza en $1$ se acerque a él.

La lección lógica es:

$$
\boxed{
\begin{array}{c}
\text{convergencia demostrada}\\
+\ \text{recurrencia}\\
+\ \text{leyes de límites}
\end{array}
\Longrightarrow
\text{ecuación necesaria para el límite},
}
$$

pero no al revés.

### En nuestro ejemplo no pasamos el límite «a través de la raíz»

Conviene aislar un detalle metodológico del @exm-t1-0038.

Podría resultar tentador escribir

$$
a_{n+1}=\sqrt{2+a_n}
$$

y, como $a_n\to L$, declarar inmediatamente

$$
L=\sqrt{2+L}.
$$

Ese paso sería precisamente utilizar, sin haberlo demostrado todavía, que la función

$$
x\mapsto\sqrt{x}
$$

preserva límites.

En este tratado esa propiedad pertenecerá a la teoría de continuidad posterior. No la necesitamos aquí.

En lugar de ello utilizamos la identidad algebraica

$$
a_{n+1}^2=2+a_n.
$$

Cada operación que aparece ahora —producto, suma y constante— ya tiene una ley de límites demostrada en §4.4.

Por eso la cadena legítima es

$$
\boxed{
a_n\to L
\Longrightarrow
a_{n+1}\to L
\Longrightarrow
a_{n+1}^2\to L^2
}
$$

y, simultáneamente,

$$
\boxed{
a_n\to L
\Longrightarrow
2+a_n\to2+L.
}
$$

La igualdad término a término entre ambos lados obliga entonces a

$$
L^2=2+L.
$$

No hemos apelado a continuidad de la raíz ni a un límite funcional.

### Existencia e identificación son dos problemas distintos

El ejemplo rector puede resumirse en dos bloques.

**Bloque A: demostrar existencia.**

$$
\boxed{
\begin{array}{c}
1\le a_n<2\\
a_{n+1}>a_n
\end{array}
\Longrightarrow
\text{creciente + cota superior}
\Longrightarrow
a_n\to L.
}
$$

Aquí entra la completitud a través de @thm-t1-0010.

**Bloque B: identificar el número.**

$$
\boxed{
a_n\to L
\Longrightarrow
a_{n+1}\to L
\Longrightarrow
L^2=L+2
\Longrightarrow
L\in\{-1,2\}
\Longrightarrow
L=2.
}
$$

Aquí entran la estabilidad bajo desplazamiento, el álgebra de límites y la información de orden obtenida antes.

Confundir ambos bloques produce uno de los errores más frecuentes en problemas de recurrencias.

### El protocolo reutilizable

Ante una sucesión definida por

$$
a_{n+1}=F(a_n),
$$

no buscaremos automáticamente una fórmula cerrada para $a_n$. Muchas recurrencias útiles pueden estudiarse sin ella.

El protocolo será:

$$
\boxed{
\begin{array}{c}
\text{1. bien definida}\\
\downarrow\\
\text{2. región invariante / cota}\\
\downarrow\\
\text{3. monotonía}\\
\downarrow\\
\text{4. existencia por convergencia monótona}\\
\downarrow\\
\text{5. identificación mediante desplazamiento + álgebra}
\end{array}
}
$$

No todos los problemas seguirán exactamente esta ruta. Algunas sucesiones no serán monótonas; otras necesitarán otra técnica. Pero cuando la recurrencia conserva una región y empuja los términos siempre en una misma dirección, este esquema debe ser una de las primeras estrategias que examinemos.

### Qué hemos ganado

La recurrencia

$$
a_{n+1}=\sqrt{2+a_n}
$$

nos permitió reunir por primera vez casi todas las herramientas del capítulo en una sola demostración:

- inducción para conservar una región;
- orden para construir cotas;
- comparación algebraica para demostrar monotonía;
- completitud, a través del teorema de convergencia monótona, para obtener existencia;
- estabilidad de colas y desplazamientos para pasar de $(a_n)$ a $(a_{n+1})$;
- álgebra de límites para identificar el valor final;
- control lógico para no confundir un punto fijo con una prueba de convergencia.

Esta arquitectura aparecerá muchas veces en análisis numérico, ecuaciones y procesos iterativos, aunque más adelante dispongamos de herramientas mucho más potentes.

Hasta ahora, sin embargo, todas las sucesiones convergentes del capítulo tenían un límite real finito.

La siguiente pregunta será qué lenguaje utilizar cuando los términos crecen más allá de toda cota real o disminuyen por debajo de toda cota real.

Ese será el objeto de §4.9: los **límites infinitos** y la diferencia entre escapar sistemáticamente hacia $+\infty$ o $-\infty$ y ser simplemente no acotada.


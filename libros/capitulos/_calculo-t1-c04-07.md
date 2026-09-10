## Monotonía + completitud = convergencia {#sec-t1-c04-07}

Hasta ahora, para demostrar que una sucesión converge, hemos seguido casi siempre este esquema:

1. proponemos o descubrimos un candidato $L$;
2. demostramos que $a_n\to L$ mediante la definición, el álgebra o el sándwich.

Ese procedimiento responde bien a preguntas del tipo

$$
\text{«¿cuál es el límite de esta sucesión?»}
$$

cuando ya disponemos de una expresión que permite adivinar el candidato.

Pero existe otra pregunta, más estructural:

$$
\boxed{
\text{¿podemos demostrar que un límite existe sin conocer primero su valor?}
}
$$

La respuesta será afirmativa cuando una sucesión combine dos tipos de control que hasta ahora hemos mantenido separados:

- **monotonía**, que impide retrocesos en una dirección de orden;
- **acotación**, que impide avanzar indefinidamente en esa misma dirección.

La afirmación decisiva no será una propiedad puramente algebraica. Para convertir esos dos controles en la existencia de un número real que actúe como límite necesitaremos la **completitud de $\mathbb R$**.

Esta es la cadena que debemos hacer visible:

$$
\boxed{
\text{monotonía}
+
\text{cota}
+
\text{completitud}
\longrightarrow
\sup/\inf
\longrightarrow
\text{límite}.
}
$$

### Monotonía para sucesiones

Como una sucesión es una función cuyo dominio está ordenado, podemos trasladar directamente el lenguaje de monotonía desarrollado en `T1-C03`. Conviene, sin embargo, fijar la notación específica que usaremos a partir de ahora.

::: {#def-t1-0030}
**Sucesiones crecientes, decrecientes y monótonas.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

Diremos que $(a_n)$ es **creciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n\le a_m.
$$

Diremos que es **decreciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n\ge a_m.
$$

La sucesión es **monótona** si es creciente o decreciente.

Diremos que es **estrictamente creciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n<a_m,
$$

y **estrictamente decreciente** si

$$
n<m
\quad\Longrightarrow\quad
a_n>a_m.
$$
:::

En este tratado, por tanto, las palabras **creciente** y **decreciente** se usan en sentido débil: se permite la igualdad entre términos distintos. Cuando necesitemos excluirla diremos explícitamente **estrictamente** creciente o decreciente.

Por ejemplo, una sucesión constante es a la vez creciente y decreciente. Esta convención es importante porque el teorema que demostraremos no necesita monotonía estricta.

Para verificar monotonía suele bastar comparar términos consecutivos. Si

$$
a_n\le a_{n+1}
$$

para todo $n\ge n_0$, entonces, dados $n<m$, podemos encadenar

$$
a_n\le a_{n+1}\le\cdots\le a_m,
$$

y por tanto $a_n\le a_m$. El argumento para sucesiones decrecientes es análogo.

Así, en la práctica, muchas pruebas de monotonía comenzarán estudiando el signo de

$$
a_{n+1}-a_n
$$

o comparando directamente $a_{n+1}$ con $a_n$.

### Dos controles distintos: dirección y barrera

Una sucesión creciente satisface

$$
a_{n_0}\le a_{n_0+1}\le a_{n_0+2}\le\cdots.
$$

Esto controla la **dirección**, pero no impide que los términos crezcan sin límite real finito. La sucesión

$$
a_n=n
$$

es creciente y no está acotada superiormente.

Una cota superior, en cambio, proporciona una **barrera**. Si existe $M\in\mathbb R$ tal que

$$
a_n\le M
$$

para todo $n$, los términos no pueden atravesar $M$. Pero la acotación por sí sola no controla la dirección: $(-1)^n$ permanece entre $-1$ y $1$ y, sin embargo, oscila para siempre.

Por separado, entonces,

$$
\text{monotonía}
\qquad\text{y}\qquad
\text{acotación}
$$

no garantizan convergencia.

Lo notable es que, en $\mathbb R$, su combinación sí lo hace.

### ¿De dónde saldrá el candidato a límite?

Supongamos que $(a_n)$ es creciente y está acotada superiormente. Consideremos el conjunto de todos sus valores:

$$
S=\{a_n:n\ge n_0\}.
$$

El conjunto $S$ es no vacío y está acotado superiormente. Por la completitud de $\mathbb R$, existe

$$
L=\sup S.
$$

Aquí aparece el candidato que antes no teníamos que adivinar.

La elección no es arbitraria. Como $L$ es una cota superior,

$$
a_n\le L
$$

para todo $n$. Y como es la **menor** cota superior, cualquier número un poco menor que $L$ deja de ser cota superior.

En particular, para todo $\varepsilon>0$,

$$
L-\varepsilon
$$

no puede ser una cota superior de $S$. Por la caracterización aproximativa del supremo demostrada en `T1-C02`, existe entonces algún término $a_N$ tal que

$$
L-\varepsilon<a_N\le L.
$$

Hasta aquí hemos encontrado **un** término suficientemente próximo a $L$. Eso todavía no es convergencia: necesitamos controlar todos los términos posteriores.

Aquí entra exactamente la monotonía. Si $n\ge N$, entonces

$$
a_N\le a_n.
$$

Por tanto,

$$
L-\varepsilon<a_N\le a_n\le L<L+\varepsilon.
$$

Y ahora sí toda la cola queda atrapada en el intervalo

$$
(L-\varepsilon,L+\varepsilon).
$$

La prueba completa no necesita nada más.

::: {#thm-t1-0010}
**Teorema de convergencia monótona.** Sea $(a_n)_{n\ge n_0}$ una sucesión real.

1. Si $(a_n)$ es creciente y está acotada superiormente, entonces converge y
   $$
   \lim_{n\to\infty}a_n
   =
   \sup\{a_n:n\ge n_0\}.
   $$

2. Si $(a_n)$ es decreciente y está acotada inferiormente, entonces converge y
   $$
   \lim_{n\to\infty}a_n
   =
   \inf\{a_n:n\ge n_0\}.
   $$

En particular, toda sucesión monótona y acotada converge.

**Demostración.** Demostremos primero el caso creciente.

Sea

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada superiormente, $S$ es un conjunto no vacío y acotado superiormente. Por completitud de $\mathbb R$, existe

$$
L=\sup S.
$$

Queremos demostrar que $a_n\to L$.

Sea $\varepsilon>0$. Como $L$ es el supremo de $S$, el número

$$
L-\varepsilon
$$

no es una cota superior de $S$. Por tanto existe algún índice $N\ge n_0$ tal que

$$
L-\varepsilon<a_N.
$$

Como $L$ sí es una cota superior de $S$,

$$
a_n\le L
$$

para todo $n\ge n_0$.

Además, como la sucesión es creciente, para todo $n\ge N$ tenemos

$$
a_N\le a_n.
$$

Combinando las tres desigualdades,

$$
L-\varepsilon<a_N\le a_n\le L<L+\varepsilon.
$$

Así, para todo $n\ge N$,

$$
L-\varepsilon<a_n<L+\varepsilon,
$$

lo cual equivale a

$$
|a_n-L|<\varepsilon.
$$

Como $\varepsilon>0$ era arbitrario,

$$
a_n\to L.
$$

Por tanto,

$$
\lim_{n\to\infty}a_n
=
\sup\{a_n:n\ge n_0\}.
$$

Consideremos ahora el caso decreciente. Sea nuevamente

$$
S=\{a_n:n\ge n_0\}.
$$

Como la sucesión está acotada inferiormente, $S$ es no vacío y acotado inferiormente. La completitud de $\mathbb R$, mediante la existencia de ínfimos ya deducida en `T1-C02`, garantiza que existe

$$
L=\inf S.
$$

Sea $\varepsilon>0$. Como $L$ es el ínfimo de $S$, el número

$$
L+\varepsilon
$$

no es una cota inferior de $S$. Por tanto existe algún índice $N\ge n_0$ tal que

$$
a_N<L+\varepsilon.
$$

Como $L$ es una cota inferior,

$$
L\le a_n
$$

para todo $n\ge n_0$.

Y como la sucesión es decreciente, si $n\ge N$ entonces

$$
a_n\le a_N.
$$

En consecuencia,

$$
L-\varepsilon<L\le a_n\le a_N<L+\varepsilon.
$$

Por tanto,

$$
|a_n-L|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario,

$$
a_n\to L.
$$

Así,

$$
\lim_{n\to\infty}a_n
=
\inf\{a_n:n\ge n_0\}.
$$

Quedan demostradas ambas afirmaciones.
:::

### Dónde se usa exactamente cada hipótesis

El teorema es suficientemente importante como para auditar su demostración línea por línea.

En el caso creciente:

1. **Acotación superior.** Garantiza que el conjunto
   $$
   S=\{a_n:n\ge n_0\}
   $$
   tiene cotas superiores.
2. **Completitud de $\mathbb R$.** Garantiza que entre esas cotas existe una menor:
   $$
   L=\sup S\in\mathbb R.
   $$
3. **Propiedad aproximativa del supremo.** Para cada $\varepsilon>0$ produce un índice $N$ con
   $$
   L-\varepsilon<a_N.
   $$
4. **Monotonía creciente.** Propaga esa aproximación puntual a toda la cola:
   $$
   n\ge N
   \quad\Longrightarrow\quad
   a_N\le a_n.
   $$
5. **Propiedad de cota superior del supremo.** Impide que los términos atraviesen $L$:
   $$
   a_n\le L.
   $$

La arquitectura es, por tanto,

$$
\boxed{
\begin{array}{c}
\text{acotación superior}\
+\
\text{completitud}
\end{array}
\Longrightarrow
L=\sup S
\Longrightarrow
\begin{array}{c}
\text{un término entra cerca de }L\
+\
\text{monotonía}
\end{array}
\Longrightarrow
\text{toda la cola entra cerca de }L.
}
$$

El caso decreciente reproduce el mismo mecanismo con ínfimos y orden invertido.

### La completitud no está escondida: es el motor de existencia

En las primeras pruebas $\varepsilon$–$N$ del capítulo, la propiedad arquimediana nos permitía fabricar umbrales. En el teorema anterior ocurre algo distinto: antes de buscar un umbral necesitamos **producir el propio candidato a límite**.

Ese candidato aparece como

$$
\sup S
$$

o

$$
\inf S.
$$

La afirmación de que esos números existen en $\mathbb R$ no procede de la monotonía. Procede de la completitud.

Esto permite localizar con precisión el punto donde fallaría la misma demostración si trabajáramos únicamente en $\mathbb Q$. Un conjunto no vacío y acotado de racionales puede carecer de supremo racional, como vimos en `T1-C02`. En ese caso, el paso

$$
S\text{ acotado superiormente}
\quad\Longrightarrow\quad
\sup S\text{ existe en el mismo sistema numérico}
$$

no estaría disponible.

Por eso el teorema de convergencia monótona no es simplemente una consecuencia del orden: es una manifestación secuencial de la completitud de los números reales.

Podemos condensar esta segunda gran aparición operativa de completitud en el tratado como

$$
\boxed{
\text{completitud}
\longrightarrow
\sup/\inf
\longrightarrow
\text{convergencia monótona}.
}
$$

### Qué falla si quitamos una hipótesis

El teorema necesita las dos piezas de control.

**Sin acotación suficiente.** La sucesión

$$
a_n=n
$$

es creciente, pero no está acotada superiormente. Tampoco puede converger a un número real: si convergiera, @prp-t1-0020 implicaría que sería acotada, contradiciendo la propiedad arquimediana.

Así,

$$
\boxed{
\text{creciente}
\centernot\Longrightarrow
\text{convergente}.
}
$$

La versión decreciente presenta el mismo problema si falta una cota inferior.

**Sin monotonía.** La sucesión

$$
b_n=(-1)^n
$$

es acotada, pero @exm-t1-0033 demostró que diverge.

Por tanto,

$$
\boxed{
\text{acotada}
\centernot\Longrightarrow
\text{convergente}.
}
$$

Lo que sí obtenemos al combinar ambas condiciones es

$$
\boxed{
\text{monótona}+\text{acotada}
\Longrightarrow
\text{convergente}.
}
$$

No estamos corrigiendo las implicaciones falsas anteriores; estamos añadiendo exactamente la hipótesis que faltaba para convertirlas en un teorema verdadero.

### Una cota en la dirección correcta es suficiente

La formulación «monótona y acotada» es cómoda, pero la demostración revela una versión más precisa.

Para una sucesión **creciente** solo necesitamos una cota **superior**. Ya existe automáticamente una cota inferior: el primer término satisface

$$
a_{n_0}\le a_n
$$

para todo $n\ge n_0$.

Del mismo modo, para una sucesión **decreciente** solo necesitamos una cota **inferior**, porque

$$
a_n\le a_{n_0}
$$

para todo $n\ge n_0$.

Así, las hipótesis realmente ajustadas son

$$
\boxed{
\begin{aligned}
\text{creciente}+\text{acotada superiormente}
&\Longrightarrow\text{convergente},\\
\text{decreciente}+\text{acotada inferiormente}
&\Longrightarrow\text{convergente}.
\end{aligned}
}
$$

Esta precisión será útil en sucesiones recursivas: no necesitaremos encerrar siempre todos los términos entre dos cotas nuevas; bastará demostrar monotonía y encontrar una barrera en la dirección hacia la que avanzan.

### El teorema demuestra existencia antes de identificar un número sencillo

Consideremos una sucesión creciente y acotada superiormente. El teorema garantiza que

$$
L=\sup\{a_n:n\ge n_0\}
$$

es su límite, incluso si todavía no disponemos de una fórmula elemental para $L$.

Este cambio de perspectiva es importante. Hasta ahora el candidato solía aparecer antes que la prueba de convergencia. A partir de ahora podremos invertir el orden lógico:

$$
\boxed{
\text{primero demostrar que el límite existe}
\quad\longrightarrow\quad
\text{después identificarlo}.
}
$$

En una sucesión recursiva, por ejemplo, la monotonía y una cota podrán darnos existencia mediante el teorema de convergencia monótona. Solo después tendrá sentido utilizar la recurrencia y el álgebra de límites para deducir una ecuación satisfecha por el límite.

Resolver primero esa ecuación y declarar que la sucesión converge sería invertir indebidamente la lógica.

### Monotonía eventual también basta

La convergencia depende de una cola. Por ello, si una sucesión no es monótona desde su primer término pero existe un índice $N_0$ tal que la cola

$$
(a_n)_{n\ge N_0}
$$

es creciente y está acotada superiormente, el teorema de convergencia monótona se aplica a esa cola. La cola converge y, por @prp-t1-0019, la sucesión completa converge al mismo límite.

Análogamente, una cola decreciente y acotada inferiormente basta.

Esta observación evita exigir regularidad innecesaria a una cantidad finita de términos iniciales.

### La herramienta que necesitábamos para las recurrencias

Con §4.7 disponemos por primera vez de un criterio de **existencia de límite** que no requiere conocer de antemano el valor del límite.

El protocolo que emerge es:

$$
\boxed{
\text{demostrar monotonía}
\quad+
\text{encontrar una cota en la dirección correcta}
\quad\Longrightarrow\quad
\text{obtener convergencia por completitud}.
}
$$

En §4.8 aplicaremos exactamente este mecanismo a una sucesión definida recursivamente. Allí habrá que separar cinco preguntas:

1. ¿la recurrencia está bien definida?;
2. ¿qué región permanece invariante?;
3. ¿la sucesión es monótona?;
4. ¿por qué existe un límite?;
5. una vez establecida la existencia, ¿cómo identificamos ese límite sin invocar continuidad?

El cuarto paso será una aplicación directa del @thm-t1-0010. El quinto utilizará el desplazamiento de índices y el álgebra de límites ya demostrados.


## La propiedad arquimediana {#sec-t1-c02-07}

### ¿Pueden los naturales quedar atrapados bajo un número real?

Hasta ahora la completitud ha servido para resolver un problema de existencia: a partir de un conjunto no vacío y acotado hemos obtenido una frontera real y, en §2.6, hemos demostrado que esa frontera produce raíces cuadradas.

La siguiente consecuencia parece, a primera vista, mucho más elemental:

> por grande que sea un número real, siempre existe un número natural mayor.

La afirmación nos resulta familiar desde la aritmética. Si pensamos en $10$, $10^{100}$ o cualquier número concreto, parece evidente que podemos sumar $1$ tantas veces como sea necesario y terminar superándolo. Pero nuestro objetivo no es superar números concretos uno por uno. Debemos demostrar una afirmación universal:

$$
\forall x\in\mathbb R\;\exists n\in\mathbb N\quad n>x.
$$

Y aquí aparece una pregunta estructural que no conviene ocultar:

> ¿los axiomas de cuerpo y orden obligan por sí solos a que los naturales no tengan una cota superior dentro del sistema?

En nuestro desarrollo, la respuesta no se dará por supuesta. La deduciremos de la completitud.

::: {#thm-t1-0003}
**Propiedad arquimediana.** El conjunto $\mathbb N$ no está acotado superiormente en $\mathbb R$. Equivalentemente, para todo $x\in\mathbb R$ existe $n\in\mathbb N$ tal que

$$
n>x.
$$
:::

::: {.callout-note title="Idea de la prueba"}
La afirmación habla de ausencia de cotas. Supongamos lo contrario: que $\mathbb N$ sí está acotado superiormente.

Entonces la completitud nos obligaría a aceptar la existencia de

$$
\alpha=\sup\mathbb N.
$$

Pero, si $\alpha$ es la **menor** cota superior, el número $\alpha-1$ no puede seguir siendo cota superior. De ahí obtendremos un natural muy próximo a $\alpha$ por debajo. Al sumarle $1$, aparecerá un natural estrictamente mayor que $\alpha$, contradiciendo que $\alpha$ fuese cota superior.

La prueba no necesita calcular $\alpha$. De hecho, su fuerza está en demostrar que tal $\alpha$ no puede existir.
:::

**Demostración.** Supongamos, para obtener una contradicción, que $\mathbb N$ está acotado superiormente en $\mathbb R$.

Como $\mathbb N$ es no vacío, el axioma de completitud garantiza que existe

$$
\alpha=\sup\mathbb N.
$$

Por definición, $\alpha$ es una cota superior de $\mathbb N$ y ninguna cota superior puede ser menor que $\alpha$.

Consideremos ahora

$$
\alpha-1<\alpha.
$$

El número $\alpha-1$ **no puede** ser una cota superior de $\mathbb N$, porque entonces tendríamos una cota superior estrictamente menor que el supremo.

Por consiguiente, existe algún $n\in\mathbb N$ tal que

$$
n>\alpha-1.
$$

Sumando $1$ obtenemos

$$
n+1>\alpha.
$$

Pero $n+1\in\mathbb N$. Esto contradice que $\alpha$ sea una cota superior de $\mathbb N$.

La suposición inicial era imposible. Por tanto, $\mathbb N$ no está acotado superiormente en $\mathbb R$. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
Conviene localizar con precisión el papel de cada ingrediente.

- **Completitud:** se utiliza una sola vez, para obtener $\alpha=\sup\mathbb N$ bajo la hipótesis de que $\mathbb N$ estuviera acotado.
- **Propiedad de supremo:** como $\alpha-1<\alpha$, ese número no puede ser otra cota superior.
- **Aritmética de $\mathbb N$:** si $n\in\mathbb N$, entonces $n+1\in\mathbb N$.
- **Contradicción:** aparece un elemento $n+1$ del conjunto que es mayor que una supuesta cota superior.

La prueba es breve, pero no es meramente aritmética: dentro de nuestra arquitectura, la completitud es el paso que impide que $\mathbb N$ quede encerrado bajo una frontera real.
:::

### Dos maneras de leer la misma propiedad

Decir que $\mathbb N$ no está acotado superiormente equivale exactamente a decir

$$
\boxed{
\forall x\in\mathbb R\;\exists n\in\mathbb N\quad n>x.
}
$$

En efecto, si hubiera algún $x\in\mathbb R$ para el cual ningún natural satisficiera $n>x$, entonces todos los naturales verificarían $n\le x$, y $x$ sería una cota superior de $\mathbb N$.

Esta formulación es la que utilizaremos cuando necesitemos elegir un natural **suficientemente grande**.

Por ejemplo, dados $u>0$ y $v\in\mathbb R$, podemos elegir un natural positivo $n$ con

$$
n>\frac{v}{u}
$$

cuando $v>0$, y entonces

$$
nu>v.
$$

Si $v\le0$, cualquier $n\in\mathbb N_{>0}$ ya satisface $nu>v$.

Así obtenemos una forma útil de la misma idea:

$$
\boxed{
\forall u>0\;\forall v\in\mathbb R\;\exists n\in\mathbb N_{>0}
\quad nu>v.
}
$$

No hay un tamaño positivo fijo que, multiplicado por naturales cada vez mayores, permanezca por debajo de todos los reales.

### Naturales grandes, recíprocos pequeños

La forma que aparecerá con mayor frecuencia en análisis es la recíproca.

::: {#cor-t1-0002}
**Recíprocos arbitrariamente pequeños.** Para todo $\varepsilon>0$ existe $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<\varepsilon.
$$
:::

**Demostración.** Sea $\varepsilon>0$. Entonces

$$
\frac1\varepsilon>0.
$$

Por la propiedad arquimediana existe $n\in\mathbb N_{>0}$ tal que

$$
n>\frac1\varepsilon.
$$

Como ambos miembros son positivos, al tomar recíprocos se invierte la desigualdad:

$$
\frac1n<\varepsilon.
$$

Esto prueba el resultado. $\blacksquare$

Esta afirmación merece leerse lentamente. No dice simplemente que algunos recíprocos son pequeños. Dice algo cuantificado mucho más fuerte:

$$
\boxed{
\text{por pequeña que sea la tolerancia positiva }\varepsilon,
\text{ existe un }1/n\text{ todavía menor.}
}
$$

El orden de los cuantificadores es decisivo:

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}.
$$

El natural $n$ **puede depender de** $\varepsilon$. Si exigimos una tolerancia menor, podemos necesitar elegir un natural mayor.

Esta es una de las primeras ocasiones en las que el patrón de cuantificadores de `T1-C01` se convierte en una herramienta cuantitativa del análisis.

::: {.callout-tip title="Lectura de la fórmula"}
Si necesitamos garantizar

$$
\frac1n<10^{-6},
$$

no tenemos que adivinar $n$. Basta imponer

$$
n>10^6.
$$

Por ejemplo, $n=1\,000\,001$ funciona.

La técnica general es:

$$
\boxed{
\frac1n<\varepsilon
\quad\Longleftarrow\quad
n>\frac1\varepsilon.
}
$$
:::

### En $\mathbb R$ no hay infinitésimos positivos

La misma propiedad puede formularse negativamente.

::: {#cor-t1-0003}
**Ausencia de infinitésimos reales positivos.** No existe $\eta\in\mathbb R$ tal que

$$
\eta>0
$$

y simultáneamente

$$
\eta<\frac1n
\qquad
\text{para todo }n\in\mathbb N_{>0}.
$$
:::

**Demostración.** Supongamos que existiera tal $\eta>0$. Aplicando el corolario anterior con $\varepsilon=\eta$, existiría $n\in\mathbb N_{>0}$ tal que

$$
\frac1n<\eta.
$$

Pero la propiedad supuesta de $\eta$ exigiría, para ese mismo $n$,

$$
\eta<\frac1n.
$$

Las dos desigualdades son incompatibles. Por tanto, no existe tal $\eta$. $\blacksquare$

La palabra **infinitésimo** se usa aquí únicamente para describir esta propiedad hipotética: un real positivo menor que todos los números $1/n$. No estamos introduciendo un nuevo tipo de número ni una teoría de infinitesimales.

El mensaje dentro de $\mathbb R$ es preciso:

$$
\boxed{
0\text{ es el único real no negativo que puede quedar por debajo de }1/n
\text{ para todo }n.
}
$$

### La propiedad arquimediana no es lo mismo que la completitud

Como acabamos de deducirla a partir de la completitud, podría surgir una conclusión demasiado fuerte:

> quizá un cuerpo ordenado sea completo exactamente cuando satisface la propiedad arquimediana.

Eso es falso.

El ejemplo ya está delante de nosotros. Como

$$
\mathbb Q\subseteq\mathbb R,
$$

para todo racional $q$ también existe un natural $n>q$. Por tanto, $\mathbb Q$ satisface la propiedad arquimediana.

Sin embargo, en §2.5 demostramos que

$$
S_{\mathbb Q}=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío y acotado superiormente en $\mathbb Q$, pero no posee supremo racional. Luego $\mathbb Q$ no es completo.

Por consiguiente,

$$
\boxed{
\text{completitud}\Longrightarrow\text{propiedad arquimediana},
\qquad
\text{pero no recíprocamente}.}
$$

Esta distinción es importante. La propiedad arquimediana elimina ciertos comportamientos de escala —por ejemplo, un real positivo menor que todos los $1/n$—, pero por sí sola no rellena los huecos de $\mathbb Q$.

### Encajonar un real entre dos enteros consecutivos

Para la siguiente sección necesitaremos transformar la propiedad arquimediana en una herramienta de localización.

::: {#lem-t1-0001}
**Encajonamiento entero.** Para todo $x\in\mathbb R$ existe $m\in\mathbb Z$ tal que

$$
m\le x<m+1.
$$
:::

Antes de la demostración necesitaremos un hecho elemental sobre los naturales que está contenido en el principio de inducción estudiado en `T1-C01`:

> todo subconjunto no vacío de $\mathbb N$ posee un elemento mínimo.

Veamos por qué. Si un conjunto no vacío $A\subseteq\mathbb N$ no tuviera mínimo, entonces $0\notin A$. Supongamos inductivamente que ninguno de $0,1,\dots,k$ pertenece a $A$. Si $k+1\in A$, entonces, como ninguno de los naturales menores que $k+1$ pertenece a $A$, el número $k+1$ sería el mínimo de $A$, contradicción. Así $k+1\notin A$. Por inducción, ningún natural pertenecería a $A$, contradiciendo que $A$ fuese no vacío.

Ahora podemos demostrar el lema.

**Demostración.** Sea $x\in\mathbb R$.

Por la propiedad arquimediana podemos elegir $k\in\mathbb N_{>0}$ tan grande que

$$
k>|x|+1.
$$

En particular,

$$
x+k>0.
$$

Consideremos

$$
A=\{n\in\mathbb N:n>x+k\}.
$$

La propiedad arquimediana garantiza que $A$ es no vacío. Por el hecho de buena ordenación recién justificado, $A$ posee un elemento mínimo; llamémoslo $n_0$.

Como $x+k>0$, necesariamente $n_0\ge1$. Además, por minimalidad de $n_0$,

$$
n_0-1\le x+k<n_0.
$$

Restando $k$ en toda la desigualdad,

$$
n_0-k-1\le x<n_0-k.
$$

Definamos

$$
m=n_0-k-1\in\mathbb Z.
$$

Entonces

$$
m\le x<m+1,
$$

como queríamos demostrar. $\blacksquare$

::: {.callout-note title="Qué hemos construido y qué no"}
El lema garantiza la existencia de un entero $m$ que encajona a $x$ entre dos enteros consecutivos. Más adelante ese entero se describirá mediante la función piso,

$$
\lfloor x\rfloor,
$$

pero no necesitamos introducir ahora esa función como objeto formal.

Lo que sí necesitamos es la **existencia del entero apropiado**, porque será el engranaje que permitirá fabricar un racional entre dos reales cualesquiera.
:::

### Preparación para la densidad

Supongamos que

$$
a<b.
$$

La distancia entre ambos es positiva:

$$
b-a>0.
$$

Por el corolario arquimediano podremos elegir $n\in\mathbb N_{>0}$ de modo que

$$
\frac1n<b-a.
$$

Equivalentemente,

$$
1<n(b-a),
$$

o

$$
na+1<nb.
$$

Por otra parte, el lema de encajonamiento podrá situar $na$ entre dos enteros consecutivos. Esa combinación producirá un entero $m$ con

$$
na<m<nb,
$$

y, al dividir por $n$, un racional $m/n$ estrictamente entre $a$ y $b$.

No ejecutaremos todavía la prueba completa: ese será el comienzo de §2.8. Lo importante ahora es reconocer la maquinaria que ya está disponible:

$$
\boxed{
\text{propiedad arquimediana}
\to
\text{escala }1/n\text{ suficientemente fina}
\to
\text{encajonamiento entero}
\to
\text{densidad racional}.}
$$

### Antes de seguir

::: {.callout-tip title="Antes de seguir"}
**1.** ¿Dónde se utiliza exactamente la completitud en la demostración de la propiedad arquimediana?

**Respuesta.** Bajo la suposición de que $\mathbb N$ estuviera acotado superiormente, la completitud garantiza la existencia de $\alpha=\sup\mathbb N$. El resto del argumento contradice que ese supremo pueda existir.
:::

::: {.callout-tip title="Antes de seguir"}
**2.** ¿Por qué $\alpha-1$ no puede ser una cota superior de $\mathbb N$?

**Respuesta.** Porque sería una cota superior estrictamente menor que $\alpha$, contradiciendo que $\alpha$ es la **menor** cota superior.
:::

::: {.callout-tip title="Antes de seguir"}
**3.** ¿Qué significa realmente

$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}\quad \frac1n<\varepsilon?
$$

**Respuesta.** Que ninguna tolerancia positiva es demasiado pequeña para la familia $1/n$: una vez dada $\varepsilon$, podemos escoger un natural —dependiente de esa tolerancia— cuyo recíproco sea menor.
:::

::: {.callout-tip title="Antes de seguir"}
**4.** ¿La propiedad arquimediana implica completitud?

**Respuesta.** No. $\mathbb Q$ es arquimediano pero no completo, como mostró el conjunto racional asociado a $x^2=2$.
:::

### Lo que exporta esta sección

La propiedad arquimediana nos ha dado tres herramientas distintas:

$$
\boxed{
\begin{array}{c}
\text{naturales arbitrariamente grandes},\\[3pt]
\text{recíprocos }1/n\text{ arbitrariamente pequeños},\\[3pt]
\text{encajonamiento de un real entre enteros consecutivos}.
\end{array}
}
$$

Estas tres formas son equivalentes o estrechamente derivadas, pero cumplen papeles diferentes en las pruebas.

La segunda será recurrente en límites: cuando aparezca una tolerancia positiva, podremos fabricar una escala $1/n$ menor que ella. La tercera será utilizada de inmediato.

En §2.8 veremos que, por pequeños que sean dos extremos reales distintos, siempre cabe entre ellos un número racional y también un número irracional.

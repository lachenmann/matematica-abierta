## Una fórmula no es todavía una función {#sec-t1-c03-01}

### Cuatro veces la misma fórmula

Comencemos con una expresión que no presenta ninguna dificultad algebraica:

$$
x^2.
$$

Consideremos ahora las cuatro asignaciones

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

$$
g\colon[0,\infty)\to[0,\infty),
\qquad
g(x)=x^2,
$$

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2.
$$

A primera vista parece que hemos escrito cuatro nombres para «la misma función». Después de todo, cada vez que introducimos un número permitido, la operación que realizamos es exactamente la misma: elevarlo al cuadrado.

Pero comparemos con más cuidado.

En $f$ podemos introducir números negativos y positivos, mientras que en $g$ y $k$ solo podemos introducir números no negativos. Por tanto, $f(-2)$ tiene sentido, pero $g(-2)$ y $k(-2)$ no están definidos.

También cambia el conjunto en el que declaramos que viven las salidas. En $f$ y $k$ el conjunto de llegada es todo $\mathbb R$. Sin embargo, ningún cuadrado real es negativo. En $g$ y $h$, en cambio, el conjunto de llegada se ha ajustado precisamente a los números no negativos.

Esta diferencia afectará pronto a preguntas como las siguientes:

- ¿pueden dos entradas distintas producir la misma salida?;
- ¿se obtiene realmente cada elemento del conjunto de llegada?;
- ¿podemos recuperar una entrada a partir de una salida?

Por ejemplo, $f(2)=f(-2)=4$, mientras que en $g$ no tenemos la pareja de entradas $2$ y $-2$, porque $-2$ ni siquiera pertenece a su dominio. Y todo número no negativo aparece como cuadrado de algún número no negativo, gracias al teorema de existencia de raíces demostrado en `T1-C02`; por tanto, $g$ alcanza todo su conjunto de llegada.

Con la terminología que formalizaremos en §3.3, el contraste completo será este:

- $f$ no es inyectiva ni sobreyectiva: $2$ y $-2$ producen la misma salida, y ningún real negativo es alcanzado;
- $g$ es biyectiva: entre los números no negativos no aparecen dos entradas distintas con el mismo cuadrado, y todo número no negativo es el cuadrado de su raíz no negativa;
- $h$ es sobreyectiva pero no inyectiva: alcanza todo su codominio $[0,\infty)$, pero, por ejemplo, $h(2)=h(-2)$;
- $k$ es inyectiva pero no sobreyectiva: al restringir las entradas a $[0,\infty)$ desaparece la duplicación producida por $x$ y $-x$, pero siguen sin alcanzarse los números negativos de su codominio $\mathbb R$.

No necesitamos todavía memorizar esas palabras ni sus definiciones. El cuadro sirve para revelar el problema que las hará necesarias: **la fórmula no basta para decidir las propiedades de una función; dominio y codominio importan**.

Todavía no daremos definiciones formales de estas propiedades. Lo haremos en §3.3. Lo importante por ahora es advertir el fenómeno:

$$
\boxed{\text{la misma fórmula puede determinar funciones estructuralmente distintas}.}
$$

::: {#exm-t1-0020}
**Una misma regla, cuatro funciones distintas.** Las funciones $f,g,h,k$ anteriores utilizan la regla $x\mapsto x^2$, pero difieren en dominio o codominio. En particular:

- $f$ admite entradas negativas y declara como codominio todo $\mathbb R$;
- $g$ solo admite entradas no negativas y declara como codominio $[0,\infty)$;
- $h$ admite todas las entradas reales, pero su codominio es $[0,\infty)$;
- $k$ solo admite entradas no negativas, aunque su codominio declarado sea todo $\mathbb R$.

La fórmula aislada $x^2$ no contiene por sí sola toda esta información.
:::

::: {.callout-note title="Antes de seguir"}
Si alguien escribe únicamente

$$
p(x)=\frac1x,
$$

¿conoces ya el dominio de $p$?

No necesariamente. La expresión exige al menos que $x\ne0$, pero podría estar describiendo, por ejemplo,

$$
p\colon\mathbb R\setminus\{0\}\to\mathbb R,
$$

o una restricción como

$$
p\colon(0,\infty)\to(0,\infty).
$$

La fórmula ayuda a determinar qué entradas **son posibles**, pero el dominio matemático de una función es un dato que debe quedar fijado.
:::

### Qué significa realmente $f\colon A\to B$

Ya disponemos del lenguaje de conjuntos y cuantificadores necesario para formalizar la idea.

::: {#def-t1-0019}
**Función, dominio, codominio e imagen.** Sean $A$ y $B$ conjuntos. Una **función**

$$
f\colon A\to B
$$

es una regla de asignación que a **cada** elemento $x\in A$ hace corresponder **exactamente un** elemento $y\in B$. Ese elemento se denota por $f(x)$.

El conjunto $A$ se llama **dominio** de $f$ y $B$ se llama **codominio**.

El conjunto de valores que la función efectivamente toma,

$$
\operatorname{Im}(f)
=
\{f(x):x\in A\},
$$

se llama **imagen** o **recorrido** de $f$. Siempre se cumple

$$
\operatorname{Im}(f)\subseteq B.
$$
:::

Hay dos palabras pequeñas en esta definición que contienen casi todo el concepto:

> **cada** entrada tiene **exactamente una** salida.

La palabra **cada** expresa existencia. Para todo $x\in A$ debe existir una salida permitida $f(x)\in B$.

La expresión **exactamente una** añade unicidad. Una misma entrada no puede recibir dos salidas diferentes.

En el lenguaje lógico de `T1-C01`, la condición puede leerse esquemáticamente como

$$
\forall x\in A\;\exists!y\in B
\quad
\text{tal que $y$ es la salida asignada a $x$}.
$$

La notación $f(x)$ presupone que esa existencia y esa unicidad ya están garantizadas por la regla que define $f$.

Esta reformulación permite diagnosticar dos maneras distintas en que una supuesta definición puede fracasar.

### Primer fallo posible: alguna entrada no tiene salida

Supongamos que declaramos

$$
r\colon\mathbb R\to\mathbb R,
\qquad
r(x)=\frac1x.
$$

La fórmula funciona para todo real distinto de cero, pero en $x=0$ exige dividir por cero. No existe ningún número real que pueda ser $r(0)$ de acuerdo con esa regla.

Por tanto, la declaración anterior **no define una función sobre todo $\mathbb R$**.

Podemos repararla cambiando el dominio:

$$
r\colon\mathbb R\setminus\{0\}\to\mathbb R,
\qquad
r(x)=\frac1x.
$$

Ahora sí existe una salida real para cada entrada permitida.

Este ejemplo enseña una regla de lectura que será permanente:

$$
\boxed{\text{antes de calcular con una fórmula, audita dónde está definida}.}
$$

### Segundo fallo posible: una entrada tiene más de una salida

Consideremos ahora la instrucción

> a cada $x\ge0$, asígnele un número real $y$ que satisfaga $y^2=x$.

Para $x=4$, tanto $y=2$ como $y=-2$ satisfacen la condición. La existencia está garantizada, pero la unicidad falla.

Así formulada, la instrucción **no define una función** de $[0,\infty)$ en $\mathbb R$.

En `T1-C02` demostramos, sin embargo, que para cada $x\ge0$ existe un único número **no negativo** cuyo cuadrado es $x$. Al añadir esa condición obtenemos una función perfectamente definida:

$$
s\colon[0,\infty)\to[0,\infty),
\qquad
s(x)=\sqrt{x}.
$$

La diferencia entre ambas instrucciones es exactamente la diferencia entre

$$
\exists y
$$

y

$$
\exists!y.
$$

No estamos aprendiendo una noción lógica nueva: estamos viendo por qué la lógica de existencia y unicidad era necesaria para definir uno de los objetos centrales del cálculo.

### Lo que **no** exige la definición

Existe un error casi simétrico al anterior. Un principiante puede pensar que, para ser función, entradas diferentes deben producir salidas diferentes.

Eso es falso.

La regla

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

es una función aunque

$$
f(2)=f(-2)=4.
$$

La definición exige **una sola salida para cada entrada**, no **una sola entrada para cada salida**.

La segunda condición es más fuerte y recibirá el nombre de **inyectividad** en §3.3. Conviene mantener separados ambos niveles desde ahora:

$$
\boxed{
\begin{array}{c}
\text{ser función: una entrada no tiene dos salidas;}\\[4pt]
\text{ser inyectiva: dos entradas no comparten una salida.}
\end{array}}
$$

### Dominio, codominio e imagen no son la misma cosa

Volvamos a

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Su dominio es

$$
\mathbb R.
$$

Su codominio declarado también es

$$
\mathbb R.
$$

Pero su imagen es

$$
[0,\infty),
$$

porque todo cuadrado es no negativo y, recíprocamente, todo real no negativo posee una raíz cuadrada real.

Así,

$$
\operatorname{Im}(f)=[0,\infty)\subsetneq\mathbb R.
$$

Esta diferencia es decisiva. El **codominio** pertenece a la declaración de la función. La **imagen** se determina preguntando qué valores del codominio se alcanzan realmente.

En cambio, para

$$
h\colon\mathbb R\to[0,\infty),
\qquad
h(x)=x^2,
$$

tenemos

$$
\operatorname{Im}(h)=[0,\infty),
$$

de modo que imagen y codominio coinciden.

Por eso no podemos tratar el codominio como una ornamentación tipográfica. Cambiarlo puede cambiar afirmaciones matemáticas acerca de la función aunque la regla punto a punto permanezca intacta.

::: {.callout-warning title="Error frecuente"}
No leas automáticamente

$$
f\colon A\to B
$$

como si significara que $f$ toma **todos** los valores de $B$.

La flecha solo declara que las salidas de $f$ pertenecen a $B$. La afirmación adicional

$$
\operatorname{Im}(f)=B
$$

tendrá un nombre propio —sobreyectividad— y deberá demostrarse cuando sea necesaria.
:::

### Una convención sobre la identidad de las funciones

En distintos textos pueden encontrarse convenciones ligeramente diferentes acerca de qué datos se consideran parte de una función. En este libro adoptaremos una convención especialmente útil para el cálculo y para controlar composiciones e inversas:

> en una declaración $f\colon A\to B$, **dominio, codominio y regla de asignación forman parte de los datos de la función**.

Por ello, dos funciones serán iguales cuando coincidan esos datos.

::: {#def-t1-0020}
**Igualdad, restricción y extensión.** Sean

$$
f\colon A\to B,
\qquad
g\colon C\to D.
$$

Diremos que $f=g$ si

$$
A=C,
\qquad
B=D,
$$

y

$$
f(x)=g(x)
\qquad
\text{para todo }x\in A.
$$

Si $E\subseteq A$, la **restricción** de $f$ a $E$ es la función

$$
f|_E\colon E\to B
$$

definida por

$$
f|_E(x)=f(x)
\qquad(x\in E).
$$

Si $A\subseteq C$ y $g\colon C\to B$ satisface

$$
g|_A=f,
$$

diremos que $g$ es una **extensión** de $f$.
:::

La igualdad de funciones es, por tanto, más exigente que la igualdad de dos fórmulas escritas sobre una hoja.

Consideremos

$$
f\colon\mathbb R\to\mathbb R,
\qquad f(x)=x^2,
$$

y

$$
g\colon[0,\infty)\to\mathbb R,
\qquad g(x)=x^2.
$$

En el dominio de $g$ se cumple

$$
f(x)=g(x).
$$

Pero $f\ne g$, porque sus dominios son diferentes. En realidad,

$$
g=f|_{[0,\infty)}.
$$

Así, **restricción** es el nombre preciso para lo que hemos hecho: conservar la regla y permitir menos entradas.

### Restricción: perder entradas puede ganar estructura

Restringir una función no es simplemente «recortar un dibujo». Puede cambiar profundamente sus propiedades.

La función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

produce el mismo valor en $x$ y $-x$. Pero su restricción

$$
f|_{[0,\infty)}\colon[0,\infty)\to\mathbb R
$$

ya no contiene simultáneamente esas dos entradas salvo en $0$.

Más adelante veremos que esta restricción es precisamente lo que permite invertir la operación de elevar al cuadrado sobre los números no negativos.

Este ejemplo anticipa un principio general:

$$
\boxed{\text{cambiar el dominio puede cambiar las propiedades de una función}.}
$$

No cambia los valores que ya estaban definidos en los puntos conservados. Cambia el **objeto funcional** sobre el que formulamos preguntas.

### Extensión: conservar lo conocido y definir más

La operación inversa a restringir es extender.

Por ejemplo, consideremos

$$
u\colon[0,\infty)\to\mathbb R,
\qquad
u(x)=x.
$$

La función identidad sobre $\mathbb R$,

$$
U\colon\mathbb R\to\mathbb R,
\qquad
U(x)=x,
$$

es una extensión de $u$ porque coincide con ella en cada $x\ge0$.

Pero una extensión no tiene por qué ser única. También podemos definir

$$
V(x)=
\begin{cases}
x,&x\ge0,\\
0,&x<0,
\end{cases}
$$

como función $V\colon\mathbb R\to\mathbb R$. Entonces $V$ también extiende a $u$.

Por tanto,

$$
\boxed{\text{conocer una función en un subconjunto no determina, en general, una extensión única}.}
$$

Esta observación será importante mucho más adelante, pero aquí solo necesitamos aprender a distinguir los objetos.

### Una función no necesita una fórmula cerrada

Hasta ahora casi todos nuestros ejemplos han utilizado expresiones algebraicas. Eso puede reforzar accidentalmente la asociación que intentábamos romper.

Una función es una regla de asignación con existencia y unicidad. **La manera de comunicar esa regla puede variar.**

Podemos describir una función mediante una tabla. Por ejemplo, si

$$
A=\{a,b,c,d\},
$$

la tabla

$$
\begin{array}{c|cccc}
x&a&b&c&d\\
\hline
T(x)&2&-1&2&5
\end{array}
$$

define una función

$$
T\colon A\to\mathbb R.
$$

Obsérvese nuevamente que $T(a)=T(c)=2$ no causa ningún problema: cada entrada sigue teniendo una única salida.

También podemos usar una descripción verbal. Por ejemplo,

$$
\ell\colon\{\text{palabras finitas del alfabeto latino}\}\to\mathbb N
$$

puede asignar a cada palabra su número de letras.

O podemos usar un algoritmo.

::: {#exm-t1-0021}
**Una función descrita por un procedimiento.** Para cada $n\in\mathbb N_{>0}$, sea

$$
d(n)=\text{número de divisores positivos de }n.
$$

Esto define una función

$$
d\colon\mathbb N_{>0}\to\mathbb N_{>0}.
$$

Por ejemplo,

$$
d(1)=1,
\qquad
d(6)=4,
\qquad
d(12)=6,
$$

porque

$$
\{m\in\mathbb N_{>0}:m\mid12\}
=
\{1,2,3,4,6,12\}.
$$

Para calcular $d(n)$ podemos emplear un procedimiento: examinar los enteros positivos hasta $n$ y contar cuáles dividen exactamente a $n$. Esa descripción puede ser menos eficiente que una fórmula especializada, pero determina una salida única para cada entrada. Por tanto, determina una función.
:::

La existencia de una función no depende de que poseamos una expresión algebraica breve para ella.

### Fórmula, función y gráfica: tres niveles distintos

Podemos resumir ya la primera distinción del capítulo.

Una **fórmula** es una manera posible de especificar una regla.

Una **función** es el objeto que incluye entradas admitidas, salidas admitidas y una asignación única para cada entrada.

Una **gráfica**, que estudiaremos formalmente en §3.7, será un conjunto de pares

$$
(x,f(x))
$$

que representa geométricamente esa asignación.

Los tres niveles se relacionan, pero no deben confundirse:

$$
\boxed{
\text{fórmula o regla}
\longrightarrow
\text{función completa}
\longrightarrow
\text{representaciones de la función}.
}
$$

Una misma función puede describirse por fórmulas distintas en regiones diferentes. Una misma fórmula puede utilizarse para funciones con dominios distintos. Y una gráfica puede ayudarnos a comprender una función sin sustituir la información precisa de dominio y codominio.

### Cómo leer desde ahora una declaración funcional

Ante una escritura como

$$
f\colon A\to B,
$$

conviene hacer cuatro preguntas antes de manipularla:

1. ¿Cuál es el dominio $A$? Es decir, ¿qué entradas están permitidas?
2. ¿Cuál es el codominio $B$? Es decir, ¿dónde deben vivir las salidas?
3. ¿Cuál es la regla que determina $f(x)$ para cada $x\in A$?
4. ¿Qué conjunto constituye realmente la imagen $\operatorname{Im}(f)$?

La cuarta pregunta puede requerir una demostración. Las tres primeras forman parte de la especificación de la función.

::: {.callout-note title="Antes de seguir"}
Considera

$$
p\colon[-2,2]\to\mathbb R,
\qquad
p(x)=x^2.
$$

- El dominio es $[-2,2]$.
- El codominio es $\mathbb R$.
- La imagen es $[0,4]$.

¿Por qué la imagen no es simplemente $\mathbb R$? Porque el codominio declara **salidas permitidas**, mientras que la imagen registra **salidas realmente alcanzadas**. En este caso $p(x)$ nunca es negativo ni puede superar $4$ cuando $|x|\le2$.
:::

### Qué nos falta todavía

Ya sabemos qué datos constituyen una función y podemos distinguir dominio, codominio e imagen. Pero todavía no disponemos del lenguaje adecuado para responder de manera sistemática preguntas como estas:

- ¿qué conjunto de salidas produce un subconjunto dado del dominio?;
- ¿qué entradas terminan dentro de un subconjunto dado del codominio?;
- ¿cómo se comportan estas operaciones respecto de uniones e intersecciones?

Estas preguntas exigen pasar de la imagen de **un punto** a la imagen y la preimagen de **conjuntos completos**.

Ese será el objeto de §3.2.

## Imágenes y preimágenes {#sec-t1-c03-02}

En la sección anterior distinguimos tres conjuntos asociados a una función

$$
f\colon A\to B:
$$

el dominio $A$, el codominio $B$ y la imagen total $\operatorname{Im}(f)$. Ahora vamos a refinar esa mirada.

Una función no solo envía **puntos** del dominio a puntos del codominio. También nos permite seguir lo que ocurre con **subconjuntos completos**.

Si elegimos una región $E\subseteq A$, podemos preguntar:

> ¿qué valores produce la función cuando solo dejamos entrar elementos de $E$?

Y si elegimos una región $F\subseteq B$, podemos plantear la pregunta inversa:

> ¿qué entradas del dominio terminan dentro de $F$?

Estas dos preguntas conducen a dos operaciones fundamentales: **imagen** y **preimagen**.

La diferencia de dirección conviene verla desde el principio:

$$
\boxed{
\begin{array}{ccc}
E\subseteq A & \xrightarrow{\quad f\quad} & f(E)\subseteq B,\\[6pt]
f^{-1}(F)\subseteq A & \xleftarrow{\quad f\quad} & F\subseteq B.
\end{array}}
$$

La imagen avanza en el sentido de la función. La preimagen retrocede desde un conjunto de posibles salidas hacia las entradas que llegan a él.

### De la imagen de un punto a la imagen de un conjunto

Cuando $x\in A$, ya sabemos qué significa

$$
f(x).
$$

Es un **elemento** de $B$: la salida asignada a la entrada $x$.

Ahora sea $E\subseteq A$. En lugar de introducir una sola entrada, dejamos que $x$ recorra todo $E$. Reunimos entonces todas las salidas obtenidas.

::: {#def-t1-0021}
**Imagen y preimagen de subconjuntos.** Sea

$$
f\colon A\to B
$$

una función.

Si $E\subseteq A$, la **imagen de $E$ bajo $f$** es el subconjunto de $B$

$$
f(E)
=
\{f(x):x\in E\}.
$$

Equivalentemente,

$$
y\in f(E)
\iff
\exists x\in E\text{ tal que }f(x)=y.
$$

Si $F\subseteq B$, la **preimagen** o **imagen inversa de $F$ bajo $f$** es el subconjunto de $A$

$$
f^{-1}(F)
=
\{x\in A:f(x)\in F\}.
$$

Equivalentemente,

$$
x\in f^{-1}(F)
\iff
f(x)\in F.
$$
:::

La definición contiene una asimetría lógica importante.

Para demostrar que un elemento $y$ pertenece a $f(E)$ debemos encontrar **alguna entrada** $x\in E$ que produzca $y$. La pertenencia a una imagen contiene, por tanto, una afirmación existencial:

$$
y\in f(E)
\iff
\exists x\,(x\in E\land f(x)=y).
$$

En cambio, para decidir si $x$ pertenece a $f^{-1}(F)$ no tenemos que buscar ningún testigo adicional. Basta comprobar dónde cae su imagen:

$$
x\in f^{-1}(F)
\iff
f(x)\in F.
$$

Aquí reaparece de forma concreta el entrenamiento lógico de `T1-C01`. Abrir una definición transforma una afirmación sobre conjuntos en una condición sobre elementos y cuantificadores.

### Un punto no es un conjunto

La notación puede parecer casi idéntica, pero debemos distinguir

$$
f(x)
$$

de

$$
f(E).
$$

Si $x\in A$, entonces $f(x)$ es un elemento de $B$.

Si $E\subseteq A$, entonces $f(E)$ es un subconjunto de $B$.

Por ejemplo, si

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

entonces

$$
f(2)=4,
$$

mientras que

$$
f(\{2\})=\{4\}.
$$

La primera salida es un número. La segunda es un conjunto que contiene ese número.

En general,

$$
f(\{x\})=\{f(x)\}.
$$

Esta diferencia tipológica parece pequeña, pero evitará muchos errores cuando empecemos a combinar funciones y operaciones con conjuntos.

### El recorrido es una imagen particular

En §3.1 definimos

$$
\operatorname{Im}(f)
=
\{f(x):x\in A\}.
$$

Con la notación recién introducida podemos escribir simplemente

$$
\boxed{\operatorname{Im}(f)=f(A).}
$$

El recorrido de una función es, por tanto, la imagen de **todo su dominio**.

Esto permite separar dos afirmaciones que se confunden con frecuencia:

$$
f(A)\subseteq B
$$

siempre, porque todas las salidas deben pertenecer al codominio, mientras que

$$
f(A)=B
$$

es una afirmación adicional: dice que no queda ningún elemento del codominio sin alcanzar. En §3.3 daremos nombre y estructura lógica a esa propiedad.

### Seguir un conjunto hacia delante

Volvamos a la función

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Tomemos

$$
E=[-1,2].
$$

Queremos calcular $f(E)$.

No basta con sustituir los extremos y escribir apresuradamente

$$
[f(-1),f(2)]=[1,4].
$$

Eso sería incorrecto, porque $0\in E$ y

$$
f(0)=0.
$$

El conjunto imagen contiene, por tanto, valores menores que $1$.

Para calcularlo correctamente necesitamos resolver dos tareas:

1. demostrar que toda salida producida desde $E$ pertenece a cierto conjunto candidato;
2. demostrar que todo elemento de ese conjunto candidato es realmente producido por alguna entrada de $E$.

Es el mismo patrón de doble inclusión que aprendimos para demostrar igualdad de conjuntos.

Primero, si $x\in[-1,2]$, entonces $|x|\le2$, de modo que

$$
0\le x^2\le4.
$$

Por tanto,

$$
f([-1,2])\subseteq[0,4].
$$

Ahora tomemos un $y\in[0,4]$. Por la existencia de raíces establecida en `T1-C02`, existe $\sqrt y\in[0,2]$. En particular,

$$
\sqrt y\in[-1,2],
$$

y

$$
f(\sqrt y)=(\sqrt y)^2=y.
$$

Así, cada $y\in[0,4]$ pertenece a $f([-1,2])$. Luego

$$
[0,4]\subseteq f([-1,2]).
$$

Concluimos que

$$
\boxed{f([-1,2])=[0,4].}
$$

Este cálculo revela una diferencia importante entre **evaluar una función en puntos** y **determinar la imagen de un conjunto**. La segunda tarea suele ser un problema de conjuntos: debemos caracterizar todas las salidas posibles, no solamente calcular algunos valores.

::: {.callout-warning title="Error frecuente"}
Para una función cualquiera no existe una regla general que permita obtener la imagen de un intervalo evaluando solamente sus extremos.

En este capítulo aprenderemos más adelante qué información adicional —por ejemplo, ciertas propiedades de orden— permite controlar mejor las imágenes de intervalos. Aquí no debemos suponerla de antemano.
:::

### Retroceder desde las salidas: la preimagen

Consideremos de nuevo

$$
f(x)=x^2,
\qquad
f\colon\mathbb R\to\mathbb R,
$$

pero ahora partamos del conjunto de salidas

$$
F=[1,4].
$$

La pregunta ya no es «¿qué valores produce cierto conjunto de entradas?», sino

> ¿qué números reales tienen su cuadrado entre $1$ y $4$?

Por definición,

$$
f^{-1}([1,4])
=
\{x\in\mathbb R:1\le x^2\le4\}.
$$

La condición

$$
1\le x^2\le4
$$

es equivalente a

$$
1\le|x|\le2.
$$

Por tanto,

$$
\boxed{
f^{-1}([1,4])
=
[-2,-1]\cup[1,2].
}
$$

Observa la geometría algebraica del resultado: un solo intervalo situado en el lado no negativo del codominio tiene dos ramas de antecedentes, porque $x$ y $-x$ poseen el mismo cuadrado.

No hemos definido todavía la inyectividad formalmente, pero ya estamos viendo qué aspecto tiene su fracaso: una misma salida puede provenir de más de una entrada.

### Una misma función, imágenes y preimágenes

::: {#exm-t1-0022}
**Imágenes y preimágenes bajo $x\mapsto x^2$.** Sea

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2.
$$

Entonces:

$$
f([-1,2])=[0,4],
$$

$$
f(\{-2,0,3\})=\{0,4,9\},
$$

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2],
$$

$$
f^{-1}(\{4\})=\{-2,2\},
$$

$$
f^{-1}(\{0\})=\{0\},
$$

y

$$
f^{-1}(\{-1\})=\varnothing.
$$

La última igualdad no significa que la preimagen «no exista». La preimagen existe y es un conjunto perfectamente definido; ocurre simplemente que ningún número real tiene cuadrado $-1$.
:::

Este ejemplo reúne tres posibilidades que conviene distinguir:

- una salida puede tener varios antecedentes;
- una salida puede tener exactamente un antecedente;
- una salida puede no tener antecedentes.

En todos los casos, la **preimagen del conjunto** está bien definida.

### Resolver una ecuación como calcular una preimagen

La notación de preimagen permite reinterpretar una tarea algebraica familiar.

Resolver

$$
f(x)=y
$$

para una salida fija $y\in B$ equivale a calcular

$$
f^{-1}(\{y\}).
$$

En efecto,

$$
x\in f^{-1}(\{y\})
\iff
f(x)\in\{y\}
\iff
f(x)=y.
$$

Por ejemplo, para $f(x)=x^2$,

$$
f^{-1}(\{4\})
=
\{x\in\mathbb R:x^2=4\}
=
\{-2,2\}.
$$

Así, la solución de la ecuación $x^2=4$ puede verse como la preimagen del conjunto unitario $\{4\}$.

Pero una preimagen general es más amplia que resolver una sola ecuación. Calcular

$$
f^{-1}([1,4])
$$

significa resolver una **condición de pertenencia**:

$$
f(x)\in[1,4],
$$

es decir,

$$
1\le f(x)\le4.
$$

Para $f(x)=x^2$, eso conduce a una inecuación, no a una ecuación puntual.

Podemos resumir:

$$
\boxed{
\begin{aligned}
f^{-1}(\{y\})&=\text{conjunto de soluciones de }f(x)=y,\\
f^{-1}(F)&=\text{conjunto de soluciones de }f(x)\in F.
\end{aligned}}
$$

### Un ejemplo lineal: la dirección importa

Sea

$$
g\colon\mathbb R\to\mathbb R,
\qquad
g(x)=2x-3.
$$

Calculemos primero la imagen de

$$
E=[0,2].
$$

Si $x\in[0,2]$, entonces

$$
0\le x\le2.
$$

Multiplicando por $2$ y restando $3$ obtenemos

$$
-3\le2x-3\le1.
$$

Por tanto,

$$
g([0,2])\subseteq[-3,1].
$$

Recíprocamente, si $y\in[-3,1]$, definimos

$$
x=\frac{y+3}{2}.
$$

De $-3\le y\le1$ se sigue que $0\le x\le2$, y además

$$
g(x)
=2\left(\frac{y+3}{2}\right)-3
=y.
$$

Luego

$$
\boxed{g([0,2])=[-3,1].}
$$

Ahora calculemos la preimagen de

$$
F=[-1,5].
$$

Por definición,

$$
g^{-1}([-1,5])
=
\{x\in\mathbb R:-1\le2x-3\le5\}.
$$

Sumando $3$ y dividiendo por $2$ obtenemos

$$
1\le x\le4.
$$

Así,

$$
\boxed{g^{-1}([-1,5])=[1,4].}
$$

Los dos cálculos pueden parecer similares porque la función es algebraicamente sencilla, pero responden a preguntas opuestas:

- para hallar $g(E)$, partimos de las **entradas** y caracterizamos sus salidas;
- para hallar $g^{-1}(F)$, partimos de las **salidas permitidas** y caracterizamos las entradas que llegan a ellas.

### La preimagen no exige una función inversa

Aquí aparece una de las advertencias notacionales más importantes del capítulo.

Para

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2,
$$

acabamos de escribir

$$
f^{-1}([1,4]).
$$

Sin embargo, ya vimos en §3.1 que esta función toma el mismo valor en $2$ y $-2$, y tampoco alcanza los reales negativos. Más adelante demostraremos que una función con estas características no posee una función inversa

$$
f^{-1}\colon\mathbb R\to\mathbb R.
$$

No hay contradicción.

La expresión

$$
f^{-1}(F)
$$

que hemos definido en esta sección significa **preimagen del conjunto $F$ bajo $f$**. Está definida para cualquier función $f\colon A\to B$ y cualquier subconjunto $F\subseteq B$.

La expresión

$$
f^{-1}(y)
$$

cuando $f^{-1}$ es una **función inversa** pertenece a otra construcción, que estudiaremos en §3.5 y que solo existe bajo hipótesis adicionales.

::: {.callout-warning title="La notación $f^{-1}$ tiene dos usos"}
No concluyas que existe una función inversa solo porque aparece una expresión como

$$
f^{-1}(F).
$$

La preimagen de conjuntos existe para toda función.

Cuando una verdadera función inversa exista, el contexto indicará qué significado tiene $f^{-1}$. Más adelante veremos además que ambos usos son compatibles en el caso biyectivo.
:::

### Tampoco significa tomar el recíproco

Existe una segunda confusión frecuente. Si $f$ es una función real, la expresión

$$
\frac1f
$$

puede utilizarse, donde tenga sentido, para la función definida por

$$
\left(\frac1f\right)(x)=\frac1{f(x)}.
$$

Esto no tiene relación con la preimagen y tampoco es, en general, una función inversa.

Por ejemplo, si

$$
f(x)=x^2,
$$

entonces

$$
\frac1{f(x)}=\frac1{x^2}
$$

para $x\ne0$.

En cambio,

$$
f^{-1}([1,4])=[-2,-1]\cup[1,2]
$$

es un **conjunto de entradas**.

Son objetos de tipos completamente diferentes.

### Comprobación de tipos

Una manera eficaz de evitar errores es preguntar siempre qué clase de objeto espera cada notación.

Si

$$
f\colon A\to B,
$$

entonces:

- para formar $f(x)$ necesitamos $x\in A$;
- para formar $f(E)$ necesitamos $E\subseteq A$;
- para formar $f^{-1}(F)$ como preimagen necesitamos $F\subseteq B$.

Y los resultados son:

$$
f(x)\in B,
$$

$$
f(E)\subseteq B,
$$

$$
f^{-1}(F)\subseteq A.
$$

Podemos organizarlo así:

$$
\boxed{
\begin{array}{c|c|c}
\text{entrada de la notación}&\text{operación}&\text{resultado}\\
\hline
x\in A&f(x)&\text{elemento de }B\\
E\subseteq A&f(E)&\text{subconjunto de }B\\
F\subseteq B&f^{-1}(F)&\text{subconjunto de }A
\end{array}}
$$

Esta «comprobación de tipos» es especialmente útil cuando dominio y codominio son conjuntos de naturaleza distinta.

### Cuatro pruebas de consistencia

Antes de pasar a ejemplos más elaborados, las definiciones nos proporcionan cuatro controles inmediatos.

Primero,

$$
f(\varnothing)=\varnothing.
$$

No hay entradas en el conjunto vacío, por lo que no puede producirse ninguna salida desde él.

Segundo,

$$
f^{-1}(\varnothing)=\varnothing.
$$

Ninguna entrada puede tener su imagen dentro de un conjunto que no contiene elementos.

Tercero,

$$
f(A)=\operatorname{Im}(f),
$$

como ya observamos.

Cuarto,

$$
\boxed{f^{-1}(B)=A.}
$$

Esta última igualdad merece atención. Toda entrada $x\in A$ satisface

$$
f(x)\in B
$$

por la propia definición de función $f\colon A\to B$. Por tanto, todas las entradas pertenecen a la preimagen del codominio.

No necesitamos que $f$ alcance todos los elementos de $B$. Así, puede ocurrir simultáneamente que

$$
f(A)\ne B
$$

pero

$$
f^{-1}(B)=A.
$$

La primera igualdad fallida habla de qué **salidas se alcanzan**. La segunda, siempre verdadera, habla de dónde están autorizadas a caer las salidas.

### Preimagen de un valor que no se alcanza

Sea otra vez

$$
f(x)=x^2,
\qquad
f\colon\mathbb R\to\mathbb R.
$$

Como $-1$ pertenece al codominio, tiene sentido preguntar por

$$
f^{-1}(\{-1\}).
$$

Pero ningún $x\in\mathbb R$ satisface $x^2=-1$. Por tanto,

$$
f^{-1}(\{-1\})=\varnothing.
$$

Esto muestra por qué debemos distinguir «pertenecer al codominio» de «ser alcanzado por la función».

El codominio determina qué preguntas de preimagen están tipadas correctamente. La imagen total determina cuáles de esas preguntas tienen antecedentes efectivos.

### Un método práctico para calcular imágenes

Cuando una función está dada por una fórmula y queremos calcular $f(E)$, conviene seguir este esquema:

1. **Propón un conjunto candidato** para las salidas posibles.
2. **Primera inclusión:** toma $x\in E$ y demuestra que $f(x)$ pertenece al candidato.
3. **Segunda inclusión:** toma una salida candidata $y$ y construye, si es posible, un $x\in E$ tal que $f(x)=y$.
4. Concluye la igualdad por doble inclusión.

El paso 3 suele ser el más informativo. No basta saber que ningún valor se sale del conjunto candidato; debemos saber también que no hemos incluido valores que la función nunca alcanza desde $E$.

Este método reaparecerá en §3.3 al estudiar sobreyectividad: allí la construcción de un antecedente será precisamente el núcleo de la demostración.

### Un método práctico para calcular preimágenes

Para calcular $f^{-1}(F)$ el procedimiento suele ser más directo:

1. escribe la definición
   $$
   f^{-1}(F)=\{x\in A:f(x)\in F\};
   $$
2. traduce la pertenencia $f(x)\in F$ a ecuaciones, inecuaciones o condiciones conocidas;
3. resuelve esas condiciones dentro del dominio $A$;
4. expresa el conjunto resultante de forma conveniente.

Por ejemplo, si

$$
f(x)=x^2
$$

y

$$
F=(1,4],
$$

entonces

$$
x\in f^{-1}((1,4])
\iff
1<x^2\le4
\iff
1<|x|\le2.
$$

Luego

$$
\boxed{
f^{-1}((1,4])
=[-2,-1)\cup(1,2].
}
$$

Nótese que no hemos «invertido la fórmula $x^2$». Hemos traducido una condición de pertenencia y la hemos resuelto.

### Mirar hacia §3.3 sin adelantarla

La imagen y la preimagen ya nos permiten formular con precisión las dos preguntas que motivaron la apertura del capítulo.

Para

$$
f\colon A\to B,
$$

podemos preguntar:

1. ¿cada $y\in B$ pertenece a $f(A)$?
2. para cada $y\in B$, ¿el conjunto $f^{-1}(\{y\})$ contiene como máximo un elemento?

La primera pregunta trata de si se alcanza todo el codominio. La segunda trata de si una salida puede provenir de dos entradas distintas.

En §3.3 convertiremos esas preguntas en las definiciones formales de **sobreyectividad** e **inyectividad**.

Por ahora basta conservar el mapa conceptual:

$$
\boxed{
\begin{array}{c}
\text{imagen: qué salidas produce un conjunto de entradas;}\\[4pt]
\text{preimagen: qué entradas terminan en un conjunto de salidas.}
\end{array}}
$$

Y queda pendiente una cuestión más sutil. Si combinamos subconjuntos mediante uniones, intersecciones o complementos, ¿cómo se comportan sus imágenes y preimágenes? Algunas igualdades funcionan siempre; otras requieren hipótesis adicionales.

No responderemos todavía esa pregunta. La reservamos para §3.6, donde servirá como laboratorio de demostración, contraejemplo y diagnóstico de hipótesis.

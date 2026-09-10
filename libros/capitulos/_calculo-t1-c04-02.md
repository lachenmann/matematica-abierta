## Tan cerca como queramos, desde algún momento: la definición $\varepsilon$–$N$ {#sec-t1-c04-02}

En §4.1 aprendimos a reconocer la parte temporal de una afirmación sobre el comportamiento final de una sucesión:

$$
\exists N\;\forall n\ge N.
$$

Quedó pendiente decidir qué propiedad deben satisfacer todos esos términos tardíos si queremos expresar que una sucesión «se acerca» a un número $L$.

La palabra **cerca** todavía es demasiado imprecisa. Dos números pueden parecernos cercanos en una escala y muy alejados en otra. Si estamos aproximando una longitud de varios kilómetros, un error de un metro puede ser pequeño; si estamos midiendo el grosor de una célula, el mismo error sería enorme. Una definición matemática no puede depender de esa apreciación contextual.

Necesitamos sustituir «cerca» por una condición numérica que podamos hacer tan exigente como queramos.

### De la cercanía a una tolerancia

Sean $a_n$ un término de la sucesión y $L\in\mathbb R$ un número que queremos considerar como posible límite. La distancia entre ambos es

$$
|a_n-L|.
$$

Si elegimos una tolerancia $\varepsilon>0$, la condición

$$
|a_n-L|<\varepsilon
$$

significa que $a_n$ está a distancia menor que $\varepsilon$ de $L$.

Por las equivalencias de valor absoluto estudiadas en `T1-C02`, esto es lo mismo que

$$
L-\varepsilon<a_n<L+\varepsilon.
$$

Así, exigir

$$
|a_n-L|<\varepsilon
$$

significa pedir que el término $a_n$ pertenezca al intervalo abierto

$$
(L-\varepsilon,L+\varepsilon).
$$

Si $\varepsilon=1$, permitimos una franja bastante amplia alrededor de $L$. Si $\varepsilon=10^{-3}$, exigimos mucha más precisión. Si $\varepsilon=10^{-20}$, la exigencia es todavía más estricta.

Pero ninguna tolerancia positiva particular puede definir por sí sola el límite. Una sucesión podría terminar entrando en el intervalo de radio $1$ alrededor de $L$ y, sin embargo, permanecer siempre a distancia mayor que $10^{-3}$ de $L$.

Por eso la idea de límite no es

> los términos terminan estando cerca de $L$ con alguna precisión fija,

sino

> **cualquiera que sea la precisión positiva que exijamos**, llega un momento a partir del cual todos los términos satisfacen esa precisión.

La expresión «tan cerca como queramos» se convierte así en

$$
\forall\varepsilon>0.
$$

Y la expresión «desde algún momento y para siempre después» ya fue preparada en §4.1:

$$
\exists N\;\forall n\ge N.
$$

Al unir ambas estructuras aparece la definición fundamental.

::: {#def-t1-0028}
**Convergencia, límite y divergencia.** Sea

$$
(a_n)_{n\ge n_0}
$$

una sucesión real y sea $L\in\mathbb R$.

Diremos que $(a_n)$ **converge a $L$** si para todo $\varepsilon>0$ existe un índice $N\ge n_0$ tal que

$$
|a_n-L|<\varepsilon
$$

para todo $n\ge N$.

En símbolos,

$$
\forall\varepsilon>0\;\exists N\ge n_0\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

En ese caso escribimos

$$
a_n\to L,
$$

$$
\lim_{n\to\infty}a_n=L,
$$

o, cuando no haya ambigüedad,

$$
(a_n)\to L.
$$

El número $L$ se llama **límite** de la sucesión.

Diremos que $(a_n)$ **diverge** si no existe ningún número real $L$ al cual converja.
:::

La notación

$$
n\to\infty
$$

no significa que $n$ llegue a tomar como valor un objeto llamado $\infty$. El símbolo expresa que estamos estudiando índices arbitrariamente grandes, es decir, colas cada vez más alejadas del comienzo de la sucesión.

### Leer la definición de izquierda a derecha

La definición contiene tres cuantificadores encadenados:

$$
\boxed{
\forall\varepsilon>0
\quad
\exists N\ge n_0
\quad
\forall n\ge N.
}
$$

Su orden es parte esencial del significado.

Podemos leerla como un juego de responsabilidades.

1. **La exigencia:** se nos entrega una tolerancia arbitraria $\varepsilon>0$.
2. **Nuestra respuesta:** debemos encontrar un umbral $N$ que funcione para esa tolerancia.
3. **La verificación:** una vez elegido $N$, cualquier índice $n\ge N$ debe satisfacer
   $$
   |a_n-L|<\varepsilon.
   $$

El primer cuantificador es universal. No podemos elegir una tolerancia cómoda y detenernos allí. La afirmación debe funcionar para

$$
\varepsilon=1,
\qquad
\varepsilon=10^{-2},
\qquad
\varepsilon=10^{-100},
$$

y para cualquier otro real positivo.

El segundo cuantificador es existencial. No necesitamos encontrar el menor $N$ posible. Basta producir **algún** umbral que funcione.

El tercer cuantificador vuelve a ser universal. Después de $N$ no basta con encontrar muchos términos buenos: deben ser buenos **todos** los términos de la cola.

Esta última condición es precisamente la noción de eventualidad de §4.1. Para cada tolerancia $\varepsilon>0$, la propiedad

$$
|a_n-L|<\varepsilon
$$

debe cumplirse eventualmente.

Por eso podemos resumir la definición diciendo:

$$
\boxed{
 a_n\to L
 \quad\Longleftrightarrow\quad
 \text{para toda tolerancia positiva, la sucesión está eventualmente dentro de esa tolerancia alrededor de $L$.}
}
$$

### El umbral puede depender de la tolerancia

Una de las primeras dificultades lógicas consiste en entender la dependencia entre $\varepsilon$ y $N$.

La definición permite que

$$
N=N(\varepsilon).
$$

Una tolerancia amplia puede admitir un umbral pequeño; una tolerancia más estricta puede obligarnos a avanzar mucho más.

Por ejemplo, para

$$
a_n=\frac1{n+1}
$$

y candidato $L=0$, la condición

$$
|a_n-0|<\frac1{10}
$$

se cumple desde $n=10$.

En cambio,

$$
|a_n-0|<\frac1{10^6}
$$

requiere un umbral mucho más lejano.

No hay ningún problema en que los dos valores de $N$ sean distintos. La definición no exige un único $N$ capaz de responder simultáneamente a todas las tolerancias.

De hecho, si exigiéramos

$$
\exists N\;\forall\varepsilon>0\;\forall n\ge N:
|a_n-L|<\varepsilon,
$$

estaríamos diciendo algo mucho más fuerte. Para un $n\ge N$ fijo, el número $|a_n-L|$ tendría que ser menor que **todo** real positivo. Eso solo es posible si

$$
|a_n-L|=0,
$$

es decir,

$$
a_n=L.
$$

Por tanto, ese orden incorrecto de cuantificadores describiría sucesiones que a partir de cierto índice son exactamente constantes iguales a $L$. La convergencia es mucho más flexible: permite que los términos nunca lleguen a ser exactamente $L$, siempre que podamos hacer su distancia a $L$ arbitrariamente pequeña en una cola adecuada.

### Cómo se construye una prueba $\varepsilon$–$N$

La primera vez que vemos una prueba de convergencia puede parecer que el valor de $N$ aparece por inspiración. En realidad, conviene separar dos momentos.

**Búsqueda.** Partimos de la desigualdad que queremos conseguir,

$$
|a_n-L|<\varepsilon,
$$

y la manipulamos para descubrir qué condición sobre $n$ bastaría para garantizarla.

**Demostración.** Después escribimos el argumento en el orden lógico de la definición:

1. sea $\varepsilon>0$ arbitrario;
2. elegimos un $N$ que satisfaga la condición descubierta;
3. tomamos cualquier $n\ge N$;
4. verificamos que $|a_n-L|<\varepsilon$.

El cálculo exploratorio puede ir «hacia atrás»; la prueba final debe ir «hacia adelante».

::: {#exm-t1-0032}
**Primera prueba completa: $1/(n+1)\to0$.** Consideremos

$$
a_n=\frac1{n+1},
\qquad n\ge0.
$$

Queremos demostrar directamente desde la definición que

$$
\lim_{n\to\infty}\frac1{n+1}=0.
$$

**Búsqueda del umbral.** Necesitamos lograr

$$
\left|\frac1{n+1}-0\right|<\varepsilon.
$$

Como $n+1>0$, esto equivale a pedir

$$
\frac1{n+1}<\varepsilon,
$$

y sería suficiente garantizar

$$
n+1>\frac1\varepsilon.
$$

La propiedad arquimediana demostrada en `T1-C02` asegura que existe un número natural $N$ tal que

$$
N>\frac1\varepsilon.
$$

Ese $N$ será una respuesta válida.

**Demostración.** Sea $\varepsilon>0$. Por la propiedad arquimediana, elegimos $N\in\mathbb N$ tal que

$$
N>\frac1\varepsilon.
$$

Si $n\ge N$, entonces

$$
n+1\ge N+1>N>\frac1\varepsilon.
$$

Como todas estas cantidades son positivas, al tomar recíprocos se invierte la desigualdad y obtenemos

$$
\frac1{n+1}<\varepsilon.
$$

Por tanto,

$$
\left|\frac1{n+1}-0\right|<\varepsilon
$$

para todo $n\ge N$. Como $\varepsilon>0$ era arbitrario, concluimos que

$$
\frac1{n+1}\to0.
$$
:::

Vale la pena leer la prueba señalando dónde aparece cada cuantificador:

- **para todo** $\varepsilon>0$: comenzamos con una tolerancia arbitraria;
- **existe** $N$: la propiedad arquimediana nos permite construir una respuesta;
- **para todo** $n\ge N$: la última cadena de desigualdades funciona para cualquier término de la cola.

El argumento no demuestra que algunos términos estén cerca de cero. Demuestra que, dada cualquier precisión positiva, existe una cola completa dentro de esa precisión.

### Un mismo umbral no tiene que ser óptimo

En el ejemplo anterior elegimos $N$ satisfaciendo

$$
N>\frac1\varepsilon.
$$

Esta elección es deliberadamente cómoda y puede estar lejos de ser mínima.

La definición de convergencia no pregunta

> ¿cuál es el primer índice exacto a partir del cual funciona la desigualdad?,

sino

> ¿existe algún índice a partir del cual funciona para todos los términos posteriores?

Esta diferencia libera muchas pruebas de cálculos innecesarios. Un $N$ más grande de lo imprescindible sigue siendo perfectamente válido.

### Estar cerca muchas veces no es converger

La sucesión

$$
a_n=(-1)^n
$$

toma los valores

$$
1,-1,1,-1,1,-1,\dots
$$

Si proponemos $L=1$, hay infinitos términos que están exactamente en $1$: todos los índices pares satisfacen

$$
a_n=1.
$$

Sin embargo, eso no implica convergencia a $1$. Después de cualquier índice vuelven a aparecer términos iguales a $-1$.

La definición no pide

> para toda tolerancia existen términos arbitrariamente tardíos que están cerca de $L$,

sino

> para toda tolerancia existe un momento después del cual **todos** los términos están cerca de $L$.

En símbolos, no debemos confundir

$$
\forall N\;\exists n\ge N
$$

con

$$
\exists N\;\forall n\ge N.
$$

La primera estructura expresa que algo vuelve a ocurrir por lejos que avancemos. La segunda expresa que, desde cierto punto, algo ocurre sin excepciones. Para la convergencia necesitamos la segunda.

### Negar correctamente que $a_n\to L$

La definición de convergencia a un candidato $L$ es

$$
\forall\varepsilon>0\;\exists N\ge n_0\;\forall n\ge N:
|a_n-L|<\varepsilon.
$$

Para negarla debemos invertir los cuantificadores y negar la desigualdad final. Obtenemos:

$$
\boxed{
 a_n\not\to L
 \quad\Longleftrightarrow\quad
 \exists\varepsilon_0>0\;\forall N\ge n_0\;\exists n\ge N:
 |a_n-L|\ge\varepsilon_0.
}
$$

Esta fórmula merece una lectura pausada.

Para demostrar que $L$ **no** es el límite, no tenemos que fracasar ante todas las tolerancias. Basta encontrar **una** tolerancia positiva $\varepsilon_0$ que la sucesión sea incapaz de satisfacer eventualmente.

Una vez fijada esa tolerancia, debemos demostrar que ningún umbral funciona: por lejos que alguien coloque $N$, todavía podemos encontrar algún término posterior que queda a distancia al menos $\varepsilon_0$ de $L$.

La negación tiene así la forma de un obstáculo persistente:

$$
\boxed{
\text{existe una precisión fija que la sucesión vuelve a violar arbitrariamente lejos.}
}
$$

### Refutar un candidato no basta para demostrar divergencia

Hay que distinguir dos afirmaciones:

$$
a_n\not\to L
$$

y

$$
(a_n)\text{ diverge}.
$$

La primera excluye **un** candidato concreto. La segunda afirma que **ningún** real sirve como límite.

Por ejemplo,

$$
\frac1{n+1}\not\to1,
$$

pero eso no vuelve divergente a la sucesión: acabamos de demostrar que converge a $0$.

Como divergencia significa ausencia de todo límite real, su forma lógica completa es

$$
\forall L\in\mathbb R\;\exists\varepsilon_0>0\;\forall N\ge n_0\;\exists n\ge N:
|a_n-L|\ge\varepsilon_0.
$$

En muchas situaciones posteriores dispondremos de criterios más económicos para demostrar divergencia. Por ahora podemos hacerlo directamente desde esta negación.

::: {#exm-t1-0033}
**Divergencia de $(-1)^n$ desde la definición.** Sea

$$
a_n=(-1)^n.
$$

Demostraremos que la sucesión no converge a ningún número real.

Sea $L\in\mathbb R$ un candidato arbitrario. Los dos posibles valores de la sucesión son $1$ y $-1$. Por la desigualdad triangular,

$$
2
=|1-(-1)|
\le |1-L|+|L-(-1)|
=|1-L|+|-1-L|.
$$

Por tanto, al menos uno de los dos números

$$
|1-L|,
\qquad
|-1-L|
$$

es mayor o igual que $1$.

Tomemos

$$
\varepsilon_0=1.
$$

Ahora sea $N\in\mathbb N$ cualquier umbral.

- Si $|1-L|\ge1$, elegimos un índice par $n\ge N$, por ejemplo $n=2N$. Entonces $a_n=1$ y
  $$
  |a_n-L|=|1-L|\ge1=\varepsilon_0.
  $$
- Si $|-1-L|\ge1$, elegimos un índice impar $n\ge N$, por ejemplo $n=2N+1$. Entonces $a_n=-1$ y
  $$
  |a_n-L|=|-1-L|\ge1=\varepsilon_0.
  $$

En cualquiera de los dos casos, para todo $N$ encontramos un $n\ge N$ tal que

$$
|a_n-L|\ge\varepsilon_0.
$$

Así, $a_n\not\to L$.

Como $L\in\mathbb R$ era arbitrario, ningún real puede ser límite de la sucesión. Por consiguiente,

$$
((-1)^n)\text{ diverge}.
$$
:::

Observe qué hizo posible la prueba: no necesitamos adivinar cuál sería el «verdadero» candidato. Elegimos un $L$ completamente arbitrario y demostramos que la oscilación entre $1$ y $-1$ impide que toda una cola quede dentro de una tolerancia suficientemente estrecha alrededor de ese $L$.

### Una definición que ya contiene un método de trabajo

La definición $\varepsilon$–$N$ no es solamente una frase que debamos memorizar. También prescribe la arquitectura de las primeras demostraciones.

Para **probar convergencia hacia un candidato $L$**:

$$
\boxed{
\varepsilon>0
\longrightarrow
\text{buscar una condición suficiente sobre }n
\longrightarrow
\text{elegir }N(\varepsilon)
\longrightarrow
\forall n\ge N:\ |a_n-L|<\varepsilon.
}
$$

Para **refutar que $L$ sea límite**:

$$
\boxed{
\text{elegir }\varepsilon_0>0
\longrightarrow
\forall N
\longrightarrow
\text{encontrar }n\ge N
\text{ con }
|a_n-L|\ge\varepsilon_0.
}
$$

Estas dos arquitecturas son lógicamente opuestas. Aprender a reconocerlas será tan importante como aprender a calcular límites.

En esta sección hemos definido qué significa converger, pero todavía no hemos estudiado qué consecuencias tiene hacerlo. Por ejemplo:

- ¿podría una misma sucesión converger a dos números distintos?;
- ¿puede una sucesión convergente escapar arbitrariamente lejos de todos los números?;
- ¿qué ocurre si modificamos una cantidad finita de términos de una sucesión convergente?

Las respuestas pertenecen a §4.3. Allí comenzaremos a demostrar los primeros teoremas generales que se desprenden únicamente de la definición que acabamos de construir.


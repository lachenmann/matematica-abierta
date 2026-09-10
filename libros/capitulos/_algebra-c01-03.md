## §3. Términos, expresiones y fórmulas

En las dos secciones anteriores hemos dado dos pasos. Primero aprendimos que una expresión tiene estructura; después introdujimos letras y vimos que su papel depende del contexto. Ahora necesitamos un vocabulario mínimo para describir expresiones como

$$
x+3,
$$

$$
2x^2-5x+1,
$$

$$
\frac{a+b}{c},
$$

o

$$
3(a+b)^2.
$$

La palabra «mínimo» es importante. No queremos aprender una lista de nombres como si el álgebra fuera una clasificación gramatical. Queremos palabras que nos ayuden a **leer la estructura**.

::: {.ma-block .ma-intuicion}
**Idea clave**

El vocabulario algebraico sirve para indicar **cómo está construida una expresión**.
:::

---

### 3.1 Sumas y términos

Consideremos:

$$
x+3.
$$

La operación principal es una suma. Las dos partes que esa suma reúne son

$$
x
$$

y

$$
3.
$$

En este contexto podemos llamar a esas partes **términos** de la suma.

Así, en

$$
a+b+c,
$$

podemos reconocer tres términos:

$$
a,
\qquad
b,
\qquad
c.
$$

La idea importante es que «término» no designa simplemente cualquier fragmento que veamos escrito. Describe una parte de una expresión cuando estamos mirando una **estructura aditiva**.

Consideremos ahora:

$$
2x+5.
$$

La expresión completa es una suma. Sus dos términos son

$$
2x
$$

y

$$
5.
$$

El primer término, a su vez, tiene estructura multiplicativa. Por tanto, una misma parte de una expresión puede describirse de maneras diferentes según el nivel que estemos observando.

En

$$
2x+5,
$$

la subexpresión

$$
2x
$$

es un **término** respecto de la suma exterior y un **producto** cuando la examinamos internamente.

Esta manera de hablar evita una dificultad frecuente: creer que cada símbolo debe recibir una sola etiqueta absoluta.

---

### 3.2 Productos y factores

Consideremos ahora:

$$
3x.
$$

Como vimos en la sección anterior, esta escritura significa

$$
3\cdot x.
$$

Las partes multiplicadas son

$$
3
$$

y

$$
x.
$$

Las llamamos **factores** del producto.

Así, en

$$
2ab,
$$

podemos leer

$$
2\cdot a\cdot b.
$$

Los factores son

$$
2,
\qquad
a,
\qquad
b.
$$

Pero volvamos a

$$
2x+5.
$$

Aquí debemos distinguir dos niveles. La expresión completa es una suma:

$$
\boxed{2x}+5.
$$

Por ello, $2x$ es uno de sus términos. Dentro de ese término encontramos un producto:

$$
2\cdot x.
$$

Por ello, $2$ y $x$ son factores de ese producto.

Podemos resumir la lectura así:

```text
suma
├── término: 2x
│   └── producto
│       ├── factor: 2
│       └── factor: x
└── término: 5
```

No pretendemos que este diagrama sea una definición formal. Es una ayuda para aprender a leer por niveles.

---

### 3.3 Restas y signos

Consideremos:

$$
2x-5.
$$

A primera vista podemos decir que aparecen una multiplicación y una resta. Eso es correcto. Pero en el lenguaje algebraico es frecuente tratar expresiones como

$$
2x-5
$$

como sumas de términos con signo:

$$
2x+(-5).
$$

Así podemos hablar de dos términos:

$$
2x
\qquad\text{y}\qquad
-5.
$$

No desarrollaremos todavía una teoría completa de suma de términos ni de números con signo; por ahora basta observar que el signo menos puede formar parte del término que sigue cuando la expresión se interpreta aditivamente.

Por ejemplo, en

$$
2x^2-5x+1,
$$

podemos reconocer los términos

$$
2x^2,
\qquad
-5x,
\qquad
1.
$$

Esta lectura será especialmente útil más adelante, cuando estudiemos polinomios.

::: {.ma-block .ma-error}
**Atención**

No debemos confundir el signo menos que pertenece a un término con una instrucción informal de «cambiar el signo» o «mover algo al otro lado». Las transformaciones de ecuaciones se estudiarán más adelante con precisión.
:::

---

### 3.4 Potencias: base y exponente

Consideremos:

$$
x^2.
$$

Esta expresión representa una potencia. La **base** es

$$
x,
$$

y el **exponente** es

$$
2.
$$

En

$$
(a+b)^3,
$$

la base completa es

$$
a+b,
$$

y el exponente es

$$
3.
$$

La estructura es:

```text
potencia
├── base: a+b
└── exponente: 3
```

Los paréntesis indican que toda la suma

$$
a+b
$$

actúa como base.

Comparemos:

$$
a+b^2
$$

con

$$
(a+b)^2.
$$

En la primera, solo $b$ está elevado al cuadrado. En la segunda, toda la suma está elevada al cuadrado.

---

### 3.5 Cocientes: numerador y denominador

Consideremos:

$$
\frac{a+b}{c}.
$$

La expresión completa es un cociente. Su numerador es

$$
a+b,
$$

y su denominador es

$$
c.
$$

Dentro del numerador hay una suma.

Podemos leer entonces:

```text
cociente
├── numerador: a+b
│   └── suma
│       ├── a
│       └── b
└── denominador: c
```

Comparemos ahora

$$
\frac{a+b}{c}
$$

con

$$
a+\frac{b}{c}.
$$

En la primera expresión, la operación principal es la división. En la segunda, la operación principal es la suma.

La barra de fracción cumple un papel semejante al de unos paréntesis extensos: agrupa todo el numerador y todo el denominador.

---

### 3.6 Leer una expresión por capas

Consideremos ahora una expresión más larga:

$$
\frac{2x-(a+b)^2}{3c}.
$$

No intentemos hacer nada con ella. Solo queremos leerla.

#### Primera capa

La expresión completa es un cociente:

$$
\frac{\boxed{2x-(a+b)^2}}{\boxed{3c}}.
$$

#### Segunda capa: numerador

El numerador es

$$
2x-(a+b)^2.
$$

Podemos leerlo aditivamente como dos términos:

$$
2x
\qquad\text{y}\qquad
-(a+b)^2.
$$

#### Tercera capa: primer término

En

$$
2x,
$$

hay un producto con factores

$$
2
\qquad\text{y}\qquad
x.
$$

#### Tercera capa: segundo término

En

$$
(a+b)^2,
$$

hay una potencia. La base es

$$
a+b,
$$

y el exponente es

$$
2.
$$

Dentro de la base aparece una suma con términos

$$
a
\qquad\text{y}\qquad
b.
$$

#### Segunda capa: denominador

El denominador es

$$
3c,
$$

un producto con factores

$$
3
\qquad\text{y}\qquad
c.
$$

Una expresión que inicialmente parecía complicada se vuelve mucho más legible cuando la recorremos por niveles.

El método es el mismo que aprendimos en §1:

$$
\boxed{
\text{primero la estructura exterior; después las partes interiores}.
}
$$

---

### 3.7 Una expresión representa; una igualdad afirma

Ahora comparemos:

$$
x+3
$$

con

$$
x+3=7.
$$

La primera escritura es una expresión. Representa un valor que dependerá de cómo se interprete $x$. Pero no afirma, por sí sola, que ese valor sea uno u otro.

La segunda escritura contiene una igualdad:

$$
x+3=7.
$$

Aquí ya no estamos simplemente representando un valor. Estamos **afirmando** que dos expresiones representan lo mismo:

$$
x+3
$$

y

$$
7.
$$

Todavía no introduciremos el término formal «proposición». Tampoco estudiaremos cuándo una afirmación es verdadera o falsa en sentido lógico.

Por ahora basta distinguir:

$$
\boxed{
\text{expresión}
\quad\text{frente a}\quad
\text{escritura que afirma una igualdad}.
}
$$

Esta diferencia será decisiva en las secciones siguientes.

---

### 3.8 ¿Qué llamaremos fórmula?

La palabra **fórmula** se usa en matemáticas de varias maneras.

Por ejemplo, solemos hablar de

$$
A=\pi r^2
$$

como «la fórmula del área de un círculo».

También podemos hablar de una fórmula como

$$
a(b+c)=ab+ac
$$

para expresar una relación general.

No intentaremos convertir «fórmula» en una categoría formal rígida en este capítulo.

La usaremos como una palabra funcional para una escritura matemática que expresa de manera compacta una regla, relación o patrón.

::: {.ma-block .ma-observacion}
**Observación**

Más adelante, en lógica matemática, la palabra «fórmula» puede adquirir un significado técnico más preciso. Cuando lleguemos allí distinguiremos cuidadosamente ese uso formal del uso corriente que hacemos ahora.
:::

---

### 3.9 Ejemplo guiado: leer sin simplificar

Consideremos:

$$
4a^2+\frac{b+1}{3}.
$$

La operación principal es la suma. Sus dos términos son

$$
4a^2
$$

y

$$
\frac{b+1}{3}.
$$

En el primer término,

$$
4a^2,
$$

podemos reconocer un producto entre

$$
4
$$

y

$$
a^2.
$$

La subexpresión

$$
a^2
$$

es una potencia de base $a$ y exponente $2$.

En el segundo término,

$$
\frac{b+1}{3},
$$

tenemos un cociente. El numerador es

$$
b+1,
$$

una suma de dos términos, y el denominador es

$$
3.
$$

No hemos calculado ni simplificado nada. Y, sin embargo, ahora comprendemos mucho mejor la escritura.

::: {.ma-block .ma-intuicion}
**Idea clave**

Nombrar partes de una expresión es útil solo si nos permite ver su organización.
:::

---

## Ejercicios

### Términos y factores {#apm-i-e0011}

En cada expresión, identifica los términos de la suma exterior. Después, cuando corresponda, identifica los factores de cada término.

#### a)

$$
3x+5
$$

#### b)

$$
2ab+7
$$

#### c)

$$
4x^2-3x+1
$$

#### Solución

#### a)

La suma exterior tiene dos términos:

$$
3x
\qquad\text{y}\qquad
5.
$$

Dentro de $3x$ hay un producto con factores

$$
3
\qquad\text{y}\qquad
x.
$$

#### b)

La expresión tiene dos términos:

$$
2ab
\qquad\text{y}\qquad
7.
$$

El primero puede leerse como

$$
2\cdot a\cdot b,
$$

de modo que sus factores son

$$
2,
\qquad
a,
\qquad
b.
$$

#### c)

Leída aditivamente, la expresión tiene los términos

$$
4x^2,
\qquad
-3x,
\qquad
1.
$$

En el primer término reconocemos los factores

$$
4
\qquad\text{y}\qquad
x^2.
$$

En el segundo, los factores son

$$
-3
\qquad\text{y}\qquad
x.
$$

---

### Bases y exponentes {#apm-i-e0012}

Identifica la base y el exponente de cada potencia.

#### a)

$$
x^5
$$

#### b)

$$
(a+b)^3
$$

#### c)

$$
(2x+1)^4
$$

#### Solución

#### a)

En

$$
x^5,
$$

la base es $x$ y el exponente es $5$.

#### b)

En

$$
(a+b)^3,
$$

la base completa es

$$
a+b,
$$

y el exponente es $3$.

Los paréntesis muestran que toda la suma es la base.

#### c)

En

$$
(2x+1)^4,
$$

la base es

$$
2x+1,
$$

y el exponente es $4$.

---

### Numerador, denominador y estructura {#apm-i-e0013}

Considera:

$$
\frac{x+2}{3y}.
$$

1. ¿Cuál es la operación principal?
2. ¿Cuál es el numerador?
3. ¿Cuál es el denominador?
4. ¿Qué estructura tiene el numerador?
5. ¿Qué estructura tiene el denominador?

#### Solución

La expresión completa es un cociente. Por tanto, la operación principal es la división.

El numerador es

$$
x+2.
$$

Tiene estructura de suma, con términos

$$
x
\qquad\text{y}\qquad
2.
$$

El denominador es

$$
3y.
$$

Tiene estructura de producto, con factores

$$
3
\qquad\text{y}\qquad
y.
$$

---

### Expresión o afirmación {#apm-i-e0014}

Indica cuáles de las siguientes escrituras son solo expresiones y cuáles afirman una igualdad.

1. $x+4$
2. $x+4=9$
3. $3a^2$
4. $\dfrac{a+b}{2}$
5. $(a+b)^2=a^2+2ab+b^2$

No decidas todavía si las igualdades son válidas para todos los valores. Solo clasifica el tipo de escritura.

#### Solución

**1.**

$$
x+4
$$

es una expresión. Representa un valor, pero no contiene ninguna afirmación de igualdad.

**2.**

$$
x+4=9
$$

afirma una igualdad entre las expresiones $x+4$ y $9$.

**3.**

$$
3a^2
$$

es una expresión.

**4.**

$$
\frac{a+b}{2}
$$

es una expresión.

**5.**

$$
(a+b)^2=a^2+2ab+b^2
$$

afirma una igualdad entre dos expresiones.

Todavía no estamos estudiando formalmente qué significa que esta igualdad sea válida para distintos valores; eso vendrá más adelante.

---

### Lectura por capas {#apm-i-e0015}

Describe la estructura de

$$
\frac{3a+(b-1)^2}{2c}.
$$

Debes identificar:

1. la estructura exterior;
2. numerador y denominador;
3. los términos principales del numerador;
4. la base y el exponente de la potencia;
5. los factores del denominador.

#### Solución

La expresión completa es

$$
\frac{3a+(b-1)^2}{2c}.
$$

#### 1. Estructura exterior

La operación principal es la división.

#### 2. Numerador y denominador

El numerador es

$$
3a+(b-1)^2.
$$

El denominador es

$$
2c.
$$

#### 3. Términos del numerador

La operación principal del numerador es una suma. Sus términos son

$$
3a
$$

y

$$
(b-1)^2.
$$

#### 4. Potencia

En

$$
(b-1)^2,
$$

la base es

$$
b-1,
$$

y el exponente es $2$.

Dentro de la base aparece una resta.

#### 5. Denominador

El denominador

$$
2c
$$

es un producto con factores

$$
2
\qquad\text{y}\qquad
c.
$$

La expresión completa queda organizada en capas, desde el cociente exterior hasta las subexpresiones interiores.

---

## Resumen de la sección

El objetivo de esta sección no ha sido acumular nombres, sino aprender a describir con precisión la estructura de una expresión.

Hemos usado las palabras:

- **término**, para partes de una suma;
- **factor**, para partes de un producto;
- **base** y **exponente**, para una potencia;
- **numerador** y **denominador**, para un cociente.

También hemos visto que estas palabras dependen del nivel de lectura.

En

$$
2x+5,
$$

la subexpresión $2x$ es un término de la suma exterior y, al mismo tiempo, es internamente un producto cuyos factores son $2$ y $x$.

El hábito fundamental sigue siendo:

$$
\boxed{
\text{leer de fuera hacia dentro}.
}
$$

Además distinguimos dos tipos de escritura:

$$
x+3
$$

representa una expresión, mientras que

$$
x+3=7
$$

afirma una igualdad.

Todavía no hemos formalizado el concepto lógico de afirmación; simplemente hemos preparado el terreno.

Finalmente, usaremos la palabra **fórmula** de manera no técnica para una escritura que expresa compactamente una regla, una relación o un patrón.

---

## Hacia la sección siguiente

Hasta ahora hemos hablado de expresiones como

$$
x^2+2x+1
$$

sin asignar necesariamente un valor a $x$.

Pero, si sabemos que

$$
x=-3,
$$

¿cómo debemos reemplazar correctamente cada aparición de $x$?

¿Es lo mismo escribir

$$
-3^2
$$

que

$$
(-3)^2?
$$

¿Qué ocurre si, en lugar de sustituir una variable por un número, la sustituimos por toda una expresión como

$$
a+b?
$$

Estas preguntas nos llevarán a una operación algebraica básica que exige mucho más cuidado del que parece:

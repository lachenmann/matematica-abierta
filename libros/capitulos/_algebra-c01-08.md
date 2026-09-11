## §8. Sintaxis: escribir para que no haya dudas

En las secciones anteriores hemos insistido en una idea:

$$
\boxed{\text{una expresión tiene estructura}.}
$$

Esa estructura no existe solamente en nuestra mente. La notación debe permitirnos verla.

Comparemos:

$$
-x^2
$$

y

$$
(-x)^2.
$$

Las dos escrituras contienen los mismos símbolos básicos:

$$
-,\qquad x,\qquad 2.
$$

Sin embargo, no representan lo mismo.

En la primera, la potencia actúa sobre $x$:

$$
-x^2=-(x^2).
$$

En la segunda, la potencia actúa sobre toda la expresión $-x$:

$$
(-x)^2.
$$

Si, por ejemplo, $x=3$:

$$
-x^2=-9,
$$

mientras que:

$$
(-x)^2=9.
$$

La diferencia está en el **alcance** de las operaciones.

La pregunta central de esta sección será:

> ¿cómo debemos escribir una expresión para que el lector pueda reconocer sin dudas qué operación actúa sobre qué parte?

La respuesta combinará convenciones de precedencia, paréntesis, barras de fracción, exponentes y hábitos de escritura clara.

::: {.ma-block .ma-intuicion}
**Idea clave**

Una buena notación no obliga al lector a adivinar la estructura.
:::

---

### 8.1 La escritura también tiene jerarquía

Consideremos:

$$
2+3x^2.
$$

No la leemos como si todos los símbolos tuvieran la misma jerarquía.

Las convenciones usuales nos indican que primero reconocemos la potencia:

$$
x^2,
$$

después el producto:

$$
3x^2,
$$

y finalmente la suma:

$$
2+3x^2.
$$

Podemos hacer visible la estructura escribiendo:

$$
2+\bigl(3(x^2)\bigr).
$$

Normalmente no necesitamos tantos paréntesis, porque las convenciones de precedencia ya hacen inequívoca la lectura.

Pero conviene comprender qué están abreviando esas convenciones.

En términos muy generales, en las expresiones elementales de este capítulo:

1. los agrupamientos explícitos se respetan primero;
2. las potencias tienen un alcance más estrecho que los productos y cocientes;
3. los productos y cocientes se reconocen antes que las sumas y restas.

No queremos convertir esta lista en una mnemotecnia ciega.

El objetivo es entender que las convenciones tipográficas hacen visible una **estructura jerárquica**.

---

### 8.2 Los paréntesis cambian el alcance

Comparemos:

$$
2+3^2
$$

y

$$
(2+3)^2.
$$

En la primera:

$$
2+3^2
=
2+9
=
11.
$$

En la segunda:

$$
(2+3)^2
=
5^2
=
25.
$$

Los paréntesis indican que la potencia debe actuar sobre la suma completa.

Lo mismo ocurre con:

$$
-2^2
$$

y:

$$
(-2)^2.
$$

Tenemos:

$$
-2^2
=
-(2^2)
=
-4,
$$

mientras que:

$$
(-2)^2
=
4.
$$

Los paréntesis no son decoración. Determinan qué expresión queda agrupada y, por tanto, cuál es el alcance de una operación exterior.

---

### 8.3 El signo menos merece atención especial

La escritura:

$$
-x^2
$$

se interpreta como:

$$
-(x^2).
$$

El exponente $2$ afecta a $x$, no al signo menos exterior.

En cambio:

$$
(-x)^2
$$

eleva al cuadrado toda la expresión:

$$
-x.
$$

Esto explica por qué, al sustituir un número negativo, §4 insistió en escribir:

$$
(-3)^2
$$

y no:

$$
-3^2.
$$

El problema no era únicamente «poner paréntesis porque sí». Los paréntesis protegían el alcance correcto de la potencia.

Podemos resumir:

$$
\boxed{
-x^2=-(x^2),
\qquad
(-x)^2=(-x)(-x).
}
$$

Cuando $x\ne0$, estas expresiones tienen signos opuestos.

---

### 8.4 La barra de fracción agrupa

Consideremos:

$$
\frac{a+b}{c}.
$$

La barra de fracción no solo indica división. También agrupa.

Todo lo que aparece en el numerador:

$$
a+b
$$

forma una unidad.

Por tanto:

$$
\frac{a+b}{c}
$$

tiene una estructura distinta de:

$$
a+\frac bc.
$$

Probemos, por ejemplo:

$$
a=2,\qquad b=4,\qquad c=3.
$$

Entonces:

$$
\frac{a+b}{c}
=
\frac{2+4}{3}
=
2,
$$

mientras que:

$$
a+\frac bc
=
2+\frac43
=
\frac{10}{3}.
$$

Así:

$$
\frac{a+b}{c}
\ne
a+\frac bc
$$

para estos valores.

La fracción vertical hace visible la agrupación.

---

### 8.5 Cuando escribimos en una sola línea

En texto plano, una fracción vertical puede tener que escribirse mediante `/`.

Entonces debemos ser más cuidadosos.

La expresión:

$$
\frac{a+b}{c}
$$

debe escribirse linealmente como:

```text
(a+b)/c
```

y no como:

```text
a+b/c
```

porque esta segunda escritura corresponde a:

$$
a+\frac bc.
$$

De manera semejante:

$$
\frac{a}{b+c}
$$

debe escribirse:

```text
a/(b+c)
```

si queremos que todo $b+c$ esté en el denominador.

La regla práctica es sencilla:

::: {.ma-block .ma-intuicion}
**Idea clave**

Al pasar una expresión bidimensional a una línea de texto, añade los paréntesis necesarios para conservar exactamente la estructura original.
:::

---

### 8.6 Multiplicación implícita: brevedad sin confusión

En álgebra escribimos:

$$
3x
$$

en lugar de:

$$
3\cdot x.
$$

También escribimos:

$$
2(a+b)
$$

en lugar de:

$$
2\cdot(a+b).
$$

Esta multiplicación implícita suele ser clara.

Pero no toda abreviación es igualmente buena.

Por ejemplo, una escritura lineal como:

```text
1/2x
```

puede resultar poco clara para un lector: ¿se pretende escribir

$$
\frac{1}{2x}
$$

o:

$$
\frac12 x?
$$

Aunque un contexto o una convención local pudiera decidir la lectura, podemos evitar el problema.

Si queremos:

$$
\frac{1}{2x},
$$

escribimos:

```text
1/(2x)
```

Si queremos:

$$
\frac12 x,
$$

podemos escribir:

```text
(1/2)x
```

o, mejor aún cuando el formato lo permite:

$$
\frac12 x.
$$

::: {.ma-block .ma-observacion}
**Observación**

La notación matemática no debe convertirse en una prueba de adivinación. Cuando una escritura breve pueda generar una lectura razonablemente distinta, preferiremos la forma más explícita.
:::

---

### 8.7 Los exponentes también tienen alcance

Comparemos:

$$
a+b^2
$$

con:

$$
(a+b)^2.
$$

En la primera, el exponente afecta solo a $b$.

En la segunda, afecta a toda la suma.

También debemos distinguir:

$$
x^{2+1}
$$

de:

$$
x^2+1.
$$

La primera es una potencia cuyo exponente completo es:

$$
2+1.
$$

La segunda es una suma:

$$
x^2+1.
$$

Cuando el exponente contiene más de un símbolo, las llaves de LaTeX o la composición tipográfica indican qué parte pertenece al exponente:

```text
x^{2+1}
```

produce:

$$
x^{2+1}.
$$

La regla estructural sigue siendo la misma:

$$
\boxed{\text{debemos saber qué expresión está dentro del alcance del exponente}.}
$$

---

### 8.8 Paréntesis anidados

Consideremos:

$$
3\bigl(2+(x-1)^2\bigr).
$$

Podemos leerla desde fuera hacia dentro.

La operación exterior es un producto:

$$
3\cdot\bigl(2+(x-1)^2\bigr).
$$

Dentro del segundo factor aparece una suma:

$$
2+(x-1)^2.
$$

Dentro de esa suma aparece una potencia:

$$
(x-1)^2.
$$

Y su base es:

$$
x-1.
$$

La notación contiene varios niveles de agrupamiento.

Cuando la expresión se hace más compleja, es frecuente alternar visualmente paréntesis y otros delimitadores:

$$
3\left[2+(x-1)^2\right].
$$

Matemáticamente, los corchetes pueden cumplir aquí el mismo papel de agrupamiento que los paréntesis. Se utilizan para mejorar la lectura.

La claridad tipográfica debe acompañar a la estructura matemática.

---

### 8.9 No todos los paréntesis son obligatorios, pero algunos son útiles

La expresión:

$$
2+(3x)
$$

puede escribirse simplemente:

$$
2+3x,
$$

porque la precedencia usual ya indica que $3x$ forma un producto.

En cambio:

$$
(2+3)x
$$

no puede escribirse como:

$$
2+3x
$$

sin cambiar la estructura.

Existe, por tanto, una diferencia entre:

- paréntesis **necesarios** para determinar la estructura;
- paréntesis **opcionales** que pueden ayudar a hacerla más visible.

Por ejemplo:

$$
a+(b+c)
$$

y:

$$
a+b+c
$$

pueden representar el mismo valor en nuestro contexto por asociatividad de la suma.

Sin embargo, si estamos estudiando específicamente la subexpresión $b+c$, conservar los paréntesis puede ser pedagógicamente útil.

La buena escritura matemática no busca siempre el mínimo número posible de signos. Busca una relación equilibrada entre economía y claridad.

---

### 8.10 Ejemplo desarrollado: leer una expresión compleja

::: {.ma-block .ma-observacion #apm-t1-c01-x0008}
**Ejemplo — Alcance y estructura en una expresión anidada**

:::

Consideremos:

$$
-\frac{2x-(a+b)^2}{3c}.
$$

No queremos simplificarla. Queremos leerla con precisión.

#### Paso 1 — El signo exterior

Toda la fracción aparece precedida por un signo menos:

$$
-\left(\frac{2x-(a+b)^2}{3c}\right).
$$

Por tanto, el signo menos actúa sobre el cociente completo.

#### Paso 2 — La fracción

El numerador es:

$$
2x-(a+b)^2.
$$

El denominador es:

$$
3c.
$$

#### Paso 3 — El numerador

Dentro del numerador aparecen dos grandes partes:

$$
2x
$$

y:

$$
(a+b)^2.
$$

La segunda está restada.

#### Paso 4 — La potencia

En:

$$
(a+b)^2,
$$

la base completa es:

$$
a+b.
$$

El exponente es:

$$
2.
$$

#### Paso 5 — Los productos

En:

$$
2x,
$$

hay un producto entre $2$ y $x$.

En:

$$
3c,
$$

hay un producto entre $3$ y $c$.

#### Lectura completa

Podemos describir la expresión como:

> el opuesto del cociente cuyo numerador es la diferencia entre $2x$ y el cuadrado de $a+b$, y cuyo denominador es $3c$.

La estructura puede esquematizarse así:

```text
opuesto
└── cociente
    ├── numerador: 2x - (a+b)^2
    │   ├── producto: 2x
    │   └── potencia: (a+b)^2
    │       └── base: a+b
    └── denominador: 3c
        └── producto: 3·c
```

Este ejemplo resume el hábito que venimos construyendo desde §1:

$$
\boxed{
\text{leer de fuera hacia dentro}
\longrightarrow
\text{reconocer el alcance}
\longrightarrow
\text{interpretar sin adivinar}.
}
$$

---

### 8.11 Una regla editorial: escribir para otro lector

En un cuaderno personal podemos comprender una abreviatura porque recordamos qué queríamos decir.

En un libro, una demostración o una solución escrita para otra persona, esa memoria privada no existe.

La notación debe sostenerse por sí sola.

Por eso preferiremos:

```text
(a+b)/c
```

a una escritura lineal que pueda confundirse con:

```text
a+b/c
```

y preferiremos:

```text
1/(2x)
```

cuando queramos evitar que `1/2x` admita una segunda lectura razonable.

Esta regla no es solamente estética.

La claridad de la notación reduce errores matemáticos.

$$
\boxed{
\text{escribir con claridad forma parte de razonar con claridad}.
}
$$

---

## Ejercicios

### Mismo símbolo, distinto alcance {#apm-t1-c01-e0041}

Explica la diferencia estructural entre cada par. No te limites a calcular.

#### a)

$$
-3^2
\qquad\text{y}\qquad
(-3)^2
$$

#### b)

$$
2+x^2
\qquad\text{y}\qquad
(2+x)^2
$$

#### c)

$$
a+b^3
\qquad\text{y}\qquad
(a+b)^3
$$

#### Solución

#### a)

En:

$$
-3^2,
$$

la potencia actúa sobre $3$:

$$
-(3^2)=-9.
$$

En:

$$
(-3)^2,
$$

la base completa es $-3$:

$$
(-3)^2=9.
$$

#### b)

En:

$$
2+x^2,
$$

solo $x$ está elevado al cuadrado.

En:

$$
(2+x)^2,
$$

toda la suma $2+x$ constituye la base de la potencia.

#### c)

En:

$$
a+b^3,
$$

el exponente $3$ afecta solamente a $b$.

En:

$$
(a+b)^3,
$$

la base completa es $a+b$.

La diferencia en los tres pares es una diferencia de **alcance**.

---

### Barras de fracción {#apm-t1-c01-e0042}

Describe la estructura de:

$$
\frac{a+b}{c+d}.
$$

Después escribe la misma expresión en notación lineal usando `/`.

#### Solución

La expresión completa es un cociente.

El numerador es:

$$
a+b.
$$

El denominador es:

$$
c+d.
$$

Para conservar esa estructura en una sola línea debemos escribir:

```text
(a+b)/(c+d)
```

Los paréntesis son necesarios para indicar que las dos sumas completas son el numerador y el denominador.

---

### Dos escrituras lineales {#apm-t1-c01-e0043}

Interpreta las siguientes escrituras lineales y escríbelas con fracciones verticales.

#### a)

```text
(a+b)/c
```

#### b)

```text
a+b/c
```

#### c)

```text
a/(b+c)
```

Explica por qué las tres estructuras son diferentes.

#### Solución

#### a)

```text
(a+b)/c
```

corresponde a:

$$
\frac{a+b}{c}.
$$

La suma $a+b$ completa forma el numerador.

#### b)

```text
a+b/c
```

corresponde a:

$$
a+\frac bc.
$$

La operación exterior es una suma.

#### c)

```text
a/(b+c)
```

corresponde a:

$$
\frac{a}{b+c}.
$$

La suma $b+c$ completa forma el denominador.

Las tres estructuras difieren porque las operaciones no tienen el mismo alcance.

---

### Elige la escritura inequívoca {#apm-t1-c01-e0044}

Escribe en una sola línea, usando `/`, cada expresión.

#### a)

$$
\frac{1}{2x}
$$

#### b)

$$
\frac12 x
$$

#### c)

$$
\frac{x+1}{y-2}
$$

#### Solución

#### a)

Una escritura inequívoca es:

```text
1/(2x)
```

#### b)

Podemos escribir:

```text
(1/2)x
```

Así queda claro que primero tenemos el factor $1/2$ y luego multiplicamos por $x$.

#### c)

Debemos escribir:

```text
(x+1)/(y-2)
```

Los paréntesis conservan las dos agrupaciones de la fracción original.

---

### Lectura jerárquica {#apm-t1-c01-e0045}

Considera:

$$
-\frac{3x+(y-1)^2}{2z}.
$$

Describe la expresión de fuera hacia dentro e identifica:

1. el alcance del signo menos exterior;
2. numerador y denominador;
3. la potencia y su base;
4. los productos que aparecen.

#### Solución

#### 1. Signo menos

El signo menos exterior afecta a toda la fracción:

$$
-\left(\frac{3x+(y-1)^2}{2z}\right).
$$

#### 2. Fracción

El numerador es:

$$
3x+(y-1)^2.
$$

El denominador es:

$$
2z.
$$

#### 3. Potencia

La potencia es:

$$
(y-1)^2.
$$

Su base completa es:

$$
y-1,
$$

y su exponente es $2$.

#### 4. Productos

En el numerador aparece:

$$
3x,
$$

un producto entre $3$ y $x$.

En el denominador aparece:

$$
2z,
$$

un producto entre $2$ y $z$.

La lectura completa comienza por el signo exterior y avanza hacia las subexpresiones internas.

---

## Resumen de la sección

La sintaxis matemática organiza el alcance de las operaciones.

Hemos aprendido a distinguir expresiones como:

$$
-x^2
\qquad\text{y}\qquad
(-x)^2,
$$

así como:

$$
\frac{a+b}{c}
\qquad\text{y}\qquad
a+\frac bc.
$$

Los recursos principales para hacer visible la estructura son:

- convenciones de precedencia;
- paréntesis y otros delimitadores;
- barras de fracción;
- posición de los exponentes;
- multiplicación implícita usada con cuidado.

Al escribir en una sola línea debemos añadir los paréntesis necesarios para preservar la estructura:

$$
\frac{a+b}{c}
\quad\longleftrightarrow\quad
\texttt{(a+b)/c}.
$$

La regla editorial que conservaremos es:

$$
\boxed{
\text{si una escritura puede inducir una lectura razonablemente distinta, la hacemos más explícita}.
}
$$

Y el hábito matemático es:

$$
\boxed{
\text{reconocer el alcance antes de operar}.
}
$$

---

## Hacia la sección siguiente

Ya sabemos leer la estructura, sustituir valores, interpretar igualdades, distinguir identidades y ecuaciones, justificar transformaciones y escribir de forma inequívoca.

Eso nos permite abordar un nuevo tipo de problema.

Consideremos:

$$
(a+b)^2=a^2+b^2.
$$

O:

$$
\frac{a+b}{a}=b.
$$

O:

$$
2+3x=5x.
$$

Las tres escrituras pueden parecer plausibles si se aplican reglas de manera superficial.

Pero ¿qué estructura fue ignorada en cada caso?

¿Cómo podemos detectar rápidamente que una supuesta regla es falsa?

¿Podemos construir un valor concreto que la contradiga?

La siguiente sección estará dedicada a aprender a diagnosticar precisamente esos errores:

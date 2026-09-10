## §6. Identidad y ecuación: primera distinción

En la sección anterior aprendimos que una igualdad es una afirmación:

$$
A=B
$$

dice que las expresiones $A$ y $B$ representan lo mismo en el contexto considerado.

Ahora comparemos dos igualdades que contienen la misma letra:

$$
2(x+3)=2x+6
$$

y

$$
2x+3=11.
$$

Ambas tienen un signo igual. Ambas contienen $x$. Sin embargo, no cumplen la misma función.

Probemos algunos valores en la primera.

Si $x=0$:

$$
2(0+3)=2\cdot0+6,
$$

es decir,

$$
6=6.
$$

Si $x=2$:

$$
2(2+3)=2\cdot2+6,
$$

y obtenemos:

$$
10=10.
$$

Si $x=-5$:

$$
2(-5+3)=2(-5)+6,
$$

de modo que:

$$
-4=-4.
$$

La igualdad sigue funcionando.

Consideremos ahora:

$$
2x+3=11.
$$

Si $x=4$:

$$
2\cdot4+3=11,
$$

y obtenemos:

$$
11=11.
$$

Pero si $x=3$:

$$
2\cdot3+3=11,
$$

es decir,

$$
9=11,
$$

que es falso.

Parece haber, por tanto, dos situaciones distintas:

- una igualdad que expresa un patrón general;
- una igualdad que impone una condición sobre el valor de la letra.

Esta es la primera distinción que queremos aprender.

---

### 6.1 Una igualdad que expresa un patrón general

Volvamos a:

$$
2(x+3)=2x+6.
$$

La igualdad no está intentando descubrir un valor particular de $x$.

Expresa una relación que esperamos que sea válida cada vez que sustituimos un valor permitido para $x$.

Esto ocurre porque estamos reconociendo una estructura conocida:

$$
2(x+3)
$$

puede transformarse mediante la distributividad en:

$$
2x+2\cdot3,
$$

es decir,

$$
2x+6.
$$

La igualdad expresa, por tanto, un mismo patrón algebraico.

::: {.ma-block .ma-definicion #apm-i-d0006}
**Definición — Identidad**

En este primer sentido operativo, una **identidad** es una igualdad que es válida para todos los valores permitidos de las letras que aparecen en ella, dentro del contexto considerado.
:::

La expresión «dentro del contexto considerado» vuelve a ser importante.

Por ejemplo, una igualdad que contenga una división puede exigir que ciertos valores no se utilicen. Más adelante aprenderemos a formular con precisión esas restricciones.

Por ahora trabajaremos con ejemplos elementales donde los valores permitidos son claros.

Otros ejemplos familiares de identidades son:

$$
a+0=a
$$

o:

$$
3(a+b)=3a+3b.
$$

En estos casos las letras no representan valores especiales que debamos descubrir. Representan valores generales dentro del contexto.

---

### 6.2 Probar casos no basta para demostrar una identidad

Supongamos que queremos saber si:

$$
x^2+x=x(x+1)
$$

es una identidad.

Podemos probar:

$$
x=1,
$$

y obtenemos:

$$
1^2+1=1(1+1),
$$

es decir:

$$
2=2.
$$

También podemos probar:

$$
x=2:
$$

$$
2^2+2=2(2+1),
$$

de modo que:

$$
6=6.
$$

Y con $x=-3$:

$$
(-3)^2+(-3)=(-3)(-3+1),
$$

por lo que:

$$
6=6.
$$

Estos ejemplos son compatibles con la idea de que tenemos una identidad.

Pero todavía no constituyen una demostración.

¿Por qué?

Porque hemos examinado solamente algunos valores. Una afirmación que pretende valer de manera general no queda establecida por una lista finita de comprobaciones.

Para justificar la igualdad debemos entender su estructura:

$$
x(x+1)
$$

se transforma por distributividad en:

$$
x^2+x.
$$

Esa razón algebraica explica por qué la igualdad no depende de haber elegido $1$, $2$ o $-3$.

::: {.ma-block .ma-intuicion}
**Idea clave**

Probar ejemplos puede **comprobar casos** y detectar errores, pero no demuestra por sí solo que una igualdad sea una identidad.
:::

Esta diferencia entre evidencia y demostración se volverá central en el capítulo 5.

---

### 6.3 Una igualdad que impone una condición

Consideremos ahora:

$$
2x+3=11.
$$

Aquí no afirmamos que la igualdad sea correcta para cualquier valor que demos a $x$.

La igualdad impone una condición.

Algunos valores la hacen verdadera y otros no.

Ya vimos que:

$$
x=4
$$

produce:

$$
11=11,
$$

mientras que:

$$
x=3
$$

produce:

$$
9=11.
$$

En este tipo de problema, la letra representa un valor que debe cumplir la igualdad.

::: {.ma-block .ma-definicion #apm-i-d0007}
**Definición — Ecuación**

En este primer sentido operativo, una **ecuación** es una igualdad en la que una o más letras se tratan como valores por determinar y se pregunta qué valores permitidos hacen verdadera la igualdad.
:::

No estudiaremos todavía métodos sistemáticos para encontrar esos valores.

Ese será el objetivo principal del capítulo 11.

Por ahora solo queremos reconocer qué clase de pregunta plantea una ecuación.

---

### 6.4 Identidad y ecuación no se distinguen solo por su apariencia

Considera:

$$
x+x=2x.
$$

Si la presentamos como una regla general del cálculo algebraico, la estamos usando como identidad.

Pero imaginemos una pregunta distinta:

> ¿Para qué valores de $x$ es verdadera la igualdad $x+x=2x$?

La misma escritura puede aparecer dentro de una pregunta sobre valores que satisfacen una igualdad.

En este caso descubriríamos que todos los valores permitidos la satisfacen.

Esto muestra una sutileza importante:

::: {.ma-block .ma-intuicion}
**Idea clave**

«Identidad» y «ecuación» no son etiquetas que podamos decidir siempre observando únicamente la forma de los símbolos. También importa **qué se está afirmando o preguntando**.
:::

En este capítulo usaremos normalmente:

- **identidad** cuando la intención sea expresar una igualdad general;
- **ecuación** cuando la intención sea determinar qué valores hacen verdadera una igualdad.

Más adelante podremos formular esta distinción con herramientas lógicas más precisas.

---

### 6.5 Una ecuación puede ser verdadera para un valor y falsa para otro

Consideremos:

$$
x^2=9.
$$

Si $x=3$:

$$
3^2=9,
$$

que es verdadero.

Si $x=-3$:

$$
(-3)^2=9,
$$

que también es verdadero.

Si $x=2$:

$$
2^2=9,
$$

es decir:

$$
4=9,
$$

que es falso.

No necesitamos resolver sistemáticamente esta ecuación para comprender su carácter.

La igualdad no está afirmando que:

$$
x^2=9
$$

sea válida para cualquier valor de $x$.

Está imponiendo una condición.

Este tipo de lectura será esencial cuando lleguemos a estudiar ecuaciones con precisión.

---

### 6.6 Ejemplo desarrollado: dos igualdades, dos funciones

::: {.ma-block .ma-observacion #apm-i-x0005}
**Ejemplo — Identidad frente a ecuación**

:::

Comparemos:

$$
3(x+2)=3x+6
$$

y

$$
3x+2=14.
$$

#### Primera igualdad

Probemos primero algunos valores en:

$$
3(x+2)=3x+6.
$$

Para $x=0$:

$$
3(0+2)=3\cdot0+6,
$$

por tanto:

$$
6=6.
$$

Para $x=5$:

$$
3(5+2)=3\cdot5+6,
$$

de modo que:

$$
21=21.
$$

Estos casos son compatibles con una identidad.

Pero la razón decisiva es estructural:

$$
3(x+2)
=
3x+3\cdot2
=
3x+6.
$$

La distributividad justifica la igualdad de manera general.

Por tanto, en el contexto usual:

$$
\boxed{3(x+2)=3x+6}
$$

es una identidad.

#### Segunda igualdad

Consideremos:

$$
3x+2=14.
$$

Si $x=4$:

$$
3\cdot4+2=14,
$$

y obtenemos:

$$
14=14.
$$

Si $x=3$:

$$
3\cdot3+2=14,
$$

es decir:

$$
11=14.
$$

La igualdad no es válida para cualquier valor.

Está imponiendo una condición sobre $x$.

Por tanto, en este contexto:

$$
\boxed{3x+2=14}
$$

es una ecuación.

#### Comparación

En la identidad preguntamos esencialmente:

> ¿qué relación general expresan estas dos formas?

En la ecuación preguntamos:

> ¿qué valores hacen verdadera esta igualdad?

Esa es la distinción fundamental de la sección.

---

### 6.7 Un contraejemplo puede descartar una supuesta identidad

Supongamos que alguien afirma:

$$
(a+b)^2=a^2+b^2.
$$

y sostiene que se trata de una identidad.

No necesitamos comprobar todos los valores posibles para demostrar que la afirmación es falsa.

Basta encontrar un caso donde falle.

Tomemos:

$$
a=1,
\qquad
b=1.
$$

El lado izquierdo vale:

$$
(1+1)^2=4.
$$

El lado derecho vale:

$$
1^2+1^2=2.
$$

Por tanto:

$$
4\ne2.
$$

La igualdad no puede ser una identidad.

Este razonamiento introduce una idea que estudiaremos con más profundidad después:

$$
\boxed{
\text{un solo caso donde falle basta para refutar una afirmación que pretende valer siempre}.
}
$$

Todavía no desarrollaremos formalmente el método del contraejemplo. Lo utilizaremos aquí únicamente como herramienta de diagnóstico.

---

### 6.8 Tres preguntas distintas ante una igualdad con letras

Cuando encontremos una igualdad que contiene letras, conviene preguntar:

#### 1. ¿Qué papel tienen las letras?

¿Representan valores generales, valores fijados o valores por determinar?

#### 2. ¿Qué pretende la igualdad?

¿Expresa un patrón general o impone una condición?

#### 3. ¿Cómo se justifica?

Si pretendemos que sea una identidad, ¿existe una ley algebraica que explique la igualdad?

Si estamos ante una ecuación, ¿qué valores hacen verdadera la igualdad?

Estas tres preguntas evitan una lectura mecánica de los símbolos.

---

## Ejercicios

### Identidad o ecuación {#apm-i-e0029}

En cada caso, indica si la escritura se está usando como identidad o como ecuación. Explica tu decisión.

#### a)

> La distributividad permite escribir:

$$
5(a+b)=5a+5b.
$$

#### b)

> Determina qué valor de $x$ hace verdadera:

$$
5x+2=17.
$$

#### c)

> La suma con cero cumple:

$$
n+0=n.
$$

#### d)

> ¿Qué valores de $y$ hacen verdadera:

$$
y^2=16?
$$

#### Solución

#### a)

La igualdad expresa un patrón general basado en la distributividad.

Se está usando como **identidad**.

#### b)

La igualdad impone una condición y la pregunta pide determinar el valor de $x$ que la satisface.

Se está usando como **ecuación**.

#### c)

La igualdad expresa una regla general de la suma.

Se está usando como **identidad**.

#### d)

La pregunta pide determinar qué valores hacen verdadera la igualdad.

Se está usando como **ecuación**.

---

### Comprobar valores en una ecuación {#apm-i-e0030}

Considera:

$$
2x+5=13.
$$

Decide si cada valor hace verdadera la igualdad:

1. $x=2$;
2. $x=4$;
3. $x=-4$.

No desarrolles un método general para resolver la ecuación; basta sustituir y comprobar.

#### Solución

#### 1. \(x=2\)

Sustituimos:

$$
2\cdot2+5=13.
$$

El lado izquierdo vale:

$$
4+5=9.
$$

Obtenemos:

$$
9=13,
$$

que es falso.

Por tanto, $x=2$ no hace verdadera la ecuación.

#### 2. \(x=4\)

Sustituimos:

$$
2\cdot4+5=13.
$$

Entonces:

$$
8+5=13.
$$

Obtenemos:

$$
13=13,
$$

que es verdadero.

Por tanto, $x=4$ sí hace verdadera la ecuación.

#### 3. \(x=-4\)

Sustituimos:

$$
2(-4)+5=13.
$$

Entonces:

$$
-8+5=-3.
$$

Obtenemos:

$$
-3=13,
$$

que es falso.

Por tanto, $x=-4$ no hace verdadera la ecuación.

---

### ¿Bastan tres casos? {#apm-i-e0031}

Un estudiante quiere demostrar que:

$$
4(x+1)=4x+4
$$

es una identidad.

Comprueba la igualdad para:

$$
x=0,\qquad x=1,\qquad x=10
$$

y concluye:

> «Como funcionó tres veces, ya está demostrada».

1. Comprueba los tres casos.
2. Explica por qué la conclusión del estudiante no está justificada solo por esas comprobaciones.
3. Indica qué ley algebraica explica la igualdad general.

#### Solución

#### 1. Comprobaciones

Para $x=0$:

$$
4(0+1)=4\cdot0+4,
$$

por lo que:

$$
4=4.
$$

Para $x=1$:

$$
4(1+1)=4\cdot1+4,
$$

de modo que:

$$
8=8.
$$

Para $x=10$:

$$
4(10+1)=4\cdot10+4,
$$

y obtenemos:

$$
44=44.
$$

Los tres casos funcionan.

#### 2. Por qué no basta

La identidad pretende ser válida para todos los valores permitidos de $x$.

Comprobar tres valores verifica únicamente esos tres casos.

Podría existir otro valor donde una igualdad distinta fallara.

Por tanto, los ejemplos aportan evidencia, pero no constituyen por sí solos una demostración general.

#### 3. Ley que lo explica

La distributividad da:

$$
4(x+1)
=
4x+4\cdot1
=
4x+4.
$$

Esta es la razón estructural que justifica la identidad.

---

### Refutar una supuesta identidad {#apm-i-e0032}

Un estudiante afirma que:

$$
(a-b)^2=a^2-b^2
$$

es una identidad.

Encuentra valores sencillos de $a$ y $b$ que muestren que la afirmación es falsa.

#### Solución

Podemos elegir:

$$
a=2,
\qquad
b=1.
$$

El lado izquierdo es:

$$
(2-1)^2=1.
$$

El lado derecho es:

$$
2^2-1^2
=
4-1
=
3.
$$

Por tanto:

$$
1\ne3.
$$

Así, la igualdad no puede ser una identidad.

No necesitamos examinar todos los valores: un solo caso donde falle basta para descartar una afirmación que pretendía valer siempre.

---

### La misma escritura, distinta pregunta {#apm-i-e0033}

Considera:

$$
x+x=2x.
$$

#### a)

Interprétala como una identidad y explica qué afirma.

#### b)

Interprétala como una ecuación mediante la pregunta:

> «¿Qué valores de $x$ hacen verdadera esta igualdad?»

#### c)

Explica qué enseña este ejemplo sobre las palabras «identidad» y «ecuación».

#### Solución

#### a)

Como identidad, la igualdad expresa que sumar un número consigo mismo produce el doble de ese número:

$$
x+x=2x.
$$

La intención es formular un patrón general.

#### b)

Como ecuación, preguntamos qué valores de $x$ hacen verdadera la igualdad.

En este caso, la misma ley algebraica muestra que la igualdad se cumple para todos los valores permitidos en el contexto usual.

No necesitamos construir todavía un conjunto formal de soluciones.

#### c)

El ejemplo muestra que «identidad» y «ecuación» no se distinguen únicamente por la apariencia de la escritura.

También importa la función que cumple la igualdad:

- expresar una relación general;
- o plantear una pregunta sobre los valores que la hacen verdadera.

---

## Resumen de la sección

En esta sección hemos distinguido dos usos fundamentales de las igualdades con letras.

::: {.ma-block .ma-observacion}
**Síntesis**

Una **identidad** es, en nuestro sentido operativo inicial, una igualdad válida para todos los valores permitidos de las letras dentro del contexto.

Una **ecuación** es, en nuestro sentido operativo inicial, una igualdad en la que una o más letras se tratan como valores por determinar y se pregunta qué valores permitidos la hacen verdadera.
:::

El contraste básico es:

$$
\boxed{
\text{identidad}
\longleftrightarrow
\text{patrón general}
}
$$

frente a:

$$
\boxed{
\text{ecuación}
\longleftrightarrow
\text{condición sobre valores}.
}
$$

También hemos aprendido algo metodológicamente decisivo:

$$
\boxed{
\text{comprobar ejemplos}
\neq
\text{demostrar una afirmación general}.
}
$$

Los ejemplos pueden apoyar una conjetura o detectar un error. La justificación general exige una razón matemática.

Finalmente, hemos visto que un solo contraejemplo puede refutar una supuesta identidad.

---

## Hacia la sección siguiente

En esta sección hemos usado varias veces identidades como:

$$
3(x+2)=3x+6.
$$

Pero todavía no hemos estudiado de manera sistemática **qué significa transformar una expresión sin cambiar su valor**.

Consideremos:

$$
3(x+2)+2x.
$$

Podemos escribir:

$$
3x+6+2x
$$

y luego:

$$
5x+6.
$$

¿Por qué están permitidos esos pasos?

¿Qué ley justifica cada uno?

¿«Simplificar» significa simplemente mover símbolos hasta que la expresión se vea más corta?

La siguiente sección fijará una disciplina que usaremos durante todo el libro:

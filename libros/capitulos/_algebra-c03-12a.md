## §12. Diagnosticar errores y leer lenguaje matemático

A lo largo de este capítulo construimos un lenguaje para responder preguntas cada vez más precisas:

- ¿qué variable puede cambiar?;
- ¿sobre qué dominio cambia?;
- ¿qué afirma un cuantificador?;
- ¿hasta dónde llega?;
- ¿qué apariciones quedan libres?;
- ¿en qué orden se hacen las elecciones?;
- ¿qué significa negar la afirmación?;
- ¿hay al menos un valor o exactamente uno?;
- ¿qué símbolos permanecen fijos como parámetros?

La última tarea no consiste en añadir una nueva definición.

Consiste en aprender a **diagnosticar**. En matemáticas, muchas fórmulas incorrectas parecen plausibles porque contienen los símbolos adecuados, pero los organizan de manera equivocada.

Por ejemplo, una escritura puede contener:

$$
\forall,\qquad
\exists,\qquad
R(x,y),
$$

y aun así expresar algo distinto de la frase que pretendíamos traducir.

Por eso la lectura matemática debe incluir una pregunta crítica:

> **¿La fórmula dice realmente lo que creemos que dice?**

---

### 12.1 Ocho errores que debemos poder detectar

Al cerrar el capítulo, debemos reconocer al menos estos ocho problemas.

#### 1. Dominio omitido

La fórmula $\exists x\,(2x=1)$ no tiene un significado matemático suficientemente determinado si no sabemos qué valores están permitidos para $x$.

Sobre los enteros es falsa. Sobre los racionales es verdadera.

El dominio forma parte de la afirmación.

#### 2. Universal y existencial confundidos

No es lo mismo:

$$
\forall x\,P(x)
$$

que:

$$
\exists x\,P(x).
$$

La primera exige ausencia de excepciones. La segunda exige al menos un caso favorable.

#### 3. «No todos» confundido con «todos no»

No es lo mismo:

$$
\neg\forall x\,P(x)
$$

que:

$$
\forall x\,\neg P(x).
$$

La primera dice:

> «hay al menos una excepción».

La segunda dice:

> «todos incumplen la condición».

#### 4. Orden de cuantificadores alterado

En general:

$$
\forall x\,\exists y\,R(x,y)
\not\equiv
\exists y\,\forall x\,R(x,y).
$$

La primera permite que $y$ se ajuste a $x$.

La segunda exige un mismo $y$ para todos los valores de $x$.

#### 5. Aparición libre no advertida

En:

$$
\forall x\,R(x,y),
$$

$x$ está ligada, pero $y$ permanece libre. La fórmula no está cerrada.

#### 6. Alcance incorrecto

No es lo mismo:

$$
\forall x\,(P(x)\Rightarrow Q)
$$

que:

$$
(\forall x\,P(x))\Rightarrow Q.
$$

Los paréntesis determinan qué parte de la fórmula controla el cuantificador.

#### 7. Existencia confundida con unicidad

De:

$$
\exists x\,P(x)
$$

no podemos concluir:

$$
\exists!x\,P(x).
$$

Encontrar un testigo no demuestra que sea el único.

#### 8. Cuantificación universal implícita peligrosa

Una expresión como:

$$
x^2\ge0
$$

puede aparecer en prosa matemática con la intención informal de decir:

> «para todo valor permitido de $x$, $x^2\ge0$».

Pero en este capítulo no adoptamos esa cuantificación implícita como escritura canónica.

Si queremos afirmar universalidad, escribimos:

$$
\forall x\,(x^2\ge0)
$$

después de fijar el dominio. La escritura explícita evita que una aparición libre sea interpretada como cuantificada sin justificación.

---

### 12.2 Un diagnóstico debe identificar el tipo de error

Decir:

> «La fórmula está mal»

no basta. Debemos poder explicar **qué** está mal. Por ejemplo, si alguien traduce:

> «Para cada entero $x$, existe un entero $y$ tal que $y=x+1$»

como:

$$
\exists y\,\forall x\,(y=x+1),
$$

el problema no es simplemente que «los símbolos estén cambiados».

El diagnóstico preciso es:

> **el orden de los cuantificadores fue invertido.**

La reparación es:

$$
\boxed{
\forall x\,\exists y\,(y=x+1).
}
$$

La capacidad de nombrar el error ayuda a corregirlo sin modificar otras partes que sí estaban bien.

---

### 12.3 Diagnosticar por capas

Ante una fórmula dudosa podemos revisar, en este orden:

#### Capa 1 — Contexto

- ¿Está declarado el dominio?
- ¿Hay parámetros fijados?

#### Capa 2 — Variables

- ¿Qué letras pueden variar?
- ¿Qué apariciones están libres?
- ¿Qué apariciones están ligadas?

#### Capa 3 — Cuantificadores

- ¿Corresponde $\forall$ o $\exists$?
- ¿El orden coincide con la prosa?
- ¿Se está afirmando existencia o existencia única?

#### Capa 4 — Alcance

- ¿Los paréntesis reflejan correctamente qué controla cada cuantificador?
- ¿La negación alcanza la parte correcta?

#### Capa 5 — Conectivos

- ¿«todo $P$ es $Q$» fue traducido mediante implicación?
- ¿«algún $P$ es $Q$» fue traducido mediante conjunción?
- ¿La negación de los conectivos se hizo con las leyes correctas?

#### Capa 6 — Lectura inversa

Finalmente:

> «Si leo la fórmula resultante en prosa, ¿recupero la afirmación original?»

Podemos condensarlo así:

$$
\boxed{
\text{contexto}
\to
\text{variables}
\to
\text{cuantificadores}
\to
\text{alcance}
\to
\text{conectivos}
\to
\text{lectura inversa}.
}
$$

---

### 12.4 El dominio puede revelar un error invisible

Consideremos $\exists x\,(2x=3)$. Sin dominio, no podemos decidir qué afirma exactamente.

Si trabajamos con enteros, la afirmación es falsa. Si trabajamos con racionales, es verdadera, porque:

$$
x=\frac32
$$

es un valor permitido y satisface:

$$
2\cdot\frac32=3.
$$

El error no está dentro de los paréntesis. Tampoco está en el cuantificador.

Está en la información que falta **antes** de la fórmula.

Esto muestra que el diagnóstico lógico no se limita a inspeccionar símbolos.

También debemos revisar el contexto que les da significado.

---

### 12.5 Las variables libres son una señal de alarma

Supongamos que queremos expresar una proposición acerca de dos variables y escribimos:

$$
\forall x\,R(x,y).
$$

La aparición de $y$ permanece libre. Eso no significa automáticamente que la fórmula sea inútil.

Podría ocurrir que $y$ hubiese sido fijada como parámetro en el contexto.

Pero si no existe tal declaración, la fórmula todavía depende de un valor no fijado.

Por tanto, ante una variable libre debemos preguntar:

> **¿Debe ser cuantificada o fue fijada explícitamente por el contexto?**

No debemos corregirla de manera automática. Podrían ser apropiadas, según la intención, fórmulas tan distintas como:

$$
\forall y\,\forall x\,R(x,y),
$$

$$
\exists y\,\forall x\,R(x,y),
$$

o simplemente:

$$
\forall x\,R(x,y)
$$

si $y$ ha sido declarada como parámetro. El diagnóstico debe recuperar primero la intención.

---

### 12.6 Un contraejemplo puede detectar una traducción equivocada

Supongamos que alguien afirma:

$$
\forall x\,\exists y\,R(x,y)
\equiv
\exists y\,\forall x\,R(x,y).
$$

Para mostrar que la equivalencia general es falsa no necesitamos analizar todos los predicados posibles.

Basta una interpretación donde los dos lados tengan valores de verdad distintos.

Tomemos, sobre los enteros:

$$
R(x,y):\quad y=x+1.
$$

Entonces $\forall x\,\exists y\,(y=x+1)$ es verdadera.

Pero:

$$
\exists y\,\forall x\,(y=x+1)
$$

es falsa. Así detectamos que intercambiar cuantificadores mixtos no es una transformación válida en general.

El contraejemplo funciona aquí como control semántico de una traducción o equivalencia propuesta.

---

### 12.7 Existencia no autoriza el singular

Consideremos, sobre los enteros:

$$
x^2=4.
$$

Podemos encontrar:

$$
x=2.
$$

Eso confirma:

$$
\exists x\,(x^2=4).
$$

Pero también:

$$
x=-2
$$

satisface la condición. Sería incorrecto pasar de:

> «hemos encontrado una solución»

a:

> «hemos encontrado la única solución».

La fórmula $\exists!x\,(x^2=4)$ es falsa sobre los enteros. El diagnóstico es:

> **se confundió existencia con unicidad.**

---

### 12.8 No corregir una fórmula antes de reconstruir la intención

Una misma fórmula defectuosa puede admitir varias reparaciones. Consideremos $\forall x\,R(x,y)$, sin más contexto.

Podríamos sentir la tentación de añadir:

$$
\forall y.
$$

Pero quizá la intención era:

> «Existe un $y$ que funciona para todo $x$».

Entonces la reparación correcta sería:

$$
\exists y\,\forall x\,R(x,y).
$$

O quizá $y$ debía ser un parámetro fijado previamente.

En ese caso no habría que cuantificarla. Por tanto:

$$

\text{diagnosticar}
\neq
\text{añadir símbolos hasta cerrar la fórmula}.

$$

Primero reconstruimos el significado pretendido. Después reparamos la escritura.

---

### 12.9 La lectura en prosa es una prueba de control

Supongamos que hemos escrito:

$$
\exists y\,\forall x\,(x+y=0).
$$

Leamos:

> «Existe un entero $y$ tal que, para todo entero $x$, $x+y=0$».

Si nuestra intención era:

> «Para cada entero $x$ existe un entero $y$ tal que $x+y=0$»,

la lectura inversa revela inmediatamente que hemos escrito otra cosa.

La fórmula correcta era:

$$
\forall x\,\exists y\,(x+y=0).
$$

Por eso una buena práctica final es siempre:

$$
\boxed{
\text{prosa}
\longrightarrow
\text{fórmula}
\longrightarrow
\text{prosa}.
}
$$

Si la frase recuperada no coincide con la inicial, hay un error estructural.

---

### 12.10 Ejemplo desarrollado

::: {.ma-block .ma-observacion #apm-i-x0032}
**Ejemplo — Expediente de tres errores**
:::

Queremos expresar la afirmación:

> «Para cada entero $x$, existe un entero $y$ tal que $x+y=0$».

La traducción correcta es:

$$

\forall x\,\exists y\,(x+y=0),

$$

con dominio de los enteros. Examinemos tres formulaciones defectuosas.

#### Formulación A

$$
\forall x\,\exists y\,(x+y=0)
$$

sin declarar ningún dominio.

##### Diagnóstico

Los cuantificadores y su orden coinciden con la frase, pero falta información esencial:

> ¿qué valores están permitidos para $x$ e $y$?

##### Reparación

Declaramos:

> «El dominio de $x$ y de $y$ es el de los enteros».

La fórmula queda entonces correctamente interpretada.

---

#### Formulación B

$$
\exists y\,\forall x\,(x+y=0).
$$

##### Diagnóstico

El dominio puede estar bien declarado y las dos variables están ligadas.

El error es otro:

> **se invirtió el orden de los cuantificadores.**

La fórmula afirma:

> «Hay un mismo entero $y$ que sumado con todo entero $x$ da cero».

Eso no es lo que decía la frase original.

##### Reparación

Restauramos el orden:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

---

#### Formulación C

$$
\forall x\,(x+y=0).
$$

##### Diagnóstico

La aparición de:

$$
y
$$

queda libre. La frase original decía:

> «existe un entero $y$»

para cada $x$. Por tanto, falta el cuantificador existencial correspondiente.

##### Reparación

Escribimos:

$$
\boxed{
\forall x\,\exists y\,(x+y=0).
}
$$

---

#### Control semántico

La fórmula correcta es verdadera sobre los enteros. Para cada:

$$
x,
$$

podemos elegir:

$$
y=-x.
$$

Entonces:

$$
x+(-x)=0.
$$

#### Resultado del expediente

Los tres errores eran diferentes:

1. **A:** dominio omitido;
2. **B:** orden de cuantificadores alterado;
3. **C:** aparición libre no advertida.

La reparación correcta apareció solo después de identificar con precisión el problema de cada caso.

---

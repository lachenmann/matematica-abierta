## §4. Sustitución y evaluación

En §2 introdujimos letras como símbolos que pueden representar números. En §3 aprendimos a leer expresiones formadas con esas letras.

Consideremos ahora:

$$
x^2+2x+1.
$$

Mientras no fijemos un valor para $x$, la expresión permanece escrita de forma general.

Pero supongamos que nos dicen:

$$
x=3.
$$

Entonces podemos reemplazar cada aparición de $x$ por $3$:

$$
3^2+2\cdot3+1.
$$

Y ahora sí podemos calcular:

$$
3^2+2\cdot3+1
=
9+6+1
=
16.
$$

Hemos realizado dos acciones distintas:

1. **sustituir** el símbolo $x$ por un valor;
2. **evaluar** la expresión obtenida.

Parecen operaciones elementales. Y lo son. Sin embargo, muchos errores algebraicos futuros nacen precisamente de sustituir sin respetar la estructura de la expresión.

La idea central de esta sección será:

::: {.ma-block .ma-intuicion}
**Idea clave**

Sustituir no significa «borrar una letra y poner otra cosa en su lugar» de cualquier manera.  
Sustituir significa **reemplazar el símbolo por una nueva expresión conservando intacta la estructura que lo rodea**.
:::

---

### 4.1 Sustituir es reemplazar todas las apariciones

Consideremos:

$$
2x+5.
$$

Si:

$$
x=4,
$$

debemos reemplazar la aparición de $x$ por $4$:

$$
2x+5
\quad\longrightarrow\quad
2\cdot4+5.
$$

Después calculamos:

$$
2\cdot4+5
=
8+5
=
13.
$$

Ahora considera:

$$
x^2+3x-1.
$$

Si:

$$
x=2,
$$

la letra aparece dos veces.

Debemos reemplazar **ambas** apariciones:

$$
x^2+3x-1
\quad\longrightarrow\quad
2^2+3\cdot2-1.
$$

Entonces:

$$
2^2+3\cdot2-1
=
4+6-1
=
9.
$$

Un error frecuente sería sustituir solo la primera aparición:

$$
2^2+3x-1.
$$

Eso no es la evaluación de la expresión en $x=2$, porque todavía queda una aparición de $x$ sin reemplazar.

Por tanto:

$$
\boxed{
\text{si un símbolo recibe un valor, debemos sustituir todas sus apariciones relevantes}.
}
$$

---

### 4.2 Los paréntesis protegen la estructura

El caso más importante aparece cuando sustituimos un número negativo.

Consideremos:

$$
x^2.
$$

Si:

$$
x=-3,
$$

no debemos escribir simplemente

$$
-3^2.
$$

¿Por qué?

Porque:

$$
-3^2
$$

significa, según las convenciones usuales,

$$
-(3^2),
$$

y por tanto:

$$
-3^2=-9.
$$

Pero nosotros queremos elevar al cuadrado **el valor completo de $x$**, que es $-3$.

Debemos escribir:

$$
(-3)^2.
$$

Entonces:

$$
(-3)^2=9.
$$

Así,

$$
x^2
\quad\text{con}\quad
x=-3
$$

se convierte en:

$$
(-3)^2,
$$

no en:

$$
-3^2.
$$

::: {.ma-block .ma-intuicion}
**Idea clave**

Cuando sustituimos una variable por un número negativo, los paréntesis conservan el número completo como una unidad.
:::

Este no es un truco tipográfico. Es una consecuencia de la estructura que aprendimos a leer en §1 y §3.

---

### 4.3 Ejemplo desarrollado: un número negativo

::: {.ma-block .ma-observacion #apm-i-x0002}
**Ejemplo — Sustituir sin perder el signo**

:::

Evaluemos:

$$
x^2+2x+1
$$

cuando:

$$
x=-3.
$$

#### Paso 1 — Identificar todas las apariciones de $x$

La expresión contiene dos apariciones:

$$
x^2
$$

y

$$
2x.
$$

#### Paso 2 — Sustituir el valor completo

Como:

$$
x=-3,
$$

escribimos:

$$
(-3)^2+2(-3)+1.
$$

Los paréntesis son esenciales.

#### Paso 3 — Evaluar cada parte

Tenemos:

$$
(-3)^2=9
$$

y

$$
2(-3)=-6.
$$

Por tanto:

$$
(-3)^2+2(-3)+1
=
9-6+1
=
4.
$$

#### Resultado

El valor de la expresión cuando $x=-3$ es:

$$
\boxed{4}.
$$

#### Qué habría ocurrido con una sustitución incorrecta

Si hubiéramos escrito:

$$
-3^2+2(-3)+1,
$$

obtendríamos:

$$
-9-6+1=-14.
$$

El error no estaría en la aritmética final. Estaría mucho antes: habríamos alterado la estructura al reemplazar $x$ por $-3$ sin agrupar el valor completo.

---

### 4.4 Evaluar una expresión

Ya podemos fijar el vocabulario central de la sección.

::: {.ma-block .ma-definicion #apm-i-d0004}
**Definición — Evaluación de una expresión**

**Evaluar una expresión** para valores dados de sus símbolos consiste en sustituir esos valores en todas las apariciones correspondientes y, cuando sea posible, realizar las operaciones resultantes.
:::

Por ejemplo, evaluemos:

$$
3a-2
$$

cuando:

$$
a=5.
$$

Sustituimos:

$$
3a-2
\quad\longrightarrow\quad
3\cdot5-2.
$$

Calculamos:

$$
3\cdot5-2
=
15-2
=
13.
$$

La evaluación tiene, por tanto, una secuencia conceptual clara:

$$
\boxed{
\text{expresión general}
\longrightarrow
\text{sustitución}
\longrightarrow
\text{expresión concreta}
\longrightarrow
\text{valor}.
}
$$

---

### 4.5 El cero también debe sustituirse

Consideremos:

$$
4x+7.
$$

Si:

$$
x=0,
$$

la sustitución correcta es:

$$
4\cdot0+7.
$$

Entonces:

$$
4\cdot0+7
=
0+7
=
7.
$$

Puede parecer innecesario escribir explícitamente el cero, pero hacerlo ayuda a conservar la estructura.

En expresiones más complejas, «omitir» una parte porque vale cero puede ocultar errores.

Por ejemplo, en:

$$
x^2+5x+4,
$$

si $x=0$:

$$
0^2+5\cdot0+4
=
4.
$$

El método no cambia porque el valor elegido sea cero.

---

### 4.6 Sustitución con varias letras

Consideremos:

$$
2a+3b.
$$

Supongamos que:

$$
a=4,
\qquad
b=-2.
$$

Debemos sustituir cada letra por su valor correspondiente:

$$
2a+3b
\quad\longrightarrow\quad
2\cdot4+3(-2).
$$

Después evaluamos:

$$
2\cdot4+3(-2)
=
8-6
=
2.
$$

La sustitución debe respetar dos cosas:

1. **qué símbolo recibe qué valor**;
2. **todas las apariciones del símbolo**.

Consideremos:

$$
a^2+ab+b^2.
$$

Si:

$$
a=2,
\qquad
b=-1,
$$

obtenemos:

$$
2^2+2(-1)+(-1)^2.
$$

Y entonces:

$$
4-2+1
=
3.
$$

De nuevo, los paréntesis protegen el valor negativo de $b$.

---

### 4.7 Sustituir una expresión completa

Hasta ahora hemos sustituido letras por números.

Pero podemos hacer algo más general.

Consideremos:

$$
x^2+1.
$$

Supongamos que queremos reemplazar $x$ por la expresión:

$$
a+b.
$$

No estamos diciendo que $x$ sea un número concreto. Estamos indicando que, en esta escritura, donde aparecía $x$ debe aparecer ahora **toda la expresión** $a+b$.

Entonces:

$$
x^2+1
\quad\longrightarrow\quad
(a+b)^2+1.
$$

Los paréntesis vuelven a ser esenciales.

Si escribiéramos:

$$
a+b^2+1,
$$

habríamos sustituido incorrectamente, porque solo $b$ quedaría elevado al cuadrado.

La estructura original era:

$$
\boxed{x}^2+1.
$$

La nueva estructura debe ser:

$$
\boxed{(a+b)}^2+1.
$$

La expresión $a+b$ ocupa exactamente el lugar estructural que antes ocupaba $x$.

---

### 4.8 Ejemplo desarrollado: una expresión por otra expresión

::: {.ma-block .ma-observacion #apm-i-x0003}
**Ejemplo — Sustituir una expresión completa**

:::

Consideremos:

$$
2x^2-3x+4
$$

y sustituimos:

$$
x=a+1.
$$

#### Paso 1 — Localizar todas las apariciones de $x$

Aparece en:

$$
x^2
$$

y en:

$$
-3x.
$$

#### Paso 2 — Reemplazar $x$ por la expresión completa

Escribimos:

$$
2(a+1)^2-3(a+1)+4.
$$

No escribimos:

$$
2a+1^2-3a+1+4,
$$

porque eso destruiría los agrupamientos de la expresión original.

#### Paso 3 — Decidir si necesitamos seguir

Si nuestro objetivo era únicamente realizar la sustitución, podemos detenernos aquí:

$$
\boxed{2(a+1)^2-3(a+1)+4}.
$$

No existe ninguna obligación de expandir.

Más adelante aprenderemos a transformar expresiones de forma sistemática. Por ahora es preferible separar claramente:

$$
\text{sustituir}
\qquad\text{de}\qquad
\text{simplificar o expandir}.
$$

Esta distinción evita hacer varias operaciones mentalmente al mismo tiempo.

---

### 4.9 Sustituir no es simplificar

Consideremos:

$$
3x+2
$$

y supongamos:

$$
x=a+b.
$$

La sustitución produce:

$$
3(a+b)+2.
$$

Podríamos, usando distributividad, transformar después esa expresión en:

$$
3a+3b+2.
$$

Pero son dos etapas diferentes:

#### Sustitución

$$
3x+2
\quad\longrightarrow\quad
3(a+b)+2.
$$

#### Transformación posterior

$$
3(a+b)+2
\quad\longrightarrow\quad
3a+3b+2.
$$

Mantener separadas estas acciones es un buen hábito.

::: {.ma-block .ma-intuicion}
**Idea clave**

Primero sustituimos correctamente.  
Solo después, si el problema lo requiere, simplificamos o transformamos.
:::

---

### 4.10 Un error típico: cambiar solo lo visible

Consideremos:

$$
(x+1)^2.
$$

Si:

$$
x=-2,
$$

la sustitución correcta es:

$$
((-2)+1)^2.
$$

Podemos escribirla de forma más limpia como:

$$
(-2+1)^2.
$$

Y luego:

$$
(-2+1)^2
=
(-1)^2
=
1.
$$

Un error posible sería escribir:

$$
-2+1^2.
$$

Aquí se ha perdido el hecho de que **toda** la subexpresión $x+1$ estaba elevada al cuadrado.

La sustitución no solo debe respetar el símbolo reemplazado. Debe respetar también todas las operaciones que actuaban sobre él y sobre las expresiones que lo contienen.

---

## Ejercicios

### Sustitución directa {#apm-i-e0016}

Evalúa cada expresión para el valor indicado.

#### a)

$$
3x+4,
\qquad x=2.
$$

#### b)

$$
5a-1,
\qquad a=0.
$$

#### c)

$$
2n+7,
\qquad n=-3.
$$

#### Solución

#### a)

Sustituimos:

$$
3x+4
=
3\cdot2+4.
$$

Entonces:

$$
3\cdot2+4
=
6+4
=
10.
$$

#### b)

Sustituimos:

$$
5a-1
=
5\cdot0-1.
$$

Por tanto:

$$
5\cdot0-1
=
-1.
$$

#### c)

Como $n=-3$, usamos paréntesis:

$$
2n+7
=
2(-3)+7.
$$

Entonces:

$$
2(-3)+7
=
-6+7
=
1.
$$

---

### Todas las apariciones {#apm-i-e0017}

Evalúa:

$$
x^2+4x+3
$$

cuando:

$$
x=2.
$$

Explica por qué hay que sustituir dos veces.

#### Solución

La letra $x$ aparece en:

$$
x^2
$$

y en:

$$
4x.
$$

Como:

$$
x=2,
$$

debemos reemplazar ambas apariciones:

$$
x^2+4x+3
\quad\longrightarrow\quad
2^2+4\cdot2+3.
$$

Evaluamos:

$$
2^2+4\cdot2+3
=
4+8+3
=
15.
$$

Hay que sustituir dos veces porque ambas apariciones del símbolo $x$ representan el mismo valor fijado para esta evaluación.

---

### El peligro del signo negativo {#apm-i-e0018}

Evalúa:

$$
x^2-2x
$$

cuando:

$$
x=-4.
$$

Después explica por qué sería incorrecto escribir:

$$
-4^2-2(-4).
$$

#### Solución

Sustituimos el valor completo $-4$ usando paréntesis:

$$
x^2-2x
\quad\longrightarrow\quad
(-4)^2-2(-4).
$$

Ahora calculamos:

$$
(-4)^2=16
$$

y:

$$
-2(-4)=8.
$$

Por tanto:

$$
(-4)^2-2(-4)
=
16+8
=
24.
$$

La escritura:

$$
-4^2
$$

no representa el cuadrado de $-4$.

Representa:

$$
-(4^2)=-16.
$$

Por eso eliminar los paréntesis cambiaría la estructura y produciría una evaluación incorrecta.

---

### Dos variables {#apm-i-e0019}

Evalúa:

$$
a^2+2ab+b^2
$$

cuando:

$$
a=3,
\qquad
b=-2.
$$

#### Solución

Sustituimos cada símbolo por su valor:

$$
a^2+2ab+b^2
\quad\longrightarrow\quad
3^2+2\cdot3(-2)+(-2)^2.
$$

Calculamos:

$$
3^2=9,
$$

$$
2\cdot3(-2)=-12,
$$

y:

$$
(-2)^2=4.
$$

Entonces:

$$
9-12+4
=
1.
$$

Por tanto, el valor es:

$$
\boxed{1}.
$$

---

### Sustituir una expresión {#apm-i-e0020}

En:

$$
x^2+3x
$$

sustituye:

$$
x=a-1.
$$

No expandas el resultado.

#### Solución

La letra $x$ aparece dos veces.

Reemplazamos cada aparición por la expresión completa $a-1$:

$$
x^2+3x
\quad\longrightarrow\quad
(a-1)^2+3(a-1).
$$

Como el ejercicio pide únicamente sustituir, nos detenemos:

$$
\boxed{(a-1)^2+3(a-1)}.
$$

No es necesario expandir.

---

### Detectar una sustitución incorrecta {#apm-i-e0021}

Un estudiante quiere sustituir:

$$
x=-2
$$

en:

$$
3x^2+1.
$$

Escribe:

$$
3(-2^2)+1.
$$

1. ¿Qué parte de la escritura es problemática?
2. Corrige la sustitución.
3. Evalúa correctamente.

#### Solución

#### 1. El problema

La potencia debe actuar sobre el valor completo de $x$.

El estudiante escribió:

$$
-2^2,
$$

que significa:

$$
-(2^2).
$$

#### 2. Sustitución correcta

Debemos escribir:

$$
3(-2)^2+1.
$$

#### 3. Evaluación

Tenemos:

$$
(-2)^2=4.
$$

Entonces:

$$
3(-2)^2+1
=
3\cdot4+1
=
13.
$$

La evaluación correcta es:

$$
\boxed{13}.
$$

---

### Sustitución o transformación {#apm-i-e0022}

Considera:

$$
4x-3
$$

y sustituye:

$$
x=a+b.
$$

Un estudiante escribe directamente:

$$
4a+4b-3.
$$

1. ¿Es correcta esa expresión final?
2. ¿Qué paso intermedio conviene escribir?
3. ¿Por qué es útil separar sustitución y transformación?

#### Solución

#### 1. La expresión final

Sí, la expresión:

$$
4a+4b-3
$$

puede obtenerse correctamente usando distributividad.

#### 2. Paso intermedio

Sin embargo, la sustitución propiamente dicha produce primero:

$$
4(a+b)-3.
$$

Después podemos transformar:

$$
4(a+b)-3
=
4a+4b-3.
$$

#### 3. Razón pedagógica

Separar las etapas permite comprobar dos cosas distintas:

- que hemos reemplazado correctamente $x$ por toda la expresión $a+b$;
- que la transformación posterior usa una ley válida.

Escribir todo de una vez puede ocultar dónde apareció un error.

---

## Resumen de la sección

En esta sección hemos introducido una operación básica del lenguaje algebraico: la sustitución.

La regla principal es:

$$
\boxed{
\text{sustituir}
=
\text{reemplazar un símbolo conservando la estructura}.
}
$$

Hemos aprendido que:

- hay que sustituir todas las apariciones relevantes del símbolo;
- los números negativos suelen requerir paréntesis;
- el cero se sustituye igual que cualquier otro valor;
- podemos sustituir varias letras a la vez;
- una variable puede sustituirse por una expresión completa;
- sustituir y simplificar son operaciones conceptualmente distintas.

La definición nueva es:

::: {.ma-block .ma-observacion}
**Síntesis**

**Evaluar una expresión** para valores dados consiste en sustituir esos valores en las apariciones correspondientes y, cuando sea posible, realizar las operaciones resultantes.
:::

El hábito que queremos conservar es:

$$
\boxed{
\text{primero sustituir correctamente}
\longrightarrow
\text{después calcular o transformar}.
}
$$

---

## Hacia la sección siguiente

Durante toda esta sección hemos escrito cadenas como:

$$
3\cdot2+4
=
6+4
=
10.
$$

También hemos escrito:

$$
(-3)^2+2(-3)+1
=
9-6+1
=
4.
$$

El signo

$$
=
$$

ha aparecido constantemente.

Pero todavía no nos hemos detenido a preguntar qué está afirmando.

¿Significa «ahora calculo»?

¿Significa «el resultado es»?

Si escribimos:

$$
3+4=7\cdot2=14,
$$

¿qué tiene de incorrecto, si tanto $3+4=7$ como $7\cdot2=14$ son cálculos correctos?

La próxima sección estará dedicada por completo a esa pregunta:

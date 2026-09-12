---
title: "Leyes de las operaciones y transformaciones justificadas"
description: "Tercer capítulo del Tomo I de Álgebra para matemáticos: leyes de la suma y el producto, inversos, distributividad, cancelación, equivalencia de expresiones y transformaciones reversibles de ecuaciones."
content-id: MA-BCH-0014
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C03
editorial-id: MA-BCH-APM-01-003
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
level: fundamental
topics:
  - leyes-de-las-operaciones
  - igualdad
  - inversos
  - distributividad
  - expresiones-equivalentes
  - ecuaciones
  - transformaciones-reversibles
  - cancelacion
  - dominio
prerequisites:
  - MA-BCH-0012
  - MA-BCH-0013
related:
  - MA-BOK-0006
  - MA-BCH-0012
  - MA-BCH-0013
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 3. Leyes de las operaciones y transformaciones justificadas

Los dos primeros capítulos enseñaron a leer el lenguaje algebraico: distinguir objetos, operaciones y relaciones; reconocer el papel de una variable; controlar el dominio; diferenciar una ecuación de una identidad.

Ahora aparece una pregunta más exigente.

Cuando escribimos

$2(x+3)=2x+6$,

¿por qué podemos reemplazar la primera expresión por la segunda?

Cuando pasamos de

$x+5=12$

a

$x=7$,

¿qué transformación hemos realizado y por qué conserva exactamente las soluciones?

Y cuando alguien «cancela» un factor, divide por una expresión o eleva ambos miembros al cuadrado, ¿cómo sabemos si el paso es reversible?

Este capítulo introduce una regla de trabajo que permanecerá durante toda la colección:

> **Una transformación algebraica no se acepta porque “se hace así”, sino porque existe una propiedad que la justifica bajo hipótesis precisas.**

El propósito no es volver lento el cálculo. Es construir una fluidez más profunda: poder transformar con rapidez **porque entendemos qué estamos haciendo**.

---

## 3.1. Una respuesta correcta puede contener un razonamiento incorrecto

Consideremos el siguiente intento de resolver $x+4=9$:

$$
\begin{aligned}
x+4&=9\\
x&=9-4\\
x&=5.
\end{aligned}
$$

El resultado es correcto. Pero la frase escolar «el $4$ pasa restando» oculta la transformación real. No hemos movido ningún objeto a través del signo igual. Hemos sumado $-4$ a ambos miembros:

$$
\begin{aligned}
x+4&=9\\
(x+4)+(-4)&=9+(-4)\\
x+(4+(-4))&=5\\
x+0&=5\\
x&=5.
\end{aligned}
$$

La primera cadena es una abreviación útil sólo cuando sabemos reconstruir la segunda.

Ahora observemos un razonamiento diferente:

$$
\begin{aligned}
x&=1\\
x^2&=1.
\end{aligned}
$$

El paso es válido: si $x=1$, entonces $x^2=1$. Pero el camino inverso no recupera la información original, porque $x^2=1$ también es cierto cuando $x=-1$.

Este contraste introduce dos preguntas que acompañarán todo el capítulo:

1. **¿el paso es válido?**
2. **¿el paso puede revertirse sin perder ni añadir posibilidades?**

Llegar a una respuesta correcta no basta para validar una cadena. Una solución matemática debe poder defender sus transformaciones.

---

## 3.2. La igualdad permite sustituir iguales por iguales

Si $A=B$, entonces $A$ y $B$ representan el mismo objeto o valor en el contexto considerado.

Por eso, cuando una operación está definida, podemos sustituir uno por otro.

Si $a=b$, entonces $a+c=b+c$.

Si $a=b$, entonces $ac=bc$.

Estas afirmaciones no dicen que sumar o multiplicar «mantenga la igualdad por magia». Dicen que aplicar la misma operación a dos objetos iguales produce nuevamente resultados iguales.

### Simetría y transitividad

También utilizaremos dos propiedades básicas de la igualdad.

Si $A=B$, entonces $B=A$.

Y si $A=B$ y $B=C$, entonces $A=C$.

Estas dos ideas hacen posible escribir cadenas como

$E_1=E_2=E_3$,

pero cada enlace debe ser correcto.

La cadena no significa «primero hago esto y después aquello». Afirma que todas las expresiones escritas representan el mismo valor.

### Igualdad no significa equivalencia de condiciones

Hay que distinguir dos situaciones.

En una cadena de **expresiones**, queremos mantener el mismo valor.

En una cadena de **ecuaciones**, queremos mantener el mismo conjunto de soluciones.

Esa distinción será decisiva más adelante en el capítulo.

---

## 3.3. Las leyes básicas de la suma y el producto

Trabajaremos principalmente con números racionales y reales, donde disponemos de suma y multiplicación con propiedades muy familiares.

La diferencia respecto de una presentación escolar es que ahora las propiedades se convierten en **herramientas explícitas de razonamiento**.

### Conmutatividad

Para números $a$ y $b$,

$a+b=b+a$

y

$ab=ba$.

La conmutatividad permite **intercambiar** el orden de dos términos o factores.

No permite reagrupar tres objetos. Para eso necesitamos otra propiedad.

### Asociatividad

Para números $a,b,c$,

$(a+b)+c=a+(b+c)$

y

$(ab)c=a(bc)$.

La asociatividad permite **reagrupar** sin cambiar el orden.

Por eso, cuando sólo intervienen sumas podemos escribir $a+b+c$ sin especificar paréntesis: cualquier agrupación produce el mismo resultado.

Lo mismo ocurre con un producto de varios factores.

### Elementos neutros

Existe un número $0$ tal que $a+0=a$ para todo $a$.

Existe un número $1$ tal que $a\cdot1=a$ para todo $a$.

El $0$ es el **neutro aditivo** y el $1$ es el **neutro multiplicativo**.

No son números especiales sólo por costumbre: cumplen funciones estructurales diferentes.

### Distributividad

La multiplicación se relaciona con la suma mediante

$a(b+c)=ab+ac$.

También tenemos $(a+b)c=ac+bc$, que puede verse como la misma ley combinada con conmutatividad.

La distributividad no es simplemente una regla para «sacar paréntesis». Es una relación profunda entre las dos operaciones.

---

### Intercambiar no es reagrupar

Uno de los errores conceptuales más frecuentes consiste en atribuir cualquier cambio de orden o paréntesis a una vaga «propiedad conmutativa».

Comparemos:

$a+(b+c)=(a+b)+c$

y

$a+b=b+a$.

En la primera igualdad no hemos intercambiado $a,b,c$. Conservamos el orden y cambiamos la agrupación. Usamos asociatividad.

En la segunda intercambiamos los dos sumandos. Usamos conmutatividad.

En una transformación larga pueden intervenir ambas.

Por ejemplo,

$$
\begin{aligned}
a+(b+c)
&=(a+b)+c && \text{[asociatividad]}\\
&=(b+a)+c && \text{[conmutatividad]}\\
&=b+(a+c) && \text{[asociatividad]}.
\end{aligned}
$$

La cadena es elemental, pero enseña una disciplina esencial: **nombrar la propiedad exacta**.

---

## 3.4. Inversos: deshacer una operación

Para cada número $a$ existe un número $-a$ tal que

$a+(-a)=0$.

Llamamos $-a$ **inverso aditivo** de $a$.

En cambio, si $a\neq0$, existe $a^{-1}$ tal que

$aa^{-1}=1$.

Llamamos $a^{-1}$ **inverso multiplicativo** de $a$.

### El cero marca una diferencia

El número $0$ tiene inverso aditivo: su inverso aditivo es él mismo, porque $0+0=0$.

Pero $0$ no tiene inverso multiplicativo.

Si existiera un número $u$ con $0u=1$, obtendríamos una contradicción con una propiedad que demostraremos pronto: $0u=0$ para cualquier $u$.

Por eso dividir por cero no es una operación permitida.

### Las hipótesis forman parte de la regla

La afirmación «todo número tiene inverso multiplicativo» es falsa.

La afirmación correcta, en $\mathbb Q$ o $\mathbb R$, es:

> Todo número **no nulo** tiene inverso multiplicativo.

La condición $a\neq0$ no es una nota al margen. Es parte de la afirmación matemática.

---

## 3.5. Resta y división como operaciones derivadas

La resta puede interpretarse mediante suma e inverso aditivo:

$a-b=a+(-b)$.

Esto permite explicar su comportamiento a partir de la suma.

Por ejemplo,

$a-(b+c)=a+(-(b+c))$.

Más adelante derivaremos cómo se distribuye el signo menos sobre una suma.

La división puede interpretarse mediante multiplicación e inverso:

$$
\frac ab=ab^{-1},\qquad b\neq0.
$$

Por tanto, toda regla que involucre división debe conservar visible la condición de que el divisor sea no nulo.

### Una ventaja conceptual

Al reducir resta y división a operaciones e inversos, disminuye la cantidad de reglas independientes que necesitamos memorizar.

En lugar de aprender muchas recetas, podemos reconstruirlas a partir de unas pocas propiedades.

---

## 3.6. Consecuencias que ya no deben memorizarse

### Primera consecuencia: $a\cdot0=0$

En muchas clases se aprende que «cualquier número por cero da cero».

Ahora lo demostraremos a partir de las leyes básicas.

Como $0+0=0$, tenemos

$a\cdot0=a(0+0)$.

Aplicando distributividad,

$a(0+0)=a\cdot0+a\cdot0$.

Así,

$a\cdot0=a\cdot0+a\cdot0$.

Sumamos el inverso aditivo de $a\cdot0$ a ambos miembros:

$$
\begin{aligned}
a\cdot0+(-(a\cdot0))
&=(a\cdot0+a\cdot0)+(-(a\cdot0))\\
0
&=a\cdot0+(a\cdot0+(-(a\cdot0)))\\
0
&=a\cdot0+0\\
0
&=a\cdot0.
\end{aligned}
$$

Por simetría de la igualdad,

$a\cdot0=0$.

Este argumento ilustra una idea central:

> una regla familiar puede ser una consecuencia necesaria de propiedades más fundamentales.

---

### Reglas de signos como consecuencias

#### El producto por un inverso aditivo

Queremos justificar $(-a)b=-(ab)$.

Observemos:

$$
\begin{aligned}
ab+(-a)b
&=(a+(-a))b && \text{[distributividad]}\\
&=0b && \text{[inverso aditivo]}\\
&=0. && \text{[$0b=0$]}
\end{aligned}
$$

Por definición de inverso aditivo, $(-a)b$ es el inverso aditivo de $ab$. Por tanto,

$(-a)b=-(ab)$.

De manera semejante,

$a(-b)=-(ab)$.

#### Menos por menos

Aplicando el resultado anterior,

$(-a)(-b)=-((-a)b)$.

Pero $(-a)b=-(ab)$, así que

$(-a)(-b)=-(-(ab))$.

Como el inverso aditivo del inverso de un número es el número original,

$(-a)(-b)=ab$.

«Menos por menos da más» deja así de ser una regla aislada. Es una consecuencia de distributividad, neutros e inversos.

#### El inverso del inverso

Como $a+(-a)=0$, también por conmutatividad $(-a)+a=0$.

Entonces $a$ es el inverso aditivo de $-a$. Por tanto,

$-(-a)=a$.

---

### Cancelación aditiva y multiplicativa

#### Cancelación aditiva

Si $a+c=b+c$, podemos sumar $-c$ a ambos miembros:

$$
\begin{aligned}
a+c&=b+c\\
(a+c)+(-c)&=(b+c)+(-c)\\
a&=b.
\end{aligned}
$$

No hemos «borrado $c$». Hemos aplicado una operación reversible.

#### Cancelación multiplicativa

Si $ac=bc$ y $c\neq0$, podemos multiplicar ambos miembros por $c^{-1}$:

$$
\begin{aligned}
ac&=bc\\
(ac)c^{-1}&=(bc)c^{-1}\\
a(cc^{-1})&=b(cc^{-1})\\
a&=b.
\end{aligned}
$$

La hipótesis $c\neq0$ es indispensable.

Si $c=0$, la igualdad $ac=bc$ se convierte en $0=0$, independientemente de los valores de $a$ y $b$. Ya no contiene información suficiente para concluir $a=b$.

---

## 3.7. Distributividad en ambos sentidos

La igualdad

$a(b+c)=ab+ac$

puede leerse de izquierda a derecha o de derecha a izquierda.

De izquierda a derecha solemos decir que **desarrollamos**.

De derecha a izquierda reconocemos un factor común y **factorizamos**:

$ab+ac=a(b+c)$.

No son dos leyes diferentes. Son dos usos de la misma igualdad.

### La dirección depende del objetivo

Si queremos calcular mentalmente $17\cdot101$, podemos escribir

$17(100+1)=1700+17=1717$.

Si queremos comprender $6x+6y$, la forma $6(x+y)$ hace visible el factor común.

Ninguna forma es absolutamente superior. La pregunta correcta es:

> ¿Qué forma hace visible la información que necesito?

---

## 3.8. Expresiones equivalentes y dominio

Recordemos las expresiones

$$
\frac{x^2-1}{x-1}
$$

y $x+1$.

Como $x^2-1=(x-1)(x+1)$, para $x\neq1$ obtenemos

$$
\frac{(x-1)(x+1)}{x-1}=x+1.
$$

Pero el valor $x=1$ estaba excluido de la expresión original.

La transformación no autoriza a olvidarlo.

Podemos decir que ambas expresiones producen el mismo valor para todo $x$ del dominio de la primera. No podemos decir sin más que tienen el mismo dominio natural.

### Preservar valores no implica preservar dominio

Ésta es una distinción central.

Una transformación puede:

- conservar valores donde ambas expresiones están definidas;
- cambiar la forma;
- ocultar restricciones;
- producir una nueva expresión definida en más puntos que la original.

La restricción debe viajar con el razonamiento.

---

## 3.9. Transformar una ecuación no es lo mismo que transformar una expresión

En una expresión buscamos conservar un valor.

En una ecuación queremos conservar las soluciones.

Consideremos

$x+5=12$.

Sumar $-5$ a ambos miembros produce

$x=7$.

El paso es reversible: desde $x=7$ podemos sumar $5$ a ambos miembros y recuperar $x+5=12$.

Por tanto, las dos ecuaciones tienen exactamente las mismas soluciones.

### Multiplicar por un número no nulo

Si $A=B$ y $c\neq0$, entonces $cA=cB$.

Y desde $cA=cB$ podemos volver a $A=B$ multiplicando por $c^{-1}$.

Por eso el paso es reversible.

### Multiplicar por cero

Si multiplicamos $x=1$ por $0$, obtenemos $0=0$.

La ecuación original tenía una sola solución. La nueva igualdad es verdadera para cualquier $x$.

La transformación perdió toda la información.

---

## 3.10. Transformaciones reversibles y transformaciones que pierden información

Si $x=1$, entonces $x^2=1$.

Pero de $x^2=1$ no se sigue únicamente $x=1$; también $x=-1$ satisface la nueva ecuación.

Elevar al cuadrado puede introducir soluciones adicionales.

Otro ejemplo: si $x=2$, entonces $(x-2)(x+5)=0$.

Pero la ecuación $(x-2)(x+5)=0$ también admite $x=-5$.

### La pregunta correcta

Cuando transformamos una ecuación debemos preguntar:

> ¿Puedo regresar desde la nueva ecuación a la anterior sin imponer información adicional?

Si la respuesta es sí, tenemos una transformación reversible.

Si la respuesta es no, debemos tratar la nueva condición con cautela y verificar las soluciones obtenidas.

La lógica formal de estas relaciones llegará más adelante. Por ahora basta reconocer la asimetría.

---

### Dividir por una expresión exige saber que no es cero

Supongamos que tenemos

$x(x-1)=0$.

Si dividimos por $x$, obtendríamos $x-1=0$ y concluiríamos $x=1$.

Pero hemos perdido la solución $x=0$.

El paso «dividir por $x$» sólo sería reversible bajo la hipótesis $x\neq0$.

Como esa hipótesis no formaba parte del problema, la división no es legítima si pretendemos conservar todas las soluciones.

### Regla de trabajo

Antes de dividir por una expresión $E$, preguntar:

> ¿Sé que $E\neq0$?

Si no lo sabemos, la división puede eliminar casos importantes.

Esta pregunta reaparecerá constantemente en ecuaciones, polinomios, matrices y estructuras abstractas.

---

## 3.11. Cancelar no significa borrar símbolos

Consideremos

$$
\frac{x(x+2)}{x},\qquad x\neq0.
$$

Como $x$ es un factor común no nulo,

$$
\frac{x(x+2)}{x}=x+2.
$$

Pero en

$$
\frac{x+2}{x}
$$

el símbolo $x$ no es factor de todo el numerador. No podemos «tacharlo» con el denominador.

De hecho,

$$
\frac{x+2}{x}=\frac{x}{x}+\frac2x=1+\frac2x,\qquad x\neq0.
$$

La cancelación es una consecuencia de multiplicar por un inverso. Por eso actúa sobre **factores**, no sobre términos separados por suma o resta.

### Un buen diagnóstico visual no basta

Que dos símbolos se parezcan o aparezcan «arriba y abajo» no autoriza una cancelación.

La pregunta debe ser:

> ¿Existe realmente un factor común y es no nulo en el dominio considerado?

---

## 3.12. Cadenas justificadas: escribir álgebra como argumento

Una cadena algebraica puede leerse como una demostración en miniatura.

Por ejemplo, para justificar $-(a+b)=(-a)+(-b)$ podemos mostrar que $(-a)+(-b)$ es el inverso aditivo de $a+b$:

$$
\begin{aligned}
(a+b)+((-a)+(-b))
&=((a+b)+(-a))+(-b)\\
&=(a+(b+(-a)))+(-b)\\
&=(a+((-a)+b))+(-b)\\
&=((a+(-a))+b)+(-b)\\
&=(0+b)+(-b)\\
&=b+(-b)\\
&=0.
\end{aligned}
$$

Cada paso puede asociarse con una propiedad: asociatividad, conmutatividad, neutro o inverso.

### Cuánto detalle escribir

Al comienzo conviene hacer visibles más pasos.

Con la práctica, una cadena puede comprimirse. Pero la compresión es legítima sólo cuando el lector podría reconstruir los pasos omitidos.

La meta no es escribir siempre la versión más larga. La meta es poder defenderla.

---

## 3.13. Diagnóstico: encontrar el primer paso inválido

Consideremos:

$$
\begin{aligned}
x^2&=x\\
x^2-x&=0\\
x(x-1)&=0\\
x-1&=0\\
x&=1.
\end{aligned}
$$

La conclusión omite una solución.

¿Dónde aparece el primer problema?

Los tres primeros pasos son válidos.

El paso

$x(x-1)=0 \to x-1=0$

equivale a dividir por $x$ sin saber que $x\neq0$.

Precisamente allí se pierde la solución $x=0$.

### Diagnosticar mejor que etiquetar

No basta decir «la solución está mala».

Un diagnóstico matemático debe poder señalar:

1. el primer paso incorrecto;
2. la propiedad que se intentó usar;
3. la hipótesis faltante;
4. qué información se perdió o añadió;
5. cómo reparar el razonamiento.

Este modo de leer errores será esencial en demostraciones posteriores.

---

## 3.14. Cierre — protocolo de transformación justificada

Antes de transformar, preguntar:

1. **¿Qué estoy transformando?** ¿Una expresión o una ecuación?
2. **¿Cuál es el dominio?**
3. **¿Qué valores están excluidos?**
4. **¿Qué propiedad autoriza el paso?**
5. **¿La propiedad exige una hipótesis?**
6. **¿El paso conserva el valor?**
7. **Si es una ecuación, conserva exactamente las soluciones?**
8. **¿El paso puede revertirse?**
9. **¿La nueva forma sirve al objetivo?**
10. **¿Puedo reconstruir la justificación si he abreviado?**

Éste es el nuevo estándar algebraico.

No basta con mover símbolos hasta obtener una forma familiar.

> **Transformar algebraicamente es reemplazar expresiones o condiciones mediante pasos cuya validez puede defenderse.**

---

# Ejercicios

Todos los ejercicios son originales para *Álgebra para matemáticos*, calibrados con el corpus universitario y las fuentes rectoras del capítulo.

## A. Identificar la propiedad

1. Indica qué propiedad justifica $a+b=b+a$.

2. Indica qué propiedad justifica $(ab)c=a(bc)$.

3. Indica qué propiedad justifica $a+0=a$.

4. Indica qué propiedad justifica $a(b+c)=ab+ac$.

5. Explica por qué pasar de $a+(b+c)$ a $(a+b)+c$ no usa conmutatividad.

6. En la cadena $a+(b+c)=(a+b)+c=(b+a)+c$, identifica la propiedad usada en cada paso.

## B. Neutros e inversos

7. Explica la diferencia entre $0$ como neutro aditivo y $-a$ como inverso aditivo de $a$.

8. Explica la diferencia entre $1$ como neutro multiplicativo y $a^{-1}$ como inverso multiplicativo de $a$.

9. ¿Cuál es el inverso aditivo de $0$? Justifica.

10. ¿Por qué la frase «todo número real tiene inverso multiplicativo» es falsa?

11. Si $a\neq0$, completa y justifica: $a\cdot(\ \ )=1$.

12. Reescribe $a-b$ usando sólo suma e inverso aditivo, y $\frac ab$ usando producto e inverso multiplicativo.

## C. Consecuencias derivadas

13. Demuestra que $0a=0$ para todo número real $a$.

14. Demuestra que $-(-a)=a$.

15. Demuestra que $(-a)b=-(ab)$.

16. Demuestra que $a(-b)=-(ab)$.

17. Deduce que $(-a)(-b)=ab$.

18. Demuestra que $-(a+b)=(-a)+(-b)$.

## D. Conmutatividad, asociatividad y distributividad

19. Justifica cada paso:
$$
\begin{aligned}
a+(b+c)
&=(a+b)+c\\
&=(b+a)+c\\
&=b+(a+c).
\end{aligned}
$$

20. Transforma $3(x+4)$ en $3x+12$ e identifica la propiedad.

21. Transforma $7x+7y$ en una forma factorizada e identifica la propiedad usada en sentido inverso.

22. Explica por qué $(a+b)^2=a^2+b^2$ no se deduce de distributividad.

23. Desarrolla correctamente $(a+b)^2$ justificando la estructura del cálculo.

24. Elige una forma más útil para calcular mentalmente $19\cdot101$ y explica tu elección.

## E. Cancelación

25. A partir de $a+c=b+c$, deriva $a=b$ justificando cada paso.

26. A partir de $ac=bc$ con $c\neq0$, deriva $a=b$.

27. Explica por qué no puede omitirse $c\neq0$ en el ejercicio anterior.

28. Simplifica $\frac{x(x+5)}x$ indicando el dominio.

29. Explica por qué $\frac{x+5}{x}$ no permite cancelar $x$.

30. Corrige el razonamiento falso $\frac{2x+6}{2}=x+6$.

## F. Dominio y expresiones equivalentes

31. Compara $\frac{x^2-9}{x-3}$ y $x+3$. Indica el dominio de cada expresión y dónde coinciden.

32. Simplifica $\frac{x^2+2x}{x}$ conservando la restricción original.

33. Explica por qué $\frac{x^2+2x}{x}$ y $x+2$ no tienen el mismo dominio natural.

34. Construye dos expresiones que coincidan donde la primera está definida, pero cuyos dominios naturales sean diferentes.

35. Determina la restricción necesaria para $\frac{(x-4)(x+1)}{x-4}=x+1$.

36. Un estudiante sustituye $x=4$ después de simplificar el ejercicio anterior. Explica exactamente el error.

## G. Transformaciones de ecuaciones

37. Explica por qué sumar $5$ a ambos miembros de una ecuación es reversible.

38. Explica por qué multiplicar ambos miembros por $7$ es reversible.

39. Explica por qué multiplicar ambos miembros por $0$ no es reversible.

40. Da un ejemplo donde elevar ambos miembros al cuadrado introduzca una solución adicional.

41. Analiza el paso de $x=3$ a $(x-3)(x+2)=0$. ¿Es válido? ¿Es reversible?

42. Explica la diferencia entre «el paso es válido» y «el paso es reversible».

## H. Dividir y perder soluciones

43. Encuentra el primer paso inválido:
$$
\begin{aligned}
x^2&=2x\\
x^2-2x&=0\\
x(x-2)&=0\\
x-2&=0\\
x&=2.
\end{aligned}
$$

44. Repara el argumento anterior para obtener todas las soluciones.

45. En $x(x+4)=x(x-1)$, explica por qué dividir inmediatamente por $x$ requiere separar un caso.

46. Resuelve la ecuación anterior sin perder soluciones y señala en qué momento controlas el caso $x=0$.

47. Da un ejemplo de una ecuación donde dividir por una expresión variable elimine una solución.

48. Formula en palabras una regla segura antes de dividir ambos miembros por una expresión que contiene la incógnita.

## I. Diagnóstico de razonamientos

49. Localiza el primer error:
$$
\begin{aligned}
2(x+3)&=2x+3\\
&=2x+6.
\end{aligned}
$$

50. Localiza el primer error:
$$
\begin{aligned}
\frac{x+2}{x}
&=\frac{x}{x}+2\\
&=1+2\\
&=3.
\end{aligned}
$$

51. Localiza el primer error:
$$
\begin{aligned}
x^2&=4\\
x&=2.
\end{aligned}
$$

52. Localiza el primer error:
$$
\begin{aligned}
a+(b+c)&=(b+a)+c.
\end{aligned}
$$
Un estudiante afirma que el único paso se justifica por conmutatividad. ¿Qué falta en su explicación?

53. Repara la cadena $3+5=8\cdot2=16$ para que exprese correctamente dos cálculos sucesivos.

54. Construye una secuencia de tres transformaciones que parta de una afirmación verdadera, contenga un paso inválido y termine nuevamente en una afirmación verdadera. Explica por qué el resultado final correcto no salva el razonamiento.

55. Construye una cadena justificada de **al menos ocho transformaciones** que lleve $-(a-(b-c))$ hasta una forma sin paréntesis anidados. Usa sólo la definición de resta, reglas de inversos, asociatividad y conmutatividad de la suma.

56. Desarrolla $(a-b)(c-d)$ hasta obtener $ac-ad-bc+bd$ mediante una cadena de **al menos ocho transformaciones explícitas**, interpretando cada resta como suma de un inverso y justificando distributividad y reglas de signos.

57. Resuelve $3(2x-5)-4(x+1)=5(x-2)+7$ mediante una cadena de **8–15 transformaciones reversibles**. Justifica las transformaciones estructurales y verifica la solución en la ecuación original.

58. Resuelve $\frac{2x-1}{3}-\frac{x+2}{4}=\frac{x-5}{6}+1$ mediante una cadena de **8–15 transformaciones reversibles**. Explica por qué el número usado para eliminar denominadores es seguro y verifica la solución.

59. Audita la siguiente cadena: indica cuáles pasos son reversibles y cuál puede añadir soluciones.
$$
\begin{aligned}
x-1&=2\\
(x-1)^2&=4\\
x^2-2x+1&=4\\
x^2-2x-3&=0.
\end{aligned}
$$
Luego determina qué soluciones de la ecuación final satisfacen la ecuación inicial.

60. Escribe una explicación matemática de 8–12 líneas que responda: **¿por qué una transformación algebraica es una forma de razonamiento y no sólo una manipulación de símbolos?** Debes mencionar propiedad, hipótesis, dominio, reversibilidad y conservación de información.

---

# Soluciones

## A. Identificar la propiedad

### 1
La igualdad $a+b=b+a$ expresa la **conmutatividad de la suma**: intercambiar el orden de los sumandos no cambia el resultado.

### 2
$(ab)c=a(bc)$ expresa la **asociatividad del producto**: cambia la agrupación, no el orden de los factores.

### 3
$a+0=a$ usa la propiedad del **neutro aditivo**.

### 4
$a(b+c)=ab+ac$ es la **distributividad** del producto respecto de la suma.

### 5
En $a+(b+c)=(a+b)+c$ el orden $a,b,c$ permanece. Sólo cambian los paréntesis. Por tanto, la propiedad es asociatividad, no conmutatividad.

### 6
Primer paso: asociatividad de la suma.

Segundo paso: conmutatividad de $a$ y $b$.

## B. Neutros e inversos

### 7
El número $0$ es un único objeto que deja inalterado a cualquier $a$ bajo suma: $a+0=a$. En cambio, $-a$ depende de $a$ y satisface $a+(-a)=0$. Uno es neutro; el otro deshace aditivamente a un elemento concreto.

### 8
El número $1$ deja inalterado a cualquier $a$ bajo producto: $a\cdot1=a$. El inverso $a^{-1}$ depende de $a$ y, si $a\neq0$, satisface $aa^{-1}=1$.

### 9
El inverso aditivo de $0$ es $0$, porque $0+0=0$, que es precisamente la condición para ser inverso aditivo de $0$.

### 10
Es falsa porque $0$ no tiene inverso multiplicativo. No existe un real $u$ tal que $0u=1$.

### 11
Debe escribirse $a\cdot a^{-1}=1$, con la hipótesis $a\neq0$.

### 12
$a-b=a+(-b)$.

Si $b\neq0$, $\frac ab=ab^{-1}$.

## C. Consecuencias derivadas

### 13
Como $0=0+0$,

$$
0a=(0+0)a=0a+0a.
$$

Sumamos el inverso aditivo de $0a$ a ambos miembros. Se obtiene $0=0a$, y por simetría $0a=0$.

### 14
Por definición, $a+(-a)=0$. Por conmutatividad, $(-a)+a=0$. Así, $a$ es el inverso aditivo de $-a$. Por tanto $-(-a)=a$.

### 15
Calculamos

$$
ab+(-a)b=(a+(-a))b=0b=0.
$$

Entonces $(-a)b$ es el inverso aditivo de $ab$, por lo que $(-a)b=-(ab)$.

### 16
De modo análogo,

$$
ab+a(-b)=a(b+(-b))=a0=0.
$$

Por tanto, $a(-b)=-(ab)$.

### 17
Aplicamos el resultado anterior:

$$
(-a)(-b)=-((-a)b).
$$

Pero $(-a)b=-(ab)$, así que

$$
(-a)(-b)=-(-(ab))=ab.
$$

### 18
Basta mostrar que $(-a)+(-b)$ es el inverso de $a+b$:

$$
\begin{aligned}
(a+b)+((-a)+(-b))
&=a+(b+(-a))+(-b)\\
&=a+((-a)+b)+(-b)\\
&=(a+(-a))+b+(-b)\\
&=0+0\\
&=0.
\end{aligned}
$$

Así, $-(a+b)=(-a)+(-b)$.

## D. Conmutatividad, asociatividad y distributividad

### 19
$$
\begin{aligned}
a+(b+c)
&=(a+b)+c && \text{[asociatividad]}\\
&=(b+a)+c && \text{[conmutatividad]}\\
&=b+(a+c) && \text{[asociatividad]}.
\end{aligned}
$$

### 20
Por distributividad,

$3(x+4)=3x+3\cdot4=3x+12$.

### 21
Usando distributividad en sentido inverso,

$7x+7y=7(x+y)$.

### 22
La distributividad exige multiplicar cada término del segundo factor. Como $(a+b)^2=(a+b)(a+b)$, aparecen cuatro productos, no sólo dos.

### 23
$$
\begin{aligned}
(a+b)^2
&=(a+b)(a+b)\\
&=a(a+b)+b(a+b)\\
&=a^2+ab+ba+b^2\\
&=a^2+2ab+b^2.
\end{aligned}
$$

La última igualdad usa conmutatividad del producto y suma de términos iguales.

### 24
$19\cdot101=19(100+1)=1900+19=1919$.

La forma $19(100+1)$ hace visible la distributividad y permite cálculo mental inmediato.

## E. Cancelación

### 25
$$
\begin{aligned}
a+c&=b+c\\
(a+c)+(-c)&=(b+c)+(-c)\\
a+(c+(-c))&=b+(c+(-c))\\
a+0&=b+0\\
a&=b.
\end{aligned}
$$

### 26
Como $c\neq0$, existe $c^{-1}$:

$$
\begin{aligned}
ac&=bc\\
(ac)c^{-1}&=(bc)c^{-1}\\
a(cc^{-1})&=b(cc^{-1})\\
a&=b.
\end{aligned}
$$

### 27
Si $c=0$, entonces $ac=bc$ se reduce a $0=0$ para cualesquiera $a,b$. Por ejemplo, $2\cdot0=5\cdot0$, pero $2\neq5$.

### 28
El dominio original exige $x\neq0$. Para esos valores,

$$
\frac{x(x+5)}x=x+5.
$$

La respuesta debe conservar $x\neq0$.

### 29
En $x+5$, $x$ es un término de una suma, no un factor común de todo el numerador. No existe una cancelación multiplicativa que permita borrarlo.

### 30
La división correcta es

$$
\frac{2x+6}{2}=\frac{2x}{2}+\frac62=x+3.
$$

También puede factorizarse el numerador: $\frac{2(x+3)}2=x+3$.

## F. Dominio y expresiones equivalentes

### 31
$\frac{x^2-9}{x-3}$ está definida para $x\neq3$. $x+3$ está definida para todo real.

Como $x^2-9=(x-3)(x+3)$, coinciden para todo $x\neq3$.

### 32
El dominio original exige $x\neq0$.

$$
\frac{x^2+2x}{x}
=\frac{x(x+2)}x
=x+2,\qquad x\neq0.
$$

### 33
$x+2$ está definida en $x=0$, mientras la expresión original tiene denominador $x$ y no está definida allí.

### 34
Ejemplo: $\frac{x^2-1}{x-1}$ y $x+1$. Coinciden para $x\neq1$, pero sólo la segunda está definida en $x=1$.

### 35
La igualdad

$$
\frac{(x-4)(x+1)}{x-4}=x+1
$$

requiere $x\neq4$.

### 36
Al simplificar se obtiene una expresión escrita que sí puede evaluarse en $x=4$, pero ese valor no pertenecía al dominio de la expresión original. La simplificación no autoriza a ampliar retrospectivamente el dominio del problema.

## G. Transformaciones de ecuaciones

### 37
Si sumamos $5$ a ambos miembros y luego sumamos $-5$, recuperamos la ecuación original. La operación tiene una inversa y, por tanto, el paso es reversible.

### 38
Multiplicar por $7$ es reversible porque $7\neq0$ y existe $1/7$. Podemos multiplicar después por $1/7$ para recuperar la ecuación original.

### 39
Multiplicar por $0$ convierte cualquier igualdad en $0=0$. Se pierde la información que distinguía unas soluciones de otras. No existe inverso multiplicativo de $0$.

### 40
De $x=2$ se sigue $x^2=4$. Pero $x^2=4$ también admite $x=-2$. El cuadrado introdujo una posibilidad adicional.

### 41
El paso es válido: si $x=3$, entonces $x-3=0$ y el producto vale $0$. Pero no es reversible, porque $(x-3)(x+2)=0$ también admite $x=-2$.

### 42
Un paso válido garantiza que toda solución de la condición original satisface la nueva. Un paso reversible garantiza además el regreso: toda solución de la nueva satisface la original. Sólo en el segundo caso se conserva exactamente la información.

## H. Dividir y perder soluciones

### 43
Los tres primeros pasos son válidos. El primer paso inválido es

$x(x-2)=0\to x-2=0$,

porque equivale a dividir por $x$ sin saber que $x\neq0$. Se pierde $x=0$.

### 44
Desde $x(x-2)=0$, un producto de reales es cero cuando al menos uno de los factores es cero. Por tanto,

$x=0$ o $x-2=0$,

y las soluciones son $x=0$ y $x=2$.

### 45
Si dividimos por $x$, necesitamos $x\neq0$. Pero $x=0$ puede ser una solución y debe verificarse separadamente antes de imponer esa condición.

### 46
La ecuación es

$x(x+4)=x(x-1)$.

Llevamos todo a un miembro:

$$
x[(x+4)-(x-1)]=0.
$$

Entonces

$x\cdot5=0$,

de donde $x=0$.

Si se desea dividir por $x$, primero habría que separar el caso $x=0$; precisamente ese caso resulta ser la solución.

### 47
Ejemplo: $x(x-3)=0$. Dividir por $x$ produce $x-3=0$ y elimina la solución $x=0$.

### 48
Regla segura: antes de dividir por una expresión que contiene la incógnita, determinar si puede ser cero. Si puede serlo, separar ese caso o usar otro método que no lo elimine.

## I. Diagnóstico de razonamientos

### 49
El primer paso ya es incorrecto:

$2(x+3)\neq2x+3$.

La distributividad exige multiplicar ambos términos: $2(x+3)=2x+6$.

### 50
El primer paso es incorrecto:

$$
\frac{x+2}{x}\neq\frac{x}{x}+2.
$$

Al separar una fracción, ambos términos del numerador conservan el mismo denominador:

$$
\frac{x+2}{x}=\frac{x}{x}+\frac2x.
$$

### 51
El paso $x^2=4\to x=2$ pierde la solución $x=-2$. No es una transformación reversible.

### 52
La igualdad es correcta, pero no se obtiene sólo por conmutatividad. Una justificación detallada es:

$$
a+(b+c)=(a+b)+c=(b+a)+c.
$$

Primero se usa asociatividad y luego conmutatividad.

### 53
Una escritura correcta es:

$3+5=8$.

Luego:

$8\cdot2=16$.

No debe escribirse una sola cadena porque $8\neq16$.

### 54
Un ejemplo es comenzar con $x=1$:

$$
\begin{aligned}
x&=1 && \text{[afirmación inicial]}\\
x^2&=1 && \text{[paso válido: elevar al cuadrado]}\\
x&=-1 && \text{[paso inválido]}\\
x^2&=1 && \text{[consecuencia de la línea anterior]}.
\end{aligned}
$$

La última igualdad es verdadera cuando la afirmación inicial $x=1$ es verdadera, pero el paso $x^2=1\to x=-1$ no está justificado: de $x^2=1$ se obtienen dos posibilidades, $x=1$ y $x=-1$. El hecho de terminar en una afirmación verdadera no repara el razonamiento roto.

## J. Cadenas largas y síntesis

### 55
Una cadena posible es:

$$
\begin{aligned}
-(a-(b-c))
&=-(a+(-(b-c))) && \text{[definición de resta]}\\
&=(-a)+(-(-(b-c))) && \text{[inverso de una suma]}\\
&=(-a)+(b-c) && \text{[doble inverso]}\\
&=(-a)+(b+(-c)) && \text{[definición de resta]}\\
&=((-a)+b)+(-c) && \text{[asociatividad]}\\
&=(b+(-a))+(-c) && \text{[conmutatividad]}\\
&=b+((-a)+(-c)) && \text{[asociatividad]}\\
&=b+(-(a+c)) && \text{[inverso de una suma, sentido inverso]}\\
&=b-(a+c). && \text{[definición de resta]}
\end{aligned}
$$

También es legítimo detenerse en $-a+b-c$. La cadena muestra que una expresión con varias restas puede reconstruirse usando sólo suma e inversos.

### 56
Interpretamos las restas mediante inversos:

$$
\begin{aligned}
(a-b)(c-d)
&=(a+(-b))(c+(-d)) && \text{[definición de resta]}\\
&=a(c+(-d))+(-b)(c+(-d)) && \text{[distributividad]}\\
&=ac+a(-d)+(-b)(c+(-d)) && \text{[distributividad]}\\
&=ac+a(-d)+((-b)c+(-b)(-d)) && \text{[distributividad]}\\
&=ac+(-(ad))+((-b)c+(-b)(-d)) && \text{[regla de signo]}\\
&=ac+(-(ad))+((-(bc))+(-b)(-d)) && \text{[regla de signo]}\\
&=ac+(-(ad))+((-(bc))+bd) && \text{[menos por menos, derivado]}\\
&=(ac+(-(ad)))+((-(bc))+bd) && \text{[asociatividad]}\\
&=ac-ad-bc+bd. && \text{[notación de resta]}
\end{aligned}
$$

La cadena no usa «FOIL» como regla independiente: todo proviene de distributividad e inversos.

### 57
Partimos de

$$
3(2x-5)-4(x+1)=5(x-2)+7.
$$

Una cadena reversible es:

$$
\begin{aligned}
3(2x-5)-4(x+1)
&=5(x-2)+7\\
6x-15-4(x+1)
&=5(x-2)+7 && \text{[distributividad]}\\
6x-15-4x-4
&=5(x-2)+7 && \text{[distributividad]}\\
2x-19
&=5(x-2)+7 && \text{[reagrupar y reducir]}\\
2x-19
&=5x-10+7 && \text{[distributividad]}\\
2x-19
&=5x-3 && \text{[reducir]}\\
-19
&=3x-3 && \text{[sumar $-2x$ a ambos lados]}\\
-16
&=3x && \text{[sumar $3$ a ambos lados]}\\
-\frac{16}{3}
&=x && \text{[multiplicar por $1/3$]}.
\end{aligned}
$$

El último paso es reversible porque $3\neq0$.

Verificación:

$$
3\left(2\left(-\frac{16}{3}\right)-5\right)-4\left(-\frac{16}{3}+1\right)
=
5\left(-\frac{16}{3}-2\right)+7
=
-\frac{89}{3}.
$$

### 58
La ecuación es

$$
\frac{2x-1}{3}-\frac{x+2}{4}=\frac{x-5}{6}+1.
$$

El mínimo común múltiplo de $3,4,6$ es $12$. Como $12\neq0$, multiplicar ambos miembros por $12$ es reversible:

$$
\begin{aligned}
\frac{2x-1}{3}-\frac{x+2}{4}
&=\frac{x-5}{6}+1\\
4(2x-1)-3(x+2)
&=2(x-5)+12\\
8x-4-3(x+2)
&=2(x-5)+12 && \text{[distributividad]}\\
8x-4-3x-6
&=2(x-5)+12 && \text{[distributividad]}\\
5x-10
&=2(x-5)+12 && \text{[reducir]}\\
5x-10
&=2x-10+12 && \text{[distributividad]}\\
5x-10
&=2x+2 && \text{[reducir]}\\
3x-10
&=2 && \text{[sumar $-2x$]}\\
3x
&=12 && \text{[sumar $10$]}\\
x
&=4. && \text{[multiplicar por $1/3$]}
\end{aligned}
$$

Verificación:

$$
\frac{8-1}{3}-\frac{4+2}{4}
=\frac73-\frac32
=\frac56,
$$

mientras

$$
\frac{4-5}{6}+1=-\frac16+1=\frac56.
$$

### 59
La primera transformación

$x-1=2\to(x-1)^2=4$

es válida pero no reversible: al elevar al cuadrado puede añadirse la posibilidad $x-1=-2$.

Los pasos posteriores son identidades o sumas de la misma cantidad y preservan las soluciones de la ecuación ya ampliada.

La ecuación final es

$x^2-2x-3=0=(x-3)(x+1)$,

con soluciones $x=3$ y $x=-1$.

La ecuación inicial $x-1=2$ sólo admite $x=3$. Por tanto, $x=-1$ es la solución adicional introducida por el cuadrado.

### 60
Respuesta modelo:

Una transformación algebraica es una forma de razonamiento porque cada cambio de escritura afirma algo que debe ser matemáticamente válido. Para pasar de una expresión a otra necesitamos una propiedad, como asociatividad o distributividad; para transformar una ecuación debemos además controlar si conservamos exactamente sus soluciones. Las hipótesis son parte del proceso: dividir por una cantidad exige saber que no es cero. El dominio determina qué operaciones están definidas y qué valores están excluidos. Algunas transformaciones son reversibles y permiten recuperar la condición anterior; otras sólo funcionan en una dirección y pueden añadir o eliminar posibilidades. Por eso una cadena algebraica no es simplemente un movimiento de símbolos: es una secuencia de afirmaciones cuya información y validez deben poder defenderse.

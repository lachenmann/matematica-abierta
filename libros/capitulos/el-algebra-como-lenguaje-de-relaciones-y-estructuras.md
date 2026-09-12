---
title: "El álgebra como lenguaje de relaciones y estructuras"
description: "Primer capítulo del Tomo I de Álgebra para matemáticos: del cálculo concreto al pensamiento algebraico mediante objetos, operaciones, relaciones, patrones, representaciones, invariantes y generalización."
content-id: MA-BCH-0012
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C01
editorial-id: MA-BCH-APM-01-001
status: published
date-created: 2026-09-12
date-modified: 2026-09-12
areas:
  - algebra
  - fundamentos
level: fundamental
topics:
  - pensamiento-algebraico
  - operaciones
  - relaciones
  - patrones
  - estructura
  - invariantes
  - representaciones
  - generalizacion
  - contraejemplos
prerequisites: []
related:
  - MA-BOK-0006
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# 1. El álgebra como lenguaje de relaciones y estructuras

## 1.1. Una operación puede convertirse en objeto de estudio

Hay una diferencia entre **hacer una cuenta** y **estudiar una cuenta**.

Si calculamos $27+15$, obtenemos $42$. Si calculamos $15+27$, obtenemos también $42$. Hasta aquí no hay nada sorprendente. Sin embargo, en cuanto comparamos ambos cálculos aparece otra pregunta:

> ¿Qué cambio hicimos y qué permaneció sin cambiar?

Cambiamos el orden de los números. El resultado permaneció.

Probemos ahora con una resta: $27-15=12$, pero $15-27=-12$. El mismo cambio —intercambiar los dos números— ya no conserva el resultado.

La diferencia importante no está en que una cuenta sea más difícil que otra. Está en que hemos dejado de preguntar únicamente **cuál es el resultado**. Ahora preguntamos **cómo se comporta una operación cuando modificamos sus entradas**.

Ese desplazamiento es uno de los comienzos del pensamiento algebraico.

En la aritmética elemental, una expresión como $27+15$ suele aparecer como una tarea que debe terminar en un número. En álgebra, la expresión puede convertirse también en un objeto que comparamos con otras expresiones. Podemos preguntar qué transformaciones modifican su valor, cuáles no lo modifican y qué regularidades se repiten en muchos casos.

Esto no significa que el cálculo deje de importar. Significa que el cálculo adquiere una segunda función: además de producir respuestas, puede producir **evidencia** sobre una pauta más general.

### Un primer cambio de mirada

Consideremos los pares

- $9+14$ y $14+9$;
- $6\cdot 11$ y $11\cdot 6$;
- $18-5$ y $5-18$;
- $20/4$ y $4/20$.

Podemos calcular todos los resultados. Pero la pregunta algebraicamente interesante es otra: ¿qué operaciones parecen conservar el resultado cuando intercambiamos los términos y cuáles no?

Todavía no necesitamos poner un nombre técnico a esa propiedad. El objetivo es aprender a detectarla.

En capítulos posteriores estudiaremos de manera sistemática las leyes que justifican este tipo de observaciones. Aquí sólo queremos adquirir el hábito de mirar una operación como algo que **tiene comportamiento**.

---

## 1.2. De muchos casos a una sola pregunta

Supongamos que observamos

$4+7=7+4$, $12+5=5+12$ y $103+8=8+103$.

Podemos continuar con cientos de ejemplos. En algún momento, sin embargo, seguir calculando deja de ser la mejor forma de expresar lo que estamos observando.

La notación algebraica permite formular de una vez la pregunta:

> Si $a$ y $b$ son números del contexto que estamos estudiando, ¿se cumple siempre $a+b=b+a$?

Aquí las letras no aparecen necesariamente como incógnitas que debamos descubrir. Sirven para mantener abiertos muchos casos posibles.

Éste es uno de los cambios más importantes entre una lectura escolar estrecha del álgebra y una lectura matemática más amplia. Una letra puede representar:

- un valor que queremos determinar;
- un valor arbitrario;
- un parámetro que controla una familia de objetos;
- una entrada que puede variar.

Precisaremos esas funciones en el capítulo siguiente. Por ahora basta entender que el simbolismo permite **comprimir una familia de situaciones**.

### Caso, regularidad y conjetura

Observemos ahora los números

$2$, $6$, $12$, $20$, $30$.

Podemos reconocerlos como

$1\cdot2$, $2\cdot3$, $3\cdot4$, $4\cdot5$, $5\cdot6$.

Todos son pares. La regularidad sugiere una afirmación:

> El producto de dos enteros consecutivos es siempre par.

La afirmación general puede escribirse usando $n$ y $n+1$:

> Para todo entero $n$, el producto $n(n+1)$ es par.

Todavía no hemos demostrado nada. Hemos realizado otra operación intelectual: **pasar de casos a una conjetura**.

Ese paso es valioso, pero debe mantenerse separado de la demostración. Los ejemplos pueden sugerir una afirmación. No pueden, por sí solos, garantizar que la afirmación continúe siendo verdadera en todos los casos.

---

## 1.3. Objetos, operaciones y relaciones

Para leer álgebra con precisión necesitamos distinguir papeles diferentes dentro de una escritura matemática.

Tomemos

$3x+5=17$.

En una sola línea aparecen varias cosas.

### Objetos

Trabajamos con objetos matemáticos: números, símbolos, expresiones y, más adelante, polinomios, matrices, funciones y estructuras enteras.

En $3x+5=17$, los números $3$, $5$ y $17$ son objetos. También podemos tratar $x$ como un símbolo que ocupa un papel matemático, y la expresión completa $3x+5$ como un objeto compuesto.

### Operaciones

Una operación combina o transforma objetos.

En $3x+5$, aparecen primero una multiplicación —$3x$— y luego una suma.

En otros contextos tendremos operaciones muy diferentes: sumar matrices, componer funciones, multiplicar polinomios o combinar simetrías.

### Relaciones

Una relación vincula objetos mediante una afirmación.

En $3x+5=17$, el signo $=$ afirma que las dos expresiones situadas a sus lados tienen el mismo valor en las condiciones pertinentes.

En $x<4$, la relación es de orden.

En $3\mid 12$, que se lee «$3$ divide a $12$», la relación es de divisibilidad.

La distinción es fundamental: $3x+5$ es una **expresión**; $3x+5=17$ afirma una **relación** entre esa expresión y $17$.

### Por qué importa distinguirlos

Cuando alguien manipula símbolos sin identificar primero qué está leyendo, aparecen errores típicos: tratar una expresión como si fuera una ecuación, confundir una operación con una relación o transformar una afirmación sin preguntar si la nueva afirmación conserva el mismo significado.

El hábito que queremos formar es el contrario:

> Antes de transformar una escritura, identificar qué objetos aparecen, qué operaciones se realizan y qué relación se está afirmando.

---

## 1.4. Una expresión no es una afirmación

Comparemos tres escrituras:

- $2x-1$;
- $2x-1=7$;
- $2x-1>7$.

La primera es una expresión. Presenta un objeto algebraico construido mediante operaciones.

La segunda afirma una igualdad.

La tercera afirma una desigualdad.

La diferencia parece pequeña en la página, pero es conceptual. Una expresión como $2x-1$ no es, por sí sola, verdadera ni falsa. No está diciendo que algo ocurra. En cambio, $2x-1=7$ sí afirma algo, y esa afirmación puede ser verdadera para ciertos valores de $x$ y falsa para otros.

Ésta es una razón por la que aprender matemáticas no consiste sólo en reconocer símbolos. Hay que reconocer **qué función cumple la escritura completa**.

### Cálculo, expresión y condición

También conviene distinguir entre:

- una expresión: $x^2+3x$;
- un cálculo particular: si $x=2$, entonces $x^2+3x=10$;
- una condición: $x^2+3x=10$;
- una comparación: $x^2+3x>10$.

Más adelante estudiaremos formalmente proposiciones, variables, predicados y cuantificadores. En este capítulo no necesitamos todavía ese aparato. Sí necesitamos, desde ahora, una disciplina de lectura: **no manipular antes de saber qué tipo de cosa tenemos delante**.

---

## 1.5. Patrones: descubrir no es demostrar

Los patrones son una de las fuentes más fecundas de preguntas matemáticas.

Consideremos:

- $1=1^2$;
- $1+3=2^2$;
- $1+3+5=3^2$;
- $1+3+5+7=4^2$.

La regularidad sugiere que la suma de los primeros números impares produce cuadrados perfectos.

Podemos proponer:

> La suma de los primeros $n$ números impares es $n^2$.

La palabra importante es **proponer**.

Hasta este punto hemos observado cuatro casos. Tal vez podamos observar cuarenta o cuatro mil. Cada nuevo caso favorable aumenta la evidencia, pero la afirmación habla de todos los valores posibles de $n$ dentro del contexto. La distancia entre «muchos casos» y «todos los casos» no se elimina acumulando ejemplos.

Este contraste introduce una idea esencial de la matemática universitaria: una pauta puede originar una conjetura, pero una conjetura necesita un argumento general si queremos establecerla como verdadera.

### El papel de un contraejemplo

Para refutar una afirmación universal, la situación es diferente.

Supongamos que alguien afirma:

> Para todo entero $n\ge 0$, el número $n^2+n+41$ es primo.

Los primeros valores pueden resultar muy convincentes. Pero basta encontrar **un solo** valor para el cual la expresión no sea prima.

Si tomamos $n=41$,

$$
41^2+41+41=41(41+2)=41\cdot43.
$$

La afirmación universal queda refutada.

Hay aquí una asimetría que utilizaremos durante toda la formación matemática:

- muchos ejemplos favorables pueden sugerir una afirmación universal;
- un ejemplo desfavorable basta para destruirla;
- para establecerla, necesitamos un argumento que cubra todos los casos pertinentes.

Todavía no estudiaremos cómo construir ese argumento. Pero desde el primer capítulo debemos aprender a distinguir **evidencia**, **conjetura**, **contraejemplo** y **demostración**.

---

## 1.6. Qué queremos decir aquí por “estructura”

La palabra *estructura* será central en toda esta obra, pero sería un error tratarla desde el comienzo como si tuviera una definición elemental única y autosuficiente.

En la matemática moderna, y especialmente en álgebra, el enfoque estructural surgió cuando se volvió productivo estudiar no sólo objetos particulares, sino también la organización de sus relaciones y operaciones.

Por eso utilizaremos, por ahora, una **noción de trabajo**:

> Mirar estructuralmente significa dejar de atender sólo a los valores concretos y comenzar a preguntar qué objetos intervienen, qué operaciones y relaciones los organizan, qué propiedades se repiten y qué aspectos permanecen cuando cambian los ejemplos.

Esto no es todavía una definición formal de estructura matemática. Es una guía para aprender a mirar.

### Dos contextos diferentes

Pensemos en dos situaciones:

1. números enteros con la suma;
2. movimientos que llevan un cuadrado exactamente sobre sí mismo.

En el primer caso los objetos son números. En el segundo son movimientos geométricos. Parecen mundos distintos.

Sin embargo, en ambos podemos preguntar:

- ¿cómo combinamos dos objetos?
- ¿hay una operación que no cambie nada?
- ¿podemos deshacer una operación?
- ¿importa el orden en que combinamos?
- ¿qué relaciones se conservan?

Más adelante estas preguntas conducirán a la teoría de grupos. Ahora no necesitamos esa definición. Lo importante es ver cómo dos familias de objetos radicalmente diferentes pueden empezar a compararse por su **organización** y no por su apariencia.

Los ejemplos concretos cumplen aquí una función de puente: permiten reconocer primero un comportamiento familiar y, sólo después, aislar los rasgos que pueden compararse entre contextos muy distintos.

---

## 1.7. Transformar y preguntar qué permanece

Una de las preguntas más poderosas de toda la matemática es:

> ¿Qué permanece cuando algo cambia?

Tomemos $8+13$. Si intercambiamos los sumandos, obtenemos $13+8$. La forma visible cambia, pero el valor no.

Tomemos ahora el entero $6$. Si lo reemplazamos por su cuadrado, pasamos a $36$. Cambia el número, pero la propiedad de ser par permanece.

En ambos ejemplos hemos aplicado alguna transformación y observado una propiedad preservada.

### Invariante: una palabra que exige contexto

Llamaremos **invariante**, de manera todavía informal, a una cantidad o propiedad que permanece sin cambio bajo una transformación o familia de transformaciones especificada.

La última frase es crucial. No tiene sentido decir simplemente «esto es un invariante» sin explicar **respecto de qué cambio**.

Por ejemplo:

- el valor de una suma permanece cuando intercambiamos sus sumandos;
- la paridad de un entero par permanece al elevarlo al cuadrado;
- la longitud de un segmento permanece bajo ciertos movimientos rígidos del plano.

Más adelante encontraremos invariantes mucho más profundos: dimensión, grado, orden, rango, clases de isomorfismo y otros. La pregunta elemental «¿qué cambia y qué permanece?» es la semilla de ese lenguaje.

---

## 1.8. Una idea, varias representaciones

Una misma relación matemática puede presentarse de formas distintas.

Consideremos la regla:

> A cada número le asignamos su doble aumentado en uno.

Podemos escribirla verbalmente, como acabamos de hacer.

Podemos representarla simbólicamente mediante $2x+1$.

Podemos construir una tabla:

| $x$ | $2x+1$ |
|---:|---:|
| $0$ | $1$ |
| $1$ | $3$ |
| $2$ | $5$ |
| $3$ | $7$ |
| $4$ | $9$ |

Cada representación destaca algo distinto.

La frase verbal hace visible el procedimiento.

La expresión $2x+1$ concentra la regla.

La tabla hace visible cómo varían algunos valores y permite reconocer rápidamente una regularidad.

No hay una representación universalmente superior. Una habilidad matemática importante consiste en cambiar de representación cuando el cambio permite ver una propiedad que antes estaba oculta.

### Representar no es decorar

Un diagrama, una tabla o una fórmula sólo son útiles si revelan información.

En esta colección no utilizaremos representaciones visuales como adorno. Las usaremos cuando permitan:

- detectar una pauta;
- comparar casos;
- distinguir dependencias;
- hacer visible una transformación;
- reconocer una estructura.

---

## 1.9. Generalizar exige controlar el dominio de la afirmación

Consideremos la observación:

$2^2-2=2$, $3^2-3=6$, $4^2-4=12$, $5^2-5=20$.

Todos los resultados son pares.

Podemos conjeturar que $n^2-n$ es par para todo entero $n$.

La conjetura es correcta, pero conviene observar algo importante: la frase «para todo entero $n$» forma parte de la afirmación. Si cambiamos el dominio, podemos cambiar el problema.

Por ejemplo, si $n$ pudiera ser cualquier número real, decir que $n^2-n$ es «par» dejaría de tener el mismo sentido, porque la paridad es una propiedad de enteros.

Esto anticipa una regla general de lectura matemática:

> Una afirmación no está completamente determinada sólo por su fórmula; también importan las condiciones bajo las cuales se interpreta.

Más adelante esas condiciones aparecerán mediante dominios, hipótesis y cuantificadores. Por ahora debemos aprender a buscarlas incluso cuando están escritas en lenguaje ordinario.

### Una pregunta disciplinada

Cuando una pauta parece general, conviene preguntar:

1. ¿sobre qué objetos estamos hablando?
2. ¿qué casos hemos comprobado?
3. ¿qué afirmación exacta queremos proponer?
4. ¿podemos encontrar un caso que la destruya?
5. si no encontramos uno, ¿qué tipo de razón necesitaríamos para justificarla?

Generalizar matemáticamente no es adivinar una fórmula vistosa. Es formular con precisión una afirmación cuyo alcance conocemos.

---

## 1.10. Leer algebraicamente

Podemos reunir lo aprendido en una rutina de lectura.

Ante una expresión, igualdad, fórmula o problema, conviene preguntar:

1. ¿Cuáles son los objetos?
2. ¿Qué operaciones aparecen?
3. ¿Qué relaciones se afirman?
4. ¿Qué condiciones restringen los objetos?
5. ¿Estamos mirando un caso particular o una familia de casos?
6. ¿Qué cambia cuando modificamos el ejemplo?
7. ¿Qué permanece?
8. ¿Qué patrón parece repetirse?
9. ¿Qué afirmación general sugiere?
10. ¿Qué evidencia tenemos?
11. ¿Qué contraejemplo podríamos buscar?
12. ¿Qué faltaría justificar para convertir la conjetura en conocimiento matemático?

No todas las preguntas serán útiles en cada problema. La rutina sirve para instalar un hábito: **leer antes de operar y decidir antes de transformar**.

Éste es uno de los cambios centrales de la transición a la matemática universitaria. Cada vez habrá menos instrucciones del tipo «aplica esta fórmula» y más situaciones en las que debamos reconocer por nosotros mismos qué información es relevante y qué estructura organiza el problema.

---

## 1.11. Síntesis

El álgebra no comienza cuando aparecen letras. Comienza cuando una situación particular se convierte en objeto de comparación y generalización.

En este capítulo hemos aprendido a distinguir varios movimientos intelectuales:

```text
calcular
↓
comparar
↓
describir objetos, operaciones y relaciones
↓
detectar regularidades
↓
formular una conjetura
↓
buscar contraejemplos
↓
preguntar qué permanece
↓
preguntar qué debe justificarse
```

Todavía no hemos formalizado las leyes de las operaciones, la lógica ni la demostración. Eso es deliberado.

El capítulo siguiente examinará con mayor precisión expresiones, variables, igualdad e identidad. Después estudiaremos qué propiedades autorizan las transformaciones algebraicas. Sólo entonces comenzaremos a sistematizar el lenguaje lógico y las técnicas de demostración.

Por ahora basta con que haya cambiado la pregunta.

Ya no preguntamos solamente:

> ¿cuánto da?

También preguntamos:

> ¿qué clase de objeto estoy mirando?, ¿qué operación actúa?, ¿qué relación se afirma?, ¿qué patrón se repite?, ¿qué permanece y qué tendría que demostrar?

---

# Ejercicios

Los ejercicios están ordenados por función matemática. No todos piden calcular; varios exigen explicar, comparar o decidir qué puede concluirse.

## A. Leer antes de transformar

<!-- SOURCE: ORIGINAL | CALIBRATION: UCHILE/VELLEMAN | LEVEL: A-B -->

1. En $5x-3$, identifica los objetos visibles y las operaciones. Explica por qué no aparece todavía una relación.

2. Compara $5x-3$ con $5x-3=12$. ¿Qué elemento nuevo aparece en la segunda escritura y qué cambia en su significado?

3. Clasifica cada escritura como expresión o afirmación de una relación: $a^2+b^2$, $a^2+b^2=c^2$, $m<n$, $4\mid 28$, $3(y+1)$.

4. En $2(a+b)=2a+2b$, identifica las operaciones y la relación principal. Sin justificar todavía la igualdad en general, explica qué afirma la escritura.

5. Explica la diferencia entre $x+4$ y $x+4=0$ sin resolver ninguna ecuación.

6. Un estudiante dice que «$7\mid 35$ es una división». Explica con precisión por qué esa lectura es incorrecta.

## B. Casos, patrones y generalidad

<!-- SOURCE: ORIGINAL | INSPIRED_BY: VELLEMAN_PATTERN_CONJECTURE | LEVEL: A-C -->

7. Calcula $1\cdot2$, $2\cdot3$, $3\cdot4$, $4\cdot5$, $5\cdot6$ y formula una conjetura sobre la paridad del producto de dos enteros consecutivos.

8. Examina $n^2-n$ para $n=1,2,3,4,5,6$. Formula una conjetura precisa e indica cuál es el dominio sobre el que la propones.

9. Observa $1$, $1+3$, $1+3+5$, $1+3+5+7$ y $1+3+5+7+9$. Formula una conjetura que describa los resultados.

10. Calcula $(-1)^n$ para $n=0,1,2,3,4,5,6$. Describe el patrón en palabras y luego mediante una regla que distinga dos casos.

11. Busca seis valores iniciales de $2^n$ y describe dos regularidades diferentes que observes. Distingue claramente «regularidad observada» de «afirmación demostrada».

12. Construye cinco ejemplos numéricos que sugieran una regla general propia. Escribe por separado: los casos, la regularidad observada y la conjetura.

## C. Contraejemplos y límites de la evidencia

<!-- SOURCE: ORIGINAL | INSPIRED_BY: VELLEMAN_COUNTEREXAMPLE | LEVEL: B-C -->

13. Refuta: «para todos los números reales $a,b$, se cumple $a-b=b-a$».

14. Refuta: «si $a^2=b^2$, entonces $a=b$» para números reales.

15. Refuta: «la suma de dos enteros impares es impar».

16. Un estudiante comprueba veinte valores de $n$ y observa que una fórmula produce siempre un número primo. Explica por qué eso no basta para demostrar que la fórmula produce primos para todo $n$.

17. Considera $n^2+n+41$. Comprueba algunos valores iniciales y encuentra un valor que destruya la afirmación «siempre es primo».

18. Inventa una afirmación universal falsa sobre enteros que resulte plausible al mirar al menos tres casos iniciales. Luego encuentra un contraejemplo.

## D. Comparar comportamientos

<!-- SOURCE: ORIGINAL | CALIBRATION: NICHOLSON_CONCRETE_TO_ABSTRACT | LEVEL: B-C -->

19. Compara $14+9$ con $9+14$, y $14-9$ con $9-14$. Describe el cambio aplicado y lo que ocurre con el resultado en cada operación.

20. Compara $3\cdot 8$ con $8\cdot 3$, y $3/8$ con $8/3$. Formula una pregunta general sugerida por el contraste.

21. Considera los pares $2+7=9$, $5+4=9$ y $12+(-3)=9$. ¿Qué cambia entre los ejemplos y qué permanece?

22. Considera $4^2$, $6^2$, $10^2$ y $14^2$. ¿Qué propiedad de las bases permanece en los cuadrados? Formula la observación sin intentar demostrarla.

23. Da un ejemplo de una transformación de una expresión que preserve su valor en los casos que pruebes y otro ejemplo de una transformación que no lo preserve.

24. Explica, con un ejemplo propio, qué significa estudiar «el comportamiento de una operación» en lugar de limitarse a efectuarla.

## E. Representaciones

<!-- SOURCE: ORIGINAL | CALIBRATION: SELF_STUDY / MULTIPLE_REPRESENTATIONS | LEVEL: A-C -->

25. Traduce al lenguaje simbólico: «tres veces un número, menos cinco».

26. Explica la diferencia entre «tres veces un número, menos cinco» y «tres veces la diferencia entre un número y cinco». Escribe ambas expresiones.

27. Representa «la suma de dos enteros consecutivos» usando una sola letra.

28. Construye una tabla de cinco valores para la regla $3x+2$. ¿Qué información se hace más visible en la tabla que en la expresión aislada?

29. Una tabla contiene los pares $(0,1)$, $(1,3)$, $(2,5)$, $(3,7)$, $(4,9)$. Propón una expresión sencilla que reproduzca esos valores. Explica por qué cinco pares compatibles no demuestran que esa expresión sea la única regla posible.

30. Da un ejemplo de una idea matemática elemental que puedas expresar verbalmente, mediante símbolos y mediante una tabla. Explica qué revela mejor cada representación.

## F. Pensamiento estructural y síntesis

<!-- SOURCE: ORIGINAL | INSPIRED_BY: NICHOLSON/CORRY | CALIBRATION: UCHILE | LEVEL: C-E -->

31. Explica por qué «enteros con suma» y «movimientos de un cuadrado que lo llevan sobre sí mismo» podrían ser comparables desde un punto de vista estructural, aunque sus objetos sean completamente distintos. No uses todavía vocabulario de teoría de grupos.

32. Considera el paso de $8+13$ a $13+8$. Identifica la transformación y una cantidad que permanece. Explica por qué la palabra «invariante» requiere mencionar la transformación considerada.

33. Considera el paso de un entero par $n$ a su cuadrado $n^2$. ¿Qué propiedad parece preservarse? ¿Qué tendría que hacerse más adelante para convertir la observación en una afirmación demostrada?

34. Analiza la escritura $a(b+c)=ab+ac$ mediante la rutina de lectura algebraica: objetos, operaciones, relación, familia de casos, posible regularidad y cuestión de justificación.

35. Un estudiante afirma: «como $2^2+1=5$, $4^2+1=17$ y $6^2+1=37$, entonces $n^2+1$ es primo para todo entero par $n$». Evalúa el razonamiento y encuentra un contraejemplo.

36. Escribe un párrafo matemático breve que responda: **¿qué diferencia hay entre resolver un cálculo y reconocer una estructura?** Tu respuesta debe mencionar al menos objetos, operaciones o relaciones, y generalidad.

---

# Soluciones

Las soluciones respetan deliberadamente los prerrequisitos del Capítulo 1. Cuando una afirmación requiere teoría posterior, se explica qué puede concluirse ahora y qué deberá justificarse más adelante.

## A. Leer antes de transformar

### 1
En $5x-3$ aparecen los símbolos $5$, $x$ y $3$, y también las expresiones $5x$ y $5x-3$. Las operaciones son multiplicación y resta. No aparece una relación porque la escritura no compara $5x-3$ con otro objeto mediante $=$, $<$, $\mid$ u otro signo relacional.

**Idea transferible:** una expresión puede contener varias operaciones sin afirmar todavía que dos objetos estén relacionados.

### 2
En $5x-3=12$ aparece la relación de igualdad. La expresión $5x-3$ deja de estar aislada: ahora se afirma que, bajo las condiciones pertinentes, tiene el mismo valor que $12$.

No hemos resuelto la ecuación; sólo hemos identificado qué tipo de escritura es.

### 3
- $a^2+b^2$: expresión.
- $a^2+b^2=c^2$: afirmación de igualdad.
- $m<n$: afirmación de orden.
- $4\mid28$: afirmación de divisibilidad.
- $3(y+1)$: expresión.

La presencia de operaciones no convierte automáticamente una escritura en una afirmación.

### 4
Aparecen suma y multiplicación. La relación principal es igualdad. La escritura afirma que las expresiones $2(a+b)$ y $2a+2b$ tienen el mismo valor para los objetos y condiciones bajo los cuales se interprete la igualdad.

En este capítulo no necesitamos justificar todavía por qué esa igualdad es general; su justificación sistemática llegará al estudiar las leyes de las operaciones.

### 5
$x+4$ es una expresión: no afirma nada por sí sola. $x+4=0$ es una afirmación de igualdad que impone una condición sobre los valores que pueda tomar $x$.

### 6
El símbolo $\mid$ no indica que se esté realizando la operación $35/7$. La escritura $7\mid35$ afirma una relación: que $35$ es múltiplo de $7$, o equivalentemente, que existe un entero que multiplicado por $7$ produce $35$.

## B. Casos, patrones y generalidad

### 7
Los productos son $2,6,12,20,30$, todos pares.

Conjetura: **para todo entero $n$, el producto $n(n+1)$ es par**.

Los cálculos proporcionan evidencia. La afirmación general todavía necesitaría una justificación válida para cualquier entero.

### 8
Los valores son $0,2,6,12,20,30$. Todos son pares.

Una conjetura precisa es: **para todo entero $n$, $n^2-n$ es par**.

El dominio importa: la palabra «par» tiene sentido aquí porque estamos hablando de enteros.

### 9
Los resultados son $1,4,9,16,25$, es decir, $1^2,2^2,3^2,4^2,5^2$.

Conjetura: **la suma de los primeros $n$ enteros impares positivos es $n^2$**.

### 10
Los valores son $1,-1,1,-1,1,-1,1$.

Regla:
- si $n$ es par, $(-1)^n=1$;
- si $n$ es impar, $(-1)^n=-1$.

Todavía no hemos probado la regla para todos los enteros no negativos; la hemos formulado a partir del patrón y del significado de potencia.

### 11
Por ejemplo, para $n=1,\dots,6$ se obtiene $2,4,8,16,32,64$.

Dos regularidades:
1. todos los valores son pares;
2. la última cifra sigue $2,4,8,6,2,4,\dots$.

Ambas son observaciones. Para convertirlas en teoremas habría que justificar que continúan para todos los exponentes del dominio.

### 12
Respuesta abierta. Un ejemplo válido:

Casos: $1^2+1=2$, $2^2+2=6$, $3^2+3=12$, $4^2+4=20$, $5^2+5=30$.

Regularidad: todos los resultados son pares.

Conjetura: para todo entero $n$, $n^2+n$ es par.

Lo esencial es separar los datos observados de la afirmación general.

## C. Contraejemplos y límites de la evidencia

### 13
Toma $a=5$ y $b=2$. Entonces $a-b=3$, mientras que $b-a=-3$. Como la afirmación decía «para todos», un solo caso que falle basta para refutarla.

### 14
Toma $a=1$ y $b=-1$. Se cumple $a^2=b^2=1$, pero $a\ne b$. La afirmación es falsa.

### 15
Toma dos impares, por ejemplo $3$ y $5$. Su suma es $8$, que es par. Por tanto, la afirmación universal es falsa.

### 16
Veinte comprobaciones cubren sólo veinte casos. Si la afirmación pretende valer para todos los valores posibles de $n$, todavía podría existir un contraejemplo fuera de los casos examinados.

La ausencia de contraejemplos en una búsqueda finita no constituye una demostración universal.

### 17
Para varios valores pequeños aparecen números primos. Sin embargo, para $n=41$:

$$
41^2+41+41=41\cdot43,
$$

que es compuesto. Por lo tanto, «siempre es primo» es falso.

### 18
Respuesta abierta. Ejemplo:

Afirmación: «$n^2+n+1$ es primo para todo entero positivo $n$».

Casos:
- $n=1$: $3$, primo;
- $n=2$: $7$, primo;
- $n=3$: $13$, primo.

Contraejemplo:
- $n=4$: $21=3\cdot7$, no primo.

El ejercicio muestra que una pauta muy convincente en los primeros casos puede fallar inmediatamente después.

## D. Comparar comportamientos

### 19
$14+9=23$ y $9+14=23$: al intercambiar los términos, el resultado se conserva.

$14-9=5$ y $9-14=-5$: al aplicar el mismo tipo de cambio —intercambiar los términos— el resultado no se conserva.

La comparación muestra que operaciones diferentes pueden responder de manera diferente a una misma transformación de sus entradas.

### 20
$3\cdot8=24$ y $8\cdot3=24$, mientras que $3/8\ne8/3$.

Pregunta general sugerida: **¿para qué operaciones el intercambio de los dos argumentos conserva el resultado?**

En el capítulo 3 esta pregunta se convertirá en una propiedad formal.

### 21
Cambian los sumandos: $(2,7)$, $(5,4)$ y $(12,-3)$. Permanece el resultado de la suma: $9$.

Una misma relación final puede realizarse mediante objetos concretos diferentes.

### 22
Las bases $4,6,10,14$ son pares, y sus cuadrados $16,36,100,196$ también lo son.

Observación: **al elevar al cuadrado un entero par, parece preservarse la paridad par**.

Los ejemplos no son todavía una demostración general.

### 23
Respuesta abierta.

Ejemplo que preserva valor: transformar $7+12$ en $12+7$; ambos valen $19$.

Ejemplo que no preserva valor: transformar $7-12$ en $12-7$; se pasa de $-5$ a $5$.

Lo importante es especificar la transformación y comparar una propiedad antes y después.

### 24
Respuesta modelo: estudiar el comportamiento de una operación significa observar qué ocurre cuando variamos sus entradas o las transformamos, y buscar propiedades que se repiten. Por ejemplo, sumar $a+b$ y luego intercambiar a $b+a$ permite preguntar si el resultado depende del orden, en vez de limitarse a calcular un caso particular.

## E. Representaciones

### 25
«Tres veces un número, menos cinco» puede representarse como $3x-5$.

### 26
«Tres veces un número, menos cinco» se representa como $3x-5$.

«Tres veces la diferencia entre un número y cinco» se representa como $3(x-5)$.

No son iguales en general. La primera resta $5$ después de triplicar; la segunda resta primero y triplica después toda la diferencia.

### 27
Si el primer entero es $n$, el siguiente es $n+1$. La suma es $n+(n+1)$.

No necesitamos simplificar todavía; la expresión ya representa la relación verbal.

### 28
Una tabla posible:

| $x$ | $3x+2$ |
|---:|---:|
| $0$ | $2$ |
| $1$ | $5$ |
| $2$ | $8$ |
| $3$ | $11$ |
| $4$ | $14$ |

La tabla hace visible, por ejemplo, que al aumentar $x$ en $1$, los valores mostrados aumentan en $3$. La expresión simbólica comprime la regla para cualquier entrada.

### 29
Una regla sencilla es $2x+1$.

Sin embargo, cinco pares no determinan de manera única una regla posible: pueden construirse otras expresiones que coincidan en esos cinco valores y difieran después. Por tanto, los datos apoyan la regla propuesta, pero no prueban su unicidad.

### 30
Respuesta abierta. Ejemplo:

Verbal: «a cada entero le asignamos su cuadrado».

Simbólico: $x^2$.

Tabla: $(0,0),(1,1),(2,4),(3,9)$.

La frase verbal explica la acción, la fórmula la condensa y la tabla muestra casos concretos y crecimiento.

## F. Pensamiento estructural y síntesis

### 31
Los objetos son distintos: en un caso son enteros y en otro movimientos geométricos. Sin embargo, en ambos contextos puede existir una manera de combinar dos objetos, puede haber una operación que no cambie nada y puede tener sentido preguntar si una operación puede deshacerse.

La comparación es estructural porque se centra en la organización y el comportamiento, no en la naturaleza material de los objetos.

### 32
La transformación es intercambiar los dos sumandos. La cantidad que permanece es el valor de la suma, $21$.

Decir «$21$ es un invariante» sin más sería incompleto. Es invariante **respecto de esa transformación concreta** en este ejemplo: intercambiar los sumandos.

### 33
Si $n$ es par, los ejemplos sugieren que $n^2$ también es par. Para convertirlo en una afirmación demostrada habría que dar una razón que funcione para cualquier entero par, no sólo para los valores comprobados.

Más adelante podremos expresar un entero par en una forma general y usarla en una demostración.

### 34
En $a(b+c)=ab+ac$:

- objetos: $a,b,c$ y las expresiones construidas con ellos;
- operaciones: suma y multiplicación;
- relación: igualdad;
- familia de casos: los valores permitidos de $a,b,c$;
- regularidad sugerida: multiplicar una suma por $a$ parece producir el mismo resultado que multiplicar cada término por $a$ y sumar;
- cuestión pendiente: justificar por qué la igualdad vale en todos los casos del dominio.

En este capítulo la lectura es suficiente; la ley que justifica la transformación se estudiará sistemáticamente después.

### 35
Los tres casos apoyan una conjetura, pero no una conclusión universal.

Un contraejemplo es $n=8$:

$8^2+1=65=5\cdot13$,

que no es primo. Por tanto, la afirmación es falsa.

El error del estudiante no fue calcular mal; fue atribuir a unos pocos ejemplos una fuerza lógica que no tienen.

### 36
Respuesta modelo:

Resolver un cálculo consiste en obtener información sobre un caso concreto, por ejemplo hallar el valor de $17+8$. Reconocer una estructura exige mirar más allá del resultado y preguntar qué objetos intervienen, qué operaciones o relaciones los conectan y qué propiedades continúan siendo válidas al cambiar los ejemplos. El cálculo puede aportar evidencia, pero el pensamiento estructural busca una organización que explique una familia de casos.

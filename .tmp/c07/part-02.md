## 7.12. De la lógica a los conjuntos

Para un elemento fijo $x$, pongamos

$P: x\in A$,

$Q: x\in B$.

Entonces aparece el diccionario:

| Lógica | Conjuntos |
|---|---|
| $P$ | $x\in A$ |
| $P\lor Q$ | $x\in A\cup B$ |
| $P\land Q$ | $x\in A\cap B$ |
| $\neg P$ | $x\in A^c$ |
| $P\Rightarrow Q$ | $A\subseteq B$ |
| $P\Leftrightarrow Q$ | $A=B$ |

Por ejemplo, la ley lógica de De Morgan

$$
\neg(P\lor Q)\equiv(\neg P)\land(\neg Q)
$$

se convierte, al leerla como pertenencia, en

$$
(A\cup B)^c=A^c\cap B^c.
$$

### El puente funciona elemento a elemento

No estamos afirmando que un conjunto sea literalmente una proposición. Estamos diciendo que la condición «$x$ pertenece al conjunto resultante» está gobernada por la misma estructura lógica.

Esta observación explica por qué podemos tratar ciertas expresiones de conjuntos como un álgebra.

***

## 7.13. Probar identidades de conjuntos

Hay al menos tres métodos útiles.

### 1. Transformación algebraica

Podemos aplicar leyes ya establecidas, igual que en C5 transformábamos fórmulas lógicas.

### 2. Pertenencia elemento a elemento

Para probar $X=Y$, tomamos un elemento arbitrario $x$ y mostramos

$x\in X\Leftrightarrow x\in Y$.

La equivalencia puede desarrollarse usando lógica proposicional.

### 3. Doble inclusión

Podemos demostrar $X\subseteq Y$ y $Y\subseteq X$ por separado.

### ¿Y los diagramas de Venn?

Un diagrama puede ser excelente para visualizar una identidad o descubrir un contraejemplo en una configuración simple. Pero cuando la tarea exige una prueba general, el argumento debe poder expresarse simbólicamente o elemento a elemento.

### Refutar una identidad

Si una supuesta identidad afirma $X=Y$, basta elegir conjuntos concretos y encontrar un elemento que pertenezca a un lado y no al otro.

***

## 7.14. Producto cartesiano y pares ordenados

Un **par ordenado** $(a,b)$ registra dos componentes en orden. En general,

$(a,b)\ne(b,a)$

cuando $a\ne b$.

El **producto cartesiano** de $A$ y $B$ es

$$
A\times B=\{(a,b):a\in A,\ b\in B\}.
$$

Si $A=\{1,2\}$ y $B=\{u,v\}$, entonces

$$
A\times B=\{(1,u),(1,v),(2,u),(2,v)\}.
$$

Mientras

$$
B\times A=\{(u,1),(u,2),(v,1),(v,2)\}.
$$

En general no son iguales.

### Producto con el vacío

No existe ningún par cuyo primer elemento esté en $\varnothing$. Por eso

$\varnothing\times A=\varnothing$

y, del mismo modo,

$A\times\varnothing=\varnothing$.

### Tamaño en el caso finito

Si $A$ tiene $m$ elementos y $B$ tiene $n$, entonces $A\times B$ tiene $mn$ pares.

El producto cartesiano será el punto de partida de C8, donde estudiaremos relaciones. Aquí nos detenemos antes de esa definición.

***

## 7.15. Errores estructurales frecuentes

### Error 1: confundir $\in$ con $\subseteq$

Si $A=\{1,2\}$, entonces $1\in A$ y $\{1\}\subseteq A$. Intercambiar los símbolos cambia el tipo de afirmación.

### Error 2: confundir $\varnothing$ con $\{\varnothing\}$

El primero tiene cero elementos; el segundo, uno.

### Error 3: hablar de $A^c$ sin universo

El complemento depende del universo de referencia.

### Error 4: suponer que la diferencia es conmutativa

En general $A\setminus B\ne B\setminus A$.

### Error 5: inferir igualdad desde una sola inclusión

$A\subseteq B$ no implica $A=B$. Falta controlar la inclusión inversa.

### Error 6: tratar operaciones de conjuntos como aritmética

No existen reglas de «cancelación» automáticas como

$A\cup C=B\cup C\Rightarrow A=B$.

Por ejemplo, si $C=U$, ambos lados son $U$ para cualesquiera $A,B$.

### Error 7: olvidar el orden del producto cartesiano

$A\times B$ no suele coincidir con $B\times A$.

### Error 8: convertir un dibujo en demostración

La visualización ayuda, pero la prueba debe controlar la definición para todos los elementos pertinentes.

***

## 7.16. Protocolo de lectura conjuntista

Antes de transformar una expresión de conjuntos, preguntar:

1. **¿Cuál es el universo o dominio?**
2. **¿Qué símbolos representan elementos y cuáles conjuntos?**
3. **¿Aparece pertenencia $\in$ o inclusión $\subseteq$?**
4. **¿Cómo está definido cada conjunto?**
5. **¿Qué operación aparece: unión, intersección, diferencia, complemento o producto?**
6. **¿Qué condición lógica significa pertenecer al resultado?**
7. **Si hay complemento, está fijado el universo?**
8. **¿La igualdad puede traducirse a una equivalencia sobre un elemento arbitrario?**
9. **¿Conviene transformar algebraicamente o usar doble inclusión?**
10. **Si aparece un producto cartesiano, estoy respetando el orden de las coordenadas?**

La meta del capítulo puede resumirse así:

> **El álgebra de conjuntos es la lógica de pertenencia escrita como operaciones entre colecciones.**


# Ejercicios

Los ejercicios son de redacción original para *Álgebra para matemáticos*. Algunos problemas avanzados toman como benchmark estructural el corpus MA1101 de la Universidad de Chile, sin reproducir literalmente sus enunciados.

## A. Pertenencia y descripción

1. Sea $A=\{2,4,6,8\}$. Decide cuáles son verdaderas: $4\in A$, $5\in A$, $\{4\}\in A$, $\{4\}\subseteq A$.

2. Escribe por extensión el conjunto $\{n\in\mathbb Z:-2\le n\le2\}$.

3. Describe por comprensión el conjunto $\{1,4,9,16,25\}$ usando números naturales.

4. Explica por qué $\{1,2,2,3\}=\{3,2,1\}$.

5. Determina el conjunto $A=\{x\in\mathbb Z:x^2<5\}$.

6. Sean $A=\{x\in\mathbb R:x^2=4\}$ y $B=\{-2,2\}$. Justifica que describen el mismo conjunto.


## B. Vacío, unitarios y notación

7. ¿Cuántos elementos tienen $\varnothing$, $\{\varnothing\}$ y $\{\{\varnothing\}\}$?

8. Decide si $\varnothing\in\{\varnothing,1\}$ y si $\varnothing\subseteq\{\varnothing,1\}$.

9. Sea $A=\{\varnothing,\{1\},1\}$. Decide si $1\in A$, $\{1\}\in A$, $\{1\}\subseteq A$ y $\varnothing\in A$.

10. Encuentra un conjunto $A$ tal que $\varnothing\in A$ pero $\{\varnothing\}\notin A$.

11. Encuentra un conjunto $A$ tal que $\{\varnothing\}\subseteq A$ pero $\{\varnothing\}\notin A$.

12. Explica por qué no existe ningún $x$ tal que $x\in\varnothing$. ¿Qué implicación tiene esto para una afirmación de la forma “si $x\in\varnothing$, entonces $P(x)$”?


## C. Subconjuntos e igualdad

13. Sea $A=\{1,2\}$ y $B=\{1,2,3\}$. Decide $A\subseteq B$, $B\subseteq A$, $A\in B$ y $2\subseteq B$.

14. Demuestra que $\varnothing\subseteq A$ para todo conjunto $A$.

15. Demuestra que la inclusión es transitiva: si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.

16. Sea $A=\{1,2,3\}$ y $B=\{3,2,1\}$. Justifica $A=B$ sin apelar a que “se ven iguales”.

17. Sean $A=\{x\in\mathbb Z:-1\le x\le2\}$ y $B=\{-1,0,1,2\}$. Prueba $A=B$ por doble inclusión.

18. Da un contraejemplo a la afirmación: “si $A\subseteq B$, entonces $A=B$”.

19. Supón $A\subseteq B$ y $B\subseteq A$. Explica por qué no es necesario conocer una lista de los elementos para concluir $A=B$.

20. Sean $A,B,C$ conjuntos. Si $A\subseteq B$ y $A\subseteq C$, ¿se sigue $A\subseteq B\cap C$? Demuéstralo o da contraejemplo.


## D. Conjunto potencia

21. Calcula $\mathcal P(\{a,b\})$.

22. Lista todos los elementos de $\mathcal P(\{1,2,3\})$.

23. Sea $A=\{1,2\}$. Decide: $1\in\mathcal P(A)$, $\{1\}\in\mathcal P(A)$, $A\in\mathcal P(A)$ y $\varnothing\in\mathcal P(A)$.

24. Demuestra que $\mathcal P(A\cap B)=\mathcal P(A)\cap\mathcal P(B)$.

25. ¿Es siempre cierto que $\mathcal P(A\cup B)=\mathcal P(A)\cup\mathcal P(B)$? Si no, produce un contraejemplo.

26. Un conjunto finito $A$ tiene $32$ subconjuntos. ¿Cuántos elementos tiene $A$? Justifica.


## E. Unión e intersección

27. Sean $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$. Calcula $A\cup B$ y $A\cap B$.

28. Sean $A=\{x\in\mathbb Z:x\ge0\}$ y $B=\{x\in\mathbb Z:x\le2\}$. Describe $A\cap B$ por extensión.

29. Con los conjuntos del ejercicio anterior, describe $A\cup B$ y decide si coincide con $\mathbb Z$.

30. Demuestra $A\cap B\subseteq A\subseteq A\cup B$.

31. Prueba $A\cup\varnothing=A$ por extensionalidad.

32. Prueba $A\cap A=A$ por extensionalidad.

33. Si $A\subseteq B$, demuestra $A\cup B=B$ y $A\cap B=A$.

34. ¿Es verdadera la recíproca: si $A\cap B=A$, entonces $A\subseteq B$? Justifica.


## F. Diferencia y complemento

35. Sean $A=\{1,2,3,4\}$ y $B=\{3,4,5\}$. Calcula $A\setminus B$ y $B\setminus A$.

36. Sea $U=\{1,2,3,4,5\}$ y $A=\{1,3,5\}$. Calcula $A^c$.

37. Usa $A=\{1,2\}$ y dos universos distintos para mostrar que el complemento depende del universo.

38. Demuestra $A\setminus B=A\cap B^c$ respecto de un universo que contenga a $A$ y $B$.

39. Prueba $(A^c)^c=A$.

40. Prueba la ley de De Morgan $(A\cup B)^c=A^c\cap B^c$.

41. ¿Es cierto que $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$? Demuéstralo.

42. Da un contraejemplo a $A\setminus(B\setminus C)=(A\setminus B)\setminus C$.


## G. Diferencia simétrica

43. Sean $A=\{1,2,3\}$ y $B=\{3,4\}$. Calcula $A\triangle B$.

44. Demuestra $A\triangle B=(A\cup B)\setminus(A\cap B)$.

45. Prueba que $A\triangle B=B\triangle A$.

46. Determina todas las condiciones bajo las cuales $A\triangle B=\varnothing$.


## H. Leyes y transformaciones

47. Simplifica $A\cap(A\cup B)$.

48. Simplifica $(A\cup B)\cap(A\cup B^c)$.

49. Simplifica $(A\cap B)\cup(A\cap B^c)$.

50. Demuestra $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ usando el diccionario lógico.

51. Prueba $A\cap(B\setminus C)=(A\cap B)\setminus C$.

52. Prueba $A\triangle B=(A\cup B)\cap(A^c\cup B^c)$.

53. Transforma $(A\cup B)^c\cup(A\cap B^c)$ hasta una forma sin complementos de uniones.

54. Caracteriza cuándo $\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B)$.


## I. Demostraciones por elementos y doble inclusión

55. Demuestra por doble inclusión $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$.

56. Demuestra por elementos $(A\cap B)\setminus C=A\cap(B\setminus C)$.

57. Demuestra que $A\triangle B=(A\cup B)\setminus(A\cap B)$ por doble inclusión.

58. Supón $A\cap B\subseteq C$. Demuestra $A\cap C^c\subseteq B^c$.

59. Refuta con un contraejemplo la identidad $A\cup(B\setminus C)=(A\cup B)\setminus C$.

60. Demuestra $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$ de dos maneras: por una ley algebraica y por pertenencia.


## J. Producto cartesiano

61. Sean $A=\{1,2\}$ y $B=\{a,b,c\}$. Escribe $A\times B$.

62. Con los conjuntos del ejercicio anterior, escribe $B\times A$ y explica por qué no es igual a $A\times B$.

63. Demuestra $A\times\varnothing=\varnothing$.

64. Demuestra $(A\cup B)\times C=(A\times C)\cup(B\times C)$.

65. Caracteriza cuándo $A\times B=B\times A$.

66. Si $|A|=4$ y $|B|=7$, calcula $|A\times B|$. Explica el principio.


## K. Diagnóstico y transferencia

67. Un estudiante escribe: “como $1\in A$, entonces $1\subseteq A$”. Diagnostica y repara.

68. Un estudiante calcula el complemento de $A=\{1,2\}$ como “todos los números salvo $1$ y $2$”. Explica qué información falta.

69. Un estudiante demuestra $A=B$ mostrando únicamente $A\subseteq B$. ¿Qué falta? Da un ejemplo que muestre por qué.

70. Explica por qué un diagrama de Venn puede sugerir $(A\cup B)^c=A^c\cap B^c$, pero una prueba por pertenencia es conceptualmente más general.

71. Determina si la afirmación $A\cup C=B\cup C\Rightarrow A=B$ es verdadera. Si es falsa, produce un contraejemplo y explica por qué falla la “cancelación”.

72. Síntesis: explica en 8–12 líneas por qué las leyes de conjuntos pueden entenderse como una segunda realización del álgebra lógica de C5. Incluye pertenencia, unión, intersección, complemento, inclusión y extensionalidad.


## L. Problemas tipo prueba

Los siguientes problemas están diseñados para evaluación escrita. Se espera una demostración completa, no sólo el resultado final.

73. Demuestra, para conjuntos arbitrarios $A$ y $B$, que

$$
\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B).
$$

Deduce además que

$$
\mathcal P(A)\subseteq\mathcal P(B)\quad\Longleftrightarrow\quad A\subseteq B.
$$

74. Caracteriza exactamente cuándo se cumple

$$
\mathcal P(A)\cup\mathcal P(B)=\mathcal P(A\cup B).
$$

Demuestra que la igualdad vale si y sólo si $A\subseteq B$ o $B\subseteq A$.


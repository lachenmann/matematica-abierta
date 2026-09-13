## 6.16. Cierre — protocolo de lectura cuantificada

Cuando encuentres una afirmación con variables y cuantificadores, utiliza esta rutina:

```text
1. ¿CUÁL ES EL DOMINIO?
2. ¿CUÁL ES EL PREDICADO?
3. ¿QUÉ VARIABLES ESTÁN LIBRES?
4. ¿QUÉ VARIABLES ESTÁN LIGADAS?
5. ¿QUÉ CUANTIFICADOR LIGA A CADA VARIABLE?
6. ¿CUÁL ES EL ALCANCE DE CADA CUANTIFICADOR?
7. ¿EN QUÉ ORDEN APARECEN?
8. ¿UN TESTIGO PUEDE DEPENDER DE VARIABLES ANTERIORES?
9. ¿CÓMO SE NIEGA LA AFIRMACIÓN COMPLETA?
10. ¿QUÉ BASTARÍA PARA REFUTARLA O PARA EXHIBIR EXISTENCIA?
```

El paso conceptual de C6 puede resumirse así:

$$
\text{condición abierta}
\longrightarrow
\text{dominio + cuantificación}
\longrightarrow
\text{afirmación precisa}.
$$

A partir de ahora, expresiones como “para todo”, “existe” y “existe un único” dejarán de ser palabras de apoyo y se convertirán en parte visible de la estructura matemática.

***

## Ejercicios del capítulo

### A — Predicados y dominios

**1.** Clasifica cada escritura como **expresión**, **predicado abierto** o **proposición**: (a) $x+1$; (b) $x+1=5$; (c) $4+1=5$; (d) $n$ es par; (e) “$6$ es par”.

**2.** Sea $P(x):x^2=2$. Decide la verdad de $\exists x\,P(x)$ cuando el dominio es (a) $\mathbb Z$; (b) $\mathbb Q$; (c) $\mathbb R$.

**3.** Sea $P(x):x^2\ge x$. Decide si $\forall x\,P(x)$ es verdadera sobre (a) $\{0,1\}$; (b) $\mathbb Z$; (c) $\mathbb R$.

**4.** Para $Q(x):1/x>0$, explica por qué el dominio $\mathbb R$ exige una precisión adicional antes de evaluar $Q(0)$.

**5.** Da un dominio finito $D$ con al menos dos elementos para el cual $\forall x\in D\;(x^2=1)$ sea verdadera, y otro dominio finito $E$ para el cual sea falsa.

**6.** Sea $R(x):x^2<4$. Compara $\forall x\,R(x)$ y $\exists x\,R(x)$ sobre los dominios $\mathbb Z$ y $\mathbb R$.

### B — Variables libres y ligadas

**7.** Identifica las variables libres y ligadas en $\forall x\,P(x,y)$.

**8.** Identifica las variables libres y ligadas en $\exists y\,[R(x,y)\land Q(y,z)]$.

**9.** ¿Es una proposición cerrada $\forall x\,\exists y\,R(x,y)$? ¿Y $\forall x\,\exists y\,R(x,y,z)$?

**10.** Convierte el predicado $P(x):x^2=9$ en (a) una proposición mediante sustitución; (b) una proposición existencial; (c) una proposición universal, usando dominio $\mathbb R$.

**11.** En $\forall x\,[P(x,y)\Rightarrow\exists z\,R(x,z)]$, clasifica $x,y,z$ como libres o ligadas.

**12.** Reescribe $\forall x\,P(x,y)$ cambiando el nombre de la variable ligada sin cambiar el significado. Explica por qué $\forall y\,P(y,y)$ no es, en general, una renominación válida.

### C — Universales y contraejemplos

**13.** Decide si $\forall n\in\mathbb Z\;(n^2\ge0)$ es verdadera y explica qué tipo de justificación requiere.

**14.** Refuta $\forall n\in\mathbb Z\;(n^2>n)$ con un contraejemplo.

**15.** Refuta la afirmación “la suma de dos enteros impares es impar”.

**16.** Un estudiante verifica que $n^2+n+17$ es primo para $n=0,1,\dots,15$ y concluye que es primo para todo $n\ge0$. Explica el error y encuentra un contraejemplo.

**17.** La afirmación es: “para todo entero $n$, si $n$ es par entonces $n^2$ es par”. ¿Puede un entero impar ser contraejemplo? Justifica.

**18.** Da un contraejemplo a “para todo real $x$, si $x^2>1$ entonces $x>1$”.

### D — Existenciales y testigos

**19.** Demuestra exhibiendo un testigo que $\exists n\in\mathbb Z\;(n^2=49)$.

**20.** Decide si $\exists n\in\mathbb Z\;(2n=7)$ es verdadera.

**21.** Exhibe un testigo para $\exists x\in\mathbb R\;(0<x<1\land x^2<x)$.

**22.** Exhibe enteros $a,b$ que prueben $\exists a,b\in\mathbb Z\;(a^2-b^2=15)$.

**23.** Demuestra que $\exists n\in\mathbb Z\;(n>1000)$ exhibiendo un testigo. ¿Qué demuestra este ejercicio sobre el tamaño del testigo?

**24.** Un estudiante encuentra dos testigos distintos para $\exists x\,P(x)$ y concluye que la afirmación era falsa porque “$x$ no es único”. Diagnostica el error.

### E — Negación de cuantificadores

**25.** Niega $\forall x\in\mathbb R\;(x^2\ge0)$ sin dejar una negación delante del cuantificador.

**26.** Niega $\exists n\in\mathbb Z\;(n^2=2)$.

**27.** Niega $\forall n\in\mathbb Z\;[E(n)\Rightarrow E(n^2)]$, donde $E(k)$ significa “$k$ es par”.

**28.** Niega $\exists x\in\mathbb R\;(x>0\land x^2<1)$.

**29.** Niega $\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x)$.

**30.** Niega $\exists y\in\mathbb R\;\forall x\in\mathbb R\;(y>x)$.

**31.** Traduce simbólicamente: “No todos los enteros son positivos”.

**32.** Explica con un ejemplo por qué $\neg\forall x\,P(x)$ no equivale a $\forall x\,\neg P(x)$.

### F — Cuantificación restringida

**33.** Reescribe $\forall n\in\mathbb Z\;P(n)$ usando un dominio mayor $D$ que contiene a $\mathbb Z$ y una implicación con pertenencia.

**34.** Reescribe $\exists n\in\mathbb Z\;(n^2=9)$ usando un dominio mayor $D$ y una conjunción con pertenencia.

**35.** Niega $\forall x\in A\;P(x)$.

**36.** Niega $\exists x\in A\;P(x)$.

**37.** Un estudiante escribe “todo entero es racional” como $\forall x\,[x\in\mathbb Z\land x\in\mathbb Q]$. Explica por qué esa forma es incorrecta y corrígela suponiendo un dominio numérico mayor.

**38.** Un estudiante escribe “existe un entero negativo” como $\exists x\,[x\in\mathbb Z\Rightarrow x<0]$. Diagnostica el error y corrige.

### G — Alcance y paréntesis

**39.** En $\forall x\,[P(x)\Rightarrow(Q(x)\lor R)]$, ¿qué apariciones de $x$ están ligadas?

**40.** En $(\forall x\,P(x,y))\lor Q(y)$, ¿qué variables quedan libres?

**41.** Compara $\forall x\,[P(x)\lor Q(x)]$ con $(\forall x\,P(x))\lor Q(x)$. ¿Por qué no son la misma clase de expresión?

**42.** Renombra la variable ligada en $\exists x\,[x>y\land P(x)]$ sin alterar la variable libre $y$.

**43.** Explica por qué sustituir $\forall x\,P(x,y)$ por $\forall y\,P(y,y)$ puede cambiar el significado.

**44.** Distingue $\forall x\,[P(x)\land Q(x)]$ de $(\forall x\,P(x))\land Q(x)$.

### H — Orden de cuantificadores

**45.** Sobre $\mathbb R$, decide la verdad de (a) $\forall x\exists y\;(y>x)$; (b) $\exists y\forall x\;(y>x)$.

**46.** Sobre $\mathbb R$, compara $\forall x\exists y\;(y=x+1)$ con $\exists y\forall x\;(y=x+1)$.

**47.** Sobre $\mathbb Z$, decide $\forall n\exists m\;(m=n+2)$ y su versión con cuantificadores invertidos.

**48.** Sobre $\mathbb Z$, decide (a) $\exists n\forall m\;(n+m=m)$; (b) $\forall m\exists n\;(n+m=m)$.

**49.** Sobre $\mathbb R$, decide $\forall x\exists y\;(xy=1)$. ¿Qué cambia si el dominio de $x$ es $\mathbb R\setminus\{0\}$?

**50.** Sobre $\mathbb R$, decide (a) $\exists y\forall x\;(xy=x)$; (b) $\forall x\exists y\;(xy=x)$.

**51.** Explica por qué $\forall x\forall y\,P(x,y)$ puede reordenarse como $\forall y\forall x\,P(x,y)$, y análogamente para dos existenciales, mientras que el intercambio $\forall x\exists y\leftrightarrow\exists y\forall x$ no es válido en general.

**52.** En el dominio $D=\{1,2\}$, sea $R(x,y)$ la relación “$x=y$”. Decide $\forall x\exists y\,R(x,y)$ y $\exists y\forall x\,R(x,y)$.

### I — Dependencia y elección de testigos

**53.** Para $\forall x\in\mathbb R\exists y\in\mathbb R\;(y=2x)$, da una elección de testigo y explica su dependencia.

**54.** Explica por qué en $\forall x\in\mathbb R\exists y\in\mathbb R\;(y>x)$ no puede usarse un único $y$ fijo para todos los $x$, aunque la afirmación sea verdadera.

**55.** Interpreta la dependencia en $\forall n\in\mathbb Z\exists m\in\mathbb Z\;(m=n^2)$.

**56.** En $\exists m\in\mathbb Z\forall n\in\mathbb Z\;(m+n=n)$, encuentra el testigo y explica por qué debe ser fijo.

**57.** ¿Implica $\forall x\exists y\,R(x,y)$ que para cada $x$ haya exactamente un $y$ con $R(x,y)$? Justifica.

**58.** Sea $M(p,q)$ el predicado “$q$ es madre de $p$”. Traduce y compara: (a) “toda persona tiene alguna madre”; (b) “existe una persona que es madre de todas las personas”.

### J — Existencia única

**59.** Decide $\exists!x\in\mathbb R\;(x+3=5)$ y justifica existencia y unicidad.

**60.** Decide $\exists!n\in\mathbb Z\;(2n=6)$.

**61.** Decide $\exists!x\in\mathbb R\;(x^2=4)$.

**62.** Expande $\exists!x\,P(x)$ usando sólo $\exists$, $\forall$, $\land$, $\Rightarrow$ e igualdad.

### K — Traducción bidireccional

**63.** Formaliza: “Todo entero tiene un entero mayor”.

**64.** Formaliza: “Entre un entero $n$ y su sucesor $n+1$ no existe ningún entero”.

**65.** Formaliza: “Existe un real positivo cuyo cuadrado es menor que él mismo”.

**66.** Formaliza: “No todo número real es positivo”.

**67.** Traduce a lenguaje verbal: $\forall n\in\mathbb Z\;[O(n)\Rightarrow O(n^2)]$, donde $O(k)$ significa “$k$ es impar”.

**68.** Traduce a lenguaje verbal: $\exists m\in\mathbb Z\;\forall n\in\mathbb Z\;(m+n=n)$.

### L — Diagnóstico y síntesis


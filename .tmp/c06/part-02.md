\neg(\forall x\,P(x))\equiv\exists x\,\neg P(x).
$$

Del mismo modo, negar “existe alguno que cumple $P$” significa afirmar “ninguno cumple $P$”, es decir:

$$
\neg(\exists x\,P(x))\equiv\forall x\,\neg P(x).
$$

Estas leyes son los análogos cuantificados de las leyes de De Morgan de C5: al atravesar el cuantificador, la negación **cambia $\forall$ por $\exists$ y $\exists$ por $\forall$**.

### La negación debe seguir avanzando

Supongamos

$$
\forall n\in\mathbb Z\;[E(n)\Rightarrow E(n^2)],
$$

donde $E(n)$ significa “$n$ es par”. Su negación no es simplemente cambiar $\forall$ por $\exists$. Debemos negar también el contenido:

$$
\exists n\in\mathbb Z\;\neg[E(n)\Rightarrow E(n^2)].
$$

Por C5, $\neg(A\Rightarrow B)\equiv A\land\neg B$. Así obtenemos

$$
\exists n\in\mathbb Z\;[E(n)\land\neg E(n^2)].
$$

Es decir: “existe un entero par cuyo cuadrado no es par”.

### “No todos” y “ninguno” no son lo mismo

“no todos los elementos cumplen $P$” se traduce como $\exists x\,\neg P(x)$.

“ningún elemento cumple $P$” se traduce como $\forall x\,\neg P(x)$.

Confundir estas dos frases es uno de los errores lógicos más frecuentes.

## 6.8. Cuantificación restringida

La notación

$\forall x\in A\;P(x)$

dice que sólo nos interesan los elementos de $A$. Conceptualmente puede leerse como

$$
\forall x\;[x\in A\Rightarrow P(x)].
$$

En cambio,

$\exists x\in A\;P(x)$

se interpreta como

$$
\exists x\;[x\in A\land P(x)].
$$

La diferencia entre implicación y conjunción es esencial.

Para un universal restringido, un objeto que no pertenece a $A$ no debe convertirse en contraejemplo. Para un existencial restringido, el testigo debe cumplir simultáneamente dos requisitos: pertenecer a $A$ y satisfacer $P$.

No desarrollaremos aún operaciones con conjuntos; C7 dará a $\in$, subconjunto, unión, intersección y complemento un tratamiento sistemático. Aquí usamos la pertenencia sólo para expresar dominios restringidos.

### Negaciones restringidas

De las reglas anteriores obtenemos directamente:

$$
\neg[\forall x\in A\;P(x)]\equiv\exists x\in A\;\neg P(x),
$$

$$
\neg[\exists x\in A\;P(x)]\equiv\forall x\in A\;\neg P(x).
$$

## 6.9. Alcance, paréntesis y variables

Todo cuantificador tiene un **alcance**: la parte de la fórmula sobre la cual actúa.

Comparemos:

$$
\forall x\,[P(x)\lor Q(x)]
$$

y

$$
(\forall x\,P(x))\lor Q(x).
$$

En la primera fórmula, las dos apariciones de $x$ están bajo el alcance del cuantificador. En la segunda, sólo la aparición dentro de $P(x)$ está ligada; la $x$ de $Q(x)$ queda libre.

Los paréntesis no son decoración. Determinan qué fragmento está cuantificado.

### Renombrar sin capturar

En

$\forall x\,P(x,y)$

podemos cambiar la variable ligada $x$ por $t$ y escribir $\forall t\,P(t,y)$. Pero no deberíamos renombrarla como $y$ sin más, porque la $y$ original era libre. La escritura $\forall y\,P(y,y)$ ha ligado una variable que antes no lo estaba y, por tanto, puede expresar algo distinto.

La disciplina de alcance cumple aquí la misma función que el control de subfórmulas en C5: antes de transformar símbolos debemos saber **qué estructura estamos modificando**.

## 6.10. Dos cuantificadores: el orden importa

Cuando aparecen cuantificadores de distinto tipo, cambiar su orden puede cambiar radicalmente el significado.

Consideremos, sobre $\mathbb R$:

$$
\forall x\;\exists y\;(y>x).
$$

La afirmación es verdadera: dado un real $x$, podemos elegir $y=x+1$.

Comparemos con

$$
\exists y\;\forall x\;(y>x).
$$

Ahora se pide un único real $y$ que sea mayor que **todos** los reales. Eso es imposible.

La diferencia verbal es:

- $\forall x\exists y$: **para cada** $x$ podemos buscar un $y$, posiblemente distinto;
- $\exists y\forall x$: debe existir **un mismo** $y$ que funcione para todos los $x$.

### Cuantificadores del mismo tipo

Bajo condiciones ordinarias,

$\forall x\forall y\,P(x,y)$

y

$\forall y\forall x\,P(x,y)$

expresan lo mismo. Análogamente ocurre con dos existenciales. El peligro aparece especialmente al intercambiar $\forall$ y $\exists$.

## 6.11. Dependencia entre variables y elección de testigos

En

$$
\forall x\;\exists y\;R(x,y),
$$

el valor de $y$ puede elegirse **después** de conocer $x$. Por ello el testigo puede depender de $x$.

Ejemplo:

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y=2x).
$$

Una elección natural es $y=2x$. No estamos exhibiendo un único número real; estamos dando una regla de elección que produce un testigo para cada $x$.

En cambio, en

$$
\exists y\;\forall x\;R(x,y),
$$

el $y$ debe fijarse **antes** de recorrer todos los $x$. Ya no puede adaptarse a cada caso.

Esta idea anticipa un tema futuro: una regla que asigna a cada entrada una salida. C9 estudiará las funciones de forma sistemática. Aquí sólo necesitamos comprender la dependencia lógica.

### Una advertencia

De $\forall x\exists y\,R(x,y)$ no se sigue automáticamente que haya un único $y$ para cada $x$, ni que la elección sea canónica. La afirmación promete existencia local, nada más.

## 6.12. “Existe un único”: el cuantificador de unicidad

La notación

$$
\exists!x\;P(x)
$$

se lee “existe un único $x$ tal que $P(x)$”. Contiene dos afirmaciones distintas:

1. **existencia:** al menos un elemento satisface $P$;
2. **unicidad:** no hay dos elementos distintos que satisfagan $P$.

Una expansión útil es

$$
\exists x\,[P(x)\land\forall y\,(P(y)\Rightarrow y=x)].
$$

El primer $P(x)$ garantiza existencia. El universal posterior dice que cualquier otro candidato $y$ que satisfaga $P$ debe coincidir con $x$.

Por ejemplo,

$\exists!x\in\mathbb R\;(x+3=5)$

es verdadera: $x=2$ existe y cualquier real que satisfaga la ecuación debe ser $2$.

En cambio,

$\exists!x\in\mathbb R\;(x^2=4)$

es falsa. Hay soluciones, pero son dos: $2$ y $-2$.

Existencia y unicidad deben comprobarse por separado.

## 6.13. Traducir lenguaje matemático a símbolos

La traducción correcta comienza identificando tres cosas:

1. **dominio**;
2. **cuantificador**;
3. **predicado y conectivos internos**.

Ejemplo:

> Todo entero par es divisible por $2$.

Una formalización natural es

$$
\forall n\in\mathbb Z\;[E(n)\Rightarrow D_2(n)],
$$

donde $E(n)$ significa “$n$ es par” y $D_2(n)$ significa “$2$ divide a $n$”.

Ejemplo:

> Algunos enteros no son cuadrados perfectos.

Puede escribirse

$$
\exists n\in\mathbb Z\;\neg C(n),
$$

donde $C(n)$ significa “$n$ es un cuadrado perfecto”.

### Palabras que revelan estructura

- “todo”, “cada”, “cualquiera” suelen señalar $\forall$;
- “algún”, “existe”, “hay al menos uno” suelen señalar $\exists$;
- “ningún” suele convertirse en $\forall x\,\neg P(x)$ o, equivalentemente, $\neg\exists x\,P(x)$;
- “no todos” significa $\exists x\,\neg P(x)$;
- “exactamente uno” señala $\exists!$.

No debemos traducir palabra por palabra: debemos traducir **estructura por estructura**.

## 6.14. Traducir símbolos a lenguaje matemático

La dirección inversa exige la misma disciplina. Consideremos

$$
\forall x\in\mathbb R\;\exists y\in\mathbb R\;(y>x).
$$

Una lectura fiel es:

> Para todo número real $x$, existe un número real $y$ mayor que $x$.

Una lectura defectuosa sería:

> Existe un real mayor que todos los reales.

Esa frase corresponde al orden inverso de cuantificadores.

### Leer desde afuera hacia adentro

Una rutina segura es:

1. leer el cuantificador más externo;
2. fijar mentalmente su variable;
3. pasar al siguiente cuantificador;
4. respetar el orden;
5. leer finalmente el predicado interno.

Por ejemplo,

$$
\exists m\in\mathbb Z\;\forall n\in\mathbb Z\;(m+n=n)
$$

se lee: “existe un entero $m$ tal que, para todo entero $n$, se cumple $m+n=n$”. La afirmación resulta verdadera porque $m=0$ funciona para todos los $n$.

## 6.15. Diagnóstico de errores de cuantificación

Los errores más importantes de este capítulo no son de cálculo, sino de significado.

### Error 1: cambiar el cuantificador al traducir

“Todo entero tiene un sucesor entero” no significa “existe un entero que es sucesor de todos los enteros”.

### Error 2: negar sin cambiar cuantificador

La negación de $\forall x\,P(x)$ no es $\forall x\,\neg P(x)$, sino $\exists x\,\neg P(x)$.

### Error 3: ignorar el dominio

El predicado $x^2=2$ produce afirmaciones existenciales distintas sobre $\mathbb Q$ y sobre $\mathbb R$.

### Error 4: confundir testigo dependiente con testigo fijo

En $\forall x\exists y$, el $y$ puede variar con $x$. En $\exists y\forall x$, no.

### Error 5: confundir existencia con unicidad

Encontrar un testigo prueba existencia, no existencia única.

### Error 6: perder el alcance

Mover paréntesis o renombrar variables puede ligar una variable que antes era libre.

Ante una solución dudosa conviene localizar **el primer paso donde cambia el significado**, no sólo el lugar donde aparece un resultado falso.


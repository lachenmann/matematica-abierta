---
{
  "title": "Cómo se demuestra",
  "description": "Capítulo 10 del Tomo I de Álgebra para matemáticos, con 104 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0185",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C10",
  "editorial-id": "MA-BCH-APM-01-010",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0184"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

Hasta aquí hemos demostrado muchas cosas sin detenernos a construir una teoría de la demostración. Al transformar proposiciones, comparar conjuntos, estudiar relaciones o verificar inyectividad, ya hemos usado argumentos directos, contraejemplos, doble inclusión y razonamientos por hipótesis.

C10 organiza esas prácticas.

> **Demostrar no significa convencer por acumulación de ejemplos; significa mostrar que la conclusión es forzada por las hipótesis mediante pasos válidos.**

Este capítulo no ofrece una receta universal. Ofrece un repertorio de arquitecturas, criterios para elegir entre ellas y herramientas para detectar cuándo una prueba está incompleta.

***
## 10.1. Qué es una demostración {#apm-c10-s01}

Una comprobación y una demostración no son lo mismo.

Si calculamos

$$
1+3=4,\qquad 3+5=8,\qquad 5+7=12,
$$

hemos reunido evidencia compatible con la afirmación “la suma de dos impares es par”. No hemos probado la afirmación para todos los enteros impares.

Una demostración debe explicar por qué **todo caso cubierto por las hipótesis** satisface la conclusión.

Conviene distinguir:

- **ejemplo:** muestra un caso;
- **contraejemplo:** destruye una afirmación universal;
- **cálculo:** obtiene un valor;
- **evidencia:** sugiere una conjetura;
- **demostración:** establece una conclusión en todos los casos permitidos.

La prueba comienza por leer con precisión qué se afirma.

***
## 10.2. Anatomía de un teorema {#apm-c10-s02}

Consideremos:

> Para todo entero $n$, si $n$ es par, entonces $n^2$ es par.

La estructura es

$$
\forall n\in\mathbb Z\;(P(n)\Rightarrow Q(n)).
$$

Aquí:

- universo: $\mathbb Z$;
- variable: $n$;
- hipótesis: $n$ es par;
- conclusión: $n^2$ es par.

Una prueba no debe comenzar con manipulaciones azarosas. Debe explotar esa estructura: tomar un entero arbitrario, suponer que es par y llegar a que su cuadrado es par.

Las palabras “para todo”, “existe”, “si… entonces” y “si y sólo si” determinan qué debemos construir.

***
### Del enunciado a las obligaciones de prueba

Antes de escoger un método, escribe qué dato puedes usar y qué debes producir. En una inclusión debes justificar la pertenencia de un elemento arbitrario; en una existencia debes construir un objeto admisible; en una unicidad debes comparar dos candidatos que satisfacen la propiedad. Esta traducción evita empezar con la conclusión como si fuera una hipótesis.

Considera la afirmación: «Si $A\cap B=\varnothing$, todo subconjunto de $A$ es disjunto de $B$». Su forma precisa es
$$
\forall A\,\forall B\,\bigl[A\cap B=\varnothing\Rightarrow
\forall X\,(X\subseteq A\Rightarrow X\cap B=\varnothing)\bigr].
$$
La prueba debe fijar $A,B$ bajo la hipótesis y después un $X\subseteq A$ arbitrario. Si hubiera $x\in X\cap B$, tendríamos $x\in A\cap B$, contradicción. Así $X\cap B=\varnothing$. No hace falta elegir un elemento de $X$ para iniciar la prueba: podría ser vacío.

**Control.** Un borrador empieza «Sea $x\in X$, que existe porque $X\subseteq A$». ¿Qué falla y cómo se repara?

**Solución.** La inclusión no garantiza no vacuidad; $X=\varnothing$ es un contraejemplo a esa inferencia. Se puede iniciar «Supongamos que existe $x\in X\cap B$» y obtener la contradicción anterior. Esa suposición es provisional y precisamente se descarta al final. Si la traducción de $X\subseteq A$ resulta dudosa, vuelve a C6, cuantificación universal, y C7, inclusión y conjunto vacío. Después reconstruye la prueba sin consultar el párrafo anterior.

## 10.3. Prueba directa de una implicación {#apm-c10-s03}

Para demostrar

$$
P\Rightarrow Q,
$$

la estrategia directa consiste en suponer $P$ y deducir $Q$.

Ejemplo. Si $n$ es par, existe $k\in\mathbb Z$ tal que $n=2k$. Entonces

$$
n^2=(2k)^2=4k^2=2(2k^2),
$$

y $2k^2$ es entero. Por tanto $n^2$ es par.

La estructura es:

```text
HIPÓTESIS
   ↓
DEFINICIÓN UTILIZABLE
   ↓
TRANSFORMACIÓN
   ↓
FORMA DE LA CONCLUSIÓN
```

El paso central de una prueba directa suele ser encontrar la representación adecuada de la hipótesis.

***
## 10.4. Variables arbitrarias y universales {#apm-c10-s04}

Para demostrar

$$
\forall x\in A\;P(x),
$$

no elegimos un ejemplo particular. Tomamos

> “Sea $x\in A$ arbitrario”.

La palabra **arbitrario** significa que durante la prueba no podemos usar ninguna propiedad de $x$ que no provenga de $x\in A$ o de las hipótesis.

Si al final demostramos $P(x)$ sin especializar $x$, entonces el argumento vale para todo elemento de $A$.

Este control se vuelve crucial con varias variables: cada una debe tener dominio, y sus dependencias deben mantenerse explícitas.

***
### Un objeto arbitrario no es un ejemplo cómodo

Para probar «todo $x\in D$ tiene la propiedad $P$», el objeto que fijamos sólo puede usar las condiciones que definen $D$. Elegir $x=0$ añade una condición que el enunciado no permite. En cambio, al probar «existe $x\in D$ con $P$» debemos escoger un testigo concreto o construirlo a partir de los datos.

La diferencia se vuelve visible en «para cada $a\in\mathbb R$ existe $x\in\mathbb R$ con $x+a=1$». Fijamos $a$ arbitrario y elegimos $x=1-a$. El testigo depende de $a$; sustituirlo por un único número antes de fijar $a$ cambia el orden de los cuantificadores.

**Control.** Compara $\forall a\in\mathbb R\,\exists x\in\mathbb R\;(x+a=1)$ con $\exists x\in\mathbb R\,\forall a\in\mathbb R\;(x+a=1)$.

**Solución.** La primera es verdadera: $x=1-a$ sirve para cada $a$. La segunda es falsa: el mismo $x$ debería satisfacer $x+0=1$ y $x+1=1$, lo que exigiría a la vez $x=1$ y $x=0$. Dos valores bastan para refutar esta universal; no sustituyen la prueba de la primera. Para recuperar este punto, vuelve a C6, orden de cuantificadores, y escribe qué elecciones pueden depender de cuáles.

## 10.5. Demostraciones de existencia {#apm-c10-s05}

Para demostrar

$$
\exists x\in A\;P(x),
$$

basta encontrar un **testigo** $a\in A$ y verificar $P(a)$.

Ejemplo: existe un real $x$ tal que $x^2=9$. El testigo $x=3$ basta.

Una prueba de existencia tiene dos obligaciones:

1. el objeto propuesto debe pertenecer al dominio exigido;
2. debe satisfacer la propiedad.

En otras situaciones la existencia puede deducirse sin una fórmula explícita, pero en este capítulo privilegiaremos construcciones elementales y controlables.

***
## 10.6. Demostraciones de unicidad {#apm-c10-s06}

Existencia no implica unicidad.

Para demostrar

$$
\exists!x\in A\;P(x),
$$

separamos:

1. **existencia:** mostrar que al menos un objeto cumple $P$;
2. **unicidad:** si $x$ e $y$ cumplen $P$, demostrar $x=y$.

Ejemplo: para cada $a\in\mathbb R$ existe un único $x\in\mathbb R$ tal que $x+a=0$.

Existencia: $x=-a$ funciona.

Unicidad: si $x+a=0$ y $y+a=0$, entonces

$$
x=x+a-a=0-a=y+a-a=y.
$$

***
## 10.7. Bicondicionales y equivalencias {#apm-c10-s07}

Para demostrar

$$
P\Longleftrightarrow Q,
$$

hay dos tareas:

$$
P\Rightarrow Q
$$

y

$$
Q\Rightarrow P.
$$

Una prueba de una sola dirección está incompleta.

Cuando hay tres condiciones $P,Q,R$, a veces es eficiente demostrar un ciclo:

$$
P\Rightarrow Q,\qquad Q\Rightarrow R,\qquad R\Rightarrow P.
$$

Entonces las tres son equivalentes.

También hay que distinguir:

- $P$ es **suficiente** para $Q$: $P\Rightarrow Q$;
- $P$ es **necesaria** para $Q$: $Q\Rightarrow P$.

***
## 10.8. Prueba por contraposición {#apm-c10-s08}

La implicación

$$
P\Rightarrow Q
$$

es lógicamente equivalente a

$$
\neg Q\Rightarrow\neg P.
$$

A veces la segunda forma es mucho más útil.

Ejemplo: si $n^2$ es par, entonces $n$ es par. La contrapositiva dice:

> si $n$ es impar, entonces $n^2$ es impar.

Si $n=2k+1$, entonces

$$
n^2=4k^2+4k+1=2(2k^2+2k)+1,
$$

que es impar. Por contraposición, $n^2$ par implica $n$ par.

La contraposición no cambia la afirmación; cambia el camino.

***
## 10.9. Prueba por contradicción {#apm-c10-s09}

Para demostrar $P$ por contradicción:

1. suponemos $\neg P$;
2. junto con los datos disponibles derivamos una imposibilidad;
3. concluimos que $\neg P$ no puede sostenerse.

Para demostrar una implicación $P\Rightarrow Q$, podemos suponer simultáneamente

$$
P\land\neg Q
$$

y derivar contradicción.

La contradicción debe ser real: por ejemplo $R\land\neg R$, una igualdad imposible o la violación explícita de una hipótesis.

No basta terminar con “esto parece absurdo”.

***
## 10.10. Prueba por casos {#apm-c10-s10}

A veces el universo se divide naturalmente.

Para todo real $x$, la definición de valor absoluto separa dos posibilidades: $|x|=x$ cuando $x\ge0$ y $|x|=-x$ cuando $x<0$.

Una prueba que usa valor absoluto puede necesitar separar esos dos casos.

Los casos deben ser:

- **exhaustivos:** cubren todas las posibilidades;
- **compatibles con las hipótesis**;
- **cerrados:** cada caso llega a la conclusión.

Una división “$x>0$ o $x<0$” no es exhaustiva si $x=0$ es posible.

***
## 10.11. Pruebas de conjuntos: doble inclusión {#apm-c10-s11}

Para demostrar

$$
A=B,
$$

la estrategia estándar es probar

$$
A\subseteq B
$$

y

$$
B\subseteq A.
$$

Cada inclusión se reduce a pertenencia.

Ejemplo:

$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C).
$$

Para la primera inclusión tomamos $x$ en el lado izquierdo. Entonces $x\in A$ y $x\in B$ o $x\in C$. Por casos, $x\in A\cap B$ o $x\in A\cap C$. Así pertenece al lado derecho.

La inclusión contraria se prueba recorriendo el razonamiento en la dirección adecuada, no simplemente diciendo “análogamente” si el paso requiere una idea distinta.

***
## 10.12. Pruebas con funciones {#apm-c10-s12}

Las definiciones de C9 son plantillas de objetivos.

Para demostrar que $f$ es inyectiva:

1. tomar $x_1,x_2$ del dominio;
2. suponer $f(x_1)=f(x_2)$;
3. demostrar $x_1=x_2$.

Para demostrar sobreyectividad:

1. tomar $y$ arbitrario en el codominio;
2. construir $x$ en el dominio;
3. verificar $f(x)=y$.

La prueba debe respetar el **tipo** de cada objeto. Una “preimagen” candidata fuera del dominio no prueba sobreyectividad.

***
## 10.13. Cómo se refuta: contraejemplos {#apm-c10-s13}

La negación de

$$
\forall x\in A\;(P(x)\Rightarrow Q(x))
$$

es

$$
\exists x\in A\;(P(x)\land\neg Q(x)).
$$

Por eso un solo contraejemplo basta: debe satisfacer la hipótesis y violar la conclusión.

Para refutar

> “si $g\circ f$ es inyectiva, entonces $g$ es inyectiva”,

no sirve elegir funciones cuya composición no sea inyectiva. Debemos construir un caso donde el antecedente sea verdadero y el consecuente falso.

Un contraejemplo es una pequeña demostración de falsedad.

***
## 10.14. Lemas y arquitectura de una prueba larga {#apm-c10-s14}

Una prueba larga puede contener un obstáculo recurrente. Conviene aislarlo.

Un **lema** es una proposición auxiliar que se demuestra porque simplifica el argumento principal.

Esquema:

```text
OBJETIVO PRINCIPAL
   ↓
OBSTÁCULO INTERMEDIO
   ↓
LEMA
   ↓
PRUEBA DEL LEMA
   ↓
RETORNO AL OBJETIVO
```

El lema no debe ser más difícil que el teorema sin aportar estructura. Su utilidad está en separar dependencias.

***
### Aislar un lema que realmente resuelve un obstáculo

Un lema ayuda cuando su conclusión es exactamente el dato que falta en la prueba principal. Veamos una afirmación con dos objetivos: para $A,B$ disjuntos y $X,Y\subseteq A\cup B$, si
$$
X\cap A=Y\cap A,\qquad X\cap B=Y\cap B,
$$
entonces $X=Y$.

Sin lema, fijamos $x\in X$. Como $X\subseteq A\cup B$, pertenece a $A$ o a $B$. En el primer caso la igualdad de las intersecciones con $A$ da $x\in Y$; en el segundo usamos la igualdad con $B$. Obtenemos $X\subseteq Y$ y repetimos el argumento empezando con $y\in Y$ para obtener $Y\subseteq X$.

El mecanismo repetido se puede aislar: **si $Z\subseteq A\cup B$, entonces $Z=(Z\cap A)\cup(Z\cap B)$**. En efecto, cada elemento de $Z$ está en una de las dos intersecciones; recíprocamente, cualquiera de esas intersecciones está contenida en $Z$. Ahora la prueba principal queda
$$
X=(X\cap A)\cup(X\cap B)=(Y\cap A)\cup(Y\cap B)=Y.
$$
La versión corta depende de una prueba completa del lema; omitirla sólo desplazaría la dificultad.

**Control.** ¿Dónde se usó $A\cap B=\varnothing$? ¿Puede retirarse esa hipótesis?

**Solución.** No se usó: la unión cubre los elementos aunque puedan pertenecer a ambas partes. La afirmación sigue siendo cierta sin disjunción, conservando $X,Y\subseteq A\cup B$. Esta revisión distingue una hipótesis innecesaria de una necesaria. Si falta el fundamento del lema, vuelve a C7, distributividad y doble inclusión, y demuéstralo con pertenencias antes de usar identidades.

## 10.15. Elegir estrategia y reparar pruebas {#apm-c10-s15}

No existe un algoritmo universal, pero sí preguntas útiles:

1. ¿qué forma lógica tiene el objetivo?;
2. ¿qué dicen exactamente las definiciones?;
3. ¿puedo trabajar directamente desde las hipótesis?;
4. ¿la contraposición vuelve concreta la conclusión?;
5. ¿suponer la negación produce información fuerte?;
6. ¿hay casos naturales?;
7. ¿necesito construir un testigo?;
8. ¿debo demostrar unicidad?;
9. ¿una igualdad exige dos inclusiones?;
10. ¿un lema separaría el paso difícil?

Errores frecuentes:

- asumir la conclusión;
- usar el recíproco de un resultado;
- cambiar un cuantificador;
- elegir un ejemplo en lugar de un objeto arbitrario;
- omitir una dirección;
- dividir en casos no exhaustivos;
- introducir un objeto que no se sabe que existe;
- ocultar el paso principal con “obvio”.

### Cinco niveles para leer una demostración

Cuando una prueba ya está escrita, conviene no verla como una secuencia plana de líneas. Podemos distinguir cinco niveles:

1. **Estrategia:** la elección global del camino. Por ejemplo, prueba directa, contraposición, contradicción, casos o doble inclusión.
2. **Arquitectura:** la organización del argumento en subobjetivos, direcciones, casos, lemas y dependencias.
3. **Mecanismo:** la idea matemática o lógica que produce el avance decisivo. Puede ser usar una definición para obtener una representación útil, aplicar inyectividad a una igualdad, explotar una contradicción o introducir un testigo adecuado.
4. **Técnica:** las operaciones locales con las que ejecutamos el mecanismo: manipular una igualdad, factorizar, sustituir, perseguir pertenencias, componer funciones o simplificar una expresión.
5. **Cierre:** el momento en que verificamos que lo obtenido coincide exactamente con la conclusión exigida y que todas las direcciones, casos u obligaciones abiertas han sido atendidas.

Estos niveles no son sinónimos. Dos pruebas pueden usar la misma técnica algebraica y estrategias distintas; o compartir estrategia pero organizar de manera diferente su arquitectura.

Al leer una demostración ajena, una buena práctica es intentar identificar los cinco niveles y después ocultar el texto para reconstruir el argumento. Si sólo podemos repetir las líneas pero no explicar por qué se eligió el camino ni cuál es el mecanismo decisivo, todavía no comprendemos completamente la prueba.

***
### Del ensayo a la demostración final

Explorar permite probar casos, escribir una cuenta incompleta o buscar una identidad. Después hay que separar lo observado del mecanismo que vale para todos los objetos. Para estudiar si $x,y\geq0$ y $x^2=y^2$ obligan a $x=y$, ensayar $x=2,y=2$ sólo confirma un caso. El mecanismo es
$$
0=x^2-y^2=(x-y)(x+y).
$$
En los reales, un producto nulo tiene algún factor nulo. Si $x-y=0$, terminamos. Si $x+y=0$, la no negatividad obliga a $x=y=0$: si uno fuera positivo, la suma sería positiva. También en ese caso $x=y$.

La prueba final empieza con dos reales arbitrarios bajo las hipótesis, no con los números del ensayo. Conserva el caso $x+y=0$ porque dividir directamente por $x+y$ lo perdería. Una buena explicación puede mencionar cómo se encontró la factorización, pero la justificación debe funcionar sin esa historia.

**Control.** Retira $x,y\geq0$. ¿Falla la cuenta o falla la conclusión?

**Solución.** La factorización sigue siendo válida. La conclusión $x=y$ falla para $x=1,y=-1$. Lo que sí se deduce para reales cualesquiera es $x=y$ o $x=-y$, según el factor que se anule. Para reconstruir el mecanismo, vuelve a C3, factorización y transformaciones condicionadas; después explica por qué no se puede cancelar $x+y$ sin comprobarlo.

## 10.16. Escribir y cerrar una demostración {#apm-c10-s16}

Una prueba final debe poder leerse sin reconstruir la intención del autor.

Debe quedar claro:

- qué se supone;
- qué objetos se introducen;
- de qué conjuntos provienen;
- qué resultado justifica cada paso sustantivo;
- cuándo se alcanza la conclusión.

El proceso de descubrimiento puede ser desordenado. La exposición final no tiene por qué imitarlo.

### Revisar la prueba desde la conclusión

Una revisión útil pregunta: ¿qué conclusión exacta se alcanzó?, ¿se probaron todas las direcciones?, ¿cada elección existe?, ¿los casos cubren el universo?, ¿algún paso exige una hipótesis no declarada? No basta con que cada cuenta parezca correcta: una prueba puede demostrar algo más débil que lo pedido.

En «$A\cap B=A$ si y sólo si $A\subseteq B$», probar que la igualdad implica la inclusión deja pendiente la vuelta. Para esa vuelta, si $x\in A$, la hipótesis $A\subseteq B$ da $x\in B$, luego $x\in A\cap B$; así $A\subseteq A\cap B$. La otra inclusión $A\cap B\subseteq A$ viene de la definición. Esas dos inclusiones cierran la igualdad y, con la dirección inicial, el bicondicional.

**Control.** Un texto sobre una función $f:A\to B$ termina «todo $b\in f(A)$ tiene preimagen; por tanto $f$ es sobreyectiva». ¿Qué conclusión justifica realmente?

**Solución.** Justifica que $f:A\to f(A)$, con el codominio restringido a su imagen, es sobreyectiva. Para el codominio declarado $B$ falta $f(A)=B$. Por ejemplo, $f:\{0\}\to\{0,1\}$ dada por $f(0)=0$ cumple la frase inicial y no es sobreyectiva sobre $B$. Recupera en C9 la diferencia entre imagen y codominio; luego revisa que cada «arbitrario» de la prueba recorra el conjunto exigido por la conclusión.

Cerramos con una nueva pregunta:

> **¿Cómo demostrar una afirmación $P(n)$ para todos los naturales cuando cada caso está conectado estructuralmente con el siguiente?**

Esa pregunta abrirá C11 y la inducción matemática.

***
# Ejercicios

Los ejercicios son originales para *Álgebra para matemáticos* y se calibran con el corpus rector del capítulo. Los identificadores editoriales permanecen en comentarios internos no renderizados.

## A. Anatomía y forma lógica


**1.** **Nivel A.** En «para todo real $x$, si $x>2$, entonces $x^2>4$», identifica universo, cuantificador, hipótesis y conclusión.


**2.** **Nivel A.** Explica por qué comprobar la igualdad $1+3=4$, $3+5=8$ y $5+7=12$ no demuestra que la suma de dos impares cualesquiera sea par.


**3.** **Nivel B.** Reescribe «todo elemento de $A\cap B$ pertenece a $A$» en notación cuantificada.


**4.** **Nivel B.** En «existe un real $x$ tal que $x^2=2$», ¿qué debe proporcionar una prueba constructiva?


**5.** **Nivel B.** ¿Qué dos tareas contiene una afirmación de la forma «existe un único $x$ tal que $P(x)$»?


**6.** **Nivel C.** Explica por qué demostrar sólo $P\Rightarrow Q$ no basta para establecer $P\Leftrightarrow Q$.

## B. Prueba directa y universales


**7.** **Nivel B.** Demuestra directamente que la suma de dos enteros pares es par.


**8.** **Nivel B.** Demuestra que el producto de un entero par por cualquier entero es par.


**9.** **Nivel B.** Demuestra que si $x>3$, entonces $2x+1>7$.


**10.** **Nivel C.** Demuestra que para todo $A,B,C$, si $A\subseteq B$ y $B\subseteq C$, entonces $A\subseteq C$.


**11.** **Nivel C.** Demuestra que $A\cap B\subseteq A\cup B$.


**12.** **Nivel C.** Demuestra que si $f:A\to B$ es inyectiva y $S\subseteq A$, entonces la restricción $f|_S:S\to B$ es inyectiva.


**13.** **Nivel C.** Demuestra que si $f:A\to B$ y $g:B\to C$ son inyectivas, entonces $g\circ f$ es inyectiva.


**14.** **Nivel D.** Demuestra que si $A\subseteq B$, entonces $\mathcal P(A)\subseteq\mathcal P(B)$.

## C. Existencia y unicidad


**15.** **Nivel B.** Demuestra que para cada $a\in\mathbb R$ existe $x\in\mathbb R$ tal que $x+a=0$.


**16.** **Nivel C.** Demuestra que ese $x$ es único.


**17.** **Nivel B.** Demuestra que para todo real $a\ne0$ existe un único real $x$ tal que $ax=1$.


**18.** **Nivel C.** Sea $f:A\to B$ biyectiva. Demuestra que para cada $b\in B$ existe un único $a\in A$ con $f(a)=b$.


**19.** **Nivel C.** Da un ejemplo donde exista un objeto con cierta propiedad pero no sea único.


**20.** **Nivel D.** Decide si es verdadera la afirmación: «para todo conjunto $A$ existe un único subconjunto $X\subseteq A$ tal que $X\cup A=A$ y $X\cap A=X$». Si es falsa, refútala y explica exactamente qué falla.

## D. Bicondicionales


**21.** **Nivel B.** Demuestra: un entero $n$ es par si y sólo si $n+2$ es par.


**22.** **Nivel C.** Demuestra $A\subseteq B$ si y sólo si $A\cap B=A$.


**23.** **Nivel C.** Demuestra $A\subseteq B$ si y sólo si $A\cup B=B$.


**24.** **Nivel C.** Demuestra que $f:A\to B$ es sobreyectiva si y sólo si $\operatorname{Im}(f)=B$.


**25.** **Nivel D.** Demuestra que para un real $x$, $x^2=0$ si y sólo si $x=0$.


**26.** **Nivel D.** Organiza un ciclo de implicaciones para demostrar la equivalencia entre: (i) $A=B$; (ii) $A\subseteq B$ y $B\subseteq A$; (iii) $A\triangle B=\varnothing$.

## E. Contraposición


**27.** **Nivel B.** Demuestra por contraposición: si $n^2$ es par, entonces $n$ es par.


**28.** **Nivel C.** Demuestra por contraposición: si $ab$ es impar, entonces $a$ y $b$ son impares.


**29.** **Nivel C.** Demuestra por contraposición: si $x+y$ es irracional, entonces al menos uno de $x,y$ es irracional.


**30.** **Nivel C.** Demuestra: si $A\not\subseteq B$, entonces existe $x$ tal que $x\in A$ y $x\notin B$.


**31.** **Nivel D.** Demuestra por contraposición: si $f:A\to B$ no es inyectiva, entonces existe un subconjunto $S\subseteq A$ tal que $f^{-1}(f(S))\ne S$.


**32.** **Nivel D.** Compara brevemente una prueba directa y una prueba por contraposición del enunciado «si $n^2$ es par, entonces $n$ es par».

## F. Contradicción


**33.** **Nivel B.** Demuestra por contradicción que no existe un real $x$ tal que $x>0$ y $x<0$ simultáneamente.


**34.** **Nivel C.** Demuestra por contradicción que una función constante $f:A\to B$ con $A$ que contiene dos elementos distintos no es inyectiva.


**35.** **Nivel C.** Demuestra que no existe un conjunto $A$ tal que $A\in\varnothing$.


**36.** **Nivel C.** Demuestra que si $A\subsetneq B$, entonces no puede ocurrir simultáneamente $B\subseteq A$.


**37.** **Nivel D.** Sea $f:A\to B$ biyectiva. Demuestra por contradicción que su inversa es única.


**38.** **Nivel D.** Explica por qué una prueba por contradicción de $P\Rightarrow Q$ puede comenzar suponiendo $P$ y $\neg Q$.

## G. Casos


**39.** **Nivel B.** Demuestra por casos que $|x|\ge0$ para todo real $x$.


**40.** **Nivel C.** Demuestra que para todo entero $n$, $n(n+1)$ es par.


**41.** **Nivel C.** Demuestra que para todo real $x$, $x^2=|x|^2$.


**42.** **Nivel C.** Demuestra que si $x\in A\cup B$, entonces $x\in A$ o $x\in B$, y usa esa disyunción para justificar una prueba por casos.


**43.** **Nivel D.** Demuestra que $\max\{x,y\}\ge(x+y)/2$ para todos los reales $x,y$ mediante dos casos.


**44.** **Nivel D.** Detecta el error en una prueba que divide «$x>0$ o $x<0$» para demostrar una afirmación sobre todo real $x$.

## H. Pruebas de conjuntos


**45.** **Nivel B.** Demuestra $A\cap(B\cup C)\subseteq(A\cap B)\cup(A\cap C)$.


**46.** **Nivel B.** Demuestra la inclusión contraria y concluye la distributividad.


**47.** **Nivel C.** Demuestra $A\setminus(B\cup C)=(A\setminus B)\cap(A\setminus C)$.


**48.** **Nivel C.** Demuestra $\mathcal P(A)\cap\mathcal P(B)=\mathcal P(A\cap B)$.


**49.** **Nivel D.** Refuta $A\setminus(B\cap C)=(A\setminus B)\cap(A\setminus C)$ con un contraejemplo.


**50.** **Nivel D.** Demuestra que $A=B$ si y sólo si $A\triangle B=\varnothing$.

## I. Pruebas con funciones


**51.** **Nivel B.** Demuestra que $f:\mathbb R\to\mathbb R$, $f(x)=3x-1$, es inyectiva.


**52.** **Nivel B.** Demuestra que la misma función es sobreyectiva.


**53.** **Nivel C.** Demuestra que si $g\circ f$ es inyectiva, entonces $f$ es inyectiva.


**54.** **Nivel C.** Demuestra que si $g\circ f$ es sobreyectiva, entonces $g$ es sobreyectiva.


**55.** **Nivel D.** Demuestra que si $f$ tiene inversa izquierda, entonces es inyectiva.


**56.** **Nivel D.** Demuestra que si $f$ tiene inversa derecha, entonces es sobreyectiva.

## J. Contraejemplos y refutación


**57.** **Nivel B.** Refuta «si $a+b$ es par, entonces $a$ y $b$ son pares».


**58.** **Nivel B.** Refuta «si $A\cap B=\varnothing$, entonces $A=\varnothing$ o $B=\varnothing$».


**59.** **Nivel C.** Refuta «si $f$ es sobreyectiva, entonces es inyectiva».


**60.** **Nivel C.** Refuta «si $g\circ f$ es inyectiva, entonces $g$ es inyectiva».


**61.** **Nivel D.** Explica por qué un ejemplo que viola la hipótesis de una implicación no puede refutarla.


**62.** **Nivel D.** Refuta «para todos $A,B,C$, de $A\cup C=B\cup C$ se sigue $A=B$».

## K. Diagnóstico y reparación


**63.** **Nivel C.** Diagnostica: «Supongamos que $n^2$ es par. Como $n$ es par, $n=2k$, luego $n^2$ es par».


**64.** **Nivel C.** Diagnostica: «Para demostrar que todo real tiene cuadrado no negativo, tomo $x=2$. Como $2^2\ge0$, listo».


**65.** **Nivel D.** Diagnostica: «Como para cada $x$ existe algún $y$ con $P(x,y)$, existe un mismo $y$ que sirve para todos los $x$».


**66.** **Nivel D.** Diagnostica una prueba de $P\Leftrightarrow Q$ que sólo demuestra $P\Rightarrow Q$.

## L. Síntesis


**67.** **Nivel D.** Sin método indicado, demuestra que si $A\subseteq B$, entonces $A\cap C\subseteq B\cap C$.


**68.** **Nivel D.** Sin método indicado, demuestra que si $n$ es impar, entonces $n^2+2n$ es impar.


**69.** **Nivel D.** Sin método indicado, demuestra que si $x^2<1$, entonces $-1<x<1$.


**70.** **Nivel E.** Demuestra que si $f:A\to B$ y $g:B\to C$ son biyectivas, entonces $g\circ f$ es biyectiva.


**71.** **Nivel E.** Demuestra que $A\subseteq B$ si y sólo si $A\setminus B=\varnothing$.


**72.** **Nivel E.** Decide y demuestra o refuta: «si $A\times C=B\times C$ y $C\ne\varnothing$, entonces $A=B$».

## M. Problemas avanzados tipo prueba


**73.** **Nivel E.** Demuestra el teorema «si $n^2$ es par, entonces $n$ es par» de dos maneras:  
(a) por contraposición;  
(b) por contradicción, suponiendo que $n$ es impar.  
Compara las dos pruebas y explica cuál hace más visible la estructura lógica.


**74.** **Nivel F.** Demuestra que para una función $f:A\to B$ son equivalentes:

(i) $f$ es inyectiva;  
(ii) para todo $S\subseteq A$, $f^{-1}(f(S))=S$;  
(iii) para todos $S,T\subseteq A$, $f(S\cap T)=f(S)\cap f(T)$.

Usa al menos una dirección por contraposición.


**75.** **Nivel F.** Demuestra por doble inclusión la identidad
$$
A\setminus(B\triangle C)=
(A\cap B\cap C)\cup(A\setminus(B\cup C)).
$$
Explica al final qué condición lógica sobre pertenencia expresa la identidad.


**76.** **Nivel F.** Sean $f:A\to B$ y $g:B\to C$. Supón que $g\circ f$ es biyectiva.

(a) Demuestra que $f$ es inyectiva y $g$ es sobreyectiva.  
(b) Prueba que si además $f$ es sobreyectiva, entonces $g$ es inyectiva.  
(c) Concluye que, bajo esa hipótesis adicional, ambas funciones son biyectivas.


**77.** **Nivel F.** La afirmación
> «Si $A\cup C=B\cup C$, entonces $A=B$»
es falsa.

(a) Construye un contraejemplo donde $A,B,C$ sean todos no vacíos y distintos entre sí.  
(b) Formula una hipótesis adicional natural que, junto con $A\cup C=B\cup C$, sí permita concluir $A=B$.  
(c) Demuestra tu versión corregida.


**78.** **Nivel G.** Demuestra el siguiente resultado usando un lema explícito:

> Si $f:A\to B$ es inyectiva y $g:B\to C$ es tal que $g\circ f$ es sobreyectiva, entonces la restricción $g|_{f(A)}:f(A)\to C$ es biyectiva si y sólo si $g\circ f$ es inyectiva.

Formula y demuestra primero un lema adecuado sobre la biyección $f:A\to f(A)$.


**79.** **Nivel G.** La siguiente «prueba» intenta demostrar que toda función sobreyectiva es inyectiva:

> Sea $f:A\to B$ sobreyectiva. Si $f(x_1)=f(x_2)$, como todo elemento de $B$ tiene preimagen, la preimagen de $f(x_1)$ existe. Por tanto esa preimagen debe ser $x_1=x_2$.

(a) Localiza exactamente el error.  
(b) Construye un contraejemplo mínimo.  
(c) Reescribe una afirmación verdadera cercana y demuéstrala.


**80.** **Nivel G.** Sin indicación de método, demuestra:

> Si $A,B,C$ son conjuntos y
> $$
> A\cap C\subseteq B\cap C
> \qquad\text{y}\qquad
> A\setminus C\subseteq B\setminus C,
> $$
> entonces $A\subseteq B$.

Después explica por qué una prueba por casos es la estrategia natural y por qué una contradicción sería menos económica.

***
## N. Construir pruebas con ayuda decreciente


**81.** Sean $A,B$ conjuntos. Completa una prueba de que $A\cap B=\varnothing$ si y sólo si $A\subseteq A\setminus B$. En la ida, fija $x\in A$ y justifica $x\notin B$. En la vuelta, explica por qué un supuesto $x\in A\cap B$ llevaría a contradicción. Cierra ambas direcciones y comprueba $A=\varnothing$.


**82.** Para $x,y\in\mathbb R$ con $x,y\geq0$, demuestra que $x+y=0$ si y sólo si $x=y=0$. Escribe primero las dos obligaciones. En la dirección difícil puedes empezar «si $x>0$, entonces…». Explica dónde interviene cada hipótesis de signo.


**83.** Sea $C\neq\varnothing$. Demuestra $A\times C\subseteq B\times C$ si y sólo si $A\subseteq B$. Separa las direcciones, pero completa tú los detalles. Identifica la elección que necesita no vacuidad y da un contraejemplo si se retira esa hipótesis.


**84.** Sea $f:A\to B$ y define $F:A\to A\times B$ por $F(a)=(a,f(a))$. Demuestra que es una función inyectiva. Decide exactamente cuándo es sobreyectiva: trata primero $A=\varnothing$ y después $A\neq\varnothing$. No se proporciona un esquema de prueba.


**85.** Demuestra que, dados $a,b\in\mathbb R$ con $a\neq0$, existe un único $x\in\mathbb R$ que satisface $ax+b=x$. Determina antes si la hipótesis indicada es suficiente. Si no lo es, sustituye el enunciado por una clasificación completa según $a,b$ y demuestra esa clasificación.


**86.** Para $A,B$ disjuntos, demuestra que todo $X\subseteq A\cup B$ admite una única representación $X=U\cup V$ con $U\subseteq A$ y $V\subseteq B$. Incluye existencia, unicidad y los casos vacíos. Después de escribir la prueba, señala qué paso no sobrevive si $A,B$ se solapan.

## O. Hipótesis tácitas y reparación de enunciados


**87.** Diagnostica: «Si $x^2>y^2$, entonces $x>y$, pues de $(x-y)(x+y)>0$ se cancela el factor $x+y$». Da un contraejemplo real y una hipótesis adicional de signo que haga verdadera la conclusión. Prueba el enunciado reparado e indica qué paso necesitaba esa hipótesis.


**88.** Un borrador concluye de $f\circ h=g\circ h$ que $f=g$, «eligiendo para cada $b\in B$ algún $a\in A$ con $h(a)=b$». Aquí $h:A\to B$ y $f,g:B\to C$. Identifica la hipótesis tácita. Construye un contraejemplo con todos los conjuntos no vacíos y prueba la conclusión al añadir dicha hipótesis.


**89.** Para una relación $R\subseteq A\times A$, un texto dice: «Si $R$ es simétrica y transitiva, es reflexiva: como $aRb$, también $bRa$ y entonces $aRa$». Localiza el dato no justificado. Da un contraejemplo con $A\neq\varnothing$. Demuestra que la reparación $\forall a\in A\,\exists b\in A\;(aRb)$ basta y que, bajo simetría y transitividad, es también necesaria para reflexividad.


**90.** Diagnostica: «Si $A\times B=A\times C$, fijamos $a\in A$ y concluimos $B=C$». Refuta sin usar $B=C$. Repara mediante una hipótesis sobre $A$ y demuestra ambas inclusiones. Después decide si la afirmación universal “para todos $B,C$, esa igualdad de productos implica $B=C$” caracteriza esa hipótesis sobre $A$.


**91.** Se afirma: «Para cualquier $S\subseteq\mathbb R$, si $t\notin S$ entonces $t\notin\{s^2:s\in S\}$; basta observar que $t$ no es una entrada». Refuta y escribe una condición exacta de pertenencia a la imagen de cuadrados. Úsala para decidir, justificadamente, si $1$ y $4$ pertenecen a la imagen de $S=\{-2,0\}$.


**92.** Un argumento de unicidad dice: «$X\subseteq A$ y $X\cup B=A\cup B$; al quitar $B$, queda $X=A$». Da un contraejemplo. Clasifica todos los $X\subseteq A$ que cumplen la igualdad y demuestra que la solución es única si y sólo si $A\cap B=\varnothing$.

## P. Diseñar lemas útiles


**93.** Quieres demostrar que si $A\cup B=C\cup D$ y las dos uniones son disjuntas, entonces $A\cap C$, $A\cap D$, $B\cap C$, $B\cap D$ son disjuntos dos a dos y su unión es el conjunto común. Diseña un lema sobre cruzar dos descomposiciones disjuntas, pruébalo y aplícalo. Explica por qué el lema no debe exigir que las cuatro piezas sean no vacías.


**94.** Sea $f:A\to B$ y $X,Y\subseteq A$. Para probar $f(X\cup Y)=f(X)\cup f(Y)$, propone un lema sobre testigos de pertenencia a una imagen y úsalo en ambas inclusiones. Después decide si el mismo esquema prueba $f(X\cap Y)=f(X)\cap f(Y)$ y localiza exactamente el obstáculo.


**95.** Demuestra que para reales $a,b,c$ con $a<b$ hay al menos un número $t$ tal que $a<t<b$ y $t\neq c$. Diseña primero un lema que construya dos candidatos distintos dentro del intervalo. No invoques densidad ni infinitud como resultados sin demostrar.


**96.** Sean $f:A\to B$ y $g:C\to D$, y define $H:A\times C\to B\times D$ mediante $H(a,c)=(f(a),g(c))$. Con $A,C\neq\varnothing$, prueba que $H$ es inyectiva si y sólo si $f,g$ lo son. Formula un lema que permita recuperar una coordenada fijando la otra. Explica qué se pierde si se admite un factor vacío y da un ejemplo concreto.


**97.** Para $r,s\in\mathbb R$, prueba $\max\{r,s\}+\min\{r,s\}=r+s$ y usa ese resultado para demostrar que $\max\{r,s\}=(r+s+|r-s|)/2$. Diseña un único lema por casos que sirva a ambos objetivos. Explica cómo incluye $r=s$.


**98.** Dados conjuntos $A,B,C,D$, demuestra
$$
(A\times C)\cap(B\times D)=(A\cap B)\times(C\cap D).
$$
Diseña y prueba un lema de pertenencia de pares que reduzca la igualdad a condiciones sobre coordenadas. Usa el lema en los dos sentidos y revisa todos los casos en que algún conjunto es vacío.

## Q. Síntesis y elección autónoma del método


**99.** Sea $A\subseteq U$. Caracteriza todos los $X\subseteq U$ que satisfacen simultáneamente $A\cup X=U$ y $A\cap X=\varnothing$, y demuestra existencia y unicidad. Al terminar, explica por qué la clasificación pide dos condiciones, y qué familias de candidatos deja cada una por separado.


**100.** Para $a,b\in\mathbb R$, decide exactamente cuándo la ecuación $|x-a|=b$ tiene cero, una o dos soluciones reales. Demuestra la clasificación completa y, sólo al final, justifica tu método y explica por qué los casos extremos no deben omitirse.


**101.** Sean $f:A\to B$ y $g:B\to A$ tales que $g\circ f=\operatorname{id}_A$. Demuestra que, si además $g$ es inyectiva, entonces $f\circ g=\operatorname{id}_B$. Refuta la conclusión si se retira la hipótesis adicional. Explica después por qué aplicar $g$ a dos objetos fue útil y por qué no bastaba con suponer la conclusión.


**102.** Sea $R\subseteq A\times A$ reflexiva y transitiva. Para cada $a\in A$, define $R(a)=\{x\in A:aRx\}$. Demuestra que $aRb$ si y sólo si $R(b)\subseteq R(a)$. Deduce que, si además $R$ es antisimétrica, la función $a\mapsto R(a)$ de $A$ a $\mathcal P(A)$ es inyectiva. Explica después qué hipótesis sostiene cada dirección y muestra un fallo sin reflexividad.


**103.** Sea $U$ un conjunto y define $T:\mathcal P(U)\to\mathcal P(U)$ por $T(X)=U\setminus X$. Demuestra que $T$ es biyectiva y caracteriza sus puntos fijos, es decir, los $X$ con $T(X)=X$. Distingue $U=\varnothing$ de $U\neq\varnothing$. Después explica cómo una misma identidad organiza existencia, unicidad y el análisis de puntos fijos.


**104.** Una conclusión afirma: «Si para cada subconjunto no vacío $S\subseteq A$ la restricción $f|_S$ es inyectiva, entonces $f:A\to B$ es inyectiva». Prueba la afirmación, determina si basta comprobar los subconjuntos de exactamente dos elementos y demuestra la equivalencia correspondiente, incluyendo $A$ vacío o unitario. Refuta la versión que sólo comprueba subconjuntos unitarios. Explica al final cuál es la información mínima que revela una colisión.

# Soluciones razonadas

## A. Anatomía y forma lógica


### 1

Universo: $\mathbb R$. Cuantificador: universal. Hipótesis: $x>2$. Conclusión: $x^2>4$. La forma es $\forall x\in\mathbb R\,(x>2\Rightarrow x^2>4)$.


### 2

Los cálculos sólo verifican tres casos. La afirmación es universal y exige cubrir todo par de enteros impares. La evidencia puede sugerir la conjetura, pero no fuerza los casos no comprobados.


### 3

$\forall x\,(x\in A\cap B\Rightarrow x\in A)$. Si se fija un universo $U$, puede escribirse $\forall x\in U\,(x\in A\cap B\Rightarrow x\in A)$.


### 4

Debe proporcionar un testigo real concreto y verificar que su cuadrado es $2$. Por ejemplo, puede tomarse como testigo el real no negativo cuyo cuadrado es $2$, si su existencia ya ha sido establecida.


### 5

Existencia: encontrar o garantizar al menos un $x$ con $P(x)$. Unicidad: demostrar que cualesquiera dos objetos que satisfagan $P$ deben coincidir.


### 6

El bicondicional exige simultáneamente $P\Rightarrow Q$ y $Q\Rightarrow P$. La primera dirección sólo establece suficiencia de $P$ para $Q$, no necesidad.

## B. Prueba directa y universales


### 7

Sean $a=2m$ y $b=2n$ con $m,n\in\mathbb Z$. Entonces $a+b=2m+2n=2(m+n)$. Como $m+n\in\mathbb Z$, la suma es par.


### 8

Sea $a=2m$ par y $b\in\mathbb Z$. Entonces $ab=2(mb)$. Como $mb\in\mathbb Z$, el producto es par.


### 9

De $x>3$ se sigue $2x>6$ al multiplicar por $2>0$. Sumando $1$ obtenemos $2x+1>7$.


### 10

Sea $x\in A$ arbitrario. Como $A\subseteq B$, $x\in B$. Como $B\subseteq C$, $x\in C$. Por arbitrariedad, $A\subseteq C$.


### 11

Sea $x\in A\cap B$. Entonces $x\in A$ y $x\in B$; en particular $x\in A$ o $x\in B$, luego $x\in A\cup B$.


### 12

Sean $x_1,x_2\in S$ y supón $f|_S(x_1)=f|_S(x_2)$. Esto significa $f(x_1)=f(x_2)$. Como $f$ es inyectiva, $x_1=x_2$.


### 13

Supón $(g\circ f)(x_1)=(g\circ f)(x_2)$. Entonces $g(f(x_1))=g(f(x_2))$. Inyectividad de $g$ da $f(x_1)=f(x_2)$; inyectividad de $f$ da $x_1=x_2$.


### 14

Sea $X\in\mathcal P(A)$. Entonces $X\subseteq A$. Como $A\subseteq B$, por transitividad $X\subseteq B$, así $X\in\mathcal P(B)$.

## C. Existencia y unicidad


### 15

Elige $x=-a$. Entonces $x+a=-a+a=0$. El testigo pertenece a $\mathbb R$.


### 16

Si $x+a=0$ y $y+a=0$, restamos $a$ en ambas igualdades: $x=-a$ y $y=-a$, luego $x=y$.


### 17

Existencia: $x=1/a$. Unicidad: si $ax=1$ y $ay=1$, entonces $ax=ay$; como $a\ne0$, dividir por $a$ da $x=y$.


### 18

Sobreyectividad da al menos una preimagen. Si $f(a_1)=b=f(a_2)$, inyectividad da $a_1=a_2$.


### 19

En $\mathbb R$, la ecuación $x^2=1$ tiene soluciones $x=1$ y $x=-1$. Hay existencia pero no unicidad.


### 20

Las dos condiciones las satisface cualquier $X\subseteq A$, por lo que la afirmación de unicidad es falsa salvo casos especiales. Por ejemplo, si $A=\{1\}$, funcionan $X=\varnothing$ y $X=A$. El ejercicio revela que antes de demostrar conviene verificar si el enunciado es cierto.

## D. Bicondicionales


### 21

Si $n=2k$, entonces $n+2=2(k+1)$, par. Recíprocamente, si $n+2=2m$, entonces $n=2(m-1)$, par.


### 22

Si $A\subseteq B$, todo elemento de $A$ pertenece a ambos, así $A\subseteq A\cap B$; la inclusión contraria siempre vale. Recíprocamente, si $A\cap B=A$ y $x\in A$, entonces $x\in A\cap B$, luego $x\in B$.


### 23

Si $A\subseteq B$, todo elemento de $A\cup B$ está en $B$, y $B\subseteq A\cup B$, luego igualdad. Recíprocamente, si $A\cup B=B$ y $x\in A$, entonces $x\in A\cup B=B$.


### 24

Si es sobreyectiva, todo $b\in B$ es $f(a)$ para algún $a$, luego $B\subseteq\operatorname{Im}(f)$; la otra inclusión siempre vale. Si la imagen es $B$, cada $b$ está en la imagen, que es justamente sobreyectividad.


### 25

Si $x=0$, entonces $x^2=0$. Si $x^2=0$ y $x\ne0$, dividir por $x$ daría $x=0$, contradicción. Equivalentemente, en $\mathbb R$ un producto es cero sólo si algún factor es cero.


### 26

(i)$\Rightarrow$(ii) es inmediato. (ii)$\Rightarrow$(iii): no puede existir elemento exclusivo de uno de los conjuntos. (iii)$\Rightarrow$(i): si la diferencia simétrica es vacía, ningún elemento pertenece a uno sin pertenecer al otro, luego las pertenencias coinciden y $A=B$.

## E. Contraposición


### 27

La contrapositiva es: si $n$ es impar, entonces $n^2$ es impar. Si $n=2k+1$, entonces $n^2=2(2k^2+2k)+1$, impar. Por equivalencia lógica, el enunciado original es verdadero.


### 28

La contrapositiva de «$ab$ impar $\Rightarrow$ ambos impares» es «si al menos uno es par, entonces $ab$ es par». Si $a=2k$, entonces $ab=2(kb)$; análogamente si $b$ es par.


### 29

La contrapositiva dice: si $x$ e $y$ son racionales, entonces $x+y$ es racional. Escribe $x=a/b$, $y=c/d$ con enteros y denominadores no nulos; entonces $x+y=(ad+bc)/(bd)$ es racional.


### 30

Esto es exactamente la negación de $A\subseteq B$, pues $A\subseteq B$ significa $\forall x(x\in A\Rightarrow x\in B)$. Negarla produce $\exists x(x\in A\land x\notin B)$.


### 31

El método pedido es contraposición. La contrapositiva dice: si para todo $S\subseteq A$ se cumple $f^{-1}(f(S))=S$, entonces $f$ es inyectiva.

Supongamos esa igualdad universal y sean $a,b\in A$ con $f(a)=f(b)$. Para $S=\{a\}$ tenemos $b\in f^{-1}(f(S))=S$, así que $b=a$. Esto prueba inyectividad y, por contraposición, el enunciado original.

También puede construirse directamente el subconjunto que lo verifica cuando $f$ no es inyectiva: si $a\ne b$ y $f(a)=f(b)$, toma $S=\{a\}$. Entonces $b\notin S$ pero $b\in f^{-1}(f(S))$, por lo que los conjuntos difieren. Esta última ruta prueba el mismo enunciado, pero no sustituye la prueba por el método solicitado.


### 32

La prueba directa requiere extraer paridad de $n$ a partir de la de $n^2$, lo que suele necesitar un resultado adicional. La contrapositiva convierte la hipótesis en la representación explícita $n=2k+1$, desde la que el cuadrado se calcula inmediatamente. Por eso es estratégicamente más natural.

## F. Contradicción


### 33

Supón que existe tal $x$. Entonces $0<x$ y $x<0$. Por transitividad del orden, $0<0$, imposible. Por tanto no existe.


### 34

Supón que es inyectiva. Toma $a_1\ne a_2$ en $A$. Como es constante, $f(a_1)=f(a_2)$; inyectividad implicaría $a_1=a_2$, contradicción.


### 35

Supón que existe $A$ con $A\in\varnothing$. Pero por definición el conjunto vacío no tiene elementos. Contradicción.


### 36

Si también $B\subseteq A$, las dos inclusiones darían $A=B$ por extensionalidad/doble inclusión, contradiciendo que $A$ es subconjunto propio de $B$.


### 37

Supón que $g$ y $h$ son inversas de $f$ y $g\ne h$. Pero algebraicamente $g=g\circ\operatorname{id}_B=g\circ(f\circ h)=(g\circ f)\circ h=\operatorname{id}_A\circ h=h$, contradicción.


### 38

La negación de una implicación es $P\land\neg Q$. Para demostrar que la implicación es verdadera por contradicción, se supone precisamente su falsedad y se deriva una imposibilidad.

## G. Casos


### 39

Si $x\ge0$, $|x|=x\ge0$. Si $x<0$, $|x|=-x>0$. Los casos son exhaustivos.


### 40

Todo entero es par o impar. Si $n$ es par, el producto tiene factor par. Si $n$ es impar, $n+1$ es par, así el producto vuelve a tener factor par.


### 41

Si $x\ge0$, $|x|=x$ y la igualdad es inmediata. Si $x<0$, $|x|=-x$ y $|x|^2=(-x)^2=x^2$.


### 42

Es la definición de unión. Caso 1: $x\in A$; caso 2: $x\in B$. Toda conclusión que pueda derivarse en ambos casos queda establecida para un $x\in A\cup B$.


### 43

Si $x\ge y$, entonces $\max\{x,y\}=x$ y $x-(x+y)/2=(x-y)/2\ge0$. Si $y\ge x$, análogamente $y-(x+y)/2=(y-x)/2\ge0$.


### 44

Los casos no son exhaustivos: falta $x=0$. La reparación es usar $x\ge0$ / $x<0$, o separar tres casos $x>0$, $x=0$, $x<0$.

## H. Pruebas de conjuntos


### 45

Sea $x$ en el lado izquierdo. Entonces $x\in A$ y $x\in B$ o $x\in C$. Si $x\in B$, $x\in A\cap B$; si $x\in C$, $x\in A\cap C$. Luego pertenece al lado derecho.


### 46

Sea $x\in(A\cap B)\cup(A\cap C)$. Entonces está en $A\cap B$ o en $A\cap C$. En ambos casos $x\in A$ y además $x\in B\cup C$. Por tanto $x\in A\cap(B\cup C)$.


### 47

Para $x$: $x\in A\setminus(B\cup C)$ iff $x\in A$ y $x\notin B\cup C$ iff $x\in A$, $x\notin B$ y $x\notin C$ iff $x\in(A\setminus B)\cap(A\setminus C)$.


### 48

$X$ está en el lado izquierdo iff $X\subseteq A$ y $X\subseteq B$ iff todo elemento de $X$ está en $A\cap B$ iff $X\subseteq A\cap B$ iff $X\in\mathcal P(A\cap B)$.


### 49

Toma $A=\{1\}$, $B=\{1\}$, $C=\varnothing$. Entonces $B\cap C=\varnothing$, así el lado izquierdo es $\{1\}$. El derecho es $(\varnothing)\cap\{1\}=\varnothing$.


### 50

Si $A=B$, no hay elementos exclusivos y la diferencia simétrica es vacía. Si $A\triangle B=\varnothing$ y $x\in A$, no puede ocurrir $x\notin B$, pues estaría en $A\setminus B$; así $A\subseteq B$. Simétricamente $B\subseteq A$.

## I. Pruebas con funciones


### 51

Supón $3x_1-1=3x_2-1$. Entonces $3x_1=3x_2$ y $x_1=x_2$.


### 52

Sea $y\in\mathbb R$ arbitrario. Toma $x=(y+1)/3$. Entonces $f(x)=3(y+1)/3-1=y$.


### 53

Si $f(x_1)=f(x_2)$, al aplicar $g$ se obtiene $(g\circ f)(x_1)=(g\circ f)(x_2)$. La inyectividad de la composición fuerza $x_1=x_2$.


### 54

Sea $c$ arbitrario en el codominio de $g$. Existe $a$ con $g(f(a))=c$. Tomando $b=f(a)$, se tiene $g(b)=c$.


### 55

Si $g\circ f=\operatorname{id}$ y $f(x_1)=f(x_2)$, aplicar $g$ da $x_1=(g\circ f)(x_1)=(g\circ f)(x_2)=x_2$.


### 56

Si $f\circ h=\operatorname{id}_B$, para cualquier $b\in B$, toma $a=h(b)$. Entonces $f(a)=f(h(b))=b$.

## J. Contraejemplos y refutación


### 57

$a=b=1$ es contraejemplo: $a+b=2$ es par, pero ninguno de los dos es par.


### 58

Toma $A=\{1\}$ y $B=\{2\}$. La intersección es vacía y ambos conjuntos son no vacíos.


### 59

Toma $f:\{1,2\}\to\{a\}$ con $f(1)=f(2)=a$. Es sobreyectiva hacia $\{a\}$ pero no inyectiva.


### 60

Toma $A=\{1\}$, $B=\{a,b\}$, $C=\{x\}$, $f(1)=a$ y $g(a)=g(b)=x$. La composición desde un singleton es inyectiva, pero $g$ no.


### 61

Para refutar $P\Rightarrow Q$ se necesita $P$ verdadera y $Q$ falsa. Si $P$ ya es falsa, la implicación no falla en ese caso.


### 62

Toma $C=\{1,2\}$, $A=\{1\}$, $B=\{2\}$. Entonces ambas uniones son $C$, pero $A\ne B$.

## K. Diagnóstico y reparación


### 63

La prueba asume exactamente lo que debe demostrar: que $n$ es par. Es circular. Puede repararse usando contraposición: si $n$ es impar, entonces $n^2$ es impar.


### 64

Se eligió un ejemplo particular en lugar de un real arbitrario. Hay que tomar $x\in\mathbb R$ arbitrario y usar una propiedad válida para todo real, por ejemplo que el producto de dos números del mismo signo es no negativo.


### 65

Se cambió ilegítimamente $\forall x\,\exists y$ por $\exists y\,\forall x$. El testigo $y$ puede depender de $x$. La prueba debe conservar esa dependencia.


### 66

Falta la dirección $Q\Rightarrow P$. La prueba sólo establece que $P$ es suficiente para $Q$, no que sea necesaria.

## L. Síntesis


### 67

Prueba directa por elemento arbitrario. Sea $x\in A\cap C$. Entonces $x\in A$ y $x\in C$. Como $A\subseteq B$, $x\in B$, luego $x\in B\cap C$.


### 68

Directa: $n=2k+1$. Entonces $n^2+2n=(2k+1)^2+2(2k+1)=4k^2+8k+3=2(2k^2+4k+1)+1$, impar.


### 69

Puede hacerse por contraposición/casos. Si $x\le-1$ o $x\ge1$, entonces $|x|\ge1$ y por tanto $x^2\ge1$. La contraposición da el resultado.


### 70

Para inyectividad, usa igualdad de valores y aplica sucesivamente inyectividad de $g$ y $f$. Para sobreyectividad, dado $c\in C$, elige $b$ con $g(b)=c$ y luego $a$ con $f(a)=b$. Entonces $g(f(a))=c$.


### 71

Si $A\subseteq B$, no existe elemento de $A$ fuera de $B$, así la diferencia es vacía. Si $A\setminus B=\varnothing$ y $x\in A$, no puede ser $x\notin B$, pues estaría en la diferencia. Luego $x\in B$.


### 72

Verdadero. Elige $c\in C$. Si $a\in A$, entonces $(a,c)\in A\times C=B\times C$, de modo que $a\in B$. Así $A\subseteq B$. Simétricamente $B\subseteq A$.

## M. Problemas avanzados tipo prueba


### 73

**Contraposición.** La contrapositiva es: si $n$ es impar, $n^2$ es impar. Escribe $n=2k+1$. Entonces
$$
n^2=4k^2+4k+1=2(2k^2+2k)+1,
$$
impar. Por equivalencia lógica, el teorema queda demostrado.

**Contradicción.** Supón $n^2$ par y, buscando contradicción, supón además que $n$ es impar. El mismo cálculo muestra que $n^2$ sería impar, contradiciendo la hipótesis de que es par.

Las dos usan el mismo núcleo algebraico. La contraposición muestra con mayor claridad que se está probando una implicación equivalente; la contradicción añade una hipótesis incompatible y cierra por imposibilidad.


### 74

(i)$\Rightarrow$(ii): siempre $S\subseteq f^{-1}(f(S))$. Si $x$ está en el lado derecho, existe $s\in S$ con $f(x)=f(s)$; inyectividad da $x=s\in S$.

(ii)$\Rightarrow$(i): si $f(a)=f(b)$, entonces $b\in f^{-1}(f(\{a\}))=\{a\}$, luego $a=b$.

(i)$\Rightarrow$(iii): la inclusión de izquierda a derecha siempre vale. Si $y\in f(S)\cap f(T)$, existen $s\in S,t\in T$ con $f(s)=f(t)=y$; inyectividad da $s=t\in S\cap T$.

Para (iii)$\Rightarrow$(i) por contraposición, supón que $f$ no es inyectiva. Existen $a\ne b$ con $f(a)=f(b)$. Toma $S=\{a\}$ y $T=\{b\}$. Entonces $S\cap T=\varnothing$, así $f(S\cap T)=\varnothing$, pero $f(a)\in f(S)\cap f(T)$. Por tanto (iii) falla.


### 75

Sea $x$ en el lado izquierdo. Entonces $x\in A$ y $x\notin B\triangle C$. No estar en la diferencia simétrica significa que $x$ pertenece a ambos $B,C$ o a ninguno. En el primer caso $x\in A\cap B\cap C$; en el segundo $x\in A\setminus(B\cup C)$. Así obtenemos la primera inclusión.

Recíprocamente, si $x$ está en el lado derecho, entonces $x\in A$ y o bien pertenece simultáneamente a $B,C$, o bien no pertenece a ninguno. En cualquiera de los dos casos $x\notin B\triangle C$, así $x\in A\setminus(B\triangle C)$.

La identidad expresa «dentro de $A$, $B$ y $C$ tienen el mismo valor de pertenencia».


### 76

(a) Si $f(x_1)=f(x_2)$, entonces $(g\circ f)(x_1)=(g\circ f)(x_2)$ y la inyectividad de la composición da $x_1=x_2$. Para $g$, dado $c\in C$, la sobreyectividad de la composición da $a\in A$ con $g(f(a))=c$, así $c$ tiene preimagen bajo $g$.

(b) Supón $g(b_1)=g(b_2)$. Como $f$ es sobreyectiva, existen $a_1,a_2$ con $f(a_i)=b_i$. Entonces
$$
(g\circ f)(a_1)=g(b_1)=g(b_2)=(g\circ f)(a_2).
$$
La composición es inyectiva, así $a_1=a_2$, y por tanto $b_1=b_2$.

(c) Ya sabíamos que $f$ era inyectiva y ahora suponemos sobreyectividad; por tanto $f$ es biyectiva. $g$ era sobreyectiva y (b) da inyectividad; luego $g$ es biyectiva.


### 77

(a) Toma $C=\{1,2\}$, $A=\{1\}$, $B=\{2\}$. Son no vacíos y distintos, pero $A\cup C=C=B\cup C$.

(b) Una hipótesis suficiente es también exigir
$$
A\cap C=B\cap C.
$$

(c) Sea $x\in A$. Si $x\in C$, entonces $x\in A\cap C=B\cap C$, así $x\in B$. Si $x\notin C$, como $x\in A\cup C=B\cup C$ y no pertenece a $C$, debe pertenecer a $B$. Así $A\subseteq B$. Intercambiando $A,B$ obtenemos $B\subseteq A$, luego $A=B$.

La prueba usa casos según pertenencia a $C$.


### 78

**Lema.** Si $f:A\to B$ es inyectiva, entonces la función recodificada
$$
\tilde f:A\to f(A),\qquad \tilde f(a)=f(a)
$$
es biyectiva.

Prueba: es inyectiva porque $f$ lo es; es sobreyectiva por definición de $f(A)$.

Ahora, como $g\circ f$ es sobreyectiva, $g|_{f(A)}$ es sobreyectiva: dado $c\in C$, existe $a$ con $g(f(a))=c$, y $f(a)\in f(A)$.

Queda comparar inyectividad. Tenemos
$$
g\circ f=(g|_{f(A)})\circ\tilde f.
$$
Como $\tilde f$ es biyectiva, en particular sobreyectiva e inyectiva.

Si $g|_{f(A)}$ es inyectiva, la composición con $\tilde f$ es inyectiva, así $g\circ f$ lo es.

Recíprocamente, supón $g\circ f$ inyectiva y sean $b_1,b_2\in f(A)$ con $g(b_1)=g(b_2)$. Por sobreyectividad de $\tilde f$, existen $a_i$ con $\tilde f(a_i)=b_i$. Entonces $(g\circ f)(a_1)=(g\circ f)(a_2)$, así $a_1=a_2$ y $b_1=b_2$. La restricción es inyectiva.

Como ya era sobreyectiva, es biyectiva exactamente cuando la composición es inyectiva.


### 79

(a) Sobreyectividad garantiza **existencia** de al menos una preimagen para cada elemento de $B$, no **unicidad**. La frase “esa preimagen debe ser $x_1=x_2$” introduce ilegítimamente la propiedad que define inyectividad.

(b) Sea $f:\{1,2\}\to\{a\}$ con $f(1)=f(2)=a$. Es sobreyectiva y no inyectiva. El dominio necesita al menos dos elementos distintos para que falle inyectividad; con dos basta este ejemplo. El codominio no puede ser vacío para una función con ese dominio, y un solo elemento basta. Por tanto las cardinalidades dos y uno son mínimas.

(c) Una afirmación verdadera cercana es: «si $f$ es biyectiva, entonces cada $b\in B$ tiene una única preimagen». Sobreyectividad da existencia. Si $f(x_1)=b=f(x_2)$, inyectividad da $x_1=x_2$.


### 80

Sea $x\in A$ arbitrario. Debemos mostrar $x\in B$.

Dividimos según la pertenencia a $C$.

**Caso 1: $x\in C$.** Como $x\in A$ y $x\in C$, tenemos $x\in A\cap C$. Por hipótesis, $x\in B\cap C$, luego $x\in B$.

**Caso 2: $x\notin C$.** Entonces $x\in A\setminus C$. Por hipótesis, $x\in B\setminus C$, luego $x\in B$.

Los casos $x\in C$ y $x\notin C$ son exhaustivos. Por arbitrariedad, $A\subseteq B$.

La prueba por casos es natural porque las dos hipótesis están diseñadas precisamente para las dos regiones determinadas por $C$. Una contradicción obligaría a suponer $x\notin B$ y luego volver a separar esos mismos casos, añadiendo una capa lógica innecesaria.

## N. Construir pruebas con ayuda decreciente


### 81

Supongamos $A\cap B=\varnothing$ y fijemos $x\in A$. Si $x\in B$, entonces $x\in A\cap B$, imposible. Por tanto $x\notin B$ y $x\in A\setminus B$. Como $x$ era arbitrario, $A\subseteq A\setminus B$.

Recíprocamente, supongamos esa inclusión. Si existiera $x\in A\cap B$, la pertenencia a $A$ y la inclusión darían $x\in A\setminus B$, es decir, $x\notin B$, contradiciendo $x\in B$. No existe tal elemento y la intersección es vacía. Si $A=\varnothing$, ambas condiciones son verdaderas; no se eligió un elemento cuya existencia hubiera que garantizar.


### 82

Las obligaciones son deducir ambos ceros de la suma nula y comprobar la suma cuando ambos números son cero. Si $x+y=0$ y $x>0$, de $y\geq0$ resulta $x+y\geq x>0$, contradicción. Así $x\leq0$; junto con $x\geq0$ da $x=0$. Sustituyendo en la suma, $y=0$. La vuelta es $0+0=0$.

La condición $y\geq0$ se usó para comparar la suma con $x$ y $x\geq0$ para convertir $x\leq0$ en igualdad. Sin ambas condiciones, $1+(-1)=0$ no permite concluir que los sumandos sean cero.


### 83

Si $A\subseteq B$ y $(a,c)\in A\times C$, entonces $a\in B$ y $c\in C$, de modo que $(a,c)\in B\times C$. Esto prueba la inclusión de productos sin necesitar $C\neq\varnothing$.

Para la vuelta, fijamos $c_0\in C$, que existe por la hipótesis. Dado $a\in A$ arbitrario, $(a,c_0)\in A\times C\subseteq B\times C$, luego $a\in B$. Así $A\subseteq B$. Si $A$ es vacío, el argumento universal sigue siendo válido. Sin no vacuidad, toma $A=\{0\}$ y $B=C=\varnothing$: ambos productos son vacíos, pero $A\nsubseteq B$.


### 84

Para cada $a\in A$ hay un único $f(a)\in B$, por lo que el par pertenece al codominio y está determinado de manera única. Si $F(a_1)=F(a_2)$, la igualdad de las primeras coordenadas da $a_1=a_2$; así $F$ es inyectiva.

Si $A=\varnothing$, también $A\times B=\varnothing$ y $F$ es sobreyectiva. Si $A\neq\varnothing$, fijemos $a_0\in A$; la existencia de $f$ garantiza $f(a_0)\in B$. Si $F$ es sobreyectiva, para cada $b\in B$ el par $(a_0,b)$ es $F(a)$ para algún $a$. Las coordenadas obligan a $a=a_0$ y $b=f(a_0)$; por tanto $B=\{f(a_0)\}$. Recíprocamente, si $B$ tiene un solo elemento, todo $(a,b)\in A\times B$ satisface $b=f(a)$, y es $F(a)$. La condición exacta es $A=\varnothing$ o $B$ unitario.


### 85

La hipótesis no basta: $a=1,b=1$ da $x+1=x$, imposible. Reorganizar la igualdad equivale a $(a-1)x=-b$.

Si $a\neq1$, existe $x=-b/(a-1)$ y la sustitución verifica la ecuación. Si $u,v$ son soluciones, $(a-1)u=(a-1)v$ y la no nulidad de $a-1$ permite cancelar para obtener $u=v$. Si $a=1,b=0$, todo real es solución; como $0$ y $1$ son distintos, no hay unicidad. Si $a=1,b\neq0$, la ecuación exigiría $b=0$ y no hay soluciones. Estos casos son exhaustivos y no requieren $a\neq0$: también $a=0$ pertenece al primer caso y da la única solución $x=b$.


### 86

Definimos $U=X\cap A$ y $V=X\cap B$. Tienen las inclusiones exigidas. Si $x\in X$, la inclusión $X\subseteq A\cup B$ lo sitúa en al menos una de las partes y por tanto en $U\cup V$; si $x\in U\cup V$, está en $X$. Así $X=U\cup V$.

Para unicidad, sea otra representación $X=U'\cup V'$ con las mismas inclusiones. Si $x\in U'$, entonces $x\in X\cap A$. Si $x\in X\cap A$, pertenece a $U'$ o a $V'$; la segunda posibilidad lo situaría en $A\cap B$, imposible. Luego $U'=X\cap A$. Por el mismo argumento explicitado con las partes intercambiadas, si $x\in V'$ está en $X\cap B$, y si $x\in X\cap B$ no puede estar en $U'\subseteq A$, de modo que $V'=X\cap B$. Ambas partes están determinadas.

Si alguna parte es vacía, su subconjunto correspondiente también lo es; si $X$ es vacío, ambos son vacíos. Si $A=B=X=\{0\}$, las representaciones $(U,V)=(\{0\},\varnothing)$ y $(\varnothing,\{0\})$ son distintas. Falla la exclusión de la segunda posibilidad, que usaba disjunción.

## O. Hipótesis tácitas y reparación de enunciados


### 87

Con $x=-2,y=1$ tenemos $x^2>y^2$ y $x<y$. Cancelar un factor de signo desconocido en una desigualdad puede invertir su sentido. Una reparación es añadir $x+y>0$. Entonces dividir $(x-y)(x+y)>0$ por ese número positivo da $x-y>0$ y $x>y$. La factorización no necesitaba la hipótesis; la división con preservación del orden sí. No se afirma que sea la única reparación posible.


### 88

La elección requiere que $h$ sea sobreyectiva. Sin ello, toma $A=\{0\}$, $B=C=\{0,1\}$, $h(0)=0$, $f(0)=f(1)=0$, $g(0)=0,g(1)=1$. Las composiciones coinciden en $A$, pero $f(1)\neq g(1)$.

Si $h$ es sobreyectiva, para $b\in B$ arbitrario existe $a\in A$ con $h(a)=b$. Por igualdad de las composiciones, $f(b)=f(h(a))=g(h(a))=g(b)$. Las funciones tienen el mismo dominio y codominio y coinciden en cada entrada, luego son iguales. La reparación justifica cada elección; no presupone una función que seleccione simultáneamente todas las preimágenes.


### 89

Se usó $aRb$ sin garantizar que para ese $a$ exista algún $b$. En $A=\{0\}$, la relación vacía es simétrica y transitiva, pues sus implicaciones no tienen antecedentes verdaderos, pero no es reflexiva.

Con la condición adicional, fija $a\in A$ arbitrario y escoge el $b$ que ella garantiza. De $aRb$, simetría da $bRa$ y transitividad da $aRa$. Así $R$ es reflexiva. Recíprocamente, si es reflexiva, para cada $a$ se puede tomar $b=a$. Si $A$ es vacío, todas estas condiciones son universales vacías y la equivalencia también vale.


### 90

Si $A=\varnothing$, $B=\varnothing$ y $C=\{0\}$, los productos son vacíos pero $B\neq C$. Se repara con $A\neq\varnothing$. Fija $a_0\in A$. Para $b\in B$, el par $(a_0,b)$ está en $A\times C$, por lo que $b\in C$ y $B\subseteq C$. Para $c\in C$, la igualdad inversa de productos da $(a_0,c)\in A\times B$, luego $c\in B$ y $C\subseteq B$. Así $B=C$.

La propiedad universal caracteriza no vacuidad: acabamos de probar su suficiencia y, si $A$ es vacío, los $B,C$ del contraejemplo refutan la propiedad. Una igualdad particular con $B=C$ no permitiría concluir no vacuidad de $A$; la cuantificación sobre todos $B,C$ es esencial.


### 91

Con $S=\{-1\}$ y $t=1$, $t\notin S$ pero $t=(-1)^2$ está en la imagen. Entrada y salida son papeles distintos. La condición exacta es
$$
t\in\{s^2:s\in S\}\quad\Longleftrightarrow\quad\exists s\in S\;(s^2=t).
$$
Si hay tal $s$, su cuadrado coloca $t$ en la imagen; si $t$ está en la imagen, su definición proporciona ese $s$. Para $S=\{-2,0\}$ los únicos cuadrados posibles son $4$ y $0$, de modo que $4$ sí pertenece (testigo $-2$) y $1$ no pertenece (ninguna de las dos entradas produce $1$). La reparación cambia la conclusión a la negación de la existencia de una preimagen, no a la ausencia de la salida en el dominio.


### 92

Para $A=B=\{0\}$, tanto $X=\varnothing$ como $X=A$ cumplen la igualdad. Los conjuntos buscados son exactamente
$$
A\setminus B\subseteq X\subseteq A.
$$
Si se cumple la igualdad y $a\in A\setminus B$, entonces $a\in X\cup B$ pero $a\notin B$, luego $a\in X$. Recíprocamente, si esas inclusiones valen, $X\cup B\subseteq A\cup B$. Para la inclusión inversa, un elemento de $B$ ya está en $X\cup B$ y un elemento de $A$ que no está en $B$ pertenece a $A\setminus B\subseteq X$. Así las uniones son iguales.

Si $A\cap B=\varnothing$, entonces $A\setminus B=A$ y las inclusiones obligan a $X=A$. Si la intersección no es vacía, $A\setminus B$ y $A$ son dos soluciones distintas. La operación «quitar $B$» sólo determina la parte fuera de $B$, que es el dato que el borrador confundía con el conjunto entero.

## P. Diseñar lemas útiles


### 93

Un lema útil es: si $U=U_1\cup U_2=V_1\cup V_2$, con $U_1\cap U_2=V_1\cap V_2=\varnothing$, las piezas $U_i\cap V_j$ para $i,j\in\{1,2\}$ cubren $U$ y son disjuntas dos a dos.

Prueba: dado $x\in U$, pertenece a algún $U_i$ y a algún $V_j$, de modo que está en una de las piezas. Recíprocamente, todas están contenidas en $U$. Si dos piezas tienen índices distintos, difieren en el índice $i$ o en el $j$. Un elemento común estaría respectivamente en $U_1\cap U_2$ o en $V_1\cap V_2$, ambas vacías. Esto prueba cada posible intersección entre piezas diferentes.

Aplicamos con $U=A\cup B$, $(U_1,U_2)=(A,B)$ y $(V_1,V_2)=(C,D)$. El lema produce las dos conclusiones pedidas. No afirma que estas piezas sean una partición con bloques no vacíos: por ejemplo, si $A=C$ y $B=D$ son disjuntos, las piezas $A\cap D$ y $B\cap C$ son vacías. Exigirlas no vacías excluiría ejemplos válidos.


### 94

Lema: para $T\subseteq A$, $b\in f(T)$ si y sólo si existe $t\in T$ con $f(t)=b$. Es la definición de imagen: la ida extrae un testigo y la vuelta lo verifica.

Si $b\in f(X\cup Y)$, el lema da $t\in X\cup Y$ con $f(t)=b$. Según pertenezca a $X$ o a $Y$, el mismo lema da $b\in f(X)$ o $b\in f(Y)$. Para la vuelta, si $b\in f(X)\cup f(Y)$, procede de alguna entrada de $X$ o de $Y$; esa entrada está en $X\cup Y$ y coloca $b$ en su imagen.

Para la intersección, una entrada de $X\cap Y$ sí demuestra $f(X\cap Y)\subseteq f(X)\cap f(Y)$. Pero en la vuelta se obtienen $x\in X$ y $y\in Y$ con $f(x)=b=f(y)$; pueden ser entradas diferentes, y ninguna pertenecer a $X\cap Y$. Ejemplo: $A=\{0,1\}$, $B=\{0\}$, función constante, $X=\{0\},Y=\{1\}$. La imagen de la intersección es vacía y la intersección de imágenes es $\{0\}$. Si se añade inyectividad, $x=y$ elimina exactamente ese obstáculo.


### 95

Lema: si $a<b$, los números $u=(2a+b)/3$ y $v=(a+2b)/3$ satisfacen $a<u<v<b$. En efecto,
$$
u-a=v-u=b-v=(b-a)/3>0.
$$
Cada diferencia positiva justifica una de las desigualdades, y en particular $u\neq v$.

Si $u\neq c$, elige $t=u$. Si $u=c$, elige $t=v$, que es distinto de $u$ y por tanto de $c$. En ambos casos $a<t<b$. Los casos son exhaustivos. El lema aporta dos candidatos admisibles; no presupone que uno de ellos sea el número prohibido ni que ambos lo eviten. La construcción prueba la existencia usando sólo operaciones reales y orden.


### 96

Lema: si $C\neq\varnothing$ y $H$ es inyectiva, entonces $f$ es inyectiva. Fija $c_0\in C$. Si $f(a_1)=f(a_2)$, entonces $H(a_1,c_0)=H(a_2,c_0)$; inyectividad de $H$ da $(a_1,c_0)=(a_2,c_0)$, luego $a_1=a_2$.

Con $A\neq\varnothing$, se recupera también $g$: fija $a_0\in A$; si $g(c_1)=g(c_2)$, los valores $H(a_0,c_1)$ y $H(a_0,c_2)$ coinciden, por lo que $c_1=c_2$. Así la inyectividad de $H$ implica la de ambas funciones. Para la vuelta, de $H(a_1,c_1)=H(a_2,c_2)$ se deducen $f(a_1)=f(a_2)$ y $g(c_1)=g(c_2)$; sus inyectividades dan ambas igualdades de coordenadas.

Si $C=\varnothing$, no hay $c_0$ y $A\times C$ es vacío, por lo que $H$ es inyectiva aunque $f$ no lo sea. Por ejemplo, $A=\{0,1\}$, $B=\{0\}$, $f$ constante, $C=\varnothing$, $D=\{0\}$ y $g$ vacía. Intercambiar los factores muestra el otro posible fallo.


### 97

Lema: si $r\geq s$, el máximo es $r$, el mínimo es $s$ y $|r-s|=r-s$; si $r<s$, el máximo es $s$, el mínimo es $r$ y $|r-s|=s-r$. Las primeras afirmaciones se siguen de la comparación y las últimas de la definición de valor absoluto. Los casos son exhaustivos y el primero incluye $r=s$.

En el primer caso, máximo más mínimo es $r+s$, y $(r+s+|r-s|)/2=(r+s+r-s)/2=r$, el máximo. En el segundo, la suma es $s+r=r+s$, y la fórmula da $(r+s+s-r)/2=s$, también el máximo. Se probaron los dos objetivos en cada caso. Si $r=s$, el valor absoluto es cero y la fórmula devuelve $r$; no se divide por $r-s$.


### 98

Lema: para un par $(x,y)$, pertenecer a $E\times F$ equivale a $x\in E$ e $y\in F$. La ida y la vuelta son las dos partes de la definición del producto cartesiano.

Si $z$ pertenece a la intersección de la izquierda, al pertenecer a $A\times C$ es un par $(x,y)$. El lema para ambos productos da $x\in A$, $y\in C$, $x\in B$, $y\in D$. Así $x\in A\cap B$ y $y\in C\cap D$, y otra aplicación da pertenencia a la derecha. Recíprocamente, un elemento de la derecha es un par $(x,y)$ con ambas condiciones de intersección, que implican pertenencia a los dos productos y luego a su intersección.

Si $A$ o $B$ es vacío, el producto correspondiente de la izquierda y $A\cap B$ de la derecha son vacíos. Si $C$ o $D$ es vacío, sucede lo mismo con el producto correspondiente y $C\cap D$. En todos esos casos ambos miembros son vacíos; la prueba general no necesitó elegir pares existentes.

## Q. Síntesis y elección autónoma del método


### 99

El único candidato es $X=U\setminus A$. Tiene unión $U$ con $A$: cada elemento de $U$ está en $A$ o fuera de $A$. Su intersección con $A$ es vacía por definición, y es subconjunto de $U$, así que existe.

Sea ahora $X\subseteq U$ que cumple ambas condiciones. Si $x\in X$, no puede estar en $A$ por disjunción, luego $x\in U\setminus A$. Si $x\in U\setminus A$, la unión $U=A\cup X$ obliga a $x\in X$. Las dos inclusiones dan $X=U\setminus A$ y unicidad.

Por separado, la unión sólo obliga a $U\setminus A\subseteq X\subseteq U$; la disjunción sólo obliga a $X\subseteq U\setminus A$. Ambas juntas fijan los dos extremos iguales. Se eligió doble inclusión para identificar el objeto, y las mismas inclusiones cierran la unicidad. Si $A=\varnothing$, el candidato es $U$; si $A=U$, es vacío.


### 100

Si $b<0$, no hay soluciones porque un valor absoluto es no negativo. Si $b=0$, la igualdad equivale a $x-a=0$, así que existe la única solución $x=a$.

Si $b>0$, cualquier solución cumple $x-a\geq0$ o $x-a<0$. En el primer caso, la definición da $x-a=b$ y $x=a+b$. En el segundo, $-(x-a)=b$ y $x=a-b$. Ambos candidatos satisfacen la ecuación: sus diferencias con $a$ son $b$ y $-b$, cuyos valores absolutos son $b$. Además, son distintos porque su diferencia es $2b>0$. No hay otros candidatos por exhaustividad de los casos.

La clasificación tiene cero, una y dos soluciones según el signo de $b$. Se escogieron casos para usar la definición del valor absoluto y después separar existencia de exhaustividad. Omitir $b=0$ contaría dos veces el mismo candidato; omitir $b<0$ produciría falsos testigos.


### 101

Para $b\in B$ arbitrario, aplicamos la identidad dada a $g(b)\in A$:
$$
g(f(g(b)))=g(b).
$$
Ambas entradas de $g$ son elementos de $B$. Como $g$ es inyectiva, se deduce $f(g(b))=b$. Por arbitrariedad y por los dominios declarados, $f\circ g=\operatorname{id}_B$.

Sin inyectividad, toma $A=\{0\}$, $B=\{0,1\}$, $f(0)=0$ y $g(0)=g(1)=0$. La composición $g\circ f$ es la identidad de $A$, pero $f(g(1))=0\neq1$. Aplicar $g$ convirtió la igualdad deseada en una igualdad conocida; su inyectividad permitió regresar. Ese regreso necesita una propiedad demostrada o dada, no la igualdad que se quiere probar. Si $B$ es vacío, la conclusión es universal vacía y sigue siendo válida.


### 102

Si $aRb$ y $x\in R(b)$, entonces $bRx$; por transitividad, $aRx$ y $x\in R(a)$. Así $R(b)\subseteq R(a)$. Para la vuelta, reflexividad da $bRb$, es decir, $b\in R(b)$. La inclusión lo coloca en $R(a)$ y por tanto $aRb$.

El valor $R(a)$ es un subconjunto de $A$, así que la función indicada está bien definida. Si $R(a)=R(b)$, las dos inclusiones y la equivalencia probada dan $aRb$ y $bRa$. Antisimetría implica $a=b$ y por ello la función es inyectiva. En $A=\varnothing$ esta prueba de inyectividad no requiere elegir elementos.

La ida usó transitividad; la vuelta usó reflexividad; el cierre de inyectividad usó antisimetría. Sin reflexividad, en $A=\{0\}$ con $R=\varnothing$, $R(0)\subseteq R(0)$ es verdadera pero $0R0$ es falsa. El método se eligió al traducir la pertenencia a $R(a)$ en una afirmación de la relación.


### 103

Primero $T$ tiene valores en $\mathcal P(U)$. Para $X\subseteq U$, todo $u\in U$ pertenece a $U\setminus(U\setminus X)$ exactamente cuando no está en $U\setminus X$, lo cual, dentro de $U$, equivale a $u\in X$. Así $T(T(X))=X$.

Si $T(X)=T(Y)$, aplicar $T$ y usar la identidad da $X=Y$, luego es inyectiva. Para $Y\subseteq U$ arbitrario, la entrada $X=T(Y)$ satisface $T(X)=Y$, luego es sobreyectiva. También demuestra que esa entrada es única por inyectividad.

Si $U=\varnothing$, su único subconjunto es vacío y es punto fijo. Si $U\neq\varnothing$, fija $u\in U$. La igualdad $X=U\setminus X$ exigiría $u\in X$ si y sólo si $u\notin X$. Si pertenece, la igualdad lo excluye; si no pertenece, lo incluye. Ambos casos contradicen la igualdad, así que no hay puntos fijos. La identidad doble organiza la biyectividad, pero no implica que cada subconjunto sea fijo: ser devuelto tras dos aplicaciones difiere de quedar igual tras una.


### 104

Si $A\neq\varnothing$, la primera hipótesis incluye $S=A$, cuya restricción es $f$, por lo que $f$ es inyectiva. Si $A=\varnothing$, lo es por la definición, pues no hay dos entradas que den una colisión.

La condición sobre pares de elementos también basta. Dados $a_1,a_2\in A$ con $f(a_1)=f(a_2)$, si ya son iguales no hay nada que probar. Si fueran distintos, $S=\{a_1,a_2\}$ tendría dos elementos y la inyectividad de $f|_S$ obligaría a $a_1=a_2$, contradicción. Luego toda igualdad de valores proviene de la misma entrada. Recíprocamente, si $f$ es inyectiva, cualquier restricción lo es: dos entradas en su dominio son entradas de $f$ y su igualdad de valores da igualdad de entradas. Esto incluye todas las restricciones a dos elementos.

Si $A$ es vacío o unitario, no hay subconjuntos de dos elementos, la condición es vacía y $f$ es inyectiva. En cambio, las restricciones unitarias siempre son inyectivas: en un dominio con una sola entrada, dos entradas cualesquiera ya coinciden. La función constante $f:\{0,1\}\to\{0\}$ las cumple y no es inyectiva. Una colisión necesita dos entradas distintas; ésa es la información mínima que prueba la condición sobre pares.

***

[← Capítulo 9](algebra-para-matematicos-capitulo-9-funciones-composicion-e-inversas.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 11 →](algebra-para-matematicos-capitulo-11-induccion-buen-orden-y-recursion.md)

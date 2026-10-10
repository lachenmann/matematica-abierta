---
{
  "title": "Funciones, composición e inversas",
  "description": "Capítulo 9 del Tomo I de Álgebra para matemáticos, con 104 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0184",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C09",
  "editorial-id": "MA-BCH-APM-01-009",
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
    "MA-BCH-0183"
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

En C8 estudiamos relaciones como subconjuntos de productos cartesianos. Una relación puede dejar entradas sin salida o relacionar una misma entrada con varias salidas. Una función aparece cuando esas dos libertades desaparecen.

> **Una función asigna a cada elemento de su dominio exactamente un elemento de su codominio.**

La palabra “exactamente” contiene dos exigencias distintas: debe existir una salida y esa salida debe ser única. Desde esa definición construiremos composición, inyectividad, sobreyectividad e inversas.

***
## 9.1. De una relación a una función {#apm-c09-s01}
***
Sean $A$ y $B$ conjuntos. Una relación $f\subseteq A\times B$ es una **función de $A$ en $B$** si

$$
\forall a\in A\;\exists!b\in B\;((a,b)\in f).
$$

La condición puede separarse en:

- **totalidad**: cada $a\in A$ aparece como primera componente de algún par;
- **unicidad de salida**: si $(a,b_1)\in f$ y $(a,b_2)\in f$, entonces $b_1=b_2$.

Por ejemplo, si $A=\{1,2,3\}$ y $B=\{a,b\}$,

$$
f=\{(1,a),(2,a),(3,b)\}
$$

es una función. En cambio,

$$
R=\{(1,a),(1,b),(2,a)\}
$$

falla por dos motivos: $1$ tiene dos salidas y $3$ no tiene ninguna.

Una función sigue siendo una relación; no abandonamos el lenguaje de C8. Estamos seleccionando relaciones con una propiedad adicional.

***
### Totalidad y unicidad: dos comprobaciones independientes

Sobre $A=\{1,2\}$ y $B=\{u,v\}$, cada relación de la tabla está contenida en $A\times B$. Esa pertenencia al producto cartesiano no basta para que sea una función.

| Relación | ¿Todas las entradas tienen salida? | ¿Cada entrada tiene a lo sumo una salida? | ¿Es función $A\to B$? |
|---|---|---|---|
| $\varnothing$ | No | Sí | No |
| $\{(1,u),(1,v)\}$ | No | No | No |
| $\{(1,u),(1,v),(2,u)\}$ | Sí | No | No |
| $\{(1,u),(2,u)\}$ | Sí | Sí | Sí |

Para comprobar totalidad, fijamos una entrada arbitraria y buscamos al menos un par que comience con ella. Para comprobar unicidad, suponemos que hay dos pares con la misma primera componente y comprobamos que sus segundas componentes coinciden. Son obligaciones distintas: no encontrar dos salidas diferentes no demuestra que exista alguna.

La última fila también muestra que dos entradas pueden compartir salida. Esto no contradice la definición de función: la unicidad se exige **para una entrada fija**. La prohibición de colisiones entre entradas distintas aparecerá en [§9.7](algebra-para-matematicos-capitulo-9-funciones-composicion-e-inversas.md#apm-c09-s07), como una condición adicional.

Añadir pares puede completar entradas ausentes, pero no elimina una colisión ya presente. Quitar pares puede eliminar una colisión, pero no crea una salida para una entrada ausente. Al reparar una relación conviene diagnosticar primero cuál de esas dos tareas hace falta.

**Para comprobarlo.** Parta de $R=\{(1,u),(1,v)\}$. Una modificación consiste en añadir o retirar un solo par. ¿Cuál es el menor número de modificaciones necesario para convertir $R$ en una función $A\to B$? Describa todas las funciones obtenidas con ese mínimo.

**Solución.** Hay que retirar al menos uno de los dos pares que comienzan con $1$, porque sus salidas son distintas. También hay que añadir un par que comience con $2$, porque esa entrada no tiene salida. Una sola modificación no puede realizar ambas tareas; se necesitan al menos dos.

Dos bastan: conservamos una de las salidas de $1$ y elegimos una salida para $2$. Las cuatro posibilidades son $\{(1,u),(2,u)\}$, $\{(1,u),(2,v)\}$, $\{(1,v),(2,u)\}$ y $\{(1,v),(2,v)\}$. Cada una tiene exactamente un par por entrada. La lista es exhaustiva: en dos modificaciones debemos hacer precisamente una retirada y una adición, con las elecciones indicadas.

Si $A=\varnothing$, no hay entradas cuya salida deba existir o ser única: la relación vacía es función hacia cualquier $B$. Si $A\ne\varnothing$ y $B=\varnothing$, ninguna entrada puede recibir salida y no existe función $A\to B$.

***
## 9.2. Dominio, codominio e imagen {#apm-c09-s02}
***
La notación

$$
f:A\to B
$$

declara dos conjuntos que forman parte de los datos de la función:

- $A$: **dominio**;
- $B$: **codominio**.

La **imagen** es

$$
\operatorname{Im}(f)=\{f(a):a\in A\}.
$$

Siempre

$$
\operatorname{Im}(f)\subseteq B,
$$

pero no necesariamente hay igualdad.

Esta distinción será decisiva para la sobreyectividad. La regla $f(x)=x^2$ con dominio $\mathbb R$ tiene imagen $[0,\infty)$. Si el codominio declarado es $\mathbb R$, no es sobreyectiva; si es $[0,\infty)$, sí lo es.

***
## 9.3. Notación funcional y evaluación {#apm-c09-s03}
***
Si $f:A\to B$ y el único par de $f$ cuya primera componente es $a$ es $(a,b)$, escribimos

$$
f(a)=b.
$$

Hay que distinguir cuatro objetos:

- la función $f$;
- una entrada $a$;
- el valor $f(a)$;
- una fórmula que pueda describir a $f$.

La fórmula no es la función completa. Por ejemplo, “$x^2$” no informa por sí sola dominio ni codominio.

Las funciones pueden estar dadas por listas, tablas, diagramas, fórmulas o reglas por casos. La definición estructural es independiente del modo de representación.

***
## 9.4. Igualdad de funciones {#apm-c09-s04}
***
Para comparar funciones hay que controlar sus datos.

Si $f,g:A\to B$, entonces

$$
f=g\quad\Longleftrightarrow\quad\forall a\in A\;(f(a)=g(a)).
$$

Si cambian dominio o codominio, editorialmente tratamos las funciones como objetos distintos, incluso cuando usan la misma regla simbólica.

Por ejemplo, $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, y $g:\mathbb R\to[0,\infty)$, $g(x)=x^2$, tienen los mismos valores en cada real, pero distinto codominio y distinto comportamiento respecto de la sobreyectividad.

***
### Comparar los datos antes de comparar valores

En este capítulo una función lleva consigo el dominio y el codominio declarados. Su gráfica registra los pares entrada–salida, pero no permite recuperar por sí sola un codominio que contenga elementos nunca alcanzados. Para comparar dos funciones comprobamos primero esos conjuntos; sólo cuando coinciden basta demostrar igualdad de valores para toda entrada.

Sean $A=\{1,2\}$, $B=\{u\}$ y $C=\{u,v\}$. Las asignaciones $f:A\to B$ y $g:A\to C$ con $f(1)=f(2)=g(1)=g(2)=u$ tienen la misma gráfica $\{(1,u),(2,u)\}$. Bajo la convención de [§9.4](algebra-para-matematicos-capitulo-9-funciones-composicion-e-inversas.md#apm-c09-s04) son objetos distintos. Además, $f$ alcanza todo su codominio y $g$ deja $v$ sin alcanzar. La diferencia declarada tiene una consecuencia matemática.

**Para comprobarlo.** Sea $h:\{1\}\to B$, $h(1)=u$. ¿Coincide con $f$ porque ambas usan la regla «enviar a $u$»? ¿Y coincide con la restricción $f|_{\{1\}}$?

**Solución.** No coincide con $f$: sus dominios son distintos. Sí coincide con la restricción, porque ambas tienen dominio $\{1\}$, codominio $B$ y valor $u$ en la única entrada. Una regla verbal común no reemplaza la comprobación de esos tres datos.

***
## 9.5. Imágenes de subconjuntos {#apm-c09-s05}
***
Si $S\subseteq A$, definimos la imagen de $S$ por

$$
f(S)=\{f(x):x\in S\}.
$$

Para $S,T\subseteq A$ siempre se cumple

$$
f(S\cup T)=f(S)\cup f(T).
$$

También

$$
f(S\cap T)\subseteq f(S)\cap f(T),
$$

pero la inclusión puede ser estricta.

Ejemplo: si $f:\mathbb R\to\mathbb R$ es $f(x)=x^2$, $S=\{-1\}$ y $T=\{1\}$, entonces $S\cap T=\varnothing$, de modo que $f(S\cap T)=\varnothing$, mientras

$$
f(S)\cap f(T)=\{1\}.
$$

La colisión $f(-1)=f(1)$ explica la diferencia. Cuando $f$ es inyectiva, la igualdad de intersecciones sí se recupera.

***
## 9.6. Preimágenes, restricciones y cambio de codominio {#apm-c09-s06}
***
Si $T\subseteq B$, la **preimagen** de $T$ es

$$
f^{-1}(T)=\{x\in A:f(x)\in T\}.
$$

Esta notación tiene sentido aunque $f$ no posea función inversa.

La preimagen preserva exactamente las operaciones básicas:

$$
f^{-1}(T\cup U)=f^{-1}(T)\cup f^{-1}(U),
$$

$$
f^{-1}(T\cap U)=f^{-1}(T)\cap f^{-1}(U),
$$

$$
f^{-1}(B\setminus T)=A\setminus f^{-1}(T).
$$

Si $S\subseteq A$, la **restricción** $f|_S:S\to B$ usa la misma regla de $f$, pero sólo admite entradas de $S$.

También podemos reemplazar el codominio por un conjunto menor que contenga la imagen. Este cambio puede alterar la sobreyectividad, pero no los valores de la función.

***
## 9.7. Inyectividad {#apm-c09-s07}
***
Una función $f:A\to B$ es **inyectiva** si

$$
f(x_1)=f(x_2)\Rightarrow x_1=x_2.
$$

Equivalentemente, por contraposición,

$$
x_1\ne x_2\Rightarrow f(x_1)\ne f(x_2).
$$

Una función inyectiva no presenta colisiones entre entradas distintas.

La inclusión de la sección anterior se fortalece: si $f$ es inyectiva, entonces para todo $S,T\subseteq A$,

$$
f(S\cap T)=f(S)\cap f(T).
$$

La inclusión de izquierda a derecha siempre vale. Para la otra, si $y\in f(S)\cap f(T)$, existen $s\in S$ y $t\in T$ con $f(s)=y=f(t)$. La inyectividad fuerza $s=t$, de modo que ese elemento pertenece a $S\cap T$.

***
## 9.8. Sobreyectividad {#apm-c09-s08}
***
Una función $f:A\to B$ es **sobreyectiva** si

$$
\forall b\in B\;\exists a\in A\;(f(a)=b).
$$

Equivale a

$$
\operatorname{Im}(f)=B.
$$

La sobreyectividad depende del codominio. No es correcto preguntar simplemente “¿$f$ es sobreyectiva?” sin saber hacia qué conjunto se declara la función.

Para probar sobreyectividad suele tomarse un $b\in B$ arbitrario y construirse una entrada $a\in A$ con $f(a)=b$.

***
## 9.9. Biyectividad {#apm-c09-s09}
***
Una función es **biyectiva** cuando es inyectiva y sobreyectiva.

Esto significa:

- cada elemento del codominio recibe al menos una preimagen;
- ningún elemento del codominio recibe más de una preimagen.

Por tanto cada $b\in B$ corresponde a exactamente un $a\in A$.

Las biyecciones serán precisamente las funciones que pueden deshacerse mediante una función inversa.

***
## 9.10. Composición de funciones {#apm-c09-s10}
***
Sean

$$
f:A\to B,\qquad g:B\to C.
$$

La composición es

$$
g\circ f:A\to C,
$$

definida por

$$
(g\circ f)(a)=g(f(a)).
$$

El orden es importante: **primero actúa $f$, después $g$**.

Si los conjuntos intermedios no son compatibles, la composición puede no estar definida con los tipos declarados.

La composición no es conmutativa en general. Para funciones numéricas, por ejemplo, si $f(x)=x+1$ y $g(x)=x^2$,

$$
(g\circ f)(x)=(x+1)^2,
$$

mientras

$$
(f\circ g)(x)=x^2+1.
$$

***
## 9.11. Identidad y asociatividad {#apm-c09-s11}
***
Para cada conjunto $A$, la función identidad es

$$
\operatorname{id}_A:A\to A,\qquad\operatorname{id}_A(a)=a.
$$

Si $f:A\to B$,

$$
f\circ\operatorname{id}_A=f,
$$

$$
\operatorname{id}_B\circ f=f.
$$

Además, si las composiciones tienen tipos compatibles,

$$
h\circ(g\circ f)=(h\circ g)\circ f.
$$

La prueba es puntual: para cada $a$,

$$
[h\circ(g\circ f)](a)=h(g(f(a)))=[(h\circ g)\circ f](a).
$$

La asociatividad permite escribir $h\circ g\circ f$ sin ambigüedad de paréntesis, aunque el orden de las funciones no pueda permutarse.

***
## 9.12. Inyectividad y sobreyectividad bajo composición {#apm-c09-s12}
***
Sean $f:A\to B$ y $g:B\to C$.

Si ambas son inyectivas y

$$
(g\circ f)(x_1)=(g\circ f)(x_2),
$$

la inyectividad de $g$ da $f(x_1)=f(x_2)$ y la de $f$ da $x_1=x_2$. Luego $g\circ f$ es inyectiva.

Si ambas son sobreyectivas, dado $c\in C$, existe $b\in B$ con $g(b)=c$, y existe $a\in A$ con $f(a)=b$. Entonces $(g\circ f)(a)=c$.

Hay dos conclusiones útiles en sentido inverso:

- si $g\circ f$ es inyectiva, entonces $f$ es inyectiva;
- si $g\circ f$ es sobreyectiva, entonces $g$ es sobreyectiva.

Las otras recíprocas son falsas en general y deben controlarse mediante contraejemplos.

***
### Qué parte del conjunto intermedio visita la composición

Para $f:A\to B$ y $g:B\to C$, la composición sólo evalúa $g$ en los elementos de $f(A)$. No examina por separado todos los puntos de $B$. Por eso una colisión de $g$ que ocurra fuera de esa parte puede quedar oculta.

| Dato sobre $g\circ f$ | Conclusión necesaria | Conclusión que no queda garantizada |
|---|---|---|
| Inyectividad | $f$ es inyectiva | $g$ es inyectiva en todo $B$ |
| Sobreyectividad | $g$ es sobreyectiva | $f$ alcanza todo $B$ |

La primera conclusión se obtiene empezando con $f(a_1)=f(a_2)$ y aplicando $g$; no requiere cancelar $g$. La segunda comienza con un $c\in C$ arbitrario y usa una entrada $a$ que la composición envía a $c$: entonces $f(a)$ proporciona la preimagen requerida para $g$.

**Para comprobarlo.** Tome $A=\{1,2\}$, $B=\{u,v,w\}$ y $C=\{0,1\}$. Defina $f(1)=u$, $f(2)=v$ y $g(u)=0$, $g(v)=1$, $g(w)=0$. Determine qué defectos quedan fuera de la parte visitada.

**Solución.** La composición envía $1$ a $0$ y $2$ a $1$: es biyectiva. $f$ no alcanza $w$ y $g$ identifica $u$ con $w$, de modo que no es inyectiva. El punto $w$ no se visita al componer, así que no produce una colisión entre las entradas de $A$. La restricción de $g$ a $\{u,v\}$ sí es biyectiva hacia $C$.

***
## 9.13. Función inversa {#apm-c09-s13}
***
Sea $f:A\to B$ una biyección. Para cada $b\in B$ existe exactamente un $a\in A$ con $f(a)=b$. Podemos definir

$$
f^{-1}:B\to A
$$

por

$$
f^{-1}(b)=a\quad\Longleftrightarrow\quad f(a)=b.
$$

Entonces

$$
f^{-1}\circ f=\operatorname{id}_A
$$

y

$$
f\circ f^{-1}=\operatorname{id}_B.
$$

La inversa no es $1/f$. Tampoco basta “despejar” una expresión: hay que verificar dominios, codominios y unicidad.

***
## 9.14. Invertibilidad e inversas laterales {#apm-c09-s14}
***
Una función tiene inversa bilateral si y sólo si es biyectiva.

La dirección “biyectiva $\Rightarrow$ invertible” construye $f^{-1}$ usando existencia y unicidad. Para la dirección contraria, si existe $g:B\to A$ con

$$
g\circ f=\operatorname{id}_A,\qquad f\circ g=\operatorname{id}_B,
$$

entonces $f$ es inyectiva y sobreyectiva.

También aparecen inversas laterales:

- $g\circ f=\operatorname{id}_A$: $g$ es inversa izquierda de $f$ y fuerza que $f$ sea inyectiva;
- $f\circ h=\operatorname{id}_B$: $h$ es inversa derecha de $f$ y fuerza que $f$ sea sobreyectiva.

Cuando existe una inversa bilateral, es única.

***
### Construir primero una asignación bien definida

La expresión «envíe $b$ a un $a$ que cumpla $f(a)=b$» necesita dos justificaciones antes de definir una función $B\to A$. Para cada $b\in B$ debe existir una entrada admisible $a\in A$; además, dos entradas que satisfagan la condición deben ser iguales. La sobreyectividad aporta existencia y la inyectividad aporta unicidad.

Una vez construida $g$, las dos composiciones responden preguntas distintas. Para $a\in A$, el propio $a$ es una preimagen de $f(a)$; por unicidad, $g(f(a))=a$. Para $b\in B$, la entrada $g(b)$ fue elegida precisamente para cumplir $f(g(b))=b$. Así se verifican las identidades sobre sus respectivos dominios.

Una identidad lateral no puede sustituir ambas comprobaciones. Tampoco debe usarse la supuesta inversa para probar la unicidad que todavía hace falta para construirla: ese razonamiento sería circular.

**Para comprobarlo.** Considere $f:\{1,2\}\to\{u,v\}$, $f(1)=u$, $f(2)=v$. Construya $g$ justificando existencia y unicidad antes de calcular las composiciones.

**Solución.** Para $u$ existe la preimagen $1$ y es única porque $2$ va a $v$; para $v$ existe la preimagen $2$ y es única porque $1$ va a $u$. Definimos entonces $g(u)=1$, $g(v)=2$. Las evaluaciones dan $g(f(1))=1$, $g(f(2))=2$, $f(g(u))=u$ y $f(g(v))=v$. Son las dos identidades requeridas, no sólo coincidencias de fórmulas.

***
## 9.15. Dos significados de $f^{-1}$ {#apm-c09-s15}
***
La notación $f^{-1}$ tiene dos usos que deben distinguirse por tipo.

Si $f$ es biyectiva,

$$
f^{-1}:B\to A
$$

es una **función inversa**.

Para cualquier función $f:A\to B$ y cualquier $T\subseteq B$,

$$
f^{-1}(T)=\{x\in A:f(x)\in T\}
$$

es una **preimagen**.

Ejemplo: $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, no tiene función inversa en esos dominios, pero

$$
f^{-1}(\{1\})=\{-1,1\}
$$

está perfectamente definida como preimagen.

***
### Leer el argumento de la notación inversa

La preimagen recibe un **subconjunto** del codominio y devuelve un subconjunto del dominio. No exige escoger una sola entrada para cada valor: reúne todas las entradas que cumplen la condición. Por eso sigue definida cuando hay colisiones o valores sin alcanzar.

Para $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, tenemos $f^{-1}(\{4\})=\{-2,2\}$ y $f^{-1}(\{-1\})=\varnothing$. El primer resultado tiene dos elementos y el segundo ninguno. Ninguno de esos hechos contradice la definición de preimagen; ambos impedirían construir una inversa bilateral de esta función.

**Para comprobarlo.** Calcule $f^{-1}(\varnothing)$ y $f^{-1}(\{-1,4\})$. Explique si la primera respuesta depende de que $f$ sea inyectiva.

**Solución.** Ningún valor puede pertenecer al conjunto vacío, así que $f^{-1}(\varnothing)=\varnothing$. La segunda condición dice $x^2=-1$ o $x^2=4$; la primera es imposible en $\mathbb R$ y la segunda tiene soluciones $-2,2$. Por tanto la preimagen es $\{-2,2\}$. La preimagen del vacío es vacía para cualquier función: se deduce de pertenencia, sin usar inyectividad ni existencia de inversa.

***
## 9.16. Cierre — de función a estructura {#apm-c09-s16}
***
Ante una función conviene preguntar:

1. ¿cuáles son dominio y codominio?;
2. ¿la relación es total y tiene salida única?;
3. ¿cuál es la imagen?;
4. ¿es inyectiva?;
5. ¿es sobreyectiva?;
6. ¿es biyectiva?;
7. ¿las composiciones están bien tipadas?;
8. ¿interviene una identidad?;
9. ¿$f^{-1}$ significa inversa o preimagen?;
10. ¿qué identidad de composición debe verificarse?

La composición, la identidad y la inversa forman un lenguaje que reaparecerá en toda la serie. Más adelante una pregunta será central:

> **¿Qué ocurre cuando una función, además de asignar elementos, conserva las operaciones de una estructura algebraica?**

Ése será el horizonte de los homomorfismos. Aquí cerramos antes de desarrollarlo.

***
# Ejercicios
***
Todos los ejercicios son originales para *Álgebra para matemáticos* y se calibran con el corpus rector del capítulo. Los identificadores editoriales se conservan sólo en comentarios internos no renderizados.

## A. De relaciones a funciones
***
**1.** **Nivel A.** Sean $A=\{1,2,3\}$ y $B=\{a,b\}$. Decide si $R=\{(1,a),(2,a),(3,b)\}$ es una función $A\to B$.


**2.** **Nivel B.** Con los mismos conjuntos, decide si $R=\{(1,a),(1,b),(2,a),(3,b)\}$ es función y localiza el axioma que falla.


**3.** **Nivel B.** Con los mismos conjuntos, decide si $R=\{(1,a),(2,b)\}$ define una función $A\to B$.


**4.** **Nivel C.** Explica por qué la relación vacía $\varnothing\subseteq A\times B$ es función $A\to B$ exactamente cuando $A=\varnothing$.


**5.** **Nivel C.** Sea $R\subseteq A\times B$ una relación. Reescribe «$R$ es función de $A$ en $B$» usando cuantificadores, conectivos lógicos, igualdad y pertenencia, sin emplear $\exists!$.


**6.** **Nivel D.** Si $A$ tiene $m$ elementos y $B$ tiene $n$ elementos, ¿cuántas funciones $A\to B$ existen? Justifica.

## B. Dominio, codominio, imagen y evaluación
***
**7.** **Nivel A.** Sea $f:\{1,2,3\}\to\{a,b,c,d\}$ dada por $f(1)=a$, $f(2)=a$, $f(3)=c$. Determina dominio, codominio e imagen.


**8.** **Nivel B.** Para $f:\mathbb R\to\mathbb R$, $f(x)=x^2+1$, calcula $f(0)$, $f(-2)$ y describe $\operatorname{Im}(f)$.


**9.** **Nivel B.** Una tabla asigna $1\mapsto 2$, $2\mapsto 4$, $3\mapsto 6$. Escribe la función como conjunto de pares.


**10.** **Nivel C.** Compara $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, y $g:\mathbb R\to[0,\infty)$, $g(x)=x^2$. ¿Tienen los mismos valores? ¿Son el mismo objeto en este capítulo?


**11.** **Nivel C.** Sea $f:A\to B$. Demuestra que $\operatorname{Im}(f)\subseteq B$.


**12.** **Nivel C.** Da un ejemplo de una función cuyo modo natural de definición no sea una sola fórmula algebraica.

## C. Imágenes y preimágenes de subconjuntos
***
**13.** **Nivel A.** Sea $f:\{1,2,3,4\}\to\{a,b,c\}$ con $f(1)=a,f(2)=a,f(3)=b,f(4)=c$. Calcula $f(\{1,3,4\})$.


**14.** **Nivel B.** Con la misma función, calcula $f^{-1}(\{a,c\})$.


**15.** **Nivel C.** Demuestra que $f(S\cup T)=f(S)\cup f(T)$ para $S,T\subseteq A$.


**16.** **Nivel C.** Demuestra $f(S\cap T)\subseteq f(S)\cap f(T)$ y da un ejemplo donde la inclusión sea estricta.


**17.** **Nivel C.** Demuestra $f^{-1}(U\cup V)=f^{-1}(U)\cup f^{-1}(V)$.


**18.** **Nivel D.** Demuestra $f^{-1}(B\setminus U)=A\setminus f^{-1}(U)$ para $U\subseteq B$.

## D. Igualdad, restricciones y cambio de codominio
***
**19.** **Nivel B.** Sean $f,g:\mathbb R\to\mathbb R$ dadas por $f(x)=(x+1)^2$ y $g(x)=x^2+2x+1$. Demuestra que $f=g$.


**20.** **Nivel B.** Sea $f:\mathbb R\to\mathbb R$, $f(x)=x^2$. Describe $f|_{[0,\infty)}$.


**21.** **Nivel C.** ¿Puede la función anterior recodificarse como $g:[0,\infty)\to[0,\infty)$, $g(x)=x^2$? Justifica.


**22.** **Nivel C.** Explica por qué no es válido declarar $h:\mathbb R\to(-\infty,0]$, $h(x)=x^2$.


**23.** **Nivel C.** Sea $f:A\to B$ y $S\subseteq A$. Demuestra que $\operatorname{Im}(f|_S)=f(S)$.


**24.** **Nivel D.** Dos funciones tienen la misma gráfica como conjunto de pares, pero una se declara $A\to B$ y otra $A\to C$ con $B\ne C$. Explica por qué el codominio impide identificarlas en la convención de C9.

## E. Inyectividad
***
**25.** **Nivel B.** Decide si $f:\mathbb R\to\mathbb R$, $f(x)=2x-3$, es inyectiva.


**26.** **Nivel B.** Decide si $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, es inyectiva.


**27.** **Nivel C.** Demuestra que la inclusión $i:S\hookrightarrow A$, $i(s)=s$, es inyectiva.


**28.** **Nivel C.** Demuestra que si $f$ es inyectiva, entonces $f(S\cap T)=f(S)\cap f(T)$.


**29.** **Nivel D.** Demuestra que si $f(S\cap T)=f(S)\cap f(T)$ para todos $S,T\subseteq A$, entonces $f$ es inyectiva.


**30.** **Nivel D.** Sea $f:A\to B$. Demuestra que $f$ es inyectiva si y sólo si $f^{-1}(f(S))=S$ para todo $S\subseteq A$.

## F. Sobreyectividad
***
**31.** **Nivel B.** Decide si $f:\mathbb R\to\mathbb R$, $f(x)=x^3$, es sobreyectiva.


**32.** **Nivel B.** Decide si $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, es sobreyectiva.


**33.** **Nivel C.** Explica por qué $g:\mathbb R\to[0,\infty)$, $g(x)=x^2$, sí es sobreyectiva.


**34.** **Nivel C.** Sea $f:A\to B$. Demuestra que $f$ es sobreyectiva si y sólo si $f(f^{-1}(T))=T$ para todo $T\subseteq B$.


**35.** **Nivel C.** Sea $f:A\to B$ y supón que existe $b_0\in B$ sin preimagen. ¿Qué conclusión inmediata obtienes?


**36.** **Nivel D.** Si $A$ y $B$ son finitos con $|A|<|B|$, demuestra que no existe función sobreyectiva $A\to B$.

## G. Biyectividad
***
**37.** **Nivel B.** Decide si $f:\mathbb R\to\mathbb R$, $f(x)=3x+2$, es biyectiva.


**38.** **Nivel C.** Decide si $f:[0,\infty)\to[0,\infty)$, $f(x)=x^2$, es biyectiva.


**39.** **Nivel C.** Si $A$ y $B$ son finitos con igual cardinalidad, demuestra que una función inyectiva $f:A\to B$ es sobreyectiva.


**40.** **Nivel C.** En la situación anterior, demuestra también que una función sobreyectiva es inyectiva.


**41.** **Nivel D.** Sea $f:A\to B$ biyectiva. Explica por qué para cada $b\in B$ existe exactamente un $a\in A$ con $f(a)=b$.


**42.** **Nivel D.** Construye una biyección entre $\{1,2,3,4\}$ y $\{a,b,c,d\}$ y justifica sin enumerar todas las propiedades por separado.

## H. Composición
***
**43.** **Nivel A.** Si $f(x)=x+1$ y $g(x)=2x$, calcula $(g\circ f)(3)$.


**44.** **Nivel B.** Con las mismas funciones, calcula fórmulas para $g\circ f$ y $f\circ g$.


**45.** **Nivel B.** Sean $f:A\to B$ y $g:C\to D$. ¿Qué condición sencilla garantiza que $g\circ f$ esté definida como composición total sobre $A$?


**46.** **Nivel C.** Sean $f:\{1,2,3\}\to\{a,b\}$ con $1,2\mapsto a$ y $3\mapsto b$, y $g:\{a,b\}\to\{0,1\}$ con $g(a)=0,g(b)=1$. Escribe $g\circ f$.


**47.** **Nivel C.** Demuestra que si $f$ y $g$ son inyectivas, entonces $g\circ f$ es inyectiva.


**48.** **Nivel C.** Demuestra que si $f$ y $g$ son sobreyectivas, entonces $g\circ f$ es sobreyectiva.


**49.** **Nivel D.** Demuestra que si $g\circ f$ es inyectiva, entonces $f$ es inyectiva.


**50.** **Nivel D.** Demuestra que si $g\circ f$ es sobreyectiva, entonces $g$ es sobreyectiva.

## I. Identidad y asociatividad
***
**51.** **Nivel A.** Escribe $\operatorname{id}_{\{1,2,3\}}$ como conjunto de pares.


**52.** **Nivel B.** Demuestra $f\circ\operatorname{id}_A=f$ para $f:A\to B$.


**53.** **Nivel B.** Demuestra $\operatorname{id}_B\circ f=f$.


**54.** **Nivel C.** Demuestra la asociatividad $h\circ(g\circ f)=(h\circ g)\circ f$.


**55.** **Nivel C.** Da un ejemplo explícito que muestre que la composición no es conmutativa.


**56.** **Nivel D.** Si $f:A\to B$ y $g:B\to A$ satisfacen $g\circ f=\operatorname{id}_A$, explica por qué $f$ no puede identificar dos entradas distintas.

## J. Inversas
***
**57.** **Nivel B.** Encuentra la inversa de $f:\mathbb R\to\mathbb R$, $f(x)=2x+5$.


**58.** **Nivel C.** Encuentra la inversa de $f:[0,\infty)\to[0,\infty)$, $f(x)=x^2$.


**59.** **Nivel C.** Explica por qué $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, no tiene función inversa.


**60.** **Nivel C.** Demuestra que si $g$ y $h$ son dos inversas bilaterales de $f$, entonces $g=h$.


**61.** **Nivel D.** Demuestra que si $f$ posee una inversa bilateral, entonces es inyectiva.


**62.** **Nivel D.** Demuestra que si $f$ posee una inversa bilateral, entonces es sobreyectiva.


**63.** **Nivel D.** Demuestra que si $f$ es biyectiva, entonces la definición $f^{-1}(b)=a\Longleftrightarrow f(a)=b$ produce una función bien definida.


**64.** **Nivel D.** Concluye que $f$ es invertible si y sólo si es biyectiva.

## K. Preimagen frente a inversa
***
**65.** **Nivel B.** Para $f:\mathbb R\to\mathbb R$, $f(x)=x^2$, calcula $f^{-1}(\{4\})$ e interpreta la notación.


**66.** **Nivel B.** Para la misma función, calcula $f^{-1}([0,9])$.


**67.** **Nivel C.** Si $f$ es biyectiva y $T\subseteq B$, relaciona la preimagen $f^{-1}(T)$ con la imagen de $T$ bajo la función inversa.


**68.** **Nivel D.** Refuta la afirmación «$f^{-1}(x)=1/f(x)$» con un ejemplo sencillo.

## L. Síntesis y transferencia
***
**69.** **Nivel D.** Sea $f:A\to B$ y $g:B\to C$. Si $g\circ f$ es biyectiva, ¿qué puedes concluir necesariamente sobre $f$ y sobre $g$?


**70.** **Nivel D.** Construye un ejemplo finito donde $g\circ f$ sea biyectiva, $f$ no sea sobreyectiva y $g$ no sea inyectiva.


**71.** **Nivel E.** Sea $f:A\to B$. Demuestra que si existe $g:B\to A$ con $g\circ f=\operatorname{id}_A$, entonces $f$ es inyectiva; y si existe $h:B\to A$ con $f\circ h=\operatorname{id}_B$, entonces $f$ es sobreyectiva.


**72.** **Nivel E.** Si $f:A\to B$ y $g:B\to C$ son biyectivas, demuestra que $g\circ f$ es biyectiva y anticipa una fórmula para su inversa.

## M. Problemas avanzados tipo prueba
***
**73.** **Nivel E.** Demuestra la equivalencia de las siguientes condiciones para $f:A\to B$:

(i) $f$ es inyectiva;  
(ii) para todos $S,T\subseteq A$, $f(S\cap T)=f(S)\cap f(T)$;  
(iii) para todo $S\subseteq A$, $f^{-1}(f(S))=S$.

Organiza la prueba como un ciclo de implicaciones y explicita dónde se usa inyectividad.


**74.** **Nivel E.** Sean $f:A\to B$, $g:B\to C$, $S\subseteq A$ y $U\subseteq C$.

(a) Demuestra $(g\circ f)(S)=g(f(S))$.  
(b) Demuestra $(g\circ f)^{-1}(U)=f^{-1}(g^{-1}(U))$.  
(c) Explica por qué (b) no requiere que $f$ ni $g$ sean invertibles.


**75.** **Nivel F.** Supón $f:A\to B$ y $g:B\to C$ y que $g\circ f:A\to C$ es biyectiva.

(a) Demuestra que $f$ es inyectiva.  
(b) Demuestra que $g$ es sobreyectiva.  
(c) Construye un contraejemplo finito donde $f$ no sea sobreyectiva.  
(d) Construye un contraejemplo finito donde $g$ no sea inyectiva.  
(e) Formula hipótesis adicionales suficientes para concluir que ambos son biyectivos.


**76.** **Nivel F.** Refuta mediante ejemplos separados las recíprocas falsas:

(a) «si $f$ es inyectiva, entonces $g\circ f$ es inyectiva»;  
(b) «si $g$ es sobreyectiva, entonces $g\circ f$ es sobreyectiva»;  
(c) «si $g\circ f$ es inyectiva, entonces $g$ es inyectiva»;  
(d) «si $g\circ f$ es sobreyectiva, entonces $f$ es sobreyectiva».

En cada caso explica qué parte de la composición oculta el defecto.


**77.** **Nivel F.** Demuestra cuidadosamente el teorema:

> Una función $f:A\to B$ posee una inversa bilateral si y sólo si es biyectiva.

En la dirección constructiva debes demostrar que la definición de $f^{-1}$ es una función antes de verificar las composiciones.


**78.** **Nivel G.** Sean $f:A\to B$, $g:B\to A$ y $h:B\to A$ tales que

$$
g\circ f=\operatorname{id}_A,\qquad f\circ h=\operatorname{id}_B.
$$

Demuestra, sin suponer previamente biyectividad, que $f$ es biyectiva y que necesariamente $g=h=f^{-1}$.


**79.** **Nivel G.** Sean $f:A\to B$ y $g:B\to C$ biyecciones. Demuestra

$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}.
$$

Tu demostración debe controlar los tipos de todas las funciones y verificar ambas composiciones con la identidad.


**80.** **Nivel G.** Sean conjuntos finitos $A,B,C$ y funciones $f:A\to B$, $g:B\to C$. Se sabe que $|A|=|C|=4$, $|B|=6$ y que $g\circ f:A\to C$ es biyectiva.

(a) Determina qué puede afirmarse necesariamente de $f$ y $g$.  
(b) ¿Puede $f$ ser sobreyectiva?  
(c) ¿Puede $g$ ser inyectiva?  
(d) Describe la estructura mínima que deben tener $f(A)\subseteq B$ y la restricción $g|_{f(A)}$.  
(e) Construye un ejemplo concreto con estos cardinales.

***
## N. Construir composiciones con datos prescritos


**81.** **Nivel E. Completar una función después de otra.** Sean $A=\{1,2,3,4\}$, $B=\{a,b,c,d\}$ y $C=\{0,1\}$. Defina $f:A\to B$ por $f(1)=f(2)=a$, $f(3)=b$, $f(4)=c$, y $h:A\to C$ por $h(1)=h(2)=0$, $h(3)=h(4)=1$. Determine todas las funciones $g:B\to C$ tales que $g\circ f=h$.


**82.** **Nivel F. Elegir las entradas intermedias.** Sean $A=\{1,2,3\}$, $B=\{a,b,c\}$ y $C=\{0,1\}$. Fije $g(a)=0$, $g(b)=g(c)=1$ y $h(1)=h(2)=1$, $h(3)=0$. Encuentre todas las $f:A\to B$ que cumplen $g\circ f=h$, y cuente cuántas son inyectivas.


**83.** **Nivel F. Cuándo puede pasarse por una función dada.** Sea $f:A\to B$ con $f(A)=B$ y sea $h:A\to C$. Pruebe que existe $g:B\to C$ con $g\circ f=h$ si y sólo si $f(x)=f(y)$ implica $h(x)=h(y)$. Demuestre también que, cuando existe, $g$ es única.


**84.** **Nivel D. El dominio admisible de una composición.** Sean $f:\mathbb R\to\mathbb R$, $f(x)=x-1$, y $g:\mathbb R\setminus\{0\}\to\mathbb R$, $g(t)=1/t$. Encuentre el mayor subconjunto $S\subseteq\mathbb R$ en el que $g(f(x))$ está definido para toda entrada. Declare las funciones intermedias necesarias y la fórmula de la composición.


**85.** **Nivel E. Dos composiciones con dominios distintos.** Sean $f:\mathbb R\to[0,\infty)$, $f(x)=x^2$, y $g:[0,\infty)\to\mathbb R$, $g(y)=\sqrt y$. Calcule ambas composiciones y sus tipos. ¿Qué identidad se cumple y por qué no basta para afirmar que $g$ es inversa bilateral de $f$?


**86.** **Nivel F. Contar factorizaciones de la identidad.** Para $A=\{1,2\}$ y $B=\{a,b,c\}$, cuente todos los pares de funciones $f:A\to B$, $g:B\to A$ que cumplen $g\circ f=\operatorname{id}_A$. ¿Puede algún $g$ de esos pares ser inyectivo? Justifique el conteo sin duplicaciones.


## O. Imágenes, preimágenes y cambios de conjuntos


**87.** **Nivel D. Restricción y cambio de codominio en una tabla.** Sea $f:\{1,2,3,4\}\to\{a,b,c,d\}$ con valores $a,a,b,c$, en ese orden. Para $S=\{2,3\}$ y $T=\{a,d\}$, calcule $f(S)$ y $f^{-1}(T)$. Restrinja a $S$ y reduzca después el codominio al menor conjunto posible. Determine si la función resultante es biyectiva y qué sucede con las preimágenes.


**88.** **Nivel E. Separar valores alcanzables e inalcanzables.** Para $f:\mathbb R\to\mathbb R$, $f(x)=x^2+1$, calcule las preimágenes de $\varnothing$, $\{-2,1,5\}$ y $(1,5]$. Repita para la restricción a $[0,\infty)$ con codominio $[1,\infty)$, usando en el segundo caso $\{1,5\}$. Explique cada pérdida de entradas.


**89.** **Nivel F. Recuperar todas las entradas indistinguibles.** Sea $f:A\to B$ y defina $K(S)=f^{-1}(f(S))$ para $S\subseteq A$. Pruebe $S\subseteq K(S)$ y $K(K(S))=K(S)$. Caracterice exactamente los subconjuntos que cumplen $K(S)=S$ usando los conjuntos $F_b=\{x\in A:f(x)=b\}$.


**90.** **Nivel E. Imagen de una preimagen sin sobreyectividad.** Para cualquier $f:A\to B$ y $T\subseteq B$, demuestre $f(f^{-1}(T))=T\cap\operatorname{Im}(f)$. Aplíquelo a la función constante $f:\{1,2\}\to\{u,v\}$ de valor $u$, para todos los subconjuntos de su codominio.


**91.** **Nivel F. Cuándo dos conjuntos tienen la misma preimagen.** Pruebe que $f^{-1}(T)=f^{-1}(U)$ si y sólo si $T\cap\operatorname{Im}(f)=U\cap\operatorname{Im}(f)$. Deduzca que todas las preimágenes distinguen subconjuntos distintos del codominio exactamente cuando $f$ es sobreyectiva.


**92.** **Nivel D. Preimágenes después de restringir.** Sea $f:A\to B$ y $S\subseteq A$. Demuestre que $(f|_S)^{-1}(T)=S\cap f^{-1}(T)$ para $T\subseteq B$. Use el resultado para $f(x)=x^2$, $A=B=\mathbb R$, $S=(-\infty,0)$ y $T=\{0,9\}$.


## P. Hipótesis y cancelación en composiciones


**93.** **Nivel F. El criterio exacto para evitar colisiones al componer.** Pruebe que $g\circ f:A\to C$ es inyectiva si y sólo si $f:A\to B$ es inyectiva y $g|_{f(A)}:f(A)\to C$ es inyectiva. Explique cómo permite construir ejemplos con $g$ no inyectiva en todo $B$.


**94.** **Nivel E. Alcanzar el codominio final.** Una función $g:B\to C$ es sobreyectiva. Para cada $c\in C$ escriba $G_c=\{b\in B:g(b)=c\}$. Pruebe que $g\circ f$ es sobreyectiva si y sólo si $f(A)$ corta cada $G_c$. Dé un ejemplo con dos puntos en cada $G_c$ donde $f$ alcance exactamente uno de cada par.


**95.** **Nivel F. Cancelar una función a la izquierda.** Sea $f:A\to B$. Demuestre que es inyectiva si y sólo si, para todo conjunto $X$ y todas las funciones $u,v:X\to A$, la igualdad $f\circ u=f\circ v$ implica $u=v$. Para probar necesidad, encuentre un conjunto de prueba pequeño.


**96.** **Nivel F. Cancelar una función a la derecha.** Pruebe que $f:A\to B$ es sobreyectiva si y sólo si, para todas $u,v:B\to\{0,1\}$, la igualdad $u\circ f=v\circ f$ implica $u=v$. Construya explícitamente el contraejemplo cuando falta un valor en la imagen.


**97.** **Nivel E. Una hipótesis que recupera la inyectividad perdida.** Se sabe que $g\circ f$ es inyectiva y que $f$ es sobreyectiva. Demuestre que $g$ es inyectiva. Señale el paso que se vuelve imposible si se retira la sobreyectividad de $f$.


**98.** **Nivel E. Una hipótesis que recupera la cobertura intermedia.** Se sabe que $g\circ f$ es sobreyectiva y que $g$ es inyectiva. Demuestre que $f$ es sobreyectiva. ¿Dónde interviene la inyectividad de $g$?


## Q. Construcción y diagnóstico de inversas


**99.** **Nivel F. Todas las inversas izquierdas de una inclusión.** Sea $i:\{1,2\}\to\{1,2,3,4\}$, $i(x)=x$. Encuentre y cuente todas las $r:\{1,2,3,4\}\to\{1,2\}$ con $r\circ i=\operatorname{id}_{\{1,2\}}$. Determine si alguna cumple también $i\circ r=\operatorname{id}_{\{1,2,3,4\}}$.


**100.** **Nivel F. Todas las inversas derechas de una función finita.** Sea $p:\{1,2,3,4\}\to\{u,v\}$ con $p(1)=p(2)=u$, $p(3)=p(4)=v$. Determine todas las $s:\{u,v\}\to\{1,2,3,4\}$ que cumplen $p\circ s=\operatorname{id}_{\{u,v\}}$. ¿Alguna es inversa bilateral?


**101.** **Nivel F. La excepción del dominio vacío.** Sea $f:\varnothing\to B$ la función vacía. Determine para qué $B$ existe una inversa izquierda $r:B\to\varnothing$ y para qué $B$ existe una inversa bilateral. Explique por qué «toda función inyectiva tiene inversa izquierda» requiere controlar este caso.


**102.** **Nivel F. Construir una inversa por casos y controlar los extremos.** Defina $f:\mathbb R\to(-\infty,-1)\cup[1,\infty)$ por $f(x)=x-1$ si $x<0$ y $f(x)=x+1$ si $x\ge0$. Construya su inversa justificando existencia, unicidad, dominios y ambas composiciones. Explique por qué $-1$ está excluido del codominio y $1$ no.


**103.** **Nivel F. Una función que se deshace a sí misma.** Determine todas las funciones $f:\{1,2,3\}\to\{1,2,3\}$ tales que $f\circ f=\operatorname{id}$ y exactamente una entrada cumple $f(x)=x$. Justifique que no faltan posibilidades y que cada función encontrada es su propia inversa.


**104.** **Nivel G. Diagnosticar una cancelación indebida.** Sea $f:A\to A$ con $f\circ f=f$. Un estudiante cancela $f$ y concluye $f=\operatorname{id}_A$. Determine cuándo la conclusión es válida: pruebe que una función con esa ecuación es invertible si y sólo si es la identidad. Dé un contraejemplo no invertible sobre tres elementos y pruebe que, en cualquier caso, $f$ actúa como identidad sobre su imagen.

# Soluciones razonadas
***
## A. De relaciones a funciones
***
### 1
***
Sí. Cada elemento de $A$ aparece exactamente una vez como primera componente. Por tanto existe una única salida en $B$ para cada entrada.


### 2
***
No es función: la entrada $1$ tiene dos salidas distintas, $a$ y $b$. Falla unicidad, aunque sí hay al menos una salida para cada elemento del dominio.


### 3
***
No. La entrada $3$ no tiene salida. Falla totalidad.


### 4
***
Si $A=\varnothing$, la condición universal «para todo $a\in A$ existe una única salida» es vacíamente verdadera. Si $A\ne\varnothing$, cualquier $a\in A$ carece de salida, así que falla totalidad.


### 5
***
$R$ es función si y sólo si $\forall a\in A\,\exists b\in B\big((a,b)\in R\land\forall c\in B((a,c)\in R\Rightarrow c=b)\big)$. La existencia y la unicidad aparecen por separado.


### 6
***
Si $m>0$, cada una de las $m$ entradas puede elegir independientemente una de las $n$ salidas. Para $n>0$, la regla del producto da $n^m$ funciones. Si $n=0$ y $m>0$, no hay funciones, lo que coincide con $0^m=0$.

Si $m=0$, existe exactamente una función: la función vacía, incluso cuando $n=0$. Para $n>0$ esto coincide con $n^0=1$. El caso en que ambos conjuntos son vacíos se cuenta directamente; no requiere asignar un valor aritmético a $0^0$.

## B. Dominio, codominio, imagen y evaluación
***
### 7
***
Dominio: $\{1,2,3\}$. Codominio: $\{a,b,c,d\}$. Imagen: $\{a,c\}$. En particular, imagen y codominio no coinciden.


### 8
***
$f(0)=1$ y $f(-2)=5$. Como $x^2\ge0$, la imagen es $[1,\infty)$, y todo $y\ge1$ se obtiene tomando $x=\sqrt{y-1}$.


### 9
***
$f=\{(1,2),(2,4),(3,6)\}$. Esta escritura muestra explícitamente a la función como relación.


### 10
***
Tienen el mismo valor para cada entrada real, pero codominios distintos. Bajo la convención estructural del capítulo son funciones distintas. Además, $g$ es sobreyectiva y $f$ no.


### 11
***
Si $y\in\operatorname{Im}(f)$, existe $x\in A$ con $y=f(x)$. Como los valores de una función $A\to B$ pertenecen a $B$, se tiene $y\in B$. Por inclusión, $\operatorname{Im}(f)\subseteq B$.


### 12
***
Por ejemplo, $f:\mathbb R\to\mathbb R$ definida por $f(x)=x$ si $x\ge0$ y $f(x)=-x$ si $x<0$. Es una función por casos; estructuralmente sigue asignando una única salida a cada entrada.

## C. Imágenes y preimágenes de subconjuntos
***
### 13
***
$f(\{1,3,4\})=\{a,b,c\}$. La repetición de valores no produce multiplicidades en un conjunto.


### 14
***
Las entradas cuyos valores están en $\{a,c\}$ son $1,2,4$. Por tanto $f^{-1}(\{a,c\})=\{1,2,4\}$.


### 15
***
Si $y\in f(S\cup T)$, entonces $y=f(x)$ para algún $x\in S\cup T$; así $x\in S$ o $x\in T$, y $y\in f(S)\cup f(T)$. La recíproca se obtiene invirtiendo el argumento.


### 16
***
Si $y=f(x)$ con $x\in S\cap T$, entonces $x$ pertenece a ambos conjuntos, luego $y\in f(S)$ y $y\in f(T)$. Para $f(x)=x^2$, $S=\{-1\}$, $T=\{1\}$, el lado izquierdo es vacío y el derecho es $\{1\}$.


### 17
***
$x\in f^{-1}(U\cup V)$ equivale a $f(x)\in U\cup V$, es decir, $f(x)\in U$ o $f(x)\in V$. Esto equivale a $x\in f^{-1}(U)\cup f^{-1}(V)$.


### 18
***
$x\in f^{-1}(B\setminus U)$ iff $f(x)\in B\setminus U$ iff $f(x)\notin U$ iff $x\notin f^{-1}(U)$. Como $x$ está en el dominio $A$, esto es $x\in A\setminus f^{-1}(U)$.

## D. Igualdad, restricciones y cambio de codominio
***
### 19
***
Para todo $x\in\mathbb R$, $(x+1)^2=x^2+2x+1$. Tienen mismo dominio y codominio y coinciden punto a punto; por tanto son la misma función.


### 20
***
La restricción es $f|_{[0,\infty)}:[0,\infty)\to\mathbb R$, con la misma regla $x\mapsto x^2$. Cambia el dominio, no los valores admitidos en las entradas conservadas.


### 21
***
Sí, porque para todo $x\ge0$ se tiene $x^2\ge0$. El nuevo codominio contiene toda la imagen. Esta recodificación será además biyectiva.


### 22
***
Porque para $x=1$ se obtiene $h(1)=1\notin(-\infty,0]$. La regla no produce valores en el codominio declarado.


### 23
***
Ambos conjuntos consisten exactamente en los valores $f(x)$ obtenidos con $x\in S$. La restricción cambia el dominio a $S$, por lo que su imagen es la imagen directa de $S$ bajo $f$.


### 24
***
El codominio es parte del tipo de la función. La misma colección de pares puede verse como una asignación hacia distintos codominios permitidos, pero propiedades como sobreyectividad cambian. Por ello se conservan como objetos tipados distintos.

## E. Inyectividad
***
### 25
***
Sí. Si $2x_1-3=2x_2-3$, entonces $2x_1=2x_2$ y $x_1=x_2$.


### 26
***
No. $f(1)=1=f(-1)$ con $1\ne-1$. Una sola colisión entre entradas distintas basta.


### 27
***
Si $i(s_1)=i(s_2)$, entonces $s_1=s_2$ porque $i(s)=s$. Por definición, $i$ es inyectiva.


### 28
***
La inclusión $\subseteq$ vale siempre. Si $y\in f(S)\cap f(T)$, existen $s\in S,t\in T$ con $f(s)=y=f(t)$. Inyectividad implica $s=t$, así que ese elemento está en $S\cap T$ y $y\in f(S\cap T)$.


### 29
***
Supón $f(a)=f(b)$. Toma $S=\{a\}$ y $T=\{b\}$. Si $a\ne b$, entonces $S\cap T=\varnothing$, pero $f(a)$ pertenece a $f(S)\cap f(T)$, contradiciendo la igualdad. Luego $a=b$.


### 30
***
Siempre $S\subseteq f^{-1}(f(S))$. Si $f$ es inyectiva y $x$ está en el lado derecho, existe $s\in S$ con $f(x)=f(s)$, luego $x=s\in S$. Recíprocamente, aplica la igualdad a $S=\{a\}$: si $f(x)=f(a)$, entonces $x\in f^{-1}(f(\{a\}))=\{a\}$.

## F. Sobreyectividad
***
### 31
***
Sí. Dado $y\in\mathbb R$, toma $x=\sqrt[3]{y}$. Entonces $f(x)=y$.


### 32
***
No. Ningún real se envía a $-1$, pues $x^2\ge0$.


### 33
***
Dado $y\ge0$, toma $x=\sqrt y$ (también serviría $-\sqrt y$). Entonces $g(x)=y$.


### 34
***
Siempre $f(f^{-1}(T))\subseteq T$. Si $f$ es sobreyectiva y $y\in T$, existe $x$ con $f(x)=y$, por lo que $x\in f^{-1}(T)$ y $y$ está en la imagen. Recíprocamente, toma $T=B$: la igualdad da $f(A)=B$.


### 35
***
$f$ no es sobreyectiva, porque la definición exige una preimagen en $A$ para todo elemento de $B$.


### 36
***
Una función asigna a cada una de las $|A|$ entradas un solo valor, de modo que su imagen tiene a lo sumo $|A|$ elementos. Si $|A|<|B|$, la imagen no puede ser todo $B$.

## G. Biyectividad
***
### 37
***
Es inyectiva porque $3x_1+2=3x_2+2$ implica $x_1=x_2$. Es sobreyectiva porque dado $y$, $x=(y-2)/3$ satisface $f(x)=y$.


### 38
***
Es inyectiva en $[0,\infty)$ y sobreyectiva hacia $[0,\infty)$ porque cada $y\ge0$ tiene preimagen única $\sqrt y$.


### 39
***
La inyectividad produce $|A|$ valores distintos en $B$. Como $|A|=|B|$, esos valores agotan $B$. Así $\operatorname{Im}(f)=B$.


### 40
***
La sobreyectividad exige que los $|B|=|A|$ elementos de $B$ aparezcan como valores de las $|A|$ entradas. Si hubiera una colisión, quedarían menos de $|B|$ valores distintos, contradicción.


### 41
***
La sobreyectividad da existencia. Si $f(a_1)=b=f(a_2)$, la inyectividad da $a_1=a_2$. Por tanto existe una única preimagen.


### 42
***
Por ejemplo $1\mapsto a,2\mapsto b,3\mapsto c,4\mapsto d$. Cada elemento del codominio aparece exactamente una vez: por ello hay ausencia de colisiones (inyectividad) y cobertura total (sobreyectividad).

## H. Composición
***
### 43
***
$f(3)=4$ y luego $g(4)=8$. Por tanto $(g\circ f)(3)=8$.


### 44
***
$(g\circ f)(x)=2(x+1)=2x+2$, mientras $(f\circ g)(x)=2x+1$. No coinciden.


### 45
***
Basta que $f(A)\subseteq C$. Una condición más fuerte y habitual es $B=C$. Así cada valor producido por $f$ es una entrada permitida para $g$.


### 46
***
$g\circ f=\{(1,0),(2,0),(3,1)\}$. Se sustituye cada salida de $f$ en $g$.


### 47
***
Si $g(f(x_1))=g(f(x_2))$, la inyectividad de $g$ da $f(x_1)=f(x_2)$ y la de $f$ da $x_1=x_2$.


### 48
***
Dado $c$ en el codominio de $g$, sobreyectividad de $g$ da $b$ con $g(b)=c$. Sobreyectividad de $f$ da $a$ con $f(a)=b$. Entonces $(g\circ f)(a)=c$.


### 49
***
Si $f(x_1)=f(x_2)$, al aplicar $g$ se obtiene $(g\circ f)(x_1)=(g\circ f)(x_2)$. La inyectividad de la composición fuerza $x_1=x_2$.


### 50
***
Dado $c$ en el codominio de $g$, la sobreyectividad de $g\circ f$ da $a$ con $g(f(a))=c$. Tomando $b=f(a)$, existe una preimagen de $c$ bajo $g$.

## I. Identidad y asociatividad
***
### 51
***
$\operatorname{id}=\{(1,1),(2,2),(3,3)\}$.


### 52
***
Para todo $a\in A$, $(f\circ\operatorname{id}_A)(a)=f(\operatorname{id}_A(a))=f(a)$. Luego las funciones coinciden punto a punto.


### 53
***
Para todo $a\in A$, $(\operatorname{id}_B\circ f)(a)=\operatorname{id}_B(f(a))=f(a)$.


### 54
***
Para todo $a$, el lado izquierdo vale $h((g\circ f)(a))=h(g(f(a)))$ y el derecho vale $(h\circ g)(f(a))=h(g(f(a)))$.


### 55
***
En $\mathbb R$, toma $f(x)=x+1$ y $g(x)=x^2$. Entonces $(g\circ f)(x)=(x+1)^2$ y $(f\circ g)(x)=x^2+1$, que por ejemplo difieren en $x=1$.


### 56
***
Si $f(x_1)=f(x_2)$, aplicar $g$ produce $g(f(x_1))=g(f(x_2))$, es decir $x_1=x_2$. Así $f$ es inyectiva.

## J. Inversas
***
### 57
***
Si $y=2x+5$, entonces $x=(y-5)/2$. Por tanto $f^{-1}(y)=(y-5)/2$. La función es biyectiva y las composiciones dan la identidad.


### 58
***
$f^{-1}(y)=\sqrt y$. La restricción del dominio elimina la segunda raíz y garantiza unicidad.


### 59
***
No es inyectiva ($f(1)=f(-1)$) ni sobreyectiva hacia $\mathbb R$ (no alcanza negativos). Por tanto no puede tener inversa bilateral.


### 60
***
$g=g\circ\operatorname{id}_B=g\circ(f\circ h)=(g\circ f)\circ h=\operatorname{id}_A\circ h=h$. Se usó asociatividad.


### 61
***
Si $g=f^{-1}$ y $f(x_1)=f(x_2)$, aplicar $g$ da $x_1=g(f(x_1))=g(f(x_2))=x_2$.


### 62
***
Dado $b\in B$, toma $a=f^{-1}(b)$. Entonces $f(a)=f(f^{-1}(b))=b$.


### 63
***
La sobreyectividad garantiza que para cada $b$ existe al menos un $a$. La inyectividad garantiza que ese $a$ es único. Por tanto cada entrada $b$ recibe exactamente una salida.


### 64
***
Si es invertible, los dos ejercicios anteriores dan inyectividad y sobreyectividad. Si es biyectiva, el ejercicio anterior construye $f^{-1}$, y por definición se verifican $f^{-1}\circ f=\operatorname{id}_A$ y $f\circ f^{-1}=\operatorname{id}_B$.

## K. Preimagen frente a inversa
***
### 65
***
$f^{-1}(\{4\})=\{-2,2\}$. Es una preimagen de conjunto, no una función inversa; $f$ no es biyectiva.


### 66
***
$f^{-1}([0,9])=[-3,3]$, porque $0\le x^2\le9$ equivale a $|x|\le3$.


### 67
***
Coinciden como conjuntos: $\{a:f(a)\in T\}=\{f^{-1}(b):b\in T\}$. La notación es compatible, aunque conceptualmente se llega por dos rutas distintas.


### 68
***
Para $f(x)=2x$ en $\mathbb R$, $f^{-1}(x)=x/2$, mientras $1/f(x)=1/(2x)$ cuando $x\ne0$. Son objetos distintos.

## L. Síntesis y transferencia
***
### 69
***
La biyectividad implica que $g\circ f$ es inyectiva y sobreyectiva. Por los teoremas de composición, $f$ debe ser inyectiva y $g$ debe ser sobreyectiva. No se sigue, en general, que $f$ sea sobreyectiva ni que $g$ sea inyectiva.


### 70
***
Toma $A=\{1\}$, $B=\{a,b\}$, $C=\{x\}$. Define $f(1)=a$ y $g(a)=g(b)=x$. La composición es la única función $\{1\}\to\{x\}$, por tanto biyectiva. $f$ no alcanza $b$ y $g$ identifica $a,b$.


### 71
***
Primera parte: $f(x_1)=f(x_2)$ implica $g(f(x_1))=g(f(x_2))$, luego $x_1=x_2$. Segunda: dado $b\in B$, toma $a=h(b)$; entonces $f(a)=f(h(b))=b$.


### 72
***
La composición de inyectivas es inyectiva y la de sobreyectivas es sobreyectiva, luego es biyectiva. La fórmula correcta es $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$, porque para deshacer primero se deshace $g$ y después $f$.

## M. Problemas avanzados tipo prueba
***
### 73
***
**(i)$\Rightarrow$(ii).** La inclusión $f(S\cap T)\subseteq f(S)\cap f(T)$ siempre vale. Si $y$ pertenece al lado derecho, existen $s\in S,t\in T$ con $f(s)=y=f(t)$. Inyectividad da $s=t$, por lo que $s\in S\cap T$ y $y\in f(S\cap T)$.

**(ii)$\Rightarrow$(iii).** Siempre $S\subseteq f^{-1}(f(S))$. Para la inclusión inversa, sea $x\in f^{-1}(f(S))$. Existe $s\in S$ con $f(x)=f(s)$, así que $f(x)\in f(\{x\})\cap f(S)$. Por (ii), ese valor está en $f(\{x\}\cap S)$, de modo que $\{x\}\cap S$ no es vacío. Por tanto $x\in S$. Concluimos $f^{-1}(f(S))=S$.

**(iii)$\Rightarrow$(i).** Si $f(a)=f(b)$, entonces $b\in f^{-1}(f(\{a\}))=\{a\}$, por lo que $b=a$.

Así las tres condiciones son equivalentes.


### 74
***
**(a)** $y\in(g\circ f)(S)$ iff existe $s\in S$ con $y=g(f(s))$. Esto equivale a que existe $b\in f(S)$ con $y=g(b)$, es decir $y\in g(f(S))$.

**(b)** Para $x\in A$:
$$
x\in(g\circ f)^{-1}(U)
\iff g(f(x))\in U
\iff f(x)\in g^{-1}(U)
\iff x\in f^{-1}(g^{-1}(U)).
$$
Por extensionalidad, los conjuntos son iguales.

**(c)** Los símbolos $f^{-1}(V)$ y $g^{-1}(U)$ de (b) significan preimágenes de subconjuntos. Toda función posee preimágenes; no se está afirmando que existan funciones inversas.


### 75
***
**(a)** Ya que la composición es inyectiva, $f(x_1)=f(x_2)$ implica $(g\circ f)(x_1)=(g\circ f)(x_2)$ y entonces $x_1=x_2$.

**(b)** Dado $c\in C$, la sobreyectividad de la composición da $a\in A$ con $g(f(a))=c$. Así $c$ tiene preimagen $f(a)$ bajo $g$.

**(c) y (d)** Usa $A=\{1\}$, $B=\{a,b\}$, $C=\{x\}$, $f(1)=a$, $g(a)=g(b)=x$. La composición es biyectiva, pero $f$ no alcanza $b$ y $g$ no es inyectiva.

**(e)** Basta añadir cualquiera de las dos hipótesis siguientes, cada una por separado:

- Si $f$ es sobreyectiva, ya sabemos que es inyectiva, por lo que es biyectiva. Para probar que $g$ es inyectiva, supongamos $g(b_1)=g(b_2)$ y elijamos $a_1,a_2$ con $f(a_i)=b_i$. La inyectividad de $g\circ f$ da $a_1=a_2$, luego $b_1=b_2$. Como $g$ ya era sobreyectiva, también es biyectiva.
- Si $g$ es inyectiva, ya sabemos que es sobreyectiva, por lo que es biyectiva. Para cualquier $b\in B$, la sobreyectividad de $g\circ f$ permite elegir $a$ con $g(f(a))=g(b)$. La inyectividad de $g$ da $f(a)=b$, de modo que $f$ es sobreyectiva; como ya era inyectiva, también es biyectiva.

Así, en cada alternativa se concluye la biyectividad de ambas funciones. Otra condición suficiente es que los tres conjuntos sean finitos y tengan la misma cardinalidad: las propiedades ya demostradas de $f$ y $g$ se completan mediante los ejercicios 39–40.


### 76
***
(a) Toma $A=\{1,2\}$, $B=\{a,b\}$, $C=\{x\}$, $f(1)=a,f(2)=b$ (inyectiva) y $g(a)=g(b)=x$. La composición colapsa ambas entradas.

(b) Toma $A=\{1\}$, $B=\{a,b\}$, $C=\{x,y\}$, $f(1)=a$ y $g(a)=x,g(b)=y$ (sobreyectiva). La composición sólo alcanza $x$ porque $f$ nunca llega a $b$.

(c) Toma $A=\{1\}$, $B=\{a,b\}$, $C=\{x\}$, $f(1)=a$ y $g(a)=g(b)=x$. La composición desde un singleton es inyectiva, aunque $g$ no lo sea: la parte conflictiva $b$ nunca es visitada.

(d) Usa el mismo esquema con $C=\{x\}$: la composición es sobreyectiva hacia $C$, pero $f$ no alcanza $b$. La composición sólo necesita cubrir el codominio final, no todo el conjunto intermedio.


### 77
***
**Invertible $\Rightarrow$ biyectiva.** Supón que existe $g:B\to A$ con $g\circ f=\operatorname{id}_A$ y $f\circ g=\operatorname{id}_B$.

Inyectividad: si $f(x_1)=f(x_2)$, aplicar $g$ produce
$$
x_1=g(f(x_1))=g(f(x_2))=x_2.
$$

Sobreyectividad: dado $b\in B$, toma $a=g(b)$. Entonces
$$
f(a)=f(g(b))=b.
$$

**Biyectiva $\Rightarrow$ invertible.** Dado $b\in B$, sobreyectividad garantiza al menos un $a\in A$ con $f(a)=b$. Inyectividad garantiza que no puede haber dos. Por ello podemos definir una función $g:B\to A$ enviando cada $b$ a su única preimagen $a$.

Para $a\in A$, $g(f(a))=a$ por unicidad de la preimagen de $f(a)$, así $g\circ f=\operatorname{id}_A$. Para $b\in B$, si $g(b)=a$, la definición da $f(a)=b$, luego $f\circ g=\operatorname{id}_B$.

Así $g=f^{-1}$ y el criterio queda demostrado.


### 78
***
De $g\circ f=\operatorname{id}_A$ se deduce que $f$ es inyectiva: si $f(x_1)=f(x_2)$, aplicar $g$ da $x_1=x_2$.

De $f\circ h=\operatorname{id}_B$ se deduce que $f$ es sobreyectiva: dado $b\in B$, $b=f(h(b))$.

Por tanto $f$ es biyectiva y posee una única inversa bilateral.

Podemos identificar directamente $g$ y $h$:
$$
g
=g\circ\operatorname{id}_B
=g\circ(f\circ h)
=(g\circ f)\circ h
=\operatorname{id}_A\circ h
=h.
$$
Sea $k=g=h$. Ya tenemos $k\circ f=\operatorname{id}_A$ y $f\circ k=\operatorname{id}_B$, así que $k=f^{-1}$. Por tanto $g=h=f^{-1}$.


### 79
***
Los tipos son
$$
g\circ f:A\to C,\qquad g^{-1}:C\to B,\qquad f^{-1}:B\to A,
$$
de modo que $f^{-1}\circ g^{-1}:C\to A$ tiene exactamente el tipo que debe tener la inversa de $g\circ f$.

Verificamos:
$$
\begin{aligned}
(f^{-1}\circ g^{-1})\circ(g\circ f)
&=f^{-1}\circ(g^{-1}\circ g)\circ f\\
&=f^{-1}\circ\operatorname{id}_B\circ f\\
&=f^{-1}\circ f\\
&=\operatorname{id}_A.
\end{aligned}
$$
Asimismo,
$$
\begin{aligned}
(g\circ f)\circ(f^{-1}\circ g^{-1})
&=g\circ(f\circ f^{-1})\circ g^{-1}\\
&=g\circ\operatorname{id}_B\circ g^{-1}\\
&=g\circ g^{-1}\\
&=\operatorname{id}_C.
\end{aligned}
$$
Por unicidad de la inversa, $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$. El orden se invierte porque para deshacer la composición primero debe deshacerse la última función aplicada.


### 80
***
**(a)** La composición biyectiva es inyectiva y sobreyectiva. Por tanto $f$ es inyectiva y $g$ es sobreyectiva.

**(b)** No. Como $|A|=4<6=|B|$, ninguna función $A\to B$ puede ser sobreyectiva.

**(c)** No. Una función $B\to C$ con $6>4$ no puede ser inyectiva.

**(d)** Como $f$ es inyectiva, $f(A)$ tiene 4 elementos. La composición identifica $A$ biyectivamente con $C$. Por ello $g|_{f(A)}:f(A)\to C$ debe ser biyectiva: es sobreyectiva porque $g(f(A))=C$, e inyectiva porque si dos puntos de $f(A)$ tuvieran la misma imagen, sus preimágenes únicas bajo $f$ producirían una colisión en $g\circ f$.

**(e)** Toma
$$
A=\{1,2,3,4\},\quad
B=\{a,b,c,d,e,f\},\quad
C=\{w,x,y,z\}.
$$
Define $f(1)=a,f(2)=b,f(3)=c,f(4)=d$. Define
$$
g(a)=w,\ g(b)=x,\ g(c)=y,\ g(d)=z,
$$
y, por ejemplo, $g(e)=w,g(f)=x$. Entonces $g\circ f$ es la biyección $1\mapsto w,2\mapsto x,3\mapsto y,4\mapsto z$, mientras $f$ no es sobreyectiva y $g$ no es inyectiva. Esto muestra exactamente cómo los defectos pueden quedar fuera de la parte de $B$ visitada por $f$.



***
## N. Construir composiciones con datos prescritos


### 81

Las ecuaciones de composición obligan a $g(a)=0$, $g(b)=1$ y $g(c)=1$. No imponen nada sobre $d$, porque $d\notin f(A)$. Hay exactamente dos funciones, según $g(d)=0$ o $g(d)=1$. Cada una satisface las cuatro ecuaciones. No hay más posibilidades: todo punto visitado tiene valor forzado y el único punto restante admite exactamente dos salidas.


### 82

Para $1$ y $2$, la salida de $f$ debe estar en $\{b,c\}$; para $3$ debe ser $a$. Hay cuatro funciones: las dos primeras salidas son $(b,b)$, $(b,c)$, $(c,b)$ o $(c,c)$, y la tercera siempre es $a$. Exactamente dos son inyectivas, las que usan $(b,c)$ o $(c,b)$. El valor de $h$ determina una preimagen bajo $g$, no necesariamente una elección única dentro de ella.


### 83

Si $h=g\circ f$, entradas con el mismo valor de $f$ tienen el mismo valor de $h$ al aplicar $g$. Recíprocamente, dado $b\in B$, la sobreyectividad de $f$ permite tomar un $x$ con $f(x)=b$ y proponer $g(b)=h(x)$. Otra elección $y$ cumple $f(y)=b=f(x)$, luego $h(y)=h(x)$: la salida propuesta no depende de la elección. Existe así una única salida para cada $b$, y $g(f(x))=h(x)$. Cualquier otra función que realice la composición debe tener ese valor en cada $b$, porque todo $b$ es alcanzado. Si $B$ es vacío, también $A$ es vacío y la asignación vacía verifica el mismo argumento. La señal decisiva es que $f$ pierde la distinción entre ciertas entradas: $h$ debe perder al menos esas mismas distinciones.


### 84

Se exige $x-1\ne0$, por lo que $S=\mathbb R\setminus\{1\}$. La restricción de $f$ a $S$, con codominio reducido a $\mathbb R\setminus\{0\}$, da $\widetilde f:S\to\mathbb R\setminus\{0\}$, $\widetilde f(x)=x-1$. Ahora $g\circ\widetilde f:S\to\mathbb R$ es una composición total y vale $1/(x-1)$. Toda entrada de $S$ cumple la condición; cualquier conjunto mayor incluiría $1$, cuya salida intermedia es inadmisible. La fórmula sola no elimina la necesidad de declarar la restricción.


### 85

$g\circ f:\mathbb R\to\mathbb R$ vale $\sqrt{x^2}=|x|$. $f\circ g:[0,\infty)\to[0,\infty)$ vale $(\sqrt y)^2=y$, así que es $\operatorname{id}_{[0,\infty)}$. La otra composición no es $\operatorname{id}_{\mathbb R}$: en $x=-1$ da $1$. $g$ elige una raíz no negativa, pero no recupera una entrada negativa original. Es inversa derecha de $f$, no bilateral. La raíz cuadrada de un cuadrado no es siempre la entrada original.


### 86

La identidad obliga a que $f(1)\ne f(2)$; de otro modo $g$ tendría que asignar dos valores distintos a la misma entrada. Hay $3\cdot2=6$ elecciones ordenadas para esas salidas. Fijado $f$, los valores de $g$ sobre ellas quedan forzados a $1$ y $2$, y el punto restante de $B$ puede enviarse a cualquiera de los dos: dos elecciones. En total hay $12$ pares. Ningún $g$ es inyectivo, pues el tercer punto repite uno de los dos valores ya utilizados. Los pares no se duplican porque sus primeras funciones o su valor libre de $g$ son distintos.


## O. Imágenes, preimágenes y cambios de conjuntos


### 87

$f(S)=\{a,b\}$ y $f^{-1}(T)=\{1,2\}$: $d$ no es alcanzado. La nueva función es $q:S\to\{a,b\}$, $q(2)=a$, $q(3)=b$, y es biyectiva por sus dos valores distintos que cubren el codominio. Para comparar preimágenes hay que usar un subconjunto de ambos codominios: $q^{-1}(\{a\})=\{2\}$, mientras $f^{-1}(\{a\})=\{1,2\}$. La restricción eliminó la entrada $1$. No debe escribirse una preimagen de $\{a,d\}$ bajo la definición de $q$ para subconjuntos de su codominio, pues $d$ ya no pertenece a éste.


### 88

La preimagen del vacío es vacía. El valor $-2$ es imposible; $x^2+1=1$ da $x=0$, y $x^2+1=5$ da $x=\pm2$. Por tanto la segunda preimagen es $\{-2,0,2\}$, donde $-2$ ahora es una entrada, no el valor imposible del codominio. La condición $1<x^2+1\le5$ equivale a $0<x^2\le4$, así que la tercera preimagen es $[-2,0)\cup(0,2]$. En la restricción, los resultados son $\varnothing$, $\{0,2\}$ y $(0,2]$: sólo se conservan entradas no negativas. Quitar un valor inalcanzable del conjunto objetivo no cambia su preimagen; quitar entradas del dominio sí puede hacerlo.


### 89

Cada $s\in S$ tiene su valor en $f(S)$, luego pertenece a $K(S)$. Además $f(K(S))=f(S)$: un punto de $K(S)$ tiene por definición el mismo valor que algún punto de $S$, y la inclusión $S\subseteq K(S)$ da la inclusión opuesta de imágenes. Tomando preimágenes resulta $K(K(S))=K(S)$. La igualdad $K(S)=S$ significa que, cada vez que $S$ contiene una entrada, contiene todas las entradas con el mismo valor. Equivalentemente, $S$ es unión de conjuntos completos $F_b$: si hay igualdad, $S=\bigcup_{b\in f(S)}F_b$; si $S$ es una unión de tales conjuntos, todo punto de $K(S)$ comparte valor con uno de $S$ y pertenece al mismo conjunto completo. Incluye $S=\varnothing$, unión vacía. Este criterio no exige inyectividad de $f$.


### 90

Si $y=f(x)$ con $x\in f^{-1}(T)$, entonces $y\in T$ y $y\in\operatorname{Im}(f)$. A la inversa, si $y$ está en esa intersección, existe $x\in A$ con $f(x)=y$; como $y\in T$, ese $x$ pertenece a $f^{-1}(T)$. Así se prueban ambas inclusiones. En el ejemplo, para $T=\varnothing$ o $\{v\}$ el resultado es vacío; para $T=\{u\}$ o $\{u,v\}$ es $\{u\}$. La imagen posterior recupera los valores alcanzados de $T$, no los valores que nunca tuvieron preimagen.


### 91

Si las preimágenes coinciden, sus imágenes también, y el ejercicio 90 da la igualdad de intersecciones. Si las intersecciones coinciden, para cada $x\in A$ el valor $f(x)$ pertenece a la imagen; por tanto $f(x)\in T$ equivale a $f(x)\in U$, lo que da la igualdad de preimágenes. Si $f$ es sobreyectiva, la imagen es $B$ y el criterio obliga a $T=U$. Si no lo es, existe $b\in B\setminus\operatorname{Im}(f)$; los conjuntos distintos $\varnothing$ y $\{b\}$ tienen ambos preimagen vacía. Así queda demostrada la necesidad y la suficiencia.


### 92

Pertenecer a la preimagen bajo la restricción significa ser una entrada $x\in S$ cuyo valor $f(x)$ está en $T$. Es exactamente la pertenencia simultánea a $S$ y a $f^{-1}(T)$. En el ejemplo, la preimagen original es $\{-3,0,3\}$; su intersección con $(-\infty,0)$ es $\{-3\}$. Se elimina $0$ por la desigualdad estricta del nuevo dominio y $3$ por ser positivo. No cambia la regla de evaluación, sino las entradas admitidas.


## P. Hipótesis y cancelación en composiciones


### 93

Si la composición es inyectiva, de $f(x)=f(y)$ se obtiene igualdad de valores compuestos, luego $x=y$. Para dos puntos $b_1=f(x)$, $b_2=f(y)$ de $f(A)$ con $g(b_1)=g(b_2)$, la misma inyectividad da $x=y$ y por tanto $b_1=b_2$. Esto prueba inyectividad de la restricción. Recíprocamente, una igualdad $g(f(x))=g(f(y))$ se cancela primero mediante la inyectividad de esa restricción, pues ambos valores intermedios están en $f(A)$; luego la inyectividad de $f$ da $x=y$. Se puede añadir a $B$ un punto fuera de $f(A)$ con la misma salida que uno visitado: se pierde inyectividad global de $g$, pero no de la composición. El criterio explica el papel de la restricción sin suponer que $f$ sea sobreyectiva.


### 94

La composición alcanza $c$ si y sólo si existe $a\in A$ con $g(f(a))=c$, es decir, si existe un punto $f(a)\in f(A)\cap G_c$. Exigirlo para todo $c$ es exactamente sobreyectividad. Tome $A=\{1,2\}$, $B=\{u,v,w,z\}$, $C=\{0,1\}$, con $g(u)=g(v)=0$, $g(w)=g(z)=1$, $f(1)=u$, $f(2)=w$. La composición cubre $C$, aunque $f$ no alcance $v,z$. No hace falta visitar cada punto intermedio, sino al menos uno de cada conjunto que lleva al mismo valor final.


### 95

Si $f$ es inyectiva, la igualdad compuesta da $f(u(x))=f(v(x))$ para cada $x\in X$ y entonces $u(x)=v(x)$; los tipos coinciden y las funciones son iguales. Si $f$ no es inyectiva, existen $a\ne a'$ con $f(a)=f(a')$. Tome $X=\{*\}$, $u(*)=a$ y $v(*)=a'$. Las composiciones coinciden, pero $u\ne v$. Por contraposición se demuestra necesidad. El conjunto de una entrada basta para detectar una colisión. Para $A=\varnothing$, la dirección suficiente sigue válida; no existe una colisión que invalide la propiedad.


### 96

Si $f$ es sobreyectiva, para cada $b\in B$ hay $a$ con $f(a)=b$; la igualdad compuesta da $u(b)=u(f(a))=v(f(a))=v(b)$. Si no es sobreyectiva, elija $b_0\notin f(A)$. Defina $u(b)=0$ para todo $b$ y $v(b)=1$ cuando $b=b_0$, $v(b)=0$ en otro caso. Difieren en $b_0$, pero las composiciones nunca visitan ese punto y ambas valen $0$. No se cancela la función por apariencia simbólica: la sobreyectividad garantiza que las evaluaciones compuestas prueban todos los puntos de $B$.


### 97

Sean $b_1,b_2\in B$ con $g(b_1)=g(b_2)$. Como $f$ es sobreyectiva, existen $a_1,a_2\in A$ con $f(a_i)=b_i$. La igualdad es ahora $(g\circ f)(a_1)=(g\circ f)(a_2)$, por lo que $a_1=a_2$ y $b_1=b_2$. Sin sobreyectividad puede haber un $b_i$ sin preimagen y no se puede trasladar la colisión a las entradas de la composición. El ejemplo de la nota de [§9.12](algebra-para-matematicos-capitulo-9-funciones-composicion-e-inversas.md#apm-c09-s12) muestra esa posibilidad.


### 98

Tome un $b\in B$ arbitrario. El punto $g(b)$ pertenece a $C$ y por sobreyectividad de la composición existe $a\in A$ con $g(f(a))=g(b)$. La inyectividad de $g$ permite concluir $f(a)=b$, proporcionando la preimagen requerida. Sin ella, $f(a)$ podría ser un punto distinto con el mismo valor final. Por ejemplo, en el ejercicio 94 la composición es sobreyectiva pero $f$ no lo es, porque $g$ identifica cada par intermedio.


## Q. Construcción y diagnóstico de inversas


### 99

La primera identidad exige $r(1)=1$ y $r(2)=2$. Las salidas de $3$ y $4$ son independientes y pueden ser $1$ o $2$; hay cuatro funciones, con pares de salidas $(1,1)$, $(1,2)$, $(2,1)$ o $(2,2)$ para esas entradas. Ninguna satisface la segunda identidad: $i(r(3))$ es $1$ o $2$, nunca $3$. Una inversa izquierda puede ser no única y no convertirse en bilateral. Los puntos fuera de la imagen de $i$ explican la libertad restante.


### 100

$s(u)$ debe ser $1$ o $2$ y $s(v)$ debe ser $3$ o $4$. Resultan cuatro funciones, cuyas salidas ordenadas son $(1,3)$, $(1,4)$, $(2,3)$ y $(2,4)$. Para cualquier elección, las evaluaciones de $p\circ s$ recuperan $u,v$. No existe inversa bilateral: como $p(1)=p(2)$, la función $s\circ p$ tiene el mismo valor en $1$ y $2$ y no puede ser la identidad. Elegir una entrada por valor permite volver al codominio, pero no recuperar todas las entradas originales.


### 101

$f$ es inyectiva vacíamente para cualquier $B$. Si $B\ne\varnothing$, no existe función $B\to\varnothing$: una entrada de $B$ no puede recibir salida. Por tanto no hay inversa izquierda ni bilateral. Si $B=\varnothing$, la única función $r$ es vacía y ambas composiciones son la identidad vacía. Así las dos clases de inversa existen exactamente para $B=\varnothing$. El ejemplo basta para refutar la afirmación sin condiciones. No se está demostrando aquí un resultado general de existencia de inversas laterales en conjuntos arbitrarios.


### 102

La rama negativa produce exactamente $(-\infty,-1)$; la no negativa produce $[1,\infty)$. Para $y<-1$, la única entrada posible es $x=y+1<0$; para $y\ge1$, es $x=y-1\ge0$. Las imágenes de las ramas son disjuntas, así que no hay una segunda entrada en la otra rama. Definimos $g$ en el codominio declarado por $g(y)=y+1$ si $y<-1$ y $g(y)=y-1$ si $y\ge1$. Para $x<0$, $g(f(x))=(x-1)+1=x$; para $x\ge0$, vale $(x+1)-1=x$. Para $y<-1$, $f(g(y))=(y+1)-1=y$; para $y\ge1$, vale $(y-1)+1=y$. $-1$ exigiría $x=0$ en la rama negativa, donde esa entrada no está admitida; $1$ se obtiene con $x=0$ en la otra rama. El despeje debe conservar la condición de cada caso.


### 103

Si $f(x)=f(y)$, aplicar $f$ da $x=y$, así que es inyectiva. Además cada $x$ es imagen de $f(x)$, luego es sobreyectiva. Si $a$ es el único punto fijo, los otros dos $b,c$ deben intercambiarse: $f(b)$ no puede ser $b$; tampoco $a$, porque la inyectividad y $f(a)=a$ lo impiden. Por tanto $f(b)=c$ y la identidad impone $f(c)=b$. Hay tres posibilidades, según el punto fijo sea $1$, $2$ o $3$. En cada una el intercambio aplicado dos veces devuelve las entradas, y el punto fijo permanece; ambas identidades de inversa son la misma ecuación $f\circ f=\operatorname{id}$. No se requiere una teoría previa de permutaciones.


### 104

Si $f$ es invertible, componer a la izquierda con $f^{-1}$ da $(f^{-1}\circ f)\circ f=f^{-1}\circ f$, es decir $f=\operatorname{id}_A$. A la inversa, la identidad es invertible y satisface la ecuación. Sin invertibilidad no se puede hacer esa cancelación. En $A=\{1,2,3\}$, defina $f(1)=1$, $f(2)=1$, $f(3)=3$. Evaluar por segunda vez no cambia ningún valor, pero hay una colisión y $f$ no es la identidad. Finalmente, si $y\in f(A)$, existe $x$ con $y=f(x)$ y entonces $f(y)=f(f(x))=f(x)=y$. La restricción, con codominio reducido a $f(A)$, es $\operatorname{id}_{f(A)}$. La ecuación controla los valores ya alcanzados; no obliga a que cada entrada sea uno de ellos.

***

[← Capítulo 8](algebra-para-matematicos-capitulo-8-relaciones-y-relaciones-de-equivalencia.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 10 →](algebra-para-matematicos-capitulo-10-como-se-demuestra.md)

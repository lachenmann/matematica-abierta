---
{
  "title": "Relaciones y relaciones de equivalencia",
  "description": "Capítulo 8 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0183",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C08",
  "editorial-id": "MA-BCH-APM-01-008",
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
    "MA-BCH-0018"
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

En C7 apareció el producto cartesiano $A\times B$: el conjunto de todos los pares ordenados $(a,b)$ con $a\in A$ y $b\in B$. Ese objeto permite ahora dar un paso decisivo. En lugar de estudiar únicamente los elementos de un conjunto, podemos estudiar **qué pares de elementos satisfacen cierta condición**.

La idea de relación está presente en toda la matemática: “ser menor que”, “tener la misma longitud”, “estar conectado con”, “tener el mismo valor absoluto”, “pertenecer a la misma clase”. Pero una relación matemática no será una intuición vaga de semejanza. Será un objeto perfectamente determinado.

> **Una relación es un conjunto de pares ordenados.**

A partir de esta definición, propiedades como reflexividad, simetría o transitividad se convierten en afirmaciones cuantificadas sobre esos pares. Y un caso especialmente importante —las relaciones de equivalencia— permitirá organizar un conjunto en bloques disjuntos llamados **clases de equivalencia**.

***
## 8.1. Del producto cartesiano a una relación {#apm-c08-s01}

Sean $A$ y $B$ conjuntos. Una **relación binaria de $A$ en $B$** es cualquier subconjunto de $A\times B$:

$$
R\subseteq A\times B.
$$

Si $(a,b)\in R$, podemos escribir también

$aRb$.

La relación **es** el conjunto $R$. La frase verbal que la describe es sólo una manera de reconocer cuáles pares pertenecen a ese conjunto.

### Ejemplo

Sean $A=\{1,2,3\}$ y $B=\{a,b\}$. El conjunto

$$
R=\{(1,a),(2,a),(3,b)\}
$$

es una relación de $A$ en $B$ porque todos sus pares pertenecen a $A\times B$.

En cambio,

$$
S=\{(1,a),(4,b)\}
$$

no es una relación de $A$ en $B$, porque $(4,b)\notin A\times B$.

### Cuántas relaciones hay

Como una relación es un subconjunto de $A\times B$, el conjunto de todas las relaciones de $A$ en $B$ es $\mathcal P(A\times B)$. Si $A$ y $B$ son finitos, con $|A|=m$ y $|B|=n$, entonces hay

$$
2^{mn}
$$

relaciones posibles de $A$ en $B$.

***
## 8.2. Relaciones sobre un conjunto {#apm-c08-s02}

Cuando $A=B$, diremos que $R$ es una **relación sobre $A$**:

$$
R\subseteq A\times A.
$$

Éste será el contexto natural para propiedades como reflexividad, simetría, antisimetría y transitividad.

Por ejemplo, sobre $A=\{1,2,3\}$ podemos considerar la relación

$$
R=\{(1,1),(1,2),(2,2),(2,3),(3,3)\}.
$$

También podemos definir relaciones mediante condiciones. Sobre $\mathbb R$:

$$
xRy\quad\Longleftrightarrow\quad x\le y.
$$

Aunque la condición use símbolos conocidos, la relación sigue siendo el conjunto de todos los pares $(x,y)$ que la satisfacen.

***
## 8.3. Dominio e imagen de una relación {#apm-c08-s03}

Si $R\subseteq A\times B$, llamamos **dominio** de $R$ al conjunto de primeras componentes que aparecen en algún par de $R$:

$$
\operatorname{Dom}(R)=\{a\in A:\exists b\in B\;(a,b)\in R\}.
$$

La **imagen** de $R$ es el conjunto de segundas componentes que aparecen:

$$
\operatorname{Im}(R)=\{b\in B:\exists a\in A\;(a,b)\in R\}.
$$

Si

$$
R=\{(1,a),(1,b),(3,b)\}\subseteq\{1,2,3\}\times\{a,b,c\},
$$

entonces

$$
\operatorname{Dom}(R)=\{1,3\},\qquad \operatorname{Im}(R)=\{a,b\}.
$$

Obsérvese que el dominio de la relación no tiene por qué ser todo $A$, ni su imagen todo $B$.

***
## 8.4. Representar relaciones finitas {#apm-c08-s04}

Una relación finita puede representarse de varias maneras.

### Lista de pares

La forma más directa es escribir explícitamente $R$.

### Matriz $0$–$1$

Si $A=\{a_1,\dots,a_m\}$ y $B=\{b_1,\dots,b_n\}$, podemos formar una tabla donde la entrada $(i,j)$ vale $1$ si $(a_i,b_j)\in R$ y $0$ si no.

Por ejemplo, para

$$
R=\{(1,a),(2,b),(2,c)\}
$$

con filas $1,2$ y columnas $a,b,c$, la matriz es

$$
\begin{pmatrix}
1&0&0\\
0&1&1
\end{pmatrix}.
$$

### Diagrama dirigido

Cuando $R$ es una relación sobre un conjunto finito, podemos representar cada elemento como un vértice y dibujar una flecha $a\to b$ cuando $aRb$. Un par $(a,a)$ aparece como un lazo.

Estas representaciones ayudan a inspeccionar propiedades, pero las propiedades se deciden por la definición, no por la apariencia del dibujo.

***
## 8.5. La relación inversa {#apm-c08-s05}

Si $R\subseteq A\times B$, definimos su **relación inversa** por

$$
R^{-1}=\{(b,a):(a,b)\in R\}.
$$

Simplemente invertimos el orden de cada par.

Si

$$
R=\{(1,a),(2,a),(3,b)\},
$$

entonces

$$
R^{-1}=\{(a,1),(a,2),(b,3)\}.
$$

Se cumplen dos observaciones inmediatas:

$$
(R^{-1})^{-1}=R,
$$

$$
\operatorname{Dom}(R^{-1})=\operatorname{Im}(R),\qquad
\operatorname{Im}(R^{-1})=\operatorname{Dom}(R).
$$

No debemos confundir todavía esta construcción con una función inversa. Toda relación tiene relación inversa, mientras que una función no siempre tiene función inversa.

***
## 8.6. Reflexividad e irreflexividad {#apm-c08-s06}

Sea $R$ una relación sobre $A$.

Decimos que $R$ es **reflexiva** si todo elemento está relacionado consigo mismo:

$$
\forall a\in A\; aRa.
$$

Decimos que es **irreflexiva** si ningún elemento está relacionado consigo mismo:

$$
\forall a\in A\; \neg(aRa).
$$

La distinción lógica es importante. Una relación puede ser **no reflexiva** sin ser irreflexiva.

Por ejemplo, sobre $A=\{1,2,3\}$,

$$
R=\{(1,1),(2,2)\}
$$

no es reflexiva porque falta $(3,3)$, pero tampoco es irreflexiva porque contiene pares diagonales.

***
## 8.7. Simetría, antisimetría y asimetría {#apm-c08-s07}

Sea $R$ una relación sobre $A$.

### Simetría

$R$ es **simétrica** si

$$
aRb\Rightarrow bRa.
$$

Cada flecha debe venir acompañada por su flecha inversa.

### Antisimetría

$R$ es **antisimétrica** si

$$
aRb\land bRa\Rightarrow a=b.
$$

La antisimetría **no** dice que nunca pueda ocurrir simultáneamente $aRb$ y $bRa$; dice que, si ocurre, necesariamente $a=b$.

Por eso la igualdad es a la vez simétrica y antisimétrica.

### Asimetría

$R$ es **asimétrica** si

$$
aRb\Rightarrow \neg(bRa).
$$

La asimetría sí prohíbe completamente los pares inversos, incluso cuando $a=b$. Por tanto, toda relación asimétrica es irreflexiva.

### Un error que debe desaparecer

“Antisimétrica” no significa “no simétrica”. Una relación puede no ser simétrica y tampoco ser antisimétrica. Las dos propiedades imponen condiciones lógicas distintas sobre todos los pares de elementos.

***
### Propiedades que pueden coexistir

Las palabras «simétrica», «antisimétrica» y «asimétrica» no forman una lista de alternativas excluyentes. Sobre $A=\{1,2\}$, compare estas relaciones:

| Relación | Simétrica | Antisimétrica | Asimétrica |
|---|---|---|---|
| $\varnothing$ | Sí | Sí | Sí |
| $\{(1,1),(2,2)\}$ | Sí | Sí | No |
| $\{(1,2)\}$ | No | Sí | Sí |
| $\{(1,2),(2,1)\}$ | Sí | No | No |

Cada «sí» debe leerse con su cuantificador. En la relación vacía no hay un par que pueda refutar ninguna de las tres condiciones. En la identidad hay pares en ambos sentidos únicamente cuando las componentes coinciden, lo que permite antisimetría; los lazos impiden asimetría. El último ejemplo tiene dos flechas opuestas entre elementos distintos, así que contradice tanto antisimetría como asimetría.

**Para comprobarlo.** ¿Puede una relación sobre un conjunto no vacío ser reflexiva y asimétrica a la vez?

**Solución.** No. Si $a\in A$, la reflexividad exige $aRa$. La asimetría aplicada a ese mismo par exige $\neg(aRa)$. La incompatibilidad utiliza que podemos elegir un elemento. Sobre $A=\varnothing$, ambas condiciones universales se cumplen y la única relación es vacía.

***
## 8.8. Transitividad {#apm-c08-s08}

Una relación $R$ sobre $A$ es **transitiva** si

$$
aRb\land bRc\Rightarrow aRc.
$$

Para refutar transitividad debemos encontrar una cadena concreta

$$
aRb,\qquad bRc
$$

para la cual falte $aRc$.

Por ejemplo, en $A=\{1,2,3\}$, la relación

$$
R=\{(1,2),(2,3)\}
$$

no es transitiva porque $(1,2)$ y $(2,3)$ pertenecen a $R$, pero $(1,3)$ no.

En cambio, la relación $<$ sobre $\mathbb R$ es transitiva: si $a<b$ y $b<c$, entonces $a<c$.

***
## 8.9. Diagnosticar una relación {#apm-c08-s09}

Clasificar una relación exige tratar cada propiedad por separado.

Para una relación finita conviene seguir este orden:

1. revisar todos los pares diagonales para reflexividad o irreflexividad;
2. revisar pares inversos para simetría, antisimetría y asimetría;
3. revisar cadenas de longitud dos para transitividad.

Una matriz o un diagrama puede ayudar:

- reflexividad corresponde a unos en toda la diagonal;
- simetría corresponde a simetría respecto de la diagonal principal;
- antisimetría prohíbe unos simultáneos en posiciones $(i,j)$ y $(j,i)$ cuando $i\ne j$.

Pero la transitividad no se decide por una simple condición visual local: debemos comprobar cierres de cadenas.

***
## 8.10. Relaciones de equivalencia {#apm-c08-s10}

Una relación $R$ sobre $A$ es una **relación de equivalencia** si es:

- reflexiva;
- simétrica;
- transitiva.

Las tres propiedades cumplen papeles distintos.

La reflexividad asegura que cada objeto sea equivalente a sí mismo. La simetría elimina una dirección privilegiada. La transitividad garantiza coherencia: si $a$ es equivalente a $b$ y $b$ a $c$, entonces $a$ debe ser equivalente a $c$.

### Ejemplo: mismo valor absoluto

Sobre $\mathbb Z$, definamos

$$
x\sim y\quad\Longleftrightarrow\quad |x|=|y|.
$$

Es reflexiva porque $|x|=|x|$, simétrica porque la igualdad es simétrica y transitiva porque la igualdad es transitiva. Por tanto, es una equivalencia.

***
## 8.11. Clases de equivalencia {#apm-c08-s11}

Sea $R$ una relación de equivalencia sobre $A$. Para $a\in A$, definimos la **clase de equivalencia de $a$** por

$$
[a]=\{x\in A:xRa\}.
$$

Como $R$ es reflexiva, siempre

$$
a\in[a].
$$

Para la relación “tener el mismo valor absoluto” sobre $\mathbb Z$:

$$
[0]=\{0\},
$$

y si $a\ne0$,

$$
[a]=\{a,-a\}.
$$

La clase no es un nuevo símbolo para el elemento $a$. Es un **subconjunto de $A$**.

***
## 8.12. Cuándo dos clases son iguales {#apm-c08-s12}

En una relación de equivalencia ocurre un fenómeno fundamental:

$$
aRb\quad\Longleftrightarrow\quad[a]=[b].
$$

### Por qué

Si $aRb$ y $x\in[a]$, entonces $xRa$. Como $aRb$, la transitividad produce $xRb$, así que $x\in[b]$. Esto prueba $[a]\subseteq[b]$. El argumento recíproco usa simetría y da $[b]\subseteq[a]$.

En sentido contrario, si $[a]=[b]$, como $a\in[a]$, también $a\in[b]$, de donde $aRb$.

### Iguales o disjuntas

Si dos clases comparten un elemento, entonces son iguales. En consecuencia,

$$
[a]=[b]\quad\text{o}\quad[a]\cap[b]=\varnothing.
$$

No existen dos clases de equivalencia distintas que se superpongan parcialmente.

***
### Leer la prueba por sus obligaciones

La igualdad $[a]=[b]$ exige dos inclusiones. Si sabemos $aRb$, la primera comienza con un **elemento arbitrario** $x\in[a]$: no basta verificar que el representante $a$ pertenece a ambas clases. La definición entrega $xRa$ y la transitividad permite unir $xRa$ con $aRb$ para obtener $xRb$. Para la otra inclusión debemos invertir primero $aRb$ mediante simetría: si $x\in[b]$, entonces $xRb$ y $bRa$ permiten concluir $xRa$.

La dirección $[a]=[b]\Rightarrow aRb$ utiliza otra propiedad: reflexividad asegura $a\in[a]$. Al transportar esa pertenencia a $[b]$, la definición de clase produce la conclusión. Las tres propiedades de equivalencia hacen trabajos distintos.

También podemos justificar por qué compartir un elemento obliga a compartir toda la clase. Si $z\in[a]\cap[b]$, tenemos $zRa$ y $zRb$. Por simetría, $aRz$; por transitividad, $aRb$. La igualdad de clases ya demostrada termina el argumento.

**Para reconstruirlo.** Oculte las líneas anteriores y escriba qué dato permite pasar de $zRa$ a $aRz$, y por qué no basta encontrar una intersección no vacía cuando la relación no es una equivalencia.

**Solución.** El cambio de dirección usa simetría. Sin transitividad, la relación sobre $\{1,2,3\}$ con todos los pares diagonales y flechas $1\leftrightarrow2\leftrightarrow3$, pero sin $1\leftrightarrow3$, tiene conjuntos asociados $C_1=\{1,2\}$ y $C_3=\{2,3\}$ que se solapan sin ser iguales. No podemos unir $1R2$ con $2R3$ para concluir $1R3$.

***
## 8.13. De una equivalencia a una partición {#apm-c08-s13}

Una **partición** de un conjunto $A$ es una colección de subconjuntos que cumplen:

1. cada bloque es no vacío;
2. bloques distintos son disjuntos;
3. la unión de todos los bloques es $A$.

Las clases de equivalencia de una relación de equivalencia forman una partición de $A$.

Cada elemento pertenece a su propia clase, de modo que las clases cubren $A$. Y acabamos de demostrar que dos clases son iguales o disjuntas.

Así, una equivalencia no sólo compara objetos: **clasifica** el conjunto completo.

***
## 8.14. De una partición a una equivalencia {#apm-c08-s14}

El proceso también funciona al revés.

Sea $\Pi$ una partición de $A$. Definamos

$$
a\sim b\quad\Longleftrightarrow\quad a\text{ y }b\text{ pertenecen al mismo bloque de }\Pi.
$$

Esta relación es reflexiva porque cada elemento pertenece a algún bloque; simétrica porque “estar en el mismo bloque” no depende del orden; y transitiva porque los bloques de una partición son disjuntos: si $a$ y $b$ están en un bloque, y $b$ y $c$ en otro, ambos bloques contienen a $b$ y por tanto deben ser el mismo.

Así obtenemos la correspondencia estructural:

```text
RELACIÓN DE EQUIVALENCIA  ↔  PARTICIÓN
```

***
### Ir y volver recupera el mismo objeto

La correspondencia exige más que poder construir una partición a partir de una relación y una relación a partir de una partición. Debemos comprobar que cada viaje de ida y vuelta recupera el punto de partida.

Si comenzamos con una equivalencia $R$, formamos sus clases y relacionamos después los elementos que estén en el mismo bloque. Los elementos $a,b$ comparten bloque exactamente cuando $[a]=[b]$, y [§8.12](algebra-para-matematicos-capitulo-8-relaciones-y-relaciones-de-equivalencia.md#apm-c08-s12) identifica esa condición con $aRb$. Recuperamos, por tanto, el mismo conjunto de pares $R$.

Si comenzamos con una partición $\Pi$, definimos la relación «estar en el mismo bloque». Sea $C\in\Pi$ y elijamos $a\in C$; podemos hacerlo porque un bloque es no vacío. La clase de $a$ es exactamente $C$: los elementos de $C$ están relacionados con $a$, y ningún elemento fuera de $C$ puede compartir con $a$ otro bloque, por disjunción. Recuperamos todos los bloques originales.

**Caso frontera.** ¿Qué partición corresponde a la equivalencia sobre el conjunto vacío?

**Solución.** La colección vacía de bloques. Su unión es vacía y las condiciones sobre bloques se cumplen. La colección $\{\varnothing\}$ no es una partición bajo nuestra definición porque contiene un bloque vacío. La relación sobre el conjunto vacío también es vacía; no hay representantes ni clases que añadir.

***
## 8.15. El conjunto cociente {#apm-c08-s15}

Si $R$ es una relación de equivalencia sobre $A$, el **conjunto cociente** es el conjunto de todas las clases de equivalencia:

$$
A/R=\{[a]:a\in A\}.
$$

Si $A=\{1,2,3,4\}$ y las clases son $\{1,3\}$ y $\{2,4\}$, entonces

$$
A/R=\big\{\{1,3\},\{2,4\}\big\}.
$$

Los elementos de $A/R$ son conjuntos. Ésta es una distinción de tipo importante:

- $1\in A$;
- $[1]=\{1,3\}\in A/R$;
- pero $1\notin A/R$.

Los cocientes algebraicos aparecerán mucho más adelante. Aquí sólo necesitamos la idea de reemplazar objetos por sus clases.

***
### Representante, clase y conjunto de clases

En el ejemplo anterior, $1$ es un elemento del conjunto original, $[1]=\{1,3\}$ es un subconjunto de ese conjunto y $A/R$ es una colección de esos subconjuntos. Por eso son correctas tres escrituras de tipos distintos: $1\in A$, $[1]\subseteq A$ y $[1]\in A/R$.

Podemos escoger $3$ en vez de $1$ para nombrar el mismo bloque: $[3]=[1]$. La clase conserva todos sus elementos; cambiar el representante no reemplaza el bloque por el número elegido. Una lista de representantes $\{1,2\}$ y el cociente $\{\{1,3\},\{2,4\}\}$ tampoco son el mismo conjunto.

**Para comprobarlo.** En esta partición, decida si $\{1\}$ es una clase y si $\{1,3\}$ pertenece al cociente. Justifique por qué $1\in[1]$ y $[1]\in A/R$ no permiten escribir $1\in A/R$.

**Solución.** $\{1\}$ no es una clase: la clase que contiene a $1$ también contiene a $3$. El bloque $\{1,3\}$ sí pertenece al cociente. La pertenencia no es transitiva: las dos pertenencias encadenadas sólo dicen que $1$ está dentro de uno de los elementos de $A/R$. Los elementos del cociente en este ejemplo son los dos bloques, no los números de sus interiores.

***
## 8.16. Umbral de funciones {#apm-c08-s16}

Una relación general puede relacionar una misma entrada con varias salidas, con una sola o con ninguna.

Por ejemplo,

$$
R=\{(1,a),(1,b),(2,b)\}
$$

relaciona $1$ con dos elementos diferentes.

Otra relación,

$$
S=\{(1,a),(2,b),(3,b)\},
$$

asigna a cada elemento de $\{1,2,3\}$ exactamente una segunda componente.

Esta observación abre la pregunta del próximo capítulo:

> **¿Qué condiciones debe satisfacer una relación para convertirse en una función?**

C8 termina aquí. Las funciones, su composición y sus inversas son el objeto de C9.
***
# Ejercicios

## A. Relación como subconjunto y notación

**1.** **Nivel A.** Sean $A=\{1,2\}$ y $B=\{a,b\}$. Escribe $A\times B$ y decide si $R=\{(1,a),(2,b)\}$ es una relación de $A$ en $B$.

**2.** **Nivel A.** Con $A=\{1,2,3\}$, describe por extensión la relación $R$ sobre $A$ definida por $xRy\Longleftrightarrow x<y$.

**3.** **Nivel A.** Si $R=\{(1,a),(3,b)\}$, reescribe sus dos pertenencias usando la notación infija $xRy$.

**4.** **Nivel B.** Explica por qué la relación vacía $\varnothing$ es una relación de $A$ en $B$ para cualesquiera conjuntos $A$ y $B$.

**5.** **Nivel B.** Explica por qué $A\times B$ es siempre una relación de $A$ en $B$. ¿Qué relación verbal representa si no imponemos ninguna condición adicional?

**6.** **Nivel C.** Si $|A|=2$ y $|B|=3$, ¿cuántas relaciones distintas de $A$ en $B$ existen? Justifica a partir del conjunto potencia.

## B. Dominio, imagen y representaciones

**7.** **Nivel A.** Para $R=\{(1,a),(1,c),(3,c)\}\subseteq\{1,2,3\}\times\{a,b,c\}$, calcula $\operatorname{Dom}(R)$ e $\operatorname{Im}(R)$.

**8.** **Nivel B.** Calcula dominio e imagen de la relación vacía $R=\varnothing\subseteq A\times B$.

**9.** **Nivel B.** Para $A=\{1,2,3\}$ y $R=\{(1,1),(1,3),(2,2),(3,1)\}$, construye la matriz $0$–$1$ usando ese orden de filas y columnas.

**10.** **Nivel B.** La matriz de una relación sobre $A=\{1,2,3\}$ es $\begin{pmatrix}1&0&1\\0&1&0\\1&0&0\end{pmatrix}$. Escribe la relación como conjunto de pares.

**11.** **Nivel B.** Describe mediante una lista de flechas el diagrama dirigido de $R=\{(1,1),(1,2),(2,3),(3,2)\}$ sobre $A=\{1,2,3\}$. Identifica los lazos.

**12.** **Nivel C.** Sobre $A=\{1,2,3,4\}$, define $xRy$ si y sólo si $x$ e $y$ tienen la misma paridad. Escribe $R$ como conjunto de pares.

**13.** **Nivel C.** Explica cómo se reconocen $\operatorname{Dom}(R)$ e $\operatorname{Im}(R)$ directamente en la matriz $0$–$1$ de una relación de $A$ en $B$.

**14.** **Nivel C.** Sea $R\subseteq A\times B$ una relación finita cuya matriz tiene exactamente cinco entradas iguales a $1$. ¿Cuántos pares tiene $R$? Justifica.

## C. Relación inversa

**15.** **Nivel A.** Calcula $R^{-1}$ para $R=\{(1,a),(2,a),(3,b)\}$.

**16.** **Nivel B.** Demuestra directamente a partir de la definición que $(R^{-1})^{-1}=R$.

**17.** **Nivel B.** Demuestra que $\operatorname{Dom}(R^{-1})=\operatorname{Im}(R)$ y $\operatorname{Im}(R^{-1})=\operatorname{Dom}(R)$.

**18.** **Nivel C.** Prueba que una relación $R$ sobre $A$ es simétrica si y sólo si $R=R^{-1}$.

## D. Reflexividad e irreflexividad

**19.** **Nivel A.** Sobre $A=\{1,2,3\}$, decide si $R=\{(1,1),(2,2),(3,3),(1,2)\}$ es reflexiva.

**20.** **Nivel A.** Si $A$ es no vacío, clasifica la relación vacía sobre $A$ respecto de reflexividad e irreflexividad.

**21.** **Nivel B.** Clasifica la relación identidad $I_A=\{(a,a):a\in A\}$ respecto de reflexividad e irreflexividad cuando $A$ es no vacío.

**22.** **Nivel B.** Da un ejemplo sobre $A=\{1,2,3\}$ de una relación que no sea reflexiva ni irreflexiva.

**23.** **Nivel B.** Sobre $\mathbb R$, analiza la relación $xRy\Longleftrightarrow x\le y$ respecto de reflexividad e irreflexividad.

**24.** **Nivel B.** Sobre $\mathbb R$, analiza $xRy\Longleftrightarrow x<y$ respecto de reflexividad e irreflexividad.

## E. Simetría, antisimetría y asimetría

**25.** **Nivel B.** Analiza la relación de igualdad sobre un conjunto $A$ respecto de simetría y antisimetría.

**26.** **Nivel B.** Sea $A$ un conjunto con al menos dos elementos. Analiza la relación universal $A\times A$ respecto de simetría y antisimetría.

**27.** **Nivel B.** Demuestra que $<$ sobre $\mathbb R$ es asimétrica.

**28.** **Nivel B.** Demuestra que $\le$ sobre $\mathbb R$ es antisimétrica pero no simétrica.

**29.** **Nivel C.** Sobre $\mathbb Z$, sea $xRy\Longleftrightarrow |x|=|y|$. Decide si $R$ es simétrica y si es antisimétrica.

**30.** **Nivel C.** Construye una relación sobre $A=\{1,2,3\}$ que sea simultáneamente simétrica y antisimétrica y que no sea vacía.

**31.** **Nivel C.** Da un ejemplo de una relación sobre $A=\{1,2,3\}$ que no sea simétrica ni antisimétrica.

**32.** **Nivel C.** Da un ejemplo de una relación antisimétrica que no sea asimétrica y explica qué propiedad del ejemplo impide que sea asimétrica.

**33.** **Nivel D.** Demuestra que toda relación asimétrica es irreflexiva.

**34.** **Nivel D.** Demuestra que si una relación es simultáneamente simétrica y antisimétrica, entonces todos sus pares son diagonales: $R\subseteq I_A$.

## F. Transitividad

**35.** **Nivel B.** Decide si $R=\{(1,2),(2,3),(1,3)\}$ sobre $A=\{1,2,3\}$ es transitiva.

**36.** **Nivel B.** Decide si $R=\{(1,2),(2,3)\}$ sobre $A=\{1,2,3\}$ es transitiva y, si falla, entrega el contraejemplo exacto.

**37.** **Nivel B.** Demuestra que la relación identidad $I_A$ es transitiva.

**38.** **Nivel B.** Demuestra que la relación vacía es transitiva sobre cualquier conjunto $A$.

**39.** **Nivel C.** Demuestra que $<$ sobre $\mathbb R$ es transitiva.

**40.** **Nivel C.** Sobre $A=\{1,2,3\}$, considera $R=\{(1,2),(2,1)\}$. ¿Es transitiva? Justifica revisando las cadenas posibles.

**41.** **Nivel D.** Da dos relaciones transitivas $R,S$ sobre un mismo conjunto cuya unión $R\cup S$ no sea transitiva.

**42.** **Nivel D.** Demuestra que la intersección de dos relaciones transitivas sobre $A$ es transitiva.

## G. Clasificación combinada

**43.** **Nivel C.** Sea $A$ un conjunto no vacío. Clasifica completamente $I_A$ respecto de las propiedades: reflexiva, irreflexiva, simétrica, antisimétrica, asimétrica y transitiva.

**44.** **Nivel C.** Si $|A|\ge2$, clasifica completamente $A\times A$.

**45.** **Nivel C.** Clasifica completamente la relación $<$ sobre $\mathbb R$.

**46.** **Nivel C.** Clasifica completamente la relación $\le$ sobre $\mathbb R$.

**47.** **Nivel D.** Sobre $A=\{1,2,3\}$, clasifica $R=\{(1,1),(2,2),(3,3),(1,2),(2,1)\}$.

**48.** **Nivel D.** Sobre $A=\{1,2,3\}$, clasifica $R=\{(1,1),(2,2),(3,3),(1,2)\}$.

**49.** **Nivel D.** Sobre $\mathbb Z$, clasifica la relación $xRy\Longleftrightarrow |x|=|y|$.

**50.** **Nivel D.** Sobre $\mathbb Z$, sea $xRy\Longleftrightarrow x-y=1$. Clasifica la relación respecto de reflexividad, simetría, antisimetría, asimetría y transitividad.

## H. Relaciones de equivalencia

**51.** **Nivel C.** Sobre $\mathbb Z$, define $x\sim y$ cuando $x$ e $y$ tienen la misma paridad. Demuestra que $\sim$ es una relación de equivalencia.

**52.** **Nivel C.** Sobre $\mathbb Z$, define $x\sim y\Longleftrightarrow x^2=y^2$. Demuestra que es una relación de equivalencia.

**53.** **Nivel D.** Sobre $\mathbb R\setminus\{0\}$, define $x\sim y\Longleftrightarrow xy>0$. Demuestra que es una relación de equivalencia e interpreta sus clases.

**54.** **Nivel D.** Sobre $\mathbb R$, analiza $xRy\Longleftrightarrow x\ge y$. ¿Es una relación de equivalencia? Identifica exactamente qué propiedad falla.

**55.** **Nivel D.** Sobre $A=\{1,2,3,4\}$, decide si $R=\{(1,1),(2,2),(3,3),(4,4),(1,3),(3,1),(2,4),(4,2)\}$ es una relación de equivalencia.

**56.** **Nivel D.** En el conjunto de palabras finitas sobre un alfabeto fijo, define $u\sim v$ si $u$ y $v$ tienen la misma longitud. Demuestra que es una equivalencia.

## I. Clases de equivalencia

**57.** **Nivel C.** Para la equivalencia de misma paridad sobre $\mathbb Z$, describe todas las clases de equivalencia y el cociente.

**58.** **Nivel C.** Para $x\sim y\Longleftrightarrow x^2=y^2$ sobre $\mathbb Z$, calcula $[0]$, $[3]$ y $[-5]$.

**59.** **Nivel C.** Para la relación del ejercicio 55 sobre $A=\{1,2,3,4\}$, calcula $[1]$, $[2]$, $[3]$ y $[4]$.

**60.** **Nivel D.** Sea $R$ una equivalencia sobre $A$. Demuestra que si $aRb$, entonces $[a]=[b]$.

**61.** **Nivel D.** Sea $R$ una equivalencia. Demuestra que si $[a]\cap[b]\ne\varnothing$, entonces $[a]=[b]$.

**62.** **Nivel D.** Explica por qué, si $b\in[a]$, entonces $[b]=[a]$. Interpreta esta propiedad como independencia del representante.

## J. Particiones y cocientes

**63.** **Nivel C.** Sea $A=\{1,2,3,4,5\}$ y $\Pi=\{\{1,3,5\},\{2,4\}\}$. Construye la relación de equivalencia inducida por $\Pi$.

**64.** **Nivel C.** Decide si $\{\{1,2\},\{3\},\{4,5\}\}$ es una partición de $A=\{1,2,3,4,5\}$.

**65.** **Nivel C.** Explica por qué $\{\{1,2\},\{2,3\},\{4\}\}$ no es una partición de $\{1,2,3,4\}$.

**66.** **Nivel D.** Para la equivalencia del ejercicio 55, escribe explícitamente el conjunto cociente $A/R$.

**67.** **Nivel D.** Si $A/R=\{C_1,C_2,C_3\}$, explica qué tipo de objetos son $C_1,C_2,C_3$ y por qué un elemento $a\in A$ no tiene por qué pertenecer a $A/R$.

**68.** **Nivel E.** Demuestra las dos direcciones de la correspondencia: las clases de una equivalencia forman una partición y una partición induce una equivalencia mediante la pertenencia al mismo bloque.

## K. Transferencia y diagnóstico

**69.** **Nivel E.** Un estudiante afirma: «si una relación no es simétrica, entonces es antisimétrica». Refuta la afirmación construyendo una relación sobre un conjunto finito de cardinalidad mínima y explica por qué fallan tanto la simetría como la antisimetría.

**70.** **Nivel E.** Un estudiante encuentra $x\in[a]\cap[b]$ para una equivalencia y concluye que $[a]$ y $[b]$ se solapan parcialmente. Localiza el error y reconstruye la conclusión correcta.

**71.** **Nivel F.** Sobre $A=\{1,2,3,4,5,6\}$ se define una relación de equivalencia. Se sabe que $[1]=\{1,4\}$, $[2]=\{2,5,6\}$ y que $3$ no es equivalente a ningún otro elemento. Reconstruye todas las clases, el cociente y la relación como conjunto de pares.

**72.** **Nivel G.** Escribe una síntesis matemática de 10–14 líneas que explique por qué una relación de equivalencia puede entenderse como un mecanismo de clasificación. Debes conectar: relación como conjunto de pares, las tres propiedades, clases, igualdad/disjunción de clases, partición y conjunto cociente.

***
## L. Construcción de relaciones


**73.** **Nivel D. Construir y poner a prueba.** Sobre $A=\{1,2,3\}$, construya una relación simétrica e irreflexiva con exactamente cuatro pares. Decida si puede ser transitiva. Demuestre después que ninguna relación no vacía, simétrica e irreflexiva, sobre cualquier conjunto, es transitiva.


**74.** **Nivel D. Un contraejemplo del menor tamaño.** Construya una relación asimétrica que no sea transitiva sobre un conjunto del menor tamaño posible. Dé el triple que refuta transitividad y demuestre la minimalidad.


**75.** **Nivel E. Añadir lazos sin completar cadenas.** Construya una relación reflexiva y antisimétrica que no sea transitiva, también de tamaño mínimo. Explique por qué los lazos no refutan antisimetría y por qué no bastan dos elementos.


**76.** **Nivel D. Clasificación exhaustiva de dos propiedades.** Determine todas las relaciones sobre $A=\{u,v,w\}$ que son a la vez simétricas y antisimétricas. ¿Cuántas hay? Entre ellas, ¿cuáles son reflexivas, irreflexivas y transitivas?


**77.** **Nivel F. Una relación que depende de un parámetro.** Para $t\in\mathbb R$, defina sobre $\mathbb R$ la relación $xR_t y\Longleftrightarrow |x-y|\le t$. Clasifique reflexividad, irreflexividad, simetría, antisimetría, asimetría y transitividad para todos los valores de $t$.


**78.** **Nivel E. Cambiar el conjunto declarado.** Sobre $\mathbb R$, defina $xRy\Longleftrightarrow |x|\le|y|$. Clasifique reflexividad, simetría, antisimetría y transitividad. Repita la clasificación al restringir la relación a $[0,\infty)$ y explique qué cambió.


## M. Poner a prueba las hipótesis


**79.** **Nivel E. Clases que se solapan.** En $A=\{1,2,3\}$ tome $R=I_A\cup\{(1,2),(2,1),(2,3),(3,2)\}$. Forme $C_a=\{x\in A:xRa\}$ para cada $a$. ¿Estos conjuntos forman una partición? Señale qué hipótesis del teorema de clases falla y encuentre la menor relación de equivalencia que contiene a $R$.


**80.** **Nivel D. La inclusión que no puede invertirse.** En $A=\{1,2,3\}$ defina $aRb\Longleftrightarrow a\le b$. Calcule $C_a=\{x\in A:xRa\}$. Aunque $R$ es reflexiva y transitiva, ¿por qué no puede aplicarse el teorema $aRb\Rightarrow C_a=C_b$? Localice la inferencia que falla.


**81.** **Nivel E. Un elemento sin clase.** Sobre $A=\{1,2,3\}$ considere $R=\{1,2\}\times\{1,2\}$. Demuestre que es simétrica y transitiva. Calcule $C_3=\{x\in A:xR3\}$. ¿Por qué no hay una partición de todo $A$? Encuentre el subconjunto sobre el que sí es una equivalencia.


**82.** **Nivel F. Retirar un único lazo.** Sea $R$ una equivalencia sobre $A$ y sea $a\in A$. Forme $S=R\setminus\{(a,a)\}$. Determine qué ocurre con reflexividad y simetría. Demuestre que $S$ es transitiva si y sólo si la clase $[a]_R$ es unitaria.


**83.** **Nivel E. Restringir una clasificación.** Sea $R$ una equivalencia sobre $A$ y $B\subseteq A$. Defina $S=R\cap(B\times B)$. Pruebe que $S$ es una equivalencia sobre $B$ y que para $b\in B$ se cumple $[b]_S=B\cap[b]_R$. Describa la partición de $B$, incluyendo $B=\varnothing$.


**84.** **Nivel E. Unir dos equivalencias.** En $A=\{1,2,3\}$ sean $R$ y $S$ las equivalencias de las particiones $\{\{1,2\},\{3\}\}$ y $\{\{1\},\{2,3\}\}$. ¿Es $R\cup S$ una equivalencia? Construya la menor equivalencia que la contiene y demuestre que dos elementos no bastan para obtener un ejemplo de unión no transitiva de equivalencias.


## N. Reconstruir y contar clasificaciones


**85.** **Nivel F. Datos que no determinan una sola relación.** En $A=\{1,2,3,4,5,6\}$ se sabe que una equivalencia satisface $[1]=\{1,4\}$, $2R5$ y $3R6$. Determine todas las particiones posibles y el número de pares de cada relación. Justifique que no hay otras posibilidades.


**86.** **Nivel E. Reparar bloques superpuestos.** En $A=\{a,b,c,d\}$ se propone $\Pi=\{\{a,b\},\{b,c\},\{d\}\}$. Explique por qué falla como partición. Construya la menor equivalencia que relacione entre sí a todos los elementos de cada conjunto propuesto. ¿Su partición final coincide con $\Pi$?


**87.** **Nivel F. Contar sin ordenar los bloques.** En $A=\{1,2,3,4,5\}$ construya una equivalencia cuyas clases tengan tamaños $1,2,2$. ¿Cuántas equivalencias distintas cumplen esos tamaños? Cuente sin usar una fórmula combinatoria que no haya justificado.


**88.** **Nivel F. Satisfacer dos clasificaciones a la vez.** Sean $R,S$ equivalencias sobre $A$. Pruebe que $T=R\cap S$ es una equivalencia y que $[a]_T=[a]_R\cap[a]_S$. Para $A=\{1,2,3,4\}$, aplique el resultado a las particiones $\{\{1,2\},\{3,4\}\}$ y $\{\{1,3\},\{2,4\}\}$.


**89.** **Nivel D. La clasificación del conjunto vacío.** Determine todas las relaciones y todas las particiones sobre $A=\varnothing$. Explique por qué la única relación es a la vez reflexiva e irreflexiva, y por qué su cociente es $\varnothing$, no $\{\varnothing\}$.


**90.** **Nivel F. Lo que revela el número de pares.** Una equivalencia sobre un conjunto de cuatro elementos tiene exactamente dos clases y ocho pares. Determine los tamaños de las clases, cuántas relaciones cumplen los datos y si el número de pares identifica una única clasificación.


## O. Síntesis de relaciones y clases


**91.** **Nivel F. Clasificar pares por un dato común.** En $\mathbb R^2$, se agrupan los pares que tienen la misma suma de coordenadas. Justifique que cada par queda en exactamente un bloque y que dos bloques distintos son disjuntos. Describa los bloques de $(1,2)$, $(0,3)$ y $(0,0)$, y dé una descripción exhaustiva de todos los bloques.


**92.** **Nivel F. Identificar un par con su intercambio.** En $\mathbb R^2$ se decide que cada par $(a,b)$ comparta bloque con $(b,a)$, y que ninguna otra identificación sea necesaria. Construya los bloques, compruebe que forman una partición y determine cuándo uno de ellos tiene un solo elemento.


**93.** **Nivel G. Completar datos de clasificación.** En $A=\{1,2,3,4,5\}$ deben compartir bloque $1$ con $2$, $2$ con $3$, y $4$ con $5$. Construya la clasificación que realiza esas identificaciones sin añadir otras innecesarias. Dé sus bloques, el número de pares relacionados y una prueba de minimalidad por inclusión. Determine cómo cambian ambos resultados si se retira el dato sobre $2$ y $3$ antes de construirla.


**94.** **Nivel G. Dos criterios sobre palabras.** Se agrupan las palabras finitas sobre $\{a,b\}$ por tener la misma longitud y el mismo número de letras $a$. Justifique que el criterio produce bloques disjuntos que cubren todas las palabras y enumere el bloque de $aabb$. ¿Puede obtenerse otra clasificación coherente sustituyendo «y» por «o»? Justifique con pruebas o contraejemplos.


**95.** **Nivel F. Los nombres elegidos y los bloques.** Para la partición $\{\{1,2\},\{3,4\}\}$ de $A=\{1,2,3,4\}$, un estudiante escoge $T=\{1,3\}$ y afirma que $A/R=T$. Corrija la afirmación. Demuestre que cada $a\in A$ está relacionado con exactamente un elemento de $T$, y explique qué cambia al escoger $T'=\{2,4\}$.


**96.** **Nivel G. Comparar clasificaciones por sus bloques.** Sean $R,S$ equivalencias sobre un conjunto $A$. Un estudiante dice que $R$ hace todas las identificaciones que exige $S$ porque cada bloque de $R$ está contenido en algún bloque de $S$. Decida si su conclusión invierte la inclusión. Pruebe el criterio exacto entre inclusión de relaciones e inclusión de clases. Aplíquelo a $A=\{1,2,3,4,5\}$ con particiones $\{\{1,2\},\{3\},\{4,5\}\}$ para $R$ y $\{\{1,2,3\},\{4,5\}\}$ para $S$, y cuente los pares de ambas.

# Soluciones

## A. Relación como subconjunto y notación

### 1

$A\times B=\{(1,a),(1,b),(2,a),(2,b)\}$. Como los dos pares de $R$ pertenecen a ese producto, $R\subseteq A\times B$ y por tanto sí es una relación de $A$ en $B$.

### 2

Los pares con primera componente menor que la segunda son $R=\{(1,2),(1,3),(2,3)\}$.

### 3

Las pertenencias $(1,a)\in R$ y $(3,b)\in R$ se escriben $1Ra$ y $3Rb$.

### 4

Por definición una relación de $A$ en $B$ es cualquier subconjunto de $A\times B$. Como $\varnothing\subseteq A\times B$ para cualesquiera conjuntos $A$ y $B$, la relación vacía siempre es una relación.

### 5

Se tiene $A\times B\subseteq A\times B$, así que el producto completo es una relación. Representa la relación universal: todo elemento de $A$ está relacionado con todo elemento de $B$.

### 6

$|A\times B|=2\cdot3=6$. Una relación es un subconjunto de ese conjunto de seis pares, así que hay $|\mathcal P(A\times B)|=2^6=64$ relaciones.

## B. Dominio, imagen y representaciones

### 7

Las primeras componentes que aparecen son $1$ y $3$, de modo que $\operatorname{Dom}(R)=\{1,3\}$. Las segundas son $a$ y $c$, de modo que $\operatorname{Im}(R)=\{a,c\}$.

### 8

No aparece ninguna primera ni segunda componente. Por tanto $\operatorname{Dom}(R)=\varnothing$ e $\operatorname{Im}(R)=\varnothing$.

### 9

La matriz es $\begin{pmatrix}1&0&1\\0&1&0\\1&0&0\end{pmatrix}$: cada $1$ marca exactamente uno de los cuatro pares dados.

### 10

Los unos están en $(1,1)$, $(1,3)$, $(2,2)$ y $(3,1)$. Así $R=\{(1,1),(1,3),(2,2),(3,1)\}$.

### 11

Las flechas son $1\to1$, $1\to2$, $2\to3$ y $3\to2$. El único lazo es $1\to1$.

### 12

Los impares $1$ y $3$ se relacionan entre sí, y los pares $2$ y $4$ se relacionan entre sí. Por tanto $R=\{(1,1),(1,3),(3,1),(3,3),(2,2),(2,4),(4,2),(4,4)\}$.

### 13

Una fila pertenece al dominio exactamente cuando contiene al menos un $1$. Una columna pertenece a la imagen exactamente cuando contiene al menos un $1$.

### 14

Cada entrada $1$ corresponde a un único par de la relación y cada par produce un único $1$. Por tanto $|R|=5$.

## C. Relación inversa

### 15

Se invierte cada par: $R^{-1}=\{(a,1),(a,2),(b,3)\}$.

### 16

$(x,y)\in(R^{-1})^{-1}$ si y sólo si $(y,x)\in R^{-1}$, lo que ocurre si y sólo si $(x,y)\in R$. Por extensionalidad, $(R^{-1})^{-1}=R$.

### 17

$b\in\operatorname{Dom}(R^{-1})$ si y sólo si existe $a\in A$ tal que $(b,a)\in R^{-1}$; equivalentemente, existe $a\in A$ tal que $(a,b)\in R$, lo que significa que $b\in\operatorname{Im}(R)$. La segunda igualdad se prueba de la misma manera intercambiando componentes.

### 18

Si $R$ es simétrica y $(a,b)\in R$, entonces $(b,a)\in R$, luego $(a,b)\in R^{-1}$; así $R\subseteq R^{-1}$. El mismo argumento da la inclusión inversa. Recíprocamente, si $R=R^{-1}$ y $(a,b)\in R$, entonces $(b,a)\in R^{-1}=R$, por lo que $R$ es simétrica.

## D. Reflexividad e irreflexividad

### 19

Sí. Contiene $(1,1),(2,2),(3,3)$, todos los pares diagonales de $A$.

### 20

Es irreflexiva porque no contiene ningún $(a,a)$. Como $A$ es no vacío, no es reflexiva: falta al menos un par diagonal.

### 21

$I_A$ es reflexiva porque contiene $(a,a)$ para todo $a$. No es irreflexiva cuando $A$ es no vacío, precisamente porque contiene todos esos pares.

### 22

Por ejemplo $R=\{(1,1)\}$. No es reflexiva porque faltan $(2,2),(3,3)$ y no es irreflexiva porque contiene $(1,1)$.

### 23

Es reflexiva porque $x\le x$ para todo real $x$. No es irreflexiva.

### 24

Es irreflexiva porque nunca ocurre $x<x$. Por ello no es reflexiva sobre un dominio no vacío.

## E. Simetría, antisimetría y asimetría

### 25

La igualdad es simétrica: $a=b\Rightarrow b=a$. También es antisimétrica: si $a=b$ y $b=a$, entonces necesariamente $a=b$. Por tanto posee ambas propiedades.

### 26

$A\times A$ es simétrica porque contiene todos los pares y sus inversos. Si $|A|\ge2$, no es antisimétrica: para $a\ne b$ contiene simultáneamente $(a,b)$ y $(b,a)$.

### 27

Si $a<b$, no puede ocurrir $b<a$. Por tanto $a<b\Rightarrow\neg(b<a)$, exactamente la definición de asimetría.

### 28

Si $a\le b$ y $b\le a$, entonces $a=b$, así que es antisimétrica. No es simétrica cuando existen $a<b$: entonces $a\le b$ pero no $b\le a$.

### 29

Es simétrica porque $|x|=|y|$ implica $|y|=|x|$. No es antisimétrica: $1R(-1)$ y $(-1)R1$, pero $1\ne-1$.

### 30

Por ejemplo $R=\{(1,1),(2,2)\}$. Todo par es diagonal, así que la relación es simétrica y antisimétrica; además es no vacía.

### 31

Por ejemplo $R=\{(1,2),(2,1),(2,3)\}$. No es simétrica porque $(2,3)\in R$ pero $(3,2)\notin R$. Tampoco es antisimétrica porque contiene $(1,2)$ y $(2,1)$ con $1\ne2$.

### 32

La relación $\le$ sobre $\mathbb R$ es antisimétrica, pero no asimétrica porque contiene todos los pares $(x,x)$. La asimetría prohíbe la reflexividad.

### 33

Si $R$ fuese asimétrica y existiera $aRa$, la definición aplicada a $aRa$ exigiría $\neg(aRa)$, contradicción. Por tanto ningún $a$ se relaciona consigo mismo: $R$ es irreflexiva.

### 34

Sea $(a,b)\in R$. Por simetría, $(b,a)\in R$. Por antisimetría, de ambos pares se sigue $a=b$. Así todo par de $R$ tiene componentes iguales y $R\subseteq I_A$.

## F. Transitividad

### 35

Sí. La única cadena no trivial relevante es $(1,2),(2,3)$ y el cierre $(1,3)$ está presente. No hay otras cadenas que exijan pares nuevos.

### 36

No. $(1,2)\in R$ y $(2,3)\in R$, pero $(1,3)\notin R$. Ese triple $1,2,3$ refuta transitividad.

### 37

Si $aI_Ab$ y $bI_Ac$, entonces $a=b$ y $b=c$, por lo que $a=c$ y $aI_Ac$. Es transitiva.

### 38

La condición transitiva sólo puede fallar si existen $a,b,c$ con $aRb$ y $bRc$ pero no $aRc$. En la relación vacía no existen siquiera las dos primeras premisas; por tanto la implicación universal es verdadera vacíamente.

### 39

Si $a<b$ y $b<c$, la transitividad del orden real da $a<c$. Por tanto $<$ es transitiva.

### 40

No. Como $(1,2)$ y $(2,1)$ pertenecen a $R$, transitividad exigiría $(1,1)$, que falta. También la cadena $(2,1),(1,2)$ exigiría $(2,2)$.

### 41

Tome $A=\{1,2,3\}$, $R=\{(1,2)\}$ y $S=\{(2,3)\}$. Cada una es transitiva vacíamente porque no contiene cadenas de dos pasos. Pero $R\cup S$ contiene $(1,2)$ y $(2,3)$ sin $(1,3)$, así que no es transitiva.

### 42

Si $(a,b)$ y $(b,c)$ pertenecen a $R\cap S$, pertenecen tanto a $R$ como a $S$. Como ambas son transitivas, $(a,c)$ pertenece a $R$ y a $S$. Por tanto $(a,c)\in R\cap S$.

## G. Clasificación combinada

### 43

$I_A$ es reflexiva, simétrica, antisimétrica y transitiva. No es irreflexiva ni asimétrica cuando $A$ es no vacío. En particular, es una relación de equivalencia.

### 44

$A\times A$ es reflexiva, simétrica y transitiva. Si $|A|\ge2$, no es antisimétrica ni asimétrica ni irreflexiva. Es una relación de equivalencia con una sola clase: $A$.

### 45

$<$ es irreflexiva, asimétrica, antisimétrica y transitiva. No es reflexiva ni simétrica. No es una equivalencia.

### 46

$\le$ es reflexiva, antisimétrica y transitiva. No es irreflexiva, simétrica ni asimétrica. No es una equivalencia.

### 47

Es reflexiva porque contiene toda la diagonal; simétrica porque $(1,2)$ y $(2,1)$ aparecen juntos; no es antisimétrica porque $1\ne2$ y ambos pares están presentes; no es asimétrica; es transitiva, pues el bloque $\{1,2\}$ es completo y $3$ sólo se relaciona consigo mismo. Es una equivalencia.

### 48

Es reflexiva. No es simétrica porque $(1,2)$ está y $(2,1)$ no. Es antisimétrica: no existen pares inversos entre elementos distintos. No es asimétrica porque tiene lazos. Es transitiva: las únicas composiciones con $(1,2)$ usan lazos y no generan pares nuevos. No es equivalencia por falta de simetría.

### 49

Es reflexiva, simétrica y transitiva porque la igualdad de valores absolutos posee esas tres propiedades. No es antisimétrica: $1$ y $-1$ son distintos pero se relacionan en ambos sentidos. No es asimétrica. Es una equivalencia.

### 50

No es reflexiva porque $x-x=0\ne1$. No es simétrica: si $x-y=1$, entonces $y-x=-1$. Es antisimétrica vacíamente, pues nunca pueden ocurrir a la vez $x-y=1$ y $y-x=1$. De hecho es asimétrica. No es transitiva: $2R1$ y $1R0$, pero $2R0$ exigiría $2-0=1$, falso.

## H. Relaciones de equivalencia

### 51

Reflexiva: todo entero tiene la misma paridad que sí mismo. Simétrica: si $x$ e $y$ tienen la misma paridad, entonces $y$ y $x$ también la tienen. Transitiva: si $x$ tiene la misma paridad que $y$ y $y$ tiene la misma paridad que $z$, entonces $x$ y $z$ tienen la misma paridad. Por tanto, es una equivalencia.

### 52

Reflexiva porque $x^2=x^2$; simétrica porque $x^2=y^2\Rightarrow y^2=x^2$; transitiva porque $x^2=y^2$ y $y^2=z^2$ implican $x^2=z^2$. Es equivalencia.

### 53

Reflexiva: si $x\ne0$, entonces $x\cdot x=x^2>0$. Simétrica: $xy>0$ equivale a $yx>0$. Transitiva: si $xy>0$ y $yz>0$, entonces $x,y$ tienen el mismo signo y $y,z$ también, por lo que $x,z$ tienen el mismo signo y $xz>0$. Hay dos clases: positivos y negativos.

### 54

No es equivalencia. Es reflexiva y transitiva, pero no simétrica: por ejemplo $2R1$ porque $2\ge1$, mientras $1R2$ es falso.

### 55

Sí. La diagonal da reflexividad. Los únicos pares no diagonales aparecen en parejas inversas $(1,3),(3,1)$ y $(2,4),(4,2)$, así que es simétrica. Los dos bloques $\{1,3\}$ y $\{2,4\}$ son completos internamente, de modo que cualquier cadena queda dentro del mismo bloque y la relación es transitiva. Es equivalencia.

### 56

Toda palabra tiene la misma longitud que sí misma; si $|u|=|v|$, entonces $|v|=|u|$; y si $|u|=|v|$ y $|v|=|w|$, entonces $|u|=|w|$. Por tanto es equivalencia.

## I. Clases de equivalencia

### 57

Hay exactamente dos clases: $E$, el conjunto de enteros pares, y $O$, el conjunto de enteros impares. Para cualquier par $p$, $[p]=E$; para cualquier impar $q$, $[q]=O$. El cociente es $\mathbb Z/\sim=\{E,O\}$.

### 58

$[0]=\{0\}$. Como $x^2=9$ equivale a $x=3$ o $x=-3$, $[3]=\{3,-3\}$. Del mismo modo $[-5]=\{5,-5\}$.

### 59

$[1]=[3]=\{1,3\}$ y $[2]=[4]=\{2,4\}$.

### 60

Supongamos que $aRb$. Si $x\in[a]$, entonces $xRa$. Con $aRb$, transitividad da $xRb$, de modo que $x\in[b]$ y $[a]\subseteq[b]$. Por simetría $bRa$ y el mismo argumento da $[b]\subseteq[a]$. Luego $[a]=[b]$.

### 61

Tomemos $x\in[a]\cap[b]$. Entonces $xRa$ y $xRb$. De $xRa$ y simetría obtenemos $aRx$; con $xRb$, transitividad da $aRb$. Por el resultado anterior, $[a]=[b]$.

### 62

$b\in[a]$ significa $bRa$. En una equivalencia, elementos relacionados tienen la misma clase, así que $[b]=[a]$. Por ello una clase puede nombrarse mediante cualquiera de sus miembros: el representante cambia, el subconjunto no.

## J. Particiones y cocientes

### 63

Dos elementos se relacionan exactamente cuando pertenecen al mismo bloque. Por tanto, la relación contiene los nueve pares de $\{1,3,5\}^2$ y los cuatro pares de $\{2,4\}^2$: $R=(\{1,3,5\}\times\{1,3,5\})\cup(\{2,4\}\times\{2,4\})$.

### 64

Sí. Cada bloque es no vacío; los tres bloques son dos a dos disjuntos; y su unión es $\{1,2,3,4,5\}$. Por tanto forman una partición.

### 65

No es una partición porque los dos primeros bloques se superponen: ambos contienen $2$. Una partición exige que bloques distintos sean disjuntos.

### 66

Las clases son $\{1,3\}$ y $\{2,4\}$, por lo que $A/R=\big\{\{1,3\},\{2,4\}\big\}$.

### 67

Cada $C_i$ es un subconjunto no vacío de $A$: una clase de equivalencia. Los elementos de $A/R$ son esas clases. Un elemento $a\in A$ no pertenece necesariamente a $A/R$ porque los elementos de $A/R$ son clases de equivalencia, es decir, subconjuntos de $A$, y no los objetos originales de $A$.

### 68

Dirección 1: las clases de una equivalencia son no vacías porque $a\in[a]$, cubren $A$ porque cada $a$ pertenece a su clase, y dos clases son iguales o disjuntas; por tanto forman una partición. Dirección 2: dada una partición, defina $a\sim b$ si están en el mismo bloque. La relación es reflexiva porque cada elemento está en un bloque, simétrica porque compartir bloque es simétrico y transitiva porque si dos bloques comparten el elemento intermedio deben coincidir. Así la relación es una equivalencia.

## K. Transferencia y diagnóstico

### 69

Se necesitan al menos tres elementos. En un conjunto de dos elementos, para que falle la antisimetría deben aparecer ambos pares $(a,b)$ y $(b,a)$ con $a\ne b$; pero entonces, aparte de los lazos, no queda ningún par no diagonal con el que pueda fallar la simetría. En $A=\{1,2,3\}$, tome $R=\{(1,2),(2,1),(2,3)\}$. No es simétrica porque falta $(3,2)$ y no es antisimétrica porque contiene $(1,2)$ y $(2,1)$ con $1\ne2$.

### 70

El error es suponer que clases de equivalencia distintas pueden compartir elementos. Si $x$ pertenece a ambas clases, entonces $xRa$ y $xRb$; esto implica $aRb$ y por tanto $[a]=[b]$. La conclusión correcta es que las clases coinciden por completo.

### 71

Las clases son $C_1=\{1,4\}$, $C_2=\{2,5,6\}$ y $C_3=\{3\}$. El cociente es $A/R=\{C_1,C_2,C_3\}$. La relación es la unión $C_1\times C_1\cup C_2\times C_2\cup C_3\times C_3$, es decir $\{(1,1),(1,4),(4,1),(4,4),(2,2),(2,5),(2,6),(5,2),(5,5),(5,6),(6,2),(6,5),(6,6),(3,3)\}$.

### 72

Una relación de equivalencia empieza siendo un conjunto de pares ordenados que registra qué objetos se consideran comparables bajo un mismo criterio. La reflexividad garantiza que cada objeto quede clasificado; la simetría elimina una dirección privilegiada; la transitividad hace coherente la pertenencia a una misma categoría. Para cada elemento $a$, la clase $[a]$ reúne todos los objetos equivalentes a él. Dos clases no pueden solaparse parcialmente: si comparten un elemento, son iguales; si no, son disjuntas. Por ello las clases cubren el conjunto original sin superponerse y forman una partición. Recíprocamente, cualquier partición induce una equivalencia al declarar relacionados a los elementos del mismo bloque. El conjunto cociente $A/R$ reúne esas clases y reemplaza los objetos originales por las categorías determinadas por la relación. Así, una equivalencia es un mecanismo preciso de clasificación matemática.


***
## L. Construcción de relaciones


### 73

Podemos tomar $R=\{(1,2),(2,1),(2,3),(3,2)\}$. Cada par tiene su inverso y no hay lazos. No es transitiva: $1R2$ y $2R1$ exigirían $1R1$. En general, si una relación no vacía contiene $aRb$, la simetría da $bRa$ y la transitividad daría $aRa$, prohibido por irreflexividad. Por tanto las tres propiedades juntas fuerzan que la relación sea vacía; el ejemplo construido no puede ser transitivo.


### 74

Sobre $A=\{1,2,3\}$ sirve $R=\{(1,2),(2,3)\}$. No hay lazos ni pares inversos, por lo que es asimétrica; la cadena $1R2$, $2R3$ no termina en $1R3$. En una relación asimétrica, una cadena $aRb$, $bRc$ que viole transitividad requiere tres elementos distintos: $a=b$ o $b=c$ produciría un lazo, y $a=c$ produciría pares inversos. Con menos de tres elementos no puede existir ese triple. Tres es el tamaño mínimo.


### 75

En $A=\{1,2,3\}$ tomamos $R=I_A\cup\{(1,2),(2,3)\}$. Es reflexiva y no contiene pares inversos entre distintos elementos, así que es antisimétrica. Falla transitividad por $1R2$, $2R3$ y la ausencia de $1R3$. Los lazos tienen componentes iguales y no contradicen la conclusión de antisimetría. En un conjunto con a lo sumo dos elementos, un triple $aRb$, $bRc$ tiene alguna repetición. Si $a=b$ o $b=c$, el par $aRc$ ya es una de las premisas; si $a=c$, la reflexividad lo garantiza. Por tanto una relación reflexiva sobre dos elementos siempre es transitiva: sólo podría fallar mediante tres elementos distintos. El ejemplo de tres alcanza el mínimo.


### 76

Si $aRb$, la simetría da $bRa$ y la antisimetría exige $a=b$. Así, $R\subseteq I_A$. Recíprocamente, cualquier subconjunto de $I_A$ tiene ambas propiedades. Las posibilidades son $\varnothing$, los tres conjuntos con un único lazo, los tres conjuntos con dos lazos y $I_A$: ocho en total. Sólo $I_A$ es reflexiva y sólo $\varnothing$ es irreflexiva. Todas son transitivas: en una cadena de dos pares diagonales las tres componentes coinciden, y el par exigido ya está presente. La clasificación es exhaustiva porque se ha probado la condición necesaria y suficiente $R\subseteq I_A$.


### 77

Si $t<0$, ningún par cumple la condición porque $|x-y|\ge0$. La relación es vacía: no reflexiva sobre $\mathbb R$, pero sí irreflexiva, simétrica, antisimétrica, asimétrica y transitiva. Si $t=0$, la condición equivale a $x=y$: es reflexiva, simétrica, antisimétrica y transitiva; no es irreflexiva ni asimétrica. Si $t>0$, es reflexiva y simétrica. El par de puntos distintos $0,t$ cumple la relación en ambos sentidos, lo que refuta antisimetría y asimetría; los lazos refutan irreflexividad. Tampoco es transitiva: $0R_t t$ y $tR_t(2t)$, pero $|0-2t|=2t>t$. Los tres casos cubren todos los parámetros. Para descubrir el contraejemplo, se toman dos pasos de tamaño $t$: cada paso está permitido, pero su acumulación excede el umbral.


### 78

Sobre $\mathbb R$ es reflexiva y transitiva por las propiedades de $\le$ en los módulos. No es simétrica: $0R1$, pero no $1R0$. No es antisimétrica: $1R(-1)$ y $(-1)R1$, aunque $1\ne-1$. En $[0,\infty)$ la condición es simplemente $x\le y$, así que sigue siendo reflexiva y transitiva, sigue sin ser simétrica y ahora es antisimétrica: las dos desigualdades obligan a igualdad. La fórmula de la relación no cambió; el nuevo conjunto eliminó los elementos distintos con el mismo módulo.


## M. Poner a prueba las hipótesis


### 79

Los conjuntos son $C_1=\{1,2\}$, $C_2=\{1,2,3\}$ y $C_3=\{2,3\}$. Se superponen sin ser iguales, de modo que no forman una partición. $R$ es reflexiva y simétrica, pero no transitiva: falta $(1,3)$ y también su inverso. Cualquier equivalencia que la contenga debe añadir esos dos pares por las cadenas $1R2R3$ y $3R2R1$. Así se obtiene $A\times A$, que es una equivalencia. Es la menor porque los siete pares originales y los dos forzados agotan el producto cartesiano. Fuera de una equivalencia, los conjuntos $C_a$ no heredan el teorema de igualdad o disjunción.


### 80

Tenemos $C_1=\{1\}$, $C_2=\{1,2\}$ y $C_3=\{1,2,3\}$. La relación no es simétrica. Por ejemplo, $1R2$ y $C_1\subseteq C_2$, pero $2\in C_2$ no pertenece a $C_1$. La prueba de la inclusión inversa necesitaría $2R1$, obtenido en una equivalencia por simetría. Aquí esa inferencia no es válida. Reflexividad y transitividad por sí solas no permiten concluir igualdad de los conjuntos.


### 81

Todos los pares de $R$ tienen ambas componentes en $B=\{1,2\}$. Invertir un par conserva esa condición, y unir dos pares también: si $aRb$ y $bRc$, entonces $a,c\in B$, así que $aRc$. Sin embargo, $C_3=\varnothing$ y falta $3R3$. La relación no es reflexiva sobre $A$, y los conjuntos asociados no cubren al elemento $3$ ni son todos no vacíos. Sobre $B$, $R=B\times B$ sí es reflexiva, simétrica y transitiva; tiene un único bloque, $B$. Cambiar el conjunto declarado cambia qué exige reflexividad.


### 82

$S$ no es reflexiva porque falta el lazo de $a$. Sigue siendo simétrica: sólo se retiró un par igual a su inverso. Si existe $b\ne a$ en $[a]_R$, permanecen $aSb$ y $bSa$, mientras $aSa$ falta; no es transitiva. Si $[a]_R=\{a\}$, no queda en $S$ ningún par con una componente $a$: un par $xRa$ o $aRx$ obligaría a $x\in[a]_R$, y entonces $x=a$. Por tanto cualquier cadena en $S$ tiene extremos distintos de $a$. La transitividad de $R$ produce el par de cierre y éste no es el único retirado. Así $S$ es transitiva. Esto demuestra ambas direcciones del criterio. El único cierre que puede perderse es $(a,a)$; buscar una cadena que lo exija revela por qué importa el tamaño de la clase.


### 83

Cada $b\in B$ tiene $bRb$ y ambas componentes pertenecen a $B$, de modo que $bSb$. Si $xSy$, entonces $xRy$; por simetría $yRx$, y como $y,x\in B$, resulta $ySx$. Si $xSy$ y $ySz$, la transitividad da $xRz$; como los extremos están en $B$, también $xSz$. Para cualquier $x$, $x\in[b]_S$ equivale a $x\in B$ y $xRb$, exactamente la condición $x\in B\cap[b]_R$. La partición de $B$ se obtiene intersectando los bloques de $A/R$ con $B$ y descartando las intersecciones vacías. Las intersecciones no vacías de bloques distintos siguen disjuntas, y su unión es $B$. Si $B=\varnothing$, $S=\varnothing$ y la partición es la colección vacía; no se conserva un supuesto bloque vacío.


### 84

La unión contiene todos los lazos, $1\leftrightarrow2$ y $2\leftrightarrow3$, pero no $1\leftrightarrow3$. Es reflexiva y simétrica, pero la cadena $1,2,3$ refuta transitividad. La menor equivalencia que la contiene es $A\times A$, pues los dos pares faltantes quedan forzados por transitividad. Sobre un conjunto de dos elementos, sus únicas particiones son los dos bloques unitarios y el bloque total; las equivalencias son identidad y relación universal. Cualquier unión de ellas sigue siendo una de esas dos equivalencias. Con cero o un elemento tampoco puede fallar. El tamaño mínimo es tres.


## N. Reconstruir y contar clasificaciones


### 85

El primer bloque es exactamente $C=\{1,4\}$ y no puede absorber otros elementos. Los datos obligan a que $D=\{2,5\}$ y $E=\{3,6\}$ estén contenidos en bloques. Estos bloques pueden ser distintos, dando $\{C,D,E\}$, o coincidir, dando $\{C,D\cup E\}$. No pueden dividirse los pares prescritos y no hay otros elementos que repartir. Cada bloque de tamaño $k$ aporta $k^2$ pares. La primera relación tiene $4+4+4=12$ pares y la segunda $4+16=20$. Los datos determinan dos relaciones, no una: declarar exhaustividad exige considerar tanto la separación como la unión de los dos bloques pendientes.


### 86

Los conjuntos $\{a,b\}$ y $\{b,c\}$ comparten $b$ sin ser iguales, así que $\Pi$ no es partición. Una equivalencia que contenga los pares de cada conjunto debe relacionar $a$ con $b$ y $b$ con $c$; la transitividad obliga a relacionar $a$ con $c$, y la simetría obliga a todos los pares inversos. La reflexividad añade los lazos. La relación mínima es $(\{a,b,c\}\times\{a,b,c\})\cup\{(d,d)\}$. Su partición es $\{\{a,b,c\},\{d\}\}$, distinta de la colección inicial. Es mínima porque todo par del bloque de tres está forzado; la relación construida ya satisface las condiciones sin unir $d$ con los demás.


### 87

Un ejemplo tiene bloques $\{1\}$, $\{2,3\}$ y $\{4,5\}$; su relación es la unión de los productos de cada bloque consigo mismo. Hay cinco elecciones del elemento que queda solo. Fijado ese elemento, llamemos $u,v,w,z$ a los otros cuatro. Sus particiones en dos pares son exactamente $\{\{u,v\},\{w,z\}\}$, $\{\{u,w\},\{v,z\}\}$ y $\{\{u,z\},\{v,w\}\}$. Para probar que son todas, el compañero de $u$ debe ser uno de los otros tres y, elegido éste, el par restante queda determinado. No se cuenta el orden de los dos bloques. Resultan $5\cdot3=15$ particiones, por tanto 15 equivalencias por la correspondencia de [§8.14](algebra-para-matematicos-capitulo-8-relaciones-y-relaciones-de-equivalencia.md#apm-c08-s14).


### 88

Para cada $a\in A$, el lazo $(a,a)$ pertenece a ambas relaciones y por tanto a $T$. Si $xTy$, el par inverso pertenece a $R$ y a $S$ por sus simetrías, así que $yTx$. Si $xTy$ y $yTz$, ambas relaciones contienen las dos premisas; sus transitividades dan $(x,z)$ en ambas, luego $xTz$. Para $x\in A$, $xTa$ equivale a $xRa$ y $xSa$, exactamente la pertenencia a la intersección de clases. En el ejemplo, la intersección de las dos clases de cualquier $a$ es $\{a\}$; las cuatro clases de $T$ son unitarias y $T=I_A$. Exigir ambas clasificaciones separa elementos que una sola relación podía agrupar.


### 89

Como $A\times A=\varnothing$, su único subconjunto es $R=\varnothing$. Las condiciones de reflexividad e irreflexividad son universales sobre un conjunto sin elementos: ninguna tiene un caso que la refute. Lo mismo ocurre con simetría y transitividad, de modo que $R$ es una equivalencia. Una partición sólo puede usar subconjuntos de $A$, pero el único es vacío y no se admite como bloque. Por ello la única partición es la colección vacía. En $A/R=\{[a]:a\in A\}$ no hay ningún $a$ que produzca una clase, así que el cociente es vacío. Añadir $\varnothing$ como elemento introduciría un bloque que no procede de ningún representante.


### 90

Dos clases no vacías que cubren cuatro elementos pueden tener tamaños $1,3$ o $2,2$, sin contar el orden de los bloques. El número de pares es la suma de los cuadrados de los tamaños: $1^2+3^2=10$ o $2^2+2^2=8$. Por tanto los datos fuerzan dos bloques de tamaño dos. Si $A=\{a,b,c,d\}$, sus tres particiones posibles son $\{\{a,b\},\{c,d\}\}$, $\{\{a,c\},\{b,d\}\}$ y $\{\{a,d\},\{b,c\}\}$. Cada una produce una relación diferente de ocho pares. El conteo identifica tamaños, pero no determina qué elementos comparten clase.


## O. Síntesis de relaciones y clases


### 91

Para cada $s\in\mathbb R$ tenemos el bloque $C_s=\{(t,s-t):t\in\mathbb R\}$. Es no vacío porque contiene $(0,s)$. Cada par $(a,b)$ está en $C_{a+b}$, pues $b=(a+b)-a$. Si un par perteneciera a $C_s$ y $C_r$, su suma sería a la vez $s$ y $r$, de modo que $s=r$. Estos bloques cubren y particionan $\mathbb R^2$. Los bloques de $(1,2)$ y $(0,3)$ son el mismo, $C_3=\{(t,3-t):t\in\mathbb R\}$; el de $(0,0)$ es $C_0=\{(t,-t):t\in\mathbb R\}$. La descripción es exhaustiva: todo punto tiene una suma y toda suma real aparece en $(0,s)$. La relación inducida es $(a,b)R(c,d)\Longleftrightarrow a+b=c+d$, reflexiva, simétrica y transitiva por las propiedades de la igualdad.


### 92

El bloque de $(a,b)$ es $C_{a,b}=\{(a,b),(b,a)\}$. Todo par está en su bloque. Si dos bloques comparten un par, ese par coincide con el original o con el intercambio de cada uno; intercambiar una segunda vez devuelve el original. En las cuatro combinaciones se obtiene que ambos bloques contienen exactamente los mismos dos pares, quizá repetidos. Así dos bloques distintos son disjuntos y forman una partición. La relación inducida admite igualdad o intercambio; es reflexiva y simétrica. La transitividad también queda explícita: no intercambiar ninguna vez deja el original; intercambiar sólo una vez deja el intercambio; intercambiar dos veces devuelve el original. La clase es unitaria exactamente cuando $a=b$, pues $(a,b)=(b,a)$ equivale a esa igualdad de componentes. Se conserva el orden dentro de cada par, aunque se lo clasifique junto con su intercambio.


### 93

Los primeros dos datos fuerzan que $1,2,3$ compartan bloque: el elemento $2$ no puede pertenecer a dos bloques distintos. El tercero obliga a agrupar $4,5$. Los bloques $\{1,2,3\}$ y $\{4,5\}$ forman una partición, y su relación es $R=(\{1,2,3\}\times\{1,2,3\})\cup(\{4,5\}\times\{4,5\})$. Toda equivalencia que contenga los datos debe contener cada par de esos bloques: simetría permite recorrer en ambos sentidos, transitividad une las cadenas y reflexividad suministra los lazos. Nuestra relación satisface los datos sin unir ambos bloques, por lo que es la menor por inclusión. Tiene $3^2+2^2=13$ pares. Al retirar el dato sobre $2$ y $3$, los bloques mínimos son $\{1,2\}$, $\{3\}$ y $\{4,5\}$, con $4+1+4=9$ pares. Retirar un dato antes de completar puede separar un bloque; no equivale a borrar un único par de la equivalencia ya construida.


### 94

La igualdad de longitud y la igualdad del número de letras $a$ son cada una reflexiva, simétrica y transitiva; exigir ambas conserva esas tres propiedades. En consecuencia, por §[§8.13](algebra-para-matematicos-capitulo-8-relaciones-y-relaciones-de-equivalencia.md#apm-c08-s13)–8.14, sus clases forman una partición. El bloque de $aabb$ contiene exactamente las palabras de longitud cuatro con dos letras $a$: $aabb,abab,abba,baab,baba,bbaa$. La lista es exhaustiva porque las posiciones de las dos $a$ son $12,13,14,23,24,34$ y las otras posiciones llevan $b$. Al cambiar a disyunción se pierde transitividad. Las palabras $u=a$, $v=b$ y $w=bb$ cumplen $uRv$ por longitud, y $vRw$ por tener cero letras $a$. Pero $u,w$ tienen longitudes distintas y números de $a$ distintos, así que no están relacionados. No podrían compartir bloques según ese criterio: los dos primeros vínculos obligarían a unir los tres objetos en uno. Buscar un primer vínculo por una condición y un segundo por la otra permite detectar el fallo de la disyunción.


### 95

El cociente es $A/R=\{\{1,2\},\{3,4\}\}$; sus elementos son bloques. $T$ es un conjunto de representantes y no es igual al cociente. Si $a\in\{1,2\}$, está relacionado con $1\in T$ y no con $3$; si $a\in\{3,4\}$, ocurre lo inverso. Esto demuestra existencia y unicidad del representante relacionado en $T$ para cada $a$. Con $T'$ se representan los mismos bloques mediante $2$ y $4$: $[2]=[1]$ y $[4]=[3]$. Cambia el conjunto de nombres elegidos, pero el conjunto de clases no cambia. La unicidad mencionada depende del conjunto de representantes: no afirma que una clase tenga un único elemento.


### 96

El estudiante invierte la inclusión: los bloques menores contienen menos comparaciones. El criterio es $R\subseteq S$ si y sólo si $[a]_R\subseteq[a]_S$ para todo $a\in A$. Si $R\subseteq S$ y $x\in[a]_R$, entonces $xRa$, luego $xSa$ y $x\in[a]_S$. Para el recíproco, supongamos todas las inclusiones de clases y tomemos un par cualquiera $(x,a)\in R$. Esto significa $x\in[a]_R$, por lo que $x\in[a]_S$ y $(x,a)\in S$. Así todo par de $R$ está en $S$. Si cada bloque de $R$ está contenido en algún bloque de $S$, ese bloque de $S$ tiene que ser $[a]_S$ para cualquier $a$ del primero, pues contiene a $a$. En el ejemplo, $R\subseteq S$, pero la inclusión inversa falla: $(1,3)\in S$ y $(1,3)\notin R$. Los conteos son $2^2+1^2+2^2=9$ y $3^2+2^2=13$. Unir bloques conserva pares antiguos y añade comparaciones; el criterio explica la inclusión sin listar cada par.

***

[← Capítulo 7](conjuntos-y-algebra-de-conjuntos.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 9 →](algebra-para-matematicos-capitulo-9-funciones-composicion-e-inversas.md)

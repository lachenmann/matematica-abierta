---
title: Capítulo 20 — Diagonalización y lema diagonal
status: published
draft: false
book-id: MA-BOK-0014
editorial-project: TLOG
date-modified: '2026-10-11'
license: GFDL-1.3-or-later
areas:
- fundamentos
level: avanzado
topics:
- logica
number-sections: false
content-id: MA-BCH-0222
content-type: book-chapter
source-id: TLOG-CH20-0001
prerequisites:
- MA-BCH-0211
- MA-BCH-0212
- MA-BCH-0219
- MA-BCH-0220
- MA-BCH-0221
related:
- MA-BOK-0014
source-sha256: eb93df3f3f1dcbaab9474076adab6e1d10bf9e7fd5cb388a4d4a62e401e40567
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 19](capitulo-19.md) · [Capítulo 21 →](capitulo-21.md)

## 20.0. Una fórmula que nombra su propio código

Una expresión aritmética no contiene, como parte de su gramática, una operación que diga «esta misma expresión». El capítulo anterior hizo calculable la sustitución de numerales y proporcionó fórmulas que representan ese cálculo en cada entrada concreta. Con ese puente podemos construir una sentencia δ para la cual PA prueba que δ equivale a aplicar un predicado dado al numeral del código de δ.

La construcción tendrá tres momentos: preparar una fórmula auxiliar B, calcular su código p y sustituir el numeral de p en B. El código de la fórmula resultante se obtiene entonces mediante autoinstanciación. La representación aritmética de esa función permite demostrar el bicondicional. Así la autorreferencia aparece como consecuencia de operaciones sintácticas finitas y pruebas de igualdad.

Desarrollaremos primero el lema para sentencias, después conservaremos parámetros y construiremos familias finitas de referencias mutuas. También obtendremos procedimientos externos de construcción y búsqueda de pruebas. Las aplicaciones a demostrabilidad se presentan con el predicado concreto de CH19; su análisis de incompletitud queda en los capítulos21–22. Éste es el capítulo final de la Parte IV.

## 20.1. Fundamento y alcance de la autorreferencia

### Convención 20.1.1 — Fundamento y alcance de la autorreferencia {#tlog-cnv-00031}

El universo de trabajo externo sigue siendo $M_{ext}=\mathrm{ZF}$ clásica, sin AC ni BPI. RM es el sistema operacional metateórico, y PA es la teoría objeto aritmética fijada en CH19. $\mathrm{ZF}_{obj}$ conserva su lenguaje y sus axiomas propios: no se le atribuye una interpretación aritmética, consistencia o modelo por analogía con PA.

Todos los puntos fijos de este capítulo son **fórmulas finitas de $L_A$** y todas sus equivalencias son teoremas de PA. Su construcción y el cálculo de sus códigos ocurren externamente. Una afirmación de existencia de una derivación PA se demuestra mediante las reglas admisibles ya expandidas desde axiomas y MP; no constituye por sí sola verificación Lean. No añadiremos una regla primitiva de autorreferencia ni un símbolo objeto que convierta una fórmula en su código.

La Parte IV termina al disponer de estos puntos fijos y de sus procedimientos efectivos. El análisis de independencia y del comportamiento interno de los predicados de demostrabilidad corresponde a la Parte V. Construir una equivalencia diagonal no basta, por sí solo, para declarar independencia, reflexión o consistencia interna.

## 20.2. Comillas de Gödel, instanciación y tres igualdades

### Definición 20.2.1 — Comillas de Gödel, instanciación y tres igualdades {#tlog-def-00143}

Para una fórmula aritmética concreta A, $\ulcorner A\urcorner$ abrevia **el término numeral** $\overline{G(A)}$. La operación G sigue siendo la codificación inyectiva de árboles del capítulo18; no se convierte en un símbolo de $L_A$. El natural $G(A)$, el término $\ulcorner A\urcorner$ y el código de ese término $\operatorname{Num}(G(A))$ son objetos distintos.

Si x es una variable designada, $A(t)$ abrevia la sustitución literal segura $A[t/x]_{lit}$, especificando x cuando pueda haber ambigüedad. En particular $A(\ulcorner B\urcorner)$ sustituye el **numeral del código de B** en los lugares libres designados de A; no inserta el árbol B. No se reemplazan apariciones ligadas ni se visita el término recién insertado. La notación de comillas vale también para fórmulas abiertas: G registra su árbol, incluidos los nombres de sus variables.

Distinguimos $A=B$ como igualdad literal de árboles, $G(A)=G(B)$ como igualdad externa de naturales y $\mathrm{PA}\vdash A\leftrightarrow B$ como equivalencia demostrable. Las primeras dos son equivalentes por inyectividad de G. La tercera no identifica códigos ni árboles. Las equivalencias alfa están igualmente separadas de la igualdad literal.

## 20.3. Higiene efectiva de variables en representantes

### Lema 20.3.1 — Higiene efectiva de variables en representantes {#tlog-lem-00081}

**Lema.** Una fórmula finita con una lista de variables libres designadas distintas puede transformarse efectivamente en una copia con nombres ligados fuera de un conjunto finito F y con esos argumentos en cualesquiera posiciones distintas prescritas. Se pueden dejar intactos otros parámetros libres. El renombrado ligado produce equivalencia alfa y equivalencia PA; el cambio de argumentos libres es una sustitución simultánea segura, no una identificación de fórmulas con distinto soporte libre.

**Prueba.** Recorremos las ocurrencias de cuantificadores con una pila de ligadores. A cada ocurrencia asignamos el menor índice fuera de F, de todos los nombres originales y de los ya asignados. En las hojas de variable, si hay un ligador activo homónimo, cambiamos por el nuevo nombre del ligador más cercano; de lo contrario conservamos la hoja libre. Así no se cambia una variable libre ni se confunden dos ligadores anidados homónimos. El recorrido termina por el número finito de constructores. La decisión alfa de §18.62 comprueba que el resultado conserva el árbol de índices de ligadores; CH9 da la equivalencia PA de las copias alfa.

Para cambiar los argumentos libres, incluimos en F todos los nombres destino y todos los parámetros que permanecerán. Escogemos además nombres intermedios frescos, uno por argumento. Primero cambiamos cada argumento original por su intermedio, después cada intermedio por su destino. Las sustituciones son seguras porque todos estos nombres están ausentes de los ligadores; los intermedios evitan un intercambio secuencial erróneo, como cambiar x por y y luego y por x. Si un destino coincide con un parámetro que debe conservarse, la petición se rechaza: los destinos deben ser distintos de tales parámetros. La condición es decidible.

Para transportar una prueba, primero se generalizan sus argumentos libres, después se particularizan con los nuevos nombres (seguros tras la higiene). La equivalencia alfa de la copia ligada permite cambiar esa copia dentro de la conclusión. También se puede renombrar uniformemente toda la derivación, expandiendo las reglas admisibles. Ninguna sustitución por variable se realiza suponiendo seguridad sin comprobarla. $\square$

## 20.4. Autoinstanciación en una coordenada designada

### Definición 20.4.1 — Autoinstanciación en una coordenada designada {#tlog-def-00144}

Para cada índice externo i fijamos la función total
$$
D_i(c)=\begin{cases}
G(A[\bar c/x_i]_{lit}),&c=G(A),\ A\text{ fórmula de }L_A,\\
0,&c\text{ no es código de fórmula de }L_A.
\end{cases}
$$
Es la composición $\operatorname{Sub}(c,i,c)$ de CH19. Para i=0 es exactamente D, con la misma totalización por0. Las fórmulas válidas tienen códigos positivos y la salida inválida0 no es el código de una fórmula. Si $x_i\notin FV(A)$, entonces $D_i(G(A))=G(A)$; no se requiere que la coordenada ocurra.

El numeral insertado es cerrado, por tanto seguro aunque aparezcan ligadores llamados $x_i$. La función no decide verdad, demostrabilidad o pertenencia a una clase semántica. Un código de término, una secuencia de fórmulas y el número de una prueba no pasan la guarda de fórmula sólo por ser números naturales.

## 20.5. Representación numeral de la autoinstanciación

### Lema 20.5.1 — Representación numeral de la autoinstanciación {#tlog-lem-00082}

**Lema.** Para cada i se obtiene efectivamente un representante aritmético $\Theta_i(u,v)$ de $D_i$, con sólo u,v libres. Para todo c externo y $d=D_i(c)$,
$$
\mathrm{PA}\vdash\forall v(\Theta_i(\bar c,v)\leftrightarrow v=\bar d).\tag{R_i(c)}
$$
Se pueden elegir u,v en posiciones distintas prescritas y todos los ligadores frescos respecto de cualquier conjunto finito de nombres. $\Theta_i$ puede obtenerse de la fórmula Σ1 de su programa RM; después de cambios alfa se entiende como una copia demostrablemente equivalente a ella.

**Prueba.** El programa total Sub y composición RM, con proyecciones y la constante i, calculan $D_i$. La representación general de CH19 produce su gráfica y, como cada entrada estándar termina, la equivalencia funcional en esa entrada. El lema de higiene cambia los dos argumentos y sus ligadores conservando esa equivalencia por generalización/particularización y equivalencia alfa. Cada elección es finita y efectiva. La construcción depende de i, pero la selección del programa con la constante i y su compilación en fórmula también son uniformes externamente.

No se usa ni se reclama aquí $\mathrm{PA}\vdash\forall u\exists v\Theta_i(u,v)$. La prueba diagonal necesitará una sola instancia $R_i(c)$, con c un número concreto que se construirá después de fijar la fórmula auxiliar. No hay una circularidad: el programa de $D_i$ y su representante se fijan antes de conocer ese c. $\square$

## 20.6. Eliminación de un testigo fijado por un numeral

### Lema 20.6.1 — Eliminación de un testigo fijado por un numeral {#tlog-lem-00083}

**Lema lógico.** Sea t un término cerrado, C(v,\bar z) una fórmula en la que v no liga ninguna de las apariciones libres que se sustituirán, y E(v) una fórmula con v libre. Si
$$
\mathrm{PA}\vdash\forall v(E(v)\leftrightarrow v=t),
$$
entonces, con los parámetros $\bar z$ intactos,
$$
\mathrm{PA}\vdash\exists v(E(v)\land C(v,\bar z))\leftrightarrow C(t,\bar z).\tag{E}
$$
También se prueba $\forall v(E(v)\to C(v,\bar z))\leftrightarrow C(t,\bar z)$.

**Prueba.** Para la dirección existencial hacia la derecha, bajo E(v) y C(v), la particularización de la hipótesis da v=t; el esquema de sustitución de iguales para la fórmula C da C(t). Se descarga el testigo mediante la eliminación existencial admisible, tomando un nombre auxiliar ausente de la conclusión y las hipótesis restantes. Para la recíproca, reflexividad y la equivalencia en v=t dan E(t); de C(t) se obtiene E(t)∧C(t), y la introducción existencial concluye. Deducción y cálculo proposicional combinan ambas implicaciones en el bicondicional.

Para la forma universal, C(t) y E(v) implican v=t y C(v), por simetría y sustitución de iguales; se descarga y generaliza v, que no es libre en C(t). Recíprocamente se particulariza en t y se usa E(t). Los nombres de testigo se escogen frescos y t es cerrado, de modo que todas las particularizaciones son seguras. Estas son expansiones finitas de las reglas de CH9, desde axiomas y MP, sin axioma nuevo. $\square$

## 20.7. Punto fijo demostrable y parámetro de código

### Definición 20.7.1 — Punto fijo demostrable y parámetro de código {#tlog-def-00145}

Si A(z) tiene a lo sumo z libre, una **sentencia fija para A en PA** es una sentencia δ tal que
$$
\mathrm{PA}\vdash\delta\leftrightarrow A(\ulcorner\delta\urcorner).
$$
Si $A(z,\bar w)$ tiene parámetros libres distintos de z, una **fórmula fija con parámetros** es δ(\bar w), con $FV(\delta)\subseteq\{\bar w\}$, tal que
$$
\mathrm{PA}\vdash\delta(\bar w)\leftrightarrow A(\ulcorner\delta\urcorner,\bar w).
$$
Las comillas en esta última ecuación contienen el código del árbol abierto δ, **no** el código de cada una de sus instancias numerales. No se exige igualdad literal de los dos lados, unicidad de δ ni que A describa demostrabilidad. Un parámetro z vacuo también es admisible.

## 20.8. Lema diagonal para sentencias aritméticas

### Metateorema 20.8.1 — Lema diagonal para sentencias aritméticas {#tlog-mth-00112}

**Metateorema (lema diagonal).** Para toda fórmula aritmética A(z) con $FV(A)\subseteq\{z\}$ existe una sentencia δ, construida efectivamente a partir de A, tal que $\mathrm{PA}\vdash\delta\leftrightarrow A(\ulcorner\delta\urcorner)$.

**Construcción.** Escogemos i fuera de Names(A) y una variable y distinta, también fuera de esos nombres. Ponemos x=$x_i$. Normalizamos el representante $\Theta_i(x,y)$ con todos sus ligadores fuera de Names(A)∪{x,y}. En A reemplazamos **sólo** z libre por y; como y no aparece entre sus nombres, es seguro. Llamamos C(y)=A[y/z] y construimos
$$
B(x):=\exists y(\Theta_i(x,y)\land C(y)),\quad p:=G(B),\quad
\delta:=B[\bar p/x]_{lit}.\tag{1}
$$
Todos los pasos son finitos. B sólo puede tener x libre; δ es cerrada. La sustitución del numeral es siempre segura. Por la definición de $D_i$ y la igualdad literal de (1),
$$
D_i(p)=G(B[\bar p/x]_{lit})=G(\delta)=:d.\tag{2}
$$

**Derivación.** La única instancia de representación necesaria es
$$
\mathrm{PA}\vdash\forall y(\Theta_i(\bar p,y)\leftrightarrow y=\bar d).
$$
Literalmente δ es $\exists y(\Theta_i(\bar p,y)\land C(y))$. Aplicando el lema de eliminación del testigo obtenemos $\mathrm{PA}\vdash\delta\leftrightarrow C(\bar d)$. La sustitución compuesta C[\bar d/y] es literalmente A[\bar d/z]: y era fresco, x no aparecía en A y el término final es cerrado. Por (2), $\bar d=\ulcorner\delta\urcorner$, como igualdad de términos. Concluye la equivalencia anunciada. $\square$

En el caso especial de una entrada ya higienizada para x0 puede usarse D=D0 directamente. Escoger una coordenada fresca permite tratar también A con ligadores llamados x0 sin identificar códigos alfa. En ningún paso se resuelve una ecuación numérica $d=G(A(\bar d))$: se calcula p, luego δ, luego d, en ese orden.

## 20.9. Hipótesis exactas y lectura de la prueba diagonal

### Proposición 20.9.1 — Hipótesis exactas y lectura de la prueba diagonal {#tlog-pro-00127}

**Proposición.** La prueba del lema diagonal usa sintaxis efectiva, igualdad y reglas lógicas, y la representación funcional **en la entrada numeral p** de una función sintáctica total externa. No usa consistencia de PA, un modelo de PA, totalidad uniforme de $D_i$ dentro de PA, un predicado de verdad o condiciones internas de derivabilidad. La ecuación producida sigue siendo un teorema en una teoría inconsistente que contenga esas mismas derivaciones.

**Prueba.** Se inspecciona la derivación de §20.8: (1) y (2) son cálculos externos de árboles; $R_i(p)$ es una prueba PA obtenida por representación; el resto sólo instancia el lema lógico (E). Ninguno de esos pasos elimina una prueba por inconsistencia ni usa satisfacción. La consistencia externa de PA ya demostrada en CH19 servirá para algunas consecuencias semánticas, pero no se introduce en la construcción. En particular, los números p y d son estándares externos porque proceden de árboles finitos construidos en $M_{ext}$; no se requiere afirmar dentro de PA que todas las entradas no estándar tengan salida para $D_i$. $\square$

## 20.10. Lema diagonal con parámetros preservados

### Metateorema 20.10.1 — Lema diagonal con parámetros preservados {#tlog-mth-00113}

**Metateorema.** Para toda $A(z,w_1,\ldots,w_q)$, con variables designadas distintas y sin otras variables libres, existe δ(\bar w) con $FV(\delta)\subseteq\{w_1,\ldots,w_q\}$ y
$$
\mathrm{PA}\vdash\forall w_1\cdots\forall w_q
\bigl(\delta(\bar w)\leftrightarrow A(\ulcorner\delta\urcorner,\bar w)\bigr).
\tag{P}
$$
Se admiten q=0 y parámetros vacuos. Si wj aparece libre en A, aparece libre en la δ construida.

**Prueba.** Elegimos x=$x_i$ e y fuera de **todos** los nombres de A, incluidos sus parámetros. Higienizamos $\Theta_i(x,y)$ fuera de estos nombres. Ponemos C(y,\bar w)=A[y/z], $B(x,\bar w)=\exists y(\Theta_i(x,y)\land C(y,\bar w))$, p=G(B) y δ=B[\bar p/x]. Exactamente como antes, $D_i(p)=G(\delta)=d$. Ahora $R_i(p)$ tiene sólo y libre bajo su universal, mientras C mantiene $\bar w$ libres. (E) da el bicondicional abierto δ(\bar w)↔C(\bar d,\bar w), y la sustitución segura identifica el segundo miembro con A(\bar d,\bar w). La generalización de teoremas de PA, en el orden indicado, produce (P).

Ningún wj se sustituye, se renombra o queda bajo un nuevo ligador: los nombres y,x y los ligados del representante están fuera de los nombres de A. El soporte libre final es precisamente $FV(A)\setminus\{z\}$; que una conjunción sea lógicamente equivalente a algo con menos variables no modifica su soporte sintáctico. p codifica B abierta, d codifica δ abierta, y ambos son números fijos independientes de una asignación a los parámetros. $\square$

## 20.11. Instancias de un punto fijo con parámetros

### Corolario 20.11.1 — Instancias de un punto fijo con parámetros {#tlog-cor-00031}

**Corolario.** Para cada tupla estándar $\bar n$ de longitud q,
$$
\mathrm{PA}\vdash\delta(\overline{\bar n})\leftrightarrow
A(\ulcorner\delta\urcorner,\overline{\bar n}).
$$
Esta ecuación conserva el código de δ abierta. No se puede cambiarlo, sin otro argumento, por $\ulcorner\delta(\overline{\bar n})\urcorner$.

**Prueba.** Particularizamos (P) con los numerales cerrados, luego expandimos las sustituciones simultáneas mediante nombres frescos. El término cerrado $\ulcorner\delta\urcorner$ no contiene ningún parámetro, así permanece intacto. La codificación de la instancia se obtiene por otras sustituciones sobre el árbol y puede ser un natural diferente.

Si se desea un punto fijo de la fórmula **ya especializada** $A(z,\overline{\bar n})$, se aplica otra vez el lema diagonal a esa fórmula cerrada en los parámetros. Así se obtiene una sentencia εn con su propio código en el bicondicional. No se identifica εn con la instancia de la familia anterior. $\square$

## 20.12. Compilador externo total de fórmulas fijas

### Metateorema 20.12.1 — Compilador externo total de fórmulas fijas {#tlog-mth-00114}

**Metateorema.** Hay un procedimiento RM total que, dados el código de A, el índice de su argumento de código y una lista S de parámetros distintos, decide la validez de la entrada y devuelve el código de una δ de §20.10; devuelve0 si la entrada no cumple la guarda. En particular se obtiene un compilador total de sentencias fijas para fórmulas con una variable libre designada.

**Procedimiento y prueba.** Se decodifica A en $L_A$, se decodifica la lista de índices, se comprueba distinción de argumentos y $FV(A)$ contenido en ellos. No se exige que aparezcan todos. El conjunto finito Names(A) da los menores nombres frescos x,y. Se genera el programa fijo de $D_i$ usando la constante i, se aplica el compilador de fórmulas de CH19, y se normaliza su representante a x,y con la higiene de §20.3. Se construyen C, B, se calcula p=G(B), se genera el numeral $\bar p$ y se realiza la sustitución cerrada. El resultado se codifica con G.

Las guardas y recorridos son totales por CH18. Construir $\bar p$ usa un bucle de exactamente p pasos externos, aunque p pueda ser enorme; codificar cada árbol usa sus constructores finitos. No se necesita probar una cota de complejidad útil. La composición y compilación de macros de CH17 dan un programa RM para cada fase y para su composición; el compilador de fórmulas de CH19 recorre una lista finita de instrucciones que ya ha sido generada. Cada fase termina, así el programa compuesto es total externamente. Su corrección es la construcción de §20.10, y la guarda inválida devuelve0, que no puede confundirse con un resultado válido.

Es un procedimiento externo sobre códigos. No se añade a PA una función primitiva Fix ni se afirma que PA demuestre la totalidad uniforme de ese programa. $\square$

## 20.13. Obtención efectiva de una derivación del bicondicional

### Metateorema 20.13.1 — Obtención efectiva de una derivación del bicondicional {#tlog-mth-00115}

**Metateorema.** Además del código de δ, se puede obtener efectivamente el código de una prueba PA del bicondicional abierto de §20.10 y, si se pide, de su clausura universal en los parámetros. El procedimiento es total sobre entradas válidas y puede totalizarse con0 en las inválidas.

**Prueba por búsqueda certificada.** Construida δ, se construye literalmente E=δ↔A(\ulcornerδ\urcorner,\bar w), o bien su clausura universal prescrita. Enumeramos d=0,1,2,… y aplicamos el decidor total externo $Prf^{ext}_{PA}(d,G(E))$ de CH19. Cuando acepta, devolvemos d. Cada comprobación termina, y §20.10 demuestra que existe una derivación PA finita de E. Su código S es algún natural d0, por lo que la búsqueda llegará a él y terminará. Ninguna corrección semántica de PA se usa para esta terminación: se usa la existencia sintáctica de la derivación construida en la prueba del lema.

La enumeración incluye secuencias originales con axiomas y MP, no un tag nuevo «lema diagonal». Las expansiones de las reglas admisibles de la prueba garantizan que E tiene una prueba en ese formato. Para entradas inválidas se rechaza antes de buscar. Esta búsqueda no decide cuáles fórmulas arbitrarias son teoremas: sólo es total sobre la familia cuya demostrabilidad acabamos de probar.

Se podría construir directamente la derivación expandiendo las instancias de representación y los esquemas lógicos. El algoritmo de búsqueda basta para la afirmación efectiva y evita atribuir a nuestras regresiones una implementación completa de ese constructor. No se entrega aquí una gigantesca secuencia numeral ni se afirma que una de esas secuencias haya sido validada por Lean. $\square$

## 20.14. Transferencia a extensiones de PA

### Proposición 20.14.1 — Transferencia a extensiones de PA {#tlog-pro-00128}

**Proposición.** Si T contiene deductivamente a PA en el mismo lenguaje aritmético y con el mismo cálculo, todos los bicondicionales de este capítulo y sus pruebas PA persisten como teoremas T. Para esta transferencia no hacen falta consistencia, efectividad de los axiomas T ni corrección estándar de T.

**Prueba.** Cada línea axiomática PA y cada aplicación de MP conserva una derivación T; si la inclusión es sólo deductiva, se sustituyen los axiomas PA utilizados por sus pruebas T finitas. La existencia del teorema T sigue. No se promete un algoritmo uniforme para efectuar esta segunda sustitución sin una presentación efectiva de esas pruebas de inclusión; la prueba PA producida por §20.13 siempre existe independientemente de ello.

La transferencia se refiere al lenguaje $L_A$. No se aplica automáticamente a $\mathrm{ZF}_{obj}$: faltaría una interpretación explícita, conservación de igualdad/sustitución y pruebas de la imagen de los axiomas PA. Tampoco se transportan afirmaciones estándar de verdad de T a partir de la mera inclusión PA⊆T. $\square$

## 20.15. Satisfacción de los puntos fijos en modelos de PA

### Proposición 20.15.1 — Satisfacción de los puntos fijos en modelos de PA {#tlog-pro-00129}

**Proposición.** La estructura estándar externa satisface el bicondicional diagonal, para toda asignación de sus parámetros. Más generalmente, si se da externamente una estructura $\mathcal M$ que satisface los axiomas PA, satisface también ese bicondicional bajo toda asignación. La segunda afirmación es condicional y no postula la existencia de un modelo no estándar.

**Prueba.** La corrección externa de CH19 aplica a la prueba PA de la equivalencia. Para $\mathcal M$, la misma inducción sobre la derivación, con sus axiomas PA verdaderos y MP, da satisfacción. En esa estructura $\ulcorner\delta\urcorner$ se interpreta como $S^{G(δ)}(0^{\mathcal M})$, el numeral de un código calculado **externamente**. No se identifica con una operación interna de codificación de todos los elementos de $\mathcal M$. La universalización de parámetros garantiza la afirmación para cualquier asignación. $\square$

## 20.16. La presentación universal del lema diagonal

### Lema 20.16.1 — La presentación universal del lema diagonal {#tlog-lem-00084}

**Lema.** La construcción alternativa
$$
B^\forall(x,\bar w)=\forall y(\Theta_i(x,y)\to A[y/z](y,\bar w)),\quad
p=G(B^\forall),\quad δ=B^\forall[\bar p/x]
$$
también produce un punto fijo con parámetros, cuando los nombres cumplen la misma higiene. Esta notación $A[y/z](y,\bar w)$ designa una sola sustitución libre, no dos sustituciones consecutivas.

**Prueba.** Se calcula $D_i(p)=G(δ)=d$ y se usa $R_i(p)$. La segunda parte de (E) da δ↔A[\bar d/z], con parámetros intactos. Después se generalizan. La existencia del testigo y la equivalencia de su valor están incluidas en $R_i(p)$: si se dispusiera solamente de una implicación $\Theta_i(\bar p,y)\to y=\bar d$, la universal podría ser vacuamente verdadera y el argumento fallaría.

El árbol $B^\forall$ no es literalmente el árbol existencial de §20.10; generalmente sus códigos y los de sus instancias son distintos. No se concluye que ambos puntos fijos sean equivalentes entre sí para un A arbitrario. Cada uno satisface su propio bicondicional con su propio numeral. $\square$

## 20.17. Cambio demostrablemente equivalente del predicado objetivo

### Proposición 20.17.1 — Cambio demostrablemente equivalente del predicado objetivo {#tlog-pro-00130}

**Proposición.** Si PA prueba $\forall z\forall\bar w(A(z,\bar w)\leftrightarrow C(z,\bar w))$, cualquier punto fijo δ de A es punto fijo de C, con **el mismo código de δ**. La verdad estándar de esa equivalencia sin prueba PA sólo da la conclusión semántica en la estructura estándar, no una nueva prueba del bicondicional.

**Prueba.** Particularizamos el teorema uniforme en $z=\ulcornerδ\urcorner$ y mantenemos $\bar w$ arbitrarios. Transitividad proposicional del bicondicional con δ↔A(\ulcornerδ\urcorner,\bar w) da δ↔C(\ulcornerδ\urcorner,\bar w). Se generalizan parámetros. La versión semántica sigue por sustitución segura y transitividad de satisfacción.

Esta proposición transporta un punto fijo ya existente. Si se construye otro mediante el compilador aplicado a C, su código puede cambiar y no hay razón para identificar las dos salidas. Tampoco una equivalencia alfa entre dos **sentencias fijas** justifica reemplazar, dentro de un predicado arbitrario, el numeral de una por el de la otra. $\square$

## 20.18. Autoinstanciación de una familia finita codificada

### Definición 20.18.1 — Autoinstanciación de una familia finita codificada {#tlog-def-00146}

Fijados externamente r≥1 e i, para 0≤j<r definimos $F_{r,i,j}(e)$: si e decodifica como una lista S de longitud exactamente r de códigos de fórmulas aritméticas $[c_0,\ldots,c_{r-1}]$, devolvemos $D_i(c_j)$ con **el numeral de e** en lugar del numeral de cj, es decir
$$
F_{r,i,j}(e)=\operatorname{Sub}(c_j,i,e).
$$
En cualquier otro caso devolvemos0. Se comprueba validez de todas las componentes. Los índices de componentes comienzan en0.

Por tanto F no es simplemente $D_i(c_j)$: todas las componentes reciben el mismo código e de la familia auxiliar. La distinción permite referencias mutuas sin que la j-ésima fórmula deba calcular su código antes de existir. Para r=0 se entrega una familia vacía sin ecuaciones, separadamente; F sólo se usa para r≥1.

## 20.19. Representación efectiva de los lectores diagonales finitos

### Lema 20.19.1 — Representación efectiva de los lectores diagonales finitos {#tlog-lem-00085}

**Lema.** Cada $F_{r,i,j}$ es total computable-RM y admite un representante $\Psi_j(x,y_j)$ funcional numeral por numeral. Sus fórmulas y las instancias de representación se obtienen con los argumentos prescritos y con ligadores fuera de una familia finita de nombres. La construcción es uniforme externamente en r,i,j bajo las guardas r≥1, j<r.

**Prueba.** Se decodifica e, se cuenta su longitud y se reconocen las r fórmulas mediante recorridos finitos. Se extrae cj y se aplica Sub(cj,i,e), que termina con numeral cerrado. Cualquier fallo produce0. CH17 compone los decidores y operaciones de lista, y CH19 compila el programa en un representante de su gráfica. La higiene de §20.3 dispone los nombres y conserva las instancias de equivalencia. Los parámetros r,i,j se incorporan como constantes en el programa generado, así el compilador termina también cuando ellos varían externamente.

Para e válido y $d_j=F_{r,i,j}(e)$ se dispone en particular de $\mathrm{PA}\vdash\forall y_j(\Psi_j(\bar e,y_j)\leftrightarrow y_j=\bar d_j)$. No se requiere una afirmación uniforme interna de existencia de todos esos valores ni se usa elección: la familia de r programas/fórmulas se construye mediante un bucle finito. $\square$

## 20.20. Lema diagonal simultáneo con parámetros

### Metateorema 20.20.1 — Lema diagonal simultáneo con parámetros {#tlog-mth-00116}

**Metateorema.** Dados r≥1 y fórmulas $A_j(z_0,\ldots,z_{r-1},\bar w)$, j<r, con argumentos designados distintos y sin otras variables libres, hay fórmulas $δ_j(\bar w)$ tales que para cada j
$$
\mathrm{PA}\vdash\forall\bar w\left(δ_j(\bar w)\leftrightarrow
A_j(\ulcornerδ_0\urcorner,\ldots,\ulcornerδ_{r-1}\urcorner,\bar w)\right).\tag{S}
$$
La familia y pruebas de sus ecuaciones se pueden obtener efectivamente.

**Construcción sin circularidad.** Elegimos x=xi y variables $y_0,\ldots,y_{r-1}$ distintas fuera de todos los nombres de los Aj. Para cada k<r fijamos el representante $\Psi_k(x,y_k)$ de $F_{r,i,k}$, con sus ligadores fuera de todos esos nombres y de los parámetros. Sustituimos simultáneamente los zk libres de cada Aj por yk; la frescura asegura seguridad y evita interferencias. Llamamos Cj a esa copia. Con asociación de conjunciones fijada a la derecha, ponemos
$$
B_j(x,\bar w)=\exists y_0\cdots\exists y_{r-1}
\bigl((\Psi_0(x,y_0)\land\cdots\land\Psi_{r-1}(x,y_{r-1}))\land C_j(\bar y,\bar w)\bigr).
$$
Primero construimos **todos** estos árboles, que no contienen aún el numeral de e. Después calculamos
$$
e=S([G(B_0),\ldots,G(B_{r-1})]),\qquad δ_j=B_j[\bar e/x].
$$
De la definición del lector finito resulta $F_{r,i,k}(e)=G(δ_k)=d_k$ para cada k. No se presupone una solución de r ecuaciones de números ni se elige una familia infinita.

**Derivación.** Las r instancias funcionales en e prueban que cada $\Psi_k(\bar e,y_k)$ equivale a $y_k=\bar d_k$. Eliminamos primero el existencial más interno y seguimos hacia afuera mediante (E), reordenando conjunciones por teoremas proposicionales. En cada eliminación, los otros lectores no contienen yk libre, sus ligadores se han higienizado y los términos $\bar d_k$ son cerrados. Al terminar queda Cj(\bar d,\bar w), literalmente Aj con los numerales de los códigos de las δk en las coordenadas libres. Se generalizan parámetros y se obtiene (S).

Todos los recorridos y compiladores son finitos, así la familia es computable externamente. Para las pruebas, se aplica a cada ecuación la enumeración de pruebas de §20.13; cada búsqueda termina porque acabamos de demostrar su existencia. Para r=0 no hay ninguna obligación y se devuelve la lista vacía. $\square$

## 20.21. Referencias mutuas y ausencia de una elección infinita

### Corolario 20.21.1 — Referencias mutuas y ausencia de una elección infinita {#tlog-cor-00032}

**Corolario.** Para fórmulas P(z) y Q(z) se pueden construir sentencias ε,η tales que PA prueba $ε\leftrightarrow P(\ulcornerη\urcorner)$ y $η\leftrightarrow Q(\ulcornerε\urcorner)$. Con parámetros la misma construcción conserva esos parámetros libres. No se ha demostrado una versión para familias infinitas.

**Prueba.** Tomamos r=2, $A_0(z_0,z_1)=P(z_1)$ y $A_1(z_0,z_1)=Q(z_0)$, permitiendo argumentos vacuos, y aplicamos (S). La familia auxiliar tiene exactamente dos componentes. La construcción no usa AC/BPI: todas las elecciones son mínimos de complementos de conjuntos finitos de índices, y todas las listas se generan por recursión finita. $\square$

## 20.22. Objetivos constantes y falta de unicidad literal

### Proposición 20.22.1 — Objetivos constantes y falta de unicidad literal {#tlog-pro-00131}

**Proposición.** Si C es una sentencia y el argumento z es vacuo en A(z)=C, un punto fijo para A es exactamente una sentencia demostrablemente equivalente a C. El lema diagonal no da unicidad literal, ni siquiera para un objetivo constante.

**Prueba.** La sustitución de un numeral por una variable libre ausente conserva literalmente C, por tanto la ecuación de punto fijo es δ↔C. Las sentencias δ1=C y δ2=C∧(0=0) satisfacen esa ecuación: la primera por identidad del bicondicional, la segunda por reflexividad de igualdad y cálculo proposicional. Sus árboles son distintos, pues δ2 tiene un nodo de conjunción y más constructores que C; por inyectividad G sus códigos son distintos. No se ha afirmado que haya dos clases de equivalencia PA distintas: estas dos sentencias son equivalentes PA.

Para objetivos no constantes, dos equivalencias $δ↔A(\ulcornerδ\urcorner)$ y $ε↔A(\ulcornerε\urcorner)$ tampoco proporcionan por sí solas una prueba δ↔ε. Falta relacionar las dos instancias de A en numerales diferentes. $\square$

## 20.23. Sentencias diagonales para el predicado de demostrabilidad

### Definición 20.23.1 — Sentencias diagonales para el predicado de demostrabilidad {#tlog-def-00147}

Fijamos las fórmulas $Prf_{PA}$ y $Prov_{PA}$ de CH19, con sus representantes concretos, y fijamos las elecciones efectivas de nombres del compilador. Llamamos $\mathcal G_{PA}$ a su sentencia fija para $\neg Prov_{PA}(z)$ y $\mathcal H_{PA}$ a su sentencia fija para $Prov_{PA}(z)$. Se disponen de las pruebas
$$
\mathrm{PA}\vdash\mathcal G_{PA}\leftrightarrow\neg Prov_{PA}(\ulcorner\mathcal G_{PA}\urcorner),
\qquad
\mathrm{PA}\vdash\mathcal H_{PA}\leftrightarrow Prov_{PA}(\ulcorner\mathcal H_{PA}\urcorner).
$$
Los símbolos $\mathcal G,\mathcal H$ nombran sentencias construidas; no son nuevos símbolos objeto. Sus árboles contienen numerales de códigos obtenidos por la construcción, aunque no se impriman esos numerales completos. La fórmula $Prov_{PA}$ no se sustituye por otro representante durante la construcción.

## 20.24. Qué entregan las instancias de demostrabilidad

### Proposición 20.24.1 — Qué entregan las instancias de demostrabilidad {#tlog-pro-00132}

**Proposición.** En $\mathbb N_A$, las dos sentencias recién definidas satisfacen las equivalencias de §20.23 con la relación externa de existencia de una prueba PA. La construcción entrega pruebas de los bicondicionales y no incluye una regla de reflexión ni una demostración de las condiciones internas de derivabilidad.

**Prueba.** Corrección estándar aplica a los dos bicondicionales PA. La exactitud estándar de $Prov_{PA}$ en CH19 identifica la satisfacción de su instancia numeral con la existencia externa de una prueba de la sentencia nombrada. Este paso es metateórico, limitado a $\mathbb N_A$ y al representante fijado. No se transforma en una implicación PA uniforme $Prov_{PA}(\ulcorner A\urcorner)\to A$.

El cálculo de independencia de $\mathcal G_{PA}$ y el comportamiento de $\mathcal H_{PA}$ exigen argumentos adicionales sobre demostrabilidad. Se dejan expresamente para la Parte V, donde se registrarán las hipótesis de cada resultado. Este capítulo no asigna a ambas sentencias una clasificación de independencia o decidibilidad por el mero signo de negación que aparece en el objetivo. $\square$

## 20.25. Dependencia de la numeración y del representante

### Proposición 20.25.1 — Dependencia de la numeración y del representante {#tlog-pro-00133}

**Proposición.** Un punto fijo se construye respecto de una numeración G y de una fórmula objetivo A determinadas. La igualdad de extensiones estándar de dos predicados, o la equivalencia alfa de dos sentencias, no autoriza por sí sola a conservar todos los códigos y bicondicionales al cambiar esa elección.

**Prueba.** El numeral en la ecuación es el código literal del árbol finalmente construido. Cambiar nombres ligados cambia el árbol y, por inyectividad, puede cambiar su código; la equivalencia alfa preserva satisfacción y equivalencia demostrable de la sentencia, pero no la igualdad de los dos naturales. Una traducción de códigos requeriría un procedimiento y una representación propios, y después una prueba de la ecuación transportada.

Si PA prueba equivalencia uniforme de los predicados, §20.17 sí permite conservar un **punto fijo concreto y su código**. Si sólo se sabe que los predicados coinciden en el modelo estándar, se obtiene como máximo el transporte semántico allí. Por tanto la selección de $Prov_{PA}$, la codificación de secuencias y la totalización de funciones sintácticas se mantienen explícitas al entrar en CH21. $\square$

## 20.26. Hipótesis de teorías y obligaciones de la Parte V

### Definición 20.26.1 — Hipótesis de teorías y obligaciones de la Parte V {#tlog-def-00148}

Para las aplicaciones posteriores, una teoría aritmética T será una extensión deductiva de PA en $L_A$, con una presentación de sus axiomas adicionales indicada expresamente cuando se exija efectividad. Distinguimos las siguientes propiedades **externas**, sin atribuirlas automáticamente a T:

- **Consistencia:** T no demuestra la contradicción fija $0=S0$. En una extensión clásica de PA equivale a no demostrar una fórmula y su negación: PA refuta esa igualdad, y las reglas proposicionales permiten explosión desde cualquier par contradictorio.
- **Corrección estándar:** toda sentencia demostrable en T es satisfecha por $\mathbb N_A$.
- **Corrección Σ1:** toda sentencia Σ1 demostrable en T es satisfecha por $\mathbb N_A$; no se incluyen aquí todas las sentencias por definición.
- **ω-consistencia:** no hay fórmula C(x), con sólo x libre, tal que T demuestre $\exists x C(x)$ y demuestre $\neg C(\bar n)$ para cada natural externo n. Los posibles parámetros ya están sustituidos por términos cerrados antes de aplicar esta definición.
- **Presentación efectiva:** la relación externa de axioma adicional es decidible-RM o semidecidible-RM, según se declare; son requisitos distintos. Se usará la certificación de pruebas apropiada al segundo caso.

La consistencia así definida es una propiedad metateórica; no se fija todavía una fórmula objeto de consistencia. Las relaciones entre estas hipótesis y las conclusiones de incompletitud se demostrarán en CH21, y la fórmula interna y condiciones de derivabilidad en CH22. El contrato de salida no introduce resultados pendientes como axiomas. Registra estas obligaciones:

| Frente | Disponible | Obligación pendiente |
|---|---|---|
| CH21, primer teorema | puntos fijos; verificador efectivo; representación de pruebas | declarar la clase de teorías y las hipótesis de consistencia/corrección; probar por separado cada conclusión de no demostrabilidad e independencia |
| Variante Rosser | lector de pruebas y aritmética de orden | construir la comparación de pruebas y probar sus dos direcciones bajo las hipótesis apropiadas |
| CH22, segundo teorema | $Prov_{PA}$ fijo y punto fijo | demostrar las condiciones internas de derivabilidad del representante elegido; fijar la fórmula de consistencia y probar el argumento interno |
| Verdad aritmética | satisfacción externa de fórmulas concretas | ningún predicado aritmético uniforme de verdad aprobado; cualquier resultado de indefinibilidad necesita su propia hipótesis y prueba |
| CH23, indecidibilidad | computabilidad RM y teoremas semidecidibles | demostrar las reducciones y sus hipótesis; no confundir semidecisión con decisión |
| ZF objeto / GAS | lenguajes y estados separados | interpretación y transferencias expresas, sin consistencia o modelos de ZF objeto presumidos; interfaces intertratados siguen0 |
| Formalización | pruebas humanas y candidatos seleccionados | ningún resultado TLOG compilado/verificado en Lean; elaborar certificados formales antes de cambiar ese estado |

Una afirmación metateórica de corrección PA no es una prueba PA de reflexión. Una instancia numeral de representación no es una prueba uniforme de totalidad interna. No se ha demostrado equivalencia RM–Turing ni se necesita para cerrar esta parte.

## 20.27. Cierre de diagonalización y de la Parte IV

### Corolario 20.27.1 — Cierre de diagonalización y de la Parte IV {#tlog-cor-00033}

**Corolario de cierre.** CH17–CH20 suministran el sistema operacional RM, codificaciones efectivas de expresiones/programas/derivaciones, una teoría aritmética PA con representación de cálculos y verificadores, y los lemas diagonales simple, con parámetros y simultáneo finito. La Parte IV puede cerrarse respecto de la arquitectura aprobada sin resolver las obligaciones matemáticas de la Parte V.

**Prueba.** CH17 demuestra las operaciones y la composición operacional; CH18 fija S/G, decodificadores, sustitución y pruebas originales/certificadas, y el ejecutor universal parcial; CH19 construye los representantes aritméticos; §§20.8–20 producen los puntos fijos y sus procedimientos externos. En cada interfaz se conserva la codificación fijada y se explicitan las guardas y niveles. Las obligaciones de §20.26 no son utilizadas como proveedores deductivos: son tareas posteriores. Ninguna dependencia hacia un nodo futuro se añade al DAG. La clausura de la parte no afirma completitud de la teoría objeto ni verificación formal de las pruebas humanas. $\square$

## 20.28. Ejemplos y lectura del cierre

Para A(z)=(0=0), la coordenada z es vacua. El compilador todavía construye una sentencia diagonal, pero una sentencia fija sencilla es0=0. También lo es (0=0)∧(0=0): ambas satisfacen el bicondicional y sus códigos son distintos. Para A(z,w)=(w=w), el punto fijo paramétrico conserva w libre, y el numeral de su código abierto permanece fijo al particularizar w.

Para A(z)=¬Prov_PA(z), obtenemos la equivalencia de §20.23. Esa equivalencia es el insumo sintáctico que utilizará CH21. Para dos objetivos mutuamente referidos se usa el **código de la lista auxiliar entera**: sustituir el código individual de cada componente rompería las ecuaciones demostradas en §20.20.

| Salida | Qué queda probado |
|---|---|
| Sentencia fija | bicondicional PA con el numeral de su código literal |
| Familia con parámetros | mismos parámetros libres y código del árbol abierto |
| Familia simultánea finita | r ecuaciones con los r códigos de sus resultados |
| Compilador externo | terminación sobre códigos válidos;0 en entradas inválidas |
| Obtención de prueba | búsqueda total en esta familia de teoremas ya demostrados |
| Interpretación estándar | satisfacción del bicondicional por corrección externa |
| Parte V | hipótesis y pruebas de incompletitud, derivabilidad interna e indecidibilidad pendientes |

El capítulo cierra **27/27 resultados** y añade **110 aristas directas**. La Parte IV cierra sus cuatro capítulos aprobados. Acumulado: **561 resultados / 2069 aristas**, sin ciclos, duplicados ni huérfanos; **232 candidatos Lean /0 verificados**. Partes cerradas4/5; capítulos publicados0; interfaces activas0. Las pruebas humanas, regresiones de referencia y certificado de bytes se auditan por separado.

```text
LOCAL  CH20 ████████████████████ 27/27 resultados (100 %)
GLOBAL TLOG █████████████████████░░░ 21/24 capítulos (87,50 %)
```

Próximo capítulo: **CH21 — Primer teorema de incompletitud**, dentro de la Parte V — Incompletitud y cierre lógico-formal.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 19](capitulo-19.md) · [Capítulo 21 →](capitulo-21.md)


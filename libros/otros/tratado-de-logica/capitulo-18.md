---
title: Capítulo 18 — Codificación efectiva de expresiones y derivaciones
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
content-id: MA-BCH-0220
content-type: book-chapter
source-id: TLOG-CH18-0001
prerequisites:
- MA-BCH-0202
- MA-BCH-0205
- MA-BCH-0207
- MA-BCH-0208
- MA-BCH-0211
- MA-BCH-0219
related:
- MA-BOK-0014
source-sha256: 932ac3b04f411178561df43d6ba43f727aa9a896929b8a0e21712ab826ca5a84
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 17](capitulo-17.md) · [Capítulo 19 →](capitulo-19.md)

## 18.0. De una expresión finita a un dato operacional

El Capítulo 17 ya está cerrado. Sus programas fijos permiten operaciones numéricas, pero todavía no justifican que una máquina reconozca una fórmula recibida como dato. El capítulo construye ese puente de forma explícita. Una expresión como objeto de ZF, su código natural y su interpretación en una estructura serán tres cosas distintas. Las signaturas arbitrarias de la Parte II no se convierten automáticamente en presentaciones efectivas.

Comenzaremos con datos de presentación, construiremos pares y secuencias con decodificación comprobable, y codificaremos tanto cadenas de tokens como árboles sintácticos. Las pruebas de terminación incluirán entradas inválidas; los ejemplos nularios y los cuantificadores conservarán la gramática canónica del Capítulo 5. Tras las operaciones sintácticas, se construyen verificadores de derivaciones con y sin certificados; tener un código de fórmula no basta por sí solo para reconocer una prueba.

Los metadatos comunes de este bloque son: capa meta; fundamento ZF clásica externa; sin elección; infinitud y recursión metateórica sobre naturales; testigos RM finitos y fijados, sin presuponer universalidad (se construye en §18.52). Los programas de signatura son hipótesis explícitas. Las pruebas siguientes son reconstrucciones propias sobre los resultados internos citados, sin nueva colación bibliográfica ni importación de teoremas externos. Las regresiones computacionales se registrarán separadamente de la prueba humana y de Lean.

## 18.1. Tres niveles y alcance de la efectividad

### Convención 18.1.1 — Tres niveles y alcance de la efectividad {#tlog-cnv-00027}

Todo este bloque vive en $M_{ext}=\mathrm{ZF}$ con lógica clásica, sin AC/BPI. $\mathrm{ZF}_{obj}$ es una teoría estudiada, no la fuente de validez del razonamiento metateórico. RM es el sistema operacional de §17, no una estructura que modele ZF. Se fija una presentación de la signatura y un número finito de programas testigo; cada construcción RM incorpora esos programas por compilación de programas **fijos**.

«Computable» significará computable-RM en entradas y salidas naturales. Para un objeto abstracto no presentado numéricamente sólo se afirmará existencia de una codificación conjuntista. No se introduce computabilidad de una función que reciba tokens abstractos en registros. Las afirmaciones de efectividad se refieren a los representantes numéricos de dichos tokens. No se presupone consistencia, modelo ni interpretación estándar de $\mathrm{ZF}_{obj}$.

## 18.2. Presentación efectiva de un alfabeto

### Definición 18.2.1 — Presentación efectiva de un alfabeto {#tlog-def-00118}

Una presentación efectiva de un conjunto de tokens $A$ es una terna $(D,\rho,P_D)$: $D\subseteq\omega$, $\rho:D\to A$ una biyección metateórica fijada, y $P_D$ un programa RM total que calcula $\chi_D$. El representante de $a\in A$ es $\rho^{-1}(a)$. Igualdad de tokens representados significa igualdad de naturales; $D=\varnothing$ permite el alfabeto vacío. No se exige que una máquina evalúe $\rho$ sobre un registro: su codominio abstracto no es un registro.

Una enumeración calculable de un conjunto **ya representado** de naturales es un programa total $e:\omega\to\omega$ cuya imagen es ese conjunto; el vacío no admite tal enumeración total. Esta definición no equivale a una presentación con dominio decidible ni se deduce de una biyección abstracta con $\omega$. Tampoco se identifica aquí enumeración total con dominio de parada: esa equivalencia queda pendiente.

## 18.3. Presentación efectiva de una signatura

### Definición 18.3.1 — Presentación efectiva de una signatura {#tlog-def-00119}

Para la signatura $\tau=((F_n)_n,(R_n)_n)$ se fijan dominios decidibles $D_F,D_R\subseteq\omega$ y biyecciones $\rho_F:D_F\to\bigcup_nF_n$, $\rho_R:D_R\to\bigcup_nR_n$. No se exige $D_F\cap D_R=\varnothing$: las etiquetas de categoría separan ambos espacios. Se suministran programas RM totales $a_F,a_R:\omega\to\omega$ con $a_F(j)=n$ si $\rho_F(j)\in F_n$, y análogamente para relaciones. Fuera del dominio correspondiente se fija el valor $0$.

Las variables son exactamente los tokens $x_i$ de §5.3, con representante $i$. Los once tokens lógicos/separadores de ese apartado tendrán una tabla finita. Los dominios y programas son **datos de la presentación**, no consecuencias de que $\tau$ sea numerable. Todas las conclusiones de reconocimiento se relativizan a una presentación fijada con estos testigos. Las signaturas arbitrarias de capítulos anteriores conservan su legitimidad, pero no reciben por ello un decidor RM.

## 18.4. Comparaciones y bucles numéricos compilables en RM

### Lema 18.4.1 — Comparaciones y bucles numéricos compilables en RM {#tlog-lem-00061}

**Lema.** Son realizables por programas RM fijos la igualdad, el orden, la resta truncada y el siguiente esquema de control: bucles finitos que usan copias, incrementos, decrementos, pruebas de cero y llamadas a un número finito de programas fijos ya certificados totales.

**Prueba constructiva.** Para comparar $a,b$ se copian a $A,B$ y se decrementan juntos mientras ambos sean positivos. Si se agotan simultáneamente hay igualdad; si se agota sólo $A$, $a<b$; si sólo $B$, $b<a$. Se comprueba el cero mediante $\mathtt{DECJZ}$ y se restaura con un incremento el registro que esa prueba haya decrementado. El ciclo conjunto reduce $A+B$; para $a\dotminus b$ se devuelve el resto de $A$. Las entradas originales se preservan por copia conservativa. El control de las tres salidas y la normalización a $0,1$ son finitos.

Para un bucle acotado, se carga una copia de la cota, se decrementa una vez por iteración y se sale al cero. Para un bucle con variante natural estrictamente decreciente, el buen orden metateórico de $\omega$ prueba terminación; no se confunde esta justificación con una decisión interna de cualquier predicado. Cada llamada a un programa fijo se relocaliza en un banco finito y se compila conforme al §17.27. Un número variable de iteraciones reutiliza **los mismos** registros y etiquetas; no requiere crear registros dinámicos. Todo programa así obtenido es finito y contiene sólo HALT, INC y DECJZ. El esquema no autoriza ejecutar un programa cuyo código variable sea dato de entrada. $\square$

## 18.5. Numerabilidad y presentación efectiva no se identifican

### Proposición 18.5.1 — Numerabilidad y presentación efectiva no se identifican {#tlog-pro-00116}

**Proposición.** Toda presentación efectiva proporciona una inyección del conjunto presentado en $\omega$; la sola exhibición de una inyección no proporciona programas de reconocimiento o de aridad para esa presentación. Toda signatura finita provista de una lista sin repetición y su tabla finita de aridades admite una presentación efectiva.

**Prueba.** La inversa de $\rho$ es la inyección requerida. Una inyección arbitraria sólo especifica un subconjunto de naturales como imagen y una función conjuntista de aridad sobre él; ninguna instrucción RM ni certificado de terminación figura entre esos datos. Esta es una distinción de requisitos, **no** la afirmación de que exista un conjunto numerable sin ninguna presentación efectiva abstracta. En el caso finito, numeramos las funciones y relaciones por segmentos iniciales separados, y usamos comparación con la longitud de cada lista y una tabla de casos finita para las aridades. Los programas de comparación se construirán en §18.4. No se usa elección: las listas se han dado como parámetros. $\square$

## 18.6. Emparejamiento numérico con imagen explícita

### Definición 18.6.1 — Emparejamiento numérico con imagen explícita {#tlog-def-00120}

Fijamos $p:\omega^2\to\omega$ mediante
$$
p(a,b)=(a+b)^2+a.
$$
Su imagen se denota $D_p$. No se declara una biyección con todo $\omega$. Un decodificador devolverá una bandera de validez y dos componentes; ante un código inválido devolverá bandera $0$ y componentes $0,0$. Las tres salidas son tres funciones naturales totales, implementables por programas separados, evitando presumir una salida RM multirregistro como definición oficial.

## 18.7. Inyectividad y decodificación efectiva del par

### Lema 18.7.1 — Inyectividad y decodificación efectiva del par {#tlog-lem-00062}

**Lema.** $p$ es inyectiva, $D_p$ es decidible-RM, y sus proyecciones extendidas por cero son totales computables-RM. Además $a,b\le p(a,b)$.

**Prueba.** Si $s=a+b$, $s^2\le p(a,b)\le s^2+s<(s+1)^2$. Los intervalos correspondientes a distintos $s$ son disjuntos. Dentro del intervalo, $a=p(a,b)-s^2$ y $b=s-a$, lo que prueba inyectividad. Para cualquier $z$, partimos de $s=0,u=0,d=1$; mientras $u+d\le z$, sustituimos $u$ por $u+d$, $s$ por $s+1$ y $d$ por $d+2$. El invariante es $u=s^2$, $d=2s+1$. Cada vuelta aumenta $u$ y la prueba siguiente permanece acotada por $z$; a lo sumo $z$ vueltas. Al salir, $s^2\le z<(s+1)^2$. Calculamos $r=z-u$ y aceptamos exactamente si $r\le s$, devolviendo $a=r,b=s-r$. Cada operación está compilada por §18.4; no se usa raíz cuadrada como primitiva.

Si $s=0$, ambos componentes y el código son cero. Si $s\ge1$, $a,b\le s\le s^2\le p(a,b)$. La cota también vale sobre cada par aceptado por el decodificador. $\square$

## 18.8. Codificación de secuencias finitas y tuplas

### Definición 18.8.1 — Codificación de secuencias finitas y tuplas {#tlog-def-00121}

Definimos $S:\omega^{<\omega}\to\omega$ por
$$
S(\langle\rangle)=0,\qquad
S(\langle a\rangle\mathbin{{}^\frown}s)=1+p(a,S(s)).
$$
La recursión es sobre la longitud de una secuencia **metateórica** finita. Su imagen es $D_S$. Una $k$-tupla se codifica por esta misma función con longitud exactamente $k$; la tupla nularia tiene código $0$. No se confunde esta codificación con pares conjuntistas de la teoría objeto, ni se presume representabilidad interna de su gráfica.

## 18.9. Decodificación terminante y reconocimiento de secuencias

### Metateorema 18.9.1 — Decodificación terminante y reconocimiento de secuencias {#tlog-mth-00083}

**Metateorema.** $S$ es inyectiva y $D_S$ es decidible-RM. Hay una decodificación única y finita de todo código aceptado. Para cada secuencia no vacía, cada entrada y cada cola propia tiene código o valor estrictamente menor que el código completo.

**Prueba.** Dado $c$, si $c=0$, devolvemos la lista vacía. Si $c>0$, decodificamos $c-1$ mediante $p$; si falla, rechazamos. Si da $(a,t)$, emitimos $a$ y continuamos con $t$. Por §18.7, $a,t\le c-1<c$. La variante es el código residual, y decrece en cada vuelta positiva; se llega a cero o al primer fallo. Para una entrada inválida también se termina. La lista recuperada es finita y al recomponerla desde el final se obtiene $c$ por la ecuación de §18.8; por tanto aceptar equivale a pertenecer a la imagen, sin falsos positivos.

Recíprocamente, sobre $S(s)$ cada iteración recupera exactamente la cabeza y el código de la cola, por unicidad del par. Inducción en la longitud muestra recuperación completa. Dos secuencias con igual código son ambas vacías, o tienen cabezas y colas iguales, y la inducción concluye que coinciden. Las cotas estrictas se propagan por cada cola; así valen también para entradas posteriores. Un decidor RM conserva sólo el residual y una bandera, no una lista de longitud variable en registros distintos. La decodificación como lista es una descripción metateórica; sus consultas numéricas se materializan en §18.10. $\square$

## 18.10. Operaciones efectivas sobre secuencias codificadas

### Proposición 18.10.1 — Operaciones efectivas sobre secuencias codificadas {#tlog-pro-00117}

**Proposición.** Sobre códigos válidos, longitud, consulta de posición, reversión y concatenación son computables-RM. Las consultas fuera de rango y las entradas inválidas tienen salida $0$, acompañada, cuando importe distinguirla de un valor legítimo, por una función característica de validez. Para cada $k$ fijo, ser código de $k$-tupla es decidible-RM.

**Prueba por construcción.** Primero se valida la entrada con §18.9. La longitud cuenta las extracciones hasta cero. La consulta decrementa una copia de $i$ a cada extracción hasta hallar la posición $i$; si la lista se agota, da bandera cero. No basta interpretar salida cero como error, pues cero es una entrada legítima.

Para revertir, se inicia $v=0$ y por cada cabeza $a$ se hace $v:=1+p(a,v)$. Para concatenar los códigos de $s,t$, se extrae la reversión de $s$ y se antepone cada cabeza al acumulador inicial $S(t)$; el resultado es $S(s\mathbin{{}^\frown}t)$. Los acumuladores pueden crecer pero los residuales de los bucles decrecen; no hay una hipótesis de cota pequeña de memoria. Son un número fijo de registros que almacenan naturales de tamaño arbitrario. La prueba del resultado se hace por inducción en el número de cabezas procesadas. Validar longitud $k$ consiste en validar y comparar el contador con $k$. La construcción de una tupla de aridad fija son $k$ aplicaciones finitas de $1+p$ desde el último componente, incluso $k=0$. $\square$

## 18.11. Tokens numéricos y códigos de expresiones

### Definición 18.11.1 — Tokens numéricos y códigos de expresiones {#tlog-def-00122}

La tabla lógica es $0=\neg$, $1=\land$, $2=\lor$, $3=\to$, $4=\leftrightarrow$, $5=\forall$, $6=\exists$, $7={=}$, $8=\mathtt{(}$, $9=\mathtt{)}$, $10=\mathtt{,}$. Los códigos de tokens son
$$
V(i)=S([0,i]),\quad F(j)=S([1,j]),\quad R(j)=S([2,j]),\quad L(k)=S([3,k]).
$$
Se exige $j\in D_F$ para $F(j)$, $j\in D_R$ para $R(j)$ y $k\le10$ para $L(k)$. El código de una expresión $w=\langle a_0,\ldots,a_{m-1}\rangle$ es $W(w)=S([\nu(a_0),\ldots,\nu(a_{m-1})])$, donde $\nu$ usa las cuatro categorías. La cadena vacía se codifica por cero. Este es un código de **cualquier expresión**; todavía no exige buena formación como término o fórmula. Las tablas $V,F,R,L$ codifican tokens; no son los códigos de árboles de §18.13 aunque puedan coincidir numéricamente entre espacios distintos.

## 18.12. Reconocimiento e inyectividad de expresiones

### Proposición 18.12.1 — Reconocimiento e inyectividad de expresiones {#tlog-pro-00118}

**Proposición.** Los tokens válidos y la imagen de $W$ son decidibles-RM; $\nu$ y $W$ son inyectivos como funciones conjuntistas sobre tokens y expresiones. La reconstrucción de representantes numéricos es efectiva.

**Prueba.** Decodificamos el token como una secuencia de longitud exactamente dos. La primera entrada debe ser $0,1,2$ o $3$; la segunda pasa respectivamente el control trivial de natural, el decidor $D_F$, el decidor $D_R$ o la cota $10$. El decidor de expresiones valida la secuencia externa y recorre todas sus cabezas con este control. Los programas testigo de la signatura están incorporados como subprogramas fijos; §18.9 garantiza que el recorrido es finito. Igualdad de códigos de tokens obliga a igualdad de etiqueta e índice, y las biyecciones fijadas identifican el token abstracto. Igualdad de $W$ obliga a igual longitud e iguales tokens en cada posición. Recuperar los nombres abstractos a través de $\rho$ es una operación metateórica; el procedimiento RM devuelve y compara índices. No se ha decidido todavía si la expresión es una fórmula. $\square$

## 18.13. Códigos de árboles sintácticos de primer orden

### Definición 18.13.1 — Códigos de árboles sintácticos de primer orden {#tlog-def-00123}

Escribimos $G$ para el código de árbol, definido por recursión estructural sobre los constructores canónicos, con las siguientes once etiquetas:

| Constructor | Código $G$ |
|---|---|
| $x_i$ | $S([0,i])$ |
| $f_j(t_0,\ldots,t_{n-1})$ | $S([1,j,S([G(t_0),\ldots,G(t_{n-1})])])$ |
| $(t=u)$ | $S([2,G(t),G(u)])$ |
| $R_j(t_0,\ldots,t_{n-1})$ | $S([3,j,S([G(t_0),\ldots,G(t_{n-1})])])$ |
| $(\neg\varphi)$ | $S([4,G(\varphi)])$ |
| $(\varphi\land\psi)$ | $S([5,G(\varphi),G(\psi)])$ |
| $(\varphi\lor\psi)$ | $S([6,G(\varphi),G(\psi)])$ |
| $(\varphi\to\psi)$ | $S([7,G(\varphi),G(\psi)])$ |
| $(\varphi\leftrightarrow\psi)$ | $S([8,G(\varphi),G(\psi)])$ |
| $(\forall x_i\,\varphi)$ | $S([9,i,G(\varphi)])$ |
| $(\exists x_i\,\varphi)$ | $S([10,i,G(\varphi)])$ |

El índice $j$ debe pertenecer al dominio funcional/relacional correspondiente y la lista de argumentos debe tener longitud $a_F(j)$/$a_R(j)$. Para aridad cero se usa lista vacía, de código $0$. La función $G$ conserva el índice de la variable ligada: no pasa a clases alfa ni convierte $\exists$ en una abreviatura de $\forall$. Su existencia/unicidad conjuntista procede de los recursores de §6, no de una máquina universal. Los tags tienen significado sólo en el espacio de árboles; un natural aislado carece de tipo intrínseco.

## 18.14. Descenso estricto de los códigos de hijos

### Lema 18.14.1 — Descenso estricto de los códigos de hijos {#tlog-lem-00063}

**Lema.** En toda descomposición de un posible código de árbol que supere las guardas locales de §18.13, los códigos de cada hijo requerido son estrictamente menores que el código de su padre, aun cuando alguno de esos hijos sea sintácticamente inválido.

**Prueba.** Para igualdad, conectivos, negación y cuantificadores, cada hijo es una entrada de la secuencia exterior no vacía; §18.9 da la desigualdad estricta. Para aplicación o relación, la lista de argumentos tiene código $l<c$, y cada entrada $d$ de una lista no vacía satisface $d<l$, luego $d<c$. Una lista vacía no impone hijos. La desigualdad no usa una hipótesis de buena formación de los hijos, sólo las validaciones de las secuencias locales. En particular un nodo no puede ser su propio hijo ni participar en una cadena circular de hijos; toda rama descendente tiene longitud a lo sumo el código inicial. $\square$

## 18.15. Inyectividad y decodificación fiel de términos y fórmulas

### Metateorema 18.15.1 — Inyectividad y decodificación fiel de términos y fórmulas {#tlog-mth-00084}

**Metateorema.** $G$ es inyectiva en la unión disjunta de términos y fórmulas canónicos. La recuperación desde su imagen conserva exactamente los símbolos, las aridades, la ligadura nominal y todos los constructores primitivos.

**Prueba.** Decodificamos la secuencia exterior y su tag. Tags $0,1$ corresponden a términos; los demás a fórmulas. Un mismo tag fija una única longitud exterior, un único índice de símbolo o variable cuando lo haya y la misma lista ordenada de hijos. Por inducción fuerte en el código compartido, §18.14 permite recuperar cada hijo de forma única; en el caso de función/relación, la decodificación de la lista interior da la misma longitud y los mismos códigos de hijos. Los índices identifican los tokens por las biyecciones de la presentación. Reensamblamos los constructores de §5 con su escritura canónica: $f()$, $R()$, $(t=u)$, $(\neg\varphi)$, $(\varphi\circ\psi)$ y $(Qx_i\varphi)$, incluyendo paréntesis y sin token de espacio. La legibilidad única de §5 identifica la cadena recuperada con la original. La inducción también prueba que codificar el objeto recuperado devuelve el código inicial.

No se eliminan paréntesis arbitrarios ni se aceptan abreviaciones editoriales como cadenas nuevas. $\forall x_0(x_0=x_0)$ y $\forall x_1(x_1=x_1)$ tienen códigos distintos aunque sean alfa equivalentes; igualdad de árboles es literal, no equivalencia semántica. $\square$

## 18.16. Decidibilidad RM de códigos de términos y fórmulas

### Metateorema 18.16.1 — Decidibilidad RM de códigos de términos y fórmulas {#tlog-mth-00085}

**Metateorema.** Para la presentación efectiva fijada, las imágenes $D_{Tm}=G[\operatorname{Tm}_\tau]$ y $D_{Fm}=G[\operatorname{Fm}_\tau]$ son decidibles-RM sobre **todos** los naturales.

**Programa de reconocimiento.** Se usa una pila codificada por $S$ de tareas $S([b,c])$, con $b=0$ para término y $b=1$ para fórmula. Inicialmente contiene sólo la tarea de la raíz. Mientras no esté vacía, se extrae una tarea, se valida el código $c$ como secuencia y se controla exactamente su tag y longitud exterior. En modo término sólo se permiten variable de longitud dos y aplicación de longitud tres; en aplicación se consulta $D_F,a_F$ y se valida la lista interior y su longitud exacta. En modo fórmula se controlan: igualdad con dos hijos término; relación con lista de hijos término y $D_R,a_R$; negación con un hijo fórmula; cada binario con dos hijos fórmula; cuantificador con un índice natural y un hijo fórmula. Una guarda fallida devuelve $0$. Los hijos se apilan con su tipo requerido. Una pila vacía sin fallo devuelve $1$. Se prohíben campos adicionales y se rechaza $c=0$ como árbol.

**Terminación y compilación.** Cada paso local usa sólo extracciones/consultas de secuencias, pruebas numéricas y programas de signatura ya totales. La creación de tareas usa un número fijo de acumuladores, no un registro por nodo. Por inducción fuerte en $c$, el árbol de tareas potenciales de la raíz es finito: las guardas fallidas terminan en una hoja, y en una guarda superada hay una lista finita de hijos con códigos menores que $c$ por §18.14. Para la pila, el invariante es una lista finita de tareas aún no visitadas de ese árbol; procesar una tarea consume una visita y sólo agrega sus hijos. Por tanto la profundidad primero visita un número finito de tareas incluso sobre códigos inválidos. No se usa como variante el tamaño numérico de la pila, que puede aumentar. Push/pop y recorridos interiores están realizados por §18.10; el control tiene once casos fijos y los programas de presentación están incrustados por §18.4. Así se obtiene un programa RM finito, no un intérprete de programas variables.

**Exactitud.** Una ejecución que acepta proporciona un árbol finito cuyas hojas son variables o símbolos nularios admitidos y cuyos nodos satisfacen las cláusulas de §5; inducción desde las hojas produce un término/fórmula cuyo código es la entrada. Recíprocamente, inducción estructural sobre cualquier término/fórmula muestra que todas las guardas y tareas pasan. El tipo de cada hijo se comprueba, de modo que $\neg x_0$ y una función aplicada a una fórmula se rechazan. La variable ligada no precisa aparecer en la matriz ni ser distinta de variables ligadas interiores. $\square$

## 18.17. Conversión efectiva entre cadenas canónicas y árboles

### Proposición 18.17.1 — Conversión efectiva entre cadenas canónicas y árboles {#tlog-pro-00119}

**Proposición.** Hay procedimientos RM totales con bandera de éxito para convertir $W$ de una cadena canónica de término/fórmula a su $G$ y, en sentido inverso, $G$ a $W$ de la cadena canónica. Las dos conversiones son inversas en sus dominios válidos; por consiguiente la buena formación de cadenas canónicas es decidible-RM. No se afirma todavía que sea computable la sustitución.

**Prueba constructiva.** Tras validar los tokens, analizamos tareas de segmentos finitos con tipo término/fórmula. Un término es una variable única, o un token funcional seguido por paréntesis exteriores que cierran exactamente al final; sus argumentos se separan por comas a profundidad uno, se cuenta su número y se compara con la aridad. Para fórmulas, un token relacional exige su lista de argumentos del mismo modo. Si empieza por paréntesis, se exige cierre exterior al final: un token siguiente $\neg$ o $Q$ selecciona negación o cuantificación, y en el segundo caso el token inmediato siguiente debe ser variable. En los demás casos se buscan separadores a profundidad uno: exactamente un signo de igualdad produce dos tareas término, y exactamente un conectivo binario produce dos tareas fórmula. Cualquier conflicto, coma impropia, cierre anticipado, segmento vacío o token residual se rechaza. Estas reglas cubren también la igualdad cuyo término izquierdo empieza por función y los binarios cuyo operando izquierdo es una relación nularia. Los paréntesis de las listas internas se cuentan en el recorrido; no se confunde un separador de profundidad mayor con el de la raíz.

Las tareas, listas de segmentos y marcadores de retorno se guardan como secuencias numéricas en pilas. Cada hijo de análisis es un segmento estrictamente más corto; el árbol de llamadas es finito por inducción en la longitud de la cadena, independientemente de que sea válida. Cada recorrido examina como máximo esa longitud y las consultas son las de §18.10. Al volver de los hijos, el marcador guarda el tag y los hijos ya calculados para construir la tupla de §18.13. Es un evaluador de esta gramática fija con marcadores finitos, compilable por §18.4; el valor de aridad determina una lista codificada, no la cantidad de registros del programa. Ninguna llamada se delega a una máquina universal.

Para imprimir se valida $G$ por §18.16 y se recorre su árbol con pila de marcadores: se añaden códigos de tokens de apertura, operador, nombre, separador y cierre en el orden de §5, usando concatenación de secuencias. La finitud se prueba por §18.14 y cada nodo genera una lista finita. La inducción sobre el árbol y la legibilidad única muestran las dos identidades de conversión. El código $0$ de una cadena vacía es una expresión válida, pero ambas modalidades sintácticas la rechazan. Un código que sea a la vez token y árbol sólo se procesa con el espacio de entrada declarado, nunca por inferencia implícita de tipo. $\square$

## 18.18. Frontera entre sintaxis efectiva, semántica y prueba

### Corolario 18.18.1 — Frontera entre sintaxis efectiva, semántica y prueba {#tlog-cor-00027}

**Corolario de alcance.** Quedan cerradas numeraciones inyectivas de expresiones, términos y fórmulas, con reconocimiento y conversión efectivos relativos a la presentación declarada. Ninguno de esos decidores consulta una estructura, una asignación, una teoría de axiomas ni una derivación.

**Prueba.** Los únicos controles de §§18.12, 18.16–17 son etiquetas, índices, aridades, listas finitas y reglas de formación. Sus entradas y subprogramas no incluyen datos semánticos o de demostrabilidad. Por ello las conclusiones son exactamente pertenencia a imágenes sintácticas; no entrañan una decisión de verdad, consecuencia o existencia de prueba. Esto no niega los teoremas previos de corrección/completitud, sino que evita atribuir al reconocimiento sintáctico una función distinta de la demostrada. $\square$

**Obligaciones históricas al cerrar M01, descargadas en M02/M03.** Codificación numérica de programas/configuraciones RM y trazas con guardas; algoritmos de variables libres, renombrado y sustitución con prevención de captura; reconocimiento de instancias de los esquemas HFOL= y sus prefijos de generalización; codificación de líneas de prueba con índices de referencias precedentes; decidor de una derivación finita con premisas dadas, distinguiéndolo de una teoría arbitraria cuyo conjunto de axiomas no tiene por qué ser decidible; selección de hipótesis efectivas para semidecidibilidad de demostrabilidad; máquina universal, si se necesita, con prueba propia. La representabilidad pertenece a CH19; el lema diagonal y la diagonalización a CH20. No se reserva un ID de resultado cerrado para una obligación.

## CH18-M02 — Continuación: operaciones y pruebas certificadas

El registro y el manuscrito vigentes de M01 se recuperaron antes de escribir. Sus 18 resultados se conservan; este bloque añade 20 unidades desde §18.20. La codificación con testigos evita esconder la decisión de condiciones laterales y la reconstrucción de instancias bajo una apelación a «verificar una prueba». Se recuperaron las fuentes canónicas CH03, CH06 y CH09 para conservar exactamente H1–H12, Q1–Q5, E1–E2 y la definición de derivación. No se hace nueva colación de bibliografía externa ni se importa un resultado de otro tratado.

## 18.20. Datos fijados y alcance de la verificación

### Convención 18.20.1 — Datos fijados y alcance de la verificación {#tlog-cnv-00028}

Se conserva la presentación efectiva de $\tau$ aprobada en M01 y sus programas totales de dominio/aridad. Las entradas operacionales son naturales, no tokens abstractos ni estructuras. Las pruebas humanas viven en $M_{ext}=\mathrm{ZF}$ clásica, sin AC/BPI; $\mathrm{ZF}_{obj}$ y RM conservan sus niveles distintos.

En $\mathsf H_\tau^=$ la única regla primitiva es MP. «Generalizar» no se añadirá como tipo de línea: las clausuras universales finitas son axiomas y las reglas admisibles requieren expansión a las derivaciones de §9.7. El nuevo verificador recibe **certificados de instanciación**; su totalidad no presupone decidibilidad de «ser axioma» a partir de la sola fórmula. Las entradas inválidas se rechazan con salida $0$. Cuando una función devuelve un código de objeto, $0$ significa fallo porque ningún término/fórmula tiene código de árbol $0$; para listas vacías válidas se conservará una bandera separada.

## 18.21. Recorridos y reconstrucción de árboles con pilas codificadas

### Lema 18.21.1 — Recorridos y reconstrucción de árboles con pilas codificadas {#tlog-lem-00064}

**Lema de implementación.** Para un número finito de casos de constructor, pueden compilarse en RM recorridos de árboles validados y reconstrucciones posorden que utilizan: tareas con contexto numérico; listas de hijos de aridad variable; y un número fijo de operaciones RM totales sobre resultados y contextos. No se presume un recursor universal ni que toda recursión conjuntista sea efectiva.

**Construcción y prueba.** La pila de trabajo es un código $S$ de registros de tarea; cada registro tiene un tag fijo y campos naturales. Para visitar un nodo se decodifican su tag y campos. Se coloca un marcador de retorno que guarda el constructor, el contexto y la lista de hijos pendiente; se visita el primer hijo, y su resultado se antepone a un acumulador de resultados del marcador. Al completarse los hijos, se revierte ese acumulador para recuperar el orden y se ejecuta la plantilla de reconstrucción. Una hoja devuelve directamente un resultado. Los marcadores y las listas son números en registros fijos, no registros dinámicos ni instrucciones recibidas como dato. Las extracciones, construcción de tuplas, reversión y consultas están implementadas por §18.10. Los subprogramas suministrados se relocalizan y compilan como programas fijos por §18.4.

La validación inicial es total. En el recorrido de un árbol fijo cada tarea consume una visita a un nodo o un avance de una lista finita de hijos; por §18.14 los árboles de entrada son finitos. Cada marcador vuelve una sola vez y tiene tantos avances como hijos, por lo que termina incluso si los resultados reconstruidos son mayores que la entrada. No se requiere que el código numérico de la pila decrezca. Exactitud se prueba por inducción desde hojas: cada marcador recibe precisamente los resultados de sus hijos en el orden original. Las pruebas siguientes especifican sus contextos, operaciones y medida; esta plantilla no dispensa de verificar esos datos. $\square$

## 18.22. Cálculo efectivo de variables y nombres

### Proposición 18.22.1 — Cálculo efectivo de variables y nombres {#tlog-pro-00120}

**Proposición.** Son computables-RM las listas crecientes sin repetición de índices de $\operatorname{Var}(t)$, $\operatorname{FV}(\varphi)$ y $\operatorname{Names}(\varphi)$; es decidible ser sentencia. Se totalizan por lista vacía y bandera $0$ fuera del tipo apropiado.

**Prueba.** En una variable se devuelve $[i]$; en una aplicación funcional se unen las listas de sus argumentos, incluso la lista vacía de un nulario. En igualdad/relación se unen las variables de sus términos. Negación conserva la lista; un binario une las dos. En $Qx_i\psi$, FV elimina $i$ de la lista de la matriz; Names agrega $i$ a los nombres de la matriz. Names de los átomos reúne todas sus hojas de variable. La inserción de un índice en una lista creciente compara entradas hasta hallar su posición o repetición; eliminación y unión recorren listas finitas mediante §18.10 y §18.4. La plantilla de §18.21 calcula estas listas en posorden. La inducción estructural y las ecuaciones de §6.5/18 identifican las salidas con las listas únicas de los conjuntos correspondientes. FV vacía caracteriza ser sentencia por §6.6. No se presupone una igualdad decidible entre objetos no presentados. $\square$

## 18.23. Selección efectiva de la variable fresca canónica

### Proposición 18.23.1 — Selección efectiva de la variable fresca canónica {#tlog-pro-00121}

**Proposición.** Dada una lista numérica finita válida de índices, es computable-RM el mínimo índice ausente, coincidente con $\operatorname{fresh}$ de §6.18 para el conjunto representado.

**Prueba.** Normalizamos por inserción a una lista creciente sin repetición. Con un candidato $k=0$ recorremos la lista: si su siguiente entrada es $k$, avanzamos y aumentamos $k$; si es mayor que $k$, devolvemos $k$; si se agota, devolvemos $k$. La lista normalizada no contiene entradas menores que el candidato ya consumidas. Por inducción, todos los índices menores que $k$ han aparecido y el primero no hallado es el mínimo ausente. A lo sumo se consumen tantas entradas como la longitud de la lista; la entrada vacía devuelve $0$ con bandera de éxito $1$. Ninguna cota en el tamaño del mayor índice ni búsqueda infinita de frescura es necesaria. Los dominios inválidos se rechazan. El programa conserva exactamente la selección mínima anterior, sin sustituirla por «uno más que el máximo» ni usar AC. $\square$

## 18.24. Sustitución numérica efectiva de términos

### Metateorema 18.24.1 — Sustitución numérica efectiva de términos {#tlog-mth-00086}

**Metateorema.** Para índices $i$ y códigos de términos $c,d$, se calcula $G(t[u/x_i])$ cuando $c=G(t),d=G(u)$; sobre entradas de tipos inválidos se devuelve $0$. Esta función totalizada es computable-RM.

**Prueba.** Validamos ambos términos. En una hoja $x_j$ devolvemos $d$ si $j=i$, y su código original en caso contrario. En una aplicación se reconstruye el mismo símbolo con la lista de resultados de sus hijos. El contexto $(i,d)$ se mantiene fijo en las tareas de §18.21. Las copias de $u$ introducidas se devuelven como resultados y **no** generan tareas nuevas: la sustitución afecta simultáneamente a las hojas originales. La terminación usa el árbol original de $t$, no la longitud de la salida. La prueba posorden coincide en cada cláusula con la sustitución de términos de §6.13; conserva todas las aridades, incluidas las constantes. En particular $x_i[x_i/x_i]=x_i$ y una sustitución cuyo término contiene $x_i$ no se itera indefinidamente. $\square$

## 18.25. Decisión numérica de libertad para sustituir

### Metateorema 18.25.1 — Decisión numérica de libertad para sustituir {#tlog-mth-00087}

**Metateorema.** El predicado $\operatorname{FreeFor}(u,x_i,\varphi)$ es decidible-RM en sus códigos, con rechazo si $u$ no es término o $\varphi$ no es fórmula.

**Prueba.** Calculamos la lista $\operatorname{Var}(u)$ una sola vez. Los átomos devuelven $1$; negación pasa el resultado; un binario toma su conjunción. Para $Qx_j\psi$, si $j=i$ devolvemos $1$ sin exigir seguridad en la matriz; si $j\ne i$, devolvemos la conjunción de la seguridad de $\psi$ con «$i\notin FV(\psi)$ o $j\notin\operatorname{Var}(u)$». Las consultas de FV son los programas fijos de §18.22, aunque repitan un recorrido finito; las pruebas de pertenencia recorren listas finitas. Cada tarea propia baja por el árbol original y cada consulta auxiliar termina. Estas cláusulas son exactamente §6.19, y el criterio de §6.20 certifica que detectan captura de ocurrencias libres. Un cuantificador homónimo bloquea la sustitución: no se comprueban arbitrariamente todas las ocurrencias textuales de $x_i$. $\square$

## 18.26. Sustitución literal segura como función efectiva

### Metateorema 18.26.1 — Sustitución literal segura como función efectiva {#tlog-mth-00088}

**Metateorema.** Hay un programa RM total que devuelve $G(\varphi[u/x_i]_{lit})$ si las entradas están tipadas y FreeFor vale, y $0$ en los demás casos.

**Prueba.** Primero se ejecuta §18.25; en fallo no se construye una sustitución insegura. En un átomo se llama al sustituidor de términos en cada argumento; en igualdad se procesan ambos términos, y en un relacional nulario se conserva la lista vacía. Se reconstruyen negación y los cuatro binarios. Para $Qx_j\psi$, si $j=i$ se devuelve el nodo original íntegro; si $j\ne i$ se procesa la matriz y se reconstruye el mismo cuantificador y nombre. El dominio seguro del nodo padre garantiza el de la matriz que se atraviesa; una llamada que queda bajo un cuantificador homónimo no se ejecuta. La pila recorre el árbol original, y las llamadas a término son finitas; no vuelve a sustituir dentro de resultados introducidos. Inducción sobre las cláusulas identifica literalmente la salida con §6.21, sin pasar a equivalencia alfa. Una sustitución vacua devuelve el código original. $\square$

## 18.27. Renombrado fresco y sustitución canónica sin captura

### Metateorema 18.27.1 — Renombrado fresco y sustitución canónica sin captura {#tlog-mth-00089}

**Metateorema.** El paso ligado $Qx_j\psi\mapsto Qx_k\psi[x_k/x_j]_{lit}$ es computable con bandera, bajo $k\notin Names(\psi)\cup\{j\}$. La sustitución canónica $CA_{x_i,u}$ de §6.25 también es computable-RM sobre códigos de fórmulas y términos tipados.

**Prueba.** El paso ligado consulta Names, compara $k,j$ y usa la sustitución literal de §18.26; sólo se cambian la declaración externa y las hojas libres de su matriz. Los cuantificadores homónimos interiores quedan intactos. Se rechaza frescura insuficiente, aunque $k$ no aparezca en FV.

Para CA, átomos y conectivos usan las operaciones anteriores. En $Qx_j\psi$, si $j=i$ o $i\notin FV(\psi)$, se conserva todo el nodo; si $j\ne i$ y $j\notin\operatorname{Var}(u)$, se desciende normalmente. En el caso restante se calcula exactamente el mínimo índice $k$ ausente de $Names(\psi)\cup\operatorname{Var}(u)\cup\{i,j\}$, se renombra la matriz con el paso anterior y se continúa CA sobre esa matriz renombrada, con un marcador para reconstruir $Qx_k$.

Aquí el código de la matriz renombrada puede crecer: **no** se invoca descenso numérico de §18.14 para esta llamada. La medida es el número de constructores de fórmula (incluidos átomos). Un renombrado variable por variable conserva ese número y el rango por §6.24; quitar el cuantificador exterior lo disminuye estrictamente. Negación/binarios descienden a componentes propios; los cálculos de Names, frescura y renombrado son subprogramas totales ya demostrados. Por inducción en esa medida, el árbol de llamadas es finito. Se codifican sus contextos y marcadores como en §18.21; las once ramas de control y el subprograma de renombrado son fijos. La inducción con las tres ramas cuantificadas prueba coincidencia exacta con la selección determinista de §6.25 y conservación de variables libres allí establecida. No se usa sustitución con renombrado para aceptar Q1/Q2/E2: esas instancias requieren la operación **literal**. $\square$

## 18.28. Certificados explícitos de instancias axiomáticas básicas

### Definición 18.28.1 — Certificados explícitos de instancias axiomáticas básicas {#tlog-def-00124}

Un certificado básico es $S([h,S(\bar a)])$, con selector $0\le h\le18$ y la lista de parámetros **exactamente** indicada:

| Selector | Esquema | Parámetros numéricos |
|---|---|---|
| $h=0,\ldots,11$ | H1–H12 | códigos de $\alpha,\beta$, y también $\gamma$ sólo en H2,H9 |
| $12,13$ | Q1,Q2 | $[G(\varphi),i,G(t)]$ |
| $14$ | Q3 | $[G(\varphi),G(\psi),i]$ |
| $15,16$ | Q4,Q5 | $[G(\varphi),i]$ |
| $17$ | E1 | $[G(t)]$ |
| $18$ | E2 | $[G(\varphi),i,G(t),G(u)]$ |

Los parámetros de fórmula/término deben superar los decidores de M01. Los índices de variable son naturales. Se exige FreeFor para Q1/Q2 y ambas sustituciones de E2, y $i\notin FV(\varphi)$ para Q4. Se rechazan listas con parámetros sobrantes o faltantes. El certificado declara los **testigos de instanciación**, no es el código de la fórmula obtenida; puede haber varios certificados para una misma instancia.

## 18.29. Construcción y comprobación de H1–H12

### Lema 18.29.1 — Construcción y comprobación de H1–H12 {#tlog-lem-00065}

**Lema.** Se computa el código de la instancia H indicada por un certificado válido y se decide si una fórmula dada coincide con ella. Las doce plantillas recuperadas son:

| Esquema | Plantilla sobre fórmulas de primer orden |
|---|---|
| H1 | $\alpha\to(\beta\to\alpha)$ |
| H2 | $(\alpha\to(\beta\to\gamma))\to((\alpha\to\beta)\to(\alpha\to\gamma))$ |
| H3 | $(\neg\beta\to\neg\alpha)\to(\alpha\to\beta)$ |
| H4 | $(\alpha\land\beta)\to\alpha$ |
| H5 | $(\alpha\land\beta)\to\beta$ |
| H6 | $\alpha\to(\beta\to(\alpha\land\beta))$ |
| H7 | $\alpha\to(\alpha\lor\beta)$ |
| H8 | $\beta\to(\alpha\lor\beta)$ |
| H9 | $(\alpha\to\gamma)\to((\beta\to\gamma)\to((\alpha\lor\beta)\to\gamma))$ |
| H10 | $(\alpha\leftrightarrow\beta)\to(\alpha\to\beta)$ |
| H11 | $(\alpha\leftrightarrow\beta)\to(\beta\to\alpha)$ |
| H12 | $(\alpha\to\beta)\to((\beta\to\alpha)\to(\alpha\leftrightarrow\beta))$ |

**Prueba.** Se valida la longitud indicada y cada parámetro. Se reconstruye la plantilla mediante los tags de M01, sin transformar conectivos. Como las doce plantillas tienen un número fijo finito de nodos, cada rama es un número fijo de construcciones de $S$; la comparación final es igualdad de naturales. Corrección sigue de la tabla exacta de §3.2 y el levantamiento de §9.2; todo testigo admitido por esos esquemas se serializa como un certificado de la tabla. El selector no consulta validez proposicional ni una tabla semántica. $\square$

## 18.30. Comprobación efectiva de Q1–Q5 y sus condiciones laterales

### Lema 18.30.1 — Comprobación efectiva de Q1–Q5 y sus condiciones laterales {#tlog-lem-00066}

**Lema.** Los certificados Q se comprueban por programas RM totales con las condiciones laterales exactas del cálculo.

**Prueba.** Tras validar tipos y longitud, para Q1/Q2 se comprueba FreeFor y se calcula $b=G(\varphi[t/x_i]_{lit})$. Se construyen respectivamente $(\forall x_i\varphi)\to b$ y $b\to(\exists x_i\varphi)$. Q3 construye $(\forall x_i(\varphi\to\psi))\to((\forall x_i\varphi)\to(\forall x_i\psi))$ sin condición de frescura; Q4 comprueba que $i\notin FV(\varphi)$ y construye $\varphi\to\forall x_i\varphi$; Q5 construye $(\exists x_i\varphi)\leftrightarrow\neg\forall x_i\neg\varphi$. Los símbolos $\exists$ y $\leftrightarrow$ siguen siendo primitivos.

Las validaciones y sustituciones son totales por §§18.22/25/26. Se acepta una fórmula objetivo sólo si su código coincide literalmente con el resultado. Las cinco construcciones y las guardas son precisamente §9.3, por lo que aceptación equivale a ser la instancia especificada por **esos parámetros**. No se admite un Q1 con captura porque una sustitución CA produzca alguna fórmula alfa equivalente. Tampoco se exige que la variable ligada aparezca libre ni se agrega a Q3 una condición lateral ajena al esquema. $\square$

## 18.31. Comprobación de E1–E2 con sustituciones literales

### Lema 18.31.1 — Comprobación de E1–E2 con sustituciones literales {#tlog-lem-00067}

**Lema.** Los certificados E generan y comprueban exactamente las instancias señaladas de E1/E2, mediante programas RM totales.

**Prueba.** E1 valida $t$ y genera la igualdad $t=t$. E2 valida $\varphi,t,u$ y comprueba las dos condiciones FreeFor. Calcula los códigos literales $b=G(\varphi[t/x_i]_{lit})$, $c=G(\varphi[u/x_i]_{lit})$ y construye $(t=u)\to(b\to c)$, comparando su código con la fórmula objetivo. Cada llamada termina por §§18.25/26. Corrección y cobertura con testigos dados son exactamente §9.4. No se compara el valor semántico de términos ni se requiere $t\ne u$ o una ocurrencia libre de $x_i$ en $\varphi$; las instancias redundantes también son legítimas. Los parámetros latentes de E2 se suministran como certificado: la ausencia de una cota reconstruida desde la fórmula objetivo no se oculta como una búsqueda finita ya demostrada. $\square$

## 18.32. Certificado de axioma con prefijo universal finito

### Definición 18.32.1 — Certificado de axioma con prefijo universal finito {#tlog-def-00125}

Un certificado de axioma completo es $a=S([v,b])$, donde $v=S([i_0,\ldots,i_{m-1}])$ es una lista de índices de variables y $b$ un certificado básico. Su fórmula generada es
$$
\forall x_{i_0}\cdots\forall x_{i_{m-1}}\theta_b.
$$
Se admiten prefijos vacíos, nombres repetidos y variables vacuas. No se exige que el prefijo cuantifique exactamente las variables libres ni que sea creciente. Este es el prefijo de §9.5, no la operación de clausura universal canónica de otro apartado ni una aplicación de una regla Gen.

## 18.33. Decisión de axiomas provistos de certificado

### Proposición 18.33.1 — Decisión de axiomas provistos de certificado {#tlog-pro-00122}

**Proposición.** Existe un programa RM total $\operatorname{AxCert}(a,c)\in\{0,1\}$ que acepta exactamente cuando $a$ es un certificado válido y $c$ es el código de su axioma. Además
$$
c\in G[Ax_{\mathsf H_\tau^=}]
\iff \exists a\in\omega\ \operatorname{AxCert}(a,c)=1.
$$

**Prueba.** Se valida la longitud dos del certificado, la lista $v$ y el certificado básico. Se genera $G(\theta_b)$ por §§18.29–31 y se recorre la reversión de $v$, envolviendo el acumulador en tag $9$ con cada índice. La reversión asegura que el primer índice original quede **más externo**. El bucle disminuye el residual de la lista y termina; se compara el código final con $c$, rechazando un código objetivo que no sea fórmula. La aceptación genera un axioma de §9.5. A la inversa, la definición de ese conjunto proporciona una lista finita y una instancia básica con parámetros finitos que pueden codificarse: ese certificado acepta. Se trata de equivalencia metateórica con un testigo natural, no de cuantificación aritmética representada en $\mathrm{ZF}_{obj}$.

Se ha decidido la relación binaria **certificado/fórmula**. Su proyección existencial no se declara decidible; encontrar un certificado mediante búsqueda no es decidir que ninguno existe. $\square$

## 18.34. Tres clases de líneas certificadas

### Definición 18.34.1 — Tres clases de líneas certificadas {#tlog-def-00126}

Sea $g=S([G(\gamma_0),\ldots,G(\gamma_{r-1})])$ una lista finita de premisas, que puede contener duplicados y ser vacía. Una línea certificada tiene exactamente una de estas formas:

| Forma | Código | Condición en posición $k$ |
|---|---|---|
| Premisa | $S([0,c,j])$ | $j<r$ y $c=G(\gamma_j)$ |
| Axioma | $S([1,c,a])$ | $\operatorname{AxCert}(a,c)=1$ |
| MP | $S([2,c,i,j])$ | $i,j<k$ y la fórmula de línea $j$ es la implicación de la fórmula de $i$ a la de $k$ |

En todos los casos $c\in D_{Fm}$. Los índices comienzan en cero; en MP $i$ refiere al antecedente y $j$ a la implicación. Se permite $i=j$ si la ecuación de códigos llegara a cumplirse, pero ambos deben ser precedentes. No existe un tag para «verdad», «regla derivada», «alfa equivalencia» ni «generalización de hipótesis». Una línea puede disponer de más de una justificación original; el certificado elige una.

## 18.35. Código de derivación certificada y conclusión

### Definición 18.35.1 — Código de derivación certificada y conclusión {#tlog-def-00127}

Una prueba certificada es $d=S([\ell_0,\ldots,\ell_{n-1}])$, una lista **no vacía** de códigos de línea. Su borrado es la lista de los campos fórmula $c_0,\ldots,c_{n-1}$; su conclusión es $c_{n-1}$. Definimos $\operatorname{ProofCert}(g,d,c)$ cuando $g$ es una lista válida de fórmulas, todas las líneas pasan las condiciones de §18.34 en su posición y la conclusión es $c$.

Los contextos y las pruebas se codifican con $S$, las fórmulas con $G$: no se interpretan como cadenas $W$ sin conversión explícita. Un contexto vacío tiene código $0$ y es válido; una lista de prueba vacía tiene también código $0$, pero es **inválida como prueba**. La conclusión nunca se obtiene de una consulta de último elemento sin comprobar no vaciedad.

## 18.36. Decisión total de derivaciones certificadas finitas

### Metateorema 18.36.1 — Decisión total de derivaciones certificadas finitas {#tlog-mth-00090}

**Metateorema.** $\operatorname{ProofCert}\subseteq\omega^3$ es decidible-RM, para la presentación fijada.

**Programa y prueba.** Se valida $g$ como lista de códigos de fórmulas, $d$ como lista no vacía y $c$ como fórmula. Se conserva $d$ íntegro, se recorre una copia residual y se mantiene el contador $k$ de posición. Se valida cada línea como secuencia de longitud tres (tags 0/1) o cuatro (tag 2) y su campo fórmula. En tag 0, se controla $j<r$ y se compara con la consulta de premisa. En tag 1, se llama a AxCert. En tag 2, se controla **antes de consultar** $i,j<k$; se leen del $d$ íntegro los campos fórmula de esas posiciones y se exige $c_j=S([7,c_i,c_k])$. El invariante afirma que todas las líneas anteriores ya fueron validadas; sus campos son fórmulas y sus consultas son definidas. Se rechazan autousos, referencias futuras, tags/longitudes inesperados y un objetivo distinto de la última fórmula.

La cantidad de líneas es finita y el residual exterior decrece por §18.9. Cada consulta o validación interior, incluidas sustituciones de certificados, es un programa total previamente probado; un código inválido puede fallar pero no producir una espera infinita. Con un número fijo de registros se conservan el contexto, prueba, residual, contador y datos temporales; las listas de aridad variable están codificadas. Las ramas y las llamadas son fijas y compilables por §18.4. La salida $1$ implica por el invariante todas las cláusulas de §18.35; cada objeto que las cumple supera los mismos controles. Esto prueba exactitud y totalidad sobre todos los naturales, sin consultar si una fórmula es demostrable. $\square$

## 18.37. Borrado y certificación de derivaciones originales

### Metateorema 18.37.1 — Borrado y certificación de derivaciones originales {#tlog-mth-00091}

**Metateorema.** Para una lista finita válida $g$ con conjunto subyacente $\Gamma_g$ y una fórmula $\varphi$,
$$
\boxed{\Gamma_g\vdash_{\mathsf H_\tau^=}\varphi
\iff \exists d\in\omega\ \operatorname{ProofCert}(g,d,G(\varphi)).}
$$
Más precisamente, borrar cualquier prueba aceptada da una derivación original con igual secuencia de fórmulas; toda derivación original desde $\Gamma_g$ admite una certificación con esa misma secuencia y conclusión.

**Prueba.** El borrado se calcula extrayendo cada campo fórmula, acumulando en orden inverso y revirtiendo. Por inducción en las posiciones, una línea aceptada de premisa pertenece al conjunto $\Gamma_g$; una de axioma pertenece a Ax por §18.33; una MP tiene dos precedentes y la igualdad literal de §9.7. La prueba es no vacía y la última fórmula se conserva, por lo que satisface exactamente la definición original.

Para la inversa, fijamos la derivación finita original. En cada línea, si es premisa se toma el menor índice de su aparición en $g$. Si no, y es axioma, §18.33 garantiza un certificado natural; se toma el menor entre los que aceptan. En el caso restante, la definición proporciona $i,j<k$ que cumplen MP; se toma el menor par en el orden lexicográfico del cuadrado finito $k^2$. Estas selecciones se justifican en la metateoría clásica y el buen orden de $\omega$; no requieren AC ni un decisor del caso «no es axioma». Una alternativa es codificar los finitísimos testigos de cada cláusula sin pedir una elección global. La lista de líneas así construida pasa los controles anteriores por inducción.

La inversa afirma existencia de una certificación. **No** afirma todavía un algoritmo total que decida si una secuencia desnuda es derivación y, si lo es, certifique cada línea. Dada una secuencia que sí es derivación y $g$, se puede buscar una certificación natural mediante el verificador total, parando cuando se encuentre; sobre una secuencia inválida esa búsqueda puede divergir. En ambos sentidos se mantiene sólo MP como regla primitiva. $\square$

## 18.38. Semidecidibilidad uniforme de demostrabilidad desde premisas finitas

### Metateorema 18.38.1 — Semidecidibilidad uniforme de demostrabilidad desde premisas finitas {#tlog-mth-00092}

**Metateorema.** La relación
$$
B(g,c)\iff g\text{ es lista válida de fórmulas},\ c=G(\varphi),\ \Gamma_g\vdash\varphi
$$
es semidecidible-RM sobre $\omega^2$. En particular, los códigos de teoremas lógicos forman un conjunto semidecidible-RM, fijando $g=0$.

**Programa.** Se validan $g,c$; si alguno falla se entra en un bucle RM divergente explícito (un salto incondicional a sí mismo de §17.24), porque salida $0$ con HALT también sería aceptación para un semidecidor por dominio de parada. Si los tipos pasan, se inicia $d=0$ y se repite: calcular ProofCert$(g,d,c)$, detenerse si devuelve $1$ y aumentar $d$ en caso contrario.

**Prueba.** Cada prueba finita del candidato termina por §18.36; el programa reutiliza el mismo subprograma fijo, no interpreta un código variable de programa. Si existe un certificado $d_*$, los finitísimos tests anteriores terminan y se alcanza $d_*$; entonces se detiene. Si no existe, cada test falla y la ejecución prosigue indefinidamente. §18.37 identifica la existencia del certificado con derivabilidad original. No se concluye decidibilidad de demostrabilidad ni semidecidibilidad de su complemento. Tampoco se extiende este resultado a un conjunto arbitrario de axiomas adicionales: su pertenencia o sus certificados necesitarán hipótesis efectivas propias. $\square$

## 18.39. Salida del microtramo y obligaciones restantes

### Corolario 18.39.1 — Salida del microtramo y obligaciones restantes {#tlog-cor-00028}

**Corolario de alcance.** Las operaciones de soporte, frescura, sustitución de términos, FreeFor, sustitución literal y sustitución canónica sin captura son efectivas bajo la presentación fijada. Las instancias H/Q/E con parámetros declarados y los prefijos axiomáticos se verifican mediante programas totales. Las derivaciones certificadas son decidibles y su existencia caracteriza exactamente derivabilidad desde premisas finitas, que es semidecidible-RM.

**Prueba.** Cada componente corresponde a las construcciones de §§18.22–38 y conserva las condiciones originales de los capítulos 6/9. El verificador comprueba testigos finitos, y el reconocedor de demostrabilidad busca uno; no se confunden ambos dominios de terminación. Ninguno consulta estructuras ni afirma consistencia de $\mathrm{ZF}_{obj}$. $\square$

**Frontera histórica al cerrar M02, descargada en §§18.42–63.** Para M03 se conservaron: codificación numérica explícita de programas RM, configuraciones y trazas con guardas; evaluación uniforme de un paso sobre descripciones válidas, sin confundirla con una máquina universal total de ejecución; examen de reconocimiento de axiomas y derivaciones **sin** certificados (requiere prueba específica); extensiones a teorías con presentación efectiva de axiomas; posible decisión de equivalencia alfa mediante los códigos por profundidad ya demostrados, si se necesita. No se afirma aquí máquina universal, equivalencia con Turing, representabilidad (CH19), diagonalización (CH20) ni una totalidad interna de los procedimientos en ZF objeto.

## 18.40. Ejemplos de control y estado local

Con $\varphi=R_2(x_0,x_1)$, el término $x_1$ **no** es libre para $x_0$ en $\forall x_1\varphi$: Q1 con esos parámetros se rechaza. CA puede renombrar el cuantificador a $x_2$ si los nombres usados son sólo $0,1$, y producir $\forall x_2 R_2(x_1,x_2)$, pero ese resultado no convierte en válida la instancia literal rechazada. Si el índice $2$ ya es nombre ligado interior, fresh debe escoger el siguiente mínimo ausente.

El contexto vacío admite una prueba de una línea para E1, también sobre una constante nularia. El prefijo $[0,0]$ produce $\forall x_0\forall x_0(t=t)$ y no se rechaza por repetición. Una prueba desde $[A,A\to B]$ puede certificar las dos primeras líneas como premisas y la tercera como MP$(0,1)$ con conclusión $B$. Si la tercera refiere a sí misma o al índice 3, se rechaza antes de leer la referencia; si declara $A$ como conclusión final cuando la última línea es $B$, también se rechaza. No se acepta una línea «Gen» aplicada directamente a la premisa $A$.

Al cierre histórico de M02, el Capítulo 18 tenía 38 resultados cerrados propios: 18 de M01 y 20 de M02. El cierre del capítulo seguía pendiente; se completa en §18.63. La auditoría de pruebas humanas, las regresiones de referencia, el grafo y la persistencia tienen evidencias separadas; no se atribuye compilación Lean a este bloque.

```text
LOCAL  CH18-M02 ████████████████████ 20/20 unidades (100 %)
GLOBAL TLOG     ██████████████████░░░░░░ 18/24 capítulos (75 %)
```

## 18.41. Alcance del cierre y datos efectivos fijados

### Convención 18.41.1 — Alcance del cierre y datos efectivos fijados {#tlog-cnv-00029}

El cierre conserva la presentación efectiva de la signatura de §18.2 y el cálculo exacto de §9.5/7. Los dominios de símbolos y sus aridades tienen programas RM totales fijados. La numeración no presupone un programa que calcule sobre símbolos abstractos sin presentación. Todas las pruebas son externas en ZF clásica, sin AC/BPI; no se introduce una teoría objeto ni se presume consistencia o modelo de $\mathrm{ZF}_{obj}$.

En este tramo se distingue una transición uniforme **total** de una ejecución universal **parcial**, que se construirá expresamente. La totalidad de verificadores de una prueba dada no implica decidir si existe alguna prueba. Los avisos de «pendiente» de M01/M02 documentan su alcance histórico; las obligaciones que se descargan aquí se señalan en §18.63.

## 18.42. Códigos de instrucciones con cuatro coordenadas

### Definición 18.42.1 — Códigos de instrucciones con cuatro coordenadas {#tlog-def-00128}

Usamos el mismo código $S$ de secuencias de §18.8, no una nueva función de emparejamiento. Los códigos de instrucciones son
$$
I(\mathtt{HALT})=S([0,0,0,0]),\quad I(\mathtt{INC}(i,j))=S([1,i,j,0]),\quad
I(\mathtt{DECJZ}(i,j,k))=S([2,i,j,k]).
$$
Un código debe decodificarse en **exactamente cuatro** coordenadas. En tag 0 las otras tres son cero; en tag 1 la última es cero; en tag 2 no hay una restricción adicional. Estos son los constructores de §17.2, sin instrucciones macro como nuevos tags. Que una coordenada sea natural no certifica aún que sea un registro o destino del programa.

## 18.43. Códigos de programas y su dominio tipado

### Definición 18.43.1 — Códigos de programas y su dominio tipado {#tlog-def-00129}

Para $P=(r,p)$, con lista $p=[J_0,\ldots,J_{n-1}]$, definimos
$$
\mathsf{Pr}(P)=S([r,S([I(J_0),\ldots,I(J_{n-1})])]).
$$
El dominio $D_{Pr}$ exige longitud exterior dos, $r\ge1$, lista interior válida de longitud $n\ge1$, instrucciones válidas y las guardas: en INC, $i<r,j<n$; en DECJZ, $i<r,j<n,k<n$. HALT no menciona un registro o destino. $D_{Pr,q}$ agrega $q\le r$ para $q\in\omega$. La aridad de entrada no forma parte del par $(r,p)$: un mismo programa admite las aridades $0,\ldots,r$. No se fuerza la existencia de una instrucción HALT ni que sea alcanzable.

## 18.44. Códigos de configuraciones relativas a un programa

### Definición 18.44.1 — Códigos de configuraciones relativas a un programa {#tlog-def-00130}

Para $P=(r,p)$ y $c=(\ell,\rho)\in C_P$, ponemos
$$
\mathsf{Cf}_P(c)=S([\ell,S([\rho(0),\ldots,\rho(r-1)])]).
$$
La relación $D_{Cf}(e,z)$ exige $e\in D_{Pr}$, longitud exterior dos en $z$, $\ell<n$ y una lista de **exactamente $r$** valores naturales. El código no incorpora de nuevo $e$; el tipo de configuración es relativo al programa suministrado. Códigos de programas y configuraciones son positivos, aunque algunas coordenadas o listas puedan ser cero. El número $0$ servirá como fallo de las funciones que devuelven estos códigos.

## 18.45. Decodificación, inyectividad y guardas de los códigos RM

### Lema 18.45.1 — Decodificación, inyectividad y guardas de los códigos RM {#tlog-lem-00068}

**Lema.** Las tres codificaciones son inyectivas en sus dominios, con inversas explícitas; $D_{Pr}$, $D_{Pr,q}$ y $D_{Cf}$ son decidibles-RM sobre todos los naturales. Se decide además si una configuración tipada señala HALT y se recupera su registro 0.

**Prueba.** Se aplican sucesivamente las inversas de $S$ a cada capa y se exige la longitud prescrita. La inyectividad de $S$ identifica coordenadas exteriores, lista interior y cada instrucción/valor; extensionalidad de secuencias finitas identifica los objetos originales. No se identifica una lista nula inválida con un fallo: el decodificador de §18.9 lleva bandera. Para programas, se computa $n$ recorriendo la lista una vez; otro recorrido examina cada instrucción y sus guardas mediante comparaciones RM de §18.4. Para configuraciones, se comprueba el programa, se cuenta la lista de valores y se compara con $r$; sólo después se consulta $p(\ell)$ o el valor 0. La longitud no depende del valor máximo de ningún registro.

Todos los bucles consumen listas finitas decodificadas o ejecutan decodificadores totales. Un hueco de la imagen dispersa de $S$, un tag desconocido, una coordenada extra, $r=0$, una lista de instrucciones vacía o un salto fuera del segmento produce rechazo. La lectura de la instrucción vigente usa consulta de lista con índice acotado. HALT se reconoce por las cuatro coordenadas, no por el valor del registro de salida. $\square$

## 18.46. Inicialización uniforme de registros codificados

### Proposición 18.46.1 — Inicialización uniforme de registros codificados {#tlog-pro-00123}

**Proposición.** Es computable-RM una función total $\mathsf{Init}(e,x)$ que, para $e=\mathsf{Pr}(P)$ y $x=S([a_0,\ldots,a_{q-1}])$ con $q\le r$, devuelve el código de $\operatorname{init}_P(\bar a)$, y devuelve $0$ en las demás entradas.

**Prueba.** Se valida $e$ y se decodifica $x$ con bandera; $x=0$ es la entrada vacía válida de aridad cero. Se calcula $q$ y se rechaza $q>r$. Se copia la lista de entrada, se le concatenan $r-q$ ceros mediante un contador decreciente y se construye $S([0,\text{lista}])$. Para concatenar, se revierten acumuladores como en §18.10; ningún registro de la máquina ejecutora se selecciona dinámicamente. La lista de $r$ registros simulados es un natural guardado en un registro fijo. El contador inicial $r-q$ es finito, incluso si es muy grande. La salida tiene longitud $r$, contador de instrucciones 0 y exactamente los valores exigidos en §17.5. $\square$

## 18.47. Evaluación uniforme y total de un paso codificado

### Metateorema 18.47.1 — Evaluación uniforme y total de un paso codificado {#tlog-mth-00093}

**Metateorema.** Hay un programa RM fijo total $\mathsf{Step}(e,z)$ que devuelve $0$ fuera de $D_{Cf}$ y satisface
$$
\mathsf{Step}(\mathsf{Pr}(P),\mathsf{Cf}_P(c))=\mathsf{Cf}_P(E_P(c)).
$$

**Construcción.** Tras validar, se consulta la instrucción en $\ell$. HALT devuelve $z$ íntegro. INC$(i,j)$ reconstruye la lista de valores cambiando sólo la posición $i$ por su sucesor y pone etiqueta $j$. DECJZ$(i,j,k)$ consulta ese valor: si es cero pone etiqueta $j$ sin modificar la lista; si es positivo reconstruye con su predecesor y pone etiqueta $k$. Para actualizar se recorre la lista con un contador de posición, se acumulan los valores en orden inverso y se revierte al final. El acceso/actualización son operaciones sobre naturales codificados; hay un número fijo de registros auxiliares y cuatro ramas fijas.

**Prueba.** La validación y todas las consultas terminan por §18.45. La reconstrucción consume exactamente $r$ valores. Las guardas garantizan destinos en $n$ y registro designado en $r$; por §17.8 la configuración reconstruida está tipada. Las cuatro ramas son literalmente §17.7, incluida la orientación $j$ en cero y $k$ en positivo, y la parada absorbente. La composición y los bucles se compilan por §17.22–25; el programa suministrado como dato no se inserta en el texto del ejecutor. Este resultado interpreta **un paso** y todavía no afirma parada de una ejecución no acotada. $\square$

## 18.48. Ejecución acotada uniforme y detección finita de parada

### Metateorema 18.48.1 — Ejecución acotada uniforme y detección finita de parada {#tlog-mth-00094}

**Metateorema.** $\mathsf{Run}(e,x,t)$, que devuelve el código del estado tras $t$ transiciones o $0$ si programa/entrada son inválidos, es computable-RM total. También es decidible-RM $\mathsf{HaltBy}(e,x,t)$: que esa ejecución esté en HALT en tiempo $t$.

**Prueba.** Inicializamos $z=\mathsf{Init}(e,x)$ y, si es válido, repetimos exactamente $t$ veces $z:=\mathsf{Step}(e,z)$ usando un contador decrementado. El invariante, por inducción en el número $k$ de iteraciones, es $z=\mathsf{Cf}_P(\operatorname{Run}_P(\bar a,k))$. Cada iteración termina y permanece tipada por §18.47. El bucle exterior termina porque el contador llega a cero, con caso $t=0$ incluido. Consultar HALT en la salida da el segundo programa, con rechazo en fallo. §17.12 identifica HALT en tiempo $t$ con parada en algún tiempo $s\le t$: las transiciones después de HALT repiten el estado. No se ejecuta «hasta que pare» dentro de este decidor. $\square$

## 18.49. Códigos de trazas y certificados finitos de parada

### Definición 18.49.1 — Códigos de trazas y certificados finitos de parada {#tlog-def-00131}

Una traza codificada es $v=S([z_0,\ldots,z_t])$, no vacía. $\mathsf{Trace}(e,x,t,v)$ exige programa/entrada válidos, longitud $t+1$, $z_0=\mathsf{Init}(e,x)$, todos los $z_k$ tipados y $z_{k+1}=\mathsf{Step}(e,z_k)$ para $k<t$. La relación
$$
\mathsf{StopTrace}(e,x,t,v,y)
$$
agrega HALT en $z_t$ y registro 0 igual a $y$. No exige que $t$ sea el primer tiempo de parada; se permite repetición absorbente. Su variante $\mathsf{FirstStopTrace}$ exige además que ningún $z_k$, $k<t$, señale HALT. Un certificado de parada puede almacenarse como $S([t,v])$; $y$ es un valor natural, no necesariamente código de fórmula.

## 18.50. Reconocimiento total y exactitud de trazas codificadas

### Metateorema 18.50.1 — Reconocimiento total y exactitud de trazas codificadas {#tlog-mth-00095}

**Metateorema.** Trace, StopTrace y FirstStopTrace son decidibles-RM. Para programa/entrada válidos y cada $t$ hay exactamente una traza de longitud $t+1$ aceptada.

**Prueba.** Se decodifica $v$ con bandera, se controla que no sea vacío y se cuenta su longitud; no se resta uno a una longitud cero. Se compara con $t+1$, se valida cada estado y se compara el primero con Init. Con un estado anterior conservado en un registro fijo, el recorrido compara cada siguiente con Step del anterior. La variante de parada lee instrucción y salida sólo después de validar el último estado; la variante primera rechaza cualquier HALT anterior. Se consume una lista finita y cada llamada es total; todos los naturales inválidos tienen salida 0.

Inducción en $k$ usando determinismo identifica cada $z_k$ con el estado de §17.9. La traza existente de §17.10 se codifica, y el mismo argumento prueba unicidad por inyectividad de los códigos. Se puede construirla mediante $t$ pasos acumulados y reversión. En particular, $t=0$ admite una sola configuración y certifica parada inmediata si la instrucción inicial es HALT. La repetición posterior a HALT conserva Trace y StopTrace, pero no FirstStopTrace. $\square$

## 18.51. La gráfica calculada como proyección de certificados de parada

### Proposición 18.51.1 — La gráfica calculada como proyección de certificados de parada {#tlog-pro-00124}

**Proposición.** Para $e=\mathsf{Pr}(P)$ y entrada compatible $x=S(\bar a)$,
$$
F_P(\bar a)\downarrow=y\iff\exists t,v\in\omega\ \mathsf{StopTrace}(e,x,t,v,y).
$$
La relación uniforme de la izquierda es semidecidible-RM, rechazada por divergencia en entradas inválidas, y su salida $y$ es única cuando existe.

**Prueba.** Una parada de §17.13 proporciona un tiempo y su única traza por §18.50; recíprocamente una traza aceptada es parte de la órbita original y su último estado HALT da precisamente el valor $y$. La absorción y §17.14 hacen iguales todos los valores certificados para la misma entrada. Para semidecidir se recorren $t=0,1,\ldots$, se computa Run y se consulta HALT y registro 0. Se para sólo si se cumple la igualdad con $y$; si el programa para con otro valor se puede entrar en un bucle divergente, y si no para se sigue buscando. Las consultas acotadas son totales. No se concluye decidir la proyección existencial. $\square$

## 18.52. Ejecutor universal parcial para las descripciones RM aprobadas

### Metateorema 18.52.1 — Ejecutor universal parcial para las descripciones RM aprobadas {#tlog-mth-00096}

**Metateorema.** Existe un programa ejecutor fijo $U$ de dos entradas naturales que calcula parcialmente
$$
U(e,x)\simeq F_P(\bar a)\quad\text{si }e=\mathsf{Pr}(P),\ x=S(\bar a),\ |\bar a|\le r.
$$
Se construye **un mismo** ejecutor para todas las descripciones. En entradas inválidas y en ejecuciones divergentes, $U$ diverge. La salida, si existe, es el valor original del registro 0, incluido cero.

**Construcción y prueba.** El ejecutor guarda $e$ y $z=\mathsf{Init}(e,x)$ en registros fijos. Si Init falla entra en el lazo divergente explícito de §17.24. En el lazo principal valida/consulta la instrucción actual: si es HALT, copia el valor simulado de registro 0 al registro de salida del ejecutor y entra en su propio HALT; en otro caso calcula Step$(e,z)$, reemplaza $z$ y vuelve al lazo. Los subprogramas totales de consulta y Step son fijos; sus macros se expanden y relocalizan como en §17.22. La lista de registros del programa simulado es un dato natural, por lo que un número arbitrario de registros simulados no exige un número variable de registros físicos del ejecutor.

Tras $k$ vueltas completas, la configuración simulada es la de tiempo $k$ por inducción y §18.47. Cada vuelta tiene duración finita en el ejecutor; si la órbita llega por primera vez a HALT en $t$, se realizan finitísimas vueltas y se devuelve el valor correspondiente. Si nunca llega a HALT, el lazo realiza una vuelta después de otra y nunca alcanza el HALT del ejecutor. La validación inicial también termina. Así la gráfica parcial coincide exactamente con la afirmada. El tiempo del ejecutor no es el tiempo simulado; no se da una cota de complejidad ni equivalencia con máquinas de Turing. Esta es la primera universalidad RM aprobada del tratado y se deriva de la codificación, no se retropropaga al Capítulo 17. $\square$

## 18.53. Enumeraciones finitas de subárboles y productos de opciones

### Lema 18.53.1 — Enumeraciones finitas de subárboles y productos de opciones {#tlog-lem-00069}

**Lema.** Se calculan listas de todas las ocurrencias de subtérminos de una fórmula, y productos cartesianos finitos de listas de alternativas codificadas. Una reconstrucción por constructor con un número finito de opciones locales genera una lista finita efectiva de candidatos, incluidos casos de aridad variable y nularia.

**Prueba.** Un recorrido tipado registra cada nodo de término encontrado, incluidas variables, aplicaciones completas y términos dentro de átomos; los duplicados se pueden conservar. Para formar el producto de listas $L_0,\ldots,L_{m-1}$ se inicia la lista de parciales con la tupla vacía. Por cada $L_i$, se recorren la lista de parciales y $L_i$, anexando una opción a cada parcial. La lista resultante reemplaza la anterior. Si algún $L_i$ es vacío el resultado es vacío; si $m=0$ queda exactamente la tupla vacía. Todos los bucles consumen listas ya finitas; el número de opciones puede crecer sin impedir terminación. Las listas de parciales son números codificados, no almacenamiento dinámico de instrucciones. La inducción en $i$ prueba que aparecen exactamente todas las tuplas de opciones. Posorden de §18.21 permite aplicar esta construcción a listas de hijos y reconstruir cada alternativa del padre. La medida es el árbol de entrada original y las listas auxiliares finitas, no el tamaño del resultado. $\square$

## 18.54. Recuperación finita de testigos de Q1 y Q2

### Lema 18.54.1 — Recuperación finita de testigos de Q1 y Q2 {#tlog-lem-00070}

**Lema.** Dados $\varphi,x_i,B$, se decide si existe un término $t$ libre para $x_i$ en $\varphi$ tal que $B=\varphi[t/x_i]_{lit}$, y en caso afirmativo se devuelve un testigo.

**Prueba.** Si $i\notin FV(\varphi)$, sólo puede resultar $B=\varphi$, y el término $x_i$ es un testigo seguro explícito. Si $i\in FV(\varphi)$, al menos una hoja libre original se sustituye por una copia completa de $t$ situada como subtérmino de un átomo de $B$. Por ello cualquier testigo aparece en la lista finita de subtérminos de $B$ de §18.53. Se recorren éstos en orden de visita y se verifican FreeFor y la igualdad literal computada; si ninguno pasa se rechaza. En el caso vacuo la sustitución es identidad por sus cláusulas, y en el no vacuo el argumento de ocurrencia prueba cobertura. Cada test es total. Aplicado a la forma $(\forall x_i\varphi)\to B$ decide Q1; aplicado a $B\to\exists x_i\varphi$ decide Q2. Un Q1 con captura no se acepta por usar CA, y no se buscan términos de código arbitrariamente grande. $\square$

## 18.55. Recuperación finita de los parámetros latentes de E2

### Lema 18.55.1 — Recuperación finita de los parámetros latentes de E2 {#tlog-lem-00071}

**Lema.** Dados términos $t,u$ y fórmulas $A,B$, se decide si existen $i,\varphi$ con ambas condiciones FreeFor y
$$
A=\varphi[t/x_i]_{lit},\qquad B=\varphi[u/x_i]_{lit}.
$$
En aceptación se construyen dichos testigos finitamente.

**Construcción.** Escogemos $j=\operatorname{fresh}(Names(A)\cup Names(B)\cup Var(t)\cup Var(u))$. Formamos listas de plantillas sobre pares de subárboles alineados. Para términos $a,b$, se incluye la alternativa $x_j$ siempre que $(a,b)=(t,u)$. Además se incluye una variable original si $a=b=x_h$, o se reconstruye una aplicación si ambos tienen el mismo símbolo y aridad, tomando todos los productos de alternativas de sus argumentos. Se permiten **ambas** alternativas si coinciden sus condiciones; no se corta la reconstrucción cuando es posible el hueco. No hay otras alternativas. Para fórmulas se exige el mismo constructor: igualdad y relación procesan pares de argumentos de término; negación y binarios procesan sus matrices/componentes; cuantificadores exigen el mismo $Q$ y el mismo índice ligado, y procesan matrices. No hay huecos de fórmula ni cambio de vinculante. Los nularios utilizan el producto vacío único.

Cada llamada desciende a subárboles originales propios de $A,B$; cada lista obtenida es finita por §18.53. Para cada plantilla $\psi$ generada se comprueban FreeFor$(t,x_j,\psi)$ y FreeFor$(u,x_j,\psi)$ y las dos igualdades de sustitución. Se devuelve la primera que pase; si no hay ninguna se rechaza. Las verificaciones finales son indispensables: una coincidencia de subárboles bajo un cuantificador capturante no autoriza el hueco.

**Corrección.** Todo candidato aceptado proporciona directamente $(j,\psi)$ con las cuatro condiciones. **Cobertura.** Supongamos un testigo original $(i,\varphi)$. En las posiciones de hojas **libres** de $x_i$ en $\varphi$, reemplacemos esa hoja por $x_j$, y dejemos íntegros todos los otros nodos, incluidos nombres ligados. Si $x_j$ hubiera aparecido en un nodo restante de $\varphi$, aparecería en A y B porque la sustitución literal sólo cambia las hojas libres de $x_i$; esto contradice la frescura elegida. Si $i=j$, los nombres ligados $j$ también habrían permanecido en A/B, y los restantes nodos no contienen ese nombre. Así, en todos los casos, la nueva plantilla no contiene un vinculante $j$ ni una hoja libre $j$ distinta de los huecos designados.

En cada hueco, los términos de A/B son exactamente $(t,u)$ y la construcción incluye $x_j$. En toda otra hoja de variable ambos árboles conservan la misma hoja; funciones, átomos, conectivos y cuantificadores se conservan literalmente por las cláusulas de sustitución. Inducción sobre el árbol original muestra que la plantilla figura entre los candidatos, incluso cuando $t=u$ y se necesitan elecciones de hueco y reconstrucción en lugares distintos. Las condiciones FreeFor originales garantizan que ningún nombre ligado en el camino capture una variable de $t$ o $u$ en los nuevos huecos; los cuantificadores ligados $i$ bajo los que la sustitución estaba bloqueada conservan su subárbol y no reciben huecos. La plantilla supera entonces las dos comprobaciones y las dos igualdades. El caso sin ocurrencias libres genera simplemente $\psi=A=B$. No se ha supuesto una cota para el código de $\varphi$: se construye una **familia finita de plantillas** a partir de los árboles objetivo. $\square$

## 18.56. Reconocimiento de axiomas lógicos sin certificados

### Metateorema 18.56.1 — Reconocimiento de axiomas lógicos sin certificados {#tlog-mth-00097}

**Metateorema.** La pertenencia $\mathsf{Ax}(c)$ a los códigos de axiomas de $\mathsf H_\tau^=$ es decidible-RM. Hay además una función total con bandera que obtiene un certificado $a$ de §18.32 cuando Ax vale.

**Programa básico.** Primero se valida la fórmula. H1–H12 se reconocen por ajuste de las doce plantillas de §18.29: un primer encuentro de cada metavariable almacena el subcódigo correspondiente, y los encuentros restantes exigen igualdad. Hay un número fijo de metavariables; se rechaza cualquier constructor incorrecto. Q1/Q2 extraen índice y matriz del cuantificador correspondiente y usan §18.54. Q3 compara sus tres cuantificadores, el índice común, las matrices y la implicación; Q4 controla igualdad de matriz e índice ausente de FV; Q5 compara exactamente ambos cuantificadores, las negaciones y la matriz. E1 exige una igualdad de términos iguales. E2 exige raíz $(t=u)\to(A\to B)$ y aplica §18.55. Cada éxito suministra los parámetros de un certificado básico, que se vuelve a verificar por §§18.29–31. Se examinan todos los esquemas en el orden H1–H12,Q1–Q5,E1–E2, con primer éxito como convención determinista.

**Prefijo.** Con la fórmula original, se prueba el decidor básico; en fallo, si su raíz es $\forall x_i$, se agrega $i$ a la lista de prefijo y se pasa a su matriz; de otro modo se rechaza. En cada etapa se guarda el orden exterior a interior. A lo sumo se consumen tantos cuantificadores como nodos de la entrada; si se halla un básico se devuelve $S([S(\text{prefijo}),b])$. También se admite éxito con prefijo vacío, repetido o vacuo.

**Prueba.** Cada ajuste y prueba lateral es total; E2 termina por su familia finita específica, no por minimizar certificados arbitrarios. El bucle de prefijos desciende a matrices propias. Todo éxito reconstruye exactamente un axioma de §9.5 y AxCert lo acepta. Recíprocamente un axioma es un prefijo universal finito de alguna instancia básica; se alcanza su matriz, y los ajustes H, las comprobaciones Q/E y los dos lemas de cobertura no la omiten. Esto decide la **proyección** cuya decidibilidad no se había afirmado en §18.33. La existencia de muchas certificaciones no altera el decidor. $\square$

## 18.57. Secuencias originales de derivación codificadas

### Definición 18.57.1 — Secuencias originales de derivación codificadas {#tlog-def-00132}

Para contexto finito $g$ y objetivo $c$, $\mathsf{RawProof}(g,d,c)$ exige que $g$ sea lista de códigos de fórmulas y $d=S([c_0,\ldots,c_{m-1}])$ sea lista **no vacía** de fórmulas con $c_{m-1}=c$. Cada línea es premisa en $g$, axioma lógico o consecuencia MP de dos índices menores que su posición. Aquí $d$ contiene sólo códigos de fórmulas; no son los códigos de líneas certificadas de §18.34. Los dos espacios se distinguen por su validador, aunque ambos utilicen $S$. Las reglas admisibles requieren expansión previa al cálculo de §9.7.

## 18.58. Decisión y certificación total de derivaciones originales

### Metateorema 18.58.1 — Decisión y certificación total de derivaciones originales {#tlog-mth-00098}

**Metateorema.** RawProof es decidible-RM. Existe un certificador total con fallo $0$ que en aceptación devuelve una prueba de §18.35 cuyo borrado es **exactamente** la lista original $d$.

**Programa y prueba.** Se validan contexto, lista no vacía y objetivo final. En posición $k$ se busca primero el menor índice de premisa igual a $c_k$. Si no existe, se ejecuta Ax y su extractor; en fallo se recorren los pares $(i,j)$ en orden lexicográfico de $k\times k$ y se exige $c_j=S([7,c_i,c_k])$. Se selecciona la primera justificación exitosa y se construye la línea de tag 0,1 o2 correspondiente; si ninguna existe se devuelve 0. No se consulta una referencia futura. Acumulación inversa y reversión preservan el orden. Las búsquedas de premisa y MP son finitas y Ax es total por §18.56; el bucle exterior consume la lista original. Por tanto incluso una secuencia inválida se decide en tiempo finito.

Inducción sobre $k$ prueba que la línea aceptada cumple exactamente una de las cláusulas de §9.7 y que el certificado agregado pasa ProofCert. A la inversa, si la secuencia original es derivación, cada línea satisface al menos una de las tres alternativas examinadas; el algoritmo no la rechaza y su última fórmula es la misma. El borrado conserva literalmente todas las fórmulas, incluidos duplicados. Es una certificación **constructiva total**, que fortalece la existencia metateórica de §18.37; no busca todas las derivaciones posibles. $\square$

## 18.59. Presentaciones efectivas de teorías adicionales

### Definición 18.59.1 — Presentaciones efectivas de teorías adicionales {#tlog-def-00133}

Una teoría adicional $T$ se presenta mediante un conjunto $A_T$ de códigos de fórmulas de la signatura fijada; $\mathsf H_\tau^=+T$ permite esas fórmulas como axiomas adicionales y conserva sólo MP como regla. Las reglas/prefijos de los **axiomas lógicos** de §9.5 se conservan; no se agrega aquí automáticamente el prefijo universal de todo axioma adicional. Si se desea esa extensión, debe incluirse explícitamente en $A_T$ o justificarse como otra presentación.

Una presentación decidible aporta un programa RM total para $c\in A_T$. Una presentación semidecidible aporta un programa fijo $P_T\in\operatorname{Prog}_1$ que para exactamente en las entradas $c\in A_T$, independientemente de su valor de salida. Es dato adicional, no consecuencia de que $A_T$ sea un conjunto numerable o de que se le llame teoría. No se atribuye todavía ninguna de estas hipótesis a $\mathrm{ZF}_{obj}$.

## 18.60. Verificación de derivaciones para axiomas adicionales decidibles

### Metateorema 18.60.1 — Verificación de derivaciones para axiomas adicionales decidibles {#tlog-mth-00099}

**Metateorema.** Para una presentación decidible fija de $A_T$, las secuencias originales de derivación de $\mathsf H_\tau^=+T$ desde contextos finitos se reconocen por un programa RM total. Su relación de derivabilidad es semidecidible-RM, uniformemente en contexto y conclusión para esa presentación fija.

**Prueba.** En §18.58 se agrega, entre Ax lógico y MP, la llamada al decidor de $A_T$. Cada posición sigue teniendo una disyunción de pruebas totales y búsquedas finitas, con la misma inducción de exactitud. Para semidecidir derivabilidad se recorren los números $d=0,1,\ldots$ usando ese verificador, se para en aceptación y se diverge en entradas de contexto/conclusión inválidas. Toda derivación finita tiene un código y será alcanzada; si no hay ninguna, no se para. La hipótesis aporta un **programa fijo** y su totalidad demostrada; no se decide desde un código arbitrario si éste es un decidor total correcto de una teoría. $\square$

## 18.61. Certificados para teorías de axiomas semidecidibles

### Metateorema 18.61.1 — Certificados para teorías de axiomas semidecidibles {#tlog-mth-00100}

**Metateorema.** Para una presentación semidecidible fija de $A_T$, hay un verificador total de derivaciones **certificadas** y la derivabilidad desde contextos finitos es semidecidible-RM. No se afirma en esta hipótesis decidibilidad de las derivaciones originales desnudas.

**Construcción.** Se conserva el formato de §18.34 y se agrega una línea $S([3,c,t,v])$ para un axioma adicional. Se exige que $c$ sea fórmula y que $v$ sea la traza válida del programa fijo $e_T=\mathsf{Pr}(P_T)$ en entrada $S([c])$, hasta tiempo $t$, con HALT en el último estado; **no** se exige una salida específica. Este predicado es decidible por §18.50. Las líneas 0/1/2 conservan sus controles anteriores y MP consulta el campo fórmula de cualquiera de los cuatro tipos precedentes. Todas las longitudes y referencias se validan antes de consultar.

**Prueba.** Cada línea se decide totalmente y el recorrido de prueba es finito. Una línea 3 aceptada acredita parada del semidecidor, por tanto $c\in A_T$. Recíprocamente un axioma adicional tiene algún tiempo de parada y su traza única; en una derivación finita se suministran los finitísimos certificados necesarios, con mínimo tiempo para cada aparición, sin AC. Borrado e inducción justifican exactitud como en §18.37. Buscar los códigos de pruebas certificadas mediante el verificador total semidecide su existencia y, por borrado/certificación, la derivabilidad. No se sustituye esta búsqueda por ejecutar un semidecidor de axiomas hasta una negativa que quizá nunca llegue. Una enumeración efectiva de axiomas sólo puede usarse aquí tras construir su semidecidor; una numeración abstracta de un conjunto no suministra esa construcción. $\square$

## 18.62. Decisión efectiva de equivalencia alfa

### Metateorema 18.62.1 — Decisión efectiva de equivalencia alfa {#tlog-mth-00101}

**Metateorema.** La equivalencia alfa de fórmulas codificadas es decidible-RM; no se cambia por ello la igualdad literal utilizada por Ax y MP.

**Prueba.** Calculamos el código por profundidad de §6.28 con una lista de nombres de cuantificadores ancestros, el más reciente primero. En una hoja $x_i$, se busca su primera aparición en la lista: si está en posición $j$, se serializa la hoja ligada como $S([0,j])$; si no está, la hoja libre como $S([1,i])$. Una función se serializa como $S([2,h,S(\text{hijos})])$. Para fórmulas usamos tags nuevos de este **espacio auxiliar**: igualdad3, relación4, negación5, binarios6/7/8/9 (and/or/imp/iff), cuantificadores10/11 (forall/exists). En los cuantificadores se omite el nombre en la salida y se lo antepone al contexto para visitar su matriz; sus códigos tienen campos tag y matriz. Igualdad lleva dos términos, relación lleva símbolo y lista de términos, y los demás llevan sus hijos en orden. Así los nularios, símbolos y cinco conectivos permanecen distintos.

Las listas de ancestros son finitas y cada consulta termina. La plantilla de §18.21 visita el árbol original con contexto propio para cada rama, de modo que el contexto hermano no queda contaminado por el de otra rama. La estructura auxiliar se serializa inyectivamente con $S$ y tags/longitudes distintos. Por inducción las hojas ligadas registran exactamente la distancia al vinculante más cercano y las libres conservan su índice; coincide con §6.28. §6.29 dice que dos fórmulas son alfa equivalentes exactamente cuando esos objetos son iguales; la serialización inyectiva permite decidirlo por igualdad de sus naturales. Se rechazan entradas no fórmulas. No se usa esta equivalencia para autorizar una instancia literal con captura ni para reemplazar la comparación de códigos de MP. $\square$

## 18.63. Cierre del capítulo e interfaces hacia aritmetización

### Corolario 18.63.1 — Cierre del capítulo e interfaces hacia aritmetización {#tlog-cor-00029}

**Corolario.** Bajo la presentación efectiva fijada, quedan construidas codificaciones inyectivas y decodificadores de expresiones, programas, configuraciones, trazas y derivaciones. Se deciden los dominios sintácticos, las operaciones de soporte y sustitución indicadas, los axiomas lógicos, las secuencias originales de prueba y los certificados de parada. Se construye el ejecutor universal parcial RM. La existencia de prueba es semidecidible para la lógica desde premisas finitas y para teorías adicionales bajo las hipótesis efectivas expresas.

**Prueba.** M01 proporciona presentación, pares, listas, tokens y árboles, con terminación y reconocimiento en toda entrada; M02 proporciona operaciones sintácticas y verificación certificada; §§18.42–62 descargan programas/configuraciones/trazas, universalidad parcial, recuperación finita de testigos, pruebas desnudas y teorías efectivas. Cada interfaz tiene tipos y rechazos declarados. La conjunción de resultados no añade una tesis de totalidad a ninguna búsqueda no acotada. $\square$

**Salida hacia CH19.** Los predicados externos decidibles aquí aprobados no son todavía fórmulas representadoras ni pruebas de representación en una teoría aritmética objeto. CH19 debe fijar esa teoría, traducir operaciones/códigos y probar, con su noción de representación, las obligaciones de funciones de secuencia, sustitución, transición y prueba. Para $\mathrm{ZF}_{obj}$ deberá justificarse su presentación efectiva concreta antes de usar el resultado de teorías; no se presume consistencia, modelo ni corrección.

**Salida hacia CH20.** No hay todavía lema diagonal, operador de punto fijo, sentencia de autorreferencia ni predicado de verdad aritmético aprobado. Tendrán que derivarse de la representabilidad correspondiente. La universalidad RM demostrada no aporta equivalencia con Turing ni decidibilidad de parada; esos resultados requieren sus propias pruebas.

Con estas fronteras, **CH18 CLOSED**. No queda pendiente una obligación interna de codificación del capítulo; las hipótesis de signatura/teoría permanecen visibles y las obligaciones de representabilidad y diagonalización pertenecen a los siguientes capítulos.

## 18.64. Ejemplos de cierre y mapa del capítulo

El programa $P=(1,[\mathtt{INC}(0,1),\mathtt{HALT}])$ tiene código $S([1,S([S([1,0,1,0]),S([0,0,0,0])])])$. Con entrada $S([a])$, Init es $S([0,S([a])])$, Step produce $S([1,S([a+1])])$ y el paso siguiente lo conserva. Una traza de tiempo 1 es primera parada; la traza extendida a tiempo 2 es válida y certifica la misma salida, pero no primera parada. El programa de una sola instrucción INC$(0,0)$ es válido y divergente; ni el reconocimiento de su código ni Run en un tiempo dado resuelven su parada por simple validación.

En E2, con $t=u$, la lista de plantillas conserva simultáneamente la opción hueco y la reconstrucción literal. Por ejemplo, una matriz con dos ocurrencias iguales puede necesitar abstraer una de ellas y conservar la otra. Bajo un cuantificador cuyo índice aparece en Var$(t)$, abstraer una posición que luego inserte $t$ falla FreeFor y se descarta. El reconocedor nunca reemplaza esas comprobaciones por igualdad semántica. La secuencia $[A,A\to B,B]$ es una derivación desde $[A,A\to B]$; el verificador puede certificarla con MP$(0,1)$. Que una secuencia candidata se rechace no demuestra que $B$ carezca de otra prueba.

| Bloque | Apartados | Salida |
|---|---|---|
| M01 | 18.1–18.18; ejemplos18.19 | 18 resultados: presentación, listas, tokens y sintaxis |
| M02 | 18.20–18.39; ejemplos18.40 | 20 resultados: sustitución y pruebas certificadas |
| M03 | 18.41–18.63; ejemplos18.64 | 23 resultados: ejecución codificada, reconocimiento y cierre |

El capítulo cierra **61/61 resultados propios**. Las auditorías humanas de M01/M02 se conservan; M03 y el cierre completo tienen auditorías separadas. Las regresiones de referencia y el certificado SHA-256 no son pruebas Lean. La Parte IV sigue abierta. El siguiente capítulo es **CH19 — Representabilidad en aritmética**, según la arquitectura canónica; no se inicia aquí su redacción.

```text
LOCAL  CH18-M03 ████████████████████ 23/23 resultados (100 %)
GLOBAL TLOG     ███████████████████░░░░░ 19/24 capítulos (79,17 %)
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 17](capitulo-17.md) · [Capítulo 19 →](capitulo-19.md)


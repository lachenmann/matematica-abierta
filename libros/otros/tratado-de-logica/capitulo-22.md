---
title: Capítulo 22 — Segundo teorema de incompletitud
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
content-id: MA-BCH-0224
content-type: book-chapter
source-id: TLOG-CH22-0001
prerequisites:
- MA-BCH-0220
- MA-BCH-0221
- MA-BCH-0222
- MA-BCH-0223
related:
- MA-BOK-0014
source-sha256: 701f1e650bc5242f4f13628778e0bf1f863ce2399fc338e4ca0bc6bc7c7b0a6a
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 21](capitulo-21.md) · [Capítulo 23 →](capitulo-23.md)

## 22.0. Expresar una ausencia de prueba

El primer teorema utilizó consistencia como hipótesis externa para excluir derivaciones de sentencias determinadas. El segundo exige que una teoría pueda hablar de sus propias pruebas con un predicado elegido cuidadosamente. La frase «T es consistente» tendrá ahora una traducción aritmética concreta, y tendremos que demostrar qué transformaciones de pruebas reconoce PA internamente.

La tarea técnica precede al argumento diagonal: codificación β con longitud variable dentro de PA, representación uniforme de recursión primitiva y certificados de verificaciones aritméticas finitas. Con ellas probaremos la clausura de demostrabilidad bajo MP y la introspección positiva. Después deduciremos el segundo teorema y Löb, distinguiendo consistencia, corrección, reflexión y elección del representante.

La redacción es autoral y las pruebas son humanas. Se contrastaron de forma limitada las §§4.7–4.8 de Jeremy Avigad, *Computability and Incompleteness*, versión9enero2007 ([archivo del autor](https://www.andrew.cmu.edu/user/avigad/Teaching/candi_notes.pdf)); la referencia sólo guía el contraste de las condiciones y las conclusiones. Aquí sus condiciones no se toman como axiomas: se realizan para nuestros certificados, nuestra PA y nuestra numeración S/G. No se importa la base Q ni la numeración del texto consultado.

## 22.1. Base y elección de representante

### Convención 22.1.1 — Base y elección de representante {#tlog-cnv-00033}

Trabajamos en ZF clásica externa sin AC/BPI. PA es la teoría objeto de CH19; RM es externo; ZF objeto no se identifica con ninguno de ellos. T será una presentación admisible de §21.2: PA más axiomas aritméticos cerrados semidecidibles y sus prefijos universales. La consistencia externa de T será hipótesis solamente donde se indique.

CH19 dio codificación β externa y representación de máquinas; CH21 dio D1 para certificados concretos. Ninguno demostró D2/D3 internas. Este capítulo primero construye codificación finita **dentro de PA**, luego representación con ecuaciones demostrables para funciones primitivas recursivas, y finalmente un representante de la verificación certificada cuya composición e introspección se prueban. No se inferirá totalización interna de una máquina arbitraria a partir de su totalización estándar.

El nuevo predicado se llamará $\Pr_T^*$ y su existencial $\operatorname{Prov}_T^*$. Conservamos los árboles originales $\operatorname{Prov}_{PA}$ de CH19 y $V_T$ de CH21. La coincidencia estándar de sus extensiones no se convertirá en equivalencia demostrable uniforme. Todas las comillas de este capítulo usan la numeración literal G ya aprobada.

## 22.2. Funciones primitivas recursivas y sus descripciones

### Definición 22.2.1 — Funciones primitivas recursivas y sus descripciones {#tlog-def-00156}

Una descripción PR se genera por cero, sucesor, proyecciones, composición y el esquema
$$
f(\vec x,0)=g(\vec x),\qquad f(\vec x,n+1)=h(\vec x,n,f(\vec x,n)).
$$
Aridades y descripción forman datos finitos externos. Una relación PR tiene una función característica PR de valores0/1. Suma, producto, predecesor truncado, comparación, selección por casos y búsqueda **acotada** se obtienen por estas cláusulas. La búsqueda no acotada no es una cláusula PR.

Un bucle de longitud dada por una función PR, con actualización PR de un estado numérico, es PR: se itera esa actualización por recursión y se proyecta el estado final. Los estados finitos pueden codificarse por los pares p de CH18. No se presupone aún representación PA uniforme: la construcción del grafo y sus pruebas se hará en §22.9.

## 22.3. Bézout y coprimalidad dentro de PA

### Lema 22.3.1 — Bézout y coprimalidad dentro de PA {#tlog-lem-00092}

**Lema.** PA demuestra el algoritmo de Euclides para dos naturales, la existencia de su máximo divisor común y la identidad de Bézout, interpretando coeficientes enteros mediante diferencias de pares de naturales. En particular, si m>0 y gcd(u,m)=1, existe h<m con uh≡1 (mod m). También demuestra que coprimalidad con m se conserva al multiplicar dos factores coprimos con m.

**Prueba interna.** División da u=qm+r con r<m. Por inducción fuerte sobre el segundo argumento, cuando m=0 tomamos gcd(u,0)=u y coeficientes1,0; cuando m>0 aplicamos la hipótesis a (m,r), cuyos coeficientes s,t dan sm+tr=d. Sustituir r=u−qm da tu+(s−tq)m=d. Cada diferencia entera se expresa como (a,b), valor a−b: suma, producto y cambio de signo son operaciones sobre pares de naturales; no ampliamos el dominio objeto. Un divisor común de u,m divide r y recíprocamente, de modo que la identidad y la propiedad de divisor máximo se transportan en cada paso. La inducción fuerte se obtiene de la inducción PA aplicada a «todos los argumentos anteriores satisfacen la propiedad».

Para gcd=1, reducimos el coeficiente de u módulo m; la división de diferencias se realiza trasladando una suma múltiplo de m hasta que el dividendo sea natural. El resto h sirve como inverso. Si au+bm=1 y cv+dm=1, su producto expresa1 como combinación de uv y m, probando el último aserto. Ésta es una prueba PA sobre números variables; no invoca una ejecución estándar finita de Euclides ni una tabla β preexistente. $\square$

## 22.4. Múltiplos comunes finitos con parámetros variables

### Lema 22.4.1 — Múltiplos comunes finitos con parámetros variables {#tlog-lem-00093}

**Lema.** PA demuestra que para todo L,V existe b>V positivo divisible por cada j con1≤j≤L. No necesitamos factorial como símbolo objeto.

**Prueba.** Por inducción en L, la fórmula ∃c>0∀j≤L(0<j→j∣c) vale para L=0 con c=1. Si c sirve para L, c(L+1) sirve para L+1, por las leyes de producto y divisibilidad. Finalmente b=c(V+1) es positivo, mayor que V y conserva todos los divisores. La divisibilidad se abrevia ∃q c=jq; se expande antes de emplear inducción. La fórmula puede tener cuantificadores no acotados: PA tiene inducción para ella. $\square$

## 22.5. Colección finita interna sin elección

### Lema 22.5.1 — Colección finita interna sin elección {#tlog-lem-00094}

**Lema.** Para cada fórmula Q(i,v,\vec z), PA demuestra
$$
\forall i<L\,\exists v\,Q(i,v,\vec z)\ \longrightarrow\
\exists V\,\forall i<L\,\exists v<V\,Q(i,v,\vec z).
$$
No se exige que Q sea decidible, ni que los testigos sean únicos.

**Prueba.** Inducción en L con los parámetros libres. En0 se toma V=1. En el paso, la hipótesis universal implica la del segmento anterior y proporciona un testigo v para i=L. Si V acota los anteriores, V'=V+v+1 acota éstos y v. Introducción y eliminación existencial se hacen con variables frescas; al descargar los testigos locales queda la existencia de V'. No se escoge una función infinita ni se utiliza AC. $\square$

## 22.6. Resto chino finito demostrado en PA

### Lema 22.6.1 — Resto chino finito demostrado en PA {#tlog-lem-00095}

**Lema.** Sean m_i=1+(i+1)b para i<L, donde b>0 es múltiplo de1,…,L. PA demuestra que los m_i son coprimos dos a dos. Para cada fórmula Q(i,v,\vec z), si PA dispone de ∀i<L∃v<m_i Q(i,v,\vec z), demuestra la existencia de A con ∀i<L∃v<m_i(Q(i,v,\vec z)∧A≡v mod m_i). No se requiere unicidad de Q para la existencia.

**Prueba.** Si i<j<L y d divide m_i,m_j, Bézout da gcd(d,b)=1 porque d divide1+(i+1)b. De d∣(j−i)b se sigue d∣j−i usando el inverso de b módulo d (d=1 es inmediato). Ahora1≤j−i≤L, luego d∣b, y de d∣m_i se obtiene d∣1. Todos estos pasos son fórmulas demostrables por §22.3 y aritmética PA.

Para CRT hacemos inducción en k≤L, manteniendo ∃A∃M con A≥0, M>0 y: los residuos escogidos de Q se cumplen para i<k; todos esos m_i dividen M; y gcd(M,m_j)=1 para k≤j<L. En k=0 sirven A=0,M=1. En el paso escogemos v<m_k con Q(k,v). Por coprimalidad existe h inverso de M módulo m_k. Sea a el resto de A módulo m_k y sea q el resto de h(v+m_k−a) módulo m_k. Tomamos A'=A+Mq y M'=Mm_k. El nuevo residuo es v, los anteriores se conservan y la coprimalidad futura se mantiene por el lema del producto. No se exige A'<M': ese bound es innecesario. Los residuos anteriores son testigos existenciales en el invariante, no una función elegida. En k=L se elimina M y queda A. La fórmula del invariante está en L_A tras expandir gcd, congruencia y abreviaturas; la inducción PA permite la complejidad de Q. $\square$

## 22.7. Codificación β uniforme de familias finitas definibles

### Metateorema 22.7.1 — Codificación β uniforme de familias finitas definibles {#tlog-mth-00125}

**Metateorema.** Para cada Q(i,v,\vec z), PA demuestra
$$
\forall i<L\exists v\,Q(i,v,\vec z)\ \to\
\exists a,b\,\forall i<L\exists v\,[Q(i,v,\vec z)\land B(a,b,i,v)].\tag{β-int}
$$
Si los valores de Q son únicos, se codifica exactamente esa familia. L sigue siendo un parámetro separado: β no se vuelve inyectiva ni registra longitud.

**Prueba.** §22.5 proporciona V que acota testigos. §22.4 proporciona b>V múltiplo de1,…,L. Entonces v<V<m_i. Aplicamos CRT a Q(i,v)∧v<V y obtenemos a con los restos correctos. La definición B de CH19 es la relación de resto y PA demuestra su unicidad; el cociente está acotado por a porque m_i≥1. En L=0 la condición es vacua y a=0,b=1 sirven. Todos los testigos son existenciales en una prueba PA; no se sustituye la longitud variable por un numeral estándar. $\square$

## 22.8. Extensión y recodificación de una tabla β

### Lema 22.8.1 — Extensión y recodificación de una tabla β {#tlog-lem-00096}

**Lema.** PA demuestra que una tabla (a,b,L) puede extenderse con cualquier valor v al índice L, recodificándose en (a',b',L+1) que conserva exactamente los índices i<L. También puede recodificarse una familia finita de testigos de fórmulas Σ1.

**Prueba.** Aplicamos (β-int) a Q(i,w)=(i<L∧B(a,b,i,w))∨(i=L∧w=v), sobre L+1. La unicidad de B y la exclusión de casos dan conservación. Para una fórmula ∃\vec u δ(i,\vec u) con δ Δ0, la colección finita aplicada sucesivamente a su número fijo de componentes acota los testigos; (β-int) codifica cada componente en una tabla. Los valores recuperados están acotados por1+Lb de su tabla y los cocientes por a, por lo que su lectura tiene matriz Δ0. Así PA demuestra la equivalencia entre ∀i<L∃\vec u δ y una fórmula Σ1 que comienza con los parámetros de esas tablas y cotas, seguida de una matriz con sólo cuantificadores acotados. Esta normalización de cuantificadores acotados sobre Σ1 usará la colección ya demostrada, no una clausura supuesta. $\square$

## 22.9. Representación PR con ecuaciones y totalización PA

### Metateorema 22.9.1 — Representación PR con ecuaciones y totalización PA {#tlog-mth-00126}

**Metateorema.** De cada descripción PR de f se construye una fórmula literal Σ1 F_f(\vec x,y) tal que: (a) su extensión estándar es el grafo de f; (b) PA⊢∀\vec x∃!yF_f(\vec x,y); (c) PA demuestra sus ecuaciones de definición. La construcción es efectiva sobre descripciones finitas. No incluye minimización no acotada ni todas las máquinas totales externas.

**Prueba por inducción sobre la descripción.** Para cero, sucesor y proyecciones se usan las igualdades correspondientes. Composición introduce valores intermedios y sus grafos; sus bloques existenciales se anteponen con nombres frescos. Existencia y unicidad siguen de las de los componentes.

Para recursión, el grafo afirma que existe una tabla β de n+1 valores, el primero satisface F_g(\vec x,v_0), cada par consecutivo satisface F_h(\vec x,i,v_i,v_{i+1}) para i<n y el último es y. Las lecturas B son únicas. Los testigos de los grafos componentes se codifican por §22.8 y se acotan sus lecturas; queda un prefijo existencial y una matriz Δ0. PA prueba existencia por inducción en n: para0 toma el valor inicial y lo codifica; en el paso usa totalización de h y recodifica el historial y sus testigos por §22.8. Prueba unicidad comparando dos historiales por inducción en i≤n. El mismo argumento identifica el último valor en0 y n+1, dando las ecuaciones. Estándarmente la recurrencia única coincide con f por inducción externa. Las instancias numerales se prueban por evaluación finita de esas ecuaciones; las negativas para valores incorrectos siguen de unicidad.

En cada descripción se fija el orden de componentes, de tablas y de testigos, y los nombres frescos mínimos fuera de los parámetros. Esta elección determina un árbol literal F_f; formas lógicamente equivalentes no reciben su código. La totalización interna se obtiene de la inducción y (β-int), no de la verdad estándar de «f es total». $\square$

## 22.10. Uso conservador de símbolos PR auxiliares

### Proposición 22.10.1 — Uso conservador de símbolos PR auxiliares {#tlog-pro-00139}

**Proposición.** Podemos razonar en una extensión definicional PA_PR que agrega un símbolo para cada función PR utilizada y el axioma F_f(\vec x,f(\vec x)). Cada prueba finita se elimina efectivamente a una prueba PA de su traducción en L_A. No agregamos un axioma matemático de totalización.

**Prueba.** PA ya demuestra existencia y unicidad de F_f. En un término se introducen variables frescas para sus valores, se añaden sus grafos y se elimina el símbolo. Unicidad prueba independencia de esas variables y sustitución por igualdad. Inducción estructural sobre fórmulas transporta conectivos y cuantificadores; una instancia de inducción extendida se traduce a la instancia de inducción PA de la fórmula traducida, con sus parámetros. Sólo aparecen finitísimos símbolos en una derivación: se eliminan en el orden de sus descripciones. Las ecuaciones usadas como lemas tienen pruebas PA por §22.9. La abreviatura funcional sirve para exponer los invariantes; toda fórmula que se cite o se codifique se expande en L_A con higiene. $\square$

## 22.11. Operaciones sintácticas PR para S y G

### Lema 22.11.1 — Operaciones sintácticas PR para S y G {#tlog-lem-00097}

**Lema.** Los decodificadores S/G, validez de expresiones de L_A, longitudes y entradas de listas, concatenación, cambio de referencias, Num y sustitución literal de numerales son PR. Se puede escoger una descripción PR finita para cada operación; sus invariantes de construcción son demostrables en PA_PR.

**Prueba.** Para p(a,b)=(a+b)^2+a, la raíz entera se busca hasta c, y se valida el resto r≤raíz. En S([a]+s)=1+p(a,S(s)), ambos componentes son menores que el código positivo. Una lista se decodifica en a lo sumo c pasos, reteniendo un flag de invalidez; las entradas ausentes dan0. Para G se recorre la tabla de resultados para todos los códigos k≤c: los hijos sintácticos de un código válido k son menores que k. La recursión por valores anteriores se implementa guardando la tabla en un estado S y añadiendo un valor en cada paso. El constructor S es PR al iterar p sobre la lista finita; su tamaño puede crecer sin estar acotado por c, lo que no afecta la recursión PR.

Las guardas comprueban tags0,…,10, aridades0/1/2 de funciones y2 de <, listas exactas, cinco conectivos y ambos cuantificadores; las variables tienen índices arbitrarios. Num es recursión en n que envuelve S alrededor del término0. Sustitución literal recorre los hijos menores; detiene el descenso bajo el cuantificador de la variable sustituida e inserta el término sin volver a recorrerlo. Por ser numeral cerrado no hay captura. Invalidez da el sentinel0. PA_PR prueba por inducción en k la concordancia de cada tabla con estas ecuaciones, y por inducción en longitud las de listas/concatenación. Esta prueba no añade equivalencia α a la igualdad literal de códigos. $\square$

## 22.12. Verificador certificado PR y rama PA

### Lema 22.12.1 — Verificador certificado PR y rama PA {#tlog-lem-00098}

**Lema.** Para cada presentación T se escoge una descripción PR χ_T(d,c), con valores0/1, de su verificador certificado C_T. Existe además una transformación PR que certifica cualquier línea marcada como axioma PA mediante la rama de aceptación PA del semidecidor adicional. Sus invariantes son demostrables en PA_PR.

**Prueba.** χ_T recorre la lista S de líneas, no vacía, y rechaza contextos premisa de tipo0. Tipo1 comprueba un certificado lógico finito; tipo2 comprueba referencias previas y los árboles literales A,A→B,B; tipo3 comprueba una traza finita de la máquina adicional fija sobre el código de la fórmula, con inicio, pasos correctos y HALT final. No ejecuta esa máquina hasta que pare: cada lectura y transición está acotada por la longitud de la traza dada. Su salida final es irrelevante, incluso0. Todas las guardas son operaciones PR y los bucles están acotados por los códigos recibidos.

El comprobador de axiomas PA retira sucesivamente prefijos ∀; reconoce ocho bases por árboles y el esquema de inducción reconstruyendo sus dos sustituciones desde la conclusión ∀xA. El de certificados lógicos verifica directamente el testigo de esquema/igualdad suministrado, sin búsqueda no acotada. El número de nodos/entradas visitados está acotado por los respectivos códigos, y cada paso es PR. Para semidecidir A_T se fija expresamente una **rama inicial**: si el comprobador PA acepta c, HALT; si rechaza, comienza la intercalación sobre Γ. Compilamos ese comprobador PR por bucles acotados RM (recursión→contador, composición→macros de CH17). Por inducción sobre los bucles, su número de pasos, estados y lista de traza son funciones PR, y PA_PR demuestra que forman una traza válida hasta la primera parada para un c aceptado. Así una instancia variable de un axioma PA admite certificado tipo3 sin recurrir a una parada desconocida del semidecidor Γ.

Para la parte Γ sólo se verifican trazas aportadas; jamás se declara tiempo PR para todas sus aceptaciones. La rama PA se fija en la presentación del **nuevo** predicado, y no altera la teoría deductiva T ni los códigos de pruebas antiguos. $\square$

## 22.13. Representante seleccionado de pruebas

### Definición 22.13.1 — Representante seleccionado de pruebas {#tlog-def-00157}

Fijamos la descripción PR de χ_T de §22.12 y su grafo Σ1 F_{χ_T} construido en §22.9. Definimos, con variables frescas y prenexo fijado:
$$
\Pr_T^*(d,c):=F_{χ_T}(d,c,1),\qquad
\operatorname{Prov}_T^*(c):=\exists d\Pr_T^*(d,c).
$$
El1 es el numeral S0 del lenguaje aritmético. Estas fórmulas son literalmente Σ1 tras la expansión elegida. En PA_PR la fórmula $\Pr_T^*(d,c)$ es equivalentemente χ_T(d,c)=1; esa equivalencia PA demostrable permite verificar invariantes por ecuaciones PR. La lectura estándar de Pr* es la misma relación externa C_T, pero el árbol del representante no es la simulación RM arbitraria de CH21.

Para PA se escoge Γ vacía con semidecidor que nunca para; la rama PA permanece. Cada presentación tiene su propio programa fijo, descripción PR, grafo y árbol Prov*. Los índices de variables y el orden de expansión se fijan antes de formar una instancia y citar su código.

## 22.14. Exactitud estándar y condición D1

### Metateorema 22.14.1 — Exactitud estándar y condición D1 {#tlog-mth-00127}

**Metateorema.** Para cada sentencia A,
$$
\mathbb N_A\models\operatorname{Prov}_T^*(\ulcorner A\urcorner)
\iff T\vdash A.
$$
Además T⊢A implica **PA⊢Prov_T^*(⌜A⌝)** y por tanto T⊢Prov_T^*(⌜A⌝) (D1). No se requiere consistencia ni corrección de T.

**Prueba.** Exactitud del grafo PR, del verificador y de la certificación dan el bicondicional estándar. Dada una prueba externa T de A, se escoge un certificado estándar d de esa prueba; su comprobación finita produce por las ecuaciones PR una prueba PA de F_{χ_T}(d̄,⌜A⌝,1). Introducción existencial da la conclusión. Ésta es una transformación sobre una prueba realmente aportada, no una regla «de □A obtener A» ni un axioma de reflexión. $\square$

## 22.15. Ensamblaje de certificados y conservación interna

### Lema 22.15.1 — Ensamblaje de certificados y conservación interna {#tlog-lem-00099}

**Lema.** Existe una función PR J(d,e) que concatena una prueba de A→B y una de A y añade MP con conclusión B. PA demuestra, en notación conservadora y bajo códigos válidos de las sentencias,
$$
\Pr_T^*(d,\operatorname{Imp}(a,b))\land\Pr_T^*(e,a)
\to\Pr_T^*(J(d,e),b).\tag{J}
$$
Imp(a,b) es el constructor literal de tag7. Para datos inválidos J devuelve0; esa rama no interviene bajo la antecedente.

**Prueba interna.** Sean l,m las longitudes positivas de d,e. Copiamos las primeras l líneas. En cada línea de e cambiamos sólo las referencias MP internas i,j a l+i,l+j; todos sus árboles, certificados lógicos y trazas adicionales se copian íntegros. Añadimos la línea $S([2,b,l+m−1,l−1])$, donde $b=G(B)$: la primera referencia MP es la línea de $A$ de la segunda prueba y la segunda es la línea de $A→B$ de la primera. Este orden es el de §18.34. PA_PR prueba por inducción sobre las líneas copiadas que cada fórmula y certificado coincide con el original, que una referencia anterior sigue siendo anterior, y que las fórmulas de las referencias ajustadas son las originales. Las guardas de tipo1/3 no dependen de la posición; las de tipo2 quedan preservadas por ese invariante. La última línea satisface exactamente el constructor Imp(a,b), sin equivalencia α. El plegado S reconstruye la lista y su conclusión. Las ecuaciones de χ_T prueban que su valor es1; se elimina PA_PR por §22.10. No se ha necesitado generar nuevas trazas Γ ni decidir si un axioma sin certificado pertenece a Γ. $\square$

## 22.16. Condición interna D2

### Metateorema 22.16.1 — Condición interna D2 {#tlog-mth-00128}

**Metateorema.** Para A,B sentencias concretas, PA y T demuestran
$$
\operatorname{Prov}_T^*(\ulcorner A\to B\urcorner)
\to(\operatorname{Prov}_T^*(\ulcorner A\urcorner)\to
\operatorname{Prov}_T^*(\ulcorner B\urcorner)).\tag{D2}
$$
**Prueba.** Expandimos ambas existencias de certificados d,e con nombres frescos, aplicamos (J), introducimos el testigo J(d,e) para la conclusión y descargamos los dos testigos. El constructor Imp aplicado a los numerales de códigos a,b da el numeral del código de A→B por sus ecuaciones. Eliminamos los símbolos PR auxiliares; queda una prueba PA de la fórmula indicada. Esta prueba cuantifica internamente sobre todos los certificados, también los de un modelo no estándar. D1 externa por sí sola no habría bastado. $\square$

## 22.17. Pruebas aritméticas numerales generadas uniformemente

### Lema 22.17.1 — Pruebas aritméticas numerales generadas uniformemente {#tlog-lem-00100}

**Lema.** Para cada término aritmético fijo t(\vec x), hay generadores PR de su valor y de un certificado PA de t(\bar{\vec n})=\overline{t(\vec n)}. PA demuestra la corrección de esos certificados para argumentos variables, mediante sus ecuaciones. Hay generadores positivos/negativos análogos para las comparaciones atómicas de términos.

**Prueba.** Inducción sobre el término: variable y0 usan reflexividad; sucesor usa congruencia. Para suma de numerales iteramos x+0=x y x+Sy=S(x+y) sobre el segundo argumento, ensamblando MP y transporte por igualdad en cada paso. Para producto iteramos x·0=0 y x·Sy=x·y+x y usamos el generador de suma. PA_PR prueba por inducción sobre ese argumento que la conclusión de cada certificado es la igualdad requerida y que todas sus líneas pasan χ_T. Las instancias de axiomas PA usan las trazas PR de la rama PA; las lógicas usan certificados directos. Referencias se ajustan por §22.15.

Para igualdad de numerales, si los valores son iguales usamos reflexividad; si difieren cancelamos sucesores hasta separar0 de un sucesor, usando inyectividad de S y Sx≠0. Para <, su axioma y esas igualdades dan las pruebas en el caso positivo; en el negativo usamos orden y el segmento numeral. El generador de un segmento de longitud n se construye por recursión: agrega el nuevo caso a la disyunción de los casos anteriores usando el paso de orden y sustitución por igualdad. PA_PR demuestra el invariante por inducción en n. Así se **internaliza** el corte finito de CH19/21 mediante un generador y una prueba de validación, sin pasar de «todas las instancias estándar» a una universal. $\square$

## 22.18. Certificación uniforme de verdad y falsedad Δ0

### Lema 22.18.1 — Certificación uniforme de verdad y falsedad Δ0 {#tlog-lem-00101}

**Lema.** Para cada fórmula Δ0 fija δ(\vec x) se construyen funciones PR E_δ, q_δ^+,q_δ^- de evaluación y certificados, y PA demuestra
$$
δ(\vec x)\leftrightarrow E_δ(\vec x)=1,
\quad δ(\vec x)\to\Pr_T^*(q_δ^+(\vec x),\operatorname{Inst}_δ(\vec x)),
$$
$$
\neg δ(\vec x)\to\Pr_T^*(q_δ^-(\vec x),\operatorname{Neg}(\operatorname{Inst}_δ(\vec x))).\tag{Δ-cert}
$$
Inst_δ sustituye numerales en las coordenadas libres; δ es fija y puede tener parámetros. Neg es tag4. Los códigos de conclusión son literales, después de las sustituciones.

**Prueba por inducción estructural, simultánea para ambas polaridades.** Atómicas: §22.17. Para cada uno de ¬,∧,∨,→,↔ se evalúan los bits de las subfórmulas; una de sus finitísimas filas de verdad determina las pruebas positivas o negativas requeridas. Se copian sus certificados y se agrega una derivación proposicional fija de la conclusión. Que ésta acepta se prueba por las ecuaciones de ensamblaje y las guardas de los esquemas H; no se agrega una regla nueva.

Para ∃z<t(\vec x)ψ, se calcula el valor N del bound. El bucle i<N evalúa ψ con el numeral i. Si algún bit es1, el primer testigo proporciona certificado de ψ y de i<N y se agrega introducción existencial. Si todos son0, se ensamblan sus certificados negativos, el certificado de segmento z<N↔(z=0∨…∨z=N−1), y se aplica eliminación de casos/igualdad para obtener ∀z<N¬ψ, luego ¬∃z<Nψ. El caso ∀z<tψ usa todas las pruebas positivas o un contraejemplo negativo. Para N=0 la universal acotada se prueba por vacuidad y la existencial se refuta sin testigos. El bound no contiene z; los ligadores se higienizan antes de instanciar.

Estos bucles son PR aunque el **tamaño** de sus certificados crezca mucho. PA_PR prueba sus invariantes por inducción en la longitud recorrida: «el prefijo tiene los bits correctos, los certificados de la polaridad elegida son válidos, y la derivación de casos de ese prefijo tiene la conclusión reconstruida». El paso es exactamente el ensamblaje y el paso de segmento de §22.17; el certificado de la clausura universal usa la generalización admisible compilada mediante prefijos de axiomas y Q3, sin generalizar una premisa abierta. La construcción prueba validación del código de la derivación, no reflexión sobre lo que dice. Eliminando PA_PR se obtienen (Δ-cert). $\square$

## 22.19. Completitud Σ1 interna para el representante elegido

### Metateorema 22.19.1 — Completitud Σ1 interna para el representante elegido {#tlog-mth-00129}

**Metateorema.** Para cada fórmula literal Σ1 fija σ(\vec x), PA demuestra
$$
σ(\vec x)\to\operatorname{Prov}_T^*(\operatorname{Inst}_σ(\vec x)).\tag{Σ-cert}
$$
En particular para cada sentencia Σ1 concreta σ,
PA⊢σ→Prov_T^*(⌜σ⌝). Esto no es corrección Σ1 de T.

**Prueba.** Escribimos σ=∃\vec u δ(\vec x,\vec u), matriz Δ0. Bajo δ, (Δ-cert) aporta un certificado positivo de su instancia numeral. Una transformación PR agrega, de adentro hacia afuera, la introducción de cada existencial con los numerales de los testigos \vec u; su conclusión literal es la instancia de σ en \vec x. Las instancias de cuantificación admiten esos términos cerrados y sus certificados lógicos pasan las guardas. PA_PR comprueba por inducción sobre el número fijo de cuantificadores el código final y la validez; introducimos el certificado existencial y eliminamos los testigos \vec u. Para prefijo vacío se aplica directamente (Δ-cert). Al expandir funciones auxiliares queda una prueba PA. En el caso cerrado Inst_σ es constante G(σ), por las ecuaciones sintácticas.

La dirección es **de la fórmula Σ1 a la afirmación de prueba**, no de ésta a la fórmula. No existe aquí una función que, sin disponer de un testigo, decida todas las verdades Σ1; la existencia del certificado es conclusión dentro de PA bajo σ. $\square$

## 22.20. Condición interna D3 e identificación de la instancia

### Metateorema 22.20.1 — Condición interna D3 e identificación de la instancia {#tlog-mth-00130}

**Metateorema.** Para cada sentencia A, PA y T demuestran
$$
\operatorname{Prov}_T^*(\ulcorner A\urcorner)\to
\operatorname{Prov}_T^*(\ulcorner\operatorname{Prov}_T^*(\ulcorner A\urcorner)\urcorner).\tag{D3}
$$
**Prueba.** La sentencia σ=Prov_T^*(\overline{G(A)}) es literal Σ1. Aplicamos (Σ-cert) a esa **sentencia cerrada**, cuyo árbol se forma insertando el numeral G(A) en el representante abierto previamente fijado. Su código exterior es G(σ). No es G(A), ni el código del árbol abierto de Prov*. No se utilizan corrección de T ni su consistencia. D3 se prueba mediante certificados aritméticos y colección finita interna, no mediante la repetición externa de D1. $\square$

## 22.21. Abreviatura de caja y consistencia interna

### Definición 22.21.1 — Abreviatura de caja y consistencia interna {#tlog-def-00158}

Para una sentencia A fijamos $\square_T A:=\operatorname{Prov}_T^*(\overline{G(A)})$. La caja es notación metalingüística para una fórmula aritmética, no un sexto conectivo. En □□A la caja exterior nombra el código literal de la instancia interior.

Fijamos $\bot_A:=(0=S0)$, q=G(\bot_A), y
$$
\operatorname{Con}^*(T):=\neg\operatorname{Prov}_T^*(\bar q)=\neg\square_T\bot_A.
$$
La sentencia es equivalente en PA a una fórmula Π1 al negar el prefijo Σ1 elegido; no declaramos que su árbol de negación con prefijo existencial ya sea literalmente Π1. PA demuestra ¬\bot_A por Sx≠0. En el exterior «T consistente» significa T⊬\bot_A, equivalentemente ausencia de pruebas de un par A,¬A por lógica clásica. Con*(T) es una fórmula de una presentación y representante determinados, distinta de esa aserción externa hasta interpretar la estructura estándar.

## 22.22. Cálculo de caja derivado de D1–D3

### Lema 22.22.1 — Cálculo de caja derivado de D1–D3 {#tlog-lem-00102}

**Lema.** Si PA⊢A→B, entonces PA⊢□A→□B. Si PA⊢A↔B, entonces PA⊢□A↔□B. PA demuestra □A∧□B→□(A∧B). Toda instancia □A→□□A es demostrable PA. Si T⊢A→B, la primera transformación sigue dando una prueba PA de □A→□B.

**Prueba.** D1 proporciona una prueba PA de □(A→B), incluso cuando la prueba aportada era T; D2 y MP dan la transformación. Aplicamos esto a las dos implicaciones del bicondicional. Para conjunción usamos el teorema proposicional A→(B→A∧B), D1 y dos D2. La última cláusula es D3. Las fórmulas bajo cajas son sentencias literales fijadas; equivalencia demostrable permite derivar cajas equivalentes, no igualar sus códigos. No se admite una regla de necessitación **sobre hipótesis locales**: D1 sólo se aplica a teoremas completos. $\square$

## 22.23. Sentencia de Gödel para la nueva caja

### Definición 22.23.1 — Sentencia de Gödel para la nueva caja {#tlog-def-00159}

Aplicamos el compilador diagonal de CH20 al árbol fijado ¬Prov_T^*(z), con coordenada y variables frescas aprobadas. Llamamos G_T^* a la sentencia producida, g=G(G_T^*). Se entrega una prueba PA de
$$
G_T^*\leftrightarrow\neg\square_TG_T^*.\tag{G*}
$$
El código g es el del resultado final, no el auxiliar abierto. Esta elección no renombra G_T de CH21 ni G_PA de CH20. El bicondicional tiene prueba PA para toda presentación T, sin hipótesis de consistencia. El código puede ser enorme; no lo sustituimos por un número pequeño de ejemplo.

## 22.24. Internalización de la contradicción de Gödel

### Lema 22.24.1 — Internalización de la contradicción de Gödel {#tlog-lem-00103}

**Lema.** PA demuestra □G_T^*→□\bot_A.

**Prueba.** De (G*) obtenemos el teorema PA G*→¬□G*. D1/D2 dan □G*→□¬□G*. D3 da □G*→□□G*. En PA, ¬□G* implica □G*→\bot_A por lógica; la transformación de cajas del lema anterior da □¬□G*→□(□G*→\bot_A). D2 aplicada a esa implicación, junto con □□G*, concluye □\bot_A. Así cada uso de D1 recae sobre un teorema, cada uso de D2 es una instancia interna y la introspección requerida es explícitamente D3. No se convierte ¬□G* en una refutación de cada certificado variable por una inferencia externa. $\square$

## 22.25. Equivalencia interna entre consistencia y Gödel elegido

### Metateorema 22.25.1 — Equivalencia interna entre consistencia y Gödel elegido {#tlog-mth-00131}

**Metateorema.** PA demuestra Con*(T)↔G_T^*. No se requiere consistencia de T para esta derivación.

**Prueba.** Por contraposición del lema anterior, ¬□\bot_A→¬□G*. (G*) transforma la conclusión en G*, dando Con*→G*. Para la vuelta, PA demuestra \bot_A→G* por explosión; el cálculo de caja da □\bot_A→□G*. De (G*) tenemos G*→¬□G*, luego G*→¬□\bot_A. Se ensamblan ambas implicaciones. Es una equivalencia de fórmulas dentro de PA, no una prueba PA de ninguna de ellas. $\square$

## 22.26. Segundo teorema de incompletitud

### Metateorema 22.26.1 — Segundo teorema de incompletitud {#tlog-mth-00132}

**Metateorema.** Si T es una presentación admisible **consistente**, entonces
$$
T\nvdash\operatorname{Con}^*(T).
$$
La hipótesis es consistencia simple; no se requiere ω-consistencia, corrección Σ1 ni corrección estándar de T.

**Prueba.** Primero T no demuestra G*: si lo hiciera, D1 daría una prueba PA, por tanto T, de □G*. Pero (G*) y la supuesta prueba G* darían T⊢¬□G*. Lógica clásica produciría T⊢\bot_A, contradicción. Si T demostrase Con*(T), por la equivalencia PA de §22.25 demostraría G*, lo que acabamos de excluir. No se usó la no refutación de Gödel, ni Rosser, ni una suposición sobre modelos de T. $\square$

## 22.27. Aplicación a PA y verdad estándar de su consistencia

### Corolario 22.27.1 — Aplicación a PA y verdad estándar de su consistencia {#tlog-cor-00038}

**Corolario.** PA⊬Con*(PA), y N_A⊨Con*(PA). Para toda T consistente presentada, N_A⊨Con*(T).

**Prueba.** CH19 construyó N_A y demostró su satisfacción y la corrección externa de PA dentro de M_ext; por tanto PA es externamente consistente. Aplicamos el segundo teorema a su presentación con Γ vacía. Exactitud estándar de Prov* implica que la negación de existencia de prueba de \bot_A es verdadera exactamente cuando T es externamente consistente. Para una T cualquiera sólo se usa su consistencia asumida, no su corrección. La prueba externa de Cons(PA) no se ha traducido a una prueba PA de Con*(PA); hacer esa identificación sería precisamente el paso prohibido por el resultado. Nada se concluye sobre consistencia de ZF objeto. $\square$

## 22.28. Teorema de Löb y su forma internalizada

### Metateorema 22.28.1 — Teorema de Löb y su forma internalizada {#tlog-mth-00133}

**Metateorema.** Para cada sentencia A, PA demuestra
$$
\square_T(\square_T A\to A)\to\square_T A.\tag{L-int}
$$
Además, si T⊢□_T A→A, entonces T⊢A (regla de Löb). No se exige consistencia.

**Prueba.** Elegimos por diagonalización L con prueba PA de L↔(□L→A). De L→(□L→A), D1 y D2 dan □L→□(□L→A). Otra D2 da □L→(□□L→□A), y D3 concluye el teorema PA □L→□A. Proposicionalmente, este teorema implica que PA demuestra (□A→A)→(□L→A). Aplicamos D1 y D2 a **ese teorema**: PA demuestra □(□A→A)→□(□L→A). La otra mitad del bicondicional de L, con D1/D2, da □(□L→A)→□L. Encadenando se obtiene (L-int), con □L→□A.

Para la regla, si T⊢□A→A, D1 proporciona PA⊢□(□A→A); (L-int) da PA⊢□A. Dentro de T aplicamos MP con la hipótesis externa de que **□A→A es un teorema T**, y obtenemos A. La transformación distingue el teorema de una mera hipótesis local abierta: no hemos inferido □(□A→A) por necessitar un supuesto sin descargar. $\square$

## 22.29. Reflexión local y segunda prueba del segundo teorema

### Corolario 22.29.1 — Reflexión local y segunda prueba del segundo teorema {#tlog-cor-00039}

**Corolario.** Para cada sentencia A, T⊢(□_T A→A) si y sólo si T⊢A. Si T es consistente, T no demuestra su esquema completo de reflexión local para esta caja; en particular no demuestra □\bot_A→\bot_A.

**Prueba.** La dirección difícil es Löb; la fácil es lógica proposicional a partir de una prueba A. Para \bot_A, una prueba de □\bot_A→\bot_A daría por Löb una prueba de \bot_A. PA demuestra ¬\bot_A, por lo que □\bot_A→\bot_A es equivalente a ¬□\bot_A=Con*(T). Ésta es otra demostración del segundo teorema. Es un esquema de sentencias por A externa; no se introduce un predicado aritmético de verdad para todas las fórmulas ni se identifica reflexión con corrección estándar de T. $\square$

## 22.30. Puntos fijos afirmativos para la caja seleccionada

### Proposición 22.30.1 — Puntos fijos afirmativos para la caja seleccionada {#tlog-pro-00140}

**Proposición.** Si PA demuestra H↔□_T H para una sentencia H, entonces T demuestra H; de hecho PA demuestra H para la caja seleccionada.

**Prueba.** PA demuestra □H→H; D1, (L-int) y MP dan una prueba PA de □H. MP con □H→H da PA⊢H. La construcción diagonal permite escoger tal H. Esto no es el argumento «H se prueba a sí misma»: se usa la propiedad demostrada de la caja y el lema diagonal. La H_PA original de CH20 tenía otro representante; esta conclusión no se aplica a su árbol sin demostrar previamente una equivalencia interna suficiente entre predicados. No se intercambian sus códigos. $\square$

## 22.31. Variantes de la fórmula de consistencia

### Proposición 22.31.1 — Variantes de la fórmula de consistencia {#tlog-pro-00141}

**Proposición.** Sustituir \bot_A por una sentencia B con PA⊢B↔\bot_A da una fórmula ¬□B PA equivalente a Con*(T), y por tanto no demostrable en T consistente. La negación prenexa Π1 de Prov* también es equivalente PA, si se conserva el numeral del código de \bot_A.

**Prueba.** Transporte de cajas a través de equivalencia PA da □B↔□\bot_A; negar da la conclusión. Para el prenexo, de ¬∃\vec w δ pasamos a ∀\vec w¬δ con nombres frescos, sin modificar el **objeto citado** \bot_A. La equivalencia es de fórmulas de consistencia, cuyos códigos pueden ser distintos. No autoriza cambiar el representante de demostrabilidad por una fórmula sólo estándarmente equivalente. $\square$

## 22.32. Dependencia del representante y contraste Rosser

### Proposición 22.32.1 — Dependencia del representante y contraste Rosser {#tlog-pro-00142}

**Proposición.** Exactitud estándar y representación numeral no bastan para atribuir D2/D3 a otro representante. Un contraste explícito es la variante Rosser
$$
\operatorname{RProv}_T(c):=\exists d[\Pr_T^*(d,c)\land
\forall e\le d\,\neg\Pr_T^*(e,\operatorname{Neg}(c))],
$$
con Neg expandida por su grafo y el caso de códigos válidos. Para T consistente, estándarmente RProv y Prov* coinciden sobre sentencias, pero PA demuestra ¬RProv_T(⌜\bot_A⌝). Por ello esta variante no puede satisfacer conjuntamente D1–D3 en una T consistente.

**Prueba.** Si T prueba A, consistencia excluye todas las pruebas de ¬A; cualquier certificado de A sirve. La vuelta es inmediata por el testigo d. Para la conclusión interna fijamos un certificado estándar n de la prueba PA de ¬\bot_A. Cada d<n se comprueba externamente: ninguno es certificado de \bot_A, pues PA/T contiene ¬\bot_A y suponemos consistencia de T. Sus negativas numerales son demostrables PA por las ecuaciones PR. El corte finito produce PA⊢∀d<n¬Pr*(d,q). Para d≥n, la prueba PA del certificado n de ¬\bot_A, con el testigo e=n, refuta la condición Rosser. Orden y generalización concluyen ¬RProv(q). Estos son finitísimos controles dependientes de la presentación T y n, no reflexión uniforme. Si todas las condiciones se cumplieran, la demostración del segundo teorema con esa caja prohibiría tal teorema PA. El representante Rosser no se declara Σ1 o Π1 por su sola escritura; el argumento usa el corte finito y la negación citada correcta. $\square$

## 22.33. Extensiones por consistencia y por su negación

### Metateorema 22.33.1 — Extensiones por consistencia y por su negación {#tlog-mth-00134}

**Metateorema.** Si T es consistente y presentada, T+¬Con*(T) es consistente y admite una presentación efectiva. Si T es además correcto estándarmente, también T+Con*(T) es consistente. Para PA ambas extensiones son consistentes; la primera es incorrecta Σ1.

**Prueba.** Si T+¬Con* fuese inconsistente, deducción y lógica clásica darían T⊢Con*, contradiciendo el segundo teorema. Añadir una sentencia fija conserva semidecidibilidad de axiomas. Si T es correcto, N_A satisface T y Con*(T), luego también sus consecuencias y la extensión es consistente. La corrección PA ya está probada externamente, por lo que ambos casos se aplican. PA+¬Con*(PA) demuestra □_{PA}\bot_A, una sentencia Σ1 falsa en N_A por Cons(PA); queda demostrada su incorrección Σ1. No se deduce consistencia de T+Con* de la mera consistencia de T: una T consistente puede ya demostrar ¬Con*(T). La nueva teoría tiene un **nuevo** predicado de demostrabilidad; su propia consistencia no se identifica con la antigua Con*(T). $\square$

## 22.34. Lectura condicional en modelos no estándar

### Proposición 22.34.1 — Lectura condicional en modelos no estándar {#tlog-pro-00143}

**Proposición.** Si existe una estructura M que satisface PA+¬Con*(PA), en M hay un elemento d que satisface Pr_PA^*(d,q), y tal d no es la interpretación de ningún numeral estándar. No se presupone aquí la existencia de ese modelo.

**Prueba.** Negar Con* y eliminar doble negación/existencial da el testigo d en M. Para cada natural estándar k, el verificador externo rechaza C_PA(k,q), porque PA es consistente. Las ecuaciones PR y unicidad del grafo dan PA⊢¬Pr*(k̄,q). Toda M que satisface PA satisface cada instancia, por lo que d≠k̄^M para cada k estándar. «No estándar» describe este hecho externo; no es un predicado definible de M ni una auténtica derivación PA finita del exterior. Su traza y su longitud interna pueden ser no estándar. No se ha inferido un modelo de ZF objeto ni se ha confundido satisfacción con código sintáctico. $\square$

## 22.35. Presentaciones y transferencia legítima

### Proposición 22.35.1 — Presentaciones y transferencia legítima {#tlog-pro-00144}

**Proposición.** Dos presentaciones externas de la misma teoría deductiva producen predicados con la misma extensión estándar, pero sus fórmulas internas de consistencia no se identifican automáticamente. Una prueba PA de equivalencia uniforme de sus predicados sí permite transferir la consistencia interna y sus conclusiones de no demostrabilidad.

**Prueba.** Exactitud estándar da la coincidencia a partir de igualdad externa de teoremas. Si PA⊢∀c(Prov_1(c)↔Prov_2(c)), particularizamos al numeral q y negamos: PA⊢Con_1↔Con_2. El segundo teorema para una implica no prueba T de la otra. También basta la equivalencia en q para esa transferencia concreta. La coincidencia numeral bilateral individual no produce la universal. Los antiguos Prov_PA y V_T permanecen con su contrato de CH19/21: el capítulo no afirma sin prueba sus D2/D3 ni los reemplaza en sus sentencias antiguas. La realización aprobada del segundo teorema es para Prov*. $\square$

## 22.36. Alcance del límite y frontera intertratados

### Proposición 22.36.1 — Alcance del límite y frontera intertratados {#tlog-pro-00145}

**Proposición.** El segundo teorema no excluye pruebas de consistencia de T en una teoría externa más fuerte, ni pruebas de consistencia de fragmentos propios en T. Tampoco demuestra inconsistencia de T cuando T no prueba Con*(T).

**Prueba.** La conclusión tiene exactamente la forma «Cons externa(T)⇒T⊬Con*(T)». Su antecedente no se invierte ni se deduce de la ausencia de prueba. Cambiar la teoría donde se demuestra la sentencia modifica esa conclusión; cambiar el objeto T por un fragmento cambia el predicado y el código de consistencia. La prueba externa de Cons(PA) en M_ext es compatible con su no demostrabilidad PA. Para ZF objeto u otra teoría intertratados se requieren una presentación efectiva, interpretación de la aritmética, conservación de derivaciones y representante con condiciones verificadas; no están dados por el nombre de la teoría. Interfaces activas siguen0. CH23 tratará indecidibilidad y la frontera GAS; no incorporamos MRDP/Jones, equivalencia RM–Turing ni una axiomatización de verdad. $\square$

## 22.37. Cierre del segundo teorema y contrato final

### Corolario 22.37.1 — Cierre del segundo teorema y contrato final {#tlog-cor-00040}

**Corolario.** Para la clase presentada de extensiones PA, CH22 fija un representante explícito y construible a partir del verificador certificado, prueba D1–D3 y demuestra el segundo teorema bajo consistencia simple. La codificación β interna y la representación PR justifican las transformaciones uniformes; la certificación Δ0 justifica completitud Σ1 interna y D3. Se prueban además Löb, su forma internalizada, la equivalencia de Con* con el Gödel elegido y los controles de extensiones y variantes.

**Prueba.** Los proveedores citados forman una cadena finita desde las codificaciones y PA de capítulos previos; ninguna arista exige resultados de CH23. Se han mantenido distintos verdad estándar, consistencia externa, fórmula Con*, validación de certificados y reflexión. Los árboles antiguos se conservan. La clausura humana no es una colección de derivaciones PA generadas y verificadas por software ni una formalización Lean. Parte V continúa abierta hasta CH23. $\square$

## 22.38. Lectura y balance

La codificación interna no afirma que todo programa externamente total sea PA total: la prueba uniforme abarca las descripciones PR construidas. La certificación Σ1 afirma σ→□σ, y no □σ→σ. Löb muestra por qué ese cambio de dirección es decisivo. Cons(PA) tiene una prueba externa en nuestra metateoría y su fórmula seleccionada es verdadera estándarmente, pero PA no la demuestra.

Un ejemplo pequeño del paso CRT usa residuos2,4,1 con b=6: los módulos7,13,19 son coprimos, y cualquier a que satisfaga esos residuos proporciona una tabla β de longitud3. Ese ejemplo se verifica numéricamente en las regresiones; no es una prueba PA de longitud variable ni un código de sentencia diagonal. La prueba interna utiliza el invariante de §22.6 y la inducción, no la generalización desde ejemplos.

El capítulo cierra **37/37 resultados**, con **167 aristas directas nuevas**. Acumulado **629 resultados / 2389 aristas**, sin ciclos, duplicados ni huérfanos. Lean **275 candidatos /0 compilados /0 verificados**. Partes I–IV CLOSED, ParteV OPEN:4/5 partes cerradas. Interfaces intertratados activas0; capítulos publicados0. Pruebas humanas, regresiones Python y cotejo íntegro de bytes desde Drive se acreditan por separado.

```text
LOCAL  CH22 ████████████████████ 37/37 resultados (100 %)
GLOBAL TLOG ███████████████████████░ 23/24 capítulos (95,83 %)
```

Próximo y último capítulo aprobado: **CH23 — Indecidibilidad, límites y frontera con GAS**.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 21](capitulo-21.md) · [Capítulo 23 →](capitulo-23.md)


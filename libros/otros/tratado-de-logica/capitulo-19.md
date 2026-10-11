---
title: Capítulo 19 — Representabilidad en aritmética
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
content-id: MA-BCH-0221
content-type: book-chapter
source-id: TLOG-CH19-0001
prerequisites:
- MA-BCH-0207
- MA-BCH-0211
- MA-BCH-0212
- MA-BCH-0219
- MA-BCH-0220
related:
- MA-BOK-0014
source-sha256: e5b198ccc6d34f11780edce571b370777ca5c1a16d50aff2e62d0b5e251d20c0
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 18](capitulo-18.md) · [Capítulo 20 →](capitulo-20.md)

## 19.0. De un algoritmo externo a una fórmula con pruebas

Los códigos del capítulo anterior hicieron posible que un programa fijo reconociera fórmulas y derivaciones. Una fórmula aritmética que habla de esos números es otro objeto: hace falta construirla y justificar qué pruebas permite. El puente se desarrollará sobre PA, presentada expresamente, con un modelo estándar externo; no se toma PA como abreviatura de los naturales internos de ZF objeto.

Primero fijaremos el lenguaje, la inducción y las nociones de representación. Después leeremos una tabla finita mediante restos β, construiremos una fórmula de ejecución de cada programa RM y probaremos su exactitud y funcionalidad. Finalmente aplicaremos ese teorema a las operaciones sintácticas y a los verificadores de prueba. El lema diagonal queda para CH20.

La ruta β se usa como auxiliar aritmético, conservando S/G como numeraciones canónicas. El CRT finito y Bézout se prueban aquí en ZF externa; no se presupone un teorema uniforme de codificación de tablas dentro de PA. Las pruebas de funcionalidad dentro de PA sí tienen sus inducciones declaradas. Las regresiones Python, la selección de candidatos Lean y el cotejo SHA-256 tienen informes separados.

## 19.1. Tres niveles y la nueva teoría aritmética objeto

### Convención 19.1.1 — Tres niveles y la nueva teoría aritmética objeto {#tlog-cnv-00030}

Trabajamos externamente en $M_{ext}=\mathrm{ZF}$ clásica, sin AC/BPI. RM sigue siendo el sistema operacional externo de §§17–18. $\mathrm{PA}$ será una teoría objeto de una signatura **aritmética nueva**, distinta de $\mathrm{ZF}_{obj}$. No se sustituyen los teoremas objeto de CH16 por axiomas de PA ni se usa un modelo supuesto de ZF objeto. La estructura estándar $\mathbb N$ se construye en la metateoría externa.

Para fórmulas aritméticas distinguiremos $\mathbb N\models A[\bar n]$, la afirmación externa $f(\bar n)=m$ y $\mathrm{PA}\vdash A(\overline{\bar n})$. Una prueba humana de la tercera afirmación describe una derivación finita del cálculo con MP y axiomas declarados; no equivale a un archivo verificado en Lean. Los razonamientos PA de este capítulo especifican inducciones, ecuaciones y reglas admisibles, pero no se anuncian como trazas mecánicas de todas sus instancias.

## 19.2. Signatura aritmética, numerales y abreviaturas

### Definición 19.2.1 — Signatura aritmética, numerales y abreviaturas {#tlog-def-00134}

Fijamos $L_A$ con igualdad lógica, constante $0$, función unaria $S$, funciones binarias $+$ y $\cdot$, y relación binaria $<$. Su presentación numérica usa índices funcionales $0,1,2,3$ respectivamente, con aridades $0,1,2,2$; el único índice relacional es $0$ con aridad 2. Ambos dominios son finitos decidibles y las aridades se totalizan por 0 fuera del dominio. Conservamos variables $x_i$, cinco conectivos primitivos y ambos cuantificadores. No se agrega exponenciación, función de lista o símbolo β.

El numeral $\bar n$ es el término $S^n(0)$, con $\bar0=0$. Es un término finito, distinto del natural $n$ y de su código $G(\bar n)$. $a\le b$ abrevia $(a<b)\lor(a=b)$; $a\ne b$ abrevia $\neg(a=b)$; $\exists z<t A$ abrevia $\exists z(z<t\land A)$ y $\forall z<t A$ abrevia $\forall z(z<t\to A)$, con $z$ ausente del término cota. Las cotas $\le$ se expanden mediante $S(t)$. Los nombres auxiliares siempre se escogen frescos por §18.23 antes de expandir. No se redefine $<$ conjuntista de CH16: el símbolo actual pertenece a $L_A$.

## 19.3. Axiomas de PA e inducción con parámetros

### Esquema axiomático 19.3.1 — Axiomas de PA e inducción con parámetros {#tlog-axm-00013}

Las ocho fórmulas base son las clausuras universales, en el orden escrito, de
$$
Sx\ne0;\quad Sx=Sy\to x=y;\quad x\ne0\to\exists z(x=Sz);
$$
$$
x+0=x;\quad x+Sy=S(x+y);\quad x\cdot0=0;\quad x\cdot Sy=x\cdot y+x;
$$
$$
x<y\leftrightarrow\exists z(y=x+Sz).
$$
Aquí $x=x_0,y=x_1,z=x_2$; cada fórmula base es cerrada cuantificando sus variables libres en orden creciente. Las ecuaciones sólo incluyen los variables que aparecen libres; $z$ en los dos existenciales no se cierra otra vez.

Para toda fórmula $A$ de $L_A$ y todo índice $i$, se añade la instancia abierta
$$
\mathsf{Ind}_i(A):=
\bigl(A[0/x_i]_{lit}\land\forall x_i(A\to A[Sx_i/x_i]_{lit})\bigr)\to\forall x_i A.
$$
Ambas sustituciones son seguras: 0 es cerrado y las únicas variables de $Sx_i$ son $x_i$, que un cuantificador homónimo bloquea. Las demás variables libres de A son parámetros. Se admiten $i\notin FV(A)$ y nombres ligados repetidos.

$A_{PA}$ consta de las ocho bases y de todas las instancias Ind, y de **todos sus prefijos universales finitos**, incluidos los vacíos. PA es el cálculo $\mathsf H_{L_A}^=+A_{PA}$, desde ninguna premisa adicional; su única regla primitiva sigue siendo MP. Esta presentación explicita también las instancias abiertas, válidas bajo toda asignación; sus clausuras universales están incluidas. La presentación es deductivamente equivalente a usar las bases cerradas y las clausuras universales de Ind con las reglas usuales derivadas: una instancia abierta se obtiene de su clausura por particularización, y sus prefijos se obtienen por la generalización que se justifica a continuación.

## 19.4. Efectividad de los axiomas y reglas admisibles de PA

### Lema 19.4.1 — Efectividad de los axiomas y reglas admisibles de PA {#tlog-lem-00072}

**Lema.** $A_{PA}$ es decidible-RM y se deciden las derivaciones concretas de PA. La generalización de teoremas de PA es admisible por expansión finita, sin añadir un tag Gen.

**Prueba efectiva.** Las ocho bases tienen códigos fijos. Para probar si una fórmula es Ind, se exige raíz de implicación y consecuente $\forall x_i A$. Se extraen $i,A$, se calculan las dos sustituciones de §19.3 y se reconstruye toda la plantilla, comparando literalmente. Se aceptan los tipos y se rechaza cualquier longitud/constructor incorrecto. Para prefijos se examinan la fórmula y sus sucesivas matrices de raíz universal, guardando el prefijo, como en §18.56; se prueba en cada etapa base o Ind. La cantidad de matrices es finita y las sustituciones son totales. Cada axioma de la definición será encontrado y cada éxito pertenece a ella. §18.60, con esta presentación decidible, da el verificador de secuencias originales PA.

**Generalización.** Se transforma línea a línea una prueba de A en prueba de $\forall x_i A$. Si la línea es axioma lógico o adicional, su prefijo universal es axioma por las dos definiciones. Si resulta por MP de B y $B\to C$, la hipótesis inductiva proporciona $\forall x_iB$ y $\forall x_i(B\to C)$; Q3 y dos MP dan $\forall x_iC$. No hay premisas externas en esta prueba. Esta es la construcción de §9.11 con la nueva clase de axiomas, y permite universalizar también fórmulas con parámetros. Deducción proposicional, igualdad y particularización conservan sus expansiones de CH9, pues se usan axiomas fijos y MP. $\square$

## 19.5. La estructura estándar externa de aritmética

### Definición 19.5.1 — La estructura estándar externa de aritmética {#tlog-def-00135}

$\mathbb N_A$ tiene dominio $\omega$ de la **ZF externa**, cero $\varnothing$, sucesor $n\mapsto n\cup\{n\}$, suma y producto definidos por recursión externa sobre $\omega$ y $<$ como orden de naturales externos. Las cláusulas recursivas de suma y producto son las ocho ecuaciones correspondientes de §19.3. Esta construcción es un conjunto en $M_{ext}$: infinitud y separación construyen $\omega$; recursión externa e inducción construyen las operaciones. No es una interpretación elegida de los naturales de un modelo de ZF objeto. El dominio es no vacío y las funciones tienen las aridades de $L_A$.

## 19.6. Modelo estándar y corrección externa de PA

### Metateorema 19.6.1 — Modelo estándar y corrección externa de PA {#tlog-mth-00102}

**Metateorema.** En la metateoría externa, $\mathbb N_A\models A_{PA}$ bajo toda asignación; por tanto todo teorema PA es verdadero en ella. En particular, PA no prueba dos numerales distintos iguales y es consistente externamente respecto de una contradicción fija. No se afirma que PA pruebe su propia corrección o consistencia.

**Prueba.** Cero no es sucesor, el sucesor es inyectivo y cada natural positivo tiene antecesor; se prueban por inducción externa a partir de los naturales de von Neumann. Las cuatro ecuaciones de suma/producto son sus cláusulas recursivas. La equivalencia de orden con $y=x+S(z)$ se demuestra por inducción en y: en 0 ambos lados son falsos; en $Sy$, un $x<Sy$ es x=y o x<y, que dan respectivamente z=0 o el sucesor del desplazamiento anterior; la recíproca sigue de que sumar un sucesor aumenta estrictamente. Para Ind, fijados los valores de parámetros, la separación externa forma $X=\{n\in\omega:\mathbb N_A\models A[n]\}$. Si0 pertenece a X y X es cerrado bajo sucesor, la inducción externa da $X=\omega$. La sustitución segura respeta satisfacción por CH8, así ésta es la verdad de la instancia. Prefijos universales preservan validez bajo toda asignación.

Finalmente, inducción sobre una derivación PA: cada axioma lógico es válido por CH10, cada adicional por lo recién probado y MP conserva satisfacción. Esto es la misma prueba del teorema de corrección, con los axiomas adicionales explícitos. Numerales distintos denotan naturales distintos. Una contradicción falsa en esta estructura no tiene prueba. Es una conclusión en ZF externa, obtenida por construcción, no una hipótesis de consistencia ni un modelo de $\mathrm{ZF}_{obj}$. $\square$

## 19.7. Definibilidad y representaciones débil y bilateral

### Definición 19.7.1 — Definibilidad y representaciones débil y bilateral {#tlog-def-00136}

Para $R\subseteq\omega^q$, una fórmula $\rho$ con variables libres sólo entre los q argumentos **define** R si $\mathbb N_A\models\rho[\bar n]$ equivale a $\bar n\in R$. La **representación débil en PA** significa
$$
\bar n\in R\iff\mathrm{PA}\vdash\rho(\overline{\bar n}).
$$
La **representación bilateral (o numeral por numeral)** exige: si $\bar n\in R$, PA prueba la instancia; si $\bar n\notin R$, PA prueba su negación. Bajo la corrección de §19.6, estas dos pruebas implican la definición y excluyen las pruebas equivocadas. No se reemplaza «no tiene prueba» por «su negación tiene prueba».

Para una función parcial f, una fórmula $\Phi_f(\bar x,y)$ es representante de su gráfica estándar si define exactamente los pares calculados. Se dirá **funcionalmente representada en cada entrada definida** si, siempre que $f(\bar n)=m$,
$$
\mathrm{PA}\vdash\forall y(\Phi_f(\overline{\bar n},y)\leftrightarrow y=\bar m).
$$
Se declararán por separado la funcionalidad interna $\mathrm{PA}\vdash\forall\bar x\forall y\forall z((\Phi_f(\bar x,y)\land\Phi_f(\bar x,z))\to y=z)$ y la totalidad interna $\mathrm{PA}\vdash\forall\bar x\exists y\Phi_f(\bar x,y)$. En entradas donde f no está definida, el primer requisito no pide una prueba negativa ni una prueba de divergencia. Un f total externo no incluye automáticamente el segundo requisito interno.

## 19.8. Consecuencias lógicas y límites de las representaciones

### Proposición 19.8.1 — Consecuencias lógicas y límites de las representaciones {#tlog-pro-00125}

**Proposición.** La representación bilateral en PA implica definición estándar y representación débil. Para funciones, la representación funcional en una entrada definida implica prueba de su valor, prueba de existencia en esa entrada y refutación de todo otro valor numeral. Ninguna de esas conclusiones cambia una instancia numeral por una cuantificación universal sobre todas las entradas.

**Prueba.** Si R es verdadero, hay prueba de $\rho$ y corrección da su verdad. Si es falso, hay prueba de $\neg\rho$; corrección impide una prueba de $\rho$ y da su falsedad. Éstas son ambas equivalencias. Para f, particularizamos la equivalencia en $y=\bar m$ y usamos reflexividad para obtener $\Phi_f(\bar n,\bar m)$ e introducción existencial para obtener $\exists y\Phi_f(\bar n,y)$. Para $k\ne m$, PA prueba que los dos numerales son distintos (también demostrado en §19.9), y la equivalencia implica $\neg\Phi_f(\bar n,\bar k)$. La generalización de una prueba con un **numeral fijo** no reemplaza ese término por una variable: sólo cuantifica variables libres. Por tanto una familia externa de pruebas de $\exists y\Phi_f(\bar n,y)$ no es por ese hecho una prueba única de $\forall x\exists y\Phi_f(x,y)$. $\square$

## 19.9. Aritmética elemental demostrable y segmentos numerales

### Lema 19.9.1 — Aritmética elemental demostrable y segmentos numerales {#tlog-lem-00073}

**Lema interno.** PA prueba las leyes de semianillo conmutativo de suma/producto, cancelación aditiva, orden lineal discreto, monotonía de suma/producto (estricta para factor positivo), y para cada n externo
$$
\forall z(z<\bar n\leftrightarrow(z=\bar0\lor\cdots\lor z=\overline{n-1})).
$$
Para n=0 el lado derecho es la fórmula falsa $0\ne0$. PA calcula términos cerrados y decide igualdades/orden de numerales.

**Prueba y rutas de inducción PA.** La identidad $0+x=x$ y la ecuación $Sx+y=S(x+y)$ se prueban por inducción en y usando $x+0=x$ y $x+Sy=S(x+y)$; asociatividad se prueba por inducción en el último sumando, y conmutatividad por inducción en el segundo argumento usando las dos identidades anteriores. La cancelación $a+c=b+c\to a=b$ usa inducción en c e inyectividad de S. Para producto, $0\cdot x=0$, $Sx\cdot y=x\cdot y+y$, y distributividad izquierda se prueban por inducción en y; con esas identidades se prueban conmutatividad, la otra distributividad y asociatividad, nuevamente en el argumento recursivo. Todos los parámetros permanecen libres durante cada Ind y se universalizan después mediante §19.4.

Escribamos $a\preceq b$ como $\exists d(b=a+d)$. PA prueba $a\preceq b\leftrightarrow(a<b\lor a=b)$: todo d es cero o sucesor por el tercer axioma, y se usa el axioma de <. Inducción en b prueba $a\preceq b\lor b<a$: caso0 usa cero/sucesor y $0+x=x$; en $Sb$, el caso $b<a$ escribe $a=b+Sd$, que se divide en d=0 (a=Sb) y d sucesor (Sb<a). La cancelación y que ningún sucesor es cero excluyen simultáneamente $a<b$ y $b\le a$. Transitividad sigue sumando desplazamientos. Esto da tricotomía, y los mismos desplazamientos dan monotonía aditiva. Distributividad da monotonía multiplicativa; para factor positivo, el producto de dos sucesores es sucesor por las ecuaciones, así conserva estrictamente el aumento.

La discreción $z<Sb\leftrightarrow(z<b\lor z=b)$ se obtiene cancelando el sucesor en los desplazamientos. Aplicándola finitísimas veces a b numeral se obtiene la fórmula de segmento con base $z\not<0$. Evaluar términos cerrados usa las ecuaciones recursivas hasta sus numerales; desigualdad de numerales usa inyectividad reiterada y $Sx\ne0$, y orden usa el segmento numeral. Cada afirmación es una derivación por estos axiomas/Ind, sin tomar prestada una prueba dentro de ZF objeto. $\square$

## 19.10. División con resto demostrable en PA

### Lema 19.10.1 — División con resto demostrable en PA {#tlog-lem-00074}

**Lema interno.** PA prueba que si $m>0$, todo a tiene exactamente un par $q,r$ con $a=q\cdot m+r$, $r<m$; además $q\le a$.

**Prueba.** Inducción PA en a para la existencia: en 0 elegimos q=r=0. Dado un par para a, si $Sr<m$, elegimos el mismo q y $Sr$ para $Sa$; de otro modo discreción y $r<m$ dan $Sr=m$, y elegimos $Sq,0$. Las ecuaciones de suma/producto comprueban $Sa=(Sq)m+0$ en el segundo caso. Para unicidad, si $q<q'$, entonces $qm+r<qm+m\le q'm\le q'm+r'$, contradiciendo igualdad de ambos con a; la rama $q'<q$ es simétrica. Luego q=q' y cancelación da r=r'. Puesto que $m\ge1$, monotonía da $q\le qm\le a$. La inducción usa el parámetro m bajo la guarda positiva, y se descarga/universaliza mediante §19.4. No se usa un símbolo de división ni se divide por 0. $\square$

## 19.11. Fórmulas acotadas y clase existencial Σ1

### Definición 19.11.1 — Fórmulas acotadas y clase existencial Σ1 {#tlog-def-00137}

En $L_A$, $\Delta_0$ es la clase generada por igualdades y < entre términos, los cinco conectivos, y cuantificadores acotados con cota que no contiene la variable cuantificada. Una fórmula $\Sigma_1$ aquí es una fórmula $\exists u_0\cdots\exists u_{k-1}\delta$ con $\delta\in\Delta_0$, k finito (se permite k=0). Hablamos de estas fórmulas efectivamente construidas y de equivalencias demostradas, no de una clasificación de toda fórmula por su semántica.

Las abreviaturas acotadas se expanden a la gramática primitiva; los conteos de cuantificadores acotados no afirman que desaparezcan del texto expandido. Mantener < como símbolo con su axioma definitorio evita llamar «acotada» a la fórmula expandida de ese axioma. Sólo las variables de argumento permanecen libres en los representantes finales.

## 19.12. Decisión externa y completitud numeral de Δ0

### Metateorema 19.12.1 — Decisión externa y completitud numeral de Δ0 {#tlog-mth-00103}

**Metateorema.** Para una fórmula $\Delta_0$ fija, su verdad en $\mathbb N_A$ bajo entradas naturales es decidible-RM. Cada instancia cerrada con numerales verdadera tiene prueba PA y cada falsa tiene prueba PA de su negación.

**Prueba.** Los términos se evalúan con operaciones totales RM de CH17; igualdad/< se deciden comparando naturales. Conectivos usan sus tablas finitas. En un cuantificador acotado se calcula el valor natural de la cota con la asignación actual y se recorre el segmento $0,\ldots,b-1$, consultando el procedimiento ya construido para la matriz con el valor del índice agregado al contexto. Una fórmula fija da finitísimas plantillas anidadas: el contador de cada bucle es finito y cada llamada a una subfórmula termina por inducción estructural. Una cota puede depender de variables de cuantificadores exteriores, pero no de su propia variable ligada.

Para la prueba PA se hace inducción externa sobre la fórmula y, en cada instancia, se calculan las cotas cerradas. §19.9 expande $z<\bar b$ en una disyunción finita de igualdades; sustitución de iguales y lógica de CH9 convierten $\exists z<\bar b A$ en la disyunción de sus b instancias y $\forall z<\bar b A$ en su conjunción. En b=0 se usan respectivamente falso y verdadero $0=0$. La hipótesis inductiva decide cada instancia y las tautologías H justifican la operación booleana, incluidos implicación y bicondicional. Todos los valores son numerales fijos en esta construcción, de modo que no se está afirmando completitud de todas las fórmulas PA. El mismo procedimiento genera una prueba finita del lado verdadero o de la negación del falso. Corrección asegura que no se generan pruebas equivocadas. $\square$

## 19.13. La relación aritmética auxiliar β

### Definición 19.13.1 — La relación aritmética auxiliar β {#tlog-def-00138}

Sea $m(i,b)=\bar1+(S i)\cdot b$. Definimos la fórmula, con variable q fresca,
$$
B(a,b,i,v):\equiv v<m(i,b)\land\exists q\le a\ (a=q\cdot m(i,b)+v).
$$
Es $\Delta_0$. Externamente $\beta(a,b,i)$ es el resto de dividir a por $1+(i+1)b$. Este módulo es positivo incluso si b=0. El par auxiliar $(a,b)$ no tiene una longitud implícita ni es una codificación inyectiva de secuencias; la longitud se dará aparte. No sustituimos la numeración S ni G de CH18 por β. β sólo permitirá expresar en una fórmula aritmética finita la lectura de una tabla de longitud variable.

## 19.14. Existencia y unicidad interna de la lectura β

### Lema 19.14.1 — Existencia y unicidad interna de la lectura β {#tlog-lem-00075}

**Lema.** PA prueba $\forall a\forall b\forall i\exists!v\ B(a,b,i,v)$. En los naturales externos B define precisamente el resto β, y para toda cuádrupla numeral se prueba B o su negación según corresponda.

**Prueba.** $1+(i+1)b>0$ por §19.9. §19.10 da el único resto y un cociente $q\le a$, así la cota añadida no elimina el testigo. La unicidad del resto da unicidad de v en B. La misma división en $\omega$ externo interpreta exactamente B. Las instancias numerales se deciden por §19.12, pues B es acotada. No se infiere que cualquier familia interna de valores tenga ya un código β; la prueba siguiente de codificación será **externa y finita**. $\square$

## 19.15. Bézout e inversos residuales en la metateoría externa

### Lema 19.15.1 — Bézout e inversos residuales en la metateoría externa {#tlog-lem-00076}

**Lema externo.** Para m,n positivos existe su máximo común divisor d y enteros u,v con $um+vn=d$. Si m,n son coprimos, hay $0\le h<n$ con $hm\equiv1\pmod n$ (para n=1 la congruencia es vacua y h=0). Los cálculos tienen algoritmos finitos por división repetida.

**Prueba.** Los enteros se representan externamente por diferencias de pares de naturales, con las reglas de anillo comprobadas en esos pares; no se agregan como dominio PA. Entre las combinaciones enteras positivas de m,n existe un mínimo d: m es una de ellas y $\omega$ está bien ordenado en ZF externa. Al dividir m por d, el resto r es también una combinación entera; si fuera positivo y menor que d contradice minimalidad. Luego d divide m; igual para n. Todo divisor común divide cada combinación y por tanto d, que es el máximo divisor común. Si d=1, la combinación es el certificado de Bézout. Reducimos u módulo n a h para obtener el inverso. El algoritmo de Euclides construye el mismo certificado: cada paso divide el par vigente y reemplaza el divisor por el resto menor; las identidades de resto actualizan las dos parejas de coeficientes, y la sucesión estrictamente decreciente de restos termina. El último resto positivo divide los dos argumentos y es combinación de ellos, por el invariante. La construcción sólo usa finitud, no elección ni un CRT supuesto. $\square$

## 19.16. Módulos coprimos y construcción explícita del CRT finito

### Lema 19.16.1 — Módulos coprimos y construcción explícita del CRT finito {#tlog-lem-00077}

**Lema externo.** Si una lista $a_0,\ldots,a_{L-1}$ se fija y $b=L!\,(1+\max(\{0\}\cup\{a_i:i<L\}))$, los módulos $m_i=1+(i+1)b$ son coprimos dos a dos y superan todos los valores a_i. Para módulos positivos coprimos y residuos menores que ellos se construye un a con todos esos residuos, por un procedimiento finito.

**Coprimalidad.** b es positivo y mayor que cada a_i. Para i<j<L, un divisor común d de $m_i,m_j$ divide $(j-i)b$. Como d divide $1+(i+1)b$, ningún divisor común de d,b puede superar1. Bézout para d,b permite cancelar b en la divisibilidad y da $d\mid(j-i)$. El número $j-i$ divide L!, por su definición como producto $1\cdots L$; luego d divide b. Pero d coprimo con b implica d=1. Los módulos exceden b.

**Construcción.** Inicializamos A=0,M=1. Suponiendo $0\le A<M$ y los residuos anteriores correctos, el producto M de los módulos anteriores es coprimo con el siguiente m. Esto se prueba multiplicando los certificados Bézout de cada factor con m: $(uM+vm)(u'n+v'm)=uu'Mn+m(\text{coeficiente entero})$. §19.15 da un inverso $h$ de M módulo m. Si el nuevo residuo es r, ponemos
$$
d=(r+m-(A\bmod m))\bmod m,\quad q=(hd)\bmod m,\quad A'=A+Mq,\quad M'=Mm.
$$
La diferencia natural es definida porque $A\bmod m<m$. A' mantiene los residuos anteriores ya que M es múltiplo de cada módulo anterior; en m su nuevo residuo es r por la identidad $hM\equiv1$. Puesto que q<m, se tiene $A'<Mm$. Tras L pasos se obtiene el testigo. La lista vacía entrega A=0,M=1. Euclides, división y el recorrido de la lista terminan; no se invoca simultáneamente una selección infinita de residuos. Este CRT se prueba en ZF externa, no como totalidad uniforme interna de PA. $\square$

## 19.17. Codificación β de toda secuencia finita externa

### Metateorema 19.17.1 — Codificación β de toda secuencia finita externa {#tlog-mth-00104}

**Metateorema.** Para toda secuencia externa finita $\bar a$ de longitud L, existen a,b naturales tales que $\beta(a,b,i)=a_i$ para i<L. Se construyen a,b efectivamente, y PA prueba cada una de las L igualdades B correspondientes con numerales.

**Prueba.** Elegimos b como en §19.16 y construimos a por el CRT allí demostrado, con residuos a_i menores que sus módulos. La unicidad de restos identifica β. Para L=0, a=0,b=1 es un testigo sin condiciones. Los algoritmos de factorial, máximo de lista, módulos, inversos y productos usan operaciones numéricas y bucles finitos RM fijados de CH17/18, así proporcionan un codificador efectivo externo. Cada lectura correcta es una fórmula B cerrada verdadera; §19.14/12 produce su prueba PA. Los pares no son únicos, no sustituyen S, y no se declara aquí $\mathrm{PA}\vdash$ que toda tabla de longitud arbitraria tenga codificación β. Las trazas concretas necesitarán sólo estos testigos externos y sus numerales. $\square$

## 19.18. Fórmula aritmética de transición de un programa fijo

### Definición 19.18.1 — Fórmula aritmética de transición de un programa fijo {#tlog-def-00139}

Fijado un programa válido $P=(r,p)$, $n=|p|$, la configuración se describe por $\ell,v_0,\ldots,v_{r-1}$, no por un nuevo código S. Sea $\mathsf{St}_P(\ell,\bar v,\ell',\bar w)$ la siguiente **disyunción finita**, con una rama por etiqueta h<n y con los numerales r,n,h,i,j,k insertados en el texto:

| Instrucción p(h) | Rama, además de $\ell=\bar h$ |
|---|---|
| HALT | $\ell'=\bar h$ y $w_s=v_s$ para todo s<r |
| INC(i,j) | $\ell'=\bar j$, $w_i=S v_i$, demás $w_s=v_s$ |
| DECJZ(i,j,k),cero | $v_i=0$, $\ell'=\bar j$, todos $w_s=v_s$ |
| DECJZ(i,j,k),positivo | $v_i=S w_i$, $\ell'=\bar k$, demás $w_s=v_s$ |

Las conjunciones sobre s<r son **finitas en el texto**, no un cuantificador sobre registros variables. La fórmula es cuantificacionalmente libre y coincide con las cuatro ramas de §17.7. Si no hay HALT, su disyunción de etiquetas de parada será $0\ne0$. $\mathsf H_P(\ell)$ abrevia la disyunción finita $\ell=\bar h$ para las etiquetas HALT. El tamaño del texto depende de P; no se afirma que un número variable de registros se inserte como una lista de variables durante la evaluación de una misma fórmula.

## 19.19. Exactitud y determinismo demostrable del paso aritmético

### Lema 19.19.1 — Exactitud y determinismo demostrable del paso aritmético {#tlog-lem-00078}

**Lema.** St_P define el paso externo de P. PA prueba que, si $\ell<\bar n$, existe una única configuración sucesora con etiqueta $<\bar n$. También prueba que una configuración HALT sólo sucede a sí misma.

**Prueba.** §19.9 permite dividir la etiqueta acotada en los n casos numerales. En cada caso HALT e INC designan exactamente los valores escritos. Para DECJZ, cero/sucesor es exhaustivo y excluyente: todo positivo tiene antecesor por el tercer axioma, éste es único por inyectividad, y cero no es sucesor. Cada otra coordenada se conserva. Los destinos son numerales menores que n por la validez de P; para HALT es la misma etiqueta. La disyunción se combina mediante las reglas proposicionales de CH9. El mismo examen en la estructura estándar identifica St con $E_P$. Los registros tienen valores naturales sin cota prefijada; el determinismo no necesita una cota de tiempo ni codificar el programa en el lenguaje objeto. $\square$

## 19.20. Tablas β de ejecución y fórmula de gráfica Σ1

### Definición 19.20.1 — Tablas β de ejecución y fórmula de gráfica Σ1 {#tlog-def-00140}

Fijamos además aridad q<=r y argumentos $\bar x$. Sea $w=r+1$, $L=(t+1)w$ y $M=1+Lb$. La fila k codifica la etiqueta en índice kw y el registro s en kw+s+1. Para abreviar, $\mathsf{Row}(a,b,k,\ell,\bar v)$ es la conjunción de $B(a,b,kw,\ell)$ y $B(a,b,kw+s+1,v_s)$ para los r valores. Cada Row es Δ0, con las constantes w,s escritas como numerales.

La matriz $\mathsf{Tr}_{P,q}(\bar x,y,t,a,b)$ dice:
1. existe una fila inicial con todas sus coordenadas $<M$, etiqueta0, registros $x_0,\ldots,x_{q-1}$ y r-q ceros;
2. para cada k<=t existe una fila k con coordenadas $<M$ y etiqueta $<\bar n$;
3. para cada k<t existen las dos filas k,k+1 con todas sus coordenadas $<M$ y St_P entre ellas;
4. existe la fila final t con coordenadas $<M$, $\mathsf H_P(\ell)$ y $v_0=y$.

Todas las existencias de coordenadas aquí están **acotadas por M**; cada registro se escribe mediante su propio cuantificador y la conjunción Row. Los cuantificadores k se acotan por t o $S t$. No se introduce un cuantificador sobre secuencias como primitivo. Para q=0 la fila inicial tiene r ceros. $M$ supera todos los módulos de lectura usados en índices $<L$ o los iguala cuando b=0; por ello todo resto válido está $<M$.

Definimos
$$
\Phi_{P,q}(\bar x,y):=\exists t\exists a\exists b\ \mathsf{Tr}_{P,q}(\bar x,y,t,a,b).
$$
Es una fórmula Σ1. El uso de β es auxiliar: los números x,y pueden ser los códigos S/G aprobados de CH18, pero la tabla de estados se lee mediante B. Nombres auxiliares y parámetros se escogen frescos antes de expandir cada abreviatura.

## 19.21. Exactitud estándar de las tablas de ejecución

### Lema 19.21.1 — Exactitud estándar de las tablas de ejecución {#tlog-lem-00079}

**Lema.** $\mathbb N_A\models\Phi_{P,q}[\bar n,m]$ si y sólo si el programa P en entrada $\bar n$ para con salida m.

**Prueba hacia parada.** Unos testigos t,a,b proporcionan por unicidad β una única fila por k<=t. La inicialización da el estado inicial, y St da el paso exacto. Inducción externa en k identifica las filas con la órbita de CH17. La fila final está en HALT y su registro 0 es m.

**Prueba desde parada.** Fijamos el tiempo t y la lista concreta de estados de la órbita hasta t. Aplanamos cada configuración en etiqueta seguida de r registros, conservando el orden de filas: es una lista de longitud $(t+1)(r+1)$. §19.17 proporciona a,b para la lista. Sus restos están bajo M por la cota de §19.20; cada fila, transición y condición inicial/final se cumple. Esto da los testigos de la fórmula. El tiempo 0, el programa sin etiquetas HALT y la parada absorbente están incluidos: el primero tiene una fila, el segundo no satisface el último requisito y el tercero admite más de un tiempo con igual salida. $\square$

## 19.22. Funcionalidad de las gráficas de ejecución dentro de PA

### Lema 19.22.1 — Funcionalidad de las gráficas de ejecución dentro de PA {#tlog-lem-00080}

**Lema interno.** PA prueba que $\Phi_{P,q}$ es funcional en y, aunque no se afirme totalidad interna.

**Prueba.** Supongamos dos matrices Tr con la misma entrada y testigos $(t,a,b)$ y $(u,c,d)$. La expresión «fila k de la primera tabla = fila h de la segunda» abrevia una fórmula concreta: para cada columna s=0,...,r se exige $\exists z<M_t+M_u\,(B(a,b,kw+\bar s,z)\land B(c,d,hw+\bar s,z))$, y se conjugan esas r+1 cláusulas finitas. Aquí $M_t=1+(t+1)wb$ y $M_u=1+(u+1)wd$. Bajo las hipótesis de filas válidas, esta fórmula equivale a igualdad de todas sus coordenadas por unicidad de B; la cota suma admite cualquier valor común. Para comparar dos filas de la misma tabla se usan sus mismos parámetros en ambas posiciones y la cota doble correspondiente. Todas estas abreviaturas se expanden antes de tomar una instancia Ind.

Por orden lineal se divide en t<=u o u<=t; tratemos t<=u. Inducción PA en k, con los seis testigos y la entrada como parámetros, prueba: para k<=t las dos filas k son iguales. El caso0 usa la inicialización y la unicidad de B. En el paso, si $k+1<=t$, las matrices suministran filas k,k+1 en ambas tablas; la hipótesis y el determinismo de St dan igualdad de sucesores. Si la guarda $k+1<=t$ falla, la implicación inductiva es vacua. Para cada lectura, existencia/identidad de coordenadas se obtiene de la matriz y §19.14; los existenciales locales se eliminan mediante testigos frescos, sin una función de elección.

La fila t en la primera tabla es HALT, por tanto también la fila t en la segunda. Una segunda inducción PA en k demuestra, bajo $t<=k<=u$, que la fila k de la segunda tabla coincide con su fila t: base k<t vacua y k=t por identidad; en el paso k>=t, la transición desde una fila HALT es absorbente por §19.19, y si $k+1>u$ la guarda es vacua. Formalmente se usa la fórmula $\forall j(t<=j<=k\land j<=u\to\text{fila j=fila t})$, cuya base incluye t=0 y cuyo paso agrega sólo j=k+1 por discreción. Si la nueva posición coincide con t se usa identidad, y si supera t se tiene t<=k y se aplica absorción al paso desde k. Así el registro 0 en las filas finales t,u es igual. En u<=t se intercambian las tablas. Se descargan hipótesis y se generalizan parámetros para obtener
$$
\mathrm{PA}\vdash\forall\bar x\forall y\forall z((\Phi_{P,q}(\bar x,y)\land\Phi_{P,q}(\bar x,z))\to y=z).
$$
Las dos inducciones son instancias PA sobre fórmulas con parámetros de códigos, no inducciones externas sobre un tiempo estándar supuesto. La existencia interna de una tabla arbitraria no se utilizó: se comparan las tablas **bajo sus hipótesis Tr**. $\square$

## 19.23. Representación Σ1 de funciones parcialmente computables RM

### Metateorema 19.23.1 — Representación Σ1 de funciones parcialmente computables RM {#tlog-mth-00105}

**Metateorema.** Toda función parcial computable-RM de aridad finita tiene una fórmula Σ1 que define su gráfica estándar, es internamente funcional en PA y la representa funcionalmente en cada entrada definida. La fórmula se construye efectivamente a partir del programa fijo y la aridad.

**Prueba.** Fijamos un programa P que calcula f y tomamos $\Phi_{P,q}$. §19.21 da la equivalencia estándar y §19.22 da la funcionalidad PA. Si f($\bar n$)=m, la traza concreta y §19.17 dan testigos naturales t,a,b de Tr; la matriz con todos los argumentos numerales es Δ0 verdadera. §19.12 da su prueba PA, y tres introducciones existenciales dan $\Phi_{P,q}(\overline{\bar n},\bar m)$. Por funcionalidad se deduce $\forall y(\Phi_{P,q}(\overline{\bar n},y)\to y=\bar m)$; igualdad y esa instancia dan la implicación inversa. Se obtiene la equivalencia requerida. Si f diverge, la fórmula no tiene un valor en la estructura estándar, pero no se ofrece una prueba PA de esa divergencia.

El compilador de fórmulas recorre la lista finita de instrucciones de P y construye las ramas de St, las r coordenadas de Row y el texto fijo de Tr. Las guardas de programa y aridad se deciden por CH18. La selección de nombres frescos y construcción de árboles G son efectivas; los metanombres no cuentan como nuevos símbolos objeto. La finitud de la fórmula está asegurada antes de usarla. Para f total, hay una prueba de valor/existencia para cada entrada numeral, pero este teorema no proporciona necesariamente $\mathrm{PA}\vdash\forall\bar x\exists y\Phi_f(\bar x,y)$. $\square$

## 19.24. Representación bilateral de relaciones decidibles RM

### Metateorema 19.24.1 — Representación bilateral de relaciones decidibles RM {#tlog-mth-00106}

**Metateorema.** Toda relación decidible-RM $R\subseteq\omega^q$ tiene una representación bilateral PA mediante una fórmula Σ1 que la define en $\mathbb N_A$.

**Prueba.** Su decidor total calcula la característica $\chi_R\in\{0,1\}$. Sea $\Phi_\chi$ el representante funcional de §19.23 y $\rho_R(\bar x)=\Phi_\chi(\bar x,\bar1)$. En una entrada de R se prueba la salida 1 y por tanto $\rho_R$. En una entrada fuera de R se prueba $\forall y(\Phi_\chi(\bar n,y)\leftrightarrow y=\bar0)$; particularizar en 1 y $1\ne0$ da $\neg\rho_R$. Su semántica es exactamente la gráfica del decidor. No es necesario mostrar que PA prueba la totalidad uniforme del decidor. El representante positivo es Σ1; no se reclama que la negación textual también esté en esa forma. $\square$

## 19.25. Representación débil de relaciones semidecidibles RM

### Metateorema 19.25.1 — Representación débil de relaciones semidecidibles RM {#tlog-mth-00107}

**Metateorema.** Toda relación semidecidible-RM R tiene una fórmula Σ1 que la define en los naturales y la representa débilmente en PA.

**Prueba.** Para un semidecidor P por dominio de parada, ponemos $\rho_R(\bar x)=\exists y\Phi_{P,q}(\bar x,y)$. Los existenciales se agrupan antes de la matriz Δ0, conservando nombres frescos. La exactitud de ejecución da definición estándar. Si $\bar n\in R$, hay una salida natural y la prueba numeral de §19.23 da $\rho_R(\bar n)$. Si PA la prueba, corrección de §19.6 da una parada estándar, luego $\bar n\in R$. La inexistencia de parada no proporciona una prueba de negación: por eso este resultado es débil y no bilateral. Que el semidecidor devuelva0 al parar sigue siendo aceptación por su dominio, no rechazo. $\square$

## 19.26. Caracterizaciones de la semidecidibilidad por Σ1 y pruebas

### Metateorema 19.26.1 — Caracterizaciones de la semidecidibilidad por Σ1 y pruebas {#tlog-mth-00108}

**Metateorema.** Para relaciones de aridad finita, son equivalentes: semidecidibilidad RM; definición estándar por alguna Σ1; representación débil en PA por alguna fórmula aritmética.

**Prueba.** La primera implica las otras por §19.25. Si $\rho=\exists\bar u\delta$ define R, recorremos naturales d, decodificamos d como lista S de exactamente $|\bar u|$ testigos y, para listas válidas, decidimos $\delta(\bar n,\bar u)$ por §19.12. Toda tupla finita tiene un código y cada test termina; se para sólo en verdad. Para prefijo vacío se ejecuta directamente el decidor δ, parando en verdadero y divergiendo en falso. No se requiere una biyección entre códigos válidos y todos los naturales.

Si una fórmula fija $\rho$ representa débilmente R, calculamos el código de su instancia numeral usando las sustituciones efectivas de CH18. Se recorren los posibles códigos de derivación PA y el decidor de §19.4 busca una prueba de esa instancia. Por la definición débil, se para exactamente en R. La fórmula puede tener complejidad arbitraria; no se afirma que toda fórmula de PA sea Σ1, sino que R admite algún representante Σ1 mediante el primer sentido. Estos algoritmos no usan corrección adicional en la última implicación: la equivalencia de pruebas está incluida en la hipótesis débil. $\square$

## 19.27. Caracterización bilateral y computabilidad recuperada

### Metateorema 19.27.1 — Caracterización bilateral y computabilidad recuperada {#tlog-mth-00109}

**Metateorema.** R es decidible-RM si y sólo si es representable bilateralmente en PA. Una función externa total es computable-RM si y sólo si admite un representante funcional numeral por numeral en PA; para la inversa basta la cláusula de equivalencia probada en cada valor correcto, con variables libres sólo de entrada/salida.

**Prueba para R.** El sentido directo es §19.24. En el inverso, para entrada $\bar n$, buscamos intercaladamente pruebas PA de la instancia $\rho(\bar n)$ y de su negación, recorriendo d=0,1,... con el decidor de pruebas en ambas. Alguna existe por bilateralidad, y corrección PA excluye el lado equivocado. Devolvemos1 o0 según el primer éxito, con terminación total. Es también una aplicación de la doble semidecisión de CH17.

**Prueba para f.** El sentido directo es §19.23. Para la inversa recorremos códigos S de pares $(m,d)$ y verificamos si d prueba $\forall y(\Phi(\bar n,y)\leftrightarrow y=\bar m)$, construyendo el código de esa sentencia mediante sustitución efectiva. Existe un par correcto porque f es total y representada; todo candidato se examina totalmente. Si un m distinto del valor real fuera aceptado, las equivalencias probadas para ambos valores darían igualdad de los dos numerales en PA, contra §19.6/9. Por ello la búsqueda devuelve el valor correcto. No se decide de un código arbitrario si una fórmula representa una función total: se trabaja bajo la hipótesis explícita. Tampoco se deduce totalidad **interna** desde el algoritmo externo recuperado. $\square$

## 19.28. Funciones de numeral, sustitución numeral y autoinstanciación

### Definición 19.28.1 — Funciones de numeral, sustitución numeral y autoinstanciación {#tlog-def-00141}

$\mathsf{Num}(n)=G(\bar n)$ para la presentación aritmética fijada. $\mathsf{Sub}(c,i,n)$ devuelve el código de $A[\bar n/x_i]_{lit}$ si c codifica una fórmula aritmética A, y0 si no; no se requiere que $x_i$ ocurra libre. Finalmente $\mathsf{D}(c)=\mathsf{Sub}(c,0,c)$. Es una función de naturales: introduce el **numeral del código** c en la variable distinguida, no el texto de una fórmula como un término. D(0)=0 porque0 no es código de fórmula. Estos espacios conservan los tags G de CH18.

## 19.29. Representación de la infraestructura sintáctica aprobada

### Metateorema 19.29.1 — Representación de la infraestructura sintáctica aprobada {#tlog-mth-00110}

**Metateorema.** Num, Sub y D son funciones totales computables-RM y tienen representantes Σ1 funcionales en PA. Lo mismo vale para las funciones totalizadas de secuencia, soporte, frescura, sustitución y ejecución acotada ya aprobadas; sus predicados decidibles tienen representantes bilaterales PA. Esto incluye validez de códigos, Ax lógico, RawProof, Step y Trace, en los dominios/presentaciones especificados.

**Prueba.** Num inicia el código del término nulario0 y envuelve n veces con el constructor de S mediante un contador decreciente. Sub valida c, calcula Num y aplica la sustitución literal segura: el numeral es cerrado, así no hay captura. El caso inválido devuelve0 y el válido, incluso vacuo, conserva su código correcto. D es composición total. Cada otra operación dispone de programa fijo total o decidor de CH17/18, con fallos/guardas ya declarados. Se aplica §§19.23/24 a **cada uno de esos programas**, no a una recursión conjuntista sin testigo operacional. Para signaturas distintas de $L_A$, el programa de dominio/aridad ha de estar fijado como dato y las entradas/output son números externos; sus representantes siguen siendo fórmulas de $L_A$.

La conclusión para Sub es, para cada triple numeral correcto, una equivalencia PA de su salida con el numeral de su valor. No es aún el lema diagonal, ni una identidad que PA haya demostrado uniformemente entre todos los códigos de sintaxis. Estas distinciones son el contrato de entrada de CH20. $\square$

## 19.30. Predicados externos de prueba y sus fórmulas aritméticas

### Definición 19.30.1 — Predicados externos de prueba y sus fórmulas aritméticas {#tlog-def-00142}

$\operatorname{Prf}^{ext}_{PA}(d,c)$ dice que d es código S de una secuencia original no vacía de fórmulas, desde ninguna premisa adicional, con conclusión de código c, usando axiomas lógicos o $A_{PA}$ y MP. Es la relación decidible de §19.4. Sean $\chi_{Prf}$ su decidor total y $\Phi_{\chi_{Prf}}$ el representante construido de su programa. Fijamos
$$
\mathsf{Prf}_{PA}(d,c):=\Phi_{\chi_{Prf}}(d,c,\bar1),\qquad
\mathsf{Prov}_{PA}(c):=\exists d\ \mathsf{Prf}_{PA}(d,c).
$$
La primera es una **fórmula** de $L_A$ distinta de la relación externa; la segunda es una fórmula de existencia, no un decidor. No hay un símbolo primitivo «PA demuestra» en el lenguaje. Los nombres auxiliares se eligen frescos y ambos representantes tienen sólo los argumentos indicados libres. La elección depende del programa de verificación concreto: diferentes representantes no se identifican automáticamente por una equivalencia PA uniforme.

## 19.31. Exactitud y representación del predicado de demostrabilidad

### Metateorema 19.31.1 — Exactitud y representación del predicado de demostrabilidad {#tlog-mth-00111}

**Metateorema.** Prf_PA representa bilateralmente la relación externa de prueba y la define en la estructura estándar. Prov_PA es Σ1, define exactamente los códigos de teoremas PA y representa débilmente ese conjunto. Para cada teorema concreto A, $\mathrm{PA}\vdash\mathsf{Prov}_{PA}(\overline{G(A)})$.

**Prueba.** §19.24 aplicado al verificador prueba ambas afirmaciones de Prf. La gráfica estándar de su programa acepta exactamente las pruebas originales, incluida la condición de última fórmula y sólo referencias precedentes. Agrupando los existenciales de Prf tras d se obtiene una matriz Δ0, así Prov es Σ1. Si A es teorema tiene un código de prueba concreto d; la representación positiva de Prf para $(d,G(A))$ y la introducción existencial dan Prov de su código. Recíprocamente si la estructura estándar satisface Prov existe un d estándar que acredita la derivación, y si PA prueba esa instancia, corrección estándar da el mismo testigo externo. Por tanto se obtienen definición y representación débil. Un natural que no sea código de fórmula o no sea teorema no satisface Prov en $\mathbb N_A$, pero no se afirma que PA pruebe su negación.

La implicación metateórica «si PA prueba A, PA prueba Prov de su código» se ha acreditado **caso por caso**. No se han demostrado condiciones internas de derivabilidad para el representante elegido, reflexión $\mathsf{Prov}(\ulcorner A\urcorner)\to A$, completitud/decidibilidad de PA, ni un predicado de verdad. No deben usarse esas propiedades en CH20 sin pruebas adicionales. $\square$

## 19.32. Extensiones aritméticas y teorías con axiomas efectivos

### Proposición 19.32.1 — Extensiones aritméticas y teorías con axiomas efectivos {#tlog-pro-00126}

**Proposición.** Las pruebas positivas y equivalencias funcionales PA de este capítulo persisten en toda extensión deductiva T de PA. Si T es consistente y sus axiomas adicionales son semidecidibles bajo una presentación fija, se pueden verificar pruebas con certificados y semidecidir teoremas T; un representante aritmético de sus certificados de prueba se obtiene en PA. La exactitud estándar del conjunto de teoremas y una prueba de corrección de T son cuestiones distintas.

**Prueba.** Inclusión deductiva conserva cada prueba PA, incluidas las negativas de representación bilateral y la funcionalidad. El verificador certificado T se construye por §18.61, usando trazas de parada del semidecidor de axiomas; es total aunque no lo sea el reconocimiento de secuencias desnudas. Su decidor se representa bilateralmente en PA por §19.24 y la fórmula existencial de certificados define en $\mathbb N_A$ los teoremas T por el borrado/certificación demostrado. Así PA representa débilmente ese conjunto semidecidible por §19.25; no se afirma que T sea correcto en $\mathbb N_A$ ni que una prueba T de su fórmula de demostrabilidad sea necesariamente verdadera. La consistencia de T impide colapsar representaciones contrarias, pero no sustituye una prueba de corrección estándar. Para $\mathrm{ZF}_{obj}$ no se ha fijado aquí una interpretación de $L_A$ ni su presentación efectiva de axiomas, por lo que ninguna transferencia se aplica automáticamente. $\square$

## 19.33. Cierre de representabilidad y contrato para el lema diagonal

### Corolario 19.33.1 — Cierre de representabilidad y contrato para el lema diagonal {#tlog-cor-00030}

**Corolario.** CH19 entrega una teoría aritmética objeto efectiva con modelo estándar externo construido, lectura β aritmética, fórmulas Σ1 de ejecuciones RM, representación funcional de funciones parciales en entradas definidas, representación bilateral de relaciones decidibles y caracterizaciones de la semidecidibilidad. Quedan representadas las funciones sintácticas Num/Sub/D y los predicados externos de prueba, con demostrabilidad como proyección existencial.

**Prueba.** Cada interfaz está demostrada en §§19.4–32 con sus hipótesis: la codificación finita β externa suministra los testigos numerales; las inducciones PA comparan trazas bajo sus hipótesis; la verdad de fórmulas Δ0 concretas suministra pruebas y la corrección estándar sólo se usa donde está declarada. No se sustituye S por β ni se introduce una máquina de Turing para demostrar representación. $\square$

**Contrato CH20.** Se puede utilizar la función total D y su representación funcional numeral por numeral para construir una sentencia fija para una fórmula dada, con renombrado/frescura explícitos. Todavía no se ha construido tal sentencia ni probado un lema diagonal. Tampoco se han probado incompletitud, indefinibilidad de verdad, condiciones internas de derivabilidad, segunda incompletitud o totalidad uniforme en PA de todos los programas totales externos. La teoría de base para las próximas conclusiones será PA o una extensión con hipótesis expresas; usar Q como base más débil o trasladar todo a ZF objeto requiere resultados adicionales. Son fronteras externas al alcance aprobado de CH19, no pruebas omitidas de representación.

**CH19 CLOSED.** La Parte IV sigue OPEN porque falta CH20. No se presume consistencia o existencia de modelos de ZF objeto. La consistencia externa de PA fue una conclusión de §19.6 dentro de la metateoría declarada, no un nuevo axioma de la obra.

## 19.34. Ejemplos y estado de cierre

El programa de un registro INC(0,1),HALT calcula x+1. Su fórmula St tiene las ramas $\ell=0,\ell'=1,w_0=Sv_0$ y $\ell=1,\ell'=1,w_0=v_0$. En entrada 2 y tiempo 1, la tabla aplanada es [0,2,1,3]. Un par β construido con sus cuatro residuos acredita esa tabla; la matriz cerrada verdadera tiene prueba PA y la funcionalidad da $\forall y(\Phi_P(\bar2,y)\leftrightarrow y=\bar3)$. La traza prolongada a tiempo 2 termina con la misma salida. No se calcula aquí un tiempo de ejecución de una prueba PA ni una cota de eficiencia de β.

Un decidor que devuelve0 en una entrada proporciona una **prueba de negación** para su representante con salida 1; un semidecidor que devuelve0 al parar proporciona una **prueba positiva** de pertenencia por su dominio de parada. La diferencia procede de la definición operacional, no del símbolo0 aislado.

| Afirmación | Alcance aprobado |
|---|---|
| Función RM parcial | gráfica Σ1 exacta, funcionalidad PA y prueba de valor en entradas definidas |
| Relación decidible | representación bilateral numeral por numeral |
| Relación semidecidible | definición Σ1 y representación débil |
| Programa externo total | representación para cada entrada; no totalidad uniforme PA automática |
| Prueba PA concreta | verificación decidible y representación bilateral del verificador |
| Existencia de alguna prueba | fórmula Σ1/semidecisión; no decidor de demostrabilidad |
| Autoinstanciación D | función total representada; lema diagonal todavía pendiente |

El capítulo cierra **33/33 resultados propios** con **136 dependencias directas nuevas**. La Parte IV permanece abierta. Próximo capítulo: **CH20 — Diagonalización y lema diagonal**.

```text
LOCAL  CH19 ████████████████████ 33/33 resultados (100 %)
GLOBAL TLOG ████████████████████░░░░ 20/24 capítulos (83,33 %)
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 18](capitulo-18.md) · [Capítulo 20 →](capitulo-20.md)


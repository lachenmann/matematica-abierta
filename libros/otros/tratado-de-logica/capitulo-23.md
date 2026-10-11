---
title: Capítulo 23 — Indecidibilidad, límites y frontera con GAS
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
content-id: MA-BCH-0225
content-type: book-chapter
source-id: TLOG-CH23-0001
prerequisites:
- MA-BCH-0211
- MA-BCH-0212
- MA-BCH-0213
- MA-BCH-0219
- MA-BCH-0220
- MA-BCH-0221
- MA-BCH-0222
- MA-BCH-0223
- MA-BCH-0224
related:
- MA-BOK-0014
source-sha256: 33409227d2309c2827199f3209e9f8d2bfb1f0eb290e54d35fb4b10689097bf4
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 22](capitulo-22.md) · 

## 23.0. Qué significa que no exista un método uniforme

Ya tenemos pruebas formales codificables, máquinas universales RM, aritmetización, diagonalización e incompletitud. El último capítulo conecta esas construcciones con preguntas algorítmicas precisas: parar, demostrar, tener un modelo y ser verdadero. Cada límite se prueba para una familia y conserva su nivel y sus hipótesis.

Comenzaremos con parada y reducciones. Después mostraremos que la consistencia basta para excluir un decidor de teoremas de cualquier extensión PA, incluso sin presentación efectiva; la presentación se requiere para la semidecisión. Una base aritmética finita permitirá transferir parada a validez lógica sin importarQ ni finita axiomatización PA. Finalmente separaremos verdad Σ1 y verdad completa, demostraremosTarski y prepararemos la salida diofántica elemental haciaGAS.

La redacción y las pruebas son autorales humanas. Como contraste primario limitado se consultó [Avigad, §§4.9 y apertura del capítulo5](https://www.andrew.cmu.edu/user/avigad/Teaching/candi_notes.pdf), versión9enero2007; y [Matiyasevich, §1.1 del texto del autor](https://logic.pdmi.ras.ru/~yumat/H10Pbook/par_1_1.htm), para la declaración de dominios y dirección de reducciones. Ninguna fuente sustituye nuestros proveedoresS/G/RM; no se importa una prueba MRDP o equivalencia operacional externa.

## 23.1. El cierre lógico y sus tres niveles

### Convención 23.1.1 — El cierre lógico y sus tres niveles {#tlog-cnv-00034}

Seguimos en ZF clásica externa sin AC/BPI. PA y sus extensiones son teorías objeto; RM es el sistema operacional externo aprobado; ZF objeto conserva su identidad. No se presume consistencia ni modelo de ZF objeto. El capítulo completa las consecuencias lógico-formales necesarias del tratado, sin absorber la monografía GAS.

Separamos tres límites: no existencia de un decidor RM para una familia de entradas; ausencia de una prueba de una sentencia en una teoría fijada; y no definibilidad aritmética de un conjunto de códigos en la estructura estándar. Ninguno es una descripción de dificultad psicológica o de tiempo de cálculo. Las hipótesis de consistencia y corrección Σ1 se indicarán por separado.

La construcción universal de CH18 permite ahora diagonalizar programas **codificados**: ese recurso no se retropropaga a CH17. MRDP/Jones, la equivalencia RM–Turing y las interpretaciones intertratados no se incorporan por el cierre del índice. La formulación diofántica elemental al final sólo prepara un contrato de entrada para GAS.

## 23.2. Reducción computable entre problemas codificados

### Definición 23.2.1 — Reducción computable entre problemas codificados {#tlog-def-00160}

Para A,B⊆ω escribimos $A\le_m^{RM}B$ si existe una función **total** computable-RM f:ω→ω tal que n∈A⇔f(n)∈B. f es una reducción de muchos a uno. La función se fija una vez para todas las entradas; no puede consultar el problema que pretende reducir.

Un problema de tuplas se convierte en conjunto numérico mediante S, con reconocimiento de longitud/aridades. Fuera de los códigos válidos la respuesta de pertenencia será falsa, salvo declaración explícita diferente. Los complementos sin subíndice son relativos a ω; cuando sólo se discuten entradas válidas se declara esa restricción y se usa la guarda decidible para pasar al problema total.

Dec-RM significa existencia de un programa total que entrega1 en miembros y0 en no miembros. Semi-RM significa parada exactamente en miembros, con salida irrelevante. Un algoritmo que a veces devuelve «desconocido» o diverge no es un decidor de esta definición.

## 23.3. Transferencia por reducciones y clausuras

### Lema 23.3.1 — Transferencia por reducciones y clausuras {#tlog-lem-00104}

**Lema.** Si A≤_m B y B es decidible, A es decidible. Si B es semidecidible, A es semidecidible. Si el complemento de B es semidecidible, también el complemento de A lo es. Las reducciones son reflexivas y transitivas.

**Prueba.** Se calcula f(n) y se ejecuta el procedimiento correspondiente de B. Totalidad de f asegura que no se pierden entradas antes de la prueba de pertenencia. La misma f satisface n∉A⇔f(n)∉B. Identidad y composición de programas totales dan reflexividad y transitividad. Así, para probar indecidibilidad de B desde la de A, la dirección necesaria es **A≤_m B**. Obtener B≤_m A no daría esa conclusión. $\square$

## 23.4. Parada universal y diagonal RM

### Definición 23.4.1 — Parada universal y diagonal RM {#tlog-def-00161}

Sea Prog el conjunto decidible de códigos Pr(P) de programas RM aprobados, con r≥1. Cada uno puede recibir una sola entrada. Definimos
$$
H=\{S([c,x]):c\in\mathrm{Prog}\text{ y }P_c(x)\text{ para}\},\qquad
K=\{c:c\in\mathrm{Prog}\text{ y }P_c(c)\text{ para}\}.
$$
El programa universal U de CH18 recibe dos naturales (c,z), donde **z es el código S de la lista de argumentos**, y diverge en entradas inválidas. Por tanto para una entrada x lo ejecutamos como U(c,S([x])). No confundimos x con el código de su lista ni con el par externo S([c,x]). Si la ejecución para con registro0 igual a0, sigue perteneciendo a H/K.

El código del programa no especifica una aridad adicional: fijamos aquí su interpretación con una entrada y registros restantes inicializados en0. Todo c∈Prog tiene al menos un registro, por lo que esta interpretación es válida.

## 23.5. Semidecisión uniforme de H y K

### Lema 23.5.1 — Semidecisión uniforme de H y K {#tlog-lem-00105}

**Lema.** H y K son semidecidibles-RM, con rechazo divergente de códigos inválidos.

**Prueba.** Para H se decodifica la lista de longitud2 y se valida c. Si alguna guarda falla se entra en un lazo. En caso válido se ejecuta U(c,S([x])) y se alcanza HALT exactamente si el programa simulado para. Para K se valida c y se ejecuta U(c,S([c])). Las operaciones de empaquetado son totales, y la universalidad ya demostrada da ambos bicondicionales. La prueba no exige salida positiva del programa simulado. $\square$

## 23.6. Indecidibilidad diagonal de la parada

### Metateorema 23.6.1 — Indecidibilidad diagonal de la parada {#tlog-mth-00135}

**Metateorema.** K no es decidible-RM.

**Prueba.** Supongamos un programa total χ que decide K con valores0/1. Construimos un programa D de una entrada: ejecuta χ sobre esa entrada, entra en un lazo divergente si obtiene1 y alcanza HALT si obtiene0. Composición, relocalización de macros y lazo de CH17 producen un programa RM finito válido. Sea d=Pr(D), un natural estándar y miembro de Prog. Entonces
$$
d\in K\iff D(d)\text{ para}\iff χ(d)=0\iff d\notin K,
$$
contradicción clásica. D no necesita contener su propio código ni conocerlo durante su ejecución: d se toma externamente después de construir el programa y se le entrega como entrada. No se usa un teorema de recursión de programas ni equivalencia con máquinas de Turing. $\square$

## 23.7. Parada universal y no semidecidibilidad de sus complementos

### Corolario 23.7.1 — Parada universal y no semidecidibilidad de sus complementos {#tlog-cor-00041}

**Corolario.** H es semidecidible e indecidible; ni ω\K ni ω\H son semidecidibles.

**Prueba.** La función total c↦S([c,c]) reduce K a H, incluyendo c inválido, que queda fuera de ambos lados. Un decidor H daría decidor K. Si el complemento de K o de H fuese semidecidible, sus dos semidecidores producirían por intercalación un decidor, contradiciendo la indecidibilidad. En los complementos hay también códigos inválidos; su reconocimiento decidible no afecta el argumento. $\square$

## 23.8. K es completo para semidecidibilidad RM

### Metateorema 23.8.1 — K es completo para semidecidibilidad RM {#tlog-mth-00136}

**Metateorema.** Para cada A⊆ω semidecidible-RM existe una reducción total computable A≤_m K. Junto con su semidecidibilidad, esto caracteriza a K como completo para esa clase de problemas.

**Prueba constructiva.** Fijamos un semidecidor E de A. Dado n, generamos el programa P_n de una entrada que ignora esa entrada, inicializa un registro protegido con n y ejecuta E(n). El borrado de la entrada, carga de n por n incrementos, copia de registros, instrucciones de E y relocalización de saltos son una construcción finita efectiva uniforme; se pueden generar por bucles acotados en n y el programa fijo E. P_n tiene al menos un registro y una instrucción, y toda salida de una parada se admite. Sea f(n)=Pr(P_n). f es total computable, aunque el tamaño de su código pueda ser enorme. Como la entrada es ignorada,
$$
f(n)\in K\iff P_n(f(n))\text{ para}\iff E(n)\text{ para}\iff n\in A.
$$
No se calcula si E(n) para al generar P_n, ni se utiliza un oráculo. «Completo» aquí describe reducciones entre conjuntos semidecidibles, no completitud del cálculo de primer orden. $\square$

## 23.9. Parada acotada y ausencia de una cota total uniforme

### Proposición 23.9.1 — Parada acotada y ausencia de una cota total uniforme {#tlog-pro-00146}

**Proposición.** Se decide si un programa válido para en alguno de los tiempos0,…,t dados. En cambio no existe una función total computable b(c,x) que, para todo programa válido, acote un tiempo de parada siempre que éste pare en x.

**Prueba.** Se inicializa la configuración, se consulta HALT en tiempo0 y se efectúan a lo sumo t transiciones, consultando cada estado. La parada es absorbente; se consideran ambas ramas DECJZ correctamente. El procedimiento es un bucle acotado con actualización efectiva; la versión sobre códigos es PR por las operaciones sintácticas y recursión acotada de CH22.

Si b fuese total y tuviera la propiedad indicada, para decidir H calcularíamos b(c,x), ejecutaríamos el test acotado y responderíamos no si ningún estado es HALT. Una parada posterior al bound contradice su propiedad, de modo que el procedimiento sería correcto y total, contra §23.7. La inexistencia de esa cota uniforme es compatible con que cada ejecución que para tenga su tiempo finito concreto. La cota t tampoco promete que t pasos simulados se ejecuten en t pasos del intérprete. $\square$

## 23.10. Teoremas, refutaciones y extensiones aritméticas

### Definición 23.10.1 — Teoremas, refutaciones y extensiones aritméticas {#tlog-def-00162}

Para una teoría aritmética T con el cálculo fijado definimos
$$
\operatorname{Th}_{sent}(T)=\{G(A):A\text{ sentencia de }L_A,\ T\vdash A\},
\quad\operatorname{Ref}_{sent}(T)=\{G(A):A\text{ sentencia},\ T\vdash\neg A\}.
$$
En ambas se rechazan códigos inválidos o de fórmulas abiertas. Una T consistente hace disjuntos los dos conjuntos; no hace de Ref el complemento de Th: las sentencias independientes quedan fuera de ambos.

Para el resultado de §23.11 permitimos PA+Γ con Γ un conjunto cualquiera de sentencias de L_A, con prefijos universales como en CH21, sin exigir presentación semidecidible de Γ. «PA es esencialmente indecidible» significará aquí que ninguna extensión consistente de esa clase tiene conjunto de teoremas-sentencias decidible-RM. No se confundirá con la afirmación más débil «PA es incompleta».

## 23.11. Indecidibilidad esencial de PA por diagonalización

### Metateorema 23.11.1 — Indecidibilidad esencial de PA por diagonalización {#tlog-mth-00137}

**Metateorema.** Toda extensión consistente T=PA+Γ de §23.10 tiene Th_sent(T) indecidible-RM. No se necesita efectividad de Γ ni corrección estándar de T.

**Prueba.** Supongamos que la pertenencia a Th_sent(T) se decide por una función total RM. CH19 proporciona una fórmula ρ(z), con representación **bilateral** PA: si un numeral pertenece, PA prueba ρ; si no pertenece, PA prueba ¬ρ. Higienizamos sus variables y diagonalizamos para obtener una sentencia D con PA⊢D↔¬ρ(⌜D⌝). Sea d=G(D).

Si T⊢D, entonces d∈Th_sent(T), luego PA⊢ρ(d̄); pero la prueba de D y el bicondicional dan T⊢¬ρ(d̄), contradiciendo consistencia. Queda T⊬D. Entonces d∉Th_sent(T), y la representación bilateral da PA⊢¬ρ(d̄). El bicondicional implica PA⊢D, por tanto T⊢D, contradicción. Las dos ramas usan sólo pruebas PA de instancias de un decidor supuesto; nunca infieren verdad de un teorema arbitrario T.

La representación bilateral es indispensable para la segunda rama; la mera semidecidibilidad o representación débil no bastaría. No se necesita D2/D3 de demostrabilidad, ni la no refutación de la sentencia de Gödel. $\square$

## 23.12. Teoremas efectivos y complementos no semidecidibles

### Corolario 23.12.1 — Teoremas efectivos y complementos no semidecidibles {#tlog-cor-00042}

**Corolario.** Para toda T presentada y consistente, Th_sent(T) es semidecidible e indecidible, y su complemento en ω no es semidecidible. Lo mismo vale para PA.

**Prueba.** Se guardan códigos de sentencias y se enumeran todos los certificados d, usando el comprobador total de CH21; una aceptación produce parada. Su exactitud proporciona la semidecisión, sin corrección de T. El teorema anterior da indecidibilidad y la doble semidecisión excluye semidecisión del complemento. PA tiene presentación decidible y consistencia externa ya demostrada en CH19. Ref_sent(T) sí es semidecidible por preimagen del constructor de negación; no se lo ha identificado con ese complemento. $\square$

## 23.13. Completitud deductiva y decisión mediante dos búsquedas

### Proposición 23.13.1 — Completitud deductiva y decisión mediante dos búsquedas {#tlog-pro-00147}

**Proposición.** Si una teoría de sentencias es consistente, tiene pruebas semidecidibles y es completa, se decide su conjunto de teoremas mediante dos búsquedas. Por ello una T efectiva consistente que extiende PA no puede ser completa.

**Prueba.** Para una sentencia A se intercalan las búsquedas de una prueba A y de una prueba ¬A. Completitud garantiza alguna parada, consistencia impide ambas, y se responde1/0 respectivamente. Códigos no válidos se rechazan antes. Si T extendiese PA sería un decidor prohibido por §23.11. Esta es una ruta del límite algorítmico al primer teorema, compatible con la demostración constructiva Gödel–Rosser de CH21; no reemplaza su sentencia independiente explícita. Una teoría completa e inconsistente no cumple la hipótesis de exclusión; en PA inconsistente su conjunto de sentencias sería decidible por explosión. $\square$

## 23.14. Consistencia de extensiones finitas y deducción

### Lema 23.14.1 — Consistencia de extensiones finitas y deducción {#tlog-lem-00106}

**Lema.** Para una lista finita Δ=[A_0,…,A_{k−1}] de sentencias, sea F_Δ su conjunción con un orden/asociación fijados; para Δ vacía tomamos F_∅=(0=0). Entonces
$$
T+Δ\text{ inconsistente}\iff T\vdash F_Δ\to\bot_A.
$$
En particular, T+¬A es inconsistente si y sólo si T⊢A.

**Prueba.** Una prueba de \bot_A desde Δ usa sólo esas sentencias; deducción aplicada sucesivamente y lógica proposicional empaquetan su antecedente en F_Δ. La vuelta aplica MP desde los axiomas Δ. Los prefijos universales de cada sentencia añadida se derivan de ella por Q4 y MP, así que no cambian las consecuencias. Para Δ vacía F_∅ es un teorema PA y las dos direcciones siguen por MP/deducción. En Δ=[¬A], (¬A→\bot_A) implica A por PA⊢¬\bot_A y lógica clásica; recíprocamente una prueba A contradice la premisa ¬A. El bicondicional no necesita consistencia de T, aunque sus aplicaciones negativas sí la indiquen. Los constructores de F_Δ y de estas consultas son efectivos. $\square$

## 23.15. Indecidibilidad de consistencia en extensiones finitas

### Metateorema 23.15.1 — Indecidibilidad de consistencia en extensiones finitas {#tlog-mth-00138}

**Metateorema.** Para una T presentada consistente, el conjunto de códigos de listas Δ válidas tales que T+Δ es inconsistente es semidecidible e indecidible; el de las extensiones finitas consistentes no es semidecidible, y tampoco es decidible.

**Prueba.** Por el lema se reduce la consulta de inconsistencia a buscar un certificado T de F_Δ→\bot_A; validación de Δ y compilación de la consulta terminan. Definimos f(c)=S([G(¬A)]) cuando c=G(A) es sentencia, y f(c)=S([])=0 en otro caso. Para entradas válidas el lema da c∈Th_sent(T) si y sólo si T+[¬A] es inconsistente. Para c inválido no hay pertenencia a Th_sent(T), y la lista vacía conserva la consistencia de T. Por tanto f reduce exactamente Th_sent(T) al conjunto de extensiones finitas inconsistentes en todas las entradas; esto prueba indecidibilidad.

Si el conjunto de listas válidas consistentes fuese semidecidible, se intercalaría con el de inconsistentes después de la guarda de validez y se decidiría inconsistencia; los códigos de listas inválidas tienen respuesta negativa antes de intercalar. Contradicción. Obsérvese la diferencia con Con*(T): aquí el objeto de entrada variable es una **lista externa de axiomas**, no un predicado interno de consistencia ni una condición de derivabilidad. $\square$

## 23.16. Existencia de modelos para extensiones finitas

### Corolario 23.16.1 — Existencia de modelos para extensiones finitas {#tlog-cor-00043}

**Corolario.** Para T efectiva consistente, la existencia de algún modelo de T+Δ, con Δ una lista válida de sentencias, es indecidible-RM y no semidecidible-RM; la no existencia es semidecidible. No se pregunta por un modelo estándar.

**Prueba.** El lenguaje L_A es explícitamente numerable. Sus fórmulas/axiomas se bien ordenan por G y el conjunto de premisas puede enumerarse en ese orden, agregando las clausuras universales PA equivalentes. El resultado local de Henkin de CH11 aplica a un conjunto consistente de sentencias en este lenguaje, sin AC/BPI: tiene modelo. Corrección da la vuelta modelo⇒consistencia. Por tanto la existencia coincide exactamente con la consulta de consistencia del teorema anterior. Los modelos pueden ser no estándar; consistencia no se ha convertido en corrección respecto de N_A. Esta aplicación no usa compacidad irrestricta sobre una firma arbitraria ni construye modelos de ZF objeto. $\square$

## 23.17. Verdad aritmética y fragmento Σ1

### Definición 23.17.1 — Verdad aritmética y fragmento Σ1 {#tlog-def-00163}

Definimos conjuntos externos de códigos:
$$
\mathrm{True}_A=\{G(A): A\text{ sentencia de }L_A,\ \mathbb N_A\models A\},
\quad\mathrm{True}_{Σ1}=\{G(σ):σ\text{ sentencia literalmente }Σ1,\ \mathbb N_A\models σ\}.
$$
Se rechazan otros códigos. La satisfacción es la recursión externa del tratado, no un predicado objeto de verdad. True_A es la versión codificada de Th(N_A).

Para reconocer Σ1 se examinan los finitísimos prefijos existenciales iniciales y sus matrices; Δ0 se reconoce recursivamente por átomos, cinco conectivos y cuantificadores acotados con término que no contiene libre la variable ligada. Al expandir ∀x<t y ∃x<t se reconocen las plantillas respectivas. Se admite prefijo existencial vacío. La decisión de pertenencia sintáctica a esa clase es distinta de la decisión de verdad de sus miembros.

## 23.18. Verdad Σ1 semidecidible y completa

### Metateorema 23.18.1 — Verdad Σ1 semidecidible y completa {#tlog-mth-00139}

**Metateorema.** True_Σ1 es semidecidible-RM y K≤_m True_Σ1. Por tanto es completa para semidecidibilidad-RM, indecidible y su complemento no es semidecidible.

**Prueba de semidecisión.** Después de la guarda, se elige un prefijo ∃\vec w con matriz Δ0 y se enumeran tuplas de testigos por altura. Se evalúa su matriz mediante operaciones aritméticas y bucles finitos sobre los bounds; si es verdadera se para. En caso de nombres repetidos se higienizan los ligadores antes de buscar, preservando satisfacción, y se conserva el código original como entrada. Para prefijo vacío hay una sola evaluación; si es falsa se diverge. Esto es uniforme sobre fórmulas finitas, con evaluación recursiva de su árbol; una aceptación equivale a existencia de testigos estándar.

**Reducción.** Sea Φ_U(c,z,y) la fórmula Σ1 de la gráfica del programa universal fijo de dos entradas de CH18/19. Para c∈Prog se genera
$$
σ_c:=\exists y\,Φ_U(\bar c,\overline{S([c])},y),
$$
con ligadores frescos y prefijo existencial aplanado **antes de codificar**. Su verdad equivale a parada de P_c(c), sin condición sobre la salida. Si c es inválido se devuelve G(\bot_A), una sentencia Σ1 de prefijo vacío falsa. La guarda y los constructores de numerales/formulas terminan, por lo que la función c↦G(σ_c) con ese fallback es total computable y reduce K. Completitud se obtiene por transitar las reducciones de §23.8; indecidibilidad y no semidecisión del complemento siguen por transferencia y doble semidecisión. $\square$

## 23.19. Completitud computacional de los teoremas PA

### Metateorema 23.19.1 — Completitud computacional de los teoremas PA {#tlog-mth-00140}

**Metateorema.** Th_sent(PA) es completo para semidecidibilidad-RM. También Th_sent(T) lo es si T es presentada, contiene PA y es correcto para sentencias Σ1.

**Prueba.** Para una σ cerrada Σ1 verdadera elegimos sus finitísimos testigos estándar; la matriz Δ0 verdadera tiene prueba PA por CH19 y la introducción existencial da PA⊢σ. A la inversa PA⊢σ implica verdad por corrección estándar PA. Así, la compilación c↦G(σ_c) del teorema anterior reduce K a Th_sent(PA), incluyendo el fallback falso. Su semidecidibilidad y la completitud de K dan la conclusión. En una T correcta Σ1, una prueba T de σ implica su verdad y PA proporciona todas las pruebas positivas verdaderas; vale el mismo bicondicional.

La mera consistencia de T no justifica la vuelta «T⊢σ⇒N_A⊨σ». CH22 construyó una extensión consistente incorrecta Σ1. Su indecidibilidad ya está demostrada por §23.11, pero esta **reducción particular** no se le atribuye por ese solo antecedente. $\square$

## 23.20. Fragmento finito de bases aritméticas

### Definición 23.20.1 — Fragmento finito de bases aritméticas {#tlog-def-00164}

Sea B_A la lista finita de las ocho bases aritméticas de CH19, cada una universalmente cerrada sobre las variables x,y,z que aparecen:
$$
Sx\ne0;\quad Sx=Sy\to x=y;\quad x\ne0\to\exists z\,x=Sz;
$$
$$
x+0=x;\quad x+Sy=S(x+y);\quad x\cdot0=0;\quad
x\cdot Sy=x\cdot y+x;\quad x<y\leftrightarrow\exists z\,y=x+Sz.
$$
No se incluye el esquema de inducción. Ordenamos las clausuras como aparecen, con índices de variables fijados0,1,2 y asociación de conjunción a la derecha; su conjunción cerrada es A_B. B_A es aquí un **contexto finito de sentencias** del cálculo lógico; no se lo identifica sin cotejo con una presentación externa de Q. N_A satisface todas ellas por CH19.

## 23.21. Pruebas numerales Δ0 desde las ocho bases

### Lema 23.21.1 — Pruebas numerales Δ0 desde las ocho bases {#tlog-lem-00107}

**Lema.** Para cada sentencia Δ0 cerrada, B_A demuestra su polaridad estándar correcta. Por tanto cada sentencia Σ1 cerrada verdadera tiene prueba desde B_A. Se construyen las pruebas externamente por procedimientos finitos; no afirmamos totalización interna en B_A de sus generadores.

**Prueba.** Todo término cerrado se reduce a un numeral por las ecuaciones de suma/producto y congruencia: se recorre el número **concreto** de sucesores del segundo argumento, sin inducción objeto. Numerales distintos se separan cancelando sucesores y usando Sx≠0; < se trata con el segmento numeral siguiente.

B_A demuestra para cada n estándar la fórmula ∀z(z<\bar n↔∨_{i<n}z=\bar i). En n=0, z<0 implica0=z+Sw=S(z+w), contradicción. Supongamos ya construida una prueba del segmento n. De z<S\bar n se obtiene S\bar n=z+Sw=S(z+w), luego \bar n=z+w. La tercera base separa w=0 de w=Su: en el primer caso z=\bar n; en el segundo \bar n=z+Su, esto es z<\bar n, y se aplica la prueba ya construida. La vuelta del nuevo caso z=\bar n usa el testigo0, y los casos previos usan el sucesor del testigo y las ecuaciones. Se universaliza z porque B_A son premisas cerradas. Ésta es una **inducción externa que ensambla una prueba finita para cada numeral n**, sin introducir Ind en B_A.

Inducción externa sobre la fórmula δ trata sus cinco conectivos mediante las filas clásicas. Para un cuantificador acotado cerrado se evalúa el bound numeral y se reemplaza su rango por la disyunción/conjunción finita de instancias, usando el segmento, igualdad y cuantificación. Cada instancia tiene menor complejidad de cuantificadores. Rangos vacíos se resuelven por vacuidad. Esto da prueba de δ o de ¬δ según su evaluación, incluidas fórmulas con cuantificadores acotados anidados. Para σ=∃\vec w δ verdadera, insertamos testigos numerales estándar y agregamos las introducciones existenciales. $\square$

## 23.22. Indecidibilidad de validez y demostrabilidad lógica

### Metateorema 23.22.1 — Indecidibilidad de validez y demostrabilidad lógica {#tlog-mth-00141}

**Metateorema.** En la signatura fija L_A, interpretando sus símbolos de forma arbitraria en estructuras no vacías, el conjunto de sentencias lógicamente válidas es indecidible-RM. Lo mismo vale para los teoremas del cálculo HFOL= desde contexto vacío; ambos conjuntos coinciden.

**Prueba por reducción explícita.** Para c válido generamos la sentencia σ_c de §23.18 y la implicación A_B→σ_c. Si c∈K, σ_c es verdadera Σ1; §23.21 da una prueba desde B_A y deducción da HFOL=⊢A_B→σ_c. Corrección asegura validez en **todas** las estructuras de la signatura, no sólo aritméticas. Si c∉K, N_A satisface A_B pero no σ_c, de modo que es un contramodelo de la implicación. Para c inválido usamos A_B→\bot_A, que tampoco es válido por ese contramodelo. La función es total y reduce K a validez.

Corrección y completitud local de CH11 para el lenguaje explícitamente numerable identifican validez con demostrabilidad lógica. La semidecisión enumera pruebas HFOL= y verifica sus certificados lógicos. No se incluye PA entre los axiomas lógicos: su fragmento finito figura exclusivamente en el antecedente A_B. No se ha usado finita axiomatización de PA, importado Q o supuesto compacidad irrestricta/BPI. $\square$

## 23.23. Satisfacibilidad y no satisfacibilidad de primer orden

### Corolario 23.23.1 — Satisfacibilidad y no satisfacibilidad de primer orden {#tlog-cor-00044}

**Corolario.** En L_A, validez y no satisfacibilidad de sentencias son semidecidibles e indecidibles y sus complementos no son semidecidibles. Satisfacibilidad es indecidible y no semidecidible; su complemento en ω es semidecidible tras incluir códigos inválidos.

**Prueba.** A es válida si y sólo si ¬A no tiene modelo; no se necesita computar un modelo para esta equivalencia semántica clásica. Una sentencia B no tiene modelo si y sólo si HFOL= prueba ¬B, por corrección y la existencia local de modelo para contextos numerables consistentes. Enumerar esas pruebas semidecide no satisfacibilidad. Negación literal reduce validez a no satisfacibilidad; por tanto ambas son indecidibles. Si la clase de sentencias satisfacibles fuese semidecidible, al intercalarla con no satisfacibilidad después de la guarda se decidirían ambas. El complemento total de satisfacibilidad es «código inválido o sentencia sin modelo», una unión semidecidible. No confundimos construir un modelo con comprobar una estructura finita ya dada, ni la clase lógica de todas las estructuras con N_A. $\square$

## 23.24. No definibilidad aritmética de la verdad completa

### Metateorema 23.24.1 — No definibilidad aritmética de la verdad completa {#tlog-mth-00142}

**Metateorema — Tarski en el marco aprobado.** No existe fórmula aritmética θ(z) cuya extensión estándar sea True_A, ni siquiera si se exige su corrección sólo sobre los códigos de sentencias válidas.

**Prueba.** Si existiese, diagonalizamos ¬θ(z) y obtenemos una sentencia L con PA⊢L↔¬θ(⌜L⌝). Por corrección estándar PA, N_A satisface ese bicondicional. La definición supuesta de θ en el código **válido y cerrado** de L daría a la vez N_A⊨L⇔N_A⊨θ(⌜L⌝) y N_A⊨L⇔N_A⊨¬θ(⌜L⌝), contradicción clásica. El comportamiento de θ en códigos inválidos no interviene.

Tampoco ayudan finitísimos parámetros naturales estándar fijados: se sustituyen por sus numerales y queda una fórmula de una coordenada. El teorema no impide la satisfacción externa, predicados de verdad para clases restringidas ni lenguajes más amplios. No usa consistencia de ZF objeto ni una verdad global de la metateoría codificada en sí misma. $\square$

## 23.25. Verdad completa sin semidecisión de ninguna polaridad

### Corolario 23.25.1 — Verdad completa sin semidecisión de ninguna polaridad {#tlog-cor-00045}

**Corolario.** Ni True_A ni ω\True_A son semidecidibles-RM. En particular True_A es indecidible.

**Prueba.** Una semidecisión de True_A daría por CH19 una fórmula Σ1 que define exactamente su extensión estándar, contradiciendo Tarski. Si el complemento fuese semidecidible, tendría una definición Σ1 ρ y ¬ρ definiría True_A, con la misma contradicción. La restricción sintáctica de entrada es decidible, así que una semidecisión de ambas polaridades sólo sobre sentencias también permitiría esos conjuntos totales agregando o rechazando inválidos. En contraste True_Σ1 sí es semidecidible: existe búsqueda de testigos finitos, pero no un predicado aritmético correcto para todas las sentencias. $\square$

## 23.26. Límite uniforme y afirmaciones sobre una sola instancia

### Proposición 23.26.1 — Límite uniforme y afirmaciones sobre una sola instancia {#tlog-pro-00148}

**Proposición.** Los límites demostrados no dicen que ninguna instancia pueda resolverse, que toda sentencia sea independiente ni que cualquier algoritmo práctico deba fallar en cada entrada.

**Prueba.** Indecidibilidad excluye un único decidor total correcto para **todas** las entradas de una familia; una entrada fija tiene externamente una respuesta clásica y puede admitir una prueba particular. Incompletitud afirma existencia de sentencias independientes bajo hipótesis determinadas; axiomas y consecuencias probadas siguen teniendo pruebas. No definibilidad de True_A excluye una fórmula aritmética que satisfaga todos los bicondicionales, no una definición de un fragmento. El segundo teorema concierne a Con*(T) con el representante fijado, bajo consistencia de T, y no excluye una prueba externa o la de un fragmento propio. Cada conclusión conserva su cuantificación y nivel; no se la traduce a una afirmación general de incertidumbre sobre números grandes. $\square$

## 23.27. Presentación efectiva de polinomios sobre naturales

### Definición 23.27.1 — Presentación efectiva de polinomios sobre naturales {#tlog-def-00165}

Un dato polinómico válido es e=S([r,p,q]), con r≥0 y p,q códigos S de listas de monomios. Cada monomio es S([a,S([k_0,…,k_{r−1}])]), coeficiente a natural y exponentes naturales. La lista vacía representa0; coeficientes0 y monomios repetidos son admisibles. p representa P(\vec x)=Σ a∏x_i^{k_i}, y q representa Q. Definimos
$$
\operatorname{Dio}_{\mathbb N}=\{e\text{ válido}:\exists\vec x\in\omega^r\ P(\vec x)=Q(\vec x)\}.
$$
Para r=0 hay exactamente la tupla vacía y los productos vacíos valen1; la consulta es igualdad de dos constantes. La numeración no se declara inyectiva sobre polinomios como funciones: dos listas diferentes pueden representar el mismo polinomio.

Usar dos lados con coeficientes no negativos permite expresar un polinomio de coeficientes enteros como P−Q sin introducir enteros como dominio de las incógnitas. El dominio aquí es ω, incluidos0, y no Z/Q u otro anillo. Los códigos inválidos no pertenecen a Dio_N.

## 23.28. Validación y evaluación polinómica total

### Lema 23.28.1 — Validación y evaluación polinómica total {#tlog-lem-00108}

**Lema.** Se decide validez de e y de una tupla de longitud r; se calcula totalmente la evaluación de cada polinomio. Para e válido y B dado se decide si existe solución con todas las coordenadas≤B.

**Prueba.** Decodificar S y verificar longitudes exactas es total. Potencias se calculan con k multiplicaciones, incluido x^0=1 y0^0=1 como valor del monomio; productos y sumas recorren listas finitas. Para la caja se generan las tuplas de {0,…,B}^r por productos finitos de listas y se comparan las evaluaciones. Para r=0 se genera una sola tupla vacía; no una lista de opciones vacía. Los bucles tienen medidas finitas explícitas y están en la clase PR; ningún paso decide una existencia sobre todas las alturas. Monomios repetidos se suman, no se descartan. $\square$

## 23.29. Semidecidibilidad uniforme de soluciones diofánticas

### Metateorema 23.29.1 — Semidecidibilidad uniforme de soluciones diofánticas {#tlog-mth-00143}

**Metateorema.** Dio_N es semidecidible-RM. Si se proporciona un testigo de solución, su verificación es decidible; si no hay solución, el procedimiento uniforme puede divergir.

**Prueba.** Tras validar e, recorremos B=0,1,2,… y decidimos si su caja de altura B tiene una solución; al encontrarla alcanzamos HALT. Cualquier solución tiene una altura finita igual al máximo de sus coordenadas (0 para la tupla vacía), luego aparecerá. Una aceptación implica una solución real por exactitud de la evaluación. En r=0 la primera caja decide la igualdad constante; si es falsa, el semidecidor entra explícitamente en un lazo. Códigos inválidos divergen. No se presume una cota computable de los testigos ni que una búsqueda sin éxito hasta B certifique inexistencia. Este resultado es elemental y no usa MRDP. $\square$

## 23.30. Traducción polinómica a sentencias existenciales

### Proposición 23.30.1 — Traducción polinómica a sentencias existenciales {#tlog-pro-00149}

**Proposición.** Existe una función total computable que reduce Dio_N a True_Σ1. En entradas válidas construye el árbol literal ∃x_0…∃x_{r−1}(t_P=t_Q), donde t_P,t_Q son los términos de los polinomios.

**Prueba.** Cada coeficiente se convierte en su numeral; una potencia se expande como k productos con valor inicial1; monomios y suma se asocian en un orden fijo, y la lista vacía produce el término0. En r=0 el bloque de cuantificadores es vacío y queda igualdad cerrada. N_A interpreta ese término como la evaluación calculada por §23.28, por inducción sobre los constructores. Por ello la sentencia es verdadera exactamente cuando e∈Dio_N. Las variables del prefijo son distintas y el prenexo queda construido antes de calcular G. Para un e inválido se devuelve G(\bot_A). La compilación termina incluso si no hay solución.

La dirección es **Dio_N≤_m True_Σ1**. Aunque True_Σ1 sea indecidible, esta reducción no demuestra indecidibilidad de Dio_N; reducir a un problema difícil no prueba que el problema de origen tenga esa dificultad. $\square$

## 23.31. Cotas computables de testigos y decisión diofántica

### Metateorema 23.31.1 — Cotas computables de testigos y decisión diofántica {#tlog-mth-00144}

**Metateorema.** Dio_N es decidible-RM si y sólo si existe una función total computable b(e) tal que, para cada e válido soluble, alguna solución tenga todas sus coordenadas≤b(e). No se afirma en este capítulo que tal función exista o no exista.

**Prueba.** Dada b se valida e, se calcula b(e) y se explora la caja finita; si no hay solución allí, la propiedad del bound excluye cualquier solución. Para inválidos se responde0. Recíprocamente, dado un decidor, para inválidos o insolubles fijamos b(e)=0; para solubles buscamos alturas B hasta encontrar un testigo y devolvemos la primera altura. El decidor asegura que esa rama positiva termina. r=0 está cubierto por la altura0. El programa completo es total, aunque no se haya fijado una cota de sus tiempos. El bound acota **algún** testigo cuando existe, no todos los testigos, ni la cantidad de soluciones. $\square$

## 23.32. Contrato condicional para transferir indecidibilidad a Dio

### Proposición 23.32.1 — Contrato condicional para transferir indecidibilidad a Dio {#tlog-pro-00150}

**Proposición condicional.** Si un desarrollo posterior aporta una función total computable f con c∈K⇔f(c)∈Dio_N, entonces Dio_N es indecidible, su complemento no es semidecidible y no existe el bound de §23.31. La hipótesis de esa reducción no está demostrada en TLOG.

**Prueba de la implicación.** Transferencia de un supuesto decidor Dio_N daría decidor K. Como Dio_N ya es semidecidible, semidecisión de su complemento daría decidor y la contradicción anterior. El bound sería equivalente a decisión por el teorema citado. Cada conclusión depende de la **reducción en la dirección K→Dio_N**. La traducción de §23.30 tiene la dirección contraria a la requerida para el origen K y no la sustituye.

Éste es el lugar lógico donde una representación diofántica suficientemente uniforme podría entrar. No importamos MRDP/Jones ni la tesis de que todo conjunto RM semidecidible sea diofántico. Si un texto usa otro sistema operacional, necesita además un puente efectivo demostrado; la equivalencia RM–Turing no aparece por cambiar el vocabulario. El resultado cerrado aquí es la implicación, no su antecedente. $\square$

## 23.33. Dominios diofánticos y cambios de problema

### Proposición 23.33.1 — Dominios diofánticos y cambios de problema {#tlog-pro-00151}

**Proposición.** La solubilidad sobre N, Z y Q son consultas diferentes. La transformación de una incógnita entera en diferencia de dos naturales permite reducir solubilidad entera a solubilidad natural, pero no da por sí sola una reducción de vuelta.

**Prueba.** Fijamos para los datos enteros el código S([r,p]), donde p es una lista de monomios S([S([a,b]),S([k_0,…,k_{r−1}])]) y el coeficiente entero significa a−b. Las guardas y longitudes son decidibles; datos inválidos se envían a la ecuación nularia natural0=1, que no tiene solución. Toda z∈Z puede escribirse u−v, u,v∈N; al sustituir x_i=u_i−v_i en un polinomio entero se expande un nuevo polinomio entero sobre2r variables. Separar coeficientes positivos/negativos produce dos polinomios naturales P,Q como §23.27. Una solución entera produce una natural por elección explícita (max(z,0),max(−z,0)); una solución natural del transformado produce la entera por diferencias. La expansión y separación son procedimientos finitos efectivos, con codificación explícita de signos por pares. Esto describe una reducción desde datos enteros válidos al dominio natural, no una identificación de los dominios.

No se ha probado aquí que exigir variables naturales pueda expresarse mediante ecuaciones sobre enteros sin nuevas hipótesis; no invocamos el teorema de cuatro cuadrados ni transferimos automáticamente a Q. Cambiar número de variables, grado, positividad estricta, finitud de soluciones o un polinomio universal también cambia la obligación. Esas cotas y traducciones deben figurar en el contrato posterior y no se heredan del mero nombre «ecuación diofántica». $\square$

## 23.34. Contrato de salida hacia GAS

### Definición 23.34.1 — Contrato de salida hacia GAS {#tlog-def-00166}

La frontera de TLOG ofrece a GAS, para una futura interfaz expresamente aprobada: numeración S/G y guardas; RM/H/K con pruebas de semidecidibilidad e indecidibilidad; reducciones totales y su dirección; representación Σ1 y demostrabilidad con sus hipótesis; Dio_N con evaluación, semidecisión y equivalencia entre decisión y bound computable.

Una ficha de interfaz deberá declarar: fuente canónica y versión de cada proveedor; dominio de incógnitas; formato de polinomio; función de traducción total con fallback inválido; bicondicional de pertenencia probado; sistema operacional de origen y puente si difiere; hipótesis aritméticas; y evidencia humana/computacional/Lean separada. Ninguna ficha activa se crea por esta definición: interfaces intertratados activas siguen0.

Se conservan las clases de reutilización de procedencia: PATTERN-REUSE para un método editorial; CONTENT-SEED para material que debe reconstruirse; REFERENCE-ONLY para contraste; NO-CARRYOVER para conclusiones o evidencias no transferibles. Un ID GAS no se convierte en ID TLOG y una prueba Lean externa no verifica una unidad propia sin correspondencia y revisión explícitas.

## 23.35. Lo que no se exporta por cerrar el tratado

### Proposición 23.35.1 — Lo que no se exporta por cerrar el tratado {#tlog-pro-00152}

**Proposición.** El cierre del tratado no aporta automáticamente un teorema MRDP, una ecuación universal Jones/S126, una interpretación aritmética en ZF objeto, ni verificaciones Lean de sus resultados.

**Prueba por inspección del contrato.** Ninguna reducción K→Dio_N se ha producido; el proveedor §23.32 es condicional. No hay ecuación universal o cotas de grado/variables en las definiciones polinómicas. Las aplicaciones a teorías T requieren presentación y base PA; para ZF objeto se necesitaría además interpretación, preservación de derivaciones y el representante correspondiente. Los archivos Python sólo ensayan referencias finitas y el DAG; no son archivos Lean ni un verificador de derivaciones PA. La comprobación SHA-256 prueba identidad de bytes sincronizados, no estas afirmaciones matemáticas. Toda incorporación futura debe reabrir la arquitectura/contrato pertinente sin modificar retroactivamente el estado de evidencia ya acreditado. $\square$

## 23.36. Mapa final de hipótesis y tipos de límite

### Proposición 23.36.1 — Mapa final de hipótesis y tipos de límite {#tlog-pro-00153}

**Proposición.** Las conclusiones finales tienen las siguientes hipótesis y sentidos diferentes.

| Objeto | Hipótesis | Conclusión aprobada |
|---|---|---|
| K/H | RM y codificación/universalidad aprobadas | semi, indecidibles; complementos no semi |
| Th_sent(T), T⊇PA | consistencia simple, sin efectividad necesaria para no decisión | indecidible |
| Th_sent(T) presentada | consistencia simple | semi y complemento no semi |
| Th_sent(T) presentada y correcta Σ1 | además de contener PA | completa para semi-RM por la reducción concretaΣ1 |
| True_Σ1 | estructura estándar externa | semi y completa para semi-RM |
| validez/no satisfacibilidad enL_A | todas las estructuras, lenguaje numerable | semi e indecidibles |
| True_A | PA estándarmente correcta y diagonalización | no definible aritméticamente, ninguna polaridad semi |
| Con*(T) | presentación fijada, Prov* conD1–D3, consistencia | Tno la prueba |
| reflexiónlocal □A→A | Prov* conD1–D3, no consistencia necesaria | Tla prueba si y sólo si TpruebaA |
| Dio_N | presentación polinómica natural | semi; indecidibilidad sólo bajo la reducción adicional indicada |

**Prueba.** Cada fila es una aplicación literal del resultado citado; el cambio de hipótesis se controla en las demostraciones correspondientes. Semidecidibilidad de una verdad restringida no implica definibilidad de toda verdad; correcciónΣ1 no se deduce de consistencia; completitud del cálculo no se confunde con completitud de una teoría o de un grado de reducción. $\square$

## 23.37. Cierre de la Parte V

### Corolario 23.37.1 — Cierre de la Parte V {#tlog-cor-00046}

**Corolario.** La Parte V cierra el primer teorema, el segundo para el representante realizado, Löb, indecidibilidad de la parada/teorías/validez y no definibilidad de la verdad, y fija su frontera diofántica. Las tres salidas corresponden a CH21,CH22,CH23 respectivamente.

**Prueba.** CH21 entrega Gödel–Rosser bajo consistencia simple y separa las hipótesis de Gödel; CH22 entregaProv* conD1–D3 yCon*/Löb; los resultados de este capítulo dan las reducciones y límites restantes. La semidecisión diofántica elemental y el contrato condicional no anticipan una prueba MRDP. Ninguna dependencia exige un futuro capítulo24: la arquitectura aprobó CH00–CH23, veinticuatro capítulos en total. La Parte V pasa aCLOSED por cierre matemático humano; formalización y publicación siguen separadas. $\square$

## 23.38. Cierre matemático del alcance aprobado de TLOG

### Corolario 23.38.1 — Cierre matemático del alcance aprobado de TLOG {#tlog-cor-00047}

**Corolario.** Queda completado el alcance matemático humano de los 24 capítulos aprobados delTratado de lógica, en5 partes. El cierre conserva los ID/resultados/DAG, las distinciones fundacionales y la frontera conFND/GAS.

**Prueba de alcance.** La arquitectura canónica enumera CH00–CH23; el checkpoint anterior tenía cerrados CH00–CH22 y lasPartesI–IV. Este capítulo cierra la salida de laParte V mediante el corolario precedente. Los capítulos iniciales, resultados locales de corrección/completitud y su dependencia de hipótesis conjuntistas no se reescriben ni se fortalecen: en especial, cierre del tratado no añadeBPI oAC aM_ext. La integración comprueba IDsconsecutivos, igualdad exacta registro/grafo y ausencia de ciclos, duplicados o dependencias huérfanas.

«CLOSED» acredita las pruebas autorales humanas y el alcance declarado, no un libro publicado, una verificaciónLean completa o una revisión editorial integral nueva de todos los capítulos. Esa auditoría general de cierre/publicación será una operación posterior concreta sobre la obra completa. Se mantienen0 resultadosLean verificados,0 interfaces activas y0 capítulos publicados. No se abre un capítulo adicional por este contrato. $\square$

## 23.39. Ejemplos y balance final

Una máquina HALT pertenece aH en cualquier entrada, incluso cuando devuelve0. Un lazo INC no pertenece, aunque su simulación acotada termine y pueda comprobarse hasta cualquier tiempo dado. La diferencia está entre evaluar una ventana finita y decidir la existencia de algún tiempo de parada.

En Dio_N, x²+1=x² carece de solución y puede refutarse con una prueba elemental particular; x²=4 tiene testigo2 y su verificación finita termina. Para r=0,2=2 tiene la tupla vacía como solución, mientras2=3 no la tiene. Estos ejemplos no constituyen un decidor general ni prueban por sí mismos la indecidibilidad diofántica pendiente de una reducción adicional.

El capítulo cierra **38/38 resultados** y **184 aristasdirectas nuevas**. Acumulado **667 resultados /2573 aristas**, sin ciclos, duplicados ni huérfanos. **24/24 capítulos y5/5 partes cerrados matemáticamente por pruebas humanas**. Lean **297 candidatos /0compilados /0verificados**; interfaces activas0; capítulos publicados0. Fuentes15identidades,2TEXT-COLLATEDprevias y nuevos controles online limitados, sin colación integral. QAhumana, regresiones de referencias y cotejo debytes se documentan por separado.

```text
LOCAL  CH23 ████████████████████ 38/38 resultados (100 %)
GLOBAL TLOG ████████████████████████ 24/24 capítulos (100 %)
```

La continuación natural es una **auditoría general de cierre y preparación editorial** de los 24 capítulos, con alcance y evidencias separados de formalización/publicación. No se anuncia una auditoría integral de toda la obra por el mero cierre de este capítulo.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 22](capitulo-22.md) · 


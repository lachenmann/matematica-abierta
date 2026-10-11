---
title: Capítulo 21 — Primer teorema de incompletitud
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
content-id: MA-BCH-0223
content-type: book-chapter
source-id: TLOG-CH21-0001
prerequisites:
- MA-BCH-0211
- MA-BCH-0212
- MA-BCH-0220
- MA-BCH-0221
- MA-BCH-0222
related:
- MA-BOK-0014
source-sha256: 9807a33f0072d063de6707f223accbe2d5e39e55bd470c7f99ea926cdf0c0aa9
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 20](capitulo-20.md) · [Capítulo 22 →](capitulo-22.md)

## 21.0. De un bicondicional a un límite de las pruebas

El lema diagonal construyó sentencias que PA relaciona con predicados aplicados a sus propios códigos. Ahora necesitamos analizar qué pruebas podrían tener esas sentencias en una teoría T determinada. La efectividad de los axiomas proporciona certificados comprobables; la representación aritmética traduce cada comprobación concreta en una prueba PA; la consistencia permite excluir pares contradictorios de derivaciones.

Primero estudiaremos la sentencia de Gödel, verdadera y no demostrable bajo consistencia, y su independencia bajo ω-consistencia o corrección Σ1. Después construiremos la sentencia de Rosser y probaremos sus dos lados de independencia con consistencia simple. El paso decisivo será distinguir entre infinitas instancias numerales y una prueba para un segmento numeral finito. Finalmente examinaremos qué ocurre al añadir axiomas independientes, y por qué la teoría externa de todas las verdades no puede tener la presentación efectiva considerada.

El capítulo mantiene PA como base aprobada y RM como sistema operacional externo. Las pruebas son autorales y humanas, apoyadas en las interfaces canónicas de CH17–20. Como control primario limitado se consultaron la sección4.6 de las notas de Jeremy Avigad, *Computability and Incompleteness* (versión9enero2007), y el extracto/metadata del artículo de Rosser (1936). El primero trabaja sobre Q y otro formato de prueba; no se importa esa base ni se transfiere su numeración. Nuestros dos argumentos Rosser se desarrollan completos con certificados S/G, guardas y la convención e≤d.

## 21.1. Apertura de la Parte V y alcance del teorema

### Convención 21.1.1 — Apertura de la Parte V y alcance del teorema {#tlog-cnv-00032}

Seguimos en $M_{ext}=\mathrm{ZF}$ clásica sin AC/BPI. La estructura estándar $\mathbb N_A$ y RM son externos; PA es la teoría aritmética objeto de CH19, distinta de $\mathrm{ZF}_{obj}$. La Parte V comienza con un límite preciso: una extensión **consistente** de PA que tenga una presentación semidecidible de sus axiomas no puede decidir por prueba todas las sentencias aritméticas.

Las hipótesis de consistencia de teorías T serán externas y explícitas. La corrección estándar de PA fue demostrada en CH19; no se presume corrección de toda extensión T. Ningún resultado de este capítulo se aplica a ZF objeto sin una interpretación aritmética y una presentación efectiva acreditadas. Tampoco se usa equivalencia RM–Turing.

Por «sentencia indecidida en T» entenderemos que T no demuestra ni la sentencia ni su negación. Esta propiedad de una sentencia concreta se distingue de la indecidibilidad algorítmica del conjunto de teoremas; las reducciones correspondientes se reservan a CH23. El segundo teorema de incompletitud, la fórmula interna de consistencia y las condiciones internas de derivabilidad pertenecen a CH22.

## 21.2. Presentación efectiva de una extensión aritmética

### Definición 21.2.1 — Presentación efectiva de una extensión aritmética {#tlog-def-00149}

Una presentación admisible consta de un programa RM fijo E de un argumento y una clase Γ de **sentencias** de $L_A$ tal que E para en el código c exactamente cuando c codifica un miembro de Γ. La salida de una parada es irrelevante. Se puede envolver cualquier semidecidor con la guarda decidible «c es código de sentencia aritmética». La teoría presentada es
$$
T=\mathsf H_{L_A}^{=}+A_{PA}+\operatorname{Pref}_{\forall}(\Gamma),
$$
desde ninguna premisa adicional, donde Pref incluye todos los prefijos universales finitos, incluso el vacío. La única regla primitiva es MP. Como Γ contiene sentencias, cada prefijo de C∈Γ se deriva de C por Q4 y MP: las variables del prefijo no son libres. Por tanto esta clausura no cambia la teoría deductiva PA+Γ.

El conjunto adicional $A_T=A_{PA}\cup\operatorname{Pref}_{\forall}(\Gamma)$ es semidecidible: tras validar la fórmula se acepta si es axioma PA; además se ejecutan intercaladamente E sobre las finitísimas matrices obtenidas retirando prefijos universales, reteniendo sólo las que son sentencias. Alguna parada acredita un miembro de Γ y el prefijo correspondiente. Si ninguna para, el procedimiento continúa. Su programa fijo se puede generar efectivamente a partir de E. La decidibilidad de Γ es un caso especial, no una exigencia adicional.

No se admite como sustituto una mera numeración abstracta de los axiomas. La consistencia no forma parte de la guarda que valida códigos de programas: se declarará como hipótesis matemática separada.

## 21.3. Verificador total de pruebas certificadas de T

### Lema 21.3.1 — Verificador total de pruebas certificadas de T {#tlog-lem-00086}

**Lema.** Para toda presentación admisible hay una relación externa decidible-RM $C_T(d,c)$ que reconoce exactamente las pruebas certificadas no vacías de T con conclusión de código c. Se cumple
$$
T\vdash A\iff\exists d\ C_T(d,G(A)).\tag{C}
$$
No se requiere consistencia de T para construir el verificador ni para (C).

**Prueba.** Aplicamos §18.61 al semidecidor fijo de $A_T$ construido en §21.2. d es el código S de una lista de líneas de los cuatro tipos0/1/2/3. No hay contexto: el tipo0 de premisa no puede justificar ninguna línea. El tipo1 lleva certificado de axioma lógico; el tipo2 lleva dos índices precedentes para MP; el tipo3 acredita un axioma adicional con una traza finita de parada del semidecidor. Se verifican todos los tipos, longitudes y referencias antes de usarlos, y la última fórmula debe tener código c. Una traza que termina con salida0 también es un certificado de parada válido.

El recorrido es finito, y cada test, incluido el de traza, es total. Una aceptación se borra en una derivación T original. Recíprocamente una derivación original tiene finitísimas apariciones de axiomas adicionales; para cada una el semidecidor para, y su primera traza de parada suministra el certificado. Se recorren esas apariciones en orden y se elige su mínimo tiempo de parada, sin elección infinita. Así se obtiene una lista certificada y su código d. Este proceso de certificación termina sobre una derivación T válida, aunque no se prometa terminación sobre una derivación arbitraria con una pretendida línea adicional inválida.

La decisión de pruebas certificadas no implica decisión de secuencias originales desnudas bajo la mera semidecidibilidad de axiomas. Se conserva la numeración S/G; no se mide longitud textual al comparar números d. $\square$

## 21.4. Predicados de prueba positiva, negativa y demostrabilidad

### Definición 21.4.1 — Predicados de prueba positiva, negativa y demostrabilidad {#tlog-def-00150}

Además de $C_T(d,c)$ fijamos $C_T^-(d,c)$: se rechaza si c no codifica una fórmula aritmética A; en otro caso se calcula G(¬A) y se prueba $C_T(d,G(¬A))$. Es un decidor total compuesto; no se agrega un símbolo objeto de negación de códigos.

Representamos los decidores característicos0/1 de ambas relaciones mediante sus programas concretos y las fórmulas de CH19. Ponemos
$$
P_T(d,c)=\Phi_{\chi_C}(d,c,\bar1),\qquad
N_T(d,c)=\Phi_{\chi_{C^-}}(d,c,\bar1),\qquad
V_T(c)=\exists d\ P_T(d,c).
$$
P y N son fórmulas Σ1 con sólo sus dos argumentos libres; V se dispone en forma Σ1 reuniendo los existenciales de P. Los auxiliares se higienizan por §20.3. Los tres nombres son abreviaturas de fórmulas, no predicados primitivos. P representa una prueba de la fórmula nombrada; N representa una prueba de su **negación literal**.

Para T=PA se puede usar también el verificador de pruebas originales y el $Prov_{PA}$ ya fijado en CH19. La presentación certificada actual puede producir otro representante. No se identifica uniformemente con el anterior dentro de PA sin una prueba adicional.

## 21.5. Exactitud numeral y estándar de los predicados de prueba

### Metateorema 21.5.1 — Exactitud numeral y estándar de los predicados de prueba {#tlog-mth-00117}

**Metateorema.** P y N representan bilateralmente sus relaciones externas en PA y son exactos en $\mathbb N_A$. V define allí exactamente los códigos de teoremas T. Si $T\vdash A$, entonces $\mathrm{PA}\vdash V_T(\ulcorner A\urcorner)$; para cada prueba concreta se puede obtener una prueba PA de esa instancia. Estas afirmaciones no suponen corrección ni consistencia de T.

**Prueba.** Los dos decidores son totales, por lo que §19.24 prueba, para cada par estándar(d,c), la instancia correspondiente o su negación según el resultado del verificador. Corrección PA da la exactitud estándar. Por (C), una prueba T de A tiene un certificado concreto d, y PA prueba $P_T(\bar d,\ulcorner A\urcorner)$; introducción existencial da V de su código. Recíprocamente, la satisfacción estándar de V da un natural d con certificado real, luego una prueba T por borrado.

El conjunto de teoremas T es semidecidible por enumeración de certificados, así §19.25 proporciona también representación débil de ese conjunto **en PA**. No se afirma representación débil en T: una extensión incorrecta puede demostrar V de un código sin tener una prueba real de esa fórmula.

La obtención efectiva de la prueba PA positiva usa el programa de representación: su ejecución finita concreta, la tabla β externa y pruebas de la matriz Δ0, seguidas de introducción existencial y funcionalidad. También puede buscarse esa prueba con el verificador PA, pues su existencia quedó probada. El enunciado metateórico «T demuestra A ⇒ PA demuestra V del código de A» es numeral por numeral; no se ha demostrado una condición interna uniforme sobre todas las pruebas/códigos de T. $\square$

## 21.6. De un número finito de instancias a una cota numeral

### Lema 21.6.1 — De un número finito de instancias a una cota numeral {#tlog-lem-00087}

**Lema.** Para una fórmula F(v) con sólo v libre y un natural externo n, si PA prueba F(\bar k) para cada k<n, entonces PA prueba $\forall v(v<\bar n\to F(v))$. Para k≤n se obtiene $\forall v(v\le\bar n\to F(v))$. Si PA prueba las negaciones de esas instancias, se obtiene el mismo resultado con ¬F. No se exige que F sea Δ0.

**Prueba.** El lema de segmentos de CH19 prueba $v<\bar n\leftrightarrow(v=\bar0\lor\cdots\lor v=\overline{n-1})$. Para cada k, igualdad y F(\bar k) dan $v=\bar k\to F(v)$. La eliminación proposicional de la disyunción finita da la implicación requerida, y se generaliza v. Con n=0 el antecedente es refutable y la implicación se obtiene por lógica. La versión ≤ usa v<S\bar n, y la versión negativa usa ¬F como fórmula. Los términos numerales son cerrados y los nombres de los esquemas se eligen frescos.

El procedimiento usa **una lista finita** de pruebas ya disponibles y un segmento numeral fijo. No convierte una familia infinita de pruebas F(\bar n) en una prueba $\forall vF(v)$, ni exige totalidad interna del programa que decide las instancias de F. Esta distinción será central en Rosser. $\square$

## 21.7. Completitud de una teoría e independencia de una sentencia

### Definición 21.7.1 — Completitud de una teoría e independencia de una sentencia {#tlog-def-00151}

Una teoría T es **completa para sentencias** si para toda sentencia aritmética A se cumple $T\vdash A$ o $T\vdash\neg A$. Una sentencia A es **independiente (o indecidida) en T** si no se cumple ninguna de las dos pruebas. Esta completitud se distingue de la completitud del cálculo de primer orden respecto de consecuencia semántica: un cálculo completo puede formalizar una teoría incompleta.

Se mantienen las definiciones externas de consistencia, corrección estándar, corrección Σ1 y ω-consistencia de §20.26. Para $0=S0$ se escribe ⊥ sólo como abreviatura de una contradicción objeto fija. «No existe una prueba» es una afirmación externa; no se identifica con «la negación es un teorema».

El enunciado de incompletitud tendrá la forma de una implicación externa: si la presentación de T es admisible y T es consistente, existe una sentencia independiente. El algoritmo constructor no recibe una prueba interna de consistencia ni decide si la hipótesis se cumple.

## 21.8. Implicaciones entre las hipótesis de corrección

### Proposición 21.8.1 — Implicaciones entre las hipótesis de corrección {#tlog-pro-00134}

**Proposición.** La corrección estándar implica corrección Σ1 y ω-consistencia; ambas implican consistencia en una extensión de PA. La ω-consistencia y la corrección Σ1 se usarán como dos hipótesis suficientes separadas; aquí no se establece una equivalencia entre ellas.

**Prueba.** La restricción a sentencias Σ1 es inmediata. Si una teoría estándar correcta prueba $\exists xF(x)$, hay un natural externo n que satisface F; no puede probar también ¬F(\bar n), por corrección. Esto excluye el patrón de ω-inconsistencia. Si una teoría es Σ1-correcta no puede probar la sentencia Δ0 falsa $0=S0$; Δ0 es Σ1 con prefijo vacío. Si fuera inconsistente, por explosión probaría $\exists x(x=x)$ y cada ¬(\bar n=\bar n), contra ω-consistencia. La corrección estándar también excluye directamente toda contradicción falsa.

No se asigna ninguna de las hipótesis fuertes a una extensión T por el solo hecho de ser consistente. §21.16 dará una extensión efectiva consistente que es incorrecta y ω-inconsistente. $\square$

## 21.9. Una sentencia de Gödel para cada presentación

### Definición 21.9.1 — Una sentencia de Gödel para cada presentación {#tlog-def-00152}

Aplicamos el compilador diagonal al objetivo $A(z)=\neg V_T(z)$. Fijamos su salida $G_T$ y una prueba PA de
$$
\mathrm{PA}\vdash G_T\leftrightarrow\neg V_T(\ulcorner G_T\urcorner).\tag{G}
$$
G_T es una sentencia finita de $L_A$; g=G(G_T) es su código literal y $\ulcorner G_T\urcorner=\bar g$ es un término numeral. La prueba de (G) persiste en T. Esta elección depende de la presentación, del representante P y de la construcción diagonal fijada.

Se admiten otras sentencias con una prueba PA del mismo tipo de bicondicional respecto del representante correspondiente. En particular la $\mathcal G_{PA}$ canónica de CH20 usa el $Prov_{PA}$ original y se conservará sin cambiar su árbol o su ID. No se afirma aquí que la salida existencial genérica del compilador sea literalmente una fórmula Π1.

## 21.10. No demostrabilidad y verdad de la sentencia de Gödel

### Metateorema 21.10.1 — No demostrabilidad y verdad de la sentencia de Gödel {#tlog-mth-00118}

**Metateorema.** Si T tiene presentación admisible y es consistente, $T\nvdash G_T$ y $\mathbb N_A\models G_T$. Esto no exige corrección estándar de T ni ω-consistencia.

**No demostrabilidad.** Supongamos una prueba T de G_T. Su certificado concreto y §21.5 dan $\mathrm{PA}\vdash V_T(\bar g)$, luego $T\vdash V_T(\bar g)$. Por (G), la prueba supuesta de G_T da también $T\vdash\neg V_T(\bar g)$. El par contradictorio viola consistencia. Por tanto no existe tal prueba.

**Verdad externa.** La exactitud estándar de V identifica $\mathbb N_A\models V_T(\bar g)$ con una prueba real T de G_T. Acabamos de excluirla, así V(\bar g) es falsa en el modelo estándar. La prueba PA de (G) es verdadera por corrección PA, y por tanto G_T es verdadera. El paso no aplica corrección a T: usa corrección de una derivación **PA**, junto con la ausencia externa de pruebas T.

El argumento prueba sólo el primer lado de independencia. La consistencia sola no proporciona aquí una refutación de una supuesta prueba T de ¬G_T. $\square$

## 21.11. Forma de Gödel bajo ω-consistencia

### Metateorema 21.11.1 — Forma de Gödel bajo ω-consistencia {#tlog-mth-00119}

**Metateorema.** Si T es ω-consistente y tiene presentación admisible, G_T es independiente en T.

**Prueba.** ω-consistencia implica consistencia por §21.8; el sentido positivo queda excluido por §21.10. Como no hay prueba T de G_T, para cada natural d la relación externa $C_T(d,g)$ es falsa. La representación bilateral da $\mathrm{PA}\vdash\neg P_T(\bar d,\bar g)$, luego T prueba esas negaciones para **todos los numerales externos**, una por una.

Si T probara ¬G_T, (G) y lógica clásica darían $T\vdash V_T(\bar g)=\exists dP_T(d,\bar g)$. La fórmula F(d)=P_T(d,\bar g) tiene sólo d libre; su parámetro g ha sido sustituido por un término cerrado. T probaría su existencia y negaría cada instancia numeral, precisamente el patrón prohibido por ω-consistencia. Se excluye la prueba negativa y queda independencia. No se requiere F acotada ni se afirma que exista una prueba T de su negación universal. $\square$

## 21.12. Forma de Gödel bajo corrección Σ1

### Metateorema 21.12.1 — Forma de Gödel bajo corrección Σ1 {#tlog-mth-00120}

**Metateorema.** Si T es Σ1-correcta y tiene presentación admisible, G_T es independiente en T.

**Prueba.** Σ1-corrección implica consistencia. Por §21.10, G_T no es teorema y V_T(\bar g) es falsa en el modelo estándar. Si T probara ¬G_T, (G) produciría una prueba T de V_T(\bar g), que es una sentencia Σ1 falsa, contra la hipótesis. Se excluyen ambos lados.

Es suficiente la corrección Σ1, porque la sentencia falsa utilizada es V, aunque la fórmula literal G_T obtenida por el compilador no haya sido clasificada como Π1. La corrección de todas las sentencias de T es una hipótesis más fuerte que la necesaria para este paso. $\square$

## 21.13. Independencia de la sentencia PA ya construida

### Corolario 21.13.1 — Independencia de la sentencia PA ya construida {#tlog-cor-00034}

**Corolario.** La sentencia $\mathcal G_{PA}$ de CH20 es verdadera en $\mathbb N_A$ y PA no demuestra ni $\mathcal G_{PA}$ ni su negación. PA es, por tanto, incompleta para sentencias.

**Prueba.** Para su representante **original** $Prov_{PA}$, §19.31 proporciona exactamente la definición estándar y la prueba de demostrabilidad de cada teorema concreto que usa §21.10. Corrección PA de §19.6 proporciona consistencia y corrección Σ1. El bicondicional original de §20.23 permanece intacto, así se aplican los dos argumentos anteriores a esa misma sentencia. No se cambia por el representante certificado actual ni se identifica su código con el de una nueva salida del compilador.

La verdad y consistencia de PA aquí se derivan externamente en ZF, donde se construyó el modelo estándar. No se está dando una prueba PA de su propia consistencia ni afirmando consistencia de ZF objeto. $\square$

## 21.14. Clase Π1 y normalización del auxiliar universal

### Lema 21.14.1 — Clase Π1 y normalización del auxiliar universal {#tlog-lem-00088}

**Definición y lema.** Llamamos Π1 a una fórmula de la forma $\forall u_0\cdots\forall u_{k-1}\delta$ con δ∈Δ0 y k finito, incluyendo0. Si $\Theta(x,y)=\exists\bar a\,\theta(x,y,\bar a)$ y $V(y)=\exists\bar b\,\pi(y,\bar b)$ son Σ1 con matrices Δ0, con todos los auxiliares ligados higienizados y distintos, entonces PA prueba
$$
\forall y(\Theta(x,y)\to\neg V(y))\leftrightarrow
\forall y\forall\bar a\forall\bar b\ \neg(\theta(x,y,\bar a)\land\pi(y,\bar b)).\tag{U}
$$
El lado derecho es literalmente Π1 antes de expandir las abreviaturas acotadas de sus matrices.

**Prueba.** $E\to\neg F$ equivale proposicionalmente a ¬(E∧F). Cuando las variables de los prefijos existenciales no aparecen libres en la otra matriz, $(\exists\bar a\theta)\land(\exists\bar b\pi)$ equivale a $\exists\bar a\exists\bar b(\theta\land\pi)$, mediante introducción/eliminación existencial con testigos frescos. La negación de ese prefijo existencial es el prefijo universal de la matriz negada, por Q5 y lógica clásica. Se conserva el universal y externo, que está fuera de ambos prefijos, y se generaliza x. Estas equivalencias son expansiones finitas HFOL=, no una normalización semántica sin prueba. Δ0 es cerrada bajo conjunción y negación; cotas y sus variables propias se preservan por la higiene.

La sustitución posterior de un numeral cerrado por x conserva esta gramática Π1 y la condición de las cotas: x estaba fuera del conjunto de variables ligadas. $\square$

## 21.15. Elección de una sentencia de Gödel literalmente Π1

### Metateorema 21.15.1 — Elección de una sentencia de Gödel literalmente Π1 {#tlog-mth-00121}

**Metateorema.** Para cada presentación admisible puede construirse una sentencia $G_T^{\Pi}$ literalmente Π1 con una prueba PA de $G_T^{\Pi}\leftrightarrow\neg V_T(\ulcorner G_T^{\Pi}\urcorner)$. Bajo consistencia es verdadera y no demostrable en T; bajo ω-consistencia o corrección Σ1 es independiente.

**Construcción y prueba.** Elegimos x=xi e y frescos. Tomamos el representante Σ1 $\Theta_i(x,y)$ de $D_i$ y V_T(y), higienizados como en §21.14. Construimos como árbol auxiliar B(x) **el lado derecho** de (U), y sólo entonces calculamos p=G(B) y $G_T^{\Pi}=B[\bar p/x]$. El árbol final es Π1 por el lema anterior. Por definición literal, $D_i(p)=G(G_T^{\Pi})=d$.

La equivalencia (U), particularizada en \bar p, identifica la sentencia final con $\forall y(\Theta_i(\bar p,y)\to\neg V_T(y))$. La representación numeral $R_i(p)$ y la forma universal del lema de testigo dan equivalencia PA con ¬V_T(\bar d). Se obtiene el bicondicional de Gödel, y los argumentos de §§21.10–12 se aplican sin cambio. Todas las normalizaciones se hicieron **antes** de fijar el código auxiliar; no se reemplaza después G_T por una fórmula equivalente conservando indebidamente su código.

La elección $G_T^{\Pi}$ puede diferir de G_T y de la sentencia PA de CH20. No se reclama que la sentencia de Rosser de §21.17 tenga esta misma clase literal: su predicado de prueba certificado es Σ1, y se conservará la complejidad que resulta de su construcción. $\square$

## 21.16. Una extensión consistente que demuestra una falsedad Σ1

### Proposición 21.16.1 — Una extensión consistente que demuestra una falsedad Σ1 {#tlog-pro-00135}

**Proposición.** La teoría $S=\mathrm{PA}+\neg\mathcal G_{PA}$ es una extensión efectiva consistente de PA, pero es incorrecta en la estructura estándar, no es Σ1-correcta y es ω-inconsistente. No se afirma que su sentencia de Gödel propia sea $\mathcal G_{PA}$.

**Consistencia.** Si una derivación S de ⊥ existiera, las finitísimas apariciones de prefijos universales del axioma cerrado ¬G se reemplazarían por sus derivaciones desde ¬G usando Q4. El teorema de deducción sobre PA daría $\mathrm{PA}\vdash\neg\mathcal G_{PA}\to\bot$. PA refuta ⊥, por lo que lógica clásica daría $\mathrm{PA}\vdash\mathcal G_{PA}$, contra §21.13. Por tanto S es consistente.

**Falsedad Σ1.** S prueba ¬G por su axioma, y el bicondicional PA da $S\vdash Prov_{PA}(\ulcorner G\urcorner)$. Esta sentencia Σ1 es falsa estándar, porque PA no prueba G. Para cada d estándar, el verificador original PA rechaza una pretendida prueba de G, de modo que PA y S prueban $\neg Prf_{PA}(\bar d,\ulcorner G\urcorner)$. S prueba la existencia de d y niega todas las instancias numerales: es ω-inconsistente. Además su axioma ¬G es falso estándar. La presentación de S añade una sentencia concreta y sus prefijos a PA; es decidible por comparación y retirada finita de prefijos.

El ejemplo muestra por qué se declaran hipótesis diferentes. No es un contraejemplo a Rosser: Rosser construirá otra sentencia para **S**, independiente bajo su consistencia simple. Tampoco una prueba en S de «PA demuestra G» es una prueba real PA de G. $\square$

## 21.17. La sentencia de Rosser y el orden de certificados

### Definición 21.17.1 — La sentencia de Rosser y el orden de certificados {#tlog-def-00153}

Para la misma presentación y los predicados P,N fijamos el objetivo
$$
A_T(z)=\forall d\bigl(P_T(d,z)\to\exists e(e\le d\land N_T(e,z))\bigr).
$$
Construimos su sentencia fija R_T, con r=G(R_T), y una prueba PA de
$$
R_T\leftrightarrow\forall d\bigl(P_T(d,\bar r)\to\exists e(e\le d\land N_T(e,\bar r))\bigr).\tag{R}
$$
Los ligadores de los representantes se higienizan antes de insertar las variables d,e,z. El símbolo ≤ es la abreviatura aritmética de CH19. El orden compara **naturales que codifican pruebas certificadas**, no longitudes de las derivaciones, complejidad de algoritmos o tiempos de ejecución.

Usamos e≤d de manera fija. En la dirección positiva habrá que excluir pruebas negativas hasta p **inclusive**; en la dirección negativa se excluirán pruebas positivas estrictamente menores que n, y el certificado negativo n servirá para todo d≥n. No se cambia ≤ por < a mitad de la prueba.

La fórmula objetivo tiene sólo z libre. El lema diagonal entrega una sentencia aritmética y su bicondicional; no se afirma que R_T sea literalmente Π1 ni que P/N sean Δ0. La representación bilateral en numerales y los cortes finitos serán suficientes.

## 21.18. Primera mitad de Rosser: no hay prueba positiva

### Lema 21.18.1 — Primera mitad de Rosser: no hay prueba positiva {#tlog-lem-00089}

**Lema.** Si T es consistente y tiene presentación admisible, $T\nvdash R_T$.

**Prueba.** Supongamos una prueba T de R_T y tomemos un certificado externo p. Consistencia excluye toda prueba T de ¬R_T, por tanto cada $C_T^-(e,r)$ es falso. Para los finitísimos e≤p, representación bilateral da pruebas PA de $\neg N_T(\bar e,\bar r)$; el lema de corte da
$$
\mathrm{PA}\vdash\forall e(e\le\bar p\to\neg N_T(e,\bar r)).\tag{1}
$$
El certificado p da $\mathrm{PA}\vdash P_T(\bar p,\bar r)$. En T, la prueba supuesta de R_T y (R), particularizada en d=\bar p, producen $T\vdash\exists e(e\le\bar p\land N_T(e,\bar r))$. Pero (1), que también es teorema T, niega esa existencia por lógica de cuantificadores. T tiene una contradicción.

No se exige el menor certificado p, sólo uno concreto. No se ha generalizado sobre todos los e a partir de sus instancias: se ha construido una prueba para el segmento numeral **finito** e≤p. La prueba vale para P,N de complejidad Σ1 arbitraria con las propiedades numerales indicadas. $\square$

## 21.19. Segunda mitad de Rosser: una prueba negativa fuerza una positiva

### Lema 21.19.1 — Segunda mitad de Rosser: una prueba negativa fuerza una positiva {#tlog-lem-00090}

**Lema.** Bajo las mismas hipótesis, una supuesta prueba T de ¬R_T permitiría construir una prueba **PA** de R_T; por tanto tal prueba negativa no existe.

**Prueba.** Tomemos su certificado externo n. El lema anterior excluye todas las pruebas T de R_T, así para cada d<n PA prueba $\neg P_T(\bar d,\bar r)$. El corte finito y el certificado negativo n dan
$$
\mathrm{PA}\vdash\forall d(d<\bar n\to\neg P_T(d,\bar r)),\qquad
\mathrm{PA}\vdash N_T(\bar n,\bar r).\tag{2}
$$
Ahora trabajamos **dentro de PA** con d arbitrario. PA prueba $d<\bar n\lor\bar n\le d$ por orden lineal. En la primera rama, (2) refuta P_T(d,\bar r), así la implicación de (R) es verdadera por lógica. En la segunda, $N_T(\bar n,\bar r)$ y \bar n≤d proporcionan el testigo e=\bar n de $\exists e(e\le d\land N_T(e,\bar r))$, independientemente de P. En ambas ramas se prueba
$$
P_T(d,\bar r)\to\exists e(e\le d\land N_T(e,\bar r)).
$$
Se generaliza d y se usa la dirección hacia R_T del bicondicional PA. Resulta $\mathrm{PA}\vdash R_T$, luego T prueba R_T además de la negación supuesta, contra consistencia. Con n=0 el segmento d<n es vacío y basta la segunda rama, pues PA prueba0≤d. No hay un test sobre todos los certificados posibles ni una apelación a corrección T. $\square$

## 21.20. Primer teorema de incompletitud en forma de Gödel–Rosser

### Metateorema 21.20.1 — Primer teorema de incompletitud en forma de Gödel–Rosser {#tlog-mth-00122}

**Metateorema.** Toda extensión T de PA en $L_A$ con una presentación semidecidible de axiomas como §21.2, si es consistente, tiene una sentencia R_T tal que
$$
T\nvdash R_T,\qquad T\nvdash\neg R_T,
\qquad\mathbb N_A\models R_T.
$$
En particular T no es completa para sentencias. No se requieren ω-consistencia, corrección Σ1 o corrección estándar de T.

**Prueba.** Los dos lemas anteriores excluyen ambas pruebas usando sólo consistencia y la representación bilateral PA de los verificadores. Como no existe prueba T de R_T, P_T(d,\bar r) es falso en la estructura estándar para todo d. El lado derecho de (R) es entonces verdadero allí. Su bicondicional tiene prueba PA, de modo que corrección PA da la verdad de R_T. Finalmente una sentencia sin ninguna de las dos pruebas contradice la definición de completitud.

Esta verdad se demuestra externamente. T puede ser incorrecta en otras sentencias sin afectar el argumento. El predicado certificado permite la misma conclusión cuando los axiomas originales sólo son semidecidibles; no se ha fingido un decidor de esas pertenencias negativas. No se generaliza el teorema a teorías arbitrarias sin presentación efectiva ni a ZF objeto sin interpretación declarada. $\square$

## 21.21. Aplicación a PA y a sus extensiones efectivas consistentes

### Corolario 21.21.1 — Aplicación a PA y a sus extensiones efectivas consistentes {#tlog-cor-00035}

**Corolario.** PA tiene una sentencia de Rosser verdadera e independiente, y ninguna extensión consistente de PA obtenida por un conjunto decidible o semidecidible de axiomas cerrados puede ser completa para sentencias.

**Prueba.** PA es efectiva y consistente por CH19; se usa Γ vacío o su presentación decidible propia. En una extensión con Γ decidible, su decidor se transforma en un semidecidor que para sólo en los éxitos, por CH17, y se aplica el teorema. Para Γ semidecidible la hipótesis ya tiene la forma requerida. También aplica al S consistente de §21.16, aunque S demuestre una falsedad Σ1.

La base aprobada en el tratado es PA. La extensión de este enunciado a Robinson Q requeriría verificar que las instancias de representación y cortes finitos usados se derivan en Q; no se reclama a partir de fuentes externas que trabajan con otra base. $\square$

## 21.22. Construcción uniforme externa de una sentencia independiente

### Metateorema 21.22.1 — Construcción uniforme externa de una sentencia independiente {#tlog-mth-00123}

**Metateorema.** A partir del código de un programa RM de un argumento se puede construir efectivamente la presentación de §21.2, los representantes P,N,V, una sentencia R_T y una prueba PA de su bicondicional. Sobre códigos de programas válidos, estas construcciones terminan sin comprobar consistencia. Si la teoría presentada es consistente, la sentencia obtenida es independiente y verdadera.

**Prueba.** La guarda de sentencia restringe el dominio de parada del programa dado a Γ⊆Sent(L_A). Se genera el semidecidor de prefijos/axiomas PA y el verificador certificado de CH18. Este último es un programa **total**, aunque el semidecidor inicial diverja en algunas entradas. Se compone el verificador negativo con el constructor de ¬A. El compilador de representación de CH19 produce las fórmulas P,N; las operaciones de árbol construyen V y el objetivo Rosser, con nombres frescos. El compilador de CH20 produce R_T y la búsqueda de pruebas de su bicondicional termina porque esa equivalencia es siempre un teorema PA.

Todos los compiladores recorren objetos finitos y los programas de origen sólo se **codifican** en esta construcción, no se ejecutan hasta resolver sus entradas negativas. La única ejecución de búsqueda de pruebas busca una equivalencia cuya existencia se demostró sin consistencia de T. Para un código malformado de programa se devuelve0 antes de construir, con una etiqueta externa de rechazo cuando se entregan varios campos.

La garantía de independencia es condicional. El procedimiento no es un decidor de consistencia y no suministra una prueba T de la afirmación «mi salida es independiente». La finitud de los numerales no constituye una cota práctica de tiempo o tamaño. $\square$

## 21.23. Añadir uno de los lados de una sentencia independiente

### Lema 21.23.1 — Añadir uno de los lados de una sentencia independiente {#tlog-lem-00091}

**Lema.** Si T es consistente y A es independiente en T, tanto T+A como T+¬A son consistentes. Si A es una sentencia y la presentación de T es admisible, ambas extensiones tienen presentaciones admisibles efectivamente construibles.

**Prueba de consistencia.** Si T+A probara ⊥, reemplazamos los prefijos del axioma cerrado A por las derivaciones desde A mediante Q4 y aplicamos deducción al cálculo T: $T\vdash A\to\bot$, luego $T\vdash\neg A$ porque T refuta ⊥. Contradice independencia. Si T+¬A probara ⊥, deducción y lógica clásica darían $T\vdash A$, otra contradicción.

**Efectividad.** Al semidecidor inicial se agrega una rama que compara el código con G(A), o con G(¬A), y para al coincidir; las otras entradas siguen el semidecidor previo. La clausura de prefijos se genera como §21.2. Las comparaciones y el árbol de negación son totales. No se ha decidido efectivamente si A es independiente: el lema recibe esa propiedad como hipótesis matemática. $\square$

## 21.24. Una reparación finita no elimina la incompletitud

### Proposición 21.24.1 — Una reparación finita no elimina la incompletitud {#tlog-pro-00136}

**Proposición.** Añadir una sentencia de Rosser a una teoría admisible consistente conserva consistencia y efectividad, pero la teoría nueva tiene otra sentencia independiente. Lo mismo ocurre si se añade su negación o cualquier lista finita de sentencias que deje consistente la extensión.

**Prueba.** Para R_T y ¬R_T se aplica §21.23. La teoría resultante vuelve a cumplir las hipótesis de Gödel–Rosser, así tiene su propio punto fijo R_{T'}, relativo a **su propio verificador**. En T' se demuestra el lado añadido, por lo que ese árbol no puede ser independiente allí. No se identifica R_{T'} con R_T ni se reutiliza sin cambio el predicado V_T como si verificara todos los nuevos teoremas.

Para cualquier lista finita consistente, el semidecidor admite una disyunción finita de comparaciones y el teorema vuelve a aplicar. El argumento no afirma que añadir arbitrariamente un axioma preserve consistencia: ésta se recibe como hipótesis o se prueba mediante independencia. $\square$

## 21.25. Árbol binario de extensiones y uniones de ramas

### Metateorema 21.25.1 — Árbol binario de extensiones y uniones de ramas {#tlog-mth-00124}

**Metateorema.** Desde una teoría admisible consistente T puede construirse externamente un árbol binario de teorías consistentes $T_s$, indexado por cadenas binarias finitas: $T_{\varnothing}=T$, y los dos sucesores de s añaden respectivamente R_{T_s} y ¬R_{T_s}. Para cada rama externa $b:\omega\to\{0,1\}$, la unión de sus axiomas es consistente. Si b es computable-RM, esa unión admite una presentación semidecidible y sigue siendo incompleta.

**Prueba finita.** Por inducción externa sobre |s|, el constructor uniforme entrega la sentencia de Rosser de T_s. Los dos lados son independientes y el lema de extensión da consistencia de ambos sucesores. Sus programas se generan efectivamente a partir del programa padre y el lado elegido. El árbol de cada nivel finito se construye por recursión finita; no se usa AC/BPI.

**Unión de una rama dada.** Una prueba de contradicción en la unión usa finitísimos axiomas de la rama. Cada axioma añadido tiene un índice de etapa concreto; se toma el máximo de esos finitísimos índices y se sitúa toda la prueba en esa etapa, que es consistente. Los axiomas iniciales permanecen en todas las etapas. Por finitariedad no hay contradicción en la unión. b se da como función externa: no se elige una rama por un principio de compactación o elección.

**Rama computable.** Para entrada c, intercalamos el semidecidor inicial Γ(c) con la generación de etapas de la rama. Se calculan sucesivamente b(n), la presentación de T_n y su siguiente sentencia elegida, comparando c con su código. Cada etapa termina; si c pertenece a la unión aparecerá en Γ o en una etapa y se acepta. Si no, se continúa. Esto da un semidecidor RM y la unión, ya consistente, vuelve a ser incompleta por §21.20. Para b arbitraria no se afirma semidecidibilidad de la unión. Tampoco esta construcción demuestra que cada rama, incluso una no efectiva, sea completa. $\square$

## 21.26. La teoría externa de todas las verdades aritméticas

### Definición 21.26.1 — La teoría externa de todas las verdades aritméticas {#tlog-def-00154}

Definimos externamente
$$
\operatorname{Th}(\mathbb N_A)=\{A:\ A\text{ sentencia de }L_A\ \land\ \mathbb N_A\models A\}.
$$
Es un conjunto de árboles finitos en ZF externa: las fórmulas forman un conjunto, la satisfacción para la estructura fijada se define por recursión sobre árboles y separación selecciona las sentencias verdaderas. El conjunto de sus códigos se obtiene mediante G. No se define un predicado uniforme de verdad **dentro de PA**.

Como teoría que toma todas estas sentencias por axiomas, contiene deductivamente a PA: para cada axioma PA abierto, su clausura universal es una sentencia verdadera y las particularizaciones seguras recuperan el axioma. Es consistente por corrección externa y completa para sentencias por bivalencia clásica de satisfacción. Una sentencia falsa no se deriva de sus axiomas verdaderos, y toda sentencia verdadera se deriva en una línea axiomática. Esta construcción es externa y no suministra una enumeración computable de su conjunto de axiomas.

## 21.27. La verdad completa no tiene una axiomatización semidecidible

### Corolario 21.27.1 — La verdad completa no tiene una axiomatización semidecidible {#tlog-cor-00036}

**Corolario.** No hay conjunto semidecidible-RM Γ de sentencias tal que los teoremas de PA+Γ sean exactamente $\operatorname{Th}(\mathbb N_A)$.

**Prueba.** Si existiera Γ, PA+Γ tendría una presentación admisible, sería consistente porque todos sus teoremas serían verdaderos y sería completa para sentencias. Gödel–Rosser produciría una sentencia sin ninguna de sus dos pruebas, contradiciendo esa completitud. Por tanto una teoría completa y consistente de todas las verdades existe externamente, pero no tiene esa clase de presentación efectiva.

El resultado concierne a axiomatización semidecidible. No es todavía una prueba de indefinibilidad de verdad en el lenguaje aritmético, ni una reducción algorítmica a un problema de parada. Esas afirmaciones requieren sus propios argumentos. $\square$

## 21.28. Cuadro de hipótesis y alcance de las conclusiones

### Proposición 21.28.1 — Cuadro de hipótesis y alcance de las conclusiones {#tlog-pro-00137}

**Proposición de síntesis.** Bajo presentación admisible, el cuadro siguiente conserva exactamente las hipótesis demostradas:

| Hipótesis sobre T | Sentencia | No demostrable | No refutable | Verdad estándar |
|---|---|---|---|---|
| Consistencia | G_T o $G_T^{\Pi}$ | sí | no deducido de esa hipótesis en el argumento de Gödel | sí |
| ω-consistencia | G_T o $G_T^{\Pi}$ | sí | sí | sí |
| Corrección Σ1 | G_T o $G_T^{\Pi}$ | sí | sí | sí |
| Consistencia | R_T | sí | sí | sí |
| PA, con su corrección externa probada | $\mathcal G_{PA}$ de CH20 | sí | sí | sí |

**Prueba.** Las filas son los resultados de §§21.10–15 y21.20. El ejemplo S de §21.16 prueba que una extensión consistente puede ser Σ1-incorrecta y ω-inconsistente; no se emplea para afirmar que refuta su propia G_S. La distinción entre G_PA y G_S depende de qué teoría verifica el predicado. Las afirmaciones de verdad son externas; ninguna fila autoriza reflexión T uniforme ni una prueba T de la ausencia de sus propias derivaciones. $\square$

## 21.29. Tres obligaciones de derivabilidad para el capítulo siguiente

### Definición 21.29.1 — Tres obligaciones de derivabilidad para el capítulo siguiente {#tlog-def-00155}

Para un representante concreto $V_T$ se distinguen estas obligaciones, que **no** se añaden como axiomas:

1. D1 externa: si T⊢A, entonces T⊢V_T(\ulcorner A\urcorner). En este capítulo se demostró incluso una prueba PA de la instancia, por certificación y representación.
2. D2 interna, para sentencias A,B concretas: T debe demostrar $V_T(\ulcorner A\to B\urcorner)\to(V_T(\ulcorner A\urcorner)\to V_T(\ulcorner B\urcorner))$.
3. D3 interna, para A concreta: T debe demostrar $V_T(\ulcorner A\urcorner)\to V_T(\ulcorner V_T(\ulcorner A\urcorner)\urcorner)$.

En D3 las comillas exteriores nombran el árbol de la **instancia** de V_T en el numeral del código de A. No nombran el árbol abierto V_T ni vuelven a nombrar A. Todas las expansiones y variables frescas deben fijarse antes de calcular esos códigos.

D1 es una implicación metateórica entre pruebas concretas. D2 y D3 son fórmulas objeto demostrables que necesitan argumentos adicionales de composición y aritmetización de pruebas. La exactitud estándar de V y su representación débil en PA no las sustituyen. El contrato CH22 debe fijar qué representante satisface cada obligación; el $Prov_{PA}$ original y la variante certificada no se intercambian silenciosamente.

## 21.30. Lo que el primer teorema no demuestra sobre consistencia interna

### Proposición 21.30.1 — Lo que el primer teorema no demuestra sobre consistencia interna {#tlog-pro-00138}

**Proposición.** Los argumentos de este capítulo no proporcionan por sí solos el segundo teorema de incompletitud, una fórmula objeto correcta de consistencia o condiciones D2/D3. Sus usos de consistencia son externos y se aplican a certificados estándar concretos.

**Prueba por inspección de dependencias.** En Gödel se toma una prueba concreta de G y se produce una prueba de V(\bar g); en Rosser se toman certificados p o n y se ensamblan cortes numerales finitísimos. La hipótesis «T es consistente» permite excluir pares de pruebas externas. No se ha representado dentro de PA toda esa argumentación con códigos variables, ni probado que T reconozca uniformemente la transformación de todas sus pruebas. En particular, una familia externa de pruebas negativas P(\bar d,\bar g) no da una prueba universal sobre d.

CH22 debe seleccionar un predicado, construir sus condiciones internas y definir la fórmula de consistencia antes de demostrar una nueva conclusión de no demostrabilidad. CH23 conserva las reducciones de indecidibilidad y la frontera con GAS; MRDP/Jones y las interpretaciones en ZF objeto no se incorporan aquí. $\square$

## 21.31. Cierre del primer teorema y contrato de salida

### Corolario 21.31.1 — Cierre del primer teorema y contrato de salida {#tlog-cor-00037}

**Corolario.** CH21 cierra el primer teorema de incompletitud para extensiones efectivas consistentes de PA, incluida la forma Gödel–Rosser bajo consistencia simple, con verificadores certificados, representación numeral, cortes finitos y construcción efectiva de una sentencia independiente. Entrega también la forma original bajo hipótesis más fuertes, una elección Π1 de Gödel, el contraste de una extensión incorrecta consistente y el control de extensiones finitas y ramas computables.

**Prueba.** Los resultados citados reconstruyen cada interfaz de la Parte IV y justifican las hipótesis de las conclusiones. Las codificaciones S/G y los nombres de los representantes permanecen fijados. Ninguna dependencia se dirige a un resultado futuro D2/D3 o al segundo teorema. Las sentencias independientes y la no axiomatizabilidad efectiva de la verdad completa son conclusiones externas bajo las hipótesis indicadas. La Parte V permanece abierta hasta sus capítulos22–23; el cierre humano no declara formalización Lean ni publicación web. $\square$

## 21.32. Ejemplos de uso y cierre

Si una pretendida prueba positiva de R tiene certificado p=2, el argumento Rosser sólo ensambla las tres refutaciones N(0,r), N(1,r), N(2,r). Si una pretendida prueba negativa tiene certificado n=2, se refutan P(0,r), P(1,r), y N(2,r) sirve como testigo para todo d≥2. Éstos son ejemplos de cortes lógicos, no se presentan los números0,1,2 como certificados reales de una sentencia diagonal concreta.

En PA, la sentencia de Gödel ya fijada en CH20 es verdadera e independiente por corrección estándar. En PA+¬G_PA se conserva consistencia, pero se demuestra una falsedad Σ1 acerca de pruebas PA. La sentencia de Rosser de esa nueva teoría vuelve a ser independiente, pues utiliza el verificador de la teoría nueva. Añadir una sentencia verdadera independiente tampoco vuelve completa una extensión efectiva consistente.

El capítulo cierra **31/31 resultados** y **153 aristas directas nuevas**. Acumulado: **592 resultados / 2222 aristas**, sin ciclos/duplicados/huérfanos; **251 candidatos Lean /0 compilados /0 verificados**. ParteIV sigue CLOSED; ParteV OPEN, conCH21 cerrado yCH22–23 pendientes. Partes cerradas4/5; interfaces activas0; capítulos publicados0. Auditoría humana, regresiones de referencia y cotejo de bytes se documentan por separado.

```text
LOCAL  CH21 ████████████████████ 31/31 resultados (100 %)
GLOBAL TLOG ██████████████████████░░ 22/24 capítulos (91,67 %)
```

Próximo capítulo: **CH22 — Segundo teorema de incompletitud**.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 20](capitulo-20.md) · [Capítulo 22 →](capitulo-22.md)


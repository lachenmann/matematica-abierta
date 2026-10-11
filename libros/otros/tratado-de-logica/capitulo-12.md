---
title: Capítulo 12 — El lenguaje de la teoría de conjuntos y los axiomas de ZF
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
content-id: MA-BCH-0214
content-type: book-chapter
source-id: TLOG-CH12-0001
prerequisites:
- MA-BCH-0202
- MA-BCH-0207
- MA-BCH-0208
- MA-BCH-0210
- MA-BCH-0211
- MA-BCH-0212
- MA-BCH-0213
related:
- MA-BOK-0014
source-sha256: 097e4ea7971fbaee89a83b394ff807553ea666a5e05468cf1d9c62bd405cd74b
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 11](capitulo-11.md) · [Capítulo 13 →](capitulo-13.md)

## 12.0. La teoría de conjuntos como objeto formal

La Parte II ha definido de modo autónomo la sintaxis y la semántica de $\mathrm{FOL}_{=}$, así como el cálculo deductivo $\mathsf H_\tau^{=}$. La Parte III construye a partir de ellos la infraestructura conjuntista requerida por el corpus, comenzando por una **teoría objeto de pertenencia**, no por una nueva metateoría tácita. El contrato es estricto:

$$
\boxed{\mathsf M_{\mathrm{ext}}=\mathrm{ZF}\text{ clásica (sin AC)}\qquad\neq\qquad\mathsf{ZF}_{\mathrm{obj}}=(\tau_\in,\operatorname{Ax}_{\mathsf{ZF}}).}
$$

En particular, las expresiones $\{a,b\}$, $\varnothing$, $\bigcup a$, $\mathcal P(a)$ no se tomarán inicialmente como términos del lenguaje puro. Todos los axiomas se escriben primero usando únicamente $\in$, igualdad y la gramática lógica de los capítulos 5–6. Las abreviaciones editoriales se justifican por expansión y se introducen sólo cuando su existencia y unicidad son legítimas.

**Procedencia y alcance:** `TLOG-SRC-0002` (Enderton) y `TLOG-SRC-0003` (Rautenberg) conservan su papel previo de fundamentos lógico-formales. `TLOG-SRC-00011`, suplemento «Zermelo–Fraenkel Set Theory (ZF)» de *Stanford Encyclopedia of Philosophy*, se coteja en línea para las **familias de axiomas** (extensionalidad, pares, infinito, separación, reemplazo y regularidad). Los esquemas y derivaciones que siguen están reconstruidos específicamente para la firma primitiva y el cálculo HFOL= de TLOG. **No se atribuye una lectura integral de un libro adicional ni una prueba importada**.


## 12.1. Separación estricta de ZF metateórica y ZF objeto

### Convención 12.1.1 — Separación estricta de ZF metateórica y ZF objeto {#tlog-cnv-00014}

La notación $\mathsf M_{\mathrm{ext}}$ significa la **metateoría externa** ZF clásica sin AC ni BPI incorporados. $\mathsf{ZF}_{\mathrm{obj}}$ designa una **teoría formal de sentencias**, presentada más abajo mediante una signatura y un conjunto explícito de axiomas. No se trata de dos nombres del mismo objeto: la primera es el marco de razonamiento; la segunda es un conjunto de árboles sintácticos construido dentro de ese marco.

Toda invocación de un axioma de $\mathsf{ZF}_{\mathrm{obj}}$ en una demostración se indica como un paso de **deducción objeto**, $\operatorname{Ax}_{\mathsf{ZF}}\vdash_{\mathsf H_{\tau_\in}^{=}}\theta$. No se inferirá por ello que $\mathsf{ZF}_{\mathrm{obj}}$ tiene un modelo, es consistente o posee un universo de todos los conjuntos como *conjunto*. Los hechos sobre códigos, relaciones y sucesiones en el presente desarrollo pertenecen a $\mathsf M_{\mathrm{ext}}$. No se efectúa una sustitución encubierta de BPI por el axioma de elección.

## 12.2. Signatura pura de pertenencia

### Definición 12.2.1 — Signatura pura de pertenencia {#tlog-def-00060}

Definimos la signatura extralógica unisortada $\tau_\in$ por

$$
F_n=\varnothing\quad(n\in\omega),\qquad R_2=\{\dot\in\},\qquad R_n=\varnothing\quad(n\ne2).
$$

$\dot\in$ es un **único símbolo relacional binario de objeto**; imprimiremos $x\mathbin\in y$, sin identificarlo con la relación de pertenencia de la metateoría. $x\doteq y$ continúa siendo **igualdad lógica primitiva**, no un segundo símbolo relacional extralógico. No hay constantes, funciones, símbolos de clase, cuantificador de clase ni predicados de verdad primitivos. Los términos $\operatorname{Tm}_{\tau_\in}$ son exactamente variables individuales $X$: por ausencia de símbolos funcionales no se generan términos compuestos. Las fórmulas $\operatorname{Fm}_{\tau_\in}$ y sentencias $\operatorname{Sent}_{\tau_\in}$ son las del Capítulo 5 con cinco conectivos y $\forall,\exists$ primitivos.

El texto formal mantendrá $u\in v$ para el átomo $\dot\in(u,v)$; dentro de una demostración **sobre** el sistema utilizaremos $a\mathrel{\in_{\mathrm{meta}}}b$ cuando sea necesario desambiguar. Las estructuras objeto son conjuntos no vacíos acompañados por una relación binaria que **no tiene por qué coincidir** con la pertenencia externa.

## 12.3. Abreviaciones conservativas y normalización de vinculantes

### Definición 12.3.1 — Abreviaciones conservativas y normalización de vinculantes {#tlog-def-00061}

En el lenguaje objeto se permiten las siguientes **macroabreviaciones puramente sintácticas**, siempre expandidas a fórmulas con los constructores primitivos:

$$
\begin{aligned}
a\notin b&:\equiv\neg(a\in b),\\
a\subseteq b&:\equiv\forall u\,(u\in a\to u\in b),\\
\forall u\in a\,\psi&:\equiv\forall u\,(u\in a\to\psi),\\
\exists u\in a\,\psi&:\equiv\exists u\,(u\in a\land\psi),\\
\exists!u\,\psi(u)&:\equiv\exists u\,[\psi(u)\land\forall v(\psi(v)\to v\doteq u)].
\end{aligned}
$$

La variable auxiliar $u$ de $a\subseteq b$ se elige fresca respecto de ambos argumentos; la de unicidad $v$ es fresca respecto del contexto. Las ocurrencias de $\psi(v)$ significan sustitución de **las ocurrencias libres designadas** de $u$, después de un renombrado alfa que impida captura. Por §6.29 la elección de nombres no altera las propiedades semánticas ni deductivas pertinentes. $\bar p=(p_1,\ldots,p_k)$ denota sólo un **bloque finito de variables distintas**, y $\forall\bar p$ significa un prefijo finito de cuantificadores universales; para $k=0$ es vacío.

Las expresiones $\varnothing$, $\{a,b\}$, $\bigcup a$, $\mathcal P(a)$ y $\omega$ **no son aún términos del lenguaje objeto**: su introducción como definiciones conservativas estará justificada en su debido lugar; únicamente $\varnothing$ será habilitada parcialmente por la prueba de §12.15.

## 12.4. Axioma de extensionalidad

### Axioma 12.4.1 — Axioma de extensionalidad {#tlog-axm-00005}

El axioma es la sentencia del lenguaje de pertenencia

$$
\boxed{\forall a\forall b\,\Bigl[\bigl(\forall u\,(u\in a\leftrightarrow u\in b)\bigr)\to a\doteq b\Bigr].}
$$

Afirma identidad de objetos cuando tienen exactamente los mismos miembros. La implicación inversa se deduce de las reglas lógicas de igualdad y no se incorpora como un segundo axioma. En este lugar **no** se introduce una definición de igualdad por pertenencia: la igualdad sigue siendo lógica. Se trata de una única sentencia, no de un esquema paramétrico.

## 12.5. Axioma de pares

### Axioma 12.5.1 — Axioma de pares {#tlog-axm-00006}

Se adopta la siguiente sentencia cerrada:

$$
\boxed{\forall a\forall b\exists c\forall u\,[u\in c\leftrightarrow(u\doteq a\lor u\doteq b)].}
$$

La existencia del objeto con exactamente los dos miembros prescritos es axiomática; su **unicidad** requerirá el axioma de extensionalidad. Se permite $a\doteq b$, caso que posteriormente fundamentará el singleton. No se emplea $\{a,b\}$ en el **enunciado formal**, para evitar presuponer la construcción que precisamente se axiomatiza.

## 12.6. Axioma de unión

### Axioma 12.6.1 — Axioma de unión {#tlog-axm-00007}

La sentencia de unión es

$$
\boxed{\forall a\exists b\forall u\,[u\in b\leftrightarrow\exists v\,(v\in a\land u\in v)].}
$$

$b$ contiene precisamente los miembros de miembros de $a$. Ni la existencia de un supuesto operador primitivo de unión ni un axioma de unión binaria se introducen subrepticiamente. La construcción $\bigcup a$ y su carácter único se desarrollarán desde extensionalidad en el Capítulo 13.

## 12.7. Axioma del conjunto potencia

### Axioma 12.7.1 — Axioma del conjunto potencia {#tlog-axm-00008}

La sentencia es

$$
\boxed{\forall a\exists b\forall u\,[u\in b\leftrightarrow\forall v\,(v\in u\to v\in a)].}
$$

La expresión interior a la derecha es la expansión de $u\subseteq a$, sin símbolo relacional primitivo nuevo. $b$ agrupa exactamente los subconjuntos de $a$. La notación $\mathcal P(a)$ queda diferida a la prueba de unicidad correspondiente.

## 12.8. Axioma del infinito en lenguaje primitivo

### Axioma 12.8.1 — Axioma del infinito en lenguaje primitivo {#tlog-axm-00009}

Para no anticipar $\varnothing$, singletons o sucesores, fijamos **literalmente** la sentencia

$$
\boxed{\begin{aligned}
\exists I\,\Bigl[&\exists e\,(e\in I\land\forall u\,\neg(u\in e))\\
&\land\forall a\,\bigl(a\in I\to\exists b\,(b\in I\\
&\qquad\land\forall u\,[u\in b\leftrightarrow(u\in a\lor u\doteq a)])\bigr)\Bigr].
\end{aligned}}
$$

El primer testigo es un miembro sin elementos; para cada miembro $a\in I$ existe en $I$ un miembro $b$ caracterizado extensionalmente por «elementos de $a$, más $a$». El enunciado expresa la habitual clausura bajo sucesor de von Neumann, pero **no emplea aún $a\cup\{a\}$** como término. Tras derivar existencia y unicidad de los conjuntos involucrados, recuperaremos la forma abreviada familiar. No se usa una noción previa de «conjunto infinito» para definir el axioma.

## 12.9. Esquema de separación con parámetros

### Esquema axiomático 12.9.1 — Esquema de separación con parámetros {#tlog-axm-00010}

Sea $\theta(u,a,\bar p)\in\operatorname{Fm}_{\tau_\in}$ una fórmula cualquiera cuyas variables libres están entre $u,a,p_1,\dots,p_k$. Exigimos que $u,a,p_i$ sean distintos y que el testigo $b$ **no esté libre** en $\theta$; si un nombre auxiliar aparece ligado en $\theta$, renombramos la fórmula alfa antes de construir la instancia. La instancia de **separación** es la sentencia

$$
\boxed{\operatorname{Sep}_{\theta}:\quad
\forall\bar p\forall a\exists b\forall u\,[u\in b\leftrightarrow(u\in a\land\theta(u,a,\bar p))].}
$$

La notación $\operatorname{Sep}_\theta$ nombra *metateóricamente* el árbol de fórmula resultante. Por cada fórmula $\theta$ se obtiene **una sentencia**, no una cuantificación objeto sobre $\theta$. El nombre $a$ puede figurar libre dentro del esquema original y es entonces cuantificado en la instancia; esto permite condiciones de separación que dependen también del conjunto de partida. En las pruebas se usa como caso $\theta(u)\equiv\neg(u\in u)$. Separación sólo forma un subconjunto de un conjunto $a$ ya dado; **no** afirma comprensión irrestricta.

## 12.10. Esquema de reemplazo funcional sobre conjuntos

### Esquema axiomático 12.10.1 — Esquema de reemplazo funcional sobre conjuntos {#tlog-axm-00011}

Sea $\rho(u,v,a,\bar p)\in\operatorname{Fm}_{\tau_\in}$ una fórmula arbitraria con variables libres entre $u,v,a,p_1,\ldots,p_k$. Los nombres $u,v,a,p_i$ son distintos; $b$, el testigo del conjunto imagen, se elige fresco respecto del soporte libre de $\rho$; se normaliza cualquier colisión ligada mediante equivalencia alfa. La instancia **restringida al dominio** de reemplazo es la sentencia

$$
\boxed{\begin{aligned}
\operatorname{Rep}_{\rho}:\quad\forall\bar p\forall a\,\Bigl[&\bigl(\forall u\,(u\in a\to\exists!v\,\rho(u,v,a,\bar p))\bigr)\\
&\to\exists b\forall v\,[v\in b\leftrightarrow\exists u\,(u\in a\land\rho(u,v,a,\bar p))]\Bigr].
\end{aligned}}
$$

$\exists!$ se expande según §12.3. El carácter de función es **condicional, sobre el conjunto de partida**; no se exige que $\rho$ defina una aplicación total del universo objeto. Como parte de la especificación de formación, se distinguen las variables $v$ de $\exists!v$ y $\forall v$ por su alcance, y ninguna queda capturada. La imagen es un conjunto aunque no sea subconjunto del dominio original. Esta forma equivale, en presencia de los demás axiomas, a formulaciones corrientes que exigen funcionalidad global; aquí fijamos explícitamente la versión restringida, sin utilizar un operador metateórico de clase como símbolo objeto.

## 12.11. Axioma de fundamentación o regularidad

### Axioma 12.11.1 — Axioma de fundamentación o regularidad {#tlog-axm-00012}

Se adopta la sentencia sin abreviación de vacío:

$$
\boxed{\forall a\,\Bigl[(\exists u\,u\in a)\to
\exists v\,\bigl(v\in a\land\forall w\,(w\in a\to\neg(w\in v))\bigr)\Bigr].}
$$

Todo objeto con algún miembro posee un miembro $v$ sin intersección de miembros con el objeto inicial: $v$ es $\in$-minimal **dentro de ese conjunto**. No se infiere de aquí que la relación de pertenencia sea un buen orden lineal del universo ni que cada clase propia tenga elemento mínimo. Esta sentencia, junto con pares, permitirá probar $\forall x\neg(x\in x)$ en §12.17.

## 12.12. Conjunto de axiomas objeto de ZF

### Definición 12.12.1 — Conjunto de axiomas objeto de ZF {#tlog-def-00062}

Definimos, en $\mathsf M_{\mathrm{ext}}$, el conjunto de **sentencias objeto**

$$
\boxed{\operatorname{Ax}_{\mathsf{ZF}}:=\{\operatorname{Ext},\operatorname{Pair},\operatorname{Union},\operatorname{Power},\operatorname{Inf},\operatorname{Reg}\}\cup\{\operatorname{Sep}_{\theta}:\theta\in\operatorname{Fm}_{\tau_\in}\}\cup\{\operatorname{Rep}_{\rho}:\rho\in\operatorname{Fm}_{\tau_\in}\}.}
$$

En las dos últimas familias se incluyen sólo instancias **bien tipadas** en los esquemas de §§12.9–12.10; las fórmulas originales se renombran y sus parámetros se cierran universalmente. Extensionalidad, pares, unión, potencia, infinito y regularidad son **seis** sentencias individuales; separación y reemplazo son **dos** esquemas. El nombre $\operatorname{Ax}_{\mathsf{ZF}}$ se refiere a este conjunto explícito, no al poder de deducción de la metateoría ni a una clase de todos los modelos.

No hay en el conjunto un axioma de elección $\mathsf{AC}$, el principio BPI ni axiomas que cuantifiquen sobre clases. La prueba de §12.13 justifica además que $\operatorname{Ax}_{\mathsf{ZF}}$ es un **conjunto numerable de sentencias** en la metateoría.

## 12.13. Conjuntidad y numerabilidad de las instancias de ZF

### Lema 12.13.1 — Conjuntidad y numerabilidad de las instancias de ZF {#tlog-lem-00035}

**Enunciado.** En $\mathsf M_{\mathrm{ext}}$, $\operatorname{Ax}_{\mathsf{ZF}}$ es un conjunto numerable de miembros de $\operatorname{Sent}_{\tau_\in}$; cada instancia está determinada por un código finito de fórmula y su regla fija de cierre de parámetros.

**Demostración.** La signatura $\tau_\in$ consta de un símbolo extralógico; las variables $X$ y los tokens lógicos forman conjuntos explícitamente numerables. Codificamos tokens por naturales distintos, las secuencias finitas por una aplicación inyectiva en $\omega$, y los árboles sintácticos por sus serializaciones parentizadas de legibilidad única (§5.14). De este modo $\operatorname{Fm}_{\tau_\in}\subseteq\omega$ tras una codificación inyectiva. Para una fórmula dada, la elección de las variables de la matriz se hace con las posiciones marcadas y se asignan nombres frescos por **menor código libre**, obteniendo una instancia única por reglas primitivas de formación; las fórmulas inadmisibles se omiten. Separación y reemplazo en la metateoría permiten reunir los gráficos de esas dos operaciones y sus imágenes como **conjuntos** de sentencias. Sus imágenes son numerables porque todo valor recibe el mínimo código de un antecedente; la unión con las seis sentencias aisladas sigue siendo numerable por un etiquetado finito. Cada prefijo universal cierra todas las variables libres designadas y el renombrado previo evita captura, luego los resultados pertenecen a $\operatorname{Sent}_{\tau_\in}$. No se emplean AC, CC, DC ni BPI: una sola codificación explícita gobierna toda la construcción. $\square$

La numerabilidad **de los códigos de las fórmulas** no convierte en decidible el conjunto de teoremas de ZF; no se hace esa afirmación.

## 12.14. Teoría objeto ZF, derivabilidad y satisfacción

### Definición 12.14.1 — Teoría objeto ZF, derivabilidad y satisfacción {#tlog-def-00063}

Definimos $\mathsf{ZF}_{\mathrm{obj}}$ como el **par tipado** formado por el cálculo lógico $\mathsf H_{\tau_\in}^{=}$ y la teoría de premisas $\operatorname{Ax}_{\mathsf{ZF}}$. Para una sentencia $\sigma$:

$$
\begin{aligned}
\mathsf{ZF}_{\mathrm{obj}}\vdash\sigma
&:\Longleftrightarrow
\operatorname{Ax}_{\mathsf{ZF}}\vdash_{\mathsf H_{\tau_\in}^{=}}\sigma,\\
\mathfrak A\models\mathsf{ZF}_{\mathrm{obj}}
&:\Longleftrightarrow\mathfrak A\models_{\tau_\in}\operatorname{Ax}_{\mathsf{ZF}}.
\end{aligned}
$$

La primera es una **relación metateórica de existencia de una prueba finita**; la segunda es una **relación metateórica de satisfacción** de todos los axiomas por una estructura **de conjunto** cuyo dominio puede tener relación de pertenencia no estándar. Ni $\operatorname{Mod}(\mathsf{ZF}_{\mathrm{obj}})$ ni la totalidad de estructuras se afirman conjuntos: son clases definibles. $\mathsf{ZF}_{\mathrm{obj}}$ no es, por definición, $\mathsf M_{\mathrm{ext}}$. Los axiomas de ZF en la metateoría se utilizan para construir esta teoría objeto, no como líneas de prueba dentro de ella, salvo cuando una instancia concreta se incorpore explícitamente a la derivación.

## 12.15. Existencia y unicidad del conjunto vacío en ZF objeto

### Proposición 12.15.1 — Existencia y unicidad del conjunto vacío en ZF objeto {#tlog-pro-00030}

**Enunciado objeto.**

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\exists e\,\bigl[(\forall u\,\neg(u\in e))\land\forall d\,((\forall u\,\neg(u\in d))\to d\doteq e)\bigr].}
$$

**Demostración en $\mathsf H_{\tau_\in}^{=}$ desde los axiomas objeto.** La sentencia de infinito de §12.8 aporta un $I$ y un miembro $e\in I$ con $\forall u\neg(u\in e)$. Supóngase que $d$ también satisface $\forall u\neg(u\in d)$. Para un $u$ arbitrario, ambas proposiciones $u\in d$ y $u\in e$ son falsas, de modo que la lógica proposicional prueba $(u\in d)\leftrightarrow(u\in e)$. Como se razona sin premisas abiertas adicionales, se generaliza sobre $u$, y el axioma de extensionalidad da $d\doteq e$. El cálculo de primer orden obtiene por introducción existencial el enunciado completo. $\square$

**Convención derivada:** después de esta prueba, $\varnothing$ podrá denotar metalingüísticamente el **único** objeto sin elementos, dentro de una derivación o interpretación de ZF. Al ser un símbolo no perteneciente a $\tau_\in$, todo uso formal de $\varnothing$ debe leerse como extensión definicional eliminable mediante su propiedad única; no se añadió una constante primitiva al lenguaje.

## 12.16. Imposibilidad de un conjunto universal: argumento de Russell

### Proposición 12.16.1 — Imposibilidad de un conjunto universal: argumento de Russell {#tlog-pro-00031}

**Enunciado objeto.**

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\neg\exists a\forall u\,(u\in a).}
$$

**Demostración objeto.** Supongamos, para derivar contradicción, que $a$ contiene todos los objetos: $\forall u(u\in a)$. Instanciamos el **esquema de separación** con la fórmula de un parámetro libre $\theta(u,a):=\neg(u\in u)$ (en realidad no depende de $a$). Su sentencia asegura un $r$ tal que

$$
\forall u\,[u\in r\leftrightarrow(u\in a\land\neg(u\in u))].
$$

La particularización universal para $u=r$ es libre de captura y entrega

$$
r\in r\leftrightarrow(r\in a\land\neg(r\in r)).
$$

De la universalidad supuesta resulta $r\in a$, y el bicondicional se reduce a $r\in r\leftrightarrow\neg(r\in r)$. La base clásica proposicional de $\mathsf H_{\tau_\in}^{=}$ deriva contradicción; descargando la suposición por el teorema de deducción se obtiene $\neg\forall u(u\in a)$, y, sin depender de $a$, finalmente $\neg\exists a\forall u(u\in a)$. $\square$

Esta prueba **no usa regularidad**. En particular, la supuesta colección $\{u:u=u\}$ no puede ser un **conjunto objeto**. En un metalenguaje de clases puede hablarse de «universo» $V$ como clase definible; no es una constante objeto ni un conjunto de todos los conjuntos.

## 12.17. La regularidad excluye la autopertenencia

### Proposición 12.17.1 — La regularidad excluye la autopertenencia {#tlog-pro-00032}

**Enunciado objeto.**

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\forall x\,\neg(x\in x).}
$$

**Demostración objeto.** Sea $x$ una variable arbitraria y supóngase $x\in x$. El axioma de pares con las dos entradas iguales proporciona un objeto $s$ con $\forall u\,[u\in s\leftrightarrow(u\doteq x)]$. En particular $x\in s$. Por regularidad aplicada a $s$ obtenemos un miembro $v\in s$ tal que $\forall w\,(w\in s\to\neg(w\in v))$. De $v\in s$ y la propiedad definitoria del par resulta $v\doteq x$. Como $x\in s$, la condición minimal con $w=x$ afirma $\neg(x\in v)$; por sustitución de iguales y $x\in x$, se deduce $x\in v$, contradicción. El teorema de deducción descarga $x\in x$, y la generalización sobre la variable arbitraria concluye. $\square$

Este resultado demuestra la imposibilidad de **ciclos unitarios** en ZF objeto. No es una prueba de que toda clase propia tenga miembro $\in$-minimal ni usa la noción de secuencia infinita de descensos.

## 12.18. Existencia condicional de modelos de ZF objeto

### Metateorema 12.18.1 — Existencia condicional de modelos de ZF objeto {#tlog-mth-00050}

**Enunciado en $\mathsf M_{\mathrm{ext}}$.**

$$
\boxed{\operatorname{Con}(\mathsf{ZF}_{\mathrm{obj}})\quad\Longrightarrow\quad
\exists\mathfrak A\;(\mathfrak A\models\mathsf{ZF}_{\mathrm{obj}}).}
$$

Donde $\operatorname{Con}(\mathsf{ZF}_{\mathrm{obj}})$ abrevia la **ausencia de una derivación finita** de la contradicción sentencial desde $\operatorname{Ax}_{\mathsf{ZF}}$; no es una sentencia ya aritmetizada del lenguaje objeto. La estructura $\mathfrak A$, si existe, es una $\tau_\in$-estructura de **conjunto**.

**Demostración metateórica.** Por §12.13 la signatura pura de pertenencia es finita (en particular numerable) y $\operatorname{Ax}_{\mathsf{ZF}}$ es un conjunto numerable de sentencias. Suponiendo la consistencia sintáctica en el cálculo $\mathsf H_{\tau_\in}^{=}$, la existencia de modelos del §11.10 ($\texttt{TLOG-MTH-00043}$) proporciona una $\tau_\in$-estructura que satisface **todas** las sentencias de $\operatorname{Ax}_{\mathsf{ZF}}$. Por la definición §12.14 satisface $\mathsf{ZF}_{\mathrm{obj}}$. La implicación está demostrada en $\mathsf M_{\mathrm{ext}}$ sin BPI ni AC. $\square$

**Alcance exacto:** no se ha demostrado aquí $\operatorname{Con}(\mathsf{ZF}_{\mathrm{obj}})$; tampoco se ha supuesto por definición que la estructura pertenezca a la jerarquía externa de manera transitiva o con $\in$ estándar. Una afirmación de existencia de modelo **sin antecedente** no se sigue del teorema. La no confusión entre niveles es esencial para las futuras interfaces de incompletitud.

## 12.19. Control del primer bloque y obligaciones de cierre del capítulo

`TLOG-CH12-M01` fija el lenguaje puro y todas las ocho familias de axiomas; demuestra tres proposiciones objeto y la aplicación metateórica condicional de completitud. Permanece **abierto** el desarrollo de notaciones y construcciones elementales por extensionalidad, cuya materia se distribuye con los Capítulos 13–16 sin alterar la arquitectura aprobada. También queda por auditar en el próximo microtramo el tratamiento sistemático de deducciones con parámetros y las equivalencias entre presentaciones usuales de los esquemas, antes del cierre final del Capítulo 12.

- Signatura única $\tau_\in$, con igualdad lógica y pertenencia relacional binaria: `PASS`.
- Axiomas objeto cerrados, dos esquemas infinitos tipados, fórmula de infinito sin términos derivados: `PASS`.
- Ninguna clase propia como elemento del dominio; no se deriva consistencia de la teoría objeto: `PASS`.
- $\mathsf M_{\mathrm{ext}}$ no confundida con $\mathsf{ZF}_{\mathrm{obj}}$: `PASS`.
- Sin AC, BPI ni nuevas reglas primitivas: `PASS`.
- No se proclama formalización Lean ni publicación web.

```text
TLOG-CH12-M01 = CLOSED / LOCAL QA PASS / DRIVE READBACK PASS
TLOG-CH12-0001 = PARTIAL-CLOSURE / NOT CLOSED
PART III = OPEN
PARTS CLOSED = 2/5
NEW CH12 RESULTS = 18
TLOG NODE COUNT = 220
TLOG DAG EDGES = 667
FORMALIZATION CANDIDATES = 64 / LEAN VERIFIED = 0
CHAPTERS CLOSED = 12/24 (50.0%)
```

Siguiente: `TLOG-CH12-M02 — Equivalencias de esquemas, control formal de definiciones y auditoría de cierre de la axiomatización objeto`.

## 12.20. Variantes axiomáticas y criterios de equivalencia

### Convención 12.20.1 — Equivalencia de presentaciones de una teoría objeto {#tlog-cnv-00015}

Fijada la signatura pura $\tau_\in$, dos conjuntos de sentencias $T,T'\subseteq\operatorname{Sent}_{\tau_\in}$ son **deductivamente equivalentes** si

$$
\operatorname{Cn}^{\mathrm{ded}}_{\mathsf H_{\tau_\in}^{=}}(T)
=\operatorname{Cn}^{\mathrm{ded}}_{\mathsf H_{\tau_\in}^{=}}(T').
$$

Esta condición no exige identidad *literal* de los árboles que integran $T$ y $T'$. Las variantes de esquema de §§12.22–12.25 se compararán en ese sentido: para cada fórmula generadora, se construye una **derivación finita** de la instancia correspondiente, y viceversa. No se introduce cuantificación objeto sobre fórmulas ni se confunde equivalencia deductiva de teorías con identidad de sus axiomas.

La posibilidad de reemplazar una expresión por otra dentro de una fórmula exige una justificación de equivalencia lógica o una expansión definicional expresamente tipada. No basta la semejanza tipográfica.

## 12.21. Renombrado y cierre de los esquemas

### Lema 12.21.1 — Invariancia deductiva de instancias bajo conversión alfa {#tlog-lem-00036}

Para toda matriz admitida por separación o reemplazo, dos elecciones admisibles de nombres **ligados auxiliares**, que conservan los nombres y posiciones de los parámetros libres, generan clausuras sentenciales $\sigma,\sigma'$ equivalentes por conversión alfa, y

$$
\vdash_{\mathsf H_{\tau_\in}^{=}}(\sigma\leftrightarrow\sigma').
$$

**Demostración.** Una instancia se obtiene de un árbol finito con lugares distinguidos para las variables de dominio, imagen, testigo y parámetros. En cada inserción elegimos un nombre que no pertenece al conjunto finito de nombres libres o ligados que podría producir captura; la existencia se sigue de la infinitud de $X$ y de la selección de frescos de §6.18. Dos elecciones distintas conservan los mismos marcadores de variable libre y los mismos índices de vinculación en el código $\operatorname{db}_{\tau_\in}$; la igualdad de códigos implica $\sigma\equiv_\alpha\sigma'$ por §6.29. El teorema deductivo de equivalencia alfa de §9.19 entrega el bicondicional. En este enunciado **no** se permite reordenar arbitrariamente los cuantificadores que vinculan parámetros distintos; tal reordenamiento, cuando se emplee, se prueba mediante las reglas ordinarias de primer orden. $\square$

## 12.22. Separación y dependencia del conjunto ambiente

### Proposición 12.22.1 — Equivalencia de los dos esquemas paramétricos de separación {#tlog-pro-00033}

Sea $\operatorname{Sep}^{\mathrm{amb}}$ el esquema de §12.9, que permite a la matriz $\theta(u,a,\bar p)$ mencionar el conjunto ambiente $a$. Sea $\operatorname{Sep}^{\mathrm{par}}$ el esquema aparentemente más restringido, cuyas matrices $\psi(u,\bar q)$ no mencionan **la variable designada como ambiente** $a$, aunque pueden mencionar parámetros $\bar q$ arbitrarios. Entonces

$$
\boxed{\operatorname{Sep}^{\mathrm{amb}}\equiv_{\mathrm{ded}}\operatorname{Sep}^{\mathrm{par}}}
$$

sobre la lógica de primer orden con igualdad; no se necesita reemplazo ni elección.

**Demostración.** Toda matriz $\psi(u,\bar q)$ sin dependencia de $a$ es admisible para $\operatorname{Sep}^{\mathrm{amb}}$, de modo que cada axioma de la versión paramétrica es una instancia de la primera, con renombrados frescos si procede. Para la otra dirección fijamos $\theta(u,a,\bar p)$ y escogemos un nombre nuevo $q$ que no aparezca en ella. Sea $\psi(u,q,\bar p)$ el árbol obtenido **renombrando sólo las apariciones libres designadas** de $a$ como $q$, con conversión alfa previa de los vinculantes incompatibles. El esquema $\operatorname{Sep}^{\mathrm{par}}$ proporciona la sentencia

$$
\forall q\,\forall\bar p\,\forall a\,\exists b\,\forall u\,
\bigl[u\in b\leftrightarrow(u\in a\land\psi(u,q,\bar p))\bigr].
$$

Para evitar una **captura real** que se produciría al sustituir directamente $q:=a$ bajo el cuantificador interior $\forall a$, tomamos primero una variable fresca $d$ y una lista de variables frescas y distintas $\bar r=(r_1,\ldots,r_k)$, todas fuera del soporte completo y de los nombres ligados de la matriz. Particularizamos $\forall q$ con $q:=d$ (sin captura), retiramos mediante particularización el prefijo $\forall\bar p$ reemplazando sus variables sucesivamente por los nombres frescos $\bar r$, y sólo **después** particularizamos el cuantificador interior $\forall a$ con $a:=d$. Esto produce

$$
\exists b\,\forall u\,[u\in b\leftrightarrow(u\in d\land\theta(u,d,\bar r))].
$$

La deducción proviene de una **sentencia**; aplicamos la generalización derivada de §9.24 para obtener el cierre universal de $\bar r$ y de $d$, y renombramos sus vinculantes como $\bar p$ y $a$ mediante equivalencia alfa. Así recuperamos precisamente la instancia de $\operatorname{Sep}^{\mathrm{amb}}$, sin emplear una sustitución capturante. Así cada instancia de $\operatorname{Sep}^{\mathrm{amb}}$ es consecuencia de una instancia de $\operatorname{Sep}^{\mathrm{par}}$. La equivalencia de teorías se obtiene por corte y finitud de las derivaciones. $\square$

No se ha producido el axioma de comprensión irrestricta: la existencia del conjunto ambiente $a$ sigue siendo una hipótesis interna indispensable.

## 12.23. Reemplazo global y reemplazo restringido al dominio

### Proposición 12.23.1 — Equivalencia de funcionalidad global y sobre el conjunto de partida {#tlog-pro-00034}

Para una fórmula $\rho(u,v,\bar p)$ del lenguaje puro consideremos la familia alternativa $\operatorname{Rep}^{\mathrm{glob}}$ cuyas instancias tienen la forma

$$
\forall\bar p\Bigl[
  \bigl(\forall u\exists!v\,\rho(u,v,\bar p)\bigr)
  \to\forall a\exists b\forall v\bigl(v\in b\leftrightarrow
       \exists u(u\in a\land\rho(u,v,\bar p))\bigr)
\Bigr].
$$

Aquí $a$ es el dominio cuantificado *después* de la condición global y los parámetros de $\rho$ son completamente libres de elegir. Entonces la familia de §12.10, que exige funcionalidad únicamente sobre $a$, y $\operatorname{Rep}^{\mathrm{glob}}$ son deductivamente equivalentes.

**Demostración.** De las instancias restringidas a $a$ se obtienen las globales: si $\forall u\exists!v\rho$, entonces $\forall u(u\in a\to\exists!v\rho)$ para cada $a$, y se aplica §12.10.

Recíprocamente, fijemos $\rho(u,v,a,\bar p)$ y construyamos la **relación totalizada**

$$
\widehat\rho(u,v,a,\bar p):\equiv
 \bigl(u\in a\land\rho(u,v,a,\bar p)\bigr)
 \lor\bigl(\neg(u\in a)\land v\doteq u\bigr).
$$

Renombramos previamente los vinculantes para que $u,v,a,\bar p$ sean distintos y ningún reemplazo capture variables. Bajo $\forall u(u\in a\to\exists!v\rho)$, la nueva relación tiene para **todo** $u$ un único valor: dentro de $a$, el valor único de $\rho$; fuera de $a$, exactamente $u$. Por tanto se satisface $\forall u\exists!v\widehat\rho$. Aplicamos la instancia global correspondiente, considerando $a$ como **parámetro** de $\widehat\rho$, y especializamos su variable de dominio $d$ al mismo $a$. Resulta un conjunto $b$ con

$$
\forall v\Bigl[v\in b\leftrightarrow
 \exists u\bigl(u\in a\land\widehat\rho(u,v,a,\bar p)\bigr)\Bigr].
$$

Para $u\in a$, $\widehat\rho(u,v,a,\bar p)\leftrightarrow\rho(u,v,a,\bar p)$ es demostrable proposicionalmente. Sustituyéndolo en la fórmula anterior obtenemos exactamente el consecuente de la instancia restringida. Cerramos universalmente los parámetros desde las premisas sentenciales, según §9.24. No se elige una familia de valores: la totalización fija **por fórmula** un valor único fuera del dominio. $\square$

La equivalencia es deductiva y presupone que la variante global **admite parámetros**, incluido aquel que designa el dominio en la totalización.

## 12.24. Forma de cobertura funcional

### Definición 12.24.1 — Esquema de cobertura de imágenes funcionales {#tlog-def-00064}

Para toda $\rho(u,v,a,\bar p)$ admisible, denotamos por $\operatorname{Cov}_{\rho}$ la sentencia

$$
\forall\bar p\forall a\Bigl[
 \bigl(\forall u(u\in a\to\exists!v\,\rho(u,v,a,\bar p))\bigr)
 \to\exists c\,\forall u\bigl(u\in a\to
       \exists v(v\in c\land\rho(u,v,a,\bar p))\bigr)
\Bigr].
$$

El conjunto $c$ contiene todos los valores de la relación funcional, pero **puede contener elementos adicionales**. Esto constituye un esquema de cobertura *funcional*, no el esquema general de colección para relaciones multivaluadas. Las variables testigo $c,v$ se normalizan y refrescan conforme al lema de §12.21.

## 12.25. De la cobertura a la imagen exacta

### Metateorema 12.25.1 — Equivalencia de cobertura funcional y reemplazo en presencia de separación {#tlog-mth-00051}

Sobre un sistema que contiene separación, las familias $\{\operatorname{Cov}_\rho\}_\rho$ y $\{\operatorname{Rep}_\rho\}_\rho$ generan las mismas consecuencias deductivas. En particular, **no** necesitamos elección para obtener la imagen *exacta* a partir de una cobertura funcional.

**Demostración.** Dada una instancia de reemplazo, su conjunto imagen exacto $b$ satisface $\operatorname{Cov}_\rho$: para cada $u\in a$, la hipótesis funcional aporta $v$ y el bicondicional definidor de $b$ asegura $v\in b$.

En sentido inverso, supongamos $\operatorname{Cov}_\rho$ y $\forall u\in a\,\exists!v\rho$. Hay entonces un conjunto $c$ que contiene un testigo de $\rho(u,-)$ para cada $u\in a$. Aplicamos **separación sobre ese mismo conjunto** con la matriz

$$
\theta(v,c,a,\bar p):\equiv
  \exists u\,(u\in a\land\rho(u,v,a,\bar p)).
$$

La instancia produce $b$ con

$$
\forall v\,[v\in b\leftrightarrow(v\in c\land\theta(v,c,a,\bar p))].
$$

Demostramos $\theta(v,c,a,\bar p)\Rightarrow v\in c$: el testigo $u\in a$ tiene, por cobertura, algún $w\in c$ con $\rho(u,w,a,\bar p)$; por unicidad funcional de $\rho$ sobre $a$, $v\doteq w$, y la sustitución por iguales en $v\in c$ da $v\in c$. En consecuencia el bicondicional se simplifica a $v\in b\leftrightarrow\theta(v,c,a,\bar p)$, exactamente la imagen de reemplazo de §12.10. Se trata de una prueba con existencia y unicidad **dentro** de la teoría objeto, sin seleccionar simultáneamente valores por una función externa. $\square$

**Límite:** esta equivalencia cubre sólo relaciones que ya son funcionales en $a$. La colección para relaciones arbitrarias no funcionales no queda demostrada por este argumento; no se confunden ambos principios.

## 12.26. El vacío sin utilizar infinito

### Proposición 12.26.1 — El conjunto vacío se demuestra con pares y separación {#tlog-pro-00035}

Ya es demostrable $\exists!e\,\forall u\neg(u\in e)$ en el fragmento de $\mathsf{ZF}_{\mathrm{obj}}$ que sólo utiliza **pares, separación y extensionalidad**, sin emplear infinito, unión, potencia, reemplazo ni regularidad.

**Demostración objeto.** Por la no vacuidad lógica del dominio y la reflexividad de la igualdad, existe un objeto $a$. Aplicamos pares a $a,a$, obteniendo un conjunto $s$ cuyos miembros son exactamente $a$. Instanciamos separación sobre $s$ con $\theta(u,s):\equiv\neg(u\doteq u)$, fórmula sin testigos externos. Existe $e$ tal que

$$
\forall u\,[u\in e\leftrightarrow(u\in s\land\neg(u\doteq u))].
$$

Como $u\doteq u$ es axioma lógico para cada $u$, el consecuente es falso; por lógica clásica, $\forall u\neg(u\in e)$. Si $e'$ tiene también ningún miembro, entonces $\forall u(u\in e\leftrightarrow u\in e')$; la extensionalidad proporciona $e\doteq e'$. Unimos existencia y unicidad por las reglas deductivas de primer orden. $\square$

Esto **mejora la dependencia de la demostración**, no prueba independencia axiomática de infinito. La derivación alternativa de §12.15 sigue siendo válida y registrada con su propia genealogía deductiva.

## 12.27. El nombre del vacío como extensión definicional

### Definición 12.27.1 — Extensión por una constante definida {#tlog-def-00065}

Sea $\varepsilon$ un símbolo **nuevo**, de aridad funcional cero, no perteneciente a $\tau_\in$. Construimos $\tau_\in^\varepsilon$ añadiendo $\varepsilon$ a $F_0$, y definimos la teoría ampliada

$$
T_\varepsilon:=\operatorname{Ax}_{\mathsf{ZF}}
 \cup\{\delta(\varepsilon)\},\qquad
\delta(z):\equiv\forall u\neg(u\in z).
$$

La nueva expresión $\varepsilon$ es un **término cerrado sólo del lenguaje extendido**. La existencia y unicidad de su referente están justificadas deductivamente por §12.26, no presupuestas por una sintaxis mayor. La grafía editorial $\varnothing$ puede representar $\varepsilon$ **siempre que conste este compromiso definicional**, o puede entenderse como notación eliminable en el lenguaje puro. No se añade $\varepsilon$ al conjunto canónico de símbolos de $\tau_\in$, ni $\delta(\varepsilon)$ a $\operatorname{Ax}_{\mathsf{ZF}}$.

## 12.28. Conservatividad de la extensión por una constante definida

### Metateorema 12.28.1 — Conservatividad sintáctica y semántica de definiciones únicas {#tlog-mth-00052}

**Enunciado.** Sea $L$ una signatura numerable, $T\subseteq\operatorname{Sent}_L$, $\delta(x)\in\operatorname{Fm}_L$ con $\operatorname{FV}(\delta)\subseteq\{x\}$, y supongamos

$$
T\vdash_{\mathsf H_L^{=}}\exists!x\,\delta(x).
$$

Añadamos una sola constante fresca $c$, formando $L^+=L\sqcup\{c\}$ y $T^+=T\cup\{\delta(c)\}$. Entonces, para **toda fórmula del lenguaje original** $\varphi\in\operatorname{Fm}_L$,

$$
\boxed{T^+\vdash_{\mathsf H_{L^+}^{=}}\varphi
\quad\Longleftrightarrow\quad
T\vdash_{\mathsf H_L^{=}}\varphi.}
$$

Además, el reducto de cada modelo de $T^+$ es modelo de $T$, y **cada** modelo de $T$ posee una única expansión a modelo de $T^+$ al interpretar $c$ por el único testigo de $\delta$.

**Demostración.** El transporte de una derivación de $T$ al lenguaje ampliado es inmediato, pues las instancias axiomáticas y los pasos de $\mathrm{MP}$ persisten bajo la inclusión de signaturas (§§7.13 y 9.5). Para la implicación opuesta comenzamos con una **sentencia** $\sigma\in\operatorname{Sent}_L$. Supongamos $T\nvdash\sigma$. Por el núcleo clásico, teorema de deducción y finitud de las pruebas (§§9.15, 9.23), $T\cup\{\neg\sigma\}$ es sintácticamente consistente. Puesto que $L$ es numerable, el teorema de existencia de modelos de §11.10 produce en la metateoría ZF una estructura $\mathfrak A$ que satisface $T\cup\{\neg\sigma\}$. Por corrección de §10.7, $T\vdash\exists!x\delta(x)$ fuerza que $\mathfrak A$ tenga **un único** elemento $a$ que cumple $\delta$. Interpretamos la nueva constante por $a$, obteniendo la expansión $\mathfrak A^+$. Por el lema de preservación bajo reductos y la semántica de sustitución segura, $\mathfrak A^+\models T^+$ y $\mathfrak A^+\models\neg\sigma$. Si $T^+\vdash\sigma$, la corrección de §10.7 daría $\mathfrak A^+\models\sigma$, contradicción. Por contraposición, $T^+\vdash\sigma\Rightarrow T\vdash\sigma$.

Para $\varphi$ **abierta**, las premisas $T^+$ son sentencias. El principio deductivo de generalización desde premisas sentenciales (§9.24) transforma $T^+\vdash\varphi$ en $T^+\vdash\varphi^\forall$, donde $\varphi^\forall\in\operatorname{Sent}_L$ es su clausura universal. Por el caso sentencial, $T\vdash\varphi^\forall$; una secuencia finita de particularizaciones universales lleva a $T\vdash\varphi$. Para la afirmación semántica, toda estructura de $T$ tiene un único testigo de $\delta$ por corrección y el teorema de unicidad, de modo que la interpretación de $c$ está **forzada**, no elegida entre múltiples posibilidades. La correspondencia de modelos se sigue de la coincidencia de las interpretaciones de todos los símbolos antiguos. $\square$

**Límites exactos:** (i) el uso de completitud es legítimo en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ porque $L$ es numerable; (ii) no se deduce $\operatorname{Con}(T)$; (iii) la conservatividad **no** significa que las fórmulas que contienen el símbolo nuevo fueran ya fórmulas del lenguaje original; (iv) la prueba usa existencia **y unicidad**, no meramente existencia.

## 12.29. Aplicación canónica a la constante del vacío

### Corolario 12.29.1 — La introducción de $\varnothing$ no crea teoremas antiguos {#tlog-cor-00013}

Para toda $\varphi\in\operatorname{Fm}_{\tau_\in}$,

$$
\boxed{\operatorname{Ax}_{\mathsf{ZF}}\vdash_{\tau_\in}\varphi
\iff
T_\varepsilon\vdash_{\tau_\in^\varepsilon}\varphi.}
$$

**Demostración.** §12.26 demuestra en el lenguaje primitivo $\operatorname{Ax}_{\mathsf{ZF}}\vdash\exists!z\,\delta(z)$ y la signatura $\tau_\in$ es finita, por lo tanto numerable. Aplicamos el metateorema de §12.28 con $T=\operatorname{Ax}_{\mathsf{ZF}}$ y $c=\varepsilon$. La extensión se define por el único axioma $\delta(\varepsilon)$ y su símbolo nuevo es puramente funcional nulario. $\square$

La prueba no interpreta la teoría objeto en el universo de la metateoría ni convierte $\varnothing$ en símbolo primitivo. Las construcciones de pares, unión y potencia seguirán su propio desarrollo en el Capítulo 13.

## 12.30. Instanciación con parámetros: axioma cerrado frente a cuerpo abierto

### Lema 12.30.1 — Particularización correcta de las instancias sentenciales {#tlog-lem-00037}

Sea $\sigma=\forall p_1\cdots\forall p_k\forall a\,\chi(\bar p,a)\in\operatorname{Ax}_{\mathsf{ZF}}$ una instancia universalmente cerrada de separación o reemplazo. Para cualquier sucesión finita de variables individuales o términos del lenguaje de pertenencia $\bar t,t$ **libres para sustituir** sus variables cuantificadas,

$$
\operatorname{Ax}_{\mathsf{ZF}}\vdash_{\mathsf H_{\tau_\in}^{=}}\chi(\bar t,t).
$$

**Demostración.** La sentencia $\sigma$ es línea-premisa admisible. Aplicamos el esquema lógico de particularización universal, con $\operatorname{FreeFor}$ satisfecho en cada paso. Si los nombres propuestos producen captura en una matriz interior, primero normalizamos las declaraciones ligadas por §12.21. Eliminamos sucesivamente los cuantificadores del prefijo y obtenemos $\chi(\bar t,t)$ mediante $\mathrm{MP}$. Cada paso es una deducción objeto finita. $\square$

La formulación **no** convierte automáticamente los cuerpos $\chi(\bar p,a)$ en axiomas primitivos sin cierre; tampoco autoriza generalizar desde premisas abiertas arbitrarias. La recuperación de clausuras universales desde un conjunto sentencial de premisas utiliza precisamente la condición lateral de §9.24.

## 12.31. Los testigos de separación y de reemplazo exacto son únicos

### Lema 12.31.1 — Unicidad extensional de subconjuntos e imágenes definidos {#tlog-lem-00038}

Para cada matriz $\theta(u,a,\bar p)$ de separación y cada matriz $\rho(u,v,a,\bar p)$ de reemplazo, la teoría objeto demuestra, con las premisas funcionales exigidas para $\rho$, la **unicidad** del testigo $b$ cuyo conjunto de miembros está descrito por el correspondiente bicondicional. Más precisamente, si $b,b'$ cumplen

$$
\forall u\,[u\in b\leftrightarrow(u\in a\land\theta(u,a,\bar p))]
\quad\text{y}\quad
\forall u\,[u\in b'\leftrightarrow(u\in a\land\theta(u,a,\bar p))],
$$

entonces $b\doteq b'$; y análogamente si ambos satisfacen
$\forall v\,[v\in b\leftrightarrow\exists u(u\in a\land\rho(u,v,a,\bar p))]$.

**Demostración objeto.** En el primer caso, para todo $u$, los dos bicondicionales implican $u\in b\leftrightarrow u\in b'$. Por introducción universal desde los cuerpos indicados —con sus parámetros tratados como datos fijos y sin generalización inválida desde ellos— se obtiene $\forall u(u\in b\leftrightarrow u\in b')$. Extensionalidad (§12.4) implica $b\doteq b'$. La misma secuencia funciona para el segundo caso, porque la fórmula de pertenencia de los dos testigos es idéntica; la hipótesis funcional se requiere para la **existencia** del testigo de reemplazo, no para este paso de unicidad. $\square$

En consecuencia, una futura notación de subconjunto separado o imagen por reemplazo se podrá introducir mediante una definición cuya existencia y unicidad han sido demostradas, pero **no** se promueve en este capítulo una nueva operación primitiva de conjuntos.

## 12.32. Cierre de las equivalencias axiomáticas

### Metateorema 12.32.1 — Invariancia de la teoría objeto bajo las presentaciones alternativas autorizadas {#tlog-mth-00053}

Denotemos por $\operatorname{Ax}^{\mathrm{alt}}_{\mathsf{ZF}}$ un conjunto de sentencias del **mismo lenguaje puro** que conserva literalmente los seis axiomas individuales y sustituye, de manera independiente:

- separación con matriz que depende del ambiente por la versión con el ambiente tratado como un parámetro ordinario;
- reemplazo funcional restringido al dominio por su forma global con parámetros; o
- reemplazo exacto por cobertura **funcional**, **siempre reteniendo separación**.

Entonces, para toda fórmula $\varphi\in\operatorname{Fm}_{\tau_\in}$,

$$
\boxed{
\operatorname{Ax}_{\mathsf{ZF}}\vdash_{\mathsf H_{\tau_\in}^{=}}\varphi
\iff
\operatorname{Ax}^{\mathrm{alt}}_{\mathsf{ZF}}\vdash_{\mathsf H_{\tau_\in}^{=}}\varphi.}
$$

**Demostración.** Para separación, §12.22 exhibe una derivación finita en ambos sentidos para cada instancia. Para reemplazo global/restringido, §12.23 construye las transformaciones sintácticas respectivas, incluyendo la totalización fuera del conjunto de partida. Para la cobertura, §12.25 establece los dos sentidos en presencia de separación. La invariancia bajo nombres ligados alternativos sigue de §12.21. Dada una demostración concreta desde una de estas teorías, sólo utiliza **finitas** instancias axiomáticas; reemplazamos cada instancia de la familia modificada por su derivación desde la otra familia. El lema de corte de §9.10 permite ensamblar las pruebas y conservar la conclusión. Repetimos el procedimiento en sentido contrario. Por tanto ambas relaciones de derivabilidad coinciden sobre todas las fórmulas del lenguaje puro. $\square$

**Control de alcance:** no se ha probado equivalencia con colección para relaciones **arbitrarias**, ni con cualquier combinación de axiomas más débiles que los explicitados. Tampoco se ha añadido elección ni se ha cambiado la signatura primitiva.

## 12.33. Frontera exacta entre teoría objeto, definiciones y metateoría

La reconstrucción conserva **tres niveles**: (a) axiomas y teoremas de $\mathsf{ZF}_{\mathrm{obj}}$ en la sintaxis pura; (b) abreviaciones eliminables o extensiones definicionales conservativas introducidas después de demostrar existencia y unicidad; (c) construcciones metateóricas realizadas en $\mathsf M_{\mathrm{ext}}$. No hay transitividad automática entre estos niveles. Las presentaciones alternativas de §§12.22–12.25 son **deductivamente** equivalentes, no idénticas como conjuntos de árboles. El uso de completitud en §12.28 es metateórico y restringido a signaturas numerables; no establece por sí mismo $\operatorname{Con}(\mathsf{ZF}_{\mathrm{obj}})$.

Las operaciones $\{a,b\}$, $\bigcup a$, $\mathcal P(a)$ y las funciones de conjunto siguen reservadas para el Capítulo 13, y relaciones, aplicaciones, cocientes e inducción para los capítulos 14–16. **No** se necesita formular ni interpretar $\mathsf{AC}$ como axioma objeto para esta infraestructura. Los esquemas de separación/reemplazo permanecen metasintácticos; cada instancia concreta es una sentencia de primer orden.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 11](capitulo-11.md) · [Capítulo 13 →](capitulo-13.md)


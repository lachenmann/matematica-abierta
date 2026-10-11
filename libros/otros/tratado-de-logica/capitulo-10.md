---
title: Capítulo 10 — Teorema de corrección
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
content-id: MA-BCH-0212
content-type: book-chapter
source-id: TLOG-CH10-0001
prerequisites:
- MA-BCH-0206
- MA-BCH-0209
- MA-BCH-0210
- MA-BCH-0211
related:
- MA-BOK-0014
source-sha256: b6f5df5ef8b2ccd91efd318cb9fb7f5a2712ff18e1d40c2ba9252c3188ceec27
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 9](capitulo-09.md) · [Capítulo 11 →](capitulo-11.md)

## 10.0. El puente que faltaba: de la prueba a la verdad

En los Capítulos 5–8 construimos la gramática $\operatorname{Fm}_\tau$, la semántica $\mathfrak A,s\models_\tau\varphi$ y la consecuencia **local** $\Gamma\models_\tau\varphi$. En el Capítulo 9 fijamos, con independencia de los modelos, el cálculo hilbertiano $\mathsf H_\tau^{=}$: axiomas proposicionales `H1`–`H12`, cuantificacionales `Q1`–`Q5`, de igualdad `E1`–`E2`, todas sus clausuras universales finitas y **una única regla primitiva**, modus ponens. Este capítulo verifica la compatibilidad de ambos objetos sin convertir nunca $\vdash$ en una definición de $\models$.

Se trabajará en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ con lógica clásica **sin axioma de elección tácito**. La signatura $\tau$ es cualquier conjunto de símbolos funcionales y relacionales tipados por aridad finita, incluida la aridad cero; las estructuras tienen universo no vacío y la igualdad $\doteq$ denota identidad. Las premisas pueden ser **fórmulas abiertas**, y una misma asignación sirve para comprobar simultáneamente todas ellas y la conclusión.

**Fuentes de contracontrol, no pruebas importadas.** `TLOG-SRC-0002` (Enderton, *A Mathematical Introduction to Logic*, 2.ª ed., cap. 2, §2.5, pp. 131–135) y `TLOG-SRC-0003` (Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed., cap. 3, §3.6, pp. 121–124) ya figuran en el registro bibliográfico. Se reutiliza el **alcance previamente cotejado** para la arquitectura «axiomas válidos + preservación por regla + inducción sobre pruebas». La demostración siguiente se reconstruye según la base axiomática específica de TLOG; no se afirma haber colacionado hoy nuevas páginas.

La obligación deductiva que se resolverá es

$$
\boxed{\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi
\quad\Longrightarrow\quad \Gamma\models_\tau\varphi.}
$$

La implicación inversa, que **no** se necesita para la presente, pertenece al Capítulo 11.

## 10.1. Validez de las instancias proposicionales de primer orden

### Lema 10.1.1 — Validez de las instancias proposicionales de primer orden {#tlog-lem-00024}

**Enunciado.** Cada instancia $\theta$ de `H1`–`H12` sobre fórmulas de primer orden es válida:

$$\theta\in\operatorname{Ax}^{\mathrm{prop}}_\tau\Longrightarrow\models_\tau\theta.$$

**Demostración.** Fijemos una estructura $\mathfrak A$ y una asignación $s:X\to A$. Para la instancia en cuestión, asignamos a las metavariables proposicionales los valores de satisfacción de sus fórmulas de primer orden bajo la **misma** pareja $(\mathfrak A,s)$. Por las cláusulas recursivas de satisfacción (§8.4), $\neg,\land,\lor,\to,\leftrightarrow$ actúan sobre esos valores con exactamente las tablas de verdad de `CPL` (§2.1). Las doce formas `H1`–`H12` fueron controladas en [TLOG-LEM-00005](capitulo-04.md#tlog-lem-00005): cada una es tautología para cualquier valuación de sus dos o tres metavariables, con independencia de la estructura interna de las fórmulas que las sustituyen.

En detalle, `H1` vale porque $a\to(b\to a)=1$ para cualquier $a,b\in\{0,1\}$; `H2` formaliza la composición de implicaciones y no admite una valuación con antecedente verdadero y consecuente falso; `H3` es la contraposición clásica. `H4`–`H6` corresponden a eliminación e introducción veritativo-funcional de $\land$; `H7`–`H9`, a la disyunción inclusiva y sus casos; `H10`–`H12`, a las dos direcciones de $\leftrightarrow$ y su introducción desde ambas implicaciones. Por lo tanto, la instancia $\theta$ es satisfecha bajo toda $\mathfrak A,s$. $\square$

**Caso nulario.** Nada cambia si una metavariable se reemplaza por $R()$ con $R\in R_0$: la asignación $(\mathfrak A,s)$ determina un valor de verdad, aunque el átomo no tenga variables.


## 10.2. Validez de los esquemas cuantificacionales Q1–Q5

### Lema 10.2.1 — Validez de los esquemas cuantificacionales Q1–Q5 {#tlog-lem-00025}

**Enunciado.** Para $\tau$ fija, **todas** las instancias de los cinco esquemas `Q1`–`Q5` definidos en §9.3 son válidas. Se conservan literalmente sus restricciones `FreeFor` y la condición lateral de `Q4`.

**Demostración.** Sean $\mathfrak A$ y $s$ arbitrarias, con universo $A\ne\varnothing$. Examinamos todas las familias de instancias.

**`Q1` — particularización universal.** En $\forall x\varphi\to\varphi[t/x]_{\mathrm{lit}}$, la condición $\operatorname{FreeFor}_\tau(t,x,\varphi)$ asegura la aplicación de [TLOG-MTH-00028](capitulo-08.md#tlog-mth-00028). Si $\mathfrak A,s\models\forall x\varphi$, entonces $\mathfrak A,s[x\mapsto a]\models\varphi$ para cada $a\in A$; tomando $a=\llbracket t\rrbracket_{\mathfrak A,s}\in A$, el lema de sustitución da $\mathfrak A,s\models\varphi[t/x]_{\mathrm{lit}}$. Si el antecedente no se satisface, la implicación es verdadera por su cláusula booleana.

**`Q2` — introducción existencial.** Si $\mathfrak A,s\models\varphi[t/x]_{\mathrm{lit}}$, la misma equivalencia semántica da $\mathfrak A,s[x\mapsto v]\models\varphi$, con $v=\llbracket t\rrbracket_{\mathfrak A,s}\in A$. El testigo $v$ verifica $\mathfrak A,s\models\exists x\varphi$; si falla el antecedente, la implicación vuelve a valer.

**`Q3` — distribución de $\forall$ sobre $\to$.** Supongamos verdaderos en $s$ tanto $\forall x(\varphi\to\psi)$ como $\forall x\varphi$. Para cualquier $a\in A$, en la asignación $s[x\mapsto a]$ son verdaderas $\varphi\to\psi$ y $\varphi$; por la cláusula de implicación se satisface $\psi$. Como $a$ fue arbitrario, se satisface $\forall x\psi$. Esto demuestra la instancia entera y **no** exige condición sobre $\operatorname{FV}(\varphi)$ ni $\operatorname{FV}(\psi)$.

**`Q4` — cuantificación vacua.** Si $x\notin\operatorname{FV}(\varphi)$ y $\mathfrak A,s\models\varphi$, entonces para todo $a\in A$ las asignaciones $s$ y $s[x\mapsto a]$ coinciden en las variables libres de $\varphi$. Por localidad ([TLOG-LEM-00019](capitulo-08.md#tlog-lem-00019)), también $\mathfrak A,s[x\mapsto a]\models\varphi$; luego $\mathfrak A,s\models\forall x\varphi$. Se ha usado precisamente la condición lateral del esquema.

**`Q5` — dualidad del cuantificador existencial primitivo.** Por la cláusula semántica de $\exists$, se tiene $\mathfrak A,s\models\exists x\varphi$ si y sólo si existe $a\in A$ que satisface $\varphi$ bajo $s[x\mapsto a]$. Por lógica clásica, esto equivale a negar que **todo** $a\in A$ satisfaga $\neg\varphi$; esto es exactamente $\mathfrak A,s\models\neg\forall x\neg\varphi$. La cláusula del bicondicional produce la verdad de `Q5`. La equivalencia se demostró semánticamente en [TLOG-PRO-00012](capitulo-08.md#tlog-pro-00012), sin identificar las dos fórmulas como cadenas.

Las cinco familias quedan verificadas para todas las estructuras y asignaciones. $\square$

**Control de captura.** La demostración de `Q1`/`Q2` fracasa si se omite `FreeFor`; por ejemplo, reemplazar literalmente $x$ por $y$ bajo un cuantificador $\forall y$ puede convertir una ocurrencia libre de $y$ en ligada. El esquema de TLOG excluye exactamente esas instancias.


## 10.3. Validez de los esquemas de igualdad E1–E2

### Lema 10.3.1 — Validez de los esquemas de igualdad E1–E2 {#tlog-lem-00026}

**Enunciado.** Todas las instancias de `E1` y `E2` (§9.4) son válidas en toda $\tau$-estructura, interpretando $\doteq$ como **identidad del universo**.

**Demostración.** Para `E1`, la evaluación del término $t$ es un elemento determinado $v=\llbracket t\rrbracket_{\mathfrak A,s}\in A$. Luego $v=v$, de modo que $\mathfrak A,s\models t\doteq t$.

Consideremos una instancia de `E2`:

$$
(t\doteq u)\to\bigl(\varphi[t/x]_{\mathrm{lit}}\to\varphi[u/x]_{\mathrm{lit}}\bigr),
$$

con $\operatorname{FreeFor}(t,x,\varphi)$ y $\operatorname{FreeFor}(u,x,\varphi)$. Si $\mathfrak A,s\not\models t\doteq u$, la implicación exterior es verdadera. En caso contrario, las evaluaciones existen y tienen **el mismo valor**:

$$\llbracket t\rrbracket_{\mathfrak A,s}=\llbracket u\rrbracket_{\mathfrak A,s}=v.$$

Aplicando por separado el lema de sustitución semántica [TLOG-MTH-00028](capitulo-08.md#tlog-mth-00028) a los dos términos, obtenemos

$$
\begin{aligned}
\mathfrak A,s\models\varphi[t/x]_{\mathrm{lit}}
&\iff\mathfrak A,s[x\mapsto v]\models\varphi,\\
\mathfrak A,s\models\varphi[u/x]_{\mathrm{lit}}
&\iff\mathfrak A,s[x\mapsto v]\models\varphi.
\end{aligned}
$$

Por lo tanto, las dos sustituciones tienen **idéntico valor de satisfacción**, y su implicación es verdadera. Esto vale también para términos constantes (aridad funcional cero), para una matriz con relaciones nularias y cuando $x$ no es libre en $\varphi$. $\square$

El argumento exige tanto el **tipado de la igualdad lógica** como las **dos** condiciones `FreeFor`: no utiliza una regla informal de reemplazo de caracteres ni presume reflexión de relaciones bajo homomorfismos.


## 10.4. Preservación de satisfacción bajo modus ponens

### Lema 10.4.1 — Preservación de satisfacción bajo modus ponens {#tlog-lem-00027}

**Enunciado.** Para toda pareja fija $(\mathfrak A,s)$, si $\mathfrak A,s\models_\tau\alpha$ y $\mathfrak A,s\models_\tau(\alpha\to\beta)$, entonces $\mathfrak A,s\models_\tau\beta$.

**Demostración.** La semántica de la implicación (§8.4) declara $\mathfrak A,s\models\alpha\to\beta$ exactamente cuando $\alpha$ es falsa bajo $(\mathfrak A,s)$ o $\beta$ es verdadera bajo esa misma pareja. Como la primera disyuntiva está excluida por hipótesis, debe verificarse la segunda. $\square$

La preservación es **puntual y local**: si las dos premisas se comprobaran con asignaciones distintas, la conclusión no estaría justificada. `MP` es la única regla primitiva de $\mathsf H_\tau^{=}$.


## 10.5. La validez subsiste bajo prefijos universales finitos

### Proposición 10.5.1 — La validez subsiste bajo prefijos universales finitos {#tlog-pro-00026}

**Enunciado.** Si $\models_\tau\theta$, entonces para **cualquier lista finita**, incluso vacía o con repeticiones, $\bar x=(x_1,\ldots,x_n)\in X^{<\omega}$, se cumple

$$\boxed{\models_\tau\forall x_1\cdots\forall x_n\theta.}$$

**Demostración.** Se realiza inducción sobre $n$. El caso $n=0$ es la hipótesis. Para el paso, supongamos válida una fórmula $\rho$ y fijemos una variable $x$, estructura $\mathfrak A$ y asignación $s$. Para cada $a\in A$, la actualización $s[x\mapsto a]$ es una asignación del mismo tipo. La validez de $\rho$ implica $\mathfrak A,s[x\mapsto a]\models\rho$; por la cláusula de $\forall$, $\mathfrak A,s\models\forall x\rho$. Ningún paso exige que $x$ sea libre, que las variables de la lista sean distintas, ni que se elija un elemento de cada estructura. $\square$

Se trata de la **preservación semántica** de la validez, no de una regla deductiva sobre premisas. Coincide exactamente con las clausuras **prefijas** utilizadas al definir el conjunto axiomático en §9.5.


## 10.6. Todas las instancias axiomáticas del cálculo son válidas

### Metateorema 10.6.1 — Todas las instancias axiomáticas del cálculo son válidas {#tlog-mth-00039}

**Enunciado.** Para todo $\theta\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$ se cumple $\models_\tau\theta$.

**Demostración.** Según [TLOG-DEF-00052](capitulo-09.md#tlog-def-00052), existen una fórmula básica $\theta_0\in\operatorname{Ax}^0_\tau$ y una lista finita $\bar x\in X^{<\omega}$ tales que $\theta=\forall\bar x\,\theta_0$. La unión definitoria de $\operatorname{Ax}^0_\tau$ ofrece **tres** posibilidades exhaustivas: (i) es una instancia de `H1`–`H12`, válida por [TLOG-LEM-00024](#tlog-lem-00024); (ii) es una instancia de `Q1`–`Q5`, válida por [TLOG-LEM-00025](#tlog-lem-00025); (iii) es una instancia de `E1`–`E2`, válida por [TLOG-LEM-00026](#tlog-lem-00026). En todos los casos $\models_\tau\theta_0$. La proposición [TLOG-PRO-00026](#tlog-pro-00026) transmite la validez a $\forall\bar x\theta_0=\theta$. $\square$

La prueba incluye **todas** las instancias, incluso con variables libres, y sus prefijos universales arbitrarios. No depende de la posterior corrección del cálculo.


## 10.7. Teorema de corrección de primer orden con igualdad

### Metateorema 10.7.1 — Teorema de corrección de primer orden con igualdad {#tlog-mth-00040}

**Enunciado (corrección fuerte, con premisas abiertas).** Sean $\tau$ una signatura arbitraria, $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\varphi\in\operatorname{Fm}_\tau$. Entonces

$$\boxed{\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi\ \Longrightarrow\ \Gamma\models_\tau\varphi.}$$

**Demostración.** Supongamos $\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi$. Por §9.8 existe una derivación finita $\Pi=(\varphi_0,\ldots,\varphi_n)$ desde $\Gamma$, con $\varphi_n=\varphi$. Sean $\mathfrak A$ una $\tau$-estructura **arbitraria** y $s:X\to A$ una asignación **arbitraria** tales que

$$\mathfrak A,s\models_\tau\Gamma,\quad\text{esto es, }(\forall\gamma\in\Gamma)\ \mathfrak A,s\models_\tau\gamma.$$

Demostraremos por inducción sobre $k\le n$ que $\mathfrak A,s\models_\tau\varphi_k$, usando las tres cláusulas exhaustivas de [TLOG-DEF-00053](capitulo-09.md#tlog-def-00053):

1. **Línea de premisa:** si $\varphi_k\in\Gamma$, la satisfacción se deduce directamente de la hipótesis sobre $\Gamma$.
2. **Línea axiomática:** si $\varphi_k\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$, el metateorema [TLOG-MTH-00039](#tlog-mth-00039) afirma $\models_\tau\varphi_k$; por tanto también $\mathfrak A,s\models_\tau\varphi_k$, independientemente de $\Gamma$.
3. **Línea por modus ponens:** existen $i,j<k$ con $\varphi_j=(\varphi_i\to\varphi_k)$. Por las hipótesis inductivas, $\mathfrak A,s\models_\tau\varphi_i$ y $\mathfrak A,s\models_\tau(\varphi_i\to\varphi_k)$. El lema [TLOG-LEM-00027](#tlog-lem-00027) implica $\mathfrak A,s\models_\tau\varphi_k$.

No existe cuarto caso: la **generalización no es regla primitiva**, sino transformación de derivaciones válida bajo las restricciones de §9.11. En particular, la inducción jamás generaliza a partir de una premisa abierta. La última línea satisface $\mathfrak A,s\models_\tau\varphi$. Como $\mathfrak A,s$ fue cualquier pareja que satisficiera simultáneamente $\Gamma$, la definición **local** de consecuencia ([TLOG-DEF-00049](capitulo-08.md#tlog-def-00049)) entrega $\Gamma\models_\tau\varphi$. $\square$

**Control fundacional.** La única elección de objeto realizada fue fijar temporalmente una **derivación existente** $\Pi$ y una pareja arbitraria $(\mathfrak A,s)$ bajo una implicación. No se construye una familia de pruebas elegidas ni se forma un conjunto de todos los modelos. Toda inducción recorre una lista finita en ZF clásica, sin AC.

**Separación lógica.** Hemos demostrado $\vdash\Rightarrow\models$ como *teorema*, no como equivalencia definicional. La dirección $\models\Rightarrow\vdash$ necesita construir modelos de teorías consistentes y permanece íntegramente reservada para el Capítulo 11.


## 10.8. Los teoremas son válidos y los contramodelos impiden demostraciones

### Corolario 10.8.1 — Los teoremas son válidos y los contramodelos impiden demostraciones {#tlog-cor-00008}

**Enunciado.** Se deducen tres afirmaciones:

1. Si $\vdash_{\mathsf H_\tau^{=}}\varphi$, entonces $\models_\tau\varphi$.
2. Si existe una estructura $\mathfrak A$ y una asignación $s$ con $\mathfrak A,s\models_\tau\Gamma$ y $\mathfrak A,s\not\models_\tau\varphi$, entonces $\Gamma\nvdash_{\mathsf H_\tau^{=}}\varphi$.
3. La derivabilidad local también es correcta respecto de la consecuencia **global** $\models_\tau^{\mathrm g}$: $\Gamma\vdash\varphi\Rightarrow\Gamma\models_\tau^{\mathrm g}\varphi$.

**Demostración.** En (1) se aplica [TLOG-MTH-00040](#tlog-mth-00040) con $\Gamma=\varnothing$. El antecedente de la consecuencia semántica es entonces verdadero bajo toda asignación, y resulta validez general. En (2), tal pareja $(\mathfrak A,s)$ es un **contramodelo local**; por definición niega $\Gamma\models_\tau\varphi$, y por contraposición de la corrección niega la derivabilidad. Para (3), si una estructura satisface globalmente $\Gamma$, cada una de sus asignaciones satisface todas las premisas; la consecuencia local ya probada aplica a cada asignación y la conclusión queda satisfecha globalmente. $\square$

**Contraejemplo deductivo ahora justificado.** En la signatura con predicado unario $P$, el conjunto $\Gamma=\{P(x_0)\}$ **no** demuestra $\forall x_0P(x_0)$. En efecto, tomemos $A=\{0,1\}$, $P^{\mathfrak A}=\{0\}$ y una asignación con $s(x_0)=0$. Se tiene $\mathfrak A,s\models\Gamma$, pero $\mathfrak A,s\not\models\forall x_0P(x_0)$. Por (2), $\Gamma\nvdash\forall x_0P(x_0)$. La mera ausencia de autorización para generalizar, observada en §9.12, se ha convertido aquí en una **prueba de no derivabilidad**.


## 10.9. La existencia de realización semántica implica consistencia sintáctica

### Corolario 10.9.1 — La existencia de realización semántica implica consistencia sintáctica {#tlog-cor-00009}

**Enunciado.** Si existe una $\tau$-estructura $\mathfrak A$ y una asignación $s:X\to A$ con $\mathfrak A,s\models_\tau\Gamma$, entonces $\Gamma$ es **sintácticamente consistente** en el sentido de §9.22:

$$\boxed{\operatorname{Sat}_{\mathfrak A}(\Gamma)\ne\varnothing\quad\Longrightarrow\quad\Gamma\nvdash_{\mathsf H_\tau^{=}}\bot_\tau.}$$

En particular, si $S\subseteq\operatorname{Sent}_\tau$ admite un modelo, entonces $S$ es deductivamente consistente.

**Demostración.** En §9.22 se fijó $\kappa:=\forall x_0(x_0\doteq x_0)$ y $\bot_\tau:=(\kappa\land\neg\kappa)$. Para **toda** $\mathfrak B,r$, la fórmula $\kappa$ es verdadera: cualquiera que sea $b\in B$, la actualización $r[x_0\mapsto b]$ satisface la igualdad lógica $x_0\doteq x_0$. En consecuencia $\kappa\land\neg\kappa$ es falsa para toda estructura y asignación, por las cláusulas de $\neg$ y $\land$ (§8.4).

Supongamos $\mathfrak A,s\models\Gamma$ y, buscando contradicción, $\Gamma\vdash\bot_\tau$. Por el teorema de corrección $\Gamma\models\bot_\tau$, y en particular $\mathfrak A,s\models\bot_\tau$; pero acabamos de demostrar que esto es imposible. Luego $\Gamma\nvdash\bot_\tau$. Si $S$ es un conjunto de sentencias con modelo $\mathfrak A$, existe alguna asignación (el universo es no vacío) y todas satisfacen cada sentencia de $S$; se aplica el primer enunciado. $\square$

**Límite del resultado.** No se afirma aquí $\Gamma$ consistente $\Rightarrow\Gamma$ satisfacible. Esa es la exigencia de **completitud** o de construcción de modelos del próximo Capítulo 11, y no puede obtenerse por invertir una implicación ya demostrada.


## 10.10. Diagrama de los niveles de justificación

La secuencia de dependencias reales es

$$
\underbrace{\mathrm{Ax}^{0}_\tau\text{ válidos}}_{\S\S10.1\text{–}10.3}
\quad+\quad
\underbrace{\forall\bar x\text{ preserva validez}}_{\S10.5}
\quad\Longrightarrow\quad
\underbrace{\mathrm{Ax}_{\mathsf H_\tau^{=}}\text{ válidos}}_{\S10.6}.
$$

Y, con $\mathrm{MP}$ semánticamente preservativo (§10.4), la inducción sobre una derivación (§9.9) obtiene $\vdash\Rightarrow\models$ (§10.7). Esta flecha **no** fue utilizada como premisa de ningún nodo del Capítulo 9: se ha cerrado la interfaz entre dos construcciones independientes, no un razonamiento circular.

## 10.11. Controles de interpretación y condiciones laterales

**No confundir consecuencia local y global.** La primera cuantifica sobre todas las parejas estructura–asignación que satisfacen conjuntamente las premisas. La segunda considera una estructura que satisface todas las premisas bajo toda asignación. El teorema demostrado es primariamente **local**, por lo que es más informativo para fórmulas abiertas.

**No omitir `FreeFor`.** Los casos `Q1`, `Q2`, `E2` sólo se reconocen como axiomas si las sustituciones literales están definidas con las condiciones de ausencia de captura del Capítulo 6. La prueba de verdad de esas instancias pasa explícitamente por el lema semántico §8.11.

**No agregar una regla de generalización incondicional.** El cálculo del Capítulo 9 sólo tiene `MP` como regla primitiva. La transformación $\Gamma\vdash\varphi\Rightarrow\Gamma\vdash\forall x\varphi$ vale con $x\notin\operatorname{FV}(\Gamma)$ (o para una derivación que utilice sólo premisas independientes de $x$). Añadir la versión sin restricción invalidaría la corrección local.

**No importar AC.** Toda prueba se desarrolla con operaciones de sustitución de términos, actualización de asignaciones y un número finito de líneas. Las afirmaciones sobre todas las estructuras son esquemas de cuantificación metateórica, no un conjunto universal de modelos.

**No confundir corrección y completitud.** El contraejemplo permite negar una deducción por su falsedad semántica. La ausencia de contramodelos no ha sido demostrada suficiente para derivabilidad; esa dirección queda abierta.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 9](capitulo-09.md) · [Capítulo 11 →](capitulo-11.md)


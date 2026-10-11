---
title: Capítulo 9 — Sistemas deductivos y teorías
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
content-id: MA-BCH-0211
content-type: book-chapter
source-id: TLOG-CH09-0001
prerequisites:
- MA-BCH-0205
- MA-BCH-0207
- MA-BCH-0208
- MA-BCH-0210
related:
- MA-BOK-0014
source-sha256: 0873e65cb21dd5c29774b06e315c8fcf672f4d013236ec0069e6b48ceb5954f3
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 8](capitulo-08.md) · [Capítulo 10 →](capitulo-10.md)

## 9.0. De la consecuencia semántica a la derivación formal

El Capítulo 8 definió, para conjuntos arbitrarios de fórmulas, la relación metateórica de consecuencia **local** $\Gamma\models_\tau\varphi$: toda estructura y toda asignación que satisfacen simultáneamente las premisas satisfacen también la conclusión. Esa noción no constituye por sí misma un procedimiento de prueba. El presente capítulo construye una relación distinta, $\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi$, cuya definición únicamente exige la existencia de una secuencia **finita** de fórmulas, autorizadas por axiomas o por reglas formales.

Trabajamos sobre las signaturas unisortadas $\tau$ de §5.2, con funciones y relaciones de aridad finita, incluidas las aridades nulas, igualdad lógica $\doteq$, los cinco conectivos primitivos $\neg,\land,\lor,\to,\leftrightarrow$ y **ambos cuantificadores primitivos** $\forall,\exists$. En la metateoría rige $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ clásica, sin axioma de elección tácito. No se ha elegido una estructura ni una interpretación para decidir qué secuencias cuentan como demostraciones.

### Cotejo bibliográfico y decisión de cálculo

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª edición (2001), cap. 2, §2.4, pp. **109–117**: derivaciones finitas, modus ponens, axiomas universalmente generalizados y separación entre deducción y verdad; `proof-model / countercheck`.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª edición (2010), cap. 3, §3.6, pp. **121–124**: cálculo hilbertiano completo con clausuras universales de los esquemas, modus ponens único, y generalización demostrada por inducción sobre derivaciones; `proof-model / countercheck`.

Ambas fuentes permiten adoptar **MP como única regla primitiva**, al incluir desde el comienzo las clausuras universales de todos los axiomas. Enderton trabaja con un conjunto de tautologías y una selección de esquemas para $\neg,\to,\forall,=$; Rautenberg parte de $\neg,\land,\forall,=$. TLOG reconstruye una **base propia** ajustada a su gramática de cinco conectivos y dos cuantificadores. El resultado de esta sección no importa como axioma la consecuencia semántica, ni presupone corrección, completitud o decidibilidad para signaturas arbitrarias.

## 9.1. Identidad del sistema deductivo

### Convención 9.1.1 — Cálculo $\mathsf H_\tau^{=}$ {#tlog-cnv-00011}

Fijada $\tau$, llamamos $\mathsf H_\tau^{=}$ al sistema deductivo clásico de primer orden **con igualdad** sobre el conjunto de fórmulas $\operatorname{Fm}_\tau$. Sus datos son: (a) instancias de esquemas axiomáticos proposicionales, cuantificacionales y de igualdad; (b) todas sus clausuras universales finitas; (c) la única regla primitiva $\mathrm{MP}$; y (d) derivaciones de longitud finita desde un conjunto arbitrario de premisas.

El superíndice $=$ identifica la igualdad *lógica*; no denota un predicado binario añadido a $R_2$. Este cálculo no es $\mathsf H_{\mathrm{CPL}}$ del Capítulo 3: ambos comparten ciertos **patrones** proposicionales, pero sus universos de fórmulas y sus teoremas son distintos. Una regla admisible se distinguirá de una regla primitiva y un esquema de axiomas de cada una de sus instancias.

## 9.2. Núcleo axiomático proposicional sobre fórmulas de primer orden

### Esquema axiomático 9.2.1 — Levantamiento de `H1`–`H12` {#tlog-axm-00002}

Sea $\operatorname{Ax}^{\mathrm{prop}}_\tau$ el conjunto de **todas** las instancias de los doce esquemas `H1`–`H12` de §3.2, esta vez con metavariables $\alpha,\beta,\gamma$ que recorren **$\operatorname{Fm}_\tau$**, y no sólo $\operatorname{Fm}_{\mathrm{CPL}}$. Se conservan exactamente sus formas y las cinco conectivas primitivas. En particular, `H1` y `H2` se leen

$$
\alpha\to(\beta\to\alpha),\qquad
(\alpha\to(\beta\to\gamma))\to
((\alpha\to\beta)\to(\alpha\to\gamma)),
$$

y `H3` mantiene $(\neg\beta\to\neg\alpha)\to(\alpha\to\beta)$. Los esquemas `H4`–`H12` rigen $\land,\lor,\leftrightarrow$ exactamente como en §3.2. El pasaje de $\mathrm{CPL}$ a $\operatorname{Fm}_\tau$ es un **cambio del dominio de las metavariables**, no una identificación de sistemas objetos ni la afirmación de que el cálculo proposicional demuestra automáticamente teoremas de primer orden.

Como las doce formas utilizan sólo un número finito de metavariables, el conjunto de sus instancias existe en ZF por sustitución finita de fórmulas dentro de $\operatorname{Fm}_\tau$. No se necesita elegir simultáneamente valores de metavariables en una familia arbitraria de lenguajes.

## 9.3. Esquemas cuantificacionales

### Esquema axiomático 9.3.1 — Cuantificadores primitivos y sustitución segura {#tlog-axm-00003}

Para $\varphi,\psi\in\operatorname{Fm}_\tau$, $x\in X$ y $t\in\operatorname{Tm}_\tau$, fijamos las siguientes **familias de instancias**. Toda sustitución indicada por $[t/x]_{\mathrm{lit}}$ exige expresamente $\operatorname{FreeFor}_\tau(t,x,\varphi)$ y, cuando aparece, afecta sólo a las ocurrencias libres originales:

$$
\begin{aligned}
\text{(Q1)} &\forall x\,\varphi\to\varphi[t/x]_{\mathrm{lit}},\\
\text{(Q2)} &\varphi[t/x]_{\mathrm{lit}}\to\exists x\,\varphi,\\
\text{(Q3)} &\forall x(\varphi\to\psi)\to
  (\forall x\,\varphi\to\forall x\,\psi),\\
\text{(Q4)} &\varphi\to\forall x\,\varphi
  \qquad (x\notin\operatorname{FV}_\tau(\varphi)),\\
\text{(Q5)} &\exists x\,\varphi\leftrightarrow\neg\forall x\,\neg\varphi.
\end{aligned}
$$

Para `Q1` y `Q2`, si la condición `FreeFor` no se cumple, la cadena informal correspondiente **no es una instancia** del esquema. `Q3` no impone una condición sobre variables libres: expresa cómo distribuye $\forall$ respecto de una implicación. `Q4` requiere $x\notin\operatorname{FV}(\varphi)$, no sólo que $x$ sea distinto de una variable escrita en la fórmula. `Q5` relaciona dos **fórmulas objeto distintas**, pues $\exists$ continúa siendo primitivo.

La unión de estas familias, $\operatorname{Ax}^{\mathrm q}_\tau$, es un **conjunto** de fórmulas de la signatura fija. No se postula todavía la regla de inferencia $\varphi/\forall x\varphi$ desde hipótesis arbitrarias; dicha generalización sería incompatible con la consecuencia **local** establecida en §8.26.

## 9.4. Esquemas de igualdad lógica

### Esquema axiomático 9.4.1 — Reflexividad y sustitución de iguales {#tlog-axm-00004}

Para términos $t,u\in\operatorname{Tm}_\tau$, variables $x\in X$ y fórmulas $\varphi\in\operatorname{Fm}_\tau$, sean instancias axiomáticas de igualdad:

$$
\tag{E1} t\doteq t,
$$

$$
\tag{E2}
(t\doteq u)\to
\bigl(\varphi[t/x]_{\mathrm{lit}}\to
\varphi[u/x]_{\mathrm{lit}}\bigr),
$$

bajo las condiciones conjuntas
$\operatorname{FreeFor}_\tau(t,x,\varphi)$ y
$\operatorname{FreeFor}_\tau(u,x,\varphi)$. El conjunto de instancias se denota $\operatorname{Ax}^{=}_\tau$. El esquema `E2` expresa **sustitución uniforme y libre de captura** en fórmulas arbitrarias, y no se identifica con la regla metateórica de reemplazar una cadena cualquiera por otra. Se permite $t=u$ o que $x\notin\operatorname{FV}(\varphi)$; en esos casos pueden producirse instancias redundantes, sin defecto lógico.

La reflexividad de `E1` y el carácter congruencial de `E2` son **datos sintácticos** del cálculo. La demostración metateórica de su validez bajo toda estructura pertenece al Capítulo 10, con las cláusulas de satisfacción y sustitución del Capítulo 8. La simetría, transitividad y demás reglas derivadas de igualdad no se elevan a primitivas por conveniencia editorial; se reconstruirán como resultados deductivos.

## 9.5. El conjunto de axiomas y las clausuras universales

### Definición 9.5.1 — Axiomas básicos y generalizaciones finitas {#tlog-def-00052}

Sea

$$
\operatorname{Ax}^0_\tau :=
\operatorname{Ax}^{\mathrm{prop}}_\tau
\cup\operatorname{Ax}^{\mathrm q}_\tau
\cup\operatorname{Ax}^{=}_\tau.
$$

Para una lista finita $\bar x=(x_1,\ldots,x_n)\in X^{<\omega}$, definimos la **clausura prefija** $\forall\bar x\,\theta$ como $\forall x_1\cdots\forall x_n\theta$. Cuando $n=0$, se toma $\forall()\,\theta=\theta$. El conjunto completo de axiomas del cálculo es

$$
\boxed{
\operatorname{Ax}_{\mathsf H_\tau^{=}}=
\{\forall\bar x\,\theta:
 \bar x\in X^{<\omega},\ \theta\in\operatorname{Ax}^0_\tau\}.}
$$

En particular, si $\theta\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$, entonces $\forall x\theta\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$ **para todo** $x\in X$, porque basta anteponer $x$ a su prefijo finito. No se necesita que $x$ sea libre ni que no lo sea. **Esta propiedad de cierre pertenece a la definición de axioma**, no constituye todavía una regla que permita generalizar premisas.

**Existencia conjuntista.** $X^{<\omega}$ y $\operatorname{Fm}_\tau$ son conjuntos. La operación que antepone una lista finita de cuantificadores a una fórmula se define por recursión finita; su imagen sobre $X^{<\omega}\times\operatorname{Ax}^0_\tau$ es un conjunto por reemplazo. Alternativamente, se separa de $\operatorname{Fm}_\tau$ el subconjunto que admite tal prefijo. Ninguno de estos procedimientos requiere AC. Para signaturas arbitrarias no se afirma una prueba general de **decidibilidad efectiva** de pertenencia al conjunto de axiomas.

## 9.6. Regla primitiva de inferencia

### Regla 9.6.1 — Modus ponens de primer orden {#tlog-rul-00002}

La **única regla primitiva** del cálculo $\mathsf H_\tau^{=}$ es

$$
\frac{\alpha\qquad\alpha\to\beta}{\beta}\qquad(\mathrm{MP}),
\quad\alpha,\beta\in\operatorname{Fm}_\tau.
$$

Es una regla sobre **fórmulas objeto**, no una implicación entre juicios de satisfacción. No descarga premisas, no cuantifica variables y no exige una condición lateral de frescura. En particular, el esquema proposicional $\alpha\to(\beta\to\alpha)$ y las instancias universalmente cerradas son **axiomas**, no aplicaciones de $\mathrm{MP}$.

## 9.7. Derivaciones finitas

### Definición 9.7.1 — Derivación desde un conjunto de fórmulas {#tlog-def-00053}

Sea $\Gamma\subseteq\operatorname{Fm}_\tau$. Una **derivación desde $\Gamma$** es una secuencia finita **no vacía**

$$
\Pi=(\varphi_0,\ldots,\varphi_n),\qquad n\in\omega,
$$

de fórmulas de $\operatorname{Fm}_\tau$, tal que para todo índice $k\le n$ se verifica por lo menos una de las tres cláusulas siguientes:

1. **Premisa:** $\varphi_k\in\Gamma$.
2. **Axioma lógico:** $\varphi_k\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$.
3. **Inferencia:** existen $i,j<k$ tales que $\varphi_j=(\varphi_i\to\varphi_k)$, y la línea $k$ resulta por $\mathrm{MP}$.

La conclusión es $\varphi_n$, la longitud de $\Pi$ es $n+1$, y los índices de las dos premisas de una aplicación de $\mathrm{MP}$ deben ser **estrictamente anteriores** al de la conclusión. La cláusula de axioma permite fórmulas que contienen cuantificadores, incluida una clausura universal de un axioma básico; no autoriza insertar generalizaciones arbitrarias de una premisa.

El conjunto de todas las secuencias finitas sobre $\operatorname{Fm}_\tau$ existe en ZF, y el predicado «$\Pi$ es derivación desde $\Gamma$» es una condición definida sobre él. Por separación, también el conjunto de derivaciones desde $\Gamma$ existe. Este enunciado de **existencia conjuntista** no entraña que la validez de la condición sea decidible bajo toda codificación imaginable de una signatura.

## 9.8. Derivabilidad, teoremas y notación

### Definición 9.8.1 — Derivabilidad en $\mathsf H_\tau^{=}$ {#tlog-def-00054}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\varphi\in\operatorname{Fm}_\tau$, escribimos

$$
\boxed{\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi}
$$

si existe una derivación finita desde $\Gamma$ cuya última línea sea $\varphi$. Si $\Gamma=\varnothing$, escribimos $\vdash_{\mathsf H_\tau^{=}}\varphi$ y llamamos a $\varphi$ **teorema lógico del cálculo**. La relación $\nvdash$ significa negación metateórica de la existencia de tal secuencia. No se presupone aquí ninguna conexión entre $\vdash_{\mathsf H_\tau^{=}}$ y $\models_\tau$.

La cuantificación de la definición es sobre un **conjunto** de secuencias finitas y no sobre una clase de todas las estructuras. Por ello, para una $\tau$ fija, la relación de derivabilidad constituye una relación conjuntista sobre $\mathcal P(\operatorname{Fm}_\tau)\times\operatorname{Fm}_\tau$.

## 9.9. Inducción sobre derivaciones

### Metateorema 9.9.1 — Principio de inducción deductiva {#tlog-mth-00034}

**Enunciado.** Fijados $\Gamma\subseteq\operatorname{Fm}_\tau$ y un predicado metateórico $P$ sobre fórmulas, supongamos:

1. $P(\gamma)$ para toda $\gamma\in\Gamma$;
2. $P(\theta)$ para toda $\theta\in\operatorname{Ax}_{\mathsf H_\tau^{=}}$;
3. $P(\alpha)\land P(\alpha\to\beta)\Rightarrow P(\beta)$ para todas $\alpha,\beta\in\operatorname{Fm}_\tau$.

Entonces, para toda $\varphi$,

$$
\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi
\quad\Longrightarrow\quad P(\varphi).
$$

**Demostración.** Sea $\Pi=(\varphi_0,\ldots,\varphi_n)$ una derivación dada. Por inducción ordinaria en $k\le n$, probamos $P(\varphi_k)$. Si $\varphi_k\in\Gamma$, se usa (1); si es una instancia axiomática, se usa (2). En el caso de inferencia, la definición proporciona $i,j<k$ con $\varphi_j=\varphi_i\to\varphi_k$. Las dos hipótesis inductivas y (3) entregan $P(\varphi_k)$. En particular $P(\varphi_n)$. No se presupone una regla de inferencia por generalización: sólo se analizan las tres cláusulas realmente presentes en el cálculo. $\square$

Este principio se aplicará a propiedades de **derivaciones**, no directamente a las formas de construcción de una fórmula. Es una inducción sobre la longitud de una prueba, distinta de los metateoremas de inducción estructural del Capítulo 5.

## 9.10. Propiedades estructurales de la derivabilidad

### Proposición 9.10.1 — Premisa, axioma, MP, monotonía, finitariedad y corte {#tlog-pro-00020}

Para $\Gamma,\Delta\subseteq\operatorname{Fm}_\tau$ y fórmulas apropiadas, se tienen las seis propiedades siguientes:

1. **Premisa:** $\varphi\in\Gamma\Rightarrow\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi$.
2. **Axioma:** $\theta\in\operatorname{Ax}_{\mathsf H_\tau^{=}}\Rightarrow\vdash_{\mathsf H_\tau^{=}}\theta$.
3. **MP:** de $\Gamma\vdash\alpha$ y $\Gamma\vdash(\alpha\to\beta)$ se sigue $\Gamma\vdash\beta$.
4. **Monotonía:** $\Gamma\subseteq\Delta$ y $\Gamma\vdash\varphi\Rightarrow\Delta\vdash\varphi$.
5. **Finitariedad:** $\Gamma\vdash\varphi\Rightarrow\exists\Gamma_0\subseteq\Gamma$ finito con $\Gamma_0\vdash\varphi$.
6. **Corte:** si $\Delta\vdash\varphi$ y $(\forall\delta\in\Delta)\;\Gamma\vdash\delta$, entonces $\Gamma\vdash\varphi$.

En (3)–(6), las abreviaciones $\vdash$ mantienen el subíndice fijo $\mathsf H_\tau^{=}$.

**Demostración.** (1) y (2) tienen una prueba de una línea; (3) se obtiene concatenando las dos pruebas disponibles y agregando una aplicación de $\mathrm{MP}$. (4) conserva cada línea-premisa, pues $\Gamma\subseteq\Delta$; ninguna otra cláusula cambia. Para (5), basta reunir las fórmulas de $\Gamma$ usadas efectivamente como premisas en la prueba fija: son finitas y la misma secuencia demuestra la conclusión desde ellas.

Para (6), una prueba fija $\Pi$ de $\varphi$ desde $\Delta$ utiliza sólo un número **finito** de premisas $\delta_1,\ldots,\delta_m\in\Delta$. Para cada una existe una prueba desde $\Gamma$; una elección **finita** de esas pruebas está disponible en ZF, sin AC. Insertamos dichas derivaciones antes de $\Pi$ y reemplazamos cada uso de $\delta_i$ como premisa por la aparición ya demostrada de la misma fórmula. Los índices de las aplicaciones de $\mathrm{MP}$ se desplazan manteniendo su precedencia estricta. El resultado es una derivación finita desde $\Gamma$ que termina en $\varphi$. Si $m=0$, se utiliza directamente $\Pi$. $\square$

La finitariedad demostrada es **sintáctica**; no implica aún compacidad semántica de primer orden. Del mismo modo, el corte es una operación sobre pruebas, no una sustitución de la demostración futura de corrección.

## 9.11. Generalización controlada como regla admisible

### Metateorema 9.11.1 — Generalización bajo premisas independientes {#tlog-mth-00035}

**Enunciado.** Si $\Gamma\subseteq\operatorname{Fm}_\tau$, $x\in X$, $x\notin\operatorname{FV}_\tau(\Gamma):=\bigcup_{\gamma\in\Gamma}\operatorname{FV}_\tau(\gamma)$, y $\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi$, entonces

$$
\boxed{\Gamma\vdash_{\mathsf H_\tau^{=}}\forall x\,\varphi.}
$$

En particular $\vdash_{\mathsf H_\tau^{=}}\varphi\Rightarrow\vdash_{\mathsf H_\tau^{=}}\forall x\varphi$ para cualquier variable $x$, al tomar $\Gamma=\varnothing$. Esta última propiedad es **admisible para teoremas**, no una regla de generalización desde premisas cualesquiera.

**Demostración.** Sea $\Pi=(\varphi_0,\ldots,\varphi_n)$ una derivación de $\varphi$ desde $\Gamma$. Inducimos en $k\le n$ la afirmación $\Gamma\vdash\forall x\varphi_k$. Si $\varphi_k$ es axioma, $\forall x\varphi_k$ es también axioma, por la clausura de §9.5; hay una prueba de una línea. Si es premisa $\gamma\in\Gamma$, la hipótesis lateral garantiza $x\notin\operatorname{FV}(\gamma)$, por lo que `Q4` proporciona el axioma $\gamma\to\forall x\gamma$. Junto con la prueba de una línea de $\gamma$, $\mathrm{MP}$ produce $\forall x\gamma$.

Si $\varphi_k=\beta$ proviene por $\mathrm{MP}$ de líneas anteriores $\alpha$ y $\alpha\to\beta$, la hipótesis inductiva da pruebas de $\forall x\alpha$ y de $\forall x(\alpha\to\beta)$, ambas desde $\Gamma$. Instanciamos `Q3`:

$$
\forall x(\alpha\to\beta)\to
(\forall x\alpha\to\forall x\beta).
$$

Concatenando las dos pruebas y esta instancia y aplicando dos veces $\mathrm{MP}$, obtenemos una prueba de $\forall x\beta$ desde $\Gamma$. Es una transformación finita de derivaciones; no se añade ninguna regla primitiva y concluye la inducción. $\square$

**Refinamiento por soporte finito.** Por la finitariedad de §9.10, basta disponer de **alguna** demostración de $\varphi$ que utilice un conjunto finito de premisas $\Gamma_0\subseteq\Gamma$ con $x\notin\operatorname{FV}(\Gamma_0)$. Se aplica el teorema a $\Gamma_0$ y después la monotonía. Esto sigue siendo una regla **controlada**: no autoriza generalizar una fórmula derivada con dependencia efectiva de $x$.

## 9.12. Tres controles de lectura

**Una premisa abierta no autoriza generalización.** En la signatura con predicado unario $P$, tomemos $A=\{0,1\}$, $P^{\mathfrak A}=\{0\}$ y $s(x)=0$. Se tiene $\mathfrak A,s\models P(x)$, pero $\mathfrak A,s\not\models\forall x\,P(x)$. Por ello una regla **incondicional** «de $\Gamma\vdash\varphi$ inferir $\Gamma\vdash\forall x\varphi$» no sería compatible con la consecuencia local del Capítulo 8. Este ejemplo no constituye una prueba de corrección o incorrección del sistema que estamos construyendo: explica por qué se ha restringido la regla **admisible**.

**La igualdad es lógica, no un símbolo relacional cualquiera.** Para una función unaria $f$, términos $t,u$ y fórmula $\chi(z):=f(z)\doteq f(t)$, el esquema `E2` autoriza, cuando sus condiciones de sustitución se cumplen,
$(t\doteq u)\to(\chi[t/z]\to\chi[u/z])$. A diferencia de una intuición de «reemplazar caracteres», cada paso se rige por una instancia con sustitución definida.

**Un predicado nulario también puede figurar en un axioma proposicional.** Si $R\in R_0$, la instancia `H1` con $\alpha=R()$ y $\beta=(x\doteq x)$ es $R()\to((x\doteq x)\to R())$. Los valores de esos átomos no intervienen en su reconocimiento como instancia de `H1`.

## 9.13. Cierre local del microtramo

La definición de $\vdash_{\mathsf H_\tau^{=}}$ se obtuvo **sin** utilizar $\models_\tau$. Se redactaron las doce familias proposicionales levantadas, cinco esquemas cuantificacionales, dos de igualdad y sus clausuras universales, una regla primitiva y demostraciones finitas de inducción, propiedades estructurales y generalización admisible. Las pruebas son metateóricas; no se importaron los teoremas de corrección/completitud de los manuales y no se atribuye verificación Lean.

Permanece abierto en el Capítulo 9 el estudio deductivo del teorema de deducción, de reglas derivadas de igualdad y cuantificadores, y la construcción de las teorías como extensiones axiomáticas del cálculo. Los Capítulos 10 y 11 permanecen reservados para corrección y completitud/compacidad, respectivamente. La metateoría continúa siendo ZF sin axioma de elección.

```text
TLOG-CH09-M01 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH09-0001 = PARTIAL-CLOSURE / NOT CLOSED [estado histórico tras M01]
chapter 9 closed mathematical nodes = 11
TLOG issued/registered/closed = 155/155 [histórico tras M01]
DAG = 155 nodes / 406 direct edges / acyclic PASS
formalization candidates = 44
Lean compiled/verified = 0
external interfaces = 0
chapters closed = 9/24 (37.5%)
PART I = CLOSED / PASS
PART II = OPEN
```

**Siguiente microtramo:** `TLOG-CH09-M02 — Teorema de deducción, reglas derivadas, igualdad y teorías sintácticas`.

### Vector gráfico de progreso

```text
LOCAL  CH09-M01 ██████████ 11/11 (100 %, auditoría matemática del microtramo)
GLOBAL TLOG     █████████░░░░░░░░░░░░░░░ 9/24 capítulos (37,5 %)
```

<!-- El estado histórico de la etapa de redacción de M01 se conserva en §9.13; la auditoría M01 certifica su persistencia tras el cierre del capítulo. -->

## 9.14. El puente estrictamente sintáctico con el cálculo proposicional

### Lema 9.14.1 — Levantamiento de demostraciones proposicionales {#tlog-lem-00023}

**Enunciado.** Sea $h:\mathrm{PV}\to\operatorname{Fm}_\tau$ cualquier aplicación de las variables proposicionales a fórmulas de primer orden, extendida de manera única a las cinco conectivas. Si $\Delta\vdash_{\mathsf H_{\mathrm{CPL}}}\theta$, entonces

$$
\boxed{h[\Delta]\vdash_{\mathsf H_\tau^{=}}h(\theta).}
$$

En particular, **toda instancia de una tautología proposicional** obtenida al reemplazar proposiciones atómicas por fórmulas arbitrarias de primer orden es un teorema del cálculo $\mathsf H_\tau^{=}$, ya que la completitud proposicional [TLOG-MTH-00013](capitulo-04.md#tlog-mth-00013) permite disponer de una prueba de su esquema en $\mathsf H_{\mathrm{CPL}}$. Esta afirmación es *proposicional*: no declara demostrada la completitud de primer orden.

**Demostración.** Tomemos una prueba proposicional finita $(\theta_0,\ldots,\theta_n)$. La imagen $(h(\theta_0),\ldots,h(\theta_n))$ es también una sucesión finita. Una línea-premisa cae en $h[\Delta]$; una instancia de cualquiera de los doce esquemas `H1`–`H12` se transforma en la correspondiente instancia de $\operatorname{Ax}^{\mathrm{prop}}_\tau$, incluida entre los axiomas por §9.5; y una aplicación de modus ponens se conserva porque $h(\alpha\to\beta)=h(\alpha)\to h(\beta)$. Por inducción sobre las líneas se obtiene la derivación requerida. Si $\theta$ es tautología, su derivación desde $\varnothing$ proviene del capítulo 4; aplicamos la primera parte con $\Delta=\varnothing$. Sólo se transforman secuencias sintácticas finitas, sin interpretar estructuras ni usar elección. $\square$

Este lema autoriza usar, **con constancia de la instancia**, tautologías implicativas clásicas y reglas como introducción/eliminación de $\land$, doble negación, contraposición, silogismo hipotético o explosión. No autoriza aplicar una regla cuantificacional como si fuese una tautología.

## 9.15. El teorema de deducción de primer orden

### Metateorema 9.15.1 — Descarga de una premisa para un cálculo con `MP` {#tlog-mth-00036}

**Enunciado.** Para cualquier $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\alpha,\beta\in\operatorname{Fm}_\tau$,

$$
\boxed{\Gamma\cup\{\alpha\}\vdash_{\mathsf H_\tau^{=}}\beta
\quad\Longleftrightarrow\quad
\Gamma\vdash_{\mathsf H_\tau^{=}}(\alpha\to\beta).}
$$

No aparece una condición sobre las variables libres de $\alpha$, porque **la única regla primitiva de la derivación es `MP`** y la generalización se ha incorporado como propiedad de *axiomas*, no como regla aplicable a hipótesis.

**Demostración.** Para la implicación directa, fijemos una prueba $\Pi=(\psi_0,\ldots,\psi_n)$ de $\beta$ desde $\Gamma\cup\{\alpha\}$. Por inducción en su índice construimos pruebas desde $\Gamma$ de $\alpha\to\psi_k$. Si $\psi_k=\alpha$, utilizamos la tautología proposicional $\alpha\to\alpha$, cuyo levantamiento está disponible en §9.14. Si $\psi_k\in\Gamma$ o es axioma lógico, tenemos una prueba de una línea de $\psi_k$, a la que añadimos `H1`, $\psi_k\to(\alpha\to\psi_k)$, y una aplicación de `MP`. Finalmente, si $\psi_k$ resulta por `MP` de $\chi$ y $\chi\to\psi_k$ en posiciones anteriores, la inducción proporciona $\alpha\to\chi$ y $\alpha\to(\chi\to\psi_k)$. La instancia de `H2`

$$
(\alpha\to(\chi\to\psi_k))\to
((\alpha\to\chi)\to(\alpha\to\psi_k))
$$

permite inferir $\alpha\to\psi_k$ mediante dos aplicaciones de `MP`. En $k=n$ obtenemos lo buscado. Para la implicación inversa, de $\Gamma\vdash\alpha\to\beta$ y de la premisa $\alpha$ se obtiene $\beta$ por `MP`, tras monotonía. $\square$

**Control de alcance.** El teorema descarga **una premisa formal**. No permite, por sí solo, introducir cuantificadores arbitrarios en pruebas que dependen de esa premisa. La diferencia entre el teorema de deducción irrestricto de este cálculo y la generalización lateralmente restringida de §9.11 es intencional.

## 9.16. Reglas derivadas proposicionales

### Proposición 9.16.1 — Conjunción, disyunción, bicondicional y reducción clásica {#tlog-pro-00021}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$, $\alpha,\beta,\gamma\in\operatorname{Fm}_\tau$, son **reglas admisibles**:

1. De $\Gamma\vdash\alpha$ y $\Gamma\vdash\beta$ se obtiene $\Gamma\vdash\alpha\land\beta$; de $\Gamma\vdash\alpha\land\beta$, cada conjuntando.
2. De $\Gamma\vdash\alpha$ se obtiene $\Gamma\vdash\alpha\lor\beta$, y simétricamente; de $\Gamma\vdash\alpha\to\gamma$, $\Gamma\vdash\beta\to\gamma$ y $\Gamma\vdash\alpha\lor\beta$, se obtiene $\Gamma\vdash\gamma$.
3. De $\Gamma\vdash\alpha\leftrightarrow\beta$ se obtienen las dos implicaciones, y viceversa.
4. Se admiten $\Gamma\vdash\neg\neg\alpha\Rightarrow\Gamma\vdash\alpha$, contraposición, silogismo hipotético y $\Gamma\vdash\alpha,\neg\alpha\Rightarrow\Gamma\vdash\gamma$.

**Demostración.** Cada regla sigue de una instancia concreta de los esquemas `H4`–`H12` y `H1`–`H3`, o de una tautología proposicional levantada por §9.14. Por ejemplo, $\alpha\to(\beta\to\alpha\land\beta)$ es `H6`: dos usos de `MP` dan (1); $(\alpha\to\gamma)\to((\beta\to\gamma)\to((\alpha\lor\beta)\to\gamma))$ es `H9` y tres usos dan (2). La regla de explosión proviene de la tautología $\alpha\to(\neg\alpha\to\gamma)$, y la contraposición de $(\alpha\to\beta)\to(\neg\beta\to\neg\alpha)$. Todas poseen pruebas puramente proposicionales por §9.14 y el Capítulo 4. Concatenamos las demostraciones y aplicamos `MP` el número finito de veces indicado. $\square$

## 9.17. La igualdad funciona deductivamente como identidad

### Proposición 9.17.1 — Simetría, transitividad y congruencia {#tlog-pro-00022}

Para términos $t,u,v$ se derivan:

$$
\begin{gathered}
\vdash t\doteq t,\\
\vdash (t\doteq u)\to(u\doteq t),\\
\vdash (t\doteq u)\to((u\doteq v)\to(t\doteq v)).
\end{gathered}
$$

Asimismo, dada una función $f\in F_n$, para $n\ge1$, y una relación $R\in R_n$, la igualdad de argumentos permite derivar las correspondientes congruencias:

$$
\{t_i\doteq u_i:1\le i\le n\}\ \vdash\ 
 f(t_1,\ldots,t_n)\doteq f(u_1,\ldots,u_n),
$$

$$
\{t_i\doteq u_i:1\le i\le n\}\cup\{R(t_1,\ldots,t_n)\}
\ \vdash\ R(u_1,\ldots,u_n).
$$

Para $n=0$, no hay hipótesis de igualdad: la expresión funcional es el mismo término constante y el predicado nulario es el mismo átomo, respectivamente.

**Demostración.** La reflexividad es `E1`. Para la simetría, tomemos una variable $z$ ausente de $t,u$ y la fórmula atómica $\chi(z):=z\doteq t$. La instancia de `E2` es

$$
(t\doteq u)\to((t\doteq t)\to(u\doteq t)).
$$

Por `E1` y las reglas proposicionales se obtiene la implicación de simetría. Para la transitividad, escogemos $z$ ausente de $t,u,v$ y $\chi(z):=t\doteq z$; `E2` produce

$$
(u\doteq v)\to((t\doteq u)\to(t\doteq v)).
$$

Se intercambia el orden de las hipótesis mediante una tautología de implicación, obteniendo la forma enunciada. Para las congruencias, sustituyamos **un argumento por vez**. Si $\bar w$ es la lista actual de argumentos y queremos cambiar su $i$-ésimo término $t_i$ a $u_i$, elegimos $z$ ausente de todos los términos y consideramos $\chi(z):=f(w_1,\ldots,w_{i-1},z,w_{i+1},\ldots,w_n)\doteq f(\bar w)$. `E2` y reflexividad prueban la igualdad de los dos valores de función con el orden eventualmente invertido, que corregimos por simetría. La relación se trata con $\chi(z):=R(w_1,\ldots,w_{i-1},z,w_{i+1},\ldots,w_n)$. Repetimos el paso finitas veces, y en el caso funcional encadenamos los resultados usando transitividad. Los reemplazos son `FreeFor` porque las fórmulas auxiliares son **atómicas** y $z$ es fresca; no hay cuantificadores que capturen variables. No se generaliza silenciosamente el esquema `E2` a un reemplazo textual arbitrario. $\square$

## 9.18. Reglas cuantificacionales derivadas

### Proposición 9.18.1 — Particularización, introducción existencial y dualidad {#tlog-pro-00023}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\operatorname{FreeFor}_\tau(t,x,\varphi)$:

$$
\begin{aligned}
\Gamma\vdash\forall x\,\varphi&\Longrightarrow\Gamma\vdash\varphi[t/x]_{\mathrm{lit}},\\
\Gamma\vdash\varphi[t/x]_{\mathrm{lit}}&\Longrightarrow\Gamma\vdash\exists x\,\varphi.
\end{aligned}
$$

Además, bajo la condición $x\notin\operatorname{FV}(\Gamma)$, se tiene $\Gamma\vdash\varphi\Rightarrow\Gamma\vdash\forall x\varphi$. También es admisible la **eliminación existencial controlada**: si $\Gamma\vdash\exists x\varphi$, $\Gamma\vdash\varphi\to\psi$ y $x\notin\operatorname{FV}(\Gamma)\cup\operatorname{FV}(\psi)$, entonces $\Gamma\vdash\psi$. Para toda $\varphi$, sin condiciones laterales, son teoremas las dualidades

$$
\vdash(\exists x\,\varphi\leftrightarrow\neg\forall x\,\neg\varphi),
\qquad
\vdash(\forall x\,\varphi\leftrightarrow\neg\exists x\,\neg\varphi).
$$

**Demostración.** Los dos primeros resultados son `Q1` y `Q2` seguidos de `MP`; el tercero es el metateorema 9.11.1. La primera dualidad es `Q5`. Para la segunda, sustituimos $\varphi$ por $\neg\varphi$ en `Q5`: $\exists x\neg\varphi\leftrightarrow\neg\forall x\neg\neg\varphi$. Por equivalencia proposicional entre $\varphi$ y $\neg\neg\varphi$, y por la congruencia de $\forall$ respecto de implicaciones teoremáticas derivada de `Q3` y la generalización para teoremas, se obtiene $\forall x\neg\neg\varphi\leftrightarrow\forall x\varphi$. Finalmente, las leyes clásicas de negación y sustitución de equivalentes (9.16) concluyen la segunda dualidad. Cada aplicación de la congruencia cuantificacional se efectúa sobre un **teorema**; por eso ninguna variable queda libre en premisas utilizadas indebidamente. Para la eliminación existencial, de $\Gamma\vdash\varphi\to\psi$ la contraposición proposicional da $\Gamma\vdash\neg\psi\to\neg\varphi$. Puesto que $x\notin\operatorname{FV}(\Gamma)$, se puede generalizar esta implicación a $\forall x(\neg\psi\to\neg\varphi)$. Por `Q3` y `Q4` (ya que $x\notin\operatorname{FV}(\psi)$) se deduce $\Gamma\vdash\neg\psi\to\forall x\neg\varphi$. `Q5` y la hipótesis $\Gamma\vdash\exists x\varphi$ proporcionan $\Gamma\vdash\neg\forall x\neg\varphi$; mediante contraposición y doble negación clásicas concluye $\Gamma\vdash\psi$. Todas las premisas han conservado su dependencia y las dos condiciones laterales se utilizaron expresamente. $\square$

## 9.19. Los cambios alfa son deductivamente invisibles

### Metateorema 9.19.1 — Equivalencia alfa implica equivalencia demostrable {#tlog-mth-00037}

**Enunciado.** Si $\varphi\equiv_\alpha\psi$ en la gramática del Capítulo 6, entonces

$$
\boxed{\vdash_{\mathsf H_\tau^{=}}\varphi\leftrightarrow\psi.}
$$

El enunciado **no** confunde equivalencia alfa sintáctica, equivalencia demostrable y equivalencia semántica; sólo establece una implicación entre las dos primeras.

**Demostración.** Examinemos primero un paso alfa elemental $\forall x\,\chi\rightsquigarrow_\alpha\forall y\,\chi[y/x]_{\mathrm{lit}}$ con $y$ fresca para todos los nombres de $\chi$. Sea $\chi'=\chi[y/x]_{\mathrm{lit}}$. Desde la hipótesis $\forall x\chi$, `Q1` con el término variable $y$ da $\chi'$. Como $y$ no ocurre libre en $\forall x\chi$, la regla admisible de §9.11 permite concluir $\forall y\chi'$. El teorema de deducción descarga la hipótesis y produce

$$
\vdash(\forall x\chi)\to(\forall y\chi').
$$

Para la dirección inversa, la sustitución literal $\chi'[x/y]_{\mathrm{lit}}$ recupera $\chi$: sólo se restauran hojas que eran ocurrencias libres de $x$, y la frescura inicial evita colisiones y capturas, aun si $\chi$ posee vinculantes internos que se llaman $x$. Como $x$ no pertenece a $\operatorname{FV}(\forall y\chi')$, particularizar $\forall y\chi'$ con $x$, generalizar después en $x$ y descargar la hipótesis da la implicación inversa. Por §9.16 obtenemos el bicondicional.

Para $\exists$ usamos la dualidad de §9.18 y el caso universal aplicado a $\neg\chi$: el renombrado ligado de $\exists x\chi$ es equivalente al de $\forall x\neg\chi$ y la equivalencia se recupera negando ambos lados. Para extender un paso alfa a un contexto, los cinco conectivos conservan equivalencias por tautologías proposicionales. Si $\vdash\rho\leftrightarrow\eta$, la regla de generalización para teoremas aplicada a ambas implicaciones, junto con `Q3`, da $\vdash\forall z\rho\leftrightarrow\forall z\eta$, y la dualidad obtiene lo mismo para $\exists z$. Así cada paso alfa contextual preserva equivalencia demostrable. Por reflexividad, simetría y transitividad del bicondicional clásico, también la preserva su clausura de equivalencia $\equiv_\alpha$. $\square$

**Nota crítica.** Aquí la frescura del nombre de renombrado es fuerte: incluye los **nombres ligados** de la matriz, no solamente sus variables libres. Con ello la ida y la vuelta de la sustitución literal son válidas; sin esa condición, el razonamiento de recuperación de la matriz no estaría justificado.

## 9.20. Conjuntos deductivamente cerrados y teorías de sentencias

### Definición 9.20.1 — Clausura deductiva y teoría sintáctica {#tlog-def-00055}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$ definimos

$$
\operatorname{Cn}^{\mathrm{ded}}_{\mathsf H_\tau^{=}}(\Gamma)
:=\{\varphi\in\operatorname{Fm}_\tau:\Gamma\vdash_{\mathsf H_\tau^{=}}\varphi\}.
$$

Este es un **conjunto** por separación. Llamamos *conjunto deductivamente cerrado de fórmulas* a un $D\subseteq\operatorname{Fm}_\tau$ para el cual $D=\operatorname{Cn}^{\mathrm{ded}}(D)$. No se impone que las fórmulas de $D$ sean sentencias.

Una *teoría sintáctica de sentencias* es, en cambio, un conjunto $T\subseteq\operatorname{Sent}_\tau$ con

$$
\boxed{T=\operatorname{Cn}^{\mathrm{ded}}(T)\cap\operatorname{Sent}_\tau.}
$$

La intersección con $\operatorname{Sent}_\tau$ es indispensable: incluso desde premisas que son sentencias se derivan fórmulas abiertas como $x\doteq x$. Para un conjunto de axiomas de sentencia $S$, su **teoría generada** se define por $\operatorname{Th}^{\mathrm{ded}}_\tau(S):=\operatorname{Cn}^{\mathrm{ded}}(S)\cap\operatorname{Sent}_\tau$. Esta definición no pide ni presupone modelos de $S$.

## 9.21. La clausura deductiva es un operador finitario

### Proposición 9.21.1 — Extensividad, monotonía, idempotencia y cierre de teorías {#tlog-pro-00024}

Para cualesquiera $\Gamma,\Delta\subseteq\operatorname{Fm}_\tau$:

$$
\begin{aligned}
&\Gamma\subseteq\operatorname{Cn}^{\mathrm{ded}}(\Gamma),\\
&\Gamma\subseteq\Delta\Rightarrow
 \operatorname{Cn}^{\mathrm{ded}}(\Gamma)\subseteq
 \operatorname{Cn}^{\mathrm{ded}}(\Delta),\\
&\operatorname{Cn}^{\mathrm{ded}}(\operatorname{Cn}^{\mathrm{ded}}(\Gamma))
 =\operatorname{Cn}^{\mathrm{ded}}(\Gamma),\\
&\operatorname{Cn}^{\mathrm{ded}}(\Gamma)
=\bigcup_{\substack{\Gamma_0\subseteq\Gamma\\\Gamma_0\text{ finito}}}
\operatorname{Cn}^{\mathrm{ded}}(\Gamma_0).
\end{aligned}
$$

Además, $\operatorname{Th}^{\mathrm{ded}}_\tau(S)$ es una teoría sintáctica de sentencias; todo conjunto de sentencias $S$ está contenido en su teoría generada, y cualquier teoría de sentencias que contenga $S$ contiene también a $\operatorname{Th}^{\mathrm{ded}}_\tau(S)$.

**Demostración.** Las dos primeras propiedades se deducen de las reglas de premisa y monotonía de §9.10. Una dirección de la idempotencia es extensividad; para la otra, cada miembro $\delta\in\operatorname{Cn}^{\mathrm{ded}}(\Gamma)$ tiene una demostración desde $\Gamma$, y el corte de §9.10 transforma toda demostración posterior que lo utilice en una desde $\Gamma$. La identidad finitaria es exactamente la finitariedad de pruebas del mismo apartado, en ambas direcciones por monotonía. Para las sentencias, si $S\subseteq\operatorname{Sent}_\tau$, el cierre $D=\operatorname{Cn}^{\mathrm{ded}}(S)$ es cerrado por idempotencia. Sea $T=D\cap\operatorname{Sent}_\tau$. La inclusión $T\subseteq D$ y la idempotencia dan $\operatorname{Cn}^{\mathrm{ded}}(T)\subseteq D$; inversamente $S\subseteq T$ implica $D\subseteq\operatorname{Cn}^{\mathrm{ded}}(T)$. Así $\operatorname{Cn}^{\mathrm{ded}}(T)=D$, y al intersectar con sentencias obtenemos $T=\operatorname{Th}^{\mathrm{ded}}_\tau(T)$. La minimalidad sigue por monotonía y cierre de cualquier teoría que contenga $S$. $\square$

## 9.22. Consistencia como ausencia de contradicción demostrable

### Definición 9.22.1 — Contradicción fija y consistencia sintáctica {#tlog-def-00056}

Fijamos la **sentencia** $\kappa:=\forall x_0(x_0\doteq x_0)$ y la abreviatura metateórica de fórmula objeto

$$
\boxed{\bot_\tau:=(\kappa\land\neg\kappa).}
$$

No se amplía el alfabeto objeto con un nuevo símbolo $\bot$. Para $\Gamma\subseteq\operatorname{Fm}_\tau$, decimos que $\Gamma$ es *inconsistente sintácticamente* cuando $\Gamma\vdash_{\mathsf H_\tau^{=}}\bot_\tau$, y *consistente* cuando $\Gamma\nvdash_{\mathsf H_\tau^{=}}\bot_\tau$. Estas nociones se formulan sólo en términos de derivaciones; **no** son equivalentes por definición a existencia de modelo.

La oración $\kappa$ es teorema: $x_0\doteq x_0$ es `E1` y su clausura universal es otro axioma de §9.5. Esta observación fija un testigo sintáctico explícito y estable para los controles de consistencia.

## 9.23. Caracterizaciones puramente deductivas de consistencia

### Proposición 9.23.1 — Explosión, pares contradictorios y adjunción {#tlog-pro-00025}

Para un conjunto $\Gamma\subseteq\operatorname{Fm}_\tau$ se equivalen:

1. $\Gamma\vdash\bot_\tau$.
2. Existen $\alpha\in\operatorname{Fm}_\tau$ tal que $\Gamma\vdash\alpha$ y $\Gamma\vdash\neg\alpha$.
3. Para toda $\beta\in\operatorname{Fm}_\tau$, $\Gamma\vdash\beta$.

Para toda fórmula $\rho$, se tiene asimismo

$$
\boxed{\Gamma\cup\{\rho\}\text{ es inconsistente}
\quad\Longleftrightarrow\quad\Gamma\vdash\neg\rho.}
$$

**Demostración.** (1) implica (2) tomando $\alpha=\kappa$ y eliminando la conjunción de $\kappa\land\neg\kappa$ mediante §9.16. De (2), la regla derivada de conjunción produce $\alpha\land\neg\alpha$, y la tautología proposicional $(\alpha\land\neg\alpha)\to\bot_\tau$ —levantada por §9.14— produce (1). La explosión de §9.16 obtiene cualquier $\beta$ desde el par contradictorio, dando (3); al tomar $\beta=\bot_\tau$ se vuelve a (1).

Si $\Gamma\cup\{\rho\}$ es inconsistente, el teorema de deducción entrega $\Gamma\vdash\rho\to\bot_\tau$. La instancia de la tautología clásica $(\rho\to\bot_\tau)\to\neg\rho$, donde $\bot_\tau$ es la conjunción $\kappa\land\neg\kappa$, da $\Gamma\vdash\neg\rho$. Inversamente, desde $\Gamma\vdash\neg\rho$ la premisa adicional $\rho$ permite obtener una contradicción y por tanto $\bot_\tau$. No se emplea satisfacibilidad, corrección ni completitud. $\square$

## 9.24. Teorías de sentencias y clausura universal

### Metateorema 9.24.1 — Las sentencias como premisas autorizan generalización {#tlog-mth-00038}

**Enunciado.** Sea $S\subseteq\operatorname{Sent}_\tau$ un conjunto cualquiera de sentencias y sea $\varphi\in\operatorname{Fm}_\tau$. Con la clausura universal canónica $\varphi^\forall$ de §8.30, se verifica

$$
\boxed{S\vdash_{\mathsf H_\tau^{=}}\varphi
\quad\Longleftrightarrow\quad
S\vdash_{\mathsf H_\tau^{=}}\varphi^\forall.}
$$

Más generalmente, para cualquier variable $x$, $S\vdash\varphi\iff S\vdash\forall x\varphi$. Estas equivalencias son **sintácticas** y no se identifican con la relación de consecuencia global del Capítulo 8.

**Demostración.** Al ser todas las fórmulas de $S$ sentencias, $\operatorname{FV}(S)=\varnothing$. La admisibilidad de la generalización (§9.11) permite pasar de una prueba de $\varphi$ desde $S$ a otra de $\forall x\varphi$ desde $S$, para cualquier $x$, y repetir la transformación un número finito de veces. La clausura universal $\varphi^\forall$ cuantifica sólo las finitas variables libres, en orden fijado por §8.30. Recíprocamente, de $\forall x\theta$ podemos inferir $\theta$ por `Q1` usando el **término variable $x$**, que siempre es libre para sustituirse a sí mismo, seguido de `MP`; iterando sobre el prefijo finito de $\varphi^\forall$ recuperamos $\varphi$. No aparecen premisas adicionales que dependan de las variables generalizadas. $\square$

## 9.25. Ejemplos y fronteras de lo demostrado

**Una premisa abierta y el fallo de la generalización irrestricta.** Si $P$ es un símbolo relacional unario, entonces $\{P(x)\}\vdash P(x)$ por regla de premisa. Esto **no** permite escribir $\{P(x)\}\vdash\forall xP(x)$ por §9.11, pues $x\in\operatorname{FV}(\{P(x)\})$. Tampoco se ha demostrado su *no derivabilidad*: para ello se necesitaría la corrección del sistema, diferida al Capítulo 10. El contramodelo semántico del §9.12 ilustra el peligro, pero no se utiliza como prueba de un resultado sintáctico aquí.

**Constantes, predicados nularios y congruencia.** Si $c\in F_0$, `E1` autoriza $c\doteq c$. Si $R\in R_0$, las reglas proposicionales permiten $\{R(),R()\to\chi\}\vdash\chi$, sin interpretar $R()$. Estas particularidades verifican que el cálculo conserva las aridades nulas de los capítulos 5–8.

**Teoría sintáctica versus teoría semántica.** La clausura $\operatorname{Th}^{\mathrm{ded}}_\tau(S)$ se determina exclusivamente por derivaciones finitas. La teoría $\operatorname{Th}_\tau(\mathfrak A)$ y la clausura $\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$ del Capítulo 8 se determinan por satisfacción. La coincidencia de ciertos cierres, bajo condiciones precisas, requerirá los teoremas de corrección y completitud. Este capítulo no los importa.

## 9.26. Cierre matemático de `CH09-M02` y del Capítulo 9

Los resultados §§9.14–9.24 completan la función arquitectónica del Capítulo 9: ya existe un cálculo de Hilbert para fórmulas arbitrarias de signatura conjuntista, con axiomas y reglas tipadas, pruebas finitas, teorema de deducción, generalización con condición lateral, igualdad congruencial, reglas derivadas, clausura deductiva y nociones sintácticas de teoría y consistencia. Los esquemas cubren funciones/relaciones nularias y ambos cuantificadores **primitivos**.

**Frontera rigurosa:** una afirmación $\Gamma\vdash\varphi$ todavía **no** implica aquí $\Gamma\models_\tau\varphi$ por un metateorema ya registrado; tampoco se infiere completitud, compacidad, decidibilidad ni enumerabilidad efectiva para signaturas arbitrarias. Tales obligaciones tienen sus propios capítulos y condiciones de fundamento.

```text
TLOG-CH09-M01 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH09-M02 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH09-0001 = CLOSED / PASS / DRIVE-READBACK-PASS
new mathematical nodes CH09-M02 = 11
chapter 9 nodes = 22
TLOG registered/closed nodes = 166/166
DAG = 166 nodes / 446 direct edges / acyclic PASS
Lean compiled/verified = 0
external interfaces = 0
chapters closed mathematically = 10/24 (41.7 %)
PART I = CLOSED; PART II = OPEN
```

**Siguiente frente:** `TLOG-CH10-M01 — Corrección del cálculo de primer orden: validez de los esquemas, preservación de MP y teorema de corrección`.

### Vector de progreso del microtramo

```text
LOCAL  CH09-M02 ██████████ 11/11 (100 %, pruebas redactadas)
GLOBAL TLOG     ██████████░░░░░░░░░░░░░░ 10/24 capítulos (41,7 %)
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 8](capitulo-08.md) · [Capítulo 10 →](capitulo-10.md)


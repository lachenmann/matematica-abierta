---
title: Capítulo 11 — Completitud y compacidad
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
content-id: MA-BCH-0213
content-type: book-chapter
source-id: TLOG-CH11-0001
prerequisites:
- MA-BCH-0207
- MA-BCH-0208
- MA-BCH-0209
- MA-BCH-0210
- MA-BCH-0211
- MA-BCH-0212
related:
- MA-BOK-0014
source-sha256: 2fdb172a25b14eac997e898ce254f358aacad157b1c8f9bfcd9706b59d104923
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 10](capitulo-10.md) · [Capítulo 12 →](capitulo-12.md)

## 11.0. De la consistencia sintáctica a la existencia de modelos

Los capítulos 8–10 proporcionaron, sin circularidad, satisfacción de primer orden, derivaciones finitas en $\mathsf H_\tau^{=}$ y corrección $\Gamma\vdash\varphi\Rightarrow\Gamma\models_\tau\varphi$. La dirección inversa requiere un **modelo** para cada teoría sintácticamente consistente. Aquí se construye directamente, a partir de términos cerrados, para conjuntos de **sentencias en un lenguaje numerable**. Las fórmulas abiertas y la generalidad de signaturas no bien ordenables son obligaciones distintas; no se sustituyen sus pruebas por la de este bloque.

El objeto $\mathsf M_{\mathrm{ext}}$ sigue siendo **ZF clásica sin AC**. Esta restricción importa: el principio general de completitud/compacidad para lenguajes arbitrarios, formulado para todas las signaturas sin hipótesis de buen orden, equivale sobre ZF al teorema del ideal primo booleano (`BPI`, principio del ultrafiltro), que no es un teorema de ZF. La distinción queda documentada en la bibliografía de frontera; no se importa `BPI` como axioma.

### Alcance y procedencia

- `TLOG-SRC-0002` (Enderton) y `TLOG-SRC-0003` (Rautenberg): patrones históricos y estructurales previamente registrados. **No se declara** un nuevo cotejo línea a línea de sus demostraciones de completitud en este microtramo.
- `TLOG-SRC-0009` (Jech, *The Axiom of Choice*, 1973, cap. 2 §2.3) y `TLOG-SRC-00010` (Espíndola, 2016, abstract y datos editoriales): control de la frontera ZF/BPI. Son `BIB-VERIFIED / NOT TEXT-COLLATED`; su enunciado no sustituye las pruebas positivas que siguen.

## 11.1. Alcance conjuntista del procedimiento

### Convención 11.1.1 — Lenguaje numerable y frontera de elección {#tlog-cnv-00012}

Una signatura $\tau$ es **numerable** si el conjunto de sus símbolos extralógicos posee una inyección en $\omega$. Fijada **una** de tales inyecciones, se asignan códigos naturales a todos los símbolos lógicos, variables, conectivos y delimitadores, y de allí, inyectivamente, a los árboles finitos de términos y fórmulas. Las fórmulas y sentencias quedan así bien ordenadas por sus códigos. No se elige una enumeración para cada uno de infinitos conjuntos independientes: una única codificación inicial determina todas las posteriores.

En lo sucesivo el símbolo $\vdash$ está tipado por $\mathsf H_\tau^{=}$; $\models$, por la semántica local de §8.26. El presente bloque trata **teorías de sentencias**; su ampliación a conjuntos de fórmulas abiertas no es definicional. Para signaturas arbitrarias no se adopta `BPI`, `AC` ni el lema de Zorn: se estudiará por separado la frontera de hipótesis.

## 11.2. Conservatividad por introducción de constantes

### Lema 11.2.1 — Eliminación finita de constantes auxiliares {#tlog-lem-00028}

Sea $L\subseteq L^+$ una ampliación de signatura que incorpora **sólo constantes funcionales nularias**. Si $\Gamma\cup\{\theta\}\subseteq\operatorname{Fm}_L$ y existe una derivación $\Gamma\vdash_{\mathsf H_{L^+}^{=}}\theta$, entonces

$$
\boxed{\Gamma\vdash_{\mathsf H_L^{=}}\theta.}
$$

En particular, si $S\subseteq\operatorname{Sent}_L$ es consistente en $\mathsf H_L^{=}$, lo sigue siendo al cambiar sólo el lenguaje ambiente a $L^+$.

**Demostración.** Fijemos una derivación $\Pi$ en el lenguaje ampliado. Por finitud de $\Pi$, sólo aparecen en ella finitas constantes nuevas $d_1,\ldots,d_m$. El árbol conjunto de las líneas posee finitos nombres de variable, incluidos los de vinculantes. Elegimos los primeros $m$ nombres distintos $y_1,\ldots,y_m$ que no aparecen en **ninguna** línea de $\Pi$, usando el orden fijo de $X$. Reemplazamos simultáneamente los tokens extralógicos $d_i$ por los términos variables $y_i$, sin cambiar ningún símbolo preexistente. Ningún $y_i$ aparece como variable vinculada en la derivación original, de modo que ninguna ocurrencia insertada es capturada.

Examinamos una línea axiomática. Las formas proposicionales `H1–H12` son estables bajo la sustitución; `E1` conserva reflexividad y `E2` conserva las dos condiciones `FreeFor`, pues los $y_i$ no son nombres de cuantificador de ninguna matriz usada. En `Q1`, `Q2` la ausencia de captura se mantiene; en `Q3`, `Q5` la forma se conserva, y en `Q4` la variable cuantificada no es ninguna de las $y_i$, preservando $x\notin FV(\varphi)$. Una clausura universal finita de una instancia se transforma en la clausura universal de la instancia transformada. Las líneas por `MP` siguen siendo inferencias por `MP`; las líneas-premisa y la conclusión pertenecen a $L$ y permanecen inalteradas. Así la secuencia traducida es una derivación en $\mathsf H_L^{=}$ de la misma $\theta$ desde $\Gamma$. Para la consistencia tomamos $\theta=\bot_L$, que no contiene constantes nuevas. $\square$

**Control:** la traducción se practica sobre una **prueba finita**, no sobre el conjunto total $\Gamma$; no exige encontrar un nombre fresco para todas las variables ligadas de un conjunto infinito de sentencias.

## 11.3. Introducción segura de testigos

### Lema 11.3.1 — Axioma de Henkin con constante fresca {#tlog-lem-00029}

Sea $T\subseteq\operatorname{Sent}_L$ consistente, $\delta=\exists x\,\rho(x)\in\operatorname{Sent}_L$, con $\operatorname{FV}(\rho)\subseteq\{x\}$, y sea $c$ una constante nularia nueva que no aparece en $L$. La instancia $\rho(c):=\rho[c/x]_{\mathrm{lit}}$ está definida porque $c$ es un término **cerrado**. Entonces

$$
\boxed{T\cup\{\,\delta\to\rho(c)\,\}
\text{ es consistente en }L\cup\{c\}.}
$$

**Demostración.** Por §11.2, $T$ sigue siendo consistente en el lenguaje ampliado. Si la adjunción fuese inconsistente, el teorema de deducción y las reducciones clásicas de §9.23 darían tanto $T\vdash\delta$ como $T\vdash\neg\rho(c)$. Una demostración fija de $\neg\rho(c)$ desde $T$ contiene finitas variables. Sustituyendo el token constante $c$ por una variable $y$ ausente de todas sus líneas y de $\rho$, mediante la misma transformación de §11.2, obtenemos una demostración de $\neg\rho(y)$ desde las mismas **premisas sentenciales** $T$. La condición $FV(T)=\varnothing$ permite generalizar: $T\vdash\forall y\neg\rho(y)$. Por equivalencia alfa deductiva (§9.19), $T\vdash\forall x\neg\rho(x)$, y por la dualidad `Q5` y el cálculo clásico, $T\vdash\neg\exists x\rho(x)=\neg\delta$. Junto con $T\vdash\delta$, esto contradice la consistencia de $T$. $\square$

**Frontera:** no se afirma este lema con la misma prueba para matrices con variables libres adicionales; una constante $c$ que dependiera de parámetros libres requeriría una función-testigo o un tratamiento de parámetros diferente.

## 11.4. La torre determinista de testigos

### Definición 11.4.1 — Ampliaciones de lenguaje y axiomas testigo por niveles {#tlog-def-00057}

Fijemos una signatura numerable $L_0=\tau$ y un conjunto consistente $T_0=S\subseteq\operatorname{Sent}_{L_0}$. Por recursión en $n\in\omega$, definimos $L_n,T_n$. Sea $E_n$ el conjunto de **sentencias existenciales** $\exists x\rho\in\operatorname{Sent}_{L_n}$, bien ordenado por el código finito determinado por §11.1. Para cada $\delta=\exists x\rho\in E_n$, introducimos una nueva constante distinguible $c_{n,\langle\delta\rangle}$, con etiquetas disjuntas de todos los símbolos de $L_n$ y de las otras constantes. Definimos

$$
\begin{aligned}
 L_{n+1}&=L_n\sqcup\{c_{n,\langle\delta\rangle}:\delta\in E_n\},\\
 W_n&=\{\,\delta\to\rho[c_{n,\langle\delta\rangle}/x]_{\mathrm{lit}}:\delta=\exists x\rho\in E_n\},\\
 T_{n+1}&=T_n\cup W_n.
\end{aligned}
$$

La codificación asigna a cada $\delta$ exactamente una constante y hace que todos los datos sean **conjuntos**. La unión $L_\omega=\bigcup_{n<\omega}L_n$, $T_H=\bigcup_{n<\omega}T_n$ es la expansión de Henkin inicial. Cada $T_n$ contiene **sentencias**, no premisas abiertas. En los niveles posteriores podrán aparecer fórmulas que usen constantes añadidas en niveles anteriores.

## 11.5. Consistencia y propiedad de testigos

### Lema 11.5.1 — La unión numerable es consistente y testimoniada {#tlog-lem-00030}

Todos los $T_n$ son consistentes en $L_n$; $T_H\subseteq\operatorname{Sent}_{L_\omega}$ es consistente en $L_\omega$, y toda sentencia $\delta=\exists x\rho\in\operatorname{Sent}_{L_\omega}$ posee un término constante cerrado $c$ tal que

$$
\boxed{\delta\to\rho[c/x]_{\mathrm{lit}}\in T_H.}
$$

**Demostración.** Inducimos sobre $n$. Por §11.2, $T_n$ permanece consistente al ampliar el lenguaje. Supongamos que una subfamilia finita de $W_n$ provocara inconsistencia. Sus constantes $c_{n,i_1},\ldots,c_{n,i_m}$ son mutuamente distintas; ninguna aparece en $T_n$ ni en las matrices de $E_n$. Aplicamos §11.3 sucesivamente, introduciendo una nueva constante por paso: la teoría provisional sigue siendo una teoría de **sentencias** y la constante del paso siguiente no figura en sus premisas. Se obtiene consistencia de cualquier subfamilia finita. Una derivación de contradicción desde $T_{n+1}$ sólo usa finitas líneas-premisa (§9.10), contradiciendo lo anterior. Por tanto $T_{n+1}$ es consistente.

Si $T_H$ fuera inconsistente en $L_\omega$, una demostración de $\bot$ emplearía finitas premisas de $T_H$ y finitos símbolos de $L_\omega$; todos pertenecen a un cierto $L_N$, y las premisas a un cierto $T_M$. Tomando el máximo de esos índices, existiría una demostración de contradicción desde algún $T_K$ en $L_K$, imposible. Finalmente, una sentencia existencial de $L_\omega$ tiene árbol finito y sólo finitos símbolos nuevos: aparece en algún $L_n$, y su axioma-testigo pertenece a $W_n$. Esta última propiedad es **sintáctica** y no supone todavía que el existencial sea verdadero en una estructura. $\square$

## 11.6. Decisión de todas las sentencias sin Zorn

### Metateorema 11.6.1 — Extensión completa, consistente y de Henkin {#tlog-mth-00041}

Existe $T^*\subseteq\operatorname{Sent}_{L_\omega}$ que contiene $T_H$ y satisface:

1. **consistencia:** $T^*\nvdash\bot$;
2. **decisión:** para cada sentencia $\theta$, exactamente una de $\theta,\neg\theta$ pertenece a $T^*$;
3. **cierre deductivo sentencial:** si $T^*\vdash\theta$ y $\theta$ es sentencia, entonces $\theta\in T^*$;
4. **testigos:** si $\exists x\rho\in T^*$ es sentencia existencial, existe una constante $c$ tal que $\rho[c/x]_{\mathrm{lit}}\in T^*$.

**Demostración.** Enumeramos canónicamente todas las sentencias de $L_\omega$ como $(\theta_k)_{k<\omega}$, admitiendo repeticiones si fuera necesario para cubrir los códigos. Definimos $S_0=T_H$. Dado el conjunto consistente $S_k$, ponemos $S_{k+1}=S_k\cup\{\theta_k\}$ cuando esa unión es consistente; de lo contrario $S_{k+1}=S_k\cup\{\neg\theta_k\}$. En el segundo caso §9.23 afirma $S_k\vdash\neg\theta_k$; adjuntar una fórmula ya deducible conserva consistencia por corte (§9.10). La regla de selección «si es consistente, sí; si no, no» define unívocamente la sucesión en ZF clásica: **no se invoca un selector** de extensiones maximales.

Sea $T^*=\bigcup_{k<\omega}S_k$. Es consistente por finitud de las pruebas, y contiene una de $\theta,\neg\theta$ para toda sentencia $\theta$; contener ambas violaría consistencia. Si $T^*\vdash\theta$ con $\theta$ sentencia y $\theta\notin T^*$, completitud de decisión daría $\neg\theta\in T^*$, contradicción. Luego es deductivamente cerrado en sentencias. Si $\delta=\exists x\rho\in T^*$, el axioma $\delta\to\rho(c)\in T_H\subseteq T^*$ (11.5.1), y `MP` junto con el cierre sentencial proporciona $\rho(c)\in T^*$. $\square$

## 11.7. Preparación del modelo de términos

### Definición 11.7.1 — Universo cociente e interpretaciones por términos cerrados {#tlog-def-00058}

Sea $\operatorname{CTm}_{L_\omega}$ el conjunto de términos **cerrados** del lenguaje ampliado y definamos $t\sim u$ si y sólo si $(t\doteq u)\in T^*$. Definimos el candidato de universo $M=\operatorname{CTm}_{L_\omega}/\!\sim$, cuyas clases denotamos $[t]$. Para cada símbolo funcional $f\in F_n$ y cada símbolo relacional $R\in R_n$, proponemos

$$
\begin{aligned}
 f^{\mathfrak M}([t_1],\ldots,[t_n])&=[f(t_1,\ldots,t_n)],\\
 ([t_1],\ldots,[t_n])\in R^{\mathfrak M}&\iff R(t_1,\ldots,t_n)\in T^*.
\end{aligned}
$$

Estas son **definiciones candidatas** hasta demostrar que no dependen de los representantes. Se admiten expresamente $n=0$, constantes y predicados nularios. La igualdad objeto no recibe una interpretación extralógica añadida: se evalúa como la igualdad real de clases del universo.

## 11.8. El cociente es una estructura legítima en ZF

### Lema 11.8.1 — Equivalencia, congruencia y sección canónica {#tlog-lem-00031}

La relación $\sim$ es equivalencia en $\operatorname{CTm}_{L_\omega}$, las interpretaciones de §11.7 están bien definidas, el universo $M$ es no vacío y existe una sección **canónica** $r:M\to\operatorname{CTm}_{L_\omega}$ tal que $[r(a)]=a$ para todo $a\in M$.

**Demostración.** Para cualquier término cerrado $t$, `E1` es teorema; al ser la igualdad sentencial, pertenece a $T^*$. La simetría y transitividad provienen de §9.17, aplicadas por `MP` al cierre sentencial de $T^*$. La misma proposición de congruencia muestra que, si $[t_i]=[u_i]$ para todos los argumentos, entonces $f(\bar t)\sim f(\bar u)$, y que $R(\bar t)\in T^*$ equivale a $R(\bar u)\in T^*$; para la dirección inversa se emplea simetría de las igualdades. En aridad cero no existe ninguna sustitución: los términos constantes y átomos nularios se interpretan directamente.

Hay al menos una constante en $L_\omega$: la sentencia $\exists x(x\doteq x)$ ya pertenece a $L_0$ y recibe una constante de testigo en $L_1$, con independencia de que el lenguaje original disponga de constantes. Su clase proporciona un elemento de $M$. Como el conjunto de términos cerrados posee una inyección fija en $\omega$, para cada clase no vacía $a\subseteq\operatorname{CTm}_{L_\omega}$ existe el único elemento $r(a)$ de código menor. Por separación y reemplazo, $r$ es una función sobre $M$ y satisface $[r(a)]=a$. No se ha usado ni elección numerable ni elección de representantes arbitraria. $\square$

## 11.9. Lema de verdad para fórmulas abiertas y cerradas

### Metateorema 11.9.1 — Lema de verdad del modelo canónico {#tlog-mth-00042}

Sea $\mathfrak M$ la estructura de §§11.7–11.8, y sea $s:X\to M$ una **asignación arbitraria**. Mediante la sección canónica $r$, definimos $\widehat s(x):=r(s(x))$, un término cerrado de $L_\omega$. Para $\varphi\in\operatorname{Fm}_{L_\omega}$ sea $\varphi[\widehat s]$ la **sentencia** obtenida reemplazando simultáneamente **sus variables libres** por los respectivos términos cerrados, sin tocar variables ligadas. Como los sustituyentes no tienen variables, no se produce captura; para cada fórmula se usan únicamente finitos términos y la sustitución puede implementarse literalmente sin cambiar vinculantes. Entonces

$$
\boxed{\mathfrak M,s\models_{L_\omega}\varphi
\quad\Longleftrightarrow\quad
\varphi[\widehat s]\in T^*.}
$$

**Demostración.** Inducción estructural sobre $\varphi$. Para cualquier término $t$, una inducción preliminar demuestra $\llbracket t\rrbracket_{\mathfrak M,s}=[t[\widehat s]]$, donde $t[\widehat s]$ es un término cerrado: para variable $x$, $[\widehat s(x)]=s(x)$; para $f$ resulta de la propia definición de $f^{\mathfrak M}$. Así la cláusula atómica de igualdad coincide con la pertenencia de la igualdad de los términos sustituidos a $T^*$, y la de $R$ coincide con la definición de la relación del modelo. El caso nulario evalúa el mismo átomo cerrado.

Para las conectivas, las leyes derivadas del cálculo clásico y la completitud por decisiones de $T^*$ proporcionan las identidades sentenciales $\neg\theta\in T^*\iff\theta\notin T^*$, $(\theta\land\eta)\in T^*\iff\theta,\eta\in T^*$ y las correspondientes cláusulas de $\lor,\to,\leftrightarrow$. Se corresponden exactamente con las cinco funciones de verdad de §8.3, y la hipótesis inductiva concluye cada caso.

Supongamos $\varphi=\exists x\psi$. Al cerrar las variables libres exteriores según $s$, obtenemos una sentencia $\delta=\exists x\theta(x)$, con $\theta=\psi[\widehat s\upharpoonright(X\setminus\{x\})]$. Si $\delta\in T^*$, la propiedad de Henkin produce un **término constante** $c$ con $\theta(c)\in T^*$. Tomamos el elemento $a=[c]\in M$. La hipótesis inductiva, evaluada en $s[x\mapsto a]$, muestra $\mathfrak M,s[x\mapsto a]\models\psi$, pues el representante canónico $r([c])$ es equivalente a $c$ por $\sim$, y la congruencia de igualdad y relaciones garantiza que sustituir uno por otro no modifica pertenencia a $T^*$. Recíprocamente, si existe $a\in M$ con $\mathfrak M,s[x\mapsto a]\models\psi$, la hipótesis inductiva da $\theta(r(a))\in T^*$; `Q2` y `MP` implican $\exists x\theta\in T^*$.

Para $\varphi=\forall x\psi$, si $\forall x\theta\in T^*$, `Q1` permite demostrar $\theta(t)\in T^*$ para **todo** término cerrado $t$; así la hipótesis inductiva vale bajo cada actualización $s[x\mapsto a]$. Inversamente, si $\forall x\theta\notin T^*$, la decisión completa da $\neg\forall x\theta\in T^*$. La dualidad `Q5` y el razonamiento clásico deducen $\exists x\neg\theta\in T^*$. Su testigo $c$ satisface $\neg\theta(c)\in T^*$, con lo que la hipótesis inductiva produce una actualización $s[x\mapsto[c]]$ que **no** satisface $\psi$, contra la universalidad supuesta. Ambos cuantificadores, aunque primitivos, quedan controlados. $\square$

**Advertencia de tipado:** $r$ no es un selector de una familia arbitraria de conjuntos; es la elección **por menor código** dentro de las clases de términos cerrados, que son subconjuntos de un conjunto explícitamente numerado. Asimismo, la fórmula $\varphi[\widehat s]$ usa sólo los representantes de las finitas variables libres de $\varphi$, incluso cuando la asignación $s$ sea infinita.

## 11.10. Existencia de modelos para teorías consistentes

### Metateorema 11.10.1 — Existencia de modelo en lenguaje numerable {#tlog-mth-00043}

Sea $\tau$ una signatura numerable, y $S\subseteq\operatorname{Sent}_\tau$ **cualquier conjunto de sentencias**, finito o infinito. Si $S$ es sintácticamente consistente en $\mathsf H_\tau^{=}$, entonces existe una estructura $\mathfrak A$ de signatura $\tau$ con universo no vacío tal que

$$
\boxed{S\text{ consistente}\quad\Longrightarrow\quad
\exists\mathfrak A\ (\mathfrak A\models_\tau S).}
$$

**Demostración.** La torre de §11.4 y la extensión de §11.6 producen $T^*\supseteq S$ en $L_\omega$, consistente, completa y testimoniada. El modelo cociente de términos cerrados $\mathfrak M$ está bien definido por §11.8. Para cada sentencia $\sigma\in S\subseteq T^*$ y para **cualquier** asignación $s:X\to M$, la sustitución de variables libres no altera $\sigma$ porque $FV(\sigma)=\varnothing$; por el lema de verdad $\mathfrak M,s\models\sigma$. Su reducto $\mathfrak A=\mathfrak M\upharpoonright_\tau$ comparte universo y satisface $\sigma$ por la invariancia de reductos de §8.16. Por tanto $\mathfrak A\models S$. La construcción se efectuó mediante códigos, recursión sobre $\omega$ y cocientes, sin Zorn, AC ni BPI. $\square$

La hipótesis «$\tau$ numerable» es una restricción efectiva del enunciado metateórico; **no** es condición lateral de ninguna fórmula del lenguaje objeto.

## 11.11. Primeras consecuencias y compacidad del fragmento tratado

### Proposición 11.11.1 — Consistencia, satisfacibilidad y compacidad sentencial numerable {#tlog-pro-00027}

Para un lenguaje numerable $\tau$ y un conjunto arbitrario de sentencias $S\subseteq\operatorname{Sent}_\tau$:

$$
\boxed{S\text{ consistente}\iff S\text{ satisfacible}.}
$$

Asimismo,
$$
\boxed{(\forall S_0\subseteq S\ \text{finito})\;
S_0\text{ satisfacible}\quad\Longrightarrow\quad S\text{ satisfacible}.}
$$

**Demostración.** La primera dirección es §11.10; la recíproca es el corolario de corrección §10.11, que prohíbe una prueba de $\bot$ en cualquier modelo de las premisas. Para la segunda, si $S\vdash\bot$, la finitariedad de §9.10 proporciona un subconjunto finito $S_0\subseteq S$ con $S_0\vdash\bot$, en contradicción con su satisfacibilidad y la corrección. Así $S$ es consistente y se aplica §11.10. No se ha afirmado aún la **completitud fuerte para fórmulas abiertas** ni la compactación para un conjunto arbitrario no numerable de símbolos que aparezcan simultáneamente. $\square$

## 11.12. Teorías numerables dentro de signaturas arbitrarias

### Proposición 11.12.1 — Reducción a soporte numerable y expansión uniforme {#tlog-pro-00028}

Sea $\tau$ una signatura **arbitraria**, quizá no bien ordenable, y $S\subseteq\operatorname{Sent}_\tau$ un conjunto **numerable de sentencias**, con una inyección $S\hookrightarrow\omega$ dada o existente. Si $S$ es consistente en $\mathsf H_\tau^{=}$, entonces existe una $\tau$-estructura $\mathfrak A$ con $\mathfrak A\models S$.

**Demostración.** Sea $\sigma\subseteq\tau$ la subsignatura integrada por los símbolos extralógicos que aparecen en alguna sentencia de $S$. Puesto que $S$ es numerable y cada fórmula es una **secuencia finita ordenada**, podemos codificar toda aparición de símbolo mediante un par $(i,j)\in\omega^2$: índice de sentencia y posición de aparición. Cada símbolo de $\sigma$ recibe el menor código de una de sus apariciones; así $\sigma$ es numerable **sin usar la afirmación general «unión numerable de conjuntos finitos numerables»**, que puede fallar en ZF. Toda fórmula de $S$ pertenece literalmente a $\operatorname{Sent}_\sigma$.

Si $S$ fuera inconsistente en el cálculo de la firma menor $\sigma$, esa misma prueba sería válida en $\mathsf H_\tau^{=}$ por persistencia de sintaxis y de instancias axiomáticas al ampliar signatura (§7.13), contradicción. Por §11.10 existe una $\sigma$-estructura $\mathfrak B\models S$. El resultado de expansión uniforme de §7.12 amplía $\mathfrak B$ a una $\tau$-estructura con **igual universo**, sin AC: basta fijar una sola vez un elemento $b_0$ del universo no vacío; todos los nuevos símbolos funcionales se interpretan como funciones constantes de valor $b_0$, y todas las relaciones nuevas como vacías. La invariancia de satisfacción por reductos (§8.16) asegura que la estructura ampliada satisface $S$. $\square$

**Frontera real:** «$S$ es numerable» no equivale a «$\tau$ es numerable». Esta proposición no demuestra el teorema de compacidad para **toda** teoría sobre una signatura arbitraria y no bien ordenable.

## 11.13. Controles de exactitud y tareas restantes

**Premisas abiertas.** La satisfacción de una fórmula abierta requiere asignaciones. El resultado de §11.10 es para **sentencias**, y no se transforma en completitud fuerte local simplemente cerrando universalmente todas las premisas: $\{P(x)\}$ puede satisfacerse bajo una asignación sin que $\forall xP(x)$ sea verdadera. El paso correcto deberá codificar asignaciones mediante **parámetros constantes** y demostrar conservatividad respecto de la derivabilidad original.

**Signaturas no bien ordenables.** El principio general «todo conjunto consistente de sentencias tiene un modelo» no es un teorema irrestricto de ZF; en toda su generalidad sobre signaturas arbitrarias coincide en fuerza con `BPI` (véanse `TLOG-SRC-0009`–`00010`). La ruta pendiente deberá distinguir el caso numerable (demostrado), otros casos con estructura de orden fijada (por construir) y una versión condicionada explícitamente a `BPI`.

**Sin circularidad.** El modelo de Henkin se construye mediante teoría completa y testigos sin usar la implicación inversa $\models\Rightarrow\vdash$. El corolario de consistencia desde satisfacibilidad sólo usa la corrección ya cerrada en CH10. El primer resultado de compacidad del fragmento numerable usa finitariedad de CH09 y existencia de modelo aquí, no compacidad previa.

## 11.14. Estado del bloque y vector gráfico

```text
TLOG-CH11-M01 = CLOSED / PASS / LOCAL QA PASS
TLOG-CH11-0001 = PARTIAL-CLOSURE / NOT CLOSED
new mathematical nodes = 12
closed nodes through CH11-M01 = 187
DAG direct edges = 535
formalization candidates = 54
Lean compiled/verified = 0
external interfaces = 0
closed chapters = 11/24 (45.8%)
PART I = CLOSED; PART II = OPEN
Drive readback = PASS (10/10 canonical raw Markdown SHA-256)
```

LOCAL  CH11-M01 ████████████ 12/12 (100 %, auditoría matemática)
GLOBAL TLOG    ███████████░░░░░░░░░░░░░ 11/24 capítulos (45,8 %)

**Nota histórica tras M01:** el siguiente frente proyectado era CH11-M02; queda desarrollado y auditado en los apartados siguientes.


## 11.15. Traducción de variables libres a parámetros

### Definición 11.15.1 — Parámetros constantes y traducción sentencial {#tlog-def-00059}

Fijada una signatura $\tau$, tomamos un conjunto de símbolos funcionales **nularios** nuevos $C_X=\{c_x:x\in X\}$, con etiqueta disjunta de $\tau$; escribimos $\tau^p=\tau\sqcup C_X$. No se interpreta el signo $c_x$ como la variable objeto $x$: es un símbolo extralógico distinto.

Para $\varphi\in\operatorname{Fm}_\tau$, sea $\varphi^p\in\operatorname{Sent}_{\tau^p}$ la fórmula obtenida reemplazando **simultáneamente sólo las ocurrencias libres** de cada $x$ por el término cerrado $c_x$. Los cuantificadores originales quedan intactos. En cada fórmula sólo se sustituyen los nombres de su conjunto finito $\operatorname{FV}(\varphi)$, por lo que la construcción es una recursión finita sin elección, captura ni exigencia de soporte finito para un conjunto de premisas. Para $\Gamma\subseteq\operatorname{Fm}_\tau$, definimos $\Gamma^p=\{\gamma^p:\gamma\in\Gamma\}$. Entonces $\Gamma^p\subseteq\operatorname{Sent}_{\tau^p}$ es un conjunto por reemplazo.

Las operaciones $\varphi\mapsto\varphi^p$, $\Gamma\mapsto\Gamma^p$ son *traducciones metateóricas* y no nuevas reglas del sistema objeto. En particular $\gamma^p$ NO se identifica sintácticamente con una clausura universal de $\gamma$.


## 11.16. Correspondencia semántica entre parámetros y asignaciones

### Lema 11.16.1 — Correspondencia semántica entre parámetros y asignaciones {#tlog-lem-00032}

**Enunciado.** Sea $\mathfrak B$ una $\tau^p$-estructura, $\mathfrak A=\mathfrak B\upharpoonright_\tau$, y definamos la asignación $s_{\mathfrak B}:X\to A$ por $s_{\mathfrak B}(x)=c_x^{\mathfrak B}$. Para cada $\varphi\in\operatorname{Fm}_\tau$,
$$
\boxed{\mathfrak B\models_{\tau^p}\varphi^p\iff
\mathfrak A,s_{\mathfrak B}\models_\tau\varphi.}
$$
Por tanto $\mathfrak B\models\Gamma^p\iff\mathfrak A,s_{\mathfrak B}\models\Gamma$.

**Demostración.** Enumeramos $\operatorname{FV}(\varphi)=\{x_1,\ldots,x_m\}$ en el orden fijo de $X$. Cada $c_{x_i}$ es término cerrado, libre para sustituir por $x_i$ en cualquier matriz; aplicamos sucesivamente el lema de sustitución semántica §8.11 (o su formulación simultánea §8.13). El valor de $c_{x_i}$ en $\mathfrak B$ es $c_{x_i}^{\mathfrak B}$, independiente de toda asignación. Las actualizaciones de las variables distintas conmutan (§7.5); así, dada cualquier asignación auxiliar $u$,
$$
\mathfrak B,u\models\varphi^p
\iff\mathfrak B,s_{\mathfrak B}\models\varphi.
$$
La equivalencia derecha equivale a $\mathfrak A,s_{\mathfrak B}\models\varphi$ por invariancia de satisfacción al tomar reductos (§8.16). El miembro izquierdo es independiente de $u$, porque $\varphi^p$ es sentencia (§8.6). Se aplica la equivalencia a cada miembro de $\Gamma$ utilizando **la misma asignación** $s_{\mathfrak B}$. $\square$

**Advertencia.** Esta equivalencia requiere que las constantes $c_x$ compartan una interpretación dentro de **una** estructura. No equivale a asignar distintos valores a la misma variable para premisas diferentes.


## 11.17. Clausura existencial de una familia finita consistente

### Lema 11.17.1 — Clausura existencial de una familia finita consistente {#tlog-lem-00033}

**Enunciado.** Sea $\Sigma=\{\psi_1,\ldots,\psi_k\}\subseteq\operatorname{Fm}_\tau$ un conjunto **finito** consistente en $\mathsf H_\tau^=$; el caso $k=0$ se atiende separadamente mediante la sentencia válida $\kappa$. Sea $\Theta=\psi_1\land\cdots\land\psi_k$ una conjunción de orden finito fijado y sean $x_1,\ldots,x_m$ todas las variables libres de $\Theta$. La clausura existencial
$$
\delta_\Sigma:=\exists x_1\cdots\exists x_m\,\Theta
$$
es una **sentencia sintácticamente consistente**. Lo sigue siendo en la subsignatura finita formada por los símbolos extralógicos presentes en $\Sigma$.

**Demostración.** Por iteración del esquema `Q2`, aplicado al término variable que coincide con el nombre cuantificado, y composición proposicional, se obtiene el **teorema lógico** $\vdash\Theta\to\delta_\Sigma$. La sustitución de una variable por sí misma es siempre `FreeFor`; cada cuantificación existencial de la sucesión elimina una variable libre. Supongamos $\{\delta_\Sigma\}\vdash\bot$. El test de consistencia de §9.23 proporciona $\vdash\neg\delta_\Sigma$. Por contraposición clásica de $\vdash\Theta\to\delta_\Sigma$ deducimos $\vdash\neg\Theta$. Pero de $\Sigma$ se deduce $\Theta$ por las reglas de conjunción de §9.16; de ahí $\Sigma\vdash\bot$, contradicción. Si una prueba de inconsistencia existiera en la subsignatura finita $\sigma$ de $\delta_\Sigma$, seguiría siendo una prueba en $\tau$ por persistencia de instancias axiomáticas (§7.13), imposible. Para $\Sigma=\varnothing$, tomamos $\delta_\Sigma=\kappa$, consistente por corrección y la validez de la igualdad reflexiva. $\square$

**Observación.** Se han introducido cuantificadores **existenciales**, no universales; la clausura universal de premisas abiertas modificaría la condición local que pretendemos modelar.


## 11.18. Satisfacibilidad finita de las sentencias parametrizadas

### Proposición 11.18.1 — Satisfacibilidad finita de las sentencias parametrizadas {#tlog-pro-00029}

**Enunciado.** Para $\Lambda\subseteq\operatorname{Fm}_\tau$ sintácticamente consistente, **cada subconjunto finito** de $\Lambda^p\subseteq\operatorname{Sent}_{\tau^p}$ es satisfacible en alguna $\tau^p$-estructura. No se requiere que $\Lambda$ ni $\tau$ sean numerables.

**Demostración.** Sea $F\subseteq\Lambda^p$ finito. Como cada elemento de $F$ es imagen de alguna fórmula de $\Lambda$, una selección **finita** en ZF proporciona un $\Sigma\subseteq\Lambda$ finito con $F\subseteq\Sigma^p$. Por monotonía y consistencia de $\Lambda$, también $\Sigma$ es consistente. El lema anterior suministra una sentencia consistente $\delta_\Sigma$ sobre una firma finita $\sigma$. Por existencia de modelos para sentencias de firma numerable (§11.10), existe una $\sigma$-estructura $\mathfrak C\models\delta_\Sigma$. La semántica de los finitos existenciales da testigos $a_1,\ldots,a_m\in C$ que, asignados a $x_1,\ldots,x_m$, satisfacen $\Theta$, y por tanto simultáneamente $\Sigma$. Extendemos esa asignación a todo $X$ por un único valor predeterminado $a_0\in C$, posible por $C\ne\varnothing$; si $m=0$, se usa directamente la independencia de asignación de las sentencias.

Expandimos $\mathfrak C$ uniformemente a una $\tau$-estructura $\mathfrak A$ interpretando las funciones no presentes por la función constante de valor $a_0$ y las relaciones nuevas como vacías (§7.12). Conservamos la satisfacción de $\Sigma$ por reductos (§8.16). Finalmente ampliamos a $\tau^p$ mediante $c_x^{\mathfrak B}=s(x)$; la correspondencia §11.16 asegura $\mathfrak B\models\Sigma^p$, de donde $\mathfrak B\models F$. Ninguna expansión requiere una elección simultánea de valores independientes para los símbolos nuevos: todos reciben interpretaciones uniformes. $\square$

**Límite exacto:** éste es un teorema de **satisfacibilidad finita** de $\Lambda^p$, no de existencia de un único modelo para toda $\Lambda$. La última conclusión necesitará una forma de compacidad sentencial apropiada al conjunto de símbolos empleados.


## 11.19. Completitud fuerte local para premisas numerables

### Metateorema 11.19.1 — Completitud fuerte local para premisas numerables {#tlog-mth-00044}

**Enunciado.** Sea $\tau$ una signatura cualquiera, incluso no bien ordenable, y $\Gamma\subseteq\operatorname{Fm}_\tau$ un conjunto **numerable** (finito o con inyección en $\omega$). Para toda $\varphi\in\operatorname{Fm}_\tau$,
$$
\boxed{\Gamma\models_\tau\varphi\iff
\Gamma\vdash_{\mathsf H_\tau^=}\varphi.}
$$
Es la consecuencia **local**: una única asignación satisface todas las premisas.

**Demostración.** La dirección $\vdash\Rightarrow\models$ es §10.9. Para la inversa razonamos por contraposición. Si $\Gamma\nvdash\varphi$, el test de consistencia y el teorema de deducción (§9.23) muestran que $\Lambda=\Gamma\cup\{\neg\varphi\}$ es consistente; de lo contrario $\Gamma\vdash\neg\neg\varphi$ y, por eliminación clásica de doble negación, $\Gamma\vdash\varphi$.

Por §11.18, toda parte finita de $\Lambda^p$ es satisfacible. La teoría $\Lambda^p$ es **numerable**, por ser imagen de un conjunto numerable más un elemento; no es necesario que la signatura ambiente $\tau^p$ sea numerable. Si $\Lambda^p\vdash\bot$, la finitariedad (§9.10) produciría un subconjunto finito $F\subseteq\Lambda^p$ que demuestra $\bot$; la corrección de §10 lo impediría porque $F$ posee un modelo. Por tanto $\Lambda^p$ es consistente.

Aplicamos §11.12, existencia de modelo para teorías **numerables** de sentencias en **cualquier** signatura: existe $\mathfrak B\models_{\tau^p}\Lambda^p$. Al tomar el reducto $\mathfrak A$ y la asignación $s(x)=c_x^{\mathfrak B}$, el lema §11.16 da $\mathfrak A,s\models\Gamma$ y $\mathfrak A,s\models\neg\varphi$. Éste es un contramodelo **local** de $\Gamma\models\varphi$. Se ha obtenido la contraposición deseada. $\square$

**Fundamento.** No se requirió AC, DC, elección numerable ni BPI. La numerabilidad afecta al **conjunto de premisas**, no necesariamente a todos los símbolos de $\tau$.


## 11.20. Adecuación, finitariedad semántica y compacidad local numerable

### Corolario 11.20.1 — Adecuación, finitariedad semántica y compacidad local numerable {#tlog-cor-00010}

Para cualquier $\tau$ y $\Gamma$ numerable, la corrección y completitud fuerte de §11.19 producen $\Gamma\vdash\varphi\iff\Gamma\models\varphi$; en consecuencia,
$$
\Gamma\models\varphi\iff
(\exists\Gamma_0\subseteq\Gamma\text{ finito})\;
\Gamma_0\models\varphi.
$$
La dirección no trivial usa completitud, finitariedad deductiva (§9.10) y corrección sobre el subconjunto finito. Además, si todo subconjunto finito de $\Gamma$ es **localmente satisfacible**, entonces existe una $\tau$-estructura $\mathfrak A$ y **una asignación** $s$ tales que $\mathfrak A,s\models\Gamma$. Si no, $\Gamma\models\bot_\tau$; la completitud produciría $\Gamma\vdash\bot_\tau$, y una prueba finita refutaría la satisfacibilidad de una parte finita. El caso de premisas sentenciales coincide con la compacidad del §11.11. $\square$

No se afirma aquí que la compacidad de **todos** los conjuntos de fórmulas de una firma arbitraria sea un teorema de ZF.


## 11.21. Régimen de buen orden y principio booleano de ideal primo

### Convención 11.21.1 — Régimen de buen orden y principio booleano de ideal primo {#tlog-cnv-00013}

Una signatura se llama **bien ordenable** si existe un buen orden sobre el conjunto de todos sus símbolos extralógicos (conservando sus aridades). Se puede fijar uno como **dato local** cuando existe; no se afirma que todas las signaturas admitan tal orden. Las palabras finitas sobre una firma bien ordenada forman un conjunto bien ordenable por longitud y orden lexicográfico; su orden puede escogerse constructivamente a partir del dato inicial, sin AC.

Se designa por **BPI** (*Boolean Prime Ideal Theorem*, equivalente al lema del ultrafiltro) el enunciado: «todo álgebra de Boole no trivial posee un ideal primo», equivalentemente «todo filtro propio en un álgebra de Boole admite extensión a ultrafiltro». Se distinguirán sistemáticamente tres niveles de fundamento:

- **ZF**: todas las construcciones sin BPI, incluso para firmas bien ordenables y conjuntos numerables de fórmulas;
- **ZF + BPI**: resultados generales para conjuntos de fórmulas sobre toda firma, sin bien ordenabilidad supuesta;
- **equivalencia sobre ZF**: afirmación de que la generalidad irrestricta de compacidad/completitud de primer orden tiene exactamente la fuerza de BPI.

BPI **no** se incorpora al contrato $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ del tratado: sus usos posteriores serán siempre hipótesis condicionales visibles. Tampoco se confundirá «firma bien ordenable» con «firma numerable».


## 11.22. Torre de Henkin sobre una signatura arbitraria, sin elección

### Lema 11.22.1 — Torre de Henkin sobre una signatura arbitraria, sin elección {#tlog-lem-00034}

**Enunciado.** Fijados cualquier signatura $L$ y conjunto consistente de **sentencias** $S\subseteq\operatorname{Sent}_L$, existe en ZF una expansión $L_\omega\supseteq L$ por constantes nularias y una teoría $T_H\subseteq\operatorname{Sent}_{L_\omega}$ consistente con $S\subseteq T_H$, de modo que para cada sentencia existencial $\delta=\exists x\rho$ del lenguaje final aparece en $T_H$ una instancia testigo $\delta\to\rho(c_\delta)$.

**Demostración.** Replicamos la construcción por niveles de §11.4, pero sin enumerar las sentencias. En el nivel $n$ formamos por separación el **conjunto** $E_n$ de todas las sentencias existenciales de $L_n$. Para cada $\delta\in E_n$ agregamos exactamente una constante nueva con etiqueta $(n,\delta)$, disjunta de las anteriores, y su axioma de Henkin. Todos los conjuntos están determinados por estas etiquetas, que **no se eligen**. Si un subconjunto finito de axiomas-testigo produjera contradicción, podríamos adjuntar los finitísimos axiomas uno por uno conservando consistencia mediante §11.3, ya que los nombres de constantes asignados son nuevos y mutuamente distintos. Contradicción. La finitariedad deductiva de §9.10 permite concluir consistencia de todos los axiomas-testigo del nivel a la vez. Inducimos sobre $n$ y tomamos las uniones de firmas y teorías: si la unión fuera inconsistente, una prueba finita estaría contenida en un nivel, imposible. Cada sentencia existencial de $L_\omega$ utiliza finitos símbolos nuevos y pertenece a algún $L_n$; allí recibe su testigo en el nivel siguiente. $\square$

**Precisión importante.** Esta torre —incluso para firmas no bien ordenables— **no** exige BPI. El punto en que una elección adicional podría ser indispensable es obtener una **teoría completa/maximal** de sentencias sobre un conjunto de símbolos sin buen orden, no añadir los testigos.


## 11.23. Modelo de Henkin en toda signatura bien ordenable, sin selector global

### Metateorema 11.23.1 — Modelo de Henkin en toda signatura bien ordenable, sin selector global {#tlog-mth-00045}

**Enunciado.** En ZF, si $L$ es **bien ordenable**, todo $S\subseteq\operatorname{Sent}_L$ consistente posee un modelo con universo no vacío. No hay restricción de cardinalidad ni de número de sentencias.

**Demostración, I: completar sin AC.** Fijamos un buen orden del alfabeto inicial. La torre de §11.22 adjunta etiquetas $(n,\delta)$ a fórmulas finitas; por recursión podemos bien ordenar los nuevos símbolos de cada nivel, el conjunto unión de símbolos de $L_\omega$ y las sentencias $\operatorname{Sent}_{L_\omega}$, sin elegir una sucesión arbitraria de órdenes. Indexamos dichas sentencias $(\theta_\xi)_{\xi<\alpha}$ por un ordinal $\alpha$. Partiendo de $T_H$, la recursión **transfinita determinista** agrega $\theta_\xi$ si mantiene consistencia, y en caso contrario agrega $\neg\theta_\xi$. En los ordinales límite toma uniones; cualquier contradicción en un límite dependería de una prueba y por tanto de finitas etapas anteriores. Los tests de consistencia y doble negación de §9.23 garantizan que la decisión negativa conserva consistencia. La unión final $T^*$ es consistente, decide todas las sentencias, es deductivamente cerrada **en sentencias** y hereda los axiomas-testigo de $T_H$.

**II: modelo cociente.** Sea $M=\operatorname{CTm}_{L_\omega}/\sim$, donde $t\sim u\iff (t\doteq u)\in T^*$. Interpretamos funciones y relaciones mediante términos cerrados como en §11.7. Las demostraciones de reflexividad, simetría, transitividad y congruencia de §9.17 aseguran que las interpretaciones son independientes del representante; $M$ es no vacío porque la expansión Henkin provee alguna constante nularia.

**III: verdad sin elección de representantes.** En un lenguaje **no necesariamente numerable** no damos por existente una sección global $r:M\to\operatorname{CTm}$. En cambio demostramos por inducción, para cada fórmula $\chi$ y **cada asignación finita** $a:V\to M$, $V\supseteq FV(\chi)$ finito, lo siguiente: elegidos representantes cerrados $t_x\in a(x)$ **solamente para los finitos $x\in V$**, la satisfacción de $\chi$ bajo cualquier asignación que extienda $a$ equivale a $\chi[t_x/x]_{x\in FV(\chi)}\in T^*$. La propiedad no depende de los representantes porque dos elecciones finitas dan tuplas de términos cerrados demostrablemente iguales y `E2`, congruencia y cierre sentencial transportan la pertenencia. Los átomos y cinco conectivos siguen §11.9. Para $\exists x$ se usa un testigo $c$ provisto por Henkin; para $\forall x$, una instancia cerrada por cada elemento $b\in M$ (escogiendo *un* representante de *ese* $b$, no de todos a la vez) y, en el sentido inverso, el testigo para $\exists x\neg\chi$. Las actualizaciones de asignaciones concuerdan por el lema de sustitución §8.11. La inducción implica que cada sentencia de $T^*$, y particularmente de $S$, es verdadera en la estructura. Tomamos el reducto a $L$. $\square$

**Control ZF.** Una elección finita es demostrable en ZF; una sección global del cociente de términos para una firma no numerable **no se ha supuesto**. Este detalle impide introducir inadvertidamente un principio de elección en el lema de verdad.


## 11.24. Completitud fuerte local y compacidad sobre firmas bien ordenables

### Metateorema 11.24.1 — Completitud fuerte local y compacidad sobre firmas bien ordenables {#tlog-mth-00046}

**Enunciado.** En ZF, dada una signatura **bien ordenable** $\tau$, para **todos** $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\varphi\in\operatorname{Fm}_\tau$,
$$
\boxed{\Gamma\models_\tau\varphi\iff\Gamma\vdash_{\mathsf H_\tau^=}\varphi.}
$$
Además, un conjunto cualquiera $\Gamma$ de fórmulas es localmente satisfacible si y sólo si todas sus partes finitas lo son.

**Demostración.** El lenguaje $\tau^p$ es bien ordenable: es la unión disjunta de los símbolos de $\tau$ con $\{c_x:x\in X\}$, explícitamente numerables. Si $\Gamma\nvdash\varphi$, $\Lambda=\Gamma\cup\{\neg\varphi\}$ es consistente (§9.23), y por §11.18 cada parte finita de $\Lambda^p$ tiene modelo. Por corrección y finitariedad, $\Lambda^p$ es sintácticamente consistente. Aplicamos existencia de modelo de §11.23 en el lenguaje **bien ordenable** $\tau^p$, sin requerir que $\Lambda^p$ sea numerable. Su modelo produce el contramodelo local por §11.16. La otra implicación sigue de §10.9. Para compacidad local repetimos el argumento con $\Lambda=\Gamma$ y prescindimos de $\neg\varphi$; la teoría parametrizada es finitamente satisfacible y obtiene modelo. $\square$

**Alcance:** no se ha elegido un buen orden para una firma **no bien ordenable**. El teorema es enteramente de ZF, pero su hipótesis de bien ordenabilidad **no** puede suprimirse por decreto.


## 11.25. BPI proporciona modelos a toda teoría consistente de sentencias

### Metateorema 11.25.1 — BPI proporciona modelos a toda teoría consistente de sentencias {#tlog-mth-00047}

**Enunciado condicional.** En **ZF+BPI**, para una signatura arbitraria $L$ y un conjunto consistente $S\subseteq\operatorname{Sent}_L$, existe $\mathfrak A\models_L S$.

**Demostración.** Construimos en ZF la teoría Henkin $T_H$ en $L_\omega$ mediante §11.22. Definimos sobre $\operatorname{Sent}_{L_\omega}$ la equivalencia $\theta\approx\eta\iff T_H\vdash\theta\leftrightarrow\eta$. Las reglas proposicionales, la deducción y el cierre lógico prueban que el cociente $\mathbb B=\operatorname{Sent}_{L_\omega}/\!\approx$, con operaciones inducidas por $\neg,\land,\lor$, es un álgebra de Boole. Su $0$ es la clase de $\bot$, su $1$ la de una sentencia teorema $\kappa$; por consistencia, $0\ne1$. **Aquí y solamente aquí invocamos BPI:** existe un ultrafiltro $U$ en $\mathbb B$.

Definimos $T^*=\{\theta\in\operatorname{Sent}_{L_\omega}:[\theta]\in U\}$. El ultrafiltro contiene los teoremas de $T_H$, evita $\bot$, y decide exactamente una de $\theta,\neg\theta$ para cada sentencia. Si $T^*\vdash\sigma$ para una **sentencia** $\sigma$, una prueba usa finitas premisas sentenciales $\gamma_1,\ldots,\gamma_n\in T^*$; el teorema de deducción del §9.15 permite internalizarlas y obtener $\vdash\gamma_1\to(\cdots(\gamma_n\to\sigma)\cdots)$. Por las leyes booleanas de $U$, $[\sigma]\in U$, de modo que $\sigma\in T^*$. En particular, los axiomas $\delta\to\rho(c_\delta)\in T_H$ y `MP` aseguran testigos cerrados para todos los existenciales $\delta\in T^*$.

Construimos el modelo cociente de términos cerrados como en §11.23, utilizando congruencia de igualdad y el lema de verdad para **asignaciones finitas**. Aquí el lenguaje podría no admitir buen orden ni sección global del cociente, pero cada paso de evaluación requiere sólo finitos representantes, obtenibles en ZF. Todas las sentencias de $T_H\supseteq S$ son verdaderas en el modelo; reducimos al lenguaje inicial. $\square$

No se ha utilizado Zorn ni el axioma completo de elección. Si se retira BPI, esta demostración **no** produce en general un ultrafiltro sobre $\mathbb B$.


## 11.26. BPI implica completitud fuerte y compacidad irrestrictas

### Metateorema 11.26.1 — BPI implica completitud fuerte y compacidad irrestrictas {#tlog-mth-00048}

**Enunciado condicional.** Bajo **ZF+BPI**, para toda signatura $\tau$, sin hipótesis de numerabilidad ni buen orden, y para cualquier conjunto $\Gamma$ de fórmulas abiertas o cerradas,
$$
\boxed{\Gamma\vdash\varphi\iff\Gamma\models_\tau\varphi,}
$$
y toda familia de fórmulas localmente satisfacible sobre cada parte finita posee una **misma estructura y una misma asignación** que satisfacen el conjunto completo.

**Demostración.** Si $\Gamma\nvdash\varphi$, $\Lambda=\Gamma\cup\{\neg\varphi\}$ es consistente (§9.23). La teoría de parámetros $\Lambda^p$ es finitamente satisfacible en $\tau^p$ por §11.18. La corrección y la finitariedad implican consistencia de $\Lambda^p$. El teorema anterior, **que usa BPI**, le da un modelo. El lema de parámetros produce un contramodelo local a $\Gamma\models\varphi$. La otra dirección es el teorema de corrección §10.9, que no requiere BPI.

Para compacidad de conjuntos de fórmulas, suponemos cada parte finita localmente satisfacible. Toda parte finita de $\Gamma^p$ es satisfacible (se amplía una estructura y se interpretan las constantes según los valores de la asignación testigo); por finitariedad y corrección, $\Gamma^p$ es consistente. La existencia de modelo para sentencias con BPI y el lema de parámetros entregan una estructura y **una única asignación** que satisfacen $\Gamma$. $\square$

**Distinción:** el condicional $\mathrm{BPI}\Rightarrow\mathrm{completitud/compacidad}$ es un teorema de ZF. No se afirma $\mathrm{ZF}\vdash\mathrm{BPI}$.


## 11.27. La compacidad irrestricta de primer orden implica BPI

### Metateorema 11.27.1 — La compacidad irrestricta de primer orden implica BPI {#tlog-mth-00049}

**Enunciado.** Trabajando en ZF, si para **toda** signatura y **todo** conjunto de sentencias cada subteoría finita con modelo implica existencia de modelo global, entonces vale BPI.

**Demostración.** Sea $B$ un álgebra de Boole **no trivial**. Formamos la signatura $\tau_B$ con una constante distinta $c_b$ por cada $b\in B$ y un predicado unario $U$. Formamos la teoría $\mathcal T_B$ con las siguientes **sentencias**:
$$
\begin{aligned}
&U(c_{1_B}),\qquad\neg U(c_{0_B}),\\
&U(c_{b\wedge d})\leftrightarrow(U(c_b)\land U(c_d)),\qquad (b,d\in B),\\
&U(c_{\neg b})\leftrightarrow\neg U(c_b),\qquad (b\in B).
\end{aligned}
$$
Por reemplazo y separación, $\mathcal T_B$ es un conjunto, sin necesidad de bien ordenar $B$.

**Satisfacibilidad finita.** Dada una parte finita $F\subseteq\mathcal T_B$, sea $E\subseteq B$ el conjunto finito de los índices de todas las constantes que efectivamente figuran en $F$, junto a $0_B,1_B$. La subálgebra de Boole $B_E$ generada por $E$ es **finita**: cada elemento es una combinación booleana de un número fijo finito de generadores. Como $B$ es no trivial, también $B_E$ lo es, y posee un átomo $a$. La función $h:B_E\to\{0,1\}$, $h(b)=1\iff a\le b$, es un homomorfismo booleano. Construimos una estructura de universo **$B$**, interpretando cada $c_b$ como $b$ y $U$ mediante el subconjunto $\{b\in B_E:h(b)=1\}\subseteq B$ (fuera de $B_E$ interpretamos $U$ como falso). Cada sentencia de $F$ sólo menciona constantes indexadas por elementos de $E$, donde $h$ satisface las identidades; así $F$ tiene modelo. Esta elección de un átomo de **un álgebra finita** está disponible en ZF y no produce una familia de elecciones arbitrarias.

Por la **hipótesis de compacidad irrestricta** existe una $\tau_B$-estructura $\mathfrak M\models\mathcal T_B$. Definimos $v:B\to\{0,1\}$ por $v(b)=1\iff\mathfrak M\models U(c_b)$. Las sentencias de $\mathcal T_B$ prueban $v(1)=1$, $v(0)=0$, $v(b\wedge d)=v(b)\land v(d)$ y $v(\neg b)=1-v(b)$. Por dualidad booleana, $v$ preserva todas las operaciones; $I=v^{-1}(\{0\})$ es un ideal primo de $B$. Como $B$ era arbitraria, vale BPI. $\square$

**Alcance:** el argumento presupone la **versión sobre todas las signaturas** de compacidad; no permite inferir BPI a partir del fragmento numerable de los apartados anteriores.


## 11.28. Fuerza exacta de compacidad y completitud en ZF

### Corolario 11.28.1 — Fuerza exacta de compacidad y completitud en ZF {#tlog-cor-00011}

**Enunciado.** En la metateoría ZF son equivalentes las afirmaciones siguientes:

1. BPI, o lema del ultrafiltro sobre todo álgebra de Boole no trivial.
2. Compacidad de conjuntos de **sentencias** para toda signatura.
3. Compacidad **local** de conjuntos de fórmulas, abiertas o cerradas, para toda signatura.
4. Completitud fuerte $\Gamma\models_\tau\varphi\Rightarrow\Gamma\vdash_{\mathsf H_\tau^=}\varphi$ para toda signatura y cualesquiera premisas abiertas.

**Demostración.** (1) implica (2) por §11.25 (existencia de modelo para teorías consistentes) y finitariedad/corrección; también implica (3) y (4) por §11.26. (3) implica (2) restringiendo a sentencias. (2) implica (1) por la codificación de álgebras de Boole del §11.27. Por último, (4) implica (2): si cada parte finita de una teoría sentencial $S$ es satisfacible, la corrección y finitariedad implican $S\nvdash\bot$. Si $S$ no tuviera modelo, semánticamente $S\models\bot$, y por (4) existiría una derivación de $\bot$, contradicción. $\square$

No hay contradicción con los resultados de ZF de §§11.19 y 11.24: allí las teorías o las signaturas poseen estructuras de enumeración/buen orden explícitas; aquí se cuantifica sobre **todas** las signaturas sin tal dato. El capítulo no confunde «equivalencia demostrada en ZF» con «BPI demostrado en ZF».


## 11.29. Vector de adecuación por hipótesis y cierre tipado

### Corolario 11.29.1 — Vector de adecuación por hipótesis y cierre tipado {#tlog-cor-00012}

Quedan demostrados los siguientes niveles, sin interpolar hipótesis:

| Metateoría | Lenguaje y premisas | Resultado |
|---|---|---|
| ZF | Premisas numerables; signatura arbitraria | corrección + completitud local y compacidad local |
| ZF | Signatura bien ordenable; premisas arbitrarias | corrección + completitud local y compacidad local |
| ZF+BPI | Signatura y premisas arbitrarias | corrección + completitud local y compacidad local |
| ZF | Cuantificación irrestricta sobre toda signatura | **equivalente a BPI**, no se declara incondicional |

La finitariedad semántica $\Gamma\models\varphi\iff\exists\Gamma_0\subseteq\Gamma\text{ finito}\ (\Gamma_0\models\varphi)$ está demostrada dentro de cada uno de los tres regímenes positivos de la tabla: se combina completitud fuerte, finitariedad de pruebas y corrección. La conclusión no transforma una relación local en consecuencia global, ni define $\vdash$ mediante $\models$. Tampoco se afirma una prueba mecánica Lean. $\square$

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 10](capitulo-10.md) · [Capítulo 12 →](capitulo-12.md)


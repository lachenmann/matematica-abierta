---
title: Capítulo 15 — Equivalencias, cocientes y órdenes
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
content-id: MA-BCH-0217
content-type: book-chapter
source-id: TLOG-CH15-0001
prerequisites:
- MA-BCH-0214
- MA-BCH-0215
- MA-BCH-0216
related:
- MA-BOK-0014
source-sha256: f79df2da2a92ed4b1b23ce38b2cc9a29122245a050ceaccc562c915553bc299e
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 14](capitulo-14.md) · [Capítulo 16 →](capitulo-16.md)

## 15.0. Del grafo de una relación a sus clases

El Capítulo 14 construyó, **dentro de la teoría objeto** $\mathsf{ZF}_{\mathrm{obj}}$, los códigos de pares ordenados, los productos cartesianos, las relaciones binarias y las funciones como conjuntos. Aquí se estudian las equivalencias **sobre un conjunto fijado** $A$, se forman sus clases por separación, se construye el cociente como un subconjunto de $\mathcal P(A)$ y se precisa cuándo una función desciende a ese cociente. Los órdenes y las nociones de buena definición asociadas a ellos se desarrollan en `CH15-M02`, §§15.21–15.41.

**Nivel fundacional.** La signatura objeto sigue siendo $\tau_{\in}$, cuyo único símbolo extralógico primitivo es $\in$. Las escrituras $\langle a,b\rangle$, $A\times B$, $[a]_E$, $A/E$, $f(a)$, $\ker(f)$ y $\pi_E$ son macros eliminables, con sus guardas y variables auxiliares frescas. La metateoría $\mathsf M_{\mathrm{ext}}$ es ZF clásica sin AC; no se presupone que toda sobreyección admita una sección. Las pruebas objeto quedan reconstruidas mediante instancias de separación, extensionalidad, pares y potencia ya justificadas, y no por importación de una axiomática exterior.

**Procedencia:** reconstrucción matemática interna sobre los resultados cerrados de los capítulos 12–14. `TLOG-SRC-0002`, `TLOG-SRC-0003` y `TLOG-SRC-00011` conservan su alcance bibliográfico previamente registrado; este microtramo no declara nuevas páginas cotejadas.

## 15.1. Convención de tipado de una equivalencia

### Convención 15.1.1 — Equivalencias relativas a un conjunto base {#tlog-cnv-00021}

Una **equivalencia sobre $A$** será un conjunto $E\subseteq A\times A$, no una supuesta relación sobre el universo de todos los conjuntos. Escribiremos $a\mathrel{E}b$ por $\langle a,b\rangle\in E$. La letra $E$ denota el grafo; el conjunto base $A$ es un dato indispensable del tipo $\operatorname{Equiv}_A(E)$. La notación $[a]_E$ requerirá $a\in A$; la proyección $\pi_E:A\to A/E$ y las flechas inducidas serán funciones *conjuntistas* definidas más adelante, no símbolos primitivos.

**Regla de lectura:** $\operatorname{Equiv}_A(E)$ es una fórmula del lenguaje original tras expansión de las macros. Toda generalización objeto se efectuará descargando previamente las hipótesis de parámetros, con variables ligadas frescas. Las proposiciones sobre familias de equivalencias en un $A$ fijo hablarán de **conjuntos acotados** por $\mathcal P(A\times A)$, no de clases propias tratadas como miembros de otros conjuntos.

## 15.2. Predicado de equivalencia

### Definición 15.2.1 — Reflexividad, simetría y transitividad con guarda {#tlog-def-00083}

Introducimos la abreviación de primer orden
$$
\boxed{\begin{aligned}
\operatorname{Equiv}_A(E):\Longleftrightarrow {}& E\subseteq A\times A\\
&\land\forall a\in A\ (aEa)\\
&\land\forall a,b\in A\ (aEb\to bEa)\\
&\land\forall a,b,c\in A\ ((aEb\land bEc)\to aEc).
\end{aligned}}
$$

La notación $\forall a\in A$ representa $\forall a(a\in A\to\cdots)$; $aEb$ significa $\langle a,b\rangle\in E$ mediante $\Delta_K$ y no introduce símbolo relacional nuevo. Los casos $A=\varnothing$, $E=\varnothing$ están **incluidos**: $\operatorname{Equiv}_{\varnothing}(\varnothing)$ es verdadera.

## 15.3. Criterio algebraico de equivalencia

### Proposición 15.3.1 — Diagonal, conversa y composición {#tlog-pro-00066}

Para un conjunto $E\subseteq A\times A$, la teoría objeto demuestra
$$
\boxed{\operatorname{Equiv}_A(E)\iff
\bigl(\operatorname{id}_A\subseteq E\ \land\ E^{\smile}=E\ \land\ E\circ E\subseteq E\bigr).}
$$

**Demostración.** La reflexividad da $\langle a,a\rangle\in E$ para todo $a\in A$, es decir, $\operatorname{id}_A\subseteq E$. La simetría muestra igualdad de las relaciones $E^{\smile}$ y $E$ comparando cada código ordenado; el criterio extensional de §14.14 legitima la igualdad de conjuntos. Si $\langle a,c\rangle\in E\circ E$, existe $b$ con $aEb$ y $bEc$; como $E\subseteq A\times A$, las tres coordenadas pertenecen a $A$, y la transitividad da $aEc$. Recíprocamente, inclusión de la identidad implica reflexividad; igualdad con la conversa, simetría; y la inclusión de la composición, transitividad, pues $aEb\land bEc$ suministra el testigo $b$ en la composición. No se usa elección, y las tres operaciones son conjuntos por §14.28 y §14.31. $\square$

## 15.4. Clase de un elemento

### Definición 15.4.1 — Gráfica pura de la clase relativa {#tlog-def-00084}

**Bajo las guardas** $\operatorname{Equiv}_A(E)$ y $a\in A$, describimos la clase de $a$ como el único conjunto $C$ que satisface
$$
\boxed{\operatorname{Class}(C,a,E,A):\Longleftrightarrow
\forall x\bigl(x\in C\leftrightarrow(x\in A\land aEx)\bigr).}
$$

Al acreditar existencia y unicidad escribiremos $[a]_E:=C$. Esta expresión **no** es una aplicación global de clases sin base: sólo nombra un subconjunto del conjunto fijado $A$. Su expansión elimina $aEx$, todos los cuantificadores acotados y cualquier término nuevo por las grafías del Capítulo 14, con renombrados alfa que eviten captura.

## 15.5. Existencia y pertenencia a una clase

### Proposición 15.5.1 — Existencia, unicidad y testigo interno {#tlog-pro-00067}

Se prueba en $\mathsf{ZF}_{\mathrm{obj}}$ el cierre universal de
$$
\boxed{\operatorname{Equiv}_A(E)\land a\in A
\ \Longrightarrow\ \exists!C\,\operatorname{Class}(C,a,E,A).}
$$
Para su valor único:
$$
\boxed{[a]_E\subseteq A,\quad a\in[a]_E,\quad
x\in[a]_E\iff(aEx)\ \text{cuando }x\in A.}
$$

**Demostración.** La matriz $x\in A\land aEx$ es fórmula pura (después de expandir el código de Kuratowski). Separación en $A$ forma $C=\{x\in A:aEx\}$, que satisface la gráfica. Si $C'$ la satisface también, la bicondicional para todo $x$ da $C=C'$ por extensionalidad. La reflexividad y $a\in A$ dan $aEa$, por lo cual $a\in C$; así $C\ne\varnothing$. Para $x\in A$, la guarda de pertenencia a $A$ se simplifica a la equivalencia mostrada. No se invoca reemplazo ni se escoge un testigo por cada clase: $a$ es el único parámetro de esta derivación. $\square$

## 15.6. Igualdad de clases

### Lema 15.6.1 — Criterio fundamental de coincidencia {#tlog-lem-00042}

Para $a,b\in A$, y bajo $\operatorname{Equiv}_A(E)$, se demuestra
$$
\boxed{aEb\iff[a]_E=[b]_E.}
$$
Además, para $x\in A$, $x\in[a]_E\iff[x]_E=[a]_E$.

**Demostración.** Si $aEb$ y $z\in[a]_E$, la pertenencia da $aEz$; por simetría, $bEa$, y por transitividad $bEz$, de modo que $z\in[b]_E$. La inclusión opuesta se obtiene intercambiando $a,b$; extensionalidad entrega igualdad. Si $[a]_E=[b]_E$, la reflexividad da $b\in[b]_E$; por igualdad $b\in[a]_E$, luego $aEb$ por la propiedad de la clase. El último bicondicional combina esta equivalencia con §15.5 y simetría de la igualdad. Todas las aplicaciones de simetría/transitividad se hacen con $a,b,z\in A$, lo cual sigue de las guardas. $\square$

## 15.7. Disyunción de clases

### Proposición 15.7.1 — Coincidencia o disjunción, sin elección {#tlog-pro-00068}

Si $a,b\in A$, entonces
$$
\boxed{[a]_E=[b]_E\quad\lor\quad[a]_E\cap[b]_E=\varnothing.}
$$
Para cada $x\in A$, existe una clase que lo contiene, a saber $[x]_E$, y **dos clases que contienen $x$ son necesariamente iguales**.

**Demostración.** Si la intersección no es vacía, se elimina un único existencial y se toma $z\in[a]_E\cap[b]_E$. De $aEz$ y $bEz$ se deriva $aEb$ por simetría y transitividad; §15.6 da igualdad de clases. En consecuencia, si no son iguales, su intersección es vacía. Reflexividad garantiza $x\in[x]_E$. Si $x\in[a]_E\cap[b]_E$, acabamos de probar que ambas clases coinciden. La prueba utiliza **un testigo local** para una intersección particular, no una elección simultánea de representantes. $\square$

## 15.8. Descripción del cociente

### Definición 15.8.1 — Cociente acotado por el conjunto potencia {#tlog-def-00085}

Bajo $\operatorname{Equiv}_A(E)$ definimos el grafo de cociente para la variable conjunto $Q$:
$$
\boxed{\operatorname{Quot}(Q,A,E):\Longleftrightarrow
Q\subseteq\mathcal P(A)\ \land\
\forall C\in\mathcal P(A)\bigl[C\in Q\leftrightarrow
\exists a\in A\,\operatorname{Class}(C,a,E,A)\bigr].}
$$
La notación $A/E$ quedará activada después de probar $\exists!Q\operatorname{Quot}(Q,A,E)$. La cota $\mathcal P(A)$ es esencial: **no** postulamos por comprensión irrestricta «el conjunto de todas las clases» de todos los conjuntos. Se trata exclusivamente de clases de elementos de un $A$ dado.

## 15.9. Existencia del conjunto cociente

### Proposición 15.9.1 — Construcción efectiva del cociente y casos vacíos {#tlog-pro-00069}

En la teoría objeto se demuestra
$$
\boxed{\operatorname{Equiv}_A(E)\ \Longrightarrow\
\exists!Q\,\operatorname{Quot}(Q,A,E).}
$$
El único $Q=A/E$ satisface:
$$
\begin{aligned}
&A/E\subseteq\mathcal P(A),\qquad \varnothing\notin A/E,\\
&\forall a\in A\quad [a]_E\in A/E,\\
&\bigcup(A/E)=A,\qquad
 A/E=\varnothing\iff A=\varnothing.
\end{aligned}
$$
Además, los miembros distintos de $A/E$ son disjuntos.

**Demostración.** El axioma de potencia proporciona $P=\mathcal P(A)$, ya construido en §13.10. Separa en $P$ los $C$ que verifican $\exists a\in A\,\operatorname{Class}(C,a,E,A)$. El predicado es fórmula pura, con $a,E,A$ libres como parámetros sólo donde corresponde y las variables auxiliares de $\operatorname{Class}$ renombradas antes de insertarla. La separación entrega $Q\subseteq P$ y el bicondicional definitorio; extensionalidad garantiza unicidad. Cada clase contiene a su representante (§15.5), de modo que ninguna es vacía. Por §15.5, toda clase es subconjunto de $A$, así que $\bigcup Q\subseteq A$; para $x\in A$, $x\in[x]_E\in Q$, luego $x\in\bigcup Q$. La disjunción de bloques distintos es §15.7. Si $A=\varnothing$, no hay testigos $a$ para la matriz y $Q=\varnothing$; si $A\ne\varnothing$, un solo testigo $a\in A$ produce $[a]_E\in Q$. Ninguna familia de elecciones se requiere. $\square$

## 15.10. Particiones de un conjunto

### Definición 15.10.1 — Partición con tratamiento exacto de $A=\varnothing$ {#tlog-def-00086}

Una **partición de $A$** es un conjunto $\Pi$ que cumple
$$
\boxed{\operatorname{Part}_A(\Pi):\Longleftrightarrow
\Pi\subseteq\mathcal P(A)\ \land\
\varnothing\notin\Pi\ \land\
\forall a\in A\ \exists!C\in\Pi\ (a\in C).}
$$
El último término significa que **cada** $a$ pertenece a exactamente un bloque. Es equivalente a $\bigcup\Pi=A$ y disjunción de bloques distintos, suponiendo las dos primeras condiciones. La partición del conjunto vacío es $\Pi=\varnothing$, sin excepción ad hoc ni elección de un bloque inexistente.

## 15.11. Equivalencia inducida por una partición

### Proposición 15.11.1 — Construcción por separación sobre $A\times A$ {#tlog-pro-00070}

Si $\operatorname{Part}_A(\Pi)$, existe un único conjunto
$$
\boxed{E_\Pi:=\bigl\{\langle a,b\rangle\in A\times A:
\exists C\in\Pi\ (a\in C\land b\in C)\bigr\}}
$$
con $\operatorname{Equiv}_A(E_\Pi)$. Para $a\in A$, $[a]_{E_\Pi}$ es exactamente el **único** bloque de $\Pi$ que contiene a $a$.

**Demostración.** El producto $A\times A$ existe por §14.7. Separación en ese producto forma $E_\Pi$, y extensionalidad prueba que es el único con la condición indicada. Para $a\in A$, el axioma de partición entrega el único bloque $C_a\in\Pi$ que contiene a $a$; por tanto $aE_\Pi a$. Si $aE_\Pi b$, ambos pertenecen a un bloque y la misma condición con las variables permutadas da $bE_\Pi a$. Si $aE_\Pi b$ y $bE_\Pi c$, existen bloques $C,D$ con $a,b\in C$ y $b,c\in D$; como $b$ pertenece a exactamente un bloque, $C=D$, y por tanto $aE_\Pi c$. Finalmente, $x\in[a]_{E_\Pi}$ equivale a compartir un bloque con $a$, y la unicidad del bloque obliga a que $x\in C_a$. La inclusión inversa es inmediata. No se define ninguna función de elección $a\mapsto C_a$ mediante elecciones arbitrarias: la unicidad es una propiedad **demostrada** por la partición. $\square$

## 15.12. Correspondencia exacta entre particiones y equivalencias

### Metateorema 15.12.1 — La correspondencia es una biyección de conjuntos {#tlog-mth-00060}

Para $A$ fijo, las operaciones $E\mapsto A/E$ y $\Pi\mapsto E_\Pi$ establecen biyecciones inversas entre los **conjuntos**
$$
\begin{aligned}
\operatorname{EqRel}(A)&:=\{E\in\mathcal P(A\times A):\operatorname{Equiv}_A(E)\},\\
\operatorname{Part}(A)&:=\{\Pi\in\mathcal P(\mathcal P(A)):\operatorname{Part}_A(\Pi)\}.
\end{aligned}
$$
En particular,
$$
\boxed{E_{A/E}=E,\qquad A/E_\Pi=\Pi.}
$$

**Demostración.** Los dos dominios son conjuntos por dos aplicaciones del axioma de potencia y separación. Para $a,b\in A$, por definición $aE_{A/E}b$ si existe una clase de $A/E$ que los contenga. De §15.7 resulta que esa clase debe ser $[a]_E=[b]_E$, equivalente a $aEb$ por §15.6. Como las relaciones están contenidas en $A\times A$, el criterio extensional de §14.14 da $E_{A/E}=E$. Para $\Pi$, §15.11 demuestra que las clases de $E_\Pi$ son exactamente sus bloques: cada clase es un bloque y cada bloque no vacío contiene algún $a\in A$, cuya clase es ese bloque. Por extensionalidad, $A/E_\Pi=\Pi$. Estas correspondencias tienen **valor único** para cada entrada, así que sus grafos son conjuntos obtenibles por separación de $\operatorname{EqRel}(A)\times\operatorname{Part}(A)$ y del producto opuesto. No se escoge ningún representante por bloque; la construcción también vale si $A=\varnothing$. $\square$

## 15.13. Gráfica de la proyección canónica

### Definición 15.13.1 — Proyección al cociente por separación {#tlog-def-00087}

Dados $A,E$ con $\operatorname{Equiv}_A(E)$, y $Q=A/E$ ya construido, definimos
$$
\boxed{\pi_E:=\bigl\{\langle a,C\rangle\in A\times Q:
\operatorname{Class}(C,a,E,A)\bigr\}.}
$$
La formación de $\pi_E$ por separación es **una construcción de un conjunto**, sin función primitiva $[\cdot]_E$ y sin elección global. Su lectura $\pi_E(a)=[a]_E$ requerirá $a\in A$, bajo las guardas que vuelven única esa clase.

## 15.14. La proyección como aplicación sobreyectiva

### Proposición 15.14.1 — Sobreyección, fibras e igualdad de valores {#tlog-pro-00071}

Para $\operatorname{Equiv}_A(E)$, ZF objeto prueba que la gráfica de §15.13 satisface $\pi_E:A\to A/E$, que es **sobreyectiva respecto del codominio $A/E$**, y que
$$
\boxed{\begin{aligned}
\pi_E(a)&=[a]_E\quad(a\in A),\\
\pi_E(a)=\pi_E(b)&\iff aEb\quad(a,b\in A),\\
\pi_E^{-1}[\{[a]_E\}]&=[a]_E\quad(a\in A).
\end{aligned}}
$$

**Demostración.** §15.5 da para cada $a\in A$ un $C$ único con $\operatorname{Class}(C,a,E,A)$; §15.9 garantiza que ese $C$ pertenece a $Q$. Por la condición de separación, $\pi_E$ es el grafo de una función con dominio exacto $A$ y recorrido contenido en $Q$. Para todo $C\in Q$, por definición de cociente existe $a\in A$ con $C=[a]_E=\pi_E(a)$; esto demuestra sobreyectividad, tomando **un testigo por cada demostración particular**, no una elección simultánea para todos los bloques. La equivalencia de igualdad de imágenes es §15.6. Por último, para $x\in A$, $x$ pertenece a la preimagen del singleton $\{[a]_E\}$ exactamente cuando $\pi_E(x)=\pi_E(a)$, esto es, $xEa$, equivalente por simetría a $aEx$ y a $x\in[a]_E$. Extensionalidad concluye. Si $A=\varnothing$, ambas partes de la flecha son vacías y la sobreyectividad es vacua, sin usar ningún testigo. $\square$

## 15.15. Criterio de descenso de funciones

### Metateorema 15.15.1 — Propiedad universal del cociente {#tlog-mth-00061}

Sean $\operatorname{Equiv}_A(E)$ y $f:A\to B$. Son equivalentes:

1. $f$ es **constante en cada clase**: $\forall a,b\in A\,(aEb\to f(a)=f(b))$.
2. Existe **una única** aplicación $\bar f:A/E\to B$ con $f=\bar f\circ\pi_E$.

En tal caso $\operatorname{ran}(\bar f)=\operatorname{ran}(f)$, y la aplicación viene determinada por
$$
\boxed{\bar f([a]_E)=f(a).}
$$

**Demostración.** Supongamos constancia. Dentro del producto existente $(A/E)\times B$ separamos los pares $\langle C,b\rangle$ para los que $\exists a\in A\,(C=[a]_E\land\langle a,b\rangle\in f)$. Si dos representantes $a,a'$ dan la misma clase, §15.6 prueba $aEa'$; la constancia fuerza $f(a)=f(a')$, por lo cual la relación separada es funcional. Toda clase tiene al menos un representante por definición de $A/E$, y $f$ es total en $A$; así, el grafo tiene dominio exacto $A/E$ y recorrido contenido en $B$. Lo llamamos $\bar f$. Su definición da $\bar f(\pi_E(a))=f(a)$ para cada $a\in A$, lo cual es igualdad de grafos $f=\bar f\circ\pi_E$, por las leyes de composición de §14.29–§14.30. Si $g$ también cumple esa identidad, toda clase $C\in A/E$ es $C=\pi_E(a)$ para algún $a\in A$, y entonces $g(C)=f(a)=\bar f(C)$; por extensionalidad funcional, $g=\bar f$. Recíprocamente, si $f=g\circ\pi_E$ y $aEb$, §15.14 implica $\pi_E(a)=\pi_E(b)$, luego $f(a)=f(b)$. La igualdad de recorridos sigue porque $\pi_E$ es sobreyectiva; para cada imagen de uno de los grafos hay un preimagen concreta en el otro. Si $A=\varnothing$, $A/E=\varnothing$ y los dos grafos son la función vacía, por lo que sigue habiendo unicidad sin exigir $B\ne\varnothing$. $\square$

**Distinción:** este descenso **no selecciona representantes**; define el valor en una clase por independencia demostrada del representante.

## 15.16. Transporte entre cocientes

### Proposición 15.16.1 — Aplicaciones compatibles e identidad/composición inducidas {#tlog-pro-00072}

Supongamos $\operatorname{Equiv}_A(E)$, $\operatorname{Equiv}_B(F)$ y $f:A\to B$. Si
$$
\forall a,a'\in A\,\bigl(aEa'\to f(a)\mathrel{F}f(a')\bigr),
$$
existe una única aplicación inducida $\widetilde f:A/E\to B/F$ tal que
$$
\boxed{\widetilde f([a]_E)=[f(a)]_F,\qquad
\pi_F\circ f=\widetilde f\circ\pi_E.}
$$
Cuando se componen aplicaciones compatibles, se conserva la ley $\widetilde{g\circ f}=\widetilde g\circ\widetilde f$; la identidad de $A$ induce la identidad de $A/E$.

**Demostración.** La función compuesta $h=\pi_F\circ f:A\to B/F$ existe por §14.29. Si $aEa'$, la hipótesis da $f(a)Ff(a')$; §15.14 aplicado a $F$ asegura $h(a)=h(a')$. Por el criterio de descenso §15.15, existe una única $\widetilde f$ con $h=\widetilde f\circ\pi_E$. Evaluando esta igualdad en $a$, obtenemos la fórmula indicada. Para $g:B\to C$ compatible con $F$ y otra equivalencia $G$ sobre $C$, tanto $\widetilde{g\circ f}$ como $\widetilde g\circ\widetilde f$ hacen conmutar el mismo compuesto con $\pi_E$. La unicidad del descenso da la igualdad; el caso identidad es idéntico. Todo el argumento utiliza composición de grafos conjuntistas y unicidad, no elección de un representante por clase. $\square$

## 15.17. Equivalencia núcleo de una aplicación

### Definición 15.17.1 — Núcleo relativo al dominio {#tlog-def-00088}

Para una flecha tipada $f:A\to B$, su **equivalencia núcleo** se define por separación en $A\times A$:
$$
\boxed{\operatorname{Ker}_A(f):=
\{\langle a,a'\rangle\in A\times A:f(a)=f(a')\}.}
$$
Esta notación requiere el dominio $A$, aun cuando el grafo determine $\operatorname{dom}(f)=A$. La matriz se desarrolla usando las gráficas de evaluación segura del Capítulo 14. La existencia del conjunto se sigue directamente de separación; su carácter de equivalencia y la estructura del cociente núcleo se demostrarán en el resultado siguiente.

## 15.18. Primer teorema de isomorfismo conjuntista

### Metateorema 15.18.1 — Cociente por núcleo e imagen exacta {#tlog-mth-00062}

Para toda función $f:A\to B$, el conjunto $E=\operatorname{Ker}_A(f)$ es una equivalencia sobre $A$ y existe una única biyección
$$
\boxed{\widehat f:A/E\ \longrightarrow\ \operatorname{ran}(f),\qquad
\widehat f([a]_E)=f(a),}
$$
que factoriza $f$ como $A\xrightarrow{\pi_E}A/E\xrightarrow{\widehat f}\operatorname{ran}(f)\hookrightarrow B$.

**Demostración.** Por definición, $E\subseteq A\times A$. Reflexividad de igualdad produce $f(a)=f(a)$; simetría y transitividad de igualdad se transportan a las condiciones de §15.2. Así $\operatorname{Equiv}_A(E)$. Sea $R=\operatorname{ran}(f)\subseteq B$, un conjunto construido por §14.12. El mismo grafo $f$ constituye una aplicación $A\to R$, porque su recorrido es exactamente $R$. La condición de constancia sobre las clases de $E$ es su definición; §15.15 da entonces una única $\widehat f:A/E\to R$ tal que $f=\widehat f\circ\pi_E$. Es sobreyectiva: dado $y\in R$, existe $a\in A$ con $f(a)=y$, y $\widehat f([a]_E)=y$. Es inyectiva: si $\widehat f([a]_E)=\widehat f([b]_E)$, entonces $f(a)=f(b)$, de donde $aEb$, y §15.6 implica $[a]_E=[b]_E$. En el caso $A=\varnothing$, el cociente y el recorrido son vacíos y la única aplicación vacía es biyectiva, sin excepción. Ningún paso requiere escoger un representante simultáneo de cada clase. La inclusión $R\hookrightarrow B$ es la identidad restringida de §14.28, y da la factorización final. $\square$

## 15.19. Frontera fundacional y salida local

### Corolario 15.19.1 — Cocientes y descenso sin elección de representantes {#tlog-cor-00018}

**Demostración (síntesis de resultados previos).** Los resultados §§15.1–15.18 prueban que, en ZF objeto y **sin axioma de elección**, cada equivalencia sobre un conjunto tiene un cociente que es conjunto, una proyección sobreyectiva y una propiedad universal de descenso. Toda partición corresponde a una equivalencia, y cada función factoriza canónicamente a través del cociente por su equivalencia núcleo hacia una biyección con su imagen. Ninguna de estas construcciones requiere una **sección** $s:A/E\to A$ de la proyección: la afirmación de que toda proyección cociente posee una sección no se ha supuesto ni establecido. Los nombres nuevos se introducen por descripciones de grafos conjuntistas con guardas explícitas; no son nuevos primitivos de $\tau_\in$, ni se confunde $\mathsf{ZF}_{\mathrm{obj}}$ con $\mathsf M_{\mathrm{ext}}$.

Las pruebas son humanas y reconstruidas dentro del protocolo TLOG; ninguna se declara compilada o verificada en Lean. $\square$

## 15.20. Balance histórico del primer microtramo

`TLOG-CH15-M01` cierra matemáticamente la infraestructura de equivalencias, clases, cocientes y descenso funcional. Al terminar exclusivamente `CH15-M01`, el capítulo permanecía en `PARTIAL-CLOSURE`, pues exigía introducir **preórdenes, órdenes parciales y totales, órdenes estrictos, morfismos de órdenes y condiciones de buena definición** bajo guardas propias. Esas obligaciones quedan ahora resueltas en `TLOG-CH15-M02`, desarrollado en las secciones siguientes. La Parte III permanece abierta hasta completar el Capítulo 16. Se preservan cinco partes, veinticuatro capítulos y cero interfaces externas activadas. El material canónico permanece sólo en Markdown privado, sin declaración de publicación web.

**Continuación canónica:** `TLOG-CH15-M02 — Preórdenes, órdenes parciales y totales, buena definición y cierre del capítulo`, §§15.21–15.41.

## 15.21. Convenio de tipado para órdenes como conjuntos de pares

### Convención 15.21.1 — Orden no estricto, orden estricto y universo declarado {#tlog-cnv-00022}

Una relación de orden siempre es **un conjunto** $R\subseteq A\times A$ sobre un conjunto base $A$ declarado. Escribimos $x\preceq_R y$ para $\langle x,y\rangle\in R$; no existen nuevos predicados extralógicos en la signatura pura $\tau_{\in}$. Distinguiremos $\preceq_R$ (orden no estricto o preorden) de $\prec_S$ (orden estricto). Toda cuantificación que afirme reflexividad, transitividad, antisimetría o comparabilidad estará restringida a $A$. Si $A=\varnothing$, la única relación tipada es $R=\varnothing$, y las condiciones universales correspondientes son verdaderas vacuamente. Las fórmulas de pareja, producto y relación se expanden mediante las macros de los capítulos 13–14, con renombrado de variables ligadas.

## 15.22. Preórdenes

### Definición 15.22.1 — Reflexividad y transitividad relativas {#tlog-def-00089}

Para $R\subseteq A\times A$, definimos
$$
\operatorname{Preord}_A(R):\Longleftrightarrow
\Bigl[\forall a\in A\ (a\preceq_Ra)\Bigr]\land
\Bigl[\forall a,b,c\in A\ ((a\preceq_Rb\land b\preceq_Rc)\to a\preceq_Rc)\Bigr].
$$
La guarda $R\subseteq A\times A$ es parte constitutiva del predicado. El orden $R$ se obtiene como conjunto, no como una relación propia de la totalidad del universo. Un preorden no presupone antisimetría: dos elementos distintos pueden satisfacer simultáneamente $a\preceq_Rb$ y $b\preceq_Ra$. La cláusula se entiende como familia de abreviaciones de fórmulas de primer orden en $\in$ e igualdad lógica.

## 15.23. Indistinguibilidad inducida por un preorden

### Proposición 15.23.1 — La parte simétrica es una equivalencia {#tlog-pro-00073}

Si $\operatorname{Preord}_A(R)$, existe un único conjunto
$$
E_R:=\{\langle a,b\rangle\in A\times A:a\preceq_Rb\land b\preceq_Ra\},
$$
y $\operatorname{Equiv}_A(E_R)$. **Demostración.** El conjunto existe por separación sobre el producto del Capítulo 14; extensionalidad asegura unicidad. Reflexividad de $E_R$ se sigue de $a\preceq_Ra$. La conjunción es simétrica por conmutatividad lógica. Si $aE_Rb$ y $bE_Rc$, la transitividad del preorden da $a\preceq_Rc$ y, usando los dos pasos inversos, $c\preceq_Ra$. Por ello $aE_Rc$. Estos tres hechos y $E_R\subseteq A\times A$ prueban el predicado de equivalencia del §15.2. Para $A=\varnothing$, se obtiene $E_R=\varnothing$, que cumple las tres cláusulas vacuamente. $\square$

## 15.24. Órdenes parciales y lineales

### Definición 15.24.1 — Antisimetría, totalidad y orden parcial {#tlog-def-00090}

Sobre $A$, escribimos
$$
\begin{aligned}
\operatorname{Anti}_A(R)&:\Longleftrightarrow
 \forall a,b\in A\ ((a\preceq_Rb\land b\preceq_Ra)\to a=b),\\
\operatorname{Pos}_A(R)&:\Longleftrightarrow \operatorname{Preord}_A(R)\land\operatorname{Anti}_A(R),\\
\operatorname{Lin}_A(R)&:\Longleftrightarrow \operatorname{Pos}_A(R)\land
\forall a,b\in A\,(a\preceq_Rb\lor b\preceq_Ra).
\end{aligned}
$$
La última cláusula es **comparabilidad universal** y no se sigue de antisimetría. Se distingue explícitamente entre un conjunto parcialmente ordenado $(A,R)$ y una relación linealmente ordenada $(A,R)$. La notación $\le_R$ será equivalente a $\preceq_R$ sólo bajo la guarda de orden correspondiente. No afirmamos que una relación parcial cualquiera ordene linealmente su base.

## 15.25. El cociente de un preorden

### Metateorema 15.25.1 — Orden parcial canónico sobre clases simétricas {#tlog-mth-00063}

Sea $\operatorname{Preord}_A(R)$, $E=E_R$ y $Q=A/E$. Existe un único $\bar R\subseteq Q\times Q$ que satisface, para todos $a,b\in A$,
$$
\boxed{[a]_E\preceq_{\bar R}[b]_E\iff a\preceq_Rb,}
$$
y $\operatorname{Pos}_Q(\bar R)$. Si $R$ es total como preorden, $\bar R$ es lineal.

**Demostración.** Separamos en $Q\times Q$ los pares de clases $\langle C,D\rangle$ tales que existan $a\in C$, $b\in D$ con $a\preceq_Rb$. Para la **independencia de los representantes**, si $a'Ea$, $a\preceq_Rb$ y $bEb'$, entonces $a'\preceq_Ra$, $a\preceq_Rb$ y $b\preceq_Rb'$; dos aplicaciones de transitividad dan $a'\preceq_Rb'$. Así la existencia de testigos no depende de cuáles se utilicen. Cada clase contiene alguno de sus representantes por §15.5; el bicondicional mostrado vale para todo par de elementos del conjunto base sin escoger una sección de $\pi_E$.

Reflexividad de $\bar R$ resulta de $a\preceq_Ra$. Si $C\bar R D$ y $D\bar R F$, elegimos **solamente los testigos de esas dos afirmaciones particulares**; como ambos miembros intermedios representan la misma clase, son $E$-equivalentes. El argumento de independencia permite pasar de un testigo al otro y componer por transitividad. Para antisimetría, de $C\bar R D\land D\bar R C$ y representantes $a\in C,b\in D$ obtenemos simultáneamente $a\preceq_Rb$ y $b\preceq_Ra$; luego $aEb$ y $C=D$ por §15.6. Totalidad, si se exige, pasa al cociente al tomar representantes de dos clases dadas. La unicidad de $\bar R$ es extensionalidad de relaciones porque todo miembro de $Q$ es una clase. Si $A=\varnothing$, se obtiene la relación vacía sobre el cociente vacío. $\square$

## 15.26. Cuándo el cociente no identifica elementos

### Proposición 15.26.1 — Antisimetría y trivialidad de la parte simétrica {#tlog-pro-00074}

Para un preorden $(A,R)$ son equivalentes: (i) $R$ es antisimétrico; (ii) $E_R=\Delta_A$, donde $\Delta_A=\{\langle a,a\rangle:a\in A\}$; (iii) la proyección $\pi_{E_R}:A\to A/E_R$ es inyectiva. En cualquiera de los casos, la proyección es un **isomorfismo de órdenes** entre $(A,R)$ y su orden parcial cociente, entendiendo provisionalmente «isomorfismo» como biyección que preserva y refleja el orden (la formalización terminológica se da en §15.30).

**Demostración.** $aE_Rb$ equivale por §15.23 a $aRb\land bRa$, y antisimetría equivale a que ello fuerce $a=b$; como la diagonal ya pertenece a $E_R$, esto prueba (i)$\Leftrightarrow$(ii). Por §15.14, $\pi_E(a)=\pi_E(b)\iff aEb$; por tanto, (ii)$\Leftrightarrow$(iii). Bajo estas hipótesis, la proyección es biyectiva, y §15.25 garantiza tanto $aRb\Rightarrow\pi_E(a)\bar R\pi_E(b)$ como la implicación inversa. Los argumentos valen si $A$ es vacío. $\square$

## 15.27. Relaciones de orden estricto

### Definición 15.27.1 — Irreflexividad, transitividad y tricotomía {#tlog-def-00091}

Para $S\subseteq A\times A$ escribimos $a\prec_S b$ si $\langle a,b\rangle\in S$. Un **orden estricto parcial** satisface (a) $\forall a\in A\,\neg(a\prec_Sa)$ y (b) $\forall a,b,c\in A[(a\prec_Sb\land b\prec_Sc)\to a\prec_Sc]$. Será **estricto lineal** si, además, para cualesquiera $a\ne b$ de $A$, se cumple $a\prec_Sb\lor b\prec_Sa$. La primera pareja de condiciones implica asimetría: $aSb\land bSa$ llevaría por transitividad a $aSa$, contradicción. Tricotomía designará la disyunción exclusiva $a=b$, $aSb$ o $bSa$. Los cuantificadores y predicados se expanden en $\tau_{\in}$.

## 15.28. Equivalencia de órdenes estrictos y no estrictos

### Metateorema 15.28.1 — Las dos presentaciones de un orden parcial {#tlog-mth-00064}

Si $\operatorname{Pos}_A(R)$, la relación formada por separación
$$
S_R=\{\langle a,b\rangle\in A\times A:a\preceq_Rb\land a\ne b\}
$$
es un orden estricto parcial. Recíprocamente, si $S$ es estricto parcial, $R_S=S\cup\Delta_A$ es un orden parcial, y ambas transformaciones son inversas.

**Demostración.** La irreflexividad de $S_R$ es inmediata. Si $aS_Rb\land bS_Rc$, la transitividad de $R$ da $aRc$. Si $a=c$, las dos premisas dan $aRb$ y $bRa$, y la antisimetría forzaría $a=b$, contradiciendo $aS_Rb$; por tanto $a\ne c$ y $aS_Rc$. Recíprocamente, $R_S$ es reflexivo por la diagonal; la transitividad se prueba distinguiendo si alguno de los dos es una igualdad o si ambas parejas pertenecen a $S$, cuando se usa su transitividad. Si $aR_Sb\land bR_Sa$ y $a\ne b$, ambas relaciones serían estrictas, contradiciendo la asimetría deducida de irreflexividad y transitividad; luego $a=b$. Al sustraer la diagonal de $R_S$ se recupera exactamente $S$, porque $S$ no contiene pares diagonales. Al añadir la diagonal a $S_R$, se recupera $R$, por reflexividad y la partición de cada pareja de $R$ según $a=b$ o no. Las igualdades entre conjuntos se obtienen por extensionalidad. $\square$

## 15.29. Orden total y comparabilidad

### Proposición 15.29.1 — Totalidad equivale a tricotomía estricta {#tlog-pro-00075}

Un orden parcial $R$ sobre $A$ es total si y sólo si su orden estricto asociado $S_R$ satisface tricotomía. **Demostración.** Para $a\ne b$, totalidad de $R$ da $aRb\lor bRa$; la desigualdad transforma la dirección válida en una pareja de $S_R$. Ambas direcciones simultáneas son imposibles por antisimetría. Para $a=b$, sólo se cumple el caso de igualdad porque el orden estricto es irreflexivo. Recíprocamente, si $S_R$ tiene tricotomía, para cualesquiera $a,b\in A$ se cumple $a=b\lor aS_Rb\lor bS_Ra$, lo cual implica $aRb\lor bRa$ usando reflexividad. La prueba no exige que $A$ tenga miembros; el orden vacío es a la vez parcial y lineal. $\square$

## 15.30. Morfismos de órdenes

### Definición 15.30.1 — Monotonía, reflexión, embedding e isomorfismo {#tlog-def-00092}

Sean $R\subseteq A\times A$ y $S\subseteq B\times B$ órdenes parciales y $f:A\to B$. Diremos que $f$ **preserva el orden** (es monótona) si $aRb\to f(a)Sf(b)$, y que **refleja el orden** si $f(a)Sf(b)\to aRb$, para todos $a,b\in A$. Un **embedding de órdenes** preserva y refleja el orden; un **isomorfismo de órdenes** es un embedding biyectivo. Sobre preórdenes se permiten las mismas dos propiedades, pero preservar y reflejar **no garantiza inyectividad** sin antisimetría en el dominio. La afirmación $f:A\to B$ lleva un codominio declarado, en el sentido del Capítulo 14.

## 15.31. Composición y rigidez de morfismos

### Proposición 15.31.1 — Identidades, composición e inyectividad {#tlog-pro-00076}

La identidad de un conjunto ordenado es monótona y refleja el orden; la composición de aplicaciones monótonas es monótona, y la de embeddings vuelve a ser un embedding. Si el dominio está **parcialmente ordenado** y $f$ preserva y refleja el orden hacia un orden parcial, entonces es inyectiva. Toda biyección que preserve y refleje el orden posee inversa que también preserve y refleje el orden, de modo que define un isomorfismo.

**Demostración.** Para composiciones, si $aRb$, monotonía de $f$ da $f(a)Sf(b)$, y monotonía de $g$ da $g(f(a))Tg(f(b))$; las implicaciones inversas para reflexión se concatenan en orden inverso. Si $f(a)=f(b)$, la reflexividad en el codominio da tanto $f(a)Sf(b)$ como $f(b)Sf(a)$; reflexión da $aRb\land bRa$, y la antisimetría en el dominio concluye $a=b$. Para una biyección $f$, la inversa funcional ya existe por el Capítulo 14: dadas $u=f(a),v=f(b)$, $uSv$ equivale, por las dos implicaciones, a $aRb$; así la inversa preserva y refleja. Es importante que la simple combinación «inyectiva y monótona» **no** exija reflexión: una antichain de dos puntos se puede incluir inyectiva y monótonamente en una cadena de dos puntos, sin reflejar sus comparaciones adicionales. $\square$

## 15.32. Cadenas, extremos y cotas

### Definición 15.32.1 — Subconjunto cadena, mínimos, máximos, extremos {#tlog-def-00093}

Sea $(A,R)$ un conjunto parcialmente ordenado y $C\subseteq A$. Se llama **cadena** a $C$ si $\forall a,b\in C\,(aRb\lor bRa)$. Un $u\in A$ es **cota superior** de $C$ si $\forall c\in C\,(cRu)$, e inferior si $\forall c\in C\,(uRc)$. Un $m\in C$ es **mínimo** (elemento menor) si $\forall c\in C\,(mRc)$, y es **minimal** si no existe $c\in C$ con $cRm\land c\ne m$. Se definen simétricamente **máximo** y **maximal**. Todas estas nociones son predicados relativos a un conjunto $C$ y a un orden $R$, no selecciones de elementos. Si $C=\varnothing$, no tiene mínimo ni elemento minimal, pero **todo** elemento de $A$ es cota superior e inferior de $C$; si también $A=\varnothing$, no existe tal cota en $A$.

## 15.33. Unicidad de extremos y diferencia con minimalidad

### Proposición 15.33.1 — Extremos únicos; minimalidad en un orden lineal {#tlog-pro-00077}

Un mínimo (respectivamente un máximo) de $C$ es único, cuando existe, y es minimal (respectivamente maximal). En un orden **lineal** sobre $A$, todo elemento minimal de un subconjunto $C$ es su mínimo, y simétricamente para máximos. En un orden parcial general la recíproca puede fallar.

**Demostración.** Si $m,n$ son mínimos, $mRn$ por minimalidad de $m$ en el sentido de mínimo y $nRm$ por la de $n$; antisimetría da $m=n$. Si un mínimo $m$ admitiera $cRm$ con $c\ne m$, del mínimo se seguiría $mRc$, y antisimetría daría contradicción; así es minimal. En un orden lineal, para $c\in C$, comparabilidad proporciona $mRc\lor cRm$; si $m$ es minimal y $cRm$, forzosamente $c=m$, luego en todo caso $mRc$. Para ver que «minimal» no implica «mínimo» sin linealidad, tomamos dos conjuntos distintos $p,q$ y la relación diagonal sobre $\{p,q\}$. Ambos son minimales, ninguno es mínimo. Existencia de dos conjuntos distintos se sigue de $\varnothing\ne\{\varnothing\}$, probado con la infraestructura previa. $\square$

## 15.34. Buen orden como propiedad de subconjuntos

### Definición 15.34.1 — Orden bien fundado en el sentido de buen orden {#tlog-def-00094}

Se dice que $R$ es un **buen orden** sobre $A$ si $\operatorname{Pos}_A(R)$ y todo subconjunto no vacío $C\subseteq A$ tiene **mínimo** con respecto a $R$. Esta es una única fórmula objeto, con cuantificación sobre $C$ (conjunto variable) y condiciones $C\subseteq A$, $C\ne\varnothing$; no cuantifica sobre «todos los subconjuntos» como una clase propia, pues están contenidos en $\mathcal P(A)$. La definición **no** afirma que todo conjunto admita un buen orden: añadir esa existencia irrestricta sería equivalente a un principio de elección y no está disponible en ZF sin AC.

## 15.35. Consecuencias elementales del buen orden

### Proposición 15.35.1 — Todo buen orden es lineal y se hereda por restricción {#tlog-pro-00078}

Si $(A,R)$ está bien ordenado, entonces $R$ es lineal. Toda restricción $R\cap(C\times C)$ a $C\subseteq A$ es un buen orden de $C$; todo subconjunto no vacío tiene mínimo **único**. **Demostración.** Dados $a,b\in A$, el conjunto $\{a,b\}$ existe por pares y es no vacío. Su mínimo es $a$ o $b$, porque pertenece a ese par, y la propiedad de mínimo da respectivamente $aRb$ o $bRa$: hay comparabilidad. Para la restricción, sea $D\subseteq C$ no vacío. También $D\subseteq A$, así que posee mínimo $m\in D$ respecto de $R$, y las comparaciones pertinentes siguen siendo las de $R\cap(C\times C)$. Reflexividad, antisimetría y transitividad se heredan porque todos los cuantificadores se restringen a $C$. La unicidad sigue de antisimetría, como en §15.33. Si $C=\varnothing$, la definición es vacuamente satisfecha. No se ha elegido un mínimo simultáneamente para una familia de conjuntos: sólo se usa la propiedad definitoria por cada $D$. $\square$

## 15.36. Compatibilidad de una relación con una equivalencia

### Definición 15.36.1 — Saturación bilateral e independencia del representante {#tlog-def-00095}

Para $\operatorname{Equiv}_A(E)$ y $R\subseteq A\times A$, definimos la **saturación bilateral**
$$
\operatorname{Sat}_{E}(R):\Longleftrightarrow
\forall a,a',b,b'\in A\bigl[(aEa'\land bEb')\to
 (aRb\leftrightarrow a'Rb')\bigr].
$$
Se trata exactamente de la condición para que la verdad de $aRb$ dependa sólo de los dos bloques $[a]_E$, $[b]_E$. **No** debe confundirse con la sola afirmación de que $R$ sea transitiva o antisimétrica, ni con la condición de congruencia para una **operación** binaria del §15.39.

## 15.37. Descenso de relaciones a un cociente

### Metateorema 15.37.1 — Criterio necesario y suficiente de buena definición relacional {#tlog-mth-00065}

Sean $E$ equivalencia en $A$, $R\subseteq A\times A$ y $Q=A/E$. Son equivalentes:

1. $\operatorname{Sat}_{E}(R)$.
2. Existe **una única** relación $\bar R\subseteq Q\times Q$ tal que $aRb\iff[a]_E\,\bar R\,[b]_E$, para todo $a,b\in A$.

Cuando se satisfacen, la relación descendida es
$$
\boxed{\bar R=\{\langle C,D\rangle\in Q\times Q:
\exists a\in C\,\exists b\in D\ (aRb)\}.}
$$

**Demostración.** El producto $Q\times Q$ existe; la matriz indicada es una fórmula de la signatura pura al expandir los pares y las macros, así que separación proporciona $\bar R$. Si $aRb$, el par de sus clases está en $\bar R$, tomando esos testigos. En sentido contrario, supongamos $[a]_E\,\bar R\,[b]_E$. Hay $a'\in[a]_E,b'\in[b]_E$ con $a'Rb'$. El lema de coincidencia de clases (§15.6) da $aEa'$ y $bEb'$; saturación bilateral implica $aRb$. Esto prueba (1)$\Rightarrow$(2). La unicidad es extensionalidad: todos los miembros de $Q$ son clases, de modo que cualquier pareja de $Q\times Q$ tiene representantes. Recíprocamente, si una relación $\bar R$ cumple el bicondicional para cualquier par de elementos de $A$, entonces $aEa'\land bEb'$ da igualdad de clases, y con ella $aRb\iff a'Rb'$. No se selecciona ningún sistema global de representantes. El caso $A=\varnothing$ entrega las relaciones vacías únicas y la condición vacua. $\square$

## 15.38. Restricción del descenso para órdenes antisimétricos

### Proposición 15.38.1 — Una relación reflexiva saturada identifica sólo puntos mutuamente relacionados {#tlog-pro-00079}

Si $R$ es un preorden sobre $A$ y $E$ una equivalencia en $A$, entonces
$$
\boxed{\operatorname{Sat}_E(R)\iff E\subseteq E_R.}
$$
En particular, si $R$ es un **orden parcial**, la compatibilidad bilateral de $R$ con $E$ implica que $E=\Delta_A$. Por tanto, una relación de orden parcial sobre $A$ no puede descender mediante el bicondicional literal de §15.37 a un cociente no trivial.

**Demostración.** Supongamos saturación y $aEb$. Por reflexividad $aRa$. Aplicando saturación primero a la segunda coordenada $aEb$, obtenemos $aRb$; aplicándola a la primera, también $bRa$. Así $aE_Rb$, lo que da $E\subseteq E_R$. A la inversa, si $aEa'$ y $bEb'$ y $E\subseteq E_R$, se tienen $a'Ra$ y $bRb'$. De $aRb$ se deduce $a'Rb'$ por transitividad; en la dirección inversa se usan $aRa'$ y $b'Rb$. Esta es precisamente saturación. Si $R$ es antisimétrico, $E_R=\Delta_A$ por §15.26; junto con reflexividad de $E$, $E\subseteq\Delta_A$ fuerza $E=\Delta_A$. El resultado distingue el **cociente canónico de un preorden**, que siempre funciona, del intento injustificado de trasladar un orden parcial sobre clases arbitrarias. $\square$

## 15.39. Buena definición de operaciones sobre clases

### Proposición 15.39.1 — Descenso de una operación binaria bajo congruencia {#tlog-pro-00080}

Sea $E$ equivalencia sobre $A$ y $m:A\times A\to A$ una **operación binaria conjuntista**. Son equivalentes:

1. Para todos $aEa'$ y $bEb'$, $m(\langle a,b\rangle)\,E\,m(\langle a',b'\rangle)$.
2. Existe una única operación $\bar m:(A/E)\times(A/E)\to A/E$ que cumple
$$
\boxed{\bar m(\langle[a]_E,[b]_E\rangle)=[m(\langle a,b\rangle)]_E.}
$$

**Demostración.** Definamos $Q=A/E$. Por los Capítulos 13–14, $Q\times Q$, $(Q\times Q)\times Q$ y la relación de par ordenado existen como conjuntos. Separamos en el último producto los triples codificados $\langle\langle C,D\rangle,F\rangle$ para los que existan $a\in C,b\in D$ con $F=[m(\langle a,b\rangle)]_E$. Cada clase tiene un representante, y la operación es total sobre $A\times A$, de modo que el grafo separado tiene dominio $Q\times Q$. Si un mismo par $\langle C,D\rangle$ tiene dos presentaciones $\langle[a],[b]\rangle$ y $\langle[a'],[b']\rangle$, entonces $aEa'\land bEb'$; la hipótesis (1) fuerza igualdad de las clases de las imágenes. Por tanto el grafo es unívoco y define $\bar m$. Su unicidad proviene de que cada par de clases tiene alguna presentación y de la identidad requerida; no se eligen representantes simultáneamente. Recíprocamente, si existe $\bar m$ con la identidad y $aEa',bEb'$, las dos parejas de clases coinciden y sus valores son iguales; §15.6 implica que las imágenes originales son $E$-equivalentes. Si $A=\varnothing$, $A\times A=Q\times Q=\varnothing$; las dos operaciones son el grafo vacío y las dos condiciones valen. $\square$

## 15.40. Propiedad universal del cociente de un preorden

### Metateorema 15.40.1 — Monotonía y factorización hacia órdenes parciales {#tlog-mth-00066}

Sea $R$ un preorden de $A$ y $E_R$ su parte simétrica; $Q=A/E_R$ lleva el orden parcial $\bar R$ de §15.25. Para cualquier conjunto parcialmente ordenado $(B,S)$, la precomposición con la proyección $\pi:A\to Q$ induce una correspondencia biunívoca entre **funciones monótonas** $\bar f:(Q,\bar R)\to(B,S)$ y **funciones monótonas** $f:(A,R)\to(B,S)$. En concreto,
$$
\boxed{f=\bar f\circ\pi,\qquad \bar f([a]_{E_R})=f(a),}
$$
y $\bar f$ está determinada de manera única por $f$.

**Demostración.** Si $f$ es monótona y $aE_Rb$, entonces $aRb\land bRa$. Monotonía da $f(a)Sf(b)\land f(b)Sf(a)$; antisimetría de $S$ fuerza $f(a)=f(b)$. Por §15.15 existe una única función $\bar f:Q\to B$ con $f=\bar f\circ\pi$. Si $C\bar R D$, por definición hay $a\in C,b\in D$ con $aRb$; luego $\bar f(C)=f(a)$, $\bar f(D)=f(b)$ y $\bar f(C)S\bar f(D)$. Así $\bar f$ es monótona. En sentido contrario, si $\bar f$ es monótona, la proyección preserva $R$ por §15.25, por lo que $\bar f\circ\pi$ es monótona. La unicidad del descenso junto con la sobreyectividad de $\pi$ prueba que las dos transformaciones son inversas. La correspondencia se expresa entre subconjuntos de espacios funcionales existentes, sin suponer elección ni existencia de aplicaciones cuando el codominio es vacío y el dominio no lo es. $\square$

## 15.41. Cierre de las nociones conjuntistas de orden y cociente

### Corolario 15.41.1 — Infraestructura de equivalencias y órdenes sin elección {#tlog-cor-00019}

**Demostración (síntesis).** §§15.1–15.40 han construido equivalencias, clases, particiones y cocientes en conjuntos acotados; preórdenes, órdenes parciales, lineales y estrictos como relaciones conjuntistas; morfismos y restricciones; buen orden como propiedad de un orden dado; descenso de relaciones sólo bajo saturación bilateral y de operaciones sólo bajo congruencia; y el orden parcial canónico asociado a cualquier preorden. El paso a clases se logra por grafos de separación y universalidad, **sin** escoger un miembro de cada clase. No se sostiene la existencia de un buen orden para todo conjunto ni de secciones para sobreyecciones arbitrarias. Cada fórmula con macros conserva traducción eliminable al lenguaje de $\in$, los dos estratos $\mathsf{ZF}_{\mathrm{obj}}$ y $\mathsf M_{\mathrm{ext}}$ permanecen distintos, y ninguna prueba se reclama compilada o verificada en Lean. Por tanto el Capítulo 15 satisface su función arquitectónica prevista sin modificar el número de capítulos. $\square$

## 15.42. Estado del capítulo y siguiente frente

`TLOG-CH15-M02` cierra matemáticamente la teoría elemental de órdenes y la buena definición sobre cocientes, completando el `TLOG-CH15-0001` junto con los diecinueve resultados de `M01`. La Parte III permanece `OPEN` hasta completar el Capítulo 16 — Naturales, inducción, recursión y secuencias finitas. La signatura objeto continúa con $\in$ como único símbolo extralógico primitivo; toda operación nueva es macro o función construida como conjunto, no axioma adicional. No hay publicación web ni verificación Lean; las auditorías matemáticas y de persistencia se registran por separado.

**Próxima unidad:** `TLOG-CH16-M01 — Construcción de los naturales, propiedades elementales e inducción interna en ZF objeto`.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 14](capitulo-14.md) · [Capítulo 16 →](capitulo-16.md)


---
title: Capítulo 16 — Naturales, inducción, recursión y secuencias finitas
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
content-id: MA-BCH-0218
content-type: book-chapter
source-id: TLOG-CH16-0001
prerequisites:
- MA-BCH-0214
- MA-BCH-0215
- MA-BCH-0216
- MA-BCH-0217
related:
- MA-BOK-0014
source-sha256: 8db7cd63b383298a7e99e9fc32491d714259463e10efbdc711794c8e42c87a86
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 15](capitulo-15.md) · [Capítulo 17 →](capitulo-17.md)

## 16.0. Del axioma del infinito al objeto $\omega$

El Capítulo 12 estableció el axioma objeto del infinito ([TLOG-AXM-00009](capitulo-12.md#tlog-axm-00009)) **sin** introducir como primitivos el vacío ni el sucesor. Los capítulos 12–13 demostraron las operaciones de vacío, singleton y unión; el Capítulo 14 construyó funciones como grafos, y el Capítulo 15 controló órdenes y cocientes. Los §§16.1–16.62 construyen $\omega$ como **conjunto mínimo inductivo**, prueban inducción, recursión y leyes aritméticas, y completan el buen orden de $(\omega,\in)$, las secuencias finitas y sus operaciones. Cada paso conserva sus propias obligaciones de prueba; ninguno se infiere de la mera existencia de $\omega$.

**Estratos y pruebas.** Toda declaración de la forma «$\mathsf{ZF}_{\mathrm{obj}}$ demuestra» corresponde a una derivación finita, reconstruida con las reglas de primer orden de los capítulos 9–10, desde instancias expresas de los axiomas objeto del Capítulo 12. $\varnothing$, $S(a)$, $\operatorname{Ind}(I)$ y $\omega$ son abreviaciones eliminables de fórmulas de la **signatura pura** $\tau_\in$. La metateoría $\mathsf M_{\mathrm{ext}}=\mathsf{ZF}$ no incorpora AC. La prueba de inducción se formula como un **esquema para cada fórmula fija** $\theta$; no se cuantifica en el lenguaje objeto sobre fórmulas como si fueran objetos de una nueva sort.

**Procedencia:** reconstrucción interna desde los resultados [TLOG-PRO-00035](capitulo-12.md#tlog-pro-00035), [TLOG-AXM-00009](capitulo-12.md#tlog-axm-00009), [TLOG-AXM-00010](capitulo-12.md#tlog-axm-00010), [TLOG-PRO-00039](capitulo-13.md#tlog-pro-00039), [TLOG-MTH-00054](capitulo-13.md#tlog-mth-00054) y sus dependencias. Se conservan las identidades `TLOG-SRC-0002`, `TLOG-SRC-0003` y `TLOG-SRC-00011` en sus alcances registrados; no se declara nuevo cotejo de páginas ni importación de demostraciones.

## 16.1. Convenio fundacional para naturales

### Convención 16.1.1 — Construcción de von Neumann y tipado de las abreviaciones {#tlog-cnv-00023}

La letra $I$ denotará un **conjunto inductivo particular** y $J$ uno cualquiera. La grafía $0:=\varnothing$ emplea el único vacío demostrado en §12.26. La expresión $S(a)$ será una abreviación guardada por una **gráfica funcional total**, cuya existencia y unicidad se probarán antes de usarla. Los futuros nombres $\omega$, $n+1$ y $\mathbb N$ no amplían la firma objeto $\tau_\in$ de modo primitivo. Aquí $\mathbb N$ no se introduce como conjunto distinto de $\omega$.

La afirmación $X\subseteq Y$ se expande como $\forall u(u\in X\to u\in Y)$. Cada vez que se aplique separación o se aniden las gráficas del vacío y del sucesor, los vinculantes auxiliares serán renombrados por conversión alfa. Ningún conjunto de «todos los conjuntos inductivos» se presupone.

## 16.2. Gráfica de la operación sucesor

### Definición 16.2.1 — Fórmula pura de sucesor {#tlog-def-00096}

Para variables distintas $a,b$ definimos la **fórmula pura**
$$
\boxed{\operatorname{Succ}(b,a):\Longleftrightarrow
\forall u\,[u\in b\leftrightarrow(u\in a\lor u\doteq a)].}
$$
El término aparente $a\cup\{a\}$ no figura en la definición: es su representación editorial después de verificar que $b$ existe y es único. La variable $u$ se toma fresca en cada expansión; $\operatorname{Succ}$ no es un nuevo símbolo relacional objeto.

## 16.3. Existencia y unicidad del sucesor

### Proposición 16.3.1 — El sucesor existe para todo conjunto {#tlog-pro-00081}

En ZF objeto se demuestra el cierre universal de
$$
\boxed{\forall a\,\exists!b\,\operatorname{Succ}(b,a).}
$$
Al introducir la abreviación $S(a)=a\cup\{a\}$ quedan probadas $a\in S(a)$, $a\subseteq S(a)$ y $S(a)\ne\varnothing$.

**Demostración.** El axioma de pares produce el singleton $s=\{a\}$ como $\{a,a\}$. Otro par produce $p=\{a,s\}$; la unión del par da $b=\bigcup p$, y su cláusula de pertenencia es $u\in b\leftrightarrow(u\in a\lor u\in s)$. La caracterización de singleton convierte la segunda disyunción en $u\doteq a$. Si dos objetos $b,b'$ satisfacen la fórmula, tienen exactamente los mismos elementos, luego son iguales por extensionalidad. La instanciación $u=a$ proporciona $a\in S(a)$; la disyunción izquierda prueba $a\subseteq S(a)$. Como contiene $a$, $S(a)$ no es vacío. Todo el argumento usa un número **finito** de testigos, y no una función de elección. $\square$

## 16.4. Definición de conjunto inductivo

### Definición 16.4.1 — Guarda inductiva sin cuantificación sobre fórmulas {#tlog-def-00097}

Una fórmula $\operatorname{Ind}(I)$ afirma que $I$ contiene el vacío y es cerrado bajo sucesor. Su **expansión pura**, sin términos funcionales nuevos, es
$$
\boxed{\begin{aligned}
\operatorname{Ind}(I):\Longleftrightarrow{}&\exists e\,[(\forall u\,\neg(u\in e))\land e\in I]\\
&\land\forall a\,[a\in I\to\exists b\,(b\in I\land\operatorname{Succ}(b,a))].
\end{aligned}}
$$
Por la unicidad del vacío (§12.26) y de sucesor (§16.3), equivale a $0\in I\land\forall a\in I\;S(a)\in I$. La grafía acotada es sólo una lectura editorial de la fórmula original.

## 16.5. El axioma del infinito y la existencia de inductivos

### Proposición 16.5.1 — Recuperación exacta del axioma de infinito {#tlog-pro-00082}

Se demuestra $\mathsf{ZF}_{\mathrm{obj}}\vdash\exists I\,\operatorname{Ind}(I)$. Más precisamente, la **sentencia objeto** de infinito de §12.8 coincide, después de desarrollar $\operatorname{Succ}$ y la cláusula del vacío, con $\exists I\,\operatorname{Ind}(I)$.

**Demostración.** La matriz literal de §12.8 exige un $I$ con un elemento $e$ sin miembros y, para cada $a\in I$, un miembro $b\in I$ con $\forall u(u\in b\leftrightarrow(u\in a\lor u\doteq a))$. Esta segunda matriz es exactamente $\operatorname{Succ}(b,a)$ de §16.2. La primera es la cláusula del vacío de §16.4. No se añade una hipótesis nueva ni se modifica la interpretación del infinito. $\square$

## 16.6. Candidato mínimo dentro de un testigo inductivo

### Definición 16.6.1 — Intersección definible de inductivos acotados {#tlog-def-00098}

Fijado un conjunto $I$ que satisface $\operatorname{Ind}(I)$, consideramos la fórmula
$$
\boxed{\Omega(W,I):\Longleftrightarrow
\forall x\,[x\in W\leftrightarrow
(x\in I\land\forall J\,((J\subseteq I\land\operatorname{Ind}(J))\to x\in J))].}
$$
Se cuantifica $J$ **entre objetos del universo de ZF**, no sobre una clase postulada como conjunto. La instancia de separación usa únicamente $I$ como ambiente y la matriz de la derecha como condición. Denotaremos el único conjunto producido por $W_I$ después de probar su existencia.

## 16.7. El candidato es inductivo

### Proposición 16.7.1 — Existencia de $W_I$ y clausura por sucesor {#tlog-pro-00083}

Si $\operatorname{Ind}(I)$, existe un único $W_I\subseteq I$ que satisface $\Omega(W_I,I)$, y además $\operatorname{Ind}(W_I)$.

**Demostración.** Aplicamos separación a $I$ con la matriz $\forall J\,((J\subseteq I\land\operatorname{Ind}(J))\to x\in J)$, cuya sustitución literal es segura tras renombrar auxiliares. Se obtiene $W_I$ con la equivalencia de §16.6, y su unicidad es extensional. Como todo inductivo $J$ contiene $0$, y $I$ también lo contiene, $0$ satisface la condición, luego $0\in W_I$. Si $a\in W_I$, entonces $a\in I$ y, por $\operatorname{Ind}(I)$, $S(a)\in I$. Para cada $J\subseteq I$ inductivo, la definición de $W_I$ da $a\in J$; su clausura da $S(a)\in J$. Por tanto $S(a)$ satisface la misma matriz y pertenece a $W_I$. Se ha demostrado $\operatorname{Ind}(W_I)$. $\square$

## 16.8. Minimalidad sin formar una clase de inductivos

### Lema 16.8.1 — $W_I$ está contenido en todo conjunto inductivo {#tlog-lem-00043}

Para $\operatorname{Ind}(I)$ y cualquier $J$,
$$
\boxed{\operatorname{Ind}(J)\ \Longrightarrow\ W_I\subseteq J.}
$$

**Demostración.** Dado un conjunto inductivo $J$, la intersección $K=I\cap J$ existe por separación (§13.13). Tanto $I$ como $J$ contienen el vacío, así que $0\in K$. Si $a\in K$, la clausura de ambos inductivos asegura $S(a)\in K$. De aquí $\operatorname{Ind}(K)$ y $K\subseteq I$. Por definición de $W_I$, todos sus miembros están en todo inductivo contenido en $I$, en particular en $K$; luego $W_I\subseteq K\subseteq J$. El argumento **no** supone que exista un conjunto de *todos* los inductivos. $\square$

## 16.9. Independencia del testigo de infinito

### Metateorema 16.9.1 — Existencia y unicidad del menor inductivo {#tlog-mth-00067}

ZF objeto demuestra, al expandir todas las macros,
$$
\boxed{\exists!W\,[\operatorname{Ind}(W)\land
\forall J(\operatorname{Ind}(J)\to W\subseteq J)].}
$$

**Demostración.** Por §16.5 existe un testigo inductivo $I$. Las §§16.7–16.8 producen un $W_I$ inductivo que está contenido en todo inductivo. Si $I'$ es otro testigo, también $W_{I'}$ es inductivo y mínimo. La minimalidad de ambos produce $W_I\subseteq W_{I'}$ y $W_{I'}\subseteq W_I$, de donde $W_I=W_{I'}$ por extensionalidad. Igualmente, cualesquiera conjuntos $W,W'$ que satisfagan la propiedad enmarcada se contienen mutuamente. La prueba **descarga** el testigo original $I$: el objeto final no depende de una elección de un inductivo privilegiado. $\square$

## 16.10. El nombre $\omega$ como abreviación conservativa

### Definición 16.10.1 — Gráfica única de los naturales de von Neumann {#tlog-def-00099}

Por el teorema anterior autorizamos $\omega$ como el único conjunto $W$ que satisface
$$
\boxed{\operatorname{Ind}(W)\land
\forall J(\operatorname{Ind}(J)\to W\subseteq J).}
$$
No se agrega una constante primitiva $\omega$ a $\tau_\in$. Toda aparición se elimina mediante sustitución de su **gráfica única**, con renombrados alfa, del mismo modo que las extensiones conservativas del Capítulo 13. Los símbolos $0$ y $S$ conservan sus definiciones previas; el conjunto $\omega$ así construido es el conjunto de naturales de von Neumann **dentro de ZF objeto**. Esto no es una identificación de $\omega$ objeto con la colección $\omega$ de la metateoría externa.

## 16.11. Ecuaciones de clausura y minimalidad de $\omega$

### Proposición 16.11.1 — El menor inductivo contiene cero y todos sus sucesores {#tlog-pro-00084}

Se deducen las cláusulas
$$
\boxed{0\in\omega,\qquad
\forall n\in\omega\;S(n)\in\omega,\qquad
\forall I\,(\operatorname{Ind}(I)\to\omega\subseteq I).}
$$
Además $\omega\ne\varnothing$ y ningún inductivo es vacío.

**Demostración.** Las dos primeras cláusulas son las de $\operatorname{Ind}(\omega)$ obtenidas en §§16.7–16.10; la tercera es la minimalidad §16.8, ya independizada del testigo. Si $0\in\omega$, este conjunto tiene al menos un elemento. Y si $I$ es inductivo, $0\in I$ excluye que sea vacío. No hay inducción circular: todas estas cláusulas se demostraron desde **infinito más separación** antes de formular el principio de inducción. $\square$

## 16.12. Esquema de inducción interna

### Metateorema 16.12.1 — Inducción para cada fórmula del lenguaje de pertenencia {#tlog-mth-00068}

Sea $\theta(n,\bar p)$ **una fórmula fija** de la firma pura, con las variables auxiliares elegidas frescas. ZF objeto demuestra su instancia de inducción, con clausura universal de los parámetros:
$$
\boxed{\begin{aligned}
\forall\bar p\;\bigl[&\theta(0,\bar p)\land
\forall n\in\omega(\theta(n,\bar p)\to\theta(S(n),\bar p))\\
&\longrightarrow\forall n\in\omega\;\theta(n,\bar p)\bigr].
\end{aligned}}
$$
De forma equivalente: todo $P\subseteq\omega$ que contiene $0$ y satisface $n\in P\Rightarrow S(n)\in P$ para $n\in\omega$ es $P=\omega$.

**Demostración.** Fijemos $\bar p$ y supongamos las dos hipótesis del antecedente. Por una **instancia específica** del esquema de separación construimos $P=\{n\in\omega:\theta(n,\bar p)\}$. La hipótesis inicial da $0\in P$. Si $n\in P$, entonces $n\in\omega$ y $\theta(n,\bar p)$; por la segunda hipótesis $\theta(S(n),\bar p)$, y por clausura de $\omega$, $S(n)\in\omega$; luego $S(n)\in P$. Así $P$ es inductivo. La minimalidad de $\omega$ (§16.11) da $\omega\subseteq P$; como $P\subseteq\omega$ por construcción, ambos coinciden. Por ello todo $n\in\omega$ satisface $\theta(n,\bar p)$. Se descargan las hipótesis y luego se universalizan los parámetros. La prueba es **esquemática**: para cada $\theta$ se registra una derivación finita; no se introduce un cuantificador objeto sobre códigos de fórmulas. $\square$

## 16.13. Cero no es sucesor e inyectividad de $S$

### Proposición 16.13.1 — Separación entre cero y sucesores, y cancelación {#tlog-pro-00085}

Para **todos** los conjuntos $a,b$, no sólo los naturales, ZF objeto demuestra
$$
\boxed{S(a)\ne0,\qquad S(a)=S(b)\ \longrightarrow\ a=b.}
$$

**Demostración.** $a\in S(a)$ por §16.3, mientras que $0$ carece de miembros; así $S(a)\ne0$. Supongamos $S(a)=S(b)$ y $a\ne b$. Dado que $a\in S(a)=S(b)=b\cup\{b\}$, la fórmula de sucesor y $a\ne b$ implican $a\in b$. Simétricamente, $b\in a$. El conjunto $\{a,b\}$ es no vacío por el axioma de pares; la regularidad aplicada a él aporta un miembro $z\in\{a,b\}$ sin elementos comunes con $\{a,b\}$. Pero si $z=a$, entonces $b\in a\cap\{a,b\}$; si $z=b$, $a\in b\cap\{a,b\}$. Ambos casos contradicen la regularidad. Así $a=b$. La inyectividad **sí utiliza fundamentación**; la existencia del sucesor no la utiliza. $\square$

## 16.14. Predecesor de todo natural no nulo

### Proposición 16.14.1 — Cero o sucesor de un único natural {#tlog-pro-00086}

Para cada $n\in\omega$ se demuestra
$$
\boxed{n=0\quad\lor\quad\exists!m\in\omega\;(n=S(m)).}
$$
La disyunción es exclusiva y $n\ne0$ implica el segundo miembro.

**Demostración.** Sea $\theta(n)$ la fórmula $n=0\lor\exists m\,(m\in\omega\land n=S(m))$, entendida con expansión de las descripciones únicas. La base $\theta(0)$ es inmediata. Supongamos $n\in\omega$ y $\theta(n)$. Independientemente de cuál de sus disyuntos sea verdadero, $S(n)$ tiene el testigo $m=n\in\omega$ para el segundo disyunto; por tanto vale $\theta(S(n))$. Por inducción (§16.12), todo natural satisface $\theta$. Si $n=S(m)=S(m')$, la inyectividad de §16.13 da $m=m'$. Asimismo, $0$ no es sucesor de ningún conjunto, por §16.13, y los disyuntos no pueden darse simultáneamente. $\square$

## 16.15. Cero pertenece a todo natural no nulo

### Proposición 16.15.1 — El primer elemento aparece en cada sucesor {#tlog-pro-00087}

Para $n\in\omega$:
$$
\boxed{n\ne0\quad\Longrightarrow\quad 0\in n.}
$$

**Demostración.** Inducimos sobre $n$ la fórmula $n=0\lor0\in n$. En $n=0$ vale el primer disyunto. Si $n=0$, entonces $0\in S(n)$ porque $n\in S(n)$. Si $0\in n$, entonces $0\in S(n)$ por $n\subseteq S(n)$. En ambos casos vale la fórmula para el sucesor, y §16.12 concluye que todo natural satisface la disyunción. Si $n\ne0$, sólo queda $0\in n$. La prueba no requiere que se haya demostrado todavía que $\in$ es lineal sobre $\omega$. $\square$

## 16.16. Los naturales como conjuntos transitivos

### Proposición 16.16.1 — Cada natural es transitivo {#tlog-pro-00088}

Un conjunto $n$ es **transitivo** si $\forall x\in n\,(x\subseteq n)$. En ZF objeto,
$$
\boxed{\forall n\in\omega\;\forall x\in n\;(x\subseteq n).}
$$

**Demostración.** La propiedad es vacuamente cierta para $n=0$. Supongamos que $n$ es transitivo y sea $x\in S(n)=n\cup\{n\}$. Si $x=n$, entonces $x\subseteq S(n)$ por §16.3. Si $x\in n$, la hipótesis inductiva da $x\subseteq n\subseteq S(n)$. Por tanto $S(n)$ es transitivo. La instancia de inducción de §16.12 prueba la propiedad para todo $n\in\omega$. En ningún paso se supone que **todo conjunto inductivo** sea transitivo, afirmación que sería falsa. $\square$

## 16.17. Transitividad del propio $\omega$

### Proposición 16.17.1 — Todo miembro de un natural es natural {#tlog-pro-00089}

Se demuestra la transitividad de $\omega$:
$$
\boxed{\forall n\in\omega\; n\subseteq\omega.}
$$
En particular, $m\in n\in\omega\Rightarrow m\in\omega$.

**Demostración.** Separación forma el conjunto $P=\{n\in\omega:n\subseteq\omega\}$. Cero pertenece a $P$, porque el vacío es subconjunto de todo conjunto. Supongamos $n\in P$; entonces $n\subseteq\omega$ y $n\in\omega$. Por clausura inductiva, $S(n)\in\omega$; además $S(n)=n\cup\{n\}\subseteq\omega$ ya que los elementos de $n$ están en $\omega$ y también $n\in\omega$. De aquí $S(n)\in P$. Aplicando inducción (§16.12), $P=\omega$, y por definición de $P$, todos los $n\in\omega$ son subconjuntos de $\omega$. Esta demostración usa la clausura de $\omega$ y no presupone orden total de pertenencia. $\square$

## 16.18. Estructura de Peano y límites del bloque

### Metateorema 16.18.1 — Estructura interna con cero, sucesor e inducción {#tlog-mth-00069}

Las siguientes afirmaciones tienen demostraciones en ZF objeto, con las abreviaciones traducidas a $\tau_\in$:
$$
\boxed{\begin{gathered}
0\in\omega,\qquad S:\omega\to\omega,\qquad
\forall n\in\omega\;S(n)\ne0,\\
\forall n,m\in\omega\ (S(n)=S(m)\to n=m),\\
\text{Inducción para cada fórmula }\theta(n,\bar p)
\text{ en el lenguaje puro de pertenencia.}
\end{gathered}}
$$

**Demostración.** Existencia y cierre de $\omega$ son §16.11. La fórmula total $\operatorname{Succ}$ de §16.3 determina un **único** valor $S(n)\in\omega$ para cada $n\in\omega$, y por reemplazo, o separando dentro de $\omega\times\omega$, existe su grafo restringido al dominio $\omega$. Distinguimos la operación sucesor, que es una macro con una gráfica única, de este conjunto-grafo $S\upharpoonright\omega$, cuya existencia se justifica ahora. La separación de cero y la inyectividad son §16.13; el esquema de inducción, §16.12. Esto produce el fragmento estructural de Peano necesario para la futura aritmetización, **sin** haber construido todavía las operaciones aritméticas $+$ y $\cdot$, la recursión primitiva ni las secuencias finitas. No afirmamos todavía los axiomas de Peano como una teoría formal de firma aritmética cuyo sistema deductivo haya sido definido aquí; sólo sus traducciones demostrables en ZF objeto. $\square$

## 16.19. Balance del microtramo y obligaciones posteriores

### Corolario 16.19.1 — Núcleo natural construido sin elección {#tlog-cor-00020}

**Demostración (síntesis).** Los §§16.1–16.18 prueban dentro de ZF objeto la existencia y unicidad del menor conjunto inductivo, la disponibilidad conservativa de $0,S,\omega$, la inducción para fórmulas con parámetros y las ecuaciones fundamentales del sucesor. La regularidad se usa **explícitamente** en la inyectividad general del sucesor. No se emplean elección ni BPI; la construcción no introduce cuantificadores objeto sobre predicados, ni un conjunto de todos los inductivos, ni intercambia ZF objeto con la metateoría externa. La prueba es humana, pendiente de cualquier formalización Lean. $\square$

**Estado:** `TLOG-CH16-M01 = CLOSED / MATHEMATICAL QA`; `TLOG-CH16-0001 = PARTIAL-CLOSURE / NOT CLOSED`. La Parte III permanece abierta. Para cerrar el Capítulo 16 faltan el teorema de recursión sobre $\omega$, operaciones aritméticas derivadas, carácter de buen orden de $\in$ en los naturales y secuencias finitas con sus codificaciones y operaciones básicas.

**Próximo microtramo:** `TLOG-CH16-M02 — Recursión sobre ω y construcción de operaciones aritméticas`.

## 16.20. Recursión interna: nivel objeto y requisitos de tipado

### Convención 16.20.1 — Recursión con valores en un conjunto fijado {#tlog-cnv-00024}

Fijaremos un **conjunto** de valores $B$, un dato inicial $b\in B$ y un **grafo conjuntista** $H:\omega\times B\to B$. Las flechas son las aplicaciones del Capítulo 14, no operaciones primitivas del lenguaje $\tau_\in$. Se busca una única aplicación $f:\omega\to B$ que satisfaga
$$
 f(0)=b,\qquad f(S(n))=H(\langle n,f(n)\rangle)\quad(n\in\omega).
$$
La segunda ecuación puede imprimirse $H(n,f(n))$ una vez declarada su interpretación por pares ordenados. El ámbito de $f$ no se asume existente antes de la prueba. Toda instancia con matrices paramétricas se expande a fórmulas puras de pertenencia y se universaliza después de descargar las hipótesis. Esta es **recursión con codominio conjunto**, no recursión sobre una clase propia ni recursión por elección de testigos arbitrarios.

## 16.21. Aproximaciones de recursión con dominio $S(n)$

### Definición 16.21.1 — Gráfica de aproximación admisible {#tlog-def-00100}

Con $b\in B$ y $H:\omega\times B\to B$ fijados, para $n\in\omega$ llamaremos **buena aproximación hasta $n$** a un conjunto $g$ que cumpla
$$
\boxed{\begin{aligned}
 \operatorname{Good}(g,n;b,H,B):\Longleftrightarrow{}&g:S(n)\to B,\quad g(0)=b,\\
 &\forall j\in\omega\;[S(j)\in S(n)\to g(S(j))=H(j,g(j))].
\end{aligned}}
$$
La última ecuación es legítima: si $S(j)\in S(n)$, la transitividad de $S(n)$ y $j\in S(j)$ implican $j\in S(n)$, de modo que $g(j)$ está definido. La tipificación de los grafos permite expresar todo con cuantificadores y pertenencia; por ejemplo, el propio $g$ está acotado por $\omega\times B$. No se postula aquí que exista alguna aproximación: ello se probará por inducción.

## 16.22. Propiedades de los dominios recursivos

### Lema 16.22.1 — Segmentos sucesores, cero y antecesores {#tlog-lem-00044}

Para todo $n\in\omega$ se tiene
$$
\boxed{0\in S(n)\subseteq\omega,\qquad S(n)\notin S(n),\qquad
 (S(j)\in S(n)\Rightarrow j\in S(n)).}
$$

**Demostración.** Si $n=0$, entonces $S(n)=\{0\}$ y contiene cero. Si $n\ne0$, §16.15 proporciona $0\in n\subseteq S(n)$. Por §16.11 $S(n)\in\omega$ y, al ser $\omega$ transitivo (§16.17), $S(n)\subseteq\omega$. §16.16 establece que todo natural, incluido $S(n)$, es transitivo; como $j\in S(j)$, de $S(j)\in S(n)$ se obtiene $j\in S(n)$. Finalmente, la regularidad de ZF implica $x\notin x$ para todo conjunto $x$ (aplíquese fundamentación al singleton $\{x\}$); en particular $S(n)\notin S(n)$. No se emplea linealidad ni buen orden de la pertenencia. $\square$

## 16.23. Extensión por un paso

### Lema 16.23.1 — Prolongación canónica de una aproximación {#tlog-lem-00045}

Si $\operatorname{Good}(g,n;b,H,B)$, existe una buena aproximación $g^+$ de dominio $S(S(n))$ tal que $g\subseteq g^+$; está dada por
$$
\boxed{g^+=g\cup\{\langle S(n),H(n,g(n))\rangle\}.}
$$

**Demostración.** $n\in S(n)=\operatorname{dom}(g)$, luego $g(n)$ está definido y pertenece a $B$. Dado que $n\in\omega$, el valor $H(n,g(n))$ existe y está en $B$. Por §16.22, $S(n)\notin S(n)$, de modo que la unión de grafos añade exactamente una entrada nueva, sin colisión funcional. Su dominio es $S(n)\cup\{S(n)\}=S(S(n))$. Conserva $g(0)=b$, pues la nueva entrada no es cero. Para una ecuación sucesora con $S(j)\in S(S(n))$, hay dos casos. Si $S(j)\in S(n)$, la ecuación ya vale en $g$ y las evaluaciones de $g^+$ coinciden en el dominio antiguo. En caso contrario, $S(j)=S(n)$; por inyectividad del sucesor (§16.13), $j=n$, y la nueva entrada fue elegida como $H(n,g(n))$. Se verifican todas las cláusulas de `Good`. Se utilizan únicamente conjuntos de pares y su unión, no un principio de elección. $\square$

## 16.24. Aproximaciones de toda longitud natural

### Proposición 16.24.1 — Existencia mediante inducción sin recursión previa {#tlog-pro-00090}

Bajo $b\in B$ y $H:\omega\times B\to B$,
$$
\boxed{\forall n\in\omega\;\exists g\;\operatorname{Good}(g,n;b,H,B).}
$$

**Demostración.** Para $n=0$, el grafo singleton $g_0=\{\langle0,b\rangle\}$ tiene dominio $S(0)=\{0\}$; es una función a $B$, satisface $g_0(0)=b$, y la ecuación sucesora es vacua porque ningún sucesor es cero (§16.13). Si existe una buena aproximación hasta $n$, §16.23 construye una buena aproximación hasta $S(n)$. La fórmula $\exists g\,\operatorname{Good}(g,n;b,H,B)$ admite las instancias de separación del esquema de inducción §16.12; la inducción concluye para todo $n\in\omega$. Sólo se elige **un testigo local** al ejecutar el paso inductivo, sin selección simultánea de una familia de aproximaciones. $\square$

## 16.25. Compatibilidad de aproximaciones de longitudes distintas

### Lema 16.25.1 — Unicidad de valores en dominios solapados {#tlog-lem-00046}

Si $g,h$ son buenas aproximaciones (hasta sendos $n,m\in\omega$), entonces
$$
\boxed{\forall k\in\operatorname{dom}(g)\cap\operatorname{dom}(h)\quad g(k)=h(k).}
$$
En particular, $g\cup h$ es un conjunto funcional, aunque los dominios no se hayan comparado por un supuesto orden lineal de $\in$.

**Demostración.** Apliquemos inducción §16.12 a la fórmula en $k\in\omega$ que afirma «si $k$ pertenece a ambos dominios, los dos valores coinciden», manteniendo como parámetros los grafos $g,h$. Para $k=0$, ambos lo contienen por §16.22 y ambos valores son $b$. Supuesta la afirmación para $k$, si $S(k)$ no está en ambos dominios, la implicación del paso inductivo es trivial. Si está en los dos, la transitividad de sendos segmentos (§16.22) y $k\in S(k)$ muestran que también $k$ está en ambos dominios; la hipótesis da $g(k)=h(k)$. Las dos cláusulas `Good` producen entonces
$$
g(S(k))=H(k,g(k))=H(k,h(k))=h(S(k)).
$$
La inducción cubre todos los $k\in\omega$. Como los dominios son subconjuntos de $\omega$, queda probada la compatibilidad. La unión de dos grafos funcionales compatibles es funcional por la definición de función del Capítulo 14. $\square$

## 16.26. Teorema de recursión sobre $\omega$

### Metateorema 16.26.1 — Existencia y unicidad de la función recursiva {#tlog-mth-00070}

Para cualesquiera conjuntos $B,b,H$ que satisfagan $b\in B$ y $H:\omega\times B\to B$, ZF objeto demuestra
$$
\boxed{\exists! f:\omega\to B\;\left[f(0)=b\ \land\ \forall n\in\omega\;f(S(n))=H(n,f(n))\right].}
$$
Aquí $\exists!f:\omega\to B$ abrevia «existe un único conjunto $f$ que es grafo de una función $\omega\to B$ y cumple…»; no es un cuantificador funcional primitivo.

**Demostración — existencia.** El producto $\omega\times B$ existe por §14.7 y su potencia $P=\mathcal P(\omega\times B)$ por §13.10. Mediante separación formamos el conjunto
$$
\mathscr G=\{g\in P:\exists n\in\omega\;\operatorname{Good}(g,n;b,H,B)\}.
$$
La fórmula definitoria es pura después de desarrollar las macros, y la cuantificación sobre $g$ está acotada por $P$; no hay clase propia de «todas las funciones parciales». Definimos $f=\bigcup\mathscr G$, unión conjuntista de los miembros de $\mathscr G$. Por §16.25 sus elementos son grafos compatibles dos a dos, luego $f$ es un grafo funcional de recorrido incluido en $B$. Todo elemento de $f$ es un par con primer componente en $\omega$; por consiguiente $\operatorname{dom}(f)\subseteq\omega$. Recíprocamente, para cualquier $k\in\omega$, §16.24 suministra una buena aproximación $g$ en $S(k)$; como $k\in S(k)$, el par de valor $\langle k,g(k)\rangle$ pertenece a $f$. Así $\operatorname{dom}(f)=\omega$. Toda buena aproximación contiene $0$ y le asigna $b$, por lo que $f(0)=b$. Para fijar $n\in\omega$, tomamos una buena aproximación sobre $S(S(n))$, que existe por §16.24 puesto que $S(n)\in\omega$; ambos $n,S(n)$ están en su dominio. Su cláusula sucesora y la compatibilidad con $f$ implican $f(S(n))=H(n,f(n))$.

**Demostración — unicidad.** Si $u,v:\omega\to B$ satisfacen ambas ecuaciones, inducimos en $n$ la fórmula $u(n)=v(n)$. La base usa el dato común $b$; el paso usa la funcionalidad de $H$. La inducción vale para todos los naturales; igualdad extensional de grafos implica $u=v$. No se ha usado buen orden de $\omega$, recursión previa ni elección. La construcción se mantiene en $\mathsf{ZF}_{\mathrm{obj}}$; el discurso metateórico sólo parametriza la familia de instancias definicionales. $\square$

## 16.27. Recursión uniforme con parámetros

### Proposición 16.27.1 — Gráfico simultáneo de una familia recursiva {#tlog-pro-00091}

Sean $P,B$ conjuntos, $a:P\to B$ y $H:(P\times\omega)\times B\to B$ (lectura abreviada $H(p,n,z)$). Existe una única función $F:P\times\omega\to B$ con
$$
\boxed{F(p,0)=a(p),\quad F(p,S(n))=H(p,n,F(p,n))\qquad(p\in P,n\in\omega).}
$$
La afirmación incluye $P=\varnothing$ (donde $F=\varnothing$ aun si $B=\varnothing$).

**Demostración.** Para cada $p\in P$, formamos por separación dentro de $(\omega\times B)\times B$ el grafo
$$
H_p=\{\langle\langle n,z\rangle,w\rangle:\langle\langle\langle p,n\rangle,z\rangle,w\rangle\in H\}.
$$
La codificación se interpreta como la del producto $((P\times\omega)\times B)\times B$; por la hipótesis, $H_p:\omega\times B\to B$. Además $a(p)\in B$. El metateorema §16.26 entrega para cada $p$ un **único** $f_p:\omega\to B$ con las cláusulas requeridas. No se selecciona una familia arbitraria $(f_p)$: definimos directamente $F$ por separación dentro de $(P\times\omega)\times B$, admitiendo $\langle\langle p,n\rangle,z\rangle$ exactamente si existe algún grafo $f\subseteq\omega\times B$ que satisface la recursión para $p$ y contiene $\langle n,z\rangle$. La existencia y unicidad de tal $f_p$ aseguran que este predicado determina exactamente un $z$ para cada $(p,n)$. Sus dos ecuaciones se leen en la correspondiente fibra $p$. Si $P$ es vacío, el producto ambiente y el grafo son vacíos; no se necesita escoger ningún $p$. La unicidad de $F$ se deduce de la unicidad de cada fibra, o de inducción con $p$ fijado. Las operaciones de conjuntos y las instancias de separación contienen sólo un número finito de parámetros declarados. $\square$

## 16.28. Construcción de la suma

### Definición 16.28.1 — Función de suma mediante recursión con parámetro {#tlog-def-00101}

Aplicamos §16.27 con $P=B=\omega$, dato inicial $a(p)=p$ (grafo identidad ya construido) y paso $H(p,n,z)=S(z)$ (función con codominio $\omega$, §16.18). La única $F:\omega\times\omega\to\omega$ se denota $+$ y su valor $F(a,b)$ se escribe $a+b$. Conservo las ecuaciones definitorias
$$
\boxed{a+0=a,\qquad a+S(b)=S(a+b).}
$$
La notación es una macro respaldada por existencia y unicidad del grafo; no se ha añadido el símbolo $+$ a la signatura primitiva $\tau_\in$.

## 16.29. Totalidad de la suma e identidades inmediatas

### Proposición 16.29.1 — Suma total y ecuaciones de recursión {#tlog-pro-00092}

Existe una única aplicación $+:\omega\times\omega\to\omega$ que verifica, para $a,b\in\omega$,
$$
\boxed{a+0=a,\qquad a+S(b)=S(a+b),\qquad a+1=S(a),\quad 1:=S(0).}
$$

**Demostración.** Existencia y unicidad de $+$ son §16.28 y la unicidad de §16.27. La cláusula $a+0=a$ y la sucesora son la propia especificación recursiva. Con $b=0$, $a+1=a+S(0)=S(a+0)=S(a)$. La imagen pertenece a $\omega$ porque todas las fibras fueron construidas con codominio $\omega$. La igualdad de aplicaciones se lee como igualdad de grafos en el producto existente $\omega\times\omega$. $\square$

## 16.30. Reglas en la primera variable

### Lema 16.30.1 — Identidad izquierda y sucesor izquierdo {#tlog-lem-00047}

Para todos $a,b\in\omega$,
$$
\boxed{0+b=b,\qquad S(a)+b=S(a+b).}
$$

**Demostración.** Por inducción en $b$, $0+0=0$; si $0+b=b$, entonces $0+S(b)=S(0+b)=S(b)$. Para la segunda igualdad, fijemos $a$. En $b=0$, $S(a)+0=S(a)=S(a+0)$. Si vale para $b$, aplicamos la ecuación sucesora y la hipótesis:
$$
S(a)+S(b)=S(S(a)+b)=S(S(a+b))=S(a+S(b)).
$$
La inducción establece la fórmula universal. Las sustituciones de $a,b$ son seguras porque se trabaja con las expansiones puras de las gráficas de $S$ y $+$; las variables auxiliares son frescas. $\square$

## 16.31. Asociatividad y conmutatividad de la suma

### Metateorema 16.31.1 — El monoide conmutativo aditivo de $\omega$ {#tlog-mth-00071}

La teoría objeto demuestra, para $a,b,c\in\omega$,
$$
\boxed{(a+b)+c=a+(b+c),\qquad a+b=b+a,\qquad a+0=0+a=a.}
$$

**Demostración.** La identidad bilateral de $0$ se obtiene por §16.29 y §16.30. Para asociatividad fijemos $a,b$ e induzcamos en $c$. En cero ambos miembros valen $a+b$. En el paso:
$$
\begin{aligned}
 (a+b)+S(c)&=S((a+b)+c)\\
 &=S(a+(b+c))=a+S(b+c)=a+(b+S(c)).
\end{aligned}
$$
Para conmutatividad, fijemos $a$ e induzcamos en $b$. En $b=0$, $a+0=a=0+a$. Bajo $a+b=b+a$,
$$
a+S(b)=S(a+b)=S(b+a)=S(b)+a,
$$
usando la regla de sucesor izquierdo de §16.30. Los dos principios inductivos son instancias del §16.12 para fórmulas con parámetros; no requieren una aritmética supuesta de antemano. $\square$

## 16.32. Cancelación aditiva

### Proposición 16.32.1 — Cancelación en ambos argumentos {#tlog-pro-00093}

Para $a,b,c\in\omega$,
$$
\boxed{a+c=b+c\Longrightarrow a=b,\qquad c+a=c+b\Longrightarrow a=b.}
$$

**Demostración.** Fijados $a,b$, una inducción en $c$ prueba la primera implicación. Para $c=0$ las ecuaciones de cero dan la conclusión. Si $a+S(c)=b+S(c)$, las ecuaciones sucesoras dan $S(a+c)=S(b+c)$; la inyectividad del sucesor de §16.13 da $a+c=b+c$ y se aplica la hipótesis inductiva. La segunda implicación resulta al permutar argumentos mediante conmutatividad de §16.31. No se deduce aún ninguna desigualdad ordenada de esta cancelación. $\square$

## 16.33. Construcción de la multiplicación

### Definición 16.33.1 — Producto por suma iterada {#tlog-def-00102}

Aplicando recursión con parámetro §16.27 a $P=B=\omega$, al dato inicial constante $a(p)=0$ y al paso $H(p,n,z)=z+p$ (grafo existente por la suma), se obtiene una función $\cdot:\omega\times\omega\to\omega$ caracterizada unívocamente por
$$
\boxed{a\cdot0=0,\qquad a\cdot S(b)=a\cdot b+a.}
$$
El grafo constante $p\mapsto0$ existe por separación dentro de $\omega\times\omega$. El paso se forma como subconjunto funcional del producto cartesiano apropiado mediante sustitución en el grafo $+$, sin postular una nueva operación. La multiplicación así definida pertenece a la teoría objeto como abreviación conservativa.

## 16.34. Identidades elementales del producto

### Proposición 16.34.1 — Ceros y unidades multiplicativas {#tlog-pro-00094}

Sean $a,b\in\omega$ y $1=S(0)$. Entonces
$$
\boxed{a\cdot0=0,\quad a\cdot S(b)=a\cdot b+a,\quad
 a\cdot1=a,\quad0\cdot a=0,\quad1\cdot a=a.}
$$

**Demostración.** Las dos primeras igualdades son las ecuaciones de la recursión §16.33. En particular, $a\cdot1=a\cdot S(0)=a\cdot0+a=0+a=a$, usando el cero izquierdo de la suma. Para $0\cdot a=0$, inducimos en $a$: en cero es inmediato y $0\cdot S(a)=0\cdot a+0=0$. Para $1\cdot a=a$, en cero vale $1\cdot0=0$; si $1\cdot a=a$, entonces $1\cdot S(a)=1\cdot a+1=a+1=S(a)$ (§16.29). Así ambas identidades son universales. No hemos supuesto conmutatividad del producto ni ninguna de sus distribuciones. $\square$

## 16.35. Distributividad en el primer factor

### Lema 16.35.1 — $(a+b)\cdot c=a\cdot c+b\cdot c$ {#tlog-lem-00048}

Para $a,b,c\in\omega$ se verifica
$$
\boxed{(a+b)\cdot c=(a\cdot c)+(b\cdot c).}
$$

**Demostración.** Fijemos $a,b$ e induzcamos en $c$. Si $c=0$, ambos miembros son cero por §16.34 y $0+0=0$. Para el paso:
$$
\begin{aligned}
(a+b)\cdot S(c)&=(a+b)\cdot c+(a+b)\\
&=(a\cdot c+b\cdot c)+(a+b)\\
&=(a\cdot c+a)+(b\cdot c+b)\\
&=a\cdot S(c)+b\cdot S(c).
\end{aligned}
$$
La tercera igualdad es un reagrupamiento autorizado por asociatividad y conmutatividad **ya demostradas** de la suma (§16.31). Así se cierra el paso por inducción §16.12. Esta fórmula se denomina distributividad del producto respecto de una suma en el *primer* factor, sin intercambiar los factores multiplicativos. $\square$

## 16.36. Distributividad en el segundo factor

### Proposición 16.36.1 — $a\cdot(b+c)=a\cdot b+a\cdot c$ {#tlog-pro-00095}

Para $a,b,c\in\omega$ se verifica
$$
\boxed{a\cdot(b+c)=a\cdot b+a\cdot c.}
$$

**Demostración.** Fijemos $a,b$ e induzcamos en $c$. En $c=0$, $b+0=b$ y ambos miembros se reducen a $a\cdot b$. Si la identidad vale para $c$, entonces
$$
\begin{aligned}
 a\cdot(b+S(c))&=a\cdot S(b+c)\\
 &=a\cdot(b+c)+a\\
 &=(a\cdot b+a\cdot c)+a\\
 &=a\cdot b+(a\cdot c+a)\\
 &=a\cdot b+a\cdot S(c).
\end{aligned}
$$
Se han usado exclusivamente la ecuación recursiva de la multiplicación y la asociatividad de la suma. No hay dependencia de la conmutatividad de la multiplicación ni de la distributividad del apartado anterior, evitando un ciclo entre pruebas. $\square$

## 16.37. Conmutatividad y asociatividad multiplicativas

### Metateorema 16.37.1 — Leyes fundamentales de la multiplicación de naturales {#tlog-mth-00072}

Para cualesquiera $a,b,c\in\omega$,
$$
\boxed{a\cdot b=b\cdot a,\qquad(a\cdot b)\cdot c=a\cdot(b\cdot c).}
$$

**Demostración — conmutatividad.** Por §16.35 y §16.34 tenemos
$$
S(b)\cdot a=(b+1)\cdot a=b\cdot a+1\cdot a=b\cdot a+a.
$$
Fijemos $a$ e induzcamos en $b$ la igualdad $a\cdot b=b\cdot a$. La base es $a\cdot0=0=0\cdot a$. En el paso,
$$
a\cdot S(b)=a\cdot b+a=b\cdot a+a=S(b)\cdot a,
$$
que completa la inducción.

**Demostración — asociatividad.** Fijemos $a,b$ e induzcamos en $c$. En $c=0$, ambos lados son cero. Si la igualdad vale para $c$, aplicamos las ecuaciones recursivas y la distributividad §16.36:
$$
\begin{aligned}
 (a\cdot b)\cdot S(c)&=(a\cdot b)\cdot c+a\cdot b\\
 &=a\cdot(b\cdot c)+a\cdot b\\
 &=a\cdot((b\cdot c)+b)\\
 &=a\cdot(b\cdot S(c)).
\end{aligned}
$$
Cada paso depende de resultados previos; el producto es asociativo y conmutativo sin asumir dichas leyes como definiciones. La inducción es una instancia del §16.12 y no presupone el buen orden de $\omega$. $\square$

## 16.38. Síntesis: semianillo natural y límite del microtramo

### Corolario 16.38.1 — Estructura aritmética interna sin elección {#tlog-cor-00021}

Las construcciones de §§16.20–16.37 acreditan **en la teoría objeto** la existencia como conjuntos de $+$ y $\cdot$, su carácter funcional total en $\omega\times\omega$, las identidades de cero y uno, las leyes conmutativas y asociativas, ambas distributividades y la cancelación aditiva. Junto con §16.13 y §16.12, se dispone del núcleo de las leyes usuales de un semianillo conmutativo $(\omega,+,\cdot,0,1)$ y de la inducción para fórmulas de pertenencia traducidas conservativamente.

**Demostración (síntesis).** La existencia/unicidad de la recursión procede de aproximaciones acotadas por $\mathcal P(\omega\times B)$ y de su unión compatible, no de un recurso a elegir una aproximación por cada índice. Las leyes de $+$ y $\cdot$ se derivan mediante inducción interna y sus recursiones respectivas. El término *semianillo* sintetiza las ecuaciones probadas, no se incorpora como nueva teoría objeto ni añade símbolos a $\tau_\in$. No se prueba aún que $\in$ bien ordene $\omega$, ni se construyen secuencias finitas generales ni codificación efectiva de expresiones. La teoría formal de Peano y las funciones computables quedan también fuera del presente microtramo. Cero resultados Lean compilados/verificados; ninguna interfaz intertratados activada. $\square$

**Estado de `CH16-M02`:** cierre matemático local para recursión sobre $\omega$, suma y multiplicación. Capítulo 16 y Parte III continúan abiertos, con obligaciones de buen orden y secuencias finitas reservadas a `CH16-M03`. Las demostraciones humanas no se equiparan a certificados Lean ni a publicaciones web.

## 16.39. Lema de sucesión interna de los naturales

### Lema 16.39.1 — Todo elemento de un natural tiene sucesor interno o terminal {#tlog-lem-00049}

Para $m,n\in\omega$ se demuestra
$$
\boxed{m\in n\ \Longrightarrow\ S(m)\in n\ \lor\ S(m)=n.}
$$
No se presupone la comparación lineal de cualesquiera dos naturales.

**Demostración.** Por inducción §16.12 sobre $n$. Si $n=0$, el antecedente es falso. Supongamos la afirmación para $n$ y consideremos $m\in S(n)=n\cup\{n\}$. Si $m=n$, entonces $S(m)=S(n)$. Si $m\in n$, la hipótesis inductiva ofrece $S(m)\in n$ o $S(m)=n$; en ambos casos $S(m)\in S(n)$, pues $n\subseteq S(n)$ y $n\in S(n)$. Esto cierra el paso; las instancias de inducción son fórmulas de pertenencia con los símbolos definidos expandidos. $\square$

## 16.40. Tricotomía de los ordinales finitos

### Metateorema 16.40.1 — Comparabilidad estricta de naturales {#tlog-mth-00073}

Para $m,n\in\omega$, exactamente una de las afirmaciones
$$
\boxed{m\in n,\qquad m=n,\qquad n\in m}
$$
es verdadera.

**Demostración.** Primero probamos por inducción en $n$ que *al menos una* se cumple para todo $m\in\omega$. Para $n=0$, si $m=0$ vale la igualdad y, si $m\ne0$, §16.15 proporciona $0\in m$. Supongamos la tricotomía débil para $n$ y sea $m$ arbitrario. Si $m\in n$ o $m=n$, entonces $m\in S(n)$. En el caso restante, $n\in m$; por §16.39, $S(n)=m$ o $S(n)\in m$. Así la comparación existe para $S(n)$. Para la **exclusividad**, fundamentación excluye $x\in x$ y $x\in y\land y\in x$: en el último caso el par no vacío $\{x,y\}$ no tendría elemento mínimo. Por transitividad de cada natural (§16.16), $m\in n\land n\in m$ implicaría además $m\in m$. Las tres alternativas son disjuntas. $\square$

## 16.41. La pertenencia como orden estricto

### Proposición 16.41.1 — Irreflexividad, transitividad y totalidad {#tlog-pro-00096}

La relación $<_{\omega}:=\{\langle m,n\rangle\in\omega\times\omega:m\in n\}$ es un conjunto y constituye un **orden estricto lineal** en $\omega$: es irreflexiva, transitiva y compara todos los elementos distintos.

**Demostración.** Su existencia se obtiene por separación sobre $\omega\times\omega$. La irreflexividad es consecuencia de fundamentación. Si $a\in b\in c$ con $c\in\omega$, la transitividad del conjunto $c$ (§16.16) proporciona $a\in c$. La comparación entre dos naturales distintos es §16.40. Estas propiedades son precisamente las condiciones de orden estricto lineal fijadas en el Capítulo 15; la definición no añade relaciones primitivas a $\tau_\in$. $\square$

## 16.42. Buen orden de $\omega$

### Metateorema 16.42.1 — Mínimo de todo subconjunto no vacío {#tlog-mth-00074}

Para cada conjunto $X\subseteq\omega$ no vacío existe un único $m\in X$ tal que
$$
\boxed{\forall n\in X\ (m=n\lor m\in n).}
$$
En consecuencia $(\omega,<_{\omega})$ es un buen orden; no se afirma que *todos* los conjuntos puedan bien ordenarse.

**Demostración.** Por fundamentación aplicada al **conjunto** $X\ne\varnothing$ existe $m\in X$ con $m\cap X=\varnothing$. Para cualquier $n\in X$ distinto de $m$, la tricotomía da $n\in m$ o $m\in n$. La primera alternativa contradice $m\cap X=\varnothing$, así que $m\in n$. Si también $m'\in X$ fuese mínimo, la comparación estricta entre $m,m'$ descartaría que fuesen distintos. Se ha usado el axioma de fundamentación sólo para $X$, nunca un principio de elección de mínimos para una familia arbitraria. $\square$

## 16.43. Forma del mínimo contraejemplo

### Corolario 16.43.1 — Inducción y principio del mínimo contraejemplo {#tlog-cor-00022}

Para cualquier fórmula fija $\varphi(n,\bar p)$, si el conjunto de contraejemplos $\{n\in\omega:\neg\varphi(n,\bar p)\}$ es no vacío, tiene un mínimo; en particular, no puede existir un contraejemplo si $\varphi(0,\bar p)$ y $\forall n\in\omega[\varphi(n,\bar p)\to\varphi(S(n),\bar p)]$.

**Demostración.** Separación produce el conjunto de contraejemplos, con variables ligadas frescas. Si no es vacío, §16.42 da un menor elemento $m$. La base excluye $m=0$, por lo que §16.14 da $m=S(k)$ con $k\in\omega$. Como $k\in m$, la minimalidad obliga a $\varphi(k,\bar p)$; el paso inductivo implica $\varphi(m,\bar p)$, contradicción. La equivalencia es esquema por fórmula, no cuantificación objeto sobre predicados. $\square$

## 16.44. Orden no estricto en naturales

### Definición 16.44.1 — Relación $\leq$ y su expansión conjuntista {#tlog-def-00103}

Definimos para $m,n\in\omega$
$$
\boxed{m\leq n:\Longleftrightarrow\ (m\in n\lor m=n).}
$$
La relación $\leq$ se construye por separación dentro de $\omega\times\omega$ y no se incorpora como predicado primitivo de la firma de pertenencia.

## 16.45. Orden y contención entre ordinales finitos

### Proposición 16.45.1 — Equivalencia entre $m\leq n$ y $m\subseteq n$ {#tlog-pro-00097}

Para $m,n\in\omega$,
$$
\boxed{m\leq n\iff m\subseteq n.}
$$
Además $n<S(n)$, $m<n\Rightarrow S(m)\leq n$ y $0\leq n$ para todo $n\in\omega$.

**Demostración.** Si $m=n$ hay contención trivial, y si $m\in n$, la transitividad de $n$ da $m\subseteq n$. Recíprocamente, supongamos $m\subseteq n$ y que $m\not\leq n$. Tricotomía §16.40 fuerza $n\in m$; por contención se seguiría $n\in n$, contradiciendo irreflexividad. Por §16.3 $n\in S(n)$. Si $m\in n$, el lema §16.39 da $S(m)\in n$ o $S(m)=n$. Finalmente $0=\varnothing\subseteq n$ y se aplica la equivalencia. $\square$

## 16.46. Traslaciones aditivas y partición de segmentos

### Lema 16.46.1 — Desplazamiento de un segmento finito {#tlog-lem-00050}

Fijado $n\in\omega$, la aplicación $k\mapsto n+k$ es inyectiva, $n\leq n+k$ y, para todo $m\in\omega$,
$$
\boxed{n+m=n\ \dot\cup\ \{n+k:k\in m\}.}
$$
El símbolo $\dot\cup$ significa unión de conjuntos disjuntos; la imagen de $m$ existe por reemplazo.

**Demostración.** La inyectividad es cancelación en el primer sumando (§16.32). Por inducción en $k$, $n\leq n+0=n$; y $n\leq n+k<S(n+k)=n+S(k)$ implica $n\leq n+S(k)$ por transitividad del orden de §16.41. Por ello ningún $n+k$ pertenece al conjunto $n$, pues $n\leq n+k$ es incompatible con $n+k<n$. Para la identidad de conjuntos, inducimos en $m$. En cero la imagen es vacía y $n+0=n$. Si vale para $m$, las ecuaciones recursivas dan $n+S(m)=S(n+m)=(n+m)\cup\{n+m\}$. Como $S(m)=m\cup\{m\}$, la nueva imagen es la anterior unida a $\{n+m\}$, lo que demuestra el paso y conserva la disjunción. No se utiliza el principio de elección para formar ninguna de estas imágenes funcionales. $\square$

## 16.47. Secuencias de longitud natural

### Definición 16.47.1 — Secuencia finita y longitud {#tlog-def-00104}

Sea $A$ un conjunto cualquiera, incluso $A=\varnothing$. Una **secuencia finita sobre $A$** es una función-grafo $s:n\to A$ con $n\in\omega$; el natural $n=\operatorname{dom}(s)$ es su longitud $|s|$. Aquí $n$ es el ordinal de von Neumann $\{0,\dots,n-1\}$, y $s$ es literalmente un conjunto de pares de Kuratowski. Reservamos
$$
A^{<\omega}:=\{s:\exists n\in\omega\ (s:n\to A)\}.
$$
Esta escritura denota un conjunto sólo tras la demostración del apartado siguiente; no se confunde con el uso metateórico previo $\Sigma^{<\omega}$ para palabras formales.

## 16.48. Existencia y tipado de $A^{<\omega}$

### Proposición 16.48.1 — Conjunto de todas las secuencias finitas {#tlog-pro-00098}

Para todo conjunto $A$ existe el conjunto
$$
\boxed{A^{<\omega}=\{s\in\mathcal P(\omega\times A):\operatorname{Fun}(s)\land\operatorname{dom}(s)\in\omega\}.}
$$
Siempre $\varnothing\in A^{<\omega}$, y si $A=\varnothing$ entonces $A^{<\omega}=\{\varnothing\}$.

**Demostración.** Los capítulos 13–14 construyen $\omega\times A$ y su conjunto potencia. La condición de separación es una fórmula fija con parámetros $\omega,A$ que afirma que el grafo es funcional, que cada par tiene segunda coordenada en $A$ y que el dominio es un elemento de $\omega$. Como $s\subseteq\omega\times A$, se cumple esta condición de codominio automáticamente; la unicidad de longitud es la unicidad de $\operatorname{dom}(s)$. El grafo vacío es la única función $0\to A$, y pertenece al conjunto incluso si $A$ es vacío. Para $A=\varnothing$, $\omega\times A=\varnothing$, cuya potencia contiene sólo el grafo vacío. No se requiere elegir valores de $A$. $\square$

## 16.49. Restricciones iniciales y longitud única

### Lema 16.49.1 — Existencia y composición de restricciones {#tlog-lem-00051}

Si $s:n\to A$ y $k\leq n$, el grafo
$$
\boxed{s\upharpoonright k=s\cap(k\times A)}
$$
es una secuencia de longitud $k$. Si $j\leq k\leq n$, entonces $(s\upharpoonright k)\upharpoonright j=s\upharpoonright j$; asimismo $s\upharpoonright n=s$ y $s\upharpoonright0=\varnothing$. Si $s:n\to A$ y $s:m\to A$, necesariamente $n=m$.

**Demostración.** $k\leq n$ equivale a $k\subseteq n$ (§16.45). Para cada $i\in k$ la función $s:n\to A$ tiene exactamente un valor $s(i)\in A$, cuyo par está en la intersección; no hay otros argumentos. Por tanto la restricción es función de dominio $k$. La identidad de restricciones sucesivas procede de $(s\cap(k\times A))\cap(j\times A)=s\cap(j\times A)$ cuando $j\subseteq k$. Los casos $0,n$ son inmediatos; la longitud se determina por el dominio intrínseco de un grafo. $\square$

## 16.50. Secuencia vacía y adjunción de una entrada

### Definición 16.50.1 — Extensión por un valor final {#tlog-def-00105}

Escribimos $\epsilon_A:=\varnothing$ para la secuencia vacía sobre $A$. Si $s:n\to A$ y $a\in A$, la adjunción al final es el grafo
$$
\boxed{s\mathbin{\frown}\langle a\rangle:=s\cup\{\langle n,a\rangle\}.}
$$
La notación $\langle a\rangle$ aquí es una secuencia de longitud uno; no se identifica con el par de Kuratowski $\langle n,a\rangle$ empleado en su grafo. Toda la construcción tiene dominio de definición expresamente guardado por $a\in A$.

## 16.51. Adjunción y descomposición de secuencias

### Proposición 16.51.1 — Toda secuencia no vacía tiene último término único {#tlog-pro-00099}

Si $s:n\to A$ y $a\in A$, entonces $s\frown\langle a\rangle:S(n)\to A$. Recíprocamente, si $t\in A^{<\omega}$ y $|t|\ne0$, existen únicos $s\in A^{<\omega}$ y $a\in A$ con $t=s\frown\langle a\rangle$.

**Demostración.** Los argumentos originales son los elementos de $n$; el nuevo argumento es $n$. Por regularidad, $n\notin n$, y por ello el grafo añadido no colisiona con el previo; el dominio resulta $n\cup\{n\}=S(n)$. Para el converso, §16.14 da $|t|=S(n)$ para un único $n$. La restricción $s=t\upharpoonright n$ existe por §16.49; como $n\in S(n)$, $t(n)$ existe y es único, y pertenece a $A$. La funcionalidad de $t$ da $t=s\cup\{\langle n,t(n)\rangle\}$. Todo posible factor final tiene dominio $n$ por inyectividad de sucesor y por §16.49; por ello $s$ y $a$ quedan determinados. Incluso cuando $A=\varnothing$, el enunciado universal se cumple vacuamente para secuencias no vacías. $\square$

## 16.52. Inducción estructural sobre secuencias finitas

### Metateorema 16.52.1 — Principio de inducción por adjunción {#tlog-mth-00075}

Para cualquier fórmula fija $\Phi(s,\bar p)$, si $\Phi(\epsilon_A,\bar p)$ y, para todo $s\in A^{<\omega}$ y $a\in A$, se cumple $\Phi(s,\bar p)\Rightarrow\Phi(s\frown\langle a\rangle,\bar p)$, entonces $\forall s\in A^{<\omega}\,\Phi(s,\bar p)$.

**Demostración.** Por separación definimos $P=\{n\in\omega:\forall s\in A^{<\omega}(|s|=n\to\Phi(s,\bar p))\}$. La única secuencia de dominio $0$ es $\epsilon_A$, luego $0\in P$. Si $n\in P$ y $t$ tiene longitud $S(n)$, §16.51 proporciona $t=s\frown\langle a\rangle$ con $|s|=n$ y $a\in A$. Por $n\in P$ y la hipótesis de adjunción se obtiene $\Phi(t,\bar p)$; por tanto $S(n)\in P$. Inducción en $\omega$ (§16.12) concluye $P=\omega$. Así toda secuencia finita satisface $\Phi$, también si el alfabeto es vacío. El resultado es un **esquema** de inducción para fórmulas, no una cuantificación objeto sobre propiedades arbitrarias. $\square$

## 16.53. Construcción conjuntista de concatenación

### Definición 16.53.1 — Unión del prefijo y la cola desplazada {#tlog-def-00106}

Para secuencias $s:n\to A$ y $t:m\to A$, definimos
$$
\boxed{s\mathbin{\frown}t:=s\cup\{\langle n+k,t(k)\rangle:k\in m\}.}
$$
La cola desplazada existe por reemplazo aplicado a la función de $k\in m$ que devuelve el par $\langle n+k,t(k)\rangle$; cada suma es una descripción funcional ya justificada. Se usa el mismo símbolo $\frown$ de §16.50, cuya compatibilidad con la adjunción queda demostrada más adelante.

## 16.54. Tipo y longitud de concatenación

### Proposición 16.54.1 — Concatenación de secuencias finitas {#tlog-pro-00100}

Si $s:n\to A$ y $t:m\to A$, entonces $s\frown t:(n+m)\to A$ y
$$
\boxed{|s\frown t|=|s|+|t|.}
$$

**Demostración.** El dominio del primer grafo es $n$; el de la cola desplazada es $\{n+k:k\in m\}$ por tipado de pares. §16.46 muestra que ambos son disjuntos y que su unión es exactamente $n+m$. La inyectividad de $k\mapsto n+k$ asegura que la cola desplazada es funcional. No puede haber colisiones entre ambas partes por la disjunción de dominios. Todos los valores proceden de $s$ o $t$, luego pertenecen a $A$. El grafo unido es función de dominio $n+m$, y la longitud coincide por definición §16.47. $\square$

## 16.55. Ecuaciones características de concatenación

### Lema 16.55.1 — Vacío derecho y compatibilidad con adjunción {#tlog-lem-00052}

Para $s,t\in A^{<\omega}$ y $a\in A$,
$$
\boxed{s\frown\epsilon_A=s,\qquad s\frown(t\frown\langle a\rangle)=(s\frown t)\frown\langle a\rangle.}
$$

**Demostración.** La primera fórmula se obtiene de §16.53 porque la cola vacía tiene dominio $0$ y su imagen es vacía. Para la segunda, pongamos $|s|=n$, $|t|=m$. La expresión $t\frown\langle a\rangle$ coincide, por §16.50, con $t\cup\{\langle m,a\rangle\}$. Al desplazar sus argumentos por $n$, se obtiene la cola de $t$ desplazada y el único par nuevo $\langle n+m,a\rangle$. La definición de concatenación y $n+S(m)=S(n+m)$ prueban que ambos miembros son el mismo conjunto de pares. La adjunción a la derecha tiene por dominio $S(n+m)$, tal como exige §16.51. $\square$

## 16.56. Leyes de unidad y asociatividad

### Metateorema 16.56.1 — El monoide de secuencias finitas {#tlog-mth-00076}

Para cada conjunto $A$, la concatenación define una función total $A^{<\omega}\times A^{<\omega}\to A^{<\omega}$ y
$$
\boxed{\epsilon_A\frown s=s=s\frown\epsilon_A,\qquad(s\frown t)\frown u=s\frown(t\frown u).}
$$
Por tanto $(A^{<\omega},\frown,\epsilon_A)$ es un monoide, incluso para $A=\varnothing$.

**Demostración.** §16.54 asegura que cada par de secuencias determina una única secuencia. Por separación en el producto de conjuntos, el grafo de esta operación es un conjunto funcional total. La identidad derecha es §16.55. Para la izquierda, inducción estructural §16.52 sobre $s$: en la secuencia vacía ambos lados son el grafo vacío; si vale $\epsilon_A\frown s=s$, entonces $\epsilon_A\frown(s\frown\langle a\rangle)=(\epsilon_A\frown s)\frown\langle a\rangle=s\frown\langle a\rangle$ por §16.55. Para la asociatividad, fijemos $s,t$ e induzcamos estructuralmente sobre $u$. En $u=\epsilon_A$ ambos lados son $s\frown t$. Para $u'=u\frown\langle a\rangle$, el lema §16.55 y la hipótesis inductiva dan
$$
(s\frown t)\frown u'=((s\frown t)\frown u)\frown\langle a\rangle=(s\frown(t\frown u))\frown\langle a\rangle=s\frown(t\frown u').
$$
No se ha usado ni elección ni un teorema de codificación de palabras. $\square$

## 16.57. Orden por prefijos

### Proposición 16.57.1 — Restricción inicial como orden parcial {#tlog-pro-00101}

Definimos $s\preccurlyeq_{\mathrm{pref}}t$ si $|s|\leq|t|$ y $s=t\upharpoonright |s|$. Es una relación conjuntista de orden parcial sobre $A^{<\omega}$: reflexiva, antisimétrica y transitiva. La secuencia vacía es su mínimo.

**Demostración.** La relación se forma mediante separación dentro de $A^{<\omega}\times A^{<\omega}$. La reflexividad resulta de $s=s\upharpoonright|s|$. Si $s$ es prefijo de $t$ y viceversa, sus longitudes son iguales por antisimetría de $\leq$ en $\omega$; las restricciones completas dan $s=t$. Si $r\preccurlyeq_{\mathrm{pref}}s\preccurlyeq_{\mathrm{pref}}t$, la transitividad de $\leq$ y la ley de restricciones anidadas (§16.49) dan $r=t\upharpoonright|r|$. Finalmente, todo grafo restringido al dominio $0$ es vacío. $\square$

## 16.58. Cancelación por prefijo fijado

### Lema 16.58.1 — Inyectividad de la concatenación derecha con prefijo fijo {#tlog-lem-00053}

Para $s,t,u\in A^{<\omega}$,
$$
\boxed{s\frown t=s\frown u\ \Longrightarrow\ t=u.}
$$

**Demostración.** Escribamos $|s|=n$, $|t|=m$, $|u|=p$. De la igualdad de grafos y §16.54 se deduce $n+m=n+p$; la cancelación aditiva §16.32 da $m=p$. Para cada $k\in m$, el argumento $n+k$ no pertenece a $n$ (§16.46), de modo que su valor en ambos grafos concatenados sólo puede venir de la cola desplazada. La inyectividad de $k\mapsto n+k$ impone $t(k)=u(k)$. Como tienen el mismo dominio, la extensionalidad de las funciones implica $t=u$. También aquí se admiten las secuencias vacías. $\square$

## 16.59. Aplicación coordenada a coordenada

### Lema 16.59.1 — Transformación de secuencias mediante una función {#tlog-lem-00054}

Si $f:A\to B$ es una función declarada, existe una única función $f^{<\omega}:A^{<\omega}\to B^{<\omega}$ tal que $f^{<\omega}(s)=f\circ s$ para cada $s:n\to A$. Preserva longitudes, vacío y concatenación:
$$
\boxed{|f^{<\omega}(s)|=|s|,\quad f^{<\omega}(\epsilon_A)=\epsilon_B,\quad f^{<\omega}(s\frown t)=f^{<\omega}(s)\frown f^{<\omega}(t).}
$$

**Demostración.** La composición de §14.34 construye, para cada $s:n\to A$, el grafo funcional $f\circ s:n\to B$, único. El conjunto de tales grafos se obtiene por reemplazo sobre $A^{<\omega}$ o, equivalentemente, por separación en $A^{<\omega}\times B^{<\omega}$ con una fórmula de composición. La igualdad de dominios prueba la longitud. El grafo vacío se transforma en vacío. En $s\frown t$, el valor en un argumento $i\in n$ es $f(s(i))$, y en un argumento $n+k$ de la cola es $f(t(k))$. Esta caracterización coincide exactamente con la concatenación de los dos grafos transformados; por extensionalidad ambas funciones son iguales. No se exige inversibilidad de $f$. $\square$

## 16.60. Recursión y plegado de secuencias finitas

### Metateorema 16.60.1 — Plegado izquierdo único en cualquier alfabeto conjunto {#tlog-mth-00077}

Sean conjuntos $A,B$, un elemento $b\in B$ y una función $H:B\times A\to B$. Existe una única función $F:A^{<\omega}\to B$ para la cual
$$
\boxed{F(\epsilon_A)=b,\qquad F(s\frown\langle a\rangle)=H(F(s),a)\quad(s\in A^{<\omega},\ a\in A).}
$$
El enunciado vale si $A=\varnothing$; $B$ no puede ser vacío porque contiene el dato inicial $b$.

**Demostración.** Dada $s:n\to A$, construimos una operación total $K_s:\omega\times B\to B$ poniendo $K_s(k,z)=H(z,s(k))$ si $k\in n$, y $K_s(k,z)=z$ en otro caso. Como $s$ es funcional, las dos ramas son fórmulas definibles disjuntas; su grafo se obtiene por separación en $(\omega\times B)\times B$. Por el teorema §16.26 existe una única recursión $r_s:\omega\to B$ con $r_s(0)=b$ y $r_s(S(k))=K_s(k,r_s(k))$. Definimos $F(s):=r_s(n)$. La unicidad de $r_s$ y de $n=|s|$ garantiza que $F$ es una función definible; su grafo existe por reemplazo aplicado al conjunto $A^{<\omega}$, sin elegir testigos. Para la secuencia vacía $n=0$, luego $F(\epsilon_A)=b$. Si $s'=s\frown\langle a\rangle$ tiene longitud $S(n)$, entonces $K_{s'}$ y $K_s$ coinciden en todos los argumentos $k\in n$. Una inducción en $k\leq n$ demuestra $r_{s'}(k)=r_s(k)$, y en particular en $k=n$. En ese último punto $s'(n)=a$, por lo que
$$
F(s')=r_{s'}(S(n))=H(r_{s'}(n),a)=H(F(s),a).
$$
Finalmente, si $G$ satisface las mismas dos ecuaciones, el principio de inducción estructural §16.52 demuestra $G(s)=F(s)$ para toda secuencia $s$. No se ha dado por supuesto el teorema de plegado: se ha construido a partir de la recursión sobre $\omega$ ya cerrada. $\square$

## 16.61. Descomposición como unión de potencias finitas

### Proposición 16.61.1 — Familia indexada de espacios de palabras {#tlog-pro-00102}

Para cada $n\in\omega$ el conjunto $A^n:=\{s\in\mathcal P(\omega\times A):s:n\to A\}$ existe y es único. La familia $\langle A^n:n\in\omega\rangle$ existe como grafo funcional y
$$
\boxed{A^{<\omega}=\bigcup_{n\in\omega}A^n.}
$$

**Demostración.** Fijados $A,n$, se aplica separación a $\mathcal P(\omega\times A)$ con la fórmula que expresa $\operatorname{Fun}(s)$ y $\operatorname{dom}(s)=n$, comprobando que la imagen cae en $A$ por la cota. Extensionalidad asegura unicidad de $A^n$. El reemplazo sobre $\omega$ para esta relación funcional forma su grafo y su rango; el axioma de unión produce $\bigcup_{n\in\omega}A^n$. Si $s$ pertenece a esa unión, su dominio es algún $n\in\omega$, luego $s\in A^{<\omega}$. Recíprocamente, toda $s\in A^{<\omega}$ tiene un natural $n=|s|$ y pertenece a $A^n$. La igualdad es extensional. No se escoge ninguna secuencia dentro de cada $A^n$. $\square$

## 16.62. Salida matemática de la infraestructura conjuntista

### Corolario 16.62.1 — Interfaz finitaria cerrada dentro de ZF objeto {#tlog-cor-00023}

**Demostración (síntesis de cierre).** Los §§16.39–16.61 completan en $\mathsf{ZF}_{\mathrm{obj}}$ el buen orden de $\omega$, la definición del orden $\leq$, la formación de todas las secuencias finitas sobre un conjunto arbitrario, la longitud y restricción inicial, el último término, la concatenación y su carácter de monoide, la aplicación de funciones coordenada a coordenada y el plegado recursivo con valor inicial. Los §§16.1–16.38 ya habían construido $0,S,\omega$, inducción, recursión numérica, suma y producto. Cada operación se representa por un conjunto o una fórmula con descripción única y es eliminable en la signatura $\tau_\in$. Se mantiene la metateoría externa $\mathsf M_{\mathrm{ext}}=\mathsf{ZF}$ clásica sin elección, y no se activa ninguna interfaz externa. La **codificación efectiva**, la numeración de Gödel y las afirmaciones de computabilidad no se deducen de este capítulo y se reservan para la Parte IV. No existe aún compilación Lean de estas pruebas. $\square$

**Cierre certificado tras QA y readback:** `TLOG-CH16-M03 = CLOSED / MATHEMATICAL-QA-PASS / DRIVE-READBACK-PASS`; `TLOG-CH16-0001 = CLOSED`; `PART III = CLOSED`. Las auditorías de capítulo y parte están archivadas y los 12 Markdown canónicos han superado SHA-256. **Siguiente capítulo:** `TLOG-CH17-0001 — Computabilidad mínima para la metamatemática` (Parte IV).

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 15](capitulo-15.md) · [Capítulo 17 →](capitulo-17.md)


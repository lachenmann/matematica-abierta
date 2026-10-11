---
title: Capítulo 6 — Variables, sustitución y recursión sintáctica
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
content-id: MA-BCH-0208
content-type: book-chapter
source-id: TLOG-CH06-0001
prerequisites:
- MA-BCH-0207
related:
- MA-BOK-0014
source-sha256: a51dfd65295dba376a866b6a7eeac6bc4dc01e3907633a672f86ad56c8f5440d
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 5](capitulo-05.md) · [Capítulo 7 →](capitulo-07.md)

## 6.0. Objeto, hipótesis y frontera

El Capítulo 5 ha construido, para una signatura unisortada arbitraria $\tau$, los términos $\operatorname{Tm}_\tau$, las fórmulas atómicas $\operatorname{At}_\tau$, las fórmulas $\operatorname{Fm}_\tau$, sus árboles de análisis únicos y la inducción estructural. Aquí se investiga **qué ocurrencias de variables quedan sujetas al alcance de un cuantificador** y cuáles permanecen disponibles para sustitución. El bloque `TLOG-CH06-M01` estudia ocurrencias y vínculos sin ejecutar sustituciones. El bloque `TLOG-CH06-M02` añade recursión general y sustitución de términos; `M03` construye sustitución individual segura y renombrado alfa; `M04` demuestra las leyes generales de sustitución simultánea de fórmulas y cierra la sintaxis del capítulo.

En todo el capítulo se trabaja en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}+$ lógica clásica, sin axioma de elección global, con el conjunto $X=\{x_i:i\in\omega\}$ del §5.3. Los cinco conectivos y ambos cuantificadores siguen siendo operadores **primitivos** de la sintaxis; el signo $\doteq$ es igualdad lógica **en una fórmula objeto** y nunca igualdad metateórica entre términos. Los dominios e interpretaciones de símbolos extralógicos sólo se introducirán en el Capítulo 7.

### Fuentes cotejadas

- `TLOG-SRC-0002`: Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), cap. 2, §2.1, pp. 76–77: distinción entre apariciones libres y ligadas y cláusula metateórica de variables libres. Rol `proof-model / countercheck`.
- `TLOG-SRC-0003`: Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 2, §2.2, pp. 58–59: alcance, cuantificación repetida, posible coexistencia de usos libres y ligados y fórmulas cerradas. Rol `countercheck`.

Para `M02` se amplía el cotejo a Enderton, cap. 1 §1.4 pp. 38–41 (recursión en álgebras libremente generadas), y Rautenberg, cap. 2 §2.2 pp. 58–60 (recursión de fórmulas y sustituciones). Para `M03` se cotejan además Enderton, cap. 2 §2.4 pp. 112–114 (captura y libertad para sustituir), y Rautenberg, cap. 2 §§2.2–2.3 pp. 59–61 y 70–72 (sustituciones y condiciones de colisión). El tratamiento alfa de TLOG se reconstruye de forma exclusivamente **sintáctica**, sin importar las equivalencias semánticas de Rautenberg §2.4.

Las pruebas del capítulo se reconstruyen desde los **árboles parentizados propios de TLOG**. La noción explícita de dirección de ocurrencia y el vínculo con el **cuantificador homónimo más cercano** son decisiones formales locales. No se traslada a TLOG una política de sustitución de las fuentes sin examinar previamente la captura.

## 6.1. Ocurrencias de variables individuales

### Definición 6.1.1 — Direcciones de ocurrencias individuales {#tlog-def-00028}

El árbol sintáctico finito de un término o fórmula tiene una **dirección** para cada nodo: una secuencia finita de etiquetas de rama desde la raíz. La raíz posee dirección vacía $\epsilon$. En una aplicación funcional de aridad $n$, se etiquetan sus hijos $1,\ldots,n$; en un átomo relacional, sus términos argumentos reciben análogamente direcciones $1,\ldots,n$; en una ecuación se distinguen los lados $\mathtt{izq},\mathtt{der}$; en una negación el hijo $\mathtt{cuerpo}$; en un binario $\mathtt{izq},\mathtt{der}$; y en una cuantificación, su única **matriz** se alcanza por $\mathtt{matriz}$. Los tipos de nodo y de rama están etiquetados, de modo que la reutilización de $\mathtt{izq}$ en árboles de distinta clase no crea ambigüedad.

Una **ocurrencia de variable individual en posición de término** es la dirección de una hoja $x\in X$ en un árbol de término que aparece dentro de una fórmula atómica. Se cuenta cada **posición** por separado, aun cuando su token sea igual al de otra hoja. Denotamos el conjunto de tales ocurrencias por $\operatorname{Occ}_X(\varphi)$. Para $o\in\operatorname{Occ}_X(\varphi)$, $\operatorname{var}_\varphi(o)\in X$ es el token leído en esa hoja. De forma análoga, $\operatorname{Occ}_X(t)$ registra las hojas variables de un término $t$.

Los cuantificadores tienen además una **declaración** de variable $x$ en su nodo raíz. El conjunto de declaraciones, con dirección y nombre, se escribe $\operatorname{Binder}_\tau(\varphi)$. La declaración $(b,Q,x)$ en la dirección $b$ de $\operatorname{Quant}_{Q,x}(\psi)$ **no es una hoja de término**: por definición no es un elemento de $\operatorname{Occ}_X(\varphi)$. Así se separan un token que declara un vínculo y las ocurrencias sobre las cuales ese vínculo puede operar.

Definimos también el soporte de un término:

$$
\operatorname{Var}_\tau(t):=
\{\operatorname{var}_t(o):o\in\operatorname{Occ}_X(t)\}.
$$

Las hojas de una constante nularia $f()$ y las de un átomo relacional nulario $R()$ no contienen variables. Todos los conjuntos anteriores son finitos porque proceden de árboles finitos con aridades finitas. Su definición no necesita recurrir a la futura operación general de recursión sintáctica: consiste en seleccionar y etiquetar posiciones de árboles ya construidos por [TLOG-LEM-00009](capitulo-05.md#tlog-lem-00009) y [TLOG-LEM-00010](capitulo-05.md#tlog-lem-00010).

## 6.2. Alcance de los cuantificadores

### Definición 6.2.1 — Alcance y vinculación {#tlog-def-00029}

Sea $b$ la dirección de una declaración cuantificadora $(b,Q,x)$ en el árbol de una fórmula $\varphi$. El **alcance sintáctico** de esa declaración es el subárbol de fórmula correspondiente a su matriz $\psi$; por tanto incluye todos los descendientes de la dirección $b\mathbin{\frown}\langle\mathtt{matriz}\rangle$, pero **no** incluye ramas hermanas de un constructor binario situado fuera de la matriz. Una ocurrencia de término $o\in\operatorname{Occ}_X(\varphi)$ se encuentra en ese alcance precisamente cuando su dirección prolonga aquella dirección de matriz.

Decimos que la declaración $(b,Q,x)$ es **candidata a vincular** la ocurrencia $o$ si $\operatorname{var}_\varphi(o)=x$ y $o$ pertenece a su alcance. Cuando existen varias declaraciones homónimas anidadas que satisfacen estas condiciones, llamamos **cuantificador vinculante** de $o$ a la de mayor profundidad, esto es, la declaración candidata cuyo nodo es ancestro propio más próximo a $o$. Denotamos este cuantificador por $\operatorname{bind}_\varphi(o)$. Si no existe ninguno, escribimos $\operatorname{bind}_\varphi(o)=\varnothing$ como abreviatura de «ningún cuantificador vinculante»; $\varnothing$ no es una declaración de cuantificador.

El cuantificador exterior sigue teniendo su propio alcance aunque una declaración homónima interior **oculte** su influencia sobre ciertas ocurrencias. La elección de $\forall$ o $\exists$ no modifica esta regla puramente sintáctica.

## 6.3. Unicidad del vínculo

### Lema 6.3.1 — Existencia y unicidad del vinculante más próximo {#tlog-lem-00011}

Para cada fórmula $\varphi$ y cada ocurrencia $o\in\operatorname{Occ}_X(\varphi)$, existe **a lo sumo una** declaración $\operatorname{bind}_\varphi(o)$. Si hay al menos una declaración candidata, existe exactamente una que cumple la condición de máxima profundidad. En consecuencia, la distinción entre ocurrencia libre y vinculada que se definirá en §6.4 es **exhaustiva y excluyente**.

#### Demostración

La legibilidad única de §5.14 produce un árbol finito en el que la dirección de $o$ determina una sola cadena de ancestros desde la raíz hasta su hoja. Todos los cuantificadores candidatos se encuentran entre esos ancestros; en particular, sus direcciones se comparan por relación de prefijo y, si son distintas, por longitud. Una familia finita no vacía de tales direcciones posee una longitud máxima. Si dos candidatas tuvieran esa misma longitud, serían el mismo prefijo de la dirección $o$; por la unicidad del análisis sintáctico, corresponderían a un único nodo cuantificador y a una única declaración. Así existe una candidata máxima única. En ausencia de candidatas no se asigna vinculante. Estos dos casos agotan todas las posibilidades. $\square$

La prueba utiliza sólo finitud y unicidad del árbol; no usa semántica, elección ni equivalencia entre fórmulas.

## 6.4. Variables libres y ligadas

### Definición 6.4.1 — Ocurrencias libres, ocurrencias ligadas y variables libres {#tlog-def-00030}

Una ocurrencia $o\in\operatorname{Occ}_X(\varphi)$ se llama **libre** si no tiene cuantificador vinculante y **ligada** si lo tiene. Escribimos

$$
\begin{aligned}
\operatorname{FreeOcc}_\tau(\varphi)&:=\{o\in\operatorname{Occ}_X(\varphi):\operatorname{bind}_\varphi(o)=\varnothing\},\\
\operatorname{BoundOcc}_\tau(\varphi)&:=\operatorname{Occ}_X(\varphi)\setminus\operatorname{FreeOcc}_\tau(\varphi).
\end{aligned}
$$

El conjunto de **variables libres** es el conjunto de nombres que tienen al menos una ocurrencia libre:

$$
\boxed{\operatorname{FV}_\tau(\varphi):=
\{\operatorname{var}_\varphi(o):o\in\operatorname{FreeOcc}_\tau(\varphi)\}.}
$$

Para evitar dos nociones homónimas, fijamos asimismo

$$
\begin{aligned}
\operatorname{QVar}_\tau(\varphi)
&:=\{x\in X:\exists b,Q\ ((b,Q,x)\in\operatorname{Binder}_\tau(\varphi))\},\\
\operatorname{BVocc}_\tau(\varphi)
&:=\{\operatorname{var}_\varphi(o):o\in\operatorname{BoundOcc}_\tau(\varphi)\}.
\end{aligned}
$$

La primera colección contiene los **nombres declarados por cuantificadores**; la segunda, los nombres de las **ocurrencias de término efectivamente ligadas**. Una cuantificación vacua puede añadir un nombre a $\operatorname{QVar}_\tau$ sin añadir ninguna ocurrencia a $\operatorname{BoundOcc}_\tau$ o a $\operatorname{BVocc}_\tau$. Un mismo nombre $x$ puede pertenecer a $\operatorname{FV}_\tau(\varphi)$ y a $\operatorname{BVocc}_\tau(\varphi)$ porque ambas propiedades se refieren a **ocurrencias distintas**.

Esta definición clasifica ocurrencias de **términos en fórmulas**. Los tokens que figuran en las declaraciones de cuantificación están etiquetados como declaradores, no como ocurrencias libres o ligadas de término.

## 6.5. Caracterización estructural de variables libres

### Metateorema 6.5.1 — Ecuaciones de variables libres {#tlog-mth-00016}

Para cualquier término $t$, cualquier fórmula $\varphi,\psi$, $Q\in\{\forall,\exists\}$, $x\in X$, y $\circ\in\{\land,\lor,\to,\leftrightarrow\}$, el conjunto de variables libres de §6.4 satisface:

$$
\begin{aligned}
\operatorname{Var}_\tau(x)&=\{x\},\\
\operatorname{Var}_\tau(f(t_1,\ldots,t_n))&=\bigcup_{i=1}^{n}\operatorname{Var}_\tau(t_i) \quad(f\in F_n),\\
\operatorname{FV}_\tau(\operatorname{Rel}_{R}(t_1,\ldots,t_n))
 &=\bigcup_{i=1}^{n}\operatorname{Var}_\tau(t_i) \quad(R\in R_n),\\
\operatorname{FV}_\tau(\operatorname{Eq}(s,t))
 &=\operatorname{Var}_\tau(s)\cup\operatorname{Var}_\tau(t),\\
\operatorname{FV}_\tau(\operatorname{Neg}(\varphi))&=\operatorname{FV}_\tau(\varphi),\\
\operatorname{FV}_\tau(\operatorname{Bin}_{\circ}(\varphi,\psi))
 &=\operatorname{FV}_\tau(\varphi)\cup\operatorname{FV}_\tau(\psi),\\
\operatorname{FV}_\tau(\operatorname{Quant}_{Q,x}(\varphi))
 &=\operatorname{FV}_\tau(\varphi)\setminus\{x\}.
\end{aligned}
$$

Las uniones de aridad cero son $\varnothing$. Las ecuaciones son válidas para ambos cuantificadores **primitivos**, sin identificar $\exists x\varphi$ con ninguna abreviatura que use $\forall$.

#### Demostración

**Primer paso: términos.** Una hoja variable $x$ es su única ocurrencia; una aplicación $f(t_1,\ldots,t_n)$ añade el símbolo $f$ y separadores, pero no hojas variables nuevas. Las hojas del término compuesto son exactamente las de los $n$ argumentos en sus direcciones disjuntas. Esto demuestra la cláusula de $\operatorname{Var}_\tau$, incluyendo $n=0$. El razonamiento recorre los constructores de [TLOG-MTH-00014](capitulo-05.md#tlog-mth-00014).

**Segundo paso: átomos.** En un átomo no existe un ancestro cuantificador; por tanto, todas sus hojas variables son libres. En $\operatorname{Rel}_{R}(t_1,\ldots,t_n)$ se reúnen las ocurrencias de cada término argumento, y en $\operatorname{Eq}(s,t)$, las de sus dos lados. Esto prueba las dos ecuaciones atómicas.

**Tercer paso: fórmulas compuestas.** Procedemos por los casos de inducción de [TLOG-MTH-00015](capitulo-05.md#tlog-mth-00015). La negación no incorpora declaraciones ni modifica ancestros cuantificadores de sus hojas; las libres son exactamente las de la matriz. Un constructor binario tampoco incorpora declaradores; cada ocurrencia está en una de sus dos ramas y conserva en ella el mismo vinculante que antes de formar el binario. Por eso las variables libres son la unión indicada.

Por último, $\operatorname{Quant}_{Q,x}(\varphi)$ incorpora una declaración exterior de $x$, cuyo alcance es la matriz completa. Si una hoja ya tenía un vinculante en $\varphi$, éste continúa siendo el más cercano; si era libre y su nombre es $x$, la nueva declaración la vincula; y si era libre pero tiene nombre distinto de $x$, sigue sin vinculante. En consecuencia, se eliminan **exactamente** los nombres $x$ de las ocurrencias anteriormente libres. Obtenemos $\operatorname{FV}_\tau(\varphi)\setminus\{x\}$, con independencia de que $Q$ sea $\forall$ o $\exists$. No quedan otros constructores. $\square$

El teorema prueba que las ecuaciones usuales de variables libres coinciden con la definición fundamental **por direcciones de ocurrencia**. No se invoca una transformación arbitraria de fórmulas definida por recursión ni un teorema de sustitución pendiente.

## 6.6. Fórmulas cerradas

### Definición 6.6.1 — Sentencia {#tlog-def-00031}

Una **fórmula cerrada**, también llamada **sentencia** de la signatura $\tau$, es una fórmula sin ocurrencias individuales libres:

$$
\operatorname{Sent}_\tau:=\{
\varphi\in\operatorname{Fm}_\tau:
\operatorname{FV}_\tau(\varphi)=\varnothing
\}.
$$

El término «sentencia» designa aquí sólo una propiedad **sintáctica**. No afirma verdad, validez ni demostrabilidad. Una sentencia puede tener cuantificadores vacuos; también puede carecer de cuantificadores si, por ejemplo, sus términos son constantes o se usa un predicado nulario. La clase $\operatorname{Sent}_\tau$ es un conjunto en ZF porque es un subconjunto definido de $\operatorname{Fm}_\tau$.

## 6.7. Finitud y distinciones necesarias

### Proposición 6.7.1 — Finitud y coexistencia de estados de ocurrencia {#tlog-pro-00005}

Para toda fórmula $\varphi\in\operatorname{Fm}_\tau$:

1. $\operatorname{FV}_\tau(\varphi)$, $\operatorname{QVar}_\tau(\varphi)$, $\operatorname{FreeOcc}_\tau(\varphi)$ y $\operatorname{BoundOcc}_\tau(\varphi)$ son conjuntos finitos.
2. $\operatorname{FreeOcc}_\tau(\varphi)$ y $\operatorname{BoundOcc}_\tau(\varphi)$ particionan $\operatorname{Occ}_X(\varphi)$, aun cuando $\operatorname{FV}_\tau(\varphi)\cap\operatorname{BVocc}_\tau(\varphi)\ne\varnothing$.
3. La igualdad de conjuntos $\operatorname{FV}_\tau(\operatorname{Quant}_{\forall,x}(\psi))=\operatorname{FV}_\tau(\operatorname{Quant}_{\exists,x}(\psi))$ es una **identidad sintáctica** de soportes libres, no una equivalencia lógica entre las fórmulas cuantificadas.
4. Un cuantificador puede tener alcance no vacío y no vincular ninguna ocurrencia del nombre declarado (*cuantificación vacua*).

#### Demostración

El árbol de análisis de $\varphi$ contiene un número finito de nodos, luego sólo un número finito de hojas variables y declaraciones cuantificadoras. Las cuatro colecciones del punto 1 son subconjuntos o imágenes de esas colecciones finitas; son finitas. La partición del punto 2 es inmediata de la existencia o inexistencia de vinculante único por el lema 6.3.1. El punto 3 es la aplicación de la última ecuación del metateorema 6.5.1 a $Q=\forall$ y a $Q=\exists$. Para el punto 4, basta tomar $\psi=(x_1\doteq x_1)$ y cuantificar con $x_0\ne x_1$: la matriz existe, pero no contiene ninguna ocurrencia de $x_0$. $\square$

Para comprobar que el punto 2 permite de verdad nombres simultáneamente libres y ligados, elijamos una signatura con $P\in R_1$ y la fórmula

$$
\Phi:=\bigl((\forall x_0\,P(x_0))\land P(x_0)\bigr).
$$

La primera aparición de $x_0$ como argumento de $P$ tiene vinculante $\forall x_0$; la segunda está en la rama derecha de la conjunción y queda libre, fuera del alcance de ese cuantificador. Por tanto $x_0\in\operatorname{FV}_\tau(\Phi)\cap\operatorname{BVocc}_\tau(\Phi)$, sin que ninguna **ocurrencia individual** sea simultáneamente libre y ligada.

## 6.8. Ejemplos de análisis de alcance

**Cuantificación anidada y ocultamiento.** En

$$
\Theta:=\forall x_0\,\exists x_0\,P(x_0),
$$

el vinculante de la única ocurrencia de término $x_0$ es el $\exists x_0$ interno, no el $\forall x_0$ externo. El cuantificador externo tiene alcance que contiene al interno, pero no vincula ninguna ocurrencia de término en esta fórmula. Además $\operatorname{FV}_\tau(\Theta)=\varnothing$; es una sentencia.

**Aparición declarativa, sin aparición de término.** Si $Q\in R_0$, la fórmula $\forall x_0\,Q()$ tiene $\operatorname{QVar}_\tau=\{x_0\}$ y $\operatorname{Occ}_X=\varnothing$. El nombre $x_0$ figura en el token de declaración, pero no es una ocurrencia libre ni ligada de término.

**Igualdad puramente lógica.** En la signatura vacía, $\forall x_0\,(x_0\doteq x_1)$ contiene una ocurrencia ligada de $x_0$ y una libre de $x_1$; no es una sentencia. Cuantificar externamente por $x_1$ sí produce una sentencia. Estas afirmaciones dependen sólo de la sintaxis de igualdad como átomo.

## 6.9. Frontera y estado de `M01`

El bloque demuestra los vínculos entre declaraciones de cuantificación y ocurrencias individuales, así como las ecuaciones y la finitud de variables libres. **No** autoriza aún escribir $\varphi[t/x]$ sin condiciones, sustituir bajo cuantificadores, efectuar $\alpha$-renombrado ni identificar $\alpha$-equivalencia con igualdad sintáctica. Esas obligaciones exigen una teoría precisa de recursión y sustitución, que continuará dentro de este capítulo. No se construye ningún modelo ni cálculo deductivo de primer orden.

```text
TLOG-CH06-M01 = CLOSED / PASS
TLOG-CH06-0001 = PARTIAL-CLOSURE / NOT CLOSED
new mathematical nodes = 7
chapter 6 nodes = 7 closed
TLOG registered/closed nodes = 76/76
DAG = 76 nodes / 163 direct edges / PASS
external interfaces = 0
formalization candidates = 17
compiled/verified = 0
chapters closed = 6/24
PART I = CLOSED / PASS
PART II = OPEN
```

Siguiente microtramo: `TLOG-CH06-M02 — Recursión sintáctica de términos y fórmulas; preparación de sustituciones`.

## 6.10. Recursión estructural sobre términos

### Metateorema 6.10.1 — Existencia y unicidad de la recursión de términos {#tlog-mth-00017}

Sea $\tau=((F_n)_{n\in\omega},(R_n)_{n\in\omega})$ una signatura, $A$ un **conjunto** y supongamos dados:

- una aplicación $a:X\to A$;
- para cada $n\in\omega$ y cada $f\in F_n$, una aplicación $G_f:A^n\to A$, incluido $n=0$ (en ese caso $A^0=\{()\}$).

Entonces existe **una única** función $h:\operatorname{Tm}_\tau\to A$ tal que

$$
\boxed{h(x)=a(x)\quad(x\in X),\qquad
h(f(t_1,\ldots,t_n))=G_f(h(t_1),\ldots,h(t_n)).}
$$

Las ecuaciones requieren $n$ argumentos exactamente y son válidas también para las constantes $f()$, cuyo valor es $G_f(())$. No se supone numerabilidad de $\tau$, efectividad de las operaciones $G_f$ ni elección.

#### Demostración

La definición inductiva [TLOG-DEF-00024](capitulo-05.md#tlog-def-00024) construye los conjuntos crecientes $T_k$ con $\operatorname{Tm}_\tau=\bigcup_{k<\omega}T_k$. Definimos, por recursión ordinaria sobre $k$, funciones compatibles $h_k:T_k\to A$. En $T_0$ asignamos $a(x)$ a cada variable y $G_f(())$ a cada constante $f()$. Son asignaciones compatibles porque los constructores variable y aplicación funcional nularia son disjuntos.

Si $h_k$ está definido, conservamos sus valores en $T_k$. A cada término nuevo de $T_{k+1}\setminus T_k$, necesariamente de la forma $f(t_1,\ldots,t_n)$ con $n\ge1$ y $t_i\in T_k$, asignamos $G_f(h_k(t_1),\ldots,h_k(t_n))$. La legibilidad única de [TLOG-LEM-00009](capitulo-05.md#tlog-lem-00009) asegura que $f$ y la lista ordenada de argumentos no admiten una segunda lectura. Si una expresión ya estaba en $T_k$, su valor anterior satisface la misma ecuación por la construcción en la etapa de su primera aparición; por tanto, conservarlo no genera incompatibilidad. Así $h_{k+1}|_{T_k}=h_k$.

La unión $h:=\bigcup_{k<\omega}h_k$ es una función con dominio $\operatorname{Tm}_\tau$ y satisface ambas cláusulas: todos los argumentos de cualquier aplicación están en una etapa común y finita. Si $h'$ satisface las mismas cláusulas, $h'(x)=h(x)$ en las variables y constantes. La inducción estructural [TLOG-MTH-00014](capitulo-05.md#tlog-mth-00014) propaga la igualdad desde los argumentos a cada aplicación funcional, luego $h'=h$. Todas las etapas, grafos y uniones se obtienen en ZF. $\square$

::: {.callout-note}
## Alcance

El principio de inducción de §5.6 demuestra propiedades de funciones **ya definidas**; este metateorema demuestra que los datos recursivos compatibles determinan efectivamente una función y que no pueden determinar dos. Esa diferencia es indispensable para la sustitución.
:::

## 6.11. Recursión estructural sobre fórmulas

### Metateorema 6.11.1 — Existencia y unicidad de la recursión de fórmulas {#tlog-mth-00018}

Sea $B$ un conjunto y fijemos los siguientes **datos de recursión**:

$$
\begin{aligned}
b&:\operatorname{At}_\tau\to B,\\
N&:B\to B,\\
D_\circ&:B\times B\to B &&(\circ\in\{\land,\lor,\to,\leftrightarrow\}),\\
U_{Q,x}&:B\to B &&(Q\in\{\forall,\exists\},\ x\in X).
\end{aligned}
$$

Existe **una única** función $H:\operatorname{Fm}_\tau\to B$ que satisface simultáneamente

$$
\begin{aligned}
H(\alpha)&=b(\alpha)&& (\alpha\in\operatorname{At}_\tau),\\
H(\operatorname{Neg}(\varphi))&=N(H(\varphi)),\\
H(\operatorname{Bin}_\circ(\varphi,\psi))&=D_\circ(H(\varphi),H(\psi)),\\
H(\operatorname{Quant}_{Q,x}(\varphi))&=U_{Q,x}(H(\varphi)).
\end{aligned}
$$

Ambos cuantificadores y los cuatro conectivos binarios se tratan como constructores **primitivos distintos**. El mapa inicial $b$ abarca los átomos relacionales, incluso los nularios, y las ecuaciones de igualdad lógica. Los valores de $H$ no tienen interpretación semántica presupuesta.

#### Demostración

Empleamos la sucesión $W_0=\operatorname{At}_\tau$, $W_{k+1}$ del §5.13. Sobre $W_0$ definimos $H_0=b$. Dado $H_k:W_k\to B$, extendemos su valor a cada fórmula nueva de $W_{k+1}\setminus W_k$ mediante una de las tres cláusulas compuestas. En cada caso, las subfórmulas inmediatas pertenecen a $W_k$. Por [TLOG-LEM-00010](capitulo-05.md#tlog-lem-00010), la fórmula determina **exactamente un** constructor raíz y sus argumentos; por tanto ninguna fórmula recibe prescripciones incompatibles. Las fórmulas que ya pertenecen a $W_k$ conservan su valor, que satisface las cláusulas aplicables por la etapa en que fueron incorporadas.

Obtenemos una familia compatible de grafos y su unión $H=\bigcup_kH_k$, con dominio $\operatorname{Fm}_\tau$. Cada cláusula se cumple porque una fórmula compuesta y todas sus subfórmulas aparecen en etapas finitas. Para la unicidad, si $H'$ satisface los mismos datos, las dos funciones coinciden en todos los átomos. La inducción estructural [TLOG-MTH-00015](capitulo-05.md#tlog-mth-00015), usando sucesivamente los casos de negación, los cuatro conectivos y ambos cuantificadores para cada $x$, demuestra $H'(\varphi)=H(\varphi)$ para toda fórmula. La recursión sobre $\omega$ y las imágenes de conjuntos se realizan en ZF, sin AC. $\square$

Es esencial que las operaciones $U_{Q,x}$ estén dadas **para todos** los pares $(Q,x)$. El enunciado no permite asumir una sola cláusula cuantificadora ni confundir la variable que declara el cuantificador con una variable libre de su matriz.

## 6.12. La función de variables libres como instancia recursiva

### Corolario 6.12.1 — Caracterización funcional única de $\operatorname{FV}_\tau$ {#tlog-cor-00004}

La aplicación $\operatorname{FV}_\tau:\operatorname{Fm}_\tau\to\mathcal P(X)$, definida originalmente por **ocurrencias y vínculos** en §6.4, es la única función $V:\operatorname{Fm}_\tau\to\mathcal P(X)$ que satisface

$$
\begin{aligned}
V(\operatorname{Rel}_R(t_1,\ldots,t_n))&=\bigcup_{i=1}^n\operatorname{Var}_\tau(t_i),\\
V(\operatorname{Eq}(s,t))&=\operatorname{Var}_\tau(s)\cup\operatorname{Var}_\tau(t),\\
V(\operatorname{Neg}(\varphi))&=V(\varphi),\\
V(\operatorname{Bin}_\circ(\varphi,\psi))&=V(\varphi)\cup V(\psi),\\
V(\operatorname{Quant}_{Q,x}(\varphi))&=V(\varphi)\setminus\{x\}.
\end{aligned}
$$

#### Demostración

Tomamos $B=\mathcal P(X)$ en el metateorema 6.11.1; asignamos a cada átomo su conjunto de variables de término, a la negación la identidad, a cada conectivo binario la unión y a cada par $(Q,x)$ la operación $S\mapsto S\setminus\{x\}$. Son aplicaciones totales sobre conjuntos y satisfacen las hipótesis de recursión. El metateorema garantiza exactamente una función $V$. Por [TLOG-MTH-00016](#tlog-mth-00016), $\operatorname{FV}_\tau$ —ya definida sin usar recursión general— satisface esas cinco familias de ecuaciones; de ahí, por unicidad, $V=\operatorname{FV}_\tau$. $\square$

Esta identificación **verifica** la definición por ocurrencias ya cerrada; no la sustituye retroactivamente ni convierte las variables libres en un concepto semántico.

## 6.13. Sustitución simultánea de términos

### Definición 6.13.1 — Sustitución de variables por términos {#tlog-def-00032}

Una **sustitución de términos** de signatura $\tau$ es una aplicación total

$$
\sigma:X\longrightarrow\operatorname{Tm}_\tau.
$$

Aplicando el metateorema 6.10.1 con $A=\operatorname{Tm}_\tau$, $a=\sigma$ y $G_f(t_1,\ldots,t_n)=f(t_1,\ldots,t_n)$, obtenemos su **extensión homomórfica única** $\widehat\sigma:\operatorname{Tm}_\tau\to\operatorname{Tm}_\tau$. Denotamos $t^\sigma:=\widehat\sigma(t)$. Satisface

$$
\boxed{x^\sigma=\sigma(x),\qquad
f(t_1,\ldots,t_n)^\sigma=f(t_1^\sigma,\ldots,t_n^\sigma).}
$$

Una constante $f()$ queda inalterada. El reemplazo es **simultáneo**: los términos insertados como $\sigma(x)$ no son sustituidos por segunda vez durante la misma operación. Se define el **soporte** de la sustitución como

$$
\operatorname{supp}(\sigma):=\{x\in X:\sigma(x)\ne x\}.
$$

La sustitución es *finitaria* o *de soporte finito* cuando ese conjunto es finito. Dados nombres individuales distintos $x_1,\ldots,x_m$ y términos $s_1,\ldots,s_m$, la aplicación $\sigma(x_i)=s_i$ y $\sigma(y)=y$ fuera de esa lista es una sustitución finitaria, aun si algún $s_i$ contiene alguno de los $x_j$. El caso $m=0$ da la identidad. Para una sustitución simple, $t[s/x]$ **sólo cuando $t$ es término** abrevia $t^{\sigma_{x\mapsto s}}$, donde $\sigma_{x\mapsto s}(x)=s$ y deja fijas las demás variables.

**Frontera de dominio.** La expresión $\varphi^\sigma$ para $\varphi\in\operatorname{Fm}_\tau$ **no queda definida** por esta pieza. Sobre términos no existe cuantificador que pueda capturar una variable; sobre fórmulas sí. No se transportará la notación $[s/x]$ de términos a fórmulas hasta especificar una política de ligadura.

## 6.14. Soporte de variables después de sustituir términos

### Lema 6.14.1 — Fórmula exacta de soporte {#tlog-lem-00012}

Para toda sustitución $\sigma:X\to\operatorname{Tm}_\tau$ y todo término $t$,

$$
\boxed{\operatorname{Var}_\tau(t^\sigma)
=\bigcup_{x\in\operatorname{Var}_\tau(t)}\operatorname{Var}_\tau(\sigma(x)).}
$$

En particular, ambos lados son conjuntos **finitos**; no se requiere que $\operatorname{supp}(\sigma)$ sea finito.

#### Demostración

Aplicamos la inducción estructural [TLOG-MTH-00014](capitulo-05.md#tlog-mth-00014). Si $t=x$, el lado izquierdo es $\operatorname{Var}_\tau(\sigma(x))$ por la definición de $x^\sigma$, y el derecho es la unión indexada por el singleton $\{x\}$. Si $t=f(t_1,\ldots,t_n)$, la cláusula de sustitución de §6.13 y las ecuaciones de variables de [TLOG-MTH-00016](#tlog-mth-00016) dan

$$
\begin{aligned}
\operatorname{Var}_\tau(t^\sigma)
&=\bigcup_{i=1}^n\operatorname{Var}_\tau(t_i^\sigma)\\
&=\bigcup_{i=1}^n\ \bigcup_{x\in\operatorname{Var}_\tau(t_i)}\operatorname{Var}_\tau(\sigma(x))\\
&=\bigcup_{x\in\operatorname{Var}_\tau(t)}\operatorname{Var}_\tau(\sigma(x)).
\end{aligned}
$$

Para $n=0$, ambos miembros son la unión vacía y valen $\varnothing$. Para $n>0$, sólo se reordenan uniones **finitas**; la ecuación de soporte de $t$ justifica la última igualdad. Como $\operatorname{Var}_\tau(t)$ es finito y cada $\sigma(x)$ es un término finito, también lo es la unión. $\square$

::: {.callout-important}
## Límite de interpretación

La fórmula es una identidad de conjuntos de nombres presentes en un **término**. No afirma que las variables de $\sigma(x)$ conserven su condición libre cuando se introduzcan dentro de una fórmula cuantificada.
:::

## 6.15. Identidad, composición y carácter simultáneo

### Proposición 6.15.1 — Leyes algebraicas de la sustitución de términos {#tlog-pro-00006}

Definimos $\iota:X\to\operatorname{Tm}_\tau$ por $\iota(x)=x$. Para sustituciones $\sigma,\rho$ definimos una tercera sustitución $\sigma\star\rho$ por

$$
(\sigma\star\rho)(x):=(\sigma(x))^\rho.
$$

La estrella significa: aplicar primero $\sigma$ y después $\rho$. Para todo término $t$:

$$
\boxed{t^\iota=t,\qquad (t^\sigma)^\rho=t^{\sigma\star\rho}.}
$$

Además, $\star$ es asociativa y $\iota$ es identidad bilateral en el conjunto de sustituciones de términos de signatura $\tau$.

#### Demostración

**Identidad.** La función identidad $t\mapsto t$ satisface las cláusulas de extensión de $\iota$; por la unicidad de [TLOG-MTH-00017](#tlog-mth-00017), coincide con $\widehat\iota$. Equivalentemente, se comprueba por inducción sobre términos.

**Composición.** La función $k(t):=(t^\sigma)^\rho$ satisface $k(x)=(\sigma(x))^\rho=(\sigma\star\rho)(x)$. Si $t=f(t_1,\ldots,t_n)$, la extensión de ambas sustituciones da $k(t)=f(k(t_1),\ldots,k(t_n))$, también cuando $n=0$. Por la unicidad de la extensión correspondiente a $\sigma\star\rho$, tenemos $k=\widehat{\sigma\star\rho}$. Esto prueba la segunda identidad.

Para la asociatividad, en cualquier $x\in X$ las dos composiciones se evalúan como

$$
((\sigma\star\rho)\star\kappa)(x)=((\sigma(x))^\rho)^\kappa
=(\sigma(x))^{\rho\star\kappa}
=(\sigma\star(\rho\star\kappa))(x).
$$

La igualdad para todos los $x$ implica igualdad de funciones. Finalmente $(\iota\star\sigma)(x)=x^\sigma=\sigma(x)$ y $(\sigma\star\iota)(x)=\sigma(x)^\iota=\sigma(x)$. $\square$

**Por qué «simultánea» no significa «sucesiva».** Sea $f\in F_2$, $t=f(x_0,x_1)$ y sea $\sigma$ el intercambio $x_0\mapsto x_1$, $x_1\mapsto x_0$, identidad en las demás variables. Entonces

$$
t^\sigma=f(x_1,x_0).
$$

En cambio, aplicar primero la sustitución simple $[x_1/x_0]$ y después $[x_0/x_1]$ produce

$$
\bigl(t[x_1/x_0]\bigr)[x_0/x_1]
=f(x_0,x_0),
$$

que no es el intercambio. La composición correcta registra las sustituciones sucesivas mediante $\star$, y no mediante una superposición ingenua de tablas de reemplazo.

## 6.16. Advertencia necesaria antes de sustituir fórmulas

Considérese una signatura con $P\in R_1$ y la fórmula $\forall x_0(P(x_1))$. En ella, la ocurrencia de término $x_1$ es libre, según §6.4. Si se insertara **literalmente** $x_0$ en esa posición, se obtendría la cadena bien formada $\forall x_0(P(x_0))$; pero la ocurrencia insertada quedaría ahora **ligada** por el cuantificador exterior. Este fenómeno es **captura de variable**. La inserción descrita ilustra un error, **no** define una operación autorizada sobre fórmulas.

La recursión de §6.11 permite definir funciones sobre fórmulas cuando se proporcionan sus datos estructurales, pero esos datos deben ser **adecuados a la ligadura**. Para una sustitución de fórmulas que conserve correctamente las ocurrencias libres, hay que distinguir al menos: la variable que se reemplaza, los nombres libres del término introducido, las declaraciones bajo las que se entra y la necesidad eventual de escoger un nombre fresco. Ninguna de estas decisiones se suple con la simple cláusula de términos de §6.13.

No se ha demostrado aún una equivalencia alfa ni se han fijado operaciones de renombrado de declaraciones. Tampoco se ha decidido por mera exposición que $\forall x_0P(x_0)$ y $\forall x_2P(x_2)$ sean **la misma cadena**: son expresiones formalmente distintas aunque más adelante se pueda estudiar una relación de renombrado entre ellas.

## 6.17. Estado y frontera del microtramo `M02`

El bloque establece por primera vez **existencia y unicidad de definiciones recursivas generales** sobre términos y fórmulas; recupera la función $\operatorname{FV}_\tau$ como instancia única y construye la sustitución **únicamente sobre términos**, con fórmula exacta de soporte y leyes de identidad/composición. Ningún teorema del bloque depende de semántica ni de reglas deductivas de primer orden.

```text
TLOG-CH06-M01 = CLOSED / PASS
TLOG-CH06-M02 = CLOSED / PASS
TLOG-CH06-0001 = PARTIAL-CLOSURE / NOT CLOSED
new mathematical nodes = 6
chapter 6 closed nodes = 13
TLOG registered/closed nodes = 82/82
DAG = 82 nodes / 179 direct edges / PASS
external interfaces = 0
formalization candidates = 20
compiled/verified = 0
chapters closed = 6/24
PART I = CLOSED / PASS
PART II = OPEN
```

Siguiente microtramo: `TLOG-CH06-M03 — Sustitución de fórmulas, libertad para sustituir, captura y renombrado de variables ligadas`.

## 6.18. Nombres sintácticos y selección canónica de variables frescas

### Definición 6.18.1 — Soporte total de nombres de una fórmula {#tlog-def-00033}

No basta conocer las **variables libres** para renombrar un cuantificador: hay que evitar también las declaraciones interiores con las cuales podría producirse una colisión. Para una fórmula $\varphi$, definimos el **soporte total de nombres**

$$
\operatorname{Names}_\tau(\varphi):=
\{\operatorname{var}_\varphi(o):o\in\operatorname{Occ}_X(\varphi)\}
\cup\operatorname{QVar}_\tau(\varphi).
$$

Es una unión de conjuntos finitos, por [TLOG-PRO-00005](#tlog-pro-00005). En particular, $\operatorname{FV}_\tau(\varphi)\subseteq\operatorname{Names}_\tau(\varphi)$. Si $A\subseteq X$ es **finito**, sea

$$
\operatorname{fresh}(A):=x_{\min\{i\in\omega:x_i\notin A\}}.
$$

Como $X=\{x_i:i\in\omega\}$ es infinito y $A$ finito, el conjunto de índices es no vacío, tiene mínimo y determina **una única** variable fresca. Esta operación usa el orden fijado de $X$, sin selección arbitraria ni axioma de elección. La restricción a conjuntos finitos es esencial: la construcción no pretende escoger una variable fuera de cualquier subconjunto de $X$.

## 6.19. Libertad para sustituir

### Definición 6.19.1 — Predicado sintáctico «$t$ libre para $x$ en $\varphi$» {#tlog-def-00034}

Fijados $t\in\operatorname{Tm}_\tau$ y $x\in X$, definimos por recursión sobre la fórmula el predicado metateórico $\operatorname{FreeFor}_\tau(t,x,\varphi)$. En los átomos vale siempre; atraviesa negación sin cambio y un conectivo binario si y sólo si vale en ambas ramas. Para $Q\in\{\forall,\exists\}$, la condición de cuantificación es

$$
\boxed{
\operatorname{FreeFor}_\tau(t,x,Qy\,\psi)
\iff
\begin{cases}
\mathrm{verdadero}, &y=x,\\
\operatorname{FreeFor}_\tau(t,x,\psi)\ \land\
\bigl(x\notin\operatorname{FV}_\tau(\psi)\ \lor\ y\notin\operatorname{Var}_\tau(t)\bigr),&y\ne x.
\end{cases}}
$$

En el caso $y=x$, **ninguna** ocurrencia de $x$ en la matriz es libre en la fórmula completa $Qx\,\psi$: no se atraviesa ese cuantificador al sustituir las ocurrencias libres de $x$. Si $y\ne x$, es indispensable que no haya peligro en la matriz y, cuando haya una ocurrencia libre de $x$ en ella, que la variable declarada $y$ no figure entre los nombres del término $t$ que se insertará. Las cláusulas cubren los átomos nularios, los cinco conectivos primitivos (uno unario y cuatro binarios) y ambos cuantificadores primitivos; por [TLOG-MTH-00018](#tlog-mth-00018) el predicado está determinado de manera única.

Ser libre para sustituir **no significa** que $t$ carezca de variables ni que su inserción cambie una fórmula semánticamente. Es únicamente una condición de **seguridad sintáctica** para preservar la ausencia de captura.

## 6.20. Caracterización por ocurrencias

### Lema 6.20.1 — Criterio necesario y suficiente de ausencia de captura {#tlog-lem-00013}

Para $t\in\operatorname{Tm}_\tau$, $x\in X$ y $\varphi\in\operatorname{Fm}_\tau$, son equivalentes:

1. $\operatorname{FreeFor}_\tau(t,x,\varphi)$.
2. Para **cada ocurrencia libre** $o\in\operatorname{FreeOcc}_\tau(\varphi)$ cuyo nombre sea $x$, ningún cuantificador ancestro de $o$ declara una variable perteneciente a $\operatorname{Var}_\tau(t)$.

En particular, $x\notin\operatorname{FV}_\tau(\varphi)$ implica $\operatorname{FreeFor}_\tau(t,x,\varphi)$, y $\operatorname{FreeFor}_\tau(x,x,\varphi)$ vale para toda fórmula $\varphi$.

#### Demostración

Inducimos sobre la estructura de $\varphi$. En un átomo todas las hojas son libres y no hay cuantificadores ancestros; ambas condiciones son verdaderas. La negación conserva todas las declaraciones internas y no añade ninguna, por lo que la equivalencia se hereda. En un binario, sus dos conjuntos de ocurrencias forman ramas disjuntas, y la propiedad es la conjunción de las propiedades de ambas ramas.

Supongamos $\varphi=Qy\,\psi$. Si $y=x$, todas las ocurrencias de término $x$ de la matriz quedan bajo un cuantificador homónimo y, por tanto, **ninguna** es libre en la fórmula completa: la condición de ocurrencias es vacía y coincide con la primera rama de la definición. Si $y\ne x$, las ocurrencias libres de $x$ en $\varphi$ son exactamente las libres de $x$ en $\psi$, según [TLOG-MTH-00016](#tlog-mth-00016). A sus ancestros en $\psi$ se añade el cuantificador exterior $Qy$. Por hipótesis inductiva, los ancestros interiores son inocuos si y sólo si $\operatorname{FreeFor}_\tau(t,x,\psi)$, y el nuevo ancestro lo es si y sólo si no existe una ocurrencia libre de $x$ en $\psi$ o $y\notin\operatorname{Var}_\tau(t)$. Ésa es exactamente la segunda rama de §6.19. $\square$

Para la primera consecuencia no existen ocurrencias libres de $x$ y el criterio es vacío. Para la segunda, toda ocurrencia libre de $x$ carece de cuantificadores ancestrales homónimos $x$, de modo que ninguno declara una variable del conjunto $\operatorname{Var}_\tau(x)=\{x\}$. $\square$

## 6.21. Sustitución literal segura de fórmulas

### Definición 6.21.1 — Sustitución literal bajo la condición «libre para» {#tlog-def-00035}

Para una triple $(\varphi,x,t)$ que satisfaga $\operatorname{FreeFor}_\tau(t,x,\varphi)$, definimos $\varphi[t/x]_{\mathrm{lit}}$ como la fórmula que sustituye **simultáneamente** las ocurrencias libres de $x$ por copias intactas del término $t$, sin sustituir de nuevo dentro de esas copias y sin modificar nombres de cuantificadores. En los átomos se aplica a cada término la sustitución $\sigma_{x,t}$ del §6.13, donde $\sigma_{x,t}(x)=t$ y $\sigma_{x,t}(z)=z$ para $z\ne x$. Negación y conectivos binarios se reconstruyen a partir de los resultados en sus componentes. Finalmente,

$$
(Qy\,\psi)[t/x]_{\mathrm{lit}}
:=\begin{cases}
Qx\,\psi,&y=x,\\
Qy\,\bigl(\psi[t/x]_{\mathrm{lit}}\bigr),&y\ne x.
\end{cases}
$$

La segunda rama sólo se usa en el dominio seguro de la definición. En cada aplicación del caso $y\ne x$, §6.19 asegura que la matriz también pertenece a ese dominio. Por inducción sobre el rango de las fórmulas, existe una única fórmula en cada triple admitida. La cláusula $y=x$ no atraviesa el cuantificador, aunque $x$ figure en su matriz como hoja de término.

La escritura $\varphi[t/x]$ **sin subíndice** se admite en este capítulo únicamente como abreviación de $\varphi[t/x]_{\mathrm{lit}}$ cuando se ha declarado o demostrado que $t$ es libre para $x$ en $\varphi$. Fuera de ese dominio no denota aquí una sustitución literal autorizada. La sustitución total por renombrado tendrá otro símbolo (§6.25).

## 6.22. Variables libres después de una sustitución segura

### Lema 6.22.1 — Fórmula exacta del soporte libre {#tlog-lem-00014}

Si $\operatorname{FreeFor}_\tau(t,x,\varphi)$, entonces

$$
\boxed{\operatorname{FV}_\tau(\varphi[t/x]_{\mathrm{lit}})
=\bigl(\operatorname{FV}_\tau(\varphi)\setminus\{x\}\bigr)
\cup
\begin{cases}
\operatorname{Var}_\tau(t),&x\in\operatorname{FV}_\tau(\varphi),\\
\varnothing,&x\notin\operatorname{FV}_\tau(\varphi).
\end{cases}}
$$

#### Demostración

Procedemos por inducción sobre la fórmula. En los átomos todas las variables son libres y la tesis resulta de las cláusulas de $\sigma_{x,t}$ y de la identidad exacta de [TLOG-LEM-00012](#tlog-lem-00012), aplicadas a sus términos argumentos. La negación no modifica $\operatorname{FV}$. Para una fórmula binaria, la unión de los conjuntos resultantes de sus dos ramas coincide con el miembro derecho: se incorpora $\operatorname{Var}(t)$ precisamente cuando al menos una rama tenía $x$ libre.

Sea $\varphi=Qy\,\psi$. Si $y=x$, §6.21 deja intacta la fórmula completa y $x\notin\operatorname{FV}_\tau(Qx\,\psi)$; la igualdad es inmediata. Si $y\ne x$, aplicamos la hipótesis inductiva a $\psi$. Cuando $x\notin\operatorname{FV}_\tau(\psi)$, la sustitución no afecta las hojas libres y no aparece una copia de $t$. Cuando $x\in\operatorname{FV}_\tau(\psi)$, la seguridad de §6.19 exige $y\notin\operatorname{Var}_\tau(t)$. En cualquiera de los casos, eliminar $y$ al formar $Qy$ conmuta con la eliminación de $x$ y no elimina ninguna variable libre introducida por $t$. Se obtiene exactamente la igualdad enunciada para $Qy\,\psi$. $\square$

De manera particular, si $x\notin\operatorname{FV}_\tau(\varphi)$, la sustitución literal está definida y $\varphi[t/x]_{\mathrm{lit}}=\varphi$, por inducción sobre las cláusulas de §6.21. Esta identidad es **literal**, no una declaración de equivalencia lógica.

## 6.23. Renombrado ligado y equivalencia alfa

### Definición 6.23.1 — Paso alfa elemental y clausura contextual {#tlog-def-00036}

Sea $Qx\,\psi$ una fórmula cuantificada y elijamos $y\in X$ con $y\notin\operatorname{Names}_\tau(\psi)\cup\{x\}$. La variable $y$ no aparece en ninguna hoja de término ni en ningún declarador de $\psi$. Por el criterio de §6.20, $y$ es libre para $x$ en $\psi$. Autorizamos entonces el **paso de renombrado ligado**

$$
\boxed{Qx\,\psi\quad\rightsquigarrow_\alpha\quad Qy\,\bigl(\psi[y/x]_{\mathrm{lit}}\bigr).}
$$

Este paso cambia la declaración del cuantificador exterior y, **sólo** dentro de su matriz, las ocurrencias de término de $x$ que eran libres en $\psi$; no cambia las apariciones de $x$ ligadas por cuantificadores homónimos interiores. La exigencia fuerte de frescura evita que una declaración de $y$ situada dentro de la matriz capture las nuevas hojas $y$. Ambos cuantificadores primitivos $\forall$ y $\exists$ obedecen idéntica regla.

Un **paso alfa contextual** reemplaza una única subfórmula cuantificada de la forma anterior en cualquier dirección de un árbol de fórmula, dejando iguales los demás nodos. Definimos $\varphi\equiv_\alpha\chi$ si existe una cadena **finita** de fórmulas desde $\varphi$ hasta $\chi$ en la que cada par consecutivo está relacionado por un paso alfa contextual en uno u otro sentido. Se permite la cadena de longitud cero. Por construcción, $\equiv_\alpha$ es una relación **reflexiva, simétrica y transitiva** y es una congruencia respecto de todos los constructores de fórmula. No es igualdad literal de expresiones ni se le atribuye aún equivalencia semántica, que exige la teoría de modelos de los capítulos posteriores.

::: {.callout-important}
## Firmeza de la condición de frescura

En una matriz $\psi=\forall y\,P(x)$, el nombre $y$ no está libre, pero sí aparece como **declarador**. Sustituir ingenuamente $x$ por $y$ produciría captura. Por eso la condición $y\notin\operatorname{FV}(\psi)$ es demasiado débil para **este paso literal**; aquí exigimos $y\notin\operatorname{Names}(\psi)$.
:::

## 6.24. Lo que conserva el renombrado alfa

### Proposición 6.24.1 — Conservación de variables libres y rango {#tlog-pro-00007}

Si $\varphi\equiv_\alpha\chi$, entonces

$$
\operatorname{FV}_\tau(\varphi)=\operatorname{FV}_\tau(\chi),
\qquad
\operatorname{rk}_\tau(\varphi)=\operatorname{rk}_\tau(\chi).
$$

#### Demostración

Basta examinar un paso alfa elemental. Para $y\notin\operatorname{Names}(\psi)\cup\{x\}$, la fórmula de §6.22, con término sustituyente igual a la variable $y$, da

$$
\operatorname{FV}_\tau(\psi[y/x]_{\mathrm{lit}})
=(\operatorname{FV}_\tau(\psi)\setminus\{x\})\cup E,
$$

donde $E=\{y\}$ si $x$ era libre en $\psi$, y $E=\varnothing$ en caso contrario. Como $y\notin\operatorname{FV}_\tau(\psi)$, al aplicar el cuantificador exterior $Qy$ y eliminar $y$ se obtiene

$$
\operatorname{FV}_\tau(Qy\,\psi[y/x]_{\mathrm{lit}})
=\operatorname{FV}_\tau(\psi)\setminus\{x\}
=\operatorname{FV}_\tau(Qx\,\psi).
$$

El reemplazo de una hoja variable por otra hoja variable no altera el número ni las posiciones de constructores de fórmula; tampoco modifica un paso de cuantificación, por lo que el rango sintáctico se conserva. En un **contexto** de fórmula, las ecuaciones de [TLOG-MTH-00016](#tlog-mth-00016) muestran que si dos subfórmulas tienen el mismo conjunto de variables libres, el mismo vale para los árboles completos; las ecuaciones de rango del §5.16 dan la conclusión paralela para $\operatorname{rk}$. La simetría de los pasos y la transitividad de una cadena finita conservan ambas identidades. $\square$

**Advertencia:** no concluimos que $\operatorname{Names}_\tau(\varphi)=\operatorname{Names}_\tau(\chi)$: precisamente el renombrado cambia nombres declarados. Tampoco se ha construido todavía la satisfacción en estructuras; la identidad de $\operatorname{FV}$ es una afirmación sintáctica, no una prueba de equivalencia lógica.

## 6.25. Sustitución total sin captura mediante nombres frescos

### Metateorema 6.25.1 — Existencia y unicidad de la sustitución canónica con prevención de captura {#tlog-mth-00019}

Para cada $x\in X$ y $t\in\operatorname{Tm}_\tau$ existe una **única** transformación determinada por las cláusulas siguientes,

$$
\operatorname{CA}_{x,t}:\operatorname{Fm}_\tau\longrightarrow\operatorname{Fm}_\tau,
$$

que realiza el reemplazo de las ocurrencias libres de $x$ por $t$, **renombrando antes** cualquier cuantificador que pudiera capturar una variable del término insertado. Las cláusulas son las siguientes:

1. En los átomos, aplicar a los términos argumentos $\sigma_{x,t}$ del §6.13.
2. En negación y en los cuatro conectivos binarios, aplicar $\operatorname{CA}_{x,t}$ a cada componente y reconstruir el constructor original.
3. Para $Qy\,\psi$, usar exactamente:

$$
\operatorname{CA}_{x,t}(Qy\,\psi)=
\begin{cases}
Qy\,\psi,&y=x\ \text{o}\ x\notin\operatorname{FV}_\tau(\psi),\\[2pt]
Qy\,\operatorname{CA}_{x,t}(\psi),&y\ne x,\ x\in\operatorname{FV}_\tau(\psi),\ y\notin\operatorname{Var}_\tau(t),\\[2pt]
Qz\,\operatorname{CA}_{x,t}(\psi[z/y]_{\mathrm{lit}}),&y\ne x,\ x\in\operatorname{FV}_\tau(\psi),\ y\in\operatorname{Var}_\tau(t),
\end{cases}
$$

siendo en la tercera rama

$$
z:=\operatorname{fresh}\bigl(\operatorname{Names}_\tau(\psi)\cup\operatorname{Var}_\tau(t)\cup\{x,y\}\bigr).
$$

Como $z\notin\operatorname{Names}_\tau(\psi)\cup\{y\}$, la expresión $\psi[z/y]_{\mathrm{lit}}$ está definida y realiza el paso alfa de §6.23. La elección de $z$ es **determinista** y no exige AC. La condición adicional $z\notin\operatorname{Var}(t)$ impide que el nuevo cuantificador capture hojas de $t$. En la primera rama no se toca la fórmula cuando no hay ninguna ocurrencia libre de $x$ que deba sustituirse en ella.

La transformación satisface, para toda fórmula $\varphi$:

$$
\boxed{\operatorname{FV}_\tau(\operatorname{CA}_{x,t}(\varphi))
=(\operatorname{FV}_\tau(\varphi)\setminus\{x\})
\cup
\begin{cases}
\operatorname{Var}_\tau(t),&x\in\operatorname{FV}_\tau(\varphi),\\
\varnothing,&x\notin\operatorname{FV}_\tau(\varphi).
\end{cases}}
$$

Asimismo, si $\operatorname{FreeFor}_\tau(t,x,\varphi)$, entonces la transformación coincide **literalmente** con la sustitución segura del §6.21:

$$
\operatorname{CA}_{x,t}(\varphi)=\varphi[t/x]_{\mathrm{lit}}.
$$

#### Demostración

**Existencia.** Recurrimos por inducción ordinaria sobre el rango $\operatorname{rk}_\tau(\varphi)$. Los casos atómico y de conectivos son inmediatos a partir de §6.13 y de las cláusulas de reconstrucción. En el caso $Qy\,\psi$, las tres condiciones anteriores son exhaustivas y mutuamente excluyentes. Las dos primeras ramas terminan en la fórmula dada o piden el valor de la función sobre la subfórmula estrictamente menor $\psi$. En la última rama, primero se elige el único $z$ fresco de §6.18 y se forma $\psi'=\psi[z/y]_{\mathrm{lit}}$. Este renombrado reemplaza variables por variables y conserva el rango de $\psi$:

$$
\operatorname{rk}_\tau(\psi')=\operatorname{rk}_\tau(\psi)
<\operatorname{rk}_\tau(Qy\,\psi).
$$

La hipótesis de inducción ya define $\operatorname{CA}_{x,t}(\psi')$. Así se obtiene siempre una fórmula y termina la construcción, aun en presencia de cuantificadores homónimos anidados. Para formalizar la función como **conjunto**, en cada etapa de rango definimos su gráfico sobre las fórmulas de rango acotado, usando reemplazo en ZF. Las definiciones coinciden en los niveles comunes porque el caso de un constructor depende únicamente de valores de rango estrictamente menor. La unión de los gráficos es una función de $\operatorname{Fm}_\tau$ en sí mismo. No se necesita numerar los símbolos de la signatura.

**Unicidad.** En un átomo, las cláusulas obligan a aplicar una sustitución de términos ya única. Los demás casos están determinados por el constructor y las condiciones booleanas expresadas en ellos. En la última rama el conjunto prohibido es finito y el mínimo índice fresco es único; la matriz renombrada está fijada por §6.21. La inducción sobre el rango impone el mismo resultado en todos los argumentos recursivos. No pueden existir dos funciones diferentes que cumplan las cláusulas.

**Soporte libre.** Inducimos otra vez sobre el rango. Los casos atómicos y proposicionales siguen la demostración de [TLOG-LEM-00014](#tlog-lem-00014). En $Qy\,\psi$, si $y=x$ o $x\notin\operatorname{FV}(\psi)$, la primera rama no altera la fórmula y la identidad es inmediata. Si $y\ne x$, $x$ es libre en $\psi$, y $y\notin\operatorname{Var}(t)$, aplicamos la hipótesis inductiva a la matriz y eliminamos $y$; como $y\ne x$ y $y\notin\operatorname{Var}(t)$, el resultado es

$$
(\operatorname{FV}(\psi)\setminus\{x,y\})\cup\operatorname{Var}(t),
$$

que es el miembro derecho para la fórmula cuantificada.

En la tercera rama $y\in\operatorname{Var}(t)$, elegimos $z$ fresco. Por [TLOG-LEM-00014](#tlog-lem-00014), $\operatorname{FV}(\psi')=(\operatorname{FV}(\psi)\setminus\{y\})\cup E_z$, con $E_z=\{z\}$ exactamente cuando $y\in\operatorname{FV}(\psi)$. Además $x\ne y$, $z\ne x$ y $x\in\operatorname{FV}(\psi')$. La hipótesis inductiva da

$$
\operatorname{FV}(\operatorname{CA}_{x,t}(\psi'))
=(\operatorname{FV}(\psi')\setminus\{x\})\cup\operatorname{Var}(t).
$$

Al reconstruir $Qz$ se elimina $z$, y como $z\notin\operatorname{Var}(t)$, queda otra vez $(\operatorname{FV}(\psi)\setminus\{x,y\})\cup\operatorname{Var}(t)$. Éste es exactamente el miembro derecho para $Qy\,\psi$, pues $x\in\operatorname{FV}(\psi)$ y $x\ne y$. En particular, ninguna variable nueva del término $t$ queda ligada por el cuantificador introducido.

**Coincidencia con la sustitución segura.** Si $\operatorname{FreeFor}(t,x,\varphi)$, una inducción estructural compara las cláusulas de §6.21 con las de este teorema. En el caso $Qy\,\psi$, si $y=x$, ambas dejan intacta la fórmula; si $y\ne x$ y $x\notin\operatorname{FV}(\psi)$, las dos dan también la misma fórmula. En el caso restante, el predicado `FreeFor` obliga a $y\notin\operatorname{Var}(t)$ y a la seguridad en la matriz: ambas operaciones reconstruyen $Qy$ a partir de la misma sustitución, por hipótesis inductiva. Por ello **nunca** se activa la rama de renombrado fresco cuando la sustitución literal estaba permitida. $\square$

La elección determinista del nombre fresco proporciona **unicidad literal de esta implementación**. La teoría de equivalencia alfa permite estudiar otras elecciones de nombres; en este microtramo no se afirma aún que todas las políticas de renombrado produzcan fórmulas alfa-equivalentes, ni una ley general de composición de sustituciones de fórmulas. Ambas cuestiones requieren un control adicional en `M04`.

## 6.26. Cuatro situaciones que no deben confundirse

**Captura evitada.** En una signatura con $P\in R_1$, tómese $\varphi=\forall x_0(P(x_1))$ y $t=x_0$, $x=x_1$. La sustitución literal no está permitida: la ocurrencia libre de $x_1$ se encuentra bajo el cuantificador $\forall x_0$, y $x_0\in\operatorname{Var}(t)$. La operación $\operatorname{CA}_{x_1,x_0}$ elige el primer $x_k$ fresco distinto de $x_0,x_1$, aquí $x_2$, y da

$$
\operatorname{CA}_{x_1,x_0}(\forall x_0 P(x_1))=\forall x_2 P(x_0).
$$

La variable $x_0$ **permanece libre**, como exige el teorema 6.25.1.

**Sombra de un cuantificador homónimo.** Sea $\varphi=\forall x_0\,\exists x_0 P(x_0)$. Para cualquier término $t$, $\operatorname{CA}_{x_0,t}(\varphi)=\varphi$: no existen ocurrencias libres de $x_0$. No se renombra ni se sustituye el $x_0$ ligado del predicado.

**Coexistencia de ocurrencias.** En $\varphi=(\forall x_0 P(x_0))\land P(x_0)$, sustituir $x_0$ por $x_1$ en el sentido de $\operatorname{CA}_{x_0,x_1}$ sólo afecta la rama derecha, de modo que se obtiene $(\forall x_0P(x_0))\land P(x_1)$. La ocurrencia ligada de la rama izquierda permanece idéntica.

**Renombrado y literalidad.** $\forall x_0P(x_0)$ y $\forall x_2P(x_2)$ son fórmulas **distintas como secuencias de tokens**, relacionadas por un paso alfa si $x_2$ es fresco en la matriz. Ningún resultado de este capítulo convierte su relación $\equiv_\alpha$ en igualdad metateórica.

## 6.27. Frontera y estado de `M03`

El tercer bloque define un predicado preciso de libertad para sustituir, prueba su equivalencia con el criterio por ocurrencias, construye la sustitución literal **sólo cuando es segura**, caracteriza su conjunto de variables libres, formaliza los pasos de renombrado alfa y una equivalencia alfa sintáctica, y demuestra una operación **total y determinista** de sustitución individual que evita captura mediante nombres frescos. Todo se fundamenta en árboles y rangos finitos dentro de $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ sin elección silenciosa. No se ha introducido satisfacción, validez ni derivabilidad de primer orden.

```text
TLOG-CH06-M01 = CLOSED / PASS
TLOG-CH06-M02 = CLOSED / PASS
TLOG-CH06-M03 = CLOSED / PASS
TLOG-CH06-0001 = PARTIAL-CLOSURE / NOT CLOSED
new mathematical nodes = 8
chapter 6 closed nodes = 21
TLOG registered/closed nodes = 90/90
DAG = 90 nodes / 208 direct edges / PASS
external interfaces = 0
formalization candidates = 25
compiled/verified = 0
chapters closed = 6/24
PART I = CLOSED / PASS
PART II = OPEN
```

**Siguiente microtramo:** `TLOG-CH06-M04 — Compatibilidad de equivalencia alfa y sustituciones; leyes de composición y cierre sintáctico del capítulo`.
## 6.28. Representación sintáctica sin nombres de variables ligadas

### Definición 6.28.1 — Código por profundidad del vinculante {#tlog-def-00037}

Para comparar fórmulas sin depender de la elección de los nombres ligados introducimos un **código puramente sintáctico**. Los términos codificados conservan cada símbolo funcional de $\tau$ y reemplazan una hoja variable por uno de dos constructores *metateóricos* disjuntos:

$$
\mathtt{F}(x)\quad(x\in X),\qquad
\mathtt{B}(j)\quad(j\in\omega).
$$

El primero expresa un nombre **libre**; el segundo expresa una aparición **ligada** al cuantificador situado a distancia $j$ entre los cuantificadores ancestros, contada desde el más próximo (índice cero). No se incorporan estos dos constructores al lenguaje objeto: son etiquetas de árboles en la metateoría $\mathsf M_{\mathrm{ext}}$. Las aplicaciones de función preservan su aridad, incluso $n=0$; los átomos preservan su símbolo relacional o igualdad lógica; la negación y los cuatro conectivos binarios preservan su constructor; cada cuantificador conserva $Q\in\{\forall,\exists\}$, pero **omite el nombre declarado**.

Formalmente, dada una lista finita $\Delta=(y_0,\ldots,y_{m-1})$ de declaraciones ancestro, de la más interior a la más exterior, codificamos una hoja $x$ por $\mathtt{B}(j)$ si $j<m$ es el menor índice con $y_j=x$, y por $\mathtt{F}(x)$ si no existe tal índice. El resto de los constructores se codifica componente a componente. En un cuantificador $Qy\,\psi$, suprimimos el nombre $y$ del constructor codificado y procesamos la matriz con la lista $(y)\mathbin{\frown}\Delta$. Escribimos $\operatorname{db}_\Delta(\varphi)$ para el resultado y fijamos

$$
\boxed{\operatorname{db}_\tau(\varphi):=\operatorname{db}_{()}(\varphi).}
$$

El código es un árbol finito con todas las referencias $\mathtt{B}(j)$ **bien situadas**: en una hoja con $d$ cuantificadores antecesores se tiene $j<d$. Un código de término tomado aisladamente utiliza solamente $\mathtt{F}(x)$, pues no posee cuantificadores ancestros. El conjunto de todos estos árboles codificados se obtiene mediante formación de árboles finitos sobre conjuntos de etiquetas y separación en ZF. La función $\operatorname{db}_\tau$ es única por el árbol legible unívocamente de §5.14 y el cuantificador homónimo más próximo de §6.3. **No** es una numeración de Gödel ni una codificación efectiva; esas nociones continúan diferidas a la Parte IV.

## 6.29. Caracterización exacta de la equivalencia alfa

### Metateorema 6.29.1 — Renombrado alfa si y sólo si coincide el código {#tlog-mth-00020}

Para cualesquiera fórmulas $\varphi,\chi\in\operatorname{Fm}_\tau$,

$$
\boxed{\varphi\equiv_\alpha\chi
\quad\Longleftrightarrow\quad
\operatorname{db}_\tau(\varphi)=\operatorname{db}_\tau(\chi).}
$$

#### Demostración

**Dirección directa.** En un paso alfa elemental de §6.23, $Qx\,\psi\rightsquigarrow_\alpha Qy\,\psi[y/x]_{\mathrm{lit}}$, el nuevo nombre $y$ no aparece en la matriz anterior. Las hojas que tenían como vinculante el cuantificador exterior pasan a llevar el nombre $y$, pero siguen teniendo **exactamente ese vinculante a la misma distancia**; las hojas vinculadas por cuantificadores interiores y las libres permanecen clasificadas del mismo modo. Por tanto, todas las etiquetas $\mathtt{B}(j)$ y $\mathtt{F}(z)$ se conservan en sus respectivas posiciones; también se conservan los operadores y aridades. El mismo razonamiento vale en cualquier contexto: la sustitución del subárbol por otro con las mismas referencias relativas a su propio alcance no altera la distancia de los vinculantes externos. Cada paso contextual preserva $\operatorname{db}$, y la igualdad se propaga a cadenas finitas, incluidas las inversas.

**Dirección inversa.** Supongamos iguales los códigos. En particular, ambas fórmulas tienen idénticos constructores, posiciones atómicas, símbolos extralógicos y árbol de cuantificadores **sin nombres**. Sea $h\in\omega$ el máximo número de cuantificadores estrictamente ancestrales de cualquier nodo cuantificador en ambos árboles ($h=0$ si no hay cuantificadores). El conjunto $A=\operatorname{Names}_\tau(\varphi)\cup\operatorname{Names}_\tau(\chi)$ es finito. Elegimos, en orden creciente, $h+1$ variables diferentes $z_0,\ldots,z_h$ fuera de $A$. Esta selección finita es determinada por el orden fijo $X=\{x_i\}$, sin elección.

Transformamos cada fórmula **desde la raíz hacia las matrices**, recorriendo sus cuantificadores por profundidad. En profundidad $d$, renombramos su declarador como $z_d$, mediante el paso contextual autorizado de §6.23. El paso es legítimo: $z_d$ no figuraba en las fórmulas originales y tampoco ha sido introducido a profundidades menores, porque $z_d\ne z_e$ para $e<d$. Por tanto, $z_d$ no aparece en la matriz que va a renombrarse. La sustitución literal cambia únicamente las hojas ligadas por la declaración reemplazada, respetando las ocultaciones por cuantificadores homónimos interiores. Tras finitos pasos, toda declaración a profundidad $d$ tiene nombre $z_d$. El árbol resultante depende **únicamente** del código: una hoja $\mathtt{B}(j)$, situada bajo $d$ cuantificadores, recibe el nombre $z_{d-1-j}$, mientras que $\mathtt{F}(x)$ sigue siendo $x$. Como los códigos iniciales coinciden, las dos formas renombradas son la **misma fórmula literal**. Cada original está relacionada con esa forma por una cadena alfa finita; la simetría y transitividad de §6.23 concluyen $\varphi\equiv_\alpha\chi$. $\square$

Esta prueba proporciona un criterio **combinatorio**, no semántico, para la equivalencia alfa. La expresión «sin nombres» describe sólo las variables *ligadas*: los nombres libres se conservan literalmente en el código.

## 6.30. Sustitución simultánea de fórmulas, con prevención de captura

### Definición 6.30.1 — Extensión total de una sustitución global {#tlog-def-00038}

Sea $\sigma:X\to\operatorname{Tm}_\tau$ una sustitución **arbitraria** —no es necesario que tenga soporte finito—. Definimos una operación sobre fórmulas $\mathcal S_\sigma:\operatorname{Fm}_\tau\to\operatorname{Fm}_\tau$. En un átomo aplicamos la extensión de términos del §6.13 a todos sus argumentos. Negación y conectivos binarios preservan el constructor y aplican $\mathcal S_\sigma$ a sus subfórmulas. Para una fórmula cuantificada $Qy\,\psi$, ponemos

$$
C_\sigma(\psi;y):=
\bigcup_{u\in\operatorname{FV}_\tau(\psi)\setminus\{y\}}
\operatorname{Var}_\tau(\sigma(u)),
\qquad
\sigma_{[v]}(w):=
\begin{cases}v,&w=v,\\\sigma(w),&w\ne v.\end{cases}
$$

La unión $C_\sigma(\psi;y)$ es finita aunque $\sigma$ tenga soporte infinito, porque $\operatorname{FV}_\tau(\psi)$ es finito y la imagen de cada variable es un término finito. Las cláusulas cuantificadas son

$$
\boxed{
\mathcal S_\sigma(Qy\,\psi)=
\begin{cases}
Qy\,\mathcal S_{\sigma_{[y]}}(\psi),
& y\notin C_\sigma(\psi;y),\\[3pt]
Qz\,\mathcal S_{\sigma_{[z]}}\bigl(\psi[z/y]_{\mathrm{lit}}\bigr),
& y\in C_\sigma(\psi;y),
\end{cases}}
$$

con

$$
z:=\operatorname{fresh}\bigl(
\operatorname{Names}_\tau(\psi)\cup C_\sigma(\psi;y)\cup\{y\}
\bigr)
$$

en la segunda rama. Allí $z\notin\operatorname{Names}_\tau(\psi)$, de modo que $\psi[z/y]_{\mathrm{lit}}$ está bien definida y realiza un paso alfa del cuantificador. Además $z\notin C_\sigma(\psi;y)$: ninguna variable introducida al sustituir las ocurrencias que eran libres bajo $Qy$ será capturada por el nuevo $Qz$. En **ambas** ramas, $\sigma_{[v]}$ protege las hojas originalmente vinculadas al cuantificador de nombre $v$; jamás se sustituye otra vez dentro de un término ya insertado.

La existencia de $\mathcal S_\sigma$ se obtiene por recursión sobre el **rango** de fórmula, exactamente como en §6.25. En la rama de renombrado, $\psi[z/y]_{\mathrm{lit}}$ tiene el mismo rango que $\psi$, estrictamente menor que el de $Qy\psi$. Las cláusulas son excluyentes y el $z$ fresco tiene un valor único; así se obtiene también unicidad **literal** de la transformación definida, incluso para signaturas arbitrarias y $\sigma$ de soporte infinito. Los grafos funcionales por rango y su unión existen en ZF. Ésta es una **definición**, no una equivalencia semántica de fórmulas.

## 6.31. Lema de transporte de ocurrencias, soporte y localidad

### Lema 6.31.1 — Conmutación con el código sin nombres {#tlog-lem-00015}

En un **término codificado**, definimos $D_\sigma$ reemplazando cada hoja $\mathtt{F}(x)$ por el árbol de término codificado de $\sigma(x)$, cuyas hojas son todas de tipo $\mathtt{F}$; dejamos intacta cada hoja $\mathtt{B}(j)$ y reconstruimos cada función con la misma aridad. Extendemos $D_\sigma$ a fórmulas codificadas preservando átomos, conectivos y cuantificadores **sin nombre**. Los nuevos árboles están bien situados, porque no se introducen marcadores $\mathtt{B}(j)$ nuevos. Entonces, para toda $\varphi\in\operatorname{Fm}_\tau$,

$$
\boxed{
\operatorname{db}_\tau\bigl(\mathcal S_\sigma(\varphi)\bigr)
=D_\sigma\bigl(\operatorname{db}_\tau(\varphi)\bigr).}
$$

Se obtienen, además, tres consecuencias:

$$
\boxed{
\operatorname{FV}_\tau(\mathcal S_\sigma(\varphi))
=\bigcup_{x\in\operatorname{FV}_\tau(\varphi)}
\operatorname{Var}_\tau(\sigma(x)),\qquad
\operatorname{rk}_\tau(\mathcal S_\sigma(\varphi))
=\operatorname{rk}_\tau(\varphi).}
$$

La operación es **literalmente local** en las variables libres: si $\sigma(x)=\rho(x)$ para todo $x\in\operatorname{FV}_\tau(\varphi)$, entonces $\mathcal S_\sigma(\varphi)=\mathcal S_\rho(\varphi)$. Finalmente, para la sustitución simple $\sigma_{x,t}$ de §6.13,

$$
\boxed{\mathcal S_{\sigma_{x,t}}(\varphi)
=\operatorname{CA}_{x,t}(\varphi)}
$$

**como igualdad literal**, con la implementación determinista de §6.25.

#### Demostración

Probamos por inducción sobre el rango una afirmación **más fina que la igualdad de códigos**: cada hoja de término originalmente **ligada** sigue vinculada, después de transformar la fórmula, al cuantificador correspondiente y a la **misma distancia en su cadena de ancestros**; cada hoja originalmente libre $x$ se sustituye por una copia del término $\sigma(x)$, cuyas hojas son todas **libres**, sin efectuar reemplazos secundarios dentro de la copia. Ningún constructor lógico ni posición de argumento funcional o relacional cambia.

En los átomos, todas las hojas eran libres y la afirmación es exactamente la sustitución de términos del §6.13. Negación y los cuatro conectivos binarios no introducen vínculos y preservan las afirmaciones inductivas en sus ramas. Ante $Qy\,\psi$, las hojas de nombre $y$ libres en $\psi$ estaban vinculadas por ese cuantificador; por ello $\sigma_{[y]}(y)=y$. En la primera rama, la hipótesis $y\notin C_\sigma(\psi;y)$ impide capturar una hoja introducida por cualquiera de las demás imágenes activas. La inducción aplicada a la matriz preserva exactamente los vínculos de las hojas originales y la libertad de las nuevas. En la segunda rama se ejecuta primero el cambio alfa $Qy\psi\rightsquigarrow_\alpha Qz\psi[z/y]_{\mathrm{lit}}$, que **preserva la distancia de cada vinculante** por §6.29; la condición $z\notin C_\sigma(\psi;y)$ impide capturar las nuevas hojas. La inducción se aplica a la matriz renombrada, que tiene menor rango, con $\sigma_{[z]}(z)=z$. Ambas ramas prueban la correspondencia de ocurrencias y, por las cláusulas de §6.28, la igualdad con $D_\sigma$.

Las variables libres de un código son precisamente los nombres de sus hojas $\mathtt{F}$; $D_\sigma$ reemplaza esas hojas por términos con soporte $\operatorname{Var}(\sigma(x))$. Esto prueba la fórmula del soporte; la igualdad de rango sigue de la preservación de todos los constructores de fórmula. Para la **localidad literal**, hacemos una segunda inducción sobre el rango y suponemos que las dos sustituciones coinciden en $\operatorname{FV}(\varphi)$. En un átomo sus aplicaciones coinciden término a término. En un cuantificador $Qy\psi$, las imágenes relevantes para $C_\sigma(\psi;y)$ y $C_\rho(\psi;y)$ coinciden; así la rama elegida y, cuando proceda, la variable fresca $z$ son idénticas. Las sustituciones sobrescritas $\sigma_{[y]},\rho_{[y]}$ (o $\sigma_{[z]},\rho_{[z]}$) coinciden sobre las variables libres de la matriz correspondiente: sobre los nombres exteriores por hipótesis y sobre el declarador protegido por definición. La hipótesis inductiva concluye igualdad **literal** en las matrices y, por tanto, en la fórmula completa.

Para el caso simple $\sigma_{x,t}$, el único término no idéntico de su tabla es $t$ en $x$. Si $y=x$, el cuantificador queda protegido y no altera su matriz; si $y\ne x$ y $x\notin\operatorname{FV}(\psi)$, ambas operaciones son la identidad en esa rama. Si $x\in\operatorname{FV}(\psi)$, el test $y\in C_\sigma(\psi;y)$ equivale a $y\in\operatorname{Var}(t)$: las otras imágenes activas son variables que ya figuran en $\operatorname{Names}(\psi)$ y ninguna es $y$. En ese caso, el conjunto de nombres prohibidos para $\operatorname{fresh}$ coincide con el de §6.25, porque $x\in\operatorname{Names}(\psi)$. La inducción identifica las matrices transformadas; las cláusulas coinciden **token por token**. $\square$

::: {.callout-note}
## Alcance

La localidad literal depende de esta política concreta de elegir $\operatorname{fresh}$ sólo a partir de los nombres de la matriz y de las **imágenes activas**. No debe generalizarse sin prueba a una implementación que inspeccione el soporte infinito de $\sigma$, ni sustituirse por la afirmación de que cualquier política de frescura produce la misma cadena.
:::

## 6.32. Compatibilidad alfa e identidad

### Metateorema 6.32.1 — Descenso de la sustitución al cociente alfa {#tlog-mth-00021}

Para $\sigma:X\to\operatorname{Tm}_\tau$,

$$
\boxed{\varphi\equiv_\alpha\chi
\ \Longrightarrow\ 
\mathcal S_\sigma(\varphi)\equiv_\alpha
\mathcal S_\sigma(\chi).}
$$

La sustitución identidad $\iota(x)=x$ de §6.15 satisface, incluso **literalmente**,

$$
\boxed{\mathcal S_\iota(\varphi)=\varphi.}
$$

Asimismo, si $\varphi\in\operatorname{Sent}_\tau$, entonces $\mathcal S_\sigma(\varphi)=\varphi$ como fórmulas literales, para toda sustitución $\sigma$.

#### Demostración

Si $\varphi\equiv_\alpha\chi$, §6.29 da $\operatorname{db}(\varphi)=\operatorname{db}(\chi)$. Aplicamos $D_\sigma$ a ambos lados y, por §6.31, obtenemos

$$
\operatorname{db}(\mathcal S_\sigma\varphi)
=D_\sigma(\operatorname{db}\varphi)
=D_\sigma(\operatorname{db}\chi)
=\operatorname{db}(\mathcal S_\sigma\chi).
$$

La dirección inversa de §6.29 prueba la compatibilidad deseada. Para la identidad **literal**, inducimos sobre el rango de $\varphi$: en un átomo todos los términos quedan intactos, y los conectivos preservan la fórmula por hipótesis inductiva. Bajo $Qy\psi$, las imágenes activas por $\iota$ son exactamente las variables $u\in\operatorname{FV}(\psi)\setminus\{y\}$, ninguna de las cuales es $y$. Se elige la primera rama y $\iota_{[y]}=\iota$; por hipótesis, la matriz no cambia. Para una sentencia, aplicamos la localidad literal de §6.31: $\sigma$ y $\iota$ coinciden **vacuamente** sobre $\operatorname{FV}(\varphi)=\varnothing$. Concluimos $\mathcal S_\sigma\varphi=\mathcal S_\iota\varphi=\varphi$. $\square$

La compatibilidad **no** expresa igualdad literal entre las transformaciones de dos fórmulas alfa-equivalentes: las dos construcciones pueden escoger nombres nuevos diferentes. Ésa es precisamente la razón de trabajar con $\equiv_\alpha$.

## 6.33. Composición de sustituciones en fórmulas

### Metateorema 6.33.1 — Ley de composición módulo equivalencia alfa {#tlog-mth-00022}

Sean $\sigma,\rho:X\to\operatorname{Tm}_\tau$, con la composición de términos $\sigma\star\rho$ del §6.15, que **primero** aplica $\sigma$ y **después** $\rho$. Para toda fórmula $\varphi$,

$$
\boxed{
\mathcal S_\rho\bigl(\mathcal S_\sigma(\varphi)\bigr)
\ \equiv_\alpha\ 
\mathcal S_{\sigma\star\rho}(\varphi).}
$$

La identidad es, en general, una **equivalencia alfa**, no una igualdad literal de cadenas.

#### Demostración

Por §6.31, basta comparar los códigos de las dos fórmulas. Para todo código bien situado $c$, una inducción sobre el árbol codificado demuestra las igualdades **literales**

$$
D_\iota(c)=c,
\qquad
D_\rho(D_\sigma(c))=D_{\sigma\star\rho}(c).
$$

En una hoja ligada $\mathtt{B}(j)$, las tres operaciones son la identidad. En una hoja libre $\mathtt{F}(x)$, la segunda composición produce el código del término $(\sigma(x))^\rho$, que por [TLOG-PRO-00006](#tlog-pro-00006) es exactamente el código del término $(\sigma\star\rho)(x)$. Las funciones de aridad finita reconstruyen el mismo constructor a partir de la igualdad en todos sus argumentos, incluidos los casos nularios; los átomos y los cinco conectivos, así como ambos cuantificadores sin nombre, la heredan de sus componentes. Así queda probada la ecuación para todo código.

Por consiguiente,

$$
\begin{aligned}
\operatorname{db}_\tau(\mathcal S_\rho(\mathcal S_\sigma\varphi))
&=D_\rho(\operatorname{db}_\tau(\mathcal S_\sigma\varphi))\\
&=D_\rho(D_\sigma(\operatorname{db}_\tau\varphi))\\
&=D_{\sigma\star\rho}(\operatorname{db}_\tau\varphi)\\
&=\operatorname{db}_\tau(\mathcal S_{\sigma\star\rho}\varphi).
\end{aligned}
$$

El metateorema 6.29.1 transforma la igualdad de códigos en equivalencia alfa. No se ha empleado ninguna propiedad de verdad o de consecuencia semántica. $\square$

**Contracontrol de literalidad.** En una signatura con $P\in R_1$, sean $\varphi=\forall x_0P(x_1)$, $\sigma=\sigma_{x_1,x_0}$ y $\rho=\sigma_{x_0,x_2}$. Las cláusulas deterministas dan

$$
\begin{aligned}
\mathcal S_\sigma(\varphi)&=\forall x_2P(x_0),\\
\mathcal S_\rho(\mathcal S_\sigma(\varphi))&=\forall x_1P(x_2),\\
\mathcal S_{\sigma\star\rho}(\varphi)&=\forall x_0P(x_2).
\end{aligned}
$$

Las dos últimas expresiones **no son iguales literalmente**, pero sí están relacionadas por renombrado alfa (sus cuantificadores son vacuos y sus matrices idénticas). Esto demuestra por qué la conclusión del teorema no debe reforzarse indebidamente.

## 6.34. Estructura algebraica de las sustituciones y sus clases

### Corolario 6.34.1 — Acción derecha del monoide de sustituciones sobre clases alfa {#tlog-cor-00005}

Sea $\mathscr Q_\tau:=\operatorname{Fm}_\tau/{\equiv_\alpha}$ el **conjunto cociente** de fórmulas por la equivalencia alfa de §6.23. Su existencia en ZF resulta por separación sobre $\mathcal P(\operatorname{Fm}_\tau)$ y reemplazo. Para $\sigma\in\operatorname{Tm}_\tau^X$ definimos

$$
[\varphi]_\alpha\cdot\sigma
:=[\mathcal S_\sigma(\varphi)]_\alpha.
$$

Por el metateorema 6.32.1, la definición es independiente del representante elegido. Los metateoremas 6.32.1 y 6.33.1 demuestran las identidades

$$
\boxed{
[\varphi]_\alpha\cdot\iota=[\varphi]_\alpha,
\qquad
([\varphi]_\alpha\cdot\sigma)\cdot\rho
=[\varphi]_\alpha\cdot(\sigma\star\rho).}
$$

Como $(\operatorname{Tm}_\tau^X,\star,\iota)$ es un monoide por [TLOG-PRO-00006](#tlog-pro-00006), estas ecuaciones establecen una **acción derecha** de ese monoide sobre el conjunto $\mathscr Q_\tau$. También se preserva exactamente el soporte libre de una clase:

$$
\operatorname{FV}_\tau(\mathcal S_\sigma\varphi)
=\bigcup_{x\in\operatorname{FV}_\tau(\varphi)}\operatorname{Var}_\tau(\sigma(x)),
$$

puesto que $\operatorname{FV}$ es invariante bajo $\equiv_\alpha$ por §6.24. La construcción de este cociente **no** identifica fórmulas lógicamente equivalentes ni interpreta símbolos en estructuras: es una identificación puramente sintáctica de elecciones de nombres ligados.

## 6.35. Cierre sintáctico del Capítulo 6

La teoría desarrollada en este capítulo cumple ahora las obligaciones arquitectónicas del Capítulo 6: (i) ocurrencias y vinculantes cuantificadores con unicidad; (ii) variables libres, sentencias e inducción/recursión general; (iii) sustitución simultánea de términos y sus leyes; (iv) libertad para sustituir y prevención de captura; (v) renombrado alfa y caracterización independiente por códigos; (vi) sustitución total de fórmulas con localidad, compatibilidad alfa, identidad y composición **en el cociente adecuado**.

No se ha introducido semántica de primer orden, equivalencia lógica ni relación deductiva de primer orden. Por tanto, los resultados sintácticos se exportan al Capítulo 7 sin presuposiciones de modelos. El uso de $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}+$ lógica clásica no ha requerido elección global, cardinalidades de la signatura ni procedimientos efectivos para listar sus símbolos. El número natural usado como índice de vinculante **no** es una codificación aritmética de fórmulas.

```text
TLOG-CH06-M01 = CLOSED / PASS
TLOG-CH06-M02 = CLOSED / PASS
TLOG-CH06-M03 = CLOSED / PASS
TLOG-CH06-M04 = CLOSED / PASS
TLOG-CH06-0001 = CLOSED / PASS
new mathematical nodes = 7
chapter 6 closed nodes = 28
TLOG registered/closed nodes = 97/97
DAG = 97 nodes / 232 direct edges / PASS
external interfaces = 0
formalization candidates = 30
compiled/verified = 0
chapters closed = 7/24
PART I = CLOSED / PASS
PART II = OPEN
```

**Siguiente capítulo:** `TLOG-CH07-0001 — Estructuras, asignaciones e interpretación`, comenzando por universos no vacíos, interpretaciones de la signatura y evaluación de términos.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 5](capitulo-05.md) · [Capítulo 7 →](capitulo-07.md)


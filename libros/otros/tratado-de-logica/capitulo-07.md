---
title: Capítulo 7 — Estructuras, asignaciones e interpretación
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
content-id: MA-BCH-0209
content-type: book-chapter
source-id: TLOG-CH07-0001
prerequisites:
- MA-BCH-0207
- MA-BCH-0208
related:
- MA-BOK-0014
source-sha256: 2081523df8c14736b5619f301e03ea5df419f6494ada1612c17d0c3690db109e
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 6](capitulo-06.md) · [Capítulo 8 →](capitulo-08.md)

## 7.0. Objetivo, estratos y límites del primer microtramo

Los Capítulos 5 y 6 construyeron la **sintaxis** de los lenguajes unisortados de primer orden con igualdad: símbolos de una signatura arbitraria $\tau$, términos $\operatorname{Tm}_\tau$, fórmulas $\operatorname{Fm}_\tau$, variables libres y ligadas, recursión estructural, sustituciones de términos y sustitución de fórmulas con prevención de captura. El presente bloque **`TLOG-CH07-M01`** inicia la transición hacia la semántica, sin confundir todavía la *interpretación de un término* con la *satisfacción de una fórmula*.

Permanecemos en la metateoría externa $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ con lógica clásica, sin incorporar el axioma de elección. Una signatura $\tau=((F_n)_{n\in\omega},(R_n)_{n\in\omega})$ es un dato **conjuntista**, potencialmente no numerable. Por definición, los símbolos funcionales y relacionales están tipados por una **aridad natural finita**, las constantes son miembros de $F_0$ y se permiten símbolos relacionales nularios $R_0$. El signo de igualdad lógica $\doteq$ no pertenece a ninguna de estas familias: su condición de símbolo lógico ya está fijada por [TLOG-DEF-00025](capitulo-05.md#tlog-def-00025).

La construcción que sigue distinguirá, en orden, el **dominio no vacío** de una estructura, la interpretación de los símbolos extralógicos, una **asignación** de valores a las variables y la **evaluación única de términos**. Sólo el Capítulo 8 definirá $\mathfrak A,s\models\varphi$ y las reglas de los conectivos y cuantificadores. Aquí no se usa $\models$ como relación disponible del sistema `FOL=`.

### Fuentes efectivamente cotejadas

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, segunda edición (2001), cap. 2 §2.2, pp. **80–85**. Rol `proof-model / countercheck`: estructuras con universo no vacío, operaciones totales, constantes, asignaciones y extensión recursiva única de la evaluación de términos.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, tercera edición (2010), cap. 2 §2.3, pp. **62–63**. Rol `countercheck`: distinción estructura/asignación, evaluación de términos, interpretación funcional, dominio y actualización de variables.

Las convenciones de TLOG se reconstruyen de manera independiente: ambas fuentes admiten la representación ordinaria de firmas, pero **TLOG incluye expresamente** símbolos relacionales nularios y codifica las constantes como funciones nularias. El lema de sustitución de **términos** se prueba aquí dentro del sistema ya cerrado, y su enunciado no importa la futura teoría de satisfacción de fórmulas.

## 7.1. La frontera de interpretación

### Convención 7.1.1 — Símbolo, interpretación y verdad {#tlog-cnv-00009}

Para distinguir claramente el símbolo extralógico $f\in F_n$ de la operación conjuntista con que se lo interpreta, escribiremos $f^{\mathfrak A}$. Para $R\in R_n$ escribiremos $R^{\mathfrak A}$. Esta notación pertenece a la **metateoría**: la operación $f^{\mathfrak A}$ no es otro símbolo del lenguaje objeto, ni un nuevo término. Por su parte, la interpretación de una variable $x\in X$ dependerá de una asignación $s$, no de la signatura y no de una operación extralógica.

Reservamos $\llbracket t\rrbracket_{\mathfrak A,s}$ para el **valor de un término**. En esta etapa no se asigna a una fórmula arbitraria un valor de verdad, ni se define una relación de satisfacción. La igualdad lógica de fórmulas atómicas se mantiene como constructor $\operatorname{Eq}(t,u)$; su tratamiento semántico como **identidad de valores** se definirá sólo al abrir la evaluación de fórmulas, junto con la interpretación de predicados.

Una $\tau$-estructura y una asignación constituyen datos semánticos distintos. Aun si las denotaciones de los símbolos extralógicos están fijadas, una fórmula abierta o un término con variables puede depender de $s$. La palabra «modelo» se reservará preferentemente para la relación de satisfacción de una teoría, aún no construida.

## 7.2. Estructuras sobre una signatura

### Definición 7.2.1 — Estructura unisortada de signatura $\tau$ {#tlog-def-00039}

Una **estructura de signatura** $\tau$, o **$\tau$-estructura**, es una colección de datos

$$
\mathfrak A=\bigl(A,(f^{\mathfrak A})_{n\in\omega,\,f\in F_n},(R^{\mathfrak A})_{n\in\omega,\,R\in R_n}\bigr)
$$

que satisface las siguientes condiciones:

1. $A$ es un **conjunto no vacío** (universo o dominio de $\mathfrak A$);
2. para cada $f\in F_n$, su interpretación es una **función total** $f^{\mathfrak A}:A^n\longrightarrow A$;
3. para cada $R\in R_n$, su interpretación es una **relación n-aria**, es decir, $R^{\mathfrak A}\subseteq A^n$.

Se define $A^0:=\{()\}$, el conjunto cuyo único elemento es la tupla vacía. Por ello, una función nularia $f^{\mathfrak A}:A^0\to A$ determina exactamente un elemento $f^{\mathfrak A}(())\in A$, que es la **denotación de la constante** $f$. Por el contrario, una relación nularia sólo puede ser $R^{\mathfrak A}=\varnothing$ o $R^{\mathfrak A}=\{()\}$. Estos dos casos podrán interpretarse como los dos valores de verdad al definir satisfacción en el siguiente capítulo, pero **todavía no** son una aplicación de $\models$.

La interpretación de una operación de aridad positiva es total en el producto completo $A^n$; no se admiten funciones parciales en la presente noción. Las interpretaciones de dos símbolos **distintos** pueden coincidir extensionalmente. La estructura fija el universo y los valores de los símbolos extralógicos, pero **no** asigna interpretación arbitraria a la igualdad lógica, a los conectivos ni a los cuantificadores. Los símbolos de variables permanecen distintos de los elementos de $A$.

Para la teoría de tipos de las definiciones, una $\tau$-estructura individual es un **conjunto** representable mediante pares y funciones indexadas. No se utiliza la expresión «conjunto de todas las $\tau$-estructuras» sobre todos los universos: al variar libremente $A$, se habla de una **clase** definible en la metateoría, no de un conjunto obtenido automáticamente.

### Nota pedagógica — Por qué se exige $A\ne\varnothing$

El requisito de universo no vacío no es una propiedad deducida de las fórmulas; constituye una **convención semántica explícita** del sistema clásico de primer orden que TLOG está construyendo. Garantiza, entre otras cosas, la existencia de asignaciones totales $X\to A$ sin necesidad de introducir reglas especiales para cuantificadores sobre dominios vacíos. También es coherente con las funciones nularias: una signatura que contiene una constante no podría recibir su interpretación funcional en un universo vacío. No se está afirmando que todos los otros formalismos lógicos deban excluir universos vacíos.

## 7.3. Existencia de estructuras sin elección

### Proposición 7.3.1 — Una estructura sobre todo universo no vacío {#tlog-pro-00008}

**Enunciado.** Sea $\tau$ una signatura arbitraria y $A\ne\varnothing$ un conjunto. Existe al menos una $\tau$-estructura de universo **exactamente** $A$. En particular, toda signatura admite una estructura con universo unitario. La existencia se demuestra en $\mathrm{ZF}$, sin axioma de elección, incluso cuando $\tau$ tenga un conjunto no numerable de símbolos.

**Demostración.** Fijemos **un solo** elemento $a_0\in A$, cuya existencia proviene de $A\ne\varnothing$. Para cada $n\in\omega$ y cada $f\in F_n$ definimos

$$
f^{\mathfrak A}(\mathbf a):=a_0\qquad(\mathbf a\in A^n).
$$

Se trata de una aplicación total, también para $n=0$ cuando $\mathbf a=()$. Para cada $n\in\omega$ y $R\in R_n$ ponemos $R^{\mathfrak A}:=\varnothing\subseteq A^n$. La asignación **uniforme** $f\mapsto(A^n\times\{a_0\})$, con el gráfico funcional pertinente, y la asignación $R\mapsto\varnothing$ definen familias indexadas mediante separación y reemplazo en ZF. En particular no hemos elegido independientemente valores para cada símbolo: hemos utilizado el **mismo** $a_0$ para todas las funciones. Son exactamente los datos exigidos en §7.2. Para obtener un universo unitario podemos tomar $A=\{\varnothing\}$ y $a_0=\varnothing$. $\square$

No se infiere que cualquier familia **preasignada** de valores en conjuntos distintos admita una selección simultánea sin elección; la prueba sólo establece que la estructura que acabamos de definir existe **por una regla uniforme**. Ésta es la distinción fundacional relevante.

## 7.4. Asignaciones de variables

### Definición 7.4.1 — Asignación total y modificación puntual {#tlog-def-00040}

Sea $\mathfrak A$ una estructura con universo $A$. Una **asignación de variables individuales** es una aplicación total

$$
s:X\longrightarrow A.
$$

El conjunto de todas las asignaciones a ese universo fijo es $A^X$, bien definido en ZF. Puesto que $A\ne\varnothing$, existe al menos una asignación: para $a_0\in A$, basta $s(x)=a_0$ para todo $x\in X$. No se presupone una correspondencia biunívoca entre $X$ y $A$, ni que toda variable denote un elemento distinto.

Para $x\in X$ y $a\in A$ definimos la **actualización puntual** $s[x\mapsto a]:X\to A$ por

$$
\boxed{\bigl(s[x\mapsto a]\bigr)(y)=
\begin{cases}
a,&y=x,\\
s(y),&y\ne x.
\end{cases}}
$$

La asignación modificada conserva todos los valores anteriores salvo, eventualmente, el de $x$. Es una operación **metateórica sobre funciones** y no una sustitución sintáctica de variables por términos. En particular, $s[x\mapsto a]$ no es una expresión de $\operatorname{Tm}_\tau$. La notación fijada en el registro de TLOG para modificaciones de asignaciones adquiere así un dominio y un codominio precisos.

## 7.5. Cálculo elemental de modificaciones

### Lema 7.5.1 — Leyes de actualización de asignaciones {#tlog-lem-00016}

Para cualquier asignación $s:X\to A$, variables $x,y\in X$ y valores $a,b\in A$:

$$
\begin{aligned}
s[x\mapsto s(x)]&=s,\\
\bigl(s[x\mapsto a]\bigr)[x\mapsto b]&=s[x\mapsto b],\\
x\ne y\quad&\Longrightarrow\quad
\bigl(s[x\mapsto a]\bigr)[y\mapsto b]
=\bigl(s[y\mapsto b]\bigr)[x\mapsto a].
\end{aligned}
$$

Además, $s[x\mapsto a]$ y $s$ coinciden en $X\setminus\{x\}$; por tanto, si $S\subseteq X$ y $x\notin S$, se cumple

$$
\bigl(s[x\mapsto a]\bigr)\!\upharpoonright_S=s\!\upharpoonright_S.
$$

**Demostración.** Para la primera igualdad fijemos cualquier $z\in X$. Si $z=x$, ambos lados valen $s(x)$; de lo contrario ambos valen $s(z)$. Para la segunda, cuando $z=x$ prevalece el último valor $b$; cuando $z\ne x$ ninguna de las actualizaciones altera $s(z)$. En la tercera, los casos $z=x$, $z=y$ y $z\notin\{x,y\}$ son exhaustivos por $x\ne y$. En ellos ambas aplicaciones tienen, respectivamente, los valores $a$, $b$ y $s(z)$. La extensionalidad de funciones prueba las igualdades. La afirmación sobre restricciones se sigue directamente de la cláusula para $z\ne x$. $\square$

La **última actualización de una misma variable** prevalece. Las actualizaciones en variables **distintas** conmutan, sin pretender que todas las sustituciones sintácticas sucesivas conmuten: la comparación sería entre operaciones de distinta naturaleza.

## 7.6. Interpretación recursiva de términos

### Metateorema 7.6.1 — Existencia y unicidad de la evaluación de términos {#tlog-mth-00023}

**Enunciado.** Para toda $\tau$-estructura $\mathfrak A$ de universo $A$ y toda asignación $s:X\to A$, existe una única aplicación

$$
\operatorname{val}_{\mathfrak A,s}:\operatorname{Tm}_\tau\longrightarrow A
$$

que satisface las ecuaciones

$$
\boxed{
\begin{aligned}
\operatorname{val}_{\mathfrak A,s}(x)&=s(x)&& (x\in X),\\
\operatorname{val}_{\mathfrak A,s}(f(t_1,\ldots,t_n))
&=f^{\mathfrak A}\bigl(\operatorname{val}_{\mathfrak A,s}(t_1),\ldots,\operatorname{val}_{\mathfrak A,s}(t_n)\bigr)
&& (f\in F_n).
\end{aligned}}
$$

Su valor en $t$ se escribirá también $\llbracket t\rrbracket_{\mathfrak A,s}$. Si $f\in F_0$, la ecuación especializada es

$$
\llbracket f()\rrbracket_{\mathfrak A,s}=f^{\mathfrak A}(()).
$$

En particular, el valor de una constante no depende de $s$.

**Demostración.** Aplicamos [TLOG-MTH-00017](capitulo-06.md#tlog-mth-00017), el teorema general de recursión de términos, con codominio $A$, datos iniciales $a(x):=s(x)$ y operaciones $G_f:=f^{\mathfrak A}:A^n\to A$. Por §7.2 las operaciones $G_f$ están bien tipadas y son totales, inclusive para $n=0$. Se cumplen, por tanto, todas las hipótesis del metateorema de recursión. Éste entrega una función $\operatorname{val}_{\mathfrak A,s}$ y su unicidad, con exactamente las ecuaciones deseadas. No se ha definido una evaluación mediante intuiciones sobre «el significado» de una expresión: existe una **función conjuntista** única con los valores especificados. $\square$

La distinción de §7.1 sigue siendo esencial: $\llbracket t\rrbracket_{\mathfrak A,s}\in A$, no un valor de verdad. Aun cuando $t$ sea una variable individual, $\llbracket x\rrbracket_{\mathfrak A,s}=s(x)$; una asignación no se identifica con un elemento del lenguaje objeto.

## 7.7. Localidad de la interpretación

### Lema 7.7.1 — Dependencia exclusivamente de las variables presentes {#tlog-lem-00017}

**Enunciado.** Sean $s,r:X\to A$ asignaciones en una misma estructura $\mathfrak A$. Para todo término $t\in\operatorname{Tm}_\tau$:

$$
\boxed{
s\!\upharpoonright_{\operatorname{Var}_\tau(t)}
=r\!\upharpoonright_{\operatorname{Var}_\tau(t)}
\quad\Longrightarrow\quad
\llbracket t\rrbracket_{\mathfrak A,s}
=\llbracket t\rrbracket_{\mathfrak A,r}.}
$$

Como caso particular, si $\operatorname{Var}_\tau(t)=\varnothing$, entonces el valor de $t$ es **independiente de toda asignación** a $A$. Si $x\notin\operatorname{Var}_\tau(t)$, cualquier actualización $s[x\mapsto a]$ conserva el valor de $t$.

**Demostración.** Inducimos sobre los términos con [TLOG-MTH-00014](capitulo-05.md#tlog-mth-00014). Para $t=x$, la hipótesis dice $s(x)=r(x)$, y la ecuación variable de §7.6 concluye la igualdad. Para $t=f(t_1,\ldots,t_n)$, [TLOG-MTH-00016](capitulo-06.md#tlog-mth-00016) garantiza

$$
\operatorname{Var}_\tau(t)=\bigcup_{i=1}^{n}\operatorname{Var}_\tau(t_i).
$$

Por consiguiente, el acuerdo en $\operatorname{Var}_\tau(t)$ implica el acuerdo en cada soporte $\operatorname{Var}_\tau(t_i)$. Aplicamos a cada argumento la hipótesis inductiva y obtenemos

$$
\llbracket t_i\rrbracket_{\mathfrak A,s}
=\llbracket t_i\rrbracket_{\mathfrak A,r}
\qquad(1\le i\le n).
$$

La función extensional $f^{\mathfrak A}$ toma valores iguales en tuplas iguales. La ecuación recursiva de §7.6 entrega entonces el mismo valor para $t$ bajo las dos asignaciones. Cuando $n=0$, las tuplas de argumentos son vacías y la igualdad es inmediata: ninguna variable aparece en una constante. El primer corolario aplica la tesis porque toda restricción a $\varnothing$ coincide con otra; el segundo, porque [TLOG-LEM-00016](#tlog-lem-00016) garantiza acuerdo fuera de $\{x\}$. $\square$

La localidad se refiere a una **estructura fijada**. Si se modifica el valor de la función $f^{\mathfrak A}$ o de una constante que aparece en el término, la conclusión anterior no autoriza conservar su evaluación. La invariancia bajo extensiones o reductos de signaturas se estudiará separadamente.

## 7.8. Sustitución sintáctica y actualización semántica

### Metateorema 7.8.1 — Lema de sustitución para términos {#tlog-mth-00024}

**Enunciado.** Sea $\sigma:X\to\operatorname{Tm}_\tau$ una sustitución sintáctica **arbitraria**, sin exigencia de soporte finito, y sea $s:X\to A$ una asignación en una estructura $\mathfrak A$. Definimos la asignación inducida por $\sigma$ y $s$ mediante

$$
\boxed{s^{\sigma}(x):=\llbracket\sigma(x)\rrbracket_{\mathfrak A,s}}
\qquad(x\in X).
$$

Entonces para todo término $t\in\operatorname{Tm}_\tau$:

$$
\boxed{\llbracket t^{\sigma}\rrbracket_{\mathfrak A,s}
=\llbracket t\rrbracket_{\mathfrak A,s^\sigma}.}
$$

Para una sustitución simple $\sigma_{x,u}$, con $\sigma_{x,u}(x)=u$ e identidad fuera de $x$, se obtiene la identidad particular

$$
\boxed{
\llbracket t[u/x]\rrbracket_{\mathfrak A,s}
=\llbracket t\rrbracket_{\mathfrak A,
 s[x\mapsto\llbracket u\rrbracket_{\mathfrak A,s}]}.}
$$

**Demostración.** Cada $\sigma(x)$ es un término, de modo que $\llbracket\sigma(x)\rrbracket_{\mathfrak A,s}\in A$ por §7.6. La aplicación $s^\sigma:X\to A$ está, por tanto, bien definida aun si el soporte de $\sigma$ es infinito. Usamos inducción estructural sobre $t$.

Si $t=x$ es una variable, las cláusulas de sustitución y de evaluación dan

$$
\llbracket x^\sigma\rrbracket_{\mathfrak A,s}
=\llbracket\sigma(x)\rrbracket_{\mathfrak A,s}
=s^\sigma(x)
=\llbracket x\rrbracket_{\mathfrak A,s^\sigma}.
$$

Supongamos la tesis demostrada para $t_1,\ldots,t_n$ y tomemos $t=f(t_1,\ldots,t_n)$. Por la extensión homomórfica de la sustitución a términos y la cláusula funcional de evaluación,

$$
\begin{aligned}
\llbracket f(t_1,\ldots,t_n)^\sigma\rrbracket_{\mathfrak A,s}
&=\llbracket f(t_1^\sigma,\ldots,t_n^\sigma)\rrbracket_{\mathfrak A,s}\\
&=f^{\mathfrak A}\bigl(\llbracket t_1^\sigma\rrbracket_{\mathfrak A,s},\ldots,
\llbracket t_n^\sigma\rrbracket_{\mathfrak A,s}\bigr)\\
&=f^{\mathfrak A}\bigl(\llbracket t_1\rrbracket_{\mathfrak A,s^\sigma},\ldots,
\llbracket t_n\rrbracket_{\mathfrak A,s^\sigma}\bigr)\\
&=\llbracket f(t_1,\ldots,t_n)\rrbracket_{\mathfrak A,s^\sigma}.
\end{aligned}
$$

Para $n=0$, ambos lados son $f^{\mathfrak A}(())$, y el argumento sigue siendo correcto. Esto termina la inducción. En el caso $\sigma=\sigma_{x,u}$, la definición de $s^\sigma$ da para todo $y\in X$

$$
s^{\sigma_{x,u}}(y)=
\begin{cases}
\llbracket u\rrbracket_{\mathfrak A,s},&y=x,\\
s(y),&y\ne x,
\end{cases}
$$

por lo que $s^{\sigma_{x,u}}=s[x\mapsto\llbracket u\rrbracket_{\mathfrak A,s}]$ como funciones. Sustituir esta identidad en la ecuación general prueba el caso particular. $\square$

**Nota de alcance.** Este lema no depende de interpretación de predicados, satisfacción ni equivalencia alfa: compara dos rutas para calcular el **mismo elemento de** $A$ a partir de un término. No permite todavía escribir una relación de verdad para $\varphi^\sigma$. La sustitución total de fórmulas de §6.30 —que evita captura— se incorporará al teorema semántico de sustitución sólo después de definir rigurosamente $\mathfrak A,s\models\varphi$ en el Capítulo 8.

## 7.9. Ejemplos de funcionamiento

**Una signatura elemental.** Considérese $F_0=\{c\}$, $F_1=\{u\}$, $R_2=\{E\}$, $R_0=\{B\}$ y los demás conjuntos de símbolos vacíos. Tomemos $A=\omega$, $c^{\mathfrak A}(())=0$, $u^{\mathfrak A}(m)=m+1$, $E^{\mathfrak A}=\{(m,n)\in\omega^2:m<n\}$ y $B^{\mathfrak A}=\{()\}$. Si $s(x_0)=2$, obtenemos

$$
\llbracket u(u(x_0))\rrbracket_{\mathfrak A,s}=4,
\qquad
\llbracket c()\rrbracket_{\mathfrak A,s}=0.
$$

Alterar sólo $s(x_1)$ no afecta el primer valor, puesto que $\operatorname{Var}_\tau(u(u(x_0)))=\{x_0\}$. En cambio, cambiar $s(x_0)$ sí puede afectarlo. Todavía no se afirma formalmente la **verdad** del átomo $E(c(),u(x_0))$ ni del símbolo nulario $B()$: esa evaluación de fórmulas es competencia del próximo capítulo.

**Una signatura vacía.** Si $F_n=R_n=\varnothing$ para todo $n$, los términos son exactamente las variables $X$. Sobre cualquier $A\ne\varnothing$, una estructura no requiere interpretaciones extralógicas y la evaluación se reduce a $\llbracket x\rrbracket_{\mathfrak A,s}=s(x)$. Aun en este lenguaje subsisten fórmulas de igualdad lógica $x\doteq y$, pero su satisfacción **no** se define a través de un predicado extralógico oculto.

**Sustituciones simultáneas.** Para un término $t=u(x_0)$ y sustitución $\sigma(x_0)=u(x_1)$, el cálculo sintáctico entrega $t^\sigma=u(u(x_1))$. El teorema 7.8.1 asegura que su valor en $s$ coincide con evaluar $u(x_0)$ bajo la nueva asignación $s^\sigma$, donde $s^\sigma(x_0)=s(x_1)+1$. La igualdad entre las dos evaluaciones no depende de cómo se hayan llamado las variables, sino de que los términos y operaciones estén tipados por la misma signatura.

## 7.11. Cambio de signatura: qué significa conservar un lenguaje

### Definición 7.11.1 — Inclusión de signaturas, reducto y expansión {#tlog-def-00041}

Sean $\tau=((F_n)_{n\in\omega},(R_n)_{n\in\omega})$ y $\tau'=((F'_n)_{n\in\omega},(R'_n)_{n\in\omega})$ signaturas del §5.2. Escribiremos $\tau\subseteq\tau'$ si, para **cada** $n\in\omega$,

$$
F_n\subseteq F'_n,\qquad R_n\subseteq R'_n.
$$

La inclusión es **literal y conserva el tipo y la aridad**: un símbolo funcional de aridad dos no puede pasar a ser, en la signatura ampliada, un símbolo relacional o una función de otra aridad. Los alfabetos y los constructores lógicos comunes siguen siendo los de los capítulos 5–6; en particular, $\doteq$ no se agrega a $R_2$.

Si $\mathfrak B$ es una $\tau'$-estructura de universo $B$, su **reducto a** $\tau$, denotado $\mathfrak B\!\upharpoonright_\tau$, es la $\tau$-estructura que conserva el universo $B$ y, para cada símbolo de $\tau$, exactamente la misma interpretación: $f^{\mathfrak B\upharpoonright_\tau}=f^{\mathfrak B}$ y $R^{\mathfrak B\upharpoonright_\tau}=R^{\mathfrak B}$. Si $\mathfrak A=\mathfrak B\!\upharpoonright_\tau$, se llama a $\mathfrak B$ una **expansión** de $\mathfrak A$ a $\tau'$.

La operación «reducto» **olvida símbolos, no elementos del universo**. No debe confundirse con la operación «subestructura», definida en §7.18, que puede reducir el universo. En ambos casos permanecen separados datos sintácticos (la signatura) y datos semánticos (las funciones y relaciones que la estructura asigna a sus símbolos).

### Nota pedagógica — Dos modificaciones diferentes

Si una estructura tiene universo $\omega$, función de sucesor, constante cero y la relación de orden, olvidar el orden produce un reducto **sobre el mismo** $\omega$. Restringir el universo de otra estructura a un subconjunto cerrado bajo sus operaciones —si existe tal subconjunto— plantea, en cambio, una cuestión de **subestructura**. La primera operación no requiere cierre algebraico; la segunda sí. Ninguna implica por sí sola la otra.

## 7.12. Existencia de expansiones en ZF

### Proposición 7.12.1 — Reducción iterada y expansión uniforme {#tlog-pro-00009}

**Enunciado.** Se cumplen las siguientes afirmaciones para signaturas arbitrarias:

1. Si $\tau\subseteq\tau'\subseteq\tau''$ y $\mathfrak C$ es una $\tau''$-estructura, entonces
   $$
   (\mathfrak C\!\upharpoonright_{\tau'})\!\upharpoonright_\tau
   =\mathfrak C\!\upharpoonright_\tau.
   $$
   Además, $\mathfrak C\!\upharpoonright_{\tau''}=\mathfrak C$.
2. Si $\tau\subseteq\tau'$ y $\mathfrak A$ es una $\tau$-estructura de universo no vacío $A$, entonces existe una $\tau'$-expansión $\mathfrak B$ de $\mathfrak A$, con universo **exactamente** $A$, demostrable en ZF sin el axioma de elección. La expansión no tiene por qué ser única.

**Demostración.** En el primer punto, las dos sucesivas restricciones de las familias de funciones y relaciones dejan, para cada símbolo de $\tau$, el dato original de $\mathfrak C$. Como el universo tampoco cambia, los datos estructurales de ambos lados son idénticos. La restricción de una familia a sus índices originales prueba la identidad.

Para el segundo punto, fijemos un elemento $a_0\in A$, posible por $A\ne\varnothing$. En los símbolos de $\tau$ preservamos exactamente las interpretaciones de $\mathfrak A$. Si $f\in F'_n\setminus F_n$, definimos $f^{\mathfrak B}:A^n\to A$ por $f^{\mathfrak B}(\bar a)=a_0$ para toda $\bar a\in A^n$, **incluido** $n=0$, donde el argumento es la tupla vacía. Si $R\in R'_n\setminus R_n$, ponemos $R^{\mathfrak B}:=\varnothing\subseteq A^n$. Estas prescripciones no entran en conflicto, pues los símbolos, tipos y aridades se mantienen disjuntos. Sus familias son funciones conjuntistas obtenidas por separación y reemplazo en los conjuntos de índices de la signatura ampliada. Una única elección existencial $a_0\in A$, utilizada **uniformemente** en todas las funciones nuevas, no equivale a escoger separadamente elementos para una familia arbitraria de conjuntos. La estructura $\mathfrak B$ satisface las cláusulas de §7.2 y su reducto a $\tau$ es $\mathfrak A$. $\square$

**Contracontrol.** La construcción no garantiza que se pueda ampliar una estructura respetando propiedades adicionales *no impuestas por la definición de signatura*, como exigir que un nuevo símbolo relacional represente un orden total o que una nueva operación tenga un inverso. La existencia probada sólo exige el tipado de la nueva firma.

## 7.13. Conservatividad sintáctica de las inclusiones de signaturas

### Lema 7.13.1 — Persistencia de términos, fórmulas y vinculación {#tlog-lem-00018}

**Enunciado.** Si $\tau\subseteq\tau'$, todo término de $\tau$ es un término de $\tau'$, y toda fórmula de $\tau$ es una fórmula de $\tau'$. Al considerarlos en la signatura mayor, se conservan **literalmente** el árbol de análisis, las direcciones de ocurrencia, el soporte de variables de términos, el conjunto de variables libres de fórmulas, su condición de sentencia y las relaciones de ligadura. Para $\varphi,\psi\in\operatorname{Fm}_\tau$, también se conserva $\varphi\equiv_\alpha\psi$ en ambas direcciones.

**Demostración.** Por inducción en la construcción de términos, las hojas variables permanecen en el conjunto común $X$, y cada constructor $f\in F_n$ continúa siendo un constructor de la **misma aridad** en $F'_n$. Los términos tienen, por tanto, la misma lista de hijos y el mismo árbol. Para fórmulas atómicas, cada $R\in R_n$ sigue perteneciendo a $R'_n$, y el constructor de igualdad lógica no depende de la signatura. La inducción sobre fórmulas conserva negación, los cuatro conectivos binarios y ambos cuantificadores con su nombre declarado y su matriz. Ninguno añade un nuevo nodo ni altera uno antiguo. De ello se siguen las igualdades de soportes y de las direcciones de vinculantes mediante las definiciones de §§6.1–6.4. Como un cuantificador tiene el mismo alcance en el mismo árbol, $\operatorname{FV}_\tau(\varphi)=\operatorname{FV}_{\tau'}(\varphi)$. En particular, $\operatorname{FV}=\varnothing$ es independiente de la ampliación.

Para la equivalencia alfa, cada paso elemental o contextual de §6.23 cambia únicamente el **nombre declarado** y las correspondientes hojas variables, nunca un símbolo extralógico. La condición de frescura $y\notin\operatorname{Names}(\cdot)$ se calcula sobre el mismo árbol y da el mismo resultado en ambas signaturas. Una cadena finita de pasos alfa en $\tau$ sigue siendo tal en $\tau'$; recíprocamente, una cadena que parte de una $\tau$-fórmula no puede introducir símbolos ausentes de $\tau$, por lo que todos sus términos intermedios y fórmulas siguen perteneciendo a $\tau$. Así las dos relaciones coinciden sobre $\operatorname{Fm}_\tau$. $\square$

El lema es **puramente sintáctico**: no afirma que dos estructuras distintas interpreten igual sus símbolos comunes. Esa conclusión requiere el dato adicional del reducto y la evaluación de términos.

## 7.14. La evaluación no ve los símbolos olvidados

### Metateorema 7.14.1 — Invariancia por reducto y localidad extralógica {#tlog-mth-00025}

**Enunciado.** Sean $\tau\subseteq\tau'$, una $\tau'$-estructura $\mathfrak B$ de universo $B$, su reducto $\mathfrak A:=\mathfrak B\!\upharpoonright_\tau$ y una asignación $s:X\to B$. Para todo $t\in\operatorname{Tm}_\tau$,

$$
\boxed{\llbracket t\rrbracket_{\mathfrak A,s}
=\llbracket t\rrbracket_{\mathfrak B,s}.}
$$

Más generalmente, sean $\mathfrak A_1,\mathfrak A_2$ dos $\tau$-estructuras **sobre el mismo conjunto** $A$. Denotemos por $\operatorname{FSym}(t)$ el conjunto finito de símbolos funcionales que aparecen como nodos en $t$. Si $f^{\mathfrak A_1}=f^{\mathfrak A_2}$ para cada $f\in\operatorname{FSym}(t)$ y las asignaciones $s,r:X\to A$ coinciden sobre $\operatorname{Var}_\tau(t)$, entonces

$$
\llbracket t\rrbracket_{\mathfrak A_1,s}
=\llbracket t\rrbracket_{\mathfrak A_2,r}.
$$

**Demostración.** La primera afirmación se obtiene de la segunda: por la definición de reducto, las interpretaciones de todos los símbolos funcionales de $\tau$ son idénticas en $\mathfrak A$ y $\mathfrak B$, y la asignación es la misma. Para la forma general, la existencia del conjunto finito $\operatorname{FSym}(t)$ procede de la finitud del árbol de término; no es necesario exigir finitud de la signatura completa. Aplicamos inducción estructural. En una hoja variable $x$, las dos evaluaciones son $s(x)$ y $r(x)$, iguales por acuerdo sobre el soporte. Si $t=f(t_1,\ldots,t_n)$, cada $\operatorname{FSym}(t_i)$ está contenido en $\operatorname{FSym}(t)$ y cada $\operatorname{Var}(t_i)$ en $\operatorname{Var}(t)$. Las hipótesis inductivas igualan los valores de los argumentos. La operación $f^{\mathfrak A_1}=f^{\mathfrak A_2}$ actúa sobre la misma tupla en ambos casos, de modo que iguala los valores del término compuesto. Para $n=0$, se comparan las mismas operaciones nularias sobre $()$; tampoco interviene asignación. $\square$

::: {.callout-note}
## Frontera conceptual

Esta invariancia sólo se refiere a **denotaciones de términos**. Una fórmula relacional puede distinguir dos estructuras que asignen relaciones diferentes al mismo símbolo, aun cuando todos los términos tengan la misma interpretación. La satisfacción de tales fórmulas no está definida todavía.
:::

## 7.15. Aplicaciones entre estructuras: homomorfismos y embeddings

### Definición 7.15.1 — Homomorfismo, embedding e isomorfismo {#tlog-def-00042}

Sean $\mathfrak A$ y $\mathfrak B$ estructuras de la **misma** signatura $\tau$, con universos $A$ y $B$. Un **homomorfismo** $h:\mathfrak A\to\mathfrak B$ es una función $h:A\to B$ que satisface, para todo $n\in\omega$,

$$
\begin{aligned}
h\bigl(f^{\mathfrak A}(a_1,\ldots,a_n)\bigr)
&=f^{\mathfrak B}(h(a_1),\ldots,h(a_n))&& (f\in F_n),\\
(a_1,\ldots,a_n)\in R^{\mathfrak A}
&\Longrightarrow (h(a_1),\ldots,h(a_n))\in R^{\mathfrak B}&&(R\in R_n).
\end{aligned}
$$

Para $n=0$, la primera identidad significa $h(f^{\mathfrak A}(()))=f^{\mathfrak B}(())$; la segunda dice que la pertenencia de $()$ a una relación nularia de $\mathfrak A$ **obliga** a su pertenencia a la correspondiente relación de $\mathfrak B$, pero no a la inversa.

Un **embedding** (o *inmersión estructural*) es un homomorfismo **inyectivo** que, además, **refleja** todas las relaciones: para cada $R$ y $\bar a\in A^n$,

$$
\bar a\in R^{\mathfrak A}
\quad\Longleftrightarrow\quad
h^n(\bar a)\in R^{\mathfrak B},
\qquad h^n(a_1,\ldots,a_n):=(h(a_1),\ldots,h(a_n)).
$$

Un **isomorfismo** es un embedding biyectivo; un **automorfismo** es un isomorfismo de una estructura consigo misma. La notación $\mathfrak A\cong_\tau\mathfrak B$ significa que existe un isomorfismo, no que ambos objetos conjuntistas sean iguales.

**Precisión terminológica.** Enderton llama *homomorfismo* a una aplicación que **preserva y refleja** relaciones; Rautenberg utiliza el término para la condición de preservación, y distingue los homomorfismos fuertes. TLOG adopta esta segunda convención para que un homomorfismo no inyectivo **no** adquiera implícitamente propiedades que sólo tienen los embeddings. Un homomorfismo cualquiera preserva la igualdad de elementos, pero no está obligado a reflejarla: de $h(a)=h(b)$ no se sigue $a=b$ sin inyectividad.

### Nota pedagógica — Una implicación no es una equivalencia

Si $R\in R_1$, tomamos $A=B=\{0\}$, la identidad $h(0)=0$, $R^{\mathfrak A}=\varnothing$ y $R^{\mathfrak B}=\{0\}$. Para la signatura que sólo contiene $R$, $h$ es un homomorfismo **inyectivo**: la implicación de preservación es vacuamente verdadera. Sin embargo, no es un embedding, porque $0\in R^{\mathfrak B}$ y $0\notin R^{\mathfrak A}$. La **inyectividad sola no refleja relaciones**.

## 7.16. Naturalidad de la evaluación

### Metateorema 7.16.1 — El valor de un término conmuta con homomorfismos {#tlog-mth-00026}

**Enunciado.** Sea $h:\mathfrak A\to\mathfrak B$ un homomorfismo entre $\tau$-estructuras, sea $s:X\to A$ una asignación y sea $t\in\operatorname{Tm}_\tau$. Entonces

$$
\boxed{
h\bigl(\llbracket t\rrbracket_{\mathfrak A,s}\bigr)
=\llbracket t\rrbracket_{\mathfrak B,h\circ s}.}
$$

Para cada $x\in X$ y $a\in A$ se cumple también la compatibilidad de actualizaciones

$$
\boxed{h\circ(s[x\mapsto a])=(h\circ s)[x\mapsto h(a)].}
$$

**Demostración.** Como $h:A\to B$, la composición $h\circ s:X\to B$ es una asignación total. La primera igualdad se prueba por inducción estructural en $t$. Si $t=x$, el lado izquierdo es $h(s(x))$, que coincide con $(h\circ s)(x)$ y, por la cláusula variable de §7.6, con el lado derecho. Si $t=f(t_1,\ldots,t_n)$, la ecuación funcional del homomorfismo y las hipótesis inductivas dan

$$
\begin{aligned}
h\bigl(\llbracket f(t_1,\ldots,t_n)\rrbracket_{\mathfrak A,s}\bigr)
&=h\bigl(f^{\mathfrak A}(\llbracket t_1\rrbracket_{\mathfrak A,s},\ldots,\llbracket t_n\rrbracket_{\mathfrak A,s})\bigr)\\
&=f^{\mathfrak B}(h(\llbracket t_1\rrbracket_{\mathfrak A,s}),\ldots,h(\llbracket t_n\rrbracket_{\mathfrak A,s}))\\
&=f^{\mathfrak B}(\llbracket t_1\rrbracket_{\mathfrak B,h\circ s},\ldots,\llbracket t_n\rrbracket_{\mathfrak B,h\circ s})\\
&=\llbracket f(t_1,\ldots,t_n)\rrbracket_{\mathfrak B,h\circ s}.
\end{aligned}
$$

La demostración cubre $n=0$: la identidad es precisamente $h(f^{\mathfrak A}(()))=f^{\mathfrak B}(())$. Ninguna condición sobre las relaciones ha sido usada para **evaluar términos**; su preservación es necesaria para hablar de homomorfismos de estructuras completas, no para este cálculo funcional.

Para la actualización, evaluamos ambas funciones en una variable arbitraria $y$. Si $y=x$, el primer miembro vale $h(a)$ y el segundo también. Si $y\ne x$, ambos valen $h(s(y))$. Por extensionalidad de funciones son iguales. $\square$

La igualdad de actualizaciones será una condición técnica directa para interpretar cuantificadores en el Capítulo 8. En el presente capítulo **no** se utiliza todavía para afirmar que alguna fórmula es verdadera.

## 7.17. Composición de aplicaciones estructurales

### Proposición 7.17.1 — Identidades, composición e inversas {#tlog-pro-00010}

**Enunciado.** Para una signatura fija $\tau$: (i) la identidad de cada universo determina un isomorfismo de su estructura consigo misma; (ii) la composición de homomorfismos es un homomorfismo y la de embeddings es un embedding; (iii) el inverso conjuntista de un isomorfismo es también un isomorfismo. En consecuencia, $\cong_\tau$ es una relación de equivalencia sobre la **clase** de $\tau$-estructuras.

**Demostración.** La identidad respeta todas las operaciones y las relaciones por reflexividad de la igualdad; es inyectiva y sobreyectiva. Sean $h:\mathfrak A\to\mathfrak B$ y $k:\mathfrak B\to\mathfrak C$ homomorfismos. Para cada símbolo funcional $f$ y $\bar a\in A^n$,

$$
(k\circ h)(f^{\mathfrak A}(\bar a))
=k(f^{\mathfrak B}(h^n(\bar a)))
=f^{\mathfrak C}((k\circ h)^n(\bar a)).
$$

Si $\bar a\in R^{\mathfrak A}$, la preservación por $h$ y después por $k$ entrega $(k\circ h)^n(\bar a)\in R^{\mathfrak C}$. Ambas cláusulas valen también para $n=0$, ya que las tuplas vacías se transportan a sí mismas. Si $h,k$ son embeddings, la composición es inyectiva; la implicación relacional inversa resulta aplicando primero la reflexión de $k$ y luego la de $h$. Es, por tanto, un embedding.

Sea ahora $h$ un isomorfismo biyectivo. Para $\bar b\in B^n$, escribimos $\bar a=(h^{-1})^n(\bar b)$. La identidad funcional de $h$ se transforma, aplicando $h^{-1}$, en

$$
h^{-1}(f^{\mathfrak B}(\bar b))=f^{\mathfrak A}((h^{-1})^n(\bar b)).
$$

La bicondicional de relaciones se invierte del mismo modo. Por tanto $h^{-1}$ es un homomorfismo que refleja relaciones y es biyectivo: un isomorfismo. Las tres propiedades de $\cong_\tau$ se deducen de identidad, inversa y composición. Aunque se hable de relación sobre una clase, no se postula un conjunto de **todas** las estructuras sin restringir universos. $\square$

## 7.18. Subestructuras: ahora sí cambia el universo

### Definición 7.18.1 — Subestructura e inclusión inducida {#tlog-def-00043}

Sean $\mathfrak A$ y $\mathfrak B$ $\tau$-estructuras con universos $A\subseteq B$. Decimos que $\mathfrak A$ es una **subestructura** de $\mathfrak B$, y escribimos $\mathfrak A\preccurlyeq_{\mathrm{sub}}\mathfrak B$, cuando:

$$
\begin{aligned}
f^{\mathfrak A}&=f^{\mathfrak B}\!\upharpoonright_{A^n} &&(f\in F_n),\\
R^{\mathfrak A}&=R^{\mathfrak B}\cap A^n &&(R\in R_n).
\end{aligned}
$$

Se exige asimismo que cada $f^{\mathfrak B}(A^n)\subseteq A$, para que la restricción funcional tenga realmente tipo $A^n\to A$. Esta cláusula está implícita en la existencia de $f^{\mathfrak A}$, pero se enuncia separadamente por claridad. Para $n=0$ exige que la denotación de **cada constante** de $\mathfrak B$ pertenezca a $A$; una relación nularia, en cambio, conserva exactamente su valor porque $A^0=B^0=\{()\}$.

La inclusión conjuntista $\iota_A^B:A\hookrightarrow B$ de una subestructura es un **embedding** por §7.15: conmuta con las operaciones y preserva *y refleja* las relaciones. No se identifica la subestructura con un reducto: en un reducto el universo es idéntico y **disminuye la signatura**, mientras que en una subestructura la signatura es idéntica y puede **disminuir el universo**.

## 7.19. Cierre funcional y estructura generada

### Proposición 7.19.1 — Existencia y unicidad de la subestructura inducida {#tlog-pro-00011}

**Enunciado.** Sea $\mathfrak B$ una $\tau$-estructura de universo $B$, y sea $A\subseteq B$ **no vacío**. Las siguientes condiciones son equivalentes:

1. existe una subestructura $\mathfrak A\preccurlyeq_{\mathrm{sub}}\mathfrak B$ cuyo universo es exactamente $A$;
2. $A$ está cerrado bajo todas las operaciones interpretadas: $f^{\mathfrak B}(A^n)\subseteq A$ para cada $f\in F_n$, incluidos los símbolos de aridad cero.

Cuando existe, tal subestructura es **única**. Además, para cualquier $E\subseteq B$ no vacío, existe una única subestructura mínima de $\mathfrak B$ cuyo universo contiene $E$: la **subestructura generada** por $E$. Si $\mathfrak A\preccurlyeq_{\mathrm{sub}}\mathfrak B$ y $s:X\to A$, entonces para todo término $t$,

$$
\boxed{\llbracket t\rrbracket_{\mathfrak A,s}
=\llbracket t\rrbracket_{\mathfrak B,\iota_A^B\circ s}},
$$

entendiendo la igualdad en $B$ mediante la inclusión $A\subseteq B$.

**Demostración.** Si existe $\mathfrak A$, su función interpretativa $f^{\mathfrak A}$ tiene codominio $A$ y coincide con la restricción de $f^{\mathfrak B}$ a $A^n$; luego la condición de cierre es necesaria. Recíprocamente, supongamos el cierre funcional. Para cada $f\in F_n$, definimos $f^{\mathfrak A}$ restringiendo $f^{\mathfrak B}$ a $A^n$; el cierre garantiza su codominio. Para cada $R\in R_n$, definimos $R^{\mathfrak A}=R^{\mathfrak B}\cap A^n$. Son datos conjuntistas indexados por la signatura, satisfacen §7.2 y verifican §7.18. La definición los determina sin libertad adicional: toda subestructura sobre $A$ tiene esas mismas interpretaciones. De ahí la unicidad.

Para la estructura generada por $E\ne\varnothing$, consideremos la **familia conjuntista**

$$
\mathcal C_E:=\{C\in\mathcal P(B):E\subseteq C\ \land\ C\text{ cerrado bajo cada }f^{\mathfrak B}\}.
$$

Es no vacía porque $B\in\mathcal C_E$. Su intersección $G=\bigcap\mathcal C_E$ contiene $E$, de modo que $G\ne\varnothing$. Para cada $n$ y $\bar g\in G^n$, el valor $f^{\mathfrak B}(\bar g)$ pertenece a todo $C\in\mathcal C_E$, pues $\bar g\in C^n$ (para $n=0$, $()\in C^0$ y el cierre incluye las constantes). Por tanto pertenece a $G$. La primera parte entrega la única subestructura con universo $G$; la denotamos $\langle E\rangle_{\mathfrak B}$. Por construcción está contenida en cualquier otra subestructura cuyo universo contiene $E$. Toda la operación —potencia, separación e intersección— se realiza en ZF sin elección.

Finalmente, la inclusión $\iota_A^B$ es un homomorfismo, por la definición de subestructura. Aplicando [TLOG-MTH-00026](#tlog-mth-00026) a $h=\iota_A^B$, obtenemos $\iota_A^B(\llbracket t\rrbracket_{\mathfrak A,s})=\llbracket t\rrbracket_{\mathfrak B,\iota_A^B\circ s}$; la inclusión no cambia el elemento de $A$ considerado como elemento de $B$, y queda probada la identidad final. $\square$

**Dos controles.** Si la signatura no tiene símbolos funcionales, cualquier $E\ne\varnothing$ ya es un universo cerrado: la estructura generada por $E$ tiene dominio $E$ y relaciones inducidas. Si existe una constante $c\in F_0$ cuya denotación no pertenece a $A$, ninguna subestructura con universo $A$ puede existir, **aunque todas las funciones de aridad positiva preserven** $A$.

## 7.20. Ejemplos contrastivos y frontera semántica

**Reducto frente a subestructura.** Considérese $\tau'$ con dos símbolos funcionales nularios $0,1$, una función binaria $+$ y una relación binaria $<$, interpretados de manera usual sobre $\mathbb Z$. El reducto a $\{0,+\}$ sigue teniendo universo $\mathbb Z$; simplemente olvida el símbolo $1$ y la relación $<$. En cambio, el universo $2\mathbb Z$ es cerrado bajo $+$ y contiene $0$, de modo que determina una subestructura para la signatura $\{0,+\}$, pero **no** para la signatura que exige interpretar la constante $1$ usual: $1\notin2\mathbb Z$.

**El homomorfismo no refleja automáticamente átomos.** Con universo singleton y una relación unaria vacía en la estructura de origen y total en la de destino, la identidad es un homomorfismo y no un embedding (§7.15). Así, la sola ecuación de naturalidad para términos no justifica sustituir, sin hipótesis adicional, el juicio relacional de una estructura por el juicio de la otra. Para igualdad, $h(a)=h(b)$ tampoco implica $a=b$ si $h$ no es inyectiva. Estas diferencias son justamente las que se deberán controlar cuando se defina satisfacción.

**Datos disponibles para el Capítulo 8.** Para interpretar un átomo relacional $R(t_1,\ldots,t_n)$ disponemos ya, sin ninguna operación adicional, de la tupla $(\llbracket t_1\rrbracket_{\mathfrak A,s},\ldots,\llbracket t_n\rrbracket_{\mathfrak A,s})\in A^n$ y del subconjunto $R^{\mathfrak A}\subseteq A^n$. Para una ecuación $t\doteq u$, disponemos de ambos elementos de $A$. En el **Capítulo 8**, y no aquí, se convertirán estas comparaciones en cláusulas de satisfacción y se extenderán por recursión a los cinco conectivos y los dos cuantificadores.

La posible conservación de verdad bajo embeddings o isomorfismos, así como el teorema de sustitución **de fórmulas** y la invariancia bajo equivalencia alfa, no se inferirán sólo de las ecuaciones de términos: requerirán la semántica completa de fórmulas.

## 7.21. Cierre matemático del Capítulo 7

Los bloques `M01` y `M02` construyen conjuntamente: estructuras y asignaciones, operaciones de actualización, evaluación única y localidad de términos, sustitución/evaluación, cambio de signaturas, reductos y expansiones, persistencia sintáctica, homomorfismos/embeddings/isomorfismos, naturalidad de la evaluación, subestructuras y generación por cierre funcional. Se han tratado expresamente las constantes y relaciones **nularias**, la no numerabilidad eventual de la signatura y las demostraciones de existencia en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ sin AC.

Esta salida satisface la función arquitectónica de `TLOG-CH07-0001`. La satisfacción y verdad de fórmulas de primer orden, las nociones de modelo, validez y consecuencia, así como los teoremas de invariancia semántica de fórmulas, **permanecen reservados para `TLOG-CH08-0001`**. Tampoco se introduce una relación de derivabilidad de primer orden, que corresponde al Capítulo 9.

```text
TLOG-CH07-M01 = CLOSED / PASS
TLOG-CH07-M02 = CLOSED / PASS
TLOG-CH07-0001 = CLOSED / PASS
new mathematical nodes = 9
chapter 7 nodes = 17/17 closed
TLOG total registered/closed nodes = 114/114
DAG = 114 nodes / 276 direct edges / acyclic PASS
cross-treaty interfaces = 0
formalization candidates = 34
compiled/verified Lean = 0
chapters closed = 8/24 (33.3% architectural)
PART I = CLOSED / PASS
PART II = OPEN
```

**Próximo capítulo:** `TLOG-CH08-M01 — Satisfacción de fórmulas, cláusulas semánticas y existencia/unicidad de la extensión desde los átomos`.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 6](capitulo-06.md) · [Capítulo 8 →](capitulo-08.md)


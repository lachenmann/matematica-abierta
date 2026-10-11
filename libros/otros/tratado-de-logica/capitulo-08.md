---
title: Capítulo 8 — Satisfacción, verdad y consecuencia
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
content-id: MA-BCH-0210
content-type: book-chapter
source-id: TLOG-CH08-0001
prerequisites:
- MA-BCH-0207
- MA-BCH-0208
- MA-BCH-0209
related:
- MA-BOK-0014
source-sha256: bbc052e2c5daa4d855b7f68f343bbcc064d1bebb7735be045d58e2dfcb4bc838
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 7](capitulo-07.md) · [Capítulo 9 →](capitulo-09.md)

## 8.0. De los valores de términos a la satisfacción de fórmulas

Los capítulos 5 y 6 fijaron la gramática, las ocurrencias de variables y la recursión estructural de las fórmulas de primer orden con igualdad. El Capítulo 7 construyó las estructuras $\mathfrak A$, las asignaciones $s:X\to A$ y la evaluación única $\llbracket t\rrbracket_{\mathfrak A,s}\in A$. Ninguno de esos resultados asigna por sí mismo un valor de verdad a una fórmula. Para ello se necesita definir una operación semántica distinta, regida por las formas de construcción de $\operatorname{Fm}_\tau$.

El presente microtramo **`TLOG-CH08-M01`** define las cláusulas de satisfacción para átomos, conectivos y cuantificadores; demuestra **existencia y unicidad** de su extensión recursiva; prueba la dependencia exclusiva de las variables libres; y fija la verdad de **sentencias en una estructura**. Se reservan para tramos posteriores del capítulo la consecuencia de primer orden entre premisas, la validez sobre todas las estructuras, la invariancia por isomorfismo, la sustitución semántica de fórmulas y el estudio general de teorías.

Trabajamos en $\mathsf M_{\mathrm{ext}}=\mathrm{ZF}$ con lógica clásica **sin axioma de elección**. Las signaturas son conjuntos de símbolos ordenados por aridad finita; $F_0$ contiene constantes y $R_0$, relaciones nularias. La igualdad lógica $\doteq$ se interpretará necesariamente como identidad del dominio, nunca como relación elegida libremente por una estructura. Las cinco conectivas de la gramática TLOG —$\neg,\land,\lor,\to,\leftrightarrow$— y ambos cuantificadores —$\forall,\exists$— son **primitivos**, aunque algunos puedan definirse semánticamente mediante otros.

### Fuentes y decisiones de cotejo

- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), cap. 2, §2.2, pp. **83–87**: interpretación de términos, satisfacción de átomos, actualización de asignaciones, recursión de fórmulas y dependencia de variables libres. Se toma como **control deductivo**, no como prueba importada. Enderton señala además que la recurrencia puede construirse como conjunto de asignaciones satisfactorias; nuestra formulación utiliza la función característica de dicho conjunto.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 2, §2.3, pp. **61–65**: estructura con valoración de variables, cláusulas para igualdad, predicados, negación, conjunción y cuantificador universal, y discusión de las asignaciones modificadas. Se conserva la separación explícita $(\mathfrak A,s)$ de TLOG, en lugar de identificar la pareja con una estructura básica de signatura $\tau$.

**Reconstrucción independiente.** Enderton trabaja con una base reducida de conectivas y cuantificación; Rautenberg también selecciona operadores primitivos distintos de los siete constructores de TLOG. Por ello se dan aquí **todas** las cláusulas semánticas correspondientes a la gramática realmente aprobada por [TLOG-DEF-00026](capitulo-05.md#tlog-def-00026), con inclusión expresa de aridad cero. No se importa ninguna afirmación de completitud o consecuencia desde las fuentes.

## 8.1. Estratos semánticos y codominio de la evaluación

### Convención 8.1.1 — Espacios de asignaciones y valores de verdad {#tlog-cnv-00010}

Fijadas una signatura $\tau$ y una $\tau$-estructura $\mathfrak A$ de universo no vacío $A$, sean

$$
D_{\mathfrak A}:=A^X,\qquad \mathbf2:=\{0,1\},\qquad
\mathcal B_{\mathfrak A}:=\mathbf2^{D_{\mathfrak A}}.
$$

El conjunto $D_{\mathfrak A}$ contiene las asignaciones **totales** $s:X\to A$. Es no vacío: elegimos un solo $a_0\in A$ y usamos la asignación constante $x\mapsto a_0$. El conjunto $\mathcal B_{\mathfrak A}$ contiene las **funciones booleanas sobre asignaciones**, es decir, las funciones $g:D_{\mathfrak A}\to\mathbf2$. Ambos son conjuntos de ZF por potencia, separación y reemplazo; ninguna función elegida de una familia arbitraria aparece en su construcción.

El elemento $0$ representa *no satisfacción* y $1$ representa *satisfacción*. **No** son elementos distinguidos del universo $A$: el codominio de $\llbracket t\rrbracket_{\mathfrak A,s}$ es $A$, mientras que el de la futura evaluación de fórmulas será $\mathbf2$. Cuando $A=\{0,1\}$, la coincidencia conjuntista de sus elementos con los valores booleanos no suprime la diferencia entre el **tipo de dato** de un término y el **papel semántico** de un valor de verdad.

La notación $\mathfrak A,s\models_\tau\varphi$ se activará únicamente tras demostrar la existencia de la evaluación en §8.4. El signo $\models_\tau$ pertenece a la **metateoría**; no añade un símbolo a $\Sigma_\tau$, ni expresa derivabilidad sintáctica.

## 8.2. Evaluación de fórmulas atómicas

### Definición 8.2.1 — Dato semántico inicial sobre los átomos {#tlog-def-00044}

Definimos una función total

$$
b_{\mathfrak A}:\operatorname{At}_\tau\longrightarrow\mathcal B_{\mathfrak A}
$$

que, para cada asignación $s\in D_{\mathfrak A}$, satisface las cláusulas

$$
\boxed{\begin{aligned}
b_{\mathfrak A}(\operatorname{Eq}(t,u))(s)=1
&\iff \llbracket t\rrbracket_{\mathfrak A,s}
=\llbracket u\rrbracket_{\mathfrak A,s},\\
b_{\mathfrak A}(\operatorname{Rel}_{R}(t_1,\ldots,t_n))(s)=1
&\iff
(\llbracket t_1\rrbracket_{\mathfrak A,s},\ldots,
\llbracket t_n\rrbracket_{\mathfrak A,s})\in R^{\mathfrak A}.
\end{aligned}}
$$

En todos los demás casos, cada valor es $0$. La legibilidad única de los átomos permite determinar sus datos constitutivos, y el teorema del Capítulo 7 garantiza la existencia de cada valor de término. Los gráficos de estas funciones se obtienen por separación en conjuntos fijos; por tanto $b_{\mathfrak A}$ es una función conjuntista bien definida.

Para $R\in R_0$, la segunda cláusula se convierte exactamente en

$$
b_{\mathfrak A}(\operatorname{Rel}_R())(s)=1
\iff ()\in R^{\mathfrak A}.
$$

Dicho valor **no depende** de $s$, pues la lista de argumentos está vacía. Una relación nularia representa así un átomo verdadero en todas las asignaciones o falso en todas ellas, según sea $R^{\mathfrak A}=\{()\}$ o $R^{\mathfrak A}=\varnothing$. Asimismo, una ecuación entre términos sin variables no depende de $s$. La igualdad se interpreta como $=_{A}$, no mediante un miembro libremente escogido de $R_2$.

## 8.3. Operadores semánticos sobre funciones booleanas

### Definición 8.3.1 — Conectivos y cuantificación como operaciones totales {#tlog-def-00045}

Para $g,h\in\mathcal B_{\mathfrak A}$ definimos las operaciones semánticas puntuales $N:\mathcal B_{\mathfrak A}\to\mathcal B_{\mathfrak A}$ y $D_\circ:\mathcal B_{\mathfrak A}^2\to\mathcal B_{\mathfrak A}$ mediante

$$
\begin{aligned}
N(g)(s)=1&\iff g(s)=0,\\
D_{\land}(g,h)(s)=1&\iff g(s)=1\ \text{y}\ h(s)=1,\\
D_{\lor}(g,h)(s)=1&\iff g(s)=1\ \text{o}\ h(s)=1,\\
D_{\to}(g,h)(s)=1&\iff g(s)=0\ \text{o}\ h(s)=1,\\
D_{\leftrightarrow}(g,h)(s)=1&\iff g(s)=h(s).
\end{aligned}
$$

Fuera de los casos indicados el valor es $0$. Estas operaciones se calculan en $\mathbf2$, no en el universo de la estructura. Para cada variable $x\in X$ definimos además $U_{\forall,x},U_{\exists,x}:\mathcal B_{\mathfrak A}\to\mathcal B_{\mathfrak A}$ por

$$
\boxed{\begin{aligned}
U_{\forall,x}(g)(s)=1&\iff (\forall a\in A)\;g(s[x\mapsto a])=1,\\
U_{\exists,x}(g)(s)=1&\iff (\exists a\in A)\;g(s[x\mapsto a])=1.
\end{aligned}}
$$

Para cada $s$, estas cláusulas asignan exactamente uno de los dos valores. Puesto que $D_{\mathfrak A}$, $A$ y $\mathbf2$ son conjuntos, la separación en $D_{\mathfrak A}\times\mathbf2$ entrega el gráfico de la nueva función; por reemplazo, el proceso es uniforme en $g$, $x$ y los demás parámetros. En particular, **no** se elige un testigo de cada conjunto de testigos existenciales: el cuantificador $\exists a\in A$ sólo decide el valor de una condición conjuntista.

La actualización $s[x\mapsto a]$ se aplica **antes** de evaluar la subfórmula. No cambia la interpretación de $f\in F_n$ o $R\in R_n$ y no efectúa una sustitución sintáctica en la fórmula. Los cuantificadores $\forall$ y $\exists$ permanecen constructores distintos aun si resultan interdefinibles desde el punto de vista semántico.

## 8.4. Existencia y unicidad de satisfacción

### Metateorema 8.4.1 — Extensión semántica única desde los átomos {#tlog-mth-00027}

**Enunciado.** Para toda signatura conjuntista $\tau$ y toda $\tau$-estructura $\mathfrak A$ de universo no vacío $A$, existe una **única** función

$$
\boxed{H_{\mathfrak A}:\operatorname{Fm}_\tau
\longrightarrow\mathcal B_{\mathfrak A}}
$$

cuyos valores satisfacen, para todo átomo $\alpha$, toda $\varphi,\psi\in\operatorname{Fm}_\tau$, todo $x\in X$, todo $Q\in\{\forall,\exists\}$ y todo $\circ\in\{\land,\lor,\to,\leftrightarrow\}$,

$$
\begin{aligned}
H_{\mathfrak A}(\alpha)&=b_{\mathfrak A}(\alpha),\\
H_{\mathfrak A}(\operatorname{Neg}(\varphi))&=N(H_{\mathfrak A}(\varphi)),\\
H_{\mathfrak A}(\operatorname{Bin}_\circ(\varphi,\psi))
&=D_\circ(H_{\mathfrak A}(\varphi),H_{\mathfrak A}(\psi)),\\
H_{\mathfrak A}(\operatorname{Quant}_{Q,x}(\varphi))
&=U_{Q,x}(H_{\mathfrak A}(\varphi)).
\end{aligned}
$$

**Demostración.** Aplicamos el teorema de recursión sobre fórmulas [TLOG-MTH-00018](capitulo-06.md#tlog-mth-00018), fijando como codominio el **conjunto** $B=\mathcal B_{\mathfrak A}$. El dato inicial es $b_{\mathfrak A}:\operatorname{At}_\tau\to B$ de §8.2. La negación se interpreta por $N:B\to B$, cada uno de los cuatro constructores binarios por $D_\circ:B\times B\to B$, y los dos cuantificadores, para cada $x\in X$, por $U_{Q,x}:B\to B$, definidos en §8.3. Todas las funciones son **totales** y están tipadas exactamente como exige el metateorema de §6.11. Su conclusión da una función $H_{\mathfrak A}$ con esas ecuaciones y demuestra que ninguna otra puede satisfacerlas. Las aplicaciones del teorema de recursión tienen como parámetro una estructura **fija** y no requieren formar un conjunto de todas las estructuras posibles. $\square$

**Definición de satisfacción inducida.** Para $s\in D_{\mathfrak A}$ y $\varphi\in\operatorname{Fm}_\tau$, escribimos

$$
\boxed{\mathfrak A,s\models_\tau\varphi
\quad:\Longleftrightarrow\quad H_{\mathfrak A}(\varphi)(s)=1.}
$$

En esta notación $\models_\tau$ es una relación **metateórica** entre estructura, asignación y fórmula. La propiedad de unicidad anterior equivale a que **no hay dos relaciones de satisfacción** sobre la misma estructura que respeten simultáneamente las cláusulas siguientes:

$$
\begin{aligned}
\mathfrak A,s\models_\tau\operatorname{Eq}(t,u)
&\iff\llbracket t\rrbracket_{\mathfrak A,s}=\llbracket u\rrbracket_{\mathfrak A,s},\\
\mathfrak A,s\models_\tau\operatorname{Rel}_{R}(\bar t)
&\iff\llbracket\bar t\rrbracket_{\mathfrak A,s}\in R^{\mathfrak A},\\
\mathfrak A,s\models_\tau\neg\varphi
&\iff\mathfrak A,s\not\models_\tau\varphi,\\
\mathfrak A,s\models_\tau(\varphi\land\psi)
&\iff(\mathfrak A,s\models_\tau\varphi)\ \text{y}\ (\mathfrak A,s\models_\tau\psi),\\
\mathfrak A,s\models_\tau(\varphi\lor\psi)
&\iff(\mathfrak A,s\models_\tau\varphi)\ \text{o}\ (\mathfrak A,s\models_\tau\psi),\\
\mathfrak A,s\models_\tau(\varphi\to\psi)
&\iff(\mathfrak A,s\not\models_\tau\varphi)\ \text{o}\ (\mathfrak A,s\models_\tau\psi),\\
\mathfrak A,s\models_\tau(\varphi\leftrightarrow\psi)
&\iff\bigl((\mathfrak A,s\models_\tau\varphi)\iff(\mathfrak A,s\models_\tau\psi)\bigr),\\
\mathfrak A,s\models_\tau\forall x\,\varphi
&\iff(\forall a\in A)\;\mathfrak A,s[x\mapsto a]\models_\tau\varphi,\\
\mathfrak A,s\models_\tau\exists x\,\varphi
&\iff(\exists a\in A)\;\mathfrak A,s[x\mapsto a]\models_\tau\varphi.
\end{aligned}
$$

En la segunda fila $\llbracket\bar t\rrbracket$ designa la tupla de valores de términos, y cuando $\bar t=()$, su valor es $()$. La fórmula $\neg\varphi$ es el constructor objeto de negación; la expresión metateórica $\mathfrak A,s\not\models_\tau\varphi$ significa que la relación **no** se cumple. Son cosas de distinto nivel, aun cuando la correspondiente bicondicional las conecte.

**Otra caracterización de la unicidad.** Si $S\subseteq\operatorname{Fm}_\tau\times D_{\mathfrak A}$ es cualquier relación conjuntista que cumple las nueve familias de cláusulas, sus funciones características $H_S(\varphi)(s)=1\iff(\varphi,s)\in S$ satisfacen las ecuaciones del metateorema. Entonces $H_S=H_{\mathfrak A}$ y $S=\{(\varphi,s):H_{\mathfrak A}(\varphi)(s)=1\}$. No hay circularidad escondida en la locución «se define por la verdad de la subfórmula»: primero se construye una única función por recursión, **después** se da nombre a la relación resultante.

## 8.5. Localidad de la satisfacción

### Lema 8.5.1 — Sólo importan los valores de las variables libres {#tlog-lem-00019}

**Enunciado.** Sean $s,r:X\to A$ asignaciones sobre una misma $\tau$-estructura $\mathfrak A$. Si

$$
s\!\upharpoonright_{\operatorname{FV}_\tau(\varphi)}
=r\!\upharpoonright_{\operatorname{FV}_\tau(\varphi)},
$$

entonces

$$
\boxed{\mathfrak A,s\models_\tau\varphi
\quad\Longleftrightarrow\quad
\mathfrak A,r\models_\tau\varphi.}
$$

**Demostración.** Inducimos sobre la estructura finita de $\varphi$. Si $\varphi=\operatorname{Eq}(t,u)$, por [TLOG-MTH-00016](capitulo-06.md#tlog-mth-00016) el conjunto libre de la fórmula es $\operatorname{Var}(t)\cup\operatorname{Var}(u)$. Las asignaciones coinciden en cada variable que aparece en los dos términos; por la localidad de evaluación de términos [TLOG-LEM-00017](capitulo-07.md#tlog-lem-00017), sus valores en $s$ y $r$ coinciden, y la comparación de igualdad tiene el mismo resultado. Si $\varphi=\operatorname{Rel}_{R}(t_1,\ldots,t_n)$, la fórmula de variables libres es $\bigcup_i\operatorname{Var}(t_i)$; el mismo lema iguala cada valor de argumento, por lo que la tupla pertenece o no a $R^{\mathfrak A}$ independientemente de escoger $s$ o $r$. Para $n=0$ no hay argumentos ni variables libres y ambos juicios comparan la pertenencia de $()$ a la misma relación nularia.

La negación y cada conectivo binario se tratan aplicando las hipótesis inductivas a sus subfórmulas: por [TLOG-MTH-00016](capitulo-06.md#tlog-mth-00016), las variables libres de la negación son las de su matriz y las de un binario son la unión de las de sus dos miembros. Así las cláusulas booleanas de §8.4 dan exactamente la misma respuesta para $s$ y $r$.

Queda el caso $\varphi=\operatorname{Quant}_{Q,x}(\psi)$, con $Q\in\{\forall,\exists\}$. Puesto que

$$
\operatorname{FV}(\operatorname{Quant}_{Q,x}(\psi))
=\operatorname{FV}(\psi)\setminus\{x\},
$$

las asignaciones modificadas $s[x\mapsto a]$ y $r[x\mapsto a]$ coinciden **sobre todo** $\operatorname{FV}(\psi)$ para cada $a\in A$: en $x$ ambas valen $a$, y en cualquier $y\ne x$ libre en $\psi$ ya coincidían las asignaciones originales. Por la hipótesis inductiva,

$$
\mathfrak A,s[x\mapsto a]\models_\tau\psi
\iff
\mathfrak A,r[x\mapsto a]\models_\tau\psi
\quad(a\in A).
$$

La cuantificación universal de estas equivalencias, respectivamente la existencia de algún $a$ que las satisfaga, conserva su valor para ambos tipos de cuantificador. Concluye la inducción. $\square$

El lema demuestra **localidad respecto de una estructura fija**. No permite todavía cambiar simultáneamente la estructura, ni sustituir términos por fórmulas, ni afirmar que una estructura más pequeña satisfaga toda fórmula que satisfaga una más grande.

## 8.6. Sentencias y verdad relativa a una estructura

### Corolario 8.6.1 — Independencia de asignación para sentencias {#tlog-cor-00006}

**Enunciado.** Para toda sentencia $\sigma\in\operatorname{Sent}_\tau$ y toda $\tau$-estructura $\mathfrak A$, las siguientes posibilidades son excluyentes y exhaustivas: o bien $\mathfrak A,s\models_\tau\sigma$ para **toda** asignación $s:X\to A$, o bien $\mathfrak A,s\not\models_\tau\sigma$ para **toda** asignación. Por ello es legítimo definir

$$
\boxed{\mathfrak A\models_\tau\sigma
\quad:\Longleftrightarrow\quad
(\forall s\in D_{\mathfrak A})\ \mathfrak A,s\models_\tau\sigma.}
$$

Equivalentemente, puede utilizarse $\exists s\in D_{\mathfrak A}$ en esa cláusula: ambas condiciones coinciden **sólo para sentencias**.

**Demostración.** Por [TLOG-DEF-00031](capitulo-06.md#tlog-def-00031), $\operatorname{FV}(\sigma)=\varnothing$. Dos asignaciones cualesquiera tienen restricciones idénticas al conjunto vacío, de modo que el lema de §8.5 hace equivalentes sus juicios de satisfacción. Como $D_{\mathfrak A}\ne\varnothing$, elijamos temporalmente $s_0\in D_{\mathfrak A}$: si satisface $\sigma$, todas la satisfacen; en caso contrario, ninguna la satisface. La distinción es exhaustiva por lógica clásica. La equivalencia $\exists s\iff\forall s$ vale porque hemos probado constancia y $D_{\mathfrak A}$ es no vacío; sin esta condición, la primera y la segunda condición podrían diferir. $\square$

Llamamos **verdadera en** $\mathfrak A$ a una sentencia que satisface $\mathfrak A\models_\tau\sigma$, y **falsa en** $\mathfrak A$ a la que no la satisface. Esta es **verdad relativa a una estructura**. No se ha definido aún $\models_\tau\sigma$, que exigiría cuantificar sobre todas las estructuras, ni $\Gamma\models_\tau\varphi$, que exigiría definir consecuencia semántica. Tampoco se identifica $\models_\tau$ con $\vdash_\tau$.

## 8.7. Cuantificadores primitivos: dualidad y vacuidad

### Proposición 8.7.1 — Dualidad de cuantificadores y variables no utilizadas {#tlog-pro-00012}

**Enunciado.** Para toda $\mathfrak A$, $s$, $x$ y $\varphi$ bien tipadas se verifican

$$
\begin{aligned}
\mathfrak A,s\models_\tau\forall x\,\varphi
&\iff\mathfrak A,s\models_\tau\neg\exists x\,\neg\varphi,\\
\mathfrak A,s\models_\tau\exists x\,\varphi
&\iff\mathfrak A,s\models_\tau\neg\forall x\,\neg\varphi.
\end{aligned}
$$

Además, cuando $x\notin\operatorname{FV}(\varphi)$, ambas cuantificaciones son **vacuas semánticamente**:

$$
\mathfrak A,s\models_\tau\forall x\,\varphi
\iff\mathfrak A,s\models_\tau\varphi
\iff\mathfrak A,s\models_\tau\exists x\,\varphi.
$$

**Demostración.** La primera equivalencia expresa que para todo $a\in A$ se satisface $\varphi$ bajo $s[x\mapsto a]$ si y sólo si no existe $a\in A$ que satisfaga $\neg\varphi$. La negación aplica la cláusula booleana clásica, y las cuantificaciones utilizan exactamente las cláusulas definidas en §8.4. La segunda equivalencia es la negación dual de la anterior: existe un $a$ que satisface $\varphi$ si y sólo si no sucede que cada $a$ satisfaga $\neg\varphi$. Ninguno de los dos argumentos presupone que $\exists$ sea sintácticamente una abreviatura de $\neg\forall\neg$: las fórmulas comparadas siguen siendo objetos distintos.

Si $x\notin\operatorname{FV}(\varphi)$, $s$ y $s[x\mapsto a]$ coinciden sobre las variables libres de $\varphi$, para cualquier $a\in A$. Por §8.5, $\varphi$ tiene el mismo valor bajo todas estas asignaciones. Así la condición universal equivale al juicio original. La condición existencial también lo equivale porque $A\ne\varnothing$; basta un único elemento $a_0\in A$ para presenciarlo cuando $\varphi$ es satisfecha. $\square$

**Control de hipótesis.** La hipótesis $A\ne\varnothing$ se utiliza **en ambas equivalencias vacuas con la matriz**: asegura que las condiciones universal y existencial examinen al menos una actualización. También garantiza que haya asignaciones totales $X\to A$. Los dominios vacíos no están contemplados por TLOG desde [TLOG-DEF-00039](capitulo-07.md#tlog-def-00039); la dualidad de cuantificadores, a diferencia de la eliminación de una cuantificación vacua, proviene únicamente de las cláusulas booleanas.

## 8.8. Ejemplos que separan forma, valor y alcance

**Una relación nularia.** Si $R\in R_0$ y $R^{\mathfrak A}=\varnothing$, entonces para todas las asignaciones $s$ se tiene $\mathfrak A,s\not\models_\tau R()$. Si $R^{\mathfrak A}=\{()\}$, para todas se cumple $\mathfrak A,s\models_\tau R()$. Las fórmulas son las mismas en ambos casos: lo que cambia es **la estructura**.

**Una fórmula abierta y un cuantificador.** En la signatura con símbolo relacional binario $R$, tomemos $A=\{0,1\}$ y $R^{\mathfrak A}=\{(0,0),(1,1)\}$. La fórmula $R(x_0,x_1)$ se satisface exactamente bajo las asignaciones $s$ para las que $s(x_0)=s(x_1)$. En cambio, la sentencia $\forall x_0\,\exists x_1\,R(x_0,x_1)$ es verdadera en $\mathfrak A$: dado cualquier $a\in A$, la actualización posterior $x_1\mapsto a$ proporciona un valor que se relaciona consigo mismo. No se necesitó escoger simultáneamente un testigo para una familia arbitraria de dominios.

**Sombras de variables.** La sentencia $\forall x_0\,\exists x_0\,(x_0\doteq x_0)$ es verdadera en todo universo no vacío: el cuantificador interno sustituye el valor que el externo había asignado a $x_0$. La variable del cuantificador externo queda semánticamente vacua. Las dos declaraciones no se funden en una sola operación sintáctica.

**Frontera entre estructura y sentencia.** En la signatura que contiene exclusivamente el símbolo de relación unaria $P$, dos estructuras con el mismo universo $\{0\}$ pueden diferir sólo en $P^{\mathfrak A}=\varnothing$ frente a $P^{\mathfrak B}=\{0\}$. Entonces $\exists x\,P(x)$ es falsa en la primera y verdadera en la segunda. Ninguna asignación adicional elimina esa diferencia: una sentencia es independiente de $s$, **no** independiente de $\mathfrak A$.

## 8.10. La actualización de una asignación y la sustitución de términos

### Lema 8.10.1 — Compatibilidad de asignaciones inducidas con cambios puntuales {#tlog-lem-00020}

Sea $\mathfrak A$ una $\tau$-estructura de universo $A\ne\varnothing$, $s:X\to A$ y $x,y\in X$ distintos. Si $t\in\operatorname{Tm}_\tau$ y $y\notin\operatorname{Var}_\tau(t)$, entonces para todo $a\in A$, poniendo $v:=\llbracket t\rrbracket_{\mathfrak A,s}$,

$$
\boxed{\llbracket t\rrbracket_{\mathfrak A,s[y\mapsto a]}=v,
\qquad
(s[y\mapsto a])[x\mapsto v]
=(s[x\mapsto v])[y\mapsto a].}
$$

Existe también una forma **simultánea y local**, válida aun si una sustitución $\sigma:X\to\operatorname{Tm}_\tau$ tiene soporte infinito. Para $y\in X$, sea $\sigma_{[y]}$ la sustitución que fija $y$ y coincide con $\sigma$ en los restantes nombres, según §6.30. Dado cualquier conjunto $Z\subseteq X$, supongamos

$$
y\notin\bigcup_{u\in Z\setminus\{y\}}
\operatorname{Var}_\tau(\sigma(u)).
$$

Entonces, para todo $a\in A$,

$$
\boxed{\bigl((s[y\mapsto a])^{\sigma_{[y]}}\bigr)\!\upharpoonright_Z
=\bigl((s^\sigma)[y\mapsto a]\bigr)\!\upharpoonright_Z.}
$$

**Demostración.** El primer enunciado sobre valores se obtiene de la localidad de términos [TLOG-LEM-00017](capitulo-07.md#tlog-lem-00017): $s[y\mapsto a]$ y $s$ coinciden en $\operatorname{Var}(t)$. La segunda igualdad se deduce de la conmutación de actualizaciones en variables distintas ([TLOG-LEM-00016](capitulo-07.md#tlog-lem-00016)). Para la identidad simultánea basta comparar ambas funciones en cada $u\in Z$. Si $u=y$, el lado izquierdo vale $\llbracket y\rrbracket_{\mathfrak A,s[y\mapsto a]}=a$, y el derecho también. Si $u\ne y$, el lado izquierdo vale $\llbracket\sigma(u)\rrbracket_{\mathfrak A,s[y\mapsto a]}$. La hipótesis asegura que $y\notin\operatorname{Var}(\sigma(u))$, de modo que el lema de localidad lo iguala a $\llbracket\sigma(u)\rrbracket_{\mathfrak A,s}=s^\sigma(u)$, exactamente el valor del lado derecho. Por extensionalidad de funciones restringidas se obtiene la igualdad. No se ha escogido un elemento por cada $u$: se han evaluado términos ya dados. $\square$

**Advertencia de tipos.** En general las asignaciones completas $(s[y\mapsto a])^{\sigma_{[y]}}$ y $(s^\sigma)[y\mapsto a]$ **no coinciden**: pueden diferir sobre variables externas a $Z$ cuyas imágenes contienen $y$. La igualdad sobre las variables libres pertinentes —no una igualdad global injustificada— será la utilizada en §8.14.

## 8.11. Sustitución literal segura: el primer lema semántico

### Metateorema 8.11.1 — Lema de sustitución sin captura {#tlog-mth-00028}

Sean $t\in\operatorname{Tm}_\tau$, $x\in X$, $\varphi\in\operatorname{Fm}_\tau$ y $\operatorname{FreeFor}_\tau(t,x,\varphi)$. Para cualquier $\tau$-estructura $\mathfrak A$ y asignación $s$, escribamos $v_s:=\llbracket t\rrbracket_{\mathfrak A,s}$. Se cumple

$$
\boxed{\mathfrak A,s\models_\tau\varphi[t/x]_{\mathrm{lit}}
\quad\Longleftrightarrow\quad
\mathfrak A,s[x\mapsto v_s]\models_\tau\varphi.}
$$

El reemplazo del lado izquierdo es **simultáneo** sobre las ocurrencias libres de $x$; no sustituye otra vez dentro de las copias insertadas de $t$.

**Demostración.** Por inducción estructural sobre $\varphi$ en el dominio de `FreeFor`. Si $\varphi$ es una ecuación o un átomo $R(t_1,\ldots,t_n)$, la sustitución de fórmulas actúa sobre cada término argumento con $\sigma_{x,t}$. El lema de términos [TLOG-MTH-00024](capitulo-07.md#tlog-mth-00024) identifica el valor de cada argumento sustituido en $s$ con su valor original en $s[x\mapsto v_s]$; por las cláusulas atómicas de §8.2, las dos fórmulas tienen la misma satisfacción. Esto incluye $n=0$: ambas comprueban exactamente $()\in R^{\mathfrak A}$. Los casos de negación y de los cuatro conectivos binarios siguen inmediatamente de las cláusulas booleanas y de las hipótesis inductivas.

Supongamos $\varphi=Qy\,\psi$, donde $Q\in\{\forall,\exists\}$. Si $y=x$, la sustitución literal deja intacta la fórmula cuantificada. Además, $x\notin\operatorname{FV}(Qx\,\psi)$; por localidad semántica (§8.5), la actualización $s[x\mapsto v_s]$ no altera su satisfacción. Si $y\ne x$ pero $x\notin\operatorname{FV}(\psi)$, la sustitución no altera la fórmula y la misma localidad resuelve el caso.

Resta $y\ne x$ y $x\in\operatorname{FV}(\psi)$. La hipótesis `FreeFor` exige simultáneamente `FreeFor(t,x,ψ)` y $y\notin\operatorname{Var}(t)$. Para cada $a\in A$, la hipótesis inductiva, aplicada a la asignación $s[y\mapsto a]$, da

$$
\mathfrak A,s[y\mapsto a]\models_\tau\psi[t/x]_{\mathrm{lit}}
\iff
\mathfrak A,(s[y\mapsto a])[x\mapsto
\llbracket t\rrbracket_{\mathfrak A,s[y\mapsto a]}]\models_\tau\psi.
$$

Por el lema 8.10.1, el valor de $t$ es $v_s$ y la asignación del último miembro es exactamente $(s[x\mapsto v_s])[y\mapsto a]$. Cuantificar sobre todos los $a\in A$ para $Q=\forall$, o sobre alguno para $Q=\exists$, entrega en ambos casos la equivalencia pretendida para $Qy\,\psi$. Termina la inducción. $\square$

La condición `FreeFor` no es ornamental: sin ella, una variable libre del término insertado puede pasar a quedar ligada y destruir esta equivalencia.

## 8.12. Un renombrado ligado no cambia la satisfacción

### Lema 8.12.1 — Invariancia bajo renombrado alfa elemental {#tlog-lem-00021}

Para una fórmula $Qx\,\psi$ y un nombre $y\notin\operatorname{Names}_\tau(\psi)\cup\{x\}$, sea $\psi':=\psi[y/x]_{\mathrm{lit}}$. Entonces para toda $\tau$-estructura $\mathfrak A$ y toda asignación $s$,

$$
\boxed{\mathfrak A,s\models_\tau Qx\,\psi
\quad\Longleftrightarrow\quad
\mathfrak A,s\models_\tau Qy\,\psi'.}
$$

**Demostración.** La condición fuerte de frescura de §6.23 permite la sustitución literal $\psi[y/x]_{\mathrm{lit}}$. Sea $a\in A$ arbitrario. Aplicamos el metateorema anterior con el término sustituyente $y$ y la asignación $s[y\mapsto a]$:

$$
\mathfrak A,s[y\mapsto a]\models_\tau\psi'
\iff
\mathfrak A,(s[y\mapsto a])[x\mapsto a]\models_\tau\psi.
$$

La variable $y$ no pertenece a $\operatorname{FV}(\psi)$, pues está ausente de $\operatorname{Names}(\psi)$. Por tanto $(s[y\mapsto a])[x\mapsto a]$ y $s[x\mapsto a]$ coinciden sobre $\operatorname{FV}(\psi)$; el lema de localidad les asigna idéntica satisfacción de $\psi$. Las cláusulas de cuantificación para $Q=\forall$ y $Q=\exists$ transportan la equivalencia punto por punto en $a$ al cuantificador exterior. $\square$

La prueba no identifica las cadenas $Qx\,\psi$ y $Qy\,\psi'$: utiliza su diferencia sintáctica y demuestra una igualdad de comportamiento semántico.

## 8.13. La equivalencia alfa adquiere interpretación semántica

### Metateorema 8.13.1 — Invariancia de satisfacción bajo $\equiv_\alpha$ {#tlog-mth-00029}

Si $\varphi,\chi\in\operatorname{Fm}_\tau$ satisfacen $\varphi\equiv_\alpha\chi$, entonces

$$
\boxed{(\forall\mathfrak A)(\forall s:X\to A)
\bigl[\mathfrak A,s\models_\tau\varphi
\iff \mathfrak A,s\models_\tau\chi\bigr],}
$$

donde la cuantificación externa sobre $\mathfrak A$ se entiende **metateóricamente sobre la clase definible** de las $\tau$-estructuras, no como un conjunto de todas ellas.

**Demostración.** La equivalencia alfa de §6.23 es la clausura reflexiva, simétrica y transitiva de pasos elementales ejecutados en contextos de fórmula. En la raíz de una fórmula cuantificada, cada paso preserva satisfacción bajo toda asignación por el lema 8.12.1. Mostremos que tal equivalencia se conserva al introducir un contexto alrededor de la subfórmula: la negación y cada conectivo binario consultan sólo los valores de verdad de las subfórmulas; reemplazar una de ellas por otra equivalente en **todas** las asignaciones conserva el valor del compuesto. Para $Qz\,\theta$, se comparan los valores de las matrices bajo cada $s[z\mapsto a]$, que también es una asignación total, y luego se aplica la cláusula de $Q$. Una inducción sobre la profundidad de la dirección contextual prueba la invariancia de cada paso contextual. La simetría de la bicondicional cubre su dirección inversa; la transitividad a lo largo de una cadena finita cubre $\equiv_\alpha$. $\square$

Se ha probado equivalencia **de satisfacción**, no igualdad literal de fórmulas ni identidad de códigos sintácticos bajo sustituciones diferentes.

## 8.14. Sustitución simultánea arbitraria de fórmulas

### Metateorema 8.14.1 — Lema semántico de sustitución global con prevención de captura {#tlog-mth-00030}

Sea $\sigma:X\to\operatorname{Tm}_\tau$ una sustitución de términos **arbitraria**, eventualmente de soporte infinito, y sea $\mathcal S_\sigma:\operatorname{Fm}_\tau\to\operatorname{Fm}_\tau$ la sustitución simultánea total sin captura del §6.30. Para toda $\tau$-estructura $\mathfrak A$, asignación $s:X\to A$ y fórmula $\varphi$,

$$
\boxed{\mathfrak A,s\models_\tau \mathcal S_\sigma(\varphi)
\quad\Longleftrightarrow\quad
\mathfrak A,s^\sigma\models_\tau\varphi,\qquad
s^\sigma(u)=\llbracket\sigma(u)\rrbracket_{\mathfrak A,s}.}
$$

**Demostración.** Inducimos sobre el rango sintáctico $\operatorname{rk}_\tau(\varphi)$, para **todas** las sustituciones $\sigma$ y asignaciones $s$ simultáneamente. Este fortalecimiento permite aplicar la hipótesis inductiva después de sobrescribir una entrada de $\sigma$ y, cuando haga falta, renombrar una variable ligada. En los átomos, la igualdad de las denotaciones de sus términos argumentos proviene del lema de sustitución de términos [TLOG-MTH-00024](capitulo-07.md#tlog-mth-00024); en una ecuación las dos igualdades se comparan en $A$, y en una relación los dos lados prueban la pertenencia de la misma tupla a $R^{\mathfrak A}$. Para relaciones nularias se compara sólo $()\in R^{\mathfrak A}$. Las conectivas se resuelven por las hipótesis inductivas y las cláusulas booleanas.

Consideremos ahora $\varphi=Qy\,\psi$, donde $Q\in\{\forall,\exists\}$, y escribamos

$$
C_\sigma(\psi;y)
:=\bigcup_{u\in\operatorname{FV}(\psi)\setminus\{y\}}
\operatorname{Var}(\sigma(u)).
$$

**Caso 1: $y\notin C_\sigma(\psi;y)$.** Por §6.30,
$\mathcal S_\sigma(Qy\,\psi)=Qy\,\mathcal S_{\sigma_{[y]}}(\psi)$. Para cada $a\in A$, la hipótesis inductiva da

$$
\mathfrak A,s[y\mapsto a]\models_\tau\mathcal S_{\sigma_{[y]}}(\psi)
\iff
\mathfrak A,(s[y\mapsto a])^{\sigma_{[y]}}\models_\tau\psi.
$$

Como $y\notin C_\sigma(\psi;y)$, el lema 8.10.1, aplicado a $Z=\operatorname{FV}(\psi)$, establece que esta última asignación coincide **sobre $\operatorname{FV}(\psi)$** con $(s^\sigma)[y\mapsto a]$. Por el lema de localidad 8.5.1, ambas satisfacen $\psi$ exactamente en los mismos casos. Cuantificar sobre $a\in A$ permite recuperar la cláusula original para $Qy\,\psi$ bajo $s^\sigma$.

**Caso 2: $y\in C_\sigma(\psi;y)$.** El procedimiento sintáctico fija un único

$$
z=\operatorname{fresh}\bigl(\operatorname{Names}(\psi)
\cup C_\sigma(\psi;y)\cup\{y\}\bigr).
$$

En particular, $z\ne y$, $z\notin\operatorname{Names}(\psi)$ y $z\notin C_\sigma(\psi;y)$. Pongamos $\psi':=\psi[z/y]_{\mathrm{lit}}$, que está definida por la condición de frescura y tiene $\operatorname{rk}(\psi')=\operatorname{rk}(\psi)<\operatorname{rk}(Qy\,\psi)$. Por §6.30,

$$
\mathcal S_\sigma(Qy\,\psi)
=Qz\,\mathcal S_{\sigma_{[z]}}(\psi').
$$

Para cada $a\in A$, sea $r_a:=(s[z\mapsto a])^{\sigma_{[z]}}$. Por hipótesis inductiva (aplicada ahora a $\psi'$ y $\sigma_{[z]}$) y por el lema de sustitución **literal segura** de §8.11, respectivamente,

$$
\begin{aligned}
\mathfrak A,s[z\mapsto a]\models_\tau
\mathcal S_{\sigma_{[z]}}(\psi')
&\iff\mathfrak A,r_a\models_\tau\psi'\\
&\iff\mathfrak A,r_a[y\mapsto r_a(z)]\models_\tau\psi\\
&\iff\mathfrak A,r_a[y\mapsto a]\models_\tau\psi.
\end{aligned}
$$

La última línea usa $r_a(z)=\llbracket z\rrbracket_{\mathfrak A,s[z\mapsto a]}=a$. Finalmente, $r_a[y\mapsto a]$ y $(s^\sigma)[y\mapsto a]$ **coinciden en $\operatorname{FV}(\psi)$**: en $y$ ambas valen $a$; para $u\in\operatorname{FV}(\psi)\setminus\{y\}$, se tiene $u\ne z$, pues $z\notin\operatorname{Names}(\psi)$, y entonces

$$
r_a(u)=\llbracket\sigma(u)\rrbracket_{\mathfrak A,s[z\mapsto a]}
=\llbracket\sigma(u)\rrbracket_{\mathfrak A,s}=s^\sigma(u),
$$

ya que $z\notin C_\sigma(\psi;y)$ implica $z\notin\operatorname{Var}(\sigma(u))$ y permite usar la localidad de términos. La localidad semántica de $\psi$ hace equivalentes las dos últimas valoraciones; la cuantificación por $Q$ concluye la prueba. **Ningún paso exige que $\sigma$ tenga soporte finito**: todos los conjuntos inspeccionados para elegir $z$ se obtienen de las variables libres, siempre finitas, de $\psi$. $\square$

El enunciado controla la *semántica de una sustitución sintáctica*, no una regla de inferencia del cálculo objeto. En particular, no afirma $\Gamma\vdash_\tau\varphi$.

## 8.15. Sustitución simple total: una consecuencia exacta

### Corolario 8.15.1 — Interpretación de la sustitución $\operatorname{CA}_{x,t}$ {#tlog-cor-00007}

Para cualesquiera $x\in X$, $t\in\operatorname{Tm}_\tau$, $\varphi\in\operatorname{Fm}_\tau$, $\mathfrak A$ y $s$, aun cuando $\operatorname{FreeFor}_\tau(t,x,\varphi)$ **no** se cumpla,

$$
\boxed{\mathfrak A,s\models_\tau\operatorname{CA}_{x,t}(\varphi)
\iff
\mathfrak A,s[x\mapsto\llbracket t\rrbracket_{\mathfrak A,s}]\models_\tau\varphi.}
$$

**Demostración.** La identidad sintáctica literal $\mathcal S_{\sigma_{x,t}}(\varphi)=\operatorname{CA}_{x,t}(\varphi)$ fue probada en [TLOG-LEM-00015](capitulo-06.md#tlog-lem-00015). En el teorema 8.14.1 especializamos $\sigma=\sigma_{x,t}$ y usamos la identidad de asignaciones $s^{\sigma_{x,t}}=s[x\mapsto\llbracket t\rrbracket_{\mathfrak A,s}]$, establecida por [TLOG-MTH-00024](capitulo-07.md#tlog-mth-00024). Se obtiene la bicondicional. Cuando además `FreeFor` vale, [TLOG-MTH-00019](capitulo-06.md#tlog-mth-00019) identifica $\operatorname{CA}_{x,t}(\varphi)$ con $\varphi[t/x]_{\mathrm{lit}}$ **literalmente**, y recuperamos §8.11. $\square$

## 8.16. La satisfacción no ve los símbolos olvidados

### Metateorema 8.16.1 — Invariancia de satisfacción al tomar reductos {#tlog-mth-00031}

Si $\tau\subseteq\tau'$, $\mathfrak B$ es una $\tau'$-estructura de universo $B$, $\mathfrak A:=\mathfrak B\!\upharpoonright_\tau$ y $\varphi\in\operatorname{Fm}_\tau$, entonces para toda asignación $s:X\to B$:

$$
\boxed{\mathfrak A,s\models_\tau\varphi
\quad\Longleftrightarrow\quad
\mathfrak B,s\models_{\tau'}\varphi.}
$$

Para $\varphi\in\operatorname{Sent}_\tau$, la consecuencia correspondiente es $\mathfrak A\models_\tau\varphi\iff\mathfrak B\models_{\tau'}\varphi$.

**Demostración.** El lema sintáctico [TLOG-LEM-00018](capitulo-07.md#tlog-lem-00018) garantiza que $\varphi$ se forma literalmente igual en ambas firmas, con las mismas aridades, variables y declaraciones. Inducimos sobre $\varphi$. En los átomos, [TLOG-MTH-00025](capitulo-07.md#tlog-mth-00025) identifica el valor de cada término de $\tau$ bajo $(\mathfrak A,s)$ y $(\mathfrak B,s)$. El reducto interpreta cada relación de $\tau$ por **el mismo subconjunto de $B^n$**; la ecuación de igualdad lógica consulta identidad sobre el mismo $B$. Por ello coinciden las cláusulas atómicas, incluido $n=0$. Los cinco conectivos conservan su condición booleana por hipótesis inductiva. Si $\varphi=Qx\,\psi$, el universo de ambas estructuras es **el mismo**, por lo que se consideran las mismas actualizaciones $s[x\mapsto b]$ para los mismos $b\in B$. Aplicando la hipótesis inductiva para cada actualización, coinciden las condiciones universal y existencial. La verdad de una sentencia resulta de §8.6 y la identidad para todas las asignaciones. $\square$

**Límite.** Esta invariancia exige que las fórmulas no contengan símbolos extralógicos olvidados. Una fórmula de $\tau'\setminus\tau$ no es, en general, una fórmula bien formada de $\tau$; no existe entonces juicio $\mathfrak A,s\models_\tau\varphi$ al que aplicar el enunciado.

## 8.17. El isomorfismo transporta la satisfacción completa

### Metateorema 8.17.1 — Invariancia bajo isomorfismos de estructuras {#tlog-mth-00032}

Sea $h:\mathfrak A\to\mathfrak B$ un **isomorfismo** entre $\tau$-estructuras de universos $A$ y $B$. Para toda fórmula $\varphi\in\operatorname{Fm}_\tau$ y asignación $s:X\to A$:

$$
\boxed{\mathfrak A,s\models_\tau\varphi
\quad\Longleftrightarrow\quad
\mathfrak B,h\circ s\models_\tau\varphi.}
$$

En particular, para cualquier sentencia $\chi$, $\mathfrak A\models_\tau\chi\iff\mathfrak B\models_\tau\chi$.

**Demostración.** Inducción estructural sobre $\varphi$. Para $\operatorname{Eq}(t,u)$, la naturalidad de la evaluación de términos ([TLOG-MTH-00026](capitulo-07.md#tlog-mth-00026)) da $\llbracket t\rrbracket_{\mathfrak B,h\circ s}=h(\llbracket t\rrbracket_{\mathfrak A,s})$, y análogamente para $u$. Como $h$ es **inyectiva**, dos valores son iguales si y sólo si sus imágenes lo son. En un átomo $R(t_1,\ldots,t_n)$, la misma naturalidad relaciona las tuplas de argumentos; la condición **bicondicional** sobre relaciones de un embedding refleja y preserva su pertenencia. También para $n=0$, la tupla vacía es enviada a sí misma y el predicado nulario se refleja.

Las cinco conectivas se preservan porque sus cláusulas actúan sólo sobre los valores booleanos de fórmulas ya comparadas. Si $\varphi=Qx\,\psi$, la hipótesis inductiva aplicada a cualquier $a\in A$ produce

$$
\mathfrak A,s[x\mapsto a]\models_\tau\psi
\iff
\mathfrak B,h\circ(s[x\mapsto a])\models_\tau\psi
\iff
\mathfrak B,(h\circ s)[x\mapsto h(a)]\models_\tau\psi,
$$

por la conmutación entre $h$ y las actualizaciones ([TLOG-MTH-00026](capitulo-07.md#tlog-mth-00026)). Como $h:A\to B$ es **biyectiva**, $\{h(a):a\in A\}=B$. Por ello las cuantificaciones $\forall a\in A$ y $\forall b\in B$, así como las existenciales respectivas, tienen las mismas condiciones de verdad. La sobreyectividad sólo interviene al cubrir **todos** los valores cuantificados de $B$; no se ha supuesto elección de preimágenes simultáneas. Para la afirmación sobre sentencias usamos independencia de asignación (§8.6) en ambos universos y el hecho de que las asignaciones existen. $\square$

**Contracontrol.** Un homomorfismo arbitrario puede no reflejar ni la igualdad ni las relaciones; un embedding que no es sobreyectivo tampoco compara automáticamente todos los testigos cuantificados del codominio. Por tanto, el metateorema no debe atribuirse a esas clases de aplicaciones.

## 8.18. Fórmulas sin cuantificadores

### Definición 8.18.1 — Fragmento libre de cuantificadores {#tlog-def-00046}

Llamaremos $\operatorname{QF}_\tau$ al conjunto de fórmulas $\varphi\in\operatorname{Fm}_\tau$ cuyo árbol de análisis no contiene nodos $\operatorname{Quant}_{\forall,x}$ ni $\operatorname{Quant}_{\exists,x}$. Equivalentemente, es la menor colección que contiene todos los átomos $\operatorname{At}_\tau$ y es cerrada bajo negación y bajo los cuatro conectivos binarios. Es un **conjunto**, obtenido por separación en $\operatorname{Fm}_\tau$. Esta restricción es **sintáctica**: no afirma que otras fórmulas sean o no equivalentes a alguna fórmula de este fragmento.

## 8.19. Lo que preservan los embeddings sin sobreyectividad

### Proposición 8.19.1 — Satisfacción de fórmulas sin cuantificadores bajo embeddings {#tlog-pro-00013}

Si $h:\mathfrak A\hookrightarrow\mathfrak B$ es un **embedding** de $\tau$-estructuras y $\varphi\in\operatorname{QF}_\tau$, entonces para toda asignación $s:X\to A$,

$$
\boxed{\mathfrak A,s\models_\tau\varphi
\quad\Longleftrightarrow\quad
\mathfrak B,h\circ s\models_\tau\varphi.}
$$

**Demostración.** Inducción sobre la construcción de $\operatorname{QF}_\tau$. Para ecuaciones, la naturalidad de términos y la inyectividad de $h$ dan equivalencia de identidades. Para relaciones, la naturalidad de las tuplas y la preservación **y reflexión** de $R$ por el embedding dan equivalencia de pertenencia, incluida la aridad cero. La negación y los cuatro conectivos binarios transportan esta equivalencia por sus operaciones booleanas. No aparece ningún caso cuantificador, pues ninguna fórmula del fragmento contiene uno. La sobreyectividad de $h$ no se ha usado. $\square$

La conclusión **no se extiende** sin más a fórmulas cuantificadas. En la signatura vacía, la inclusión $\{0\}\hookrightarrow\{0,1\}$ es un embedding. Sin embargo, la sentencia $\forall x\,\forall y\,(x\doteq y)$ es verdadera en el universo unitario y falsa en el de dos elementos, mientras que $\exists x\,\exists y\,\neg(x\doteq y)$ es falsa en el primero y verdadera en el segundo. La diferencia proviene exclusivamente del dominio recorrido por los cuantificadores, no de la interpretación de símbolos extralógicos.

## 8.20. Tres controles que impiden extrapolaciones

**Captura de variables.** Sea $\varphi=\forall y\,P(x)$, con $P\in R_1$, y sustituyamos la variable libre $x$ por el término $y$. La sustitución literal ingenua escribiría $\forall y\,P(y)$, donde $y$ queda capturada. La sustitución total del §6.25 produce, con $z$ fresca, $\forall z\,P(y)$. Para $A=\{0,1\}$, $P^{\mathfrak A}=\{0\}$, $s(y)=0$, la fórmula correcta es verdadera y la ingenua falsa: se observa por qué §8.15 necesita la política de frescura. En este ejemplo $s(x)$ puede ser cualquier elemento del dominio.

**Homomorfismo frente a embedding.** Para $P\in R_1$, sean $A=B=\{0\}$, $P^{\mathfrak A}=\varnothing$, $P^{\mathfrak B}=\{0\}$ y $h=\operatorname{id}$. La aplicación es un homomorfismo y no un embedding: $\neg P(x)$ es satisfecha en $\mathfrak A$ y no en $\mathfrak B$. Para la igualdad, el colapso de dos elementos de $A$ en uno de $B$ muestra por separado que un homomorfismo no inyectivo puede destruir $\neg(x\doteq y)$.

**Firma frente a universo.** Un reducto conserva el dominio completo y el significado de los símbolos retenidos (§8.16). Una subestructura cambia el universo, por lo que sólo las fórmulas sin cuantificadores tienen en general la garantía bicondicional de §8.19. Ni una expansión ni una subestructura deben confundirse con una transformación de la sintaxis $\operatorname{CA}_{x,t}$.

## 8.21. Cierre local y frontera del siguiente microtramo

Los resultados §§8.10–8.19 resuelven la semántica de sustituciones simples y simultáneas, con aridad cero, variables ligadas, renombrado alfa, reductos e isomorfismos. La demostración de §8.14 cubre sustituciones de **soporte infinito** y no confunde igualdad de asignaciones con acuerdo sobre variables libres. No se ha introducido ningún cálculo de prueba de primer orden.

Permanece pendiente para el Capítulo 8 definir, con tipos y dominios precisos, la satisfacción de **conjuntos** de fórmulas, los modelos de teorías, la consecuencia y la validez de primer orden, y las propiedades deductivo-semánticas elementales de estas nociones. Las afirmaciones de invariancia probadas aquí no son un teorema de completitud ni presuponen la derivabilidad objeto.

```text
TLOG-CH08-M01 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH08-M02 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH08-0001 = PARTIAL-CLOSURE / NOT CLOSED
new mathematical nodes = 10
chapter 8 closed nodes = 17
TLOG registered/closed nodes = 131/131
DAG = 131 nodes / 338 direct edges / acyclic PASS (local QA)
external interfaces = 0
formalization candidates = 39
Lean compiled/verified = 0
chapters closed = 8/24 (33.3%)
PART I = CLOSED / PASS
PART II = OPEN
```

**Próximo microtramo:** `TLOG-CH08-M03 — Satisfacción de conjuntos, modelos, validez y consecuencia de primer orden`.

### Vector de progreso — `CH08-M02`

```text
LOCAL  CH08-M02 ██████████ 100 % (10/10 resultados revisados)
GLOBAL TLOG     ████████░░░░░░░░░░░░░░░░ 8/24 capítulos (33,3 %)
```

La barra global utiliza el número de capítulos completamente cerrados y no extrapola un porcentaje de nodos a toda la obra.

## 8.22. De fórmulas individuales a conjuntos de premisas

El juicio de §8.4 tiene como argumentos una estructura, una asignación y **una fórmula**. Una familia de premisas no es una fórmula adicional del lenguaje objeto: por regla general, no existe una conjunción infinita de sus miembros dentro de $\operatorname{Fm}_\tau$. Para interpretar una familia se cuantificará metateóricamente sobre sus elementos. Esta decisión permite tratar conjuntos de premisas de cardinalidad arbitraria sin introducir conectivos infinitarios ni presupuestos de enumerabilidad.

### Definición 8.22.1 — Satisfacción simultánea y asignaciones realizadoras {#tlog-def-00047}

Sean $\Gamma\subseteq\operatorname{Fm}_\tau$ un **conjunto** de fórmulas, $\mathfrak A$ una $\tau$-estructura de universo $A\ne\varnothing$ y $s:X\to A$ una asignación total. Definimos

$$
\boxed{\mathfrak A,s\models_\tau\Gamma
\quad:\Longleftrightarrow\quad
(\forall\gamma\in\Gamma)\;\mathfrak A,s\models_\tau\gamma.}
$$

Para la estructura fija, el **conjunto de asignaciones realizadoras** de $\Gamma$ es

$$
\operatorname{Sat}_{\mathfrak A}(\Gamma)
:=\{s\in A^X:(\forall\gamma\in\Gamma)\;\mathfrak A,s\models_\tau\gamma\}.
$$

La expresión es un subconjunto bien definido de $A^X$ por separación en ZF. El parámetro $\Gamma$ puede ser infinito; la condición $\forall\gamma\in\Gamma$ pertenece al **metalenguaje** y no crea una fórmula de longitud infinita. La familia vacía se satisface vacuamente:

$$
\mathfrak A,s\models_\tau\varnothing\quad\text{para todo }s,
\qquad \operatorname{Sat}_{\mathfrak A}(\varnothing)=A^X.
$$

::: {.callout-note}
## Lectura exacta

Una estructura y una asignación que satisfacen $\Gamma$ deben satisfacer **todos sus miembros bajo la misma asignación**. No basta que cada fórmula tenga alguna asignación realizadora posiblemente diferente.
:::

## 8.23. Intersección, monotonía y soporte libre

### Lema 8.23.1 — Álgebra y localidad de los conjuntos de asignaciones {#tlog-lem-00022}

Para cualesquiera $\Gamma,\Delta\subseteq\operatorname{Fm}_\tau$,

$$
\begin{aligned}
\operatorname{Sat}_{\mathfrak A}(\Gamma\cup\Delta)
&=\operatorname{Sat}_{\mathfrak A}(\Gamma)
  \cap\operatorname{Sat}_{\mathfrak A}(\Delta),\\
\Gamma\subseteq\Delta\quad&\Longrightarrow\quad
\operatorname{Sat}_{\mathfrak A}(\Delta)
\subseteq\operatorname{Sat}_{\mathfrak A}(\Gamma),\\
\operatorname{Sat}_{\mathfrak A}(\Gamma)
&=\bigcap_{\gamma\in\Gamma}\operatorname{Sat}_{\mathfrak A}(\{\gamma\}),
\end{aligned}
$$

con la convención de que la intersección de la familia vacía de subconjuntos de $A^X$ es $A^X$. Si $\operatorname{FV}(\Gamma):=\bigcup_{\gamma\in\Gamma}\operatorname{FV}_\tau(\gamma)$ y dos asignaciones $s,r$ coinciden en $\operatorname{FV}(\Gamma)$, entonces

$$
s\in\operatorname{Sat}_{\mathfrak A}(\Gamma)
\iff r\in\operatorname{Sat}_{\mathfrak A}(\Gamma).
$$

**Demostración.** La primera identidad resulta al desplegar la cuantificación sobre $\Gamma\cup\Delta$: satisfacer cada uno de sus miembros equivale a satisfacer los dos conjuntos. Para la segunda, si una asignación satisface cada fórmula de $\Delta$, satisface las del subconjunto $\Gamma$. La tercera igualdad expresa el mismo criterio miembro por miembro; las intersecciones son intersecciones de subconjuntos del conjunto fijo $A^X$. Finalmente, si $s$ y $r$ coinciden en la unión de variables libres, coinciden en $\operatorname{FV}(\gamma)$ para cada $\gamma\in\Gamma$. El lema [TLOG-LEM-00019](#tlog-lem-00019) da equivalencia de satisfacción de cada miembro bajo ambas asignaciones, y la cuantificación sobre $\Gamma$ concluye la prueba. $\square$

La unión $\operatorname{FV}(\Gamma)$ es un **conjunto**, por reemplazo y unión en ZF, pero no tiene por qué ser finita cuando $\Gamma$ es infinito. No se infiere una tabla de verdad finita para $\Gamma$.

## 8.24. Modelos, satisfacibilidad y tamaño de las colecciones

### Definición 8.24.1 — Modelo de un conjunto de sentencias y satisfacibilidad {#tlog-def-00048}

Una colección $\Gamma\subseteq\operatorname{Fm}_\tau$ es **satisfacible** si existen una $\tau$-estructura $\mathfrak A$ de universo no vacío y una asignación $s:X\to A$ tales que $\mathfrak A,s\models_\tau\Gamma$. En caso contrario se llama **insatisfacible**. Para una fórmula aislada se emplea la misma terminología aplicada a su conjunto unitario.

Cuando $S\subseteq\operatorname{Sent}_\tau$ consta enteramente de **sentencias**, definimos

$$
\boxed{\mathfrak A\models_\tau S
\quad:\Longleftrightarrow\quad
(\forall\sigma\in S)\;\mathfrak A\models_\tau\sigma.}
$$

Una $\tau$-estructura que cumple esta condición es un **modelo** de $S$. La notación $\operatorname{Mod}_\tau(S)$ designa la **clase definible** de dichas estructuras, no un conjunto que la metateoría asegure existente. Para $S$ de sentencias, $\operatorname{Mod}_\tau(S)$ es no vacía si y sólo si $S$ es satisfacible en el sentido anterior; la justificación figura en §8.25.

No definimos $\mathfrak A\models_\tau\Gamma$ sin aclaración cuando $\Gamma$ contenga fórmulas abiertas; su tratamiento por cuantificación sobre **todas** las asignaciones se fijará expresamente en §8.30. Aquí la palabra «modelo», sin calificador, corresponde a una **estructura que satisface sentencias**, mientras que $(\mathfrak A,s)$ satisface conjuntos arbitrarios de fórmulas.

## 8.25. Modelos de teorías y clases propias

### Proposición 8.25.1 — Independencia de asignación y naturaleza de la clase de modelos {#tlog-pro-00014}

Sean $S,T\subseteq\operatorname{Sent}_\tau$. Se cumplen las siguientes propiedades:

1. $S$ es satisfacible si y sólo si $\operatorname{Mod}_\tau(S)$ contiene alguna estructura.
2. Para cada estructura $\mathfrak A$, $\operatorname{Sat}_{\mathfrak A}(S)$ es **todo** $A^X$ o es $\varnothing$. En el primer caso $\mathfrak A\models_\tau S$, y en el segundo no.
3. Si $S\subseteq T$, entonces $\operatorname{Mod}_\tau(T)\subseteq\operatorname{Mod}_\tau(S)$, como inclusión de clases definibles.
4. Si $S$ tiene un modelo, $\operatorname{Mod}_\tau(S)$ es una **clase propia** en ZF: no puede ser un conjunto.

**Demostración.** Para la segunda afirmación, el corolario de §8.6 hace independiente de la asignación la satisfacción de cada sentencia. Como $A^X\ne\varnothing$, o todas las asignaciones satisfacen cada miembro de $S$, o al menos una sentencia es falsa bajo todas ellas. Esto demuestra la dicotomía. La primera afirmación es ahora inmediata: si alguna $(\mathfrak A,s)$ satisface $S$, la constancia fuerza $\mathfrak A\models_\tau S$; a la inversa, un modelo admite una asignación constante porque $A\ne\varnothing$. La tercera afirmación procede de la cuantificación universal sobre los miembros de los conjuntos.

Para probar la cuarta, fijemos **un** modelo $\mathfrak A$ de $S$ y un único $a_0\in A$. Para todo conjunto $z$, el conjunto $A_z:=A\times\{z\}$ es equipotente a $A$ mediante $a\mapsto(a,z)$. Transportando las interpretaciones de $\mathfrak A$ por esa biyección obtenemos una $\tau$-estructura $\mathfrak A_z$ sobre $A_z$; la invariancia por isomorfismo de [TLOG-MTH-00032](#tlog-mth-00032) prueba que $\mathfrak A_z\models_\tau S$. Todas estas construcciones son uniformes en $z$, y no constituyen elecciones independientes.

Si la clase de todos los modelos fuera un conjunto $K$, la unión de los universos de sus miembros sería un conjunto $U$ por reemplazo y unión. Para **todo** conjunto $z$, tendríamos $(a_0,z)\in A_z\subseteq U$. Por separación, el subconjunto $\{u\in U:(\exists z)\;u=(a_0,z)\}$ sería un conjunto; mediante reemplazo y segunda proyección obtendríamos el conjunto de **todos los conjuntos** $z$, contradicción con ZF. Luego la clase de modelos, cuando no es vacía, es propia. $\square$

::: {.callout-important}
## Control fundacional

Las expresiones $\operatorname{Mod}_\tau(S)$ y «para toda estructura» se entienden como abreviaciones de fórmulas metateóricas con una variable de estructura. No se realiza una unión o intersección conjuntista sobre la clase propia de todas las estructuras.
:::

## 8.26. Consecuencia y validez de primer orden

### Definición 8.26.1 — Consecuencia local, validez y equivalencia semántica {#tlog-def-00049}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\varphi\in\operatorname{Fm}_\tau$, definimos la **consecuencia semántica local de primer orden** por

$$
\boxed{\Gamma\models_\tau\varphi
\iff
(\forall\tau\text{-estructuras }\mathfrak A)(\forall s:X\to A)
\bigl(\mathfrak A,s\models_\tau\Gamma\Rightarrow
\mathfrak A,s\models_\tau\varphi\bigr).}
$$

El calificativo «local» indica que **la misma asignación** se usa para todas las premisas y para la conclusión. Los cuantificadores metateóricos recorren todos los conjuntos $A\ne\varnothing$ dotados de las interpretaciones correspondientes; no forman un conjunto de estructuras.

Definimos también:

$$
\begin{aligned}
\models_\tau\varphi
&\iff (\forall\mathfrak A)(\forall s:X\to A)\;
\mathfrak A,s\models_\tau\varphi,
\qquad\text{(validez general)}\\
\varphi\equiv^{\mathrm{sem}}_\tau\psi
&\iff(\forall\mathfrak A)(\forall s:X\to A)
\bigl(\mathfrak A,s\models_\tau\varphi
\leftrightarrow\mathfrak A,s\models_\tau\psi\bigr).
\end{aligned}
$$

La equivalencia semántica $\equiv^{\mathrm{sem}}_\tau$ no es ni igualdad literal de árboles, ni equivalencia alfa $\equiv_\alpha$, ni derivabilidad $\vdash$. La notación $\models_\tau\varphi$ **no** lleva estructura ni asignación porque expresa una cuantificación metateórica general; la verdad $\mathfrak A\models_\tau\sigma$ de una sentencia en una estructura fija es otro juicio.

## 8.27. Contramodelos y caracterizaciones fundamentales

### Proposición 8.27.1 — Consecuencia, negación, validez y sentencias {#tlog-pro-00015}

Para $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\varphi,\psi\in\operatorname{Fm}_\tau$:

$$
\begin{aligned}
\Gamma\models_\tau\varphi
&\iff \Gamma\cup\{\neg\varphi\}\text{ es insatisfacible},\\
\models_\tau\varphi
&\iff\varnothing\models_\tau\varphi
\iff\{\neg\varphi\}\text{ es insatisfacible},\\
\varphi\equiv^{\mathrm{sem}}_\tau\psi
&\iff (\varphi\models_\tau\psi\ \text{y}\ \psi\models_\tau\varphi)
\iff\models_\tau(\varphi\leftrightarrow\psi).
\end{aligned}
$$

En la tercera línea $\varphi\models_\tau\psi$ abrevia $\{\varphi\}\models_\tau\psi$. Si $S\subseteq\operatorname{Sent}_\tau$ y $\chi\in\operatorname{Sent}_\tau$, entonces

$$
\boxed{S\models_\tau\chi
\iff(\forall\mathfrak A\in\operatorname{Mod}_\tau(S))\;
\mathfrak A\models_\tau\chi,}
$$

entendiendo el cuantificador del segundo miembro como abreviación de una implicación metateórica, no como cuantificación acotada sobre un conjunto existente.

**Demostración.** La negación satisface $\mathfrak A,s\models_\tau\neg\varphi$ exactamente cuando no se cumple $\mathfrak A,s\models_\tau\varphi$. Así, un testigo $(\mathfrak A,s)$ de la satisfacibilidad de $\Gamma\cup\{\neg\varphi\}$ es precisamente un **contramodelo con asignación** de $\Gamma\models_\tau\varphi$; la primera equivalencia es su negación clásica. La segunda especializa la primera a premisas vacías y utiliza que la condición de antecedente es universalmente verdadera para $\varnothing$. En la tercera, la implicación puntual de $\varphi$ a $\psi$ en todas las parejas estructura-asignación, junto con la inversa, equivale a igualdad de los dos valores de verdad, que es la cláusula de $\leftrightarrow$. Finalmente, para sentencias las cláusulas de §8.6 hacen independientes de $s$ todas las premisas y la conclusión. Dado un universo no vacío existe al menos una asignación; por ello cuantificar sobre todas las asignaciones equivale a cuantificar sobre las estructuras que son modelos de $S$. $\square$

El caso **insatisfacible** no es una excepción: si $\Gamma$ no tiene ninguna pareja $(\mathfrak A,s)$ realizadora, entonces $\Gamma\models_\tau\varphi$ para toda conclusión $\varphi$ por verdad vacua de la implicación metateórica. Esta afirmación no invoca un principio deductivo objeto de explosión.

## 8.28. Propiedades estructurales de la consecuencia

### Proposición 8.28.1 — Reflexividad, monotonía y corte semántico {#tlog-pro-00016}

Si $\Gamma,\Delta,\Lambda\subseteq\operatorname{Fm}_\tau$ y $\varphi\in\operatorname{Fm}_\tau$, se cumplen:

1. **Reflexividad:** si $\varphi\in\Gamma$, entonces $\Gamma\models_\tau\varphi$.
2. **Monotonía:** si $\Gamma\subseteq\Delta$ y $\Gamma\models_\tau\varphi$, entonces $\Delta\models_\tau\varphi$.
3. **Corte:** si $\Gamma\models_\tau\delta$ para cada $\delta\in\Delta$ y $\Gamma\cup\Delta\models_\tau\varphi$, entonces $\Gamma\models_\tau\varphi$.
4. **Transitividad de la consecuencia colectiva:** si $\Gamma\models_\tau\delta$ para toda $\delta\in\Delta$ y $\Delta\models_\tau\varphi$, entonces $\Gamma\models_\tau\varphi$.

**Demostración.** Sea $(\mathfrak A,s)$ arbitraria y supongamos que satisface las premisas situadas a la izquierda de cada condición. En (1), satisface en particular $\varphi$, que pertenece a $\Gamma$. En (2), satisfacer $\Delta$ implica satisfacer $\Gamma$; la hipótesis de consecuencia entrega la conclusión. En (3), la satisfacción de $\Gamma$ y de cada consecuencia $\delta\in\Delta$ muestra que la misma pareja satisface $\Gamma\cup\Delta$; la segunda hipótesis entrega $\varphi$. Para (4), una pareja realizadora de $\Gamma$ satisface $\Delta$ por las hipótesis, y de allí $\varphi$. No se ha elegido ninguna asignación dependiente de una fórmula de $\Delta$: **una sola** pareja arbitraria sirve simultáneamente para todos sus miembros. $\square$

Las pruebas no apelan a completitud ni a compacidad. En particular, no se deduce que un conjunto insatisfacible tenga un subconjunto finito insatisfacible; esa dirección pertenece a un metateorema posterior.

## 8.29. Deducción semántica y cuantificadores

### Proposición 8.29.1 — Implicación interna y generalización con condición lateral {#tlog-pro-00017}

Para cualesquiera $\Gamma\subseteq\operatorname{Fm}_\tau$ y $\alpha,\beta\in\operatorname{Fm}_\tau$ se cumple el **teorema de deducción semántica local**:

$$
\boxed{\Gamma\cup\{\alpha\}\models_\tau\beta
\iff\Gamma\models_\tau(\alpha\to\beta).}
$$

Si $x\notin\operatorname{FV}(\Gamma)$, donde $\operatorname{FV}(\Gamma)=\bigcup_{\gamma\in\Gamma}\operatorname{FV}_\tau(\gamma)$, se tiene asimismo

$$
\boxed{\Gamma\models_\tau\varphi
\iff\Gamma\models_\tau\forall x\,\varphi.}
$$

Finalmente, sin condición lateral, $\Gamma\models_\tau\varphi$ implica $\Gamma\models_\tau\exists x\,\varphi$.

**Demostración.** En la primera equivalencia, fijemos estructura y asignación que satisfacen $\Gamma$. La afirmación de que satisfacer adicionalmente $\alpha$ obliga a satisfacer $\beta$ es, por la cláusula de $\to$ de §8.4, exactamente la satisfacción de $\alpha\to\beta$ bajo esa misma asignación. Como la elección de pareja fue arbitraria, ambas direcciones quedan demostradas.

Para la segunda, supongamos primero $\Gamma\models_\tau\varphi$ y $x\notin\operatorname{FV}(\Gamma)$. Si $\mathfrak A,s\models_\tau\Gamma$, entonces para todo $a\in A$ las asignaciones $s$ y $s[x\mapsto a]$ coinciden sobre $\operatorname{FV}(\Gamma)$, y por la localidad de §8.23 también $\mathfrak A,s[x\mapsto a]\models_\tau\Gamma$. La consecuencia inicial aplicada **a cada actualización** entrega $\mathfrak A,s[x\mapsto a]\models_\tau\varphi$. La cláusula universal prueba $\mathfrak A,s\models_\tau\forall x\varphi$. Recíprocamente, si $\Gamma\models_\tau\forall x\varphi$, toda pareja que satisface $\Gamma$ satisface esa cuantificación; al considerar $a=s(x)\in A$, la actualización $s[x\mapsto s(x)]=s$ demuestra $\mathfrak A,s\models_\tau\varphi$. Esta dirección no exige la condición lateral.

Para la última afirmación, una pareja realizadora de $\Gamma$ satisface $\varphi$; tomando como testigo existencial $a=s(x)$, se satisface $\exists x\varphi$. El universo y la asignación ya existen, sin selección adicional. $\square$

**No puede suprimirse la condición lateral.** Con $\Gamma=\{P(x)\}$, $A=\{0,1\}$, $P^{\mathfrak A}=\{0\}$ y $s(x)=0$, se cumple $\mathfrak A,s\models\Gamma$ pero $\mathfrak A,s\not\models\forall xP(x)$. Por tanto, $P(x)\not\models_\tau\forall xP(x)$. El ejemplo no contradice la independencia de asignación para **sentencias**: $P(x)$ es abierta.

## 8.30. Cierre universal y consecuencia global

### Definición 8.30.1 — Generalización canónica y consecuencia global {#tlog-def-00050}

Toda fórmula $\varphi$ posee un conjunto **finito** $\operatorname{FV}_\tau(\varphi)$. Sean $x_{i_1},\ldots,x_{i_n}$ sus variables libres, enumeradas en el orden creciente de índices. Definimos su **clausura universal**

$$
\varphi^\forall
:=\forall x_{i_1}\cdots\forall x_{i_n}\,\varphi,
\qquad \text{y si }n=0,\quad\varphi^\forall:=\varphi.
$$

El orden fijo de los índices evita elegir un orden de enumeración. Para $\Gamma\subseteq\operatorname{Fm}_\tau$ ponemos $\Gamma^\forall:=\{\gamma^\forall:\gamma\in\Gamma\}\subseteq\operatorname{Sent}_\tau$; esta imagen es un conjunto por reemplazo. La operación forma sentencias **nuevas**, no identifica literalmente $\varphi$ con su clausura.

Para cualquier $\Gamma$, no necesariamente compuesta de sentencias, distinguimos la **satisfacción global por una estructura**

$$
\mathfrak A\models_\tau^{\mathrm g}\Gamma
\iff (\forall s\in A^X)\;\mathfrak A,s\models_\tau\Gamma
$$

y la **consecuencia global**

$$
\Gamma\models_\tau^{\mathrm g}\varphi
\iff (\forall\mathfrak A)
\bigl(\mathfrak A\models_\tau^{\mathrm g}\Gamma
\Rightarrow\mathfrak A\models_\tau^{\mathrm g}\varphi\bigr).
$$

La distinción entre $\models_\tau$ (local) y $\models_\tau^{\mathrm g}$ (global) es obligatoria en TLOG para conjuntos **abiertos**. Si $S\subseteq\operatorname{Sent}_\tau$, la escritura previa $\mathfrak A\models_\tau S$ coincide con $\mathfrak A\models_\tau^{\mathrm g}S$, sin duplicar nociones.

## 8.31. Alcance exacto de la distinción local/global

### Proposición 8.31.1 — Clausura universal y contraejemplo de consecuencia {#tlog-pro-00018}

Para cualquier estructura $\mathfrak A$, conjunto $\Gamma\subseteq\operatorname{Fm}_\tau$ y fórmula $\varphi$,

$$
\begin{aligned}
\mathfrak A\models_\tau^{\mathrm g}\varphi
&\iff\mathfrak A\models_\tau\varphi^\forall,\\
\mathfrak A\models_\tau^{\mathrm g}\Gamma
&\iff\mathfrak A\models_\tau\Gamma^\forall,\\
\Gamma\models_\tau^{\mathrm g}\varphi
&\iff\Gamma^\forall\models_\tau\varphi^\forall.
\end{aligned}
$$

Además, siempre vale

$$
\Gamma\models_\tau\varphi
\quad\Longrightarrow\quad
\Gamma\models_\tau^{\mathrm g}\varphi.
$$

Si todas las premisas de $\Gamma$ son sentencias, entonces vale también la implicación inversa, aunque $\varphi$ sea abierta. **Sin esa condición**, la implicación inversa es falsa.

**Demostración.** Una sucesión finita de cuantificadores universales sobre todas las variables libres de $\varphi$ exige que la matriz sea satisfecha para cualquier tupla de valores en $A^n$, manteniendo fijos los valores de las variables restantes. Por localidad ([TLOG-LEM-00019](#tlog-lem-00019)), éstas no afectan la verdad de la matriz. Toda tupla de $A^n$ aparece como restricción de una asignación total a las variables libres: partiendo de cualquier asignación $s_0\in A^X$, se modifican sus $n$ valores relevantes. A la inversa, cada asignación proporciona una de las tuplas. Así, la satisfacción de $\varphi^\forall$, que es una sentencia, equivale a satisfacción de $\varphi$ bajo **todas** las asignaciones. Para $n=0$ esto es la independencia de asignación ya demostrada. Aplicar la primera equivalencia miembro a miembro prueba la segunda; aplicado a las premisas y conclusión en todas las estructuras entrega la tercera, utilizando además la caracterización para sentencias de §8.27.

Si $\Gamma\models_\tau\varphi$ y $\mathfrak A\models_\tau^{\mathrm g}\Gamma$, toda asignación de esa estructura satisface $\Gamma$; por consecuencia local, toda asignación satisface $\varphi$. Esto prueba la implicación. Si $\Gamma\subseteq\operatorname{Sent}_\tau$, satisfacer $\Gamma$ bajo una asignación equivale a satisfacerla bajo todas por §8.6. Por ello la hipótesis de consecuencia global produce la conclusión para la asignación inicialmente fijada, y ambas consecuencias coinciden.

Para el contraejemplo, en el lenguaje con relación unaria $P$ tomemos $\Gamma=\{P(x)\}$ y $\varphi=\forall x\,P(x)$. Toda estructura que satisface **globalmente** $P(x)$ interpreta $P$ como todo su universo y, por tanto, satisface globalmente $\varphi$. Luego $\Gamma\models_\tau^{\mathrm g}\varphi$. Pero en $A=\{0,1\}$, con $P^{\mathfrak A}=\{0\}$ y una asignación $s(x)=0$, $\mathfrak A,s\models_\tau\Gamma$ mientras $\mathfrak A,s\not\models_\tau\forall xP(x)$. Luego $\Gamma\not\models_\tau\varphi$. $\square$

No se transporta, por simple cambio de símbolo, el teorema de deducción semántica local a la consecuencia global: el mismo ejemplo haría verdadera $P(x)\models_\tau^{\mathrm g}\forall xP(x)$, pero falsa la validez general de $P(x)\to\forall xP(x)$.

## 8.32. Teorías semánticas y clausura de consecuencias

### Definición 8.32.1 — Teoría de una estructura y clausura semántica de sentencias {#tlog-def-00051}

Para una $\tau$-estructura fija $\mathfrak A$ definimos su **teoría de sentencias**

$$
\operatorname{Th}_\tau(\mathfrak A)
:=\{\sigma\in\operatorname{Sent}_\tau:\mathfrak A\models_\tau\sigma\}.
$$

Para $S\subseteq\operatorname{Sent}_\tau$, definimos su **clausura semántica**

$$
\operatorname{Cn}^{\mathrm{sem}}_\tau(S)
:=\{\sigma\in\operatorname{Sent}_\tau:S\models_\tau\sigma\}.
$$

Ambas son **conjuntos** por separación en el conjunto previamente construido $\operatorname{Sent}_\tau$; en la segunda se cuantifica metateóricamente sobre estructuras, pero no se necesita ni se presupone que éstas formen un conjunto. Llamaremos **teoría semánticamente cerrada** a un conjunto $T\subseteq\operatorname{Sent}_\tau$ que satisface $T=\operatorname{Cn}^{\mathrm{sem}}_\tau(T)$. Un conjunto arbitrario $S\subseteq\operatorname{Sent}_\tau$ es, mientras tanto, un **conjunto de axiomas** que puede generar dicha teoría.

Esta distinción terminológica separa «axiomas» de «todas sus consecuencias». No define $\vdash$, pues el cálculo de primer orden corresponderá al Capítulo 9. La notación $\operatorname{Th}_\tau(\mathfrak A)$ no supone que la estructura $\mathfrak A$ sea un conjunto de sentencias.

## 8.33. La clausura semántica es un operador de clausura

### Proposición 8.33.1 — Extensividad, monotonía, idempotencia y modelos invariantes {#tlog-pro-00019}

Para $S,T\subseteq\operatorname{Sent}_\tau$ se cumplen

$$
\begin{aligned}
S&\subseteq\operatorname{Cn}^{\mathrm{sem}}_\tau(S),\\
S\subseteq T&\Longrightarrow
\operatorname{Cn}^{\mathrm{sem}}_\tau(S)
\subseteq\operatorname{Cn}^{\mathrm{sem}}_\tau(T),\\
\operatorname{Cn}^{\mathrm{sem}}_\tau
(\operatorname{Cn}^{\mathrm{sem}}_\tau(S))
&=\operatorname{Cn}^{\mathrm{sem}}_\tau(S),\\
\operatorname{Mod}_\tau(\operatorname{Cn}^{\mathrm{sem}}_\tau(S))
&=\operatorname{Mod}_\tau(S).
\end{aligned}
$$

Además, $\operatorname{Th}_\tau(\mathfrak A)$ es una teoría semánticamente cerrada para toda estructura fija $\mathfrak A$. Si $S$ es insatisfacible, entonces $\operatorname{Cn}^{\mathrm{sem}}_\tau(S)=\operatorname{Sent}_\tau$.

**Demostración.** La extensividad proviene de la reflexividad de §8.28: cada sentencia de $S$ es consecuencia de $S$. Para la monotonía, si $S\subseteq T$, cualquier pareja que satisface $T$ satisface $S$; toda consecuencia de $S$ es, pues, consecuencia de $T$. Para la idempotencia, la extensividad ya demuestra una inclusión. Para la otra, sea $\chi$ consecuencia de $\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$. Por la propia definición de la clausura, $S\models_\tau\sigma$ para todo miembro $\sigma$ de $\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$. La transitividad colectiva de §8.28 entrega $S\models_\tau\chi$, es decir, $\chi\in\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$.

Si una estructura modela $S$, satisface todas las consecuencias de $S$, luego modela su clausura; la inclusión inversa de clases de modelos resulta de $S\subseteq\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$. Para $\operatorname{Th}_\tau(\mathfrak A)$, tomemos una sentencia $\chi$ que sea consecuencia de todas las sentencias verdaderas en $\mathfrak A$: como $\mathfrak A$ misma es un modelo de ese conjunto, también satisface $\chi$; ésta pertenece entonces a $\operatorname{Th}_\tau(\mathfrak A)$. La inclusión opuesta viene de extensividad. Si $S$ no tiene modelos, todas las implicaciones metateóricas con antecedente $S$ son verdaderas, por lo que toda sentencia pertenece a su clausura. $\square$

**Precisión de tamaño.** No hemos definido $\operatorname{Cn}$ como intersección conjuntista de las teorías de una **clase propia** de estructuras. La expresión es un subconjunto separado de $\operatorname{Sent}_\tau$ mediante una propiedad metateórica.

## 8.34. Conservación de consecuencia por expansión de signatura

### Metateorema 8.34.1 — La consecuencia no depende de símbolos nuevos {#tlog-mth-00033}

Supongamos $\tau\subseteq\tau'$, inclusiones literales que conservan aridad y tipo, y fijemos $\Gamma\subseteq\operatorname{Fm}_\tau$, $\varphi\in\operatorname{Fm}_\tau$. Considerados literalmente como fórmulas de la firma más grande, se cumple

$$
\boxed{\Gamma\models_\tau\varphi
\iff\Gamma\models_{\tau'}\varphi.}
$$

También son equivalentes: (i) $\Gamma$ es satisfacible como conjunto de fórmulas de $\tau$; (ii) $\Gamma$ es satisfacible como conjunto de fórmulas de $\tau'$. En particular,

$$
\models_\tau\varphi\iff\models_{\tau'}\varphi.
$$

**Demostración.** Si la consecuencia vale en $\tau$, consideremos cualquier $\tau'$-estructura $\mathfrak B$ y cualquier asignación $s:X\to B$. Su reducto $\mathfrak A=\mathfrak B\!\upharpoonright_\tau$ tiene **el mismo** universo y, por [TLOG-MTH-00031](#tlog-mth-00031), las mismas condiciones de satisfacción para cada miembro de $\Gamma$ y para $\varphi$. La consecuencia en $\mathfrak A,s$ entrega la de $\mathfrak B,s$. Esto prueba una dirección.

Recíprocamente, supongamos $\Gamma\models_{\tau'}\varphi$, y sea $(\mathfrak A,s)$ una pareja arbitraria en la firma $\tau$ que satisface $\Gamma$. Por [TLOG-PRO-00009](capitulo-07.md#tlog-pro-00009), existe en ZF una expansión $\tau'$-estructural $\mathfrak B$ **sobre exactamente el mismo universo**, obtenida interpretando las funciones nuevas constantemente con un solo $a_0\in A$ y las relaciones nuevas como vacías. El lema de reducto mantiene la satisfacción de $\Gamma$ y de $\varphi$ en ambas estructuras. La consecuencia en $\tau'$ da $\mathfrak B,s\models_{\tau'}\varphi$, y el lema devuelve $\mathfrak A,s\models_\tau\varphi$. No se ha elegido una expansión simultánea de una familia de estructuras: se ha construido una sola expansión para una estructura **arbitraria**.

La equivalencia de satisfacibilidad se prueba transportando cualquier testigo $(\mathfrak A,s)$ hacia una expansión y cualquier testigo $(\mathfrak B,s)$ hacia su reducto. La equivalencia de validez es el caso de premisas vacías. $\square$

El teorema **no** permite olvidar símbolos presentes en las premisas o la conclusión, ni garantiza invariancia al **reducir el universo** de una estructura. Tampoco establece que alguna relación de consecuencia sea decidible.

## 8.35. Ejemplos de lectura semántica

**Premisas incompatibles.** En cualquier signatura, sea $\alpha=(x_0\doteq x_0)$ y $\Gamma=\{\alpha,\neg\alpha\}$. Ninguna pareja $(\mathfrak A,s)$ satisface $\Gamma$, porque la negación tiene el valor opuesto de $\alpha$. En consecuencia $\Gamma\models_\tau\varphi$ para cualquier $\varphi$, pero ello no exhibe una **derivación** en un cálculo de primer orden todavía no definido.

**Validez sin premisas.** La sentencia $\exists x\,(x\doteq x)$ es válida: toda estructura tiene dominio no vacío; escogido un único $a\in A$, su identidad consigo mismo proporciona el testigo. La sentencia $\forall x\forall y\,(x\doteq y)$ no es válida, pues falla en el universo de dos elementos con una asignación cualquiera.

**Una teoría como clase de modelos.** Con $\tau$ reducida a un símbolo relacional binario $R$, el conjunto unitario $S=\{\forall x\neg R(x,x)\}$ describe la clase de estructuras en que $R$ es irreflexiva. Sus modelos abarcan universos de muchos tamaños; la clase no es un conjunto, aunque $S$ y $\operatorname{Cn}^{\mathrm{sem}}_\tau(S)$ sí lo son.

**Premisas abiertas.** $P(x)\models_\tau^{\mathrm g}\forall xP(x)$ es verdadera en el sentido **global**; $P(x)\models_\tau\forall xP(x)$ es falsa en el sentido **local**. No bastará, por tanto, escribir $\Gamma\models\varphi$ sin una convención fijada acerca de variables libres de las premisas.

## 8.36. Balance del Capítulo 8 y frontera deductiva

Los tres microtramos construyen la semántica de primer orden con igualdad desde interpretaciones conjuntistas, asignaciones y recursión estructural: satisfacción de átomos y fórmulas, cinco conectivos y ambos cuantificadores primitivos, relaciones nularias, invariancia de asignación sobre variables libres, sustitución sin captura, equivalencia alfa, reductos, isomorfismos, embeddings en el fragmento sin cuantificadores y, finalmente, modelos de conjuntos de sentencias, satisfacibilidad, validez y consecuencia semántica de conjuntos arbitrarios de fórmulas.

La separación **local/global** hace que la consecuencia semántica elegida conserve el teorema de deducción sin condiciones adicionales, pero reconoce el riesgo de generalizar variables libres en las premisas. Las estructuras se cuantifican como clase definible en ZF; los conjuntos de fórmulas y sus clausuras semánticas son conjuntos. La existencia de modelos de teorías consistentes **no** se infiere en este capítulo: no hay aún cálculo de primer orden sobre el cual formular consistencia deductiva, corrección o completitud. Tampoco se reclama compacidad, decidibilidad, código Lean compilado o verificación mecánica.

Tras QA deductiva, bibliográfica, editorial y de persistencia, la función arquitectónica del Capítulo 8 queda satisfecha. Se mantiene abierta la **Parte II** para `TLOG-CH09-0001 — Sistemas deductivos y teorías`, donde $\vdash$ recibirá una definición autónoma. Ninguna arista deductiva del presente capítulo apunta a un resultado todavía pendiente del Capítulo 9.

```text
TLOG-CH08-M03 = CLOSED / PASS / DRIVE-READBACK-PASS
TLOG-CH08-0001 = CLOSED / PASS / DRIVE-READBACK-PASS
new mathematical nodes = 13
chapter 8 nodes = 30
TLOG nodes = 144
DAG nodes = 144
DAG edges = 378
cycle-check = PASS
external interfaces = 0
formalization candidates = 41
Lean compiled/verified = 0
closed chapters = 9/24 (37.5%)
PART I = CLOSED / PASS
PART II = OPEN
publication = NOT PUBLISHED
```

### Vector de progreso — `TLOG-CH08-M03`

```text
LOCAL  CH08-M03 ████████████████████ 13/13 (100 %, cierre matemático)
GLOBAL TLOG     █████████░░░░░░░░░░░░░░░ 9/24 capítulos (37,5 %)
```

La barra global contabiliza capítulos **completamente cerrados**, no un porcentaje supuesto sobre el número final de resultados del tratado.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 7](capitulo-07.md) · [Capítulo 9 →](capitulo-09.md)


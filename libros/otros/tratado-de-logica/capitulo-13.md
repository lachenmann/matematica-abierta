---
title: Capítulo 13 — Construcciones elementales de conjuntos
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
content-id: MA-BCH-0215
content-type: book-chapter
source-id: TLOG-CH13-0001
prerequisites:
- MA-BCH-0211
- MA-BCH-0213
- MA-BCH-0214
related:
- MA-BOK-0014
source-sha256: 0d9f5c9736b7ad8ca687d5e4000e0d9bbe8098bacd73982c4e73e7c297e97fb1
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 12](capitulo-12.md) · [Capítulo 14 →](capitulo-14.md)

## 13.0. De los axiomas a las operaciones definibles

El Capítulo 12 fijó la teoría objeto $\mathsf{ZF}_{\mathrm{obj}}$ sobre la firma pura $\tau_\in$, donde sólo $\dot\in$ es símbolo extralógico primitivo. Este capítulo **no amplía de manera tácita la signatura**. Primero demuestra dentro de la teoría objeto la existencia y unicidad de cada conjunto, y sólo después autoriza las impresiones familiares $\{a,b\}$, $\bigcup a$, $\mathcal P(a)$, $a\cup b$, $a\cap b$ y $a\setminus b$ como abreviaciones eliminables.

La metateoría $\mathsf M_{\mathrm{ext}}$ continúa siendo ZF clásica sin axioma de elección. El símbolo $\vdash$ indica derivabilidad **desde los axiomas objeto** con el cálculo $\mathsf H_{\tau_\in}^{=}$. Las variables y las expresiones entre llaves usadas para mostrar una relación definitoria pertenecen al metalenguaje, salvo que se explicite una extensión definicional. No se presupone ninguna interpretación estándar de un supuesto universo conjunto de todos los conjuntos.

**Fuentes y alcance:** se conservan las referencias ya registradas `TLOG-SRC-0002` (Enderton), `TLOG-SRC-0003` (Rautenberg) y `TLOG-SRC-00011` (control en línea de familias de axiomas de ZF). No se declara nuevo cotejo monográfico; todas las demostraciones del microtramo son reconstrucciones internas a partir de los nodos cerrados de los capítulos 9–12.

## 13.1. Política de operaciones definidas

### Convención 13.1.1 — Fórmulas caracterizadoras y nombres eliminables {#tlog-cnv-00016}

Para un símbolo matemático $\mathscr O$ que aún **no** pertenezca a $\tau_\in$, una expresión como $c=\mathscr O(\bar a)$ significa inicialmente la fórmula objeto $\Delta_{\mathscr O}(c,\bar a)$ en el lenguaje de pura pertenencia. Sólo después de verificar

$$
\mathsf{ZF}_{\mathrm{obj}}\vdash
\forall\bar a\,\exists!c\,\Delta_{\mathscr O}(c,\bar a)
$$

se autoriza $\mathscr O(\bar a)$ como **macro de término** en una extensión definicional cuyo símbolo funcional nuevo queda caracterizado por $\Delta_{\mathscr O}$. Una igualdad que contenga esa macro es la traducción abreviada de una fórmula con testigos únicos y cuantificadores frescos, no una nueva fórmula primitiva de $\tau_\in$. Se eligen los nombres auxiliares por frescura respecto de todos los parámetros, conforme a §§6.19–6.32 y §12.21; los casos con variables libres en $\bar a$ no autorizan captura por cuantificadores nuevos. La eliminación simultánea y la conservatividad finita se demostrarán en §13.14.

En esta sección $c=\mathscr O(\bar a)$ utiliza el igual de lectura matemática; las fórmulas objeto desplegadas escriben $c\doteq d$. Las definiciones no requieren un conjunto universal de objetos ni una función global externa cuyo dominio sea una clase propia.

## 13.2. Criterio de unicidad extensional

### Lema 13.2.1 — Unicidad de una descripción extensional {#tlog-lem-00039}

Sea $\theta(u,\bar a)$ una fórmula de $\tau_\in$, con variables libres entre $u,\bar a$, y sea $c$ un nombre nuevo respecto de $\theta$. Si de los axiomas objeto se deduce

$$
\forall\bar a\,\exists c\,\forall u\,[u\in c\leftrightarrow\theta(u,\bar a)],
$$

entonces también se deduce

$$
\boxed{\forall\bar a\,\exists!c\,\forall u\,[u\in c\leftrightarrow\theta(u,\bar a)].}
$$

**Demostración objeto, para cada $\theta$ fija.** Supóngase que $c,d$ cumplen sus respectivas caracterizaciones con los mismos parámetros. Por eliminación de $\leftrightarrow$ y transitividad proposicional, para todo $u$ se obtiene $u\in c\leftrightarrow u\in d$. El parámetro $u$ no permanece libre en ninguna premisa extra que impida generalizar el enunciado **dentro del condicional** $[\Delta(c)\land\Delta(d)]\to\forall u(u\in c\leftrightarrow u\in d)$. Extensionalidad implica $c\doteq d$. El resultado se internaliza con la implicación $\Delta(c)\to\forall d(\Delta(d)\to d\doteq c)$ y se combina con el testigo existencial supuesto. El uso del criterio no proporciona existencia por sí solo. $\square$

## 13.3. Construcción del par no ordenado

### Proposición 13.3.1 — Existencia y unicidad del par {#tlog-pro-00036}

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\forall a\forall b\exists!c\forall u\,[u\in c\leftrightarrow(u\doteq a\lor u\doteq b)].}
$$

**Demostración.** Particularizamos el axioma de pares (§12.5) a $a,b$, obteniendo existencia de un $c$ cuya pertenencia coincide con la disyunción indicada. §13.2 aplica con $\theta(u,a,b)\equiv(u\doteq a\lor u\doteq b)$, sin apariciones libres del testigo. Extensionalidad proporciona la unicidad. Todos los cuantificadores se introducen o particularizan con las condiciones de §12.30; no interviene elección. $\square$

El axioma de pares no declara un constructor $\{\cdot,\cdot\}$ como primitivo: sólo afirma existencia de su valor para cada pareja de parámetros objeto.

## 13.4. Notación del par y del singleton

### Definición 13.4.1 — Par no ordenado y singleton como extensiones definicionales {#tlog-def-00066}

Autorizamos la impresión $\{a,b\}$ para el único objeto $c$ que satisface

$$
\Delta_{\mathrm{par}}(c,a,b):\equiv\forall u\,[u\in c\leftrightarrow(u\doteq a\lor u\doteq b)].
$$

El **singleton** es la abreviación $\{a\}:=\{a,a\}$, cuyo gráfico se reduce por lógica clásica a $\forall u\,[u\in c\leftrightarrow u\doteq a]$. El símbolo $\{a,b\}$ no se incorpora a $F_2$ de la firma primitiva; si se quiere un cálculo con términos extendidos, la admisibilidad de la incorporación de una función binaria nueva se fundamenta en la unicidad de §13.3 y en la conservatividad del §13.14. No se requieren simultáneamente dos elecciones de objetos para definir el singleton.

## 13.5. Leyes de los pares y singletons

### Proposición 13.5.1 — Membresía y leyes extensionales de pares {#tlog-pro-00037}

Las siguientes son abreviaciones eliminables de teoremas de $\mathsf{ZF}_{\mathrm{obj}}$:

$$
\begin{aligned}
 u\in\{a,b\}&\leftrightarrow(u\doteq a\lor u\doteq b),\\
 u\in\{a\}&\leftrightarrow u\doteq a,\\
 \{a,b\}&=\{b,a\},\\
 \{a\}=\{b\}&\leftrightarrow a\doteq b,\\
 \{a,b\}=\{a\}&\leftrightarrow b\doteq a.
\end{aligned}
$$

**Demostración.** Las dos primeras líneas son la propiedad caracterizadora de §13.4. Para la conmutatividad, la disyunción es simétrica: $(u\doteq a\lor u\doteq b)\leftrightarrow(u\doteq b\lor u\doteq a)$. Extensionalidad equipara los testigos únicos. Si $\{a\}=\{b\}$, entonces $a\in\{a\}$; por sustitución de iguales, $a\in\{b\}$, y la segunda línea entrega $a\doteq b$. La implicación opuesta es congruencia lógica de igualdad. Si $\{a,b\}=\{a\}$, entonces $b\in\{a,b\}$ y, al reemplazar por el igual, $b\in\{a\}$, de donde $b\doteq a$; la recíproca se sigue al comparar membresía de ambas descripciones. Las pruebas con macros se expanden a fórmulas puras con testigos únicos antes de contarse como derivaciones objeto. $\square$

## 13.6. Existencia y unicidad de la unión de una familia

### Proposición 13.6.1 — Unión de un conjunto de conjuntos {#tlog-pro-00038}

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\forall a\exists!b\forall u\,[u\in b\leftrightarrow\exists v(v\in a\land u\in v)].}
$$

**Demostración.** El axioma de unión de §12.6 suministra $b$ para cada $a$. Para dos testigos $b_1,b_2$, el mismo bicondicional implica $\forall u(u\in b_1\leftrightarrow u\in b_2)$ y extensionalidad deduce $b_1\doteq b_2$. La fórmula definitoria no contiene el nombre del testigo libre en la matriz de pertenencia; las variables ligadas $u,v$ se eligen distintas de los parámetros. $\square$

## 13.7. Abreviación de unión

### Definición 13.7.1 — Macro $\bigcup a$ y su regla de expansión {#tlog-def-00067}

Autorizamos la expresión $\bigcup a$ por la propiedad definitoria

$$
\Delta_{\bigcup}(b,a):\equiv\forall u\,[u\in b\leftrightarrow\exists v\,(v\in a\land u\in v)].
$$

En toda fórmula que contenga $\bigcup a$ se lee un símbolo funcional **de una extensión definicional**, no un constructor primitivo de términos de $\tau_\in$. Su unicidad proviene de §13.6; la notación no añade una elección de representante, pues la propiedad caracteriza exactamente un objeto para cada $a$.

## 13.8. Unión binaria y leyes básicas

### Proposición 13.8.1 — Unión binaria por par más unión {#tlog-pro-00039}

La impresión binaria $a\cup b:=\bigcup\{a,b\}$ es una abreviación compuesta. Cumple

$$
\boxed{u\in(a\cup b)\leftrightarrow(u\in a\lor u\in b).}
$$

Además:

$$
\begin{aligned}
 a\cup\varnothing&=a,&a\cup b&=b\cup a,\\
 (a\cup b)\cup c&=a\cup(b\cup c),&
 \bigcup\varnothing&=\varnothing,&\bigcup\{a\}&=a.
\end{aligned}
$$

**Demostración.** Se despliega primero la macro de unión:

$$
 u\in\bigcup\{a,b\}\iff\exists v\,[(v\doteq a\lor v\doteq b)\land u\in v].
$$

La eliminación del existencial, el principio de sustitución de iguales y la introducción existencial prueban que equivale a $u\in a\lor u\in b$. Para $a\cup\varnothing=a$, la equivalencia se reduce a $u\in a\lor\bot\iff u\in a$; extensionalidad concluye. Conmutatividad y asociatividad se obtienen comparando respectivamente $A\lor B$ con $B\lor A$ y $(A\lor B)\lor C$ con $A\lor(B\lor C)$. Si $u\in\bigcup\varnothing$, habría $v\in\varnothing$, contradicción; por tanto la unión carece de elementos y coincide con el vacío único. Finalmente, $u\in\bigcup\{a\}\iff\exists v(v\doteq a\land u\in v)\iff u\in a$. En todos los casos el principio final es extensionalidad, no la sustitución de una igualdad metateórica en lugar de una fórmula objeto. $\square$

**Advertencia:** la unión binaria no es un axioma adicional ni requiere reemplazo. Las propiedades se derivan sólo de pares, unión, extensionalidad y la existencia del vacío.

## 13.9. Existencia y unicidad del conjunto potencia

### Proposición 13.9.1 — Potencia de un conjunto {#tlog-pro-00040}

Para la macro de inclusión de §12.3,

$$
\boxed{\mathsf{ZF}_{\mathrm{obj}}\vdash\forall a\exists!b\forall u\,[u\in b\leftrightarrow u\subseteq a].}
$$

**Demostración.** §12.7 da para cada $a$ un conjunto $b$ con $u\in b\leftrightarrow\forall v(v\in u\to v\in a)$. Dicha fórmula es precisamente la expansión de $u\subseteq a$; la unicidad del testigo sigue de §13.2. En la escritura primitiva se sustituye $u\subseteq a$ por su fórmula con $v$ fresca; la inclusión no se agrega a $R_2$. $\square$

## 13.10. Abreviación del conjunto potencia

### Definición 13.10.1 — Macro $\mathcal P(a)$ {#tlog-def-00068}

Se admite $\mathcal P(a)$ como el único $b$ que satisface

$$
\Delta_{\mathcal P}(b,a):\equiv\forall u\,[u\in b\leftrightarrow\forall v(v\in u\to v\in a)].
$$

Cada ocurrencia de $\mathcal P(a)$ en una igualdad o fórmula de pertenencia expresa una **extensión definicional** eliminable. La notación $\mathcal P$ no denota una función objeto primitiva ni una función metateórica con dominio igual a una supuesta clase universal tratada como conjunto.

## 13.11. Primeras leyes del conjunto potencia

### Proposición 13.11.1 — Membresía, monotonía y reflexión de la inclusión {#tlog-pro-00041}

Las expresiones siguientes se leen después de expansión de sus macros:

$$
\begin{aligned}
 u\in\mathcal P(a)&\leftrightarrow u\subseteq a,\\
 \varnothing\in\mathcal P(a),&\qquad a\in\mathcal P(a),\\
 a\subseteq b&\Longrightarrow\mathcal P(a)\subseteq\mathcal P(b),\\
 \mathcal P(a)\subseteq\mathcal P(b)&\Longrightarrow a\subseteq b,\\
 \mathcal P(a)=\mathcal P(b)&\Longleftrightarrow a\doteq b,\\
 \mathcal P(\varnothing)&=\{\varnothing\}.
\end{aligned}
$$

**Demostración.** La primera línea es definitoria. La fórmula $\varnothing\subseteq a$ es válida porque $\varnothing$ no tiene miembros, y $a\subseteq a$ por reflexividad lógica; de ahí la segunda. Si $a\subseteq b$, todo miembro de cualquier $u\subseteq a$ pertenece a $b$, por lo que $u\subseteq b$ y, por cuantificación universal, $\mathcal P(a)\subseteq\mathcal P(b)$. Para la reflexión, $a\in\mathcal P(a)$; si $\mathcal P(a)\subseteq\mathcal P(b)$, entonces $a\in\mathcal P(b)$, lo que significa $a\subseteq b$. La igualdad de potencias implica ambas inclusiones de sus argumentos y extensionalidad produce $a\doteq b$; la recíproca es sustitución de iguales. Finalmente, si $u\in\mathcal P(\varnothing)$, entonces $u\subseteq\varnothing$, de donde $u$ carece de miembros y $u=\varnothing$ por extensionalidad; la dirección inversa se sigue de la vacuidad de la inclusión. La descripción resultante coincide con el singleton de $\varnothing$. $\square$

No se infiere que la aplicación potencia sea sobreyectiva, ni se introduce cardinalidad o el teorema de Cantor en este microtramo.

## 13.12. Separación como construcción por parámetros

### Definición 13.12.1 — Subconjunto separado por fórmula {#tlog-def-00069}

Para cada fórmula fija $\theta(u,a,\bar p)\in\operatorname{Fm}_{\tau_\in}$, se autoriza la notación esquemática

$$
\{u\in a:\theta(u,a,\bar p)\}
$$

como nombre eliminable del único $b$ que satisface

$$
\Delta_{\mathrm{sep},\theta}(b,a,\bar p):\equiv\forall u\,[u\in b\leftrightarrow(u\in a\land\theta(u,a,\bar p))].
$$

La **existencia** de este $b$ para cada valor de $a,\bar p$ es una instancia cerrada del esquema de separación (§12.9), particularizada con condiciones de frescura (§12.30); su **unicidad** se prueba por §12.31. Al imprimir un cuantificador cuyo nombre colisione con un vinculante de $\theta$, se aplica la equivalencia alfa de §12.21 antes de insertarlo. No hay una operación objeto que tome «todas las fórmulas» como argumentos: $\theta$ es un índice **metateórico** del esquema, no una variable objeto.

No se permite escribir $\{u:\theta(u)\}$ sin un conjunto ambiente demostrado. En particular, esta notación no revive la comprensión irrestricta refutada en §12.16.

## 13.13. Intersecciones y diferencias

### Proposición 13.13.1 — Construcción de intersección y diferencia relativas {#tlog-pro-00042}

Tomando $\theta(u,a,b):\equiv u\in b$ y $\chi(u,a,b):\equiv\neg(u\in b)$ en §13.12, obtenemos, para cualesquiera $a,b$, los conjuntos $a\cap b$ y $a\setminus b$, caracterizados por

$$
\boxed{\begin{aligned}
 u\in(a\cap b)&\leftrightarrow(u\in a\land u\in b),\\
 u\in(a\setminus b)&\leftrightarrow(u\in a\land\neg(u\in b)).
\end{aligned}}
$$

Derivamos asimismo

$$
\begin{aligned}
 a\cap b &= b\cap a,\\
 a\cap\varnothing &=\varnothing,\\
 a\setminus a&=\varnothing,\\
 a\cap(b\cup c)&=(a\cap b)\cup(a\cap c).
\end{aligned}
$$

**Demostración.** Separación garantiza existencia de cada testigo con el parámetro $b$ libre en la matriz inicial y universalmente cerrado después. §12.31 garantiza unicidad; en consecuencia se autorizan las macros $a\cap b$, $a\setminus b$. Sus cláusulas de pertenencia son exactamente las instancias empleadas. En la primera ley, $A\land B$ es conmutativo. Para las dos leyes del vacío, $u\in\varnothing$ es siempre falso, y $u\in a\land\neg(u\in a)$ es contradictorio; extensionalidad iguala ambos resultados con $\varnothing$. Para la distributividad, desplegamos unión por §13.8 y separación por las dos cláusulas precedentes: ambos lados tienen como condición de pertenencia $u\in a\land(u\in b\lor u\in c)$, que es proposicionalmente equivalente a $(u\in a\land u\in b)\lor(u\in a\land u\in c)$. Extensionalidad concluye. Las aparentes igualdades entre expresiones construidas se traducen por sus gráficos funcionales antes de invocar las reglas de primer orden. $\square$

**Frontera:** la intersección $\bigcap A$ de una familia arbitraria y el complemento absoluto no se introducen sin precisar el conjunto ambiente y la hipótesis de no vacuidad cuando sea necesaria.

## 13.14. Conservatividad para familias finitas de operaciones definidas

### Metateorema 13.14.1 — Eliminación finita de símbolos funcionales definibles {#tlog-mth-00054}

Sea $L_0=\tau_\in$, $T_0=\operatorname{Ax}_{\mathsf{ZF}}$, y una **sucesión finita** de expansiones $L_0\subset L_1\subset\cdots\subset L_m$, en la cual el paso $i+1$ añade un símbolo funcional nuevo $f_i$ de aridad finita $k_i$, junto a la única sentencia de definición

$$
\forall\bar x\,\Delta_i(f_i(\bar x),\bar x),
$$

con $\Delta_i(y,\bar x)$ fórmula de $L_i$ y prueba previa $T_i\vdash\forall\bar x\exists!y\,\Delta_i(y,\bar x)$. Aquí $k_i=0$ está permitido y la secuencia de definiciones sólo utiliza símbolos antiguos o de **pasos anteriores**. Entonces:

1. todo modelo de $T_0$ admite una **única expansión sucesiva** a modelo de $T_m$;
2. si $\varphi\in\operatorname{Fm}_{L_0}$, entonces
   $$
   \boxed{T_m\vdash_{\mathsf H_{L_m}^{=}}\varphi\iff T_0\vdash_{\mathsf H_{L_0}^{=}}\varphi;}
   $$
3. toda fórmula con los nuevos símbolos tiene una **traducción definicional** a una fórmula del lenguaje original, equivalente en las expansiones que satisfacen sus axiomas de definición.

**Demostración metateórica.** Fijada una estructura $\mathfrak A_i\models T_i$, la corrección de §10.7 convierte $T_i\vdash\forall\bar x\exists!y\Delta_i(y,\bar x)$ en la existencia, para cada $\bar a\in A^{k_i}$, de un único $b\in A$ que verifica $\Delta_i(b,\bar a)$. Por separación y reemplazo **en la metateoría externa** sobre el conjunto $A^{k_i}$, la gráfica $\{(\bar a,b):\mathfrak A_i\models\Delta_i(b,\bar a)\}$ constituye una función total y única; no se requiere elección. Se interpreta $f_i$ por esa función. Si $k_i=0$, la gráfica tiene dominio $A^0=\{()\}$ y selecciona el único valor obligado. La recursión **finita** de $i=0$ a $m$ genera la expansión única.

Para las consecuencias antiguas, si $T_0\nvdash\varphi$ y $\varphi$ es una sentencia, entonces $T_0\cup\{\neg\varphi\}$ es consistente por las propiedades clásicas del cálculo. Puesto que $L_0=\tau_\in$ es finito (y por tanto numerable), §11.10 entrega un modelo $\mathfrak A_0$ de esas premisas en la metateoría ZF. La expansión sucesiva anterior produce $\mathfrak A_m\models T_m\cup\{\neg\varphi\}$. Corrección impide $T_m\vdash\varphi$. La otra implicación se obtiene transportando las pruebas originales a la signatura ampliada. Si $\varphi$ es **abierta**, se pasa primero a su clausura universal desde las premisas sentenciales de $T_m$, aplica el caso sentencial y luego se particulariza; esto controla las variables libres. La demostración vale asimismo si $T_0$ es inconsistente: en ese caso la dirección nueva-a-antigua resulta trivial, aunque no existe modelo inicial.

Finalmente se elimina cada término ampliado por **traducción de su gráfica**: para una variable $x$, el gráfico es $y\doteq x$; para $f_i(t_1,\ldots,t_k)$, se introducen nombres testigo frescos $y_1,\ldots,y_k$ para las traducciones de los sub-términos y se agrega $\Delta_i(y,\bar y)$; para una fórmula atómica se reemplazan todos sus términos por estos gráficos y se cuantifican sus valores, recursivamente para las conectivas y los cuantificadores de la fórmula. La unicidad de cada gráfico demuestra por inducción que la traducción preserva satisfacción en toda expansión correspondiente, y que los vinculantes originales no capturan los nombres auxiliares. Se eliminan después los símbolos añadidos **en orden inverso** de introducción, porque la fórmula definitoria de cada uno sólo usa el lenguaje disponible previamente. $\square$

**Aplicación.** Las operaciones $\{a,b\}$, $\bigcup a$, $\mathcal P(a)$, el vacío nombrado y las dos operaciones $a\cap b,a\setminus b$ se pueden introducir en cualquier **orden finito de dependencias** respetado por sus definiciones. La separación $\{u\in a:\theta(u,a,\bar p)\}$ es un *esquema de macros indexadas por fórmulas*; no se interpreta como una única función objeto cuyo argumento fuera el código de una fórmula, a menos que dicha codificación y su semántica se desarrollen expresamente. No se introduce AC, BPI ni una pretensión de verdad absoluta de $T_0$.

## 13.15. Conjuntos finitos generados sin selección

### Corolario 13.15.1 — Construcción uniforme de familias finitas {#tlog-cor-00014}

Para cada natural **metateórico fijo** $n$ existe una expresión definicional eliminable $\{a_0,\ldots,a_{n-1}\}$ con la propiedad de pertenencia

$$
\boxed{u\in\{a_0,\ldots,a_{n-1}\}\ \leftrightarrow\ \bigvee_{i<n}(u\doteq a_i).}
$$

Para $n=0$ la disyunción vacía se interpreta como falsedad y la expresión como el conjunto vacío; para $n+1$, se define recursivamente $F_{n+1}=F_n\cup\{a_n\}$. La existencia del vacío procede de §12.26; el paso sucesor utiliza §13.4 y §13.8. La inducción **externa sobre un entero fijo** verifica que la cláusula de pertenencia resultante es la disyunción finita escrita; la unicidad se debe a extensionalidad. No se elige simultáneamente un testigo entre múltiples opciones: cada conjunto está determinado de modo único. Si se desea una expresión de $\tau_\in$ sin llaves, se eliminan sus macros en el orden finito de construcción mediante §13.14. $\square$

No se afirma aquí un **teorema objeto uniforme** que cuantifique sobre un natural $n$: la codificación interna de naturales, secuencias y recursión objeto pertenece al Capítulo 16. El corolario es una **familia metateórica de resultados objeto**, una para cada $n$ fijado.

## 13.16. Control local, fuentes y obligaciones pendientes

El microtramo `TLOG-CH13-M01` cierra 15 nodos matemáticos. Se han construido pares y singletons, unión general y binaria, conjunto potencia y subconjuntos por separación, con pruebas objeto de existencia/unicidad y justificación metateórica de las macros. La equivalencia entre grafos y notaciones extendidas es finita y no convierte una función definible sobre conjuntos en un símbolo primitivo del lenguaje de pertenencia.

La teoría objeto **no** ha demostrado su propia consistencia. Los principios de existencia usados son únicamente las instancias axiomáticas correspondientes; las funciones y clases metateóricas se construyen sobre **conjuntos dados**. Se mantiene la reserva BPI para compacidad en signaturas irrestrictas, aunque aquí se utiliza únicamente el lenguaje numerable $\tau_\in$.

Quedan abiertas para `CH13-M02` las imágenes por reemplazo, la intersección de familias no vacías, el control de separación con condiciones definibles de dos o más parámetros, diferencias y otras leyes pertinentes, y la auditoría de cierre del capítulo. No se activan interfaces intertratados, no se declara Lean compilado, y la publicación web permanece pendiente.

```text
TLOG-CH13-M01 = CLOSED / MATHEMATICAL-QA-PASS / DRIVE-READBACK-PASS
TLOG-CH13-0001 = PARTIAL-CLOSURE / NOT CLOSED
PART III = OPEN
CHAPTERS CLOSED = 13/24
PARTS CLOSED = 2/5
LEAN VERIFIED = 0
PUBLICATION = NOT PUBLISHED
```

## 13.17. Relaciones definibles y condiciones de funcionalidad

### Convención 13.17.1 — Fórmulas que definen valores sobre un conjunto {#tlog-cnv-00017}

Sea $\Theta(x,y,\bar p)\in\operatorname{Fm}_{\tau_\in}$ una fórmula **fija**, con variables libres sólo entre $x,y,\bar p$. Las listas de parámetros son finitas; los nombres de todos los testigos y de sus vinculantes se normalizan por equivalencia alfa antes de instanciar axiomas. Para el conjunto objeto $a$, llamamos **condición funcional restringida** a la fórmula

$$
F_\Theta(a,\bar p):\equiv \forall x\,[x\in a\to\exists!y\,\Theta(x,y,\bar p)].
$$

Esta fórmula no cuantifica sobre $\Theta$: para **cada** matriz sintáctica fija se obtiene una instancia del metalenguaje. No es requisito que la relación sea funcional fuera de $a$, ni se supone que $\Theta$ sea el gráfico de una función formal previamente construida. El símbolo $\exists!$ se expande como en §12.3. Conviene distinguir $F_\Theta$ de la mera cota $\forall x\in a\forall y(\Theta(x,y)\to y\in b)$: la segunda **no implica** funcionalidad ni existencia de valores.

## 13.18. Imagen exacta por reemplazo

### Proposición 13.18.1 — Existencia y unicidad de la imagen funcional {#tlog-pro-00043}

Para toda fórmula fija $\Theta(x,y,\bar p)$ con los nombres frescos de §13.17, la teoría objeto demuestra la sentencia

$$
\boxed{\forall\bar p\forall a\,\bigl[F_\Theta(a,\bar p)\to
\exists!b\forall y\,(y\in b\leftrightarrow
\exists x\,[x\in a\land\Theta(x,y,\bar p)])\bigr].}
$$

**Demostración objeto.** Instanciamos reemplazo restringido (§12.10) con la matriz $\rho(x,y,a,\bar p):=\Theta(x,y,\bar p)$, que simplemente ignora el parámetro adicional $a$. La premisa de la instancia coincide, después de expandir $\exists!$ y de renombrar las variables ligadas, con $F_\Theta(a,\bar p)$. Reemplazo produce $b$ cuya membresía está caracterizada por $\exists x(x\in a\land\Theta(x,y,\bar p))$. Si $b'$ también satisface esa caracterización, entonces $\forall y(y\in b\leftrightarrow y\in b')$, y extensionalidad da $b\doteq b'$. La fórmula final se cierra universalmente sobre $a,\bar p$, que no figuran libres en premisas extralógicas añadidas. No se usa selección simultánea de testigos: la hipótesis $\exists!$ asegura su determinación. $\square$

**Precisión:** esta conclusión no está afirmada para una relación arbitraria sin funcionalidad, pues el esquema de reemplazo adoptado no concede imágenes no acotadas de relaciones multivaluadas.

## 13.19. Notación de imagen y dominio vacío

### Definición 13.19.1 — Macro de imagen de una fórmula funcional {#tlog-def-00070}

**Bajo la hipótesis** $F_\Theta(a,\bar p)$, escribimos $\operatorname{Im}_\Theta(a;\bar p)$ para el único $b$ que satisface

$$
\Delta_{\operatorname{Im},\Theta}(b,a,\bar p):\equiv
\forall y\,[y\in b\leftrightarrow\exists x(x\in a\land\Theta(x,y,\bar p))].
$$

Se trata de una **macro parcial con condición lateral demostrada**, no de un nuevo símbolo funcional total de la signatura pura $\tau_\in$. Su expansión en una fórmula objeto exige conservar la hipótesis $F_\Theta$ y cuantificar los testigos con nombres frescos. La posible totalización por valor vacío fuera de $F_\Theta$ se construirá en §13.31, sin llamar a esa totalización «imagen» sin cualificación.

La fórmula $F_\Theta(\varnothing,\bar p)$ es demostrable, pues no existe $x\in\varnothing$. La caracterización resultante tiene membresía siempre falsa; por extensionalidad,

$$
\mathsf{ZF}_{\mathrm{obj}}\vdash
\operatorname{Im}_\Theta(\varnothing;\bar p)=\varnothing
$$

para cada $\Theta$ fija, con ambas macros leídas mediante sus grafos. No se confunde esta afirmación con el dominio no vacío exigido para la intersección absoluta de familias.

## 13.20. Leyes elementales de la imagen

### Proposición 13.20.1 — Identidad, constante y monotonía de imágenes {#tlog-pro-00044}

Para una relación definible $\Theta(x,y,\bar p)$ **independiente del nombre de su dominio** y conjuntos $a\subseteq b$ donde $F_\Theta(b,\bar p)$, se deriva

$$
\operatorname{Im}_\Theta(a;\bar p)\subseteq\operatorname{Im}_\Theta(b;\bar p).
$$

La relación identidad $\mathsf{Id}(x,y):\equiv y\doteq x$ es funcional sobre cualquier conjunto, y su imagen satisface $\operatorname{Im}_{\mathsf{Id}}(a)=a$. La relación constante $\mathsf K_p(x,y):\equiv y\doteq p$, para parámetro $p$, es funcional sobre todo $a$ y cumple

$$
\operatorname{Im}_{\mathsf K_p}(a)=
\begin{cases}\varnothing,&a=\varnothing,\\\{p\},&\exists x\,x\in a.\end{cases}
$$

**Demostración objeto.** De $F_\Theta(b,\bar p)$ y $a\subseteq b$ se obtiene $F_\Theta(a,\bar p)$ por particularización. Si $y$ pertenece a la primera imagen, algún $x\in a$ satisface $\Theta(x,y,\bar p)$; como $a\subseteq b$, ese mismo $x$ atestigua la pertenencia a la segunda. Para la identidad, $\exists x(x\in a\land y\doteq x)\leftrightarrow y\in a$, así que extensionalidad iguala los conjuntos. Para la relación constante, $\exists x(x\in a\land y\doteq p)$ equivale a $(\exists x\,x\in a)\land y\doteq p$; en el caso vacío no tiene testigos y en el no vacío caracteriza el singleton. Todas las afirmaciones son **esquemas de derivaciones objeto** para las fórmulas indicadas. $\square$

La independencia de $\Theta$ respecto del *nombre de dominio* es necesaria para la monotonía tal como se ha formulado; no se intercambian fórmulas distintas $\Theta(x,y,a)$ y $\Theta(x,y,b)$.

## 13.21. Composición de imágenes funcionales

### Proposición 13.21.1 — Imagen de una composición definible {#tlog-pro-00045}

Sean $\Theta(x,y,\bar p)$ y $\Psi(y,z,\bar q)$ dos fórmulas fijas, con nombres ligados disjuntos de los parámetros. Si $F_\Theta(a,\bar p)$, $b=\operatorname{Im}_\Theta(a;\bar p)$ y $F_\Psi(b,\bar q)$, entonces

$$
\Xi(x,z,\bar p,\bar q):\equiv
\exists y\,[\Theta(x,y,\bar p)\land\Psi(y,z,\bar q)]
$$

es funcional sobre $a$ y la teoría objeto prueba

$$
\boxed{\operatorname{Im}_\Xi(a;\bar p,\bar q)
=\operatorname{Im}_\Psi(\operatorname{Im}_\Theta(a;\bar p);\bar q).}
$$

**Demostración objeto.** Para cada $x\in a$, la funcionalidad de $\Theta$ determina un único $y$. Por definición de $b$, ese $y\in b$, y la funcionalidad de $\Psi$ determina un único $z$. Si $z,z'$ verifican $\Xi(x,\cdot)$, la unicidad del intermediario $y$ obliga a escoger el mismo valor y después la unicidad de $\Psi$ da $z\doteq z'$. Así $F_\Xi(a)$. Un objeto $z$ pertenece a la imagen izquierda si y sólo si $\exists x\in a\exists y\,[\Theta(x,y)\land\Psi(y,z)]$. Reasociando los cuantificadores acotados, esta condición equivale a $\exists y\in b\,\Psi(y,z)$, que caracteriza la imagen derecha. Extensionalidad prueba la igualdad de los testigos únicos. $\square$

La composición es de **relaciones definibles funcionales**; no se anticipa aquí la teoría de funciones como conjuntos de pares ordenados del Capítulo 14.

## 13.22. Imágenes de relaciones con cota preexistente

### Proposición 13.22.1 — Imagen relativa de una relación no funcional {#tlog-pro-00046}

Sea $\rho(x,y,\bar p)$ una fórmula **arbitraria**, sin hipótesis de unicidad. Para todos los conjuntos $a,b$ existe un único conjunto $c$ caracterizado por

$$
\boxed{\forall y\,[y\in c\leftrightarrow
(y\in b\land\exists x(x\in a\land\rho(x,y,\bar p)))].}
$$

**Demostración objeto.** Instanciamos separación con conjunto ambiente $b$, matriz $\theta(y,a,b,\bar p):=\exists x(x\in a\land\rho(x,y,\bar p))$ y parámetros $a,\bar p$. El nuevo testigo $c$ y los nombres ligados se toman frescos. Separación produce el conjunto especificado; extensionalidad da unicidad. No se emplea reemplazo. $\square$

Si además se demuestra $\forall x\in a\forall y(\rho(x,y,\bar p)\to y\in b)$, la conjunción $y\in b$ es redundante y $c$ es la **imagen exacta**, incluso cuando $\rho$ tiene muchos valores para un mismo $x$. Sin tal cota no se concluye que la colección de todos sus valores sea un conjunto. La notación $\{y\in b:\exists x\in a\,\rho(x,y,\bar p)\}$ es eliminable y nunca constituye comprensión sin conjunto ambiente.

## 13.23. Dos lecturas de una intersección de familia

### Convención 13.23.1 — Intersección absoluta y relativa {#tlog-cnv-00018}

Para una familia objeto $A$, la expresión informal $\bigcap A$ pretende designar el conjunto de **todos** los objetos que pertenecen a cada miembro de $A$. Cuando $A=\varnothing$, esa descripción sería la totalidad del universo objeto, la cual §12.16 demuestra que **no constituye un conjunto**. En cambio, dado un conjunto ambiente $U$, la intersección relativa $\bigcap_U A$ se restringirá a $U$ y estará definida incluso cuando $A$ sea vacía. La pertenencia externa de las estructuras utilizadas en la metateoría no altera esta distinción.

## 13.24. Intersección de una familia no vacía

### Proposición 13.24.1 — Existencia y unicidad de intersección no vacía {#tlog-pro-00047}

La teoría objeto demuestra

$$
\boxed{\forall A\,\Bigl[(\exists a\,a\in A)\to
\exists!c\forall u\,\bigl(u\in c\leftrightarrow
\forall b(b\in A\to u\in b)\bigr)\Bigr].}
$$

**Demostración objeto.** Supóngase $\exists a(a\in A)$. Mediante eliminación existencial en el cálculo de primer orden, tomamos un **único** testigo auxiliar $a_0\in A$ dentro de una subdemostración, sin instaurar función de elección alguna. Aplicamos separación al conjunto ambiente $a_0$ con la matriz $\forall b(b\in A\to u\in b)$. Obtenemos $c$ tal que

$$
\forall u\,[u\in c\leftrightarrow(u\in a_0\land\forall b(b\in A\to u\in b))].
$$

Como $a_0\in A$, la condición $\forall b\in A(u\in b)$ implica $u\in a_0$, y la equivalencia anterior se simplifica a la caracterización requerida. Si $c,d$ satisfacen esa misma fórmula, extensionalidad da $c\doteq d$. Cerramos la subdemostración descargando $a_0$, que no aparece en el enunciado final, y generalizamos sobre $A$. Ninguna selección sobre los miembros de $A$ se ha efectuado. $\square$

## 13.25. Notación contextual de la intersección

### Definición 13.25.1 — Macro parcial $\bigcap A$ {#tlog-def-00071}

La escritura $\bigcap A$ queda autorizada **sólo** en un contexto objeto que permita demostrar $\exists a(a\in A)$, y significa el único objeto $c$ del §13.24. Fuera de ese contexto no denota un término del lenguaje puro ni un símbolo funcional total de una expansión. Las ocurrencias de $\bigcap A$ en fórmulas se eliminan agregando su descripción única y conservando la condición de no vacuidad. Esta es una abreviación contextual, no una aplicación automática del metateorema de introducción de **funciones totales** §13.14.

## 13.26. Leyes de intersecciones de familias

### Proposición 13.26.1 — Singletons, pares y antitonicidad {#tlog-pro-00048}

Con las hipótesis de existencia de las macros implicadas, los siguientes son teoremas objeto:

$$
\begin{aligned}
\bigcap\{a\}&=a,\\
\bigcap\{a,b\}&=a\cap b,\\
A\subseteq B\ \land\ A\ne\varnothing&\Longrightarrow\bigcap B\subseteq\bigcap A,\\
A\ne\varnothing&\Longrightarrow\bigcap A\subseteq\bigcup A.
\end{aligned}
$$

**Demostración.** La familia $\{a\}$ contiene $a$ y es no vacía; $\forall b\in\{a\}\,u\in b$ equivale a $u\in a$. Para $\{a,b\}$, la condición equivale a $(u\in a\land u\in b)$; el conjunto caracterizado coincide con la intersección binaria de §13.13. Si $A\subseteq B$ y $A$ no es vacía, entonces $B$ tampoco lo es; quien pertenece a todos los miembros de $B$ pertenece a todos los miembros de $A$. Para la última inclusión, de $A\ne\varnothing$ obtenemos un testigo $a_0\in A$; si $u\in\bigcap A$, entonces $u\in a_0$, por lo que $u\in\bigcup A$. Las cuatro igualdades o inclusiones se concluyen mediante sus cláusulas de pertenencia y extensionalidad donde corresponde. $\square$

Aquí $A\ne\varnothing$ significa la fórmula $\exists a(a\in A)$, no una primitiva nueva.

## 13.27. Intersección relativa total

### Definición 13.27.1 — Intersección dentro de un conjunto ambiente {#tlog-def-00072}

Para **cualesquiera** conjuntos $U,A$, separación y extensionalidad prueban la existencia y unicidad de $c$ tal que

$$
\boxed{\forall u\,[u\in c\leftrightarrow
(u\in U\land\forall b(b\in A\to u\in b))].}
$$

Autorizamos $\bigcap_U A$ como notación del $c$ así determinado. Como la caracterización es total para $U,A$, a diferencia de $\bigcap A$, cabe incorporarla como función binaria definida en una extensión conservativa finita (§13.14). Para la familia vacía se tiene $\bigcap_U\varnothing=U$, pues la condición universal en $b\in\varnothing$ es vacuamente verdadera; para una familia no vacía, $\bigcap_U A=U\cap\bigcap A$, con la intersección de la derecha autorizada por §13.25. Todas estas identidades se demuestran expandiendo las cláusulas de membresía.

## 13.28. Intersección como separación sobre una unión

### Proposición 13.28.1 — Descripción sin selección sobre $\bigcup A$ {#tlog-pro-00049}

Para toda familia **no vacía** $A$,

$$
\boxed{\bigcap A=
\{u\in\bigcup A:\forall b(b\in A\to u\in b)\}
=\bigcap_{\bigcup A} A.}
$$

**Demostración objeto.** Existe $\bigcup A$ sin ninguna hipótesis, por §13.6. Si $u\in\bigcap A$, eligiendo dentro de una sola subdemostración un $b\in A$, se infiere $u\in b$ y por ello $u\in\bigcup A$; además $u$ satisface la condición universal. La inclusión recíproca es inmediata de la cláusula de separación: todo miembro del conjunto derecho pertenece a cada miembro de $A$. Extensionalidad iguala ambos conjuntos. La última igualdad resulta de la definición de intersección relativa con ambiente $\bigcup A$. $\square$

La fórmula relativa permanece válida para $A=\varnothing$, pero entonces su valor es $\bigcup\varnothing=\varnothing$; no es la intersección absoluta de la familia vacía.

## 13.29. Unión de una familia funcionalmente indexada

### Proposición 13.29.1 — Unión de imágenes por reemplazo {#tlog-pro-00050}

Si $F_\Theta(a,\bar p)$, la **imagen** $B=\operatorname{Im}_\Theta(a;\bar p)$ existe por reemplazo, y la **unión** $U=\bigcup B$ existe por el axioma de unión. El conjunto $U$ queda caracterizado exactamente por

$$
\boxed{u\in U\iff\exists x\,[x\in a\land
\exists y(\Theta(x,y,\bar p)\land u\in y)].}
$$

**Demostración objeto.** Por la cláusula de unión, $u\in U$ equivale a $\exists y(y\in B\land u\in y)$. Por la cláusula de imagen, $y\in B$ equivale a $\exists x(x\in a\land\Theta(x,y,\bar p))$. Sustituyendo y reordenando dos cuantificadores existenciales no capturadores se obtiene el enunciado. La unicidad de $U$ procede de extensionalidad; su existencia ya se obtuvo en dos aplicaciones sucesivas a **conjuntos** dados, no en una comprensión de clase. $\square$

Esto prepara uniones indexadas sin introducir todavía una función objeto representada por un conjunto de pares ordenados.

## 13.30. Por qué no existe la intersección absoluta vacía

### Lema 13.30.1 — Necesidad de la condición de no vacuidad {#tlog-lem-00040}

La teoría objeto demuestra

$$
\boxed{\neg\exists c\forall u\,[u\in c\leftrightarrow
\forall b(b\in\varnothing\to u\in b)].}
$$

**Demostración objeto.** Suponiendo tal $c$, la condición $b\in\varnothing$ es falsa para todo $b$. Por lógica clásica de primer orden, $\forall b(b\in\varnothing\to u\in b)$ resulta verdadera para cada $u$; el bicondicional supuesto implica $\forall u(u\in c)$. Esto contradice §12.16 (inexistencia de conjunto universal). Descargando el supuesto queda la negación existencial. $\square$

Así la elección de $\bigcap\varnothing=\varnothing$ como *totalización convencional* no es el valor de la intersección absoluta; para obtener una operación total hay que distinguir expresamente el caso vacío, como se hará enseguida.

## 13.31. Totalizaciones definicionales sin pérdida de control

### Metateorema 13.31.1 — Eliminación de macros funcionales condicionadas {#tlog-mth-00055}

Sea $\Delta(y,\bar a)$ una fórmula fija de $\tau_\in$, y $F(\bar a)$ una condición demostrable cuando pretendemos usar su valor, tales que

$$
\mathsf{ZF}_{\mathrm{obj}}\vdash
\forall\bar a\,[F(\bar a)\to\exists!y\,\Delta(y,\bar a)].
$$

Definamos, usando el conjunto vacío ya demostrado, la fórmula **totalizada**

$$
\widehat\Delta(y,\bar a):\equiv
\bigl(F(\bar a)\land\Delta(y,\bar a)\bigr)\lor
\bigl(\neg F(\bar a)\land\forall u\neg(u\in y)\bigr).
$$

Entonces $\mathsf{ZF}_{\mathrm{obj}}\vdash\forall\bar a\exists!y\,\widehat\Delta(y,\bar a)$. Además, **bajo la hipótesis $F(\bar a)$** el valor así introducido coincide con el único valor de $\Delta$, mientras que fuera de ella vale $\varnothing$. En cualquier **familia finita y bien ordenada de introducciones** de estas funciones totalizadas, el metateorema de §13.14 asegura conservatividad sobre el lenguaje puro y eliminación de sus símbolos en las fórmulas ampliadas.

**Demostración metateórica.** El cálculo clásico de la teoría objeto decide $F(\bar a)\lor\neg F(\bar a)$ para parámetros arbitrarios. Bajo $F$, la hipótesis aporta un único $y$ con $\Delta$, que satisface $\widehat\Delta$; la otra disyunción es falsa. Bajo $\neg F$, el testigo único del conjunto vacío satisface la segunda disyunción y la primera es falsa. Mediante eliminación de casos y generalización interna se obtiene $\forall\bar a\exists!y\widehat\Delta$. Aplicamos §13.14 a una expansión por el símbolo funcional cuya ecuación definitoria es $\widehat\Delta$, respetando el orden de anteriores símbolos si aparecen en la expresión. La traducción inversa reemplaza cada término nuevo por su gráfico puro con nombres auxiliares frescos; el caso $\neg F$ nunca se confunde con la descripción original. $\square$

**Aplicaciones con fronteras explícitas.** Para $\Delta_{\operatorname{Im},\Theta}$, se toma $F=F_\Theta$; se obtiene una función totalizada para **cada $\Theta$ fija**, no una operación sobre todas las fórmulas. Para la intersección absoluta se toma $F(A):\equiv\exists a\,a\in A$. El valor totalizado en la familia vacía es, **por estipulación**, $\varnothing$, y no el imposible conjunto universal. La intersección relativa $\bigcap_U A$ ya es total y no necesita esa estipulación. Ninguna de estas operaciones se añade al alfabeto primitivo $\tau_\in$, ni se presupone que la teoría objeto tenga un modelo.

## 13.32. Cierre de las construcciones y frontera arquitectónica

### Corolario 13.32.1 — Infraestructura conjuntista elemental obtenida en ZF objeto {#tlog-cor-00015}

Las operaciones construidas en §§13.1–13.31 se organizan en tres familias, cada una con condición formal de uso:

1. **Operaciones total y unívocamente definibles:** vacío, par no ordenado, singleton, unión, unión binaria, potencia, separación fijada por una matriz y conjunto ambiente, intersección binaria, diferencia e intersección relativa a $U$. Tienen traducciones puras por grafos únicos; cualquier colección **finita** de sus símbolos puede introducirse conservativamente.
2. **Operaciones funcionales sometidas a hipótesis locales:** $\operatorname{Im}_\Theta(a;\bar p)$ exige funcionalidad de $\Theta$ en el dominio y $\bigcap A$ exige $A\ne\varnothing$. La eliminación contextual de las macros conserva las hipótesis y la eventual totalización requiere distinguir su valor convencional cuando falla la guarda.
3. **Construcciones derivadas por operaciones sucesivas sobre conjuntos:** composición de imágenes, imagen acotada de relación arbitraria y unión de imágenes funcionales. No incorporan comprensión irrestricta ni principios de elección.

**Demostración.** La primera familia procede de las pruebas de existencia/unicidad de M01 y de §13.27; sus expansiones finitas están autorizadas por §13.14. La segunda procede de §§13.18, 13.24 y 13.31, y no convierte una operación parcial en un símbolo funcional primitivo. La tercera sigue de §§13.21–13.22 y §13.29; las transformaciones de membresía son pruebas objeto específicas y la existencia se obtiene siempre de un axioma aplicable sobre un conjunto previamente dado. $\square$

Quedan deliberadamente **para los Capítulos 14–16** las definiciones de par ordenado, productos cartesianos, relaciones y funciones como conjuntos de pares, cocientes, órdenes, naturales y recursión interna. Tampoco se deriva $\operatorname{Con}(\mathsf{ZF}_{\mathrm{obj}})$, no se requiere AC/BPI, no se activa ninguna interfaz intertratados ni se afirma Lean compilado.

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 12](capitulo-12.md) · [Capítulo 14 →](capitulo-14.md)


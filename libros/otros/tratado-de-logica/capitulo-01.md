---
title: Capítulo 1 — Sintaxis proposicional
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
content-id: MA-BCH-0203
content-type: book-chapter
source-id: TLOG-CH01-0001
prerequisites:
- MA-BCH-0202
related:
- MA-BOK-0014
source-sha256: 13185f62cb0cfc1a167904b15ff2c4446e2f2613e92e18df1c49a4ffe8cd2b5e
provenance:
  type: original
  sources: []
---

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 0](capitulo-00.md) · [Capítulo 2 →](capitulo-02.md)

## 1.0. Función del capítulo


El objetivo de este capítulo es construir la sintaxis de un primer lenguaje objeto concreto: la lógica proposicional clásica de referencia de TLOG. Todavía no se asignan valores de verdad, no se define consecuencia semántica y no se introduce ningún cálculo deductivo. Esas tareas pertenecen, respectivamente, a los capítulos 2 y 3.


El capítulo parte de las nociones cerradas en el Capítulo 0:


$$
\text{alfabeto}
\longrightarrow
\text{expresiones finitas}
\longrightarrow
\text{reglas de formación}
\longrightarrow
\text{lenguaje formal}.
$$


Aquí esas nociones se especializan a un lenguaje proposicional y se obtiene el primer principio de inducción estructural del tratado.


### Fuentes efectivamente cotejadas para este bloque


- `TLOG-SRC-0002` — Herbert B. Enderton, *A Mathematical Introduction to Logic*, 2.ª ed. (2001), §1.1, pp. 13–19; §1.3, pp. 29–34; §1.4, pp. 34–44.
- `TLOG-SRC-0003` — Wolfgang Rautenberg, *A Concise Introduction to Mathematical Logic*, 3.ª ed. (2010), cap. 1, §1.1, pp. 4–8.


Enderton funciona como modelo directo para una sintaxis con cinco conectivos primitivos. Rautenberg sirve de contracontrol: muestra explícitamente que la elección de firma puede ser más pequeña y que conectivos adicionales pueden tratarse como abreviaturas. TLOG adopta aquí una decisión propia y deliberada.


## 1.1. Sistema proposicional de referencia


### Convención 1.1.1 — Lenguaje objeto `CPL` {#tlog-cnv-00003}


En la Parte I, mientras no se declare otra cosa, `CPL` designará el sistema proposicional clásico de referencia. En este capítulo sólo fijamos su **capa sintáctica**.


Tomamos un conjunto numerable de variables proposicionales


$$
\mathrm{PV}
=
\{p_n\mid n\in\mathbb N,\ n\ge 1\},
$$


cuyos miembros son símbolos distintos. Adoptamos además como conectivos lógicos **primitivos**:


$$
\neg,\qquad
\land,\qquad
\lor,\qquad
\to,\qquad
\leftrightarrow,
$$


con aridades


$$
1,\qquad 2,\qquad 2,\qquad 2,\qquad 2,
$$


respectivamente. Los paréntesis `(` y `)` son signos auxiliares de puntuación. Todos estos símbolos se toman distintos entre sí y disjuntos de $\mathrm{PV}$.


La elección de cinco conectivos primitivos es una convención de TLOG, no una afirmación de minimalidad funcional. En particular, todavía no se sostiene que alguno pueda definirse semánticamente a partir de los demás: esa cuestión pertenece a la semántica proposicional.


## 1.2. Alfabeto proposicional


### Definición 1.2.1 — Alfabeto de `CPL` {#tlog-def-00005}


Sea


$$
\mathcal C_{\mathrm{CPL}}
=
\{\neg,\land,\lor,\to,\leftrightarrow\}.
$$


El **alfabeto proposicional de `CPL`** es


$$
\Sigma_{\mathrm{CPL}}
:=
\mathrm{PV}
\cup
\mathcal C_{\mathrm{CPL}}
\cup
\{\mathtt{(},\mathtt{)}\}.
$$


Por [TLOG-DEF-00002](capitulo-00.md#tlog-def-00002), una expresión proposicional es cualquier elemento de


$$
\Sigma_{\mathrm{CPL}}^{<\omega}.
$$


Ser una expresión sobre este alfabeto no implica ser una fórmula.


## 1.3. Operaciones constructoras


### Definición 1.3.1 — Constructores proposicionales {#tlog-def-00006}


Sobre el conjunto de expresiones $\Sigma_{\mathrm{CPL}}^{<\omega}$ definimos las siguientes operaciones por concatenación:


$$
E_{\neg}(\alpha)
:=
(\neg\alpha),
$$


y, para cada


$$
\circ\in
\{\land,\lor,\to,\leftrightarrow\},
$$


$$
E_{\circ}(\alpha,\beta)
:=
(\alpha\circ\beta).
$$


Formalmente,


$$
E_{\neg}:
\Sigma_{\mathrm{CPL}}^{<\omega}
\to
\Sigma_{\mathrm{CPL}}^{<\omega},
$$


mientras que cada constructor binario satisface


$$
E_{\circ}:
\bigl(\Sigma_{\mathrm{CPL}}^{<\omega}\bigr)^2
\to
\Sigma_{\mathrm{CPL}}^{<\omega}.
$$


Estas operaciones se definen sobre **todas** las expresiones. La restricción a fórmulas aparecerá en la definición siguiente.


## 1.4. Fórmulas bien formadas


### Definición 1.4.1 — Fórmulas proposicionales de `CPL` {#tlog-def-00007}


Llamaremos


$$
\mathrm{Fm}_{\mathrm{CPL}}
\subseteq
\Sigma_{\mathrm{CPL}}^{<\omega}
$$


al menor conjunto de expresiones que satisface:


1. para todo $n\ge 1$,
   $$
   p_n\in\mathrm{Fm}_{\mathrm{CPL}};
   $$
2. si $\alpha\in\mathrm{Fm}_{\mathrm{CPL}}$, entonces
   $$
   E_{\neg}(\alpha)\in\mathrm{Fm}_{\mathrm{CPL}};
   $$
3. si $\alpha,\beta\in\mathrm{Fm}_{\mathrm{CPL}}$ y
   $$
   \circ\in\{\land,\lor,\to,\leftrightarrow\},
   $$
   entonces
   $$
   E_{\circ}(\alpha,\beta)\in\mathrm{Fm}_{\mathrm{CPL}}.
   $$


La palabra “menor” es parte sustantiva de la definición: no se admiten otras expresiones por una cláusula implícita de “sentido”.


### Existencia del conjunto definido


No estamos presuponiendo el objeto que queremos definir. Sea $\mathcal I$ la familia de todos los subconjuntos


$$
S\subseteq\Sigma_{\mathrm{CPL}}^{<\omega}
$$


que contienen todas las variables proposicionales y son cerrados bajo los cinco constructores. La propia colección


$$
\Sigma_{\mathrm{CPL}}^{<\omega}
$$


pertenece a $\mathcal I$, de modo que $\mathcal I\neq\varnothing$. Por tanto puede tomarse


$$
\mathrm{Fm}_{\mathrm{CPL}}
=
\bigcap\mathcal I.
$$


Esta intersección satisface las tres cláusulas y está contenida en cualquier otro conjunto que las satisfaga. Así queda justificada la existencia y la minimalidad de $\mathrm{Fm}_{\mathrm{CPL}}$.


Por [TLOG-DEF-00004](capitulo-00.md#tlog-def-00004), $\mathrm{Fm}_{\mathrm{CPL}}$ es un lenguaje formal sobre $\Sigma_{\mathrm{CPL}}$.


## 1.5. Primer metateorema sintáctico


### Metateorema 1.5.1 — Principio de inducción estructural proposicional {#tlog-mth-00001}


Sea $P$ una propiedad de fórmulas proposicionales. Supongamos que:


1. $P(p_n)$ vale para todo $n\ge 1$;
2. si $P(\alpha)$, entonces
   $$
   P(E_{\neg}(\alpha));
   $$
3. para cada
   $$
   \circ\in\{\land,\lor,\to,\leftrightarrow\},
   $$
   si $P(\alpha)$ y $P(\beta)$, entonces
   $$
   P(E_{\circ}(\alpha,\beta)).
   $$


Entonces


$$
P(\varphi)
$$


vale para toda


$$
\varphi\in\mathrm{Fm}_{\mathrm{CPL}}.
$$


#### Demostración


Definamos


$$
S_P
=
\{\varphi\in\mathrm{Fm}_{\mathrm{CPL}}
\mid
P(\varphi)\}.
$$


Por la hipótesis 1, todas las variables proposicionales pertenecen a $S_P$. Por las hipótesis 2 y 3, $S_P$ es cerrado bajo todos los constructores proposicionales.


Pero $\mathrm{Fm}_{\mathrm{CPL}}$ es, por [TLOG-DEF-00007](#tlog-def-00007), el **menor** conjunto que contiene las variables proposicionales y es cerrado bajo esos constructores. De aquí se sigue


$$
\mathrm{Fm}_{\mathrm{CPL}}
\subseteq
S_P.
$$


La inclusión inversa es inmediata por la definición de $S_P$. Por tanto,


$$
S_P=\mathrm{Fm}_{\mathrm{CPL}},
$$


y $P$ vale para toda fórmula proposicional. $\square$


## 1.6. Ejemplo desarrollado — construir antes de interpretar


Consideremos


$$
\varphi
=
((p_1\land(\neg p_2))\to p_3).
$$


Su pertenencia a $\mathrm{Fm}_{\mathrm{CPL}}$ puede reconstruirse sin usar ninguna noción de verdad:


1. $p_1,p_2,p_3\in\mathrm{Fm}_{\mathrm{CPL}}$;
2. $E_{\neg}(p_2)=(\neg p_2)\in\mathrm{Fm}_{\mathrm{CPL}}$;
3. 
   $$
   E_{\land}(p_1,E_{\neg}(p_2))
   =
   (p_1\land(\neg p_2))
   \in\mathrm{Fm}_{\mathrm{CPL}};
   $$
4. finalmente,
   $$
   E_{\to}\bigl(
     E_{\land}(p_1,E_{\neg}(p_2)),
     p_3
   \bigr)
   =
   \varphi
   \in
   \mathrm{Fm}_{\mathrm{CPL}}.
   $$


El ejemplo es deliberadamente sintáctico. No afirmamos aún si $\varphi$ es verdadera, satisfacible, válida o demostrable.


## 1.9. Estado tras el primer bloque


Este microtramo **no cierra el Capítulo 1**. Quedan pendientes obligaciones necesarias antes de introducir complejidad y recursión estructural, en particular:


1. demostrar la descomposición y legibilidad única de las fórmulas;
2. fijar subfórmulas;
3. definir rango o complejidad por recursión estructural;
4. justificar el esquema general de recursión sobre fórmulas;
5. auditar las convenciones de omisión de paréntesis sólo después de que la lectura única esté disponible.


Próximo microtramo:


```text
TLOG-CH01-M02
Legibilidad única, subfórmulas, rango y recursión estructural
```

## 1.10. Balance de paréntesis y segmentos iniciales

La legibilidad única no se presume a partir de la apariencia visual de las fórmulas. Primero necesitamos un control puramente sintáctico de sus segmentos iniciales.

Para una expresión finita $s$, sean $L(s)$ y $R(s)$ el número de paréntesis izquierdos y derechos que aparecen en $s$, y definamos su **balance de paréntesis** por

$$
b(s):=L(s)-R(s).
$$

### Lema 1.10.1 — Balance y segmentos iniciales de una fórmula {#tlog-lem-00001}

Para toda fórmula $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$:

1. $b(\varphi)=0$;
2. todo segmento inicial **no vacío y propio** $s$ de $\varphi$ satisface
   $$
   b(s)>0.
   $$

En particular, ninguna fórmula proposicional puede ser un segmento inicial propio de otra fórmula proposicional.

#### Demostración

Aplicamos [TLOG-MTH-00001](#tlog-mth-00001).

**Caso atómico.** Si $\varphi=p_n$, entonces no aparecen paréntesis, de modo que $b(\varphi)=0$. Como $p_n$ es un símbolo único del alfabeto, no tiene segmentos iniciales no vacíos propios.

**Caso unario.** Supongamos que $\varphi=E_{\neg}(\alpha)=(\neg\alpha)$ y que el resultado vale para $\alpha$. El paréntesis exterior aporta $+1$ al comienzo y $-1$ al final; como $b(\alpha)=0$,

$$
b((\neg\alpha))=0.
$$

Antes del último paréntesis derecho queda al menos abierto el paréntesis exterior. Si un segmento termina dentro de $\alpha$, la hipótesis inductiva añade un balance estrictamente positivo cuando el segmento interno es propio. Por tanto todo segmento inicial no vacío propio tiene balance positivo.

**Caso binario.** Supongamos

$$
\varphi=E_{\circ}(\alpha,\beta)=(\alpha\circ\beta),
\qquad
\circ\in\{\land,\lor,\to,\leftrightarrow\},
$$

y que el resultado vale para $\alpha$ y $\beta$. Entonces

$$
b((\alpha\circ\beta))
=
1+b(\alpha)+b(\beta)-1
=
0.
$$

Un segmento inicial propio puede terminar dentro de $\alpha$, después de $\alpha$, en el conectivo, dentro de $\beta$ o justo después de $\beta$; en todos esos casos el paréntesis exterior sigue abierto y la hipótesis inductiva impide que el balance caiga a cero antes del último símbolo.

Así, las dos propiedades valen para toda fórmula. Si una fórmula $\psi$ fuese segmento inicial propio de una fórmula $\varphi$, tendríamos simultáneamente $b(\psi)=0$ y $b(\psi)>0$, contradicción. $\square$

## 1.11. Legibilidad única y generación libre

### Metateorema 1.11.1 — Legibilidad única de las fórmulas proposicionales {#tlog-mth-00002}

Toda fórmula $\varphi\in\mathrm{Fm}_{\mathrm{CPL}}$ pertenece a **exactamente uno** de los siguientes casos:

1. $\varphi=p_n$ para un único $n\ge 1$;
2. $\varphi=E_{\neg}(\alpha)$ para una única fórmula $\alpha$;
3. $\varphi=E_{\circ}(\alpha,\beta)$ para un único
   $$
   \circ\in\{\land,\lor,\to,\leftrightarrow\}
   $$
   y un único par ordenado $(\alpha,\beta)$ de fórmulas.

Equivalentemente, las restricciones de los cinco constructores a $\mathrm{Fm}_{\mathrm{CPL}}$ son inyectivas, sus imágenes son dos a dos disjuntas y todas esas imágenes son disjuntas de $\mathrm{PV}$. Por tanto $\mathrm{Fm}_{\mathrm{CPL}}$ está **libremente generado** por $\mathrm{PV}$ mediante los cinco constructores.

#### Demostración

Las variables proposicionales son símbolos individuales y no comienzan con `(`; toda fórmula construida por $E_{\neg}$ o por algún $E_{\circ}$ sí comienza con `(`. Por tanto el caso atómico es disjunto de los casos compuestos.

Una fórmula de la forma $(\neg\alpha)$ tiene como segundo símbolo $\neg$. En cambio, una fórmula binaria $(\alpha\circ\beta)$ tiene después del primer paréntesis el primer símbolo de $\alpha$, que es o bien alguna variable $p_n$ o bien `(`. Luego la imagen de $E_{\neg}$ es disjunta de las imágenes de los constructores binarios. Además, $E_{\neg}$ es inyectivo por igualdad de secuencias.

Consideremos ahora

$$
(\alpha\circ\beta)
=
(\gamma\star\delta).
$$

Tras eliminar el primer paréntesis izquierdo, $\alpha$ y $\gamma$ aparecen como segmentos iniciales. Si $\alpha\neq\gamma$, uno de ellos tendría que ser segmento inicial propio del otro, porque ambas secuencias coinciden hasta que termina la más corta. Esto contradice [TLOG-LEM-00001](#tlog-lem-00001). Por tanto $\alpha=\gamma$.

El símbolo siguiente queda entonces determinado, de modo que $\circ=\star$, y la igualdad del resto de las secuencias fuerza $\beta=\delta$.

Así, cada constructor binario es inyectivo y las imágenes de constructores binarios distintos son disjuntas. Los tres casos son mutuamente excluyentes y la definición inductiva [TLOG-DEF-00007](#tlog-def-00007) garantiza que agotan todas las fórmulas. $\square$

> [!important] Consecuencia
> Desde este punto, hablar de **conectivo principal**, **constituyente inmediato** o **árbol sintáctico** de una fórmula compuesta es inequívoco.

## 1.12. Recursión estructural

La inducción estructural permite **probar** propiedades de todas las fórmulas. La recursión estructural permite **definir funciones** sobre todas las fórmulas. La segunda requiere más que minimalidad: necesita que una fórmula compuesta no admita dos descomposiciones incompatibles.

### Metateorema 1.12.1 — Teorema de recursión estructural proposicional {#tlog-mth-00003}

Sea $A$ un conjunto. Supongamos dados

$$
g:\mathrm{PV}\to A,
\qquad
F_{\neg}:A\to A,
$$

y, para cada $\circ\in\{\land,\lor,\to,\leftrightarrow\}$, una operación binaria

$$
F_{\circ}:A^2\to A.
$$

Entonces existe una única función

$$
h:\mathrm{Fm}_{\mathrm{CPL}}\to A
$$

tal que

$$
h(p_n)=g(p_n),
$$

$$
h(E_{\neg}(\alpha))
=
F_{\neg}(h(\alpha)),
$$

y

$$
h(E_{\circ}(\alpha,\beta))
=
F_{\circ}(h(\alpha),h(\beta)).
$$

#### Demostración — existencia

Construimos niveles finitos de fórmulas:

$$
F_0:=\mathrm{PV},
$$

$$
F_{k+1}
:=
F_k
\cup
E_{\neg}[F_k]
\cup
\bigcup_{\circ}
E_{\circ}[F_k\times F_k].
$$

Cada $F_k\subseteq\mathrm{Fm}_{\mathrm{CPL}}$. A la inversa,

$$
F_\omega:=\bigcup_{k\in\mathbb N}F_k
$$

contiene $\mathrm{PV}$ y es cerrado bajo los cinco constructores; por la minimalidad de [TLOG-DEF-00007](#tlog-def-00007),

$$
\mathrm{Fm}_{\mathrm{CPL}}
\subseteq
F_\omega.
$$

Luego

$$
\mathrm{Fm}_{\mathrm{CPL}}=F_\omega.
$$

Definimos, por recursión ordinaria sobre $k$, funciones compatibles $h_k:F_k\to A$. Ponemos $h_0=g$. Dado $h_k$, conservamos sus valores sobre $F_k$ y asignamos a cada fórmula nueva de $F_{k+1}\setminus F_k$ el valor prescrito por $F_{\neg}$ o por el $F_{\circ}$ correspondiente. [TLOG-MTH-00002](#tlog-mth-00002) garantiza que una fórmula nueva tiene un único constructor principal y únicos constituyentes inmediatos; no pueden surgir dos prescripciones incompatibles.

Así,

$$
h_{k+1}\!\upharpoonright F_k=h_k.
$$

La unión

$$
h:=\bigcup_{k\in\mathbb N}h_k
$$

es una función total sobre $\mathrm{Fm}_{\mathrm{CPL}}$ y satisface las ecuaciones requeridas.

#### Demostración — unicidad

Sean $h,h'$ dos funciones que satisfacen las mismas cláusulas. Aplicamos [TLOG-MTH-00001](#tlog-mth-00001) a

$$
P(\varphi)\iff h(\varphi)=h'(\varphi).
$$

La cláusula atómica se sigue de $g$. Los pasos unario y binario se siguen de las ecuaciones recursivas y de las hipótesis inductivas. Por tanto $P$ vale para toda fórmula y $h=h'$. $\square$

La construcción usa únicamente recursión ordinaria sobre los naturales en la metateoría de trabajo. No usa Choice y no presupone ninguna valoración semántica.

## 1.13. Subfórmulas

### Definición 1.13.1 — Conjunto de subfórmulas {#tlog-def-00008}

Definimos recursivamente

$$
\operatorname{Sub}_{\mathrm{CPL}}(p_n)
=
\{p_n\},
$$

$$
\operatorname{Sub}_{\mathrm{CPL}}(E_{\neg}(\alpha))
=
\operatorname{Sub}_{\mathrm{CPL}}(\alpha)
\cup
\{E_{\neg}(\alpha)\},
$$

y

$$
\operatorname{Sub}_{\mathrm{CPL}}(E_{\circ}(\alpha,\beta))
=
\operatorname{Sub}_{\mathrm{CPL}}(\alpha)
\cup
\operatorname{Sub}_{\mathrm{CPL}}(\beta)
\cup
\{E_{\circ}(\alpha,\beta)\}.
$$

La propia fórmula es, por convención, una subfórmula de sí misma. Una **subfórmula propia** de $\varphi$ es cualquier elemento de

$$
\operatorname{Sub}_{\mathrm{CPL}}(\varphi)\setminus\{\varphi\}.
$$

La buena definición se obtiene de [TLOG-MTH-00003](#tlog-mth-00003). Como la cláusula necesita recordar la fórmula construida, puede aplicarse el teorema al codominio

$$
\mathrm{Fm}_{\mathrm{CPL}}
\times
\mathcal P(\mathrm{Fm}_{\mathrm{CPL}})
$$

y proyectar luego la segunda coordenada.

## 1.14. Rango sintáctico

### Definición 1.14.1 — Rango de una fórmula {#tlog-def-00009}

El **rango sintáctico**

$$
\operatorname{rk}:
\mathrm{Fm}_{\mathrm{CPL}}
\to
\mathbb N
$$

se define por

$$
\operatorname{rk}(p_n)=0,
$$

$$
\operatorname{rk}(E_{\neg}(\alpha))
=
\operatorname{rk}(\alpha)+1,
$$

$$
\operatorname{rk}(E_{\circ}(\alpha,\beta))
=
1+\max\{\operatorname{rk}(\alpha),\operatorname{rk}(\beta)\}.
$$

El rango mide la máxima profundidad de anidamiento de conectivos, no la longitud tipográfica.

Todo constituyente inmediato de una fórmula compuesta tiene rango estrictamente menor. Por inducción sobre $\varphi$,

$$
\psi\in
\operatorname{Sub}_{\mathrm{CPL}}(\varphi),
\quad
\psi\neq\varphi
\quad\Longrightarrow\quad
\operatorname{rk}(\psi)<\operatorname{rk}(\varphi).
$$

Así queda disponible una medida explícita bien fundada para argumentos posteriores, satisfaciendo `LOG-QA-12`.

## 1.15. Convención de escritura compacta

### Convención 1.15.1 — Omisión controlada de paréntesis {#tlog-cnv-00004}

La sintaxis canónica de `CPL` continúa siendo la sintaxis **completamente parentizada** de [TLOG-DEF-00006](#tlog-def-00006)–`00007`. Se permiten abreviaturas tipográficas que deben expandirse de modo único a esa sintaxis.

Se adopta la precedencia

$$
\neg>\land>\lor>\to>\leftrightarrow.
$$

Además:

1. pueden omitirse los paréntesis exteriores de una fórmula completa;
2. $\neg$ se aplica a la fórmula inmediatamente siguiente según la precedencia anterior;
3. $\to$ asocia hacia la derecha;
4. las repeticiones de $\land,\lor,\leftrightarrow$ asocian hacia la izquierda;
5. ante cualquier posible conflicto, se escriben paréntesis explícitos.

Por ejemplo,

$$
p_1\land\neg p_2\to p_3
$$

abrevia exactamente

$$
((p_1\land(\neg p_2))\to p_3).
$$

Estas convenciones **no amplían** $\mathrm{Fm}_{\mathrm{CPL}}$.

## 1.16. Ejemplo integrado — árbol, subfórmulas y rango

Sea

$$
\varphi=((p_1\land(\neg p_2))\to p_3).
$$

Su conectivo principal es $\to$ y sus constituyentes inmediatos únicos son

$$
(p_1\land(\neg p_2))
\qquad\text{y}\qquad
p_3.
$$

Además,

$$
\operatorname{Sub}_{\mathrm{CPL}}(\varphi)
=
\{
\varphi,\,
(p_1\land(\neg p_2)),\,
p_1,\,
(\neg p_2),\,
p_2,\,
p_3
\},
$$

y

$$
\operatorname{rk}(p_1)
=
\operatorname{rk}(p_2)
=
\operatorname{rk}(p_3)=0,
$$

$$
\operatorname{rk}((\neg p_2))=1,
\qquad
\operatorname{rk}((p_1\land(\neg p_2)))=2,
\qquad
\operatorname{rk}(\varphi)=3.
$$

Con [TLOG-CNV-00004](#tlog-cnv-00004), la misma fórmula puede escribirse

$$
p_1\land\neg p_2\to p_3.
$$

## 1.19. Cierre del capítulo

Las cinco obligaciones dejadas abiertas por `TLOG-CH01-M01` quedan satisfechas:

1. legibilidad única: [TLOG-LEM-00001](#tlog-lem-00001) + [TLOG-MTH-00002](#tlog-mth-00002);
2. subfórmulas: [TLOG-DEF-00008](#tlog-def-00008);
3. rango/complejidad: [TLOG-DEF-00009](#tlog-def-00009);
4. recursión estructural: [TLOG-MTH-00003](#tlog-mth-00003);
5. omisión segura de paréntesis: [TLOG-CNV-00004](#tlog-cnv-00004).

El capítulo cumple la función arquitectónica fijada por `TLOG-ARCH-0001`: **construir fórmulas, complejidad e inducción/recursión sintáctica**.

No se ha introducido ninguna valoración, verdad, satisfacibilidad, validez, consecuencia semántica, axioma lógico o regla de inferencia.

Por tanto,

$$
\boxed{\texttt{TLOG-CH01-0001 — CLOSED}}
$$

```text
chapter nodes = 11
chapter closed nodes = 11
TLOG registered/closed nodes = 17/17
DAG = 17 nodes / 23 direct edges / PASS
formalization candidates = 4
active cross-treaty interfaces = 0
```

El siguiente frente arquitectónico es:

```text
TLOG-CH02-0001 — Semántica proposicional
```

[Índice del tratado](index.qmd) · [Resultados](resultados.qmd) · [Verificación](verificacion.qmd)

[← Capítulo 0](capitulo-00.md) · [Capítulo 2 →](capitulo-02.md)


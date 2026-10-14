---
title: Soluciones — Capítulo 0
content-id: MA-BCH-0177
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-000-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: '2026-10-14'
areas:
- analisis
level: universitario
topics:
- analisis-real
- numeros-reales
- completitud
prerequisites: []
related:
- MA-BOK-0010
provenance:
  type: original
  sources:
  - ANM-C00_SOLUCIONES.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.html)

## §0.1. ¿Existen los números reales?

[]{#MA-SOL-ANM-01-000-001}

[]{#MA-EX-ANM-01-000-001}

### 1. Auditar una especificación antes de usarla

La expresión $A\le u$ aplica una relación entre elementos de $F$ a un conjunto y un elemento. Debe sustituirse por $\forall a\in A:\ a\le u$, que expresa que $u$ es cota superior. La segunda afirmación debe excluir cero: $\forall x\in F\setminus\{0\}\;\exists y\in F:\ xy=1$. En un cuerpo, $0y=0\ne1$ para todo $y$.

La tercera expresión formula correctamente la propiedad del supremo. Bajo no vaciedad y acotación superior, pide $s\in F$ con $a\le s$ para todo $a\in A$ y $s\le v$ para toda cota superior $v$. Son las dos obligaciones de una menor cota superior.

La cuarta, $\sup A\in A$, sólo puede escribirse tras acreditar existencia del supremo y añade una exigencia que no pertenece a su definición. Si se cumple, el supremo es también máximo. Por ejemplo, $\{q\in\mathbb Q:q<1\}$ tiene supremo racional uno, pero no lo contiene: si $u<1$, el racional $(u+1)/2$ pertenece al conjunto y supera a $u$. Así, las expresiones primera y segunda necesitan reparación, la tercera es correcta y la cuarta exige más de lo pedido.

[]{#MA-SOL-ANM-01-000-002}

[]{#MA-EX-ANM-01-000-002}

### 2. Una existencia demostrada suponiendo que ya existe

La primera presuposición aparece en «sea $F$ un cuerpo ordenado completo»: ya se ha introducido un objeto cuya existencia es justamente la conclusión buscada. A partir de esa hipótesis es legítimo deducir sus leyes de cuerpo, compatibilidad del orden y propiedad del supremo. El argumento demuestra una afirmación condicional sobre una estructura supuesta, sin proporcionar un modelo.

Para demostrar existencia habría que construir un conjunto concreto sin atribuirle de antemano toda la estructura, definir sus operaciones y orden, verificar las leyes de cuerpo y su compatibilidad, y demostrar la propiedad del supremo. El objeto así verificado sería un testigo de $\exists F\,(F\text{ es un cuerpo ordenado completo})$. Este ejercicio localiza el trabajo pendiente; todavía no necesita construir ese testigo.

[]{#MA-SOL-ANM-01-000-003}

[]{#MA-EX-ANM-01-000-003}

### 3. Qué tendría que certificar un modelo

La etapa I construye un candidato $M$ con operaciones y relación, pero una fórmula para esos datos no garantiza las leyes que deben cumplir. Las etapas II y III prueban que $M$ es un cuerpo ordenado. Las etapas II y III todavía no verifican la existencia de supremos. Esa exigencia forma parte de la especificación inicial y requiere la etapa IV.

La etapa IV acredita que cada subconjunto no vacío acotado superiormente posee supremo en $M$. Junto con I–III, hace del candidato construido un cuerpo ordenado completo y proporciona un testigo de existencia.

Si otro objeto $N$ superara las mismas verificaciones, existirían dos modelos de la especificación. La pregunta nueva sería si sus estructuras pueden compararse mediante un isomorfismo de cuerpos ordenados y si esa correspondencia es única. La construcción y verificación de $M$ ya habría resuelto existencia; esa comparación necesita su propia prueba.

## §0.2. Extender sin perder estructura: de $\mathbb N$ a $\mathbb Q$

[]{#MA-SOL-ANM-01-000-004}

[]{#MA-EX-ANM-01-000-004}

### 4. Qué significa realmente cada flecha

La frase «inclusiones de cuerpos que conservan toda la estructura» falla por dos razones distintas: atribuye a los dominios más estructura de la que tienen y transforma demasiado pronto una incrustación en una inclusión literal.

Para

$$
\iota_{\mathbb N\mathbb Z}:\mathbb N\longrightarrow\mathbb Z,
$$

la sección exige conservar la estructura que ya está disponible en $\mathbb N$. En particular:

$$
\iota_{\mathbb N\mathbb Z}(m+n)
=
\iota_{\mathbb N\mathbb Z}(m)+\iota_{\mathbb N\mathbb Z}(n),
$$

$$
\iota_{\mathbb N\mathbb Z}(mn)
=
\iota_{\mathbb N\mathbb Z}(m)\,
\iota_{\mathbb N\mathbb Z}(n),
$$

y

$$
m<n
\iff
\iota_{\mathbb N\mathbb Z}(m)
<
\iota_{\mathbb N\mathbb Z}(n).
$$

Además, los elementos distinguidos $0$ y $1$ se transportan a los correspondientes $0$ y $1$ de $\mathbb Z$. La aplicación debe ser inyectiva para que números naturales distintos no se colapsen.

En cambio, para

$$
\iota_{\mathbb Z\mathbb Q}:\mathbb Z\longrightarrow\mathbb Q,
$$

el dominio ya tiene estructura de anillo ordenado. Por eso deben conservarse suma, producto, $0$, $1$ y orden, además de la inyectividad.

No es correcto comenzar diciendo que las flechas son inclusiones literales. Lo que tenemos primero es una aplicación inyectiva que preserva la estructura pertinente. Su imagen

$$
\iota(A)\subseteq B
$$

sí es literalmente un subconjunto del codominio. Sólo después de verificar que $A$ y $\iota(A)$ son copias estructurales podemos adoptar la convención de identificar ambos y escribir

$$
A\subseteq B.
$$

Finalmente, la expresión «inclusiones de cuerpos» está mal tipada porque ni $\mathbb N$ ni $\mathbb Z$ son cuerpos. La descripción correcta es, esquemáticamente,

$$
\boxed{
\mathbb N
\hookrightarrow
\mathbb Z
\hookrightarrow
\mathbb Q
}
$$

donde cada flecha preserva exactamente la estructura disponible en su dominio; en particular, la segunda puede describirse como una incrustación de anillos ordenados.

[]{#MA-SOL-ANM-01-000-005}

[]{#MA-EX-ANM-01-000-005}

### 5. Construir la flecha directa de $\mathbb N$ a $\mathbb Q$

Definimos

$$
\iota_{\mathbb N\mathbb Q}
=
\iota_{\mathbb Z\mathbb Q}
\circ
\iota_{\mathbb N\mathbb Z}.
$$

Bajo las representaciones canónicas de §0.2,

$$
\iota_{\mathbb N\mathbb Z}(n)=n
$$

como entero correspondiente, y luego

$$
\iota_{\mathbb Z\mathbb Q}(n)=\frac n1.
$$

Por tanto,

$$
\boxed{
\iota_{\mathbb N\mathbb Q}(n)=\frac n1.
}
$$

En particular,

$$
0\mapsto\frac01,
\qquad
1\mapsto\frac11,
\qquad
2\mapsto\frac21,
\qquad
3\mapsto\frac31.
$$

Para la suma,

$$
\begin{aligned}
\iota_{\mathbb N\mathbb Q}(m+n)
&=
\iota_{\mathbb Z\mathbb Q}
\bigl(
\iota_{\mathbb N\mathbb Z}(m+n)
\bigr)\\
&=
\iota_{\mathbb Z\mathbb Q}
\bigl(
\iota_{\mathbb N\mathbb Z}(m)
+
\iota_{\mathbb N\mathbb Z}(n)
\bigr)\\
&=
\iota_{\mathbb N\mathbb Q}(m)
+
\iota_{\mathbb N\mathbb Q}(n).
\end{aligned}
$$

El mismo razonamiento produce

$$
\iota_{\mathbb N\mathbb Q}(mn)
=
\iota_{\mathbb N\mathbb Q}(m)\,
\iota_{\mathbb N\mathbb Q}(n).
$$

La composición de dos aplicaciones inyectivas es inyectiva: si

$$
\iota_{\mathbb N\mathbb Q}(m)
=
\iota_{\mathbb N\mathbb Q}(n),
$$

la inyectividad de $\iota_{\mathbb Z\mathbb Q}$ permite concluir

$$
\iota_{\mathbb N\mathbb Z}(m)
=
\iota_{\mathbb N\mathbb Z}(n),
$$

y luego la inyectividad de $\iota_{\mathbb N\mathbb Z}$ da $m=n$.

Para el orden, si $m<n$, la primera incrustación produce

$$
\iota_{\mathbb N\mathbb Z}(m)
<
\iota_{\mathbb N\mathbb Z}(n),
$$

y la segunda conserva esa relación, de modo que

$$
\iota_{\mathbb N\mathbb Q}(m)
<
\iota_{\mathbb N\mathbb Q}(n).
$$

La reflexión del orden se obtiene recorriendo las equivalencias en sentido contrario.

Después de estas verificaciones, identificamos $\mathbb N$ con la imagen

$$
\iota_{\mathbb N\mathbb Q}(\mathbb N)
=
\left\{
\frac n1:n\in\mathbb N
\right\}
\subseteq\mathbb Q.
$$

Sólo entonces la escritura

$$
\mathbb N\subseteq\mathbb Q
$$

funciona como una economía notacional sustentada por la incrustación.

[]{#MA-SOL-ANM-01-000-006}

[]{#MA-EX-ANM-01-000-006}

### 6. La composición de incrustaciones vuelve a ser una incrustación

Sea

$$
\lambda=\kappa\circ\iota.
$$

Primero probemos que $\lambda$ es inyectiva. Supongamos que

$$
\lambda(a)=\lambda(a').
$$

Entonces

$$
\kappa(\iota(a))
=
\kappa(\iota(a')).
$$

Como $\kappa$ es inyectiva,

$$
\iota(a)=\iota(a').
$$

Y como $\iota$ también es inyectiva,

$$
a=a'.
$$

Para la suma,

$$
\begin{aligned}
\lambda(a+a')
&=
\kappa(\iota(a+a'))\\
&=
\kappa(\iota(a)+\iota(a'))\\
&=
\kappa(\iota(a))
+
\kappa(\iota(a'))\\
&=
\lambda(a)+\lambda(a').
\end{aligned}
$$

Análogamente,

$$
\begin{aligned}
\lambda(aa')
&=
\kappa(\iota(aa'))\\
&=
\kappa(\iota(a)\iota(a'))\\
&=
\kappa(\iota(a))
\kappa(\iota(a'))\\
&=
\lambda(a)\lambda(a').
\end{aligned}
$$

Para el orden, encadenamos las equivalencias:

$$
a<a'
\iff
\iota(a)<\iota(a')
\iff
\kappa(\iota(a))
<
\kappa(\iota(a')).
$$

Es decir,

$$
a<a'
\iff
\lambda(a)<\lambda(a').
$$

Por tanto, $\lambda$ es inyectiva, conserva suma y producto y preserva y refleja el orden. Es una incrustación al mismo nivel estructural.

Aplicado a

$$
\mathbb N
\hookrightarrow
\mathbb Z
\hookrightarrow
\mathbb Q,
$$

el resultado muestra que las dos flechas canónicas determinan una incrustación compuesta

$$
\mathbb N\hookrightarrow\mathbb Q.
$$

La cadena no es sólo una sucesión de inclusiones visuales: las compatibilidades estructurales se transmiten a través de la composición.

[]{#MA-SOL-ANM-01-000-007}

[]{#MA-EX-ANM-01-000-007}

### 7. Una aplicación inyectiva no basta

La aplicación $f(n)=2n$ es inyectiva: $2m=2n$ implica $m=n$. También preserva y refleja el orden, porque $m<n$ equivale a $2m<2n$, y conserva la suma: $f(m+n)=2m+2n=f(m)+f(n)$. Por tanto transporta fielmente el grupo aditivo ordenado de los enteros a su imagen.

La unidad no se conserva, pues $f(1)=2\ne1$. Tampoco el producto: $f(mn)=2mn$, mientras $f(m)f(n)=4mn$. Basta $m=n=1$ para obtener dos y cuatro. La igualdad puede darse para algunos pares, como los que tienen un factor cero, pero la preservación requerida es universal.

Así no es la incrustación de anillos ordenados que preserva la aritmética entera dentro de $\mathbb Q$. Identificar $n$ con $2n$ usando las operaciones ambientales conservaría suma y orden, pero cambiaría unidad y producto. La copia debe declararse respecto de la estructura que realmente conserva.

## §0.3. El obstáculo: $\mathbb Q$ no está completo

[]{#MA-SOL-ANM-01-000-008}

[]{#MA-EX-ANM-01-000-008}

### 8. Construir un racional que escape por la derecha

El conjunto

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío porque

$$
1\in S_2.
$$

Además, $2$ es una cota superior racional. En efecto, si $q\in S_2$ y $q\ge2$, entonces $q\ge0$ y

$$
q^2\ge4>2,
$$

contradicción. Por tanto todo $q\in S_2$ satisface $q<2$.

Ahora sea $s\in\mathbb Q$ con $1\le s$ y $s^2<2$, y definamos

$$
\delta=\frac{2-s^2}{4s+4}.
$$

Numerador y denominador son racionales, y el denominador es no nulo; luego $\delta\in\mathbb Q$. Como $2-s^2>0$ y $4s+4>0$,

$$
\delta>0.
$$

Además, de $s\ge1$ y $s^2<2$ obtenemos

$$
0<2-s^2\le1,
\qquad
4s+4\ge8,
$$

de modo que

$$
0<\delta\le\frac18<1.
$$

Sea

$$
u=s+\delta.
$$

Claramente $u>s$ y $u\in\mathbb Q$. Falta probar que $u^2<2$. Como $0<\delta<1$,

$$
\delta^2<\delta.
$$

Por tanto

$$
\begin{aligned}
u^2
&=(s+\delta)^2\\
&=s^2+2s\delta+\delta^2\\
&<s^2+(2s+1)\delta.
\end{aligned}
$$

Ahora

$$
(2s+1)\delta
=(2-s^2)\frac{2s+1}{4s+4}.
$$

Como

$$
0<\frac{2s+1}{4s+4}<1,
$$

se sigue que

$$
(2s+1)\delta<2-s^2.
$$

Así,

$$
u^2< s^2+(2-s^2)=2.
$$

Además $u>0$, de modo que $u\in S_2$.

Hemos construido racionalmente

$$
\boxed{s<u\in S_2.}
$$

Por eso ningún racional $s$ con $s^2<2$ puede ser una cota superior de $S_2$: siempre podemos fabricar un elemento del conjunto que queda estrictamente a su derecha.

*Referencia visual.* Véase la figura [C00-F03](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f03) del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-009}

[]{#MA-EX-ANM-01-000-009}

### 9. Mejorar una cota que queda demasiado a la derecha

Sea $s\in\mathbb Q$, $s>0$ y $s^2>2$. Definimos

$$
\delta=\frac{s^2-2}{4s},
\qquad
t=s-\delta.
$$

Como $s^2-2>0$ y $4s>0$,

$$
\delta>0.
$$

También

$$
s^2-2<4s^2,
$$

pues esto equivale a

$$
0<3s^2+2,
$$

que es cierto. Al dividir por $4s>0$ obtenemos

$$
\delta<s.
$$

Por tanto

$$
0<t=s-\delta<s.
$$

Calculemos:

$$
\begin{aligned}
t^2
&=(s-\delta)^2\\
&=s^2-2s\delta+\delta^2\\
&>s^2-2s\delta\\
&=s^2-\frac{s^2-2}{2}\\
&=\frac{s^2+2}{2}\\
&>2.
\end{aligned}
$$

Ahora sea $q\in S_2$. Si $q\ge t$, entonces $q\ge0$ y $t>0$, de modo que

$$
q^2\ge t^2>2,
$$

contradiciendo la definición de $S_2$. Por consiguiente,

$$
q<t
$$

para todo $q\in S_2$.

Esto dice exactamente que $t$ es una cota superior racional de $S_2$. Pero además

$$
t<s.
$$

Así, cualquier supuesto supremo racional $s$ con $s^2>2$ dejaría de ser la menor cota superior, porque acabamos de construir otra cota superior estrictamente menor.

*Referencia visual.* Véase la figura [C00-F03](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f03) del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-010}

[]{#MA-EX-ANM-01-000-010}

### 10. Ningún candidato racional sobrevive

Supongamos, para obtener una contradicción, que existe

$$
s=\sup_{\mathbb Q}S_2.
$$

Como $1\in S_2$, toda cota superior de $S_2$ debe satisfacer $s\ge1$. Y como $2$ es una cota superior racional,

$$
s\le2.
$$

Luego

$$
1\le s\le2.
$$

En particular $s>0$. Por tricotomía, exactamente uno de los tres casos siguientes debe ocurrir.

Si $s^2<2$, el ejercicio 8 construye un racional $u$ tal que

$$
s<u\in S_2.
$$

Eso contradice que $s$ sea cota superior.

Si $s^2>2$, el ejercicio 9 construye un racional $t$ tal que

$$
t<s
$$

y $t$ sigue siendo cota superior de $S_2$. Eso contradice que $s$ sea la menor cota superior.

Queda el caso

$$
s^2=2.
$$

Escribamos

$$
s=\frac mn
$$

con $m,n\in\mathbb Z$, $n>0$ y $m/n$ en términos mínimos. Entonces

$$
m^2=2n^2.
$$

Así $m^2$ es par, luego $m$ es par. Escribamos $m=2k$. Sustituyendo,

$$
4k^2=2n^2,
$$

y por tanto

$$
n^2=2k^2.
$$

Entonces $n$ también es par. Esto contradice que $m/n$ estuviera en términos mínimos.

Por consiguiente, ningún racional satisface $s^2=2$.

Los tres casos son imposibles. Por tanto,

$$
\boxed{S_2\text{ no posee supremo en }\mathbb Q.}
$$

Como $S_2$ es no vacío y está acotado superiormente, hemos encontrado un contraejemplo directo a la propiedad del supremo dentro de $\mathbb Q$. En consecuencia,

$$
\boxed{\mathbb Q\text{ no es completo para la propiedad del supremo}.}
$$

Toda la prueba ha permanecido en aritmética racional.

*Referencia visual.* Véase la figura [C00-F03](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f03) del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-011}

[]{#MA-EX-ANM-01-000-011}

### 11. Una prueba que introduce demasiado pronto la frontera

La primera premisa no disponible es «en $\mathbb R$ existe $\sqrt2$»: el capítulo todavía está construyendo un cuerpo ordenado completo. También la aproximación racional a esa frontera presupone una copia de $\mathbb Q$ en un sistema ordenado mayor y densidad allí. La densidad racional disponible sólo inserta racionales entre extremos racionales.

Si ese sistema mayor estuviera ya construido, y se hubieran acreditado tanto la raíz positiva de dos como la densidad de su copia racional, el argumento externo podría identificar el supremo de $S_2$ con esa raíz. Después, su irracionalidad excluiría un supremo racional. Esa conclusión posterior no constituye la justificación racional requerida en §0.3.

La reparación toma un supuesto $s=\sup_{\mathbb Q}S_2$, obtiene $1\le s\le2$ y separa los casos $s^2<2$, $s^2>2$ y $s^2=2$. Las perturbaciones de los ejercicios 8 y 9 contradicen, respectivamente, que sea cota superior y que sea la menor. La paridad de una fracción irreducible excluye el caso de igualdad. Los tres argumentos permanecen en $\mathbb Q$ y no presuponen una frontera externa.

[]{#MA-SOL-ANM-01-000-012}

[]{#MA-EX-ANM-01-000-012}

### 12. Denso, pero no completo

Tomemos dos racionales $p<q$. El punto medio

$$
r=\frac{p+q}{2}
$$

es racional y satisface

$$
p<r<q.
$$

Por tanto $\mathbb Q$ es denso en el sentido pertinente: entre dos racionales distintos siempre hay otro racional.

Sin embargo, el ejercicio 10 mostró que

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío, está acotado superiormente en $\mathbb Q$ y no posee supremo racional. Luego $\mathbb Q$ no es completo para la propiedad del supremo.

Así, $\mathbb Q$ es ya el contraejemplo solicitado a la implicación

$$
\text{densidad}
\Longrightarrow
\text{completitud}.
$$

Conviene separar todavía otra confusión. Consideremos

$$
A=\{q\in\mathbb Q:q<1\}.
$$

El conjunto $A$ no tiene máximo. En efecto, si $q\in A$, entonces

$$
q<\frac{q+1}{2}<1,
$$

y el número $(q+1)/2$ es racional y pertenece a $A$. Por tanto ningún elemento de $A$ puede ser el mayor.

No obstante,

$$
\sup_{\mathbb Q}A=1.
$$

El número $1$ es una cota superior de $A$. Además, si $u<1$ fuera otra cota superior racional, entonces

$$
r=\frac{u+1}{2}
$$

sería racional y cumpliría

$$
u<r<1.
$$

Así $r\in A$ y $r>u$, contradiciendo que $u$ fuera cota superior. Luego ninguna cota superior puede ser menor que $1$.

Tenemos entonces dos fenómenos distintos dentro del mismo sistema:

$$
A\text{ no tiene máximo, pero sí supremo racional},
$$

mientras que

$$
S_2\text{ no tiene supremo racional}.
$$

Por eso «no tener máximo» no equivale a «no tener supremo».

La distinción final es:

$$
\boxed{
\text{densidad: qué ocurre entre puntos ya presentes;}
\qquad
\text{completitud: si existen dentro del sistema las fronteras exigidas.}
}
$$

## §0.4. Construir una frontera sin tener el punto

*Referencia visual.* Véase la figura [C00-F03](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f03) del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-013}

[]{#MA-EX-ANM-01-000-013}

### 13. Auditar las cuatro condiciones de una cortadura

Recordemos las cuatro condiciones separadas:

$$
A\ne\varnothing,\qquad
A\subsetneq\mathbb Q,
$$

clausura hacia abajo y ausencia de máximo.

Para

$$
B_1=\{q\in\mathbb Q:q<3\},
$$

las cuatro se cumplen. Es no vacío, por ejemplo $0\in B_1$; es propio porque $3\notin B_1$; si $q<3$ y $r<q$, entonces $r<3$; y si $q<3$, el racional

$$
r=\frac{q+3}{2}
$$

satisface

$$
q<r<3.
$$

Por tanto $r\in B_1$ y $B_1$ no tiene máximo. Así,

$$
B_1\in\mathcal D.
$$

Para

$$
B_2=\{q\in\mathbb Q:q\le3\},
$$

las tres primeras condiciones se cumplen, pero la cuarta falla: $3\in B_2$ y todo $q\in B_2$ satisface $q\le3$. Por tanto $3$ es máximo de $B_2$. Luego $B_2\notin\mathcal D$.

Para

$$
B_3=\mathbb Q,
$$

fallan la segunda condición y sólo ésa entre las cuatro: $B_3$ no es un subconjunto propio de $\mathbb Q$. Es no vacío, está cerrado hacia abajo y no tiene máximo, porque dado cualquier racional $q$, también $q+1\in\mathbb Q$ y $q<q+1$. Así $B_3\notin\mathcal D$.

Para

$$
B_4=\varnothing,
$$

falla la no vaciedad. La clausura hacia abajo y la ausencia de máximo son verdaderas de manera vacía, y $\varnothing\subsetneq\mathbb Q$, pero una cortadura debe contener al menos un racional. Por tanto $B_4\notin\mathcal D$.

Finalmente,

$$
B_5=\{q\in\mathbb Q:q<0\ \text{o}\ 1<q<2\}
$$

es no vacío y propio. Tampoco tiene máximo: si $q<0$, entonces $q<q/2<0$; si $1<q<2$, entonces $q<(q+2)/2<2$ y el nuevo racional sigue siendo mayor que uno. En ambos casos se obtiene un miembro estrictamente mayor de $B_5$. Sin embargo, no está cerrado hacia abajo. Por ejemplo,

$$
\frac32\in B_5,
$$

pero

$$
\frac12<\frac32
$$

y

$$
\frac12\notin B_5.
$$

Luego $B_5\notin\mathcal D$.

La clasificación es entonces:

$$
\boxed{
B_1\in\mathcal D,
\qquad
B_2,B_3,B_4,B_5\notin\mathcal D.
}
$$

El control de tipos es igualmente importante. Si $A\in\mathcal D$, entonces

$$
A\subseteq\mathbb Q.
$$

Si además $q\in A$, entonces necesariamente

$$
q\in\mathbb Q.
$$

Pero $A$ mismo no es un racional: es un conjunto de racionales. Por eso las expresiones correctas distinguen

$$
A\in\mathcal D,
\qquad
A\subseteq\mathbb Q,
\qquad
q\in A,
\qquad
q\in\mathbb Q.
$$

*Referencia visual.* Véase la figura [C00-F04](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f04) del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-014}

[]{#MA-EX-ANM-01-000-014}

### 14. Construir la cortadura determinada por un racional

Sea $c\in\mathbb Q$ y definamos

$$
c^*=\{q\in\mathbb Q:q<c\}.
$$

**No vaciedad.** Como $c-1<c$,

$$
c-1\in c^*.
$$

Por tanto $c^*\ne\varnothing$.

**Subconjunto propio.** Por definición,

$$
c\notin c^*.
$$

Así,

$$
c^*\subsetneq\mathbb Q.
$$

**Clausura hacia abajo.** Si $q\in c^*$ y $r<q$, entonces

$$
q<c.
$$

Por transitividad,

$$
r<q<c,
$$

y por tanto $r<c$. Luego $r\in c^*$.

**Ausencia de máximo.** Sea $q\in c^*$. Entonces $q<c$. Definimos

$$
r=\frac{q+c}{2}.
$$

Como $q<c$,

$$
q<\frac{q+c}{2}<c.
$$

Además $r\in\mathbb Q$. Por tanto

$$
q<r
\qquad\text{y}\qquad
r\in c^*.
$$

Ningún elemento de $c^*$ puede ser máximo.

Hemos verificado las cuatro condiciones, así que

$$
\boxed{c^*\in\mathcal D.}
$$

Consideremos ahora

$$
B_c=\{q\in\mathbb Q:q\le c\}.
$$

Este conjunto contiene a $c$, y $c$ es su máximo. Por ello falla exactamente la condición de ausencia de máximo. Si admitiéramos tanto $c^*$ como $B_c$, una misma frontera racional quedaría codificada por dos conjuntos distintos.

La convención de excluir máximos fuerza un único código del lado izquierdo:

$$
\boxed{c^*=\{q\in\mathbb Q:q<c\}.}
$$

Todavía no hemos probado que la aplicación $c\mapsto c^*$ preserve el orden; aquí sólo hemos construido y verificado que cada racional determina una cortadura.

[]{#MA-SOL-ANM-01-000-015}

[]{#MA-EX-ANM-01-000-015}

### 15. Reparar $S_2$ hasta obtener una cortadura

Partimos de

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}.
$$

El conjunto no es una cortadura porque falla la clausura hacia abajo. En efecto,

$$
1\in S_2,
$$

pero

$$
-2<1
$$

y

$$
-2\notin S_2,
$$

ya que $-2$ no satisface $q\ge0$.

Para reparar ese defecto definimos

$$
A_2=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.
$$

Verifiquemos las cuatro condiciones.

**No vaciedad.** Tenemos

$$
0\in A_2
$$

porque $0^2<2$.

**Subconjunto propio.** El racional $2$ no pertenece a $A_2$, pues

$$
2\not<0
\qquad\text{y}\qquad
2^2=4\not<2.
$$

Así $A_2\subsetneq\mathbb Q$.

**Clausura hacia abajo.** Sea $q\in A_2$ y $r<q$.

Si $q<0$, entonces $r<0$, de modo que $r\in A_2$.

Si $q\ge0$, la pertenencia $q\in A_2$ implica $q^2<2$. Si $r<0$, nuevamente $r\in A_2$. Si

$$
0\le r<q,
$$

entonces

$$
r^2<q^2<2,
$$

y también $r\in A_2$.

Por tanto $A_2$ es cerrado hacia abajo.

**Ausencia de máximo.** Sea $q\in A_2$.

Si $q<0$, tomamos

$$
r=\frac q2.
$$

Como $q<0$,

$$
q<\frac q2<0,
$$

de modo que $r\in A_2$ y $r>q$.

Si $q\ge0$, entonces $q^2<2$. Definimos

$$
\delta=\frac{2-q^2}{2q+3}.
$$

El numerador y el denominador son racionales y positivos, por lo que

$$
\delta\in\mathbb Q,
\qquad
\delta>0.
$$

Además,

$$
2-q^2\le2
\qquad\text{y}\qquad
2q+3\ge3,
$$

de donde

$$
0<\delta<1.
$$

Así $\delta^2<\delta$. Entonces

$$
\begin{aligned}
(q+\delta)^2
&=q^2+2q\delta+\delta^2\\
&<q^2+(2q+1)\delta\\
&=q^2+(2-q^2)\frac{2q+1}{2q+3}\\
&<q^2+(2-q^2)\\
&=2.
\end{aligned}
$$

Por tanto

$$
q+\delta\in A_2
\qquad\text{y}\qquad
q+\delta>q.
$$

En ambos casos todo elemento de $A_2$ admite otro elemento de $A_2$ estrictamente mayor. Luego $A_2$ no tiene máximo.

Concluimos:

$$
\boxed{A_2\in\mathcal D.}
$$

La construcción no ha introducido ninguna frontera externa. $A_2$ es literalmente un subconjunto de $\mathbb Q$, definido mediante desigualdades y operaciones racionales. Incluso el avance $q\mapsto q+\delta$ permanece enteramente dentro de $\mathbb Q$.

*Referencia visual.* Véase la figura [C00-F04](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f04) del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-016}

[]{#MA-EX-ANM-01-000-016}

### 16. La inclusión ordena linealmente todas las cortaduras

Sean $A,B\in\mathcal D$.

Si

$$
A\subseteq B,
$$

ya tenemos una de las dos comparaciones requeridas.

Supongamos entonces

$$
A\not\subseteq B.
$$

Existe algún

$$
a\in A\setminus B.
$$

Tomemos un elemento arbitrario $b\in B$.

No puede ocurrir $a<b$. Si ocurriera, como $b\in B$ y $B$ es cerrado hacia abajo, tendríamos

$$
a\in B,
$$

contradiciendo $a\notin B$.

Tampoco puede ocurrir

$$
a=b,
$$

porque $b\in B$ y $a\notin B$.

Como el orden de $\mathbb Q$ satisface tricotomía, sólo queda

$$
b<a.
$$

Ahora $a\in A$ y $A$ es cerrado hacia abajo. Por tanto

$$
b\in A.
$$

El elemento $b\in B$ era arbitrario, así que

$$
B\subseteq A.
$$

Hemos probado que para cualesquiera $A,B\in\mathcal D$,

$$
\boxed{
A\subseteq B
\quad\text{o}\quad
B\subseteq A.
}
$$

Definimos

$$
A\le_{\mathcal D}B
\iff
A\subseteq B.
$$

La inclusión de conjuntos es reflexiva:

$$
A\subseteq A;
$$

es antisimétrica:

$$
A\subseteq B
\ \text{y}\
B\subseteq A
\Longrightarrow
A=B;
$$

y es transitiva:

$$
A\subseteq B
\ \text{y}\
B\subseteq C
\Longrightarrow
A\subseteq C.
$$

La comparabilidad que acabamos de demostrar añade la propiedad que faltaba. Por tanto,

$$
\boxed{\le_{\mathcal D}\text{ es un orden lineal sobre }\mathcal D.}
$$

El paso estructural decisivo es que la clausura hacia abajo convierte un único testigo $a\in A\setminus B$ en información sobre todos los elementos de $B$.

*Referencia visual.* Véase la figura [C00-F04](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f04) del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-017}

[]{#MA-EX-ANM-01-000-017}

### 17. Situar $A_2$ entre dos cortaduras racionales

Recordemos

$$
1^*=\{q\in\mathbb Q:q<1\},
\qquad
2^*=\{q\in\mathbb Q:q<2\},
$$

y

$$
A_2=\{q\in\mathbb Q:q<0\ \text{o}\ q^2<2\}.
$$

Primero probemos

$$
1^*\subseteq A_2.
$$

Sea $q<1$. Si $q<0$, entonces $q\in A_2$. Si $0\le q<1$, entonces

$$
q^2<1<2,
$$

así que también $q\in A_2$.

La inclusión es estricta. Por ejemplo,

$$
\frac43>1
$$

y

$$
\left(\frac43\right)^2=\frac{16}{9}<2.
$$

Por tanto

$$
\frac43\in A_2\setminus1^*,
$$

y así

$$
1^*\subsetneq A_2.
$$

Ahora probemos

$$
A_2\subseteq2^*.
$$

Sea $q\in A_2$. Si $q<0$, ciertamente $q<2$. Si $q\ge0$, entonces $q^2<2$. No puede ocurrir $q\ge2$, pues eso implicaría

$$
q^2\ge4>2.
$$

Luego $q<2$, y por tanto $q\in2^*$.

La inclusión también es estricta. En efecto,

$$
\frac32<2,
$$

de modo que

$$
\frac32\in2^*,
$$

pero

$$
\left(\frac32\right)^2=\frac94>2,
$$

y $\frac32\not<0$. Así,

$$
\frac32\notin A_2.
$$

Concluimos

$$
\boxed{
1^*\subsetneq A_2\subsetneq2^*.
}
$$

Falta demostrar que $A_2$ no es una cortadura racional.

Supongamos, para obtener una contradicción, que existe $c\in\mathbb Q$ tal que

$$
A_2=c^*.
$$

Como

$$
0\in A_2=c^*,
$$

por la definición de $c^*$ tenemos

$$
0<c.
$$

Ahora aplicamos tricotomía a $c^2$ y $2$.

Si

$$
c^2<2,
$$

entonces, como $c>0$,

$$
c\in A_2.
$$

Pero

$$
c\notin c^*
$$

por definición. Esto contradice $A_2=c^*$.

Si

$$
c^2=2,
$$

contradecimos el resultado de §0.3 según el cual ningún racional tiene cuadrado igual a $2$.

Finalmente, supongamos

$$
c^2>2.
$$

Como $c>0$, la perturbación racional de §0.3 produce un racional $t$ tal que

$$
0<t<c
\qquad\text{y}\qquad
t^2>2.
$$

De $t<c$ obtenemos

$$
t\in c^*.
$$

Pero $t>0$ y $t^2>2$, por lo que

$$
t\notin A_2.
$$

Nuevamente contradicción.

Los tres casos son imposibles. Por tanto,

$$
\boxed{
A_2\ne c^*
\quad\text{para todo }c\in\mathbb Q.
}
$$

La conclusión disponible en §0.4 es estrictamente estructural:

$$
\boxed{
1^*\subsetneq A_2\subsetneq2^*
\quad\text{y}\quad
A_2\text{ no es una cortadura racional}.
}
$$

Esto sitúa a $A_2$ en el orden por inclusión sin identificarla todavía con ningún número real previamente existente.

## §0.5. Una copia de $\mathbb Q$ dentro del nuevo sistema

*Referencia visual.* Véase la figura [C00-F05](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f05) del texto principal, **La copia racional q↦q***, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-018}

[]{#MA-EX-ANM-01-000-018}

### 18. Construir la aplicación racional hacia $\mathcal D$

Para cada $q\in\mathbb Q$ definimos

$$
q^*=\{r\in\mathbb Q:r<q\}.
$$

En §0.4 ya se verificó que este subconjunto satisface las cuatro condiciones de una cortadura de Dedekind. Por tanto,

$$
q^*\in\mathcal D
$$

para todo $q\in\mathbb Q$.

Eso garantiza que la regla

$$
\iota_{\mathbb Q}(q)=q^*
$$

tiene efectivamente valores en $\mathcal D$. Luego queda bien definida la aplicación

$$
\boxed{
\iota_{\mathbb Q}:\mathbb Q\longrightarrow\mathcal D,
\qquad
q\longmapsto q^*.
}
$$

Las tres imágenes pedidas son

$$
\iota_{\mathbb Q}\left(-\frac32\right)
=
\left(-\frac32\right)^*
=
\left\{r\in\mathbb Q:r<-\frac32\right\},
$$

$$
\iota_{\mathbb Q}(0)
=
0^*
=
\{r\in\mathbb Q:r<0\},
$$

y

$$
\iota_{\mathbb Q}\left(\frac74\right)
=
\left(\frac74\right)^*
=
\left\{r\in\mathbb Q:r<\frac74\right\}.
$$

Los tipos deben mantenerse separados. Si $q\in\mathbb Q$, entonces

$$
q
$$

es un racional, mientras que

$$
q^*
$$

es un subconjunto de $\mathbb Q$ que, además, pertenece al nuevo dominio:

$$
q^*\subseteq\mathbb Q,
\qquad
q^*\in\mathcal D.
$$

No tendría sentido escribir $q\in\mathcal D$ sólo por haber construido $q^*$, ni confundir la pertenencia

$$
q^*\in\mathcal D
$$

con la inclusión

$$
q^*\subseteq\mathbb Q.
$$

La imagen de la aplicación es

$$
\mathcal Q^*
=
\iota_{\mathbb Q}(\mathbb Q)
=
\{q^*:q\in\mathbb Q\}.
$$

Como todos los $q^*$ son elementos de $\mathcal D$,

$$
\boxed{\mathcal Q^*\subseteq\mathcal D.}
$$

En este punto hemos construido una aplicación desde $\mathbb Q$ hacia $\mathcal D$ y un subconjunto concreto $\mathcal Q^*$ de $\mathcal D$. Todavía no hemos identificado literalmente $\mathbb Q$ con esa imagen.

*Referencia visual.* Véase la figura [C00-F05](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.html#fig-anm-c00-f05) del texto principal, **La copia racional q↦q***, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-019}

[]{#MA-EX-ANM-01-000-019}

### 19. Recuperar exactamente el orden racional

Supongamos primero

$$
p<q.
$$

Sea $r\in p^*$. Por definición,

$$
r<p.
$$

Como $p<q$, la transitividad del orden racional da

$$
r<q.
$$

Por tanto $r\in q^*$. Hemos probado

$$
p^*\subseteq q^*.
$$

La inclusión es estricta porque el propio $p$ sirve como testigo:

$$
p<q
\Longrightarrow
p\in q^*,
$$

mientras que

$$
p\notin p^*
$$

porque $p<p$ es falso. Así,

$$
p^*\subsetneq q^*.
$$

Probemos ahora el recíproco. Supongamos

$$
p^*\subsetneq q^*.
$$

Entonces existe

$$
r\in q^*\setminus p^*.
$$

De $r\in q^*$ obtenemos

$$
r<q.
$$

De $r\notin p^*$ sabemos que no ocurre $r<p$. Como el orden de $\mathbb Q$ es lineal,

$$
p\le r.
$$

Por tanto

$$
p\le r<q,
$$

y de aquí

$$
p<q.
$$

Queda demostrado

$$
\boxed{
p<q
\quad\Longleftrightarrow\quad
p^*\subsetneq q^*.
}
$$

Para el orden no estricto, si $p\le q$, entonces o bien $p=q$, en cuyo caso $p^*=q^*$, o bien $p<q$, en cuyo caso $p^*\subsetneq q^*$. En ambos casos,

$$
p^*\subseteq q^*.
$$

Recíprocamente, si $p^*\subseteq q^*$ y fuera $q<p$, la equivalencia estricta ya demostrada produciría

$$
q^*\subsetneq p^*,
$$

incompatible con $p^*\subseteq q^*$. Luego $p\le q$. Por tanto,

$$
\boxed
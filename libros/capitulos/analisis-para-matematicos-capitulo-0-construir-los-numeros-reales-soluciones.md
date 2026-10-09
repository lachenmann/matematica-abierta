---
title: "Soluciones — Capítulo 0"
content-id: MA-BCH-0177
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-000-SOLUCIONES
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: 2026-10-07
date-modified: 2026-10-07
areas: [analisis]
level: universitario
topics: [analisis-real, numeros-reales, completitud]
prerequisites: []
related: [MA-BOK-0010]
provenance:
  type: original
  sources:
    - "ANM-C00_SOLUCIONES.md, fuente canónica ANM; paquete C00 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)

## §0.1. ¿Existen los números reales?

[]{#MA-SOL-ANM-01-000-001}

[]{#MA-EX-ANM-01-000-001}

### 1. Auditar una especificación antes de usarla

La primera expresión,

$$
A\le u,
$$

mezcla dos tipos de objeto. $A$ es un conjunto y $u$ es un elemento de $F$; la relación $\le$ del cuerpo compara elementos de $F$, no directamente un subconjunto con un elemento.

La reparación correcta es escribir

$$
\forall a\in A,\qquad a\le u.
$$

Eso expresa que $u$ es una cota superior de $A$.

La segunda expresión afirma que

$$
\forall x\in F\;\exists y\in F:\ xy=1.
$$

El problema está en $x=0$. Si $F$ es un cuerpo, $0$ no tiene inverso multiplicativo. La cuantificación correcta es

$$
\forall x\in F,\qquad
x\ne0\Longrightarrow
\exists y\in F:\ xy=1.
$$

Equivalentemente,

$$
\forall x\in F\setminus\{0\}\;\exists y\in F:\ xy=1.
$$

Ésta es una condición algebraica propia de un cuerpo.

La tercera expresión sí captura la propiedad del supremo. Sus hipótesis dicen que $A$ es no vacío y está acotado superiormente. La conclusión exige un elemento $s\in F$ que cumple simultáneamente

$$
\forall a\in A,\qquad a\le s,
$$

y

$$
\forall v\in F,\qquad
\left(
\forall a\in A,\ a\le v
\right)
\Longrightarrow
s\le v.
$$

La primera condición dice que $s$ es cota superior; la segunda, que es menor o igual que cualquier otra cota superior. Eso es exactamente decir que $s=\sup A$.

La cuarta expresión,

$$
\sup A\in A,
$$

está bien formada una vez que se ha establecido que $\sup A$ existe, pero **no forma parte de la definición de supremo**. La propiedad del supremo exige que $\sup A$ pertenezca al sistema $F$, no que pertenezca al subconjunto $A$.

Por tanto:

- 1: mal tipada; debe cuantificarse sobre los elementos de $A$;
- 2: mal cuantificada; debe excluirse $x=0$;
- 3: formulación correcta de la exigencia de completitud;
- 4: bien formada cuando el supremo existe, pero añade una condición que la especificación no exige.

Antes de preguntar si una estructura existe, la especificación debe estar escrita con dominios, cuantificadores y tipos correctos.

[]{#MA-SOL-ANM-01-000-002}

[]{#MA-EX-ANM-01-000-002}

### 2. Una existencia demostrada suponiendo que ya existe

El argumento no demuestra existencia porque introduce desde el comienzo el objeto cuya existencia debía justificar:

> «Sea $F$ un cuerpo ordenado completo».

Esa frase es legítima en un razonamiento **condicional** acerca de una estructura que suponemos dada. No es legítima como paso que permita concluir que tal estructura existe.

Después de introducir la hipótesis, el estudiante sólo desarrolla lo que ya está contenido en ella. De

$$
F\text{ es un cuerpo ordenado completo}
$$

puede deducirse correctamente que $F$ satisface los axiomas de cuerpo, posee un orden lineal compatible con las operaciones y tiene la propiedad del supremo.

Pero eso sólo establece una afirmación de la forma

$$
\boxed{
\text{si existe un }F\text{ con esa estructura, entonces }F\text{ cumple esas propiedades}.
}
$$

No permite eliminar el «si».

El salto inválido aparece cuando se pretende pasar de la hipótesis

$$
F\text{ es un cuerpo ordenado completo}
$$

a la conclusión existencial

$$
\exists F\;
\bigl(F\text{ es un cuerpo ordenado completo}\bigr).
$$

La hipótesis ya presupone un testigo de esa existencia; usarla para producir el mismo testigo es circular.

Para una prueba auténtica haría falta:

1. definir un objeto matemático concreto $M$ sin asumir previamente que sea un cuerpo ordenado completo;
2. definir sobre $M$ las operaciones y el orden pertinentes;
3. demostrar los axiomas de cuerpo;
4. demostrar que el orden es lineal y compatible con las operaciones;
5. demostrar la propiedad del supremo.

Sólo entonces $M$ sería un testigo de la afirmación existencial.

Una especificación dice qué tendría que cumplir un modelo; una prueba de existencia debe producir al menos un modelo y verificarlo.

[]{#MA-SOL-ANM-01-000-003}

[]{#MA-EX-ANM-01-000-003}

### 3. Qué tendría que certificar un modelo

La etapa I garantiza que tenemos un objeto concreto sobre el que podemos trabajar. Eso es indispensable, pero no basta. Un conjunto equipado con operaciones cualesquiera puede fallar las leyes algebraicas, el orden o la completitud.

Por eso

$$
\text{CONSTRUCCIÓN}
\not\Longrightarrow
\text{CUERPO ORDENADO COMPLETO}.
$$

La etapa II añade la estructura algebraica: sabemos que $M$ es un cuerpo. La etapa III añade un orden lineal compatible con esa aritmética. Después de I–III podemos concluir que $M$ es un **cuerpo ordenado**.

Todavía falta la exigencia decisiva de §0.1. Ser cuerpo ordenado no garantiza, por sí solo, que todo subconjunto no vacío y acotado superiormente tenga una menor cota superior dentro del mismo sistema. Por tanto,

$$
\text{I}+\text{II}+\text{III}
\not\Longrightarrow
\text{completitud}.
$$

La etapa IV cierra exactamente esa brecha. Una vez verificadas I–IV, $M$ es un cuerpo, está linealmente ordenado de manera compatible y posee la propiedad del supremo. Por la especificación de §0.1,

$$
M\text{ es un cuerpo ordenado completo}.
$$

Como $M$ fue construido concretamente, ya disponemos de un testigo para

$$
\exists F\;
\bigl(F\text{ es un cuerpo ordenado completo}\bigr).
$$

Así se cierra una prueba de existencia:

$$
\boxed{
\text{construir un candidato}
\longrightarrow
\text{verificar toda la especificación}
\longrightarrow
\text{obtener un testigo de existencia}.
}
$$

Si otra construcción produjera después un objeto $N$ que también superara I–IV, la existencia no volvería a estar en cuestión. La nueva pregunta sería de **comparación estructural**: habría que decidir en qué sentido $M$ y $N$ representan la misma estructura o podrían diferir esencialmente.

Las tareas quedan separadas:

- **construir** proporciona un candidato concreto;
- **verificar** demuestra que pertenece a la clase especificada;
- **comparar estructuras** pregunta cómo se relacionan dos candidatos ya verificados.

La comparación sólo tiene sentido una vez que la existencia ha sido resuelta.

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

Consideremos

$$
f(n)=2n.
$$

Es inyectiva, porque si

$$
f(m)=f(n),
$$

entonces

$$
2m=2n,
$$

y por tanto $m=n$.

También preserva y refleja el orden:

$$
m<n
\iff
2m<2n.
$$

La suma sí se conserva:

$$
f(m+n)
=
2(m+n)
=
2m+2n
=
f(m)+f(n).
$$

Hasta aquí, la aplicación transporta fielmente la estructura aditiva ordenada.

Pero falla al intentar preservar la estructura de anillo usada en §0.2. En primer lugar,

$$
f(1)=2\ne1.
$$

Además,

$$
f(mn)=2mn,
$$

mientras que

$$
f(m)f(n)
=
(2m)(2n)
=
4mn.
$$

En general,

$$
f(mn)\ne f(m)f(n).
$$

Por tanto, $f$ no preserva ni la unidad ni el producto. No es la incrustación de anillos ordenados que necesitamos para representar la aritmética entera dentro de $\mathbb Q$.

El diagnóstico preciso es:

$$
\boxed{
\text{inyectividad}
+
\text{orden}
+
\text{suma}
\not\Rightarrow
\text{incrustación de anillos ordenados}.
}
$$

La identificación de un sistema con su imagen sólo está justificada respecto de la estructura que la aplicación realmente conserva. Si identificáramos sin más el entero $n$ con el racional $2n$, la suma y el orden sobrevivirían, pero la multiplicación y la unidad dejarían de coincidir con las del sistema original.

Por eso la mera inyectividad no basta para autorizar la notación inclusiva en el sentido estructural requerido por §0.2: antes hay que comprobar exactamente qué operaciones, relaciones y elementos distinguidos se transportan sin alteración.

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

*Referencia visual.* Véase la figura C00-F03 del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F03 del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F03 del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-011}

[]{#MA-EX-ANM-01-000-011}

### 11. Una prueba que introduce demasiado pronto la frontera

El primer paso ilegítimo es la frase

> «En $\mathbb R$ existe $\sqrt2$».

En el punto actual del capítulo todavía estamos intentando justificar la existencia de un cuerpo ordenado completo que pueda desempeñar el papel de los números reales. Introducir $\mathbb R$ como estructura ya disponible y, dentro de ella, el elemento $\sqrt2$, presupone precisamente una parte del resultado que la construcción posterior debe establecer.

Hay una segunda anticipación en la frase «podemos aproximarnos racionalmente a $\sqrt2$ tanto como queramos desde abajo». La densidad demostrada hasta aquí para $\mathbb Q$ tiene la forma

$$
p<q,
\quad p,q\in\mathbb Q
\Longrightarrow
\exists r\in\mathbb Q:
 p<r<q.
$$

Hablar de racionales entre un racional y $\sqrt2$ exige haber situado ya $\sqrt2$ en un sistema ordenado común con $\mathbb Q$. Ese marco todavía no está disponible como premisa de §0.3.

Si $\mathbb R$ ya estuviera construido y se hubiera demostrado que $\sqrt2$ existe en él, el argumento externo podría servir para identificar la frontera de $S_2$ en ese sistema. Pero ésa es una afirmación posterior. No puede usarse para justificar, desde dentro de $\mathbb Q$, por qué necesitamos construir una extensión completa.

La reparación consiste en no nombrar ninguna frontera externa. Se toma un candidato arbitrario

$$
s\in\mathbb Q
$$

para ser $\sup_{\mathbb Q}S_2$ y se estudian las únicas tres posibilidades para $s^2$:

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

- En el primer caso se construye racionalmente $u>s$ con $u\in S_2$.
- En el tercero se construye racionalmente una cota superior $t<s$.
- En el caso central se demuestra, mediante paridad y una fracción irreducible, que ningún racional puede satisfacer $s^2=2$.

Así se obtiene la contradicción sin usar $\mathbb R$, sin usar $\sqrt2$ como objeto ya existente y sin recurrir a una noción externa de aproximación.

El problema no es que la conclusión del estudiante sea falsa; el problema es que su ruta lógica gasta antes de tiempo el objeto cuya necesidad estamos intentando demostrar.

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

*Referencia visual.* Véase la figura C00-F03 del texto principal, **Densidad sin completitud**, como síntesis posterior de este argumento.

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

es no vacío y propio. Tampoco tiene máximo: los racionales del intervalo $(1,2)$ pueden aumentarse permaneciendo por debajo de $2$. Sin embargo, no está cerrado hacia abajo. Por ejemplo,

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

*Referencia visual.* Véase la figura C00-F04 del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F04 del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F04 del texto principal, **Una cortadura es un lado izquierdo racional**, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F05 del texto principal, **La copia racional q↦q***, como síntesis posterior de este argumento.

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

*Referencia visual.* Véase la figura C00-F05 del texto principal, **La copia racional q↦q***, como síntesis posterior de este argumento.

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
\boxed{
p\le q
\quad\Longleftrightarrow\quad
p^*\subseteq q^*.
}
$$

Finalmente, supongamos

$$
\iota_{\mathbb Q}(p)
=
\iota_{\mathbb Q}(q).
$$

Esto significa

$$
p^*=q^*.
$$

Si $p<q$, tendríamos $p^*\subsetneq q^*$; si $q<p$, tendríamos $q^*\subsetneq p^*$. Ambas posibilidades contradicen la igualdad. Por tricotomía,

$$
p=q.
$$

Así,

$$
\boxed{\iota_{\mathbb Q}\text{ es inyectiva}.}
$$

La equivalencia de órdenes contiene más que una simple preservación: el orden de los racionales puede reconstruirse mirando únicamente las inclusiones entre sus imágenes.

*Referencia visual.* Véase la figura C00-F05 del texto principal, **La copia racional q↦q***, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-020}

[]{#MA-EX-ANM-01-000-020}

### 20. Una certificación algebraica demasiado temprana

El informe mezcla un resultado ya probado con conclusiones que pertenecen a etapas posteriores.

Hasta §0.5 sabemos que:

1. para cada $q\in\mathbb Q$, la cortadura $q^*$ pertenece a $\mathcal D$;
2. la aplicación

$$
\iota_{\mathbb Q}(q)=q^*
$$

está bien definida;
3. es inyectiva;
4. preserva y refleja el orden:

$$
p<q
\iff
p^*\subsetneq q^*.
$$

Eso certifica una incrustación de conjuntos linealmente ordenados:

$$
\boxed{
\iota_{\mathbb Q}:
(\mathbb Q,<)
\hookrightarrow
(\mathcal D,<_{\mathcal D}).
}
$$

No certifica todavía una incrustación de cuerpos ordenados.

La razón es estructural. En este punto del capítulo aún no hemos definido operaciones

$$
+_{\mathcal D}:
\mathcal D\times\mathcal D\longrightarrow\mathcal D
$$

ni

$$
\cdot_{\mathcal D}:
\mathcal D\times\mathcal D\longrightarrow\mathcal D.
$$

Por tanto, escribir

$$
p^*+q^*
$$

o

$$
p^*q^*
$$

como operaciones ya disponibles en $\mathcal D$ adelanta definiciones que todavía no forman parte de la construcción.

Después de definir esas operaciones habría que demostrar, además, que la imagen racional es compatible con ellas. En particular, deberán verificarse identidades del tipo

$$
p^*+_{\mathcal D}q^*=(p+q)^*
$$

y

$$
p^*\cdot_{\mathcal D}q^*=(pq)^*,
$$

junto con la correspondencia de los elementos neutros y las demás propiedades necesarias para la estructura de cuerpo ordenado.

Así aparecen dos etapas distintas.

La primera, ya cerrada, es:

$$
\boxed{
\text{ETAPA ORDINAL:}
\quad
\text{inyectividad}
+
\text{orden preservado y reflejado}.
}
$$

La segunda permanece pendiente:

$$
\boxed{
\text{ETAPA ALGEBRAICA:}
\quad
\text{operaciones definidas}
+
\text{aritmética racional preservada}.
}
$$

Sólo después de completar la segunda etapa estará justificado afirmar que la copia racional está incrustada como **cuerpo ordenado**.

Por eso tampoco conviene usar todavía la abreviatura no cualificada

$$
\mathbb Q\subseteq\mathcal D
$$

si se pretende que esa notación arrastre toda la estructura algebraica de $\mathbb Q$. Lo demostrado por ahora es, con precisión,

$$
\mathcal Q^*
=
\iota_{\mathbb Q}(\mathbb Q)
\subseteq\mathcal D
$$

y

$$
\mathbb Q
\cong
\mathcal Q^*
$$

como órdenes lineales.

El defecto del informe no consiste en que las identidades algebraicas futuras sean falsas. Consiste en tratarlas como disponibles antes de haber definido y certificado las operaciones que aparecen en ellas.

[]{#MA-SOL-ANM-01-000-021}

[]{#MA-EX-ANM-01-000-021}

### 21. La copia racional como orden, no todavía como cuerpo

Sea

$$
\mathcal Q^*=\{q^*:q\in\mathbb Q\}.
$$

Queremos definir

$$
\rho:\mathcal Q^*\longrightarrow\mathbb Q,
\qquad
\rho(q^*)=q.
$$

La primera obligación es probar que esta regla está bien definida. Un mismo elemento de $\mathcal Q^*$ podría, en principio, presentarse como $p^*$ y como $q^*$. Pero si

$$
p^*=q^*,
$$

la inyectividad de $\iota_{\mathbb Q}$ demostrada en el ejercicio 19 implica

$$
p=q.
$$

Por tanto la regla asigna un único racional a cada elemento de $\mathcal Q^*$.

Ahora sea $q\in\mathbb Q$. Entonces

$$
(\rho\circ\iota_{\mathbb Q})(q)
=
\rho(q^*)
=
q.
$$

Por consiguiente,

$$
\boxed{
\rho\circ\iota_{\mathbb Q}
=
\operatorname{id}_{\mathbb Q}.
}
$$

En sentido contrario, sea $A\in\mathcal Q^*$. Por definición de la imagen existe un $q\in\mathbb Q$ tal que

$$
A=q^*.
$$

Entonces

$$
(\iota_{\mathbb Q}\circ\rho)(A)
=
\iota_{\mathbb Q}(\rho(q^*))
=
\iota_{\mathbb Q}(q)
=
q^*
=
A.
$$

Luego

$$
\boxed{
\iota_{\mathbb Q}\circ\rho
=
\operatorname{id}_{\mathcal Q^*}.
}
$$

Así $\iota_{\mathbb Q}$, considerada como aplicación

$$
\mathbb Q\longrightarrow\mathcal Q^*,
$$

es biyectiva y $\rho$ es su inversa.

Para el orden, recordemos que

$$
A<_{\mathcal D}B
\iff
A\subsetneq B.
$$

El ejercicio 19 estableció

$$
p<q
\iff
p^*\subsetneq q^*.
$$

Por tanto,

$$
\boxed{
p<q
\quad\Longleftrightarrow\quad
p^*<_{\mathcal D}q^*.
}
$$

La biyección preserva y refleja el orden. En consecuencia,

$$
\boxed{
(\mathbb Q,<)
\cong
(\mathcal Q^*,<_{\mathcal D})
}
$$

como órdenes lineales.

Podemos incluso transportar la densidad racional sin introducir ninguna operación nueva en $\mathcal D$. Supongamos

$$
p^*<_{\mathcal D}q^*.
$$

Entonces $p<q$. En $\mathbb Q$ tomamos, por ejemplo,

$$
r=\frac{p+q}{2}.
$$

Se cumple

$$
p<r<q.
$$

Al aplicar la equivalencia de orden dos veces obtenemos

$$
p^*\subsetneq r^*\subsetneq q^*,
$$

es decir,

$$
\boxed{
p^*<_{\mathcal D}r^*<_{\mathcal D}q^*.
}
$$

Además $r^*\in\mathcal Q^*$ por construcción.

Por tanto $\mathcal Q^*$ reproduce exactamente el orden racional, incluida su densidad interna. Éste es el sentido preciso en que $\mathcal D$ contiene una **copia ordenada** de $\mathbb Q$.

Lo que todavía no hemos certificado es la estructura de cuerpo. No hay aún, en el desarrollo del capítulo, suma y producto definidos sobre todas las cortaduras y verificados contra la aritmética racional. Así, el cierre correcto de §0.5 es

$$
\boxed{
\text{ORDER ISOMORPHISM = VERIFIED}
\qquad
\text{ORDERED-FIELD EMBEDDING = PENDING}.
}
$$

## §0.6. Dar aritmética a las cortaduras I: suma y opuesto

[]{#MA-SOL-ANM-01-000-022}

[]{#MA-EX-ANM-01-000-022}

### 22. Construir una suma que permanezca dentro de $\mathcal D$

Sean $A,B\in\mathcal D$ y definamos

$$
A+B=\{a+b:a\in A,\ b\in B\}.
$$

Debemos demostrar que $A+B$ vuelve a ser una cortadura.

**No vaciedad.** Como $A$ y $B$ son no vacíos, existen

$$
a_0\in A,
\qquad
b_0\in B.
$$

Entonces

$$
a_0+b_0\in A+B,
$$

de modo que $A+B\ne\varnothing$.

**Propiedad de ser propio.** Como $A\subsetneq\mathbb Q$ y $B\subsetneq\mathbb Q$, podemos elegir

$$
u\notin A,
\qquad
v\notin B.
$$

Afirmamos que todo $a\in A$ satisface $a<u$. Si ocurriera $u\le a$, entonces, como $a\in A$ y $A$ es cerrado hacia abajo, tendríamos $u\in A$, contradicción. Por tanto

$$
a<u
$$

para todo $a\in A$. Del mismo modo,

$$
b<v
$$

para todo $b\in B$.

Así, para cualesquiera $a\in A$ y $b\in B$,

$$
a+b<u+v.
$$

En consecuencia,

$$
u+v\notin A+B.
$$

Luego $A+B\ne\mathbb Q$.

**Clausura hacia abajo.** Sea

$$
x=a+b\in A+B
$$

y sea $y<x$. Definamos

$$
a'=y-b.
$$

Como $y<a+b$,

$$
a'<a.
$$

La clausura hacia abajo de $A$ da $a'\in A$, y entonces

$$
y=a'+b\in A+B.
$$

**Ausencia de máximo.** Sea

$$
x=a+b\in A+B.
$$

Como $A$ no tiene máximo, existe $a'\in A$ con $a<a'$. Por tanto

$$
x=a+b<a'+b,
$$

y $a'+b\in A+B$. Ningún elemento de $A+B$ es máximo.

Las cuatro condiciones se cumplen. Por tanto

$$
\boxed{A+B\in\mathcal D.}
$$

Así la regla define realmente

$$
+:\mathcal D\times\mathcal D\longrightarrow\mathcal D.
$$

La última observación es lógica: una fórmula puede producir un subconjunto de $\mathbb Q$ sin producir una cortadura. Para definir una operación interna en $\mathcal D$ hacía falta demostrar la clausura del codominio.

*Referencia visual.* Véase la figura C00-F06 del texto principal, **Aritmética I: suma, opuesto y cancelación**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-023}

[]{#MA-EX-ANM-01-000-023}

### 23. Recuperar la suma racional y localizar el cero

Sean $p,q\in\mathbb Q$.

Primero probemos

$$
p^*+q^*\subseteq(p+q)^*.
$$

Si $x\in p^*+q^*$, existen $a<p$ y $b<q$ con $x=a+b$. Entonces

$$
x=a+b<p+q,
$$

de modo que $x\in(p+q)^*$.

Para la inclusión recíproca, sea $x<p+q$. Definimos

$$
\varepsilon=\frac{p+q-x}{2}>0
$$

y

$$
a=p-\varepsilon,
\qquad
b=q-\varepsilon.
$$

Entonces $a<p$ y $b<q$, por lo que

$$
a\in p^*,
\qquad
b\in q^*.
$$

Además,

$$
a+b=p+q-2\varepsilon=x.
$$

Así $x\in p^*+q^*$. Concluimos

$$
\boxed{p^*+q^*=(p+q)^*.}
$$

Como $\iota_{\mathbb Q}(r)=r^*$,

$$
\boxed{
\iota_{\mathbb Q}(p+q)
=
\iota_{\mathbb Q}(p)+\iota_{\mathbb Q}(q).
}
$$

Ahora probemos que $0^*$ es neutro aditivo. Si $x\in A+0^*$, existen $a\in A$ y $b<0$ con

$$
x=a+b<a.
$$

La clausura hacia abajo de $A$ da $x\in A$. Por tanto

$$
A+0^*\subseteq A.
$$

Recíprocamente, sea $x\in A$. Como $A$ no tiene máximo, existe $a\in A$ con $x<a$. Definimos

$$
b=x-a<0.
$$

Entonces $b\in0^*$ y

$$
x=a+b\in A+0^*.
$$

Así

$$
\boxed{A+0^*=A.}
$$

Por conmutatividad, también $0^*+A=A$.

La conmutatividad se obtiene directamente: si $x=a+b$ con $a\in A$ y $b\in B$, entonces

$$
x=b+a\in B+A.
$$

Intercambiando $A$ y $B$ se obtiene la igualdad

$$
\boxed{A+B=B+A.}
$$

Para la asociatividad, $x\in(A+B)+C$ si y sólo si existen $a\in A$, $b\in B$, $c\in C$ tales que

$$
x=(a+b)+c.
$$

Por asociatividad en $\mathbb Q$,

$$
(a+b)+c=a+(b+c),
$$

y esta última forma caracteriza la pertenencia a $A+(B+C)$. Por extensionalidad,

$$
\boxed{(A+B)+C=A+(B+C).}
$$

Al finalizar este ejercicio ya sabemos que la suma de cortaduras es interna, asociativa y conmutativa, que $0^*$ es su neutro y que la copia racional conserva la suma. Falta todavía construir y verificar los inversos aditivos, y toda la estructura multiplicativa continúa fuera de alcance.

*Referencia visual.* Véase la figura C00-F06 del texto principal, **Aritmética I: suma, opuesto y cancelación**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-024}

[]{#MA-EX-ANM-01-000-024}

### 24. Construir el opuesto sin introducir un punto final

Consideremos primero

$$
N(A)=\{-s:s\notin A\}.
$$

Si $A=q^*$, entonces

$$
s\notin q^*
\quad\Longleftrightarrow\quad
s\ge q.
$$

Por tanto

$$
N(q^*)
=
\{-s:s\ge q\}
=
\{t\in\mathbb Q:t\le -q\}.
$$

Este conjunto tiene máximo, a saber $-q$. Luego no es una cortadura.

La reparación consiste en tomar la clausura inferior estricta:

$$
-A
=
\{x\in\mathbb Q:
\exists s\notin A\text{ tal que }x<-s\}.
$$

Verifiquemos las cuatro condiciones.

**No vaciedad.** Como $A$ es propio, existe $s\notin A$. Entonces

$$
-s-1<-s,
$$

de modo que $-s-1\in-A$.

**Propiedad de ser propio.** Como $A$ no es vacío, tomemos $a\in A$. Afirmamos que $-a\notin-A$. Si $-a\in-A$, existiría $s\notin A$ con

$$
-a<-s,
$$

equivalentemente $s<a$. La clausura hacia abajo de $A$ implicaría $s\in A$, contradicción.

**Clausura hacia abajo.** Si $x\in-A$, existe $s\notin A$ con $x<-s$. Si $y<x$, entonces

$$
y<x<-s,
$$

y el mismo $s$ demuestra que $y\in-A$.

**Ausencia de máximo.** Sea $x\in-A$. Existe $s\notin A$ con $x<-s$. El racional

$$
x'=\frac{x-s}{2}
=
\frac{x+(-s)}{2}
$$

satisface

$$
x<x'<-s.
$$

Así $x'\in-A$ y $x'>x$.

Por tanto

$$
\boxed{-A\in\mathcal D.}
$$

Finalmente, para $A=q^*$, si $x\in-(q^*)$, existe $s\notin q^*$ con $x<-s$. La condición $s\notin q^*$ equivale a $s\ge q$, luego

$$
-s\le -q
$$

y por tanto $x<-q$. Así $x\in(-q)^*$.

Recíprocamente, si $x<-q$, tomamos $s=q$. Como $q\notin q^*$ y $x<-q=-s$, obtenemos $x\in-(q^*)$.

Luego

$$
\boxed{-(q^*)=(-q)^*.}
$$

La desigualdad estricta es indispensable: excluye el punto extremo que haría aparecer un máximo. La definición conserva la convención esencial de toda cortadura: lado izquierdo sin punto final.

*Referencia visual.* Véase la figura C00-F06 del texto principal, **Aritmética I: suma, opuesto y cancelación**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-025}

[]{#MA-EX-ANM-01-000-025}

### 25. Trazar la prueba de que el opuesto es un inverso aditivo

Comenzamos con el lema.

Sea $h\in\mathbb Q$, $h>0$. Elegimos

$$
a_0\in A
\qquad\text{y}\qquad
u\notin A.
$$

Como $a_0\in A$ y $u\notin A$, necesariamente $a_0<u$.

La propiedad arquimediana de $\mathbb Q$ se usa exactamente ahora: existe $n\in\mathbb N$ tal que

$$
nh>u-a_0.
$$

Por tanto

$$
a_0+nh>u.
$$

Ese racional no puede pertenecer a $A$, porque si perteneciera, la clausura hacia abajo y $u<a_0+nh$ obligarían a $u\in A$.

En la lista finita

$$
a_0,\ a_0+h,\ a_0+2h,\ldots,a_0+nh
$$

el primer término pertenece a $A$ y el último no. Sea $k\ge1$ el primer índice con

$$
a_0+kh\notin A.
$$

Entonces, por minimalidad,

$$
a:=a_0+(k-1)h\in A,
$$

mientras que

$$
a+h\notin A.
$$

Queda demostrado el lema.

Ahora probemos

$$
A+(-A)=0^*.
$$

Sea $x\in A+(-A)$. Existen $a\in A$ y $b\in-A$ con $x=a+b$. Por definición de $-A$, existe $s\notin A$ tal que

$$
b<-s.
$$

Como $a\in A$ y $s\notin A$, tenemos $a<s$. Luego

$$
x=a+b<a-s<0.
$$

Por tanto $x\in0^*$, y así

$$
A+(-A)\subseteq0^*.
$$

Para la otra inclusión, sea $x\in0^*$, es decir, $x<0$. Definimos

$$
h=-\frac{x}{2}>0.
$$

Esta elección hace que

$$
x=-2h,
$$

lo que permitirá fabricar un sumando que quede estrictamente por debajo del negativo de un racional exterior.

Por el lema existe $a\in A$ tal que

$$
a+h\notin A.
$$

Sea

$$
s=a+h
$$

y definamos

$$
b=x-a.
$$

Como $x=-2h$,

$$
b=-2h-a<-h-a=-s.
$$

Dado que $s\notin A$, la desigualdad $b<-s$ implica $b\in-A$. Finalmente,

$$
x=a+b
$$

con $a\in A$ y $b\in-A$, por lo que $x\in A+(-A)$.

Así,

$$
0^*\subseteq A+(-A),
$$

y por tanto

$$
\boxed{A+(-A)=0^*.}
$$

Pasemos a la traslación del orden.

Si $A\subseteq B$, cualquier elemento de $A+C$ tiene forma $a+c$ con $a\in A\subseteq B$ y $c\in C$. Por tanto

$$
A+C\subseteq B+C.
$$

Recíprocamente, supongamos

$$
A+C\subseteq B+C.
$$

La monotonía recién demostrada permite sumar $-C$ a ambos lados:

$$
(A+C)+(-C)
\subseteq
(B+C)+(-C).
$$

Por asociatividad y por $C+(-C)=0^*$,

$$
A+0^*\subseteq B+0^*.
$$

Luego

$$
A\subseteq B.
$$

Así,

$$
\boxed{
A\subseteq B
\quad\Longleftrightarrow\quad
A+C\subseteq B+C.
}
$$

Como la traslación tiene inversa —sumar $-C$— también conserva y refleja desigualdad estricta:

$$
\boxed{
A\subsetneq B
\quad\Longleftrightarrow\quad
A+C\subsetneq B+C.
}
$$

El balance de dependencias es:

- **clausura hacia abajo:** permite comparar elementos interiores con racionales exteriores y justificar pasos del lema;
- **existencia de racionales exteriores:** se usa para elegir $u\notin A$ y para la definición del opuesto;
- **arquimedianidad de $\mathbb Q$:** se usa exactamente para elegir $n$ con $nh>u-a_0$;
- **existencia del opuesto ya verificado:** se usa para invertir una traslación y recuperar $A\subseteq B$ desde $A+C\subseteq B+C$.

La prueba no usa producto ni ninguna propiedad de completitud.

*Nota visual.* El barrido racional por pasos de tamaño $h$ queda diferido a la versión Manim/web; la figura C00-F06 ofrece únicamente el contexto estático del lema de cruce.

[]{#MA-SOL-ANM-01-000-026}

[]{#MA-EX-ANM-01-000-026}

### 26. Auditar un cierre aditivo demasiado rápido

La primera inferencia inválida aparece inmediatamente después de escribir las fórmulas. De que

$$
A+B\subseteq\mathbb Q
$$

o de que un conjunto esté formado por racionales no se sigue que sea una cortadura. Para pertenecer a $\mathcal D$ deben verificarse no vaciedad, propiedad de ser propio, clausura hacia abajo y ausencia de máximo.

El segundo error está en la fórmula

$$
-A=\{-a:a\in A\}.
$$

Tomemos, por ejemplo,

$$
A=0^*=\{a\in\mathbb Q:a<0\}.
$$

Entonces

$$
\{-a:a\in0^*\}
=
\{r\in\mathbb Q:r>0\}.
$$

Este conjunto no es cerrado hacia abajo: $1$ pertenece a él, pero $-1<1$ y $-1$ no pertenece. Por tanto no es una cortadura.

Incluso la variante

$$
\{-s:s\notin A\}
$$

falla en general: para $A=q^*$ produce $\{t:t\le -q\}$, que tiene máximo.

La definición correcta es

$$
-A
=
\{x\in\mathbb Q:
\exists s\notin A\text{ tal que }x<-s\},
$$

y antes de usarla algebraicamente hay que demostrar que $-A\in\mathcal D$.

Tampoco basta la intuición para afirmar

$$
A+(-A)=0^*.
$$

Antes deben estar disponibles:

1. la clausura de la suma en $\mathcal D$;
2. la construcción correcta de $-A$ y su clausura;
3. el lema de aproximación racional;
4. las dos inclusiones
   $A+(-A)\subseteq0^*$ y $0^*\subseteq A+(-A)$.

La cancelación del último paso del informe también estaba adelantada. Para pasar de

$$
A+C\subseteq B+C
$$

a

$$
A\subseteq B
$$

necesitamos traducir por $-C$. Esa maniobra sólo es legítima después de haber probado que $-C$ existe como cortadura y que

$$
C+(-C)=0^*.
$$

La cadena lógica correcta es, por tanto,

$$
\boxed{
\begin{aligned}
&\text{definir suma}\\
&\Longrightarrow \text{probar clausura}\\
&\Longrightarrow \text{probar asociatividad y conmutatividad}\\
&\Longrightarrow \text{identificar }0^*\\
&\Longrightarrow \text{construir y cerrar }-A\\
&\Longrightarrow \text{probar }A+(-A)=0^*\\
&\Longrightarrow \text{obtener el grupo abeliano}\\
&\Longrightarrow \text{probar compatibilidad por traslaciones}.
\end{aligned}
}
$$

Sólo entonces está justificado concluir

$$
\boxed{
(\mathcal D,+,\le_{\mathcal D})
\text{ es un grupo abeliano linealmente ordenado}.
}
$$

El estado algebraico sigue siendo parcial: la multiplicación, la unidad multiplicativa y los inversos multiplicativos todavía no forman parte del sistema construido.

## §0.7. Dar aritmética a las cortaduras II: producto e inverso

[]{#MA-SOL-ANM-01-000-027}

[]{#MA-EX-ANM-01-000-027}

### 27. Construir el núcleo positivo del producto

La receta ingenua ya falla para la cortadura racional $1^*$.

Sea

$$
1^*=\{q\in\mathbb Q:q<1\}.
$$

Para cada entero positivo $N$ tenemos

$$
-N\in1^*.
$$

Por tanto

$$
N^2=(-N)(-N)\in P(1^*,1^*).
$$

Así $P(1^*,1^*)$ contiene racionales positivos arbitrariamente grandes. Una cortadura propia no puede tener esa propiedad: si $C\in\mathcal D$ y $u\notin C$, todo $c\in C$ satisface $c<u$. Por tanto $P(1^*,1^*)$ no puede ser una cortadura. El problema proviene de multiplicar racionales negativos muy alejados de la frontera.

Pasemos a la positividad. Supongamos primero

$$
0^*\subsetneq A.
$$

Existe entonces $x\in A\setminus0^*$. Así $x\ge0$. Si $x=0$, ya tenemos $0\in A$; si $x>0$, como $0<x$ y $A$ es cerrado hacia abajo, también $0\in A$.

Si $0\in A$, la ausencia de máximo produce $a\in A$ con

$$
0<a.
$$

Finalmente, si existe $a\in A$ con $a>0$, todo $q<0$ satisface $q<a$, y la clausura hacia abajo da $q\in A$. Por tanto

$$
0^*\subseteq A.
$$

La inclusión es estricta porque $a\in A\setminus0^*$. Hemos demostrado

$$
\boxed{
0^*<_{\mathcal D}A
\Longleftrightarrow
0\in A
\Longleftrightarrow
\exists a\in A\text{ con }a>0.
}
$$

Si $A,B>0^*$, los conjuntos $A_{>0}$ y $B_{>0}$ son no vacíos. Definimos

$$
A\cdot_+B
=
\{x\in\mathbb Q:\exists a\in A_{>0}\ \exists b\in B_{>0}\text{ con }x<ab\}.
$$

Elijamos $a\in A_{>0}$ y $b\in B_{>0}$. Como $ab>0$,

$$
0<ab,
$$

de modo que $0\in A\cdot_+B$. En particular, el conjunto es no vacío y ya contiene el cero racional.

Para la clausura hacia abajo, sea $x\in A\cdot_+B$. Existen $a,b>0$ con $a\in A$, $b\in B$ y

$$
x<ab.
$$

Si $y<x$, entonces

$$
y<x<ab,
$$

y los mismos testigos $a,b$ muestran que $y\in A\cdot_+B$.

Hasta aquí tenemos no vaciedad, presencia de $0$ y clausura inferior. Aún falta demostrar que el conjunto es propio y que carece de máximo; por eso todavía no declaramos clausura en $\mathcal D$.

*Referencia visual.* Véase la figura C00-F11 del texto principal, **Aritmética II: producto, inverso y signos**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-028}

[]{#MA-EX-ANM-01-000-028}

### 28. Cerrar el producto positivo y recuperar el producto racional

Sean $A,B>0^*$. Como $A$ y $B$ son cortaduras propias, existen racionales

$$
u\notin A,
\qquad
v\notin B.
$$

Además $0\in A$ y $0\in B$. Si $u\le0$, la clausura hacia abajo aplicada a $0\in A$ obligaría a $u\in A$ cuando $u<0$, y para $u=0$ ya sabemos que $0\in A$. Por tanto

$$
u>0.
$$

Análogamente, $v>0$.

Todo $a\in A$ satisface $a<u$, pues de $u\le a$ y $a\in A$ se seguiría $u\in A$. Del mismo modo, todo $b\in B$ cumple $b<v$. Para $a\in A_{>0}$ y $b\in B_{>0}$,

$$
ab<ub<uv.
$$

Así ningún par de testigos puede satisfacer $uv<ab$. Luego

$$
uv\notin A\cdot_+B,
$$

y $A\cdot_+B$ es propio.

Para la ausencia de máximo, sea $x\in A\cdot_+B$. Existen $a\in A_{>0}$ y $b\in B_{>0}$ con

$$
x<ab.
$$

Por densidad de $\mathbb Q$, existe $y\in\mathbb Q$ tal que

$$
x<y<ab.
$$

Los mismos $a,b$ prueban $y\in A\cdot_+B$. Por tanto ningún elemento es máximo.

Junto con el ejercicio 27, quedan verificadas las cuatro condiciones de cortadura, y además $0\in A\cdot_+B$. Por consiguiente,

$$
\boxed{
A\cdot_+B\in\mathcal D
\quad\text{y}\quad
A\cdot_+B>0^*.
}
$$

Ahora sean $p,q>0$ racionales.

Si $x\in p^*\cdot_+q^*$, existen $0<a<p$ y $0<b<q$ tales que

$$
x<ab.
$$

Como

$$
ab<pb<pq,
$$

tenemos $x<pq$, es decir,

$$
x\in(pq)^*.
$$

Así

$$
p^*\cdot_+q^*\subseteq(pq)^*.
$$

Para la inclusión inversa, sea $x<pq$.

Si $x\le0$, elegimos cualesquiera racionales $a,b$ con

$$
0<a<p,
\qquad
0<b<q.
$$

Entonces $x\le0<ab$, y por tanto $x\in p^*\cdot_+q^*$.

Supongamos ahora

$$
0<x<pq.
$$

Como $q>0$,

$$
\frac{x}{q}<p.
$$

Por densidad elegimos $a\in\mathbb Q$ con

$$
\frac{x}{q}<a<p.
$$

Entonces $a>0$ y $x<aq$, de modo que

$$
\frac xa<q.
$$

Una segunda aplicación de la densidad proporciona $b$ con

$$
\frac xa<b<q.
$$

Así $0<a<p$, $0<b<q$ y $x<ab$. Por tanto

$$
x\in p^*\cdot_+q^*.
$$

La doble inclusión da

$$
\boxed{p^*\cdot_+q^*=(pq)^*.}
$$

La densidad de $\mathbb Q$ se gasta exactamente en la ausencia de máximo del producto y, para la inclusión racional inversa, en la elección sucesiva de $a$ y $b$.

*Referencia visual.* Véase la figura C00-F11 del texto principal, **Aritmética II: producto, inverso y signos**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-029}

[]{#MA-EX-ANM-01-000-029}

### 29. Trazar el paso del producto positivo a todos los signos

En §0.6, el opuesto de una cortadura quedó caracterizado como su inverso aditivo. Como $A$ y $-(-A)$ son ambos inversos aditivos de $-A$, la unicidad del inverso da

$$
\boxed{-(-A)=A.}
$$

Si $A<0^*$, sumamos $-A$ a ambos lados. La compatibilidad del orden con traslaciones produce

$$
0^*<-A.
$$

Así una cortadura negativa se transforma en positiva al tomar su opuesto.

Definimos el producto general por

$$
A\cdot B=
\begin{cases}
0^*,&A=0^*\text{ o }B=0^*,\\[1ex]
A\cdot_+B,&A>0^*,\ B>0^*,\\[1ex]
(-A)\cdot_+(-B),&A<0^*,\ B<0^*,\\[1ex]
-\bigl(A\cdot_+(-B)\bigr),&A>0^*>B,\\[1ex]
-\bigl((-A)\cdot_+B\bigr),&B>0^*>A.
\end{cases}
$$

La tricotomía respecto de $0^*$ hace que los cinco casos sean exhaustivos y disjuntos. En las ramas con $\cdot_+$, los argumentos son positivos por construcción: los factores ya son positivos o han sido reemplazados por su opuesto. Como $\cdot_+$ produce una cortadura positiva y el opuesto de una cortadura vuelve a pertenecer a $\mathcal D$, el producto general es interno.

Probemos ahora la compatibilidad racional.

Si $p,q>0$, el resultado es el ejercicio 28:

$$
p^*\cdot q^*=(pq)^*.
$$

Si $p,q<0$, entonces $-p,-q>0$ y, usando $-(p^*)=(-p)^*$,

$$
\begin{aligned}
p^*\cdot q^*
&=(-p)^*\cdot_+(-q)^*\\
&=((-p)(-q))^*\\
&=(pq)^*.
\end{aligned}
$$

Si $p>0>q$,

$$
\begin{aligned}
p^*\cdot q^*
&=-\bigl(p^*\cdot_+(-q)^*\bigr)\\
&=-\bigl(p(-q)\bigr)^*\\
&=(pq)^*.
\end{aligned}
$$

El caso $q>0>p$ es simétrico. Si alguno de los racionales es cero, ambos lados son $0^*$. Luego

$$
\boxed{p^*\cdot q^*=(pq)^*\qquad(p,q\in\mathbb Q).}
$$

Veamos la unidad. Supongamos primero $A>0^*$.

Si $x\in A\cdot_+1^*$, existen $a\in A$, $a>0$, y $b$ con $0<b<1$ tales que

$$
x<ab<a.
$$

La clausura inferior de $A$ da $x\in A$. Así

$$
A\cdot_+1^*\subseteq A.
$$

Recíprocamente, sea $x\in A$. Si $x\le0$, elegimos $a\in A$ positivo y $b\in\mathbb Q$ con $0<b<1$; entonces $x<ab$.

Si $x>0$, la ausencia de máximo de $A$ proporciona $a\in A$ con $x<a$. Entonces

$$
0<\frac xa<1.
$$

Por densidad elegimos $b$ con

$$
\frac xa<b<1.
$$

Así $x<ab$ y $x\in A\cdot_+1^*$. Por tanto

$$
A\cdot_+1^*=A.
$$

La igualdad $1^*\cdot_+A=A$ se obtiene simétricamente.

Si $A=0^*$, la identidad es inmediata por definición. Si $A<0^*$, entonces $-A>0^*$ y

$$
A\cdot1^*
=-\bigl((-A)\cdot_+1^*\bigr)
=-(-A)
=A.
$$

Análogamente por la izquierda. Luego

$$
\boxed{A\cdot1^*=A=1^*\cdot A.}
$$

El mapa de dependencias es:

- **opuesto de §0.6:** permite convertir factores negativos en positivos y volver a colocar el signo;
- **producto racional positivo:** permite extender $p^*q^*=(pq)^*$ a todos los signos;
- **ausencia de máximo:** se usa para aproximar desde dentro un $x>0$ al demostrar que $1^*$ actúa como unidad.

*Referencia visual.* Véase la figura C00-F11 del texto principal, **Aritmética II: producto, inverso y signos**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-030}

[]{#MA-EX-ANM-01-000-030}

### 30. Construir y verificar el inverso multiplicativo

Sea $A>0^*$. Consideremos

$$
A^{-1,+}
=
\left\{
q\in\mathbb Q:
q\le0
\text{ o }
\exists s>0\;\bigl(s\notin A\text{ y }q<s^{-1}\bigr)
\right\}.
$$

Como $0\le0$,

$$
0\in A^{-1,+}.
$$

El conjunto es no vacío y, una vez cerrado como cortadura, será positivo.

Para demostrar que es propio, tomemos $a\in A$ con $a>0$. Afirmamos que

$$
a^{-1}\notin A^{-1,+}.
$$

No satisface la cláusula $q\le0$. Si satisficiera la segunda, existiría $s>0$, $s\notin A$, tal que

$$
a^{-1}<s^{-1}.
$$

Como ambos son positivos, invertir revierte el orden y tendríamos

$$
s<a.
$$

Pero $a\in A$ y $A$ es cerrado hacia abajo, luego $s\in A$, contradicción.

La clausura hacia abajo es directa. Si $q\le0$ y $r<q$, entonces $r\le0$. Si $q<s^{-1}$ para algún exterior positivo $s$ y $r<q$, el mismo $s$ muestra

$$
r<q<s^{-1}.
$$

Para la ausencia de máximo distinguimos tres casos. Si $q<0$, entonces $q<0$ y $0\in A^{-1,+}$. Si $q=0$, elegimos $s\notin A$; necesariamente $s>0$ porque $0\in A$ y todo racional no positivo pertenece a $A$. Por densidad existe

$$
0<r<s^{-1},
$$

y $r\in A^{-1,+}$. Si $q>0$, su pertenencia proporciona $s>0$, $s\notin A$, con $q<s^{-1}$; de nuevo por densidad elegimos

$$
q<r<s^{-1}.
$$

Por tanto $A^{-1,+}$ es una cortadura y, como contiene $0$,

$$
\boxed{A^{-1,+}>0^*.}
$$

Probemos ahora

$$
A\cdot_+A^{-1,+}=1^*.
$$

Sea $x\in A\cdot_+A^{-1,+}$. Existen $a\in A$, $a>0$, y $b\in A^{-1,+}$, $b>0$, con

$$
x<ab.
$$

Como $b>0$, su pertenencia proviene de un $s>0$, $s\notin A$, tal que

$$
b<s^{-1}.
$$

Todo elemento de $A$ está por debajo de todo exterior, así que $a<s$. Luego

$$
x<ab<a\,s^{-1}=\frac as<1.
$$

Por tanto

$$
A\cdot_+A^{-1,+}\subseteq1^*.
$$

Para la otra inclusión, sea $x<1$.

Si $x\le0$, elegimos $a\in A$ positivo y un $b\in A^{-1,+}$ positivo. Entonces $x<ab$, de modo que $x$ pertenece al producto.

Supongamos ahora

$$
0<x<1.
$$

Elegimos $c\in A$ con $c>0$. Como $(1-x)c>0$, tomamos un racional

$$
0<h<(1-x)c.
$$

Por el lema de aproximación racional de §0.6 existe $a\in A$ tal que

$$
s:=a+h\notin A.
$$

Como $c\in A$ y $s\notin A$, necesariamente $c<s=a+h$. Además $h<(1-x)c<c$, así que

$$
a>c-h>0.
$$

Tenemos

$$
(1-x)(c-h)-xh=(1-x)c-h>0.
$$

Como $a>c-h$,

$$
(1-x)a>xh.
$$

Equivalente a

$$
a>x(a+h)=xs.
$$

Por tanto

$$
\frac xa<\frac1s.
$$

Por densidad elegimos $b\in\mathbb Q$ con

$$
\frac xa<b<\frac1s.
$$

Entonces $b>0$, y como $s>0$, $s\notin A$ y $b<s^{-1}$,

$$
b\in A^{-1,+}.
$$

Además $x<ab$. Por tanto $x\in A\cdot_+A^{-1,+}$.

Hemos demostrado

$$
\boxed{A\cdot_+A^{-1,+}=1^*.}
$$

La igualdad con los factores intercambiados se obtiene de la simetría de la definición de $\cdot_+$, pues $ab=ba$ en $\mathbb Q$.

Para $A\ne0^*$ definimos

$$
A^{-1}
=
\begin{cases}
A^{-1,+},&A>0^*,\\[1ex]
-\bigl((-A)^{-1,+}\bigr),&A<0^*.
\end{cases}
$$

Si $A>0^*$, la ley del inverso ya está probada. Si $A<0^*$, ponemos

$$
B=-A>0^*.
$$

Entonces

$$
A^{-1}=-B^{-1,+},
$$

y, usando la rama de dos factores negativos,

$$
\begin{aligned}
A\cdot A^{-1}
&=(-A)\cdot_+(-A^{-1})\\
&=B\cdot_+B^{-1,+}\\
&=1^*.
\end{aligned}
$$

El mismo argumento en el orden inverso da

$$
\boxed{
A\cdot A^{-1}=1^*=A^{-1}\cdot A
\qquad(A\ne0^*).
}
$$

El lema de aproximación de §0.6 es el mecanismo que fabrica, para un $x<1$, un interior $a$ y un exterior $s$ suficientemente próximos como para abrir el intervalo racional

$$
\left(\frac xa,\frac1s\right).
$$

*Referencia visual.* Véase la figura C00-F11 del texto principal, **Aritmética II: producto, inverso y signos**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-031}

[]{#MA-EX-ANM-01-000-031}

### 31. Un producto correcto para positivos que no forma un cuerpo

La operación $\star$ es interna. En la rama positiva, $A\cdot_+B\in\mathcal D$ por el ejercicio 28. En las ramas con signo negativo, primero se aplica $\cdot_+$ a cortaduras positivas y luego se toma el opuesto, operación que ya sabemos que conserva $\mathcal D$. La rama con cero devuelve $0^*$.

Además, si $A,B>0^*$,

$$
A\star B=A\cdot_+B.
$$

Por tanto $\star$ coincide exactamente con el producto correcto en todo el sector positivo.

Tomemos ahora

$$
A=B=(-1)^*.
$$

Como $(-1)^*<0^*$ y

$$
-((-1)^*)=1^*,
$$

la rama deliberadamente alterada da

$$
\begin{aligned}
(-1)^*\star(-1)^*
&=-\bigl(1^*\cdot_+1^*\bigr)\\
&=-1^*\\
&=(-1)^*.
\end{aligned}
$$

Ya esto contradice el comportamiento racional que debería tener un producto de cuerpos, pues $(-1)(-1)=1$.

Veamos además el fallo directo de distributividad sugerido en la pista. Como la suma racional ya está preservada,

$$
(-1)^*+1^*=0^*.
$$

Por tanto

$$
(-1)^*\star\bigl((-1)^*+1^*\bigr)
=
(-1)^*\star0^*
=
0^*.
$$

En cambio,

$$
(-1)^*\star(-1)^*=(-1)^*.
$$

Para el producto de signos opuestos, la definición de $\star$ coincide con la regla correcta, de modo que

$$
(-1)^*\star1^*=(-1)^*.
$$

Así el miembro derecho de la distributividad sería

$$
(-1)^*+(-1)^*=(-2)^*.
$$

Como

$$
(-2)^*\ne0^*,
$$

obtenemos

$$
\boxed{
(-1)^*\star\bigl((-1)^*+1^*\bigr)
\ne
\bigl((-1)^*\star(-1)^*\bigr)
+
\bigl((-1)^*\star1^*\bigr).
}
$$

Por tanto $\star$ no es distributiva.

El contraejemplo aísla exactamente el punto lógico: conocer el producto en el cono positivo no determina por sí solo las reglas de signo ni garantiza que la extensión respete las leyes de anillo. Los casos negativos y mixtos deben definirse y verificarse explícitamente.

[]{#MA-SOL-ANM-01-000-032}

[]{#MA-EX-ANM-01-000-032}

### 32. Cerrar el cuerpo ordenado sin confundirlo con completitud

Empecemos por el núcleo positivo.

La conmutatividad de $\cdot_+$ es inmediata: para $A,B>0^*$,

$$
x<ab
\quad\Longleftrightarrow\quad
x<ba,
$$

de modo que

$$
\boxed{A\cdot_+B=B\cdot_+A.}
$$

Probemos la asociatividad positiva. Sea

$$
x\in(A\cdot_+B)\cdot_+C.
$$

Existen $u>0$ y $c\in C_{>0}$ tales que

$$
u\in A\cdot_+B,
\qquad
x<uc.
$$

A su vez existen $a\in A_{>0}$ y $b\in B_{>0}$ con

$$
u<ab.
$$

Por tanto

$$
x<uc<abc.
$$

Si $x\le0$, elegimos $v\in\mathbb Q$ con

$$
0<v<bc.
$$

Entonces $v\in B\cdot_+C$ y $x<0<av$, de modo que $x\in A\cdot_+(B\cdot_+C)$.

Si $x>0$, de $x<abc$ obtenemos

$$
\frac xa<bc.
$$

Por densidad elegimos

$$
\frac xa<v<bc.
$$

Entonces $v\in B\cdot_+C$ y $x<av$. Así

$$
(A\cdot_+B)\cdot_+C
\subseteq
A\cdot_+(B\cdot_+C).
$$

La inclusión inversa es simétrica: partiendo de $x<av<abc$, si $x\le0$ elegimos $0<u<ab$; si $x>0$, elegimos

$$
\frac xc<u<ab.
$$

Entonces $u\in A\cdot_+B$ y $x<uc$. Concluimos

$$
\boxed{(A\cdot_+B)\cdot_+C=A\cdot_+(B\cdot_+C).}
$$

Para extender conmutatividad y asociatividad a todos los signos, observemos que toda cortadura no nula puede escribirse como una parte positiva acompañada de un signo: si $A>0^*$ usamos $A$; si $A<0^*$ usamos $-A>0^*$. La definición del producto multiplica las partes positivas mediante $\cdot_+$ y coloca un opuesto exterior exactamente cuando aparece un número impar de factores negativos.

Por tanto, en cualquiera de las dos agrupaciones de tres factores no nulos, el signo final es el mismo y el núcleo positivo es el mismo por asociatividad de $\cdot_+$. Si aparece un cero, ambos lados son $0^*$. Así

$$
\boxed{A\cdot B=B\cdot A}
$$

y

$$
\boxed{(A\cdot B)\cdot C=A\cdot(B\cdot C)}
$$

para todos $A,B,C\in\mathcal D$.

Pasemos a la distributividad positiva. Sean $A,B,C>0^*$. Entonces $B+C>0^*$ porque $0\in B$ y $0\in C$, luego $0=0+0\in B+C$.

Sea

$$
x\in A\cdot_+(B+C).
$$

Existen $a\in A_{>0}$ y $u\in(B+C)_{>0}$ con

$$
x<au.
$$

Escribimos $u=b_0+c_0$ con $b_0\in B$, $c_0\in C$. Podemos obtener otra representación

$$
u=b+c
$$

con $b\in B_{>0}$ y $c\in C_{>0}$. Si ambos testigos originales son positivos, no hay nada que hacer. Si, por ejemplo, $b_0\le0$, entonces $c_0>0$. Elegimos $d\in B$ positivo y un racional

$$
0<b<\min\{u,d\}.
$$

Así $b\in B$, $b>b_0$ y, poniendo $c=u-b$, tenemos $c>0$ y

$$
c=u-b<u-b_0=c_0,
$$

por lo que $c\in C$. El otro caso es simétrico.

Ahora

$$
x<a(b+c)=ab+ac.
$$

Como

$$
x-ac<ab,
$$

por densidad elegimos $y$ con

$$
x-ac<y<ab.
$$

Sea $z=x-y$. Entonces

$$
y\in A\cdot_+B,
\qquad
z<ac,
$$

de modo que $z\in A\cdot_+C$ y $x=y+z$. Por tanto

$$
A\cdot_+(B+C)
\subseteq
(A\cdot_+B)+(A\cdot_+C).
$$

Para la inclusión inversa, sea

$$
x=y+z
$$

con $y\in A\cdot_+B$ y $z\in A\cdot_+C$. Elegimos

$$
a_1,a_2\in A_{>0},
\qquad
b\in B_{>0},
\qquad
c\in C_{>0}
$$

tales que

$$
y<a_1b,
\qquad
z<a_2c.
$$

Sea $m=\max\{a_1,a_2\}$. Como $m$ es uno de los dos elementos de $A$ y $A$ no tiene máximo, existe $a\in A$ con $m<a$. Entonces

$$
\begin{aligned}
x
&=y+z\\
&<a_1b+a_2c\\
&<ab+ac\\
&=a(b+c).
\end{aligned}
$$

Como $b+c>0$ y $b+c\in B+C$,

$$
x\in A\cdot_+(B+C).
$$

Concluimos

$$
\boxed{
A\cdot_+(B+C)
=(A\cdot_+B)+(A\cdot_+C)
}
$$

para cortaduras positivas.

La definición por signos implica

$$
(-A)B=-(AB),
\qquad
A(-B)=-(AB),
\qquad
(-A)(-B)=AB.
$$

Fijemos primero $A>0^*$ y permitamos signos arbitrarios para $B,C$.

Si $B,C>0^*$, ya tenemos distributividad. Si ambos son negativos, escribimos

$$
B=-B_0,
\qquad
C=-C_0,
$$

con $B_0,C_0>0^*$. Entonces

$$
B+C=-(B_0+C_0),
$$

y las reglas de signo reducen la igualdad al caso positivo.

Supongamos ahora

$$
B>0^*>C
$$

y pongamos $C_0=-C>0^*$. Por linealidad del orden, exactamente uno de los tres casos

$$
B=C_0,
\qquad
C_0<B,
\qquad
B<C_0
$$

ocurre.

Si $B=C_0$, entonces $B+C=0^*$ y ambos lados de la distributividad son $0^*$.

Si $C_0<B$, definimos

$$
D=B-C_0>0^*.
$$

Entonces $C_0+D=B$. La distributividad positiva da

$$
AB=AC_0+AD.
$$

Cancelando $AC_0$ en el grupo aditivo,

$$
AD=AB-AC_0=AB+AC.
$$

Como $D=B+C$,

$$
A(B+C)=AB+AC.
$$

Si $B<C_0$, ponemos

$$
D=C_0-B>0^*.
$$

Entonces $C_0=B+D$, y la distributividad positiva produce

$$
AC_0=AB+AD.
$$

Por cancelación,

$$
AB-AC_0=-AD.
$$

Pero $B+C=-D$ y $AC=-AC_0$, así que nuevamente

$$
A(B+C)=AB+AC.
$$

El caso $B<0^*<C$ es simétrico.

Por tanto la distributividad vale para $A>0^*$ y todos $B,C$. Si $A<0^*$, escribimos $A=-A_0$ con $A_0>0^*$ y usamos las reglas de signo:

$$
\begin{aligned}
A(B+C)
&=-A_0(B+C)\\
&=-(A_0B+A_0C)\\
&=AB+AC.
\end{aligned}
$$

Para $A=0^*$ es inmediata. Hemos probado

$$
\boxed{A(B+C)=AB+AC}
$$

para todos $A,B,C\in\mathcal D$. La distributividad por la derecha sigue de la conmutatividad del producto.

La compatibilidad multiplicativa del orden también queda cerrada. Si

$$
0^*\le A,
\qquad
0^*\le B,
$$

cada factor es cero o positivo. Si alguno es cero, $AB=0^*$. Si ambos son positivos, el ejercicio 28 mostró

$$
AB=A\cdot_+B>0^*.
$$

Luego

$$
\boxed{
0^*\le A,\ 0^*\le B
\Longrightarrow
0^*\le AB.
}
$$

Ya podemos reunir las verificaciones. De §0.6 tenemos un grupo abeliano aditivo y un orden lineal compatible con traslaciones. En §0.7 hemos establecido:

- cierre del producto;
- conmutatividad y asociatividad;
- unidad $1^*$ con $1^*\ne0^*$;
- inverso multiplicativo para todo $A\ne0^*$;
- distributividad;
- compatibilidad del orden con productos no negativos.

Por tanto

$$
\boxed{
(\mathcal D,+,\cdot,\le_{\mathcal D})
\text{ es un cuerpo ordenado}.
}
$$

La copia racional queda ahora certificada al nivel algebraico completo. Ya sabíamos que $q\mapsto q^*$ es inyectiva y preserva y refleja el orden. En §0.6 se probó

$$
(p+q)^*=p^*+q^*,
\qquad
0_{\mathcal D}=0^*,
$$

y ahora tenemos

$$
(pq)^*=p^*\cdot q^*,
\qquad
1_{\mathcal D}=1^*.
$$

Así

$$
\boxed{
\iota_{\mathbb Q}:\mathbb Q\hookrightarrow\mathcal D
\text{ es una incrustación de cuerpos ordenados}.
}
$$

Sin embargo, esto todavía no responde por completo la pregunta de existencia de §0.1. Allí se pidió un **cuerpo ordenado completo**. Hasta este punto sólo se ha demostrado que $\mathcal D$ es un cuerpo ordenado. Falta probar que toda familia no vacía de cortaduras acotada superiormente posee un supremo en $\mathcal D$.

Por eso el cierre correcto es

$$
\boxed{
\text{CUERPO ORDENADO = VERIFICADO}
\qquad
\text{COMPLETITUD = PENDIENTE}.
}
$$

No es legítimo convertir el primer certificado en el segundo sin una prueba adicional.

## §0.8. Sí existen: el supremo como unión

*Referencia visual.* Véase la figura C00-F11 del texto principal, **Aritmética II: producto, inverso y signos**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-033}

[]{#MA-EX-ANM-01-000-033}

### 33. Demostrar que la unión vuelve a ser una cortadura

Sea

$$
S=\bigcup_{A\in\mathscr A}A.
$$

Debemos verificar las cuatro condiciones de una cortadura.

**No vaciedad.** Como $\mathscr A\ne\varnothing$, existe $A_0\in\mathscr A$. Como $A_0\in\mathcal D$, tenemos $A_0\ne\varnothing$, de modo que existe $q\in A_0$. Entonces $q\in S$. Por tanto

$$
S\ne\varnothing.
$$

Aquí se usa exactamente la no vaciedad de la familia.

**Subconjunto propio.** Como $\mathscr A$ está acotada superiormente, existe $U\in\mathcal D$ tal que

$$
A\subseteq U
\qquad
\text{para todo }A\in\mathscr A.
$$

Si $q\in S$, existe $A\in\mathscr A$ con $q\in A$. Entonces $q\in U$. Por tanto

$$
S\subseteq U.
$$

Pero $U$ es una cortadura y, en particular,

$$
U\subsetneq\mathbb Q.
$$

Luego también

$$
S\subsetneq\mathbb Q.
$$

Éste es el único punto de las cuatro verificaciones donde necesitamos la hipótesis de acotación superior.

**Clausura hacia abajo.** Sea $q\in S$ y sea $r<q$. De $q\in S$ se sigue que existe $A\in\mathscr A$ con $q\in A$. Como $A$ es cerrada hacia abajo,

$$
r\in A.
$$

Entonces $r\in S$.

**Ausencia de máximo.** Sea $q\in S$. Elegimos nuevamente $A\in\mathscr A$ con $q\in A$. Como $A$ no tiene máximo, existe $r\in A$ tal que

$$
q<r.
$$

Como $A\subseteq S$, también $r\in S$. Así ningún elemento de $S$ es máximo.

Las cuatro condiciones quedan verificadas:

$$
\boxed{
S=\bigcup_{A\in\mathscr A}A\in\mathcal D.
}
$$

La trazabilidad de hipótesis es precisa:

- $\mathscr A\ne\varnothing$ se gasta para obtener un primer elemento de $S$;
- la acotación superior se gasta para impedir $S=\mathbb Q$;
- la clausura hacia abajo y la ausencia de máximo se heredan localmente del miembro de la familia que contiene al racional considerado.

Todavía no hemos demostrado que $S$ sea supremo: sólo que el candidato vive dentro del dominio ordenado correcto.

*Referencia visual.* Véase la figura C00-F07 del texto principal, **La unión que cierra la existencia**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-034}

[]{#MA-EX-ANM-01-000-034}

### 34. Separar «ser cortadura» de «ser supremo»

Partimos ahora del resultado ya establecido

$$
S=\bigcup_{A\in\mathscr A}A\in\mathcal D.
$$

Esto permite formular la pregunta de orden: ¿es $S$ la menor cota superior?

**Primera obligación: $S$ es cota superior.** Sea $A\in\mathscr A$. Por definición de unión,

$$
A\subseteq S.
$$

Como el orden de $\mathcal D$ es la inclusión,

$$
A\le_{\mathcal D}S.
$$

Esto vale para todo $A\in\mathscr A$. Por tanto $S$ es una cota superior de la familia.

**Segunda obligación: $S$ es menor que cualquier otra cota superior.** Sea $V\in\mathcal D$ una cota superior de $\mathscr A$. Entonces

$$
A\subseteq V
\qquad
\text{para todo }A\in\mathscr A.
$$

Tomemos $q\in S$. Por definición de unión existe $A\in\mathscr A$ tal que $q\in A$. Como $A\subseteq V$,

$$
q\in V.
$$

Por tanto

$$
S\subseteq V,
$$

es decir,

$$
S\le_{\mathcal D}V.
$$

Las dos obligaciones prueban

$$
\boxed{
S=\sup_{\mathcal D}\mathscr A.
}
$$

Sustituyendo la definición de $S$,

$$
\boxed{
\sup_{\mathcal D}\mathscr A
=
\bigcup_{A\in\mathscr A}A.
}
$$

Las dos pruebas no son intercambiables. Para que $S$ pueda ser un supremo **en $\mathcal D$**, primero debe estar demostrado que $S\in\mathcal D$. El argumento de menor cota superior compara conjuntos por inclusión, pero por sí solo no certifica que la unión sea una cortadura.

El inventario de hipótesis queda así:

- la no vaciedad y la acotación superior de $\mathscr A$ son necesarias en el ejercicio 33 para garantizar $S\in\mathcal D$;
- una vez que $S\in\mathcal D$, la condición $A\subseteq S$ proviene puramente de la definición de unión;
- para demostrar minimalidad se toma una cota superior arbitraria $V$ y se usa exactamente la condición $A\subseteq V$ para todo $A\in\mathscr A$.

La arquitectura lógica es, por tanto,

$$
\boxed{
S\in\mathcal D
\quad\Longrightarrow\quad
\text{podemos preguntar si }S=\sup_{\mathcal D}\mathscr A,
}
$$

no al revés.

*Referencia visual.* Véase la figura C00-F07 del texto principal, **La unión que cierra la existencia**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-035}

[]{#MA-EX-ANM-01-000-035}

### 35. Localizar exactamente por qué hace falta una cota superior

La familia

$$
\mathscr N=\{n^*:n\in\mathbb N\}
$$

es no vacía porque, por ejemplo, $0^*\in\mathscr N$.

Probemos ahora que su unión es todo $\mathbb Q$. Sea $q\in\mathbb Q$. Por la propiedad arquimediana de $\mathbb Q$, existe $n\in\mathbb N$ tal que

$$
q<n.
$$

Entonces, por definición de cortadura racional,

$$
q\in n^*.
$$

Como $n^*$ es uno de los miembros de $\mathscr N$,

$$
q\in\bigcup_{n\in\mathbb N}n^*.
$$

Así

$$
\mathbb Q
\subseteq
\bigcup_{n\in\mathbb N}n^*.
$$

La inclusión inversa es automática porque cada $n^*$ es un subconjunto de $\mathbb Q$. Por tanto

$$
\boxed{
\bigcup_{n\in\mathbb N}n^*=\mathbb Q.
}
$$

Pero $\mathbb Q$ no es una cortadura: falla la condición de ser un subconjunto propio de sí mismo. En consecuencia, la unión de una familia no vacía de cortaduras no tiene por qué pertenecer a $\mathcal D$.

Esto también demuestra que $\mathscr N$ no está acotada superiormente en $\mathcal D$. Si existiera $U\in\mathcal D$ con

$$
n^*\subseteq U
\qquad
\text{para todo }n\in\mathbb N,
$$

entonces, tomando uniones,

$$
\mathbb Q
=
\bigcup_{n\in\mathbb N}n^*
\subseteq U.
$$

Como siempre $U\subseteq\mathbb Q$, seguiría $U=\mathbb Q$, contradicción con $U\in\mathcal D$.

La falla se localiza exactamente en el segundo bloque de la prueba del ejercicio 33. Allí elegíamos una cota superior $U$ y obteníamos

$$
S\subseteq U\subsetneq\mathbb Q.
$$

Para $\mathscr N$ no existe tal $U$. Sin ese cerco, la unión crece hasta llenar todos los racionales.

Es instructivo observar que las otras propiedades no son el problema: $\mathbb Q$ es no vacío, está cerrado hacia abajo respecto de su propio orden y no tiene máximo. Falla exactamente la propiedad de ser un subconjunto propio de $\mathbb Q$.

Por tanto,

$$
\boxed{
\text{UNIÓN DE CORTADURAS}
\not\Longrightarrow
\text{CORTADURA}
}
$$

sin la hipótesis de acotación superior.

*Referencia visual.* Véase la figura C00-F07 del texto principal, **La unión que cierra la existencia**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-036}

[]{#MA-EX-ANM-01-000-036}

### 36. Cerrar la pregunta de existencia sin confundir modelo con esencia

El cierre exige combinar dos certificados lógicamente distintos.

De §§0.6–0.7 sabemos que

$$
\boxed{
(\mathcal D,+,\cdot,\le_{\mathcal D})
\text{ es un cuerpo ordenado}.
}
$$

De los ejercicios 33–34 sabemos que toda familia $\mathscr A\subseteq\mathcal D$ no vacía y acotada superiormente tiene un supremo en $\mathcal D$, concretamente

$$
\boxed{
\sup_{\mathcal D}\mathscr A
=
\bigcup_{A\in\mathscr A}A.
}
$$

Por definición, un cuerpo ordenado que satisface la propiedad del supremo es un cuerpo ordenado completo. Luego

$$
\boxed{
(\mathcal D,+,\cdot,\le_{\mathcal D})
\text{ es un cuerpo ordenado completo}.
}
$$

Esto resuelve la pregunta de existencia de §0.1. No hemos supuesto de antemano un sistema de reales: construimos $\mathcal D$ como una colección concreta de subconjuntos de $\mathbb Q$, definimos en ella las operaciones y el orden y verificamos toda la especificación. Así existe al menos un testigo de la afirmación

$$
\exists F\;
\bigl(F\text{ es un cuerpo ordenado completo}\bigr).
$$

Además, la aplicación

$$
\iota_{\mathbb Q}:\mathbb Q\longrightarrow\mathcal D,
\qquad
q\longmapsto q^*,
$$

ya fue certificada como incrustación de cuerpos ordenados. Es inyectiva, preserva y refleja el orden, y conserva suma, producto, $0$ y $1$. Por tanto $\mathcal D$ no sólo satisface la especificación abstracta: contiene una copia estructural fiel de $\mathbb Q$.

Éste es el sentido preciso de afirmar

$$
\boxed{\mathcal D\text{ es un modelo de los números reales}.}
$$

La palabra «modelo» expresa que la estructura concreta realiza todos los axiomas y propiedades exigidos. No afirma que todo número real deba ser ontológicamente, en cualquier presentación posible, un conjunto de racionales. Las cortaduras proporcionan una **realización concreta** de la estructura.

Consideremos ahora

$$
A_2=\{q\in\mathbb Q:q<0\text{ o }q^2<2\}.
$$

En §0.4 sólo podíamos afirmar que $A_2$ era una cortadura no racional. Ahora sabemos además que

$$
A_2\in\mathcal D
$$

y que $\mathcal D$ es un modelo de los reales. Por tanto $A_2$ es legítimamente un elemento de un sistema de números reales, y sigue fuera de la copia racional $\iota_{\mathbb Q}(\mathbb Q)$.

Lo que **no** se ha demostrado todavía es que cualquier otro cuerpo ordenado completo sea estructuralmente el mismo que $\mathcal D$. La existencia responde

$$
\text{«¿hay al menos un modelo?»}
$$

pero no responde aún

$$
\text{«¿son todos los modelos esencialmente el mismo?»}
$$

Esa segunda pregunta queda abierta para las secciones siguientes.

*Referencias visuales.* Véanse las figuras [C00-F01 (**Existencia antes que unicidad**)](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md#fig-anm-c00-f01) y C00-F07 (**La unión que cierra la existencia**) del texto principal para sintetizar, respectivamente, las capas de este cierre.

[]{#MA-SOL-ANM-01-000-037}

[]{#MA-EX-ANM-01-000-037}

### 37. Auditar un cierre de existencia que mezcla cuatro niveles

El informe contiene varias inferencias inválidas y conviene detenerse en la primera.

La primera es

> «$\mathcal D$ es un cuerpo ordenado; por tanto ya es completo».

Ser cuerpo ordenado no implica completitud. Ya tenemos dentro del propio capítulo un contraejemplo: $\mathbb Q$ es un cuerpo ordenado y, sin embargo, el conjunto

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

es no vacío, está acotado superiormente y no posee supremo racional. Por tanto

$$
\boxed{
\text{CUERPO ORDENADO}
\not\Longrightarrow
\text{COMPLETO}.
}
$$

La segunda afirmación defectuosa es

> «la unión de cualquier familia de cortaduras es una cortadura».

El ejercicio 35 da un contraejemplo explícito:

$$
\mathscr N=\{n^*:n\in\mathbb N\},
$$

para el cual

$$
\bigcup\mathscr N=\mathbb Q.
$$

Como $\mathbb Q\notin\mathcal D$, la unión no es una cortadura.

El teorema correcto exige ambas hipótesis:

$$
\boxed{
\mathscr A\subseteq\mathcal D,
\quad
\mathscr A\ne\varnothing,
\quad
\mathscr A\text{ acotada superiormente}
}
$$

implican

$$
\boxed{
\bigcup\mathscr A\in\mathcal D
\quad\text{y}\quad
\sup_{\mathcal D}\mathscr A=\bigcup\mathscr A.
}
$$

Con ese teorema sí queda demostrada la propiedad del supremo de $\mathcal D$. Combinada con el resultado de §0.7, podemos concluir correctamente que $\mathcal D$ es un cuerpo ordenado completo.

El siguiente salto del informe confunde **modelo** con **igualdad literal**. Decir

$$
\mathcal D\text{ es un modelo de los números reales}
$$

significa que la estructura construida satisface la especificación de cuerpo ordenado completo y contiene la copia racional pertinente. No significa que hayamos establecido que cualquier presentación legítima de los reales tenga exactamente los mismos elementos conjuntistas que $\mathcal D$.

La última frase añade todavía una afirmación de unicidad que §0.8 no ha demostrado. De la existencia de un modelo no se deduce que cualquier otro modelo sea literalmente igual, ni siquiera hemos demostrado todavía en esta sección qué relación estructural precisa debe unirlos.

La reparación completa del informe es:

$$
\boxed{
\begin{array}{c}
\mathcal D\text{ es un cuerpo ordenado}\\
+\\
\text{toda familia no vacía y acotada superiormente en }\mathcal D\\
\text{tiene supremo, dado por su unión}\\
\hline
\mathcal D\text{ es un cuerpo ordenado completo}.
\end{array}
}
$$

Además,

$$
\iota_{\mathbb Q}:\mathbb Q\hookrightarrow\mathcal D
$$

es una incrustación de cuerpos ordenados. Por tanto existe al menos un cuerpo ordenado completo que contiene una copia ordenada de $\mathbb Q$; en ese sentido,

$$
\boxed{\mathcal D\text{ es un modelo de los números reales}.}
$$

La pregunta de existencia queda cerrada. La pregunta de unicidad estructural queda abierta y no debe anticiparse con resultados de §§0.9–0.10.

## §0.9. ¿Podría haber otros reales?

[]{#MA-SOL-ANM-01-000-038}

[]{#MA-EX-ANM-01-000-038}

### 38. Separar universos y construir la copia racional canónica

Partimos sólo de que $F$ es un cuerpo ordenado. En particular,

$$
0_F<1_F.
$$

Definimos

$$
\nu_F(0)=0_F,\qquad \nu_F(n+1)=\nu_F(n)+1_F.
$$

Por inducción, $n>0$ implica $\nu_F(n)>0_F$. Si $m<n$, existe $k>0$ con $n=m+k$, y entonces

$$
\nu_F(n)=\nu_F(m)+\nu_F(k)>\nu_F(m).
$$

Por tanto los numerales preservan estrictamente el orden. En particular, ningún $n>0$ satisface $\nu_F(n)=0_F$, así que

$$
\boxed{\operatorname{char}F=0}.
$$

Los tipos son

$$
\nu_F:\mathbb N\longrightarrow F,
$$

$$
\jmath_{\mathbb Z}^F:\mathbb Z\longrightarrow F,
$$

y

$$
\iota_F:\mathbb Q\longrightarrow F.
$$

Para un entero presentado como $m-n$, definimos

$$
\jmath_{\mathbb Z}^F(m-n)=\nu_F(m)-\nu_F(n).
$$

Si $m-n=p-q$, entonces $m+q=n+p$. La aditividad de los numerales da

$$
\nu_F(m)+\nu_F(q)=\nu_F(n)+\nu_F(p),
$$

y, trasladando términos,

$$
\nu_F(m)-\nu_F(n)=\nu_F(p)-\nu_F(q).
$$

Así la definición no depende de la representación. La característica cero impide que enteros distintos colapsen, por lo que $\jmath_{\mathbb Z}^F$ es inyectiva.

Para $a/b\in\mathbb Q$, con $b\ne0$, definimos

$$
\iota_F\!\left(\frac ab\right)
=
\jmath_{\mathbb Z}^F(a)
\bigl(\jmath_{\mathbb Z}^F(b)\bigr)^{-1}.
$$

Como $b\ne0$ y $\jmath_{\mathbb Z}^F$ es inyectiva,

$$
\jmath_{\mathbb Z}^F(b)\ne0_F,
$$

de modo que el inverso existe. Si

$$
\frac ab=\frac cd,
$$

entonces $ad=bc$. Aplicando la multiplicatividad de la copia entera,

$$
\jmath_{\mathbb Z}^F(a)\jmath_{\mathbb Z}^F(d)
=
\jmath_{\mathbb Z}^F(b)\jmath_{\mathbb Z}^F(c).
$$

Multiplicando por los inversos de las imágenes de $b$ y $d$, obtenemos el mismo valor para ambas fracciones. Por tanto $\iota_F$ está bien definida. Las leyes de cuerpo muestran que conserva suma, producto, $0$ y $1$, y el orden se conserva y refleja. En consecuencia,

$$
\boxed{\iota_F:\mathbb Q\hookrightarrow F}
$$

es una incrustación de cuerpos ordenados.

Después de esta certificación podemos identificar notacionalmente $\mathbb Q$ con la imagen $\iota_F(\mathbb Q)$ cuando resulte cómodo. Eso no afirma una igualdad literal entre los conjuntos subyacentes: la afirmación estructural primaria es la existencia de la incrustación canónica.

Nada de esta construcción ha usado completitud. La copia canónica de $\mathbb Q$ existe en todo cuerpo ordenado.

*Referencia visual.* Véase la figura C00-F08 del texto principal, **De completitud a rejilla racional en F**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-039}

[]{#MA-EX-ANM-01-000-039}

### 39. La completitud obliga a la arquimedianidad

Supongamos, para obtener una contradicción, que

$$
N_F=\{\nu_F(n):n\in\mathbb N\}
$$

está acotado superiormente. Es no vacío porque $0_F=\nu_F(0)\in N_F$.

Aquí se gasta la completitud. Existe

$$
s=\sup_F N_F.
$$

Como $1_F>0_F$,

$$
s-1_F<s.
$$

El elemento $s-1_F$ no puede ser una cota superior de $N_F$: si lo fuera, sería una cota superior estrictamente menor que el supremo. Por tanto existe $n\in\mathbb N$ tal que

$$
s-1_F<\nu_F(n).
$$

Sumando $1_F$,

$$
s<\nu_F(n)+1_F=\nu_F(n+1).
$$

Pero $\nu_F(n+1)\in N_F$, contradicción con que $s$ sea cota superior. Luego $N_F$ no está acotado superiormente.

Así, ningún $x\in F$ puede ser cota superior de $N_F$. Por tanto para todo $x\in F$ existe $n\in\mathbb N$ con

$$
\boxed{x<\nu_F(n)}.
$$

Ésta es la forma arquimediana que usaremos.

La completitud intervino exactamente en la existencia de $s=\sup_F N_F$ bajo la hipótesis de acotación. El resto utiliza sólo orden y estructura aditiva. Por ello el resultado correcto es

$$
\boxed{\text{cuerpo ordenado completo}\Longrightarrow\text{arquimediano}},
$$

no la falsa inferencia «todo cuerpo ordenado es arquimediano».

*Referencia visual.* Véase la figura C00-F08 del texto principal, **De completitud a rejilla racional en F**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-040}

[]{#MA-EX-ANM-01-000-040}

### 40. Trazar el camino desde la arquimedianidad hasta la densidad racional

Primero localizamos cualquier elemento entre enteros consecutivos. Sea $x\in F$. Por arquimedianidad existen $n_1,n_2\in\mathbb N$ tales que

$$
x<\iota_F(n_1),
\qquad
-x<\iota_F(n_2).
$$

Tomamos, por ejemplo,

$$
n=n_1+n_2+1.
$$

Entonces $n>0$ y

$$
-\iota_F(n)<x<\iota_F(n).
$$

Definimos

$$
K=\{k\in\mathbb N:x<-\iota_F(n)+\iota_F(k)\}.
$$

El conjunto $K$ no es vacío. Para $k=2n+1$,

$$
-\iota_F(n)+\iota_F(2n+1)=\iota_F(n+1)>x.
$$

Por el buen orden de $\mathbb N$, $K$ tiene mínimo; llamémoslo $k_0$. No puede ser $0$, porque $-\iota_F(n)<x$. Escribimos

$$
k_0=k+1.
$$

La minimalidad implica $k\notin K$, de modo que

$$
-\iota_F(n)+\iota_F(k)\le x.
$$

Como $k+1\in K$,

$$
x<-\iota_F(n)+\iota_F(k+1).
$$

Definimos

$$
m=-n+(k+1)\in\mathbb Z.
$$

Entonces $m-1=-n+k$, y obtenemos

$$
\boxed{\iota_F(m-1)\le x<\iota_F(m)}.
$$

Ésta es la localización entera.

Sean ahora $x<y$. La diferencia $y-x$ es positiva. Aplicamos la arquimedianidad a $(y-x)^{-1}$. Existe $n\in\mathbb N$ tal que

$$
(y-x)^{-1}<\iota_F(n).
$$

Necesariamente $n>0$. Al invertir elementos positivos se invierte el orden, así que

$$
0<\iota_F(n)^{-1}<y-x.
$$

Como $\iota_F$ preserva inversos,

$$
\boxed{0<\iota_F\!\left(\frac1n\right)<y-x}.
$$

Aplicamos la localización entera a $x\,\iota_F(n)$. Existe $m\in\mathbb Z$ tal que

$$
\iota_F(m-1)\le x\,\iota_F(n)<\iota_F(m).
$$

Como $\iota_F(n)>0$, dividimos por ella:

$$
\iota_F\!\left(\frac{m-1}{n}\right)
\le x<
\iota_F\!\left(\frac mn\right).
$$

De la desigualdad izquierda antes de dividir se obtiene también

$$
\iota_F(m)\le x\,\iota_F(n)+1_F.
$$

Dividiendo otra vez por $\iota_F(n)$,

$$
\iota_F\!\left(\frac mn\right)
\le x+\iota_F\!\left(\frac1n\right)
< x+(y-x)=y.
$$

Para

$$
q=\frac mn\in\mathbb Q,
$$

queda

$$
\boxed{x<\iota_F(q)<y}.
$$

Así la copia canónica de $\mathbb Q$ es densa en $F$.

El mapa de dependencias es preciso:

- el orden permite comparar, trasladar e invertir desigualdades positivas;
- la arquimedianidad proporciona escalas enteras suficientemente grandes;
- el buen orden de $\mathbb N$ produce el mínimo de $K$;
- la estructura de cuerpo permite formar $(y-x)^{-1}$ y dividir por $n>0$;
- la incrustación racional traduce numerales, enteros, fracciones e inversos entre $\mathbb Q$ y $F$.

No se ha supuesto densidad por analogía geométrica: se la ha deducido estructuralmente.

*Referencia visual.* Véase la figura C00-F08 del texto principal, **De completitud a rejilla racional en F**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-041}

[]{#MA-EX-ANM-01-000-041}

### 41. Convertir una posición abstracta en una cortadura racional

Sea $x\in F$ y definamos

$$
A_x=\{q\in\mathbb Q:\iota_F(q)<x\}.
$$

Los tipos son

$$
x\in F,
\qquad
q\in\mathbb Q,
\qquad
\iota_F(q)\in F,
\qquad
A_x\subseteq\mathbb Q.
$$

La desigualdad que define $A_x$ ocurre en $F$, entre $\iota_F(q)$ y $x$; pero los objetos registrados son los racionales $q$. Por eso $A_x$ vive en $\mathbb Q$, no en $F$.

**No vaciedad.** Como

$$
x-1_F<x,
$$

la densidad racional proporciona $q_-\in\mathbb Q$ tal que

$$
x-1_F<\iota_F(q_-)<x.
$$

Entonces $q_-\in A_x$.

**Subconjunto propio.** Como

$$
x<x+1_F,
$$

la densidad racional proporciona $q_+\in\mathbb Q$ con

$$
x<\iota_F(q_+)<x+1_F.
$$

Por tanto $q_+\notin A_x$ y $A_x\ne\mathbb Q$.

**Clausura hacia abajo.** Si $q\in A_x$ y $p<q$, entonces

$$
\iota_F(p)<\iota_F(q)<x,
$$

por preservación estricta del orden. Luego $p\in A_x$. Aquí no se usa densidad.

**Ausencia de máximo.** Si $q\in A_x$, entonces $\iota_F(q)<x$. Por densidad racional existe $r\in\mathbb Q$ con

$$
\iota_F(q)<\iota_F(r)<x.
$$

Como $\iota_F$ refleja el orden, $q<r$, y además $r\in A_x$. Por tanto $A_x$ no tiene máximo.

Así,

$$
\boxed{A_x\in\mathcal D}.
$$

La densidad se usa en no vaciedad, propiedad de ser subconjunto propio y ausencia de máximo; la clausura hacia abajo usa sólo preservación del orden.

Tomemos ahora $c\in\mathbb Q$ y $x=\iota_F(c)$. Entonces

$$
\begin{aligned}
q\in A_{\iota_F(c)}
&\iff \iota_F(q)<\iota_F(c)\\
&\iff q<c.
\end{aligned}
$$

Por tanto

$$
\boxed{A_{\iota_F(c)}=\{q\in\mathbb Q:q<c\}=c^*}.
$$

La traza racional de un racional abstractamente incrustado reproduce exactamente la cortadura racional canónica. La compatibilidad aparece sin identificar a $F$ con el modelo concreto de Dedekind.

*Referencia visual.* Véase la figura C00-F09 del texto principal, **Traza racional y reconstrucción**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-042}

[]{#MA-EX-ANM-01-000-042}

### 42. Reconstruir un elemento desde su traza y recuperar el orden

Sea

$$
B_x=\iota_F(A_x)=\{\iota_F(q):q\in A_x\}\subseteq F.
$$

Como $A_x$ es una cortadura, $B_x$ es no vacío. Además, si $q\in A_x$, entonces

$$
\iota_F(q)<x,
$$

de modo que $x$ es una cota superior de $B_x$.

Aquí se gasta nuevamente la completitud de $F$: existe

$$
s=\sup_F B_x.
$$

Como $x$ es cota superior,

$$
s\le x.
$$

Supongamos $s<x$. Por densidad racional existe $q\in\mathbb Q$ tal que

$$
s<\iota_F(q)<x.
$$

La segunda desigualdad implica $q\in A_x$, de modo que $\iota_F(q)\in B_x$. Pero la primera afirma que un elemento de $B_x$ es mayor que su cota superior $s$, contradicción. Por tanto $s<x$ es imposible y

$$
\boxed{x=\sup_F\iota_F(A_x)}.
$$

Si $A_x=A_y$, entonces sus imágenes racionales coinciden y la reconstrucción da

$$
x=\sup_F\iota_F(A_x)=\sup_F\iota_F(A_y)=y.
$$

Así $x\mapsto A_x$ es inyectiva.

Si $x\le y$ y $q\in A_x$, entonces

$$
\iota_F(q)<x\le y,
$$

y por tanto $q\in A_y$. Luego

$$
x\le y\Longrightarrow A_x\subseteq A_y.
$$

Recíprocamente, si $A_x\subseteq A_y$, entonces

$$
\iota_F(A_x)\subseteq\iota_F(A_y).
$$

Como

$$
y=\sup_F\iota_F(A_y),
$$

$y$ es una cota superior de $\iota_F(A_x)$. Pero

$$
x=\sup_F\iota_F(A_x),
$$

así que $x\le y$. Por tanto

$$
\boxed{x\le y\iff A_x\subseteq A_y}.
$$

Si $x<y$, la densidad racional produce $q$ con

$$
x<\iota_F(q)<y.
$$

Entonces $q\in A_y\setminus A_x$, de modo que

$$
A_x\subsetneq A_y.
$$

Recíprocamente, si $A_x\subsetneq A_y$, la equivalencia no estricta da $x\le y$, y no puede ocurrir $x=y$ porque entonces las trazas serían iguales. Por tanto

$$
\boxed{x<y\iff A_x\subsetneq A_y}.
$$

Cada posición $x\in F$ queda así codificada por un subconjunto $A_x\subseteq\mathbb Q$, y tanto el elemento como su orden se recuperan desde esa información racional. Ésta es la razón por la que $\mathbb Q$ puede servir como lenguaje común entre modelos completos cuyos elementos sean literalmente distintos.

El límite de §0.9 debe permanecer visible: todavía no hemos definido ninguna aplicación

$$
F\longrightarrow G
$$

entre dos modelos completos. Sólo hemos construido el código racional que permitirá ese transporte en §0.10.

## §0.10. Únicos hasta isomorfismo

*Referencia visual.* Véase la figura C00-F09 del texto principal, **Traza racional y reconstrucción**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-043}

[]{#MA-EX-ANM-01-000-043}

### 43. Antes del transporte: demostrar que el supremo existe

Los universos deben mantenerse separados. Tenemos

$$
x\in F,
\qquad
A_x^F\subseteq\mathbb Q,
$$

mientras que

$$
\iota_G(A_x^F)
=
\{\iota_G(q):q\in A_x^F\}
\subseteq G.
$$

Si el supremo existe, entonces

$$
\phi(x)\in G.
$$

La no vaciedad es inmediata porque §0.9 ya demostró que $A_x^F$ es una cortadura. Elijamos

$$
r\in A_x^F.
$$

Entonces

$$
\iota_G(r)\in\iota_G(A_x^F),
$$

así que la imagen no es vacía.

Para la acotación superior usamos que la cortadura es propia. Elijamos

$$
u\in\mathbb Q\setminus A_x^F.
$$

Afirmamos que todo $q\in A_x^F$ satisface $q<u$. Si $q=u$, tendríamos $u\in A_x^F$. Si $u<q$, como $q\in A_x^F$ y la cortadura es cerrada hacia abajo, también tendríamos $u\in A_x^F$. Ambas posibilidades contradicen la elección de $u$. Por tricotomía,

$$
q<u.
$$

Como $\iota_G$ preserva el orden,

$$
\iota_G(q)<\iota_G(u)
\qquad(q\in A_x^F).
$$

Por tanto $\iota_G(u)$ es una cota superior de $\iota_G(A_x^F)$.

Hasta aquí no hemos usado completitud de $G$. Ahora sí: el conjunto es no vacío y está acotado superiormente, así que la propiedad del supremo de $G$ garantiza la existencia de

$$
\sup_G\iota_G(A_x^F).
$$

Sólo después de verificar esas hipótesis queda legítimamente definida

$$
\boxed{
\phi:F\longrightarrow G,
\qquad
\phi(x)=\sup_G\{\iota_G(q):q\in A_x^F\}.
}
$$

No se elige una cota superior especial para definir el valor: una cota sólo certifica la hipótesis de acotación. Tampoco se elige entre varios supremos, porque el supremo de un subconjunto, cuando existe, es único. Así, $\phi(x)$ queda forzado por $x$ y por las estructuras de $F$ y $G$.

*Referencia visual.* Véase la figura C00-F10 del texto principal, **Transporte canónico y unicidad**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-044}

[]{#MA-EX-ANM-01-000-044}

### 44. El transporte conserva exactamente la traza racional

Escribamos

$$
S_x=\iota_G(A_x^F),
\qquad
\phi(x)=\sup_GS_x.
$$

Primero probemos

$$
A_x^F\subseteq A_{\phi(x)}^G.
$$

Sea $q\in A_x^F$. Como $A_x^F$ no tiene máximo, existe $r\in A_x^F$ con

$$
q<r.
$$

Entonces

$$
\iota_G(q)<\iota_G(r).
$$

Además $\iota_G(r)\in S_x$, así que

$$
\iota_G(r)\le\sup_GS_x=\phi(x).
$$

Por tanto

$$
\iota_G(q)<\phi(x),
$$

y $q\in A_{\phi(x)}^G$.

Para la inclusión inversa, sea

$$
q\in A_{\phi(x)}^G.
$$

Entonces

$$
\iota_G(q)<\phi(x).
$$

Supongamos, buscando contradicción, que $q\notin A_x^F$. Como $A_x^F$ es una cortadura, para todo $r\in A_x^F$ debe cumplirse $r<q$: no puede ser $r=q$, y tampoco puede ocurrir $q<r$, pues la clausura hacia abajo forzaría $q\in A_x^F$.

Luego

$$
\iota_G(r)<\iota_G(q)
\qquad(r\in A_x^F).
$$

Así $\iota_G(q)$ sería una cota superior de $S_x$. La minimalidad del supremo daría

$$
\phi(x)=\sup_GS_x\le\iota_G(q),
$$

contradiciendo $\iota_G(q)<\phi(x)$. Por tanto $q\in A_x^F$.

Concluimos

$$
\boxed{A_{\phi(x)}^G=A_x^F}.
$$

Ahora sean $x,y\in F$. Por §0.9,

$$
x\le y
\iff
A_x^F\subseteq A_y^F.
$$

Usando la identidad de trazas,

$$
A_x^F\subseteq A_y^F
\iff
A_{\phi(x)}^G\subseteq A_{\phi(y)}^G
\iff
\phi(x)\le\phi(y).
$$

Así,

$$
\boxed{x\le y\iff\phi(x)\le\phi(y)}.
$$

La misma cadena con inclusiones estrictas produce

$$
\boxed{x<y\iff\phi(x)<\phi(y)}.
$$

En particular, si $\phi(x)=\phi(y)$, sus trazas son iguales; por la identidad anterior,

$$
A_x^F=A_y^F.
$$

La reconstrucción de §0.9 fuerza $x=y$. Luego $\phi$ es inyectiva.

El resultado es más fuerte que decir que $\phi$ es creciente: para cada $x$, el subconjunto de racionales situado debajo de $x$ es exactamente el mismo subconjunto que queda debajo de $\phi(x)$ en $G$. Se transporta la posición racional completa.

*Referencia visual.* Véase la figura C00-F10 del texto principal, **Transporte canónico y unicidad**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-045}

[]{#MA-EX-ANM-01-000-045}

### 45. Construir la inversa sin cardinalidad ni elección de preimágenes

Para $y\in G$, la traza

$$
A_y^G\subseteq\mathbb Q
$$

es una cortadura. Por el mismo argumento del ejercicio 43,

$$
\iota_F(A_y^G)
$$

es no vacío y está acotado superiormente en $F$. Aquí se gasta la completitud de $F$, que permite definir

$$
\boxed{
\psi(y)=\sup_F\{\iota_F(q):q\in A_y^G\}.
}
$$

Repitiendo literalmente el argumento de recuperación de traza del ejercicio 44 con $F$ y $G$ intercambiados, obtenemos

$$
\boxed{A_{\psi(y)}^F=A_y^G}.
$$

Sea ahora $x\in F$. Entonces

$$
\begin{aligned}
A_{\psi(\phi(x))}^F
&=A_{\phi(x)}^G\\
&=A_x^F.
\end{aligned}
$$

Dentro de $F$, la traza racional determina al elemento. Por tanto

$$
\boxed{\psi(\phi(x))=x}.
$$

Simétricamente, para $y\in G$,

$$
\begin{aligned}
A_{\phi(\psi(y))}^G
&=A_{\psi(y)}^F\\
&=A_y^G,
\end{aligned}
$$

y la reconstrucción en $G$ da

$$
\boxed{\phi(\psi(y))=y}.
$$

Así,

$$
\boxed{\psi=\phi^{-1}}.
$$

En particular, $\phi$ es biyectiva.

La dependencia completa es:

$$
\begin{array}{c}
\text{traza en }F\\
\downarrow\\
\text{completitud de }G\Rightarrow\phi\\
\downarrow\\
\text{misma traza en }G
\end{array}
\qquad
\begin{array}{c}
\text{traza en }G\\
\downarrow\\
\text{completitud de }F\Rightarrow\psi\\
\downarrow\\
\text{misma traza en }F.
\end{array}
$$

La composición recupera las trazas originales y, por tanto, los elementos originales. No se ha contado la cardinalidad de ningún modelo ni se ha escogido un preimagen de cada $y$ entre posibles candidatos: $\psi(y)$ está determinado canónicamente por la traza de $y$.

*Referencia visual.* Véase la figura C00-F10 del texto principal, **Transporte canónico y unicidad**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-046}

[]{#MA-EX-ANM-01-000-046}

### 46. Tres atajos que no producen un isomorfismo de cuerpos ordenados

Consideremos primero

$$
\tau(x)=x+1_F.
$$

Su inversa es

$$
\tau^{-1}(y)=y-1_F,
$$

así que $\tau$ es biyectiva. Además,

$$
x<y
\iff
x+1_F<y+1_F,
$$

por compatibilidad del orden con traslaciones. Por tanto preserva y refleja el orden.

Sin embargo,

$$
\tau(0_F)=1_F\ne0_F,
$$

y también

$$
\tau(x+y)=x+y+1_F,
$$

mientras que

$$
\tau(x)+\tau(y)=x+y+2_F.
$$

Por tanto no preserva cero ni suma. Mucho menos es un isomorfismo de cuerpos. La lección es

$$
\boxed{
\text{isomorfismo de órdenes}
\not\Rightarrow
\text{isomorfismo de cuerpos ordenados}.
}
$$

El segundo atajo confunde una propiedad de los conjuntos con una propiedad de una aplicación concreta. Por ejemplo, $\mathbb N$ tiene la misma cardinalidad que sí mismo, pero

$$
f:\mathbb N\longrightarrow\mathbb N,
\qquad
f(n)=n+1
$$

es inyectiva y no es sobreyectiva, porque $0$ no pertenece a su imagen. Por tanto, aun con igual cardinalidad, la sobreyectividad de una aplicación concreta necesita una prueba propia.

En §0.10 esa obligación se satisface construyendo explícitamente

$$
\psi:G\to F
$$

y demostrando que es inversa de $\phi$.

El tercer atajo deja casos lógicos abiertos. La afirmación

$$
\phi(xy)=\phi(x)\phi(y)
\qquad(x,y\ge0)
$$

sólo controla el cono no negativo. No contiene los casos

$$
x<0\le y,
\qquad
x\ge0>y,
\qquad
x<0,
\ y<0.
$$

Para cerrarlos se necesita primero la preservación del opuesto y luego la regla de signos. Por ejemplo, si $x<0\le y$,

$$
xy=-((-x)y),
$$

y el caso se reduce al producto de dos elementos no negativos sólo después de saber que

$$
\phi(-x)=-\phi(x).
$$

Las obligaciones correctas son, por tanto:

- para la biyectividad: construir y verificar una inversa;
- para la estructura de cuerpo: demostrar preservación de $0$, $1$, suma y producto;
- para la multiplicación: cerrar explícitamente todos los signos;
- para el orden: preservarlo y reflejarlo, sin confundir esa capa con la algebraica.

Ningún atajo sustituye esas verificaciones.

[]{#MA-SOL-ANM-01-000-047}

[]{#MA-EX-ANM-01-000-047}

### 47. Recuperar toda la aritmética desde las trazas

Primero fijamos la copia racional. Sea $q\in\mathbb Q$. Por §0.9,

$$
A_{\iota_F(q)}^F=q^*,
\qquad
A_{\iota_G(q)}^G=q^*.
$$

Como $\phi$ conserva trazas,

$$
A_{\phi(\iota_F(q))}^G
=A_{\iota_F(q)}^F
=q^*
=A_{\iota_G(q)}^G.
$$

La traza determina al elemento de $G$, así que

$$
\boxed{\phi(\iota_F(q))=\iota_G(q)}.
$$

En particular,

$$
\boxed{\phi(0_F)=0_G,
\qquad
\phi(1_F)=1_G.}
$$

Ahora caractericemos la suma. Supongamos

$$
q\in A_{x+y}^F.
$$

Entonces

$$
\iota_F(q)<x+y,
$$

y al trasladar $-y$,

$$
\iota_F(q)-y<x.
$$

Por densidad racional existe $r\in\mathbb Q$ tal que

$$
\iota_F(q)-y<\iota_F(r)<x.
$$

La segunda desigualdad dice $r\in A_x^F$. La primera equivale a

$$
\iota_F(q)-\iota_F(r)<y.
$$

Aplicando de nuevo densidad, elegimos $s\in\mathbb Q$ con

$$
\iota_F(q)-\iota_F(r)<\iota_F(s)<y.
$$

Entonces $s\in A_y^F$ y

$$
\iota_F(q)<\iota_F(r+s).
$$

La reflexión del orden da

$$
q<r+s.
$$

Recíprocamente, si $r\in A_x^F$, $s\in A_y^F$ y $q<r+s$, entonces

$$
\iota_F(r)<x,
\qquad
\iota_F(s)<y.
$$

Sumando,

$$
\iota_F(r+s)<x+y.
$$

Además

$$
\iota_F(q)<\iota_F(r+s),
$$

de modo que $\iota_F(q)<x+y$ y $q\in A_{x+y}^F$.

Por tanto

$$
\boxed{
q\in A_{x+y}^F
\iff
\exists r\in A_x^F\;\exists s\in A_y^F:
q<r+s.
}
$$

El lado derecho depende sólo de $A_x^F$ y $A_y^F$. Como

$$
A_{\phi(x)}^G=A_x^F,
\qquad
A_{\phi(y)}^G=A_y^F,
$$

la misma caracterización en $G$ da

$$
A_{\phi(x+y)}^G
=A_{x+y}^F
=A_{\phi(x)+\phi(y)}^G.
$$

La traza determina al elemento, luego

$$
\boxed{\phi(x+y)=\phi(x)+\phi(y)}.
$$

Aplicando esto a $x+(-x)=0_F$,

$$
\phi(x)+\phi(-x)=0_G,
$$

y por unicidad del inverso aditivo,

$$
\boxed{\phi(-x)=-\phi(x)}.
$$

Pasemos al producto. Supongamos $x,y\ge0_F$.

Si $q\in A_{xy}^F$ y $q<0$, estamos en la primera alternativa. Supongamos $q\ge0$. Entonces

$$
0\le\iota_F(q)<xy,
$$

por lo que $x>0$ y $y>0$. Multiplicando por $y^{-1}>0$,

$$
\iota_F(q)y^{-1}<x.
$$

Por densidad elegimos $r\in\mathbb Q$ con

$$
\iota_F(q)y^{-1}<\iota_F(r)<x.
$$

Como el extremo izquierdo es no negativo, $r>0$; además $r\in A_x^F$. La primera desigualdad da

$$
\iota_F(q)<\iota_F(r)y.
$$

Multiplicando por $\iota_F(r)^{-1}>0$,

$$
\iota_F(q)\iota_F(r)^{-1}<y.
$$

Por densidad elegimos $s\in\mathbb Q$ con

$$
\iota_F(q)\iota_F(r)^{-1}<\iota_F(s)<y.
$$

Entonces $s>0$, $s\in A_y^F$ y

$$
\iota_F(q)<\iota_F(rs),
$$

de donde $q<rs$.

Recíprocamente, si $q<0$, entonces

$$
\iota_F(q)<0_F\le xy,
$$

y $q\in A_{xy}^F$.

Si existen $r,s>0$ con $r\in A_x^F$, $s\in A_y^F$ y $q<rs$, entonces

$$
0<\iota_F(r)<x,
\qquad
0<\iota_F(s)<y.
$$

La compatibilidad del producto con el orden da

$$
\iota_F(r)\iota_F(s)<xy,
$$

y como

$$
\iota_F(q)<\iota_F(rs)
=\iota_F(r)\iota_F(s),
$$

obtenemos $q\in A_{xy}^F$.

Así,

$$
\boxed{
q\in A_{xy}^F
\iff
q<0
\ \text{o}\
\exists r,s>0:
(r\in A_x^F,
\ s\in A_y^F,
\ q<rs).
}
$$

Este criterio depende sólo de las trazas. Por tanto, para $x,y\ge0$,

$$
A_{\phi(xy)}^G
=A_{\phi(x)\phi(y)}^G,
$$

y

$$
\boxed{\phi(xy)=\phi(x)\phi(y)}.
$$

Quedan los signos.

Si $x<0\le y$, entonces

$$
xy=-((-x)y).
$$

Como $-x>0$,

$$
\begin{aligned}
\phi(xy)
&=-\phi((-x)y)\\
&=-\bigl(\phi(-x)\phi(y)\bigr)\\
&=-\bigl((-\phi(x))\phi(y)\bigr)\\
&=\phi(x)\phi(y).
\end{aligned}
$$

El caso $x\ge0>y$ es simétrico. Si $x<0$ y $y<0$, entonces

$$
xy=(-x)(-y),
$$

y

$$
\begin{aligned}
\phi(xy)
&=\phi((-x)(-y))\\
&=\phi(-x)\phi(-y)\\
&=(-\phi(x))(-\phi(y))\\
&=\phi(x)\phi(y).
\end{aligned}
$$

Por tanto

$$
\boxed{
\phi(xy)=\phi(x)\phi(y)
\qquad(x,y\in F).
}
$$

Finalmente, si $x\ne0_F$, entonces

$$
xx^{-1}=1_F.
$$

Aplicando $\phi$,

$$
\phi(x)\phi(x^{-1})=1_G.
$$

Como $\phi$ es inyectiva y preserva cero, $\phi(x)\ne0_G$. Por unicidad del inverso,

$$
\boxed{\phi(x^{-1})=\phi(x)^{-1}}.
$$

Toda la aritmética queda así transportada desde la información racional, sin calcular directamente los supremos que definen las imágenes.

*Referencia visual.* Véase la figura C00-F12 del texto principal, **La aritmética viaja con la traza**, como síntesis posterior de este argumento.

[]{#MA-SOL-ANM-01-000-048}

[]{#MA-EX-ANM-01-000-048}

### 48. Cerrar la unicidad estructural de los números reales

Por los ejercicios 43–47, $\phi:F\to G$ es biyectiva, preserva y refleja el orden, satisface

$$
\phi(0_F)=0_G,
\qquad
\phi(1_F)=1_G,
$$

preserva suma y producto, y por tanto es un isomorfismo de cuerpos ordenados:

$$
\boxed{\phi:F\xrightarrow{\sim}G}.
$$

Falta demostrar que es el único.

Sea

$$
T:F\longrightarrow G
$$

un isomorfismo de cuerpos ordenados cualquiera. La composición

$$
T\circ\iota_F:\mathbb Q\longrightarrow G
$$

es una incrustación de cuerpos ordenados: preserva $0$, $1$, suma, producto y orden. Pero §0.9 demostró que la incrustación racional en un cuerpo ordenado es canónica y única. Por tanto

$$
\boxed{T\circ\iota_F=\iota_G}.
$$

Sea $x\in F$ y $q\in\mathbb Q$. Entonces

$$
\begin{aligned}
q\in A_x^F
&\iff \iota_F(q)<x\\
&\iff T(\iota_F(q))<T(x)\\
&\iff \iota_G(q)<T(x)\\
&\iff q\in A_{T(x)}^G.
\end{aligned}
$$

Así,

$$
\boxed{A_{T(x)}^G=A_x^F}.
$$

Por construcción del transporte canónico,

$$
A_{\phi(x)}^G=A_x^F.
$$

Luego

$$
A_{T(x)}^G=A_{\phi(x)}^G.
$$

La traza racional determina al elemento de $G$, de modo que

$$
T(x)=\phi(x).
$$

Como $x$ era arbitrario,

$$
\boxed{T=\phi}.
$$

Por tanto:

$$
\boxed{
\text{si }F\text{ y }G\text{ son cuerpos ordenados completos,}
\\
\text{existe un único isomorfismo de cuerpos ordenados }F\to G.
}
$$

Tomando $F=G$, todo automorfismo de cuerpo ordenado de $F$ debe coincidir con el transporte canónico de $F$ a sí mismo. La identidad es uno de esos isomorfismos, luego por unicidad

$$
\boxed{\operatorname{Aut}_{\mathrm{ord\text{-}field}}(F)=\{\operatorname{id}_F\}}.
$$

Ahora separamos las tres afirmaciones.

**Igualdad literal.**

$$
F=G
$$

significa que ambos son el mismo conjunto equipado con exactamente las mismas operaciones y relación. El capítulo no exige ni demuestra esto para dos realizaciones arbitrarias.

**Existencia de isomorfismo.**

$$
F\cong G
$$

significa que existe una biyección que conserva la estructura de cuerpo ordenado. Esto ya dice que las dos realizaciones tienen la misma estructura abstracta.

**Único isomorfismo de cuerpos ordenados.** Aquí hemos demostrado algo más fuerte: la estructura obliga a una sola correspondencia posible, determinada por la copia racional y por las trazas.

Por eso el transporte es **canónico por unicidad**: no depende de elegir coordenadas, representantes o una biyección conveniente. Sin embargo, canonicidad no es sinónimo de computabilidad. La definición

$$
\phi(x)=\sup_G\iota_G(A_x^F)
$$

determina matemáticamente un único elemento, pero no proporciona por sí sola un algoritmo efectivo para calcularlo a partir de cualquier codificación imaginable de $F$ y $G$.

El arco del capítulo queda entonces cerrado en dos etapas.

Primero, las cortaduras de Dedekind construyeron un testigo concreto:

$$
\boxed{\text{existe un cuerpo ordenado completo}.}
$$

Después, el argumento abstracto con trazas racionales demuestra:

$$
\boxed{\text{cualesquiera dos cuerpos ordenados completos son únicamente isomorfos}.}
$$

En conjunto,

$$
\boxed{
\text{EXISTENCIA}
+
\text{UNICIDAD HASTA ÚNICO ISOMORFISMO}
=
\text{JUSTIFICACIÓN ESTRUCTURAL DE }\mathbb R.
}
$$

Las cortaduras son una realización concreta. Lo que autoriza a hablar de **los números reales** sin imponer esa realización como ontología obligatoria es la estructura compartida: cuerpo ordenado completo, determinada hasta único isomorfismo.

*Referencias visuales.* Véanse las figuras C00-F10 (**Transporte canónico y unicidad**) y C00-F12 (**La aritmética viaja con la traza**) del texto principal para sintetizar, respectivamente, las capas de este cierre.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)

## 13.2. Colas y propiedades eventuales {#sec-ta-13-2}

La definición de sucesión describe todos sus términos simultáneamente, pero el análisis de convergencia depende de una idea diferente: muchas propiedades no necesitan cumplirse desde el primer índice. Sólo importa que terminen siendo verdaderas de manera permanente.

Esta asimetría entre el comienzo y la parte tardía de una sucesión es esencial. Si queremos estudiar qué ocurre cuando el índice crece, debemos disponer de un lenguaje que permita ignorar un número fijo de términos iniciales sin borrar el orden ni las repeticiones de los términos restantes.

El patrón lógico que aparecerá una y otra vez es

$$
\boxed{
\exists N\in\mathbb N\;\forall n\in\mathbb N,
\qquad
N\le n\Longrightarrow \mathcal P(n).
}
$$

Antes de usarlo en la definición de convergencia, lo aislaremos y estudiaremos por sí mismo.

### Definición 13.2.1 — Segmento final de los naturales

Sea $N\in\mathbb N$. Definimos el segmento final de $\mathbb N$ a partir de $N$ por

$$
\boxed{
\mathbb N_{\ge N}
:=
\{n\in\mathbb N:N\le n\}.
}
$$

El conjunto existe por Separación dentro de $\mathbb N$.

Como $N\le N$, se tiene

$$
N\in\mathbb N_{\ge N},
$$

de modo que todo segmento final es no vacío.

La expresión «para todo $n$ suficientemente grande» significará precisamente «para todo $n$ perteneciente a algún segmento final $\mathbb N_{\ge N}$». No introduce una noción métrica de tamaño: sólo utiliza el orden ya construido en $\mathbb N$.

### Proposición 13.2.2 — Monotonía de los segmentos finales

Si $N,M\in\mathbb N$ y

$$
N\le M,
$$

entonces

$$
\boxed{
\mathbb N_{\ge M}
\subseteq
\mathbb N_{\ge N}.
}
$$

**Demostración.**

Sea $n\in\mathbb N_{\ge M}$. Por Definición 13.2.1 — Segmento final de los naturales,

$$
M\le n.
$$

La hipótesis da $N\le M$, y la transitividad del orden natural de Proposición 1.6.2 — Reflexividad y transitividad produce

$$
N\le n.
$$

Por tanto $n\in\mathbb N_{\ge N}$. Como $n$ era arbitrario,

$$
\mathbb N_{\ge M}\subseteq\mathbb N_{\ge N}.
$$

∎

La dirección de la inclusión merece atención: cuanto mayor es el umbral, menor es el segmento final. Pedir una propiedad desde $M$ con $N\le M$ permite descartar al menos tantos términos iniciales como pedirla desde $N$.

### Definición 13.2.3 — Cola reindexada de una sucesión

Sea

$$
a=(a_n)_{n\in\mathbb N}
$$

una sucesión real y sea $N\in\mathbb N$. Definimos la cola reindexada de $a$ a partir de $N$ como la sucesión real

$$
\boxed{
a^{\langle N\rangle}:\mathbb N\longrightarrow\mathbb R}
$$

dada por

$$
\boxed{
a^{\langle N\rangle}_k:=a_{N+k}
\qquad(k\in\mathbb N).
}
$$

El grafo correspondiente es

$$
G_{a^{\langle N\rangle}}
:=
\left\{
\langle k,x\rangle\in\mathbb N\times\mathbb R:
 x=a_{N+k}
\right\},
$$

que existe por Separación. Para cada $k\in\mathbb N$, la suma natural $N+k$ pertenece a $\mathbb N$, y como $a:\mathbb N\to\mathbb R$, el valor $a_{N+k}$ es un único número real. Por tanto el grafo determina una función $\mathbb N\to\mathbb R$.

La reindexación es deliberada. La familia restringida a $\mathbb N_{\ge N}$ tendría dominio $\mathbb N_{\ge N}$, no $\mathbb N$; en cambio $a^{\langle N\rangle}$ vuelve a ser una sucesión real en el sentido exacto de Definición 13.1.1 — Sucesión real.

> **Lectura conceptual.** Tomar una cola no significa reemplazar la sucesión por el conjunto de sus valores tardíos. Conservamos el orden de aparición y las repeticiones; únicamente desplazamos el origen de los índices.

### Definición 13.2.4 — Conjunto eventual y propiedad eventual

Sea $E\subseteq\mathbb N$. Diremos que $E$ es eventual si contiene algún segmento final de los naturales; es decir, si

$$
\boxed{
\exists N\in\mathbb N,
\qquad
\mathbb N_{\ge N}\subseteq E.
}
$$

Equivalentemente, si $\mathcal P(n)$ es una propiedad de números naturales cuyos parámetros permanecen fijos, diremos que

> $\mathcal P(n)$ vale eventualmente

si el conjunto

$$
E_{\mathcal P}
:=
\{n\in\mathbb N:\mathcal P(n)\}
$$

es eventual. Por la definición del segmento final, esto equivale exactamente a

$$
\boxed{
\exists N\in\mathbb N\;\forall n\in\mathbb N,
\qquad
N\le n\Longrightarrow\mathcal P(n).
}
$$

El número $N$ es un umbral para la propiedad. No se exige que sea el menor umbral ni que esté determinado de manera única.

Esta definición distingue dos ideas que no deben confundirse:

- que una propiedad vuelva a ocurrir para índices cada vez mayores;
- que, desde algún índice en adelante, no vuelva a fallar.

Sólo la segunda es eventualidad.

### Proposición 13.2.5 — Reglas elementales de eventualidad

Sean $E,F\subseteq\mathbb N$.

1. $\mathbb N$ es eventual.
2. Si $E$ es eventual y $E\subseteq F$, entonces $F$ es eventual.
3. Si $E$ y $F$ son eventuales, entonces $E\cap F$ es eventual.

En lenguaje de propiedades, si $\mathcal P(n)$ y $\mathcal Q(n)$ valen eventualmente, entonces

$$
\boxed{
\mathcal P(n)\land\mathcal Q(n)
\quad\text{vale eventualmente}.}
$$

Además, si $\mathcal P(n)$ vale eventualmente y

$$
\forall n\in\mathbb N,
\qquad
\mathcal P(n)\Longrightarrow\mathcal Q(n),
$$

entonces $\mathcal Q(n)$ vale eventualmente.

**Demostración.**

Para (1), cualquier segmento final está contenido en $\mathbb N$; por ejemplo,

$$
\mathbb N_{\ge 0}\subseteq\mathbb N.
$$

Luego $\mathbb N$ es eventual.

Para (2), si $E$ es eventual, existe $N\in\mathbb N$ con

$$
\mathbb N_{\ge N}\subseteq E.
$$

Si además $E\subseteq F$, la transitividad de la inclusión da

$$
\mathbb N_{\ge N}\subseteq F,
$$

y por tanto $F$ es eventual.

Para (3), sean $N,M\in\mathbb N$ umbrales tales que

$$
\mathbb N_{\ge N}\subseteq E,
\qquad
\mathbb N_{\ge M}\subseteq F.
$$

Como el orden de $\mathbb N$ es total por Teorema 1.6.5 — Orden total, se cumple

$$
N\le M
\qquad\text{o}\qquad
M\le N.
$$

Si $N\le M$, Proposición 13.2.2 — Monotonía de los segmentos finales da

$$
\mathbb N_{\ge M}\subseteq\mathbb N_{\ge N}\subseteq E,
$$

y ya teníamos $\mathbb N_{\ge M}\subseteq F$. Por tanto

$$
\mathbb N_{\ge M}\subseteq E\cap F.
$$

El caso $M\le N$ es simétrico, tomando $N$ como umbral común. Así $E\cap F$ es eventual.

Las dos formulaciones en lenguaje de propiedades son traducciones directas de (2) y (3) mediante los conjuntos de verdad correspondientes. ∎

La tercera regla es el mecanismo que más adelante permitirá combinar varias estimaciones: si una desigualdad vale desde un índice y otra desde quizá otro índice, podemos pasar a un único umbral después del cual ambas son verdaderas.

### Definición 13.2.6 — Coincidencia eventual de sucesiones reales

Sobre el conjunto $\mathbb R^{\mathbb N}$ definimos la relación

$$
\sim_{\mathrm{ev}}\;\subseteq
\mathbb R^{\mathbb N}\times\mathbb R^{\mathbb N}
$$

por Separación, declarando para $a,b\in\mathbb R^{\mathbb N}$ que $a$ y $b$ coinciden eventualmente, y escribiendo

$$
\boxed{
a\sim_{\mathrm{ev}}b,}
$$

si la propiedad

$$
a_n=b_n
$$

vale eventualmente. Equivalentemente,

$$
\boxed{
a\sim_{\mathrm{ev}}b
\iff
\exists N\in\mathbb N\;\forall n\in\mathbb N,
\quad
N\le n\Longrightarrow a_n=b_n.
}
$$

La coincidencia eventual es estrictamente más débil que la igualdad de sucesiones. La igualdad exige coincidencia en todo índice; $a\sim_{\mathrm{ev}}b$ permite discrepancias antes de algún umbral.

### Proposición 13.2.7 — La coincidencia eventual es una relación de equivalencia

La relación $\sim_{\mathrm{ev}}$ es una relación de equivalencia sobre $\mathbb R^{\mathbb N}$.

**Demostración.**

**Reflexividad.** Para toda sucesión $a$ y todo $n\in\mathbb N$,

$$
a_n=a_n.
$$

Por Proposición 13.2.5 — Reglas elementales de eventualidad (1), la propiedad vale eventualmente. Luego

$$
a\sim_{\mathrm{ev}}a.
$$

**Simetría.** Si $a\sim_{\mathrm{ev}}b$, entonces $a_n=b_n$ eventualmente. Por simetría de la igualdad,

$$
b_n=a_n
$$

para esos mismos índices. Por tanto

$$
b\sim_{\mathrm{ev}}a.
$$

**Transitividad.** Supongamos

$$
a\sim_{\mathrm{ev}}b,
\qquad
b\sim_{\mathrm{ev}}c.
$$

Las propiedades

$$
a_n=b_n
\qquad\text{y}\qquad
b_n=c_n
$$

valen eventualmente. Por Proposición 13.2.5 — Reglas elementales de eventualidad (3), ambas valen simultáneamente desde algún umbral común. En esos índices, la transitividad de la igualdad da

$$
a_n=c_n.
$$

Por Proposición 13.2.5 — Reglas elementales de eventualidad (2), esta última propiedad es eventual. Luego

$$
a\sim_{\mathrm{ev}}c.
$$

Se satisfacen las tres condiciones de Definición 0.4.7 — Relación de equivalencia. ∎

### Proposición 13.2.8 — Caracterización por igualdad de colas

Sean $a,b\in\mathbb R^{\mathbb N}$. Entonces

$$
\boxed{
a\sim_{\mathrm{ev}}b
\iff
\exists N\in\mathbb N,
\qquad
a^{\langle N\rangle}=b^{\langle N\rangle}.
}
$$

**Demostración.**

Supongamos primero

$$
a\sim_{\mathrm{ev}}b.
$$

Por Definición 13.2.6 — Coincidencia eventual de sucesiones reales, existe $N\in\mathbb N$ tal que

$$
N\le n
\Longrightarrow
 a_n=b_n
$$

para todo $n\in\mathbb N$.

Sea $k\in\mathbb N$. Por la definición del orden natural Definición 1.6.1 — Orden aritmético,

$$
N\le N+k,
$$

pues $k$ es un testigo de

$$
N+k=N+k.
$$

En consecuencia,

$$
a_{N+k}=b_{N+k}.
$$

Por Definición 13.2.3 — Cola reindexada de una sucesión, esto equivale a

$$
a^{\langle N\rangle}_k
=
b^{\langle N\rangle}_k.
$$

Como vale para todo $k\in\mathbb N$, el criterio término a término Proposición 13.1.2 — Criterio término a término para la igualdad de sucesiones reales produce

$$
a^{\langle N\rangle}=b^{\langle N\rangle}.
$$

Recíprocamente, supongamos que existe $N\in\mathbb N$ tal que

$$
a^{\langle N\rangle}=b^{\langle N\rangle}.
$$

Sea $n\in\mathbb N$ con $N\le n$. Por Definición 1.6.1 — Orden aritmético, existe $k\in\mathbb N$ tal que

$$
N+k=n.
$$

Evaluando la igualdad de las colas en ese índice $k$ obtenemos

$$
a_{N+k}=b_{N+k},
$$

y por tanto

$$
a_n=b_n.
$$

Así $a_n=b_n$ para todo $n\ge N$, es decir,

$$
a\sim_{\mathrm{ev}}b.
$$

∎

La proposición expresa con exactitud la intuición que necesitábamos: dos sucesiones coinciden eventualmente si, después de eliminar un tramo inicial adecuado y reindexar, se vuelven literalmente la misma sucesión.

> **Prueba de estrés conceptual.** «Eventualmente» no significa «para muchos índices», «para infinitos índices» ni «cada vez con mayor frecuencia». Significa que existe un único umbral tras el cual ya no aparecen excepciones. Esta diferencia será decisiva cuando cuantifiquemos sobre tolerancias en la definición de convergencia.

La infraestructura lógica está ahora preparada. En la sección siguiente podremos formular rigurosamente qué significa que los términos de una sucesión real permanezcan eventualmente dentro de cada tolerancia positiva alrededor de un número real, conservando visible el orden de los cuantificadores.

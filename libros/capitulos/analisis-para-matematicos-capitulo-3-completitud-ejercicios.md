---
title: "Ejercicios — Capítulo 3"
content-id: MA-BCH-0093
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-003-EJERCICIOS
book-id: MA-BOK-0009
status: published
solution-status: complete
date-created: 2026-09-30
date-modified: 2026-09-30
areas: [analisis]
level: universitario
topics: [analisis-real, orden, topologia]
prerequisites: [MA-BCH-0084]
related: [MA-BOK-0009]
provenance:
  type: original
  sources:
    - "Manuscrito ANM C03; referencias de contraste en la portada del libro."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Capítulo 3](analisis-para-matematicos-capitulo-3-completitud.md) · [Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Ejercicios](analisis-para-matematicos-capitulo-3-completitud-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-3-completitud-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-3-completitud-microcontroles.md)

# Ejercicios — Capítulo 3

## §3.1. El problema heredado: definir no basta

[]{#MA-EX-ANM-01-003-001}

### 1. Qué permiten concluir las hipótesis

Sea $X$ un sistema ordenado y sea $A\subseteq X$. Supón únicamente que

$$
A\ne\varnothing
\qquad\text{y}\qquad
U_X(A)\ne\varnothing,
$$

donde

$$
U_X(A)=\{u\in X:\forall a\in A,\ a\le u\}.
$$

Clasifica cada afirmación como **forzada por las hipótesis**, **no forzada** o **condicional**:

1. $A$ posee al menos una cota superior en $X$.
2. $U_X(A)$ posee un mínimo.
3. La expresión $\sup_X A$ designa necesariamente un elemento existente de $X$.
4. Si existe $s=\min U_X(A)$, entonces $s=\sup_X A$.
5. Si $\sup_X A$ existe, entonces necesariamente $\sup_X A\in A$.
6. Si $A$ es no vacío y está acotado superiormente, entonces $A$ posee máximo.

Para cada afirmación que no esté forzada, indica qué información adicional faltaría o da un ejemplo que muestre el fallo. No uses el principio del supremo de §3.2.

[]{#MA-EX-ANM-01-003-002}

### 2. Densidad no fabrica una frontera

Un estudiante razona así sobre

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}:
$$

> Como $\mathbb Q$ es denso y $S_2$ tiene cotas superiores racionales, podemos tomar cotas cada vez más ajustadas. Entre racionales siempre hay racionales, así que al final debe aparecer una cota racional que sea la menor. Por tanto, $S_2$ tiene supremo en $\mathbb Q$.

Diagnostica el argumento.

1. Escribe con cuantificadores qué afirma realmente la densidad de $\mathbb Q$.
2. Identifica el salto lógico que pretende pasar de «hay racionales intermedios» a «existe una menor cota superior racional».
3. Explica por qué disponer de cotas superiores cada vez menores no implica que la familia de cotas superiores tenga mínimo.
4. Reescribe la conclusión correcta que sí puede obtenerse de la densidad, sin atribuirle una propiedad de completitud.

No invoques todavía ningún principio de completitud de $\mathbb R$.

[]{#MA-EX-ANM-01-003-003}

### 3. Probar el fallo racional sin nombrar la frontera

Demuestra directamente que

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}
$$

no posee supremo en $\mathbb Q$.

Supón, buscando una contradicción, que existe

$$
s=\sup_{\mathbb Q}S_2.
$$

Como $1\in S_2$, sabemos que $s\ge1$. Define

$$
T(s)=\frac{2(s+1)}{s+2}.
$$

1. Demuestra las identidades
   $$
   T(s)-s=\frac{2-s^2}{s+2}
   $$
   y
   $$
   2-T(s)^2=\frac{2(2-s^2)}{(s+2)^2}.
   $$
2. Si $s^2<2$, demuestra que $T(s)\in S_2$ y $T(s)>s$, contradiciendo que $s$ sea cota superior.
3. Si $s^2>2$, demuestra que $0<T(s)<s$, que $T(s)^2>2$ y que $T(s)$ sigue siendo una cota superior racional de $S_2$, contradiciendo la minimalidad de $s$.
4. Excluye el caso $s^2=2$ mediante un argumento de divisibilidad para racionales escritos en términos irreducibles.
5. Concluye que $U_{\mathbb Q}(S_2)$ es no vacío pero no posee mínimo.

La demostración debe permanecer enteramente dentro de $\mathbb Q$ y no debe identificar la frontera ausente con un número real ya nombrado.

[]{#MA-EX-ANM-01-003-004}

### 4. Cambiar el umbral cambia la existencia, no la densidad

Compara los tres conjuntos racionales

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\},
$$

$$
S_4^{<}=\{q\in\mathbb Q:0\le q,\ q^2<4\},
$$

y

$$
S_4^{\le}=\{q\in\mathbb Q:0\le q,\ q^2\le4\}.
$$

1. Verifica que los tres conjuntos son no vacíos y están acotados superiormente en $\mathbb Q$.
2. Usa el ejercicio anterior para recordar por qué $S_2$ no posee supremo racional.
3. Demuestra directamente, desde la definición, que
   $$
   \sup_{\mathbb Q}S_4^{<}=2,
   $$
   aunque $S_4^{<}$ no tenga máximo.
4. Demuestra que
   $$
   \max S_4^{\le}=\sup_{\mathbb Q}S_4^{\le}=2.
   $$
5. Determina $U_{\mathbb Q}(S_4^{<})$ y $U_{\mathbb Q}(S_4^{\le})$.
6. Explica por qué estos tres ejemplos impiden atribuir a la densidad de $\mathbb Q$ la existencia o inexistencia del supremo: la densidad es la misma en los tres casos, mientras que el comportamiento de la barrera extremal cambia.

No uses resultados de §3.2 o posteriores.

## §3.2. El principio del supremo

[]{#MA-EX-ANM-01-003-005}

### 5. Antes de invocar el principio

Para cada conjunto siguiente, decide si el **principio del supremo** puede aplicarse directamente en $\mathbb R$:

$$
A=(-2,5),
\qquad
B=[0,\infty),
\qquad
C=\varnothing,
\qquad
D=\{3\}.
$$

En cada caso:

1. verifica explícitamente si el conjunto es no vacío;
2. verifica explícitamente si está acotado superiormente en $\mathbb R$;
3. sólo cuando ambas hipótesis estén satisfechas, escribe la conclusión de existencia autorizada por completitud;
4. distingue esa conclusión de la afirmación más fuerte de que el conjunto tenga máximo.

No calcules supremos mediante resultados posteriores: el objetivo es entrenar la lectura exacta de las hipótesis del principio.

[]{#MA-EX-ANM-01-003-006}

### 6. El mismo conjunto, dos universos distintos

Considera de nuevo

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}.
$$

Podemos leerlo como subconjunto de $\mathbb Q$ o, usando $\mathbb Q\subseteq\mathbb R$, como subconjunto de $\mathbb R$.

1. Verifica que $S_2$ es no vacío y posee una cota superior racional; concluye que también es no vacío y está acotado superiormente como subconjunto de $\mathbb R$.
2. Explica por qué el principio del supremo adoptado en §3.2 puede invocarse para $S_2\subseteq\mathbb R$, pero no puede invocarse como si fuese un axioma válido en $\mathbb Q$.
3. Concluye, sin calcularlo, que existe
   $$
   s=\sup_{\mathbb R}S_2.
   $$
4. Usa el resultado del ejercicio 3 para demostrar que ese $s$ no puede ser racional.
5. Explica por qué la frase «$S_2$ tiene supremo» es incompleta si no se especifica el sistema ordenado en el que se busca la menor cota superior.

No identifiques $s$ con ningún número real concreto.

[]{#MA-EX-ANM-01-003-007}

### 7. La inclusión produce una desigualdad entre supremos existentes

Sean $A,B\subseteq\mathbb R$ tales que

$$
A\ne\varnothing,
\qquad
A\subseteq B,
\qquad
B\text{ está acotado superiormente}.
$$

Demuestra que existen $\sup A$ y $\sup B$ y que

$$
\sup A\le\sup B.
$$

La prueba debe separar explícitamente estas etapas:

1. demostrar que $B\ne\varnothing$;
2. demostrar que $A$ está acotado superiormente;
3. indicar cada aplicación del principio del supremo;
4. explicar por qué $\sup B$ es una cota superior de $A$;
5. usar la minimalidad de $\sup A$ para obtener la desigualdad final.

No cites simplemente «monotonía del supremo»: reconstruye la demostración desde las definiciones y el principio de existencia.

[]{#MA-EX-ANM-01-003-008}

### 8. Trasladar un conjunto sin gastar completitud dos veces

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

Demuestra que

$$
\sup(A+c)=\sup A+c.
$$

Tu demostración debe organizarse de modo que el principio del supremo se use **una sola vez**:

1. aplica completitud a $A$ y escribe $s=\sup A$;
2. demuestra directamente que $s+c$ es una cota superior de $A+c$;
3. demuestra directamente que cualquier cota superior $v$ de $A+c$ satisface $s+c\le v$;
4. concluye, por la definición de supremo, que $s+c=\sup(A+c)$, sin volver a invocar el principio del supremo;
5. usando la caracterización $\varepsilon$ de C02, deduce que para todo $\varepsilon>0$ existe $y\in A+c$ tal que
   $$
   s+c-\varepsilon<y\le s+c.
   $$

Al final, identifica qué paso usa completitud y cuáles usan sólo orden, álgebra y resultados ya demostrados en C02.

[]{#MA-EX-ANM-01-003-009}

### 9. Un supremo real no vuelve completo a $\mathbb Q$

Un estudiante afirma:

> Todo conjunto $A\subseteq\mathbb Q$ no vacío y acotado superiormente en $\mathbb Q$ también es un subconjunto no vacío y acotado superiormente de $\mathbb R$. Por el principio del supremo, $A$ tiene un supremo real. Por tanto, $\mathbb Q$ satisface el principio del supremo y es completo.

Diagnostica el razonamiento.

1. Determina qué parte del argumento es correcta.
2. Formula exactamente qué tendría que garantizar el principio del supremo **interno a $\mathbb Q$**.
3. Explica por qué la existencia de $\sup_{\mathbb R}A$ no implica que exista $\sup_{\mathbb Q}A$.
4. Usa $S_2$ como contraejemplo decisivo.
5. Reescribe la conclusión correcta: ¿qué sí proporciona la completitud de $\mathbb R$ a un subconjunto racional no vacío y racionalmente acotado superiormente?
6. Identifica el paso en el que el estudiante cambia ilegítimamente el universo al que debe pertenecer el objeto cuya existencia se reclama.

La respuesta debe distinguir **existencia externa en $\mathbb R$** de **existencia interna en $\mathbb Q$**.
## §3.3. La cara dual: el principio del ínfimo

[]{#MA-EX-ANM-01-003-010}

### 10. Traducir una prueba superior a lenguaje inferior

Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente, y define

$$
B=-A=\{-a:a\in A\}.
$$

Construye un **diccionario de reflexión** que traduzca, línea por línea, las siguientes afirmaciones sobre $B$ a afirmaciones equivalentes sobre $A$:

1. $u$ es una cota superior de $B$;
2. $s=\sup B$;
3. $b\le s$ para todo $b\in B$;
4. si $u$ es cota superior de $B$, entonces $s\le u$;
5. para todo $\varepsilon>0$ existe $b\in B$ tal que
   $$
   s-\varepsilon<b\le s.
   $$

En cada traducción debes sustituir explícitamente $b=-a$, indicar cuándo una desigualdad cambia de sentido al multiplicar por $-1$ y expresar el resultado final en términos de $A$ y de $i=-s$.

Concluye qué papel desempeña la reflexión en el paso de supremo a ínfimo. No invoques todavía ningún resultado de §3.4 o posteriores.

[]{#MA-EX-ANM-01-003-011}

### 11. Las familias completas de cotas también se reflejan

Para un conjunto $A\subseteq\mathbb R$, define

$$
L(A)=\{l\in\mathbb R:\forall a\in A,\ l\le a\}
$$

y, para cualquier conjunto $E\subseteq\mathbb R$,

$$
-E=\{-x:x\in E\}.
$$

Supón que $A$ es no vacío y está acotado inferiormente.

1. Demuestra la igualdad de conjuntos
   $$
   U(-A)=-L(A).
   $$
2. Verifica, antes de usar completitud, que $-A$ es no vacío y está acotado superiormente.
3. Aplica el principio del supremo a $-A$ y escribe
   $$
   s=\sup(-A).
   $$
4. Usa la igualdad del apartado 1 para demostrar que
   $$
   -s=\max L(A).
   $$
5. Concluye que
   $$
   \inf A=-\sup(-A).
   $$

La prueba debe localizar exactamente el único paso de completitud y separar la existencia de $s$ de las manipulaciones de las familias de cotas.

[]{#MA-EX-ANM-01-003-012}

### 12. El ínfimo de una unión

Sean $A,B\subseteq\mathbb R$ conjuntos no vacíos y acotados inferiormente.

Demuestra que $A\cup B$ es no vacío y está acotado inferiormente y prueba que

$$
\boxed{
\inf(A\cup B)=\min\{\inf A,\inf B\}.
}
$$

La demostración debe incluir:

1. una construcción explícita de una cota inferior de $A\cup B$ a partir de cotas inferiores de $A$ y de $B$;
2. la justificación de existencia de los tres ínfimos que aparecen;
3. la prueba de que
   $$
   m=\min\{\inf A,\inf B\}
   $$
   es cota inferior de $A\cup B$;
4. la prueba de que cualquier cota inferior de $A\cup B$ es menor o igual que $m$.

No cites una fórmula conocida para uniones: deriva la igualdad desde las definiciones y el principio del ínfimo ya obtenido en §3.3.

[]{#MA-EX-ANM-01-003-013}

### 13. Trasladar un ínfimo abriendo la caja negra

Sea $A\subseteq\mathbb R$ no vacío y acotado inferiormente, y sea $c\in\mathbb R$. Define

$$
A+c=\{a+c:a\in A\}.
$$

Demuestra

$$
\inf(A+c)=\inf A+c,
$$

pero con la siguiente restricción de trazabilidad:

- no puedes invocar el principio del ínfimo como una caja negra;
- debes abrir su demostración y usar el **principio del supremo exactamente una vez**, aplicado a $-A$;
- después de obtener $s=\sup(-A)$ y $i=-s$, todo el resto debe probarse directamente mediante orden y álgebra.

En particular:

1. verifica las hipótesis sobre $-A$;
2. señala el único `Paso de completitud`;
3. demuestra que $i=\inf A$;
4. demuestra directamente que $i+c$ es la mayor cota inferior de $A+c$;
5. explica por qué no fue necesario gastar completitud una segunda vez para $A+c$.

[]{#MA-EX-ANM-01-003-014}

### 14. Una transformación afín decreciente intercambia las fronteras

Sea $A\subseteq\mathbb R$ no vacío y acotado tanto superior como inferiormente. Sean

$$
\lambda<0,
\qquad
c\in\mathbb R,
$$

y define

$$
\lambda A+c=\{\lambda a+c:a\in A\}.
$$

Demuestra las dos identidades

$$
\boxed{
\sup(\lambda A+c)=\lambda\inf A+c,
}
$$

y

$$
\boxed{
\inf(\lambda A+c)=\lambda\sup A+c.
}
$$

Tu prueba debe:

1. justificar la existencia de $\sup A$ e $\inf A$ a partir de §3.2–§3.3;
2. demostrar directamente que $\lambda\inf A+c$ es cota superior del conjunto transformado y es menor o igual que toda otra cota superior;
3. demostrar de manera dual la segunda identidad;
4. indicar en qué pasos se invierte el sentido de las desigualdades por ser $\lambda<0$;
5. explicar conceptualmente por qué una transformación afín **decreciente** intercambia supremo e ínfimo, mientras que una traslación no los intercambia.

No uses propiedad arquimediana, sucesiones ni resultados de §3.4 o posteriores.

## §3.4. Una consecuencia decisiva: la propiedad arquimediana

[]{#MA-EX-ANM-01-003-015}

### 15. Un paso positivo repetido supera cualquier barrera

Sean

$$
h>0,
\qquad
M\in\mathbb R.
$$

Demuestra que existe $n\in\mathbb N$ tal que

$$
nh>M.
$$

Tu prueba debe:

1. identificar el número real al que conviene aplicar la propiedad arquimediana;
2. explicar por qué multiplicar la desigualdad obtenida por $h$ no cambia su sentido;
3. distinguir el uso **directo** de completitud del uso **indirecto** de una consecuencia ya demostrada de completitud;
4. explicar por qué el resultado sigue siendo válido aunque $M<0$.

No vuelvas a demostrar desde cero la propiedad arquimediana: úsala como el resultado ya obtenido en §3.4.

[]{#MA-EX-ANM-01-003-016}

### 16. Construir una malla finita más fina que una tolerancia

Sean $a,b\in\mathbb R$ con $a<b$ y sea $\varepsilon>0$.

Demuestra que existe $N\in\mathbb N_{>0}$ tal que, al definir

$$
x_k=a+k\frac{b-a}{N},
\qquad
k=0,1,\dots,N,
$$

se cumple

$$
x_0=a,
\qquad
x_N=b,
$$

y, para cada $k=0,1,\dots,N-1$,

$$
0<x_{k+1}-x_k<\varepsilon.
$$

La demostración debe justificar explícitamente:

1. por qué $(b-a)/\varepsilon$ es un real positivo;
2. cómo elegir $N$ mediante arquimedianidad;
3. por qué esa elección implica $(b-a)/N<\varepsilon$;
4. por qué la construcción usa sólo una familia **finita** de puntos y no necesita sucesiones ni límites.

No uses resultados de §3.5 o posteriores.

[]{#MA-EX-ANM-01-003-017}

### 17. Abrir toda la cadena: de SUP a una escala $L/N<\varepsilon$

Sean

$$
L>0,
\qquad
\varepsilon>0.
$$

Partiendo del **principio del supremo** y sin citar la propiedad arquimediana como una caja negra, demuestra que existe $N\in\mathbb N_{>0}$ tal que

$$
\frac{L}{N}<\varepsilon.
$$

Organiza la prueba en dos capas.

**Capa A — obtener arquimedianidad desde completitud.** Supón por contradicción que $\mathbb N$ está acotado superiormente, usa exactamente una vez el principio del supremo para producir $s=\sup\mathbb N$ y completa la contradicción mediante $s-1$ y $n+1$.

**Capa B — producir la escala.** Aplica el resultado de la capa A a $L/\varepsilon$ y deduce la desigualdad requerida.

Al final clasifica cada paso como:

- uso directo de completitud;
- orden y aritmética;
- uso posterior de un resultado ya derivado.

La respuesta debe dejar visible por qué la existencia de $N$ depende estructuralmente de completitud aunque la desigualdad final no invoque de nuevo el supremo.

[]{#MA-EX-ANM-01-003-018}

### 18. «No tiene máximo» no significa «no está acotado»

Un estudiante propone esta prueba de la propiedad arquimediana:

> Los naturales no tienen máximo, porque para cada $n\in\mathbb N$ también $n+1\in\mathbb N$ y $n+1>n$. Todo conjunto sin máximo es no acotado superiormente. Por tanto, $\mathbb N$ no está acotado superiormente y no necesitamos completitud.

Diagnostica el argumento.

1. Identifica exactamente la afirmación falsa.
2. Da un subconjunto no vacío de $\mathbb R$ que esté acotado superiormente y no tenga máximo.
3. Explica por qué $n+1>n$ sólo demuestra que $\mathbb N$ no tiene máximo, pero por sí solo no excluye una cota superior no alcanzada.
4. Repara la prueba suponiendo que $\mathbb N$ está acotado superiormente y señalando el punto exacto donde el principio del supremo elimina la posibilidad de una barrera no alcanzada.
5. Explica por qué la prueba reparada no contradice el contraejemplo del apartado 2.

[]{#MA-EX-ANM-01-003-019}

### 19. Arquimediano no implica completo

Usa $\mathbb Q$ para refutar la conversa

$$
\text{arquimediano}
\Longrightarrow
\text{completo}.
$$

La demostración debe ser autosuficiente en los siguientes puntos:

1. demuestra directamente que para todo $q\in\mathbb Q$ existe $n\in\mathbb N$ con $n>q$;
2. deduce también que para todo $\varepsilon\in\mathbb Q$ con $\varepsilon>0$ existe $n\in\mathbb N_{>0}$ tal que
   $$
   \frac1n<\varepsilon;
   $$
3. recuerda el conjunto
   $$
   S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}
   $$
   y usa el ejercicio 3 para justificar que es no vacío, está acotado superiormente en $\mathbb Q$ y no posee supremo racional;
4. concluye con una separación lógica explícita entre
   $$
   \text{completitud}\Longrightarrow\text{arquimedianidad}
   $$
   y la conversa, que es falsa.

No identifiques el hueco de $S_2$ con ningún número real concreto: utiliza únicamente el fallo interno del supremo racional ya demostrado.

## §3.5. Intervalos encajados: conservar un punto al refinar

[]{#MA-EX-ANM-01-003-020}

### 20. Antes de aplicar el teorema de intervalos encajados

Para cada una de las siguientes familias, decide si el **teorema numerable de intervalos cerrados encajados** de §3.5 puede aplicarse directamente:

$$
I_n=\left[0,1+\frac1n\right],
$$

$$
J_n=\left(0,\frac1n\right],
$$

$$
K_n=[n,n+1],
$$

y

$$
L_n=[-1,1],
\qquad n\in\mathbb N_{>0}.
$$

En cada caso verifica por separado:

1. que cada intervalo sea no vacío;
2. que sea un intervalo **cerrado** de $\mathbb R$;
3. que la familia esté encajada, es decir,
   $$
   I_{n+1}\subseteq I_n
   $$
   con la letra correspondiente;
4. sólo si se cumplen las tres condiciones, escribe la conclusión de existencia autorizada por el teorema.

No calcules todavía la intersección cuando no sea necesario. El objetivo es entrenar la lectura exacta de hipótesis antes de invocar una consecuencia de completitud.

[]{#MA-EX-ANM-01-003-021}

### 21. La misma existencia vista desde los extremos derechos

Sean

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N_{>0},
$$

intervalos cerrados no vacíos tales que

$$
I_{n+1}\subseteq I_n
\qquad\text{para todo }n.
$$

En §3.5 se construyó un punto común usando el supremo de los extremos izquierdos. Da una demostración **dual** usando los extremos derechos.

Define

$$
B=\{b_n:n\in\mathbb N_{>0}\}.
$$

Debes demostrar, en este orden:

1. $B\ne\varnothing$;
2. cada $a_m$ es una cota inferior de $B$;
3. existe
   $$
   y=\inf B;
   $$
4. para cada $n$,
   $$
   a_n\le y\le b_n;
   $$
5. por tanto,
   $$
   y\in\bigcap_{n=1}^{\infty}I_n.
   $$

Localiza el paso que hereda completitud a través del principio del ínfimo de §3.3 y explica por qué las desigualdades posteriores no consumen una nueva aplicación de completitud.

[]{#MA-EX-ANM-01-003-022}

### 22. Describir toda la intersección, no sólo encontrar un punto

Bajo las mismas hipótesis del ejercicio anterior, define

$$
A=\{a_n:n\ge1\},
\qquad
B=\{b_n:n\ge1\},
$$

y escribe

$$
s=\sup A,
\qquad
t=\inf B.
$$

Demuestra que ambos extremos existen y prueba la identidad

$$
\boxed{
\bigcap_{n=1}^{\infty}[a_n,b_n]=[s,t].
}
$$

La prueba debe incluir:

1. la compatibilidad cruzada
   $$
   a_m\le b_n
   \qquad\text{para todos }m,n;
   $$
2. la deducción
   $$
   s\le t;
   $$
3. la inclusión
   $$
   \bigcap_n I_n\subseteq[s,t];
   $$
4. la inclusión recíproca
   $$
   [s,t]\subseteq\bigcap_n I_n.
   $$

No añadas ninguna hipótesis de estrechamiento. El resultado debe dejar abierta la posibilidad de que $s<t$ y la intersección contenga más de un punto.

[]{#MA-EX-ANM-01-003-023}

### 23. Un solo gasto de completitud, tres usos del supremo

Considera la prueba estándar de §3.5 y el conjunto

$$
A=\{a_n:n\ge1\}.
$$

Un lector marca como “uso de completitud” las tres líneas siguientes:

1. existe $x=\sup A$;
2. como $a_n\in A$, entonces $a_n\le x$;
3. como $b_n$ es cota superior de $A$, entonces $x\le b_n$.

Audita esas marcas.

Tu respuesta debe:

1. justificar antes de la línea 1 que $A$ es no vacío y está acotado superiormente;
2. clasificar cada una de las tres líneas como **uso directo de completitud** o **uso de propiedades de un supremo ya existente**;
3. identificar en la línea 2 qué parte de la definición de supremo se usa;
4. identificar en la línea 3 qué parte de la definición de supremo se usa;
5. explicar por qué concluir
   $$
   x\in[a_n,b_n]
   $$
   depende además de que los extremos pertenezcan al intervalo cerrado;
6. escribir la cadena completa de dependencias desde el encajamiento hasta el punto común, marcando exactamente una sola flecha con `COMPLETITUD`.

No introduzcas convergencia, compactidad ni resultados de §3.6 o posteriores.

[]{#MA-EX-ANM-01-003-024}

### 24. Qué ocurre al retirar una hipótesis

Construye y analiza dos familias que muestren que las hipótesis del teorema de §3.5 no son decorativas.

**A. Encajamiento sin cierre.** Considera

$$
J_n=\left(0,\frac1n\right).
$$

Demuestra, sin lenguaje de límites, que cada $J_n$ es no vacío, que

$$
J_{n+1}\subseteq J_n,
$$

pero que

$$
\bigcap_{n=1}^{\infty}J_n=\varnothing.
$$

Señala exactamente qué hipótesis del teorema falla.

**B. Cierre sin encajamiento.** Considera

$$
K_n=[n,n+1].
$$

Demuestra que cada $K_n$ es cerrado y no vacío, pero que la familia no está encajada y que

$$
\bigcap_{n=1}^{\infty}K_n=\varnothing.
$$

Concluye qué muestran estos ejemplos —y qué **no** muestran— acerca del papel de las hipótesis de cierre y encajamiento.

[]{#MA-EX-ANM-01-003-025}

### 25. Transportar intervalos encajados por una transformación afín

Sea

$$
T(x)=\lambda x+c,
\qquad
\lambda\ne0,
$$

y sea

$$
I_n=[a_n,b_n]
$$

una familia de intervalos cerrados no vacíos con

$$
I_{n+1}\subseteq I_n
\qquad\text{para todo }n.
$$

Define

$$
J_n=T(I_n)=\{T(x):x\in I_n\}.
$$

Demuestra que:

1. si $\lambda>0$, entonces
   $$
   J_n=[\lambda a_n+c,\lambda b_n+c];
   $$
2. si $\lambda<0$, entonces
   $$
   J_n=[\lambda b_n+c,\lambda a_n+c];
   $$
3. en ambos casos, cada $J_n$ es cerrado y no vacío y
   $$
   J_{n+1}\subseteq J_n;
   $$
4. como $T$ es biyectiva,
   $$
   T\!\left(\bigcap_{n=1}^{\infty}I_n\right)
   =
   \bigcap_{n=1}^{\infty}T(I_n);
   $$
5. el teorema de §3.5 aplicado a cualquiera de las dos familias da una conclusión equivalente de no vaciedad de la intersección.

Explica conceptualmente por qué una transformación afín biyectiva puede invertir el orden cuando $\lambda<0$ y, sin embargo, preservar el fenómeno de “restricciones cerradas encajadas con punto común”. No uses la hipótesis de estrechamiento de §3.6.

## §3.6. Refinar hasta aislar un único punto

[]{#MA-EX-ANM-01-003-026}

### 26. El estrechamiento controla la cardinalidad sin usar encajamiento

Sea
$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N_{>0},
$$
una familia de intervalos no vacíos. No supongas que está encajada.

Supón únicamente que
$$
\forall\varepsilon>0\;\exists n\in\mathbb N_{>0}:
\quad b_n-a_n<\varepsilon.
$$

Demuestra que
$$
\left|\bigcap_{n=1}^{\infty}I_n\right|\le1.
$$

La prueba debe:

1. comenzar suponiendo que existen dos puntos distintos
   $$
   x,y\in\bigcap_n I_n;
   $$
2. definir
   $$
   \delta=|x-y|>0;
   $$
3. usar la hipótesis de estrechamiento con $\varepsilon=\delta$;
4. demostrar directamente que, si $x,y\in[a_n,b_n]$, entonces
   $$
   |x-y|\le b_n-a_n;
   $$
5. obtener la contradicción
   $$
   \delta\le b_n-a_n<\delta.
   $$

Al final, identifica cuáles de las hipótesis habituales de §3.5 —cierre, encajamiento y completitud— no son necesarias para esta afirmación de **a lo sumo un punto**.

[]{#MA-EX-ANM-01-003-027}

### 27. Desmontar el teorema del singleton en piezas lógicas

Sean
$$
I_n=[a_n,b_n]\ne\varnothing
$$
intervalos cerrados encajados que satisfacen
$$
\forall\varepsilon>0\;\exists n:
\quad b_n-a_n<\varepsilon.
$$

Reconstruye la afirmación
$$
\bigcap_n I_n=\{x\}
$$
como una cadena de dependencias y clasifica cada paso en una de estas categorías:

- **completitud directa**;
- **consecuencia ya demostrada de completitud**;
- **orden / distancia / teoría elemental de conjuntos**;
- **hipótesis adicional de estrechamiento**.

Tu auditoría debe separar explícitamente:

1. la existencia de algún punto común mediante §3.5;
2. el paso de §3.5 donde se produce
   $$
   x=\sup\{a_n:n\ge1\};
   $$
3. la prueba de que dos puntos distintos no pueden sobrevivir al estrechamiento;
4. la inferencia
   $$
   \text{al menos uno}+\text{a lo sumo uno}
   \Longrightarrow
   \text{exactamente uno};
   $$
5. el caso especial en que el estrechamiento se obtiene por bisección y se usa la propiedad arquimediana para elegir un número finito de refinamientos.

Dibuja al final, en texto matemático, dos rutas de dependencia: una para **existencia** y otra para **unicidad**, y explica por qué no deben fusionarse en una sola apelación vaga a “completitud”.

[]{#MA-EX-ANM-01-003-028}

### 28. «Se hace cada vez más pequeño» no es todavía una prueba

Un estudiante parte de un intervalo de ancho $L>0$, lo biseca repetidamente y escribe:

> Después de $k$ bisecciones el ancho es $L/2^k$. Como cada vez es más pequeño, para cualquier $\varepsilon>0$ llegará un momento en que $L/2^k<\varepsilon$. Por tanto la intersección contiene exactamente un punto.

Diagnostica el argumento.

1. Explica por qué la frase «cada vez es más pequeño» no demuestra por sí sola la afirmación cuantificada
   $$
   \forall\varepsilon>0\;\exists k:
   \quad \frac{L}{2^k}<\varepsilon.
   $$
2. Repara ese paso sin usar límites: parte de la propiedad arquimediana y de
   $$
   2^r\ge r+1
   \qquad(r\ge1)
   $$
   para producir explícitamente un $k$ finito adecuado.
3. Identifica un segundo salto lógico en la frase «por tanto la intersección contiene exactamente un punto»: ¿qué argumento adicional garantiza **existencia**?
4. Separa finalmente qué parte usa arquimedianidad, qué parte hereda completitud de §3.5 y qué parte es la prueba elemental de unicidad.

No escribas $\lim_{k\to\infty}L/2^k$ ni cites resultados sobre sucesiones.

[]{#MA-EX-ANM-01-003-029}

### 29. Estrechamiento arbitrario sin punto común

Considera la familia semiabierta
$$
J_k=\left(0,\frac1{2^k}\right],
\qquad k=0,1,2,\dots.
$$

Demuestra que:

1. cada $J_k$ es no vacío;
2. la familia está encajada:
   $$
   J_{k+1}\subseteq J_k;
   $$
3. para toda $\varepsilon>0$ existe un $k$ finito tal que
   $$
   \frac1{2^k}<\varepsilon;
   $$
4. sin embargo,
   $$
   \bigcap_{k=0}^{\infty}J_k=\varnothing.
   $$

En los apartados 3 y 4 no uses lenguaje de límites. Puedes usar la propiedad arquimediana y la desigualdad elemental $2^r\ge r+1$.

Concluye con precisión qué demuestra este ejemplo acerca de la afirmación
$$
\text{estrechamiento arbitrario}
\Longrightarrow
\text{existencia de un punto común}.
$$

[]{#MA-EX-ANM-01-003-030}

### 30. Refinar en $p$ partes en vez de bisecar

Sea
$$
p\in\mathbb N,
\qquad p\ge2,
$$
y sea
$$
J_0=[a,b],
\qquad a<b,
\qquad L=b-a.
$$

En cada etapa divide el intervalo retenido en $p$ subintervalos cerrados de igual ancho y conserva uno de ellos. Así se obtiene una cadena
$$
J_0\supseteq J_1\supseteq J_2\supseteq\cdots.
$$

Demuestra que:

1. después de $k$ refinamientos,
   $$
   \operatorname{anch}(J_k)=\frac{L}{p^k};
   $$
2. para todo $r\ge1$,
   $$
   p^r\ge2^r\ge r+1;
   $$
3. dado $\varepsilon>0$, la propiedad arquimediana permite elegir un $k$ finito con
   $$
   \frac{L}{p^k}<\varepsilon;
   $$
4. la familia satisface las hipótesis de existencia de §3.5 y la hipótesis de unicidad de §3.6;
5. por tanto existe un único $x\in\mathbb R$ tal que
   $$
   \bigcap_{k=0}^{\infty}J_k=\{x\}.
   $$

Explica qué parte del argumento cambia respecto de la bisección y qué parte permanece idéntica. No uses teoría de convergencia.

[]{#MA-EX-ANM-01-003-031}

### 31. Tres formas de reconocer que el núcleo es un solo punto

Sea
$$
I_n=[a_n,b_n]\ne\varnothing
$$
una familia numerable de intervalos cerrados encajados. Define
$$
A=\{a_n:n\ge1\},
\qquad
B=\{b_n:n\ge1\},
$$
y, usando §3.5,
$$
s=\sup A,
\qquad
t=\inf B.
$$

Demuestra la equivalencia entre las siguientes afirmaciones:

1. **estrechamiento arbitrario**
   $$
   \forall\varepsilon>0\;\exists n:
   \quad b_n-a_n<\varepsilon;
   $$
2. **coincidencia de las barreras**
   $$
   s=t;
   $$
3. **intersección puntual**
   $$
   \bigcap_{n=1}^{\infty}I_n
   \text{ contiene exactamente un punto}.
   $$

Para probar $1\Rightarrow2$, no uses convergencia: demuestra que
$$
0\le t-s\le b_n-a_n
$$
para todo $n$ y aplica el estrechamiento a la tolerancia $t-s$ si fuera positiva.

Para probar $2\Rightarrow1$, usa las caracterizaciones $\varepsilon$ del supremo y del ínfimo de C02: para una tolerancia dada, encuentra índices $m,n$ que acerquen $a_m$ a $s$ y $b_n$ a $t$, y usa el encajamiento con un índice posterior común.

Para relacionar 2 y 3, puedes usar el resultado de §3.5
$$
\bigcap_n I_n=[s,t].
$$

Cierra el ejercicio indicando exactamente dónde se requiere completitud para disponer de $s$ y $t$, y por qué las equivalencias posteriores no constituyen nuevas aplicaciones del principio del supremo.

## §3.7. Tres lenguajes para una recta sin huecos

[]{#MA-EX-ANM-01-003-032}

### 32. El mismo objeto en tres lenguajes

Sea $A\subseteq\mathbb R$ no vacío y acotado superiormente, y sea

$$
U(A)=\{u\in\mathbb R:\forall a\in A,\ a\le u\}.
$$

Traduce la búsqueda de $\sup A$ a los otros dos lenguajes equivalentes de §3.7.

1. En lenguaje **SUP**, escribe las dos propiedades que debe satisfacer un número $s$ para ser $\sup A$.
2. En lenguaje **SEP**, considera las clases $A$ y $U(A)$. Demuestra que un número $c$ las separa,
   $$
   a\le c\le u
   \qquad
   \forall a\in A,\ \forall u\in U(A),
   $$
   si y sólo si $c=\sup A$.
3. En lenguaje **GCI**, considera la familia
   $$
   \mathcal I_A=\{[a,u]:(a,u)\in A\times U(A)\}.
   $$
   Verifica su condición cruzada y demuestra que un punto común $c$ a todos los intervalos de $\mathcal I_A$ existe exactamente cuando existe un separador entre $A$ y $U(A)$.
4. Concluye que, para este conjunto $A$, los tres vocabularios no producen tres objetos distintos: cualquier testigo válido debe ser el mismo real.

Indica qué parte del argumento es una mera **traducción lógica** y qué parte necesita una hipótesis estructural de existencia si todavía no sabemos que el objeto existe.

[]{#MA-EX-ANM-01-003-033}

### 33. De SUP a GCI sin pasar por SEP

Supón válido el principio del supremo **SUP**. Sea

$$
\bigl([a_i,b_i]\bigr)_{i\in I}
$$

una familia no vacía de intervalos cerrados que satisface la condición cruzada

$$
a_i\le b_j
\qquad
\forall i,j\in I.
$$

Demuestra **directamente**, sin invocar SEP como lema intermedio, que

$$
\bigcap_{i\in I}[a_i,b_i]\ne\varnothing.
$$

Tu prueba debe:

1. definir
   $$
   L=\{a_i:i\in I\};
   $$
2. justificar que $L\ne\varnothing$;
3. demostrar que cualquier extremo derecho $b_j$ es una cota superior de $L$;
4. localizar el único `Paso de completitud` al producir
   $$
   s=\sup L;
   $$
5. demostrar para cada $i\in I$ que
   $$
   a_i\le s\le b_i;
   $$
6. concluir que $s$ pertenece a todos los intervalos.

Cierra comparando esta ruta directa con la ruta `SUP ⇒ SEP ⇒ GCI`: ¿qué parte matemática es la misma aunque cambie el vocabulario intermedio?

[]{#MA-EX-ANM-01-003-034}

### 34. «Intervalos encajados» no basta para decir «equivalente»

Un estudiante resume §3.7 así:

> GCI es equivalente a SUP. El teorema de §3.5 también habla de intervalos cerrados y dice que una familia encajada tiene intersección no vacía. Por tanto, el teorema numerable de intervalos encajados de §3.5 es automáticamente equivalente a completitud.

Diagnostica esta conclusión.

1. Escribe con precisión las hipótesis de **GCI**: tipo de familia, conjunto de índices y condición cruzada.
2. Escribe con precisión las hipótesis del teorema numerable encajado de §3.5.
3. Demuestra la dirección que sí está establecida en el capítulo:
   $$
   \mathrm{GCI}
   \Longrightarrow
   \mathrm{NESTED\_INTERVALS}_{\mathbb N}.
   $$
4. Explica por qué esta implicación, por sí sola, no autoriza a invertir la flecha.
5. Señala dos diferencias estructurales que impiden identificar sin prueba ambos enunciados: la generalidad del conjunto de índices y la sustitución de la condición cruzada general por una cadena encajada.
6. Explica por qué la hipótesis de estrechamiento de §3.6 tampoco debe incorporarse al ciclo básico de equivalencias.

La respuesta debe distinguir cuidadosamente **equivalencia demostrada**, **consecuencia** y **especialización**.

[]{#MA-EX-ANM-01-003-035}

### 35. El mismo fallo racional en tres idiomas

Trabaja enteramente dentro de $\mathbb Q$. Sea

$$
A=S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}
$$

y sea

$$
B=U_{\mathbb Q}(A)
$$

el conjunto de cotas superiores racionales de $A$.

Sabemos por el ejercicio 3 que $A$ es no vacío, $B$ es no vacío y $A$ no posee supremo en $\mathbb Q$.

1. Demuestra que
   $$
   a\le b
   \qquad
   \forall a\in A,\ \forall b\in B.
   $$
2. Demuestra que un racional $c$ separa $A$ y $B$ si y sólo si
   $$
   c=\sup_{\mathbb Q}A.
   $$
3. Para cada $(a,b)\in A\times B$, define el intervalo racional
   $$
   [a,b]_{\mathbb Q}=\{q\in\mathbb Q:a\le q\le b\}.
   $$
   Demuestra que la familia satisface la condición cruzada racional.
4. Demuestra que un racional $c$ pertenece a **todos** esos intervalos si y sólo si separa $A$ y $B$.
5. Concluye que el mismo defecto puede expresarse como:
   $$
   \text{fallo de SUP}
   \Longleftrightarrow
   \text{fallo de SEP}
   \Longleftrightarrow
   \text{fallo de GCI}
   $$
   para esta instancia concreta dentro de $\mathbb Q$.

No nombres la frontera real ausente ni uses la completitud de $\mathbb R$ para resolver el problema.

[]{#MA-EX-ANM-01-003-036}

### 36. De intersecciones por pares a una intersección global

Sea

$$
\bigl([a_i,b_i]\bigr)_{i\in I}
$$

una familia no vacía de intervalos cerrados de $\mathbb R$.

Demuestra que las siguientes condiciones son equivalentes:

1. todos los pares de intervalos se intersectan:
   $$
   [a_i,b_i]\cap[a_j,b_j]\ne\varnothing
   \qquad
   \forall i,j\in I;
   $$
2. se cumple la condición cruzada de GCI:
   $$
   a_i\le b_j
   \qquad
   \forall i,j\in I.
   $$

Después usa **GCI** para deducir

$$
\boxed{
\bigcap_{i\in I}[a_i,b_i]\ne\varnothing.
}
$$

La solución debe separar dos capas:

- la equivalencia «intersección por pares ⇔ condición cruzada», que debe probarse sólo con orden e intervalos;
- el paso de compatibilidad por pares a **un punto común para toda la familia**, que usa la formulación GCI de completitud.

Explica por qué, en esta prueba, el hecho de trabajar en la recta ordenada es esencial para convertir la intersección por pares en desigualdades entre extremos.

[]{#MA-EX-ANM-01-003-037}

### 37. GCI más estrechamiento: unicidad sin numerabilidad ni encajamiento

Sea

$$
\bigl([a_i,b_i]\bigr)_{i\in I}
$$

una familia no vacía de intervalos cerrados de $\mathbb R$ que satisface la condición cruzada

$$
a_i\le b_j
\qquad
\forall i,j\in I.
$$

No supongas que $I$ es numerable ni que la familia está encajada. Supón además la condición cuantitativa

$$
\forall\varepsilon>0\;\exists i\in I:
\quad b_i-a_i<\varepsilon.
$$

Demuestra que existe un único real $x$ tal que

$$
\boxed{
\bigcap_{i\in I}[a_i,b_i]=\{x\}.
}
$$

Organiza la demostración en dos rutas:

1. **existencia:** usa GCI y localiza qué infraestructura de completitud está siendo invocada;
2. **unicidad:** si $x\ne y$ fueran dos puntos comunes, toma
   $$
   \delta=|x-y|>0
   $$
   y usa un intervalo de ancho menor que $\delta$ para obtener una contradicción.

Concluye comparando este resultado con §3.6: determina exactamente qué hipótesis de la versión numerable encajada eran necesarias para **obtener existencia allí**, pero no son necesarias una vez que la existencia es proporcionada directamente por GCI.

## §3.8. Dónde se gasta la completitud

[]{#MA-EX-ANM-01-003-038}

### 38. Auditar una prueba con tres capas de dependencia

Sea

$$
I_n=[a_n,b_n],
\qquad n\in\mathbb N_{>0},
$$

una familia de intervalos cerrados, no vacíos y encajados. Supón además que el estrechamiento se verifica mediante una construcción de refinamiento para la cual, dado todo $\varepsilon>0$, la propiedad arquimediana permite elegir un índice $k$ con

$$
b_k-a_k<\varepsilon.
$$

Queremos justificar que la intersección contiene exactamente un punto.

Audita la siguiente cadena, clasificando cada paso como **elemental**, **uso directo de completitud** o **uso indirecto/heredado de completitud**:

1. del encajamiento se obtiene
   $$
   a_m\le b_n
   \qquad
   \forall m,n;
   $$
2. el conjunto
   $$
   A=\{a_n:n\ge1\}
   $$
   es no vacío y está acotado superiormente;
3. existe
   $$
   x=\sup A;
   $$
4. para todo $n$,
   $$
   a_n\le x\le b_n,
   $$
   y por tanto $x\in I_n$;
5. si $x,y$ son dos puntos comunes distintos, se define
   $$
   \delta=|x-y|>0;
   $$
6. se elige un índice $k$ con
   $$
   b_k-a_k<\delta;
   $$
7. de $x,y\in I_k$ se deduce
   $$
   |x-y|\le b_k-a_k<|x-y|,
   $$
   contradicción.

Tu respuesta debe:

- señalar la **única línea** en la que se invoca directamente el principio del supremo;
- explicar por qué las líneas 1, 2, 4, 5 y 7 no gastan completitud de nuevo;
- explicar por qué la línea 6 puede constituir una dependencia **indirecta** cuando la elección de $k$ usa arquimedianidad;
- dibujar al final un grafo de dependencias que distinga la ruta de **existencia** de la ruta de **unicidad**.

No resumas todo diciendo simplemente «la prueba usa completitud».

[]{#MA-EX-ANM-01-003-039}

### 39. Recompilar la prueba usando separación en lugar de SUP

En §3.5, la existencia de un punto común para una familia numerable de intervalos cerrados encajados se demostró usando

$$
x=\sup\{a_n:n\ge1\}.
$$

Reescribe esa demostración usando como interfaz de completitud únicamente la propiedad de separación **SEP**:

> si $A,B\subseteq\mathbb R$ son no vacíos y
> $$
> a\le b
> \qquad
> \forall a\in A,\ b\in B,
> $$
> entonces existe $c\in\mathbb R$ tal que
> $$
> a\le c\le b
> \qquad
> \forall a\in A,\ b\in B.
> $$

Sea

$$
I_n=[a_n,b_n]
e\varnothing,
\qquad
I_{n+1}\subseteq I_n.
$$

Debes:

1. definir
   $$
   A_L=\{a_n:n\ge1\},
   \qquad
   A_R=\{b_n:n\ge1\};
   $$
2. demostrar que ambos conjuntos son no vacíos;
3. deducir del encajamiento la condición cruzada
   $$
   a_m\le b_n
   \qquad
   \forall m,n;
   $$
4. aplicar **SEP** para producir un real $c$ con
   $$
   a_n\le c\le b_n
   \qquad
   \forall n;
   $$
5. concluir
   $$
   c\in\bigcap_{n=1}^{\infty}I_n;
   $$
6. explicar por qué esta prueba no usa una «segunda» completitud distinta de SUP, sino una interfaz equivalente ya establecida en §3.7;
7. comparar el punto exacto de gasto estructural en la versión con SUP y en la versión con SEP.

No introduzcas supremos ni ínfimos en la prueba recompilada.

[]{#MA-EX-ANM-01-003-040}

### 40. Qué sobrevive sin completitud y qué debe exportar C03

Compara estructuralmente $\mathbb R$ con $\mathbb Q$ usando únicamente los resultados establecidos en C02–C03 y el conjunto

$$
S_2=\{q\in\mathbb Q:0\le q,\ q^2<2\}.
$$

Construye una tabla razonada para las siguientes afirmaciones:

1. se pueden definir cotas, supremos e ínfimos de manera condicional;
2. si un supremo existe, es único;
3. el sistema es denso;
4. el sistema es arquimediano;
5. todo subconjunto no vacío y acotado superiormente posee supremo interno;
6. toda pareja de clases no vacías globalmente ordenadas admite un separador interno;
7. toda familia GCI de intervalos cerrados posee un punto común interno.

Para cada afirmación indica si:

- está disponible tanto en $\mathbb Q$ como en $\mathbb R$;
- está garantizada en $\mathbb R$ por la infraestructura de completitud;
- falla en $\mathbb Q$, usando $S_2$ cuando corresponda.

Después responde estas cuestiones de conexión:

1. ¿por qué densidad y arquimedianidad no bastan para recuperar completitud?
2. ¿qué significa decir que `SUP`, `SEP` y `GCI` son distintas **interfaces** de una misma infraestructura?
3. usando sólo el mapa de dependencias de §3.8, clasifica los papeles futuros de C07, C10 y C23 como:
   - **consumo de una garantía de existencia**,
   - **comparación/reformulación de la noción de completitud**,
   - o ambos si el texto de §3.8 lo justificara;
4. explica por qué esta clasificación no constituye todavía una demostración de ningún teorema de C07, C10 o C23.

Cierra formulando en una sola frase matemática —sin apelar a la imagen informal de una línea continua— qué aporta la completitud de $\mathbb R$.

---
title: "Álgebra de proposiciones y formas normales"
description: "Quinto capítulo del Tomo I de Álgebra para matemáticos: equivalencia lógica, leyes del álgebra proposicional, reemplazo de equivalentes, formas normales disyuntiva y conjuntiva, formas canónicas y estrategias de normalización."
content-id: MA-BCH-0016
content-type: book-chapter
collection: PM-ALG
book-id: MA-BOK-0006
source-id: APM-T1-C05
editorial-id: MA-BCH-APM-01-005
status: published
date-created: 2026-09-12
date-modified: 2026-10-09
areas:
  - algebra
  - fundamentos
  - logica
level: fundamental
topics:
  - equivalencia-logica
  - algebra-proposicional
  - leyes-de-de-morgan
  - distributividad-logica
  - absorcion
  - formas-normales
  - fnd
  - fnc
  - normalizacion
prerequisites:
  - MA-BCH-0015
related:
  - MA-BOK-0006
  - MA-BCH-0012
  - MA-BCH-0013
  - MA-BCH-0014
  - MA-BCH-0015
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

En C4 aprendimos a **leer** una fórmula proposicional. Sabemos localizar su conectivo principal, construir una tabla de verdad, distinguir implicación de bicondicional y reconocer tautologías, contradicciones y contingencias.

Ahora cambia la pregunta.

Supongamos que dos fórmulas producen exactamente la misma columna final en todas las valuaciones. ¿Podemos reemplazar una por la otra? ¿Podemos transformar una fórmula extensa hasta hacer visible una estructura más simple? ¿Podemos llevar cualquier fórmula a una forma estandarizada?

Ése es el paso propiamente algebraico.

> **Transformar una fórmula proposicional no consiste en cambiar símbolos libremente: consiste en sustituir subfórmulas por otras de comportamiento semántico idéntico.**

La disciplina será la misma que en C3: cada paso debe tener una ley, una dirección y un alcance precisos.

***
## 5.1. De la coincidencia semántica a la equivalencia lógica

Consideremos las fórmulas $P\Rightarrow Q$ y $\neg Q\Rightarrow\neg P$. En C4 verificamos mediante tabla que sus columnas finales coinciden.

Cuando dos fórmulas tienen el mismo valor de verdad bajo **toda** valuación de sus variables proposicionales, diremos que son **lógicamente equivalentes**.

Escribiremos

$A\equiv B$.

La expresión $A\equiv B$ no introduce un nuevo conectivo dentro de la fórmula proposicional que estamos analizando. Es una afirmación acerca de dos fórmulas: dice que, semánticamente, se comportan igual en todas las valuaciones.

Esto debe distinguirse de $A\Leftrightarrow B$. El bicondicional es una fórmula y, para una valuación concreta, puede ser verdadero o falso. En cambio, $A\equiv B$ afirma una coincidencia global.

### Criterio por bicondicional

Tenemos un criterio inmediato:

> **Dos fórmulas $A$ y $B$ son lógicamente equivalentes si y sólo si $A\Leftrightarrow B$ es una tautología.**

La razón es directa. El bicondicional es verdadero exactamente cuando sus dos componentes tienen el mismo valor de verdad. Por tanto, será verdadero en todas las valuaciones exactamente cuando $A$ y $B$ coincidan en todas ellas.

### Refutar una equivalencia

Para demostrar $A\equiv B$ por tabla debemos revisar todas las valuaciones relevantes.

Para demostrar que $A\not\equiv B$ basta mucho menos: encontrar **una sola valuación** en la que difieran.

Ese patrón reaparecerá constantemente en matemática: una afirmación universal exige control global; un contraejemplo basta para refutarla.

***
## 5.2. Una equivalencia es una regla de reemplazo

La utilidad algebraica de $A\equiv B$ aparece cuando $A$ no está aislada, sino dentro de una fórmula mayor.

Supongamos que sabemos

$\neg\neg P\equiv P$.

Entonces, dentro de

$(Q\lor\neg\neg P)\land R$

podemos reemplazar únicamente la subfórmula $\neg\neg P$ por $P$ y obtener

$(Q\lor P)\land R$.

No hemos cambiado arbitrariamente el resto de la fórmula.

### Principio de sustitución de equivalentes

> **Si una subfórmula se reemplaza por otra lógicamente equivalente, el valor de verdad de la fórmula completa se conserva bajo toda valuación.**

La intuición es composicional: los conectivos determinan su resultado únicamente a partir de los valores de verdad de sus componentes. Si un componente conserva siempre su valor, la fórmula mayor no puede detectar el reemplazo.

### La forma debe coincidir

Una ley sólo puede aplicarse a una subfórmula que tenga la estructura adecuada.

Saber que $\neg\neg X\equiv X$ no autoriza a borrar dos signos de negación que no formen una doble negación sobre la **misma subfórmula**.

De manera semejante, la ley de absorción que veremos más adelante no se aplica por semejanza visual: debe localizarse exactamente su patrón.

Esta precisión de alcance será indispensable en cadenas largas.

***
## 5.3. Leyes estructurales: identidad, dominación, idempotencia y complemento

Comenzamos con leyes sencillas que eliminan información redundante.

### Identidad

$P\land V\equiv P$ y $P\lor F\equiv P$.

Conjuntar con una verdad segura no añade restricción; disyuntar con una falsedad segura no añade posibilidad.

### Dominación

$P\lor V\equiv V$ y $P\land F\equiv F$.

Una verdad basta para hacer verdadera una disyunción; una falsedad basta para hacer falsa una conjunción.

### Idempotencia

$P\lor P\equiv P$ y $P\land P\equiv P$.

Repetir una condición no cambia su contenido lógico.

### Complemento

$P\lor\neg P\equiv V$ y $P\land\neg P\equiv F$.

La primera es el tercero excluido en este marco bivalente; la segunda expresa que una proposición y su negación no pueden ser simultáneamente verdaderas.

### Doble negación

$\neg\neg P\equiv P$.

Estas leyes parecen elementales, pero en una fórmula extensa su valor es estratégico. Con frecuencia una transformación previa tiene como objetivo **hacer aparecer** un patrón de complemento, idempotencia o dominación.

### Una primera simplificación

Por ejemplo,

$$
(P\land Q)\lor(P\land\neg Q)
\equiv P\land(Q\lor\neg Q)
\equiv P\land V
\equiv P.
$$

La simplificación no estaba visible al comienzo. Fue necesario factorizar $P$ para producir el complemento $Q\lor\neg Q$.

***
## 5.4. Conmutatividad y asociatividad: preparar el terreno

La conjunción y la disyunción son conmutativas:

$P\land Q\equiv Q\land P$,

$P\lor Q\equiv Q\lor P$.

También son asociativas:

$(P\land Q)\land R\equiv P\land(Q\land R)$,

$(P\lor Q)\lor R\equiv P\lor(Q\lor R)$.

Estas leyes rara vez simplifican por sí solas. Su función más importante es **reorganizar** la fórmula para que otra ley pueda actuar.

Consideremos

$(P\lor Q)\lor\neg P$.

Podemos reordenar y reagrupar:

$$
\begin{aligned}
(P\lor Q)\lor\neg P
&\equiv P\lor(Q\lor\neg P) && \text{[asociatividad]}\\
&\equiv P\lor(\neg P\lor Q) && \text{[conmutatividad]}\\
&\equiv (P\lor\neg P)\lor Q && \text{[asociatividad]}\\
&\equiv V\lor Q && \text{[complemento]}\\
&\equiv V. && \text{[dominación]}
\end{aligned}
$$

El paso conceptual importante no es que podamos permutar símbolos, sino que sabemos **para qué** hacerlo.

***
## 5.5. Leyes de De Morgan y control de negaciones

Las leyes de De Morgan son:

$\neg(P\land Q)\equiv\neg P\lor\neg Q$,

$\neg(P\lor Q)\equiv\neg P\land\neg Q$.

Pueden verificarse por tabla de verdad. Pero una vez establecidas, ya no necesitamos reconstruir la tabla cada vez: se convierten en reglas de transformación.

### La negación atraviesa el conectivo y lo cambia

Un modo útil de recordar la estructura —sin sustituir la comprensión— es:

```text
¬ atraviesa ∧  →  ∨
¬ atraviesa ∨  →  ∧
```

Cada componente queda negado.

### Negaciones anidadas

Consideremos

$\neg(P\lor(Q\land\neg R))$.

Aplicamos De Morgan desde afuera hacia adentro:

$$
\begin{aligned}
\neg(P\lor(Q\land\neg R))
&\equiv \neg P\land\neg(Q\land\neg R)\\
&\equiv \neg P\land(\neg Q\lor\neg\neg R)\\
&\equiv \neg P\land(\neg Q\lor R).
\end{aligned}
$$

Al final, cada negación afecta directamente a una proposición atómica. Esa configuración será esencial para las formas normales.

### Error típico

Es falso que

$\neg(P\land Q)\equiv\neg P\land\neg Q$.

Basta la valuación $P=V,Q=F$: la primera fórmula es verdadera y la segunda falsa.

Una ley recordada con el conectivo equivocado deja de ser una equivalencia.

***
## 5.6. Distributividad y factorización lógica

La lógica proposicional posee dos leyes distributivas:

$P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R)$,

$P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R)$.

La primera recuerda de inmediato a la distributividad algebraica ordinaria. La segunda suele resultar menos familiar, porque en aritmética la suma no distribuye sobre el producto. Aquí ambas son válidas.

### Desarrollar y factorizar

Las equivalencias pueden leerse en ambas direcciones.

De izquierda a derecha **desarrollamos**. De derecha a izquierda **factorizamos**.

Por ejemplo,

$(P\land Q)\lor(P\land R)\equiv P\land(Q\lor R)$.

La dirección adecuada depende del objetivo.

- Para obtener una FND puede convenir desarrollar una conjunción sobre una disyunción.
- Para simplificar puede convenir factorizar y hacer visible un complemento o una absorción.
- Para obtener una FNC puede convenir distribuir una disyunción sobre una conjunción.

### Un ejemplo no intuitivo

Para llevar $P\lor(Q\land R)$ a forma conjuntiva:

$P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R)$.

La fórmula resultante es una conjunción de disyunciones: ya tiene la arquitectura básica de una FNC.

***
## 5.7. Absorción y simplificación estratégica

Las leyes de absorción son:

$P\lor(P\land Q)\equiv P$,

$P\land(P\lor Q)\equiv P$.

Podemos justificarlas algebraicamente a partir de leyes anteriores. Por ejemplo:

$$
\begin{aligned}
P\lor(P\land Q)
&\equiv (P\land V)\lor(P\land Q) && \text{[identidad]}\\
&\equiv P\land(V\lor Q) && \text{[distributividad inversa]}\\
&\equiv P\land V && \text{[dominación]}\\
&\equiv P. && \text{[identidad]}
\end{aligned}
$$

### Absorción escondida

En una fórmula larga el patrón puede no aparecer literalmente.

Consideremos

$(Q\land P)\lor P$.

Por conmutatividad,

$(Q\land P)\lor P\equiv(P\land Q)\lor P$,

y por conmutatividad de $\lor$,

$(P\land Q)\lor P\equiv P\lor(P\land Q)\equiv P$.

Aquí reordenar no fue un fin: fue una preparación para reconocer absorción.

***
## 5.8. Eliminar implicaciones y bicondicionales

Las formas normales que estudiaremos se expresarán usando únicamente $\neg$, $\land$ y $\lor$. Por eso necesitamos eliminar $\Rightarrow$ y $\Leftrightarrow$.

### Implicación

La equivalencia fundamental es

$P\Rightarrow Q\equiv\neg P\lor Q$.

Puede verificarse directamente por tabla: ambas fórmulas son falsas sólo cuando $P=V$ y $Q=F$.

La negación de una implicación queda entonces:

$$
\begin{aligned}
\neg(P\Rightarrow Q)
&\equiv\neg(\neg P\lor Q)\\
&\equiv\neg\neg P\land\neg Q\\
&\equiv P\land\neg Q.
\end{aligned}
$$

Esto recupera una idea de C4: un condicional falla exactamente cuando el antecedente es verdadero y el consecuente falso.

### Bicondicional

Podemos usar

$P\Leftrightarrow Q\equiv(P\Rightarrow Q)\land(Q\Rightarrow P)$.

Eliminando las implicaciones:

$P\Leftrightarrow Q\equiv(\neg P\lor Q)\land(\neg Q\lor P)$.

Otra forma útil es

$P\Leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q)$.

La primera forma ya tiene arquitectura de FNC; la segunda, de FND.

### Elegir la expansión según el objetivo

Si buscamos FND, la segunda representación suele ser más conveniente.

Si buscamos FNC, la primera suele ahorrar trabajo.

Ésta es una primera muestra de estrategia: una equivalencia puede ser correcta en varias formas, pero no todas son igualmente útiles para el objetivo presente.

***
## 5.9. Cadenas largas de equivalencias

Una cadena lógica extensa debe leerse como un argumento matemático. Cada enlace afirma que la fórmula de la izquierda puede reemplazarse por la de la derecha sin cambiar el valor de verdad bajo ninguna valuación.

Consideremos

$\neg[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]$.

Queremos simplificarla.

$$
\begin{aligned}
&\neg[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]\\
&\equiv \neg[(\neg P\lor Q)\land(\neg P\lor\neg Q)]
&&\text{[eliminar implicaciones]}\\
&\equiv \neg[\neg P\lor(Q\land\neg Q)]
&&\text{[distributividad inversa]}\\
&\equiv \neg[\neg P\lor F]
&&\text{[complemento]}\\
&\equiv \neg(\neg P)
&&\text{[identidad]}\\
&\equiv P.
&&\text{[doble negación]}
\end{aligned}
$$

La ruta es corta porque reconocimos una factorización decisiva.

### Una ruta más larga también puede ser correcta

Podríamos haber aplicado De Morgan a la negación exterior, eliminado después cada implicación, distribuido y simplificado. El resultado sería el mismo, pero con más pasos.

En este capítulo no buscamos siempre la cadena más corta. Primero queremos una cadena **segura y auditable**. Luego aprenderemos a mejorarla.

### Igualdad de destino, diversidad de rutas

Dos estudiantes pueden producir cadenas distintas y ambas ser correctas. La pregunta editorial no es «¿usó exactamente la ruta modelo?», sino:

1. ¿cada paso es una equivalencia válida?;
2. ¿el alcance de la ley está controlado?;
3. ¿la estrategia llega al objetivo pedido?;
4. ¿la escritura permite auditar el razonamiento?

***
## 5.10. Literales, términos y cláusulas

Para hablar de formas normales necesitamos algunas unidades estructurales.

Un **literal** es una proposición atómica o la negación de una proposición atómica.

Ejemplos: $P$, $\neg P$, $Q$, $\neg R$.

Un **término conjuntivo** es una conjunción de uno o más literales.

Ejemplos:

$P\land\neg Q$,

$P\land Q\land\neg R$.

Una **cláusula disyuntiva** es una disyunción de uno o más literales.

Ejemplos:

$P\lor\neg Q$,

$\neg P\lor Q\lor R$.

Estas definiciones no dicen todavía que una fórmula sea normal. Nos entregan los bloques con los que construiremos FND y FNC.

### Término no significa «verdadero»

Un término conjuntivo puede ser verdadero o falso según la valuación. Lo mismo una cláusula. Los nombres describen **estructura sintáctica**, no valor de verdad.

***
## 5.11. Forma normal disyuntiva

Una fórmula está en **forma normal disyuntiva (FND)** cuando es una disyunción de uno o más términos conjuntivos de literales.

Por ejemplo,

$$(P\land\neg Q)\lor(\neg P\land R)$$

está en FND.

En cambio,

$P\land(Q\lor R)$

no está en FND porque la disyunción aparece dentro de una conjunción.

### Procedimiento por leyes

Para obtener una FND suele funcionar:

1. eliminar $\Leftrightarrow$;
2. eliminar $\Rightarrow$;
3. llevar negaciones hasta los literales;
4. distribuir $\land$ sobre $\lor$;
5. simplificar términos imposibles o redundantes.

Ejemplo:

$$
\begin{aligned}
P\land(Q\lor\neg R)
&\equiv(P\land Q)\lor(P\land\neg R).
\end{aligned}
$$

Ya tenemos una FND.

### FND no significa mínima

La fórmula

$(P\land Q)\lor(P\land\neg Q)$

está en FND, pero además se simplifica a $P$. Por tanto, estar en forma normal no garantiza ser la escritura más corta.

***
## 5.12. Forma normal conjuntiva

Una fórmula está en **forma normal conjuntiva (FNC)** cuando es una conjunción de una o más cláusulas disyuntivas de literales.

Por ejemplo,

$$(P\lor\neg Q)\land(\neg P\lor R)$$

está en FNC.

La fórmula

$P\lor(Q\land R)$

no está en FNC, pero distributividad produce

$$(P\lor Q)\land(P\lor R),$$

que sí está en FNC.

### Procedimiento por leyes

Para obtener FNC:

1. eliminar $\Leftrightarrow$;
2. eliminar $\Rightarrow$;
3. llevar negaciones hasta los literales;
4. distribuir $\lor$ sobre $\land$;
5. simplificar cláusulas tautológicas o redundantes cuando sea útil.

### Dos arquitecturas para una misma fórmula

Una fórmula puede tener una FND y una FNC equivalentes entre sí y con la fórmula original. No se trata de dos significados distintos, sino de dos representaciones normalizadas del mismo comportamiento semántico.

***
## 5.13. Formas normales canónicas desde tablas de verdad

Las transformaciones algebraicas pueden requerir ingenio. La tabla de verdad ofrece, en cambio, un procedimiento universal.

### FND canónica: mirar las filas verdaderas

Para cada fila donde una fórmula $F$ sea verdadera construimos un término que sea verdadero **exactamente en esa fila**.

Si una fila tiene

$P=V,Q=F,R=V$,

el término correspondiente es

$P\land\neg Q\land R$.

Usamos la variable sin negar cuando vale $V$ y negada cuando vale $F$.

Luego disyuntamos todos los términos correspondientes a filas verdaderas.

### FNC canónica: mirar las filas falsas

Para cada fila donde $F$ sea falsa construimos una cláusula que sea falsa **exactamente en esa fila**.

Si una fila tiene

$P=V,Q=F,R=V$,

queremos una disyunción cuyos tres literales sean falsos en esa fila. Por tanto usamos

$\neg P\lor Q\lor\neg R$.

Aquí el signo se invierte respecto del valor de la fila:

- si una variable vale $V$, usamos su negación;
- si vale $F$, usamos la variable sin negar.

Luego conjuntamos todas las cláusulas correspondientes a filas falsas.

### Teorema de existencia de formas normales

> **Toda fórmula proposicional finita es lógicamente equivalente a alguna FND y a alguna FNC.**

La demostración es constructiva.

- Si la fórmula tiene filas verdaderas, la disyunción de los términos que representan esas filas es verdadera exactamente donde la fórmula original lo es.
- Si tiene filas falsas, la conjunción de las cláusulas que excluyen esas filas es falsa exactamente donde la fórmula original lo es.

Los casos extremos se representan por $F$ para una contradicción y por $V$ para una tautología, o mediante formas equivalentes que contengan literales si se desea conservar variables.

No necesitamos una teoría más avanzada para garantizar la existencia: la propia tabla de verdad construye las formas.

***
### Los casos extremos y las listas vacías

La convención de esta sección admite las constantes $V$ y $F$ como representaciones de los casos extremos. Para entender el procedimiento canónico, interpretaremos una disyunción sin términos como $F$ y una conjunción sin cláusulas como $V$. La primera no ofrece ninguna fila verdadera; la segunda no impone ninguna exclusión.

Con las variables declaradas $P,Q$, hay cuatro filas. Una tautología utiliza todas en su FND canónica:

$(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q)\lor(\neg P\land\neg Q)$.

Su FNC canónica no tiene cláusulas, porque no hay filas falsas, y se representa por $V$. Para una contradicción ocurre lo opuesto: su FND canónica no tiene términos y se representa por $F$; su FNC canónica incluye una cláusula por cada fila:

$(\neg P\lor\neg Q)\land(\neg P\lor Q)\land(P\lor\neg Q)\land(P\lor Q)$.

La conjunción anterior es falsa en todas las filas: cada valuación hace falsa la cláusula construida específicamente para ella. No hay que inventar una fila verdadera para una contradicción ni una fila falsa para una tautología.

| Comportamiento con $P,Q$ declaradas | Términos de la FND canónica | Cláusulas de la FNC canónica |
|---|---:|---:|
| Siempre verdadero | $4$ | $0$: se representa por $V$ |
| Siempre falso | $0$: se representa por $F$ | $4$ |

Una escritura como $P\lor\neg P$ representa una tautología con literales, pero no es la FND canónica relativa a $P,Q$: sus términos no contienen la variable $Q$. Ser equivalente y ser canónica respecto de una lista dada son requisitos diferentes.

**Control.** Para las variables declaradas $P,Q$, ¿puede $P\land\neg P$ ser una FND equivalente a una contradicción sin ser su FND canónica? ¿Qué ocurre con $P\lor\neg P$ como FNC de una tautología?

**Resolución.** Sí. $P\land\neg P$ es un término conjuntivo de literales y, por tanto, una FND de un término; siempre es falso. No es la FND canónica, que no tiene términos verdaderos y se representa por $F$. Análogamente, $P\lor\neg P$ es una FNC de una cláusula siempre verdadera; no es la FNC canónica de la tautología, que no tiene cláusulas y se representa por $V$. Las formas normales ordinarias permiten esas escrituras; el procedimiento canónico selecciona exactamente las filas pertinentes. Si la dificultad estuvo en reconocer un término o una cláusula, vuelve a §§5.10–5.12; si estuvo en seleccionar filas, vuelve al comienzo de §5.13.

***
## 5.14. Normalizar no es minimizar

Una **forma normal** cumple una arquitectura sintáctica determinada.

Una **forma mínima** busca reducir algún criterio de tamaño: número de literales, número de conectivos, número de cláusulas u otro.

Son problemas diferentes.

### Una forma canónica puede crecer mucho

Con $n$ variables existen $2^n$ valuaciones. Si una fórmula es verdadera en muchas filas, su FND canónica puede contener muchos términos, cada uno con $n$ literales.

Una fórmula corta como $P\lor Q$ tiene tabla con tres filas verdaderas. Su FND canónica respecto de las variables $P,Q$ es

$$(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q).$$

Es correcta y canónica, pero mucho más larga que $P\lor Q$.

### Canonizar puede facilitar comparación

La utilidad de una forma canónica no es necesariamente compactar. Es ofrecer una representación sistemática derivada directamente de la semántica.

Dos fórmulas con la misma tabla producirán la misma FND canónica y la misma FNC canónica, salvo reordenamientos triviales.

### Primera advertencia algorítmica

El crecimiento de $2^n$ anuncia un fenómeno que reaparecerá muchas veces: un procedimiento completamente sistemático puede ser costoso. Aquí sólo registramos la idea; no desarrollaremos teoría de complejidad.

***
### Declarar las variables y el criterio de tamaño

La fórmula $P$ no depende del valor de $Q$ ni de $R$. Sin embargo, su forma canónica cambia cuando decidimos que esas variables también formarán parte de la tabla de comparación.

Con sólo $P$ declarada, la FND canónica es $P$. Con $P,Q$ declaradas, las filas verdaderas son $(V,V)$ y $(V,F)$, y la FND canónica pasa a ser $(P\land Q)\lor(P\land\neg Q)$. Con $P,Q,R$, cada una de esas filas se desdobla según el valor de $R$: aparecen cuatro términos de tres literales. Por distributividad y complemento, todas esas escrituras siguen siendo equivalentes a $P$.

Para comparar tamaños, aquí contaremos **apariciones de literales**, no variables distintas. En $P\land\neg Q$, el literal $P$ cuenta una vez y $\neg Q$ una vez; la negación no añade otra aparición de literal. En dos términos que repiten $P$, se cuentan sus dos apariciones. Los paréntesis no se cuentan.

| Variables declaradas | Filas verdaderas de $P$ | Literales en su FND canónica | Filas falsas de $P$ | Literales en su FNC canónica |
|---|---:|---:|---:|---:|
| $P$ | $1$ | $1$ | $1$ | $1$ |
| $P,Q$ | $2$ | $4$ | $2$ | $4$ |
| $P,Q,R$ | $4$ | $12$ | $4$ | $12$ |

Añadir una variable que la fórmula no utiliza duplica las filas verdaderas y falsas: cada valuación previa se extiende con esa variable verdadera o falsa. No cambia el significado original. La forma canónica describe ahora una tabla más grande.

Antes de decir «esta forma es menor», declara qué comparas: apariciones de literales, términos, cláusulas o conectivos. Una reducción respecto de una escritura concreta no demuestra por sí sola que se haya alcanzado el mínimo entre todas las escrituras posibles.

**Control.** Sin enumerar todos los términos, compara los tamaños canónicos de $Q\lor R$ con las variables declaradas $Q,R$ y con $P,Q,R$.

**Resolución.** Con $Q,R$, hay tres filas verdaderas y una falsa: la FND canónica tiene tres términos y seis apariciones de literales; la FNC canónica tiene una cláusula y dos apariciones. Al añadir $P$, las filas se duplican: seis términos de tres literales, con dieciocho apariciones, y dos cláusulas de tres literales, con seis apariciones. La fórmula compacta $Q\lor R$ sigue teniendo sólo dos apariciones y no depende de $P$. Si confundiste la cantidad de variables con las apariciones, compara §5.10 con el criterio fijado aquí; si omitiste la duplicación de filas, vuelve a §4.11.

***
## 5.15. Estrategias de transformación

Conocer las leyes no basta. Una fórmula extensa puede admitir muchas transformaciones correctas, pero algunas nos alejan del objetivo.

### Estrategia A — normalización sistemática

Si el objetivo es obtener FND o FNC y no vemos un atajo claro:

```text
1. eliminar ↔
2. eliminar →
3. empujar ¬ hasta los literales
4. decidir si buscamos FND o FNC
5. distribuir en la dirección necesaria
6. simplificar
```

Es una estrategia robusta, aunque no siempre corta.

### Estrategia B — simplificación oportunista

Antes de expandir conviene mirar:

- ¿hay un complemento escondido?;
- ¿puedo absorber una parte?;
- ¿puedo factorizar?;
- ¿puedo reagrupar para producir $P\lor\neg P$ o $P\land\neg P$?;
- ¿una expansión va a duplicar innecesariamente grandes subfórmulas?

### Ejemplo

Para

$(P\land Q)\lor(P\land\neg Q)$,

una expansión no ayuda. Factorizar produce inmediatamente

$P\land(Q\lor\neg Q)\equiv P$.

### Verificar por una segunda vía

En problemas importantes puede ser útil comprobar el resultado por tabla de verdad. La tabla no reemplaza la derivación cuando se pide una cadena algebraica, pero puede detectar un error.

Aprender matemática implica también desarrollar controles independientes.

***
### Comparar rutas sin perder el objetivo

Sea $X=Q\lor R$ y consideremos $G=(P\land X)\lor(P\land\neg X)$. Una simplificación local reconoce el bloque repetido completo:

$G\equiv P\land(X\lor\neg X)\equiv P\land V\equiv P$.

Aquí complemento se aplica a $X$ y a su negación, aunque $X$ sea una fórmula compuesta. No se ha negado por separado un símbolo que aparezca dentro del bloque.

Una normalización sistemática trabaja directamente con $Q,R$:

$$
\begin{aligned}
G
&\equiv (P\land(Q\lor R))\lor(P\land(\neg Q\land\neg R)) &&\text{[De Morgan]}\\
&\equiv(P\land Q)\lor(P\land R)\lor(P\land\neg Q\land\neg R) &&\text{[distributividad]}.
\end{aligned}
$$

Esta última escritura es una FND equivalente, pero no canónica respecto de $P,Q,R$: sus dos primeros términos no incluyen todas las variables. Para obtener la FND canónica de $P$ en esas variables habría que desdoblarlos y conservar exactamente las cuatro filas con $P=V$.

El control semántico de ambas rutas puede hacerse separando los valores de $P$. Si $P=F$, todos los términos de $G$ son falsos. Si $P=V$, una de $X,\neg X$ es verdadera y $G$ es verdadero. Por eso $G$ siempre comparte el valor de $P$. La ruta local exhibe una ley útil; la sistemática produce la arquitectura solicitada; la canónica enumera filas. Elige la ruta según lo que necesites entregar.

**Control.** Simplifica $G\Rightarrow R$ sin expandir primero todo $G$. Da una FNC y comprueba la equivalencia por los casos que podrían hacer falso al condicional.

**Resolución.** Como $G\equiv P$, podemos reemplazar el antecedente completo y obtener $P\Rightarrow R\equiv\neg P\lor R$. Una sola cláusula constituye una FNC. El original sólo es falso cuando $G=V,R=F$; como $G$ y $P$ coinciden en toda valuación, eso ocurre exactamente cuando $P=V,R=F$, la misma combinación que hace falsa a $\neg P\lor R$. El valor de $Q$ no altera el resultado. Si aplicaste una ley a símbolos dispersos, vuelve a §5.2; si no identificaste el antecedente, vuelve a §4.10.

***
## 5.16. Cierre — protocolo de transformación proposicional

Ante una fórmula extensa, preguntaremos:

1. **¿Qué quiero obtener?** ¿Simplificar, demostrar equivalencia, producir FND o FNC?
2. **¿Cuál es el conectivo principal?**
3. **¿Hay $\Rightarrow$ o $\Leftrightarrow$ que convenga eliminar?**
4. **¿Las negaciones afectan ya sólo a literales?**
5. **¿Puedo reordenar o reagrupar para hacer visible una ley?**
6. **¿Hay complementos, idempotencias, dominaciones o absorciones?**
7. **¿Conviene distribuir o factorizar?**
8. **¿Cada paso es una equivalencia y no sólo una implicación?**
9. **¿La forma final cumple realmente la estructura pedida?**
10. **¿Puedo verificar el resultado mediante una segunda estrategia?**

La nueva competencia puede formularse así:

> **Transformar proposicionalmente es diseñar una cadena de sustituciones equivalentes, controlando estructura, alcance y objetivo.**

C4 enseñó a leer la verdad de una fórmula. C5 enseña a transformar su forma sin cambiar esa verdad.

***
# Ejercicios

Todos los ejercicios son originales para *Álgebra para matemáticos* y han sido calibrados con el corpus rector del capítulo. En las cadenas de equivalencias, justifica los pasos sustantivos.

## A. Reconocer equivalencia y no equivalencia


**1.** Mediante tabla de verdad, decide si $P\Rightarrow Q\equiv\neg P\lor Q$.


**2.** Decide si $P\land Q\equiv P\lor Q$. Si no lo son, da una valuación que lo muestre.


**3.** Explica la diferencia entre escribir $P\Leftrightarrow Q$ y escribir $P\equiv Q$.


**4.** Verifica por tabla que $P\Rightarrow Q\equiv\neg Q\Rightarrow\neg P$.


**5.** Decide si $P\Rightarrow Q\equiv Q\Rightarrow P$ y produce una contra-valuación si falla.


**6.** Demuestra que $A\equiv B$ si y sólo si $A\Leftrightarrow B$ es tautología.

## B. Leyes básicas


**7.** Simplifica $P\land V$.


**8.** Simplifica $P\lor F$.


**9.** Simplifica $(P\lor P)\land Q$.


**10.** Simplifica $P\lor\neg P$ y clasifica el resultado.


**11.** Simplifica $P\land\neg P$ y clasifica el resultado.


**12.** Simplifica $\neg\neg(P\lor Q)$.

## C. Reordenar y reagrupar estratégicamente


**13.** Simplifica $(P\lor Q)\lor\neg P$ justificando los reordenamientos.


**14.** Simplifica $(P\land Q)\land P$.


**15.** Reordena $Q\lor(\neg P\lor P)$ para hacer visible una ley de complemento y simplifica.


**16.** Simplifica $(Q\land\neg P)\land P$.


**17.** Transforma $(P\lor Q)\lor(R\lor\neg Q)$ hasta una forma donde sea inmediata la simplificación.


**18.** Explica por qué conmutatividad y asociatividad suelen funcionar como leyes **preparatorias** y da un ejemplo propio.

## D. De Morgan y negaciones anidadas


**19.** Lleva $\neg(P\land Q)$ a una forma donde las negaciones afecten sólo a literales.


**20.** Lleva $\neg(P\lor(Q\land R))$ a forma con negaciones sólo sobre literales.


**21.** Simplifica $\neg\neg(\neg P\lor Q)$ dejando negaciones sólo sobre literales.


**22.** Lleva $\neg[(P\lor Q)\land(\neg R\lor S)]$ a una forma donde cada negación afecte a una proposición atómica.


**23.** Decide si $\neg(P\land Q)\equiv\neg P\land\neg Q$. Si falla, produce una contra-valuación.


**24.** Transforma $\neg[\neg P\lor\neg(Q\land R)]$ hasta una fórmula sin dobles negaciones y con negaciones sólo sobre literales.

## E. Distributividad y absorción


**25.** Lleva $P\land(Q\lor R)$ a una disyunción de conjunciones.


**26.** Lleva $P\lor(Q\land R)$ a una conjunción de disyunciones.


**27.** Factoriza $(P\land Q)\lor(P\land R)$.


**28.** Simplifica $P\lor(P\land Q)$ demostrando la absorción mediante leyes anteriores.


**29.** Simplifica $(Q\land P)\lor P$ haciendo visible primero el patrón de absorción.


**30.** Simplifica $(P\lor Q)\land(P\lor\neg Q)$ sin tabla de verdad.

## F. Eliminar implicaciones y bicondicionales


**31.** Reescribe $P\Rightarrow Q$ usando sólo $\neg,\lor$.


**32.** Reescribe $\neg(P\Rightarrow Q)$ usando sólo $\neg,\land,\lor$ y simplifica.


**33.** Reescribe $(P\Rightarrow Q)\land R$ sin $\Rightarrow$.


**34.** Reescribe $P\Leftrightarrow Q$ en una FNC que use sólo $\neg,\land,\lor$.


**35.** Reescribe $P\Leftrightarrow Q$ en una FND que use sólo $\neg,\land,\lor$.


**36.** Elimina $\Rightarrow$ y $\Leftrightarrow$ de $(P\Leftrightarrow Q)\Rightarrow R$ sin exigir todavía una forma normal final.

## G. Cadenas largas justificadas


**37.** Simplifica $\neg[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]$ mediante una cadena sistemática de transformaciones justificadas y llega a una sola literal. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**38.** Demuestra por equivalencias, mediante una cadena de transformaciones justificadas, que $[(P\Rightarrow Q)\land(Q\Rightarrow R)\land P]\Rightarrow R$ es una tautología. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**39.** Demuestra que $\neg(P\Leftrightarrow Q)\equiv(P\land\neg Q)\lor(\neg P\land Q)$ mediante transformaciones explícitas y justificadas, eliminando conectivos paso a paso. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**40.** Simplifica $[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]$ mediante transformaciones explícitas y justificadas y clasifica la fórmula final. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**41.** Simplifica $(P\Rightarrow Q)\land(P\Rightarrow\neg Q)$ hasta una fórmula con una sola variable proposicional.


**42.** Lleva $\neg[(P\Rightarrow Q)\lor(R\Rightarrow P)]$ mediante una cadena de transformaciones justificadas a una fórmula que use sólo literales, $\land$ y $\lor$, y simplifica todo lo posible. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**43.** Demuestra que $(P\Rightarrow(Q\land R))\equiv(P\Rightarrow Q)\land(P\Rightarrow R)$ mediante una cadena de equivalencias.


**44.** Encuentra dos rutas distintas para simplificar $(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q)$: una por factorización estratégica y otra mediante una expansión o reagrupación diferente. Compara las longitudes.

## H. Diagnóstico de derivaciones


**45.** Encuentra el primer paso inválido:

$$
\neg(P\land Q)\equiv\neg P\land\neg Q\equiv\neg(Q\land P).
$$


**46.** Un estudiante escribe $P\lor(Q\land R)\equiv(P\lor Q)\land R$. Diagnostica la ley mal aplicada y corrige el paso.


**47.** Encuentra el primer paso inválido:

$$
P\Rightarrow Q\equiv P\lor Q\equiv Q\lor P.
$$


**48.** Un estudiante simplifica $P\lor(P\land Q)$ como $(P\lor P)\land Q\equiv P\land Q$. Localiza el error y repara la derivación.


**49.** Un estudiante afirma que $(P\land Q)\lor(\neg P\land Q)\equiv P\lor\neg P\land Q$. Explica el problema de estructura/paréntesis y produce una derivación correcta.


**50.** En una supuesta cadena de equivalencias aparece el paso $P\Rightarrow Q\to\neg P\lor Q$, escrito con una flecha de implicación entre fórmulas de la cadena. Explica por qué esa notación no expresa correctamente lo que se necesita en una cadena de equivalencias.

## I. Forma normal disyuntiva


**51.** Decide si $(P\land\neg Q)\lor(R\land Q)$ está en FND y justifica por definición.


**52.** Decide si $P\land(Q\lor R)$ está en FND. Si no, conviértela a FND.


**53.** Obtén una FND de $P\land(Q\Rightarrow R)$.


**54.** Obtén una FND de $\neg(P\Rightarrow Q)$.


**55.** Obtén una FND de $P\Leftrightarrow Q$.


**56.** Lleva $(P\lor Q)\land R$ a FND y verifica que cada término final sea una conjunción de literales.

## J. Forma normal conjuntiva


**57.** Decide si $(P\lor\neg Q)\land(R\lor Q)$ está en FNC y justifica.


**58.** Decide si $P\lor(Q\land R)$ está en FNC. Si no, conviértela a FNC.


**59.** Obtén una FNC de $P\Rightarrow(Q\land R)$.


**60.** Obtén una FNC de $\neg(P\land Q)$.


**61.** Obtén una FNC de $P\Leftrightarrow Q$.


**62.** Lleva $(P\land Q)\lor R$ a FNC y verifica la arquitectura final.

## K. Formas canónicas desde tablas


**63.** Construye la FND canónica de $P\lor Q$ a partir de sus filas verdaderas.


**64.** Construye la FNC canónica de $P\land Q$ a partir de sus filas falsas.


**65.** Una fórmula $F(P,Q)$ es verdadera sólo en las filas $(V,F)$ y $(F,V)$. Construye su FND canónica.


**66.** Para la misma fórmula del ejercicio 65, construye su FNC canónica.


**67.** La fórmula $G(P,Q,R)$ es falsa únicamente en la fila $(V,F,V)$. Construye su FNC canónica.


**68.** Explica constructivamente por qué toda fórmula proposicional finita admite FND y FNC.

## L. Síntesis y transferencia


**69.** Sin que se indique el método, simplifica y clasifica

$$
[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]\Rightarrow\neg P.
$$


**70.** Construye una fórmula en FND que sea verdadera exactamente cuando **exactamente una** de $P,Q,R$ sea verdadera.


**71.** Construye una FNC que sea falsa exactamente cuando $P=V,Q=F,R=V$, y explica por qué una sola cláusula basta.


**72.** Compara dos estrategias para estudiar

$$
(P\Leftrightarrow Q)\land(Q\Leftrightarrow R).
$$

Una debe partir de equivalencias algebraicas y otra de la tabla de verdad. Explica qué revela mejor cada método y construye una FND razonable de la fórmula.

## M. Problemas avanzados tipo prueba


**73.** **Nivel E — prueba algebraica larga.** Demuestra, sin tabla de verdad, la **ley de consenso**
$$
(P\land Q)\lor(\neg P\land R)\lor(Q\land R)
\equiv
(P\land Q)\lor(\neg P\land R).
$$
La demostración debe hacer explícito por qué el término $Q\land R$ es redundante y contener una cadena suficientemente detallada de equivalencias justificadas.


**74.** **Nivel E — resolución proposicional.** Demuestra algebraicamente que
$$
[(P\lor Q)\land(\neg P\lor R)]\Rightarrow(Q\lor R)
$$
es una tautología. No uses una tabla de verdad como método principal: elimina primero la implicación y lleva la fórmula, mediante equivalencias, hasta $V$.


**75.** **Nivel F — formas normales y reducción.** Sea $M(P,Q,R)$ la fórmula que debe ser verdadera exactamente cuando **al menos dos** de $P,Q,R$ son verdaderas.

(a) Construye la FND canónica de $M$.  
(b) Obtén y demuestra una FND reducida.  
(c) Construye la FNC canónica de $M$.  
(d) Obtén y demuestra una FNC reducida.  
(e) Demuestra algebraicamente, sin tabla, que tus formas reducidas FND y FNC son equivalentes.


**76.** **Nivel F — normalización completa.** Simplifica mediante una cadena de transformaciones justificadas
$$
H=\neg[(P\Leftrightarrow Q)\Rightarrow(R\lor\neg P)].
$$
Elimina primero $\Rightarrow$ y $\Leftrightarrow$, empuja todas las negaciones hasta literales y simplifica hasta una conjunción mínima. Explica por qué la forma final puede leerse simultáneamente como FND y como FNC. Después compara con una ruta más económica y explica qué justificaciones has comprimido.


**77.** **Nivel F — ciclo de implicaciones.** Considera
$$
G=(P\Rightarrow Q)\land(Q\Rightarrow R)\land(R\Rightarrow P).
$$

(a) Obtén una FNC inmediata eliminando las implicaciones.  
(b) Deriva algebraicamente una FND reducida.  
(c) Determina exactamente qué valuaciones satisfacen $G$.  
(d) Explica por qué $G$ expresa que $P,Q,R$ deben compartir valor de verdad.


**78.** **Nivel G — teorema de cancelación booleana.** Sean $A,B,C$ fórmulas cualesquiera. Demuestra que si
$$
A\land C\equiv B\land C
\qquad\text{y}\qquad
A\lor C\equiv B\lor C,
$$
entonces necesariamente $A\equiv B$.

Da dos demostraciones: una por valuaciones, separando los casos $C=V$ y $C=F$, y otra puramente algebraica. Finalmente muestra, con contraejemplos, que ninguna de las dos hipótesis por separado basta.


**79.** **Nivel G — cuatro variables y dependencia estructural.** Sea
$$
H=(P\Leftrightarrow Q)\land(Q\Leftrightarrow\neg R)\land(R\Leftrightarrow S).
$$

(a) Sin construir una tabla completa de dieciséis filas, determina todas las valuaciones que satisfacen $H$.  
(b) Construye la FND canónica.  
(c) Obtén una FNC compacta eliminando los bicondicionales.  
(d) Justifica rigurosamente que las dos formas obtenidas son equivalentes a $H$.


**80.** **Nivel G — síntesis tipo prueba.** Demuestra que
$$
[(P\Rightarrow Q)\land(Q\Rightarrow R)\land(R\Rightarrow S)]
\Rightarrow
(P\Rightarrow S)
$$
es una tautología de dos maneras independientes:

(a) mediante una cadena algebraica extensa que elimine todas las implicaciones y termine en $V$;  
(b) suponiendo falsa la fórmula y mostrando que las condiciones necesarias conducen a contradicción.

Concluye explicando qué estructura general de las implicaciones está haciendo visible el ejercicio.


## N. Elegir la representación según el objetivo


**81.** Sea $A=(P\land Q)\lor(P\land\neg Q)\lor R$, con $P,Q,R$ declaradas. Elige y construye una representación para cada objetivo: a) decidir rápidamente cuándo $A$ es falsa; b) enumerar exactamente todas sus filas verdaderas. Justifica la equivalencia, cuenta las apariciones de literales de ambas representaciones y explica por qué la escritura mayor puede ser la adecuada para el segundo objetivo.


**82.** Para $B=(P\Leftrightarrow Q)\lor R$, obtén una FND y una FNC mediante leyes. Elige cuál hace más visible que $R=V$ basta para satisfacer $B$ y cuál expone los casos que pueden hacerla falsa. Compara sus apariciones de literales y aclara si esta comparación prueba un mínimo global.


**83.** Considera $C=(P\Rightarrow Q)\land(P\Rightarrow R)$. Construye una FNC útil para auditar cada exigencia por separado y una FND compacta útil para describir cómo satisfacer $C$. Cuenta sus apariciones de literales y determina cuántos términos tendría su FND canónica respecto de $P,Q,R$. Justifica qué gana y qué pierde cada representación.


## O. Variables declaradas y formas canónicas


**84.** Construye las FND y FNC canónicas de $P\Leftrightarrow Q$ primero con $P,Q$ declaradas y después con $P,Q,R$ declaradas, en ese orden. Explica cómo el valor de $R$ cambia las filas y los tamaños sin cambiar la condición sobre $P,Q$. Verifica que las formas ampliadas se reducen a las originales.


**85.** Una fórmula exige únicamente que $Q$ sea falsa. Construye sus FND y FNC canónicas con sólo $Q$ declarada y después con $P,Q$ declaradas. Indica cómo se leen las mismas filas si el orden de columnas se cambia a $Q,P$. ¿Cambiar el orden modifica el significado? ¿Qué tamaños tendrían ambas formas al declarar $P,Q,R$?


**86.** Aplica la convención de constantes y listas vacías a una tautología y una contradicción: a) sin variables declaradas; b) con $P,Q$ declaradas. Indica cuántas valuaciones hay en cada contexto y cuántos términos o cláusulas aporta cada construcción canónica. Explica qué representa un término sin literales y una cláusula sin literales.


## P. Alcance de una sustitución


**87.** Un estudiante pretende eliminar «dos negaciones de $P$» en $D=\neg P\lor\neg(Q\lor\neg P)$ y obtiene $P\lor\neg Q$. Localiza el problema de alcance, simplifica correctamente y produce una valuación que refute el resultado propuesto. Indica a qué subfórmula sí se puede aplicar doble negación durante la reparación.


**88.** En $E=(P\lor Q)\land((P\lor Q)\lor R)$, un estudiante dice «absorbo porque aparece $P$» y concluye $P$. Identifica el bloque que realmente cumple el patrón de absorción, repara la simplificación y refuta la respuesta del estudiante. Explica por qué una subfórmula compuesta puede ocupar el lugar de una letra en una ley.


**89.** Audita el paso $\neg[(P\Rightarrow Q)\lor R]\equiv[(\neg P\Rightarrow\neg Q)\land\neg R]$. Decide qué subfórmula fue negada incorrectamente, da un contraejemplo y repara la fórmula hasta obtener literales. Comprueba la reparación describiendo exactamente la única fila verdadera.


## Q. Diseñar desde la tabla prescrita


**90.** Con las variables declaradas $P,Q,R$, diseña una fórmula verdadera exactamente en las filas $(V,V,F)$, $(V,F,F)$, $(F,V,V)$ y $(F,F,V)$. Construye ambas formas canónicas y una forma compacta. Explica qué variable puede cambiar sin alterar la verdad y justifica la equivalencia sin limitarte a una sola fila.


**91.** Diseña una fórmula verdadera sólo en $(P,Q,R)=(V,F,V)$ y $(V,F,F)$. Construye su FND canónica, una FNC compacta y su FNC canónica completa. Justifica por qué es lícito eliminar una variable en la forma compacta y compara las apariciones de literales de las tres representaciones.


**92.** Para las variables declaradas $P,Q,R,S$, diseña una fórmula sin constantes que no tenga ninguna fila falsa y otra que no tenga ninguna fila verdadera. Justifícalas mediante leyes, describe cómo construir sus formas canónicas sin escribir todos los bloques y calcula sus tamaños en apariciones de literales. Explica cómo interviene la convención de listas vacías.


***
# Soluciones

## A. Reconocer equivalencia y no equivalencia


### 1

Construimos:

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg P$ | $\neg P\lor Q$ |
|---|---|---|---|---|
| V | V | V | F | V |
| V | F | F | F | F |
| F | V | V | V | V |
| F | F | V | V | V |

Las columnas finales coinciden. Por tanto,

$P\Rightarrow Q\equiv\neg P\lor Q$.


### 2

No son equivalentes. Con $P=V,Q=F$,

$P\land Q=F$,

pero $P\lor Q=V$.

Una sola contra-valuación basta para refutar la equivalencia.


### 3

$P\Leftrightarrow Q$ es una **fórmula** cuyo valor depende de la valuación de $P,Q$.

$P\equiv Q$ es una afirmación metalingüística: asegura que $P$ y $Q$ —entendidos aquí como fórmulas— tienen el mismo valor bajo toda valuación. Si $P$ y $Q$ son proposiciones atómicas distintas e independientes, no son lógicamente equivalentes: la valuación $P=V$, $Q=F$ las distingue.


### 4

| $P$ | $Q$ | $P\Rightarrow Q$ | $\neg Q$ | $\neg P$ | $\neg Q\Rightarrow\neg P$ |
|---|---|---|---|---|---|
| V | V | V | F | F | V |
| V | F | F | V | F | F |
| F | V | V | F | V | V |
| F | F | V | V | V | V |

Las columnas relevantes son $V,F,V,V$ en ambos casos. Son equivalentes.


### 5

No. Con $P=V,Q=F$,

$P\Rightarrow Q=F$,

mientras $Q\Rightarrow P=V$ porque su antecedente $Q$ es falso.


### 6

Por definición, $A\equiv B$ significa que para toda valuación $v$, $A$ y $B$ reciben el mismo valor.

El bicondicional $A\Leftrightarrow B$ es verdadero exactamente cuando sus componentes tienen el mismo valor. Por tanto:

- si $A\equiv B$, el bicondicional es verdadero en toda valuación y es tautología;
- si $A\Leftrightarrow B$ es tautología, en toda valuación sus componentes coinciden, luego $A\equiv B$.

## B. Leyes básicas


### 7

$P\land V\equiv P$ por identidad de la conjunción.


### 8

$P\lor F\equiv P$ por identidad de la disyunción.


### 9

$$
(P\lor P)\land Q\equiv P\land Q
$$

por idempotencia de $\lor$.


### 10

$P\lor\neg P\equiv V$ por complemento. Es una tautología.


### 11

$P\land\neg P\equiv F$ por complemento. Es una contradicción.


### 12

Por doble negación aplicada a la subfórmula completa,

$\neg\neg(P\lor Q)\equiv P\lor Q$.

## C. Reordenar y reagrupar estratégicamente


### 13

$$
\begin{aligned}
(P\lor Q)\lor\neg P
&\equiv P\lor(Q\lor\neg P) && \text{[asociatividad]}\\
&\equiv P\lor(\neg P\lor Q) && \text{[conmutatividad]}\\
&\equiv(P\lor\neg P)\lor Q && \text{[asociatividad]}\\
&\equiv V\lor Q && \text{[complemento]}\\
&\equiv V. && \text{[dominación]}
\end{aligned}
$$


### 14

$$
\begin{aligned}
(P\land Q)\land P
&\equiv P\land(Q\land P)\\
&\equiv P\land(P\land Q)\\
&\equiv(P\land P)\land Q\\
&\equiv P\land Q.
\end{aligned}
$$

Se usaron asociatividad, conmutatividad e idempotencia.


### 15

$$
\begin{aligned}
Q\lor(\neg P\lor P)
&\equiv Q\lor(P\lor\neg P) && \text{[conmutatividad]}\\
&\equiv Q\lor V && \text{[complemento]}\\
&\equiv V. && \text{[dominación]}
\end{aligned}
$$


### 16

$$
\begin{aligned}
(Q\land\neg P)\land P
&\equiv Q\land(\neg P\land P) && \text{[asociatividad]}\\
&\equiv Q\land F && \text{[complemento]}\\
&\equiv F. && \text{[dominación]}
\end{aligned}
$$


### 17

$$
\begin{aligned}
(P\lor Q)\lor(R\lor\neg Q)
&\equiv P\lor Q\lor R\lor\neg Q\\
&\equiv P\lor R\lor(Q\lor\neg Q)\\
&\equiv P\lor R\lor V\\
&\equiv V.
\end{aligned}
$$

Las dos primeras reescrituras condensan asociatividad y conmutatividad.


### 18

Conmutatividad y asociatividad no suelen eliminar conectivos; permiten colocar componentes en una posición útil para otra ley. Por ejemplo,

$Q\lor(\neg P\lor P)$

se reordena como $Q\lor(P\lor\neg P)$ para hacer visible $P\lor\neg P\equiv V$, después de lo cual dominación produce $V$.

## D. De Morgan y negaciones anidadas


### 19

$\neg(P\land Q)\equiv\neg P\lor\neg Q$.

Las negaciones ya afectan sólo a literales.


### 20

$$
\begin{aligned}
\neg(P\lor(Q\land R))
&\equiv\neg P\land\neg(Q\land R)\\
&\equiv\neg P\land(\neg Q\lor\neg R).
\end{aligned}
$$


### 21

La doble negación afecta a toda la subfórmula:

$\neg\neg(\neg P\lor Q)\equiv\neg P\lor Q$.


### 22

$$
\begin{aligned}
\neg[(P\lor Q)\land(\neg R\lor S)]
&\equiv\neg(P\lor Q)\lor\neg(\neg R\lor S)\\
&\equiv(\neg P\land\neg Q)\lor(\neg\neg R\land\neg S)\\
&\equiv(\neg P\land\neg Q)\lor(R\land\neg S).
\end{aligned}
$$


### 23

No. Con $P=V,Q=F$:

$\neg(P\land Q)=\neg F=V$,

pero $\neg P\land\neg Q=F\land V=F$.

La ley correcta cambia $\land$ por $\lor$.


### 24

$$
\begin{aligned}
\neg[\neg P\lor\neg(Q\land R)]
&\equiv\neg\neg P\land\neg\neg(Q\land R) && \text{[De Morgan]}\\
&\equiv P\land(Q\land R) && \text{[doble negación]}\\
&\equiv P\land Q\land R. && \text{[asociatividad]}
\end{aligned}
$$

## E. Distributividad y absorción


### 25

$P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R)$.


### 26

$P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R)$.


### 27

Por distributividad en sentido inverso,

$(P\land Q)\lor(P\land R)\equiv P\land(Q\lor R)$.


### 28

Una derivación de absorción es:

$$
\begin{aligned}
P\lor(P\land Q)
&\equiv(P\land V)\lor(P\land Q) && \text{[identidad]}\\
&\equiv P\land(V\lor Q) && \text{[distributividad inversa]}\\
&\equiv P\land V && \text{[dominación]}\\
&\equiv P. && \text{[identidad]}
\end{aligned}
$$


### 29

$$
\begin{aligned}
(Q\land P)\lor P
&\equiv(P\land Q)\lor P && \text{[conmutatividad]}\\
&\equiv P\lor(P\land Q) && \text{[conmutatividad]}\\
&\equiv P. && \text{[absorción]}
\end{aligned}
$$


### 30

Usamos la distributividad inversa en la forma $(A\lor B)\land(A\lor C)\equiv A\lor(B\land C)$:

$$
\begin{aligned}
(P\lor Q)\land(P\lor\neg Q)
&\equiv P\lor(Q\land\neg Q)\\
&\equiv P\lor F\\
&\equiv P.
\end{aligned}
$$

## F. Eliminar implicaciones y bicondicionales


### 31

$P\Rightarrow Q\equiv\neg P\lor Q$.


### 32

$$
\begin{aligned}
\neg(P\Rightarrow Q)
&\equiv\neg(\neg P\lor Q)\\
&\equiv\neg\neg P\land\neg Q\\
&\equiv P\land\neg Q.
\end{aligned}
$$


### 33

$(P\Rightarrow Q)\land R\equiv(\neg P\lor Q)\land R$.


### 34

$$
P\Leftrightarrow Q
\equiv(P\Rightarrow Q)\land(Q\Rightarrow P)
\equiv(\neg P\lor Q)\land(\neg Q\lor P).
$$

Ésta es una FNC.


### 35

El bicondicional es verdadero cuando ambos valores coinciden:

$P\Leftrightarrow Q\equiv(P\land Q)\lor(\neg P\land\neg Q)$.

Ésta es una FND.


### 36

$$
\begin{aligned}
(P\Leftrightarrow Q)\Rightarrow R
&\equiv\neg(P\Leftrightarrow Q)\lor R\\
&\equiv\neg[(P\land Q)\lor(\neg P\land\neg Q)]\lor R.
\end{aligned}
$$

Ya no aparecen $\Rightarrow$ ni $\Leftrightarrow$. Si se quisiera continuar hacia forma normal, aplicaríamos De Morgan a la negación exterior.

## G. Cadenas largas justificadas

Las soluciones 37–40 y 42 muestran rutas detalladas. Para compararlas con rutas económicas, en 37 y 40 puede simplificarse cada bloque de dos condicionales antes de desarrollar la negación o la disyunción exterior; en 38 puede justificarse semánticamente que las premisas fuerzan $R$; en 39 puede partirse de la FND del bicondicional y negar sus dos términos; en 42 basta observar que el primer condicional falso exige $P=V$ y el segundo falso exige $P=F$. La vía semántica sirve de control independiente y no sustituye una cadena algebraica cuando ésta se pide. En 76, la identidad $\neg(A\Rightarrow B)\equiv A\land\neg B$ y el bloque $P\land(P\Leftrightarrow Q)\equiv P\land Q$ permiten comprimir la ruta, conservando De Morgan, eliminación del bicondicional y las absorciones que justifican ese bloque. La comparación debe explicar esas razones, no añadir líneas para alcanzar una cuota.

Rutas económicas de comparación:

- **37.** $\neg[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]\equiv\neg[\neg P\lor(Q\land\neg Q)]\equiv\neg\neg P\equiv P$. Se comprimen eliminación de implicaciones, distributividad inversa, complemento e identidad.
- **38.** El antecedente equivale a $P\land(\neg P\lor Q)\land(\neg Q\lor R)\equiv P\land Q\land R$: distribuir y eliminar los términos con complemento justifica cada reducción. La fórmula completa equivale entonces a $\neg(P\land Q\land R)\lor R\equiv\neg P\lor\neg Q\lor\neg R\lor R\equiv V$. Se comprimen eliminación de implicaciones, las reducciones del antecedente, De Morgan, complemento y dominación.
- **39.** $\neg(P\Leftrightarrow Q)\equiv\neg[(\neg P\lor Q)\land(\neg Q\lor P)]\equiv(P\land\neg Q)\lor(Q\land\neg P)$. Se comprimen eliminación del bicondicional, De Morgan y dobles negaciones; conmutatividad da la forma pedida.
- **40.** Sus bloques equivalen respectivamente a $\neg P$ y $P$, por eliminación de implicaciones, distributividad inversa y complemento. Su disyunción se reduce a $\neg P\lor P\equiv V$.
- **42.** $\neg[(P\Rightarrow Q)\lor(R\Rightarrow P)]\equiv(P\land\neg Q)\land(R\land\neg P)\equiv F$. Se comprimen De Morgan, negación de cada implicación, reagrupación para exponer $P\land\neg P$ y dominación.
- **76.** La fórmula equivale a $(P\Leftrightarrow Q)\land P\land\neg R\equiv P\land Q\land\neg R$. Para justificar el bloque comprimido, expandir el bicondicional en FND da $P\land[(P\land Q)\lor(\neg P\land\neg Q)]\equiv(P\land Q)\lor F\equiv P\land Q$, por distributividad, idempotencia y complemento. La otra compresión usa negación de implicación y De Morgan sobre $R\lor\neg P$.

Estas rutas conservan las razones de las cadenas detalladas siguientes; su menor extensión no elimina ninguna condición de equivalencia.


### 37

Aplicamos deliberadamente una sola transformación sustantiva por línea:

$$
\begin{aligned}
&\neg[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]\\
&\equiv \neg(P\Rightarrow Q)\lor\neg(P\Rightarrow\neg Q)
&&\text{[De Morgan]}\\
&\equiv \neg(\neg P\lor Q)\lor\neg(P\Rightarrow\neg Q)
&&\text{[eliminar la primera implicación]}\\
&\equiv \neg(\neg P\lor Q)\lor\neg(\neg P\lor\neg Q)
&&\text{[eliminar la segunda implicación]}\\
&\equiv (\neg\neg P\land\neg Q)\lor\neg(\neg P\lor\neg Q)
&&\text{[De Morgan, primer término]}\\
&\equiv (\neg\neg P\land\neg Q)\lor(\neg\neg P\land\neg\neg Q)
&&\text{[De Morgan, segundo término]}\\
&\equiv (P\land\neg Q)\lor(\neg\neg P\land\neg\neg Q)
&&\text{[doble negación]}\\
&\equiv (P\land\neg Q)\lor(P\land Q)
&&\text{[doble negación]}\\
&\equiv P\land(\neg Q\lor Q)
&&\text{[distributividad inversa]}\\
&\equiv P\land V
&&\text{[complemento]}\\
&\equiv P.
&&\text{[identidad]}
\end{aligned}
$$

La ruta sistemática tiene diez transformaciones. Una ruta estratégica más corta sería factorizar antes de negar; ambas son correctas, pero ésta hace visible la disciplina de sustitución local.


### 38

Sea

$F=[(P\Rightarrow Q)\land(Q\Rightarrow R)\land P]\Rightarrow R$.

Eliminamos la implicación exterior y luego las interiores:

$$
\begin{aligned}
F
&\equiv\neg[(P\Rightarrow Q)\land(Q\Rightarrow R)\land P]\lor R\\
&\equiv\neg[(\neg P\lor Q)\land(\neg Q\lor R)\land P]\lor R\\
&\equiv[\neg(\neg P\lor Q)\lor\neg(\neg Q\lor R)\lor\neg P]\lor R\\
&\equiv[(P\land\neg Q)\lor(Q\land\neg R)\lor\neg P]\lor R\\
&\equiv(\neg P\lor(P\land\neg Q))\lor(Q\land\neg R)\lor R\\
&\equiv(\neg P\lor\neg Q)\lor(Q\land\neg R)\lor R\\
&\equiv\neg P\lor[\neg Q\lor(Q\land\neg R)]\lor R\\
&\equiv\neg P\lor(\neg Q\lor\neg R)\lor R\\
&\equiv\neg P\lor\neg Q\lor(\neg R\lor R)\\
&\equiv\neg P\lor\neg Q\lor V\\
&\equiv V.
\end{aligned}
$$

En dos pasos usamos la identidad derivada $A\lor(\neg A\land B)\equiv A\lor B$, que puede verificarse por distributividad y absorción. La conclusión $F\equiv V$ demuestra que la fórmula es tautológica.

**Cómo pensar este problema.** La fórmula expresa transitividad del razonamiento: si $P$ lleva a $Q$, $Q$ lleva a $R$ y además $P$ ocurre, entonces $R$ debe ocurrir. La derivación algebraica confirma esa estructura.


### 39

Partimos de la definición del bicondicional por dos condicionales y reemplazamos una subfórmula por vez:

$$
\begin{aligned}
\neg(P\Leftrightarrow Q)
&\equiv\neg[(P\Rightarrow Q)\land(Q\Rightarrow P)]
&&\text{[bicondicional]}\\
&\equiv\neg(P\Rightarrow Q)\lor\neg(Q\Rightarrow P)
&&\text{[De Morgan]}\\
&\equiv\neg(\neg P\lor Q)\lor\neg(Q\Rightarrow P)
&&\text{[eliminar primera implicación]}\\
&\equiv\neg(\neg P\lor Q)\lor\neg(\neg Q\lor P)
&&\text{[eliminar segunda implicación]}\\
&\equiv(\neg\neg P\land\neg Q)\lor\neg(\neg Q\lor P)
&&\text{[De Morgan]}\\
&\equiv(\neg\neg P\land\neg Q)\lor(\neg\neg Q\land\neg P)
&&\text{[De Morgan]}\\
&\equiv(P\land\neg Q)\lor(\neg\neg Q\land\neg P)
&&\text{[doble negación]}\\
&\equiv(P\land\neg Q)\lor(Q\land\neg P)
&&\text{[doble negación]}\\
&\equiv(P\land\neg Q)\lor(\neg P\land Q).
&&\text{[conmutatividad]}
\end{aligned}
$$

La fórmula final dice exactamente que $P$ y $Q$ tienen valores distintos: uno verdadero y el otro falso.


### 40

Aplicamos los reemplazos de manera local para que la cadena sea auditable:

$$
\begin{aligned}
&[(P\Rightarrow Q)\land(P\Rightarrow\neg Q)]
\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]\\
&\equiv[(\neg P\lor Q)\land(P\Rightarrow\neg Q)]
\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]
&&\text{[eliminar implicación]}\\
&\equiv[(\neg P\lor Q)\land(\neg P\lor\neg Q)]
\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]
&&\text{[eliminar implicación]}\\
&\equiv[\neg P\lor(Q\land\neg Q)]
\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]
&&\text{[distributividad inversa]}\\
&\equiv[\neg P\lor F]
\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]
&&\text{[complemento]}\\
&\equiv\neg P\lor[(\neg P\Rightarrow R)\land(\neg P\Rightarrow\neg R)]
&&\text{[identidad]}\\
&\equiv\neg P\lor[(P\lor R)\land(\neg P\Rightarrow\neg R)]
&&\text{[eliminar implicación]}\\
&\equiv\neg P\lor[(P\lor R)\land(P\lor\neg R)]
&&\text{[eliminar implicación]}\\
&\equiv\neg P\lor[P\lor(R\land\neg R)]
&&\text{[distributividad inversa]}\\
&\equiv\neg P\lor(P\lor F)
&&\text{[complemento]}\\
&\equiv\neg P\lor P
&&\text{[identidad]}\\
&\equiv V.
&&\text{[complemento]}
\end{aligned}
$$

La fórmula es una **tautología**. Estructuralmente, el primer bloque equivale a $\neg P$ y el segundo a $P$; por eso su disyunción cubre todos los casos.


### 41

$$
\begin{aligned}
(P\Rightarrow Q)\land(P\Rightarrow\neg Q)
&\equiv(\neg P\lor Q)\land(\neg P\lor\neg Q)\\
&\equiv\neg P\lor(Q\land\neg Q)\\
&\equiv\neg P\lor F\\
&\equiv\neg P.
\end{aligned}
$$

La fórmula afirma, en efecto, que si $P$ obligara simultáneamente a $Q$ y a $\neg Q$, entonces $P$ no puede ser verdadero.


### 42

Aplicamos una transformación local por línea:

$$
\begin{aligned}
&\neg[(P\Rightarrow Q)\lor(R\Rightarrow P)]\\
&\equiv\neg(P\Rightarrow Q)\land\neg(R\Rightarrow P)
&&\text{[De Morgan]}\\
&\equiv\neg(\neg P\lor Q)\land\neg(R\Rightarrow P)
&&\text{[eliminar primera implicación]}\\
&\equiv\neg(\neg P\lor Q)\land\neg(\neg R\lor P)
&&\text{[eliminar segunda implicación]}\\
&\equiv(\neg\neg P\land\neg Q)\land\neg(\neg R\lor P)
&&\text{[De Morgan]}\\
&\equiv(\neg\neg P\land\neg Q)\land(\neg\neg R\land\neg P)
&&\text{[De Morgan]}\\
&\equiv(P\land\neg Q)\land(\neg\neg R\land\neg P)
&&\text{[doble negación]}\\
&\equiv(P\land\neg Q)\land(R\land\neg P)
&&\text{[doble negación]}\\
&\equiv(P\land\neg P)\land(\neg Q\land R)
&&\text{[conmutatividad y asociatividad]}\\
&\equiv F\land(\neg Q\land R)
&&\text{[complemento]}\\
&\equiv F.
&&\text{[dominación]}
\end{aligned}
$$

La contradicción tiene además una lectura semántica: para que $P\Rightarrow Q$ sea falsa necesitamos $P=V$, mientras para que $R\Rightarrow P$ sea falsa necesitamos $P=F$. Es imposible satisfacer ambas exigencias a la vez.


### 43

$$
\begin{aligned}
P\Rightarrow(Q\land R)
&\equiv\neg P\lor(Q\land R) && \text{[eliminar $\Rightarrow$]}\\
&\equiv(\neg P\lor Q)\land(\neg P\lor R) && \text{[distributividad]}\\
&\equiv(P\Rightarrow Q)\land(P\Rightarrow R). && \text{[reintroducir $\Rightarrow$]}
\end{aligned}
$$

Cada paso es reversible, por lo que tenemos equivalencia.


### 44

**Ruta 1: factorizar respecto de $P$.**

$$
\begin{aligned}
&(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q)\\
&\equiv P\land(Q\lor\neg Q)\lor(\neg P\land Q)\\
&\equiv P\lor(\neg P\land Q)\\
&\equiv(P\lor\neg P)\land(P\lor Q)\\
&\equiv V\land(P\lor Q)\\
&\equiv P\lor Q.
\end{aligned}
$$

**Ruta 2: factorizar respecto de $Q$ los términos primero y tercero.**

Reordenamos:

$$
\begin{aligned}
&(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q)\\
&\equiv[(P\land Q)\lor(\neg P\land Q)]\lor(P\land\neg Q)\\
&\equiv[(P\lor\neg P)\land Q]\lor(P\land\neg Q)\\
&\equiv Q\lor(P\land\neg Q)\\
&\equiv(Q\lor P)\land(Q\lor\neg Q)\\
&\equiv(P\lor Q)\land V\\
&\equiv P\lor Q.
\end{aligned}
$$

Las rutas tienen longitudes semejantes pero hacen visibles estructuras distintas. La primera reconoce una partición por $Q$ dentro del caso $P$; la segunda reconoce una partición por $P$ dentro del caso $Q$.

## H. Diagnóstico de derivaciones


### 45

El primer paso es inválido:

$\neg(P\land Q)\not\equiv\neg P\land\neg Q$.

De Morgan exige cambiar $\land$ por $\lor$:

$\neg(P\land Q)\equiv\neg P\lor\neg Q$.

Por ejemplo, con $P=V,Q=F$, la fórmula correcta vale $V$, mientras $\neg P\land\neg Q$ vale $F$.


### 46

Se aplicó distributividad de forma incompleta. La ley correcta es

$P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R)$.

El factor $P$ debe aparecer en **ambas** cláusulas.


### 47

El primer paso es inválido. La eliminación correcta de la implicación es

$P\Rightarrow Q\equiv\neg P\lor Q$,

no $P\lor Q$.

Con $P=V,Q=F$, el condicional vale $F$ y $P\lor Q$ vale $V$.


### 48

La distribución fue mal aplicada. De $P\lor(P\land Q)$ se obtiene

$$(P\lor P)\land(P\lor Q),$$

no $(P\lor P)\land Q$.

Entonces

$$
(P\lor P)\land(P\lor Q)
\equiv P\land(P\lor Q)
\equiv P
$$

por idempotencia y absorción.


### 49

Sin paréntesis, $P\lor\neg P\land Q$ es ambiguo o depende de una convención de precedencia; además no muestra correctamente la factorización.

La derivación correcta es

$$
\begin{aligned}
(P\land Q)\lor(\neg P\land Q)
&\equiv(P\lor\neg P)\land Q\\
&\equiv V\land Q\\
&\equiv Q.
\end{aligned}
$$


### 50

Una cadena de equivalencias necesita afirmar que cada fórmula puede sustituirse por la siguiente en ambas direcciones semánticamente. El símbolo apropiado es $\equiv$ en el metanivel de la derivación:

$P\Rightarrow Q\equiv\neg P\lor Q$.

Escribir sólo una implicación entre las dos fórmulas afirmaría una relación más débil y no justificaría un reemplazo reversible en una cadena de equivalencias.

## I. Forma normal disyuntiva


### 51

Sí. Es una disyunción de dos términos conjuntivos:

- $P\land\neg Q$;
- $R\land Q$.

Cada componente de esos términos es un literal.


### 52

No está en FND porque contiene una disyunción dentro de una conjunción. Distribuimos:

$P\land(Q\lor R)\equiv(P\land Q)\lor(P\land R)$.

La forma final sí es FND.


### 53

$$
\begin{aligned}
P\land(Q\Rightarrow R)
&\equiv P\land(\neg Q\lor R)\\
&\equiv(P\land\neg Q)\lor(P\land R).
\end{aligned}
$$

Es FND.


### 54

Ya obtuvimos:

$\neg(P\Rightarrow Q)\equiv P\land\neg Q$.

Un único término conjuntivo cuenta como FND.


### 55

Una FND natural es

$(P\land Q)\lor(\neg P\land\neg Q)$.

Cada término representa uno de los dos casos en que $P,Q$ comparten valor de verdad.


### 56

$$
(P\lor Q)\land R
\equiv(P\land R)\lor(Q\land R).
$$

Los dos términos finales son conjunciones de literales, por lo que la fórmula está en FND.

## J. Forma normal conjuntiva


### 57

Sí. Es una conjunción de dos cláusulas disyuntivas:

- $P\lor\neg Q$;
- $R\lor Q$.

Todos sus componentes son literales.


### 58

No está en FNC. Aplicamos distributividad:

$P\lor(Q\land R)\equiv(P\lor Q)\land(P\lor R)$.


### 59

$$
\begin{aligned}
P\Rightarrow(Q\land R)
&\equiv\neg P\lor(Q\land R)\\
&\equiv(\neg P\lor Q)\land(\neg P\lor R).
\end{aligned}
$$

Es FNC.


### 60

Por De Morgan,

$\neg(P\land Q)\equiv\neg P\lor\neg Q$.

Una sola cláusula disyuntiva cuenta como FNC.


### 61

Una FNC inmediata es

$(\neg P\lor Q)\land(\neg Q\lor P)$.

Proviene de $(P\Rightarrow Q)\land(Q\Rightarrow P)$.


### 62

Distribuimos $R$ sobre la conjunción:

$$(P\land Q)\lor R\equiv(P\lor R)\land(Q\lor R).$$

La forma final es una conjunción de dos cláusulas disyuntivas de literales.

## K. Formas canónicas desde tablas


### 63

La tabla de $P\lor Q$ es verdadera en $(V,V)$, $(V,F)$ y $(F,V)$.

Los términos correspondientes son:

- $(V,V)$: $P\land Q$;
- $(V,F)$: $P\land\neg Q$;
- $(F,V)$: $\neg P\land Q$.

Por tanto, la FND canónica es

$$(P\land Q)\lor(P\land\neg Q)\lor(\neg P\land Q).$$

Se simplifica a $P\lor Q$, pero la forma canónica conserva explícitamente cada fila verdadera.


### 64

$P\land Q$ es falsa en $(V,F)$, $(F,V)$ y $(F,F)$.

Construimos una cláusula falsa en cada fila:

- $(V,F)$: $\neg P\lor Q$;
- $(F,V)$: $P\lor\neg Q$;
- $(F,F)$: $P\lor Q$.

La FNC canónica es

$$(\neg P\lor Q)\land(P\lor\neg Q)\land(P\lor Q).$$

Aunque se puede simplificar a $P\land Q$, ésa es la forma canónica obtenida directamente de las filas falsas.


### 65

Las filas verdaderas son $(V,F)$ y $(F,V)$. Por tanto,

$$(P\land\neg Q)\lor(\neg P\land Q).$$

Es la FND canónica del XOR de dos variables.


### 66

La fórmula es falsa en $(V,V)$ y $(F,F)$.

- Para $(V,V)$, la cláusula falsa exacta es $\neg P\lor\neg Q$.
- Para $(F,F)$, la cláusula falsa exacta es $P\lor Q$.

Por tanto,

$$(\neg P\lor\neg Q)\land(P\lor Q).$$


### 67

Queremos una cláusula falsa exactamente cuando $P=V,Q=F,R=V$.

Los literales deben ser falsos en esa fila:

- para $P=V$: $\neg P$;
- para $Q=F$: $Q$;
- para $R=V$: $\neg R$.

Así,

$G\equiv\neg P\lor Q\lor\neg R$.

Como sólo hay una fila falsa, una sola cláusula forma la FNC canónica.


### 68

Sea $F$ una fórmula con $n$ variables.

Para cada fila donde $F$ sea verdadera construimos una conjunción de $n$ literales que sea verdadera exactamente en esa fila: variable positiva si en la fila vale $V$, negada si vale $F$. La disyunción de todos esos términos coincide con $F$ en todas las filas; por tanto es una FND equivalente.

Para cada fila falsa construimos una disyunción de $n$ literales que sea falsa exactamente en esa fila: variable negada si en la fila vale $V$, positiva si vale $F$. La conjunción de esas cláusulas coincide con $F$ en todas las filas; por tanto es una FNC equivalente.

Los casos tautología y contradicción se representan por $V$ y $F$ respectivamente. Así, toda fórmula finita admite ambas formas normales.

## L. Síntesis y transferencia


### 69

Sea

$A=(P\Rightarrow Q)\land(P\Rightarrow\neg Q)$.

Del ejercicio 41 sabemos, o podemos reconstruir, que

$A\equiv\neg P$.

Entonces

$$
\begin{aligned}
A\Rightarrow\neg P
&\equiv\neg P\Rightarrow\neg P\\
&\equiv\neg(\neg P)\lor\neg P\\
&\equiv P\lor\neg P\\
&\equiv V.
\end{aligned}
$$

La fórmula es una tautología.

**Cómo pensar este problema.** Antes de expandir el condicional exterior, conviene simplificar su antecedente. Esa decisión evita una expansión mucho mayor.


### 70

«Exactamente una» de $P,Q,R$ verdadera significa que ocurre uno de tres casos mutuamente excluyentes:

1. $P$ verdadera, $Q,R$ falsas;
2. $Q$ verdadera, $P,R$ falsas;
3. $R$ verdadera, $P,Q$ falsas.

La FND es

$$(P\land\neg Q\land\neg R)
\lor(\neg P\land Q\land\neg R)
\lor(\neg P\land\neg Q\land R).$$

Es además la FND canónica relativa a esas tres filas verdaderas.


### 71

Para ser falsa exactamente en $(P,Q,R)=(V,F,V)$, una cláusula debe contener literales todos falsos en esa fila:

$\neg P\lor Q\lor\neg R$.

En cualquier otra fila al menos uno de esos literales cambia a verdadero, por lo que la cláusula se vuelve verdadera. Una sola cláusula basta porque sólo queremos excluir una valuación.


### 72

La fórmula

$F=(P\Leftrightarrow Q)\land(Q\Leftrightarrow R)$

exige que $P$ y $Q$ compartan valor y que $Q$ y $R$ también lo compartan. Por tanto, las tres variables deben tener el mismo valor.

**Ruta semántica.** La tabla de ocho filas muestra que $F$ sólo es verdadera en

$(V,V,V)$ y $(F,F,F)$.

Por eso una FND canónica inmediata es

$$(P\land Q\land R)\lor(\neg P\land\neg Q\land\neg R).$$

**Ruta algebraica.** Sustituimos cada bicondicional por su FND:

$$
\begin{aligned}
F
&\equiv[(P\land Q)\lor(\neg P\land\neg Q)]
\land[(Q\land R)\lor(\neg Q\land\neg R)].
\end{aligned}
$$

Al distribuir aparecen cuatro combinaciones. Dos contienen $Q\land\neg Q$ y desaparecen por contradicción; sobreviven exactamente

$P\land Q\land R$

y

$\neg P\land\neg Q\land\neg R$.

La tabla revela de manera transparente **qué valuaciones** sobreviven. La vía algebraica revela **por qué los casos mixtos se anulan estructuralmente**. Ambas son útiles, pero responden preguntas distintas.

## M. Problemas avanzados tipo prueba


### 73

Sea
$$
F=(P\land Q)\lor(\neg P\land R)\lor(Q\land R).
$$

El término sospechoso es $Q\land R$. Para decidir si aporta valuaciones nuevas introducimos una tautología dentro de él:

$$
\begin{aligned}
Q\land R
&\equiv Q\land R\land V\\
&\equiv Q\land R\land(P\lor\neg P)\\
&\equiv(P\land Q\land R)\lor(\neg P\land Q\land R).
\end{aligned}
$$

Sustituyendo en $F$,

$$
\begin{aligned}
F
&\equiv(P\land Q)\lor(\neg P\land R)
   \lor(P\land Q\land R)\lor(\neg P\land Q\land R)\\
&\equiv\big[(P\land Q)\lor(P\land Q\land R)\big]
   \lor\big[(\neg P\land R)\lor(\neg P\land Q\land R)\big]\\
&\equiv(P\land Q)\lor(\neg P\land R),
\end{aligned}
$$

porque

$$
(P\land Q)\lor[(P\land Q)\land R]\equiv P\land Q
$$

y

$$
(\neg P\land R)\lor[(\neg P\land R)\land Q]\equiv\neg P\land R
$$

por absorción.

Por tanto,

$$
\boxed{
(P\land Q)\lor(\neg P\land R)\lor(Q\land R)
\equiv
(P\land Q)\lor(\neg P\land R)
}.
$$

La razón estructural es precisa: si $Q\land R$ es verdadera, entonces o bien $P$ es verdadera, en cuyo caso ya es verdadero $P\land Q$, o bien $P$ es falsa, en cuyo caso ya es verdadero $\neg P\land R$. El término de consenso no añade ninguna valuación nueva.


### 74

Partimos de

$$
F=[(P\lor Q)\land(\neg P\lor R)]\Rightarrow(Q\lor R).
$$

Eliminamos la implicación:

$$
\begin{aligned}
F
&\equiv
\neg[(P\lor Q)\land(\neg P\lor R)]\lor(Q\lor R)\\
&\equiv
\neg(P\lor Q)\lor\neg(\neg P\lor R)\lor Q\lor R\\
&\equiv
(\neg P\land\neg Q)\lor(P\land\neg R)\lor Q\lor R.
\end{aligned}
$$

Reordenamos para agrupar los términos útiles:

$$
F\equiv
[Q\lor(\neg P\land\neg Q)]
\lor
[R\lor(P\land\neg R)].
$$

Aplicamos distributividad:

$$
\begin{aligned}
Q\lor(\neg P\land\neg Q)
&\equiv(Q\lor\neg P)\land(Q\lor\neg Q)\\
&\equiv(Q\lor\neg P)\land V\\
&\equiv Q\lor\neg P,
\end{aligned}
$$

y, análogamente,

$$
\begin{aligned}
R\lor(P\land\neg R)
&\equiv(R\lor P)\land(R\lor\neg R)\\
&\equiv(R\lor P)\land V\\
&\equiv R\lor P.
\end{aligned}
$$

Por tanto,

$$
\begin{aligned}
F
&\equiv(Q\lor\neg P)\lor(R\lor P)\\
&\equiv Q\lor R\lor(\neg P\lor P)\\
&\equiv Q\lor R\lor V\\
&\equiv V.
\end{aligned}
$$

La fórmula es una tautología:

$$
\boxed{F\equiv V}.
$$

La lectura semántica subyacente es la regla de resolución: si $P\lor Q$ y $\neg P\lor R$ son verdaderas, el valor de $P$ obliga a que al menos una de $Q,R$ sea verdadera.


### 75

La condición “al menos dos verdaderas” se cumple en cuatro filas:

$$
(V,V,F),\quad(V,F,V),\quad(F,V,V),\quad(V,V,V).
$$

**(a) FND canónica.** Cada fila verdadera produce un mintermino:

$$
\begin{aligned}
M\equiv&
(P\land Q\land\neg R)
\lor(P\land\neg Q\land R)\\
&\lor(\neg P\land Q\land R)
\lor(P\land Q\land R).
\end{aligned}
$$

**(b) FND reducida.** La condición “al menos dos” equivale a que sea verdadera alguna pareja:

$$
\boxed{
M\equiv(P\land Q)\lor(P\land R)\lor(Q\land R).
}
$$

Para justificarla algebraicamente, expandimos cada término con la variable ausente:

$$
P\land Q
\equiv
(P\land Q\land R)\lor(P\land Q\land\neg R),
$$

$$
P\land R
\equiv
(P\land Q\land R)\lor(P\land\neg Q\land R),
$$

$$
Q\land R
\equiv
(P\land Q\land R)\lor(\neg P\land Q\land R).
$$

Al unir los tres desarrollos y eliminar repeticiones por idempotencia recuperamos exactamente la FND canónica.

**(c) FNC canónica.** $M$ es falsa cuando hay cero o una proposición verdadera:

$$
(F,F,F),\quad(V,F,F),\quad(F,V,F),\quad(F,F,V).
$$

Las cláusulas canónicas correspondientes son

$$
\begin{aligned}
M\equiv&
(P\lor Q\lor R)
\land(\neg P\lor Q\lor R)\\
&\land(P\lor\neg Q\lor R)
\land(P\lor Q\lor\neg R).
\end{aligned}
$$

**(d) FNC reducida.** Al menos dos son verdaderas si y sólo si ninguna pareja tiene sus dos componentes falsos. Si como máximo una es verdadera, las otras dos forman una pareja falsa; si una pareja tiene sus dos componentes falsos, queda como máximo una verdadera. Por tanto, cada una de las tres parejas debe tener al menos un miembro verdadero. Equivalentemente:

$$
\boxed{
M\equiv(P\lor Q)\land(P\lor R)\land(Q\lor R).
}
$$

**(e) Equivalencia algebraica de las formas reducidas.** Partimos de la FNC:

$$
\begin{aligned}
&(P\lor Q)\land(P\lor R)\land(Q\lor R)\\
&\equiv[P\lor(Q\land R)]\land(Q\lor R)\\
&\equiv[P\land(Q\lor R)]\lor[(Q\land R)\land(Q\lor R)]\\
&\equiv[(P\land Q)\lor(P\land R)]\lor(Q\land R)\\
&\equiv(P\land Q)\lor(P\land R)\lor(Q\land R).
\end{aligned}
$$

Así las dos formas reducidas son equivalentes sin recurrir a una tabla.


### 76

Para distinguir el nombre de la fórmula de la constante falsa $F$, usamos $H$. Sea

$$
H=\neg[(P\Leftrightarrow Q)\Rightarrow(R\lor\neg P)].
$$

Comenzamos usando $\neg(A\Rightarrow B)\equiv A\land\neg B$:

$$
\begin{aligned}
H
&\equiv(P\Leftrightarrow Q)\land\neg(R\lor\neg P)\\
&\equiv(P\Leftrightarrow Q)\land(\neg R\land\neg\neg P)\\
&\equiv(P\Leftrightarrow Q)\land\neg R\land P.
\end{aligned}
$$

Eliminamos ahora el bicondicional en FNC:

$$
P\Leftrightarrow Q
\equiv
(\neg P\lor Q)\land(\neg Q\lor P).
$$

Por tanto,

$$
\begin{aligned}
H
&\equiv
(\neg P\lor Q)\land(\neg Q\lor P)\land\neg R\land P\\
&\equiv
P\land(\neg P\lor Q)\land(\neg Q\lor P)\land\neg R\\
&\equiv
[(P\land\neg P)\lor(P\land Q)]
\land(\neg Q\lor P)\land\neg R\\
&\equiv
[F\lor(P\land Q)]\land(\neg Q\lor P)\land\neg R\\
&\equiv
(P\land Q)\land(\neg Q\lor P)\land\neg R.
\end{aligned}
$$

Distribuimos una vez más:

$$
\begin{aligned}
(P\land Q)\land(\neg Q\lor P)
&\equiv
(P\land Q\land\neg Q)\lor(P\land Q\land P)\\
&\equiv F\lor(P\land Q)\\
&\equiv P\land Q.
\end{aligned}
$$

Finalmente,

$$
\boxed{H\equiv P\land Q\land\neg R}.
$$

Esta expresión es una **FND** porque es una disyunción de un solo término, y ese término es una conjunción de literales. También puede leerse como **FNC**:

$$
(P)\land(Q)\land(\neg R),
$$

es decir, una conjunción de tres cláusulas unitarias.

La simplificación muestra además exactamente cuándo la fórmula original es verdadera: $P$ y $Q$ deben ser verdaderas y $R$ falsa.


### 77

Consideremos

$$
G=(P\Rightarrow Q)\land(Q\Rightarrow R)\land(R\Rightarrow P).
$$

**(a) FNC inmediata.** Eliminando las implicaciones:

$$
\boxed{
G\equiv
(\neg P\lor Q)\land(\neg Q\lor R)\land(\neg R\lor P).
}
$$

Cada factor es ya una cláusula.

**(b) FND reducida.** Distribuimos primero las dos primeras cláusulas:

$$
\begin{aligned}
(\neg P\lor Q)\land(\neg Q\lor R)
\equiv&
(\neg P\land\neg Q)
\lor(\neg P\land R)\\
&\lor(Q\land\neg Q)
\lor(Q\land R)\\
\equiv&
(\neg P\land\neg Q)
\lor(\neg P\land R)
\lor(Q\land R).
\end{aligned}
$$

Ahora conjuntamos con $(\neg R\lor P)$.

Para el primer término:

$$
(\neg P\land\neg Q)\land(\neg R\lor P)
\equiv
(\neg P\land\neg Q\land\neg R)\lor F.
$$

Para el segundo:

$$
(\neg P\land R)\land(\neg R\lor P)
\equiv F\lor F\equiv F.
$$

Para el tercero:

$$
(Q\land R)\land(\neg R\lor P)
\equiv F\lor(P\land Q\land R).
$$

Por tanto,

$$
\boxed{
G\equiv
(\neg P\land\neg Q\land\neg R)
\lor(P\land Q\land R).
}
$$

**(c) Valuaciones.** Sólo satisfacen $G$

$$
(F,F,F)\quad\text{y}\quad(V,V,V).
$$

**(d) Interpretación.** Si alguna proposición del ciclo es verdadera, las implicaciones fuerzan sucesivamente la verdad de las otras dos. Si alguna es falsa, recorrer el ciclo en sentido lógico impide que aparezca una combinación mixta estable. El ciclo completo obliga a que las tres compartan valor.


### 78

Supongamos

$$
A\land C\equiv B\land C
\tag{1}
$$

y

$$
A\lor C\equiv B\lor C.
\tag{2}
$$

**Primera demostración: por valuaciones.**

Sea $v$ una valuación arbitraria.

- Si $v(C)=V$, de (1) obtenemos
  $v(A\land C)=v(A)$ y $v(B\land C)=v(B)$.
  Como ambos valores son iguales, $v(A)=v(B)$.
- Si $v(C)=F$, de (2) obtenemos
  $v(A\lor C)=v(A)$ y $v(B\lor C)=v(B)$.
  Nuevamente $v(A)=v(B)$.

En toda valuación, independientemente del valor de $C$, $A$ y $B$ coinciden. Por definición,

$$
\boxed{A\equiv B}.
$$

**Segunda demostración: algebraica.**

De (2), conjuntamos ambos lados con $\neg C$:

$$
(A\lor C)\land\neg C
\equiv
(B\lor C)\land\neg C.
$$

Distribuyendo,

$$
(A\land\neg C)\lor(C\land\neg C)
\equiv
(B\land\neg C)\lor(C\land\neg C),
$$

de donde

$$
A\land\neg C\equiv B\land\neg C.
\tag{3}
$$

Ahora descomponemos $A$ según $C\lor\neg C$:

$$
\begin{aligned}
A
&\equiv A\land V\\
&\equiv A\land(C\lor\neg C)\\
&\equiv(A\land C)\lor(A\land\neg C)\\
&\equiv(B\land C)\lor(B\land\neg C) &&\text{por (1) y (3)}\\
&\equiv B\land(C\lor\neg C)\\
&\equiv B.
\end{aligned}
$$

**Cada hipótesis aislada es insuficiente.**

Para la primera, toma $C=F$, $A=P$, $B=Q$. Entonces

$$
A\land C\equiv F\equiv B\land C,
$$

pero $P\not\equiv Q$.

Para la segunda, toma $C=V$, $A=P$, $B=Q$. Entonces

$$
A\lor C\equiv V\equiv B\lor C,
$$

pero nuevamente $P\not\equiv Q$.

Las dos hipótesis se complementan: una controla el caso $C=V$ y la otra el caso $C=F$.


### 79

La fórmula es

$$
H=(P\Leftrightarrow Q)\land(Q\Leftrightarrow\neg R)\land(R\Leftrightarrow S).
$$

**(a) Valuaciones sin tabla completa.**

Las tres condiciones imponen:

$$
Q=P,\qquad Q=\neg R,\qquad S=R.
$$

Por tanto,

$$
R=\neg P,\qquad S=\neg P.
$$

Todo queda determinado por el valor de $P$.

Si $P=V$:

$$
(P,Q,R,S)=(V,V,F,F).
$$

Si $P=F$:

$$
(P,Q,R,S)=(F,F,V,V).
$$

No hay otras posibilidades.

**(b) FND canónica.**

Los dos minterminos correspondientes son

$$
\boxed{
H\equiv
(P\land Q\land\neg R\land\neg S)
\lor
(\neg P\land\neg Q\land R\land S).
}
$$

**(c) FNC compacta.**

Usamos

$$
A\Leftrightarrow B
\equiv
(\neg A\lor B)\land(\neg B\lor A).
$$

Entonces:

$$
\begin{aligned}
P\Leftrightarrow Q
&\equiv(\neg P\lor Q)\land(\neg Q\lor P),\\
Q\Leftrightarrow\neg R
&\equiv(\neg Q\lor\neg R)\land(R\lor Q),\\
R\Leftrightarrow S
&\equiv(\neg R\lor S)\land(\neg S\lor R).
\end{aligned}
$$

Por tanto una FNC compacta es

$$
\boxed{
\begin{aligned}
H\equiv&
(\neg P\lor Q)\land(\neg Q\lor P)\\
&\land(\neg Q\lor\neg R)\land(R\lor Q)\\
&\land(\neg R\lor S)\land(\neg S\lor R).
\end{aligned}
}
$$

**(d) Justificación de equivalencia.**

La FNC procede directamente de reemplazar cada bicondicional por una fórmula equivalente; por sustitución de equivalentes, conserva exactamente el valor de $H$.

La FND canónica enumera exactamente las dos valuaciones que satisfacen simultáneamente las tres igualdades lógicas deducidas en (a). Cada mintermino es verdadero en una y sólo una de ellas. En cualquier otra valuación falla al menos uno de los tres bicondicionales.

Por tanto ambas formas representan exactamente la misma función booleana que $H$.


### 80

Sea

$$
F=
[(P\Rightarrow Q)\land(Q\Rightarrow R)\land(R\Rightarrow S)]
\Rightarrow(P\Rightarrow S).
$$

**(a) Demostración algebraica.**

Eliminamos la implicación principal:

$$
\begin{aligned}
F
&\equiv
\neg[(P\Rightarrow Q)\land(Q\Rightarrow R)\land(R\Rightarrow S)]
\lor(\neg P\lor S).
\end{aligned}
$$

Aplicamos De Morgan:

$$
\begin{aligned}
F
&\equiv
\neg(P\Rightarrow Q)
\lor\neg(Q\Rightarrow R)
\lor\neg(R\Rightarrow S)
\lor\neg P\lor S.
\end{aligned}
$$

Usamos $\neg(A\Rightarrow B)\equiv A\land\neg B$:

$$
F\equiv
(P\land\neg Q)
\lor(Q\land\neg R)
\lor(R\land\neg S)
\lor\neg P\lor S.
$$

Reordenamos:

$$
F\equiv
[\neg P\lor(P\land\neg Q)]
\lor(Q\land\neg R)
\lor(R\land\neg S)
\lor S.
$$

Simplificamos el primer corchete:

$$
\begin{aligned}
\neg P\lor(P\land\neg Q)
&\equiv(\neg P\lor P)\land(\neg P\lor\neg Q)\\
&\equiv V\land(\neg P\lor\neg Q)\\
&\equiv\neg P\lor\neg Q.
\end{aligned}
$$

Entonces

$$
F\equiv
\neg P\lor[\neg Q\lor(Q\land\neg R)]
\lor(R\land\neg S)\lor S.
$$

Ahora

$$
\begin{aligned}
\neg Q\lor(Q\land\neg R)
&\equiv(\neg Q\lor Q)\land(\neg Q\lor\neg R)\\
&\equiv\neg Q\lor\neg R.
\end{aligned}
$$

Por tanto

$$
F\equiv
\neg P\lor\neg Q\lor[\neg R\lor(R\land\neg S)]\lor S.
$$

Una vez más,

$$
\neg R\lor(R\land\neg S)
\equiv
\neg R\lor\neg S.
$$

Así,

$$
\begin{aligned}
F
&\equiv
\neg P\lor\neg Q\lor\neg R\lor\neg S\lor S\\
&\equiv
\neg P\lor\neg Q\lor\neg R\lor V\\
&\equiv V.
\end{aligned}
$$

Luego $F$ es tautología.

**(b) Demostración por contradicción semántica.**

Para que una implicación sea falsa, su antecedente debe ser verdadero y su consecuente falso.

Supongamos entonces que $F$ es falsa. Deben cumplirse simultáneamente:

$$
P\Rightarrow Q,\qquad
Q\Rightarrow R,\qquad
R\Rightarrow S,
$$

y debe ser falsa $P\Rightarrow S$.

La falsedad de $P\Rightarrow S$ exige

$$
P=V,\qquad S=F.
$$

Como $P=V$ y $P\Rightarrow Q$ es verdadera, necesariamente $Q=V$.

Como $Q=V$ y $Q\Rightarrow R$ es verdadera, necesariamente $R=V$.

Como $R=V$ y $R\Rightarrow S$ es verdadera, necesariamente $S=V$.

Pero ya habíamos obtenido $S=F$. Contradicción.

Por tanto no existe valuación que haga falsa a $F$, y nuevamente

$$
\boxed{F\equiv V}.
$$

La estructura general es la **transitividad encadenada de la implicación**: si la verdad de $P$ fuerza la de $Q$, la de $Q$ fuerza la de $R$ y la de $R$ fuerza la de $S$, entonces la verdad de $P$ fuerza necesariamente la de $S$.


## N. Elegir la representación según el objetivo


### 81
Factorizamos los dos primeros términos: $A\equiv P\land(Q\lor\neg Q)\lor R\equiv P\lor R$. Esta cláusula, con dos apariciones de literales, permite leer que $A$ es falsa exactamente cuando $P=F,R=F$, sea cual sea $Q$.

Para enumerar las filas verdaderas usamos la FND canónica:

$(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(P\land\neg Q\land R)\lor(P\land\neg Q\land\neg R)\lor(\neg P\land Q\land R)\lor(\neg P\land\neg Q\land R)$.

Los cuatro primeros términos cubren todas las filas con $P=V$; los dos últimos cubren $P=F,R=V$. Son las seis filas verdaderas de $P\lor R$, sin duplicaciones. Cada término contiene tres literales, por lo que hay dieciocho apariciones. La forma grande no reduce el tamaño; identifica cada fila por separado, que es precisamente el segundo objetivo. No es necesario expandir la fórmula compacta para decidir sus casos falsos.


### 82
La expansión disyuntiva del bicondicional da $B\equiv(P\land Q)\lor(\neg P\land\neg Q)\lor R$, una FND de tres términos y cinco apariciones de literales. El término unitario $R$ hace visible que $R=V$ basta para satisfacerla.

Usando la expansión conjuntiva y distribuyendo $R$:

$B\equiv[(\neg P\lor Q)\land(\neg Q\lor P)]\lor R\equiv(\neg P\lor Q\lor R)\land(\neg Q\lor P\lor R)$.

Esta FNC tiene dos cláusulas y seis apariciones de literales. La primera falla en $P=V,Q=F,R=F$; la segunda en $P=F,Q=V,R=F$. Son exactamente los dos casos de bicondicional falso y $R$ falso. Ambas formas son equivalentes por las leyes utilizadas. La FND tiene una aparición menos que esta FNC; eso compara dos escrituras concretas y no demuestra un mínimo entre todas las representaciones posibles.


### 83
Eliminar implicaciones da la FNC $(\neg P\lor Q)\land(\neg P\lor R)$, con cuatro apariciones. Sus dos cláusulas conservan visibles las dos exigencias: cuando $P$ es verdadero, se necesita $Q$ y también $R$.

Por distributividad inversa, esa FNC equivale a $\neg P\lor(Q\land R)$, una FND de dos términos y tres apariciones. Sus alternativas son claras: basta que $P$ sea falso, o que $Q,R$ sean ambos verdaderos.

Con $P=F$, las cuatro elecciones de $Q,R$ satisfacen la fórmula; con $P=V$, sólo $Q=V,R=V$ la satisface. Por tanto, la FND canónica tiene cinco términos de tres literales, con quince apariciones. Cada uno identifica una fila, mientras los dos términos compactos agrupan varias. La FNC separa exigencias; la FND compacta agrupa maneras de satisfacerlas; la canónica enumera cada posibilidad. Todas conservan el mismo comportamiento semántico.


## O. Variables declaradas y formas canónicas


### 84
Con $P,Q$, la FND canónica es $(P\land Q)\lor(\neg P\land\neg Q)$, y la FNC canónica es $(\neg P\lor Q)\land(P\lor\neg Q)$. Cada una tiene dos bloques de dos literales, con cuatro apariciones.

Al declarar también $R$, la FND canónica es

$(P\land Q\land R)\lor(P\land Q\land\neg R)\lor(\neg P\land\neg Q\land R)\lor(\neg P\land\neg Q\land\neg R)$.

La FNC canónica es

$(\neg P\lor Q\lor\neg R)\land(\neg P\lor Q\lor R)\land(P\lor\neg Q\lor\neg R)\land(P\lor\neg Q\lor R)$.

Cada fila previa se extiende con $R=V$ y $R=F$. Hay cuatro bloques de tres literales en cada forma, con doce apariciones. En la FND, factorizar cada pareja según $R\lor\neg R$ y usar complemento recupera los dos términos originales. En la FNC, cada pareja tiene la forma $(X\lor\neg R)\land(X\lor R)\equiv X\lor(\neg R\land R)\equiv X$, y recupera las dos cláusulas originales. $R$ figura en las formas canónicas ampliadas, pero su valor no decide la verdad del bicondicional.


### 85
Con sólo $Q$, ambas formas canónicas son $\neg Q$: un término o una cláusula de un literal.

Con $P,Q$, las filas verdaderas son $(V,F)$ y $(F,F)$, y la FND es $(P\land\neg Q)\lor(\neg P\land\neg Q)$. Las filas falsas son $(V,V)$ y $(F,V)$, y la FNC es $(\neg P\lor\neg Q)\land(P\lor\neg Q)$. Cada forma tiene dos bloques y cuatro apariciones. Factorización y complemento reducen las dos a $\neg Q$.

En el orden $Q,P$, las filas verdaderas se escriben $(F,V)$ y $(F,F)$; las falsas, $(V,V)$ y $(V,F)$. Cambia la posición de cada coordenada, no la condición «$Q$ falsa». Manteniendo identificadas las variables, las formas sólo requieren reordenar literales o bloques.

Con $P,Q,R$, hay cuatro filas verdaderas y cuatro falsas. Cada forma canónica tiene cuatro bloques de tres literales, con doce apariciones. Las variables adicionales no alteran el significado; duplican las extensiones de cada fila previa.


### 86
Sin variables declaradas hay una única valuación, la asignación vacía: no queda ninguna elección por realizar. Una tautología es verdadera en ella, así que su FND canónica contiene un término sin literales, interpretado como una conjunción vacía, $V$; su FNC no tiene cláusulas y también se representa por $V$.

Una contradicción es falsa en esa valuación. Su FND no tiene términos y se representa por $F$; su FNC contiene una cláusula sin literales, interpretada como una disyunción vacía, $F$. No deben confundirse «una cláusula vacía» y «ninguna cláusula»: la primera excluye la única valuación; la segunda no excluye ninguna.

Con $P,Q$, hay cuatro valuaciones. La tautología tiene cuatro términos canónicos de dos literales en su FND y ninguna cláusula en su FNC. La contradicción tiene ningún término en su FND y cuatro cláusulas canónicas de dos literales en su FNC. Las formas no vacías tienen ocho apariciones de literales; las representaciones constantes tienen cero. Son las mismas verdades extremas sobre dos contextos de comparación distintos.


## P. Alcance de una sustitución


### 87
Los signos de negación sobre las dos apariciones de $P$ no están anidados sobre una misma subfórmula. La doble negación exige el patrón $\neg\neg X$, no dos signos encontrados en lugares distintos.

De Morgan sobre el segundo término da

$D\equiv\neg P\lor(\neg Q\land\neg\neg P)\equiv\neg P\lor(\neg Q\land P)$.

Ahora sí aparece la subfórmula $\neg\neg P$ dentro de ese término y puede reemplazarse por $P$. Distribuyendo:

$\neg P\lor(\neg Q\land P)\equiv(\neg P\lor\neg Q)\land(\neg P\lor P)\equiv\neg P\lor\neg Q$.

Con $P=V,Q=V$, el original vale $F$, mientras el resultado propuesto $P\lor\neg Q$ vale $V$. Ese caso refuta la sustitución. La reparación aplica cada ley a un bloque con la estructura exacta que exige.


### 88
La ley es $X\land(X\lor Y)\equiv X$. Aquí $X=P\lor Q$ y $Y=R$, de modo que $E\equiv P\lor Q$. No puede reemplazarse el bloque completo por una sola parte $P$.

Con $P=F,Q=V,R=F$, ambos factores de $E$ son verdaderos, por lo que $E=V$, pero la respuesta propuesta $P$ vale $F$.

La ley depende de los valores del bloque $X$, que pueden ser $V$ o $F$, y no de cuántos símbolos tenga dentro. Por eso el mismo esquema vale para una subfórmula compuesta. Precisamente por eso hay que conservar ese bloque entero al sustituir. El resultado $P\lor Q$ es una cláusula y, por tanto, una FNC de una cláusula; también es una FND de dos términos unitarios.


### 89
De Morgan sobre la disyunción exterior da $\neg(P\Rightarrow Q)\land\neg R$. El paso propuesto reemplaza la negación de todo el condicional por un condicional con ambos componentes negados. Esos bloques no son equivalentes.

Con $P=F,Q=F,R=F$, el condicional $P\Rightarrow Q$ vale $V$, por lo que el original vale $F$. En cambio, $\neg P\Rightarrow\neg Q$ vale $V$ y $\neg R$ vale $V$, así que el resultado propuesto vale $V$.

La reparación es

$\neg[(P\Rightarrow Q)\lor R]\equiv\neg(P\Rightarrow Q)\land\neg R\equiv(P\land\neg Q)\land\neg R$.

El último paso usa eliminación de implicación y De Morgan: $\neg(P\Rightarrow Q)\equiv P\land\neg Q$. La fórmula sólo es verdadera en $P=V,Q=F,R=F$, pues exige esos tres literales simultáneamente. Es una FND de un término y una FNC de tres cláusulas unitarias.


## Q. Diseñar desde la tabla prescrita


### 90
Los cuatro minterminos dan la FND canónica

$(P\land Q\land\neg R)\lor(P\land\neg Q\land\neg R)\lor(\neg P\land Q\land R)\lor(\neg P\land\neg Q\land R)$.

Las filas falsas restantes son $(V,V,V),(V,F,V),(F,V,F),(F,F,F)$, por lo que la FNC canónica es

$(\neg P\lor\neg Q\lor\neg R)\land(\neg P\lor Q\lor\neg R)\land(P\lor\neg Q\lor R)\land(P\lor Q\lor R)$.

Agrupar las dos primeras filas verdaderas y las dos últimas por el valor de $Q$ simplifica la FND a $(P\land\neg R)\lor(\neg P\land R)$. La condición es que $P,R$ tengan valores distintos; $Q$ puede cambiar sin alterar la verdad.

Cada mintermino selecciona exactamente su fila y cada cláusula canónica excluye exactamente una fila falsa. Esa descripción cubre las ocho valuaciones, no sólo un ejemplo. Las formas canónicas tienen doce apariciones cada una; la FND compacta tiene cuatro.


### 91
La FND canónica es $(P\land\neg Q\land R)\lor(P\land\neg Q\land\neg R)$. Al factorizar se obtiene $P\land\neg Q\land(R\lor\neg R)\equiv P\land\neg Q$.

Esta última es una FNC de dos cláusulas unitarias. Eliminar $R$ es lícito porque, cuando $P=V,Q=F$, ambos valores de $R$ están permitidos, y cuando falla uno de esos requisitos, ninguno está permitido.

Las seis filas falsas producen la FNC canónica

$(\neg P\lor\neg Q\lor\neg R)\land(\neg P\lor\neg Q\lor R)\land(P\lor\neg Q\lor\neg R)\land(P\lor\neg Q\lor R)\land(P\lor Q\lor\neg R)\land(P\lor Q\lor R)$.

Las cláusulas corresponden, en orden, a $(V,V,V),(V,V,F),(F,V,V),(F,V,F),(F,F,V),(F,F,F)$. La conjunción es falsa exactamente en esas filas y verdadera en las dos prescritas. La FND canónica tiene seis apariciones, la FNC compacta dos y la FNC canónica dieciocho. Ninguna de estas equivalencias autoriza eliminar una variable de un término aislado sin comprobar qué filas nuevas se aceptarían.


### 92
Una opción siempre verdadera es $T=(P\lor Q)\lor\neg(P\lor Q)$: complemento aplicado al bloque $P\lor Q$ da $T\equiv V$. Una opción siempre falsa es $K=(R\land S)\land\neg(R\land S)$: complemento sobre $R\land S$ da $K\equiv F$.

Con cuatro variables declaradas hay dieciséis valuaciones. La FND canónica de $T$ incluye un mintermino por cada una: en cada bloque, las variables verdaderas se escriben sin negar y las falsas negadas. Son dieciséis términos de cuatro literales, con sesenta y cuatro apariciones. Su FNC canónica no tiene cláusulas y se representa por $V$.

La FND canónica de $K$ no tiene términos y se representa por $F$. Su FNC canónica incluye una cláusula por cada valuación, negando las variables que valen $V$ y dejando positivas las que valen $F$. Son dieciséis cláusulas de cuatro literales, con sesenta y cuatro apariciones. Cada fila hace falsa su propia cláusula.

Las constantes no aparecen en las fórmulas diseñadas, pero sí pueden aparecer en sus representaciones canónicas extremas conforme a la convención de §5.13. Las variables que no usa cada fórmula siguen interviniendo en la tabla declarada; su inclusión no cambia el comportamiento constante.

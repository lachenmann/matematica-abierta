---
title: "Soluciones de microcontroles — Capítulo 0"
content-id: MA-BCH-0178
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-000-MICROCONTROLES
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
    - "ANM-C00_MICROCONTROLES_SOLUCIONES.md, fuente canónica ANM; paquete C00 cerrado."
license: GFDL-1.3-or-later
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)

## §0.1. ¿Existen los números reales?

[]{#MA-MSOL-ANM-01-000-001}

[]{#MA-MIC-ANM-01-000-001}

[]{#MA-SEC-ANM-01-000-001}

### 1. ¿Por qué escribir una lista de axiomas no demuestra existencia?

Porque una **especificación** sólo describe qué propiedades debería satisfacer un objeto si existiera. Una lista de condiciones puede incluso ser incompatible. Para demostrar existencia hace falta exhibir al menos un modelo concreto y verificar que cumple simultáneamente todas las condiciones exigidas.

En símbolos, el paso inválido sería confundir

$$
\text{«si }F\text{ existe y satisface los axiomas, entonces tiene tales propiedades»}
$$

con

$$
\exists F\;\bigl(F\text{ satisface esos axiomas}\bigr).
$$

Definir la clase buscada no produce por sí solo un elemento de esa clase.

[]{#MA-MSOL-ANM-01-000-002}

[]{#MA-MIC-ANM-01-000-002}

### 2. Álgebra, orden y completitud

La especificación se divide en tres capas.

- **Álgebra:** $F$ debe ser un **cuerpo**: posee suma y producto, $0$ y $1$, opuestos, inversos multiplicativos para elementos no nulos y las leyes algebraicas correspondientes.
- **Orden:** $F$ debe llevar un **orden lineal compatible** con las operaciones; en particular, trasladar una desigualdad por la misma cantidad preserva el orden y el producto de dos elementos no negativos sigue siendo no negativo.
- **Completitud:** todo subconjunto no vacío de $F$ acotado superiormente debe tener un **supremo en $F$**.

Las dos primeras capas producen un cuerpo ordenado. La tercera añade la propiedad del supremo y da un cuerpo ordenado completo.

[]{#MA-MSOL-ANM-01-000-003}

[]{#MA-MIC-ANM-01-000-003}

### 3. ¿Qué falta para que una cota superior sea el supremo?

Si $s$ ya es una cota superior de $A$, falta que sea la **menor** de todas ellas. Es decir, debe cumplirse

$$
\forall u\in F,
\qquad
\bigl(u\text{ es cota superior de }A\bigr)
\Longrightarrow
s\le u.
$$

Junto con

$$
a\le s
\qquad(a\in A),
$$

esta condición caracteriza exactamente

$$
\boxed{s=\sup A}.
$$

[]{#MA-MSOL-ANM-01-000-004}

[]{#MA-MIC-ANM-01-000-004}

### 4. Acotación superior no es existencia de supremo

Decir que $A$ está **acotado superiormente** significa sólo que existe algún $u\in F$ tal que

$$
a\le u
\qquad(a\in A).
$$

Decir que $A$ **tiene supremo en $F$** exige mucho más: debe existir una cota superior $s\in F$ que sea menor o igual que cualquier otra cota superior.

Por tanto,

$$
\text{acotado superiormente}
\not\Rightarrow
\text{tener supremo}
$$

sin una hipótesis adicional de completitud. Precisamente la propiedad del supremo exige que esa implicación sí valga para todo subconjunto no vacío y acotado superiormente.

[]{#MA-MSOL-ANM-01-000-005}

[]{#MA-MIC-ANM-01-000-005}

### 5. ¿Qué significa que los racionales estén «dentro» de $F$?

La notación

$$
\mathbb Q\subseteq F
$$

no debería tomarse de entrada como inclusión literal de conjuntos. Lo que necesitamos es una **copia estructural** de $\mathbb Q$ dentro de $F$: una aplicación inyectiva que preserve la aritmética y el orden racionales.

Sólo después de construir y verificar esa incrustación podremos identificar por convenio cada racional con su imagen y usar una notación de inclusión sin perder información estructural.

La cuestión, por tanto, no es sólo dónde están los elementos, sino qué operaciones y relaciones se conservan al incorporarlos en el sistema mayor.

[]{#MA-MSOL-ANM-01-000-006}

[]{#MA-MIC-ANM-01-000-006}

### 6. Dos modelos no tienen que ser literalmente el mismo conjunto

Dos construcciones pueden usar objetos subyacentes distintos y, sin embargo, realizar exactamente la misma estructura matemática. Exigir desde el comienzo

$$
F=G
$$

como igualdad literal de conjuntos sería imponer una coincidencia de representación que no forma parte de la especificación.

La pregunta adecuada es estructural: si ambos resultan ser cuerpos ordenados completos, habrá que investigar si existe una correspondencia que conserve las operaciones y el orden, es decir, un **isomorfismo de cuerpos ordenados**.

En §0.1 esta cuestión queda sólo planteada. El orden lógico del capítulo sigue siendo

$$
\boxed{\text{primero existencia; después comparación estructural}.}
$$
## §0.2. Extender sin perder estructura: de $\mathbb N$ a $\mathbb Q$

[]{#MA-MSOL-ANM-01-000-007}

[]{#MA-MIC-ANM-01-000-007}

[]{#MA-SEC-ANM-01-000-002}

### 7. ¿Por qué la inyectividad es indispensable para una copia estructural?

La inyectividad impide que dos elementos distintos del sistema original se vuelvan indistinguibles después del transporte. Si existieran $a
e b$ con

$$
\iota(a)=\iota(b),
$$

entonces la imagen en $B$ ya no permitiría recuperar la diferencia entre $a$ y $b$. El sistema mayor habría **colapsado información** del sistema menor.

Por eso, para considerar a $A$ como una copia dentro de $B$, necesitamos que

$$
a
e b\Longrightarrow \iota(a)
e\iota(b).
$$

La preservación de operaciones y relaciones sólo produce una copia fiel cuando los elementos distintos siguen siendo distintos.

[]{#MA-MSOL-ANM-01-000-008}

[]{#MA-MIC-ANM-01-000-008}

### 8. Conservar la suma significa que dos caminos coinciden

La igualdad

$$
\iota(a+b)=\iota(a)+\iota(b)
$$

dice que podemos proceder de dos maneras sin cambiar el resultado.

1. **Calcular primero en $A$:** formar $a+b$ y luego transportarlo mediante $\iota$.
2. **Transportar primero a $B$:** tomar $\iota(a)$ y $\iota(b)$ y sumarlos usando la suma de $B$.

La condición de preservación afirma que ambos caminos terminan en el mismo elemento de $B$. Así, la suma antigua no cambia al pasar al sistema mayor.

[]{#MA-MSOL-ANM-01-000-009}

[]{#MA-MIC-ANM-01-000-009}

### 9. Qué ecuaciones nuevas resuelve cada ampliación

Al pasar de $\mathbb N$ a $\mathbb Z$ aparecen los **opuestos aditivos**, de modo que se pueden resolver ecuaciones que exigen una diferencia negativa. Por ejemplo,

$$
x+3=1
$$

no tiene solución en $\mathbb N$, pero en $\mathbb Z$ tiene la solución

$$
x=-2.
$$

Al pasar de $\mathbb Z$ a $\mathbb Q$ aparecen los **cocientes** necesarios para divisiones que no se resuelven enteramente. Por ejemplo,

$$
2x=1
$$

no tiene solución en $\mathbb Z$, pero en $\mathbb Q$ tiene

$$
x=\frac12.
$$

Cada ampliación añade soluciones nuevas sin borrar la aritmética que ya estaba disponible.

[]{#MA-MSOL-ANM-01-000-010}

[]{#MA-MIC-ANM-01-000-010}

### 10. Por qué $\mathbb N\hookrightarrow\mathbb Z$ no es una incrustación de cuerpos

Porque ni $\mathbb N$ ni $\mathbb Z$ son cuerpos. En $\mathbb N$ ni siquiera todos los elementos poseen opuesto aditivo dentro del sistema, y en $\mathbb Z$ un entero no nulo como $2$ no tiene inverso multiplicativo entero.

La flecha

$$
\mathbb N\hookrightarrow\mathbb Z
$$

sí es una incrustación de la estructura disponible en $\mathbb N$: preserva suma, producto, orden y los elementos distinguidos pertinentes. Lo incorrecto es atribuir al dominio y al codominio una estructura de cuerpo que no poseen.

[]{#MA-MSOL-ANM-01-000-011}

[]{#MA-MIC-ANM-01-000-011}

### 11. Incrustación, imagen e identificación con la imagen

Las tres expresiones corresponden a pasos distintos.

- $A\hookrightarrow B$ indica que existe una **incrustación estructural** $\iota:A\to B$: una aplicación inyectiva que conserva la estructura pertinente.
- $\iota(A)\subseteq B$ es una **inclusión literal de conjuntos**: la imagen de la aplicación es realmente un subconjunto de $B$.
- Escribir después $A\subseteq B$ es una **convención de identificación**: reemplazamos notacionalmente $A$ por la copia $\iota(A)$ porque ambas son estructuralmente equivalentes para lo que estamos estudiando.

El orden lógico es, por tanto,

$$
A\xhookrightarrow{\ \iota\ }B
\longrightarrow
\iota(A)\subseteq B
\longrightarrow
\text{identificar }A\text{ con }\iota(A).
$$

La última escritura no debe confundirse con una inclusión literal que estuviera dada desde el comienzo.

[]{#MA-MSOL-ANM-01-000-012}

[]{#MA-MIC-ANM-01-000-012}

### 12. Qué debe conservar una futura copia de $\mathbb Q$

Como $\mathbb Q$ es ya un cuerpo ordenado, una futura incrustación

$$
\iota_{\mathbb Q}:\mathbb Q\longrightarrow F
$$

debe ser inyectiva y conservar la estructura racional pertinente. En particular, para $p,q\in\mathbb Q$, deberá satisfacer

$$
\iota_{\mathbb Q}(p+q)
=
\iota_{\mathbb Q}(p)+\iota_{\mathbb Q}(q),
$$

$$
\iota_{\mathbb Q}(pq)
=
\iota_{\mathbb Q}(p)\,\iota_{\mathbb Q}(q),
$$

$$
\iota_{\mathbb Q}(0)=0,
\qquad
\iota_{\mathbb Q}(1)=1,
$$

y deberá preservar y reflejar el orden:

$$
p<q
\quad\Longleftrightarrow\quad
\iota_{\mathbb Q}(p)<\iota_{\mathbb Q}(q).
$$

Sólo después de verificar esa copia estructural estará justificada la economía notacional de escribir $\mathbb Q\subseteq F$.

## §0.3. El obstáculo: $\mathbb Q$ no está completo

[]{#MA-MSOL-ANM-01-000-013}

[]{#MA-MIC-ANM-01-000-013}

[]{#MA-SEC-ANM-01-000-003}

### 13. No vacío y acotado superiormente

Por definición,

$$
S_2=\{q\in\mathbb Q:q\ge 0,\ q^2<2\}.
$$

Para comprobar que no es vacío basta exhibir un elemento. Como

$$
1\ge0,
\qquad
1^2=1<2,
$$

tenemos

$$
1\in S_2.
$$

Ahora veamos que $2$ es una cota superior. Si $q\in S_2$ y suponemos $q\ge2$, entonces $q\ge0$ y por monotonía del cuadrado en los no negativos,

$$
q^2\ge4>2,
$$

contradiciendo $q^2<2$. Luego todo $q\in S_2$ satisface $q<2$, y en particular $q\le2$. Por tanto,

$$
\boxed{S_2\ne\varnothing\quad\text{y}\quad 2\text{ es una cota superior de }S_2.}
$$

[]{#MA-MSOL-ANM-01-000-014}

[]{#MA-MIC-ANM-01-000-014}

### 14. Por qué $s^2\ne2$ no basta

Demostrar que ningún racional satisface $s^2=2$ descarta sólo **una** de las tres posibilidades para un supuesto supremo racional $s$:

$$
s^2<2,
\qquad
s^2=2,
\qquad
s^2>2.
$$

Pero la definición de supremo no exige, por sí sola, que $s^2=2$. Para excluir realmente la existencia de $s=\sup_{\mathbb Q}S_2$ hay que mostrar también que los otros dos casos contradicen alguna propiedad esencial del supremo.

- Si $s^2<2$, la perturbación hacia la derecha produce un racional $s+\delta>s$ que aún pertenece a $S_2$.
- Si $s^2>2$, la perturbación hacia la izquierda produce una cota superior racional $t=s-\delta<s$.

Los dos argumentos de perturbación son, por tanto, los que enlazan la aritmética de $s^2$ con las dos condiciones definitorias del supremo: **ser cota superior** y **ser la menor cota superior**.

[]{#MA-MSOL-ANM-01-000-015}

[]{#MA-MIC-ANM-01-000-015}

### 15. Qué contradice $s+\delta$ cuando $s^2<2$

En ese caso se construye un racional $\delta>0$ tal que

$$
s+\delta>s
$$

y, al mismo tiempo,

$$
(s+\delta)^2<2.
$$

Como $s+\delta>0$, se sigue que

$$
s+\delta\in S_2.
$$

Esto contradice la primera obligación de un supremo: **ser una cota superior** del conjunto. En efecto, si $s$ fuera cota superior, ningún elemento de $S_2$ podría ser estrictamente mayor que $s$.

Así, el caso $s^2<2$ falla porque

$$
\boxed{s\text{ no puede ser cota superior de }S_2.}
$$

[]{#MA-MSOL-ANM-01-000-016}

[]{#MA-MIC-ANM-01-000-016}

### 16. Qué contradice $t=s-\delta$ cuando $s^2>2$

En este caso se construye un racional positivo

$$
t=s-\delta<s
$$

con

$$
t^2>2.
$$

Si $q\in S_2$ y ocurriera $q\ge t$, entonces, como $q,t\ge0$,

$$
q^2\ge t^2>2,
$$

contradiciendo $q^2<2$. Por tanto todo $q\in S_2$ satisface $q<t$, de modo que $t$ es también una cota superior de $S_2$.

Pero $t<s$. Esto contradice la segunda obligación del supremo: **ser la menor de todas las cotas superiores**.

Por eso el caso $s^2>2$ falla porque

$$
\boxed{s\text{ no puede ser la menor cota superior de }S_2.}
$$

[]{#MA-MSOL-ANM-01-000-017}

[]{#MA-MIC-ANM-01-000-017}

### 17. Densidad y completitud responden preguntas distintas

La **densidad** de $\mathbb Q$ afirma que entre dos racionales distintos siempre existe otro racional:

$$
p<q
\Longrightarrow
\exists r\in\mathbb Q:\ p<r<q.
$$

Es una propiedad local del orden entre puntos que ya pertenecen al sistema.

La **completitud por supremos**, en cambio, exige que todo subconjunto no vacío y acotado superiormente posea dentro del sistema una menor cota superior.

Por eso un orden puede ser denso y, sin embargo, incompleto. El conjunto $S_2$ muestra exactamente esa situación: podemos encontrar racionales cada vez más cercanos a la frontera que determina la condición $q^2<2$, pero esa frontera requerida no aparece como supremo racional.

En síntesis,

$$
\boxed{\text{densidad llena intervalos entre puntos; completitud garantiza ciertas fronteras.}}
$$

[]{#MA-MSOL-ANM-01-000-018}

[]{#MA-MIC-ANM-01-000-018}

### 18. La prueba no presupone un real con cuadrado $2$

El conjunto

$$
S_2=\{q\in\mathbb Q:q\ge0,\ q^2<2\}
$$

se define usando únicamente racionales, su orden y su multiplicación. La demostración trabaja siempre con elementos racionales: un supuesto $s\in\mathbb Q$, las perturbaciones racionales $s+\delta$ y $s-\delta$, y el argumento elemental de que ningún cociente de enteros en términos mínimos puede tener cuadrado igual a $2$.

Por tanto no necesitamos introducir antes un objeto llamado $\sqrt2$ ni suponer que exista en algún sistema mayor. La conclusión obtenida es más elemental y precisamente constructiva para el argumento del capítulo:

$$
\boxed{S_2\text{ es no vacío y acotado superiormente, pero no tiene supremo en }\mathbb Q.}
$$

Sólo después de localizar esta falla queda justificada la búsqueda de una ampliación que añada la frontera ausente sin perder la estructura racional.

## §0.4. Construir una frontera sin tener el punto

[]{#MA-MSOL-ANM-01-000-019}

[]{#MA-MIC-ANM-01-000-019}

[]{#MA-SEC-ANM-01-000-004}

### 19. Verificar que $L_c$ es una cortadura

Sea
$$
L_c=\{q\in\mathbb Q:q<c\},
\qquad c\in\mathbb Q.
$$

- **No vacío:** $c-1<c$, luego $c-1\in L_c$.
- **Propio:** $c\notin L_c$, así que $L_c\ne\mathbb Q$.
- **Cerrado hacia abajo:** si $q\in L_c$ y $r<q$, entonces $r<q<c$, por transitividad; por tanto $r\in L_c$.
- **Sin máximo:** si $q\in L_c$, entonces
  $$
  r=\frac{q+c}{2}
  $$
  satisface $q<r<c$. Así, $r\in L_c$ y $r>q$.

Por consiguiente,
$$
\boxed{L_c\text{ es una cortadura de Dedekind}.}
$$

[]{#MA-MSOL-ANM-01-000-020}

[]{#MA-MIC-ANM-01-000-020}

### 20. Por qué exigimos que una cortadura no tenga máximo

El conjunto
$$
\{q\in\mathbb Q:q\le c\}
$$
tiene máximo: el propio racional $c$. Por eso queda excluido por la condición «sin máximo».

Si suprimiéramos esa condición, serían admisibles a la vez
$$
\{q\in\mathbb Q:q<c\}
\qquad\text{y}\qquad
\{q\in\mathbb Q:q\le c\}.
$$
Son conjuntos distintos, pero ambos codificarían intuitivamente la misma frontera racional $c$. La cláusula «sin máximo» fija una convención única: una frontera racional se representa por los racionales estrictamente menores que ella.

[]{#MA-MSOL-ANM-01-000-021}

[]{#MA-MIC-ANM-01-000-021}

### 21. Por qué se separan los casos $q<0$ y $q\ge0$ en $A_2$

Para demostrar que $A_2$ no tiene máximo debemos, dado $q\in A_2$, encontrar otro elemento de $A_2$ estrictamente mayor.

Si $q<0$, basta tomar
$$
r=\frac q2,
$$
pues $q<r<0$, de modo que $r\in A_2$.

Si $q\ge0$, en cambio, $q/2\le q$ y no sirve. En ese caso, de $q\in A_2$ se sigue $q^2<2$, y esa desigualdad permite construir una perturbación racional positiva $\delta$ con
$$
(q+\delta)^2<2.
$$
Entonces $q+\delta\in A_2$ y $q+\delta>q$.

Los casos se separan porque la razón que garantiza la pertenencia —negatividad o desigualdad cuadrática— es distinta en cada región.

[]{#MA-MSOL-ANM-01-000-022}

[]{#MA-MIC-ANM-01-000-022}

### 22. Dónde se usa la tricotomía en la linealidad

Partimos de $A\not\subseteq B$ y elegimos $a\in A\setminus B$. Para un $b\in B$ arbitrario, no puede ocurrir $a<b$, porque la clausura hacia abajo de $B$ implicaría $a\in B$. Tampoco puede ocurrir $a=b$.

Es exactamente aquí donde usamos la **tricotomía** del orden racional: entre $a<b$, $a=b$ y $b<a$, descartadas las dos primeras posibilidades, necesariamente
$$
b<a.
$$
Como $a\in A$ y $A$ es cerrado hacia abajo, $b\in A$. Al ser $b\in B$ arbitrario,
$$
B\subseteq A.
$$

[]{#MA-MSOL-ANM-01-000-023}

[]{#MA-MIC-ANM-01-000-023}

### 23. Interpretar $A\subsetneq B$ como comparación de posiciones

La inclusión
$$
A\subsetneq B
$$
dice que todo racional registrado como situado a la izquierda de la posición codificada por $A$ también está a la izquierda de la posición codificada por $B$, y además existe al menos un racional que pertenece a $B$ pero no a $A$.

Por tanto $B$ registra **más racionales a su izquierda** que $A$. Ésta es la lectura que motiva
$$
A<_{\mathcal D}B
\quad\Longleftrightarrow\quad
A\subsetneq B:
$$
la posición codificada por $B$ queda estrictamente más a la derecha que la codificada por $A$. Esta interpretación usa sólo los códigos racionales y no presupone puntos reales ya construidos.

[]{#MA-MSOL-ANM-01-000-024}

[]{#MA-MIC-ANM-01-000-024}

### 24. Tener $\mathcal D$ como conjunto no basta para construir los reales

La inclusión
$$
\mathcal D\subseteq\mathcal P(\mathbb Q)
$$
justifica que $\mathcal D$ es un conjunto bien definido. Además, §0.4 le da un orden lineal por inclusión.

Pero todavía falta definir y verificar suma y producto, cero y uno, opuestos e inversos multiplicativos, las leyes de cuerpo, la compatibilidad con el orden y la propiedad del supremo.

Por tanto, de $\mathcal D\subseteq\mathcal P(\mathbb Q)$ no se sigue que $\mathcal D$ sea un cuerpo ordenado completo. En §0.4 hemos construido **el dominio y su orden**; la estructura algebraica y la completitud todavía deben demostrarse.

## §0.5. Una copia de $\mathbb Q$ dentro del nuevo sistema

[]{#MA-MSOL-ANM-01-000-025}

[]{#MA-MIC-ANM-01-000-025}

[]{#MA-SEC-ANM-01-000-005}

### 25. Comparar directamente $(-2)^*$, $0^*$ y $3^*$

Por definición,

$$
(-2)^*=\{r\in\mathbb Q:r<-2\},
\qquad
0^*=\{r\in\mathbb Q:r<0\},
\qquad
3^*=\{r\in\mathbb Q:r<3\}.
$$

Si $r\in(-2)^*$, entonces $r<-2<0$, de modo que $r\in0^*$. Por tanto,

$$
(-2)^*\subseteq0^*.
$$

La inclusión es estricta porque, por ejemplo,

$$
-1\in0^*
\qquad\text{pero}\qquad
-1\notin(-2)^*.
$$

Análogamente, si $r\in0^*$, entonces $r<0<3$, así que $r\in3^*$ y

$$
0^*\subseteq3^*.
$$

La inclusión es estricta porque

$$
1\in3^*
\qquad\text{pero}\qquad
1\notin0^*.
$$

Así, sin usar la proposición general,

$$
\boxed{(-2)^*\subsetneq0^*\subsetneq3^*.}
$$

[]{#MA-MSOL-ANM-01-000-026}

[]{#MA-MIC-ANM-01-000-026}

### 26. Recuperar $p<q$ desde $p^*\subsetneq q^*$

La inclusión estricta garantiza que existe algún

$$
r\in q^*\setminus p^*.
$$

De $r\in q^*$ obtenemos

$$
r<q.
$$

En cambio, $r\notin p^*$ significa que no se cumple $r<p$. Por tricotomía del orden racional, de $\neg(r<p)$ se sigue

$$
p\le r.
$$

Combinando ambas desigualdades,

$$
p\le r<q,
$$

y por tanto

$$
\boxed{p<q.}
$$

El elemento de la diferencia funciona como un testigo racional que queda a la izquierda de $q$ pero no a la izquierda de $p$.

[]{#MA-MSOL-ANM-01-000-027}

[]{#MA-MIC-ANM-01-000-027}

### 27. Preservar el orden no es lo mismo que reflejarlo

La implicación

$$
p<q
\Longrightarrow
p^*\subsetneq q^*
$$

dice que $\iota_{\mathbb Q}$ **preserva** el orden: una desigualdad racional verdadera sigue siendo visible después del transporte.

La equivalencia completa

$$
p<q
\Longleftrightarrow
p^*\subsetneq q^*
$$

añade la dirección recíproca. Por tanto también podemos **recuperar** el orden racional mirando sólo las imágenes:

$$
p^*\subsetneq q^*
\Longrightarrow
p<q.
$$

Eso es reflexión del orden. Así, la equivalencia certifica que dentro de la imagen no aparecen comparaciones estrictas nuevas que no correspondan a una comparación racional original.

[]{#MA-MSOL-ANM-01-000-028}

[]{#MA-MIC-ANM-01-000-028}

### 28. Cómo se obtiene la inyectividad

Supongamos

$$
p^*=q^*.
$$

Si $p<q$, la equivalencia de orden obligaría a

$$
p^*\subsetneq q^*,
$$

lo que contradice $p^*=q^*$.

Si $q<p$, obtendríamos del mismo modo

$$
q^*\subsetneq p^*,
$$

otra contradicción.

Por tricotomía sólo queda

$$
p=q.
$$

Así,

$$
\boxed{p^*=q^*\Longrightarrow p=q,}
$$

y por tanto $\iota_{\mathbb Q}$ es inyectiva. La igualdad de imágenes no puede ocultar dos racionales distintos porque cualquier desigualdad entre ellos produciría una inclusión estricta entre sus cortaduras.

[]{#MA-MSOL-ANM-01-000-029}

[]{#MA-MIC-ANM-01-000-029}

### 29. Situar $A_2$ entre $1^*$ y $2^*$

Recordemos

$$
A_2=\{r\in\mathbb Q:r<0\ \text{o}\ r^2<2\}.
$$

Primero probamos

$$
1^*\subsetneq A_2.
$$

Si $r\in1^*$, entonces $r<1$. Si $r<0$, ya pertenece a $A_2$. Si $0\le r<1$, entonces

$$
r^2<1<2,
$$

de modo que también $r\in A_2$. Por tanto $1^*\subseteq A_2$.

La inclusión es estricta porque

$$
1\in A_2
\qquad\text{pero}\qquad
1\notin1^*.
$$

Ahora probamos

$$
A_2\subsetneq2^*.
$$

Sea $r\in A_2$. Si $r<0$, entonces $r<2$. Si $r\ge0$ y $r^2<2$, no puede ocurrir $r\ge2$, pues eso daría $r^2\ge4>2$. Luego siempre $r<2$, y por tanto $r\in2^*$.

La inclusión es estricta porque

$$
\frac32\in2^*
$$

pero

$$
\left(\frac32\right)^2=\frac94>2,
$$

y además $\frac32\not<0$, así que $\frac32\notin A_2$.

Concluimos, usando sólo aritmética racional,

$$
\boxed{1^*\subsetneq A_2\subsetneq2^*.}
$$

No fue necesario introducir ningún número cuyo cuadrado sea $2$.

[]{#MA-MSOL-ANM-01-000-030}

[]{#MA-MIC-ANM-01-000-030}

### 30. Por qué todavía no hay una incrustación de cuerpos ordenados

Hasta §0.5 hemos definido en $\mathcal D$ el orden por inclusión, y hemos demostrado que

$$
\iota_{\mathbb Q}(q)=q^*
$$

es inyectiva y preserva y refleja ese orden.

Pero todavía no hemos definido en $\mathcal D$ una suma ni un producto. Por tanto expresiones como

$$
p^*+q^*
\qquad\text{o}\qquad
p^*q^*
$$

aún no forman parte de la estructura disponible en esta sección.

Una incrustación de cuerpos ordenados debe conservar, además del orden, las operaciones de cuerpo y los elementos distinguidos correspondientes. Como esa verificación algebraica todavía no puede formularse plenamente, el certificado correcto es sólo

$$
\boxed{\text{incrustación de órdenes lineales}.}
$$

La certificación como incrustación de cuerpos ordenados queda pendiente hasta definir y verificar la aritmética de cortaduras.

[]{#MA-MSOL-ANM-01-000-031}

[]{#MA-MIC-ANM-01-000-031}

### 31. Las dos identidades algebraicas que quedan pendientes

Para que la copia racional conserve también la aritmética habrá que definir primero suma y producto en $\mathcal D$ y demostrar, para todos $p,q\in\mathbb Q$,

$$
\boxed{p^*+q^*=(p+q)^*}
$$

y

$$
\boxed{p^*q^*=(pq)^*.}
$$

La primera identidad certificará que sumar dentro de $\mathcal D$ y luego identificar el resultado con una cortadura racional coincide con sumar primero en $\mathbb Q$.

La segunda hará lo mismo para el producto.

Sólo después de esas verificaciones, junto con los elementos distinguidos y los inversos pertinentes, podrá elevarse la certificación de $\iota_{\mathbb Q}$ desde una incrustación ordenada a una incrustación de cuerpos ordenados.

## §0.6. Dar aritmética a las cortaduras I: suma y opuesto

[]{#MA-MSOL-ANM-01-000-032}

[]{#MA-MIC-ANM-01-000-032}

[]{#MA-SEC-ANM-01-000-006}

### 32. Por qué un racional exterior domina a toda la cortadura

Sean $A\in\mathcal D$, $u\notin A$ y $a\in A$. Queremos justificar que necesariamente

$$
a<u.
$$

Si ocurriera $u\le a$, la clausura hacia abajo de $A$ se aplicaría a $a\in A$ y daría

$$
u\in A,
$$

contradiciendo $u\notin A$. Por tanto $u\le a$ es imposible.

Como $a$ y $u$ son racionales comparables, sólo queda

$$
\boxed{a<u.}
$$

Ésta es exactamente la propiedad usada al probar que $A+B$ es propio: si $u\notin A$ y $v\notin B$, entonces todo $a+b\in A+B$ satisface

$$
a+b<u+v,
$$

de modo que $u+v\notin A+B$.

[]{#MA-MSOL-ANM-01-000-033}

[]{#MA-MIC-ANM-01-000-033}

### 33. Reconstruir explícitamente una suma racional

Queremos demostrar

$$
p^*+q^*=(p+q)^*.
$$

Si $x\in p^*+q^*$, existen $a<p$ y $b<q$ con $x=a+b$. Entonces

$$
x=a+b<p+q,
$$

y por tanto $x\in(p+q)^*$.

Para la inclusión contraria, supongamos

$$
x<p+q.
$$

La diferencia $p+q-x$ es racional y positiva. Tomemos

$$
\varepsilon=\frac{p+q-x}{2}>0,
$$

y definamos

$$
a=p-\varepsilon,
\qquad
b=q-\varepsilon.
$$

Entonces

$$
a<p,
\qquad
b<q,
$$

de modo que $a\in p^*$ y $b\in q^*$. Además,

$$
a+b
=p+q-2\varepsilon
=p+q-(p+q-x)
=x.
$$

Así $x\in p^*+q^*$. Las dos inclusiones dan

$$
\boxed{p^*+q^*=(p+q)^*.}
$$

La elección simétrica de $\varepsilon$ reparte exactamente entre los dos sumandos el margen que separa a $x$ de $p+q$.

[]{#MA-MSOL-ANM-01-000-034}

[]{#MA-MIC-ANM-01-000-034}

### 34. Por qué el reflejo ingenuo no define el opuesto

Consideremos primero

$$
\{-s:s\notin A\}.
$$

Para ver el problema basta tomar una cortadura racional $A=q^*$. Entonces

$$
s\notin q^*
\quad\Longleftrightarrow\quad
s\ge q.
$$

Por tanto

$$
\{-s:s\notin q^*\}
=
\{t\in\mathbb Q:t\le -q\}.
$$

Este conjunto tiene máximo, precisamente $-q$. En consecuencia viola la condición de que una cortadura no tenga máximo.

Así, el simple reflejo del complemento produce un lado izquierdo **cerrado en la frontera**. La definición correcta

$$
-A
=
\{r\in\mathbb Q:\exists s\notin A\text{ con }r<-s\}
$$

vuelve a abrir esa frontera: no toma sólo los puntos $-s$, sino todos los racionales estrictamente menores que alguno de ellos.

En el caso racional esto recupera exactamente $(-q)^*$, pero sin introducir un punto final en la cortadura.

[]{#MA-MSOL-ANM-01-000-035}

[]{#MA-MIC-ANM-01-000-035}

### 35. Dónde se usa la propiedad arquimediana en el lema de aproximación

En el lema partimos de

$$
a_0\in A,
\qquad
u\notin A,
\qquad
h>0.
$$

Como todo elemento de $A$ queda estrictamente por debajo de todo racional exterior,

$$
a_0<\nu,
$$

y por tanto $\nu-a_0>0$.

La propiedad arquimediana de $\mathbb Q$ se usa exactamente para elegir un natural $n$ tal que

$$
nh>\nu-a_0.
$$

De aquí obtenemos

$$
a_0+nh>\nu.
$$

Ese término ya no puede pertenecer a $A$, pues si perteneciera, la clausura hacia abajo y $\nu<a_0+nh$ obligarían a $\nu\in A$.

Por tanto la lista finita

$$
a_0,
a_0+h,
\ldots,
a_0+nh
$$

empieza dentro de $A$ y termina fuera. Sólo después de este paso arquimediano tiene sentido escoger el **primer** índice en que se sale de la cortadura.

La propiedad arquimediana no se usa para identificar una frontera; se usa únicamente para garantizar que una cantidad finita de pasos de tamaño $h$ termina atravesándola.

[]{#MA-MSOL-ANM-01-000-036}

[]{#MA-MIC-ANM-01-000-036}

### 36. La inclusión $0^*\subseteq A+(-A)$

Sea

$$
x\in0^*.
$$

Entonces $x<0$. Debemos escribir $x$ como suma de un elemento de $A$ y uno de $-A$.

Definimos

$$
h=-\frac{x}{2}>0.
$$

Esta elección tiene dos funciones simultáneas:

$$
x=-2h
$$

y el lema de aproximación puede aplicarse porque $h>0$.

El lema proporciona $a\in A$ tal que

$$
a+h\notin A.
$$

Escribamos

$$
s=a+h
$$

y

$$
b=x-a.
$$

Como $x=-2h$,

$$
b=-2h-a<-h-a=-s.
$$

Además $s\notin A$. Por la definición de $-A$, estas dos condiciones implican

$$
b\in-A.
$$

Finalmente,

$$
x=a+b,
$$

con $a\in A$ y $b\in-A$. Por tanto

$$
\boxed{x\in A+(-A).}
$$

Como $x<0$ era arbitrario,

$$
\boxed{0^*\subseteq A+(-A).}
$$

El factor $1/2$ crea exactamente el margen estricto necesario: $b$ queda no sólo en $-s$, sino estrictamente por debajo de $-s$.

[]{#MA-MSOL-ANM-01-000-037}

[]{#MA-MIC-ANM-01-000-037}

### 37. El orden se conserva y se refleja al sumar la misma cortadura

Supongamos primero

$$
A\subseteq B.
$$

Si $x\in A+C$, entonces $x=a+c$ para ciertos $a\in A$ y $c\in C$. Como $A\subseteq B$, también $a\in B$, y por tanto

$$
x\in B+C.
$$

Así,

$$
A+C\subseteq B+C.
$$

Para la recíproca, supongamos

$$
A+C\subseteq B+C.
$$

La monotonía ya demostrada permite sumar $-C$ a ambos lados:

$$
(A+C)+(-C)
\subseteq
(B+C)+(-C).
$$

Por asociatividad,

$$
A+(C+(-C))
\subseteq
B+(C+(-C)).
$$

Como

$$
C+(-C)=0^*
$$

y $0^*$ es el neutro aditivo, obtenemos

$$
A\subseteq B.
$$

Por consiguiente,

$$
\boxed{A\subseteq B\iff A+C\subseteq B+C.}
$$

La posibilidad de cancelar $C$ depende precisamente de que ya hayamos construido su opuesto aditivo.

[]{#MA-MSOL-ANM-01-000-038}

[]{#MA-MIC-ANM-01-000-038}

### 38. El opuesto de una cortadura racional

Queremos probar directamente

$$
-(q^*)=(-q)^*.
$$

Sea $x\in-(q^*)$. Por definición existe $s\notin q^*$ tal que

$$
x<-s.
$$

La condición $s\notin q^*$ equivale a $s\ge q$. Al cambiar de signo,

$$
-s\le -q.
$$

Por tanto

$$
x<-s\le -q,
$$

de modo que $x<-q$ y

$$
x\in(-q)^*.
$$

Esto prueba

$$
-(q^*)\subseteq(-q)^*.
$$

Recíprocamente, si $x\in(-q)^*$, entonces $x<-q$. Tomamos

$$
s=q.
$$

Como $q\notin q^*$ y $x<-q=-s$, la definición de $-(q^*)$ da

$$
x\in-(q^*).
$$

Así,

$$
\boxed{-(q^*)=(-q)^*.}
$$

La construcción del opuesto en $\mathcal D$ reproduce exactamente el opuesto racional sobre la copia $q\mapsto q^*$.

[]{#MA-MSOL-ANM-01-000-039}

[]{#MA-MIC-ANM-01-000-039}

### 39. Qué falta para obtener una incrustación de cuerpos ordenados

Al terminar §0.6 ya están certificadas para la copia racional la inyectividad, el orden, la suma, el cero y los opuestos. Lo que falta es la **estructura multiplicativa** necesaria para que $\mathcal D$ sea un cuerpo ordenado y para que $\iota_{\mathbb Q}$ sea un homomorfismo de cuerpos ordenados.

En concreto, todavía habrá que:

- definir un producto interno $\mathcal D\times\mathcal D\to\mathcal D$ y probar su clausura;
- verificar asociatividad y conmutatividad del producto;
- identificar una unidad multiplicativa, que deberá corresponder a $1^*$;
- construir inversos multiplicativos para las cortaduras no nulas;
- verificar la distributividad respecto de la suma;
- comprobar la compatibilidad del producto con el orden;
- demostrar sobre la copia racional la identidad pendiente
  $$
  p^*q^*=(pq)^*.
  $$

Sólo cuando esas obligaciones estén demostradas podrá concluirse que $\mathcal D$ posee estructura de cuerpo ordenado y que

$$
\iota_{\mathbb Q}:\mathbb Q\hookrightarrow\mathcal D
$$

conserva toda la estructura de cuerpo ordenado.

Por tanto, al cierre de §0.6 el certificado correcto sigue siendo

$$
\boxed{
\text{estructura aditiva completa; estructura multiplicativa todavía pendiente}.
}
$$

## §0.7. Dar aritmética a las cortaduras II: producto e inverso

[]{#MA-MSOL-ANM-01-000-040}

[]{#MA-MIC-ANM-01-000-040}

[]{#MA-SEC-ANM-01-000-007}

### 40. Por qué el producto ingenuo de todos los testigos falla

El conjunto

$$
\{ab:a\in A,\ b\in B\}
$$

no puede ser la definición general del producto. Toda cortadura es no vacía y cerrada hacia abajo, de modo que contiene racionales negativos de magnitud arbitrariamente grande. En efecto, si $a_0\in A$ y $b_0\in B$, podemos elegir un natural $n$ suficientemente grande para que

$$
-n<a_0,
\qquad
-n<b_0.
$$

Entonces $-n\in A\cap B$, y el producto de esos dos testigos es

$$
(-n)(-n)=n^2.
$$

Como $n^2$ puede hacerse arbitrariamente grande, el conjunto de productos ingenuos contiene racionales positivos sin cota superior. En particular, no puede representar una cortadura propia situada a la izquierda de una frontera finita.

El problema no es la multiplicación racional, sino haber ignorado el signo de los testigos. Por eso §0.7 construye primero el producto de las **partes positivas** y sólo después extiende la regla a todos los signos.

[]{#MA-MSOL-ANM-01-000-041}

[]{#MA-MIC-ANM-01-000-041}

### 41. Tres formas equivalentes de positividad

Queremos probar

$$
A>0^*
\quad\Longleftrightarrow\quad
0\in A
\quad\Longleftrightarrow\quad
\exists a\in A:\ a>0.
$$

Si $A>0^*$, entonces $0^*\subsetneq A$. Existe, por tanto, $x\in A\setminus0^*$. Como $x\notin0^*$, tenemos $x\ge0$. Si $x=0$, ya está probado que $0\in A$; si $x>0$, la clausura hacia abajo de $A$ vuelve a dar $0\in A$.

Si $0\in A$, la ausencia de máximo proporciona un $a\in A$ con

$$
0<a.
$$

Finalmente, si existe $a\in A$ con $a>0$, todo racional $q<0$ satisface $q<a$, y la clausura hacia abajo implica $q\in A$. Luego

$$
0^*\subseteq A.
$$

La inclusión es estricta porque $a\in A$ pero $a\notin0^*$. Así $0^*\subsetneq A$, es decir, $A>0^*$.

[]{#MA-MSOL-ANM-01-000-042}

[]{#MA-MIC-ANM-01-000-042}

### 42. Por qué un racional exterior debe ser positivo

Supongamos $A>0^*$ y $u\notin A$. Por la equivalencia anterior,

$$
0\in A.
$$

Si $u<0$, entonces $u\in0^*\subseteq A$, contradicción. Si $u=0$, también tendríamos $u\in A$.

Por tanto las posibilidades $u\le0$ quedan excluidas y necesariamente

$$
\boxed{u>0.}
$$

Este hecho es el que permite comparar productos conservando el sentido del orden: para $a\in A_{>0}$ y un exterior $u\notin A$, tenemos $0<a<u$, y al multiplicar por cantidades positivas la desigualdad sigue orientada de la misma manera.

[]{#MA-MSOL-ANM-01-000-043}

[]{#MA-MIC-ANM-01-000-043}

### 43. Verificación directa del producto racional positivo

Sean $p,q>0$. Debemos probar

$$
p^*\cdot_+q^*=(pq)^*.
$$

Si $x\in p^*\cdot_+q^*$, existen $0<a<p$ y $0<b<q$ con $x<ab$. Como

$$
ab<pb<pq,
$$

se sigue $x<pq$, es decir, $x\in(pq)^*$.

Para la recíproca, sea $x<pq$. Si $x\le0$, cualquier elección racional $0<a<p$ y $0<b<q$ da

$$
x\le0<ab,
$$

y por tanto $x\in p^*\cdot_+q^*$.

Supongamos ahora $0<x<pq$. Como $q>0$,

$$
\frac{x}{q}<p.
$$

Aquí aparece la primera aplicación de la densidad de $\mathbb Q$: elegimos

$$
\frac{x}{q}<a<p.
$$

Entonces $a>0$ y $x<aq$, de modo que

$$
\frac{x}{a}<q.
$$

La segunda aplicación de la densidad permite escoger

$$
\frac{x}{a}<b<q.
$$

Así $0<a<p$, $0<b<q$ y $x<ab$. Por consiguiente $x\in p^*\cdot_+q^*$.

La densidad se usa exactamente para insertar testigos racionales estrictamente dentro de las dos fronteras racionales y, al mismo tiempo, mantener su producto por encima de $x$.

[]{#MA-MSOL-ANM-01-000-044}

[]{#MA-MIC-ANM-01-000-044}

### 44. Los cinco casos del producto general están bien tipados

La definición separa exhaustivamente los signos de $A$ y $B$.

- Si $A=0^*$ o $B=0^*$, se define $AB=0^*$ y no aparece $\cdot_+$.
- Si $A>0^*$ y $B>0^*$, se usa directamente $A\cdot_+B$: ambos argumentos son positivos.
- Si $A<0^*$ y $B<0^*$, entonces $-A>0^*$ y $-B>0^*$; por eso $(-A)\cdot_+(-B)$ está bien definido.
- Si $A>0^*>B$, entonces $A>0^*$ y, como $B<0^*$, tenemos $-B>0^*$. Así $A\cdot_+(-B)$ recibe dos argumentos positivos; el opuesto exterior fija el signo negativo del resultado.
- Si $B>0^*>A$, entonces $B>0^*$ y $-A>0^*$. Por tanto $(-A)\cdot_+B$ vuelve a recibir dos argumentos positivos, y el opuesto exterior vuelve a producir el signo correcto.

La tricotomía del orden de $\mathcal D$ garantiza que no falta ningún caso y que dos casos no pueden aplicarse simultáneamente.

[]{#MA-MSOL-ANM-01-000-045}

[]{#MA-MIC-ANM-01-000-045}

### 45. Por qué el recíproco positivo contiene automáticamente $q\le0$

Si $A>0^*$, su recíproco debe ser también una cortadura **estrictamente positiva**. Toda cortadura positiva contiene $0$ y, por clausura hacia abajo, contiene todos los racionales negativos.

Por eso la definición

$$
A^{-1,+}
=
\left\{
q\in\mathbb Q:
q\le0
\text{ o }
\exists s>0\,(s\notin A\text{ y }q<s^{-1})
\right\}
$$

incluye desde el comienzo la región $q\le0$. Esta cláusula cumple dos funciones: garantiza inmediatamente que

$$
0\in A^{-1,+},
$$

y fija toda la parte izquierda no positiva sin obligarnos a producir, para cada uno de esos racionales, un testigo exterior $s$ específico.

La información nueva sobre la frontera inversa está sólo en la segunda cláusula, que controla los racionales positivos mediante recíprocos de puntos exteriores de $A$.

[]{#MA-MSOL-ANM-01-000-046}

[]{#MA-MIC-ANM-01-000-046}

### 46. El papel del lema de aproximación y de $h<(1-x)c$

En la inclusión difícil

$$
1^*\subseteq A\cdot_+A^{-1,+},
$$

tomamos $0<x<1$ y elegimos primero $c\in A$ con $c>0$.

La condición

$$
0<h<(1-x)c
$$

hace que $h$ sea un paso racional positivo **suficientemente pequeño**. El lema de aproximación de §0.6 puede entonces aplicarse y produce un $a\in A$ tal que

$$
s:=a+h\notin A.
$$

Así obtenemos simultáneamente un punto interior $a$ y un punto exterior $s$ separados exactamente por $h$.

Como $c\in A$ y $s\notin A$, tenemos $c<s=a+h$, luego

$$
a>c-h>0.
$$

Además,

$$
(1-x)(c-h)-xh=(1-x)c-h>0.
$$

Como $a>c-h$ y $1-x>0$,

$$
(1-x)a>xh.
$$

Esto equivale a

$$
a>x(a+h)=xs,
$$

y, como $a,s>0$,

$$
\frac{x}{a}<\frac1s.
$$

Ahora la densidad racional permite elegir $b$ entre esos dos números. La desigualdad $b<1/s$ coloca $b$ en $A^{-1,+}$, mientras que $x/a<b$ da $x<ab$.

Por tanto, el lema fabrica el par interior–exterior cercano y la elección de $h<(1-x)c$ garantiza exactamente el margen necesario para que el intervalo

$$
\left(\frac{x}{a},\frac1s\right)
$$

sea no vacío.

[]{#MA-MSOL-ANM-01-000-047}

[]{#MA-MIC-ANM-01-000-047}

### 47. Cómo $x<abc$ fabrica el testigo intermedio de la asociatividad

Supongamos primero que, después de desplegar los testigos de

$$
(A\cdot_+B)\cdot_+C,
$$

hemos llegado a

$$
x<abc
$$

con $a\in A_{>0}$, $b\in B_{>0}$ y $c\in C_{>0}$.

Para demostrar que $x\in A\cdot_+(B\cdot_+C)$ necesitamos un racional positivo $v\in B\cdot_+C$ con $x<av$.

- Si $x\le0$, basta escoger por densidad $0<v<bc$. Entonces $v\in B\cdot_+C$ y $x<0<av$.
- Si $x>0$, de $x<abc$ obtenemos $x/a<bc$. Por densidad elegimos
  $$
  \frac{x}{a}<v<bc.
  $$
  Entonces $v\in B\cdot_+C$ y $x<av$.

En la dirección inversa se hace exactamente lo mismo con un testigo $u\in A\cdot_+B$: si $x\le0$, tomamos $0<u<ab$; si $x>0$, usamos

$$
\frac{x}{c}<u<ab.
$$

Así, la desigualdad $x<abc$ no se usa como si $abc$ fuera un elemento-frontera del producto. Se usa para abrir un **intervalo racional no vacío** en el que la densidad permite insertar el testigo intermedio requerido por la otra agrupación.

[]{#MA-MSOL-ANM-01-000-048}

[]{#MA-MIC-ANM-01-000-048}

### 48. Por qué hay que comparar $B$ con $-C$ en la distributividad de signos opuestos

Supongamos

$$
B>0^*>C.
$$

Entonces $C_0:=-C$ es positivo. El signo de la suma

$$
B+C=B-C_0
$$

no puede decidirse sólo sabiendo que $B$ es positivo y $C$ negativo: depende de cuál de las dos magnitudes positivas, $B$ o $C_0$, sea mayor.

Por linealidad hay exactamente tres posibilidades:

$$
B=C_0,
\qquad
C_0<B,
\qquad
B<C_0.
$$

En el primer caso $B+C=0^*$. En el segundo,

$$
D:=B-C_0>0^*,
\qquad
C_0+D=B,
$$

y podemos aplicar la distributividad **positiva** a $C_0+D$. En el tercero,

$$
D:=C_0-B>0^*,
\qquad
B+D=C_0,
$$

y de nuevo disponemos de una suma de cortaduras positivas a la que sí se aplica el resultado ya demostrado.

La comparación $B$ frente a $-C$ sirve, por tanto, para convertir el caso de signos opuestos en uno de tres problemas cuyo término residual $D$ es positivo. Sin esa comparación no sabríamos qué expresión positiva está autorizada para invocar la distributividad ya probada.

[]{#MA-MSOL-ANM-01-000-049}

[]{#MA-MIC-ANM-01-000-049}

### 49. Qué certifica ahora que $\mathcal D$ es un cuerpo ordenado

Al terminar §0.7 están verificadas exactamente las propiedades siguientes.

- **Estructura aditiva:** $(\mathcal D,+,0^*)$ es un grupo abeliano.
- **Producto interno:** $A\cdot B\in\mathcal D$ para todos $A,B\in\mathcal D$.
- **Leyes multiplicativas:** el producto es asociativo y conmutativo.
- **Unidad:** $1^*$ satisface $A1^*=A=1^*A$ y $1^*\ne0^*$.
- **Inversos:** todo $A\ne0^*$ posee $A^{-1}$ con
  $$
  AA^{-1}=1^*=A^{-1}A.
  $$
- **Distributividad:** $A(B+C)=AB+AC$ y, por conmutatividad, también $(B+C)A=BA+CA$.
- **Orden:** la inclusión es un orden lineal; la suma preserva el orden y el producto de dos elementos no negativos es no negativo.

Éstas son precisamente las obligaciones algebraicas y de orden necesarias para concluir

$$
\boxed{(\mathcal D,+,\cdot,\le_{\mathcal D})\text{ es un cuerpo ordenado}.}
$$

La propiedad que todavía falta es la **completitud**: aún no se ha probado que toda familia no vacía de cortaduras acotada superiormente tenga supremo en $\mathcal D$. Por eso el cuerpo ordenado ya construido todavía no satisface toda la especificación de §0.1.

[]{#MA-MSOL-ANM-01-000-050}

[]{#MA-MIC-ANM-01-000-050}

### 50. Por qué sólo ahora podemos escribir $\mathbb Q\subseteq\mathcal D$

En §0.5 sabíamos que

$$
q\longmapsto q^*
$$

era inyectiva y preservaba y reflejaba el orden. En §0.6 añadimos la conservación de la suma, el cero y los opuestos. Eso todavía no bastaba para una incrustación de **cuerpos**.

Al terminar §0.7 están verificadas también

$$
(pq)^*=p^*\cdot q^*,
\qquad
1_{\mathcal D}=1^*,
$$

y, para $q\ne0$,

$$
(q^{-1})^*=(q^*)^{-1}.
$$

Por tanto la aplicación

$$
\iota_{\mathbb Q}:\mathbb Q\to\mathcal D,
\qquad
q\mapsto q^*,
$$

es ya una **incrustación de cuerpos ordenados**: es inyectiva y conserva suma, producto, $0$, $1$ y orden.

Sólo ahora está justificada la identificación estructural de cada racional con su imagen. La abreviatura

$$
\boxed{\mathbb Q\subseteq\mathcal D}
$$

no afirma una inclusión literal preexistente entre los objetos de ambas construcciones; significa que, desde este punto, trabajaremos identificando $\mathbb Q$ con la copia isomorfa $\iota_{\mathbb Q}(\mathbb Q)$ contenida en $\mathcal D$.

## §0.8. Sí existen: el supremo como unión

[]{#MA-MSOL-ANM-01-000-051}

[]{#MA-MIC-ANM-01-000-051}

[]{#MA-SEC-ANM-01-000-008}

### 51. La unión es cerrada hacia abajo sin usar todavía una cota superior

Sea

$$
S=\bigcup_{A\in\mathscr A}A.
$$

Supongamos $q\in S$ y $r<q$. Por definición de unión existe alguna cortadura $A\in\mathscr A$ tal que $q\in A$. Como toda cortadura es cerrada hacia abajo,

$$
r<q\in A
\quad\Longrightarrow\quad
r\in A.
$$

Entonces $r\in S$.

Por tanto,

$$
\boxed{q\in S,\ r<q\Longrightarrow r\in S.}
$$

La hipótesis de que $\mathscr A$ esté acotada superiormente no interviene aquí: la clausura inferior se hereda localmente de un único miembro de la familia que contiene a $q$.

[]{#MA-MSOL-ANM-01-000-052}

[]{#MA-MIC-ANM-01-000-052}

### 52. Dónde se usa exactamente la acotación superior

La acotación superior se necesita en la verificación de que

$$
S=\bigcup\mathscr A
$$

es una cortadura **propia**, es decir, que

$$
S\ne\mathbb Q.
$$

Si $U\in\mathcal D$ es una cota superior de $\mathscr A$, entonces

$$
A\subseteq U
\qquad(A\in\mathscr A).
$$

De aquí se obtiene

$$
S\subseteq U.
$$

Como $U$ es una cortadura,

$$
U\ne\mathbb Q.
$$

Luego tampoco puede ocurrir $S=\mathbb Q$.

Así, la hipótesis de acotación se gasta exactamente para impedir que la unión de todos los miembros de $\mathscr A$ crezca hasta ocupar todo $\mathbb Q$.

[]{#MA-MSOL-ANM-01-000-053}

[]{#MA-MIC-ANM-01-000-053}

### 53. Por qué una cota superior contiene a toda la unión

Sea $U$ una cota superior de $\mathscr A$. En el orden de $\mathcal D$, esto significa

$$
A\subseteq U
\qquad
\text{para todo }A\in\mathscr A.
$$

Tomemos $q\in\bigcup\mathscr A$. Por definición de unión existe algún $A\in\mathscr A$ con

$$
q\in A.
$$

Como $A\subseteq U$, se sigue que

$$
q\in U.
$$

El racional $q$ era arbitrario, luego

$$
\boxed{\bigcup\mathscr A\subseteq U.}
$$

La inclusión es simplemente la traducción conjuntista de que $U$ domina simultáneamente a todos los miembros de la familia.

[]{#MA-MSOL-ANM-01-000-054}

[]{#MA-MIC-ANM-01-000-054}

### 54. La unión no tiene máximo

Sea

$$
q\in S=\bigcup_{A\in\mathscr A}A.
$$

Entonces existe algún $A\in\mathscr A$ tal que $q\in A$. Como $A$ es una cortadura, no tiene máximo. Por tanto existe un racional $r\in A$ con

$$
q<r.
$$

Pero $A\subseteq S$, de modo que también

$$
r\in S.
$$

Así, cada elemento $q$ de $S$ admite otro elemento de $S$ estrictamente mayor. Por consiguiente,

$$
\boxed{S\text{ no tiene máximo}.}
$$

No hace falta coordinar simultáneamente todos los miembros de la familia: basta trabajar en la cortadura concreta que testimonia la pertenencia de $q$ a la unión.

[]{#MA-MSOL-ANM-01-000-055}

[]{#MA-MIC-ANM-01-000-055}

### 55. «Ser cortadura» y «ser supremo» son dos certificados distintos

La afirmación

$$
S\in\mathcal D
$$

es un certificado de **tipado**: dice que $S$ satisface las cuatro condiciones de una cortadura y, por tanto, es un elemento legítimo del sistema ordenado $\mathcal D$.

La afirmación

$$
S=\sup_{\mathcal D}\mathscr A
$$

es un certificado de **posición en el orden**: exige que

$$
A\subseteq S
\qquad(A\in\mathscr A)
$$

y que, para toda cota superior $V$,

$$
S\subseteq V.
$$

Probar que $S$ es una cortadura no demuestra esas dos propiedades de orden: una cortadura cualquiera puede no dominar a la familia. Y antes de poder presentar $S$ como supremo en $\mathcal D$ debemos saber que $S$ pertenece efectivamente a $\mathcal D$.

Por eso el manuscrito separa los bloques:

$$
\boxed{S\in\mathcal D}
\qquad\text{y después}\qquad
\boxed{S=\sup_{\mathcal D}\mathscr A}.
$$

[]{#MA-MSOL-ANM-01-000-056}

[]{#MA-MIC-ANM-01-000-056}

### 56. Toda otra cota superior contiene a $S$

Sea $V\in\mathcal D$ otra cota superior de $\mathscr A$. Entonces

$$
A\subseteq V
\qquad(A\in\mathscr A).
$$

Tomemos $q\in S$. Como

$$
S=\bigcup_{A\in\mathscr A}A,
$$

existe algún $A\in\mathscr A$ con $q\in A$. Al ser $V$ cota superior,

$$
A\subseteq V,
$$

por lo que $q\in V$.

Así,

$$
\boxed{S\subseteq V.}
$$

En el orden por inclusión esto equivale a

$$
S\le_{\mathcal D}V,
$$

y prueba que $S$ es menor o igual que cualquier otra cota superior.

[]{#MA-MSOL-ANM-01-000-057}

[]{#MA-MIC-ANM-01-000-057}

### 57. La fórmula del supremo no presupone números reales anteriores

La identidad

$$
\sup_{\mathcal D}\mathscr A
=
\bigcup\mathscr A
$$

se demuestra enteramente dentro de la construcción por cortaduras.

- Cada $A\in\mathscr A$ es un subconjunto de $\mathbb Q$.
- $\bigcup\mathscr A$ es la unión conjuntista ordinaria de esos subconjuntos racionales.
- Después se verifica que esa unión es una cortadura.
- Finalmente se comprueba, usando inclusión de conjuntos, que es cota superior y menor que cualquier otra cota superior.

En ningún paso se parte de un número real previamente existente ni de un supremo tomado en un sistema real externo. Precisamente la demostración establece que el objeto construido por unión **satisface la definición** de supremo dentro de $\mathcal D$.

Por tanto la fórmula es una conclusión de la construcción, no una importación de la completitud que estamos intentando demostrar.

[]{#MA-MSOL-ANM-01-000-058}

[]{#MA-MIC-ANM-01-000-058}

### 58. Los dos certificados que cierran la existencia

El primer certificado proviene de §0.7:

```text
ORDERED_FIELD = VERIFIED
```

Es decir,

$$
(\mathcal D,+,\cdot,\le_{\mathcal D})
$$

es un cuerpo ordenado.

El segundo certificado es el resultado central de §0.8:

```text
SUPREMUM_PROPERTY = VERIFIED
```

Toda familia no vacía de cortaduras acotada superiormente posee un supremo en $\mathcal D$, dado por su unión.

Al combinar ambos obtenemos exactamente la especificación de §0.1:

$$
\boxed{
\text{cuerpo ordenado}
+
\text{propiedad del supremo}
=
\text{cuerpo ordenado completo}.
}
$$

Por tanto

$$
\boxed{\mathcal D\text{ es un cuerpo ordenado completo}.}
$$

[]{#MA-MSOL-ANM-01-000-059}

[]{#MA-MIC-ANM-01-000-059}

### 59. Por qué sólo ahora podemos llamar a $\mathcal D$ un modelo de los reales

Antes de §0.8 habíamos construido un dominio de cortaduras, un orden y finalmente una estructura de cuerpo ordenado. Pero la especificación inicial exigía además la propiedad del supremo.

Ahora sabemos simultáneamente que

$$
\mathcal D
$$

es un cuerpo ordenado y que toda familia no vacía y acotada superiormente tiene supremo en él. Por tanto $\mathcal D$ satisface **todas** las condiciones que habíamos fijado para el sistema buscado.

Eso autoriza la afirmación

$$
\boxed{\mathcal D\text{ es un modelo de los números reales}.}
$$

«Modelo» significa aquí una realización concreta de la estructura especificada. No significa que un número real deba ser, por esencia, una cortadura de Dedekind.

[]{#MA-MSOL-ANM-01-000-060}

[]{#MA-MIC-ANM-01-000-060}

### 60. Existencia y unicidad son problemas distintos

Haber demostrado existencia significa haber probado

$$
\boxed{\text{existe al menos un cuerpo ordenado completo con una copia ordenada de }\mathbb Q.}
$$

La construcción de $\mathcal D$ proporciona ese ejemplo concreto.

La unicidad plantea una afirmación diferente. Si $F$ y $G$ fueran dos cuerpos ordenados completos construidos de maneras posiblemente distintas, habría que demostrar que no representan estructuras esencialmente diferentes, es decir, establecer una comparación estructural adecuada entre ambos.

Nada en la mera existencia de $\mathcal D$ demuestra por sí solo ese resultado. Por tanto, al cierre de §0.8 tenemos

$$
\boxed{\text{EXISTENCIA: resuelta}}
$$

pero la cuestión de unicidad queda como un problema nuevo que todavía debe demostrarse.

[]{#MA-MSOL-ANM-01-000-061}

[]{#MA-MIC-ANM-01-000-061}

### 61. Qué sabemos ahora de $A_2$ que no sabíamos en §0.4

En §0.4 habíamos construido

$$
A_2
=
\{q\in\mathbb Q:q<0\text{ o }q^2<2\}
$$

y demostrado dos cosas: que $A_2$ es una cortadura y que no coincide con ninguna cortadura racional $q^*$.

En ese punto todavía no estaba justificado llamarla número real, porque aún no habíamos probado que el sistema $\mathcal D$ tuviera toda la estructura exigida.

Ahora sí sabemos que

$$
\mathcal D
$$

es un cuerpo ordenado completo. Como

$$
A_2\in\mathcal D,
$$

$A_2$ es legítimamente un elemento de **un modelo de los números reales**. Además, como no es ningún $q^*$,

$$
A_2\notin\iota_{\mathbb Q}(\mathbb Q).
$$

Por tanto la antigua «frontera codificada» se ha convertido en un elemento no racional del modelo completo construido, sin haber supuesto previamente la existencia de irracionales.
## §0.9. ¿Podría haber otros reales?

[]{#MA-MSOL-ANM-01-000-062}

[]{#MA-MIC-ANM-01-000-062}

[]{#MA-SEC-ANM-01-000-009}

### 62. Por qué un cuerpo ordenado debe tener característica cero

En un cuerpo ordenado se tiene $0_F<1_F$. Sumando $1_F$ repetidamente y usando la invariancia del orden por traslación obtenemos, para $n>0$,

$$
0_F<1_F<2\cdot1_F<\cdots<n\cdot1_F.
$$

En particular,

$$
n\cdot1_F\ne0_F
$$

para todo entero positivo $n$. Pero la característica de un cuerpo sería positiva precisamente si existiera un mínimo $n>0$ con $n\cdot1_F=0_F$. Por tanto

$$
\boxed{\operatorname{char}F=0.}
$$

El orden impide que los numerales positivos colapsen en el cero.

[]{#MA-MSOL-ANM-01-000-063}

[]{#MA-MIC-ANM-01-000-063}

### 63. Por qué $\jmath_{\mathbb Z}^F(m-n)$ no depende de la diferencia formal

Supongamos que el mismo entero admite dos representaciones

$$
m-n=p-q.
$$

Entonces, en $\mathbb Z$,

$$
m+q=n+p.
$$

Los numerales en $F$ respetan la suma, así que

$$
\nu_F(m)+\nu_F(q)=\nu_F(n)+\nu_F(p).
$$

Trasladando términos dentro del grupo aditivo de $F$,

$$
\nu_F(m)-\nu_F(n)=\nu_F(p)-\nu_F(q).
$$

Por tanto ambas diferencias formales producen el mismo elemento de $F$, y la definición

$$
\boxed{\jmath_{\mathbb Z}^F(m-n)=\nu_F(m)-\nu_F(n)}
$$
\nes independiente del representante escogido.

[]{#MA-MSOL-ANM-01-000-064}

[]{#MA-MIC-ANM-01-000-064}

### 64. Por qué $\iota_F(a/b)$ no depende del representante racional

Si

$$
\frac ab=\frac cd,
\qquad b,d\ne0,
$$
\nentonces

$$
ad=bc
$$
\nen $\mathbb Z$. La multiplicatividad de $\jmath_{\mathbb Z}^F$ da

$$
\jmath(a)\jmath(d)=\jmath(b)\jmath(c).
$$

Como $b,d\ne0$ y $\jmath_{\mathbb Z}^F$ es inyectiva, $\jmath(b)$ y $\jmath(d)$ son no nulos y poseen inversos en $F$. Multiplicando por esos inversos, obtenemos

$$
\jmath(a)\jmath(b)^{-1}=\jmath(c)\jmath(d)^{-1}.
$$

Así el valor

$$
\boxed{\iota_F(a/b)=\jmath(a)\jmath(b)^{-1}}
$$

no depende de la fracción elegida. La propiedad decisiva es la **igualdad por productos cruzados**, transportada por la multiplicatividad, junto con la no anulación de los denominadores.

[]{#MA-MSOL-ANM-01-000-065}

[]{#MA-MIC-ANM-01-000-065}

### 65. Primer uso exacto de la completitud

La completitud no se usa para construir la copia canónica de $\mathbb Q$: característica cero, enteros y racionales aparecen en cualquier cuerpo ordenado.

El primer gasto de completitud ocurre al demostrar que $F$ es arquimediano. Se supone por contradicción que

$$
N_F=\{\nu_F(n):n\in\mathbb N\}
$$
\nestá acotado superiormente. Entonces, y sólo entonces, la completitud permite formar

$$
\boxed{s=\sup N_F.}
$$

Ese supremo es la herramienta que produce la contradicción.

[]{#MA-MSOL-ANM-01-000-066}

[]{#MA-MIC-ANM-01-000-066}

### 66. La contradicción arquimediana completa

Supongamos que $N_F$ está acotado superiormente y sea

$$
s=\sup N_F.
$$

Como

$$
s-1_F<s,
$$

$s-1_F$ no puede ser una cota superior de $N_F$, pues sería una cota superior menor que el supremo. Por tanto existe $n\in\mathbb N$ tal que

$$
s-1_F<\nu_F(n).
$$

Sumando $1_F$ a ambos lados,

$$
s<\nu_F(n)+1_F=\nu_F(n+1).
$$

Pero $\nu_F(n+1)\in N_F$, lo que contradice que $s$ sea cota superior. Luego $N_F$ no está acotado superiormente y

$$
\boxed{F\text{ es arquimediano}.}
$$

[]{#MA-MSOL-ANM-01-000-067}

[]{#MA-MIC-ANM-01-000-067}

### 67. Por qué «hay un entero mayor que $x$» todavía no localiza a $x$

Saber solamente que existe un entero $m$ con

$$
x<\iota_F(m)
$$

da una cota superior entera, pero no dice cuál es la primera celda de la rejilla entera que contiene a $x$. Para el refinamiento racional posterior necesitamos simultáneamente un extremo entero por debajo y otro inmediatamente por encima:

$$
\boxed{\iota_F(m-1)\le x<\iota_F(m).}
$$

La información adicional de que $m$ es el **primer** entero de cierta lista que queda por encima de $x$ es lo que produce la desigualdad inferior con $m-1$.

[]{#MA-MSOL-ANM-01-000-068}

[]{#MA-MIC-ANM-01-000-068}

### 68. El papel del mínimo de $K$

Se define

$$
K=\{k\in\mathbb N:x<-\nu_F(n)+\nu_F(k)\}.
$$

La arquimedianidad garantiza que $K$ es no vacío. Por el buen orden de $\mathbb N$, existe un mínimo $k_0$. Como $k_0\ne0$, escribimos $k_0=k+1$.

La minimalidad tiene dos consecuencias complementarias:

- $k_0\in K$, luego
  $$
  x<-\nu_F(n)+\nu_F(k+1);
  $$
- $k\notin K$, luego, por totalidad del orden,
  $$
  -\nu_F(n)+\nu_F(k)\le x.
  $$

Si definimos $m=-n+(k+1)$, estas dos desigualdades se convierten exactamente en

$$
\boxed{\iota_F(m-1)\le x<\iota_F(m).}
$$

El mínimo convierte una cota cualquiera en una **celda entera consecutiva**.

[]{#MA-MSOL-ANM-01-000-069}

[]{#MA-MIC-ANM-01-000-069}

### 69. Cómo $1/n<y-x$ y la localización de $nx$ producen un racional intermedio

Sean $x<y$. La arquimedianidad permite elegir $n>0$ con

$$
\iota_F\!\left(\frac1n\right)<y-x.
$$

Aplicamos la localización entera a $x\,\iota_F(n)$ y obtenemos $m\in\mathbb Z$ tal que

$$
\iota_F(m-1)\le x\,\iota_F(n)<\iota_F(m).
$$

Como $\iota_F(n)>0$, al dividir por ella obtenemos

$$
\iota_F\!\left(\frac{m-1}{n}\right)\le x<\iota_F\!\left(\frac mn\right).
$$

Además, de la desigualdad izquierda de la localización se deduce

$$
\iota_F\!\left(\frac mn\right)\le x+\iota_F\!\left(\frac1n\right)<y.
$$

Por tanto, para $q=m/n$,

$$
\boxed{x<\iota_F(q)<y.}
$$

El paso $1/n<y-x$ hace que la malla racional sea más fina que la separación entre $x$ e $y$.

[]{#MA-MSOL-ANM-01-000-070}

[]{#MA-MIC-ANM-01-000-070}

### 70. Las cuatro condiciones de $A_x$ y dónde se usa la densidad

Para

$$
A_x=\{q\in\mathbb Q:\iota_F(q)<x\}
$$

verificamos:

- **No vacío:** como $x-1_F<x$, por densidad existe $q_-$ con $x-1_F<\iota_F(q_-)<x$. Entonces $q_-\in A_x$.
- **Propio:** como $x<x+1_F$, por densidad existe $q_+$ con $x<\iota_F(q_+)<x+1_F$. Entonces $q_+\notin A_x$.
- **Cerrado hacia abajo:** si $p<q$ y $q\in A_x$, la preservación del orden da $\iota_F(p)<\iota_F(q)<x$, luego $p\in A_x$.
- **Sin máximo:** si $q\in A_x$, entonces $\iota_F(q)<x$; por densidad existe $r$ con $\iota_F(q)<\iota_F(r)<x$. La reflexión del orden da $q<r$, y $r\in A_x$.

Así

$$
\boxed{A_x\in\mathcal D.}
$$

La densidad se usa en las condiciones **no vacío**, **propio** y **sin máximo**; la clausura hacia abajo sólo usa que $\iota_F$ preserva el orden.

[]{#MA-MSOL-ANM-01-000-071}

[]{#MA-MIC-ANM-01-000-071}

### 71. Segundo gasto de completitud: reconstruir $x$ desde su traza

El conjunto

$$
\iota_F(A_x)=\{\iota_F(q):q\in A_x\}
$$
\nes no vacío y está acotado superiormente por $x$. La completitud se usa por segunda vez para asegurar que existe

$$
s=\sup_F\iota_F(A_x).
$$

Como $x$ es cota superior, $s\le x$. Si $s<x$, la densidad racional produciría $q$ con

$$
s<\iota_F(q)<x.
$$

Entonces $q\in A_x$, de modo que $\iota_F(q)\in\iota_F(A_x)$, contradiciendo que $s$ sea cota superior. Por tanto

$$
\boxed{x=\sup_F\iota_F(A_x).}
$$

La completitud no fabrica la traza; garantiza que la información racional contenida en ella puede volver a reunirse en un elemento de $F$.

[]{#MA-MSOL-ANM-01-000-072}

[]{#MA-MIC-ANM-01-000-072}

### 72. Por qué $A_x=A_y$ obliga a $x=y$

Si

$$
A_x=A_y,
$$
\nentonces también

$$
\iota_F(A_x)=\iota_F(A_y).
$$

Aplicando la fórmula de reconstrucción a ambos elementos,

$$
x=\sup_F\iota_F(A_x)
=\sup_F\iota_F(A_y)=y.
$$

Por tanto

$$
\boxed{A_x=A_y\Longrightarrow x=y.}
$$

La traza racional determina al elemento de manera inyectiva: dos posiciones distintas no pueden tener exactamente los mismos racionales por debajo.

[]{#MA-MSOL-ANM-01-000-073}

[]{#MA-MIC-ANM-01-000-073}

### 73. Por qué $\mathbb Q$ sirve como interfaz común entre modelos distintos

Sean $F$ y $G$ cuerpos ordenados completos. Cada uno contiene su copia canónica de $\mathbb Q$,

$$
\iota_F:\mathbb Q\hookrightarrow F,
\qquad
\iota_G:\mathbb Q\hookrightarrow G.
$$

Para $x\in F$, su posición queda codificada por

$$
A_x=\{q\in\mathbb Q:\iota_F(q)<x\}\subseteq\mathbb Q.
$$

Análogamente, un elemento de $G$ posee una traza que también es un subconjunto del **mismo** conjunto $\mathbb Q$. Así, aunque los elementos de $F$ y $G$ sean objetos literalmente distintos, sus posiciones pueden describirse mediante datos que viven en un dominio común.

Además, en cada modelo completo la traza determina al elemento mediante un supremo. Por eso la estrategia de comparación puede ser

$$
\boxed{\text{elemento}\to\text{traza racional}\to\text{reconstrucción en el otro modelo}.}
$$

En §0.9 esto prepara el puente; todavía no construye el transporte $F\to G$, que pertenece a §0.10.

## §0.10. Únicos hasta isomorfismo

[]{#MA-MSOL-ANM-01-000-074}

[]{#MA-MIC-ANM-01-000-074}

[]{#MA-SEC-ANM-01-000-010}

### 74. Por qué hay que justificar el supremo antes de definir $\phi(x)$

La expresión

$$
\phi(x)=\sup_G\iota_G(A_x)
$$

sólo tiene sentido si el conjunto del que tomamos el supremo satisface las hipótesis de completitud: debe ser no vacío y estar acotado superiormente en $G$.

Como $A_x$ es una cortadura, $A_x\ne\varnothing$, luego $\iota_G(A_x)\ne\varnothing$. Además, como $A_x\ne\mathbb Q$, podemos elegir $u\notin A_x$. Para todo $q\in A_x$ se tiene $q<u$: si $q=u$ o $u<q$, la clausura inferior de $A_x$ obligaría a $u\in A_x$. Por tanto

$$
\iota_G(q)<\iota_G(u)
\qquad(q\in A_x),
$$

y $\iota_G(u)$ es una cota superior. Sólo después de estas dos verificaciones queda legítimamente definida

$$
\boxed{\phi(x)=\sup_G\iota_G(A_x).}
$$

[]{#MA-MSOL-ANM-01-000-075}

[]{#MA-MIC-ANM-01-000-075}

### 75. Dónde se usa exactamente la completitud de $G$

La completitud de $G$ se gasta una vez comprobado que

$$
\iota_G(A_x)\ne\varnothing
$$

y que este conjunto posee una cota superior en $G$. Entonces la propiedad del supremo garantiza la existencia de

$$
\boxed{\sup_G\iota_G(A_x).}
$$

Nada anterior en la construcción de $A_x$ o de la copia racional de $G$ necesita completitud. La hipótesis adicional de que $G$ es completo se usa precisamente para convertir la información racional transportada en un elemento concreto de $G$.

[]{#MA-MSOL-ANM-01-000-076}

[]{#MA-MIC-ANM-01-000-076}

### 76. Por qué $A_{\phi(x)}=A_x$ y dónde interviene que $A_x$ no tenga máximo

Sea

$$
S_x=\iota_G(A_x),
\qquad
\phi(x)=\sup_G S_x.
$$

Para probar $A_x\subseteq A_{\phi(x)}$, tomamos $q\in A_x$. Como $A_x$ **no tiene máximo**, existe $r\in A_x$ con $q<r$. Entonces

$$
\iota_G(q)<\iota_G(r)\le\phi(x),
$$

por lo que $\iota_G(q)<\phi(x)$ y $q\in A_{\phi(x)}$. La ausencia de máximo es exactamente lo que convierte la desigualdad no estricta $\iota_G(r)\le\phi(x)$ en una desigualdad estricta para $q$.

Para la otra inclusión, supongamos $q\in A_{\phi(x)}$ pero $q\notin A_x$. Todo $r\in A_x$ satisface $r<q$, luego $\iota_G(q)$ es cota superior de $S_x$. Por minimalidad del supremo,

$$
\phi(x)\le\iota_G(q),
$$

contradiciendo $\iota_G(q)<\phi(x)$. Por tanto

$$
\boxed{A_{\phi(x)}=A_x.}
$$

[]{#MA-MSOL-ANM-01-000-077}

[]{#MA-MIC-ANM-01-000-077}

### 77. De la igualdad de trazas al transporte exacto del orden

En §0.9 se demostró, dentro de cualquier cuerpo ordenado completo,

$$
x\le y
\Longleftrightarrow
A_x\subseteq A_y,
$$

y análogamente para el orden estricto mediante inclusión estricta.

Como

$$
A_{\phi(x)}=A_x,
\qquad
A_{\phi(y)}=A_y,
$$

tenemos

$$
x\le y
\Longleftrightarrow
A_x\subseteq A_y
\Longleftrightarrow
A_{\phi(x)}\subseteq A_{\phi(y)}
\Longleftrightarrow
\phi(x)\le\phi(y).
$$

Por tanto $\phi$ preserva y refleja el orden. En particular,

$$
\boxed{x<y\Longleftrightarrow\phi(x)<\phi(y).}
$$

[]{#MA-MSOL-ANM-01-000-078}

[]{#MA-MIC-ANM-01-000-078}

### 78. Por qué el transporte simétrico demuestra sobreyectividad sin elegir preimágenes

Intercambiamos los papeles de los cuerpos y definimos

$$
\psi:G\to F,
\qquad
\psi(y)=\sup_F\iota_F(A_y^G).
$$

La misma prueba da

$$
A_{\psi(y)}^F=A_y^G.
$$

Entonces, para $x\in F$,

$$
A_{\psi(\phi(x))}^F
=A_{\phi(x)}^G
=A_x^F,
$$

y la reconstrucción desde la traza fuerza

$$
\psi(\phi(x))=x.
$$

Simétricamente,

$$
\phi(\psi(y))=y
\qquad(y\in G).
$$

Así

$$
\boxed{\psi=\phi^{-1}},
$$

y $\phi$ es sobreyectiva. No se eligió una preimagen entre varias: la preimagen de $y$ está canónicamente determinada como $\psi(y)$.

[]{#MA-MSOL-ANM-01-000-079}

[]{#MA-MIC-ANM-01-000-079}

### 79. Por qué $\phi$ fija la copia racional

Para $q\in\mathbb Q$,

$$
A_{\iota_F(q)}
=\{r\in\mathbb Q:r<q\}
=q^*,
$$

porque $\iota_F$ preserva y refleja el orden. Del mismo modo,

$$
A_{\iota_G(q)}=q^*.
$$

Como $\phi$ conserva la traza,

$$
A_{\phi(\iota_F(q))}
=A_{\iota_F(q)}
=q^*
=A_{\iota_G(q)}.
$$

La traza determina al elemento en $G$, luego

$$
\boxed{\phi(\iota_F(q))=\iota_G(q).}
$$

Equivalente:

$$
\boxed{\phi\circ\iota_F=\iota_G.}
$$

En particular, $\phi(0_F)=0_G$ y $\phi(1_F)=1_G$.

[]{#MA-MSOL-ANM-01-000-080}

[]{#MA-MIC-ANM-01-000-080}

### 80. Caracterización racional de $A_{x+y}$ y las dos aplicaciones de densidad

Para $q\in\mathbb Q$,

$$
\boxed{
q\in A_{x+y}
\Longleftrightarrow
\exists r\in A_x\;\exists s\in A_y:\ q<r+s.
}
$$

Si $q\in A_{x+y}$, entonces

$$
\iota_F(q)-y<x.
$$

**Primera aplicación de densidad:** elegimos $r\in\mathbb Q$ con

$$
\iota_F(q)-y<\iota_F(r)<x.
$$

Así $r\in A_x$ y

$$
\iota_F(q)-\iota_F(r)<y.
$$

**Segunda aplicación de densidad:** elegimos $s\in\mathbb Q$ con

$$
\iota_F(q)-\iota_F(r)<\iota_F(s)<y.
$$

Entonces $s\in A_y$ y $q<r+s$.

La recíproca usa sólo preservación de suma y orden de la copia racional: si $r\in A_x$, $s\in A_y$ y $q<r+s$, entonces

$$
\iota_F(q)<\iota_F(r)+\iota_F(s)<x+y.
$$

[]{#MA-MSOL-ANM-01-000-081}

[]{#MA-MIC-ANM-01-000-081}

### 81. Por qué el criterio de producto se prueba primero para $x,y\ge0$

La multiplicación interactúa con el orden de forma uniforme sólo cuando controlamos los signos. Si

$$
0\le x,
\qquad
0\le y,
$$

entonces multiplicar o dividir desigualdades por $x$, $y$ o por racionales positivos no invierte el orden.

Eso permite caracterizar $A_{xy}$ mediante testigos racionales positivos:

$$
q\in A_{xy}
\Longleftrightarrow
q<0
\text{ o }
\exists r,s>0:
r\in A_x,
\ s\in A_y,
\ q<rs.
$$

Sin fijar primero los signos, una multiplicación por un factor negativo podría invertir desigualdades y el mismo criterio dejaría de ser válido. Por eso el argumento se establece primero en el cono no negativo y después se extiende algebraicamente al resto de los casos.

[]{#MA-MSOL-ANM-01-000-082}

[]{#MA-MIC-ANM-01-000-082}

### 82. Los tres casos adicionales de signo

El caso $x,y\ge0$ ya está probado. Quedan tres posibilidades.

1. Si $x<0\le y$, entonces $-x>0$ y
   $$
   xy=-((-x)y).
   $$
   Por preservación del opuesto y multiplicatividad en no negativos,
   $$
   \phi(xy)=\phi(x)\phi(y).
   $$
2. Si $x\ge0>y$, el argumento es simétrico usando $-y>0$.
3. Si $x<0$ y $y<0$, entonces $-x,-y>0$ y
   $$
   xy=(-x)(-y).
   $$
   Por el caso positivo y $\phi(-z)=-\phi(z)$,
   $$
   \phi(xy)=(-\phi(x))(-\phi(y))=\phi(x)\phi(y).
   $$

Así

$$
\boxed{\phi(xy)=\phi(x)\phi(y)}
$$

para todos $x,y\in F$.

[]{#MA-MSOL-ANM-01-000-083}

[]{#MA-MIC-ANM-01-000-083}

### 83. Por qué todo isomorfismo ordenado debe transportar la copia racional canónica

Sea

$$
T:F\to G
$$

un isomorfismo de cuerpos ordenados. Entonces

$$
T\circ\iota_F:\mathbb Q\to G
$$

es otra incrustación de cuerpos ordenados: preserva $0$, $1$, suma, producto y orden.

Pero §0.9 demostró que la incrustación racional en un cuerpo ordenado es única: debe enviar $1$ a $1_G$, con lo que fija numerales, enteros y fracciones. Por tanto

$$
\boxed{T\circ\iota_F=\iota_G.}
$$

Todo isomorfismo posible coincide sobre la copia racional canónica.

[]{#MA-MSOL-ANM-01-000-084}

[]{#MA-MIC-ANM-01-000-084}

### 84. Por qué la misma traza fuerza $T(x)=\phi(x)$

Para $q\in\mathbb Q$,

$$
q\in A_x
\Longleftrightarrow
\iota_F(q)<x.
$$

Como $T$ preserva y refleja el orden y satisface $T(\iota_F(q))=\iota_G(q)$,

$$
q\in A_x
\Longleftrightarrow
\iota_G(q)<T(x)
\Longleftrightarrow
q\in A_{T(x)}.
$$

Luego

$$
A_{T(x)}=A_x.
$$

El transporte canónico también satisface

$$
A_{\phi(x)}=A_x.
$$

Por tanto $A_{T(x)}=A_{\phi(x)}$. Como la traza racional determina al elemento de $G$,

$$
\boxed{T(x)=\phi(x).}
$$

Esto vale para todo $x$, así que $T=\phi$.

[]{#MA-MSOL-ANM-01-000-085}

[]{#MA-MIC-ANM-01-000-085}

### 85. Igualdad literal, isomorfía y unicidad del isomorfismo

Son tres afirmaciones distintas.

- **Igualdad literal:** $F=G$ significa que ambos modelos son exactamente el mismo conjunto con las mismas operaciones. No se exige ni se demuestra.
- **Existencia de un isomorfismo:** $F\cong G$ afirma que existe una biyección que preserva las operaciones y el orden. Esto demuestra equivalencia estructural.
- **Existencia de un único isomorfismo de cuerpos ordenados:** además de existir, esa correspondencia está completamente forzada por la estructura; cualquier isomorfismo $T:F\to G$ coincide con $\phi$.

El resultado del capítulo es la tercera afirmación:

$$
\boxed{\text{entre dos cuerpos ordenados completos existe un único isomorfismo de cuerpos ordenados}.}
$$

[]{#MA-MSOL-ANM-01-000-086}

[]{#MA-MIC-ANM-01-000-086}

### 86. Por qué unicidad estructural no implica computabilidad

La construcción

$$
x\mapsto A_x\mapsto \iota_G(A_x)\mapsto\sup_G\iota_G(A_x)
$$

determina matemáticamente un único valor $\phi(x)$. Eso es una afirmación de **existencia y unicidad** dentro de la teoría.

Un algoritmo, en cambio, requiere representaciones efectivas de los elementos, procedimientos para decidir o enumerar la información racional relevante y un método computable para obtener el supremo correspondiente.

Nada de la prueba estructural proporciona automáticamente esos datos para representaciones arbitrarias de $F$ y $G$. Por tanto

$$
\boxed{\text{canónico por unicidad}\ne\text{computable por sí solo}.}
$$

[]{#MA-MSOL-ANM-01-000-087}

[]{#MA-MIC-ANM-01-000-087}

### 87. Las cortaduras como realización, no como esencia conjuntista

Las cortaduras de Dedekind proporcionan un modelo concreto

$$
\mathcal D
$$

que satisface la especificación de cuerpo ordenado completo. Por eso prueban **existencia**.

Pero §0.10 muestra que cualquier otro cuerpo ordenado completo $F$ está relacionado con $\mathcal D$ —y con cualquier otro modelo $G$— por un único isomorfismo de cuerpos ordenados. Los elementos subyacentes pueden ser objetos conjuntistas completamente distintos.

Por tanto lo que queda fijado matemáticamente no es una codificación concreta, sino la estructura compartida:

$$
\boxed{
\text{cuerpo ordenado completo, canónico hasta único isomorfismo}.
}
$$

Las cortaduras son una realización especialmente útil de esa estructura; no son una afirmación de que los reales deban ser, «por esencia», subconjuntos de $\mathbb Q$.

[Índice del libro](../para-matematicos/analisis-para-matematicos.md) · [Capítulo 0](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales.md) · [Ejercicios](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-ejercicios.md) · [Soluciones](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-soluciones.md) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-0-construir-los-numeros-reales-microcontroles.md)

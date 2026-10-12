---
content-id: MA-BCH-0238
content-type: book-chapter
collection: PM-ANA
editorial-project: ANM
editorial-id: MA-BCH-ANM-01-009
book-id: MA-BOK-0010
status: published
solution-status: complete
date-created: '2026-10-11'
areas:
- analisis
level: universitario
topics:
- analisis-real
prerequisites: []
related:
- MA-BOK-0010
license: GFDL-1.3-or-later
title: 'Capítulo 9 — Límite superior e inferior: las envolventes de una cola'
date-modified: '2026-10-11'
provenance:
  type: original
  sources:
  - ANM-C09.md, manuscrito canónico ANM auditado; ANM-FINAL_GLOBAL_QA_v01.
css: ../../assets/books/anm/reader.css
---

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)

Una sucesión acotada puede seguir oscilando. Queremos identificar dos fronteras que sobrevivan al retirar cualquier prefijo, y relacionarlas con los destinos de sus extracciones. No basta el supremo de la imagen completa: una única altura inicial puede dominarlo. Miraremos los conjuntos de valores de cola y construiremos dos sucesiones nuevas que sí tienen dirección monótona.

La ruta será cola, supremo e ínfimo de cola, envolventes monótonas y límites de esas envolventes. Después construiremos extracciones que alcancen las fronteras como límites, mediremos la oscilación y estudiaremos qué operaciones conservan o comparan los extremos. Usaremos orden y sup/inf de C02, completitud de C03, colas de C05 y las herramientas de C06–C08. Todo el capítulo desarrolla la teoría real finita de sucesiones acotadas; no introduce una extensión implícita a valores infinitos.

## 9.1. Conservar la cola y olvidar el prefijo

[]{#MA-SEC-ANM-01-009-001}

Una altura excepcional puede dominar la imagen completa sin describir lo que sucede después. Si $a_0=10$ y $a_n=0$ para $n\ge1$, el supremo de la imagen es diez y el límite es cero. Queremos conservar las fronteras que sobreviven al avanzar el corte temporal.

Fijemos una sucesión real acotada $a:\mathbb N\to\mathbb R$, con $\mathbb N=\{0,1,2,\ldots\}$. Para $N\in\mathbb N$, su conjunto de valores de cola es $T_N=\{a_n:n\ge N\}$. El conjunto de índices $\{n:n\ge N\}$ vive en $\mathbb N$; $T_N$ vive en $\mathbb R$. La sucesión conserva multiplicidades y orden; el conjunto de valores los olvida. En particular, $T_N$ puede ser un singleton aunque haya infinitos índices disponibles.

Cada $T_N$ contiene $a_N$ y es acotado. La completitud asegura los reales

$$
\ell_N=\inf T_N,\qquad u_N=\sup T_N.
$$

Para todo $n\ge N$ se cumple $\ell_N\le a_n\le u_N$. Las funciones $\ell,u:\mathbb N\to\mathbb R$ son nuevas sucesiones, llamadas **envolventes inferior y superior**. No son en general subsucesiones de $a$: sus valores pueden no aparecer nunca entre los términos.

**La propiedad que necesitaremos.** Para cada corte $N$ y cada $\eta>0$ existen $p,q\ge N$ con $\ell_N\le a_p<\ell_N+\eta$ y $u_N-\eta<a_q\le u_N$. Veamos por qué. Si ningún término de la cola superara $u_N-\eta$, ese número sería una cota superior de $T_N$ menor que su supremo. Esto contradice la definición de supremo. Si ningún término fuera menor que $\ell_N+\eta$, ese número sería una cota inferior mayor que el ínfimo. Los valores obtenidos pertenecen a $T_N$ y, por su definición, tienen índices al menos $N$. No hemos supuesto que los extremos se alcancen, ni elegido aún testigos para todos los pares $(N,\eta)$.

En $a_n=1/(n+1)$ tenemos $u_N=1/(N+1)$, alcanzado en $N$, y $\ell_N=0$, no alcanzado. Cero es cota inferior; cualquier número positivo deja de ser cota inferior por arquimedianidad. Para la sucesión del prefijo excepcional, $u_0=10$ y $u_N=0$ desde $N=1$, mientras que $\ell_N=0$ siempre. La frontera de una cola debe leerse con su corte, no sólo con la lista de alturas de la imagen total.

![El valor inicial diez determina el supremo total, pero desaparece del conjunto de valores de cola desde el corte uno.](../../assets/books/anm/C09/C09-F01.svg){#fig-anm-c09-f01 fig-alt="El valor inicial diez determina el supremo total, pero desaparece del conjunto de valores de cola desde el corte uno."}

### Antes de seguir

[]{#MA-MIC-ANM-01-009-001}

1. ¿En qué conjuntos viven el corte $N$ y los valores de $T_N$?

[]{#MA-MIC-ANM-01-009-002}

2. ¿Por qué $T_N$ no es vacío?

[]{#MA-MIC-ANM-01-009-003}

3. ¿Qué hipótesis permite que $\ell_N$ y $u_N$ sean reales?

[]{#MA-MIC-ANM-01-009-004}

4. ¿Debe $u_N$ ser uno de los términos de la cola?

[]{#MA-MIC-ANM-01-009-005}

5. Calcula $\ell_N$ y $u_N$ para $a_n=1/(n+1)$.

[]{#MA-MIC-ANM-01-009-006}

6. ¿Qué contradicción aparece si todos los términos de la cola satisfacen $a_n\le u_N-\eta$ con $\eta>0$?

[]{#MA-MIC-ANM-01-009-007}

7. ¿Una cola constante tiene infinitos valores distintos?

[]{#MA-MIC-ANM-01-009-008}

8. Para $a_0=10$ y $a_n=0$ si $n\ge1$, ¿cuándo cambia el supremo de cola?

## 9.2. Dos envolventes que sí tienen dirección

[]{#MA-SEC-ANM-01-009-002}

La sucesión original puede saltar en ambas direcciones. Sus envolventes tienen una dirección obligada: al descartar términos, no creamos alturas nuevas. Como $T_{N+1}\subseteq T_N$, toda cota superior de $T_N$ sigue siendo cota de $T_{N+1}$ y toda cota inferior sigue siéndolo. Las propiedades de supremo e ínfimo dan

$$
\ell_N\le\ell_{N+1}\le u_{N+1}\le u_N.
$$

Si $m\le a_n\le M$ para todo $n$, también $m\le\ell_N\le u_N\le M$. C07 permite concluir que ambas envolventes convergen. Definimos

$$
\alpha=\liminf_{n\to\infty}a_n:=\lim_{N\to\infty}\ell_N=\sup_{N\in\mathbb N}\ell_N,
\qquad
\beta=\limsup_{n\to\infty}a_n:=\lim_{N\to\infty}u_N=\inf_{N\in\mathbb N}u_N.
$$

El supremo exterior se aplica al recorrido de $\ell$ y el ínfimo exterior al recorrido de $u$. No podemos intercambiar estas operaciones: $\sup_N\sup T_N=u_0$ describiría el supremo total, no la frontera persistente. La existencia usa completitud dos veces: primero en cada conjunto de cola; después, mediante convergencia monótona, en el conjunto de valores de cada envolvente. Unicidad de límites de C06 hace unívocas las definiciones.

Por conservación del orden bajo límites, $\alpha\le\beta$. Además, $\ell_N\le\alpha$ y $\beta\le u_N$ para todo $N$. Esto no afirma $\alpha\le a_n\le\beta$ para todo $n$, ni siquiera para toda una cola. Los extremos de las envolventes pueden seguir fuera del intervalo final durante cualquier tiempo finito.

Tomemos $a_n=(-1)^n(1+1/(n+1))$. Sea $e(N)$ el menor índice par al menos $N$ y $o(N)$ el menor impar al menos $N$. Entonces $u_N=1+1/(e(N)+1)$ y $\ell_N=-1-1/(o(N)+1)$. Los términos pares positivos disminuyen y los impares negativos aumentan; por eso sus primeros índices disponibles dan los extremos. Como $e(N),o(N)\ge N$, las dos correcciones tienden a cero, de modo que $\alpha=-1$ y $\beta=1$. Todos los términos quedan fuera de $[-1,1]$, aunque las fronteras asintóticas sean precisamente esos extremos.

La nueva herramienta no fuerza convergencia de $a$. Hace converger las dos sucesiones que delimitan sus colas. Visualmente obtenemos dos movimientos monótonos a partir de una oscilación.

![La sucesión alterna fuera de la banda final; sus envolventes avanzan monótonamente hacia menos uno y uno sin exigir que los términos entren en esa banda exacta.](../../assets/books/anm/C09/C09-F02.svg){#fig-anm-c09-f02 fig-alt="La sucesión alterna fuera de la banda final; sus envolventes avanzan monótonamente hacia menos uno y uno sin exigir que los términos entren en esa banda exacta."}

### Antes de seguir

[]{#MA-MIC-ANM-01-009-009}

1. ¿Cuál es la inclusión entre $T_{N+1}$ y $T_N$?

[]{#MA-MIC-ANM-01-009-010}

2. ¿En qué sentido es monótona la envolvente inferior?

[]{#MA-MIC-ANM-01-009-011}

3. ¿En qué sentido es monótona la envolvente superior?

[]{#MA-MIC-ANM-01-009-012}

4. Escribe el supremo exterior que define $\alpha$.

[]{#MA-MIC-ANM-01-009-013}

5. Escribe el ínfimo exterior que define $\beta$.

[]{#MA-MIC-ANM-01-009-014}

6. ¿Por qué $\alpha\le\beta$?

[]{#MA-MIC-ANM-01-009-015}

7. Para $a_n=(-1)^n(1+1/(n+1))$, ¿cuáles son los extremos asintóticos?

[]{#MA-MIC-ANM-01-009-016}

8. ¿El ejemplo anterior tiene términos en $[\alpha,\beta]$?

## 9.3. Fronteras eventuales y visitas tardías

[]{#MA-SEC-ANM-01-009-003}

¿Cómo se reconoce $\beta$ sin calcular todos los supremos? Necesitamos dos condiciones: ninguna altura persistentemente mayor puede sobrevivir y los términos siguen llegando cerca de la frontera desde abajo. Para una sucesión acotada, un real $b$ es su límite superior si y sólo si

$$
\forall\varepsilon>0\ \exists N\ \forall n\ge N: a_n<b+\varepsilon,
\qquad
\forall\varepsilon>0\ \forall K\ \exists n\ge K: a_n>b-\varepsilon.
$$

**Del límite superior a las condiciones.** La convergencia $u_N\to\beta$ da un corte con $u_N<\beta+\varepsilon$; entonces toda su cola queda por debajo. Para cualquier corte $K$, la aproximación del supremo da $a_n>u_K-\varepsilon\ge\beta-\varepsilon$ para algún $n\ge K$. La segunda condición permite un índice distinto para cada tolerancia y corte; no exige que toda la cola se acerque a $\beta$.

**De las condiciones al límite superior.** La primera da $u_N\le b+\varepsilon$ para algún corte, pues una cota estricta término a término puede pasar a no estricta al tomar supremo. Así $\beta\le b+\varepsilon$. La segunda obliga a $u_K>b-\varepsilon$ para cada $K$; al tomar límite, $\beta\ge b-\varepsilon$. Como esto vale para toda tolerancia positiva, $\beta=b$: si fueran diferentes, la mitad de su distancia contradiría una de esas desigualdades.

La caracterización inferior es dual y conviene conservarla completa: $c=\alpha$ si y sólo si, para cada $\varepsilon>0$, todos los términos de alguna cola satisfacen $a_n>c-\varepsilon$, y para todo corte $K$ existe $n\ge K$ con $a_n<c+\varepsilon$. En efecto, $\ell_N\to\alpha$ prueba la primera condición y la aproximación del ínfimo la segunda. Recíprocamente, la primera implica $\alpha\ge c-\varepsilon$ y la segunda $\ell_K<c+\varepsilon$ para cada $K$, luego $\alpha\le c+\varepsilon$. La misma prueba por distancia da $\alpha=c$.

Un conjunto de índices supera cualquier corte exactamente cuando es infinito, porque un prefijo natural es finito y cualquier conjunto finito de naturales tiene cota. Por tanto, «arbitrariamente tarde» equivale aquí a «para infinitos índices». Repetir un mismo valor en esos índices está permitido.

Dos consecuencias útiles fijan el significado de frontera. Si $t>\beta$, sólo hay finitos índices con $a_n\ge t$: usar $\varepsilon=(t-\beta)/2$ en la primera condición. Si $t<\beta$, hay infinitos índices con $a_n>t$: usar $\varepsilon=\beta-t$ en la segunda. Para $t=\beta$, ambas posibilidades existen; la sucesión constante uno alcanza su frontera siempre, mientras $1-1/(n+1)$ no la alcanza nunca. Dualmente, por debajo de $\alpha$ sólo puede haber finitas visitas y por encima de $\alpha$ hay infinitas visitas inferiores al umbral.

Al combinar las dos cotas eventuales, para cada $\varepsilon>0$ alguna cola queda dentro de $(\alpha-\varepsilon,\beta+\varepsilon)$. Esta es la banda que podemos garantizar. El intervalo exacto $[\alpha,\beta]$ puede seguir sin contener ningún término, como vimos antes.

![Desde el corte cuatro todos los términos quedan bajo cinco cuartos. Después del corte nueve, el término de índice diez visita la ventana de radio un cuarto de la frontera superior; los términos negativos siguen fuera de ella.](../../assets/books/anm/C09/C09-F03.svg){#fig-anm-c09-f03 fig-alt="Desde el corte cuatro todos los términos quedan bajo cinco cuartos. Después del corte nueve, el término de índice diez visita la ventana de radio un cuarto de la frontera superior; los términos negativos siguen fuera de ella."}

### Antes de seguir

[]{#MA-MIC-ANM-01-009-017}

1. ¿Qué orden de cuantificadores expresa una cota superior eventual con tolerancia $\varepsilon$?

[]{#MA-MIC-ANM-01-009-018}

2. ¿Qué orden de cuantificadores expresa visitas tardías cerca de $\beta$ desde abajo?

[]{#MA-MIC-ANM-01-009-019}

3. ¿La condición de visitas obliga a que toda la cola esté cerca de $\beta$?

[]{#MA-MIC-ANM-01-009-020}

4. ¿Qué ocurre con las visitas a alturas al menos $t$ si $t>\beta$?

[]{#MA-MIC-ANM-01-009-021}

5. ¿Qué ocurre si $t<\beta$ con los índices que cumplen $a_n>t$?

[]{#MA-MIC-ANM-01-009-022}

6. ¿Se puede decidir sólo con $\beta$ si hay infinitos índices con $a_n=\beta$?

[]{#MA-MIC-ANM-01-009-023}

7. Escribe las dos condiciones que caracterizan $\alpha$.

[]{#MA-MIC-ANM-01-009-024}

8. ¿Qué banda abierta contiene alguna cola para cada $\varepsilon>0$?

## 9.4. Alcanzar las fronteras mediante extracciones

[]{#MA-SEC-ANM-01-009-004}

Las fronteras existen, pero aún debemos relacionarlas con los destinos de C08. Demostraremos que $\alpha$ y $\beta$ son respectivamente el mínimo y el máximo del conjunto de límites de subsucesiones, que denotaremos $\operatorname{LimSub}(a)$. Primero construiremos dos extracciones; después confinaremos cualquier otra.

**Construir la extracción superior.** Para cualquier $\delta>0$ y corte $K$, hay un término posterior con $|a_n-\beta|<\delta$. Para verlo, escogemos primero un corte $H$ desde el cual $a_n<\beta+\delta$; luego la condición de visitas, aplicada al corte $\max\{H,K\}$, da un término con $a_n>\beta-\delta$. Ambas restricciones se cumplen en el mismo índice. Esa coordinación es el paso decisivo: una visita por un solo lado no bastaría.

Definimos $n_0$ como el mínimo del conjunto no vacío $\{n:|a_n-\beta|<1\}$. Una vez definido $n_{k-1}$, para $k\ge1$ ponemos

$$
n_k=\min\{n\ge n_{k-1}+1:|a_n-\beta|<1/(k+1)\}.
$$

La propiedad anterior demuestra la no vacuidad antes de tomar cada mínimo. La recursión produce un selector estrictamente creciente $k\mapsto n_k$; no requiere escoger un mínimo real ni testigos arbitrarios. Además $|a_{n_k}-\beta|<1/(k+1)$. Para $\varepsilon>0$, la propiedad arquimediana da $K$ con $1/(K+1)<\varepsilon$; todo $k\ge K$ satisface el error requerido. Así $a_{n_k}\to\beta$ con dominio nuevo $\mathbb N$ y codominio $\mathbb R$.

**Construir la extracción inferior.** Para $\delta,K$ fijos, la cota eventual $a_n>\alpha-\delta$ y la visita $a_n<\alpha+\delta$ después del máximo de los cortes dan $|a_n-\alpha|<\delta$. Definimos $m_0=\min\{n:|a_n-\alpha|<1\}$ y, para $k\ge1$, $m_k=\min\{n\ge m_{k-1}+1:|a_n-\alpha|<1/(k+1)\}$. Los conjuntos son no vacíos; el selector aumenta y la misma estimación arquimediana prueba $a_{m_k}\to\alpha$.

**Confinar otros destinos.** Si $a_{\varphi(k)}\to x$ con $\varphi$ estrictamente creciente, C08 da $\varphi(k)\ge k$. Para cada corte fijo $N$, todos los $k\ge N$ cumplen $\ell_N\le a_{\varphi(k)}\le u_N$. Pasando al límite en $k$, obtenemos $\ell_N\le x\le u_N$. Ahora dejamos variar $N$ y pasamos al límite en las envolventes: $\alpha\le x\le\beta$. Son dos pasos de límite con dominios diferentes; no se sustituye un índice infinito en una fórmula.

Los extremos pertenecen al conjunto de destinos y acotan a todos sus elementos. Por ello

$$
\min\operatorname{LimSub}(a)=\alpha,\qquad
\max\operatorname{LimSub}(a)=\beta.
$$

En la alternancia cero–uno los destinos son exactamente $\{0,1\}$: las selecciones de pares e impares los alcanzan, y ningún otro real puede ser límite, porque está a distancia positiva del conjunto finito de valores. El intervalo $[0,1]$ es la envolvente de esos destinos, no el conjunto completo de ellos. La construcción que acabamos de realizar ofrece candidatos concretos y demuestra su convergencia; Bolzano–Weierstrass queda disponible como contraste, pero no sustituye ninguno de esos pasos.

![La selección par conserva valores y cambia el dominio de lectura al índice k. Sus términos se acercan a uno, aunque ningún término seleccionado vale uno.](../../assets/books/anm/C09/C09-F04.svg){#fig-anm-c09-f04 fig-alt="La selección par conserva valores y cambia el dominio de lectura al índice k. Sus términos se acercan a uno, aunque ningún término seleccionado vale uno."}

| Índice nuevo k | Índice original φ(k) | Valor seleccionado |
|---|---|---|
| 0 | 0 | 2 |
| 1 | 2 | 4/3 |
| 2 | 4 | 6/5 |
| 3 | 6 | 8/7 |
| 4 | 8 | 10/9 |
| 5 | 10 | 12/11 |

### Antes de seguir

[]{#MA-MIC-ANM-01-009-025}

1. ¿Qué dos restricciones se coordinan antes de elegir un índice próximo a $\beta$?

[]{#MA-MIC-ANM-01-009-026}

2. ¿Por qué existe el mínimo que define $n_0$?

[]{#MA-MIC-ANM-01-009-027}

3. ¿Qué evita que $n_k$ repita un índice previo?

[]{#MA-MIC-ANM-01-009-028}

4. ¿Por qué usamos $1/(k+1)$ en vez de $1/k$?

[]{#MA-MIC-ANM-01-009-029}

5. ¿En qué dominio vive el selector $k\mapsto n_k$?

[]{#MA-MIC-ANM-01-009-030}

6. ¿Cómo demuestra $|a_{n_k}-\beta|<1/(k+1)$ la convergencia?

[]{#MA-MIC-ANM-01-009-031}

7. ¿Qué desigualdad satisface cualquier límite $x$ de subsucesión?

[]{#MA-MIC-ANM-01-009-032}

8. ¿Por qué $\beta$ es máximo de $\operatorname{LimSub}(a)$ y no sólo su supremo?

## 9.5. Medir la oscilación y reconocer convergencia

[]{#MA-SEC-ANM-01-009-005}

Las dos fronteras permiten recuperar la convergencia ordinaria. Para una sucesión real acotada,

$$
a_n\to L\quad\Longleftrightarrow\quad\alpha=\beta=L.
$$

Si $a_n\to L$, las dos extracciones construidas en §9.4 deben converger a $L$ por C08; unicidad identifica $\alpha=\beta=L$. Para la vuelta no basta decir que las fronteras coinciden: debemos controlar toda la cola. Si $\alpha=\beta=L$ y $\varepsilon>0$, la convergencia de las envolventes da cortes $N_1,N_2$ desde los cuales $\ell_n>L-\varepsilon$ y $u_n<L+\varepsilon$, respectivamente. Con $N=\max\{N_1,N_2\}$, todo $n\ge N$ cumple $L-\varepsilon<\ell_n\le a_n\le u_n<L+\varepsilon$. Esto prueba $|a_n-L|<\varepsilon$ con el orden correcto de elecciones.

Podemos medir lo que queda de la oscilación mediante $d_N=u_N-\ell_N\ge0$. Como $u$ decrece y $\ell$ crece, $d$ decrece. Las reglas de límites reales de C06 dan $d_N\to\beta-\alpha$. Llamaremos **oscilación asintótica** al número $\omega(a)=\beta-\alpha$. Así $\omega(a)=0$ si y sólo si $a$ converge. El número cero registra desaparición de amplitud, aunque los términos alternen de lado para siempre.

La anchura tiene una interpretación independiente de que se alcancen los extremos:

$$
d_N=\sup\{|a_p-a_q|:p,q\ge N\}.
$$

Todo par de términos está en $[\ell_N,u_N]$, luego su distancia es a lo sumo $d_N$. Para comprobar que ninguna cota menor sirve, fijemos $\eta>0$. La aproximación de §9.1 ofrece $a_p>u_N-\eta/2$ y $a_q<\ell_N+\eta/2$, ambos en la cola. Entonces $|a_p-a_q|\ge a_p-a_q>d_N-\eta$. El conjunto de distancias es no vacío y acotado, y estas dos propiedades identifican su supremo. Los índices pueden depender de $\eta$ y $N$; no afirmamos que el supremo de distancias sea un máximo.

En $a_n=(-1)^n/(n+1)$ la envolvente superior es $1/(e(N)+1)$ y la inferior es $-1/(o(N)+1)$. Su anchura tiende a cero y la sucesión converge a cero, aunque no sea monótona. En la alternancia cero–uno, en cambio, $d_N=1$ siempre. La monotonía de las envolventes puede convivir con una anchura persistente.

Esta sección añade un diagnóstico geométrico de convergencia. Hemos probado sus equivalencias usando las fronteras ya construidas. La relación con una condición interna de proximidad entre términos se desarrollará con su propia arquitectura en el capítulo siguiente; no necesitamos anticiparla para cerrar estas pruebas.

![La anchura de las colas amortiguadas tiende a cero; la de la alternancia cero–uno permanece en uno. Ambas envolventes son monótonas, pero sólo la primera pareja se reúne.](../../assets/books/anm/C09/C09-F05.svg){#fig-anm-c09-f05 fig-alt="La anchura de las colas amortiguadas tiende a cero; la de la alternancia cero–uno permanece en uno. Ambas envolventes son monótonas, pero sólo la primera pareja se reúne."}

### Antes de seguir

[]{#MA-MIC-ANM-01-009-033}

1. ¿Qué concluyes si $\alpha=\beta=L$?

[]{#MA-MIC-ANM-01-009-034}

2. ¿Qué concluyes sobre los extremos si $a_n\to L$?

[]{#MA-MIC-ANM-01-009-035}

3. ¿Cómo se define la anchura $d_N$?

[]{#MA-MIC-ANM-01-009-036}

4. ¿Por qué $d_N$ no aumenta?

[]{#MA-MIC-ANM-01-009-037}

5. ¿Cuál es el límite de $d_N$?

[]{#MA-MIC-ANM-01-009-038}

6. ¿Debe la máxima distancia entre dos términos de una cola existir?

[]{#MA-MIC-ANM-01-009-039}

7. Calcula la oscilación asintótica de la alternancia cero–uno.

[]{#MA-MIC-ANM-01-009-040}

8. ¿Oscilar de lado para siempre impide converger?

## 9.6. Cambiar términos sin cambiar las fronteras

[]{#MA-SEC-ANM-01-009-006}

Un objeto asintótico debería ignorar un prefijo finito. Si $a_n=b_n$ para $n\ge N_0$, entonces $T_N(a)=T_N(b)$ para todo $N\ge N_0$. Sus supremos e ínfimos coinciden desde ese corte, por lo que los respectivos límites coinciden. Modificar finitos términos de una sucesión acotada conserva la acotación: se incorpora a la cota la máxima magnitud de los nuevos valores, un conjunto finito. Por tanto, esa modificación conserva $\alpha$, $\beta$ y $\omega$ aunque cambie el supremo de la imagen total.

También podemos desplazar el origen temporal. Para $r\in\mathbb N$ fijo, definamos $b_k=a_{k+r}$. Tenemos $T_K(b)=T_{K+r}(a)$, de modo que $\ell_K(b)=\ell_{K+r}(a)$ y $u_K(b)=u_{K+r}(a)$. Las colas de las envolventes convergen a sus mismos límites por C06. Suprimir un prefijo y reindexar desde cero conserva los extremos; esta operación es distinta de modificar sólo el valor de un término.

**Estabilidad ante un error que desaparece.** Supongamos que $a$ es acotada y $b_n-a_n\to0$. La diferencia es acotada por C06; por desigualdad triangular $b$ también es acotada. Para $\varepsilon>0$ existe $N_0$ con $|b_n-a_n|<\varepsilon$ para $n\ge N_0$. Si $N\ge N_0$, entonces, para todo $n\ge N$,

$$
\ell_N(a)-\varepsilon\le b_n\le u_N(a)+\varepsilon,
\qquad
\ell_N(b)-\varepsilon\le a_n\le u_N(b)+\varepsilon.
$$

Tomando extremos de cola, obtenemos $u_N(b)\le u_N(a)+\varepsilon$ y $u_N(a)\le u_N(b)+\varepsilon$; además $\ell_N(b)\ge\ell_N(a)-\varepsilon$ y $\ell_N(a)\ge\ell_N(b)-\varepsilon$. Al pasar al límite en $N$, resulta $|\beta(b)-\beta(a)|\le\varepsilon$ y $|\alpha(b)-\alpha(a)|\le\varepsilon$. La tolerancia es arbitraria, así que ambas diferencias son cero. No suponemos que el error se anule exactamente en una cola.

En particular, $(-1)^n+1/(n+1)$ conserva los extremos $-1,1$ de $(-1)^n$. Una perturbación pequeña en el límite conserva las fronteras y la oscilación, pero puede cambiar todos los términos. Más generalmente, la misma prueba muestra que, si $|a_n-b_n|\le\delta$ eventualmente para una constante $\delta\ge0$, los respectivos extremos difieren a lo sumo en $\delta$. Para trasladar por una constante exacta, los conjuntos de cola se trasladan: $\ell_N(a+c)=\ell_N(a)+c$ y $u_N(a+c)=u_N(a)+c$, pues la traducción preserva cotas y su optimalidad. Por ello ambos extremos aumentan en $c$.

Conviene conservar las hipótesis: cambiar infinitos términos sin control puede cambiar ambas fronteras. En la alternancia cero–uno, reemplazar todos los unos por cero produce una sucesión constante. La infinitud del conjunto de cambios no decide por sí sola el efecto; lo decide su comportamiento en la cola.

### Antes de seguir

[]{#MA-MIC-ANM-01-009-041}

1. ¿Qué ocurre con $\alpha,\beta$ si se cambian finitos términos?

[]{#MA-MIC-ANM-01-009-042}

2. ¿Qué conjunto de cola tiene $b_k=a_{k+r}$?

[]{#MA-MIC-ANM-01-009-043}

3. ¿Por qué $b$ es acotada si $a$ lo es y $b_n-a_n\to0$?

[]{#MA-MIC-ANM-01-009-044}

4. ¿Qué cota de $u_N(b)$ obtienes de $|a_n-b_n|<\varepsilon$ para todo $n\ge N$?

[]{#MA-MIC-ANM-01-009-045}

5. ¿Por qué se comparan las envolventes también intercambiando $a$ y $b$?

[]{#MA-MIC-ANM-01-009-046}

6. Calcula los extremos de $a_n=(-1)^n+1/(n+1)$.

[]{#MA-MIC-ANM-01-009-047}

7. ¿Qué hace una traslación constante $c$ a los extremos?

[]{#MA-MIC-ANM-01-009-048}

8. ¿Modificar infinitos términos obliga a cambiar los extremos?

## 9.7. Comparar y combinar comportamientos

[]{#MA-SEC-ANM-01-009-007}

En esta sección $a$ y $b$ son sucesiones reales acotadas. Escribiremos $\alpha_a,\beta_a$ y $\alpha_b,\beta_b$ para sus extremos. Si $a_n\le b_n$ eventualmente, para toda cola posterior $u_N(a)\le u_N(b)$: cada $a_n$ está por debajo de $b_n\le u_N(b)$. También $\ell_N(a)\le\ell_N(b)$, porque $\ell_N(a)\le a_n\le b_n$ para todos los índices de la cola y por tanto $\ell_N(a)$ es cota inferior de los valores de $b$. Pasando al límite,

$$
\alpha_a\le\alpha_b,\qquad\beta_a\le\beta_b.
$$

Una desigualdad estricta entre términos puede dar igualdad en sus extremos. Por ejemplo, $0<1/(n+1)$ en todos los índices, pero ambos límites superiores valen cero.

**Cambiar la escala.** Si $c>0$, la multiplicación preserva orden y optimalidad de cotas, luego $\ell_N(ca)=c\ell_N(a)$ y $u_N(ca)=cu_N(a)$. Si $c<0$, invierte el orden: $\ell_N(ca)=cu_N(a)$ y $u_N(ca)=c\ell_N(a)$. Para justificar optimalidad en este caso, una cota inferior de $cT_N$ dividida por $c$ es cota superior de $T_N$, y una cota superior dividida por $c$ es cota inferior. Al pasar al límite se obtienen las mismas fórmulas para $\alpha,\beta$. Si $c=0$, ambas fronteras son cero. En particular, $\alpha(-a)=-\beta_a$ y $\beta(-a)=-\alpha_a$.

**Sumar sin sincronizar extremos.** La suma es acotada, y para todo $n\ge N$ se cumple $\ell_N(a)+\ell_N(b)\le a_n+b_n\le u_N(a)+u_N(b)$. Los dos términos extremos del lado derecho pueden provenir de índices diferentes. Tomando extremos y luego límites,

$$
\alpha_a+\alpha_b\le\alpha(a+b)\le\beta(a+b)\le\beta_a+\beta_b.
$$

La igualdad general sería falsa. Para $a_n=(-1)^n$ y $b_n=-a_n$, ambas sucesiones tienen extremos $-1,1$, mientras su suma es cero. Los máximos de una aparecen cuando la otra está en sus mínimos. En cambio, si $b_n\to B$, escribimos $a_n+b_n=(a_n+B)+(b_n-B)$. La traslación y la estabilidad de §9.6 dan $\alpha(a+b)=\alpha_a+B$ y $\beta(a+b)=\beta_a+B$. Una de las dos convergencias ordinarias basta para recuperar la igualdad.

**Producto con signo controlado.** Si además $a_n,b_n\ge0$ para todos los índices, todos los extremos de cola son no negativos. Podemos multiplicar las cotas:

$$
\ell_N(a)\ell_N(b)\le a_nb_n\le u_N(a)u_N(b).
$$

El producto es acotado y las reglas de límites de C06 dan $\alpha(ab)\ge\alpha_a\alpha_b$ y $\beta(ab)\le\beta_a\beta_b$. También vale si los factores son eventualmente no negativos, aplicando el razonamiento sólo a las colas posteriores. Sin esa hipótesis las fórmulas pueden fallar. En concreto, $a_n=b_n\in\{-2,-1\}$ alternando da $\beta(ab)=4>1=\beta_a\beta_b$. No trasladamos al producto una desigualdad diseñada para factores no negativos.

Las reglas se convierten en herramientas después de verificar acotación, signo y sincronización. El retorno visual explica por qué sumar dos fronteras superiores produce una cota, aunque ninguna suma de términos alcance esa altura.

![Los máximos de los sumandos ocurren en paridades opuestas. La suma es cero en cada índice, por debajo de la suma dos de sus fronteras superiores.](../../assets/books/anm/C09/C09-F06.svg){#fig-anm-c09-f06 fig-alt="Los máximos de los sumandos ocurren en paridades opuestas. La suma es cero en cada índice, por debajo de la suma dos de sus fronteras superiores."}

### Antes de seguir

[]{#MA-MIC-ANM-01-009-049}

1. Si $a_n\le b_n$ eventualmente, ¿qué orden tienen sus extremos?

[]{#MA-MIC-ANM-01-009-050}

2. ¿Una desigualdad estricta entre términos obliga a desigualdad estricta entre extremos?

[]{#MA-MIC-ANM-01-009-051}

3. ¿Qué ocurre al multiplicar por una constante positiva $c$?

[]{#MA-MIC-ANM-01-009-052}

4. ¿Qué ocurre al multiplicar por una constante negativa $c$?

[]{#MA-MIC-ANM-01-009-053}

5. Escribe la cota general superior para una suma de sucesiones acotadas.

[]{#MA-MIC-ANM-01-009-054}

6. ¿Qué extremos tiene la suma si $a_n=(-1)^n$ y $b_n=-a_n$?

[]{#MA-MIC-ANM-01-009-055}

7. Si $b_n\to B$, ¿cuál es $\beta(a+b)$?

[]{#MA-MIC-ANM-01-009-056}

8. ¿Qué hipótesis de signo permite la cota $\beta(ab)\le\beta_a\beta_b$?

## 9.8. Qué describen los extremos y qué dejan abierto

[]{#MA-SEC-ANM-01-009-008}

Reunamos tres lecturas que deben permanecer distintas. $\inf\{a_n:n\in\mathbb N\}$ y $\sup\{a_n:n\in\mathbb N\}$ describen toda la imagen. $\alpha,\beta$ describen las fronteras persistentes de sus colas. $\operatorname{LimSub}(a)$ describe todos los destinos de extracciones convergentes. Las relaciones demostradas son

$$
\inf T_0\le\alpha\le\beta\le\sup T_0,
\qquad
\{\alpha,\beta\}\subseteq\operatorname{LimSub}(a)\subseteq[\alpha,\beta].
$$

La primera cadena se sigue de las cotas de las envolventes y sus límites. La segunda reúne extracción y confinamiento. Una igualdad entre extremos no identifica las sucesiones como funciones: la constante cero y $1/(n+1)$ tienen las mismas fronteras y diferentes valores en cada índice.

**Picos escasos que persisten.** Definamos $a_n=1$ si $n=2^j$ para algún $j\in\mathbb N$, y $a_n=0$ en los demás índices. Cada cola contiene un uno: las potencias de dos superan todo corte, por ejemplo porque $2^j\ge j+1$. También contiene un cero: los índices $2^j+1$ para $j\ge1$ no son potencias de dos y crecen sin cota. Así $\ell_N=0$ y $u_N=1$ para toda cola, luego $\alpha=0$, $\beta=1$. La separación creciente entre picos no elimina su efecto. Las fronteras usan la posibilidad de visitas arbitrariamente tardías, sin medir su frecuencia.

**Dos extremos no determinan todos los destinos.** La alternancia cero–uno y la sucesión periódica $0,1/2,1,0,1/2,1,\ldots$ tienen ambos extremos cero y uno. Sus conjuntos de destinos son, respectivamente, $\{0,1\}$ y $\{0,1/2,1\}$. Para una sucesión con imagen finita, cada límite de subsucesión pertenece a esa imagen: si $x$ quedara fuera, la mínima distancia a sus finitos valores sería positiva e impediría convergencia. Los valores periódicos sí son destinos mediante selecciones de una clase de índices. Así las fronteras delimitan, pero no describen toda la estructura interna.

**La frontera del contrato.** Para $a_n=n$, cada cola tiene ínfimo $N$, pero carece de supremo real. Además la envolvente inferior $N$ no converge a un real. Para $a_n=(-1)^n(n+1)$, cada cola carece de ambos extremos reales, pues incluye valores positivos y negativos sin cota. La definición real finita de este capítulo no se aplica a esos ejemplos. C06 permite describir escape hacia infinito en su sentido ordinario; una teoría de límites extremos extendidos exigiría declarar otro espacio de valores y otras reglas, y no se introduce aquí de forma tácita.

La ruta completa ha sido cola, extremos reales de cola, dos envolventes monótonas y límites de esas envolventes. Volvimos después a los términos para construir destinos y medir oscilación. Quedan autorizadas las caracterizaciones, el criterio de igualdad, las invariancias y las reglas con sus hipótesis. Una muestra finita ayuda a ver esa estructura; las pruebas que controlan cualquier corte son las que la sostienen.

### Antes de seguir

[]{#MA-MIC-ANM-01-009-057}

1. ¿Qué extremos tiene la sucesión que vale uno en potencias de dos y cero en los demás índices?

[]{#MA-MIC-ANM-01-009-058}

2. ¿La separación creciente entre picos elimina su efecto sobre $\beta$?

[]{#MA-MIC-ANM-01-009-059}

3. ¿Igualdad de ambos extremos entre dos sucesiones significa igualdad de funciones?

[]{#MA-MIC-ANM-01-009-060}

4. ¿Dos sucesiones con extremos cero y uno deben tener el mismo conjunto de destinos?

[]{#MA-MIC-ANM-01-009-061}

5. ¿Por qué una sucesión con imagen finita no puede tener un destino fuera de esa imagen?

[]{#MA-MIC-ANM-01-009-062}

6. ¿Por qué no se aplica la definición real finita de $\beta$ a $a_n=n$?

[]{#MA-MIC-ANM-01-009-063}

7. ¿Qué impide que los ínfimos de cola de $a_n=n$ produzcan un $\alpha$ real?

[]{#MA-MIC-ANM-01-009-064}

8. Escribe en orden los cuatro objetos de la construcción central.

[Índice del libro](../para-matematicos/analisis-para-matematicos.html) · [Capítulo 9](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola.html) · [Ejercicios](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-ejercicios.html) · [Soluciones](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-soluciones.html) · [Soluciones de microcontroles](analisis-para-matematicos-capitulo-9-limite-superior-e-inferior-las-envolventes-de-una-cola-microcontroles.html)

[← Capítulo 8](analisis-para-matematicos-capitulo-8-subsucesiones-acumulacion-y-bolzanoweierstrass.html) · [Capítulo 10 →](analisis-para-matematicos-capitulo-10-cauchy-converger-sin-conocer-el-destino.html)

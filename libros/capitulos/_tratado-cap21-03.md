## 21.3. Integral inferior e integral superior {#sec-ta-21-3}

Las sumas de Darboux son números asociados a una partición particular. Para obtener cantidades que dependan solamente de la función y del intervalo, consideraremos todas las particiones admisibles. El paso exige dos verificaciones separadas: que las colecciones de sumas sean conjuntos genuinos, no clases indefinidas, y que sus extremos existan como números reales. La comparación de §21.2 proporcionará las cotas necesarias; sólo después aplicaremos la completitud.

### Definición 21.3.1 — Conjuntos de sumas inferiores y superiores
Sean $a,b\in\mathbb R$ con $a<b$, sea $f:[a,b]\to\mathbb R$ acotada y escribamos $\mathcal P_{a,b}:=\operatorname{Part}[a,b]$. Definimos

$$
\boxed{\mathcal L_f:=\{L(f,P):P\in\mathcal P_{a,b}\},\qquad
       \mathcal U_f:=\{U(f,P):P\in\mathcal P_{a,b}\}.}
\tag{21.3.1}
$$

La notación de llaves en (21.3.1) significa imagen de funciones, no comprensión irrestricta. En efecto, $P\mapsto L(f,P)$ y $P\mapsto U(f,P)$ son reglas unívocas con dominio el conjunto $\mathcal P_{a,b}$ construido en Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes; sus grafos se obtienen por Separación dentro de $\mathcal P_{a,b}\times\mathbb R$ y sus imágenes son subconjuntos de $\mathbb R$. El parámetro $f$ está fijado y no se seleccionan particiones simultáneamente.

### Proposición 21.3.2 — Los conjuntos de sumas son no vacíos y están acotados
Para toda función acotada $f:[a,b]\to\mathbb R$, con $a<b$, los conjuntos $\mathcal L_f$ y $\mathcal U_f$ de (21.3.1) son no vacíos y están acotados superior e inferiormente en $\mathbb R$. Más precisamente, para cualesquiera cotas globales $A\le f(t)\le B$ y para la partición trivial $P_0$ de §21.1, se tiene

$$
\boxed{
 A(b-a)\le L(f,P)\le U(f,P_0),\qquad
 L(f,P_0)\le U(f,Q)\le B(b-a)
 \quad(P,Q\in\mathcal P_{a,b}).}
\tag{21.3.2}
$$

**Demostración.**
La partición trivial $P_0\in\mathcal P_{a,b}$ fue construida explícitamente en Proposición §21.1.2 — Existencia, anchuras positivas y suma de longitudes. Por la definición de los conjuntos, $L(f,P_0)\in\mathcal L_f$ y $U(f,P_0)\in\mathcal U_f$. Por tanto, ninguno de ellos es vacío.

Fijemos una pareja $A,B$ que satisfaga la acotación global; existe por hipótesis de acotación, y no se necesita definir una elección de cotas para distintas funciones o particiones. La desigualdad (21.2.6) de Proposición §21.2.5 — Encierro global e identidad de la brecha da

$$
A(b-a)\le L(f,P),\qquad U(f,Q)\le B(b-a).
$$

La comparación cruzada Corolario §21.2.9 — Toda suma inferior queda por debajo de toda suma superior, aplicada primero a $P,P_0$ y después a $P_0,Q$, da $L(f,P)\le U(f,P_0)$ y $L(f,P_0)\le U(f,Q)$. De aquí se obtiene exactamente (21.3.2). El primer par de extremos acota toda $\mathcal L_f$ y el segundo toda $\mathcal U_f$, en ambos sentidos. No se ha aplicado todavía la propiedad del supremo o del ínfimo. $\square$

### Definición 21.3.3 — Integrales inferior y superior de Darboux
Sean $f:[a,b]\to\mathbb R$ acotada y $a<b$. La proposición anterior garantiza que los dos conjuntos de (21.3.1) son no vacíos y están acotados. Por la propiedad del supremo del cuerpo ordenado completo $\mathbb R$ (Definición §4.6.1 — Propiedad del supremo y cuerpo ordenado completo, Teorema §12.8.1 — Existencia y caracterización única de la completación ordenada de $\mathbb Q$) y por la propiedad del ínfimo deducida en Proposición §4.6.2 — La propiedad del supremo implica la propiedad del ínfimo, existen únicos números reales que definimos como

$$
\boxed{
\underline{\int_a^b} f
 :=\sup\mathcal L_f=\sup_{P\in\mathcal P_{a,b}}L(f,P),
\qquad
\overline{\int_a^b} f
 :=\inf\mathcal U_f=\inf_{P\in\mathcal P_{a,b}}U(f,P).}
\tag{21.3.3}
$$

La notación $\underline{\int_a^b}f$ designa la integral inferior y $\overline{\int_a^b}f$ la integral superior. Son reales definidos para *toda* función acotada en el intervalo no degenerado. Las barras no denotan límites de sucesiones ni suponen que alguna partición alcance estos extremos. Tampoco se ha definido aún un símbolo de integral sin barra: tal símbolo exigirá primero probar que ambas cantidades coinciden.

### Proposición 21.3.4 — Orden y encierro de las integrales extremas
Para toda función acotada $f:[a,b]\to\mathbb R$ y cualesquiera cotas $A,B$ de (21.2.1) se tiene

$$
\boxed{
 A(b-a)\le L(f,P)\le\underline{\int_a^b}f
 \le\overline{\int_a^b}f\le U(f,Q)\le B(b-a)}
 \quad(P,Q\in\mathcal P_{a,b}).
\tag{21.3.4}
$$

En particular, la integral inferior nunca supera la superior; ambos números son finitos y ninguna integral extrema necesita coincidir con una suma particular.

**Demostración.**
La condición $A\le f(t)\le B$, junto con Proposición §21.2.5 — Encierro global e identidad de la brecha, proporciona $A(b-a)\le L(f,P)$ y $U(f,Q)\le B(b-a)$ para todas las particiones. Por definición de supremo, $L(f,P)\le\sup\mathcal L_f$; por definición de ínfimo, $\inf\mathcal U_f\le U(f,Q)$.

**La desigualdad central requiere comparar las dos colecciones completas.** Fijemos una partición $Q$. Para *toda* partición $P$, Corolario §21.2.9 — Toda suma inferior queda por debajo de toda suma superior da $L(f,P)\le U(f,Q)$. Por tanto, $U(f,Q)$ es cota superior del conjunto entero $\mathcal L_f$, y la minimalidad del supremo implica

$$
\underline{\int_a^b}f=\sup\mathcal L_f\le U(f,Q).
$$

Como $Q$ era arbitraria, la integral inferior es cota inferior de $\mathcal U_f$; por maximalidad del ínfimo,

$$
\underline{\int_a^b}f\le\inf\mathcal U_f
=\overline{\int_a^b}f.
$$

Finalmente, $A(b-a)$ es cota inferior de $\mathcal L_f$; al ser ésta no vacía, no puede exceder su supremo. Análogamente, $B(b-a)$ es cota superior de $\mathcal U_f$, cuyo ínfimo no puede excederla. Con estas observaciones se reúnen todas las desigualdades de (21.3.4). La prueba no usa una partición óptima ni un extremo alcanzado. $\square$

### Corolario 21.3.5 — Aproximación simultánea por una sola partición
Para toda función acotada $f:[a,b]\to\mathbb R$ y todo $\varepsilon>0$ existe una misma partición $R\in\mathcal P_{a,b}$ tal que

$$
\boxed{
\underline{\int_a^b}f-\varepsilon<L(f,R)
\le\underline{\int_a^b}f
\le\overline{\int_a^b}f
\le U(f,R)<\overline{\int_a^b}f+\varepsilon.}
\tag{21.3.5}
$$

Más precisamente, si $D_f:=\overline{\int_a^b}f-\underline{\int_a^b}f\ge0$, para todo $\varepsilon>0$ existe una partición $R$ con

$$
\boxed{D_f\le U(f,R)-L(f,R)<D_f+\varepsilon.}
\tag{21.3.6}
$$

**Demostración.**
Por (21.3.3), el real $\ell:=\underline{\int_a^b}f$ es supremo de $\mathcal L_f$. Dado $\eta>0$, existe una partición $P$ tal que $\ell-\eta<L(f,P)\le\ell$. Si no existiera, $\ell-\eta$ sería cota superior de $\mathcal L_f$, estrictamente menor que su supremo, contradicción. La pertenencia de una suma a $\mathcal L_f$ suministra un testigo $P$ por la definición de imagen; la prueba no elige una familia de testigos para todos los $\eta$.

De manera dual, $u:=\overline{\int_a^b}f$ es ínfimo de $\mathcal U_f$. Existe una partición $Q$ con $u\le U(f,Q)<u+\eta$: en caso contrario $u+\eta$ sería cota inferior estrictamente mayor que el ínfimo.

Tomemos ahora $\eta=\varepsilon/2>0$ e instanciemos esos dos testigos $P,Q$. El refinamiento común Teorema §21.1.5 — Existencia de un refinamiento común proporciona una partición $R$ que refina simultáneamente a ambas. La monotonía Teorema §21.2.8 — Monotonía de las sumas bajo refinamiento y las propiedades extremales de (21.3.3) implican

$$
\ell-\eta<L(f,P)\le L(f,R)\le\ell
\le u\le U(f,R)\le U(f,Q)<u+\eta.
$$

Como $\eta<\varepsilon$, esto demuestra (21.3.5). Restando los extremos correspondientes obtenemos

$$
0\le (U(f,R)-L(f,R))-(u-\ell)<2\eta=\varepsilon,
$$

de donde se sigue (21.3.6). La existencia de $P$ y $Q$ para una precisión fijada y la construcción de un refinamiento finito no constituyen una instancia de elección numerable. No se afirma que $D_f=0$: esa cuestión pertenece a la sección siguiente. $\square$

**Ejemplo de control.** Si $f(t)=c$ en todo $[a,b]$, §21.2 mostró que $L(f,P)=U(f,P)=c(b-a)$ para cada partición. Ambos conjuntos de (21.3.1) son entonces el singleton $\{c(b-a)\}$ y, por (21.3.3), las dos integrales extremas valen $c(b-a)$. Esto sólo utiliza las definiciones disponibles; la futura expresión de integral sin barras todavía no está habilitada.

**Transición.** §21.3 ha asociado dos números reales a toda función acotada y ha demostrado que su diferencia no negativa es la menor brecha que las sumas de una partición pueden aproximar. La próxima sección, §21.4, definirá integrabilidad mediante la igualdad de las dos integrales y demostrará el criterio de Darboux en términos de $U(f,P)-L(f,P)<\varepsilon$.

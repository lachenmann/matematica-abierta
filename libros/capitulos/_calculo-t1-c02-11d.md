Esta es una forma elemental de propiedad de corte de la recta real.
:::

::: {#exr-t1-0075}
<!-- CPM-T1-EXR-0075 | G | PROOF | SYNTHESIS | DISCOVERY | ORIGINAL -->
**Ejercicio G3. Construir una raíz cúbica sin continuidad.** Sea $a>0$ y define

$$
S=\{x\in\mathbb R:x\ge0,\ x^3<a\}.
$$

1. Demuestra que $S$ es no vacío y está acotado superiormente.
2. Define $\alpha=\sup S$.
3. Demuestra, mediante perturbaciones algebraicas explícitas, que ni $\alpha^3<a$ ni $\alpha^3>a$ son posibles.
4. Concluye que existe un único $\alpha>0$ tal que $\alpha^3=a$.

No utilices continuidad ni el teorema del valor intermedio.
:::

### Soluciones

Las soluciones siguen el mismo orden. En los ejercicios técnicos se incluyen los controles de dominio y de signos; en los problemas de síntesis se explicita la estrategia y la dependencia estructural decisiva.

#### Soluciones del nivel A

::: {#sol-t1-0036}
<!-- CPM-T1-SOL-0036 -->
**Solución A1.**

Por la equivalencia entre valor absoluto y distancia,

$$
|x-3|<2
\iff
-2<x-3<2.
$$

Sumando $3$,

$$
1<x<5.
$$

Por tanto, las cuatro lecturas son:

$$
|x-3|<2,
\qquad
1<x<5,
\qquad
x\in(1,5),
$$

y, verbalmente: **$x$ está a distancia menor que $2$ del punto $3$**.
:::

::: {#sol-t1-0037}
<!-- CPM-T1-SOL-0037 -->
**Solución A2.**

Si $a<b$:

1. para $c>0$, se conserva el sentido:
   $$ac<bc;$$
2. para $c<0$, se invierte:
   $$ac>bc;$$
3. para $c=0$,
   $$ac=bc=0.$$

La razón no es una regla tipográfica, sino la compatibilidad del orden con el producto por positivos, combinada con $c=-(-c)$ cuando $c<0$.
:::

::: {#sol-t1-0038}
<!-- CPM-T1-SOL-0038 -->
**Solución A3.**

Para $A=(0,4)$:

1. $5$ es cota superior: todo $a\in A$ satisface $a<4<5$.
2. $4$ es cota superior: todo $a\in A$ satisface $a<4$.
3. $4$ no es máximo, porque $4\notin A$.
4. $\sup A=4$: ya sabemos que es cota superior y, dado $\varepsilon>0$, podemos elegir un punto de $A$ situado entre $4-\varepsilon$ y $4$; por ejemplo, si $\varepsilon<4$, $4-\varepsilon/2\in A$.

La diferencia decisiva es que una cota o un supremo no necesitan pertenecer al conjunto; un máximo sí.
:::

::: {#sol-t1-0039}
<!-- CPM-T1-SOL-0039 -->
**Solución A4.**

La clasificación es la siguiente.

1. **Axioma.**
   $$
   a(b+c)=ab+ac
   $$
   es exactamente `C9`, la distributividad.

2. **Definición.**
   $$
   a-b:=a+(-b)
   $$
   es la definición de resta como operación derivada de la suma y el inverso aditivo.

3. **Resultado demostrado.**
   $$
   a0=0
   $$
   no figura entre `C1--C9`. Se demuestra a partir de los axiomas; en §2.2 aparece como la prueba auditada @exm-t1-0040.

4. **Resultado demostrado.** La implicación
   $$
   a\ne0,\quad ab=ac\Longrightarrow b=c
   $$
   es la cancelación multiplicativa de @prp-t1-0027. La hipótesis $a\ne0$ no es decorativa: permite usar el inverso multiplicativo de $a$.

5. **Definición.** El orden se introduce mediante la positividad:
   $$
   a<b
   \iff
   b-a>0.
   $$
   Por tanto esta equivalencia fija el significado de $<$ dentro de la estructura ordenada.

La distinción importa porque un axioma puede usarse como punto de partida, una definición fija significado y un resultado demostrado solo puede reutilizarse después de haber sido establecido. Si tratamos una consecuencia como si fuese axioma, podemos ocultar precisamente la dependencia que una auditoría de prueba debe hacer visible.
:::
::: {#sol-t1-0040}
<!-- CPM-T1-SOL-0040 -->
**Solución A5.**

El axioma del supremo exige dos hipótesis: conjunto **no vacío** y **acotado superiormente**.

1. $(0,1)$ cumple ambas: completitud garantiza un supremo.
2. $\mathbb N$ es no vacío, pero no está acotado superiormente en $\mathbb R$; el axioma no se aplica.
3. $\varnothing$ falla la hipótesis de no vacuidad.
4. $\{-3,7,10\}$ es no vacío y acotado superiormente; completitud garantiza supremo, aunque en este caso su existencia puede verse incluso sin recurrir al axioma general.
:::

::: {#sol-t1-0041}
<!-- CPM-T1-SOL-0041 -->
**Solución A6.**

1. La desigualdad triangular se obtiene de **cuerpo ordenado** y las propiedades del valor absoluto; no necesita completitud.
2. La existencia general de supremos para conjuntos no vacíos y acotados superiormente es **completitud directamente**.
3. $1/n<\varepsilon$ se deduce de la **propiedad arquimediana**, que en nuestro desarrollo es una **consecuencia previa de completitud**.
4. La densidad racional se deduce de arquimedianidad y encajonamiento entero; por tanto depende **indirectamente de completitud** en la cadena adoptada por este capítulo.

La clasificación depende de nuestra arquitectura de pruebas, no solo de que un resultado sea verdadero en $\mathbb R$.
:::

::: {#sol-t1-0042}
<!-- CPM-T1-SOL-0042 -->
**Solución A7.**

Tenemos

$$
\frac1{n+2}<\frac1{n+1}.
$$

Por tanto,

$$
1-\frac1{n+1}<1-\frac1{n+2}
$$

y

$$
1+\frac1{n+2}<1+\frac1{n+1}.
$$

Así, los extremos del intervalo siguiente quedan dentro del anterior y

$$
I_{n+1}\subseteq I_n.
$$

Además,

$$
1-\frac1{n+1}\le1\le1+\frac1{n+1},
$$

de modo que $1\in I_n$ para todo $n$.

Como todos los $I_n$ son cerrados, no vacíos, acotados y encajados, el principio de intervalos encajados garantiza

$$
\bigcap_nI_n\neq\varnothing.
$$

Ese teorema por sí solo garantiza existencia, no unicidad. La unicidad requeriría además explotar que las longitudes se hacen arbitrariamente pequeñas.
:::

#### Soluciones del nivel B

::: {#sol-t1-0043}
<!-- CPM-T1-SOL-0043 -->
**Solución B1.**

$$
|2x-5|<3
\iff
-3<2x-5<3.
$$

Sumando $5$,

$$
2<2x<8.
$$

Dividiendo por $2>0$,

$$
1<x<4.
$$

Por tanto,

$$
\boxed{x\in(1,4).}
$$
:::

::: {#sol-t1-0044}
<!-- CPM-T1-SOL-0044 -->
**Solución B2.**

Factorizamos:

$$
|x^2-4|=|x-2|\,|x+2|.
$$

Para controlar el segundo factor escribimos

$$
x+2=(x-2)+4.
$$

Por desigualdad triangular,

$$
|x+2|\le |x-2|+4<\frac1{10}+4=\frac{41}{10}.
$$

Luego

$$
|x^2-4|
<
\frac1{10}\cdot\frac{41}{10}
=
\frac{41}{100}.
$$

La idea es típica de las estimaciones futuras: el dato controla $|x-2|$ y fabricamos a partir de él un control del factor restante.
:::

::: {#sol-t1-0045}
<!-- CPM-T1-SOL-0045 -->
**Solución B3.**

Tenemos

$$
a+b=0,
\qquad
a+c=0.
$$


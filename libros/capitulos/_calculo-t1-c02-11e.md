### Soluciones

Las soluciones siguen el mismo orden. En los ejercicios técnicos se incluyen los controles de dominio y de signos; en los problemas de síntesis se explicita la estrategia y la dependencia estructural decisiva.

#### Soluciones del nivel A

::: {#sol-t1-0036}
<!-- CPM-T1-SOL-0036 -->
**Solución A1.**

Las dos condiciones equivalen a

$$
-1<x<5
$$

y

$$
-3\le x\le1.
$$

Debemos tomar la intersección. Por tanto,

$$
-1<x\le1,
$$

y

$$
\boxed{S=(-1,1]}.
$$

El extremo $-1$ queda excluido por la primera desigualdad estricta; el extremo $1$ satisface ambas condiciones.
:::
::: {#sol-t1-0037}
<!-- CPM-T1-SOL-0037 -->
**Solución A2.**

Como $c<0$, multiplicar $a<b$ por $c$ invierte el orden; además, los dos productos son negativos:

$$
\boxed{bc<ac<0}.
$$

Dividir por $c<0$ también invierte el orden, y ambos cocientes son negativos:

$$
\boxed{\frac bc<\frac ac<0}.
$$

Finalmente, para recíprocos positivos se invierte el orden:

$$
\boxed{0<\frac1b<\frac1a}.
$$

Las tres cadenas usan el mismo dato $a<b$, pero cada transformación exige controlar el signo del factor o divisor.
:::
::: {#sol-t1-0038}
<!-- CPM-T1-SOL-0038 -->
**Solución A3.**

Todo elemento de $A$ es menor que $5$, y en el componente $[3,5)$ hay elementos arbitrariamente próximos a $5$ por la izquierda. Por tanto,

$$
\sup A=5,
$$

pero $5\notin A$, así que no hay máximo.

Del mismo modo, $-2$ es cota inferior y el componente $(-2,1]$ contiene puntos arbitrariamente próximos a $-2$ por la derecha. Luego

$$
\inf A=-2,
$$

y como $-2\notin A$, tampoco hay mínimo.
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

1. Sí. El conjunto es no vacío —por ejemplo, contiene a $2$— y está acotado superiormente, por ejemplo por $3$.
2. No. Es no vacío, pero no está acotado superiormente.
3. No. Falla la hipótesis de no vacuidad.
4. Sí. Contiene a $1$ y está acotado superiormente por $1$.
5. Sí. Es no vacío y $0$ es una cota superior.

La quinta parte subraya que el axioma solo exige acotación **superior**; el conjunto puede ser ilimitado hacia abajo.
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

La desigualdad equivale a

$$
1\le|x-1|\le3.
$$

La cota superior da

$$
-2\le x\le4,
$$

mientras que $|x-1|\ge1$ equivale a

$$
x\le0
\quad\text{o}\quad
x\ge2.
$$

Intersectando ambas condiciones,

$$
\boxed{x\in[-2,0]\cup[2,4]}.
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

Por las reglas de cocientes,

$$
a^{-1}-b^{-1}
=
\frac1a-\frac1b
=
\frac{b-a}{ab}.
$$

Si $0<a<b$, entonces $b-a>0$ y $ab>0$. Dividir un positivo por un positivo produce un número positivo, de modo que

$$
\frac1a-\frac1b>0.
$$

Por definición del orden,

$$
\boxed{\frac1b<\frac1a}.
$$
:::
::: {#sol-t1-0046}
<!-- CPM-T1-SOL-0046 -->
**Solución B4.**

La elección más sencilla es

$$
\boxed{n=201}.
$$

Claramente $201>200$. Además, como $201>137>0$, al tomar recíprocos se invierte el orden:

$$
\frac1{201}<\frac1{137}.
$$

Por tanto satisface simultáneamente ambas exigencias.
:::

::: {#sol-t1-0047}
<!-- CPM-T1-SOL-0047 -->
**Solución B5.**

Partimos de

$$
I_0=[3,4],
$$

porque $3^2=9<10<16=4^2$.

Primer punto medio:

$$
m_1=\frac72,
\qquad
\left(\frac72\right)^2=\frac{49}{4}>10.
$$

Conservamos

$$
I_1=\left[3,\frac72\right].
$$

Segundo punto medio:

$$
m_2=\frac{13}{4},
\qquad
\left(\frac{13}{4}\right)^2=\frac{169}{16}>10
$$

porque $169>160$. Luego

$$
I_2=\left[3,\frac{13}{4}\right].
$$

Tercer punto medio:

$$
m_3=\frac{25}{8},
\qquad
\left(\frac{25}{8}\right)^2=\frac{625}{64}<10
$$

porque $625<640$. Por tanto,

$$
I_3=\left[\frac{25}{8},\frac{13}{4}\right].
$$

Así,

$$
\boxed{\frac{25}{8}<\sqrt{10}<\frac{13}{4}.}
$$
:::

::: {#sol-t1-0048}
<!-- CPM-T1-SOL-0048 -->
**Solución B6.**

Por definición,

$$
\frac ab=ab^{-1}.
$$

La parte 5 de @prp-t1-0007 dice que $b^{-1}$ tiene el mismo signo que $b$. La parte 8 caracteriza el signo de un producto: es positivo cuando los factores tienen el mismo signo y negativo cuando tienen signos opuestos. Sustituyendo el signo de $b^{-1}$ por el de $b$ obtenemos exactamente

$$
\boxed{\frac ab>0
\iff
(a>0,b>0)\text{ o }(a<0,b<0)}
$$

y

$$
\boxed{\frac ab<0
\iff
(a>0,b<0)\text{ o }(a<0,b>0)}.
$$
:::
::: {#sol-t1-0049}
<!-- CPM-T1-SOL-0049 -->
**Solución B7.**

Queremos resolver

$$
\left|\frac{x-1}{x+2}\right|
\le
\frac{|x-3|}{2}.
$$

**1. Dominio y puntos críticos.** El denominador exige

$$
x\ne-2.
$$

Los argumentos de los valores absolutos se anulan en $x=1$ y $x=3$. Estos puntos, junto con el polo $-2$, deben registrarse aunque una transformación posterior produzca fronteras adicionales.

**2. Eliminación segura de denominadores y valores absolutos.** Para $x\ne-2$, $2|x+2|>0$. Multiplicamos sin cambiar el sentido:

$$
2|x-1|\le |x-3|\,|x+2|.
$$

Ambos lados son no negativos, así que elevar al cuadrado es una equivalencia:

$$
4(x-1)^2\le (x-3)^2(x+2)^2.
$$

Llevando todo a un lado y factorizando,

$$
(x-3)^2(x+2)^2-4(x-1)^2
=(x-4)(x+1)(x^2+x-8).
$$

Las raíces del factor cuadrático son

$$
r_- =\frac{-1-\sqrt{33}}2,
\qquad
r_+ =\frac{-1+\sqrt{33}}2.
$$

El orden relevante es

$$
r_-<-2<-1<r_+<3<4.
$$

**3. Análisis de signos.** Debemos resolver

$$
(x-4)(x+1)(x-r_-)(x-r_+)\ge0.
$$

Todos los ceros son simples, por lo que el signo alterna al atravesarlos. Como el polinomio es positivo para $x$ grande y positivo, resulta no negativo en

$$
(-\infty,r_-]\cup[-1,r_+]\cup[4,\infty).
$$

El punto excluido $x=-2$ se encuentra en una región que ya no pertenece a la solución, pero debe mantenerse fuera del dominio en todo momento.

**4. Extremos.** En $r_-$, $-1$, $r_+$ y $4$ se obtiene igualdad, y ninguno es un polo; por eso se incluyen.

Por consiguiente,

$$
\boxed{
(-\infty,\tfrac{-1-\sqrt{33}}2]
\cup
[-1,\tfrac{-1+\sqrt{33}}2]
\cup
[4,\infty)
}.
$$

La comprobación final respeta el dominio original y todos los extremos proceden de equivalencias algebraicas reversibles.
:::


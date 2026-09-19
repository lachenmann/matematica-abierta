## 13.5. Álgebra de los límites {#sec-ta-13-5}

La definición de convergencia controla una sucesión mediante desigualdades. Sin embargo, el análisis necesita algo más: debe ser posible **calcular con sucesiones convergentes** sin abandonar el régimen de convergencia.

Las operaciones puntuales fueron construidas ya en §13.1. Lo que todavía no sabemos es si esas operaciones son compatibles con el paso al límite. Esa compatibilidad no forma parte de la definición de suma o producto de sucesiones; requiere demostraciones.

La diferencia entre suma y producto anticipa una idea metodológica importante. Para la suma basta repartir una tolerancia entre dos errores. Para el producto aparece un factor variable y, por tanto, necesitamos primero saber que una sucesión convergente está acotada. Precisamente por eso §13.4 precede a esta sección.

### Proposición 13.5.1 — Límite de una suma

Sean $x=(x_n)$ e $y=(y_n)$ sucesiones reales. Si

$$
x_n\to\alpha
\qquad\text{y}\qquad
y_n\to\beta,
$$

entonces

$$
\boxed{
x_n+y_n\to\alpha+\beta.
}
$$

Equivalentemente,

$$
\boxed{
\lim_{n\to\infty}(x_n+y_n)
=
\lim_{n\to\infty}x_n
+
\lim_{n\to\infty}y_n
}
$$

siempre que los dos límites del segundo miembro existan.

**Demostración.**

Sea $\varepsilon>0$. Escribamos

$$
s:=1+1.
$$

Como $0<1$, se tiene $0<s$. Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6),

$$
s^{-1}>0.
$$

Definimos

$$
\eta:=\varepsilon s^{-1}.
$$

Entonces $\eta>0$ y, por las leyes del cuerpo,

$$
s\eta=\varepsilon.
$$

De $x_n\to\alpha$ obtenemos eventualmente

$$
|x_n-\alpha|<\eta,
$$

y de $y_n\to\beta$ obtenemos eventualmente

$$
|y_n-\beta|<\eta.
$$

La regla de intersección de propiedades eventuales Proposición 13.2.5 — Reglas elementales de eventualidad (3) proporciona un mismo tramo final en el que ambas desigualdades valen. Para todo índice de ese tramo,

$$
\begin{aligned}
|(x_n+y_n)-(\alpha+\beta)|
&=|(x_n-\alpha)+(y_n-\beta)|\\
&\le |x_n-\alpha|+|y_n-\beta|\\
&<\eta+\eta\\
&=s\eta\\
&=\varepsilon.
\end{aligned}
$$

La desigualdad no estricta es la desigualdad triangular Teorema 4.2.3 — Desigualdad triangular; la estricta se obtiene sumando las dos estimaciones estrictas en el cuerpo ordenado.

Como $\varepsilon>0$ era arbitrario,

$$
x_n+y_n\to\alpha+\beta.
$$

La formulación con $\lim$ se sigue de Notación 13.3.6 — Límite de una sucesión convergente. ∎

> **Estrategia.** El paso esencial no es la manipulación algebraica, sino la elección de una tolerancia auxiliar que pueda gastarse dos veces:
>
> $$
> \eta+\eta=\varepsilon.
> $$
>
> Una demostración de límite debe diseñar primero el **presupuesto de error** y sólo después buscar un umbral.

### Proposición 13.5.2 — Límite del opuesto y de una diferencia

Sea $x=(x_n)$ una sucesión real. Si

$$
x_n\to\alpha,
$$

entonces

$$
\boxed{
-x_n\to-\alpha.
}
$$

En consecuencia, si además $y_n\to\beta$, entonces

$$
\boxed{
x_n-y_n\to\alpha-\beta.
}
$$

**Demostración.**

Para todo $n\in\mathbb N$,

$$
\begin{aligned}
|(-x_n)-(-\alpha)|
&=|-(x_n-\alpha)|\\
&=|x_n-\alpha|
\end{aligned}
$$

por Proposición 4.2.2 — Propiedades elementales del valor absoluto (3).

Por tanto, para cada $\varepsilon>0$, cualquier umbral que sirva para

$$
|x_n-\alpha|<\varepsilon
$$

sirve también para

$$
|(-x_n)-(-\alpha)|<\varepsilon.
$$

Luego

$$
-x_n\to-\alpha.
$$

Si ahora $y_n\to\beta$, acabamos de probar

$$
-y_n\to-\beta.
$$

Aplicando Proposición 13.5.1 — Límite de una suma a $x$ y $-y$,

$$
x_n+(-y_n)\to\alpha+(-\beta),
$$

es decir,

$$
x_n-y_n\to\alpha-\beta.
$$

∎

La resta no exige una nueva estimación: una vez demostrados el opuesto y la suma, aparece como consecuencia estructural de las operaciones ya definidas.

### Teorema 13.5.3 — Límite de un producto

Sean $x=(x_n)$ e $y=(y_n)$ sucesiones reales. Si

$$
x_n\to\alpha
\qquad\text{y}\qquad
y_n\to\beta,
$$

entonces

$$
\boxed{
x_ny_n\to\alpha\beta.
}
$$

Por tanto,

$$
\boxed{
\lim_{n\to\infty}(x_ny_n)
=
\left(\lim_{n\to\infty}x_n\right)
\left(\lim_{n\to\infty}y_n\right)
}
$$

cuando ambos límites existen.

**Demostración.**

La dificultad es que el error de un producto contiene factores que dependen de $n$. Partimos de la identidad

$$
x_ny_n-\alpha\beta
=
x_n(y_n-\beta)+\beta(x_n-\alpha).
$$

Como $x_n\to\alpha$, Teorema 13.4.5 — Toda sucesión real convergente es acotada implica que $x$ es acotada. Por Proposición 13.4.2 — Caracterización de la acotación mediante el valor absoluto, existe $M\in\mathbb R$ tal que

$$
0\le M
$$

y

$$
|x_n|\le M
\qquad
\text{para todo }n\in\mathbb N.
$$

Sea ahora $\varepsilon>0$. Definimos

$$
r:=M+|\beta|+1.
$$

La no negatividad de $M$ y de $|\beta|$, junto con $0<1$, da

$$
r>0.
$$

Sea

$$
\eta:=\varepsilon r^{-1}.
$$

Por Lema 4.1.3 — Cálculo elemental de signos en un cuerpo ordenado (6) y la positividad del producto,

$$
\eta>0,
$$

y además

$$
r\eta=\varepsilon.
$$

Por convergencia, valen eventualmente las dos propiedades

$$
|x_n-\alpha|<\eta
$$

y

$$
|y_n-\beta|<\eta.
$$

Tomamos un tramo final común mediante Proposición 13.2.5 — Reglas elementales de eventualidad (3). Para todo índice de ese tramo, usando la desigualdad triangular y la multiplicatividad del valor absoluto,

$$
\begin{aligned}
|x_ny_n-\alpha\beta|
&=
|x_n(y_n-\beta)+\beta(x_n-\alpha)|\\
&\le
|x_n|\,|y_n-\beta|
+
|\beta|\,|x_n-\alpha|\\
&\le
M\eta+|\beta|\eta\\
&=
(M+|\beta|)\eta.
\end{aligned}
$$

En el tercer paso usamos dos veces que la multiplicación por un factor no negativo preserva el orden no estricto. Esta propiedad se deriva directamente de Definición 4.1.1 — Cuerpo ordenado: de $u\le v$ obtenemos $0\le v-u$ por Lema 4.1.3(1), y si $0\le w$, entonces $0\le w(v-u)=wv-wu$, de donde $wu\le wv$.

De

$$
M+|\beta|<M+|\beta|+1=r
$$

y $\eta>0$, la compatibilidad del orden con la multiplicación por un factor positivo da

$$
(M+|\beta|)\eta<r\eta=\varepsilon.
$$

Por consiguiente,

$$
|x_ny_n-\alpha\beta|<\varepsilon
$$

eventualmente. Como $\varepsilon>0$ era arbitrario,

$$
x_ny_n\to\alpha\beta.
$$

∎

> **Por qué la acotación era necesaria.** En la suma, los coeficientes de los dos errores son constantes. En el producto aparece
>
> $$
> |x_n|\,|y_n-\beta|.
> $$
>
> La convergencia de $y_n-\beta$ hacia cero no basta por sí sola para controlar ese producto si no sabemos que $|x_n|$ permanece uniformemente limitado. Teorema 13.4.5 — Toda sucesión real convergente es acotada aporta exactamente esa información.

> **Nota fundacional.** La extracción de un testigo $M$ desde la afirmación existencial de acotación ocurre dentro de una única demostración. No se selecciona una familia de cotas para una familia de sucesiones; no interviene Choice. Tampoco se usa completitud de $\mathbb R$.

### Corolario 13.5.4 — Compatibilidad con la multiplicación por una constante

Sea $c\in\mathbb R$. Si

$$
x_n\to\alpha,
$$

entonces

$$
\boxed{
cx_n\to c\alpha.
}
$$

**Demostración.**

La sucesión constante $\underline c$ converge a $c$ por Proposición 13.3.4 — Las sucesiones constantes convergen a su valor. Aplicando Teorema 13.5.3 — Límite de un producto a $\underline c$ y $x$,

$$
\underline c_n x_n\to c\alpha.
$$

Como $\underline c_n=c$ para todo $n$,

$$
cx_n\to c\alpha.
$$

∎

En particular, las combinaciones lineales finitas de sucesiones convergentes pueden tratarse iterando suma y multiplicación por constantes. No afirmamos aquí todavía un teorema para familias finitas arbitrarias: las operaciones binarias ya bastan para las aplicaciones inmediatas.

### Proposición 13.5.5 — El valor absoluto preserva límites

Sea $x=(x_n)$ una sucesión real. La regla

$$
z_n:=|x_n|
$$

determina una sucesión real $z=(z_n)$. Si

$$
x_n\to\alpha,
$$

entonces

$$
\boxed{
|x_n|\to|\alpha|.
}
$$

**Demostración.**

Primero justificamos que $(|x_n|)$ es efectivamente una sucesión. Dentro de $\mathbb N\times\mathbb R$ consideramos

$$
G_z
:=
\left\{
\langle n,u\rangle\in\mathbb N\times\mathbb R:
u=|x_n|
\right\}.
$$

El conjunto existe por Separación. Para cada $n\in\mathbb N$, Definición 4.2.1 — Valor absoluto determina un único real $|x_n|$; por tanto $G_z$ es el grafo de una función

$$
z:\mathbb N\to\mathbb R.
$$

Ahora la desigualdad triangular inversa Corolario 4.2.4 — Desigualdad triangular inversa da, para todo $n$,

$$
\bigl||x_n|-|\alpha|\bigr|
\le
|x_n-\alpha|.
$$

Sea $\varepsilon>0$. Como $x_n\to\alpha$, la propiedad

$$
|x_n-\alpha|<\varepsilon
$$

vale eventualmente. Para todo índice en que se cumple,

$$
\bigl||x_n|-|\alpha|\bigr|
<
\varepsilon.
$$

Por Proposición 13.2.5 — Reglas elementales de eventualidad (5), esta última propiedad también vale eventualmente. Por definición de convergencia,

$$
|x_n|\to|\alpha|.
$$

∎

El patrón de la prueba es especialmente reutilizable:

$$
\boxed{
\text{error de la transformación}
\le
\text{error original}.
}
$$

Cuando una operación satisface una estimación de este tipo, la convergencia puede transportarse sin modificar siquiera la tolerancia.

Los resultados de esta sección muestran que el paso al límite respeta las operaciones algebraicas que ya están disponibles término a término:

$$
\boxed{
\begin{aligned}
x_n\to\alpha,\ y_n\to\beta
&\Longrightarrow
x_n+y_n\to\alpha+\beta,\\
x_n\to\alpha,\ y_n\to\beta
&\Longrightarrow
x_n-y_n\to\alpha-\beta,\\
x_n\to\alpha,\ y_n\to\beta
&\Longrightarrow
x_ny_n\to\alpha\beta.
\end{aligned}
}
$$

y, además,

$$
x_n\to\alpha
\Longrightarrow
cx_n\to c\alpha
\quad\text{y}\quad
|x_n|\to|\alpha|.
$$

No hemos usado todavía la completitud de $\mathbb R$. Los cinco resultados de esta sección son compatibles con una lectura constructiva relativa a la estructura fija del cuerpo ordenado real y no emplean Choice. Esto no altera la clasificación ya registrada de Teorema 13.3.5 — Unicidad del límite real: la unicidad del límite conserva su último paso clásico de eliminación de doble negación sobre la igualdad real.

La siguiente sección estudiará cómo la convergencia interactúa con el **orden** y culminará en el **teorema del sándwich**. Ese será el puente natural hacia las sucesiones monótonas, donde la completitud empezará finalmente a producir nuevos límites.

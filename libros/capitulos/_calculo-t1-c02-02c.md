### La parte de orden: empezar por la positividad

Sea $F$ un cuerpo. Supongamos que se ha distinguido un subconjunto

$$
F_+\subseteq F,
$$

cuyos elementos llamaremos **positivos**, y que satisface las propiedades siguientes.

1. **(O1) Clausura de los positivos bajo la suma.** Si $a,b\in F_+$, entonces
   $$
   a+b\in F_+.
   $$
2. **(O2) Clausura de los positivos bajo el producto.** Si $a,b\in F_+$, entonces
   $$
   ab\in F_+.
   $$
3. **(O3) Tricotomía respecto de cero.** Para cada $a\in F$ ocurre exactamente una de las tres posibilidades
   $$
   a=0,
   \qquad
   a\in F_+,
   \qquad
   -a\in F_+.
   $$

Diremos entonces que

$$
a>0
\iff
a\in F_+,
$$

y

$$
a<0
\iff
-a\in F_+.
$$

Para comparar dos elementos cualesquiera definimos

$$
\boxed{
 a<b
 \iff
 b-a>0.
}
$$

Equivalentemente,

$$
a>b
\iff
a-b>0.
$$

Un cuerpo equipado con una elección de positivos que satisface (O1)--(O3), y con el orden definido de esta manera, se llama **cuerpo ordenado**.

En este libro asumiremos que $\mathbb R$ posee esta estructura. Obsérvese que todavía no hemos introducido ninguna propiedad de completitud.

::: {.callout-note title="Por qué esta formulación es útil"}
También es posible presentar un cuerpo ordenado tomando la relación $<$ como dato primitivo y postulando directamente tricotomía, transitividad y compatibilidad con las operaciones.

Aquí preferimos comenzar por los positivos porque hace visible una dependencia más profunda: varias propiedades que en la escuela suelen aparecer como «reglas de las desigualdades» pueden demostrarse a partir de solo tres exigencias sobre $F_+$.
:::

### De la tricotomía respecto de cero a la tricotomía entre dos números

La condición (O3) habla de un solo número y de su relación con $0$. Sin embargo, basta aplicarla a la **diferencia** de dos números para comparar cualquier par.

Dados $a,b\in F$, apliquemos (O3) a

$$
b-a.
$$

Exactamente una de estas posibilidades ocurre:

$$
b-a=0,
\qquad
b-a>0,
\qquad
-(b-a)>0.
$$

La primera equivale a $a=b$. La segunda, por definición, equivale a $a<b$. Y como

$$
-(b-a)=a-b,
$$

la tercera equivale a $b<a$.

Por tanto, para cualesquiera $a,b\in F$, exactamente una de las afirmaciones

$$
\boxed{
 a<b,
 \qquad
 a=b,
 \qquad
 b<a
}
$$

es verdadera.

Esta es la **tricotomía del orden**.

En particular, no puede ocurrir simultáneamente

$$
a<b
\quad\text{y}\quad
b<a.
$$

Tampoco puede cumplirse $a<a$, porque eso exigiría

$$
a-a=0>0,
$$

mientras que (O3) excluye que $0$ sea positivo.

### La transitividad también se demuestra

Supongamos

$$
a<b
\qquad\text{y}\qquad
b<c.
$$

Por definición,

$$
b-a>0
\qquad\text{y}\qquad
c-b>0.
$$

La clausura de los positivos bajo la suma da

$$
(b-a)+(c-b)>0.
$$

Pero el miembro izquierdo se simplifica a

$$
c-a.
$$

Luego

$$
c-a>0,
$$

y por definición

$$
\boxed{a<c.}
$$

Así, la transitividad de $<$ no ha sido añadida como un cuarto axioma independiente: sale de (O1) y de la manera en que definimos la comparación mediante diferencias.

::: {.callout-important title="Una idea estructural que conviene retener"}
Para comparar $a$ y $b$ estudiamos el signo de

$$
b-a.
$$

Este patrón aparecerá constantemente en análisis. Muchas preguntas acerca de dos cantidades se convierten en preguntas acerca del signo, el tamaño o el valor absoluto de su diferencia.
:::

### Del orden estricto al orden débil

Definiremos

$$
a\le b
$$

como abreviatura de

$$
a<b
\quad\text{o}\quad
a=b.
$$

Análogamente,

$$
a\ge b
\iff
b\le a.
$$

Las palabras **positivo**, **negativo**, **no negativo** y **no positivo** son entonces comparaciones con $0$:

$$
a>0,
\qquad
a<0,
\qquad
a\ge0,
\qquad
a\le0.
$$

La relación $\le$ es reflexiva, antisimétrica y transitiva. La reflexividad proviene de $a=a$; la antisimetría, de la tricotomía; y la transitividad se obtiene combinando la transitividad de $<$ con los casos de igualdad.

Estas propiedades serán especialmente importantes en §2.4, cuando hablemos de cotas superiores e inferiores.

### Las reglas de desigualdad son teoremas

Ya podemos obtener sistemáticamente las reglas que necesitaremos durante todo el tratado.

::: {#prp-t1-0007}
**Leyes básicas de desigualdad en un cuerpo ordenado.** Sean $a,b,c,d\in\mathbb R$.

1. **Traslación del orden.** Para todo $c$,
   $$
   a<b
   \iff
   a+c<b+c,
   $$
   y también
   $$
   a\le b
   \iff
   a+c\le b+c.
   $$
2. **Suma de desigualdades.** Si $a<b$ y $c<d$, entonces
   $$
   a+c<b+d.
   $$
   La versión correspondiente con $\le$ también es válida.
3. **Multiplicación por un no negativo.** Si $a\le b$ y $c\ge0$, entonces
   $$
   ac\le bc.
   $$
   Si además $a<b$ y $c>0$, entonces
   $$
   ac<bc.
   $$
4. **Multiplicación por un no positivo.** Si $a\le b$ y $c\le0$, entonces
   $$
   ac\ge bc.
   $$
   Si además $a<b$ y $c<0$, entonces
   $$
   ac>bc.
   $$
5. **Signo del inverso.** Si $a\ne0$, entonces $a$ y $a^{-1}$ tienen el mismo signo:
   $$
   a>0\iff a^{-1}>0,
   \qquad
   a<0\iff a^{-1}<0.
   $$
6. **División y orden.** Si $c>0$, entonces
   $$
   a<b
   \iff
   \frac ac<\frac bc.
   $$
   Si $c<0$, entonces
   $$
   a<b
   \iff
   \frac ac>\frac bc.
   $$
7. **Orden de los recíprocos positivos.** Si
   $$
   0<a<b,
   $$
   entonces
   $$
   0<\frac1b<\frac1a.
   $$
8. **Signo de un producto.** Se tiene
   $$
   ab>0
   \iff
   (a>0\ \text{y}\ b>0)
   \ \text{o}\
   (a<0\ \text{y}\ b<0),
   $$
   y
   $$
   ab<0
   \iff
   (a>0\ \text{y}\ b<0)
   \ \text{o}\
   (a<0\ \text{y}\ b>0).
   $$
9. **Cuadrados.** Para todo $a\in\mathbb R$,
   $$
   a^2\ge0,
   $$
   y si $a\ne0$, entonces
   $$
   a^2>0.
   $$
10. **El cuadrado preserva el orden en los no negativos.** Si
   $$
   0\le a\le b,
   $$
   entonces
   $$
   a^2\le b^2.
   $$
:::

::: {.callout-note title="Idea de la prueba"}
Las diez afirmaciones no son reglas independientes.

La demostración se apoya repetidamente en cuatro movimientos:

1. traducir $a<b$ a la positividad de $b-a$;
2. usar la clausura de los positivos bajo suma o producto;
3. utilizar las identidades algebraicas ya demostradas en la primera parte de §2.2;
4. traducir nuevamente una positividad en una desigualdad.

El caso de los inversos añade una observación crucial: para dividir una desigualdad necesitamos saber el **signo del divisor**, no solo que sea distinto de cero.
:::

**Demostración.**

Para la parte 1, observemos que

$$
(b+c)-(a+c)=b-a.
$$

Por tanto,

$$
b-a>0
\iff
(b+c)-(a+c)>0,
$$

que, por definición, equivale a

$$
a<b
\iff
a+c<b+c.
$$

La versión con $\le$ se obtiene añadiendo el caso $a=b$.

Para la parte 2, de $a<b$ y la parte 1 obtenemos

$$
a+c<b+c.
$$

De $c<d$, sumando $b$, obtenemos

$$
b+c<b+d.
$$

Por transitividad,

$$
a+c<b+d.
$$

Consideremos ahora la parte 3. Si $a<b$, entonces

$$
b-a>0.
$$

Como además $c>0$, (O2) da

$$
c(b-a)>0.
$$

Por distributividad,

$$
bc-ac>0.
$$

Por definición del orden,

$$
ac<bc.
$$

Si solo sabemos $a\le b$ y $c\ge0$, hay tres posibilidades relevantes: si $a=b$ o $c=0$, los productos son iguales; si $a<b$ y $c>0$, acabamos de demostrar $ac<bc$. En todos los casos,

$$
ac\le bc.
$$

Para la parte 4, supongamos primero $a<b$ y $c<0$. Entonces

$$
-c>0.
$$

La parte 3 aplicada a $-c$ produce

$$
a(-c)<b(-c).
$$

Usando las reglas de signos ya demostradas,

$$
-ac<-bc.
$$

Sumando $ac+bc$ a ambos miembros obtenemos

$$
bc<ac,
$$

es decir,

$$
ac>bc.
$$

La versión débil para $a\le b$ y $c\le0$ se obtiene del mismo modo, separando los casos de igualdad.

Antes de estudiar inversos conviene establecer un hecho pequeño pero decisivo:

$$
\boxed{1>0.}
$$

Como $1\ne0$, (O3) dice que exactamente una de las cantidades $1$ y $-1$ es positiva. Si $-1>0$, entonces (O2) implicaría

$$
(-1)(-1)>0.
$$

Pero por las reglas de signos,

$$
(-1)(-1)=1,
$$

de modo que $1>0$ y $-1>0$ simultáneamente, contradiciendo (O3). Por tanto,

$$
1>0.
$$

Probemos la parte 5. Supongamos primero $a>0$. Sabemos por @prp-t1-0026 que $a^{-1}\ne0$. Por tricotomía, $a^{-1}$ es positivo o negativo.

Si fuera negativo, entonces

$$
-a^{-1}>0.
$$

Como $a>0$, (O2) daría

$$
a(-a^{-1})>0.
$$

Pero

$$
a(-a^{-1})=-(aa^{-1})=-1,
$$

lo que contradice que $1>0$. Luego

$$
a^{-1}>0.
$$

La implicación recíproca se obtiene aplicando el resultado anterior a $a^{-1}$ y usando

$$
(a^{-1})^{-1}=a.
$$

Supongamos ahora $a<0$. Entonces $-a>0$, y por lo recién demostrado

$$
(-a)^{-1}>0.
$$

Además,

$$
(-a)(-a^{-1})=aa^{-1}=1.
$$

Por unicidad del inverso multiplicativo,

$$
(-a)^{-1}=-a^{-1}.
$$

Así,

$$
-a^{-1}>0,
$$

que equivale a

$$
a^{-1}<0.
$$

La recíproca vuelve a seguir de $(a^{-1})^{-1}=a$.

La parte 6 es ahora una consecuencia inmediata. Si $c>0$, entonces

$$
c^{-1}>0.
$$

Multiplicar $a<b$ por $c^{-1}$ conserva el sentido:

$$
ac^{-1}<bc^{-1},
$$

es decir,

$$
\frac ac<\frac bc.
$$

Como el mismo argumento es reversible, obtenemos la equivalencia. Si $c<0$, entonces $c^{-1}<0$ y la multiplicación invierte el sentido, lo que da la segunda equivalencia.

Para la parte 7, supongamos

$$
0<a<b.
$$

Por (O2),

$$
ab>0,
$$

y por la parte 5,

$$
(ab)^{-1}>0.
$$

Multiplicamos $a<b$ por esta cantidad positiva. La parte 3 produce

$$
a(ab)^{-1}<b(ab)^{-1}.
$$

Usando @prp-t1-0026,

$$
(ab)^{-1}=a^{-1}b^{-1},
$$

y simplificando,

$$
b^{-1}<a^{-1}.
$$

Como ambos inversos son positivos,

$$
0<\frac1b<\frac1a.
$$

Probemos la parte 8. Supongamos primero $ab>0$. Entonces $a\ne0$ y $b\ne0$ por @prp-t1-0027. Por tricotomía, $a>0$ o $a<0$.

Si $a>0$, dividir

$$
ab>0
$$

por el número positivo $a$ conserva el sentido y da

$$
b>0.
$$

Si $a<0$, dividir por $a$ invierte el sentido y produce

$$
b<0.
$$

Así, un producto positivo obliga a que los factores tengan el mismo signo. La recíproca se obtiene directamente de (O2) cuando ambos son positivos y, cuando ambos son negativos, escribiendo

$$
ab=(-a)(-b)
$$

con $-a>0$ y $-b>0$.

Supongamos ahora $ab<0$. Nuevamente $a,b\ne0$. Si $a>0$, dividir por $a$ conserva el sentido y da $b<0$; si $a<0$, dividir por $a$ invierte el sentido y da $b>0$. Recíprocamente, si los signos son opuestos, las reglas de signos convierten $ab$ en el negativo de un producto positivo. Esto prueba las dos equivalencias de la parte 8.

Para la parte 9 consideremos los tres casos que proporciona la tricotomía.

Si $a=0$, entonces

$$
a^2=0.
$$

Si $a>0$, (O2) da inmediatamente

$$
a^2>0.
$$

Si $a<0$, entonces $-a>0$ y, por (O2),

$$
(-a)^2>0.
$$

Como

$$
(-a)^2=a^2,
$$

volvemos a obtener $a^2>0$. En consecuencia,

$$
a^2\ge0
$$

para todo $a$, y la igualdad solo puede ocurrir cuando $a=0$.

Finalmente, probemos la parte 10. Supongamos

$$
0\le a\le b.
$$

De $a\le b$, sumando $-a$, obtenemos

$$
0\le b-a.
$$

Además, de $0\le a$, sumando $b$, resulta $b\le a+b$; combinando esto con $0\le b$ por transitividad,

$$
0\le a+b.
$$

El producto de dos números no negativos es no negativo: si alguno es $0$, el producto es $0$; si ambos son positivos, (O2) da un producto positivo. Por tanto,

$$
0\le(b-a)(a+b).
$$

Pero

$$
(b-a)(a+b)=b^2-a^2.
$$

Luego

$$
0\le b^2-a^2,
$$

y la parte 1 permite sumar $a^2$ a ambos miembros:

$$
a^2\le b^2.
$$

Esto demuestra las diez afirmaciones. $\blacksquare$

::: {.callout-note title="Después de la prueba"}
La proposición muestra que hay tres preguntas diferentes antes de «cancelar» un factor en una desigualdad:

1. ¿es el factor distinto de cero?;
2. ¿es positivo?;
3. ¿es negativo?

En una **igualdad**, para cancelar multiplicativamente basta la no nulidad.

En una **desigualdad**, la no nulidad no basta: el signo decide si el orden se conserva o se invierte.
:::

### Una pequeña tabla de control

Las reglas anteriores pueden condensarse, una vez demostradas, en la tabla siguiente.

| Operación aplicada a ambos miembros | Hipótesis | Efecto sobre $<$ |
|---|---|---|
| sumar $c$ | ninguna | conserva el sentido |
| restar $c$ | ninguna | conserva el sentido |
| multiplicar por $c$ | $c>0$ | conserva el sentido |
| multiplicar por $c$ | $c<0$ | invierte el sentido |
| dividir por $c$ | $c>0$ | conserva el sentido |
| dividir por $c$ | $c<0$ | invierte el sentido |

Si $c=0$, una desigualdad estricta desaparece al multiplicar ambos miembros por $c$: ambos productos se vuelven $0$.

La tabla es una herramienta de cálculo. La proposición anterior es su fundamento.

### Volvamos por un momento al ejemplo de Rudin

En §2.1 utilizamos un paso que entonces parecía familiar. Si $a$ y $b$ eran positivos y $b\le a$, escribimos

$$
b^2\le a^2.
$$

Ahora sabemos exactamente por qué: es la parte 10 de @prp-t1-0007. No era una propiedad misteriosa de los cuadrados, sino una consecuencia de la positividad y de la compatibilidad del orden con las operaciones del cuerpo.

Esta relectura muestra una ventaja del método axiomático. Podemos auditar una demostración preguntando:

> ¿qué propiedad estructural autoriza este paso?

En pruebas más largas, esa pregunta ayuda a distinguir una manipulación legítima de una inferencia que solo «parece razonable».

### Una desigualdad no es una ecuación: los pasos deben ser reversibles

Consideremos la desigualdad

$$
3x-7<8.
$$

Sumar $7$ a ambos miembros y después dividir por el número positivo $3$ produce

$$
3x<15
$$

y luego

$$
x<5.
$$

Esto demuestra que toda solución de la desigualdad original satisface $x<5$.

Pero si queremos afirmar que **el conjunto de soluciones es exactamente** $(-\infty,5)$, debemos justificar también la dirección inversa. Si $x<5$, multiplicar por $3>0$ y restar $7$ produce

$$
3x<15
\quad\Longrightarrow\quad
3x-7<8.
$$

Como todos los pasos utilizados son equivalencias, obtenemos

$$
3x-7<8
\iff
x<5.
$$

Esta pequeña auditoría anticipa una regla importante para resolver inecuaciones:

$$
\boxed{
\text{una cadena de transformaciones encuentra el conjunto solución solo si controlamos cuáles pasos son reversibles.}
}
$$

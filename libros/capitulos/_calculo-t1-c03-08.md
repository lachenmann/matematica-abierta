## Funciones por tramos y transformaciones de gráficas {#sec-t1-c03-08}

En §3.7 aprendimos a leer una gráfica como un conjunto de pares ordenados. Esa perspectiva permite ahora hacer algo más activo: **construir funciones a partir de varias reglas** y **predecir cómo cambia su gráfica cuando modificamos algebraicamente la función**.

En ambos casos mantendremos la misma disciplina que ha guiado todo el capítulo:

$$
\boxed{\text{primero identificamos la función; después interpretamos su gráfica}.}
$$

No comenzaremos memorizando frases como «sumar afuera desplaza hacia arriba» o «restar adentro desplaza hacia la derecha». Esas reglas son correctas cuando se formulan con sus hipótesis, pero resultan mucho más seguras si podemos reconstruirlas a partir de la igualdad que define cada punto de la gráfica.

### Una función puede usar reglas diferentes en partes diferentes del dominio

No existe ninguna exigencia matemática de que una función deba estar descrita por una única fórmula en todo su dominio.

Supongamos que queremos definir una función

$$
f\colon A\to\mathbb R
$$

mediante subconjuntos $A_1,\dots,A_n\subseteq A$ y reglas $r_1,\dots,r_n$. Esquemáticamente escribiríamos

$$
f(x)=
\begin{cases}
r_1(x),&x\in A_1,\\
r_2(x),&x\in A_2,\\
\vdots&\vdots\\
r_n(x),&x\in A_n.
\end{cases}
$$

Para que esta escritura determine realmente una función sobre **todo** $A$, debemos volver a las dos exigencias de §3.1: existencia y unicidad.

#### Existencia: ningún punto del dominio puede quedar sin regla

Necesitamos

$$
A=A_1\cup\cdots\cup A_n.
$$

Si algún $x\in A$ no pertenece a ninguno de los conjuntos $A_i$, la receta no dice qué valor debe tener $f(x)$. En ese punto fallaría la existencia de una salida.

#### Unicidad: un punto cubierto por varias reglas no puede recibir valores incompatibles

No es necesario que los conjuntos $A_i$ sean disjuntos. Pueden solaparse, pero entonces las reglas deben ser compatibles en cada solapamiento.

Si

$$
x\in A_i\cap A_j,
$$

debemos tener

$$
r_i(x)=r_j(x).
$$

De lo contrario, la misma entrada recibiría dos valores distintos y la receta no definiría una función.

Así, la definición por tramos no introduce una noción nueva de función. Solo reutiliza la definición ya conocida:

$$
\boxed{
\begin{array}{c}
\text{los tramos deben cubrir el dominio}\\[2pt]
\text{y deben concordar allí donde se superponen.}
\end{array}}
$$

### El valor absoluto como primer modelo

La función valor absoluto puede escribirse como

$$
|x|=
\begin{cases}
-x,&x<0,\\
x,&x\ge0.
\end{cases}
$$

Los dos tramos cubren todo $\mathbb R$ y no se superponen, de modo que no existe ambigüedad.

También podríamos escribir

$$
|x|=
\begin{cases}
-x,&x\le0,\\
x,&x\ge0.
\end{cases}
$$

Ahora los tramos se superponen en $x=0$, pero las dos fórmulas producen allí el mismo valor:

$$
-0=0.
$$

Por tanto, la segunda receta también define exactamente la misma función.

En cambio,

$$
h(x)=
\begin{cases}
-x+1,&x\le0,\\
x,&x\ge0
\end{cases}
$$

**no** define una función sobre $\mathbb R$, porque en el punto de solapamiento obtenemos dos instrucciones incompatibles:

$$
-0+1=1,
\qquad
0=0.
$$

La entrada $0$ tendría dos salidas.

::: {.callout-note title="Lectura estructural"}
Cuando veas una definición por tramos, no empieces dibujando. Comprueba primero:

1. cuál es el dominio declarado;
2. si los tramos lo cubren por completo;
3. si hay puntos que pertenecen a más de un tramo;
4. si las fórmulas coinciden en esos puntos.

Solo después la receta está auditada como función.
:::

### Fórmulas familiares y dominios naturales

Las funciones por tramos amplían el repertorio, pero también conviene ordenar las familias de expresiones que ya conocemos.

Una función **polinómica**, por ejemplo

$$
p(x)=x^3-2x+1,
$$

puede evaluarse para todo $x\in\mathbb R$. Si no se declara otra cosa, su dominio natural es $\mathbb R$.

Una expresión **racional**

$$
r(x)=\frac{p(x)}{q(x)}
$$

solo puede evaluarse donde

$$
q(x)\ne0.
$$

Por ejemplo,

$$
r(x)=\frac{1}{x^2-1}
$$

tiene como dominio natural

$$
\mathbb R\setminus\{-1,1\}.
$$

Una expresión **algebraica** que contiene una raíz cuadrada real exige que el radicando sea no negativo. Por ejemplo,

$$
s(x)=\sqrt{4-x^2}
$$

requiere

$$
4-x^2\ge0,
$$

es decir,

$$
-2\le x\le2.
$$

Por tanto, su dominio natural es

$$
[-2,2].
$$

Entre las funciones trigonométricas conocidas, $\sin x$ y $\cos x$ están definidas para todo real, mientras que una expresión como

$$
\tan x=\frac{\sin x}{\cos x}
$$

solo está definida donde $\cos x\ne0$.

Estas observaciones conducen a una convención útil, pero debemos formularla con cuidado:

> cuando se proporciona **solo una expresión** y se pide su dominio natural, buscamos el mayor subconjunto de $\mathbb R$ en el que todas las operaciones indicadas están definidas.

Esto no reemplaza el dominio como parte de los datos de una función. Podemos restringir deliberadamente una expresión a un dominio menor. Por ejemplo,

$$
p\colon[0,1]\to\mathbb R,
\qquad
p(x)=x^3-2x+1,
$$

es una función perfectamente legítima aunque la fórmula polinómica tenga sentido fuera de $[0,1]$.

La distinción permanece:

$$
\boxed{
\text{dominio natural de una expresión}
\neq
\text{dominio declarado de toda función que use esa expresión}.}
$$

### Transformar una gráfica significa transformar sus puntos

Fijemos ahora una función real

$$
f\colon D\to\mathbb R
$$

y un punto cualquiera de su gráfica:

$$
(u,f(u))\in\Gamma_f.
$$

Para entender una transformación, seguiremos ese punto. Preguntaremos qué punto de la nueva gráfica contiene **el mismo valor**, una versión modificada de ese valor o una entrada modificada.

Este método evita casi todas las reglas mnemotécnicas problemáticas.

### Desplazamiento vertical: $f(x)+c$

Definamos

$$
g(x)=f(x)+c.
$$

El dominio de $g$ es el mismo $D$, porque no hemos cambiado la entrada que introducimos en $f$.

Si

$$
y=f(u),
$$

entonces

$$
g(u)=f(u)+c=y+c.
$$

Por tanto, el punto

$$
(u,y)
$$

de la gráfica original se convierte en

$$
(u,y+c).
$$

La primera coordenada permanece fija y la segunda aumenta en $c$. Si $c>0$, todos los puntos se desplazan $c$ unidades hacia arriba; si $c<0$, se desplazan $|c|$ unidades hacia abajo.

En símbolos,

$$
\boxed{(u,y)\longmapsto(u,y+c).}
$$

### Desplazamiento horizontal: $f(x-c)$

Definamos ahora

$$
h(x)=f(x-c).
$$

Aquí sí hemos cambiado la entrada de $f$. Antes de hablar de la gráfica debemos auditar el dominio:

$$
x\in\operatorname{Dom}(h)
\iff
x-c\in D.
$$

Tomemos nuevamente un punto original

$$
(u,f(u)).
$$

¿En qué entrada de $h$ reaparece el valor $f(u)$? Debemos resolver

$$
x-c=u.
$$

Por tanto,

$$
x=u+c.
$$

y

$$
h(u+c)=f((u+c)-c)=f(u).
$$

Así,

$$
\boxed{(u,y)\longmapsto(u+c,y).}
$$

Si $c>0$, la gráfica se desplaza $c$ unidades **hacia la derecha**.

El signo puede parecer contrario a la intuición superficial porque dentro de la fórmula aparece $x-c$. Pero el desplazamiento no se adivina mirando el signo: se obtiene resolviendo

$$
x-c=u.
$$

::: {.callout-warning title="Error frecuente: el signo del desplazamiento horizontal"}
No confundas

$$
f(x)+c
$$

con

$$
f(x-c).
$$

La primera operación modifica la **salida**:

$$
(u,y)\mapsto(u,y+c).
$$

La segunda modifica la **entrada necesaria para obtener el mismo valor**:

$$
(u,y)\mapsto(u+c,y).
$$

En particular, para $c>0$,

$$
f(x-c)
$$

se desplaza hacia la **derecha**, no hacia la izquierda.

Si dudas, no memorices: fija un punto $u$ de la función original y resuelve $x-c=u$.
:::

Un ejemplo especialmente transparente es

$$
f(x)=\sqrt{x},
\qquad x\ge0.
$$

Entonces

$$
h(x)=\sqrt{x-3}
$$

solo está definida cuando

$$
x-3\ge0,
$$

es decir, cuando $x\ge3$. El dominio $[0,\infty)$ se ha desplazado a $[3,\infty)$, exactamente como predice la transformación horizontal.

### Reflexión respecto del eje horizontal: $-f(x)$

Sea

$$
g(x)=-f(x).
$$

Para cada $u\in D$,

$$
g(u)=-f(u).
$$

Por tanto,

$$
\boxed{(u,y)\longmapsto(u,-y).}
$$

La primera coordenada permanece fija y cambia el signo de la segunda. Geométricamente, la gráfica se refleja respecto del eje horizontal.

### Reflexión respecto del eje vertical: $f(-x)$

Sea ahora

$$
h(x)=f(-x).
$$

Su dominio es

$$
\{x\in\mathbb R:-x\in D\}.
$$

Si $u\in D$, buscamos la entrada $x$ que satisface

$$
-x=u.
$$

Entonces

$$
x=-u
$$

y

$$
h(-u)=f(u).
$$

Así,

$$
\boxed{(u,y)\longmapsto(-u,y).}
$$

Cambia el signo de la primera coordenada y se conserva la segunda: obtenemos una reflexión respecto del eje vertical.

Las dos reflexiones muestran otra vez la diferencia entre modificar una salida y modificar una entrada:

$$
\boxed{
\begin{array}{rcl}
-f(x)&:&(u,y)\mapsto(u,-y),\\[4pt]
f(-x)&:&(u,y)\mapsto(-u,y).
\end{array}}
$$

### Escalas verticales y horizontales: $a f(bx)$

Consideremos

$$
g(x)=a f(bx).
$$

Supongamos primero que

$$
a\ne0,
\qquad
b\ne0.
$$

Si $(u,y)$ pertenece a la gráfica de $f$, entonces queremos elegir $x$ de manera que

$$
bx=u.
$$

Por tanto,

$$
x=\frac{u}{b}.
$$

En esa entrada,

$$
g\!\left(\frac{u}{b}\right)
=
a f(u)
=
ay.
$$

Así, la transformación completa de los puntos es

$$
\boxed{
(u,y)
\longmapsto
\left(\frac{u}{b},ay\right).}
$$

El factor $a$ actúa directamente sobre las alturas:

- si $|a|>1$, las distancias verticales al eje horizontal se multiplican por $|a|$;
- si $0<|a|<1$, se reducen por ese factor;
- si $a<0$, además aparece la reflexión respecto del eje horizontal.

El factor $b$ actúa de modo recíproco sobre las coordenadas horizontales:

- si $|b|>1$, las coordenadas horizontales se dividen por un número mayor que $1$ y la gráfica se comprime horizontalmente;
- si $0<|b|<1$, se dilata horizontalmente;
- si $b<0$, además aparece la reflexión respecto del eje vertical.

La reciprocidad $u\mapsto u/b$ no es una convención gráfica: procede directamente de resolver $bx=u$.

También el dominio debe transformarse. Si $D$ es el dominio de $f$, entonces

$$
\operatorname{Dom}(g)
=
\{x\in\mathbb R:bx\in D\}.
$$

Los casos $a=0$ o $b=0$ son degenerados y deben analizarse por la definición, no por prolongación automática de la regla geométrica. Si $a=0$, todos los valores de una función ya definida se convierten en $0$. Si $b=0$, la expresión exige evaluar $f(0)$; solo tiene sentido si $0\in D$, y entonces la dependencia respecto de $x$ desaparece en la parte interior.

### La composición unifica las transformaciones

La notación de composición de §3.4 permite ver que no estamos acumulando cinco trucos aislados.

Definamos, para $c,a\in\mathbb R$,

$$
\tau_c(x)=x+c,
\qquad
\sigma_a(x)=ax.
$$

Siempre que los dominios permitan las composiciones correspondientes, tenemos

$$
f(x)+c
=
(\tau_c\circ f)(x),
$$

$$
f(x-c)
=
(f\circ\tau_{-c})(x),
$$

$$
-f(x)
=
(\sigma_{-1}\circ f)(x),
$$

$$
f(-x)
=
(f\circ\sigma_{-1})(x),
$$

y

$$
a f(bx)
=
(\sigma_a\circ f\circ\sigma_b)(x).
$$

Esto explica la diferencia fundamental entre transformaciones «de afuera» y «de adentro»:

- componer **después** de $f$ modifica las salidas;
- componer **antes** de $f$ modifica las entradas que llegan a $f$.

La geometría refleja ese orden algebraico.

### Un ejemplo completo: construir por tramos y transformar

::: {#exm-t1-0028}
**Una función por tramos bajo varias transformaciones.** Definamos

$$
p\colon[-1,2]\to\mathbb R
$$

mediante

$$
p(x)=
\begin{cases}
x+1,&-1\le x\le0,\\[2pt]
1-\dfrac{x}{2},&0\le x\le2.
\end{cases}
$$

Los dos tramos cubren $[-1,2]$. Se superponen únicamente en $x=0$, y allí coinciden:

$$
0+1
=
1
=
1-\frac02.
$$

Por tanto, la receta define una función.

La primera rama recorre valores desde $0$ hasta $1$, y la segunda vuelve desde $1$ hasta $0$. Así,

$$
p([-1,2])=[0,1].
$$

Ahora sigamos varias transformaciones.

**1. Desplazamiento vertical.** Sea

$$
q(x)=p(x)+2.
$$

El dominio permanece $[-1,2]$ y

$$
q(x)=
\begin{cases}
x+3,&-1\le x\le0,\\[2pt]
3-\dfrac{x}{2},&0\le x\le2.
\end{cases}
$$

Cada punto $(u,y)$ pasa a $(u,y+2)$, y la imagen pasa de $[0,1]$ a

$$
[2,3].
$$

**2. Desplazamiento horizontal.** Sea

$$
r(x)=p(x-3).
$$

La condición $x-3\in[-1,2]$ equivale a

$$
2\le x\le5.
$$

Por tanto, el dominio nuevo es $[2,5]$. Sustituyendo cuidadosamente en cada tramo,

$$
r(x)=
\begin{cases}
x-2,&2\le x\le3,\\[2pt]
\dfrac{5-x}{2},&3\le x\le5.
\end{cases}
$$

La gráfica completa se ha desplazado tres unidades hacia la derecha:

$$
(u,y)\longmapsto(u+3,y).
$$

**3. Dos reflexiones.** Sea

$$
s(x)=-p(-x).
$$

La sustitución interior $-x$ refleja primero las entradas; el signo exterior refleja después las salidas. El dominio es $[-2,1]$ y, desarrollando los tramos,

$$
s(x)=
\begin{cases}
-1-\dfrac{x}{2},&-2\le x\le0,\\[4pt]
x-1,&0\le x\le1.
\end{cases}
$$

Cada punto de la gráfica original se transforma según

$$
(u,y)\longmapsto(-u,-y).
$$

**4. Cambio simultáneo de escalas.** Finalmente, sea

$$
t(x)=2p(2x).
$$

Como $2x\in[-1,2]$, el dominio es

$$
\left[-\frac12,1\right].
$$

Además,

$$
t(x)=
\begin{cases}
4x+2,&-\dfrac12\le x\le0,\\[4pt]
2-2x,&0\le x\le1.
\end{cases}
$$

Los puntos obedecen a

$$
(u,y)\longmapsto\left(\frac{u}{2},2y\right).
$$

La gráfica se comprime horizontalmente por un factor $2$ y las alturas se duplican. La imagen es ahora

$$
[0,2].
$$

En los cuatro casos no hemos necesitado adivinar la nueva gráfica: cada cambio se dedujo de la nueva regla y de su dominio.
:::

### Un protocolo seguro para transformar funciones

Cuando aparezca una expresión construida a partir de una función conocida, conviene seguir siempre este orden:

1. **Escribe la nueva función.** No trabajes todavía con el dibujo.
2. **Audita su dominio.** Las modificaciones interiores pueden cambiarlo.
3. **Fija un punto original $(u,f(u))$.**
4. **Resuelve qué nueva entrada produce el valor relacionado con $f(u)$.**
5. **Calcula la nueva salida.**
6. **Obtén la transformación de coordenadas.**
7. **Solo entonces interpreta desplazamiento, reflexión o cambio de escala.**

Este procedimiento es algo más lento que memorizar una tabla la primera vez, pero es mucho más robusto. Además, funciona también cuando varias transformaciones aparecen combinadas.

Podemos resumir las transformaciones básicas, para los casos en que las expresiones estén definidas, del siguiente modo:

$$
\boxed{
\begin{array}{rcl}
f(x)+c
&:&(u,y)\mapsto(u,y+c),\\[4pt]
f(x-c)
&:&(u,y)\mapsto(u+c,y),\\[4pt]
-f(x)
&:&(u,y)\mapsto(u,-y),\\[4pt]
f(-x)
&:&(u,y)\mapsto(-u,y),\\[4pt]
a f(bx)
&:&(u,y)\mapsto\left(\dfrac{u}{b},ay\right),\quad ab\ne0.
\end{array}}
$$

La tabla es ahora una **consecuencia** de los cálculos anteriores, no un sustituto de ellos.

En §3.9 añadiremos una propiedad cualitativa nueva que depende del orden del dominio: estudiaremos cómo comparar las salidas correspondientes a entradas ordenadas y por qué ciertas funciones pueden invertirse después de restringir adecuadamente su dominio. Hasta entonces, todo lo que hemos hecho en esta sección depende solo de la definición de función, de su dominio, de la composición y de la representación mediante pares ordenados.

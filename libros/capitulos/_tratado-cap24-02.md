## 24.2. Distancias admitidas y radio de convergencia {#sec-ta-24-2}

El teorema anterior afirma que la convergencia en un punto distinto del centro impone convergencia absoluta a distancias estrictamente menores. Para transformar esta propiedad en una frontera numérica necesitamos aislar las distancias admitidas; tomar directamente el supremo del conjunto de convergencia sería incorrecto, porque éste contiene puntos a ambos lados de $c$ y puede ser no acotado. Tampoco podemos escribir un supremo real sin verificar antes que el conjunto correspondiente es no vacío y está acotado superiormente.

### Definición 24.2.1 — Conjunto de distancias admitidas
Para $a:\mathbb N\to\mathbb R$ y $c\in\mathbb R$ dados, definimos

$$
\boxed{D(a,c):=\{d\in\mathbb R: d\ge0\ \land\
\exists x\in C(a,c)\ (d=|x-c|)\}.}
\tag{24.2.1}
$$

Separación sobre $\mathbb R$ demuestra que $D(a,c)$ es un conjunto. Es exactamente el conjunto de las distancias al centro de los puntos de convergencia; la fórmula no pide seleccionar un punto para cada distancia. La proposición «El centro siempre pertenece al conjunto de convergencia» proporciona el testigo explícito $x=c$, de modo que

$$
\boxed{0\in D(a,c)\subseteq\{d\in\mathbb R:d\ge0\}.}
\tag{24.2.2}
$$

### Proposición 24.2.2 — Herencia de las distancias menores
Si $d\in D(a,c)$ y $t\in\mathbb R$ satisface $0\le t\le d$, entonces $t\in D(a,c)$. Más precisamente, cuando $0\le t<d$, las series evaluadas en ambos puntos $c+t$ y $c-t$ convergen absolutamente.

**Demostración.**
La pertenencia $d\in D(a,c)$ entrega un punto $y\in C(a,c)$ con $|y-c|=d$. Si $t=d$, la conclusión $t\in D(a,c)$ ya está dada. Si $0\le t<d$, necesariamente $d>0$ y $y\ne c$. Los puntos explícitos $x_+:=c+t$ y $x_-:=c-t$ satisfacen

$$
|x_+-c|=|x_--c|=t<d=|y-c|.
$$

El teorema «Convergencia absoluta hacia el interior», aplicado por separado a estos dos puntos, demuestra su convergencia absoluta. Por definición pertenecen a $C(a,c)$, y cualquiera de ellos testimonia que $t\in D(a,c)$. No fue necesario elegir una función de testigos indexada por las distancias. $\square$

**Interpretación.** $D(a,c)$ es un segmento inicial de los reales no negativos: una distancia admitida no puede estar precedida por una distancia inadmisible. Esto no afirma todavía que la distancia frontera pertenezca a $D(a,c)$.

### Definición 24.2.3 — Radio finito y radio infinito
Distinguimos dos casos excluyentes para el conjunto no vacío $D(a,c)$:

1. **Caso acotado.** Si existe $B\in\mathbb R$ que acota superiormente a $D(a,c)$, la propiedad del supremo de $\mathbb R$ («Propiedad del supremo y cuerpo ordenado completo», disponible estructuralmente por «Existencia y caracterización única de la completación ordenada de $\mathbb Q$») y su unicidad («Unicidad de supremo e ínfimo») proporcionan un único real
   $$
   \boxed{R(a,c):=\sup D(a,c)\in\mathbb R,\qquad R(a,c)\ge0.}
   \tag{24.2.3}
   $$
   Lo llamamos radio finito de convergencia; incluye el caso $R(a,c)=0$.
2. **Caso no acotado superiormente.** Decimos que el radio es infinito y escribimos, por convenio,
   $$
   \boxed{R(a,c)=+\infty.}
   \tag{24.2.4}
   $$
   Aquí $+\infty$ es una *marca formal de caso*, distinta de cualquier número real. (24.2.4) no define un supremo real de un conjunto no acotado ni introduce operaciones con infinitos.

La lógica clásica garantiza que exactamente uno de los casos ocurre. En el caso acotado las condiciones de existencia del supremo se verificaron antes de utilizarlo: $0\in D(a,c)$ asegura no vacuidad; el acotamiento es la hipótesis expresa de ese caso. En el otro caso no escribimos $\sup D(a,c)$ como si fuese un elemento de $\mathbb R$.

### Teorema 24.2.4 — Clasificación por el radio y convergencia interior
Para cualquier serie real de potencias centrada en $c$ vale exactamente una de las siguientes alternativas.

**(i) Radio cero.** Si $R(a,c)=0$, entonces $C(a,c)=\{c\}$.

**(ii) Radio finito positivo.** Si $R:=R(a,c)\in\mathbb R$ y $R>0$, entonces

$$
\boxed{|x-c|<R\ \Longrightarrow\
\sum_{n=0}^{\infty}a_n(x-c)^n\text{ converge absolutamente},}
\tag{24.2.5}
$$

$$
\boxed{|x-c|>R\ \Longrightarrow\
\sum_{n=0}^{\infty}a_n(x-c)^n\text{ diverge}.}
\tag{24.2.6}
$$

**(iii) Radio infinito.** Si $R(a,c)=+\infty$, la serie converge absolutamente para todo $x\in\mathbb R$ y $C(a,c)=\mathbb R$.

**Demostración.**
**Caso (i).** Si $R=\sup D=0$, todo $d\in D$ cumple $0\le d\le0$, de modo que $D=\{0\}$. Para $x\in C(a,c)$, $|x-c|\in D$; luego $|x-c|=0$ y $x=c$. La inclusión inversa $c\in C(a,c)$ es «El centro siempre pertenece al conjunto de convergencia».

**Caso (ii): interior.** Sea $x\in\mathbb R$ con $d:=|x-c|<R$. Por definición, $R$ es la menor cota superior de $D$. Por tanto $d$ no puede ser cota superior: en caso contrario $R\le d$, contra $d<R$. Existe, pues, $e\in D$ con $e>d$. Tomemos el testigo de esa pertenencia, un punto $y\in C(a,c)$ con $|y-c|=e$. Como $e>d\ge0$, se tiene $e>0$ y $y\ne c$. Aplicando «Convergencia absoluta hacia el interior» a $|x-c|=d<e=|y-c|$ obtenemos convergencia absoluta en $x$. La demostración vale también para $x=c$, sin efectuar ninguna división por $x-c$.

**Caso (ii): exterior.** Si $d:=|x-c|>R$ y la serie convergiese en $x$, entonces $x\in C(a,c)$, por lo que $d\in D(a,c)$. Pero $R=\sup D$ es una cota superior y obligaría a $d\le R$, contradicción. La serie diverge por la definición de convergencia numérica.

**Caso (iii).** Fijemos un real $x$ y pongamos $d:=|x-c|$. La falta de cota superior de $D$ implica que existe $e\in D$ con $e>d$. Como antes, un punto $y\in C(a,c)$ a distancia $e>0$ permite aplicar «Convergencia absoluta hacia el interior» y concluir convergencia absoluta en $x$. Puesto que $x$ era arbitrario, $C(a,c)=\mathbb R$.

Por último, el caso finito se separa exhaustivamente en $R=0$ y $R>0$, pues $R\ge0$; el caso no acotado es excluyente del caso finito. Ninguna etapa emplea un conjunto de testigos escogidos de manera simultánea. $\square$

**Advertencia decisiva.** Las dos desigualdades de (24.2.5)–(24.2.6) son *estrictas*. El teorema no resuelve el caso $|x-c|=R$ y no permite reemplazar $<$ por $\le$ en la afirmación de convergencia.

### Corolario 24.2.5 — Forma exacta del conjunto de convergencia salvo los extremos
Si el radio $R:=R(a,c)$ es un real estrictamente positivo, entonces existe el conjunto explícito

$$
E_{a,c}:=C(a,c)\cap\{c-R,c+R\}\subseteq\{c-R,c+R\}
$$

y se cumple la igualdad de conjuntos

$$
\boxed{C(a,c)=(c-R,c+R)\cup E_{a,c}.}
\tag{24.2.7}
$$

Si el radio es cero, $C(a,c)=\{c\}$; si es infinito, $C(a,c)=\mathbb R$.

**Demostración.**
Sea $R>0$ finito. El teorema anterior demuestra que todos los puntos con $|x-c|<R$ pertenecen a $C(a,c)$ y que ninguno con $|x-c|>R$ pertenece. La primera condición equivale a $c-R<x<c+R$; la única posibilidad restante para un punto convergente es $|x-c|=R$, equivalente a $x=c-R$ o $x=c+R$. Intersectar el conjunto existente $C(a,c)$ con ese par existente produce $E_{a,c}$ sin seleccionar extremos. Así se prueban ambas inclusiones de (24.2.7). Los otros dos casos son las conclusiones (i) y (iii) de «Clasificación por el radio y convergencia interior». $\square$

El conjunto $E_{a,c}$ puede ser vacío, tener un elemento o contener ambos extremos; aquí no se afirma que cada posibilidad esté realizada. Se investigará con ejemplos y criterios separados, sin trasladar automáticamente la convergencia de un extremo al otro.

### Proposición 24.2.6 — Realización de los tres tipos de radio
Para cualquier centro real $c$ hay series de potencias con radio cero y con radio infinito. Además, para cada real dado $r>0$ hay una serie centrada en $c$ cuyo radio es exactamente $r$.

**Demostración.**
**Radio infinito.** Tomemos $a_0=1$ y $a_n=0$ para $n\ge1$. Para cualquier real $x$, la sucesión de sumas parciales es constantemente $1$, por lo que converge absolutamente. Así $C(a,c)=\mathbb R$, las distancias admitidas son todos los reales no negativos (para $d\ge0$, basta $x=c+d$) y son no acotadas por la arquimedianidad. El radio es infinito.

**Radio finito prescrito.** Fijemos $r>0$ y tomemos $a_n=(1/r)^n$ para todo $n\in\mathbb N$. La serie en $x$ es exactamente la serie geométrica de razón $(x-c)/r$, pues la regla de potencias de un producto se demuestra por la misma inducción de (24.1.13). Según la clasificación cerrada «Clasificación completa de la convergencia de la serie geométrica», converge precisamente cuando $|(x-c)/r|<1$, o equivalentemente $|x-c|<r$. Por tanto $D(a,c)=[0,r)$: si $0\le d<r$, el punto explícito $c+d$ converge; y ninguna distancia $d\ge r$ lo hace. El conjunto es no vacío y está acotado, y su supremo es $r$: $r$ es cota superior y, si $b<r$, el punto medio entre $\max\{b,0\}$ y $r$ pertenece a $D$ y supera a $b$. Luego $R(a,c)=r$.

**Radio cero.** Para cada $n\in\mathbb N$ fijemos el coeficiente $a_n=\nu_{\mathbb R}(n)^n$, con $0^0=1$ conforme a «Potencias naturales de un número real». Esto define una única sucesión de coeficientes por Separación sobre $\mathbb N\times\mathbb R$. En el centro la serie converge, como siempre. Si $x\ne c$, ponemos $h:=|x-c|>0$. La propiedad arquimediana «Todo cuerpo ordenado completo es arquimediano» da un natural $N\ge1$ tal que $\nu_{\mathbb R}(N)h\ge1$. Como los numerales reales preservan el orden natural, para todo $n\ge N$ se tiene $\nu_{\mathbb R}(n)h\ge1$; por inducción sobre el exponente,

$$
|a_n(x-c)^n|=\bigl(\nu_{\mathbb R}(n)h\bigr)^n\ge1.
$$

El término general no tiende a cero, de modo que la serie diverge por «Condición necesaria de convergencia: el término general tiende a cero». En consecuencia $C(a,c)=\{c\}$, $D(a,c)=\{0\}$ y $R(a,c)=0$. Todos los coeficientes fueron definidos mediante operaciones únicas sobre objetos dados; no se invocó elección. $\square$

**Transición.** Hemos obtenido la frontera del conjunto de convergencia sin una fórmula para calcular el radio a partir de los coeficientes. Antes de abordar el criterio de Cauchy–Hadamard y la convergencia uniforme interior, corresponde examinar las dos evaluaciones $x=c-R$ y $x=c+R$ cuando $R$ es finito y positivo: la convergencia de una no autoriza por sí sola inferir la de la otra y tampoco puede decidirse su comportamiento por las desigualdades estrictas anteriores.

---

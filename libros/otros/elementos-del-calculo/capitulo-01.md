---
title: Capítulo 1. Tangentes, velocidades y variación
status: published
draft: false
book-id: MA-BOK-0015
editorial-project: EDC
date-modified: '2026-10-12'
license: GFDL-1.3-or-later
areas:
  - calculo
  - analisis
  - fundamentos
level: intermedio
topics:
  - calculo-de-una-variable
  - historia-de-las-matematicas
number-sections: false
provenance:
  type: original
  sources:
    - role: idea
      note: 'Inspiración metodológica: Gabor Toth, Elements of Mathematics (2021); obra independiente.'
source-id: EDC-C01
source-sha256: f96ddd0913eed76cdb380c65be21965e755d7f781bfb50ccff3f9991e6dda06b
content-id: MA-BCH-0332
content-type: book-chapter
related:
  - MA-BOK-0015
---

[Índice del libro](index.html) · [Prefacio](prefacio.html) · [Itinerarios](itinerarios.html)

[Exposición](capitulo-01.html) · [Ejercicios](capitulo-01-ejercicios.html) · [Soluciones](capitulo-01-soluciones.html) · [Notas históricas](capitulo-01-notas.html)

[← Capítulo 0](capitulo-00.html) · [Capítulo 2 →](capitulo-02.html)

> **Pregunta generadora.** ¿Cómo asignar a una curva una inclinación en un punto y a un móvil una velocidad en un instante, sin dividir por un incremento que ya se ha hecho cero?

Hay una diferencia entre conocer dos valores y conocer cómo cambia una magnitud en un lugar preciso. El álgebra permite calcular $f(a)$ y $f(a+h)$; la geometría permite unir los correspondientes puntos de una gráfica por una recta. Pero el problema de la tangente exige una inclinación **local**, y el problema de la velocidad exige una razón de cambio **instantánea**. Ninguno se resuelve simplemente sustituyendo $h=0$ en una división por $h$.

En el capítulo anterior aprendimos a trabajar con límites reales, a distinguirlos del valor de una función y a justificar las consecuencias de la continuidad. Ahora podremos dar el paso decisivo: reconocer cuándo las razones de cambio calculadas sobre intervalos cada vez más cortos convergen a un número. Ese número será la **derivada**. No presentaremos todavía un catálogo de fórmulas; primero estudiaremos qué significa que la derivada exista, qué información proporciona y qué no autoriza a concluir.

## 1.1. Una secante que se aproxima, pero no se anula

Volvamos a $f(x)=x^2$, el primer problema de [C00, §0.1](capitulo-00.html). Fijemos $a\in\mathbb R$. La recta por $P=(a,a^2)$ y $Q_h=(a+h,(a+h)^2)$, para $h\ne0$, tiene pendiente

$$
\frac{(a+h)^2-a^2}{(a+h)-a}=2a+h.
$$

Mientras $h\ne0$, **la recta es secante**, no la recta que todavía buscamos. Al hacer que $h$ tienda a cero, la pendiente se acerca a $2a$. El numerador y el denominador originales tienden a cero, pero el **cociente** ya simplificado tiene un límite finito. Esto no es el cálculo ilegítimo $0/0$: es el estudio de una función definida para incrementos no nulos.

La ecuación de esas secantes, escrita tomando siempre como punto de paso $P$, es

$$
y=a^2+(2a+h)(x-a).
$$

Cuando sus pendientes convergen a $2a$, la recta candidata es

$$
y=a^2+2a(x-a).
$$

¿Podemos llamar «tangente» a esta recta? Sí, cuando precisemos qué significa aproximar la gráfica **hasta el primer orden**. Pero ni todos los cocientes incrementales tienen límite, ni una definición basada exclusivamente en «tocar una sola vez» funciona para cualquier curva.

<figure id="fig-edc-c01-01" class="quarto-float-fig">
<img src="/assets/books/elementos-del-calculo/EDC-C01-F01_SECANTE_TANGENTE.svg" alt="Parábola negra y=x²; secante roja discontinua por los puntos P y Qh; tangente azul en P. La pendiente secante vale 2a+h y converge a 2a.">
<figcaption>Figura 1.1. La secante y la tangente cumplen ecuaciones diferentes; su coincidencia en el límite exige el cociente incremental.</figcaption>
</figure>



## 1.2. De la geometría al movimiento: dos problemas distintos

La recta tangente a una circunferencia sugiere una línea que tiene con ella un contacto singular. No es una definición que se traslade sin más a las gráficas de funciones. Por ejemplo, la recta $y=0$ atraviesa la curva $y=x^3$ en el origen: a pesar de cruzarla, será su tangente en el sentido diferencial. Tampoco basta pedir que una recta comparta un único punto con la gráfica: esa condición depende de toda la gráfica y no de lo que sucede cerca del punto.

Por otra parte, una posición $s(t)$ se mide en unidades de longitud y el tiempo $t$ en unidades temporales. Para $t$ y $t+h$ del dominio físico, la razón

$$
\frac{s(t+h)-s(t)}{h},\qquad h\ne0,
$$

mide **desplazamiento dividido por tiempo transcurrido**. Es una velocidad media *con signo* en el intervalo. No equivale necesariamente a la rapidez media: un movimiento puede avanzar y retroceder, de modo que el desplazamiento neto sea cero sin que la distancia recorrida lo sea.

Consideremos el modelo algebraico $s(t)=s_0+v_0t+ct^2$, con $t\ge0$. Para $h\ne0$ permitido por el dominio,

$$
\frac{s(t+h)-s(t)}h=v_0+2ct+ch.
$$

Por tanto, las velocidades medias se aproximan a $v_0+2ct$ cuando $h\to0$. Si $c$ tiene dimensiones de longitud/tiempo$^2$, la expresión resultante tiene dimensiones de longitud/tiempo, como corresponde. **El límite es una afirmación matemática** acerca del modelo; su interpretación como una ley del movimiento exige, adicionalmente, que el modelo sea adecuado a la situación física.

**Nota histórica H1.** El estudio galileano de la caída uniformemente acelerada proporciona una motivación histórica para la relación entre distancia y cuadrado del tiempo. No afirmamos que Galileo formulara una derivada mediante límites modernos: véanse [notas históricas H1–H5](capitulo-01-notas.html).

## 1.3. La razón de cambio media

**Definición 1.1 (`EDC-C01-DEF-001`).** Sea $f:D\to\mathbb R$, donde $D\subseteq\mathbb R$, y sean $a,b\in D$ con $a\ne b$. La **razón de cambio media** de $f$ entre $a$ y $b$ es

$$
M_f(a,b)=\frac{f(b)-f(a)}{b-a}.
$$

Para $b=a+h$ escribiremos $Q_f(a,h)=M_f(a,a+h)$, de modo que

$$
Q_f(a,h)=\frac{f(a+h)-f(a)}h,
\qquad h\ne0,\quad a,a+h\in D.
$$

Las dos variables de $M_f$ son puntos del dominio; la segunda variable de $Q_f$ es un **incremento**. Conviene no confundir estos papeles. Si $f$ representa una posición, $Q_f$ es una velocidad media con signo; si $f$ representa temperatura en función del tiempo, sus unidades serán grados por unidad temporal. Si $f$ representa una magnitud sin unidad, la razón puede llevar las unidades inversas de la variable.

Una razón de cambio puede ser positiva, negativa o cero. Sin embargo, el signo de una sola secante no determina lo que sucederá al acercar los extremos: para conocer una tasa instantánea necesitamos un límite de todas las secantes suficientemente próximas y admisibles, no una muestra favorable.

## 1.4. La derivada en un punto interior

**Definición 1.2 (`EDC-C01-DEF-002`).** Sea $D\subseteq\mathbb R$, $f:D\to\mathbb R$ y $a\in D$ un **punto interior** de $D$: existe $r>0$ tal que $(a-r,a+r)\subseteq D$. Decimos que $f$ es **derivable en $a$** si existe un número real $L$ que satisface

$$
\lim_{h\to0}\frac{f(a+h)-f(a)}h=L.
$$

Escribimos $f'(a)=L$, y llamamos a ese número **derivada de $f$ en $a$**. La función $f$ será derivable en un intervalo abierto $I$ si lo es en cada $a\in I$.

La definición exige un límite **finito**, **bilateral** y **único**. Su traducción $\varepsilon$–$\delta$, usando la definición de límite de C00, es la siguiente:

$$
\begin{gathered}
\exists L\in\mathbb R\ \forall\varepsilon>0\ \exists\delta>0\ \forall h\in\mathbb R:\\
0<|h|<\delta
\quad\Longrightarrow\quad
\left|\frac{f(a+h)-f(a)}h-L\right|<\varepsilon,
\end{gathered}
$$

con $\delta\le r$ si es necesario. El orden de los cuantificadores impide escoger una pendiente distinta para cada tolerancia. Por la unicidad de límites probada en C00, **no puede haber dos números** que satisfagan esta condición.

**Teorema 1.1 (unicidad de la derivada; `EDC-C01-THM-001`).** Si $f$ es derivable en el punto interior $a$, su derivada $f'(a)$ está determinada de manera única.

**Demostración.** Si $L$ y $M$ satisfacen la definición, ambos son límites finitos de la misma función $h\mapsto Q_f(a,h)$ en $h=0$, que es un punto de acumulación de su dominio perforado. La unicidad del límite funcional de C00 obliga a $L=M$. $\square$

Al escribir $f'(a)$ no debe confundirse el número obtenido en $a$ con la **función derivada** $f'$ que eventualmente se obtiene cuando repetimos el procedimiento en distintos puntos. Es perfectamente posible que una función sea derivable sólo en una parte de su dominio.

::: {.callout-note appearance="simple" icon="false" collapse="false" title="Historia — Newton: seguir el movimiento de una curva"}

*Lectura opcional.*

Imaginemos un punto que recorre una curva. Mientras avanza hacia la derecha, su altura cambia: a veces crece con rapidez, a veces lentamente, a veces empieza a bajar. Podemos mirar el dibujo como una figura quieta, pero también como la huella de un movimiento.

Esta segunda mirada fue muy importante para Newton. Llamaba fluentes a las magnitudes que cambian y fluxiones a sus velocidades de cambio. Los nombres evocan justamente algo que fluye. Encontrar la inclinación de una curva y estudiar una velocidad quedaban así estrechamente relacionados.

La derivada que acabamos de definir recoge esa intuición: nos dice cómo está cambiando una magnitud en un instante. Cuando calculamos la pendiente de una tangente, también podemos pensar que estamos siguiendo un movimiento y preguntando qué está ocurriendo justo ahora.

**Para seguir leyendo:** [Newton, History of the Method of Fluxions, transcripción del Newton Project](https://newtonproject.ox.ac.uk/view/texts/normalized/NATP00356).

:::

## 1.5. Primeras derivadas obtenidas sin reglas memorizadas

### 1.5.1. Una parábola y una cúbica

**Proposición 1.1 (`EDC-C01-PRP-001`).** Para $f(x)=x^2$ sobre $\mathbb R$ se cumple $f'(a)=2a$; para $g(x)=x^3$ se cumple $g'(a)=3a^2$, para cada $a\in\mathbb R$.

**Demostración.** Para $f$ ya conocemos $Q_f(a,h)=2a+h\to2a$. Para $g$, el binomio finito proporciona

$$
\frac{(a+h)^3-a^3}h=3a^2+3ah+h^2,
\qquad h\ne0.
$$

El límite es $3a^2$. En ambos casos el cálculo se hizo únicamente para $h\ne0$ y el paso al límite utiliza operaciones sobre funciones polinómicas, justificadas en C00. $\square$

En el origen, la cúbica tiene derivada cero; su recta tangente es horizontal. Pero la curva pasa de valores negativos a positivos y **cruza** esa recta: un buen contraejemplo a una imagen geométrica demasiado estrecha.

### 1.5.2. Una función racional

**Proposición 1.2 (`EDC-C01-PRP-002`).** Si $f(x)=1/x$ con dominio $D=\mathbb R\setminus\{0\}$, entonces $f'(a)=-1/a^2$ para cada $a\ne0$.

**Demostración.** Elegimos $|h|<|a|/2$ para asegurar $a+h\ne0$. Entonces

$$
\frac{\dfrac1{a+h}-\dfrac1a}{h}
=-\frac{1}{a(a+h)}\longrightarrow-\frac1{a^2}.
$$

El último paso usa continuidad de cocientes racionales en puntos con denominador no nulo, demostrada en C00. No hemos usado una regla general de derivación de recíprocos: esa regla se obtendrá en C02. $\square$

### 1.5.3. La función valor absoluto

La función $f(x)=|x|$ es continua en todo $\mathbb R$, pero en el origen

$$
Q_f(0,h)=\frac{|h|}{h}
=\begin{cases}1,&h>0,\\-1,&h<0.\end{cases}
$$

No existe límite bilateral. Se trata de un obstáculo conceptual: una gráfica puede ser continua y, sin embargo, no admitir una pendiente local única. En §1.8 precisaremos los límites por cada lado.

## 1.6. Lo que significa aproximar por una recta

Las cuentas anteriores permiten proponer un criterio más informativo que «pendiente límite». Supongamos que una recta pasa por $(a,f(a))$ y tiene pendiente $m$. Su función afín es

$$
\ell_{a,m}(x)=f(a)+m(x-a).
$$

Lo relevante no es sólo que $f(a+h)-\ell_{a,m}(a+h)$ tienda a cero: eso sucede con **cualquier** pendiente $m$ cuando $f$ es continua en $a$. Exigiremos algo más fuerte: que el error sea pequeño **en comparación con $|h|$**.

**Teorema 1.2 (caracterización por aproximación lineal; `EDC-C01-THM-002`).** Sean $D\subseteq\mathbb R$, $a$ interior de $D$ y $f:D\to\mathbb R$. Las siguientes afirmaciones son equivalentes:

1. $f$ es derivable en $a$.
2. Existe $m\in\mathbb R$ y una función $\eta$ definida para incrementos $h$ suficientemente pequeños, con $\eta(0)=0$ y $\eta(h)\to0$ cuando $h\to0$, tales que

$$
f(a+h)=f(a)+mh+h\eta(h).
$$

En tal caso $m=f'(a)$, y este número es único.

**Demostración.** Si existe $f'(a)=m$, para $h\ne0$ pequeño definimos

$$
\eta(h)=\frac{f(a+h)-f(a)}h-m
$$

y ponemos $\eta(0)=0$. Por definición de derivada, $\eta(h)\to0$, y la identidad deseada resulta multiplicando por $h$. Recíprocamente, si se cumple la identidad, para $h\ne0$ obtenemos

$$
\frac{f(a+h)-f(a)}h=m+\eta(h)\longrightarrow m.
$$

Luego existe $f'(a)=m$, que es único por el Teorema 1.1. $\square$

También podemos expresar la condición mediante el **resto** $R_a(h)=f(a+h)-f(a)-f'(a)h$:

$$
\lim_{h\to0}\frac{R_a(h)}{|h|}=0.
$$

En efecto, $R_a(h)=h\eta(h)$ y $|R_a(h)|/|h|=|\eta(h)|\to0$. En esta obra escribiremos $R_a(h)=o(|h|)$ como abreviatura de la condición anterior. No significa que $R_a(h)$ sea literalmente cero, ni que el cociente se calcule en $h=0$.

**Definición 1.3 (recta tangente diferencial; `EDC-C01-DEF-003`).** Si $f$ es derivable en el punto interior $a$, la **recta tangente a la gráfica de $f$ en $(a,f(a))$** es

$$
y=f(a)+f'(a)(x-a).
$$

Es la única recta que pasa por el punto y cuyo error respecto de la función es $o(|x-a|)$ cuando $x\to a$. Esa unicidad es una consecuencia del Teorema 1.2, no una convención basada en contar intersecciones. Esta definición no pretende clasificar tangentes verticales: una pendiente vertical no es un número real finito y exige otro lenguaje geométrico.

**Ejemplo 1.1.** Para $f(x)=x^2$ la recta tangente en $a$ es $y=a^2+2a(x-a)$. La diferencia exacta es

$$
f(a+h)-[a^2+2ah]=h^2,
\qquad \frac{|h^2|}{|h|}=|h|\longrightarrow0.
$$

La recta candidata de §1.1 queda así justificada. En la cúbica, la tangente en el origen es $y=0$ y el error es $h^3=o(|h|)$, aunque la gráfica la atraviese.

## 1.7. Derivabilidad y continuidad: una implicación, no una equivalencia

**Teorema 1.3 (`EDC-C01-THM-003`).** Si $f:D\to\mathbb R$ es derivable en un punto interior $a$ de $D$, entonces $f$ es continua en $a$.

**Demostración.** Por el Teorema 1.2,

$$
f(a+h)-f(a)=h\bigl(f'(a)+\eta(h)\bigr),
$$

con $\eta(h)\to0$. El factor entre paréntesis converge al número finito $f'(a)$ y, por tanto, permanece acotado cerca de cero. Como $h\to0$, el producto converge a cero. Es decir, $f(a+h)\to f(a)$ cuando $h\to0$ en el dominio, que es continuidad en $a$ según C00. $\square$

La recíproca es falsa: $|x|$ es continua en cero pero no derivable allí. También es instructiva una función cuyo problema no sea una esquina visible. Definamos

$$
u(x)=\begin{cases}x\sin(1/x),&x\ne0,\\0,&x=0.\end{cases}
$$

Sabemos que $|u(x)|\le|x|$, pues $|\sin t|\le1$. Por encajonamiento, $u$ es continua en cero. En cambio, su cociente incremental allí es $\sin(1/h)$, sin límite cuando $h\to0$. Por ejemplo, para

$$
h_n=\frac{1}{\pi/2+2\pi n},\qquad
k_n=\frac{1}{3\pi/2+2\pi n}
$$

ambas sucesiones tienden a cero, pero $\sin(1/h_n)=1$ y $\sin(1/k_n)=-1$. Por el criterio secuencial de límite de C00, $u'(0)$ no existe.

Este contraejemplo no depende de disponer de una fórmula para la derivada de $\sin x$; sólo utiliza sus valores trigonométricos elementales y el criterio de límite. **La continuidad asegura proximidad de valores, pero no controla cómo se divide su diferencia por un incremento pequeño.**

## 1.8. Derivadas laterales y extremos de un dominio

Si $f$ está definida a ambos lados de $a$, el límite bilateral del cociente incremental requiere concordancia de ambos lados. Pero hay dominios, como $[0,\infty)$ para un tiempo contado desde el comienzo de un experimento, donde sólo tiene sentido aproximarse desde la derecha al punto extremo.

**Definición 1.4 (derivadas laterales; `EDC-C01-DEF-004`).** Sea $f:D\to\mathbb R$ y $a\in D$. Si para algún $r>0$ tenemos $[a,a+r)\subseteq D$, definimos, cuando exista finitamente,

$$
f'_+(a)=\lim_{h\to0^+}\frac{f(a+h)-f(a)}h.
$$

Si $(a-r,a]\subseteq D$, definimos, cuando exista finitamente,

$$
f'_-(a)=\lim_{h\to0^-}\frac{f(a+h)-f(a)}h.
$$

**Teorema 1.4 (unión de los dos lados; `EDC-C01-THM-004`).** Si $a$ es interior al dominio $D$, entonces $f'(a)$ existe si y sólo si existen $f'_+(a)$ y $f'_-(a)$ como números reales y son iguales. En ese caso los tres valores coinciden.

**Demostración.** Si existe el límite bilateral, sus restricciones derecha e izquierda tienen el mismo valor por la definición $\varepsilon$–$\delta$. Recíprocamente, supongamos que los dos límites laterales valen $L$. Dado $\varepsilon>0$, obtenemos $\delta_+>0$ y $\delta_->0$ que controlan los cocientes desde el lado correspondiente. Para $0<|h|<\min(\delta_+,\delta_-,r)$, $h$ pertenece a uno de los dos lados y $|Q_f(a,h)-L|<\varepsilon$. Ésta es la definición del límite bilateral. $\square$

**Ejemplo 1.2.** Para $f(x)=|x|$, las derivadas laterales en cero son $f'_-(0)=-1$ y $f'_+(0)=1$; no hay derivada bilateral. Para $f:[0,\infty)\to\mathbb R$, $f(x)=x^2$, existe $f'_+(0)=0$, pero la **definición interior** no atribuye derivada bilateral a ese extremo, pues no hay valores del dominio para $h<0$. La expresión «derivable en el extremo» sólo es aceptable cuando se declare explícitamente la convención unilateral.

La existencia de una derivada **infinita** es una manera informal de describir ciertos cocientes no acotados, pero no es una derivada real en el sentido de la Definición 1.2. Por ejemplo, para $f(x)=\sqrt{x}$ en $[0,\infty)$, el cociente por la derecha en cero es $1/\sqrt h$; a lo largo de $h=1/n^2$ toma el valor $n$ y no converge a un número finito. En este volumen las derivadas laterales, cuando se declaran existentes, también son finitas.

## 1.9. Cuando una función está definida por tramos

Los puntos donde cambia una fórmula obligan a separar dos preguntas: ¿la función es continua allí?, y ¿sus razones de cambio laterales se aproximan a una misma pendiente? La primera es necesaria, pero no suficiente, para la segunda.

**Ejemplo 1.3.** Sean $p,q,r,s\in\mathbb R$ y

$$
f(x)=\begin{cases}px+q,&x<0,\\rx+s,&x\ge0.\end{cases}
$$

Como $f(0)=s$, el límite izquierdo de $f(x)$ en cero es $q$ y el derecho es $s$. Por tanto, $f$ es continua en cero exactamente cuando $q=s$. Si se cumple esa igualdad,

$$
\frac{f(h)-f(0)}h=
\begin{cases}p,&h<0,\\r,&h>0.\end{cases}
$$

Luego $f$ es derivable en cero si y sólo si $q=s$ y $p=r$; en tal caso $f'(0)=p=r$. Si $q\ne s$, el cociente desde la izquierda incluye $(q-s)/h$, lo que impide una derivada finita allí. Esta cuenta muestra por qué no conviene «comparar pendientes» antes de verificar la continuidad del empalme.

**Ejemplo 1.4.** Sea $v(x)=x|x|$ para $x\in\mathbb R$. Entonces

$$
\frac{v(h)-v(0)}h=|h|\longrightarrow0,
$$

así que $v'(0)=0$, pese a que su expresión cambia de forma entre $h<0$ y $h>0$. Un cambio de fórmula no implica necesariamente una esquina.

## 1.10. Qué dicen —y qué no dicen— los cocientes locales

La existencia de $f'(a)$ es **una propiedad en un punto**. No afirma que la derivada exista en todo un intervalo, ni que una fórmula de derivación pueda aplicarse globalmente. En particular, de $f'(a)=0$ no se deduce que haya un máximo o un mínimo: para $f(x)=x^3$, $f'(0)=0$, pero $f(x)<f(0)$ si $x<0$ y $f(x)>f(0)$ si $x>0$. El principio de Fermat y los criterios de extremos serán objeto de C03, con hipótesis precisas.

Hay incluso funciones derivables en un punto cuya gráfica presenta oscilaciones a cualquier escala. Definamos

$$
w(x)=\begin{cases}x^2\sin(1/x),&x\ne0,\\0,&x=0.\end{cases}
$$

En cero,

$$
\frac{w(h)-w(0)}h=h\sin(1/h),
\qquad \left|h\sin(1/h)\right|\le|h|.
$$

Por encajonamiento, $w'(0)=0$. El ejemplo contrasta con $u(x)=x\sin(1/x)$ del §1.7, que era continua pero no derivable en cero. Un factor adicional $x$ cambia el orden del error lo suficiente como para recuperar la aproximación lineal.

Existe una consecuencia positiva inmediata del signo de una derivada.

**Proposición 1.3 (comparación estrictamente local; `EDC-C01-PRP-003`).** Si $f$ es derivable en un punto interior $a$ y $f'(a)>0$, existe $\delta>0$ tal que, cuando $0<|h|<\delta$, se cumple

$$
h>0\Longrightarrow f(a+h)>f(a),
\qquad
h<0\Longrightarrow f(a+h)<f(a).
$$

Si $f'(a)<0$, las dos desigualdades se invierten.

**Demostración.** Si $L=f'(a)>0$, aplicamos la definición de derivada con tolerancia $\varepsilon=L/2$. Para $0<|h|<\delta$ se obtiene $Q_f(a,h)>L/2>0$. Como $f(a+h)-f(a)=hQ_f(a,h)$, la señal de la diferencia coincide con la de $h$. Si $L<0$, el cociente es negativo suficientemente cerca de cero, usando $\varepsilon=|L|/2$, y se invierten los signos. $\square$

La proposición compara $f(a)$ con valores cercanos, pero no demuestra que **todos los pares** de puntos próximos conserven un orden. Por eso no sustituye al teorema del valor medio ni a un criterio de monotonía. Confundir esas conclusiones sería cambiar un cuantificador: «cada punto con $a$» no es «cada par de puntos». En C03 estudiaremos la diferencia.

## 1.11. Cinco momentos de una historia no lineal

Los problemas que ahora unificamos en la noción de derivada tuvieron recorridos históricos variados. Fermat investigó en el siglo XVII problemas de extremos y tangentes mediante procedimientos algebraicos que hoy se comparan con técnicas diferenciales; **no debe atribuirse a esos procedimientos la definición $\varepsilon$–$\delta$ que acabamos de dar** [H2]. Galileo estudió las relaciones geométricas entre distancia, tiempo y aceleración, incluida la ley cuadrática del tiempo para la caída uniformemente acelerada [H1]. Barrow desarrolló procedimientos geométricos para tangentes y cuadraturas y reconoció relaciones entre esos problemas [H3].

Newton trabajó con cantidades variables y sus *fluxiones*; Leibniz articuló el cálculo diferencial mediante otros conceptos y una notación de enorme influencia. La historia de sus contribuciones y de su disputa de prioridad no puede reducirse limpiamente a una sola fecha de invención. Para el problema de este capítulo importa reconocer que esas tradiciones acercaron preguntas de geometría y movimiento, aunque no las formularon del modo moderno utilizado en nuestras demostraciones [H4–H5].

Las [notas históricas de C01](capitulo-01-notas.html) identifican las obras de contraste, sus localizadores textuales y sus límites documentales. El álgebra de $x^2$ o $x^3$ que hemos realizado **es una reconstrucción matemática nuestra**, no una transcripción ficticia de una demostración histórica.

## 1.12. Síntesis: qué hemos demostrado y qué falta

La noción de derivada reúne dos preguntas bajo una sola condición matemática:

$$
\boxed{\quad f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h\quad}
$$

cuando $a$ es interior al dominio y ese límite es real y finito. Si existe, determina una única mejor aproximación afín de primer orden y garantiza continuidad; si no existe, la función puede seguir siendo continua, pero la pendiente local única no está justificada. En un extremo del dominio debe declararse el lado desde el cual se aproxima. Para movimientos, la misma operación produce una velocidad instantánea **con signo** y con unidades propias.

Hemos demostrado con los resultados de C00, y sin utilizar reglas futuras, la unicidad de la derivada, los casos concretos de $x^2$, $x^3$ y $1/x$, la equivalencia con una aproximación lineal de error $o(|h|)$, la implicación derivabilidad $\Rightarrow$ continuidad, la combinación de derivadas laterales y una comparación estrictamente local cuando el signo de $f'(a)$ es conocido. Los contraejemplos han mostrado los límites de cada afirmación.

**Próximos capítulos.** En C02 obtendremos reglas generales para derivar sumas, productos, cocientes, composiciones, funciones inversas y funciones elementales. En C03 usaremos Rolle y el valor medio para convertir información sobre derivadas en conclusiones sobre toda una región. La trayectoria de la acumulación comenzará en C04; sólo tras la construcción de la integral en C05 se probará su vínculo con la derivada en C06.

### Mapa de dependencias

- **De C00:** orden y completitud de $\mathbb R$; límites funcionales y secuenciales, continuidad y operaciones con límites; valor absoluto, polinomios y funciones racionales; uso elemental de desigualdades y del principio de encajonamiento. Las desigualdades $|\sin t|\le1$ y los valores de seno en ángulos elementales pertenecen a la trigonometría escolar de entrada, no a un teorema de derivación.
- **Del propio C01:** `EDC-C01-DEF-001--004`, `EDC-C01-THM-001--004`, `EDC-C01-PRP-001--003` y sus pruebas. Ningún resultado de Rolle, valor medio, integral o Taylor interviene.
- **Hacia C02–C03:** derivada en punto interior, derivadas laterales, tangente como aproximación lineal, derivabilidad implica continuidad y contraejemplos de hipótesis.

### Trabajo del lector

Los [ejercicios del capítulo 1](capitulo-01-ejercicios.html) proponen cálculos por definición, diagnósticos de dominio y derivadas laterales, contraejemplos y argumentos breves de demostración. Las [soluciones desarrolladas](capitulo-01-soluciones.html) se presentan aparte, con correspondencia exacta de identificadores. Se conservan también las [notas históricas](capitulo-01-notas.html), separadas del discurso demostrativo.

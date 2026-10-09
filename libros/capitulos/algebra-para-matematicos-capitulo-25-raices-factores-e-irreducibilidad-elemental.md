---
{
  "title": "Raíces, factores e irreducibilidad elemental",
  "description": "Capítulo 25 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0200",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C25",
  "editorial-id": "MA-BCH-APM-01-021",
  "status": "published",
  "date-created": "2026-10-09",
  "date-modified": "2026-10-09",
  "areas": [
    "algebra",
    "fundamentos"
  ],
  "level": "fundamental",
  "topics": [
    "numeros-complejos-y-el-horizonte-de-las-ecuaciones"
  ],
  "prerequisites": [
    "MA-BCH-0199"
  ],
  "related": [
    "MA-BOK-0006"
  ],
  "provenance": {
    "type": "original",
    "sources": []
  },
  "license": "GFDL-1.3-or-later"
}
---

Una evaluación puede dar información sobre todo un polinomio. Por ejemplo, de $P(2)=0$ podremos deducir que $x-2$ divide a $P$. Esa conexión convierte una búsqueda de números en una búsqueda de factores. Para utilizarla con precisión necesitamos especificar dónde buscamos las raíces, justificar la extracción de factores y controlar cuánto puede certificar el grado.

En estas primeras secciones trabajaremos con coeficientes racionales o reales. La división, el grado del producto y la evaluación se recuperan de C24. Cada vez que una conclusión dependa del conjunto de coeficientes, lo indicaremos.

## 25.1. Raíces y conjunto de coeficientes {#apm-c25-s01}

Sea $K=\mathbb Q$ o $K=\mathbb R$, y sea $P\in K[x]$. Un número $a\in K$ es una **raíz de $P$ en $K$** si $P(a)=0$. La condición es una igualdad comprobable: sustituimos $x$ por $a$ y operamos en $K$. Un candidato solo se convierte en raíz cuando esa igualdad queda justificada.

Consideremos $P(x)=x^2-3x+2$. Las evaluaciones $P(1)=1-3+2=0$ y $P(2)=4-6+2=0$ certifican dos raíces. En cambio, $P(3)=9-9+2=2$ descarta el candidato $3$. Como los coeficientes y los tres números son racionales, estas comprobaciones son válidas tanto en $\mathbb Q$ como en $\mathbb R$.

### El conjunto de búsqueda forma parte del problema

El polinomio $R(x)=x^2-2$ tiene coeficientes racionales. Su evaluación en un número real también está definida: interpretamos esos coeficientes como reales y efectuamos las mismas operaciones. En $\mathbb R$ sus raíces son $\sqrt2$ y $-\sqrt2$, porque $a^2=2$ equivale a $a=\pm\sqrt2$.

En $\mathbb Q$ no tiene raíces. Recordemos la justificación aritmética: si un racional en forma reducida $p/q$, con $p,q\in\mathbb Z$ y $q>0$, satisficiera $(p/q)^2=2$, tendríamos $p^2=2q^2$. Entonces $p$ sería par; al escribir $p=2r$, resultaría $q^2=2r^2$, de modo que $q$ también sería par. Esto contradice que la fracción esté reducida.

La expresión $x^2-2$ sigue siendo la misma; cambia el conjunto en el que permitimos buscar $a$. También cambiará el conjunto de coeficientes permitido para los factores: $x-\sqrt2$ pertenece a $\mathbb R[x]$, pero no a $\mathbb Q[x]$. Por eso una afirmación como «el polinomio no tiene raíces» necesita indicar el conjunto de búsqueda.

### Cero y constantes

El polinomio cero se anula en cada número del conjunto elegido. Por tanto, todos los racionales son raíces del polinomio cero en $\mathbb Q$, y todos los reales lo son en $\mathbb R$.

Un polinomio constante no nulo, $P(x)=c$ con $c\ne0$, no tiene raíces: su evaluación siempre es $c$. El contraste será decisivo al relacionar raíces y grado. El polinomio cero no recibe un grado natural y quedará excluido de la cota que probaremos.

**Recuperación resuelta.** Un estudiante dice: «$x^2-2$ no tiene raíces porque no encontré una fracción que lo anule». ¿Qué puede concluir y cómo debe justificarlo?

La búsqueda de unas cuantas fracciones solo descarta esas candidatas. La conclusión universal requiere la demostración de irracionalidad anterior. Con ella sí podemos afirmar que no hay raíces racionales. Las evaluaciones en $\pm\sqrt2$ muestran, además, que sí hay raíces reales. La respuesta completa distingue los dos conjuntos y aporta un argumento para cada uno.

**Comprobación resuelta.** Para $P(x)=0$, $Q(x)=5$ y $R(x)=x-5$, ¿es $5$ una raíz?

Sí para $P$, pues $P(5)=0$; no para $Q$, pues $Q(5)=5$; sí para $R$, pues $R(5)=5-5=0$. Los tres casos impiden confundir «constante» con «sin raíces»: la constante cero es la excepción.

## 25.2. Teorema del factor {#apm-c25-s02}

La división por $x-a$ establece el vínculo entre raíz y factor. Como su divisor tiene grado uno, el resto es constante. Por la división y el teorema del resto de §[§24.7](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s07)–24.11, para $a\in K$ existe un único cociente $Q\in K[x]$ tal que

$$
P(x)=(x-a)Q(x)+P(a).
$$

**Teorema del factor.** Para $P\in K[x]$ y $a\in K$, las siguientes afirmaciones son equivalentes:

1. $P(a)=0$.
2. $x-a$ divide a $P$ en $K[x]$.

**Demostración.** Si $P(a)=0$, la identidad de división se reduce a $P=(x-a)Q$, que es exactamente la divisibilidad afirmada. Recíprocamente, si $P=(x-a)Q$, evaluamos en $a$ y obtenemos $P(a)=(a-a)Q(a)=0$. Ambas direcciones usan identidades; no dependen de aproximaciones numéricas. $\square$

El teorema también vale para $P=0$: podemos tomar $Q=0$. Si $P\ne0$ y $a$ es una raíz, entonces $P$ no es constante. Además, $Q\ne0$ y la regla del grado del producto de [§24.4](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s04) da $\deg Q=\deg P-1$.

### Extraer el factor y comprobarlo

Sea $P(x)=2x^3-3x^2-8x+12$. La evaluación en $2$ da $16-12-16+12=0$. El teorema asegura que $x-2$ es factor; todavía debemos calcular el cociente si queremos usar la factorización.

Horner con $a=2$ transforma los coeficientes $2,-3,-8,12$ del siguiente modo: bajamos $2$; obtenemos $-3+2\cdot2=1$; después $-8+2\cdot1=-6$; finalmente $12+2(-6)=0$. El cociente es $2x^2+x-6$, y el último número es el resto. Así,

$$
2x^3-3x^2-8x+12=(x-2)(2x^2+x-6).
$$

La multiplicación comprueba el certificado: $2x^3+x^2-6x-4x^2-2x+12=2x^3-3x^2-8x+12$. Comprobar únicamente el resto confirma que $2$ es raíz; reconstruir el producto confirma también el cociente calculado.

### Una identidad que permite ver todos los factores lineales

Para cualquier entero $n\ge1$ y cualquier $a\in K$,

$$
x^n-a^n=(x-a)(x^{n-1}+ax^{n-2}+\cdots+a^{n-2}x+a^{n-1}).
$$

Al distribuir el producto, los términos intermedios se cancelan por parejas, y quedan $x^n-a^n$. Para $n=1$, la suma entre paréntesis consta del único término $1$. Si $P(x)=\sum_{j=0}^n c_jx^j$, aplicamos esta identidad a cada término de $P(x)-P(a)$; el término constante se cancela. Obtenemos que $x-a$ divide siempre a $P(x)-P(a)$. Cuando $P(a)=0$, esto vuelve a demostrar el teorema del factor y ofrece una construcción del cociente.

**Recuperación resuelta.** Dividimos $S(x)=x^2+x+1$ por $x-1$. ¿Qué información contiene el resto?

La identidad es $S=(x-1)(x+2)+3$. El resto $3$ coincide con $S(1)$, de modo que $1$ no es raíz y $x-1$ no divide a $S$. El cociente existe aunque el candidato falle; lo que decide la divisibilidad es el resto cero.

**Diagnóstico resuelto.** «Como $x^2-2$ tiene raíz $\sqrt2$, se factoriza en $\mathbb Q[x]$ como $(x-\sqrt2)(x+\sqrt2)$». ¿Dónde está el error?

La igualdad del producto es correcta, pero ambos factores tienen coeficientes irracionales. Es una factorización en $\mathbb R[x]$. Para invocar el teorema del factor dentro de $\mathbb Q[x]$, necesitaríamos una raíz $a\in\mathbb Q$, y [§25.1](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s01) demuestra que no existe. El conjunto elegido en la hipótesis determina dónde pertenece el cociente.

## 25.3. Raíces distintas y factores simultáneos {#apm-c25-s03}

Si conocemos varias raíces, queremos extraer todos sus factores lineales. Debemos justificar que, al extraer uno, las otras raíces permanecen en el cociente.

**Proposición.** Si $a_1,\ldots,a_r$ son raíces distintas de $P\in K[x]$, con $r\ge1$, entonces existe $Q\in K[x]$ tal que

$$
P(x)=(x-a_1)(x-a_2)\cdots(x-a_r)Q(x).
$$

**Demostración por inducción sobre $r$.** Para $r=1$, es el teorema del factor. Supongamos probado el resultado para $r-1$ y consideremos $r$ raíces distintas. Por la hipótesis inductiva,

$$
P(x)=(x-a_1)\cdots(x-a_{r-1})R(x).
$$

Evaluamos en $a_r$. Como $P(a_r)=0$, obtenemos $(a_r-a_1)\cdots(a_r-a_{r-1})R(a_r)=0$. Cada diferencia es no nula porque las raíces son distintas. En $\mathbb Q$ y en $\mathbb R$, un producto de números no nulos es no nulo; por tanto, $R(a_r)=0$. El teorema del factor aplicado a $R$ da $R=(x-a_r)Q$. Sustituyendo, resulta la identidad buscada. $\square$

La proposición incluye al polinomio cero, para el que $Q=0$. Si $P\ne0$, necesariamente $Q\ne0$; entonces los grados dan $\deg P=r+\deg Q$. No hemos supuesto que la lista contenga todas las raíces: cualquier lista finita de raíces distintas proporciona su propio divisor.

### Extraer sin perder las otras raíces

Para $P(x)=x^3-2x^2-x+2$, comprobamos $P(1)=0$, $P(-1)=0$ y $P(2)=0$. Una primera extracción da $P=(x-1)(x^2-x-2)$. La raíz $-1$ queda en el cociente porque $0=P(-1)=(-2)(1+1-2)$ y el primer factor es no nulo. El cociente se factoriza como $(x+1)(x-2)$, de modo que $P(x)=(x-1)(x+1)(x-2).$

Desarrollar $(x^2-1)(x-2)$ devuelve $x^3-2x^2-x+2$. Esta identidad permite certificar también que las únicas raíces en $\mathbb Q$ o en $\mathbb R$ son $1,-1,2$: si un producto de estos tres factores vale cero, al menos uno debe valer cero.

### Por qué no podemos repetir un nombre de raíz

La lista $1,1$ no cumple la hipótesis de raíces distintas. El polinomio $P(x)=x-1$ se anula en $1$, pero $(x-1)^2$ no lo divide: un producto no nulo que contenga ese factor tendría grado al menos dos, mientras que $P$ tiene grado uno.

La prueba anterior muestra exactamente qué falla. Tras extraer $x-1$, el cociente es $1$. Evaluar $P$ en $1$ produce $0=0\cdot1$, una igualdad que no obliga al cociente a anularse. Repetir el mismo dato $P(1)=0$ no añade un nuevo factor. La extracción repetida requerirá comprobar de nuevo la anulación del cociente.

**Recuperación resuelta.** Sabemos que $P(3)=P(5)=0$. Después de escribir $P=(x-3)R$, ¿por qué podemos extraer $x-5$ de $R$?

Evaluamos en $5$: $0=P(5)=(5-3)R(5)=2R(5)$. Como $2\ne0$, se sigue que $R(5)=0$. El teorema del factor da $R=(x-5)Q$. El paso crucial es la diferencia no nula entre las raíces.

**Diagnóstico resuelto.** «Si dos polinomios dividen a $P$, su producto divide a $P$». ¿Basta esta regla para la proposición?

La regla, sin hipótesis adicionales, es falsa. Por ejemplo, $x-1$ divide a $P=x-1$; tomarlo como ambos divisores no hace que $(x-1)^2$ divida a $P$. Nuestra demostración evita esa regla: muestra directamente, mediante evaluación y diferencias no nulas, que cada factor siguiente divide al cociente anterior.

## 25.4. Cota del número de raíces {#apm-c25-s04}

**Teorema.** Un polinomio no nulo $P\in K[x]$ de grado $n$ tiene a lo sumo $n$ raíces distintas en $K$.

**Demostración por inducción sobre el grado.** Si $n=0$, $P$ es una constante no nula y no tiene raíces. Supongamos válida la afirmación para los polinomios no nulos de grado $n-1$, con $n\ge1$, y consideremos un polinomio de grado $n$.

Si $P$ no tiene raíces, la cota se cumple. Si tiene una raíz $a$, el teorema del factor da $P=(x-a)Q$, donde $Q\ne0$ y $\deg Q=n-1$. Toda raíz $b$ de $P$ distinta de $a$ satisface $0=(b-a)Q(b)$; como $b-a\ne0$, es raíz de $Q$. Por la hipótesis inductiva, $Q$ tiene a lo sumo $n-1$ raíces distintas. Por tanto, las raíces de $P$ están contenidas en el conjunto formado por $a$ y esas, a lo sumo, $n-1$ raíces de $Q$. Hay a lo sumo $n$ en total. $\square$

La prueba establece también que el conjunto de raíces es finito. No comienza enumerando todas las raíces y suponiendo, sin justificación, que existe una lista finita de ellas.

La proposición de [§25.3](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s03) ofrece otro certificado de la misma cota: si hubiera más de $n$ raíces distintas, podríamos seleccionar $n+1$ de ellas. Su producto de factores lineales dividiría a $P$, de modo que $P=(x-a_1)\cdots(x-a_{n+1})Q$ con $Q\ne0$. La regla del grado daría $n=n+1+\deg Q\ge n+1$, una contradicción. Seleccionar una cantidad finita de raíces no presupone que el conjunto completo sea finito.

### La cota no afirma que existan tantas raíces

El polinomio $x^2+1$ no tiene raíces reales: para cada real $a$, $a^2+1\ge1>0$. Su grado es dos. El polinomio $(x-1)^3$ tiene grado tres, pero una sola raíz distinta, $1$, pues una potencia se anula exactamente cuando su base se anula. En cambio, $x^3-x=x(x-1)(x+1)$ tiene tres raíces distintas: $0,1,-1$.

La cota cuenta números distintos. Tres apariciones del factor $x-1$ no representan tres números diferentes. Por otra parte, el polinomio cero tiene infinitas raíces en ambos conjuntos y está excluido del teorema: no podemos asignarle un grado natural para aplicar esta conclusión.

### Reconstruir a partir de un grado y de raíces

Sea $P\in\mathbb R[x]$ de grado cuatro, con coeficiente principal $3$, y supongamos que $-2,-1,1,2$ son raíces. Por [§25.3](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s03), el producto de los cuatro factores lineales divide a $P$. El cociente es no nulo y tiene grado cero; por tanto, es una constante. Como el producto de los factores es mónico, esa constante debe ser $3$. Así,

$$
P(x)=3(x+2)(x+1)(x-1)(x-2)=3x^4-15x^2+12.
$$

Para desarrollar, agrupamos $(x+2)(x-2)=x^2-4$ y $(x+1)(x-1)=x^2-1$, cuyo producto es $x^4-5x^2+4$. Las cuatro raíces ya encontradas agotan la cota; ninguna otra raíz real puede añadirse.

**Recuperación resuelta.** Un polinomio de grado tres se anula en cuatro reales distintos. ¿Qué conclusión corresponde?

Las dos afirmaciones son incompatibles: «de grado tres» implica que el polinomio es no nulo, y la cota permite a lo sumo tres raíces distintas. Si solo supiéramos que su grado es a lo sumo tres, admitiendo además al polinomio cero como posibilidad, las cuatro anulaciones obligarían a que fuese el polinomio cero.

**Diagnóstico resuelto.** Una supuesta prueba empieza: «Sean $a_1,\ldots,a_k$ todas las raíces de $P$; entonces su producto de factores divide a $P$ y $k\le n$». ¿Qué paso necesita reparación?

La escritura de todas las raíces como una lista finita presupone la finitud que se intenta demostrar. Podemos repararla con la inducción sobre el grado desarrollada arriba. También podemos suponer que existen más de $n$ raíces, elegir solo $n+1$ distintas y obtener la contradicción de grados. Ambas reparaciones evitan usar como premisa la propia conclusión.



### Contar valores y contar factores

La cota por grado distingue raíces diferentes de sus multiplicidades. En $P=(x-a)^3(x-b)^2$, con $a\ne b$, hay dos raíces distintas y la suma de multiplicidades es cinco. Para certificar la multiplicidad exacta en $a$, retiramos $(x-a)^3$: el residual vale $(a-b)^2\ne0$. En $b$, retiramos $(x-b)^2$ y el residual vale $(b-a)^3\ne0$. **Control resuelto:** si $a=b$, el producto se convierte en $(x-a)^5$. Ya no tiene dos raíces ni multiplicidades tres y dos separadas: hay una raíz de multiplicidad cinco. Una construcción por factores certifica existencia, pero la exactitud exige revisar que el residual no vuelva a anularse. La coincidencia de parámetros debe comprobarse antes de contar.

## 25.5. Identidades y datos de evaluación {#apm-c25-s05}

Dos expresiones polinómicas pueden parecer diferentes y, sin embargo, tener los mismos coeficientes al desarrollarlas. La cota de raíces proporciona otra manera de justificar su igualdad: comparar sus valores en suficientes puntos. El número de puntos necesario depende de un control previo del grado.

Diremos que un polinomio tiene **grado a lo sumo $n$**, con $n\ge0$, si es el polinomio cero o si es no nulo y su grado es menor o igual que $n$. Esta convención incluye al cero sin asignarle un grado natural.

**Proposición de identificación.** Sean $P,Q\in K[x]$ de grado a lo sumo $n$. Si coinciden en $n+1$ puntos distintos de $K$, entonces $P=Q$ como polinomios.

**Demostración.** Sea $D=P-Q$. Si $D\ne0$, su grado es a lo sumo $n$, porque la resta no puede crear términos de grado mayor. Cada punto de coincidencia es raíz de $D$, de modo que tendría $n+1$ raíces distintas. Esto contradice [§25.4](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s04). Por tanto, $D=0$ y $P=Q$. $\square$

Por ejemplo, $P(x)=(x+1)(x^2-x+1)$ y $Q(x)=x^3+1$ tienen grado a lo sumo tres. Sus valores en $-1,0,1,2$ son, respectivamente, $0,1,2,9$ para ambas expresiones. Esas cuatro coincidencias prueban la identidad. Aquí también es breve desarrollar el producto; la identificación por puntos será útil cuando las expresiones tengan formas distintas y evaluar resulte más sencillo que comparar todos sus coeficientes.

### Construir el polinomio que toma unos valores dados

Sean $a_0,\ldots,a_n$ puntos distintos de $K$, y sean $b_0,\ldots,b_n\in K$ los valores que queremos imponer. Buscamos un polinomio de grado a lo sumo $n$ que satisfaga $P(a_i)=b_i$ para cada $i$.

La construcción separa los datos. Para cada índice $i$, queremos un polinomio que valga $1$ en $a_i$ y $0$ en todos los demás puntos. Los factores $x-a_j$, con $j\ne i$, producen los ceros deseados; dividimos por su valor en $a_i$ para normalizar. Definimos

$$
L_i(x)=\prod_{\substack{0\le j\le n\\j\ne i}}\frac{x-a_j}{a_i-a_j},
\qquad
P(x)=\sum_{i=0}^{n}b_iL_i(x).
$$

Todos los denominadores son constantes no nulas, pues los puntos son distintos. Por tanto, $L_i\in K[x]$ y tiene grado $n$. Para $n=0$, el producto sin factores se interpreta como $1$, y la construcción da el polinomio constante $b_0$.

En $a_i$, cada fracción del producto vale $1$, así que $L_i(a_i)=1$. En $a_k$ con $k\ne i$, aparece el factor $a_k-a_k=0$, así que $L_i(a_k)=0$. Al evaluar la suma en $a_k$, todos los términos desaparecen salvo $b_kL_k(a_k)=b_k$. Esto prueba la existencia del polinomio buscado, de grado a lo sumo $n$. Si hubiera otro con las mismas condiciones y la misma cota de grado, la proposición de identificación los haría iguales. La construcción y la unicidad constituyen la **interpolación polinómica elemental** en esos puntos.

Tomemos los datos $P(-1)=2$, $P(0)=1$, $P(2)=5$ y grado a lo sumo dos. Los tres polinomios de la construcción son $L_{-1}=x(x-2)/3$, $L_0=-(x+1)(x-2)/2$ y $L_2=x(x+1)/6$. Los subíndices nombran aquí los puntos correspondientes. Entonces

$$
P(x)=\frac{2x(x-2)}3-\frac{(x+1)(x-2)}2+\frac{5x(x+1)}6=x^2+1.
$$

El coeficiente de $x^2$ es $2/3-1/2+5/6=1$; el de $x$ es $-4/3+1/2+5/6=0$; el término constante es $1$. Evaluar $x^2+1$ en los tres puntos devuelve $2,1,5$, y la identificación asegura que ningún otro polinomio de grado a lo sumo dos satisface esos datos.

**Recuperación resuelta.** ¿Siguen siendo únicos esos datos si permitimos grado tres?

No. Para cualquier $t\in K$, el polinomio $P_t(x)=x^2+1+t\,x(x+1)(x-2)$ toma los mismos tres valores, porque el término añadido se anula en cada punto. Si $t\ne0$, su grado es tres y difiere de $P_0=x^2+1$. Los tres datos identifican un polinomio dentro de la clase de grado a lo sumo dos; no lo identifican entre todos los polinomios.

**Diagnóstico resuelto.** Se intenta interpolar con $P(1)=2$ y $P(1)=3$. ¿Cómo se repara el planteamiento?

Esos datos son incompatibles: una evaluación en un mismo número tiene un único valor. Si los dos valores fueran $2$, el segundo dato repetiría el primero y no aportaría otro punto distinto. La construcción debe partir de puntos distintos y de un valor por punto; repetir un punto tampoco aumenta el número de coincidencias que permite aplicar la cota de raíces.

## 25.6. Multiplicidad mediante divisiones sucesivas {#apm-c25-s06}

Saber que $P(a)=0$ permite extraer una vez $x-a$. Para extraerlo otra vez necesitamos que el cociente también se anule en $a$. La multiplicidad registra cuántas extracciones consecutivas son posibles.

Sea $P\in K[x]$ no nulo y sea $a\in K$. Definimos la **multiplicidad de $a$ en $P$**, denotada por $\nu_a(P)$, como el mayor entero $m\ge0$ para el que $(x-a)^m$ divide a $P$. El valor $m=0$ siempre está permitido, pues $(x-a)^0=1$ divide a cualquier polinomio. Si $\deg P=n$ y $(x-a)^m$ divide a $P$, el cociente es no nulo y la regla del grado exige $m\le n$. El conjunto de valores posibles es, por tanto, un subconjunto no vacío de $\{0,\ldots,n\}$ y tiene máximo. Esto justifica que la definición existe.

Por el teorema del factor, $a$ es raíz si y solo si $\nu_a(P)\ge1$. Una raíz de multiplicidad uno se llama **simple**; una de multiplicidad dos, **doble**. Para un número que no es raíz, la multiplicidad es cero.

### El residual certifica dónde termina la extracción

**Proposición.** Para $P\ne0$, $a\in K$ y $m\ge0$, se tiene $\nu_a(P)=m$ si y solo si existe $Q\in K[x]$ tal que

$$
P(x)=(x-a)^mQ(x),\qquad Q(a)\ne0.
$$

**Demostración.** Si $m=\nu_a(P)$, la divisibilidad de la definición proporciona $Q$. Si $Q(a)=0$, el teorema del factor daría $Q=(x-a)R$; entonces $(x-a)^{m+1}$ dividiría a $P$, contradiciendo la maximalidad de $m$. Luego $Q(a)\ne0$.

Recíprocamente, supongamos la identidad con $Q(a)\ne0$. Ya sabemos que $(x-a)^m$ divide a $P$. Si también lo dividiera $(x-a)^{m+1}$, tendríamos $P=(x-a)^{m+1}R$. Al comparar ambas expresiones, $(x-a)^m[Q-(x-a)R]=0$. Como el primer factor no es cero y el producto de dos polinomios no nulos no puede ser cero ([§24.4](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s04)), se sigue que $Q=(x-a)R$. Evaluar en $a$ contradice $Q(a)\ne0$. Ninguna potencia superior puede dividir a $P$, pues implicaría también la divisibilidad por la potencia $m+1$. Así, $\nu_a(P)=m$. $\square$

Una vez fijado $m$, el cociente $Q$ es único: si dos cocientes dieran la misma identidad, su diferencia multiplicada por $(x-a)^m$ sería cero y la misma cancelación los haría iguales.

Para calcular $m$, dividimos sucesivamente por $x-a$ mientras el resto sea cero. Cada extracción reduce el grado en uno, y un cociente constante no nulo ya no puede anularse en $a$. El proceso termina, a más tardar, después de $\deg P$ extracciones. El primer resto no nulo es el valor en $a$ del residual final.

### Un cálculo completo

Sea $P(x)=x^3-3x+2$ y busquemos la multiplicidad de $1$. Las divisiones sucesivas son:

| Polinomio dividido | Cociente al dividir por $x-1$ | Resto |
|---|---|---:|
| $x^3-3x+2$ | $x^2+x-2$ | $0$ |
| $x^2+x-2$ | $x+2$ | $0$ |
| $x+2$ | $1$ | $3$ |

Las identidades que justifican las dos primeras filas son $P=(x-1)(x^2+x-2)$ y $x^2+x-2=(x-1)(x+2)$. En la tercera, $x+2=(x-1)\cdot1+3$. Hemos extraído dos factores, y el residual $x+2$ vale $3\ne0$ en $1$. Por eso $P=(x-1)^2(x+2)$ y $\nu_1(P)=2$.

Para $-2$, extraer $x+2$ deja el residual $(x-1)^2$, cuyo valor en $-2$ es $9\ne0$. Por tanto, $\nu_{-2}(P)=1$. Las dos raíces distintas tienen multiplicidades diferentes.

El polinomio cero se excluye de esta definición: cualquier potencia de $x-a$ lo divide, y no existe un mayor entero de extracciones. Las constantes no nulas sí están incluidas; su multiplicidad es cero en cada punto.

**Recuperación resuelta.** Se encontró $P=(x-4)^2Q$. ¿Ya está demostrado que $4$ es raíz doble?

Solo se ha probado que su multiplicidad es al menos dos. Para afirmar que es exactamente dos debemos verificar $Q(4)\ne0$. Por ejemplo, si $Q=x-4$, la multiplicidad es tres; si $Q=x+1$, es dos, pues $Q(4)=5\ne0$.

**Variación resuelta.** Sea $P_t(x)=(x-1)^2(x-t)$, con $t\in K$. Determine la multiplicidad de $1$ según $t$.

Si $t\ne1$, el residual $x-t$ vale $1-t\ne0$ en $1$, así que la multiplicidad es dos. Si $t=1$, obtenemos $P_1=(x-1)^3$, y el residual después de tres extracciones es $1$, no nulo en $1$; la multiplicidad es tres. La condición sobre el parámetro se obtiene evaluando el residual, sin desarrollar el producto.

## 25.7. Multiplicidad de productos y límites del conteo {#apm-c25-s07}

Los factores de un producto pueden aportar varias copias de un mismo factor lineal. Para contarlas necesitamos una regla que sume las multiplicidades sin crear cancelaciones inexistentes.

**Proposición.** Si $P,R\in K[x]$ son no nulos y $a\in K$, entonces $\nu_a(PR)=\nu_a(P)+\nu_a(R)$.

**Demostración.** Escribamos $P=(x-a)^mU$ y $R=(x-a)^sV$, donde $m=\nu_a(P)$, $s=\nu_a(R)$ y $U(a),V(a)\ne0$. Entonces $PR=(x-a)^{m+s}UV$. Como $(UV)(a)=U(a)V(a)\ne0$, la caracterización de [§25.6](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s06) da $\nu_a(PR)=m+s$. $\square$

En particular, multiplicar por una constante no nula no cambia ninguna multiplicidad. El resultado se aplica también cuando uno de los números $m,s$ es cero: el factor que no se anula en $a$ no añade multiplicidad allí.

Por ejemplo, para $P=(x-1)^2(x+2)$ y $R=(x-1)(x+2)^3(x^2+1)$, la multiplicidad de $1$ en $PR$ es $2+1=3$, y la de $-2$ es $1+3=4$. Los factores $x^2+1$ y los factores lineales correspondientes al otro punto no se anulan en el punto evaluado. Así, $PR=(x-1)^3(x+2)^4(x^2+1)$ tiene grado nueve y suma de multiplicidades reales $3+4=7$. El residual $x^2+1$ es positivo en $\mathbb R$ y no aporta otras raíces reales.

### Extraer las multiplicidades de varias raíces

**Proposición.** Sean $a_1,\ldots,a_r$ raíces distintas de un polinomio no nulo $P\in K[x]$, y sea $m_i=\nu_{a_i}(P)$. Entonces existe un polinomio no nulo $Q\in K[x]$ tal que

$$
P(x)=\prod_{i=1}^{r}(x-a_i)^{m_i}Q(x),
\qquad
Q(a_i)\ne0\ \text{para cada }i.
$$

**Demostración.** Extraemos primero $(x-a_1)^{m_1}$ mediante [§25.6](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s06). Supongamos extraídas las potencias correspondientes a $a_1,\ldots,a_{j-1}$ y escribamos $P=B R$, con $B=\prod_{i<j}(x-a_i)^{m_i}$. La evaluación $B(a_j)$ es un producto de diferencias no nulas, por lo que $B(a_j)\ne0$ y $\nu_{a_j}(B)=0$. La aditividad ya probada da $\nu_{a_j}(R)=\nu_{a_j}(P)=m_j$. Podemos extraer de $R$ la potencia $(x-a_j)^{m_j}$ y continuar. Esto construye el producto completo y su cociente no nulo $Q$.

Para cualquier índice $i$, la multiplicidad en $a_i$ del producto completo de factores es $m_i$: los factores de los otros puntos tienen multiplicidad cero allí. La aditividad aplicada a la identidad final da $m_i=m_i+\nu_{a_i}(Q)$. Luego $\nu_{a_i}(Q)=0$, equivalente a $Q(a_i)\ne0$. $\square$

Tomar grados proporciona la cota más precisa

$$
m_1+\cdots+m_r\le\deg P,
\qquad
\deg Q=\deg P-(m_1+\cdots+m_r).
$$

Si la lista incluye todas las raíces de $P$ en $K$, entonces $Q$ no tiene ninguna raíz en $K$. En los puntos de la lista ya probamos que no se anula; en cualquier otro punto, una raíz de $Q$ sería también raíz de $P$ y contradice que la lista fuese completa. La cota de [§25.4](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s04) asegura que podemos listar todas las raíces de un polinomio no nulo en $K$; si no hay ninguna, la suma es cero y el producto sin factores es $1$.

La suma de multiplicidades puede ser menor que el grado aun después de encontrar todas las raíces en el conjunto elegido. Para $S=(x-1)^2(x^2+1)$, la única raíz real es $1$ y tiene multiplicidad dos, pues el residual vale $2$ allí. El grado es cuatro. La diferencia $4-2=2$ es el grado del residual sin raíces reales. La igualdad entre suma y grado ocurre exactamente cuando, después de extraer todas esas potencias, el residual es una constante no nula.

**Recuperación resuelta.** Si $\nu_{-1}(P)=2$ y $R(-1)\ne0$, ¿puede multiplicar por $R$ eliminar la raíz $-1$?

No. Como $\nu_{-1}(R)=0$, la aditividad da $\nu_{-1}(PR)=2$. Los polinomios se multiplican sin denominadores; no hay un factor que pueda cancelar las dos copias de $x+1$.

**Diagnóstico resuelto.** «Un polinomio de grado cinco tiene cinco raíces cuando contamos multiplicidades». ¿Es una conclusión disponible para raíces reales?

No. El polinomio $T=(x-2)(x^2+1)^2$ tiene grado cinco y una única raíz real, $2$, de multiplicidad uno; el residual vale $25$ en $2$ y es positivo en todos los reales. La conclusión disponible es que la suma de multiplicidades reales es a lo sumo cinco. Para que sea cinco hace falta que el polinomio se descomponga por completo en factores lineales reales, condición que el grado por sí solo no garantiza.

## 25.8. Construir polinomios con raíces prescritas {#apm-c25-s08}

Construir un polinomio exige traducir cada dato a una condición sobre factores, grado o evaluaciones. Primero distinguimos «tener estas raíces» de «tener únicamente estas raíces», y «multiplicidad al menos $m$» de «multiplicidad exactamente $m$».

Sean $a_1,\ldots,a_r\in K$ distintos, y sean $m_1,\ldots,m_r$ enteros positivos. Definamos $H(x)=\prod_{i=1}^{r}(x-a_i)^{m_i}$ y $d=m_1+\cdots+m_r$. El polinomio $H$ es mónico y tiene grado $d$.

Todo polinomio no nulo que tenga esas raíces con multiplicidades al menos $m_i$ es de la forma $P=HQ$. Para justificarlo, podemos aplicar la extracción de [§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07) a las multiplicidades efectivas, que son mayores o iguales que las pedidas, y absorber las potencias sobrantes en $Q$. Recíprocamente, cualquier producto $HQ$ con $Q\ne0$ cumple esas cotas inferiores, por la aditividad.

Si pedimos multiplicidades **exactamente** $m_i$, debemos añadir $Q(a_i)\ne0$ para cada $i$. Si además pedimos grado exactamente $N$ y coeficiente principal $c\ne0$, entonces $N\ge d$, el grado de $Q$ es $N-d$ y su coeficiente principal es $c$. La monicidad de $H$ justifica esta última condición.

### Grado mínimo y un valor adicional

Cuando $N=d$, el residual es una constante no nula, de modo que $P=cH$. El coeficiente principal fija todo el polinomio. Si ese coeficiente no estaba dado, un valor $P(b)=v$ con $H(b)\ne0$ obliga a $c=v/H(b)$. Es necesario que $v\ne0$ para conservar el polinomio no nulo de grado $d$.

Si $b$ es una de las raíces prescritas, entonces $H(b)=0$. Un valor $v\ne0$ es incompatible con esa raíz; un valor $v=0$ no agrega información a su anulación y no determina el coeficiente principal.

Busquemos un polinomio de grado tres cuya raíz $-1$ sea doble, cuya raíz $2$ sea simple y que satisfaga $P(0)=-6$. El producto requerido es $H=(x+1)^2(x-2)$, de grado tres; por tanto, $P=cH$. Como $H(0)=-2$, la condición $-2c=-6$ da $c=3$. Obtenemos $P(x)=3(x+1)^2(x-2)=3x^3-9x-6.$

La multiplicidad en $-1$ es exactamente dos: al extraer $(x+1)^2$, el residual $3(x-2)$ vale $-9$ allí. En $2$ es exactamente uno: el residual $3(x+1)^2$ vale $27$. La evaluación en cero devuelve $-6$ y el grado es tres. Si se hubiera añadido coeficiente principal $2$, los datos serían incompatibles, porque el único polinomio con ese coeficiente y esos factores de grado mínimo tendría valor $-4$ en cero.

### Qué libertad deja un grado mayor

Mantengamos las multiplicidades exactas dos en $-1$ y uno en $2$, pero pidamos grado cuatro y coeficiente principal $3$. El residual debe ser lineal de coeficiente principal $3$, así que todos los candidatos tienen la forma

$$
P_t(x)=(x+1)^2(x-2)(3x+t),\qquad t\in K.
$$

La condición de multiplicidad en $-1$ exige $t-3\ne0$; la de $2$ exige $t+6\ne0$. Por tanto, los parámetros admisibles son $t\ne3,-6$. Queda una familia de polinomios, y un valor adicional puede seleccionarlos: $P_t(0)=-2t$. Si imponemos $P_t(0)=-2$, resulta $t=1$, que es admisible. El polinomio correspondiente es $3x^4+x^3-9x^2-9x-2$.

En cambio, imponer $P_t(0)=-6$ fuerza $t=3$. El producto sería $3(x+1)^3(x-2)$, que aumenta a tres la multiplicidad de $-1$. Ese dato era compatible con el grado mínimo tres del ejemplo anterior, pero resulta incompatible con el nuevo conjunto de condiciones: grado cuatro, coeficiente principal $3$ y multiplicidades exactas dos y uno.

Para un residual de grado mayor, la condición $P(b)=v$ en un punto con $H(b)\ne0$ se convierte en $Q(b)=v/H(b)$. Es una restricción sobre $Q$, además de su grado, su coeficiente principal y sus valores no nulos en las raíces de $H$; no garantiza por sí sola unicidad.

**Recuperación resuelta.** ¿Puede un polinomio real de grado cuatro tener únicamente las raíces $-1$ y $2$, con multiplicidades exactas dos y uno?

No. Después de extraer $H$, queda un residual lineal no nulo, que tiene una raíz real. Si esa raíz fuera $-1$ o $2$, aumentaría una de sus multiplicidades; si fuera otra, añadiría una raíz distinta. Ambas posibilidades contradicen las condiciones. En grado cinco sí existe un ejemplo: $H(x)(x^2+1)$ conserva esas multiplicidades y no añade raíces reales.

**Comprobación resuelta.** Se solicita grado dos con una raíz doble en $-1$ y otra simple en $2$. ¿Hace falta resolver un sistema de coeficientes?

No. Los factores exigidos tienen grado total $2+1=3$, y deben dividir a cualquier polinomio no nulo que cumpla las multiplicidades. La cota de [§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07) obliga a un grado al menos tres. Las condiciones son incompatibles antes de iniciar un cálculo de coeficientes.

## 25.9. Teorema de las raíces racionales {#apm-c25-s09}

Para un polinomio con coeficientes enteros, una raíz racional tiene un numerador y un denominador restringidos por dos coeficientes: el término constante y el coeficiente principal. Esto reduce la búsqueda a una lista finita, siempre que el término constante sea no nulo.

El argumento necesita una propiedad de divisibilidad entera. La recordamos con su justificación para no confundir «no divide» con «es coprimo».

### El paso aritmético de la prueba

**Lema.** Sean $u,v\in\mathbb Z$ no nulos y coprimos, sea $k\ge1$ y sea $w\in\mathbb Z$. Si $u$ divide a $v^kw$, entonces $u$ divide a $w$.

**Demostración.** La identidad de Bézout para enteros proporciona $s,t\in\mathbb Z$ con $su+tv=1$. Para recuperar su justificación, consideramos el menor entero positivo de la forma $su+tv$, que existe porque hay combinaciones positivas. Al dividir $u$ y $v$ por ese entero, cada resto es también una combinación de $u,v$. Un resto positivo y menor contradiría su elección; por tanto, ambos restos son cero. El entero elegido divide a $u,v$, y la coprimalidad obliga a que sea $1$.

Elevando $su+tv=1$ a la potencia $k$ y desarrollando, todos los términos salvo $t^kv^k$ contienen un factor $u$. Así, $1=uA+t^kv^k$ para algún $A\in\mathbb Z$. Multiplicamos por $w$: $w=uAw+t^kv^kw$. Ambos términos de la derecha son divisibles por $u$ bajo la hipótesis del lema, de modo que $u$ divide a $w$. $\square$

Los signos de $u,v$ no afectan la divisibilidad ni la coprimalidad. En cambio, reemplazar la coprimalidad por $u\nmid v$ haría falso el lema: $6$ divide a $2\cdot3$, pero no divide a $2$ ni a $3$.

### Numerador y denominador de una raíz

**Teorema de las raíces racionales.** Sea $P(x)=a_nx^n+\cdots+a_1x+a_0$, con coeficientes enteros, $n\ge1$, $a_n\ne0$ y $a_0\ne0$. Si $p/q$ es una raíz, escrita en forma irreducible con $p\in\mathbb Z$, $q>0$ y $\gcd(|p|,q)=1$, entonces $p$ divide a $a_0$ y $q$ divide a $a_n$.

**Demostración.** Como $a_0\ne0$, la raíz no puede ser cero y $p\ne0$. Multiplicamos $P(p/q)=0$ por $q^n$:

$$
a_np^n+a_{n-1}p^{n-1}q+\cdots+a_1pq^{n-1}+a_0q^n=0.
$$

Todos los términos salvo el último son divisibles por $p$, por lo que $p$ divide a $a_0q^n$. Aplicamos el lema con $u=p$, $v=q$, $k=n$ y $w=a_0$; la fracción irreducible asegura la coprimalidad necesaria. Se sigue que $p$ divide a $a_0$.

Todos los términos salvo el primero son divisibles por $q$, de modo que $q$ divide a $a_np^n$. Aplicamos el mismo lema con $u=q$, $v=p$, $k=n$ y $w=a_n$, y obtenemos que $q$ divide a $a_n$. $\square$

Por tanto, los candidatos se construyen con numeradores entre los divisores positivos y negativos de $a_0$ y denominadores positivos entre los divisores de $|a_n|$. Reducimos las fracciones y eliminamos duplicados. Cada raíz racional está en esa lista; pertenecer a la lista no demuestra que sea raíz.

Si $P$ es mónico, $a_n=1$ y necesariamente $q=1$. Sus raíces racionales, si las tiene, son enteros que dividen al término constante. La conclusión se refiere a coeficientes enteros: un polinomio mónico con coeficientes racionales puede tener raíces racionales no enteras.

### Candidatos y comprobaciones

Para $P(x)=2x^2-5x+2$, los candidatos racionales distintos son $\pm1,\pm2,\pm1/2$. Las evaluaciones exactas son:

| Candidato $a$ | $P(a)$ | Resultado |
|---|---:|---|
| $1$ | $-1$ | No es raíz |
| $-1$ | $9$ | No es raíz |
| $2$ | $0$ | Es raíz |
| $-2$ | $20$ | No es raíz |
| $1/2$ | $0$ | Es raíz |
| $-1/2$ | $5$ | No es raíz |

El producto $(2x-1)(x-2)=2x^2-5x+2$ confirma la factorización. En particular, no se deduce que $1$ sea raíz por el hecho de que su numerador y su denominador cumplan las divisibilidades.

**Recuperación resuelta.** Determine las raíces racionales de $x^3-2$ usando el teorema.

Por ser mónico, sus candidatos son $\pm1,\pm2$. Sus valores son, respectivamente, $-1,-3,6,-10$, todos no nulos. Por tanto, no tiene raíces racionales. Esto no excluye raíces reales: $\sqrt[3]{2}$ es real y su cubo es $2$.

**Diagnóstico resuelto.** Se afirma: «Como $p$ no divide a $q^n$ y divide a $a_0q^n$, divide a $a_0$». ¿Qué argumento falta?

La condición suficiente es la coprimalidad entre $p$ y $q$, seguida del lema aritmético. El ejemplo $6\mid3\cdot2$ con $6\nmid2$ y $6\nmid3$ refuta la inferencia basada solo en «no divide». En la prueba del teorema, la fracción irreducible aporta la hipótesis correcta, y el lema explica cómo se utiliza.



### Una lista exhaustiva de candidatos todavía necesita evaluaciones

El teorema de raíces racionales proporciona una condición necesaria. Para $P=2x^2+x-1$, los candidatos reducidos son $\pm1,\pm1/2$. Evaluarlos da $P(1)=2$, $P(-1)=0$, $P(1/2)=0$, $P(-1/2)=-1$. Solo $-1,1/2$ son raíces, y $(2x-1)(x+1)$ reconstruye el polinomio. **Control resuelto:** decir que $1$ es raíz porque divide al término independiente confunde pertenencia a la lista con verificación. Si el término constante es cero, primero extraemos las potencias de $x$ y aplicamos el teorema al residual de término constante no nulo. La lista completa evita perder candidatos; las evaluaciones separan los candidatos de las soluciones.

## 25.10. Búsqueda finita y factorización progresiva {#apm-c25-s10}

Una lista de candidatos organiza la búsqueda, pero el trabajo puede reducirse a medida que encontramos factores. Después de extraer una raíz, buscamos en el cociente: cada raíz del polinomio original es la ya extraída o una raíz del cociente. Una factorización comprobada permite conservar esa información sin volver a evaluar todos los candidatos originales.

### Preparar el polinomio

Si los coeficientes son racionales, multiplicamos por un entero positivo que elimine sus denominadores. El polinomio cambia, pero sus raíces y multiplicidades se conservan, pues multiplicar por una constante no nula no cambia la anulación ni la multiplicidad ([§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07)). Por ejemplo,

$$
A(x)=\frac{x^3}{2}-\frac{2x^2}{3}-\frac{17x}{6}+1,
\qquad
6A(x)=3x^3-4x^2-17x+6.
$$

El teorema de raíces racionales se aplica al segundo polinomio, con coeficientes enteros. Si todos esos coeficientes tienen además un divisor común, podemos retirarlo como factor constante; esto puede acortar la lista de candidatos sin cambiar las raíces.

Si el término constante es cero, extraemos primero la potencia de $x$ presente en todos los términos. Para un polinomio no nulo, escribimos $P=x^mB$, donde $B(0)\ne0$; el exponente $m$ es el menor exponente con coeficiente no nulo. Entonces $0$ tiene multiplicidad $m$, y las raíces no nulas están en $B$. Aplicar directamente la regla «el numerador divide al término constante» no produce una lista finita cuando ese término es cero: todo entero no nulo divide a $0$.

Para $Z(x)=2x^5-5x^4+2x^3$, extraemos $x^3$ y recuperamos la cuadrática anterior:

$$
Z(x)=x^3(2x^2-5x+2)=x^3(2x-1)(x-2).
$$

La raíz $0$ tiene multiplicidad tres porque el residual vale $2$ en cero; $1/2$ y $2$ son simples. La suma de multiplicidades es cinco, igual al grado en este ejemplo.

### Buscar, extraer y reconstruir

Consideremos $P(x)=3x^3-4x^2-17x+6$. Los candidatos racionales son $\pm1,\pm2,\pm3,\pm6,\pm1/3,\pm2/3$. Podemos probarlos en un orden conveniente, siempre manteniendo el registro de qué hemos comprobado. En particular, $P(1)=-12$ y $P(-1)=16$ descartan esos dos números. En cambio,

$$
P(1/3)=\frac19-\frac49-\frac{17}3+6=0.
$$

Horner con los coeficientes $3,-4,-17,6$ y el número $1/3$ produce los coeficientes $3,-3,-18$ del cociente y resto cero. Así, $P=(x-1/3)(3x^2-3x-18)$. El cociente admite $-2$ como raíz; al dividirlo por $x+2$ queda $3x-9$. Por tanto,

$$
P(x)=(x-1/3)(x+2)(3x-9)=(3x-1)(x+2)(x-3).
$$

La reconstrucción confirma el resultado: $(x+2)(x-3)=x^2-x-6$, y multiplicar por $3x-1$ devuelve $3x^3-4x^2-17x+6$. Las raíces son $1/3,-2,3$. La identidad muestra que ninguna otra raíz real puede existir, pues todo cero del producto debe anular uno de sus factores lineales. Las tres raíces son distintas y sus multiplicidades son uno.

No fue necesario evaluar todos los candidatos de la primera lista. Dejamos de buscarlos cuando la factorización completa proporcionó una justificación de exhaustividad. Si un cociente no tiene raíces racionales, la búsqueda racional termina allí, pero aún puede haber raíces reales no racionales o factores de grado mayor.

Al formar una nueva lista para un cociente con coeficientes racionales, podemos eliminar sus denominadores de nuevo. Hay que utilizar el término constante y el coeficiente principal de ese cociente preparado, no los del polinomio original. Cada extracción disminuye el grado, así que el proceso de extraer factores lineales no puede continuar indefinidamente.

**Recuperación resuelta.** Un polinomio entero no nulo tiene término constante cero y es $P=x^2(x^2+1)$. ¿Cuáles son sus raíces racionales y reales?

La extracción inicial certifica que $0$ tiene multiplicidad dos, porque el residual vale $1$ en cero. El residual $x^2+1$ es positivo para todo real, por lo que no aporta raíces reales ni racionales. La única raíz en ambos conjuntos es $0$, aunque el grado del polinomio sea cuatro.

**Diagnóstico resuelto.** Se sustituye $A$ por $6A$ para eliminar denominadores y se afirma que todos sus valores siguen siendo iguales. ¿Qué se conserva?

Se conservan las raíces y sus multiplicidades; los valores se multiplican por seis. En el ejemplo inicial, $A(0)=1$, mientras que $(6A)(0)=6$. Si una condición de construcción exigía un valor concreto, habría que transformarla al multiplicar el polinomio. La preparación para buscar ceros no autoriza a ignorar esa diferencia.

## 25.11. Factores cuadráticos y elección del dominio {#apm-c25-s11}

La búsqueda racional puede dejar un factor cuadrático. Para decidir qué hacer con él, utilizamos el discriminante y especificamos si buscamos factores en $\mathbb Q[x]$ o en $\mathbb R[x]$.

Sea $B(x)=ax^2+bx+c$, con $a\ne0$. Recuperamos de C21 el discriminante $\Delta=b^2-4ac$ y la identidad $4aB(x)=(2ax+b)^2-\Delta$. Para coeficientes reales, los casos son:

| Discriminante | Raíces reales | Forma factorizada real |
|---|---|---|
| $\Delta>0$ | Dos distintas: $r_\pm=(-b\pm\sqrt\Delta)/(2a)$ | $a(x-r_+)(x-r_-)$ |
| $\Delta=0$ | Una doble: $r=-b/(2a)$ | $a(x-r)^2$ |
| $\Delta<0$ | Ninguna | No hay descomposición en dos factores de grado positivo en $\mathbb R[x]$ |

Las dos primeras identidades se comprueban con $r_++r_-=-b/a$ y $r_+r_-=c/a$, o completando el cuadrado cuando $\Delta=0$. En el primer caso, el residual tras extraer cualquiera de los factores lineales no se anula en su raíz, pues las dos raíces son distintas; ambas son simples.

Si $\Delta<0$, la identidad $4aB(x)=(2ax+b)^2-\Delta$ tiene lado derecho positivo para todo real $x$. Por eso $B(x)$ nunca vale cero. Una descomposición $B=UV$ con ambos grados positivos obligaría, por la regla del grado, a que ambos factores fueran lineales. Todo polinomio lineal real no constante tiene una raíz real, que sería también raíz de $B$; la ausencia de raíces descarta esa descomposición.

### La restricción adicional para coeficientes racionales

Supongamos $a,b,c\in\mathbb Q$. La existencia de raíces reales no garantiza que pertenezcan a $\mathbb Q$. Hay raíces racionales si y solo si $\Delta$ es el cuadrado de un racional, incluyendo el cuadrado cero.

Si $\Delta=s^2$ con $s\in\mathbb Q$, la fórmula cuadrática produce raíces racionales. Recíprocamente, si $r\in\mathbb Q$ es raíz, al evaluar la identidad anterior obtenemos $\Delta=(2ar+b)^2$, el cuadrado de un racional. En tal caso, la otra raíz también es racional, pues su suma con $r$ es $-b/a$.

Esto decide la descomposición cuadrática en $\mathbb Q[x]$: si tiene una raíz racional, el teorema del factor deja un cociente lineal racional. Si se descompone en dos factores de grado positivo con coeficientes racionales, ambos deben ser lineales y uno proporciona una raíz racional. No estamos usando aquí la regla para grados mayores.

Por ejemplo, $x^2-2$ tiene discriminante $8$, que no es un cuadrado racional: si $s^2=8$ con $s$ racional, $(s/2)^2=2$ contradiría [§25.1](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s01). En $\mathbb Q[x]$ no se descompone en dos factores de grado positivo. En $\mathbb R[x]$ sí tenemos $(x-\sqrt2)(x+\sqrt2)$.

Para $2x^2-5x+2$, el discriminante es $9=3^2$, y la fórmula da $2$ y $1/2$. La factorización $(2x-1)(x-2)$ utiliza coeficientes enteros; equivalentemente, es $2(x-1/2)(x-2)$ en $\mathbb Q[x]$ y en $\mathbb R[x]$. La constante $2$ debe conservarse para reconstruir el coeficiente principal.

El polinomio $x^2+x+1$ tiene discriminante $-3$. Completar el cuadrado da $(x+1/2)^2+3/4>0$ para todo real. No tiene raíces reales y no se descompone en factores de grado positivo sobre $\mathbb R$ ni sobre $\mathbb Q$.

**Recuperación resuelta.** Clasifique $B(x)=x^2+2x+1$ según sus raíces y multiplicidades.

El discriminante es cero y $B=(x+1)^2$. Su única raíz real y racional es $-1$, con multiplicidad dos, porque el residual después de extraer las dos copias de $x+1$ es la constante $1$. La fórmula cuadrática produce dos expresiones iguales; no son dos números distintos.

**Diagnóstico resuelto.** «Como el discriminante es positivo, la cuadrática se factoriza en $\mathbb Q[x]$». ¿Qué debe corregirse?

Un discriminante positivo asegura dos raíces reales distintas. Para que la descomposición sea en $\mathbb Q[x]$, hace falta además que el discriminante sea un cuadrado racional. El ejemplo $x^2-2$ distingue ambas condiciones: tiene raíces reales distintas y ninguna racional.

## 25.12. Estrategias de factorización de grados mayores {#apm-c25-s12}

Antes de preparar una lista de candidatos, inspeccionamos la forma del polinomio. Un factor común, una agrupación o una sustitución puede reducir el problema más que una sucesión de evaluaciones. La forma desarrollada permite comprobar coeficientes; la forma factorizada permite leer raíces, multiplicidades y grado residual.

### Agrupar términos y reconocer una expresión repetida

En $P(x)=x^3+2x^2-9x-18$, los dos primeros términos contienen $x^2$ y los dos últimos contienen $-9$. Agrupar produce

$$
P(x)=x^2(x+2)-9(x+2)=(x+2)(x^2-9)=(x+2)(x-3)(x+3).
$$

Las raíces reales y racionales son $-2,3,-3$, todas simples. La expresión repetida $x+2$ hace útil la agrupación; la diferencia de cuadrados termina el cálculo. Multiplicar los factores devuelve la expresión inicial.

En una expresión con solo potencias pares, la sustitución $y=x^2$ puede reducir el grado del cálculo. Para $S(x)=x^4-10x^2+9$, resolvemos primero la factorización $y^2-10y+9=(y-1)(y-9)$. Al sustituir de nuevo,

$$
S(x)=(x^2-1)(x^2-9)=(x-1)(x+1)(x-3)(x+3).
$$

Las raíces son $\pm1,\pm3$. Si se usa la sustitución para resolver una ecuación real, hay que recordar que $y=x^2\ge0$; un valor negativo de $y$ no corresponde a ningún $x$ real.

Para $T(x)=x^4+3x^2+2$, la misma estrategia da $T=(x^2+1)(x^2+2)$. Ambos factores son positivos en $\mathbb R$, así que $T$ no tiene raíces reales ni racionales. Sin embargo, sí está expresado como producto de dos factores de grado positivo, incluso con coeficientes racionales. La ausencia de raíces descarta factores lineales en el dominio elegido; no descarta factores cuadráticos en un polinomio de grado cuatro.

### Combinar búsqueda racional y control del residual

Consideremos la cuártica $F(x)=2x^4-x^3+2x^2+19x-10$, sabiendo que tiene una raíz racional positiva no entera y una raíz entera negativa. El teorema de raíces racionales restringe la primera a $1/2$ o $5/2$, y la segunda a $-1,-2,-5,-10$. Estas listas utilizan la información adicional y las fracciones reducidas.

Evaluar en $1/2$ da $1/8-1/8+1/2+19/2-10=0$. La división por $x-1/2$ produce el cociente $2x^3+2x+20$. Por tanto, $F(x)=(2x-1)(x^3+x+10).$

Para buscar la raíz entera negativa, podemos trabajar en el cociente: en ninguno de esos números se anula $2x-1$. Probamos $-2$ y obtenemos $-8-2+10=0$. Dividir $x^3+x+10$ por $x+2$ deja $x^2-2x+5$. Así,

$$
F(x)=(2x-1)(x+2)(x^2-2x+5).
$$

El residual cuadrático es $(x-1)^2+4>0$ para todo real. Por ello, las únicas raíces reales son $1/2$ y $-2$. Son simples: el residual al extraer $x-1/2$ es $2(x+2)(x^2-2x+5)$, no nulo en $1/2$; al extraer $x+2$, el residual es $(2x-1)(x^2-2x+5)$, no nulo en $-2$.

La comprobación por coeficientes también es breve: $(x+2)(x^2-2x+5)=x^3+x+10$, y multiplicar por $2x-1$ devuelve $2x^4-x^3+2x^2+19x-10$. La búsqueda queda cerrada por la identidad y la positividad del residual, sin necesidad de evaluar los candidatos restantes.

### Elegir qué información necesita la conclusión

Una factorización es un certificado cuando el producto se reconstruye y los factores pertenecen al conjunto de coeficientes elegido. Para responder «todas las raíces reales», también debemos justificar qué raíces aportan los factores residuales. Para afirmar multiplicidades exactas, evaluamos esos residuales en las raíces extraídas. Son comprobaciones diferentes y cada una responde a una parte de la pregunta.

**Recuperación resuelta.** Factorice $U(x)=x^4+2x^2-3$ y determine todas sus raíces reales.

La sustitución $y=x^2$ da $y^2+2y-3=(y-1)(y+3)$. Por tanto, $U=(x^2-1)(x^2+3)=(x-1)(x+1)(x^2+3)$. El factor $x^2+3$ es positivo para todo real; las únicas raíces son $1$ y $-1$, ambas simples porque el residual de cada factor lineal no se anula en su raíz. Los valores $y=1,-3$ de la ecuación auxiliar no se convierten ambos en raíces reales de la original: solo $y=1$ es compatible con $y=x^2\ge0$.

**Diagnóstico resuelto.** Una búsqueda exhaustiva de candidatos racionales de una cuártica no encontró ninguna raíz, y se concluyó que no se puede factorizar en $\mathbb Q[x]$. ¿Cómo se evalúa esa conclusión?

La búsqueda demuestra que no existen raíces racionales y, por el teorema del factor, que no hay factores lineales racionales. El ejemplo $x^4+3x^2+2=(x^2+1)(x^2+2)$ muestra que aún puede haber factores cuadráticos racionales. Para descartar cualquier descomposición de grado positivo habría que examinar también esa posibilidad.

## 25.13. Irreducibilidad elemental {#apm-c25-s13}

Una descomposición en factores lineales puede terminar dejando un factor de grado mayor. La cuestión es entonces si ese factor admite otra descomposición dentro del conjunto de coeficientes elegido. Las constantes no nulas deben separarse de esta pregunta: siempre podemos escribir $P=c(P/c)$, y ese cambio no reduce el problema de factorización.

Trabajamos en $K[x]$, con $K=\mathbb Q$ o $K=\mathbb R$. Un polinomio no nulo de grado positivo es **irreducible sobre $K$** si en toda identidad $P=AB$, con $A,B\in K[x]$, al menos uno de los factores es constante. Es **reducible sobre $K$** si admite una identidad así con ambos factores de grado positivo.

Como $P\ne0$, ninguno de los factores de una identidad $P=AB$ puede ser cero. La condición de irreducibilidad permite factores constantes no nulos; prohíbe una descomposición en dos partes de grado positivo. En este capítulo reservamos «reducible» e «irreducible» para polinomios no nulos de grado positivo: el cero y las constantes quedan fuera de esa clasificación.

### Constantes, grado y normalización

Las constantes no nulas son precisamente los polinomios con inverso multiplicativo en $K[x]$ ([§24.5](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s05)). En efecto, una constante $c\ne0$ tiene inverso $1/c$. Si $AB=1$, la regla del grado exige $\deg A+\deg B=0$, así que ambos son constantes no nulas. Estos polinomios se llaman **unidades**.

Todo polinomio lineal no constante es irreducible. Si $P=AB$ tiene grado uno, la igualdad $\deg A+\deg B=1$ obliga a que uno de los grados sea cero. Por ejemplo, $2x-1$ es irreducible en $\mathbb Q[x]$ y en $\mathbb R[x]$, aunque tenga la raíz $1/2$.

Multiplicar por una constante no nula conserva la irreducibilidad. Si $cP=AB$ con ambos grados positivos, entonces $P=(A/c)B$ proporciona una descomposición de los mismos grados. Recíprocamente, una descomposición $P=UV$ produce $cP=(cU)V$ con ambos grados positivos. Por tanto, $P$ y $cP$ son reducibles o irreducibles simultáneamente.

Dos polinomios no nulos de $K[x]$ se llaman **asociados** si uno es un múltiplo del otro por una constante no nula. Por ejemplo, $2x-2$ y $x-1$ son asociados; al normalizarlos como mónicos obtenemos el mismo polinomio.

Si $c$ es el coeficiente principal de $P$, el polinomio $P/c$ es mónico. Normalizarlo así facilita comparar factores: retiramos una constante y conservamos su condición de irreducibilidad. La constante deberá volver a aparecer al reconstruir el polinomio.

### El dominio pertenece a la afirmación

Por [§25.11](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s11), $x^2-2$ no se descompone en dos factores de grado positivo en $\mathbb Q[x]$; es irreducible sobre $\mathbb Q$. En $\mathbb R[x]$ se descompone como $(x-\sqrt2)(x+\sqrt2)$ y es reducible. No hay contradicción: los factores permitidos son distintos en ambos conjuntos.

El polinomio $x^2+1$ es irreducible sobre $\mathbb R$ y sobre $\mathbb Q$. La positividad $a^2+1>0$ descarta raíces reales. Cualquier descomposición de una cuadrática en dos factores de grado positivo tendría dos factores lineales y produciría una raíz en el conjunto de coeficientes, como se justificó en [§25.11](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s11).

**Recuperación resuelta.** Se escribe $x^2+1=2[(x^2+1)/2]$. ¿Se ha demostrado que es reducible?

No. Uno de los factores es constante y tiene grado cero. Esa identidad está permitida por la definición de irreducibilidad. Para demostrar reducibilidad haría falta una descomposición con ambos grados positivos.

**Diagnóstico resuelto.** Se afirma que todo irreducible carece de raíces en su conjunto de coeficientes. ¿Qué excepción necesita la afirmación?

Los irreducibles lineales sí tienen una raíz: para $ax+b$, con $a\ne0$, es $-b/a\in K$. Por tanto, la afirmación solo puede plantearse para irreducibles de grado al menos dos. El grado es una hipótesis que no debe omitirse.



### El criterio por raíces termina donde cambian las particiones del grado

Una cuadrática o una cúbica reducible tiene un factor lineal: las particiones en dos grados positivos son $1+1$ y $1+2$. Por eso, en esos grados, ausencia de raíces en $K$ certifica irreducibilidad en $K[x]$. En grado cuatro existe además $2+2$, que puede no producir raíces en $K$. **Control resuelto:** $(x^2+1)(x^2+2)$ es reducible sobre $\mathbb R$, pero siempre positivo en la recta. No encontrar raíces reales no descarta sus dos factores cuadráticos. Para una cuártica se necesita un certificado que examine también esa posibilidad. La conclusión debe indicar cuerpo y grado; una regla válida para grados dos y tres no se extiende por analogía.

## 25.14. Criterios para grados dos y tres {#apm-c25-s14}

En cualquier grado al menos dos, una raíz en $K$ demuestra reducibilidad: el teorema del factor da $P=(x-a)Q$, y el cociente tiene grado $\deg P-1\ge1$. La afirmación recíproca requiere controlar cómo puede repartirse el grado entre dos factores.

**Teorema.** Si $P\in K[x]$ tiene grado dos o tres, entonces es irreducible sobre $K$ si y solo si no tiene raíces en $K$.

**Demostración.** Si $P$ tiene una raíz $a\in K$, el argumento anterior lo descompone en dos factores de grado positivo. Por tanto, un irreducible de esos grados no puede tener raíces en $K$.

Recíprocamente, supongamos que $P$ es reducible y escribamos $P=AB$ con ambos grados positivos. La suma de esos grados es dos o tres, de modo que uno de ellos debe ser uno: las únicas reparticiones posibles son $1+1$, $1+2$ y $2+1$. Ese factor lineal tiene una raíz en $K$, y la identidad del producto la convierte en raíz de $P$. Por contraposición, si $P$ no tiene raíces en $K$, no puede ser reducible. $\square$

Para una cuadrática racional, [§25.11](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s11) convierte este criterio en otro comprobable: es irreducible sobre $\mathbb Q$ si y solo si su discriminante no es un cuadrado racional. Para una cuadrática real, es irreducible sobre $\mathbb R$ si y solo si su discriminante es negativo. El caso de discriminante cero produce dos factores lineales iguales, por lo que sigue siendo reducible.

### Una cúbica que cambia al ampliar los coeficientes

El polinomio $P(x)=x^3-2$ no tiene raíces racionales, como se comprobó en [§25.9](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s09) mediante su lista completa de candidatos. Por el criterio de grado tres, es irreducible sobre $\mathbb Q$.

En $\mathbb R$, el número $r=\sqrt[3]{2}$ satisface $r^3=2$ y proporciona la identidad

$$
x^3-2=(x-r)(x^2+rx+r^2).
$$

La expansión cancela los términos intermedios y deja $x^3-r^3$. Como $r>0$, el discriminante del residual es $r^2-4r^2=-3r^2<0$: es una cuadrática irreducible real. Por tanto, la cúbica es reducible sobre $\mathbb R$, con una única raíz real $r$, simple, pues el residual vale $3r^2\ne0$ allí. La existencia de esa raíz proviene del radical ya disponible; no se ha utilizado un teorema general de existencia de raíces para todos los grados.

### El límite de la prueba por raíces

En grado cuatro aparece una repartición nueva, $2+2$, que no obliga a que exista un factor lineal. El ejemplo

$$
x^4+3x^2+2=(x^2+1)(x^2+2)
$$

es reducible sobre $\mathbb Q$ y sobre $\mathbb R$, aunque no tiene raíces reales: ambos factores son positivos. La búsqueda exhaustiva de raíces racionales tampoco podría certificar su irreducibilidad.

Para una cuártica sin raíces en $K$, las reparticiones $1+3$ y $3+1$ están descartadas, pero queda por examinar la posibilidad de dos factores cuadráticos. El teorema de grados dos y tres funciona porque allí no existe esa posibilidad.

**Recuperación resuelta.** Determine si $C(x)=x^3-3x+1$ es irreducible sobre $\mathbb Q$.

Por ser mónico con coeficientes enteros y término constante $1$, sus únicos candidatos racionales son $1$ y $-1$. Los valores son $C(1)=-1$ y $C(-1)=3$, de modo que no hay raíces racionales. Como su grado es tres, el criterio demuestra irreducibilidad sobre $\mathbb Q$. Esta comprobación no decide aquí una factorización sobre $\mathbb R$.

**Diagnóstico resuelto.** «Un polinomio tiene grado uno y una raíz racional, así que es reducible sobre $\mathbb Q$». ¿Qué falla?

Extraer el factor lineal deja un cociente constante, no otro factor de grado positivo. El argumento de reducibilidad por una raíz necesitaba grado al menos dos. Los polinomios lineales son irreducibles y sí tienen raíces.

## 25.15. Existencia y unicidad de factores irreducibles {#apm-c25-s15}

Una identidad factorizada debe distinguirse de una factorización terminada. Por ejemplo, agrupar términos puede producir factores que todavía sean reducibles. Probaremos que todo polinomio no nulo admite una descomposición en irreducibles y que, al normalizar los factores como mónicos, esa descomposición es única salvo el orden.

La existencia se obtiene bajando el grado. Para la unicidad necesitamos un resultado distinto: un irreducible que divide un producto debe dividir alguno de sus factores. Bézout de [§24.15](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s15) proporciona ese paso.

### Un irreducible que divide un producto

**Lema.** Sean $I,A,B\in K[x]$, con $I$ irreducible y $A,B$ no nulos. Si $I$ divide a $AB$, entonces $I$ divide a $A$ o divide a $B$.

**Demostración.** Si $I$ divide a $A$, la conclusión ya se cumple. Supongamos que no lo divide y sea $D$ el MCD mónico de $I,A$. Como $D$ divide a $I$, escribimos $I=DE$. Si $D$ tuviera grado positivo, la irreducibilidad de $I$ obligaría a que $E$ fuera una constante no nula. Entonces $I$ sería un múltiplo constante de $D$; como $D$ divide a $A$, también $I$ dividiría a $A$, contradiciendo nuestra suposición.

Por tanto, $D$ tiene grado cero y, por ser mónico, es $1$. Bézout da $UI+VA=1$ para ciertos $U,V\in K[x]$. Multiplicamos por $B$:

$$
B=UIB+VAB.
$$

El primer sumando es divisible por $I$, y el segundo también porque $I$ divide a $AB$. Así, $I$ divide a $B$. $\square$

Por inducción sobre el número de factores, si $I$ divide un producto finito de polinomios no nulos, divide alguno de ellos. Para pasar de dos a más, aplicamos el lema al primer factor y al producto de los restantes; si divide este último, repetimos el argumento. Un irreducible no puede dividir a una constante no nula, porque su grado es positivo.

### Teorema de factorización

**Teorema.** Todo polinomio no nulo $P\in K[x]$ se escribe como

$$
P=c\,I_1I_2\cdots I_r,
$$

donde $c\in K$ es su coeficiente principal, cada $I_j$ es mónico e irreducible sobre $K$, y los factores pueden repetirse. La lista de factores es única salvo su orden. Si $P$ es constante, $r=0$ y el producto sin factores es $1$.

**Demostración de existencia.** Procedemos por inducción fuerte sobre $n=\deg P$. Si $n=0$, $P$ es una constante no nula y basta el producto sin factores. Si $n\ge1$ y $P$ es irreducible, escribimos $P=c(P/c)$; el segundo factor es mónico e irreducible por [§25.13](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s13).

Si $P$ es reducible, existe una descomposición $P=AB$ con ambos grados positivos y menores que $n$. Por la hipótesis inductiva, tanto $A$ como $B$ se descomponen en factores mónicos irreducibles. Multiplicamos sus descomposiciones. El producto de sus coeficientes principales es el coeficiente principal de $P$ ([§24.4](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s04)), así que obtenemos exactamente la forma afirmada. Este paso cubre todos los casos y completa la inducción. $\square$

**Demostración de unicidad.** Supongamos que hay dos descomposiciones

$$
P=c\,I_1\cdots I_r=d\,J_1\cdots J_s,
$$

con todos los factores mónicos e irreducibles. Comparar coeficientes principales da $c=d$, y cancelamos esa constante no nula. Si una lista está vacía, su producto tiene grado cero; la igualdad de grados obliga a que la otra también esté vacía.

Si ambas listas son no vacías, $I_1$ divide el producto $J_1\cdots J_s$. Por el lema, divide algún $J_j$, que podemos colocar primero. Escribimos $J_j=I_1H$. Como $J_j$ es irreducible y $I_1$ tiene grado positivo, $H$ debe ser una constante no nula. La monicidad de $I_1,J_j$ obliga a $H=1$, de modo que $I_1=J_j$.

Cancelamos el factor común utilizando [§24.5](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s05) y repetimos con las listas restantes. Cada cancelación elimina un factor de cada lado, así que el proceso es finito. No puede quedar una lista vacía y otra no vacía: sus productos tendrían grados cero y positivo, respectivamente. Por tanto, $r=s$ y los factores coinciden, contando sus repeticiones, después de reordenarlos. $\square$

### Qué fija la normalización

Para $P=6(x-1)^2(x^2+1)$, los factores mónicos irreducibles sobre $\mathbb Q$ y sobre $\mathbb R$ son $x-1,x-1,x^2+1$, y el coeficiente principal separado es $6$. La escritura $(2x-2)(3x-3)(x^2+1)$ distribuye esa constante entre dos factores, pero al normalizar devuelve la misma lista. El orden tampoco crea una factorización distinta.

La repetición de un factor irreducible no siempre corresponde a una raíz en $K$. El producto $(x^2+1)^2$ repite un irreducible real y no tiene raíces reales. En cambio, para un factor lineal mónico $x-a$, su número de repeticiones en la descomposición es $\nu_a(P)$. Los otros factores lineales se anulan en otros puntos; los irreducibles de grado al menos dos no pueden tener una raíz en $K$, pues eso los haría reducibles por [§25.14](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s14). La aditividad de [§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07) justifica el conteo.

El teorema asegura existencia y unicidad; no proporciona por sí solo una lista de todos los irreducibles posibles ni un procedimiento breve para encontrarlos en cualquier grado.

**Recuperación resuelta.** Si un irreducible $I$ divide a $A^2$, con $A\ne0$, ¿debe dividir a $A$?

Sí. Aplicamos el lema al producto $A\cdot A$: sus dos alternativas son la misma afirmación, $I\mid A$. La irreducibilidad es la hipótesis que convierte la divisibilidad del producto en divisibilidad de un factor.

**Diagnóstico resuelto.** Se usa la regla «si $D$ divide a $AB$, divide a $A$ o a $B$» para cualquier polinomio no constante $D$. ¿Es válida?

No. Tomemos $D=x^2-1$, $A=x-1$ y $B=x+1$. Entonces $D=AB$ divide al producto, pero no divide a ninguno de los factores, pues ambos tienen grado menor. El polinomio $D$ es reducible; el lema necesita irreducibilidad, o una hipótesis de coprimalidad adecuada como la de C24.

## 25.16. Síntesis: qué se puede certificar {#apm-c25-s16}

Las herramientas del capítulo responden a preguntas diferentes. Evaluar certifica una raíz; dividir extrae su factor; repetir la división determina su multiplicidad. El grado limita cuántos factores pueden extraerse y cuántos datos de evaluación identifican un polinomio. Para terminar una factorización, necesitamos además justificar la irreducibilidad de los factores que quedan, dentro del conjunto de coeficientes elegido.

### Parámetros que cambian las multiplicidades

Consideremos, para $t\in\mathbb R$,

$$
P_t(x)=x^4-(t+1)x^2+t=(x^2-1)(x^2-t).
$$

La identidad se comprueba multiplicando. Determinemos todas sus raíces reales, sus multiplicidades y una descomposición en irreducibles reales.

| Parámetro | Raíces reales y multiplicidades | Factores irreducibles reales |
|---|---|---|
| $t<0$ | $1,-1$, simples | $(x-1)(x+1)(x^2-t)$ |
| $t=0$ | $1,-1$, simples; $0$, doble | $(x-1)(x+1)x^2$ |
| $t>0$, $t\ne1$ | $1,-1,\sqrt t,-\sqrt t$, simples | $(x-1)(x+1)(x-\sqrt t)(x+\sqrt t)$ |
| $t=1$ | $1,-1$, dobles | $(x-1)^2(x+1)^2$ |

En la segunda fila, $x^2$ representa dos copias del irreducible lineal $x$. En las otras filas, las potencias también indican repeticiones de factores, no nuevos números.

Si $t<0$, el residual $x^2-t$ es positivo y su discriminante $4t$ es negativo; por tanto, es irreducible real y no agrega raíces. En $t=0$, el residual aporta dos copias de $x$ y no se anula en $1,-1$. Si $t>0$ y $t\ne1$, los cuatro números son distintos, y cada factor lineal aparece una vez. Para $t=1$, los dos factores cuadráticos coinciden y sus contribuciones a las multiplicidades se suman. Estos argumentos justifican tanto los ceros como sus multiplicidades exactas y la exhaustividad.

Si $t\in\mathbb Q$, el polinomio también pertenece a $\mathbb Q[x]$. El factor $x^2-t$ se descompone en factores lineales racionales si y solo si $t$ es el cuadrado de un racional, incluyendo $t=0$; en cualquier otro caso es irreducible racional por el criterio cuadrático. Así, para $t=2$, la descomposición racional es $(x-1)(x+1)(x^2-2)$, mientras que la real añade los factores $x-\sqrt2$ y $x+\sqrt2$.

### Construcción, unicidad y comprobación por puntos

Busquemos un polinomio de grado cuatro, coeficiente principal $2$, raíz doble en $1$, raíz simple en $-2$ y valor $P(0)=4$. Los factores exigidos forman $H=(x-1)^2(x+2)$, mónico de grado tres. El residual debe ser lineal de coeficiente principal $2$, por lo que $P=H(2x+b)$. Como $H(0)=2$, la condición $2b=4$ da $b=2$. El único candidato es $P(x)=2(x-1)^2(x+2)(x+1).$

El residual al extraer $(x-1)^2$ vale $2(3)(2)=12\ne0$ en $1$; al extraer $x+2$, vale $2(-3)^2(-1)=-18\ne0$ en $-2$. Las multiplicidades pedidas son exactas. También aparece la raíz simple $-1$, que el enunciado no prohibía. El grado, el coeficiente principal y el valor en cero quedan satisfechos.

Podemos certificar una expresión desarrollada sin repetir la multiplicación completa. Sea $Q(x)=2x^4+2x^3-6x^2-2x+4$. En los cinco puntos distintos $-2,-1,0,1,2$, tanto $P$ como $Q$ toman los valores $0,0,4,0,24$, respectivamente. Ambos tienen grado a lo sumo cuatro; [§25.5](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s05) demuestra que son el mismo polinomio. Los factores certifican las multiplicidades, mientras que los cinco valores y la cota de grado certifican la identidad desarrollada.

### Una cuártica sin raíces: cómo examinar factores cuadráticos

El polinomio $V(x)=x^4+1$ es positivo en todos los reales, por lo que no tiene raíces reales ni racionales. Esto descarta factores lineales en ambos dominios, pero todavía debemos examinar factores cuadráticos para decidir su irreducibilidad.

Supongamos una descomposición en $\mathbb Q[x]$ con ambos grados positivos. Al no haber factores lineales, los grados deben ser dos y dos. Como $V$ es mónico, podemos normalizar ambos factores como mónicos sin alterar su producto. Escribimos

$$
x^4+1=(x^2+ux+v)(x^2+wx+z),\qquad u,v,w,z\in\mathbb Q.
$$

Comparar coeficientes da $u+w=0$, $v+z+uw=0$, $uz+vw=0$ y $vz=1$. Sustituimos $w=-u$ y obtenemos

$$
v+z-u^2=0,\qquad u(z-v)=0,\qquad vz=1.
$$

Si $u=0$, entonces $z=-v$ y $vz=-v^2=1$, imposible para racionales. Si $u\ne0$, la segunda igualdad da $z=v$, y la tercera exige $v^2=1$. Para $v=-1$, la primera igualdad daría $u^2=-2$, imposible; para $v=1$, daría $u^2=2$, también imposible en $\mathbb Q$ por [§25.1](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s01). Se han agotado los casos. No existen dos factores cuadráticos racionales, y $x^4+1$ es irreducible sobre $\mathbb Q$.

Sobre $\mathbb R$, la última posibilidad sí puede realizarse:

$$
x^4+1=(x^2+\sqrt2\,x+1)(x^2-\sqrt2\,x+1).
$$

La identidad es $(x^2+1)^2-2x^2=x^4+1$. Cada cuadrática tiene discriminante $-2$ y es irreducible real. Así, la misma cuártica es irreducible racional y reducible real, sin tener raíces reales. La comparación de coeficientes resolvió aquí la posibilidad que la búsqueda de raíces no podía decidir.

**Recuperación resuelta.** Para $W=(x-3)^2(x^2+2)$, ¿qué certificados permiten dar todas las raíces reales y saber que la factorización está terminada sobre $\mathbb R$?

Los dos factores lineales aportan $3$. Después de extraer $(x-3)^2$, el residual vale $11\ne0$ en $3$, de modo que su multiplicidad es dos. El residual $x^2+2$ es positivo y tiene discriminante $-8$; no aporta raíces reales y es irreducible real. Los factores lineales también son irreducibles. Por tanto, $3$ es la única raíz real y la expresión, con las dos copias de $x-3$, es una descomposición en irreducibles.

**Diagnóstico resuelto.** Se sabe que todo polinomio no nulo se descompone en irreducibles y se concluye que todos esos factores tienen que ser lineales. ¿Qué se ha añadido sin justificación?

El teorema de [§25.15](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s15) no fija los grados de los irreducibles. Ya hemos probado que $x^2+1$ es irreducible real y que $x^3-2$ es irreducible racional. La existencia de una descomposición en irreducibles no garantiza una descomposición en factores lineales en el mismo dominio.

Una respuesta completa queda respaldada por las identidades calculadas, las hipótesis de grado y dominio y el criterio aplicado a cada factor residual. Esos certificados permiten distinguir lo demostrado de lo que una búsqueda de candidatos todavía deja abierto.

## Ejercicios y soluciones

Intente cada ejercicio antes de consultar la solución que lo acompaña. En las respuestas que piden todas las raíces, compruebe también qué puede aportar el factor residual.

### A. Lectura y reconocimiento

#### Ejercicio 001. Comprobar candidatos



**Enunciado.** Para $P(x)=x^2-4x+3$, determine cuáles de los números $-1,0,1,3,4$ son raíces. Justifique cada decisión por evaluación.



**Solución.** Evaluamos cada candidato: $P(-1)=1+4+3=8$, $P(0)=3$, $P(1)=1-4+3=0$, $P(3)=9-12+3=0$ y $P(4)=16-16+3=3$. De la lista dada, las raíces son $1$ y $3$; los otros tres números quedan descartados porque sus valores no son cero. Además, $P=(x-1)(x-3)$ confirma las dos anulaciones. Como este producto se anula únicamente cuando uno de sus factores vale cero, también certifica que no hay otras raíces reales.

#### Ejercicio 002. Cero, constante y lineal



**Enunciado.** Describa las raíces en $\mathbb Q$ y en $\mathbb R$ de $P(x)=0$, $Q(x)=-7$ y $R(x)=3x+6$. Indique cuándo corresponde asignar una multiplicidad finita.



**Solución.** Para $P$, cada número del conjunto elegido es raíz, pues todas las evaluaciones son cero. La multiplicidad finita de [§25.6](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s06) no se define para el polinomio cero: cualquier potencia de $x-a$ lo divide y no existe un exponente máximo.

El polinomio $Q$ no tiene raíces en ninguno de los dos conjuntos, porque su evaluación siempre es $-7$. Su multiplicidad en cualquier punto es cero.

Para $R$, resolver $3a+6=0$ da $a=-2$, racional y real. La identidad $R=3(x+2)$ y el residual constante $3\ne0$ demuestran que esa raíz es simple. La ecuación lineal también muestra que no existe otra raíz.

#### Ejercicio 003. Cambiar el conjunto de búsqueda



**Enunciado.** Determine todas las raíces de $P(x)=x^2-5$ en $\mathbb Q$ y en $\mathbb R$.



**Solución.** Una raíz racional de este polinomio mónico entero tendría que ser un entero divisor de $-5$. Los únicos candidatos son $\pm1,\pm5$. Sus valores son $-4$ para $\pm1$ y $20$ para $\pm5$, así que no hay raíces racionales.

En $\mathbb R$, la ecuación $a^2=5$ da $a=\pm\sqrt5$. La identidad $P=(x-\sqrt5)(x+\sqrt5)$ comprueba la factorización real y la exhaustividad: cualquier raíz debe anular uno de los factores. Ambos números son irracionales, de acuerdo con la búsqueda racional anterior.

#### Ejercicio 004. Leer una forma factorizada



**Enunciado.** Sea $P(x)=-2(x+3)^2(x-1)^3(x^2+4)$. Determine su grado, coeficiente principal, todas sus raíces reales y sus multiplicidades. Compare la suma de multiplicidades con el grado.



**Solución.** Los factores tienen grados $2,3,2$; por tanto, el grado total es siete y el coeficiente principal es $-2$. El factor $x^2+4$ es positivo en todos los reales y no aporta raíces.

La raíz $-3$ tiene multiplicidad dos: después de extraer $(x+3)^2$, el residual es $-2(x-1)^3(x^2+4)$, cuyo valor en $-3$ es $-2(-4)^3\cdot13=1664\ne0$. La raíz $1$ tiene multiplicidad tres, pues el residual $-2(x+3)^2(x^2+4)$ vale $-2\cdot16\cdot5=-160\ne0$ allí.

Las únicas raíces reales son, por tanto, $-3$ y $1$. Sus multiplicidades suman $2+3=5$, dos menos que el grado. Esa diferencia corresponde al grado del factor residual $x^2+4$ sin raíces reales.

#### Ejercicio 005. Interpretar un cociente



**Enunciado.** Se conoce la identidad $4x^3+2x^2+3x+5=(x+1)(4x^2-2x+5)$. Determine si $-1$ es raíz y cuál es su multiplicidad. Compruebe también si $1$ es raíz.



**Solución.** La identidad contiene el factor $x+1$, de modo que $-1$ es raíz por el teorema del factor. Para decidir su multiplicidad exacta evaluamos el residual: $4(-1)^2-2(-1)+5=11\ne0$. Por tanto, es una raíz simple.

En $1$, la evaluación del polinomio original da $4+2+3+5=14\ne0$, así que $1$ no es raíz. La factorización también devuelve ese valor: $(1+1)(4-2+5)=2\cdot7=14$.

#### Ejercicio 006. Un candidato que falla



**Enunciado.** Para $P(x)=3x^2+x-2$, compruebe si $1/3$ cumple las restricciones del teorema de raíces racionales y si realmente es raíz.



**Solución.** La fracción $1/3$ está reducida. Su numerador divide al término constante $-2$ y su denominador divide al coeficiente principal $3$, así que pertenece a la lista de candidatos permitidos.

Sin embargo, $P(1/3)=3/9+1/3-2=2/3-2=-4/3\ne0$. No es raíz. Las divisibilidades son condiciones necesarias para una raíz racional; la evaluación decide si un candidato permitido se anula.

#### Ejercicio 007. Cinco anulaciones y grado acotado



**Enunciado.** Un polinomio $P\in\mathbb R[x]$ tiene grado a lo sumo cuatro, admitiendo al polinomio cero, y se anula en cinco números reales distintos. ¿Qué puede concluirse?



**Solución.** Si $P$ fuera no nulo, su grado sería un entero menor o igual que cuatro. La cota de [§25.4](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s04) permitiría a lo sumo cuatro raíces distintas, en contradicción con las cinco dadas. Por tanto, $P$ es el polinomio cero.

Esto no atribuye un grado cuatro al cero. «Grado a lo sumo cuatro» se usa con la convención de [§25.5](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s05), que admite por separado al polinomio cero. Si se hubiera afirmado grado exactamente cuatro, los datos serían incompatibles.

#### Ejercicio 008. Qué falta para una raíz doble



**Enunciado.** Sea $P=(x-2)^2R$, con $R$ no nulo. Decida la multiplicidad de $2$ cuando $R(2)\ne0$ y qué puede afirmarse cuando $R(2)=0$. Dé un ejemplo del segundo caso.



**Solución.** Si $R(2)\ne0$, la caracterización por residual demuestra $\nu_2(P)=2$.

Si $R(2)=0$, el teorema del factor permite escribir $R=(x-2)S$, y $P=(x-2)^3S$. La multiplicidad es al menos tres; podría ser mayor si $S$ vuelve a anularse en $2$. Por ejemplo, $R=x-2$ produce $P=(x-2)^3$, cuya multiplicidad en $2$ es exactamente tres porque el residual final es $1$.

#### Ejercicio 009. Clasificar sin incluir unidades



**Enunciado.** Clasifique $0$, $5$, $x+4$, $(x+4)^2$ y $x^2+4$ como irreducibles, reducibles o fuera de esa clasificación, tanto sobre $\mathbb Q$ como sobre $\mathbb R$.



**Solución.** El cero y la constante $5$ quedan fuera de la clasificación de [§25.13](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s13), que se reserva a polinomios no nulos de grado positivo. La constante $5$ es una unidad.

El lineal $x+4$ es irreducible sobre ambos conjuntos, porque un producto de grado uno debe tener un factor constante. El polinomio $(x+4)^2$ es reducible: presenta dos factores lineales de grado positivo.

Para $x^2+4$, la desigualdad $a^2+4>0$ descarta raíces reales y, en particular, racionales. Como es una cuadrática, el criterio de [§25.14](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s14) demuestra irreducibilidad sobre ambos conjuntos. La presencia de una raíz en $x+4$ no contradice su irreducibilidad lineal.

#### Ejercicio 010. Cuántos puntos identifican



**Enunciado.** Dos polinomios de grado a lo sumo tres coinciden en $0,1,2$. ¿Deben ser iguales? Indique qué cambia si también coinciden en $3$.



**Solución.** Tres puntos no bastan. Por ejemplo, $P=0$ y $Q=x(x-1)(x-2)$ coinciden en $0,1,2$, pero son polinomios diferentes: $Q$ tiene coeficiente principal $1$ y $Q(3)=6$.

Si también coinciden en $3$, tienen cuatro puntos distintos de coincidencia. Aplicar [§25.5](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s05) con $n=3$ demuestra que son iguales. La cota de grado y la cantidad de puntos deben utilizarse juntas.

### B. Técnica y cálculo

#### Ejercicio 011. Horner y una raíz simple



**Enunciado.** Divida $P(x)=2x^3-x^2-7x+2$ por $x-2$, reconstruya la identidad y determine la multiplicidad de $2$.



**Solución.** Horner con $2$ y los coeficientes $2,-1,-7,2$ da: bajamos $2$; luego $-1+2\cdot2=3$; después $-7+2\cdot3=-1$; finalmente $2+2(-1)=0$. El cociente es $2x^2+3x-1$ y el resto es cero.

La identidad es $P=(x-2)(2x^2+3x-1)$. Al multiplicar obtenemos $2x^3+3x^2-x-4x^2-6x+2=2x^3-x^2-7x+2$, lo que verifica el cociente. El residual vale $8+6-1=13\ne0$ en $2$, por lo que esa raíz es simple.

#### Ejercicio 012. Un resto no nulo



**Enunciado.** Divida $P(x)=x^3+2x^2-5x+4$ por $x-1$. Decida si $x-1$ es factor y compruebe la respuesta mediante una identidad.



**Solución.** Horner con $1$ transforma los coeficientes $1,2,-5,4$ en $1,3,-2$ para el cociente y resto $2$. Por tanto, $P(x)=(x-1)(x^2+3x-2)+2.$

El producto es $x^3+2x^2-5x+2$; añadir el resto devuelve el término constante $4$. Como el resto no es cero, $x-1$ no divide a $P$. El mismo número es $P(1)=1+2-5+4=2$, de modo que $1$ tampoco es raíz.

#### Ejercicio 013. Divisiones sucesivas



**Enunciado.** Para $P(x)=x^4-5x^3+9x^2-7x+2$, determine la multiplicidad de $1$ mediante divisiones sucesivas. Obtenga después todas las raíces reales.



**Solución.** Dividimos repetidamente por $x-1$:

| Dividendo | Cociente | Resto |
|---|---|---:|
| $x^4-5x^3+9x^2-7x+2$ | $x^3-4x^2+5x-2$ | $0$ |
| $x^3-4x^2+5x-2$ | $x^2-3x+2$ | $0$ |
| $x^2-3x+2$ | $x-2$ | $0$ |

El residual final $x-2$ vale $-1\ne0$ en $1$. Hemos extraído exactamente tres copias de $x-1$, así que $P=(x-1)^3(x-2)$ y $\nu_1(P)=3$. Multiplicar estos factores devuelve los cinco coeficientes iniciales.

El factor residual aporta la raíz $2$, simple, porque $(2-1)^3=1\ne0$. Cualquier cero del producto debe ser $1$ o $2$, por lo que esta lista de raíces reales es completa.

#### Ejercicio 014. Extraer dos raíces distintas



**Enunciado.** Compruebe que $-1$ y $2$ son raíces de $P(x)=x^3-4x^2+x+6$. Extraiga sus factores sucesivamente y determine todas las raíces reales.



**Solución.** Las evaluaciones dan $P(-1)=-1-4-1+6=0$ y $P(2)=8-16+2+6=0$. Dividir por $x+1$ produce el cociente $x^2-5x+6$ y resto cero. Este cociente se anula en $2$: $4-10+6=0$. Al dividirlo por $x-2$, queda $x-3$.

Por tanto, $P=(x+1)(x-2)(x-3)$. La multiplicación de $(x-2)(x-3)=x^2-5x+6$ por $x+1$ reconstruye $x^3-4x^2+x+6$. Las únicas raíces son $-1,2,3$, todas simples porque los tres factores lineales corresponden a puntos distintos.

#### Ejercicio 015. Lista racional y reducción del grado



**Enunciado.** Determine todos los candidatos racionales de $P(x)=2x^3+3x^2-8x-12$ y encuentre todas sus raíces racionales mediante una factorización comprobada.



**Solución.** El numerador debe dividir a $-12$ y el denominador positivo a $2$. Después de reducir y eliminar duplicados, los candidatos son

$$
\pm1,\ \pm2,\ \pm3,\ \pm4,\ \pm6,\ \pm12,\ \pm\frac12,\ \pm\frac32.
$$

Probamos $-3/2$: los términos cúbico y cuadrático son $-27/4$ y $27/4$, mientras que los dos restantes son $12$ y $-12$. La suma es cero. Horner con $-3/2$ produce el cociente $2x^2-8$ y resto cero. Así,

$$
P(x)=(x+3/2)(2x^2-8)=(2x+3)(x-2)(x+2).
$$

El producto reconstruye $2x^3+3x^2-8x-12$. Sus únicas raíces son $-3/2,2,-2$, racionales y simples. La identidad determina todos los ceros, de modo que no es necesario evaluar los demás candidatos.

#### Ejercicio 016. Extraer cero antes de buscar



**Enunciado.** Determine todas las raíces reales y sus multiplicidades de $P(x)=\frac32x^5-\frac92x^4+3x^3$.



**Solución.** El menor exponente con coeficiente no nulo es tres. Extraemos esa potencia y la constante:

$$
P(x)=\frac32x^3(x^2-3x+2)=\frac32x^3(x-1)(x-2).
$$

El residual en cero es $(3/2)(-1)(-2)=3\ne0$, por lo que $0$ tiene multiplicidad tres. Los factores restantes dan las raíces simples $1$ y $2$: sus residuales son no nulos en los respectivos puntos, al ser distintos de cero y entre sí.

El desarrollo da $(3/2)x^5-(9/2)x^4+3x^3$, que verifica la identidad. No hay otras raíces reales porque todos los factores restantes son lineales. La suma $3+1+1=5$ coincide con el grado.

#### Ejercicio 017. Eliminar denominadores



**Enunciado.** Encuentre todas las raíces racionales de $A(x)=\frac13x^3+\frac12x^2-\frac13x-\frac12$ y escriba una factorización del polinomio original.



**Solución.** Multiplicamos por seis para obtener coeficientes enteros: $6A=2x^3+3x^2-2x-3$. Agrupamos $x^2(2x+3)-(2x+3)$ y obtenemos $(2x+3)(x^2-1)$. Recuperar el polinomio original exige dividir por seis: $A(x)=\frac16(2x+3)(x-1)(x+1).$

Las raíces son $-3/2,1,-1$, todas racionales. La identidad descarta otras raíces reales y racionales. Al multiplicar los factores y la constante $1/6$ se recuperan los coeficientes iniciales; por ejemplo, en cero dan $(1/6)\cdot3\cdot(-1)\cdot1=-1/2$, el valor correcto de $A(0)$. Multiplicar para preparar la búsqueda conservó las raíces, pero no los valores del polinomio.

#### Ejercicio 018. Una cuadrática en dos dominios



**Enunciado.** Factorice $P(x)=3x^2-6x-6$ en irreducibles sobre $\mathbb Q$ y sobre $\mathbb R$. Determine sus raíces reales y multiplicidades.



**Solución.** Retiramos la constante: $P=3(x^2-2x-2)$. El factor mónico entero tiene candidatos racionales $\pm1,\pm2$. Sus valores en $1,-1,2,-2$ son $-3,1,-2,6$, respectivamente. No hay raíces racionales; al ser cuadrático, $x^2-2x-2$ es irreducible sobre $\mathbb Q$. Esta es la factorización racional normalizada, con constante $3$.

Completar el cuadrado da $x^2-2x-2=(x-1)^2-3$. En $\mathbb R$, $P(x)=3(x-1-\sqrt3)(x-1+\sqrt3).$

Las raíces son $1+\sqrt3$ y $1-\sqrt3$, distintas y simples. El producto reproduce $3[(x-1)^2-3]$, y cada residual lineal es no nulo en la raíz del otro factor. Los factores lineales reales son irreducibles.

#### Ejercicio 019. Discriminante cero o negativo



**Enunciado.** Para $P(x)=4x^2+12x+9$ y $Q(x)=2x^2-4x+7$, determine las raíces reales con multiplicidad y decida reducibilidad o irreducibilidad sobre $\mathbb Q$ y sobre $\mathbb R$.



**Solución.** Para $P$, el discriminante es $12^2-4\cdot4\cdot9=0$, y $P=(2x+3)^2=4(x+3/2)^2$. Su única raíz real y racional es $-3/2$, doble, pues el residual después de dos extracciones es $4\ne0$. Es reducible sobre ambos conjuntos.

Para $Q$, el discriminante es $(-4)^2-4\cdot2\cdot7=-40<0$. También podemos escribir $Q=2(x-1)^2+5>0$ para todo real. No tiene raíces reales ni racionales; el criterio de grado dos demuestra irreducibilidad sobre $\mathbb R$ y sobre $\mathbb Q$. La constante $2$ no afecta esa conclusión.

#### Ejercicio 020. Agrupar antes de evaluar



**Enunciado.** Factorice $P(x)=2x^3-x^2-18x+9$ y determine todas sus raíces reales.



**Solución.** Los dos primeros términos contienen $x^2$ y los dos últimos contienen $-9$. Por agrupación,

$$
P(x)=x^2(2x-1)-9(2x-1)=(2x-1)(x^2-9)=(2x-1)(x-3)(x+3).
$$

La reconstrucción da $2x^3-x^2-18x+9$. Las raíces son $1/2,3,-3$ y no hay otras, porque cualquier cero del producto debe anular uno de los tres factores lineales. Son simples al corresponder a tres puntos distintos; todos los factores residuales en cada raíz son no nulos.

#### Ejercicio 021. Sustitución y dominio de factores



**Enunciado.** Factorice $P(x)=x^4-7x^2+12$ en irreducibles sobre $\mathbb Q$ y sobre $\mathbb R$. Dé todas sus raíces reales.



**Solución.** La sustitución $y=x^2$ transforma la expresión en $y^2-7y+12=(y-3)(y-4)$. Volver a $x$ da $P=(x^2-3)(x^2-4)$.

Sobre $\mathbb Q$, $x^2-3$ es irreducible: sus candidatos racionales, al ser mónico entero, son $\pm1,\pm3$, con valores $-2$ y $6$, ninguno cero. El segundo factor es $(x-2)(x+2)$. La descomposición racional es $(x^2-3)(x-2)(x+2)$.

Sobre $\mathbb R$ se obtiene $(x-\sqrt3)(x+\sqrt3)(x-2)(x+2)$. Las raíces reales son $\pm\sqrt3,\pm2$, distintas y simples. La multiplicación de los dos factores cuadráticos devuelve $x^4-7x^2+12$ y certifica la identidad.

#### Ejercicio 022. Factorizar sin raíces reales



**Enunciado.** Descomponga $P(x)=x^4+5x^2+4$ en irreducibles sobre $\mathbb Q$ y sobre $\mathbb R$, y determine sus raíces reales.



**Solución.** Tratamos la expresión como una cuadrática en $x^2$: $y^2+5y+4=(y+1)(y+4)$. Así, $P=(x^2+1)(x^2+4)$, cuya multiplicación devuelve la expresión inicial.

Ambos factores son cuadráticos positivos para todo real y tienen discriminantes negativos, $-4$ y $-16$. Son irreducibles sobre $\mathbb R$ y también sobre $\mathbb Q$. Por tanto, la misma expresión es una descomposición en irreducibles en ambos dominios.

El polinomio no tiene raíces reales: el producto de dos números positivos es positivo. Aun sin raíces reales, es reducible porque los dos factores tienen grado positivo.

#### Ejercicio 023. Construcción con coeficiente principal



**Enunciado.** Construya el polinomio de grado tres y coeficiente principal $-4$ que tiene raíz simple en $0$ y raíz doble en $-1$. Compruebe las multiplicidades y calcule $P(2)$.



**Solución.** Los factores exigidos forman el polinomio mónico $H=x(x+1)^2$, de grado tres. Como el grado pedido ya coincide con el de $H$, el residual debe ser constante. El coeficiente principal lo fija en $-4$. Por tanto, el único candidato es $P=-4x(x+1)^2=-4x^3-8x^2-4x$.

En cero, el residual tras extraer $x$ vale $-4(0+1)^2=-4\ne0$; la raíz es simple. En $-1$, después de extraer $(x+1)^2$, el residual $-4x$ vale $4\ne0$; la raíz es doble. Finalmente, $P(2)=-4\cdot2\cdot3^2=-72$. El grado y el coeficiente principal también se leen en la forma desarrollada.

#### Ejercicio 024. Construcción con un valor



**Enunciado.** Construya un polinomio de grado tres con raíz simple en $1$, raíz doble en $-2$ y valor $P(0)=-12$. Justifique la unicidad y las multiplicidades exactas.



**Solución.** La suma de multiplicidades pedidas es tres, igual al grado. Todo candidato debe ser $P=c(x-1)(x+2)^2$, con $c\ne0$. Evaluar en cero da $-4c=-12$, así que $c=3$, que fija un único candidato: $P(x)=3(x-1)(x+2)^2=3x^3+9x^2-12.$

En $1$, el residual después de extraer $x-1$ vale $3(1+2)^2=27\ne0$, y la raíz es simple. En $-2$, el residual tras extraer $(x+2)^2$ es $3(x-1)$ y vale $-9\ne0$, así que la multiplicidad es dos. El desarrollo confirma el grado y $P(0)=-12$.

#### Ejercicio 025. Interpolar tres datos



**Enunciado.** Encuentre el polinomio de grado a lo sumo dos que satisface $P(-1)=4$, $P(0)=1$ y $P(1)=0$. Justifique que es único y determine sus raíces reales.



**Solución.** Escribimos $P=ax^2+bx+c$, permitiendo que alguno de los coeficientes iniciales sea cero. El dato en cero da $c=1$. Los otros dos datos se convierten en $a-b=3$ y $a+b=-1$. Sumarlos da $2a=2$, por lo que $a=1$; entonces $b=-2$. Así, $P=x^2-2x+1=(x-1)^2$.

Evaluar en $-1,0,1$ devuelve $4,1,0$, de modo que el candidato satisface todos los datos. La identificación de [§25.5](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s05) prueba unicidad porque son tres puntos distintos y el grado está acotado por dos. La única raíz real es $1$, doble, pues el residual de $(x-1)^2$ es $1$.

#### Ejercicio 026. Normalizar factores irreducibles



**Enunciado.** Para $P(x)=(2x-2)(3x+3)(x^2+2)$, separe el coeficiente principal y escriba factores mónicos irreducibles sobre $\mathbb Q$ y sobre $\mathbb R$. Determine todas sus raíces reales y sus multiplicidades.



**Solución.** Retiramos las constantes de los factores lineales: $2x-2=2(x-1)$ y $3x+3=3(x+1)$. Por tanto, $P(x)=6(x-1)(x+1)(x^2+2)=6x^4+6x^2-12.$

El coeficiente principal separado es $6$. Los factores $x-1$ y $x+1$ son mónicos e irreducibles lineales en ambos conjuntos. El factor $x^2+2$ es mónico, positivo en todos los reales y tiene discriminante $-8$; es irreducible real y racional.

Las únicas raíces reales son $1$ y $-1$. En $1$, el residual $6(x+1)(x^2+2)$ vale $36\ne0$; en $-1$, el residual $6(x-1)(x^2+2)$ vale $-36\ne0$. Ambas raíces son simples. El producto desarrollado comprueba la normalización y muestra que no se perdió el coeficiente principal.

### C. Demostraciones

#### Ejercicio 027. Un factor común a partir de valores



**Enunciado.** Sean $P,Q\in K[x]$, con $K=\mathbb Q$ o $\mathbb R$, y $a_1,\ldots,a_r$ distintos. Prueba que si $P(a_i)=Q(a_i)$ para todo $i$, entonces $\prod_{i=1}^r(x-a_i)$ divide a $P-Q$. Incluye el caso $P=Q$.



**Solución.** Escribimos $R=P-Q$. Si $R=0$, cualquier polinomio divide a $R$, pues $0=H\cdot0$. Si $R\ne0$, cada $a_i$ es raíz de $R$. Extraemos $x-a_1$ por el teorema del factor: $R=(x-a_1)R_1$. Para $i>1$, $0=(a_i-a_1)R_1(a_i)$, y $a_i-a_1\ne0$ permite concluir $R_1(a_i)=0$. Repetimos sobre el cociente con las raíces restantes. Tras $r$ pasos obtenemos $R=\prod_i(x-a_i)S$. La distinción de los puntos justifica cada cancelación. Si $r=0$, el producto vacío es $1$ y la afirmación sigue siendo válida.

#### Ejercicio 028. La cota con multiplicidades



**Enunciado.** Sean $P\ne0$ en $K[x]$ y $a_1,\ldots,a_r$ raíces distintas, de multiplicidades $m_1,\ldots,m_r$. Prueba que $\sum_i m_i\le\deg P$ sin suponer que $P$ se descompone completamente en factores lineales.



**Solución.** Si la lista de raíces es vacía, la suma es cero y la desigualdad se cumple porque $P$ es no nulo y $\deg P\ge0$. Para una lista no vacía, extraemos $(x-a_1)^{m_1}$ y obtenemos un cociente no nulo. Para $i>1$, el factor extraído tiene multiplicidad cero en $a_i$, pues allí vale $(a_i-a_1)^{m_1}\ne0$. La aditividad de multiplicidad de [§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07) muestra que el cociente conserva multiplicidad $m_i$ en $a_i$. Repetimos con las restantes raíces y obtenemos $P=\prod_i(x-a_i)^{m_i}S$, con $S\ne0$. Por aditividad del grado, $\deg P=\sum_i m_i+\deg S\ge\sum_i m_i$. El residual puede tener grado positivo y carecer de raíces en $K$; no fue necesario eliminarlo.

#### Ejercicio 029. Multiplicidad de una suma



**Enunciado.** Sean $P,Q,P+Q$ no nulos en $K[x]$. Demuestra que $\nu_a(P+Q)\ge\min\{\nu_a(P),\nu_a(Q)\}$ y que hay igualdad si las dos multiplicidades son distintas. Da un ejemplo de desigualdad estricta cuando son iguales.



**Solución.** Sean $m=\nu_a(P)$ y $n=\nu_a(Q)$; intercambiando los nombres podemos suponer $m\le n$. Escribimos $P=(x-a)^mU$, $Q=(x-a)^nV$, con $U(a),V(a)\ne0$. Entonces $P+Q=(x-a)^m[U+(x-a)^{n-m}V]$, lo que da la cota porque la suma es no nula. Si $m<n$, el corchete vale $U(a)\ne0$, así que su multiplicidad es cero y la de la suma es $m$. Si $m=n$, los valores residuales pueden cancelarse. Por ejemplo, en $a=0$, $P=x$ y $Q=-x+x^2$ tienen multiplicidad $1$, pero $P+Q=x^2$ tiene multiplicidad $2$. Se excluye la suma cero para no atribuirle una multiplicidad finita.

#### Ejercicio 030. Escala y multiplicidad



**Enunciado.** Prueba que para $c\in K$, $c\ne0$, y $P\ne0$, los polinomios $P$ y $cP$ tienen las mismas raíces y multiplicidades. Explica qué parte cambia al comparar sus valores.



**Solución.** Para cada $a\in K$, $(cP)(a)=cP(a)$; al ser $c\ne0$, uno de estos valores es cero si y solo si el otro lo es. Si $P=(x-a)^mU$ con $U(a)\ne0$, entonces $cP=(x-a)^m(cU)$ y $(cU)(a)\ne0$. Por la definición de multiplicidad, $\nu_a(cP)=m$. Esto también cubre $m=0$, es decir, un punto que no es raíz. Los valores no nulos se multiplican por $c$; no se conservan en general. Por ejemplo, $P=x+1$, $c=2$ dan $P(0)=1$ y $(cP)(0)=2$.

#### Ejercicio 031. Trasladar las raíces



**Enunciado.** Sea $b\in K$ y $P\ne0$. Define $T(x)=P(x+b)$. Prueba que $a$ es raíz de $P$ de multiplicidad $m$ si y solo si $a-b$ es raíz de $T$ de multiplicidad $m$.



**Solución.** Si $P(x)=(x-a)^mU(x)$ y $U(a)\ne0$, al sustituir $x+b$ obtenemos $T(x)=(x-(a-b))^mU(x+b)$. El residual en $a-b$ vale $U(a)\ne0$, así que la multiplicidad es exactamente $m$. El polinomio trasladado es no nulo: la sustitución inversa $x-b$ devuelve $P$ (también conserva el coeficiente principal y el grado). Para la implicación recíproca aplicamos el mismo argumento a $T(x-b)=P(x)$. Las raíces se trasladan por $-b$, no por $b$.

#### Ejercicio 032. Unicidad de una construcción mínima



**Enunciado.** Sean $a_i\in K$ distintos y $m_i\ge1$. Pon $M=\sum_i m_i$ y $c\ne0$. Prueba que hay un único polinomio de grado $M$, coeficiente principal $c$, y multiplicidad al menos $m_i$ en cada $a_i$. Decide si las multiplicidades pueden ser mayores.



**Solución.** El polinomio $H=c\prod_i(x-a_i)^{m_i}$ cumple las condiciones: tiene grado $M$ y coeficiente principal $c$. Su residual en $a_i$ es $c\prod_{j\ne i}(a_i-a_j)^{m_j}\ne0$, luego sus multiplicidades son exactamente las prescritas. Si $P$ es otro candidato, la extracción sucesiva de [§25.7](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s07) da $P=\prod_i(x-a_i)^{m_i}S$. Como $\deg P=M$, $S$ es constante; la condición del coeficiente principal obliga a $S=c$. Por tanto $P=H$. Una multiplicidad mayor haría que la suma excediera el grado $M$, contradiciendo la cota. Para una lista vacía, $M=0$ y la única solución es la constante $c$.

#### Ejercicio 033. De raíz racional a raíz entera



**Enunciado.** Prueba que toda raíz racional de un polinomio mónico no constante de $\mathbb Z[x]$ es entera. Explica por qué no basta que el polinomio tenga coeficientes racionales.



**Solución.** Sea la raíz $p/q$ escrita en forma reducida, con $q>0$. Por el teorema de las raíces racionales, $q$ divide al coeficiente principal, que es $1$. Por tanto $q=1$ y la raíz es el entero $p$. Si el término independiente es cero, podemos extraer primero la potencia de $x$; la raíz cero es entera y el residual sigue siendo mónico con coeficientes enteros, por lo que el argumento se aplica a las otras raíces. La integridad de los coeficientes es esencial: el polinomio mónico $x-\tfrac12$ pertenece a $\mathbb Q[x]$ y tiene la raíz no entera $\tfrac12$.

#### Ejercicio 034. Un cúbico y el dominio



**Enunciado.** Sea $P\in K[x]$ de grado $3$. Prueba que $P$ es reducible en $K[x]$ si y solo si tiene una raíz en $K$. Identifica los dos usos del grado.



**Solución.** Si $a\in K$ es raíz, el teorema del factor da $P=(x-a)Q$, con $\deg Q=2$; ambos factores tienen grado positivo y esto es una factorización no trivial. Recíprocamente, si $P=AB$ con $\deg A,\deg B\ge1$, la suma de sus grados es $3$. Los únicos pares posibles son $(1,2)$ y $(2,1)$. Uno de los factores es $ux+v$, con $u\ne0$, y se anula en $-v/u\in K$, donde también se anula $P$. El grado asegura primero que el cociente no es una unidad y después que una factorización no trivial contiene un lineal. No justifica el mismo criterio en grado cuatro.

#### Ejercicio 035. Un irreducible que divide un producto



**Enunciado.** Sea $p\in K[x]$ irreducible y supón que $p\mid AB$. Prueba que $p\mid A$ o $p\mid B$ usando Bézout, sin dar por supuesta la factorización única.



**Solución.** Si $p\mid A$, ya terminamos. En caso contrario, todo divisor común no constante de $p$ y $A$ sería asociado a $p$: al dividir a $p$, la irreducibilidad obliga a que su cofactor sea una unidad. Esto implicaría $p\mid A$, contradicción. Así, el máximo común divisor mónico de $p$ y $A$ es $1$. Por Bézout de C24 existen $U,V\in K[x]$ tales que $Up+VA=1$. Multiplicando por $B$, obtenemos $B=UpB+VAB$. Los dos sumandos son divisibles por $p$, el segundo por la hipótesis, por lo que $p\mid B$. Si $A=0$, se cae en el primer caso; si $B=0$, la conclusión también es inmediata.

#### Ejercicio 036. Conservar irreducibilidad al trasladar



**Enunciado.** Para $b\in K$ y $P$ no constante, demuestra que $P(x)$ es irreducible en $K[x]$ si y solo si $P(x+b)$ lo es.



**Solución.** La sustitución $\tau_b:F(x)\mapsto F(x+b)$ conserva sumas, productos y el grado de todo polinomio no nulo: el término principal $cx^d$ se transforma en $c(x+b)^d$, cuyo coeficiente de $x^d$ sigue siendo $c$, y los otros términos tienen grado menor. Su inversa es $\tau_{-b}$. Si $P=AB$ con ambos factores de grado positivo, entonces $\tau_b(P)=\tau_b(A)\tau_b(B)$ es una factorización no trivial. Si $\tau_b(P)=CD$ con grados positivos, al aplicar $\tau_{-b}$ obtenemos $P=C(x-b)D(x-b)$, también no trivial. La equivalencia de reducibilidad, negada para polinomios no constantes, da la de irreducibilidad.

#### Ejercicio 037. Raíces de un producto y de una potencia



**Enunciado.** Sean $P,Q\ne0$ en $K[x]$ y $k\ge1$ entero. Prueba que las raíces de $PQ$ son la unión de las de $P$ y $Q$, y que $\nu_a(P^k)=k\nu_a(P)$.



**Solución.** Para $a\in K$, $(PQ)(a)=P(a)Q(a)$. Como $K$ es un cuerpo, un producto de escalares es cero si y solo si uno de ellos lo es; esto prueba la igualdad de conjuntos de raíces. Sea $m=\nu_a(P)$ y escribamos $P=(x-a)^mU$, con $U(a)\ne0$. Entonces $P^k=(x-a)^{km}U^k$ y $U(a)^k\ne0$, por lo que la multiplicidad es $km$. Se incluyen los puntos que no son raíces mediante $m=0$. La primera afirmación habla de conjuntos y la segunda de multiplicidades: repetir un factor no añade una raíz distinta.

#### Ejercicio 038. Interpolar sin perder el grado



**Enunciado.** Sean $a_0,\ldots,a_n\in K$ distintos y $y_0,\ldots,y_n\in K$. Prueba existencia y unicidad de un polinomio $P$ de grado a lo sumo $n$ con $P(a_i)=y_i$. Incluye $n=0$ y los datos todos nulos.



**Solución.** Para cada $i$ definimos $L_i(x)=\prod_{j\ne i}(x-a_j)/(a_i-a_j)$; los denominadores son no nulos. Tiene grado a lo sumo $n$ y satisface $L_i(a_k)=0$ si $k\ne i$, mientras que $L_i(a_i)=1$. Por tanto $P=\sum_{i=0}^n y_iL_i$ tiene grado a lo sumo $n$ (o es cero) y cumple todos los datos. Si $Q$ es otra solución, $P-Q$ es cero o tiene grado a lo sumo $n$ y $n+1$ raíces distintas. La cota de raíces excluye el segundo caso; así $P=Q$. Para $n=0$, el producto vacío da $L_0=1$ y $P=y_0$. Si todos los datos son cero, la construcción y la unicidad dan el polinomio cero, sin asignarle un grado ordinario.

### D. Diagnóstico y reparación

#### Ejercicio 039. Tres puntos no siempre bastan



**Enunciado.** Un estudiante dice: «Dos polinomios de grado a lo sumo $3$ coinciden en $0,1,2$; por tanto son iguales». Localiza el fallo, da un contraejemplo y repara el criterio.



**Solución.** La diferencia puede tener grado $3$ y tres raíces distintas sin ser cero. Tomamos $P=0$ y $Q=x(x-1)(x-2)=x^3-3x^2+2x$. Coinciden en los tres puntos, pero $Q(3)=6\ne0=P(3)$. La condición de grado a lo sumo $3$ permite el polinomio cero; no se usa su grado como un número. La reparación consiste en pedir coincidencia en cuatro puntos distintos: una diferencia no nula de grado a lo sumo $3$ no puede tener cuatro raíces. Alternativamente, con solo esos tres puntos se puede bajar la cota de grado a $2$.

#### Ejercicio 040. Cancelar en una raíz repetida



**Enunciado.** Al partir de $P(a)=0$ y $P=(x-a)Q$, alguien escribe $0=(a-a)Q(a)$ y concluye $Q(a)=0$. Explica el error y la condición correcta para una raíz de multiplicidad al menos dos.



**Solución.** La igualdad obtenida es $0=0\cdot Q(a)$ y no permite cancelar el factor cero. Por ejemplo, $P=x-2$, $a=2$ y $Q=1$ satisfacen la igualdad, pero $Q(2)=1$. La condición correcta es $Q(a)=0$, que debe verificarse por separado. Por el teorema del factor equivale a $Q=(x-a)R$ y, por tanto, a $(x-a)^2\mid P$. Para multiplicidad exactamente dos hay que exigir además $R(a)\ne0$; si $R(a)=0$, puede extraerse otra copia y la multiplicidad es mayor. Se presupone $P\ne0$ para hablar de multiplicidad finita.

#### Ejercicio 041. Una lista de candidatos no es una lista de raíces



**Enunciado.** Para $P=2x^3+x+3$, un informe llama raíces a todos los números $\pm1,\pm3,\pm\tfrac12,\pm\tfrac32$. Corrige el informe y determina las raíces racionales.



**Solución.** El teorema de las raíces racionales solo da candidatos: numeradores divisores de $3$ y denominadores positivos divisores de $2$. Evaluarlos o extraer un factor es indispensable. Como $P(-1)=0$, dividimos y obtenemos $P=(x+1)(2x^2-2x+3)$; la expansión recupera $2x^3+x+3$. El discriminante del cuadrático es $(-2)^2-4\cdot2\cdot3=-20<0$, así que no tiene raíces reales y, en particular, tampoco racionales. La única raíz racional es $-1$, simple porque el residual en ella vale $7\ne0$. La lista inicial es exhaustiva para candidatos, no para raíces verdaderas.

#### Ejercicio 042. Cambiar el cuerpo cambia la conclusión



**Enunciado.** Se afirma: «$x^2-2$ no tiene raíces racionales, luego no puede factorizarse con coeficientes reales». Diagnostica la inferencia y clasifica el polinomio en $\mathbb Q[x]$ y $\mathbb R[x]$.



**Solución.** La premisa se refiere a $\mathbb Q$ y no excluye raíces en un conjunto mayor. Si una raíz racional se escribe $p/q$ reducida con $q>0$, el carácter mónico exige $q=1$, y la raíz entera tendría que dividir $-2$. Los candidatos $\pm1,\pm2$ no se anulan. Por el criterio de grado dos, $x^2-2$ es irreducible en $\mathbb Q[x]$. En $\mathbb R[x]$ tenemos $x^2-2=(x-\sqrt2)(x+\sqrt2)$, una factorización no trivial. Las raíces son distintas, y los dos factores lineales son irreducibles reales. La reparación es indicar el cuerpo en la conclusión: sin raíces racionales implica irreducibilidad racional aquí, por el grado dos.

#### Ejercicio 043. El criterio de raíces en grado cuatro



**Enunciado.** Un alumno prueba $x^4+6x^2+8>0$ para todo $x\in\mathbb R$ y concluye irreducibilidad en $\mathbb R[x]$. Conserva la afirmación válida y corrige la conclusión.



**Solución.** La positividad es válida: $x^4\ge0$, $6x^2\ge0$ y el término constante es $8>0$, así que no hay raíces reales ni factores lineales reales. Pero $x^4+6x^2+8=(x^2+2)(x^2+4)$, como comprueba el producto: $x^4+(2+4)x^2+8$. Ambos factores tienen grado dos, de modo que el polinomio es reducible en $\mathbb R[x]$ y también en $\mathbb Q[x]$. Cada cuadrático es irreducible en ambos cuerpos, pues es positivo en $\mathbb R$ y el criterio de grado dos se aplica. La equivalencia entre no tener raíces e irreducibilidad exige grado dos o tres; no se extiende automáticamente a grado cuatro.

#### Ejercicio 044. Unidades que no cuentan como reducción



**Enunciado.** Se propone que $3x+1$ es reducible en $\mathbb Q[x]$ porque $3x+1=3(x+\tfrac13)$, y que $5$ es irreducible porque no tiene raíces. Repara ambas clasificaciones según la convención del capítulo.



**Solución.** Una factorización que demuestra reducibilidad requiere dos factores de grado positivo. El $3$ es una unidad en $\mathbb Q[x]$, con inversa $1/3$; por tanto la igualdad dada solo cambia la normalización. El polinomio lineal $3x+1$ es irreducible: si fuera producto de dos factores de grado positivo, su grado sería al menos dos. La constante $5$ también es unidad, con inversa $1/5$, y por la convención del capítulo no es ni reducible ni irreducible. No tener raíces no clasifica por sí solo a una unidad. El polinomio cero tampoco pertenece a esas dos clases y sí se anula en todo punto.

#### Ejercicio 045. Contar multiplicidades sin perder raíces



**Enunciado.** Para $P=(x-1)^2(x+2)^3(x^2+1)$, un registro declara siete raíces reales distintas y multiplicidad $5$ en $1$. Corrige todas las cantidades y explica cómo se obtienen.



**Solución.** El grado es $2+3+2=7$, pero ese número no cuenta raíces reales distintas. El residual cuadrático $x^2+1$ es positivo en $\mathbb R$ y no aporta raíces reales. Las únicas son $1$ y $-2$. En $1$, el residual $(x+2)^3(x^2+1)$ vale $3^3\cdot2=54\ne0$, así que la multiplicidad es $2$. En $-2$, el residual $(x-1)^2(x^2+1)$ vale $9\cdot5=45\ne0$, así que la multiplicidad es $3$. Hay dos raíces reales distintas y suma de multiplicidades $5\le7$. El $5$ suma multiplicidades en puntos distintos, no la multiplicidad de una raíz individual; no es preciso introducir otras clases de números para explicar el residual.

#### Ejercicio 046. Extraer cero antes del término independiente



**Enunciado.** Para $P=3x^4-6x^3=3x^3(x-2)$, se escribe: «El término independiente es cero; todos los racionales son candidatos y no se puede completar la búsqueda». Corrige el procedimiento y da multiplicidades.



**Solución.** El término independiente nulo indica que debe extraerse primero la potencia de $x$. Aquí la extracción ya está hecha: $P=x^3(3x-6)$. El residual tiene valor $-6\ne0$ en cero, así que $0$ tiene multiplicidad exactamente $3$. Las otras raíces deben anular $3x-6$, cuya única raíz es $2$. Allí $3x^3$ vale $24\ne0$, por lo que la raíz es simple. La lista completa de raíces racionales y reales es $\{0,2\}$. Para un residual de mayor grado y término independiente no nulo, se aplica entonces el teorema de las raíces racionales a sus coeficientes enteros; no se intenta crear una lista finita usando divisores de cero.

#### Ejercicio 047. Un coeficiente principal omitido



**Enunciado.** Un registro sustituye $P=6x^2-6$ por $Q=(x-1)(x+1)$ y declara tanto «mismas raíces» como «mismos valores». Decide qué se conserva y repara la factorización normalizada.



**Solución.** Al expandir, $Q=x^2-1$ y $P=6Q$. Como $6\ne0$, los dos polinomios tienen las mismas raíces $1,-1$, ambas simples. No tienen los mismos valores: $P(0)=-6$, mientras que $Q(0)=-1$. La factorización exacta es $P=6(x-1)(x+1)$; el escalar $6$ conserva el coeficiente principal original, mientras que los factores irreducibles lineales están normalizados como mónicos. Quitar una unidad no altera raíces, multiplicidades o reducibilidad, pero sí la identidad del polinomio y cualquier dato de valor no nulo.

#### Ejercicio 048. Aplicar la cota al polinomio cero



**Enunciado.** Se deduce: «El polinomio cero tiene infinitas raíces; esto contradice que un polinomio tiene a lo sumo tantas raíces como su grado». Identifica la hipótesis omitida y da una formulación válida para un polinomio de grado a lo sumo $n$ que se anula en $n+1$ puntos distintos.



**Solución.** La cota exige que el polinomio sea no nulo; el polinomio cero no tiene un grado ordinario al que aplicar esa desigualdad. No hay contradicción: se anula en todos los puntos, pero queda fuera de la hipótesis del teorema. La formulación válida es: si $P$ es cero o tiene grado a lo sumo $n$, con $n\ge0$, y $P(a_i)=0$ en $n+1$ puntos distintos, entonces $P=0$. En efecto, suponer $P\ne0$ permitiría aplicar la cota y daría $n+1\le\deg P\le n$, imposible. Esta prueba no asigna un grado al cero y cubre también $n=0$, donde una constante no nula no puede anularse.

#### Ejercicio 049. Una construcción con grado incorrecto



**Enunciado.** Se busca un polinomio de grado $3$, coeficiente principal $2$, raíz $1$ doble y raíz $-1$ simple. Se propone $P=2(x-1)^2(x+1)(x^2+1)$ para «asegurar que no haya más raíces reales». Diagnostica y repara.



**Solución.** La propuesta tiene grado $2+1+2=5$, no $3$. Aunque $x^2+1$ no aporta raíces reales, sí aumenta el grado. El factor mínimo exigido por las multiplicidades es $(x-1)^2(x+1)$, ya de grado tres, así que el residual debe ser constante y el coeficiente principal lo fija en $2$. La única solución es $H=2(x-1)^2(x+1)=2x^3-2x^2-2x+2$. En $1$, el residual $2(x+1)$ vale $4\ne0$; en $-1$, el residual $2(x-1)^2$ vale $8\ne0$. Las multiplicidades son exactamente dos y uno. Toda raíz real de $H$ anula uno de esos factores, de modo que no hace falta añadir un residual para impedir raíces adicionales.

#### Ejercicio 050. Un parámetro excepcional olvidado



**Enunciado.** Para $P_t=(x^2-1)(x^2-t)$, con $t\in\mathbb R$, un informe dice: «Cuando $t\ge0$, las cuatro raíces reales son siempre distintas y simples». Corrige la afirmación, incluyendo también $t<0$.



**Solución.** Si $t<0$, $x^2-t>0$ en $\mathbb R$, así que solo hay raíces $1,-1$, ambas simples: el otro factor vale $1-t\ne0$ allí. Si $t=0$, $P_0=x^2(x-1)(x+1)$; hay tres raíces distintas, $0$ doble y $\pm1$ simples. Si $t>0$ y $t\ne1$, las raíces $1,-1,\sqrt t,-\sqrt t$ son cuatro puntos distintos y cada lineal aparece una sola vez; por tanto son simples. Si $t=1$, $P_1=(x^2-1)^2=(x-1)^2(x+1)^2$, con solo dos raíces distintas, ambas dobles. La reparación separa la aparición de la raíz cero y la coincidencia de los factores; el grado cuatro se mantiene en todos los casos, pero no obliga a cuatro raíces reales distintas.

### E. Transferencia y elección de estrategia

#### Ejercicio 051. Separar los casos de un parámetro



**Enunciado.** Para $t\in\mathbb R$, clasifica las raíces reales y sus multiplicidades de $P_t=x^2-2tx+1$. Determina cuándo es irreducible en $\mathbb R[x]$. Si $t\in\mathbb Q$, expresa además un criterio de irreducibilidad en $\mathbb Q[x]$.



**Solución.** El discriminante es $4(t^2-1)$. Si $|t|<1$, es negativo: no hay raíces reales y el cuadrático es irreducible real. Si $t=1$, $P_t=(x-1)^2$; si $t=-1$, $P_t=(x+1)^2$: en ambos casos hay una raíz doble y reducibilidad. Si $|t|>1$, hay dos raíces distintas $t\pm\sqrt{t^2-1}$, ambas simples, y la factorización real es el producto de sus dos lineales mónicos. Para $t$ racional, el criterio de grado dos dice que es reducible racional si y solo si una de esas raíces es racional. Esto equivale a que $t^2-1$ sea un cuadrado de un racional: si la raíz $r$ es racional, $(r-t)^2=t^2-1$; si $t^2-1=u^2$ con $u\in\mathbb Q$, $t\pm u$ son raíces racionales. Cuando $t^2-1<0$, no puede ser un cuadrado racional. La igualdad a cero sí cuenta como cuadrado y produce la raíz doble.

#### Ejercicio 052. Reconstruir con un valor y un coeficiente



**Enunciado.** Determina todos los polinomios reales de grado $4$, coeficiente principal $3$, con raíz $-1$ de multiplicidad exactamente dos, raíz $2$ simple y valor $P(0)=8$. Decide si aparecen otras raíces reales.



**Solución.** Las condiciones de divisibilidad dan $P=(x+1)^2(x-2)Q$. Por el grado, $Q$ es lineal; por el coeficiente principal, $Q=3x+b$. Como $(0+1)^2(0-2)=-2$, el dato $P(0)=8$ da $-2b=8$, es decir, $b=-4$. El único candidato es $P=(x+1)^2(x-2)(3x-4)$. En $-1$, el residual vale $(-3)(-7)=21\ne0$, así que la multiplicidad es exactamente dos. En $2$, vale $9\cdot2=18\ne0$, luego es simple. El residual lineal añade la raíz $4/3$, distinta de las anteriores y simple porque $(4/3+1)^2(4/3-2)\ne0$. No hay otras: anular el producto exige anular uno de los factores. Esta verificación de los residuales es necesaria; la divisibilidad inicial solo garantizaba multiplicidades mínimas.

#### Ejercicio 053. Un dato que fija un parámetro



**Enunciado.** Sea $P_t=x^3-3x+t$ con $t\in\mathbb R$. Encuentra el valor de $t$ para el cual $2$ es raíz, y certifica todas las raíces y multiplicidades de ese polinomio.



**Solución.** Evaluar en $2$ da $P_t(2)=8-6+t=2+t$, por lo que la condición equivale a $t=-2$. Dividimos entonces $x^3-3x-2$ por $x-2$ y obtenemos el cociente $x^2+2x+1=(x+1)^2$. Así $P_{-2}=(x-2)(x+1)^2$. La expansión da $x^3-3x-2$, lo que comprueba la identidad. En $2$, el residual $(x+1)^2$ vale $9\ne0$: raíz simple. En $-1$, el residual $x-2$ vale $-3\ne0$: raíz doble. El producto no se anula en ningún otro real; por tanto la lista es completa, y sus multiplicidades suman el grado tres.

#### Ejercicio 054. Una sustitución cúbica útil



**Enunciado.** Factoriza $P=x^6-7x^3-8$ en irreducibles de $\mathbb Q[x]$ y de $\mathbb R[x]$. Determina sus raíces reales sin usar resultados generales sobre polinomios de grado impar.



**Solución.** La forma sugiere $y=x^3$: $y^2-7y-8=(y-8)(y+1)$. Por tanto $P=(x^3-8)(x^3+1)$. Las identidades de cubos dan $P=(x-2)(x^2+2x+4)(x+1)(x^2-x+1)$. Sus cuadráticos tienen discriminantes $4-16=-12$ y $1-4=-3$, respectivamente; son irreducibles reales y también racionales. Los factores lineales son irreducibles en ambos cuerpos, así que esta expresión sirve en $\mathbb Q[x]$ y en $\mathbb R[x]$. Las únicas raíces reales son $2$ y $-1$. En $2$, el residual vale $12\cdot3\cdot3=108\ne0$; en $-1$, vale $(-3)\cdot3\cdot3=-27\ne0$. Ambas son simples. El producto inicial se verifica como $x^6+(1-8)x^3-8$, sin buscar seis raíces ni presuponer que todo factor se vuelve lineal.

#### Ejercicio 055. Comprobar la compatibilidad de datos



**Enunciado.** ¿Existe un polinomio de grado a lo sumo $2$ que satisfaga $P(0)=1$, $P(1)=2$, $P(2)=5$ y $P(3)=11$? Resuelve también el problema si se permite grado a lo sumo $3$.



**Solución.** Los primeros tres datos los satisface $Q=x^2+1$. Es la única solución de grado a lo sumo dos para esos datos: la diferencia de dos soluciones se anularía en tres puntos distintos y, por la cota, sería cero. Pero $Q(3)=10\ne11$, así que los cuatro datos son incompatibles con grado a lo sumo dos. Para grado a lo sumo tres, cualquier solución difiere de $Q$ en un múltiplo de $x(x-1)(x-2)$, por las tres coincidencias. La cota de grado obliga a que el múltiplo sea constante: $P=Q+c\,x(x-1)(x-2)$. En $3$, $11=10+6c$, de donde $c=1/6$. Resulta $P=x^2+1+\tfrac16x(x-1)(x-2)$. Cumple los cuatro valores y es único, pues dos cúbicos que coincidan en cuatro puntos son iguales.

#### Ejercicio 056. Certificar una diferencia entre cuerpos



**Enunciado.** Clasifica $P=x^2-6x+3$ en $\mathbb Q[x]$ y en $\mathbb R[x]$. Da en cada caso una factorización en irreducibles y determina las raíces reales.



**Solución.** El discriminante es $36-12=24$. Las raíces reales son $3\pm\sqrt6$, distintas, y $P=(x-(3+\sqrt6))(x-(3-\sqrt6))$ es la factorización en irreducibles reales mónicos. En $\mathbb Q[x]$, al ser mónico entero, toda raíz racional tendría que ser entera y dividir a $3$: los candidatos son $\pm1,\pm3$. Los valores respectivos son $-2,10,-6,30$, todos no nulos. Por el criterio de grado dos, $P$ es irreducible racional, así que él mismo es su factor irreducible mónico. La ausencia de raíces racionales no elimina las dos raíces reales; cada una es simple porque en la factorización real el otro lineal tiene allí valor no nulo.

#### Ejercicio 057. Un residual que no se puede omitir



**Enunciado.** Determina el polinomio real de grado $5$, coeficiente principal $2$, con multiplicidad al menos dos en $1$ y en $-1$, y con $P(0)=6$. Comprueba las multiplicidades exactas y cualquier raíz adicional.



**Solución.** El producto impuesto es $H=(x-1)^2(x+1)^2=(x^2-1)^2$, mónico de grado cuatro. Debe ser $P=H(2x+b)$; el grado y el coeficiente principal fijan la pendiente. Como $H(0)=1$, el dato exige $b=6$. Así $P=2(x-1)^2(x+1)^2(x+3)$, y la construcción es única. En $1$, el residual $2(x+1)^2(x+3)$ vale $32\ne0$; en $-1$, $2(x-1)^2(x+3)$ vale $16\ne0$. Esas raíces son exactamente dobles. La raíz adicional es $-3$, simple porque $2((-3)^2-1)^2=128\ne0$. No hay más raíces reales, y $2+2+1=5$ confirma que las multiplicidades consumen todo el grado. No habría sido correcto usar solo $2H$, que tiene grado cuatro y valor $2$ en cero.

#### Ejercicio 058. Factorizar una suma positiva



**Enunciado.** El polinomio $x^4+4$ es positivo en $\mathbb R$. Encuentra una factorización no trivial con coeficientes racionales y decide si sus factores son irreducibles racionales y reales.



**Solución.** Completamos un cuadrado: $x^4+4=(x^2+2)^2-(2x)^2$. La diferencia de cuadrados produce $(x^2-2x+2)(x^2+2x+2)$. Cada factor es un cuadrático mónico con discriminante $4-8=-4<0$, por lo que es irreducible en $\mathbb R[x]$; al no tener raíces racionales también es irreducible en $\mathbb Q[x]$. La factorización es no trivial en ambos cuerpos, y el producto se comprueba como $(x^2+2)^2-4x^2=x^4+4$. La positividad excluye raíces reales y factores lineales reales; no excluye factores cuadráticos.

#### Ejercicio 059. Cuánto informa una tabla de valores



**Enunciado.** Una tabla contiene $P(0)=0$, $P(1)=1$, $P(2)=8$, $P(3)=27$. Determina $P$ bajo la condición $\deg P\le3$, y describe todos los polinomios de grado a lo sumo $4$ que cumplen la tabla.



**Solución.** El polinomio $x^3$ cumple los cuatro valores. Cualquier otro de grado a lo sumo tres tendría diferencia de grado a lo sumo tres con cuatro raíces distintas, y esa diferencia sería cero. Por tanto $P=x^3$. Para la cota cuatro, $P-x^3$ se anula en $0,1,2,3$, así que es divisible por $H=x(x-1)(x-2)(x-3)$. Si la diferencia no es cero, el grado permite solo un cociente constante. Incluyendo también la diferencia cero, todas las soluciones son $P=x^3+cH$, con $c\in\mathbb R$ (o $c\in\mathbb Q$ si se exigen coeficientes racionales). La sustitución en los cuatro puntos verifica la familia. Para $c=0$ tiene grado tres; para $c\ne0$, grado cuatro. Sin una cota de grado, el cociente podría ser cualquier polinomio del cuerpo elegido.

#### Ejercicio 060. Una condición que aumenta la multiplicidad



**Enunciado.** Describe los polinomios reales mónicos de grado cuatro con raíz $0$ exactamente doble y raíz $1$ exactamente simple. Decide si alguno cumple $P(2)=8$, y si alguno cumple $P(2)=12$.



**Solución.** La divisibilidad impone $P=x^2(x-1)(x+b)$, pues el residual es lineal mónico. En cero, el residual $(x-1)(x+b)$ vale $-b$; la multiplicidad es exactamente dos si y solo si $b\ne0$. En uno, el residual $x^2(x+b)$ vale $1+b$; la multiplicidad es exactamente uno si y solo si $b\ne-1$. La familia buscada corresponde a $b\in\mathbb R\setminus\{0,-1\}$. Ahora $P(2)=4(2+b)$. El valor $8$ obliga a $b=0$, excluido: produce $x^3(x-1)$ y multiplicidad tres en cero. El valor $12$ obliga a $b=1$, admisible: la única solución es $x^2(x-1)(x+1)$. Sus residuales en cero y uno son $-1$ y $2$, respectivamente, y su valor en dos es $12$.

### F. Integración universitaria

#### Ejercicio 061. Certificar un cuártico por extracción



**Enunciado.** Factoriza $P=6x^4-7x^3+11x^2-4$ en irreducibles racionales y reales. Determina todas sus raíces reales y sus multiplicidades.



**Solución.** Como el término independiente es no nulo, una raíz racional reducida $p/q$ debe satisfacer $p\mid4$ y $q\mid6$. Probamos $-1/2$, que da $3/8+7/8+11/4-4=0$, y extraemos $2x+1$. La división da $P=(2x+1)(3x^3-5x^2+8x-4)$. El cociente se anula en $2/3$: $8/9-20/9+16/3-4=0$. Extraer $3x-2$ deja $x^2-x+2$. Obtenemos $P=(2x+1)(3x-2)(x^2-x+2)$. La expansión de $(6x^2-x-2)(x^2-x+2)$ confirma todos los coeficientes. El cuadrático tiene discriminante $1-8=-7<0$, por lo que es irreducible en ambos cuerpos y no aporta raíces reales. Las únicas raíces son $-1/2$ y $2/3$, ambas simples: los otros dos factores no se anulan en ellas. En normalización mónica la factorización es $6(x+\tfrac12)(x-\tfrac23)(x^2-x+2)$. No es necesario evaluar todos los candidatos una vez que el residual queda certificado.

#### Ejercicio 062. Una raíz que reaparece en el cociente



**Enunciado.** Resuelve $x^5-x^4-5x^3+5x^2+4x-4=0$ en $\mathbb R$, indicando multiplicidades y una factorización irreducible racional. Justifica que no quedan raíces pendientes.



**Solución.** Agrupamos como $(x-1)(x^4-5x^2+4)$. Para el cuártico, la sustitución $y=x^2$ da $y^2-5y+4=(y-1)(y-4)$. Así el polinomio es $(x-1)(x^2-1)(x^2-4)=(x-1)^2(x+1)(x-2)(x+2)$. La expansión de la primera agrupación reproduce el enunciado. Todos los lineales son mónicos e irreducibles racionales y reales. La raíz $1$ es doble: su residual $(x+1)(x-2)(x+2)$ vale $-6\ne0$ allí. En $-1,2,-2$, cada residual es producto de factores lineales no nulos, por lo que esas tres raíces son simples. Ningún otro real anula el producto. La suma $2+1+1+1=5$ coincide con el grado; contar una sola vez la raíz $1$ tras la primera extracción habría perdido su segunda aparición.

#### Ejercicio 063. Una familia con una raíz doble impuesta



**Enunciado.** Para $P_{a,b}=x^4+ax^3+bx^2+ax+1$, con $a,b\in\mathbb R$, determina cuándo $-1$ tiene multiplicidad al menos dos. En esa familia, clasifica todas las raíces reales y sus multiplicidades según $a$.



**Solución.** La condición de raíz en $-1$ es $2-2a+b=0$, es decir, $b=2a-2$. Para ese valor se verifica por expansión $P_{a,2a-2}=(x+1)^2[x^2+(a-2)x+1]$. Por tanto la sola condición de raíz ya fuerza multiplicidad al menos dos, y también demuestra la suficiencia. El residual $R_a$ vale $4-a$ en $-1$ y tiene discriminante $a(a-4)$. Si $0<a<4$, ese discriminante es negativo: la única raíz real es $-1$, doble. Si $a<0$ o $a>4$, $R_a$ tiene dos raíces reales distintas $[2-a\pm\sqrt{a(a-4)}]/2$, diferentes de $-1$ porque $a\ne4$; ambas son simples y $-1$ es doble. Si $a=0$, $R_a=(x-1)^2$, así que $P=(x+1)^2(x-1)^2$: las dos raíces son dobles. Si $a=4$, $R_a=(x+1)^2$ y $P=(x+1)^4$: solo $-1$, de multiplicidad cuatro. Estos casos cubren todos los parámetros; no se necesita derivar para verificar la raíz repetida.

#### Ejercicio 064. Dos cuerpos y una potencia par



**Enunciado.** Factoriza $x^4-9$ en irreducibles de $\mathbb Q[x]$ y $\mathbb R[x]$. Explica por qué una factorización completa en el primer cuerpo puede seguir descomponiéndose en el segundo.



**Solución.** La diferencia de cuadrados da $x^4-9=(x^2-3)(x^2+3)$. El segundo cuadrático tiene discriminante $-12$, por lo que es irreducible real y racional. Para el primero, una raíz racional sería un entero divisor de $3$; los candidatos $\pm1,\pm3$ dan $-2$ u $6$, nunca cero. Así $x^2-3$ es irreducible racional y la expresión inicial es una factorización en irreducibles de $\mathbb Q[x]$. En $\mathbb R[x]$, $x^2-3=(x-\sqrt3)(x+\sqrt3)$, y la factorización completa es $(x-\sqrt3)(x+\sqrt3)(x^2+3)$. Sus únicas raíces reales son $\pm\sqrt3$, simples: son distintas y $x^2+3$ vale $6\ne0$ allí. Irreducibilidad significa imposibilidad de factorización dentro del cuerpo especificado; al ampliar el cuerpo aparecen coeficientes antes no disponibles.

#### Ejercicio 065. Reconstrucción con control de una desigualdad



**Enunciado.** Busca un polinomio real de grado a lo sumo cuatro que tenga multiplicidad al menos dos en $1$, raíz $-2$, $P(0)=4$ y $P(2)=0$. Decide si es único y determina sus multiplicidades.



**Solución.** Como $P(0)=4$, el polinomio es no nulo. La condición $P(2)=0$ añade una raíz distinta de $1$ y $-2$. El producto $H=(x-1)^2(x+2)(x-2)$, de grado cuatro, divide a $P$. La cota de grado obliga a $P=cH$. En cero, $H(0)=-4$, así que $c=-1$. La única solución es $P=-(x-1)^2(x+2)(x-2)=-(x-1)^2(x^2-4)$. Los residuales son no nulos: en $1$, $-(1^2-4)=3$; en $-2$, $-(-2-1)^2(-2-2)=36$; en $2$, $-(2-1)^2(2+2)=-4$. Por tanto las multiplicidades son dos, uno y uno, respectivamente, y no hay más raíces reales. Los datos consumen el grado máximo; aumentar alguna multiplicidad sería incompatible con esa cota y con $P\ne0$.

#### Ejercicio 066. Interpolación con un resto conocido



**Enunciado.** Determina el polinomio de grado a lo sumo tres que cumple $P(-1)=3$, $P(0)=2$, $P(1)=3$ y deja resto $12$ al dividir por $x-2$. Factoriza el resultado en irreducibles racionales y reales.



**Solución.** El resto al dividir por $x-2$ es $P(2)$, así que el cuarto dato es $P(2)=12$. El polinomio $Q=x^2+2$ satisface los tres primeros datos. Por divisibilidad de la diferencia en puntos distintos, todo candidato de grado a lo sumo tres es $P=Q+c(x+1)x(x-1)$. Evaluar en dos da $12=6+6c$, por lo que $c=1$. Así $P=x^3+x^2-x+2$. Sus valores en los cuatro puntos son $3,2,3,12$, y la cota de raíces asegura unicidad. Para factorizar, observamos que $P(-2)=-8+4+2+2=0$; la división da $P=(x+2)(x^2-x+1)$. Expandir confirma la identidad. El discriminante del residual es $1-4=-3<0$, de modo que es irreducible real y racional; el lineal también es irreducible en ambos cuerpos. La única raíz real es $-2$, simple porque el residual allí vale $7\ne0$.

#### Ejercicio 067. Traslado y repetición de un factor



**Enunciado.** Factoriza $P=[(x-3)^2-2]^2(x-2)$ en irreducibles racionales y reales. Determina todas sus raíces reales y multiplicidades.



**Solución.** El cuadrático $A=(x-3)^2-2=x^2-6x+7$ es un traslado de $x^2-2$, irreducible racional. En efecto, $x^2-2$ no tiene raíces racionales (los candidatos enteros $\pm1,\pm2$ fallan), y una factorización no trivial de su traslado, al sustituir $x+3$, daría una del original. Así $P=(x^2-6x+7)^2(x-2)$ ya está factorizado en irreducibles racionales mónicos. Sobre $\mathbb R$, $A=(x-(3+\sqrt2))(x-(3-\sqrt2))$, por lo que los dos lineales aparecen al cuadrado en $P$. Las raíces $3\pm\sqrt2$ son distintas y no son $2$: si alguna lo fuera, tendríamos $\sqrt2=1$ o $-1$, imposible. Por tanto tienen multiplicidad dos. La raíz $2$ es simple porque $A(2)^2=(-1)^2=1\ne0$. Estas tres raíces agotan el producto; la suma de multiplicidades es $2+2+1=5=\deg P$.

#### Ejercicio 068. Encontrar un divisor común con multiplicidades



**Enunciado.** En $\mathbb Q[x]$, sean $P=(x-1)^3(x+2)(x^2+1)$ y $Q=(x-1)^2(x+2)^2(x^2+2)$. Determina su máximo común divisor mónico y justifica que ningún factor falta.



**Solución.** Los lineales son irreducibles racionales; $x^2+1$ y $x^2+2$ son irreducibles por no tener raíces reales, en particular racionales. Son mónicos distintos, de modo que no son asociados, y ninguno es asociado a un lineal por su grado. Por unicidad de la factorización de [§25.15](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md#apm-c25-s15), un divisor común solo puede usar irreducibles presentes en ambos productos, con exponentes no mayores que los de cada uno. Los mínimos son dos para $x-1$ y uno para $x+2$. Así $D=(x-1)^2(x+2)$ divide a ambos: $P/D=(x-1)(x^2+1)$ y $Q/D=(x+2)(x^2+2)$. Cualquier divisor común divide a $D$ por esos límites de exponentes, lo que prueba la propiedad de máximo común divisor. La normalización mónica elimina la libertad de multiplicar por una constante no nula. En $\mathbb R[x]$ los dos cuadráticos también permanecen irreducibles, por lo que el mismo $D$ sigue sirviendo.

#### Ejercicio 069. Irreducibilidad y un certificado de Bézout



**Enunciado.** Para $P=x^3-3x+1\in\mathbb Q[x]$, prueba irreducibilidad racional y construye una identidad de Bézout entre $P$ y $x-1$. Deduce que si $P\mid(x-1)R$ para $R\in\mathbb Q[x]$, entonces $P\mid R$.



**Solución.** Como $P$ es mónico entero y su término independiente es $1$, sus únicos candidatos racionales son $1$ y $-1$. Pero $P(1)=-1$ y $P(-1)=3$. No tiene raíz racional, y el criterio de grado tres da irreducibilidad en $\mathbb Q[x]$. La división por $x-1$ produce $P=(x-1)(x^2+x-2)-1$. Reordenando, $(x^2+x-2)(x-1)-P=1$, una identidad de Bézout explícita. Multiplicamos por $R$ y obtenemos $R=(x^2+x-2)(x-1)R-PR$. Si $P$ divide a $(x-1)R$, divide a los dos términos del lado derecho y, por tanto, a $R$. Esta última conclusión está certificada directamente por la identidad, sin suponer factorización única ni cancelar divisibilidad de manera informal. No se infiere irreducibilidad real de la ausencia de raíces racionales.

#### Ejercicio 070. Eliminar denominadores y normalizar



**Enunciado.** Sea $P=\tfrac1{12}(3x-2)^2(2x+1)(x^2+2)$. Da su grado y coeficiente principal, determina sus raíces reales y multiplicidades, y escribe la factorización en irreducibles mónicos de $\mathbb Q[x]$ con la unidad correspondiente. Explica qué cambia al pasar a $12P$.



**Solución.** Los grados suman $2+1+2=5$ y el coeficiente principal es $(1/12)\cdot9\cdot2=3/2$. Sacar los coeficientes principales de los lineales da $P=\tfrac32(x-\tfrac23)^2(x+\tfrac12)(x^2+2)$. El cuadrático tiene discriminante $-8$ y es irreducible racional y real; los lineales son irreducibles. Las únicas raíces reales son $2/3$ y $-1/2$, de multiplicidades dos y uno respectivamente: el otro lineal no se anula en cada punto y $x^2+2>0$. La unidad de la normalización es $3/2$. Multiplicar por $12$ elimina denominadores, conserva raíces y multiplicidades, pero multiplica todos los valores por $12$ y cambia el coeficiente principal a $18$. Por ejemplo, $P(0)=2/3$ y $(12P)(0)=8$. El residual cuadrático explica por qué la suma de multiplicidades reales es tres aunque el grado sea cinco.

#### Ejercicio 071. Una identidad determinada por cinco datos



**Enunciado.** Sean $P,Q\in\mathbb R[x]$ de grado a lo sumo cuatro. Supón que coinciden en $-2,-1,0,1$ y que $P(2)-Q(2)=24$. Determina $P-Q$ y decide si puede tener una raíz adicional a los cuatro puntos de coincidencia.



**Solución.** La diferencia $R=P-Q$ es divisible por $H=(x+2)(x+1)x(x-1)$, debido a las cuatro raíces distintas. Como $R(2)=24\ne0$, no es cero; la cota de grado fuerza $R=cH$, con $c$ constante. En dos, $H(2)=4\cdot3\cdot2\cdot1=24$, así que $c=1$ y $R=H$. La expansión da $R=x^4+2x^3-x^2-2x$, y la evaluación en los cinco puntos confirma los datos. Sus cuatro raíces son simples, porque en cada una el producto de los otros tres factores es no nulo. No hay ninguna raíz real adicional: un producto de los cuatro lineales solo puede anularse en sus cuatro puntos, o bien la cota excluiría una quinta raíz para este polinomio no nulo de grado cuatro. Los datos fijan la diferencia, no fijan $P$ y $Q$ individualmente.

#### Ejercicio 072. Cuántas raíces certifica una forma mixta



**Enunciado.** Para $P=(x^2-2)^2(x^2+1)(x-1)\in\mathbb Q[x]$, determina grado, raíces racionales, raíces reales y multiplicidades. Da las factorizaciones en irreducibles racionales y reales y explica qué parte del grado no aparece en el conteo de raíces reales.



**Solución.** El grado es $4+2+1=7$ y el polinomio es mónico. En $\mathbb Q[x]$, $x^2-2$ es irreducible porque los candidatos racionales enteros $\pm1,\pm2$ no se anulan; $x^2+1$ es irreducible porque no tiene raíces reales. Por tanto la forma dada es la factorización en irreducibles racionales. Su única raíz racional es $1$, simple: el residual allí vale $(1-2)^2(1+1)=2\ne0$. En $\mathbb R[x]$ se obtiene $P=(x-\sqrt2)^2(x+\sqrt2)^2(x^2+1)(x-1)$. Las raíces $\sqrt2,-\sqrt2,1$ son distintas; las dos primeras son dobles y la tercera simple, pues sus residuales no se anulan. No hay más raíces reales por la positividad de $x^2+1$ y la propiedad de un producto. La suma de multiplicidades reales es cinco; los dos grados restantes corresponden al factor cuadrático sin raíces reales. No se atribuyen esas dos unidades de grado a raíces que no han sido introducidas en el capítulo.

### G. Síntesis avanzada

#### Ejercicio 073. Reconstrucción y libertad residual



**Enunciado.** Determina todos los polinomios reales mónicos de grado cinco con raíz $0$ exactamente doble, raíz $1$ exactamente simple y $P(-1)=4$. Para cada solución, certifica cuántas raíces reales distintas tiene y sus multiplicidades. Decide además si el dato $P(2)=12$ selecciona una única solución.



**Solución.** Las multiplicidades mínimas fuerzan $P=x^2(x-1)Q$; el grado y la normalización exigen $Q=x^2+ux+v$. En $-1$, el factor inicial vale $-2$, por lo que $-2(1-u+v)=4$, es decir, $v=u-3$. Así los candidatos son $P_u=x^2(x-1)(x^2+ux+u-3)$. La multiplicidad en cero es exactamente dos si $Q(0)=u-3\ne0$; en uno es exactamente uno si $Q(1)=2u-2\ne0$. La familia buscada corresponde, por tanto, a $u\in\mathbb R\setminus\{1,3\}$, y cada miembro cumple también el valor en $-1$.

El discriminante de $Q$ es $u^2-4(u-3)=(u-2)^2+8>0$, de modo que añade dos raíces reales distintas $r_\pm=[-u\pm\sqrt{(u-2)^2+8}]/2$. Las exclusiones de $u$ aseguran que ninguna coincide con cero o uno. Cada una es simple porque el otro lineal de $Q$, así como $x^2(x-1)$, tiene allí valor no nulo. Hay cuatro raíces reales distintas: cero doble y las otras tres simples; la suma de multiplicidades es cinco.

Finalmente, $P_u(2)=4(4+2u+u-3)=4(1+3u)$. El valor $12$ exige $u=2/3$, que no está excluido. Selecciona la única solución $x^2(x-1)(x^2+\tfrac23x-\tfrac73)$. Las verificaciones anteriores demuestran que el nuevo dato no altera las multiplicidades exigidas.

#### Ejercicio 074. Parámetros y coincidencia de raíces



**Enunciado.** Para $t\in\mathbb R$, clasifica todas las raíces reales de $P_t=(x^2-t)(x^2-2tx+1)$ y sus multiplicidades. Justifica exhaustivamente los valores del parámetro en que raíces de los dos factores pueden coincidir.



**Solución.** Analizamos primero cada cuadrático. El factor $A_t=x^2-t$ no tiene raíces reales si $t<0$, tiene cero doble si $t=0$, y raíces simples $\pm\sqrt t$ si $t>0$. El factor $B_t=x^2-2tx+1$ tiene discriminante $4(t^2-1)$: sin raíces si $|t|<1$, raíz doble $-1$ si $t=-1$, raíz doble $1$ si $t=1$, y dos raíces simples $t\pm\sqrt{t^2-1}$ si $|t|>1$.

Solo con $t>0$ es posible una coincidencia real entre factores, pues $B_0(0)=1$. Si $r$ es común, $r^2=t$ y $r^2-2tr+1=0$, de donde $r=(t+1)/(2t)$. Al elevar al cuadrado se obtiene $4t^3=(t+1)^2$, o bien $(t-1)(4t^2+3t+1)=0$. El segundo factor es $4(t+3/8)^2+7/16>0$, así que necesariamente $t=1$. Para ese valor, $r=1$ sí es común. Esta sustitución comprueba la suficiencia, pues elevar al cuadrado por sí solo no la garantiza.

La clasificación completa es la siguiente. Si $t<-1$, las únicas raíces son $t\pm\sqrt{t^2-1}$, simples. Si $t=-1$, solo $-1$, doble. Si $-1<t<0$, no hay raíces reales. Si $t=0$, solo cero, doble. Si $0<t<1$, las únicas raíces son $\pm\sqrt t$, simples. Si $t=1$, $P_1=(x-1)^3(x+1)$: uno triple y menos uno simple. Si $t>1$, las cuatro raíces $\pm\sqrt t$ y $t\pm\sqrt{t^2-1}$ son distintas y simples por la exclusión de coincidencias. En los casos sin coincidencia, el otro factor es no nulo en cada raíz, de modo que no cambia su multiplicidad. Anular el producto exige anular un factor, lo que certifica que ninguna raíz real falta.

#### Ejercicio 075. Irreducibilidad de una cuártica por coeficientes



**Enunciado.** Decide si $P=x^4+2x^2+2$ es irreducible en $\mathbb Q[x]$ y en $\mathbb R[x]$. Justifica cada conclusión y da una factorización real en irreducibles si existe.



**Solución.** Como $P=(x^2+1)^2+1>0$ para todo real, no tiene raíces reales ni racionales. Esto excluye factores lineales, pero todavía permite una descomposición de grados dos y dos. Si fuera reducible racional, podemos absorber las unidades y tomar ambos cuadráticos mónicos, pues $P$ es mónico. El coeficiente cúbico cero obliga a una expresión $(x^2+ux+v)(x^2-ux+w)$ con $u,v,w\in\mathbb Q$. Comparar coeficientes da $v+w-u^2=2$, $u(w-v)=0$ y $vw=2$.

Si $u=0$, se exige $v+w=2$ y $vw=2$, de modo que $v,w$ serían raíces reales de $z^2-2z+2$, imposible porque su discriminante es $-4$. Si $u\ne0$, entonces $w=v$ y $v^2=2$. Esta última ecuación no tiene solución racional: el polinomio mónico entero $z^2-2$ solo admite como candidatos racionales $\pm1,\pm2$, y ninguno es raíz. Quedan excluidas todas las factorizaciones racionales no triviales; $P$ es irreducible en $\mathbb Q[x]$.

En $\mathbb R[x]$ tomamos $v=w=\sqrt2$ y $u=\sqrt{2\sqrt2-2}$, que existe y es positivo porque $\sqrt2>1$. Entonces
$$
P=(x^2+ux+\sqrt2)(x^2-ux+\sqrt2).
$$
El producto tiene coeficiente cuadrático $2\sqrt2-u^2=2$, término constante $2$ y términos impares cero. Cada cuadrático tiene discriminante $u^2-4\sqrt2=-2\sqrt2-2<0$, así que es irreducible real. La expresión demuestra reducibilidad real y proporciona la factorización en irreducibles, sin suponer un teorema general sobre grados de irreducibles reales.

#### Ejercicio 076. Identidad con información parcial



**Enunciado.** Sean $P,Q\in\mathbb R[x]$ de grado a lo sumo cinco, que coinciden en $-1,0,1$. Supón además que $P-Q$ tiene multiplicidad al menos dos en cero y que $(P-Q)(2)=12$, $(P-Q)(-2)=-12$. Describe todas las diferencias posibles y decide si la información obliga a $P=Q$.



**Solución.** Escribimos $R=P-Q$. Los dos valores no nulos aseguran $R\ne0$. Las condiciones de raíces y multiplicidad hacen que $H=x^2(x-1)(x+1)=x^2(x^2-1)$ divida a $R$. Como $H$ tiene grado cuatro y $R$ grado a lo sumo cinco, escribimos $R=H(ax+b)$; se incluye un cociente constante mediante $a=0$. En ambos puntos $2$ y $-2$, $H$ vale $12$, por lo que $2a+b=1$ y $-2a+b=-1$. Restar da $4a=2$, así que $a=1/2$ y $b=0$. La única diferencia posible es $R=\tfrac12x^3(x^2-1)$.

Este polinomio cumple las tres coincidencias, tiene multiplicidad exactamente tres en cero y toma los valores prescritos en $\pm2$. Por tanto los datos son compatibles con «al menos dos», pero no con «exactamente dos». No obligan a $P=Q$: de hecho lo excluyen, ya que $R(2)\ne0$. Para mostrar existencia de pares, basta escoger cualquier $Q$ de grado a lo sumo cinco y poner $P=Q+R$, que mantiene esa cota. Los datos fijan la diferencia, pero dejan libre el polinomio común que se añade a ambos.

#### Ejercicio 077. Interpolación y una condición de multiplicidad



**Enunciado.** Determina todos los polinomios reales de grado a lo sumo cinco con valores $P(-2)=9$, $P(-1)=0$, $P(0)=1$, $P(1)=0$, $P(2)=9$. Entre ellos, decide cuáles tienen multiplicidad al menos dos en $1$ y determina sus raíces reales.



**Solución.** El polinomio $S=(x^2-1)^2$ cumple los cinco valores, como se comprueba sustituyendo: en $\pm2$ vale $9$, en $\pm1$ vale cero y en cero vale uno. Si $P$ es otro candidato, $P-S$ se anula en los cinco nodos distintos, así que es divisible por $H=(x+2)(x+1)x(x-1)(x-2)=x(x^2-1)(x^2-4)$. La cota de grado obliga a $P=S+cH$, con $c\in\mathbb R$, incluida la diferencia cero. Recíprocamente, cada miembro de esta familia satisface los cinco datos. Si se exigiera grado a lo sumo cuatro, la cota de raíces daría unicidad de $S$.

Para estudiar la multiplicidad en uno, dividimos por $x-1$:
$$
\frac{P}{x-1}=(x-1)(x+1)^2+c\,x(x+1)(x^2-4).
$$
El cociente vale $-6c$ en uno. Por el teorema del factor, $1$ tiene multiplicidad al menos dos si y solo si $c=0$. Por tanto la única solución con ese requisito adicional es $P=S=(x-1)^2(x+1)^2$. Sus raíces reales son $\pm1$, ambas exactamente dobles, porque los residuales en esos puntos valen $4\ne0$. No tiene ninguna otra raíz. La condición de multiplicidad elimina la libertad que cinco valores dejan bajo la cota cinco; no basta tratarla como otro dato de evaluación idéntico al ya conocido $P(1)=0$.

#### Ejercicio 078. Grado residual y ausencia de nuevas raíces



**Enunciado.** Describe todos los polinomios reales de grado siete, coeficiente principal $2$, cuyas únicas raíces reales sean $-2$ de multiplicidad tres y $1$ de multiplicidad dos, y que satisfagan $P(0)=16$. Justifica tanto la necesidad como la suficiencia de las condiciones sobre tus parámetros.



**Solución.** Las multiplicidades dan $P=2(x+2)^3(x-1)^2Q$, donde $Q$ es un cuadrático mónico real, por el grado y el coeficiente principal. Escribimos $Q=x^2+bx+c$. En cero, $P(0)=2\cdot8\cdot1\cdot c=16c$, por lo que $c=1$. Para no aumentar las multiplicidades ni añadir otras raíces reales, $Q$ debe carecer de raíces reales: si tuviera alguna, coincidiría con una raíz prescrita o sería una adicional, y ambas opciones infringen el enunciado. En grado dos esta ausencia equivale a discriminante negativo. Aquí $b^2-4<0$, esto es, $-2<b<2$.

Así la familia completa es $P_b=2(x+2)^3(x-1)^2(x^2+bx+1)$, con $b\in(-2,2)$. Para cada parámetro permitido, $Q=(x+b/2)^2+1-b^2/4>0$ en todo real. Por ello los residuales en $-2$ y uno no se anulan, las multiplicidades son exactamente tres y dos, y no existen raíces adicionales. Grado, coeficiente principal y valor en cero se comprueban en el producto. Los extremos no se admiten: $b=-2$ produce $(x-1)^2$ y aumenta la multiplicidad en uno; $b=2$ produce $(x+1)^2$ y añade la raíz $-1$. La suma de multiplicidades prescritas es cinco y los dos grados residuales se conservan en un factor irreducible real, sin aportar raíces.

#### Ejercicio 079. Divisibilidad certificada por Bézout



**Enunciado.** En $\mathbb Q[x]$, sean $A=x^2+1$, $B=x^2+2$ y $P=A^2B$. Determina todos los polinomios $R$ que cumplen simultáneamente $A\mid R$ y $P\mid BR$. Da un certificado de Bézout que justifique tu conclusión y explica qué información adicional aporta la segunda condición.



**Solución.** La diferencia $B-A=1$ da coprimalidad entre $A$ y $B$. Para aplicar Bézout al exponente requerido, buscamos un certificado entre $A^2$ y $B$. Como $A=B-1$, $A^2=(B-1)^2=B(B-2)+1$; por tanto
$$
A^2-(B-2)B=1.
$$
Si $P=A^2B$ divide a $BR$, existe $S$ con $BR=A^2BS$. El polinomio $B$ es no nulo, y $K[x]$ no tiene divisores de cero, así que cancelar esta igualdad ya da $R=A^2S$. También podemos certificarlo sin esa cancelación: la hipótesis implica $A^2\mid BR$, y multiplicar la identidad de Bézout por $R$ produce $R=A^2R-(B-2)BR$, cuyos dos términos son divisibles por $A^2$; de nuevo $A^2\mid R$.

Recíprocamente, si $R=A^2S$ para cualquier $S\in\mathbb Q[x]$, entonces $A\mid R$ y $BR=A^2BS=PS$, por lo que ambas condiciones se cumplen. Todas las soluciones son, pues, $R=(x^2+1)^2S$, incluido $R=0$. La segunda condición exige una segunda copia del irreducible $A$, no solo la divisibilidad por una copia. De hecho hace redundante la primera. Los factores $A$ y $B$ son irreducibles racionales por sus discriminantes negativos; la factorización única confirma que el exponente de $A$ requerido es dos, aunque el argumento de Bézout no la necesitó.

#### Ejercicio 080. Comparar certificados en dos cuerpos



**Enunciado.** Para $P=(x^4+4)(x^2-2)^2(x-1)$, determina las factorizaciones en irreducibles mónicos de $\mathbb Q[x]$ y $\mathbb R[x]$, las raíces reales y sus multiplicidades. Justifica la exhaustividad y explica por qué ni buscar solo raíces racionales ni contar el grado basta para obtener la respuesta.



**Solución.** Primero usamos la identidad $x^4+4=(x^2-2x+2)(x^2+2x+2)$, comprobada como $(x^2+2)^2-4x^2$. Ambos cuadráticos tienen discriminante $-4$, de modo que son irreducibles reales y racionales. El factor $x^2-2$ es irreducible racional: por ser mónico entero solo podría tener raíces racionales entre $\pm1,\pm2$, que no lo anulan. Por tanto la factorización irreducible racional mónica es
$$
P=(x^2-2x+2)(x^2+2x+2)(x^2-2)^2(x-1).
$$
La unidad es uno. En $\mathbb R[x]$ se descompone el tercer factor y queda
$$
P=(x^2-2x+2)(x^2+2x+2)(x-\sqrt2)^2(x+\sqrt2)^2(x-1).
$$
Los cuadráticos continúan siendo irreducibles reales y los lineales lo son por su grado. Así hemos justificado cada factor dentro del cuerpo correspondiente, sin usar una clasificación general de irreducibles reales.

Las únicas raíces reales son $1,\sqrt2,-\sqrt2$, distintas. En uno, el residual vale $(1^4+4)(1^2-2)^2=5\ne0$, así que es simple. En cada una de $\pm\sqrt2$, el factor $x^2-2$ tiene una raíz simple porque sus dos raíces son distintas; al elevarlo al cuadrado, la multiplicidad pasa a dos. Los factores restantes no se anulan allí: $x^4+4>0$ y esos puntos no son uno. Por tanto ambas raíces son exactamente dobles. No hay más raíces reales porque todo cero del producto debe anular algún factor y los dos cuadráticos no tienen raíces reales.

El grado es $4+4+1=9$, mientras que la suma de multiplicidades reales es $1+2+2=5$. Los cuatro grados restantes están en los dos cuadráticos sin raíces reales. Una búsqueda solo racional detecta la raíz uno pero omite las dos irracionales; contar nueve grados tampoco da nueve raíces reales. La factorización racional completa y la real completa son certificados distintos, cada uno con su dominio explícito.



















### H. Profundización y reconstrucción

Intente el enunciado antes de leer la solución que lo acompaña. Las tareas mantienen separados dominio, certificado y cobertura.



#### Ejercicio 081. Construcción mínima y dato incompatible

Dados $k\in\mathbb R$, busque un polinomio de grado mínimo con raíz $1$ de multiplicidad exactamente tres, raíz $-1$ de multiplicidad exactamente dos y $P(0)=k$. Clasifique la existencia y la unicidad mínima.



#### Solución 081

Todo candidato es divisible por $F=(x-1)^3(x+1)^2$, de grado cinco. En el grado mínimo debe ser $P=cF$, con $c\ne0$. Como $F(0)=-1$, el dato exige $c=-k$. Si $k\ne0$, $P=-kF$ es el único candidato de grado cinco y sus multiplicidades son exactas porque los factores residuales no se anulan en las raíces opuestas. Si $k=0$, el grado cinco es imposible, pero el grado seis se alcanza con $P=cxF$, cualquier $c\ne0$: cero no coincide con las dos raíces impuestas. Así existe una familia mínima de grado seis, sin unicidad.



#### Ejercicio 082. Un dato adicional que fuerza multiplicidad mayor

Busque todos los $P\in\mathbb R[x]$ de grado a lo sumo cuatro que tengan $1$ como raíz de multiplicidad al menos dos, $-1$ como raíz y satisfagan $P(0)=2$, $P(2)=m$. Determine cuándo las multiplicidades impuestas son exactas.



#### Solución 082

Escribimos $P=(x-1)^2(x+1)(ax+b)$ por divisibilidad y la cota de grado. El dato en cero fuerza $b=2$; en dos, $3(2a+2)=m$, luego $a=(m-6)/6$. Esta fórmula construye un único $P$ para cada $m$. La multiplicidad en $1$ es exactamente dos si $a+2\ne0$, es decir $m\ne-6$; en $-1$ es exactamente uno si $2-a\ne0$, es decir $m\ne18$. En esos dos valores excepcionales, el residual lineal añade respectivamente un factor en la misma raíz. Las evaluaciones comprueban todos los datos.



#### Ejercicio 083. Colisión y normalización de una familia construida

Para $t\in\mathbb R$, construya el polinomio mónico de menor grado divisible por $(x-t)^2$ y $(x+t)^3$. Compare $t=0$ con $t\ne0$ y certifique sus multiplicidades.



#### Solución 083

Si $t\ne0$, los dos factores corresponden a raíces distintas; su producto divide a cualquier candidato. El mínimo mónico es $P=(x-t)^2(x+t)^3$, de grado cinco. Sus residuales en $t$ y $-t$ son $(2t)^3$ y $(-2t)^2$, no nulos, así las multiplicidades son dos y tres. Si $t=0$, los requisitos son divisibilidad por $x^2$ y por $x^3$, equivalentes a la segunda; el mínimo mónico es $x^3$, no $x^5$. La suma de multiplicidades solo correspondía a raíces distintas, no a dos requisitos sobre la misma raíz.



#### Ejercicio 084. Cambiar el cuerpo y mantener el certificado

Sea $d>0$ racional que no sea cuadrado de ningún racional. Compare la irreducibilidad de $x^2-d$ sobre $\mathbb Q$ y $\mathbb R$.



#### Solución 084

Una raíz racional $r$ cumpliría $r^2=d$, contra la hipótesis. Como el grado es dos, la ausencia de raíces racionales prueba irreducibilidad sobre $\mathbb Q$. En los reales existe $\sqrt d$ y $(x-\sqrt d)(x+\sqrt d)=x^2-d$ es una factorización en dos lineales, luego es reducible. Expandir certifica la identidad. La hipótesis no afirma ausencia de raíces reales; especifica justamente qué coeficientes faltan en el cuerpo pequeño.



#### Ejercicio 085. Construir una familia positiva reducible

Para $c>0$ racional, construya todos los $u\in\mathbb Q$ que permitan $x^4+4c^4=(x^2+ux+2c^2)(x^2-ux+2c^2)$. Pruebe que los factores son irreducibles reales y que el producto no tiene raíces reales.



#### Solución 085

La expansión da $x^4+(4c^2-u^2)x^2+4c^4$. La identidad exige $u^2=4c^2$, luego todos los valores son $u=\pm2c$, racionales. Para cualquiera, los factores son $(x\pm c)^2+c^2$, estrictamente positivos e irreducibles cuadráticos sobre los reales. El producto es reducible racional, pero positivo en toda la recta. La construcción determina los coeficientes de la descomposición y certifica una familia entera; no deduce irreducibilidad de la ausencia de raíces del cuártico.



#### Ejercicio 086. Separar raíces y factores en dos cuerpos

Dé factorizaciones irreducibles de $P=x^4-x^2-2$ sobre $\mathbb Q$ y $\mathbb R$, indicando sus raíces en cada cuerpo.



#### Solución 086

La sustitución $u=x^2$ da $P=(x^2-2)(x^2+1)$. En $\mathbb Q$, el primero no tiene raíces racionales porque $\sqrt2$ es irracional, y el segundo no tiene raíces reales; ambos son irreducibles cuadráticos. Por tanto $P$ no tiene raíces racionales aunque es reducible allí. En $\mathbb R$, se obtiene $(x-\sqrt2)(x+\sqrt2)(x^2+1)$, con los dos lineales irreducibles y el cuadrático positivo irreducible. Sus raíces reales son exactamente $\pm\sqrt2$. Expandir el producto original recupera el cuártico.



#### Ejercicio 087. Una familia entera de contraejemplos

Para $a,b\in\mathbb R\setminus\{0\}$, pruebe que $(x^2+a^2)(x^2+b^2)$ es reducible sobre $\mathbb R$ y carece de raíces reales. Clasifique la repetición de sus factores mónicos.



#### Solución 087

Ambos factores son cuadráticos de grado positivo, así el producto es reducible. Para todo real $x$, cada factor es estrictamente positivo, de modo que el producto nunca es cero. Cada cuadrático es irreducible real por la ausencia de raíces. Coinciden exactamente si $a^2=b^2$, es decir $a=b$ o $a=-b$; entonces el producto es el cuadrado de un irreducible. Si no coinciden, son dos factores irreducibles mónicos distintos. La clasificación evita confundir repetición de factores con existencia de raíces reales.



#### Ejercicio 088. Dos factores irreducibles y ninguna raíz

Factorice $x^4+x^2+1$ sobre $\mathbb R$ y explique por qué un criterio basado solo en raíces no basta.



#### Solución 088

Es $(x^2+1)^2-x^2=(x^2+x+1)(x^2-x+1)$. Cada factor es $(x\pm1/2)^2+3/4>0$, de modo que no tiene raíces reales y es irreducible de grado dos. El cuártico es reducible porque tiene esa descomposición no constante, pese a no tener raíces reales. Expandir da $x^4+2x^2+1-x^2=x^4+x^2+1$. La partición $2+2$ del grado permite exactamente este fenómeno.



#### Ejercicio 089. Ausencia de raíces y una prueba adicional necesaria

Pruebe que $x^4+1$ es irreducible sobre $\mathbb Q$ pero reducible sobre $\mathbb R$, sin usar «no tiene raíces» como prueba suficiente de la primera afirmación.



#### Solución 089

No hay raíces racionales por positividad; si fuera reducible racional, habría dos factores cuadráticos, normalizados como $(x^2+ax+b)(x^2-ax+d)$. Comparar da $bd=1$, $a(d-b)=0$, $b+d-a^2=0$. Si $a=0$, $d=-b$ y $bd=-b^2=1$, imposible en reales. Si $a\ne0$, $d=b$ y $b^2=1$. Para $b=-1$, $a^2=-2$, imposible; para $b=1$, $a^2=2$, imposible racional. Se agotaron las particiones sin lineales, probando irreducibilidad racional. En reales sí existe $\sqrt2$, y $x^4+1=(x^2+\sqrt2x+1)(x^2-\sqrt2x+1)$. La expansión verifica el cambio de cuerpo.



#### Ejercicio 090. Cuántos datos certifican un resto

Sean $D=x^2+1$ y $R,S$ de grado menor que dos o cero. Pruebe que $R(0)=S(0)$ y $R(2)=S(2)$ fuerzan $R=S$. ¿Basta un solo dato?



#### Solución 090

La diferencia $R-S$ tiene grado a lo sumo uno o es cero. Si no fuera cero, no podría tener dos raíces distintas por la cota de raíces de C25. Los dos datos la anulan en cero y dos, luego es cero. Un solo dato no basta: $R=0$ y $S=x$ coinciden en cero, ambos son restos de grado permitido y son distintos. La cota de grado es esencial; $x(x-2)$ también se anula en esos dos puntos pero no es un resto permitido para $D$.



#### Ejercicio 091. Datos independientes para un polinomio par

Sean $P,Q$ polinomios pares de grado a lo sumo $2n$, admitiendo cero. Pruebe que $n+1$ coincidencias en puntos con cuadrados distintos fuerzan $P=Q$. Construya un contraejemplo si solo se dan $n$ de esos puntos, para $n\ge1$.



#### Solución 091

Escribimos $P(x)=U(x^2)$, $Q(x)=V(x^2)$, con $U,V$ de grado a lo sumo $n$. Las coincidencias en $a_j$ dan raíces $a_j^2$ distintas de $U-V$, así $n+1$ de ellas fuerzan diferencia cero por la cota. Con solo $n$ puntos, tome $P=0$ y $Q=\prod_{j=1}^n(x^2-a_j^2)$, mónico par de grado $2n$, que coincide con cero en todos los datos pero no es idéntico. Los valores en $a$ y $-a$ no aportan datos independientes para polinomios pares; la condición sobre cuadrados evita contarlos dos veces.



#### Ejercicio 092. Valores que dejan una libertad residual

Dados reales distintos $a,b,c$ y valores $u,v,w$, describa todos los polinomios reales que toman esos valores en $a,b,c$; indique cuándo son únicos.



#### Solución 092

Construimos $L=u\frac{(x-b)(x-c)}{(a-b)(a-c)}+v\frac{(x-a)(x-c)}{(b-a)(b-c)}+w\frac{(x-a)(x-b)}{(c-a)(c-b)}$. Los denominadores son no nulos y evaluar comprueba los tres valores. Cualquier otro $P$ tiene $P-L$ anulado en los tres puntos, luego es divisible por $(x-a)(x-b)(x-c)$. Así todos son $P=L+(x-a)(x-b)(x-c)T$, $T\in\mathbb R[x]$. En grado a lo sumo dos, esa diferencia debe ser cero, de modo que $L$ es único. Sin la cota hay infinitos candidatos.

***

[← Capítulo 24](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 26 →](algebra-para-matematicos-capitulo-26-numeros-complejos-y-el-horizonte-de-las-ecuaciones.md)

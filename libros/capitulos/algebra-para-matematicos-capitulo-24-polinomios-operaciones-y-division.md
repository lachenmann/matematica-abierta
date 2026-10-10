---
{
  "title": "Polinomios: operaciones y división",
  "description": "Capítulo 24 del Tomo I de Álgebra para matemáticos, con 100 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0199",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C24",
  "editorial-id": "MA-BCH-APM-01-020",
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
    "MA-BCH-0198"
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

Una división aritmética separa una cantidad en múltiplos de otra y un resto. Con polinomios, la misma idea sigue funcionando, pero la medida que hace terminar el procedimiento es el grado. En este capítulo aprenderemos a calcular y a justificar: una identidad se comprueba por coeficientes, una división por reconstrucción y cota del resto, y un máximo común divisor por las divisiones que lo producen.

Trabajaremos principalmente con coeficientes racionales o reales. La letra $K$ designará uno de esos dos conjuntos, $\mathbb Q$ o $\mathbb R$, fijo durante cada argumento. Ambos permiten dividir por cualquier coeficiente no nulo. No es una condición decorativa: veremos qué falla cuando se exigen coeficientes enteros.

## [§24.1](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s01) Polinomios como objetos formales {#apm-c24-s01}

¿Qué estamos comparando al escribir $x^2+2x+1=(x+1)^2$? No basta comprobar la igualdad para un valor de $x$. Estamos afirmando que, después de efectuar las operaciones, los coeficientes de cada potencia coinciden.

Un **polinomio formal con coeficientes en $K$** es una sucesión $(a_0,a_1,a_2,\ldots)$ de elementos de $K$ en la que solo hay un número finito de coeficientes no nulos. Lo escribimos como

$$
P(x)=a_0+a_1x+\cdots+a_nx^n.
$$

Aquí $x$ es una indeterminada: organiza los coeficientes, y todavía no representa un número elegido. Las potencias tienen exponentes enteros no negativos. Escribir ceros al final no cambia el polinomio; $3+2x$ y $3+2x+0x^2$ representan la misma sucesión. El conjunto de estos objetos se denota $K[x]$.

Dos polinomios son iguales si y solo si tienen el mismo coeficiente en cada posición, completando con ceros cuando sea necesario. Esta es nuestra definición de igualdad formal, no un resultado deducido de sustituir valores. Más adelante asociamos a cada polinomio una función mediante evaluación.

**Contraste.** Las expresiones $x^{-1}+1$ y $\sqrt{x}+2$ no son polinomios en $K[x]$: sus exponentes no cumplen la condición. En cambio, $\sqrt2x^2+1$ pertenece a $\mathbb R[x]$. La restricción afecta a los exponentes de la indeterminada, no a la forma de escribir un coeficiente real.

**Recuperación resuelta.** ¿Son iguales $x^3-x$ y $x^3-x+0x^5$? Sí: sus sucesiones de coeficientes coinciden. ¿Basta que $x^3-x$ y $0$ valgan cero en $x=0$? No: el coeficiente de $x^3$ distingue los objetos. Conserva esta separación entre igualdad formal e igualdad en un punto.



### Identidad formal y coincidencia en puntos

Un polinomio formal es una sucesión finita de coeficientes; su evaluación produce valores. Dos expresiones formales son iguales cuando coinciden sus coeficientes después de operar. **Control resuelto:** $P=x^2$ y $Q=x$ coinciden en $0$ y $1$, pero no son el mismo polinomio: sus coeficientes difieren y en $2$ sus valores son $4$ y $2$. En C25 justificaremos cuántos puntos bastan si se conoce una cota de grado. Por ahora, reconstruir una división significa expandir y comparar todos los coeficientes; unos ensayos numéricos pueden detectar un fallo, pero no reemplazan ese certificado. La función asociada ayuda a interpretar, sin cambiar el criterio formal de igualdad que utilizamos aquí.

## [§24.2](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s02) Coeficientes, grado y polinomio nulo {#apm-c24-s02}

La longitud de una escritura no determina el grado. Primero hay que eliminar los coeficientes finales nulos. Para $P\ne0$, su **grado**, $\deg P$, es el mayor exponente con coeficiente no nulo. Ese coeficiente es el **coeficiente principal**; si vale $1$, el polinomio es **mónico**.

Así, $5x^4-2x+7$ tiene grado $4$ y coeficiente principal $5$. Todo polinomio constante no nulo tiene grado $0$. El polinomio nulo tiene todos sus coeficientes iguales a cero; aquí **no le asignamos grado**. Algunos textos usan $\deg0=-\infty$. Esa convención es posible, pero en este capítulo escribiremos las alternativas que involucran cero explícitamente.

Una familia con parámetros requiere distinguir casos antes de usar el grado. En

$P_t(x)=(t-2)x^3+(t+1)x+3$

el grado es $3$ si $t\ne2$ y es $1$ si $t=2$. No existe un valor de $t$ que anule todo el polinomio, porque el término constante es $3$.

**Recuperación resuelta.** Para $Q_t=(t-1)x^2+(t-1)x$, si $t\ne1$ el grado es $2$; si $t=1$, $Q_t=0$ y su grado no está definido. La frase “el grado baja a cero” sería incorrecta: cero y constante no nula son casos distintos.

La normalización mónica de $P\ne0$ consiste en dividir todos sus coeficientes por el principal. Por ejemplo, $2x^2-4x+6$ se transforma en $x^2-2x+3$. No son polinomios iguales, pero uno es un múltiplo constante no nulo del otro.

## [§24.3](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s03) Suma, resta y comparación de coeficientes {#apm-c24-s03}

La suma se define posición a posición. Si $P=\sum a_kx^k$ y $Q=\sum b_kx^k$, completando con ceros, entonces

$$
P+Q=\sum_k(a_k+b_k)x^k,\qquad
P-Q=\sum_k(a_k-b_k)x^k.
$$

Multiplicar por un escalar $c\in K$ significa reemplazar cada $a_k$ por $ca_k$. Las propiedades asociativa y conmutativa de la suma, y la distributividad escalar, se heredan coeficiente a coeficiente de la aritmética de $K$. No necesitamos adivinarlas a partir de ejemplos.

Si $P,Q$ son no nulos y $P+Q\ne0$, entonces $\deg(P+Q)\le\max(\deg P,\deg Q)$. Por encima de ese máximo ambos coeficientes son cero. Si los grados son distintos, el término principal del polinomio de mayor grado no tiene otro término que lo cancele: la suma tiene ese mismo grado. Si los grados son iguales, puede haber cancelación.

Por ejemplo, $(2x^3-x+4)+(-2x^3+3x^2+x-1)=3x^2+3.$

El grado desciende de $3$ a $2$. La suma de $P$ y $-P$ sería cero, caso en que no hablamos de su grado.

**Comparación resuelta.** Para que $ax^2+(a+b)x+2b=x^2+4x+6$, deben cumplirse simultáneamente $a=1$, $a+b=4$ y $2b=6$. Las tres condiciones son compatibles y dan $(a,b)=(1,3)$. Resolver solo una igualdad de valores dejaría información sin usar.

**Recuperación resuelta.** Si $P$ tiene grado $5$ y $Q$ grado $2$, ¿puede $P-Q$ tener grado $1$? No: el coeficiente principal de $P$ permanece intacto. En una suma, identifica primero qué términos tienen posibilidad real de cancelarse.

## [§24.4](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s04) Producto y grado {#apm-c24-s04}

El producto combina exponentes y luego reúne los términos con el mismo exponente. Su coeficiente de $x^k$ es

$$
c_k=\sum_{i=0}^{k}a_i b_{k-i}.
$$

Solo intervienen coeficientes de las sucesiones originales. Esta fórmula expresa la distributividad de las sumas finitas: cada par $a_ix^i$, $b_jx^j$ aporta $a_ib_jx^{i+j}$.

Si $P,Q\ne0$, de grados $n,m$, el coeficiente de $x^{n+m}$ en $PQ$ es exactamente $a_nb_m$. Los demás pares con suma $n+m$ tienen un índice fuera de los grados posibles y aportan cero. Como el producto de dos racionales o reales no nulos no es cero, obtenemos

$$
PQ\ne0,\qquad \deg(PQ)=\deg P+\deg Q.
$$

Esta es una prueba; comprobar diez productos no sustituiría el argumento para todos ellos.

**Ejemplo.** Al multiplicar $P=x^2-2x+3$ y $Q=2x+1$,

$PQ=2x^3-3x^2+4x+3.$

El resultado tiene grado $3=2+1$ y coeficiente principal $2=1\cdot2$. Ambas comprobaciones detectan algunos errores, pero no garantizan por sí solas que los coeficientes intermedios estén bien: hay que conservar el cálculo completo.

**Recuperación resuelta.** ¿Puede el producto de dos polinomios cuadráticos no nulos tener grado $3$ en $\mathbb R[x]$? No: debe tener grado $4$. El argumento depende de que los coeficientes principales no nulos tengan producto no nulo; no debe exportarse sin comprobar esa propiedad a cualquier aritmética modular.



### La hipótesis que protege el coeficiente principal

El término de mayor grado de $PQ$ tiene coeficiente $a_nb_m$, donde ambos factores son no nulos. En $\mathbb Q$ y $\mathbb R$ su producto sigue siendo no nulo; eso demuestra la suma de grados. **Diagnóstico resuelto:** con aritmética módulo $6$, $(2x)(3x)=0$, aunque los dos polinomios iniciales sean no nulos. La aritmética modular de C17 permite comprobar $2\cdot3\equiv0$. No se trata de una excepción dentro de los cuerpos elegidos, sino de una hipótesis perdida al exportar el argumento. Antes de usar la regla del grado, hay que fijar los coeficientes y excluir el polinomio cero. Tampoco basta acertar el coeficiente principal para certificar todos los demás términos de un producto.

## [§24.5](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s05) Cancelación e inversos polinómicos {#apm-c24-s05}

Si $A\ne0$ y $AB=AC$, la distributividad da $A(B-C)=0$. Si $B-C$ fuera no nulo, el resultado anterior impediría que su producto por $A$ fuera cero. Por tanto $B=C$. Hemos probado la **cancelación de un factor polinómico no nulo**.

Esta cancelación es una propiedad de objetos formales. No exige dividir numéricamente por $A(t)$ en cada punto, operación que podría fallar cuando $A(t)=0$. Por ejemplo, de $(x-1)B=(x-1)C$ se concluye $B=C$ aunque al evaluar en $1$ la igualdad original solo diga $0=0$.

¿Cuándo existe $Q\in K[x]$ con $PQ=1$? Tanto $P$ como $Q$ deben ser no nulos. La fórmula del grado exige $\deg P+\deg Q=0$, de modo que ambos son constantes. Recíprocamente, una constante $c\ne0$ tiene el inverso constante $1/c$. Así, **los únicos polinomios con inverso polinómico son las constantes no nulas**.

**Recuperación resuelta.** $x+1$ no tiene inverso en $\mathbb Q[x]$. La expresión $1/(x+1)$ sirve como función racional donde esté definida, pero no es un polinomio. La cancelación y la existencia de inversos son afirmaciones distintas: la primera no implica la segunda.

Esta distinción prepara la división con resto. No intentaremos fabricar un inverso polinómico para cada divisor; construiremos un cociente y un resto.

## [§24.6](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s06) Evaluación y composición {#apm-c24-s06}

Evaluar $P$ en $a\in K$ significa calcular $P(a)=\sum a_ka^k$. En esta evaluación, la potencia formal $x^0=1$ aporta siempre el término constante $a_0$, también cuando $a=0$: la notación abrevia $a_0+\sum_{k\ge1}a_ka^k$, con solo finitísimos términos no nulos. No requiere evaluar un radical ni un límite escrito como $0^0$. De las propiedades de las sumas finitas se deduce

$$
(P+Q)(a)=P(a)+Q(a),\qquad (PQ)(a)=P(a)Q(a).
$$

Para el producto, al evaluar la suma de los términos $a_ib_jx^{i+j}$ obtenemos $\sum_{i,j}a_ib_ja^{i+j}=(\sum_i a_ia^i)(\sum_j b_ja^j)$. Esa igualdad explica por qué una identidad formal conserva su validez al evaluar.

La **composición** $P\circ Q$ se obtiene reemplazando cada $x^k$ de $P$ por $Q(x)^k$. Si $P=x^2+1$ y $Q=x-2$, entonces $(P\circ Q)(x)=x^2-4x+5$, mientras que $(Q\circ P)(x)=x^2-1$. La composición no es conmutativa.

Si $P$ tiene grado $n\ge1$ y $Q$ grado $m\ge1$, el término $a_nQ^n$ tiene grado $nm$ y coeficiente principal $a_nb_m^n\ne0$. Los términos $a_kQ^k$ con $k<n$ tienen grado menor cuando son no nulos. Por tanto $\deg(P\circ Q)=nm$. Las composiciones con constantes se analizan aparte: por ejemplo, $P\circ0$ puede ser cero.

**Recuperación resuelta.** Para $P=x^2-1$, $P(1)=0$, pero $P\ne0$. Evaluar una identidad es válido; inferir una identidad de una coincidencia en un punto no lo es. La relación entre suficientes puntos distintos y la igualdad formal se justificará en C25.

## [§24.7](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s07) División con resto: enunciado y condiciones {#apm-c24-s07}

Sean $P,D\in K[x]$ y $D\ne0$. Existen únicos $Q,R\in K[x]$ tales que

$$
P=DQ+R,\qquad R=0\ \text{o}\ \deg R<\deg D.
$$

$P$ es el dividendo, $D$ el divisor, $Q$ el cociente y $R$ el resto. La segunda condición es indispensable: sin ella, $Q+1$ y $R-D$ darían otra descomposición del mismo $P$.

Si $P=0$, sirven $Q=R=0$. Si $P\ne0$ y su grado es menor que el del divisor, sirven $Q=0$, $R=P$. Si $D=c$ es una constante no nula, $Q=P/c$ y $R=0$; ningún resto no nulo tiene grado menor que $0$.

**Límite del dominio.** En $\mathbb Z[x]$, dividir $x$ por $2$ con resto cero exigiría $Q=x/2$, que no tiene coeficientes enteros. La división euclídea de este enunciado no vale para todo divisor en $\mathbb Z[x]$. Si el divisor es mónico, el procedimiento sí permanece en los enteros: al cancelar el coeficiente principal solo se divide por $1$.

**Recuperación resuelta.** Al dividir $x+2$ por $x^2+1$, ¿se debe seguir hasta obtener una constante? No: el resto $x+2$ ya tiene grado menor que $2$. El criterio de parada depende del divisor, no de un grado fijo que deba tener todo resto.

## [§24.8](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s08) División larga y verificación {#apm-c24-s08}

Dividamos $P=2x^4-3x^2+x-5$ por $D=x^2-1$. Es útil escribir $0x^3$ y organizar las restas por potencias.

El primer término del cociente es $2x^2$, porque cancela $2x^4$. Restamos $2x^2D=2x^4-2x^2$ y obtenemos $-x^2+x-5$. El siguiente término es $-1$. Restamos $-D=-x^2+1$ y queda $x-6$. Este resto tiene grado $1<2$, así que terminamos: $Q=2x^2-1,\qquad R=x-6.$

La verificación reconstruye el dividendo completo:

$$
(x^2-1)(2x^2-1)+(x-6)=2x^4-3x^2+x-5.
$$

Si el divisor no es mónico, dividimos los coeficientes principales. Para $P=x^2+1$ y $D=2x-1$, el primer término es $x/2$; queda $x/2+1$. El siguiente es $1/4$; queda $5/4$. Por tanto $Q=x/2+1/4$ y $R=5/4$.

**Recuperación resuelta.** Para $P=x^3+2x+1$ y $D=x^2+1$, el término $x$ deja el resto $x+1$. La identidad $P=xD+(x+1)$ y la cota $1<2$ verifican la respuesta. Si se omite el coeficiente cero de $x^2$, hay riesgo de desplazar los demás coeficientes en una tabla; los ceros no son pasos inútiles, conservan las posiciones.

Una sustitución numérica puede detectar un error en una división, pero la certificación usa la identidad formal y la cota del resto.



### Tres obligaciones en una división

Un certificado de división contiene $P=DQ+R$, $D\ne0$ y $R=0$ o $\deg R<\deg D$. La identidad sola no fija un cociente: de $P=DQ+R$ se obtiene también $P=D(Q+H)+(R-DH)$. La cota selecciona el único par válido. **Control resuelto:** $x^2=(x+1)x-x$ es identidad, pero $-x$ no es resto válido para un divisor lineal. Reparar da $x^2=(x+1)(x-1)+1$. En el algoritmo, cada resta cancela el término principal del residual y baja estrictamente su grado, hasta cero o un grado menor que el del divisor. Esta disminución demuestra terminación; verificar solo el último renglón no explica por qué el proceso pudo detenerse.

## [§24.9](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s09) Existencia del cociente y del resto {#apm-c24-s09}

Ahora probamos que el procedimiento siempre funciona. El caso $P=0$ ya está resuelto. Para $P\ne0$, fijamos el divisor $D$, de grado $m$, y usamos inducción fuerte en $n=\deg P$.

Si $n<m$, tomamos $Q=0$, $R=P$. Si $n\ge m$, sean $a$ y $b\ne0$ los coeficientes principales de $P$ y $D$. Construimos

$$
T=\frac ab x^{n-m},\qquad P_1=P-TD.
$$

El coeficiente de $x^n$ de $P_1$ es $a-(a/b)b=0$, y no aparecen potencias superiores. Entonces $P_1=0$ o $\deg P_1<n$. En el primer caso $P=TD+0$. En el segundo, la hipótesis de inducción da $P_1=DQ_1+R$ con resto admisible. Sustituyendo, $P=D(Q_1+T)+R$. Esto completa la existencia.

El mismo argumento explica la terminación operativa. En cada paso, el resto parcial o se vuelve cero o pierde grado. No hay una sucesión infinita estrictamente decreciente de enteros no negativos. Durante el proceso se mantiene la identidad **dividendo = divisor por cociente acumulado + resto parcial**. Esa identidad es el invariante que permite reconstruir el resultado.

**Recuperación resuelta.** ¿Por qué no basta afirmar que “en cada paso baja un coeficiente”? Porque una medida de terminación debe descender de forma controlada. Aquí desciende el grado, no el valor numérico de los coeficientes. También se explica por qué podemos efectuar el paso: $b$ tiene inverso en $K$.

## [§24.10](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s10) Unicidad de la división {#apm-c24-s10}

Supongamos dos divisiones admisibles:

$P=DQ_1+R_1=DQ_2+R_2.$

Entonces $D(Q_1-Q_2)=R_2-R_1$. Si $Q_1-Q_2\ne0$, el miembro izquierdo es no nulo y tiene grado al menos $\deg D$. El miembro derecho es cero o tiene grado menor que $\deg D$, pues cada resto solo contiene potencias menores que ese grado. Ninguna opción permite la igualdad. Así, $Q_1=Q_2$, y la misma ecuación da $R_1=R_2$.

Para un divisor constante, los dos restos admisibles son necesariamente cero; la cancelación da directamente la igualdad de cocientes. Esto evita hablar del grado de un resto nulo.

**Diagnóstico resuelto.** La identidad $x^2+1=(x+1)(x-1)+2$ tiene resto admisible. También es cierto que $x^2+1=(x+1)x+(1-x)$, pero el resto de esta segunda expresión tiene grado $1$, igual al del divisor. No contradice la unicidad: no es una división con resto admisible.

**Recuperación resuelta.** Si una división larga y otra sintética dan restos diferentes para el mismo divisor, ¿pueden ser ambas correctas? No, siempre que ambas reconstruyan el dividendo y satisfagan la cota. La unicidad convierte esas dos verificaciones en un certificado, independiente del método usado.

## [§24.11](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s11) División lineal, Horner y teorema del resto {#apm-c24-s11}

Dividir por $x-c$ deja un resto constante, incluido el cero. De $P=(x-c)Q+r$, al evaluar en $c$ obtenemos $P(c)=r$. Este es el **teorema del resto**; no requiere conocer ni buscar todas las raíces de $P$.

Para $P=a_nx^n+\cdots+a_0$, con $n\ge1$, podemos construir el cociente mediante la recurrencia

$$
b_{n-1}=a_n,\qquad
b_{k-1}=a_k+cb_k\quad(k=n-1,\ldots,1),\qquad
r=a_0+cb_0.
$$

El cociente es $Q=b_{n-1}x^{n-1}+\cdots+b_0$. En $(x-c)Q+r$, el coeficiente de $x^n$ es $b_{n-1}=a_n$; el de $x^k$ es $b_{k-1}-cb_k=a_k$ para $1\le k<n$; el constante es $r-cb_0=a_0$. Por comparación de coeficientes queda probada la fórmula de Horner o división sintética.

**Ejemplo.** Para $P=2x^3+0x^2-3x+4$ y $c=2$, obtenemos $b_2=2$, $b_1=4$, $b_0=5$ y $r=14$. Así, $Q=2x^2+4x+5$. La evaluación directa $P(2)=16-6+4=14$ confirma el resto.

Si el divisor es $ax-b$, con $a\ne0$, se escribe $a(x-b/a)$. Horner con $c=b/a$ da el cociente para $x-c$; el cociente para $ax-b$ es ese cociente dividido por $a$. El resto no cambia.

**Recuperación resuelta.** Para dividir $x^2+1$ por $2x-1$, Horner con $c=1/2$ da cociente $x+1/2$ para $x-1/2$ y resto $5/4$. El cociente buscado es $x/2+1/4$. No se puede usar la tabla como si el divisor original fuera mónico.

## [§24.12](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s12) Divisibilidad polinómica {#apm-c24-s12}

Escribimos $D\mid P$ si existe $Q\in K[x]$ con $P=DQ$. Para $D\ne0$, el teorema de división muestra que esto equivale a tener resto cero. Cada polinomio divide a cero; cero solo divide a cero. Una constante no nula divide a cualquier polinomio de $K[x]$.

Si $D\mid P$ y $D\mid S$, escribimos $P=DU$, $S=DV$. Para cualesquiera polinomios $A,B$,

$AP+BS=D(AU+BV),$

de modo que $D\mid(AP+BS)$. Además, si $D\mid P$ y $P\mid S$, la sustitución de las dos factorizaciones prueba $D\mid S$.

Si $D,P\ne0$ y $D\mid P$, el cociente es no nulo, por lo que $\deg D\le\deg P$. Si ambos se dividen mutuamente, sus grados coinciden y los cocientes son constantes no nulas: uno es un múltiplo escalar del otro. A estos polinomios se les llama **asociados**.

**Contraste.** La divisibilidad depende del conjunto de coeficientes: $2x\mid x$ en $\mathbb Q[x]$, mediante el cociente $1/2$, pero no en $\mathbb Z[x]$.

**Recuperación resuelta.** Si $D\mid P$ y $D\mid(P+S)$, entonces $D\mid S$, porque $S=(P+S)-P$. En cambio, que $P(a)$ sea múltiplo numérico de $D(a)$ en un punto no ofrece una factorización formal de $P$. La divisibilidad se certifica con un cociente polinómico.

## [§24.13](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s13) Cálculo con restos {#apm-c24-s13}

Fijemos un divisor no nulo $D$ de grado al menos $1$. Denotemos por $\operatorname{rem}_D(P)$ su resto único. También escribimos $P\equiv S\pmod D$ si $D\mid(P-S)$.

Esta congruencia es reflexiva, simétrica y transitiva: las diferencias $P-P=0$, $S-P=-(P-S)$ y $P-T=(P-S)+(S-T)$ preservan la divisibilidad. Además, si $P\equiv P_0$ y $S\equiv S_0$, entonces sus sumas son congruentes y sus productos también, porque

$$
PS-P_0S_0=(P-P_0)S+P_0(S-S_0).
$$

Cada término de la derecha es divisible por $D$. Así, podemos reducir antes de sumar o multiplicar, pero debemos reducir otra vez si el resultado aún tiene grado demasiado grande. Por unicidad, dos polinomios congruentes tienen el mismo resto.

**Ejemplo.** Módulo $D=x^2+1$ se tiene $x^2\equiv-1$, por lo que $x^4\equiv1$ y

$x^7+2x^4-x\equiv -x+2-x=2-2x.$

El resultado ya tiene grado menor que $2$ y es el resto. La reducción evita una división larga de grado siete.

**Recuperación resuelta.** Para $D=x^2-x-1$, se tiene $x^2\equiv x+1$ y $x^3\equiv x(x+1)\equiv2x+1$. Entonces el resto de $x^3-2x-1$ es cero. No hace falta encontrar los valores que anulan $D$; el argumento ocurre enteramente entre polinomios.

## [§24.14](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s14) Algoritmo de Euclides y máximo común divisor {#apm-c24-s14}

Para $P,S$ no ambos nulos, un **máximo común divisor** $G$ es un polinomio que divide a ambos y al que divide todo divisor común. “Máximo” expresa esta propiedad de divisibilidad, no una comparación del tamaño de los coeficientes. Elegiremos $G$ mónico para eliminar la ambigüedad por factores constantes.

Si $P=SQ+R$, un polinomio divide a $P$ y $S$ si y solo si divide a $S$ y $R$: una dirección usa $R=P-SQ$; la otra, $P=SQ+R$. Dividimos sucesivamente

$$
P=SQ_1+R_1,\quad
S=R_1Q_2+R_2,\quad
R_1=R_2Q_3+R_3,\quad\ldots
$$

hasta un resto cero. Los grados de los restos no nulos descienden estrictamente, así que el proceso termina. En la última pareja $(L,0)$, los divisores comunes son exactamente los divisores de $L$. La equivalencia anterior, repetida hacia atrás, muestra que $L$ es un MCD de la pareja inicial. Dividir $L$ por su coeficiente principal da el MCD mónico.

Si dos MCD mónicos $G,H$ existieran, cada uno dividiría al otro; serían asociados. Como sus coeficientes principales son $1$, el factor escalar sería $1$. Luego $G=H$.

**Ejemplo.** Para $P=x^3-x$ y $S=x^2-1$, la primera división da $P=xS+0$. El MCD mónico es $x^2-1$. Si uno de los polinomios es cero y el otro $P\ne0$, el MCD es la normalización mónica de $P$. Para $(0,0)$ no adoptamos un MCD mónico: no hay uno que satisfaga la definición.

**Recuperación resuelta.** En $P=x^2+1$, $S=x+1$, el resto inicial es $2$, y dividir $S$ por $2$ deja cero. El MCD mónico es $1$, no $2$. La normalización es parte de la respuesta acordada.



### Lo que Euclides conserva y lo que la normalización elige

Si $P=DQ+R$, un polinomio divide a $P,D$ exactamente cuando divide a $D,R$: en una dirección restamos $DQ$, en la otra sumamos $DQ$. Esta equivalencia conserva el conjunto de divisores comunes en cada paso de Euclides. El último resto no nulo determina el MCD salvo una constante no nula; hacerlo mónico elige un representante único. **Control resuelto:** si el último resto es $6(x-2)$, el MCD mónico es $x-2$. Dividir por seis no cambia sus divisores ni su propiedad universal. Para certificar un MCD propuesto, comprobamos que divide ambos polinomios y damos una combinación $UP+VD=G$: todo divisor común debe dividir entonces a $G$. No basta presentar solo un factor compartido.

## [§24.15](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s15) Identidad de Bézout y coprimalidad {#apm-c24-s15}

El algoritmo también produce un certificado: $G=UP+VS$

para ciertos $U,V\in K[x]$, donde $G$ es el MCD mónico. En efecto, $P$ y $S$ ya son combinaciones de sí mismos. Si dos restos consecutivos lo son, su diferencia después de multiplicar uno por el cociente vuelve a serlo. Por inducción, el último resto no nulo es una combinación de $P,S$; la normalización mónica multiplica esa combinación por una constante. Esto prueba la existencia de la **identidad de Bézout**.

**Ejemplo con sustitución hacia atrás.** Sean $P=x^3+2x+1$ y $S=x^2+1$. Las divisiones son

$$
P=xS+(x+1),\qquad
S=(x-1)(x+1)+2.
$$

El MCD mónico es $1$. Sustituyendo $x+1=P-xS$ en la segunda igualdad,

$$
1=\frac{1-x}{2}P+\frac{x^2-x+1}{2}S.
$$

No basta anunciar que el MCD vale $1$: esta identidad permite comprobarlo multiplicando. Cualquier divisor común divide al miembro derecho y por tanto divide a $1$.

Decimos que $P,S$ son **coprimos** si su MCD mónico es $1$. Si $A,B$ son coprimos y $A\mid BC$, Bézout da $UA+VB=1$. Multiplicamos por $C$: $C=UAC+VBC$. Ambos sumandos son divisibles por $A$, de modo que $A\mid C$. Esta cancelación de divisibilidad necesita la hipótesis de coprimalidad.

**Recuperación resuelta.** Sin esa hipótesis, con $A=B=x$ y $C=1$ tenemos $A\mid BC$, pero $A\nmid C$. La ley no autoriza a “tachar” un factor común de cualquier afirmación de divisibilidad.

## [§24.16](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s16) Parámetros, síntesis y enlace con C25 {#apm-c24-s16}

Una condición sobre un resto suele transformarse en una ecuación. Para una división lineal podemos evaluar; para un divisor de mayor grado usamos reducción o comparación de coeficientes. Si aparecen parámetros en el divisor, antes comprobamos cuándo es no nulo y cuándo cambia su grado.

**Problema de síntesis resuelto.** Sea $P_t=x^3+tx+2$. Hallar $t$ para que, al dividir por $x-1$, el resto sea $5$, y obtener el cociente. Por el teorema del resto, $P_t(1)=t+3=5$, de donde $t=2$. Horner con coeficientes $1,0,2,2$ y $c=1$ produce el cociente $x^2+x+3$ y el resto $5$. La comprobación final es

$(x-1)(x^2+x+3)+5=x^3+2x+2.$

Se han satisfecho la condición numérica, la identidad formal y la cota del resto.

**Caso excepcional resuelto.** Si el divisor es $D_t=(t-1)x+2$, para $t\ne1$ podemos tratarlo como un divisor lineal no mónico. Para $t=1$ es la constante $2$ y el resto de cualquier división en $K[x]$ debe ser cero. Aplicar una tabla con $c=-2/(t-1)$ en ese caso introduciría una división por cero.

La identidad $P=DQ+R$ puede convertirse en $P(a)/D(a)=Q(a)+R(a)/D(a)$ solamente para los valores con $D(a)\ne0$. La identidad formal original no tiene esa restricción; el paso a cocientes numéricos sí.

**Recuperación resuelta.** Para $P=x^2-1$ y $D=x-1$, el cociente polinómico es $x+1$ y el resto es cero. La función $(a^2-1)/(a-1)$ coincide con $a+1$ cuando $a\ne1$; la cancelación no asigna por sí sola un valor al cociente original en $a=1$.

El capítulo deja disponibles tres certificaciones: igualdad por coeficientes; división por identidad y cota del resto; MCD por Euclides y Bézout. En C25 estudiaremos qué información adicional proporciona la anulación de un polinomio, cómo se relaciona con sus factores y cómo interviene el conjunto de coeficientes en la factorización.

## Ejercicios

Todos los coeficientes son racionales o reales según se indique. Si se utiliza $K$, designa uno de los conjuntos $\mathbb Q$ o $\mathbb R$. Justifica las respuestas; el polinomio cero no tiene grado en la convención del capítulo. Las soluciones se reúnen después del banco para permitir un intento autónomo.

### Lectura formal y grado



**1. Reconocer el objeto.** Clasifica $3x^2-\sqrt2x+1$, $x^{-2}+3$ y $5$ según pertenezcan a $\mathbb Q[x]$, a $\mathbb R[x]$ o a ninguno.



**2. Ceros finales.** Escribe la sucesión de coeficientes de $P=4-3x^2+0x^5$. Determina su grado y compárala con la de $Q=4-3x^2$.



**3. Una familia que se anula.** Determina el grado de $P_t=(t^2-1)x^3+(t-1)x+2(t-1)$ para todos los valores reales de $t$.



**4. Coeficientes y posiciones.** En $P=7x^4-2x+9$, identifica $a_0,a_1,a_2,a_3,a_4,a_6$ y el coeficiente principal.



**5. Normalizar.** Obtén la normalización mónica de $-3x^3+6x-9$ y explica si es igual al polinomio inicial.



**6. Grados desiguales.** Sean $P,Q\in\mathbb R[x]$ de grados $7$ y $4$. Sin conocer sus coeficientes, determina los grados de $P+Q$ y $PQ$.



**7. Cancelar un factor.** De $(x^2+1)A=(x^2+1)(2x-3)$ en $\mathbb Q[x]$, determina $A$ y justifica la cancelación.



**8. Una comprobación insuficiente.** Un estudiante evalúa $x^2$ y $x$ en $0$ y $1$ y concluye que son iguales. Audita su conclusión.



**9. Grado de una potencia.** Si $P\ne0$ tiene grado $3$, determina el grado de $P^4$ y explica por qué no es $3^4$.



**10. Inversos.** Decide cuáles de $0$, $-5$ y $x^2+1$ tienen inverso en $\mathbb Q[x]$.

### Operaciones, evaluación y composición



**11. Suma organizada.** Calcula $(3x^3-2x^2+4)+( -x^3+2x^2+5x-7)$ y determina el grado.



**12. Resta con signos.** Calcula $(2x^4-x^2+3x-1)-(x^4+2x^2-x+5)$.



**13. Combinación lineal.** Para $P=x^2-2x+1$ y $Q=2x^2+x-3$, calcula $2P-Q$.



**14. Producto completo.** Multiplica $(x^2+x-2)(x-3)$.



**15. Producto con huecos.** Calcula $(2x^3-1)(x^2+2)$ y especifica el coeficiente de $x^4$.



**16. Un coeficiente sin expandir todo.** Obtén el coeficiente de $x^3$ en $(1+2x-x^2+3x^3)(2-x+4x^2)$.



**17. Cuadrado.** Desarrolla $(x^2-2x+2)^2$.



**18. Producto telescópico.** Demuestra por distributividad $(x-1)(1+x+\cdots+x^{n-1})=x^n-1$ para todo entero $n\ge1$.



**19. Evaluación exacta.** Para $P=3x^3-2x^2+x-4$, calcula $P(-2)$ y $P(1/2)$.



**20. Evaluar con Horner.** Evalúa $P=2x^4-3x^2+5x-1$ en $x=-1$ mediante Horner.



**21. Dos composiciones.** Para $P=x^2-2$ y $Q=2x+1$, calcula $P\circ Q$ y $Q\circ P$.



**22. Composición con una constante.** Con $P=x^2-4$ y el polinomio constante $C=2$, calcula $P\circ C$ y $C\circ P$, y trata sus grados.



**23. Identidad con parámetros.** Determina $a,b,c$ para que $(ax+b)(x+2)+c=2x^2+3x+5$.



**24. Factor desconocido.** Encuentra $u,v$ si $(x-2)(ux+v)=3x^2-7x+2$.



**25. Trasladar una indeterminada.** Para $P=x^2+3x+1$, desarrolla $P(x+1)-P(x)$ y determina su grado.



**26. Grado de una composición.** Sin desarrollar, determina el grado y el principal de $P(Q(x))$ si $P=3x^4-x+1$ y $Q=2x^3+x^2-5$.

### División larga y división lineal



**27. División cuadrática.** Divide $x^4+x^3-2x^2+3x-1$ por $x^2+x+1$.



**28. División lineal con signos.** Divide $2x^3+3x^2-x+5$ por $x+2$.



**29. Un resto constante con divisor cuadrático.** Divide $x^4+1$ por $x^2+2$.



**30. Divisor no mónico.** Divide $3x^3-x^2+4x-2$ por $2x^2+1$ en $\mathbb Q[x]$.



**31. Resto negativo.** Divide $x^3-4x+1$ por $x-1$.



**32. Horner y escala.** Divide $2x^3+x^2-5x+4$ por $2x+1$.



**33. Dividendo de menor grado.** Divide $3x-2$ por $x^3+x+1$. Explica el criterio de parada.



**34. División por una constante.** Divide $6x^2-3x+9$ por $-3$ en $\mathbb Q[x]$.



**35. Dividendo cero.** Divide el polinomio nulo por $x^2-5$ y justifica la respuesta sin atribuir grado a cero.



**36. División dentro de los enteros.** Divide $x^3+2x+1$ por $x^2+x$ y explica por qué el resultado está en $\mathbb Z[x]$.



**37. Reconstrucción hacia atrás.** Una división tiene divisor $x^2-2$, cociente $2x+3$ y resto $x-1$. Encuentra el dividendo y comprueba que el dato del resto es admisible.



**38. Identidad que todavía necesita reducirse.** Se propone $x^3=(x^2+1)(x-1)+(x^2-x+1)$ como división. Decide si es admisible y corrígela.

### Demostraciones y diagnóstico



**39. Cancelación del término principal.** Para $P,Q$ no nulos de igual grado $n$, demuestra que $P+Q$ es cero o tiene grado menor que $n$ si y solo si sus coeficientes principales suman cero.



**40. Dónde falla la ley del grado.** En la aritmética de coeficientes módulo $4$, calcula $(2x)(2x)$ y explica qué hipótesis de la prueba de [§24.4](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md#apm-c24-s04) falla.



**41. Divisor mónico entero.** Justifica que dividir $P\in\mathbb Z[x]$ por un divisor mónico no nulo $D\in\mathbb Z[x]$ produce cociente y resto enteros.



**42. Una cancelación numérica inválida.** Se intenta justificar que $(x-2)A=(x-2)B$ implica $A=B$ “dividiendo por $x-2$ para cada real $x$”. Señala la falla y da una prueba formal válida.



**43. Cambiar el dividendo por un múltiplo.** Si $P=DQ+R$ es una división admisible y $T\in K[x]$, encuentra la división de $P+DT$ por $D$.



**44. Grado del cociente.** Demuestra que, si $P,D\ne0$ y $\deg P\ge\deg D$, el cociente de su división es no nulo y tiene grado $\deg P-\deg D$.



**45. Qué exige un resto lineal.** Un alumno afirma que “en toda división el resto es una constante”. Refútalo y formula la afirmación correcta.



**46. Multiplicar restos y volver a reducir.** Módulo $x^2+1$, los restos de $x$ y $x$ son $x$. ¿Es $x^2$ el resto de su producto? Corrige el razonamiento.



**47. Distributividad en composición.** Prueba $(P+Q)\circ S=(P\circ S)+(Q\circ S)$ y decide si siempre $P\circ(Q+S)=(P\circ Q)+(P\circ S)$.



**48. Por qué se excluye el divisor cero.** Explica qué falla al pedir una división por el polinomio cero, incluso cuando el dividendo es cero.



**49. El factor de normalización.** Si $G$ es un MCD no nulo de $P,S$ y $c\in K$ es no nulo, prueba que $cG$ también es MCD. Explica por qué se exige que el MCD canónico sea mónico.



**50. Evaluar no certifica un MCD.** Un alumno concluye que $\gcd(x,x^2+1)=x$ porque $x(0)=0$. Diagnostica y calcula el MCD correcto.

### Restos y parámetros



**51. Una potencia grande.** Encuentra el resto de $x^{100}+3x^{99}-2$ al dividir por $x^2+1$.



**52. Reducir por recurrencia.** Calcula el resto de $x^6$ módulo $x^2-x-1$.



**53. Divisibilidad sin raíces complejas.** Para enteros $r,s,t\ge0$, demuestra que $x^{3r+2}+2x^{3s+1}+x^{3t}-x$ es divisible por $x^2+x+1$.



**54. Resto cuadrático prescrito.** Encuentra $a,b\in\mathbb R$ para que el resto de $x^3+ax^2+bx+1$ por $x^2+1$ sea $x+2$.



**55. Resto y valor del cociente.** Al dividir $P=ax^3+bx^2+2x+1$ por $x-1$, el resto es $4$ y el cociente satisface $Q(2)=7$. Encuentra $a,b$.



**56. El divisor cambia de grado.** Para $P=x^2-1$, determina el resto al dividir por $D_t=(t-2)x+1$ para todo real $t$.



**57. Toda una familia divisible.** Determina todos los pares $(a,b)$ para los que $x^4+ax^2+b$ es divisible por $x^2+1$, y da el cociente.



**58. Paridad de exponentes.** Obtén el resto de $x^{2025}+1$ por $x^2-1$.



**59. Dos restos lineales.** Encuentra $a,b$ si $P=x^3+ax+b$ deja resto $3$ al dividir por $x-1$ y resto $1$ al dividir por $x+1$.



**60. Reconstruir un resto a partir de valores.** Si $P(1)=5$ y $P(-1)=1$, determina el resto de $P$ por $x^2-1$, sin conocer el grado de $P$.

### Euclides y Bézout



**61. Euclides: un resto lineal.** Calcula el MCD mónico de $P=x^3-1$ y $S=x^2-1$.



**62. Grados mayores con la misma estrategia.** Calcula el MCD mónico de $x^4-1$ y $x^3-1$.



**63. Bézout con resto uno.** Calcula el MCD de $P=x^2+2x+2$ y $S=x+1$, y una identidad de Bézout para su representante mónico.



**64. Normalizar una constante final.** Calcula el MCD y una identidad de Bézout de $P=x^3+x+2$ y $S=x^2+1$.



**65. Factores escalares distintos.** Calcula el MCD mónico de $2x^2-2$ y $3x-3$.



**66. Un argumento cero.** Determina el MCD mónico de $0$ y $4x^2+2x$, y una identidad de Bézout.



**67. Auditar un certificado.** Se propone $1=x^2-(x-1)(x+1)$ como certificado de coprimalidad de $x^2$ y $x+1$. Verifícalo y extrae el MCD.



**68. Cancelar divisibilidad coprima.** Si $A=x^2+1$, $B=x$ y $A\mid BC$, demuestra que $A\mid C$ sin factorizar $A$.



**69. Producto de divisores coprimos.** Si $A,B$ son no nulos y coprimos, y ambos dividen a $P$, prueba que $AB\mid P$.



**70. Describir todos los certificados.** Para $P=x^2$, $S=x+1$, una pareja de Bézout es $(U_0,V_0)=(1,1-x)$. Demuestra que todas las parejas que satisfacen $UP+VS=1$ son $U=1+(x+1)T$, $V=1-x-x^2T$ con $T\in K[x]$.



**71. MCD y un parámetro constante.** Determina el MCD mónico de $x^2+1$ y $x^2+t$ para cada real $t$.



**72. Certificado con MCD no constante.** Para $P=x^3-x$ y $S=x^2+x$, calcula el MCD mónico y justifícalo mediante una combinación de $P,S$.

### Problemas de síntesis



**73. Dos divisiones simultáneas.** Encuentra todos los $P\in K[x]$ cuyo resto por $A=x^2+1$ es $x$ y cuyo resto por $B=x^2-x+1$ es $1$. Determina el único de grado menor que $4$ y justifica la unicidad.



**74. Euclides con bifurcaciones.** Determina, para cada real $t$, el MCD mónico de $P=x^3-2x+1$ y $S_t=x^2+t$. No utilices una factorización completa de $P$.



**75. Una recurrencia y una identidad de enteros.** Define $f_0=0$, $f_1=1$, $f_{n+1}=f_n+f_{n-1}$ para $n\ge1$. Demuestra que el resto de $x^n$ por $D=x^2-x-1$ es $f_nx+f_{n-1}$ para $n\ge1$. Deducir, para $m,n\ge1$, la identidad $f_{m+n}=f_mf_{n+1}+f_{m-1}f_n$.



**76. Euclides en los exponentes.** Demuestra que para enteros positivos $m,n$ el MCD mónico de $x^m-1$ y $x^n-1$ es $x^d-1$, donde $d=\gcd(m,n)$ es el MCD entero.



**77. Certificados con grados acotados.** Sean $A,B\in K[x]$ coprimos, de grados $a,b\ge1$. Prueba que existe una única pareja $U,V$ con $UA+VB=1$, donde $U=0$ o $\deg U<b$, y $V=0$ o $\deg V<a$.



**78. Invertir un resto mediante Euclides.** Para $D=x^3+x+1$ y $A=x^2+1$, encuentra un polinomio $H$ de grado menor que $3$ tal que $AH\equiv1\pmod D$. Explica por qué es único entre los de ese grado y cómo cambia la conclusión si $A,D$ no son coprimos.



**79. Reconstrucción y libertad residual.** Encuentra todos los polinomios mónicos $P$ de grado $4$ que dejan resto $x+1$ por $x^2+1$ y cumplen $P(1)=6$, $P(-1)=2$. Luego describe todas las soluciones de las tres condiciones sin imponer grado ni monicidad.



**80. Inversos y parámetros en dos restos.** Para cada real $t$, decide si existe un polinomio $H_t$ de grado menor que $2$ o cero tal que $(x-t)H_t\equiv1\pmod{x^2-1}$. Encuéntralo cuando exista y describe todos los polinomios que satisfacen la congruencia.

### H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Una división válida en racionales que falla en enteros

Divida $x^3$ por $3x-1$ en $\mathbb Q[x]$ y explique por qué el mismo cociente y resto no pertenecen a $\mathbb Z[x]$.



#### Ejercicio 082. Ampliar los coeficientes no altera una división ya certificada

Divida $P=(x^3+2x+1)/2$ por $D=x^2+1$ y compare la división en $\mathbb Q[x]$ y en $\mathbb R[x]$.



#### Ejercicio 083. El divisor obliga a usar coeficientes reales

Divida $x^2$ por $\sqrt2x-1$ en $\mathbb R[x]$. Explique por qué no es una división formulada en $\mathbb Q[x]$.



#### Ejercicio 084. Diagnosticar una regla de grados fuera de un cuerpo

Usando coeficientes módulo $6$, calcule $(2x+1)(3x+1)$. Compare el grado obtenido con la suma de grados y localice la hipótesis perdida.



#### Ejercicio 085. Clasificar cuándo la división conserva coeficientes enteros

Para $m\in\mathbb Z\setminus\{0\}$, divida $x^2$ por $mx-1$ en $\mathbb Q[x]$. Determine cuándo cociente y resto son enteros.



#### Ejercicio 086. Construir un dividendo desde cociente, grado y valores

Construya $P$ cuya división por $x^2+1$ tenga cociente $x^2-2$, resto de grado menor que dos y valores $P(0)=3$, $P(1)=7$.



#### Ejercicio 087. Prescribir dos valores del resto

Dados $u,v\in\mathbb R$ y un polinomio $Q$, construya el único $P$ con cociente $Q$ al dividir por $x^2-1$ y resto $R$ que satisfaga $R(1)=u$, $R(-1)=v$.



#### Ejercicio 088. Diseñar un cúbico mediante un resto

Para cada $k\in\mathbb R$, construya el cúbico mónico $P$ cuya división por $x^2-1$ tenga resto $2x+3$ y que cumpla $P(0)=k$.



#### Ejercicio 089. Construir todos los dividendos pares de una división

Sean $c,v\in\mathbb R$. Describa todos los polinomios pares $P$ de grado cuatro y coeficiente principal dos cuya división por $x^2+1$ tenga $Q(0)=v$ y $P(0)=c$.



#### Ejercicio 090. Una reconstrucción que todavía no certifica la división

Para $P=x^3+1$, $D=x^2+1$, alguien propone $Q=x+1$, $R=-x^2-x$. Verifique la identidad y repare el par.



#### Ejercicio 091. Un divisor lineal que se vuelve constante

Divida $x^2+1$ por $tx+1$ para cada $t\in\mathbb R$.



#### Ejercicio 092. Un divisor cuadrático que baja de grado

Divida $x^3$ por $(t-1)x^2+x$ para todo real $t$.



#### Ejercicio 093. Un divisor que desaparece

Divida $x^3-1$ por $t(x^2+1)$ cuando la operación exista. Identifique todos los parámetros inadmisibles.



#### Ejercicio 094. Clasificar una división y detectar un cociente nulo

Divida $t x^2+1$ por $x^2+1$ para todo real $t$, e indique los cambios de grado del dividendo y del resto.



#### Ejercicio 095. Un divisor cuyo término principal se anula en dos valores

Divida $x^2+1$ por $(t^2-1)x+1$ y clasifique los valores especiales.



#### Ejercicio 096. Certificar un MCD sin buscar todas las raíces

Sean $P=x^2+1$ y $S=x^3+x+1$. Determine su MCD mónico y dé un certificado de Bézout.



#### Ejercicio 097. Leer un factor común y certificar que es máximo

Sean $P=(x-2)(x^2+1)$ y $S=(x-2)(x^2+2)$. Determine su MCD mónico y una combinación que lo certifique.



#### Ejercicio 098. Construir un inverso residual que existe para todo parámetro

Para $t\in\mathbb R$, encuentre todos los $H\in\mathbb R[x]$ tales que $(x-t)H$ deje resto uno al dividir por $D=x^2+x+1$.



#### Ejercicio 099. Certificar unicidad de un resto por grados

Sea $D\ne0$ y suponga que $P=DQ_1+R_1=DQ_2+R_2$, con ambos restos cero o de grado menor que $\deg D$. Pruebe la unicidad y explique el caso de divisor constante.



#### Ejercicio 100. Normalizar un certificado de Euclides

Se dispone de $G=6x-12$, $P=(6x-12)(x+1)$, $S=(6x-12)(x+2)$ y $S-P=G$. Obtenga el MCD mónico y su Bézout; explique qué cambia.

## Soluciones desarrolladas

### Soluciones — Lectura formal y grado



**1.** Los exponentes de una indeterminada deben ser enteros no negativos. El primer objeto tiene coeficientes reales, pero el coeficiente $-\sqrt2$ no es racional: pertenece a $\mathbb R[x]$ y no a $\mathbb Q[x]$. El segundo tiene un exponente negativo, así que no pertenece a ninguno. La constante $5$ pertenece a ambos y tiene grado $0$. El dominio de los coeficientes y la condición sobre los exponentes son controles independientes.



**2.** La sucesión es $(4,0,-3,0,0,\ldots)$. El último coeficiente no nulo ocupa la posición $2$, por lo que $\deg P=2$. El coeficiente escrito de $x^5$ es cero y no aumenta el grado. La sucesión de $Q$ es idéntica; por definición formal, $P=Q$.



**3.** El coeficiente principal se anula exactamente en $t=1,-1$. Para $t\notin\{-1,1\}$ el grado es $3$. Si $t=-1$, resulta $P_t=-2x-4$, de grado $1$. Si $t=1$, todos los coeficientes son cero y el grado no está definido. Revisar solo el coeficiente cúbico no permite distinguir los dos casos excepcionales.



**4.** Cada índice es un exponente: $a_0=9$, $a_1=-2$, $a_2=a_3=0$, $a_4=7$ y $a_6=0$. El grado es $4$ y el principal es $7$. Los términos ausentes tienen coeficiente cero, incluso por encima del grado; no hay un coeficiente “desconocido” en esas posiciones.



**5.** Dividir todos los coeficientes por $-3$ da $G=x^3-2x+3$. Su principal es $1$ y el polinomio inicial es $-3G$. No son iguales: sus coeficientes cúbicos son diferentes. La normalización conserva la clase de asociados, no la igualdad formal.



**6.** El término de grado $7$ de $P$ no puede cancelarse con uno de $Q$, así que $\deg(P+Q)=7$. En el producto, los principales no nulos tienen producto no nulo y $\deg(PQ)=7+4=11$. La primera conclusión usa que los grados son distintos; la segunda usa la aritmética real.



**7.** Restar da $(x^2+1)(A-(2x-3))=0$. El primer factor es un polinomio no nulo; un producto de dos polinomios no nulos en $\mathbb Q[x]$ no puede ser cero. Por tanto el segundo factor debe ser cero y $A=2x-3$. La justificación es formal y no requiere elegir valores de $x$.



**8.** Ambas evaluaciones coinciden en esos dos puntos, pero sus coeficientes no: el de $x^2$ es $1$ en el primer polinomio y $0$ en el segundo. Además, en $x=2$ sus valores son $4$ y $2$. La conclusión es falsa; coincidir en una muestra sin un teorema y sus hipótesis no certifica una identidad.



**9.** Cada multiplicación suma grados. Aplicando la fórmula tres veces, $\deg(P^4)=3+3+3+3=12$. Todos los productos intermedios son no nulos. La expresión $3^4$ elevaría el número que mide el grado; el polinomio se eleva mediante cuatro productos.



**10.** Cero no tiene inverso porque $0Q=0\ne1$. La constante $-5$ tiene inverso $-1/5$. Si $(x^2+1)Q=1$, entonces $Q\ne0$ y la fórmula del grado exigiría $2+\deg Q=0$, imposible. La expresión racional $1/(x^2+1)$ no es un inverso polinómico.

### Soluciones — Operaciones, evaluación y composición



**11.** Se agrupan coeficientes del mismo exponente: $(3-1)x^3+(-2+2)x^2+5x+(4-7)=2x^3+5x-3$. El término cuadrático desaparece, pero el cúbico permanece. El grado es $3$, con principal $2$.



**12.** El signo menos afecta a todos los términos del segundo polinomio. Después de distribuirlo, queda $(2-1)x^4+(-1-2)x^2+(3+1)x+(-1-5)=x^4-3x^2+4x-6$. La comprobación consiste en sumar el sustraendo al resultado y recuperar el minuendo.



**13.** Primero $2P=2x^2-4x+2$. Al restar $Q$, los términos cuadráticos se cancelan y obtenemos $-5x+5$. Su grado es $1$. Sustituir $P,Q$ en $2P-Q$ y comparar coeficientes verifica la cancelación y el término constante.



**14.** La distributividad da $x^3-3x^2+x^2-3x-2x+6$. Reunir términos produce $x^3-2x^2-5x+6$. El grado $3$ y el principal $1$ concuerdan con los de los factores; el constante $6=(-2)(-3)$ comprueba el extremo inferior.



**15.** Los cuatro productos son $2x^5$, $4x^3$, $-x^2$ y $-2$. Por tanto el resultado es $2x^5+4x^3-x^2-2$. No hay pareja de términos que produzca $x^4$, cuyo coeficiente es cero. El hueco debe conservarse si después se usa una tabla de división.



**16.** Solo se necesitan las parejas cuyos exponentes suman $3$: $a_1b_2=2\cdot4$, $a_2b_1=(-1)(-1)$ y $a_3b_0=3\cdot2$. La pareja $a_0b_3$ aporta cero. La suma es $8+1+6=15$. Esta selección evita calcular coeficientes que no pide el problema.



**17.** Los cuadrados de los tres términos son $x^4$, $4x^2$ y $4$; los productos cruzados dobles son $-4x^3$, $4x^2$ y $-8x$. Al reunirlos resulta $x^4-4x^3+8x^2-8x+4$. Olvidar los términos cruzados produciría otro polinomio, aunque conservara el grado y el constante.



**18.** Multiplicar la suma por $x$ produce $x+x^2+\cdots+x^n$; multiplicarla por $-1$ produce $-1-x-\cdots-x^{n-1}$. Los términos de grados $1$ a $n-1$ se cancelan por parejas y quedan $x^n-1$. Para $n=1$ las sumas intermedias vacías no aparecen y la identidad dice $(x-1)\cdot1=x-1$.



**19.** Sustituir $-2$ da $3(-8)-2(4)-2-4=-38$. Para $1/2$, $P(1/2)=3/8-1/2+1/2-4=-29/8$. Las potencias se calculan antes de multiplicar por los coeficientes; el término cuadrático conserva signo positivo antes de aplicar su coeficiente negativo.



**20.** Se usan los coeficientes $2,0,-3,5,-1$. Acumular multiplicaciones por $-1$ y sumas sucesivas da $2$, $-2$, $-1$, $6$, $-7$. El último valor es $P(-1)=-7$. La sustitución directa $2-3-5-1=-7$ confirma el resultado. El cero del término cúbico mantiene la posición de los coeficientes.



**21.** En la primera composición reemplazamos la indeterminada de $P$ por $Q$: $(2x+1)^2-2=4x^2+4x-1$. En la segunda, $2(x^2-2)+1=2x^2-3$. No coinciden: el coeficiente cuadrático es $4$ en una y $2$ en otra. El orden determina cuál polinomio actúa por fuera.



**22.** $P(C)=2^2-4=0$, así que $P\circ C$ es el polinomio nulo y no tiene grado. La composición $C\circ P$ sigue siendo la constante $2$, de grado $0$: $C$ no depende de su argumento. No se aplica la fórmula de grados para dos polinomios no constantes.



**23.** La expansión izquierda es $ax^2+(2a+b)x+2b+c$. Igualar coeficientes da $a=2$, $2a+b=3$ y $2b+c=5$. Así, $b=-1$ y $c=7$. Comprobar $(2x-1)(x+2)+7=2x^2+3x+5$ verifica las tres condiciones simultáneamente.



**24.** El producto es $ux^2+(v-2u)x-2v$. El coeficiente principal exige $u=3$ y el constante exige $v=-1$. El coeficiente intermedio queda $-1-6=-7$, por lo que también se satisface. Es necesario revisar esta tercera ecuación: dos extremos correctos no garantizan una identidad.



**25.** $P(x+1)=(x+1)^2+3(x+1)+1=x^2+5x+5$. Al restar $P(x)$, queda $2x+4$, de grado $1$. La cancelación del término cuadrático explica la disminución del grado; no se utilizó ninguna derivada.



**26.** El término $3Q^4$ tiene grado $12$ y principal $3\cdot2^4=48$. Los otros términos, $-Q$ y $1$, tienen grados $3$ y $0$, y no pueden cancelar el término de grado $12$. Por tanto la composición tiene grado $12$ y principal $48$.

### Soluciones — División larga y división lineal



**27.** El término $x^2$ del cociente cancela los dos primeros términos y deja $-3x^2+3x-1$. El siguiente término es $-3$; al restar $-3(x^2+x+1)$ queda $6x+2$. Por tanto $Q=x^2-3$, $R=6x+2$. El resto tiene grado $1<2$ y la reconstrucción $(x^2+x+1)(x^2-3)+6x+2$ devuelve el dividendo.



**28.** Horner usa $c=-2$, no $2$. Con coeficientes $2,3,-1,5$, obtiene $2,-1,1,3$. El cociente es $2x^2-x+1$ y el resto $3$. Multiplicar $(x+2)(2x^2-x+1)$ da $2x^3+3x^2-x+2$; al sumar $3$ recuperamos el dividendo. También $P(-2)=3$.



**29.** Restar $x^2(x^2+2)$ deja $-2x^2+1$. Restar $-2(x^2+2)$ deja $5$. Así, $Q=x^2-2$ y $R=5$. La identidad $(x^2+2)(x^2-2)+5=x^4+1$ y la cota $0<2$ lo verifican. El resto podría haber sido lineal; que aquí sea constante se debe al cálculo.



**30.** El primer término del cociente es $(3/2)x$. Después de restar su producto por el divisor queda $-x^2+(5/2)x-2$. El siguiente término es $-1/2$, y el resto es $(5/2)x-3/2$. Por tanto $Q=(3/2)x-1/2$. La expansión de $(2x^2+1)Q$ es $3x^3-x^2+(3/2)x-1/2$; sumar el resto restituye los coeficientes pedidos.



**31.** Los coeficientes son $1,0,-4,1$. Horner con $c=1$ da $1,1,-3,-2$, de modo que $Q=x^2+x-3$ y $R=-2$. La reconstrucción $(x-1)(x^2+x-3)-2=x^3-4x+1$ lo confirma. Un resto polinómico no está sujeto a la condición de ser un número no negativo de la división entera.



**32.** El divisor es $2(x+1/2)$. Horner con $c=-1/2$ da cociente $2x^2-5$ para $x+1/2$, y resto $13/2$. Dividir ese cociente por $2$ da $Q=x^2-5/2$ para el divisor original. En efecto, $(2x+1)(x^2-5/2)+13/2=2x^3+x^2-5x+4$.



**33.** El grado del dividendo es $1<3$, por lo que $Q=0$ y $R=3x-2$. La identidad $P=D\cdot0+P$ ya cumple la cota. No se introducen potencias negativas para continuar: eso cambiaría el tipo de objeto que admite el cociente.



**34.** Dividir cada coeficiente por $-3$ produce $Q=-2x^2+x-3$, y $R=0$. Un resto no nulo tendría grado al menos $0$, así que no cumpliría la cota estricta respecto de un divisor de grado $0$. La multiplicación por $-3$ reconstruye el dividendo.



**35.** La identidad $0=(x^2-5)0+0$ demuestra que $Q=R=0$ es una división admisible, pues la condición del resto admite explícitamente cero. La unicidad de la división prueba que es la única. No se necesita ninguna comparación que use $\deg0$.



**36.** Restar $x(x^2+x)$ deja $-x^2+2x+1$. Restar $-(x^2+x)$ deja $3x+1$. Entonces $Q=x-1$, $R=3x+1$. La identidad $(x^2+x)(x-1)+3x+1=x^3+2x+1$ y la cota verifican el resultado. El divisor es mónico: cada cancelación divide el principal del resto por $1$, por lo que conserva coeficientes enteros.



**37.** La identidad de división obliga a tomar $P=(x^2-2)(2x+3)+(x-1)=2x^3+3x^2-3x-7$. El resto es no nulo de grado $1<2$, por lo que los datos sí constituyen una división. La unicidad asegura que, al dividir el polinomio construido, se recuperarán ese cociente y ese resto.



**38.** La expansión confirma la identidad, pero el supuesto resto tiene grado $2$, igual al del divisor. Hay que dividirlo otra vez: $x^2-x+1=(x^2+1)\cdot1-x$. Sumando $1$ al cociente propuesto, resulta $Q=x$ y $R=-x$. La identidad corregida es $x^3=(x^2+1)x-x$, con resto de grado $1<2$.

### Soluciones — Demostraciones y diagnóstico



**39.** El coeficiente de $x^n$ de la suma es $a_n+b_n$, y todos los superiores son cero. Si $a_n+b_n=0$, desaparece el término de grado $n$; la suma es cero o su último coeficiente no nulo aparece por debajo. Recíprocamente, cualquiera de esas dos posibilidades exige que el coeficiente de $x^n$ sea cero. La equivalencia incluye $n=0$: entonces la suma debe ser el polinomio nulo.



**40.** El producto formal es $4x^2$, que tiene todos los coeficientes cero módulo $4$. Cada factor $2x$ es no nulo, pero su producto es cero. Falla la inferencia “dos coeficientes principales no nulos tienen producto no nulo”: $2\cdot2=0$ en esa aritmética. No contradice el resultado del capítulo, formulado para $\mathbb Q$ y $\mathbb R$.



**41.** En cada cancelación, si el principal del resto parcial es $a$, el término agregado al cociente es $ax^{n-m}$ porque el principal del divisor vale $1$. Ese término y su producto por $D$ tienen coeficientes enteros; restarlos mantiene los coeficientes enteros del nuevo resto. La propiedad vale al inicio y se conserva en todos los pasos. El descenso de grado termina el proceso, incluso si el divisor es la constante mónica $1$, cuyo resto es cero.



**42.** En $x=2$ no se puede dividir por el valor del factor. La prueba formal evita ese paso: $ (x-2)(A-B)=0$ como identidad. Si $A-B\ne0$, el producto tendría grado $1+\deg(A-B)$ y sería no nulo, contradicción. Luego $A=B$. La conclusión era correcta, pero el argumento numérico tal como se escribió no la justificaba para cada real.



**43.** Sustituir la identidad da $P+DT=D(Q+T)+R$. El resto conserva su condición de ser cero o de grado menor que el divisor. Por unicidad, el nuevo cociente es $Q+T$ y el nuevo resto es $R$. Esta prueba permite modificar el dividendo sin recalcular cuando la diferencia es un múltiplo del divisor.



**44.** Si el cociente fuera cero, la identidad daría $P=R$, incompatible con la cota del resto. Por tanto $DQ\ne0$ y su grado es $\deg D+\deg Q$, al menos $\deg D$. El resto tiene grado menor que $\deg D$ o es cero, y no puede cancelar el principal de $DQ$. Así $\deg P=\deg D+\deg Q$, que da la fórmula. El caso de divisor constante también cumple el razonamiento, con resto cero.



**45.** Al dividir $x$ por $x^2+1$, el cociente es cero y el resto es $x$, que no es constante. La condición correcta es que el resto sea cero o tenga grado menor que el divisor. En particular, para un divisor de grado $1$, el resto sí es constante; para uno de grado $2$ puede ser lineal.



**46.** La multiplicación de congruencias da $x\cdot x\equiv x^2$, pero $x^2$ aún tiene grado igual al del divisor. Como $x^2=(x^2+1)-1$, su resto es $-1$. La regla correcta es reducir el producto de los restos una segunda vez si no cumple la cota. Una expresión congruente no es necesariamente el representante de grado mínimo.



**47.** Por coeficientes, al sustituir $S$ en $P+Q$ se obtiene $\sum_k(a_k+b_k)S^k=\sum_k a_kS^k+\sum_k b_kS^k$. Esto prueba la primera identidad. La segunda es falsa: con $P=x^2$, $Q=x$ y $S=1$, la izquierda es $(x+1)^2=x^2+2x+1$ y la derecha es $x^2+1$. El término cruzado distingue los polinomios.



**48.** Para $P\ne0$, la identidad $P=0Q+R$ fuerza $R=P$, y no existe grado del divisor con el que imponer la cota. Para $P=0$, tomando $R=0$ la identidad vale para cualquier cociente $Q$; no hay unicidad. El requisito $D\ne0$ garantiza tanto una cota de grado definida como una cancelación principal que puede ejecutarse.



**49.** De $P=GA$ resulta $P=(cG)(A/c)$, y lo mismo para $S$, así que $cG$ divide a ambos. Si $H$ es divisor común, $H\mid G$, luego también $H\mid cG$. Eso prueba las dos obligaciones del MCD. La condición mónica fija $c$ para que el principal sea $1$ y selecciona un único representante entre los asociados.



**50.** Que el primer polinomio se anule en un punto no demuestra que divida al segundo. De hecho, $x^2+1=x\cdot x+1$ deja resto $1$. Todo divisor común divide a ese resto, y la constante $1$ divide a ambos. Por tanto el MCD mónico es $1$. La división ofrece el certificado que la evaluación aislada no proporciona.

### Soluciones — Restos y parámetros



**51.** Módulo el divisor, $x^2\equiv-1$ y $x^4\equiv1$. Así $x^{100}\equiv1$ y $x^{99}=x^{96}x^3\equiv-x$. El polinomio es congruente con $-1-3x$, que ya tiene grado menor que $2$. Por unicidad ese es el resto. La reducción de exponentes evita efectuar cincuenta pasos de división larga.



**52.** Usamos $x^2\equiv x+1$ y multiplicamos sucesivamente por $x$, reduciendo de nuevo: $x^3\equiv2x+1$, $x^4\equiv3x+2$, $x^5\equiv5x+3$, $x^6\equiv8x+5$. Cada sustitución cambia la expresión por un múltiplo del divisor. Como la última expresión tiene grado $1$, el resto buscado es $8x+5$.



**53.** La identidad $x^3-1=(x-1)(x^2+x+1)$ muestra $x^3\equiv1$ módulo el divisor. Al elevar esa congruencia a exponentes no negativos, los tres primeros términos se reducen a $x^2$, $2x$ y $1$. Tras restar $x$, queda $x^2+x+1$, cuyo resto es cero. Por tanto el polinomio original es divisible por el divisor. Se comprueba también el caso $r=s=t=0$: el polinomio ya es $x^2+x+1$. El argumento usa aritmética de restos, sin raíces complejas.



**54.** Al reducir $x^2\equiv-1$ y $x^3\equiv-x$, el resto es $(b-1)x+(1-a)$. Igualar sus dos coeficientes con los de $x+2$ da $b-1=1$ y $1-a=2$, es decir, $b=2$, $a=-1$. El cociente es $x-1$, y $(x^2+1)(x-1)+(x+2)=x^3-x^2+2x+1$ verifica la división.



**55.** El resto da $P(1)=a+b+3=4$, luego $a+b=1$. Evaluar $P=(x-1)Q+4$ en $2$ da $P(2)=11$, o $8a+4b+5=11$. Así $2a+b=3/2$, y al restar la primera ecuación queda $a=1/2$, $b=1/2$. Horner produce $Q=x^2/2+x+3$, cuyo valor en $2$ es $7$; el resto es $1+3=4$.



**56.** Si $t\ne2$, el divisor es lineal y se anula en $c=-1/(t-2)$. Por el teorema del resto para un divisor lineal no mónico, el resto es $P(c)=1/(t-2)^2-1$. Si $t=2$, el divisor es la constante $1$, de modo que $Q=P$ y $R=0$. La fórmula del caso lineal no está definida en $2$ y no se extiende por sustitución.



**57.** Reducir módulo $x^2+1$ deja el constante $1-a+b$. La divisibilidad equivale a $b=a-1$. En ese caso $Q=x^2+a-1$, porque $(x^2+1)(x^2+a-1)=x^4+ax^2+(a-1)$. Todos los reales $a$ son posibles y la igualdad muestra la suficiencia, además de la necesidad obtenida con el resto.



**58.** Se tiene $x^2\equiv1$, así que $x^{2025}=x(x^2)^{1012}\equiv x$. El resto es $x+1$, de grado $1<2$. Evaluar el resto en $1$ y $-1$ da $2$ y $0$, igual que el polinomio original; esto comprueba dos valores, mientras que la congruencia demuestra la reducción formal.



**59.** Los datos son $P(1)=1+a+b=3$ y $P(-1)=-1-a+b=1$. Por tanto $a+b=2$ y $-a+b=2$. Sumando, $b=2$; sustituyendo, $a=0$. Con $P=x^3+2$, las evaluaciones dan efectivamente $3$ y $1$. Cada resto aporta una ecuación distinta.



**60.** Por división, el resto se escribe $R=ux+v$, permitiendo $u=0$. Como el divisor vale cero en $1,-1$, la identidad de división da $u+v=5$ y $-u+v=1$. Entonces $u=2$, $v=3$, y $R=2x+3$. El argumento no supone que dos valores determinen todo $P$: solo determinan el resto, cuyo grado ya está acotado por el teorema de división.

### Soluciones — Euclides y Bézout



**61.** La primera división es $P=xS+(x-1)$. La siguiente es $S=(x+1)(x-1)+0$. El último resto no nulo es $x-1$, ya mónico. Cada paso conserva los divisores comunes, por lo que $\gcd(P,S)=x-1$. La factorización visible en la segunda igualdad comprueba que ese polinomio divide a ambos.



**62.** Restar $x(x^3-1)$ del primer polinomio deja $x-1$. Después, $x^3-1=(x^2+x+1)(x-1)$. Así el último resto no nulo es $x-1$ y ese es el MCD mónico. No es necesario factorizar ambos polinomios completamente: Euclides identifica un divisor que recoge todos los divisores comunes.



**63.** La división da $P=(x+1)S+1$. El siguiente paso divide $S$ por $1$ y termina. El MCD es $1$ y la misma igualdad produce $1=P-(x+1)S$. Los coeficientes de Bézout son $U=1$, $V=-(x+1)$. Expandir el miembro derecho deja la constante $1$.



**64.** Se tiene $P=xS+2$. Al dividir $S$ por $2$ queda resto cero. El último resto es $2$, pero su normalización mónica es $1$. Dividir la identidad del resto por $2$ da $1=P/2-(x/2)S$, así que $U=1/2$, $V=-x/2$. Esa normalización es admisible porque trabajamos con coeficientes racionales o reales.



**65.** La primera división tiene cociente $(2/3)(x+1)$ y resto cero, puesto que $(3x-3)(2/3)(x+1)=2x^2-2$. El último divisor es $3x-3$; dividirlo por su principal $3$ da $x-1$. La constante escalar del divisor no se conserva en el MCD mónico.



**66.** Todos los divisores comunes son exactamente los divisores del segundo polinomio, porque cualquier polinomio divide a cero. Su normalización es $G=x^2+x/2$. Una identidad es $G=0\cdot0+(1/4)(4x^2+2x)$. El polinomio no nulo fija el MCD; no se utiliza el grado del argumento cero.



**67.** El producto $(x-1)(x+1)$ es $x^2-1$, así que la igualdad vale. Todo divisor común de $x^2$ y $x+1$ divide su combinación $1$ y debe ser constante no nulo. Como $1$ divide a ambos, es el MCD mónico. El certificado corresponde a $U=1$, $V=1-x$.



**68.** La identidad $1=A-xB$ certifica la coprimalidad. Multiplicar por $C$ da $C=AC-xBC$. El primer sumando es múltiplo de $A$, y el segundo también por la hipótesis $A\mid BC$. Su diferencia es divisible por $A$, luego $A\mid C$. La identidad de Bézout permite seleccionar la cancelación adecuada.



**69.** Como $A\mid P$, existe $T$ con $P=AT$. La otra hipótesis da $B\mid AT$. La coprimalidad permite cancelar $A$ en esta afirmación, de modo que $B\mid T$. Escribiendo $T=BU$, resulta $P=ABU$. Si $P=0$, el mismo argumento admite $U=0$. Sin coprimalidad, $A=B=x$, $P=x$ refutaría la conclusión.



**70.** Sustituir esas fórmulas produce la identidad inicial más $SPT-PST=0$, por lo que toda pareja construida sirve. Recíprocamente, restar el certificado inicial da $(U-1)P+(V-(1-x))S=0$. Entonces $S\mid(U-1)P$. Como $P,S$ son coprimos por el ejercicio 67, $S\mid U-1$, así que $U-1=ST$. La ecuación restante es $S(PT+V-(1-x))=0$; cancelar $S\ne0$ da $V=1-x-PT$.



**71.** La diferencia entre los dos polinomios es $t-1$. Si $t\ne1$, todo divisor común divide a una constante no nula, de modo que el MCD mónico es $1$. Si $t=1$, los polinomios coinciden y su MCD es $x^2+1$. La identidad de Bézout en el primer caso es $1=((x^2+t)-(x^2+1))/(t-1)$, que también señala por qué debe separarse $t=1$.



**72.** La división exacta es $P=(x-1)S$, porque $(x-1)(x^2+x)=x^3-x$. Por tanto $G=S=x^2+x$, ya mónico. Es divisor de ambos y tiene el certificado $G=0P+1S$. Todo divisor común divide a $S$ por definición, así que esa elección también satisface la condición universal del MCD. Una identidad de Bézout puede tener un coeficiente cero.

### Soluciones — Problemas de síntesis



**73.** La dificultad es compatibilizar dos divisiones, no resolverlas aisladamente. Como $A-B=x$ y $B=x(x-1)+1$, obtenemos $1=(1-x)A+xB$. Esto certifica que $A,B$ son coprimos.

Un candidato es $P_0=-x^3$: módulo $A$, $x^2\equiv-1$ y $-x^3\equiv x$; módulo $B$, $x^2\equiv x-1$, luego $x^3\equiv x^2-x\equiv-1$, de modo que $-x^3\equiv1$. Así satisface ambos datos.

Si $P$ es cualquier otra solución, los dos divisores dividen a $P-P_0$. Por la coprimalidad y el resultado del ejercicio 69, $AB\mid P-P_0$. Por tanto todas las soluciones son $P=-x^3+ABT$, con $T\in K[x]$; la sustitución verifica la suficiencia. Si $T\ne0$, el término $ABT$ tiene grado al menos $4$ y no puede cancelarse con $-x^3$. El único de grado menor que $4$ es $-x^3$. La identidad de Bézout es la herramienta que permite combinar condiciones sobre restos.



**74.** La primera división es $P=xS_t+R_t$, donde $R_t=1-(t+2)x$. Si $t=-2$, el resto es $1$ y el MCD es $1$.

Para $t\ne-2$, $R_t$ es lineal, asociado a $x-c$, con $c=1/(t+2)$. Dividir $S_t$ por $x-c$ deja el resto $S_t(c)=1/(t+2)^2+t$. Si este resto es no nulo, el algoritmo termina en una constante y el MCD mónico es $1$. Si es cero, termina en $R_t$, cuyo representante mónico es $x-c$.

La condición excepcional es $t(t+2)^2+1=0$. Por expansión se verifica que el miembro izquierdo es $(t+1)(t^2+3t+1)$. La resolución de estas ecuaciones, disponible desde C19–C21, da $t=-1$ o $t=(-3\pm\sqrt5)/2$, ninguno igual a $-2$. Para esos tres valores, $G_t=x-1/(t+2)$; para todos los demás, $G_t=1$.

Cada bifurcación corresponde a la anulación de un resto real del algoritmo. No se supuso de antemano que el grado del MCD permaneciera constante cuando cambiaba $t$.



**75.** Para $n=1$, el resto es $x=f_1x+f_0$. Si la fórmula vale en $n$, multiplicar por $x$ y usar $x^2\equiv x+1$ da
$$
x^{n+1}\equiv f_n(x+1)+f_{n-1}x=f_{n+1}x+f_n.
$$
La expresión tiene grado menor que $2$, por lo que es el resto único. La inducción prueba la fórmula para todo $n\ge1$; el resto de $x^0$ se trata aparte y es $1$.

Para deducir la identidad, reducimos el producto de los restos de $x^m$ y $x^n$. Antes de reducir es $f_mf_nx^2+(f_mf_{n-1}+f_{m-1}f_n)x+f_{m-1}f_{n-1}$. Después de reemplazar $x^2$ por $x+1$, su coeficiente lineal es $f_m(f_n+f_{n-1})+f_{m-1}f_n=f_mf_{n+1}+f_{m-1}f_n$. El producto representa el resto de $x^{m+n}$, cuyo coeficiente lineal ya sabemos que es $f_{m+n}$. La unicidad del resto y la igualdad por coeficientes prueban la identidad. La recurrencia numérica se recupera como consecuencia de una operación polinómica.



**76.** La señal que permite cambiar de problema es que la división de exponentes también produce una división de polinomios. Si $m=qn+r$, con $0\le r<n$ y $m\ge n$, la identidad telescópica da
$$
x^m-1=(x^n-1)x^r\bigl(1+x^n+\cdots+x^{(q-1)n}\bigr)+(x^r-1).
$$
Para $r=0$, el último término es cero; para $r>0$ tiene grado $r<n$. Esta es una división admisible y transforma la pareja de divisores comunes en $(x^n-1,x^r-1)$.

Se repite el procedimiento según el algoritmo de Euclides entero. Sus restos positivos descienden hasta el último, $d$, y el paso siguiente tiene resto cero. En la versión polinómica se llega a $(x^d-1,0)$. Como cada paso conserva todos los divisores comunes, el último polinomio no nulo es un MCD. Ya es mónico, así que no requiere otra normalización. Si inicialmente $m<n$, se intercambian los argumentos; si son iguales, la conclusión es inmediata con $d=m$.

La prueba no usa raíces de la unidad. Transporta el algoritmo entero mediante una identidad que puede comprobarse por distributividad.



**77.** Bézout proporciona alguna pareja $U_0,V_0$, pero sus grados pueden ser grandes. Dividimos $U_0$ por $B$: $U_0=BT+U$, con $U$ de grado menor que $b$ o cero. La identidad se convierte en $UA+(V_0+TA)B=1$. Definimos $V=V_0+TA$.

Si $U=0$, entonces $VB=1$, imposible porque $b\ge1$. Por tanto $U\ne0$; $UA$ tiene grado menor que $a+b$. El polinomio $1-UA$ tiene grado menor que $a+b$ o es cero. Como $VB=1-UA$, si $V\ne0$, la fórmula del producto da $\deg V+b<a+b$, luego $\deg V<a$. Esto demuestra la existencia con las dos cotas.

Para la unicidad, restamos dos certificados: $(U-U')A=-(V-V')B$. Entonces $B\mid(U-U')A$, y la coprimalidad implica $B\mid U-U'$. Si la diferencia fuera no nula, tendría grado al menos $b$ por divisibilidad, pero también menor que $b$ por las cotas de $U,U'$. Así $U=U'$. Cancelar $B\ne0$ en la igualdad restante da $V=V'$. La reducción de un coeficiente de Bézout controla el otro sin necesitar calcularlos explícitamente.



**78.** Para construir el inverso no buscamos un cociente racional: buscamos un certificado de Bézout. La división $D=xA+1$ da directamente $1=D-xA$. Entonces $H=-x$ satisface $AH=1-D$, y por tanto $AH\equiv1\pmod D$. Su grado es $1<3$.

Si otro $H'$ con grado menor que $3$ o cero cumple la misma congruencia, $D\mid A(H-H')$. La identidad anterior certifica que $A,D$ son coprimos; cancelando divisibilidad, $D\mid H-H'$. La diferencia es cero o tiene grado menor que $3$, y la segunda posibilidad no puede ser un múltiplo no nulo de $D$. Luego $H=H'$.

En general, la existencia de $AH=1+DT$ obliga a que todo divisor común de $A,D$ divida a $1$, es decir, a que su MCD mónico sea $1$. Si son coprimos, Bézout proporciona un inverso y la división por $D$ lo reduce al representante único. Un MCD no constante impide la existencia, no solamente la unicidad del candidato.



**79.** La división prescrita dice $P=(x^2+1)Q+x+1$. Si $P$ es mónico de grado $4$, el cociente debe ser mónico de grado $2$, así que $Q=x^2+ax+b$. Al evaluar en $1$, $6=2(1+a+b)+2$, de donde $a+b=1$. En $-1$, $2=2(1-a+b)$, de donde $b=a$. Así $a=b=1/2$ y
$$
P_0=x^4+\tfrac12x^3+\tfrac32x^2+\tfrac32x+\tfrac32.
$$
La forma $P_0=(x^2+1)(x^2+x/2+1/2)+x+1$ comprueba el resto; evaluar da $6$ y $2$.

Sin restricciones de grado, toda solución tiene $Q=Q_0+T$, donde $Q_0=x^2+x/2+1/2$. Las condiciones de evaluación exigen $T(1)=T(-1)=0$. Para describir estos $T$ sin teoría posterior de raíces, dividimos por $x^2-1$: $T=(x^2-1)W+ux+v$. Evaluar en $1,-1$ da $u+v=0$ y $-u+v=0$, luego $u=v=0$. Por tanto todas las soluciones son $P=P_0+(x^2+1)(x^2-1)W$, con $W\in K[x]$.

Si $W\ne0$ tiene grado positivo, el resultado tiene grado mayor que $4$. Si $W$ es constante no nula, el principal cambia de $1$ a $1+W$, y no es mónico de grado $4$. Esto también comprueba que $P_0$ es la única solución con las restricciones iniciales.



**80.** Escribimos $H_t=ux+v$. Al reducir el producto usando $x^2\equiv1$, obtenemos $(u-tv)+(v-tu)x$. Para que el resto sea $1$, las ecuaciones son $u-tv=1$ y $v-tu=0$. La segunda da $v=tu$ y la primera se convierte en $(1-t^2)u=1$.

Si $t=\pm1$, la última ecuación es imposible, por lo que no hay inverso. Si $t\ne\pm1$, existe la pareja única $u=1/(1-t^2)$, $v=t/(1-t^2)$, y $H_t=(x+t)/(1-t^2)$. La identidad
$$
(x-t)H_t=1+\frac{x^2-1}{1-t^2}
$$
verifica el resultado e identifica el múltiplo que se descarta al reducir.

Para clasificar inversos sin cota de grado, divide cualquier candidato $H$ por $x^2-1$. Su resto también es inverso, ya que cambiar $H$ por un múltiplo del divisor no cambia la congruencia del producto. La unicidad de las dos ecuaciones fuerza ese resto a ser $H_t$. Por tanto todos son $H=H_t+(x^2-1)T$, con $T\in\mathbb R[x]$. La ausencia de solución en $t=\pm1$ también se comprueba evaluando una supuesta identidad en $x=t$, donde ambos términos divisibles se anularían y dejarían $0=1$.

### H. Soluciones de profundización y reconstrucción



#### Solución 081

El cociente es $Q=x^2/3+x/9+1/27$ y el resto $R=1/27$. Multiplicar da $(3x-1)Q=x^3-1/27$, luego $P=DQ+R$ y el resto constante tiene grado menor que uno. Son válidos también en $\mathbb R[x]$. En enteros no puede existir división con resto constante: comparar el término cúbico exigiría un coeficiente principal $q$ entero con $3q=1$, imposible. Multiplicar la identidad por $27$ elimina denominadores, pero cambia el dividendo y no resuelve la división entera original.



#### Solución 082

Tenemos $Q=x/2$ y $R=(x+1)/2$, pues $DQ+R=(x^3+x)/2+(x+1)/2=P$. El resto tiene grado uno, menor que dos. Ambos pertenecen a $\mathbb Q[x]$ y por tanto a $\mathbb R[x]$. La unicidad de división en cada cuerpo impide que ampliar a reales genere otro par válido. El certificado contiene todos los coeficientes y la cota; no depende de probar valores aislados de $x$.



#### Solución 083

El cociente es $Q=x/\sqrt2+1/2$ y el resto $R=1/2$: multiplicar da $(\sqrt2x-1)Q=x^2-1/2$. La cota es $0<1$. El divisor tiene coeficiente irracional, de modo que no pertenece a $\mathbb Q[x]$ y la operación no tiene allí los objetos requeridos. Además, comparar el término cuadrático forzaría un coeficiente $1/\sqrt2$ en cualquier cociente, que tampoco es racional. No se confunde un resultado real correcto con una operación dentro de otro conjunto de coeficientes.



#### Solución 084

El producto formal previo a reducir es $6x^2+5x+1$, que módulo seis se convierte en $5x+1$, de grado uno. Los factores tienen grado uno cada uno, pero sus coeficientes principales multiplican a $2\cdot3=0$ módulo seis. Falló la propiedad de que el producto de no nulos sea no nulo, usada en la prueba sobre $\mathbb Q$ y $\mathbb R$. El cálculo no contradice ese teorema; muestra por qué no puede aplicarse a esta aritmética modular sin revisar sus hipótesis.



#### Solución 085

El par es $Q=x/m+1/m^2$, $R=1/m^2$, porque $(mx-1)Q=x^2-1/m^2$. La cota del resto es válida. Si $m=\pm1$, ambos tienen coeficientes enteros. Si $|m|>1$, el coeficiente $1/m$ del cociente no es entero; por unicidad no existe otro par entero con resto de grado menor que uno. Así la condición necesaria y suficiente es $|m|=1$. El valor cero se excluye porque el divisor perdería el grado que usa la clasificación.



#### Solución 086

Escribimos $R=ax+b$. En cero, $-2+b=3$ fuerza $b=5$; en uno, $2(-1)+a+5=7$ fuerza $a=4$. Por tanto $P=(x^2+1)(x^2-2)+4x+5=x^4-x^2+4x+3$. Evaluar da los dos datos, y la identidad con resto lineal certifica la división. Los dos valores fijaron de forma única $a,b$, luego no hay otro dividendo con el cociente impuesto.



#### Solución 087

La cota obliga $R=ax+b$, incluyendo constantes y cero. Los datos dan $a+b=u$ y $-a+b=v$, así $a=(u-v)/2$, $b=(u+v)/2$. El único dividendo es $P=(x^2-1)Q+[(u-v)x+u+v]/2$. Reconstruir confirma la identidad y la cota. Si $u=v$, el resto es constante; si ambos son cero, es cero. No debe asignarse un grado natural al resto cero.



#### Solución 088

El cociente debe ser mónico lineal, $Q=x+b$. Así $P=(x^2-1)(x+b)+2x+3=x^3+bx^2+x+3-b$. En cero, $3-b=k$, luego $b=3-k$. Resulta $P=x^3+(3-k)x^2+x+k$. Su coeficiente principal es uno, su valor en cero es $k$ y el resto impuesto tiene grado uno menor que dos. La comparación del término constante fija la única elección de $b$, probando unicidad.



#### Solución 089

El cociente es $Q=2x^2+ux+v$ y el resto $R=ax+b$. La reconstrucción da $P=2x^4+ux^3+(v+2)x^2+(u+a)x+v+b$. Ser par exige $u=0$ y luego $a=0$; el dato en cero fuerza $b=c-v$. Así solo hay $P=2x^4+(v+2)x^2+c$, con $Q=2x^2+v$, $R=c-v$. La identidad y la cota certifican el resultado también si el resto es cero. No se necesitan condiciones adicionales para conservar grado cuatro, porque el coeficiente principal es dos.



#### Solución 090

En efecto, $(x^2+1)(x+1)-x^2-x=x^3+1$. Pero el resto propuesto tiene grado dos, igual al divisor, y no cumple la cota. Restamos al cociente el término uno y añadimos $D$ al resto: $Q=x$, $R=1-x$. Ahora $DQ+R=x^3+x+1-x=P$ y $\deg R=1<2$. La identidad incorrectamente interpretada era verdadera; lo que faltaba era una condición del certificado de división.



#### Solución 091

Si $t=0$, el divisor es uno y la división es $Q=x^2+1$, $R=0$. Si $t\ne0$, $Q=x/t-1/t^2$ y $R=1+1/t^2$: multiplicar $D Q$ da $x^2-1/t^2$, y añadir el resto reconstruye $P$. El resto es constante y el divisor lineal. La rama constante exige resto cero; intentar sustituir $t=0$ en las fórmulas genéricas no tiene sentido porque se obtuvieron dividiendo por $t$.



#### Solución 092

Si $t=1$, $D=x$, $Q=x^2$, $R=0$. Si $t\ne1$, sea $a=t-1\ne0$: $Q=x/a-1/a^2$ y $R=x/a^2$. El producto $(ax^2+x)Q$ es $x^3-x/a^2$, de modo que la suma con $R$ da $x^3$. El resto lineal cumple la cota del divisor cuadrático. Ningún valor de $t$ produce divisor cero; separar el descenso de grado evita usar una cota equivocada en la rama lineal.



#### Solución 093

Para $t=0$, el divisor es el polinomio cero y la división no está definida. Para $t\ne0$, $Q=x/t$, $R=-x-1$: $t(x^2+1)(x/t)+(-x-1)=x^3-1$. El resto tiene grado uno menor que dos y la identidad certifica el par. La cota no compensa un divisor cero; por eso no puede extenderse el resultado a $t=0$ aunque el resto escrito no dependa del parámetro.



#### Solución 094

La identidad es $t x^2+1=t(x^2+1)+(1-t)$, luego $Q=t$, $R=1-t$. Para $t\ne0$, el dividendo tiene grado dos; para $t=0$ es la constante uno y el cociente es cero. Para $t=1$, el resto es cero; para los demás parámetros es constante no nulo. La cota se cumple en todos los casos. Los grados del polinomio cero se tratan como ausencia de grado natural, no como cero.



#### Solución 095

Sea $a=t^2-1$. Si $t=\pm1$, $a=0$ y el divisor es uno: $Q=x^2+1$, $R=0$. Si $t\ne\pm1$, $Q=x/a-1/a^2$ y $R=1+1/a^2$, pues $(ax+1)Q=x^2-1/a^2$. La identidad y el resto constante certifican la división lineal. Los dos valores especiales tienen el mismo comportamiento, pero ambos deben constar: dividir por $t^2-1$ sin separarlos omitiría dos operaciones válidas de otro grado.



#### Solución 096

La identidad $S-xP=1$ muestra que todo divisor común divide uno, por lo que es una constante no nula. El polinomio uno divide ambos; así el MCD mónico es uno. Los coeficientes de Bézout son $U=-x$, $V=1$. Esta prueba es formal y vale en $\mathbb Q[x]$ y $\mathbb R[x]$, sin calcular raíces ni suponer factorizaciones irreducibles.



#### Solución 097

El polinomio $G=x-2$ divide ambos por construcción. Además $S-P=x-2=G$. Por tanto, cualquier divisor común de $P,S$ divide a $G$. Estas dos propiedades prueban que $G$ es MCD, y es mónico. La combinación tiene coeficientes $-1,1$. Compartir un factor solo habría probado divisibilidad; la diferencia certifica la propiedad universal que faltaba.



#### Solución 098

Sea $c=t^2+t+1=(t+1/2)^2+3/4>0$. La identidad $D=(x-t)(x+t+1)+c$ da $H_0=-(x+t+1)/c$ y $(x-t)H_0=1-D/c$. Todos los $H=H_0+DT$ cumplen la condición. Recíprocamente, si $D$ divide $(x-t)(H-H_0)$, la misma identidad, multiplicada por $H-H_0$, muestra que $D$ divide $c(H-H_0)$ y por tanto $H-H_0$. Así la lista es completa. El resto de grado menor que dos es único y existe para todos los parámetros porque $c$ nunca es cero.



#### Solución 099

Restar da $D(Q_1-Q_2)=R_2-R_1$. Si $Q_1-Q_2\ne0$, el miembro izquierdo tiene grado al menos $\deg D$, mientras el derecho es cero o tiene grado menor; es imposible. Por tanto $Q_1=Q_2$ y luego $R_1=R_2$. Si $D$ es constante no nulo, no existe resto no nulo de grado menor que cero, así ambos restos son cero y el cociente es $P/D$. La prueba usa el grado del producto sobre el cuerpo y no aplica un grado natural al cero.



#### Solución 100

Como $G$ divide ambos y es su diferencia, todo divisor común divide a $G$. El MCD mónico es $g=G/6=x-2$. También divide a $P,S$, y $g=(-1/6)P+(1/6)S$. La normalización cambia los coeficientes de la combinación y el representante, pero no la clase de divisores comunes. Dividir por seis es legítimo en $\mathbb Q$ y $\mathbb R$. La reconstrucción de la diferencia comprueba el certificado; elegir el factor común sin esa segunda propiedad no bastaría para demostrar que es máximo.

## Referencias y continuidad del trabajo

La exposición es original. El rigor estructural se contrastó con Nicholson, *Introduction to Abstract Algebra*, 4.ª ed., [§4.1](proposiciones-y-conectivos-logicos.md#apm-c04-s01) y [§4.2](proposiciones-y-conectivos-logicos.md#apm-c04-s02); la división y su nivel universitario, con el apunte UChile de 2019, cap. 11. Lial, *College Algebra*, 12.ª ed., [§3.2](leyes-de-las-operaciones-y-transformaciones-justificadas.md#apm-c03-s02), y McCallum, *Algebra: Form and Function*, [§13.3](algebra-para-matematicos-capitulo-13-coeficientes-binomiales-y-teorema-del-binomio.md#apm-c13-s03), aportan referentes de fluidez. La calibración de tareas se documenta en el SOURCE_PACKET y la revisión de fuentes del capítulo, incluyendo el Control 7 UChile de 2009 y el repertorio Polinomios.pdf del expediente ULS.

***

[← Capítulo 23](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 25 →](algebra-para-matematicos-capitulo-25-raices-factores-e-irreducibilidad-elemental.md)

---
{
  "title": "Potencias, exponentes racionales y radicales",
  "description": "Capítulo 18 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0193",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C18",
  "editorial-id": "MA-BCH-APM-01-023",
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
    "MA-BCH-0192"
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

Hasta ahora hemos insistido en una disciplina básica: **una transformación algebraica no se justifica porque “se vea bien”, sino porque una propiedad permite hacerla bajo ciertas hipótesis**. En este capítulo esa disciplina se vuelve imprescindible.

Considere tres expresiones familiares:

$$
2^3,
\qquad
2^{-3},
\qquad
2^{3/2}.
$$

La primera puede interpretarse directamente como un producto repetido. Las otras dos no. Si intentáramos leer un exponente negativo como “multiplicar un número negativo de veces”, o un exponente fraccionario como “multiplicar una fracción de veces”, perderíamos el significado de la operación.

Por tanto, extender la noción de potencia exige una idea distinta: **queremos definir nuevos exponentes de manera que las leyes algebraicas ya conocidas continúen siendo coherentes**.

Pero esa extensión tiene un precio. Las nuevas expresiones traen consigo restricciones:

- una potencia con exponente negativo exige una base no nula;
- una raíz de índice par exige, en los reales, un radicando no negativo;
- un exponente racional puede cambiar de significado si se ignora la forma reducida de la fracción;
- una simplificación puede ocultar restricciones que pertenecían a la expresión original.

El capítulo girará alrededor de una idea:

> **Una ley algebraica incluye las condiciones bajo las cuales tiene sentido. La fluidez no consiste en mover símbolos con rapidez, sino en transformar expresiones sin perder su dominio ni su significado.**

Trabajaremos en $\mathbb R$ salvo indicación expresa. Usaremos como hecho fundacional la existencia de raíces reales: para $a\ge0$ y $n\ge2$ existe una única raíz $n$-ésima no negativa de $a$; si $n$ es impar, todo real posee una única raíz $n$-ésima real. La demostración de este hecho a partir de la completitud de $\mathbb R$ pertenece al análisis y no será reconstruida aquí.

***
## 18.1. Las leyes no vienen antes que el dominio {#apm-c18-s01}

Una misma cadena simbólica puede ser correcta para ciertos valores e incorrecta para otros. Por eso, antes de transformar una expresión, conviene hacer una pregunta que a menudo se omite:

> **¿Para qué valores están definidas todas las expresiones que aparecen en la cadena?**

Considere

$$
\sqrt{x^2}=x.
$$

Para $x=5$ la igualdad es verdadera. Para $x=-5$ no lo es, porque

$$
\sqrt{(-5)^2}=\sqrt{25}=5\neq-5.
$$

La forma correcta para todo real será

$$
\sqrt{x^2}=|x|.
$$

El error no está en una operación aritmética complicada. Está en haber usado una regla sin examinar el signo de la cantidad que sale de una raíz principal.

Observe ahora

$$
\frac{x^3}{x^3}=1.
$$

La simplificación es correcta cuando $x\neq0$. Pero la expresión original no está definida en $x=0$. Por tanto no debemos convertir la igualdad en una afirmación universal sobre todos los reales sin conservar la condición

$$
x\neq0.
$$

Un tercer ejemplo muestra otro tipo de peligro. La identidad

$$
\sqrt{ab}=\sqrt a\,\sqrt b
$$

es válida en $\mathbb R$ para $a,b\ge0$. No es una regla que pueda extenderse sin condiciones a cualesquiera números reales. Si $a=b=-1$, el lado izquierdo es

$$
\sqrt{(-1)(-1)}=1,
$$

mientras que las dos raíces del lado derecho no son reales.

Estos ejemplos sugieren una rutina que utilizaremos a lo largo del capítulo:

```text
EXPRESIÓN
   ↓
DOMINIO
   ↓
REGLA PROPUESTA
   ↓
HIPÓTESIS DE LA REGLA
   ↓
TRANSFORMACIÓN
   ↓
DOMINIO CONSERVADO
```

No siempre será necesario escribir esta cadena completa. La meta es que se vuelva parte del modo de leer una expresión.

### Una distinción útil: cálculo y validez

Dos preguntas diferentes pueden aparecer ante una transformación:

1. **¿El cálculo está ejecutado correctamente?**
2. **¿La transformación estaba permitida en el dominio considerado?**

Por ejemplo, en

$$
\frac{x^{-2}}{x^{-5}}=x^3
$$

el cálculo de exponentes es correcto, pero ambas potencias negativas exigen $x\neq0$. Es decir, la forma final $x^3$ está definida en $0$, pero la expresión original no.

La simplificación no autoriza a ampliar silenciosamente el dominio.

### Micropráctica de lectura

Antes de calcular, decida qué condición mínima debe acompañar a cada expresión:

$$
a^{-4},
\qquad
\frac1{\sqrt x},
\qquad
\sqrt[4]{y},
\qquad
\frac{z^2}{z}.
$$

La tarea no es todavía simplificar. Es **leer la estructura**.

**Control razonado.** $a^{-4}$ exige $a\ne0$ por el recíproco; $1/\sqrt x$ exige $x>0$, porque la raíz debe existir y no anularse; $\sqrt[4]y$ exige $y\ge0$; $z^2/z$ exige $z\ne0$, aunque después se simplifique a $z$.

***
## 18.2. Potencias enteras no negativas y estructura del exponente {#apm-c18-s02}

Comencemos en el dominio donde la interpretación es directa.

Para $a\in\mathbb R$ y un entero positivo $n$, definimos

$$
a^n=\underbrace{a\cdot a\cdots a}_{n\text{ factores}}.
$$

En particular,

$$
a^1=a.
$$

Aquí el exponente $n$ cuenta el número de factores iguales a $a$. Esa lectura permite demostrar las primeras leyes sin apelar a una tabla memorizada.

### Producto de potencias de igual base

Si $m,n$ son enteros positivos, entonces

$$
a^m a^n=a^{m+n}.
$$

La razón es simplemente que el primer factor contiene $m$ copias de $a$ y el segundo contiene $n$ copias. Al multiplicarlos obtenemos $m+n$ copias.

Por ejemplo,

$$
a^3a^4=(aaa)(aaaa)=a^7.
$$

### Potencia de una potencia

Si $m,n$ son enteros positivos,

$$
(a^m)^n=a^{mn}.
$$

Ahora el exponente exterior indica cuántas veces repetimos el bloque $a^m$. Cada bloque aporta $m$ factores, y hay $n$ bloques. En total aparecen $mn$ factores.

### Potencia de un producto

Para $a,b\in\mathbb R$ y $n>0$ entero,

$$
(ab)^n=a^n b^n.
$$

En efecto,

$$
(ab)^n=(ab)(ab)\cdots(ab),
$$

y por asociatividad y conmutatividad podemos reagrupar las $n$ copias de $a$ y las $n$ copias de $b$.

### El signo forma parte de la base

Una dificultad elemental, pero persistente, es confundir

$$
(-a)^n
$$

con

$$
-a^n.
$$

Los paréntesis determinan la base. Por ejemplo,

$$
(-2)^4=16,
$$

mientras que

$$
-2^4=-(2^4)=-16.
$$

Para una base negativa, la paridad del exponente controla el signo:

- si $n$ es par, $(-a)^n=a^n$;
- si $n$ es impar, $(-a)^n=-a^n$.

No es una convención adicional. Es consecuencia del número de factores negativos.

### Leer antes de operar

Considere

$$
(-x^2)^3.
$$

La base es $-x^2$, no $-x$. Por tanto

$$
(-x^2)^3=-(x^2)^3=-x^6.
$$

En cambio,

$$
(-x)^{2\cdot3}=(-x)^6=x^6.
$$

Una diferencia pequeña en la estructura produce resultados distintos.

### Micropráctica de autoexplicación

Explique verbalmente por qué los exponentes se **suman** en $a^ma^n$ y se **multiplican** en $(a^m)^n$. Una explicación correcta debe referirse a la cantidad de factores, no sólo citar la fórmula.

**Control razonado.** En $a^ma^n$ se concatenan dos listas con $m$ y $n$ factores: hay $m+n$ en total. En $(a^m)^n$ se repite $n$ veces una lista de $m$ factores: hay $mn$. Para exponentes positivos esto sigue del producto repetido; los exponentes cero y negativos se tratarán mediante la extensión de la definición.

***
## 18.3. Exponente cero y exponentes negativos: extender conservando leyes {#apm-c18-s03}

La interpretación como producto repetido sólo explica exponentes positivos. Para introducir $0$ y los enteros negativos, buscaremos definiciones que mantengan coherentes las leyes anteriores.

### ¿Qué debería significar $a^0$?

Suponga $a\neq0$. Si queremos conservar la regla del cociente, deberíamos tener

$$
\frac{a^m}{a^m}=a^{m-m}=a^0.
$$

Pero, como $a^m\neq0$,

$$
\frac{a^m}{a^m}=1.
$$

Esto motiva la definición

$$
\boxed{a^0=1\qquad(a\neq0).}
$$

El exponente cero no significa “multiplicar cero veces” en el mismo sentido elemental del producto repetido. Es una **extensión algebraicamente coherente** de la potencia.

En este capítulo no definiremos $0^0$. Diferentes áreas de las matemáticas emplean convenciones contextuales cuando resulta útil, pero aquí no necesitamos imponer ninguna.

### ¿Qué debería significar $a^{-n}$?

Sea $n>0$ y $a\neq0$. Si queremos que

$$
a^n a^{-n}=a^{n-n}=a^0=1,
$$

entonces $a^{-n}$ debe ser el inverso multiplicativo de $a^n$. Definimos

$$
\boxed{a^{-n}=\frac1{a^n}\qquad(a\neq0).}
$$

Por ejemplo,

$$
2^{-3}=\frac1{2^3}=\frac18.
$$

El signo del exponente **no** indica el signo del número. Así,

$$
(-2)^{-3}=\frac1{(-2)^3}=-\frac18,
$$

pero

$$
(-2)^{-4}=\frac1{(-2)^4}=\frac1{16}.
$$

### Por qué la base no puede ser cero

La expresión

$$
0^{-1}
$$

exigiría, por definición,

$$
0^{-1}=\frac10,
$$

que no existe en $\mathbb R$. La restricción $a\neq0$ no es decorativa: forma parte de la definición.

### Una consecuencia útil

Si $a\neq0$, entonces

$$
\frac1{a^{-n}}=a^n.
$$

En efecto,

$$
\frac1{a^{-n}}
=
\frac1{1/a^n}
=a^n.
$$

La idea de exponente negativo como inverso permite leer expresiones complejas con mayor claridad. Por ejemplo,

$$
\frac{x^{-2}y^3}{x^4y^{-1}}
$$

puede analizarse por base:

$$
x^{-2-4}y^{3-(-1)}=x^{-6}y^4=\frac{y^4}{x^6},
$$

siempre con

$$
x\neq0,
\qquad
y\neq0,
$$

porque la expresión original contiene potencias negativas de ambas bases.

***
## 18.4. Leyes de exponentes enteros con hipótesis explícitas {#apm-c18-s04}

Una vez definidos los exponentes cero y negativos, podemos reunir las leyes en un dominio uniforme.

**Teorema.** Sean $a,b\in\mathbb R\setminus\{0\}$ y $m,n\in\mathbb Z$. Entonces:

$$
a^m a^n=a^{m+n},
$$

$$
\frac{a^m}{a^n}=a^{m-n},
$$

$$
(a^m)^n=a^{mn},
$$

$$
(ab)^n=a^n b^n,
$$

$$
\left(\frac ab\right)^n=\frac{a^n}{b^n}.
$$

**Demostración.** Para la ley del producto de igual base, los exponentes positivos concatenan factores; un exponente cero aporta uno. Si $m\ge0$ y $n=-k<0$, se tiene $a^ma^{-k}=a^m/a^k$: cancelar factores da $a^{m-k}$ si $m\ge k$ y $1/a^{k-m}=a^{m-k}$ si $m<k$. El caso con los signos intercambiados usa conmutatividad. Si ambos son negativos, $a^{-j}a^{-k}=1/(a^ja^k)=a^{-(j+k)}$. Esto cubre todos los pares de enteros y demuestra la primera ley.

En particular $a^na^{-n}=1$, así que $1/a^n=a^{-n}$ para todo $n\in\mathbb Z$. El cociente se convierte en $a^ma^{-n}=a^{m-n}$. Para la potencia de potencia, si $n>0$ el producto de $n$ copias de $a^m$ tiene exponente $mn$ por la primera ley; si $n=0$ ambos lados valen uno; si $n=-k<0$, se obtiene $1/(a^m)^k=1/a^{mk}=a^{-mk}$. La potencia de un producto se demuestra reagrupando factores para $n>0$, vale uno para $n=0$ y para $n=-k$ se sigue de $1/(ab)^k=1/(a^kb^k)=a^{-k}b^{-k}$. Finalmente se aplica esa ley al producto $a(1/b)$; la ley de potencia de potencia da $(1/b)^n=(b^{-1})^n=b^{-n}=1/b^n$. Queda demostrada también la ley del cociente. $\square$

La hipótesis $a,b\neq0$ permite enunciar todas las leyes de una sola vez incluso cuando aparecen exponentes negativos. En casos particulares con exponentes no negativos puede existir un dominio más amplio.

### Ejemplo: una cadena con control de dominio

Suponga $x,y\neq0$. Entonces

$$
\frac{(x^{-2}y^3)^2}{x^{-1}y^4}
=
\frac{x^{-4}y^6}{x^{-1}y^4}
=
x^{-3}y^2
=
\frac{y^2}{x^3}.
$$

Cada igualdad usa una ley concreta:

1. potencia de un producto;
2. potencia de una potencia;
3. cociente de potencias de igual base;
4. definición de exponente negativo.

La forma final aislada está definida para $x\neq0$ aunque ya no muestre ninguna potencia negativa. La cadena conserva las dos restricciones originales, $x\ne0$ e $y\ne0$; no se reincorpora $y=0$ por haber desaparecido su potencia negativa.

### Lo que las leyes no dicen

Las leyes de exponentes gobiernan productos, cocientes y potencias de potencias. No permiten distribuir un exponente sobre una suma:

$$
(a+b)^n\neq a^n+b^n
$$

en general.

Por ejemplo,

$$
(1+1)^2=4,
$$

pero

$$
1^2+1^2=2.
$$

Tampoco existe una ley que permita “cancelar exponentes” atravesando una suma. El tipo de operación importa.

### Estrés de hipótesis

Considere la igualdad

$$
\frac{x^5}{x^2}=x^3.
$$

Es correcta para $x\neq0$. En $x=0$ el lado derecho tiene sentido, pero el izquierdo no. La forma simplificada tiene un dominio mayor que la forma original.

Una transformación algebraica puede producir una expresión más simple **sin convertirla en la misma función sobre un dominio mayor**.

***
## 18.5. Raíz $n$-ésima y paridad del índice {#apm-c18-s05}

Las potencias permiten avanzar desde una base hacia un resultado. Las raíces plantean la pregunta inversa: dado un resultado, ¿qué base produjo ese valor al elevarla a cierta potencia?

La respuesta depende decisivamente de si el índice es par o impar.

### Raíz principal de índice par

Sea $n\ge2$ par y $a\ge0$. Definimos $\sqrt[n]{a}$ como el único número real **no negativo** $b$ tal que

$$
b^n=a.
$$

Por ejemplo,

$$
\sqrt[4]{16}=2
$$

porque $2\ge0$ y $2^4=16$.

Aunque también $(-2)^4=16$, el símbolo $\sqrt[4]{16}$ no representa “las dos raíces”. Representa la raíz principal no negativa.

### Raíz de índice impar

Sea $n\ge3$ impar y $a\in\mathbb R$. Existe un único real $b$ tal que

$$
b^n=a.
$$

Definimos ese número como $\sqrt[n]{a}$.

Por ejemplo,

$$
\sqrt[3]{-8}=-2
$$

porque

$$
(-2)^3=-8.
$$

A diferencia de los índices pares, los índices impares admiten radicandos negativos en $\mathbb R$.

### Raíz principal no es conjunto de soluciones

La notación

$$
\sqrt9=3
$$

nombra un solo número: la raíz cuadrada principal de $9$.

En cambio, la ecuación

$$
x^2=9
$$

tiene dos soluciones, $x=3$ y $x=-3$.

No escribiremos

$$
\sqrt9=\pm3.
$$

Esa escritura confunde una función de raíz principal con un conjunto de soluciones de una ecuación. La resolución sistemática de ecuaciones quedará para C21.

### Paridad y dominio

Compare:

$$
\sqrt[4]{-16}
$$

y

$$
\sqrt[3]{-27}.
$$

La primera expresión no representa un número real; la segunda vale $-3$.

El índice no es un detalle tipográfico. Determina qué radicandos son admisibles.

***
## 18.6. Por qué $\sqrt{a^2}=|a|$ {#apm-c18-s06}

Una de las identidades más importantes de este capítulo es

$$
\boxed{\sqrt{a^2}=|a|.}
$$

La presencia del valor absoluto no es una corrección artificial. Se sigue directamente de la definición de raíz principal.

### Demostración por casos

Sea $a\in\mathbb R$.

Si $a\ge0$, entonces $a$ es no negativo y

$$
a^2=a^2.
$$

Por unicidad de la raíz cuadrada principal,

$$
\sqrt{a^2}=a=|a|.
$$

Si $a<0$, entonces $-a>0$ y

$$
(-a)^2=a^2.
$$

Como $-a$ es no negativo, es la raíz cuadrada principal de $a^2$. Por tanto

$$
\sqrt{a^2}=-a=|a|.
$$

En ambos casos,

$$
\sqrt{a^2}=|a|.
$$

$\square$

### Consecuencia inmediata

No podemos simplificar

$$
\sqrt{(x-3)^2}
$$

como $x-3$ sin conocer el signo de $x-3$. La forma válida para todo real es

$$
\boxed{\sqrt{(x-3)^2}=|x-3|.}
$$

### Generalización

Para $n\ge2$ entero y $a\in\mathbb R$:

$$
\sqrt[n]{a^n}
=
\begin{cases}
|a|,&n\text{ par},\\
a,&n\text{ impar}.
\end{cases}
$$

Si $n$ es par, la raíz principal debe ser no negativa; por eso aparece $|a|$. Si $n$ es impar, la potencia $a^n$ conserva el signo de $a$, y la raíz impar recupera exactamente $a$.

### Ejemplos

$$
\sqrt{x^2y^4}
=
\sqrt{x^2}\sqrt{y^4}
=
|x|\,y^2,
$$

si utilizamos la regla del producto en un contexto donde ambos radicandos son no negativos. Observe que $y^2\ge0$, de modo que

$$
\sqrt{y^4}=|y^2|=y^2.
$$

También

$$
\sqrt[4]{x^8}=x^2,
$$

porque

$$
\sqrt[4]{x^8}=|x^2|=x^2.
$$

La pregunta correcta no es “¿puedo cancelar la raíz con la potencia?”, sino “¿qué información sobre el signo debe conservar la raíz principal?”.

### Nota pedagógica — Una longitud no conserva la orientación

Sobre la recta real, $a$ registra posición y signo; $|a|$ registra distancia al origen. Al pasar de $a$ a $a^2$, las posiciones $a$ y $-a$ se identifican. La raíz cuadrada principal recupera la longitud, pues por definición debe ser no negativa. No dispone de la información necesaria para elegir la posición original.

**Control resuelto.** Los desplazamientos tres y menos tres tienen el mismo cuadrado, nueve. La raíz principal devuelve tres en ambos casos. Para un punto $x$ y una referencia $c$, $\sqrt{(x-c)^2}=|x-c|$ mide la distancia a $c$; vale $x-c$ si $x\ge c$ y $c-x$ si $x<c$. Con $c=2$, los puntos cinco y menos uno están a distancia tres, aunque sus desplazamientos respecto de dos tengan signos opuestos.

La misma lectura controla una extracción algebraica. $\sqrt{u^2v^4}=|uv^2|=|u|v^2$ para todos $u,v\in\mathbb R$. Si $v=0$, el resultado es cero sea cual sea el signo de $u$. Si $v\ne0$, suprimir el valor absoluto de $u$ exige $u\ge0$. Antes de escribir una condición «necesaria», revisa si otro factor puede anular todo el producto.

Para recuperar esta idea, vuelve a la definición de raíz principal en [§18.5](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s05) y verifica las dos condiciones del candidato: no negatividad y potencia correcta. La igualdad de cuadrados, sin la condición de signo, no identifica una raíz principal.

***
## 18.7. Exponentes racionales sobre bases positivas {#apm-c18-s07}

Queremos ahora dar sentido a expresiones como

$$
a^{1/2},
\qquad
a^{2/3},
\qquad
a^{-5/4}.
$$

La guía será la misma de antes: extender la notación conservando las leyes de exponentes.

Sea $a>0$ y sea

$$
r=\frac mn
$$

un número racional escrito en términos mínimos, con $m\in\mathbb Z$ y $n\in\mathbb N$ positivo. Si $n=1$, se conserva la potencia entera ya definida; en las fórmulas de esta sección se entiende $\sqrt[1]{a}=a$.

Definimos

$$
\boxed{
a^{m/n}=\left(\sqrt[n]{a}\right)^m.
}
$$

Cuando $m>0$, también podemos escribir

$$
a^{m/n}=\sqrt[n]{a^m}.
$$

Por ejemplo,

$$
8^{2/3}
=
\left(\sqrt[3]{8}\right)^2
=2^2
=4.
$$

Y

$$
16^{3/4}
=
\left(\sqrt[4]{16}\right)^3
=2^3
=8.
$$

### Exponentes racionales negativos

Si $a>0$ y $m>0$, definimos

$$
a^{-m/n}=\frac1{a^{m/n}}.
$$

Por ejemplo,

$$
9^{-3/2}
=
\frac1{9^{3/2}}
=
\frac1{(\sqrt9)^3}
=
\frac1{27}.
$$

### Las leyes se conservan en bases positivas

Para $a,b>0$ y $r,s\in\mathbb Q$, las leyes familiares continúan siendo válidas:

$$
a^r a^s=a^{r+s},
$$

$$
\frac{a^r}{a^s}=a^{r-s},
$$

$$
(a^r)^s=a^{rs},
$$

$$
(ab)^r=a^r b^r,
$$

$$
\left(\frac ab\right)^r=\frac{a^r}{b^r}.
$$

**Demostración de independencia y leyes.** Primero, si $m/n=p/q$ con $n,q>0$, los candidatos positivos $u=(\sqrt[n]a)^m$ y $v=(\sqrt[q]a)^p$ satisfacen $u^{nq}=a^{mq}$ y $v^{nq}=a^{pn}$. Las potencias enteras ya están justificadas; como $mq=np$, la unicidad de la raíz positiva da $u=v$. Así se puede usar una fracción no reducida en bases positivas sin cambiar el valor.

Para $r=m/n$, $s=p/q$, sea $w=\sqrt[nq]a>0$. La unicidad da $\sqrt[n]a=w^q$ y $\sqrt[q]a=w^n$, por lo que $a^ra^s=w^{mq}w^{pn}=w^{mq+pn}=a^{r+s}$. Además $a^sa^{-s}=a^0=1$, y el cociente resulta de multiplicar por $a^{-s}$.

Para la potencia de potencia, pon $b=a^{m/n}$ y $u=b^{p/q}$. Se tiene $b^n=a^m$, $u^q=b^p$ y por tanto $u^{nq}=a^{mp}$. El candidato positivo $v=a^{mp/(nq)}$ tiene la misma potencia $nq$, de modo que $u=v$ por unicidad. Esto incluye numeradores cero y negativos, pues todas las bases son positivas.

Finalmente, $\sqrt[n]a\sqrt[n]b$ es positivo y su potencia $n$ vale $ab$; por unicidad es $\sqrt[n]{ab}$. Elevar esta igualdad al entero $m$ prueba $(ab)^{m/n}=a^{m/n}b^{m/n}$. Con $b$ reemplazado por $1/b$ y $(b^{-1})^r=b^{-r}=1/b^r$, se obtiene la ley del cociente. El índice uno sólo usa la identidad. $\square$

La condición de positividad evita los problemas de dominio y representación que aparecerán en la sección siguiente.

### Dos representaciones del mismo objeto

Para $a>0$,

$$
a^{3/5}
$$

y

$$
\sqrt[5]{a^3}
$$

representan el mismo número. La elección de una u otra forma puede depender de la tarea.

Por ejemplo, para combinar potencias con exponentes distintos suele ser útil la notación exponencial:

$$
a^{1/2}a^{1/3}
=
a^{3/6}a^{2/6}
=
a^{5/6}.
$$

En cambio, si el objetivo es reconocer una raíz concreta, puede ser más informativo escribir

$$
a^{1/3}=\sqrt[3]{a}.
$$

La equivalencia de formas no elimina la necesidad de elegir estratégicamente.

***
## 18.8. Bases cero y negativas: el borde donde las reglas dejan de ser automáticas {#apm-c18-s08}

La teoría de exponentes racionales es especialmente limpia para bases positivas. En $0$ y en las bases negativas aparecen fronteras que debemos examinar explícitamente.

### Base cero

Si $r>0$ es racional, definimos

$$
0^r=0
$$

cuando la expresión radical correspondiente tiene sentido; en esta situación el valor siempre es $0$.

Pero si $r<0$, la definición exigiría un recíproco de $0$ y por tanto la expresión no está definida.

Así,

$$
0^{3/2}=0,
$$

mientras que

$$
0^{-3/2}
$$

no está definido.

Como ya acordamos,

$$
0^0
$$

no recibe un valor en este capítulo.

### Bases negativas y fracciones reducidas

Sea $a<0$ y

$$
r=\frac mn
$$

escrito en términos mínimos, con $n>0$.

- Si $n$ es impar, podemos definir $a^{m/n}$ mediante la raíz impar real.
- Si $n$ es par, $a^{m/n}$ no es un número real.

Por ejemplo,

$$
(-8)^{1/3}=-2,
$$

$$
(-8)^{2/3}=(-2)^2=4,
$$

pero

$$
(-8)^{1/2}
$$

no es real.

### Por qué debemos reducir primero el exponente

Considere

$$
(-8)^{2/6}.
$$

Como número racional,

$$
\frac26=\frac13.
$$

Nuestra definición debe depender del número racional, no de una escritura accidental. Por tanto

$$
(-8)^{2/6}=(-8)^{1/3}=-2.
$$

Si, en cambio, se intentara usar directamente la representación $2/6$ como

$$
\sqrt[6]{(-8)^2}=\sqrt[6]{64}=2,
$$

obtendríamos otro valor. Esta contradicción muestra por qué **no podemos definir exponentes racionales con bases negativas a partir de cualquier representación no reducida de la fracción**.

### Una ley que deja de ser automática

Para bases positivas tenemos

$$
(a^r)^s=a^{rs}.
$$

Con bases negativas, esta ley no puede utilizarse indiscriminadamente.

Observe:

$$
(-8)^{2/3}=4.
$$

Luego

$$
\left((-8)^{2/3}\right)^{3/2}=4^{3/2}=8.
$$

Pero si combináramos formalmente los exponentes sin examinar el dominio,

$$
(-8)^{(2/3)(3/2)}=(-8)^1=-8.
$$

Los resultados difieren. La regla que era segura para bases positivas no sobrevivió sin condiciones.

La lección es más importante que este ejemplo particular:

> **Cuando una extensión algebraica depende del dominio, una manipulación formal puede cruzar una frontera donde la ley deja de ser válida.**

### Nota pedagógica — El racional se mantiene; la receta radical puede cambiar

Para $a>0$, la independencia de escritura se prueba comparando raíces positivas. Si $m/n=p/q$ con denominadores positivos, los candidatos $(\sqrt[n]a)^m$ y $(\sqrt[q]a)^p$ son positivos y, por las leyes enteras, sus potencias $nq$ valen $a^{mq}$ y $a^{pn}$. Esos valores son iguales porque $mq=np$. La unicidad de la raíz positiva obliga a que los candidatos coincidan, incluso con numeradores negativos. El índice uno se interpreta como la identidad.

Para $a<0$, primero se determina el denominador de la fracción reducida. Una escritura con denominador par no vuelve irreal una potencia que ya está definida; lo que puede dejar de servir es una receta radical construida a partir de esa escritura.

**Control resuelto.** Como $-2/3=-4/6=-6/9$, las tres escrituras de $(-8)^r$ nombran el mismo valor, $1/4$. La receta $\sqrt[6]{(-8)^{-4}}$ también produce $1/4$, pero eso no demuestra que las recetas con denominador par funcionen siempre: para $r=-1/3=-2/6$, la potencia es $-1/2$ y $\sqrt[6]{(-8)^{-2}}=1/2$. En el primer caso se conservó el valor porque el resultado era positivo; en el segundo se perdió el signo. La receta $(\sqrt[6]{-8})^{-2}$ ni siquiera existe en los reales.

Una comprobación numérica puede revelar el error, pero la decisión general se toma antes de calcular: reduce el exponente, comprueba existencia y registra el signo dado por el numerador. Después decide qué expresión radical conserva esos datos. Si falla ese paso, recupera [§18.5](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s05) para la paridad del índice y [§18.3](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s03) para los exponentes negativos.

***
## 18.9. Simplificar radicales: extraer estructura, no “sacar números” {#apm-c18-s09}

Simplificar un radical significa reconocer dentro del radicando potencias perfectas compatibles con el índice.

Por ejemplo,

$$
\sqrt{72}
=
\sqrt{36\cdot2}
=
6\sqrt2.
$$

No hemos “sacado el $36$”. Hemos usado que $36=6^2$ y que, para factores no negativos,

$$
\sqrt{36\cdot2}=\sqrt{36}\sqrt2.
$$

### Un ejemplo algebraico con signo

Considere

$$
\sqrt{18x^2}.
$$

Como

$$
18x^2=9\cdot2\cdot x^2,
$$

obtenemos

$$
\sqrt{18x^2}
=3\sqrt2\,|x|.
$$

La forma

$$
3x\sqrt2
$$

sólo sería válida bajo la hipótesis adicional $x\ge0$.

### Índice impar

Para raíces impares no aparece el valor absoluto al extraer una potencia del mismo índice. Por ejemplo,

$$
\sqrt[3]{-54}
=
\sqrt[3]{(-27)\cdot2}
=-3\sqrt[3]2.
$$

También

$$
\sqrt[3]{x^3y^4}
=
xy\sqrt[3]y.
$$

Aquí $x$ puede ser positivo, negativo o cero.

### Incorporar factores al radical

La operación inversa también requiere atención al signo. Si $c\ge0$, entonces

$$
c\sqrt a=\sqrt{c^2a}
$$

cuando las expresiones están definidas.

Pero si $c<0$, la igualdad anterior no puede ser correcta porque el lado derecho es no negativo y el izquierdo es negativo cuando $a>0$.

Para índices pares, introducir un factor dentro de una raíz exige controlar el signo del factor exterior. Para índices impares, la situación es más flexible porque la raíz conserva el signo.

### Estrategia de simplificación

Una rutina útil es:

```text
1. IDENTIFICAR EL ÍNDICE.
2. FACTORIZAR EL RADICANDO EN POTENCIAS PERFECTAS Y RESTO.
3. EXTRAER LAS POTENCIAS COMPLETAS.
4. SI EL ÍNDICE ES PAR, CONTROLAR VALORES ABSOLUTOS.
5. VERIFICAR QUE EL DOMINIO ORIGINAL SIGUE REGISTRADO.
```

No siempre conviene factorizar completamente un número. Conviene factorizar lo suficiente para hacer visibles las potencias compatibles con el índice.

***
## 18.10. Producto y cociente de radicales {#apm-c18-s10}

Las reglas de producto y cociente de radicales son útiles, pero deben formularse con el dominio incluido.

### Raíz cuadrada de un producto

Si $a,b\ge0$, entonces

$$
\boxed{\sqrt{ab}=\sqrt a\,\sqrt b.}
$$

Por ejemplo,

$$
\sqrt{12}\sqrt3
=
\sqrt{36}
=6.
$$

Podríamos también simplificar primero $\sqrt{12}=2\sqrt3$ y obtener

$$
2\sqrt3\sqrt3=6.
$$

Dos rutas válidas pueden tener distinta longitud.

### Raíz cuadrada de un cociente

Si $a\ge0$ y $b>0$, entonces

$$
\boxed{
\sqrt{\frac ab}
=
\frac{\sqrt a}{\sqrt b}.
}
$$

La condición $b>0$ combina dos necesidades: la fracción original exige $b\neq0$ y la raíz cuadrada del denominador exige $b\ge0$.

### Justificación de las reglas radicales

Para el producto cuadrático, el candidato $c=\sqrt a\sqrt b$ es no negativo y $c^2=ab$, por las leyes enteras. La unicidad de la raíz principal da $c=\sqrt{ab}$. Para el cociente, $c=\sqrt a/\sqrt b$ existe y es no negativo cuando $a\ge0$, $b>0$; además $c^2=a/b$. La misma unicidad prueba la fórmula.

Este argumento vale para cualquier índice par $n\ge2$: se verifica no negatividad y potencia $n$ correcta. Para índice impar $n\ge3$, el producto $c=\sqrt[n]a\sqrt[n]b$ satisface $c^n=ab$ para cualesquiera reales $a,b$; la unicidad de la raíz impar basta, sin condición de signo. Para el cociente con $b\ne0$, la raíz del denominador es no nula y el candidato tiene potencia $n$ igual a $a/b$. Quedan así justificadas también las reglas impares enunciadas abajo. Estas pruebas admiten radicandos cero donde el denominador no se anule.

### Por qué no debemos borrar las hipótesis

La igualdad

$$
\sqrt{ab}=\sqrt a\sqrt b
$$

no es una identidad universal en los reales. Si $a=b=-1$, entonces $ab=1$ y el lado izquierdo es real, pero las raíces del lado derecho no lo son.

Una fórmula puede ser algebraicamente familiar y aun así tener un dominio más estrecho que las expresiones que aparecen por separado.

### Índices impares

Para $n$ impar y $a,b\in\mathbb R$,

$$
\sqrt[n]{ab}=\sqrt[n]a\,\sqrt[n]b.
$$

Y si $b\neq0$,

$$
\sqrt[n]{\frac ab}
=
\frac{\sqrt[n]a}{\sqrt[n]b}.
$$

Las raíces impares no exigen no negatividad del radicando.

### Una advertencia estructural

Producto y suma son operaciones distintas. De

$$
\sqrt{ab}=\sqrt a\sqrt b
$$

no se sigue ninguna regla del tipo

$$
\sqrt{a+b}=\sqrt a+\sqrt b.
$$

La sección siguiente analizará esta diferencia.

***
## 18.11. Sumar radicales exige reconocer términos semejantes {#apm-c18-s11}

Los radicales pueden sumarse cuando, después de simplificar, comparten la misma parte radical.

Por ejemplo,

$$
\sqrt8+\sqrt{18}
=
2\sqrt2+3\sqrt2
=5\sqrt2.
$$

La última igualdad no usa una “ley de raíces”. Usa la propiedad distributiva:

$$
2\sqrt2+3\sqrt2=(2+3)\sqrt2.
$$

### Radicales semejantes

Expresiones como

$$
3\sqrt5
\qquad\text{y}\qquad
-7\sqrt5
$$

son semejantes respecto de su parte radical y pueden combinarse:

$$
3\sqrt5-7\sqrt5=-4\sqrt5.
$$

En cambio,

$$
\sqrt2+\sqrt3
$$

no puede reducirse mediante una combinación lineal inmediata porque las partes radicales son distintas.

### La falsa distribución sobre la suma

No existe en general la identidad

$$
\sqrt{a+b}=\sqrt a+\sqrt b.
$$

Basta un contraejemplo:

$$
\sqrt{9+16}=5,
$$

mientras que

$$
\sqrt9+\sqrt{16}=3+4=7.
$$

La confusión suele venir de transportar una regla válida para productos hacia una suma, sin reconocer que las operaciones son diferentes.

### Simplificar antes de decidir

Considere

$$
\sqrt{12}+\sqrt{27}.
$$

A primera vista las raíces son distintas. Pero

$$
\sqrt{12}=2\sqrt3,
\qquad
\sqrt{27}=3\sqrt3,
$$

y por tanto

$$
\sqrt{12}+\sqrt{27}=5\sqrt3.
$$

La semejanza estaba oculta por la forma original.

Esta es una primera muestra de **foresight algebraico**: antes de ejecutar una operación, preguntarse qué forma hará visible la estructura útil.

***
## 18.12. Racionalización: cambiar de forma con un objetivo {#apm-c18-s12}

Racionalizar significa transformar una expresión para eliminar ciertos radicales de un denominador —o, en contextos específicos, de un numerador— sin cambiar su valor en el dominio considerado.

La técnica es útil. Pero no debemos convertirla en un mandato sin propósito.

### Denominador monomial

Si $a>0$,

$$
\frac1{\sqrt a}
=
\frac1{\sqrt a}\cdot\frac{\sqrt a}{\sqrt a}
=
\frac{\sqrt a}{a}.
$$

Por ejemplo,

$$
\frac3{2\sqrt5}
=
\frac3{2\sqrt5}\cdot\frac{\sqrt5}{\sqrt5}
=
\frac{3\sqrt5}{10}.
$$

La operación multiplica por una forma de $1$. No cambia el valor.

### Conjugados

Cuando el denominador tiene la forma

$$
u-v
$$

con radicales cuadráticos, puede ser útil multiplicar por el conjugado $u+v$. La razón es la identidad

$$
(u-v)(u+v)=u^2-v^2,
$$

que se obtiene directamente de la distributividad.

Por ejemplo,

$$
\frac1{\sqrt{x+1}-\sqrt x},
\qquad x\ge0.
$$

Multiplicamos por el conjugado:

$$
\frac1{\sqrt{x+1}-\sqrt x}
\cdot
\frac{\sqrt{x+1}+\sqrt x}{\sqrt{x+1}+\sqrt x}.
$$

El denominador se convierte en

$$
(x+1)-x=1.
$$

Por tanto

$$
\boxed{
\frac1{\sqrt{x+1}-\sqrt x}
=
\sqrt{x+1}+\sqrt x,
\qquad x\ge0.
}
$$

Aquí la racionalización produce una simplificación notable.

### Pero no siempre racionalizar mejora la forma

Compare

$$
\frac1{\sqrt x}
$$

con

$$
\frac{\sqrt x}{x}.
$$

Ambas formas son equivalentes para $x>0$. Dependiendo del problema, una puede ser más útil que la otra.

Si el objetivo es reconocer una potencia,

$$
\frac1{\sqrt x}=x^{-1/2}
$$

puede ser la representación más informativa. Si el objetivo es eliminar radicales del denominador en una expresión numérica, la forma racionalizada puede ser preferible.

La pregunta madura no es “¿ya racionalicé?”, sino:

> **¿Qué forma revela mejor la estructura que necesito para el siguiente paso?**

***
## 18.13. Elegir entre notación radical y exponente racional {#apm-c18-s13}

Una misma cantidad puede escribirse de maneras distintas. La fluidez algebraica incluye saber **cambiar de representación con una razón**.

Para $a>0$:

$$
\sqrt[n]{a^m}=a^{m/n}.
$$

Ninguna de las dos notaciones es universalmente superior.

### Cuando conviene el exponente racional

Considere

$$
\sqrt x\,\sqrt[3]x,
\qquad x>0.
$$

En notación radical los índices son distintos. En notación exponencial,

$$
\sqrt x\,\sqrt[3]x
=x^{1/2}x^{1/3}
=x^{5/6}.
$$

La suma de exponentes se vuelve visible inmediatamente.

Otro ejemplo:

$$
\frac{x^{3/2}x^{-1/3}}{x^{1/6}}
=
x^{3/2-1/3-1/6}
=
x^1=x,
$$

para $x>0$.

### Cuando conviene la notación radical

Considere

$$
16^{3/4}.
$$

Escribir

$$
\left(\sqrt[4]{16}\right)^3
$$

hace visible una evaluación inmediata:

$$
2^3=8.
$$

También, al estudiar dominio, una expresión como

$$
\sqrt[4]{x-2}
$$

hace visible de inmediato que el radicando debe ser no negativo. La forma

$$
(x-2)^{1/4}
$$

representa lo mismo en los reales, pero puede ocultar al lector inexperto la restricción.

### Criterios de elección

Antes de cambiar de forma, pregunte:

- ¿necesito combinar exponentes?
- ¿necesito ver una raíz concreta?
- ¿necesito hacer visible el dominio?
- ¿necesito comparar términos semejantes?
- ¿necesito racionalizar?

El cambio de representación es una decisión matemática, no un gesto tipográfico.

### Micropráctica estratégica

Sin efectuar toda la simplificación, decida qué representación usaría primero en cada caso:

$$
\sqrt[3]{x^2}\sqrt[6]x,
$$

$$
81^{3/4},
$$

$$
\frac1{\sqrt{x+2}},
$$

$$
\sqrt{12}+\sqrt{27}.
$$

La respuesta debe incluir una razón.

**Control razonado.** En $\sqrt[3]{x^2}\sqrt[6]x$ convienen exponentes para sumar $2/3+1/6=5/6$, con dominio $x\ge0$; si $x=0$, ambos factores valen cero y se verifica directamente. Para $81^{3/4}$ conviene la raíz cuarta de 81, que es tres, y luego su cubo: 27. Para $1/\sqrt{x+2}$, la forma radical revela $x>-2$; una racionalización sólo se justifica si sirve a una tarea posterior. Para $\sqrt{12}+\sqrt{27}$ conviene extraer cuadrados: $2\sqrt3+3\sqrt3=5\sqrt3$.

***
## 18.14. Dominios de expresiones con varias restricciones {#apm-c18-s14}

En expresiones reales de varias capas, el dominio se obtiene **intersectando todas las condiciones necesarias**.

No basta revisar la última operación. Debemos inspeccionar cada componente.

### Radical de índice par y denominador

Considere

$$
E(x)=\frac{\sqrt{x-1}}{x-3}.
$$

La raíz exige

$$
x-1\ge0,
$$

mientras que el denominador exige

$$
x\neq3.
$$

Por tanto el dominio es

$$
\{x\in\mathbb R:x\ge1,\ x\neq3\}.
$$

No hemos resuelto una ecuación. Hemos leído las condiciones de existencia de la expresión.

### Radical en el denominador

Considere

$$
F(x)=\frac1{\sqrt{x+2}}.
$$

No basta exigir $x+2\ge0$. Como la raíz aparece además en un denominador, debe ser distinta de cero. Por tanto

$$
x+2>0,
$$

y el dominio es

$$
x>-2.
$$

### Varias restricciones simultáneas

Considere

$$
G(x)=\frac{\sqrt{x+4}}{\sqrt x\,(x-2)}.
$$

Las condiciones son:

- $x+4\ge0$ por la raíz del numerador;
- $x\ge0$ por $\sqrt x$;
- $\sqrt x\neq0$, luego $x\neq0$;
- $x\neq2$ por el segundo factor del denominador.

La intersección se reduce a

$$
x>0,
\qquad
x\neq2.
$$

### Simplificar sin ampliar el dominio

Considere

$$
H(x)=\frac{\sqrt{(x-1)^2}}{x-1}.
$$

La raíz existe para todo real, pero el denominador exige $x\neq1$. Además,

$$
\sqrt{(x-1)^2}=|x-1|.
$$

Por tanto

$$
H(x)=\frac{|x-1|}{x-1},
\qquad x\neq1.
$$

No podemos cancelar el numerador con el denominador porque $|x-1|$ no es igual a $x-1$ para todos los valores del dominio.

Este ejemplo reúne tres hilos del libro:

```text
DOMINIO
+
VALOR ABSOLUTO
+
TRANSFORMACIÓN JUSTIFICADA
```

### Nota pedagógica — Restricciones por capas y recuperación

Las restricciones de una expresión se acumulan; ninguna simplificación posterior las borra. Conviene registrar de qué operación procede cada una para no confundir una raíz existente con un denominador admisible.

**Control resuelto.** Considera

$$
J(x)=\frac{\sqrt{4-\sqrt x}}{(\sqrt x-1)(x-9)}.
$$

| Capa | Condición | Qué se recupera si hay duda |
|---|---|---|
| Raíz interior | $x\ge0$ | [§18.5](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s05): raíz cuadrada real |
| Raíz exterior | $4-\sqrt x\ge0$ | [§18.14](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s14): leer el radicando completo |
| Primer factor del denominador | $\sqrt x\ne1$ | [§18.5](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s05): raíz principal y potencia correcta |
| Segundo factor del denominador | $x\ne9$ | [§18.1](algebra-para-matematicos-capitulo-18-potencias-exponentes-racionales-y-radicales.md#apm-c18-s01): no división por cero |

Con $x\ge0$, la segunda condición equivale a $x\le16$: para números no negativos, comparar sus cuadrados conserva el orden, pues $v^2-u^2=(v-u)(v+u)$ tiene el signo de $v-u$ cuando $v+u>0$, y el caso ambos cero se comprueba directamente. Además, $\sqrt x=1$ equivale a $x=1$ por la definición de raíz principal. Por tanto el dominio exacto es $[0,16]\setminus\{1,9\}$. Los extremos cero y dieciséis están permitidos; los puntos uno y nueve se excluyen aunque las raíces existan.

La verificación tiene dos direcciones. Cada punto del conjunto declarado satisface todas las capas, así que la expresión existe allí. Un punto exterior incumple alguna capa, así que no puede añadirse. Esta doble revisión evita que una lista de condiciones necesarias se confunda con una descripción suficiente del dominio.

***
## 18.15. Laboratorio P3 — el primer paso inválido {#apm-c18-s15}

Una cadena algebraica incorrecta puede contener varios pasos posteriores formalmente correctos. Por eso, para diagnosticarla, no basta señalar que “el resultado está mal”. Hay que localizar **el primer paso que dejó de estar justificado**.

Usaremos este protocolo:

```text
1. LEER LA CADENA COMPLETA.
2. MARCAR EL PRIMER PASO NO JUSTIFICADO.
3. NOMBRAR LA REGLA QUE SE INTENTÓ USAR.
4. IDENTIFICAR LA HIPÓTESIS QUE FALTA O LA REGLA FALSA.
5. REPARAR DESDE ESE PUNTO.
6. CONSERVAR EL DOMINIO ORIGINAL.
```

### Diagnóstico 1 — valor absoluto perdido

Supongamos que alguien escribe

$$
\sqrt{(x-4)^2}=x-4.
$$

El primer paso ya es inválido como identidad universal. La regla correcta es

$$
\sqrt{u^2}=|u|.
$$

Por tanto

$$
\sqrt{(x-4)^2}=|x-4|.
$$

La forma $x-4$ sólo sería válida bajo una hipótesis adicional que garantizara $x-4\ge0$.

### Diagnóstico 2 — exponente racional no reducido

Cadena propuesta:

$$
(-8)^{2/6}
=
\sqrt[6]{(-8)^2}
=
\sqrt[6]{64}
=2.
$$

El primer paso es inválido bajo nuestra definición para bases negativas: el exponente racional debe interpretarse como número racional en forma reducida. Como

$$
\frac26=\frac13,
$$

la reparación comienza con

$$
(-8)^{2/6}=(-8)^{1/3}=-2.
$$

### Diagnóstico 3 — raíz distribuida sobre una suma

Cadena propuesta:

$$
\sqrt{x+9}=\sqrt x+3.
$$

No existe una ley de distribución de la raíz sobre la suma. Un contraejemplo basta para destruir la identidad. Con $x=7$:

$$
\sqrt{7+9}=4,
$$

mientras que

$$
\sqrt7+3\neq4.
$$

### Diagnóstico 4 — simplificación correcta, dominio olvidado

Cadena propuesta:

$$
\frac{x^{-2}}{x^{-5}}
=x^3.
$$

El cálculo es correcto, pero si la conclusión se declara “para todo real $x$”, el razonamiento es inválido. La expresión original requiere $x\neq0$.

La reparación es

$$
\frac{x^{-2}}{x^{-5}}=x^3,
\qquad x\neq0.
$$

### Diagnóstico 5 — producto de radicales fuera de dominio

Cadena propuesta:

$$
\sqrt{(-2)(-8)}
=
\sqrt{-2}\sqrt{-8}.
$$

El lado izquierdo está definido en $\mathbb R$ y vale $4$. El lado derecho no está definido en $\mathbb R$. La regla del producto para raíces cuadradas se aplicó sin las hipótesis $a,b\ge0$.

### Diagnóstico 6 — una ley válida en bases positivas usada en una base negativa

Cadena propuesta:

$$
\left((-8)^{2/3}\right)^{3/2}
=
(-8)^{(2/3)(3/2)}
=-8.
$$

El primer paso utiliza sin control la ley $(a^r)^s=a^{rs}$ en un contexto donde la base inicial es negativa. El lado izquierdo vale

$$
4^{3/2}=8,
$$

y por tanto la igualdad propuesta es falsa.

### Qué debe aprenderse del laboratorio

Estos errores no son todos del mismo tipo:

- algunos pierden una condición de signo;
- otros usan una regla falsa;
- otros usan una regla válida fuera de su dominio;
- otros simplifican correctamente pero olvidan el dominio original;
- otros confunden una representación de un racional con el racional mismo.

Diagnosticar exige reconocer **qué clase de error ocurrió**.

***
## 18.16. Cierre — protocolo de potencias y radicales {#apm-c18-s16}

El capítulo comenzó con una pregunta: ¿cómo extender la potencia sin convertir las leyes de exponentes en reglas ciegas?

La respuesta puede resumirse en un protocolo reutilizable.

```text
1. ¿CUÁL ES EL DOMINIO REAL DE LA EXPRESIÓN?

2. ¿EL EXPONENTE ES ENTERO O RACIONAL?

3. SI EL EXPONENTE ES CERO O NEGATIVO:
   ¿LA BASE ES NO NULA?

4. SI EL EXPONENTE ES RACIONAL:
   ¿ESTÁ ESCRITO EN TÉRMINOS MÍNIMOS?
   ¿LA BASE ES POSITIVA, CERO O NEGATIVA?

5. SI HAY UN RADICAL:
   ¿EL ÍNDICE ES PAR O IMPAR?
   ¿SE TRATA DE UNA RAÍZ PRINCIPAL?

6. SI SALE UNA POTENCIA DE UNA RAÍZ PAR:
   ¿DEBE APARECER UN VALOR ABSOLUTO?

7. ¿QUÉ LEY SE ESTÁ USANDO Y CUÁLES SON SUS HIPÓTESIS?

8. ¿CONVIENE MÁS LA NOTACIÓN RADICAL O LA EXPONENCIAL?

9. SI SE RACIONALIZA:
   ¿QUÉ OBJETIVO CUMPLE EL CAMBIO DE FORMA?

10. ¿LA FORMA FINAL CONSERVA EXPLÍCITAMENTE EL DOMINIO ORIGINAL?
```

### Red conceptual del capítulo

Las ideas principales no forman una lista aislada. Se encadenan:

```text
POTENCIA ENTERA POSITIVA
        ↓
LEYES DERIVADAS
        ↓
EXTENSIÓN A 0 Y ENTEROS NEGATIVOS
        ↓
INVERSOS / NO NULIDAD
        ↓
RAÍZ n-ÉSIMA
        ↓
PARIDAD / RAÍZ PRINCIPAL
        ↓
√(a²)=|a|
        ↓
EXPONENTE RACIONAL
        ↓
DOMINIO DE LA BASE
        ↓
RADICAL ↔ POTENCIA RACIONAL
        ↓
SIMPLIFICACIÓN / PRODUCTO / COCIENTE
        ↓
RADICALES SEMEJANTES
        ↓
RACIONALIZACIÓN
        ↓
ELECCIÓN ESTRATÉGICA DE FORMA
        ↓
DIAGNÓSTICO DEL PRIMER PASO INVÁLIDO
```

### Qué debe poder hacer ahora el lector

Al terminar este capítulo, el lector debe ser capaz de:

- explicar de dónde provienen las leyes de exponentes, en lugar de recitarlas como un catálogo;
- distinguir exponentes positivos, cero, negativos y racionales por su definición;
- declarar las restricciones de no nulidad necesarias;
- distinguir raíz principal de conjunto de soluciones;
- usar la paridad del índice para determinar el dominio real de un radical;
- justificar por qué $\sqrt{a^2}=|a|$;
- convertir entre radicales y exponentes racionales;
- tratar con cuidado bases cero y negativas;
- simplificar y combinar radicales sin perder signos ni dominios;
- racionalizar cuando la transformación tiene un propósito;
- elegir entre representaciones equivalentes según la tarea;
- intersectar varias restricciones de dominio;
- encontrar el primer paso inválido de una cadena y repararlo.

### Hacia el capítulo 19

En C18 hemos aprendido a reconocer potencias perfectas y a cambiar de forma sin perder información. El paso siguiente será ampliar esa capacidad a expresiones polinómicas completas.

Allí aparecerá una nueva pregunta:

> **¿Cómo reconocer que una expresión aparentemente complicada es en realidad la expansión —o la factorización— de una estructura más simple?**

Ese será el problema de **identidades, productos notables y factorización**.

***
# Ejercicios

El banco está organizado por **función cognitiva**, no sólo por dificultad. Los ejercicios A–B construyen lectura y fluidez; C–D exigen justificación y diagnóstico; E–F obligan a elegir estrategias y transferir ideas; G reúne problemas largos de síntesis. Salvo indicación expresa, se trabaja en $\mathbb R$ y toda simplificación debe conservar el dominio de la expresión original.


## A. Reconocimiento y lectura estructural (1–10)


**1.** **Nivel A.** Para cada expresión, determina su dominio real y explica en una frase qué restricción lo produce:

   $a^{-3}$, $\sqrt[4]{a}$, $\sqrt[3]{a}$, $\dfrac1{\sqrt a}$ y $\sqrt[5]{a^{-2}}$.


**2.** **Nivel A.** Sea $n\ge1$ un entero. Sin desarrollar potencias, decide cuáles de las siguientes expresiones son iguales para todo real $x$ y cuáles dependen de la paridad del exponente:

   $(-x)^4$, $-x^4$, $(-x)^5$, $-x^5$, $(-x)^{2n}$ y $(-x)^{2n+1}$.


**3.** **Nivel A.** Distingue entre raíz principal y conjunto de soluciones. Indica cuáles afirmaciones son correctas:

   (a) $\sqrt{49}=7$;  
   (b) $\sqrt{49}=\pm7$;  
   (c) la ecuación $t^2=49$ tiene dos soluciones reales;  
   (d) $\sqrt[3]{-27}=-3$;  
   (e) la raíz cuarta principal de $16$ es $2$.


**4.** **Nivel A.** Reduce primero cada exponente racional y decide si la potencia tiene valor real:

   $(-16)^{2/4}$, $(-8)^{2/6}$, $(-32)^{6/15}$, $(-27)^{-4/6}$ y $(-1)^{15/21}$.

   No calcules todavía los valores salvo cuando sea necesario para justificar la decisión.


**5.** **Nivel A.** Para cada ley, escribe las condiciones de la formulación indicada para que el enunciado sea correcto en el contexto real de este capítulo. En (b), toma $m,n\in\mathbb Z$ y formula una condición uniforme sobre la base; en (e), usa la teoría sistemática sobre bases positivas, sin afirmar que esa condición sea mínima para cada exponente particular:

   (a) $a^{-n}=1/a^n$;  
   (b) $a^m/a^n=a^{m-n}$;  
   (c) $\sqrt{ab}=\sqrt a\sqrt b$;  
   (d) $\sqrt{a/b}=\sqrt a/\sqrt b$;  
   (e) $a^{m/n}=\sqrt[n]{a^m}$ cuando se usa sistemáticamente la teoría de exponentes racionales.


**6.** **Nivel A.** Determina el dominio real de cada expresión, sin simplificarla:

   (a) $\sqrt{x-3}$;  
   (b) $\dfrac1{\sqrt{x+1}}$;  
   (c) $(x-2)^{-4}$;  
   (d) $\sqrt[4]{(x+5)(x-1)}$;  
   (e) $\dfrac{\sqrt{x+2}}{x-7}$.


**7.** **Nivel A.** Empareja cada expresión con una representación equivalente bajo las hipótesis indicadas:

   $a^{3/2}$, $a^{2/3}$, $a^{-1/4}$, $\sqrt[5]{a^7}$,

   con

   $\dfrac1{\sqrt[4]{a}}$, $a\sqrt a$, $(\sqrt[3]{a})^2$, $a\sqrt[5]{a^2}$.

   Declara las condiciones sobre $a$ que estás usando.


**8.** **Nivel A.** Clasifica cada transformación como `válida`, `válida con hipótesis adicionales` o `falsa en general`:

   (a) $\sqrt{x^2}=x$;  
   (b) $\sqrt{x^2}=|x|$;  
   (c) $\sqrt{x+4}=\sqrt x+2$;  
   (d) $x^{-3}=1/x^3$;  
   (e) $\sqrt{12x^2}=2|x|\sqrt3$.


**9.** **Nivel A.** Sea $a>0$. Determina el signo de $(-a)^n$ según $n$ sea par o impar, y después compara esa información con el signo de $-a^n$. Explica por qué los paréntesis cambian el objeto que se eleva a potencia.


**10.** **Nivel A.** Para cada tarea, indica qué representación parece más informativa antes de efectuar cálculos: radical o exponente racional.

   (a) multiplicar $\sqrt[3]{a^2}\sqrt[3]{a}$;  
   (b) reconocer términos semejantes en $3\sqrt{12}+2\sqrt{27}$;  
   (c) elevar $(a^{2/5})^{15}$ con $a>0$;  
   (d) estudiar el signo de $\sqrt{x^2}$;  
   (e) comparar $a^{3/4}a^{5/4}$ con una potencia entera.


## B. Fluidez técnica (11–26)


**11.** **Nivel B.** Simplifica y escribe el resultado con exponentes positivos:

   $$\frac{x^{-3}y^5}{x^2y^{-4}},\qquad x,y\neq0.$$


**12.** **Nivel B.** Simplifica completamente:

   $$\frac{(a^{-2}b^3)^3(a^4b^{-1})^2}{a^{-1}b^5},\qquad a,b\neq0.$$


**13.** **Nivel B.** Simplifica:

   $$\left(\frac{3x^{-2}y^3}{2x^4y^{-1}}\right)^{-2},\qquad x,y\neq0.$$


**14.** **Nivel B.** Evalúa exactamente:

   $$2^{-4},\qquad 16^{-3/4},\qquad 27^{2/3},\qquad 81^{-1/2},\qquad 32^{3/5}.$$


**15.** **Nivel B.** Simplifica los radicales numéricos:

   $$\sqrt{288},\qquad \sqrt[3]{432},\qquad \sqrt[4]{1296\cdot5},\qquad \sqrt[5]{96}.$$


**16.** **Nivel B.** Simplifica para variables reales:

   $$\sqrt{72x^6y^4}.$$

   La respuesta debe ser válida sin suponer signos positivos para $x$ e $y$.


**17.** **Nivel B.** Simplifica para todo real $t$:

   $$\sqrt[3]{54t^7},\qquad \sqrt[4]{48t^8},\qquad \sqrt{200t^{10}}.$$


**18.** **Nivel B.** Simplifica usando las leyes de producto y cociente con sus condiciones:

   $$\sqrt{18}\sqrt{8},\qquad
   \frac{\sqrt{75}}{\sqrt3},\qquad
   \sqrt[3]{12}\sqrt[3]{18},\qquad
   \frac{\sqrt[3]{250}}{\sqrt[3]{2}}.$$


**19.** **Nivel B.** Reduce y combina términos semejantes:

   $$5\sqrt{12}-3\sqrt{27}+2\sqrt{75}-\sqrt{48}.$$


**20.** **Nivel B.** Simplifica:

   $$2\sqrt{18x^2}+3\sqrt{8x^2}-\sqrt{50x^2}$$

   para $x\in\mathbb R$.


**21.** **Nivel B.** Racionaliza el denominador y simplifica:

   $$\frac{7}{3\sqrt5},\qquad
   \frac{2\sqrt3}{\sqrt7},\qquad
   \frac{5}{\sqrt[3]{4}}.$$


**22.** **Nivel B.** Racionaliza usando conjugados:

   $$\frac{1}{3+\sqrt5},\qquad
   \frac{2}{\sqrt7-\sqrt3},\qquad
   \frac{\sqrt2}{2-\sqrt2}.$$


**23.** **Nivel B.** Convierte a exponentes racionales y simplifica, suponiendo $a,b>0$:

   $$\sqrt[3]{a^2}\sqrt[6]{a^5},\qquad
   \frac{\sqrt[4]{b^7}}{\sqrt b}.$$


**24.** **Nivel B.** Evalúa en $\mathbb R$:

   $$(-27)^{2/3},\qquad
   (-32)^{3/5},\qquad
   (-8)^{-2/3},\qquad
   (-243)^{1/5}.$$


**25.** **Nivel B.** Determina el dominio real y luego simplifica sin ampliarlo:

   $$\frac{\sqrt{(x-2)^2}}{x-2}.$$


**26.** **Nivel B.** Para $a,b>0$, simplifica por completo:

   $$\frac{a^{7/6}b^{-5/4}\sqrt[3]{a^2b^3}}
           {a^{-1/2}b^{1/4}\sqrt a}.$$

   Da la respuesta final con exponentes positivos.


## C. Justificación y reconstrucción (27–38)


**27.** **Nivel C.** Justifica, a partir de la ley del cociente para potencias positivas, por qué la definición coherente de $a^0$ debe ser $1$ cuando $a\neq0$. Señala exactamente dónde se usa la hipótesis de no nulidad.


**28.** **Nivel C.** Deriva la definición

   $$a^{-n}=\frac1{a^n}$$

   para $a\neq0$ y $n>0$, suponiendo que se desea conservar $a^ma^n=a^{m+n}$.


**29.** **Nivel C.** Demuestra la ley

   $$a^m a^n=a^{m+n}$$

   para exponentes enteros $m,n$ y base $a\neq0$. Organiza la prueba por casos según los signos de $m$ y $n$.


**30.** **Nivel C.** Demuestra que para todo $x\in\mathbb R$,

   $$\sqrt{x^2}=|x|.$$

   La prueba debe usar la definición de raíz cuadrada principal, no una regla memorizada.


**31.** **Nivel C.** Sea $n\ge2$. Justifica

   $$\sqrt[n]{x^n}=
   \begin{cases}
   |x|,&n\text{ par},\\
   x,&n\text{ impar},
   \end{cases}$$

   para todo real $x$ para el cual la expresión tenga sentido.


**32.** **Nivel C.** Demuestra que si $a,b\ge0$, entonces

   $$\sqrt{ab}=\sqrt a\sqrt b.$$

   Tu argumento debe verificar dos cosas: no negatividad y cuadrado correcto.


**33.** **Nivel C.** Da un contraejemplo numérico que destruya cada afirmación:

   (a) $\sqrt{u+v}=\sqrt u+\sqrt v$;  
   (b) $(u+v)^2=u^2+v^2$;  
   (c) $\sqrt{u^2}=u$ para todo real $u$.

   Después explica por qué un solo contraejemplo basta lógicamente.


**34.** **Nivel C.** Sea $a>0$ y $m/n=p/q$ dos fracciones reducidas o no reducidas con denominadores positivos. Explica por qué una definición correcta de $a^r$ no puede depender de la forma fraccionaria elegida para representar el mismo racional. Señala qué propiedad de las raíces hace plausible esa independencia.


**35.** **Nivel C.** Para $a>0$, justifica que

   $$a^{m/n}=\sqrt[n]{a^m}=(\sqrt[n]{a})^m.$$

   No te limites a citar la definición: verifica que ambas expresiones representan la misma raíz positiva apropiada.


**36.** **Nivel C.** Para $a>0$ y $r,s\in\mathbb Q$, explica por qué la ley

   $$(a^r)^s=a^{rs}$$

   es estable en este dominio. Contrasta tu argumento con lo que puede fallar cuando la base es negativa.


**37.** **Nivel C.** Sea $u,v\in\mathbb R$ y supón que $u+\sqrt v$ y $u-\sqrt v$ están definidos y son no nulos. Justifica algebraicamente por qué multiplicar por

   $$\frac{u-\sqrt v}{u-\sqrt v}$$

   conserva el valor de una fracción y explica qué falla si el conjugado fuese cero.


**38.** **Nivel C.** Considera una expresión $E(x)$ y una forma simplificada $S(x)$ obtenida mediante transformaciones válidas en el dominio $D$ de $E$. Explica por qué no se sigue que $E$ y $S$ tengan el mismo dominio como expresiones aisladas. Ilustra tu explicación con

   $$E(x)=\frac{x^2}{x},\qquad S(x)=x.$$


## D. Diagnóstico del primer paso inválido (39–50)


**39.** **Nivel D.** Un estudiante escribe

   $$\sqrt{(x-7)^2}=x-7.$$

   Localiza el primer paso conceptual incorrecto, nombra la regla correcta y repara la expresión para todo real $x$.


**40.** **Nivel D.** Diagnostica:

   $$\sqrt{x+16}=\sqrt x+4.$$

   Encuentra el primer paso no justificado, ofrece un contraejemplo y formula una versión verdadera relacionada con producto o cociente de radicales.


**41.** **Nivel D.** Un estudiante afirma:

   $$(a+b)^3=a^3+b^3.$$

   Explica por qué ninguna ley de exponentes autoriza esta distribución sobre una suma. Usa C13 para mostrar qué términos faltan.


**42.** **Nivel D.** Analiza la cadena

   $$\frac{x^5}{x^5}=x^0=1.$$

   ¿Es incorrecta? ¿Para qué valores es válida? Explica por qué no permite concluir que $0^0=1$ en este capítulo.


**43.** **Nivel D.** Diagnostica la afirmación

   $$(-3)^{-2}=-\frac19.$$

   Identifica qué se ha confundido entre signo de la base y signo del exponente.


**44.** **Nivel D.** Un estudiante simplifica

   $$\frac{x^4}{x}=x^3$$

   y luego dice que ambas expresiones son iguales para todo $x\in\mathbb R$. Separa el cálculo correcto del error de dominio y formula la igualdad con su restricción exacta.


**45.** **Nivel D.** Repara la cadena

   $$(-64)^{2/6}
   =\sqrt[6]{(-64)^2}
   =\sqrt[6]{4096}
   =4.$$

   Debes localizar el primer paso incompatible con la política de exponentes racionales para bases negativas.


**46.** **Nivel D.** Analiza

   $$\left((-27)^{2/3}\right)^{3/2}
   =(-27)^1
   =-27.$$

   Calcula el lado izquierdo por una ruta válida, identifica la ley aplicada fuera de su dominio rector y explica la discrepancia.


**47.** **Nivel D.** Diagnostica:

   $$\sqrt{(-3)(-12)}
   =\sqrt{-3}\sqrt{-12}
   =6.$$

   ¿En qué paso sale la cadena de $\mathbb R$? ¿Cuál es el valor correcto del lado izquierdo?


**48.** **Nivel D.** Un estudiante escribe

   $$\sqrt{x^4y^2}=x^2y.$$

   Determina qué parte es siempre correcta y qué parte depende del signo de $y$. Da la forma válida para todo $x,y\in\mathbb R$.


**49.** **Nivel D.** Al racionalizar

   $$\frac1{1+\sqrt1},$$

   alguien multiplica por $(1-\sqrt1)/(1-\sqrt1)$. Explica por qué ese procedimiento es inválido aunque “use el conjugado”, y simplifica la expresión original por una ruta legítima.


**50.** **Nivel D.** Localiza el primer paso inválido y repara desde allí:

   $$\frac{\sqrt{(x-1)^2}}{x-1}
   =\frac{x-1}{x-1}
   =1
   \qquad(x\neq1).$$

   Describe además el comportamiento correcto de la expresión según el signo de $x-1$, sin resolver ninguna ecuación.


## E. Estrategia y elección de representación (51–60)


**51.** **Nivel E.** Supón $a>0$. Para simplificar

   $$\sqrt[3]{a^5}\,\sqrt[6]{a},$$

   compara dos estrategias: mantener radicales o pasar a exponentes racionales. Ejecuta ambas y explica cuál revela más rápido la estructura.


**52.** **Nivel E.** Antes de calcular

   $$4\sqrt{18}-3\sqrt8+\sqrt{50},$$

   decide qué operación debe realizarse primero para saber si existen términos semejantes. Justifica por qué sumar coeficientes de inmediato sería una mala estrategia.


**53.** **Nivel E.** Considera

   $$\frac1{\sqrt5+2}.$$

   Produce una forma racionalizada y la forma original. Explica en qué tipo de tarea podría ser más útil cada una y por qué ninguna es universalmente “la forma correcta”.


**54.** **Nivel E.** Para estudiar

   $$\frac{\sqrt{x-1}}{x^{-2}\sqrt{x+3}},$$

   diseña un orden de trabajo que minimice errores: dominio, tratamiento del exponente negativo, combinación de factores y forma final. No empieces por simplificar.


**55.** **Nivel E.** Construye un contraejemplo pequeño para refutar

   $$\sqrt{u^2+v^2}=|u|+|v|.$$

   Después explica cómo elegiste los valores para que el cálculo fuese inmediato.


**56.** **Nivel E.** Para $a>0$, simplifica

   $$\frac{\sqrt[4]{a^3}}{\sqrt[6]{a}}$$

   por dos rutas: usando exponentes racionales y usando un índice común de radicales. Compara la longitud y transparencia de ambas rutas.


**57.** **Nivel E.** Decide la mejor representación para simplificar

   $$\frac{(x^{3/4})^2\sqrt x}{x^{1/2}},\qquad x>0.$$

   Explica por qué mezclar notaciones sin un plan puede ocultar cancelaciones.


**58.** **Nivel E.** La expresión

   $$\sqrt{72(x-1)^6}$$

   puede simplificarse de varias maneras. Elige una ruta que mantenga visible el problema de signo y explica en qué momento debe aparecer un valor absoluto.


**59.** **Nivel E.** Racionaliza

   $$\frac{3}{\sqrt7-2}$$

   y luego decide cuál de las dos formas —original o racionalizada— usarías para:  
   (a) estimar numéricamente el valor;  
   (b) sumar la expresión con $\dfrac{3}{\sqrt7+2}$;  
   (c) estudiar sólo su dominio.


**60.** **Nivel E.** Considera

   $$\frac{\sqrt{50x^4}}{x\sqrt2}.$$

   Diseña la ruta de simplificación más segura para $x\neq0$, de modo que el resultado no pierda información de signo. Explica por qué cancelar “un $x$” antes de tratar $\sqrt{x^4}$ puede inducir razonamientos poco claros.


## F. Transferencia acumulativa (61–72)


**61.** **Nivel F.** Determina el dominio real de

   $$\frac{x^{-1/2}}{\sqrt{x-1}}$$

   interpretando $x^{-1/2}$ mediante exponentes racionales. Después reescribe la expresión usando sólo radicales, sin ampliar el dominio.


**62.** **Nivel F.** Simplifica preservando exactamente el dominio original:

   $$\frac{(x-3)^{-2}\sqrt{(x-3)^4}}{x+1}.$$

   Indica por separado la forma simplificada y las restricciones heredadas.


**63.** **Nivel F.** Usa el teorema del binomio de C13 para expandir $(u+v)^2$ y explica por qué esa expansión confirma que

   $$\sqrt{u^2+2uv+v^2}=|u+v|,$$

   pero no autoriza la identidad $\sqrt{u^2+v^2}=|u|+|v|$.


**64.** **Nivel F.** Simplifica, conservando el dominio original,

   $$\sqrt{\frac{(a-b)^4}{(a+b)^2}}$$

   bajo la condición $a+b\neq0$. La respuesta debe tratar correctamente el valor absoluto.


**65.** **Nivel F.** Determina el dominio y simplifica:

   $$\frac{x^{3/2}}{x^{-1/2}\sqrt{x+2}}.$$

   Trabaja en el dominio real sistemático para exponentes racionales y explica qué restricciones desaparecen visualmente en la forma final.


**66.** **Nivel F.** Sean

   $$E(x)=\frac{\sqrt{x^2}}{x},
   \qquad
   F(x)=\frac{|x|}{x},
   \qquad
   G(x)=1.$$

   Compara sus dominios y determina qué pares representan la misma función en su dominio común. Explica por qué la igualdad simbólica no puede separarse del dominio.


**67.** **Nivel F.** Simplifica

   $$\sqrt{(t-3)^2}\,\sqrt{(t+3)^2}$$

   para todo real $t$. Da una forma con valores absolutos y explica por qué sustituirla por $(t-3)(t+3)$ exigiría información adicional de signo.


**68.** **Nivel F.** Racionaliza y conserva las restricciones:

   $$\frac{\sqrt{x+1}}{\sqrt{x+4}-\sqrt{x+1}}.$$

   Determina primero el dominio de la expresión original y verifica que el factor conjugado usado no se anula allí.


**69.** **Nivel F.** Determina el dominio de

   $$\sqrt{1-\sqrt{x}}$$

   razonando de afuera hacia adentro y de adentro hacia afuera. Compara ambos recorridos y explica por qué este ejercicio no requiere una teoría especial de radicales anidados.


**70.** **Nivel F.** Para $c>0$, clasifica cuándo

   $$(-c)^{p/q}$$

   es real si $p/q$ está reducido y $q>0$. Indica además el signo del resultado según la paridad de $p$ cuando $q$ es impar.


**71.** **Nivel F.** Simplifica para $x>0$:

   $$\frac{\sqrt[3]{x^4}\,x^{-5/6}}
           {\sqrt[6]{x^{-1}}}.$$

   Resuelve primero con exponentes racionales y después traduce el resultado final a notación radical.


**72.** **Nivel F.** Considera

   $$\frac{\sqrt{18x^6}}{x^2}\cdot
   \frac{x^{-1}}{\sqrt2},
   \qquad x\neq0.$$

   Simplifica sin perder información de signo y explica qué parte del razonamiento depende de $\sqrt{x^2}=|x|$.


## G. Síntesis avanzada (73–80)


**73.** **Nivel G.** Sea

   $$E(x)=
   \frac{x^{-3/2}\sqrt{x^5}}
        {\sqrt{x}\,(\sqrt{x+1}-1)}.$$

   (a) Determina primero el dominio real.  
   (b) Simplifica por una ruta basada en exponentes racionales.  
   (c) Simplifica por una ruta que mantenga radicales el mayor tiempo posible.  
   (d) Racionaliza sólo si mejora la forma para una tarea explícita.  
   (e) Compara ambas rutas y explica en qué pasos el dominio original debe mantenerse aunque ya no sea visible.


**74.** **Nivel G.** Sea $n\ge2$ par y $a,b\in\mathbb R$. Analiza

   $$\sqrt[n]{a^{2n}b^n}.$$

   Produce una fórmula válida para todos los valores para los que la expresión está definida. Justifica cuidadosamente qué factores salen con valor absoluto, qué ocurre con el signo de $b$ y cómo cambia la respuesta si el índice $n$ se reemplaza por un índice impar.


**75.** **Nivel G.** Para $a>0$, simplifica

   $$P(a)=
   \frac{\sqrt[3]{a^5}\sqrt[4]{a^3}}
        {a^{7/12}}$$

   de dos maneras completas:  
   (i) sólo mediante exponentes racionales;  
   (ii) convirtiendo primero a un radical de índice común.  
   Compara las dos soluciones según longitud, transparencia y facilidad para verificar el dominio.


**76.** **Nivel G.** Un estudiante propone la siguiente cadena:

   $$(-64)^{4/6}
   =\left((-64)^{1/6}\right)^4
   =\left(\sqrt[6]{-64}\right)^4
   =(-2)^4
   =16
   =\left((-64)^{2/3}\right)
   =\left(\sqrt[3]{(-64)^2}\right)
   =16.$$

   Analiza la cadena línea por línea. Localiza el **primer** paso inválido, explica por qué los pasos posteriores no reparan el razonamiento aunque el resultado final coincida con el valor correcto, y reconstruye una cadena válida desde la fracción reducida.


**77.** **Nivel G.** Racionaliza completamente

   $$\frac1{\sqrt2+\sqrt3+\sqrt5}.$$

   Agrupa primero $\sqrt2+\sqrt3$ como una unidad y usa un conjugado para reducir el denominador a un solo radical; después completa la racionalización. Verifica cada multiplicador y explica por qué ninguno de los denominadores introducidos es cero.


**78.** **Nivel G.** Estudia las tres expresiones

   $$E(x)=\frac{\sqrt{x^2}}x,\qquad
   F(x)=\frac{x}{\sqrt{x^2}},\qquad
   G(x)=\frac{x^2}{|x|^2}.$$

   (a) Determina sus dominios originales.  
   (b) Simplifica cada una sin ampliar el dominio.  
   (c) Decide cuáles son iguales como funciones.  
   (d) Explica por qué obtener la forma final $1$ en algún caso no autoriza a insertar $x=0$.  
   (e) Formula la lección general sobre dominio como invariante de una cadena de transformaciones.


**79.** **Nivel G.** Fija $c>0$ y estudia la familia

   $$(-c)^r,\qquad r\in\mathbb Q.$$

   Escribe $r=p/q$ en términos mínimos con $q>0$ y:

   (a) clasifica exactamente cuándo la potencia es real;  
   (b) determina su signo cuando existe;  
   (c) compara $(-c)^{2/3}$, $((-c)^{2/3})^{3/2}$ y $(-c)^{(2/3)(3/2)}$;  
   (d) explica por qué la ley $(a^r)^s=a^{rs}$ se adopta sistemáticamente sobre bases positivas y no se transporta sin control a toda base negativa.


**80.** **Nivel G.** Realiza una auditoría MA-PED completa de

   $$Q(x)=
   \frac{\sqrt{72x^6}\,x^{-1/2}}
        {\sqrt{x+2}\,(\sqrt{x+5}-\sqrt{x+2})}.$$

   Tu solución deberá contener, en este orden:

   1. lectura estructural de la expresión;  
   2. dominio real original;  
   3. elección y justificación de una representación;  
   4. simplificación de potencias y radicales;  
   5. tratamiento explícito de cualquier valor absoluto;  
   6. racionalización sólo si cumple un objetivo;  
   7. forma final con dominio conservado;  
   8. verificación de que ninguna transformación introdujo una ampliación silenciosa del dominio.

   No resuelvas ecuaciones asociadas: el problema es exclusivamente de **expresiones, dominio y transformaciones justificadas**.

***
## H. Convenciones, leyes y construcción de dominios (81–96)


**81.** **Nivel D.** Sea $a<0$. Compara $a^{5/3}$, $a^{10/6}$, $\sqrt[3]{a^5}$, $\sqrt[6]{a^{10}}$ y $(\sqrt[6]a)^{10}$. Determina cuáles existen en los reales, cuáles representan el mismo valor y qué información pierde una receta que dé un valor distinto.


**82.** **Nivel C.** Sea $a<0$ y $m/n\ne0$ una fracción reducida con $n>0$ impar. Clasifica el valor de $(a^{m/n})^{n/m}$ según la paridad de $m$, incluyendo $m<0$. Compara con $a^{(m/n)(n/m)}$.


**83.** **Nivel C.** Sea $A$ el conjunto de racionales cuya fracción reducida tiene denominador impar. Demuestra que una fracción con denominador impar siempre representa un elemento de $A$ y que todo elemento de $A$ admite también una escritura con denominador par. Determina si $A$ se conserva al sumar, multiplicar y tomar recíprocos de elementos no nulos. Relaciona las conclusiones con una base negativa fija.


**84.** **Nivel C.** Sea $a<0$ y sean $r=p/q$, $s=u/v$ fracciones reducidas con $q,v>0$ impares. Decide si $a^r a^s=a^{r+s}$ sigue siendo válida. Justifica la independencia de la escritura elegida para $r+s$, incluyendo $r+s=0$ y exponentes negativos.


**85.** **Nivel F.** Compara los dominios de $(ab)^{2/3}$ y $a^{2/3}b^{2/3}$ para $a,b\in\mathbb R$, y decide si son iguales donde existen. Contrasta con los dominios de $\sqrt{ab}$ y $\sqrt a\sqrt b$. Da un caso que distinga ambos tipos de ley.


**86.** **Nivel C.** Determina exactamente para qué $a,b\in\mathbb R$ la igualdad $\sqrt{a+b}=\sqrt a+\sqrt b$ es una igualdad de números reales. Demuestra ambas direcciones y explica por qué refutar una identidad universal no excluye todos los casos particulares.


**87.** **Nivel D.** Sea $n\ge3$ impar. Compara los dominios y valores de $\sqrt[n]a$ y $\sqrt[2n]{a^2}$. Decide cuándo se puede aumentar el índice multiplicándolo por dos a la vez que se eleva el radicando al cuadrado. Formula una reparación que valga para todo real $a$.


**88.** **Nivel F.** Compara los dominios naturales de $\sqrt{a/b}$ y $\sqrt a/\sqrt b$. Describe todos los casos en los que sólo existe la primera y expresa su valor mediante raíces de números no negativos en esos casos.


**89.** **Nivel E.** Determina el dominio y simplifica $R(t)=(\sqrt[4]t-\sqrt[6]t)/(\sqrt[12]t-1)$. Elige una representación que haga visible una cancelación y explica si la forma final puede usarse en $t=1$.


**90.** **Nivel E.** Para $t\ge0$, estudia $L(t)=\sqrt{t+9}-\sqrt{t+4}$. Obtén una forma que permita demostrar $0<L(t)\le1$ sin aproximaciones decimales y determina cuándo se alcanza la cota superior. Explica qué aporta la representación elegida.


**91.** **Nivel F.** Sea $P(x,y)=\sqrt[3]{x^2}\sqrt[3]{y^4}$ para reales $x,y$. Busca una representación que permita decidir cómo cambia $P$ al reemplazar $(x,y)$ por $(\lambda x,\lambda y)$, con $\lambda$ real. Demuestra la fórmula obtenida, incluyendo signos y ceros.


**92.** **Nivel E.** Para $x>0$, sea $P(x)=\sqrt[4]{x^3}\sqrt[6]{x^5}$. Determina el menor entero positivo $N$ para el que existe un entero $M$ con $P(x)^N=x^M$ para todo $x>0$. Determina también todos los pares $(N,M)$ posibles.


**93.** **Nivel F.** Sean $a<b$ y $a<c<b$. Construye una expresión real usando raíces y un cociente cuyo dominio natural sea exactamente $[a,b]\setminus\{c\}$. Justifica que no faltan puntos ni se admiten otros; compara una forma con dos raíces y una con una sola.


**94.** **Nivel F.** Sea $F=\{c_1,\ldots,c_k\}$ un conjunto finito de reales distintos. Construye una expresión cuyo dominio natural sea $\mathbb R\setminus F$ y cuyo valor sea uno en todo su dominio. Incluye el caso $F=\varnothing$ y explica por qué simplificarla no restituye los puntos excluidos.


**95.** **Nivel F.** Sean $a<b$ y $F\subset(a,b)$ finito. Construye una expresión de raíces y cocientes con dominio natural exactamente $(a,b]\setminus F$. Haz que su valor se simplifique a $\sqrt{b-x}/\sqrt{x-a}$ dentro de ese dominio. Explica la diferencia entre los dos extremos.


**96.** **Nivel F.** Sean $a<b$. Construye una expresión cuyo dominio natural sea $(-\infty,a)\cup(b,\infty)$. Decide si separar una raíz de producto en dos raíces conserva ese dominio. Da fórmulas válidas para el valor en cada una de las dos regiones.

***
## Cierre del banco

Los ejercicios 73–80 constituyen el bloque avanzado. Ninguno requiere teoría posterior a C18: incluso cuando aparecen expresiones largas, conjugados sucesivos, parámetros o radicales anidados, la dificultad procede de **coordinar dominio, representación, leyes de exponentes, raíz principal, valor absoluto y diagnóstico**, no de introducir una teoría nueva.

Las soluciones razonadas forman parte de este capítulo bajo `FULL_SOLUTION_PROTOCOL`.

***
# Soluciones razonadas

Las soluciones siguen `FULL_SOLUTION_PROTOCOL`: no se limitan a registrar un resultado, sino que hacen visible la lectura del dominio, la regla utilizada, la estrategia y el cierre cuando esas capas son matemáticamente relevantes. En los ejercicios de diagnóstico se identifica el **primer** paso inválido antes de reconstruir la cadena.

## A. Reconocimiento y lectura estructural


### 1

El dominio se obtiene leyendo cada operación antes de simplificar.

- $a^{-3}$ exige $a\neq0$, porque $a^{-3}=1/a^3$.
- $\sqrt[4]{a}$ exige $a\ge0$.
- $\sqrt[3]{a}$ está definida para todo $a\in\mathbb R$.
- $\dfrac1{\sqrt a}$ exige $\sqrt a$ real y no nula; por tanto $a>0$.
- $\sqrt[5]{a^{-2}}$ exige primero $a^{-2}$, de modo que $a\neq0$. La raíz quinta no añade restricciones.

Así, los dominios son, respectivamente,
$$
\mathbb R\setminus\{0\},\qquad
[0,\infty),\qquad
\mathbb R,\qquad
(0,\infty),\qquad
\mathbb R\setminus\{0\}.
$$


### 2

Los paréntesis determinan cuál es la base.

Para todo real $x$,
$$
(-x)^4=x^4
$$
porque aparecen cuatro factores negativos. En cambio,
$$
-x^4=-(x^4),
$$
que sólo coincide con $x^4$ cuando $x=0$.

También
$$
(-x)^5=-x^5.
$$

Para el entero $n\ge1$ del enunciado,
$$
(-x)^{2n}=x^{2n},
\qquad
(-x)^{2n+1}=-x^{2n+1}.
$$

La paridad del exponente controla el signo de una base negativa.


### 3

(a) Es correcta:
$$
\sqrt{49}=7,
$$
porque el símbolo $\sqrt{\phantom{x}}$ designa la raíz cuadrada principal, que es no negativa.

(b) Es falsa:
$$
\sqrt{49}\neq\pm7.
$$
El símbolo radical nombra un solo número.

(c) Es correcta: la ecuación
$$
t^2=49
$$
tiene dos soluciones,
$$
t=7,\qquad t=-7.
$$

(d) Es correcta:
$$
\sqrt[3]{-27}=-3.
$$

(e) La formulación correcta es que la **raíz cuarta principal** de $16$ es $2$:
$$
\sqrt[4]{16}=2.
$$
La ecuación $t^4=16$ tiene dos soluciones reales, $t=\pm2$.


### 4

Primero reducimos cada exponente.

$$
\frac24=\frac12,
$$
de modo que
$$
(-16)^{2/4}=(-16)^{1/2},
$$
que no es real.

$$
\frac26=\frac13,
$$
por lo que $(-8)^{2/6}$ sí es real: el denominador reducido es impar.

$$
\frac6{15}=\frac25,
$$
así que $(-32)^{6/15}$ es real.

$$
-\frac46=-\frac23,
$$
de modo que $(-27)^{-4/6}$ es real; la base además es no nula.

Finalmente,
$$
\frac{15}{21}=\frac57,
$$
y $(-1)^{15/21}$ es real.

La clasificación es:
$$
\text{no real},\quad
\text{real},\quad
\text{real},\quad
\text{real},\quad
\text{real}.
$$


### 5

Las hipótesis forman parte de las leyes.

(a)
$$
a^{-n}=\frac1{a^n}
$$
requiere $a\neq0$ y $n>0$ entero.

(b) En la formulación uniforme para exponentes enteros,
$$
\frac{a^m}{a^n}=a^{m-n}
$$
requiere $a\neq0$.

(c)
$$
\sqrt{ab}=\sqrt a\sqrt b
$$
se usa en $\mathbb R$ bajo
$$
a\ge0,\qquad b\ge0.
$$

(d)
$$
\sqrt{\frac ab}=\frac{\sqrt a}{\sqrt b}
$$
requiere
$$
a\ge0,\qquad b>0.
$$

(e) Para la teoría sistemática de exponentes racionales usamos
$$
a>0,
$$
con $m/n$ interpretado como racional y $n>0$. Esta elección mantiene estables las leyes sin ambigüedades de dominio.


### 6

Leemos cada restricción por separado.

(a)
$$
\sqrt{x-3}
$$
exige
$$
x-3\ge0,
$$
luego
$$
x\ge3.
$$

(b)
$$
\frac1{\sqrt{x+1}}
$$
exige además que la raíz del denominador no sea cero:
$$
x+1>0,
$$
luego
$$
x>-1.
$$

(c)
$$
(x-2)^{-4}
$$
exige
$$
x\neq2.
$$

(d)
$$
\sqrt[4]{(x+5)(x-1)}
$$
exige
$$
(x+5)(x-1)\ge0.
$$
El producto es no negativo fuera del intervalo entre sus ceros:
$$
x\le-5
\quad\text{o}\quad
x\ge1.
$$

(e)
$$
\frac{\sqrt{x+2}}{x-7}
$$
exige
$$
x\ge-2,
\qquad
x\neq7.
$$


### 7

Bajo la convención común $a>0$:

$$
a^{3/2}=a\sqrt a,
$$

$$
a^{2/3}=(\sqrt[3]a)^2,
$$

$$
a^{-1/4}=\frac1{\sqrt[4]a},
$$

y
$$
\sqrt[5]{a^7}
=
\sqrt[5]{a^5a^2}
=
a\sqrt[5]{a^2}.
$$

Las correspondencias son, por tanto,
$$
a^{3/2}\leftrightarrow a\sqrt a,
$$
$$
a^{2/3}\leftrightarrow(\sqrt[3]a)^2,
$$
$$
a^{-1/4}\leftrightarrow\frac1{\sqrt[4]a},
$$
$$
\sqrt[5]{a^7}\leftrightarrow a\sqrt[5]{a^2}.
$$

La última identidad, por tratarse de una raíz impar, se extiende de hecho a todo $a\in\mathbb R$.


### 8

(a)
$$
\sqrt{x^2}=x
$$
es falsa en general. Es válida bajo la hipótesis adicional $x\ge0$.

(b)
$$
\sqrt{x^2}=|x|
$$
es válida para todo real $x$.

(c)
$$
\sqrt{x+4}=\sqrt x+2
$$
es falsa en general. Por ejemplo, con $x=5$:
$$
3\neq\sqrt5+2.
$$

(d)
$$
x^{-3}=\frac1{x^3}
$$
es válida con la hipótesis
$$
x\neq0.
$$

(e)
$$
\sqrt{12x^2}
=
\sqrt{4\cdot3\cdot x^2}
=
2\sqrt3\,|x|
$$
es válida para todo real $x$.


### 9

Sea $a>0$.

Si $n$ es par,
$$
(-a)^n=a^n>0.
$$

Si $n$ es impar,
$$
(-a)^n=-a^n<0.
$$

En cambio,
$$
-a^n
$$
significa primero calcular $a^n$ y después cambiar el signo; por tanto siempre es negativo.

La diferencia es estructural:
$$
(-a)^n
$$
eleva una **base negativa**, mientras que
$$
-a^n
$$
aplica un signo menos a una potencia cuya base es $a$.


### 10

(a) Para
$$
\sqrt[3]{a^2}\sqrt[3]a
$$
conviene mantener radicales de igual índice o pasar a exponentes; ambas formas revelan de inmediato
$$
a^{2/3}a^{1/3}=a.
$$

(b) En
$$
3\sqrt{12}+2\sqrt{27}
$$
conviene la notación radical, porque simplificar los radicandos revela términos semejantes.

(c) Para
$$
(a^{2/5})^{15}
$$
conviene la notación exponencial:
$$
a^{(2/5)15}=a^6.
$$

(d) Para estudiar
$$
\sqrt{x^2},
$$
la notación radical hace visible la raíz principal y conduce a
$$
|x|.
$$

(e) En
$$
a^{3/4}a^{5/4}
$$
la notación exponencial es claramente superior:
$$
a^{3/4+5/4}=a^2.
$$

## B. Fluidez técnica


### 11

Usamos la regla del cociente por base:
$$
\frac{x^{-3}y^5}{x^2y^{-4}}
=
x^{-3-2}y^{5-(-4)}
=
x^{-5}y^9.
$$
Con exponentes positivos:
$$
\boxed{\frac{y^9}{x^5}},
\qquad x,y\neq0.
$$


### 12

Primero elevamos cada factor:
$$
(a^{-2}b^3)^3=a^{-6}b^9,
$$
$$
(a^4b^{-1})^2=a^8b^{-2}.
$$
El numerador es
$$
a^2b^7.
$$
Dividiendo por $a^{-1}b^5$:
$$
a^{2-(-1)}b^{7-5}
=
a^3b^2.
$$
Por tanto,
$$
\boxed{a^3b^2},\qquad a,b\ne0.
$$


### 13

Dentro del paréntesis:
$$
\frac{3x^{-2}y^3}{2x^4y^{-1}}
=
\frac32x^{-6}y^4.
$$
Al elevar a $-2$:
$$
\left(\frac32x^{-6}y^4\right)^{-2}
=
\left(\frac23\right)^2x^{12}y^{-8}.
$$
Así,
$$
\boxed{\frac{4x^{12}}{9y^8}},
\qquad x,y\neq0.
$$


### 14

Calculamos uno a uno:
$$
2^{-4}=\frac1{16},
$$
$$
16^{-3/4}
=
\frac1{(\sqrt[4]{16})^3}
=
\frac18,
$$
$$
27^{2/3}
=
(\sqrt[3]{27})^2
=
9,
$$
$$
81^{-1/2}
=
\frac1{\sqrt{81}}
=
\frac19,
$$
$$
32^{3/5}
=
(\sqrt[5]{32})^3
=
2^3
=
8.
$$


### 15

Extraemos potencias perfectas compatibles con cada índice:
$$
\sqrt{288}
=
\sqrt{144\cdot2}
=
12\sqrt2,
$$
$$
\sqrt[3]{432}
=
\sqrt[3]{216\cdot2}
=
6\sqrt[3]2,
$$
$$
\sqrt[4]{1296\cdot5}
=
6\sqrt[4]5,
$$
porque $1296=6^4$, y
$$
\sqrt[5]{96}
=
\sqrt[5]{32\cdot3}
=
2\sqrt[5]3.
$$


### 16

Factorizamos:
$$
72x^6y^4
=
36\cdot2\cdot x^6y^4.
$$
Entonces
$$
\sqrt{72x^6y^4}
=
6\sqrt2\,\sqrt{x^6}\sqrt{y^4}.
$$
Como
$$
\sqrt{x^6}=|x^3|=|x|^3
$$
y
$$
\sqrt{y^4}=y^2,
$$
obtenemos
$$
\boxed{6|x|^3y^2\sqrt2}.
$$


### 17

Para la raíz cúbica:
$$
\sqrt[3]{54t^7}
=
\sqrt[3]{27t^6\cdot2t}
=
3t^2\sqrt[3]{2t}.
$$

Para la raíz cuarta:
$$
\sqrt[4]{48t^8}
=
\sqrt[4]{16(t^2)^4\cdot3}
=
2t^2\sqrt[4]3.
$$

Para la raíz cuadrada:
$$
\sqrt{200t^{10}}
=
\sqrt{100\cdot2\cdot(t^5)^2}
=
10|t|^5\sqrt2.
$$


### 18

Aplicamos las leyes correspondientes:
$$
\sqrt{18}\sqrt8
=
\sqrt{144}
=
12,
$$
$$
\frac{\sqrt{75}}{\sqrt3}
=
\sqrt{25}
=
5,
$$
$$
\sqrt[3]{12}\sqrt[3]{18}
=
\sqrt[3]{216}
=
6,
$$
y
$$
\frac{\sqrt[3]{250}}{\sqrt[3]2}
=
\sqrt[3]{125}
=
5.
$$


### 19

Simplificamos antes de sumar:
$$
5\sqrt{12}=10\sqrt3,
$$
$$
-3\sqrt{27}=-9\sqrt3,
$$
$$
2\sqrt{75}=10\sqrt3,
$$
$$
-\sqrt{48}=-4\sqrt3.
$$
Por tanto
$$
(10-9+10-4)\sqrt3
=
\boxed{7\sqrt3}.
$$


### 20

Para todo real $x$:
$$
\sqrt{18x^2}=3|x|\sqrt2,
$$
$$
\sqrt{8x^2}=2|x|\sqrt2,
$$
$$
\sqrt{50x^2}=5|x|\sqrt2.
$$
Así,
$$
2(3|x|\sqrt2)
+
3(2|x|\sqrt2)
-
5|x|\sqrt2
=
\boxed{7|x|\sqrt2}.
$$


### 21

Primer caso:
$$
\frac7{3\sqrt5}
=
\frac{7\sqrt5}{15}.
$$

Segundo:
$$
\frac{2\sqrt3}{\sqrt7}
=
\frac{2\sqrt{21}}7.
$$

Tercero:
$$
\frac5{\sqrt[3]4}
\cdot
\frac{\sqrt[3]2}{\sqrt[3]2}
=
\frac{5\sqrt[3]2}{\sqrt[3]8}
=
\boxed{\frac{5\sqrt[3]2}{2}}.
$$


### 22

Usamos conjugados.

$$
\frac1{3+\sqrt5}
=
\frac{3-\sqrt5}{9-5}
=
\boxed{\frac{3-\sqrt5}{4}}.
$$

$$
\frac2{\sqrt7-\sqrt3}
=
\frac{2(\sqrt7+\sqrt3)}{7-3}
=
\boxed{\frac{\sqrt7+\sqrt3}{2}}.
$$

Finalmente,
$$
\frac{\sqrt2}{2-\sqrt2}
=
\frac{\sqrt2(2+\sqrt2)}{4-2}
=
\boxed{1+\sqrt2}.
$$


### 23

Con $a,b>0$:
$$
\sqrt[3]{a^2}\sqrt[6]{a^5}
=
a^{2/3}a^{5/6}
=
a^{4/6+5/6}
=
a^{3/2}.
$$
Por tanto,
$$
\boxed{a\sqrt a}.
$$

Y
$$
\frac{\sqrt[4]{b^7}}{\sqrt b}
=
b^{7/4-1/2}
=
b^{7/4-2/4}
=
b^{5/4}.
$$
Así,
$$
\boxed{b\sqrt[4]b}.
$$


### 24

Como los denominadores reducidos son impares:
$$
(-27)^{2/3}
=
(\sqrt[3]{-27})^2
=
(-3)^2
=
9,
$$
$$
(-32)^{3/5}
=
(\sqrt[5]{-32})^3
=
(-2)^3
=
-8,
$$
$$
(-8)^{-2/3}
=
\frac1{(-8)^{2/3}}
=
\frac14,
$$
y
$$
(-243)^{1/5}
=
-3.
$$


### 25

La expresión original exige
$$
x\neq2.
$$
Además,
$$
\sqrt{(x-2)^2}=|x-2|.
$$
Por tanto
$$
\boxed{
\frac{\sqrt{(x-2)^2}}{x-2}
=
\frac{|x-2|}{x-2},
\qquad x\neq2.
}
$$
Equivalentemente,
$$
\frac{|x-2|}{x-2}
=
\begin{cases}
1,&x>2,\\
-1,&x<2.
\end{cases}
$$


### 26

Pasamos los radicales a exponentes:
$$
\sqrt[3]{a^2b^3}=a^{2/3}b,
\qquad
\sqrt a=a^{1/2}.
$$
Entonces
$$
\frac{a^{7/6}b^{-5/4}a^{2/3}b}
     {a^{-1/2}b^{1/4}a^{1/2}}.
$$
Para $a$:
$$
\frac76+\frac23=\frac{11}{6},
$$
y el denominador aporta exponente total $0$.

Para $b$:
$$
-\frac54+1-\frac14
=
-\frac12.
$$
Así,
$$
\boxed{\frac{a^{11/6}}{b^{1/2}}},
\qquad a,b>0.
$$

## C. Justificación y reconstrucción


### 27

Queremos conservar la regla del cociente. Para $a\neq0$ y $m>0$:
$$
\frac{a^m}{a^m}=1.
$$
Si la ley
$$
\frac{a^m}{a^m}=a^{m-m}
$$
continúa siendo válida, entonces
$$
a^{m-m}=a^0.
$$
Por tanto necesariamente
$$
a^0=1.
$$

La hipótesis $a\neq0$ se usa exactamente al formar el cociente $a^m/a^m$. Si $a=0$, ese cociente sería $0/0$ y no está definido. De aquí no se obtiene ningún valor para $0^0$.


### 28

Deseamos preservar
$$
a^na^{-n}=a^{n-n}=a^0=1.
$$
Con $a\neq0$, $a^n$ posee inverso multiplicativo. Por tanto el único valor posible para $a^{-n}$ que mantiene la ley es
$$
\boxed{a^{-n}=\frac1{a^n}}.
$$

La condición $a\neq0$ es indispensable: si $a=0$, la definición exigiría dividir por cero.


### 29

Definimos para $k>0$
$$
a^{-k}=\frac1{a^k},
\qquad a^0=1,
$$
con $a\neq0$.

Hay tres configuraciones esenciales.

**1. $m,n\ge0$.** La ley ya fue demostrada por producto repetido:
$$
a^ma^n=a^{m+n}.
$$

**2. Uno es no negativo y el otro negativo.** Escribamos $n=-q$ con $q>0$:
$$
a^ma^{-q}
=
\frac{a^m}{a^q}.
$$
Si $m\ge q$, el cociente vale $a^{m-q}=a^{m+n}$. Si $m<q$,
$$
\frac{a^m}{a^q}
=
\frac1{a^{q-m}}
=
a^{m-q}
=
a^{m+n}.
$$

**3. Ambos son negativos.** Si $m=-p$ y $n=-q$,
$$
a^ma^n
=
\frac1{a^p}\frac1{a^q}
=
\frac1{a^{p+q}}
=
a^{-(p+q)}
=
a^{m+n}.
$$

Así, para todo $m,n\in\mathbb Z$ y $a\neq0$,
$$
\boxed{a^ma^n=a^{m+n}}.
$$


### 30

Sea $x\in\mathbb R$. El número $|x|$ satisface dos propiedades:

1. $|x|\ge0$;
2. $|x|^2=x^2$.

La raíz cuadrada principal de $x^2$ es, por definición, el único número no negativo cuyo cuadrado es $x^2$. Como $|x|$ cumple exactamente esas condiciones,
$$
\boxed{\sqrt{x^2}=|x|}.
$$

El argumento usa la **unicidad de la raíz principal**; no es una cancelación formal entre el cuadrado y la raíz.


### 31

Si $n$ es par, $|x|\ge0$ y
$$
|x|^n=x^n.
$$
La raíz $n$-ésima principal de $x^n$ debe ser no negativa, de modo que
$$
\sqrt[n]{x^n}=|x|.
$$

Si $n$ es impar, la función $t\mapsto t^n$ conserva el signo y cada real tiene una única raíz $n$-ésima real. Como
$$
x^n=x^n,
$$
esa raíz es precisamente $x$:
$$
\sqrt[n]{x^n}=x.
$$

Por tanto,
$$
\boxed{
\sqrt[n]{x^n}
=
\begin{cases}
|x|,&n\text{ par},\\
x,&n\text{ impar}.
\end{cases}}
$$


### 32

Sea
$$
c=\sqrt a\,\sqrt b.
$$
Como $a,b\ge0$, ambas raíces son no negativas, luego
$$
c\ge0.
$$
Además,
$$
c^2
=
(\sqrt a)^2(\sqrt b)^2
=
ab.
$$
Por definición, $\sqrt{ab}$ es el único número no negativo cuyo cuadrado es $ab$. Como $c$ cumple ambas condiciones,
$$
\boxed{\sqrt{ab}=\sqrt a\sqrt b}.
$$


### 33

(a) Tomemos $u=v=1$:
$$
\sqrt{u+v}=\sqrt2
\neq
2=\sqrt u+\sqrt v.
$$

(b) Con $u=v=1$:
$$
(u+v)^2=4
\neq
2=u^2+v^2.
$$

(c) Con $u=-1$:
$$
\sqrt{u^2}=1
\neq
-1=u.
$$

Cada afirmación era universal: pretendía valer para **todos** los valores permitidos. Una proposición universal queda refutada en cuanto aparece un solo caso del dominio en el que resulta falsa.


### 34

Supongamos
$$
\frac mn=\frac pq,
\qquad n,q>0,
$$
y $a>0$. Entonces
$$
mq=np.
$$

Sea $x=(\sqrt[n]a)^m$ y $y=(\sqrt[q]a)^p$, con la convención de índice uno. Ambos son positivos. Las leyes de exponentes enteros, válidas también para exponentes negativos porque las bases son no nulas, dan $x^{nq}=a^{mq}$ y $y^{nq}=a^{pn}$. Como $mq=np$, ambos son la misma raíz positiva de ese número. Por unicidad, $x=y$.

Así, el valor de $a^r$ depende del racional $r$, no de una escritura fraccionaria accidental. La unicidad de raíces positivas es la propiedad estructural que garantiza esa independencia.


### 35

Sea
$$
b=\sqrt[n]a.
$$
Como $a>0$, tenemos $b>0$ y
$$
b^n=a.
$$

Si $m\ge0$, entonces
$$
(b^m)^n=b^{mn}=(b^n)^m=a^m.
$$
Además $b^m>0$. Por unicidad de la raíz $n$-ésima positiva de $a^m$,
$$
b^m=\sqrt[n]{a^m}.
$$
Como por definición
$$
a^{m/n}=b^m,
$$
obtenemos
$$
\boxed{
a^{m/n}
=
(\sqrt[n]a)^m
=
\sqrt[n]{a^m}.
}
$$

Si $m<0$, se aplica el mismo argumento a $-m>0$ y luego se toman recíprocos; la positividad de $a$ garantiza que todo está definido.


### 36

Escribamos
$$
r=\frac mn,\qquad
s=\frac pq
$$
con denominadores positivos. Para $a>0$, todas las raíces intermedias son positivas y únicas.

Sea $b=a^{m/n}>0$, y sea $u=b^{p/q}>0$. Por definición de potencia racional sobre bases positivas y por las leyes enteras, $b^n=a^m$ y $u^q=b^p$. Entonces

$$
u^{nq}=(u^q)^n=(b^p)^n=(b^n)^p=a^{mp}.
$$

Por otra parte, $v=a^{mp/(nq)}>0$ satisface $v^{nq}=a^{mp}$: puede evaluarse con la fracción no reducida porque la independencia de representación ya se justificó en la solución del ejercicio 34. Como $u,v$ son positivos y tienen la misma potencia entera $nq$, la unicidad de la raíz positiva da $u=v$. Se obtiene $(a^r)^s=a^{rs}$ sin suponer esa ley durante la prueba. Si algún exponente es cero, las mismas igualdades siguen válidas porque todas las bases son positivas.

La positividad es decisiva: no hay cambio de signo ni ambigüedad de raíz principal. Con bases negativas la ley puede fallar. Por ejemplo,
$$
\left((-8)^{2/3}\right)^{3/2}=4^{3/2}=8,
$$
mientras que
$$
(-8)^{(2/3)(3/2)}=(-8)^1=-8.
$$

Por eso la ley se adopta sistemáticamente sobre bases positivas.


### 37

Multiplicar una fracción por
$$
\frac{u-\sqrt v}{u-\sqrt v}
$$
conserva su valor sólo cuando
$$
u-\sqrt v\neq0,
$$
porque entonces el multiplicador vale exactamente $1$.

La utilidad proviene de
$$
(u+\sqrt v)(u-\sqrt v)=u^2-v.
$$
Así desaparece el radical cruzado del denominador.

Si
$$
u-\sqrt v=0,
$$
el supuesto multiplicador sería
$$
\frac00,
$$
que no está definido. Por tanto no sería una forma de $1$ y la transformación dejaría de ser legítima.


### 38

Una igualdad obtenida mediante simplificación debe interpretarse **sobre el dominio donde empezó la cadena**.

Para
$$
E(x)=\frac{x^2}{x},
$$
el dominio es
$$
x\neq0.
$$
En ese dominio,
$$
E(x)=x.
$$
La forma aislada
$$
S(x)=x
$$
sí está definida en $x=0$, pero ese punto nunca perteneció al dominio de $E$.

Por tanto,
$$
\frac{x^2}{x}=x
\qquad(x\neq0),
$$
pero las dos expresiones no definen la misma función si a $S$ se le asigna su dominio natural completo.

## D. Diagnóstico del primer paso inválido


### 39

La regla correcta es
$$
\sqrt{u^2}=|u|.
$$
Con $u=x-7$:
$$
\boxed{\sqrt{(x-7)^2}=|x-7|}.
$$

El primer error consiste en reemplazar la raíz principal por $u$ sin comprobar que $u\ge0$. La forma $x-7$ sólo sería válida bajo
$$
x\ge7.
$$


### 40

No existe una ley que distribuya la raíz sobre una suma.

Con $x=9$:
$$
\sqrt{x+16}
=
\sqrt{25}
=
5,
$$
mientras que
$$
\sqrt x+4
=
3+4
=
7.
$$
Por tanto la identidad propuesta es falsa.

Una ley verdadera relacionada es, por ejemplo,
$$
\sqrt{ab}=\sqrt a\sqrt b
\qquad(a,b\ge0),
$$
o
$$
\sqrt{\frac ab}=\frac{\sqrt a}{\sqrt b}
\qquad(a\ge0,\ b>0).
$$


### 41

Las leyes de exponentes se distribuyen sobre productos, no sobre sumas.

Por C13,
$$
(a+b)^3
=
a^3+3a^2b+3ab^2+b^3.
$$
La expresión
$$
a^3+b^3
$$
omite los términos cruzados
$$
3a^2b+3ab^2.
$$

Por tanto,
$$
(a+b)^3=a^3+b^3
$$
sólo puede ocurrir en casos especiales, no como identidad universal.


### 42

La cadena es correcta **cuando $x\neq0$**:
$$
\frac{x^5}{x^5}
=
1
=
x^0.
$$

En $x=0$ la primera expresión sería
$$
\frac00,
$$
que no está definida. Por tanto la cadena nunca produce una afirmación sobre $0^0$.

Lo correcto es escribir
$$
\frac{x^5}{x^5}=x^0=1,
\qquad x\neq0.
$$


### 43

Por definición,
$$
(-3)^{-2}
=
\frac1{(-3)^2}
=
\frac19.
$$

El signo negativo del exponente indica **recíproco**; no convierte el resultado en negativo. El signo del valor depende de la base y de la paridad del exponente entero:
$$
(-3)^2=9>0.
$$

Por tanto,
$$
\boxed{(-3)^{-2}=\frac19}.
$$


### 44

El cálculo
$$
\frac{x^4}{x}=x^3
$$
es correcto siempre que el cociente original esté definido.

Pero
$$
\frac{x^4}{x}
$$
exige
$$
x\neq0.
$$
La forma $x^3$ sí existe en $x=0$, de modo que no puede declararse la igualdad sobre todo $\mathbb R$.

La formulación correcta es
$$
\boxed{\frac{x^4}{x}=x^3,\qquad x\neq0.}
$$


### 45

El exponente debe reducirse primero:
$$
\frac26=\frac13.
$$
Por tanto
$$
(-64)^{2/6}
=
(-64)^{1/3}
=
\sqrt[3]{-64}
=
-4.
$$

El primer paso de la cadena propuesta,
$$
(-64)^{2/6}
=
\sqrt[6]{(-64)^2},
$$
usa la representación no reducida $2/6$ para una base negativa. Bajo la política del capítulo esa operación no define correctamente la potencia racional.

Así,
$$
\boxed{(-64)^{2/6}=-4}.
$$


### 46

Primero evaluamos el lado izquierdo por una ruta permitida:
$$
(-27)^{2/3}
=
(\sqrt[3]{-27})^2
=
9.
$$
Entonces
$$
\left((-27)^{2/3}\right)^{3/2}
=
9^{3/2}
=
(\sqrt9)^3
=
27.
$$

La combinación formal de exponentes daría
$$
(-27)^{(2/3)(3/2)}
=
(-27)^1
=
-27.
$$

La discrepancia aparece porque
$$
(a^r)^s=a^{rs}
$$
se está usando fuera de su dominio rector de bases positivas.

Por tanto el lado izquierdo vale
$$
\boxed{27},
$$
no $-27$.


### 47

El producto dentro de la raíz sí está en $\mathbb R$:
$$
(-3)(-12)=36,
$$
luego
$$
\sqrt{(-3)(-12)}
=
\sqrt{36}
=
6.
$$

El paso
$$
\sqrt{(-3)(-12)}
=
\sqrt{-3}\sqrt{-12}
$$
es el primero inválido: las raíces cuadradas del lado derecho no son reales.

La ley
$$
\sqrt{ab}=\sqrt a\sqrt b
$$
requiere $a,b\ge0$.


### 48

Como
$$
\sqrt{x^4}=x^2
$$
para todo real $x$, y
$$
\sqrt{y^2}=|y|,
$$
tenemos
$$
\sqrt{x^4y^2}
=
x^2|y|.
$$

El paso incorrecto consiste en reemplazar
$$
\sqrt{y^2}
$$
por $y$ sin controlar su signo.

La forma universal es
$$
\boxed{x^2|y|}.
$$
La igualdad con $x^2y$ se cumple exactamente cuando $y\ge0$ o $x=0$. Si $x=0$, ambos lados son cero incluso cuando $y<0$; si $x\ne0$ y $y<0$, los signos de los dos valores son opuestos.


### 49

La expresión original es simplemente
$$
\frac1{1+\sqrt1}
=
\frac1{2}.
$$

El conjugado sería
$$
1-\sqrt1=0.
$$
Por tanto
$$
\frac{1-\sqrt1}{1-\sqrt1}
=
\frac00
$$
no está definido y no puede usarse como multiplicador equivalente a $1$.

La lección es que “usar el conjugado” no basta: el factor por el que multiplicamos debe ser no nulo.


### 50

El dominio original exige
$$
x\neq1.
$$
El primer paso inválido es
$$
\sqrt{(x-1)^2}=x-1.
$$
La regla correcta es
$$
\sqrt{(x-1)^2}=|x-1|.
$$
Así,
$$
\frac{\sqrt{(x-1)^2}}{x-1}
=
\frac{|x-1|}{x-1},
\qquad x\neq1.
$$

Por casos:
$$
\frac{|x-1|}{x-1}
=
\begin{cases}
1,&x>1,\\
-1,&x<1.
\end{cases}
$$

La cadena propuesta sólo es correcta en la región $x>1$.

## E. Estrategia y elección de representación


### 51

**Ruta exponencial.**
Como $a>0$,
$$
\sqrt[3]{a^5}\sqrt[6]a
=
a^{5/3}a^{1/6}
=
a^{10/6+1/6}
=
a^{11/6}.
$$

**Ruta radical.**
Pasamos al índice $6$:
$$
\sqrt[3]{a^5}
=
\sqrt[6]{a^{10}},
$$
de modo que
$$
\sqrt[6]{a^{10}}\sqrt[6]a
=
\sqrt[6]{a^{11}}
=
a\sqrt[6]{a^5}.
$$

Como
$$
a^{11/6}=a\sqrt[6]{a^5},
$$
ambas rutas coinciden.

La ruta exponencial hace visible de inmediato la suma de exponentes y es más corta.


### 52

La decisión estratégica correcta es **simplificar cada radical antes de sumar**:
$$
4\sqrt{18}
=
12\sqrt2,
$$
$$
-3\sqrt8
=
-6\sqrt2,
$$
$$
\sqrt{50}
=
5\sqrt2.
$$
Entonces
$$
12\sqrt2-6\sqrt2+5\sqrt2
=
\boxed{11\sqrt2}.
$$

Sumar coeficientes desde el comienzo sería injustificado porque todavía no sabemos si las partes radicales son semejantes.


### 53

Racionalizando:
$$
\frac1{\sqrt5+2}
\cdot
\frac{\sqrt5-2}{\sqrt5-2}
=
\frac{\sqrt5-2}{5-4}
=
\boxed{\sqrt5-2}.
$$

Las dos formas son equivalentes.

- La forma original puede ser natural si se quiere conservar la estructura “recíproco de una suma”.
- La forma racionalizada es útil si se desea sumar con una expresión que contiene el conjugado o eliminar radicales del denominador.
- Para una aproximación decimal, cualquiera de las dos puede evaluarse directamente.

Racionalizar cambia la representación, no el valor.


### 54

**1. Dominio.**
El numerador exige
$$
x-1\ge0,
$$
luego $x\ge1$.

Además $x^{-2}$ exige $x\neq0$ y $\sqrt{x+3}$ está en el denominador, por lo que $x+3>0$. Ambas condiciones ya se cumplen si $x\ge1$.

Así,
$$
D=[1,\infty).
$$

**2. Exponente negativo.**
$$
x^{-2}=\frac1{x^2}.
$$

Entonces
$$
\frac{\sqrt{x-1}}{x^{-2}\sqrt{x+3}}
=
\frac{\sqrt{x-1}}{\sqrt{x+3}/x^2}
=
\boxed{\frac{x^2\sqrt{x-1}}{\sqrt{x+3}}},
\qquad x\ge1.
$$

La lectura del dominio antes de simplificar evita perder condiciones.


### 55

Elegimos valores pequeños y simétricos:
$$
u=v=1.
$$
Entonces
$$
\sqrt{u^2+v^2}
=
\sqrt2,
$$
mientras que
$$
|u|+|v|
=
2.
$$
Como
$$
\sqrt2\neq2,
$$
la identidad queda refutada.

La elección $u=v=1$ elimina signos y produce cálculos mínimos; ésa es una buena estrategia para construir contraejemplos.


### 56

**Ruta exponencial.**
$$
\frac{\sqrt[4]{a^3}}{\sqrt[6]a}
=
a^{3/4-1/6}
=
a^{9/12-2/12}
=
\boxed{a^{7/12}}.
$$

**Ruta radical.**
Usamos índice común $12$:
$$
\sqrt[4]{a^3}
=
\sqrt[12]{a^9},
$$
$$
\sqrt[6]a
=
\sqrt[12]{a^2}.
$$
Por tanto
$$
\frac{\sqrt[12]{a^9}}{\sqrt[12]{a^2}}
=
\boxed{\sqrt[12]{a^7}}.
$$

Las formas coinciden porque $a>0$:
$$
a^{7/12}=\sqrt[12]{a^7}.
$$

La ruta exponencial es más breve; la radical hace visible el índice común.


### 57

Como $x>0$, la notación exponencial es la más transparente:
$$
\frac{(x^{3/4})^2\sqrt x}{x^{1/2}}
=
x^{3/2}x^{1/2}x^{-1/2}.
$$
Sumando exponentes:
$$
\frac32+\frac12-\frac12
=
\frac32.
$$
Así,
$$
\boxed{x^{3/2}}.
$$

Si se mezclan radicales y exponentes sin un objetivo, la cancelación entre $\sqrt x$ y $x^{1/2}$ queda menos visible.


### 58

Factorizamos:
$$
72(x-1)^6
=
36\cdot2\cdot\big((x-1)^3\big)^2.
$$
Entonces
$$
\sqrt{72(x-1)^6}
=
6\sqrt2\,\left|(x-1)^3\right|.
$$
Como
$$
|(x-1)^3|=|x-1|^3,
$$
obtenemos
$$
\boxed{6\sqrt2\,|x-1|^3}.
$$

El valor absoluto aparece exactamente al extraer de una raíz cuadrada el cuadrado de $(x-1)^3$.


### 59

Racionalizamos:
$$
\frac3{\sqrt7-2}
\cdot
\frac{\sqrt7+2}{\sqrt7+2}
=
\frac{3(\sqrt7+2)}{7-4}
=
\boxed{\sqrt7+2}.
$$

(a) Para una estimación numérica, cualquiera sirve; la forma racionalizada tiene una suma sencilla.

(b) Para sumar con
$$
\frac3{\sqrt7+2},
$$
conviene racionalizar ambas:
$$
\frac3{\sqrt7+2}=\sqrt7-2.
$$
La suma queda
$$
2\sqrt7.
$$

(c) Para estudiar dominio, la forma original ya basta: el denominador es una constante positiva. Racionalizar no aporta información adicional.


### 60

Con $x\neq0$:
$$
\sqrt{50x^4}
=
5\sqrt2\,\sqrt{x^4}
=
5\sqrt2\,x^2.
$$
Por tanto
$$
\frac{\sqrt{50x^4}}{x\sqrt2}
=
\frac{5\sqrt2\,x^2}{x\sqrt2}
=
\boxed{5x},
\qquad x\neq0.
$$

La ruta segura trata primero la raíz:
$$
\sqrt{x^4}=x^2.
$$
Cancelar símbolos antes de identificar correctamente lo que sale del radical puede ocultar el papel del signo y del dominio.

## F. Transferencia acumulativa


### 61

La potencia
$$
x^{-1/2}
$$
se trabaja sistemáticamente para $x>0$.

Además, como
$$
\sqrt{x-1}
$$
está en el denominador,
$$
x-1>0,
$$
es decir,
$$
x>1.
$$
La intersección es
$$
D=(1,\infty).
$$

Ahora
$$
x^{-1/2}=\frac1{\sqrt x},
$$
de modo que
$$
\frac{x^{-1/2}}{\sqrt{x-1}}
=
\frac1{\sqrt x\,\sqrt{x-1}}
=
\boxed{\frac1{\sqrt{x(x-1)}}},
\qquad x>1.
$$


### 62

El dominio original exige
$$
x\neq3
$$
por $(x-3)^{-2}$ y
$$
x\neq-1
$$
por el denominador $x+1$.

Además,
$$
\sqrt{(x-3)^4}
=
\sqrt{\big((x-3)^2\big)^2}
=
(x-3)^2,
$$
porque $(x-3)^2\ge0$.

Entonces
$$
(x-3)^{-2}\sqrt{(x-3)^4}
=
\frac1{(x-3)^2}(x-3)^2
=
1
$$
en el dominio original.

Por tanto,
$$
\boxed{\frac1{x+1}},
\qquad x\neq3,-1.
$$

Aunque la forma final está definida en $x=3$, ese valor no se reincorpora.


### 63

Por C13,
$$
(u+v)^2=u^2+2uv+v^2.
$$
Por tanto,
$$
u^2+2uv+v^2=(u+v)^2,
$$
y entonces
$$
\sqrt{u^2+2uv+v^2}
=
\sqrt{(u+v)^2}
=
\boxed{|u+v|}.
$$

En cambio,
$$
u^2+v^2
$$
no es el cuadrado de $u+v$ porque faltaría el término $2uv$. Por eso no puede concluirse
$$
\sqrt{u^2+v^2}=|u|+|v|.
$$


### 64

La condición $a+b\neq0$ hace que el cociente esté definido.

Observamos:
$$
\frac{(a-b)^4}{(a+b)^2}
=
\left(\frac{(a-b)^2}{a+b}\right)^2.
$$
Por tanto
$$
\sqrt{\frac{(a-b)^4}{(a+b)^2}}
=
\left|
\frac{(a-b)^2}{a+b}
\right|.
$$
Como $(a-b)^2\ge0$,
$$
\boxed{
\frac{(a-b)^2}{|a+b|}
},
\qquad a+b\neq0.
$$


### 65

La teoría sistemática de $x^{3/2}$ y $x^{-1/2}$ exige
$$
x>0.
$$
La raíz $\sqrt{x+2}$ sólo exigiría $x\ge-2$, de modo que la intersección sigue siendo
$$
x>0.
$$

Simplificamos:
$$
\frac{x^{3/2}}{x^{-1/2}\sqrt{x+2}}
=
\frac{x^{3/2-(-1/2)}}{\sqrt{x+2}}
=
\boxed{\frac{x^2}{\sqrt{x+2}}},
\qquad x>0.
$$

La forma final aislada está definida para $x>-2$, porque la raíz del denominador no puede anularse; pero el dominio original era $x>0$ y debe conservarse.


### 66

Tenemos
$$
E(x)=\frac{\sqrt{x^2}}x=\frac{|x|}{x},
\qquad x\neq0.
$$
Por tanto
$$
D_E=\mathbb R\setminus\{0\}.
$$

También
$$
F(x)=\frac{|x|}{x}
$$
tiene dominio
$$
D_F=\mathbb R\setminus\{0\}.
$$

En cambio
$$
G(x)=1
$$
tiene dominio natural
$$
D_G=\mathbb R.
$$

Así, $E$ y $F$ son la misma función: mismo dominio y mismos valores. En su dominio común con $G$, no coinciden para $x<0$, pues
$$
E(x)=F(x)=-1,
\qquad
G(x)=1.
$$

La comparación muestra que una forma simbólica no determina por sí sola la función: también importa el dominio.


### 67

Para todo real $t$:
$$
\sqrt{(t-3)^2}=|t-3|,
$$
$$
\sqrt{(t+3)^2}=|t+3|.
$$
Así,
$$
\boxed{|t-3||t+3|}
=
\boxed{|t^2-9|}.
$$

Sustituir esto por
$$
(t-3)(t+3)=t^2-9
$$
sería válido sólo cuando
$$
t^2-9\ge0,
$$
es decir,
$$
t\le-3
\quad\text{o}\quad
t\ge3.
$$


### 68

Primero el dominio. Las raíces exigen
$$
x+1\ge0,
\qquad
x+4\ge0.
$$
La condición dominante es
$$
x\ge-1.
$$

En ese dominio,
$$
\sqrt{x+4}>\sqrt{x+1},
$$
de modo que el denominador original es positivo y no se anula. El conjugado
$$
\sqrt{x+4}+\sqrt{x+1}
$$
también es positivo.

Racionalizamos:
$$
\frac{\sqrt{x+1}}{\sqrt{x+4}-\sqrt{x+1}}
\cdot
\frac{\sqrt{x+4}+\sqrt{x+1}}
     {\sqrt{x+4}+\sqrt{x+1}}.
$$
El denominador es
$$
(x+4)-(x+1)=3.
$$
Por tanto,
$$
\boxed{
\frac{\sqrt{x+1}\big(\sqrt{x+4}+\sqrt{x+1}\big)}3
},
\qquad x\ge-1.
$$


### 69

Leemos primero la raíz interior:
$$
\sqrt x
$$
exige
$$
x\ge0.
$$

Luego la raíz exterior exige
$$
1-\sqrt x\ge0,
$$
es decir,
$$
\sqrt x\le1.
$$
Como $\sqrt x\ge0$, esto equivale a
$$
x\le1.
$$

Por tanto,
$$
\boxed{D=[0,1]}.
$$

De afuera hacia adentro, la raíz exterior exige $1-\sqrt x\ge0$, siempre que exista la raíz interior. Esta última exige $x\ge0$ y por ello $\sqrt x\ge0$. Juntas, las condiciones son $0\le\sqrt x\le1$, equivalentes a $0\le x\le1$. La cota superior uno para el radicando exterior procede de la no negatividad de la raíz interior, no de la raíz exterior por sí sola.

No usamos ninguna técnica de desanidamiento; sólo intersectamos condiciones de dominio.


### 70

Escribimos
$$
r=\frac pq
$$
en términos mínimos, con $q>0$.

Como la base es negativa:

- si $q$ es par, $(-c)^{p/q}$ no es real;
- si $q$ es impar, la raíz $q$-ésima real de $-c$ existe, de modo que la potencia es real.

Cuando $q$ es impar,
$$
(-c)^{p/q}
=
\left(-c^{1/q}\right)^p.
$$
Por tanto:

- si $p$ es par, el resultado es positivo;
- si $p$ es impar, el resultado es negativo.

Si $p<0$, la base es no nula, así que se toma además el recíproco; la regla de signo según la paridad permanece igual.


### 71

Como $x>0$:
$$
\sqrt[3]{x^4}=x^{4/3},
$$
$$
\sqrt[6]{x^{-1}}=x^{-1/6}.
$$
Entonces
$$
\frac{x^{4/3}x^{-5/6}}{x^{-1/6}}
=
x^{4/3-5/6+1/6}.
$$
Llevando a sextos:
$$
\frac86-\frac56+\frac16
=
\frac46
=
\frac23.
$$
Así,
$$
\boxed{x^{2/3}}
=
\boxed{\sqrt[3]{x^2}}.
$$


### 72

Como $x\neq0$:
$$
\sqrt{18x^6}
=
3\sqrt2\,|x^3|
=
3\sqrt2\,|x|^3.
$$
Por tanto
$$
\frac{\sqrt{18x^6}}{x^2}\cdot\frac{x^{-1}}{\sqrt2}
=
\frac{3\sqrt2\,|x|^3}{x^2}\cdot\frac1{x\sqrt2}.
$$
Cancelando factores no nulos:
$$
=
3\frac{|x|^3}{x^3}.
$$
Como
$$
\frac{|x|^3}{x^3}
=
\frac{|x|}{x},
$$
obtenemos
$$
\boxed{3\frac{|x|}{x}},
\qquad x\neq0.
$$

La dependencia de
$$
\sqrt{x^2}=|x|
$$
aparece al extraer el factor $x^3$ de la raíz cuadrada:
$$
\sqrt{x^6}=|x^3|.
$$

## G. Síntesis avanzada


### 73

**Lectura y dominio.**
La potencia $x^{-3/2}$, bajo la política sistemática del capítulo, exige
$$
x>0.
$$
Con $x>0$, todas las raíces restantes existen y
$$
\sqrt{x+1}-1>0,
$$
de modo que el denominador no se anula. Por tanto
$$
D=(0,\infty).
$$

**Ruta exponencial.**
Como $x>0$:
$$
x^{-3/2}\sqrt{x^5}
=
x^{-3/2}x^{5/2}
=
x.
$$
Así
$$
E(x)
=
\frac{x}{\sqrt x(\sqrt{x+1}-1)}
=
\frac{\sqrt x}{\sqrt{x+1}-1}.
$$
Racionalizando el último denominador:
$$
E(x)
=
\frac{\sqrt x(\sqrt{x+1}+1)}
     {(x+1)-1}
=
\boxed{\frac{\sqrt{x+1}+1}{\sqrt x}},
\qquad x>0.
$$

**Ruta radical.**
Como $x>0$,
$$
\sqrt{x^5}=x^2\sqrt x,
$$
mientras que
$$
x^{-3/2}=\frac1{x\sqrt x}.
$$
Por tanto el numerador vuelve a ser
$$
x.
$$
Desde allí se obtiene la misma forma.

**Comparación.**
La ruta exponencial condensa mejor las potencias; la radical hace visible cómo se cancelan los factores de $\sqrt x$. En ambas rutas, el dominio $x>0$ se conserva aunque la forma final por sí sola sugiera sólo $x>0$ por su denominador.


### 74

Sea $n$ par. Entonces
$$
a^{2n}b^n
=
(a^2b)^n.
$$
Como $n$ es par,
$$
\sqrt[n]{(a^2b)^n}
=
|a^2b|.
$$
Pero $a^2\ge0$, de modo que
$$
|a^2b|
=
a^2|b|.
$$
Por tanto
$$
\boxed{
\sqrt[n]{a^{2n}b^n}=a^2|b|
}
$$
para todos $a,b\in\mathbb R$. El radicando siempre es no negativo porque $a^{2n}\ge0$ y $b^n\ge0$.

Si el índice $n$ fuera impar, la raíz impar recuperaría directamente la base:
$$
\sqrt[n]{(a^2b)^n}=a^2b.
$$
La diferencia entre $a^2|b|$ y $a^2b$ proviene exactamente de la raíz principal de índice par.


### 75

**Ruta 1: exponentes racionales.**
Para $a>0$:
$$
P(a)
=
a^{5/3}a^{3/4}a^{-7/12}.
$$
Con denominador común $12$:
$$
\frac{20}{12}+\frac9{12}-\frac7{12}
=
\frac{22}{12}
=
\frac{11}{6}.
$$
Así,
$$
\boxed{P(a)=a^{11/6}}.
$$

**Ruta 2: índice común.**
Escribimos todo con índice $12$:
$$
\sqrt[3]{a^5}=\sqrt[12]{a^{20}},
$$
$$
\sqrt[4]{a^3}=\sqrt[12]{a^9},
$$
$$
a^{7/12}=\sqrt[12]{a^7}.
$$
Entonces
$$
P(a)
=
\sqrt[12]{a^{20+9-7}}
=
\sqrt[12]{a^{22}}.
$$
Extraemos $a^{12}$:
$$
P(a)
=
a\sqrt[12]{a^{10}}
=
a\sqrt[6]{a^5}.
$$
Como
$$
a\sqrt[6]{a^5}=a^{11/6},
$$
las rutas coinciden.

La ruta exponencial es más corta; la radical hace visible la unificación de índices y sirve como control independiente.


### 76

La cadena debe auditarse desde el primer símbolo.

El exponente
$$
\frac46
$$
se reduce a
$$
\frac23.
$$
Por tanto el primer paso
$$
(-64)^{4/6}
=
\left((-64)^{1/6}\right)^4
$$
ya es inválido bajo la definición del capítulo: se está usando una representación no reducida con denominador par para una base negativa.

El paso siguiente
$$
(-64)^{1/6}=\sqrt[6]{-64}
$$
sale además de $\mathbb R$, pues una raíz sexta de un número negativo no es real. La escritura posterior $(-2)^4$ no puede reparar esa ruptura.

La cadena correcta empieza reduciendo:
$$
(-64)^{4/6}
=
(-64)^{2/3}.
$$
Como el denominador reducido es impar,
$$
(-64)^{2/3}
=
\left(\sqrt[3]{-64}\right)^2
=
(-4)^2
=
\boxed{16}.
$$

Que una cadena inválida termine casualmente en $16$ no la convierte en demostración: la validez depende de cada paso, no sólo del resultado final.


### 77

Sea
$$
A=\sqrt2+\sqrt3.
$$
Entonces
$$
\frac1{A+\sqrt5}
\cdot
\frac{A-\sqrt5}{A-\sqrt5}
=
\frac{A-\sqrt5}{A^2-5}.
$$
Calculamos
$$
A^2
=
2+3+2\sqrt6
=
5+2\sqrt6.
$$
Por tanto
$$
A^2-5=2\sqrt6,
$$
y
$$
\frac1{\sqrt2+\sqrt3+\sqrt5}
=
\frac{\sqrt2+\sqrt3-\sqrt5}{2\sqrt6}.
$$

Racionalizamos el denominador restante:
$$
=
\frac{\sqrt6(\sqrt2+\sqrt3-\sqrt5)}{12}.
$$
Simplificando:
$$
\sqrt{12}=2\sqrt3,\qquad
\sqrt{18}=3\sqrt2.
$$
Así,
$$
\boxed{
\frac{2\sqrt3+3\sqrt2-\sqrt{30}}{12}
}.
$$

Los multiplicadores son legítimos. En el primer paso,
$$
A-\sqrt5\neq0,
$$
pues
$$
A^2=5+2\sqrt6>5.
$$
En el segundo,
$$
\sqrt6\neq0.
$$


### 78

**Dominios.**

Para
$$
E(x)=\frac{\sqrt{x^2}}x,
$$
el denominador exige
$$
x\neq0.
$$
Por tanto
$$
D_E=\mathbb R\setminus\{0\}.
$$

Para
$$
F(x)=\frac{x}{\sqrt{x^2}},
$$
la raíz existe para todo real, pero el denominador vale $0$ en $x=0$. Así,
$$
D_F=\mathbb R\setminus\{0\}.
$$

Para
$$
G(x)=\frac{x^2}{|x|^2},
$$
el denominador también se anula en $0$:
$$
D_G=\mathbb R\setminus\{0\}.
$$

**Simplificación.**
Como
$$
\sqrt{x^2}=|x|,
$$
tenemos
$$
E(x)=\frac{|x|}{x},
$$
$$
F(x)=\frac{x}{|x|},
$$
y
$$
G(x)=1
\qquad(x\neq0).
$$

Pero para $x\neq0$,
$$
\frac{|x|}{x}
=
\frac{x}{|x|}
=
\begin{cases}
1,&x>0,\\
-1,&x<0.
\end{cases}
$$
Por tanto $E=F$ como funciones, mientras que $G$ difiere de ellas para $x<0$.

Aunque $G$ se simplifique a $1$, el punto $x=0$ no puede reincorporarse: no pertenecía al dominio original.


### 79

Escribimos
$$
r=\frac pq
$$
en términos mínimos, con $q>0$.

**(a) Existencia real.**
Como la base es negativa,
$$
(-c)^r
$$
es real exactamente cuando $q$ es impar. Si $q$ es par, la raíz real necesaria no existe.

**(b) Signo.**
Si $q$ es impar,
$$
(-c)^{p/q}
=
\left(-c^{1/q}\right)^p.
$$
El signo es positivo si $p$ es par y negativo si $p$ es impar.

**(c) Tres expresiones.**
Tenemos
$$
(-c)^{2/3}=c^{2/3}>0.
$$
Entonces
$$
\left((-c)^{2/3}\right)^{3/2}
=
(c^{2/3})^{3/2}
=
c.
$$
Pero
$$
(-c)^{(2/3)(3/2)}
=
(-c)^1
=
-c.
$$

**(d) Conclusión.**
Las dos últimas expresiones tienen valores opuestos:
$$
c\neq-c.
$$
Por tanto
$$
(a^r)^s=a^{rs}
$$
no puede trasladarse automáticamente a bases negativas. Sobre bases positivas, en cambio, las raíces intermedias permanecen positivas y la ley es estable.


### 80

**1. Lectura estructural.**
La expresión combina una raíz cuadrada con potencia de $x$, una potencia racional negativa, dos radicales en el denominador y una diferencia de raíces:
$$
Q(x)=
\frac{\sqrt{72x^6}\,x^{-1/2}}
     {\sqrt{x+2}\,(\sqrt{x+5}-\sqrt{x+2})}.
$$

**2. Dominio real original.**
La potencia $x^{-1/2}$ se trabaja sistemáticamente con
$$
x>0.
$$
Esta condición implica ya
$$
x+2>0,\qquad x+5>0.
$$
Además
$$
\sqrt{x+5}>\sqrt{x+2},
$$
así que la diferencia del denominador no se anula. Por tanto
$$
\boxed{D=(0,\infty)}.
$$

**3. Elección de representación.**
Para el bloque de potencias de $x$ conviene usar exponentes racionales; para la diferencia del denominador conviene conservar radicales, porque así queda visible el conjugado.

**4. Simplificación.**
Como $x>0$,
$$
\sqrt{72x^6}
=
6\sqrt2\,x^3.
$$
Entonces
$$
\sqrt{72x^6}\,x^{-1/2}
=
6\sqrt2\,x^{3-1/2}
=
6\sqrt2\,x^{5/2}.
$$
Así,
$$
Q(x)
=
\frac{6\sqrt2\,x^{5/2}}
     {\sqrt{x+2}\,(\sqrt{x+5}-\sqrt{x+2})}.
$$

**5. Valor absoluto.**
En una simplificación universal aparecería
$$
\sqrt{x^6}=|x^3|.
$$
Pero el dominio ya impone $x>0$, de modo que
$$
|x^3|=x^3.
$$
El valor absoluto no se omite: se resuelve usando información previa de dominio.

**6. Racionalización con objetivo.**
Racionalizamos la diferencia para eliminarla del denominador:
$$
\frac{\sqrt{x+5}+\sqrt{x+2}}
     {\sqrt{x+5}+\sqrt{x+2}}.
$$
Como
$$
(\sqrt{x+5}-\sqrt{x+2})(\sqrt{x+5}+\sqrt{x+2})=3,
$$
obtenemos
$$
Q(x)
=
\frac{2\sqrt2\,x^{5/2}
      (\sqrt{x+5}+\sqrt{x+2})}
     {\sqrt{x+2}}.
$$

Si se desea un denominador completamente racional, multiplicamos además por
$$
\frac{\sqrt{x+2}}{\sqrt{x+2}},
$$
válido porque $x>0$:
$$
\boxed{
Q(x)=
\frac{
2\sqrt2\,x^{5/2}
\left(\sqrt{(x+5)(x+2)}+x+2\right)
}{x+2}
},
\qquad x>0.
$$

**7. Dominio conservado.**
La forma final podría tener sentido en puntos adicionales si se leyera aislada, pero la equivalencia demostrada vale sobre
$$
x>0.
$$

**8. Auditoría final.**
Cada transformación respetó el dominio original; no se usaron ecuaciones radicales, no se introdujeron raíces extrañas y la racionalización tuvo un objetivo explícito: eliminar radicales del denominador. La forma final debe viajar acompañada por
$$
\boxed{x>0}.
$$

***
## H. Convenciones, leyes y construcción de dominios


### 81

Las dos potencias tienen el mismo exponente racional porque $10/6=5/3$. El denominador reducido tres es impar; ambas existen y son negativas. Si $a=-c$ con $c>0$, valen $-c^{5/3}$.

La raíz cúbica $\sqrt[3]{a^5}$ también es negativa y vale $-c^{5/3}$: su cubo es $a^5$ y la raíz impar es única. En cambio, $\sqrt[6]{a^{10}}=c^{5/3}>0$, porque la raíz sexta es principal. La potencia del radicando borró el signo y la raíz par no lo reconstruye. Finalmente, $\sqrt[6]a$ no es real; por ello $(\sqrt[6]a)^{10}$ tampoco define un valor real. Elevar después a un entero par no legitima una operación interior inexistente.

Así, las primeras tres expresiones coinciden; la cuarta existe y tiene el signo opuesto; la quinta no existe en $\mathbb R$. Una fracción no reducida sigue nombrando el mismo racional, pero no autoriza cualquier descomposición en operaciones.


### 82

Escribe $a=-c$, con $c>0$. Como $n$ es impar, la potencia interior existe y es $(-1)^m c^{m/n}$.

Si $m$ es impar, la base interior es negativa y el racional $n/m$, escrito con denominador positivo, tiene denominador $|m|$ impar. La potencia exterior existe. Su valor absoluto es $(c^{m/n})^{n/m}=c$ por las leyes sobre bases positivas; su signo es negativo porque el numerador reducido es impar. El resultado es $-c=a$.

Si $m$ es par, la base interior es positiva. Se puede usar la ley de potencia de potencia en esa base positiva y el valor es $c=|a|$. Este razonamiento incluye $m<0$: tomar recíprocos conserva los signos y las bases nunca son cero.

En ambos casos $a^{(m/n)(n/m)}=a^1=a$. Por tanto las dos expresiones coinciden exactamente cuando $m$ es impar. El numerador par elimina el signo en el paso interior y la potencia exterior positiva no puede recuperarlo.


### 83

Al reducir una fracción de denominador impar, sólo se divide ese denominador por un divisor suyo; el denominador reducido sigue siendo impar. Recíprocamente, si $p/q$ está reducido y $q$ es impar, la escritura $2p/(2q)$ tiene denominador par y representa exactamente el mismo racional. La paridad de una escritura arbitraria no decide pertenencia a $A$.

Si $p/q$ y $u/v$ tienen denominadores impares, la suma $(pv+uq)/(qv)$ y el producto $pu/(qv)$ también tienen denominador impar antes de reducirse. Por el primer argumento, pertenecen a $A$. Incluimos cero: su forma reducida es $0/1$.

Para $p/q\ne0$ reducido, el recíproco tiene denominador positivo $|p|$, y sigue reducido porque $\gcd(|p|,q)=1$. Pertenece a $A$ exactamente cuando $p$ es impar. Por ejemplo, $2/3\in A$, pero $3/2\notin A$; $1/3$ y tres pertenecen a $A$.

Para una base negativa fija, $A$ es exactamente el conjunto de exponentes con potencia real. Una escritura con denominador par puede representar un exponente admisible. Sumar y multiplicar exponentes admisibles mantiene la existencia de la potencia final; esto no prueba por sí solo una ley de potencias de potencias.


### 84

Escribe $a=-c$, con $c>0$. Los dos factores existen y valen $(-1)^p c^r$, $(-1)^u c^s$. Su producto es $(-1)^{p+u}c^{r+s}$.

La suma tiene la escritura $(pv+uq)/(qv)$, de denominador impar. Al reducirla sólo se cancela un divisor impar, por lo que la paridad de su numerador reducido es la de $pv+uq$, igual a la de $p+u$ porque $q,v$ son impares. La potencia final existe y tiene exactamente el signo del producto. Su valor absoluto es $c^{r+s}$, luego la igualdad es verdadera.

Si la suma es cero, la forma reducida es $0/1$ y $p+u$ es par; ambos lados valen uno. Si algún exponente es negativo, la base no es cero y el recíproco conserva la misma regla de signo. La prueba usa leyes racionales sólo en la base positiva $c$ y controla el signo aparte. Reescribir la suma con un denominador par no cambia su valor; se vuelve siempre a la fracción reducida para interpretar la potencia.


### 85

El denominador reducido tres es impar y el exponente es positivo; las tres potencias de exponente $2/3$ existen para todo real, incluido cero. Sean $u=\sqrt[3]a$ y $v=\sqrt[3]b$. Por las leyes enteras, $(uv)^3=ab$, así que $\sqrt[3]{ab}=uv$ por unicidad. Al cuadrar, $(ab)^{2/3}=u^2v^2=a^{2/3}b^{2/3}$. El dominio de ambas expresiones es todo $\mathbb R^2$.

La raíz $\sqrt{ab}$ existe cuando $ab\ge0$; el producto separado de raíces exige $a\ge0$, $b\ge0$. En el dominio común coinciden, pero sus dominios naturales son distintos. Con $a=-8$, $b=-1$, la ley de exponente $2/3$ da cuatro en ambos lados; $\sqrt{ab}=\sqrt8$ es real y las raíces cuadradas separadas no lo son. La restricción depende de la operación y del exponente, no sólo de que la base sea negativa.


### 86

Para que ambos lados sean reales se necesita $a,b\ge0$; esto garantiza también $a+b\ge0$. Si la igualdad se cumple, elevar ambos lados al cuadrado da $a+b=a+b+2\sqrt a\sqrt b$, de modo que $\sqrt a\sqrt b=0$. En los reales, un producto nulo tiene un factor nulo, por lo que $a=0$ o $b=0$.

Recíprocamente, si $a,b\ge0$ y uno es cero, la igualdad se reduce a $\sqrt b=\sqrt b$ o $\sqrt a=\sqrt a$ y es verdadera. La clasificación exacta es $a,b\ge0$ con $ab=0$.

El cuadrado se usó para obtener una condición necesaria; la suficiencia se comprobó directamente, sin resolver ecuaciones radicales por un método general. El ejemplo $a=b=1$ refuta la universalidad, pero no los casos de la clasificación. Una regla falsa en general puede ser verdadera en una familia particular que se describa y pruebe.


### 87

Ambas expresiones existen para todo $a\in\mathbb R$: la primera tiene índice impar y el radicando de la segunda es no negativo. Pon $u=\sqrt[n]a$, así que $u^n=a$. Entonces $|u|\ge0$ y $|u|^{2n}=a^2$. Por unicidad de la raíz principal, $\sqrt[2n]{a^2}=|u|=|\sqrt[n]a|$.

Las expresiones originales son iguales exactamente cuando $u\ge0$, equivalente a $a\ge0$ porque la potencia impar conserva el signo. Para $a<0$, una es negativa y la otra positiva. Por ejemplo, $\sqrt[3]{-8}=-2$ y $\sqrt[6]{64}=2$.

La reparación universal es $\sqrt[2n]{a^2}=|\sqrt[n]a|$. Igualar índices mediante un número par puede convertir una raíz con signo en una raíz principal no negativa; el dominio común por sí solo no garantiza igualdad.


### 88

La primera exige $b\ne0$ y $a/b\ge0$. Si $b>0$, esto equivale a $a\ge0$; si $b<0$, equivale a $a\le0$. El dominio es la unión de esas dos regiones, con cero permitido para $a$.

La segunda exige $a\ge0$ y $b>0$: la raíz del denominador debe existir y no anularse. En esta región ambas expresiones coinciden por la ley del cociente. Sólo existe la primera exactamente cuando $b<0$ y $a\le0$.

En esa región $-a\ge0$, $-b>0$ y $a/b=(-a)/(-b)$, por lo que $\sqrt{a/b}=\sqrt{-a}/\sqrt{-b}$. Esto incluye $a=0$, cuyo valor es cero. Las dos regiones agotan los signos posibles de un denominador no nulo. No se puede separar el cociente usando raíces de $a,b$ negativos; sí se puede cambiar simultáneamente sus signos antes de separar.


### 89

Las raíces pares exigen $t\ge0$. El denominador se anula exactamente cuando $t=1$, por la definición de raíz principal. Así, $D=[0,\infty)\setminus\{1\}$.

La presencia de los índices cuatro, seis y doce sugiere nombrar $u=\sqrt[12]t\ge0$. Entonces $u^{12}=t$, y la unicidad de las raíces principales da $\sqrt[4]t=u^3$, $\sqrt[6]t=u^2$. Para $u\ne1$, $u^3-u^2=u^2(u-1)$ por distributividad. Por tanto $R(t)=u^2=\sqrt[6]t$ en $D$; esta última identificación se verifica porque $u^2\ge0$ y $(u^2)^6=t$.

En $t=0$ la expresión original vale cero y está permitida. La forma aislada $\sqrt[6]t$ tiene valor uno en $t=1$, pero $R$ no existe allí. La cancelación conserva una función restringida al dominio original, aunque su fórmula simplificada admita una extensión.


### 90

Ambas raíces existen para $t\ge0$. Son no negativas y la primera es mayor: si fuese menor o igual, sus cuadrados también lo serían, contradiciendo $t+9>t+4$. Por ello $L(t)>0$.

El conjugado $\sqrt{t+9}+\sqrt{t+4}$ es positivo. Multiplicar y dividir por él da

$$
L(t)=\frac5{\sqrt{t+9}+\sqrt{t+4}}.
$$

Para $t\ge0$ se tiene $\sqrt{t+9}\ge3$ y $\sqrt{t+4}\ge2$, de modo que el denominador es al menos cinco. Resulta $0<L(t)\le1$. Si $t=0$, el denominador vale cinco y se alcanza uno. Si $t>0$, ambas raíces superan respectivamente tres y dos, el denominador supera cinco y la desigualdad es estricta. Así, la igualdad superior ocurre exactamente en cero.

La forma original revela una diferencia positiva; la racionalizada convierte una cota de esa diferencia en una cota sencilla de una suma. No se necesita calcular las raíces ni desarrollar una teoría general de inecuaciones.


### 91

Las raíces cúbicas existen para todos los reales. La ley del producto impar, demostrable elevando el candidato al cubo, da $P(x,y)=\sqrt[3]{x^2y^4}=\sqrt[3]{(xy^2)^2}$. Puede escribirse también $(xy^2)^{2/3}$; el denominador impar y el exponente positivo permiten cualquier signo y cero.

Después de sustituir, el radicando es $(\lambda x)^2(\lambda y)^4=\lambda^6x^2y^4$. El candidato $\lambda^2P(x,y)$ tiene cubo $\lambda^6x^2y^4$, pues $P(x,y)^3=x^2y^4$. Por unicidad de la raíz cúbica,

$$
P(\lambda x,\lambda y)=\lambda^2P(x,y).
$$

El argumento funciona para $\lambda<0$, porque el factor obtenido es $\lambda^2$, y también cuando $\lambda,x$ o $y$ son cero: ambos lados son cero. La notación de un único radical hace visible el grado total seis y permite verificar la escala sin aplicar una ley racional a una base negativa sin control.


### 92

En bases positivas, $P(x)=x^{3/4+5/6}=x^{19/12}$. Si $N$ es múltiplo positivo de doce, digamos $N=12k$, la ley de potencia de potencia da $P(x)^N=x^{19k}$, así que $(N,M)=(12k,19k)$ funciona.

Para probar necesidad, supón que la igualdad vale para todo $x>0$ y toma $x=2$. Elevando ambos lados a doce se obtiene $2^{19N}=2^{12M}$. Las potencias enteras de dos son distintas para exponentes distintos: si una diferencia positiva $h$ diera $2^h=1$, se contradiría $2^h\ge2$; para una diferencia negativa se toman recíprocos. Luego $19N=12M$. Como $\gcd(19,12)=1$, doce divide a $N$ por cancelación coprima. Escribiendo $N=12k$, se obtiene $M=19k$.

Todos los pares son los ya construidos, con $k\ge1$. El mínimo es $N=12$, con $M=19$. La fracción reducida no sólo simplifica la notación: su denominador determina cuántas repeticiones hacen desaparecer el exponente fraccionario.


### 93

Una construcción es $E(x)=\sqrt{x-a}\sqrt{b-x}/(x-c)$. Las raíces exigen $x\ge a$ y $x\le b$, y el cociente exige $x\ne c$. Estas condiciones son necesarias y suficientes, luego el dominio es exactamente $[a,b]\setminus\{c\}$. Los extremos se permiten porque la raíz del numerador puede valer cero y allí el denominador no se anula.

En ese dominio se puede reunir el producto: $E(x)=\sqrt{(x-a)(b-x)}/(x-c)$. La forma reunida tiene el mismo dominio natural. Para $a\le x\le b$, ambos factores son no negativos. Si $x<a$, el primero es negativo y el segundo positivo; si $x>b$, el primero es positivo y el segundo negativo. Por tanto el producto es no negativo exactamente en $[a,b]$. Se excluye después $c$ por el denominador.

La comparación revisa los dominios de las dos expresiones, en lugar de inferirlos de una igualdad válida sólo en un conjunto previamente fijado.


### 94

Si $k\ge1$, toma

$$
E_F(x)=\prod_{i=1}^k\frac{(x-c_i)^2}{(x-c_i)^2}.
$$

Cada cociente existe exactamente cuando $x\ne c_i$ y vale uno allí. Un producto de expresiones sólo está definido cuando cada factor lo está: el dominio es la intersección de las exclusiones, $\mathbb R\setminus F$, y el valor es uno. Si $F$ es vacío, toma directamente $E_F(x)=1$, con dominio $\mathbb R$; no hace falta imponer una convención de producto vacío.

La construcción verifica ambas direcciones. Si $x\notin F$, todos los denominadores son no nulos. Si $x\in F$, al menos un cociente contiene división por cero y la expresión no existe. La forma simplificada uno, acompañada por $x\notin F$, representa la misma función restringida; la constante uno en todos los reales sería una extensión distinta.


### 95

Escribe $F=\{c_1,\ldots,c_k\}$. Para $k\ge1$, una expresión es

$$
E(x)=\frac{\sqrt{b-x}}{\sqrt{x-a}}
\prod_{i=1}^k\frac{(x-c_i)^2}{(x-c_i)^2}.
$$

Si $F=\varnothing$, usa sólo el primer cociente. La raíz del numerador exige $x\le b$; la raíz del denominador debe ser real y no nula, por lo que exige $x>a$. Los cocientes adicionales excluyen exactamente los $c_i$. Son condiciones necesarias y suficientes: cada punto permitido define todas las operaciones y cada punto exterior incumple alguna. Por tanto el dominio es $(a,b]\setminus F$.

El extremo $b$ está incluido y produce valor cero: su denominador es $\sqrt{b-a}>0$ y ningún $c_i$ coincide con $b$. El extremo $a$ está excluido porque anula la raíz del denominador. Todos los factores adicionales valen uno en el dominio, por lo que queda la forma pedida, conservando $x\notin F$. Una raíz en el numerador y la misma raíz en el denominador imponen restricciones diferentes.


### 96

Toma $E(x)=1/\sqrt{(x-a)(x-b)}$. La raíz del denominador exige producto estrictamente positivo. Si $x<a$, ambos factores son negativos; si $a<x<b$, tienen signos opuestos; si $x>b$, ambos son positivos; en los extremos el producto es cero. Por tanto el dominio es exactamente $(-\infty,a)\cup(b,\infty)$.

La expresión separada $1/(\sqrt{x-a}\sqrt{x-b})$ exige $x-a>0$ y $x-b>0$ por sus dos raíces denominadoras; su dominio es sólo $(b,\infty)$. Coincide con $E$ allí, pero pierde toda la región izquierda.

Para $x<a$, cambia simultáneamente los signos: $(x-a)(x-b)=(a-x)(b-x)$, con ambos factores positivos. Por la ley del producto, $E(x)=1/(\sqrt{a-x}\sqrt{b-x})$ en esa región. Para $x>b$, $E(x)=1/(\sqrt{x-a}\sqrt{x-b})$. Las dos fórmulas describen todos los valores de la expresión construida; ninguna separación única usando sólo $x-a,x-b$ conserva por sí sola las dos regiones.

***
## Cierre de las soluciones

Las 96 soluciones quedan integradas con correspondencia uno a uno entre ejercicio y solución. El capítulo está ahora preparado para la auditoría QA integral: contenido matemático, dominios, metadatos, IDs internos, delimitadores, conteos y coherencia MA-PED.

***

[← Capítulo 17](algebra-para-matematicos-capitulo-17-congruencias-y-aritmetica-modular.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 19 →](algebra-para-matematicos-capitulo-19-identidades-productos-notables-y-factorizacion.md)

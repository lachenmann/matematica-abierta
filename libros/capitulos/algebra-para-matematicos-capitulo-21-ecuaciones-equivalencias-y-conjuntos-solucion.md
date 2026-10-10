---
{
  "title": "Ecuaciones, equivalencias y conjuntos solución",
  "description": "Capítulo 21 del Tomo I de Álgebra para matemáticos, con 92 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0196",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C21",
  "editorial-id": "MA-BCH-APM-01-018",
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
    "MA-BCH-0195"
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

En C20 aprendimos que una transformación algebraica debe conservar algo más que una fórmula: también debe conservar las condiciones bajo las cuales esa fórmula tenía sentido. Al pasar de expresiones a ecuaciones aparece una exigencia nueva.

Considere

$$
x^2=4.
$$

Si trabajamos con números reales, hay dos valores que hacen verdadera la igualdad:

$$
x=-2
\qquad\text{y}\qquad
x=2.
$$

Pero si el problema declara desde el comienzo que $x\ge0$, entonces sólo uno de ellos es admisible:

$$
x=2.
$$

La fórmula de la ecuación no cambió. Lo que cambió fue el conjunto en el que preguntamos por su verdad.

Este ejemplo muestra la idea que gobernará todo el capítulo:

> **Resolver una ecuación no consiste en aislar una letra. Consiste en determinar exactamente qué valores, dentro del dominio declarado, hacen verdadera la igualdad.**

A partir de ahora, cada paso de una resolución tendrá que responder una pregunta que en cursos más elementales suele permanecer oculta: **¿este paso conserva exactamente el conjunto solución, o sólo produce candidatos que después habrá que filtrar?**

## 21.1. Ecuación, dominio y conjunto solución {#apm-c21-s01}

### Una ecuación es una afirmación cuyo valor de verdad depende de la variable

Compare las expresiones

$$
2x+1
\qquad\text{y}\qquad
7.
$$

Por sí solas son expresiones. En cambio,

$$
2x+1=7
$$

es una afirmación acerca de $x$. Mientras $x$ permanezca sin fijar, no podemos asignarle simplemente el valor de verdad «verdadero» o «falso»: eso dependerá del valor que sustituyamos.

Si ponemos $x=3$, obtenemos

$$
2(3)+1=7,
$$

que es verdadera. Si ponemos $x=4$, obtenemos

$$
2(4)+1=7,
$$

que es falsa.

Diremos que una **ecuación en la variable $x$ sobre un dominio $D$** es una igualdad

$$
E(x)=F(x)
$$

donde ambos miembros están definidos para todo $x\in D$. La ecuación se interpreta entonces como una afirmación acerca de los valores de $x$ que pertenecen a ese dominio.

El dominio no es decoración. Forma parte del problema. Cuando un enunciado propone primero un dominio ambiente más amplio, las restricciones de las expresiones determinarán después el dominio efectivo sobre el que realmente se interpreta la ecuación.

### Qué significa ser solución

Un valor $a\in D$ es una **solución** de la ecuación

$$
E(x)=F(x)
$$

si, al sustituir $x=a$, ambos miembros están definidos y la igualdad resultante es verdadera.

En el ejemplo

$$
2x+1=7,
\qquad x\in\mathbb R,
$$

el número $3$ es solución porque

$$
2(3)+1=7.
$$

El número $4$ no lo es porque

$$
2(4)+1\neq7.
$$

Pero observar que $3$ funciona todavía no resuelve por completo la ecuación. Resolver exige saber si existen otros valores que también funcionen.

### El conjunto solución

Llamaremos **conjunto solución** de la ecuación $E(x)=F(x)$ sobre el dominio $D$ al conjunto

$$
\operatorname{Sol}_D(E=F)
=
\{x\in D:E(x)=F(x)\}.
$$

Esta notación convierte la tarea de resolver en un problema preciso de conjuntos: debemos describir exactamente el subconjunto de $D$ donde la igualdad es verdadera.

Para

$$
2x+1=7,
\qquad x\in\mathbb R,
$$

obtenemos

$$
\operatorname{Sol}_{\mathbb R}(2x+1=7)=\{3\}.
$$

Una solución individual es un elemento. El **conjunto solución** es el objeto completo que buscamos.

### La misma ecuación, dominios distintos

Volvamos a

$$
x^2=4.
$$

Sobre los reales,

$$
\operatorname{Sol}_{\mathbb R}(x^2=4)=\{-2,2\}.
$$

Si el dominio declarado es

$$
D=[0,\infty),
$$

entonces

$$
\operatorname{Sol}_{[0,\infty)}(x^2=4)=\{2\}.
$$

Y si el dominio fuera

$$
D=(0,2),
$$

entonces ningún valor admisible satisface la ecuación:

$$
\operatorname{Sol}_{(0,2)}(x^2=4)=\varnothing.
$$

La igualdad escrita es la misma en los tres casos. El problema de resolución no lo es.

Ésta es la primera razón por la que nunca debemos separar una ecuación del dominio sobre el que se interpreta.

### El dominio puede venir de la propia expresión

En C20 aprendimos a detectar restricciones de dominio antes de simplificar. Esa disciplina entra ahora directamente en la resolución de ecuaciones.

Considere

$$
\frac{x-1}{x-1}=1.
$$

La expresión del lado izquierdo sólo está definida cuando

$$
x-1\neq0,
$$

es decir,

$$
x\neq1.
$$

Por tanto, si no se ha declarado otro dominio ambiente, el dominio natural de la ecuación es

$$
D=\mathbb R\setminus\{1\}.
$$

Para todo $x\in D$ podemos cancelar el factor no nulo $x-1$ y obtener

$$
1=1.
$$

Eso significa que **todos los valores del dominio original** son soluciones:

$$
\operatorname{Sol}_D\left(\frac{x-1}{x-1}=1\right)
=
\mathbb R\setminus\{1\}.
$$

Sería incorrecto concluir que el conjunto solución es $\mathbb R$. La fórmula simplificada $1=1$ ya no muestra la exclusión $x=1$, pero esa exclusión pertenece al problema con el que comenzamos.

La conexión con C20 es directa:

> **Una transformación puede hacer desaparecer de la escritura una restricción sin hacer desaparecer esa restricción del problema.**

### Dominio ambiente y dominio efectivo

A veces el problema declara un conjunto en el que desea trabajar, pero las expresiones introducen restricciones adicionales.

Por ejemplo, suponga que se pide resolver

$$
\frac{1}{x-2}=3,
\qquad x\in[0,5].
$$

El dominio ambiente es $[0,5]$, pero el cociente exige además $x\neq2$. El dominio efectivo del problema es entonces

$$
D=[0,5]\setminus\{2\}.
$$

Sólo dentro de ese conjunto tiene sentido preguntar si la igualdad es verdadera o falsa.

La distinción será útil durante todo el capítulo:

- el **dominio ambiente** dice dónde queremos buscar;
- las expresiones pueden imponer restricciones adicionales;
- el **dominio efectivo** es el conjunto de valores admisibles sobre el que realmente se interpreta la ecuación.

### Una ecuación puede tener una, varias, ninguna o todas las soluciones del dominio

El lenguaje de conjuntos permite tratar de manera uniforme situaciones que, vistas sólo como «despejes», parecen muy distintas.

| Ecuación sobre $\mathbb R$ | Conjunto solución |
|---|---|
| $x+2=5$ | $\{3\}$ |
| $x^2=9$ | $\{-3,3\}$ |
| $x^2+1=0$ | $\varnothing$ |
| $x+1=x+1$ | $\mathbb R$ |

Por ahora no necesitamos clasificar sistemáticamente estas formas; eso se hará en [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05). Lo importante es observar que **resolver** siempre significa describir correctamente el conjunto que aparece en la segunda columna.

### Comprobar un valor no es resolver una ecuación

Si alguien propone $x=3$ para

$$
x^2-5x+6=0,
$$

podemos comprobar:

$$
3^2-5(3)+6=9-15+6=0.
$$

Así sabemos que $3$ es una solución.

Pero eso no demuestra que sea la única. De hecho,

$$
2^2-5(2)+6=4-10+6=0,
$$

por lo que $2$ también es solución.

La comprobación responde a la pregunta

> «¿este valor pertenece al conjunto solución?»

Resolver responde a otra más fuerte:

> «¿cuál es **todo** el conjunto solución?»

Esta diferencia será esencial cuando aparezcan transformaciones que producen candidatos adicionales.

### Un primer protocolo de lectura

Antes de manipular una ecuación, haremos tres preguntas:

1. **¿Cuál es el dominio declarado o efectivo?**
2. **¿Qué significa que un valor sea solución?**
3. **¿Qué conjunto exacto debemos determinar?**

Todavía no hemos discutido qué transformaciones pueden usarse para encontrar ese conjunto. Ése será el tema de las secciones siguientes.

### Recuperación breve

Determine el dominio efectivo y el conjunto solución de

$$
\frac{x+2}{x-3}=0,
\qquad x\in\mathbb R.
$$

**Respuesta razonada.** La expresión está definida sólo si $x-3\neq0$, por lo que

$$
D=\mathbb R\setminus\{3\}.
$$

Una fracción definida vale cero exactamente cuando su numerador vale cero. Por tanto,

$$
x+2=0,
$$

de donde

$$
x=-2.
$$

Como $-2\in D$, el valor es admisible. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R\setminus\{3\}}
\left(\frac{x+2}{x-3}=0\right)
=
\{-2\}.
}
$$

Obsérvese que $x=3$ no es una «solución que falla»: ni siquiera pertenece al dominio en el que la ecuación está definida.

### Qué debemos conservar de esta sección

Una ecuación debe leerse siempre junto con el conjunto en el que se interpreta:

> **dominio + igualdad + conjunto solución**.

El dominio determina qué valores son admisibles; la igualdad determina cuáles de ellos hacen verdadera la proposición; el conjunto solución recoge exactamente esos valores.

En [§21.2](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s02) estudiaremos la pregunta decisiva para resolver ecuaciones mediante álgebra: **¿cuándo dos ecuaciones tienen exactamente el mismo conjunto solución y cuándo una transformación conserva sólo una dirección lógica?**

## 21.2. Equivalencia de ecuaciones e implicación {#apm-c21-s02}

En [§21.1](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s01) fijamos el objeto que queremos conservar: el conjunto solución. Ahora podemos formular la pregunta que gobierna toda resolución algebraica:

> **Si reemplazamos una ecuación por otra, ¿hemos conservado exactamente sus soluciones?**

No basta con que la nueva ecuación sea más simple. Tampoco basta con que toda solución de la ecuación original siga funcionando en la nueva. Para poder sustituir una ecuación por otra sin cambiar el problema necesitamos una condición más fuerte: que ambas tengan exactamente el mismo conjunto solución sobre el mismo dominio vigente.

### Ecuaciones equivalentes

Sean dos ecuaciones definidas sobre un mismo dominio $D$:

$$
E_1(x)=F_1(x)
$$

y

$$
E_2(x)=F_2(x).
$$

Diremos que son **equivalentes sobre $D$** cuando tienen exactamente el mismo conjunto solución:

$$
\operatorname{Sol}_D(E_1=F_1)
=
\operatorname{Sol}_D(E_2=F_2).
$$

Cuando esta igualdad de conjuntos está justificada, podemos escribir

$$
E_1(x)=F_1(x)
\Longleftrightarrow
E_2(x)=F_2(x)
\qquad (x\in D).
$$

La doble flecha no significa «ahora hago el siguiente paso». Significa algo lógico preciso: si un valor de $D$ satisface la primera ecuación, también satisface la segunda, y recíprocamente. Están justificadas **ambas direcciones**.

### Un ejemplo completamente reversible

Considere

$$
3x-5=7,
\qquad x\in\mathbb R.
$$

Sumar $5$ en ambos miembros produce $3x=12$. Restar $5$ deshace exactamente ese paso. Después podemos dividir ambos miembros por $3$; como $3\neq0$, esa operación también es reversible. Por tanto,

$$
3x-5=7
\Longleftrightarrow
3x=12
\Longleftrightarrow
x=4.
$$

Cada ecuación tiene el mismo conjunto solución, $\{4\}$. Aquí la doble flecha está justificada paso por paso.

### Implicación: una sola dirección

Ahora considere $x=1$. Si elevamos ambos miembros al cuadrado obtenemos $x^2=1$. Todo valor que satisface $x=1$ satisface también $x^2=1$, de modo que

$$
x=1
\Longrightarrow
x^2=1.
$$

Pero la vuelta falla, porque $x^2=1$ tiene soluciones $\{-1,1\}$, mientras que la ecuación original sólo tiene $\{1\}$. No podemos escribir una equivalencia. En términos de conjuntos,

$$
\operatorname{Sol}_{\mathbb R}(x=1)
\subsetneq
\operatorname{Sol}_{\mathbb R}(x^2=1).
$$

La transformación creó un **candidato adicional**.

### La dirección de la flecha importa

Si

$$
E_1=F_1\Longrightarrow E_2=F_2,
$$

entonces

$$
\operatorname{Sol}_D(E_1=F_1)\subseteq\operatorname{Sol}_D(E_2=F_2).
$$

Si, en cambio, sólo sabemos

$$
E_1=F_1\Longleftarrow E_2=F_2,
$$

entonces

$$
\operatorname{Sol}_D(E_2=F_2)\subseteq\operatorname{Sol}_D(E_1=F_1).
$$

La orientación de la flecha registra así qué conjunto puede contener al otro.

### Cómo se puede perder una solución

Considere

$$
x(x-2)=0.
$$

Su conjunto solución es $\{0,2\}$. Si dividimos ambos miembros por $x$, obtenemos $x-2=0$, cuya única solución es $2$. El paso no es reversible porque dividir por $x$ exige $x\neq0$, y $x=0$ era precisamente una solución original.

No es correcto escribir

$$
x(x-2)=0\Longleftrightarrow x-2=0.
$$

Sí es cierto, en cambio, que

$$
x-2=0\Longrightarrow x(x-2)=0.
$$

En términos de conjuntos, $\{2\}\subsetneq\{0,2\}$. La operación no creó candidatos: **borró una solución**.

### Dos fallas diferentes

Conviene separar dos fenómenos:

1. una transformación puede **crear candidatos adicionales**;
2. una transformación puede **perder soluciones originales**.

Elevar al cuadrado suele ilustrar el primer peligro. Dividir por una expresión que puede anularse ilustra el segundo. En el primer caso, una comprobación final puede filtrar candidatos extraños. En el segundo, comprobar lo que sobrevivió no recupera automáticamente lo que ya fue eliminado. Por eso debemos controlar la lógica durante la transformación y no sólo al final.

### La equivalencia depende también del dominio

Volvamos a

$$
\frac{x-1}{x-1}=1.
$$

Sobre el dominio efectivo $D=\mathbb R\setminus\{1\}$, podemos escribir

$$
\frac{x-1}{x-1}=1
\Longleftrightarrow
1=1
\qquad (x\in D),
$$

porque dentro de $D$ el factor $x-1$ nunca es cero. Sería incorrecto reinterpretar la ecuación de la derecha sobre todo $\mathbb R$ y reinsertar $x=1$. La equivalencia se afirmó **sobre $D$**.

### Una cadena mixta

Considere

$$
\sqrt{x+1}=x-1.
$$

No la resolveremos todavía; eso corresponde a [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11). Pero si elevamos ambos miembros al cuadrado, la flecha segura es

$$
\sqrt{x+1}=x-1
\Longrightarrow
x+1=(x-1)^2.
$$

Al cuadrar podemos perder información de signo y generar candidatos. Más adelante veremos cómo añadir condiciones de admisibilidad para recuperar una equivalencia exacta.

### Un protocolo para leer cadenas de resolución

En cada transición preguntaremos:

1. **¿la transformación es reversible sobre el dominio vigente?**
2. **si lo es, puedo escribir $\Longleftrightarrow$?**
3. **si sólo conservo una dirección, cuál es la flecha correcta?**
4. **el nuevo conjunto es igual, mayor o menor que el anterior?**
5. **aparecieron candidatos o pudieron perderse soluciones?**

### Recuperación breve

Clasifique cada transición sobre $\mathbb R$.

**a)** $x+4=9\to x=5$.

**b)** $x=3\to x^2=9$.

**c)** $x(x+1)=0\to x+1=0$, obtenida dividiendo por $x$.

**Respuesta razonada.** En **a)** restar $4$ es reversible, por lo que

$$
x+4=9\Longleftrightarrow x=5.
$$

En **b)** se conserva sólo una dirección:

$$
x=3\Longrightarrow x^2=9,
$$

porque la ecuación cuadrada también admite $x=-3$.

En **c)** la ecuación original tiene soluciones $\{-1,0\}$, mientras que la transformada sólo conserva $-1$; la dirección segura es

$$
x+1=0\Longrightarrow x(x+1)=0.
$$

### Qué debemos conservar de esta sección

La fuerza lógica de una transformación se lee en su efecto sobre el conjunto solución:

> **equivalencia = mismo conjunto solución; implicación = inclusión en una sola dirección.**

La doble flecha $\Longleftrightarrow$ exige reversibilidad sobre el dominio vigente. Una flecha simple puede señalar candidatos adicionales o soluciones perdidas, según su orientación.

En [§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03) estudiaremos sistemáticamente qué operaciones aplicadas a ambos miembros son reversibles y qué hipótesis —en especial la no nulidad— permiten escribir una equivalencia.

## 21.3. Operaciones reversibles en ambos miembros {#apm-c21-s03}

En [§21.2](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s02) vimos que una doble flecha sólo está justificada cuando el paso conserva exactamente el conjunto solución. Ahora podemos estudiar las operaciones que usamos con más frecuencia al resolver ecuaciones y preguntar, para cada una:

> **¿qué hipótesis hacen que aplicar la misma operación a ambos miembros sea realmente reversible?**

La respuesta tiene dos capas. Primero, todas las expresiones nuevas deben estar definidas sobre el dominio vigente. Segundo, cuando aparece una multiplicación o una división, debemos controlar además si el factor puede valer cero.

### Sumar la misma expresión

Suponga que, sobre un dominio $D$, tenemos la ecuación

$$
A(x)=B(x),
$$

y que $G(x)$ está definida para todo $x\in D$. Entonces

$$
A(x)=B(x)
\Longleftrightarrow
A(x)+G(x)=B(x)+G(x)
\qquad (x\in D).
$$

La razón es simple pero importante: si sumamos $G$ podemos deshacer el paso restando exactamente la misma expresión. No hay una condición de no nulidad.

Por ejemplo,

$$
2x-7=5
\Longleftrightarrow
2x=12,
$$

porque se sumó $7$ a ambos miembros y la operación inversa consiste en restar $7$.

Lo mismo vale para restar una expresión definida en todo el dominio, ya que restar $G$ equivale a sumar $-G$.

### La condición de definida no debe olvidarse

La frase «sumar lo mismo en ambos miembros» no autoriza a introducir una expresión que no esté definida en todo el dominio vigente.

Considere, sobre $D=\mathbb R$,

$$
x=2.
$$

Si intentáramos sumar $1/(x-1)$ a ambos miembros, obtendríamos una nueva escritura que ni siquiera está definida en $x=1$. Aunque $x=1$ no sea solución de la ecuación original, hemos cambiado el dominio de la ecuación transformada.

Por eso, la regla correcta no es simplemente «se puede sumar lo mismo». Es:

> **se puede sumar o restar la misma expresión siempre que esa expresión esté definida en todo el dominio sobre el que afirmamos la equivalencia.**

### Multiplicar por una constante no nula

Si $c$ es una constante real con $c\neq0$, entonces

$$
A=B
\Longleftrightarrow
cA=cB.
$$

La vuelta se obtiene dividiendo por $c$, operación permitida porque $c$ no es cero.

Por ejemplo,

$$
\frac{x}{3}=4
\Longleftrightarrow
x=12.
$$

Aquí hemos multiplicado ambos miembros por $3$, y el paso es reversible porque $3\neq0$.

¿Qué ocurre si multiplicamos por $0$? Toda ecuación se transforma en

$$
0=0,
$$

que es verdadera para todos los valores del dominio. La información sobre el conjunto solución desaparece por completo. Ésta es la primera señal de que la multiplicación necesita una hipótesis adicional que la suma no requería.

### Multiplicar por una expresión variable

Sea ahora $M(x)$ una expresión definida sobre $D$. Siempre se cumple la implicación

$$
A(x)=B(x)
\Longrightarrow
A(x)M(x)=B(x)M(x).
$$

Pero para poder escribir la equivalencia

$$
A(x)=B(x)
\Longleftrightarrow
A(x)M(x)=B(x)M(x),
$$

una condición suficiente que garantiza la reversibilidad para cualquier ecuación es

$$
M(x)\neq0
\qquad\text{para todo }x\in D.
$$

Para una ecuación concreta, esta condición no es necesaria: si todos los ceros de $M$ ya satisfacen $A=B$, multiplicar no añade soluciones. En efecto, la ecuación multiplicada equivale a $M=0$ o $A=B$, por el producto nulo. Así, su conjunto solución es la unión de las soluciones originales con los ceros de $M$ en $D$. El ejercicio 87 examina precisamente esa excepción.

Si $M$ puede anularse, la ecuación multiplicada puede adquirir soluciones nuevas precisamente en los ceros de $M$.

Por ejemplo,

$$
x=2
$$

tiene conjunto solución $\{2\}$. Multiplicando ambos miembros por $x$ obtenemos

$$
x^2=2x,
$$

es decir,

$$
x(x-2)=0,
$$

cuyo conjunto solución es $\{0,2\}$. El cero apareció porque el factor por el que multiplicamos podía anularse.

Así,

$$
x=2
\Longrightarrow
x^2=2x,
$$

pero no hay equivalencia sobre $\mathbb R$.

### El dominio puede convertir un factor variable en un factor seguro

Que $M(x)$ dependa de $x$ no es, por sí solo, un problema. Lo decisivo es si puede valer cero en el dominio vigente.

Considere

$$
\frac{1}{x-2}=3.
$$

Su dominio efectivo es

$$
D=\mathbb R\setminus\{2\}.
$$

Dentro de $D$, el factor $x-2$ está garantizado como no nulo. Por eso podemos multiplicar ambos miembros por $x-2$ y escribir legítimamente

$$
\frac{1}{x-2}=3
\Longleftrightarrow
1=3(x-2)
\qquad (x\in D).
$$

La operación es reversible **sobre ese dominio**. La misma multiplicación no podría declararse automáticamente reversible sobre todo $\mathbb R$, porque en $x=2$ el factor se anula y, además, la ecuación original ni siquiera está definida.

### Dividir por una expresión

Dividir por $M(x)$ equivale a multiplicar por su recíproco. Por tanto, la operación sólo tiene sentido donde

$$
M(x)\neq0.
$$

Si sabemos que $M$ es no nula en todo el dominio $D$, entonces

$$
A=B
\Longleftrightarrow
\frac{A}{M}=\frac{B}{M}
\qquad (x\in D).
$$

Pero si $M$ puede anularse en una solución original, dividir sin separar ese caso puede borrar soluciones.

Por ejemplo,

$$
x(x+3)=2x
$$

se puede escribir como

$$
x(x+1)=0,
$$

de modo que sus soluciones son $x=0$ y $x=-1$.

Si dividimos desde el comienzo por $x$, obtenemos

$$
x+3=2,
$$

y sólo recuperamos $x=-1$. La solución $x=0$ desapareció porque la división no estaba autorizada allí.

La dirección segura es

$$
x+3=2
\Longrightarrow
x(x+3)=2x,
$$

no una equivalencia sobre todo $\mathbb R$.

### Dividir exige una decisión previa

Cuando aparece un factor variable que quisiéramos cancelar o usar como divisor, debemos decidir antes entre dos situaciones:

1. **sabemos que el factor es no nulo en todo el dominio vigente**: podemos dividir y conservar equivalencia;
2. **el factor puede valer cero**: debemos separar el caso $M(x)=0$ antes de dividir, o usar otra ruta que no lo elimine.

Este principio aparecerá repetidamente en ecuaciones factorizadas, racionales, paramétricas y sistemas.

### Una forma general de recordar las reglas

Sobre un dominio $D$ donde todas las expresiones involucradas están definidas:

- sumar o restar la misma expresión preserva equivalencia;
- multiplicar por una expresión $M$ preserva equivalencia si $M\neq0$ en todo $D$;
- dividir por $M$ preserva equivalencia si $M\neq0$ en todo $D$;
- si $M$ puede anularse, multiplicar puede crear candidatos y dividir puede perder soluciones.

La asimetría de los dos últimos casos es importante. Multiplicar por cero destruye información porque varias igualdades distintas pueden convertirse en la misma igualdad. Dividir por una expresión que vale cero en una solución descarta directamente ese caso.

### Recuperación breve

Clasifique cada transformación sobre el dominio indicado.

**a)** Sobre $\mathbb R$,

$$
x-5=8
\quad\longrightarrow\quad
x=13,
$$

sumando $5$ a ambos miembros.

**b)** Sobre $\mathbb R$,

$$
x=3
\quad\longrightarrow\quad
x^2=3x,
$$

multiplicando por $x$.

**c)** Sobre $D=\mathbb R\setminus\{4\}$,

$$
\frac{2}{x-4}=5
\quad\longrightarrow\quad
2=5(x-4),
$$

multiplicando por $x-4$.

**Respuesta razonada.** En **a)** sumar $5$ es reversible y no introduce restricciones nuevas, por lo que

$$
x-5=8\Longleftrightarrow x=13.
$$

En **b)** el factor $x$ puede valer cero. La ecuación original tiene solución $\{3\}$, mientras que $x^2=3x$ tiene soluciones $\{0,3\}$. Por tanto,

$$
x=3\Longrightarrow x^2=3x,
$$

pero no hay equivalencia sobre $\mathbb R$.

En **c)** el dominio ya excluye $x=4$, así que $x-4\neq0$ en todo $D$. La multiplicación es reversible sobre ese dominio:

$$
\frac{2}{x-4}=5
\Longleftrightarrow
2=5(x-4)
\qquad (x\in D).
$$

### Qué debemos conservar de esta sección

Las operaciones sobre ambos miembros no se justifican por una regla gráfica de «hacer lo mismo a ambos lados». Se justifican porque son reversibles bajo hipótesis precisas.

> **Sumar o restar exige que la expresión añadida esté definida; multiplicar o dividir exige además controlar la no nulidad del factor.**

La condición $M(x)\neq0$ es lo que permite recuperar la ecuación anterior y, por tanto, conservar exactamente el conjunto solución.

En [§21.4](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s04) estudiaremos qué ocurre cuando esas hipótesis fallan y aprenderemos a localizar con precisión la primera transformación que crea candidatos o pierde soluciones.

## 21.4. Transformaciones que crean o pierden candidatos {#apm-c21-s04}

En [§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03) identificamos las hipótesis que hacen reversibles las operaciones más comunes. Ahora estudiaremos el caso complementario: **qué ocurre cuando usamos una transformación sin disponer de esas hipótesis**.

La pregunta cambia ligeramente. Ya no preguntaremos sólo

> **¿la transformación es correcta como cálculo?**

sino, de manera más precisa,

> **¿qué ocurrió con el conjunto solución en el primer paso que dejó de ser reversible?**

Ésta será nuestra idea de **primera ruptura**. Una cadena puede contener muchos pasos algebraicamente impecables después de una transición no equivalente. Si el conjunto solución ya cambió en esa transición, los pasos posteriores no reparan por sí solos la pérdida de información.

### Tres comportamientos posibles

Suponga que una ecuación $E_0$ se transforma en otra $E_1$ sobre un dominio $D$.

Pueden ocurrir tres situaciones:

1. **equivalencia**:
   $$
   \operatorname{Sol}_D(E_0)=\operatorname{Sol}_D(E_1);
   $$
2. **creación de candidatos**:
   $$
   \operatorname{Sol}_D(E_0)\subsetneq\operatorname{Sol}_D(E_1);
   $$
3. **pérdida de soluciones**:
   $$
   \operatorname{Sol}_D(E_1)\subsetneq\operatorname{Sol}_D(E_0).
   $$

En el primer caso podemos escribir $\Longleftrightarrow$. En el segundo, la dirección segura es $E_0\Longrightarrow E_1$. En el tercero, la dirección segura es $E_1\Longrightarrow E_0$.

La dificultad práctica consiste en reconocer **qué operación produjo la inclusión estricta**.

### Multiplicar por un factor que puede anularse: aparecen candidatos

Considere, sobre $\mathbb R$,

$$
2x=6.
$$

Su conjunto solución es

$$
\{3\}.
$$

Multipliquemos ambos miembros por $x-4$:

$$
2x(x-4)=6(x-4).
$$

Toda solución de la ecuación original satisface la nueva, de modo que

$$
2x=6
\Longrightarrow
2x(x-4)=6(x-4).
$$

Pero la ecuación transformada se puede escribir como

$$
2(x-4)(x-3)=0,
$$

y entonces admite

$$
x=3
\qquad\text{o}\qquad
x=4.
$$

El valor $4$ no apareció por un error de expansión ni por una factorización incorrecta. Apareció porque, cuando $x=4$, el factor multiplicativo $x-4$ convierte **ambos miembros** en cero, aunque la igualdad original $2x=6$ sea falsa.

Por tanto,

$$
\{3\}\subsetneq\{3,4\}.
$$

La primera ruptura fue exactamente la multiplicación por un factor que podía anularse.

### Dividir por un factor que puede anularse: desaparecen soluciones

Ahora considere

$$
(x-1)(x+2)=0.
$$

Por la propiedad del producto nulo, su conjunto solución es

$$
\{-2,1\}.
$$

Si dividimos por $x-1$, obtenemos

$$
x+2=0,
$$

cuya única solución es

$$
-2.
$$

El valor $x=1$ no se volvió falso. Fue eliminado porque la división por $x-1$ no estaba definida precisamente en ese valor.

Así,

$$
\{-2\}\subsetneq\{-2,1\}.
$$

La dirección segura es

$$
x+2=0
\Longrightarrow
(x-1)(x+2)=0,
$$

pero no la equivalencia.

Este fenómeno es más peligroso que la mera aparición de un candidato extra: **una comprobación final de los valores que sobrevivieron no recupera una solución que ya fue borrada de la cadena**.

### Elevar al cuadrado: una transformación que puede borrar el signo

Considere la ecuación

$$
x+1=-1.
$$

Su única solución es

$$
x=-2.
$$

Si elevamos ambos miembros al cuadrado,

$$
(x+1)^2=1.
$$

La ecuación cuadrada admite

$$
x+1=1
\qquad\text{o}\qquad
x+1=-1,
$$

es decir,

$$
x=0
\qquad\text{o}\qquad
x=-2.
$$

Por tanto,

$$
\{-2\}\subsetneq\{-2,0\}.
$$

El cuadrado no recuerda si antes de elevar ambos miembros éstos eran iguales o eran opuestos. Por eso, en general,

$$
A=B
\Longrightarrow
A^2=B^2,
$$

pero no podemos invertir la flecha sin información adicional.

En [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11) aplicaremos esta idea a ecuaciones radicales. Aquí sólo necesitamos identificar la estructura lógica: **elevar al cuadrado puede ampliar el conjunto de candidatos porque destruye información de signo**.

### Un candidato extra no es lo mismo que un valor excluido por dominio

Considere

$$
\frac{x+1}{x-2}=0.
$$

El dominio efectivo excluye desde el principio $x=2$. Si al eliminar denominadores apareciera después el número $2$ como raíz de alguna ecuación auxiliar, ese valor no sería una solución «creada» por la transformación en el mismo sentido que el $4$ del ejemplo anterior: $2$ **nunca fue admisible en el problema original**.

Conviene mantener separados los dos diagnósticos:

- **candidato extraño por transformación**: pertenece al dominio original, pero aparece sólo después de una implicación no reversible;
- **valor inadmisible por dominio**: nunca perteneció al conjunto donde se interpretaba la ecuación original.

En ambos casos el valor debe descartarse, pero la causa lógica es distinta.

### La primera ruptura en una cadena larga

Considere la cadena

$$
x=2
\Longrightarrow
x^2=2x
\Longleftrightarrow
x^2-2x=0
\Longleftrightarrow
x(x-2)=0.
$$

Los dos últimos pasos son equivalencias: restar $2x$ y factorizar no cambian el conjunto solución de la ecuación que reciben.

Sin embargo, la ecuación final tiene soluciones

$$
\{0,2\},
$$

mientras que la inicial sólo tenía

$$
\{2\}.
$$

¿Dónde nació $x=0$? No en la factorización. No al pasar todos los términos a un miembro. La primera ruptura fue

$$
x=2
\Longrightarrow
x^2=2x,
$$

obtenida al multiplicar por $x$, que podía valer cero.

Este modo de leer una cadena será fundamental en el laboratorio de errores de [§21.15](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s15):

> **cuando el resultado final contiene una solución incorrecta o falta una solución correcta, busque la primera transición donde dejó de haber equivalencia.**

### Filtrar candidatos cuando sólo hemos avanzado por implicación

Si una cadena tiene la forma

$$
E_0
\Longrightarrow
E_1
\Longleftrightarrow
E_2
\Longleftrightarrow
\cdots
\Longleftrightarrow
E_n,
$$

las soluciones de $E_n$ son, en principio, **candidatos** para $E_0$. La primera flecha sólo garantiza

$$
\operatorname{Sol}(E_0)\subseteq\operatorname{Sol}(E_n).
$$

Para decidir cuáles candidatos pertenecen realmente al conjunto solución original debemos volver a $E_0$ o utilizar condiciones de admisibilidad equivalentes que hayamos conservado.

Esto justifica la comprobación final en ecuaciones donde hubo pasos sólo implicativos.

### Por qué verificar al final no basta para todo

La verificación final es muy poderosa para eliminar candidatos adicionales. Si una transformación amplió el conjunto, probar cada candidato en la ecuación original permite distinguir cuáles sobreviven.

Pero no resuelve el problema opuesto.

Si una transformación perdió una solución, esa solución ya no aparece entre los candidatos finales. Verificar los valores restantes no puede advertirnos automáticamente de que falta uno.

Por eso la disciplina correcta tiene dos niveles:

1. **durante la cadena**, controlar la fuerza lógica de cada paso;
2. **al final**, verificar los candidatos cuando hubo alguna transformación sólo implicativa.

La verificación complementa el control lógico; no lo sustituye.

### Una tabla de diagnóstico

| Transformación | Efecto posible | Señal lógica |
|---|---|---|
| operación reversible bajo sus hipótesis | conserva exactamente | $\Longleftrightarrow$ |
| multiplicar por factor que puede ser cero | añade candidatos | $\Longrightarrow$ desde la original |
| dividir por factor que puede ser cero | pierde soluciones | $\Longleftarrow$ desde la original |
| elevar al cuadrado | puede añadir candidatos | $\Longrightarrow$ desde la original |
| olvidar una restricción de dominio | admite valores que nunca fueron válidos | cambio indebido del dominio |

Esta tabla no sustituye el análisis del caso concreto. Sirve para saber **qué pregunta hacer** cuando una cadena parece sospechosa.

### Recuperación breve

En cada cadena, localice la primera ruptura de equivalencia y describa su efecto sobre el conjunto solución.

**a)**

$$
x=5
\Longrightarrow
x(x-5)=0
\Longleftrightarrow
x=0\ \text{o}\ x=5.
$$

**b)**

$$
(x+1)(x-3)=0
\longrightarrow
x-3=0,
$$

donde la flecha se obtuvo dividiendo por $x+1$.

**c)**

$$
x-2=-2
\Longrightarrow
(x-2)^2=4
\Longleftrightarrow
x-2=2\ \text{o}\ x-2=-2.
$$

**Respuesta razonada.** En **a)** la ruptura está en la primera transición: multiplicar la ecuación $x=5$ por $x$ permite que $x=0$ satisfaga la ecuación transformada. El conjunto pasa de $\{5\}$ a $\{0,5\}$.

En **b)** la ecuación original tiene soluciones $\{-1,3\}$. Dividir por $x+1$ elimina $x=-1$, por lo que la transformada conserva sólo $\{3\}$. La ruptura es una pérdida de solución.

En **c)** la ecuación original tiene solución $\{0\}$. Al cuadrar obtenemos $(x-2)^2=4$, cuyas soluciones son $\{0,4\}$. El nuevo valor $4$ es un candidato adicional creado por la pérdida de información de signo.

### Qué debemos conservar de esta sección

Cuando una resolución deja de ser una cadena de equivalencias, debemos saber **cómo** cambió el conjunto solución.

> **Crear candidatos y perder soluciones son fallas lógicas distintas, y ambas pueden localizarse buscando la primera ruptura de equivalencia.**

Si una transformación sólo amplía el conjunto, los resultados finales deben tratarse como candidatos y filtrarse. Si una transformación reduce el conjunto, una comprobación final de los sobrevivientes no basta: debemos volver al paso donde se perdió información.

En [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05) aplicaremos esta disciplina a las ecuaciones lineales, incluidas identidades, contradicciones y casos degenerados sencillos.



### La comprobación filtra; la cobertura conserva

Si una ecuación original tiene soluciones $S$ y una transformación produce candidatos $T$ con $S\subseteq T$, comprobar todos los elementos de $T$ en la original puede recuperar exactamente $S$. Si, en cambio, se perdió una parte de $S$, comprobar los sobrevivientes solo prueba que son soluciones. **Control resuelto:** dividir $(x-a)(x-b)=0$ por $x-a$ entrega $x=b$ donde la división existe, pero no examina $x=a$. Debemos separar primero $x=a$ y $x\ne a$; en la primera rama el producto es cero, y en la segunda obtenemos $x=b$, sujeto a la rama. Si $a=b$, la segunda rama no aporta nada y la primera da la única solución. Comprobar un resultado y demostrar que no falta ninguno son obligaciones diferentes.

## 21.5. Ecuaciones lineales, identidades y contradicciones {#apm-c21-s05}

Hasta ahora hemos estudiado la lógica de las transformaciones sin concentrarnos en una familia particular de ecuaciones. Podemos aplicar ahora esa disciplina al caso más elemental y, precisamente por eso, más importante para fijar hábitos correctos: las ecuaciones lineales.

La pregunta de esta sección no será sólo «¿cómo despejo $x$?», sino una más completa:

> **¿qué conjunto solución puede producir una ecuación lineal una vez que todas las transformaciones equivalentes han sido realizadas?**

La respuesta incluye tres posibilidades fundamentales: una única solución, ninguna solución o todos los valores del dominio.

### La forma lineal básica

Consideremos, sobre un dominio $D\subseteq\mathbb R$, una ecuación de la forma

$$
ax+b=c,
$$

donde $a$, $b$ y $c$ son constantes reales.

Restar $b$ en ambos miembros es una transformación reversible, de modo que

$$
ax+b=c
\Longleftrightarrow
ax=c-b.
$$

Es natural querer dividir inmediatamente por $a$. Pero [§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03) nos obliga a formular antes la pregunta correcta:

> **¿sabemos que $a\neq0$?**

Si la respuesta es sí, podemos dividir por $a$ y conservar equivalencia. Si la respuesta es no, debemos separar casos.

### Caso 1: el coeficiente de la variable es no nulo

Supongamos primero que

$$
a\neq0.
$$

Entonces

$$
ax=c-b
\Longleftrightarrow
x=\frac{c-b}{a}.
$$

Si trabajamos sobre $D=\mathbb R$, el conjunto solución es el singleton

$$
\left\{\frac{c-b}{a}\right\}.
$$

Sobre un dominio general $D$, todavía hay que comprobar que el valor obtenido pertenece a $D$. Por tanto,

$$
\operatorname{Sol}_D(ax+b=c)
=
\begin{cases}
\left\{\dfrac{c-b}{a}\right\}, & \text{si } \dfrac{c-b}{a}\in D,\\[6pt]
\varnothing, & \text{si } \dfrac{c-b}{a}\notin D.
\end{cases}
$$

Incluso una ecuación lineal puede quedar sin solución si el dominio declarado excluye el único valor algebraicamente posible.

### Un ejemplo con una solución única

Resolvamos

$$
5x-7=2x+8
$$

sobre $\mathbb R$.

Restamos $2x$ en ambos miembros:

$$
5x-7=2x+8
\Longleftrightarrow
3x-7=8.
$$

Sumamos $7$:

$$
3x-7=8
\Longleftrightarrow
3x=15.
$$

Como $3\neq0$, dividimos por $3$:

$$
3x=15
\Longleftrightarrow
x=5.
$$

Cada paso fue reversible, por lo que

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(5x-7=2x+8)=\{5\}.
}
$$

Aquí el procedimiento habitual de «reunir las $x$ a un lado y las constantes al otro» funciona porque, detrás de cada movimiento, hay operaciones reversibles ya justificadas.

### El dominio puede eliminar la única solución algebraica

Considere ahora

$$
2x=6,
\qquad x\in[0,2].
$$

Algebraicamente,

$$
2x=6
\Longleftrightarrow
x=3.
$$

Pero $3\notin[0,2]$. Por tanto,

$$
\boxed{
\operatorname{Sol}_{[0,2]}(2x=6)=\varnothing.
}
$$

No hay contradicción entre «la ecuación da $x=3$» y «el conjunto solución es vacío». La primera frase identifica el único candidato producido por el álgebra; la segunda incorpora además el dominio del problema.

### Caso 2: el coeficiente de la variable se anula

Supongamos ahora que

$$
a=0.
$$

La ecuación

$$
ax+b=c
$$

se reduce a

$$
b=c.
$$

La variable ha desaparecido. Ya no estamos ante una condición que seleccione un valor particular de $x$, sino ante una proposición constante.

Pueden ocurrir dos cosas.

Si

$$
b=c,
$$

la igualdad es verdadera para **todo** $x\in D$. Entonces

$$
\operatorname{Sol}_D(0x+b=b)=D.
$$

Si, en cambio,

$$
b\neq c,
$$

la igualdad es falsa para **todo** $x\in D$. Entonces

$$
\operatorname{Sol}_D(0x+b=c)=\varnothing.
$$

Ésta es la razón por la que no se debe dividir por el coeficiente de $x$ antes de saber que ese coeficiente es distinto de cero.

### Identidad sobre el dominio

Considere

$$
3(x-2)=3x-6.
$$

Al desarrollar el lado izquierdo obtenemos

$$
3x-6=3x-6.
$$

Restando $3x$ y sumando $6$ en ambos miembros llegamos a

$$
0=0.
$$

No hemos «perdido la variable por accidente». Hemos descubierto que la igualdad es verdadera para todo número real. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}\bigl(3(x-2)=3x-6\bigr)=\mathbb R.
}
$$

Diremos que la ecuación es una **identidad sobre el dominio considerado**: todos los valores admisibles la satisfacen.

Si el dominio hubiera sido un subconjunto $D\subseteq\mathbb R$, el conjunto solución sería exactamente $D$, no necesariamente todo $\mathbb R$.

### Contradicción sobre el dominio

Considere ahora

$$
2(x+1)=2x+5.
$$

Desarrollamos:

$$
2x+2=2x+5.
$$

Restamos $2x$ en ambos miembros:

$$
2=5.
$$

La proposición final es falsa. Ningún valor de $x$ puede hacer verdadera la ecuación original, porque todas las transformaciones utilizadas fueron equivalencias. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}\bigl(2(x+1)=2x+5\bigr)=\varnothing.
}
$$

Diremos que la ecuación es una **contradicción sobre el dominio considerado**.

### Tres resultados posibles después de reducir una ecuación lineal

Una ecuación lineal con la variable en ambos miembros puede escribirse, después de transformaciones equivalentes, en la forma

$$
ax=b.
$$

Sobre un dominio $D$, la clasificación completa es:

| Condición | Forma final | Conjunto solución |
|---|---|---|
| $a\neq0$ | $x=b/a$ | $\{b/a\}$ si $b/a\in D$; en otro caso $\varnothing$ |
| $a=0$ y $b=0$ | $0=0$ | $D$ |
| $a=0$ y $b\neq0$ | $0=b$ | $\varnothing$ |

Esta tabla contiene más información que la receta «despejar $x$». En particular, explica por qué algunas ecuaciones lineales no tienen una única solución.

### Variable en ambos miembros

Consideremos la forma más general

$$
ax+b=cx+d.
$$

Restar $cx$ y luego $b$ produce

$$
ax+b=cx+d
\Longleftrightarrow
(a-c)x=d-b.
$$

La clasificación depende ahora del coeficiente

$$
a-c.
$$

Si $a-c\neq0$, obtenemos una única solución algebraica:

$$
x=\frac{d-b}{a-c}.
$$

Si $a-c=0$, la variable desaparece y debemos comparar $d-b$ con cero:

- si $d-b=0$, la ecuación es verdadera para todo el dominio;
- si $d-b\neq0$, no hay soluciones.

El punto lógico es el mismo que antes. La desaparición de la variable no es un error: es información sobre la relación entre los dos miembros.

### Un contraste muy cercano

Compare las ecuaciones

$$
4x+3=4x+3
$$

y

$$
4x+3=4x+5.
$$

En ambas desaparece $x$ al restar $4x$. Pero las conclusiones son opuestas:

$$
4x+3=4x+3
\Longleftrightarrow
3=3,
$$

por lo que todas las $x$ del dominio son soluciones; mientras que

$$
4x+3=4x+5
\Longleftrightarrow
3=5,
$$

por lo que ninguna lo es.

La expresión «se canceló la $x$» no basta para diagnosticar el problema. Hay que leer la proposición constante que queda.

### Un primer caso degenerado con parámetro

Los parámetros se estudiarán sistemáticamente en [§21.13](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s13). Aquí basta un ejemplo mínimo para mostrar por qué la separación de casos es obligatoria.

Considere

$$
(a-1)x=2(a-1)
$$

sobre $\mathbb R$.

Si $a\neq1$, entonces $a-1\neq0$ y podemos dividir:

$$
(a-1)x=2(a-1)
\Longleftrightarrow
x=2.
$$

Por tanto,

$$
\operatorname{Sol}_{\mathbb R}=\{2\}.
$$

Pero si $a=1$, la ecuación se convierte en

$$
0=0,
$$

y entonces

$$
\operatorname{Sol}_{\mathbb R}=\mathbb R.
$$

Dividir inmediatamente por $a-1$ habría borrado por completo el caso $a=1$. Éste es exactamente el tipo de pérdida que aprendimos a detectar en §[§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03)–21.4.

### No toda desaparición de la variable significa lo mismo

Después de simplificar una ecuación lineal pueden aparecer escrituras como

$$
0=0,
\qquad
0=7,
\qquad
0x=0,
\qquad
0x=7.
$$

Las dos primeras parejas expresan la misma distinción:

- una proposición verdadera independiente de $x$;
- una proposición falsa independiente de $x$.

Por eso, ante una ecuación lineal, la pregunta final no es simplemente «¿quedó $x$ aislada?». Es:

> **¿qué proposición equivalente quedó y qué conjunto de valores del dominio la satisface?**

### Un protocolo para ecuaciones lineales

Podemos resumir el procedimiento sin convertirlo en una receta ciega:

1. fijar el dominio vigente;
2. usar sólo transformaciones equivalentes para reunir los términos con $x$ y las constantes;
3. reducir a una forma $ax=b$;
4. preguntar si $a$ es cero;
5. si $a\neq0$, dividir y comprobar que el valor obtenido pertenece al dominio;
6. si $a=0$, decidir si la proposición restante es verdadera o falsa;
7. declarar explícitamente el conjunto solución.

Este protocolo evita dos errores frecuentes: dividir por un coeficiente que podría ser cero y confundir una identidad con una «ecuación sin respuesta».

### Recuperación breve

Determine el conjunto solución sobre $\mathbb R$ en cada caso.

**a)**

$$
7x+4=2x+19.
$$

**b)**

$$
5(x-2)=5x-10.
$$

**c)**

$$
4(x+1)=4x+7.
$$

**Respuesta razonada.** En **a)**,

$$
7x+4=2x+19
\Longleftrightarrow
5x=15
\Longleftrightarrow
x=3,
$$

por lo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{3\}.}
$$

En **b)**,

$$
5(x-2)=5x-10
\Longleftrightarrow
5x-10=5x-10
\Longleftrightarrow
0=0.
$$

La igualdad es verdadera para todo real, así que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\mathbb R.}
$$

En **c)**,

$$
4(x+1)=4x+7
\Longleftrightarrow
4x+4=4x+7
\Longleftrightarrow
4=7.
$$

La igualdad es falsa para todo real, de modo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\varnothing.}
$$

### Qué debemos conservar de esta sección

Una ecuación lineal no siempre produce «un valor de $x$». Después de transformaciones equivalentes puede quedar una ecuación con coeficiente no nulo, una identidad o una contradicción.

> **La forma $ax=b$ debe leerse por casos: si $a\neq0$, hay a lo sumo una solución; si $a=0$, la ecuación puede ser verdadera para todo el dominio o falsa para todo el dominio.**

La obligación de separar el caso $a=0$ no es una precaución técnica menor: evita dividir por cero y perder familias completas de soluciones.

En [§21.6](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s06) estudiaremos ecuaciones cuya estructura multiplicativa permite reemplazar una igualdad por una disyunción de casos mediante la propiedad del producto nulo.

## 21.6. Producto nulo y ecuaciones factorizadas {#apm-c21-s06}

En [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05) vimos que una ecuación puede resolverse reduciéndola mediante transformaciones equivalentes hasta una forma sencilla. Ahora estudiaremos una estructura diferente: una ecuación cuyo lado izquierdo aparece como un **producto** y cuyo lado derecho es cero.

La forma básica es

$$
A(x)B(x)=0.
$$

Aquí no necesitamos dividir por ninguno de los factores. En cambio, podemos usar una propiedad elemental de los números reales que transforma una sola ecuación en una **disyunción de casos**.

### La propiedad del producto nulo

Para números reales $u$ y $v$,

$$
uv=0
\Longleftrightarrow
u=0\ \text{o}\ v=0.
$$

Aplicada a expresiones definidas sobre un dominio $D$, esta propiedad da

$$
A(x)B(x)=0
\Longleftrightarrow
A(x)=0\ \text{o}\ B(x)=0.
$$

La doble flecha es importante. No estamos produciendo candidatos adicionales: estamos describiendo exactamente cuándo el producto vale cero.

En términos de conjuntos solución,

$$
\operatorname{Sol}_D(AB=0)
=
\operatorname{Sol}_D(A=0)
\cup
\operatorname{Sol}_D(B=0).
$$

Resolver una ecuación factorizada consiste, por tanto, en resolver cada factor igualado a cero y **unir** los conjuntos obtenidos.

### Un primer ejemplo

Resolvamos

$$
(x-4)(2x+3)=0
$$

sobre $\mathbb R$.

Por producto nulo,

$$
(x-4)(2x+3)=0
\Longleftrightarrow
x-4=0\ \text{o}\ 2x+3=0.
$$

De la primera rama obtenemos

$$
x=4,
$$

y de la segunda,

$$
x=-\frac32.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl((x-4)(2x+3)=0\bigr)
=
\left\{-\frac32,4\right\}.
}
$$

El conjunto final es la unión de las soluciones de las dos ramas.

### Factorizar puede revelar la estructura lógica

Considere ahora

$$
x^2-5x+6=0.
$$

Tal como vimos en C19,

$$
x^2-5x+6=(x-2)(x-3).
$$

La factorización es una identidad algebraica, de modo que reemplazar el polinomio por su forma factorizada no cambia el conjunto solución:

$$
x^2-5x+6=0
\Longleftrightarrow
(x-2)(x-3)=0.
$$

Ahora la propiedad del producto nulo produce

$$
(x-2)(x-3)=0
\Longleftrightarrow
x-2=0\ \text{o}\ x-3=0.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2-5x+6=0)=\{2,3\}.
}
$$

La factorización no es aquí sólo una reescritura conveniente. **Hace visible una disyunción que estaba escondida en la forma expandida.**

### Primero llevar la ecuación a cero

La propiedad del producto nulo se aplica a una igualdad de la forma

$$
\text{producto}=0.
$$

Por eso, ante

$$
x^2=5x-6,
$$

no podemos factorizar cada miembro por separado y declarar casos. Primero llevamos todos los términos a un miembro mediante una transformación equivalente:

$$
x^2=5x-6
\Longleftrightarrow
x^2-5x+6=0.
$$

Después factorizamos:

$$
x^2-5x+6=0
\Longleftrightarrow
(x-2)(x-3)=0,
$$

y recién entonces usamos el producto nulo.

La secuencia lógica es

$$
\text{ecuación}
\Longleftrightarrow
\text{expresión}=0
\Longleftrightarrow
\text{producto}=0
\Longleftrightarrow
\text{disyunción de factores nulos}.
$$

### No se debe dividir por un factor

Considere nuevamente

$$
(x-1)(x+2)=0.
$$

El producto nulo da inmediatamente

$$
x=1\ \text{o}\ x=-2.
$$

Si, en cambio, dividimos por $x-1$, obtenemos sólo

$$
x+2=0,
$$

y perdemos la solución $x=1$.

La razón ya fue estudiada en §[§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03)–21.4: el factor $x-1$ puede ser cero precisamente en una solución de la ecuación.

Por eso, cuando tenemos

$$
A(x)B(x)=0,
$$

la propiedad del producto nulo es estructuralmente superior a cancelar un factor. **La disyunción conserva todas las ramas; la división puede borrar una de ellas.**

### Más de dos factores

La propiedad se extiende a cualquier producto finito. Sobre los reales,

$$
A_1A_2\cdots A_n=0
\Longleftrightarrow
A_1=0\ \text{o}\ A_2=0\ \text{o}\ \cdots\ \text{o}\ A_n=0.
$$

Por ejemplo,

$$
x(x-2)(x+5)=0
$$

es equivalente a

$$
x=0
\quad\text{o}\quad
x=2
\quad\text{o}\quad
x=-5.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(x(x-2)(x+5)=0\bigr)
=
\{-5,0,2\}.
}
$$

En términos de conjuntos, cada factor aporta una posible rama y el conjunto solución final es la unión de todas ellas.

### Factores repetidos no crean soluciones nuevas

Considere

$$
(x-2)^2(x+1)=0.
$$

Podemos leerlo como

$$
(x-2)(x-2)(x+1)=0.
$$

El producto nulo produce las ramas

$$
x-2=0,
\qquad
x-2=0,
\qquad
x+1=0.
$$

Las dos primeras son la misma condición. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl((x-2)^2(x+1)=0\bigr)
=
\{-1,2\}.
}
$$

Que un factor aparezca repetido puede ser algebraicamente relevante en otros contextos, pero **no duplica un elemento del conjunto solución**.

### El dominio sigue gobernando la respuesta

La propiedad del producto nulo identifica qué valores hacen cero el producto, pero sólo los valores pertenecientes al dominio vigente pueden ser soluciones.

Por ejemplo, sobre

$$
D=[0,\infty),
$$

la ecuación

$$
(x+2)(x-3)=0
$$

produce algebraicamente los valores

$$
x=-2
\qquad\text{y}\qquad
x=3.
$$

Pero $-2\notin D$. Así,

$$
\boxed{
\operatorname{Sol}_{[0,\infty)}
\bigl((x+2)(x-3)=0\bigr)
=
\{3\}.
}
$$

La factorización y el producto nulo no suspenden la disciplina de dominio establecida desde [§21.1](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s01).

### La propiedad no se aplica a una suma

Una confusión frecuente consiste en intentar convertir

$$
A(x)+B(x)=0
$$

en

$$
A(x)=0\ \text{o}\ B(x)=0.
$$

Eso es falso en general.

Por ejemplo,

$$
x+(2-x)=0
$$

se reduce a

$$
2=0,
$$

por lo que no tiene soluciones. Sin embargo, las ecuaciones separadas

$$
x=0
\qquad\text{o}\qquad
2-x=0
$$

producirían los valores $0$ y $2$, que no satisfacen la ecuación original.

La estructura decisiva no es «hay dos términos». Es específicamente

$$
\boxed{\text{producto}=0}.
$$

### Factorizar antes de resolver las ramas

Considere

$$
2x^2+7x+3=0.
$$

Buscamos primero una factorización:

$$
2x^2+7x+3=(2x+1)(x+3).
$$

Entonces

$$
2x^2+7x+3=0
\Longleftrightarrow
(2x+1)(x+3)=0
$$

y, por producto nulo,

$$
2x+1=0
\quad\text{o}\quad
x+3=0.
$$

De aquí,

$$
x=-\frac12
\quad\text{o}\quad
x=-3.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(2x^2+7x+3=0)
=
\left\{-3,-\frac12\right\}.
}
$$

La dificultad de esta ruta reside en encontrar la factorización. Una vez que el producto está visible, la lógica de resolución está completamente determinada.

### Una lectura conjuntista de la factorización

Si

$$
P(x)=A(x)B(x),
$$

entonces resolver

$$
P(x)=0
$$

sobre $D$ equivale a resolver las dos ramas

$$
A(x)=0,
\qquad
B(x)=0,
$$

y formar

$$
\operatorname{Sol}_D(P=0)
=
\operatorname{Sol}_D(A=0)
\cup
\operatorname{Sol}_D(B=0).
$$

Esta perspectiva explica por qué la factorización es tan poderosa para ecuaciones: transforma una condición global en una unión de condiciones más simples.

También explica por qué cancelar un factor es conceptualmente peligroso. Cancelar sustituye una **unión de ramas** por una sola de ellas.

### Un protocolo para ecuaciones factorizables

Cuando una ecuación parece resoluble por factorización, seguiremos esta secuencia:

1. fijar el dominio vigente;
2. transformar equivaléntemente la ecuación hasta obtener una expresión igual a cero;
3. factorizar usando identidades válidas;
4. aplicar la propiedad del producto nulo;
5. resolver cada rama por separado;
6. unir las soluciones obtenidas;
7. intersectar con el dominio si es necesario;
8. declarar explícitamente el conjunto solución.

Este protocolo evita dos errores distintos: aplicar producto nulo a una expresión que no es un producto igualado a cero y dividir por un factor que puede representar una solución.

### Recuperación breve

Determine el conjunto solución sobre $\mathbb R$.

**a)**

$$
(x+4)(x-1)=0.
$$

**b)**

$$
x^2+x-6=0.
$$

**c)**

$$
x^2(x-5)=0.
$$

**Respuesta razonada.** En **a)**,

$$
(x+4)(x-1)=0
\Longleftrightarrow
x+4=0\ \text{o}\ x-1=0,
$$

por lo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-4,1\}.}
$$

En **b)** factorizamos

$$
x^2+x-6=(x+3)(x-2),
$$

de modo que

$$
(x+3)(x-2)=0
\Longleftrightarrow
x=-3\ \text{o}\ x=2.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-3,2\}.}
$$

En **c)**,

$$
x^2(x-5)=0
\Longleftrightarrow
x^2=0\ \text{o}\ x-5=0.
$$

La primera rama da $x=0$ y la segunda $x=5$. Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{0,5\}.}
$$

El factor $x^2$ no hace que $0$ aparezca dos veces en el conjunto solución.

### Qué debemos conservar de esta sección

La propiedad del producto nulo convierte una ecuación factorizada en una disyunción exacta de casos:

$$
AB=0
\Longleftrightarrow
A=0\ \text{o}\ B=0.
$$

En términos de conjuntos,

$$
\boxed{
\operatorname{Sol}(AB=0)
=
\operatorname{Sol}(A=0)\cup\operatorname{Sol}(B=0).
}
$$

> **Factorizar hace visible la unión de ramas; dividir por un factor puede borrar una de ellas.**

En [§21.7](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s07) usaremos esta estructura para resolver ecuaciones cuadráticas por factorización y la compararemos con otra transformación equivalente fundamental: completar cuadrados.

## 21.7. Ecuaciones cuadráticas por factorización y completar cuadrados {#apm-c21-s07}

En [§21.6](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s06) vimos que una ecuación factorizada puede resolverse separando ramas mediante la propiedad del producto nulo. Las ecuaciones cuadráticas ofrecen ahora un primer contexto en el que **la misma ecuación puede admitir más de una ruta de resolución**.

Una ecuación cuadrática sobre los reales tiene la forma

$$
ax^2+bx+c=0,
$$

con

$$
a\neq0.
$$

La condición $a\neq0$ no es accesoria: si $a=0$, la ecuación deja de ser cuadrática y vuelve al caso lineal estudiado en [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05).

En esta sección compararemos dos rutas:

1. **factorizar**, cuando la estructura puede reconocerse con facilidad;
2. **completar cuadrados**, cuando conviene transformar la expresión en una forma

$$
(x-h)^2=k.
$$

Las dos rutas deben producir el mismo conjunto solución porque ambas se construyen mediante transformaciones equivalentes.

### Primera ruta: factorizar

Considere

$$
x^2-5x+6=0.
$$

Reconocemos la factorización

$$
x^2-5x+6=(x-2)(x-3).
$$

Por tanto,

$$
x^2-5x+6=0
\Longleftrightarrow
(x-2)(x-3)=0.
$$

Aplicando producto nulo,

$$
(x-2)(x-3)=0
\Longleftrightarrow
x-2=0\ \text{o}\ x-3=0.
$$

Así,

$$
x=2
\qquad\text{o}\qquad
x=3,
$$

y

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2-5x+6=0)=\{2,3\}.
}
$$

Aquí la factorización es la ruta natural porque la estructura multiplicativa aparece de inmediato.

### Una condición previa que no debe omitirse

La propiedad del producto nulo sólo puede aplicarse cuando el producto está igualado a cero.

Por ejemplo,

$$
x^2-5x=6
$$

no autoriza escribir directamente

$$
x(x-5)=0.
$$

Primero debemos obtener una ecuación equivalente con cero en uno de los miembros:

$$
x^2-5x=6
\Longleftrightarrow
x^2-5x-6=0.
$$

Ahora sí podemos factorizar:

$$
x^2-5x-6=(x-6)(x+1),
$$

y concluir

$$
x=6
\qquad\text{o}\qquad
x=-1.
$$

La secuencia correcta es entonces

$$
\text{ecuación}
\longrightarrow
\text{cero en un miembro}
\longrightarrow
\text{factorización}
\longrightarrow
\text{producto nulo}.
$$

### Segunda ruta: construir un cuadrado perfecto

No toda cuadrática revela de inmediato una factorización conveniente. Una segunda posibilidad es **completar el cuadrado**.

La identidad fundamental es

$$
x^2+px
=
\left(x+\frac{p}{2}\right)^2
-
\left(\frac{p}{2}\right)^2.
$$

La razón se obtiene expandiendo:

$$
\left(x+\frac{p}{2}\right)^2
=
x^2+px+\frac{p^2}{4}.
$$

Por tanto, para convertir $x^2+px$ en un cuadrado perfecto debemos añadir

$$
\left(\frac{p}{2}\right)^2.
$$

Cuando estamos dentro de una ecuación, ese término debe añadirse **a ambos miembros**, de modo que la transformación siga siendo reversible.

### Completar cuadrados paso a paso

Resolvamos

$$
x^2+6x-7=0.
$$

Primero aislamos los términos que contienen $x$:

$$
x^2+6x=7.
$$

La mitad de $6$ es $3$, y

$$
3^2=9.
$$

Sumamos $9$ en ambos miembros:

$$
x^2+6x+9=16.
$$

El lado izquierdo es ahora un cuadrado perfecto:

$$
(x+3)^2=16.
$$

Hasta aquí todos los pasos fueron equivalencias. Sobre los reales,

$$
(x+3)^2=16
\Longleftrightarrow
x+3=4\ \text{o}\ x+3=-4.
$$

Por tanto,

$$
x=1
\qquad\text{o}\qquad
x=-7.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2+6x-7=0)=\{-7,1\}.
}
$$

Completar cuadrados no consiste en «inventar» un término. Consiste en añadir exactamente la cantidad que convierte el trinomio en el cuadrado de un binomio, compensándola en el otro miembro para conservar equivalencia.

### El paso desde un cuadrado hasta sus raíces

Cuando alcanzamos una ecuación de la forma

$$
U(x)^2=k,
$$

debemos distinguir el signo de $k$ si trabajamos sobre $\mathbb R$.

Si $k>0$,

$$
U(x)^2=k
\Longleftrightarrow
U(x)=\sqrt{k}\ \text{o}\ U(x)=-\sqrt{k}.
$$

Si $k=0$,

$$
U(x)^2=0
\Longleftrightarrow
U(x)=0.
$$

Si $k<0$, no existen soluciones reales, porque el cuadrado de un número real nunca es negativo.

Este paso no es la misma operación lógica que elevar al cuadrado estudiada en [§21.4](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s04). Aquí partimos de una igualdad ya escrita como $U^2=k$ y describimos exactamente todos los reales que la satisfacen.

### Un ejemplo que no factoriza de manera inmediata sobre los enteros

Considere

$$
x^2+4x-1=0.
$$

Podríamos buscar una factorización real, pero no es visible con coeficientes enteros sencillos. Completar cuadrados da una ruta directa:

$$
x^2+4x=1.
$$

Añadimos $4$ a ambos miembros:

$$
x^2+4x+4=5.
$$

Entonces

$$
(x+2)^2=5.
$$

Por tanto,

$$
x+2=\sqrt5
\qquad\text{o}\qquad
x+2=-\sqrt5,
$$

y finalmente

$$
x=-2+\sqrt5
\qquad\text{o}\qquad
x=-2-\sqrt5.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2+4x-1=0)
=
\{-2-\sqrt5,\,-2+\sqrt5\}.
}
$$

Este ejemplo muestra una ventaja estratégica: completar cuadrados no depende de que podamos reconocer de antemano factores simples.

### Si el coeficiente principal no es uno

Considere

$$
2x^2+8x-10=0.
$$

Como el coeficiente principal es $2\neq0$, podemos dividir toda la ecuación por $2$:

$$
2x^2+8x-10=0
\Longleftrightarrow
x^2+4x-5=0.
$$

Ahora completamos cuadrados:

$$
x^2+4x=5,
$$

$$
x^2+4x+4=9,
$$

$$
(x+2)^2=9.
$$

Luego,

$$
x+2=3
\qquad\text{o}\qquad
x+2=-3,
$$

de donde

$$
x=1
\qquad\text{o}\qquad
x=-5.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(2x^2+8x-10=0)=\{-5,1\}.
}
$$

Dividir primero por el coeficiente principal no es una maniobra automática aplicable a cualquier expresión simbólica: aquí está justificada porque, por definición de ecuación cuadrática, $a\neq0$.

### La misma ecuación por dos rutas

Consideremos

$$
x^2-6x+5=0.
$$

**Ruta A: factorización.**

$$
x^2-6x+5
=
(x-1)(x-5),
$$

de modo que

$$
(x-1)(x-5)=0
\Longleftrightarrow
x=1\ \text{o}\ x=5.
$$

**Ruta B: completar cuadrados.**

$$
x^2-6x=-5.
$$

Añadimos $9$:

$$
x^2-6x+9=4,
$$

por lo que

$$
(x-3)^2=4.
$$

Entonces

$$
x-3=2
\qquad\text{o}\qquad
x-3=-2,
$$

y nuevamente

$$
x=5
\qquad\text{o}\qquad
x=1.
$$

Ambas rutas producen

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\{1,5\}.
}
$$

No son dos respuestas distintas. Son dos representaciones de la misma estructura y, por tanto, dos cadenas equivalentes que deben terminar en el mismo conjunto solución.

### Qué ruta conviene elegir

No existe una regla que obligue a resolver toda cuadrática de una sola manera.

La factorización suele ser preferible cuando:

- los factores se reconocen con rapidez;
- el producto nulo deja visibles inmediatamente las ramas;
- la ecuación ya viene parcialmente factorizada.

Completar cuadrados suele ser preferible cuando:

- la factorización simple no es evidente;
- queremos construir una forma $(x-h)^2=k$;
- necesitamos hacer visible la estructura de cuadrado perfecto.

En ambos casos la pregunta estratégica es la misma:

> **¿qué representación hace más visible la estructura que permite resolver sin perder ni añadir soluciones?**

### Completar cuadrados como transformación general

La identidad

$$
x^2+px
=
\left(x+\frac p2\right)^2
-
\frac{p^2}{4}
$$

permite reescribir cualquier expresión cuadrática mónico-lineal de la forma

$$
x^2+px+q
$$

como

$$
\left(x+\frac p2\right)^2
+
q-\frac{p^2}{4}.
$$

Ésta es una identidad algebraica, no una operación que cambie el conjunto solución.

Cuando la usamos dentro de una ecuación, podemos mover después la constante al otro miembro mediante operaciones reversibles y llegar a una forma

$$
\left(x+\frac p2\right)^2=k.
$$

En [§21.8](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s08) aplicaremos este mecanismo a la cuadrática general y veremos cómo de él emerge la fórmula cuadrática.

### Un caso sin soluciones reales, sin usar todavía el discriminante

Considere

$$
x^2+2x+5=0.
$$

Completando cuadrados,

$$
x^2+2x=-5,
$$

$$
x^2+2x+1=-4,
$$

y por tanto

$$
(x+1)^2=-4.
$$

Sobre $\mathbb R$ esto es imposible. Luego,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2+2x+5=0)=\varnothing.
}
$$

No necesitamos todavía una fórmula ni un criterio basado en el discriminante para justificar esta conclusión: basta la propiedad elemental de que un cuadrado real es siempre no negativo.

En [§21.8](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s08) organizaremos sistemáticamente este fenómeno mediante una expresión que permitirá clasificar las soluciones reales de cualquier cuadrática.

### Protocolo para elegir y justificar una ruta

Ante una ecuación cuadrática elemental:

1. fijar el dominio;
2. llevar la ecuación a una forma equivalente con cero en un miembro si queremos factorizar;
3. buscar primero una estructura visible;
4. si factorizamos, aplicar producto nulo y unir las ramas;
5. si completamos cuadrados, añadir la misma cantidad a ambos miembros hasta construir $(x-h)^2=k$;
6. resolver exactamente la ecuación cuadrada resultante;
7. intersectar con el dominio cuando corresponda;
8. declarar el conjunto solución;
9. si se comparan dos rutas, comprobar que ambas terminan en el mismo conjunto.

### Recuperación breve

Resuelva sobre $\mathbb R$ usando la ruta indicada.

**a) Factorización**

$$
x^2+x-12=0.
$$

**b) Completar cuadrados**

$$
x^2-8x+7=0.
$$

**c) Elija la ruta que considere más eficiente**

$$
x^2+2x-8=0.
$$

**Respuesta razonada.** En **a)**,

$$
x^2+x-12=(x+4)(x-3),
$$

por lo que

$$
(x+4)(x-3)=0
\Longleftrightarrow
x=-4\ \text{o}\ x=3.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-4,3\}.}
$$

En **b)**,

$$
x^2-8x=-7.
$$

Añadimos $16$:

$$
x^2-8x+16=9,
$$

de modo que

$$
(x-4)^2=9.
$$

Por tanto,

$$
x-4=3
\qquad\text{o}\qquad
x-4=-3,
$$

y

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{1,7\}.}
$$

En **c)** la factorización es inmediata:

$$
x^2+2x-8=(x+4)(x-2),
$$

de modo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-4,2\}.}
$$

Completar cuadrados también sería correcto, pero aquí requiere más pasos. La elección de ruta no cambia la solución; cambia la eficiencia y la visibilidad de la estructura.

### Qué debemos conservar de esta sección

Las ecuaciones cuadráticas pueden admitir varias rutas equivalentes.

> **Factorizar explota una estructura multiplicativa ya visible; completar cuadrados construye deliberadamente una estructura de cuadrado perfecto.**

La factorización conduce al producto nulo y a una unión de ramas. Completar cuadrados conduce a una ecuación de la forma $(x-h)^2=k$, que puede resolverse exactamente sobre los reales.

Ninguna de las dos rutas debe tratarse como una receta opaca. Cada transformación debe conservar el conjunto solución y cada elección debe justificarse por la estructura que hace visible.

En [§21.8](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s08) derivaremos la fórmula cuadrática a partir de completar cuadrados y usaremos el discriminante para clasificar sistemáticamente el número de soluciones reales.

## 21.8. Fórmula cuadrática y discriminante real {#apm-c21-s08}

En [§21.7](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s07) vimos que completar cuadrados transforma una ecuación cuadrática en una ecuación de la forma $(x-h)^2=k$. Podemos aplicar ahora esa misma idea a la cuadrática general y obtener, sin memorizar una regla externa, una fórmula que resuelve todos los casos reales.

Partimos de

$$
ax^2+bx+c=0,
$$

con

$$
a\neq0.
$$

La condición $a\neq0$ pertenece a la definición misma de ecuación cuadrática. También es exactamente la hipótesis que permitirá dividir por $a$ durante la derivación.

### Derivación desde completar cuadrados

Dividimos toda la ecuación por $a$:

$$
x^2+\frac{b}{a}x+\frac{c}{a}=0.
$$

Movemos el término constante al segundo miembro:

$$
x^2+\frac{b}{a}x=-\frac{c}{a}.
$$

Para completar el cuadrado, tomamos la mitad del coeficiente de $x$:

$$
\frac12\frac{b}{a}=\frac{b}{2a},
$$

y añadimos su cuadrado a ambos miembros:

$$
x^2+\frac{b}{a}x+\frac{b^2}{4a^2}
=
-\frac{c}{a}+\frac{b^2}{4a^2}.
$$

El primer miembro es

$$
\left(x+\frac{b}{2a}\right)^2.
$$

En el segundo miembro usamos denominador común $4a^2$:

$$
-\frac{c}{a}
+
\frac{b^2}{4a^2}
=
\frac{-4ac+b^2}{4a^2}.
$$

Por tanto,

$$
\left(x+\frac{b}{2a}\right)^2
=
\frac{b^2-4ac}{4a^2}.
$$

Esta igualdad es el punto estructural de toda la derivación. La cantidad

$$
b^2-4ac
$$

no aparece por convención: surge exactamente como el numerador que queda después de completar cuadrados en la cuadrática general.

### Del cuadrado a la fórmula

Supongamos primero que el lado derecho es no negativo, de modo que existen raíces cuadradas reales. Entonces

$$
\left|x+\frac{b}{2a}\right|
=
\frac{\sqrt{b^2-4ac}}{2|a|}.
$$

Para mantener la forma algebraica habitual resulta más cómodo volver a la equivalencia

$$
U^2=K
\Longleftrightarrow
U=\sqrt K\ \text{o}\ U=-\sqrt K,
$$

cuando $K\ge0$. Aplicada a nuestra ecuación,

$$
x+\frac{b}{2a}
=
\pm\frac{\sqrt{b^2-4ac}}{2a}.
$$

La notación $\pm$ permite reemplazar el denominador $2|a|$ por $2a$: cuando $a<0$, ese reemplazo sólo intercambia las dos ramas de la misma ecuación. No estamos cambiando el coeficiente $a$ de la ecuación original.

Restando $b/(2a)$ obtenemos

$$
\boxed{
x=
\frac{-b\pm\sqrt{b^2-4ac}}{2a}
}.
$$

Ésta es la **fórmula cuadrática**. No es una receta independiente de [§21.7](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s07): es el resultado de completar cuadrados una vez en forma general.

### El discriminante

Definimos

$$
\boxed{\Delta=b^2-4ac}.
$$

La expresión $\Delta$ se llama **discriminante** porque discrimina, sobre los números reales, qué tipo de conjunto solución puede tener la cuadrática.

La ecuación obtenida al completar cuadrados puede escribirse como

$$
\left(x+\frac{b}{2a}\right)^2
=
\frac{\Delta}{4a^2}.
$$

Como $a\neq0$, tenemos $4a^2>0$. Por tanto, el signo del lado derecho depende exclusivamente del signo de $\Delta$.

### Caso $\Delta>0$: dos soluciones reales distintas

Si

$$
\Delta>0,
$$

entonces

$$
\sqrt{\Delta}>0.
$$

Las dos ramas

$$
x=
\frac{-b+\sqrt\Delta}{2a}
$$

y

$$
x=
\frac{-b-\sqrt\Delta}{2a}
$$

son distintas. En consecuencia, la ecuación tiene dos soluciones reales distintas.

Por ejemplo,

$$
x^2-5x+6=0.
$$

Aquí

$$
a=1,
\qquad
b=-5,
\qquad
c=6,
$$

y

$$
\Delta=(-5)^2-4(1)(6)=25-24=1>0.
$$

La fórmula da

$$
x=\frac{5\pm1}{2},
$$

de donde

$$
x=3
\qquad\text{o}\qquad
x=2.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2-5x+6=0)=\{2,3\}.
}
$$

Coincide, como debe, con la factorización usada en §[§21.6](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s06)–21.7.

### Caso $\Delta=0$: una única solución real

Si

$$
\Delta=0,
$$

las dos ramas de la fórmula coinciden:

$$
x=
\frac{-b\pm0}{2a}
=
-\frac{b}{2a}.
$$

El conjunto solución contiene un solo elemento:

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac{b}{2a}\right\}.
}
$$

En lenguaje algebraico suele decirse que existe una **raíz real doble**. La palabra «doble» describe la multiplicidad algebraica, no significa que el conjunto solución contenga el mismo número dos veces.

Por ejemplo,

$$
x^2-6x+9=0.
$$

Tenemos

$$
\Delta=(-6)^2-4(1)(9)=36-36=0,
$$

y

$$
x=\frac{6}{2}=3.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2-6x+9=0)=\{3\}.
}
$$

Esto coincide con la forma

$$
(x-3)^2=0.
$$

### Caso $\Delta<0$: no hay soluciones reales

Si

$$
\Delta<0,
$$

entonces

$$
\frac{\Delta}{4a^2}<0.
$$

Pero un cuadrado real no puede ser negativo. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(ax^2+bx+c=0)=\varnothing.
}
$$

Por ejemplo,

$$
x^2+2x+5=0
$$

tiene

$$
\Delta=2^2-4(1)(5)=4-20=-16<0.
$$

Así, no tiene soluciones reales.

En C21 detenemos aquí el análisis. La ecuación sí podrá estudiarse en un dominio más amplio, pero las soluciones complejas de cuadráticas con $\Delta<0$ pertenecen a C25.

### La clasificación real completa

Para

$$
ax^2+bx+c=0,
\qquad a\neq0,
$$

la clasificación sobre $\mathbb R$ es:

| Discriminante | Soluciones reales | Conjunto solución |
|---|---|---|
| $\Delta>0$ | dos distintas | $\left\{\dfrac{-b-\sqrt\Delta}{2a},\dfrac{-b+\sqrt\Delta}{2a}\right\}$ |
| $\Delta=0$ | una raíz doble | $\left\{-\dfrac{b}{2a}\right\}$ |
| $\Delta<0$ | ninguna | $\varnothing$ |

Esta tabla no reemplaza la derivación: la resume. La razón de los tres casos está en la ecuación cuadrada

$$
\left(x+\frac{b}{2a}\right)^2
=
\frac{\Delta}{4a^2}.
$$

### La fórmula no elimina la elección estratégica

Disponer de una fórmula general no significa que deba usarse siempre.

Considere

$$
x^2-7x+12=0.
$$

La fórmula funciona. Sin embargo, la factorización

$$
x^2-7x+12=(x-3)(x-4)
$$

hace visible inmediatamente el conjunto solución

$$
\{3,4\}.
$$

En cambio, para

$$
3x^2+2x-7=0,
$$

la factorización elemental no es evidente. La fórmula da directamente

$$
\Delta=2^2-4(3)(-7)=4+84=88,
$$

y

$$
x=\frac{-2\pm\sqrt{88}}{6}
=
\frac{-2\pm2\sqrt{22}}{6}
=
\frac{-1\pm\sqrt{22}}{3}.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(3x^2+2x-7=0)
=
\left\{
\frac{-1-\sqrt{22}}{3},
\frac{-1+\sqrt{22}}{3}
\right\}.
}
$$

La fórmula es universal; la elección de usarla sigue siendo estratégica.

### El dominio puede filtrar soluciones de la fórmula

La fórmula determina las soluciones reales de la ecuación cuadrática como igualdad algebraica. Si el problema impone un dominio más pequeño, debemos conservar únicamente las soluciones que pertenezcan a ese dominio.

Por ejemplo,

$$
x^2-5x+6=0,
\qquad x\in[0,2].
$$

La ecuación tiene raíces reales $2$ y $3$, pero sólo $2$ pertenece al dominio declarado. Por tanto,

$$
\boxed{
\operatorname{Sol}_{[0,2]}(x^2-5x+6=0)=\{2\}.
}
$$

Ni la fórmula cuadrática ni el discriminante suspenden la disciplina de dominio establecida en [§21.1](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s01).

### No olvidar la hipótesis $a\neq0$

La expresión

$$
\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

sólo tiene sentido como fórmula cuadrática cuando

$$
a\neq0.
$$

Si $a=0$, la ecuación

$$
ax^2+bx+c=0
$$

se reduce a una ecuación lineal o a un caso degenerado de [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05). Aplicar la fórmula sin separar este caso introduciría una división por cero.

La condición $a\neq0$ no es una nota al pie: es una hipótesis estructural de la fórmula.

### Comprobación mediante relaciones entre las raíces

Cuando $\Delta\ge0$, las raíces dadas por la fórmula son

$$
x_1=\frac{-b+\sqrt\Delta}{2a},
\qquad
x_2=\frac{-b-\sqrt\Delta}{2a}.
$$

Sumando,

$$
x_1+x_2
=
\frac{-2b}{2a}
=
-\frac{b}{a},
$$

y multiplicando,

$$
x_1x_2
=
\frac{b^2-\Delta}{4a^2}
=
\frac{b^2-(b^2-4ac)}{4a^2}
=
\frac{c}{a}.
$$

Estas relaciones sirven como control estructural de una resolución:

$$
\boxed{
x_1+x_2=-\frac ba,
\qquad
x_1x_2=\frac ca.
}
$$

No sustituyen la resolución, pero permiten detectar errores de signo o de simplificación.

### Un protocolo para usar la fórmula con sentido

Ante una cuadrática general:

1. escribirla en la forma $ax^2+bx+c=0$;
2. comprobar que $a\neq0$;
3. identificar correctamente $a$, $b$ y $c$, incluidos sus signos;
4. calcular $\Delta=b^2-4ac$;
5. clasificar primero el caso real según el signo de $\Delta$;
6. si $\Delta\ge0$, aplicar la fórmula cuadrática;
7. simplificar radicales cuando corresponda;
8. intersectar con el dominio declarado;
9. declarar explícitamente el conjunto solución;
10. cuando sea útil, verificar suma y producto de raíces.

El orden importa: calcular primero $\Delta$ permite saber qué tipo de respuesta real debemos esperar antes de manipular la raíz cuadrada.

### Recuperación breve

Resuelva sobre $\mathbb R$ usando la fórmula cuadrática y clasifique cada caso mediante el discriminante.

**a)**

$$
2x^2-5x-3=0.
$$

**b)**

$$
4x^2+4x+1=0.
$$

**c)**

$$
2x^2+2x+5=0.
$$

**Respuesta razonada.** En **a)**,

$$
a=2,
\qquad
b=-5,
\qquad
c=-3,
$$

y

$$
\Delta=25-4(2)(-3)=49>0.
$$

Por tanto,

$$
x=\frac{5\pm7}{4},
$$

de donde

$$
x=3
\qquad\text{o}\qquad
x=-\frac12.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac12,3\right\}.
}
$$

En **b)**,

$$
\Delta=4^2-4(4)(1)=16-16=0.
$$

Hay una única solución real:

$$
x=\frac{-4}{8}=-\frac12.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\left\{-\frac12\right\}.
}
$$

En **c)**,

$$
\Delta=2^2-4(2)(5)=4-40=-36<0.
$$

Luego no existen soluciones reales:

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\varnothing.
}
$$

### Qué debemos conservar de esta sección

La fórmula cuadrática no aparece por magia: se obtiene completando cuadrados en

$$
ax^2+bx+c=0,
\qquad a\neq0.
$$

La cantidad

$$
\Delta=b^2-4ac
$$

surge durante esa derivación y controla la existencia de raíces reales.

> **Sobre $\mathbb R$: $\Delta>0$ produce dos soluciones distintas, $\Delta=0$ una única solución real y $\Delta<0$ ninguna solución real.**

La fórmula es una herramienta universal, pero no vuelve innecesarias la elección de representación, la atención al dominio ni la comprobación de hipótesis.

En [§21.9](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s09) estudiaremos ecuaciones que no parecen cuadráticas en la variable original, pero que pueden reducirse a una cuadrática mediante una sustitución adecuada.

## 21.9. Sustituciones y ecuaciones cuadráticas en forma {#apm-c21-s09}

Hasta ahora hemos resuelto ecuaciones que eran lineales o cuadráticas de manera visible. Sin embargo, una ecuación puede tener grado mayor y conservar, escondida dentro de su escritura, una estructura cuadrática.

Considere

$$
x^4-5x^2+4=0.
$$

No es cuadrática en $x$, pero sí lo es en la expresión $x^2$. Si introducimos

$$
u=x^2,
$$

entonces

$$
x^4=(x^2)^2=u^2,
$$

y la ecuación se convierte en

$$
u^2-5u+4=0.
$$

La sustitución ha comprimido la estructura. Pero todavía no hemos resuelto la ecuación original: sólo hemos resuelto una ecuación auxiliar en una variable nueva.

La pregunta decisiva de esta sección será:

> **¿qué valores obtenidos para la variable auxiliar provienen realmente de valores admisibles de la variable original, y cuántas preimágenes produce cada uno?**

### Una cuadrática en una expresión

Muchas ecuaciones elementales tienen la forma

$$
a\,[\phi(x)]^2+b\,\phi(x)+c=0,
\qquad a\neq0.
$$

Si definimos

$$
u=\phi(x),
$$

obtenemos la cuadrática

$$
au^2+bu+c=0.
$$

Podemos resolverla mediante cualquiera de las herramientas de §[§21.7](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s07)–21.8. Supongamos que la ecuación auxiliar produce los valores

$$
u_1,\dots,u_k.
$$

El trabajo no termina allí. Para volver a la variable original debemos resolver, para cada valor realizable,

$$
\phi(x)=u_i.
$$

La sustitución es completa sólo cuando hemos reconstruido **todas** las preimágenes admisibles en el dominio original.

### Primer ejemplo: una ecuación bicuadrada

Resolvamos sobre $\mathbb R$

$$
x^4-5x^2+4=0.
$$

Definimos

$$
u=x^2.
$$

La ecuación auxiliar es

$$
u^2-5u+4=0.
$$

Factorizamos:

$$
u^2-5u+4=(u-1)(u-4).
$$

Por tanto,

$$
u=1
\qquad\text{o}\qquad
u=4.
$$

Ahora regresamos a $x$.

Si

$$
x^2=1,
$$

entonces

$$
x=\pm1.
$$

Si

$$
x^2=4,
$$

entonces

$$
x=\pm2.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^4-5x^2+4=0)
=
\{-2,-1,1,2\}.
}
$$

La ecuación auxiliar tenía dos soluciones. La ecuación original tiene cuatro porque cada valor positivo de $u=x^2$ posee dos preimágenes reales.

### La variable auxiliar no vive necesariamente en todo $\mathbb R$

Cuando escribimos

$$
u=x^2,
$$

no estamos introduciendo un real arbitrario. Sobre $\mathbb R$ se cumple necesariamente

$$
u\ge0.
$$

Por tanto, la variable auxiliar tiene una restricción heredada de la sustitución.

Considere

$$
x^4+3x^2-4=0.
$$

Con

$$
u=x^2,
$$

obtenemos

$$
u^2+3u-4=0,
$$

y factorizando,

$$
(u+4)(u-1)=0.
$$

La ecuación auxiliar tiene soluciones

$$
u=-4
\qquad\text{o}\qquad
u=1.
$$

Pero $u=-4$ no es realizable como cuadrado de un número real. No corresponde a ningún $x\in\mathbb R$.

La única rama realizable es

$$
x^2=1,
$$

de donde

$$
x=\pm1.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^4+3x^2-4=0)=\{-1,1\}.
}
$$

El valor auxiliar $u=-4$ no es una «solución extraña en $x$». Es un valor de la ecuación auxiliar que queda fuera de la imagen de la sustitución $u=x^2$.

### Imagen y preimagen

Conviene formular el proceso de manera precisa.

Sea

$$
\phi:D\to\mathbb R
$$

una expresión definida sobre el dominio $D$. Si queremos resolver

$$
Q(\phi(x))=0,
$$

introducimos

$$
u=\phi(x).
$$

Primero resolvemos

$$
Q(u)=0,
$$

pero sólo interesan los valores auxiliares que pertenecen a la imagen

$$
\phi(D).
$$

Si

$$
U=
\{u\in\phi(D):Q(u)=0\},
$$

entonces el conjunto solución original es

$$
\boxed{
\operatorname{Sol}_D(Q(\phi(x))=0)
=
\bigcup_{u\in U}
\{x\in D:\phi(x)=u\}.
}
$$

Esta fórmula describe exactamente las dos tareas de una sustitución:

1. resolver la ecuación en la variable auxiliar;
2. recuperar todas las preimágenes válidas en la variable original.

### La sustitución puede no ser biyectiva

La aplicación

$$
x\longmapsto x^2
$$

no es inyectiva sobre $\mathbb R$, porque

$$
x^2=(-x)^2.
$$

Tampoco es sobreyectiva sobre todo $\mathbb R$, porque ningún cuadrado real es negativo.

Por eso el regreso desde $u$ hacia $x$ debe distinguir:

| Valor auxiliar | Preimágenes reales bajo $u=x^2$ |
|---|---|
| $u>0$ | $x=\pm\sqrt u$ |
| $u=0$ | $x=0$ |
| $u<0$ | ninguna |

Escribir sólo

$$
x=\sqrt u
$$

perdería la rama negativa cuando $u>0$. En cambio, escribir automáticamente $x=\pm\sqrt u$ para $u<0$ introduciría símbolos que no representan soluciones reales.

La sustitución exige, por tanto, conocer la estructura de la aplicación utilizada.

### Un caso en que una solución auxiliar produce una sola preimagen

Considere

$$
x^4-4x^2=0.
$$

Con $u=x^2$ obtenemos

$$
u^2-4u=0,
$$

es decir,

$$
u(u-4)=0.
$$

Por tanto,

$$
u=0
\qquad\text{o}\qquad
u=4.
$$

Al regresar a $x$:

$$
x^2=0
\Longleftrightarrow
x=0,
$$

y

$$
x^2=4
\Longleftrightarrow
x=\pm2.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^4-4x^2=0)=\{-2,0,2\}.
}
$$

El valor auxiliar $u=0$ tiene una sola preimagen real, no dos.

### La misma idea con una expresión desplazada

La sustitución no tiene por qué ser exactamente $u=x^2$.

Considere

$$
(x-1)^4-5(x-1)^2+4=0.
$$

La estructura repetida es

$$
(x-1)^2.
$$

Definimos

$$
u=(x-1)^2.
$$

La ecuación auxiliar vuelve a ser

$$
u^2-5u+4=0,
$$

por lo que

$$
u=1
\qquad\text{o}\qquad
u=4.
$$

Ahora debemos resolver dos ecuaciones en $x$.

Para $u=1$,

$$
(x-1)^2=1
\Longleftrightarrow
x-1=\pm1,
$$

de donde

$$
x=0
\qquad\text{o}\qquad
x=2.
$$

Para $u=4$,

$$
(x-1)^2=4
\Longleftrightarrow
x-1=\pm2,
$$

de donde

$$
x=-1
\qquad\text{o}\qquad
x=3.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl((x-1)^4-5(x-1)^2+4=0\bigr)
=
\{-1,0,2,3\}.
}
$$

La sustitución no depende del grado visible de $x$, sino de reconocer una expresión que se repite con potencias compatibles.

### Sustituciones biyectivas y no biyectivas

Compare dos elecciones auxiliares.

Si

$$
u=2x-1,
$$

entonces, sobre $\mathbb R$, cada valor real de $u$ corresponde a un único valor de $x$:

$$
x=\frac{u+1}{2}.
$$

La sustitución es biyectiva y el regreso no ramifica.

En cambio, si

$$
u=x^2,
$$

la sustitución no es biyectiva sobre $\mathbb R$. El regreso puede producir dos, una o ninguna preimagen.

Esta diferencia será importante en problemas más complejos: una sustitución conveniente simplifica la ecuación, pero también cambia la forma en que debemos reconstruir el conjunto solución.

### Un ejemplo con sustitución lineal

Considere

$$
(2x-1)^2-5(2x-1)+6=0.
$$

Definimos

$$
u=2x-1.
$$

Entonces

$$
u^2-5u+6=0,
$$

y

$$
(u-2)(u-3)=0.
$$

Por tanto,

$$
u=2
\qquad\text{o}\qquad
u=3.
$$

Al regresar,

$$
2x-1=2
\Longleftrightarrow
x=\frac32,
$$

y

$$
2x-1=3
\Longleftrightarrow
x=2.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl((2x-1)^2-5(2x-1)+6=0\bigr)
=
\left\{\frac32,2\right\}.
}
$$

Aquí cada solución auxiliar produce exactamente una solución original.

### El dominio original sigue siendo decisivo

Suponga que resolvemos

$$
x^4-5x^2+4=0
$$

pero sobre

$$
D=[0,\infty).
$$

La ecuación auxiliar con $u=x^2$ sigue produciendo

$$
u=1
\qquad\text{o}\qquad
u=4.
$$

Sobre $\mathbb R$ las preimágenes serían $\pm1$ y $\pm2$. Sin embargo, al intersectar con $D$ sólo sobreviven

$$
1
\qquad\text{y}\qquad
2.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{[0,\infty)}(x^4-5x^2+4=0)=\{1,2\}.
}
$$

La sustitución no sustituye el control de dominio: simplemente añade una capa intermedia de representación.

### Qué errores puede producir una sustitución incompleta

Hay tres fallas especialmente frecuentes.

**1. Detenerse en la variable auxiliar.**

De

$$
u^2-5u+4=0
$$

concluir

$$
u\in\{1,4\}
$$

no resuelve todavía una ecuación cuyo problema original estaba formulado en $x$.

**2. Olvidar la imagen de la sustitución.**

Si $u=x^2$, un valor auxiliar negativo no posee preimagen real.

**3. Recuperar sólo una preimagen.**

De

$$
x^2=9
$$

no se sigue sólo $x=3$, sino

$$
x=\pm3.
$$

Estas tres fallas tienen una misma causa: tratar la sustitución como un simple cambio de letra en lugar de verla como una aplicación entre conjuntos de valores.

### No estamos abriendo todavía la teoría general de ecuaciones polinómicas

La sustitución puede resolver algunas ecuaciones polinómicas de grado mayor cuando presentan una estructura repetida sencilla, como

$$
x^4+px^2+q=0
$$

o

$$
[\phi(x)]^2+p\phi(x)+q=0.
$$

Esto no significa que cualquier ecuación de grado cuatro o superior pueda resolverse por la misma técnica. En C21 sólo trabajaremos con patrones elementales reducibles a herramientas ya construidas.

La división polinómica sistemática, la teoría de raíces y otras estructuras más generales quedan para C23–C24.

### Un protocolo para sustituciones

Cuando una ecuación sugiera una variable auxiliar:

1. fijar el dominio original $D$;
2. identificar una expresión repetida $\phi(x)$;
3. definir $u=\phi(x)$ y determinar, cuando sea relevante, qué valores puede tomar $u$;
4. reescribir completamente la ecuación en términos de $u$;
5. resolver la ecuación auxiliar;
6. descartar valores auxiliares que no pertenezcan a $\phi(D)$;
7. para cada valor auxiliar restante, resolver $\phi(x)=u$;
8. reunir **todas** las preimágenes obtenidas;
9. intersectar con el dominio original;
10. declarar explícitamente el conjunto solución en la variable original.

La etapa 7 es tan importante como la 5. Resolver la ecuación auxiliar y olvidar el regreso produce una respuesta incompleta.

### Recuperación breve

Resuelva sobre $\mathbb R$ usando una sustitución adecuada.

**a)**

$$
x^4-13x^2+36=0.
$$

**b)**

$$
x^4+5x^2+4=0.
$$

**c)**

$$
(x+2)^4-5(x+2)^2+4=0.
$$

**Respuesta razonada.** En **a)** definimos $u=x^2$. Entonces

$$
u^2-13u+36=0,
$$

y

$$
(u-4)(u-9)=0.
$$

Así,

$$
u=4
\qquad\text{o}\qquad
u=9.
$$

Al regresar,

$$
x=\pm2
\qquad\text{o}\qquad
x=\pm3.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\{-3,-2,2,3\}.
}
$$

En **b)**, con $u=x^2$,

$$
u^2+5u+4=0,
$$

y

$$
(u+1)(u+4)=0.
$$

Los únicos valores auxiliares son

$$
u=-1
\qquad\text{o}\qquad
u=-4,
$$

pero ninguno pertenece a la imagen real de $x\mapsto x^2$. Luego,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\varnothing.
}
$$

En **c)** definimos

$$
u=(x+2)^2.
$$

La ecuación auxiliar es otra vez

$$
u^2-5u+4=0,
$$

por lo que

$$
u=1
\qquad\text{o}\qquad
u=4.
$$

De

$$
(x+2)^2=1
$$

obtenemos

$$
x=-3
\qquad\text{o}\qquad
x=-1,
$$

y de

$$
(x+2)^2=4
$$

obtenemos

$$
x=-4
\qquad\text{o}\qquad
x=0.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\{-4,-3,-1,0\}.
}
$$

### Qué debemos conservar de esta sección

Una sustitución útil hace visible una ecuación conocida dentro de una expresión más compleja.

> **Resolver la ecuación auxiliar no basta: hay que conservar sólo los valores auxiliares realizables y reconstruir todas sus preimágenes válidas en la variable original.**

Para $u=x^2$, la condición $u\ge0$ y la vuelta $x=\pm\sqrt u$ cuando $u>0$ forman parte del método, no son correcciones opcionales al final.

En [§21.10](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s10) trasladaremos nuevamente la disciplina de dominio de C20 a la resolución de ecuaciones racionales: allí la transformación central será eliminar denominadores sin olvidar los valores que estaban excluidos desde el comienzo.

## 21.10. Ecuaciones racionales: dominio, eliminación y filtrado {#apm-c21-s10}

En C20 aprendimos a transformar expresiones racionales sin perder las restricciones que pertenecían a su dominio original. Al resolver ecuaciones racionales, esa misma disciplina adquiere una función lógica adicional: las restricciones determinan **qué valores pueden pertenecer al conjunto solución**.

La pregunta central de esta sección será:

> **¿Cuándo podemos eliminar los denominadores sin cambiar el conjunto solución y qué debemos hacer con los valores que la ecuación algebraica resultante parece admitir?**

La respuesta tiene tres etapas inseparables:

```text
DOMINIO
   ↓
ELIMINACIÓN JUSTIFICADA DE DENOMINADORES
   ↓
FILTRADO EN EL DOMINIO ORIGINAL
```

No debemos invertir este orden.

### Una ecuación racional debe leerse primero como una ecuación sobre un dominio

Considere

$$
\frac{x+1}{x-2}=3.
$$

Antes de multiplicar por $x-2$, declaramos

$$
x\neq2.
$$

Por tanto, el dominio efectivo es

$$
D=\mathbb R\setminus\{2\}.
$$

Dentro de $D$, el factor $x-2$ nunca es cero. Por [§21.3](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s03), multiplicar ambos miembros por ese factor es reversible **sobre $D$**:

$$
\frac{x+1}{x-2}=3
\Longleftrightarrow
x+1=3(x-2)
\qquad (x\in D).
$$

Resolviendo,

$$
x+1=3x-6
\Longleftrightarrow
7=2x
\Longleftrightarrow
x=\frac72.
$$

Como $7/2\in D$,

$$
\boxed{
\operatorname{Sol}_D
\left(\frac{x+1}{x-2}=3\right)
=
\left\{\frac72\right\}.
}
$$

La eliminación del denominador fue una equivalencia porque el dominio ya garantizaba la no nulidad del factor multiplicador.

### El principio general de eliminación

Suponga que una ecuación racional está definida sobre un dominio efectivo $D$ y que $M(x)$ es un múltiplo común de todos sus denominadores. Si la construcción de $D$ garantiza

$$
M(x)\neq0
\qquad\text{para todo }x\in D,
$$

entonces

$$
E(x)=F(x)
\Longleftrightarrow
M(x)E(x)=M(x)F(x)
\qquad (x\in D).
$$

Ésta es la formulación correcta de la frase informal «eliminar denominadores».

No estamos borrando símbolos. Estamos multiplicando ambos miembros por una expresión conocida como no nula **en el dominio vigente**.

Por eso el orden lógico es:

1. encontrar el dominio efectivo;
2. elegir un múltiplo común de los denominadores;
3. comprobar que ese múltiplo es no nulo en el dominio;
4. multiplicar ambos miembros;
5. resolver la ecuación resultante;
6. conservar sólo los valores que pertenecen al dominio original.

### Un candidato algebraico puede estar excluido desde el comienzo

Considere

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1}.
$$

El dominio efectivo es

$$
D=\mathbb R\setminus\{1\}.
$$

Sobre $D$ podemos multiplicar por $x-1$:

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1}
\Longleftrightarrow
x+1=2
\qquad (x\in D).
$$

La ecuación algebraica resultante produce

$$
x=1.
$$

Pero

$$
1\notin D.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_D=\varnothing.
}
$$

El valor $1$ no es una solución «creada» por una transformación ilegítima. La multiplicación por $x-1$ fue perfectamente reversible **sobre $D$**. Lo que ocurre es que la ecuación transformada, si se leyera fuera de $D$, tendría una solución que nunca fue admisible en el problema original.

Ésta es la distinción que ya anticipamos en [§21.4](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s04):

> **un valor excluido por dominio no es lo mismo que un candidato extraño producido por una transformación no reversible.**

### La ecuación transformada debe seguir interpretándose sobre el mismo dominio

El ejemplo anterior puede escribirse como

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1}
\Longleftrightarrow
x+1=2
\qquad (x\in\mathbb R\setminus\{1\}).
$$

Observe que la ecuación $x+1=2$, considerada por sí sola sobre todo $\mathbb R$, tiene solución $1$. Pero **ésa no es la ecuación transformada que hemos obtenido**. La afirmación correcta conserva el dominio:

$$
x+1=2,
\qquad x\in\mathbb R\setminus\{1\}.
$$

Sobre ese dominio, tampoco tiene soluciones.

La restricción puede desaparecer de la fórmula visible sin desaparecer del problema.

### Varios denominadores: usar un múltiplo común no nulo

Resolvamos

$$
\frac{1}{x-1}
+
\frac{1}{x+1}
=1.
$$

Primero,

$$
x\neq1,
\qquad
x\neq-1.
$$

Así,

$$
D=\mathbb R\setminus\{-1,1\}.
$$

Un múltiplo común de los denominadores es

$$
M(x)=(x-1)(x+1).
$$

En todo $D$ se cumple $M(x)\neq0$. Podemos multiplicar la ecuación completa por $M(x)$:

$$
(x+1)+(x-1)=(x-1)(x+1).
$$

Entonces

$$
2x=x^2-1,
$$

y por tanto

$$
x^2-2x-1=0.
$$

La fórmula cuadrática da

$$
x=1\pm\sqrt2.
$$

Ninguno de esos valores es $1$ ni $-1$, de modo que ambos pertenecen a $D$. Así,

$$
\boxed{
\operatorname{Sol}_D
=
\{1-\sqrt2,\,1+\sqrt2\}.
}
$$

Aquí no hubo que «comprobar por desconfianza» la ecuación polinómica obtenida: cada paso fue una equivalencia sobre $D$. El control final consiste en verificar que las soluciones obtenidas pertenecen al dominio sobre el que afirmamos esas equivalencias.

### El múltiplo común no necesita ser el más pequeño, pero debe ser seguro

En el ejemplo anterior podríamos multiplicar por

$$
2(x-1)(x+1)
$$

en lugar de $(x-1)(x+1)$. El factor extra $2$ no cambia nada porque nunca es cero.

En cambio, introducir un factor variable adicional puede ser peligroso. Si multiplicáramos innecesariamente por

$$
x(x-1)(x+1),
$$

entonces $x=0$ anularía el multiplicador aunque $0\in D$. La transformación ya no sería reversible en todo el dominio y podría crear candidatos adicionales.

Por tanto:

> **Un multiplicador común puede contener factores auxiliares sólo si sabemos que también son no nulos en todo el dominio vigente.**

La forma más segura suele ser usar el producto de los factores de denominador necesarios, simplificado únicamente cuando esa simplificación no introduce ambigüedad sobre la no nulidad.

### Simplificar antes de resolver puede ser útil, pero el dominio se fija antes

Considere

$$
\frac{x^2-9}{x-3}=6.
$$

El dominio original exige

$$
x\neq3.
$$

Factorizamos el numerador:

$$
x^2-9=(x-3)(x+3).
$$

Sobre

$$
D=\mathbb R\setminus\{3\},
$$

podemos cancelar $x-3$ y escribir

$$
\frac{x^2-9}{x-3}=6
\Longleftrightarrow
x+3=6
\qquad (x\in D).
$$

La ecuación lineal da

$$
x=3,
$$

pero ese valor no pertenece a $D$. Luego,

$$
\boxed{
\operatorname{Sol}_D=\varnothing.
}
$$

Este ejemplo es especialmente importante porque la fórmula simplificada

$$
x+3=6
$$

parece tener una solución obvia. El problema no está en la simplificación: está en olvidar que la equivalencia fue demostrada sólo para $x\neq3$.

### Eliminar denominadores puede producir una ecuación de grado mayor

Considere

$$
\frac{2}{x}
+
\frac{1}{x-1}
=3.
$$

El dominio efectivo es

$$
D=\mathbb R\setminus\{0,1\}.
$$

Multiplicamos por

$$
x(x-1),
$$

que es no nulo en todo $D$:

$$
2(x-1)+x=3x(x-1).
$$

Entonces

$$
3x-2=3x^2-3x,
$$

y

$$
3x^2-6x+2=0.
$$

Su discriminante es

$$
\Delta=(-6)^2-4(3)(2)=36-24=12.
$$

Por tanto,

$$
x
=
\frac{6\pm\sqrt{12}}{6}
=
1\pm\frac{\sqrt3}{3}.
$$

Ambos valores son distintos de $0$ y $1$. Así,

$$
\boxed{
\operatorname{Sol}_D
=
\left\{
1-\frac{\sqrt3}{3},
1+\frac{\sqrt3}{3}
\right\}.
}
$$

Una ecuación racional puede transformarse en una ecuación lineal, cuadrática o de otro tipo. La eliminación de denominadores no determina el método final; sólo elimina una capa de representación conservando el problema sobre $D$.

### Denominadores factorizables: leer las restricciones antes de expandir

Considere

$$
\frac{1}{x^2-4}
=
\frac{1}{x-2}.
$$

Antes de operar, factorizamos el denominador para leer su dominio:

$$
x^2-4=(x-2)(x+2).
$$

Por tanto,

$$
D=\mathbb R\setminus\{-2,2\}.
$$

Sobre $D$, multiplicar por $(x-2)(x+2)$ es reversible:

$$
1=x+2.
$$

La ecuación resultante da

$$
x=-1,
$$

que pertenece a $D$. Luego,

$$
\boxed{
\operatorname{Sol}_D=\{-1\}.
}
$$

La factorización del denominador cumplió aquí dos funciones distintas:

- permitió leer correctamente el dominio;
- mostró un multiplicador común eficiente.

### Cancelación y eliminación de denominadores no son el mismo paso

Considere

$$
\frac{(x-2)(x+1)}{x-2}=5.
$$

El dominio exige $x\neq2$.

Podemos simplificar primero:

$$
\frac{(x-2)(x+1)}{x-2}=5
\Longleftrightarrow
x+1=5
\qquad (x\neq2),
$$

porque cancelar $x-2$ significa dividir numerador y denominador por un factor no nulo en el dominio.

También podríamos multiplicar toda la ecuación por $x-2$:

$$
(x-2)(x+1)=5(x-2).
$$

Sobre $x\neq2$ ambas rutas son equivalentes. La primera reduce la expresión antes; la segunda elimina el denominador exterior.

La elección es estratégica, pero la lógica común es la misma: **el factor $x-2$ está garantizado como no nulo por el dominio original**.

### Una identidad racional puede tener como solución todo el dominio, no todo $\mathbb R$

Considere

$$
\frac{x^2-1}{x-1}=x+1.
$$

La expresión racional del lado izquierdo exige

$$
x\neq1.
$$

Sobre

$$
D=\mathbb R\setminus\{1\},
$$

factorizamos

$$
x^2-1=(x-1)(x+1)
$$

y obtenemos

$$
\frac{x^2-1}{x-1}=x+1
\Longleftrightarrow
x+1=x+1.
$$

La igualdad final es verdadera para todo valor de $D$. Por tanto,

$$
\boxed{
\operatorname{Sol}_D=D=\mathbb R\setminus\{1\}.
}
$$

No es correcto responder $\mathbb R$. El punto $x=1$ continúa excluido aunque la identidad final tenga sentido allí.

### Filtrar no significa probar al azar

En ecuaciones racionales, «filtrar» puede significar dos cosas distintas.

**1. Filtrado por dominio.** Si la cadena fue completamente equivalente sobre $D$, basta descartar cualquier valor final que no pertenezca a $D$.

**2. Filtrado después de una implicación.** Si en algún punto usamos una transformación no reversible, entonces los valores finales son sólo candidatos y debemos comprobarlos en la ecuación original o recuperar condiciones equivalentes suficientes.

En la eliminación estándar de denominadores **bien hecha**, sobre un dominio ya fijado, estamos en el primer caso. Multiplicar por un común denominador que sabemos no nulo es una equivalencia.

Esta distinción evita un hábito confuso: comprobar siempre al final sin saber por qué. La comprobación tiene una función lógica concreta; no reemplaza el análisis de las flechas.

### Un protocolo para ecuaciones racionales

Podemos condensar la estrategia de esta sección en nueve pasos:

1. fijar el dominio ambiente;
2. factorizar denominadores cuando sea necesario para localizar sus ceros;
3. formar el dominio efectivo excluyendo todos los ceros de denominador;
4. simplificar sólo mediante equivalencias válidas sobre ese dominio;
5. elegir un múltiplo común de los denominadores que sea no nulo en todo el dominio efectivo;
6. multiplicar **la ecuación completa** por ese múltiplo;
7. resolver la ecuación resultante con las herramientas ya conocidas;
8. descartar valores que no pertenezcan al dominio original;
9. declarar explícitamente el conjunto solución sobre ese dominio.

Si durante la ruta aparece una transformación que no sea reversible, añadimos un décimo paso:

10. comprobar en la ecuación original los candidatos que hayan sobrevivido.

### Recuperación breve

Resuelva sobre $\mathbb R$.

**a)**

$$
\frac{3}{x-2}=1.
$$

**b)**

$$
\frac{x}{x+1}=\frac{-1}{x+1}.
$$

**c)**

$$
\frac{1}{x-1}+\frac{2}{x+1}=1.
$$

**Respuesta razonada.** En **a)** el dominio exige $x\neq2$. Sobre ese dominio,

$$
\frac{3}{x-2}=1
\Longleftrightarrow
3=x-2,
$$

por lo que

$$
x=5.
$$

Como $5\neq2$,

$$
\boxed{\operatorname{Sol}=\{5\}.}
$$

En **b)** el dominio exige $x\neq-1$. Multiplicando por $x+1$,

$$
x=-1.
$$

Ese valor está excluido del dominio. Por tanto,

$$
\boxed{\operatorname{Sol}=\varnothing.}
$$

En **c)**,

$$
D=\mathbb R\setminus\{-1,1\}.
$$

Multiplicamos por $(x-1)(x+1)$:

$$
(x+1)+2(x-1)=(x-1)(x+1).
$$

Así,

$$
3x-1=x^2-1,
$$

y por tanto

$$
x^2-3x=0.
$$

Factorizamos:

$$
x(x-3)=0,
$$

de donde

$$
x=0
\qquad\text{o}\qquad
x=3.
$$

Ambos pertenecen a $D$. Luego,

$$
\boxed{
\operatorname{Sol}=\{0,3\}.
}
$$

### Qué debemos conservar de esta sección

Las ecuaciones racionales no se resuelven «quitando denominadores» y recordando después algunas excepciones. El dominio es parte del problema desde el comienzo.

> **Si un común denominador es no nulo en todo el dominio efectivo, multiplicar la ecuación por él es una equivalencia sobre ese dominio.**

Los valores excluidos no vuelven a ser admisibles aunque desaparezcan los denominadores de la escritura. Una ecuación algebraica resultante debe seguir leyéndose sobre el mismo dominio de procedencia.

En [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11) estudiaremos ecuaciones radicales. Allí aparecerá una dificultad lógica distinta: elevar al cuadrado puede dejar de ser una equivalencia y producir candidatos verdaderamente adicionales, por lo que el control final tendrá una función diferente de la que tuvo aquí.

## 21.11. Ecuaciones radicales: implicación, signo y verificación {#apm-c21-s11}

En [§21.10](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s10) eliminamos denominadores mediante una transformación que podía conservar exactamente el conjunto solución: una vez fijado el dominio efectivo, multiplicábamos por una expresión conocida como no nula en ese dominio. Las ecuaciones radicales introducen una dificultad lógica diferente.

Considere

$$
\sqrt{x+1}=x-1.
$$

Es natural querer elevar ambos miembros al cuadrado. El cálculo produce

$$
x+1=(x-1)^2.
$$

Pero aquí aparece la pregunta que guiará toda la sección:

> **¿Cuadrar conserva exactamente el conjunto solución o sólo produce una ecuación que toda solución original debe satisfacer?**

La respuesta depende del signo. Una raíz cuadrada principal es siempre no negativa. El cuadrado, en cambio, no recuerda el signo de la expresión que fue elevada.

### La raíz principal lleva información de signo

C18 estableció dos hechos que ahora se vuelven decisivos:

$$
\sqrt{u}\ge0
$$

siempre que la raíz cuadrada principal esté definida, y

$$
\boxed{\sqrt{u^2}=|u|}.
$$

Por tanto, una igualdad de la forma

$$
\sqrt{R(x)}=S(x)
$$

contiene inmediatamente una condición necesaria:

$$
S(x)\ge0.
$$

Si para algún valor $S(x)<0$, ese valor no puede satisfacer la ecuación, aunque una ecuación obtenida después de cuadrar sí pudiera admitirlo.

Esta condición de signo no abre todavía la teoría sistemática de inequaciones de C22. Aquí funciona sólo como una **condición de admisibilidad** impuesta por la raíz principal.

### Cuadrar conserva una dirección

Para números reales,

$$
A=B
\Longrightarrow
A^2=B^2.
$$

La vuelta no es cierta en general, porque

$$
A^2=B^2
\Longleftrightarrow
A=B\ \text{o}\ A=-B.
$$

Así, de

$$
\sqrt{R(x)}=S(x)
$$

podemos concluir siempre

$$
R(x)=S(x)^2,
$$

pero la ecuación cuadrada puede admitir valores para los cuales

$$
\sqrt{R(x)}=-S(x)
$$

en lugar de $\sqrt{R(x)}=S(x)$.

La flecha segura, si no conservamos ninguna condición adicional, es

$$
\sqrt{R(x)}=S(x)
\Longrightarrow
R(x)=S(x)^2.
$$

Por eso los resultados de la ecuación cuadrada deben considerarse **candidatos** para la ecuación original.

### Recuperar la equivalencia completa

Cuando la raíz principal está aislada, podemos describir exactamente qué condición falta.

Sobre el dominio efectivo en el que $R(x)$ y $S(x)$ están definidos y $R(x)\ge0$,

$$
\boxed{
\sqrt{R(x)}=S(x)
\Longleftrightarrow
\bigl(R(x)=S(x)^2\ \text{y}\ S(x)\ge0\bigr).
}
$$

La demostración contiene las dos direcciones.

Si

$$
\sqrt{R(x)}=S(x),
$$

entonces al cuadrar obtenemos

$$
R(x)=S(x)^2,
$$

y además $S(x)\ge0$ porque una raíz principal nunca es negativa.

Recíprocamente, si

$$
R(x)=S(x)^2
$$

y

$$
S(x)\ge0,
$$

entonces

$$
\sqrt{R(x)}
=
\sqrt{S(x)^2}
=
|S(x)|
=
S(x).
$$

La última igualdad usa precisamente la condición $S(x)\ge0$.

Observe además que $R(x)=S(x)^2$ ya garantiza $R(x)\ge0$. Por ello, también podemos hallar las soluciones resolviendo las dos condiciones de la derecha en el dominio ambiente donde $R$ y $S$ existen: todo valor que las cumpla pertenece automáticamente al dominio efectivo de la raíz. Esto es una igualdad de conjuntos solución; no asigna un valor de verdad a la expresión radical en los puntos donde no está definida.

### Ejemplo rector: un candidato creado al cuadrar

Resolvamos

$$
\sqrt{x+1}=x-1
$$

sobre $\mathbb R$.

Podemos usar directamente la equivalencia completa:

$$
\sqrt{x+1}=x-1
\Longleftrightarrow
\begin{cases}
x+1=(x-1)^2,\\
x-1\ge0.
\end{cases}
$$

La ecuación cuadrada da

$$
x+1=x^2-2x+1,
$$

por lo que

$$
x^2-3x=0,
$$

y entonces

$$
x=0
\qquad\text{o}\qquad
x=3.
$$

Pero la condición de signo exige

$$
x-1\ge0.
$$

De los dos candidatos, sólo $x=3$ cumple esa condición. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(\sqrt{x+1}=x-1\bigr)
=
\{3\}.
}
$$

La comprobación directa muestra qué ocurrió con $x=0$:

$$
\sqrt{0+1}=1,
\qquad
0-1=-1.
$$

El candidato $0$ no estaba excluido por dominio. **Fue creado por una transformación que perdió información de signo.** Ésta es exactamente la situación que distinguimos de los valores inadmisibles por dominio en §[§21.4](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s04) y 21.10.

### El signo puede descartar una rama antes de cuadrar

Considere

$$
\sqrt{2x+3}=-x.
$$

La raíz principal es no negativa, así que cualquier solución debe cumplir

$$
-x\ge0.
$$

Si cuadramos obtenemos

$$
2x+3=x^2,
$$

o equivalentemente

$$
(x-3)(x+1)=0.
$$

Los candidatos son

$$
x=3
\qquad\text{o}\qquad
x=-1.
$$

La condición $-x\ge0$ elimina inmediatamente $x=3$. El valor $x=-1$ sí satisface la ecuación original:

$$
\sqrt{2(-1)+3}=1=-(-1).
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(\sqrt{2x+3}=-x\bigr)
=
\{-1\}.
}
$$

Aquí la condición de signo no es un control posterior accidental: forma parte de una formulación equivalente del problema.

### Cuando ambos miembros son raíces principales

Hay situaciones en que cuadrar sí puede ser reversible porque el signo está controlado automáticamente.

Considere

$$
\sqrt{x+5}=\sqrt{2x+1}.
$$

En el dominio común de ambas raíces, los dos miembros son no negativos. Para números no negativos, la función $t\mapsto t^2$ es inyectiva. Por tanto,

$$
\sqrt{x+5}=\sqrt{2x+1}
\Longleftrightarrow
x+5=2x+1
$$

sobre el dominio donde ambas raíces están definidas.

La ecuación lineal da

$$
x=4,
$$

que pertenece al dominio. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(\sqrt{x+5}=\sqrt{2x+1}\bigr)
=
\{4\}.
}
$$

No es el acto gráfico de «cuadrar» lo que decide si hay equivalencia. Lo que importa es si el signo de ambos miembros permite recuperar la igualdad original a partir de la igualdad de cuadrados.

### Dos radicales pueden exigir más de una etapa

Considere ahora

$$
\sqrt{x+5}+\sqrt{x}=5.
$$

El dominio exige

$$
x\ge0.
$$

Los dos miembros de la igualdad son no negativos, así que podemos cuadrar la igualdad completa de manera reversible dentro de ese dominio:

$$
\bigl(\sqrt{x+5}+\sqrt{x}\bigr)^2=25.
$$

Desarrollando,

$$
2x+5+2\sqrt{x(x+5)}=25,
$$

y por tanto

$$
\sqrt{x(x+5)}=10-x.
$$

Aparece de nuevo una raíz principal aislada. Para mantener equivalencia debemos conservar

$$
10-x\ge0.
$$

Ahora sí cuadramos una segunda vez:

$$
x(x+5)=(10-x)^2.
$$

Al desarrollar,

$$
x^2+5x=x^2-20x+100,
$$

de modo que

$$
25x=100
$$

y

$$
x=4.
$$

El valor satisface $x\ge0$ y $10-x\ge0$, y además

$$
\sqrt{9}+\sqrt4=3+2=5.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(\sqrt{x+5}+\sqrt{x}=5\bigr)
=
\{4\}.
}
$$

Este ejemplo muestra que una ecuación con varios radicales puede exigir aislar un radical después de la primera transformación y repetir el procedimiento. Cada nuevo cuadrado debe auditarse con sus propias condiciones de signo.

### Una condición de signo puede ahorrar un segundo cuadrado inútil

Compare el ejemplo anterior con

$$
\sqrt{x+5}+\sqrt{x}=1.
$$

El dominio vuelve a exigir $x\ge0$. Si cuadramos la igualdad completa,

$$
2x+5+2\sqrt{x(x+5)}=1,
$$

de donde

$$
\sqrt{x(x+5)}=-x-2.
$$

Pero para $x\ge0$ el segundo miembro cumple

$$
-x-2<0,
$$

mientras que una raíz principal nunca es negativa. Podemos concluir inmediatamente

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\varnothing.
}
$$

Si ignoráramos el signo y eleváramos de nuevo al cuadrado, obtendríamos

$$
x(x+5)=(x+2)^2,
$$

lo que produce el candidato $x=4$. Ese valor no satisface la ecuación original:

$$
\sqrt9+\sqrt4=5\neq1.
$$

La condición de signo no sólo aporta rigor: puede evitar trabajo algebraico que conduciría únicamente a candidatos falsos.

### Verificar tiene aquí una función lógica específica

En [§21.10](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s10) vimos que, si eliminábamos denominadores mediante equivalencias sobre el dominio efectivo, el filtrado final podía limitarse a comprobar pertenencia al dominio. En una ecuación radical la situación puede ser distinta.

Si en algún momento usamos

$$
A=B
\Longrightarrow
A^2=B^2
$$

sin conservar condiciones suficientes para recuperar la equivalencia, el conjunto solución de la ecuación transformada puede ser mayor que el original. Entonces los valores finales son **candidatos** y deben comprobarse en la ecuación de partida.

La verificación final cumple así una función bien determinada:

- no sustituye el análisis de dominio;
- no repara una solución perdida por una transformación reductiva;
- **filtra candidatos creados por una transformación sólo implicativa**.

Cuando conservamos en cada etapa las condiciones de signo que restituyen equivalencia, la comprobación final sigue siendo un buen control independiente, pero ya no es la única razón por la que sabemos que el conjunto solución es correcto.

### Aislar antes de cuadrar

Cuando aparece un solo radical junto con otros términos, suele ser preferible aislarlo antes de elevar al cuadrado.

Por ejemplo, ante

$$
\sqrt{x+7}+2=x,
$$

la forma útil es

$$
\sqrt{x+7}=x-2.
$$

En ese punto la estructura lógica es visible:

$$
\sqrt{x+7}=x-2
\Longleftrightarrow
\begin{cases}
x+7=(x-2)^2,\\
x-2\ge0.
\end{cases}
$$

Cuadrar la ecuación antes de aislar el radical produciría términos cruzados y una representación menos transparente sin aportar ninguna ventaja lógica.

La regla estratégica es:

> **Aísle un radical principal siempre que eso haga visible la condición de signo que deberá acompañar al cuadrado.**

### Un protocolo para ecuaciones radicales

Para las ecuaciones radicales elementales de C21 seguiremos este orden:

1. fijar el dominio ambiente y las condiciones de existencia de todos los radicales;
2. simplificar sólo mediante equivalencias válidas en ese dominio;
3. aislar un radical cuando sea posible;
4. registrar la condición de signo del miembro opuesto;
5. elevar al cuadrado, indicando si el paso es equivalencia o sólo implicación;
6. resolver la ecuación algebraica resultante;
7. si quedan radicales, aislar de nuevo uno de ellos y repetir el control de signo antes del siguiente cuadrado;
8. conservar sólo los candidatos que satisfacen todas las condiciones acumuladas;
9. comprobar en la ecuación original cuando haya existido algún paso sólo implicativo o cuando se desee un control independiente;
10. declarar explícitamente el conjunto solución.

Este protocolo mantiene separadas tres obligaciones que a menudo se mezclan:

$$
\boxed{
\text{dominio}
\quad+
\text{signo}
\quad+
\text{fuerza lógica de cada cuadrado}.
}
$$

### Recuperación breve

Resuelva sobre $\mathbb R$ y explique en qué pasos hay equivalencia y en cuáles sólo implicación.

**a)**

$$
\sqrt{x+6}=4.
$$

**b)**

$$
\sqrt{3x+4}=x.
$$

**c)**

$$
\sqrt{x+5}+\sqrt{x}=5.
$$

**Respuesta razonada.** En **a)** el segundo miembro es la constante positiva $4$, de modo que

$$
\sqrt{x+6}=4
\Longleftrightarrow
x+6=16.
$$

Así,

$$
x=10,
$$

y

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{10\}.}
$$

En **b)** la raíz principal exige que el segundo miembro sea no negativo en cualquier solución. Por tanto,

$$
\sqrt{3x+4}=x
\Longleftrightarrow
\begin{cases}
3x+4=x^2,\\
x\ge0.
\end{cases}
$$

La ecuación cuadrada factoriza como

$$
x^2-3x-4=0
\Longleftrightarrow
(x-4)(x+1)=0.
$$

Los candidatos son $4$ y $-1$, pero la condición $x\ge0$ conserva sólo $4$. En efecto,

$$
\sqrt{16}=4.
$$

Luego,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{4\}.}
$$

Si hubiéramos escrito sólo la implicación obtenida al cuadrar, $-1$ habría aparecido como candidato adicional.

En **c)** el dominio exige $x\ge0$. Como ambos miembros de

$$
\sqrt{x+5}+\sqrt{x}=5
$$

son no negativos, el primer cuadrado puede leerse como equivalencia en ese dominio y produce

$$
\sqrt{x(x+5)}=10-x.
$$

Debemos conservar además $10-x\ge0$. El segundo cuadrado da

$$
x(x+5)=(10-x)^2,
$$

de donde $x=4$. Ese valor satisface todas las condiciones acumuladas y la ecuación original, por lo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{4\}.}
$$

### Qué debemos conservar de esta sección

Elevar al cuadrado no debe tratarse como una operación automáticamente reversible.

> **En general, $A=B$ implica $A^2=B^2$, pero la vuelta requiere información de signo. Para una raíz principal aislada, esa información se expresa exactamente mediante $S(x)\ge0$.**

Por eso,

$$
\boxed{
\sqrt{R(x)}=S(x)
\Longleftrightarrow
\bigl(R(x)=S(x)^2\ \text{y}\ S(x)\ge0\bigr).
}
$$

Las raíces extrañas no son valores que «casi sirven». Son candidatos producidos porque una transformación perdió información. El control de signo permite prevenir muchos de ellos; la verificación en la ecuación original permite filtrarlos cuando la cadena incluyó pasos sólo implicativos.

En [§21.12](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s12) estudiaremos ecuaciones con valor absoluto. Allí volverá a aparecer una estructura de casos, pero ahora no a causa de una transformación no reversible, sino porque el valor absoluto codifica desde el comienzo dos posibilidades de signo.

## 21.12. Ecuaciones con valor absoluto {#apm-c21-s12}

En [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11) apareció una estructura de casos porque elevar al cuadrado puede borrar información de signo. En las ecuaciones con valor absoluto también aparecerán dos casos, pero por una razón distinta: las dos posibilidades están contenidas desde el comienzo en el significado mismo del valor absoluto.

Considere

$$
|2x-1|=5.
$$

La igualdad afirma que $2x-1$ está a distancia $5$ de $0$. En los reales hay exactamente dos números con esa propiedad, $5$ y $-5$. Por tanto,

$$
|2x-1|=5
\Longleftrightarrow
2x-1=5
\quad\text{o}\quad
2x-1=-5.
$$

La palabra **o** será esencial. Resolver una ecuación con valor absoluto no consiste en escoger uno de los signos, sino en reunir todas las posibilidades permitidas por una equivalencia.

### El valor absoluto codifica dos posibilidades de signo

Para un número real $u$ y una constante real $c$, la ecuación $|u|=c$ presenta tres comportamientos.

Si $c<0$, no hay soluciones, porque el valor absoluto nunca es negativo.

Si $c=0$, entonces

$$
|u|=0
\Longleftrightarrow
u=0.
$$

Si $c>0$, entonces

$$
\boxed{
|u|=c
\Longleftrightarrow
u=c
\quad\text{o}\quad
u=-c.
}
$$

Estas posibilidades no constituyen una receta añadida desde fuera. Se desprenden del significado del valor absoluto: $|u|$ mide la distancia de $u$ al origen, y hay dos puntos de la recta a distancia positiva $c$ de $0$.

Hay aquí una diferencia importante respecto de las ecuaciones radicales. Al pasar de $|u|=c$ a $u=c$ o $u=-c$ no estamos aplicando una transformación sólo implicativa. Estamos escribiendo una condición **equivalente**.

### Ejemplo rector: abrir las dos ramas

Resolvamos

$$
|2x-1|=5
$$

sobre $\mathbb R$.

Como $5>0$,

$$
|2x-1|=5
\Longleftrightarrow
2x-1=5
\quad\text{o}\quad
2x-1=-5.
$$

La primera ecuación da $x=3$; la segunda, $x=-2$. Como las dos ramas proceden de una equivalencia,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(|2x-1|=5\bigr)
=
\{-2,3\}.
}
$$

No hemos «probado dos signos» de manera heurística. Hemos reemplazado una condición por otra exactamente equivalente.

### Un segundo miembro negativo cierra el problema antes de operar

Considere

$$
|3x+2|=-4.
$$

Para todo número real $x$,

$$
|3x+2|\ge0.
$$

El lado derecho es negativo. Luego la igualdad nunca puede cumplirse:

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(|3x+2|=-4\bigr)
=
\varnothing.
}
$$

Leer primero la estructura evita álgebra innecesaria. No tendría sentido «quitar las barras» antes de advertir que la igualdad contradice una propiedad básica del valor absoluto.

### Aislar el valor absoluto antes de abrir casos

Cuando el valor absoluto aparece acompañado por otras operaciones, suele ser preferible aislarlo primero mediante transformaciones equivalentes.

Resolvamos

$$
2|x-3|+1=9.
$$

Restamos $1$ y dividimos por $2$:

$$
2|x-3|=8
\Longleftrightarrow
|x-3|=4.
$$

Ahora sí abrimos los casos:

$$
|x-3|=4
\Longleftrightarrow
x-3=4
\quad\text{o}\quad
x-3=-4.
$$

Por tanto,

$$
x=7
\qquad\text{o}\qquad
x=-1,
$$

y

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-1,7\}.
}
$$

Aislar primero reduce el cálculo y deja visible cuál es exactamente la cantidad cuyo valor absoluto estamos interpretando.

### Cuando el segundo miembro depende de la variable

La situación merece más cuidado si tenemos

$$
|A(x)|=B(x).
$$

El lado izquierdo es siempre no negativo. Por tanto, toda solución debe cumplir $B(x)\ge0$. Conservando esa condición, obtenemos la equivalencia completa

$$
\boxed{
|A(x)|=B(x)
\Longleftrightarrow
\left(
B(x)\ge0
\quad\text{y}\quad
\left(A(x)=B(x)\ \text{o}\ A(x)=-B(x)\right)
\right).
}
$$

No estamos abriendo todavía la teoría de inequaciones de C22. La condición $B(x)\ge0$ aparece sólo como requisito de admisibilidad impuesto por el valor absoluto.

Resolvamos

$$
|x-2|=x.
$$

Toda solución debe satisfacer $x\ge0$. Bajo esa condición,

$$
|x-2|=x
\Longleftrightarrow
x-2=x
\quad\text{o}\quad
x-2=-x.
$$

La primera rama produce la contradicción $-2=0$. La segunda da $2x=2$, de modo que $x=1$. Este valor cumple la condición de admisibilidad y satisface la ecuación original. Luego

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(|x-2|=x\bigr)
=
\{1\}.
}
$$

La no negatividad del segundo miembro no es un filtro añadido al final: forma parte de la caracterización equivalente del problema.

### Dos valores absolutos: la igualdad de distancias

Si ambos miembros son valores absolutos, la condición de no negatividad está incorporada automáticamente. Para números reales,

$$
\boxed{
|A(x)|=|B(x)|
\Longleftrightarrow
A(x)=B(x)
\quad\text{o}\quad
A(x)=-B(x).
}
$$

La equivalencia también puede verse algebraicamente. De $|A|=|B|$ se obtiene $A^2=B^2$, y entonces

$$
(A-B)(A+B)=0.
$$

Por el producto nulo, $A=B$ o $A=-B$. La vuelta es inmediata.

Resolvamos

$$
|2x-3|=|x+1|.
$$

Tenemos

$$
2x-3=x+1
\quad\text{o}\quad
2x-3=-(x+1).
$$

La primera rama da $x=4$. La segunda da $3x=2$, por lo que $x=2/3$. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{\frac23,4\right\}.
}
$$

### El caso cero colapsa las dos ramas

El patrón «positivo y negativo» no significa que toda ecuación con valor absoluto deba producir dos ramas distintas.

Considere

$$
|x^2-5x+6|=0.
$$

Como $|u|=0$ si y sólo si $u=0$,

$$
|x^2-5x+6|=0
\Longleftrightarrow
x^2-5x+6=0.
$$

Factorizando,

$$
(x-2)(x-3)=0.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{2,3\}.
}
$$

Las dos soluciones proceden aquí de la factorización de la expresión interior, no de dos signos del valor absoluto.

### Valor absoluto anidado: abrir de afuera hacia adentro

Una ecuación puede contener valores absolutos anidados. En ese caso conviene empezar por el más exterior.

Resolvamos

$$
\bigl||x|-2\bigr|=1.
$$

La ecuación exterior equivale a

$$
|x|-2=1
\quad\text{o}\quad
|x|-2=-1.
$$

La primera rama da $|x|=3$, luego $x=\pm3$. La segunda da $|x|=1$, luego $x=\pm1$. Al reunir todas las soluciones,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-3,-1,1,3\}.
}
$$

Cada apertura fue una equivalencia. El conjunto solución final se obtiene uniendo las soluciones de todas las ramas, no comprobando una lista de candidatos producida por pasos irreversibles.

### La unión de ramas es parte de la lógica

Si una ecuación $E$ es equivalente a

$$
E_1
\quad\text{o}\quad
E_2,
$$

entonces

$$
\operatorname{Sol}(E)
=
\operatorname{Sol}(E_1)
\cup
\operatorname{Sol}(E_2).
$$

Esto evita dos errores frecuentes: resolver sólo una rama y perder soluciones, o intersectar accidentalmente las ramas como si ambas condiciones tuvieran que cumplirse a la vez.

Para $c>0$, la afirmación

$$
|A(x)|=c
$$

significa

$$
A(x)=c
\quad\text{o}\quad
A(x)=-c,
$$

no ambas simultáneamente.

### El dominio anterior a las barras sigue vigente

El valor absoluto no borra las restricciones de la expresión que contiene.

Considere

$$
\left|
\frac{x+1}{x-1}
\right|
=2.
$$

El dominio original es

$$
D=\mathbb R\setminus\{1\}.
$$

Sobre ese dominio,

$$
\left|
\frac{x+1}{x-1}
\right|
=2
\Longleftrightarrow
\frac{x+1}{x-1}=2
\quad\text{o}\quad
\frac{x+1}{x-1}=-2.
$$

En la primera rama, multiplicar por $x-1$ es reversible porque $x\neq1$:

$$
x+1=2x-2,
$$

de donde $x=3$.

En la segunda,

$$
x+1=-2x+2,
$$

de donde $3x=1$ y $x=1/3$.

Ambos valores pertenecen a $D$. Así,

$$
\boxed{
\operatorname{Sol}_{D}
=
\left\{\frac13,3\right\}.
}
$$

Las barras exteriores no protegen de una división por cero. El dominio se fija desde la expresión original y acompaña todas las ramas posteriores.

### Comparación con las ecuaciones radicales

La comparación con [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11) aclara el papel lógico de los casos.

Para una raíz principal aislada,

$$
\sqrt{R(x)}=S(x)
\Longleftrightarrow
\bigl(R(x)=S(x)^2\ \text{y}\ S(x)\ge0\bigr).
$$

Si olvidamos la condición de signo y sólo cuadramos, podemos crear candidatos adicionales.

En cambio, para $c>0$,

$$
|A(x)|=c
\Longleftrightarrow
A(x)=c
\quad\text{o}\quad
A(x)=-c.
$$

Abrir las dos ramas no pierde información. Expresa exactamente la condición inicial.

Por eso la «verificación al final» no debe convertirse en un ritual independiente de la lógica. Si toda la resolución está formada por equivalencias y se conserva el dominio, las ramas finales ya describen exactamente el conjunto solución. La verificación sigue siendo útil como control, pero no es lo que convierte la respuesta en correcta.

### No hace falta construir tablas de signos

También podríamos resolver $|2x-1|=5$ separando los intervalos donde $2x-1$ es positivo o negativo. Ese método es válido, pero aquí sería innecesario y adelantaría herramientas de C22.

Las ecuaciones de esta sección se resuelven mediante equivalencias en casos. En C22 necesitaremos describir regiones completas del dominio donde una expresión sea positiva, negativa o nula; allí las tablas de signos y los intervalos tendrán una función propia.

### Un protocolo para ecuaciones con valor absoluto

Para las ecuaciones elementales de C21 seguiremos este orden:

1. fijar el dominio antes de transformar;
2. aislar, cuando sea posible, la expresión con valor absoluto;
3. si el otro miembro es una constante negativa, concluir que no hay soluciones;
4. si aparece $|A(x)|=0$, reemplazarlo por $A(x)=0$;
5. si aparece $|A(x)|=c$ con $c>0$, abrir las ramas equivalentes $A(x)=c$ o $A(x)=-c$;
6. si aparece $|A(x)|=B(x)$, conservar $B(x)\ge0$ como condición de admisibilidad;
7. si aparece $|A(x)|=|B(x)|$, usar $A(x)=B(x)$ o $A(x)=-B(x)$;
8. resolver cada rama conservando las restricciones de dominio heredadas;
9. unir los conjuntos solución de las ramas válidas;
10. comprobar en la ecuación original si alguna rama contiene además un paso sólo implicativo, o como control independiente cuando sea útil.

La estructura es

$$
\boxed{
\text{dominio}
\longrightarrow
\text{aislar}
\longrightarrow
\text{equivalencia en casos}
\longrightarrow
\text{resolver ramas}
\longrightarrow
\text{unir soluciones}.
}
$$

### Recuperación breve

Resuelva sobre $\mathbb R$ y haga explícita la equivalencia que abre cada caso.

**a)**

$$
|3x+1|=7.
$$

**b)**

$$
2|x-1|-3=5.
$$

**c)**

$$
|x+2|=|2x-1|.
$$

**Respuesta razonada.** En **a)**,

$$
|3x+1|=7
\Longleftrightarrow
3x+1=7
\quad\text{o}\quad
3x+1=-7.
$$

Las ramas dan $x=2$ y $x=-8/3$. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac83,2\right\}.
}
$$

En **b)**,

$$
2|x-1|-3=5
\Longleftrightarrow
|x-1|=4.
$$

Entonces

$$
x-1=4
\quad\text{o}\quad
x-1=-4,
$$

de modo que $x=5$ o $x=-3$. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-3,5\}.
}
$$

En **c)**,

$$
|x+2|=|2x-1|
\Longleftrightarrow
x+2=2x-1
\quad\text{o}\quad
x+2=-(2x-1).
$$

La primera rama da $x=3$. La segunda da $3x=-1$, luego $x=-1/3$. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac13,3\right\}.
}
$$

### Qué debemos conservar de esta sección

Una ecuación con valor absoluto se resuelve interpretando lo que las barras afirman, no suprimiéndolas de manera formal.

Para una constante real $c$, la ecuación $|A|=c$ tiene tres regímenes: ninguna solución si $c<0$, la condición $A=0$ si $c=0$, y dos ramas equivalentes $A=c$ o $A=-c$ si $c>0$.

Además,

$$
\boxed{
|A|=|B|
\Longleftrightarrow
A=B
\quad\text{o}\quad
A=-B.
}
$$

Cuando el segundo miembro depende de la variable, su no negatividad debe conservarse como condición de admisibilidad. Si la expresión interior tiene restricciones de dominio, esas restricciones pasan intactas a todas las ramas.

> **Las ramas de una ecuación con valor absoluto describen una unión de posibilidades equivalentes. El rigor consiste en conservarlas todas, conservar el dominio y reunir exactamente sus conjuntos solución.**

En [§21.13](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s13) estudiaremos qué ocurre cuando los coeficientes de una ecuación dependen de parámetros. Allí una misma forma podrá cambiar su conjunto solución según el valor del parámetro: en algunos casos habrá una solución, en otros ninguna y, en situaciones degeneradas, podrá aparecer todo el dominio.

## 21.13. Parámetros y familias de conjuntos solución {#apm-c21-s13}

Hasta ahora, las letras que aparecían en una ecuación representaban casi siempre cantidades que debíamos determinar. Sin embargo, una misma forma algebraica puede describir muchas ecuaciones distintas cuando alguno de sus coeficientes queda sin fijar.

Considere

$$
(a-1)x=2(a-1).
$$

Aquí $x$ será la **incógnita** y $a$ será un **parámetro**. No preguntamos por todos los pares $(a,x)$ que satisfacen la igualdad. La pregunta es otra:

> **Para cada valor fijo de $a$, ¿cuál es el conjunto solución en la variable $x$?**

Si $a\neq1$, podemos dividir por $a-1$ y obtenemos $x=2$. Pero si $a=1$, la misma división sería imposible y la ecuación se transforma en $0=0$, verdadera para todo real.

La expresión escrita es una sola. El conjunto solución cambia con el parámetro.

### Incógnita y parámetro cumplen funciones distintas

Una **incógnita** es la variable cuyos valores queremos determinar. Un **parámetro** es una cantidad que se considera fija mientras resolvemos una ecuación particular, aunque después estudiemos qué ocurre al cambiar ese valor fijo.

Podemos escribir una familia de ecuaciones como

$$
E_a(x),
$$

donde $a$ recorre un conjunto de parámetros $P$. Para cada $a\in P$, la ecuación $E_a(x)$ tiene su propio conjunto solución.

Si trabajamos sobre un dominio $D$, resulta natural definir

$$
S(a)
=
\operatorname{Sol}_D(E_a).
$$

Resolver la familia significa describir la correspondencia

$$
a\longmapsto S(a).
$$

La respuesta ya no es necesariamente un único número ni un único conjunto. Es una **familia de conjuntos solución**.

### Un primer ejemplo: el caso genérico y el caso degenerado

Volvamos a

$$
(a-1)x=2(a-1)
$$

sobre $\mathbb R$.

El factor por el que querríamos dividir es $a-1$. Por tanto, antes de dividir separamos el valor que lo anula.

Si

$$
a\neq1,
$$

entonces $a-1\neq0$ y

$$
(a-1)x=2(a-1)
\Longleftrightarrow
x=2.
$$

Así,

$$
S(a)=\{2\}.
$$

Si, en cambio,

$$
a=1,
$$

la ecuación se convierte en

$$
0\cdot x=0,
$$

es decir,

$$
0=0.
$$

Todos los reales la satisfacen:

$$
S(1)=\mathbb R.
$$

La familia completa queda descrita por

$$
\boxed{
S(a)
=
\begin{cases}
\{2\}, & a\neq1,\\[4pt]
\mathbb R, & a=1.
\end{cases}
}
$$

El valor $a=1$ es **degenerado** para esta familia porque hace desaparecer el coeficiente de la incógnita y cambia la naturaleza de la ecuación.

### La clasificación general de una ecuación lineal paramétrica

El ejemplo anterior pertenece a una forma más general. Supongamos que, para cada parámetro $a$, debemos resolver

$$
A(a)x=B(a)
$$

sobre $\mathbb R$.

La decisión central es si el coeficiente de $x$ se anula.

Si

$$
A(a)\neq0,
$$

podemos dividir y obtenemos una única solución:

$$
x=\frac{B(a)}{A(a)}.
$$

Si

$$
A(a)=0,
$$

la variable desaparece y queda la proposición

$$
0=B(a).
$$

Entonces hay dos posibilidades:

- si además $B(a)=0$, todos los reales son soluciones;
- si $B(a)\neq0$, no hay ninguna solución.

Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\left\{\dfrac{B(a)}{A(a)}\right\}, & A(a)\neq0,\\[8pt]
\mathbb R, & A(a)=0\ \text{y}\ B(a)=0,\\[4pt]
\varnothing, & A(a)=0\ \text{y}\ B(a)\neq0.
\end{cases}
}
$$

Esta clasificación resume la lógica de [§21.5](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s05), pero ahora el coeficiente puede cambiar de régimen al variar el parámetro.

### Un caso con los tres tipos de conjunto solución

Queremos ahora una familia en la que aparezcan, para distintos valores del parámetro, los tres comportamientos posibles.

Considere

$$
a(a-1)x=a-1
$$

sobre $\mathbb R$.

Los valores potencialmente excepcionales son aquellos que anulan el coeficiente de $x$:

$$
a(a-1)=0.
$$

Por producto nulo,

$$
a=0
\qquad\text{o}\qquad
a=1.
$$

Éstos son exactamente los valores que debemos separar antes de dividir.

Si

$$
a\notin\{0,1\},
$$

entonces $a(a-1)\neq0$ y podemos escribir

$$
a(a-1)x=a-1
\Longleftrightarrow
x=\frac{a-1}{a(a-1)}
=
\frac1a.
$$

Por tanto,

$$
S(a)=\left\{\frac1a\right\}.
$$

Si

$$
a=0,
$$

la ecuación se convierte en

$$
0\cdot x=-1,
$$

es decir,

$$
0=-1.
$$

No hay soluciones:

$$
S(0)=\varnothing.
$$

Si

$$
a=1,
$$

obtenemos

$$
0\cdot x=0,
$$

por lo que

$$
S(1)=\mathbb R.
$$

La clasificación completa es

$$
\boxed{
S(a)
=
\begin{cases}
\varnothing, & a=0,\\[4pt]
\mathbb R, & a=1,\\[4pt]
\left\{\dfrac1a\right\}, & a\notin\{0,1\}.
\end{cases}
}
$$

Una sola familia exhibe así tres cardinalidades radicalmente distintas: ninguna solución, una solución y todo el dominio.

### El caso genérico no autoriza a borrar los casos excepcionales

En el ejemplo anterior sería tentador cancelar el factor $a-1$ desde el comienzo:

$$
a(a-1)x=a-1
\quad\leadsto\quad
ax=1.
$$

Esa transformación presupone

$$
a-1\neq0.
$$

Por tanto, describe correctamente sólo el caso $a\neq1$. Si se utiliza sin registrar la restricción, desaparece precisamente el caso $a=1$, donde el conjunto solución es $\mathbb R$.

Después podríamos dividir por $a$, pero eso introduciría una segunda condición:

$$
a\neq0.
$$

La cadena correcta para el caso genérico es

$$
a(a-1)x=a-1
\Longleftrightarrow
ax=1
\Longleftrightarrow
x=\frac1a,
\qquad
a\notin\{0,1\}.
$$

Los valores $0$ y $1$ no son molestias que se agregan al final. Son los puntos donde las transformaciones genéricas dejan de ser reversibles.

### No toda familia necesita una separación de casos

La presencia de un parámetro no obliga a dividir automáticamente el problema en ramas.

Considere

$$
3x=a+4.
$$

El coeficiente de $x$ es la constante $3$, que nunca se anula. Para todo $a\in\mathbb R$,

$$
3x=a+4
\Longleftrightarrow
x=\frac{a+4}{3}.
$$

Por tanto,

$$
\boxed{
S(a)
=
\left\{
\frac{a+4}{3}
\right\}
\qquad
\text{para todo }a\in\mathbb R.
}
$$

Aquí el parámetro mueve la posición de la solución, pero no cambia ni la licitud de la división ni el tipo de conjunto solución.

Este contraste fija una regla importante:

> **Separamos casos cuando cambia la validez de una transformación, el dominio efectivo o la estructura del conjunto solución; no sólo porque aparece un parámetro.**

### Un parámetro puede cambiar el número de soluciones reales

Las familias paramétricas no se limitan a ecuaciones lineales.

Considere

$$
x^2=a
$$

sobre $\mathbb R$, con $a$ fijo.

Si

$$
a>0,
$$

hay dos soluciones reales:

$$
x=\sqrt a
\qquad\text{o}\qquad
x=-\sqrt a.
$$

Si

$$
a=0,
$$

la única solución es $x=0$.

Si

$$
a<0,
$$

no hay soluciones reales, porque ningún cuadrado real es negativo.

Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\{-\sqrt a,\sqrt a\}, & a>0,\\[4pt]
\{0\}, & a=0,\\[4pt]
\varnothing, & a<0.
\end{cases}
}
$$

Aquí no estamos resolviendo una inequación en $x$. Sólo usamos el signo del parámetro fijo para decidir qué forma puede tener el conjunto solución de la ecuación.

### El parámetro también puede modificar el dominio efectivo

Hasta ahora el parámetro alteraba coeficientes. También puede aparecer en una expresión cuyo dominio depende de él.

Considere

$$
\frac{x-1}{x-a}=0
$$

sobre los reales.

Para cada valor fijo de $a$, el denominador exige

$$
x\neq a.
$$

Así, el dominio efectivo es

$$
D_a=\mathbb R\setminus\{a\}.
$$

Una fracción definida vale cero exactamente cuando su numerador vale cero. El único valor algebraicamente posible es

$$
x=1.
$$

Si $a\neq1$, entonces $1\in D_a$, de modo que

$$
S(a)=\{1\}.
$$

Si $a=1$, el único valor que anularía el numerador está excluido por el denominador. En ese caso,

$$
S(1)=\varnothing.
$$

Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\{1\}, & a\neq1,\\[4pt]
\varnothing, & a=1.
\end{cases}
}
$$

Este ejemplo muestra una segunda fuente de valores excepcionales: no sólo debemos vigilar los coeficientes por los que queremos dividir; también debemos observar cuándo el parámetro cambia el dominio de la ecuación.

### Simplificar una familia no borra el dominio paramétrico

En el caso $a=1$, la ecuación anterior se convierte en

$$
\frac{x-1}{x-1}=0,
\qquad
x\neq1.
$$

Sobre su dominio,

$$
\frac{x-1}{x-1}=1,
$$

de modo que la ecuación equivale a $1=0$. No hay soluciones.

Sería incorrecto cancelar $x-1$, olvidar la exclusión y después considerar $x=1$ como candidato. La disciplina de C20 permanece intacta: el parámetro puede hacer coincidir factores, pero una simplificación no recupera puntos que nunca pertenecieron al dominio original.

### Una ecuación literal sigue siendo una ecuación en la variable elegida

Considere

$$
ax+b=c.
$$

Si la incógnita es $x$, entonces $a$, $b$ y $c$ se tratan como parámetros.

Restando $b$,

$$
ax=c-b.
$$

La clasificación depende de $a$.

Si $a\neq0$,

$$
x=\frac{c-b}{a}.
$$

Si $a=0$, la ecuación se reduce a $b=c$.

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\begin{cases}
\left\{\dfrac{c-b}{a}\right\}, & a\neq0,\\[8pt]
\mathbb R, & a=0\ \text{y}\ b=c,\\[4pt]
\varnothing, & a=0\ \text{y}\ b\neq c.
\end{cases}
}
$$

Si el problema hubiera pedido despejar $a$ en vez de $x$, la clasificación sería distinta. La palabra «parámetro» no pertenece para siempre a una letra concreta: depende de qué variable se declare como incógnita.

### Valores excepcionales y valores ordinarios

En una familia paramétrica suele ser útil distinguir dos tipos de valores.

Los **valores ordinarios** son aquellos para los cuales el procedimiento general funciona sin cambio de lógica.

Los **valores excepcionales** son aquellos en los que ocurre alguna de estas situaciones:

- se anula un coeficiente por el que el caso genérico quería dividir;
- cambia el dominio efectivo;
- desaparece la incógnita;
- una ecuación cambia de grado o de tipo;
- cambia el número o la forma de las soluciones.

No toda excepción produce una dificultad algebraica. Su importancia está en que obliga a revisar el conjunto solución por separado.

### Cómo localizar los valores excepcionales antes de resolver

Considere una familia lineal

$$
A(a)x=B(a).
$$

Antes de dividir por $A(a)$ preguntamos

$$
A(a)=0?
$$

Los valores de $a$ que resuelven esa ecuación son candidatos naturales a casos excepcionales.

Si además la familia contiene denominadores, radicales u otras expresiones con dominio restringido, debemos localizar también los valores del parámetro que alteran esas restricciones.

La estrategia consiste en analizar primero **dónde puede fallar el método genérico**. Sólo después resolvemos el caso ordinario.

Esta inversión del orden evita un error frecuente: obtener una fórmula válida bajo una condición y presentarla después como si describiera toda la familia.

### Una clasificación no es una lista de ejemplos aislados

Cuando terminamos un problema paramétrico, la respuesta debe describir todos los valores permitidos del parámetro sin huecos ni superposiciones ambiguas.

En el ejemplo

$$
a(a-1)x=a-1,
$$

la respuesta $x=1/a$ es incompleta, aunque sea correcta para la mayoría de los valores de $a$.

La respuesta completa debe especificar

$$
a=0,
\qquad
a=1,
\qquad
a\notin\{0,1\}.
$$

Estos tres casos son:

- exhaustivos: todo real pertenece a uno de ellos;
- mutuamente excluyentes: ningún real pertenece simultáneamente a dos;
- suficientes para determinar $S(a)$.

Una buena clasificación paramétrica no deja valores sin tratar y no divide en más casos de los necesarios.

### Un protocolo para ecuaciones con parámetros

Para las familias elementales de C21 seguiremos este orden:

1. identificar con claridad la incógnita y los parámetros;
2. fijar el conjunto de valores permitido para cada parámetro;
3. determinar el dominio efectivo de la ecuación para un parámetro fijo;
4. localizar las expresiones por las que el procedimiento genérico querría dividir;
5. identificar los valores del parámetro que anulan esas expresiones o cambian el dominio;
6. resolver primero el caso genérico bajo sus condiciones explícitas;
7. volver a cada valor excepcional y resolverlo sin usar la operación que allí dejó de ser válida;
8. escribir el conjunto solución correspondiente a cada caso;
9. comprobar que los casos son exhaustivos y mutuamente excluyentes;
10. presentar la familia completa como una descripción por casos de $a\longmapsto S(a)$.

La estructura conceptual es

$$
\boxed{
\text{parámetro fijo}
\longrightarrow
\text{dominio}
\longrightarrow
\text{valores excepcionales}
\longrightarrow
\text{caso genérico + casos degenerados}
\longrightarrow
S(a).
}
$$

### Recuperación breve

Para cada familia, resuelva en $x$ sobre $\mathbb R$ y describa el conjunto solución según el parámetro.

**a)**

$$
(a+2)x=6.
$$

**b)**

$$
a(a-2)x=a-2.
$$

**c)**

$$
\frac{x-3}{x-a}=0.
$$

**Respuesta razonada.** En **a)** el único valor excepcional es $a=-2$.

Si $a\neq-2$,

$$
x=\frac{6}{a+2},
$$

por lo que

$$
S(a)
=
\left\{
\frac{6}{a+2}
\right\}.
$$

Si $a=-2$, la ecuación se convierte en $0=6$, que es falsa. Así,

$$
\boxed{
S(a)
=
\begin{cases}
\left\{\dfrac{6}{a+2}\right\}, & a\neq-2,\\[8pt]
\varnothing, & a=-2.
\end{cases}
}
$$

En **b)** el coeficiente $a(a-2)$ se anula para $a=0$ y $a=2$.

Si $a\notin\{0,2\}$,

$$
a(a-2)x=a-2
\Longleftrightarrow
x=\frac1a.
$$

Si $a=0$, obtenemos $0=-2$, de modo que no hay soluciones.

Si $a=2$, obtenemos $0=0$, de modo que todos los reales son soluciones.

Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\varnothing, & a=0,\\[4pt]
\mathbb R, & a=2,\\[4pt]
\left\{\dfrac1a\right\}, & a\notin\{0,2\}.
\end{cases}
}
$$

En **c)** el dominio depende del parámetro:

$$
D_a=\mathbb R\setminus\{a\}.
$$

La fracción puede valer cero sólo si $x-3=0$, es decir, si $x=3$.

Cuando $a\neq3$, ese valor pertenece al dominio y $S(a)=\{3\}$.

Cuando $a=3$, el valor $x=3$ está excluido y no queda ninguna solución. Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\{3\}, & a\neq3,\\[4pt]
\varnothing, & a=3.
\end{cases}
}
$$

### Qué debemos conservar de esta sección

En una ecuación paramétrica no buscamos un único conjunto solución independiente de los coeficientes. Buscamos una familia

$$
a\longmapsto S(a).
$$

> **El caso genérico sólo es válido bajo las condiciones que hacen reversibles sus transformaciones. Los valores donde esas condiciones fallan deben resolverse por separado.**

Un parámetro puede cambiar la posición de las soluciones, su número, la aparición de una identidad o una contradicción e incluso el dominio efectivo de la ecuación. Por eso una clasificación completa debe cubrir todos los valores del parámetro y distinguir únicamente los casos que realmente cambian la lógica o el conjunto solución.

En [§21.14](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s14) llevaremos esta disciplina a ecuaciones simultáneas en dos variables. Allí el objeto solución ya no será un número real, sino un par ordenado, y estudiaremos sistemas algebraicos elementales no lineales mediante sustitución, eliminación y simetría.



### Un árbol de casos debe cubrir también los dominios

Resolver $A(t)x=B(t)$ obliga a separar $A(t)=0$ antes de dividir. En una ecuación racional hay otra pregunta: ¿el candidato genérico pertenece a su dominio? Para $(t-1)x/(x-t)=0$, el dominio es $x\ne t$. Si $t=1$, la ecuación es verdadera en $\mathbb R\setminus\{1\}$. Si $t\ne1$, el numerador exige $x=0$, admitido solo cuando $t\ne0$. Por tanto, $t=0$ da conjunto vacío y los demás valores distintos de $1$ dan $\{0\}$. **Control resuelto:** separar únicamente $t=1$ y $t\ne1$ es insuficiente; el segundo caso todavía contiene un candidato excluido. Las ramas deben ser disjuntas, cubrir todos los parámetros y conservar las restricciones de la ecuación original.

## 21.14. Sistemas algebraicos elementales no lineales {#apm-c21-s14}

Hasta ahora, resolver una ecuación significaba determinar un subconjunto de $\mathbb R$: los valores de una incógnita que hacían verdadera una igualdad. En un sistema de dos ecuaciones con dos incógnitas, el objeto solución cambia.

Considere

$$
\begin{cases}
x+y=5,\\
xy=6.
\end{cases}
$$

Un valor aislado de $x$ o de $y$ ya no basta. Necesitamos encontrar **pares ordenados** $(x,y)$ que satisfagan simultáneamente ambas ecuaciones.

La pregunta rectora de esta sección será:

> **¿cómo reducimos un sistema no lineal elemental a ecuaciones ya conocidas sin perder ni añadir pares solución?**

Trabajaremos sólo con sistemas que puedan resolverse mediante sustitución, eliminación elemental o simetría básica. No desarrollaremos matrices, eliminación gaussiana ni teoría sistemática de sistemas lineales.

### El conjunto solución vive en $\mathbb R^2$

Sea un sistema

$$
\begin{cases}
F(x,y)=0,\\
G(x,y)=0.
\end{cases}
$$

sobre un dominio $D\subseteq\mathbb R^2$.

Diremos que $(a,b)\in D$ es una **solución del sistema** si satisface simultáneamente

$$
F(a,b)=0
$$

y

$$
G(a,b)=0.
$$

El conjunto solución es

$$
\operatorname{Sol}_D(F=0,G=0)
=
\{(x,y)\in D:F(x,y)=0\ \text{y}\ G(x,y)=0\}.
$$

La conjunción es decisiva. Un par debe satisfacer las dos ecuaciones a la vez.

Por eso, si

$$
S_F=\{(x,y)\in D:F(x,y)=0\}
$$

y

$$
S_G=\{(x,y)\in D:G(x,y)=0\},
$$

entonces

$$
\boxed{
\operatorname{Sol}_D(F=0,G=0)
=
S_F\cap S_G.
}
$$

Resolver un sistema consiste en encontrar la intersección de dos condiciones, no en unir las soluciones de cada ecuación por separado.

### Una primera advertencia: resolver ecuaciones por separado no basta

Considere

$$
\begin{cases}
x+y=5,\\
xy=6.
\end{cases}
$$

La primera ecuación, por sí sola, tiene infinitos pares solución. La segunda también.

Pero el sistema exige los pares que satisfacen ambas simultáneamente.

No sería correcto resolver una ecuación, resolver la otra y formar una unión. La lógica del sistema es

$$
\boxed{\text{ecuación 1}\ \text{y}\ \text{ecuación 2}},
$$

no

$$
\text{ecuación 1}\ \text{o}\ \text{ecuación 2}.
$$

Esta diferencia será el equivalente bidimensional de la disciplina de conjuntos solución que ha guiado todo C21.

### Sustitución: reemplazar una variable por una expresión equivalente

Supongamos que una de las ecuaciones permite expresar una variable en función de la otra.

Considere

$$
\begin{cases}
y=x^2,\\
y=2x+3.
\end{cases}
$$

Como ambas expresiones son iguales a $y$, todo par solución debe satisfacer

$$
x^2=2x+3.
$$

Podemos escribir el sistema de manera equivalente como

$$
\begin{cases}
y=x^2,\\
x^2=2x+3.
\end{cases}
$$

La segunda ecuación se reduce a

$$
x^2-2x-3=0,
$$

y factoriza como

$$
(x-3)(x+1)=0.
$$

Por tanto,

$$
x=3
\qquad\text{o}\qquad
x=-1.
$$

Ahora reconstruimos $y$.

Si $x=3$,

$$
y=3^2=9.
$$

Si $x=-1$,

$$
y=(-1)^2=1.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(3,9),(-1,1)\}.
}
$$

Conviene verificar el orden de los pares: la primera coordenada corresponde a $x$ y la segunda a $y$.

### Sustituir no es eliminar información

La sustitución es segura cuando reemplazamos una variable mediante una igualdad equivalente ya contenida en el sistema.

Si tenemos

$$
y=H(x),
$$

entonces el sistema

$$
\begin{cases}
F(x,y)=0,\\
y=H(x)
\end{cases}
$$

puede reducirse a

$$
F(x,H(x))=0,
$$

pero la reconstrucción del par requiere volver después a

$$
y=H(x).
$$

Resolver sólo la ecuación reducida produce valores de $x$, no soluciones completas del sistema.

La estructura del método es

$$
\boxed{
(x,y)
\longrightarrow
x
\longrightarrow
\text{resolver en }x
\longrightarrow
\text{reconstruir }y
\longrightarrow
(x,y).
}
$$

### Una sustitución puede ramificar

Considere

$$
\begin{cases}
y=x^2,\\
x+y=6.
\end{cases}
$$

Sustituimos $y=x^2$ en la segunda ecuación:

$$
x+x^2=6.
$$

Por tanto,

$$
x^2+x-6=0,
$$

y

$$
(x+3)(x-2)=0.
$$

Así,

$$
x=-3
\qquad\text{o}\qquad
x=2.
$$

Volvemos a $y=x^2$:

$$
x=-3\Longrightarrow y=9,
$$

mientras que

$$
x=2\Longrightarrow y=4.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(-3,9),(2,4)\}.
}
$$

Una sola ecuación sustituida puede producir varias ramas. Cada valor de $x$ debe llevarse de vuelta al sistema para reconstruir el par correspondiente.

### Eliminación elemental: combinar ecuaciones para borrar una expresión

La sustitución no es la única ruta. A veces dos ecuaciones contienen expresiones que pueden eliminarse al sumarlas o restarlas.

Considere

$$
\begin{cases}
x^2+y^2=25,\\
x^2-y^2=7.
\end{cases}
$$

Restamos la segunda ecuación de la primera:

$$
(x^2+y^2)-(x^2-y^2)=25-7.
$$

Entonces

$$
2y^2=18,
$$

y por tanto

$$
y^2=9.
$$

Así,

$$
y=3
\qquad\text{o}\qquad
y=-3.
$$

Sustituimos $y^2=9$ en la primera ecuación:

$$
x^2+9=25,
$$

de donde

$$
x^2=16.
$$

Por tanto,

$$
x=4
\qquad\text{o}\qquad
x=-4.
$$

Como las ecuaciones originales sólo contienen $x^2$ y $y^2$, las elecciones de signo son independientes. Los cuatro pares

$$
(4,3),\quad
(4,-3),\quad
(-4,3),\quad
(-4,-3)
$$

satisfacen ambas ecuaciones.

Luego,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(4,3),(4,-3),(-4,3),(-4,-3)\}.
}
$$

La eliminación redujo el sistema, pero no reemplazó la necesidad de reconstruir todas las combinaciones válidas.

### Combinar ecuaciones debe conservar el sistema

Si de un sistema

$$
\begin{cases}
E_1,\\
E_2
\end{cases}
$$

reemplazamos $E_2$ por una combinación reversible como

$$
E_2-E_1,
$$

conservamos el conjunto solución siempre que mantengamos además una de las ecuaciones originales.

Por ejemplo,

$$
\begin{cases}
E_1,\\
E_2
\end{cases}
\Longleftrightarrow
\begin{cases}
E_1,\\
E_2-E_1.
\end{cases}
$$

La vuelta es posible porque

$$
E_2=(E_2-E_1)+E_1.
$$

En cambio, conservar sólo la ecuación combinada puede perder información. Una consecuencia del sistema no suele ser equivalente al sistema completo.

Esta observación conecta la eliminación con el eje lógico de todo el capítulo: no basta con obtener una ecuación verdadera para toda solución; debemos conservar suficiente información para recuperar el sistema original.

### El caso simétrico $x+y=s$, $xy=p$

Algunos sistemas no lineales tienen una simetría especial.

Considere

$$
\begin{cases}
x+y=5,\\
xy=6.
\end{cases}
$$

Las ecuaciones no distinguen entre $(x,y)$ y $(y,x)$. Si un par es solución, intercambiar sus coordenadas produce otra solución.

Podemos usar la primera ecuación para escribir

$$
y=5-x.
$$

Sustituyendo en $xy=6$,

$$
x(5-x)=6.
$$

Entonces

$$
5x-x^2=6,
$$

o

$$
x^2-5x+6=0.
$$

Factorizamos:

$$
(x-2)(x-3)=0.
$$

Así,

$$
x=2
\qquad\text{o}\qquad
x=3.
$$

Si $x=2$, entonces $y=3$.

Si $x=3$, entonces $y=2$.

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(2,3),(3,2)\}.
}
$$

La simetría anticipaba que las soluciones debían aparecer intercambiadas.

### La misma solución mediante una lectura simétrica

El sistema anterior admite otra lectura.

Si

$$
x+y=5
$$

y

$$
xy=6,
$$

entonces $x$ e $y$ son dos números cuya suma es $5$ y cuyo producto es $6$.

Considere el polinomio

$$
t^2-5t+6.
$$

Factoriza como

$$
(t-2)(t-3).
$$

Sus raíces son $2$ y $3$. Por tanto, las coordenadas $x$ e $y$ deben ser precisamente esos dos valores, en algún orden.

Obtenemos nuevamente

$$
\boxed{
\{(2,3),(3,2)\}.
}
$$

Esta segunda ruta no introduce una teoría nueva de polinomios. Usa únicamente la relación ya conocida entre una cuadrática factorizada y sus raíces.

La comparación de ambas rutas muestra la función de la simetría: puede permitirnos pensar primero en el **conjunto de valores de las coordenadas** y sólo después recuperar su orden.

### Simetría no significa que siempre haya dos soluciones

Considere

$$
\begin{cases}
x+y=4,\\
xy=4.
\end{cases}
$$

El polinomio asociado es

$$
t^2-4t+4=(t-2)^2.
$$

Sólo aparece el valor

$$
t=2.
$$

Por tanto,

$$
x=y=2,
$$

y el conjunto solución es

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(2,2)\}.
}
$$

Intercambiar las coordenadas no produce un par nuevo porque ambas coinciden.

### Un sistema puede no tener soluciones reales

Considere

$$
\begin{cases}
y=x^2,\\
y=-1.
\end{cases}
$$

Sustituyendo,

$$
x^2=-1.
$$

No existe ningún real que satisfaga esa igualdad. Luego,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\varnothing.
}
$$

El hecho de que cada ecuación por separado tenga soluciones no garantiza que exista un par que satisfaga ambas simultáneamente.

La ausencia de solución corresponde a una intersección vacía de las dos condiciones.

### Una ecuación reducida puede producir candidatos que deben reconstruirse como pares

Considere

$$
\begin{cases}
x^2+y=5,\\
y=1.
\end{cases}
$$

Sustituyendo $y=1$,

$$
x^2+1=5,
$$

de donde

$$
x^2=4.
$$

Así,

$$
x=2
\qquad\text{o}\qquad
x=-2.
$$

Pero la respuesta del sistema no es

$$
\{-2,2\}.
$$

Ése sería un subconjunto de $\mathbb R$, mientras que el sistema vive en $\mathbb R^2$.

Debemos reconstruir los pares:

$$
(2,1)
\qquad\text{y}\qquad
(-2,1).
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(2,1),(-2,1)\}.
}
$$

Este cambio de tipo de objeto es una de las obligaciones conceptuales centrales de la sección.

### El orden de las coordenadas importa

Un par ordenado

$$
(a,b)
$$

no es, en general, igual a

$$
(b,a).
$$

Por ejemplo,

$$
(2,3)\neq(3,2).
$$

En el sistema

$$
\begin{cases}
x+y=5,\\
xy=6,
\end{cases}
$$

ambos pares son soluciones porque el sistema es simétrico.

Pero en

$$
\begin{cases}
y=x^2,\\
x+y=6,
\end{cases}
$$

el par $(-3,9)$ es solución, mientras que $(9,-3)$ ni siquiera satisface la primera ecuación.

Por eso cada reconstrucción debe respetar qué valor pertenece a cada variable.

### Elegir entre sustitución, eliminación y simetría

No existe una ruta única para todo sistema elemental.

La **sustitución** suele ser natural cuando:

- una ecuación ya tiene una variable aislada;
- una variable aparece mediante una expresión sencilla;
- sustituir reduce el sistema a una ecuación de una sola variable.

La **eliminación elemental** suele ser natural cuando:

- las ecuaciones contienen términos iguales u opuestos;
- sumarlas o restarlas borra directamente una expresión;
- la combinación resultante conserva una ecuación original suficiente para reconstruir el sistema.

La **simetría** suele ser útil cuando:

- las ecuaciones permanecen invariantes al intercambiar $x$ e $y$;
- aparecen $x+y$ y $xy$;
- interesa comparar pares intercambiados o detectar que $x=y$ en un caso degenerado.

La elección debe responder a la estructura del sistema, no a una receta universal.

### Un protocolo para sistemas no lineales elementales

Para los sistemas de C21 seguiremos este orden:

1. fijar el dominio del sistema en $\mathbb R^2$ o en el subconjunto declarado;
2. recordar que una solución es un **par ordenado** que satisface todas las ecuaciones;
3. buscar la estructura más visible: variable aislada, términos eliminables o simetría;
4. reducir el sistema a una ecuación en una sola variable mediante una transformación equivalente o una consecuencia acompañada de información suficiente;
5. resolver esa ecuación con las herramientas ya construidas;
6. reconstruir la otra variable para cada rama;
7. formar todos los pares ordenados obtenidos;
8. comprobar que cada par satisface simultáneamente todas las ecuaciones originales;
9. eliminar duplicados si distintas ramas producen el mismo par;
10. declarar el conjunto solución como subconjunto de $\mathbb R^2$.

La estructura puede resumirse como

$$
\boxed{
\text{sistema}
\longrightarrow
\text{reducción a una variable}
\longrightarrow
\text{ramas}
\longrightarrow
\text{reconstrucción de pares}
\longrightarrow
\operatorname{Sol}\subseteq\mathbb R^2.
}
$$

### Recuperación breve

Resuelva cada sistema sobre $\mathbb R^2$.

**a)**

$$
\begin{cases}
y=x^2,\\
x+y=2.
\end{cases}
$$

**b)**

$$
\begin{cases}
x+y=7,\\
xy=12.
\end{cases}
$$

**c)**

$$
\begin{cases}
x^2+y^2=10,\\
x^2-y^2=8.
\end{cases}
$$

**Respuesta razonada.** En **a)** sustituimos $y=x^2$:

$$
x+x^2=2.
$$

Entonces

$$
x^2+x-2=0,
$$

y

$$
(x+2)(x-1)=0.
$$

Así,

$$
x=-2
\qquad\text{o}\qquad
x=1.
$$

Reconstruimos $y$:

$$
x=-2\Longrightarrow y=4,
$$

y

$$
x=1\Longrightarrow y=1.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(-2,4),(1,1)\}.
}
$$

En **b)** usamos la simetría. Los valores $x$ e $y$ deben tener suma $7$ y producto $12$, por lo que son raíces de

$$
t^2-7t+12=0.
$$

Factorizando,

$$
(t-3)(t-4)=0.
$$

Así, las coordenadas son $3$ y $4$ en algún orden:

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(3,4),(4,3)\}.
}
$$

En **c)** restamos la segunda ecuación de la primera:

$$
2y^2=2,
$$

por lo que

$$
y^2=1
$$

y

$$
y=\pm1.
$$

Sustituyendo en la primera ecuación,

$$
x^2+1=10,
$$

de modo que

$$
x^2=9
$$

y

$$
x=\pm3.
$$

Como las ecuaciones sólo dependen de los cuadrados, las elecciones de signo son independientes. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(3,1),(3,-1),(-3,1),(-3,-1)\}.
}
$$

### Qué debemos conservar de esta sección

Un sistema no lineal elemental cambia el tipo de objeto que buscamos:

$$
\boxed{
\text{una ecuación en }x
\longrightarrow
\operatorname{Sol}\subseteq\mathbb R,
\qquad
\text{un sistema en }x,y
\longrightarrow
\operatorname{Sol}\subseteq\mathbb R^2.
}
$$

> **Resolver un sistema significa determinar todos los pares ordenados que satisfacen simultáneamente todas sus ecuaciones.**

La sustitución reduce una variable y obliga a reconstruir la otra. La eliminación debe conservar información suficiente para recuperar el sistema. La simetría puede revelar pares intercambiados o reducir el problema a una cuadrática conocida.

En [§21.15](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s15) volveremos sobre todas las técnicas del capítulo desde otra perspectiva: ya no preguntaremos primero cómo resolver, sino cómo diagnosticar una resolución incorrecta localizando la **primera ruptura** donde cambió indebidamente el conjunto solución.

## 21.15. Laboratorio de errores y primera ruptura {#apm-c21-s15}

En las secciones anteriores aprendimos a resolver distintos tipos de ecuaciones y sistemas. Ahora cambiaremos deliberadamente de tarea. En vez de comenzar con un problema correcto y buscar su solución, comenzaremos con **resoluciones defectuosas** y preguntaremos:

> **¿cuál fue el primer paso en que el conjunto solución dejó de estar bajo control?**

Ésta es una habilidad distinta de calcular. Una cadena puede contener varios pasos algebraicamente impecables después de un error lógico. Si sólo miramos el final, podemos culpar a la factorización, a la fórmula cuadrática o a una simplificación que en realidad estaban bien hechas. El diagnóstico correcto exige retroceder hasta la **primera ruptura**.

### Qué llamaremos primera ruptura

Considere una cadena de ecuaciones

$$
E_0,\ E_1,\ E_2,\dots,E_n
$$

sobre un dominio vigente $D$.

Si cada transición satisface

$$
E_i\Longleftrightarrow E_{i+1}
$$

sobre $D$, todas las ecuaciones tienen el mismo conjunto solución.

Llamaremos **primera ruptura** al primer índice $i$ en que una transición deja de conservar exactamente el problema que pretendíamos resolver: puede cambiar el conjunto solución, cambiar indebidamente el dominio, omitir una rama o convertir la respuesta en un objeto de tipo distinto.

La pregunta diagnóstica no es sólo

> «¿este cálculo está bien hecho?»,

sino

> **«¿esta transición conserva exactamente el conjunto de valores —o pares— que todavía representan soluciones del problema original?»**

### Cuatro diagnósticos básicos

A lo largo del capítulo han aparecido cuatro fallas fundamentales.

**1. Creación de candidatos.** La ecuación transformada admite valores adicionales:

$$
\operatorname{Sol}(E_0)
\subsetneq
\operatorname{Sol}(E_1).
$$

Esto puede ocurrir al multiplicar por una expresión que puede anularse o al elevar al cuadrado sin conservar información suficiente.

**2. Pérdida de soluciones.** La transformación elimina valores que sí resolvían el problema original:

$$
\operatorname{Sol}(E_1)
\subsetneq
\operatorname{Sol}(E_0).
$$

Dividir o cancelar un factor que puede ser cero es el ejemplo rector.

**3. Cambio indebido de dominio.** La fórmula transformada puede ser correcta sobre el dominio original, pero se la reinterpreta después sobre un dominio mayor y se readmiten valores que nunca fueron admisibles.

**4. Pérdida de estructura de la respuesta.** En una sustitución o en un sistema se resuelve correctamente una ecuación auxiliar, pero no se reconstruyen las preimágenes o los pares ordenados que exige el problema original.

Estas cuatro fallas no se reparan del mismo modo.

### Laboratorio 1: dividir y perder una solución

Considere la resolución

$$
x(x-2)=0
$$

$$
\Longrightarrow
$$

$$
x-2=0
$$

$$
\Longrightarrow
$$

$$
x=2.
$$

El cálculo de las dos últimas líneas es correcto. El problema está antes.

La ecuación original satisface

$$
x(x-2)=0
\Longleftrightarrow
x=0\ \text{o}\ x=2.
$$

Por tanto,

$$
\operatorname{Sol}_{\mathbb R}=\{0,2\}.
$$

La transición

$$
x(x-2)=0
\quad\longrightarrow\quad
x-2=0
$$

se obtuvo dividiendo por $x$. Pero $x$ puede valer cero, y precisamente $x=0$ es una solución original.

La primera ruptura es, por tanto, la división no autorizada.

El efecto es una pérdida:

$$
\{2\}
\subsetneq
\{0,2\}.
$$

La reparación correcta es no dividir por el factor. Podemos usar producto nulo o separar previamente el caso $x=0$ del caso $x\neq0$.

### Por qué la verificación final no detecta este error

Suponga que, al terminar, comprobamos el único valor obtenido:

$$
2(2-2)=0.
$$

La comprobación confirma que $2$ es solución. Pero no informa que falta $0$.

Éste es el límite esencial de la verificación final:

> **comprobar candidatos puede eliminar valores sobrantes; no recupera automáticamente soluciones que fueron borradas antes de llegar al final.**

Por eso las pérdidas deben detectarse durante la cadena.

### Laboratorio 2: multiplicar por un posible cero y crear un candidato

Considere ahora

$$
x=3.
$$

Alguien multiplica ambos miembros por $x-1$ y escribe

$$
x(x-1)=3(x-1).
$$

Después desarrolla y factoriza:

$$
x^2-x=3x-3,
$$

$$
x^2-4x+3=0,
$$

$$
(x-1)(x-3)=0.
$$

Finalmente obtiene

$$
x=1
\qquad\text{o}\qquad
x=3.
$$

Todos los cálculos posteriores a la multiplicación son correctos. La primera ruptura está en interpretar

$$
x=3
$$

y

$$
x(x-1)=3(x-1)
$$

como ecuaciones equivalentes sobre $\mathbb R$.

La dirección segura es sólo

$$
x=3
\Longrightarrow
x(x-1)=3(x-1).
$$

Cuando $x=1$, el factor $x-1$ convierte ambos miembros de la ecuación transformada en cero, aunque la ecuación original $x=3$ sea falsa.

Por tanto,

$$
\{3\}
\subsetneq
\{1,3\}.
$$

El valor $1$ es un candidato creado en la primera transición.

Aquí sí sirve la verificación final:

$$
1\neq3,
$$

de modo que $1$ se descarta.

### La misma operación puede ser segura sobre otro dominio

El diagnóstico siempre depende del dominio.

Si el problema estuviera restringido a

$$
D=\mathbb R\setminus\{1\},
$$

entonces $x-1$ sería no nulo en todo $D$, y multiplicar por ese factor sí sería reversible sobre ese dominio.

No existe una lista de operaciones «buenas» y «malas» separada de las hipótesis. Lo que auditamos es la operación **junto con el dominio vigente**.

### Laboratorio 3: cuadrar y aceptar una raíz extraña

Considere la resolución

$$
\sqrt{x+1}=x-1
$$

$$
\Longleftrightarrow
$$

$$
x+1=(x-1)^2
$$

$$
\Longleftrightarrow
$$

$$
x(x-3)=0
$$

$$
\Longleftrightarrow
$$

$$
x=0\ \text{o}\ x=3.
$$

La factorización es correcta. También lo es el desarrollo del cuadrado. La falsa afirmación aparece en la primera doble flecha.

Elevar al cuadrado garantiza

$$
\sqrt{x+1}=x-1
\Longrightarrow
x+1=(x-1)^2,
$$

pero la vuelta requiere información de signo.

La equivalencia completa es

$$
\sqrt{x+1}=x-1
\Longleftrightarrow
\begin{cases}
x+1=(x-1)^2,\\
x-1\ge0.
\end{cases}
$$

La ecuación cuadrada produce los candidatos $0$ y $3$, pero la condición $x-1\ge0$ conserva sólo $3$.

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
\bigl(\sqrt{x+1}=x-1\bigr)
=
\{3\}.
}
$$

El candidato $0$ no estaba prohibido por el dominio. Fue creado por pérdida de información de signo.

### No toda raíz rechazada es una raíz extraña del mismo tipo

Compare el ejemplo anterior con una ecuación racional donde un valor final queda fuera del dominio.

En una ecuación radical, un valor puede pertenecer al dominio original y aparecer sólo porque una transformación implicativa amplió el conjunto de candidatos.

En una ecuación racional bien tratada, un valor puede surgir al resolver la fórmula simplificada, pero haber estado excluido desde el principio por el dominio.

Ambos valores se descartan, pero el diagnóstico lógico es diferente.

### Laboratorio 4: borrar el dominio sin cometer un error de cancelación

Considere

$$
\frac{x^2-1}{x-1}=2.
$$

El dominio original es

$$
D=\mathbb R\setminus\{1\}.
$$

Factorizamos:

$$
x^2-1=(x-1)(x+1).
$$

Sobre $D$ podemos cancelar $x-1$:

$$
\frac{x^2-1}{x-1}=2
\Longleftrightarrow
x+1=2
\qquad (x\in D).
$$

Hasta aquí **no hay error**. La cancelación es legítima porque en $D$ sabemos que $x-1\neq0$.

La ecuación lineal produce

$$
x=1.
$$

Pero

$$
1\notin D.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_D=\varnothing.
}
$$

La ruptura aparece sólo si, después de simplificar, olvidamos el dominio y reinterpretamos

$$
x+1=2
$$

como una ecuación sobre todo $\mathbb R$.

Éste es un diagnóstico importante:

> **la fórmula puede simplificarse correctamente y, sin embargo, el problema puede quedar mal resuelto si se borra el dominio sobre el que se afirmó la equivalencia.**

### Laboratorio 5: tomar una sola rama de una ecuación cuadrada

Considere

$$
x^2=9.
$$

Una resolución defectuosa escribe

$$
x=\sqrt9
$$

y concluye

$$
x=3.
$$

La primera ruptura está en reemplazar $\sqrt{x^2}$ por $x$.

En realidad,

$$
\sqrt{x^2}=|x|.
$$

Por tanto,

$$
x^2=9
\Longleftrightarrow
|x|=3
\Longleftrightarrow
x=3\ \text{o}\ x=-3.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}(x^2=9)
=
\{-3,3\}.
}
$$

El error perdió una rama completa. No produjo un candidato adicional: eliminó una solución válida.

La misma estructura aparece cuando se resuelve un producto nulo y se conserva sólo uno de los factores.

### Laboratorio 6: dividir por un parámetro y borrar el caso degenerado

Considere la familia

$$
(a-1)x=2(a-1).
$$

Una resolución automática divide por $a-1$ y concluye

$$
x=2
$$

para todo $a$.

La primera ruptura está en la división, porque no sabemos todavía que

$$
a-1\neq0.
$$

Si $a\neq1$, la división es lícita y

$$
S(a)=\{2\}.
$$

Pero si $a=1$, la ecuación original se convierte en

$$
0=0,
$$

de modo que

$$
S(1)=\mathbb R.
$$

La clasificación correcta es

$$
\boxed{
S(a)
=
\begin{cases}
\{2\}, & a\neq1,\\[4pt]
\mathbb R, & a=1.
\end{cases}
}
$$

La fórmula genérica no era falsa. Era **condicional**. El error consistió en olvidar la condición que autorizaba la división.

### Laboratorio 7: resolver la ecuación reducida y olvidar el objeto original

Considere el sistema

$$
\begin{cases}
y=x^2,\\
x+y=2.
\end{cases}
$$

Sustituyendo correctamente obtenemos

$$
x^2+x-2=0,
$$

y por tanto

$$
x=-2
\qquad\text{o}\qquad
x=1.
$$

Una respuesta defectuosa termina allí y declara

$$
\{-2,1\}
$$

como conjunto solución del sistema.

No se ha cometido un error al resolver la cuadrática. La ruptura aparece al confundir las soluciones de la ecuación reducida con las soluciones del problema original.

El sistema busca pares de $\mathbb R^2$.

Debemos reconstruir $y$:

$$
x=-2\Longrightarrow y=4,
$$

$$
x=1\Longrightarrow y=1.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R^2}
=
\{(-2,4),(1,1)\}.
}
$$

Este error no amplía ni reduce simplemente un subconjunto del mismo espacio: cambia el **tipo de objeto** que se está reportando.

### Una cadena puede tener un único error y muchos pasos correctos después

Considere

$$
x=3
$$

$$
\Longrightarrow
$$

$$
x(x-1)=3(x-1)
$$

$$
\Longleftrightarrow
$$

$$
x^2-4x+3=0
$$

$$
\Longleftrightarrow
$$

$$
(x-1)(x-3)=0
$$

$$
\Longleftrightarrow
$$

$$
x=1\ \text{o}\ x=3.
$$

Después de la primera transición, todos los pasos son equivalencias de la ecuación que reciben.

El resultado incorrecto no autoriza a afirmar que la factorización «introdujo» $1$. El valor $1$ ya estaba presente en el conjunto solución de la segunda ecuación.

El diagnóstico correcto es:

$$
\boxed{
\text{la primera ruptura fue multiplicar por }x-1
\text{ y tratar el paso como equivalencia}.
}
$$

La localización temporal del error es parte del razonamiento matemático.

### Qué puede y qué no puede reparar la verificación final

Podemos resumir el papel de la verificación.

| Falla | Efecto | ¿La verificación final puede repararla por sí sola? |
|---|---|---|
| cuadrar sin conservar signo | crea candidatos | sí, puede filtrar candidatos |
| multiplicar por posible cero | crea candidatos | sí, puede filtrar candidatos |
| dividir por posible cero | pierde soluciones | no |
| tomar una sola rama de $U^2=k$ | pierde soluciones | no |
| olvidar el dominio | readmite valores inadmisibles | una comprobación de dominio sí los detecta |
| olvidar reconstruir una sustitución o un sistema | respuesta incompleta o de tipo incorrecto | no; hay que volver a la variable o al objeto original |
| dividir por parámetro sin separar el caso nulo | pierde un régimen completo | no; hay que reabrir el caso excepcional |

Por eso la regla «compruebe siempre al final» es insuficiente como método universal.

La disciplina completa es:

$$
\boxed{
\text{control lógico durante la cadena}
\quad+\quad
\text{verificación final cuando corresponde}.
}
$$

### Un protocolo de auditoría de resoluciones

Ante una resolución sospechosa, seguiremos este orden:

1. **recuperar el problema original**, incluido su dominio;
2. **identificar el tipo de objeto buscado**: número, conjunto de números, familia paramétrica o conjunto de pares;
3. **leer la cadena desde el comienzo**, no desde el resultado final;
4. **clasificar cada flecha** como equivalencia, implicación o transición condicionada;
5. **detenerse en la primera transición no justificada**;
6. **describir su efecto**: candidatos extra, soluciones perdidas, dominio borrado, rama omitida o reconstrucción incompleta;
7. **reparar localmente ese paso**, sin reescribir innecesariamente toda la resolución;
8. **continuar desde la reparación** conservando dominio y condiciones;
9. **verificar candidatos** si alguna transición sólo amplió el conjunto;
10. **declarar el conjunto solución exacto** en el espacio correcto.

Este protocolo puede representarse como

$$
\boxed{
\text{problema original}
\longrightarrow
\text{auditar flechas}
\longrightarrow
\text{primera ruptura}
\longrightarrow
\text{clasificar el daño}
\longrightarrow
\text{reparar}
\longrightarrow
\text{solución exacta}.
}
$$

### Recuperación breve

En cada resolución defectuosa, localice la primera ruptura, clasifique el error y dé el conjunto solución correcto.

**a)**

$$
x(x+4)=0
\quad\longrightarrow\quad
x+4=0
\quad\longrightarrow\quad
x=-4,
$$

donde el primer paso se obtuvo dividiendo por $x$.

**b)**

$$
\sqrt{x+2}=x
\Longleftrightarrow
x+2=x^2
\Longleftrightarrow
(x-2)(x+1)=0
\Longleftrightarrow
x=2\ \text{o}\ x=-1.
$$

**c)**

$$
\frac{x^2-4}{x-2}=4
\Longleftrightarrow
x+2=4
\Longleftrightarrow
x=2,
$$

sin conservar ninguna restricción de dominio.

**d)**

$$
(m-1)x=m-1
\Longleftrightarrow
x=1
$$

para todo $m$.

**Respuesta razonada.** En **a)** la ecuación original satisface

$$
x(x+4)=0
\Longleftrightarrow
x=0\ \text{o}\ x=-4.
$$

Dividir por $x$ elimina la rama $x=0$. La primera ruptura es una **pérdida de solución**. Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-4,0\}.
}
$$

En **b)** cuadrar sin conservar la condición $x\ge0$ sólo produce una implicación. La ecuación cuadrada da los candidatos $2$ y $-1$, pero

$$
\sqrt{-1+2}=1\neq-1.
$$

El valor $-1$ es un **candidato extra**. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{2\}.
}
$$

En **c)** el dominio original es

$$
D=\mathbb R\setminus\{2\}.
$$

Sobre ese dominio, cancelar $x-2$ es válido:

$$
\frac{x^2-4}{x-2}=4
\Longleftrightarrow
x+2=4
\qquad (x\in D).
$$

La ecuación reducida produce $x=2$, pero $2\notin D$. El error fue **borrar el dominio después de simplificar**, no la cancelación misma. Por tanto,

$$
\boxed{
\operatorname{Sol}_D
=
\varnothing.
}
$$

En **d)** dividir por $m-1$ sólo está permitido cuando $m\neq1$.

Si $m\neq1$,

$$
x=1.
$$

Si $m=1$, la ecuación original se convierte en $0=0$ y todo real es solución. Luego,

$$
\boxed{
S(m)
=
\begin{cases}
\{1\}, & m\neq1,\\[4pt]
\mathbb R, & m=1.
\end{cases}
}
$$

### Qué debemos conservar de esta sección

Una resolución incorrecta no se diagnostica buscando «el último lugar donde algo parece raro». Debemos localizar la primera transición donde la cadena dejó de conservar el problema original.

> **La primera ruptura explica el error; los pasos correctos que vienen después sólo propagan sus consecuencias.**

Crear candidatos, perder soluciones, borrar el dominio, omitir una rama y olvidar reconstruir el objeto original son fallas diferentes. También requieren reparaciones diferentes.

La idea que resume todo el laboratorio es

$$
\boxed{
\text{dominio}
+
\text{tipo de objeto}
+
\text{fuerza lógica de cada transición}
=
\text{trazabilidad del conjunto solución}.
}
$$

En [§21.16](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s16) reuniremos todo C21 en un protocolo único de resolución autónoma. El objetivo ya no será aprender una nueva clase de ecuaciones, sino decidir por cuenta propia qué estructura usar, qué transformaciones son equivalentes, cuándo aparecen candidatos y cómo entregar un conjunto solución completamente justificado antes de pasar a las inequaciones de C22.

## 21.16. Síntesis y puente a C22 {#apm-c21-s16}

C21 comenzó con una pregunta aparentemente elemental: ¿qué significa resolver una ecuación? A lo largo de quince secciones la respuesta se volvió más precisa. Resolver no es simplemente «despejar» una incógnita ni ejecutar una secuencia de operaciones aprendidas de memoria.

Resolver significa **determinar exactamente un conjunto solución y conservar su trazabilidad durante todas las transformaciones**.

La pregunta final del capítulo será, por tanto, más estratégica:

> **Cuando el método no viene anunciado, ¿cómo decidimos qué hacer sin perder el dominio, las soluciones ni la lógica de la transformación?**

Esta sección reunirá las herramientas de C21 en un único protocolo autónomo.

### El objeto final gobierna todo el proceso

Antes de elegir una técnica debemos saber qué objeto buscamos.

Para una ecuación en una variable sobre un dominio $D$,

$$
\operatorname{Sol}_D(E=F)
=
\{x\in D:E(x)=F(x)\}.
$$

Para una familia paramétrica $E_a(x)$ buscamos una correspondencia

$$
a\longmapsto S(a).
$$

Para un sistema en dos variables, el conjunto solución vive en un subconjunto de $\mathbb R^2$.

Esta distinción parece elemental, pero evita varias respuestas incompletas: terminar en una variable auxiliar, olvidar las preimágenes de una sustitución, entregar sólo valores de $x$ para un sistema o presentar una fórmula genérica sin los casos excepcionales del parámetro.

La primera pregunta de una resolución autónoma será siempre:

> **¿qué tipo de objeto debe aparecer en la respuesta final?**

### El dominio se fija antes de transformar

La segunda pregunta es:

> **¿dónde tiene sentido el problema original?**

Si aparecen denominadores, radicales u otras expresiones restringidas, el dominio efectivo debe establecerse antes de simplificar.

Por ejemplo,

$$
\frac{x^2-1}{x-1}=4
$$

no es una ecuación sobre todo $\mathbb R$, sino sobre

$$
D=\mathbb R\setminus\{1\}.
$$

La factorización

$$
x^2-1=(x-1)(x+1)
$$

permite escribir, sobre $D$,

$$
\frac{x^2-1}{x-1}=4
\Longleftrightarrow
x+1=4.
$$

Entonces

$$
x=3,
$$

y como $3\in D$,

$$
\boxed{
\operatorname{Sol}_D=\{3\}.
}
$$

La simplificación hizo desaparecer el denominador de la escritura, pero no el dominio del problema.

### Reconocer estructura antes de elegir una técnica

Una ecuación no debería resolverse buscando de inmediato «qué fórmula usar». Primero conviene preguntar qué estructura está visible.

| Estructura visible | Herramienta natural | Control principal |
|---|---|---|
| forma lineal | reunir términos y despejar | coeficiente no nulo / casos degenerados |
| producto igualado a cero | producto nulo | conservar todas las ramas |
| cuadrática | factorizar, completar cuadrados o fórmula | dominio y discriminante real |
| expresión repetida | sustitución | imagen y preimágenes |
| cocientes | dominio y eliminación de denominadores | denominadores no nulos |
| radical principal | aislar, controlar signo, cuadrar | equivalencia frente a implicación |
| valor absoluto | equivalencia en casos | unión de ramas y admisibilidad |
| parámetros | separar valores excepcionales | no dividir por expresiones que pueden anularse |
| sistema elemental | sustitución, eliminación o simetría | reconstruir pares ordenados |

La tabla no es un algoritmo rígido. Es un **mapa de reconocimiento**.

Una misma ecuación puede admitir varias rutas. El criterio de elección es qué representación hace visible la estructura con menor riesgo lógico y menor carga algebraica.

### La técnica y la fuerza lógica son preguntas diferentes

Después de elegir una transformación debemos preguntar algo independiente:

> **¿el paso es reversible sobre el dominio vigente?**

Si lo es, podemos escribir

$$
E_0\Longleftrightarrow E_1.
$$

Entonces ambos problemas tienen exactamente el mismo conjunto solución.

Si sólo sabemos

$$
E_0\Longrightarrow E_1,
$$

las soluciones de $E_1$ son, en principio, candidatos para $E_0$.

Si sólo conocemos la implicación inversa,

$$
E_1\Longrightarrow E_0,
$$

la transformación puede haber perdido soluciones originales.

Esta distinción acompaña cualquier técnica. Factorizar puede ser una equivalencia; dividir por un factor puede no serlo. Eliminar denominadores puede ser una equivalencia sobre el dominio efectivo; elevar al cuadrado puede ser sólo una implicación si no conservamos las condiciones de signo.

No existe una «técnica correcta» separada de su justificación lógica.

### El protocolo rector de C21

Podemos condensar el capítulo completo en diez decisiones.

1. **Identificar el objeto buscado.** Determinar si la respuesta será un subconjunto de $\mathbb R$, una familia de conjuntos solución o un conjunto de pares.
2. **Fijar el dominio original.** Registrar todas las restricciones antes de transformar.
3. **Reconocer la estructura.** Buscar linealidad, producto nulo, cuadrática, expresión repetida, cociente, radical, valor absoluto, parámetro o sistema.
4. **Elegir una representación útil.** Factorizar, aislar, sustituir, completar cuadrados o combinar ecuaciones sólo cuando la nueva forma haga más visible el problema.
5. **Clasificar cada transición.** Escribir $\Longleftrightarrow$ sólo cuando la transformación sea reversible bajo las hipótesis vigentes.
6. **Conservar condiciones laterales.** No nulidad, dominio, signo, imagen de una sustitución y valores excepcionales de parámetros acompañan la cadena.
7. **Resolver todas las ramas.** Una disyunción exige unión de soluciones; un sistema exige simultaneidad; una sustitución exige volver a la variable original.
8. **Tratar los resultados finales según la fuerza lógica de la cadena.** Si hubo sólo implicaciones, los resultados son candidatos hasta ser filtrados.
9. **Verificar cuando corresponda.** La comprobación sirve para candidatos creados, pero no reemplaza el control de pérdidas de soluciones.
10. **Declarar el conjunto solución exacto.** La respuesta final debe conservar dominio, tipo de objeto y condiciones relevantes.

La estructura global es

$$
\boxed{
\text{objeto}
\longrightarrow
\text{dominio}
\longrightarrow
\text{estructura}
\longrightarrow
\text{representación}
\longrightarrow
\text{fuerza lógica}
\longrightarrow
\text{ramas/candidatos}
\longrightarrow
\text{reconstrucción}
\longrightarrow
\text{conjunto solución}.
}
$$

### Una resolución de síntesis

Resolvamos sobre los reales

$$
\frac{x^2-1}{x-1}
=
\sqrt{2x+8}.
$$

Este problema combina dominio racional, simplificación y una ecuación radical.

**1. Dominio.** El denominador exige

$$
x\neq1.
$$

La raíz exige

$$
2x+8\ge0,
$$

es decir,

$$
x\ge-4.
$$

Por tanto,

$$
D=[-4,\infty)\setminus\{1\}.
$$

**2. Simplificación sobre el dominio.** Factorizamos

$$
x^2-1=(x-1)(x+1).
$$

Como $x\neq1$ en $D$,

$$
\frac{x^2-1}{x-1}=x+1.
$$

Así,

$$
\frac{x^2-1}{x-1}
=
\sqrt{2x+8}
\Longleftrightarrow
x+1=\sqrt{2x+8}
\qquad (x\in D).
$$

**3. Condición de signo.** La raíz principal es no negativa. Para conservar equivalencia al cuadrar necesitamos

$$
x+1\ge0.
$$

Por tanto,

$$
x+1=\sqrt{2x+8}
\Longleftrightarrow
\begin{cases}
(x+1)^2=2x+8,\\
x+1\ge0,
\end{cases}
$$

sobre $D$.

**4. Ecuación algebraica.** Desarrollamos:

$$
x^2+2x+1=2x+8,
$$

de donde

$$
x^2=7.
$$

Así,

$$
x=\sqrt7
\qquad\text{o}\qquad
x=-\sqrt7.
$$

**5. Filtrado por las condiciones conservadas.**

Ambos valores pertenecen al dominio $D$, porque son mayores que $-4$ y ninguno es $1$.

Pero

$$
-\sqrt7+1<0,
$$

por lo que $-\sqrt7$ no satisface la condición $x+1\ge0$.

En cambio,

$$
\sqrt7+1>0.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_D
=
\{\sqrt7\}.
}
$$

Aquí no fue necesario realizar una comprobación ciega de todos los resultados en la ecuación original: la cadena conservó explícitamente el dominio y la condición de signo que restauraba equivalencia. Una comprobación directa sigue siendo un control independiente válido.

### Qué aprendemos del ejemplo de síntesis

En la resolución anterior aparecieron varias herramientas, pero sólo un principio rector.

- El dominio se fijó antes de cancelar.
- La cancelación fue equivalente porque el factor era no nulo en el dominio.
- El radical se aisló antes de cuadrar.
- La condición de signo se conservó para recuperar una equivalencia exacta.
- La ecuación cuadrada produjo dos valores, pero sólo uno sobrevivió a las condiciones del problema.
- La respuesta se declaró como conjunto solución sobre el dominio original.

La técnica cambió durante la resolución; la obligación lógica permaneció constante.

### Cuando dos rutas son posibles

Considere

$$
x^2-5x+6=0.
$$

Podemos factorizar:

$$
(x-2)(x-3)=0,
$$

y obtener

$$
\{2,3\}.
$$

También podemos usar la fórmula cuadrática. El discriminante es

$$
\Delta=25-24=1,
$$

y obtenemos nuevamente

$$
\{2,3\}.
$$

La existencia de dos rutas no significa que debamos ejecutar ambas siempre.

Una segunda ruta es especialmente útil cuando:

- queremos verificar un resultado independiente;
- una primera ruta contiene una transformación delicada;
- la estructura permite comparar eficiencia;
- el problema pide justificar una estrategia.

En otros casos, una sola ruta completamente trazable es suficiente.

### Elegir la ruta más segura puede ser mejor que elegir la más corta

Una resolución con menos líneas no es automáticamente mejor.

Dividir por un factor para «ahorrar pasos» puede perder una solución. Cuadrar antes de aislar un radical puede ocultar la condición de signo. Aplicar la fórmula cuadrática a una expresión fácilmente factorizable puede aumentar el cálculo sin aportar claridad.

Por eso, en C21 la eficiencia no significa minimizar símbolos. Significa minimizar trabajo **sin sacrificar trazabilidad**.

Podemos expresar el criterio así:

$$
\boxed{
\text{buena estrategia}
=
\text{estructura visible}
+
\text{transformaciones seguras}
+
\text{reconstrucción completa}.
}
$$

### Un árbol de preguntas para problemas no anunciados

Cuando una ecuación nueva no indique método, puede ser útil recorrer este árbol conceptual:

1. ¿Cuál es el dominio?
2. ¿Qué objeto debo entregar al final?
3. ¿Puedo simplificar sin cambiar el dominio?
4. ¿Hay un producto igualado a cero?
5. ¿La ecuación es lineal o cuadrática, o se vuelve una de ellas mediante sustitución?
6. ¿Hay denominadores que conviene eliminar sobre un dominio ya fijado?
7. ¿Hay un radical que conviene aislar?
8. ¿Hay valor absoluto que exija abrir ramas equivalentes?
9. ¿Hay un parámetro que pueda anular un coeficiente o divisor?
10. ¿Es un sistema que permite reducir una variable?
11. ¿La transformación que quiero hacer es reversible?
12. Si no lo es, ¿estoy creando candidatos o perdiendo soluciones?
13. ¿Debo reconstruir preimágenes, ramas o pares?
14. ¿Qué conjunto solución exacto queda al final?

Estas preguntas no reemplazan el conocimiento técnico. Lo organizan.

### El puente conceptual hacia C22

Hasta ahora hemos preguntado principalmente **dónde una expresión es igual a otra**.

Una ecuación

$$
E(x)=F(x)
$$

puede escribirse como

$$
E(x)-F(x)=0.
$$

El conjunto solución está formado por los puntos donde una diferencia se anula.

En C22 cambia la relación lógica. Preguntaremos, por ejemplo, dónde

$$
E(x)-F(x)>0,
$$

dónde

$$
E(x)-F(x)<0,
$$

o dónde se cumple una condición no estricta.

La transición es profunda: ya no bastará localizar puntos aislados donde una expresión vale cero. Tendremos que describir **regiones completas del dominio** en las que una expresión conserve determinado signo u orden.

### Los ceros seguirán siendo importantes, pero cambiará su función

Considere un producto

$$
(x-2)(x+1).
$$

En C21, la ecuación

$$
(x-2)(x+1)=0
$$

se resuelve localizando sus ceros:

$$
x=2
\qquad\text{o}\qquad
x=-1.
$$

En C22, si preguntamos cuándo

$$
(x-2)(x+1)>0,
$$

los ceros seguirán siendo puntos críticos, pero ya no serán por sí solos la respuesta. Habrá que estudiar qué ocurre **entre** ellos y fuera de ellos.

Éste es el lugar natural para introducir intervalos, particiones del dominio y tablas de signos.

C21 no desarrollará todavía ese método.

### Las condiciones de signo dejan de ser auxiliares

En [§21.11](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s11) usamos condiciones como

$$
S(x)\ge0
$$

para garantizar la admisibilidad de una raíz principal.

En [§21.12](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md#apm-c21-s12) usamos la no negatividad del segundo miembro para interpretar ecuaciones con valor absoluto.

Hasta ahora esas condiciones de orden aparecían como auxiliares dentro de problemas cuyo objetivo final era una igualdad.

En C22 pasarán a ser el objeto principal:

> ya no preguntaremos sólo qué valores hacen verdadera una igualdad, sino qué subconjuntos del dominio hacen verdadera una relación de orden.

Éste es el puente entre ambos capítulos.

### Recuperación breve

En cada caso, identifique primero el dominio y la estructura; después resuelva justificando las transformaciones.

**a)**

$$
\frac{x^2-4}{x-2}=5.
$$

**b)**

$$
\sqrt{x+5}=x-1.
$$

**c)** Para cada $a\in\mathbb R$, resuelva en $x$:

$$
(a-2)x=a-2.
$$

**Respuesta razonada.** En **a)** el dominio es

$$
D=\mathbb R\setminus\{2\}.
$$

Factorizamos

$$
x^2-4=(x-2)(x+2).
$$

Sobre $D$ podemos cancelar $x-2$ y escribir

$$
\frac{x^2-4}{x-2}=5
\Longleftrightarrow
x+2=5.
$$

Entonces $x=3$, que pertenece a $D$. Por tanto,

$$
\boxed{
\operatorname{Sol}_D=\{3\}.
}
$$

En **b)** la raíz principal exige que el segundo miembro sea no negativo en cualquier solución:

$$
x-1\ge0.
$$

Con esa condición,

$$
\sqrt{x+5}=x-1
\Longleftrightarrow
\begin{cases}
x+5=(x-1)^2,\\
x-1\ge0.
\end{cases}
$$

La ecuación cuadrada da

$$
x+5=x^2-2x+1,
$$

por lo que

$$
x^2-3x-4=0.
$$

Factorizamos:

$$
(x-4)(x+1)=0.
$$

Los candidatos algebraicos son $4$ y $-1$, pero sólo $4$ satisface $x-1\ge0$. Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\{4\}.
}
$$

En **c)** debemos separar el valor del parámetro que anula el coeficiente.

Si $a\neq2$, podemos dividir por $a-2$:

$$
x=1.
$$

Si $a=2$, la ecuación se convierte en

$$
0=0,
$$

y todos los reales son soluciones.

Por tanto,

$$
\boxed{
S(a)
=
\begin{cases}
\{1\}, & a\neq2,\\[4pt]
\mathbb R, & a=2.
\end{cases}
}
$$

### Qué debemos conservar de C21

El capítulo entero puede resumirse en una sola obligación:

> **Resolver significa preservar y determinar exactamente el conjunto solución sobre el dominio correcto.**

Para lograrlo debemos conservar simultáneamente:

- el dominio de procedencia;
- el tipo de objeto buscado;
- la estructura algebraica útil;
- las hipótesis que hacen reversibles las operaciones;
- la diferencia entre equivalencia e implicación;
- todas las ramas válidas;
- las condiciones de admisibilidad;
- las preimágenes y pares que deban reconstruirse;
- la distinción entre candidatos y soluciones.

La síntesis final es

$$
\boxed{
\text{dominio}
\longrightarrow
\text{estructura}
\longrightarrow
\text{transformaciones justificadas}
\longrightarrow
\text{candidatos o ramas}
\longrightarrow
\text{filtrado/reconstrucción}
\longrightarrow
\text{conjunto solución}.
}
$$

C22 conservará esta disciplina, pero cambiará la pregunta. En vez de buscar solamente los puntos donde una expresión se anula o dos expresiones coinciden, estudiaremos regiones del dominio determinadas por relaciones de orden. Allí los ceros, los intervalos y el signo se convertirán en herramientas centrales.

# Ejercicios

## A. Lectura: dominio, verdad y equivalencia

En este primer bloque no se busca todavía velocidad de cálculo. El objetivo es leer con precisión qué afirma cada ecuación, sobre qué dominio se interpreta y qué relación lógica existe entre distintas escrituras.

**1.** Considere la ecuación

$$
2x+1=7
$$

sobre $\mathbb R$.

a) Determine si la proposición es verdadera o falsa cuando $x=3$.

b) Determine si es verdadera o falsa cuando $x=4$.

c) Explique cuál de esos valores pertenece al conjunto solución y por qué comprobar un solo valor no basta, en general, para resolver una ecuación.

**2.** Considere la misma ecuación

$$
x^2=4
$$

en cada uno de los siguientes dominios:

a) $D_1=\mathbb R$;

b) $D_2=[0,\infty)$;

c) $D_3=(0,2)$.

Escriba el conjunto solución en cada caso y explique qué cambia entre los tres problemas aunque la igualdad escrita sea la misma.

**3.** Se pide estudiar

$$
\frac{1}{x-2}=3,
\qquad
x\in[0,5].
$$

a) Identifique el dominio ambiente.

b) Determine el dominio efectivo.

c) Explique por qué $x=2$ no debe describirse como una «solución que no funciona».

No resuelva todavía la ecuación.

**4.** Considere

$$
\frac{x-1}{x-1}=1.
$$

a) Determine su dominio natural.

b) Simplifique la expresión sobre ese dominio.

c) Escriba el conjunto solución exacto.

d) Explique por qué la respuesta no es $\mathbb R$ aunque la fórmula simplificada sea $1=1$.

**5.** Para cada par de ecuaciones sobre $\mathbb R$, compare sus conjuntos solución y decida si corresponde escribir $\Longleftrightarrow$, sólo $\Longrightarrow$ desde la primera ecuación, o sólo $\Longleftarrow$ desde la primera.

a)

$$
x+4=9
\qquad\text{y}\qquad
x=5.
$$

b)

$$
x=3
\qquad\text{y}\qquad
x^2=9.
$$

c)

$$
x(x+1)=0
\qquad\text{y}\qquad
x+1=0.
$$

En cada caso, justifique la dirección de la flecha mediante inclusión o igualdad de conjuntos solución.

**6.** Compare, sobre $\mathbb R$, las ecuaciones

$$
x=2
$$

y

$$
x^2=2x.
$$

a) Determine el conjunto solución de cada una.

b) Decida cuál conjunto está contenido en cuál.

c) Explique qué valor aparece al pasar de la primera ecuación a la segunda y por qué debe llamarse **candidato adicional** si la segunda se obtuvo multiplicando por $x$.

**7.** Sea

$$
D=\mathbb R\setminus\{4\}.
$$

Compare las ecuaciones

$$
\frac{2}{x-4}=5
$$

y

$$
2=5(x-4).
$$

a) Explique por qué son equivalentes sobre $D$.

b) Explique por qué la afirmación de equivalencia debe conservar explícitamente el dominio $D$.

c) ¿Qué problema tendría afirmar sin más que ambas ecuaciones son equivalentes «sobre $\mathbb R$»?

**8.** Considere

$$
\frac{x+1}{x-2}=0
$$

sobre su dominio natural.

Clasifique cada uno de los valores $-1$, $2$ y $0$ como:

- solución;
- valor admisible que no es solución;
- valor inadmisible.

Justifique cada clasificación distinguiendo con claridad «no satisface la ecuación» de «no pertenece al dominio».

**9.** Una estudiante escribe

$$
x=1
\Longleftrightarrow
x^2=1.
$$

a) Determine el conjunto solución de cada ecuación sobre $\mathbb R$.

b) Explique por qué la doble flecha es incorrecta.

c) Reemplace la doble flecha por la flecha correcta.

d) Indique qué inclusión entre conjuntos solución expresa esa flecha.

**10.** Considere la transformación

$$
x(x-2)=0
\quad\longrightarrow\quad
x-2=0,
$$

obtenida dividiendo por $x$.

a) Determine el conjunto solución de la ecuación original.

b) Determine el conjunto solución de la ecuación transformada.

c) Explique por qué la transformación no conserva equivalencia.

d) Escriba la dirección de implicación que sí es válida.

e) Indique qué solución se pierde y por qué una comprobación final del valor que sobrevivió no permitiría recuperarla.



## B. Fluidez: lineales, producto nulo y cuadráticas

En los ejercicios 11–26 el objetivo principal es ejecutar con soltura procedimientos ya justificados en la teoría. Salvo que se indique otra cosa, trabaje sobre $\mathbb R$ y declare siempre el conjunto solución.

**11.** Resuelva:

$$
7x-11=24.
$$

**12.** Resuelva:

$$
5x+8=2x-13.
$$

**13.** Resuelva:

$$
\frac{3x-2}{4}-\frac{x+1}{2}=5.
$$

**14.** Determine el conjunto solución de

$$
6(x-2)+3=6x-9.
$$

Clasifique el resultado como ecuación con solución única, identidad o contradicción.

**15.** Determine el conjunto solución de

$$
4(2x+1)=8x+11.
$$

Clasifique el resultado como ecuación con solución única, identidad o contradicción.

**16.** Resuelva mediante la propiedad del producto nulo:

$$
(3x-2)(x+5)=0.
$$

**17.** Resuelva:

$$
x(x-4)(2x+3)=0.
$$

**18.** Resuelva sin dividir por ningún factor:

$$
(x-1)^2(x+6)=0.
$$

**19.** Lleve primero la ecuación a cero y resuelva por factorización:

$$
x^2=7x-12.
$$

**20.** Resuelva por factorización:

$$
6x^2-x-2=0.
$$

**21.** Resuelva completando cuadrados:

$$
x^2+8x+7=0.
$$

**22.** Resuelva completando cuadrados:

$$
x^2-6x-2=0.
$$

**23.** Resuelva la ecuación

$$
x^2-10x+21=0
$$

por dos rutas:

a) factorización;

b) completar cuadrados.

Compruebe que ambas rutas producen el mismo conjunto solución.

**24.** Use la fórmula cuadrática para resolver

$$
3x^2-2x-8=0.
$$

Calcule primero el discriminante.

**25.** Use el discriminante para clasificar el número de soluciones reales y luego resuelva:

$$
9x^2+12x+4=0.
$$

**26.** Calcule el discriminante y determine el conjunto solución real de

$$
2x^2-4x+7=0.
$$



## C. Justificación: hipótesis y transformaciones

En los ejercicios 27–38 no basta con obtener el conjunto solución. En cada resolución deberá indicarse **por qué** la transformación usada es equivalente, o qué condición adicional permite recuperar la equivalencia.

**27.** Resuelva sobre $\mathbb R$:

$$
x(x-3)=2x.
$$

No divida directamente por $x$. Transforme primero la ecuación mediante equivalencias y explique por qué su procedimiento conserva todas las soluciones.

**28.** Sea

$$
D=\mathbb R\setminus\{1\}.
$$

Resuelva sobre $D$:

$$
(x-1)(2x+3)=7(x-1).
$$

Justifique explícitamente por qué dividir ambos miembros por $x-1$ es una transformación equivalente sobre este dominio.

**29.** Resuelva sobre $\mathbb R$ mediante la sustitución

$$
u=x^2:
$$

$$
x^4-10x^2+9=0.
$$

Indique:

a) qué restricción hereda la variable auxiliar $u$;

b) cuáles soluciones de la ecuación en $u$ son realizables;

c) todas las preimágenes reales que deben reconstruirse.

**30.** Resuelva sobre $\mathbb R$ mediante

$$
u=2x-1:
$$

$$
(2x-1)^2-7(2x-1)+10=0.
$$

Explique por qué cada valor real de $u$ produce una única preimagen real en $x$ y por qué la sustitución no introduce ramificación adicional.

**31.** Resuelva sobre $\mathbb R$:

$$
\frac{x+2}{x-3}=4.
$$

Antes de eliminar el denominador:

a) determine el dominio efectivo;

b) explique por qué multiplicar por $x-3$ es una equivalencia sobre ese dominio;

c) declare el conjunto solución sobre el dominio original.

**32.** Resuelva sobre $\mathbb R$:

$$
\frac{1}{x-2}+\frac{1}{x+2}=1.
$$

Debe indicar el dominio efectivo, elegir un multiplicador común y justificar por qué dicho multiplicador es no nulo en todo el dominio vigente antes de eliminar denominadores.

**33.** Resuelva sobre $\mathbb R$:

$$
\frac{x^2-4}{x-2}=4.
$$

Fije primero el dominio y después simplifique. Explique por qué la cancelación es válida sobre el dominio efectivo aunque la ecuación simplificada produzca un valor que no pertenece a ese dominio.

**34.** Resuelva sobre $\mathbb R$:

$$
\sqrt{2x+3}=5.
$$

Determine primero el dominio y explique por qué, en este caso, elevar al cuadrado puede escribirse como una equivalencia y no sólo como una implicación.

**35.** Resuelva sobre $\mathbb R$:

$$
\sqrt{x+4}=x.
$$

Use la equivalencia completa para una raíz principal aislada:

$$
\sqrt{R(x)}=S(x)
\Longleftrightarrow
\bigl(R(x)=S(x)^2\ \text{y}\ S(x)\ge0\bigr).
$$

Identifique con precisión la condición de signo que debe acompañar al cuadrado y úsela para filtrar la ecuación algebraica resultante.

**36.** Resuelva sobre $\mathbb R$:

$$
\sqrt{x+8}=\sqrt{3x+2}.
$$

Determine el dominio común de ambas raíces y justifique por qué, dentro de ese dominio, elevar ambos miembros al cuadrado es reversible.

**37.** Resuelva sobre $\mathbb R$:

$$
3|2x-1|-2=10.
$$

Aísle primero el valor absoluto y escriba explícitamente la equivalencia que abre las dos ramas. Explique por qué aquí no se están generando candidatos adicionales.

**38.** Resuelva sobre $\mathbb R$:

$$
|x-3|=x+1.
$$

Antes de abrir las ramas:

a) indique la condición de admisibilidad que debe satisfacer el segundo miembro;

b) escriba una formulación equivalente del problema usando esa condición;

c) resuelva las ramas y conserve sólo los valores que satisfacen todas las condiciones acumuladas.



## D. Diagnóstico: localizar la primera ruptura

En los ejercicios 39–50 se presenta una resolución defectuosa. No basta con indicar que «está mal». En cada caso:

1. localice la **primera ruptura**;
2. clasifique el daño: candidato adicional, solución perdida, dominio omitido, rama omitida o reconstrucción incompleta;
3. escriba la relación lógica correcta en el paso problemático;
4. repare la resolución y declare el conjunto solución exacto.

**39.** Se propone:

$$
(x-4)(x+1)=0
\Longleftrightarrow
x+1=0
\Longleftrightarrow
x=-1,
$$

donde el primer paso se obtuvo dividiendo por $x-4$.

Diagnostique la resolución. Compare los conjuntos solución antes y después de la división e identifique qué solución se perdió.

**40.** Se propone:

$$
x(x-5)=0
\Longleftrightarrow
x-5=0
\Longleftrightarrow
x=5.
$$

Luego se verifica

$$
5(5-5)=0
$$

y se concluye que la respuesta es correcta.

Explique por qué la verificación final de $x=5$ no basta para detectar el error cometido en la primera transición. Repare la resolución completa.

**41.** Partiendo de

$$
2x=8,
$$

una estudiante multiplica ambos miembros por $x-3$ y escribe

$$
2x=8
\Longleftrightarrow
2x(x-3)=8(x-3).
$$

Después factoriza y obtiene dos valores.

Determine qué valor adicional puede aparecer, explique por qué la doble flecha es incorrecta y escriba la dirección de implicación válida.

**42.** Se resuelve

$$
\sqrt{x+6}=x
$$

mediante la cadena

$$
\sqrt{x+6}=x
\Longleftrightarrow
x+6=x^2
\Longleftrightarrow
(x-3)(x+2)=0
\Longleftrightarrow
x=3\ \text{o}\ x=-2.
$$

Localice la primera ruptura. Distinga el dominio de la ecuación de la condición de signo que se pierde al cuadrar y determine cuál valor es sólo un candidato.

**43.** Se propone:

$$
\frac{x^2-9}{x-3}=6
\Longleftrightarrow
x+3=6
\Longleftrightarrow
x=3.
$$

Una estudiante afirma: «la cancelación de $x-3$ fue ilegítima porque produjo una respuesta falsa».

Analice esa afirmación. Determine el dominio original, explique si la cancelación es o no válida sobre ese dominio y localice con precisión dónde aparece el error de la resolución.

**44.** En la ecuación

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1},
$$

se multiplica por $x-1$, se obtiene $x+1=2$ y después $x=1$. El resolutor dice: «$x=1$ es una raíz extraña creada al eliminar denominadores».

Decida si ese diagnóstico es correcto. Distinga entre **candidato creado por una transformación no reversible** y **valor inadmisible por el dominio original**.

**45.** Se escribe

$$
x-2=-3
\Longleftrightarrow
(x-2)^2=9
\Longleftrightarrow
x-2=3\ \text{o}\ x-2=-3.
$$

Determine el conjunto solución de la primera y de la segunda ecuación de la cadena. Localice la primera falsa equivalencia y escriba la flecha correcta.

**46.** Para resolver

$$
(x-1)+(x+2)=0,
$$

un estudiante razona:

$$
(x-1)+(x+2)=0
\Longleftrightarrow
x-1=0\ \text{o}\ x+2=0,
$$

y concluye $x=1$ o $x=-2$.

Explique qué propiedad se aplicó fuera de su hipótesis estructural. Resuelva correctamente la ecuación y compare el conjunto obtenido con los dos valores propuestos.

**47.** Para

$$
x^4-5x^2+4=0,
$$

se define $u=x^2$, se resuelve

$$
u^2-5u+4=0
$$

y se obtiene

$$
u\in\{1,4\}.
$$

La resolución termina declarando

$$
\operatorname{Sol}_{\mathbb R}=\{1,4\}.
$$

Explique por qué el cálculo auxiliar puede ser correcto y, sin embargo, la respuesta final tener el tipo de objeto equivocado. Reconstruya todas las preimágenes reales.

**48.** Para

$$
x^4-10x^2+9=0,
$$

se usa $u=x^2$. La ecuación auxiliar da $u=1$ o $u=9$, y se concluye

$$
x=1\ \text{o}\ x=3.
$$

Localice la pérdida de soluciones. Explique qué propiedad de la sustitución $x\mapsto x^2$ obliga a reconstruir más de una preimagen para cada valor auxiliar positivo.

**49.** Se estudia la familia

$$
(a-2)x=a-2
$$

en la incógnita $x$. Una resolución divide inmediatamente por $a-2$ y concluye

$$
S(a)=\{1\}
\qquad
\text{para todo }a\in\mathbb R.
$$

Localice la primera ruptura, determine el valor excepcional del parámetro y describa la familia correcta de conjuntos solución.

**50.** Para el sistema

$$
\begin{cases}
y=x^2,\\
x+y=2,
\end{cases}
$$

se sustituye correctamente y se obtiene

$$
x^2+x-2=0,
$$

de donde

$$
x=-2
\qquad\text{o}\qquad
x=1.
$$

La resolución termina con

$$
\operatorname{Sol}=\{-2,1\}.
$$

Explique por qué no hay error en la ecuación reducida pero sí en la respuesta final. Identifique el espacio en el que vive el conjunto solución del sistema y reconstruya los pares ordenados correspondientes.



## E. Estrategia: elegir ruta y decidir cuándo verificar

En los ejercicios 51–60 no se anuncia de antemano el método óptimo. El objetivo es **elegir una ruta**, justificar por qué conviene y distinguir entre una verificación final lógicamente necesaria y una comprobación meramente independiente.

**51.** Resuelva sobre $\mathbb R$:

$$
x^2-9x+20=0.
$$

Antes de operar:

a) compare factorización, completar cuadrados y fórmula cuadrática;

b) elija la ruta que considere más eficiente y justifique la elección;

c) resuelva por esa ruta;

d) indique una segunda ruta válida sin desarrollarla por completo y explique por qué debe producir el mismo conjunto solución.

**52.** Resuelva sobre $\mathbb R$:

$$
x^2+6x-2=0.
$$

Compare específicamente estas dos estrategias:

- completar cuadrados;
- fórmula cuadrática.

Ejecute la que considere más transparente para esta ecuación y explique qué estructura hace menos natural una factorización elemental con coeficientes enteros.

**53.** Considere

$$
6x^2+x-2=0.
$$

Resuelva por dos rutas:

a) factorización;

b) fórmula cuadrática.

Después compare:

- número de pasos;
- cantidad de cálculo numérico;
- visibilidad de las soluciones;
- oportunidades de error de signo.

Concluya cuál ruta preferiría si sólo necesitara el conjunto solución.

**54.** Considere

$$
x^2-8x+16=0.
$$

Sin resolver inmediatamente, identifique qué rasgo visible debería gobernar la elección de método. Resuelva por la ruta más económica y use el discriminante únicamente como control estructural independiente.

Explique por qué aplicar directamente la fórmula cuadrática sería correcto pero estratégicamente innecesario.

**55.** Considere sobre $\mathbb R$:

$$
2x^2+4x+7=0.
$$

Entre las siguientes posibilidades,

- intentar factorizar;
- completar cuadrados;
- calcular primero el discriminante;

elija la que permita decidir con menor trabajo si existen soluciones reales. Justifique la elección y determine el conjunto solución real sin introducir raíces complejas.

**56.** Resuelva

$$
x^2-2x-1=0
$$

por:

a) completar cuadrados;

b) fórmula cuadrática.

Compare ambas rutas y responda: ¿cuál hace más visible la forma $(x-h)^2=k$ y cuál es más mecánica? Explique por qué «más mecánica» no significa necesariamente «más conveniente».

**57.** Considere

$$
\frac{x^2-9}{x-3}=6.
$$

Un estudiante propone esta estrategia:

1. fijar el dominio;
2. factorizar $x^2-9$;
3. cancelar $x-3$ sobre el dominio efectivo;
4. resolver la ecuación lineal resultante;
5. filtrar por pertenencia al dominio.

Analice la estrategia antes de efectuarla. Decida si, después del paso 5, sustituir de nuevo cada valor en la ecuación original es **lógicamente necesario** o sólo un control opcional. Fundamente su respuesta mediante la fuerza lógica de las transformaciones usadas y luego resuelva.

**58.** Resuelva sobre $\mathbb R$:

$$
\sqrt{x+4}=x.
$$

Compare estas dos rutas.

**Ruta A.** Cuadrar usando sólo

$$
\sqrt{x+4}=x
\Longrightarrow
x+4=x^2,
$$

y verificar al final todos los candidatos.

**Ruta B.** Conservar desde el comienzo la condición de signo y usar

$$
\sqrt{x+4}=x
\Longleftrightarrow
\bigl(x+4=x^2\ \text{y}\ x\ge0\bigr).
$$

Resuelva por ambas rutas. Explique por qué la verificación final es necesaria en A, mientras que en B las condiciones conservadas ya restablecen equivalencia.

**59.** Resuelva sobre $\mathbb R$:

$$
|2x-3|=7.
$$

Antes de resolver, responda:

a) ¿abrir las dos ramas produce una equivalencia o sólo una implicación?;

b) ¿la verificación final en la ecuación original es necesaria para recuperar corrección lógica?;

c) ¿en qué se diferencia este caso de una ecuación radical que fue simplemente elevada al cuadrado?

Después resuelva mediante la ruta que considere conceptualmente más directa.

**60.** Para cada una de las siguientes resoluciones planificadas, decida **antes de calcular** si la verificación final en la ecuación original es:

- necesaria para filtrar candidatos;
- innecesaria si se conserva correctamente el dominio o las condiciones equivalentes;
- útil sólo como control independiente.

Justifique cada decisión.

**a)** Factorizar y aplicar producto nulo a

$$
x^2-5x+6=0.
$$

**b)** Fijar $D=\mathbb R\setminus\{1\}$ y multiplicar por $x-1$ en

$$
\frac{x+2}{x-1}=3.
$$

**c)** Cuadrar sin registrar condición de signo en

$$
\sqrt{x+1}=x-1.
$$

**d)** Abrir las ramas equivalentes de

$$
|3x+1|=5.
$$

No basta con escribir «sí» o «no»: relacione cada decisión con $\Longleftrightarrow$, $\Longrightarrow$, dominio vigente y conjunto de candidatos.



## F. Transferencia: parámetros, dominios heredados, sustituciones y sistemas

En los ejercicios 61–72 las herramientas ya no aparecen aisladas. El objetivo es transferir a problemas nuevos la disciplina desarrollada en C18–C20 y en las secciones anteriores de C21: conservar dominios, reconocer valores excepcionales, reconstruir preimágenes y declarar el objeto solución correcto.

**61.** Para cada $a\in\mathbb R$, resuelva en $x$:

$$
(a-2)x=a^2-4.
$$

a) Identifique el valor excepcional del parámetro.

b) Resuelva el caso genérico sin cancelar antes de justificarlo.

c) Resuelva por separado el caso excepcional.

d) Escriba la familia completa $a\mapsto S(a)$.

**62.** Para cada $a\in\mathbb R$, resuelva en $x$:

$$
a(a+1)x=a+1.
$$

La clasificación debe distinguir todos los valores del parámetro que cambian la validez de una división. Presente el resultado de modo que aparezcan, si corresponde, los regímenes

$$
\varnothing,\qquad
\mathbb R,
\qquad
\text{y un conjunto unitario}.
$$

**63.** Para cada $a\in\mathbb R$, considere la ecuación

$$
\frac{x-2}{x-a}=0.
$$

a) Determine el dominio efectivo $D_a$.

b) Localice el valor del parámetro para el cual el único cero posible del numerador deja de ser admisible.

c) Describa completamente $S(a)$.

d) Explique por qué este ejercicio es simultáneamente un problema paramétrico y una transferencia directa de la disciplina de dominio de C20.

**64.** Resuelva sobre $\mathbb R$:

$$
\frac{x^2-9}{x^2-x-6}=0.
$$

Factorice numerador y denominador antes de decidir qué valores pueden ser soluciones. Debe distinguir:

- ceros del numerador;
- ceros del denominador;
- valores algebraicamente posibles que son inadmisibles por el dominio.

Declare el conjunto solución sobre el dominio efectivo.

**65.** Resuelva sobre $\mathbb R$:

$$
\sqrt{(x-1)^2}=3.
$$

No eleve al cuadrado de manera automática. Use primero la identidad heredada de C18

$$
\sqrt{u^2}=|u|
$$

y reduzca el problema a una ecuación con valor absoluto. Haga explícitas las equivalencias hasta obtener el conjunto solución.

**66.** Resuelva sobre $\mathbb R$:

$$
\sqrt{(2x-1)^2}=7.
$$

Compare dos lecturas:

a) convertir la raíz principal mediante $\sqrt{u^2}=|u|$ y resolver por ramas equivalentes;

b) elevar al cuadrado y tratar los resultados como candidatos.

Explique cuál ruta conserva mejor la información de signo y por qué ambas deben terminar en el mismo conjunto solución después del control lógico correspondiente.

**67.** Resuelva sobre $\mathbb R$:

$$
(x^2-1)^2-5(x^2-1)+4=0.
$$

Use una sustitución adecuada. La resolución debe mostrar tres niveles:

1. ecuación original en $x$;
2. ecuación auxiliar en una variable $u$;
3. reconstrucción completa de todas las preimágenes reales en $x$.

No se detenga en los valores de $u$.

**68.** Resuelva sobre $\mathbb R$:

$$
(x-1)^4-10(x-1)^2+9=0.
$$

Introduzca una variable auxiliar que haga visible una cuadrática. Después de resolverla, reconstruya **todas** las soluciones de la variable original y explique por qué cada valor auxiliar positivo puede producir más de una preimagen.

**69.** Resuelva sobre

$$
D=\mathbb R\setminus\{1\}
$$

la ecuación

$$
\left(\frac{x+1}{x-1}\right)^2
-
5\left(\frac{x+1}{x-1}\right)
+
6
=
0.
$$

Use

$$
u=\frac{x+1}{x-1}.
$$

Debe:

a) conservar el dominio original durante toda la sustitución;

b) resolver la cuadrática auxiliar;

c) reconstruir $x$ para cada valor admisible de $u$;

d) comprobar que las preimágenes obtenidas pertenecen a $D$.

**70.** Resuelva sobre $\mathbb R^2$ el sistema

$$
\begin{cases}
y=x^2,\\
x+y=12.
\end{cases}
$$

Use sustitución, reduzca a una ecuación en una variable y reconstruya después la segunda coordenada. La respuesta final debe ser un conjunto de pares ordenados.

**71.** Resuelva sobre $\mathbb R^2$:

$$
\begin{cases}
x+y=7,\\
xy=10.
\end{cases}
$$

Puede usar sustitución o la simetría suma–producto. Explique por qué, si aparece una solución $(r,s)$ con $r\neq s$, la simetría del sistema hace esperable también $(s,r)$.

**72.** Resuelva sobre $\mathbb R^2$:

$$
\begin{cases}
x^2+y^2=20,\\
x^2-y^2=12.
\end{cases}
$$

Use una combinación reversible de las ecuaciones para determinar primero $x^2$ y $y^2$. Después reconstruya todas las combinaciones de signos y verifique cuáles pares satisfacen simultáneamente el sistema original.



## G. Síntesis avanzada: problemas no rutinarios y trazabilidad completa

Los ejercicios 73–80 constituyen el bloque avanzado del capítulo. El método no viene anunciado. En cada problema deberá conservarse la trazabilidad completa del conjunto solución: dominio, fuerza lógica de las transformaciones, candidatos, ramas, reconstrucciones y objeto final.

**73.** Considere sobre $\mathbb R$ la ecuación

$$
\sqrt{3x+10}=x+2.
$$

Un borrador de resolución propone la cadena

$$
\sqrt{3x+10}=x+2
\quad\to\quad
3x+10=(x+2)^2
\quad\to\quad
x^2+x-6=0
\quad\to\quad
(x-2)(x+3)=0
\quad\to\quad
x=2\ \text{o}\ x=-3.
$$

a) Determine primero el dominio de la ecuación original.

b) Sustituya cada flecha $\to$ por $\Longleftrightarrow$ o $\Longrightarrow$, según corresponda, y justifique cada elección.

c) Identifique el primer paso en que el conjunto puede ampliarse.

d) Distinga el **conjunto de candidatos** del **conjunto solución**.

e) Explique qué información adicional permitiría convertir el primer cuadrado en una equivalencia completa.

**74.** Resuelva sobre $\mathbb R$:

$$
\frac{x^2}{x-1}
=
\frac{1}{x-1}.
$$

La solución debe comenzar por el dominio efectivo.

Después:

a) elimine denominadores mediante una transformación equivalente sobre ese dominio;

b) resuelva la ecuación polinómica resultante;

c) explique por qué uno de los valores algebraicos obtenidos sigue siendo inadmisible;

d) justifique por qué ese valor **no** debe describirse como un candidato extraño creado por una transformación no reversible.

El objetivo es separar con precisión **equivalencia sobre el dominio** y **filtrado por dominio original**.

**75.** Resuelva sobre $\mathbb R$:

$$
\sqrt{x+8}+\sqrt{x}=2.
$$

Desarrolle dos lecturas de la misma resolución.

**Ruta A — control lógico.** Fije el dominio, eleve al cuadrado la igualdad completa cuando esté justificado y aísle el radical restante. Examine el signo del miembro opuesto antes de volver a cuadrar.

**Ruta B — continuación algebraica.** Ignore provisionalmente esa señal de signo, eleve al cuadrado una segunda vez y determine el valor candidato que aparece.

Después:

a) verifique el candidato en la ecuación original;

b) explique en qué paso se volvió posible que apareciera una raíz extraña;

c) compare por qué la Ruta A puede cerrar el problema antes que la Ruta B.

**76.** Para cada $a\in\mathbb R$, resuelva en $x$:

$$
(a-1)(x^2-a)=0.
$$

La clasificación final debe distinguir, cuando corresponda, los cuatro tipos siguientes de conjunto solución:

$$
\varnothing,
\qquad
\text{un singleton},
\qquad
\text{un conjunto finito con más de un elemento},
\qquad
\mathbb R.
$$

Debe:

a) localizar primero el valor del parámetro que hace degenerar toda la ecuación;

b) resolver después el caso no degenerado;

c) separar los regímenes que dependen del signo de $a$ sin abrir teoría sistemática de inequaciones;

d) comprobar que los casos finales son exhaustivos y mutuamente excluyentes.

**77.** Resuelva sobre $\mathbb R$:

$$
(x-1)^4+3(x-1)^2-4=0.
$$

El método no está anunciado.

Si introduce una variable auxiliar, deberá justificar:

a) qué expresión conviene sustituir;

b) cuál es la imagen real de esa sustitución;

c) cuáles soluciones de la ecuación auxiliar son realizables;

d) cuántas preimágenes reales produce cada valor auxiliar admisible;

e) por qué el conjunto solución debe expresarse finalmente en la variable $x$ y no en la variable auxiliar.

**78.** Resuelva sobre $\mathbb R$:

$$
\left|
\frac{x-3}{x+1}
\right|
=
\frac12.
$$

La resolución debe integrar dos estructuras distintas.

a) Determine el dominio efectivo antes de abrir las barras.

b) Use una equivalencia exacta para convertir el valor absoluto en ramas.

c) Resuelva cada ecuación racional conservando el dominio heredado.

d) Una las ramas válidas y declare el conjunto solución.

e) Explique por qué no fue necesario construir una tabla de signos ni verificar como si las ramas hubieran surgido de una transformación sólo implicativa.

**79.** Resuelva sobre $\mathbb R^2$ el sistema

$$
\begin{cases}
x+y=6,\\
x^2+y^2=20.
\end{cases}
$$

Debe resolverlo por **dos rutas**.

**Ruta A.** Sustitución directa de una variable en la otra ecuación.

**Ruta B.** Use la identidad

$$
(x+y)^2=x^2+2xy+y^2
$$

para determinar primero $xy$ y convertir el problema en uno de suma–producto.

Después:

a) reconstruya todos los pares ordenados en cada ruta;

b) compruebe que ambas rutas producen exactamente el mismo subconjunto de $\mathbb R^2$;

c) explique qué papel desempeña la simetría bajo el intercambio $x\leftrightarrow y$.

**80.** Resuelva sobre $\mathbb R$ sin método anunciado:

$$
\frac{x^2-4}{x-2}
=
\sqrt{x+7}.
$$

La solución debe ser una síntesis completa del capítulo.

1. Determine el dominio original, conservando simultáneamente la restricción racional y la existencia del radical.
2. Simplifique la expresión racional sólo sobre ese dominio.
3. Decida qué fuerza lógica tiene elevar al cuadrado si no registra ninguna condición adicional.
4. Resuelva la ecuación algebraica resultante y obtenga el conjunto de candidatos.
5. Distinga:
   - valores excluidos desde el dominio original;
   - candidatos creados por pérdida de información de signo;
   - soluciones efectivas.
6. Realice una verificación independiente en la ecuación original.
7. Reescriba después la etapa radical mediante una **equivalencia completa con condición de signo** y explique cómo esa segunda ruta filtra el mismo conjunto sin depender únicamente de la comprobación final.
8. Declare el conjunto solución exacto y señale la primera transición que habría sido sólo implicativa en la ruta menos informativa.



## H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Diseñar exactamente dos soluciones

Dados $r<s$ y $h\notin\{r,s\}$, construya una ecuación racional cuyo conjunto solución real sea exactamente $\{r,s\}$ y cuyo dominio excluya $h$.



#### Ejercicio 082. Diseñar un intervalo solución con un radical

Dados $r<s$, construya una ecuación con raíz principal cuyo conjunto solución sea $[r,s]$.



#### Ejercicio 083. Una identidad sobre un dominio perforado

Dados $r\ne s$, diseñe una ecuación verdadera exactamente en $\mathbb R\setminus\{r,s\}$, sin que los puntos excluidos sean soluciones falsas.



#### Ejercicio 084. Parámetro, grado y candidato excluido

Resuelva $\dfrac{(t-1)x(x-2)}{x-t}=0$ para cada real $t$.



#### Ejercicio 085. Una cuadrática que se vuelve lineal

Clasifique todas las soluciones reales de $t x^2+(1-t)x-1=0$.



#### Ejercicio 086. Dos causas distintas de degeneración

Resuelva $(t-1)x/(x-t)=t-1$ para todo real $t$.



#### Ejercicio 087. Multiplicar por un factor: medir los candidatos añadidos

Compare $x=r$ con $(x-h)(x-r)=0$. Determine sus conjuntos solución y cuándo la multiplicación es una equivalencia sobre $\mathbb R$.



#### Ejercicio 088. Cuadrar con y sin condición de signo

Compare $\sqrt{x+2}=x$ con $x+2=x^2$ sobre $x\ge-2$. Localice el cambio del conjunto solución y repare la equivalencia.



#### Ejercicio 089. Una división que pierde una solución y otra que conserva el dominio

Resuelva $(x-r)^2=(x-r)(x-s)$ y compare dividir por $x-r$ con separar sus ceros, para todos los $r,s$.



#### Ejercicio 090. Reconstruir todos los pares de un sistema simétrico

Para reales $s,p$, resuelva $x+y=s$, $xy=p$, y clasifique el número de pares ordenados reales.



#### Ejercicio 091. Un sistema con una región imposible

Clasifique las soluciones reales de $x-y=a$, $xy=b$ según los parámetros reales $a,b$.



#### Ejercicio 092. Un sistema donde dividir borra una rama

Resuelva $x+y=s$, $x(y-r)=0$ para todos los reales $r,s$. Indique cuándo coinciden las ramas.

# Soluciones razonadas

Las soluciones conservan la función cognitiva del banco. En el bloque A la meta no es acelerar el cálculo, sino distinguir con precisión **dominio, valor de verdad, conjunto solución y fuerza lógica de una transformación**. Cuando dos ecuaciones se comparan, la dirección de la flecha se justifica mediante igualdad o inclusión de sus conjuntos solución; cuando interviene una expresión parcial, el dominio efectivo se fija antes de operar.

## A. Lectura: dominio, verdad y equivalencia


### Solución 1

La ecuación es

$$
2x+1=7.
$$

Para $x=3$,

$$
2(3)+1=6+1=7,
$$

por lo que la proposición es **verdadera**.

Para $x=4$,

$$
2(4)+1=8+1=9\neq7,
$$

por lo que la proposición es **falsa**.

Así, entre los dos valores examinados, sólo $3$ pertenece al conjunto solución. De hecho, resolviendo la ecuación,

$$
2x+1=7
\Longleftrightarrow
2x=6
\Longleftrightarrow
x=3,
$$

de modo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{3\}.}
$$

Comprobar un valor sólo decide si **ese valor concreto** satisface la ecuación. Una comprobación positiva no demuestra, en general, que no existan otras soluciones; una comprobación negativa tampoco determina cuáles son las que sí funcionan. Resolver exige caracterizar el conjunto completo de valores que hacen verdadera la proposición.


### Solución 2

La igualdad escrita es siempre

$$
x^2=4,
$$

pero el conjunto solución depende del dominio sobre el que se interpreta.

En $D_1=\mathbb R$,

$$
x^2=4
\Longleftrightarrow
x=2\ \text{o}\ x=-2,
$$

por lo que

$$
\boxed{S_{D_1}=\{-2,2\}.}
$$

En $D_2=[0,\infty)$, el valor $-2$ no pertenece al dominio. Por tanto,

$$
\boxed{S_{D_2}=\{2\}.}
$$

En $D_3=(0,2)$, ni $-2$ ni $2$ pertenecen al dominio: $-2$ queda fuera por ser negativo y $2$ queda fuera porque el extremo derecho es abierto. Así,

$$
\boxed{S_{D_3}=\varnothing.}
$$

La fórmula $x^2=4$ no ha cambiado. Lo que cambia es el universo de valores admisibles. Por eso una ecuación no queda completamente especificada sólo por la igualdad escrita: el dominio forma parte del problema.


### Solución 3

El problema declara

$$
x\in[0,5],
$$

por lo que el **dominio ambiente** es

$$
\boxed{D_{\mathrm{amb}}=[0,5].}
$$

La expresión

$$
\frac1{x-2}
$$

no está definida cuando

$$
x-2=0,
$$

es decir, cuando $x=2$. Por tanto, el **dominio efectivo** es

$$
\boxed{D_{\mathrm{ef}}=[0,5]\setminus\{2\}.}
$$

El valor $x=2$ no es una «solución que no funciona». Para poder preguntar si un valor satisface una ecuación, primero debe pertenecer al dominio efectivo. En $x=2$ el miembro izquierdo ni siquiera está definido; por ello $2$ es un **valor inadmisible**, no un candidato que se prueba y falla.

No es necesario resolver la ecuación para establecer esta distinción.


### Solución 4

La ecuación es

$$
\frac{x-1}{x-1}=1.
$$

Su dominio natural excluye el cero del denominador:

$$
x-1\neq0,
$$

de modo que

$$
\boxed{D=\mathbb R\setminus\{1\}.}
$$

Sobre este dominio, $x-1$ es no nulo y puede cancelarse:

$$
\frac{x-1}{x-1}=1.
$$

Por tanto la ecuación se reduce, **sobre $D$**, a

$$
1=1,
$$

que es verdadera para todo valor admisible. Luego

$$
\boxed{\operatorname{Sol}=\mathbb R\setminus\{1\}.}
$$

La respuesta no es $\mathbb R$ porque la simplificación no modifica retroactivamente el dominio de la expresión original. En $x=1$ aparece $0/0$, que no está definido. La fórmula simplificada oculta esa exclusión, pero no la elimina.


### Solución 5

Conviene comparar los conjuntos solución de cada par.

#### a)

Para

$$
x+4=9
$$

se obtiene $x=5$, y la segunda ecuación es precisamente

$$
x=5.
$$

Por tanto,

$$
S_1=S_2=\{5\},
$$

y corresponde escribir

$$
\boxed{x+4=9\ \Longleftrightarrow\ x=5.}
$$

#### b)

La primera ecuación tiene

$$
S_1=\{3\},
$$

mientras que

$$
x^2=9
$$

tiene

$$
S_2=\{-3,3\}.
$$

Se cumple la inclusión propia

$$
\{3\}\subsetneq\{-3,3\}.
$$

Todo valor que satisface $x=3$ satisface $x^2=9$, pero la recíproca falla en $x=-3$. Así,

$$
\boxed{x=3\ \Longrightarrow\ x^2=9.}
$$

#### c)

Por la propiedad del producto nulo,

$$
x(x+1)=0
$$

tiene

$$
S_1=\{0,-1\}.
$$

En cambio,

$$
x+1=0
$$

tiene

$$
S_2=\{-1\}.
$$

Ahora

$$
\{-1\}\subsetneq\{0,-1\},
$$

de modo que toda solución de la segunda ecuación es solución de la primera, pero no al revés. Por tanto,

$$
\boxed{x(x+1)=0\ \Longleftarrow\ x+1=0.}
$$

La doble flecha corresponde exactamente a igualdad de conjuntos solución. Una sola flecha corresponde a una inclusión en la dirección apropiada.


### Solución 6

La primera ecuación es

$$
x=2,
$$

por lo que

$$
S_1=\{2\}.
$$

La segunda puede escribirse como

$$
x^2=2x
\Longleftrightarrow
x^2-2x=0
\Longleftrightarrow
x(x-2)=0.
$$

Por la propiedad del producto nulo,

$$
x=0
\qquad\text{o}\qquad
x=2.
$$

Así,

$$
S_2=\{0,2\}.
$$

Por tanto,

$$
\boxed{S_1\subsetneq S_2.}
$$

Si se obtiene la segunda ecuación multiplicando

$$
x=2
$$

por $x$, entonces

$$
x=2
\Longrightarrow
x^2=2x.
$$

La transformación no es reversible para todo real porque el factor usado para multiplicar puede ser cero. En $x=0$, la ecuación multiplicada se convierte en $0=0$, aunque la ecuación original $x=2$ sea falsa. Por eso $0$ es un **candidato adicional** creado por la transformación.


### Solución 7

Trabajamos sobre

$$
D=\mathbb R\setminus\{4\}.
$$

En todo punto de $D$ se cumple

$$
x-4\neq0.
$$

Por ello podemos multiplicar ambos miembros de

$$
\frac2{x-4}=5
$$

por $x-4$ sin perder ni crear soluciones:

$$
\frac2{x-4}=5
\Longleftrightarrow
2=5(x-4),
\qquad x\in D.
$$

La reversibilidad es inmediata: partiendo de $2=5(x-4)$, como $x-4\neq0$ en $D$, podemos dividir otra vez por $x-4$ y recuperar la ecuación original.

El dominio debe conservarse explícitamente porque la primera ecuación no está definida en $x=4$, mientras que la segunda expresión

$$
2=5(x-4)
$$

sí tiene sentido como proposición para todo número real. Por tanto, afirmar sin más que son equivalentes «sobre $\mathbb R$» ignoraría que en $x=4$ una de las dos ecuaciones ni siquiera está definida.

La afirmación correcta es

$$
\boxed{
\frac2{x-4}=5
\Longleftrightarrow
2=5(x-4)
\quad\text{sobre }D=\mathbb R\setminus\{4\}.
}
$$


### Solución 8

La ecuación es

$$
\frac{x+1}{x-2}=0.
$$

Su dominio natural es

$$
D=\mathbb R\setminus\{2\}.
$$

Examinamos los tres valores pedidos.

Para $x=-1$, el valor es admisible y

$$
\frac{-1+1}{-1-2}
=
\frac0{-3}
=0.
$$

Por tanto,

$$
\boxed{-1\ \text{es solución}.}
$$

Para $x=2$, el denominador se anula. La expresión no está definida, así que

$$
\boxed{2\ \text{es un valor inadmisible}.}
$$

Para $x=0$, el valor pertenece al dominio, pero

$$
\frac{0+1}{0-2}
=
-\frac12\neq0.
$$

Por tanto,

$$
\boxed{0\ \text{es admisible, pero no es solución}.}
$$

La diferencia conceptual es esencial: en $x=0$ la ecuación tiene un valor de verdad y resulta falsa; en $x=2$ la expresión del miembro izquierdo no existe, por lo que el valor queda excluido antes de preguntar si satisface la igualdad.


### Solución 9

Sobre $\mathbb R$, la primera ecuación

$$
x=1
$$

tiene conjunto solución

$$
S_1=\{1\}.
$$

La segunda ecuación

$$
x^2=1
$$

equivale a

$$
x^2-1=0
\Longleftrightarrow
(x-1)(x+1)=0,
$$

y por tanto

$$
S_2=\{-1,1\}.
$$

Los conjuntos no son iguales:

$$
\{1\}\neq\{-1,1\}.
$$

Así, la doble flecha es incorrecta. Sí se cumple

$$
\boxed{x=1\ \Longrightarrow\ x^2=1,}
$$

porque

$$
\boxed{\{1\}\subsetneq\{-1,1\}.}
$$

La implicación inversa falla: $x=-1$ satisface $x^2=1$, pero no satisface $x=1$.


### Solución 10

La ecuación original es

$$
x(x-2)=0.
$$

Por la propiedad del producto nulo,

$$
x=0
\qquad\text{o}\qquad
x=2,
$$

de modo que

$$
S_{\mathrm{orig}}=\{0,2\}.
$$

La ecuación transformada es

$$
x-2=0,
$$

y por tanto

$$
S_{\mathrm{trans}}=\{2\}.
$$

La división por $x$ no conserva equivalencia porque $x$ puede ser cero en la ecuación original. Precisamente en $x=0$ el factor por el que se pretende dividir se anula. Ese valor satisface la ecuación original y desaparece al efectuar la división.

La relación válida es

$$
\boxed{x(x-2)=0\ \Longleftarrow\ x-2=0,}
$$

o, equivalentemente,

$$
x-2=0
\Longrightarrow
x(x-2)=0.
$$

En términos de conjuntos solución,

$$
\{2\}\subsetneq\{0,2\}.
$$

La solución perdida es

$$
\boxed{x=0.}
$$

Si al final sólo comprobamos el valor superviviente $x=2$, verificaremos correctamente que

$$
2(2-2)=0.
$$

Pero esa comprobación únicamente confirma que $2$ es una solución verdadera; no demuestra que sea **la única**. Una verificación final puede eliminar candidatos falsos, pero no puede recuperar por sí sola una solución que ya fue descartada por una transformación no reversible.

## B. Fluidez: lineales, producto nulo y cuadráticas

En este bloque el objetivo es consolidar procedimientos ya justificados sin perder la estructura lógica del capítulo. Como todos los ejercicios se resuelven sobre $\mathbb R$, no aparecen restricciones adicionales de dominio; las transformaciones lineales usadas son equivalencias, la factorización conserva la ecuación y la propiedad del producto nulo describe exactamente la unión de las ramas.


### Solución 11

Partimos de

$$
7x-11=24.
$$

Sumamos $11$ en ambos miembros:

$$
7x=35.
$$

Como $7\neq0$, dividir por $7$ es reversible:

$$
x=5.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{5\}.}
$$


### Solución 12

Tenemos

$$
5x+8=2x-13.
$$

Restamos $2x$ y después $8$ en ambos miembros:

$$
5x+8=2x-13
\Longleftrightarrow
3x+8=-13
\Longleftrightarrow
3x=-21.
$$

Dividiendo por la constante no nula $3$,

$$
x=-7.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-7\}.}
$$


### Solución 13

La ecuación es

$$
\frac{3x-2}{4}-\frac{x+1}{2}=5.
$$

Multiplicamos toda la ecuación por $4$. Como $4\neq0$, el paso conserva equivalencia:

$$
3x-2-2(x+1)=20.
$$

Desarrollando,

$$
3x-2-2x-2=20,
$$

de donde

$$
x-4=20
\Longleftrightarrow
x=24.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{24\}.}
$$


### Solución 14

Partimos de

$$
6(x-2)+3=6x-9.
$$

Desarrollamos el miembro izquierdo:

$$
6x-12+3=6x-9,
$$

es decir,

$$
6x-9=6x-9.
$$

Restando $6x-9$ en ambos miembros obtenemos

$$
0=0.
$$

La proposición final es verdadera para todo número real. Como todas las transformaciones fueron equivalentes, la ecuación original también es verdadera para todo $x\in\mathbb R$.

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\mathbb R.}
$$

La ecuación es una **identidad sobre $\mathbb R$**.


### Solución 15

Tenemos

$$
4(2x+1)=8x+11.
$$

Desarrollamos:

$$
8x+4=8x+11.
$$

Restando $8x$ en ambos miembros queda

$$
4=11.
$$

Esta proposición es falsa, independientemente del valor de $x$. Como llegamos a ella mediante transformaciones equivalentes, ningún real satisface la ecuación original.

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\varnothing.}
$$

La ecuación es una **contradicción sobre $\mathbb R$**.


### Solución 16

La ecuación ya tiene la estructura apropiada para aplicar producto nulo:

$$
(3x-2)(x+5)=0.
$$

Sobre los reales,

$$
(3x-2)(x+5)=0
\Longleftrightarrow
3x-2=0
\quad\text{o}\quad
x+5=0.
$$

La primera rama da

$$
x=\frac23,
$$

y la segunda,

$$
x=-5.
$$

Al unir ambas ramas,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-5,\frac23\right\}.
}
$$

No fue necesario dividir por ninguno de los factores: la propiedad del producto nulo conserva exactamente las dos posibilidades.


### Solución 17

Tenemos un producto de tres factores:

$$
x(x-4)(2x+3)=0.
$$

La propiedad del producto nulo da la equivalencia

$$
x=0
\quad\text{o}\quad
x-4=0
\quad\text{o}\quad
2x+3=0.
$$

Por tanto,

$$
x=0,
\qquad
x=4,
\qquad
x=-\frac32.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac32,0,4\right\}.
}
$$

Cada factor aporta una rama posible y el conjunto solución final es la unión de las tres.


### Solución 18

La ecuación es

$$
(x-1)^2(x+6)=0.
$$

Sin dividir por ningún factor, aplicamos producto nulo:

$$
(x-1)^2=0
\quad\text{o}\quad
x+6=0.
$$

La primera rama equivale a

$$
x-1=0,
$$

de donde $x=1$. La segunda produce $x=-6$.

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-6,1\}.}
$$

El factor $(x-1)$ aparece con multiplicidad $2$, pero un conjunto no repite elementos: $1$ aparece una sola vez en el conjunto solución. Dividir por $(x-1)^2$ habría sido una mala estrategia, pues eliminaría precisamente la rama $x=1$.


### Solución 19

Primero llevamos todos los términos a un mismo miembro:

$$
x^2=7x-12
\Longleftrightarrow
x^2-7x+12=0.
$$

Factorizamos:

$$
x^2-7x+12=(x-3)(x-4).
$$

Entonces

$$
(x-3)(x-4)=0
\Longleftrightarrow
x=3
\quad\text{o}\quad
x=4.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{3,4\}.}
$$

La propiedad del producto nulo sólo se aplicó después de obtener una ecuación equivalente de la forma producto igual a cero.


### Solución 20

Buscamos una factorización de

$$
6x^2-x-2.
$$

Se tiene

$$
6x^2-x-2=(3x-2)(2x+1),
$$

pues

$$
(3x-2)(2x+1)
=6x^2+3x-4x-2
=6x^2-x-2.
$$

Así,

$$
6x^2-x-2=0
\Longleftrightarrow
(3x-2)(2x+1)=0.
$$

Por producto nulo,

$$
3x-2=0
\quad\text{o}\quad
2x+1=0,
$$

de donde

$$
x=\frac23
\quad\text{o}\quad
x=-\frac12.
$$

Luego,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac12,\frac23\right\}.
}
$$


### Solución 21

Completamos cuadrados en

$$
x^2+8x+7=0.
$$

Aislamos primero los términos con $x$:

$$
x^2+8x=-7.
$$

La mitad de $8$ es $4$ y $4^2=16$. Añadimos $16$ a ambos miembros:

$$
x^2+8x+16=9.
$$

Por tanto,

$$
(x+4)^2=9.
$$

Sobre $\mathbb R$,

$$
(x+4)^2=9
\Longleftrightarrow
x+4=3
\quad\text{o}\quad
x+4=-3.
$$

Así,

$$
x=-1
\quad\text{o}\quad
x=-7,
$$

y finalmente

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-7,-1\}.}
$$


### Solución 22

Partimos de

$$
x^2-6x-2=0.
$$

Aislamos los términos variables:

$$
x^2-6x=2.
$$

La mitad de $-6$ es $-3$ y $(-3)^2=9$. Sumamos $9$ a ambos miembros:

$$
x^2-6x+9=11.
$$

Entonces

$$
(x-3)^2=11.
$$

Como $11>0$,

$$
x-3=\sqrt{11}
\quad\text{o}\quad
x-3=-\sqrt{11}.
$$

Por tanto,

$$
x=3+\sqrt{11}
\quad\text{o}\quad
x=3-\sqrt{11},
$$

y

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{3-\sqrt{11},\,3+\sqrt{11}\}.
}
$$


### Solución 23

Debemos resolver

$$
x^2-10x+21=0
$$

por dos rutas.

#### Ruta a: factorización

Buscamos dos números cuyo producto sea $21$ y cuya suma sea $10$. Son $3$ y $7$. Por tanto,

$$
x^2-10x+21=(x-3)(x-7).
$$

Así,

$$
(x-3)(x-7)=0
\Longleftrightarrow
x=3
\quad\text{o}\quad
x=7.
$$

#### Ruta b: completar cuadrados

Partimos de

$$
x^2-10x=-21.
$$

La mitad de $-10$ es $-5$ y $(-5)^2=25$. Sumando $25$ a ambos miembros,

$$
x^2-10x+25=4,
$$

de modo que

$$
(x-5)^2=4.
$$

Entonces

$$
x-5=2
\quad\text{o}\quad
x-5=-2,
$$

y otra vez

$$
x=7
\quad\text{o}\quad
x=3.
$$

Ambas cadenas están formadas por equivalencias y terminan en el mismo conjunto:

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{3,7\}.}
$$

La coincidencia no es accidental: las dos rutas resuelven la misma ecuación mediante representaciones distintas que preservan su conjunto solución.


### Solución 24

Para

$$
3x^2-2x-8=0,
$$

tenemos

$$
a=3,
\qquad
b=-2,
\qquad
c=-8.
$$

Calculamos primero el discriminante:

$$
\Delta=b^2-4ac
=(-2)^2-4(3)(-8)
=4+96
=100.
$$

Como

$$
\Delta>0,
$$

esperamos dos soluciones reales distintas. Aplicamos la fórmula cuadrática:

$$
x
=
\frac{-b\pm\sqrt\Delta}{2a}
=
\frac{2\pm10}{6}.
$$

Las dos ramas son

$$
x=\frac{12}{6}=2
$$

y

$$
x=\frac{-8}{6}=-\frac43.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac43,2\right\}.
}
$$


### Solución 25

En

$$
9x^2+12x+4=0
$$

tenemos

$$
a=9,
\qquad
b=12,
\qquad
c=4.
$$

El discriminante es

$$
\Delta
=12^2-4(9)(4)
=144-144
=0.
$$

Por tanto, la ecuación posee **una única solución real** —una raíz doble en sentido algebraico—. La fórmula da

$$
x
=
\frac{-12}{18}
=-\frac23.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac23\right\}.
}
$$

Como control estructural,

$$
9x^2+12x+4=(3x+2)^2,
$$

por lo que la misma solución se hace visible directamente desde $(3x+2)^2=0$.


### Solución 26

Para

$$
2x^2-4x+7=0,
$$

tenemos

$$
a=2,
\qquad
b=-4,
\qquad
c=7.
$$

Calculamos

$$
\Delta
=(-4)^2-4(2)(7)
=16-56
=-40.
$$

Como

$$
\Delta<0,
$$

la ecuación no tiene soluciones reales: al completar cuadrados se obtendría un cuadrado real igual a una cantidad negativa.

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\varnothing.}
$$

En C21 la resolución termina aquí, porque el dominio es $\mathbb R$; las soluciones complejas pertenecen al tratamiento posterior correspondiente.

## C. Justificación: hipótesis y transformaciones

En este bloque no basta con llegar a un conjunto solución correcto. Cada transformación debe acompañarse de la hipótesis que la hace reversible o, cuando aparece una estructura de casos, de la equivalencia exacta que justifica la ramificación. La meta es que el cálculo y la lógica permanezcan visibles al mismo tiempo.


### Solución 27

Partimos de

$$
x(x-3)=2x.
$$

No dividimos por $x$, porque todavía no sabemos si $x$ puede valer cero. En cambio, restamos $2x$ en ambos miembros, operación reversible sobre todo $\mathbb R$:

$$
x(x-3)=2x
\Longleftrightarrow
x(x-3)-2x=0.
$$

Extraemos factor común:

$$
x(x-5)=0.
$$

La factorización es una identidad algebraica, por lo que no altera el conjunto solución. Aplicamos ahora la propiedad del producto nulo:

$$
x(x-5)=0
\Longleftrightarrow
x=0
\quad\text{o}\quad
x-5=0.
$$

Así,

$$
x=0
\quad\text{o}\quad
x=5,
$$

y por tanto

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{0,5\}.}
$$

La ruta conserva todas las soluciones porque sólo usamos equivalencias. Dividir directamente por $x$ habría exigido $x\neq0$ y habría eliminado precisamente la solución $x=0$.


### Solución 28

Trabajamos sobre el dominio declarado

$$
D=\mathbb R\setminus\{1\}.
$$

La ecuación es

$$
(x-1)(2x+3)=7(x-1).
$$

Para todo $x\in D$ se cumple

$$
x-1\neq0.
$$

Por eso dividir ambos miembros por $x-1$ es una transformación reversible **sobre $D$**:

$$
(x-1)(2x+3)=7(x-1)
\Longleftrightarrow
2x+3=7,
\qquad x\in D.
$$

Resolviendo,

$$
2x=4
\Longleftrightarrow
x=2.
$$

Como $2\in D$, obtenemos

$$
\boxed{\operatorname{Sol}_D=\{2\}.}
$$

La hipótesis decisiva no es que el factor dependa o no de $x$, sino que **no puede anularse en el dominio vigente**. Si el dominio fuera todo $\mathbb R$, la división no sería automáticamente equivalente, porque $x=1$ sería un valor posible antes de separar casos.


### Solución 29

La ecuación es

$$
x^4-10x^2+9=0.
$$

Introducimos

$$
u=x^2.
$$

Como $x\in\mathbb R$, la variable auxiliar hereda la restricción

$$
\boxed{u\ge0.}
$$

Además,

$$
x^4=(x^2)^2=u^2,
$$

de modo que la ecuación auxiliar es

$$
u^2-10u+9=0.
$$

Factorizamos:

$$
u^2-10u+9=(u-1)(u-9).
$$

Por producto nulo,

$$
u=1
\quad\text{o}\quad
u=9.
$$

Ambos valores son realizables porque pertenecen a $[0,\infty)$, la imagen de la sustitución $u=x^2$ sobre $\mathbb R$.

Ahora reconstruimos **todas** las preimágenes.

Si $u=1$,

$$
x^2=1
\Longleftrightarrow
x=\pm1.
$$

Si $u=9$,

$$
x^2=9
\Longleftrightarrow
x=\pm3.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-3,-1,1,3\}.
}
$$

La sustitución no estaría completa si termináramos en $u\in\{1,9\}$: ésas son soluciones de la ecuación auxiliar, no todavía del problema original en $x$.


### Solución 30

Definimos

$$
u=2x-1.
$$

La ecuación se transforma en

$$
u^2-7u+10=0.
$$

Factorizamos:

$$
u^2-7u+10=(u-2)(u-5),
$$

de modo que

$$
u=2
\quad\text{o}\quad
u=5.
$$

La sustitución

$$
x\longmapsto 2x-1
$$

es biyectiva de $\mathbb R$ en $\mathbb R$: para cada $u\in\mathbb R$ existe exactamente un

$$
x=\frac{u+1}{2}.
$$

Por tanto, no hay restricción adicional sobre la variable auxiliar ni ramificación al regresar.

Para $u=2$,

$$
2x-1=2
\Longleftrightarrow
x=\frac32.
$$

Para $u=5$,

$$
2x-1=5
\Longleftrightarrow
x=3.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{\frac32,3\right\}.
}
$$

A diferencia de $u=x^2$, aquí cada solución auxiliar posee una sola preimagen real.


### Solución 31

La ecuación es

$$
\frac{x+2}{x-3}=4.
$$

Antes de eliminar el denominador fijamos el dominio efectivo:

$$
x-3\neq0,
$$

de modo que

$$
\boxed{D=\mathbb R\setminus\{3\}.}
$$

En todo $D$ el factor $x-3$ está definido y es no nulo. Por ello podemos multiplicar ambos miembros por $x-3$ y conservar equivalencia:

$$
\frac{x+2}{x-3}=4
\Longleftrightarrow
x+2=4(x-3),
\qquad x\in D.
$$

Resolvemos:

$$
x+2=4x-12
\Longleftrightarrow
14=3x
\Longleftrightarrow
x=\frac{14}{3}.
$$

Como

$$
\frac{14}{3}\neq3,
$$

el valor pertenece al dominio original. Por tanto,

$$
\boxed{
\operatorname{Sol}_D
=
\left\{\frac{14}{3}\right\}.
}
$$

La eliminación del denominador no fue un paso meramente formal: fue una equivalencia autorizada por la no nulidad de $x-3$ en todo el dominio vigente.


### Solución 32

Consideramos

$$
\frac{1}{x-2}+\frac{1}{x+2}=1.
$$

Los denominadores exigen

$$
x\neq2,
\qquad
x\neq-2.
$$

Así,

$$
\boxed{D=\mathbb R\setminus\{-2,2\}.}
$$

Tomamos como multiplicador común

$$
M(x)=(x-2)(x+2).
$$

Por la definición de $D$,

$$
M(x)\neq0
\qquad\text{para todo }x\in D.
$$

Multiplicar la ecuación completa por $M(x)$ es, por tanto, reversible sobre $D$:

$$
(x+2)+(x-2)=(x-2)(x+2).
$$

Simplificando,

$$
2x=x^2-4,
$$

y entonces

$$
x^2-2x-4=0.
$$

Completamos cuadrados:

$$
x^2-2x=4
\Longleftrightarrow
x^2-2x+1=5
\Longleftrightarrow
(x-1)^2=5.
$$

Por tanto,

$$
x=1-\sqrt5
\quad\text{o}\quad
x=1+\sqrt5.
$$

Ninguno de estos valores es $-2$ ni $2$, por lo que ambos pertenecen a $D$. Así,

$$
\boxed{
\operatorname{Sol}_D
=
\{1-\sqrt5,\,1+\sqrt5\}.
}
$$

No aparecen candidatos extraños por la eliminación de denominadores: cada paso fue una equivalencia sobre el dominio fijado al comienzo.


### Solución 33

La ecuación original es

$$
\frac{x^2-4}{x-2}=4.
$$

El denominador exige

$$
x\neq2,
$$

de modo que

$$
\boxed{D=\mathbb R\setminus\{2\}.}
$$

Factorizamos el numerador:

$$
x^2-4=(x-2)(x+2).
$$

Como $x-2\neq0$ en todo $D$, podemos cancelar ese factor y conservar equivalencia **sobre $D$**:

$$
\frac{(x-2)(x+2)}{x-2}=4
\Longleftrightarrow
x+2=4,
\qquad x\in D.
$$

La ecuación algebraica simplificada produce

$$
x=2.
$$

Pero

$$
2\notin D.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_D=\varnothing.}
$$

La cancelación fue completamente válida: la equivalencia se afirmó desde el principio sólo para $x\neq2$. El error aparecería si, después de simplificar, reinterpretáramos $x+2=4$ sobre todo $\mathbb R$ y olvidáramos el dominio de procedencia. El valor $2$ no es un candidato extraño creado por una transformación no reversible; es un valor **inadmisible desde el problema original**.


### Solución 34

La ecuación es

$$
\sqrt{2x+3}=5.
$$

La raíz exige

$$
2x+3\ge0,
$$

de modo que el dominio es

$$
\boxed{D=\left[-\frac32,\infty\right).}
$$

En este dominio el miembro izquierdo es una raíz principal y, por tanto, es no negativo. El miembro derecho es la constante positiva $5$. Así, ambos miembros pertenecen a $[0,\infty)$, donde la función $t\mapsto t^2$ es inyectiva. Por eso elevar al cuadrado es reversible:

$$
\sqrt{2x+3}=5
\Longleftrightarrow
2x+3=25,
\qquad x\in D.
$$

Equivalentemente, la formulación completa sería

$$
\sqrt{2x+3}=5
\Longleftrightarrow
\bigl(2x+3=25\ \text{y}\ 5\ge0\bigr),
$$

y la condición de signo es automática.

Resolvemos:

$$
2x=22
\Longleftrightarrow
x=11.
$$

Como $11\in D$,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{11\}.}
$$


### Solución 35

Consideramos

$$
\sqrt{x+4}=x.
$$

La raíz está definida cuando

$$
x+4\ge0,
$$

es decir,

$$
x\ge-4.
$$

Pero una raíz principal es siempre no negativa. Para que pueda ser igual a $x$, necesitamos además

$$
\boxed{x\ge0.}
$$

Usamos la equivalencia completa para una raíz principal aislada:

$$
\sqrt{x+4}=x
\Longleftrightarrow
\begin{cases}
x+4=x^2,\\
x\ge0.
\end{cases}
$$

La ecuación algebraica es

$$
x^2-x-4=0.
$$

Su discriminante es

$$
\Delta=(-1)^2-4(1)(-4)=17,
$$

de modo que

$$
x=\frac{1\pm\sqrt{17}}{2}.
$$

Ahora aplicamos la condición de signo. Como $\sqrt{17}>1$,

$$
\frac{1-\sqrt{17}}{2}<0,
$$

por lo que esa raíz no puede satisfacer la ecuación original. En cambio,

$$
\frac{1+\sqrt{17}}{2}>0.
$$

Así,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{\frac{1+\sqrt{17}}{2}\right\}.
}
$$

El valor negativo sí pertenece al dominio de existencia de $\sqrt{x+4}$, pero viola la condición $x\ge0$. Si hubiéramos cuadrado sin conservar esa condición, habría aparecido como candidato adicional.


### Solución 36

La ecuación es

$$
\sqrt{x+8}=\sqrt{3x+2}.
$$

Para que ambas raíces estén definidas necesitamos

$$
x+8\ge0
$$

y

$$
3x+2\ge0.
$$

Esto equivale a

$$
x\ge-8
$$

y

$$
x\ge-\frac23.
$$

El dominio común es, por tanto,

$$
\boxed{D=\left[-\frac23,\infty\right).}
$$

En $D$ ambos miembros son raíces principales y, por tanto, son no negativos. Como el cuadrado es inyectivo sobre $[0,\infty)$, podemos escribir la equivalencia

$$
\sqrt{x+8}=\sqrt{3x+2}
\Longleftrightarrow
x+8=3x+2,
\qquad x\in D.
$$

Resolviendo,

$$
6=2x
\Longleftrightarrow
x=3.
$$

Como $3\in D$,

$$
\boxed{\operatorname{Sol}_D=\{3\}.}
$$

Aquí cuadrar no crea candidatos porque el signo de **ambos** miembros está controlado automáticamente por tratarse de raíces principales.


### Solución 37

Partimos de

$$
3|2x-1|-2=10.
$$

Primero aislamos el valor absoluto mediante transformaciones reversibles:

$$
3|2x-1|-2=10
\Longleftrightarrow
3|2x-1|=12
\Longleftrightarrow
|2x-1|=4.
$$

Como $4>0$, la definición del valor absoluto da una equivalencia exacta en dos ramas:

$$
|2x-1|=4
\Longleftrightarrow
2x-1=4
\quad\text{o}\quad
2x-1=-4.
$$

La primera rama produce

$$
2x=5
\Longleftrightarrow
x=\frac52,
$$

y la segunda,

$$
2x=-3
\Longleftrightarrow
x=-\frac32.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac32,\frac52\right\}.
}
$$

No se generan candidatos adicionales porque abrir las barras mediante

$$
|A|=c
\Longleftrightarrow
A=c\ \text{o}\ A=-c
\qquad(c>0)
$$

no es una aproximación ni una implicación unilateral: describe exactamente todas las posibilidades de la ecuación original.


### Solución 38

La ecuación es

$$
|x-3|=x+1.
$$

El miembro izquierdo es siempre no negativo. Por tanto, toda solución debe satisfacer la condición de admisibilidad

$$
\boxed{x+1\ge0,}
$$

es decir,

$$
x\ge-1.
$$

Conservando esa condición, la ecuación admite la formulación equivalente

$$
|x-3|=x+1
\Longleftrightarrow
\left(
 x\ge-1
 \ \text{y}\ 
 \bigl(x-3=x+1\ \text{o}\ x-3=-(x+1)\bigr)
\right).
$$

Resolvemos las ramas.

La primera da

$$
x-3=x+1
\Longleftrightarrow
-3=1,
$$

que es una contradicción y no aporta soluciones.

La segunda da

$$
x-3=-x-1
\Longleftrightarrow
2x=2
\Longleftrightarrow
x=1.
$$

El valor obtenido satisface la condición acumulada $x\ge-1$. Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{1\}.}
$$

La no negatividad de $x+1$ no es un filtro improvisado al final: forma parte de la equivalencia que permite reemplazar correctamente la ecuación con valor absoluto por sus ramas.

## D. Diagnóstico: localizar la primera ruptura

En este bloque la prioridad no es sólo obtener la respuesta correcta, sino reconstruir **dónde** dejó de conservarse el problema original. Para cada caso se identifica la primera ruptura, se clasifica su efecto sobre el conjunto solución y se repara la cadena desde ese punto. La verificación final se usa cuando corresponde, pero nunca como sustituto del control lógico durante la resolución.


### Solución 39

La ecuación original es

$$
(x-4)(x+1)=0.
$$

Por producto nulo,

$$
(x-4)(x+1)=0
\Longleftrightarrow
x-4=0
\quad\text{o}\quad
x+1=0,
$$

de modo que

$$
S_{\mathrm{orig}}=\{-1,4\}.
$$

La resolución defectuosa divide por $x-4$ y conserva sólo

$$
x+1=0,
$$

cuyo conjunto solución es

$$
S_{\mathrm{trans}}=\{-1\}.
$$

La primera ruptura está, por tanto, en

$$
(x-4)(x+1)=0
\not\Longleftrightarrow
x+1=0.
$$

Dividir por $x-4$ exige $x\neq4$, pero $x=4$ es precisamente una solución de la ecuación original. El daño es una **solución perdida**.

La relación lógica segura es

$$
x+1=0
\Longrightarrow
(x-4)(x+1)=0,
$$

o, con la orientación de la cadena original,

$$
(x-4)(x+1)=0
\Longleftarrow
x+1=0.
$$

La reparación correcta evita la división:

$$
(x-4)(x+1)=0
\Longleftrightarrow
x=4
\quad\text{o}\quad
x=-1.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-1,4\}.}
$$


### Solución 40

La ecuación es

$$
x(x-5)=0.
$$

La propiedad del producto nulo da inmediatamente

$$
x(x-5)=0
\Longleftrightarrow
x=0
\quad\text{o}\quad
x-5=0.
$$

Por tanto,

$$
S_{\mathrm{orig}}=\{0,5\}.
$$

La cadena propuesta divide implícitamente por $x$ y pasa a

$$
x-5=0,
$$

cuyo conjunto solución es sólo

$$
\{5\}.
$$

La primera ruptura es esa división: como $x$ puede valer cero en una solución original, el paso no es reversible. La relación correcta es

$$
x-5=0
\Longrightarrow
x(x-5)=0,
$$

pero no la recíproca.

La verificación

$$
5(5-5)=0
$$

demuestra únicamente que $5$ **sí** es solución. No demuestra que sea la única. La solución $x=0$ ya desapareció de la cadena antes de la verificación, y comprobar el valor superviviente no puede recuperarla.

La resolución completa es

$$
x(x-5)=0
\Longleftrightarrow
x=0
\quad\text{o}\quad
x=5,
$$

de modo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{0,5\}.}
$$

El daño es una **solución perdida**; la verificación final no detecta por sí sola pérdidas de este tipo.


### Solución 41

La ecuación original

$$
2x=8
$$

tiene una única solución:

$$
x=4.
$$

Por tanto,

$$
S_{\mathrm{orig}}=\{4\}.
$$

Se multiplica por $x-3$:

$$
2x(x-3)=8(x-3).
$$

Todo valor que satisface $2x=8$ satisface también esta nueva ecuación, así que la dirección siempre válida es

$$
\boxed{
2x=8
\Longrightarrow
2x(x-3)=8(x-3).
}
$$

Sin embargo, la vuelta no está garantizada porque el factor $x-3$ puede anularse. Reescribiendo la ecuación transformada,

$$
2x(x-3)-8(x-3)=0,
$$

$$
(x-3)(2x-8)=0,
$$

$$
2(x-3)(x-4)=0.
$$

Por producto nulo,

$$
x=3
\quad\text{o}\quad
x=4.
$$

Así,

$$
S_{\mathrm{trans}}=\{3,4\},
$$

y

$$
\{4\}\subsetneq\{3,4\}.
$$

El valor adicional es

$$
\boxed{x=3.}
$$

La primera ruptura es haber escrito una doble flecha al multiplicar por un factor que podía valer cero. El daño es la **creación de un candidato adicional**.


### Solución 42

Consideramos

$$
\sqrt{x+6}=x.
$$

La raíz existe cuando

$$
x+6\ge0,
$$

por lo que el dominio de existencia es

$$
D=[-6,\infty).
$$

Pero la ecuación contiene además una condición que no proviene del dominio: como una raíz principal es no negativa, toda solución debe satisfacer

$$
\boxed{x\ge0.}
$$

La cadena propuesta escribe

$$
\sqrt{x+6}=x
\Longleftrightarrow
x+6=x^2.
$$

Ésta es la primera ruptura. Sin conservar la condición $x\ge0$, elevar al cuadrado sólo garantiza

$$
\sqrt{x+6}=x
\Longrightarrow
x+6=x^2.
$$

La equivalencia completa es

$$
\sqrt{x+6}=x
\Longleftrightarrow
\begin{cases}
x+6=x^2,\\
x\ge0.
\end{cases}
$$

La ecuación algebraica resultante es

$$
x^2-x-6=0,
$$

y factoriza como

$$
(x-3)(x+2)=0.
$$

Por tanto, los candidatos algebraicos son

$$
x=3
\quad\text{o}\quad
x=-2.
$$

Ambos pertenecen al dominio $[-6,\infty)$, pero sólo $3$ satisface la condición acumulada $x\ge0$. En efecto,

$$
\sqrt{3+6}=3,
$$

mientras que una raíz principal no puede ser igual a $-2$.

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{3\}.}
$$

El valor $-2$ es un **candidato adicional creado al perder la información de signo**, no un valor excluido por el dominio.


### Solución 43

La ecuación es

$$
\frac{x^2-9}{x-3}=6.
$$

Antes de simplificar fijamos el dominio:

$$
x-3\neq0,
$$

de modo que

$$
\boxed{D=\mathbb R\setminus\{3\}.}
$$

Factorizamos el numerador:

$$
x^2-9=(x-3)(x+3).
$$

Como $x-3\neq0$ para todo $x\in D$, la cancelación es perfectamente válida **sobre ese dominio**:

$$
\frac{(x-3)(x+3)}{x-3}=6
\Longleftrightarrow
x+3=6,
\qquad x\in D.
$$

Resolviendo la ecuación simplificada obtenemos

$$
x=3.
$$

Pero

$$
3\notin D.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_D=\varnothing.}
$$

La afirmación de que «la cancelación fue ilegítima porque produjo una respuesta falsa» es incorrecta. La cancelación conservó equivalencia en el dominio efectivo. El error aparece **después**, cuando se olvida que la ecuación simplificada sigue interpretándose sobre $D=\mathbb R\setminus\{3\}$.

El daño es un **dominio omitido**. El valor $3$ no fue creado por una transformación no reversible: nunca fue admisible en el problema original.


### Solución 44

La ecuación es

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1}.
$$

Su dominio efectivo es

$$
\boxed{D=\mathbb R\setminus\{1\}.}
$$

En todo $D$ se cumple $x-1\neq0$. Por ello multiplicar ambos miembros por $x-1$ es una equivalencia legítima:

$$
\frac{x+1}{x-1}
=
\frac{2}{x-1}
\Longleftrightarrow
x+1=2,
\qquad x\in D.
$$

La ecuación lineal produce

$$
x=1.
$$

Sin embargo,

$$
1\notin D.
$$

Así,

$$
\boxed{\operatorname{Sol}_D=\varnothing.}
$$

El diagnóstico «$x=1$ es una raíz extraña creada al eliminar denominadores» no es correcto. La eliminación de denominadores fue reversible sobre el dominio vigente y no creó soluciones nuevas.

El valor $1$ es un **valor inadmisible por el dominio original**. La distinción es:

- un candidato extraño por transformación pertenece al dominio original y aparece porque una implicación no reversible amplió el conjunto;
- un valor inadmisible por dominio nunca perteneció al universo en que la ecuación original estaba definida.

Aquí ocurre lo segundo.


### Solución 45

La primera ecuación es

$$
x-2=-3,
$$

y equivale a

$$
x=-1.
$$

Por tanto,

$$
S_1=\{-1\}.
$$

La segunda ecuación es

$$
(x-2)^2=9.
$$

Ésta equivale a

$$
x-2=3
\quad\text{o}\quad
x-2=-3,
$$

de donde

$$
x=5
\quad\text{o}\quad
x=-1.
$$

Así,

$$
S_2=\{-1,5\}.
$$

Como

$$
S_1\subsetneq S_2,
$$

la primera falsa equivalencia es

$$
x-2=-3
\not\Longleftrightarrow
(x-2)^2=9.
$$

La flecha correcta es

$$
\boxed{
x-2=-3
\Longrightarrow
(x-2)^2=9.
}
$$

El cuadrado borra la información de signo y crea el candidato adicional $x=5$.

Para resolver correctamente la ecuación original no necesitamos conservar ese candidato:

$$
x-2=-3
\Longleftrightarrow
x=-1,
$$

por lo que

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-1\}.}
$$


### Solución 46

La ecuación es

$$
(x-1)+(x+2)=0.
$$

El paso defectuoso fue

$$
(x-1)+(x+2)=0
\Longleftrightarrow
x-1=0
\ \text{o}\ 
x+2=0.
$$

Aquí se aplicó fuera de su hipótesis estructural la **propiedad del producto nulo**. Esa propiedad afirma

$$
AB=0
\Longleftrightarrow
A=0
\ \text{o}\ 
B=0,
$$

pero no existe una regla análoga para una suma $A+B=0$.

Resolvemos la ecuación original mediante equivalencias:

$$
(x-1)+(x+2)=0
\Longleftrightarrow
2x+1=0
\Longleftrightarrow
x=-\frac12.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac12\right\}.
}
$$

La resolución defectuosa proponía $\{1,-2\}$. Ninguno de esos valores satisface la ecuación original:

$$
(1-1)+(1+2)=3\neq0,
$$

y

$$
(-2-1)+(-2+2)=-3\neq0.
$$

En este caso la falsa equivalencia produce **candidatos falsos** y, al mismo tiempo, elimina la solución verdadera $-1/2$. No hay una inclusión simple entre los dos conjuntos: el problema es una sustitución estructuralmente inválida de una suma por una disyunción de ceros.


### Solución 47

La sustitución

$$
u=x^2
$$

transforma correctamente

$$
x^4-5x^2+4=0
$$

en

$$
u^2-5u+4=0.
$$

Factorizamos:

$$
(u-1)(u-4)=0,
$$

de modo que

$$
u\in\{1,4\}.
$$

Hasta aquí el cálculo auxiliar es correcto.

La ruptura aparece al declarar

$$
\operatorname{Sol}_{\mathbb R}=\{1,4\}.
$$

Los números $1$ y $4$ son soluciones para la **variable auxiliar $u$**. El problema original pide valores de $x$. La respuesta final tiene, por tanto, el tipo de objeto equivocado y la reconstrucción está incompleta.

Debemos hallar todas las preimágenes reales.

Si

$$
u=1,
$$

entonces

$$
x^2=1
\Longleftrightarrow
x=\pm1.
$$

Si

$$
u=4,
$$

entonces

$$
x^2=4
\Longleftrightarrow
x=\pm2.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-2,-1,1,2\}.
}
$$

El daño se clasifica como **reconstrucción incompleta**: la ecuación auxiliar fue resuelta correctamente, pero no se volvió de la variable $u$ a la variable original $x$.


### Solución 48

Usamos

$$
u=x^2
$$

en

$$
x^4-10x^2+9=0.
$$

La ecuación auxiliar es

$$
u^2-10u+9=0,
$$

que factoriza como

$$
(u-1)(u-9)=0.
$$

Por tanto,

$$
u=1
\quad\text{o}\quad
u=9.
$$

El error ocurre al reconstruir sólo

$$
x=1
\quad\text{o}\quad
x=3.
$$

La función

$$
x\longmapsto x^2
$$

no es inyectiva sobre $\mathbb R$: para todo $u>0$ existen dos preimágenes reales,

$$
x=\sqrt u
\quad\text{y}\quad
x=-\sqrt u.
$$

Así, de

$$
x^2=1
$$

obtenemos

$$
x=\pm1,
$$

y de

$$
x^2=9
$$

obtenemos

$$
x=\pm3.
$$

La solución correcta es

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-3,-1,1,3\}.
}
$$

La pérdida de $-1$ y $-3$ es una **rama omitida durante la reconstrucción de preimágenes**.


### Solución 49

Estudiamos, para cada parámetro real $a$,

$$
(a-2)x=a-2.
$$

La resolución defectuosa divide inmediatamente por $a-2$. Ésa es la primera ruptura, porque todavía no se ha establecido que

$$
a-2\neq0.
$$

Debemos separar casos.

Si

$$
a\neq2,
$$

entonces $a-2\neq0$ y la división es reversible:

$$
(a-2)x=a-2
\Longleftrightarrow
x=1.
$$

Por tanto,

$$
S(a)=\{1\}
\qquad(a\neq2).
$$

Si

$$
a=2,
$$

la ecuación original se convierte en

$$
0\cdot x=0,
$$

es decir,

$$
0=0.
$$

Esta igualdad es verdadera para todo $x\in\mathbb R$, de modo que

$$
S(2)=\mathbb R.
$$

La familia correcta es

$$
\boxed{
S(a)=
\begin{cases}
\{1\}, & a\neq2,\\[4pt]
\mathbb R, & a=2.
\end{cases}
}
$$

El valor excepcional del parámetro es

$$
\boxed{a=2.}
$$

Dividir sin separar ese caso borra una familia completa de soluciones; el daño es una **pérdida del caso paramétrico degenerado**.


### Solución 50

El sistema es

$$
\begin{cases}
y=x^2,\\
x+y=2.
\end{cases}
$$

La sustitución

$$
y=x^2
$$

en la segunda ecuación es correcta y produce

$$
x+x^2=2,
$$

es decir,

$$
x^2+x-2=0.
$$

Factorizamos:

$$
(x+2)(x-1)=0,
$$

de donde

$$
x=-2
\quad\text{o}\quad
x=1.
$$

No hay error en esta ecuación reducida. La ruptura aparece al declarar

$$
\operatorname{Sol}=\{-2,1\}.
$$

Un sistema en las variables $(x,y)$ no tiene como solución un subconjunto de $\mathbb R$, sino un conjunto de **pares ordenados** en $\mathbb R^2$. Falta reconstruir $y$.

Para

$$
x=-2,
$$

tenemos

$$
y=x^2=4,
$$

y obtenemos el par

$$
(-2,4).
$$

Para

$$
x=1,
$$

tenemos

$$
y=x^2=1,
$$

y obtenemos

$$
(1,1).
$$

Ambos pares satisfacen además $x+y=2$:

$$
-2+4=2,
\qquad
1+1=2.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}
=
\{(-2,4),(1,1)\}
\subseteq\mathbb R^2.
}
$$

El daño es una **reconstrucción incompleta** y, además, una declaración del conjunto solución en el espacio equivocado.

## E. Estrategia: elegir ruta y decidir cuándo verificar

En este bloque la resolución incluye una decisión previa: no sólo importa obtener el conjunto solución, sino elegir una representación adecuada y saber si la cadena usada conserva equivalencia. La verificación final se distingue de acuerdo con su función lógica: puede ser necesaria para filtrar candidatos, innecesaria cuando ya se conservaron todas las condiciones equivalentes, o útil sólo como control independiente.


### Solución 51

Consideramos

$$
x^2-9x+20=0.
$$

Antes de operar conviene leer la estructura. La **factorización** parece especialmente prometedora porque buscamos dos enteros cuyo producto sea $20$ y cuya suma sea $9$. Completar cuadrados también es válido, pero introduce fracciones o un paso intermedio menos directo. La fórmula cuadrática es universal, aunque aquí exige calcular un discriminante para obtener información que la factorización ya hace visible.

Buscamos entonces $4$ y $5$:

$$
x^2-9x+20=(x-4)(x-5).
$$

Por tanto,

$$
x^2-9x+20=0
\Longleftrightarrow
(x-4)(x-5)=0
$$

y, por producto nulo,

$$
x=4
\quad\text{o}\quad
x=5.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{4,5\}.}
$$

La factorización es la ruta más eficiente porque la estructura entera es visible inmediatamente y cada paso conserva equivalencia.

Una segunda ruta válida sería la fórmula cuadrática. En efecto, con $a=1$, $b=-9$ y $c=20$ se obtendría el mismo conjunto solución. Debe ocurrir así porque ambas rutas resuelven la **misma ecuación** mediante transformaciones o teoremas equivalentes sobre $\mathbb R$; la elección de método cambia el recorrido, no el conjunto solución.


### Solución 52

La ecuación es

$$
x^2+6x-2=0.
$$

Una factorización elemental con coeficientes enteros no es natural: si escribiéramos

$$
(x+r)(x+s),
$$

necesitaríamos

$$
rs=-2,
\qquad
r+s=6,
$$

y ningún par de enteros con producto $-2$ tiene suma $6$.

Entre completar cuadrados y usar la fórmula cuadrática, completar cuadrados hace especialmente visible la estructura de esta ecuación porque el coeficiente de $x^2$ ya es $1$ y el término lineal es par.

Partimos de

$$
x^2+6x-2=0
\Longleftrightarrow
x^2+6x=2.
$$

Añadimos $9$ a ambos miembros:

$$
x^2+6x+9=11,
$$

de donde

$$
(x+3)^2=11.
$$

Sobre $\mathbb R$,

$$
(x+3)^2=11
\Longleftrightarrow
x+3=\sqrt{11}
\quad\text{o}\quad
x+3=-\sqrt{11}.
$$

Por tanto,

$$
x=-3+\sqrt{11}
\quad\text{o}\quad
x=-3-\sqrt{11},
$$

y

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-3-\sqrt{11},\,-3+\sqrt{11}\}.
}
$$

La fórmula cuadrática habría sido igualmente válida y habría producido las mismas dos raíces. Completar cuadrados resulta aquí más transparente porque revela directamente la forma

$$
(x-h)^2=k.
$$


### Solución 53

Consideramos

$$
6x^2+x-2=0.
$$

#### Ruta a: factorización

Buscamos una descomposición del trinomio. Se verifica que

$$
6x^2+x-2=(3x+2)(2x-1),
$$

porque

$$
(3x+2)(2x-1)=6x^2-3x+4x-2=6x^2+x-2.
$$

Entonces

$$
(3x+2)(2x-1)=0
\Longleftrightarrow
3x+2=0
\quad\text{o}\quad
2x-1=0.
$$

Así,

$$
x=-\frac23
\quad\text{o}\quad
x=\frac12.
$$

#### Ruta b: fórmula cuadrática

Aquí

$$
a=6,
\qquad
b=1,
\qquad
c=-2.
$$

El discriminante es

$$
\Delta
=1^2-4(6)(-2)
=1+48
=49.
$$

Por tanto,

$$
x
=
\frac{-1\pm7}{12}.
$$

Las dos ramas dan

$$
x=\frac6{12}=\frac12
$$

y

$$
x=\frac{-8}{12}=-\frac23.
$$

En ambos casos,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{-\frac23,\frac12\right\}.
}
$$

La factorización usa menos cálculo numérico una vez reconocida la descomposición y hace visibles las dos ramas en cuanto aparece el producto nulo. La fórmula cuadrática es sistemática, pero obliga a identificar $a,b,c$, calcular $\Delta$, extraer su raíz y manejar cuidadosamente los signos en $-b\pm\sqrt\Delta$.

Si sólo necesitara el conjunto solución, preferiría **factorizar**: en esta ecuación la factorización es corta, exacta y expone las raíces con menos oportunidades de error aritmético o de signo.


### Solución 54

La ecuación es

$$
x^2-8x+16=0.
$$

Antes de calcular debe gobernar la elección de método un rasgo visible: el trinomio es un **cuadrado perfecto**, pues

$$
x^2-8x+16=(x-4)^2.
$$

La ruta más económica es, por tanto,

$$
(x-4)^2=0
\Longleftrightarrow
x-4=0
\Longleftrightarrow
x=4.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{4\}.}
$$

Usamos ahora el discriminante sólo como control estructural independiente:

$$
\Delta=(-8)^2-4(1)(16)=64-64=0.
$$

El valor $\Delta=0$ confirma que la cuadrática tiene una única solución real, o una raíz doble en sentido algebraico, exactamente lo que mostraba la forma $(x-4)^2$.

Aplicar directamente la fórmula cuadrática habría sido correcto, pero estratégicamente innecesario: habría introducido más notación y más operaciones para recuperar una estructura que ya estaba visible en el polinomio original.


### Solución 55

Consideramos

$$
2x^2+4x+7=0
$$

sobre $\mathbb R$.

Como la pregunta principal es decidir con el menor trabajo si existen soluciones reales, conviene calcular primero el **discriminante**. Con

$$
a=2,
\qquad
b=4,
\qquad
c=7,
$$

obtenemos

$$
\Delta
=4^2-4(2)(7)
=16-56
=-40.
$$

Como

$$
\Delta<0,
$$

la ecuación no tiene soluciones reales. Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\varnothing.}
$$

Intentar factorizar sobre los reales no aporta una decisión más rápida. Completar cuadrados también funciona —de hecho,

$$
2x^2+4x+7
=2(x+1)^2+5>0
$$

para todo real $x$—, pero el discriminante decide inmediatamente el régimen real sin necesidad de continuar hasta calcular raíces complejas, que quedan fuera del dominio de este capítulo.


### Solución 56

Resolvemos

$$
x^2-2x-1=0
$$

por dos rutas.

#### Ruta a: completar cuadrados

Movemos la constante:

$$
x^2-2x=1.
$$

Añadimos $1$ a ambos miembros:

$$
x^2-2x+1=2,
$$

de modo que

$$
(x-1)^2=2.
$$

Entonces

$$
x-1=\pm\sqrt2,
$$

y por tanto

$$
x=1\pm\sqrt2.
$$

#### Ruta b: fórmula cuadrática

Tenemos

$$
a=1,
\qquad
b=-2,
\qquad
c=-1.
$$

El discriminante es

$$
\Delta=(-2)^2-4(1)(-1)=8.
$$

Por la fórmula,

$$
x
=
\frac{2\pm\sqrt8}{2}
=
\frac{2\pm2\sqrt2}{2}
=1\pm\sqrt2.
$$

En ambas rutas,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{1-\sqrt2,\,1+\sqrt2\}.
}
$$

Completar cuadrados hace visible de manera inmediata la forma

$$
(x-h)^2=k,
$$

aquí con $h=1$ y $k=2$. La fórmula cuadrática es más mecánica porque puede aplicarse siguiendo un algoritmo uniforme a cualquier cuadrática con $a\neq0$.

Pero «más mecánica» no significa necesariamente «más conveniente»: una estrategia puede ser general y, sin embargo, introducir más cálculo del necesario o esconder una estructura que la ecuación ya sugiere. La elección óptima depende de la forma concreta del problema.


### Solución 57

La ecuación es

$$
\frac{x^2-9}{x-3}=6.
$$

La estrategia propuesta es lógicamente sólida **si el dominio se conserva durante toda la cadena**.

Primero fijamos

$$
D=\mathbb R\setminus\{3\}.
$$

Factorizamos el numerador mediante una identidad:

$$
x^2-9=(x-3)(x+3).
$$

Por tanto,

$$
\frac{(x-3)(x+3)}{x-3}=6,
\qquad x\in D.
$$

Como $x-3\neq0$ para todo $x\in D$, la cancelación es reversible sobre el dominio efectivo:

$$
\frac{(x-3)(x+3)}{x-3}=6
\Longleftrightarrow
x+3=6,
\qquad x\in D.
$$

La ecuación lineal da

$$
x=3.
$$

Pero

$$
3\notin D.
$$

Luego

$$
\boxed{\operatorname{Sol}_D=\varnothing.}
$$

Después de filtrar por pertenencia al dominio, sustituir de nuevo cada valor en la ecuación original **no es lógicamente necesario**. Todas las transformaciones utilizadas fueron equivalencias sobre $D$, y el único valor algebraico obtenido fue descartado porque nunca perteneció al dominio original. Una sustitución final puede servir como control independiente cuando quedan valores admisibles, pero no es lo que restaura la corrección lógica de esta resolución: la corrección ya está garantizada por haber conservado el dominio y usado equivalencias válidas.


### Solución 58

Consideramos

$$
\sqrt{x+4}=x.
$$

La raíz está definida para

$$
x\ge-4.
$$

Compararemos las dos rutas propuestas.

#### Ruta A: cuadrar por implicación y verificar candidatos

De la ecuación original se sigue

$$
\sqrt{x+4}=x
\Longrightarrow
x+4=x^2.
$$

No escribimos una equivalencia, porque al cuadrar se pierde la información de que el miembro derecho debe ser no negativo.

La ecuación cuadrática es

$$
x^2-x-4=0,
$$

y produce los candidatos

$$
x=\frac{1\pm\sqrt{17}}2.
$$

Debemos verificar ambos en la ecuación original.

Sea

$$
\alpha=\frac{1+\sqrt{17}}2.
$$

Tenemos $\alpha>0$ y, como satisface $\alpha^2=\alpha+4$,

$$
\sqrt{\alpha+4}
=\sqrt{\alpha^2}
=|\alpha|
=\alpha.
$$

Por tanto, $\alpha$ sí es solución.

Sea ahora

$$
\beta=\frac{1-\sqrt{17}}2.
$$

Entonces $\beta<0$, mientras que $\sqrt{\beta+4}\ge0$. Por ello no puede cumplirse

$$
\sqrt{\beta+4}=\beta.
$$

Así, $\beta$ es un candidato extraño generado por el cuadrado.

#### Ruta B: conservar la condición de signo

Usamos la equivalencia completa

$$
\sqrt{x+4}=x
\Longleftrightarrow
\begin{cases}
x+4=x^2,\\
x\ge0.
\end{cases}
$$

La misma cuadrática da

$$
x=\frac{1\pm\sqrt{17}}2,
$$

pero la condición $x\ge0$ conserva solamente

$$
x=\frac{1+\sqrt{17}}2.
$$

Por tanto, por ambas rutas,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\left\{\frac{1+\sqrt{17}}2\right\}.
}
$$

En la ruta A la verificación final es **necesaria** porque la cadena contiene una implicación que puede ampliar el conjunto de candidatos. En la ruta B la condición de signo forma parte de la transformación y restablece una equivalencia exacta; una comprobación final puede hacerse como control, pero ya no es necesaria para reparar la lógica de la resolución.


### Solución 59

La ecuación es

$$
|2x-3|=7.
$$

Como $7>0$, la definición del valor absoluto proporciona una **equivalencia exacta**:

$$
|2x-3|=7
\Longleftrightarrow
2x-3=7
\quad\text{o}\quad
2x-3=-7.
$$

Por tanto, abrir las dos ramas no crea candidatos adicionales ni pierde soluciones. En consecuencia, una verificación final en la ecuación original **no es necesaria para recuperar corrección lógica**. Puede usarse como control independiente.

Esto difiere de una ecuación radical simplemente elevada al cuadrado. En ese caso, en general sólo tenemos una implicación

$$
A=B\Longrightarrow A^2=B^2,
$$

porque el cuadrado puede borrar información de signo y ampliar el conjunto de candidatos. Aquí, en cambio, las dos ramas son precisamente la caracterización completa de $|A|=c$ cuando $c>0$.

Resolvemos:

$$
2x-3=7
\Longleftrightarrow
2x=10
\Longleftrightarrow
x=5,
$$

y

$$
2x-3=-7
\Longleftrightarrow
2x=-4
\Longleftrightarrow
x=-2.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-2,5\}.}
$$


### Solución 60

La función de la verificación depende de la fuerza lógica de la cadena que la precede. Clasificamos cada planificación **antes** de calcular.

#### a) Factorizar y aplicar producto nulo

La ecuación es

$$
x^2-5x+6=0.
$$

La identidad

$$
x^2-5x+6=(x-2)(x-3)
$$

y la propiedad del producto nulo producen equivalencias:

$$
x^2-5x+6=0
\Longleftrightarrow
(x-2)(x-3)=0
\Longleftrightarrow
x=2\ \text{o}\ x=3.
$$

Así,

$$
\operatorname{Sol}_{\mathbb R}=\{2,3\}.
$$

La verificación final es **útil sólo como control independiente**. No es necesaria para filtrar candidatos, porque no hubo ninguna ampliación del conjunto solución.

#### b) Eliminar un denominador sobre el dominio efectivo

Consideramos

$$
\frac{x+2}{x-1}=3,
$$

con

$$
D=\mathbb R\setminus\{1\}.
$$

Como $x-1\neq0$ en todo $D$, multiplicar por $x-1$ conserva equivalencia:

$$
\frac{x+2}{x-1}=3
\Longleftrightarrow
x+2=3(x-1),
\qquad x\in D.
$$

Entonces

$$
x+2=3x-3
\Longleftrightarrow
5=2x
\Longleftrightarrow
x=\frac52.
$$

Como $5/2\in D$,

$$
\operatorname{Sol}_D
=
\left\{\frac52\right\}.
$$

La verificación final es **innecesaria si se conserva correctamente el dominio**. La eliminación del denominador fue reversible sobre $D$. Sustituir $5/2$ en la ecuación original sería sólo un control adicional.

#### c) Cuadrar sin registrar la condición de signo

Tenemos

$$
\sqrt{x+1}=x-1.
$$

Si se cuadra sin conservar la condición $x-1\ge0$, sólo podemos escribir

$$
\sqrt{x+1}=x-1
\Longrightarrow
x+1=(x-1)^2.
$$

La ecuación cuadrada da

$$
x+1=x^2-2x+1
\Longleftrightarrow
x(x-3)=0,
$$

de modo que aparecen los candidatos

$$
x=0
\quad\text{o}\quad
x=3.
$$

Aquí la verificación final es **necesaria para filtrar candidatos**. En efecto,

$$
\sqrt{0+1}=1\neq-1,
$$

por lo que $0$ es extraño, mientras que

$$
\sqrt{3+1}=2=3-1.
$$

Así, el conjunto solución original es

$$
\{3\}.
$$

#### d) Abrir ramas equivalentes de un valor absoluto

Consideramos

$$
|3x+1|=5.
$$

Como $5>0$,

$$
|3x+1|=5
\Longleftrightarrow
3x+1=5
\quad\text{o}\quad
3x+1=-5.
$$

La ramificación es una equivalencia exacta. Resolvemos:

$$
x=\frac43
\quad\text{o}\quad
x=-2.
$$

Por tanto,

$$
\operatorname{Sol}_{\mathbb R}
=
\left\{-2,\frac43\right\}.
$$

La verificación final es **útil sólo como control independiente**. No es necesaria para restablecer la corrección lógica porque la apertura de ramas ya preserva exactamente el conjunto solución.

En resumen, la pregunta decisiva no es «¿conviene comprobar siempre?», sino **qué relación lógica produjo la cadena**. Una cadena de equivalencias ya caracteriza exactamente el conjunto solución; una implicación no reversible puede dejar candidatos y exige filtrarlos; conservar explícitamente dominio y condiciones de signo puede convertir una ruta aparentemente peligrosa en una cadena nuevamente equivalente.

## F. Transferencia: parámetros, dominios heredados, sustituciones y sistemas

En este bloque las técnicas anteriores se transfieren a situaciones donde el cálculo debe convivir con parámetros, dominios heredados, sustituciones no biyectivas y reconstrucción de pares ordenados. En cada ejercicio distinguimos el problema original de las ecuaciones auxiliares y regresamos al objeto solución correcto.


### Solución 61

Consideramos, para cada $a\in\mathbb R$,

$$
(a-2)x=a^2-4.
$$

Factorizamos el miembro derecho:

$$
a^2-4=(a-2)(a+2).
$$

El factor que querríamos cancelar es $a-2$, de modo que el valor excepcional es

$$
\boxed{a=2.}
$$

Si $a\neq2$, entonces $a-2\neq0$ y podemos dividir ambos miembros por ese factor conservando equivalencia:

$$
(a-2)x=(a-2)(a+2)
\Longleftrightarrow
x=a+2.
$$

Por tanto,

$$
S(a)=\{a+2\}
\qquad(a\neq2).
$$

Si $a=2$, la ecuación original se convierte en

$$
0\cdot x=0,
$$

es decir,

$$
0=0.
$$

Esta proposición es verdadera para todo $x\in\mathbb R$, de modo que

$$
S(2)=\mathbb R.
$$

La familia completa es

$$
\boxed{
S(a)=
\begin{cases}
\{a+2\}, & a\neq2,\\[4pt]
\mathbb R, & a=2.
\end{cases}
}
$$

El caso excepcional no puede obtenerse cancelando primero y «sustituyendo después»: la cancelación sólo estaba autorizada bajo la hipótesis $a\neq2$.


### Solución 62

Estudiamos

$$
a(a+1)x=a+1.
$$

Los valores que pueden cambiar la validez de una división son aquellos que anulan $a$ o $a+1$:

$$
a=0
\qquad\text{y}\qquad
a=-1.
$$

Conviene separar ambos antes de dividir.

Si $a=-1$, obtenemos

$$
(-1)(0)x=0,
$$

es decir,

$$
0=0.
$$

Por tanto,

$$
S(-1)=\mathbb R.
$$

Si $a=0$, la ecuación se transforma en

$$
0\cdot1\cdot x=1,
$$

esto es,

$$
0=1,
$$

una contradicción. Luego

$$
S(0)=\varnothing.
$$

Supongamos ahora

$$
a\neq0,-1.
$$

Entonces $a\neq0$ y $a+1\neq0$, por lo que podemos dividir por $a+1$:

$$
a(a+1)x=a+1
\Longleftrightarrow
ax=1.
$$

Como además $a\neq0$,

$$
ax=1
\Longleftrightarrow
x=\frac1a.
$$

Así,

$$
\boxed{
S(a)=
\begin{cases}
\mathbb R, & a=-1,\\[4pt]
\varnothing, & a=0,\\[4pt]
\left\{\dfrac1a\right\}, & a\in\mathbb R\setminus\{-1,0\}.
\end{cases}
}
$$

Aparecen exactamente los tres regímenes solicitados: todo $\mathbb R$, el conjunto vacío y un singleton.


### Solución 63

Para cada $a\in\mathbb R$ consideramos

$$
\frac{x-2}{x-a}=0.
$$

El denominador exige

$$
x-a\neq0,
$$

de modo que el dominio efectivo depende del parámetro:

$$
\boxed{D_a=\mathbb R\setminus\{a\}.}
$$

Una fracción definida vale cero exactamente cuando su numerador vale cero. Por tanto, el único valor algebraicamente posible es

$$
x-2=0
\Longleftrightarrow
x=2.
$$

Ahora debemos preguntar si $2\in D_a$. Esto ocurre si y sólo si

$$
a\neq2.
$$

Por consiguiente, si $a\neq2$,

$$
S(a)=\{2\}.
$$

En cambio, si $a=2$, el único cero posible del numerador coincide con el valor excluido por el denominador. Entonces

$$
S(2)=\varnothing.
$$

La familia completa es

$$
\boxed{
S(a)=
\begin{cases}
\{2\}, & a\neq2,\\[4pt]
\varnothing, & a=2.
\end{cases}
}
$$

Este ejercicio es paramétrico porque $a$ modifica la familia $S(a)$ y, simultáneamente, es una transferencia directa de C20 porque el parámetro modifica también el **dominio efectivo**. El valor $x=2$ no «deja de satisfacer» el numerador cuando $a=2$; deja de ser admisible en el problema original.


### Solución 64

Consideramos

$$
\frac{x^2-9}{x^2-x-6}=0.
$$

Factorizamos numerador y denominador:

$$
x^2-9=(x-3)(x+3)
$$

y

$$
x^2-x-6=(x-3)(x+2).
$$

El denominador se anula en

$$
x=3
\qquad\text{o}\qquad
x=-2,
$$

de modo que el dominio efectivo es

$$
\boxed{D=\mathbb R\setminus\{-2,3\}.}
$$

Los ceros del numerador son

$$
x=3
\qquad\text{o}\qquad
x=-3.
$$

Para que la fracción sea cero, además del numerador nulo el denominador debe estar definido. El valor

$$
x=3
$$

es algebraicamente cero del numerador, pero

$$
3\notin D,
$$

por lo que es inadmisible. En cambio,

$$
-3\in D.
$$

Así,

$$
\boxed{\operatorname{Sol}_D=\{-3\}.}
$$

El factor común $x-3$ podría cancelarse **sobre $D$**, pero esa simplificación no reintroduciría $x=3$: la restricción pertenece al problema original y debe conservarse.


### Solución 65

La ecuación es

$$
\sqrt{(x-1)^2}=3.
$$

Usamos la identidad heredada de C18

$$
\sqrt{u^2}=|u|
\qquad(u\in\mathbb R).
$$

Con $u=x-1$ obtenemos la equivalencia

$$
\sqrt{(x-1)^2}=3
\Longleftrightarrow
|x-1|=3.
$$

Como $3>0$,

$$
|x-1|=3
\Longleftrightarrow
x-1=3
\quad\text{o}\quad
x-1=-3.
$$

La primera rama da

$$
x=4,
$$

y la segunda,

$$
x=-2.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-2,4\}.}
$$

Toda la resolución se construyó mediante equivalencias. No fue necesario elevar al cuadrado ni introducir candidatos que después debieran filtrarse.


### Solución 66

Debemos resolver

$$
\sqrt{(2x-1)^2}=7.
$$

#### Ruta a: convertir la raíz principal en valor absoluto

Por

$$
\sqrt{u^2}=|u|,
$$

tenemos

$$
\sqrt{(2x-1)^2}=7
\Longleftrightarrow
|2x-1|=7.
$$

Como $7>0$,

$$
|2x-1|=7
\Longleftrightarrow
2x-1=7
\quad\text{o}\quad
2x-1=-7.
$$

De la primera rama,

$$
2x=8
\Longleftrightarrow
x=4,
$$

y de la segunda,

$$
2x=-6
\Longleftrightarrow
x=-3.
$$

Así,

$$
\operatorname{Sol}_{\mathbb R}=\{-3,4\}.
$$

#### Ruta b: cuadrar y tratar los resultados como candidatos

Si usamos únicamente la dirección siempre segura,

$$
\sqrt{(2x-1)^2}=7
\Longrightarrow
(2x-1)^2=49.
$$

La ecuación cuadrada es equivalente a

$$
2x-1=7
\quad\text{o}\quad
2x-1=-7,
$$

y produce los candidatos

$$
x=4
\quad\text{o}\quad
x=-3.
$$

Los verificamos en la ecuación original:

$$
\sqrt{(2\cdot4-1)^2}=\sqrt{49}=7,
$$

y

$$
\sqrt{(2(-3)-1)^2}=\sqrt{49}=7.
$$

Ambos sobreviven, de modo que nuevamente

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{-3,4\}.}
$$

La primera ruta conserva mejor la información porque la identidad $\sqrt{u^2}=|u|$ registra de inmediato las dos posibilidades de signo. En este caso particular, como el otro miembro es $7\ge0$, también puede justificarse que el cuadrado sea reversible; pero si se adopta la lectura conservadora de la ruta b, la verificación final recupera exactamente el mismo conjunto solución.


### Solución 67

Partimos de

$$
(x^2-1)^2-5(x^2-1)+4=0.
$$

#### Nivel 1: ecuación original en $x$

La expresión repetida sugiere la sustitución

$$
u=x^2-1.
$$

Como $x\in\mathbb R$,

$$
x^2\ge0,
$$

y por tanto la imagen de la sustitución satisface

$$
u\ge-1.
$$

#### Nivel 2: ecuación auxiliar

Sustituyendo,

$$
u^2-5u+4=0.
$$

Factorizamos:

$$
(u-1)(u-4)=0,
$$

de modo que

$$
u=1
\quad\text{o}\quad
u=4.
$$

Ambos valores pertenecen a la imagen permitida $[-1,\infty)$.

#### Nivel 3: reconstrucción de preimágenes

Si $u=1$,

$$
x^2-1=1
\Longleftrightarrow
x^2=2
\Longleftrightarrow
x=\pm\sqrt2.
$$

Si $u=4$,

$$
x^2-1=4
\Longleftrightarrow
x^2=5
\Longleftrightarrow
x=\pm\sqrt5.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}
=
\{-\sqrt5,-\sqrt2,\sqrt2,\sqrt5\}.
}
$$

Los valores $u=1$ y $u=4$ resuelven sólo la ecuación auxiliar. El problema original queda resuelto únicamente después de reconstruir **todas** sus preimágenes reales.


### Solución 68

Consideramos

$$
(x-1)^4-10(x-1)^2+9=0.
$$

La cantidad repetida es $(x-1)^2$, así que definimos

$$
u=(x-1)^2.
$$

Como $x$ es real,

$$
\boxed{u\ge0.}
$$

Además,

$$
(x-1)^4=u^2,
$$

de modo que la ecuación auxiliar es

$$
u^2-10u+9=0.
$$

Factorizamos:

$$
(u-1)(u-9)=0.
$$

Así,

$$
u=1
\quad\text{o}\quad
u=9.
$$

Ambos valores son positivos y, por tanto, realizables.

Reconstruimos ahora todas las preimágenes.

Para $u=1$,

$$
(x-1)^2=1
\Longleftrightarrow
x-1=\pm1,
$$

de donde

$$
x=0
\quad\text{o}\quad
x=2.
$$

Para $u=9$,

$$
(x-1)^2=9
\Longleftrightarrow
x-1=\pm3,
$$

y entonces

$$
x=-2
\quad\text{o}\quad
x=4.
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}_{\mathbb R}=\{-2,0,2,4\}.
}
$$

La razón por la que cada valor auxiliar positivo produce dos preimágenes es que

$$
(x-1)^2=u>0
\Longleftrightarrow
x=1\pm\sqrt u.
$$

La sustitución no es biyectiva: comprime dos valores simétricos alrededor de $1$ en un mismo valor de $u$.


### Solución 69

Trabajamos desde el comienzo sobre

$$
D=\mathbb R\setminus\{1\}.
$$

La ecuación es

$$
\left(\frac{x+1}{x-1}\right)^2
-
5\left(\frac{x+1}{x-1}\right)
+6=0.
$$

Definimos

$$
u=\frac{x+1}{x-1},
\qquad x\in D.
$$

La sustitución no borra el dominio de procedencia: durante toda la resolución seguimos exigiendo $x\neq1$.

La ecuación auxiliar es

$$
u^2-5u+6=0,
$$

y factoriza como

$$
(u-2)(u-3)=0.
$$

Por tanto,

$$
u=2
\quad\text{o}\quad
u=3.
$$

Reconstruimos $x$.

Si $u=2$,

$$
\frac{x+1}{x-1}=2.
$$

Como $x\in D$, podemos multiplicar por $x-1$ conservando equivalencia:

$$
x+1=2(x-1)
\Longleftrightarrow
x+1=2x-2
\Longleftrightarrow
x=3.
$$

Y

$$
3\in D.
$$

Si $u=3$,

$$
\frac{x+1}{x-1}=3
\Longleftrightarrow
x+1=3(x-1)
\Longleftrightarrow
x+1=3x-3
\Longleftrightarrow
x=2.
$$

También

$$
2\in D.
$$

Por tanto,

$$
\boxed{\operatorname{Sol}_D=\{2,3\}.}
$$

El dominio heredado cumple dos funciones: autoriza las multiplicaciones por $x-1$ durante la reconstrucción y evita que una ecuación auxiliar se interprete fuera del problema original.


### Solución 70

Consideramos el sistema sobre $\mathbb R^2$:

$$
\begin{cases}
y=x^2,\\
x+y=12.
\end{cases}
$$

Sustituimos la primera ecuación en la segunda:

$$
x+x^2=12.
$$

Por tanto,

$$
x^2+x-12=0.
$$

Factorizamos:

$$
(x+4)(x-3)=0,
$$

de modo que

$$
x=-4
\quad\text{o}\quad
x=3.
$$

Reconstruimos ahora la segunda coordenada mediante $y=x^2$.

Si $x=-4$,

$$
y=16,
$$

y obtenemos

$$
(-4,16).
$$

Si $x=3$,

$$
y=9,
$$

y obtenemos

$$
(3,9).
$$

Ambos pares satisfacen $x+y=12$. Por tanto,

$$
\boxed{
\operatorname{Sol}
=
\{(-4,16),(3,9)\}
\subseteq\mathbb R^2.
}
$$

Los valores $x=-4$ y $x=3$ son soluciones de la ecuación reducida, no todavía soluciones completas del sistema hasta reconstruir $y$.


### Solución 71

El sistema es

$$
\begin{cases}
x+y=7,\\
xy=10.
\end{cases}
$$

De la primera ecuación,

$$
y=7-x.
$$

Sustituimos en $xy=10$:

$$
x(7-x)=10.
$$

Entonces

$$
7x-x^2=10
\Longleftrightarrow
x^2-7x+10=0.
$$

Factorizamos:

$$
(x-2)(x-5)=0.
$$

Por tanto,

$$
x=2
\quad\text{o}\quad
x=5.
$$

Reconstruimos $y$.

Si $x=2$,

$$
y=7-2=5,
$$

y obtenemos $(2,5)$. Si $x=5$,

$$
y=7-5=2,
$$

y obtenemos $(5,2)$.

Así,

$$
\boxed{
\operatorname{Sol}
=
\{(2,5),(5,2)\}.
}
$$

La aparición de los dos pares es también esperable por simetría. Las ecuaciones

$$
x+y=7
\qquad\text{y}\qquad
xy=10
$$

no cambian si intercambiamos $x$ e $y$. Por eso, si $(r,s)$ es solución con $r\neq s$, entonces $(s,r)$ satisface automáticamente el mismo sistema.


### Solución 72

Consideramos

$$
\begin{cases}
x^2+y^2=20,\\
x^2-y^2=12.
\end{cases}
$$

Sumamos las dos ecuaciones:

$$
2x^2=32,
$$

de donde

$$
x^2=16.
$$

Restamos la segunda ecuación de la primera:

$$
2y^2=8,
$$

y por tanto

$$
y^2=4.
$$

Estas combinaciones son reversibles: a partir de $x^2=16$ y $y^2=4$ recuperamos

$$
x^2+y^2=20
$$

y

$$
x^2-y^2=12.
$$

Reconstruimos ahora los signos:

$$
x=\pm4,
\qquad
y=\pm2.
$$

Como las ecuaciones originales sólo dependen de $x^2$ y $y^2$, las cuatro combinaciones satisfacen simultáneamente el sistema:

$$
(-4,-2),
\quad
(-4,2),
\quad
(4,-2),
\quad
(4,2).
$$

Por tanto,

$$
\boxed{
\operatorname{Sol}
=
\{(-4,-2),(-4,2),(4,-2),(4,2)\}.
}
$$

Aquí la reconstrucción de signos es parte esencial de la resolución: conocer sólo $x^2$ y $y^2$ no determina todavía los pares ordenados de $\mathbb R^2$.

## G. Síntesis avanzada: trazabilidad completa

En este bloque final la resolución no viene gobernada por una técnica única. Cada solución debe conservar simultáneamente dominio, fuerza lógica de las transformaciones, candidatos, ramas, reconstrucciones y forma correcta del objeto solución.


### Solución 73

Consideramos

$$
\sqrt{3x+10}=x+2.
$$

El radical exige

$$
3x+10\ge0,
$$

por lo que el dominio de la ecuación original es

$$
D=\left[-\frac{10}{3},\infty\right).
$$

Partimos ahora de la cadena propuesta. Si una igualdad es verdadera, sus cuadrados también son iguales; sin embargo, elevar al cuadrado puede borrar información de signo. Por eso el primer paso seguro es sólo

$$
\sqrt{3x+10}=x+2
\Longrightarrow
3x+10=(x+2)^2.
$$

A partir de allí las transformaciones son reversibles:

$$
3x+10=(x+2)^2
\Longleftrightarrow
3x+10=x^2+4x+4
$$

$$
\Longleftrightarrow
x^2+x-6=0
\Longleftrightarrow
(x-2)(x+3)=0
$$

$$
\Longleftrightarrow
x=2\ \text{o}\ x=-3.
$$

La **primera ruptura de equivalencia** es, por tanto, el cuadrado inicial. El conjunto producido por la cadena algebraica es el conjunto de candidatos

$$
C=\{-3,2\}.
$$

Ambos valores pertenecen al dominio original, pues

$$
-3\ge-\frac{10}{3}.
$$

Debemos volver a la ecuación original. Para $x=2$,

$$
\sqrt{3(2)+10}=\sqrt{16}=4=2+2,
$$

por lo que $2$ sí es solución. Para $x=-3$,

$$
\sqrt{3(-3)+10}=\sqrt1=1,
$$

mientras que

$$
-3+2=-1.
$$

Así, $-3$ es un candidato extraño creado por la pérdida de información de signo. En consecuencia,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{2\}.}
$$

La información adicional que convierte el primer cuadrado en una equivalencia completa es el signo del miembro derecho. Para una raíz principal aislada,

$$
\sqrt{3x+10}=x+2
\Longleftrightarrow
\begin{cases}
3x+10=(x+2)^2,\\
x+2\ge0.
\end{cases}
$$

La condición

$$
x+2\ge0
$$

elimina inmediatamente $x=-3$ y conserva $x=2$.


### Solución 74

La ecuación es

$$
\frac{x^2}{x-1}=\frac1{x-1}.
$$

Antes de operar fijamos el dominio efectivo:

$$
x-1\neq0,
$$

de modo que

$$
D=\mathbb R\setminus\{1\}.
$$

En todo $D$, el factor $x-1$ es no nulo. Por eso multiplicar ambos miembros por él es una transformación reversible **sobre ese dominio**:

$$
\frac{x^2}{x-1}=\frac1{x-1}
\Longleftrightarrow
x^2=1,
\qquad x\in D.
$$

Sobre los reales,

$$
x^2=1
\Longleftrightarrow
x=1\ \text{o}\ x=-1.
$$

Pero la ecuación transformada sigue interpretándose sobre $D$. El valor $1$ no pertenece al dominio original, mientras que $-1$ sí. Por tanto,

$$
\boxed{
\operatorname{Sol}_{D}=\{-1\}.
}
$$

El valor $x=1$ no es un candidato extraño creado por una transformación no reversible. La multiplicación por $x-1$ fue reversible en todo el dominio vigente. Lo que ocurre es distinto: $1$ es una raíz algebraica de $x^2=1$ **si esa ecuación se mira sobre todo $\mathbb R$**, pero nunca perteneció al universo de valores admisibles del problema original.

Así se separan dos fenómenos:

- candidato extraño: aparece tras ampliar el conjunto mediante una implicación no reversible;
- valor inadmisible: queda fuera porque nunca perteneció al dominio del problema.

Aquí sólo ocurre el segundo.


### Solución 75

Consideramos

$$
\sqrt{x+8}+\sqrt{x}=2.
$$

El dominio exige simultáneamente

$$
x+8\ge0
\qquad\text{y}\qquad
x\ge0,
$$

por lo que

$$
D=[0,\infty).
$$

#### Ruta A — control lógico

En $D$, el miembro izquierdo es no negativo y el miembro derecho vale $2>0$. Por tanto, cuadrar la igualdad completa conserva equivalencia:

$$
\sqrt{x+8}+\sqrt{x}=2
$$

$$
\Longleftrightarrow
x+8+x+2\sqrt{x(x+8)}=4.
$$

Simplificando,

$$
2\sqrt{x(x+8)}=-2x-4,
$$

y entonces

$$
\sqrt{x(x+8)}=-x-2.
$$

Pero para todo $x\in D$ se cumple

$$
\sqrt{x(x+8)}\ge0,
$$

mientras que

$$
-x-2\le-2<0.
$$

Los dos miembros no pueden ser iguales. Por tanto, la ecuación no tiene soluciones reales:

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\varnothing.}
$$

La Ruta A cierra el problema aquí, sin necesidad de un segundo cuadrado.

#### Ruta B — continuación algebraica

Supongamos que ignoramos provisionalmente la incompatibilidad de signos y elevamos al cuadrado

$$
\sqrt{x(x+8)}=-x-2.
$$

Sólo podemos afirmar la implicación

$$
\sqrt{x(x+8)}=-x-2
\Longrightarrow
x(x+8)=(x+2)^2.
$$

Entonces

$$
x^2+8x=x^2+4x+4,
$$

de donde

$$
4x=4
\Longleftrightarrow
x=1.
$$

El valor $1$ es un candidato producido después del segundo cuadrado. Lo verificamos en la ecuación original:

$$
\sqrt{1+8}+\sqrt1
=3+1
=4\neq2.
$$

Por tanto, $1$ es extraño.

La primera operación que permitió ampliar el conjunto fue **el segundo cuadrado**, aplicado a una igualdad en la que el lado izquierdo era no negativo y el derecho era negativo en todo el dominio. La Ruta A conserva esa información de signo y detecta de inmediato la imposibilidad; la Ruta B la borra y por eso necesita filtrar el candidato falso al final.


### Solución 76

Para cada $a\in\mathbb R$ estudiamos

$$
(a-1)(x^2-a)=0.
$$

El primer valor excepcional es

$$
a=1,
$$

porque entonces el primer factor se anula para todo $x$:

$$
(1-1)(x^2-1)=0.
$$

La ecuación se reduce a $0=0$, de modo que

$$
S(1)=\mathbb R.
$$

Supongamos ahora

$$
a\neq1.
$$

Entonces $a-1\neq0$, y dividir por ese factor constante es reversible:

$$
(a-1)(x^2-a)=0
\Longleftrightarrow
x^2=a.
$$

La clasificación depende ahora del signo de $a$.

Si

$$
a<0,
$$

ningún cuadrado real puede valer $a$, por lo que

$$
S(a)=\varnothing.
$$

Si

$$
a=0,
$$

entonces

$$
x^2=0
\Longleftrightarrow
x=0,
$$

y

$$
S(0)=\{0\}.
$$

Si

$$
a>0
\quad\text{y}\quad
a\neq1,
$$

entonces

$$
x^2=a
\Longleftrightarrow
x=\sqrt a\ \text{o}\ x=-\sqrt a,
$$

de modo que

$$
S(a)=\{-\sqrt a,\sqrt a\}.
$$

La familia completa es

$$
\boxed{
S(a)=
\begin{cases}
\varnothing, & a<0,\\[4pt]
\{0\}, & a=0,\\[4pt]
\{-\sqrt a,\sqrt a\}, & a>0,\ a\neq1,\\[4pt]
\mathbb R, & a=1.
\end{cases}
}
$$

Los cuatro casos son mutuamente excluyentes y cubren todos los números reales. Aparecen exactamente los cuatro tipos pedidos: vacío, singleton, conjunto finito de dos elementos y todo $\mathbb R$.


### Solución 77

La ecuación es

$$
(x-1)^4+3(x-1)^2-4=0.
$$

La estructura sugiere sustituir

$$
u=(x-1)^2.
$$

Esta elección convierte la cuarta potencia en $u^2$ y, además, tiene una restricción de imagen que debemos conservar:

$$
u\in[0,\infty).
$$

La ecuación auxiliar es

$$
u^2+3u-4=0.
$$

Factorizamos:

$$
(u+4)(u-1)=0,
$$

de donde

$$
u=-4
\quad\text{o}\quad
u=1.
$$

El valor $u=-4$ no pertenece a la imagen real de la sustitución $u=(x-1)^2$, así que no tiene preimágenes reales. El valor $u=1$ sí es admisible.

Reconstruimos:

$$
(x-1)^2=1
\Longleftrightarrow
x-1=1\ \text{o}\ x-1=-1.
$$

Por tanto,

$$
x=2
\quad\text{o}\quad
x=0.
$$

Así,

$$
\boxed{\operatorname{Sol}_{\mathbb R}=\{0,2\}.}
$$

La variable auxiliar sólo organiza la estructura. El conjunto solución del problema original debe expresarse en $x$. Además, este ejemplo muestra que resolver la ecuación en $u$ no basta: hay que filtrar por la imagen de la sustitución y reconstruir todas las preimágenes reales de cada valor admisible.


### Solución 78

Consideramos

$$
\left|\frac{x-3}{x+1}\right|=\frac12.
$$

El denominador impone

$$
x+1\neq0,
$$

por lo que el dominio efectivo es

$$
D=\mathbb R\setminus\{-1\}.
$$

Como $1/2>0$, la ecuación con valor absoluto se abre mediante una equivalencia exacta:

$$
\left|\frac{x-3}{x+1}\right|=\frac12
$$

$$
\Longleftrightarrow
\frac{x-3}{x+1}=\frac12
\quad\text{o}\quad
\frac{x-3}{x+1}=-\frac12,
\qquad x\in D.
$$

#### Primera rama

Como $x+1\neq0$ en $D$,

$$
\frac{x-3}{x+1}=\frac12
\Longleftrightarrow
2(x-3)=x+1.
$$

Entonces

$$
2x-6=x+1
\Longleftrightarrow
x=7.
$$

Y $7\in D$.

#### Segunda rama

De nuevo sobre $D$,

$$
\frac{x-3}{x+1}=-\frac12
\Longleftrightarrow
2(x-3)=-(x+1).
$$

Así,

$$
2x-6=-x-1
\Longleftrightarrow
3x=5
\Longleftrightarrow
x=\frac53.
$$

También $5/3\in D$.

Uniendo las ramas,

$$
\boxed{
\operatorname{Sol}_{D}
=
\left\{\frac53,7\right\}.
}
$$

No fue necesaria una tabla de signos: la caracterización $|A|=c\Longleftrightarrow(A=c\ \text{o}\ A=-c)$ para $c>0$ ya es exacta. Tampoco es necesario verificar los valores como si fueran candidatos obtenidos por una implicación no reversible; todas las transformaciones usadas fueron equivalencias sobre el dominio heredado. Una sustitución final puede hacerse como control independiente.


### Solución 79

Resolvemos sobre $\mathbb R^2$ el sistema

$$
\begin{cases}
x+y=6,\\
x^2+y^2=20.
\end{cases}
$$

#### Ruta A — sustitución directa

De la primera ecuación,

$$
y=6-x.
$$

Sustituimos en la segunda:

$$
x^2+(6-x)^2=20.
$$

Desarrollando,

$$
x^2+36-12x+x^2=20,
$$

de donde

$$
2x^2-12x+16=0.
$$

Dividimos por $2$:

$$
x^2-6x+8=0.
$$

Factorizamos:

$$
(x-2)(x-4)=0,
$$

de modo que

$$
x=2
\quad\text{o}\quad
x=4.
$$

Reconstruimos $y$:

$$
x=2\Longrightarrow y=4,
$$

$$
x=4\Longrightarrow y=2.
$$

La Ruta A produce

$$
\{(2,4),(4,2)\}.
$$

#### Ruta B — suma y producto

Usamos

$$
(x+y)^2=x^2+2xy+y^2.
$$

Como

$$
x+y=6,
$$

tenemos

$$
36=20+2xy,
$$

y por tanto

$$
xy=8.
$$

Ahora $x$ e $y$ son dos números cuya suma es $6$ y cuyo producto es $8$. Son, por tanto, las raíces de

$$
t^2-6t+8=0.
$$

Factorizamos:

$$
(t-2)(t-4)=0,
$$

de modo que los dos valores son $2$ y $4$. Como el sistema es simétrico bajo el intercambio $x\leftrightarrow y$, aparecen los dos órdenes:

$$
(2,4)
\quad\text{y}\quad
(4,2).
$$

Así, ambas rutas producen exactamente

$$
\boxed{
\operatorname{Sol}
=
\{(2,4),(4,2)\}
\subseteq\mathbb R^2.
}
$$

La simetría explica por qué una solución no diagonal viene acompañada de su par intercambiado: las dos ecuaciones permanecen invariantes al permutar las coordenadas.


### Solución 80

Consideramos

$$
\frac{x^2-4}{x-2}=\sqrt{x+7}.
$$

#### 1. Dominio original

La expresión racional exige

$$
x\neq2,
$$

y el radical exige

$$
x+7\ge0,
$$

es decir,

$$
x\ge-7.
$$

Por tanto,

$$
D=[-7,\infty)\setminus\{2\}.
$$

#### 2. Simplificación racional sobre el dominio

Factorizamos

$$
x^2-4=(x-2)(x+2).
$$

Como $x\neq2$ en todo $D$, podemos cancelar el factor $x-2$ sin cambiar el conjunto solución:

$$
\frac{x^2-4}{x-2}=\sqrt{x+7}
\Longleftrightarrow
x+2=\sqrt{x+7},
\qquad x\in D.
$$

La simplificación es una equivalencia **sobre $D$**; no reincorpora $x=2$.

#### 3. Ruta menos informativa: cuadrar sin registrar el signo

De

$$
x+2=\sqrt{x+7}
$$

podemos deducir

$$
(x+2)^2=x+7,
$$

pero, si no conservamos ninguna condición de signo, la flecha segura es sólo

$$
x+2=\sqrt{x+7}
\Longrightarrow
(x+2)^2=x+7.
$$

Desarrollamos:

$$
x^2+4x+4=x+7,
$$

de donde

$$
x^2+3x-3=0.
$$

La fórmula cuadrática produce

$$
x=\frac{-3\pm\sqrt{21}}2.
$$

Así, el conjunto de candidatos algebraicos es

$$
C=
\left\{
\frac{-3-\sqrt{21}}2,
\frac{-3+\sqrt{21}}2
\right\}.
$$

Los dos candidatos pertenecen al dominio $D$: ambos son mayores que $-7$ y ninguno vale $2$.

Sin embargo, para

$$
x_- = \frac{-3-\sqrt{21}}2,
$$

se tiene

$$
x_-+2=\frac{1-\sqrt{21}}2<0,
$$

mientras que una raíz principal es siempre no negativa. Por tanto, $x_-$ no puede satisfacer la ecuación radical. Es un **candidato extraño creado por la pérdida de información de signo** al cuadrar.

Para

$$
x_+ = \frac{-3+\sqrt{21}}2,
$$

tenemos

$$
x_++2=\frac{1+\sqrt{21}}2>0.
$$

Además, como $x_+$ satisface

$$
(x+2)^2=x+7,
$$

y el lado $x_++2$ es no negativo, se sigue que

$$
x_++2=\sqrt{x_++7}.
$$

Por tanto, $x_+$ sí es solución.

Las restricciones de dominio original deben mantenerse conceptualmente separadas de este filtrado. Desde el comienzo quedan excluidos

$$
x< -7
\qquad\text{y}\qquad
x=2.
$$

Ninguno de los dos candidatos cuadráticos cae en esas exclusiones. El candidato $x_-$ se descarta por una razón distinta: perdió la condición de signo durante el cuadrado.

#### 4. Verificación independiente

Para

$$
x_+=\frac{-3+\sqrt{21}}2,
$$

la parte racional se simplifica legítimamente a $x_++2$, porque $x_+\neq2$. Además,

$$
(x_++2)^2=x_++7
$$

y $x_++2>0$, de modo que

$$
\frac{x_+^2-4}{x_+-2}
=x_++2
=\sqrt{x_++7}.
$$

La comprobación confirma la pertenencia al conjunto solución.

#### 5. Ruta con equivalencia completa

La etapa radical puede escribirse sin perder información:

$$
x+2=\sqrt{x+7}
$$

$$
\Longleftrightarrow
\begin{cases}
(x+2)^2=x+7,\\
x+2\ge0,
\end{cases}
\qquad x\in D.
$$

Equivalentemente,

$$
\Longleftrightarrow
\begin{cases}
x^2+3x-3=0,\\
x\ge-2,
\end{cases}
\qquad x\in D.
$$

De las dos raíces de la cuadrática,

$$
\frac{-3-\sqrt{21}}2<-2,
$$

mientras que

$$
\frac{-3+\sqrt{21}}2>-2.
$$

Por tanto, la condición de signo selecciona directamente la única solución:

$$
\boxed{
\operatorname{Sol}_{D}
=
\left\{\frac{-3+\sqrt{21}}2\right\}.
}
$$

En la ruta menos informativa, la **primera transición sólo implicativa** fue elevar al cuadrado la ecuación radical sin registrar que el miembro $x+2$ debía ser no negativo. La segunda ruta conserva esa condición y mantiene equivalencia hasta el final.

## H. Soluciones de profundización y reconstrucción



#### Solución 081

La ecuación $(x-r)(x-s)/(x-h)=0$ tiene dominio $x\ne h$. En él, una fracción es cero exactamente cuando su numerador es cero: $x=r$ o $x=s$. Ambos están admitidos por la condición sobre $h$ y verifican la original. Todo otro valor permitido tiene numerador no nulo. Así se certifican simultáneamente existencia y exhaustividad; elegir $h=r$ habría eliminado una de las soluciones prescritas.



#### Solución 082

Tomemos $\sqrt{(x-r)^2} +\sqrt{(x-s)^2}=s-r$, definida en todos los reales. Es $|x-r|+|x-s|=s-r$. En $r\le x\le s$, la suma es $(x-r)+(s-x)=s-r$. Si $x<r$, vale $r+s-2x>s-r$; si $x>s$, vale $2x-r-s>s-r$. Estas tres regiones cubren la recta, de modo que no faltan soluciones ni se añaden otras. El resultado utiliza las raíces principales, no una elección libre de signos.



#### Solución 083

La ecuación $\dfrac{(x-r)(x-s)}{(x-r)(x-s)}=1$ está definida exactamente fuera de $r,s$. Allí el cociente vale uno, así que todos esos valores son soluciones. En $r,s$ no hay proposición definida que comprobar: no son soluciones y tampoco igualdades falsas de la expresión original. Multiplicar por el denominador da una identidad válida solo en el dominio fijado. Resolver esa identidad en toda la recta cambiaría el problema.



#### Solución 084

El dominio es $x\ne t$. Si $t=1$, el numerador es cero y el conjunto solución es $\mathbb R\setminus\{1\}$. Si $t\ne1$, el producto nulo da candidatos $0,2$. Para $t=0$ solo queda $\{2\}$; para $t=2$ solo $\{0\}$; para $t\notin\{0,1,2\}$ quedan $\{0,2\}$. Cada candidato conservado anula el numerador y deja denominador no nulo. Las cuatro ramas cubren todos los parámetros y evitan dividir por $t-1$ en su cero.



#### Solución 085

Factorizamos $(x-1)(tx+1)$, cuya expansión es la original. Si $t=0$, la ecuación es $x-1=0$ y la solución es $\{1\}$. Si $t\ne0$, las soluciones son $1,-1/t$; coinciden exactamente en $t=-1$. Así $S(-1)=\{1\}$ y $S(t)=\{1,-1/t\}$ para $t\notin\{0,-1\}$. El producto nulo demuestra que la lista es completa y sustituir cada factor cero verifica las soluciones. Una fórmula que divide por $t$ no puede cubrir el caso lineal.



#### Solución 086

El dominio exige $x\ne t$. Si $t=1$, queda $0=0$ en ese dominio, y $S(1)=\mathbb R\setminus\{1\}$. Si $t\ne1$, dividimos por $t-1$ y multiplicamos por $x-t\ne0$: $x=x-t$, equivalente a $t=0$. Para $t=0$, todos los $x\ne0$ verifican $x/x=1$, y $S(0)=\mathbb R\setminus\{0\}$. Para cualquier otro $t$, no hay soluciones. El factor paramétrico nulo y la cancelación de la incógnita generan ramas diferentes.



#### Solución 087

La original tiene $\{r\}$. El producto tiene $\{r,h\}$ por el producto nulo, con un único elemento si $h=r$. Toda solución original satisface el producto; el recíproco solo vale en toda la recta cuando $h=r$. Si $h\ne r$, comprobar $h$ en la original lo elimina, mientras comprobar $r$ lo conserva. Sobre el dominio restringido $x\ne h$, la multiplicación sí es reversible; si $h=r$, ambas ecuaciones restringidas carecen de soluciones. La equivalencia depende del dominio declarado.



#### Solución 088

La cuadrática es $(x-2)(x+1)=0$ y da $2,-1$, ambos en el dominio del radical. La original además exige $x\ge0$ porque el miembro izquierdo es no negativo. Con esa condición solo queda $2$, que verifica $\sqrt4=2$. El valor $-1$ da $1=-1$ y se rechaza. Cuadrar sin conservar el signo creó un candidato. La equivalencia correcta es $\sqrt{x+2}=x\Longleftrightarrow[x\ge0\ \text{y}\ x+2=x^2]$; esa formulación justifica la completitud.



#### Solución 089

Restar y factorizar da $(x-r)[(x-r)-(x-s)]=(s-r)(x-r)=0$. Si $s=r$, la original es una identidad y todos los reales son soluciones. Si $s\ne r$, solo $x=r$ la satisface. Dividir de entrada por $x-r$ dejaría $x-r=x-s$, que no tiene soluciones cuando $s\ne r$, perdiendo la única solución. Separar $x=r$ verifica siempre ese valor; en $x\ne r$, la ecuación equivale a $r=s$, y cubre el resto de la recta únicamente en el caso idéntico.



#### Solución 090

Sustituir $y=s-x$ da $x^2-sx+p=0$, equivalente a $(x-s/2)^2=s^2/4-p$. Si $s^2-4p<0$, no hay soluciones. Si es cero, el único par es $(s/2,s/2)$. Si es positivo, con $d=\sqrt{s^2-4p}/2$ hay los dos pares $(s/2+d,s/2-d)$ y su intercambio. Su suma es $s$ y su producto $s^2/4-d^2=p$. La sustitución era reversible, de modo que todos los pares están incluidos.



#### Solución 091

Sustituimos $y=x-a$. Entonces $x^2-ax-b=0$, o $(x-a/2)^2=a^2/4+b$. Si $a^2+4b<0$, el conjunto es vacío. Si es cero, tenemos $(x,y)=(a/2,-a/2)$. Si es positivo, sea $d=\sqrt{a^2+4b}/2$: los pares son $(a/2+d,-a/2+d)$ y $(a/2-d,-a/2-d)$. En ambos la diferencia es $a$ y el producto $d^2-a^2/4=b$. La reconstrucción conserva las coordenadas ordenadas y demuestra exhaustividad.



#### Solución 092

El producto nulo exige $x=0$ o $y=r$. La primera opción da $(0,s)$; la segunda da $(s-r,r)$. Ambos pares verifican suma y producto originales. Todo par solución pertenece a una de las dos opciones, por lo que la lista es completa. Coinciden exactamente cuando $s=r$, y entonces hay un solo par $(0,r)$. Dividir por $x$ dejaría solo la segunda rama y, cuando $s\ne r$, perdería $(0,s)$.

***

[← Capítulo 20](algebra-para-matematicos-capitulo-20-fracciones-algebraicas-y-expresiones-racionales.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 22 →](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md)

---
{
  "title": "Orden e inequaciones",
  "description": "Capítulo 22 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0197",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C22",
  "editorial-id": "MA-BCH-APM-01-019",
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
    "MA-BCH-0196"
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

En C21 el objeto de una resolución era el conjunto de valores que hacían verdadera una igualdad. Una inequación conserva esa misma exigencia de precisión, pero la relación que debemos estudiar ya no es sólo $=$.

Compare $x=3$ con $x<3$. La primera afirmación selecciona, sobre $\mathbb R$, un único valor. La segunda selecciona todos los números reales situados a la izquierda de $3$ en la recta real. Para $x=2$ la relación $x<3$ es verdadera; para $x=4$ es falsa; para $x=3$ tampoco es verdadera, porque la desigualdad es estricta.

Antes de aprender técnicas para transformar inequaciones necesitamos fijar qué expresa el orden de los números reales y qué significa resolver una condición de este tipo.



## 22.1. Orden en los reales y conjunto solución {#apm-c22-s01}

### Comparar dos números reales

Los números reales están ordenados. Para $a,b\in\mathbb R$, la escritura $a<b$ afirma que $a$ es menor que $b$. Geométricamente, $a$ se encuentra a la izquierda de $b$ en la recta real. La misma comparación puede escribirse en el sentido opuesto como $b>a$.

Las relaciones no estrictas incorporan también la igualdad:

$$
a\le b
\Longleftrightarrow
(a<b\ \text{o}\ a=b),
$$

y, de manera análoga,

$$
a\ge b
\Longleftrightarrow
(a>b\ \text{o}\ a=b).
$$

La palabra «o» tiene aquí su significado lógico inclusivo: si $a=b$, la relación $a\le b$ es verdadera aunque $a<b$ sea falsa.

Por ejemplo, $-2<1,\qquad 4\le4,\qquad 7>3$. En cambio, $5<2$ y $6\le1$ son proposiciones falsas.

### Tricotomía

El orden de $\mathbb R$ permite comparar cualquier par de números reales. Dados $a,b\in\mathbb R$, exactamente una de las tres relaciones $a<b,\qquad a=b,\qquad a>b$ es verdadera.

Esta propiedad se llama **tricotomía**. Las tres posibilidades se excluyen entre sí y cubren todos los casos. Si sabemos, por ejemplo, que $a<b$, quedan descartadas simultáneamente $a=b$ y $a>b$.

La tricotomía evita una ambigüedad que sería incompatible con el orden usual de la recta: dos números reales no pueden quedar «sin comparar», ni pueden satisfacer a la vez dos de las tres relaciones estrictas anteriores.

### De una desigualdad numérica a una inequación

Una desigualdad como $2<5$ es una proposición: una vez fijados los dos números, tiene un valor de verdad determinado.

La expresión $2x+1<7$ se comporta de otro modo. Su verdad depende del valor asignado a $x$. Si $x=2$, $2(2)+1<7$ es verdadera. Si $x=4$, $2(4)+1<7$ es falsa.

En este libro llamaremos **inequación en la variable $x$ sobre un dominio $D$** a una condición de la forma

$$
E(x)<F(x),\qquad
E(x)\le F(x),\qquad
E(x)>F(x)
\quad\text{o}\quad
E(x)\ge F(x),
$$

interpretada para los valores $x\in D$ en los que las expresiones involucradas están definidas.

El signo de orden forma parte de la proposición. Cambiar $<$ por $>$ no es una modificación tipográfica: produce una condición distinta y, en general, un conjunto solución distinto.

### Qué significa ser solución

Sea, por ejemplo, $E(x)<F(x)$ una inequación definida sobre un dominio $D$. Un valor $a\in D$ es una **solución** si la sustitución $x=a$ convierte la inequación en una proposición verdadera.

Así, $x=2$ es solución de $x<3, \qquad x\in\mathbb R$, porque $2<3$. En cambio, $x=3$ no es solución de esa inequación: la proposición $3<3$ es falsa.

Para una relación no estricta la situación cambia. El mismo valor $x=3$ sí es solución de $x\le3$, pues la igualdad está incluida en el significado de $\le$.

La diferencia entre $<$ y $\le$ afectará más adelante la inclusión o exclusión de puntos frontera. Por ahora basta con mantener separados sus significados.

### El conjunto solución

Resolver una inequación exige determinar todos sus valores válidos, no verificar algunos ejemplos.

Para una inequación $E(x)<F(x)$ sobre un dominio $D$, definimos

$$
\operatorname{Sol}_D(E<F)
=
\{x\in D:E(x)<F(x)\}.
$$

Las otras relaciones de orden se tratan de la misma forma. Por ejemplo,

$$
\operatorname{Sol}_D(E\le F)
=
\{x\in D:E(x)\le F(x)\}.
$$

El conjunto solución es siempre un subconjunto del dominio: $\operatorname{Sol}_D(E<F)\subseteq D$. Esta inclusión registra algo que acompañará todo el capítulo: ninguna transformación posterior puede convertir en solución un valor que no pertenecía al dominio del problema.

### La misma fórmula sobre dominios distintos

Considere la inequación $x<3$. Sobre $\mathbb R$, su conjunto solución puede dejarse por ahora en notación constructiva:

$$
\operatorname{Sol}_{\mathbb R}(x<3)
=
\{x\in\mathbb R:x<3\}.
$$

Geométricamente, este conjunto contiene todos los puntos de la recta real situados a la izquierda de $3$ y no contiene el punto $3$.

Suponga, en cambio, que el dominio declarado es $D=\{-1,0,1,2,3,4\}$. Entonces sólo debemos examinar esos seis valores. Los cuatro primeros satisfacen $x<3$, mientras que $3$ y $4$ no lo hacen. Por tanto, $\operatorname{Sol}_D(x<3) = \{-1,0,1,2\}$. La inequación escrita no cambió. Cambió el conjunto dentro del cual se pregunta por su verdad, y con él cambió el conjunto solución.

### El dominio efectivo sigue siendo obligatorio

La disciplina de dominio de C20 y C21 no desaparece al pasar de ecuaciones a inequaciones.

Considere $\frac{x-1}{x-1}>0, \qquad x\in\mathbb R$. La fracción sólo está definida cuando $x\neq1$. El dominio efectivo es $D=\mathbb R\setminus\{1\}$. Para cada $x\in D$ podemos cancelar el factor no nulo $x-1$ y la condición se reduce a $1>0$, que es verdadera. En consecuencia,

$$
\operatorname{Sol}_{\mathbb R\setminus\{1\}}
\left(
\frac{x-1}{x-1}>0
\right)
=
\mathbb R\setminus\{1\}.
$$

El valor $x=1$ no es una solución que deba descartarse después de probarla. No pertenece al dominio de la expresión original. La simplificación hace desaparecer de la fórmula el denominador, pero no elimina la restricción que éste impuso.

Este ejemplo anticipa una distinción que será central en las inequaciones racionales: un punto puede quedar fuera del conjunto solución porque la relación es falsa o porque la expresión ni siquiera está definida allí. Son razones matemáticamente distintas.

### Probar valores no equivale a resolver

Considere $x^2<5, \qquad x\in\mathbb R$. Sustituir $x=0$ muestra que $0$ es solución: $0^2<5$. Sustituir $x=3$ muestra que $3$ no lo es: $3^2<5$ es falsa.

Ninguna de las dos comprobaciones describe el conjunto solución completo. Una prueba puntual responde a la pregunta «¿pertenece este valor al conjunto solución?». Resolver exige caracterizar todos los valores para los que la relación es verdadera.

En dominios finitos puede bastar una comprobación exhaustiva. Sobre $\mathbb R$, donde hay infinitos candidatos, necesitaremos propiedades del orden y transformaciones que preserven la relación de manera controlada.

### Un no-ejemplo de razonamiento

Alguien considera $\frac{x+2}{x-1}>0$ y afirma: «$x=1$ no sirve porque al sustituirlo la desigualdad resulta falsa».

La conclusión de que $1$ no pertenece al conjunto solución es correcta, pero la razón no lo es. Al sustituir $x=1$ obtenemos un denominador nulo; no aparece una proposición falsa, sino una expresión indefinida. El valor $1$ queda excluido antes de estudiar el signo.

Separar **dominio** de **verdad de la inequación** será necesario cuando aparezcan ceros, puntos excluidos y extremos.

### Prueba de estrés: igualdad frente a orden estricto

Considere un número real $a$. Por tricotomía, exactamente una de las siguientes afirmaciones es verdadera: $a<3,\qquad a=3,\qquad a>3$. De aquí no se sigue que exactamente una de $a\le3$ y $a\ge3$ sea verdadera. Si $a=3$, ambas lo son: $3\le3 \qquad\text{y}\qquad 3\ge3$. La tricotomía corresponde a las relaciones **estrictas** junto con la igualdad. Las relaciones $\le$ y $\ge$ se superponen precisamente en el caso de igualdad.

### Recuperación breve

Sea $D=\{-2,-1,0,1,2,3\}$ y considere la inequación $x^2<5$. Determine su conjunto solución sin aplicar transformaciones algebraicas: compruebe directamente los valores del dominio.

**Respuesta razonada.** Evaluamos la condición en los seis elementos de $D$:

$$
(-2)^2=4<5,\qquad
(-1)^2=1<5,\qquad
0^2=0<5,
$$



$$
1^2=1<5,\qquad
2^2=4<5,\qquad
3^2=9>5.
$$

Los cinco primeros valores satisfacen la inequación y $3$ no la satisface. Por tanto, $\operatorname{Sol}_D(x^2<5) = \{-2,-1,0,1,2\}$. La resolución fue posible por inspección exhaustiva porque $D$ era finito. El mismo procedimiento no constituye un método adecuado para describir el conjunto solución sobre todo $\mathbb R$.

### Qué debemos conservar de esta sección

Una inequación se interpreta sobre un dominio y pregunta dónde una relación de orden es verdadera. Su solución completa es un conjunto:

$$
\operatorname{Sol}_D(E\triangleleft F)
=
\{x\in D:E(x)\triangleleft F(x)\},
$$

donde $\triangleleft$ representa una de las relaciones $<$, $\le$, $>$ o $\ge$.

La tricotomía organiza la comparación estricta de dos reales; el dominio decide qué valores son admisibles; la inequación decide cuáles de esos valores satisfacen la relación. Resolver significa describir todo ese subconjunto, no acumular verificaciones aisladas.



## 22.2. Intervalos, semirrectas y extremos {#apm-c22-s02}

En [§22.1](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s01) dejamos el conjunto solución de $x<3$ escrito como $\{x\in\mathbb R:x<3\}$.

La descripción es exacta, pero no aprovecha una propiedad especial del orden real: todos esos valores forman una región continua de la recta. Para trabajar con inequaciones necesitaremos una notación que permita ver de inmediato dónde comienza y termina una región, qué puntos frontera pertenecen a ella y qué ocurre cuando el conjunto se extiende indefinidamente.

### Intervalos entre dos números

Sean $a,b\in\mathbb R$ con $a<b$. El **intervalo abierto** entre $a$ y $b$ es

$$
(a,b)=\{x\in\mathbb R:a<x<b\}.
$$

Los extremos $a$ y $b$ no pertenecen al conjunto. En la recta real, el intervalo contiene todos los puntos situados estrictamente entre ambos.

El **intervalo cerrado** correspondiente es $[a,b]=\{x\in\mathbb R:a\le x\le b\}$. Aquí los dos extremos sí pertenecen al conjunto. Las otras dos posibilidades incluyen sólo uno de ellos:

$$
[a,b)=\{x\in\mathbb R:a\le x<b\},
\qquad
(a,b]=\{x\in\mathbb R:a<x\le b\}.
$$

Los corchetes y paréntesis no son adornos tipográficos. Registran pertenencia. Un corchete junto a un extremo real indica que ese punto está incluido; un paréntesis indica que está excluido.

Por ejemplo, $[-2,4)=\{x\in\mathbb R:-2\le x<4\}$. El número $-2$ pertenece al conjunto y $4$ no pertenece.

### Una misma región, varias representaciones

El conjunto $S=\{x\in\mathbb R:-1<x\le3\}$ puede escribirse como $S=(-1,3]$.

Ambas expresiones describen el mismo objeto. La notación constructiva hace visibles las condiciones lógicas; la notación de intervalo hace visible la geometría del conjunto sobre la recta.

La traducción entre ambas formas debe preservar exactamente la inclusión de los extremos:

| Condición | Notación de intervalo |
|---|---|
| $a<x<b$ | $(a,b)$ |
| $a\le x\le b$ | $[a,b]$ |
| $a\le x<b$ | $[a,b)$ |
| $a<x\le b$ | $(a,b]$ |

Una desigualdad estricta excluye el punto frontera que produce; una desigualdad no estricta puede incluirlo, siempre que ese punto pertenezca al dominio efectivo.

### Semirrectas

Muchas inequaciones no acotan al conjunto solución por ambos lados. Si la condición es $x<3$, el conjunto se extiende indefinidamente hacia la izquierda. Las cuatro formas básicas son:

| Condición | Semirrecta |
|---|---|
| $x<3$ | $(-\infty,3)$ |
| $x\le3$ | $(-\infty,3]$ |
| $x>2$ | $(2,\infty)$ |
| $x\ge2$ | $[2,\infty)$ |

Estos conjuntos se llaman **semirrectas**. El símbolo $\infty$ no representa un número real ni un punto que pueda pertenecer al conjunto. Por eso siempre escribimos paréntesis junto a $\infty$ y $-\infty$.

La escritura $[-\infty,3]$ no es una notación válida de intervalo real: $-\infty$ no es un extremo perteneciente a $\mathbb R$ que pueda incluirse con un corchete.

### Todo $\mathbb R$ y el conjunto vacío

La recta real completa puede escribirse como $(-\infty,\infty)=\mathbb R$.

En el extremo opuesto, algunas condiciones no dejan ningún valor admisible. Su conjunto solución es el conjunto vacío, $\varnothing$.

También hay casos degenerados útiles para controlar la notación. Para cualquier $a\in\mathbb R$, se tiene $[a,a]=\{a\}$, mientras que $(a,a)=\varnothing$.

El primer conjunto contiene el único punto que satisface $a\le x\le a$; el segundo exigiría simultáneamente $a<x$ y $x<a$, lo que es imposible.

### Unión: varias regiones separadas

No todos los conjuntos solución forman un único intervalo. Considere $S=\{x\in\mathbb R:x<-1\ \text{o}\ 2\le x\le5\}$. La palabra «o» indica que basta satisfacer una de las dos condiciones. En lenguaje de conjuntos, $S=(-\infty,-1)\cup[2,5]$.

La unión conserva ambas regiones. El espacio entre $-1$ y $2$ no pertenece al conjunto.

Este tipo de respuesta aparecerá con frecuencia cuando un producto o un cociente cambie de signo en varios puntos críticos. La notación de unión permite conservar una solución desconectada sin forzarla artificialmente a convertirse en un solo intervalo.

### Intersección: condiciones simultáneas

Si un valor debe satisfacer dos condiciones a la vez, buscamos la intersección de los conjuntos correspondientes.

Por ejemplo, $x>-2$ y $x\le4$ exigen simultáneamente $x\in(-2,\infty)$ y $x\in(-\infty,4]$. Por tanto, $(-2,\infty)\cap(-\infty,4]=(-2,4]$. La primera condición elimina todo lo que está en $(-\infty,-2]$; la segunda elimina todo lo que está en $(4,\infty)$. Sobrevive la región común.

Unión e intersección ya aparecieron en C7. Aquí adquieren una función operativa: permiten describir con precisión conjuntos solución que tienen varias ramas o que deben satisfacer varias restricciones al mismo tiempo.

### Extremo abierto no significa siempre «desigualdad estricta»

Considere un dominio efectivo que ya excluye un punto, $D=\mathbb R\setminus\{2\}$. Dentro de ese dominio queremos describir los valores que satisfacen $x\le3$.

Si sólo miráramos el signo $\le$, podríamos pensar en $(-\infty,3]$. Pero el punto $2$ no pertenece a $D$. El conjunto solución correcto es $(-\infty,2)\cup(2,3]$. Aquí aparecen dos tipos de frontera diferentes:

- $3$ pertenece al conjunto porque la relación es no estricta y $3\in D$;
- $2$ queda fuera porque no pertenece al dominio, aunque $2\le3$ sea una proposición verdadera.

La forma gráfica de ambos hechos puede parecer similar —en los dos casos un punto podría quedar «abierto»—, pero la razón matemática no es la misma. Esta diferencia será indispensable cuando trabajemos con inequaciones racionales.

### Un punto frontera debe pasar dos pruebas

Cuando una resolución produce un candidato a extremo real $c$, su inclusión requiere comprobar dos cosas:

1. $c$ debe pertenecer al dominio efectivo;
2. la relación de la inequación debe admitir la igualdad en ese punto.

Si falla la primera condición, el punto queda excluido por dominio. Si el punto pertenece al dominio pero la inequación es estricta, queda excluido por la relación de orden.

Considere $S=\left\{x\in\mathbb R\setminus\{1\}:x\ge-2\right\}$.

El extremo $-2$ pertenece al dominio y la relación es no estricta, por lo que se incluye. El punto $1$ satisface numéricamente $1\ge-2$, pero está excluido del dominio. Así, $S=[-2,1)\cup(1,\infty)$.

### Prueba de estrés: leer los símbolos antes de calcular

Compare $A=(-1,2]$, $B=[-1,2)$ y $C=(-1,2)$. Comparten todos los puntos interiores entre $-1$ y $2$, pero difieren en sus extremos: $-1\notin A$ y $2\in A$; $-1\in B$ y $2\notin B$; en $C$ quedan excluidos ambos extremos.

Por tanto, los tres conjuntos son distintos. Una sola marca de inclusión o exclusión puede cambiar el conjunto solución.

La notación de intervalo debe leerse como una afirmación de pertenencia, no como una convención visual aproximada.

### Recuperación breve

Escriba en notación de intervalos los siguientes conjuntos.

**a)** $A=\{x\in\mathbb R:-2<x\le4\}$.

**b)** $B=\{x\in\mathbb R:x\le1\ \text{o}\ x>3\}$.

**c)** $C=\{x\in\mathbb R\setminus\{0\}:x\ge-1\}$.

**Respuesta razonada.** En **a)** el extremo $-2$ está excluido y $4$ incluido, de modo que $A=(-2,4]$.

En **b)** la condición describe dos semirrectas separadas. El punto $1$ se incluye y $3$ se excluye, de modo que $B=(-\infty,1]\cup(3,\infty)$.

En **c)** la condición $x\ge-1$ incluiría inicialmente $[-1,\infty)$, pero el dominio elimina $0$. Por tanto, $C=[-1,0)\cup(0,\infty)$.

El punto $0$ no se excluye por una desigualdad estricta; se excluye porque no pertenece al dominio.

### Qué debemos conservar de esta sección

La notación de intervalos es una forma compacta de describir subconjuntos ordenados de $\mathbb R$. Los corchetes y paréntesis registran pertenencia de extremos reales; $\pm\infty$ nunca se incluyen; la unión permite reunir regiones separadas y la intersección expresa condiciones simultáneas.

Un extremo real se incluye sólo si pertenece al dominio y la relación admite la igualdad. Esta doble verificación impide confundir un punto excluido por dominio con un punto excluido por una desigualdad estricta.



## 22.3. Sumar, restar y comparar {#apm-c22-s03}

En [§22.2](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s02) aprendimos a leer un conjunto solución sobre la recta real. Para empezar a transformar inequaciones necesitamos saber qué operaciones conservan el orden. La primera es la más estable de todas: **trasladar ambos miembros por la misma cantidad**.

Si $4<9$, entonces también $4+7<9+7$ y $4-20<9-20$. El orden no cambia aunque el número añadido sea positivo, negativo o cero. Ambos puntos se desplazan la misma distancia y en la misma dirección sobre la recta.

### Compatibilidad del orden con la suma

Sean $a,b,c\in\mathbb R$. Si $a<b$, entonces $b-a>0$. Después de sumar $c$ a ambos números, la diferencia entre el segundo y el primero sigue siendo la misma: $(b+c)-(a+c)=b-a>0$. Por tanto, $a+c<b+c$. El paso es reversible: restar $c$ recupera la comparación original. Tenemos así

$$
a<b\Longleftrightarrow a+c<b+c,
\qquad
a\le b\Longleftrightarrow a+c\le b+c.
$$

Las versiones con $>$ y $\ge$ son la misma propiedad leída en el sentido opuesto.

Sumar la misma cantidad a ambos miembros produce una equivalencia: conserva exactamente la relación de orden. En una inequación, esto significa que el conjunto solución no cambia, siempre que la expresión añadida esté definida en todo el dominio vigente.

### Restar es sumar el opuesto

No necesitamos una regla nueva para la resta. Restar $c$ equivale a sumar $-c$, de modo que

$$
a<b\Longleftrightarrow a-c<b-c,
\qquad
a\le b\Longleftrightarrow a-c\le b-c.
$$

El signo de $c$ no interviene en la dirección de la desigualdad. Por ejemplo, de $2<5$ se obtiene $-8<-5$ al sumar $-10$ a ambos miembros. El orden sigue apuntando en la misma dirección.

El signo de la cantidad sumada no altera la orientación. **Sumar o restar la misma cantidad conserva la relación cualquiera sea ese signo.** Multiplicar y dividir plantean un problema diferente, porque allí sí interviene el signo del factor.

### La regla sobre expresiones

La misma propiedad funciona cuando los miembros dependen de una variable. Suponga que $A(x)$, $B(x)$ y $G(x)$ están definidos para todo $x$ de un dominio $D$. Para cada $x\in D$,

$$
A(x)<B(x)
\Longleftrightarrow
A(x)+G(x)<B(x)+G(x).
$$

En términos de conjuntos solución,

$$
\operatorname{Sol}_D(A<B)
=
\operatorname{Sol}_D(A+G<B+G).
$$

La igualdad de conjuntos expresa lo que realmente nos interesa: la transformación es reversible sobre $D$.

Por ejemplo, sobre $\mathbb R$, $x-5<2\Longleftrightarrow x<7$. Se sumó $5$ a ambos miembros. El conjunto solución es el mismo antes y después de la transformación: $(-\infty,7)$.

También podemos eliminar una expresión común más complicada. Considere $x^2+x<x^2+7$. Restar $x^2$, que está definido para todo real, produce $x<7$. No estamos «cancelando» símbolos por semejanza visual: aplicamos a ambos miembros la misma transformación reversible sobre el dominio completo.

### El dominio sigue formando parte de la equivalencia

La condición «$G(x)$ está definida en todo $D$» no puede omitirse.

Considere la inequación $x<2$ sobre $D=\mathbb R$. Si añadimos $1/(x-1)$ a ambos miembros, obtenemos $x+1/(x-1)<2+1/(x-1)$. La nueva escritura no está definida en $x=1$. Sobre $\mathbb R\setminus\{1\}$, la transformación es reversible; sobre el dominio original $\mathbb R$, no podemos afirmar que ambas inequaciones representen el mismo problema, porque hemos eliminado un valor que sí pertenecía al dominio inicial y que además satisfacía $x<2$.

El error no está en sumar «lo mismo» a ambos lados. Está en introducir una expresión cuyo dominio es más pequeño y olvidar que la equivalencia debe conservar también el conjunto de valores admisibles.

### Transitividad: comparar a través de un término intermedio

El orden de los reales es transitivo. Si $a<b$ y $b<c$, entonces $a<c$. La misma idea vale para la relación no estricta: de $a\le b$ y $b\le c$ se sigue $a\le c$.

También aparecen formas mixtas. Si $a<b$ y $b\le c$, entonces $a<c$; si $a\le b$ y $b<c$, también $a<c$. En ambos casos hay al menos una separación estricta entre los extremos.

Esta propiedad permite encadenar comparaciones. La escritura $a<b<c$ abrevia simultáneamente $a<b$ y $b<c$; no introduce una relación nueva. Por transitividad, la cadena contiene además la información $a<c$.

Por ejemplo, de $-4<1$ y $1<6$ se obtiene $-4<6$. Si añadimos $3$ a las dos comparaciones, aparecen $-1<4$ y $4<9$, y por transitividad concluimos $-1<9$.

### Una consecuencia: sumar comparaciones compatibles

Suponga que $a<b$ y $c<d$. La primera desigualdad permite sumar $c$ en ambos miembros: $a+c<b+c$. La segunda permite sumar $b$ en ambos miembros: $b+c<b+d$. Por transitividad, $a+c<b+d$. Esta conclusión no es una regla aislada; combina dos propiedades ya justificadas: compatibilidad aditiva y transitividad.

La misma lógica funciona con relaciones no estrictas. Si $a\le b$ y $c\le d$, entonces $a+c\le b+d$.

### Prueba de estrés: «sumar» no significa modificar un solo miembro

Partimos de una afirmación verdadera, $2<3$. Si sumamos $5$ sólo al miembro izquierdo obtenemos $7<3$, que es falsa. La propiedad de compatibilidad aditiva exige aplicar **la misma** suma a ambos miembros.

Tampoco exige que la cantidad añadida sea positiva. De $2<3$ podemos pasar a $2-100<3-100$, es decir, $-98<-97$. La dirección se conserva.

Lo que debe controlarse es que ambos miembros reciban la misma traslación y que esa traslación esté definida. El signo de la cantidad añadida no cambia la orientación.

### Recuperación breve

Trabaje sobre los dominios indicados.

**a)** Transforme $x+7\le12$ usando sólo una suma o resta aplicada a ambos miembros y escriba el conjunto solución.

**b)** Determine el conjunto solución de $x^2+1<x^2+5$ sobre $\mathbb R$ sin probar valores uno por uno.

**c)** Explique por qué añadir $1/(x-2)$ a ambos miembros de $x<4$ no produce, sobre todo $\mathbb R$, una inequación equivalente al problema original.

**Respuesta razonada.** En **a)** restamos $7$ en ambos miembros: $x+7\le12\Longleftrightarrow x\le5$. Por tanto, el conjunto solución es $(-\infty,5]$.

En **b)** restamos $x^2$ en ambos miembros. Como $x^2$ está definido para todo $x\in\mathbb R$, obtenemos $1<5$, una proposición verdadera para cualquier real. El conjunto solución es $\mathbb R$.

En **c)** la expresión $1/(x-2)$ no está definida en $x=2$. La inequación original sí estaba definida allí y $2<4$ es verdadera. La transformación sería reversible sobre $\mathbb R\setminus\{2\}$, pero no conserva el problema sobre el dominio original $\mathbb R$.

### Qué debemos conservar de esta sección

La suma es compatible con el orden: aplicar la misma traslación a ambos miembros conserva la dirección y, cuando todas las expresiones están definidas en el dominio vigente, conserva exactamente el conjunto solución. Restar es el mismo principio aplicado al opuesto.

La transitividad permite encadenar comparaciones y combinar pasos ya justificados. En cada transformación deben mantenerse visibles dos datos: **qué operación se aplicó a ambos miembros y sobre qué dominio esa operación está definida**.



## 22.4. Multiplicar y dividir: el signo gobierna la dirección {#apm-c22-s04}

En [§22.3](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s03) sumar la misma cantidad a ambos miembros conservaba el orden sin importar el signo de esa cantidad. La multiplicación no tiene esa estabilidad. El signo del factor decide qué ocurre con la dirección de la desigualdad.

Compare $2<5$. Al multiplicar ambos miembros por $3$ obtenemos $6<15$: el orden se conserva. Si multiplicamos por $-3$, aparecen $-6$ y $-15$, pero en la recta real $-6$ está a la derecha de $-15$. La comparación correcta es $-6>-15$.

La diferencia entre ambos casos no es una convención de escritura. Proviene de las propiedades del orden real.

### Multiplicar por un número positivo conserva la dirección

Sean $a,b,c\in\mathbb R$ con $a<b$ y $c>0$. Como $b-a>0$, el producto de dos números positivos también es positivo: $c(b-a)>0$. Al distribuir, $cb-ca>0$, y por la definición del orden se obtiene $ca<cb$.

El argumento es reversible porque $c\neq0$ y $1/c>0$. Por tanto,

$$
a<b\Longleftrightarrow ca<cb,
\qquad
 a\le b\Longleftrightarrow ca\le cb
\quad(c>0).
$$

Las relaciones $>$ y $\ge$ obedecen la misma regla. Multiplicar o dividir por una constante positiva preserva la orientación.

Por ejemplo, $4x<20\Longleftrightarrow x<5$: dividimos por $4>0$ y la dirección no cambia.

### Multiplicar por un número negativo invierte la dirección

Suponga ahora $a<b$ y $c<0$. Entonces $-c>0$. Como $b-a>0$, tenemos $(b-a)(-c)>0$. Al desarrollar, $ac-bc>0$, por lo que $ac>bc$. El número que antes estaba a la izquierda termina a la derecha después de multiplicar por un factor negativo.

Así,

$$
a<b\Longleftrightarrow ca>cb,
\qquad
 a\le b\Longleftrightarrow ca\ge cb
\quad(c<0).
$$

La inversión de la desigualdad no es una regla mnemotécnica añadida al álgebra. Es la forma simbólica de una inversión real del orden.

Por ejemplo, de $-3x\le12$ obtenemos $x\ge-4$ al dividir por $-3$. Mantener $\le$ produciría un conjunto distinto y sería incorrecto.

### Dividir es multiplicar por el recíproco

Dividir por $c\neq0$ equivale a multiplicar por $1/c$. El recíproco tiene el mismo signo que $c$: si $c>0$, entonces $1/c>0$; si $c<0$, entonces $1/c<0$.

Por eso la regla de división no necesita una teoría separada:

- dividir por un número positivo conserva la dirección;
- dividir por un número negativo la invierte.

La condición $c\neq0$ es indispensable. La división por cero no está definida.

### El caso cero no es una tercera versión reversible

Multiplicar por cero destruye la información de orden. A partir de $2<5$, por ejemplo, multiplicar ambos miembros por $0$ produce $0<0$, que es falso. Para una relación no estricta, $2\le5$ daría $0\le0$, que es verdadero, pero ya no permite recuperar la comparación original.

En ambos casos se perdió la diferencia entre los dos miembros. El paso no es reversible.

Esto distingue tres situaciones que deben mantenerse separadas:

| Factor $c$ | Efecto sobre $a<b$ | ¿Se puede dividir después? |
|---|---|---|
| $c>0$ | $ca<cb$ | Sí |
| $c<0$ | $ca>cb$ | Sí |
| $c=0$ | ambos miembros colapsan a $0$ | No |

### Una lectura geométrica

Multiplicar todos los puntos de la recta por un número positivo realiza un cambio de escala que conserva izquierda y derecha. Multiplicar por un número negativo combina una escala con una reflexión respecto de $0$; esa reflexión intercambia izquierda y derecha.

Esta imagen explica por qué el valor absoluto del factor controla el tamaño del cambio y su signo controla la orientación.

### Cuando el multiplicador depende de $x$

El problema se vuelve más delicado si el factor es una expresión $M(x)$. No podemos decidir de antemano si la dirección se conserva o se invierte sin conocer su signo.

Sobre un dominio $D$, conviene separar

$$
D_+=\{x\in D:M(x)>0\},\qquad
D_-=\{x\in D:M(x)<0\},\qquad
D_0=\{x\in D:M(x)=0\}.
$$

Si $A(x)<B(x)$, entonces sobre $D_+$ podemos multiplicar por $M(x)$ conservando la dirección; sobre $D_-$ debemos invertirla. En $D_0$ no podemos dividir por $M(x)$ y la multiplicación por cero no conserva de manera reversible la desigualdad original.

En símbolos,

$$
\begin{aligned}
x\in D_+&:\quad A(x)<B(x)\Longleftrightarrow M(x)A(x)<M(x)B(x),\\
x\in D_-&:\quad A(x)<B(x)\Longleftrightarrow M(x)A(x)>M(x)B(x).
\end{aligned}
$$

No existe una sola transformación equivalente que ignore esta partición cuando $M$ cambia de signo.

### Un no-ejemplo: multiplicar por la variable sin mirar su signo

Considere $x<2$. Alguien multiplica ambos miembros por $x$ y escribe $x^2<2x$.

El paso no es equivalente sobre $\mathbb R$. Si $x=1$, ambas desigualdades son verdaderas. Si $x=-1$, la original $-1<2$ es verdadera, pero la transformada $1<-2$ es falsa. Si $x=0$, la original es verdadera y la transformada se convierte en $0<0$, también falsa.

El mismo factor $x$ es positivo en una parte del dominio, negativo en otra y cero en un tercer caso. La operación correcta exige separar esos regímenes antes de decidir la dirección.

### Dividir por una expresión variable exige dos controles

Para dividir una inequación por $M(x)$ necesitamos saber, en el dominio considerado, dos cosas:

1. que $M(x)\neq0$;
2. si $M(x)$ es positivo o negativo.

La primera condición autoriza la división. La segunda determina la orientación de la desigualdad. Saber sólo que $M(x)\neq0$ no basta si su signo puede variar.

Por esta razón, «pasar un factor dividiendo» no es una operación puramente sintáctica en una inequación. La validez depende de información matemática que debe estar disponible antes del paso.

### Prueba de estrés: el mismo cálculo con signos distintos

Parta de $a<b$. Si multiplicamos por $5$, obtenemos $5a<5b$. Si multiplicamos por $-5$, obtenemos $-5a>-5b$. Si intentamos multiplicar por una cantidad cuyo signo no conocemos, no podemos elegir responsablemente entre esas dos orientaciones.

El cálculo algebraico puede ser idéntico en apariencia; la hipótesis de signo cambia la conclusión lógica.

### Recuperación breve

**a)** Resuelva $-4x>12$ usando una sola división justificada y escriba el conjunto solución.

**b)** Si $3a\le3b$, explique por qué puede concluirse $a\le b$.

**c)** Un estudiante parte de $x<4$ y multiplica ambos miembros por $x-1$, escribiendo $x(x-1)<4(x-1)$. Explique por qué la transformación no es equivalente sobre todo $\mathbb R$.

**Respuesta razonada.** En **a)** dividimos por $-4<0$, de modo que la desigualdad se invierte: $x<-3$. El conjunto solución es $(-\infty,-3)$.

En **b)** dividimos por $3>0$. La división está definida y conserva la orientación, por lo que $a\le b$.

En **c)** el factor $x-1$ es negativo para $x<1$, cero en $x=1$ y positivo para $x>1$. No existe una única dirección válida sobre todo $\mathbb R$; además, en $x=1$ la multiplicación por cero pierde información. La transformación sólo puede justificarse después de separar los casos de signo correspondientes.

### Qué debemos conservar de esta sección

Multiplicar o dividir una desigualdad exige conocer el signo del factor. Un factor positivo conserva la orientación; uno negativo la invierte; el cero destruye la reversibilidad y nunca puede usarse como divisor.

Cuando el factor depende de la variable, el dominio debe separarse según $M(x)>0$, $M(x)<0$ y $M(x)=0$. **El signo no acompaña al cálculo como una anotación secundaria: decide qué transformación es válida.**



### El signo de una expresión requiere regiones

El signo de una constante no nula se fija una vez; el de $x-a$ cambia con $x$. Por eso multiplicar una inequación por $x-a$ exige separar $x<a$, $x>a$ y, si pertenece al dominio, $x=a$. **Control resuelto:** $1/(x-a)>0$ tiene dominio $x\ne a$ y equivale a $x>a$. Multiplicar sin revisar el signo y concluir $1>0$ para todo el dominio sería falso. Una alternativa segura es multiplicar por $(x-a)^2>0$ en el dominio: se obtiene $x-a>0$. Se justifica así la misma solución con un multiplicador de signo fijo. Elegir una ruta breve requiere demostrar por qué conserva el orden en toda la región donde se usa.



## 22.5. Inequaciones lineales {#apm-c22-s05}

Las secciones anteriores separaron las operaciones que siempre conservan el orden de aquellas cuya validez depende del signo. Ya podemos resolver de manera sistemática una inequación lineal sin recurrir a reglas memorizadas.

Considere $3x-5\le7$. Sumar $5$ en ambos miembros conserva la relación y produce $3x\le12$. Como $3>0$, dividir por $3$ también conserva la dirección. Así, $x\le4$ y el conjunto solución es $(-\infty,4]$.

La resolución fue breve porque el coeficiente de $x$ era positivo. Si ese coeficiente fuera negativo, el último paso invertiría la desigualdad. Si fuera cero, ni siquiera habría una variable por aislar. La estructura completa de una inequación lineal exige distinguir los tres casos.

### Qué llamaremos inequación lineal

En una variable, una inequación lineal propiamente dicha puede reducirse a la forma $ax\triangleleft d$, con $a\neq0$, $a,d\in\mathbb R$ y $\triangleleft$ igual a $<$, $\le$, $>$ o $\ge$.

Una expresión más simétrica, como $ax+b\triangleleft cx+d$, se reduce mediante sumas y restas a $(a-c)x\triangleleft d-b$. Esa reducción conserva el conjunto solución porque sólo usa transformaciones aditivas justificadas en [§22.3](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s03).

Al reunir los términos puede ocurrir que el coeficiente efectivo $a-c$ sea positivo, negativo o cero. Este último es el caso degenerado que debe formar parte del algoritmo, aunque la variable apareciera en la escritura original.

### Coeficiente positivo

Suponga primero $ax\le d$ con $a>0$. Dividir por $a$ está permitido y conserva la orientación: $x\le d/a$.

La solución es la semirrecta $(-\infty,d/a]$. Para las otras relaciones de orden ocurre lo mismo: un coeficiente positivo no cambia la dirección.

Por ejemplo, $5x-8>12\Longleftrightarrow5x>20\Longleftrightarrow x>4$. Cada transición conserva exactamente el conjunto solución: primero sumamos $8$ y después dividimos por $5>0$. La respuesta es $(4,\infty)$.

### Coeficiente negativo

Si el coeficiente es negativo, el aislamiento de $x$ termina con una inversión de la relación.

Considere $-4x+3<11$. Restamos $3$ y obtenemos $-4x<8$. Como $-4<0$, al dividir por $-4$ la desigualdad cambia de orientación: $x>-2$.

El conjunto solución es $(-2,\infty)$.

La inversión no aparece porque «la $x$ pasó al otro lado» ni porque exista una regla especial para despejar. Aparece únicamente en el paso en que dividimos por un número negativo.

### La forma general con la variable en ambos miembros

Considere $7x-4\ge3x+8$. Restar $3x$ y sumar $4$ conserva la relación: $4x\ge12$. Como $4>0$, dividir por $4$ da $x\ge3$. Por tanto, la solución es $[3,\infty)$.

En cambio, para $2x+5>6x-3$, reunir los términos produce $-4x>-8$. El coeficiente efectivo es negativo, así que dividir por $-4$ invierte la relación y obtenemos $x<2$.

El signo que importa no es el de los coeficientes tal como aparecen al principio, sino el del coeficiente que multiplica a $x$ después de reunir la variable en un solo miembro.

### Cuando el coeficiente se anula

El caso $a=0$ no puede tratarse dividiendo. La inequación $ax\triangleleft d$ se reduce entonces a una comparación entre números, $0\triangleleft d$.

La variable desaparece. Sólo quedan dos posibilidades:

- si la comparación numérica es verdadera, **todos los valores del dominio** son soluciones;
- si es falsa, el conjunto solución es $\varnothing$.

Por ejemplo, $3x+2<3x+5$ se reduce a $2<5$, que es verdadera. Sobre $\mathbb R$, su conjunto solución es $\mathbb R$.

En cambio, $2x+7\ge2x+9$ se reduce a $7\ge9$, que es falsa. Su conjunto solución es $\varnothing$.

Ambas situaciones pertenecen a la clasificación completa y deben reconocerse antes de intentar cualquier división.

### Clasificación de $ax+b\le c$

La estructura puede reunirse en un solo esquema. Sobre $\mathbb R$, $ax+b\le c\Longleftrightarrow ax\le c-b$.

A partir de allí:

| Condición sobre $a$ | Inequación equivalente | Conjunto solución |
|---|---|---|
| $a>0$ | $x\le\dfrac{c-b}{a}$ | $\left(-\infty,\dfrac{c-b}{a}\right]$ |
| $a<0$ | $x\ge\dfrac{c-b}{a}$ | $\left[\dfrac{c-b}{a},\infty\right)$ |
| $a=0$ y $b\le c$ | comparación verdadera | $\mathbb R$ |
| $a=0$ y $b>c$ | comparación falsa | $\varnothing$ |

Para $<$, $>$ o $\ge$ cambia la condición en el extremo, pero no la lógica de los tres regímenes del coeficiente.

### Parámetro fijo y control de signo

Considere la familia $ax+2\le5$, donde $a\in\mathbb R$ es un parámetro fijo.

Antes de dividir por $a$ debemos conocer su signo. La clasificación es:

- si $a>0$, entonces $x\le3/a$;
- si $a<0$, entonces $x\ge3/a$;
- si $a=0$, queda $2\le5$, verdadera para todo $x\in\mathbb R$.

No existe una sola fórmula obtenida «dividiendo por $a$» que sea válida sin separar $a>0$, $a<0$ y $a=0$. En [§22.13](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s13) estudiaremos familias paramétricas más ricas; aquí sólo necesitamos que el parámetro no oculte una condición de signo.

### El dominio declarado todavía manda

Las expresiones lineales están definidas para todo real, pero el problema puede imponer un dominio más pequeño.

Si resolvemos $2x-1<7$ con $x\in[0,10]$, la inequación da $x<4$. El conjunto solución no es entonces $(-\infty,4)$, porque buscamos sólo dentro del dominio declarado: $\operatorname{Sol}_{[0,10]}(2x-1<7)=[0,4)$. Resolver la inequación produce una condición de orden; el conjunto solución final se obtiene al conservar simultáneamente esa condición y el dominio vigente.

### Prueba de estrés: una cadena correcta con una justificación incorrecta

Un estudiante escribe

$$
-6x+1\le13
\Longleftrightarrow
-6x\le12
\Longleftrightarrow
x\ge-2
$$

y explica el último paso diciendo: «pasé el $-6$ dividiendo y cambié el signo».

La respuesta es correcta, pero la explicación es insuficiente. El paso válido es: dividir ambos miembros por $-6$, operación reversible porque $-6\neq0$, e invertir la relación porque $-6<0$.

La notación final puede ser breve; la razón matemática que la autoriza no debe desaparecer.

### Recuperación breve

Resuelva sobre $\mathbb R$.

**a)** $5x+4\le19$.

**b)** $7-3x>16$.

**c)** $4x-1\le4x+2$.

**d)** $6x+5>6x+9$.

**e)** $mx<6$, donde $m\in\mathbb R$ es un parámetro fijo.

**Respuesta razonada.** En **a)**, $5x\le15$ y, como $5>0$, $x\le3$. La solución es $(-\infty,3]$.

En **b)**, $-3x>9$ y, como $-3<0$, al dividir se obtiene $x<-3$. La solución es $(-\infty,-3)$.

En **c)**, al restar $4x$ queda $-1\le2$, verdadera para todo real. La solución es $\mathbb R$.

En **d)** queda $5>9$, que es falsa. La solución es $\varnothing$.

En **e)** hay tres casos. Si $m>0$, $x<6/m$; si $m<0$, $x>6/m$; si $m=0$, queda $0<6$, verdadera para todo real. La división por $m$ sólo aparece en los casos en que $m\neq0$ y después de conocer su signo.

### Qué debemos conservar de esta sección

Una inequación lineal se reduce mediante transformaciones equivalentes hasta una comparación de la forma $ax\triangleleft d$. El signo de $a$ decide la orientación del último paso; el caso $a=0$ decide si la solución es todo el dominio o el conjunto vacío.

El procedimiento completo exige **reunir la variable, identificar el coeficiente efectivo, clasificar su signo y declarar el conjunto solución dentro del dominio vigente**.



## 22.6. Inequaciones compuestas y sistemas {#apm-c22-s06}

Un valor puede tener que satisfacer más de una comparación. Si una temperatura debe superar $-2$ y no exceder $5$, las condiciones son $x>-2$ y $x\le5$. Su conjunto solución es $(-2,5]$: conservamos únicamente los valores admitidos por ambas condiciones. Si, en cambio, basta que la temperatura sea menor que $-2$ o mayor que $5$, obtenemos dos regiones separadas, $(-\infty,-2)\cup(5,\infty)$.

La diferencia procede del enlace lógico. Antes de operar con las expresiones, debemos identificar si se exige simultaneidad o si se ofrecen alternativas.

### Conjunción e intersección

Sean $P(x)$ y $Q(x)$ dos condiciones definidas sobre un mismo dominio efectivo $D$, y sean $S_P=\{x\in D:P(x)\}$ y $S_Q=\{x\in D:Q(x)\}$. Por definición de intersección, un elemento pertenece a $S_P\cap S_Q$ si pertenece a ambos conjuntos. Por tanto, el conjunto solución de «$P(x)$ y $Q(x)$» es $S_P\cap S_Q$.

Un **sistema de inequaciones en una variable** exige que todas sus condiciones se satisfagan simultáneamente. Si hay más de dos condiciones, se intersectan todos sus conjuntos solución. Los elementos siguen siendo números reales; la cantidad de condiciones no cambia el tipo de objeto que buscamos.

Resolvamos el sistema

$$
\begin{cases}
3x-2\ge4,\\
5-x>1.
\end{cases}
$$

La primera condición equivale a $3x\ge6$ y después a $x\ge2$, porque dividimos por $3>0$. La segunda equivale a $-x>-4$ y después a $x<4$, porque dividimos por $-1<0$. Sus soluciones individuales son $[2,\infty)$ y $(-\infty,4)$. La región común es $S=[2,4)$.

El punto $2$ satisface ambas condiciones: en la primera produce igualdad y en la segunda produce $3>1$. El punto $4$ queda fuera porque la segunda condición produciría $1>1$. La inclusión de cada extremo depende de todas las condiciones que actúan allí.

### Dobles desigualdades

La escritura $a<E(x)\le b$ abrevia la conjunción $a<E(x)$ y $E(x)\le b$. Una transformación aplicada a los tres miembros sólo es válida si conserva esas dos comparaciones.

Considere $-1<2x+3\le9$. Restar $3$ en los tres miembros equivale a restarlo en cada una de las comparaciones y produce $-4<2x\le6$. Dividir por $2>0$ conserva ambas direcciones, de modo que $-2<x\le3$. La solución es $(-2,3]$.

Cuando el divisor es negativo, las dos relaciones se invierten. Para $-1<-2x+3\le9$, restamos $3$ y obtenemos $-4<-2x\le6$. Al dividir por $-2$ queda $2>x\ge-3$. Para leerla de izquierda a derecha en orden creciente, reescribimos la cadena como $-3\le x<2$. Así, $S=[-3,2)$.

La primera escritura tras dividir es válida: afirma simultáneamente $x<2$ y $x\ge-3$. Reordenarla mejora la lectura, pero no autoriza cambiar la inclusión de los extremos.

### Una comparación compuesta puede resultar imposible

Estudie $2x+1>7$ y $x\le2$. La primera condición equivale a $x>3$, de modo que el sistema exige $x\in(3,\infty)\cap(-\infty,2]$. Los conjuntos no tienen elementos comunes y $S=\varnothing$.

También puede sobrevivir un único punto. Las condiciones $x\ge2$ y $x\le2$ tienen solución $\{2\}=[2,2]$. Si una de ellas se hace estricta, por ejemplo $x>2$ y $x\le2$, la intersección es vacía. Esta variación muestra por qué una frontera coincidente debe examinarse antes de escribir un intervalo.

### Disyunción y unión

Para condiciones $P,Q$ definidas en $D$, un valor satisface «$P(x)$ o $Q(x)$» si satisface al menos una de ellas. Por definición de unión, su conjunto solución es $S_P\cup S_Q$. La palabra «o» es inclusiva: también se admiten los valores que satisfacen las dos condiciones.

Resolvamos $2x+1<5$ o $3x-6\ge6$. La primera rama da $x<2$ y la segunda da $x\ge4$. Por tanto, $S=(-\infty,2)\cup[4,\infty)$.

Si las alternativas fueran $x<3$ o $x\ge1$, su unión sería $\mathbb R$. Todo real menor que $3$ cumple la primera; los restantes son mayores o iguales que $3$ y también mayores o iguales que $1$, por lo que cumplen la segunda. El solapamiento de las ramas no crea una restricción adicional.

### Alcance de los enlaces

Cuando un problema combina «y» con «o», los paréntesis determinan qué condiciones se agrupan. Compare «($x<0$ o $x>3$) y $x\le5$» con «$x<0$ o ($x>3$ y $x\le5$)».

En este ejemplo ambos conjuntos coinciden, porque todos los valores con $x<0$ ya cumplen $x\le5$. Esa coincidencia depende del caso. Para las condiciones «($x<4$ o $x>6$) y $x\ge2$», la solución es $[2,4)\cup(6,\infty)$. Para «$x<4$ o ($x>6$ y $x\ge2$)», la solución es $(-\infty,4)\cup(6,\infty)$. El valor $0$ pertenece sólo al segundo conjunto.

La expresión de conjuntos permite conservar el alcance: en el primer caso calculamos $(S_P\cup S_Q)\cap S_R$; en el segundo, $S_P\cup(S_Q\cap S_R)$.

### Dominio común y restricciones heredadas

En un sistema algebraico ordinario, todas las expresiones deben estar definidas simultáneamente. Primero fijamos el dominio común y después resolvemos cada condición dentro de él.

Suponga que el dominio común ya conocido es $D=\mathbb R\setminus\{1\}$ y que las condiciones son $x\ge0$ y $x\le2$. Su intersección dentro de $D$ es $[0,1)\cup(1,2]$. La condición no estricta en $2$ permite incluirlo; ninguna de las dos condiciones reinserta el punto $1$.

Para una disyunción también debe declararse la convención de dominio. Aquí interpretamos sus ramas sobre un dominio efectivo común, donde todas las expresiones escritas tienen significado. Si se desea unir problemas definidos sobre dominios distintos, se describen primero sus conjuntos solución respectivos y luego se toma su unión; no se evalúa una expresión indefinida como si fuera falsa.

### Prueba de estrés: resolver cada condición no termina el sistema

Una resolución defectuosa obtiene $x\ge2$ de una condición y $x<4$ de otra, y declara $[2,\infty)\cup(-\infty,4)=\mathbb R$ como solución del sistema. Las resoluciones individuales son correctas; la ruptura ocurre al usar unión donde se exige intersección.

El valor $10$ pertenece a la unión, pero incumple $x<4$. La reparación consiste en conservar la simultaneidad: $[2,\infty)\cap(-\infty,4)=[2,4)$. Una prueba puntual refuta la respuesta equivocada; la intersección justificada demuestra la respuesta completa.

### Recuperación breve

**a)** Resuelva $1<3x-2\le10$.

**b)** Resuelva el sistema $2-x\ge0$ y $2x+1>3$.

**c)** Resuelva $x\le-1$ o $x>2$, y explique qué cambiaría si se reemplazara «o» por «y».

**Respuesta razonada.** En **a)** sumamos $2$ en los tres miembros y dividimos por $3>0$: $3<3x\le12$, luego $1<x\le4$. La solución es $(1,4]$.

En **b)** la primera condición da $-x\ge-2$, es decir $x\le2$; la segunda da $2x>2$, es decir $x>1$. La intersección es $(1,2]$. En $2$ ambas comparaciones son verdaderas; en $1$ la segunda es falsa.

En **c)** la disyunción da $(-\infty,-1]\cup(2,\infty)$. Con «y» se requerirían las dos condiciones simultáneamente, pero ningún real puede ser a la vez menor o igual que $-1$ y mayor que $2$. La solución sería $\varnothing$.

### Qué debemos conservar de esta sección

Las condiciones simultáneas se resuelven mediante intersección; las alternativas, mediante unión. Una doble desigualdad abrevia dos comparaciones que deben conservarse en cada operación. La resolución completa mantiene el alcance de los enlaces, el dominio común y la pertenencia de cada frontera a todas las condiciones exigidas.



## 22.7. Valor absoluto y distancia {#apm-c22-s07}

La condición $|x-2|<3$ describe los puntos cuya distancia a $2$ es menor que $3$. Sobre la recta, desplazarse tres unidades desde $2$ lleva a $-1$ y $5$. Los puntos buscados quedan entre esas fronteras y ninguna pertenece a la solución. La interpretación geométrica sugiere $(-1,5)$; vamos a justificarla algebraicamente y a controlar qué ocurre cuando cambia la comparación.

### Recuperar la definición

Para un real $u$, $|u|=u$ si $u\ge0$ y $|u|=-u$ si $u<0$. En ambos casos $|u|\ge0$. Por eso comparar un valor absoluto con un número negativo produce respuestas distintas de las habituales y debe examinarse antes de abrir ramas.

Además, $|x-a|$ es la distancia entre $x$ y $a$. Una cota superior sobre esa distancia selecciona la zona próxima a $a$; una cota inferior selecciona puntos exteriores.

### Cotas superiores positivas

Sea $c>0$. La equivalencia $|u|\le c\Longleftrightarrow -c\le u\le c$ puede demostrarse por el signo de $u$.

Si $u\ge0$, la condición $|u|\le c$ significa $u\le c$. La desigualdad inferior $-c\le u$ ya se cumple porque $-c<0\le u$. Si $u<0$, la condición significa $-u\le c$, equivalente a $u\ge-c$ al multiplicar por $-1$. La desigualdad superior $u\le c$ ya se cumple. Así, en ambos casos aparecen las dos cotas. Para la vuelta, las mismas divisiones por casos muestran que esas cotas implican $|u|\le c$.

Con desigualdades estrictas se obtiene $|u|<c\Longleftrightarrow -c<u<c$. Sustituir $u$ por una expresión $A(x)$ conserva estas equivalencias en el dominio donde $A$ esté definida.

Por ejemplo, $|2x-1|\le5$ equivale a $-5\le2x-1\le5$. Sumando $1$ y dividiendo por $2>0$, resulta $-2\le x\le3$. La solución es $[-2,3]$. En ambos extremos el valor absoluto vale $5$, por lo que la comparación no estricta los admite.

### Cotas inferiores positivas

Para $c>0$, la condición $|u|>c$ exige que $u$ quede a más de $c$ unidades del origen. Su solución se distribuye en dos ramas: $u<-c$ o $u>c$.

Algebraicamente, si $u\ge0$, queda $u>c$; si $u<0$, queda $-u>c$, equivalente a $u<-c$. Cada rama tiene el signo requerido, de modo que también prueba la vuelta. Con inclusión de la igualdad, $|u|\ge c\Longleftrightarrow(u\le-c\ \text{o}\ u\ge c)$.

Considere $|3x+2|>4$. Las ramas son $3x+2<-4$ o $3x+2>4$. Dividir los despejes correspondientes por $3>0$ da $x<-2$ o $x>2/3$. Por tanto, $S=(-\infty,-2)\cup(2/3,\infty)$.

Usar intersección en este ejemplo exigiría que una misma cantidad fuera menor que $-4$ y mayor que $4$. El error produciría un conjunto vacío donde existen dos semirrectas.

### Qué ocurre cuando la cota es cero o negativa

La no negatividad decide estos regímenes sin aplicar una receta de dos ramas.

| Comparación | Si $c=0$ | Si $c<0$ |
|---|---|---|
| $|A(x)|<c$ | $\varnothing$ | $\varnothing$ |
| $|A(x)|\le c$ | ceros de $A$ en el dominio | $\varnothing$ |
| $|A(x)|>c$ | valores del dominio con $A(x)\ne0$ | todo el dominio |
| $|A(x)|\ge c$ | todo el dominio | todo el dominio |

En la fila $|A(x)|\le0$, sólo puede ocurrir $|A(x)|=0$, equivalente a $A(x)=0$. En la fila estricta $|A(x)|>0$, se excluyen esos ceros. Las respuestas «todo el dominio» conservan cualquier restricción previa de la expresión $A$.

Así, $|x-4|\le0$ tiene solución $\{4\}$, mientras que $|x-4|<0$ no tiene soluciones. Para $|1/(x-1)|>-2$, toda comparación definida es verdadera, pero $x=1$ continúa excluido: $S=\mathbb R\setminus\{1\}$.

### Dos valores absolutos

La comparación $|A(x)|\le|B(x)|$ tiene ambos miembros no negativos. Para $r,s\ge0$, $r\le s$ equivale a $r^2\le s^2$: si $r\le s$, entonces $(s-r)(s+r)\ge0$; si $r>s$, ambos factores de $(r-s)(r+s)$ son positivos y $r^2>s^2$. Por tanto, la comparación equivale a $A(x)^2\le B(x)^2$.

Por ejemplo, $|x-1|\le|x+2|$ equivale a $(x-1)^2\le(x+2)^2$. Expandir y cancelar $x^2$ da $-2x+1\le4x+4$, de donde $x\ge-1/2$. Geométricamente, $-1/2$ es el punto medio entre $1$ y $-2$; hacia su derecha los puntos están al menos tan cerca de $1$ como de $-2$.

El argumento de cuadrados necesita la no negatividad de ambos miembros. Para expresiones de signo libre, elevar al cuadrado puede cambiar la comparación.

### Prueba de estrés

La afirmación $|x-2|\ge3\Longleftrightarrow -3\le x-2\le3$ es falsa. El segundo miembro describe distancia menor o igual que $3$; $x=2$ lo satisface y no satisface el primero. La reparación es $x-2\le-3$ o $x-2\ge3$, es decir $x\le-1$ o $x\ge5$.

### Recuperación breve

**a)** Resuelva $|x+1|<2$.

**b)** Resuelva $|2x-3|\ge1$.

**c)** Resuelva $|x+2|>0$.

**Respuesta razonada.** En **a)**, $-2<x+1<2$ equivale a $-3<x<1$, de modo que $S=(-3,1)$. En **b)**, $2x-3\le-1$ o $2x-3\ge1$ da $x\le1$ o $x\ge2$; $S=(-\infty,1]\cup[2,\infty)$. En **c)** se admiten todos los reales excepto el cero de $x+2$, por lo que $S=\mathbb R\setminus\{-2\}$.

### Qué debemos conservar de esta sección

Una cota superior positiva de distancia produce dos condiciones simultáneas; una cota inferior positiva produce alternativas exteriores. Las cotas cero y negativas se deciden mediante $|A|\ge0$. El dominio se conserva al abrir las ramas y el signo de la comparación decide si las fronteras se incluyen.



## 22.8. Cuadráticas: de ecuación a análisis de signos {#apm-c22-s08}

La ecuación $x^2-x-6=0$ localiza dos puntos, $-2$ y $3$. La inequación $x^2-x-6\le0$ pregunta también por todos los puntos entre las raíces y fuera de ellas. Necesitamos determinar en qué regiones el polinomio es negativo, positivo o cero.

### Llevar la comparación a cero

Una comparación $P(x)\le Q(x)$ equivale a $P(x)-Q(x)\le0$ porque restamos la misma expresión definida en ambos miembros. Para una cuadrática, obtenemos $ax^2+bx+c\triangleleft0$, con $a\ne0$.

Esta forma concentra la pregunta en el signo de una expresión. La ecuación frontera $ax^2+bx+c=0$ localiza sus ceros, pero todavía no decide dónde se cumple la inequación.

### Dos factores lineales

Por C19, $x^2-x-6=(x+2)(x-3)$. Si $x<-2$, ambos factores son negativos y el producto es positivo. Si $-2<x<3$, el primer factor es positivo y el segundo negativo, de modo que el producto es negativo. Si $x>3$, ambos son positivos.

| Región | $x+2$ | $x-3$ | Producto |
|---|---|---|---|
| $(-\infty,-2)$ | $-$ | $-$ | $+$ |
| $(-2,3)$ | $+$ | $-$ | $-$ |
| $(3,\infty)$ | $+$ | $+$ | $+$ |

Cada fila representa todos los puntos del intervalo. El signo de un factor lineal $x-r$ queda determinado por estar a la izquierda o a la derecha de $r$, así que no necesitamos comprobar infinitos valores por separado.

La condición $\le0$ admite la región negativa y los ceros. Por tanto, $S=[-2,3]$. Para $<0$, la solución sería $(-2,3)$; para $>0$, las regiones exteriores abiertas; para $\ge0$, las exteriores con las raíces incluidas.

### Forma general con dos raíces distintas

Si $P(x)=a(x-r_1)(x-r_2)$, con $r_1<r_2$, el producto de los factores lineales es positivo fuera de $[r_1,r_2]$ y negativo dentro. Si $a>0$, ese signo se conserva; si $a<0$, se invierte. La orientación depende de ese coeficiente, no sólo de las raíces.

Por ejemplo, $-2(x+1)(x-4)>0$ equivale a $(x+1)(x-4)<0$ al dividir por $-2$. La solución es $(-1,4)$. La prueba de signo revela por qué escoger automáticamente «los exteriores» sería incorrecto.

### Una raíz doble

La cuadrática $(x-2)^2$ es positiva para $x\ne2$ y cero en $2$. Como un cuadrado nunca es negativo, $(x-2)^2<0$ no tiene soluciones, mientras que $(x-2)^2\le0$ tiene solución $\{2\}$.

El factor cuadrado mantiene el signo positivo a ambos lados de su cero. Con coeficiente negativo, $-3(x-2)^2$ es no positivo en toda la recta y sólo se anula en $2$. Por tanto, $-3(x-2)^2\ge0$ tiene solución $\{2\}$ y $-3(x-2)^2<0$ tiene solución $\mathbb R\setminus\{2\}$.

### Ausencia de raíces reales

Para una cuadrática general, completar cuadrados permite estudiar el signo sin usar gráficas ni cálculo:

$$
ax^2+bx+c=a\left[\left(x+\frac{b}{2a}\right)^2-\frac{\Delta}{4a^2}\right],
\qquad \Delta=b^2-4ac.
$$

Si $\Delta<0$, la cantidad $-\Delta/(4a^2)$ es positiva. El corchete es entonces estrictamente positivo para todo real, porque suma un cuadrado no negativo y una constante positiva. El signo de la cuadrática coincide siempre con el de $a$.

Por ejemplo, $x^2+2x+2=(x+1)^2+1>0$ para todo real. Así, $x^2+2x+2\le0$ tiene solución vacía y $x^2+2x+2>0$ tiene solución $\mathbb R$.

Si $\Delta=0$, la forma completada es un múltiplo de un cuadrado y se aplica el caso anterior. Si $\Delta>0$, la fórmula cuadrática de C21 da dos raíces distintas y permite regresar al análisis de factores. La clasificación por discriminante organiza tres mecanismos de signo diferentes.

### Prueba de estrés: una raíz no siempre cambia el signo

La regla «el signo se invierte cada vez que atravesamos una raíz» falla para $(x-1)^2$. En $x=0$ y $x=2$ la expresión vale $1$. La raíz es una frontera donde la expresión se anula, pero los dos intervalos vecinos tienen el mismo signo. La justificación por factores distingue este caso sin necesidad de imponer una regla adicional.

### Recuperación breve

**a)** Resuelva $(x-1)(x-5)\ge0$.

**b)** Resuelva $-x^2+4x-4\ge0$.

**c)** Resuelva $2x^2+2<0$.

**Respuesta razonada.** En **a)** el producto es positivo fuera de las raíces y negativo entre ellas; al admitir igualdad, $S=(-\infty,1]\cup[5,\infty)$. En **b)** la expresión es $-(x-2)^2$, no positiva, así que sólo puede ser no negativa donde se anula: $S=\{2\}$. En **c)**, $2x^2+2\ge2>0$ para todo real; $S=\varnothing$.

### Qué debemos conservar de esta sección

Los ceros dividen el problema en regiones, y los signos de los factores deciden cuáles seleccionar. Dos raíces distintas, una raíz doble y ausencia de raíces producen comportamientos diferentes. Completar cuadrados y el discriminante permiten justificar esa clasificación; al finalizar, se comprueban la relación de orden y cada extremo.



## 22.9. Productos polinómicos y tablas de signos {#apm-c22-s09}

La técnica de [§22.8](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s08) se extiende a productos con varios factores. Considere $P(x)=(x+2)(x-1)^2(x-3)$. Sus ceros son $-2$, $1$ y $3$, pero el factor cuadrado tiene un papel distinto de los dos factores lineales.

### Por qué funciona una tabla

Para $x\ne r$, el factor $x-r$ es negativo si $x<r$ y positivo si $x>r$. Una potencia par $(x-r)^{2k}$, con $k$ entero positivo, es positiva a ambos lados de $r$; una potencia impar conserva el signo de $x-r$. En $x=r$, ambas se anulan.

Ordenar los ceros reales de los factores permite dividir la recta en intervalos donde cada signo es fijo. El producto tiene entonces un signo fijo, obtenido por las reglas de multiplicación de positivos y negativos. Éste es el fundamento de la tabla; elegir un punto de prueba por intervalo sólo abrevia una constancia que debe estar justificada.

Un factor como $x^2+1$ es positivo en todo $\mathbb R$ y no introduce puntos críticos. Un factor $-(x^2+1)$ invierte el signo global. Si aparecen factores cuya constancia no está justificada por herramientas conocidas, una colección de puntos de prueba aislados no sustituye la demostración.

### Un producto con un factor repetido

Para el producto inicial:

| Región | $x+2$ | $(x-1)^2$ | $x-3$ | $P(x)$ |
|---|---|---|---|---|
| $(-\infty,-2)$ | $-$ | $+$ | $-$ | $+$ |
| $(-2,1)$ | $+$ | $+$ | $-$ | $-$ |
| $(1,3)$ | $+$ | $+$ | $-$ | $-$ |
| $(3,\infty)$ | $+$ | $+$ | $+$ | $+$ |

El signo cambia al atravesar $-2$ y $3$, pero permanece negativo a ambos lados de $1$. Allí el producto se anula. Para $P(x)<0$, la solución es $(-2,1)\cup(1,3)$; para $P(x)\le0$, los tres ceros se admiten y las regiones se reúnen en $[-2,3]$.

El cero interior $1$ no puede omitirse en la inequación estricta. Aunque no cambie el signo, sí puede cambiar la pertenencia al conjunto solución.

### Coeficientes y factores siempre positivos

Resolvamos $-2(x+1)^3(x-2)^2(x^2+1)\ge0$. Los factores $(x-2)^2$ y $x^2+1$ son positivos fuera de $2$, y el segundo también lo es en $2$. Para $x\ne2$, el signo total es el opuesto del signo de $x+1$: positivo si $x<-1$ y negativo si $x>-1$. Los ceros son $-1$ y $2$.

Se admiten todos los valores $x\le-1$ y también el cero aislado $2$. Por tanto, $S=(-\infty,-1]\cup\{2\}$. Un conjunto solución puede contener una región y un punto aislado; la notación de intervalos debe conservar ambas partes.

### Una tabla es una representación del argumento

Podemos marcar signos con $+$ y $-$, pero cada marca debe poder traducirse a una afirmación. En la fila $x<-2$ del primer ejemplo, $x+2<0$ y $x-3<0$; su producto es positivo y el cuadrado es positivo porque $x\ne1$. El razonamiento demuestra el signo para todo el intervalo, sin usar continuidad.

Para un producto factorizado con exponentes enteros positivos, el número de factores negativos contados con sus exponentes determina el signo: un número par da positivo y uno impar da negativo. Este conteo deriva de $(-1)^{2k}=1$ y $(-1)^{2k+1}=-1$, ya estudiados en C18.

### Prueba de estrés: conservar un cero aislado

Si alguien resuelve $(x-2)^2(x+1)\le0$ y responde $(-\infty,-1]$, pierde $x=2$, donde el producto vale cero. Para $x\ne2$, el cuadrado es positivo y exige $x+1\le0$; en $2$ hay que evaluar por separado. La solución completa es $(-\infty,-1]\cup\{2\}$.

Dividir por el cuadrado sin registrar su cero elimina esa solución. La reparación usa dos casos, no una verificación tardía de los valores que quedaron.

### Recuperación breve

**a)** Resuelva $(x+3)(x-2)^2>0$.

**b)** Resuelva $(x+3)(x-2)^2\ge0$.

**Respuesta razonada.** Fuera de $2$, el cuadrado es positivo y el producto tiene el signo de $x+3$. En **a)** se requiere $x>-3$ y se excluye $2$ porque allí el producto es cero: $S=(-3,2)\cup(2,\infty)$. En **b)** se incluye $-3$ y también $2$; $S=[-3,\infty)$.

### Qué debemos conservar de esta sección

Una tabla registra signos constantes justificados por los factores. La paridad de un exponente decide si el signo cambia al atravesar su cero, mientras que la comparación estricta o no estricta decide si ese cero pertenece a la solución. Un cero que no cambia el signo todavía puede separar regiones o aportar un punto aislado.



### Ceros y puntos excluidos no tienen la misma función

En $(x-a)^2/(x-b)$, con $a\ne b$, el cuadrado no cambia signo al atravesar $a$, pero allí el cociente vale cero. El punto $b$ nunca está definido. Para $\ge0$ se incluyen los $x>b$ y además $a$ si $a<b$; para $>0$ se exige $x>b$ y se retira $a$ si cae en esa región. **Control resuelto:** si $a=b$, la expresión se simplifica a $x-a$ solamente en $x\ne a$. La inequación $\ge0$ da $(a,\infty)$, no $[a,\infty)$. Cuando coinciden factores, la escritura reducida puede cambiar su lectura local; las exclusiones originales permanecen. Paridad, signo y pertenencia al dominio son tres controles distintos.



## 22.10. Inequaciones racionales {#apm-c22-s10}

Para resolver $(x-2)/(x+1)\ge0$ debemos saber dónde numerador y denominador tienen signos iguales, o dónde el numerador se anula con denominador no nulo. El punto $-1$ y el punto $2$ organizan la recta, pero sólo el segundo puede producir una igualdad admisible.

### Dominio antes de transformar

Una inequación $P(x)/Q(x)\triangleleft0$ se interpreta donde $Q(x)\ne0$. Para el ejemplo, $D=\mathbb R\setminus\{-1\}$. El numerador se anula en $2$.

| Región | $x-2$ | $x+1$ | Cociente |
|---|---|---|---|
| $(-\infty,-1)$ | $-$ | $-$ | $+$ |
| $(-1,2)$ | $-$ | $+$ | $-$ |
| $(2,\infty)$ | $+$ | $+$ | $+$ |

La tabla tiene el mismo fundamento que para productos: el signo de cada factor es fijo en cada intervalo. Dividir por un positivo conserva el signo del numerador y dividir por un negativo lo invierte. El cociente es no negativo en las regiones exteriores; se incluye $2$ y se excluye $-1$. Así, $S=(-\infty,-1)\cup[2,\infty)$.

Un **polo**, en los ejemplos racionales sin cancelación, es un punto donde el denominador se anula y el cociente no está definido. Para resolver basta distinguir «cero admisible» y «punto excluido»; no necesitamos estudiar límites ni comportamientos analíticos.

### Una comparación con otro miembro

Resolvamos $(x+1)/(x-2)\le2$. El dominio es $x\ne2$. Restar $2$ conserva la comparación y reunir los términos da
$\frac{x+1}{x-2}-2=\frac{5-x}{x-2}$.
Los puntos críticos son $2$ y $5$. Si $x<2$, el numerador es positivo y el denominador negativo: el cociente es negativo. Si $2<x<5$, ambos son positivos. Si $x>5$, el numerador es negativo y el denominador positivo. Para $\le0$, se selecciona $(-\infty,2)\cup[5,\infty)$.

Multiplicar directamente por $x-2$ sin separar su signo perdería la región $x<2$, donde la comparación debe invertirse. Llevar todo a un miembro evita esa bifurcación operativa.

### Cancelaciones y agujeros del dominio

Considere $(x^2-1)/(x-1)>0$. El dominio original excluye $1$. Dentro de él, factorizar y cancelar $x-1$ transforma el cociente en $x+1$. La condición equivalente es $x+1>0$ con $x\ne1$, de modo que $S=(-1,1)\cup(1,\infty)$.

La forma simplificada está definida en $1$, pero la expresión original no. Ese punto cancelado es un agujero de dominio y no debe confundirse con un cero del cociente ni con un polo sin cancelación.

Para una comparación no estricta, la exclusión permanece. La inequación $(x^2-1)/(x-1)\ge0$ tiene solución $[-1,1)\cup(1,\infty)$. El punto $-1$ sí pertenece porque anula el numerador con denominador no nulo.

### Numerador y denominador con factores repetidos

En $(x-1)^2/[(x+2)(x-3)]\le0$, el dominio excluye $-2$ y $3$. Fuera de $1$, el numerador es positivo. El denominador es negativo en $(-2,3)$ y positivo en las regiones exteriores. Por tanto, el cociente es negativo en $(-2,1)\cup(1,3)$ y cero en $1$. Al incluir ese cero, $S=(-2,3)$.

Si el denominador contuviera $(x-1)^2$, ese punto se excluiría aunque el signo no cambiara al atravesarlo. La paridad controla el signo; la ubicación en numerador o denominador controla el dominio y la posible igualdad.

### Multiplicar por un cuadrado positivo

Existe una segunda ruta útil. En el dominio $Q(x)\ne0$, se cumple $Q(x)^2>0$. Multiplicar por ese cuadrado conserva la dirección:

$$
\frac{P(x)}{Q(x)}\le0
\Longleftrightarrow
P(x)Q(x)\le0,
\qquad Q(x)\ne0.
$$

La identidad $Q^2(P/Q)=PQ$ justifica la transformación. La restricción escrita al lado es indispensable: si se olvidara, los ceros de $Q$ parecerían soluciones de la inequación polinómica.

Para $(x-2)/(x+1)\ge0$, la ruta produce $(x-2)(x+1)\ge0$ con $x\ne-1$. El producto selecciona $(-\infty,-1]\cup[2,\infty)$ y el dominio retira $-1$, recuperando la respuesta de la tabla.

### Prueba de estrés

Una resolución defectuosa de $1/(x-1)\le0$ multiplica por $x-1$ y obtiene $1\le0$, declarando solución vacía. La transformación conserva la dirección sólo en $x>1$; en $x<1$ debe invertirla. El numerador es positivo, así que el cociente es negativo para $x<1$ y positivo para $x>1$. La solución correcta es $(-\infty,1)$.

### Recuperación breve

**a)** Resuelva $(x+2)/(x-4)>0$.

**b)** Resuelva $(x^2-4)/(x-2)\le0$.

**Respuesta razonada.** En **a)** se excluye $4$ por dominio y $-2$ por la comparación estricta. El cociente es positivo cuando sus dos factores tienen el mismo signo: $S=(-\infty,-2)\cup(4,\infty)$. En **b)** el dominio excluye $2$; cancelar sobre ese dominio deja $x+2\le0$, es decir $x\le-2$. Ningún valor de esa semirrecta es el excluido $2$, de modo que $S=(-\infty,-2]$.

### Qué debemos conservar de esta sección

Las inequaciones racionales conservan el dominio original durante toda simplificación. Los ceros de numerador pueden satisfacer una comparación no estricta; los ceros de denominador nunca se incluyen. Llevar la comparación a cero y estudiar los signos evita multiplicar por un factor desconocido. Si se usa un cuadrado positivo, su positividad se justifica dentro del dominio y las exclusiones se mantienen.



## 22.11. Transformaciones y formas estratégicas {#apm-c22-s11}

Una expresión puede admitir varias escrituras correctas, pero no todas dejan ver con igual claridad su signo. Para resolver $(x-1)^2-9\ge0$, expandir produce $x^2-2x-8\ge0$; factorizar como diferencia de cuadrados produce $(x-4)(x+2)\ge0$. La segunda forma muestra directamente las fronteras $-2$ y $4$ y permite aplicar [§22.8](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s08).

Elegir una forma útil es parte del razonamiento. Las transformaciones deben conservar el conjunto solución y reducir la dificultad que todavía queda.

### Llevar todo a un miembro

Comparar $E(x)$ con $F(x)$ equivale a comparar $E(x)-F(x)$ con cero, dentro del dominio común. Esa resta permite reunir los signos en una sola expresión. Para $x^2+1\le3x-1$, obtenemos $x^2-3x+2\le0$, después $(x-1)(x-2)\le0$, y finalmente $S=[1,2]$.

La expansión fue útil para reunir términos, y la factorización posterior fue útil para decidir signos. Ninguna forma es obligatoria por sí misma: su función cambia durante la resolución.

### Conservar factores visibles

Para $(x+1)(x-2)^2(x-5)\le0$, expandir un polinomio de grado cuatro ocultaría información que ya tenemos. Fuera de $2$, el cuadrado es positivo y los dos factores lineales restantes dan signo no positivo en $[-1,5]$. El cero $2$ está dentro de esa región y se admite, de modo que $S=[-1,5]$.

Si la comparación fuera estricta, habría que retirar $-1$, $2$ y $5$: $S=(-1,2)\cup(2,5)$. La forma factorizada evita volver a buscar esos ceros después de expandir.

### Normalizar un signo global

Para $-(x-3)(x+4)\le0$, multiplicar por $-1$ invierte la comparación y deja $(x-3)(x+4)\ge0$. Su solución es $(-\infty,-4]\cup[3,\infty)$.

También podríamos mantener el signo negativo en una tabla. Ambas rutas son válidas. Normalizarlo al comienzo reduce una operación en cada fila, siempre que se registre la inversión de la desigualdad.

### Un denominador común permite comparar

Resolvamos $1/(x-1)\ge1/(x+1)$. El dominio excluye $-1$ y $1$. Restar el segundo miembro y reunir las fracciones da
$\frac{1}{x-1}-\frac{1}{x+1}=\frac{2}{(x-1)(x+1)}$.
El numerador es positivo y nunca se anula. Se requiere entonces denominador positivo, que ocurre para $x<-1$ o $x>1$. La solución es $(-\infty,-1)\cup(1,\infty)$. La igualdad nunca se alcanza, aunque la comparación escrita sea no estricta.

Multiplicar por $(x-1)(x+1)$ sin controlar su signo sería inseguro. Reunir las fracciones permite localizar esa misma información de manera explícita.

### Comparar rutas completas

Para $(x-2)/(x+1)\le1$, la resta produce $-3/(x+1)\le0$ con $x\ne-1$. Como el numerador es negativo, el denominador debe ser positivo: $x>-1$. No hay igualdad porque el numerador nunca es cero. Así, $S=(-1,\infty)$.

Una segunda ruta separa casos. Si $x>-1$, el denominador es positivo y multiplicar conserva la dirección: $x-2\le x+1$, verdadera. Si $x<-1$, el denominador es negativo y la dirección se invierte: $x-2\ge x+1$, falsa. Se obtiene la misma semirrecta.

La primera ruta concentra el signo en una fracción; la segunda hace visible por qué falla la multiplicación indiscriminada. Elegir una depende de la dificultad que queremos controlar.

### Una cota puede ahorrar cálculos

La inequación $(x-1)^2+2\le0$ se decide sin buscar raíces: el cuadrado es no negativo y la expresión es al menos $2$. La solución es vacía.

Para $(x-1)^2+2\ge0$, esa misma cota demuestra que todo real es solución. Una técnica más extensa no añade información cuando una propiedad global ya responde a la comparación.

### Prueba de estrés: sumar inequaciones no conserva toda la información

De $x\ge0$ y $-x\ge0$ podemos sumar y obtener $0\ge0$. La suma es una consecuencia válida, pero no una condición equivalente al sistema: el sistema sólo admite $x=0$, mientras que la comparación numérica es verdadera para todo real.

La fuerza lógica importa también en la elección de método. Una consecuencia necesaria puede servir como filtro, pero la reconstrucción debe conservar las condiciones que se perdieron.

### Recuperación breve

**a)** Elija una forma útil para resolver $(x+2)^2-16>0$.

**b)** Resuelva $x^2+3\le0$ sin fórmula cuadrática.

**c)** Resuelva $1/(x-2)-1/(x+2)>0$.

**Respuesta razonada.** En **a)** la diferencia de cuadrados es $(x-2)(x+6)>0$, cuya solución es $(-\infty,-6)\cup(2,\infty)$. En **b)** la expresión es al menos $3>0$, así que $S=\varnothing$. En **c)** el dominio excluye $\pm2$ y la diferencia es $4/[(x-2)(x+2)]$. Para que sea positiva, el denominador debe ser positivo: $S=(-\infty,-2)\cup(2,\infty)$.

### Qué debemos conservar de esta sección

La forma útil revela el dato que falta: una factorización muestra ceros y signos, un denominador común reúne comparaciones y una forma cuadrática puede mostrar una cota global. La economía de cálculo es válida cuando conserva dominio, orientación y fuerza lógica de las transformaciones.



## 22.12. Sustituciones y reconstrucción de preimágenes {#apm-c22-s12}

La inequación $x^4-5x^2+4\le0$ contiene una cuadrática en $x^2$. La sustitución $u=x^2$ permite resolver esa estructura conocida, pero también introduce una condición: $u\ge0$. Al terminar debemos regresar a todos los valores reales de $x$ que producen los valores admitidos de $u$.

### La variable auxiliar tiene una imagen

Sea $\phi:D\to\mathbb R$ una función conocida y sea $u=\phi(x)$. Si la inequación depende de $x$ mediante $\phi(x)$, se puede estudiar primero en $u$, restringido a $\phi(D)$. Si $S_u$ es el conjunto auxiliar válido, el conjunto original es

$$
S_x=\{x\in D:\phi(x)\in S_u\}=\phi^{-1}(S_u).
$$

La escritura $\phi^{-1}(S_u)$ denota preimagen, como en C9; no exige que $\phi$ tenga función inversa. Esta distinción permite manejar sustituciones como $u=x^2$, que identifican dos valores opuestos de $x$.

### Una bicuadrada

Para el ejemplo inicial, $u^2-5u+4=(u-1)(u-4)$. La inequación auxiliar da $1\le u\le4$, compatible con $u\ge0$.

La vuelta exige $1\le x^2\le4$. Por la no negatividad de $|x|$ y la comparación de cuadrados, equivale a $1\le|x|\le2$. La cota inferior produce $x\le-1$ o $x\ge1$; la superior produce $-2\le x\le2$. Al intersectarlas, $S_x=[-2,-1]\cup[1,2]$.

Los cuatro extremos hacen cero el polinomio original. Un valor entre $-1$ y $1$ tiene $x^2<1$ y no satisface la condición auxiliar; un valor con $|x|>2$ tiene $x^2>4$ y tampoco la satisface. La reconstrucción cubre las dos ramas y demuestra las exclusiones.

### Restricciones del problema auxiliar

En $x^4+3x^2+2\le0$, la sustitución produce $(u+1)(u+2)\le0$, cuya solución formal es $[-2,-1]$. Ninguno de esos valores pertenece a la imagen $u=x^2\ge0$. Por tanto, el conjunto auxiliar admisible es vacío y la inequación original no tiene soluciones.

Declarar $x\in[-2,-1]$ sería confundir variables; buscar raíces cuadradas de valores negativos también ignoraría la imagen real de la sustitución.

### Una sustitución trasladada

Para $[(x-3)^2-1][(x-3)^2-9]>0$, tomamos $u=(x-3)^2\ge0$. La condición $(u-1)(u-9)>0$ da $u<1$ o $u>9$. Tras intersectar con $[0,\infty)$, queda $0\le u<1$ o $u>9$.

La primera rama equivale a $|x-3|<1$, es decir $2<x<4$. La segunda equivale a $|x-3|>3$, es decir $x<0$ o $x>6$. La solución completa es $(-\infty,0)\cup(2,4)\cup(6,\infty)$.

La reconstrucción es una unión porque basta pertenecer a una rama auxiliar. Dentro de cada rama pueden aparecer intersecciones al imponer dos cotas.

### Sustitución con exclusiones heredadas

Resolvamos $(x^4-1)/(x^2-1)\le0$. El dominio original excluye $x=\pm1$. Con $u=x^2$ necesitamos $u\ge0$ y $u\ne1$. La fracción auxiliar $(u^2-1)/(u-1)$ se simplifica a $u+1$ sobre ese dominio.

Como $u+1\ge1$, nunca es no positiva. La solución es vacía. La ausencia de soluciones no autoriza borrar las exclusiones de la explicación: ellas son las que hacen válida la cancelación.

### Prueba de estrés: perder una rama

Una resolución de $x^4-5x^2+4\le0$ obtiene $u\in[1,4]$ y responde $x\in[1,2]$. La primera ruptura aparece en la vuelta: tomar sólo la raíz principal omite los valores negativos cuyo cuadrado también está en $[1,4]$.

El valor $-3/2$ es un contraejemplo a esa respuesta incompleta. La reparación consiste en reconstruir la preimagen completa, $[-2,-1]\cup[1,2]$.

### Recuperación breve

Resuelva $x^4-10x^2+9<0$ y después resuélvala con la restricción adicional $x\ge0$.

**Respuesta razonada.** Con $u=x^2\ge0$, queda $(u-1)(u-9)<0$, de modo que $1<u<9$. La vuelta da $1<|x|<3$, cuya solución es $(-3,-1)\cup(1,3)$. Con $x\ge0$, se intersecta ese conjunto con $[0,\infty)$ y queda $(1,3)$.

### Qué debemos conservar de esta sección

Una sustitución conserva la relación entre dos variables y debe registrar la imagen de la auxiliar. Resolver en $u$ termina sólo al reconstruir su preimagen en el dominio original. La no inyectividad puede producir varias ramas, y una restricción sobre $x$ se conserva hasta la respuesta final.



### Reconstruir una preimagen no exige una función inversa

Si $u=(x-h)^2$, su imagen real es $[0,\infty)$. Una solución auxiliar $u\in[\alpha,\beta]$, con $0<\alpha\le\beta$, se reconstruye como $\sqrt\alpha\le|x-h|\le\sqrt\beta$: hay dos intervalos, no uno. **Control resuelto:** $u\in[-2,4]$ se intersecta primero con la imagen y queda $[0,4]$; su preimagen es $[h-2,h+2]$. No se toman raíces reales de los extremos negativos. Si el dominio original además exige $x>h$, se intersecta al final y queda $(h,h+2]$. Cada restricción participa en la misma reconstrucción. Escribir $\phi^{-1}(S)$ nombra un conjunto de preimágenes y no presupone que $\phi$ sea inyectiva.



## 22.13. Parámetros y familias de conjuntos solución {#apm-c22-s13}

En la familia $(x-a)(x-1)\le0$, el parámetro $a$ permanece fijo mientras varía $x$. Las dos fronteras son $a$ y $1$; su orden cambia al pasar de $a<1$ a $a>1$, y coinciden cuando $a=1$. La resolución debe describir una familia de conjuntos, no un intervalo escrito con extremos posiblemente invertidos.

### Identificar qué puede cambiar

Un valor del parámetro requiere un caso separado cuando cambia una condición relevante: el signo de un coeficiente, la coincidencia de fronteras, el dominio o la forma de la solución. Separar casos por costumbre puede aumentar cálculos sin mejorar la clasificación.

Para la familia inicial, el producto tiene coeficiente positivo y es no positivo entre las dos raíces. Así:

$$
S(a)=
\begin{cases}
[a,1],&a<1,\\
\{1\},&a=1,\\
[1,a],&a>1.
\end{cases}
$$

En el caso coincidente, la expresión es $(x-1)^2$ y sólo se admite su cero. La fórmula equivalente $[\min(a,1),\max(a,1)]$ resume la familia, pero la clasificación explica el mecanismo.

### Cambiar el signo de un coeficiente

Para $a(x-2)\ge0$, si $a>0$ dividimos conservando la dirección y obtenemos $[2,\infty)$. Si $a<0$, dividimos invirtiendo y obtenemos $(-\infty,2]$. Si $a=0$, la comparación $0\ge0$ es verdadera para todo real y $S(0)=\mathbb R$.

El caso $a=0$ no se obtiene tomando un valor en una fórmula con división por $a$. Se estudia en la expresión original.

### Una frontera que pasa a ser inadmisible

Estudie $(x-a)/(x-1)\ge0$. El dominio excluye siempre $1$, mientras que el cero de numerador es $a$ cuando $a\ne1$.

Si $a<1$, ambos signos coinciden para $x\le a$ y para $x>1$, con el cero $a$ incluido. Así, $S(a)=(-\infty,a]\cup(1,\infty)$. Si $a>1$, coinciden para $x<1$ y para $x\ge a$, y $S(a)=(-\infty,1)\cup[a,\infty)$.

Si $a=1$, el cociente vale $1$ en todo su dominio y $S(1)=\mathbb R\setminus\{1\}$. La coincidencia de fronteras elimina la región negativa, pero conserva el punto excluido.

### Parámetro como cota

La familia $(x-2)^2\le a$ tiene tres regímenes. Si $a<0$, la no negatividad del cuadrado da solución vacía. Si $a=0$, queda $\{2\}$. Si $a>0$, la raíz principal $\sqrt a$ existe y es positiva; comparar cuadrados de no negativos da $|x-2|\le\sqrt a$. Por tanto, $S(a)=[2-\sqrt a,2+\sqrt a]$.

Esta clasificación muestra vacío, punto e intervalo sin introducir análisis. Para cada parámetro, sólo usamos orden, cuadrado y raíz principal.

### El dominio también puede depender del parámetro

En $1/(x-a)>0$, el dominio es $D(a)=\mathbb R\setminus\{a\}$. El numerador es positivo, así que se requiere $x-a>0$ y $S(a)=(a,\infty)$.

No hace falta separar el signo de $a$: la diferencia $x-a$ tiene el mismo patrón a ambos lados de la frontera, sea ésta negativa, cero o positiva. Todos los valores del parámetro quedan cubiertos por la misma forma de respuesta.

### Prueba de estrés: un intervalo con extremos invertidos

Responder $[a,1]$ a $(x-a)(x-1)\le0$ para todo $a$ falla cuando $a=3$. La condición $(x-3)(x-1)\le0$ tiene solución $[1,3]$; el valor $2$ satisface el producto y no cabe en una escritura $[3,1]$ entendida mediante $3\le x\le1$.

Ordenar fronteras es una obligación de la resolución, incluso cuando son expresiones paramétricas.

### Recuperación breve

Clasifique $(x+1)^2<a$ para todo $a\in\mathbb R$.

**Respuesta razonada.** Si $a\le0$, el cuadrado no puede ser estrictamente menor que $a$, y la solución es vacía. Si $a>0$, la condición equivale a $|x+1|<\sqrt a$, de donde $S(a)=(-1-\sqrt a,-1+\sqrt a)$. El caso $a=0$ también es vacío porque la comparación es estricta.

### Qué debemos conservar de esta sección

El parámetro se fija antes de resolver. Los casos se organizan por cambios de signo, coincidencia de fronteras, dominio y degeneración. La respuesta debe ordenar sus extremos y tratar las excepciones en la expresión original, especialmente si un divisor se anula.



## 22.14. Transferencia: racionales, radicales y varias capas {#apm-c22-s14}

Resolver una inequación con varias capas exige coordinar los controles anteriores. En $\sqrt{x+1}\le x-1$, la raíz necesita $x\ge-1$, pero la comparación exige además que el miembro derecho sea no negativo. Ese segundo filtro cambia la región donde podemos elevar al cuadrado.

### Cuadrar con una raíz principal

Para reales $R\ge0$ y $B$, se tiene

$$
\sqrt R\le B
\Longleftrightarrow
(B\ge0\ \text{y}\ R\le B^2).
$$

Si la comparación original es verdadera, $B$ es al menos la raíz no negativa y por tanto $B\ge0$; cuadrar conserva el orden entre no negativos. Para la vuelta, $B\ge0$ y $R\le B^2$ permiten comparar las raíces principales y obtener $\sqrt R\le\sqrt{B^2}=B$.

Para la comparación estricta, $\sqrt R<B$ equivale a $B>0$ y $R<B^2$. La positividad estricta de $B$ es necesaria porque una raíz no negativa no puede ser menor que cero.

### Ejemplo con cota superior

En $\sqrt{x+1}\le x-1$, el dominio es $x\ge-1$ y la admisibilidad del miembro derecho exige $x\ge1$. Dentro de esa región, cuadrar es equivalente:

$$
x+1\le(x-1)^2
\Longleftrightarrow
x(x-3)\ge0.
$$

El producto da $x\le0$ o $x\ge3$. Al intersectar con $x\ge1$, sólo queda $S=[3,\infty)$. En $3$ ambos miembros valen $2$ y la igualdad es admisible.

La región $x\le0$ de la condición cuadrada no satisface el requisito $x-1\ge0$. Verificarla después no sustituye escribir esa condición como parte de la equivalencia.

### Cota inferior de una raíz

Para $\sqrt R\ge B$ con $R\ge0$, hay una diferencia: si $B\le0$, la condición es automáticamente verdadera. Si $B>0$, cuadrar es equivalente y exige $R\ge B^2$.

Resolvamos $\sqrt{x+1}>x-1$. El dominio es $x\ge-1$. Si $x<1$, el miembro derecho es negativo y la comparación es verdadera. Si $x=1$, también es verdadera porque $\sqrt2>0$. Si $x>1$, ambos miembros son positivos y cuadrar da $x+1>(x-1)^2$, equivalente a $x(x-3)<0$, de donde $1<x<3$ en ese caso. Reuniendo las ramas, $S=[-1,3)$.

Las soluciones de $\le$ y $>$ son complementarias dentro de $[-1,\infty)$, como exige la lógica de esas comparaciones. Este control independiente confirma los extremos.

### Una raíz en un cociente

Resolvamos $\sqrt{x+2}/(x-1)\le0$. El dominio es $x\ge-2$ y $x\ne1$. La raíz es no negativa, cero sólo en $-2$ y positiva para $x>-2$.

En $-2$ el cociente vale cero y se admite. Para $-2<x<1$, el numerador es positivo y el denominador negativo, de modo que el cociente es negativo. Para $x>1$ es positivo. Así, $S=[-2,1)$.

No necesitamos eliminar la raíz para resolver: su signo es suficiente. Cuadrar el cociente ocultaría el signo negativo que decide la comparación.

### Valor absoluto y racionalidad

Considere $|(x+1)/(x-2)|\le2$. El dominio excluye $2$ y la cota positiva permite escribir $-2\le(x+1)/(x-2)\le2$. La solución es la intersección de dos inequaciones racionales.

La cota superior equivale a $(5-x)/(x-2)\le0$, con solución $(-\infty,2)\cup[5,\infty)$. La inferior equivale a $3(x-1)/(x-2)\ge0$, con solución $(-\infty,1]\cup(2,\infty)$. La intersección es $S=(-\infty,1]\cup[5,\infty)$.

En $1$ el cociente vale $-2$ y en $5$ vale $2$, de modo que el valor absoluto vale $2$ en ambos extremos. El punto $2$ está excluido desde el dominio y tampoco aparece en la intersección.

### Prueba de estrés: cuadrar cantidades de signo libre

La comparación $-3<-2$ es verdadera; al cuadrar, $9<4$ es falsa. El cuadrado conserva el orden sobre los no negativos, lo invierte sobre los no positivos y no proporciona una regla única para cantidades de signo desconocido.

En una inequación radical, el signo de la raíz está controlado, pero el signo del otro miembro todavía debe examinarse.

### Recuperación breve

**a)** Resuelva $\sqrt{x+4}\le2$.

**b)** Resuelva $\sqrt{x+4}>-1$.

**c)** Resuelva $\sqrt{x+4}/(x-2)\ge0$.

**Respuesta razonada.** En **a)** el dominio es $x\ge-4$ y la cota $2$ es positiva. Cuadrar equivale a $x+4\le4$, de donde $S=[-4,0]$. En **b)** una raíz no negativa siempre supera $-1$; todo el dominio es solución, $S=[-4,\infty)$. En **c)** el dominio es $[-4,\infty)\setminus\{2\}$. El numerador se anula en $-4$, que se admite; es positivo en los demás valores. Se requiere denominador positivo para esos valores, y resulta $S=\{-4\}\cup(2,\infty)$.

### Qué debemos conservar de esta sección

Cada capa aporta una obligación distinta. La raíz fija dominio y no negatividad, el denominador fija exclusiones y signo, y el valor absoluto introduce ramas. Cuadrar sólo produce equivalencias tras controlar el signo de ambos miembros; en algunos problemas basta estudiar el signo de la expresión sin eliminar sus capas.



## 22.15. Laboratorio de errores y primera ruptura {#apm-c22-s15}

Una respuesta equivocada puede proceder de una sola transición inválida dentro de cálculos correctos. La auditoría de C21 se amplía: debemos examinar si una operación conserva el dominio, la orientación, las ramas y los extremos.

### Invertir sin un factor negativo

**Resolución defectuosa.** De $3x-2\le7$ se obtiene $3x\le9$ y después $x\ge3$.

La resta o suma inicial es válida. La primera ruptura es dividir por $3>0$ e invertir la relación. La reparación da $x\le3$ y $S=(-\infty,3]$. El valor $0$ pertenece a la solución original y refuta la semirrecta equivocada.

### Conservar la dirección con divisor negativo

**Resolución defectuosa.** De $-2x>6$ se concluye $x>-3$.

Dividir por $-2$ exige invertir y da $x<-3$. En la cadena defectuosa se cambia el conjunto solución en el único paso. Sustituir $x=-4$ confirma una solución que la respuesta perdió: $8>6$.

### Multiplicar por signo desconocido

**Resolución defectuosa.** De $1/(x-2)>0$ se obtiene $1>0$ multiplicando por $x-2$, y se declara $\mathbb R\setminus\{2\}$.

La multiplicación sin casos es la ruptura. En $x<2$, el factor es negativo y debe invertirse la relación. El cociente es positivo sólo para $x>2$, así que $S=(2,\infty)$. El punto $0$ está en el dominio, pero da $-1/2>0$, falso: es una falsa solución, no un valor indefinido.

### Cancelar y borrar el dominio

**Resolución defectuosa.** Se simplifica $(x^2-1)/(x-1)\ge0$ a $x+1\ge0$ y se declara $[-1,\infty)$.

La cancelación es válida para $x\ne1$. La ruptura aparece al formular la respuesta sin esa restricción. La reparación es $[-1,1)\cup(1,\infty)$. El punto $1$ no es una comparación falsa; la expresión original es indefinida.

### Dividir y perder un cero

**Resolución defectuosa.** Para $(x-2)^2(x+1)\le0$, se divide por $(x-2)^2$ y se responde $x\le-1$.

La división sólo es posible para $x\ne2$. Allí el divisor es positivo y la comparación equivalente da $x\le-1$. Falta examinar el caso $x=2$, donde el producto vale cero y satisface la inequación. El conjunto completo es $(-\infty,-1]\cup\{2\}$.

Verificar los puntos que permanecieron en la respuesta no descubre por sí solo la solución perdida. Se necesita recuperar el caso eliminado.

### Unir un sistema

**Resolución defectuosa.** Para $x\ge-1$ y $x<2$, se declara $[-1,\infty)\cup(-\infty,2)=\mathbb R$.

El cálculo de cada conjunto individual es correcto. La ruptura es sustituir la conjunción por unión. La intersección correcta es $[-1,2)$.

### Abrir mal el valor absoluto

**Resolución defectuosa.** Se escribe $|x|>2$ como $-2<x<2$.

La equivalencia inicial es falsa. La cota inferior de distancia exige $x<-2$ o $x>2$, con solución $(-\infty,-2)\cup(2,\infty)$. El punto $0$ cumple la doble desigualdad propuesta y falla la original.

### Cuadrar y borrar una condición de signo

**Resolución defectuosa.** De $\sqrt{x+1}\le x-1$ se pasa a $x+1\le(x-1)^2$ y se declara $(-\infty,0]\cup[3,\infty)$.

Además del dominio $x\ge-1$, la comparación original exige $x\ge1$. El paso cuadrado necesita esa condición para ser equivalente. La reparación conserva ambas restricciones y da $[3,\infty)$, como en [§22.14](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md#apm-c22-s14). El valor $0$ está en el dominio pero no satisface $1\le-1$.

### Incluir un extremo prohibido

**Resolución defectuosa.** Se responde $[-1,2]$ a $(x-2)/(x+1)\le0$.

La región interior tiene signo negativo y el cero $2$ se admite, pero $-1$ anula el denominador. La reparación es $(-1,2]$. Una relación no estricta permite ciertos ceros; no convierte un punto indefinido en una igualdad.

### Protocolo de reparación

Para auditar una resolución, primero recuperamos el dominio original y el conjunto que cada transición pretende conservar. Localizamos la primera operación que usa una hipótesis ausente o cambia un enlace lógico. Después clasificamos el efecto: valores inadmisibles reintegrados, falsas soluciones creadas, soluciones perdidas, extremos alterados o ramas omitidas.

La reparación regresa al último paso válido y añade el caso, restricción o inversión que faltaba. Una verificación puntual puede refutar una respuesta, pero una resolución completa debe demostrar que las regiones seleccionadas son todas y sólo las válidas.

### Recuperación breve

Una resolución de $(x+1)^2/(x-3)\ge0$ cancela el signo positivo del numerador y responde $(3,\infty)$. Determine la solución perdida y repare el argumento.

**Respuesta razonada.** El dominio excluye $3$. El numerador es positivo para $x\ne-1$ y cero en $-1$. Para los valores distintos de $-1$ se necesita $x>3$; en $-1$ el cociente vale cero y se admite. Por tanto, $S=\{-1\}\cup(3,\infty)$. Tratar el numerador como estrictamente positivo en todo el dominio omitió su cero.

### Qué debemos conservar de esta sección

El diagnóstico identifica la primera transición que altera el conjunto solución y la hipótesis que faltaba. El control final debe distinguir falsedad de falta de dominio y debe recuperar soluciones o ramas eliminadas durante la cadena. Cada reparación conserva la causa del error para que pueda reconocerse en otra expresión.



## 22.16. Síntesis: dominio → puntos críticos → signos → solución {#apm-c22-s16}

El objeto común de todos los métodos estudiados es un subconjunto del dominio. La resolución puede usar despeje, distancia, tablas, sustituciones o casos paramétricos, pero debe explicar por qué cada valor admitido satisface la condición y por qué no quedan otros.

### Elegir el método a partir de la estructura

Una condición lineal pide reunir la variable y clasificar el coeficiente. Un valor absoluto sugiere distancia y ramas. Un producto o cociente factorizado permite ordenar ceros y exclusiones y estudiar signos. Una expresión en $x^2$ puede admitir variable auxiliar y reconstrucción. Una raíz exige recuperar dominio y examinar el signo del otro miembro antes de cuadrar.

Estos reconocimientos son decisiones justificadas por la forma. Cuando aparecen varias estructuras, se decide cuál simplifica primero el problema conservando los controles restantes.

### Síntesis con dominio, signo y distancia

Resolvamos simultáneamente

$$
\begin{cases}
\dfrac{(x-1)^2(x+2)}{x-3}\le0,\\
|x|\le2.
\end{cases}
$$

El dominio común excluye $3$. La segunda condición equivale a $x\in[-2,2]$. Dentro de ese intervalo, $x-3<0$ y $x+2\ge0$. El factor $(x-1)^2$ es no negativo. El numerador es entonces no negativo y dividir por el denominador negativo da un cociente no positivo. Todos los valores de $[-2,2]$ satisfacen la primera condición.

Por tanto, la intersección es $S=[-2,2]$. En $-2$ y $1$ el numerador se anula; ambos valores pertenecen al dominio y la comparación admite igualdad. En $2$ el cociente es negativo y la condición de distancia admite ese extremo.

Una segunda ruta resuelve primero la racional en toda la recta. Los puntos críticos son $-2$, $1$ y $3$. Fuera de $1$, el cuadrado es positivo, de modo que el signo es el de $(x+2)/(x-3)$. Es negativo entre $-2$ y $3$ y positivo fuera; los ceros $-2$ y $1$ se admiten y $3$ se excluye. La solución racional es $[-2,3)$. Su intersección con $[-2,2]$ confirma $[-2,2]$.

La primera ruta usa una restricción del sistema para conocer signos y ahorrar una tabla; la segunda verifica el resultado mediante una resolución independiente de cada condición.

### Síntesis con reconstrucción

Considere $(x^4-5x^2+4)/(x^2-1)\ge0$. El dominio excluye $\pm1$. Con $u=x^2$ debemos conservar $u\ge0$ y $u\ne1$. La factorización $(u-1)(u-4)$ permite cancelar sobre ese dominio y obtener $u-4\ge0$, es decir $u\ge4$.

La vuelta exige $x^2\ge4$, equivalente a $|x|\ge2$. Se obtiene $S=(-\infty,-2]\cup[2,\infty)$. Las exclusiones $\pm1$ no pertenecen a esas regiones, pero permanecieron explícitas para justificar la cancelación. En $\pm2$ el numerador es cero con denominador $3$, así que se incluyen.

### Cómo saber que terminamos

En una resolución por intervalos, cada región seleccionada necesita una razón global de signo, no sólo un ejemplo favorable. Cada punto crítico se examina según su naturaleza: cero de la expresión, exclusión de dominio o frontera de otra condición. Una sustitución termina con sus preimágenes, y un sistema termina con la intersección.

La respuesta debe ser un conjunto legible y exacto. Se pueden reunir intervalos contiguos si el punto común pertenece a la solución; si está excluido, la separación se conserva. Una solución aislada puede escribirse como singleton y una ausencia de valores como $\varnothing$.

### Prueba de estrés de la estrategia

Para $\sqrt{(x-1)^2}/(x+2)>0$, el dominio excluye $-2$. Por C18, el numerador es $|x-1|$, no $x-1$. Es positivo salvo en $1$, donde se anula. Por eso el cociente es positivo exactamente cuando $x>-2$ y $x\ne1$: $S=(-2,1)\cup(1,\infty)$.

Reemplazar la raíz por $x-1$ cambiaría el signo del numerador para $x<1$ y daría una solución distinta. La selección de método comienza por leer correctamente la expresión.

### Recuperación breve

Resuelva el sistema $(x-1)(x+3)\ge0$ y $|x|\le4$, e indique por qué se incluyen los cuatro extremos de los intervalos resultantes.

**Respuesta razonada.** El producto es no negativo en $(-\infty,-3]\cup[1,\infty)$. La distancia exige $[-4,4]$. Su intersección es $[-4,-3]\cup[1,4]$. Los puntos $-3$ y $1$ anulan el producto y están en el dominio; $-4$ y $4$ satisfacen la cota de distancia con igualdad y el producto es positivo allí. Ambas condiciones son no estrictas.

### Qué debemos conservar del capítulo

Resolver una inequación exige conservar la información que decide la verdad de una relación de orden. El dominio identifica valores admisibles; los signos autorizan transformaciones; las fronteras organizan regiones; los enlaces lógicos indican cómo reunirlas. La verificación controla extremos, exclusiones y reconstrucciones, y el conjunto solución reúne el resultado de ese argumento.

En C23 volveremos a usar el orden para comparar valores de funciones exponenciales y logaritmos. Las transformaciones estarán gobernadas por su monotonía creciente o decreciente; las obligaciones de dominio y conjunto solución seguirán siendo las mismas.

## Ejercicios

Resuelva antes de consultar las soluciones. En los problemas sobre conjuntos solución, conserve el dominio, justifique las transformaciones y controle extremos y puntos excluidos.

### A. Lectura



#### Ejercicio 1

Escriba $\{x\in\mathbb R:-3<x\le2\}$ como intervalo y decida si $-3,0,2$ pertenecen.



#### Ejercicio 2

Traduzca $(-\infty,-2]\cup(5,\infty)$ a una condición con «o».



#### Ejercicio 3

En $D=\{-3,-2,-1,0,1,2,3\}$, determine dónde $x^2\le4$.



#### Ejercicio 4

Para $(x-4)/(x-4)\ge0$, distinga dominio y conjunto solución.



#### Ejercicio 5

Calcule $[-2,4)\cap(1,6]$ y $[-2,4)\cup(1,6]$.



#### Ejercicio 6

Si $a<b$, compare $a-7$ con $b-7$ y $-3a$ con $-3b$. Justifique.



#### Ejercicio 7

Explique qué regiones describe $|x-4|\le2$ y si $x=2,6$ se incluyen.



#### Ejercicio 8

En $(x+3)/(x-2)\le0$, identifique el cero admisible y el punto excluido sin resolver todavía.



#### Ejercicio 9

¿Es válida como intervalo real la escritura $[2,\infty]$? Corríjala.



#### Ejercicio 10

¿Qué cambia en las soluciones de $(x-3)^2<0$, $\le0$, $>0$ y $\ge0$?

### B. Fluidez



#### Ejercicio 11

Resuelva $7x-5<16$.



#### Ejercicio 12

Resuelva $4-5x\le19$.



#### Ejercicio 13

Resuelva $6x+1\ge2x-7$.



#### Ejercicio 14

Resuelva $5x+8<5x+3$.



#### Ejercicio 15

Resuelva $2x-9\le2x-4$.



#### Ejercicio 16

Resuelva $-5<3x+1\le10$.



#### Ejercicio 17

Resuelva $-4\le1-2x<7$.



#### Ejercicio 18

Resuelva simultáneamente $x+3>1$ y $4x\le12$.



#### Ejercicio 19

Resuelva $2x-1<-5$ o $x+2\ge6$.



#### Ejercicio 20

Resuelva $|2x+3|<7$.



#### Ejercicio 21

Resuelva $|x-5|\ge3$.



#### Ejercicio 22

Resuelva $x^2+2x-15\le0$.



#### Ejercicio 23

Resuelva $-x^2+6x-8>0$.



#### Ejercicio 24

Resuelva $(x+2)^2(x-4)<0$.



#### Ejercicio 25

Resuelva $(x-5)/(x+2)\ge0$.



#### Ejercicio 26

Resuelva $(x^2-9)/(x-3)<0$.

### C. Justificación



#### Ejercicio 27

Demuestre que sumar $c$ a ambos miembros conserva $a<b$ y explique la reversibilidad.



#### Ejercicio 28

Demuestre que $a<b$ y $c<0$ implican $ac>bc$ usando un multiplicador positivo.



#### Ejercicio 29

Justifique por qué $x(x-2)\ge0$ no puede dividirse por $x$ sin separar casos; resuelva.



#### Ejercicio 30

Pruebe $|u|\le c\Longleftrightarrow-c\le u\le c$ para $c>0$.



#### Ejercicio 31

Justifique que el signo de $(x-1)(x-4)$ es constante en cada intervalo determinado por $1,4$.



#### Ejercicio 32

Explique por qué atravesar el cero de $(x-2)^4$ no cambia su signo.



#### Ejercicio 33

Demuestre en el dominio $Q(x)\ne0$ que $P(x)/Q(x)\le0$ equivale a $P(x)Q(x)\le0$.



#### Ejercicio 34

Explique por qué un cero del numerador puede admitirse en una racional no estricta y uno del denominador no.



#### Ejercicio 35

Demuestre que para $r,s\ge0$, $r\le s$ equivale a $r^2\le s^2$.



#### Ejercicio 36

Formule y pruebe la condición completa equivalente a $\sqrt{R(x)}\le B(x)$.



#### Ejercicio 37

Justifique por qué sumar dos inequaciones de un sistema puede dar sólo una condición necesaria. Construya un caso.



#### Ejercicio 38

Pruebe que la solución tras $u=\phi(x)$ es la preimagen del conjunto auxiliar, aun si $\phi$ no es inyectiva.

### D. Diagnóstico



#### Ejercicio 39

Diagnostique y repare: $-4x\le8\Longleftrightarrow x\le-2$.



#### Ejercicio 40

Diagnostique y repare: $2x+1<7\Longleftrightarrow x>3$.



#### Ejercicio 41

Diagnostique y repare: $1/(x+3)>0\Longleftrightarrow1>0$, por lo que todos los reales salvo $-3$ son solución.



#### Ejercicio 42

Diagnostique y repare: $(x^2-4)/(x-2)\ge0\Longleftrightarrow x+2\ge0$, con solución $[-2,\infty)$.



#### Ejercicio 43

Diagnostique y repare: $(x-4)^2(x+2)\le0$ se divide por el cuadrado y da $x\le-2$.



#### Ejercicio 44

Diagnostique y repare: $|x-1|>2\Longleftrightarrow-2<x-1<2$.



#### Ejercicio 45

Diagnostique y repare un sistema $x\ge0$, $x<3$ cuya respuesta es $[0,\infty)\cup(-\infty,3)$.



#### Ejercicio 46

Diagnostique y repare: $(x-2)/(x+1)\le0$ tiene solución $[-1,2]$.



#### Ejercicio 47

Diagnostique y repare: $\sqrt{x+2}\le x$ se cuadra y da $x^2-x-2\ge0$, con respuesta $(-\infty,-1]\cup[2,\infty)$.



#### Ejercicio 48

Diagnostique y repare: $x^4-13x^2+36\le0$, con $u=x^2$, da $u\in[4,9]$ y se responde $x\in[2,3]$.



#### Ejercicio 49

Diagnostique y repare la afirmación «$(x+1)^2>0$ para todo real».



#### Ejercicio 50

Diagnostique y repare: $ax<1$ siempre tiene solución $x<1/a$.

### E. Estrategia



#### Ejercicio 51

Resuelva $(x-2)^2-25\ge0$ y compare expandir con factorizar directamente.



#### Ejercicio 52

Resuelva $x^2-6x+11<0$ eligiendo una forma que permita decidir sin raíces.



#### Ejercicio 53

Resuelva $-(x+2)(x-5)>0$ por dos rutas y compare.



#### Ejercicio 54

Resuelva $1/(x-3)\le1/(x+3)$ mediante una diferencia.



#### Ejercicio 55

Resuelva $(x-4)/(x+2)\le1$ por signo y por casos del denominador.



#### Ejercicio 56

Resuelva $(x^2+4)(x-1)\ge0$ y explique qué factor puede estudiarse globalmente.



#### Ejercicio 57

Resuelva $(x-3)^2(x+2)\ge0$ y explique si conviene dividir por el cuadrado.



#### Ejercicio 58

Resuelva $x^4-8x^2+7>0$ indicando el método elegido y reconstrucción.



#### Ejercicio 59

Resuelva $\sqrt{x+5}/(x-2)<0$ evitando un cuadrado innecesario.



#### Ejercicio 60

Resuelva $(x-1)(x-4)\le0$ con $x\ge3$, comparando resolver primero todo el producto con usar el dominio.

### F. Transferencia



#### Ejercicio 61

Clasifique $(x-a)(x-2)<0$ para todo parámetro real $a$.



#### Ejercicio 62

Clasifique $(a-1)x\le2$ para todo $a\in\mathbb R$.



#### Ejercicio 63

Clasifique $(x+2)^2\ge a$ para todo $a\in\mathbb R$.



#### Ejercicio 64

Resuelva $x^4-20x^2+64\le0$.



#### Ejercicio 65

Resuelva $[(x+1)^2-4][(x+1)^2-9]<0$.



#### Ejercicio 66

Resuelva $(x^4-16)/(x^2-4)>0$.



#### Ejercicio 67

Resuelva $\sqrt{x+6}\le x$.



#### Ejercicio 68

Resuelva $\sqrt{x+6}>x$.



#### Ejercicio 69

Resuelva $|\sqrt{x+1}-2|\le1$.



#### Ejercicio 70

Resuelva el sistema $(x+4)(x-1)\ge0$, $|x|\le5$.



#### Ejercicio 71

Resuelva simultáneamente $(x-2)/(x+3)\le0$ y $x>-1$.



#### Ejercicio 72

Resuelva $|(x-1)/(x+1)|\ge2$.

### G. Síntesis



#### Ejercicio 73

Resuelva $(x+4)(x+1)^2(x-2)^3(x-5)^2\le0$. Justifique los ceros que cambian el signo.



#### Ejercicio 74

Resuelva $(x^2-9)(x-1)/[(x-3)(x+2)]\ge0$, distinguiendo ceros y punto cancelado.



#### Ejercicio 75

Una resolución de $(x+1)/(x-2)>1$ multiplica por $x-2$ y concluye $x+1>x-2$, de modo que todos los valores del dominio servirían. Localice la ruptura y resuelva por dos rutas.



#### Ejercicio 76

Clasifique $a(x-1)^2\le a-1$ para todo $a\in\mathbb R$.



#### Ejercicio 77

Resuelva $|(x-2)/(x+2)|<1$ y después intersecte la solución con $(x-1)(x-4)\ge0$.



#### Ejercicio 78

Resuelva el sistema $(x-1)/(x+2)\ge0$, $(x-3)(x+4)\le0$, $|x-1|\le4$.



#### Ejercicio 79

Resuelva $(x^4-10x^2+9)/(x^2-4)\le0$ reconstruyendo todas las preimágenes.



#### Ejercicio 80

Resuelva simultáneamente $\sqrt{x+2}/(x-1)\le0$ y $|(x-2)/(x+2)|\ge1$. Dé una verificación independiente de regiones y extremos.

### H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Diseñar un intervalo cerrado

Dados $a<b$, construya una inequación polinómica cuyo conjunto solución real sea exactamente $[a,b]$ y justifique las regiones.



#### Ejercicio 082. Diseñar un intervalo abierto con un hueco

Dados $a<c<b$, construya una inequación racional con conjunto solución $(a,c)\cup(c,b)$.



#### Ejercicio 083. Diseñar un rayo y un punto aislado

Dados $a<b$, construya una inequación polinómica cuya solución sea $(-\infty,a]\cup\{b\}$.



#### Ejercicio 084. Diseñar dos intervalos de signos

Dados $a<b<c$, construya una inequación de producto que tenga solución $(a,b)\cup(c,\infty)$.



#### Ejercicio 085. Comparar dos dominios después de cancelar

Compare los conjuntos solución de $(x-a)^2/(x-a)^2\ge1$ y $(x-b)^2/(x-b)^2\ge1$. Determine cuándo las ecuaciones reducidas tienen el mismo conjunto y cuándo las originales son equivalentes.



#### Ejercicio 086. Un punto que la forma reducida admitiría

Para reales $a,b$, resuelva $(x-a)(x-b)/(x-a)\le0$ y clasifique la solución según la posición relativa de $a,b$.



#### Ejercicio 087. Un signo global antes y después de cancelar

Para $a<b$, resuelva $(x-a)/(a-x)\,(x-b)\ge0$.



#### Ejercicio 088. Un cuadrado cancelado dentro de una racional

Resuelva $(x-a)^2(x-b)/[(x-a)^2(x-c)]>0$ para $b<c$, conservando cualquier real $a$.



#### Ejercicio 089. Dos ceros que se fusionan

Clasifique la solución de $(x-t)(x+t)\le0$ para todo real $t$.



#### Ejercicio 090. Un cero que se convierte en hueco

Clasifique $(x-t)/(x-1)\ge0$ según $t<1$, $t=1$ y $t>1$.



#### Ejercicio 091. Un cuadrado y un polo paramétricos

Para todo real $t$, resuelva $(x-t)^2/(x-1)\le0$.



#### Ejercicio 092. Una región que colapsa al coincidir dos parámetros

Resuelva $(x-t)(x-1)\ge0$ para cada $t$, con atención al caso $t=1$.



#### Ejercicio 093. Dos ramas con una traslación

Resuelva $[(x-h)^2-A][(x-h)^2-B]\le0$ para $0<A<B$.



#### Ejercicio 094. Intersectar con una imagen que excluye ceros

Resuelva $(|x-h|+1-2)(|x-h|+1-4)<0$.



#### Ejercicio 095. Una sustitución recíproca y un hueco permanente

Resuelva $0<1/(x-h)^2\le4$ sobre los reales.



#### Ejercicio 096. Reconstruir después de una imagen acotada

Resuelva $\dfrac{(x-h)^2}{1+(x-h)^2}\le c$ para todo real $c$.

## Soluciones desarrolladas

### A. Lectura



#### Solución 1

La cota izquierda es estricta y la derecha admite igualdad: $S=(-3,2]$. El valor $-3$ queda excluido, $0$ está entre las fronteras y $2$ se incluye.



#### Solución 2

La primera semirrecta exige $x\le-2$; la segunda exige $x>5$. La unión permite satisfacer al menos una: $x\le-2$ o $x>5$.



#### Solución 3

Los cuadrados son $9,4,1,0,1,4,9$. La comparación admite los cinco valores centrales, así que $S=\{-2,-1,0,1,2\}$. El dominio finito permite esta comprobación exhaustiva.



#### Solución 4

El dominio es $D=\mathbb R\setminus\{4\}$. Allí la fracción vale $1$ y $1\ge0$ es verdadera, de modo que $S=D$. En $4$ la expresión es indefinida, no falsa.



#### Solución 5

La región común exige $x>1$ y $x<4$: la intersección es $(1,4)$. Los intervalos se superponen y reúnen todos los valores desde $-2$ hasta $6$, incluidos ambos: la unión es $[-2,6]$.



#### Solución 6

Sumar $-7$ conserva el orden, por lo que $a-7<b-7$. Multiplicar por $-3<0$ lo invierte y da $-3a>-3b$. Ambas operaciones son reversibles porque el multiplicador es no nulo.



#### Solución 7

La distancia a $4$ no excede $2$, equivalente a $2\le x\le6$. La solución es $[2,6]$; los extremos tienen distancia exactamente $2$ y se incluyen por la comparación no estricta.



#### Solución 8

El numerador se anula en $-3$ y el denominador allí vale $-5$, de modo que el cociente vale cero y se admite. El punto $2$ anula el denominador y queda excluido desde el dominio, independientemente del signo $\le$.



#### Solución 9

El símbolo $\infty$ no es un real que pueda incluirse. La semirrecta de reales mayores o iguales que $2$ se escribe $[2,\infty)$. El corchete izquierdo incluye $2$ y el paréntesis derecho expresa extensión sin extremo real.



#### Solución 10

El cuadrado es no negativo y se anula sólo en $3$. Por tanto, los cuatro conjuntos son, en ese orden, $\varnothing$, $\{3\}$, $\mathbb R\setminus\{3\}$ y $\mathbb R$.

### B. Fluidez



#### Solución 11

Sumar $5$ da $7x<21$. Dividir por $7>0$ conserva la dirección y da $x<3$. Así, $S=(-\infty,3)$; en $3$ hay igualdad y la condición estricta lo excluye.



#### Solución 12

Restar $4$ da $-5x\le15$. Al dividir por $-5<0$ se invierte la relación: $x\ge-3$. Por tanto, $S=[-3,\infty)$; en $-3$ ambos miembros valen $19$.



#### Solución 13

Restar $2x$ y $1$ conserva la relación y deja $4x\ge-8$. Dividir por $4>0$ da $x\ge-2$, de modo que $S=[-2,\infty)$.



#### Solución 14

Restar $5x$ deja $8<3$, falsa para todos los valores de $x$. No existe un coeficiente no nulo por el que dividir. El conjunto solución es $\varnothing$.



#### Solución 15

Restar $2x$ deja $-9\le-4$, verdadera para todo real. Por tanto, $S=\mathbb R$. La variable desaparece y el problema se decide por una comparación numérica.



#### Solución 16

Restar $1$ en los tres miembros da $-6<3x\le9$. Dividir por $3>0$ conserva ambas direcciones: $-2<x\le3$. Así, $S=(-2,3]$.



#### Solución 17

Restar $1$ da $-5\le-2x<6$. Dividir por $-2$ invierte ambas comparaciones: $5/2\ge x>-3$. Reordenando, $S=(-3,5/2]$.



#### Solución 18

La primera condición equivale a $x>-2$ y la segunda a $x\le3$, porque se divide por $4>0$. El sistema exige la intersección: $S=(-2,3]$.



#### Solución 19

Las ramas son $x<-2$ y $x\ge4$. Al ser alternativas, reunimos sus conjuntos mediante unión: $S=(-\infty,-2)\cup[4,\infty)$.



#### Solución 20

La cota positiva permite $-7<2x+3<7$. Restar $3$ y dividir por $2>0$ da $-5<x<2$, así que $S=(-5,2)$. Los dos extremos producen valor absoluto $7$ y se excluyen.



#### Solución 21

Una distancia de al menos $3$ exige $x-5\le-3$ o $x-5\ge3$. Resulta $x\le2$ o $x\ge8$, con $S=(-\infty,2]\cup[8,\infty)$.



#### Solución 22

Factorizamos $(x+5)(x-3)$. Los factores tienen signos opuestos entre $-5$ y $3$, y el producto se anula en ambos extremos. Para $\le0$, $S=[-5,3]$.



#### Solución 23

La expresión es $-(x-2)(x-4)$. Dividir por $-1$ invierte y exige $(x-2)(x-4)<0$, verdadero entre las raíces. Así, $S=(2,4)$.



#### Solución 24

Fuera de $-2$, el cuadrado es positivo, así que se necesita $x-4<0$. La condición estricta excluye ambos ceros. Por tanto, $S=(-\infty,-2)\cup(-2,4)$.



#### Solución 25

El dominio excluye $-2$. Numerador y denominador tienen signos iguales para $x<-2$ y $x>5$; el cero $5$ se admite. Así, $S=(-\infty,-2)\cup[5,\infty)$.



#### Solución 26

El dominio excluye $3$. Factorizar y cancelar sobre él deja $x+3<0$, es decir $x<-3$. Esa región no contiene el punto excluido, por lo que $S=(-\infty,-3)$.

### C. Justificación



#### Solución 27

Si $a<b$, entonces $b-a>0$ y $(b+c)-(a+c)=b-a>0$, de donde $a+c<b+c$. Restar $c$ recupera el orden inicial. Así se prueban ambas direcciones de la equivalencia para todo real $c$.



#### Solución 28

Como $-c>0$, la propiedad para multiplicadores positivos da $-ac<-bc$. Sumamos $ac+bc$ a ambos miembros y obtenemos $bc<ac$, esto es $ac>bc$. Sólo se usaron multiplicación por positivo y compatibilidad aditiva; así se evita suponer la regla para negativos que se quiere demostrar.



#### Solución 29

Si $x>0$, dividir conserva y exige $x\ge2$. Si $x<0$, dividir invierte y exige $x\le2$, cumplido por todos los negativos. Si $x=0$, el producto vale cero y se admite. Reuniendo, $S=(-\infty,0]\cup[2,\infty)$.



#### Solución 30

Si $u\ge0$, $|u|=u$ y la comparación equivale a $u\le c$, mientras $u\ge-c$ ya se cumple. Si $u<0$, $|u|=-u$ y equivale a $u\ge-c$, mientras $u\le c$ ya se cumple. En cada caso el razonamiento es reversible, así que las dos cotas son necesarias y suficientes.



#### Solución 31

En $x<1$, ambos factores son negativos; en $1<x<4$, el primero es positivo y el segundo negativo; en $x>4$, ambos son positivos. Estas condiciones valen para todos los puntos de cada intervalo, y las reglas del producto fijan signos $+,-,+$. No se infiere constancia a partir de un único valor de prueba.



#### Solución 32

Para $x\ne2$, $(x-2)^4=[(x-2)^2]^2>0$. La cuarta potencia es positiva a ambos lados y sólo vale cero en $2$. El exponente par elimina el signo negativo de la base.



#### Solución 33

En ese dominio, $Q(x)^2>0$. Multiplicar por ese cuadrado conserva la comparación y transforma $Q^2(P/Q)$ en $PQ$. Dividir por el mismo cuadrado recupera la fracción y prueba la vuelta. La exclusión $Q\ne0$ permanece en ambos problemas.



#### Solución 34

Si $P(c)=0$ y $Q(c)\ne0$, el cociente vale $0$ y satisface tanto $\le0$ como $\ge0$. Si $Q(c)=0$, no hay cociente real definido, aun si también $P(c)=0$. La segunda exclusión procede del dominio y no de la comparación.



#### Solución 35

Si $r\le s$, $(s-r)(s+r)\ge0$ y por tanto $s^2-r^2\ge0$. Si $r>s$, ambos factores de $(r-s)(r+s)$ son positivos, de modo que $r^2>s^2$, contradiciendo la condición cuadrada. Esto prueba la vuelta y señala dónde se usa la no negatividad.



#### Solución 36

En el dominio $R(x)\ge0$, la equivalencia completa exige $B(x)\ge0$ y $R(x)\le B(x)^2$. La original fuerza $B$ no negativo; cuadrar entre no negativos da la segunda condición. Para la vuelta, comparar raíces da $\sqrt R\le\sqrt{B^2}=B$, donde se usa $B\ge0$.



#### Solución 37

Sumar comparaciones compatibles produce una consecuencia válida, pero puede borrar información independiente. El sistema $x\ge1$, $-x\ge-1$ sólo admite $x=1$; al sumar queda $0\ge0$, verdadera para todos los reales. Por tanto, esa consecuencia no es suficiente para recuperar el sistema.



#### Solución 38

Un valor $x\in D$ satisface la condición original exactamente cuando $u=\phi(x)$ pertenece al conjunto auxiliar válido $S_u$. Por definición de preimagen, esto equivale a $x\in\phi^{-1}(S_u)$. La prueba no requiere valores únicos de $x$ para cada $u$; todas las preimágenes válidas se conservan.

### D. Diagnóstico



#### Solución 39

La ruptura está en dividir por $-4$ sin invertir. El paso correcto da $x\ge-2$ y $S=[-2,\infty)$. La frontera se incluye porque produce igualdad.



#### Solución 40

Restar $1$ y dividir por $2>0$ conserva la orientación: $x<3$. La primera ruptura es la inversión injustificada, y la respuesta correcta es $(-\infty,3)$.



#### Solución 41

Se multiplicó por $x+3$ sin controlar su signo. El numerador positivo exige denominador positivo, así que $x>-3$. La solución es $(-3,\infty)$; en $x<-3$ habría que invertir la relación al multiplicar.



#### Solución 42

La simplificación es válida sólo para $x\ne2$. La respuesta borró ese dominio, reintegrando un valor indefinido. Se conserva $x\ge-2$ y se retira $2$: $S=[-2,2)\cup(2,\infty)$.



#### Solución 43

El divisor se anula en $4$, que debe estudiarse aparte. Fuera de $4$ es positivo y da $x\le-2$; en $4$ el producto vale cero. La solución completa es $(-\infty,-2]\cup\{4\}$.



#### Solución 44

La doble cota representa $|x-1|<2$, no $>2$. La distancia mayor exige $x-1<-2$ o $x-1>2$, dando $S=(-\infty,-1)\cup(3,\infty)$.



#### Solución 45

Un sistema exige simultaneidad y por tanto intersección, no unión. El conjunto correcto es $[0,3)$. La unión defectuosa sería toda la recta e incluiría valores que incumplen una de las condiciones.



#### Solución 46

El extremo $-1$ anula el denominador y no pertenece al dominio. La región interior tiene signo negativo y $2$ es cero admisible. La solución es $(-1,2]$.



#### Solución 47

La raíz exige $x\ge-2$ y la comparación original exige $x\ge0$. Cuadrar es equivalente sólo con esa condición de signo. El producto $(x-2)(x+1)\ge0$ se intersecta con $[0,\infty)$, dando $S=[2,\infty)$.



#### Solución 48

La vuelta perdió las preimágenes negativas. La condición $4\le x^2\le9$ equivale a $2\le|x|\le3$, de modo que $S=[-3,-2]\cup[2,3]$. Los cuatro extremos se admiten por la relación no estricta.



#### Solución 49

El cuadrado es positivo salvo donde su base se anula. En $x=-1$ vale cero, así que la inequación tiene solución $\mathbb R\setminus\{-1\}$. La propiedad general disponible era no negatividad, no positividad estricta.



#### Solución 50

La división sólo es posible si $a\ne0$ y su orientación depende del signo. Si $a>0$, $S=(-\infty,1/a)$; si $a<0$, $S=(1/a,\infty)$; si $a=0$, la comparación $0<1$ es verdadera y $S=\mathbb R$.

### E. Estrategia



#### Solución 51

La diferencia de cuadrados da $(x-7)(x+3)\ge0$. El producto es no negativo fuera de las raíces: $S=(-\infty,-3]\cup[7,\infty)$. Expandir da $x^2-4x-21$, correcto pero obliga a recuperar los mismos factores; la forma inicial ya ofrece la diferencia de cuadrados.



#### Solución 52

Completar cuadrados da $(x-3)^2+2$. Es al menos $2>0$ para todo real, de modo que $S=\varnothing$. Buscar raíces sería innecesario porque la cota global resuelve la comparación.



#### Solución 53

Multiplicar por $-1$ invierte y deja $(x+2)(x-5)<0$, verdadero entre raíces: $S=(-2,5)$. Una tabla que conserve el signo negativo cambia los signos exteriores a negativos y el interior a positivo, dando el mismo conjunto. Normalizar evita repetir esa inversión por fila.



#### Solución 54

El dominio excluye $\pm3$. La diferencia es $6/[(x-3)(x+3)]$. Como el numerador es positivo, ser no positiva exige denominador negativo, que ocurre entre las raíces. No hay ceros del numerador: $S=(-3,3)$.



#### Solución 55

Restar $1$ da $-6/(x+2)\le0$ con $x\ne-2$, por lo que se necesita $x>-2$. Por casos: para $x>-2$, multiplicar conserva y deja $x-4\le x+2$, verdadera; para $x<-2$, invierte y deja $x-4\ge x+2$, falsa. Ambas rutas dan $(-2,\infty)$.



#### Solución 56

El factor $x^2+4$ es estrictamente positivo para todo real. Dividir por él conserva la relación y exige $x-1\ge0$. Así, $S=[1,\infty)$. No introduce ceros ni fronteras adicionales.



#### Solución 57

Fuera de $3$, el cuadrado es positivo y se necesita $x\ge-2$. En $3$ el producto vale cero y se admite; ese punto ya está en la semirrecta. Por tanto, $S=[-2,\infty)$. Dividir sólo es válido tras separar $3$, aunque aquí no cambia la unión final.



#### Solución 58

Con $u=x^2\ge0$, $(u-1)(u-7)>0$ exige $u<1$ o $u>7$. La vuelta da $|x|<1$ o $|x|>\sqrt7$. Así, $S=(-\infty,-\sqrt7)\cup(-1,1)\cup(\sqrt7,\infty)$.



#### Solución 59

El dominio es $x\ge-5$, $x\ne2$. El numerador es cero en $-5$ y positivo para $x>-5$. La comparación estricta requiere numerador positivo y denominador negativo: $S=(-5,2)$. Cuadrar borraría el signo que decide el cociente.



#### Solución 60

La solución del producto en toda la recta es $[1,4]$, cuya intersección con $[3,\infty)$ es $[3,4]$. Dentro del dominio, $x-1>0$, así que dividir por él conserva y exige $x-4\le0$, llegando directamente al mismo conjunto.

### F. Transferencia



#### Solución 61

Para $a<2$, el producto es negativo entre las raíces y $S(a)=(a,2)$. Para $a>2$, $S(a)=(2,a)$. Para $a=2$, queda $(x-2)^2<0$ y la solución es vacía. Los extremos siempre se excluyen por la comparación estricta.



#### Solución 62

Si $a>1$, el coeficiente es positivo y $S(a)=(-\infty,2/(a-1)]$. Si $a<1$, es negativo y $S(a)=[2/(a-1),\infty)$. Si $a=1$, queda $0\le2$ y $S(a)=\mathbb R$.



#### Solución 63

Si $a\le0$, todo cuadrado es mayor o igual que $a$, así que $S(a)=\mathbb R$. Si $a>0$, la condición equivale a $|x+2|\ge\sqrt a$, dando $S(a)=(-\infty,-2-\sqrt a]\cup[-2+\sqrt a,\infty)$.



#### Solución 64

Con $u=x^2\ge0$, $(u-4)(u-16)\le0$ da $4\le u\le16$. Reconstruir exige $2\le|x|\le4$. Así, $S=[-4,-2]\cup[2,4]$ y los cuatro extremos anulan la expresión.



#### Solución 65

Con $u=(x+1)^2\ge0$, la condición exige $4<u<9$, es decir $2<|x+1|<3$. La rama negativa da $-3<x+1<-2$, y la positiva $2<x+1<3$. Por tanto, $S=(-4,-3)\cup(1,2)$.



#### Solución 66

El dominio excluye $\pm2$. Con $u=x^2\ge0$, $u\ne4$, factorizar permite cancelar y deja $u+4>0$, siempre verdadera. Al reconstruir se admiten todos los reales salvo las exclusiones originales: $S=\mathbb R\setminus\{-2,2\}$.



#### Solución 67

El dominio exige $x\ge-6$ y la comparación exige $x\ge0$. Allí cuadrar es equivalente: $x+6\le x^2$, es decir $(x-3)(x+2)\ge0$. Sus exteriores se intersectan con $[0,\infty)$, dando $S=[3,\infty)$. En $3$ hay igualdad.



#### Solución 68

En el dominio $x\ge-6$, todos los valores $x<0$ satisfacen la comparación porque la raíz es no negativa. En $x=0$ también se cumple. Para $x>0$, cuadrar equivale a $(x-3)(x+2)<0$, dando $0<x<3$ en ese caso. La unión es $S=[-6,3)$.



#### Solución 69

El dominio es $x\ge-1$. La cota de distancia equivale a $1\le\sqrt{x+1}\le3$. Los tres miembros son no negativos, así que cuadrar ambas comparaciones da $1\le x+1\le9$. Por tanto, $S=[0,8]$.



#### Solución 70

El producto selecciona $(-\infty,-4]\cup[1,\infty)$. La distancia selecciona $[-5,5]$. La intersección es $[-5,-4]\cup[1,5]$, con todos los extremos incluidos porque ambas condiciones admiten igualdad.



#### Solución 71

El dominio excluye $-3$. La racional tiene signo negativo entre $-3$ y $2$, e incluye el cero $2$: su solución es $(-3,2]$. Intersectar con $(-1,\infty)$ da $S=(-1,2]$.



#### Solución 72

El dominio excluye $-1$. Las dos ramas son $(x-1)/(x+1)\le-2$ o $\ge2$. La primera equivale a $(3x+1)/(x+1)\le0$, con solución $(-1,-1/3]$. La segunda equivale a $(-x-3)/(x+1)\ge0$, con solución $[-3,-1)$. La unión es $[-3,-1)\cup(-1,-1/3]$.

### G. Síntesis



#### Solución 73

El dominio es toda la recta. Fuera de $-1$ y $5$, los factores cuadrados son positivos, y el signo es el de $(x+4)(x-2)$ porque la potencia cúbica conserva el signo de $x-2$. Es negativo entre $-4$ y $2$ y positivo fuera. Los ceros $-4$ y $2$ cambian signo; $-1$ y $5$ no. La relación admite todos los ceros: $-1$ ya queda dentro del intervalo, mientras $5$ aporta un punto aislado. Así, $S=[-4,2]\cup\{5\}$.



#### Solución 74

El dominio excluye $3$ y $-2$. Cancelar $x-3$ deja $(x+3)(x-1)/(x+2)$ sobre ese dominio. Los puntos ordenados son $-3,-2,1$, más el agujero $3$. Los signos del cociente son negativos en $(-\infty,-3)$, positivos en $(-3,-2)$, negativos en $(-2,1)$ y positivos en $(1,\infty)$. Se admiten los ceros $-3$ y $1$, y se retira $3$ de la última región. Por tanto, $S=[-3,-2)\cup[1,3)\cup(3,\infty)$.



#### Solución 75

La ruptura es multiplicar por signo desconocido. Restar $1$ deja $3/(x-2)>0$ con $x\ne2$, así que $S=(2,\infty)$. Por casos, para $x>2$ se conserva y queda $1>-2$, verdadera; para $x<2$ se invierte y queda $1<-2$, falsa. La comparación estricta excluye el punto indefinido y no tiene ceros del numerador. Ambas rutas prueban que se admiten todos y sólo los valores mayores que $2$.



#### Solución 76

Si $a=0$, queda $0\le-1$ y no hay soluciones. Si $0<a<1$, dividir por positivo da un cuadrado menor o igual que $1-1/a<0$, imposible. Si $a=1$, queda $(x-1)^2\le0$ y $S=\{1\}$. Si $a>1$, la cota $1-1/a$ es positiva y $S=[1-\sqrt{1-1/a},1+\sqrt{1-1/a}]$. Si $a<0$, dividir invierte y exige $(x-1)^2\ge1-1/a$, con cota positiva: $S=(-\infty,1-\sqrt{1-1/a}]\cup[1+\sqrt{1-1/a},\infty)$. El signo del coeficiente y el de la cota explican todos los valores críticos.



#### Solución 77

El dominio excluye $-2$. Como ambos valores absolutos son no negativos y $|x+2|>0$, la primera condición equivale a $|x-2|<|x+2|$. Cuadrar conserva el orden: $(x-2)^2<(x+2)^2$, que se reduce a $x>0$. Esa región respeta la exclusión. El producto de la segunda condición da $(-\infty,1]\cup[4,\infty)$. La intersección es $S=(0,1]\cup[4,\infty)$. En $0$ los valores absolutos son iguales y se excluye; $1$ y $4$ admiten igualdad en el producto.



#### Solución 78

El dominio excluye $-2$. La racional da $(-\infty,-2)\cup[1,\infty)$; la cuadrática da $[-4,3]$; la distancia da $[-3,5]$. Las dos últimas condiciones se intersectan en $[-3,3]$. Intersectar con la racional produce $S=[-3,-2)\cup[1,3]$. El extremo $-3$ satisface distancia con igualdad y la racional es positiva allí; $1$ anula la racional; $3$ anula la cuadrática. El punto $-2$ se mantiene excluido por dominio.



#### Solución 79

El dominio excluye $\pm2$. Con $u=x^2\ge0$, $u\ne4$, la condición es $(u-1)(u-9)/(u-4)\le0$. Sus signos son negativos para $u<1$, positivos para $1<u<4$, negativos para $4<u<9$ y positivos para $u>9$. En la imagen válida queda $S_u=[0,1]\cup(4,9]$. La primera preimagen es $[-1,1]$; la segunda exige $2<|x|\le3$ y da $[-3,-2)\cup(2,3]$. Por tanto, $S=[-3,-2)\cup[-1,1]\cup(2,3]$. Los ceros $\pm1,\pm3$ se incluyen y los polos $\pm2$ no.



#### Solución 80

El dominio común es $x\ge-2$ con $x\ne-2,1$, es decir $(-2,\infty)\setminus\{1\}$. En ese dominio la raíz es positiva, por lo que la primera condición exige denominador negativo: $-2<x<1$. Para la segunda, multiplicar por $|x+2|>0$ da $|x-2|\ge|x+2|$. Cuadrar entre no negativos equivale a $(x-2)^2\ge(x+2)^2$, es decir $x\le0$. La intersección es $S=(-2,0]$. Independientemente, para $-2<x\le0$ el primer denominador es negativo y la raíz positiva, mientras $2-x\ge x+2>0$, confirmando la segunda comparación. El punto $0$ da igualdad en los valores absolutos y se incluye; $-2$ es indefinido en la segunda condición. Los valores con $0<x<1$ fallan la segunda; los mayores que $1$ fallan la primera, y los restantes están fuera del dominio.

### H. Soluciones de profundización y reconstrucción



#### Solución 081

La inequación $(x-a)(x-b)\le0$ sirve. Para $x<a$, ambos factores son negativos y el producto positivo; para $a<x<b$, tienen signos opuestos y el producto negativo; para $x>b$, ambos son positivos. En $a,b$ el producto es cero y se admite. Estas regiones agotan la recta, así que la solución es exactamente $[a,b]$. La orientación de la comparación fija la elección de la región interior.



#### Solución 082

Tomemos $(x-a)(x-b)/(x-c)^2<0$. El dominio excluye $c$; allí el denominador es positivo, de modo que el signo lo decide el numerador. Por los signos de sus dos factores, es negativo exactamente entre $a$ y $b$. Los extremos se excluyen porque la comparación es estricta, y $c$ porque la expresión no existe. Así queda $(a,c)\cup(c,b)$. Multiplicar por el cuadrado es reversible en todo el dominio.



#### Solución 083

La inequación $(x-a)(x-b)^2\le0$ tiene ese conjunto. Fuera de $b$, el cuadrado es positivo y la condición equivale a $x-a\le0$, es decir $x\le a$. En $b$, el producto es cero y también se admite. No hay otros ceros ni puntos donde el cuadrado sea negativo. La multiplicidad par crea el punto aislado sin cambiar el signo de las regiones próximas.



#### Solución 084

Tomemos $(x-a)(x-b)(x-c)>0$. En las cuatro regiones determinadas por $a,b,c$, hay respectivamente tres, dos, una y cero factores negativos, de modo que los signos son $-,+,-,+$. Los tres ceros se excluyen por la comparación estricta. Por tanto, el conjunto es $(a,b)\cup(c,\infty)$. El coeficiente principal positivo importa: cambiarlo por uno negativo intercambiaría las regiones de solución.



#### Solución 085

Cada expresión vale uno en su dominio: $S_a=\mathbb R\setminus\{a\}$ y $S_b=\mathbb R\setminus\{b\}$. Las dos comparaciones reducidas, tomadas en sus dominios naturales, tienen conjunto $\mathbb R$ y coinciden siempre. Las originales tienen el mismo conjunto exactamente si $a=b$. Si $a\ne b$, $a$ pertenece solo a $S_b$ y $b$ solo a $S_a$; su diferencia simétrica es $\{a,b\}$. Sobre el dominio común $\mathbb R\setminus\{a,b\}$ ambas son equivalentes. Cancelar puede producir fórmulas iguales sin producir funciones o problemas iguales.



#### Solución 086

El dominio es $x\ne a$; allí la expresión es $x-b$, luego $S=(-\infty,b]\setminus\{a\}$. Si $a<b$, se escribe $(-\infty,a)\cup(a,b]$; si $a=b$, queda $(-\infty,b)$; si $a>b$, queda $(-\infty,b]$. Cada punto conservado cumple la comparación lineal y el denominador no nulo; ningún otro puede cumplir ambas condiciones. Esta clasificación distingue un hueco interior, un extremo eliminado y una exclusión fuera del conjunto solución.



#### Solución 087

El dominio exige $x\ne a$ y el cociente es $-1$ en él. La inequación es $-(x-b)\ge0$, equivalente a $x\le b$. Por tanto, $S=(-\infty,a)\cup(a,b]$. En $b$ vale cero y se admite; en $a$ no existe. Normalizar $a-x=-(x-a)$ evita perder el signo negativo. Como verificación, el producto original tiene el signo opuesto al de $x-b$ en cada región permitida.



#### Solución 088

El dominio exige $x\ne a,c$. Cancelar el cuadrado da $(x-b)/(x-c)$, cuyo signo es positivo para $x<b$ o $x>c$, y negativo entre $b,c$. El cero $b$ se excluye por ser estricta; el polo $c$ por dominio. Así $S=[(-\infty,b)\cup(c,\infty)]\setminus\{a\}$. Si $a$ está entre $b,c$, coincide con un extremo o cae fuera de ambas regiones, la notación sigue siendo válida; si está en una región admitida, se crea un hueco. No hace falta inventar una rama diferente para cada fórmula si la diferencia de conjuntos conserva todos los casos.



#### Solución 089

La expresión es $x^2-t^2$. La comparación equivale a $|x|\le|t|$, pues ambos módulos son no negativos y comparar sus cuadrados es reversible. Por tanto $S(t)=[-|t|,|t|]$. Para $t=0$ se reduce al punto $\{0\}$; para $t\ne0$ es un intervalo de longitud positiva. Los extremos anulan el producto. Usar $[-t,t]$ sin controlar el signo del parámetro produciría extremos invertidos para $t<0$.



#### Solución 090

Siempre $x\ne1$. Si $t<1$, el cociente es positivo fuera del tramo entre sus puntos críticos y cero en $t$, de modo que $S=(-\infty,t]\cup(1,\infty)$. Si $t>1$, resulta $S=(-\infty,1)\cup[t,\infty)$. Si $t=1$, el cociente vale uno en todo el dominio y $S=\mathbb R\setminus\{1\}$. Los extremos de numerador se admiten y los del denominador no; al fusionarse no puede conservarse el antiguo cero como punto definido.



#### Solución 091

Si $x\ne t,1$, el numerador es positivo y el signo es el del denominador: la comparación se cumple para $x<1$. Si $t\ne1$, también $x=t$ da cero y se admite. Por tanto $S=(-\infty,1)\cup\{t\}$ para $t\ne1$, entendiendo que el punto ya pertenece al rayo si $t<1$. Para $t=1$, la simplificación a $x-1$ conserva el hueco y da $S=(-\infty,1)$. Un cero de multiplicidad par puede aportar un punto aislado cuando $t>1$.



#### Solución 092

Si $t<1$, los factores tienen igual signo para $x\le t$ o $x\ge1$, y $S=(-\infty,t]\cup[1,\infty)$. Si $t>1$, queda $S=(-\infty,1]\cup[t,\infty)$. Si $t=1$, el producto es $(x-1)^2\ge0$ para todo real, por lo que $S=\mathbb R$. Los ceros se incluyen y las regiones exteriores se fusionan cuando desaparece el intervalo intermedio. No hay restricción de dominio porque la expresión es polinómica.



#### Solución 093

Con $u=(x-h)^2\ge0$, la inequación auxiliar da $A\le u\le B$, ya dentro de la imagen. Volver exige $\sqrt A\le|x-h|\le\sqrt B$. Su preimagen es $[h-\sqrt B,h-\sqrt A]\cup[h+\sqrt A,h+\sqrt B]$. Los cuatro extremos hacen cero un factor y se admiten; las regiones entre ellos tienen los signos fijados por el intervalo auxiliar. La sustitución identifica dos ramas pero no autoriza descartar la negativa.



#### Solución 094

Con $u=|x-h|+1$, la imagen es $[1,\infty)$. El producto $(u-2)(u-4)<0$ da $2<u<4$, compatible con esa imagen. Por tanto $1<|x-h|<3$, cuya preimagen es $(h-3,h-1)\cup(h+1,h+3)$. Los extremos producen producto cero y se excluyen. En cada intervalo admitido el valor auxiliar está entre sus dos raíces, y fuera no lo está; esta reconstrucción certifica toda la solución.



#### Solución 095

El dominio exige $x\ne h$ y la positividad es automática allí. La cota superior se multiplica por el cuadrado positivo: $1\le4(x-h)^2$, equivalente a $|x-h|\ge1/2$. Así $S=(-\infty,h-1/2]\cup[h+1/2,\infty)$. Los extremos cumplen la igualdad y el centro no pertenece a ninguna región ni al dominio. La imagen de $u=1/(x-h)^2$ es $(0,\infty)$; cero no es un valor que pueda reconstruirse como un $x$ finito.



#### Solución 096

El denominador es siempre positivo. Con $v=(x-h)^2\ge0$, $u=v/(1+v)$ tiene imagen $[0,1)$: es no negativo, menor que uno y cada $u$ de ese intervalo da $v=u/(1-u)$. Si $c<0$, no hay soluciones; si $c\ge1$, todos los reales sirven. Para $0\le c<1$, $v\le c(1+v)$ equivale a $v\le c/(1-c)$, luego $S=[h-\sqrt{c/(1-c)},h+\sqrt{c/(1-c)}]$. Incluye $c=0$, que da solo $h$. Las cuatro ramas cubren todos los parámetros sin dividir por un número de signo desconocido.

***

[← Capítulo 21](algebra-para-matematicos-capitulo-21-ecuaciones-equivalencias-y-conjuntos-solucion.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 23 →](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md)

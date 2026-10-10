---
{
  "title": "Funciones exponenciales y logaritmos",
  "description": "Capítulo 23 del Tomo I de Álgebra para matemáticos, con 96 ejercicios y soluciones desarrolladas.",
  "content-id": "MA-BCH-0198",
  "content-type": "book-chapter",
  "collection": "PM-ALG",
  "book-id": "MA-BOK-0006",
  "source-id": "APM-T1-C23",
  "editorial-id": "MA-BCH-APM-01-026",
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
    "MA-BCH-0197"
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

C22 nos enseñó a conservar dominio y orden al transformar una condición. Ahora estudiaremos dos funciones que convierten productos en sumas y permiten recuperar exponentes. La estructura de funciones e inversas será tan importante como la destreza de cálculo.



## 23.1. De la potencia a la función exponencial {#apm-c23-s01}

Si una cantidad aumenta tres unidades en cada paso, su evolución puede escribirse $L(n)=L(0)+3n$. Si se multiplica por tres en cada paso, se escribe $M(n)=M(0)3^n$. En el primer caso se repite una suma; en el segundo se repite un producto. Esa diferencia se conserva aunque ambos modelos coincidan en algunos valores.

### ¿Dónde está la variable?

Compare $x^3$ con $3^x$. En $x^3$ varía la base y permanece fijo el exponente. En $3^x$ permanece fija la base y varía el exponente. Son funciones diferentes, con reglas de variación diferentes.

| $x$ | $x^3$ | $3^x$ |
|---:|---:|---:|
| $-1$ | $-1$ | $1/3$ |
| $0$ | $0$ | $1$ |
| $1$ | $1$ | $3$ |
| $2$ | $8$ | $9$ |
| $3$ | $27$ | $27$ |

La coincidencia en $x=3$ no identifica las funciones. Una igualdad de funciones exige coincidencia para todos los argumentos del dominio, como sabemos desde el estudio de funciones. La tabla proporciona aquí contraejemplos a esa igualdad.

### Lo que C18 ya permite

Para una base positiva $a$, C18 define $a^n$ con exponente entero y $a^{m/n}$ con exponente racional mediante raíces principales. Por ejemplo, $9^{1/2}=3$, $9^{-1}=1/9$ y $9^{3/2}=27$.

También conocemos las leyes $a^{r+s}=a^ra^s$ y $(a^r)^s=a^{rs}$ en el régimen racional disponible. La primera muestra cómo se traduce una suma de exponentes en un producto de valores. En particular, $a^{r+1}/a^r=a$: avanzar una unidad en el exponente multiplica por un factor constante.

Para $a=3$, los valores en enteros forman la sucesión $1,3,9,27,\ldots$. No hay una diferencia constante entre términos sucesivos; hay un cociente constante. Ésta es la señal algebraica de variación exponencial.

### Una tasa y un factor no son el mismo dato

Si se añade el $20\%$ del valor presente en cada paso, el nuevo valor es $Q+0.20Q=1.20Q$. El factor es $1.20$, no $0.20$. Tras $n$ pasos, $Q(n)=Q(0)(1.20)^n$, para $n$ entero no negativo.

Si se retira el $20\%$ en cada paso, queda $0.80Q$. La expresión correspondiente es $Q(0)(0.80)^n$. El porcentaje se aplica cada vez al valor presente, no siempre al valor inicial.

Estos son modelos matemáticos hipotéticos. Su fórmula describe la regla estipulada; no demuestra que una población o un objeto real siga esa regla.

### Lo que todavía falta

La expresión $3^{\sqrt2}$ no se define mediante una raíz de índice entero y una potencia entera como las de C18. La función que buscamos debe admitir todo $x\in\mathbb R$, no sólo exponentes racionales.

Una tabla de exponentes decimales puede sugerir valores, pero una sugerencia no demuestra existencia, unicidad ni las leyes para exponentes irracionales. En la siguiente sección explicitaremos el resultado de extensión que admitiremos y separaremos ese resultado de las consecuencias que sí probaremos aquí.

### Prueba de estrés

La expresión $(-3)^x$ no define una función real para todos los reales: en $x=1/2$ exigiría una raíz real de un número negativo. Que algunos exponentes enteros produzcan números reales no resuelve ese problema.

Por otro lado, $1^x$ sí puede extenderse como la constante $1$. Su comportamiento no permite recuperar el exponente: todos los argumentos tienen el mismo valor. Esta degeneración será decisiva cuando definamos el logaritmo.

### Recuperación breve

Una cantidad hipotética comienza en $50$ y se duplica en cada paso. Escriba sus valores después de cero, uno y dos pasos. Compare con sumar $50$ en cada paso.

**Respuesta razonada.** El modelo multiplicativo es $Q(n)=50\,2^n$, con valores $50,100,200$. El aditivo es $L(n)=50+50n$, con valores $50,100,150$. Coinciden en dos argumentos y difieren en el tercero; la regla multiplicativa no puede sustituirse por la aditiva.

### Qué debemos conservar

La posición de la variable decide el tipo de función. Una exponencial mantiene fija la base y hace variar el exponente; en pasos iguales produce factores iguales. Las potencias racionales preparan esa idea, pero no construyen por sí solas la función sobre todo $\mathbb R$.



## 23.2. Exponente real: alcance y propiedades admitidas {#apm-c23-s02}

Queremos utilizar $a^x$ incluso cuando $x$ es irracional. Para hacerlo con honestidad matemática debemos declarar qué resultado aceptamos y qué parte de su prueba dejamos para el análisis.

### Resultado de extensión que admitimos

Para cada $a>0$ existe una función de exponente real $x\mapsto a^x$, compatible con las potencias racionales de C18. Admitimos su existencia y las siguientes propiedades:

- $a^x>0$ para todo real $x$; $a^0=1$ y $a^1=a$.
- $a^{x+y}=a^xa^y$ y $(a^x)^y=a^{xy}$ para $x,y\in\mathbb R$.
- Para $a,b>0$, $(ab)^x=a^xb^x$.
- Si $a>1$, la función es estrictamente creciente; si $0<a<1$, estrictamente decreciente.
- Si $a\ne1$, su imagen es exactamente $(0,\infty)$: todo número positivo aparece como valor.

La extensión estándar es única entre las extensiones que conservan las leyes y la monotonía indicadas; también admitimos ese resultado. Para $a=1$ obtenemos la constante $1$, cuya imagen es $\{1\}$.

**La existencia de esta extensión y sus propiedades fundamentales se admiten en este capítulo.** Su construcción rigurosa, incluida la justificación de que se alcanzan todos los positivos, corresponde al tratamiento de los reales y las funciones en cálculo/análisis. No la deduciremos de una gráfica o de una lista de aproximaciones.

Esto no significa que todas las reglas posteriores sean admisiones. Desde estas propiedades podremos demostrar identidades, definir la inversa y justificar transformaciones de ecuaciones e inequaciones.

### Definición de función exponencial

Para una base $a>0$ con $a\ne1$, llamamos **función exponencial de base $a$** a $E_a:\mathbb R\to(0,\infty)$, $E_a(x)=a^x$.

El codominio positivo coincide aquí con la imagen. La exclusión $a\ne1$ garantiza que la función no sea constante y permitirá invertirla. La condición $a>0$ garantiza que se trata de la exponencial real definida para todos los exponentes reales.

### Consecuencias que ya podemos probar

Como $a^xa^{-x}=a^0=1$, se obtiene $a^{-x}=1/a^x$. El denominador nunca es cero por positividad.

De ahí,

$$
\frac{a^x}{a^y}=a^xa^{-y}=a^{x-y}.
$$

La ley del producto para bases positivas da $(a/b)^x=a^x/b^x$ cuando $a,b>0$. Se aplica a $a$ y $1/b$ y se usa $(1/b)^x=b^{-x}$.

Por ejemplo, $5^{\sqrt2}/5^{\sqrt2-1}=5$. El resultado no exige aproximar $\sqrt2$: depende de una identidad válida para exponentes reales.

### Argumentos diferentes, misma regla

La ley $a^{u+v}=a^ua^v$ puede utilizarse con $u=2x$ y $v=-3$, de modo que $a^{2x-3}=a^{2x}/a^3$. También $(a^2)^x=a^{2x}$.

No puede utilizarse para distribuir la exponencial sobre una suma de valores: $a^x+a^y$ no es, en general, $a^{x+y}$. Para $a=2$ y $x=y=1$, la coincidencia $2+2=4$ resulta accidental; con $x=y=2$, tenemos $4+4=8$ mientras $2^4=16$. Un contraejemplo basta para refutar la supuesta identidad.

### Aproximar y demostrar

Una calculadora puede dar una aproximación a $2^{\sqrt2}$. Si se escribe un decimal truncado, se debe usar $\approx$, no sustituirlo silenciosamente por una igualdad exacta.

Los decimales son útiles para leer escala o ubicar valores. La solución exacta puede seguir siendo $2^{\sqrt2}$, y las leyes permiten operar con ella sin convertirla a decimal. Tampoco muchos valores numéricos favorables demuestran una identidad para todos los reales.

### Prueba de estrés de las hipótesis

La positividad de la base es parte de las leyes aquí admitidas. No trasladamos automáticamente $(a^x)^y=a^{xy}$ a bases negativas. Por ejemplo, $((-1)^2)^{1/2}=1$ y $(-1)^{2(1/2)}=-1$. Ambas expresiones concretas existen, pero no coinciden.

El capítulo estudia la familia de bases positivas. Las raíces reales con bases negativas de C18 conservan sus propias condiciones; una fórmula escrita sin ellas puede ser falsa.

### Recuperación breve

Simplifique $7^{t+2}/7^t$ y $7^t7^{-t}$ para cualquier real $t$. Identifique qué parte de su argumento usa el resultado admitido.

**Respuesta razonada.** La ley del cociente da $7^2=49$ y la del producto da $7^0=1$. El argumento usa las leyes exponenciales para exponentes reales y la positividad que autoriza dividir. No requiere construir cada valor $7^t$ ni suponer que $t$ sea racional.

### Qué debemos conservar

Trabajaremos sobre una extensión real declarada, con hipótesis y propiedades precisas. Su construcción se difiere; sus consecuencias algebraicas se demuestran. Esta distinción permite avanzar con rigor sin presentar aproximaciones como pruebas.



### Registrar la dependencia de una prueba

Las leyes de las potencias reales se admiten en [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02); usarlas para deducir una consecuencia no convierte esa consecuencia en una nueva admisión. Por ejemplo, la inyectividad de $a^x$ para $a\ne1$ se demuestra desde la monotonía estricta admitida: si $x<y$ o $y<x$, los valores son distintos. **Control resuelto:** de $a^{2x+1}=a^5$, con $a>0$, $a\ne1$, concluimos $2x+1=5$ y $x=2$. La comprobación es $a^5=a^5$. Si $a=1$, todos los reales verifican la ecuación y la inferencia por inyectividad deja de estar disponible. Una prueba debe declarar su punto de apoyo y conservar las hipótesis, sin presentar la construcción de la exponencial real como si ya hubiese sido demostrada.



## 23.3. Monotonía, inyectividad e imagen {#apm-c23-s03}

El orden de C22 permite comparar valores exponenciales sin calcularlos. La comparación cambia según la base esté por encima o por debajo de $1$.

### Dos orientaciones

Para $a>1$, la monotonía admitida dice que $u<v$ implica $a^u<a^v$. Para $0<a<1$, implica $a^u>a^v$. Al aumentar el exponente, la primera función aumenta y la segunda disminuye.

| Base | Valores en $-1,0,1,2$ | Orientación |
|---|---|---|
| $2$ | $1/2,1,2,4$ | creciente |
| $1/2$ | $2,1,1/2,1/4$ | decreciente |

La tabla ilustra propiedades válidas para todos los reales; no las prueba. Esas propiedades provienen del resultado admitido en [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02).

### Por qué la monotonía estricta da inyectividad

Suponga $a^u=a^v$ con base válida. Si $u<v$, la monotonía estricta produciría valores distintos; si $u>v$, también. La tricotomía deja únicamente $u=v$.

La vuelta es inmediata: exponentes iguales dan valores iguales. Por tanto, $a^u=a^v\Longleftrightarrow u=v$. Éste es el fundamento de «igualar exponentes» cuando las bases coinciden.

Por ejemplo, $3^{2x-1}=3^{x+4}$ equivale a $2x-1=x+4$, así que $x=5$. No se canceló una letra: se aplicó la inyectividad de una función conocida.

La base debe ser la misma y válida. De $2^u=4^v$ no se sigue $u=v$; primero se escribe $4^v=2^{2v}$ y entonces se obtiene $u=2v$.

### Equivalencias de orden

Para $a>1$, también es cierta la vuelta de $u<v\Rightarrow a^u<a^v$. Si los valores satisfacen esa comparación, las alternativas $u=v$ y $u>v$ la contradicen. Así,

$$
a^u<a^v\Longleftrightarrow u<v\quad(a>1),\qquad
a^u<a^v\Longleftrightarrow u>v\quad(0<a<1).
$$

Las relaciones no estrictas incluyen además la igualdad. Estas equivalencias permiten transportar un problema de valores a uno de exponentes.

Por ejemplo, $(1/3)^{2x}> (1/3)^4$ equivale a $2x<4$, de modo que $x<2$. Hay una inversión por monotonía decreciente; dividir después por $2>0$ conserva la orientación.

### Positividad e imagen

Ninguna exponencial de base positiva vale cero ni toma valores negativos. La ecuación $2^x=-5$ no tiene solución real y $2^x=0$ tampoco.

En cambio, $2^x=5$ tiene exactamente una solución: existencia porque $5$ pertenece a la imagen positiva; unicidad por inyectividad. Todavía no hemos nombrado esa solución, pero sabemos que está entre $2$ y $3$ porque $2^2=4<5<8=2^3$.

La sobreyectividad no se deduce sólo de la monotonía. Una función puede ser estrictamente creciente sin cubrir todo su codominio. Aquí la cobertura de $(0,\infty)$ es una propiedad adicional admitida en [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02).

### Comparar con uno

Como $a^0=1$, para $a>1$ tenemos $a^x>1$ exactamente cuando $x>0$, y $0<a^x<1$ exactamente cuando $x<0$. Para $0<a<1$, esas conclusiones se invierten: exponentes positivos producen valores entre $0$ y $1$.

Así, sin calcular un decimal, $5^{-2/3}<1$ y $(1/5)^{-2/3}>1$. En ambos casos los valores siguen siendo positivos.

### Prueba de estrés: la base constante

Con $a=1$, la igualdad $1^u=1^v$ siempre es verdadera, aunque $u\ne v$. La ecuación $1^x=1$ tiene todo $\mathbb R$ como solución y $1^x=2$ tiene solución vacía. No se puede igualar exponentes en este régimen.

Si la base es un parámetro, su restricción debe fijarse antes de usar inyectividad. La notación exponencial no reemplaza esa comprobación.

### Recuperación breve

Resuelva $4^{x-2}=1$ y $(1/4)^{x-2}\ge1$. Explique la diferencia.

**Respuesta razonada.** En la primera, $1=4^0$ e inyectividad da $x=2$. En la segunda, $1=(1/4)^0$ y la monotonía decreciente da $x-2\le0$, de modo que $S=(-\infty,2]$. La igualdad selecciona un exponente; la comparación de orden selecciona una región.

### Qué debemos conservar

La monotonía estricta prueba inyectividad y gobierna las comparaciones. La imagen positiva decide existencia y descarta valores imposibles. Igualdad, orden y cobertura son propiedades relacionadas, pero cumplen obligaciones diferentes en una resolución.



## 23.4. Transformaciones y lectura funcional {#apm-c23-s04}

Una función exponencial puede aparecer trasladada, multiplicada por una constante o compuesta con otra expresión. Reconocer esas operaciones permite determinar su dominio e imagen antes de resolver una ecuación.

### Trasladar el argumento o el valor

Compare $f(x)=2^{x-3}$ y $g(x)=2^x-3$. En la primera se resta dentro del argumento exponencial; en la segunda se resta al valor.

Como $f(3)=1$ y $g(3)=5$, son funciones diferentes. La identidad $2^{x-3}=2^x/8$ muestra que trasladar el argumento puede interpretarse también como escalar los valores. Restar $3$ a los valores produce otra operación.

| $x$ | $2^x$ | $2^{x-3}$ | $2^x-3$ |
|---:|---:|---:|---:|
| $0$ | $1$ | $1/8$ | $-2$ |
| $3$ | $8$ | $1$ | $5$ |
| $4$ | $16$ | $2$ | $13$ |

La lectura mediante pares conserva la distinción entre coordenada de entrada y valor de salida. No hace falta una gráfica para decidir que las transformaciones son distintas.

### Imagen de una familia trasladada

Considere $F(x)=A\,a^{kx+h}+B$, con $a>0$, $a\ne1$, $A\ne0$ y $k\ne0$. El argumento afín $kx+h$ recorre todo $\mathbb R$: para un real $u$, basta tomar $x=(u-h)/k$.

Por ello $a^{kx+h}$ recorre todos los positivos. Si $A>0$, $F$ tiene imagen $(B,\infty)$; si $A<0$, tiene imagen $(-\infty,B)$. El valor $B$ nunca se alcanza porque el término exponencial no se anula.

Ésta es una prueba de imagen: indica qué valores aparecen y construye una preimagen a partir de la cobertura de la exponencial. No se infiere sólo de la apariencia de una curva.

Para $F(x)=3\,2^{x-1}-4$, el dominio es $\mathbb R$ y la imagen $(-4,\infty)$. Una ecuación $F(x)=-4$ no tiene solución; una ecuación $F(x)=8$ sí tiene una, porque $8>-4$.

### Orientación bajo composición y escala

Si $a>1$ y $k>0$, aumentar $x$ aumenta $kx+h$ y luego aumenta la exponencial. Si $k<0$, la primera operación invierte el orden. Para $0<a<1$, la exponencial agrega otra inversión.

Multiplicar por $A<0$ invierte otra vez, mientras sumar $B$ no cambia la orientación. Podemos contar esas inversiones porque cada una está justificada por C22 o [§23.3](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s03).

En $F(x)=-2(1/3)^{2x+1}+5$, el argumento es creciente, la exponencial decreciente y el multiplicador negativo invierte: $F$ es creciente. Su imagen es $(-\infty,5)$. Ser creciente no obliga a que sus valores sean positivos.

### Argumentos con dominio propio

La función $H(x)=2^{1/(x-2)}$ sólo existe si $x\ne2$. La exponencial exterior admite todo real, pero la expresión interior no. Así, el dominio es $\mathbb R\setminus\{2\}$.

El argumento $1/(x-2)$ recorre $\mathbb R\setminus\{0\}$: no vale cero y cualquier $u\ne0$ tiene preimagen $x=2+1/u$. Por inyectividad, el valor exponencial omitido es $2^0=1$. La imagen es $(0,\infty)\setminus\{1\}$.

La regla de dominio de composición conserva todas las condiciones interiores. No debemos responder automáticamente «dominio $\mathbb R$» sólo porque aparezca una exponencial.

### Casos degenerados

En la familia $A\,a^{kx+h}+B$, si $A=0$, la función vale $B$ allí donde la expresión original esté definida. Si $k=0$ y el resto de parámetros es válido, es constante $Aa^h+B$. Las fórmulas de imagen anteriores se justificaron con $A\ne0$ y $k\ne0$, de modo que no se aplican sin cambios a esos casos.

Si una escritura original contiene un argumento indefinido, multiplicar por cero no le da automáticamente un valor allí: se conserva el dominio de la expresión original, como en C20.

### Recuperación breve

Determine dominio, imagen y orientación de $F(x)=4-3\,2^{-x}$.

**Respuesta razonada.** El dominio es $\mathbb R$. Como $-x$ recorre todos los reales, $2^{-x}$ recorre todos los positivos, así que la imagen es $(-\infty,4)$. Aumentar $x$ disminuye $-x$ y la exponencial; multiplicar por $-3$ invierte esa disminución. Por tanto, $F$ es estrictamente creciente. El valor $4$ se excluye porque la exponencial nunca vale cero.

### Qué debemos conservar

Leer una transformación exige seguir entrada, función exterior y salida. El dominio se hereda desde el argumento; la imagen se transporta mediante escala y traslación; la orientación se determina por operaciones que conservan o invierten el orden. Las hipótesis no nulas separan las funciones invertibles de sus degeneraciones.



## 23.5. El logaritmo como función inversa {#apm-c23-s05}

La ecuación $2^x=7$ tiene una única solución real, pero no podemos nombrarla con un exponente entero sencillo. El logaritmo dará un nombre exacto a ese exponente; no es una aproximación ni una nueva operación sin relación con las anteriores.

### Existencia y unicidad antes de la notación

Fijemos $a>0$, $a\ne1$. Para cada $b>0$, la imagen de $E_a$ garantiza un real $y$ con $a^y=b$. Su inyectividad garantiza que ese real sea único.

**Definición.** Llamamos **logaritmo de $b$ en base $a$** a ese exponente único y lo escribimos $\log_a b$. Así,

$$
y=\log_a b\Longleftrightarrow a^y=b,\qquad a>0,\ a\ne1,\ b>0.
$$

Se trata de la inversa $L_a:(0,\infty)\to\mathbb R$ de $E_a$. En la forma exponencial, $a$ es la base, $y$ el exponente y $b$ el valor. En la forma logarítmica, la base sigue siendo $a$, el argumento es $b$ y el valor es el exponente $y$.

### Una traducción que conserva tres papeles

| Forma exponencial | Forma logarítmica | Lectura |
|---|---|---|
| $3^4=81$ | $\log_3 81=4$ | exponente que produce $81$ |
| $5^{-2}=1/25$ | $\log_5(1/25)=-2$ | un argumento positivo puede dar logaritmo negativo |
| $(1/2)^3=1/8$ | $\log_{1/2}(1/8)=3$ | una base menor que uno es válida |
| $9^{1/2}=3$ | $\log_9 3=1/2$ | el exponente puede ser fraccionario |

En particular, $\log_a1=0$ y $\log_aa=1$, porque $a^0=1$ y $a^1=a$. Para $2^x=7$, la solución exacta es $x=\log_2 7$. La notación identifica completamente el número mediante una propiedad de existencia y unicidad.

### Por qué no hay logaritmo real de cero o negativo

Para todo real $y$, $a^y>0$. Por ello no existe un exponente que produzca $0$ o un número negativo. Las expresiones $\log_a0$ y $\log_a(-3)$ no están definidas en nuestro marco real.

Que el valor del logaritmo pueda ser negativo no contradice esa condición: el argumento debe ser positivo, mientras el resultado puede ser cualquier real. $\log_2(1/8)=-3$ es un ejemplo que distingue ambos papeles.

### Por qué la base uno no sirve

La función $1^y$ vale $1$ para todos los exponentes. Si el argumento es $1$, no hay un exponente único; si el argumento es diferente de $1$, no hay ninguno. En ningún caso se obtiene una inversa de la exponencial constante.

Por eso $\log_1 b$ no es una función logarítmica válida. La restricción de la base no es una dificultad de la calculadora: es una obligación matemática anterior al cálculo.

### Soluciones por definición

Considere $\log_3(x+2)=2$. Primero se exige $x+2>0$, es decir $x>-2$. Dentro de ese dominio, la definición da $x+2=3^2=9$, de modo que $x=7$. Ese valor está en el dominio y sustituirlo recupera $\log_39=2$.

La definición también permite que la base sea la incógnita, si se conservan sus restricciones. Para $\log_x16=2$, el dominio es $x>0$, $x\ne1$. La forma exponencial da $x^2=16$; de los candidatos $\pm4$ sólo $4$ es una base admisible. Por tanto, $S=\{4\}$.

### Prueba de estrés de la traducción

De $\log_2 8=3$ no se obtiene $2^8=3$. Esa escritura intercambia argumento y exponente. La verificación por la definición muestra inmediatamente el error: el exponente buscado es $3$, y $2^3=8$.

Tampoco $\log_a b$ significa dividir $b$ entre $a$. Con $a=2,b=8$, el logaritmo vale $3$ y el cociente vale $4$.

### Recuperación breve

Evalúe $\log_4(1/8)$ y determine si $\log_{-4}16$ pertenece al marco de este capítulo.

**Respuesta razonada.** Como $4^{-3/2}=(2^2)^{-3/2}=2^{-3}=1/8$, se obtiene $\log_4(1/8)=-3/2$. La segunda expresión tiene base negativa y no es un logaritmo real de base válida. No se rescata la función por observar que alguna potencia entera de $-4$ pueda ser positiva.

### Qué debemos conservar

Un logaritmo es un exponente único, definido mediante una inversa. Su argumento es positivo, su base positiva y distinta de uno, y su valor puede ser cualquier real. Traducir de forma exponencial a logarítmica conserva los papeles de los tres números.



## 23.6. Dominios, imagen y composiciones inversas {#apm-c23-s06}

Una operación inversa sólo deshace la original en el dominio donde ambas tienen sentido. Esa condición merece escribirse incluso cuando los símbolos parezcan cancelarse.

### Las dos identidades inversas

Para todo $x\in\mathbb R$, el número $a^x$ es positivo. Su logaritmo está definido y, por la unicidad del exponente, $\log_a(a^x)=x$.

Para todo $t>0$, el número $\log_at$ está definido y su propiedad definitoria da $a^{\log_at}=t$. Esta segunda identidad no está definida en $t=0$ ni en $t<0$.

En términos de composición, $L_a\circ E_a$ es la identidad de $\mathbb R$ y $E_a\circ L_a$ es la identidad de $(0,\infty)$. Son identidades sobre conjuntos diferentes.

Por ejemplo, $2^{\log_2(x-3)}=x-3$ sólo en $x>3$. La expresión simplificada $x-3$ puede escribirse para todo real, pero eso no amplía el dominio de la expresión original.

### Dominio de un logaritmo compuesto

Para $\log_a G(x)$, conservamos el dominio de $G$ y añadimos $G(x)>0$. No basta exigir que $G$ esté definida.

En $F(x)=\log_2((x-1)/(x+2))$, la racional exige $x\ne-2$ y el argumento positivo exige $(x-1)/(x+2)>0$. Por C22, el cociente es positivo para $x<-2$ o $x>1$. El dominio de $F$ es $(-\infty,-2)\cup(1,\infty)$.

El punto $1$ no es un polo, pero produce argumento cero y queda excluido. El punto $-2$ es un polo y queda excluido antes de preguntar por el logaritmo. Ambos extremos son abiertos por razones diferentes.

### Una composición dentro de otra

Para $H(x)=\log_2(\log_3x)$, el logaritmo interior exige $x>0$. El exterior exige además $\log_3x>0$. Como la base $3>1$ y $\log_31=0$, esa condición equivale a $x>1$. El dominio completo es $(1,\infty)$.

Si se cambia el interior por $\log_{1/3}x$, su positividad equivale a $0<x<1$. La base modifica el dominio de la composición porque modifica el signo del valor interior.

No confundimos aquí «argumento positivo» con «logaritmo positivo». Para un logaritmo simple basta el primero; si ese logaritmo es argumento de otro, aparece también el segundo.

### Un logaritmo en un denominador

En $J(x)=1/\log_2(x-1)$ necesitamos $x-1>0$ y $\log_2(x-1)\ne0$. El logaritmo vale cero exactamente cuando $x-1=1$. Por tanto, $D=(1,2)\cup(2,\infty)$.

La exclusión $x=2$ proviene de la división exterior. El argumento del logaritmo es positivo allí, pero el valor resultante no puede usarse como denominador.

### Imagen del logaritmo y de una restricción

La función $L_a:(0,\infty)\to\mathbb R$ cubre todo $\mathbb R$: dado $y\in\mathbb R$, el argumento $a^y$ produce $\log_a(a^y)=y$. Esta prueba utiliza la primera identidad inversa.

Una restricción de dominio modifica la imagen. Para $\log_2x$ con $x\in[1,8]$, escriba $y=\log_2x$, de modo que $x=2^y$. Como la exponencial de base $2$ es creciente, $1\le2^y\le8$ equivale a $0\le y\le3$. Recíprocamente, cada $y\in[0,3]$ tiene preimagen $x=2^y\in[1,8]$. Por tanto, la imagen es $[0,3]$. La prueba usa la monotonía exponencial ya establecida; la monotonía de la inversa se demostrará en [§23.7](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s07).

### Prueba de estrés: simplificar sin recuperar restricciones

La expresión $2^{\log_2(x^2-1)}$ se simplifica a $x^2-1$ cuando $x^2-1>0$, esto es $x<-1$ o $x>1$. En $x=0$, el polinomio simplificado vale $-1$, pero la expresión original no existe.

La igualdad de expresiones se afirma sobre el dominio común. La simplificación puede ofrecer una fórmula más extendida; usarla en valores nuevos cambia el objeto original.

### Recuperación breve

Determine el dominio de $\log_5(\sqrt{x+4}-2)$.

**Respuesta razonada.** La raíz exige $x\ge-4$. El argumento debe ser estrictamente positivo: $\sqrt{x+4}>2$. Ambos miembros son no negativos, así que cuadrar equivale a $x+4>4$, es decir $x>0$. Esta última condición ya garantiza la existencia de la raíz. El dominio es $(0,\infty)$; en $0$ el argumento vale cero y se excluye.

### Qué debemos conservar

En una composición, cada capa aporta sus condiciones. Las identidades inversas conservan los dominios originales; no convierten una expresión indefinida en un valor nuevo. La imagen también se transporta con cuidado cuando se restringe el dominio.



### Leer las capas antes de aplicar una inversa

Para $F=\log_a(a^{\log_a G(x)})$, primero debe existir $G$, luego ser positivo para el logaritmo interior. La exponencial produce entonces un positivo y el logaritmo exterior existe. Solo después se reduce a $\log_a G(x)$. **Control resuelto:** si $G(x)=(x-r)/(x-s)$ con $r<s$, el dominio es $(-\infty,r)\cup(s,\infty)$. La reducción conserva ese mismo dominio, porque el cociente debe ser positivo y estar definido. Si en cambio escribimos $a^{\log_a G(x)}=G(x)$, la fórmula racional final tiene un dominio natural mayor, pero la composición no lo adquiere. Las operaciones inversas deshacen valores admisibles; no reparan capas originalmente indefinidas.



## 23.7. Monotonía y signo del logaritmo {#apm-c23-s07}

Si la exponencial permite comparar exponentes, su inversa permite comparar argumentos. Debemos demostrar cuál es la orientación de esa inversa, sin deducirla únicamente de una gráfica.

### Inversa de una exponencial creciente

Sean $0<u<v$ y $a>1$. Escribamos $r=\log_au$ y $s=\log_av$, de modo que $a^r=u$ y $a^s=v$.

Si $r=s$, tendríamos $u=v$, contradicción. Si $r>s$, la exponencial creciente daría $u>v$, otra contradicción. Por tricotomía, $r<s$. Así, $\log_a$ es estrictamente creciente.

La vuelta también se obtiene mediante la exponencial: si $\log_au<\log_av$, aplicar $a^x$ conserva el orden y produce $u<v$. Ambas operaciones están definidas en los dominios indicados.

### Inversa de una exponencial decreciente

Ahora sea $0<a<1$. Con los mismos $u<v$ y exponentes $r,s$, si $r\le s$, la exponencial decreciente daría $u\ge v$. Por tanto, $r>s$.

Así, $\log_a$ es estrictamente decreciente. La equivalencia completa es $\log_au<\log_av\Longleftrightarrow u>v$ para argumentos positivos. También es inyectiva: valores logarítmicos iguales producen argumentos iguales al aplicar la exponencial.

### Signo respecto de uno

Como $\log_a1=0$, para $a>1$ el logaritmo es negativo en $(0,1)$, cero en $1$ y positivo en $(1,\infty)$. Para $0<a<1$, los signos se invierten.

| Argumento $t$ | $\log_2t$ | $\log_{1/2}t$ |
|---|---|---|
| $0<t<1$ | negativo | positivo |
| $t=1$ | cero | cero |
| $t>1$ | positivo | negativo |

La condición $t>0$ se conserva en toda la tabla. Un valor negativo del logaritmo nunca implica argumento negativo.

### Comparar sin aproximaciones

Para comparar $\log_2 5$ y $\log_2 7$, basta $5<7$ y la monotonía creciente. Para comparar $\log_{1/2}5$ y $\log_{1/2}7$, se invierte: el primero es mayor.

También podemos acotar $\log_3 20$ porque $9<20<27$. Aplicar el logaritmo creciente da $2<\log_320<3$. Una cota exacta comunica información sin calcular un decimal.

No comparamos automáticamente $\log_25$ con $\log_35$ mediante sus argumentos iguales: las funciones son diferentes. Más adelante el cambio de base permitirá relacionarlas.

### Transportar una comparación con un número real

Para $G(x)>0$, la comparación $\log_aG(x)\le c$ equivale a $G(x)\le a^c$ si $a>1$, y a $G(x)\ge a^c$ si $0<a<1$.

La prueba consiste en escribir $c=\log_a(a^c)$ y aplicar la equivalencia de orden entre argumentos positivos. La restricción $G(x)>0$ no desaparece después de transformar.

Por ejemplo, $\log_{1/2}(x-1)\le2$ exige inicialmente $x>1$. La orientación decreciente da $x-1\ge1/4$, de modo que $S=[5/4,\infty)$. En ese caso la desigualdad transformada implica la restricción original, pero se comprobó antes de descartarla como redundante.

### Prueba de estrés

La frase «el logaritmo es creciente» omite una hipótesis. Para base $1/2$, $\log_{1/2}(1/4)=2$ y $\log_{1/2}(1/2)=1$: el argumento aumenta y el valor disminuye.

Una demostración o resolución que aplique monotonía debe identificar la base. Si depende de un parámetro, los regímenes pueden exigir respuestas distintas.

### Recuperación breve

Sin decimales, determine el signo de $\log_7(1/3)$ y de $\log_{1/7}(1/3)$. Después resuelva $\log_7(x+1)>0$.

**Respuesta razonada.** El argumento $1/3$ está entre cero y uno: el primer logaritmo es negativo y el segundo positivo. La inequación exige $x+1>0$ y, por base creciente, $x+1>1$. Su solución es $(0,\infty)$; la condición final implica el dominio inicial.

### Qué debemos conservar

La inversa conserva la orientación de una función monótona: creciente con creciente y decreciente con decreciente. El signo del logaritmo se lee comparando el argumento con uno. Al transportar desigualdades, mantenemos positividad y controlamos la base.



## 23.8. Leyes de productos, cocientes y potencias {#apm-c23-s08}

Los logaritmos convierten estructuras multiplicativas en estructuras aditivas. Esa afirmación necesita hipótesis: todos los argumentos de los logaritmos que aparezcan deben ser positivos.

### Ley del producto y su demostración

Sean $u,v>0$ y una base válida $a$. Defina $r=\log_au$ y $s=\log_av$. Entonces $u=a^r$ y $v=a^s$, de modo que $uv=a^ra^s=a^{r+s}$.

El exponente que produce $uv$ es único. Por definición, $\log_a(uv)=r+s=\log_au+\log_av$. Esta prueba muestra de dónde proviene la suma: de la suma de exponentes en la ley exponencial.

Por ejemplo, $\log_2(8\cdot4)=\log_28+\log_24=3+2=5$. El argumento compuesto es $32=2^5$, lo que permite una comprobación independiente.

### Ley del cociente

Con $u,v>0$, los mismos exponentes dan $u/v=a^{r-s}$. Por la definición inversa,

$$
\log_a\left(\frac uv\right)=\log_au-\log_av.
$$

El cociente es positivo y los dos logaritmos del lado derecho existen. Un cociente positivo formado por dos negativos no autoriza esta escritura: los logaritmos separados serían indefinidos.

Por ejemplo, $\log_2((-8)/(-2))=\log_24=2$ existe. La escritura $\log_2(-8)-\log_2(-2)$ no existe en los reales, aunque el cociente previo sí exista.

### Ley de la potencia

Si $u>0$ y $t\in\mathbb R$, escribimos $u=a^r$ con $r=\log_au$. La ley exponencial da $u^t=(a^r)^t=a^{rt}$. Por tanto, $\log_a(u^t)=t\log_au$.

Se admite cualquier exponente real porque las bases $u$ y $a$ son positivas. La ley también cubre $t=0$, cuando ambos miembros valen cero, y exponentes negativos, que corresponden a recíprocos positivos.

### Cuadrados y valor absoluto

Para $x\ne0$, $x^2=|x|^2$ y $|x|>0$. La ley de potencia se aplica a la base positiva $|x|$, así que $\log_a(x^2)=2\log_a|x|$.

Escribir $2\log_ax$ sólo es válido si $x>0$. En $x=-2$, el lado izquierdo $\log_a4$ existe, pero $\log_a(-2)$ no. La fórmula con valor absoluto conserva todo el dominio original.

Análogamente, para $x,y\ne0$, $\log_a(x^2/y^2)=2\log_a|x|-2\log_a|y|$. Los valores absolutos no son adornos: permiten que los argumentos de los logaritmos separados sigan siendo positivos.

### Expandir y condensar conservando dominio

En $x>2$, podemos expandir $\log_3((x-2)(x+1)^2)$ como $\log_3(x-2)+2\log_3(x+1)$, porque los dos factores base son positivos.

El dominio del logaritmo original también es $x>2$: el cuadrado es positivo salvo en $-1$, y el signo del producto exige $x-2>0$. Ambas formas representan la misma función allí.

En cambio, $\log_3((x-2)(x+1))$ tiene dominio $x<-1$ o $x>2$. Expandir como $\log_3(x-2)+\log_3(x+1)$ conserva sólo $x>2$. Si se necesita una expansión sobre todo el dominio original, se usa $\log_3|x-2|+\log_3|x+1|$ allí, ya que el producto original es positivo y coincide con el producto de los valores absolutos.

Condensar dos logaritmos tampoco permite ampliar el dominio. Si partimos de la suma sin valores absolutos, seguimos exigiendo ambos argumentos positivos aunque el producto condensado también sea positivo en otra región.

### Prueba de estrés: no hay ley de suma

En general, $\log_a(u+v)\ne\log_au+\log_av$. La ley del producto identifica el lado derecho con $\log_a(uv)$, no con un logaritmo de suma.

Por ejemplo, $\log_2(1+3)=2$, mientras $\log_21+\log_23=\log_23<2$, porque $3<4$. El contraejemplo usa valores definidos y comparación exacta.

Tampoco $(\log_au)^2$ es $2\log_au$: el primero es un cuadrado del valor logarítmico; el segundo puede expresarse como $\log_a(u^2)$ con $u>0$. Son operaciones distintas.

### Recuperación breve

Expanda $\log_5(25x^2/y)$ sin perder valores de su dominio.

**Respuesta razonada.** El argumento es positivo exactamente cuando $x\ne0$ y $y>0$: el numerador es positivo para $x\ne0$, y el denominador debe ser positivo. Sobre ese dominio, la expansión es $2+2\log_5|x|-\log_5y$. Se usaron producto, potencia de $|x|>0$ y cociente, manteniendo $y>0$.

### Qué debemos conservar

Las leyes logarítmicas se demuestran desde leyes exponenciales y unicidad del exponente. Su uso conserva argumentos positivos y el dominio original. Expandir o condensar cambia la forma de una expresión; no concede automáticamente valores nuevos.



## 23.9. Cambio de base {#apm-c23-s09}

Una calculadora suele ofrecer logaritmos de base $10$ y de una base especial llamada $e$. Eso no limita el concepto a esas bases. Podemos relacionar cualesquiera dos bases válidas mediante una identidad demostrada.

### Derivación de la fórmula

Sean $a,b>0$, $a\ne1$, $b\ne1$, y $t>0$. Si $y=\log_at$, entonces $a^y=t$. Aplicar $\log_b$ a ambos miembros es válido porque son positivos. La ley de potencia da $y\log_ba=\log_bt$.

Además, $\log_ba\ne0$: un logaritmo vale cero exactamente cuando su argumento es $1$, y $a\ne1$. Podemos dividir y obtener

$$
\log_at=\frac{\log_bt}{\log_ba}.
$$

No se trata de elegir una base «mejor» en la definición. Se trata de expresar el mismo exponente con valores de otra función logarítmica.

### Una evaluación exacta

Para $\log_4 8$, elegimos base $2$. Tenemos $\log_48=\log_28/\log_24=3/2$. La comprobación por definición es $4^{3/2}=8$.

Para $\log_{1/3}9$, la base $3$ da $2/(-1)=-2$. El denominador negativo es correcto: la nueva fórmula también representa bases menores que uno.

### Identidades entre bases

Con $t=b$, la fórmula da $\log_ab=1/\log_ba$. Ambas expresiones existen porque las bases son positivas y distintas de uno.

Para tres bases válidas, $\log_ab\cdot\log_bc=\log_ac$, como se comprueba usando una misma base auxiliar y cancelando un denominador no nulo. Esta identidad enlaza conversiones sucesivas de base; no expresa un producto de argumentos de una misma función.

Si $a>0$, $a\ne1$ y $r\ne0$, la base $a^r$ es válida. La fórmula y la ley de potencia dan $\log_{a^r}t=(1/r)\log_at$. La hipótesis $r\ne0$ evita la base $a^0=1$.

### Signo del denominador y orientación

Si se usa una base auxiliar $b>1$, el denominador $\log_ba$ es positivo para $a>1$ y negativo para $0<a<1$. Como el numerador $\log_bt$ es creciente, dividir por ese denominador explica las dos orientaciones de $\log_at$.

No es una nueva admisión: es una reinterpretación de la monotonía ya demostrada. El signo de una constante multiplicativa vuelve a gobernar el orden, como en C22.

### Base variable y dominio

En $F(x)=\log_x9$, la base variable exige $x>0$ y $x\ne1$. El argumento fijo $9$ es positivo. Usando base $3$, $F(x)=2/\log_3x$ sobre ese dominio.

La fórmula muestra las dos exclusiones: el logaritmo del denominador exige $x>0$ y la división exige $\log_3x\ne0$, esto es $x\ne1$. No podemos tratar $\log_x9$ como un logaritmo de base fija al comparar distintos valores de $x$; el cambio de base permite analizar su dependencia real.

### Prueba de estrés

El cociente $\log_b t/\log_b a$ no es $\log_b(t/a)$. La ley del cociente resta logaritmos; el cambio de base divide sus valores.

Por ejemplo, $\log_28/\log_24=3/2$, mientras $\log_2(8/4)=1$. Las dos formas responden a operaciones diferentes.

### Recuperación breve

Evalúe $\log_9 27$ y $\log_{1/9}27$ por una base común. Explique por qué no puede usar base auxiliar $1$.

**Respuesta razonada.** En base $3$, los cocientes son $3/2$ y $3/(-2)=-3/2$. La base auxiliar $1$ no define un logaritmo ni una función inversa, de modo que sus supuestos valores no existen.

### Qué debemos conservar

El cambio de base se deriva de una identidad exponencial y una ley de potencia. Conserva argumento positivo, bases válidas y denominador no nulo. Permite cambiar representación sin cambiar el número que queremos describir.



## 23.10. e, exp y ln {#apm-c23-s10}

Hasta ahora cualquier base positiva distinta de uno ha sido válida. Una de ellas recibe una notación especial por su papel en el análisis y en muchos modelos: la constante $e$.

### Un objeto nombrado, no construido aquí

Denotamos por $e$ la constante distinguida de los reales cuya aproximación es $e\approx2.71828$. En particular, $e>1$. Su construcción y caracterización analítica se estudiarán en cálculo/análisis; no se deducen en este capítulo de esa aproximación.

No definiremos $e$ mediante una serie, una integral, un límite de capitalización o una ecuación diferencial. Tampoco definiremos simultáneamente $e$ desde $\ln$ y $\ln$ desde $e$: eso sería circular.

Para la práctica algebraica de este capítulo usamos $e$ como base nombrada y aplicamos las propiedades de exponenciales positivas ya admitidas.

### Definiciones de las funciones

La **exponencial natural** es $\exp:\mathbb R\to(0,\infty)$, $\exp(x)=e^x$. El **logaritmo natural** es $\ln:(0,\infty)\to\mathbb R$, $\ln t=\log_et$.

Como $e>1$, ambas son estrictamente crecientes. Son inversas, con $\ln(\exp x)=x$ para $x\in\mathbb R$ y $\exp(\ln t)=t$ para $t>0$.

Además, $\exp(0)=1$, $\ln1=0$ y $\ln e=1$. Por ejemplo, $\ln(e^{-3})=-3$, aunque el argumento $e^{-3}$ sea positivo.

La escritura $\exp(x)$ hace visible el argumento cuando es largo. $\exp((x+1)/(x-2))$ equivale a $e^{(x+1)/(x-2)}$ y conserva $x\ne2$.

### Leyes ya demostradas, nueva notación

Las leyes de [§23.8](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s08) se aplican a base $e$: $\ln(uv)=\ln u+\ln v$, $\ln(u/v)=\ln u-\ln v$ y $\ln(u^r)=r\ln u$ para $u,v>0$ y $r\in\mathbb R$.

La exponencial satisface $\exp(x+y)=\exp(x)\exp(y)$ y $\exp(-x)=1/\exp(x)$. Estas notaciones no crean leyes nuevas ni eliminan las condiciones de las anteriores.

### Toda base positiva mediante exp

Para $a>0$, la identidad inversa da $a=\exp(\ln a)$. Elevando a $x\in\mathbb R$ y usando la ley de potencia,

$$
a^x=(e^{\ln a})^x=e^{x\ln a}=\exp(x\ln a).
$$

La fórmula también vale para $a=1$, pues $\ln1=0$ y ambos miembros valen $1$. Si queremos invertir $a^x$, vuelve a necesitarse $a\ne1$.

Con $a\ne1$, el cambio de base da $\log_at=\ln t/\ln a$. El signo de $\ln a$ distingue crecimiento ($a>1$) y decrecimiento ($0<a<1$).

### Reparametrizar un modelo

La expresión hipotética $Q(t)=Q_0b^t$, con $Q_0>0,b>0$, puede escribirse $Q(t)=Q_0\exp(kt)$, donde $k=\ln b$. Para $b>1$, $k>0$; para $b<1$, $k<0$; para $b=1$, $k=0$.

Ese $k$ es un parámetro logarítmico del factor por unidad, no el porcentaje $b-1$. En un factor $b=1.10$, el porcentaje por paso es $10\%$, mientras $k=\ln(1.10)$. La distinción es algebraica; no requiere introducir derivadas ni tasas instantáneas.

### Prueba de estrés

Sustituir $e$ por $2.71828$ da aproximaciones a valores de $\exp$, no identidades exactas de la función. Por eso $\ln e=1$ es exacto, mientras $\ln(2.71828)$ sólo es próximo a $1$.

Tampoco $\ln(x+y)$ se convierte en $\ln x+\ln y$ por ser «natural». Las mismas restricciones y falsas leyes siguen vigentes.

### Recuperación breve

Escriba $5^{2x-1}$ mediante $\exp$ y evalúe $\ln(\sqrt e)$.

**Respuesta razonada.** La primera expresión es $\exp((2x-1)\ln5)$ para todo real $x$. La segunda vale $1/2$ porque $\sqrt e=e^{1/2}$ y $\ln(e^{1/2})=1/2$. Ambas conclusiones son exactas y no usan el decimal de $e$.

### Qué debemos conservar

exp y ln nombran una pareja inversa en base $e$. La constante se introduce sin simular su construcción analítica. El cambio de base permite expresar cualquier exponencial positiva mediante exp y cualquier logaritmo válido mediante ln.



## 23.11. Ecuaciones exponenciales {#apm-c23-s11}

Resolver una ecuación exponencial significa determinar exactamente los valores del dominio que igualan dos expresiones. La variable en el exponente cambia las herramientas disponibles, pero no el objeto de resolución de C21.

### Primero positividad

En $4\,3^{x-1}+2=14$, restar $2$ y dividir por $4$ da $3^{x-1}=3$. Como la base es válida, inyectividad da $x-1=1$, así que $x=2$. La sustitución produce $4\cdot3+2=14$.

Si el segundo miembro hubiera sido $-2$, obtendríamos $3^{x-1}=-1$, imposible por positividad. No tomamos logaritmos de ese valor negativo; decidimos que no existe solución real.

En general, para $Aa^{kx+h}+B=C$ con $A\ne0$, primero se aísla $a^{kx+h}=(C-B)/A$. Si ese cociente es no positivo, no hay soluciones. Si es positivo, se puede usar el logaritmo y resolver la condición sobre el argumento.

### Bases comunes

La ecuación $9^{x+1}=3^{4x-2}$ se reescribe $3^{2x+2}=3^{4x-2}$ mediante $(a^u)^v=a^{uv}$. Inyectividad da $2x+2=4x-2$ y por tanto $x=2$. Ambas expresiones originales valen $9^3=3^6$.

La transformación conserva toda la información porque la exponencial de base $3$ es inyectiva sobre todos los exponentes reales.

### Cuando no aparece una potencia conocida

Para $5^{2x-1}=7$, la definición inversa da $2x-1=\log_57$, así que $x=(1+\log_57)/2$. También puede escribirse $(1+\ln7/\ln5)/2$.

La solución es exacta. La verificación simbólica usa $5^{\log_57}=7$, sin decimales. Una aproximación puede ayudar a ubicar el valor, pero no es necesaria para declarar el conjunto solución.

### Bases diferentes con variable en ambos exponentes

En $2^x=3^{x-1}$, ambos miembros son positivos. Aplicar ln es una equivalencia por inyectividad y da $x\ln2=(x-1)\ln3$. Reunir términos produce $x(\ln3-\ln2)=\ln3$.

El coeficiente $\ln3-\ln2=\ln(3/2)>0$, así que no es cero. La solución es $x=\ln3/\ln(3/2)$. Se puede verificar sustituyendo esta relación en la igualdad de logaritmos y recuperando la igualdad original con exp.

### Sustitución positiva

Para $4^x-6\cdot2^x+8=0$, se usa $4^x=(2^x)^2$. La auxiliar $u=2^x$ recorre $(0,\infty)$ y la ecuación es $(u-2)(u-4)=0$.

Ambos candidatos auxiliares son positivos. Reconstruir $2^x=2$ y $2^x=4$ da $x=1,2$, de modo que $S=\{1,2\}$. La sustitución es biyectiva entre $\mathbb R$ y los positivos, por lo que cada $u$ válido tiene exactamente una preimagen.

Si una ecuación auxiliar diera $u=-2$, esa rama no tendría preimagen real. No se intenta escribir un logaritmo real de $-2$ ni se conserva ese candidato en el conjunto original.

### Factores que nunca se anulan

En $(x-1)e^{2x}=0$, la exponencial es estrictamente positiva. Dividir por ella es reversible y queda $x-1=0$. El conjunto solución es $\{1\}$.

La ecuación $e^{2x}=0$ no aporta una rama; sabemos de antemano que es imposible. Reconocer ese factor puede simplificar una resolución sin introducir candidatos adicionales.

### Prueba de estrés: no tomar logaritmo de una suma por partes

En $2^x+3^x=5$, no podemos escribir $x\ln2+x\ln3=\ln5$: eso reemplazaría logaritmo de suma por suma de logaritmos.

Aquí $x=1$ es solución. Además, la suma de dos funciones estrictamente crecientes es estrictamente creciente: si $u<v$, cada sumando en $u$ es menor que el correspondiente en $v$, y sumar conserva una desigualdad estricta. Por tanto, la solución es única y $S=\{1\}$. Se eligió una ruta distinta porque las leyes no autorizaban la primera.

### Recuperación breve

Resuelva $e^{2x}-3e^x-4=0$.

**Respuesta razonada.** Con $u=e^x>0$, queda $(u-4)(u+1)=0$. Se descarta $u=-1$ por imagen y se conserva $u=4$. La vuelta da $x=\ln4$. Sustituir produce $16-12-4=0$, y la biyectividad de exp demuestra que no se omitieron otras soluciones.

### Qué debemos conservar

Una ecuación exponencial se resuelve mediante forma e imagen: bases comunes, logaritmos de valores positivos, sustituciones positivas o factores que nunca se anulan. Cada ruta necesita una equivalencia y una vuelta completa al dominio original.



## 23.12. Ecuaciones logarítmicas {#apm-c23-s12}

El riesgo principal de una ecuación logarítmica es borrar el dominio al condensar o al aplicar la función inversa. La condición de positividad debe fijarse antes de transformar.

### Una ecuación directa

Para $\ln(2x-3)=\ln7$, el dominio exige $2x-3>0$, esto es $x>3/2$. Por inyectividad de ln, la ecuación equivale allí a $2x-3=7$. Así, $x=5$, que pertenece al dominio y satisface la original.

Si aparece $\ln(2x-3)=0$, escribimos $0=\ln1$ y obtenemos $x=2$. Un logaritmo cero corresponde a argumento uno, nunca a argumento cero.

### Suma de logaritmos y candidatos

Resolvamos $\log_2(x-1)+\log_2(x+1)=3$. Las dos condiciones de dominio dan $x>1$. Sobre ese conjunto, condensar es válido y produce $\log_2(x^2-1)=3$.

La definición da $x^2-1=8$, así que los candidatos algebraicos son $\pm3$. Sólo $3$ pertenece al dominio original. En él, $\log_22+\log_24=1+2=3$. Por tanto, $S=\{3\}$.

La ecuación condensada considerada aisladamente también tendría sentido en $x<-1$. Eso no autoriza incorporar $-3$: el problema inicial requería dos argumentos positivos separados.

### Diferencia de logaritmos

Para $\ln(x+4)-\ln(x-1)=\ln2$, el dominio común es $x>1$. La ley de cociente da $\ln((x+4)/(x-1))=\ln2$ y la inyectividad da $(x+4)/(x-1)=2$.

Multiplicar por $x-1\ne0$ es reversible en ese dominio. Queda $x+4=2x-2$ y $x=6$. La comprobación usa $10/5=2$. La solución es $\{6\}$.

No se exige que $\ln(x-1)$ sea positivo: aquí se resta su valor, no se usa como argumento de otro logaritmo.

### Potencia del valor logarítmico

En $(\ln x)^2-3\ln x+2=0$, el dominio es $x>0$. Definimos $u=\ln x$, que puede recorrer todo $\mathbb R$. La ecuación $(u-1)(u-2)=0$ da $u=1$ o $u=2$, de donde $x=e$ o $x=e^2$.

La imagen auxiliar es distinta de la de $u=e^x$: un logaritmo puede ser negativo o cero. Las restricciones de la sustitución provienen de la función escogida, no de una receta universal.

### Composiciones logarítmicas

Para $\ln(\ln x)=0$, el dominio exige $x>0$ y $\ln x>0$, es decir $x>1$. Aplicar exp da $\ln x=1$ y una segunda aplicación da $x=e$. El resultado está en el dominio porque $e>1$.

El razonamiento hace visibles las dos capas y sus argumentos. No se «eliminan» dos símbolos de ln en un mismo paso.

### Base variable

En $\log_x27=3$, se exige $x>0$, $x\ne1$. La forma exponencial da $x^3=27$, con único candidato real $x=3$, que es base válida.

En $\log_x1=0$, todo $x>0$, $x\ne1$ sirve: para cada base válida, el exponente que produce uno es cero. La forma exponencial $x^0=1$ no determina una base única. Siempre se conserva el dominio de bases.

### Prueba de estrés: aplicar exp no amplía el dominio

Una resolución de $\ln(x-2)=\ln(4-x)$ que se limita a $x-2=4-x$ obtiene $x=3$. En este caso la respuesta es correcta porque $3$ está en el dominio $(2,4)$, pero la resolución necesita expresar o verificar ese requisito.

La cadena sería inválida para una igualdad con argumentos no positivos: exp no convierte en reales logaritmos que nunca existieron. La admisibilidad es anterior a la aplicación de la inversa.

### Recuperación breve

Resuelva $\ln(x-1)+\ln(x+2)=\ln4$.

**Respuesta razonada.** El dominio es $x>1$. Condensar da $(x-1)(x+2)=4$, equivalente allí a $x^2+x-6=0$, con candidatos $2,-3$. Sólo $2$ es admisible. La sustitución produce $\ln1+\ln4=\ln4$, de modo que $S=\{2\}$. La exclusión de $-3$ conserva los dos argumentos originales.

### Qué debemos conservar

Las ecuaciones logarítmicas empiezan por el dominio. Condensar, aplicar exp o sustituir el valor del logaritmo son operaciones válidas sobre ese dominio, y sus candidatos se reconstruyen con las restricciones originales.



## 23.13. Inequaciones exponenciales y logarítmicas {#apm-c23-s13}

En una ecuación, la inyectividad permite recuperar argumentos iguales. En una inequación, necesitamos además conocer la orientación de la función. Compare $2^x<8$ con $(1/2)^x<8$: ambas tienen una base válida, pero sus conjuntos solución se extienden en sentidos opuestos.

### Transportar el orden mediante una exponencial

Para una base fija $a>0$, $a\ne1$, y argumentos reales $U(x),V(x)$ definidos en un dominio $D$, la monotonía de [§23.3](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s03) da

$$
a^{U(x)}<a^{V(x)}
\Longleftrightarrow
\begin{cases}
U(x)<V(x),&a>1,\\
U(x)>V(x),&0<a<1.
\end{cases}
$$

La equivalencia se afirma sobre $D$. Las relaciones no estrictas incluyen también la igualdad: con base creciente se conserva $\le$; con base decreciente se transforma en $\ge$.

Para $2^{3x-1}\le16$, escribimos $16=2^4$. La base creciente da $3x-1\le4$, de donde $x\le5/3$. Así, $S=(-\infty,5/3]$. En la frontera ambos miembros valen $16$; para cualquier $x$ menor, el exponente es menor o igual que $4$, lo que prueba que se admite toda la semirrecta.

En $(1/2)^{2x+1}<4$, escribimos $4=(1/2)^{-2}$. La base decreciente da $2x+1>-2$, así que $S=(-3/2,\infty)$. La frontera produce igualdad y se excluye.

| Condición | Base y orientación | Condición equivalente | Solución |
|---|---|---|---|
| $2^x<8$ | creciente | $x<3$ | $(-\infty,3)$ |
| $(1/2)^x<8$ | decreciente | $x>-3$ | $(-3,\infty)$ |

La tabla registra el argumento completo de la comparación. La inversión procede de la función decreciente, no de que un exponente concreto sea negativo.

### Comparar con cero o con un número negativo

Para cualquier base positiva, $a^{U(x)}>0$ en todo el dominio de $U$. Por tanto, $a^{U(x)}\le0$ no tiene soluciones y $a^{U(x)}>0$ admite todo ese dominio.

Si el término de comparación es $c>0$, podemos escribir $c=a^{\log_ac}$ y transportar el orden. Si $c\le0$, ese logaritmo real no existe; la positividad ya decide las comparaciones elementales y no debemos intentar aplicar una fórmula fuera de su dominio.

Por ejemplo, $3^x<5$ equivale a $x<\log_35$. La frontera es exacta aunque no se exprese con un decimal. En cambio, $3^x<-5$ tiene solución vacía.

### Logaritmos: dos controles antes de transformar

Para comparar $\log_aU(x)$ y $\log_aV(x)$, ambos argumentos deben ser positivos. Sobre ese dominio común, una base mayor que uno conserva el orden de los argumentos y una base entre cero y uno lo invierte.

La comparación con un real $c$ se obtiene escribiendo $c=\log_a(a^c)$:

$$
\log_aU(x)\le c
\Longleftrightarrow
\begin{cases}
0<U(x)\le a^c,&a>1,\\
U(x)\ge a^c,&0<a<1,
\end{cases}
$$

siempre que $U$ esté definida. En la segunda rama, la condición $U(x)\ge a^c>0$ ya implica positividad. En la primera, la cota superior no basta: debemos mantener también $U(x)>0$.

Por ejemplo, $\log_2(x-1)\le3$ exige $x>1$ y luego $x-1\le8$. Su solución es $(1,9]$, no $(-\infty,9]$. El punto $1$ produce argumento cero y se excluye por dominio; el punto $9$ se incluye porque el logaritmo vale $3$.

Para $\log_{1/2}(x-1)\ge-1$, el dominio vuelve a ser $x>1$. La base decreciente da $x-1\le(1/2)^{-1}=2$. Intersectando, $S=(1,3]$. La relación $\ge$ entre valores se convirtió en $\le$ entre argumentos.

### Un argumento racional

Resolvamos $\log_2((x-1)/(x+2))\ge0$. La expresión interior exige $x\ne-2$ y el logaritmo exige cociente positivo. Como la base es creciente y $0=\log_21$, la condición equivale, en ese dominio, a $(x-1)/(x+2)\ge1$.

Restar $1$ produce $-3/(x+2)\ge0$, que se cumple exactamente si $x<-2$: el numerador es negativo y el denominador debe ser negativo. En esa región, el argumento original es mayor que $1$, así que también satisface el dominio logarítmico.

Por tanto, $S=(-\infty,-2)$. No multiplicamos por $x+2$ sin conocer su signo. La racional se decidió mediante C22, conservando el punto excluido.

### Comparar dos logaritmos con base fraccionaria

Considere $\log_{1/2}(x-1)<\log_{1/2}(5-x)$. El dominio común es $1<x<5$. La monotonía decreciente transforma la condición en $x-1>5-x$, es decir $x>3$.

La intersección con el dominio da $S=(3,5)$. En $3$ los argumentos coinciden y la desigualdad estricta falla; en $5$ el segundo logaritmo no existe. Las dos fronteras son abiertas por motivos diferentes.

### Condiciones compuestas y sistemas

En $-1<\log_2(x-1)\le2$, el dominio exige $x>1$. La función creciente transporta las dos comparaciones a $2^{-1}<x-1\le2^2$. Así, $S=(3/2,5]$. Las condiciones deben cumplirse simultáneamente: forman una intersección, como en C22.

Si añadimos $2^x<16$ a $\log_2(x-1)\ge1$, la primera condición selecciona $x<4$ y la segunda $x\ge3$. El sistema tiene solución $[3,4)$. En $3$ el logaritmo admite igualdad; en $4$ la exponencial no admite igualdad.

La operación que transforma cada condición puede ser distinta, pero el enlace lógico del sistema no cambia.

### Prueba de estrés: invertir dos veces sin motivo

Una resolución de $\log_{1/2}(x+1)<-2$ obtiene correctamente $x+1>4$, pero luego escribe $x<3$ «porque la base es menor que uno». La primera inversión ya incorporó esa información. Restar $1$ conserva el orden, de modo que el resultado correcto es $x>3$.

Para todos esos valores, el argumento supera $4$ y el logaritmo decreciente es menor que $\log_{1/2}4=-2$. En la frontera hay igualdad. Cada inversión debe corresponder a una operación concreta; la base no sigue invirtiendo los pasos algebraicos posteriores.

### Recuperación breve

**a)** Resuelva $(1/3)^{x-2}\ge9$.

**b)** Resuelva $\ln(4-x)<0$ conservando el dominio.

**Respuesta razonada.** En **a)**, $9=(1/3)^{-2}$ y la base decreciente da $x-2\le-2$. Por tanto, $S=(-\infty,0]$; en $0$ se produce igualdad.

En **b)**, el dominio exige $4-x>0$, así que $x<4$. Como ln es creciente y $\ln1=0$, la comparación exige además $4-x<1$, esto es $x>3$. La solución es $(3,4)$. En $3$ el logaritmo vale cero; en $4$ no existe. Ambas fronteras quedan excluidas.

### Qué debemos conservar

La base decide cómo se transporta el orden; el dominio decide dónde ese transporte tiene sentido. Después se resuelven las condiciones algebraicas con las reglas de C22 y se conserva su enlace lógico. Una respuesta completa justifica las regiones admitidas y distingue fronteras excluidas por desigualdad estricta de puntos donde una expresión no está definida.



## 23.14. Sustituciones, parámetros y varias capas {#apm-c23-s14}

La expresión $4^x-5\cdot2^x+4$ contiene una cuadrática, aunque no esté escrita como un polinomio en $x$. Reconocerla permite usar C19–C22. La sustitución debe registrar qué valores puede tomar la nueva variable y cómo se vuelve a la original.

### Exponencial como variable auxiliar

En $4^x-5\cdot2^x+4\le0$, escribimos $4^x=(2^x)^2$ y tomamos $u=2^x$. La auxiliar recorre exactamente $(0,\infty)$ y cada valor positivo tiene una única preimagen $x=\log_2u$.

La inequación se transforma en $(u-1)(u-4)\le0$. Por signos, $1\le u\le4$, intervalo ya contenido en la imagen válida. Al volver, $1\le2^x\le4$ equivale a $0\le x\le2$ por monotonía creciente. Por tanto, $S=[0,2]$.

Los extremos producen cero en la expresión original. Para $x<0$, la auxiliar es menor que $1$ y el producto es positivo; para $x>2$, supera $4$ y vuelve a ser positivo. La reconstrucción demuestra tanto la inclusión del intervalo como la exclusión de sus regiones exteriores.

### Resolver en toda la recta auxiliar no basta

Para $(e^x+2)(e^x-3)<0$, la auxiliar $u=e^x>0$ da formalmente $-2<u<3$. La intersección con su imagen es $(0,3)$, no $(-2,3)$.

Reconstruir $0<e^x<3$ da $x<\ln3$. La cota inferior se cumple para todo real y no produce un extremo finito. Así, $S=(-\infty,\ln3)$.

No escribimos $\ln(-2)$ para transformar la frontera negativa. Esa frontera pertenece al problema polinómico auxiliar, pero no a los valores alcanzables por la exponencial.

### Un logaritmo tiene otra imagen auxiliar

En $(\ln x)^2-\ln x-2\le0$, el dominio inicial es $x>0$. Con $u=\ln x$, la auxiliar puede ser cualquier real. La factorización $(u-2)(u+1)\le0$ da $-1\le u\le2$.

La vuelta mediante exp, que es creciente, produce $e^{-1}\le x\le e^2$. Ambos extremos son positivos y pertenecen al dominio, por lo que $S=[e^{-1},e^2]$.

| Sustitución | Imagen auxiliar | Reconstrucción |
|---|---|---|
| $u=a^x$, base válida | $(0,\infty)$ | $x=\log_au$ |
| $u=\ln x$, $x>0$ | $\mathbb R$ | $x=e^u$ |
| $u=2^{x^2}$ | $[1,\infty)$ | $x^2=\log_2u$, con todas sus raíces reales |

La tercera fila muestra que una composición puede cambiar la imagen y destruir la inyectividad. No todas las sustituciones exponenciales identifican una única preimagen.

### Sustitución no inyectiva

Resolvamos $2^{x^2}\le8$. El dominio es toda $\mathbb R$. Por base creciente, la comparación equivale a $x^2\le3$, de donde $S=[-\sqrt3,\sqrt3]$.

Si se usa $u=2^{x^2}$, su imagen es $[1,\infty)$: el cuadrado es no negativo y cada exponente no negativo tiene preimágenes reales. La condición auxiliar $u\le8$ selecciona $[1,8]$. Reconstruir ese intervalo exige $0\le x^2\le3$ y conserva las dos ramas de $x$.

Elegir sólo $x=\sqrt{\log_2u}$ perdería los valores negativos. La inversa de la exponencial recupera $x^2$, no identifica automáticamente una inversa de toda la composición.

### Parámetro de base: separar regímenes reales

Clasifiquemos $a^x\le a^2$ para $a>0$. El parámetro es una base fija en cada problema; no varía mientras se resuelve para $x$.

Si $a>1$, la monotonía creciente da $x\le2$. Si $0<a<1$, la monotonía decreciente da $x\ge2$. Si $a=1$, ambos miembros valen $1$ y todo real sirve.

$$
S(a)=
\begin{cases}
[2,\infty),&0<a<1,\\
\mathbb R,&a=1,\\
(-\infty,2],&a>1.
\end{cases}
$$

La familia incluye el caso constante como degeneración de las potencias positivas. No lo tratamos como una función exponencial invertible. Para $a\le0$, la expresión no pertenece a esta familia real definida para todos los exponentes.

Si el problema fuera $\log_a x\le2$, el caso $a=1$ estaría fuera del dominio de bases, no daría toda la recta. Para $a>1$, se obtiene $0<x\le a^2$; para $0<a<1$, $x\ge a^2$. La existencia de la expresión determina qué casos paramétricos se pueden resolver.

### Un parámetro en el término de comparación

En $e^x\le c$, con $c\in\mathbb R$, la positividad da solución vacía si $c\le0$. Si $c>0$, ln es aplicable y creciente: $x\le\ln c$. Por tanto, $S(c)=(-\infty,\ln c]$ en ese régimen.

En $c=0$ no aparece una solución aislada ni un extremo llamado «$\ln0$». El cambio de régimen proviene de la imagen de exp. Las fronteras paramétricas deben justificarse por una propiedad, no añadirse mecánicamente a una lista de casos.

### Varias capas: un logaritmo en un denominador

Considere $1/(\ln x-1)\ge0$. El dominio exige $x>0$ y $\ln x\ne1$, es decir $x\ne e$. Como el numerador es positivo, el cociente sólo puede ser no negativo si el denominador es positivo; nunca vale cero.

Así, $\ln x>1$ y la monotonía de exp da $x>e$. La solución es $(e,\infty)$, con extremo abierto pese a la relación no estricta. La razón es que $e$ anula el denominador, no que falle una comparación numérica definida.

Si añadimos $\ln x\le2$, el sistema selecciona $(e,e^2]$. Cada capa conserva su condición y la simultaneidad termina en una intersección.

### Prueba de estrés: condensar antes de fijar dominio

Para $\ln(x-1)+\ln(x+1)\le\ln3$, el dominio inicial es $x>1$. Allí se puede condensar y comparar argumentos: $x^2-1\le3$, equivalente a $-2\le x\le2$. La intersección da $S=(1,2]$.

Responder $[-2,2]$ pierde el dominio. Incluso resolver el logaritmo condensado por su propio dominio daría una región negativa adicional, porque $x^2-1$ también es positivo para $x<-1$. Esa región nunca perteneció a la suma de los dos logaritmos originales.

La primera operación válida no borra las hipótesis que la autorizaron. Una cadena de varias capas conserva el dominio desde el principio hasta la respuesta.

### Recuperación breve

**a)** Resuelva $(2^x)^2-2^x-6\ge0$.

**b)** Clasifique $b^x=4$ para bases $b>0$, incluido el caso constante.

**Respuesta razonada.** En **a)**, $u=2^x>0$ da $(u-3)(u+2)\ge0$. La solución auxiliar en toda la recta es $u\le-2$ o $u\ge3$; la imagen positiva conserva sólo $u\ge3$. La vuelta da $S=[\log_23,\infty)$. En el extremo, $u=3$ anula el producto, y para valores mayores ambos factores son positivos.

En **b)**, si $b\ne1$, la imagen positiva y la inyectividad garantizan exactamente una solución $x=\log_b4$. Es positiva para $b>1$ y negativa para $0<b<1$, por el signo del logaritmo. Si $b=1$, la igualdad sería $1=4$, falsa para todo real: la solución es vacía.

### Qué debemos conservar

Una sustitución se justifica por la estructura que revela, su imagen y la reconstrucción de todas las preimágenes. Un parámetro exige separar los regímenes donde cambian definición, orientación o existencia de soluciones. En expresiones de varias capas, esas obligaciones se acumulan: cada transformación conserva las condiciones que la hicieron válida.



## 23.15. Modelos multiplicativos y laboratorio de errores {#apm-c23-s15}

Una cantidad hipotética comienza en $80$ y aumenta un $25\%$ en cada paso. Después del primer paso vale $100$; después del segundo, $125$. El incremento absoluto cambió, pero el cociente entre valores consecutivos siguió siendo $5/4$. La función exponencial expresa esa regla multiplicativa.

### Del paso repetido a la fórmula

Si $Q_0>0$ es el valor inicial y $b>0$ el factor por paso, la regla $Q(n+1)=bQ(n)$ da $Q(n)=Q_0b^n$ para enteros $n\ge0$. La fórmula se justifica por inducción: en $n=0$ vale $Q_0b^0=Q_0$; si vale en $n$, multiplicar por $b$ produce $Q_0b^{n+1}$.

Para el ejemplo, $Q(n)=80(5/4)^n$. El porcentaje de aumento es $b-1=1/4$, mientras el factor es $b=5/4$. Si disminuyera un $25\%$ por paso, el factor sería $3/4$.

| Paso $n$ | $Q(n)$ | Incremento desde el paso anterior |
|---:|---:|---:|
| $0$ | $80$ | — |
| $1$ | $100$ | $20$ |
| $2$ | $125$ | $25$ |
| $3$ | $625/4$ | $125/4$ |

La constancia del cociente caracteriza la regla estipulada. Una tabla con unos pocos valores puede sugerir un modelo; no demuestra que una situación real lo obedezca en todos los pasos.

### Extender el modelo exige una decisión

La regla de pasos enteros no determina por sí sola los valores entre pasos. Si elegimos el modelo exponencial para tiempo real, escribimos $Q(t)=Q_0b^t$, normalmente con $t\ge0$. Esta elección utiliza la extensión real de [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02) y agrega una hipótesis al modelo discreto.

Podrían existir otras funciones que coincidieran en tiempos enteros y difirieran entre ellos. No afirmamos que el proceso discreto haya probado la interpolación exponencial.

En el modelo elegido, avanzar una cantidad fija $h$ de tiempo multiplica por $b^h$, pues $Q(t+h)/Q(t)=b^h$. El cociente es independiente de $t$, siempre que ambos tiempos pertenezcan al dominio del modelo.

### Cambiar la unidad de tiempo

Suponga que una cantidad se duplica cada tres horas. Si $t$ mide horas, el modelo exponencial es $Q(t)=Q_0\,2^{t/3}$. En tres horas el exponente aumenta una unidad y el factor es $2$.

Si $s$ cuenta períodos de tres horas, entonces $t=3s$ y la misma cantidad se escribe $Q=Q_0\,2^s$. Son dos coordenadas temporales para el mismo modelo.

Escribir $Q_0\,2^{3t}$ cuando $t$ mide horas describiría otra regla: al avanzar una hora, el factor sería $8$. La fracción $t/3$ cuenta cuántos períodos de tres horas han transcurrido; el exponente es adimensional.

### Tiempo de duplicación y semivida

Para $Q(t)=Q_0b^t$ con $b>1$, el tiempo de duplicación $T$ satisface $Q(T)=2Q_0$. Dividir por $Q_0>0$ y tomar ln da $T\ln b=\ln2$, así que $T=\ln2/\ln b>0$.

Para $0<b<1$, el tiempo de reducción a la mitad $H$ satisface $b^H=1/2$. Por tanto, $H=\ln(1/2)/\ln b=-\ln2/\ln b>0$: numerador y denominador son negativos.

Estas fórmulas son propiedades del modelo, no datos de una sustancia real. Si el tiempo se restringe a pasos enteros, el valor real obtenido puede no ser un instante permitido; se debe distinguir igualdad exacta de primer paso en que se supera un umbral.

### Umbral real y primer paso entero

En el modelo $Q(t)=30\,2^{t/2}$, con $t\ge0$ medido en horas, queremos $Q(t)\ge100$. Dividir por $30$ y aplicar el logaritmo creciente da $t/2\ge\log_2(10/3)$, de modo que $t\ge2\log_2(10/3)$.

Si sólo observamos en horas enteras, comprobamos $Q(3)=60\sqrt2<100$ y $Q(4)=120>100$. La primera comparación es exacta: $60\sqrt2<100$ equivale, entre positivos, a $7200<10000$. Como el modelo es creciente, el primer entero admisible es $4$.

No redondeamos al entero más cercano: buscamos el primer entero que cumple la desigualdad. La condición del problema decide cómo pasar de tiempo real a una observación discreta.

### Inferir un modelo exponencial de dos valores

Dentro de la familia $Q(t)=Cb^t$ con $C>0,b>0$, suponga $Q(1)=12$ y $Q(3)=27$. Dividir las ecuaciones da $b^2=27/12=9/4$. La base positiva obliga a $b=3/2$ y luego $C=12/(3/2)=8$.

Así, el único miembro de esa familia que cumple los datos es $Q(t)=8(3/2)^t$. La comprobación produce $12$ y $27$ en los tiempos indicados.

La unicidad se refiere a la familia elegida. Dos datos no prueban que el fenómeno sea exponencial ni excluyen todas las demás familias funcionales.

### Laboratorio: localizar la primera ruptura

**Error de factor.** Una resolución dice: «aumentar un $20\%$ por paso da $Q(n)=Q_0(0.20)^n$». La primera ruptura es confundir la parte añadida con el valor que permanece después de añadirla. La reparación es $Q_0(1.20)^n$. Para $n=1$, la fórmula errónea reduce al $20\%$ el valor inicial en vez de aumentarlo.

**Error de unidad.** «Duplicar cada cuatro pasos da $Q(n)=Q_0\,2^{4n}$». El exponente debe contar períodos de cuatro pasos: $n/4$. La reparación $Q_0\,2^{n/4}$ da $2Q_0$ en $n=4$; la fórmula errónea daría $2^{16}Q_0$.

**Error de ley.** De $2^x+2=10$ se escribe $x\ln2+\ln2=\ln10$. El primer paso inválido distribuye ln sobre una suma. Debemos aislar $2^x=8$ y usar inyectividad para obtener $x=3$. La sustitución da $8+2=10$.

**Error de dominio.** Se afirma $\ln(x^2)=2\ln x$ para todo $x\ne0$. La ley de potencia usada con base $x$ exige $x>0$. Sobre el dominio completo del miembro izquierdo, la reparación es $\ln(x^2)=2\ln|x|$. En $x=-1$, el miembro izquierdo existe y vale cero, mientras $\ln x$ no existe.

**Error de orientación.** De $(1/5)^x<(1/5)^2$ se concluye $x<2$. La función es decreciente y exige $x>2$. Para $x=3$, la comparación original es verdadera y la respuesta errónea excluye una solución.

En cada caso, un contraejemplo muestra que la respuesta falla; la reparación requiere además una regla válida que caracterice todas las soluciones o todos los valores del modelo.

### Prueba de estrés: tasa porcentual y parámetro logarítmico

Escribir $Q(t)=Q_0e^{kt}$ y $Q(t)=Q_0b^t$ describe el mismo modelo si $k=\ln b$. El aumento porcentual por unidad es $b-1=e^k-1$, no $k$.

Para un factor $b=2$, el aumento por unidad es $100\%$ y el parámetro logarítmico es $\ln2$. Son números distintos. La igualdad de modelos se demuestra mediante $b^t=e^{t\ln b}$; no se obtiene identificando indebidamente sus parámetros.

### Recuperación breve

**a)** Una cantidad hipotética comienza en $96$ y conserva tres cuartas partes de su valor en cada paso. Escriba el modelo discreto y calcule los dos primeros valores posteriores al inicial.

**b)** Una cantidad se triplica cada dos horas según un modelo exponencial de tiempo real. Determine cuándo alcanza nueve veces su valor inicial.

**Respuesta razonada.** En **a)**, $Q(n)=96(3/4)^n$ para enteros $n\ge0$. Los valores son $72$ y $54$; en cada paso se pierde una cuarta parte del valor presente, no una cantidad absoluta fija.

En **b)**, $Q(t)=Q_0\,3^{t/2}$ con $Q_0>0$ y $t\ge0$ medido en horas. La condición $Q(t)=9Q_0$ equivale a $3^{t/2}=3^2$. Inyectividad da $t/2=2$ y $t=4$ horas. La sustitución produce exactamente el factor $9$.

### Qué debemos conservar

Un modelo multiplicativo conserva un factor por períodos iguales. Su uso exige declarar valor inicial, factor, unidad temporal y dominio; la extensión entre pasos es una hipótesis adicional. Los logaritmos recuperan tiempos y parámetros, mientras el diagnóstico controla leyes, dominios y orientación en cada transición.



### Un ajuste exacto no demuestra una ley universal

Dos datos positivos en tiempos diferentes pueden fijar $Q_0$ y $b$ en un modelo $Q(t)=Q_0b^t$. Un tercer dato prueba compatibilidad con esa elección, no la validez del modelo para todo tiempo. **Control resuelto:** $Q(0)=6$, $Q(1)=9$ fuerzan $b=3/2$, y predicen $Q(2)=27/2$. Si el tercer dato es $14$, el modelo no ajusta los tres exactamente. Incluso tres coincidencias permiten otras funciones entre los tiempos observados. Debemos indicar además si $t$ cuenta pasos enteros o tiempo continuo y cuál es su unidad: cambiar de horas a minutos cambia el exponente, no el proceso. La distinción entre datos, parámetros e hipótesis de extensión evita atribuir a una tabla una demostración que no proporciona.



## 23.16. Síntesis y puente al álgebra polinómica {#apm-c23-s16}

En este capítulo hemos aprendido a recuperar exponentes, transportar comparaciones y reconocer estructuras algebraicas dentro de expresiones exponenciales y logarítmicas. La dificultad final consiste en elegir qué herramienta aplicar sin perder las condiciones que sostienen el argumento.

Considere $\ln(4^x-5\cdot2^x+4)\le\ln4$. Antes de aplicar una ley, debemos preguntar dónde existe el logaritmo y qué forma tiene su argumento. La factorización y la monotonía resuelven obligaciones diferentes; ninguna sustituye a la otra.

### Organizar una resolución autónoma

El primer dato es el dominio original. Para cada logaritmo se exige base válida y argumento positivo; para cada denominador, valor no nulo; para cada composición, las condiciones de todas sus capas.

Después se identifica la estructura: bases comunes, una potencia de otra exponencial, un polinomio en un valor logarítmico, una comparación que se transporta por monotonía o una familia que cambia según el parámetro. La forma elegida debe hacer visible esa estructura.

Cada transición necesita una razón. Aplicar una función inyectiva a una igualdad puede conservarla como equivalencia; aplicarla a una desigualdad exige además su orientación. Expandir un logaritmo requiere argumentos positivos. Dividir exige un factor no nulo y, para orden, conocer su signo.

Una sustitución añade la obligación de registrar su imagen y reconstruir todas las preimágenes. Al final se declara un conjunto en la variable original, conservando los puntos excluidos y la unión o intersección que exige el problema.

| Pregunta | Evidencia que debe aparecer |
|---|---|
| ¿Dónde tiene sentido el problema? | dominio de las expresiones originales |
| ¿Qué estructura permite avanzar? | forma equivalente y herramienta disponible |
| ¿Por qué vale el paso? | hipótesis de ley, inyectividad, monotonía o signo |
| ¿Qué valores admite la auxiliar? | imagen y restricciones heredadas |
| ¿Cómo volvemos a la variable original? | preimágenes completas |
| ¿Por qué ésta es toda la solución? | prueba de regiones y control de fronteras |

Estas preguntas organizan el razonamiento; no obligan a escribir una plantilla larga para un problema sencillo. En una síntesis de varias capas, permiten detectar qué información aún falta.

### Síntesis: logaritmo de un polinomio en una exponencial

Resolvamos la condición inicial. El dominio exige $4^x-5\cdot2^x+4>0$. Como ln es creciente y ambos argumentos deben ser positivos, la inequación equivale a

$$
0<4^x-5\cdot2^x+4\le4.
$$

Tomamos $u=2^x>0$, de modo que $4^x=u^2$. Debemos resolver simultáneamente $u^2-5u+4>0$ y $u^2-5u+4\le4$.

La primera condición se factoriza como $(u-1)(u-4)>0$. En la imagen positiva selecciona $0<u<1$ o $u>4$.

La segunda se reduce a $u(u-5)\le0$. En la imagen positiva, equivale a $0<u\le5$. Intersectando ambas condiciones, obtenemos $S_u=(0,1)\cup(4,5]$.

La vuelta mediante la exponencial de base $2$, creciente y biyectiva hacia los positivos, da $x<0$ o $2<x\le\log_25$. Por tanto,

$$
S=(-\infty,0)\cup(2,\log_25].
$$

El orden de las fronteras está justificado: $5>4$ implica $\log_25>2$.

### Verificar regiones y extremos de la síntesis

Si $x<0$, entonces $0<u<1$. El producto $(u-1)(u-4)$ es positivo y $u(u-5)<0$, así que el argumento del logaritmo está estrictamente entre $0$ y $4$. La condición original es verdadera en toda esa región.

Si $2<x\le\log_25$, tenemos $4<u\le5$. El argumento vuelve a ser positivo y no excede $4$. En el extremo superior, $u=5$ produce argumento $4$, de modo que la igualdad se admite.

Los puntos $x=0$ y $x=2$ producen argumento cero: allí el logaritmo no existe. No son fronteras excluidas por una desigualdad estricta entre valores definidos. Entre esos puntos, $1<u<4$ produce argumento negativo. Para $x>\log_25$, el argumento es mayor que $4$ y la comparación falla.

Esta verificación separa inadmisibilidad de dominio y falsedad de una condición definida. La biyectividad de la sustitución garantiza que todas las regiones auxiliares se reconstruyeron.

### Otra ruta: resolver primero el dominio en x

Podemos empezar por el dominio: $(2^x-1)(2^x-4)>0$ equivale a $x<0$ o $x>2$.

Dentro de ese dominio, ln creciente permite comparar el argumento con $4$. La condición restante es $2^x(2^x-5)\le0$. Dividir por $2^x>0$ conserva la relación y da $2^x\le5$, esto es $x\le\log_25$.

Intersectar esta semirrecta con el dominio anterior recupera $(-\infty,0)\cup(2,\log_25]$. La primera ruta reunió las condiciones en la auxiliar; la segunda resolvió por separado dominio y comparación. Ambas conservan exactamente las mismas obligaciones.

### El alcance de una sustitución algebraica

La expresión $4^x-5\cdot2^x+4$ es un polinomio en $2^x$: si $P(u)=u^2-5u+4$, la expresión es $P(2^x)$. No es por ello un polinomio en $x$.

En el anillo de expresiones polinómicas que estudiaremos, un polinomio en $x$ combina coeficientes con potencias enteras no negativas de $x$ mediante una suma finita. La posición exponencial de $x$ pertenece a otra estructura. Reemplazar $2^x$ por $u$ permite resolver un problema polinómico auxiliar, pero no cambia el tipo de la función original.

Las identidades, factorizaciones y reglas de signo de C19–C22 ya han proporcionado herramientas para esa auxiliar. C24 estudiará sistemáticamente el objeto polinomio y sus operaciones, incluida la división. C25 desarrollará raíces, factores e irreducibilidad. La función logarítmica seguirá siendo la herramienta para reconstruir el exponente después de resolver en la imagen positiva.

### Qué se demostró y qué se admitió

Las leyes de logaritmos, el cambio de base, la monotonía de la inversa y las transformaciones usadas en esta síntesis se demostraron a partir de las propiedades exponenciales declaradas.

La construcción de la exponencial real, con sus leyes fundamentales, monotonía e imagen positiva, se admitió explícitamente en [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02). Nombrar e y usar exp y ln no equivale a haber construido analíticamente esa constante o esas funciones.

Esta frontera permite reconocer qué podemos justificar con el álgebra disponible y qué queda para cálculo/análisis. Una gráfica, una tabla o un decimal puede ilustrar o comprobar un caso; no reemplaza la prueba de existencia diferida.

### Prueba de estrés de la estrategia

Resolvamos $\ln((e^x-1)^2)\le0$. La exponencial existe para todo real, pero el logaritmo exige $e^x\ne1$, es decir $x\ne0$.

Como ln es creciente, la condición equivale a $0<(e^x-1)^2\le1$. Con $u=e^x>0$, la cota superior exige $|u-1|\le1$, es decir $0\le u\le2$. Se conserva $u>0$ y se excluye $u=1$, de modo que $S_u=(0,1)\cup(1,2]$.

La vuelta da $S=(-\infty,0)\cup(0,\ln2]$. El punto $0$ permanece excluido aunque una expansión incorrecta del logaritmo pudiera ocultarlo. La identidad válida es $\ln((e^x-1)^2)=2\ln|e^x-1|$ para $x\ne0$; escribir $2\ln(e^x-1)$ perdería toda la rama negativa de x.

### Recuperación breve

Resuelva $\ln((2^x-1)/(2^x+1))\ge-\ln3$ y verifique la frontera.

**Respuesta razonada.** El denominador $2^x+1$ es positivo para todo real. El argumento del logaritmo es positivo exactamente si $2^x>1$, de modo que el dominio es $x>0$.

Como $-\ln3=\ln(1/3)$ y ln es creciente, la comparación equivale en ese dominio a $(2^x-1)/(2^x+1)\ge1/3$. Multiplicar por el denominador positivo y por $3>0$ da $3(2^x-1)\ge2^x+1$, equivalente a $2^x\ge2$. Por monotonía, $x\ge1$, condición que ya respeta el dominio.

Así, $S=[1,\infty)$. En $x=1$, el cociente es $1/3$ y los dos miembros logarítmicos coinciden. Para $x>1$, el argumento es mayor que $1/3$, como muestra la misma cadena reversible. Los valores $0<x<1$ incumplen la comparación y los valores $x\le0$ no pertenecen al dominio.

### Qué debemos conservar del capítulo

Exponenciales y logaritmos relacionan exponentes, productos y orden mediante funciones inversas con dominios precisos. La base gobierna la orientación; la imagen decide qué valores pueden reconstruirse; las leyes cambian la forma sin ampliar el dominio. Resolver requiere conservar esos datos hasta declarar el conjunto solución.

El paso hacia los polinomios prolonga una práctica ya adquirida: reconocer una estructura, elegir una forma útil y justificar cada operación. Ahora estudiaremos ese objeto algebraico por derecho propio, con sus operaciones y algoritmos.

## Ejercicios

Intente resolver cada ejercicio antes de consultar su solución. Conserve las condiciones de base y dominio en las traducciones y simplificaciones.

### A. Lectura



#### Ejercicio 1

Compare $f(x)=x^4$ y $g(x)=4^x$. Identifique qué papel ocupa la variable en cada expresión y dé un valor de $x$ que muestre que no son la misma función.



#### Ejercicio 2

Entre $a=-2,0,1,1/4,3$, identifique las bases que definen una función exponencial real invertible sobre todo $\mathbb R$. Explique qué ocurre con las restantes.



#### Ejercicio 3

Traduzca $5^{-2}=1/25$ a forma logarítmica. Identifique base, argumento y valor del logaritmo.



#### Ejercicio 4

Determine si están definidas en los reales las expresiones $\log_2(-4)$, $\log_2(1/4)$ y $\log_1 4$. Evalúe la que corresponda.



#### Ejercicio 5

Escriba el dominio y la imagen de $E_3(x)=3^x$ y de su inversa $L_3(t)=\log_3t$. Indique qué pares corresponden a $(2,9)$.



#### Ejercicio 6

Para $\log_2(x-4)$, explique por qué no basta excluir $x=4$ y determine el dominio.



#### Ejercicio 7

Determine el dominio de $F(x)=2^{\log_2(x+3)}$ y la fórmula que resulta al componer las funciones inversas. ¿Esa fórmula amplía el dominio de $F$?



#### Ejercicio 8

Sin calcular decimales, compare $(1/3)^2$ con $(1/3)^5$, y $\log_{1/3}2$ con $\log_{1/3}7$. Indique la propiedad usada.



#### Ejercicio 9

Una cantidad hipotética comienza en $60$ y conserva el $80\%$ de su valor en cada paso entero. Identifique valor inicial, factor y porcentaje de disminución; escriba el modelo y el valor tras un paso.



#### Ejercicio 10

En la sustitución $u=e^x$, ¿qué valores reales puede tomar $u$? Si una ecuación auxiliar ofrece $u=-1$ o $u=4$, determine qué candidatos se reconstruyen y cómo.

### B. Fluidez

Practique las leyes y las funciones inversas conservando sus hipótesis. En ecuaciones e inequaciones, declare el conjunto solución.



#### Ejercicio 11

Evalúe exactamente $27^{2/3}$, $16^{-3/4}$ y $(1/9)^{-1/2}$.



#### Ejercicio 12

Evalúe $\log_4(1/8)$, $\log_{1/2}8$ y $\log_9 3$ sin aproximaciones decimales.



#### Ejercicio 13

Simplifique $5^{2t-1}5^{3-t}/5^{t+1}$ para $t\in\mathbb R$.



#### Ejercicio 14

Simplifique $\ln(e^{3x-2})$ y $e^{\ln(x^2-4)}$, indicando el dominio de cada expresión original.



#### Ejercicio 15

Expanda $\log_3(9x^2/\sqrt y)$ para $x\ne0$ e $y>0$. Conserve una fórmula válida también cuando $x<0$.



#### Ejercicio 16

Condense $2\ln(x-1)-\ln(x+2)$ en un solo logaritmo y determine el dominio que debe acompañar a la fórmula.



#### Ejercicio 17

Escriba $\log_7 20$ mediante ln y calcule exactamente $\log_8 32$ usando cambio de base.



#### Ejercicio 18

Resuelva en $\mathbb R$ la ecuación $9^{x-1}=27^{2x+1}$.



#### Ejercicio 19

Resuelva $5\,2^{x+1}=30$ y dé la solución exacta.



#### Ejercicio 20

Resuelva $e^{2x}-5e^x+6=0$ y reconstruya todas las soluciones reales.



#### Ejercicio 21

Resuelva $\log_3(2x-1)=2$ y compruebe el dominio.



#### Ejercicio 22

Resuelva $\ln(x+3)=\ln(2x-1)$.



#### Ejercicio 23

Resuelva $\log_2(x-1)+\log_2(x+1)=3$, conservando el dominio antes de condensar.



#### Ejercicio 24

Resuelva $(1/4)^{2x-1}\ge8$ y escriba el resultado como intervalo.



#### Ejercicio 25

Resuelva $\log_{1/2}(x-2)<-1$, distinguiendo dominio y comparación.



#### Ejercicio 26

Resuelva la condición compuesta $0\le\ln(x+1)<\ln4$ y compruebe ambos extremos.

### C. Justificación

En cada argumento, identifique las hipótesis que hacen posibles las expresiones y las propiedades que autorizan las transformaciones. Una equivalencia debe conservar el dominio y justificarse en ambos sentidos.



#### Ejercicio 27

Sean $a>0$, $a\ne1$ y $u,v>0$. Demuestre $\log_a(uv)=\log_a u+\log_a v$ a partir de las leyes exponenciales y la definición de inversa. Indique dónde se utiliza cada hipótesis.



#### Ejercicio 28

Con $a>0$, $a\ne1$ y $u,v>0$, demuestre la ley $\log_a(u/v)=\log_a u-\log_a v$. Explique por qué la sola condición $u/v>0$ no basta para que la igualdad escrita tenga sentido.



#### Ejercicio 29

Para $a>0$, $a\ne1$, $u>0$ y $r\in\mathbb R$, demuestre $\log_a(u^r)=r\log_a u$. Separe las propiedades exponenciales admitidas del argumento que demuestra esta consecuencia.



#### Ejercicio 30

Demuestre que $\ln(x^2)=2\ln|x|$ para todo $x\ne0$. Determine en qué dominio puede reemplazarse $|x|$ por $x$ y dé un contraejemplo a ese reemplazo fuera de dicho dominio.



#### Ejercicio 31

Demuestre que el logaritmo de base $a>1$ es estrictamente creciente y el de base $0<a<1$ es estrictamente decreciente. Puede usar la monotonía de la exponencial, pero no asumir la monotonía de su inversa.



#### Ejercicio 32

Sean $a,b>0$, $a\ne1$, $b\ne1$ y $u>0$. Demuestre la fórmula de cambio de base $\log_a u=\log_b u/\log_b a$ y justifique que el denominador no es cero.



#### Ejercicio 33

Demuestre $a^x=e^{x\ln a}$ para $a>0$ y $x\in\mathbb R$. ¿Debe excluirse $a=1$ en esta identidad? Justifique su respuesta sin usar límites ni series.



#### Ejercicio 34

Para $a>0$ fijo y $p,q\in\mathbb R$, justifique la equivalencia $a^p=a^q\Longleftrightarrow p=q$ cuando $a\ne1$. Explique exactamente qué cambia si $a=1$.



#### Ejercicio 35

Fije $0<a<1$. Demuestre $a^{p}\le a^{q}\Longleftrightarrow p\ge q$ para $p,q\in\mathbb R$, incluyendo la vuelta y el caso de igualdad. Úselo para resolver $(1/5)^{x+2}\le(1/5)^{3x-4}$.



#### Ejercicio 36

Sea $D=(2,\infty)$. Justifique, para $x\in D$, la equivalencia $\log_2(x-2)+\log_2(x+2)=2\Longleftrightarrow x^2-4=4$. Resuelva la ecuación original y explique por qué no puede borrar $D$ en la equivalencia.



#### Ejercicio 37

Justifique que la sustitución $u=3^x$ establece una correspondencia biyectiva entre las soluciones reales de $9^x-2\,3^x-3=0$ y las soluciones positivas de $u^2-2u-3=0$. Resuelva y explique por qué «resolver el polinomio» no termina el problema.



#### Ejercicio 38

Determine el dominio de $\ln((x-1)/(x+1))$ y justifique, sobre ese dominio, la equivalencia $\ln((x-1)/(x+1))\ge0\Longleftrightarrow (x-1)/(x+1)\ge1$. Resuelva sin multiplicar por $x+1$ antes de conocer su signo.

### D. Diagnóstico

Localice la primera ruptura o la obligación omitida en cada resolución. Explique su efecto y dé una reparación completa.



#### Ejercicio 39

Una resolución propone $\ln(x+2)=\ln x+\ln2=0$, y concluye $x=1/2$. Localice la primera ruptura y resuelva correctamente $\ln(x+2)=0$.



#### Ejercicio 40

Se afirma que $F(x)=e^{\ln(x-3)}=x-3$ para todo $x\in\mathbb R$. Identifique el error, determine el dominio de $F$ y decida si $F(2)$ existe.



#### Ejercicio 41

Una cadena dice $1^{2x-1}=1^{x+3}\Longleftrightarrow 2x-1=x+3\Longleftrightarrow x=4$. Localice la primera falsa equivalencia y dé el conjunto solución original.



#### Ejercicio 42

Para resolver $(1/2)^x>4$, se escribe $x>2$ «porque $4=(1/2)^2$». Identifique los errores en el valor exponencial y en el transporte de orden; repare la solución.



#### Ejercicio 43

Se resuelve $\log_{1/3}(x+1)\ge0$ como $x+1\ge1$, y se responde $x\ge0$. Localice la primera ruptura y conserve el dominio al corregirla.



#### Ejercicio 44

Se propone $\ln(x^2)=\ln9\Longleftrightarrow 2\ln x=2\ln3\Longleftrightarrow x=3$. Indique qué solución se pierde y repare la cadena sobre el dominio original.



#### Ejercicio 45

Para $\ln(x-2)+\ln(x+2)=\ln5$, se condensa y se obtiene $x^2-4=5$, luego se aceptan $x=\pm3$. Localice la obligación omitida y dé la respuesta correcta.



#### Ejercicio 46

Una resolución de $\ln x\,(\ln x-2)=0$ divide por $\ln x$ y concluye $x=e^2$. Localice la primera operación no reversible y recupere todas las soluciones.



#### Ejercicio 47

Se afirma $\log_2 8=\ln2/\ln8=1/3$. Identifique la fórmula mal aplicada y repare el cálculo con una verificación exponencial.



#### Ejercicio 48

De $2^x+2^{x+1}=12$ se pasa a $2^{2x+1}=12$ y se igualan exponentes tras expresar $12=2^{\log_2 12}$. Localice la primera ruptura y resuelva la ecuación original.



#### Ejercicio 49

Tras sustituir $u=e^x$ en $e^{2x}+e^x-2=0$, se obtienen $u=1,-2$ y se anuncian $x=0,\ln2$ «tomando logaritmo del valor absoluto». Diagnostique la reconstrucción y repárela.



#### Ejercicio 50

Se dice que «el logaritmo de $-4$ es negativo» y se usa $\ln(-4)=-\ln4$ para justificar $e^x=-4\Longleftrightarrow x=-\ln4$. Localice la primera ruptura y decida la ecuación real.

### E. Estrategia

Compare las rutas propuestas atendiendo a la estructura, las hipótesis y la información que cada una conserva. Resuelva con argumentos exactos.



#### Ejercicio 51

Resuelva $16^{x-1}=8^{x+1}$ por bases comunes y por logaritmos. Compare qué ruta ofrece menos operaciones y qué hipótesis comparten.



#### Ejercicio 52

Resuelva $3^{2x+1}=7$. Compare usar ln con usar $\log_3$, y explique por qué una solución decimal no es necesaria.



#### Ejercicio 53

Resuelva $4^x-6\,2^x+8=0$. Compare tratarla como cuadrática en $2^x$ con aplicar ln a ambos miembros después de aislar $4^x$. Indique qué ruta aprovecha mejor la estructura.



#### Ejercicio 54

Para $x>0$, resuelva $\ln x+\ln(4x)=\ln36$ por condensación y por expansión. Compare la cantidad de pasos sin perder el dominio.



#### Ejercicio 55

Decida sin aproximaciones si $\log_2 7<\log_4 49$. Compare cambio de base e interpretación como exponentes.



#### Ejercicio 56

Determine el signo de $\log_{1/4}3$ y ubíquelo entre dos enteros consecutivos, sin calculadora. Compare trabajar con potencias de $1/4$ con cambiar a base $4$.



#### Ejercicio 57

Resuelva $5^{x-2}\le3$. Compare transportar el orden con $\log_5$ y con ln; indique por qué no conviene redondear la frontera antes de dar el conjunto solución.



#### Ejercicio 58

Resuelva $e^x+e^{-x}=5/2$. Compare la sustitución positiva con tomar ln de la suma y justifique cuál elimina mejor la dificultad.



#### Ejercicio 59

Determine el dominio de $\ln((x-2)^2)$ y el de $\ln(x-2)+\ln(x-2)$. Decida si expandir es útil para estudiar la primera función en todo su dominio y proponga una expansión válida.



#### Ejercicio 60

Resuelva $\log_2(x+1)-\log_2(x-1)=1$. Compare condensar el cociente con exponenciar por separado las expresiones, y explique qué verificación requiere su ruta.

### F. Transferencia

Use las herramientas de dominios, ecuaciones y orden en composiciones, parámetros y modelos. Conserve las restricciones al reconstruir la variable original.



#### Ejercicio 61

Determine dominio e imagen de $F(x)=\ln((x-2)/(x+1))$. Justifique cada valor omitido y reconstruya una preimagen para cualquier valor de la imagen.



#### Ejercicio 62

Resuelva $\log_2((x+1)/(x-1))=2$, conservando el dominio racional y logarítmico.



#### Ejercicio 63

Resuelva $\ln((x+2)/(x-2))<\ln3$ y explique cómo conserva el signo del denominador.



#### Ejercicio 64

Resuelva $(\ln x)^2-3\ln x+2=0$. Indique la imagen de la variable auxiliar y reconstruya todas las soluciones.



#### Ejercicio 65

Resuelva $2^{x^2-1}=8$ y explique por qué la inyectividad exponencial no implica una única solución en $x$.



#### Ejercicio 66

Resuelva $\ln(\sqrt{x+1})=\ln2$. Determine primero el dominio de la composición.



#### Ejercicio 67

Para cada parámetro $a>0$, determine el conjunto solución de $a^{x-1}=a^2$. Separe los valores de base que cambian el argumento.



#### Ejercicio 68

Para cada $c\in\mathbb R$, clasifique las soluciones de $\ln(x-1)=c$, indicando existencia y unicidad.



#### Ejercicio 69

Una cantidad hipotética comienza en $96$ unidades y conserva $3/4$ de su valor por paso entero. Escriba el modelo, calcule su valor tras dos pasos y decida si ya es menor que la mitad inicial.



#### Ejercicio 70

Se estipula el modelo real $Q(t)=80(1/2)^{t/6}$, donde $t\ge0$ se mide en horas y $Q$ en unidades. Reescríbalo con tiempo $s$ medido en minutos y determine el tiempo para alcanzar $20$ unidades.



#### Ejercicio 71

En la familia hipotética $Q(n)=A b^n$, con $A>0$, $b>0$ y $n\in\mathbb Z_{\ge0}$, se conocen $Q(1)=18$ y $Q(3)=72$. Determine $A,b$ y compruebe ambos datos.



#### Ejercicio 72

Para el modelo real estipulado $Q(t)=10\,2^{t/3}$, $t\ge0$ en horas, halle el primer tiempo real con $Q(t)\ge50$. Si sólo se observa en horas enteras $n\ge0$, determine la primera observación que satisface el umbral y justifíquela sin redondear.

### G. Síntesis avanzada

Elija una representación útil sin que el enunciado anuncie el método. Justifique dominio, transformaciones, reconstrucción y cobertura completa de las soluciones.



#### Ejercicio 73

Resuelva en $\mathbb R$ la inequación $8^x-3\,4^x-6\,2^x+8\ge0$. Justifique que su respuesta cubre todas las regiones y determine qué fronteras se admiten.



#### Ejercicio 74

Resuelva $\ln(x-1)+\ln(x+1)=\ln(3x+3)$. Distinga los candidatos que ofrecen las transformaciones algebraicas de las soluciones de la ecuación original.



#### Ejercicio 75

Resuelva $\log_{1/2}((x-2)/(x+1))\ge1$. Justifique por separado la positividad del argumento y la orientación de la comparación.



#### Ejercicio 76

Para cada parámetro $a>0$, clasifique el conjunto solución de $a^{x^2-1}\le a$. Explique cómo cambian las regiones al atravesar el valor de base $1$ y qué ocurre exactamente en él.



#### Ejercicio 77

Determine el dominio y resuelva $\ln(e^{\ln(x^2-1)}-3)=0$. Explique por qué simplificar las inversas interiores no basta para fijar el dominio de toda la composición.



#### Ejercicio 78

Resuelva el sistema $\ln2/\ln(x-1)\ge1/2$ y $\log_{1/2}x\ge-2$. Dé un único conjunto solución y justifique cualquier multiplicación por un denominador de signo variable.



#### Ejercicio 79

En la familia hipotética $Q(t)=A b^t$, con $A,b>0$ y $t\ge0$ medido en días, se registran $Q(0)=12$ y $Q(2)=27$ unidades. Determine los parámetros. Si el modelo se estipula para todo tiempo real, halle el primer tiempo con $Q(t)\ge100$; si sólo se consulta en días enteros, determine el primero sin aproximaciones decimales.



#### Ejercicio 80

Resuelva $\ln((2^x-1)/(2^x-4))\le\ln2$. Justifique el dominio, todas las regiones y las fronteras. Presente una segunda ruta o una verificación independiente que confirme el conjunto solución.

### H. Profundización y reconstrucción

Intente cada tarea antes de consultar su solución. Los parámetros son reales salvo indicación distinta.



#### Ejercicio 081. Una base que cruza el valor uno

Para $t>0$, resuelva $t^{x-2}=t^{2x+1}$ y clasifique el caso $t=1$.



#### Ejercicio 082. Clasificar una inequación por la base

Para $t>0$, resuelva $t^{2x-1}\le t^{x+3}$.



#### Ejercicio 083. Una ecuación logarítmica con dos bases

Para $t>0$, $t\ne1$, resuelva $\log_t(x+1)=\log_{1/t}(x+1)+2$.



#### Ejercicio 084. Una familia exponencial con una región imposible

Para $t>0$, resuelva $t^x=2t^{x/2}$ y clasifique $t=1$.



#### Ejercicio 085. Construir un logaritmo con dos regiones de dominio

Dados $a<b$ y una base $q>0$, $q\ne1$, construya una composición logarítmica cuyo dominio sea $(-\infty,a)\cup(b,\infty)$.



#### Ejercicio 086. Prescribir un intervalo abierto mediante dos capas

Dados $a<b$, construya una composición de logaritmo y raíz con dominio exactamente $(a,b)$.



#### Ejercicio 087. Un dominio con una exclusión interior

Para $a<b$, determine el dominio de $1/\log_2[(x-a)/(b-x)]$ y simplifique la descripción del punto excluido.



#### Ejercicio 088. La base interior cambia una composición

Para $t>0$, $t\ne1$, determine el dominio de $\log_2(\log_t x)$.



#### Ejercicio 089. Umbral discreto por comparaciones exactas

Una sucesión satisface $Q(0)=5$ y $Q(n+1)=2Q(n)$ para enteros $n\ge0$. Determine el primer paso con $Q(n)\ge100$, sin aproximar logaritmos.



#### Ejercicio 090. Convertir un umbral en una condición sobre el factor

Para $0<b<1$, una sucesión vale $Q(n)=80b^n$. Determine todas las bases para las que el primer paso con $Q(n)<30$ es exactamente $n=4$.



#### Ejercicio 091. Elegir una unidad que normaliza el factor

En $Q(t)=Q_0b^{t/\tau}$, con $Q_0>0$, $b>0$, $b\ne1$, $\tau>0$, el tiempo $t$ se mide en horas. Encuentre la duración $d$ de una nueva unidad para que, al contar $s=t/d$, el factor por unidad sea $b^2$. Indique qué pasa si $b=1$.



#### Ejercicio 092. Todos los factores que cruzan un umbral en un paso dado

Para $b>1$, $Q_0>0$ y un entero $m\ge2$, determine todas las bases $b$ para las que $Q(n)=Q_0b^n$ alcanza por primera vez $5Q_0$ en el paso $m$.



#### Ejercicio 093. Ajustar dos datos y comprobar un tercero

En $Q(n)=Ab^n$ con $A,b>0$, ajuste $Q(0)=6$, $Q(1)=9$ y decida si puede cumplirse también $Q(2)=14$.



#### Ejercicio 094. Un solo dato y una familia de ajustes

Para $A,b>0$, se conoce $Q(2)=12$ en $Q(t)=Ab^t$. Describa todos los ajustes. Determine cuál de ellos satisface además $Q(5)=12$ y explique qué información añade el segundo dato.



#### Ejercicio 095. Un parámetro de datos y un test de compatibilidad

Para $u>0$, se dan $Q(0)=u$, $Q(1)=u+1$, $Q(2)=u+3$. Determine si existe $Q(n)=Ab^n$, $A,b>0$, que ajuste los tres.



#### Ejercicio 096. Datos finitos frente a una extensión continua

Construya dos funciones positivas distintas en $t\ge0$ que coincidan con $A b^n$ en cada entero $n\ge0$, para $A>0,b>0$. Explique qué demuestra el ejemplo.

## Soluciones desarrolladas

### A. Lectura



#### Solución 1

En $f$ varía la base y el exponente permanece fijo; es una función potencia. En $g$ la base permanece fija y varía el exponente; es una función exponencial. En $x=0$, $f(0)=0$ y $g(0)=1$. Por tanto, no coinciden en todo su dominio común y no son iguales como funciones. Una coincidencia en algún otro argumento no repararía esa diferencia.



#### Solución 2

Las bases válidas son $1/4$ y $3$: son positivas y distintas de $1$. La base negativa $-2$ no admite, por ejemplo, el exponente real $1/2$. La base $0$ no admite exponentes negativos, pues exigirían dividir por cero. La base $1$ produce la constante $1$, definida para todos los reales pero no inyectiva. Sólo las dos bases válidas proporcionan la pareja exponencial–logaritmo inversa del capítulo.



#### Solución 3

La forma equivalente es $\log_5(1/25)=-2$. La base es $5$, el argumento es $1/25$ y el valor es el exponente $-2$. El argumento es positivo, aunque el resultado sea negativo. La equivalencia se comprueba elevando $5$ a ese resultado: $5^{-2}=1/25$.



#### Solución 4

La primera no está definida: una potencia real de base $2$ nunca produce un valor negativo. La segunda está definida y vale $-2$, porque $2^{-2}=1/4$. La tercera no está definida como logaritmo de base válida: la función de base $1$ es constante y no tiene inversa. Las restricciones de argumento y base son distintas y ambas deben cumplirse.



#### Solución 5

La exponencial tiene dominio $\mathbb R$ e imagen $(0,\infty)$. Su inversa tiene dominio $(0,\infty)$ e imagen $\mathbb R$. El par $(2,9)$ pertenece a $E_3$, y el par intercambiado $(9,2)$ pertenece a $L_3$, porque $3^2=9$ equivale a $\log_39=2$. La inversión intercambia entrada y salida, además de dominio e imagen.



#### Solución 6

El argumento debe ser estrictamente positivo: $x-4>0$, de modo que el dominio es $(4,\infty)$. Excluir sólo $4$ seguiría admitiendo los valores $x<4$, que producen argumentos negativos y no tienen logaritmo real. En $4$ el argumento es cero y tampoco se admite.



#### Solución 7

El logaritmo interior exige $x+3>0$, así que $D=(-3,\infty)$. La exponencial exterior acepta todo valor real del logaritmo. Sobre $D$, la identidad inversa da $F(x)=x+3$. El polinomio $x+3$ existe en más argumentos, pero la composición original conserva $D$; la simplificación no define $F$ en $x\le-3$.



#### Solución 8

La base $1/3$ está entre cero y uno, por lo que tanto la exponencial como su inversa logarítmica son estrictamente decrecientes. Como $2<5$, se tiene $(1/3)^2>(1/3)^5$. Como $2<7$ y ambos argumentos son positivos, se tiene $\log_{1/3}2>\log_{1/3}7$. En cada caso la función decreciente invierte el orden de las entradas.



#### Solución 9

El valor inicial es $60$ y el factor por paso es $0.80=4/5$. La disminución es $1-0.80=0.20$, es decir $20\%$ del valor presente. El modelo discreto es $Q(n)=60(4/5)^n$ para enteros $n\ge0$. Tras un paso, $Q(1)=48$. El $80\%$ conservado no es el porcentaje perdido, y la fórmula no decide por sí sola valores entre pasos.



#### Solución 10

La imagen de exp es $(0,\infty)$: $u$ puede ser cualquier positivo, pero no cero ni negativo. El candidato $-1$ carece de preimagen real y se descarta. El candidato $4$ tiene una única preimagen $x=\ln4$, pues $\exp(\ln4)=4$ y exp es inyectiva. La resolución auxiliar sólo produce soluciones originales después de intersectar con la imagen y reconstruirlas.

### B. Fluidez



#### Solución 11

Las bases son positivas, por lo que podemos usar raíces principales y las leyes de exponentes racionales. Se obtiene $27^{2/3}=(\sqrt[3]{27})^2=9$. Asimismo, $16^{-3/4}=1/(\sqrt[4]{16})^3=1/8$. Finalmente, $(1/9)^{-1/2}=1/\sqrt{1/9}=3$. Los exponentes negativos indican recíprocos, sin cambiar el signo positivo de los valores.



#### Solución 12

Cada base es positiva y distinta de $1$, y los tres argumentos son positivos. Como $4^{-3/2}=1/8$, la definición inversa da $\log_4(1/8)=-3/2$. Puesto que $(1/2)^{-3}=8$, resulta $\log_{1/2}8=-3$. Finalmente, $9^{1/2}=3$ da $\log_9 3=1/2$. En cada caso, el resultado es el exponente que recupera el argumento.



#### Solución 13

El denominador es positivo para todo real $t$, así que el dominio es $\mathbb R$. Las leyes de producto y cociente de potencias de la misma base dan $5^{(2t-1)+(3-t)-(t+1)}=5^1=5$. Por tanto, la expresión es la constante $5$ sobre todo su dominio. La cancelación se realiza en los exponentes mediante leyes admitidas para exponentes reales.



#### Solución 14

En la primera, $e^{3x-2}>0$ para todo real y la identidad inversa da $\ln(e^{3x-2})=3x-2$ sobre $\mathbb R$. En la segunda, el logaritmo interior exige $x^2-4>0$, esto es $x<-2$ o $x>2$. Sobre ese dominio, $e^{\ln(x^2-4)}=x^2-4$. Aunque el polinomio final existe para todos los reales, la composición conserva el dominio $(-\infty,-2)\cup(2,\infty)$.



#### Solución 15

Con las hipótesis dadas, $9x^2>0$ y $\sqrt y>0$, de modo que el cociente tiene logaritmo real. Las leyes de cociente y producto dan $\log_3 9+\log_3(x^2)-\log_3(y^{1/2})$. Como $x^2=|x|^2$ y $|x|>0$, la ley de potencia da $\log_3(x^2)=2\log_3|x|$. La expansión válida es $2+2\log_3|x|-\tfrac12\log_3 y$. Reemplazar $|x|$ por $x$ perdería los argumentos negativos permitidos.



#### Solución 16

Las expresiones originales exigen $x-1>0$ y $x+2>0$, cuya intersección es $x>1$. En ese dominio, las leyes de potencia y cociente dan $\ln((x-1)^2/(x+2))$. La igualdad se afirma sobre $(1,\infty)$. El logaritmo condensado aislado también admitiría algunos valores $x<1$, pero éstos no pertenecen al dominio original. Condensar conserva la restricción $x>1$.



#### Solución 17

El cambio de base da $\log_7 20=\ln20/\ln7$. El denominador no se anula porque $7\ne1$, y $20>0$ garantiza que el numerador existe. Para el segundo cálculo conviene usar base $2$: $\log_8 32=\log_2 32/\log_2 8=5/3$. La comprobación $8^{5/3}=32$ confirma el valor exacto. No se requieren aproximaciones decimales.



#### Solución 18

Ambos miembros están definidos y son positivos para todo real. Escribiendo las bases como potencias de $3$, obtenemos $3^{2x-2}=3^{6x+3}$. La inyectividad de la exponencial de base $3$ hace esta igualdad equivalente a $2x-2=6x+3$, de donde $x=-5/4$. En ese valor ambos exponentes son $-9/2$. Por tanto, $S=\{-5/4\}$.



#### Solución 19

El dominio es $\mathbb R$. Dividir por $5\ne0$ da $2^{x+1}=6$, equivalente a $x+1=\log_2 6$ por la definición de logaritmo. Así, $x=\log_2 6-1=\log_2 3$, usando $1=\log_2 2$ y la ley de cociente con argumentos positivos. La comprobación da $5\,2^{\log_2 3+1}=5\cdot6=30$. El conjunto solución es $S=\{\log_2 3\}$.



#### Solución 20

El dominio original es $\mathbb R$. Con $u=e^x>0$, la ecuación equivale a $u^2-5u+6=(u-2)(u-3)=0$. Los candidatos $u=2$ y $u=3$ pertenecen a la imagen positiva de exp. La inversa ln reconstruye exactamente una preimagen para cada uno: $x=\ln2$ y $x=\ln3$. Sustituir $e^x=2$ o $3$ anula el polinomio, y la biyectividad garantiza que no faltan soluciones. Así, $S=\{\ln2,\ln3\}$.



#### Solución 21

El argumento exige $2x-1>0$, así que $D=(1/2,\infty)$. Sobre $D$, la definición de logaritmo convierte la ecuación en $2x-1=3^2=9$. Resulta $x=5$, que pertenece a $D$. La sustitución original da $\log_3 9=2$, de modo que $S=\{5\}$. La equivalencia inversa y el control de dominio prueban que ésta es toda la solución.



#### Solución 22

Las dos condiciones de argumento positivo son $x>-3$ y $x>1/2$, por lo que $D=(1/2,\infty)$. En ese dominio, la inyectividad de ln hace la ecuación equivalente a $x+3=2x-1$. La solución algebraica es $x=4$ y pertenece a $D$. Ambos argumentos valen $7$, lo que verifica la igualdad original. Por tanto, $S=\{4\}$.



#### Solución 23

Los argumentos exigen $x>1$ y $x>-1$, así que el dominio original es $D=(1,\infty)$. Allí la ley de producto da $\log_2((x-1)(x+1))=3$, equivalente a $x^2-1=8$. Los candidatos algebraicos son $x=3$ y $x=-3$, pero sólo $3$ pertenece a $D$. En $3$, la suma es $\log_2 2+\log_2 4=1+2=3$. En consecuencia, $S=\{3\}$; el candidato $-3$ no tiene logaritmos originales definidos.



#### Solución 24

El dominio es $\mathbb R$ y $8=(1/4)^{-3/2}$. Como la base $1/4$ está entre cero y uno, la exponencial es estrictamente decreciente. La comparación equivale a $2x-1\le-3/2$, de donde $x\le-1/4$. La frontera produce igualdad y se incluye. Así, $S=(-\infty,-1/4]$. La inversión del orden ocurre al comparar exponentes, mientras dividir por $2>0$ conserva el orden.



#### Solución 25

El logaritmo exige $x-2>0$, así que $D=(2,\infty)$. Escribimos $-1=\log_{1/2}2$. La base menor que uno hace el logaritmo estrictamente decreciente; por tanto, sobre $D$, la inequación equivale a $x-2>2$. Se obtiene $x>4$, condición que ya respeta el dominio. El punto $4$ produce igualdad y queda excluido por la comparación estricta. El conjunto solución es $S=(4,\infty)$.



#### Solución 26

El dominio original exige $x>-1$. Como $0=\ln1$ y ln es estrictamente creciente, la condición compuesta equivale a $1\le x+1<4$. Esto da $0\le x<3$, una región contenida en el dominio. En $x=0$, el logaritmo vale cero y la primera igualdad se admite; en $x=3$, vale $\ln4$ y la cota estricta lo excluye. Por tanto, $S=[0,3)$. Ambas comparaciones se han intersectado, no unido.

### C. Justificación



#### Solución 27

Definamos $r=\log_a u$ y $s=\log_a v$. La positividad de $u,v$ permite definir ambos números y la inversión da $u=a^r$, $v=a^s$. La ley exponencial produce $uv=a^ra^s=a^{r+s}$. Como $uv>0$, podemos aplicar $\log_a$ y obtener $\log_a(uv)=r+s$. La base positiva permite utilizar la exponencial real, y $a\ne1$ garantiza su inyectividad y la existencia de su inversa. No se han aplicado leyes logarítmicas para demostrar la misma ley que se buscaba.



#### Solución 28

Sean $r=\log_a u$ y $s=\log_a v$, bien definidos por las hipótesis. La ley exponencial del cociente da $u/v=a^r/a^s=a^{r-s}$. El cociente es positivo y la identidad inversa permite concluir $\log_a(u/v)=r-s$. La igualdad requiere también que los dos logaritmos del miembro derecho existan. Por ejemplo, con $u=-2$ y $v=-1$, el cociente es $2>0$ y el miembro izquierdo está definido, pero $\log_a u$ y $\log_a v$ no son reales. La positividad del cociente sólo autoriza su propio logaritmo.



#### Solución 29

Escribamos $s=\log_a u$, de modo que $u=a^s$. Como las bases son positivas, la ley exponencial admitida para exponentes reales da $u^r=(a^s)^r=a^{sr}$. También por las propiedades admitidas, $u^r>0$, así que su logaritmo está definido. La identidad de inversa proporciona $\log_a(u^r)=sr=r\log_a u$. Aquí se usaron la ley de potencia de una potencia, la positividad y la inversa. La construcción de las potencias reales no se ha demostrado: se ha demostrado la ley logarítmica como consecuencia de aquellas propiedades.



#### Solución 30

Si $x\ne0$, entonces $|x|>0$ y $x^2=|x|^2$. La ley de potencia aplicada a la base positiva $|x|$ da $\ln(x^2)=\ln(|x|^2)=2\ln|x|$. Ambas expresiones tienen dominio $\mathbb R\setminus\{0\}$. Podemos escribir $2\ln x$ sólo cuando $x>0$, pues allí $|x|=x$ y el logaritmo existe. En $x=-2$, el miembro izquierdo es $\ln4$ y la fórmula con valor absoluto da $2\ln2$, mientras $\ln(-2)$ no está definido en los reales. El reemplazo falla por dominio, aunque el cuadrado original sea positivo.



#### Solución 31

Sean $0<u<v$ y escribamos $r=\log_a u$, $s=\log_a v$, de manera que $a^r=u$ y $a^s=v$. Si $a>1$ y fuese $r\ge s$, la monotonía de la exponencial daría $u\ge v$, contradicción. Por tricotomía, $r<s$, lo que prueba que el logaritmo es estrictamente creciente. Si $0<a<1$ y fuese $r\le s$, la exponencial decreciente volvería a dar $u\ge v$, contradicción. En este régimen debe cumplirse $r>s$, y el logaritmo es estrictamente decreciente. La prueba utiliza preimágenes positivas y orden, sin añadir una admisión sobre la inversa.



#### Solución 32

Sea $r=\log_a u$, así que $u=a^r$. Aplicando $\log_b$, definido porque ambos lados son positivos, y la ley de potencia ya demostrada, resulta $\log_b u=r\log_b a$. Si $\log_b a=0$, la definición inversa daría $a=b^0=1$, contrario a la hipótesis. Podemos dividir por ese denominador no nulo y obtener $r=\log_b u/\log_b a$. Las restricciones sobre $b$ aseguran una base logarítmica válida; las de $a$ permiten definir $r$. La prueba sirve también cuando alguno de los logaritmos es negativo.



#### Solución 33

Como $a>0$, existe $\ln a$ y la identidad inversa da $a=e^{\ln a}$. La ley de potencia de una potencia con base positiva permite escribir $a^x=(e^{\ln a})^x=e^{x\ln a}$. No es necesario excluir $a=1$: en ese caso $\ln1=0$ y los dos miembros valen $1$ para todo $x$. La condición $a\ne1$ corresponde a la invertibilidad de la exponencial de base $a$, que aquí no se necesita. El argumento usa las leyes reales admitidas y las identidades de inversa; no construye analíticamente e ni exp.



#### Solución 34

Si $a\ne1$, la exponencial es estrictamente monótona. Si $p<q$ o $p>q$, sus valores son distintos, tanto en el régimen creciente como en el decreciente. Así, $a^p=a^q$ obliga a $p=q$; la implicación inversa se obtiene sustituyendo exponentes iguales. Para $a=1$, ambos valores son siempre $1$, incluso si $p\ne q$. Por ejemplo, $1^0=1^2$ con $0\ne2$. Por tanto, en ese caso sólo subsiste la implicación $p=q\Rightarrow a^p=a^q$, y la igualdad de valores no impone una condición sobre los exponentes.



#### Solución 35

Si $p>q$, la monotonía estrictamente decreciente da $a^p<a^q$; si $p=q$, los valores son iguales. Esto prueba $p\ge q\Rightarrow a^p\le a^q$. Para la vuelta, si $p<q$, la misma monotonía daría $a^p>a^q$, contradiciendo la comparación propuesta. La tricotomía deja $p\ge q$, y la igualdad de valores ocurre exactamente cuando $p=q$. En el problema, el dominio es $\mathbb R$ y la equivalencia da $x+2\ge3x-4$, es decir $x\le3$. Por tanto, $S=(-\infty,3]$; en $3$ ambos exponentes valen $5$ y se admite la frontera.



#### Solución 36

Para $x\in D$, los dos factores $x-2$ y $x+2$ son positivos. La ley de producto permite condensar la suma como $\log_2(x^2-4)$, y la definición inversa hace $\log_2(x^2-4)=2$ equivalente a $x^2-4=2^2=4$. La ecuación algebraica tiene candidatos $x=\pm2\sqrt2$. Sólo $2\sqrt2>2$ pertenece a $D$, por lo que $S=\{2\sqrt2\}$. El candidato negativo satisface la ecuación algebraica y tiene producto positivo, pero los dos argumentos logarítmicos originales son negativos. La equivalencia se ha probado sobre $D$; fuera de él, el miembro original ni siquiera está definido.



#### Solución 37

La ley de potencia da $9^x=(3^x)^2$, de modo que cada solución original produce una solución auxiliar $u=3^x>0$. Recíprocamente, para cada raíz auxiliar positiva existe una única preimagen $x=\log_3u$; al sustituirla, se recupera la ecuación original. Ésta es la correspondencia biyectiva entre los dos conjuntos indicados. Factorizando, $u^2-2u-3=(u-3)(u+1)$, con raíces $3$ y $-1$. La raíz $-1$ no está en la imagen exponencial; la raíz $3$ se reconstruye como $x=1$. Así, $S=\{1\}$, verificado por $9-6-3=0$. Resolver en toda $\mathbb R$ la auxiliar sólo ofrece candidatos: todavía debe conservarse $u>0$ y volverse a $x$.



#### Solución 38

El cociente debe existir y ser positivo. Su tabla de signos, con puntos $-1$ y $1$, da $D=(-\infty,-1)\cup(1,\infty)$. En ese dominio, escribir $0=\ln1$ y usar la monotonía estrictamente creciente de ln justifica la equivalencia en ambos sentidos. Restar $1$ en la comparación racional da $-2/(x+1)\ge0$. Como el numerador es estrictamente negativo y el denominador no se anula, esto ocurre exactamente si $x+1<0$, es decir $x<-1$. La intersección con $D$ conserva esa región, así que $S=(-\infty,-1)$. Allí el cociente es mayor que $1$; para $x>1$ está entre $0$ y $1$. No hay punto de igualdad, y $-1$ se excluye porque la expresión no existe.

### D. Diagnóstico



#### Solución 39

La primera ruptura es distribuir el logaritmo sobre la suma $x+2$: la ley conocida corresponde a productos, no a sumas. Además, $\ln x+\ln2$ exigiría $x>0$, mientras el dominio original es $x>-2$. La definición inversa da $\ln(x+2)=0\Longleftrightarrow x+2=1$, y resulta $x=-1$, que pertenece al dominio. Así, $S=\{-1\}$. El candidato $1/2$ tiene argumento $5/2\ne1$ y no satisface la ecuación. La falsa ley ha perdido la solución verdadera y producido una respuesta incorrecta.



#### Solución 40

La identidad inversa sólo puede aplicarse si el logaritmo interior está definido. Su argumento exige $x-3>0$, de modo que $D_F=(3,\infty)$. Sobre ese dominio, $F(x)=x-3$ es correcto. La primera ruptura está en extender la igualdad funcional a todo $\mathbb R$ después de simplificar. En particular, $F(2)$ no existe, aunque el polinomio $x-3$ tenga valor $-1$ en $2$. La reparación consiste en acompañar la fórmula simplificada de su dominio heredado.



#### Solución 41

El primer paso usa inyectividad de una exponencial de base $1$, que es constante y no inyectiva. Ambos miembros originales valen $1$ para todo real $x$, por lo que $S=\mathbb R$. La ecuación de exponentes sí tiene solución $4$, pero no es equivalente a la original. Todos los demás reales se perdieron al imponer una condición innecesaria. La reparación es separar la base $1$ antes de igualar exponentes; no basta verificar que $4$ satisface la igualdad.



#### Solución 42

La igualdad numérica es falsa: $(1/2)^2=1/4$, mientras $4=(1/2)^{-2}$. Ésta es la primera ruptura. Al comparar con el exponente correcto también debe usarse que la base $1/2$ produce una función decreciente. Por tanto, $(1/2)^x>(1/2)^{-2}\Longleftrightarrow x<-2$. El dominio es $\mathbb R$ y $S=(-\infty,-2)$. El extremo $-2$ da igualdad y queda excluido; no basta cambiar sólo el signo del exponente sin reparar la orientación.



#### Solución 43

El dominio exige $x+1>0$, es decir $x>-1$. Como $0=\log_{1/3}1$ y el logaritmo es decreciente, la comparación correcta es $x+1\le1$, no $x+1\ge1$. La primera ruptura está en transportar el orden como si la base fuese mayor que uno. Al intersectar $x\le0$ con el dominio se obtiene $S=(-1,0]$. El punto $0$ se admite por igualdad y $-1$ se excluye porque su argumento es cero. La respuesta propuesta pierde todos los valores entre $-1$ y $0$ y agrega valores positivos falsos.



#### Solución 44

El dominio original es $x\ne0$. La primera equivalencia introduce $\ln x$, que sólo existe para $x>0$, y pierde la rama negativa. La identidad válida en todo el dominio es $\ln(x^2)=2\ln|x|$. Dividir por $2$ e inyectividad de ln dan $|x|=3$, de donde $x=\pm3$. Ambos valores tienen cuadrado $9$ y satisfacen la ecuación, así que $S=\{-3,3\}$. Verificar sólo $3$ no revelaría la solución perdida.



#### Solución 45

Los argumentos originales exigen simultáneamente $x>2$ y $x>-2$, así que $D=(2,\infty)$. La condensación y el paso a $x^2-4=5$ son equivalentes sobre $D$. La obligación omitida consiste en conservar ese dominio al aceptar las raíces algebraicas. Sólo $3$ pertenece a $D$; en $-3$ ambos logaritmos originales tienen argumentos negativos. En $3$, la suma es $\ln1+\ln5=\ln5$, de modo que $S=\{3\}$. La reparación no altera la factorización: filtra los candidatos por las condiciones originales.



#### Solución 46

El dominio original es $x>0$. Dividir por $\ln x$ exige además $\ln x\ne0$, condición que no estaba asegurada y que excluye $x=1$. La primera operación no reversible es esa división sin separar el caso nulo. La ley del producto nulo da $\ln x=0$ o $\ln x-2=0$. Aplicando exp, se reconstruyen $x=1$ y $x=e^2$, ambos positivos y ambos verificables en el producto original. Por tanto, $S=\{1,e^2\}$.



#### Solución 47

La fórmula de cambio de base coloca el logaritmo del argumento en el numerador y el de la base en el denominador. La primera ruptura es invertir ese cociente. La reparación es $\log_2 8=\ln8/\ln2=3$, porque $\ln8=3\ln2$ y $\ln2\ne0$. La comprobación exponencial da $2^3=8$. En cambio, $2^{1/3}\ne8$; el valor $1/3$ corresponde a $\log_8 2$.



#### Solución 48

La primera ruptura es reemplazar una suma de potencias por una potencia cuyo exponente es la suma. La ley $2^u2^v=2^{u+v}$ corresponde a un producto. En el dominio $\mathbb R$, la identidad $2^{x+1}=2\,2^x$ permite factorizar la suma como $3\,2^x=12$. Dividir por $3$ da $2^x=4=2^2$, y la inyectividad produce $x=2$. La sustitución $4+8=12$ verifica el resultado, de modo que $S=\{2\}$. La operación posterior con logaritmos no repara la igualdad falsa anterior.



#### Solución 49

La ecuación auxiliar $u^2+u-2=(u-1)(u+2)=0$ está bien resuelta. La primera ruptura aparece al reconstruir el candidato negativo como si $u$ pudiera ser cualquier real. La imagen de exp es $(0,\infty)$, así que $u=-2$ no tiene preimagen y debe descartarse. Reemplazarlo por $|u|=2$ cambia el candidato; en $x=\ln2$ la ecuación original vale $4+2-2=4\ne0$. El candidato positivo $u=1$ tiene única preimagen $x=0$, y $1+1-2=0$ verifica. Por tanto, $S=\{0\}$.



#### Solución 50

La primera ruptura consiste en tratar $\ln(-4)$ como un número real: el argumento negativo está fuera del dominio de ln. La identidad correcta es $-\ln4=\ln(1/4)$, con argumento positivo. La exponencial real es siempre positiva, por lo que $e^x=-4$ carece de solución y $S=\varnothing$. En particular, $e^{-\ln4}=1/4$, no $-4$. Un valor logarítmico negativo representa el exponente de un argumento positivo menor que uno; no autoriza argumentos negativos.

### E. Estrategia



#### Solución 51

Ambos miembros son positivos para todo real. Con base común $2$, la ecuación equivale a $2^{4x-4}=2^{3x+3}$, luego $4x-4=3x+3$ y $x=7$. Por logaritmos, la inyectividad de ln da $(x-1)\ln16=(x+1)\ln8$. Como $\ln16=4\ln2$ y $\ln8=3\ln2$, dividir por $\ln2\ne0$ recupera la misma ecuación. En $7$ ambos miembros son $2^{24}$, así que $S=\{7\}$. La base común evita introducir logaritmos y sus coeficientes; ambas rutas necesitan leyes con bases positivas e inyectividad.



#### Solución 52

El dominio es $\mathbb R$ y el valor $7$ pertenece a la imagen positiva. Usar $\log_3$ da directamente $2x+1=\log_3 7$ y $x=(\log_3 7-1)/2$. Con ln obtenemos $(2x+1)\ln3=\ln7$, de donde $x=(\ln7/\ln3-1)/2$, ya que $\ln3\ne0$. El cambio de base muestra que ambas respuestas coinciden. La primera ruta expresa más directamente el exponente buscado; la segunda permite trabajar con una base habitual de cálculo. La sustitución devuelve $3^{\log_3 7}=7$, por lo que el singleton indicado es la solución exacta y no requiere redondeo.



#### Solución 53

La relación $4^x=(2^x)^2$ sugiere $u=2^x>0$. La auxiliar se factoriza como $(u-2)(u-4)=0$, y ambas raíces positivas se reconstruyen como $x=1,2$. Así, $S=\{1,2\}$, verificado por $4-12+8=0$ y $16-24+8=0$. Aislar primero $4^x=6\,2^x-8$ y tomar ln sólo sería reversible donde el miembro derecho sea positivo. Además produciría $x\ln4=\ln(6\,2^x-8)$, cuyo logaritmo no se distribuye sobre la diferencia ni elimina la variable interior. La ruta cuadrática resuelve una estructura reconocible y permite reconstruir todas las preimágenes; la otra añade una condición sin simplificar el problema.



#### Solución 54

El dominio original es $x>0$, que asegura ambos argumentos positivos. Condensar da $\ln(4x^2)=\ln36$, equivalente a $4x^2=36$; las raíces algebraicas son $\pm3$, y el dominio conserva sólo $3$. Expandir $\ln(4x)=\ln4+\ln x$ da $2\ln x=\ln36-\ln4=\ln9=2\ln3$, y luego $x=3$. En la original, $\ln3+\ln12=\ln36$, por lo que $S=\{3\}$. La condensación reduce pronto a una cuadrática y exige filtrar su raíz negativa; la expansión mantiene directamente el logaritmo de un argumento positivo y evita ese candidato. Ambas rutas son breves si se declara $x>0$ al comienzo.



#### Solución 55

El cambio de base a $2$ da $\log_4 49=\log_2(7^2)/\log_2 4=2\log_2 7/2=\log_2 7$. Por tanto, la desigualdad estricta es falsa: los dos números son iguales. Una segunda ruta toma $r=\log_2 7$, de modo que $2^r=7$. Entonces $4^r=(2^r)^2=49$ y la definición inversa implica $r=\log_4 49$. Todos los argumentos son positivos y las bases son válidas. Ambas rutas son exactas; la segunda muestra directamente que el mismo exponente sirve para las dos bases.



#### Solución 56

Como $(1/4)^0=1<3<4=(1/4)^{-1}$ y la exponencial es decreciente, el exponente que produce $3$ está entre $-1$ y $0$. Así, $-1<\log_{1/4}3<0$, y el signo es negativo. Con cambio de base, $\log_{1/4}3=\log_4 3/\log_4(1/4)=-\log_4 3$. De $1<3<4$ y monotonía creciente se deduce $0<\log_4 3<1$; multiplicar por $-1$ recupera la misma ubicación. La primera ruta usa directamente la base dada; la segunda convierte la comparación a una base creciente y explicita la inversión de signo.



#### Solución 57

El dominio es $\mathbb R$. Como $5>1$ y $3=5^{\log_5 3}$, la comparación equivale a $x-2\le\log_5 3$, de modo que $S=(-\infty,2+\log_5 3]$. La ruta con ln da $(x-2)\ln5\le\ln3$; al dividir por $\ln5>0$ se obtiene la misma frontera por cambio de base. El extremo satisface igualdad y se incluye. Redondearlo sustituiría la frontera exacta por otra y podría incluir valores falsos o excluir valores verdaderos cercanos a ella. Una aproximación puede acompañar la respuesta, pero el intervalo exacto conserva toda la solución.



#### Solución 58

El dominio es $\mathbb R$. Con $u=e^x>0$, tenemos $e^{-x}=1/u$ y la ecuación equivale a $u+1/u=5/2$. Multiplicar por $2u>0$ da $2u^2-5u+2=(2u-1)(u-2)=0$. Las raíces positivas $1/2$ y $2$ se reconstruyen como $x=-\ln2$ y $x=\ln2$, y ambas verifican $2+1/2=5/2$. Por tanto, $S=\{-\ln2,\ln2\}$. Tomar ln de la suma conservaría la igualdad porque ambos miembros son positivos, pero $\ln(e^x+e^{-x})$ no se separa en una suma de logaritmos. La sustitución convierte el problema en una cuadrática y controla la reconstrucción.



#### Solución 59

La primera expresión exige $(x-2)^2>0$, de modo que su dominio es $\mathbb R\setminus\{2\}$. La suma exige $x-2>0$, así que sólo existe en $(2,\infty)$. Sustituir la primera por esa suma perdería todos los argumentos $x<2$. La expansión válida en todo el dominio original es $\ln((x-2)^2)=2\ln|x-2|$, porque $|x-2|>0$ cuando $x\ne2$. Esta forma puede ser útil para estudiar el tamaño o resolver condiciones de orden, siempre conservando la exclusión $x=2$. La elección de representación debe respetar el dominio antes de buscar economía de cálculo.



#### Solución 60

El dominio original es $x>1$. Condensar da $\log_2((x+1)/(x-1))=1$, equivalente en ese dominio a $(x+1)/(x-1)=2$. Multiplicar por $x-1\ne0$ da $x+1=2x-2$, luego $x=3$. Exponenciar la igualdad completa también produce $2^{\log_2(x+1)-\log_2(x-1)}=2$, y la ley de cociente lleva a la misma ecuación racional; no permite sustituir la diferencia por $(x+1)-(x-1)$. El candidato $3$ pertenece al dominio y verifica $\log_2 4-\log_2 2=2-1=1$. Así, $S=\{3\}$. La cadena conserva equivalencias sobre $x>1$, por lo que no creó candidatos extraños; la sustitución final aporta un control independiente.

### F. Transferencia



#### Solución 61

El cociente debe ser positivo y su denominador no nulo. La tabla de signos da $D=(-\infty,-1)\cup(2,\infty)$. Si $t=(x-2)/(x+1)=1-3/(x+1)$, entonces $t>1$ en $x<-1$ y $0<t<1$ en $x>2$. Todo $t>0$, $t\ne1$, tiene preimagen $x=(t+2)/(1-t)$, que pertenece a la rama correspondiente. Así, la imagen del cociente es $(0,\infty)\setminus\{1\}$ y la de $F$ es $\mathbb R\setminus\{0\}$. Para cualquier $y\ne0$, tomar $t=e^y$ y $x=(e^y+2)/(1-e^y)$ construye una preimagen. El valor $0$ se omite porque exigiría un cociente igual a $1$, imposible con numerador y denominador separados por $3$.



#### Solución 62

El cociente existe y es positivo exactamente si $x<-1$ o $x>1$. Sobre ese dominio, la definición inversa da $(x+1)/(x-1)=4$. Multiplicar por el denominador no nulo produce $x+1=4x-4$, luego $x=5/3$. Este valor pertenece a $x>1$ y el cociente vale $4$, de modo que el logaritmo vale $2$. Todas las transformaciones fueron equivalentes sobre el dominio original, así que $S=\{5/3\}$.



#### Solución 63

El dominio es $D=(-\infty,-2)\cup(2,\infty)$. Sobre él, ln creciente da $(x+2)/(x-2)<3$. Restar $3$ sin multiplicar por un signo desconocido produce $-2(x-4)/(x-2)<0$, equivalente a $(x-4)/(x-2)>0$. Su tabla de signos da $x<2$ o $x>4$. Al intersectar con $D$, resulta $S=(-\infty,-2)\cup(4,\infty)$. El punto $-2$ produce argumento cero, $2$ anula el denominador y $4$ produce igualdad; ninguno se admite. La tabla resuelve la comparación sin suponer un signo global para $x-2$.



#### Solución 64

El dominio original es $x>0$. La sustitución $u=\ln x$ recorre todo $\mathbb R$, y la ecuación se convierte en $(u-1)(u-2)=0$. Ambas raíces $u=1,2$ pertenecen a esa imagen. La inversa exp proporciona las únicas preimágenes $x=e$ y $x=e^2$, ambas positivas. Sustituir sus logaritmos anula el polinomio y la biyectividad asegura cobertura completa. Por tanto, $S=\{e,e^2\}$. No se impone $u>0$ por el mero hecho de que aparezca un logaritmo: esa restricción corresponde a su argumento, no a su valor.



#### Solución 65

El dominio es $\mathbb R$ y $8=2^3$. La inyectividad de la función exterior da $x^2-1=3$, equivalente a $x^2=4$. La expresión interior no es inyectiva sobre $\mathbb R$, de modo que debe reconstruirse $x=\pm2$. Ambos valores producen exponente $3$ y verifican la ecuación. Así, $S=\{-2,2\}$. La exponencial identifica el valor del argumento, pero no identifica entre sí las distintas preimágenes de ese argumento bajo la función cuadrática.



#### Solución 66

La raíz exige $x+1\ge0$, pero el logaritmo exige que la raíz sea estrictamente positiva. La condición conjunta es $x>-1$. En ese dominio, ln inyectiva da $\sqrt{x+1}=2$. La equivalencia de raíz principal con segundo miembro positivo permite elevar al cuadrado y obtener $x+1=4$, luego $x=3$. El candidato pertenece al dominio y la raíz vale $2$, por lo que $S=\{3\}$. El extremo $-1$ no se admite aunque la raíz exista, pues su valor cero no tiene logaritmo.



#### Solución 67

Todas las expresiones existen para $x\in\mathbb R$. Si $a\ne1$, la exponencial es inyectiva y la ecuación equivale a $x-1=2$, de donde $S(a)=\{3\}$. Esta conclusión vale tanto para $a>1$ como para $0<a<1$, pues ambos regímenes son estrictamente monótonos. Si $a=1$, ambos miembros valen $1$ para cualquier real y $S(1)=\mathbb R$. El caso constante debe separarse antes de igualar exponentes; no se define aquí un logaritmo de base $1$.



#### Solución 68

El dominio en $x$ es $(1,\infty)$, independiente de $c$. Aplicar exp da $x-1=e^c$, por lo que $x=1+e^c$. Como $e^c>0$ para todo real $c$, este valor siempre pertenece al dominio. La identidad $\ln(e^c)=c$ verifica la ecuación y la inyectividad de ln prueba que no hay otra solución. Así, $S(c)=\{1+e^c\}$ para cada $c\in\mathbb R$. No se exige $c>0$: la imagen de ln es todo $\mathbb R$.



#### Solución 69

El modelo discreto es $Q(n)=96(3/4)^n$ para enteros $n\ge0$. El factor se aplica al valor presente en cada paso, así que $Q(2)=96\cdot9/16=54$ unidades. La mitad inicial es $48$ unidades y $54>48$, por lo que después de dos pasos todavía no se ha reducido por debajo de la mitad. La disminución por paso es $1/4=25\%$ del valor presente, no $25\%$ del valor inicial cada vez. La fórmula no fija por sí sola un comportamiento entre pasos.



#### Solución 70

La relación de unidades es $t=s/60$. Sustituirla da $Q=80(1/2)^{s/360}$, con $s\ge0$ en minutos. Para $Q=20$, se requiere $(1/2)^{s/360}=1/4=(1/2)^2$. La inyectividad da $s/360=2$, así que $s=720$ minutos, equivalentes a $12$ horas. La sustitución en cualquiera de las dos fórmulas produce $20$ unidades. La escala $6$ horas corresponde a $360$ minutos; cambiar sólo el nombre de la variable sin ajustar el exponente alteraría el modelo.



#### Solución 71

Los datos dan $Ab=18$ y $Ab^3=72$. Dividir la segunda igualdad por la primera, no nula, produce $b^2=4$. La hipótesis $b>0$ selecciona $b=2$ y luego $A=18/2=9$. El modelo es $Q(n)=9\,2^n$. Se verifica $Q(1)=18$ y $Q(3)=9\cdot8=72$. Dentro de la familia declarada los parámetros son únicos; los dos datos no prueban que una cantidad real siga esa ley para otros tiempos.



#### Solución 72

Dividir por $10>0$ da $2^{t/3}\ge5$. La base creciente hace esta condición equivalente a $t\ge3\log_2 5$, que ya respeta $t\ge0$; el primer tiempo real es $t_*=3\log_2 5$ horas. Para ubicarlo, $2^6=64<125<128=2^7$ implica $6<\log_2 125=3\log_2 5<7$. Por tanto, la primera hora entera admisible es $n=7$. En $n=6$, el valor es $40<50$; en $n=7$, la comparación $2^{7/3}>5$ se deduce al elevar al cubo ambos positivos y usar $128>125$. El umbral continuo y la primera observación entera son objetos distintos.

### G. Síntesis avanzada



#### Solución 73

El dominio es $\mathbb R$. Reconocer $4^x=(2^x)^2$ y $8^x=(2^x)^3$ permite tomar $u=2^x>0$. El polinomio auxiliar factoriza como $u^3-3u^2-6u+8=(u-1)(u-4)(u+2)$. Sobre la imagen $u>0$, el factor $u+2$ es positivo, así que la inequación equivale a $(u-1)(u-4)\ge0$. La tabla de signos conserva $0<u\le1$ o $u\ge4$. Como $2^x$ es creciente y biyectiva hacia los positivos, la vuelta da $x\le0$ o $x\ge2$. Por tanto, $S=(-\infty,0]\cup[2,\infty)$. En $0$ y $2$ el polinomio se anula y ambos extremos se incluyen; entre ellos el producto de los dos factores es negativo. La raíz auxiliar $-2$ no tiene preimagen y no crea otra región original.



#### Solución 74

Los tres argumentos deben ser positivos: $x>1$, $x>-1$ y $x>-1$, cuya intersección es $D=(1,\infty)$. Sobre $D$, la ley de producto y la inyectividad de ln dan $x^2-1=3x+3$. La factorización $x^2-3x-4=(x-4)(x+1)=0$ ofrece candidatos $4$ y $-1$. Sólo $4$ pertenece a $D$; en $-1$ dos argumentos son cero y el primero es negativo. En $4$, la igualdad se comprueba como $\ln3+\ln5=\ln15$. Así, $S=\{4\}$. Condensar el producto no autoriza borrar el dominio original, y la raíz inadmisible no es un valor en el que la ecuación logarítmica sea falsa: allí no está definida.



#### Solución 75

El dominio racional y logarítmico es $D=(-\infty,-1)\cup(2,\infty)$. Como $1=\log_{1/2}(1/2)$ y el logaritmo es decreciente, la condición equivale sobre $D$ a $(x-2)/(x+1)\le1/2$. Restar $1/2$ da $(x-5)/(2(x+1))\le0$, cuya tabla de signos produce $(-1,5]$. La intersección con $D$ es $S=(2,5]$. En $5$ el argumento vale $1/2$ y la igualdad se admite; en $2$ vale cero y el logaritmo no existe. En la rama $x<-1$ el argumento es mayor que $1$, por lo que su logaritmo de base fraccionaria es negativo y no puede ser al menos $1$. Esta observación verifica independientemente la exclusión de esa rama.



#### Solución 76

El dominio en $x$ es $\mathbb R$ para todas las bases permitidas. Si $a>1$, escribir $a=a^1$ y usar la monotonía creciente da $x^2-1\le1$, equivalente a $x^2\le2$. Así, $S(a)=[-\sqrt2,\sqrt2]$. Si $0<a<1$, la monotonía decreciente invierte el orden y da $x^2-1\ge1$, es decir $S(a)=(-\infty,-\sqrt2]\cup[\sqrt2,\infty)$. En ambos regímenes los extremos se incluyen por igualdad. Para $a=1$, la comparación es $1\le1$ para todo real, luego $S(1)=\mathbb R$. Las regiones pasan del intervalo central a las dos regiones exteriores, y el caso constante no se obtiene igualando exponentes. Tampoco puede justificarse con $\log_1$, que no existe como inversa.



#### Solución 77

El logaritmo interior exige $x^2-1>0$. Sobre esa condición, la identidad inversa da $e^{\ln(x^2-1)}=x^2-1$. El logaritmo exterior exige además $x^2-4>0$, condición que implica la interior. Por tanto, el dominio completo es $D=(-\infty,-2)\cup(2,\infty)$. En él, la ecuación equivale a $\ln(x^2-4)=0$, luego $x^2-4=1$ y $x=\pm\sqrt5$. Ambos candidatos pertenecen a $D$ y producen argumento exterior $1$, así que $S=\{-\sqrt5,\sqrt5\}$. La simplificación interior es válida, pero la sustracción posterior puede producir valores no positivos; éstos deben excluirse antes de usar el logaritmo exterior.



#### Solución 78

La primera expresión exige $x>1$ y $\ln(x-1)\ne0$, es decir $x\ne2$. La segunda exige $x>0$, de modo que el dominio conjunto es $D=(1,2)\cup(2,\infty)$. Si $1<x<2$, entonces $\ln(x-1)<0$ y el cociente de la primera condición es negativo, así que no puede ser al menos $1/2$. Si $x>2$, el denominador es positivo y multiplicar por $2\ln(x-1)$ conserva el orden: $2\ln2\ge\ln(x-1)$. La monotonía de ln da $x-1\le4$, por lo que la primera condición selecciona $(2,5]$. La segunda, por base decreciente y $-2=\log_{1/2}4$, equivale a $x\le4$ sobre su dominio. Intersectando, $S=(2,4]$. En $4$ ambos requisitos se cumplen y la segunda es igualdad; en $2$ la primera expresión no existe. La separación de signos autoriza la multiplicación sólo en la rama positiva.



#### Solución 79

El dato inicial da $A=12$. El segundo da $12b^2=27$, de donde $b^2=9/4$ y la positividad selecciona $b=3/2$. El modelo es $Q(t)=12(3/2)^t$, y verifica ambos datos. Puesto que $3/2>1$, el umbral real equivale a $(3/2)^t\ge25/3$, es decir $t\ge t_*=\log_{3/2}(25/3)$. Este número es positivo porque $25/3>1$. Para observaciones enteras, $Q(5)=729/8<100$ y $Q(6)=2187/16>100$, con comparaciones exactas $729<800$ y $2187>1600$. La monotonía prueba que $5<t_*<6$ y que el primer día entero es $6$. Los datos determinan los parámetros dentro de la familia; la extensión a tiempos reales es una hipótesis adicional del modelo, no una conclusión de dos observaciones.



#### Solución 80

El denominador debe ser no nulo y el cociente positivo. Con $u=2^x>0$, la tabla de signos del argumento da $0<u<1$ o $u>4$. En ese dominio, ln creciente hace la comparación equivalente a $(u-1)/(u-4)\le2$. Restar $2$ da $(7-u)/(u-4)\le0$, que selecciona $u<4$ o $u\ge7$ entre los valores con denominador no nulo. Intersectando con el dominio y la imagen positiva queda $0<u<1$ o $u\ge7$. La vuelta creciente produce $S=(-\infty,0)\cup[\log_2 7,\infty)$. Como $\log_2 7>2$, la segunda región respeta el dominio. Para verificar sin repetir la tabla, escribimos el argumento como $1+3/(u-4)$. Si $0<u<1$, está entre $0$ y $1$, por lo que su logaritmo es menor que $0<\ln2$. Si $u>4$, la comparación con $2$ equivale, multiplicando por $u-4>0$, a $3\le u-4$, esto es $u\ge7$. En $u=7$ hay igualdad y se admite; en $u=1$ el argumento es cero y en $u=4$ el denominador se anula, de modo que $x=0,2$ permanecen excluidos. Ambas rutas cubren las dos ramas del dominio y confirman la respuesta.

### H. Soluciones de profundización y reconstrucción



#### Solución 081

Si $t\ne1$, la exponencial es estrictamente monótona y por ello inyectiva: $x-2=2x+1$ da $x=-3$. Sustituir produce $t^{-5}$ en ambos miembros. Si $t=1$, ambos valen uno para todo real $x$, luego $S(1)=\mathbb R$. No se usa un logaritmo de base uno. El sentido de monotonía cambia entre $0<t<1$ y $t>1$, pero la inyectividad sigue siendo válida en ambos casos.



#### Solución 082

Si $t>1$, la monotonía creciente da $2x-1\le x+3$, luego $x\le4$. Si $0<t<1$, la monotonía decreciente invierte la comparación y da $2x-1\ge x+3$, luego $x\ge4$. Si $t=1$, la igualdad $1\le1$ vale para todo real. En $x=4$ ambos exponentes coinciden y el extremo se incluye en las dos ramas no constantes. Las propiedades utilizadas para exponentes reales son las admitidas en [§23.2](algebra-para-matematicos-capitulo-23-funciones-exponenciales-y-logaritmos.md#apm-c23-s02).



#### Solución 083

El dominio es $x>-1$. Como $\log_{1/t}u=-\log_tu$ para $u>0$, la ecuación equivale a $2\log_t(x+1)=2$, luego $x+1=t$ y $x=t-1$. Este valor está en el dominio porque $t>0$. Sus logaritmos son $1$ y $-1$, de modo que verifica $1=-1+2$. La identidad entre bases sigue de $(1/t)^v=t^{-v}$ y la unicidad del exponente. El valor $t=1$ queda fuera de la familia porque ambos logaritmos serían indefinidos.



#### Solución 084

Con $u=t^{x/2}>0$, la ley de potencias da $u^2=2u$. Dividir por $u$ es seguro y deja $u=2$. Si $t\ne1$, la solución única es $x=2\log_t2$; sustituir da $t^x=4$ y $2t^{x/2}=4$. Si $t=1$, la ecuación original es $1=2$ y no tiene soluciones. La sustitución auxiliar no puede tratar $u=0$ como candidato ni suponer que la base uno alcanza todos los positivos.



#### Solución 085

Una elección es $F(x)=\log_q[(x-a)/(x-b)]$. El cociente existe fuera de $b$ y es positivo exactamente en las dos regiones exteriores a $a,b$. En $a$ vale cero y el logaritmo no existe; entre los dos puntos es negativo. Así el dominio es el prescrito. El sentido creciente o decreciente de la base no afecta esta condición de existencia, que solo exige argumento positivo.



#### Solución 086

Tomemos $F(x)=\log_2\sqrt{(x-a)(b-x)}$. La raíz existe cuando el producto es no negativo; el logaritmo exige que la raíz sea estrictamente positiva, equivalente a producto positivo. Este ocurre exactamente para $a<x<b$, porque ambos factores son positivos dentro y tienen signos opuestos fuera. En los extremos la raíz vale cero y la capa exterior falla. La segunda condición implica la primera, pero debe justificarse antes de reducir el dominio.



#### Solución 087

El argumento es positivo exactamente en $(a,b)$. Además, el denominador logarítmico no puede ser cero; esto ocurre cuando $(x-a)/(b-x)=1$, equivalente a $2x=a+b$. Así $D=(a,(a+b)/2)\cup((a+b)/2,b)$. En el punto medio el argumento es uno, por lo que falla solo la división exterior. En los extremos falla el argumento o el cociente. Todos los demás puntos tienen logaritmo definido y no nulo.



#### Solución 088

Primero $x>0$; después $\log_t x>0$. Si $t>1$, la monotonía creciente y $\log_t1=0$ dan $x>1$, luego $D=(1,\infty)$. Si $0<t<1$, la monotonía decreciente da $0<x<1$, luego $D=(0,1)$. Ambos extremos se excluyen: cero no admite el logaritmo interior y uno produce argumento exterior cero. Las condiciones exteriores se aplican al valor del logaritmo, no directamente al signo de $x$.



#### Solución 089

La inducción da $Q(n)=5\,2^n$: vale en cero y multiplicar por dos avanza un paso. La condición es $2^n\ge20$. Como $2^4=16<20<32=2^5$ y las potencias de base dos crecen, el primer paso es $n=5$. En el modelo continuo elegido $Q(t)=5\,2^t$, el umbral sería $t=\log_220$, situado estrictamente entre cuatro y cinco. Ese tiempo continuo requiere una hipótesis adicional a la recurrencia.



#### Solución 090

Como la sucesión decrece estrictamente, basta exigir $Q(3)\ge30$ y $Q(4)<30$. Estas condiciones son $b^3\ge3/8$ y $b^4<3/8$. Por monotonía de las potencias positivas equivalen a $\sqrt[3]{3/8}\le b<\sqrt[4]{3/8}$. Ambos extremos están en $(0,1)$ y el inferior es menor que el superior: para un número de ese intervalo, la raíz cuarta es mayor que la cúbica. El extremo izquierdo se admite porque la comparación del paso tres es no estricta; el derecho se excluye porque en el cuarto habría igualdad. Los pasos anteriores quedan descartados por monotonía.



#### Solución 091

Sustituir $t=ds$ da $Q=Q_0(b^{d/\tau})^s$. El requisito $b^{d/\tau}=b^2$ equivale, por inyectividad, a $d/\tau=2$, luego $d=2\tau$ horas. Esa elección es única cuando $b\ne1$ y comprobarla devuelve $Q_0b^{2s}$. Si $b=1$, la cantidad es constante y cualquier $d>0$ cumple un factor por unidad igual a $b^2=1$; la unidad no queda identificada por los datos. Se conserva el mismo proceso al cambiar las coordenadas temporales.



#### Solución 092

La monotonía estricta hace necesaria y suficiente la condición $b^{m-1}<5\le b^m$. Tomar raíces positivas da $5^{1/m}\le b<5^{1/(m-1)}$. Ambas fronteras son mayores que uno y el intervalo no es vacío. En el extremo inferior el paso $m$ alcanza exactamente el umbral y se admite; en el superior lo alcanzaría ya $m-1$, así se excluye. La clasificación cubre todos los factores que satisfacen el primer cruce, en vez de redondear un tiempo para una sola base.



#### Solución 093

El primer dato fuerza $A=6$; el segundo, $6b=9$ y $b=3/2$. Entonces $Q(2)=6(3/2)^2=27/2$, distinto de $14$. No existe un modelo de esa familia que ajuste los tres exactamente, pues los dos primeros ya fijaron ambos parámetros. La conclusión refuta ese ajuste, no la posibilidad de otros modelos ni una medición aproximada cuya tolerancia no fue especificada.



#### Solución 094

El dato exige $Ab^2=12$, luego todos los ajustes son $b>0$, $A=12/b^2$. No hay unicidad con un solo dato. El segundo da $Ab^5=12$; dividir por el primero produce $b^3=1$, y como $b>0$, $b=1$, $A=12$. La única función que ajusta ambos es la constante doce. Sustituir verifica los datos. Dos observaciones iguales en tiempos distintos fuerzan base uno dentro de esta familia, pero no prueban que cualquier proceso real entre esos tiempos sea constante.



#### Solución 095

Los primeros datos obligan $A=u$ y $b=(u+1)/u$. La predicción del tercero es $u b^2=(u+1)^2/u=u+2+1/u$. Igualarla a $u+3$ exige $1/u=1$, luego $u=1$. En ese caso $A=1,b=2$ y los tres valores son $1,2,4$, que coinciden. Para cualquier otro $u>0$ no hay ajuste exacto de esta familia. Todas las divisiones se hicieron por cantidades positivas.



#### Solución 096

La exponencial es $F(t)=Ab^t$. Defina $H(t)=Ab^t[1+(t-n)(n+1-t)]$ cuando $n\le t<n+1$, para cada entero $n\ge0$. El factor entre corchetes es al menos uno y vale uno en cada entero; en los límites derechos también tiende a uno. Así $H$ es positiva, coincide en todos los enteros con $F$ y difiere en $t=n+1/2$, donde el factor es $5/4$. Incluso todos los datos enteros no determinan por sí solos la extensión continua exponencial. No se afirma que $H$ conserve las leyes multiplicativas de esa extensión.

***

[← Capítulo 22](algebra-para-matematicos-capitulo-22-orden-e-inequaciones.md) · [Tomo I](../para-matematicos/algebra-para-matematicos.md) · [Capítulo 24 →](algebra-para-matematicos-capitulo-24-polinomios-operaciones-y-division.md)

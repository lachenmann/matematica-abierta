## Laboratorio de estructura funcional {#sec-t1-c03-10}

Hasta aquí hemos construido las piezas del lenguaje funcional una por una. Sabemos distinguir una fórmula de una función completamente especificada; calcular imágenes y preimágenes; decidir inyectividad y sobreyectividad; componer funciones con control de tipos; construir inversas; leer gráficas; trabajar con definiciones por tramos y reconocer la fuerza de la monotonía estricta.

Ahora cambia la tarea.

En los problemas que siguen **no se anunciará de antemano qué herramienta debe utilizarse**. La primera parte de cada solución será diagnosticar qué información importa y qué estructura del capítulo permite avanzar.

Conviene adoptar este protocolo general:

$$
\boxed{
\text{identificar la función}
\to
\text{auditar tipos y conjuntos}
\to
\text{elegir la estructura pertinente}
\to
\text{resolver}
\to
\text{revisar qué hipótesis fueron esenciales}
}
$$

El objetivo no es repetir mecánicamente definiciones. Es empezar a ver dominio, codominio, imagen, composición, inyectividad, inversa, gráfica y monotonía como partes de un mismo sistema.

### Laboratorio 1 — Qué sabemos y qué todavía falta

Alguien escribe solamente

$$
p(x)=\sqrt{4-x^2}.
$$

**Problema.** Determinar qué información puede inferirse de esa expresión y qué información falta todavía para tener una función completamente especificada. Después, construir dos funciones distintas que utilicen exactamente la misma fórmula.

#### Diagnóstico

La expresión contiene información algebraica. Como estamos trabajando con valores reales, la raíz cuadrada exige

$$
4-x^2\ge0.
$$

Pero una **restricción impuesta por la fórmula** no es todavía lo mismo que un dominio declarado. Tampoco aparece un codominio.

Debemos separar, por tanto, tres preguntas:

1. ¿para qué reales puede evaluarse la expresión?;
2. ¿qué conjunto elegimos efectivamente como dominio?;
3. ¿en qué conjunto declaramos que viven las salidas?

#### Solución

La condición

$$
4-x^2\ge0
$$

equivale a

$$
x^2\le4,
$$

y por tanto a

$$
-2\le x\le2.
$$

Así, el **dominio real máximo de la expresión** es

$$
[-2,2].
$$

Además, para todo $x\in[-2,2]$,

$$
0\le\sqrt{4-x^2}\le2.
$$

Eso permite definir, por ejemplo,

$$
f\colon[-2,2]\to[0,2],
\qquad
f(x)=\sqrt{4-x^2},
$$

y también

$$
g\colon[0,2]\to\mathbb R,
\qquad
g(x)=\sqrt{4-x^2}.
$$

Ambas funciones utilizan la misma fórmula, pero son funciones distintas porque sus dominios y codominios no coinciden.

Todavía podríamos construir muchas otras. Si $D\subseteq[-2,2]$, la misma expresión define una función sobre $D$; y cualquier codominio que contenga las salidas efectivas puede formar parte de una declaración válida.

Lo que **no** podemos hacer a partir de la fórmula aislada es decidir, por ejemplo, si «$p$ es sobreyectiva». La sobreyectividad depende del codominio declarado. Tampoco podemos preguntar sin más si «$p$ tiene inversa», porque antes debemos conocer la función completa y su inyectividad/sobreyectividad.

#### Lectura de la solución

Este primer laboratorio recupera la pregunta central del capítulo:

$$
\boxed{\text{una expresión restringe posibilidades, pero no especifica por sí sola toda la función}.}
$$

El dominio natural de una expresión es una información que podemos **deducir**. El dominio y el codominio de una función son datos que debemos **declarar**.

### Laboratorio 2 — Una fórmula, cuatro clasificaciones

Consideremos ahora la regla

$$
x\longmapsto x^2-1.
$$

Definamos

$$
f\colon\mathbb R\to\mathbb R,
\qquad
f(x)=x^2-1,
$$

$$
g\colon[0,\infty)\to[-1,\infty),
\qquad
g(x)=x^2-1,
$$

$$
h\colon\mathbb R\to[-1,\infty),
\qquad
h(x)=x^2-1,
$$

y

$$
k\colon[0,\infty)\to\mathbb R,
\qquad
k(x)=x^2-1.
$$

**Problema.** Determinar la imagen y clasificar cada función como inyectiva, sobreyectiva, biyectiva o ninguna de ellas.

#### Diagnóstico

La fórmula es idéntica en las cuatro declaraciones. Por tanto, el cálculo de valores no distingue las funciones. Las diferencias deben provenir de dos lugares:

- qué entradas están permitidas;
- qué conjunto se ha declarado como codominio.

El cuadrado sobre todo $\mathbb R$ identifica $x$ y $-x$, mientras que sobre $[0,\infty)$ preserva estrictamente el orden. Además,

$$
x^2-1\ge-1.
$$

Estas dos observaciones controlan casi toda la clasificación.

#### Solución

Para $f$ y $h$, el dominio es todo $\mathbb R$. Como

$$
f(1)=f(-1)=0
$$

y

$$
h(1)=h(-1)=0,
$$

ninguna de las dos funciones es inyectiva.

La imagen de la regla sobre $\mathbb R$ es

$$
[-1,\infty).
$$

En efecto, $x^2-1\ge-1$ para todo real $x$. Recíprocamente, si $y\ge-1$, entonces $y+1\ge0$ y podemos tomar

$$
x=\sqrt{y+1},
$$

para obtener

$$
x^2-1=y.
$$

Por tanto,

$$
\operatorname{Im}(f)=\operatorname{Im}(h)=[-1,\infty).
$$

Como el codominio de $f$ es $\mathbb R$, los valores menores que $-1$ no son alcanzados. Así,

$$
\boxed{f\text{ no es inyectiva ni sobreyectiva}.}
$$

En cambio, el codominio de $h$ es exactamente $[-1,\infty)$, de modo que

$$
\boxed{h\text{ es sobreyectiva pero no inyectiva}.}
$$

Consideremos ahora $g$ y $k$. Si

$$
0\le x_1<x_2,
$$

entonces, como vimos en §3.9,

$$
x_1^2<x_2^2,
$$

y al restar $1$ obtenemos

$$
x_1^2-1<x_2^2-1.
$$

La regla es, por tanto, estrictamente creciente sobre $[0,\infty)$ y las dos funciones son inyectivas.

Su imagen sigue siendo

$$
[-1,\infty),
$$

porque para cada $y\ge-1$ el número

$$
\sqrt{y+1}\in[0,\infty)
$$

satisface

$$
(\sqrt{y+1})^2-1=y.
$$

Así,

$$
\boxed{g\text{ es biyectiva},}
$$

mientras que

$$
\boxed{k\text{ es inyectiva pero no sobreyectiva}.}
$$

Podemos resumir:

| Función | Imagen | Inyectiva | Sobreyectiva | Biyectiva |
|---|---|---:|---:|---:|
| $f\colon\mathbb R\to\mathbb R$ | $[-1,\infty)$ | no | no | no |
| $g\colon[0,\infty)\to[-1,\infty)$ | $[-1,\infty)$ | sí | sí | sí |
| $h\colon\mathbb R\to[-1,\infty)$ | $[-1,\infty)$ | no | sí | no |
| $k\colon[0,\infty)\to\mathbb R$ | $[-1,\infty)$ | sí | no | no |

#### Lectura de la solución

La tabla muestra dos sensibilidades diferentes:

$$
\boxed{\text{la inyectividad responde al dominio}}
$$

y

$$
\boxed{\text{la sobreyectividad responde al codominio y a la imagen}.}
$$

Cambiar el dominio puede eliminar entradas que producían la misma salida. Cambiar el codominio puede convertir una función en sobreyectiva sin alterar ninguno de sus valores punto a punto.

### Laboratorio 3 — Componer empieza por verificar que se puede

Sean

$$
f\colon\mathbb R\to[0,\infty),
\qquad
f(x)=x^2,
$$

$$
g\colon[0,\infty)\to\mathbb R,
\qquad
g(u)=u+1,
$$

y

$$
h\colon(0,\infty)\to\mathbb R,
\qquad
h(u)=\frac1u.
$$

**Problema.** Decidir cuáles de las composiciones

$$
g\circ f,
\qquad
f\circ g,
\qquad
h\circ f,
\qquad
f\circ h,
\qquad
h\circ g
$$

están definidas con las funciones tal como han sido declaradas. Calcular las que existan y explicar por qué el orden de composición importa.

#### Diagnóstico

Antes de sustituir fórmulas debemos auditar tipos. Para que $v\circ u$ esté definida sobre todo el dominio de $u$ necesitamos

$$
\operatorname{Im}(u)\subseteq\operatorname{Dom}(v).
$$

Esta condición es anterior a cualquier simplificación algebraica.

#### Solución

Como

$$
\operatorname{Im}(f)=[0,\infty)
$$

y ese conjunto es exactamente el dominio de $g$, existe

$$
g\circ f\colon\mathbb R\to\mathbb R,
$$

con

$$
(g\circ f)(x)=g(x^2)=x^2+1.
$$

También existe $f\circ g$. En efecto,

$$
\operatorname{Im}(g)=[1,\infty)\subseteq\mathbb R=\operatorname{Dom}(f).
$$

Por tanto,

$$
f\circ g\colon[0,\infty)\to[0,\infty)
$$

y

$$
(f\circ g)(u)=f(u+1)=(u+1)^2.
$$

Estas dos composiciones ya muestran que el orden importa. Bajo nuestra convención ni siquiera son la misma función, porque tienen dominios y codominios distintos. Incluso si comparamos un valor perteneciente a ambos dominios, por ejemplo $2$, obtenemos

$$
(g\circ f)(2)=5
$$

mientras que

$$
(f\circ g)(2)=9.
$$

Examinemos ahora $h\circ f$. Para que existiera sobre todo $\mathbb R$ necesitaríamos

$$
f(\mathbb R)\subseteq(0,\infty).
$$

Pero

$$
f(0)=0\notin(0,\infty).
$$

Así,

$$
\boxed{h\circ f\text{ no está definida como composición sobre todo }\mathbb R.}
$$

Es cierto que la expresión formal

$$
\frac1{x^2}
$$

puede evaluarse cuando $x\ne0$. Pero eso produciría una función sobre $\mathbb R\setminus\{0\}$, no la composición $h\circ f$ con el dominio original de $f$.

En cambio, $f\circ h$ sí existe porque

$$
\operatorname{Im}(h)=(0,\infty)\subseteq\mathbb R=\operatorname{Dom}(f).
$$

Entonces

$$
(f\circ h)(u)
=
\left(\frac1u\right)^2
=
\frac1{u^2},
\qquad u>0.
$$

Finalmente,

$$
\operatorname{Im}(g)=[1,\infty)\subseteq(0,\infty)=\operatorname{Dom}(h),
$$

por lo que también existe $h\circ g$ y

$$
(h\circ g)(u)=\frac1{u+1},
\qquad u\ge0.
$$

#### Lectura de la solución

El error que debemos evitar es

$$
\boxed{\text{ver dos fórmulas y componerlas antes de mirar sus tipos}.}
$$

Una expresión algebraica simplificada puede tener sentido en ciertos puntos aun cuando la composición de las funciones originalmente declaradas no exista sobre todo el dominio requerido.

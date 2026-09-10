$$
\boxed{
\text{estatus físico}
\not=
\text{forma algebraica}
}
$$
Esta es la regla central de la sección.
La cuestión decisiva no es la forma gráfica de la ecuación, sino su **procedencia y función dentro del argumento**. Por eso, al leer una derivación física, la primera pregunta será: «¿de dónde viene esta afirmación?».

::: {.ma-block .ma-definicion #fpm-i-01-d18}
**Definición operativa FPM-I-01-D18 — Estatus de una afirmación**
El **estatus** de una afirmación dentro de un modelo o teoría indica el papel epistemológico y lógico que cumple: si fija significado, resume evidencia empírica, introduce un postulado, especifica una idealización, declara una aproximación, fija condiciones, conecta con observaciones o se deduce matemáticamente de premisas ya aceptadas.
:::

La palabra **dentro** es esencial.

Una expresión puede cambiar de estatus cuando cambia el contexto.

No clasificamos fórmulas por su aspecto, sino **afirmaciones situadas**.
### 6.2. Las nueve etiquetas canónicas

Usaremos las siguientes etiquetas:

| Etiqueta | Estatus | Pregunta principal |
|---|---|---|
| `[DEF]` | definición | ¿estamos fijando el significado de algo? |
| `[EMP]` | ley o relación empírica | ¿su respaldo depende de observación o experimento? |
| `[POST]` | postulado o principio físico | ¿se introduce como hipótesis estructural de la teoría? |
| `[MOD]` | hipótesis de modelo / idealización | ¿qué rasgo del sistema real estamos sustituyendo o simplificando? |
| `[APPROX]` | aproximación | ¿qué diferencia o efecto despreciamos y en qué régimen? |
| `[IC]` | condición inicial | ¿qué se fija al comienzo del problema dinámico? |
| `[BC]` | condición de frontera | ¿qué se prescribe en una frontera? |
| `[MATH]` | consecuencia matemática | ¿se deduce sin introducir una nueva premisa física? |
| `[OBS]` | relación de observación o medición | ¿cómo se conecta el formalismo con un procedimiento experimental? |

No todas aparecerán en todos los problemas.

Pero cuando una relación importante aparece por primera vez, el lector debe poder identificar su tipo.
Las etiquetas forman un vocabulario de lectura. Conviene reunir aquí sus diferencias esenciales sin repetir nueve veces el mismo esquema.

#### `[DEF]`, `[EMP]` y `[POST]`

Una definición fija significado.

Por ejemplo, si dos instantes registrados son $t_i$ y $t_f$, podemos definir

$$
[\mathrm{DEF}]
\qquad
\Delta t:=t_f-t_i.
$$
No hemos descubierto experimentalmente que

$$
\Delta t=t_f-t_i.
$$
Hemos decidido usar el símbolo $\Delta t$ para esa diferencia.

La definición puede estar motivada físicamente, pero su verdad no se contrasta como una ley.

Una vez aceptada, podemos usarla en deducciones.

##### Pregunta de control

> ¿la ecuación afirma algo sobre el comportamiento del mundo, o está fijando el significado de un símbolo?
Una relación empírica obtiene su respaldo de observaciones o experimentos.

Esquemáticamente:

$$
[\mathrm{EMP}]
\qquad
Y=f(X;\theta)
$$
significa que la relación se acepta porque describe, dentro de cierto dominio, una regularidad del mundo físico.

No necesitamos todavía estudiar una ley concreta.

Lo importante es reconocer que:

$$
\boxed{
\text{una ley empírica no se demuestra solo con álgebra}
}
$$
Podemos demostrar consecuencias **a partir** de ella.

Pero su conexión con la realidad requiere contraste.

##### Pregunta de control

> si ninguna observación del mundo pudiera contar a favor o en contra de esta relación, ¿seguiríamos llamándola empírica?
Un postulado no es una simple abreviatura ni una observación aislada.

Es una hipótesis estructural que se adopta como parte de una teoría.

Podemos representarlo esquemáticamente:

$$
[\mathrm{POST}]
\qquad
P.
$$
Después podremos derivar consecuencias:

$$
P\Longrightarrow Q.
$$
Entonces $Q$ puede tener estatus `[MATH]` relativo al postulado $P$.

La teoría no «demuestra» $P$ usando sus propias consecuencias.

Su justificación física proviene de la coherencia del marco, sus éxitos, su relación con experimentos y su integración con otras estructuras.

##### Pregunta de control

> ¿esta afirmación funciona como una premisa estructural del marco teórico?
#### `[MOD]` y `[APPROX]`

En §4 vimos ejemplos:

$$
[\mathrm{MOD}]
\qquad
\text{«el cuerpo se trata como partícula puntual».}
$$
o

$$
[\mathrm{MOD}]
\qquad
\text{«el hilo se considera inextensible».}
$$
Estas afirmaciones no pretenden ser literalmente verdaderas del objeto real.

Son exactas **dentro del modelo**.

Cada `[MOD]` debe permitir responder:

1. ¿qué propiedad real se omite o idealiza?;
2. ¿por qué creemos que no importa para la pregunta?;
3. ¿qué observación podría mostrar que sí importa?

Esta es una de las reglas de auditoría más importantes de la obra.
Una aproximación declara una sustitución:

$$
A\approx B.
$$
Pero el símbolo $\approx$ no constituye una justificación.

Debemos registrar, cuando sea posible:

- qué término o efecto se desprecia;
- qué cantidad controla su tamaño;
- respecto de qué escala es pequeño;
- cuándo esperamos que el reemplazo falle.

Por ejemplo:

$$
[\mathrm{APPROX}]
\qquad
1-2\varepsilon+\varepsilon^2
\approx
1-2\varepsilon
$$
solo es informativo si añadimos un régimen en el que $|\varepsilon|$ sea suficientemente pequeño para la precisión buscada.

##### Pregunta de control

> ¿qué diferencia concreta estamos aceptando?
Este es un punto especialmente delicado.

Supongamos que una ecuación final no contiene cierto efecto $D$.

Podemos llegar a ella de dos maneras:

##### Ruta A — Idealización

Declaramos:

$$
[\mathrm{MOD}]
\qquad
D=0.
$$
Dentro del modelo, el efecto es exactamente nulo.

##### Ruta B — Aproximación

Partimos de

$$
D\neq0
$$
pero mostramos que, en el régimen estudiado,

$$
|D|
\ll
\text{escala relevante},
$$
y entonces escribimos

$$
[\mathrm{APPROX}]
\qquad
D\approx0.
$$
La ecuación simplificada puede ser la misma.

El razonamiento físico no.
#### `[IC]`, `[BC]`, `[MATH]` y `[OBS]`

Una condición inicial especifica información del estado en un instante elegido como inicial.

Por ejemplo:

$$
[\mathrm{IC}]
\qquad
x(0)=a.
$$
La relación no es una ley universal.

No afirma que todos los sistemas tengan $x(0)=a$.

Describe una realización o preparación particular.

Una condición inicial puede provenir de:

- una medición;
- una preparación experimental;
- un enunciado de problema;
- una elección hipotética.

##### Pregunta de control

> ¿esta ecuación describe la regla de evolución o especifica desde qué estado comenzamos?
Una condición de frontera especifica información en el borde de un dominio.

Por ejemplo, en un problema posterior podríamos encontrar simbólicamente

$$
[\mathrm{BC}]
\qquad
u=0
\quad
\text{en una frontera}.
$$
No necesitamos saber todavía resolver una ecuación de frontera.

Solo distinguir:

$$
\boxed{
\text{ley en el interior}
\neq
\text{condición prescrita en el borde}.
}
$$
La misma fórmula $u=0$ puede ser una condición de frontera, una condición inicial o una solución, dependiendo del contexto.
Esta es la categoría más familiar para un lector matemático.

Supongamos que ya hemos declarado:

$$
A=B,
$$
$$
B=C.
$$
Entonces, por transitividad de la igualdad,

$$
[\mathrm{MATH}]
\qquad
A=C.
$$
No hemos añadido nueva física.

Hemos deducido una consecuencia lógica.

La regla crítica del proyecto es:

$$
\boxed{
\text{la prueba matemática comienza después de declarar las premisas físicas}.
}
$$
Una derivación física completa puede mezclar varios estatus, pero cada tramo deductivo debe dejar claro qué usa como premisa.
Si de un modelo obtenemos matemáticamente

$$
P,
$$
entonces $P$ es una consecuencia del modelo.

Pero todavía debemos distinguir:

$$
\boxed{
\text{«el modelo implica }P\text{»}
}
$$
de

$$
\boxed{
\text{«el experimento observa }P\text{».}
}
$$
La primera afirmación puede estar demostrada.

La segunda requiere contraste físico.

Esta separación será decisiva en §13.
Supongamos que un modelo contiene una cantidad $x$.

Para compararla con el laboratorio necesitamos alguna conexión como

$$
[\mathrm{OBS}]
\qquad
x
\longleftrightarrow
\text{procedimiento de medición}.
$$
En un experimento con video, por ejemplo, una coordenada física puede inferirse a partir de píxeles mediante una calibración.

La regla que convierte señal instrumental en valor físico no es automáticamente una ley dinámica.

Es una **relación de observación**.

##### Pregunta de control

> ¿esta relación nos dice cómo evoluciona el sistema o cómo obtenemos un dato sobre él?
### 6.3. Leer una derivación como una cadena de estatus

Construyamos una cadena deliberadamente elemental.

Supongamos que registramos dos instantes $t_i$ y $t_f$.

#### Paso 1 — Definición

$$
[\mathrm{DEF}]
\qquad
\Delta t:=t_f-t_i.
$$
#### Paso 2 — Observación

El aparato produce lecturas:

$$
[\mathrm{OBS}]
\qquad
t_i=2.0,
\qquad
t_f=5.0.
$$
No discutimos todavía incertidumbres.

#### Paso 3 — Consecuencia matemática

Sustituimos:

$$
[\mathrm{MATH}]
\qquad
\Delta t=5.0-2.0.
$$
Entonces:

$$
[\mathrm{MATH}]
\qquad
\Delta t=3.0.
$$
La cadena es transparente porque vemos dónde entró el dato y dónde comenzó la deducción.

Si escribiéramos simplemente

$$
\Delta t=t_f-t_i=5.0-2.0=3.0,
$$
la matemática sería correcta, pero el origen epistemológico de cada parte quedaría oculto.
Podemos representar una derivación física típica como una secuencia:

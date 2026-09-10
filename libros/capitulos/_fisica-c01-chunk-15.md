como si cada palabra designara simplemente un conjunto matemático contenido en otro.

La relación es **funcional**: una teoría puede contener o motivar leyes, y sus principios permiten construir modelos; un modelo puede emplear leyes y postulados, pero además necesita sistema, interpretación, parámetros, condiciones, idealizaciones y régimen de validez.
#### Ley física

::: {.ma-block .ma-definicion #fpm-i-01-d19}
**Definición operativa FPM-I-01-D19 — Ley física**
Llamaremos **ley física**, en sentido operativo, a una relación, regularidad o principio que expresa una estructura estable del comportamiento físico dentro de un dominio declarado y que puede emplearse como parte de la descripción o predicción de una clase de fenómenos.
:::

Esta definición es deliberadamente amplia.

No exige que toda ley sea:

- una ecuación;
- una relación exacta;
- puramente empírica;
- universal;
- independiente de una teoría;
- válida en todas las escalas.

La palabra «ley» tiene una historia compleja en física.

Nuestro objetivo no es imponer una única filosofía de las leyes naturales, sino poder leer correctamente un texto físico.
La taxonomía de §6 no desaparece cuando usamos la palabra «ley».

Una relación llamada históricamente «ley» puede aparecer principalmente como:

$$
[\mathrm{EMP}]
$$

si enfatizamos que resume una regularidad observada.

Otra relación puede aparecer como:

$$
[\mathrm{POST}]
$$

si dentro de cierta presentación funciona como principio estructural de una teoría.

Y una relación llamada «ley» en lenguaje informal puede resultar, dentro de otra formulación, una consecuencia matemática:

$$
[\mathrm{MATH}]
$$

de principios más generales.

Por eso:

$$
\boxed{
\text{«ley» no reemplaza la etiqueta de estatus}
}
$$

Cuando una ley importante aparezca en este libro, seguiremos preguntando:

> **¿qué estatus tiene aquí?**
La palabra «ley» puede sugerir algo sin excepciones y válido en todo contexto.

En física esto sería peligroso.

Una ley puede describir con enorme precisión un régimen y dejar de ser adecuada fuera de él.

Por eso una afirmación física debe viajar junto con algún dominio o régimen:

$$
\boxed{
\text{ley física utilizada}
+
\text{régimen de aplicación}
}
$$

Una relación válida para cierto tipo de sistema, intervalo de variables o escala no queda desacreditada simplemente porque exista un régimen donde deje de funcionar.

Lo correcto es especificar **dónde** y **para qué** se utiliza.

Esta idea se desarrollará sistemáticamente en §11.
#### Modelo físico

En §5 construimos la plantilla formal

$$
\mathcal M
=
(\mathcal S,X,\theta,\mathcal L,I,B,\mathcal R)
$$

acompañada por un diccionario de interpretación

$$
\mathfrak I_{\mathcal M}.
$$

Ahora podemos condensar esa arquitectura.

::: {.ma-block .ma-definicion #fpm-i-01-d20}
**Definición operativa FPM-I-01-D20 — Modelo físico**
Un **modelo físico** es una representación estructurada de un sistema o de una clase de sistemas que selecciona estados, variables, parámetros, relaciones, condiciones, idealizaciones, aproximaciones y reglas de interpretación suficientes para responder determinadas preguntas dentro de un régimen de validez.
:::

La frase **suficientes para responder determinadas preguntas** conecta directamente con `FPM-I-01-MP11`.

Un modelo no es simplemente:

$$
\text{ecuación}
+
\text{números}.
$$

Es una arquitectura de representación.
Consideremos de nuevo la Tierra.

Según la pregunta podemos utilizar modelos muy diferentes:

- plano local;
- esfera;
- cuerpo rígido;
- masa puntual;
- distribución continua.

No hemos cambiado de planeta.

Hemos cambiado de representación.

Por tanto:

$$
\boxed{
\text{un sistema físico}
\not\longrightarrow
\text{un único modelo obligatorio}
}
$$

La multiplicidad de modelos no es necesariamente una deficiencia.

Puede reflejar el hecho de que distintas preguntas seleccionan estructuras distintas.
#### Teoría física

Una teoría física debe permitir algo más general que describir una única realización.

Debe proporcionar una organización estable que nos diga, por ejemplo:

- qué tipos de sistemas o entidades consideramos;
- qué cantidades pueden representar sus estados;
- qué principios estructurales aceptamos;
- qué relaciones están permitidas;
- cómo construir modelos particulares;
- qué transformaciones dejan intacta la descripción física;
- qué observables pueden compararse con experimentos;
- qué clases de problemas quedan dentro del dominio de la teoría.

No todas las teorías responden estas preguntas del mismo modo.

Pero esta lista muestra una diferencia de escala conceptual.
::: {.ma-block .ma-definicion #fpm-i-01-d21}
**Definición operativa FPM-I-01-D21 — Teoría física**
Una **teoría física** es un marco conceptual y matemático que organiza una familia de modelos mediante conceptos, principios, estructuras, reglas de construcción e interpretación compartidos, y que permite formular consecuencias contrastables para una clase amplia de fenómenos.
:::

Una teoría no tiene por qué presentarse como una lista finita de axiomas.

Tampoco toda la física se organiza históricamente con una única forma lógica.

La definición es una guía de lectura.
Una teoría útil debe sobrevivir al cambio de problema.

Dentro de un mismo marco podremos estudiar, más adelante:

- partículas;
- sistemas de varias partículas;
- cuerpos rígidos;
- osciladores;
- sistemas sometidos a restricciones;
- campos.

Los modelos pueden parecer matemáticamente muy diferentes.

Lo que los reúne es que comparten parte de la arquitectura teórica.

Por eso:

$$
\boxed{
\text{unidad teórica}
\neq
\text{uniformidad superficial de las ecuaciones}
}
$$

La unidad puede encontrarse en principios, simetrías, estructuras o reglas de construcción.
### 7.2. Cómo se relacionan sin confundirse

Una ley puede ser ingrediente de un modelo; un modelo representa un sistema o una clase de sistemas; una teoría organiza familias de modelos mediante principios, estructuras y reglas de interpretación. Esta relación es funcional, no una inclusión conjuntista literal.

Supongamos que conocemos una ley esquemática:

$$
Y=kX.
$$

¿Podemos predecir ya un experimento concreto?

No necesariamente.

Todavía puede faltar:

- qué sistema estudiamos;
- qué valor tiene $k$ para ese sistema;
- cuál es el estado inicial;
- qué cantidad controlamos;
- cómo medimos $X$;
- cómo medimos $Y$;
- qué idealizaciones hemos hecho;
- si el régimen experimental está dentro del dominio de validez.

Así aparece el siguiente nivel:

$$
\boxed{
\text{una ley puede ser un ingrediente de un modelo,
pero no sustituye al modelo completo}
}
$$
Podemos distinguir tres niveles.

#### Nivel 1 — Teoría

Proporciona una arquitectura general.

#### Nivel 2 — Modelo

Selecciona una clase concreta de sistemas, variables, parámetros, hipótesis y condiciones.

#### Nivel 3 — Realización

Fija valores o datos particulares.

Esquemáticamente:

$$
\text{teoría}
\longrightarrow
\text{familia de modelos}
\longrightarrow
\text{realización concreta}
\longrightarrow
\text{predicciones}.
$$

Pero para llegar al experimento debemos añadir la capa de observación:

$$
\text{predicciones del modelo}
\longleftrightarrow
[\mathrm{OBS}]
\longleftrightarrow
\text{datos}.
$$
Nuestro péndulo sirve para visualizar la jerarquía sin usar todavía leyes de movimiento.

#### Sistema físico

Esfera, hilo y entorno seleccionado.

#### Modelo

Decidimos:

- qué pertenece al sistema;
- si la esfera se trata como partícula puntual;
- si el hilo se considera inextensible;
- qué cantidades describen el estado;
- qué parámetros permanecen fijos;
- qué condiciones iniciales se preparan;
- qué efectos se omiten;
- qué observables registramos.

#### Teoría

Más adelante introduciremos un marco mecánico general que proporcionará principios para construir la dinámica de muchos sistemas distintos, no solo de este péndulo.

El punto importante es:

$$
\boxed{
\text{la teoría no es «la teoría del péndulo»;
el péndulo es un modelo particular construido dentro de un marco más general}
}
$$

Todavía no necesitamos conocer ese marco para comprender la jerarquía.
La misma situación experimental puede admitir representaciones de distinto nivel sin que las palabras históricas «ley», «modelo» o «teoría» se utilicen siempre con idéntico alcance.

Consideremos un dispositivo óptico.

Podemos describir ciertos fenómenos mediante **rayos**.

En otras preguntas necesitamos una descripción **ondulatoria**.

Más adelante, para otros fenómenos, necesitaremos una descripción **cuántica**.

No desarrollaremos todavía ninguna de esas teorías.

Solo observaremos la arquitectura.

El mismo dispositivo físico puede admitir descripciones diferentes porque cambian:

- las escalas relevantes;
- los observables;
- el tipo de pregunta;
- la precisión;
- los fenómenos que queremos capturar.

Así:

$$
\boxed{
\text{cambiar de modelo o de marco teórico}
\not\Rightarrow
\text{que una descripción anterior haya sido inútil}
}
$$

Puede seguir siendo excelente dentro de su régimen.
Hay nombres establecidos por tradición que pueden resultar engañosos.

Algo llamado «modelo» puede ser un marco teórico extraordinariamente amplio.

Algo llamado «ley» puede ocupar el papel de postulado.

Algo llamado «teoría» puede designar una familia histórica de formulaciones distintas.

Por eso no corregiremos automáticamente el vocabulario histórico de la física.

Haremos algo más útil:

> **preguntaremos qué función cumple el objeto en el argumento presente.**

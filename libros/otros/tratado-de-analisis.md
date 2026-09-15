---
title: "Tratado de análisis"
description: "Tratado moderno de análisis que reconstruye los sistemas numéricos desde fundamentos explícitos y desarrolla progresivamente el análisis real."
author: "Gustav A. Tachek"
content-id: MA-BOK-0003
content-type: book
status: published
date-created: 2026-09-09
date-modified: 2026-09-14
areas:
  - fundamentos
  - analisis
level: avanzado
topics:
  - fundamentos
  - teoria-de-conjuntos
  - numeros-naturales
  - numeros-enteros
  - numeros-racionales
  - numeros-reales
  - completitud
prerequisites: []
related:
  - MA-BCH-0005
  - MA-BCH-0006
  - MA-BCH-0007
  - MA-BCH-0019
  - MA-BCH-0020
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
---

# Tratado de análisis

**Gustav A. Tachek**

Este tratado desarrolla el análisis matemático desde fundamentos explícitos y construye progresivamente los sistemas numéricos que el análisis utiliza. La edición web se publica por etapas: cada parte se incorpora cuando ha superado su revisión matemática y editorial.

## Prefacio

Este tratado nace de una intención sencilla de formular, aunque exigente de llevar a cabo: **desarrollar el análisis matemático desde fundamentos explícitos, con todo el rigor necesario, sin renunciar por ello a la claridad, la continuidad del pensamiento y el placer de comprender**.

No queremos presentar los conceptos fundamentales del análisis como objetos ya terminados que el lector deba aceptar antes de comenzar. Preferimos reconstruir el camino que conduce hasta ellos. Los números naturales, enteros, racionales y reales no aparecerán simplemente porque sean familiares: serán construidos; sus operaciones serán definidas; sus propiedades, demostradas. Sólo después podremos utilizarlos con la libertad que habitualmente damos por supuesta.

Este principio guía toda la obra:

> **Nada debe utilizarse antes de haber sido definido, construido o demostrado, salvo aquello que haya sido declarado explícitamente como fundamento.**

Pero rigor no tiene por qué significar aridez. Cada construcción importante procurará comenzar por el problema que la hace necesaria. Los enteros aparecen porque en los naturales la sustracción no siempre es posible; los racionales, porque los enteros no bastan para resolver toda división; los números reales surgirán, a su vez, de una insuficiencia más profunda de los racionales. Queremos que el lector pueda reconocer no sólo **cómo** se construye un objeto matemático, sino también **por qué vale la pena construirlo**.

Las demostraciones seguirán el mismo criterio. Aspiramos a que sean completas, pero también legibles: que indiquen su estrategia, hagan visibles sus pasos esenciales y permitan reconstruir la razón de cada argumento. La notación deberá servir al pensamiento en vez de enmascararlo.

Detrás del texto existe además una infraestructura de control: registramos dependencias entre resultados, revisamos la coherencia de las definiciones y, cuando resulta apropiado, contrastamos partes del desarrollo mediante herramientas de verificación formal. Estos mecanismos son auxiliares. **La prueba destinada al lector seguirá siendo siempre una demostración matemática humana, completa y comprensible.**

La publicación abierta y progresiva de este tratado forma parte de la misma filosofía. El texto irá creciendo capítulo a capítulo, y las versiones publicadas podrán ser corregidas, ampliadas y perfeccionadas. No queremos ocultar que una obra matemática extensa también se construye: esperamos que la web permita conservar esa condición viva sin sacrificar la estabilidad y el rigor de aquello que ya ha sido establecido.

Nuestro ideal podría resumirse en una fórmula:

$$
\boxed{\text{claridad de una conversación matemática seria}
\; + \;
\text{rigor de una formalización moderna}}
$$

Si este tratado consigue que una demostración rigurosa no se sienta como un obstáculo para comprender, sino como una forma más profunda de comprensión, habrá cumplido una parte esencial de su propósito.

---

## Cómo leer este libro

Este libro ha sido escrito como un **tratado**. Esa palabra no designa aquí simplemente un libro extenso, sino una forma particular de organizar el conocimiento matemático: cada concepto debe aparecer cuando existen ya los elementos necesarios para definirlo; cada resultado debe apoyarse únicamente en aquello que ha sido establecido antes; y cada nueva estructura debe construirse, en la medida de lo posible, a partir de las anteriores.

El principio que gobierna toda la obra puede formularse así:

> **Nada se utiliza antes de haber sido definido, construido o demostrado, salvo aquello que pertenezca expresamente al fundamento declarado del libro.**

Esta elección tiene consecuencias para la lectura.

En muchos textos de análisis se comienza dando por conocidos los números reales, sus operaciones, su orden y sus propiedades fundamentales. Aquí el camino es diferente. Partimos mucho antes. Construiremos sucesivamente los objetos y las estructuras que harán posible el análisis: conjuntos, relaciones, funciones, números naturales, enteros, racionales y, finalmente, los números reales por más de un procedimiento.

Esto significa que ciertos capítulos iniciales pueden parecer alejados de aquello que habitualmente se entiende por análisis. No lo están. Cada uno prepara una parte del lenguaje que después utilizaremos sin ambigüedad. Cuando aparezca una cortadura de Dedekind, una sucesión de Cauchy, un supremo, una función continua o una derivada, las nociones necesarias para comprender exactamente qué clase de objeto estamos manipulando ya habrán sido construidas.

No es necesario, sin embargo, leer todas las páginas con la misma intensidad.

Una **primera lectura** puede seguir el hilo principal: las motivaciones que abren cada construcción, las definiciones, los enunciados de los resultados fundamentales y los comentarios que explican qué se ha ganado después de demostrarlos. Esta lectura permite comprender la arquitectura de la teoría sin detenerse necesariamente en cada detalle técnico de cada demostración.

Una **segunda lectura**, más lenta, puede concentrarse en las demostraciones. En ella conviene preguntarse no sólo por qué el argumento es correcto, sino también por qué las hipótesis son necesarias, qué resultados anteriores están siendo utilizados y qué cambiaría si alguna de esas piezas faltara. Buena parte del contenido matemático profundo de un tratado se encuentra precisamente en esas relaciones.

Existe también una tercera forma de lectura, más cercana a la verificación: reconstruir la cadena deductiva completa. La edición web facilita esta lectura mediante encabezados estables, enlaces internos y el [glosario matemático](tratado-de-analisis-glosario.md), que permiten regresar al lugar exacto donde una noción fue introducida o un resultado quedó establecido.

Estas herramientas de navegación no sustituyen a la exposición matemática. Su función es hacer más visible una estructura deductiva que en muchos libros permanece implícita.

Algunas partes de la obra poseen además una verificación formal complementaria mediante asistentes de prueba. Esta capa tampoco reemplaza las demostraciones destinadas al lector humano. Una prueba formal certifica que cierta cadena de inferencias puede ser verificada dentro de un sistema preciso; una demostración matemática debe, además, mostrar por qué la idea funciona, cuáles son sus puntos decisivos y cómo se relaciona con el resto de la teoría. Ambas tareas son valiosas, pero no son idénticas.

Por esta razón, las demostraciones de este libro procuran no reducirse a una sucesión de manipulaciones simbólicas. Antes de las construcciones importantes se explicará qué problema intentamos resolver y por qué las herramientas anteriores todavía no bastan. Después de los resultados principales se señalará qué nueva posibilidad matemática ha quedado abierta.

Hay también una precaución terminológica importante. Los distintos sistemas numéricos que aparecen en el libro son **objetos construidos**. Por ello no identificaremos silenciosamente, por ejemplo, un número racional con el real que posteriormente lo representa. Primero construiremos una aplicación canónica

$$
\mathbb Q\longrightarrow\mathbb R,
$$

demostraremos las propiedades pertinentes de esa aplicación y sólo entonces utilizaremos, cuando sea conveniente, las identificaciones habituales. Esta insistencia puede parecer excesiva al principio, pero evita una de las fuentes más comunes de circularidad cuando se intenta construir rigurosamente los números reales.

Algo semejante sucede con resultados conocidos. Que un teorema sea familiar no significa que pueda utilizarse antes de que sus hipótesis y conceptos estén disponibles. El orden de exposición importa. En este tratado, una afirmación elemental situada demasiado pronto puede ser lógicamente más problemática que un teorema difícil situado en el lugar correcto.

Esto no significa que el lector deba retener en la memoria todas las definiciones y todos los lemas anteriores. El libro está pensado también como obra de consulta. Cuando un término técnico, una construcción o una propiedad no resulte inmediata, las referencias internas y el glosario permiten regresar al lugar exacto donde fue introducido.

Conviene, por último, no confundir **lentitud** con **dificultad**.

Algunas páginas avanzarán despacio porque estaremos construyendo cuidadosamente los cimientos. Otras recorrerán grandes distancias con relativa rapidez porque esos cimientos ya estarán disponibles. La paciencia invertida al comienzo produce economía más adelante: una vez demostrado un resultado estructural, podrá reutilizarse sin reconstruir continuamente sus detalles.

El objetivo de este libro no es que el lector acepte que los números reales existen, ni que aprenda solamente a operar con ellos. Es mostrar cómo puede levantarse, desde fundamentos explícitos, la estructura sobre la cual descansa el análisis.

Por eso la pregunta que acompaña toda la obra no es únicamente

$$
\text{«¿es verdadero?»}
$$

sino también

$$
\boxed{\text{«¿de dónde viene, de qué depende y por qué podemos usarlo aquí?»}}
$$

Leer este tratado consiste, en buena medida, en aprender a seguir esa pregunta.

## Contenido disponible

1. [**Capítulo 0 — Fundamento lógico y conjuntista**](../capitulos/tratado-de-analisis-capitulo-0-fundamento-logico-y-conjuntista.md) (`MA-BCH-0005`) — **capítulo completo**: lógica ambiente y axiomas conjuntistas; operaciones de conjuntos; pares ordenados y productos cartesianos; relaciones; clases de equivalencia y cocientes; funciones, composición, biyectividad, imagen y preimagen; proyección canónica y definición sobre clases; familias indexadas; teoría abstracta del orden; resumen de notación, cierre deductivo y transición hacia los números naturales.
2. [**Capítulo 1 — Los números naturales**](../capitulos/tratado-de-analisis-capitulo-1-los-numeros-naturales.md) (`MA-BCH-0007`) — **capítulo completo**: construcción de $\mathbb N=\omega$, inducción, estructura de Peano, teorema de recursión, suma y producto naturales, construcción del orden natural como orden total compatible con las operaciones, principio de buen orden, inducción fuerte, balance estructural, notas bibliográficas y transición hacia los números enteros.

   $$
   m\leq n\iff\exists k\in\mathbb N\;(n=m+k)\iff m\subseteq n,
   \qquad
   m<n\iff m\in n.
   $$

3. [**Capítulo 2 — Los números enteros**](../capitulos/tratado-de-analisis-capitulo-2-los-numeros-enteros.md) (`MA-BCH-0019`) — **capítulo completo**. A partir de diferencias formales y del cociente

   $$
   \mathbb Z=(\mathbb N\times\mathbb N)/{\sim_{\mathbb Z}},
   $$

   se construyen suma, opuesto, sustracción y producto sobre clases. Se demuestra que $\mathbb Z$ es un dominio de integridad totalmente ordenado. La incrustación canónica

   $$
   \iota_{\mathbb N}^{\mathbb Z}(n)=[(n,0)]
   $$

   es inyectiva y preserva $0$, $1$, suma, producto y orden. El orden entero satisface

   $$
   x\leq_{\mathbb Z}y
   \iff
   \exists n\in\mathbb N\;\bigl(y=x+\iota(n)\bigr),
   $$

   y, sobre representantes,

   $$
   [(a,b)]\leq_{\mathbb Z}[(c,d)]
   \iff
   a+d\leq c+b.
   $$

   §2.11 explicita el patrón metodológico que sostiene toda la construcción:

   $$
   \boxed{
   \text{representantes}
   \to
   \text{equivalencia}
   \to
   \text{cociente}
   \to
   \text{buena definición}
   \to
   \text{estructura}.
   }
   $$

   §2.12 consigna las referencias metodológicas del capítulo, aclara que las demostraciones son propias y deja explícito que no se utilizó el axioma de elección. §2.13 identifica la obstrucción multiplicativa que permanece en $\mathbb Z$ y prepara la construcción de $\mathbb Q$ mediante pares de enteros con segundo componente no nulo y un nuevo cociente.

4. [**Capítulo 3 — Los números racionales**](../capitulos/tratado-de-analisis-capitulo-3-los-numeros-racionales.md) (`MA-BCH-0020`) — publicado hasta **§3.6 — Inversos multiplicativos**. Después de construir el cociente racional, la estructura aditiva, el producto y la incrustación canónica

   $$
   \jmath_{\mathbb Z}^{\mathbb Q}:\mathbb Z\hookrightarrow\mathbb Q,
   $$

   §3.6 caracteriza el cero racional mediante

   $$
   \frac ab=0_{\mathbb Q}\iff a=0_{\mathbb Z},
   $$

   define $\mathbb Q_{\neq0}$ y construye el recíproco

   $$
   \left(\frac ab\right)^{-1}=\frac ba
   $$

   sin elegir representantes. Se introduce la división por $x/y:=xy^{-1}$ y se demuestra finalmente

   $$
   \boxed{\mathbb Q\text{ es un cuerpo}.}
   $$

   Como consecuencia, $\mathbb Q$ carece de divisores de cero. El orden racional se construirá a continuación en §3.7.

5. [**Glosario matemático**](tratado-de-analisis-glosario.md) (`MA-BCH-0006`) — glosario vivo con enlaces bidireccionales al punto exacto donde cada noción se introduce; incorpora ya **cuerpo**, **división racional**, **racionales no nulos** y **recíproco racional**, además de la infraestructura algebraica previa.

El **Capítulo 2 — Los números enteros** está completo en la edición web y el **Capítulo 3 — Los números racionales** está publicado hasta §3.6. La siguiente incorporación será **§3.7 — Orden racional**.

Cada capítulo conservará la continuidad deductiva del tratado, mientras la infraestructura interna de dependencias, auditoría y verificación permanecerá al servicio de la obra sin invadir la superficie de lectura.

Esta edición es abierta y progresiva. El contenido textual original se publica bajo **GNU Free Documentation License 1.3 o posterior**.

---
title: "Magnitudes, unidades y análisis dimensional"
subtitle: "Física para matemáticos · Tomo I · Capítulo 2"
author: "A. Peña"
description: "Capítulo 2 del Tomo I de Física para matemáticos, con ejercicios y soluciones desarrolladas."
content-id: MA-BCH-0031
source-id: FISPM-T1-C02
editorial-id: FPM-I-02
content-type: book-chapter
collection: PM-FIS
book-id: MA-BOK-0005
status: published
date-modified: 2026-10-17
areas: [fisica-matematica, mecanica]
level: fundamental
prerequisites: ["MA-BCH-0009"]
related: [MA-BOK-0005]
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
include-in-header:
  - ../../assets/includes/ma-math-font-ready.html
  - ../../assets/books/fispm/fispm-lightbox-focus.html
format:
  html:
    css: ../../assets/books/fispm/fispm-reader.css
    lightbox: true
number-sections: false
---

[Capítulo 1](fisica-para-matematicos-capitulo-1-teorias-fisicas-fenomenos-modelos-y-leyes.md) · [Índice del Tomo I](../para-matematicos/fisica-para-matematicos.md#tomo-i-fundamentos-y-mecanica) · [Capítulo 3](fisica-para-matematicos-capitulo-3-medicion-incertidumbre-estimacion-y-ordenes-de-magnitud.md)

[]{#fispm-c02-magnitudes-unidades-y-anuxe1lisis-dimensional}

Este capítulo desarrolla el tránsito desde la representación de una magnitud física hasta el análisis dimensional como herramienta de auditoría, reducción y modelización. Su hilo conductor distingue sistemáticamente:

$$\boxed{ \text{fenómeno físico} \leftrightarrow \text{modelo matemático} \leftrightarrow \text{estructura matemática}. }$$

[]{#un-número-no-es-todavía-una-magnitud-física}

[]{#fispm-t1-c02-s01}

[]{#fpm-i-02-s01}

## 1. Un número no es todavía una magnitud física {#fispm-c02-un-nuxfamero-no-es-todavuxeda-una-magnitud-fuxedsica}

[]{#el-resultado-42}

### El resultado «42» {#fispm-c02-el-resultado-42}

El capítulo anterior terminó con una regla que acompañará todo el tratado: un cálculo físico no se cierra cuando aparece un número. Debemos todavía interpretarlo respecto del sistema, las premisas, el régimen y la observación. Ahora haremos esa regla más concreta.

Supongamos que resolvemos un problema y escribimos:

$$42.$$

¿Es una respuesta física?

No podemos saberlo.

Podría significar:

- $42\,\mathrm m$;

- $42\,\mathrm s$;

- $42\,\mathrm{kg}$;

- $42$ partículas;

- un índice sin dimensión;

- un número puramente matemático que todavía no ha recibido ninguna interpretación física.

Shankar formula esta dificultad de manera pedagógica al introducir el movimiento unidimensional: una posición necesita una unidad de longitud y un tiempo necesita una unidad de tiempo; un resultado numérico sin esa información no permite siquiera decidir qué se está afirmando.[^1]

La primera distinción del capítulo será, por tanto:

$$\boxed{ \text{número} \neq \text{valor de una magnitud} \neq \text{magnitud física}. }$$

Esta separación parece elemental. Sin embargo, una gran cantidad de errores posteriores ---conversiones mal hechas, ecuaciones dimensionalmente imposibles, argumentos de funciones con unidades incompatibles--- puede rastrearse hasta su pérdida.

[]{#magnitud-física}

### Magnitud física {#fispm-c02-magnitud-fuxedsica}

El vocabulario metrológico internacional llama **magnitud** a una propiedad de un fenómeno, cuerpo o sustancia cuya magnitud puede expresarse mediante un número y una referencia.[^2]

Para nuestro tratado necesitaremos una formulación ligeramente orientada al modelado.

**Definición 1 --- Magnitud física** Una **magnitud física** es una propiedad cuantificable de un fenómeno, sistema o proceso que el modelo trata como comparable y representable mediante valores de magnitud.

Ejemplos:

- longitud;

- duración;

- masa;

- temperatura termodinámica;

- velocidad;

- energía.

La definición no dice todavía **cómo** medir cada magnitud. Tampoco afirma que toda propiedad física sea una magnitud. El color nominal de una etiqueta, por ejemplo, puede ser una propiedad del sistema sin constituir por sí mismo una magnitud en el sentido metrológico adoptado aquí. En cambio, una longitud de onda asociada con cierta radiación sí es una magnitud.

Debemos separar entonces:

$$\text{propiedad física}$$

de:

$$\text{propiedad cuantificable según una estructura de comparación}.$$

Esta distinción prolonga el capítulo 1: antes de escribir una ecuación, el modelo ya ha seleccionado qué propiedades considera relevantes.

[]{#una-magnitud-no-es-uno-de-sus-valores-particulares}

### Una magnitud no es uno de sus valores particulares {#fispm-c02-una-magnitud-no-es-uno-de-sus-valores-particulares}

Consideremos la **longitud**.

«Longitud» designa una clase o tipo de magnitud. Pero la longitud de una barra concreta puede tener un valor particular: $2\,\mathrm m.$ Otra barra puede tener: $0.30\,\mathrm m.$ Y una tercera: $1.7\,\mathrm m.$

No debemos confundir:

$$\boxed{ \text{la magnitud longitud} }$$

con:

$$\boxed{ \text{el valor de longitud de un objeto particular}. }$$

**Definición 2 --- Valor de una magnitud** Un **valor de una magnitud** es una especificación cuantitativa de una magnitud particular, expresada mediante un número y una referencia adecuada; cuando la referencia es una unidad de medida, el valor se expresa como número por unidad.

Así, la expresión

$$L=2\,\mathrm m$$

contiene varios niveles:

- $L$: símbolo que representa la longitud particular que estamos considerando;

- $2\,\mathrm m$: valor de esa longitud;

- $2$: valor numérico respecto de la unidad elegida;

- $\mathrm m$: unidad.

El BIPM resume esta estructura mediante la idea de que el valor de una magnitud se expresa generalmente como producto de un número y una unidad.[^3]

[]{#la-unidad-es-una-referencia-no-un-adorno-tipográfico}

### La unidad es una referencia, no un adorno tipográfico {#fispm-c02-la-unidad-es-una-referencia-no-un-adorno-tipogruxe1fico}

¿Qué trabajo realiza el metro en

$$L=2\,\mathrm m?$$

No es una etiqueta decorativa colocada después del número.

Nos proporciona una referencia con la que comparamos el valor de longitud.

**Definición 3 --- Unidad de medida** Una **unidad de medida** para una magnitud de cierto tipo es una cantidad particular de ese mismo tipo adoptada por convención como referencia para expresar valores de magnitudes comparables.

Si $u$ representa una unidad apropiada para una magnitud $Q$, podemos escribir: $Q=q\,u,$

donde $q$ es un número. Por ejemplo: $L=2\,\mathrm m.$

Aquí: $u=1\,\mathrm m$

y: $q=2.$ La unidad nos permite convertir una comparación física en una representación numérica.

No debemos leer: $2\,\mathrm m$

como una yuxtaposición informal entre «el número 2» y «la palabra metro».

Dentro del cálculo de magnitudes, la unidad participa algebraicamente.

[]{#el-valor-numérico-depende-de-la-unidad}

### El valor numérico depende de la unidad {#fispm-c02-el-valor-numuxe9rico-depende-de-la-unidad}

El BIPM escribe conceptualmente:

$$\text{valor de magnitud} = \text{valor numérico} \times \text{unidad}.$$

Podemos hacerlo explícito.

**Definición 4 --- Valor numérico relativo a una unidad** Si un valor de magnitud $Q$ se expresa respecto de una unidad $u$ como

$$Q=q\,u,$$

llamaremos **valor numérico de $Q$ respecto de $u$** al número $q$. Lo denotaremos

$$\{Q\}_u:=q.$$

Equivalentemente: $\{Q\}_u=\frac{Q}{u}.$

Esta escritura es importante porque hace visible algo que la notación cotidiana suele ocultar:

$$\boxed{ \text{el valor numérico depende de la unidad elegida}. }$$

La magnitud representada puede permanecer exactamente igual.

[]{#la-misma-longitud-números-diferentes}

### La misma longitud, números diferentes {#fispm-c02-la-misma-longitud-nuxfameros-diferentes}

Consideremos una misma longitud física: $L=2\,\mathrm m.$

Como: $1\,\mathrm m=100\,\mathrm{cm},$

también podemos escribir: $L=200\,\mathrm{cm}.$ Y como: $1\,\mathrm m=1000\,\mathrm{mm},$

tenemos: $L=2000\,\mathrm{mm}.$

Por tanto:

$$\boxed{ 2\,\mathrm m = 200\,\mathrm{cm} = 2000\,\mathrm{mm}. }$$

Pero: $2\neq200\neq2000.$

Los números cambian. La longitud no.

  Unidad elegida   Valor numérico   Valor de la longitud
  ---------------- ---------------- ----------------------
  $\mathrm m$      $2$              $2\,\mathrm m$
  $\mathrm{cm}$    $200$            $200\,\mathrm{cm}$
  $\mathrm{mm}$    $2000$           $2000\,\mathrm{mm}$

**Principio 1 --- No confundir magnitud, valor, número y unidad** En una expresión física distinguiremos siempre la magnitud considerada, su valor particular, el valor numérico y la unidad o referencia usada para expresarlo.

**Principio 2 --- Cambiar la unidad cambia el número, no la magnitud representada** Cuando dos unidades representan el mismo tipo de magnitud y están relacionadas por un cambio de escala, la misma magnitud física recibe valores numéricos diferentes de manera compensatoria.

[]{#por-qué-aparece-la-compensación-inversa}

### Por qué aparece la compensación inversa {#fispm-c02-por-quuxe9-aparece-la-compensaciuxf3n-inversa}

Supongamos que tenemos una unidad $u$ y otra unidad $u'$ del mismo tipo.

Sea: $u'=\lambda u, \qquad \lambda>0.$ Si $u'$ es una unidad **más grande** que $u$, entonces: $\lambda>1.$ Por ejemplo: $1\,\mathrm{km}=1000\,\mathrm m.$ La misma longitud necesitará menos unidades grandes para expresarse. Si: $L=3000\,\mathrm m,$

entonces: $L=3\,\mathrm{km}.$ El número disminuye exactamente en el factor en que aumentó el tamaño de la unidad. Esto no es una regla memorizada de conversión. Es una consecuencia algebraica de que estamos representando la **misma magnitud**.

[]{#primera-proposición-formal}

### Primera proposición formal {#fispm-c02-primera-proposiciuxf3n-formal}

**Proposición 1 --- Covariancia del valor numérico bajo un cambio multiplicativo de unidad**

Sea $Q$ un valor de magnitud. Supongamos que

$$Q=q\,u=q'\,u'$$

y que las unidades del mismo tipo satisfacen

$$u'=\lambda u, \qquad \lambda>0.$$

Entonces:

$$\boxed{ q'=\frac{q}{\lambda}. }$$

[]{#demostración}

#### Demostración {#fispm-c02-demostraciuxf3n}

Partimos de: $Q=q\,u.$

También: $Q=q'\,u'.$ Por tanto: $q\,u=q'\,u'.$

Usando: $u'=\lambda u,$

obtenemos: $q\,u=q'\lambda u.$

Como $u$ es una unidad no nula, podemos dividir ambos miembros por $u$: $q=\lambda q'.$

Finalmente: $q'=\frac{q}{\lambda}.$

Por tanto:

$$\boxed{ q'=\frac{q}{\lambda}. }$$

$$\boxed{\text{QED}}$$

[]{#interpretación-de-la-proposición-1}

### Interpretación de la Proposición 1 {#fispm-c02-interpretaciuxf3n-de-la-proposiciuxf3n-1}

Si agrandamos la unidad por un factor $\lambda$, el valor numérico disminuye por el mismo factor: $u\longrightarrow\lambda u$

implica: $q\longrightarrow\frac{q}{\lambda}.$

El producto permanece invariante:

$$q\,u = \left(\frac{q}{\lambda}\right)(\lambda u).$$

Ésta es una primera forma de covariancia de representación:

$$\boxed{ \text{cambia la representación numérica} \quad \text{mientras permanece la magnitud física}. }$$

Más adelante veremos una idea análoga cuando cambiemos sistemas de coordenadas.

[]{#ejemplo-desarrollado-1-metros-y-kilómetros}

### Ejemplo desarrollado 1 --- Metros y kilómetros {#fispm-c02-ejemplo-desarrollado-1-metros-y-kiluxf3metros}

Sea: $L=7500\,\mathrm m.$

Como: $1\,\mathrm{km} = 1000\,\mathrm m,$

tenemos $\lambda=1000$. Por la Proposición 1: $q' = \frac{7500}{1000} = 7.5.$

Luego:

$$\boxed{ 7500\,\mathrm m = 7.5\,\mathrm{km}. }$$

La conversión no consistió en mover mecánicamente una coma.

Consistió en mantener fija la magnitud mientras cambiábamos la referencia utilizada para expresarla.

[]{#ejemplo-desarrollado-2-segundos-y-milisegundos}

### Ejemplo desarrollado 2 --- Segundos y milisegundos {#fispm-c02-ejemplo-desarrollado-2-segundos-y-milisegundos}

Consideremos: $T=0.032\,\mathrm s.$

Como: $1\,\mathrm{ms} = 10^{-3}\,\mathrm s,$

tenemos: $\lambda=10^{-3}.$ Por la Proposición 1: $q' = \frac{0.032}{10^{-3}} = 32.$

Por tanto:

$$\boxed{ 0.032\,\mathrm s = 32\,\mathrm{ms}. }$$

La unidad disminuyó por un factor $1000$ y el valor numérico aumentó por un factor $1000$.

[]{#no-todas-las-conversiones-son-de-escala-pura}

### No todas las conversiones son de escala pura {#fispm-c02-no-todas-las-conversiones-son-de-escala-pura}

La Proposición 1 tiene una hipótesis explícita: $u'=\lambda u.$

No debemos extenderla fuera de ese caso. Hay escalas de uso físico en las que la relación entre los números incluye además un desplazamiento de origen. La temperatura Celsius y la temperatura termodinámica en kelvin ofrecen un ejemplo importante.

Por eso no diremos:

> «Toda conversión de unidades es una regla de tres».

La formulación correcta es:

> la Proposición 1 describe los cambios **multiplicativos de unidad**.

El tratamiento preciso de kelvin, grado Celsius y SI aparecerá en §3.

[]{#el-símbolo-de-la-magnitud-no-debería-depender-de-la-unidad}

### El símbolo de la magnitud no debería depender de la unidad {#fispm-c02-el-suxedmbolo-de-la-magnitud-no-deberuxeda-depender-de-la-unidad}

Si: $L=2\,\mathrm m$

y: $L=200\,\mathrm{cm},$

el símbolo $L$ no cambia.

Eso expresa:

$$\boxed{ \text{la magnitud representada es independiente de cómo elijamos expresarla}. }$$

Podemos tener: $\{L\}_{\mathrm m}=2$

y: $\{L\}_{\mathrm{cm}}=200,$

pero ambos corresponden al mismo $L$. Una ley física no debería depender accidentalmente de que el investigador prefiera metros o centímetros.

[]{#del-número-a-la-observación}

### Del número a la observación {#fispm-c02-del-nuxfamero-a-la-observaciuxf3n}

En el capítulo 1 introdujimos relaciones `[``OBS``]`.

Ahora podemos refinar esa cadena:

$$\boxed{\begin{gathered} \text{sistema físico} \longrightarrow \text{magnitud seleccionada}\\[2pt]\Downarrow\\[2pt]\text{procedimiento de comparación}\\[2pt]\Downarrow\\[2pt]\text{valor respecto de una referencia}\\[2pt]\Downarrow\\[2pt]\text{representación numérica}. \end{gathered}}$$

Por ejemplo:

$$[\mathrm{OBS}] \qquad L \longleftrightarrow \text{procedimiento de medición de longitud}.$$

Después escogemos una unidad $u=\mathrm m$ y obtenemos: $L=\{L\}_{\mathrm m}\,\mathrm m.$ En el capítulo 3 estudiaremos la incertidumbre del procedimiento de medida. Aquí construimos solamente la gramática que permitirá hablar de ella sin confundirla con la unidad.

[]{#un-número-puro-también-puede-tener-significado-físico}

### Un número puro también puede tener significado físico {#fispm-c02-un-nuxfamero-puro-tambiuxe9n-puede-tener-significado-fuxedsico}

Debemos evitar el error contrario.

No toda cantidad físicamente significativa necesita llevar un símbolo de unidad distinto de $1$.

Existen magnitudes de **dimensión uno**:

- cocientes entre magnitudes del mismo tipo;

- ciertas fracciones;

- conteos;

- ángulos expresados en radianes, bajo la convención del SI.

Su tratamiento requiere cuidado y se desarrollará en §8.

Por ahora conservamos:

$$\boxed{ \text{un número aislado no determina por sí mismo su interpretación física}. }$$

No afirmamos:

$$\boxed{ \text{todo número físicamente significativo debe llevar siempre una unidad con nombre}. }$$

La segunda afirmación sería falsa.

[]{#ficha-de-lectura-cuantitativa}

### Ficha de lectura cuantitativa {#fispm-c02-ficha-de-lectura-cuantitativa}

**Ficha de lectura de un valor** 1. **Magnitud:** ¿qué propiedad física representa el símbolo? 2. **Valor:** ¿qué valor particular se atribuye? 3. **Unidad:** ¿qué referencia se utiliza? 4. **Número:** ¿cuál es el valor numérico respecto de esa unidad? 5. **Cambio de unidad:** ¿la transformación es multiplicativa? 6. **Observación:** ¿qué procedimiento conecta la magnitud con el dato? 7. **Interpretación:** ¿el número conserva sentido físico si borramos la referencia?

[]{#ejercicios-de-1}

### Ejercicios de §1 {#fispm-c02-ejercicios-de-1}

**Ejercicio 1 --- Número, valor o magnitud**

**Tipo:** conceptual · **Nivel:** básico

Considera:

1.  $3$;

2.  $3\,\mathrm m$;

3.  $L=3\,\mathrm m$;

4.  «la longitud de la barra»;

5.  $\{L\}_{\mathrm m}=3$.

Explica qué representa cada expresión y cuáles no bastan, por sí solas, para identificar un valor físico completo.

**Solución.**

1.  $3$ es un número. Sin contexto no determina una magnitud.

2.  $3\,\mathrm m$ es un valor de longitud, pero no identifica qué objeto posee esa longitud.

3.  $L=3\,\mathrm m$ asigna ese valor a la magnitud particular $L$.

4.  «La longitud de la barra» identifica una magnitud particular, pero no su valor.

5.  $\{L\}_{\mathrm m}=3$ dice que el valor numérico de $L$ respecto del metro es $3$; equivale a $L=3\,\mathrm m$.

La conclusión es:

$$\boxed{ \text{magnitud},\quad \text{valor},\quad \text{número},\quad \text{unidad} }$$

son conceptos relacionados pero no intercambiables.

------------------------------------------------------------------------

**Ejercicio 2 --- La misma longitud en tres unidades**

**Tipo:** cálculo · **Nivel:** básico

Una barra tiene: $L=2.35\,\mathrm m.$

1.  Exprésala en centímetros.

2.  Exprésala en milímetros.

3.  Calcula $\{L\}_{\mathrm m}$, $\{L\}_{\mathrm{cm}}$ y $\{L\}_{\mathrm{mm}}$.

4.  Explica qué cambia y qué permanece invariante.

**Solución.**

Como $1\,\mathrm m=100\,\mathrm{cm}$: $2.35\,\mathrm m = 235\,\mathrm{cm}.$

Como $1\,\mathrm m=1000\,\mathrm{mm}$: $2.35\,\mathrm m = 2350\,\mathrm{mm}.$

Así:

$$\boxed{ L = 2.35\,\mathrm m = 235\,\mathrm{cm} = 2350\,\mathrm{mm}. }$$

Y:

$$\{L\}_{\mathrm m}=2.35,$$

$$\{L\}_{\mathrm{cm}}=235,$$

$$\{L\}_{\mathrm{mm}}=2350.$$

Cambian la unidad y el valor numérico. Permanece invariante la longitud física $L$.

------------------------------------------------------------------------

**Ejercicio 3 --- Cambio de unidad y cambio de número**

**Tipo:** demostración · **Nivel:** central

Una distancia se expresa como $D=q\,u.$

Introducimos

$$u'=5u.$$

1.  Demuestra que:

$$\{D\}_{u'} = \frac{1}{5}\{D\}_u.$$

1.  Si $\{D\}_u=60$, calcula $\{D\}_{u'}$.

2.  Explica por qué sería incorrecto afirmar que la distancia se volvió cinco veces menor.

**Solución.**

Tenemos: $D=q\,u=q'\,u'.$

Como $u'=5u$: $q\,u=q'(5u).$

Dividiendo por $u$: $q=5q'.$

Luego:

$$\boxed{ q'=\frac{q}{5}. }$$

Por tanto:

$$\boxed{ \{D\}_{u'} = \frac{1}{5}\{D\}_u. }$$

Si $\{D\}_u=60$: $\{D\}_{u'}=\frac{60}{5}=12.$

Así:

$$\boxed{ 60u=12u'. }$$

La distancia no cambió. La unidad nueva es cinco veces mayor y por eso hacen falta cinco veces menos unidades para representar la misma distancia.

[]{#cierre}

### Cierre {#fispm-c02-cierre}

Hemos construido la primera capa cuantitativa del tratado:

$$\boxed{ Q = \{Q\}_u\,u. }$$

Esta escritura separa:

- la magnitud representada;

- el valor particular;

- la unidad;

- el valor numérico.

Y la Proposición 1 mostró que, bajo: $u'=\lambda u,$

el número transforma como: $\{Q\}_{u'} = \frac{\{Q\}_u}{\lambda}.$

Por tanto:

$$\boxed{ \text{la física no está contenida en el número aislado}. }$$

La sección siguiente profundizará en una pregunta que aquí hemos tratado de manera operativa:

> **¿qué significa que dos magnitudes sean del mismo tipo y puedan compararse mediante una misma unidad?**

Entramos así en el §[2](#fispm-c02-magnitudes-clases-de-magnitudes-y-referencias).

[]{#magnitudes-clases-de-magnitudes-y-referencias}

[]{#fispm-t1-c02-s02}

[]{#fpm-i-02-s02}

## 2. Magnitudes, clases de magnitudes y referencias {#fispm-c02-magnitudes-clases-de-magnitudes-y-referencias}

[]{#antes-de-comparar-números-debemos-saber-qué-estamos-comparando}

### Antes de comparar números, debemos saber qué estamos comparando {#fispm-c02-antes-de-comparar-nuxfameros-debemos-saber-quuxe9-estamos-comparando}

En §1 distinguimos cuatro niveles:

$$\text{magnitud} \neq \text{valor de magnitud} \neq \text{valor numérico} \neq \text{unidad}.$$

Ahora aparece una pregunta anterior incluso a la elección de unidad:

> ¿Cuándo tiene sentido decir que dos magnitudes pueden compararse entre sí?

Consideremos las expresiones: $5\,\mathrm m$

y

$$8\,\mathrm m.$$

Podemos preguntar cuál longitud es mayor, calcular su diferencia o formar, cuando el contexto lo permite, el cociente entre ambas. Pero comparemos ahora: $5\,\mathrm m$

[]{#fig:I-02-R01}

<figure id="fig-fpm-v04-i-02-r01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R01.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R01.svg" alt="Magnitud y representación numérica. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="168" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.1.** Cambiar de metros a centímetros multiplica por cien el valor numérico y divide por cien la unidad empleada. El segmento físico representado permanece igual: $2\,\mathrm m=200\,\mathrm{cm}$. Véase §[2](#fispm-c02-magnitudes-clases-de-magnitudes-y-referencias).

</figcaption>

</figure>

[]{#fig:I-02-N01}

<figure id="fig-fpm-v04-i-02-n01" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-N01.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-N01.svg" alt="Magnitud y unidad. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="154" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.2.** La longitud permanece fija al cambiar la unidad. Cada centímetro contiene diez milímetros; el valor numérico se multiplica por diez. Véase §[2](#fispm-c02-magnitudes-clases-de-magnitudes-y-referencias).

</figcaption>

</figure>

y

$$8\,\mathrm s.$$

Los números $5$ y $8$ sí son comparables como números.

Las magnitudes físicas representadas no lo son de la misma manera.

No tiene sentido físico ordinario afirmar: $5\,\mathrm m<8\,\mathrm s.$ La dificultad no está en los números. Está en que representan **clases distintas de magnitudes**. Ésta es una de las primeras restricciones estructurales que la física impone al álgebra que usamos para describirla.

[]{#tipo-de-magnitud}

### Tipo de magnitud {#fispm-c02-tipo-de-magnitud}

El Vocabulario Internacional de Metrología introduce la noción de *kind of quantity* como el aspecto común a magnitudes mutuamente comparables.[^4]

Adoptaremos una formulación operativa compatible con esa idea.

**Definición 5 --- Tipo de magnitud** Un **tipo de magnitud** es la clase determinada por el aspecto cuantificable común que hace mutuamente comparables ciertas magnitudes físicas.

Ejemplos de magnitudes que normalmente consideramos del mismo tipo son:

- el diámetro de una esfera;

- la longitud de una cuerda;

- la longitud de onda de cierta radiación;

- la distancia entre dos puntos.

Todas pertenecen al tipo de magnitud:

$$\boxed{\text{longitud}.}$$

En cambio, una longitud y una masa no pertenecen al mismo tipo. La clasificación no depende de que los valores numéricos coincidan. Podemos tener: $L=5\,\mathrm m$

y

$$T=5\,\mathrm s.$$

Entonces: $\{L\}_{\mathrm m}=5$

y

$$\{T\}_{\mathrm s}=5,$$

pero la igualdad entre los números no convierte longitud y duración en la misma magnitud física.

Por tanto:

$$\boxed{ \text{mismo valor numérico} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

[]{#una-clase-física-precede-a-la-elección-de-unidad}

### Una clase física precede a la elección de unidad {#fispm-c02-una-clase-fuxedsica-precede-a-la-elecciuxf3n-de-unidad}

En §1 escribimos: $Q=q\,u.$

Esa escritura tiene una condición silenciosa que ahora debemos hacer explícita:

$$Q$$

y

$$u$$

deben pertenecer al mismo tipo de magnitud.

No podemos usar un segundo como unidad de una longitud ni un metro como unidad de una masa. La unidad no crea el tipo de magnitud. Lo presupone.

La secuencia conceptual correcta es:

$$\boxed{ \text{tipo de magnitud} \longrightarrow \text{elección de una referencia compatible} \longrightarrow \text{valor numérico}. }$$

No:

$$\boxed{ \text{número} \longrightarrow \text{adición posterior de una etiqueta de unidad}. }$$

Este orden será esencial cuando estudiemos dimensiones.

[]{#la-unidad-como-cantidad-de-referencia-del-mismo-tipo}

### La unidad como cantidad de referencia del mismo tipo {#fispm-c02-la-unidad-como-cantidad-de-referencia-del-mismo-tipo}

El VIM define una unidad de medida como una cantidad escalar real, adoptada por convención, con la cual puede compararse cualquier otra cantidad del mismo tipo para expresar la razón entre ambas como un número.[^5]

Ésta es la estructura que ya utilizábamos implícitamente en §1. Si $u$ es una unidad del mismo tipo que $Q$, escribimos: $Q=q\,u.$ Entonces: $q=\frac{Q}{u}.$ La división tiene aquí una interpretación física precisa: estamos preguntando cuántas veces la referencia $u$ entra, en sentido de razón, en la magnitud $Q$.

Por ejemplo: $L=2.5\,\mathrm m$

puede leerse como: $\frac{L}{1\,\mathrm m}=2.5.$ El metro no es un comentario sobre el número $2.5$. Es la referencia que permite producir ese número a partir de una magnitud de longitud.

[]{#comparabilidad-no-significa-identidad-física}

### Comparabilidad no significa identidad física {#fispm-c02-comparabilidad-no-significa-identidad-fuxedsica}

Que dos magnitudes sean del mismo tipo no significa que sean la misma magnitud particular. La longitud de una mesa y la longitud de una habitación pueden compararse porque ambas son longitudes. Pero son propiedades de sistemas diferentes.

Podemos escribir: $L_{\mathrm{mesa}}=1.8\,\mathrm m$

y

$$L_{\text{habitación}}=4.5\,\mathrm m.$$

Entonces tiene sentido formar:

$$\frac{L_{\text{habitación}}}{L_{\mathrm{mesa}}} = \frac{4.5\,\mathrm m}{1.8\,\mathrm m} = 2.5.$$

La razón es numérica porque se canceló una referencia común de longitud. Pero esto no elimina la diferencia entre los objetos físicos representados.

Debemos distinguir:

$$\boxed{ \text{mismo tipo} \neq \text{misma magnitud particular} \neq \text{mismo valor}. }$$

[]{#el-tipo-de-magnitud-tampoco-está-determinado-por-el-símbolo-algebraico}

### El tipo de magnitud tampoco está determinado por el símbolo algebraico {#fispm-c02-el-tipo-de-magnitud-tampoco-estuxe1-determinado-por-el-suxedmbolo-algebraico}

Supongamos que en dos problemas distintos aparece la letra:

$$x.$$

En un problema $x$ puede representar una posición. En otro, una fracción sin unidad. En un tercero, un tiempo reescalado. La letra no determina la clase física del objeto.

El significado procede del modelo y del diccionario de interpretación introducido en el capítulo 1.

Por tanto:

$$\boxed{ \text{misma letra} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

Esto es una razón adicional para no manipular fórmulas físicas como si fueran expresiones algebraicas descontextualizadas.

[]{#basta-la-expresión-de-unidad-para-identificar-el-tipo}

### ¿Basta la expresión de unidad para identificar el tipo? {#fispm-c02-basta-la-expresiuxf3n-de-unidad-para-identificar-el-tipo}

Tampoco.

Éste es un punto más sutil. El VIM advierte que dos tipos de magnitud diferentes pueden compartir la misma expresión de unidad.[^6]

Por ejemplo, tanto la **capacidad calorífica** como la **entropía** pueden expresarse mediante: $\mathrm{J/K}.$ Sin embargo, no se consideran generalmente magnitudes del mismo tipo. Otro ejemplo especialmente instructivo utiliza: $\mathrm{s}^{-1}.$ Una frecuencia puede expresarse con esa estructura de unidad y una actividad radiactiva también.

El SI utiliza nombres especiales distintos: $1\,\mathrm{Hz}=1\,\mathrm{s}^{-1}$

para frecuencia, y: $1\,\mathrm{Bq}=1\,\mathrm{s}^{-1}$

para actividad de radionúclidos. La igualdad de las expresiones algebraicas de unidad no significa identidad del concepto físico.

Por tanto:

$$\boxed{ \text{misma expresión de unidad} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

Todavía no hemos definido formalmente la dimensión física.

En §5 veremos una versión más profunda de esta advertencia:

> tener la misma dimensión tampoco basta para ser la misma clase de magnitud.

[]{#la-física-de-una-cantidad-no-cabe-entera-en-sus-unidades}

### La física de una cantidad no cabe entera en sus unidades {#fispm-c02-la-fuxedsica-de-una-cantidad-no-cabe-entera-en-sus-unidades}

La observación anterior tiene una consecuencia metodológica importante.

Consideremos una expresión como: $3\,\mathrm{s}^{-1}.$

Sin información adicional, no sabemos todavía si representa:

- una frecuencia;

- una actividad radiactiva;

- alguna otra tasa inversa de tiempo.

La unidad restringe el significado posible.

No lo determina completamente.

Necesitamos además:

- qué sistema estudiamos;

- qué observable se representa;

- cómo se define esa magnitud en el modelo;

- qué procedimiento `[``OBS``]` la conecta con datos.

Así reaparece la tesis del capítulo 1:

$$\boxed{ \text{formalismo} + \text{interpretación física} }$$

son inseparables.

[]{#comparar-ordenar-restar-y-formar-razones}

### Comparar, ordenar, restar y formar razones {#fispm-c02-comparar-ordenar-restar-y-formar-razones}

Cuando dos valores pertenecen al mismo tipo de magnitud, ciertas operaciones adquieren sentido natural. Si: $L_1=2\,\mathrm m$

y: $L_2=5\,\mathrm m,$

podemos comparar: $L_1<L_2,$

restar: $L_2-L_1=3\,\mathrm m,$

y formar la razón: $\frac{L_2}{L_1}=\frac52.$ En cambio, la expresión: $L_2-T$

con $T$ una duración no representa, sin una construcción física adicional, una magnitud ordinaria definida por resta. La regla no debe formularse de manera excesivamente fuerte. La física sí construye nuevas magnitudes combinando clases diferentes mediante productos y cocientes. Por ejemplo, más adelante aparecerán magnitudes cuya unidad contiene longitud dividida por tiempo.

Lo que no podemos hacer es **sumar o comparar por orden magnitudes de tipos incompatibles como si fueran homogéneas**. La combinación multiplicativa será objeto de §4.

[]{#comparabilidad-y-ecuaciones-físicas}

### Comparabilidad y ecuaciones físicas {#fispm-c02-comparabilidad-y-ecuaciones-fuxedsicas}

Supongamos que alguien propone: $L_1=L_2+T.$

Antes de preguntar si la ecuación describe algún fenómeno real, ya tenemos un problema semántico:

- $L_1$ es una longitud;

- $L_2$ es una longitud;

- $T$ es una duración.

La suma: $L_2+T$

no está definida como suma de magnitudes del mismo tipo.

No necesitamos conocer todavía análisis dimensional para detectar el problema. La incompatibilidad aparece ya en el nivel de los tipos de magnitud. En §6 convertiremos esta intuición en una prueba sistemática mediante homogeneidad dimensional.

[]{#primera-regla-metodológica-de-2}

### Primera regla metodológica de §2 {#fispm-c02-primera-regla-metodoluxf3gica-de-2}

**Principio 3 --- La comparabilidad física precede a la comparación numérica** Antes de comparar, sumar o interpretar conjuntamente valores numéricos, debe establecerse qué magnitudes representan y si las operaciones propuestas son compatibles con sus tipos de magnitud.

Esto evita errores como: $3\,\mathrm m+4\,\mathrm s=7.$ El problema no consiste en que $3+4\neq7$. De hecho: $3+4=7.$ El problema es que la operación física propuesta no está bien tipada.

[]{#la-palabra-referencia-es-más-amplia-que-unidad}

### La palabra «referencia» es más amplia que «unidad» {#fispm-c02-la-palabra-referencia-es-muxe1s-amplia-que-unidad}

Hasta ahora hemos trabajado casi exclusivamente con valores del tipo: $Q=q\,u.$ Pero el VIM define un valor de magnitud de manera más general como la combinación de un número y una referencia.[^7]

En muchos casos, esa referencia es una unidad de medida.

Sin embargo, el VIM contempla también valores cuya referencia se da mediante:

- un procedimiento de medida especificado;

- un material de referencia.

Por ejemplo, determinadas escalas de dureza dependen de un procedimiento convencional, y algunas magnitudes de laboratorio pueden expresarse respecto de materiales de referencia internacionalmente establecidos. No desarrollaremos aquí esas ramas de la metrología. Pero debemos conservar la distinción conceptual.

**Definición 6 --- Referencia de un valor de magnitud** Una **referencia de un valor de magnitud** es el elemento convencional respecto del cual el número asociado adquiere significado cuantitativo. En las magnitudes tratadas ordinariamente en este capítulo, la referencia será normalmente una unidad de medida; en contextos metrológicos más generales puede ser también un procedimiento o un material de referencia.

Por tanto:

$$\boxed{ \text{unidad} \subset \text{clase más amplia de referencias usadas para expresar valores}. }$$

La expresión anterior es conceptual: no afirma una inclusión conjuntista formal entre objetos metrológicos.

[]{#por-qué-en-física-elemental-podemos-concentrarnos-en-unidades}

### Por qué en física elemental podemos concentrarnos en unidades {#fispm-c02-por-quuxe9-en-fuxedsica-elemental-podemos-concentrarnos-en-unidades}

La mayor parte de las magnitudes de este tratado ---longitud, masa, tiempo, velocidad, aceleración, energía, carga, temperatura termodinámica--- se manipularán mediante unidades. Por eso nuestra notación principal seguirá siendo: $Q=\{Q\}_u\,u.$

La ampliación de §2.12 cumple otra función:

> impedir que confundamos una convención pedagógica útil con la definición más general de valor de magnitud.

En otras palabras:

$$\boxed{ \text{nuestro cálculo con unidades es central} \quad \text{pero no agota toda la metrología}. }$$

La teoría sistemática de medición, incertidumbre y trazabilidad pertenece al capítulo 3 y a tratamientos metrológicos especializados.

[]{#una-unidad-no-es-cualquier-cantidad-elegida-informalmente}

### Una unidad no es cualquier cantidad elegida informalmente {#fispm-c02-una-unidad-no-es-cualquier-cantidad-elegida-informalmente}

Podemos comparar una mesa con otra mesa y obtener una razón de longitudes. Pero eso no convierte automáticamente la longitud de la segunda mesa en una **unidad de medida** institucionalizada. Para que una referencia funcione como unidad necesitamos una adopción convencional suficientemente clara y una forma de identificar o realizar esa referencia.

En un ejercicio escolar podemos decir:

> «Tomemos esta barra como una unidad provisional de longitud».

Eso construye un modelo sencillo de comparación. Pero el SI contemporáneo requiere una estructura metrológica mucho más precisa, que estudiaremos en §3.

La diferencia es:

[]{#el-símbolo-de-cantidad-debe-permanecer-físicamente-estable}

### El símbolo de cantidad debe permanecer físicamente estable {#fispm-c02-el-suxedmbolo-de-cantidad-debe-permanecer-fuxedsicamente-estable}

Volvamos a una longitud particular $L$.

Podemos escribir: $L=2\,\mathrm m$

o: $L=200\,\mathrm{cm}.$

La elección de unidad cambia:

$$\{L\}_{\mathrm m}=2,$$

$$\{L\}_{\mathrm{cm}}=200.$$

Pero la cantidad representada sigue siendo $L$.

Conviene por tanto que nuestra notación separe:

$$L$$

de: $\{L\}_u.$ El primero representa la magnitud física particular. El segundo representa el número que obtenemos al expresarla respecto de una unidad concreta.

Esto nos permitirá más adelante distinguir entre:

- **ecuaciones entre magnitudes**;

- **ecuaciones entre valores numéricos**.

La primera clase tiene un grado de independencia respecto de la elección de unidad que la segunda puede no tener.

[]{#mismo-fenómeno-magnitudes-diferentes}

### Mismo fenómeno, magnitudes diferentes {#fispm-c02-mismo-fenuxf3meno-magnitudes-diferentes}

Un solo sistema físico puede portar muchas magnitudes diferentes.

Consideremos una barra.

Podemos asociarle:

- una longitud;

- una masa;

- una temperatura;

- una velocidad, si se mueve;

- una energía, según el modelo considerado.

No debemos pensar que «la barra tiene un número».

Tiene múltiples propiedades cuantificables, cada una perteneciente a un tipo diferente y cada una necesitada de una referencia apropiada.

La estructura correcta es:

$$\boxed{ \text{sistema físico} \longrightarrow \text{familia de magnitudes seleccionadas por el modelo}. }$$

Esto vuelve a conectar el capítulo con el concepto de observable del capítulo 1.

[]{#misma-magnitud-general-instancias-diferentes}

### Misma magnitud general, instancias diferentes {#fispm-c02-misma-magnitud-general-instancias-diferentes}

La palabra «longitud» puede aparecer en dos niveles.

Por un lado, hablamos del tipo general:

$$\text{longitud}.$$

Por otro, hablamos de una longitud concreta: $L_{\mathrm{barra}}.$ La primera organiza una clase de magnitudes comparables. La segunda es una instancia física particular. Para evitar una carga terminológica excesiva no construiremos una teoría formal de universales e instancias.

Pero mantendremos la distinción operativa:

$$\boxed{ \text{tipo de magnitud} \neq \text{magnitud particular de un sistema}. }$$

[]{#una-advertencia-sobre-temperaturas-y-escalas}

### Una advertencia sobre temperaturas y escalas {#fispm-c02-una-advertencia-sobre-temperaturas-y-escalas}

El lenguaje de comparación por razón funciona limpiamente para magnitudes como longitud y masa.

No todas las escalas cuantitativas se comportan de la misma manera. En particular, la temperatura Celsius introduce un desplazamiento convencional de origen respecto de la temperatura termodinámica expresada en kelvin.

Por eso debemos evitar inferencias del tipo:

> «$20\,^{\circ}\mathrm C$ es el doble de $10\,^{\circ}\mathrm C$».

Esa afirmación no expresa una razón de temperaturas termodinámicas. El caso será tratado cuidadosamente en §3.

Aquí cumple una función conceptual:

$$\boxed{\begin{gathered} \text{\parbox{.82\linewidth}{\centering que algo se exprese con un número y una referencia}}\\[2pt] \not\Rightarrow\\[2pt] \text{\parbox{.82\linewidth}{\centering que todas las operaciones numéricas tengan interpretación física directa}}. \end{gathered}}$$

[]{#segunda-regla-metodológica-de-2}

### Segunda regla metodológica de §2 {#fispm-c02-segunda-regla-metodoluxf3gica-de-2}

**Principio 4 --- La notación de unidad no determina por sí sola el significado físico** Una expresión de unidad restringe las magnitudes que puede representar, pero la identificación del tipo de magnitud exige además el contexto físico, la definición de la cantidad y su regla de interpretación.

Así, ante: $2\,\mathrm{s}^{-1},$

no preguntaremos únicamente:

> «¿qué unidad tiene?»

También preguntaremos:

> «¿qué magnitud física representa?»

[]{#ficha-de-lectura-identificar-correctamente-una-cantidad-física}

### Ficha de lectura: identificar correctamente una cantidad física {#fispm-c02-ficha-de-lectura-identificar-correctamente-una-cantidad-fuxedsica}

A partir de ahora, cuando encontremos una cantidad en una fórmula, podemos aplicar esta ficha mínima.

1.  **Sistema:** ¿de qué sistema o fenómeno es propiedad?

2.  **Magnitud particular:** ¿qué cantidad concreta representa el símbolo?

3.  **Tipo:** ¿a qué clase de magnitud pertenece?

4.  **Referencia:** ¿respecto de qué se expresa su valor?

5.  **Unidad:** si corresponde, ¿qué unidad se ha elegido?

6.  **Valor numérico:** ¿qué número resulta respecto de esa unidad?

7.  **Interpretación:** ¿cómo se conecta con el modelo y con `[``OBS``]`?

Esta secuencia impide reducir prematuramente la física a números.

[]{#ejercicios-de-2}

### Ejercicios de §2 {#fispm-c02-ejercicios-de-2}

**Ejercicio 4 --- Misma unidad, magnitudes diferentes**

**Tipo:** conceptual · **Nivel:** central

Considera los siguientes casos conceptuales:

1.  una frecuencia expresada en $\mathrm{s}^{-1}$;

2.  una actividad radiactiva expresada en $\mathrm{s}^{-1}$;

3.  la longitud de onda de una señal expresada en metros;

4.  el diámetro de una esfera expresado en metros;

5.  una duración expresada en segundos.

Responde:

1.  ¿Qué pares pertenecen claramente al mismo tipo de magnitud?

2.  ¿Qué ejemplo muestra que una misma expresión de unidad no basta para identificar el tipo de magnitud?

3.  ¿Por qué tener el mismo valor numérico tampoco basta?

4.  Explica por qué $2\,\mathrm{Hz}$ y $2\,\mathrm{Bq}$ no deben interpretarse como la misma magnitud física aunque ambas unidades sean algebraicamente equivalentes a $\mathrm{s}^{-1}$.

**Solución del ejercicio 4.**

[]{#a.-magnitudes-del-mismo-tipo}

#### a. Magnitudes del mismo tipo {#fispm-c02-a.-magnitudes-del-mismo-tipo}

La longitud de onda y el diámetro son ambas longitudes.

Por tanto pertenecen al mismo tipo de magnitud:

$$\boxed{\text{longitud}.}$$

Pueden compararse mediante una misma familia de unidades de longitud. La frecuencia y la actividad radiactiva no se consideran, en general, magnitudes del mismo tipo. La duración pertenece al tipo tiempo o duración y tampoco coincide con los anteriores.

[]{#b.-misma-expresión-de-unidad}

#### b. Misma expresión de unidad {#fispm-c02-b.-misma-expresiuxf3n-de-unidad}

Frecuencia y actividad ofrecen el ejemplo buscado:

$$[\text{frecuencia}]\sim\mathrm{s}^{-1},$$

$$[\text{actividad}]\sim\mathrm{s}^{-1}.$$

Sin embargo, representan conceptos físicos distintos. Por eso el SI usa nombres especiales diferentes: $\mathrm{Hz}$

y: $\mathrm{Bq}.$

La lección es:

$$\boxed{ \text{misma expresión algebraica de unidad} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

[]{#c.-mismo-valor-numérico}

#### c. Mismo valor numérico {#fispm-c02-c.-mismo-valor-numuxe9rico}

Supongamos: $L=2\,\mathrm m$

y: $T=2\,\mathrm s.$

Entonces ambos valores numéricos son $2$, pero una cantidad es longitud y la otra duración.

Por tanto:

$$\boxed{ \{L\}_{\mathrm m}=\{T\}_{\mathrm s} \not\Rightarrow L\text{ y }T\text{ son del mismo tipo}. }$$

[]{#d.-hertz-frente-a-becquerel}

#### d. Hertz frente a becquerel {#fispm-c02-d.-hertz-frente-a-becquerel}

Tenemos las igualdades de unidades:

$$1\,\mathrm{Hz}=1\,\mathrm{s}^{-1},$$

$$1\,\mathrm{Bq}=1\,\mathrm{s}^{-1}.$$

Pero los nombres especiales señalan usos físicos diferentes:

- hertz para frecuencia;

- becquerel para actividad de radionúclidos.

Así, aunque:

$$2=2$$

y las expresiones algebraicas de unidad coincidan, la interpretación física no coincide. La cantidad no queda identificada solo por el par «número + forma algebraica de unidad» si hemos perdido el tipo físico que el modelo asigna.

**Ejercicio 5 --- Diseñar una referencia de medida**

**Tipo:** modelización · **Nivel:** central

Una comunidad aislada desea comparar longitudes antes de adoptar un sistema internacional. Decide conservar una barra y declarar su longitud como una unidad provisional $u$.

1.  Explica qué debe significar la afirmación

$$L=3.7\,u.$$

1.  ¿Por qué $u$ debe representar una longitud y no una masa o una duración?

2.  Si otra barra $u'$ tiene una longitud igual a la mitad de $u$, ¿qué valor numérico tendrá la misma longitud $L$ respecto de $u'$?

3.  Identifica qué partes del procedimiento son convencionales y qué parte expresa una comparación física.

4.  Explica por qué este modelo local no equivale todavía a construir el SI contemporáneo.

**Solución del ejercicio 5.**

[]{#significado-de-l3.7u}

#### 1. Significado de $L=3.7u$ {#fispm-c02-significado-de-l3.7u}

La expresión afirma que la longitud particular $L$ tiene, respecto de la referencia de longitud $u$, el valor numérico: $\{L\}_u=3.7.$ Equivalentemente: $\frac{L}{u}=3.7.$ No significa que $3.7$ sea la longitud. Significa que la longitud $L$ se expresa como $3.7$ veces la referencia elegida.

[]{#compatibilidad-de-tipo}

#### 2. Compatibilidad de tipo {#fispm-c02-compatibilidad-de-tipo .unnumbered}

Para formar la razón: $\frac{L}{u},$

$L$ y $u$ deben ser magnitudes comparables del mismo tipo.

Como $L$ es una longitud, $u$ debe ser también una longitud. Una masa o una duración no constituyen una unidad de longitud.

[]{#nueva-referencia}

#### 3. Nueva referencia {#fispm-c02-nueva-referencia .unnumbered}

Tenemos: $u'=\frac12u.$ La unidad nueva es dos veces más pequeña. Por la Proposición 1, si: $u'=\lambda u$

con: $\lambda=\frac12,$

entonces el nuevo valor numérico es: $q'=\frac{q}{\lambda} = \frac{3.7}{1/2} = 7.4.$

Por tanto:

$$\boxed{ L=7.4\,u'. }$$

La magnitud no cambió.

Cambió la referencia.

[]{#convención-y-comparación-física}

#### 4. Convención y comparación física {#fispm-c02-convenciuxf3n-y-comparaciuxf3n-fuxedsica .unnumbered}

Es convencional:

- elegir cierta barra como referencia;

- llamarla $u$;

- adoptar esa referencia de manera común.

La comparación física consiste en establecer la relación entre la longitud que queremos expresar y la longitud de referencia.

Podemos esquematizar:

$$\boxed{ \text{convención de referencia} + \text{comparación física} \longrightarrow \text{valor numérico}. }$$

[]{#por-qué-no-es-todavía-el-si}

#### 5. Por qué no es todavía el SI {#fispm-c02-por-quuxe9-no-es-todavuxeda-el-si .unnumbered}

El ejercicio construye un sistema local muy simple basado en una barra material. El SI contemporáneo es una estructura internacional mucho más precisa: sus unidades se definen mediante valores fijados de constantes definitorias y requieren procedimientos de realización y trazabilidad metrológica.

Por tanto:

$$\boxed{ \text{referencia local mediante una barra} \neq \text{definición moderna del SI}. }$$

El SI será el objeto de §3.

[]{#síntesis}

### Síntesis {#fispm-c02-suxedntesis}

§1 mostró que:

$$\boxed{ Q=\{Q\}_u\,u. }$$

§2 ha añadido la condición estructural que esa escritura presupone:

$$\boxed{ Q\text{ y }u\text{ deben pertenecer al mismo tipo de magnitud}. }$$

Definimos:

- la Definición 5 --- tipo de magnitud;

- la Definición 6 --- referencia de un valor de magnitud.

Y fijamos dos principios:

$$\boxed{ \text{comparabilidad física antes que comparación numérica} }$$

y:

$$\boxed{ \text{la unidad no determina por sí sola el significado físico}. }$$

Las cuatro negaciones que debemos conservar son:

$$\boxed{ \text{mismo número} \not\Rightarrow \text{mismo tipo}, }$$

$$\boxed{ \text{misma letra} \not\Rightarrow \text{mismo tipo}, }$$

$$\boxed{ \text{misma expresión de unidad} \not\Rightarrow \text{mismo tipo}, }$$

y:

$$\boxed{ \text{misma clase de magnitud} \not\Rightarrow \text{misma magnitud particular}. }$$

El siguiente paso será construir el sistema de unidades que usaremos de manera predominante en el tratado (§[3](#fispm-c02-el-sistema-internacional-contemporuxe1neo)).

Allí distinguiremos cuidadosamente:

- las siete magnitudes base;

- las siete unidades base;

- las siete constantes definitorias;

- definición de una unidad;

- realización práctica;

- prefijos y escritura correcta de símbolos.

[]{#el-sistema-internacional-contemporáneo}

[]{#fispm-t1-c02-s03}

[]{#fpm-i-02-s03}

## 3. El Sistema Internacional contemporáneo {#fispm-c02-el-sistema-internacional-contemporuxe1neo}

[]{#una-unidad-local-no-basta-para-una-ciencia-global}

### Una unidad local no basta para una ciencia global {#fispm-c02-una-unidad-local-no-basta-para-una-ciencia-global}

En §1 vimos que un valor de magnitud puede escribirse, en los casos ordinarios que nos interesan, como $Q=\{Q\}_u\,u.$ En §2 añadimos que la unidad $u$ debe ser una referencia compatible con el tipo de magnitud de $Q$. Todavía queda un problema. Nada impide que dos comunidades elijan referencias diferentes para la misma clase de magnitud.

Una longitud puede expresarse en metros, millas, pulgadas o mediante cualquier otra referencia definida de manera suficientemente precisa. Matemáticamente podemos convertir entre esas elecciones si conocemos sus relaciones. Pero una ciencia experimental internacional necesita algo más que la posibilidad abstracta de convertir.

Necesita un sistema que permita que resultados obtenidos en laboratorios distintos sean comparables sin renegociar desde cero el significado de cada unidad. Ésta es una de las funciones del **Sistema Internacional de Unidades**. El SI no es simplemente una tabla de nombres.

Es una infraestructura convencional para expresar valores de magnitudes de forma coherente, reproducible y globalmente comparable.

[]{#qué-significa-si-en-2026}

### Qué significa «SI» en 2026 {#fispm-c02-quuxe9-significa-si-en-2026}

La formulación contemporánea del SI debe leerse con cuidado. Antes de la revisión adoptada por la 26.ª CGPM en 2018 y efectiva desde el 20 de mayo de 2019, era habitual presentar el sistema diciendo que estaba definido mediante siete unidades base y que las demás unidades se derivaban de ellas.

Esa descripción histórica ya no es la definición fundamental vigente.

La formulación actual procede en la dirección inversa:

$$\boxed{ \text{siete valores exactos de constantes definitorias} \longrightarrow \text{definición del SI} \longrightarrow \text{unidades del SI}. }$$

La 9.ª edición de la *SI Brochure*, en su versión 4.01 de junio de 2026, mantiene esta arquitectura.[^8]

**Definición 7 --- Sistema Internacional de Unidades** El **Sistema Internacional de Unidades (SI)** es el sistema de unidades definido fijando exactamente los valores numéricos de siete constantes definitorias cuando se expresan en las unidades especificadas por el propio SI.

Esta definición operativa conserva el rasgo que necesitaremos matemáticamente:

$$\boxed{ \text{el sistema se fija mediante relaciones exactas entre valores de constantes y unidades}. }$$

No debemos leer esta frase como si las constantes fueran «elegidas arbitrariamente». Algunas son constantes fundamentales de la naturaleza y otra, como $K_{\mathrm{cd}}$, es de carácter técnico. Lo que fija convencionalmente el SI es **su valor numérico exacto en determinadas unidades**.

[]{#las-siete-constantes-definitorias}

### Las siete constantes definitorias {#fispm-c02-las-siete-constantes-definitorias}

Las siete constantes son las siguientes.[^9]

  Constante definitoria                                                                      Símbolo                     Valor numérico fijado exactamente   Unidad en la que se fija
  ------------------------------------------------------------------------------------------ --------------------------- ----------------------------------- --------------------------
  frecuencia de la transición hiperfina del estado fundamental no perturbado del cesio-133   $\Delta\nu_{\mathrm{Cs}}$   $9\,192\,631\,770$                  $\mathrm{Hz}$
  velocidad de la luz en el vacío                                                            $c$                         $299\,792\,458$                     $\mathrm{m\,s^{-1}}$
  constante de Planck                                                                        $h$                         $6.626\,070\,15\times10^{-34}$      $\mathrm{J\,s}$
  carga elemental                                                                            $e$                         $1.602\,176\,634\times10^{-19}$     $\mathrm C$
  constante de Boltzmann                                                                     $k$                         $1.380\,649\times10^{-23}$          $\mathrm{J\,K^{-1}}$
  constante de Avogadro                                                                      $N_{\mathrm A}$             $6.022\,140\,76\times10^{23}$       $\mathrm{mol^{-1}}$
  eficacia luminosa de una radiación monocromática definida                                  $K_{\mathrm{cd}}$           $683$                               $\mathrm{lm\,W^{-1}}$

En esta tabla aparecen nombres de unidades derivadas ---$\mathrm{Hz}$, $\mathrm J$, $\mathrm C$, $\mathrm{lm}$ y $\mathrm W$--- que estudiaremos sistemáticamente en §4.

Por ahora basta registrar las relaciones:

$$\mathrm{Hz}=\mathrm{s^{-1}},$$

$$\mathrm J=\mathrm{kg\,m^2\,s^{-2}},$$

$$\mathrm C=\mathrm{A\,s},$$

$$\mathrm W=\mathrm{kg\,m^2\,s^{-3}}.$$

La unidad lumen requerirá además la noción de estereorradián, que retomaremos al estudiar cantidades de dimensión uno.

[]{#exacto-por-definición-no-significa-medido-con-incertidumbre-cero}

### «Exacto por definición» no significa «medido con incertidumbre cero» {#fispm-c02-exacto-por-definiciuxf3n-no-significa-medido-con-incertidumbre-cero}

Esta distinción es fundamental. El valor numérico

$$299\,792\,458$$

asignado a $c$ cuando se expresa en $\mathrm{m\,s^{-1}}$ no es en el SI actual el resultado de una nueva medición cuyo último decimal podría modificarse mañana. Es un valor fijado exactamente por definición. Lo mismo ocurre con los otros seis valores de la tabla.

Por eso la *SI Brochure* declara que los valores numéricos de las siete constantes definitorias no tienen incertidumbre.[^10]

Pero sería un error inferir:

> «Entonces toda realización experimental del metro, del segundo o del kilogramo carece de incertidumbre.»

La definición y la realización son niveles distintos.

Podemos tener:

$$\boxed{ \text{definición exacta} \quad+\quad \text{realización experimental con incertidumbre}. }$$

La incertidumbre pertenece al proceso mediante el cual materializamos, comparamos o medimos la unidad en condiciones reales. Su tratamiento sistemático pertenece al capítulo 3.

[]{#constantes-definitorias-no-todas-son-del-mismo-carácter-físico}

### Constantes definitorias: no todas son del mismo carácter físico {#fispm-c02-constantes-definitorias-no-todas-son-del-mismo-caruxe1cter-fuxedsico}

Conviene evitar otra simplificación.

A veces se dice:

> «El SI está definido mediante siete constantes fundamentales de la naturaleza.»

La frase es demasiado fuerte. La propia *SI Brochure* distingue la naturaleza de las constantes definitorias. Algunas, como $c$ y $h$, son propiamente constantes fundamentales; $K_{\mathrm{cd}}$ es una constante técnica asociada a una convención fotométrica.[^11]

Por tanto, usaremos la expresión exacta:

$$\boxed{ \text{siete constantes definitorias} }$$

y no:

$$\boxed{ \text{siete constantes fundamentales} }$$

como si ambas clases coincidieran.

**Definición 8 --- Constante definitoria del SI** Una **constante definitoria del SI** es una de las siete constantes cuyo valor numérico se fija exactamente en la definición del SI cuando se expresa en la unidad correspondiente.

La palabra **definitoria** describe el papel que la constante cumple en el sistema de unidades.

[]{#las-siete-magnitudes-base-y-las-siete-unidades-base}

### Las siete magnitudes base y las siete unidades base {#fispm-c02-las-siete-magnitudes-base-y-las-siete-unidades-base}

Aunque el SI ya no se define fundamentalmente «a partir de las unidades base», las siete magnitudes base y sus unidades siguen cumpliendo un papel estructural central.[^12]

  Magnitud base               Símbolo típico        Unidad base   Símbolo
  --------------------------- --------------------- ------------- ----------------
  tiempo                      $t$                   segundo       $\mathrm s$
  longitud                    $l$, $x$, $r$, etc.   metro         $\mathrm m$
  masa                        $m$                   kilogramo     $\mathrm{kg}$
  corriente eléctrica         $I$, $i$              amperio       $\mathrm A$
  temperatura termodinámica   $T$                   kelvin        $\mathrm K$
  cantidad de sustancia       $n$                   mol           $\mathrm{mol}$
  intensidad luminosa         $I_{\mathrm v}$       candela       $\mathrm{cd}$

**Definición 9 --- Magnitud base del SI** Una **magnitud base del SI** es una de las siete magnitudes elegidas convencionalmente como base para organizar el sistema de dimensiones y unidades del SI: tiempo, longitud, masa, corriente eléctrica, temperatura termodinámica, cantidad de sustancia e intensidad luminosa.

**Definición 10 --- Unidad base del SI** Una **unidad base del SI** es la unidad SI asociada a una de las siete magnitudes base: segundo, metro, kilogramo, amperio, kelvin, mol o candela.

La palabra **base** indica un papel dentro de la arquitectura del sistema.

No significa que una magnitud base sea «más real» o «más importante» que una magnitud derivada.

[]{#las-unidades-base-no-son-siete-patrones-materiales}

### Las unidades base no son siete patrones materiales {#fispm-c02-las-unidades-base-no-son-siete-patrones-materiales}

La palabra «unidad» puede evocar una colección de objetos guardados en un laboratorio:

- una barra patrón;

- una masa patrón;

- un reloj patrón;

- y así sucesivamente.

Ésa no es la estructura conceptual del SI actual. El kilogramo, por ejemplo, ya no se define como la masa del Prototipo Internacional del Kilogramo. La unidad se define mediante las constantes del SI; después debe **realizarse** experimentalmente mediante métodos compatibles con esa definición.

Esto permite que los métodos de realización mejoren sin obligarnos a cambiar cada vez la definición de la unidad.

La separación es:

$$\boxed{ \text{definición} \neq \text{artefacto particular} \neq \text{procedimiento concreto de realización}. }$$

[]{#no-existe-una-correspondencia-simple-una-constante-una-unidad-base}

### No existe una correspondencia simple «una constante = una unidad base» {#fispm-c02-no-existe-una-correspondencia-simple-una-constante-una-unidad-base}

La presencia de siete constantes y siete unidades base invita a imaginar siete parejas independientes:

$$c\leftrightarrow \mathrm m, \qquad h\leftrightarrow\mathrm{kg}, \qquad\ldots$$

Esta representación puede servir como recordatorio pedagógico muy aproximado, pero no describe fielmente la estructura lógica. La propia documentación del BIPM advierte que no existe una correspondencia uno a uno entre las siete constantes definitorias y las siete unidades base: la definición de varias unidades base utiliza más de una constante.[^13]

Por ejemplo, el kilogramo se expresa mediante la constante de Planck, pero la unidad

$$\mathrm{J\,s}$$

que aparece en el valor de $h$ contiene a su vez metro y segundo. Por tanto, el SI debe entenderse como una **red coherente de relaciones definitorias**, no como siete definiciones aisladas.

[]{#definición-y-realización}

### Definición y realización {#fispm-c02-definiciuxf3n-y-realizaciuxf3n}

El BIPM utiliza la expresión francesa *mise en pratique* para los documentos que describen maneras de realizar prácticamente las definiciones de las unidades.

Esto nos da una distinción permanente:

**Principio 5 --- No confundir definición y realización** La definición de una unidad fija su significado dentro del SI; una realización es un procedimiento físico para materializar o acceder experimentalmente a esa definición. Una definición puede ser exacta aunque toda realización concreta posea incertidumbre.

Esta diferencia será decisiva cuando estudiemos medición.

En términos del capítulo anterior:

$$\text{definición de unidad}$$

pertenece a la infraestructura convencional del modelo de medida, mientras que

$$\text{realización}$$

introduce sistemas físicos, instrumentos, procedimientos y condiciones experimentales.

[]{#base-tampoco-significa-fundamental-en-la-ontología-de-la-física}

### «Base» tampoco significa «fundamental en la ontología de la física» {#fispm-c02-base-tampoco-significa-fundamental-en-la-ontologuxeda-de-la-fuxedsica}

La elección de las siete magnitudes base posee una función organizativa e histórica.

No debemos inferir de ella una jerarquía ontológica. Por ejemplo, energía no es una magnitud base del SI. Eso no significa que la energía sea físicamente secundaria o poco importante.

La unidad de energía, el joule, puede expresarse mediante unidades base: $1\,\mathrm J = 1\,\mathrm{kg\,m^2\,s^{-2}}.$ La clasificación «base/derivada» responde a cómo organizamos el sistema de unidades.

**Principio 6 --- «Base» es una función del sistema de unidades** Que una magnitud o unidad sea base en el SI no implica que sea físicamente más fundamental que una magnitud o unidad derivada. La distinción organiza la representación metrológica.

Esta regla evitará confundir:

$$\text{fundamentalidad física}$$

con

$$\text{estatus metrológico de base}.$$

[]{#prefijos-si}

### Prefijos SI {#fispm-c02-prefijos-si}

El SI permite construir múltiplos y submúltiplos decimales mediante prefijos. La lista vigente llega desde

$$10^{-30}$$

hasta

$$10^{30}.$$

Los cuatro prefijos más recientes fueron adoptados por la 27.ª CGPM en 2022: **ronna**, **quetta**, **ronto** y **quecto**.[^14]

  Factor      Prefijo   Símbolo         Factor       Prefijo   Símbolo
  ----------- --------- --------------- ------------ --------- ----------------
  $10^{30}$   quetta    $\mathrm Q$     $10^{-30}$   quecto    $\mathrm q$
  $10^{27}$   ronna     $\mathrm R$     $10^{-27}$   ronto     $\mathrm r$
  $10^{24}$   yotta     $\mathrm Y$     $10^{-24}$   yocto     $\mathrm y$
  $10^{21}$   zetta     $\mathrm Z$     $10^{-21}$   zepto     $\mathrm z$
  $10^{18}$   exa       $\mathrm E$     $10^{-18}$   atto      $\mathrm a$
  $10^{15}$   peta      $\mathrm P$     $10^{-15}$   femto     $\mathrm f$
  $10^{12}$   tera      $\mathrm T$     $10^{-12}$   pico      $\mathrm p$
  $10^{9}$    giga      $\mathrm G$     $10^{-9}$    nano      $\mathrm n$
  $10^{6}$    mega      $\mathrm M$     $10^{-6}$    micro     $\mathrm{\mu}$
  $10^{3}$    kilo      $\mathrm k$     $10^{-3}$    mili      $\mathrm m$
  $10^{2}$    hecto     $\mathrm h$     $10^{-2}$    centi     $\mathrm c$
  $10^{1}$    deca      $\mathrm{da}$   $10^{-1}$    deci      $\mathrm d$

La tabla debe leerse algebraicamente.

Por ejemplo:

$$1\,\mathrm{km}=10^3\,\mathrm m,$$

$$1\,\mathrm{\mu s}=10^{-6}\,\mathrm s,$$

$$1\,\mathrm{nm}=10^{-9}\,\mathrm m.$$

[]{#el-prefijo-forma-parte-de-la-unidad}

### El prefijo forma parte de la unidad {#fispm-c02-el-prefijo-forma-parte-de-la-unidad}

Cuando escribimos

$$1\,\mathrm{cm},$$

la unidad completa es el **centímetro**. Su relación con el metro es: $1\,\mathrm{cm} = 10^{-2}\,\mathrm m.$ Esto tiene una consecuencia importante cuando elevamos unidades a potencias.

Para área:

$$1\,\mathrm{cm^2} = (1\,\mathrm{cm})^2 = (10^{-2}\,\mathrm m)^2 = 10^{-4}\,\mathrm{m^2}.$$

No: $1\,\mathrm{cm^2} = 10^{-2}\,\mathrm{m^2}.$

Para volumen:

$$1\,\mathrm{mm^3} = (10^{-3}\,\mathrm m)^3 = 10^{-9}\,\mathrm{m^3}.$$

El exponente afecta a toda la unidad prefijada.

[]{#no-se-encadenan-prefijos}

### No se encadenan prefijos {#fispm-c02-no-se-encadenan-prefijos}

Los prefijos SI no se apilan. Por ejemplo, no escribimos una supuesta unidad «milimicrómetro» mediante una cadena de prefijos. Se elige un único prefijo cuyo factor total represente la escala deseada.

Así: $10^{-9}\,\mathrm m = 1\,\mathrm{nm},$

no una composición de «mili» y «micro».

Esto mantiene unívoca la lectura de los símbolos.

[]{#la-excepción-histórica-del-kilogramo}

### La excepción histórica del kilogramo {#fispm-c02-la-excepciuxf3n-histuxf3rica-del-kilogramo}

El kilogramo tiene una peculiaridad nominal:

$$\boxed{\mathrm{kg}}$$

es la única unidad base del SI cuyo nombre ya contiene un prefijo. Por esa razón, los múltiplos y submúltiplos de masa se forman aplicando prefijos a **gramo**, no añadiendo un segundo prefijo a kilogramo.

Por ejemplo:

$$1\,\mathrm{mg} = 10^{-3}\,\mathrm g = 10^{-6}\,\mathrm{kg}.$$

Y:

$$1\,\mathrm{\mu g} = 10^{-6}\,\mathrm g = 10^{-9}\,\mathrm{kg}.$$

No escribimos: $\mathrm{mkg}$

para representar miligramos. Esta regla es histórica y notacional, no una dificultad matemática.

[]{#las-mayúsculas-importan}

### Las mayúsculas importan {#fispm-c02-las-mayuxfasculas-importan}

Los símbolos SI son sensibles a mayúsculas y minúsculas. Por ejemplo: $\mathrm m$

es metro, mientras que

$$\mathrm M$$

es el prefijo mega cuando antecede a un símbolo de unidad.

Del mismo modo: $\mathrm k$

es kilo, mientras que

$$\mathrm K$$

es kelvin. Por eso: $1\,\mathrm{km}$

y

$$1\,\mathrm{Km}$$

no son escrituras equivalentes del SI. La segunda combina una grafía de prefijo incorrecta con el símbolo del metro.

[]{#reglas-elementales-de-escritura}

### Reglas elementales de escritura {#fispm-c02-reglas-elementales-de-escritura}

Usaremos desde ahora las siguientes convenciones.

[]{#regla-1-espacio-entre-número-y-símbolo-de-unidad}

#### Regla 1 --- Espacio entre número y símbolo de unidad {#fispm-c02-regla-1-espacio-entre-nuxfamero-y-suxedmbolo-de-unidad}

Escribiremos:

$$25\,\mathrm m,$$

$$3.2\,\mathrm s,$$

$$300\,\mathrm K.$$

En texto Markdown/LaTeX representaremos el espacio tipográfico dentro de la fórmula mediante `\,` cuando sea útil.

[]{#regla-2-los-símbolos-de-unidad-no-se-pluralizan}

#### Regla 2 --- Los símbolos de unidad no se pluralizan {#fispm-c02-regla-2-los-suxedmbolos-de-unidad-no-se-pluralizan}

Escribimos: $5\,\mathrm{kg},$

no: $5\,\mathrm{kgs}.$

[]{#regla-3-el-símbolo-no-lleva-punto-por-ser-abreviatura}

#### Regla 3 --- El símbolo no lleva punto por ser abreviatura {#fispm-c02-regla-3-el-suxedmbolo-no-lleva-punto-por-ser-abreviatura}

Escribimos: $10\,\mathrm m$

y no añadimos un punto a $\mathrm m$ salvo que el signo de puntuación corresponda al final de la oración.

[]{#regla-4-los-prefijos-se-unen-al-símbolo-de-unidad}

#### Regla 4 --- Los prefijos se unen al símbolo de unidad {#fispm-c02-regla-4-los-prefijos-se-unen-al-suxedmbolo-de-unidad}

Escribimos:

$$\mathrm{mm}, \qquad \mathrm{MHz}, \qquad \mathrm{\mu s}.$$

El prefijo no se separa mediante un espacio del símbolo de la unidad.

[]{#regla-5-una-potencia-actúa-sobre-toda-la-unidad}

#### Regla 5 --- Una potencia actúa sobre toda la unidad {#fispm-c02-regla-5-una-potencia-actuxfaa-sobre-toda-la-unidad}

Ya vimos: $\mathrm{cm^2} = (10^{-2}\,\mathrm m)^2.$ Esta regla será esencial en conversiones de área y volumen.

[]{#unidades-símbolos-y-nombres-no-son-intercambiables-sin-reglas}

### Unidades, símbolos y nombres no son intercambiables sin reglas {#fispm-c02-unidades-suxedmbolos-y-nombres-no-son-intercambiables-sin-reglas}

Consideremos: $5\,\mathrm m.$

Aquí:

- $5$ es valor numérico;

- $\mathrm m$ es símbolo de la unidad metro;

- «metro» es el nombre de esa unidad;

- el producto representa un valor de longitud.

El símbolo $\mathrm m$ no es una variable algebraica ordinaria cuyo significado pueda redefinirse libremente dentro de un cálculo. En este capítulo lo manipularemos formalmente de acuerdo con las relaciones del sistema de unidades. Esto permitirá más adelante escribir, por ejemplo: $\frac{\mathrm m}{\mathrm s}$

sin perder de vista que estamos calculando con representaciones de unidades físicas.

[]{#ejemplo-desarrollado-la-misma-velocidad-en-dos-unidades}

### Ejemplo desarrollado --- La misma velocidad en dos unidades {#fispm-c02-ejemplo-desarrollado-la-misma-velocidad-en-dos-unidades}

Supongamos una rapidez: $v=25\,\mathrm{m\,s^{-1}}.$

Queremos expresarla en kilómetros por hora.

Usamos: $1\,\mathrm{km}=1000\,\mathrm m$

y: $1\,\mathrm h=3600\,\mathrm s.$

Entonces:

$$25\,\frac{\mathrm m}{\mathrm s} \left( \frac{1\,\mathrm{km}}{1000\,\mathrm m} \right) \left( \frac{3600\,\mathrm s}{1\,\mathrm h} \right) = 25\frac{3600}{1000}\, \frac{\mathrm{km}}{\mathrm h}.$$

Por tanto: $v=90\,\mathrm{km\,h^{-1}}.$ La magnitud física no cambió.

Cambió su representación numérica respecto de otras unidades.

Recuperamos así el Principio 2:

$$\boxed{ 25\,\mathrm{m\,s^{-1}} = 90\,\mathrm{km\,h^{-1}}. }$$

[]{#ejemplo-desarrollado-por-qué-1mathrmcm2-no-es-10-2mathrmm2}

### Ejemplo desarrollado --- Por qué $1\,\mathrm{cm^2}$ no es $10^{-2}\,\mathrm{m^2}$ {#fispm-c02-ejemplo-desarrollado-por-quuxe9-1mathrmcm2-no-es-10-2mathrmm2}

Tomemos un cuadrado de lado: $1\,\mathrm{cm}.$

Como: $1\,\mathrm{cm}=10^{-2}\,\mathrm m,$

su área es: $A = (10^{-2}\,\mathrm m)(10^{-2}\,\mathrm m).$ Por tanto: $A = 10^{-4}\,\mathrm{m^2}.$ El error

$$1\,\mathrm{cm^2}=10^{-2}\,\mathrm{m^2}$$

aparece cuando se aplica el factor del prefijo una sola vez en lugar de elevarlo junto con la unidad. Este tipo de error será muy importante cuando trabajemos con densidades, presiones y otras magnitudes derivadas.

[]{#ejercicios-de-3}

### Ejercicios de §3 {#fispm-c02-ejercicios-de-3}

**Ejercicio 6 --- Leer correctamente el SI actual**

**Tipo:** conceptual · **Nivel:** central

Decide si cada afirmación es correcta o incorrecta. Cuando sea incorrecta, reescríbela.

1.  «El SI actual se define fundamentalmente eligiendo siete objetos que materializan las siete unidades base.»

2.  «Los valores numéricos de las siete constantes definitorias son exactos dentro del SI.»

3.  «Si el valor definitorio de una constante es exacto, cualquier realización experimental de la unidad correspondiente tiene incertidumbre exactamente cero.»

4.  «Las siete unidades base siguen desempeñando una función estructural en el SI actual.»

5.  «Cada una de las siete constantes definitorias corresponde de manera aislada y uno a uno a exactamente una unidad base.»

6.  «Que el joule sea una unidad derivada significa que la energía es físicamente menos fundamental que la longitud.»

7.  «La constante $K_{\mathrm{cd}}$ es una constante definitoria del SI, aunque no tenga el mismo carácter físico que $c$ o $h$.»

**Solución**

**1. Incorrecta.**

El SI contemporáneo se define fijando exactamente los valores numéricos de siete constantes definitorias en unidades especificadas. Las unidades no se definen mediante siete objetos materiales.

**2. Correcta.**

En el SI esos valores no son resultados experimentales ajustables: forman parte de la definición.

**3. Incorrecta.**

Debemos distinguir:

$$\text{definición exacta} \neq \text{realización experimental exacta}.$$

Una realización concreta utiliza sistemas físicos e instrumentos y puede tener incertidumbre.

**4. Correcta.**

Segundo, metro, kilogramo, amperio, kelvin, mol y candela siguen siendo las siete unidades base y organizan la expresión de unidades derivadas y dimensiones.

**5. Incorrecta.**

No existe una correspondencia uno a uno simple. Varias definiciones de unidades base dependen de más de una constante definitoria.

**6. Incorrecta.**

«Base» y «derivada» son categorías de organización del sistema de unidades. No establecen por sí mismas una jerarquía ontológica de conceptos físicos.

**7. Correcta.**

$K_{\mathrm{cd}}$ pertenece al conjunto de siete constantes definitorias, pero la propia documentación del SI distingue constantes fundamentales y constantes de carácter técnico.

La conclusión conjunta es:

$$\boxed{ \text{definición del SI} \neq \text{lista de siete artefactos} }$$

y:

$$\boxed{ \text{unidad base} \neq \text{magnitud físicamente más fundamental}. }$$

**Ejercicio 7 --- Prefijos y potencias de diez**

**Tipo:** cálculo · **Nivel:** central

Convierte:

1.  $3.6\,\mathrm{km}$ a metros.

2.  $250\,\mathrm{\mu s}$ a segundos.

3.  $7.2\,\mathrm{nm}$ a metros.

4.  $4.5\,\mathrm{cm^2}$ a metros cuadrados.

5.  $2.0\,\mathrm{mm^3}$ a metros cúbicos.

6.  $5\,\mathrm{mg}$ a kilogramos.

7.  $2.4\,\mathrm{Rm}$ a metros.

8.  $6\,\mathrm{qs}$ a segundos.

Explica además por qué: $1\,\mathrm{cm^2}\neq10^{-2}\,\mathrm{m^2}.$

**Solución**

**1. Kilómetros a metros**

$$1\,\mathrm{km}=10^3\,\mathrm m.$$

Entonces: $3.6\,\mathrm{km} = 3.6\times10^3\,\mathrm m.$

Por tanto:

$$\boxed{ 3.6\,\mathrm{km}=3600\,\mathrm m. }$$

**2. Microsegundos a segundos**

$$1\,\mathrm{\mu s}=10^{-6}\,\mathrm s.$$

Luego:

$$250\,\mathrm{\mu s} = 250\times10^{-6}\,\mathrm s = 2.50\times10^{-4}\,\mathrm s.$$

**3. Nanómetros a metros**

$$1\,\mathrm{nm}=10^{-9}\,\mathrm m.$$

Así:

$$\boxed{ 7.2\,\mathrm{nm} = 7.2\times10^{-9}\,\mathrm m. }$$

**4. Centímetros cuadrados a metros cuadrados**

$$1\,\mathrm{cm} = 10^{-2}\,\mathrm m.$$

Elevamos toda la unidad al cuadrado:

$$1\,\mathrm{cm^2} = (10^{-2}\,\mathrm m)^2 = 10^{-4}\,\mathrm{m^2}.$$

Entonces:

$$\boxed{ 4.5\,\mathrm{cm^2} = 4.5\times10^{-4}\,\mathrm{m^2}. }$$

**5. Milímetros cúbicos a metros cúbicos**

$$1\,\mathrm{mm} = 10^{-3}\,\mathrm m.$$

Por tanto:

$$1\,\mathrm{mm^3} = (10^{-3}\,\mathrm m)^3 = 10^{-9}\,\mathrm{m^3}.$$

Así:

$$\boxed{ 2.0\,\mathrm{mm^3} = 2.0\times10^{-9}\,\mathrm{m^3}. }$$

**6. Miligramos a kilogramos**

$$1\,\mathrm{mg} = 10^{-3}\,\mathrm g.$$

Además: $1\,\mathrm g = 10^{-3}\,\mathrm{kg}.$

Entonces: $1\,\mathrm{mg} = 10^{-6}\,\mathrm{kg}.$

Por tanto:

$$\boxed{ 5\,\mathrm{mg} = 5\times10^{-6}\,\mathrm{kg}. }$$

**7. Ronnametros a metros**

El prefijo ronna, símbolo $\mathrm R$, representa: $10^{27}.$

Entonces:

$$\boxed{ 2.4\,\mathrm{Rm} = 2.4\times10^{27}\,\mathrm m. }$$

**8. Quectosegundos a segundos**

El prefijo quecto, símbolo $\mathrm q$, representa: $10^{-30}.$

Luego:

$$\boxed{ 6\,\mathrm{qs} = 6\times10^{-30}\,\mathrm s. }$$

Finalmente:

$$1\,\mathrm{cm^2} = (10^{-2}\,\mathrm m)^2 = 10^{-4}\,\mathrm{m^2},$$

porque el exponente $2$ actúa tanto sobre el metro como sobre el factor $10^{-2}$.

Por eso:

$$\boxed{ 1\,\mathrm{cm^2}\neq10^{-2}\,\mathrm{m^2}. }$$

[]{#síntesis-1}

### Síntesis {#fispm-c02-suxedntesis-1}

El SI contemporáneo se organiza mediante dos capas que no debemos confundir.

La capa definitoria:

$$\boxed{ \Delta\nu_{\mathrm{Cs}}, c, h, e, k, N_{\mathrm A}, K_{\mathrm{cd}} }$$

con valores numéricos fijados exactamente.

Y la capa organizativa de las unidades base:

$$\boxed{ \mathrm s,\, \mathrm m,\, \mathrm{kg},\, \mathrm A,\, \mathrm K,\, \mathrm{mol},\, \mathrm{cd}. }$$

Las dos están relacionadas, pero no mediante siete parejas aisladas.

Además:

$$\boxed{ \text{definición} \neq \text{realización} }$$

y:

$$\boxed{ \text{base} \neq \text{más fundamental físicamente}. }$$

Los prefijos SI permiten cambiar cómodamente de escala decimal, pero deben manipularse algebraicamente con cuidado:

$$\boxed{ (pu)^n=p^n u^n. }$$

Por eso las conversiones de área y volumen exigen elevar también el factor del prefijo. Con esta infraestructura ya podemos avanzar al siguiente nivel. Hasta ahora hemos trabajado principalmente con unidades escogidas para clases de magnitudes ya conocidas.

En §4 construiremos nuevas magnitudes mediante productos y cocientes y veremos cómo aparecen sistemáticamente las **unidades derivadas coherentes** (§[4](#fispm-c02-magnitudes-derivadas-y-unidades-coherentes)).

------------------------------------------------------------------------

[]{#fispm-c02-fuentes-normativas-de-3 label="fispm-c02-fuentes-normativas-de-3"}

[]{#magnitudes-derivadas-y-unidades-coherentes}

[]{#fispm-t1-c02-s04}

[]{#fpm-i-02-s04}

## 4. Magnitudes derivadas y unidades coherentes {#fispm-c02-magnitudes-derivadas-y-unidades-coherentes}

[]{#las-unidades-también-obedecen-relaciones}

### Las unidades también obedecen relaciones {#fispm-c02-las-unidades-tambiuxe9n-obedecen-relaciones}

En §1 distinguimos una magnitud de su valor numérico y de la unidad elegida para expresarla. En §2 vimos que la comparabilidad física precede a la comparación numérica. En §3 fijamos la arquitectura contemporánea del Sistema Internacional.

Ahora aparece una cuestión nueva: las magnitudes físicas no se presentan siempre de manera aislada. Un modelo puede relacionarlas mediante productos, cocientes y potencias. Por ejemplo,

$$v=\frac{\ell}{t},$$

$$\rho=\frac{m}{V},$$

o

$$A=xy.$$

Estas relaciones entre magnitudes inducen relaciones entre las unidades utilizadas para expresarlas.

La idea rectora será:

$$\boxed{ \text{estructura algebraica entre magnitudes} \longrightarrow \text{estructura correspondiente entre unidades} }$$

Pero no toda combinación de unidades es **coherente** con el sistema elegido, y una misma expresión de unidad puede corresponder a tipos de magnitud físicamente distintos.

[]{#magnitud-derivada}

### Magnitud derivada {#fispm-c02-magnitud-derivada}

**Definición 11 --- Magnitud derivada** Una **magnitud derivada** es una magnitud definida, dentro de un sistema de magnitudes, mediante una relación algebraica con otras magnitudes del sistema, en particular con las magnitudes tomadas como base.

Ejemplos elementales son: $A=xy,$

para un área rectangular; $V=xyz,$

para un volumen; $v=\frac{\ell}{t},$

para una rapidez o velocidad escalar en un modelo elemental;

y

$$\rho=\frac{m}{V},$$

para densidad de masa. La palabra **derivada** no significa que la magnitud sea menos física, menos importante o menos observable. Describe su papel dentro de la arquitectura elegida.

Así,

$$\boxed{ \text{base/derivada} = \text{papel dentro de un sistema de magnitudes} }$$

y no una jerarquía ontológica.

[]{#producto-cociente-y-potencia}

### Producto, cociente y potencia {#fispm-c02-producto-cociente-y-potencia}

Sean

$$Q_1=q_1u_1, \qquad Q_2=q_2u_2.$$

Si

$$Q=Q_1Q_2,$$

entonces $Q=(q_1q_2)(u_1u_2).$ La unidad producto natural es $u=u_1u_2.$

Si

$$Q=\frac{Q_1}{Q_2},$$

entonces $Q= \frac{q_1}{q_2} \frac{u_1}{u_2},$

de modo que aparece

$$u=\frac{u_1}{u_2}.$$

Y si

$$Q=Q_1^n,$$

para un exponente entero $n$, entonces $Q=q_1^n u_1^n.$ Por tanto, producto, cociente y potencia de magnitudes inducen producto, cociente y potencia de unidades. Todavía no estamos hablando formalmente de dimensiones. Eso corresponde a §5.

[]{#unidad-derivada}

### Unidad derivada {#fispm-c02-unidad-derivada}

**Definición 12 --- Unidad derivada** Una **unidad derivada** es una unidad asociada a una magnitud derivada y expresable, dentro del sistema de unidades considerado, mediante productos de potencias de unidades base.

En el SI:

$$\text{área}\longrightarrow \mathrm{m^2},$$

$$\text{volumen}\longrightarrow \mathrm{m^3},$$

$$\text{rapidez o velocidad}\longrightarrow \mathrm{m\,s^{-1}},$$

$$\text{aceleración}\longrightarrow \mathrm{m\,s^{-2}},$$

$$\text{densidad de masa}\longrightarrow \mathrm{kg\,m^{-3}}.$$

La *SI Brochure* vigente incluye precisamente estas expresiones entre sus ejemplos de unidades derivadas coherentes.[^15]

[]{#unidad-derivada-coherente}

### Unidad derivada coherente {#fispm-c02-unidad-derivada-coherente}

**Definición 13 --- Unidad derivada coherente** Una **unidad derivada coherente**, respecto de un sistema de magnitudes y un conjunto elegido de unidades base, es una unidad derivada que se obtiene como producto de potencias de las unidades base sin introducir ningún factor de proporcionalidad distinto de $1$.

Así, $\mathrm{m\,s^{-1}}$

es la unidad coherente SI de rapidez o velocidad, $\mathrm{m\,s^{-2}}$

la de aceleración, y

$$\mathrm{kg\,m^{-3}}$$

la de densidad de masa. En cambio, $\mathrm{cm\,s^{-1}}$

puede ser una unidad perfectamente válida para expresar una rapidez, pero no es la unidad derivada coherente de rapidez **en el SI**, porque

$$1\,\mathrm{cm}=10^{-2}\,\mathrm m$$

introduce un factor distinto de $1$ respecto de la unidad base metro. La coherencia no significa «unidad correcta frente a unidad incorrecta». Significa que la unidad se obtiene de la base elegida sin factores adicionales.

[]{#por-qué-importa-la-coherencia}

### Por qué importa la coherencia {#fispm-c02-por-quuxe9-importa-la-coherencia}

Consideremos

$$v=\frac{\ell}{t}.$$

Escribamos

$$\ell=\{\ell\}_{\mathrm m}\,\mathrm m,$$

$$t=\{t\}_{\mathrm s}\,\mathrm s,$$

$$v=\{v\}_{\mathrm{m\,s^{-1}}}\,\mathrm{m\,s^{-1}}.$$

Sustituyendo:

$$\{v\}_{\mathrm{m\,s^{-1}}}\,\mathrm{m\,s^{-1}} = \frac{\{\ell\}_{\mathrm m}\,\mathrm m} {\{t\}_{\mathrm s}\,\mathrm s}.$$

Por tanto,

$$\boxed{ \{v\}_{\mathrm{m\,s^{-1}}} = \frac{\{\ell\}_{\mathrm m}}{\{t\}_{\mathrm s}} }.$$

La ecuación entre valores numéricos conserva exactamente la forma de la ecuación entre magnitudes. Éste es el sentido técnico de coherencia empleado por el BIPM.[^16]

**Principio 7 --- La coherencia preserva la forma numérica de las ecuaciones de magnitudes** Cuando todas las magnitudes de una relación se expresan mediante unidades pertenecientes a un sistema coherente, la ecuación entre sus valores numéricos tiene la misma forma que la ecuación entre las magnitudes, sin factores de conversión adicionales.

[]{#ejemplo-rapidez-en-unidades-coherentes}

### Ejemplo: rapidez en unidades coherentes {#fispm-c02-ejemplo-rapidez-en-unidades-coherentes}

Si

$$\ell=120\,\mathrm m$$

y

$$t=30\,\mathrm s,$$

entonces

$$v=\frac{120\,\mathrm m}{30\,\mathrm s} = 4\,\mathrm{m\,s^{-1}}.$$

La ecuación numérica es simplemente

$$4=\frac{120}{30}.$$

No aparece ningún factor extra.

[]{#qué-ocurre-cuando-mezclamos-unidades-no-coherentes}

### Qué ocurre cuando mezclamos unidades no coherentes {#fispm-c02-quuxe9-ocurre-cuando-mezclamos-unidades-no-coherentes}

Expresemos la misma longitud como $\ell=12\,000\,\mathrm{cm}.$ Si mantenemos $t$ en segundos y queremos $v$ en $\mathrm{m\,s^{-1}}$, entonces $1\,\mathrm{cm}=10^{-2}\,\mathrm m$

y

$$v = \frac{12\,000\times10^{-2}\,\mathrm m} {30\,\mathrm s} = 4\,\mathrm{m\,s^{-1}}.$$

La ecuación numérica se vuelve

$$\boxed{ \{v\}_{\mathrm{m\,s^{-1}}} = 10^{-2} \frac{\{\ell\}_{\mathrm{cm}}}{\{t\}_{\mathrm s}} }.$$

El factor $10^{-2}$ no pertenece a la física de la relación. Pertenece a nuestra mezcla de unidades. Ésa es una ventaja práctica de la coherencia: separa la estructura física de los factores de conversión.

[]{#área-volumen-y-potencias-de-unidades}

### Área, volumen y potencias de unidades {#fispm-c02-uxe1rea-volumen-y-potencias-de-unidades}

Si un cuadrado tiene lado

$$\ell=3\,\mathrm m,$$

entonces $A=\ell^2 = (3\,\mathrm m)^2 = 9\,\mathrm{m^2}.$ La potencia actúa sobre el número y sobre la unidad. Análogamente, si

$$\ell=2\,\mathrm m,$$

entonces $V=\ell^3 = (2\,\mathrm m)^3 = 8\,\mathrm{m^3}.$ Por eso

$$1\,\mathrm{cm^2} = (10^{-2}\,\mathrm m)^2 = 10^{-4}\,\mathrm{m^2},$$

y

$$1\,\mathrm{cm^3} = (10^{-2}\,\mathrm m)^3 = 10^{-6}\,\mathrm{m^3}.$$

[]{#densidad-de-masa}

### Densidad de masa {#fispm-c02-densidad-de-masa}

Para

$$\rho=\frac{m}{V},$$

las unidades coherentes dan

$$\rho = \frac{\{m\}_{\mathrm{kg}}}{\{V\}_{\mathrm{m^3}}} \mathrm{kg\,m^{-3}}.$$

Así,

$$\boxed{ \{\rho\}_{\mathrm{kg\,m^{-3}}} = \frac{\{m\}_{\mathrm{kg}}} {\{V\}_{\mathrm{m^3}}} }.$$

Si

$$m=6\,\mathrm{kg}$$

y

$$V=2\times10^{-3}\,\mathrm{m^3},$$

entonces $\rho = 3\times10^3\,\mathrm{kg\,m^{-3}}.$

[]{#prefijos-y-coherencia}

### Prefijos y coherencia {#fispm-c02-prefijos-y-coherencia}

En §3 vimos que los prefijos introducen factores decimales.

Aunque el centímetro sea una unidad construida correctamente mediante un prefijo SI, $1\,\mathrm{cm}=10^{-2}\,\mathrm m,$

y por tanto no pertenece al conjunto de unidades SI coherentes respecto de la base cuyo representante de longitud es el metro. La *SI Brochure* indica expresamente que una unidad prefijada deja de ser coherente porque aparece un factor numérico distinto de $1$.[^17]

[]{#unidades-coherentes-con-nombres-especiales}

### Unidades coherentes con nombres especiales {#fispm-c02-unidades-coherentes-con-nombres-especiales}

Ciertas combinaciones aparecen tan frecuentemente que el SI les asigna nombres y símbolos especiales.

Por ejemplo:

$$1\,\mathrm N = 1\,\mathrm{kg\,m\,s^{-2}},$$

$$1\,\mathrm{Pa} = 1\,\mathrm{kg\,m^{-1}\,s^{-2}},$$

$$1\,\mathrm J = 1\,\mathrm{kg\,m^2\,s^{-2}},$$

$$1\,\mathrm W = 1\,\mathrm{kg\,m^2\,s^{-3}}.$$

El nombre especial no cambia la estructura algebraica de la unidad.

**Principio 8 --- Un nombre especial no crea una nueva clase algebraica de unidad** Una unidad SI con nombre especial sigue siendo una unidad coherente expresable mediante productos de potencias de unidades base. El nombre especial mejora la lectura y puede ayudar a distinguir contextos físicos, pero no altera la estructura algebraica de la unidad.

[]{#las-22-unidades-si-con-nombres-especiales}

### Las 22 unidades SI con nombres especiales {#fispm-c02-las-22-unidades-si-con-nombres-especiales}

La *SI Brochure* vigente enumera 22 unidades SI con nombres y símbolos especiales.[^18]

  Magnitud asociada              Nombre           Símbolo               Expresión o relación coherente
  ------------------------------ ---------------- --------------------- -------------------------------------------
  ángulo plano                   radián           $\mathrm{rad}$        $1$
  ángulo sólido                  estereorradián   $\mathrm{sr}$         $1$
  frecuencia                     hercio           $\mathrm{Hz}$         $\mathrm{s^{-1}}$
  fuerza                         newton           $\mathrm N$           $\mathrm{kg\,m\,s^{-2}}$
  presión, tensión mecánica      pascal           $\mathrm{Pa}$         $\mathrm{kg\,m^{-1}\,s^{-2}}$
  energía, trabajo, calor        joule            $\mathrm J$           $\mathrm{kg\,m^2\,s^{-2}}$
  potencia, flujo radiante       watt             $\mathrm W$           $\mathrm{kg\,m^2\,s^{-3}}$
  carga eléctrica                coulomb          $\mathrm C$           $\mathrm{A\,s}$
  diferencia de potencial        volt             $\mathrm V$           $\mathrm{kg\,m^2\,s^{-3}\,A^{-1}}$
  capacitancia                   farad            $\mathrm F$           $\mathrm{kg^{-1}\,m^{-2}\,s^4\,A^2}$
  resistencia eléctrica          ohm              $\mathrm{\Omega}$     $\mathrm{kg\,m^2\,s^{-3}\,A^{-2}}$
  conductancia eléctrica         siemens          $\mathrm S$           $\mathrm{kg^{-1}\,m^{-2}\,s^3\,A^2}$
  flujo magnético                weber            $\mathrm{Wb}$         $\mathrm{kg\,m^2\,s^{-2}\,A^{-1}}$
  densidad de flujo magnético    tesla            $\mathrm T$           $\mathrm{kg\,s^{-2}\,A^{-1}}$
  inductancia                    henry            $\mathrm H$           $\mathrm{kg\,m^2\,s^{-2}\,A^{-2}}$
  temperatura Celsius            grado Celsius    $\mathrm{^\circ C}$   mismo tamaño de intervalo que $\mathrm K$
  flujo luminoso                 lumen            $\mathrm{lm}$         $\mathrm{cd\,sr}$
  iluminancia                    lux              $\mathrm{lx}$         $\mathrm{lm\,m^{-2}}$
  actividad de un radionúclido   becquerel        $\mathrm{Bq}$         $\mathrm{s^{-1}}$
  dosis absorbida                gray             $\mathrm{Gy}$         $\mathrm{m^2\,s^{-2}}$
  dosis equivalente              sievert          $\mathrm{Sv}$         $\mathrm{m^2\,s^{-2}}$
  actividad catalítica           katal            $\mathrm{kat}$        $\mathrm{mol\,s^{-1}}$

No necesitamos memorizar la tabla. Debemos reconocer su arquitectura.

[]{#misma-expresión-de-unidad-distinta-magnitud}

### Misma expresión de unidad, distinta magnitud {#fispm-c02-misma-expresiuxf3n-de-unidad-distinta-magnitud}

Tenemos: $\mathrm{Hz}=\mathrm{s^{-1}},$

pero también

$$\mathrm{Bq}=\mathrm{s^{-1}}.$$

Frecuencia y actividad de un radionúclido no son el mismo tipo de magnitud.

Análogamente, $\mathrm{Gy} = \mathrm{m^2\,s^{-2}},$

y

$$\mathrm{Sv} = \mathrm{m^2\,s^{-2}},$$

pero dosis absorbida y dosis equivalente no son la misma magnitud física.

Por tanto:

$$\boxed{ \text{misma expresión de unidad} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

Los nombres especiales pueden ayudar a conservar la distinción semántica.

[]{#energía-y-torque}

### Energía y torque {#fispm-c02-energuxeda-y-torque}

La unidad coherente de energía puede escribirse

$$\mathrm J=\mathrm{N\,m}.$$

El torque o momento de una fuerza también utiliza una unidad expresable como $\mathrm{N\,m}.$ Sin embargo, no se acostumbra llamar joule a la unidad de torque. La razón es semántica: `J` señala magnitudes como energía o trabajo, mientras que `N m` conserva visible una interpretación distinta.

Así,

$$\boxed{ \text{estructura dimensional} \neq \text{significado físico completo}. }$$

[]{#coherencia-no-significa-una-única-escritura}

### Coherencia no significa una única escritura {#fispm-c02-coherencia-no-significa-una-uxfanica-escritura}

Una misma unidad coherente puede escribirse, por ejemplo,

$$\mathrm{Pa} = \mathrm{N\,m^{-2}} = \mathrm{kg\,m^{-1}\,s^{-2}}.$$

Las tres expresiones representan la misma unidad coherente. La elección puede resaltar distintos aspectos de la estructura.

[]{#ejemplo-expandir-nombres-especiales}

### Ejemplo: expandir nombres especiales {#fispm-c02-ejemplo-expandir-nombres-especiales}

Como $\mathrm N = \mathrm{kg\,m\,s^{-2}},$

tenemos

$$\mathrm{Pa} = \mathrm{N\,m^{-2}} = \mathrm{kg\,m^{-1}\,s^{-2}}.$$

Además,

$$\mathrm J = \mathrm{N\,m} = \mathrm{kg\,m^2\,s^{-2}},$$

y

$$\mathrm W = \mathrm{J\,s^{-1}} = \mathrm{kg\,m^2\,s^{-3}}.$$

Los nombres especiales forman parte de la misma álgebra coherente.

[]{#conversión-de-densidad}

### Conversión de densidad {#fispm-c02-conversiuxf3n-de-densidad}

Calculemos

$$1\,\mathrm{g\,cm^{-3}}$$

en unidades coherentes SI.

Tenemos $1\,\mathrm g = 10^{-3}\,\mathrm{kg},$

y

$$1\,\mathrm{cm^3} = 10^{-6}\,\mathrm{m^3}.$$

Por tanto,

$$1\,\mathrm{g\,cm^{-3}} = \frac{10^{-3}\,\mathrm{kg}} {10^{-6}\,\mathrm{m^3}} = 10^3\,\mathrm{kg\,m^{-3}}.$$

Así,

$$\boxed{ 1\,\mathrm{g\,cm^{-3}} = 1000\,\mathrm{kg\,m^{-3}}. }$$

[]{#el-álgebra-de-unidades-no-elige-la-física}

### El álgebra de unidades no elige la física {#fispm-c02-el-uxe1lgebra-de-unidades-no-elige-la-fuxedsica}

Podemos formar matemáticamente

$$\frac{m}{t},$$

pero la teoría de unidades no decide por sí sola si esa combinación representa una magnitud relevante para el problema. Para eso necesitamos una definición, una ley, una hipótesis de modelo o alguna otra razón física.

Por tanto:

$$\boxed{ \text{álgebra de unidades} \neq \text{selección automática de variables físicas}. }$$

Esta limitación reaparecerá en el análisis dimensional.

[]{#ficha-de-construcción-de-una-unidad-derivada}

### Ficha de construcción de una unidad derivada {#fispm-c02-ficha-de-construcciuxf3n-de-una-unidad-derivada}

**Ficha FPM --- Construcción de una unidad derivada** 1. **Magnitud:** ¿qué cantidad estamos definiendo? 2. **Ecuación de magnitudes:** ¿qué relación la conecta con otras magnitudes? 3. **Tipos:** ¿qué tipos de magnitud intervienen? 4. **Unidades de entrada:** ¿qué unidades usamos? 5. **Álgebra:** ¿qué producto, cociente o potencia resulta? 6. **Factor:** ¿aparece un factor distinto de $1$? 7. **Coherencia:** ¿la unidad resultante es coherente en el SI? 8. **Nombre especial:** ¿existe uno? 9. **Semántica:** ¿otras magnitudes comparten la misma expresión? 10. **Modelo:** ¿qué justifica físicamente esta combinación?

[]{#ejercicios}

### Ejercicios {#fispm-c02-ejercicios}

**Ejercicio 8 --- Construir unidades derivadas coherentes** **Tipo:** análisis dimensional · **Nivel:** básico

Determina la unidad derivada coherente SI para:

1.  $A=xy$.

2.  $V=xyz$.

3.  $v=\ell/t$.

4.  $a=v/t$.

5.  $\rho=m/V$.

**Solución**

1.

$$\mathrm m\cdot\mathrm m = \boxed{\mathrm{m^2}}.$$

1.

$$\mathrm m^3 = \boxed{\mathrm{m^3}}.$$

1.

$$\frac{\mathrm m}{\mathrm s} = \boxed{\mathrm{m\,s^{-1}}}.$$

1.

$$\frac{\mathrm{m\,s^{-1}}}{\mathrm s} = \boxed{\mathrm{m\,s^{-2}}}.$$

1.

$$\frac{\mathrm{kg}}{\mathrm{m^3}} = \boxed{\mathrm{kg\,m^{-3}}}.$$

Todas se obtienen con factor $1$ respecto de las unidades base del SI.

**Ejercicio 9 --- Coherencia y factor de conversión** **Tipo:** cálculo · **Nivel:** central

Sea

$$\ell=750\,\mathrm{cm}, \qquad t=25\,\mathrm s.$$

1.  Calcula $v=\ell/t$ en $\mathrm{cm\,s^{-1}}$.

2.  Convierte el resultado a $\mathrm{m\,s^{-1}}$.

3.  Escribe la relación entre $\{v\}_{\mathrm{m\,s^{-1}}}$, $\{\ell\}_{\mathrm{cm}}$ y $\{t\}_{\mathrm s}$.

4.  Explica el factor de conversión.

**Solución**

1.

$$v = \frac{750\,\mathrm{cm}}{25\,\mathrm s} = 30\,\mathrm{cm\,s^{-1}}.$$

1.

$$30\,\mathrm{cm\,s^{-1}} = 30\times10^{-2}\,\mathrm{m\,s^{-1}} = \boxed{0.30\,\mathrm{m\,s^{-1}}}.$$

1.

$$\boxed{ \{v\}_{\mathrm{m\,s^{-1}}} = 10^{-2} \frac{\{\ell\}_{\mathrm{cm}}}{\{t\}_{\mathrm s}} }.$$

1.  El factor $10^{-2}$ aparece porque el centímetro introduce una escala distinta de la unidad base metro.

**Ejercicio 10 --- Nombres especiales, expansión y significado**

1.  Expande en unidades base:

$$\mathrm N,\qquad \mathrm{Pa},\qquad \mathrm J,\qquad \mathrm W.$$

1.  Demuestra:

$$\mathrm{Pa}=\mathrm{N\,m^{-2}}, \qquad \mathrm J=\mathrm{N\,m}.$$

1.  Explica por qué

$$\mathrm{Hz}=\mathrm{Bq}=\mathrm{s^{-1}}$$

no implica que frecuencia y actividad sean la misma magnitud.

1.  Convierte

$$2.5\,\mathrm{g\,cm^{-3}}$$

a $\mathrm{kg\,m^{-3}}$.

**Solución**

1.

$$\mathrm N = \boxed{\mathrm{kg\,m\,s^{-2}}},$$

$$\mathrm{Pa} = \boxed{\mathrm{kg\,m^{-1}\,s^{-2}}},$$

$$\mathrm J = \boxed{\mathrm{kg\,m^2\,s^{-2}}},$$

$$\mathrm W = \boxed{\mathrm{kg\,m^2\,s^{-3}}}.$$

1.

$$\mathrm{N\,m^{-2}} = \mathrm{kg\,m\,s^{-2}}\mathrm{m^{-2}} = \mathrm{kg\,m^{-1}\,s^{-2}} = \mathrm{Pa},$$

y

$$\mathrm{N\,m} = \mathrm{kg\,m^2\,s^{-2}} = \mathrm J.$$

1.  La igualdad algebraica de las expresiones de unidad no identifica el tipo de magnitud. `Hz` conserva la interpretación de frecuencia; `Bq` la de actividad.

2.

$$2.5\,\mathrm{g\,cm^{-3}} = 2.5\times10^3\,\mathrm{kg\,m^{-3}} = \boxed{2500\,\mathrm{kg\,m^{-3}}}.$$

[]{#síntesis-2}

### Síntesis {#fispm-c02-suxedntesis-2}

Las relaciones entre magnitudes generan relaciones entre unidades:

$$Q=Q_1Q_2 \quad\Rightarrow\quad u=u_1u_2,$$

$$Q=\frac{Q_1}{Q_2} \quad\Rightarrow\quad u=\frac{u_1}{u_2},$$

$$Q=Q_1^n \quad\Rightarrow\quad u=u_1^n.$$

Definimos magnitud derivada, unidad derivada y unidad derivada coherente.

La propiedad central es:

$$\boxed{ \text{coherencia} \Longrightarrow \text{misma forma de la ecuación para magnitudes y valores numéricos}. }$$

Pero conservamos dos límites:

$$\boxed{ \text{misma expresión de unidad} \not\Rightarrow \text{mismo tipo de magnitud} }$$

y

$$\boxed{ \text{álgebra de unidades} \not\Rightarrow \text{selección automática de las variables físicas correctas}. }$$

La siguiente sección construirá una estructura que no depende de la unidad concreta elegida (§[5](#fispm-c02-dimensiuxf3n-fuxedsica)).

[]{#dimensión-física}

[]{#fispm-t1-c02-s05}

[]{#fpm-i-02-s05}

## 5. Dimensión física {#fispm-c02-dimensiuxf3n-fuxedsica}

[]{#la-unidad-concreta-no-es-la-dimensión}

### La unidad concreta no es la dimensión {#fispm-c02-la-unidad-concreta-no-es-la-dimensiuxf3n}

En §4 vimos que una misma magnitud derivada puede expresarse mediante unidades diferentes. Una rapidez puede escribirse como $72\,\mathrm{km\,h^{-1}},$

o como $20\,\mathrm{m\,s^{-1}}.$

Los números son distintos y las unidades son distintas, pero la estructura física que relaciona longitud y tiempo es la misma.

Esto sugiere separar dos niveles:

$$\boxed{ \text{unidad} \neq \text{dimensión} }$$

La unidad especifica una referencia concreta de medida. La dimensión registra cómo una magnitud depende, dentro de un sistema de magnitudes, de las magnitudes tomadas como base. Así, $\mathrm{m\,s^{-1}}$

[]{#fig:I-02-R02}

<figure id="fig-fpm-v04-i-02-r02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R02.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R02.svg" alt="La dimensión fija una escala, no una función. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="177" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.3.** Para un péndulo ideal, el análisis de dimensiones permite escribir $T=\sqrt{\ell/g}\,\Phi(\theta_0)$. No determina la función de la amplitud. En oscilaciones pequeñas, la dinámica da $\Phi(0)=2\pi$. Véase §[5](#fispm-c02-dimensiuxf3n-fuxedsica).

</figcaption>

</figure>

y

$$\mathrm{km\,h^{-1}}$$

son unidades diferentes, pero ambas representan magnitudes con la misma estructura dimensional: $LT^{-1}.$ Esta separación será la base del análisis dimensional.

[]{#dimensión-de-una-magnitud}

### Dimensión de una magnitud {#fispm-c02-dimensiuxf3n-de-una-magnitud}

El Vocabulario Internacional de Metrología define la dimensión de una magnitud como la expresión de su dependencia respecto de las magnitudes base de un sistema mediante un producto de potencias, omitiendo cualquier factor numérico.[^19]

**Definición 14 --- Dimensión de una magnitud** La **dimensión** de una magnitud $Q$, respecto de un sistema elegido de magnitudes base, es la expresión simbólica que registra su dependencia respecto de esas magnitudes base como producto de potencias, sin incluir factores numéricos.

Usaremos la notación

$$[Q]$$

para la dimensión de $Q$. La documentación metrológica suele escribir también

$$\dim Q.$$

Ambas notaciones expresan la misma idea; en este libro utilizaremos preferentemente corchetes porque resultan compactos en los cálculos.

[]{#las-siete-dimensiones-base-del-si}

### Las siete dimensiones base del SI {#fispm-c02-las-siete-dimensiones-base-del-si}

El SI organiza las magnitudes físicas mediante siete magnitudes base. A cada una se asocia convencionalmente un símbolo dimensional.[^20]

  Magnitud base               Símbolo dimensional
  --------------------------- ---------------------
  tiempo                      $T$
  longitud                    $L$
  masa                        $M$
  corriente eléctrica         $I$
  temperatura termodinámica   $\Theta$
  cantidad de sustancia       $N$
  intensidad luminosa         $J$

Debemos leer estos símbolos con cuidado.

Por ejemplo:

- $T$ como dimensión significa **tiempo**;

- $\Theta$ significa **temperatura termodinámica**;

- $J$ como dimensión significa **intensidad luminosa** y no debe confundirse con el símbolo $\mathrm J$ del joule.

Los símbolos dimensionales no son unidades. Por tanto,

$$L \neq \mathrm m,$$

$$T \neq \mathrm s,$$

$$M \neq \mathrm{kg}.$$

El lado izquierdo representa una dimensión; el lado derecho, una unidad concreta.

**Principio 9 --- La dimensión es independiente de la unidad particular** Cambiar la unidad utilizada para expresar una magnitud puede cambiar su valor numérico y el símbolo de unidad, pero no cambia su dimensión dentro del sistema de magnitudes fijado.

[]{#el-producto-dimensional-general}

### El producto dimensional general {#fispm-c02-el-producto-dimensional-general}

En el sistema dimensional utilizado por el SI, una magnitud $Q$ puede representarse dimensionalmente mediante

$$\boxed{ [Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta }$$

donde los exponentes

$$\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta$$

son los **exponentes dimensionales** de $Q$ respecto de la base elegida.

**Definición 15 --- Exponente dimensional** Un **exponente dimensional** es el exponente con el que aparece una dimensión base en la expresión dimensional de una magnitud.

Por ejemplo, para una velocidad, $[v]=LT^{-1}.$

Podemos escribirla en la forma completa: $[v] = T^{-1} L^1 M^0 I^0 \Theta^0 N^0 J^0.$ Por tanto, sus exponentes dimensionales son $(-1,1,0,0,0,0,0)$

si usamos el orden

$$(T,L,M,I,\Theta,N,J).$$

Esta representación como lista de exponentes será útil más adelante en el teorema $\Pi$ de Buckingham.

[]{#producto-cociente-y-potencia-de-dimensiones}

### Producto, cociente y potencia de dimensiones {#fispm-c02-producto-cociente-y-potencia-de-dimensiones}

Las operaciones dimensionales siguen la estructura algebraica de las magnitudes.

Si

$$Q=Q_1Q_2,$$

entonces $[Q]=[Q_1][Q_2].$

Si

$$Q=\frac{Q_1}{Q_2},$$

entonces $[Q] = \frac{[Q_1]}{[Q_2]}.$ Y si

$$Q=Q_1^n,$$

entonces $[Q]=[Q_1]^n.$

No estamos manipulando unidades concretas.

Estamos manipulando la dependencia estructural respecto de las magnitudes base.

[]{#área-y-volumen}

### Área y volumen {#fispm-c02-uxe1rea-y-volumen}

Si

$$A=xy,$$

con

$$[x]=L$$

y

$$[y]=L,$$

entonces $[A] = [x][y] = L^2.$ Por tanto,

$$\boxed{ [A]=L^2. }$$

Análogamente, si

$$V=xyz,$$

entonces $[V] = L^3.$ Por eso metro cuadrado, centímetro cuadrado y kilómetro cuadrado son unidades distintas de magnitudes cuya dimensión es $L^2.$

[]{#rapidez-y-velocidad}

### Rapidez y velocidad {#fispm-c02-rapidez-y-velocidad}

Para una relación elemental

$$v=\frac{\ell}{t},$$

tenemos $[\ell]=L$

y

$$[t]=T.$$

Entonces $[v] = \frac{L}{T} = LT^{-1}.$

Así,

$$\boxed{ [v]=LT^{-1}. }$$

Esta expresión no contiene metro, kilómetro, segundo ni hora. Por eso vale igualmente si la velocidad se expresa en

$$\mathrm{m\,s^{-1}},$$

$$\mathrm{km\,h^{-1}},$$

o cualquier otra unidad compatible.

[]{#aceleración}

### Aceleración {#fispm-c02-aceleraciuxf3n}

Si una aceleración se modela como cambio de velocidad por intervalo de tiempo, $a=\frac{\Delta v}{\Delta t},$

entonces $[a] = \frac{[v]}{[t]}.$

Como $[v]=LT^{-1}$

y

$$[t]=T,$$

obtenemos $[a] = LT^{-2}.$ Por tanto,

$$\boxed{ [a]=LT^{-2}. }$$

[]{#densidad-de-masa-1}

### Densidad de masa {#fispm-c02-densidad-de-masa-1}

Para

$$\rho=\frac{m}{V},$$

tenemos $[m]=M$

y

$$[V]=L^3.$$

Luego

$$[\rho] = \frac{M}{L^3} = ML^{-3}.$$

Así,

$$\boxed{ [\rho]=ML^{-3}. }$$

Las unidades

$$\mathrm{kg\,m^{-3}}$$

y

$$\mathrm{g\,cm^{-3}}$$

son diferentes, pero comparten esta misma dimensión.

[]{#algunas-dimensiones-frecuentes}

### Algunas dimensiones frecuentes {#fispm-c02-algunas-dimensiones-frecuentes}

A partir de las relaciones físicas que las definen dentro del modelo correspondiente podemos obtener:

  Magnitud                  Relación elemental   Dimensión
  ------------------------- -------------------- -----------------
  área                      $A=xy$               $L^2$
  volumen                   $V=xyz$              $L^3$
  velocidad                 $v=\ell/t$           $LT^{-1}$
  aceleración               $a=v/t$              $LT^{-2}$
  densidad de masa          $\rho=m/V$           $ML^{-3}$
  frecuencia                $f=1/t$              $T^{-1}$
  fuerza                    $F=ma$               $MLT^{-2}$
  energía mecánica típica   $E=F\ell$            $ML^2T^{-2}$
  potencia                  $P=E/t$              $ML^2T^{-3}$
  presión                   $p=F/A$              $ML^{-1}T^{-2}$
  carga eléctrica           $q=It$               $IT$

Esta tabla no debe memorizarse como una lista arbitraria.

Cada entrada se reconstruye a partir de una relación entre magnitudes.

[]{#la-dimensión-no-es-una-unidad-abreviada}

### La dimensión no es una unidad abreviada {#fispm-c02-la-dimensiuxf3n-no-es-una-unidad-abreviada}

Es tentador pensar:

> «$LT^{-1}$ es una manera abstracta de escribir $\mathrm{m\,s^{-1}}$.»

La frase es incompleta. La dimensión

$$LT^{-1}$$

no selecciona una unidad concreta.

Muchas unidades pueden corresponder a esa dimensión:

$$\mathrm{m\,s^{-1}},$$

$$\mathrm{km\,h^{-1}},$$

$$\mathrm{cm\,s^{-1}},$$

etc.

La relación correcta es:

$$\boxed{ \text{una dimensión} \longrightarrow \text{muchas unidades posibles} }$$

mientras que un sistema coherente selecciona una forma privilegiada de construir unidades a partir de su base.

[]{#cambiar-unidades-no-cambia-exponentes-dimensionales}

### Cambiar unidades no cambia exponentes dimensionales {#fispm-c02-cambiar-unidades-no-cambia-exponentes-dimensionales}

Consideremos una velocidad. En SI: $v=q\,\mathrm{m\,s^{-1}}.$

Podemos cambiar las unidades base de longitud y tiempo:

$$\mathrm{m} \longrightarrow \mathrm{cm},$$

$$\mathrm{s} \longrightarrow \mathrm{min}.$$

El valor numérico de $v$ cambia. La unidad cambia.

Pero la relación estructural sigue siendo:

$$\text{longitud}/\text{tiempo}.$$

Por tanto, $[v]=LT^{-1}$

antes y después del cambio. Lo mismo ocurre para cualquier magnitud cuya dimensión sea

$$[Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta.$$

Un cambio de las unidades concretas asociadas a las magnitudes base altera factores numéricos, pero no los exponentes

$$\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta.$$

Ésta es la razón algebraica del Principio 9.

[]{#una-demostración-elemental-de-la-invariancia}

### Una demostración elemental de la invariancia {#fispm-c02-una-demostraciuxf3n-elemental-de-la-invariancia}

Supongamos, para simplificar, que una magnitud depende solo de longitud y tiempo y tiene la forma $Q=C\,\ell^\beta t^\alpha,$

donde $C$ es un factor numérico que no introduce dimensión adicional.

Sean las unidades originales

$$u_L, \qquad u_T,$$

y nuevas unidades

$$u_L'=\lambda_Lu_L,$$

$$u_T'=\lambda_Tu_T,$$

con

$$\lambda_L>0, \qquad \lambda_T>0.$$

Por la Proposición 1, los valores numéricos de longitud y tiempo cambian inversamente:

$$\{\ell\}_{u_L'} = \frac{\{\ell\}_{u_L}}{\lambda_L},$$

$$\{t\}_{u_T'} = \frac{\{t\}_{u_T}}{\lambda_T}.$$

Entonces el valor numérico de $Q$ adquiere factores

$$\lambda_L^{-\beta} \lambda_T^{-\alpha}.$$

Cambian los números. Pero la forma de dependencia continúa siendo

$$L^\beta T^\alpha.$$

Por tanto, los exponentes dimensionales no dependen del tamaño concreto de las unidades elegidas. No elevaremos este resultado a una nueva proposición numerada porque su función aquí es preparar la Proposición 2, que en §6 formalizará una consecuencia más fuerte: la homogeneidad dimensional necesaria de las ecuaciones físicas.

[]{#misma-dimensión-no-significa-mismo-tipo-de-magnitud}

### Misma dimensión no significa mismo tipo de magnitud {#fispm-c02-misma-dimensiuxf3n-no-significa-mismo-tipo-de-magnitud}

En §2 aprendimos que la comparabilidad física es más exigente que compartir una notación de unidad. Ahora podemos formular la versión dimensional de esa cautela.

El VIM establece:

- magnitudes del mismo tipo tienen la misma dimensión;

- magnitudes con dimensiones diferentes son necesariamente de tipos distintos;

- magnitudes con la misma dimensión no son necesariamente del mismo tipo.[^21]

Por tanto,

$$\boxed{ \text{mismo tipo} \Longrightarrow \text{misma dimensión} }$$

pero no:

$$\boxed{ \text{misma dimensión} \Longrightarrow \text{mismo tipo}. }$$

**Principio 10 --- La igualdad dimensional no identifica el significado físico** Que dos magnitudes posean la misma dimensión es una condición estructural importante, pero no basta para concluir que pertenecen al mismo tipo de magnitud ni que son físicamente intercambiables.

[]{#ejemplo-frecuencia-y-actividad-radionúclida}

### Ejemplo: frecuencia y actividad radionúclida {#fispm-c02-ejemplo-frecuencia-y-actividad-radionuxfaclida}

En ambos casos aparece

$$T^{-1}.$$

Para frecuencia, $[f]=T^{-1}.$ Para actividad radionúclida, $[A]=T^{-1}.$

Sin embargo, el SI utiliza nombres especiales distintos:

$$1\,\mathrm{Hz}=1\,\mathrm{s^{-1}},$$

$$1\,\mathrm{Bq}=1\,\mathrm{s^{-1}}.$$

La igualdad dimensional no borra la diferencia física entre frecuencia y número de desintegraciones por unidad de tiempo.

[]{#ejemplo-presión-y-densidad-de-energía}

### Ejemplo: presión y densidad de energía {#fispm-c02-ejemplo-presiuxf3n-y-densidad-de-energuxeda}

Para presión, $p=\frac{F}{A}.$

Como $[F]=MLT^{-2}$

y

$$[A]=L^2,$$

tenemos $[p] = ML^{-1}T^{-2}.$ Ahora consideremos una densidad de energía

$$u=\frac{E}{V}.$$

Como $[E]=ML^2T^{-2}$

y

$$[V]=L^3,$$

obtenemos $[u] = ML^{-1}T^{-2}.$ Por tanto, $[p]=[u].$ Pero esto no demuestra que presión y densidad de energía sean la misma magnitud. Solo demuestra que ocupan la misma posición en el sistema dimensional.

[]{#dimensión-y-forma-vectorial}

### Dimensión y forma vectorial {#fispm-c02-dimensiuxf3n-y-forma-vectorial}

El VIM señala además que, al obtener la dimensión de una magnitud, no se toma en cuenta su carácter escalar, vectorial o tensorial.[^22]

Esto será importante más adelante.

Dos objetos matemáticos con naturaleza geométrica distinta pueden compartir dimensión. Por ejemplo, una posición y un desplazamiento vectorial pueden poseer dimensión

$$L,$$

aunque su estructura matemática no sea la de un escalar arbitrario.

Por tanto:

$$\boxed{ \text{dimensión} \neq \text{estructura matemática completa de la magnitud}. }$$

El análisis dimensional conserva cierta información y descarta otra.

[]{#la-dimensión-depende-del-sistema-de-magnitudes}

### La dimensión depende del sistema de magnitudes {#fispm-c02-la-dimensiuxf3n-depende-del-sistema-de-magnitudes}

También debemos evitar presentar la dimensión como una etiqueta metafísica adherida a cada magnitud de manera independiente de toda elección. El BIPM y el VIM hablan de dimensiones **respecto de un sistema de magnitudes**. La elección de magnitudes base es convencional.

Una vez fijada la base, la expresión dimensional de las magnitudes derivadas queda determinada por las relaciones adoptadas en ese sistema.

Así:

$$\boxed{ \text{dimensión} = \text{estructura relativa a un sistema de magnitudes} }$$

aunque, una vez fijado el sistema, resulte extremadamente estable y útil.

**Definición 16 --- Sistema de dimensiones** Un **sistema de dimensiones** es la organización de las magnitudes de un sistema mediante dimensiones base elegidas y expresiones dimensionales derivadas construidas como productos de potencias de esas dimensiones base.

En el SI trabajaremos con la base

$$(T,L,M,I,\Theta,N,J).$$

[]{#zorich-y-el-cambio-de-base-de-unidades}

### Zorich y el cambio de base de unidades {#fispm-c02-zorich-y-el-cambio-de-base-de-unidades}

Zorich organiza su teoría dimensional precisamente alrededor del cambio de tamaños de las unidades base y de la manera en que cambian los valores numéricos de las magnitudes mientras se conserva su estructura dimensional.[^23]

Esta perspectiva es especialmente adecuada para nuestro proyecto porque conecta directamente con la Proposición 1.

La secuencia conceptual es:

$$\boxed{ \text{magnitud} \longrightarrow \text{elección de unidades} \longrightarrow \text{valores numéricos} }$$

y, al cambiar las unidades,

$$\boxed{ \text{cambian los números} \quad\text{pero no}\quad \text{la dependencia dimensional}. }$$

En §6 usaremos exactamente esta invariancia para detectar qué sumas e igualdades pueden conservar significado físico bajo cambios de escala de las unidades base.

[]{#ejercicios-1}

### Ejercicios {#fispm-c02-ejercicios-1}

**Ejercicio 11 --- Reconstruir dimensiones**

**Tipo:** análisis dimensional · **Nivel:** básico

Calcula las dimensiones de:

1.  área;

2.  volumen;

3.  velocidad;

4.  aceleración;

5.  densidad de masa;

6.  fuerza, usando $F=ma$;

7.  energía, usando $E=F\ell$;

8.  potencia, usando $P=E/t$;

9.  presión, usando $p=F/A$.

No uses una tabla memorizada: deriva cada resultado.

**Solución**

1.  Para área:

$$[A]=L\cdot L=L^2.$$

1.  Para volumen:

$$[V]=L^3.$$

1.  Para velocidad:

$$[v]=\frac{L}{T}=LT^{-1}.$$

1.  Para aceleración:

$$[a] = \frac{LT^{-1}}{T} = LT^{-2}.$$

1.  Para densidad:

$$[\rho] = \frac{M}{L^3} = ML^{-3}.$$

1.  Para fuerza:

$$[F] = [m][a] = MLT^{-2}.$$

1.  Para energía:

$$[E] = [F]L = ML^2T^{-2}.$$

1.  Para potencia:

$$[P] = \frac{[E]}{T} = ML^2T^{-3}.$$

1.  Para presión:

$$[p] = \frac{[F]}{[A]} = \frac{MLT^{-2}}{L^2} = ML^{-1}T^{-2}.$$

El procedimiento es siempre el mismo:

$$\boxed{ \text{relación entre magnitudes} \longrightarrow \text{relación entre dimensiones}. }$$

**Ejercicio 12 --- Cambiar unidades sin cambiar dimensión**

Una rapidez vale $v=90\,\mathrm{km\,h^{-1}}.$

1.  Exprésala en $\mathrm{m\,s^{-1}}$.

2.  Escribe su dimensión antes y después de la conversión.

3.  Explica por qué el cambio de valor numérico no modifica los exponentes dimensionales.

4.  Repite el argumento de manera simbólica si

$$u_L'=\lambda_Lu_L, \qquad u_T'=\lambda_Tu_T.$$

**Solución**

Como $1\,\mathrm{km}=10^3\,\mathrm m$

y

$$1\,\mathrm h=3600\,\mathrm s,$$

tenemos

$$90\,\mathrm{km\,h^{-1}} = 90\frac{10^3\,\mathrm m}{3600\,\mathrm s}.$$

Por tanto, $v=25\,\mathrm{m\,s^{-1}}.$ El valor numérico cambió: $90\longrightarrow25.$

La unidad cambió:

$$\mathrm{km\,h^{-1}} \longrightarrow \mathrm{m\,s^{-1}}.$$

Pero en ambos casos

$$[v]=LT^{-1}.$$

En forma simbólica, si

$$u_L'=\lambda_Lu_L$$

y

$$u_T'=\lambda_Tu_T,$$

entonces los valores numéricos de longitud y tiempo adquieren factores inversos:

$$\ell'\sim\lambda_L^{-1}\ell,$$

$$t'\sim\lambda_T^{-1}t.$$

Por ello la rapidez numérica adquiere el factor

$$\lambda_L^{-1}\lambda_T,$$

pero la estructura de dependencia continúa siendo

$$L^1T^{-1}.$$

Los factores de conversión afectan números; los exponentes dimensionales registran la estructura y permanecen iguales.

**Ejercicio 13 --- Misma dimensión, distinto significado**

Considera los pares:

1.  frecuencia y actividad radionúclida;

2.  presión y densidad de energía;

3.  longitud de una barra y longitud de onda;

4.  masa y tiempo.

Para cada par:

1.  determina si las dimensiones son iguales;

2.  decide si la igualdad dimensional basta para afirmar que son magnitudes del mismo tipo;

3.  explica qué conclusión es legítima.

**Solución**

**1. Frecuencia y actividad radionúclida**

Ambas tienen

$$T^{-1}.$$

Sin embargo, no son del mismo tipo de magnitud.

La conclusión legítima es:

$$\boxed{ \text{misma dimensión, distinto significado físico}. }$$

**2. Presión y densidad de energía**

Para presión: $[p]=ML^{-1}T^{-2}.$

Para densidad de energía:

$$\left[\frac{E}{V}\right] = \frac{ML^2T^{-2}}{L^3} = ML^{-1}T^{-2}.$$

Las dimensiones coinciden.

Esto no demuestra que ambas magnitudes sean del mismo tipo.

**3. Longitud de una barra y longitud de onda**

Ambas pertenecen al tipo longitud y tienen

$$L.$$

Aquí la igualdad dimensional es compatible con que sean del mismo tipo. Pero no es la igualdad dimensional por sí sola la que establece esa clasificación: necesitamos además la interpretación física.

**4. Masa y tiempo**

Tenemos

$$[m]=M,$$

$$[t]=T.$$

Como las dimensiones son diferentes, necesariamente se trata de tipos de magnitud distintos.

En conjunto:

$$\boxed{ \text{dimensiones diferentes} \Longrightarrow \text{tipos diferentes}, }$$

pero

$$\boxed{ \text{dimensiones iguales} \not\Longrightarrow \text{mismo tipo}. }$$

[]{#síntesis-3}

### Síntesis {#fispm-c02-suxedntesis-3}

La sección introduce la abstracción decisiva:

$$\boxed{ \text{unidad concreta} \longrightarrow \text{dimensión} }$$

La dimensión de una magnitud se expresa, respecto de la base dimensional del SI, como

$$\boxed{ [Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta. }$$

Los exponentes describen la estructura dimensional y no dependen del tamaño de las unidades concretas elegidas.

Por eso:

$$\boxed{ \text{cambiar unidad} \not\Rightarrow \text{cambiar dimensión}. }$$

Y debemos conservar otra cautela:

$$\boxed{ \text{misma dimensión} \not\Rightarrow \text{mismo tipo de magnitud}. }$$

Con este lenguaje ya podemos formular la siguiente pregunta.

Si una ecuación física debe seguir teniendo sentido cuando cambiamos las unidades base, ¿qué restricciones impone eso a los términos que sumamos o igualamos?

Ése será el objeto de (§[6](#fispm-c02-homogeneidad-dimensional)).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes label="fispm-c02-notas-y-fuentes"}

[]{#homogeneidad-dimensional}

## 6. Homogeneidad dimensional {#fispm-c02-homogeneidad-dimensional}

[]{#una-igualdad-física-debe-sobrevivir-al-cambio-de-unidades}

### Una igualdad física debe sobrevivir al cambio de unidades {#fispm-c02-una-igualdad-fuxedsica-debe-sobrevivir-al-cambio-de-unidades}

En §5 vimos que una magnitud conserva su dimensión cuando cambiamos las unidades concretas con que expresamos sus magnitudes base.[^24]

[]{#fig:I-02-N02}

<figure id="fig-fpm-v04-i-02-n02" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-N02.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-N02.svg" alt="Dimensiones de las derivadas. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="535" height="111" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.4.** La posición, su primera derivada y su segunda derivada pertenecen a clases dimensionales distintas. Una suma exige homogeneidad de sus términos. Véase §[6](#fispm-c02-homogeneidad-dimensional).

</figcaption>

</figure>

Por ejemplo, $[v]=LT^{-1}$

tanto si escribimos una velocidad en

$$\mathrm{m\,s^{-1}}$$

como si la escribimos en

$$\mathrm{km\,h^{-1}}.$$

Ahora preguntaremos qué ocurre con una **ecuación física completa**.

Consideremos

$$x=x_0+vt.$$

Dimensionalmente,

$$[x]=L,$$

$$[x_0]=L,$$

y

$$[vt] = [v][t] = LT^{-1}T = L.$$

Todos los términos poseen dimensión $L$. En cambio, si alguien escribiera

$$x=x_0+vt^2,$$

tendríamos

$$[vt^2] = LT^{-1}T^2 = LT.$$

La suma intentaría combinar:

$$L$$

con

$$LT.$$

El problema aparece antes de sustituir números. La expresión no conserva una interpretación física coherente bajo cambios de unidades.

[]{#homogeneidad-dimensional-1}

[]{#fispm-t1-c02-s06}

[]{#fpm-i-02-s06}

### Homogeneidad dimensional {#fispm-c02-homogeneidad-dimensional-1}

**Definición 17 --- Ecuación dimensionalmente homogénea** Una ecuación física es **dimensionalmente homogénea** cuando todos los términos que se suman o se igualan poseen la misma dimensión, una vez incorporadas las dimensiones de todos los parámetros y constantes físicas que aparecen en ellos.

Por ejemplo, $x=x_0+vt$

es dimensionalmente homogénea porque

$$[x]=[x_0]=[vt]=L.$$

La expresión

$$x=x_0+vt^2$$

no lo es porque

$$[x]=[x_0]=L$$

mientras

$$[vt^2]=LT.$$

La homogeneidad dimensional es una condición estructural sobre la ecuación. No depende de los valores numéricos particulares que sustituyamos.[^25]

[]{#sumar-magnitudes-exige-compatibilidad}

### Sumar magnitudes exige compatibilidad {#fispm-c02-sumar-magnitudes-exige-compatibilidad}

En §2 distinguimos **tipo de magnitud** y **dimensión**.

Dos magnitudes del mismo tipo tienen la misma dimensión.[^26]

La recíproca, como vimos en §5, no es cierta.

Esto nos obliga a formular dos niveles de control.

[]{#nivel-1-condición-dimensional}

#### Nivel 1 --- Condición dimensional {#fispm-c02-nivel-1-condiciuxf3n-dimensional}

Para que una suma física

$$A+B$$

pueda tener sentido, es necesario que

$$[A]=[B].$$

[]{#nivel-2-compatibilidad-física}

#### Nivel 2 --- Compatibilidad física {#fispm-c02-nivel-2-compatibilidad-fuxedsica}

La igualdad dimensional no basta por sí sola.

También debemos saber que $A$ y $B$ representan magnitudes que el modelo permite combinar mediante esa operación. Por ejemplo, presión y densidad de energía tienen la misma dimensión: $ML^{-1}T^{-2}.$ Pero la igualdad dimensional por sí sola no autoriza cualquier suma entre ambas fuera de una relación física que le otorgue significado.

**Principio 11 --- La homogeneidad dimensional es necesaria para la suma física** Los términos que se suman o se comparan mediante una igualdad física deben poseer dimensiones compatibles. Si sus dimensiones difieren, la ecuación no puede representar una relación física independiente de la elección de unidades.

[]{#de-la-dimensión-al-factor-de-reescalado}

### De la dimensión al factor de reescalado {#fispm-c02-de-la-dimensiuxf3n-al-factor-de-reescalado}

En §5 escribimos

$$[Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta.$$

Supongamos ahora que cambiamos independientemente los tamaños de las siete unidades base:

$$u_T'=\lambda_Tu_T,$$

$$u_L'=\lambda_Lu_L,$$

$$u_M'=\lambda_Mu_M,$$

$$u_I'=\lambda_Iu_I,$$

$$u_\Theta'=\lambda_\Theta u_\Theta,$$

$$u_N'=\lambda_Nu_N,$$

$$u_J'=\lambda_Ju_J,$$

con todos los factores positivos. Por la Proposición 1, el valor numérico de una magnitud base cambia de manera inversa al tamaño de su unidad. Por tanto, una magnitud con dimensión

$$T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta$$

adquiere el factor numérico

$$\lambda_T^{-\alpha} \lambda_L^{-\beta} \lambda_M^{-\gamma} \lambda_I^{-\delta} \lambda_\Theta^{-\varepsilon} \lambda_N^{-\zeta} \lambda_J^{-\eta}.$$

Definiremos, solo como notación auxiliar,

$$\chi_Q(\lambda) = \lambda_T^{-\alpha} \lambda_L^{-\beta} \lambda_M^{-\gamma} \lambda_I^{-\delta} \lambda_\Theta^{-\varepsilon} \lambda_N^{-\zeta} \lambda_J^{-\eta}.$$

Entonces, bajo el cambio de unidades, $\{Q\}' = \chi_Q(\lambda)\{Q\}.$ La función $\chi_Q$ codifica cómo cambia el **valor numérico** de $Q$ al reescalar las unidades base. No es una nueva magnitud física. Es una herramienta algebraica para la demostración.

[]{#por-qué-una-suma-obliga-a-un-mismo-factor}

### Por qué una suma obliga a un mismo factor {#fispm-c02-por-quuxe9-una-suma-obliga-a-un-mismo-factor}

Consideremos una relación física

$$A+B=C.$$

En cierto sistema de unidades, sus valores numéricos satisfacen

$$a+b=c.$$

Después de reescalar las unidades base, obtendríamos

$$\chi_A a + \chi_B b = \chi_C c.$$

Como $c=a+b,$

la ecuación transformada es $\chi_A a + \chi_B b = \chi_C(a+b).$

Reordenando: $(\chi_A-\chi_C)a + (\chi_B-\chi_C)b = 0.$ Si la relación física pretende ser una ley y no una coincidencia numérica para un único par especial $(a,b)$, debe mantener su forma para las realizaciones admisibles del modelo. En particular, si $a$ y $b$ pueden variar independientemente dentro de una familia no degenerada de realizaciones, la igualdad anterior solo puede mantenerse para todas ellas si

$$\chi_A=\chi_C$$

y

$$\chi_B=\chi_C.$$

Por tanto, $\chi_A=\chi_B=\chi_C.$ La suma exige que todos sus términos transformen de la misma manera al cambiar las unidades.

[]{#igualdad-de-factores-implica-igualdad-de-exponentes}

### Igualdad de factores implica igualdad de exponentes {#fispm-c02-igualdad-de-factores-implica-igualdad-de-exponentes}

Supongamos ahora que

$$\chi_A(\lambda)=\chi_B(\lambda)$$

para **todo** cambio independiente de unidades base.

Escribamos

$$[A] = T^{\alpha_A} L^{\beta_A} M^{\gamma_A} I^{\delta_A} \Theta^{\varepsilon_A} N^{\zeta_A} J^{\eta_A},$$

y

$$[B] = T^{\alpha_B} L^{\beta_B} M^{\gamma_B} I^{\delta_B} \Theta^{\varepsilon_B} N^{\zeta_B} J^{\eta_B}.$$

Entonces

$$\lambda_T^{-\alpha_A} \lambda_L^{-\beta_A} \cdots \lambda_J^{-\eta_A} = \lambda_T^{-\alpha_B} \lambda_L^{-\beta_B} \cdots \lambda_J^{-\eta_B}$$

para todo conjunto de factores positivos.

Mantengamos todas las $\lambda$ iguales a $1$ salvo $\lambda_T$.

Obtenemos $\lambda_T^{-\alpha_A} = \lambda_T^{-\alpha_B}$

para todo

$$\lambda_T>0.$$

Por tanto, $\alpha_A=\alpha_B.$

Repitiendo el argumento una dimensión base a la vez,

$$\beta_A=\beta_B,$$

$$\gamma_A=\gamma_B,$$

$$\delta_A=\delta_B,$$

$$\varepsilon_A=\varepsilon_B,$$

$$\zeta_A=\zeta_B,$$

$$\eta_A=\eta_B.$$

Luego

$$[A]=[B].$$

Esta observación completa la idea necesaria para nuestro segundo resultado formal.

[]{#segunda-proposición-formal-del-capítulo}

### Segunda proposición formal del capítulo {#fispm-c02-segunda-proposiciuxf3n-formal-del-capuxedtulo}

**Proposición 2 --- Homogeneidad dimensional necesaria bajo cambios independientes de unidades base**

Considérese una relación física de la forma $Q_1+\cdots+Q_r = R_1+\cdots+R_s,$

donde cada término tiene una dimensión bien definida respecto de un sistema de magnitudes base.

Supongamos:

1.  que la relación representa una ley o familia de realizaciones no degenerada, y no una igualdad numérica accidental;

2.  que su forma numérica debe conservarse bajo cambios multiplicativos independientes de las unidades base;

3.  que existe una realización de la relación en la cual podemos variar cualquier par de términos, manteniendo los restantes fijos, de modo que la igualdad siga siendo válida: si ambos términos están en el mismo miembro, sus variaciones numéricas son $h$ y $-h$; si están en miembros distintos, ambas son $h$. Para cada par se admiten valores no nulos de $h$ suficientemente pequeños.

Entonces todos los términos que participan aditivamente deben poseer la misma dimensión:

$$[Q_1] = \cdots = [Q_r] = [R_1] = \cdots = [R_s].$$

[]{#demostración-1}

#### Demostración {#fispm-c02-demostraciuxf3n-1}

Fijemos un sistema inicial de unidades y llamemos $z_1,\ldots,z_{r+s}$ a los valores numéricos de todos los términos, tomando con signo negativo los del segundo miembro. La relación se escribe entonces $\sum_{i=1}^{r+s}z_i=0.$ Un cambio multiplicativo de las unidades base multiplica cada valor numérico por un factor positivo $\chi_i$, determinado por la dimensión del término. La invariancia de forma exige, para cada realización de la familia, $\sum_{i=1}^{r+s}\chi_i z_i=0.$

Tomemos dos índices distintos $i,j$. La tercera hipótesis permite cambiar los valores firmados a $z_i+h$ y $z_j-h$, con $h\ne0$, sin alterar los restantes. La relación reescalada vale tanto antes como después de esa variación. Restar ambas igualdades da $h(\chi_i-\chi_j)=0.$

Por tanto $\chi_i=\chi_j$. Como el par era arbitrario, todos los términos tienen el mismo factor de reescalado para cada elección de unidades. Al variar una sola unidad base por un factor positivo arbitrario, la igualdad de sus potencias obliga a que coincidan los exponentes dimensionales correspondientes. Repetirlo con cada unidad base prueba

$$[Q_1]=\cdots=[Q_r]=[R_1]=\cdots=[R_s].$$

La hipótesis de variación excluye, por ejemplo, una suma de dos identidades independientes escritas juntas, cuyos términos podrían cancelarse por grupos de dimensiones distintas. La independencia respecto de las unidades, sin esa condición adicional, no bastaría para la conclusión sobre todos los sumandos. $\square$

[]{#qué-demuestra-exactamente-la-proposición-2}

### Qué demuestra exactamente la Proposición 2 {#fispm-c02-quuxe9-demuestra-exactamente-la-proposiciuxf3n-2}

La Proposición 2 establece una **condición necesaria** para una ecuación física aditiva que deba conservar su forma bajo cambios de unidades. No demuestra que toda ecuación dimensionalmente homogénea sea físicamente correcta. Por ejemplo, $x=x_0+vt$

y

$$x=x_0+2vt$$

son ambas dimensionalmente homogéneas.

También lo es $x=x_0-17vt.$ La dimensión no decide cuál, si alguna, describe un sistema físico concreto.

Por tanto:

$$\boxed{ \text{homogeneidad dimensional} \not\Rightarrow \text{verdad física}. }$$

**Principio 12 --- Pasar el control dimensional no prueba una ley** La homogeneidad dimensional es una condición necesaria de consistencia para una amplia clase de ecuaciones físicas, pero no constituye una demostración de su corrección empírica, de su interpretación ni de su dominio de validez.

[]{#un-error-dimensional-sí-puede-ser-decisivo}

### Un error dimensional sí puede ser decisivo {#fispm-c02-un-error-dimensional-suxed-puede-ser-decisivo}

La asimetría es importante. Si una ecuación falla el control dimensional, entonces tenemos una razón estructural para rechazarla **tal como está escrita**. Si una ecuación pasa el control dimensional, solo sabemos que ha superado una prueba necesaria.

En símbolos:

$$\boxed{ \text{inhomogeneidad} \Longrightarrow \text{ecuación físicamente inadmisible tal como está escrita}, }$$

mientras que

$$\boxed{ \text{homogeneidad} \not\Longrightarrow \text{ecuación físicamente correcta}. }$$

Esta asimetría convierte el análisis dimensional en una excelente herramienta de auditoría.

[]{#ejemplo-cinemática-elemental}

### Ejemplo: cinemática elemental {#fispm-c02-ejemplo-cinemuxe1tica-elemental}

Consideremos

$$x=x_0+v_0t+\frac12 at^2.$$

Sin derivarla todavía desde una teoría del movimiento, podemos auditarla dimensionalmente.

Tenemos:

$$[x]=L,$$

$$[x_0]=L.$$

Además, $[v_0t] = LT^{-1}T = L,$

y

$$[at^2] = LT^{-2}T^2 = L.$$

El factor

$$\frac12$$

es un número puro y no modifica la dimensión. Por tanto,

$$\boxed{ [x] = [x_0] = [v_0t] = [at^2] = L. }$$

La ecuación pasa el control de homogeneidad.

Esto no constituye todavía una derivación física de la fórmula.

Solo demuestra que su estructura aditiva es dimensionalmente compatible.

[]{#ejemplo-de-ecuación-defectuosa}

### Ejemplo de ecuación defectuosa {#fispm-c02-ejemplo-de-ecuaciuxf3n-defectuosa}

Supongamos que aparece

$$x=x_0+v_0t+at.$$

Los dos primeros términos tienen dimensión:

$$L.$$

Pero

$$[at] = LT^{-2}T = LT^{-1}.$$

Por tanto, $[at]\neq L.$ La suma intenta combinar longitud con velocidad. La ecuación no puede ser correcta tal como está escrita. No necesitamos datos experimentales para detectar este problema.

[]{#unidades-iguales-no-bastan-para-justificar-una-suma}

### Unidades iguales no bastan para justificar una suma {#fispm-c02-unidades-iguales-no-bastan-para-justificar-una-suma}

En §5 vimos que presión y densidad de energía poseen la misma dimensión: $ML^{-1}T^{-2}.$ En SI ambas pueden incluso expresarse mediante unidades algebraicamente equivalentes: $\mathrm{Pa} = \mathrm{J\,m^{-3}}.$

Sin embargo, la Proposición 2 no dice:

> «Toda magnitud con la misma dimensión puede sumarse físicamente con cualquier otra.»

Dice únicamente que una suma físicamente significativa debe superar el control dimensional.

Después debemos verificar también:

- el tipo de magnitud;

- la interpretación del modelo;

- la procedencia de cada término;

- el estatus físico de la ecuación.

Así, la homogeneidad es un filtro estructural, no un diccionario semántico completo.

[]{#constantes-numéricas-y-constantes-físicas}

### Constantes numéricas y constantes físicas {#fispm-c02-constantes-numuxe9ricas-y-constantes-fuxedsicas}

Consideremos

$$Q=2X.$$

El factor $2$ es un número puro. Por tanto, $[Q]=[X].$ Pero en

$$Q=kX,$$

no podemos suponer que $k$ sea adimensional. Su dimensión debe satisfacer

$$[k] = \frac{[Q]}{[X]}.$$

Por ejemplo, si

$$F=kx,$$

y queremos

$$[F]=MLT^{-2},$$

mientras

$$[x]=L,$$

entonces $[k] = MT^{-2}.$ La letra $k$ no trae consigo una dimensión universal. Su dimensión depende del papel que desempeña en la relación física.

[]{#las-constantes-pueden-reparar-una-ecuación-solo-si-pertenecen-al-modelo}

### Las constantes pueden reparar una ecuación solo si pertenecen al modelo {#fispm-c02-las-constantes-pueden-reparar-una-ecuaciuxf3n-solo-si-pertenecen-al-modelo}

Supongamos que alguien propone

$$x=t.$$

Dimensionalmente, $L\neq T.$ La ecuación falla.

Podríamos introducir una constante $c$ con dimensión

$$[c]=LT^{-1}$$

y escribir

$$x=ct.$$

Ahora: $[ct] = LT^{-1}T = L.$ La nueva ecuación es homogénea. Pero no hemos demostrado que exista físicamente una constante $c$ apropiada ni que la relación describa el sistema. Solo hemos construido una forma dimensionalmente admisible.

Por tanto:

$$\boxed{ \text{restaurar dimensiones} \neq \text{derivar una ley física}. }$$

[]{#igualdades-entre-magnitudes-y-ecuaciones-numéricas}

### Igualdades entre magnitudes y ecuaciones numéricas {#fispm-c02-igualdades-entre-magnitudes-y-ecuaciones-numuxe9ricas}

Una ecuación física puede leerse en dos niveles.

[]{#nivel-de-magnitudes}

#### Nivel de magnitudes {#fispm-c02-nivel-de-magnitudes}

$$Q_1+Q_2=Q_3.$$

[]{#nivel-de-valores-numéricos-en-un-sistema-de-unidades-coherente}

#### Nivel de valores numéricos en un sistema de unidades coherente {#fispm-c02-nivel-de-valores-numuxe9ricos-en-un-sistema-de-unidades-coherente}

$$q_1+q_2=q_3.$$

La coherencia estudiada en §4 permite que ambas formas se parezcan.

Pero la Proposición 2 nos recuerda por qué esa semejanza no es accidental:

si los términos tuvieran dimensiones distintas, cambiarían con factores distintos al cambiar las unidades base y la forma numérica dejaría de ser estable. La homogeneidad es, por tanto, una manifestación de la independencia física respecto de la convención de unidades.

[]{#ecuaciones-multiplicativas}

### Ecuaciones multiplicativas {#fispm-c02-ecuaciones-multiplicativas}

La exigencia de igualdad dimensional término a término se refiere especialmente a **sumas e igualdades aditivas**. En una relación multiplicativa, $Q=AB,$

no exigimos

$$[Q]=[A]=[B].$$

Exigimos

$$[Q]=[A][B].$$

Por ejemplo, $E=F\ell$

satisface $[E] = [F][\ell] = MLT^{-2}L = ML^2T^{-2}.$

Así, una auditoría dimensional debe respetar la estructura algebraica de la ecuación:

- en productos, las dimensiones se multiplican;

- en cocientes, se dividen;

- en potencias, se elevan;

- en sumas, los términos deben ser homogéneos.

[]{#la-dimensión-de-una-derivada-o-cociente-incremental}

### La dimensión de una derivada o cociente incremental {#fispm-c02-la-dimensiuxf3n-de-una-derivada-o-cociente-incremental}

Todavía no necesitamos cálculo diferencial formal para comprender un patrón. Si una magnitud $Q$ cambia durante un intervalo temporal $\Delta t$, el cociente

$$\frac{\Delta Q}{\Delta t}$$

posee dimensión

$$\frac{[Q]}{T}.$$

Así, si

$$[Q]=L,$$

entonces

$$\left[ \frac{\Delta Q}{\Delta t} \right] = LT^{-1}.$$

Más adelante, cuando introduzcamos derivadas, el mismo razonamiento dimensional se conservará: $\left[ \frac{dQ}{dt} \right] = [Q]T^{-1}.$ La dimensión no sustituye al concepto de derivada. Solo registra qué estructura dimensional debe tener el resultado.

[]{#la-dimensión-de-una-integral}

### La dimensión de una integral {#fispm-c02-la-dimensiuxf3n-de-una-integral}

De manera análoga, cuando más adelante encontremos una cantidad definida mediante una integral temporal,

$$R=\int Q\,dt,$$

la dimensión esperada será $[R]=[Q]T.$

No desarrollaremos aquí integración. El objetivo es mostrar que el análisis dimensional es compatible con las operaciones matemáticas que aparecerán después. Cada operación modifica la dimensión de una manera controlable.

[]{#funciones-no-algebraicas-frontera-de-esta-sección}

### Funciones no algebraicas: frontera de esta sección {#fispm-c02-funciones-no-algebraicas-frontera-de-esta-secciuxf3n}

¿Qué ocurre con expresiones como

$$\sin x,$$

$$e^x,$$

o

$$\log x?$$

La respuesta exige tratar cuidadosamente las **cantidades de dimensión uno**.

Ése será el objeto de §8.

No adelantaremos ahora la discusión.

Solo registramos que no debemos aplicar reglas algebraicas de manera mecánica a funciones no polinómicas sin examinar la dimensión de sus argumentos.

[]{#ejercicios-2}

### Ejercicios {#fispm-c02-ejercicios-2}

**Ejercicio 14 --- Auditoría de ecuaciones**

**Tipo:** análisis dimensional · **Nivel:** central

Decide cuáles de las siguientes ecuaciones son dimensionalmente homogéneas. No juzgues todavía si son físicamente correctas.

1.  $$x=x_0+vt.$$

2.  $$x=x_0+vt^2.$$

3.  $$v=v_0+at.$$

4.  $$v=v_0+a t^2.$$

5.  $$E=F\ell.$$

6.  $$p=\frac{F}{A}.$$

**Solución**

**1.**

$$[x]=L,$$

$$[x_0]=L,$$

$$[vt]=LT^{-1}T=L.$$

Es homogénea.

**2.**

$$[vt^2] = LT^{-1}T^2 = LT.$$

No es homogénea.

**3.**

$$[v_0]=LT^{-1},$$

y

$$[at] = LT^{-2}T = LT^{-1}.$$

Es homogénea.

**4.**

$$[at^2] = LT^{-2}T^2 = L.$$

No puede sumarse con una velocidad: $L\neq LT^{-1}.$

No es homogénea.

**5.**

$$[F\ell] = MLT^{-2}L = ML^2T^{-2}.$$

La ecuación es homogénea si $E$ tiene dimensión de energía.

**6.**

$$\left[\frac{F}{A}\right] = \frac{MLT^{-2}}{L^2} = ML^{-1}T^{-2}.$$

La ecuación es homogénea si $p$ representa una magnitud de esa dimensión.

Resultado:

$$\boxed{ 1,\ 3,\ 5,\ 6 \text{ pasan el control dimensional;} \quad 2,\ 4 \text{ fallan.} }$$

**Ejercicio 15 --- Determinar la dimensión de una constante**

En cada relación, determina la dimensión que debe tener la constante indicada para que la ecuación sea homogénea.

1.  $$F=kx.$$

2.  $$E=\kappa t.$$

3.  $$x=ct.$$

4.  $$v^2=\alpha x.$$

**Solución**

**1.**

Queremos

$$[F]=[k][x].$$

Entonces $[k] = \frac{MLT^{-2}}{L} = MT^{-2}.$

**2.**

$$[E]=[\kappa]T.$$

Luego

$$[\kappa] = \frac{ML^2T^{-2}}{T} = ML^2T^{-3}.$$

**3.**

$$L=[c]T.$$

Por tanto

$$[c]=LT^{-1}.$$

**4.**

$$[v^2] = L^2T^{-2}.$$

Como $[\alpha x] = [\alpha]L,$

necesitamos

$$[\alpha] = LT^{-2}.$$

En conjunto:

$$\boxed{ [k]=MT^{-2}, \quad [\kappa]=ML^2T^{-3}, \quad [c]=LT^{-1}, \quad [\alpha]=LT^{-2}. }$$

**Ejercicio 16 --- Homogénea pero no determinada**

Considera la familia de ecuaciones

$$x=x_0+Cvt,$$

donde $C$ es una constante numérica.

1.  Demuestra que la ecuación es dimensionalmente homogénea para todo número real $C$.

2.  Explica por qué el análisis dimensional no puede determinar el valor de $C$.

3.  ¿Qué tipo de información adicional sería necesaria para determinarlo físicamente?

4.  ¿Qué enseña el ejercicio acerca de la Proposición 2?

**Solución**

Tenemos

$$[x]=L,$$

$$[x_0]=L,$$

y

$$[vt] = LT^{-1}T = L.$$

Un número puro $C$ no modifica la dimensión: $[Cvt]=L.$ Por tanto, $[x]=[x_0]=[Cvt]=L$

para cualquier

$$C\in\mathbb R.$$

La ecuación es dimensionalmente homogénea para todo $C$. El análisis dimensional solo exige compatibilidad de dimensiones. No distingue entre

$$C=1,$$

$$C=2,$$

$$C=-17,$$

o cualquier otro valor.

Para determinar $C$ necesitaríamos información adicional, por ejemplo:

- una ley física más específica;

- una derivación a partir de postulados del modelo;

- una condición experimental;

- datos empíricos;

- una simetría u otra restricción estructural.

El ejercicio muestra exactamente el alcance de la Proposición 2:

$$\boxed{ \text{homogeneidad} = \text{condición necesaria}, }$$

pero

$$\boxed{ \text{homogeneidad} \neq \text{determinación completa de la ley}. }$$

[]{#síntesis-4}

### Síntesis {#fispm-c02-suxedntesis-4}

La idea central de la sección es:

$$\boxed{ \text{una ecuación física no debe depender de la convención usada para medir}. }$$

Al cambiar independientemente las unidades base, cada término adquiere un factor controlado por su dimensión. Para que una suma conserve su forma física, todos los términos aditivos deben transformarse con el mismo factor.

De ahí la Proposición 2:

$$\boxed{ Q_1+\cdots+Q_r = R_1+\cdots+R_s }$$

implica, bajo las hipótesis declaradas,

$$\boxed{ [Q_1] = \cdots = [Q_r] = [R_1] = \cdots = [R_s]. }$$

La homogeneidad permite detectar errores estructurales. Pero no selecciona por sí sola la ley correcta.

Por tanto:

$$\boxed{ \text{inhomogeneidad} \Rightarrow \text{problema}, }$$

mientras

$$\boxed{ \text{homogeneidad} \not\Rightarrow \text{verdad física}. }$$

La siguiente sección convertirá esta condición necesaria en una herramienta de trabajo sistemática (§[7](#fispm-c02-el-anuxe1lisis-dimensional-como-auditoruxeda)).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-1 label="fispm-c02-notas-y-fuentes-1"}

[]{#el-análisis-dimensional-como-auditoría}

[]{#fispm-t1-c02-s07}

[]{#fpm-i-02-s07}

## 7. El análisis dimensional como auditoría {#fispm-c02-el-anuxe1lisis-dimensional-como-auditoruxeda}

[]{#por-qué-aparece-una-ecuación-puede-parecer-razonable-y-estar-mal-construida}

### Por qué aparece: una ecuación puede parecer razonable y estar mal construida {#fispm-c02-por-quuxe9-aparece-una-ecuaciuxf3n-puede-parecer-razonable-y-estar-mal-construida}

Consideremos la expresión

$$x=x_0+v_0t+\frac12 at.$$

A primera vista tiene una apariencia familiar:

- posición inicial;

- velocidad;

- aceleración;

- tiempo.

Incluso contiene los símbolos que esperaríamos encontrar en un problema de movimiento.

Sin embargo, antes de sustituir un solo número podemos preguntar:

$$\boxed{ \text{¿pueden sumarse físicamente estos términos?} }$$

Tenemos

$$[x]=L,$$

$$[x_0]=L,$$

$$[v_0t] = LT^{-1}T = L,$$

pero

$$[at] = LT^{-2}T = LT^{-1}.$$

El último término tiene dimensión de velocidad, no de longitud. Por tanto, la expresión falla antes de cualquier cálculo numérico.

Ésta es la función práctica que comenzaremos a atribuir al análisis dimensional:

$$\boxed{ \text{usar la estructura dimensional para auditar una expresión física}. }$$

La palabra **auditar** es deliberada.

No significa derivar toda la física de las dimensiones. Significa someter una fórmula, un cálculo o un modelo a una prueba estructural que puede descubrir ciertos errores antes de continuar.[^27]

[]{#qué-podríamos-pensar-inicialmente}

### Qué podríamos pensar inicialmente {#fispm-c02-quuxe9-podruxedamos-pensar-inicialmente}

Un lector puede formular una primera intuición:

> «Si las unidades finales son correctas, la ecuación está bien.»

Esta intuición contiene una parte útil y una parte peligrosa. La parte útil es que una incompatibilidad de unidades puede revelar un problema. La parte peligrosa es creer que una coincidencia dimensional certifica la física.

Por ejemplo, $E=\frac12 mv^2$

y

$$E=37mv^2$$

tienen exactamente la misma dimensión: $ML^2T^{-2}.$

También la tiene $E=-mv^2.$ El análisis dimensional no puede decidir, por sí solo, cuál de estas expresiones describe una energía física en un modelo determinado.

Por eso la intuición inicial debe corregirse:

$$\boxed{ \text{las dimensiones pueden refutar ciertas formas, pero no verificar por sí solas una ley}. }$$

Esta asimetría ya apareció en el Principio 12. En §7 la convertiremos en un procedimiento de trabajo.

[]{#primera-representación-la-ecuación-como-colección-de-términos}

### Primera representación: la ecuación como colección de términos {#fispm-c02-primera-representaciuxf3n-la-ecuaciuxf3n-como-colecciuxf3n-de-tuxe9rminos}

Cuando vemos

$$Q_1+Q_2+\cdots+Q_n=R,$$

la primera representación útil no es todavía numérica.

Separamos la ecuación en términos: $Q_1,\quad Q_2,\quad\ldots,\quad Q_n,\quad R.$

Después reemplazamos cada término por su dimensión: $[Q_1],\quad [Q_2],\quad\ldots,\quad [Q_n],\quad [R].$

Por la Proposición 2, si la relación pretende ser una ecuación física aditiva independiente de la elección de unidades, necesitamos:

$$[Q_1] = [Q_2] = \cdots = [Q_n] = [R].$$

Este cambio de representación transforma una expresión física en un problema algebraico sobre exponentes dimensionales.

[]{#segunda-representación-la-firma-dimensional}

### Segunda representación: la firma dimensional {#fispm-c02-segunda-representaciuxf3n-la-firma-dimensional}

En §5 escribimos, para una magnitud $Q$,

$$[Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta.$$

Podemos registrar los mismos datos mediante el vector

$$\mathbf d(Q) = (\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta),$$

usando el orden fijo

$$(T,L,M,I,\Theta,N,J).$$

**Definición 18 --- Firma dimensional** La **firma dimensional** de una magnitud $Q$ es el vector ordenado de exponentes de sus dimensiones base:

$$\mathbf d(Q) = (\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta)$$

cuando

$$[Q] = T^\alpha L^\beta M^\gamma I^\delta \Theta^\varepsilon N^\zeta J^\eta.$$

Por ejemplo, $[v]=LT^{-1}$

corresponde a

$$\mathbf d(v) = (-1,1,0,0,0,0,0).$$

Para una aceleración, $[a]=LT^{-2},$

por lo que

$$\mathbf d(a) = (-2,1,0,0,0,0,0).$$

Para una fuerza, $[F]=MLT^{-2},$

de modo que

$$\mathbf d(F) = (-2,1,1,0,0,0,0).$$

La firma dimensional no añade nueva física.

Solo reorganiza la información de una manera que facilitará:

- auditorías;

- comparación de términos;

- sistemas de ecuaciones para exponentes;

- el teorema $\Pi$ de Buckingham en §12.

[]{#leer-operaciones-mediante-firmas}

### Leer operaciones mediante firmas {#fispm-c02-leer-operaciones-mediante-firmas}

La notación vectorial convierte las reglas dimensionales en operaciones muy simples.

[]{#producto}

#### Producto {#fispm-c02-producto}

Si

$$Q=AB,$$

entonces $[Q]=[A][B].$ Por tanto,

$$\boxed{ \mathbf d(Q) = \mathbf d(A) + \mathbf d(B). }$$

[]{#cociente}

#### Cociente {#fispm-c02-cociente}

Si

$$Q=\frac{A}{B},$$

entonces

$$\boxed{ \mathbf d(Q) = \mathbf d(A) - \mathbf d(B). }$$

[]{#potencia}

#### Potencia {#fispm-c02-potencia}

Si

$$Q=A^n,$$

entonces

$$\boxed{ \mathbf d(Q) = n\,\mathbf d(A). }$$

[]{#suma}

#### Suma {#fispm-c02-suma}

Si

$$Q=A+B$$

representa una suma física admisible, entonces necesitamos

$$\boxed{ \mathbf d(Q) = \mathbf d(A) = \mathbf d(B). }$$

La suma es diferente de las otras operaciones.

No combina firmas: exige igualdad de firmas.

[]{#precisar-el-método-qué-es-una-auditoría-dimensional}

### Precisar el método: qué es una auditoría dimensional {#fispm-c02-precisar-el-muxe9todo-quuxe9-es-una-auditoruxeda-dimensional}

**Definición 19 --- Auditoría dimensional** Una **auditoría dimensional** es el procedimiento de analizar una expresión, ecuación o cadena de cálculo reemplazando sus magnitudes por dimensiones o firmas dimensionales para comprobar la compatibilidad estructural exigida por sus operaciones y localizar posibles inconsistencias.

La definición contiene tres verbos:

1.  **analizar**;

2.  **comprobar**;

3.  **localizar**.

Una auditoría no se limita a pronunciar «correcto» o «incorrecto».

Debe intentar identificar **dónde** aparece la incompatibilidad.

**Principio 13 --- Auditar la estructura antes de sustituir números** Cuando una relación física contiene varios términos, parámetros o conversiones, conviene verificar primero su estructura dimensional. Una incompatibilidad detectada en esta etapa evita cálculos numéricos que no pueden reparar el problema.

[]{#protocolo-fpm-de-auditoría-dimensional}

### Protocolo FPM de auditoría dimensional {#fispm-c02-protocolo-fpm-de-auditoruxeda-dimensional}

Aplicaremos el siguiente procedimiento.

[]{#paso-1-declarar-el-significado-de-los-símbolos}

#### Paso 1 --- Declarar el significado de los símbolos {#fispm-c02-paso-1-declarar-el-significado-de-los-suxedmbolos}

No comenzamos con letras desnudas.

Escribimos, por ejemplo:

$$x:\text{ posición},$$

$$v:\text{ velocidad},$$

$$t:\text{ tiempo}.$$

Esta etapa evita asignar una dimensión incorrecta a una letra por hábito.

[]{#paso-2-registrar-dimensiones-conocidas}

#### Paso 2 --- Registrar dimensiones conocidas {#fispm-c02-paso-2-registrar-dimensiones-conocidas}

Por ejemplo:

$$[x]=L,$$

$$[v]=LT^{-1},$$

$$[t]=T.$$

[]{#paso-3-descomponer-cada-término}

#### Paso 3 --- Descomponer cada término {#fispm-c02-paso-3-descomponer-cada-tuxe9rmino}

Si aparece

$$v^2t,$$

calculamos: $[v^2t] = [v]^2[t].$

No intentamos adivinar el resultado visualmente.

[]{#paso-4-simplificar-dimensiones-o-firmas}

#### Paso 4 --- Simplificar dimensiones o firmas {#fispm-c02-paso-4-simplificar-dimensiones-o-firmas}

Tenemos $[v^2t] = (LT^{-1})^2T = L^2T^{-1}.$

[]{#paso-5-aplicar-la-regla-algebraica-pertinente}

#### Paso 5 --- Aplicar la regla algebraica pertinente {#fispm-c02-paso-5-aplicar-la-regla-algebraica-pertinente}

- producto: multiplicar dimensiones;

- cociente: dividir;

- potencia: elevar;

- suma o igualdad aditiva: exigir igualdad dimensional.

[]{#paso-6-si-falla-localizar-el-primer-punto-incompatible}

#### Paso 6 --- Si falla, localizar el primer punto incompatible {#fispm-c02-paso-6-si-falla-localizar-el-primer-punto-incompatible}

No basta decir:

> «las unidades no dan».

Debemos señalar, por ejemplo: $[at]=LT^{-1} \neq L=[x_0].$

[]{#paso-7-si-pasa-no-detener-la-revisión-física}

#### Paso 7 --- Si pasa, no detener la revisión física {#fispm-c02-paso-7-si-pasa-no-detener-la-revisiuxf3n-fuxedsica}

Después del control dimensional todavía debemos preguntar:

- ¿la manipulación algebraica es correcta?;

- ¿los símbolos representan lo que creemos?;

- ¿la ecuación tiene el estatus físico declarado?;

- ¿las hipótesis del modelo son adecuadas?;

- ¿estamos dentro del régimen de validez?;

- ¿la relación está apoyada por una ley, derivación o evidencia?

La auditoría dimensional es una capa de control dentro de una auditoría física más amplia.

[]{#ejemplo-desarrollado-1-encontrar-el-término-defectuoso}

### Ejemplo desarrollado 1 --- Encontrar el término defectuoso {#fispm-c02-ejemplo-desarrollado-1-encontrar-el-tuxe9rmino-defectuoso}

Consideremos: $x=x_0+v_0t+\frac12 at.$

[]{#intuir}

#### Intuir {#fispm-c02-intuir}

Sabemos que todos los términos sumados a una posición deberían representar contribuciones a una posición.

[]{#representar}

#### Representar {#fispm-c02-representar}

Asignamos:

$$[x]=[x_0]=L,$$

$$[v_0]=LT^{-1},$$

$$[a]=LT^{-2},$$

$$[t]=T.$$

[]{#precisar}

#### Precisar {#fispm-c02-precisar}

Calculamos: $[v_0t] = LT^{-1}T = L,$

pero: $[at] = LT^{-2}T = LT^{-1}.$

[]{#poner-a-prueba}

#### Poner a prueba {#fispm-c02-poner-a-prueba}

Comparamos las firmas:

$$\mathbf d(x) = (0,1,0,0,0,0,0),$$

$$\mathbf d(v_0t) = (0,1,0,0,0,0,0),$$

$$\mathbf d(at) = (-1,1,0,0,0,0,0).$$

El último término no pertenece a la misma clase dimensional.

[]{#diagnóstico}

#### Diagnóstico {#fispm-c02-diagnuxf3stico}

La ecuación falla por **inhomogeneidad dimensional**. La auditoría no nos dice automáticamente cuál era la fórmula pretendida. Podría faltar, por ejemplo, otro factor de tiempo.

Pero reconstruir ese factor requiere información adicional.

**Pausa de autoexplicación** Antes de continuar, explica sin mirar las ecuaciones:

**¿por qué sustituir valores numéricos de $a$ y $t$ no puede corregir el defecto dimensional de $at$ dentro de una suma de longitudes?**

Una respuesta adecuada debe mencionar que cambiar números no cambia la dimensión del término.

[]{#ejemplo-desarrollado-2-una-fórmula-que-pasa-y-puede-seguir-siendo-falsa}

### Ejemplo desarrollado 2 --- Una fórmula que pasa y puede seguir siendo falsa {#fispm-c02-ejemplo-desarrollado-2-una-fuxf3rmula-que-pasa-y-puede-seguir-siendo-falsa}

Consideremos: $E=7mv^2.$

Tenemos $[m]=M$

y

$$[v^2]=L^2T^{-2}.$$

Por tanto, $[7mv^2] = ML^2T^{-2}.$ La fórmula posee dimensión de energía.

Pasa el control dimensional. Pero el análisis dimensional no demuestra que el coeficiente $7$ tenga justificación física. Tampoco demuestra que la dependencia exacta en $v^2$ sea la ley apropiada en cualquier teoría o régimen.

La fórmula puede ser:

- algebraicamente homogénea;

- dimensionalmente admisible;

- físicamente incorrecta.

Éste es un **no-ejemplo** crucial de la inferencia:

$$\text{«es homogénea»} \Longrightarrow \text{«es una ley correcta»}.$$

La inferencia es inválida.

[]{#tres-clases-de-fallo-que-no-debemos-confundir}

### Tres clases de fallo que no debemos confundir {#fispm-c02-tres-clases-de-fallo-que-no-debemos-confundir}

La auditoría dimensional ayuda a separar errores distintos.

[]{#a.-fallo-dimensional}

#### A. Fallo dimensional {#fispm-c02-a.-fallo-dimensional}

Ejemplo: $x=x_0+at.$

Tenemos $L\neq LT^{-1}.$ El problema es estructural y puede detectarse sin conocer los valores.

[]{#b.-fallo-algebraico}

#### B. Fallo algebraico {#fispm-c02-b.-fallo-algebraico}

Supongamos una ecuación dimensionalmente correcta: $v=v_0+at.$ Si alguien parte de ella y escribe $v-v_0=a+t,$

la nueva expresión puede contener un error algebraico aunque el problema original fuera dimensionalmente correcto. El análisis dimensional puede detectar además que

$$[a+t]$$

intenta sumar

$$LT^{-2}$$

y

$$T,$$

pero la causa inmediata del fallo fue una manipulación algebraica ilegítima.

[]{#c.-fallo-físico-o-de-modelización}

#### C. Fallo físico o de modelización {#fispm-c02-c.-fallo-fuxedsico-o-de-modelizaciuxf3n}

Una fórmula puede ser dimensionalmente homogénea y algebraicamente impecable, pero utilizar:

- una ley inaplicable;

- una aproximación fuera de régimen;

- una condición inicial incorrecta;

- una interpretación equivocada;

- una idealización físicamente insuficiente.

Por eso necesitamos una jerarquía de auditorías.

[]{#representación-por-capas}

### Representación por capas {#fispm-c02-representaciuxf3n-por-capas}

Organizaremos el diagnóstico así:

$$\boxed{ \text{dimensional} \to \text{algebraica} \to \text{semántica} \to \text{física} }$$

[]{#capa-1-auditoría-dimensional}

#### Capa 1 --- Auditoría dimensional {#fispm-c02-capa-1-auditoruxeda-dimensional}

Pregunta:

> ¿las operaciones combinan dimensiones compatibles?

[]{#capa-2-auditoría-algebraica}

#### Capa 2 --- Auditoría algebraica {#fispm-c02-capa-2-auditoruxeda-algebraica}

Pregunta:

> ¿las transformaciones matemáticas son válidas?

[]{#capa-3-auditoría-semántica}

#### Capa 3 --- Auditoría semántica {#fispm-c02-capa-3-auditoruxeda-semuxe1ntica}

Pregunta:

> ¿cada símbolo conserva el significado físico que le asignamos?

[]{#capa-4-auditoría-física}

#### Capa 4 --- Auditoría física {#fispm-c02-capa-4-auditoruxeda-fuxedsica}

Pregunta:

> ¿las leyes, hipótesis, idealizaciones y aproximaciones son adecuadas para el sistema y el régimen?

**Principio 14 --- Identificar el nivel del fallo** Detectar que una expresión es incorrecta no basta. Siempre que sea posible distinguiremos si el problema es dimensional, algebraico, semántico o físico, porque cada clase de fallo exige una corrección diferente.

Este principio extiende el protocolo de revisión del capítulo 1.

[]{#conflicto-típico-las-unidades-se-cancelan-así-que-está-bien}

### Conflicto típico: «las unidades se cancelan, así que está bien» {#fispm-c02-conflicto-tuxedpico-las-unidades-se-cancelan-asuxed-que-estuxe1-bien}

Consideremos: $Q=\frac{ab}{c}.$ Un estudiante sustituye números y obtiene finalmente una unidad esperada.

¿Basta eso para validar todo el cálculo?

No necesariamente.

Dos errores de conversión pueden compensarse. Una constante dimensional puede haberse interpretado mal. Una manipulación algebraica previa puede ser incorrecta.

Incluso una fórmula físicamente falsa puede producir la dimensión esperada. La revisión correcta no observa únicamente la unidad de la última línea. Debe seguir la estructura de los términos relevantes.

Por eso:

$$\boxed{ \text{unidad final plausible} \not\Rightarrow \text{cálculo íntegro correcto}. }$$

[]{#conflicto-típico-si-falla-puedo-arreglarlo-con-una-constante}

### Conflicto típico: «si falla, puedo arreglarlo con una constante» {#fispm-c02-conflicto-tuxedpico-si-falla-puedo-arreglarlo-con-una-constante}

Supongamos: $x=t^2.$ La expresión es inhomogénea: $L\neq T^2.$

Podemos introducir una constante $\alpha$ con dimensión

$$[\alpha]=LT^{-2}$$

y escribir: $x=\alpha t^2.$ Ahora la ecuación es homogénea. Pero la operación solo muestra que **existe una manera dimensional de completar la forma**.

No demuestra:

- que $\alpha$ sea constante físicamente;

- que $x$ dependa de $t^2$;

- que el modelo describa un sistema real.

La reparación dimensional genera una **familia admisible de formas**, no una ley verificada.

[]{#variación-detectar-la-dimensión-que-falta}

### Variación: detectar la dimensión que falta {#fispm-c02-variaciuxf3n-detectar-la-dimensiuxf3n-que-falta}

Aunque §7 no está dedicado todavía a inferir leyes, la auditoría puede localizar información ausente. Supongamos: $F=k\frac{m_1m_2}{r^2}.$ Sin interpretar todavía la ecuación como una ley concreta, podemos preguntar qué dimensión necesitaría $k$ para que la relación fuera homogénea.

Tenemos: $[F]=MLT^{-2},$

y

$$\left[ \frac{m_1m_2}{r^2} \right] = \frac{M^2}{L^2} = M^2L^{-2}.$$

Por tanto,

$$[k] = \frac{MLT^{-2}}{M^2L^{-2}} = M^{-1}L^3T^{-2}.$$

La auditoría ha determinado una restricción necesaria sobre $k$.

No ha demostrado la relación. Esta forma de razonamiento prepara §§10--12.

[]{#variación-usar-firmas-para-localizar-un-error}

### Variación: usar firmas para localizar un error {#fispm-c02-variaciuxf3n-usar-firmas-para-localizar-un-error}

Sea

$$R=A+B+C.$$

Supongamos:

$$\mathbf d(A) = (-2,2,1,0,0,0,0),$$

$$\mathbf d(B) = (-2,2,1,0,0,0,0),$$

$$\mathbf d(C) = (-3,2,1,0,0,0,0),$$

y

$$\mathbf d(R) = (-2,2,1,0,0,0,0).$$

No necesitamos reconstruir inmediatamente los nombres físicos de las magnitudes.

Vemos que $C$ difiere solo en el exponente temporal:

$$-3$$

en lugar de

$$-2.$$

Esto orienta el diagnóstico:

> el término sospechoso contiene probablemente un factor temporal adicional o faltante.

La firma dimensional funciona así como una herramienta de **localización**, no solo de clasificación.

[]{#qué-no-puede-detectar-el-análisis-dimensional}

### Qué no puede detectar el análisis dimensional {#fispm-c02-quuxe9-no-puede-detectar-el-anuxe1lisis-dimensional}

Una auditoría dimensional puede no advertir:

[]{#coeficientes-numéricos-incorrectos}

#### Coeficientes numéricos incorrectos {#fispm-c02-coeficientes-numuxe9ricos-incorrectos}

$$E=2mv^2$$

y

$$E=\frac12 mv^2$$

tienen la misma dimensión.

[]{#signos-incorrectos}

#### Signos incorrectos {#fispm-c02-signos-incorrectos}

$$A+B=C$$

y

$$A-B=C$$

pueden ser igualmente homogéneas.

[]{#dependencias-funcionales-distintas-con-igual-dimensión}

#### Dependencias funcionales distintas con igual dimensión {#fispm-c02-dependencias-funcionales-distintas-con-igual-dimensiuxf3n}

Dos funciones diferentes pueden producir la misma dimensión final.

[]{#hipótesis-físicas-incorrectas}

#### Hipótesis físicas incorrectas {#fispm-c02-hipuxf3tesis-fuxedsicas-incorrectas}

Una ecuación puede utilizar una aproximación fuera de régimen y seguir siendo homogénea.

[]{#confusión-entre-magnitudes-de-igual-dimensión}

#### Confusión entre magnitudes de igual dimensión {#fispm-c02-confusiuxf3n-entre-magnitudes-de-igual-dimensiuxf3n}

Presión y densidad de energía pueden compartir dimensión sin ser intercambiables en cualquier contexto. Ésta es la frontera conceptual de la herramienta.

[]{#lectura-de-una-auditoría-estrategia-global-y-pasos-locales}

### Lectura de una auditoría: estrategia global y pasos locales {#fispm-c02-lectura-de-una-auditoruxeda-estrategia-global-y-pasos-locales}

práctica guiada exige distinguir la estrategia de las manipulaciones.

En una auditoría dimensional:

[]{#estrategia-global}

#### Estrategia global {#fispm-c02-estrategia-global}

Queremos comprobar si la estructura de la ecuación puede permanecer independiente de la elección de unidades.

[]{#pasos-locales}

#### Pasos locales {#fispm-c02-pasos-locales}

Calculamos dimensiones, sumamos exponentes y comparamos firmas.

No debemos confundir ambos niveles.

Las operaciones algebraicas son el mecanismo. La razón física de hacerlas es la invariancia estructural expresada por la Proposición 2.

**Pausa de autoexplicación** Explica en tus propias palabras:

1.  por qué una firma dimensional diferente detecta un problema en una suma;

2.  por qué una firma dimensional igual no basta para probar una ley;

3.  qué papel cumple la Proposición 2 dentro del protocolo de auditoría.

Si las tres respuestas pueden darse sin recurrir a una fórmula memorizada, la herramienta empieza a estar comprendida y no solo aplicada.

[]{#conectar-con-el-protocolo-general-de-física-para-matemáticos}

### Conectar con el protocolo general de Física para matemáticos {#fispm-c02-conectar-con-el-protocolo-general-de-fuxedsica-para-matemuxe1ticos}

En el capítulo 1 fijamos la cadena:

$$\text{fenómeno} \to \text{modelo} \to \text{predicción} \to \text{contraste} \to \text{revisión}.$$

La auditoría dimensional se inserta dentro de la construcción y revisión del modelo:

$$\boxed{\begin{gathered} \text{representación} \to \text{ecuaciones}\\[2pt]\Downarrow\\[2pt]\text{auditoría dimensional} \to \text{derivación matemática}\\[2pt]\Downarrow\\[2pt]\text{interpretación física}. \end{gathered}}$$

No sustituye:

- observaciones;

- teoría;

- modelización;

- prueba matemática;

- contraste experimental.

Cumple una función más específica:

$$\boxed{ \text{descartar incompatibilidades estructurales baratas de detectar}. }$$

[]{#práctica-guiada}

### Práctica guiada {#fispm-c02-pruxe1ctica-guiada}

**Ejercicio 17 --- Auditoría dimensional completa**

**Objetivo:** `Síntesis — auditoría`

**Intenta primero: 3--5 min antes de leer la solución.**

Los cuatro apartados siguen la secuencia:

$$\text{Recuperación} \to \text{Consolidación} \to \text{Diagnóstico} \to \text{Síntesis}.$$

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n}

Calcula las firmas dimensionales de: $v,\qquad a,\qquad F,\qquad E.$

Usa el orden

$$(T,L,M,I,\Theta,N,J).$$

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n}

Audita: $x=x_0+v_0t+\frac12 at^2.$

Verifica la dimensión de cada término y explica por qué el factor $1/2$ no interviene en el control dimensional.

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico}

Un estudiante propone: $v=v_0+at^2.$

Otro responde:

> «La fórmula puede arreglarse cambiando el valor numérico de $a$.»

Identifica el error dimensional y explica por qué la respuesta no puede repararlo.

### D. Síntesis {#fispm-c02-d.-suxedntesis}

Considera: $Q=C\,m^\alpha v^\beta,$

donde $C$ es un número puro y queremos que $Q$ tenga dimensión de energía.

1.  Determina las condiciones sobre $\alpha$ y $\beta$.

2.  Decide si esas condiciones determinan completamente una ley física para la energía.

3.  Clasifica qué parte de tu razonamiento es dimensional y qué información adicional sería física.

**Solución**

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-1}

Para velocidad: $[v]=LT^{-1},$

por tanto

$$\boxed{ \mathbf d(v) = (-1,1,0,0,0,0,0). }$$

Para aceleración: $[a]=LT^{-2},$

entonces

$$\boxed{ \mathbf d(a) = (-2,1,0,0,0,0,0). }$$

Para fuerza: $[F]=MLT^{-2},$

de modo que

$$\boxed{ \mathbf d(F) = (-2,1,1,0,0,0,0). }$$

Para energía: $[E]=ML^2T^{-2},$

luego

$$\boxed{ \mathbf d(E) = (-2,2,1,0,0,0,0). }$$

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-1}

Tenemos: $[x]=[x_0]=L.$

Además: $[v_0t] = LT^{-1}T = L.$

Y: $[at^2] = LT^{-2}T^2 = L.$

Por tanto:

$$\boxed{ [x] = [x_0] = [v_0t] = [at^2] = L. }$$

La expresión es dimensionalmente homogénea. El factor

$$\frac12$$

es un número puro y no introduce ninguna potencia de las dimensiones base.

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico-1}

La velocidad tiene dimensión: $[v]=LT^{-1}.$

También: $[v_0]=LT^{-1}.$

Pero: $[at^2] = LT^{-2}T^2 = L.$ Por tanto: $LT^{-1}\neq L.$ La ecuación intenta sumar una velocidad y una longitud. Cambiar el valor numérico de $a$ no altera: $[a]=LT^{-2}.$ Luego ningún ajuste numérico puede convertir

$$at^2$$

en una velocidad. El fallo es dimensional, no numérico.

### D. Síntesis {#fispm-c02-d.-suxedntesis-1}

Queremos: $[Q] = ML^2T^{-2}.$

Como: $[m^\alpha v^\beta] = M^\alpha (LT^{-1})^\beta,$

obtenemos: $[Q] = M^\alpha L^\beta T^{-\beta}.$

Igualamos exponentes con: $M^1L^2T^{-2}.$ Para masa: $\alpha=1.$ Para longitud: $\beta=2.$ Para tiempo: $-\beta=-2,$

que es compatible con: $\beta=2.$

Por tanto:

$$\boxed{ \alpha=1,\qquad \beta=2. }$$

La forma dimensional es: $Q=Cmv^2.$ Sin embargo, el análisis dimensional no determina $C$. Tampoco demuestra que una magnitud física concreta llamada energía deba depender exactamente de $mv^2$ en todo modelo y régimen. El razonamiento dimensional determinó los exponentes compatibles con la dimensión objetivo bajo las hipótesis dadas.

La identificación física de $Q$, el valor de $C$ y el régimen de validez requieren información adicional.

Esta separación es el objetivo de la práctica:

$$\boxed{ \text{restricción dimensional} \neq \text{ley física completa}. }$$

[]{#variar-el-método}

### Variar el método {#fispm-c02-variar-el-muxe9todo}

El ejercicio anterior usó una dimensión objetivo conocida.

Podemos variar el problema de tres maneras.

[]{#variación-1-ocultar-una-dimensión}

#### Variación 1 --- Ocultar una dimensión {#fispm-c02-variaciuxf3n-1-ocultar-una-dimensiuxf3n}

Dar una ecuación y pedir la dimensión de una constante desconocida.

[]{#variación-2-ocultar-un-exponente}

#### Variación 2 --- Ocultar un exponente {#fispm-c02-variaciuxf3n-2-ocultar-un-exponente}

Dar una forma como $Q=AX^\alpha Y^\beta$

y usar homogeneidad para restringir $\alpha,\beta$.

[]{#variación-3-insertar-un-término-defectuoso}

#### Variación 3 --- Insertar un término defectuoso {#fispm-c02-variaciuxf3n-3-insertar-un-tuxe9rmino-defectuoso}

Dar una ecuación casi correcta y pedir localizar exactamente el primer término incompatible.

Las tres variaciones practican actividades cognitivas distintas:

- reconstrucción;

- inferencia;

- diagnóstico.

El análisis dimensional se vuelve más potente cuando el lector puede pasar de una a otra sin depender de una plantilla memorizada.

[]{#red-conceptual}

### Red conceptual {#fispm-c02-red-conceptual}

§7 conecta directamente con lo ya construido:

$$\boxed{ \text{§1 cambio de unidad} \to \text{§5 dimensión} \to \text{§6 homogeneidad} \to \text{§7 auditoría}. }$$

Y prepara:

$$\boxed{ \text{§8 cantidades de dimensión uno} }$$

porque funciones como seno, exponencial y logaritmo requieren un análisis especial de sus argumentos;

$$\boxed{ \text{§10–§12 inferencia dimensional y semejanza} }$$

porque las firmas dimensionales pueden organizarse como ecuaciones lineales entre exponentes. La firma dimensional introducida aquí será, por tanto, una herramienta reutilizable y no una notación decorativa.

[]{#qué-debe-haber-cambiado-en-la-comprensión}

### Qué debe haber cambiado en la comprensión {#fispm-c02-quuxe9-debe-haber-cambiado-en-la-comprensiuxf3n}

Al cerrar la sección, el lector no debería limitarse a saber «comprobar unidades».

Debe poder:

1.  representar una magnitud mediante su firma dimensional;

2.  traducir productos, cocientes y potencias a operaciones con firmas;

3.  auditar sumas e igualdades usando la Proposición 2;

4.  localizar un término dimensionalmente incompatible;

5.  distinguir un fallo dimensional de uno algebraico o físico;

6.  explicar por qué pasar el control dimensional no demuestra una ley;

7.  reconocer cuándo el análisis dimensional solo restringe una forma y cuándo se necesita información física adicional.

Podemos condensar el método completo:

$$\boxed{\begin{gathered} \text{significado} \to \text{dimensión}\\[2pt]\Downarrow\\[2pt]\text{firma} \to \text{operación}\\[2pt]\Downarrow\\[2pt]\text{comparación} \to \text{diagnóstico}\\[2pt]\Downarrow\\[2pt]\text{control físico}. \end{gathered}}$$

La siguiente sección aborda la frontera que hemos pospuesto desde §6 (§[8](#fispm-c02-cantidades-de-dimensiuxf3n-uno)).

Allí veremos por qué «adimensional» no significa «sin significado físico» y por qué los argumentos de ciertas funciones requieren un tratamiento especial.

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-2 label="fispm-c02-notas-y-fuentes-2"}

[]{#cantidades-de-dimensión-uno}

[]{#fispm-t1-c02-s08}

[]{#fpm-i-02-s08}

## 8. Cantidades de dimensión uno {#fispm-c02-cantidades-de-dimensiuxf3n-uno}

[]{#intuir-adimensional-no-significa-sin-física}

### Intuir: «adimensional» no significa «sin física» {#fispm-c02-intuir-adimensional-no-significa-sin-fuxedsica}

Consideremos estas cantidades:

- el índice de refracción de un medio;

- el número de Mach;

- una fracción de masa;

- un ángulo plano;

- el número de vueltas de una bobina.

Todas tienen una característica común: su dimensión es

$$1.$$

Pero no significan lo mismo. Un índice de refracción no es un ángulo. Un ángulo no es un conteo. Una fracción de masa no es un número de Mach.

Por tanto, la primera intuición que debemos corregir es:

$$\boxed{ \text{dimensión uno} \neq \text{ausencia de significado físico}. }$$

El VIM conserva históricamente el término «cantidad adimensional», pero recomienda entenderlo como una **cantidad de dimensión uno**: todos sus exponentes dimensionales son cero. Además, advierte que estas cantidades transmiten más información que un número desnudo.[^28]

[]{#fig:I-02-R04}

<figure id="fig-fpm-v04-i-02-r04" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R04.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R04.svg" alt="El ángulo como razón geométrica. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="334" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.5.** En radianes, $\theta=s/R$. Un arco de longitud igual al radio determina un radián. Ser una razón de longitudes no vuelve intercambiables el ángulo y cualquier otra cantidad de dimensión uno. Véase §[8](#fispm-c02-cantidades-de-dimensiuxf3n-uno).

</figcaption>

</figure>

[]{#precisar-cantidad-de-dimensión-uno}

### Precisar: cantidad de dimensión uno {#fispm-c02-precisar-cantidad-de-dimensiuxf3n-uno}

**Definición 20 --- Cantidad de dimensión uno** Una **cantidad de dimensión uno** es una magnitud cuya expresión dimensional tiene todos sus exponentes iguales a cero:

$$[Q] = T^0L^0M^0I^0\Theta^0N^0J^0 = 1.$$

En términos de firmas dimensionales, $\mathbf d(Q) = (0,0,0,0,0,0,0).$ Esta definición no dice que $Q$ carezca de contenido físico. Dice que su valor no cambia mediante factores asociados a una reescala independiente de las unidades base.

**Principio 15 --- Dimensión uno no borra la semántica** Dos cantidades pueden tener dimensión uno y, sin embargo, pertenecer a tipos físicos diferentes, requerir convenciones distintas y desempeñar papeles distintos dentro de un modelo.

[]{#representar-cociente-de-magnitudes-del-mismo-tipo}

### Representar: cociente de magnitudes del mismo tipo {#fispm-c02-representar-cociente-de-magnitudes-del-mismo-tipo}

Una fuente frecuente de cantidades de dimensión uno es el cociente de dos magnitudes del mismo tipo. Si

$$R=\frac{Q_1}{Q_2}$$

y

$$[Q_1]=[Q_2],$$

entonces $[R] = \frac{[Q_1]}{[Q_2]} = 1.$ Por ejemplo, si

$$R=\frac{\ell_1}{\ell_2},$$

entonces $[R] = \frac{L}{L} = 1.$

Esto explica muchas razones relativas. Pero no toda cantidad de dimensión uno debe interpretarse simplemente como «una división entre dos números parecidos».

El VIM incluye también:

- ángulo plano;

- ángulo sólido;

- conteos;

- número de Mach;

- índice de refracción.

La igualdad dimensional no colapsa estas interpretaciones.

[]{#una-razón-conserva-información-sobre-qué-se-comparó}

### Una razón conserva información sobre qué se comparó {#fispm-c02-una-razuxf3n-conserva-informaciuxf3n-sobre-quuxe9-se-comparuxf3}

Supongamos $R=\frac{2\,\mathrm m}{1\,\mathrm m}=2.$ El valor final es numéricamente $2$.

Pero la construcción física fue:

$$\text{longitud} \div \text{longitud}.$$

Si en cambio contamos dos partículas, obtenemos también el número

$$2,$$

pero la procedencia conceptual es diferente.

Así:

$$\boxed{ \text{mismo número} \not\Rightarrow \text{misma cantidad física}. }$$

Esta observación generaliza §2: la semántica no puede reconstruirse desde el valor numérico final.

[]{#la-unidad-coherente-es-uno}

### La unidad coherente es uno {#fispm-c02-la-unidad-coherente-es-uno}

Para una cantidad de dimensión uno, la unidad SI derivada coherente es

$$1.$$

Normalmente el símbolo $1$ no se escribe. Por ejemplo, un índice de refracción puede aparecer como $n=1.50$

y no como $n=1.50\,1.$ Sin embargo, el hecho de que la unidad coherente sea uno no significa que cualquier convención de representación sea irrelevante. El VIM señala que algunas cantidades de dimensión uno emplean unidades especiales o cocientes convencionales.[^29]

[]{#porcentajes-y-razones-escaladas}

### Porcentajes y razones escaladas {#fispm-c02-porcentajes-y-razones-escaladas}

Una fracción

$$r=0.25$$

puede expresarse también como $25\%.$ El símbolo

$$\%$$

representa el factor

$$10^{-2}.$$

Por tanto, $25\% = 25\times10^{-2} = 0.25.$

Análogamente, $1\,\mathrm{mmol/mol} = 10^{-3}.$

Aquí aparece una distinción útil:

$$\boxed{ \text{unidad de dimensión uno} \neq \text{factor numérico necesariamente igual a }1. }$$

La unidad coherente es uno, pero podemos emplear unidades o convenciones escaladas para comunicar mejor ciertos valores.

[]{#el-ángulo-plano-el-caso-que-obliga-a-pensar}

### El ángulo plano: el caso que obliga a pensar {#fispm-c02-el-uxe1ngulo-plano-el-caso-que-obliga-a-pensar}

El ángulo plano es una cantidad de dimensión uno en el SI. Su unidad coherente es el **radián**: $\mathrm{rad}.$ Geométricamente, para un círculo de radio $r$ y arco de longitud $s$, $\theta = \frac{s}{r}\,\mathrm{rad}.$ Como $[s]=[r]=L,$

la razón

$$\frac{s}{r}$$

tiene dimensión uno. Pero la SI Brochure advierte que identificar sin más

$$\mathrm{rad} = \frac{\mathrm m}{\mathrm m}$$

puede ser engañoso: un ángulo no es simplemente cualquier razón de dos longitudes.[^30]

Por eso conviene mantener explícitamente

$$\mathrm{rad}$$

cuando ayuda a conservar el significado físico.

**Definición 21 --- Ángulo plano en radianes** Para una circunferencia de radio $r$, el valor angular en radianes asociado a un arco de longitud $s$ es la razón

$$\theta=\frac{s}{r},$$

acompañada por la interpretación geométrica de ángulo plano y expresada coherentemente en radianes. La definición no identifica «ángulo» con «razón de longitudes» como tipos de magnitud. La razón construye su medida radian.

[]{#el-radián-es-dimensión-uno-pero-no-es-semánticamente-vacío}

### El radián es dimensión uno, pero no es semánticamente vacío {#fispm-c02-el-radiuxe1n-es-dimensiuxf3n-uno-pero-no-es-semuxe1nticamente-vacuxedo}

Tenemos $[\theta]=1.$ Sin embargo, $30^\circ$

y

$$\frac{\pi}{6}\,\mathrm{rad}$$

representan el mismo ángulo con convenciones distintas. La relación exacta es $360^\circ=2\pi\,\mathrm{rad}.$ El grado no es unidad SI, aunque su uso está ampliamente establecido. El valor numérico depende de la unidad angular: $30 \neq \frac{\pi}{6}.$ Así, incluso una cantidad de dimensión uno puede presentar una transformación no trivial de valor numérico al cambiar su unidad.

Esto refuerza una idea de §1:

$$\boxed{ \text{dimensión} \neq \text{unidad} \neq \text{valor numérico}. }$$

[]{#ángulo-sólido}

### Ángulo sólido {#fispm-c02-uxe1ngulo-suxf3lido}

El ángulo sólido también tiene dimensión uno. Su unidad coherente es el estereorradián: $\mathrm{sr}.$ Para una esfera de radio $r$, si una región de su superficie tiene área $A$, puede escribirse

$$\Omega = \frac{A}{r^2}\,\mathrm{sr}.$$

Dimensionalmente, $[\Omega] = \frac{L^2}{L^2} = 1.$

Pero, igual que con el radián, la SI Brochure advierte que

$$\mathrm{sr} = \frac{\mathrm{m^2}}{\mathrm{m^2}}$$

no debe interpretarse como si cualquier razón de áreas fuese automáticamente un ángulo sólido.[^31]

La interpretación geométrica sigue siendo indispensable.

[]{#poner-a-prueba-una-intuición-1-significa-intercambiable}

### Poner a prueba una intuición: ¿«1» significa intercambiable? {#fispm-c02-poner-a-prueba-una-intuiciuxf3n-1-significa-intercambiable}

Consideremos: $n=1.50$

para un índice de refracción, y

$$M=1.50$$

para un número de Mach.

Ambos tienen dimensión uno.

Ambos pueden tener el mismo valor numérico. Sin embargo,

$$n=M$$

no constituye automáticamente una igualdad física significativa. El número coincide. La dimensión coincide. El tipo de magnitud no necesariamente.

Por tanto:

$$\boxed{ \text{mismo valor} + \text{misma dimensión} \not\Rightarrow \text{misma magnitud}. }$$

[]{#funciones-no-algebraicas-aparece-una-nueva-exigencia}

### Funciones no algebraicas: aparece una nueva exigencia {#fispm-c02-funciones-no-algebraicas-aparece-una-nueva-exigencia}

En §6 dejamos pendiente expresiones como

$$\sin x,$$

$$e^x,$$

$$\log x.$$

Consideremos la serie formal

$$e^x = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots.$$

Para poder sumar los términos, la Proposición 2 exige que todos tengan la misma dimensión. El primer término,

$$1,$$

tiene dimensión uno. Por tanto necesitamos

$$[x]=1.$$

La misma lógica aparece en las expansiones de seno y coseno.

**Principio 16 --- Los argumentos de funciones trascendentes deben ser dimensionalmente apropiados** En expresiones físicas con funciones como exponencial, logaritmo, seno o coseno, el argumento debe construirse como una cantidad de dimensión uno, o mediante una convención equivalente que haga explícita la normalización necesaria.

[]{#exponencial-por-qué-aparece-ttau}

### Exponencial: por qué aparece $t/\tau$ {#fispm-c02-exponencial-por-quuxe9-aparece-ttau}

Consideremos

$$Q(t)=Q_0e^{-t/\tau}.$$

Aquí

$$[t]=T$$

y

$$[\tau]=T.$$

Por tanto, $\left[\frac{t}{\tau}\right] = 1.$ El exponente es dimensionalmente admisible. En cambio, $Q(t)=Q_0e^{-t}$

es una escritura incompleta si $t$ representa un tiempo dimensional y no se ha declarado una normalización. Cambiar segundos por minutos alteraría el número introducido en la exponencial de una manera que no representa la misma relación física.

[]{#logaritmo-no-tomar-logaritmos-de-una-magnitud-desnuda}

### Logaritmo: no tomar logaritmos de una magnitud desnuda {#fispm-c02-logaritmo-no-tomar-logaritmos-de-una-magnitud-desnuda}

Supongamos que escribimos

$$\log p,$$

donde $p$ es una presión. Si cambiamos de pascales a kilopascales, el valor numérico de $p$ cambia por un factor. La expresión depende de la unidad elegida.

En cambio, $\log\left(\frac{p}{p_0}\right)$

utiliza una razón de presiones: $\left[\frac{p}{p_0}\right] = 1.$ Al cambiar coherentemente la unidad de ambas, $\frac{\{p\}'}{\{p_0\}'} = \frac{\{p\}}{\{p_0\}},$

de modo que el argumento permanece invariante.

[]{#seno-y-coseno-el-papel-especial-del-radián}

### Seno y coseno: el papel especial del radián {#fispm-c02-seno-y-coseno-el-papel-especial-del-radiuxe1n}

En matemática escribimos

$$\sin\theta.$$

Si $\theta$ representa un ángulo físico, el número que entra en la función matemática debe corresponder a su medida coherente, normalmente en radianes. Por ejemplo, $30^\circ = \frac{\pi}{6}\,\mathrm{rad}.$ La función matemática recibe entonces el número $\frac{\pi}{6}.$

Esto explica por qué el radián ocupa una posición especial en cálculo y física.

No porque el grado sea «incorrecto», sino porque las fórmulas analíticas estándar de derivación, series y límites utilizan naturalmente la medida angular coherente en radianes.

[]{#no-toda-cantidad-de-dimensión-uno-es-una-razón-continua}

### No toda cantidad de dimensión uno es una razón continua {#fispm-c02-no-toda-cantidad-de-dimensiuxf3n-uno-es-una-razuxf3n-continua}

El VIM incluye entre las cantidades de dimensión uno los **números de entidades**.[^32]

Por ejemplo, $N=20$

puede representar un conteo. La dimensión es uno. Pero este objeto no tiene la misma estructura operacional que una fracción continua como $0.20.$

La dimensión no codifica:

- discreción;

- continuidad;

- carácter angular;

- interpretación probabilística;

- interpretación geométrica.

De nuevo:

$$\boxed{ \text{dimensión} \neq \text{estructura física completa}. }$$

[]{#mapa-conceptual}

### Mapa conceptual {#fispm-c02-mapa-conceptual}

  Cantidad               Origen conceptual         Dimensión   Representación frecuente
  ---------------------- ------------------------- ----------- --------------------------
  razón de longitudes    cociente de mismo tipo    $1$         número
  fracción de masa       cociente de masas         $1$         número, %
  índice de refracción   relación física           $1$         número
  número de Mach         cociente de velocidades   $1$         número
  ángulo plano           estructura geométrica     $1$         rad, °
  ángulo sólido          estructura geométrica     $1$         sr
  conteo                 número de entidades       $1$         entero

La tabla evita dos simplificaciones:

1.  creer que todas son «solo ratios»;

2.  creer que, por ser adimensionales, son intercambiables.

[]{#autoexplicación}

### Autoexplicación {#fispm-c02-autoexplicaciuxf3n}

**Pausa de autoexplicación** Explica sin consultar la tabla:

1.  por qué $30^\circ$ y $\pi/6\,\mathrm{rad}$ tienen valores numéricos diferentes pero representan el mismo ángulo;

2.  por qué $\log(p)$ es problemático si $p$ conserva dimensión de presión;

3.  por qué dos cantidades con firma dimensional nula no tienen por qué pertenecer al mismo tipo físico.

Una respuesta satisfactoria debe distinguir:

$$\text{dimensión}, \quad \text{unidad}, \quad \text{valor numérico}, \quad \text{significado físico}.$$

[]{#práctica-guiada-1}

### Práctica guiada {#fispm-c02-pruxe1ctica-guiada-1}

**Ejercicio 18 --- Reconocer dimensión uno**

**Objetivo:** `Recuperación → Consolidación`

**Intenta primero: 3--5 min antes de leer la solución.**

Determina cuáles tienen dimensión uno:

1.  $\ell_1/\ell_2$;

2.  $v/c$, con $v,c$ velocidades;

3.  $m/V$;

4.  $p/p_0$;

5.  $A/r^2$;

6.  $t/\tau$;

7.  $F/(ma)$.

Para cada caso explica además qué estructura física podría representar.

**Solución**

1.

$$\left[\frac{\ell_1}{\ell_2}\right]=1.$$

Razón de longitudes.

1.

$$\left[\frac vc\right]=1.$$

Razón de velocidades.

1.

$$\left[\frac mV\right]=ML^{-3}.$$

No tiene dimensión uno.

1.

$$\left[\frac p{p_0}\right]=1.$$

Razón entre presiones.

1.

$$\left[\frac A{r^2}\right]=1.$$

Con interpretación geométrica adecuada puede intervenir en un ángulo sólido.

1.

$$\left[\frac t\tau\right]=1.$$

Escala temporal normalizada.

1.

Como $[F]=[ma]=MLT^{-2},$

tenemos $\left[\frac{F}{ma}\right]=1.$ El punto común es dimensional, pero las interpretaciones siguen siendo distintas.

**Ejercicio 19 --- Diagnóstico de argumentos de funciones**

**Objetivo:** `Diagnóstico — transferencia`

**Intenta primero: 3--5 min antes de leer la solución.**

Examina:

1.  $e^{-t}$;

2.  $e^{-t/\tau}$;

3.  $\log p$;

4.  $\log(p/p_0)$;

5.  $\sin(\omega t)$, con $[\omega]=T^{-1}$;

6.  $\sin(vt)$, con $[v]=LT^{-1}$.

Decide cuáles son dimensionalmente admisibles tal como están escritas.

**Solución**

**1.** Si $[t]=T$, el argumento conserva dimensión temporal. No está normalizado.

**2.**

$$\left[\frac t\tau\right]=1.$$

Es admisible.

**3.** $\log p$ depende de la unidad usada para representar $p$. No es una forma física completa tal como está escrita.

**4.**

$$\left[\frac p{p_0}\right]=1.$$

Es admisible.

**5.**

$$[\omega t]=1.$$

Es admisible.

**6.**

$$[vt]=L.$$

No es admisible como argumento directo del seno sin una escala adicional de longitud. Por ejemplo: $\sin\left(\frac{vt}{\ell_0}\right)$

sí posee argumento de dimensión uno.

Regla:

$$\boxed{ \text{antes de una función trascendente, auditar la dimensión de su argumento}. }$$

[]{#variar}

### Variar {#fispm-c02-variar}

Si aparece

$$e^{-kx},$$

la homogeneidad del argumento exige

$$[kx]=1.$$

Por tanto, $[k]=[x]^{-1}.$

Si

$$[x]=L,$$

entonces $[k]=L^{-1}.$ Lo mismo ocurre en

$$\sin(kx).$$

El análisis dimensional no determina el valor de $k$, pero sí la dimensión necesaria.

[]{#conectar}

### Conectar {#fispm-c02-conectar}

Las cantidades de dimensión uno permiten construir **parámetros que comparan escalas**. En §9 estudiaremos órdenes de magnitud y estimaciones. En §§10--11 aparecerán razones que controlan aproximaciones y semejanza.

En §12, Buckingham $\Pi$ reorganizará problemas mediante combinaciones

$$\Pi_1,\Pi_2,\ldots,\Pi_k$$

de dimensión uno.

Por tanto:

$$\boxed{ \text{la física compara escalas mediante combinaciones de dimensión uno}. }$$

[]{#síntesis-5}

### Síntesis {#fispm-c02-suxedntesis-5}

Una cantidad de dimensión uno satisface $[Q]=1,$

o

$$\mathbf d(Q)=\mathbf 0.$$

Pero:

$$\boxed{ [Q]=1 \not\Rightarrow Q\text{ es semánticamente vacío}. }$$

Puede representar una razón, un ángulo, un conteo, una fracción, un índice o un parámetro de semejanza. Además, $e^x,\qquad \log x,\qquad \sin x$

exigen argumentos construidos de manera dimensionalmente apropiada.

La regla práctica queda:

$$\boxed{ \text{función trascendente} \longrightarrow \text{auditar primero el argumento}. }$$

El siguiente paso será el §[9](#fispm-c02-escalas-caracteruxedsticas-y-uxf3rdenes-de-magnitud).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-3 label="fispm-c02-notas-y-fuentes-3"}

[]{#escalas-características-y-órdenes-de-magnitud}

[]{#fispm-t1-c02-s09}

[]{#fpm-i-02-s09}

## 9. Escalas características y órdenes de magnitud {#fispm-c02-escalas-caracteruxedsticas-y-uxf3rdenes-de-magnitud}

[]{#intuir-una-magnitud-puede-ser-grande-o-pequeña-solo-respecto-de-una-escala}

### Intuir: una magnitud puede ser grande o pequeña solo respecto de una escala {#fispm-c02-intuir-una-magnitud-puede-ser-grande-o-pequeuxf1a-solo-respecto-de-una-escala}

Decir que

$$\ell=2\,\mathrm{mm}$$

es «pequeño» no tiene todavía un significado físico completo.

Dos milímetros pueden ser enormes frente al espesor de una membrana y diminutos frente al tamaño de una habitación.

La afirmación correcta necesita una referencia:

$$\boxed{ \text{grande o pequeño} \quad \text{respecto de una escala}. }$$

Ésta es la función de una **escala característica**.

[]{#escala-característica}

### Escala característica {#fispm-c02-escala-caracteruxedstica}

**Definición 32 --- Escala característica** Una **escala característica** de una magnitud $Q$ en un modelo es un valor de referencia $Q_\ast$, del mismo tipo de magnitud, elegido para representar el tamaño relevante de $Q$ en el fenómeno o régimen considerado.

La escala puede proceder de:

- una dimensión geométrica del sistema;

- un parámetro del modelo;

- una condición inicial;

- un valor experimental representativo;

- una escala impuesta externamente.

No tiene por qué ser un promedio ni el valor máximo. Su elección depende de la pregunta física.

**Principio 27 --- Una escala característica pertenece al modelo** Una escala característica no se deduce únicamente de la dimensión de una magnitud. Debe justificarse por la geometría, el régimen, los datos o la estructura física del problema.

[]{#representar-una-magnitud-respecto-de-su-escala}

### Representar una magnitud respecto de su escala {#fispm-c02-representar-una-magnitud-respecto-de-su-escala}

Si $Q_\ast$ es una escala característica de $Q$, la razón

$$\widehat Q = \frac{Q}{Q_\ast}$$

tiene dimensión uno: $[\widehat Q]=1.$

Entonces podemos interpretar: $\widehat Q\ll1$

como «$Q$ es pequeño respecto de $Q_\ast$», $\widehat Q\sim1$

como «$Q$ es comparable con $Q_\ast$», y

$$\widehat Q\gg1$$

como «$Q$ es grande respecto de $Q_\ast$». La escala convierte una comparación cualitativa en una afirmación cuantitativa.

[]{#varias-escalas-características-pueden-coexistir}

### Varias escalas características pueden coexistir {#fispm-c02-varias-escalas-caracteruxedsticas-pueden-coexistir}

Un sistema puede contener más de una longitud relevante. Por ejemplo: $L,\qquad \ell.$

Si

$$\ell\ll L,$$

la razón

$$\varepsilon=\frac{\ell}{L}$$

es pequeña. Pero no existe una regla universal que obligue a elegir $L$ como escala y no $\ell$. La elección depende de la representación que resulte útil.

Si normalizamos con $L$: $\frac{\ell}{L}=\varepsilon.$ Si normalizamos con $\ell$: $\frac{L}{\ell}=\varepsilon^{-1}.$ Ambas descripciones contienen la misma comparación.

[]{#década-decimal}

### Década decimal {#fispm-c02-duxe9cada-decimal}

Conservaremos una herramienta numérica de la primera redacción.

**Definición 22 --- Década decimal** Si

$$x=a\times10^n, \qquad 1\le a<10,$$

llamaremos **década decimal** de $x$ al intervalo

$$[10^n,10^{n+1}).$$

La década registra una escala decimal gruesa.

[]{#orden-de-magnitud}

### Orden de magnitud {#fispm-c02-orden-de-magnitud}

**Definición 23 --- Orden de magnitud** Para $x>0$, el **orden de magnitud decimal** de $x$ será la potencia de diez más cercana en escala logarítmica.

Si

$$x=a\times10^n, \qquad 1\le a<10,$$

entonces:

$$\operatorname{OM}(x)= \begin{cases} 10^n, & 1\le a<\sqrt{10},\\ 10^{n+1}, & \sqrt{10}<a<10. \end{cases}$$

En el caso frontera

$$a=\sqrt{10},$$

declararemos explícitamente la convención utilizada. El umbral aparece porque el punto medio multiplicativo satisface: $\frac{x}{10^n} = \frac{10^{n+1}}{x},$

de donde: $x=\sqrt{10}\,10^n.$

**Principio 17 --- Un orden de magnitud describe escala, no precisión** Informar un orden de magnitud identifica una escala multiplicativa dominante. No equivale a conocer con precisión el coeficiente numérico ni sus cifras significativas.

[]{#escala-característica-y-orden-de-magnitud-no-son-lo-mismo}

### Escala característica y orden de magnitud no son lo mismo {#fispm-c02-escala-caracteruxedstica-y-orden-de-magnitud-no-son-lo-mismo}

Una escala característica es una **elección física del modelo**. Un orden de magnitud es una **clasificación numérica aproximada**. Por ejemplo, podemos adoptar: $L_\ast=2.4\,\mathrm m$

como escala geométrica relevante. Su orden de magnitud puede ser: $10^0\,\mathrm m.$ Pero reemplazar sistemáticamente $L_\ast$ por $1\,\mathrm m$ puede perder información física útil.

Así:

$$\boxed{ \text{escala característica} \neq \text{orden de magnitud}. }$$

[]{#escalas-derivadas}

### Escalas derivadas {#fispm-c02-escalas-derivadas}

Si elegimos una escala de longitud: $L_\ast$

y una escala de tiempo: $T_\ast,$

aparece naturalmente una escala de velocidad: $V_\ast = \frac{L_\ast}{T_\ast}.$

También una escala de aceleración: $A_\ast = \frac{L_\ast}{T_\ast^2}.$ La estructura dimensional permite construir escalas coherentes a partir de las escalas básicas seleccionadas por el modelo.

[]{#ejemplo-movimiento-en-una-pista}

### Ejemplo: movimiento en una pista {#fispm-c02-ejemplo-movimiento-en-una-pista}

Supongamos que una pista tiene longitud característica: $L_\ast=400\,\mathrm m$

y que el fenómeno que estudiamos dura típicamente: $T_\ast=50\,\mathrm s.$

La escala de velocidad asociada es:

$$V_\ast = \frac{400\,\mathrm m}{50\,\mathrm s} = 8\,\mathrm{m\,s^{-1}}.$$

Una velocidad: $v=2\,\mathrm{m\,s^{-1}}$

corresponde a: $\widehat v = \frac{v}{V_\ast} = 0.25.$ Una velocidad: $v=10\,\mathrm{m\,s^{-1}}$

corresponde a: $\widehat v = 1.25.$ La comparación no depende de memorizar si $2$ o $10$ son números «grandes». Depende del fenómeno y de su escala.

[]{#parámetros-pequeños-y-grandes}

### Parámetros pequeños y grandes {#fispm-c02-paruxe1metros-pequeuxf1os-y-grandes}

Las razones de escala permiten identificar regímenes.

Si: $\varepsilon = \frac{\ell}{L} \sim10^{-3},$

entonces: $\varepsilon\ll1.$

Esa información puede justificar más adelante aproximaciones del tipo:

$$\text{corrección de orden }\varepsilon$$

o:

$$\text{efecto dominante frente a uno pequeño}.$$

El análisis dimensional no decide por sí solo qué términos pueden descartarse. Pero ayuda a construir el parámetro que hace cuantitativa la pregunta.

[]{#estimación-física-puente-hacia-el-capítulo-siguiente}

### Estimación física: puente hacia el capítulo siguiente {#fispm-c02-estimaciuxf3n-fuxedsica-puente-hacia-el-capuxedtulo-siguiente}

Conservamos el concepto ya activado:

**Definición 24 --- Estimación física** Una **estimación física** es una inferencia cuantitativa aproximada construida a partir de un modelo simplificado, valores representativos, cotas o escalas plausibles, con las hipótesis y la precisión pretendida explícitas.

**Principio 18 --- Toda estimación debe exponer su modelo** Una estimación es auditable solo si hace visibles las cantidades intermedias, los valores representativos y las simplificaciones utilizadas.

En este capítulo usaremos esta idea solo para **identificar escalas**.

El desarrollo sistemático de:

- estimaciones tipo Fermi;

- cifras significativas;

- cotas experimentales;

- incertidumbre;

- propagación de incertidumbres;

- precisión de resultados;

pertenece al capítulo 3.

[]{#práctica-guiada-2}

### Práctica guiada {#fispm-c02-pruxe1ctica-guiada-2}

**Ejercicio 20 --- Elegir y usar escalas características**

**Objetivo:** `Consolidación → Diagnóstico → Síntesis`

**Intenta primero: 3--5 min antes de leer la solución.**

Un movimiento ocurre en una región cuya longitud relevante es $L_\ast=100\,\mathrm m$

y durante un tiempo característico

$$T_\ast=20\,\mathrm s.$$

1.  Construye la escala de velocidad $V_\ast$.

2.  Para $x=5\,\mathrm m$, $t=4\,\mathrm s$ y $v=15\,\mathrm{m\,s^{-1}}$, calcula

$$\widehat x=\frac{x}{L_\ast}, \qquad \widehat t=\frac{t}{T_\ast}, \qquad \widehat v=\frac{v}{V_\ast}.$$

1.  Clasifica cada razón como pequeña, de orden uno o grande respecto de la escala elegida.

2.  Explica por qué cambiar metros por centímetros no cambia $\widehat x$.

3.  Si elegimos por error una escala $L_\ast=1\,\mathrm{mm}$ para el mismo fenómeno, explica qué se vuelve pedagógicamente poco útil aunque la razón siga siendo matemáticamente válida.

**Solución**

La escala de velocidad es:

$$V_\ast = \frac{L_\ast}{T_\ast} = \frac{100\,\mathrm m}{20\,\mathrm s} = 5\,\mathrm{m\,s^{-1}}.$$

Entonces:

$$\widehat x = \frac{5}{100} = 0.05,$$

$$\widehat t = \frac{4}{20} = 0.2,$$

y: $\widehat v = \frac{15}{5} = 3.$

Respecto de las escalas elegidas:

- $\widehat x=0.05$ es pequeño;

- $\widehat t=0.2$ es menor que uno pero no extremadamente pequeño;

- $\widehat v=3$ es de orden uno en sentido de escala: difiere de la referencia solo por un factor de pocos.

Si escribimos: $x=500\,\mathrm{cm}$

y: $L_\ast=10\,000\,\mathrm{cm},$

la razón sigue siendo: $\widehat x = \frac{500}{10\,000} = 0.05.$ La variable reducida es independiente de la unidad coherentemente utilizada. Finalmente, elegir: $L_\ast=1\,\mathrm{mm}$

daría: $\widehat x=5000.$ La razón es correcta, pero la escala elegida no representa bien el tamaño característico del fenómeno y oculta en lugar de revelar su estructura.

[]{#autoexplicación-1}

### Autoexplicación {#fispm-c02-autoexplicaciuxf3n-1}

**Pausa de autoexplicación** Explica:

1.  por qué una escala característica no es una unidad;

2.  por qué una escala característica no es necesariamente un orden de magnitud;

3.  qué información añade la razón $Q/Q_\ast$;

4.  por qué una mala elección de escala puede ser matemáticamente válida y físicamente poco informativa.

[]{#conectar-1}

### Conectar {#fispm-c02-conectar-1}

Hemos construido razones: $\widehat Q=\frac{Q}{Q_\ast}$

de dimensión uno.

La siguiente sección convertirá esta idea en un procedimiento sistemático para reescribir modelos completos (§[10](#fispm-c02-adimensionalizaciuxf3n-e-inferencia-dimensional)).

La pregunta dejará de ser únicamente:

> ¿cuál es el tamaño característico de cada variable?

y pasará a ser:

> ¿cómo reescribimos todo el problema en variables de dimensión uno y qué parámetros sobreviven a esa reducción?

[]{#adimensionalización-e-inferencia-dimensional}

[]{#fispm-t1-c02-s10}

[]{#fpm-i-02-s10}

## 10. Adimensionalización e inferencia dimensional {#fispm-c02-adimensionalizaciuxf3n-e-inferencia-dimensional}

[]{#intuir-cambiar-de-unidades-no-debería-cambiar-la-forma-esencial-del-problema}

### Intuir: cambiar de unidades no debería cambiar la forma esencial del problema {#fispm-c02-intuir-cambiar-de-unidades-no-deberuxeda-cambiar-la-forma-esencial-del-problema}

En §9 elegimos escalas características. Ahora utilizaremos esas escalas para construir variables de dimensión uno.

Si:

$$x$$

es una longitud y: $L_\ast$

una escala característica de longitud, definimos: $\widehat x = \frac{x}{L_\ast}.$

El número $\widehat x$ ya no pregunta «¿cuántos metros mide $x$?».

Pregunta:

> ¿qué tamaño tiene $x$ respecto de la escala física elegida?

[]{#variable-adimensionalizada}

### Variable adimensionalizada {#fispm-c02-variable-adimensionalizada}

**Definición 33 --- Variable adimensionalizada** Dada una magnitud $Q$ y una escala característica $Q_\ast$ del mismo tipo, la variable

$$\widehat Q=\frac{Q}{Q_\ast}$$

es una **variable adimensionalizada** o **variable reducida** asociada a esa escala.

Tenemos: $[\widehat Q]=1.$ Pero $\widehat Q$ conserva una interpretación: expresa el tamaño relativo de $Q$.

[]{#adimensionalización}

### Adimensionalización {#fispm-c02-adimensionalizaciuxf3n}

**Definición 34 --- Adimensionalización** La **adimensionalización** de una relación o modelo es el procedimiento de elegir escalas características para sus magnitudes y reescribirlo en términos de variables de dimensión uno, de modo que queden explícitos los parámetros adimensionales que controlan su forma.

La operación tiene dos objetivos:

1.  separar unidades y escalas convencionales de la estructura esencial;

2.  identificar los parámetros de dimensión uno que no pueden eliminarse mediante una simple elección de escalas.

**Principio 28 --- Adimensionalizar reorganiza la física; no la elimina** Al adimensionalizar desaparecen las unidades explícitas de las variables reducidas, pero permanecen las relaciones físicas y los parámetros de dimensión uno que controlan el modelo.

[]{#ejemplo-elemental-una-relación-cinemática}

### Ejemplo elemental: una relación cinemática {#fispm-c02-ejemplo-elemental-una-relaciuxf3n-cinemuxe1tica}

Consideremos: $x=x_0+vt.$

Elegimos: $L_\ast, \qquad T_\ast,$

y construimos: $V_\ast=\frac{L_\ast}{T_\ast}.$

Definimos:

$$\widehat x=\frac{x}{L_\ast}, \qquad \widehat x_0=\frac{x_0}{L_\ast},$$

$$\widehat t=\frac{t}{T_\ast}, \qquad \widehat v=\frac{v}{V_\ast}.$$

Sustituyendo:

$$L_\ast\widehat x = L_\ast\widehat x_0 + V_\ast T_\ast \widehat v\widehat t.$$

Como: $V_\ast T_\ast=L_\ast,$

obtenemos:

$$\boxed{ \widehat x = \widehat x_0 + \widehat v\widehat t. }$$

La ecuación conserva su forma y todas las variables son de dimensión uno.

[]{#qué-puede-quedar-después-de-adimensionalizar}

### Qué puede quedar después de adimensionalizar {#fispm-c02-quuxe9-puede-quedar-despuuxe9s-de-adimensionalizar}

No siempre podemos absorber todos los parámetros. Si una relación contiene varias escalas independientes, aparecerán razones como: $\varepsilon=\frac{\ell}{L}$

[]{#fig:I-02-R05}

<figure id="fig-fpm-v04-i-02-r05" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R05.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R05.svg" alt="Comparar usando referencias declaradas. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="403" height="250" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.6.** Si $L=L_*\lambda$, una familia de áreas semejantes satisface $A/A_*=\lambda^2$. Ambas razones son adimensionales; su interpretación conserva las referencias físicas $L_*$ y $A_*$. Véase §[10](#fispm-c02-adimensionalizaciuxf3n-e-inferencia-dimensional).

</figcaption>

</figure>

o combinaciones más complejas.

Esos parámetros son importantes precisamente porque **sobreviven** al cambio de unidades y a la elección de escalas.

La adimensionalización prepara así el camino hacia:

- inferencia dimensional;

- semejanza;

- grupos $\Pi$ de Buckingham.

[]{#inferir-puede-la-dimensión-ayudarnos-a-construir-una-fórmula}

### Inferir: ¿puede la dimensión ayudarnos a construir una fórmula? {#fispm-c02-inferir-puede-la-dimensiuxf3n-ayudarnos-a-construir-una-fuxf3rmula}

Hasta ahora hemos usado la dimensión principalmente como herramienta de control.

Dada una expresión como $x=x_0+vt,$

podemos preguntar si es homogénea.

Pero supongamos ahora que conocemos solamente esto:

- una magnitud objetivo $Q$;

- varias magnitudes relevantes $X_1,\ldots,X_n$;

- sus dimensiones.

¿Podemos obtener alguna información sobre la forma de $Q$ antes de conocer una ley completa?

La respuesta es sí, con una restricción importante. Si suponemos que la dependencia puede escribirse como un producto de potencias, $Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},$

la homogeneidad dimensional produce ecuaciones para los exponentes

$$\alpha_1,\ldots,\alpha_n.$$

Esto no deriva toda la física. Pero puede restringir fuertemente la forma posible.

[]{#representar-del-problema-físico-a-un-ansatz}

### Representar: del problema físico a un ansatz {#fispm-c02-representar-del-problema-fuxedsico-a-un-ansatz}

La palabra **ansatz** designará aquí una forma propuesta de solución o dependencia que todavía debe justificarse.

**Definición 25 --- Ansatz dimensional monomial** Un **ansatz dimensional monomial** para una magnitud $Q$ en función de magnitudes $X_1,\ldots,X_n$ es una expresión de la forma

$$Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},$$

donde $C$ tiene dimensión uno y los exponentes $\alpha_i$ son desconocidos que se determinan, cuando es posible, imponiendo homogeneidad dimensional. La hipótesis monomial no es una consecuencia automática de la física. Es una elección de clase funcional.

Por tanto, el razonamiento correcto tiene dos capas:

$$\boxed{ \text{hipótesis de forma} + \text{restricciones dimensionales} }$$

[]{#precisar-convertir-dimensiones-en-ecuaciones-para-exponentes}

### Precisar: convertir dimensiones en ecuaciones para exponentes {#fispm-c02-precisar-convertir-dimensiones-en-ecuaciones-para-exponentes}

Supongamos que

$$[Q]=T^aL^bM^c,$$

y

$$[X_i]=T^{a_i}L^{b_i}M^{c_i}.$$

Si

$$Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},$$

entonces $[Q] = [X_1]^{\alpha_1}\cdots[X_n]^{\alpha_n}.$ Por tanto,

$$T^aL^bM^c = T^{\sum a_i\alpha_i} L^{\sum b_i\alpha_i} M^{\sum c_i\alpha_i}.$$

La igualdad de dimensiones exige igualdad de exponentes base a base:

$$a=\sum_i a_i\alpha_i,$$

$$b=\sum_i b_i\alpha_i,$$

$$c=\sum_i c_i\alpha_i.$$

Aparece así un **sistema lineal de ecuaciones para los exponentes**.

No necesitamos todavía teoría formal de espacios vectoriales para utilizarlo.

[]{#firma-dimensional-y-sistema-lineal}

### Firma dimensional y sistema lineal {#fispm-c02-firma-dimensional-y-sistema-lineal}

Con la firma de §7, $\mathbf d(Q) = (a,b,c,\ldots),$

la relación anterior puede escribirse conceptualmente como

$$\boxed{ \mathbf d(Q) = \alpha_1\mathbf d(X_1) + \cdots + \alpha_n\mathbf d(X_n). }$$

Ésta es la razón por la que introdujimos las firmas dimensionales. El problema de inferir potencias se convierte en un problema de combinar vectores de exponentes.

**Principio 19 --- La inferencia dimensional restringe exponentes dentro de una clase funcional elegida** El análisis dimensional puede determinar o restringir los exponentes de un ansatz monomial, pero no justifica por sí solo que la dependencia física real pertenezca a esa clase funcional.

[]{#primer-ejemplo-período-de-un-péndulo-simple}

### Primer ejemplo: período de un péndulo simple {#fispm-c02-primer-ejemplo-peruxedodo-de-un-puxe9ndulo-simple}

Supongamos que buscamos una escala temporal $T_p$ para un péndulo y aceptamos, como modelo dimensional mínimo, que depende de:

- una longitud $\ell$;

- una aceleración gravitatoria $g$.

Proponemos

$$T_p=C\ell^\alpha g^\beta.$$

Sabemos:

$$[T_p]=T,$$

$$[\ell]=L,$$

$$[g]=LT^{-2}.$$

Entonces $T = L^\alpha (LT^{-2})^\beta.$ Por tanto, $T = L^{\alpha+\beta}T^{-2\beta}.$

Igualamos exponentes. Para longitud: $\alpha+\beta=0.$ Para tiempo: $-2\beta=1.$ De la segunda, $\beta=-\frac12.$ Luego

$$\alpha=\frac12.$$

Por tanto,

$$\boxed{ T_p=C\sqrt{\frac{\ell}{g}}. }$$

El análisis dimensional ha fijado la dependencia en $\ell$ y $g$.

No ha determinado $C$.

[]{#qué-falta-en-el-ejemplo-del-péndulo}

### Qué falta en el ejemplo del péndulo {#fispm-c02-quuxe9-falta-en-el-ejemplo-del-puxe9ndulo}

La teoría del péndulo simple para oscilaciones pequeñas conduce a

$$T_p=2\pi\sqrt{\frac{\ell}{g}}.$$

Pero la dimensión solo produjo

$$T_p=C\sqrt{\frac{\ell}{g}}.$$

Por tanto,

$$\boxed{ C=2\pi }$$

no es una conclusión del análisis dimensional.

Debe provenir de información adicional:

- ecuación de movimiento;

- aproximación de ángulo pequeño;

- solución matemática del modelo;

- o evidencia experimental.

Éste es un ejemplo limpio de la frontera del método.

[]{#poner-a-prueba-una-intuición-la-dimensión-determina-siempre-una-única-forma}

### Poner a prueba una intuición: ¿la dimensión determina siempre una única forma? {#fispm-c02-poner-a-prueba-una-intuiciuxf3n-la-dimensiuxf3n-determina-siempre-una-uxfanica-forma}

No.

Supongamos que queremos una cantidad $Q$ con dimensión

$$[Q]=L$$

a partir de dos longitudes $x$ e $y$. Un ansatz monomial sería

$$Q=Cx^\alpha y^\beta.$$

La dimensión exige solamente

$$\alpha+\beta=1.$$

Hay infinitas soluciones:

$$(\alpha,\beta)=(1,0),$$

$$(0,1),$$

$$\left(\frac12,\frac12\right),$$

y muchas más. Por tanto, la información dimensional es insuficiente para elegir una sola dependencia.

[]{#la-aparición-de-una-libertad-adimensional}

### La aparición de una libertad adimensional {#fispm-c02-la-apariciuxf3n-de-una-libertad-adimensional}

Escribamos

$$\beta=1-\alpha.$$

Entonces $Q=Cx^\alpha y^{1-\alpha}.$

Factorizamos $y$: $Q = y\,C\left(\frac xy\right)^\alpha.$ La razón

$$\frac xy$$

tiene dimensión uno.

Esto sugiere una forma mucho más general:

$$\boxed{ Q = y\,\Phi\left(\frac xy\right), }$$

donde $\Phi$ es una función de dimensión uno. La dimensión no determina $\Phi$. Este fenómeno será central en Buckingham $\Pi$.

[]{#segunda-definición-libertad-funcional-adimensional}

### Segunda definición: libertad funcional adimensional {#fispm-c02-segunda-definiciuxf3n-libertad-funcional-adimensional}

**Definición 26 --- Libertad funcional adimensional** Existe **libertad funcional adimensional** cuando las restricciones dimensionales permiten multiplicar una forma dimensionalmente admisible por una función arbitraria de una o más combinaciones de dimensión uno sin alterar la dimensión total.

Por ejemplo, si

$$[Q]=L$$

y

$$[x]=[y]=L,$$

entonces $Q=y\,\Phi(x/y)$

es dimensionalmente admisible para cualquier función adecuada $\Phi$. La física debe determinar cuál, si alguna, es la función correcta.

**Principio 20 --- Toda libertad adimensional marca información física aún no determinada** Cuando el análisis dimensional deja una función arbitraria de cantidades de dimensión uno, esa libertad no es un defecto del método: identifica exactamente la parte de la relación que las dimensiones no pueden fijar.

[]{#resultado-formal-condición-para-un-ansatz-monomial}

### Resultado formal: condición para un ansatz monomial {#fispm-c02-resultado-formal-condiciuxf3n-para-un-ansatz-monomial}

**Proposición 3 --- Criterio de homogeneidad para un ansatz monomial**

Sea

$$Q=C\prod_{i=1}^n X_i^{\alpha_i},$$

con $[C]=1$. Escribamos las dimensiones respecto de una base dimensional $D_1,\ldots,D_r$ como $[Q] = \prod_{j=1}^r D_j^{q_j},$

y

$$[X_i] = \prod_{j=1}^r D_j^{a_{ji}}.$$

Entonces el ansatz es dimensionalmente homogéneo si y solo si, para cada $j$,

$$\boxed{ q_j = \sum_{i=1}^n a_{ji}\alpha_i. }$$

[]{#demostración-2}

#### Demostración {#fispm-c02-demostraciuxf3n-2}

Partimos de

$$Q=C\prod_{i=1}^n X_i^{\alpha_i}.$$

Como $[C]=1,$

obtenemos $[Q] = \prod_{i=1}^n [X_i]^{\alpha_i}.$

Sustituyendo

$$[X_i] = \prod_{j=1}^rD_j^{a_{ji}},$$

resulta

$$[Q] = \prod_{i=1}^n \left( \prod_{j=1}^rD_j^{a_{ji}} \right)^{\alpha_i}.$$

Reagrupando por dimensión base, $[Q] = \prod_{j=1}^r D_j^{\sum_i a_{ji}\alpha_i}.$ Pero también

$$[Q] = \prod_{j=1}^rD_j^{q_j}.$$

Dos expresiones dimensionales son iguales exactamente cuando coinciden los exponentes de cada dimensión base. Por tanto, $q_j = \sum_{i=1}^n a_{ji}\alpha_i$

para todo $j$.

Recíprocamente, si estas igualdades se cumplen, entonces las dos expresiones dimensionales coinciden y el ansatz es homogéneo.

$$\boxed{\text{QED}}$$

[]{#lectura-de-la-proposición-3}

### Lectura de la Proposición 3 {#fispm-c02-lectura-de-la-proposiciuxf3n-3}

La Proposición 3 no dice que toda ley física tenga forma monomial.

Dice algo más preciso:

> **si** elegimos una forma monomial, **entonces** la homogeneidad es equivalente a resolver un sistema lineal para sus exponentes.

La hipótesis y la conclusión deben permanecer separadas.

[]{#hipótesis-estructural}

#### Hipótesis estructural {#fispm-c02-hipuxf3tesis-estructural}

$$Q=C\prod_iX_i^{\alpha_i}.$$

[]{#restricción-dimensional}

#### Restricción dimensional {#fispm-c02-restricciuxf3n-dimensional}

$$q_j=\sum_i a_{ji}\alpha_i.$$

[]{#información-no-obtenida}

#### Información no obtenida {#fispm-c02-informaciuxf3n-no-obtenida}

- validez física del ansatz;

- valor de $C$;

- presencia de funciones adimensionales adicionales;

- régimen de validez;

- signos o correcciones aditivas.

**Pausa de autoexplicación** Explica por qué la Proposición 3 es un teorema matemático correcto y, al mismo tiempo, no constituye una ley física.

Una respuesta adecuada debe distinguir la hipótesis monomial de la información dimensional.

[]{#segundo-ejemplo-período-orbital}

### Segundo ejemplo: período orbital {#fispm-c02-segundo-ejemplo-peruxedodo-orbital}

Siguiendo un ejemplo clásico de teoría dimensional,[^33] supongamos que una escala temporal orbital $T_o$ depende de:

- radio orbital $r$;

- masa central $M$;

- constante gravitacional $G$.

Proponemos

$$T_o=Cr^\alpha M^\beta G^\gamma.$$

Las dimensiones son:

$$[T_o]=T,$$

$$[r]=L,$$

$$[M]=M,$$

$$[G]=L^3M^{-1}T^{-2}.$$

Entonces

$$T = L^\alpha M^\beta \left(L^3M^{-1}T^{-2}\right)^\gamma.$$

Agrupando:

$$T = L^{\alpha+3\gamma} M^{\beta-\gamma} T^{-2\gamma}.$$

Igualamos exponentes:

$$\alpha+3\gamma=0,$$

$$\beta-\gamma=0,$$

$$-2\gamma=1.$$

De la última: $\gamma=-\frac12.$

Entonces $\beta=-\frac12,$

y

$$\alpha=\frac32.$$

Por tanto,

$$\boxed{ T_o = C\sqrt{\frac{r^3}{GM}}. }$$

La dimensión fija los exponentes dentro del ansatz.

No fija $C$ ni demuestra que $r,M,G$ sean las únicas variables físicamente relevantes.

[]{#el-problema-de-las-variables-omitidas}

### El problema de las variables omitidas {#fispm-c02-el-problema-de-las-variables-omitidas}

Ésta es una limitación decisiva. El análisis dimensional opera sobre **las variables que le damos**. Si omitimos una magnitud relevante, podemos obtener una fórmula dimensionalmente impecable y físicamente incompleta.

Por ejemplo, si un fenómeno depende además de una viscosidad $\mu$ y no la incluimos, ningún cálculo dimensional posterior puede recuperar mágicamente esa variable.

Por eso la inferencia debe empezar con una pregunta física:

$$\boxed{ \text{¿qué variables son plausiblemente relevantes para el fenómeno?} }$$

La selección de variables es parte de la modelización, no del álgebra dimensional.

[]{#un-no-ejemplo-deducir-demasiado-de-una-solución-única}

### Un no-ejemplo: deducir demasiado de una solución única {#fispm-c02-un-no-ejemplo-deducir-demasiado-de-una-soluciuxf3n-uxfanica}

Supongamos que el sistema dimensional produce una única pareja

$$(\alpha,\beta).$$

Sería incorrecto concluir:

> «Hemos demostrado la ley física.»

Lo único demostrado es:

> dentro del ansatz monomial elegido y con las variables incluidas, existe una única combinación de exponentes compatible con las dimensiones.

Todavía puede faltar:

- una constante numérica;

- una función de parámetros adimensionales no incluidos explícitamente;

- otra clase funcional;

- una variable relevante omitida.

[]{#variar-si-añadimos-una-variable-de-dimensión-uno}

### Variar: si añadimos una variable de dimensión uno {#fispm-c02-variar-si-auxf1adimos-una-variable-de-dimensiuxf3n-uno}

Volvamos al péndulo. Si además del largo $\ell$ y de $g$ incluimos un ángulo inicial $\theta_0$, con

$$[\theta_0]=1,$$

la dimensión ya no puede fijar completamente la dependencia.

Podemos escribir

$$\boxed{ T_p = \sqrt{\frac{\ell}{g}}\,\Phi(\theta_0). }$$

Para oscilaciones pequeñas, $\Phi(\theta_0) \approx 2\pi.$ Para amplitudes mayores, la función cambia. La dimensión no puede decidir esa dependencia porque $\theta_0$ ya es de dimensión uno. Este ejemplo muestra por qué los parámetros adimensionales concentran información física que el análisis dimensional deja libre.

[]{#ejercicios-práctica-guiada}

### Ejercicios práctica guiada {#fispm-c02-ejercicios-pruxe1ctica-guiada}

**Ejercicio 21 --- Adimensionalizar una relación cinemática**

**Objetivo:** `Consolidación`

**Intenta primero: 3--5 min antes de leer la solución.**

Considera: $x=x_0+vt.$

Elige escalas $L_\ast$ y $T_\ast$ y define: $V_\ast=\frac{L_\ast}{T_\ast}.$

1.  Introduce

$$\widehat x=\frac{x}{L_\ast}, \quad \widehat x_0=\frac{x_0}{L_\ast}, \quad \widehat t=\frac{t}{T_\ast}, \quad \widehat v=\frac{v}{V_\ast}.$$

1.  Demuestra que la relación se convierte en

$$\boxed{ \widehat x=\widehat x_0+\widehat v\,\widehat t. }$$

1.  Explica por qué todas las variables con sombrero tienen dimensión uno.

2.  Explica qué ocurriría si se eligiera una escala de velocidad distinta de $L_\ast/T_\ast$.

**Solución**

Sustituimos:

$$x=L_\ast\widehat x, \qquad x_0=L_\ast\widehat x_0,$$

$$v=V_\ast\widehat v, \qquad t=T_\ast\widehat t.$$

Entonces:

$$L_\ast\widehat x = L_\ast\widehat x_0 + V_\ast T_\ast \widehat v\widehat t.$$

Como: $V_\ast T_\ast=L_\ast,$

obtenemos:

$$L_\ast\widehat x = L_\ast \left( \widehat x_0+\widehat v\widehat t \right).$$

Dividiendo por $L_\ast$:

$$\boxed{ \widehat x=\widehat x_0+\widehat v\widehat t. }$$

Además: $[\widehat x] = \frac{L}{L} = 1,$

y análogamente:

$$[\widehat x_0] = [\widehat t] = [\widehat v] = 1.$$

Si eligiéramos una escala de velocidad arbitraria $V_\ast'$, aparecería el parámetro

$$\frac{V_\ast'T_\ast}{L_\ast}.$$

La elección

$$V_\ast=L_\ast/T_\ast$$

absorbe ese factor y revela una forma reducida más simple.

**Ejercicio 22 --- Qué sobrevive a la adimensionalización**

**Objetivo:** `Diagnóstico → Síntesis`

**Intenta primero: 3--5 min antes de leer la solución.**

Sean $x$ e $y$ dos longitudes y $Q$ otra longitud. Buckingham y la homogeneidad permiten una forma $Q=y\,\Phi\left(\frac{x}{y}\right).$

1.  Define:

$$\widehat Q=\frac{Q}{y}, \qquad \xi=\frac{x}{y}.$$

1.  Reescribe la relación en forma adimensional.

2.  Explica qué información ha desaparecido y cuál permanece.

3.  ¿Puede el análisis dimensional determinar $\Phi$?

4.  Aplica la misma lectura al péndulo:

$$P= \sqrt{\frac{\ell}{g}} \Psi(\varphi_0).$$

**Solución**

Dividiendo por $y$:

$$\boxed{ \widehat Q=\Phi(\xi). }$$

Tanto: $\widehat Q$

como:

$$\xi$$

tienen dimensión uno. La unidad concreta de longitud ha desaparecido de la forma reducida. Pero no ha desaparecido la física: permanece en la función $\Phi$ y en el significado de la razón $x/y$.

El análisis dimensional no determina $\Phi$. Para el péndulo podemos definir: $\widehat P = P\sqrt{\frac g\ell}.$

Entonces:

$$\boxed{ \widehat P=\Psi(\varphi_0). }$$

La adimensionalización ha aislado exactamente la dependencia que no puede fijarse solo con dimensiones.

[]{#autoexplicación-2}

### Autoexplicación {#fispm-c02-autoexplicaciuxf3n-2}

**Pausa de autoexplicación** Sin revisar los ejemplos, responde:

1.  ¿qué hipótesis adicional introducimos al escribir un ansatz monomial?;

2.  ¿por qué una solución única para los exponentes no equivale a una ley física única?;

3.  ¿qué significa que aparezca una función $\Phi$ de una cantidad de dimensión uno?;

4.  ¿qué información proviene de las dimensiones y cuál proviene de la modelización?

[]{#conectar-con-buckingham-pi}

### Conectar con Buckingham $\Pi$ {#fispm-c02-conectar-con-buckingham-pi}

La estructura que acabamos de encontrar puede resumirse así. A veces las dimensiones fijan una combinación monomial básica: $Q_0.$ Pero si existen combinaciones independientes de dimensión uno,

$$\Pi_1,\ldots,\Pi_k,$$

la forma más general puede contener

$$\boxed{ Q = Q_0\,\Phi(\Pi_1,\ldots,\Pi_k). }$$

Ésta es precisamente la dirección que formalizará el teorema $\Pi$.

No lo demostramos todavía.

§10 ha construido el problema que ese teorema resolverá.

[]{#síntesis-6}

### Síntesis {#fispm-c02-suxedntesis-6}

La inferencia dimensional comienza con una elección física de variables y una hipótesis de forma. Para un ansatz

$$Q=C\prod_iX_i^{\alpha_i},$$

la homogeneidad se convierte en un sistema lineal para los exponentes:

$$\boxed{ \mathbf d(Q) = \sum_i\alpha_i\mathbf d(X_i). }$$

La Proposición 3 demuestra que resolver ese sistema es exactamente la condición de homogeneidad del ansatz monomial.

Pero la dimensión no determina por sí sola:

- la selección correcta de variables;

- la validez del ansatz;

- constantes numéricas adimensionales;

- funciones de parámetros de dimensión uno;

- el régimen físico de validez.

Por tanto:

$$\boxed{ \text{inferencia dimensional} = \text{restricción estructural}, \not\equiv \text{derivación completa de una ley}. }$$

El siguiente paso será el §[11](#fispm-c02-semejanza-escalamiento-y-cambio-de-escala).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-4 label="fispm-c02-notas-y-fuentes-4"}

[]{#semejanza-escalamiento-y-cambio-de-escala}

[]{#fispm-t1-c02-s11}

[]{#fpm-i-02-s11}

## 11. Semejanza, escalamiento y cambio de escala {#fispm-c02-semejanza-escalamiento-y-cambio-de-escala}

[]{#intuir-hacer-un-sistema-más-grande-no-significa-multiplicarlo-todo-por-el-mismo-número}

### Intuir: hacer un sistema más grande no significa multiplicarlo todo por el mismo número {#fispm-c02-intuir-hacer-un-sistema-muxe1s-grande-no-significa-multiplicarlo-todo-por-el-mismo-nuxfamero}

Imaginemos dos modelos geométricamente semejantes de una misma figura. Si todas las longitudes del segundo son $\lambda$

veces las del primero, es natural escribir

$$L'\!=\lambda L.$$

Pero el área no cambia por el mismo factor: $A'\!=\lambda^2A.$ Y el volumen cambia como $V'\!=\lambda^3V.$ Por tanto,

$$\boxed{ \text{cambiar de escala} \neq \text{multiplicar todas las magnitudes por el mismo factor}. }$$

Cada magnitud responde al reescalado según su estructura.

Ésta es la idea básica de una **ley de escalamiento**.

[]{#representar-una-familia-de-sistemas-relacionados-por-un-parámetro}

### Representar: una familia de sistemas relacionados por un parámetro {#fispm-c02-representar-una-familia-de-sistemas-relacionados-por-un-paruxe1metro}

Introduciremos un parámetro positivo

$$\lambda>0.$$

Una magnitud $X$ puede transformarse según

$$X(\lambda)=\lambda^sX_0,$$

donde $s$ describe cómo responde al cambio de escala. Por ejemplo: $L(\lambda)=\lambda L_0$

tiene exponente de escalamiento $1$; $A(\lambda)=\lambda^2A_0$

tiene exponente $2$; $V(\lambda)=\lambda^3V_0$

tiene exponente $3$.

**Definición 27 --- Ley de escalamiento** Una **ley de escalamiento** para una magnitud $Q$ respecto de un parámetro positivo $\lambda$ es una relación que describe cómo cambia $Q$ al variar $\lambda$. Cuando tiene la forma

$$Q(\lambda)=\lambda^sQ(1),$$

llamaremos $s$ **exponente de escalamiento** de $Q$ respecto de esa transformación.

[]{#dimensión-y-escalamiento-no-son-lo-mismo}

### Dimensión y escalamiento no son lo mismo {#fispm-c02-dimensiuxf3n-y-escalamiento-no-son-lo-mismo}

Debemos separar dos ideas.

La **dimensión** responde:

> ¿cómo depende una magnitud de las magnitudes base del sistema dimensional?

El **escalamiento** responde:

> ¿cómo cambia una magnitud dentro de una familia concreta de transformaciones?

Una longitud tiene dimensión

$$L.$$

Pero no toda longitud física debe escalar necesariamente como $\lambda^1$

en cualquier problema. Por ejemplo, en una transformación podríamos duplicar el radio de un objeto y mantener fija otra longitud externa. Ambas tienen dimensión $L$, pero sus leyes de escalamiento son distintas.

[]{#fig:I-02-R03}

<figure id="fig-fpm-v04-i-02-r03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R03.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R03.svg" alt="La escala lineal no es la escala de área. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="340" height="292" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.7.** En figuras semejantes, duplicar todas las longitudes multiplica el área por cuatro y el volumen por ocho. La comparación exige conservar la forma; el dibujo ilustra la relación de áreas. Véase §[11](#fispm-c02-semejanza-escalamiento-y-cambio-de-escala).

</figcaption>

</figure>

[]{#fig:I-02-N03}

<figure id="fig-fpm-v04-i-02-n03" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-N03.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-N03.svg" alt="Escalamiento del péndulo. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="450" height="253" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.8.** Para el péndulo ideal a pequeña amplitud y $g$ fijo, $T/T_0=\sqrt{L/L_0}$. Duplicar la longitud multiplica el período por $\sqrt2$, dentro de ese régimen. Véase §[11](#fispm-c02-semejanza-escalamiento-y-cambio-de-escala).

</figcaption>

</figure>

Por tanto,

$$\boxed{ \text{misma dimensión} \not\Rightarrow \text{mismo exponente de escalamiento}. }$$

**Principio 21 --- El escalamiento pertenece al modelo de transformación** La dimensión de una magnitud es una propiedad relativa al sistema dimensional; su exponente de escalamiento depende además de qué familia de sistemas o transformación física estamos comparando.

[]{#escalamiento-geométrico-uniforme}

### Escalamiento geométrico uniforme {#fispm-c02-escalamiento-geomuxe9trico-uniforme}

Consideremos una familia de cuerpos geométricamente semejantes en la que toda longitud lineal se multiplica por $\lambda.$ Entonces: $L'\!=\lambda L.$ Un área construida como producto de dos longitudes satisface $A'\! = (\lambda L_1)(\lambda L_2) = \lambda^2A.$

Un volumen construido como producto de tres longitudes satisface $V'\! = \lambda^3V.$

Así obtenemos:

$$\boxed{ L\sim\lambda, \qquad A\sim\lambda^2, \qquad V\sim\lambda^3. }$$

Aquí el símbolo

$$\sim$$

indica dependencia de escala, no igualdad exacta entre magnitudes.

[]{#consecuencia-superficie-frente-a-volumen}

### Consecuencia: superficie frente a volumen {#fispm-c02-consecuencia-superficie-frente-a-volumen}

Para objetos geométricamente semejantes, $\frac AV \sim \frac{\lambda^2}{\lambda^3}.$ Por tanto,

$$\boxed{ \frac AV \sim \lambda^{-1}. }$$

Al aumentar el tamaño lineal de un objeto, disminuye su razón superficie/volumen. Si duplicamos la escala lineal, $\lambda=2,$

entonces $\frac{(A/V)'}{A/V} = \frac12.$ Esta conclusión es geométrica.

No necesitamos todavía afirmar ninguna consecuencia biológica, térmica o mecánica concreta.

Esas aplicaciones requerirían modelos físicos adicionales.

[]{#masa-bajo-densidad-constante}

### Masa bajo densidad constante {#fispm-c02-masa-bajo-densidad-constante}

Supongamos ahora que comparamos objetos semejantes fabricados con un material de densidad constante

$$\rho.$$

Como $m=\rho V,$

si

$$\rho'=\rho$$

y

$$V'=\lambda^3V,$$

entonces $m' = \rho V' = \lambda^3m.$ Por tanto,

$$\boxed{ m\sim\lambda^3 }$$

bajo las hipótesis:

- semejanza geométrica;

- misma densidad.

Si cambia el material o la densidad, esta ley deja de seguirse automáticamente.

[]{#precisar-semejanza-respecto-de-un-modelo}

### Precisar: semejanza respecto de un modelo {#fispm-c02-precisar-semejanza-respecto-de-un-modelo}

Dos objetos pueden tener la misma forma geométrica y no comportarse físicamente de manera semejante. Para hablar de semejanza física necesitamos declarar qué estructura queremos preservar.[^34]

**Definición 28 --- Semejanza respecto de un modelo** Dos realizaciones de un modelo son **semejantes respecto de un conjunto declarado de variables y relaciones** cuando pueden relacionarse mediante transformaciones de escala que preservan la forma de esas relaciones y los parámetros de dimensión uno relevantes para la comparación.

Esta definición es deliberadamente relativa.

No existe una única noción universal de «ser semejante» para todos los propósitos físicos.

Podemos estudiar:

- semejanza geométrica;

- semejanza cinemática;

- semejanza dinámica;

- semejanza térmica;

según las variables y relaciones que el modelo conserve.

[]{#un-ejemplo-temporal-péndulos-semejantes}

### Un ejemplo temporal: péndulos semejantes {#fispm-c02-un-ejemplo-temporal-puxe9ndulos-semejantes}

En §10 obtuvimos, para el modelo elemental, $T_p = C\sqrt{\frac{\ell}{g}}.$

Supongamos ahora que mantenemos fijo $g$ y cambiamos

$$\ell'\!=\lambda\ell.$$

Entonces

$$T_p' = C\sqrt{\frac{\lambda\ell}{g}} = \lambda^{1/2}T_p.$$

Por tanto,

$$\boxed{ T_p\sim\lambda^{1/2}. }$$

Un péndulo cuatro veces más largo tiene, dentro de este modelo, $T_p'=2T_p.$ La longitud creció por un factor $4$. El período solo creció por un factor $2$.

[]{#otro-ejemplo-escala-orbital}

### Otro ejemplo: escala orbital {#fispm-c02-otro-ejemplo-escala-orbital}

En §10 obtuvimos

$$T_o = C\sqrt{\frac{r^3}{GM}}.$$

Si mantenemos fijos $G$ y $M$ y reescalamos

$$r'\!=\lambda r,$$

entonces

$$T_o' = C\sqrt{\frac{\lambda^3r^3}{GM}} = \lambda^{3/2}T_o.$$

Así,

$$\boxed{ T_o\sim r^{3/2} }$$

cuando $M$ permanece fija dentro del modelo.

Ésta es una ley de escala más informativa que una simple afirmación dimensional.

Nos dice cómo comparar dos miembros de una familia física.

[]{#teorema-elemental-de-escalamiento-monomial}

### Teorema elemental de escalamiento monomial {#fispm-c02-teorema-elemental-de-escalamiento-monomial}

**Proposición 4 --- Escalamiento de un ansatz monomial**

Sea

$$Q=C\prod_{i=1}^nX_i^{\alpha_i},$$

donde $C$ permanece invariante bajo una transformación parametrizada por $\lambda>0$.

Supongamos que cada variable escala como $X_i(\lambda)=\lambda^{s_i}X_i(1).$

Entonces

$$\boxed{ Q(\lambda) = \lambda^{\sum_i\alpha_is_i}Q(1). }$$

Por tanto, el exponente de escalamiento de $Q$ es

$$\boxed{ s_Q = \sum_i\alpha_is_i. }$$

[]{#demostración-3}

#### Demostración {#fispm-c02-demostraciuxf3n-3}

Sustituimos las leyes de escala de las variables:

$$Q(\lambda) = C\prod_i \left( \lambda^{s_i}X_i(1) \right)^{\alpha_i}.$$

Separando los factores de $\lambda$,

$$Q(\lambda) = C \left( \prod_i \lambda^{\alpha_is_i} \right) \left( \prod_iX_i(1)^{\alpha_i} \right).$$

Como

$$\prod_i \lambda^{\alpha_is_i} = \lambda^{\sum_i\alpha_is_i},$$

obtenemos

$$Q(\lambda) = \lambda^{\sum_i\alpha_is_i} C\prod_iX_i(1)^{\alpha_i}.$$

Pero

$$C\prod_iX_i(1)^{\alpha_i} = Q(1).$$

Luego

$$\boxed{ Q(\lambda) = \lambda^{\sum_i\alpha_is_i}Q(1). }$$

$$\boxed{\text{QED}}$$

[]{#leer-la-proposición-4-correctamente}

### Leer la Proposición 4 correctamente {#fispm-c02-leer-la-proposiciuxf3n-4-correctamente}

La Proposición 4 no afirma que toda magnitud física siga una potencia de $\lambda$.

La conclusión depende de dos hipótesis:

1.  que la relación tenga la forma monomial indicada;

2.  que conozcamos cómo escala cada variable $X_i$.

Así, la Proposición 4 traduce una ley monomial en una ley de escala.

No crea por sí sola la relación física.

[]{#cantidades-de-dimensión-uno-e-invariantes-de-semejanza}

### Cantidades de dimensión uno e invariantes de semejanza {#fispm-c02-cantidades-de-dimensiuxf3n-uno-e-invariantes-de-semejanza}

Supongamos que bajo una transformación

$$X'\!=\lambda^aX$$

y

$$Y'\!=\lambda^bY.$$

La combinación

$$\Pi = X^pY^q$$

será invariante bajo el reescalado si

$$ap+bq=0.$$

Entonces $\Pi'=\Pi.$

Esto es distinto de decir solamente que

$$[\Pi]=1.$$

Una cantidad puede tener dimensión uno y aun cambiar durante una transformación física concreta. Para que funcione como **invariante de semejanza**, debe además conservar su valor bajo la familia de escalamiento elegida.

**Principio 22 --- Semejanza exige preservar los parámetros adimensionales relevantes** En una comparación por semejanza, no basta con que una combinación tenga dimensión uno: los parámetros adimensionales que controlan el modelo deben conservar valores compatibles entre los sistemas comparados.

Esta idea anticipa directamente los grupos $\Pi$ de §12.

[]{#poner-a-prueba-dimensión-uno-no-implica-invariancia-de-escala}

### Poner a prueba: dimensión uno no implica invariancia de escala {#fispm-c02-poner-a-prueba-dimensiuxf3n-uno-no-implica-invariancia-de-escala}

Sea

$$R=\frac{x}{y},$$

con

$$[x]=[y]=L.$$

Entonces $[R]=1.$ Pero supongamos que

$$x'\!=2x$$

y

$$y'\!=3y.$$

Entonces $R' = \frac{2x}{3y} = \frac23R.$ Por tanto, $R'\neq R.$ La cantidad es de dimensión uno, pero no es invariante bajo ese reescalado. En cambio, si

$$x'\!=\lambda x$$

y

$$y'\!=\lambda y,$$

entonces $R'=R.$ La semejanza depende del patrón de transformación.

[]{#diagnóstico-miniatura-geométrica-no-equivale-automáticamente-a-modelo-físico}

### Diagnóstico: miniatura geométrica no equivale automáticamente a modelo físico {#fispm-c02-diagnuxf3stico-miniatura-geomuxe9trica-no-equivale-automuxe1ticamente-a-modelo-fuxedsico}

Supongamos que construimos una maqueta a escala

$$1:10.$$

Todas las longitudes se reducen por $\lambda=\frac1{10}.$

Geométricamente, $A'\!=10^{-2}A,$

y

$$V'\!=10^{-3}V.$$

Si conservamos densidad, $m'\!=10^{-3}m.$ Pero de aquí no sigue que todos los tiempos, fuerzas o velocidades deban reducirse también por $10^{-1}.$ Cada una requiere su propia ley de escala. Una maqueta geométricamente semejante puede no ser dinámicamente semejante.

Esta distinción es central en modelos experimentales.

[]{#ejemplo-velocidad-bajo-escalamiento-de-longitud-y-tiempo}

### Ejemplo: velocidad bajo escalamiento de longitud y tiempo {#fispm-c02-ejemplo-velocidad-bajo-escalamiento-de-longitud-y-tiempo}

La velocidad satisface $v=\frac{L}{T}.$ Si una familia transforma

$$L'\!=\lambda^aL$$

y

$$T'\!=\lambda^bT,$$

entonces

$$v' = \frac{\lambda^aL}{\lambda^bT} = \lambda^{a-b}v.$$

Así,

$$\boxed{ s_v=a-b. }$$

La dimensión de $v$ sigue siendo

$$LT^{-1},$$

pero su exponente de escalamiento depende de los valores concretos

$$a,\ b.$$

Éste es otro modo de ver por qué dimensión y escalamiento no son sinónimos.

[]{#ejemplo-aceleración-bajo-un-escalamiento-general}

### Ejemplo: aceleración bajo un escalamiento general {#fispm-c02-ejemplo-aceleraciuxf3n-bajo-un-escalamiento-general}

Como $a_{\mathrm f} \sim \frac{L}{T^2},$

si

$$L'\!=\lambda^pL$$

y

$$T'\!=\lambda^qT,$$

entonces $a_{\mathrm f}' = \lambda^{p-2q}a_{\mathrm f}.$ Por tanto,

$$\boxed{ s_{a_{\mathrm f}}=p-2q. }$$

Si queremos preservar una aceleración externa fija, debemos imponer

$$p-2q=0.$$

Entonces $q=\frac p2.$

Para

$$p=1,$$

obtenemos $T\sim\lambda^{1/2},$

exactamente como en el escalamiento temporal del péndulo bajo gravedad fija.

[]{#autoexplicación-3}

### Autoexplicación {#fispm-c02-autoexplicaciuxf3n-3}

**Pausa de autoexplicación** Responde sin volver a los ejemplos:

1.  ¿por qué dos magnitudes con la misma dimensión pueden tener exponentes de escalamiento diferentes?;

2.  ¿qué hipótesis permiten deducir $m\sim\lambda^3$ para objetos semejantes?;

3.  ¿por qué una cantidad de dimensión uno puede no ser invariante bajo un cambio de escala?;

4.  ¿qué diferencia hay entre semejanza geométrica y semejanza física?

[]{#práctica-guiada-3}

### Práctica guiada {#fispm-c02-pruxe1ctica-guiada-3}

**Ejercicio 23 --- Escalar una familia de modelos**

**Objetivo:** `Síntesis`

**Intenta primero: 3--5 min antes de leer la solución.**

Considera una familia de cuerpos geométricamente semejantes construidos con el mismo material. La escala lineal cambia según

$$L'\!=\lambda L.$$

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-2}

Determina cómo escalan:

1.  área $A$;

2.  volumen $V$;

3.  masa $m$;

4.  razón $A/V$.

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-2}

Si una cantidad característica satisface $Q=Cm^\alpha L^\beta,$

demuestra usando la Proposición 4 que

$$Q'\! = \lambda^{3\alpha+\beta}Q.$$

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico-2}

Un estudiante afirma:

> «Una maqueta diez veces más pequeña tiene todas sus magnitudes físicas diez veces más pequeñas.»

Identifica el error.

### D. Síntesis {#fispm-c02-d.-suxedntesis-2}

Supón además que un proceso posee una escala temporal

$$T=C\sqrt{\frac{L}{g}},$$

con $g$ fijo.

Determina cómo cambia $T$ cuando

$$\lambda=\frac1{100}.$$

Explica por qué la respuesta no es $T'=\frac1{100}T.$

**Solución**

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-3}

Por semejanza geométrica,

$$A'\!=\lambda^2A,$$

$$V'\!=\lambda^3V.$$

Con el mismo material, $\rho'=\rho.$

Como $m=\rho V,$

resulta $m'\!=\lambda^3m.$

Finalmente,

$$\frac{A'}{V'} = \frac{\lambda^2A}{\lambda^3V} = \lambda^{-1}\frac AV.$$

Por tanto:

$$\boxed{ A\sim\lambda^2,\quad V\sim\lambda^3,\quad m\sim\lambda^3,\quad A/V\sim\lambda^{-1}. }$$

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-3}

Tenemos $Q=Cm^\alpha L^\beta.$

Como $m'\!=\lambda^3m$

y

$$L'\!=\lambda L,$$

entonces $Q' = C(\lambda^3m)^\alpha(\lambda L)^\beta.$

Así, $Q' = \lambda^{3\alpha+\beta} Cm^\alpha L^\beta.$

Luego

$$\boxed{ Q' = \lambda^{3\alpha+\beta}Q. }$$

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico-3}

El estudiante confunde una escala **lineal** con una regla universal para todas las magnitudes. Las áreas cambian como $\lambda^2,$

los volúmenes y masas bajo densidad fija como $\lambda^3,$

y otras magnitudes dependen de las relaciones físicas del modelo.

No existe una regla

$$Q'\!=\lambda Q$$

válida para toda magnitud.

### D. Síntesis {#fispm-c02-d.-suxedntesis-3}

Si

$$T=C\sqrt{\frac Lg}$$

y $g$ permanece fijo, entonces $T'\!=\lambda^{1/2}T.$

Con

$$\lambda=\frac1{100},$$

tenemos $\lambda^{1/2} = \frac1{10}.$ Por tanto,

$$\boxed{ T'=\frac1{10}T. }$$

El tiempo no disminuye cien veces porque su ley de escala no es lineal en $L$: $T\propto L^{1/2}.$

La conclusión sintetiza la sección:

$$\boxed{ \text{\parbox{.66\linewidth}{\centering el escalamiento de una magnitud viene de la estructura del modelo, no del tamaño lineal por sí solo}}. }$$

[]{#variar-escalamiento-simultáneo-de-varias-magnitudes}

### Variar: escalamiento simultáneo de varias magnitudes {#fispm-c02-variar-escalamiento-simultuxe1neo-de-varias-magnitudes}

Supongamos ahora que

$$r'\!=\lambda r$$

y

$$M'\!=\lambda^\mu M$$

en la relación orbital

$$T_o = C\sqrt{\frac{r^3}{GM}}.$$

Con $G$ fijo,

$$T_o' = \sqrt{ \frac{\lambda^3r^3} {G\lambda^\mu M} }\,C.$$

Por tanto,

$$\boxed{ T_o' = \lambda^{(3-\mu)/2}T_o. }$$

Distintos valores de $\mu$ producen familias de semejanza distintas.

Por ejemplo:

- si $\mu=0$, $T_o\sim\lambda^{3/2}$;

- si $\mu=3$, $T_o$ permanece invariante;

- si $\mu=1$, $T_o\sim\lambda$.

Esto muestra que una ley dimensional puede contener muchas reglas de escalamiento según qué variables se transformen conjuntamente.

[]{#conectar-con-el-teorema-pi}

### Conectar con el teorema $\Pi$ {#fispm-c02-conectar-con-el-teorema-pi}

§10 mostró que una relación dimensional puede dejar funciones arbitrarias de cantidades de dimensión uno.

§11 añade una nueva lectura:

esas cantidades pueden actuar como **invariantes de semejanza** cuando sus valores permanecen fijos a través de una familia de sistemas.

La estructura que buscamos es:

$$\boxed{ \text{variables dimensionales} \longrightarrow \text{combinaciones de dimensión uno} \longrightarrow \text{familias semejantes}. }$$

Buckingham $\Pi$ hará sistemática esta reducción.

En §12 preguntaremos:

> Dadas $n$ variables físicas construidas a partir de $r$ dimensiones independientes, ¿cuántas combinaciones de dimensión uno independientes podemos esperar?

[]{#síntesis-7}

### Síntesis {#fispm-c02-suxedntesis-7}

El cambio de escala se describe mediante leyes como $Q(\lambda)=\lambda^sQ(1).$

El exponente $s$ depende de:

- la relación física;

- las variables que cambian;

- las variables que permanecen fijas;

- el modelo de semejanza adoptado.

Para un ansatz monomial, $Q=C\prod_iX_i^{\alpha_i},$

si

$$X_i(\lambda)=\lambda^{s_i}X_i(1),$$

La Proposición 4 demuestra:

$$\boxed{ s_Q=\sum_i\alpha_is_i. }$$

Además,

$$\boxed{ \text{dimensión uno} \not\Rightarrow \text{invariante de escala}, }$$

y

$$\boxed{ \text{semejanza geométrica} \not\Rightarrow \text{semejanza física completa}. }$$

La semejanza exige declarar qué relaciones e invariantes queremos preservar.

El siguiente paso es el §[12](#fispm-c02-el-teorema-ux3c0-de-buckingham).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-5 label="fispm-c02-notas-y-fuentes-5"}

[]{#el-teorema-π-de-buckingham}

[]{#fispm-t1-c02-s12}

[]{#fpm-i-02-s12}

## 12. El teorema Π de Buckingham {#fispm-c02-el-teorema-ux3c0-de-buckingham}

[]{#intuir-muchas-variables-pocas-combinaciones-esenciales}

### Intuir: muchas variables, pocas combinaciones esenciales {#fispm-c02-intuir-muchas-variables-pocas-combinaciones-esenciales}

Supongamos que un fenómeno se describe mediante $q_1,q_2,\ldots,q_n.$

Cada variable puede tener unidades y dimensiones distintas. A primera vista, una relación $F(q_1,\ldots,q_n)=0$

parece depender de las $n$ variables por separado.

Sin embargo, §§8--11 nos han mostrado algo importante:

- las combinaciones de dimensión uno sobreviven al cambio de unidades;

- esas combinaciones pueden funcionar como invariantes de semejanza;

- una libertad adimensional contiene precisamente información que las dimensiones no fijan.

La pregunta natural es:

$$\boxed{ \text{¿cuántas combinaciones adimensionales independientes podemos construir?} }$$

El teorema $\Pi$ de Buckingham responde, bajo hipótesis precisas:[^35]

[]{#fig:I-02-R06}

<figure id="fig-fpm-v04-i-02-r06" class="fpm-v04-panel">

<a href="/assets/books/fispm/v04/I-02-R06.svg" class="lightbox" data-gallery="fpm-v04-c02"><img src="/assets/books/fispm/v04/I-02-R06.svg" alt="Un grupo adimensional explícito. Diagrama del capítulo 2; el pie describe las variables, las hipótesis y el significado de los trazos." class="fpm-v04-figure img-fluid" width="351" height="204" loading="lazy" decoding="async"></a>

<figcaption>

**Figura 2.9.** Con las magnitudes $v$, $g$ y $\ell$, la combinación $\Pi=v/\sqrt{g\ell}$ tiene dimensión uno. El control dimensional no fija su valor ni garantiza que esas tres magnitudes describan por completo el fenómeno. Véase §[12](#fispm-c02-el-teorema-ux3c0-de-buckingham).

</figcaption>

</figure>

$$\boxed{ n-r, }$$

donde $r$ es el **rango dimensional** de las variables. La clave está en entender qué significa ese rango.

[]{#representar-columnas-de-exponentes-dimensionales}

### Representar: columnas de exponentes dimensionales {#fispm-c02-representar-columnas-de-exponentes-dimensionales}

Fijemos un orden de dimensiones base relevantes: $D_1,\ldots,D_d.$ Para cada variable $q_i$, escribimos

$$[q_i] = D_1^{a_{1i}} D_2^{a_{2i}} \cdots D_d^{a_{di}}.$$

La firma dimensional de $q_i$ es la columna

$$\mathbf a_i = \begin{pmatrix} a_{1i}\\ a_{2i}\\ \vdots\\ a_{di} \end{pmatrix}.$$

Colocamos todas las columnas juntas:

$$A = \begin{pmatrix} | & | & & |\\ \mathbf a_1 & \mathbf a_2 & \cdots & \mathbf a_n\\ | & | & & | \end{pmatrix}.$$

**Definición 29 --- Matriz dimensional** La **matriz dimensional** de las variables $q_1,\ldots,q_n$, respecto de una lista ordenada de dimensiones base, es la matriz cuyas columnas son sus firmas dimensionales.

La matriz dimensional no contiene los valores de las variables.

Contiene solamente sus exponentes dimensionales.

[]{#rango-dimensional-sin-presuponer-álgebra-lineal-avanzada}

### Rango dimensional sin presuponer álgebra lineal avanzada {#fispm-c02-rango-dimensional-sin-presuponer-uxe1lgebra-lineal-avanzada}

Aplicamos eliminación gaussiana a $A$. El número de columnas pivote ---equivalentemente, el número de filas no nulas de una forma escalonada--- mide cuántas direcciones dimensionales independientes aparecen realmente entre las variables.

**Definición 30 --- Rango dimensional** El **rango dimensional** de un conjunto de variables es el rango $r$ de su matriz dimensional, calculado por eliminación gaussiana. Es el número de restricciones dimensionales independientes que intervienen en el problema.

Siempre: $r\le d$

y

$$r\le n.$$

El número relevante en Buckingham no es simplemente «cuántos símbolos $M,L,T,\ldots$ vemos». Es el número de combinaciones dimensionales **independientes**.

**Principio 23 --- La cuenta de Buckingham usa rango, no conteo superficial de dimensiones** Para determinar el número de grupos adimensionales independientes debemos calcular el rango de la matriz de exponentes. Contar símbolos dimensionales sin verificar su independencia puede producir una cuenta incorrecta.

[]{#un-monomio-es-adimensional-exactamente-cuando-resuelve-un-sistema-homogéneo}

### Un monomio es adimensional exactamente cuando resuelve un sistema homogéneo {#fispm-c02-un-monomio-es-adimensional-exactamente-cuando-resuelve-un-sistema-homoguxe9neo}

Consideremos un producto de potencias:

$$\Pi = q_1^{\alpha_1} q_2^{\alpha_2} \cdots q_n^{\alpha_n}.$$

Su firma dimensional es

$$\mathbf d(\Pi) = \alpha_1\mathbf a_1 + \cdots+ \alpha_n\mathbf a_n.$$

En forma matricial: $\mathbf d(\Pi) = A\alpha,$

donde

$$\alpha = \begin{pmatrix} \alpha_1\\ \vdots\\ \alpha_n \end{pmatrix}.$$

Por tanto: $[\Pi]=1$

si y solo si

$$\boxed{ A\alpha=0. }$$

Así, construir combinaciones adimensionales equivale a resolver un sistema lineal homogéneo.

[]{#por-qué-aparecen-n-r-parámetros-libres}

### ¿Por qué aparecen $n-r$ parámetros libres? {#fispm-c02-por-quuxe9-aparecen-n-r-paruxe1metros-libres}

Sea $A$ una matriz con $n$ columnas y rango $r$. Al reducir

$$A\alpha=0$$

por eliminación gaussiana, aparecen:

- $r$ variables pivote;

- $n-r$ variables libres.

Cada elección independiente de las variables libres produce una solución del sistema. Por tanto, el conjunto de exponentes que generan monomios adimensionales posee

$$\boxed{ n-r }$$

grados de libertad independientes.

Éste es el núcleo algebraico de la cuenta de Buckingham.

No necesitamos todavía una teoría abstracta del espacio nulo.

Basta la lógica de los sistemas lineales:

$$\boxed{ n\text{ incógnitas} - r\text{ pivotes} = n-r\text{ variables libres}. }$$

[]{#grupo-π}

### Grupo Π {#fispm-c02-grupo-ux3c0}

**Definición 31 --- Grupo $\Pi$** Un **grupo $\Pi$** es una combinación monomial de las variables pertinentes,

$$\Pi = \prod_{i=1}^nq_i^{\alpha_i},$$

cuya dimensión es uno: $[\Pi]=1.$ Un conjunto de grupos $\Pi_1,\ldots,\Pi_k$ será llamado **independiente** cuando ninguno pueda obtenerse como producto de potencias de los demás. Esta independencia es multiplicativa. Al pasar a los vectores de exponentes, se convierte en la independencia ordinaria de soluciones de

$$A\alpha=0.$$

[]{#variables-repetidoras}

### Variables repetidoras {#fispm-c02-variables-repetidoras}

Si

$$\operatorname{rank}A=r,$$

podemos escoger $r$ columnas independientes.

Después de reordenar variables, llamémoslas: $q_1,\ldots,q_r.$

La submatriz formada por esas columnas será:

$$B.$$

Como las columnas son independientes, $B$ posee rango de columnas $r$. En general $B$ es una matriz $d\times r$ y no tiene por qué ser cuadrada. Lo que necesitaremos es que sus columnas formen una base del espacio generado por todas las columnas de $A$.

Llamaremos a

$$q_1,\ldots,q_r$$

**variables repetidoras**.

No porque aparezcan físicamente «más veces», sino porque se reutilizan para construir cada grupo adimensional.

[]{#construcción-de-los-grupos}

### Construcción de los grupos {#fispm-c02-construcciuxf3n-de-los-grupos}

Tomemos una variable no repetidora: $q_{r+k}.$

Buscamos un grupo de la forma

$$\Pi_k = q_{r+k} q_1^{c_{1k}} \cdots q_r^{c_{rk}}.$$

Queremos: $[\Pi_k]=1.$

Si

$$\mathbf a_{r+k}$$

es la columna dimensional de $q_{r+k}$, la condición es: $Bc^{(k)} + \mathbf a_{r+k} = 0,$

donde

$$c^{(k)} = \begin{pmatrix} c_{1k}\\ \vdots\\ c_{rk} \end{pmatrix}.$$

Como cada columna de $A$ pertenece al espacio generado por las columnas independientes de $B$, existe una solución de

$$Bc^{(k)} = -\mathbf a_{r+k}.$$

Esa solución es única porque las columnas de $B$ son independientes: si

$$Bc=Bc',$$

entonces $B(c-c')=0,$

y la independencia obliga a

$$c=c'.$$

No escribiremos $B^{-1}$, porque $B$ puede ser rectangular cuando el número de dimensiones base $d$ es mayor que el rango $r$. En la práctica resolveremos el sistema por eliminación. Como existen

$$n-r$$

variables no repetidoras, esta construcción produce $\Pi_1,\ldots,\Pi_{n-r}.$

[]{#por-qué-esos-grupos-son-independientes}

### Por qué esos grupos son independientes {#fispm-c02-por-quuxe9-esos-grupos-son-independientes}

Cada grupo construido tiene exponente $1$ en una variable no repetidora distinta:

$$\Pi_k = q_{r+k} \times \text{potencias de las variables repetidoras}.$$

Supongamos que

$$\Pi_1^{\lambda_1} \cdots \Pi_{n-r}^{\lambda_{n-r}} = 1$$

como identidad monomial.

Miremos el exponente de

$$q_{r+k}.$$

Esa variable aparece con exponente $\lambda_k$ y no aparece en los otros grupos. Por tanto: $\lambda_k=0.$ Esto vale para todo $k$. Luego los grupos son independientes.

[]{#por-qué-generan-todos-los-monomios-adimensionales}

### Por qué generan todos los monomios adimensionales {#fispm-c02-por-quuxe9-generan-todos-los-monomios-adimensionales}

Sea

$$\Pi = q_1^{\alpha_1}\cdots q_n^{\alpha_n}$$

cualquier monomio adimensional.

Queremos mostrar que se obtiene a partir de los grupos construidos.

Formemos:

$$\widetilde\Pi = \Pi \Pi_1^{-\alpha_{r+1}} \cdots \Pi_{n-r}^{-\alpha_n}.$$

Por construcción, se cancelan todos los exponentes de las variables no repetidoras. Por tanto,

$$\widetilde\Pi = q_1^{\beta_1}\cdots q_r^{\beta_r}.$$

Además, $\widetilde\Pi$ sigue siendo adimensional porque es producto y cociente de cantidades de dimensión uno. Entonces: $B\beta=0.$ Pero las columnas de $B$ son independientes. La única solución es: $\beta=0.$ Por tanto: $\widetilde\Pi=1.$

Luego:

$$\boxed{ \Pi = \Pi_1^{\alpha_{r+1}} \cdots \Pi_{n-r}^{\alpha_n}. }$$

Toda combinación monomial adimensional se genera mediante los

$$n-r$$

grupos construidos.

[]{#la-parte-física-invariancia-frente-a-cambios-de-unidades}

### La parte física: invariancia frente a cambios de unidades {#fispm-c02-la-parte-fuxedsica-invariancia-frente-a-cambios-de-unidades}

Hasta aquí hemos probado un hecho algebraico.

Para llegar al teorema de Buckingham debemos añadir una hipótesis física:

> la relación entre las cantidades no debe depender de la elección arbitraria de las unidades base.

Supongamos: $F(q_1,\ldots,q_n)=0.$

Cambiamos independientemente las unidades base.

Los valores numéricos de los $q_i$ cambian según sus firmas dimensionales. La relación física, sin embargo, debe describir la misma situación. Por tanto, debe ser constante a lo largo de las transformaciones numéricas inducidas únicamente por cambios de unidades.

Los grupos $\Pi_k$, al ser adimensionales, permanecen invariantes bajo esas transformaciones. La información que sobrevive al cambio de unidades puede organizarse entonces mediante ellos.

[]{#normalizar-las-variables-repetidoras}

### Normalizar las variables repetidoras {#fispm-c02-normalizar-las-variables-repetidoras}

Hay una forma concreta de verlo.

Trabajemos con valores positivos para poder usar logaritmos y potencias reales sin discutir signos.

Queremos cambiar las unidades base de modo que los valores numéricos de las $r$ variables repetidoras adopten valores de referencia, por ejemplo: $1,\ldots,1.$ Sea

$$u= \begin{pmatrix} \log\lambda_1\\ \vdots\\ \log\lambda_d \end{pmatrix}$$

el vector de logaritmos de los factores de reescalado de las $d$ unidades base.

Si

$$b= \begin{pmatrix} \log q_1\\ \vdots\\ \log q_r \end{pmatrix}$$

contiene los logaritmos de los valores numéricos de las variables repetidoras, la condición de llevar esos valores a $1$ se escribe: $B^{\mathsf T}u=b.$ Como $B$ tiene rango de columnas $r$, la matriz $B^{\mathsf T}$ tiene rango de filas $r$. Por tanto, el sistema es compatible para todo $b$.

Si $d>r$, la solución $u$ no tiene por qué ser única: quedan cambios de unidades que no afectan a las variables repetidoras. Esa no unicidad es irrelevante para la reducción, porque basta con que exista una normalización.

Después de esta normalización:

- las variables repetidoras ya no aportan parámetros numéricos libres;

- los valores normalizados de las variables restantes quedan representados por combinaciones adimensionales equivalentes a los grupos $\Pi_k$.

Por tanto, una relación invariante bajo cambios de unidades puede describirse únicamente mediante esos invariantes.

[]{#teorema-π-de-buckingham}

### Teorema Π de Buckingham {#fispm-c02-teorema-ux3c0-de-buckingham}

**Teorema 5 --- $\Pi$ de Buckingham, forma elemental**

Sean

$$q_1,\ldots,q_n>0$$

variables físicas pertinentes, y sea $A$ su matriz dimensional, de rango

$$r.$$

Supongamos que:

1.  las dimensiones de las variables están expresadas respecto de un sistema fijo de dimensiones base;

2.  la relación física

$$F(q_1,\ldots,q_n)=0$$

es independiente de la elección multiplicativa de las unidades base; 3. el conjunto de variables es el declarado por el modelo y la relación se considera en una región positiva donde las potencias reales utilizadas están bien definidas. Entonces pueden construirse

$$\boxed{ n-r }$$

grupos adimensionales independientes

$$\Pi_1,\ldots,\Pi_{n-r},$$

tales que:

1.  toda combinación monomial adimensional de las $q_i$ es producto de potencias de esos grupos;

2.  la relación física puede reescribirse en la forma

$$\boxed{ \Phi(\Pi_1,\ldots,\Pi_{n-r})=0 }$$

para alguna función $\Phi$.

[]{#demostración-4}

#### Demostración {#fispm-c02-demostraciuxf3n-4}

Como $\operatorname{rank}A=r,$

elegimos $r$ columnas independientes y, reordenando las variables si es necesario, las llamamos

$$q_1,\ldots,q_r.$$

Para cada una de las

$$n-r$$

variables restantes construimos:

$$\Pi_k = q_{r+k} q_1^{c_{1k}} \cdots q_r^{c_{rk}},$$

eligiendo los exponentes mediante: $Bc^{(k)} = -\mathbf a_{r+k}.$

Esto es posible porque las columnas de $B$ generan el espacio de columnas de $A$, y determina de manera única cada $c^{(k)}$ porque esas columnas son independientes. Así: $[\Pi_k]=1.$ Los grupos son independientes porque cada uno contiene una variable no repetidora distinta con exponente $1$.

La argumentación de §12.10 muestra además que cualquier otro monomio adimensional es un producto de potencias de estos grupos. Queda demostrar la reducción funcional. Denotemos por $z_i>0$ los valores numéricos iniciales de las variables, para distinguirlos de las magnitudes físicas. Si las unidades base se multiplican por $\lambda_1,\ldots,\lambda_d>0$, y $u_j=\log\lambda_j$, sus nuevos valores satisfacen

$$\log z_i'=\log z_i-\mathbf a_i^{\mathsf T}u.$$

Queremos llevar las $r$ variables repetidoras a $z_1'=\cdots=z_r'=1$. Esto equivale a resolver

$$B^{\mathsf T}u=(\log z_1,\ldots,\log z_r)^{\mathsf T}.$$

La matriz $B^{\mathsf T}$ tiene rango de filas $r$, así que este sistema admite solución para cualquier vector real de logaritmos. Si $d>r$, la solución puede no ser única; basta su existencia. Los factores $\lambda_j=e^{u_j}$ son positivos.

En las unidades así elegidas, cada valor no repetidor coincide con el valor de su grupo adimensional, pues los factores repetidores de $\Pi_k$ valen uno. Por tanto, toda lista inicial tiene un representante normalizado

$$(1,\ldots,1,\Pi_1,\ldots,\Pi_{n-r}).$$

La hipótesis de invariancia significa aquí que la validez de la relación, es decir, su conjunto de soluciones, se conserva bajo esos cambios de unidades. No exige que el valor numérico de $F$ sea invariante fuera de su conjunto de ceros. Escribiendo $F$ en la representación numérica inicial, definimos $\Phi(p_1,\ldots,p_{n-r})=F(1,\ldots,1,p_1,\ldots,p_{n-r}).$

La relación inicial vale si y sólo si vale en su representante normalizado, esto es, si y sólo si $\Phi(\Pi_1,\ldots,\Pi_{n-r})=0$. Cuando el modelo se limita a una región positiva, usamos su saturación por los cambios de unidades y la correspondiente imagen en los grupos; no se impone la relación en estados ajenos al dominio físico. Así queda justificada la reducción funcional.

$$\boxed{\text{QED}}$$

[]{#qué-significa-exactamente-n-r}

### Qué significa exactamente $n-r$ {#fispm-c02-quuxe9-significa-exactamente-n-r}

La fórmula:

$$n-r$$

no significa:

> «el problema físico ha quedado completamente resuelto».

Significa:

> la dependencia de unidades permite reducir una relación entre $n$ variables a una relación entre $n-r$ parámetros adimensionales independientes.

Todavía queda por determinar: $\Phi.$

Esa función puede requerir:

- teoría física;

- ecuaciones diferenciales;

- experimentos;

- simulaciones;

- datos;

- aproximaciones adicionales.

**Principio 24 --- Buckingham reduce variables, no determina la función adimensional** El teorema $\Pi$ identifica una representación mediante parámetros adimensionales, pero no determina en general la función que relaciona esos parámetros.

[]{#los-grupos-π-no-son-únicos}

### Los grupos Π no son únicos {#fispm-c02-los-grupos-ux3c0-no-son-uxfanicos}

Supongamos que: $\Pi_1,\Pi_2$

son dos grupos independientes.

Entonces también pueden servir, por ejemplo:

$$\widetilde\Pi_1=\Pi_1\Pi_2,$$

$$\widetilde\Pi_2=\Pi_2.$$

O:

$$\widehat\Pi_1=\Pi_1^2,$$

$$\widehat\Pi_2=\frac{\Pi_2}{\Pi_1},$$

si la transformación entre conjuntos conserva independencia y puede invertirse en la región considerada.

Por tanto:

$$\boxed{ \text{el conjunto de grupos }\Pi \text{ no es canónico}. }$$

Lo canónico es la cantidad de grados de libertad: $n-r.$ La elección práctica debe favorecer grupos con interpretación física clara.

[]{#ejemplo-elemental-número-de-reynolds-dimensional}

### Ejemplo elemental: número de Reynolds dimensional {#fispm-c02-ejemplo-elemental-nuxfamero-de-reynolds-dimensional}

Consideremos las variables: $v,\quad L,\quad \rho,\quad \mu,$

con:

$$[v]=LT^{-1},$$

$$[L]=L,$$

$$[\rho]=ML^{-3},$$

$$[\mu]=ML^{-1}T^{-1}.$$

Usaremos el orden: $(T,L,M).$

La matriz dimensional es:

$$A = \begin{pmatrix} -1 & 0 & 0 & -1\\ 1 & 1 & -3 & -1\\ 0 & 0 & 1 & 1 \end{pmatrix}.$$

Su rango es: $r=3.$

Como: $n=4,$

esperamos: $n-r=1$

grupo independiente.

Buscamos: $\Pi = v^\alpha L^\beta \rho^\gamma \mu^\delta.$

La condición:

$$A \begin{pmatrix} \alpha\\ \beta\\ \gamma\\ \delta \end{pmatrix} = 0$$

produce:

$$-\alpha-\delta=0,$$

$$\alpha+\beta-3\gamma-\delta=0,$$

$$\gamma+\delta=0.$$

Tomando: $\alpha=1,$

obtenemos:

$$\delta=-1,$$

$$\gamma=1,$$

$$\beta=1.$$

Por tanto:

$$\boxed{ \Pi = \frac{\rho vL}{\mu}. }$$

Éste es el grupo que, en mecánica de fluidos, se denomina número de Reynolds.

Aquí nos interesa primero su estructura dimensional. Su interpretación física detallada pertenecerá a capítulos posteriores de fluidos.

[]{#poner-a-prueba-contar-dimensiones-sin-calcular-rango}

### Poner a prueba: contar dimensiones sin calcular rango {#fispm-c02-poner-a-prueba-contar-dimensiones-sin-calcular-rango}

Supongamos que las variables tienen dimensiones:

$$[x]=L,$$

$$[y]=L^2T^{-1},$$

$$[z]=L^3T^{-2}.$$

Alguien dice:

> «Aparecen $L$ y $T$, así que el rango es $2$.»

No necesariamente.

Miremos las columnas en el orden $(L,T)$:

$$\begin{pmatrix} 1\\ 0 \end{pmatrix}, \qquad \begin{pmatrix} 2\\ -1 \end{pmatrix}, \qquad \begin{pmatrix} 3\\ -2 \end{pmatrix}.$$

Las dos primeras son independientes.

La tercera satisface:

$$\begin{pmatrix} 3\\ -2 \end{pmatrix} = -1 \begin{pmatrix} 1\\ 0 \end{pmatrix} + 2 \begin{pmatrix} 2\\ -1 \end{pmatrix}.$$

Por tanto: $r=2.$ En este caso el conteo superficial acertó. Pero acertó porque las columnas realmente alcanzan rango $2$. Si todas las columnas fueran múltiplos de una sola, el rango sería $1$ aunque aparecieran varios exponentes numéricos.

La eliminación gaussiana es el control fiable.

[]{#ejercicios-práctica-guiada-1}

### Ejercicios práctica guiada {#fispm-c02-ejercicios-pruxe1ctica-guiada-1}

**Ejercicio 24 --- Construir un grupo $\Pi$ por eliminación**

**Objetivo:** `Consolidación`

**Intenta primero: 3--5 min antes de leer la solución.**

Usa: $v,\quad L,\quad\rho,\quad\mu$

con las dimensiones de §12.16.

1.  Construye la matriz dimensional.

2.  Comprueba que su rango es $3$.

3.  Resuelve $A\alpha=0$.

4.  Construye un grupo $\Pi$.

5.  Verifica directamente que $[\Pi]=1$.

**Solución**

La matriz es:

$$A = \begin{pmatrix} -1 & 0 & 0 & -1\\ 1 & 1 & -3 & -1\\ 0 & 0 & 1 & 1 \end{pmatrix}.$$

Las columnas de $v,L,\rho$ son independientes, por lo que: $r=3.$ Con $n=4$: $n-r=1.$

El sistema homogéneo es:

$$-\alpha-\delta=0,$$

$$\alpha+\beta-3\gamma-\delta=0,$$

$$\gamma+\delta=0.$$

Tomando: $\alpha=1,$

resulta: $\delta=-1, \qquad \gamma=1, \qquad \beta=1.$

Así:

$$\boxed{ \Pi=\frac{\rho vL}{\mu}. }$$

Verificación:

$$[\rho vL] = ML^{-3} \cdot LT^{-1} \cdot L = ML^{-1}T^{-1}.$$

Como: $[\mu]=ML^{-1}T^{-1},$

obtenemos:

$$\boxed{ [\Pi]=1. }$$

**Ejercicio 25 --- Reconstruir la cuenta $n-r$**

**Objetivo:** `Demostración — consolidación`

**Intenta primero: 3--5 min antes de leer la solución.**

Sea $A$ una matriz dimensional con $n$ columnas y rango $r$.

1.  Explica mediante eliminación gaussiana por qué el sistema

$$A\alpha=0$$

tiene $n-r$ variables libres. 2. Explica por qué cada solución produce un monomio adimensional. 3. Explica por qué una elección de $n-r$ soluciones independientes genera todos los monomios adimensionales. 4. Señala qué paso adicional hace falta para pasar de este resultado algebraico al teorema físico de Buckingham.

**Solución**

**1.**

El rango $r$ significa que una forma escalonada de $A$ posee:

$$r$$

pivotes.

Como existen:

$$n$$

incógnitas, quedan:

$$\boxed{ n-r }$$

variables libres.

**2.**

Si: $A\alpha=0,$

entonces la firma dimensional de: $\Pi = \prod_iq_i^{\alpha_i}$

es cero. Por tanto: $[\Pi]=1.$

**3.**

Las soluciones del sistema homogéneo se obtienen asignando valores a las variables libres y resolviendo las pivote. Una base de soluciones independientes permite escribir cualquier solución como combinación de ellas. Al volver a los monomios, la suma de vectores de exponentes se convierte en producto de potencias de grupos $\Pi$.

Por tanto, los grupos asociados generan todos los monomios adimensionales.

**4.**

Falta la hipótesis física de que la relación sea independiente de la elección de unidades.

Solo entonces podemos concluir que la información de la relación puede reorganizarse mediante los invariantes adimensionales.

Esta separación es esencial:

$$\boxed{ \text{álgebra dimensional} + \text{invariancia física} \Longrightarrow \text{Buckingham }\Pi. }$$

**Ejercicio 26 --- Variables redundantes y rango dimensional**

**Objetivo:** `Diagnóstico → Síntesis`

**Intenta primero: 3--5 min antes de leer la solución.**

Considera: $F,\quad m,\quad a,\quad \ell_1,\quad \ell_2,$

con:

$$[F]=MLT^{-2},$$

$$[m]=M,$$

$$[a]=LT^{-2},$$

$$[\ell_1]=[\ell_2]=L.$$

1.  Construye la matriz dimensional usando $(T,L,M)$.

2.  Determina su rango.

3.  ¿Cuántos grupos $\Pi$ independientes deben existir?

4.  Encuentra dos.

5.  Explica por qué añadir $\ell_2$ aumenta $n$ pero no el rango.

6.  Explica qué enseña esto sobre la expresión $n-r$.

**Solución**

Las columnas son:

$$F: \begin{pmatrix} -2\\ 1\\ 1 \end{pmatrix}, \qquad m: \begin{pmatrix} 0\\ 0\\ 1 \end{pmatrix},$$

$$a: \begin{pmatrix} -2\\ 1\\ 0 \end{pmatrix}, \qquad \ell_1: \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix}, \qquad \ell_2: \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix}.$$

Por tanto:

$$A = \begin{pmatrix} -2 & 0 & -2 & 0 & 0\\ 1 & 0 & 1 & 1 & 1\\ 1 & 1 & 0 & 0 & 0 \end{pmatrix}.$$

Las columnas de: $m,\quad a,\quad\ell_1$

son independientes.

Luego:

$$\boxed{ r=3. }$$

Como: $n=5,$

tenemos:

$$\boxed{ n-r=2. }$$

Dos grupos independientes son:

$$\boxed{ \Pi_1=\frac{F}{ma} }$$

y:

$$\boxed{ \Pi_2=\frac{\ell_1}{\ell_2}. }$$

Verificación: $[ma] = MLT^{-2} = [F],$

por lo que: $[\Pi_1]=1.$

Además: $[\Pi_2] = \frac LL = 1.$

Añadir $\ell_2$ aumenta el número de variables: $4\to5,$

pero su columna dimensional es idéntica a la de $\ell_1$. Por tanto, no añade una nueva dirección dimensional independiente. El rango permanece: $r=3.$ Sin embargo, aparece una nueva razón adimensional: $\frac{\ell_1}{\ell_2}.$

Esto muestra el significado de:

$$\boxed{ n-r: }$$

variables adicionales que no aumentan el rango producen nuevas libertades adimensionales.

[]{#autoexplicación-4}

### Autoexplicación {#fispm-c02-autoexplicaciuxf3n-4}

**Pausa de autoexplicación** Responde sin volver a la demostración:

1.  ¿por qué un grupo $\Pi$ corresponde a una solución de $A\alpha=0$?;

2.  ¿por qué el número de grupos independientes es $n-r$?;

3.  ¿por qué los grupos no son únicos?;

4.  ¿qué hipótesis física convierte el resultado algebraico en el teorema de Buckingham?;

5.  ¿qué información sigue faltando después de escribir

$$\Phi(\Pi_1,\ldots,\Pi_{n-r})=0?$$

[]{#variar-cambiar-las-variables-repetidoras}

### Variar: cambiar las variables repetidoras {#fispm-c02-variar-cambiar-las-variables-repetidoras}

En el ejemplo: $v,\quad L,\quad\rho,\quad\mu,$

podemos construir el grupo usando diferentes conjuntos de tres variables repetidoras, siempre que sus columnas dimensionales sean independientes. Las formas intermedias cambiarán. El resultado puede aparecer como: $\Pi = \frac{\rho vL}{\mu},$

o como su inverso: $\Pi^{-1} = \frac{\mu}{\rho vL}.$

Ambos contienen la misma información. En general, si: $\widetilde\Pi=\Pi^{-1},$

entonces: $\Phi(\Pi)=0$

puede reescribirse como otra relación: $\widetilde\Phi(\widetilde\Pi)=0.$ La física no depende de nuestra elección particular de coordenadas adimensionales.

[]{#conectar-con-semejanza}

### Conectar con semejanza {#fispm-c02-conectar-con-semejanza}

§11 definió semejanza como preservación de las relaciones relevantes y de los parámetros adimensionales que controlan el modelo. Buckingham explica ahora por qué esos parámetros aparecen. Si dos sistemas tienen los mismos valores de un conjunto completo de: $\Pi_1,\ldots,\Pi_{n-r},$

entonces ocupan el mismo punto en la descripción adimensional del problema.

Bajo las hipótesis del modelo, esto constituye la base algebraica de una comparación por semejanza.

Pero debemos conservar la cautela:

$$\boxed{ \text{mismos grupos }\Pi + \text{mismo modelo} }$$

es la afirmación relevante.

Los grupos solos no garantizan que dos sistemas físicos distintos compartan todas las leyes, condiciones de frontera o regímenes necesarios.

[]{#qué-hemos-ganado}

### Qué hemos ganado {#fispm-c02-quuxe9-hemos-ganado}

Partimos de una relación con:

$$n$$

variables dimensionales.

Buckingham la reorganiza mediante:

$$n-r$$

parámetros de dimensión uno. La reducción puede ser enorme.

Por ejemplo, si:

$$n=8$$

y: $r=3,$

pasamos conceptualmente de ocho variables dimensionales a:

$$5$$

grupos adimensionales.

Esto no resuelve la función física.

Pero reduce el espacio en que debemos:

- experimentar;

- ajustar datos;

- comparar modelos;

- realizar simulaciones;

- buscar semejanzas.

Ésta es una de las razones por las que el análisis dimensional es una herramienta de modelización y no solamente de comprobación de unidades.

[]{#síntesis-8}

### Síntesis {#fispm-c02-suxedntesis-8}

El procedimiento completo es:

$$\boxed{ \text{variables} \to \text{firmas} \to A \to r \to A\alpha=0 \to \Pi_1,\ldots,\Pi_{n-r}. }$$

La parte algebraica establece:

$$\boxed{ \dim(\text{libertad adimensional}) = n-r }$$

en el sentido elemental de:

$$n-r$$

variables libres del sistema homogéneo.

La parte física añade invariancia bajo cambios de unidades y permite escribir:

$$\boxed{ F(q_1,\ldots,q_n)=0 \quad\Longrightarrow\quad \Phi(\Pi_1,\ldots,\Pi_{n-r})=0. }$$

Pero:

$$\boxed{ \text{Buckingham }\Pi \not\Rightarrow \text{función }\Phi\text{ conocida}. }$$

El siguiente paso será usar todo el aparato en problemas físicos completos (§[13](#fispm-c02-ejemplos-de-modelizaciuxf3n-dimensional)).

Allí volveremos al péndulo y añadiremos un segundo caso de semejanza para separar con precisión:

- lo que obliga la dimensión;

- lo que debe aportar la física;

- lo que queda para experimento o teoría.

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-6 label="fispm-c02-notas-y-fuentes-6"}

[]{#ejemplos-de-modelización-dimensional}

[]{#fispm-t1-c02-s13}

[]{#fpm-i-02-s13}

## 13. Ejemplos de modelización dimensional {#fispm-c02-ejemplos-de-modelizaciuxf3n-dimensional}

[]{#intuir-ahora-importa-tanto-elegir-variables-como-manipular-dimensiones}

### Intuir: ahora importa tanto elegir variables como manipular dimensiones {#fispm-c02-intuir-ahora-importa-tanto-elegir-variables-como-manipular-dimensiones}

Hasta §12 hemos construido un aparato poderoso:

- dimensión;

- homogeneidad;

- firmas dimensionales;

- inferencia de exponentes;

- escalamiento;

- semejanza;

- teorema $\Pi$ de Buckingham.

Pero una herramienta formal solo trabaja con las variables que el modelo le entrega. Si seleccionamos mal esas variables, podemos hacer álgebra impecable sobre un modelo incompleto. Por eso esta sección no introduce un nuevo teorema.

Introduce un modo de **usar** los teoremas.

La pregunta rectora será:

$$\boxed{ \text{¿qué parte de la conclusión proviene de la dimensión y qué parte proviene de la física?} }$$

Trabajaremos dos casos:

1.  período de un péndulo;

2.  fuerza de arrastre de una esfera en un medio.

Ambos aparecen en la tradición clásica del análisis dimensional y están tratados como aplicaciones por Zorich.[^36]

[]{#caso-i-el-péndulo-empezar-por-la-lista-de-variables}

### Caso I --- El péndulo: empezar por la lista de variables {#fispm-c02-caso-i-el-puxe9ndulo-empezar-por-la-lista-de-variables}

Consideremos un péndulo idealizado:

- masa puntual $m$;

- suspensión sin masa de longitud $\ell$;

- ángulo inicial $\varphi_0$;

- aceleración gravitatoria $g$;

- período $P$.

Queremos modelar:

$$P.$$

Una primera lista incompleta sería: $P=f(\ell,m,\varphi_0).$ Pero esta lista no distingue, por ejemplo, un péndulo situado en campos gravitatorios de distinta intensidad. Zorich utiliza precisamente esta observación para justificar que debe incluirse $g$.[^37]

La lista mínima considerada pasa entonces a:

$$\boxed{ P=f(\ell,m,g,\varphi_0). }$$

**Principio 25 --- La selección de variables es una hipótesis de modelización** Buckingham $\Pi$ puede reorganizar una lista de variables pertinente, pero no decide por sí solo si esa lista está físicamente completa. Incluir u omitir una variable es una decisión del modelo que debe justificarse por separado.

[]{#representar-matriz-dimensional-del-péndulo}

### Representar: matriz dimensional del péndulo {#fispm-c02-representar-matriz-dimensional-del-puxe9ndulo}

Usaremos el orden de dimensiones: $(T,L,M).$

Las firmas son:

$$\mathbf d(P) = \begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix},$$

$$\mathbf d(\ell) = \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix},$$

$$\mathbf d(m) = \begin{pmatrix} 0\\ 0\\ 1 \end{pmatrix},$$

$$\mathbf d(g) = \begin{pmatrix} -2\\ 1\\ 0 \end{pmatrix},$$

y, porque el ángulo tiene dimensión uno,

$$\mathbf d(\varphi_0) = \begin{pmatrix} 0\\ 0\\ 0 \end{pmatrix}.$$

Por tanto:

$$A = \begin{pmatrix} 1 & 0 & 0 & -2 & 0\\ 0 & 1 & 0 & 1 & 0\\ 0 & 0 & 1 & 0 & 0 \end{pmatrix}.$$

Tenemos: $n=5.$

Las tres primeras columnas son independientes, por lo que: $r=3.$

Buckingham predice:

$$\boxed{ n-r=2 }$$

grupos adimensionales independientes.

[]{#construir-los-dos-grupos-π}

### Construir los dos grupos Π {#fispm-c02-construir-los-dos-grupos-ux3c0}

Uno es inmediato:

$$\boxed{ \Pi_2=\varphi_0. }$$

Para el otro buscamos: $\Pi_1 = P\ell^\alpha g^\beta.$ La dimensión es: $[\Pi_1] = T L^\alpha (LT^{-2})^\beta.$ Entonces: $[\Pi_1] = L^{\alpha+\beta} T^{1-2\beta}.$

Exigimos dimensión uno:

$$\alpha+\beta=0,$$

$$1-2\beta=0.$$

De aquí:

$$\beta=\frac12,$$

$$\alpha=-\frac12.$$

Por tanto:

$$\boxed{ \Pi_1 = P\sqrt{\frac g\ell}. }$$

[]{#buckingham-aplicado-al-péndulo}

### Buckingham aplicado al péndulo {#fispm-c02-buckingham-aplicado-al-puxe9ndulo}

El teorema permite escribir: $\Phi(\Pi_1,\Pi_2)=0.$

Es decir:

$$\Phi\left( P\sqrt{\frac g\ell}, \varphi_0 \right) = 0.$$

Localmente, cuando la relación puede resolverse respecto del primer grupo, podemos escribir: $P\sqrt{\frac g\ell} = \Psi(\varphi_0).$

Por tanto:

$$\boxed{ P = \sqrt{\frac{\ell}{g}}\, \Psi(\varphi_0). }$$

Ésta es una conclusión mucho más precisa que: $P=C\sqrt{\frac{\ell}{g}}.$ La constante $C$ aparece solo si $\Psi$ puede tratarse como aproximadamente constante en el régimen físico considerado.

[]{#dónde-quedó-la-masa}

### ¿Dónde quedó la masa? {#fispm-c02-duxf3nde-queduxf3-la-masa}

La masa $m$ estaba incluida en la lista. Sin embargo, no aparece en la forma reducida: $P = \sqrt{\frac{\ell}{g}}\, \Psi(\varphi_0).$ Esto no ocurrió porque decidiéramos de antemano «ignorar la masa». Ocurrió porque, dentro de este conjunto de variables y dimensiones, no puede construirse una dependencia adimensional independiente en $m$ compatible con el período.

La dimensión impide que $m$ aparezca no trivialmente en la forma reducida.

Pero debemos leer la conclusión correctamente:

> dentro del modelo idealizado y de la lista de variables declarada, la masa no aparece como parámetro independiente del período.

No estamos afirmando que la masa sea irrelevante para toda propiedad física de un péndulo real.

[]{#lo-que-la-dimensión-no-determina-en-el-péndulo}

### Lo que la dimensión no determina en el péndulo {#fispm-c02-lo-que-la-dimensiuxf3n-no-determina-en-el-puxe9ndulo}

La expresión: $P = \sqrt{\frac{\ell}{g}}\, \Psi(\varphi_0)$

todavía contiene información desconocida: $\Psi.$

El análisis dimensional no dice:

- cuál es la función exacta;

- si es constante;

- cómo depende de $\varphi_0$;

- para qué amplitudes puede aproximarse;

- cuál es el error de una aproximación.

Para oscilaciones de pequeña amplitud, la teoría dinámica permite obtener: $\Psi(\varphi_0) \approx 2\pi.$ Entonces: $P \approx 2\pi \sqrt{\frac{\ell}{g}}.$ Pero el símbolo: $\approx$

marca información física adicional: una aproximación de régimen pequeño, no una consecuencia del teorema $\Pi$.

[]{#autoexplicación-del-primer-caso}

### Autoexplicación del primer caso {#fispm-c02-autoexplicaciuxf3n-del-primer-caso}

**Pausa de autoexplicación** Explica con tus propias palabras:

1.  por qué fue necesario incluir $g$;

2.  por qué $\varphi_0$ sobrevive como argumento de una función;

3.  por qué la masa desaparece;

4.  por qué Buckingham no produce $2\pi$;

5.  qué afirmación depende del modelo idealizado y no solo del álgebra.

[]{#caso-ii-arrastre-en-un-medio-empezar-por-el-modelo-más-austero}

### Caso II --- Arrastre en un medio: empezar por el modelo más austero {#fispm-c02-caso-ii-arrastre-en-un-medio-empezar-por-el-modelo-muxe1s-austero}

Consideremos una esfera de radio $r$ que se mueve con velocidad característica $v$ en un medio de densidad $\rho$. Queremos estudiar una fuerza de arrastre $F$.

Comencemos con el modelo dimensional:

$$\boxed{ F=f(\rho,v,r). }$$

Zorich utiliza precisamente este conjunto de variables para su ejemplo de una esfera en un medio no viscoso.[^38]

Las dimensiones son:

$$[F]=MLT^{-2},$$

$$[\rho]=ML^{-3},$$

$$[v]=LT^{-1},$$

$$[r]=L.$$

Tenemos cuatro variables: $n=4.$ Y las dimensiones $M,L,T$ aparecen independientemente, de modo que: $r_{\mathrm{dim}}=3.$ Por tanto: $n-r_{\mathrm{dim}}=1.$ Solo existe un grupo adimensional independiente.

[]{#construir-el-grupo-de-fuerza}

### Construir el grupo de fuerza {#fispm-c02-construir-el-grupo-de-fuerza}

Buscamos: $\Pi_F = F\rho^\alpha v^\beta r^\gamma.$

Su dimensión es:

$$MLT^{-2} \cdot (M L^{-3})^\alpha \cdot (LT^{-1})^\beta \cdot L^\gamma.$$

Agrupando:

$$M^{1+\alpha} L^{1-3\alpha+\beta+\gamma} T^{-2-\beta}.$$

Exigimos exponente cero para cada dimensión.

Masa: $1+\alpha=0,$

luego: $\alpha=-1.$

Tiempo: $-2-\beta=0,$

luego: $\beta=-2.$

Longitud: $1-3(-1)-2+\gamma=0.$ Por tanto: $2+\gamma=0,$

y: $\gamma=-2.$

Así:

$$\boxed{ \Pi_F = \frac{F}{\rho v^2r^2}. }$$

[]{#qué-concluye-buckingham-en-el-modelo-de-tres-variables-explicativas}

### Qué concluye Buckingham en el modelo de tres variables explicativas {#fispm-c02-quuxe9-concluye-buckingham-en-el-modelo-de-tres-variables-explicativas}

Como solo existe un grupo adimensional independiente, la relación reducida tiene la forma: $\Phi(\Pi_F)=0.$ En una rama física donde esta ecuación selecciona un valor constante: $\Pi_F=C.$

Entonces:

$$\boxed{ F = C\rho v^2r^2. }$$

Ésta es precisamente la estructura obtenida en el ejemplo dimensional de Zorich.[^39]

Pero:

$$\boxed{ C }$$

no viene determinado por la dimensión. La dimensión tampoco prueba que el modelo de variables: $\rho,\ v,\ r$

sea suficiente para un fluido real.

[]{#poner-a-prueba-el-modelo-introducir-viscosidad}

### Poner a prueba el modelo: introducir viscosidad {#fispm-c02-poner-a-prueba-el-modelo-introducir-viscosidad}

Supongamos ahora que el medio posee una viscosidad dinámica relevante: $\mu.$

La lista se amplía:

$$\boxed{ F=f(\rho,v,r,\mu). }$$

Tenemos ahora: $n=5.$ El rango dimensional continúa siendo: $r_{\mathrm{dim}}=3.$

Por tanto:

$$\boxed{ n-r_{\mathrm{dim}}=2. }$$

Debemos esperar dos grupos adimensionales independientes.

Uno puede seguir siendo: $\Pi_1 = \frac{F}{\rho v^2r^2}.$ El segundo puede tomarse como: $\Pi_2 = \frac{\rho vr}{\mu}.$

Verifiquemos:

$$[\rho vr] = ML^{-3} \cdot LT^{-1} \cdot L = ML^{-1}T^{-1}.$$

Y: $[\mu] = ML^{-1}T^{-1}.$ Por tanto: $[\Pi_2]=1.$

[]{#la-función-reaparece}

### La función reaparece {#fispm-c02-la-funciuxf3n-reaparece}

Buckingham produce ahora: $\Phi(\Pi_1,\Pi_2)=0.$ Cuando podemos despejar $\Pi_1$: $\Pi_1 = \Psi(\Pi_2).$

Así:

$$\boxed{ \frac{F}{\rho v^2r^2} = \Psi\left( \frac{\rho vr}{\mu} \right). }$$

O:

$$\boxed{ F = \rho v^2r^2 \, \Psi\left( \frac{\rho vr}{\mu} \right). }$$

La combinación: $\frac{\rho vr}{\mu}$

es una forma del número de Reynolds basada en la escala $r$. La sección no necesita todavía interpretar en detalle todos los regímenes de flujo.

Lo importante es observar qué ocurrió al añadir una variable físicamente relevante:

$$\boxed{ \text{constante adimensional} \longrightarrow \text{función de un parámetro adimensional}. }$$

[]{#qué-enseña-el-segundo-caso}

### Qué enseña el segundo caso {#fispm-c02-quuxe9-enseuxf1a-el-segundo-caso}

Con el modelo: $F=f(\rho,v,r),$

la dimensión obliga a una forma: $F=C\rho v^2r^2.$ Con el modelo ampliado: $F=f(\rho,v,r,\mu),$

la dimensión solo obliga a: $F = \rho v^2r^2 \Psi(\rho vr/\mu).$

No hay contradicción.

Cambió el modelo. La diferencia muestra por qué la elección de variables es una decisión física previa a Buckingham. Si omitimos $\mu$, el teorema no puede advertir que la viscosidad era importante.

[]{#semejanza-en-el-problema-de-arrastre}

### Semejanza en el problema de arrastre {#fispm-c02-semejanza-en-el-problema-de-arrastre}

Supongamos dos experimentos con: $(\rho_1,v_1,r_1,\mu_1)$

y: $(\rho_2,v_2,r_2,\mu_2).$

Si queremos que ambos ocupen el mismo punto en la descripción adimensional del modelo viscoso, debemos mantener:

$$\boxed{ \frac{\rho_1v_1r_1}{\mu_1} = \frac{\rho_2v_2r_2}{\mu_2}. }$$

Entonces el mismo valor del argumento de $\Psi$ produce, dentro del modelo, el mismo valor del coeficiente adimensional: $\frac{F}{\rho v^2r^2}.$

Ésta es la lógica de semejanza:

$$\boxed{ \text{igualar parámetros adimensionales relevantes} \longrightarrow \text{comparar sistemas a escalas distintas}. }$$

[]{#ejemplo-de-escalamiento-de-un-modelo}

### Ejemplo de escalamiento de un modelo {#fispm-c02-ejemplo-de-escalamiento-de-un-modelo}

Supongamos:

- mismo fluido, de modo que $\rho$ y $\mu$ son iguales;

- radios relacionados por:

$$r_2=\lambda r_1.$$

Para conservar: $\frac{\rho vr}{\mu},$

necesitamos: $v_2r_2=v_1r_1.$

Entonces: $v_2 = \lambda^{-1}v_1.$

Así, si el modelo es diez veces más pequeño: $\lambda=\frac1{10},$

la velocidad necesaria para conservar este parámetro sería: $v_2=10v_1.$ La semejanza física no sigue automáticamente la escala geométrica. Puede exigir reescalar otras variables en sentido contrario.

[]{#diagnóstico-comparado-de-los-dos-casos}

### Diagnóstico comparado de los dos casos {#fispm-c02-diagnuxf3stico-comparado-de-los-dos-casos}

El péndulo y el arrastre muestran dos mecanismos distintos.

[]{#péndulo}

#### Péndulo {#fispm-c02-puxe9ndulo}

Una variable ya adimensional: $\varphi_0$

sobrevive directamente como argumento funcional: $P = \sqrt{\frac{\ell}{g}} \Psi(\varphi_0).$

[]{#arrastre-viscoso}

#### Arrastre viscoso {#fispm-c02-arrastre-viscoso}

La variable adicional $\mu$ no es adimensional.

Pero, al combinarse con: $\rho,\ v,\ r,$

genera: $\frac{\rho vr}{\mu}.$

Entonces: $F = \rho v^2r^2 \Psi(\rho vr/\mu).$ En ambos casos, la función adimensional contiene física no resuelta por las dimensiones.

[]{#qué-puede-decir-la-dimensión-y-qué-no}

### Qué puede decir la dimensión y qué no {#fispm-c02-quuxe9-puede-decir-la-dimensiuxf3n-y-quuxe9-no}

Podemos ordenar los resultados.

[]{#la-dimensión-sí-puede}

#### La dimensión sí puede {#fispm-c02-la-dimensiuxf3n-suxed-puede}

- detectar variables incompatibles;

- construir grupos adimensionales;

- restringir exponentes;

- eliminar dependencias imposibles dentro de un modelo;

- identificar escalas naturales;

- reducir el número de variables;

- formular criterios de semejanza.

[]{#la-dimensión-no-puede-por-sí-sola}

#### La dimensión no puede, por sí sola {#fispm-c02-la-dimensiuxf3n-no-puede-por-suxed-sola}

- decidir qué variables son físicamente relevantes;

- demostrar que una idealización es válida;

- determinar funciones adimensionales generales;

- fijar todos los coeficientes numéricos;

- establecer regímenes de aproximación;

- reemplazar experimentos o ecuaciones dinámicas.

La herramienta es poderosa precisamente cuando mantenemos visible esta frontera.

[]{#práctica-guiada-4}

### Práctica guiada {#fispm-c02-pruxe1ctica-guiada-4}

**Ejercicio 27 --- Modelización dimensional completa**

**Objetivo:** `Síntesis`

**Intenta primero: 3--5 min antes de leer la solución.**

Queremos estudiar una fuerza $F$ asociada al movimiento de un objeto de tamaño característico $L$ con velocidad $v$ en un medio de densidad $\rho$ y viscosidad dinámica $\mu$.

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-4}

Usa:

$$[F]=MLT^{-2},$$

$$[L]=L,$$

$$[v]=LT^{-1},$$

$$[\rho]=ML^{-3},$$

$$[\mu]=ML^{-1}T^{-1}.$$

Construye la matriz dimensional en el orden $(T,L,M)$ y determina su rango.

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-4}

Usa Buckingham para justificar que deben existir dos grupos adimensionales independientes.

Encuentra un conjunto posible.

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico-4}

Un estudiante omite $\mu$ y obtiene: $F=C\rho v^2L^2.$

Explica:

1.  por qué la deducción dimensional es correcta para la lista reducida;

2.  por qué eso no demuestra que la viscosidad sea físicamente irrelevante.

### D. Síntesis {#fispm-c02-d.-suxedntesis-4}

Para dos modelos en el mismo fluido, con tamaños: $L_2=\frac14L_1,$

determina cómo debe cambiar la velocidad para conservar: $\frac{\rho vL}{\mu}.$

Luego explica qué cantidad adimensional de fuerza debería coincidir entre ambos modelos si la semejanza es válida.

### E. Autoexplicación {#fispm-c02-e.-autoexplicaciuxf3n}

Señala en tu solución:

- qué vino de las dimensiones;

- qué vino de la selección de variables;

- qué sigue dependiendo de una función o de datos físicos.

**Solución**

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-5}

Las columnas dimensionales son:

$$F: \begin{pmatrix} -2\\ 1\\ 1 \end{pmatrix}, \qquad L: \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix},$$

$$v: \begin{pmatrix} -1\\ 1\\ 0 \end{pmatrix}, \qquad \rho: \begin{pmatrix} 0\\ -3\\ 1 \end{pmatrix},$$

$$\mu: \begin{pmatrix} -1\\ -1\\ 1 \end{pmatrix}.$$

Por tanto:

$$A = \begin{pmatrix} -2 & 0 & -1 & 0 & -1\\ 1 & 1 & 1 & -3 & -1\\ 1 & 0 & 0 & 1 & 1 \end{pmatrix}.$$

Hay tres columnas independientes, por ejemplo las de: $L,\ v,\ \rho.$

Así:

$$\boxed{ r=3. }$$

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-5}

Como: $n=5,$

Buckingham da:

$$\boxed{ n-r=2. }$$

Un conjunto posible es:

$$\boxed{ \Pi_1 = \frac{F}{\rho v^2L^2} }$$

y:

$$\boxed{ \Pi_2 = \frac{\rho vL}{\mu}. }$$

Ambas tienen dimensión uno. La relación reducida puede escribirse: $\Phi(\Pi_1,\Pi_2)=0,$

o, cuando puede despejarse:

$$\frac{F}{\rho v^2L^2} = \Psi\left( \frac{\rho vL}{\mu} \right).$$

### C. Diagnóstico {#fispm-c02-c.-diagnuxf3stico-5}

Si omitimos $\mu$, quedan cuatro variables: $F,\rho,v,L.$ Su rango sigue siendo $3$. Por tanto: $n-r=1.$ El único grupo independiente puede tomarse como: $\frac{F}{\rho v^2L^2}.$ De ahí: $F=C\rho v^2L^2.$ La deducción es dimensionalmente correcta **para ese modelo de variables**.

El error sería concluir que $\mu$ es irrelevante en la física real.

Buckingham no selecciona las variables.

### D. Síntesis {#fispm-c02-d.-suxedntesis-5}

En el mismo fluido: $\rho_2=\rho_1, \qquad \mu_2=\mu_1.$ Para conservar: $\frac{\rho vL}{\mu},$

necesitamos: $v_2L_2=v_1L_1.$

Como: $L_2=\frac14L_1,$

obtenemos: $v_2 \frac14L_1 = v_1L_1.$

Por tanto:

$$\boxed{ v_2=4v_1. }$$

Si la semejanza física del modelo es válida, debería coincidir también:

$$\boxed{ \frac{F_1}{\rho_1v_1^2L_1^2} = \frac{F_2}{\rho_2v_2^2L_2^2}. }$$

### E. Autoexplicación {#fispm-c02-e.-autoexplicaciuxf3n-1}

**De las dimensiones** obtuvimos:

- el rango;

- el número de grupos;

- las combinaciones posibles;

- las reglas de escalamiento necesarias para preservar los grupos.

**De la modelización** vino:

- la decisión de incluir $F,L,v,\rho,\mu$;

- la hipótesis de que esos son los parámetros pertinentes;

- la comparación en el mismo fluido.

**No quedó determinado por dimensiones**:

$$\Psi.$$

Su forma concreta exige física adicional, teoría, datos o experimentos.

[]{#variar-volver-al-péndulo-con-una-variable-omitida}

### Variar: volver al péndulo con una variable omitida {#fispm-c02-variar-volver-al-puxe9ndulo-con-una-variable-omitida}

Supongamos que alguien comienza con: $P=f(\ell,m,\varphi_0)$

y aplica Buckingham correctamente. El resultado será matemáticamente consistente con esa lista.

Pero no contendrá:

$$g.$$

El problema no está en la reducción dimensional.

Está **antes** de ella. La pregunta física fue incompleta.

Esta variación muestra una regla general:

$$\boxed{ \text{una inferencia formal no puede recuperar una variable que el modelo nunca declaró}. }$$

[]{#conectar-con-el-cierre-del-capítulo}

### Conectar con el cierre del capítulo {#fispm-c02-conectar-con-el-cierre-del-capuxedtulo}

Después de trece secciones podemos ver el análisis dimensional como una cadena completa:

$$\boxed{\begin{gathered} \text{magnitudes} \to \text{unidades}\\[2pt]\Downarrow\\[2pt]\text{dimensiones} \to \text{homogeneidad}\\[2pt]\Downarrow\\[2pt]\text{auditoría} \to \text{escalamiento}\\[2pt]\Downarrow\\[2pt]\text{grupos }\Pi \to \text{modelización}. \end{gathered}}$$

El valor del método no está únicamente en encontrar potencias correctas.

Está en hacer visibles las preguntas:

- ¿qué variables elegimos?;

- ¿qué supuestos estamos introduciendo?;

- ¿qué información es dimensional?;

- ¿qué información sigue siendo física?;

- ¿qué debe decidir un experimento o una teoría más completa?

[]{#síntesis-9}

### Síntesis {#fispm-c02-suxedntesis-9}

[]{#péndulo-1}

#### Péndulo {#fispm-c02-puxe9ndulo-1}

Buckingham produce:

$$\boxed{ P = \sqrt{\frac{\ell}{g}} \Psi(\varphi_0). }$$

La dimensión explica:

- la escala temporal $\sqrt{\ell/g}$;

- la ausencia de una dependencia independiente en $m$;

- la supervivencia de $\varphi_0$ como parámetro adimensional.

No produce:

- la función $\Psi$;

- el valor $2\pi$;

- el régimen de pequeña amplitud.

[]{#arrastre-viscoso-1}

#### Arrastre viscoso {#fispm-c02-arrastre-viscoso-1}

Buckingham produce:

$$\boxed{ F = \rho v^2r^2 \Psi\left( \frac{\rho vr}{\mu} \right). }$$

La dimensión explica:

- la escala de fuerza;

- el grupo adimensional de flujo;

- la estructura de semejanza.

No produce:

- la función $\Psi$;

- qué regímenes físicos existen;

- la validez del modelo para un medio concreto.

La lección común es:

$$\boxed{ \text{análisis dimensional} = \text{estructura rigurosa dentro de un modelo}, }$$

no:

$$\boxed{ \text{análisis dimensional} = \text{física completa}. }$$

Solo queda cerrar el capítulo mediante (§[14](#fispm-c02-quuxe9-puede-y-quuxe9-no-puede-decir-el-anuxe1lisis-dimensional)).

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-7 label="fispm-c02-notas-y-fuentes-7"}

[]{#qué-puede-y-qué-no-puede-decir-el-análisis-dimensional}

[]{#fispm-t1-c02-s14}

[]{#fpm-i-02-s14}

## 14. Qué puede y qué no puede decir el análisis dimensional {#fispm-c02-quuxe9-puede-y-quuxe9-no-puede-decir-el-anuxe1lisis-dimensional}

[]{#intuir-una-herramienta-poderosa-puede-ser-peligrosa-si-olvidamos-qué-información-contiene}

### Intuir: una herramienta poderosa puede ser peligrosa si olvidamos qué información contiene {#fispm-c02-intuir-una-herramienta-poderosa-puede-ser-peligrosa-si-olvidamos-quuxe9-informaciuxf3n-contiene}

A lo largo del capítulo hemos obtenido resultados sorprendentemente fuertes a partir de información aparentemente modesta.

Con dimensiones pudimos:

- detectar ecuaciones imposibles;

- inferir exponentes;

- construir escalas;

- comparar sistemas semejantes;

- reducir problemas con muchas variables;

- aislar parámetros adimensionales.

Esto puede producir una ilusión:

> si el análisis dimensional funciona tan bien, quizá pueda reemplazar la física detallada.

No puede. La razón es estructural.

Las dimensiones conservan cierta información sobre las magnitudes, pero descartan otra. Por eso el análisis dimensional es potente **porque comprime información**, y limitado **por la misma compresión**.

La pregunta final del capítulo será:

$$\boxed{ \text{¿qué información conserva la dimensión y qué información pierde?} }$$

[]{#lo-que-conserva}

### Lo que conserva {#fispm-c02-lo-que-conserva}

Una firma dimensional como

$$\mathbf d(Q) = (\alpha,\beta,\gamma,\delta,\varepsilon,\zeta,\eta)$$

conserva cómo una magnitud depende de las dimensiones base.

Esto permite reconstruir:

- cómo cambia su valor numérico al cambiar unidades base;

- qué productos y cocientes son dimensionalmente admisibles;

- qué términos pueden aparecer en una suma homogénea;

- qué combinaciones monomiales tienen dimensión uno;

- qué exponentes puede tener un ansatz monomial;

- qué parámetros pueden actuar como grupos de semejanza.

En este sentido, la dimensión conserva **estructura de escala**.

[]{#lo-que-pierde}

### Lo que pierde {#fispm-c02-lo-que-pierde}

La misma firma no registra, por sí sola:

- el significado físico completo;

- el tipo de magnitud;

- si un objeto es escalar, vector o tensor;

- el signo;

- la dirección;

- coeficientes numéricos;

- condiciones iniciales;

- condiciones de frontera;

- geometría detallada;

- régimen de aproximación;

- causalidad;

- estabilidad;

- mecanismo dinámico;

- dependencia funcional entre parámetros adimensionales.

Dos cantidades pueden compartir dimensión y diferir en muchas de estas propiedades.

Por tanto:

$$\boxed{ \text{misma dimensión} \neq \text{misma física}. }$$

[]{#primera-capacidad-detectar-incompatibilidades}

### Primera capacidad --- detectar incompatibilidades {#fispm-c02-primera-capacidad-detectar-incompatibilidades}

Si una ecuación propone: $x=x_0+at,$

entonces: $[x]=L,$

mientras: $[at]=LT^{-1}.$ La ecuación falla.

Ésta es una conclusión fuerte:

$$\boxed{ \text{una inhomogeneidad dimensional real invalida la expresión tal como está escrita}. }$$

No necesitamos medir el sistema.

No necesitamos resolver una ecuación diferencial.

No necesitamos conocer el valor de $a$. La contradicción está en la estructura.

[]{#primera-limitación-pasar-la-auditoría-no-prueba-la-ley}

### Primera limitación --- pasar la auditoría no prueba la ley {#fispm-c02-primera-limitaciuxf3n-pasar-la-auditoruxeda-no-prueba-la-ley}

Consideremos: $E=Cmv^2.$ Para cualquier número puro $C$: $[E]=ML^2T^{-2}.$

Por tanto, todas estas expresiones son dimensionalmente admisibles:

$$E=\frac12mv^2,$$

$$E=mv^2,$$

$$E=17mv^2,$$

$$E=-3mv^2.$$

Las dimensiones no distinguen entre ellas.

Así:

$$\boxed{ \text{homogeneidad} \text{ es necesaria en muchos modelos, pero no suficiente para la verdad física}. }$$

Esta fue la lección del Principio 12.

[]{#segunda-capacidad-inferir-escalas-y-exponentes}

### Segunda capacidad --- inferir escalas y exponentes {#fispm-c02-segunda-capacidad-inferir-escalas-y-exponentes}

Si aceptamos un ansatz: $Q=CX_1^{\alpha_1}\cdots X_n^{\alpha_n},$ La Proposición 3 convierte la homogeneidad en un sistema lineal. Por ejemplo, para el péndulo: $P=C\ell^\alpha g^\beta,$

obtenemos:

$$\alpha=\frac12,$$

$$\beta=-\frac12,$$

y por tanto: $P=C\sqrt{\frac{\ell}{g}}.$ La inferencia es rigurosa **dentro del ansatz declarado**.

[]{#segunda-limitación-la-clase-funcional-fue-una-hipótesis}

### Segunda limitación --- la clase funcional fue una hipótesis {#fispm-c02-segunda-limitaciuxf3n-la-clase-funcional-fue-una-hipuxf3tesis}

El análisis dimensional no demostró que el período fuera monomial.

Nosotros propusimos esa clase funcional. Al incorporar el ángulo inicial: $\varphi_0,$

Buckingham mostró que la forma más general es: $P= \sqrt{\frac{\ell}{g}} \Psi(\varphi_0).$ La función: $\Psi$

no es determinada por las dimensiones.

Por tanto:

$$\boxed{ \text{restricción dimensional} \neq \text{determinación funcional completa}. }$$

[]{#tercera-capacidad-descubrir-grupos-adimensionales}

### Tercera capacidad --- descubrir grupos adimensionales {#fispm-c02-tercera-capacidad-descubrir-grupos-adimensionales}

Con $n$ variables y matriz dimensional de rango $r$, el Teorema 5 permite encontrar:

$$n-r$$

grupos independientes: $\Pi_1,\ldots,\Pi_{n-r}.$ La relación física puede reorganizarse como: $\Phi(\Pi_1,\ldots,\Pi_{n-r})=0.$ Esto puede reducir drásticamente un problema experimental o numérico. En lugar de explorar cada variable dimensional por separado, podemos explorar el espacio reducido de parámetros adimensionales.

[]{#tercera-limitación-buckingham-no-determina-φ}

### Tercera limitación --- Buckingham no determina Φ {#fispm-c02-tercera-limitaciuxf3n-buckingham-no-determina-ux3c6}

El teorema produce: $\Phi(\Pi_1,\ldots,\Pi_k)=0,$

pero no suele producir: $\Phi.$ La función restante puede contener casi toda la física interesante del problema.

En el arrastre viscoso obtuvimos:

$$F = \rho v^2L^2 \Psi\left( \frac{\rho vL}{\mu} \right).$$

El análisis dimensional identifica:

- la escala de fuerza;

- el parámetro adimensional;

- la reducción de variables.

No determina la función: $\Psi.$

[]{#cuarta-capacidad-construir-semejanza}

### Cuarta capacidad --- construir semejanza {#fispm-c02-cuarta-capacidad-construir-semejanza}

Si dos sistemas preservan los mismos grupos adimensionales relevantes, pueden compararse dentro de una misma descripción reducida.

Por ejemplo, en un modelo viscoso:

$$\frac{\rho_1v_1L_1}{\mu_1} = \frac{\rho_2v_2L_2}{\mu_2}.$$

Esto permite diseñar:

- modelos a escala;

- comparaciones experimentales;

- familias de sistemas dinámicamente semejantes.

La semejanza es una de las aplicaciones más profundas del método.

[]{#cuarta-limitación-semejanza-dimensional-no-significa-identidad-física}

### Cuarta limitación --- semejanza dimensional no significa identidad física {#fispm-c02-cuarta-limitaciuxf3n-semejanza-dimensional-no-significa-identidad-fuxedsica}

Dos sistemas pueden compartir ciertos grupos $\Pi$ y, sin embargo, diferir en:

- geometría no incluida en el modelo;

- condiciones de frontera;

- rugosidad;

- propiedades constitutivas;

- campos externos;

- mecanismos adicionales;

- transiciones de régimen;

- variables omitidas.

Por eso la afirmación correcta siempre tiene la forma:

$$\boxed{ \text{semejanza respecto de un modelo declarado}. }$$

No:

$$\boxed{ \text{identidad física absoluta}. }$$

[]{#quinta-capacidad-revelar-variables-omitidas-indirectamente}

### Quinta capacidad --- revelar variables omitidas indirectamente {#fispm-c02-quinta-capacidad-revelar-variables-omitidas-indirectamente}

El análisis dimensional no puede inventar una variable que no incluimos. Pero puede producir señales de que el modelo es insuficiente. Por ejemplo, si experimentos realizados con la misma combinación dimensional predicha muestran comportamientos sistemáticamente diferentes, debemos preguntar si falta un parámetro.

La discrepancia puede sugerir:

- una viscosidad omitida;

- una longitud característica adicional;

- temperatura;

- elasticidad;

- una condición geométrica;

- otro mecanismo físico.

Así, el fracaso de una reducción dimensional puede funcionar como herramienta diagnóstica.

[]{#quinta-limitación-ninguna-inferencia-formal-recupera-una-premisa-ausente}

### Quinta limitación --- ninguna inferencia formal recupera una premisa ausente {#fispm-c02-quinta-limitaciuxf3n-ninguna-inferencia-formal-recupera-una-premisa-ausente}

Este punto merece quedar como principio final del capítulo.

**Principio 26 --- Ninguna conclusión dimensional puede exceder las premisas del modelo** El análisis dimensional puede deducir consecuencias rigurosas de una lista de magnitudes, dimensiones e hipótesis de invariancia, pero no puede establecer por sí solo la corrección física de esas premisas ni recuperar variables, mecanismos o regímenes que el modelo haya omitido.

Podemos escribir:

Éste es uno de los riesgos más importantes del método.

[]{#la-advertencia-de-zorich}

### La advertencia de Zorich {#fispm-c02-la-advertencia-de-zorich}

Zorich cierra sus ejemplos dimensionales señalando que la eficacia del método depende principalmente de comprender correctamente la naturaleza del fenómeno al que se aplica.[^40]

Esta observación resume nuestra arquitectura. El análisis dimensional es especialmente valioso cuando aún no conocemos toda la ley física, porque puede revelar conexiones generales y orientar la investigación.

Pero precisamente en esos casos debemos ser más cuidadosos con:

- la selección de variables;

- las idealizaciones;

- las escalas;

- el dominio físico.

No basta con «hacer cuadrar las dimensiones».

[]{#tabla-de-decisión-del-análisis-dimensional}

### Tabla de decisión del análisis dimensional {#fispm-c02-tabla-de-decisiuxf3n-del-anuxe1lisis-dimensional}

Ante un problema nuevo, usaremos esta secuencia.

  Pregunta                                             Si la respuesta es sí    Si la respuesta es no
  ---------------------------------------------------- ------------------------ -------------------------
  ¿Están definidas las magnitudes?                     seguir                   precisar significado
  ¿Las unidades y referencias son coherentes?          seguir                   corregir representación
  ¿La ecuación es homogénea?                           seguir                   localizar error
  ¿Los argumentos de funciones son de dimensión uno?   seguir                   normalizar/corregir
  ¿La lista de variables es físicamente plausible?     aplicar inferencia       revisar modelo
  ¿Hay grupos $\Pi$?                                   reducir variables        revisar rango/lista
  ¿Se preservan los $\Pi$ relevantes entre sistemas?   comparar por semejanza   no afirmar semejanza
  ¿La función adimensional está determinada?           usarla                   teoría/datos necesarios
  ¿El resultado está dentro del régimen del modelo?    interpretar              no extrapolar

Esta tabla no es un algoritmo que reemplace el juicio físico. Es una lista de control para organizarlo.

[]{#qué-distingue-una-demostración-dimensional-de-una-afirmación-física}

### Qué distingue una demostración dimensional de una afirmación física {#fispm-c02-quuxe9-distingue-una-demostraciuxf3n-dimensional-de-una-afirmaciuxf3n-fuxedsica}

A lo largo de FPM mantendremos dos capas.

[]{#capa-matemática}

#### Capa matemática {#fispm-c02-capa-matemuxe1tica}

Ejemplos:

$$A\alpha=0,$$

$$\operatorname{rank}A=r,$$

$$n-r,$$

$$s_Q=\sum_i\alpha_is_i.$$

Estas conclusiones pueden demostrarse exactamente bajo hipótesis formales.

[]{#capa-física}

#### Capa física {#fispm-c02-capa-fuxedsica}

Ejemplos:

- estas son las variables relevantes;

- esta aproximación es adecuada;

- esta constante puede ignorarse;

- estos dos sistemas son comparables;

- este régimen experimental corresponde al modelo.

Estas afirmaciones deben justificarse físicamente. La separación no debilita el rigor. Lo aumenta.

[]{#exactitud-matemática-y-adecuación-física}

### Exactitud matemática y adecuación física {#fispm-c02-exactitud-matemuxe1tica-y-adecuaciuxf3n-fuxedsica}

Volvemos así a una idea del capítulo 1.

Podemos resolver exactamente un modelo inadecuado.

También podemos trabajar con una aproximación controlada de un modelo mucho más adecuado. El análisis dimensional participa de esta misma distinción. Una matriz dimensional puede ser impecable.

Un sistema de exponentes puede estar perfectamente resuelto.

Los grupos $\Pi$ pueden ser correctos.

Y, sin embargo, la representación física inicial puede ser insuficiente.

Por eso:

$$\boxed{ \text{exactitud matemática relativa al modelo} \neq \text{adecuación física del modelo}. }$$

[]{#autoexplicación-final}

### Autoexplicación final {#fispm-c02-autoexplicaciuxf3n-final}

**Pausa de autoexplicación** Sin consultar las secciones anteriores, explica:

1.  una cosa que una incompatibilidad dimensional puede demostrar de manera concluyente;

2.  una cosa que la homogeneidad nunca demuestra por sí sola;

3.  qué información aporta Buckingham $\Pi$;

4.  qué información deja sin determinar;

5.  por qué la selección de variables pertenece a la física y no solamente al álgebra;

6.  qué significa decir que dos sistemas son semejantes «respecto de un modelo».

[]{#práctica-final}

### Práctica final {#fispm-c02-pruxe1ctica-final}

**Ejercicio 28 --- Auditoría integral de un modelo dimensional**

**Objetivo:** `Síntesis final`

**Intenta primero: 5--10 min antes de leer la solución.**

Un investigador propone que el tiempo característico $\tau$ de cierto fenómeno depende de: $L,\qquad v,\qquad \rho,\qquad \mu,$

donde:

$$[L]=L,$$

$$[v]=LT^{-1},$$

$$[\rho]=ML^{-3},$$

$$[\mu]=ML^{-1}T^{-1}.$$

Propone además:

$$\tau = \frac Lv \left[ 1+ \frac{\rho vL}{\mu} \right].$$

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-6}

Audita dimensionalmente la fórmula.

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-6}

Construye la matriz dimensional de: $\tau,\ L,\ v,\ \rho,\ \mu.$

Determina $n$, $r$ y $n-r$.

### C. Buckingham {#fispm-c02-c.-buckingham}

Construye dos grupos adimensionales independientes y escribe la forma general que Buckingham permite para $\tau$.

### D. Diagnóstico {#fispm-c02-d.-diagnuxf3stico}

Decide si la fórmula propuesta por el investigador queda demostrada por el análisis dimensional.

### E. Variación {#fispm-c02-e.-variaciuxf3n}

Supón que nuevos experimentos muestran que dos sistemas con el mismo valor de: $\frac{\rho vL}{\mu}$

tienen valores distintos de: $\frac{\tau v}{L}.$

Da al menos tres explicaciones físicamente plausibles que deberían investigarse antes de concluir que Buckingham falla.

### F. Síntesis epistemológica {#fispm-c02-f.-suxedntesis-epistemoluxf3gica}

Clasifica cada afirmación como:

- consecuencia dimensional;

- hipótesis de modelización;

- información física adicional.

1.  $\tau v/L$ tiene dimensión uno.

2.  $\rho vL/\mu$ tiene dimensión uno.

3.  solo las variables $L,v,\rho,\mu$ son relevantes.

4.  existe una función $\Psi$ tal que

$$\frac{\tau v}{L} = \Psi\left( \frac{\rho vL}{\mu} \right).$$

1.  $\Psi(x)=1+x$.

2.  dos sistemas con igual argumento de $\Psi$ deben compararse dentro del mismo modelo.

**Solución**

### A. Recuperación {#fispm-c02-a.-recuperaciuxf3n-7}

Primero: $\left[\frac Lv\right] = \frac{L}{LT^{-1}} = T.$

Además: $\left[ \frac{\rho vL}{\mu} \right] = 1.$ Por tanto: $\left[ 1+\frac{\rho vL}{\mu} \right] = 1.$ Entonces: $[\tau]=T.$ La expresión es dimensionalmente homogénea.

### B. Consolidación {#fispm-c02-b.-consolidaciuxf3n-7}

En el orden $(T,L,M)$:

$$\tau: \begin{pmatrix} 1\\ 0\\ 0 \end{pmatrix}, \qquad L: \begin{pmatrix} 0\\ 1\\ 0 \end{pmatrix},$$

$$v: \begin{pmatrix} -1\\ 1\\ 0 \end{pmatrix}, \qquad \rho: \begin{pmatrix} 0\\ -3\\ 1 \end{pmatrix},$$

$$\mu: \begin{pmatrix} -1\\ -1\\ 1 \end{pmatrix}.$$

Así: $n=5.$

Hay tres columnas dimensionalmente independientes, de modo que: $r=3.$

Por tanto:

$$\boxed{ n-r=2. }$$

### C. Buckingham {#fispm-c02-c.-buckingham-1}

Dos grupos posibles son:

$$\boxed{ \Pi_1 = \frac{\tau v}{L} }$$

y:

$$\boxed{ \Pi_2 = \frac{\rho vL}{\mu}. }$$

Buckingham permite: $\Phi(\Pi_1,\Pi_2)=0.$

Si podemos resolver para $\Pi_1$:

$$\boxed{ \frac{\tau v}{L} = \Psi\left( \frac{\rho vL}{\mu} \right). }$$

Equivalentemente:

$$\boxed{ \tau = \frac Lv \Psi\left( \frac{\rho vL}{\mu} \right). }$$

### D. Diagnóstico {#fispm-c02-d.-diagnuxf3stico-1}

La fórmula propuesta:

$$\tau = \frac Lv \left[ 1+ \frac{\rho vL}{\mu} \right]$$

corresponde a elegir: $\Psi(x)=1+x.$

Buckingham no determina esa función.

Por tanto:

$$\boxed{ \text{la fórmula pasa el control dimensional, pero no queda demostrada por él}. }$$

### E. Variación {#fispm-c02-e.-variaciuxf3n-1}

Si dos sistemas con el mismo: $\frac{\rho vL}{\mu}$

producen distinto: $\frac{\tau v}{L},$

antes de culpar al teorema debemos revisar, por ejemplo:

1.  **variables omitidas**: rugosidad, geometría adicional, temperatura u otro parámetro relevante;

2.  **diferentes condiciones de frontera o iniciales**;

3.  **regímenes físicos distintos** no capturados por el modelo;

4.  errores experimentales o definición no equivalente de $\tau$;

5.  hipótesis constitutivas distintas para el medio.

Buckingham trabaja sobre el modelo declarado. Una discrepancia puede indicar que el modelo no contiene toda la física pertinente.

### F. Síntesis epistemológica {#fispm-c02-f.-suxedntesis-epistemoluxf3gica-1}

**1.**

$$\frac{\tau v}{L}$$

tiene dimensión uno:

**consecuencia dimensional**.

**2.**

$$\frac{\rho vL}{\mu}$$

tiene dimensión uno:

**consecuencia dimensional**.

**3.**

Solo $L,v,\rho,\mu$ son relevantes:

**hipótesis de modelización**.

**4.**

$$\frac{\tau v}{L} = \Psi\left( \frac{\rho vL}{\mu} \right)$$

es la reducción dimensional derivada de Buckingham **condicionada a esa lista de variables y a sus hipótesis de invariancia**.

**5.**

$$\Psi(x)=1+x$$

es **información física adicional** o una hipótesis funcional que requiere justificación.

**6.**

Comparar sistemas con el mismo argumento adimensional es una consecuencia del marco de semejanza **dentro del mismo modelo**.

La distinción final queda:

$$\boxed{ \text{álgebra dimensional} \quad|\quad \text{premisas del modelo} \quad|\quad \text{contenido físico adicional}. }$$

[]{#mapa-final-del-capítulo}

### Mapa final del capítulo {#fispm-c02-mapa-final-del-capuxedtulo}

El capítulo comenzó con una advertencia sencilla:

$$\boxed{ \text{un número no es todavía una magnitud física}. }$$

Desde allí construimos:

$$\begin{gathered} \text{número} \to \text{valor}\\[2pt]\Downarrow\\[2pt]\text{unidad} \to \text{tipo de magnitud}\\[2pt]\Downarrow\\[2pt]\text{SI} \to \text{unidad derivada}\\[2pt]\Downarrow\\[2pt]\text{dimensión} \to \text{homogeneidad}\\[2pt]\Downarrow\\[2pt]\text{auditoría} \to \text{dimensión uno}\\[2pt]\Downarrow\\[2pt]\text{escala característica} \to \text{adimensionalización}\\[2pt]\Downarrow\\[2pt]\text{inferencia} \to \text{semejanza}\\[2pt]\Downarrow\\[2pt]\text{Buckingham }\Pi \to \text{modelización}. \end{gathered}$$

La cadena no termina en una fórmula.

Termina en una disciplina de lectura:

$$\boxed{ \text{¿qué sabemos?} \quad \text{¿qué suponemos?} \quad \text{¿qué demostramos?} \quad \text{¿qué sigue siendo físico?} }$$

[]{#cierre-1}

### Cierre {#fispm-c02-cierre-1}

El análisis dimensional es una herramienta extraordinaria porque detecta estructura sin exigir conocer todos los detalles de una teoría. Puede decir mucho con poca información. Pero no puede decir más de lo que esa información contiene.

Por eso su uso riguroso exige dos movimientos simultáneos:

$$\boxed{ \text{explotar al máximo las consecuencias dimensionales} }$$

y

$$\boxed{ \text{no atribuirles contenido físico que no poseen}. }$$

[]{#fpm-i-02-referencias}

Con esto queda cerrado el capítulo:

$$\boxed{ \text{Magnitudes, unidades y análisis dimensional}. }$$

El siguiente capítulo del tratado será:

$$\boxed{ \text{el capítulo 3 — Medición, incertidumbre, estimación y órdenes de magnitud}. }$$

Allí cambiaremos de pregunta.

Hasta ahora estudiamos principalmente cómo **representar y estructurar magnitudes**, elegir escalas y construir variables de dimensión uno. A continuación cambiaremos desde la estructura del modelo hacia la **obtención experimental de valores**: mediciones finitas, incertidumbre, cifras significativas y estimaciones cuantitativas. El desarrollo detallado de estimaciones tipo Fermi y de precisión experimental queda deliberadamente allí, para no duplicar el alcance de este capítulo.

------------------------------------------------------------------------

[]{#fispm-c02-notas-y-fuentes-8 label="fispm-c02-notas-y-fuentes-8"}

[]{#bibliografía-y-fuentes-normativas}

## Bibliografía y fuentes normativas {#fispm-c02-bibliografuxeda-y-fuentes-normativas .unnumbered}

[]{#fuentes-normativas}

### Fuentes normativas {#fispm-c02-fuentes-normativas}

**Bureau International des Poids et Mesures (BIPM).** *The International System of Units (SI)*. 9.ª edición, versión 4.01, junio de 2026. DOI: 10.59161/AUEZ1291. Se utilizaron especialmente §§2.1--2.3.4, capítulo 3 y §5.4.7.

**Joint Committee for Guides in Metrology (JCGM).** *International Vocabulary of Metrology --- Basic and general concepts and associated terms (VIM)*. 3.ª edición, JCGM 200:2012, versión 2008 con correcciones menores. DOI: 10.59161/JCGM200-2012. Se utilizaron especialmente las entradas 1.1, 1.2, 1.7--1.9, 1.12, 1.19 y 1.20.

**BIPM.** «SI --- Defining constants», «SI --- Base units» y «SI --- Prefixes». Fuentes web oficiales utilizadas para controlar la formulación vigente del SI y la lista contemporánea de prefijos.

[]{#fuentes-matemático-físicas}

### Fuentes matemático-físicas {#fispm-c02-fuentes-matemuxe1tico-fuxedsicas}

**Zorich, Vladimir.** *Mathematical Analysis of Problems in the Natural Sciences*. Springer, 2011. DOI: 10.1007/978-3-642-14813-2. Parte I, especialmente cap. 1, §§1.1--1.3, pp. 5--10; cap. 2, pp. 11--21.

**Shankar, Ramamurti.** *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*. Expanded edition. Yale University Press, 2019. Cap. 1, §1.3, p. 4.

[^1]: R. Shankar, *Fundamentals of Physics I: Mechanics, Relativity, and Thermodynamics*, expanded ed., Yale University Press, 2019, cap. 1, §1.3, p. 4.

[^2]: JCGM, *International Vocabulary of Metrology --- Basic and general concepts and associated terms (VIM)*, 3.ª ed., JCGM 200:2012, entrada 1.1, «quantity», DOI 10.59161/JCGM200-2012.

[^3]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §2.1, p. 123, DOI 10.59161/AUEZ1291.

[^4]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.2, «kind of quantity».

[^5]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.9, «measurement unit».

[^6]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.9, «measurement unit».

[^7]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.19, «quantity value».

[^8]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §§2.2--2.3.2, pp. 123--132, DOI 10.59161/AUEZ1291.

[^9]: BIPM, *SI --- Defining constants*; véase también *SI Brochure*, v4.01 (2026), §2.2, pp. 123--125.

[^10]: BIPM, *SI --- Defining constants*; véase también *SI Brochure*, v4.01 (2026), §2.2, pp. 123--125.

[^11]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §§2.2--2.3.2, pp. 123--132, DOI 10.59161/AUEZ1291.

[^12]: BIPM, *SI --- Base units*; véase también *SI Brochure*, v4.01 (2026), §2.3.1, pp. 126--131.

[^13]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01, junio de 2026, §§2.2--2.3.2, pp. 123--132, DOI 10.59161/AUEZ1291.

[^14]: BIPM, *SI --- Prefixes*; 27.ª CGPM, Resolución 3 (2022), «On the extension of the range of SI prefixes».

[^15]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01 (2026), §2.3.4, pp. 133--137.

[^16]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.4, pp. 133--137; compárese JCGM, *VIM*, entrada 1.12, «coherent derived unit».

[^17]: BIPM, *The International System of Units (SI)*, 9.ª ed., versión 4.01 (2026), §2.3.4, pp. 133--137.

[^18]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.4, tabla 4, pp. 133--136.

[^19]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.7, «quantity dimension».

[^20]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.3, pp. 132--133.

[^21]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.7, «quantity dimension».

[^22]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.7, «quantity dimension».

[^23]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.1--1.2, pp. 5--8, DOI 10.1007/978-3-642-14813-2.

[^24]: BIPM, *SI Brochure*, v4.01 (2026), §2.3.3, pp. 132--133.

[^25]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.2, pp. 6--8.

[^26]: JCGM, *VIM*, 3.ª ed., entradas 1.2, 1.4 y 1.7.

[^27]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.1--1.2, pp. 5--8.

[^28]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.8, «quantity of dimension one».

[^29]: JCGM, *VIM*, 3.ª ed., entradas 1.9, 1.12 y 1.20.

[^30]: BIPM, *SI Brochure*, v4.01 (2026), §§2.3.3--2.3.4, pp. 132--136, y §5.4.7, pp. 146--147.

[^31]: BIPM, *SI Brochure*, v4.01 (2026), §§2.3.3--2.3.4, pp. 132--136, y §5.4.7, pp. 146--147.

[^32]: JCGM, *VIM*, 3.ª ed., JCGM 200:2012, entrada 1.8, «quantity of dimension one».

[^33]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §§1.2--1.3, pp. 6--10, y cap. 2, §§2.1--2.3, pp. 11--14.

[^34]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.3.2, p. 10, y cap. 2, pp. 11--18.

[^35]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §1.3.1, pp. 9--10; §1.3.2, p. 10.

[^36]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, cap. 2, «Examples of applications», pp. 11--21.

[^37]: Zorich, op. cit., §2.3, «Period of oscillation of a heavy pendulum (inclusion of g)», pp. 13--14.

[^38]: Zorich, op. cit., §2.5, «Drag force for the motion of a ball in a non-viscous medium», pp. 14--15, y §2.6, «...in a viscous medium», pp. 15--16.

[^39]: Zorich, op. cit., §2.5, pp. 14--15, ecuación (2.1).

[^40]: V. Zorich, *Mathematical Analysis of Problems in the Natural Sciences*, Springer, 2011, Parte I, §2.8, «Concluding remarks», pp. 18--21.

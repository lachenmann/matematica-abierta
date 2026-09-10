$$
[\mathrm{POST}]
\to
[\mathrm{MOD}]
\to
[\mathrm{EMP}]
\to
[\mathrm{IC}]
\to
[\mathrm{MATH}]
\to
[\mathrm{APPROX}]
\to
[\mathrm{MATH}]
\to
[\mathrm{OBS}].
$$
No todas las derivaciones siguen este orden.

El esquema solo muestra que una solución física puede combinar:

- premisas teóricas;
- hipótesis sobre el sistema;
- datos;
- aproximaciones;
- deducciones.

Por eso llamaremos **demostración** únicamente al tramo matemático apropiado.

La argumentación física completa es más amplia.
Supongamos que un texto parte de una relación física $L$ y mediante álgebra obtiene otra relación $R$.

Si $L$ es empírica o postulada, podemos demostrar:

$$
L\Longrightarrow R.
$$
Pero no hemos demostrado que $L$ describa la naturaleza.

Hemos demostrado una implicación dentro del marco.

Esta es una diferencia especialmente importante para el lector formado en matemática pura.

En matemáticas, las premisas suelen presentarse explícitamente como axiomas, definiciones o hipótesis.

En física, parte de esas premisas puede estar escondida en frases aparentemente inocentes como:

- «despreciemos el rozamiento»;
- «supongamos un cuerpo rígido»;
- «experimentalmente se encuentra que…»;
- «tomemos el sistema inicialmente en reposo».

Nuestro protocolo hace visibles esas entradas.
Cuando una ecuación sea ambigua, seguiremos esta secuencia.

#### Pregunta 1

¿Está fijando significado?

Sí:

$$
[\mathrm{DEF}].
$$
#### Pregunta 2

¿Conecta el formalismo con un procedimiento de medida?

Sí:

$$
[\mathrm{OBS}].
$$
#### Pregunta 3

¿Es una condición particular de preparación o de borde?

Inicial:

$$
[\mathrm{IC}].
$$
Frontera:

$$
[\mathrm{BC}].
$$
#### Pregunta 4

¿Introduce una simplificación del sistema real?

Exacta dentro del modelo:

$$
[\mathrm{MOD}].
$$
Como reemplazo cercano:

$$
[\mathrm{APPROX}].
$$
#### Pregunta 5

¿Funciona como premisa estructural de la teoría?

$$
[\mathrm{POST}].
$$
#### Pregunta 6

¿Su respaldo es primordialmente empírico?

$$
[\mathrm{EMP}].
$$
#### Pregunta 7

¿Se sigue lógicamente de premisas ya declaradas?

$$
[\mathrm{MATH}].
$$
La clasificación puede requerir contexto histórico o teórico adicional.

No siempre será mecánica.
Tres casos fronterizos merecen quedar visibles porque reaparecerán en el resto del tratado:

La frontera entre `[EMP]` y `[POST]` no siempre coincide con una frontera filosófica absoluta.

Una relación históricamente descubierta como regularidad empírica puede ser incorporada después como parte estructural de un marco.

Para nuestro uso:

- `[EMP]` enfatiza su papel como regularidad respaldada experimentalmente;
- `[POST]` enfatiza su papel como premisa organizadora del formalismo.

En los casos dudosos, la solución deberá explicar **por qué** adopta una etiqueta.

El objetivo del protocolo no es fingir que toda epistemología de la física cabe en nueve casillas.

Es impedir que diferencias importantes desaparezcan bajo una sola palabra: «ecuación».
Supongamos que definimos una magnitud $T$ mediante una construcción teórica.

Eso puede ser `[DEF]`.

Pero si además especificamos que cierto instrumento produce una lectura utilizada para estimar $T$, esa conexión es `[OBS]`.

Una misma magnitud puede tener:

$$
[\mathrm{DEF}]
\qquad
\text{significado teórico}
$$
y

$$
[\mathrm{OBS}]
\qquad
\text{procedimiento de acceso experimental}.
$$
Confundir ambos niveles puede ocultar problemas de calibración.
Una observación individual como

$$
x=4.2
$$
no es una ley física.

Es un dato o resultado de medición.

Una colección de datos puede sugerir una relación.

Pero el salto

$$
\{(x_i,y_i)\}
\longrightarrow
y=f(x)
$$
no es una deducción puramente lógica.

En §9 demostraremos que un conjunto finito de datos puede ser compatible con infinitas funciones distintas.

Esta sección prepara la distinción.
La regla práctica será sencilla: una demostración matemática comienza una vez declaradas las premisas físicas. Si durante la derivación aparece una nueva premisa empírica, de modelo, de aproximación o de observación, debe marcarse como tal.

### 6.4. Ejercicios

::: {.ma-block .ma-enunciado #fpm-i-01-e019}
**Ejercicio FPM-I-01-E019 — ¿Qué tipo de afirmación es?**

**Familia:** `E-CON / BASIC`

Clasifica cada afirmación con la etiqueta más adecuada y justifica.

1. $\Delta t:=t_f-t_i$.
2. «El cuerpo se tratará como partícula puntual».
3. $x(0)=3$, cuando el problema especifica que el sistema se prepara inicialmente con ese valor.
4. $u=0$ sobre el borde de una región.
5. $1-2\varepsilon+\varepsilon^2\approx1-2\varepsilon$ para $|\varepsilon|$ suficientemente pequeño.
6. $A=C$, obtenido únicamente a partir de $A=B$ y $B=C$.
7. Una relación $Y=kX$ que resume un patrón experimental dentro de un intervalo medido.
8. Una regla que convierte píxeles de una imagen calibrada en una posición física.
9. Un principio estructural que la teoría adopta como premisa y del que se derivan consecuencias.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

1. **`[DEF]`.** Fija el significado de $\Delta t$.

2. **`[MOD]`.** Introduce una idealización: un cuerpo extendido se modela como punto.

3. **`[IC]`.** Fija el estado inicial de una realización particular; no es una ley general.

4. **`[BC]`.** Prescribe información en la frontera del dominio.

5. **`[APPROX]`.** Reemplaza una relación por otra cercana en un régimen declarado.

6. **`[MATH]`.** Es consecuencia de la transitividad de la igualdad y no añade una premisa física.

7. **`[EMP]`.** Su respaldo depende del patrón observado experimentalmente.

8. **`[OBS]`.** Conecta el formalismo con un procedimiento de medición.

9. **`[POST]`.** Funciona como premisa estructural del marco.

La estrategia general es:

$$
\boxed{
\text{preguntar por origen y función, no por apariencia algebraica}.
}
$$
:::

::: {.ma-block .ma-enunciado #fpm-i-01-e020}
**Ejercicio FPM-I-01-E020 — La misma fórmula, distinto estatus**

**Familia:** `E-CON / CORE`

Construye cuatro contextos distintos en los que la fórmula

$$
y=kx
$$
tenga respectivamente estatus:

1. `[DEF]`;
2. `[EMP]`;
3. `[MOD]`;
4. `[MATH]`.

Después explica por qué no existe una función que, leyendo únicamente la cadena de símbolos $y=kx$, determine correctamente su estatus físico.

:::

::: {.ma-block .ma-comprobacion}
**Solución**

##### 1. Como definición

Definimos una nueva variable:

$$
[\mathrm{DEF}]
\qquad
y:=kx.
$$
La ecuación fija qué significa $y$.

##### 2. Como relación empírica

Medimos $x$ e $y$ y encontramos experimentalmente que, dentro de cierto intervalo,

$$
[\mathrm{EMP}]
\qquad
y\approx kx.
$$
La relación resume la evidencia.

##### 3. Como hipótesis de modelo

Decidimos idealizar un sistema mediante una dependencia exactamente lineal:

$$
[\mathrm{MOD}]
\qquad
y=kx.
$$
La linealidad exacta pertenece al modelo.

##### 4. Como consecuencia matemática

Partimos de

$$
y=ka
$$
y de

$$
a=x.
$$
Por sustitución:

$$
[\mathrm{MATH}]
\qquad
y=kx.
$$
##### Conclusión

La secuencia de caracteres

$$
y=kx
$$
es la misma en los cuatro casos.

Por tanto, ninguna regla que inspeccione **solo** la sintaxis puede distinguirlos.

El estatus depende de información contextual:

- cómo se introdujo la ecuación;
- qué premisas la sostienen;
- qué papel cumple;
- cómo se conecta con observaciones.

En términos de §5:

$$
\boxed{
\text{la sintaxis pertenece al núcleo formal;
el estatus exige también el diccionario de interpretación y la historia lógica del argumento}.
}
$$
:::

### 6.5. Síntesis

A partir de ahora no leeremos una ecuación física como una entidad homogénea.

Preguntaremos:

$$
\boxed{
\text{¿qué clase de afirmación es?}
}
$$
La taxonomía canónica es:

$$
\boxed{
[\mathrm{DEF}],\,
[\mathrm{EMP}],\,
[\mathrm{POST}],\,
[\mathrm{MOD}],\,
[\mathrm{APPROX}],\,
[\mathrm{IC}],\,
[\mathrm{BC}],\,
[\mathrm{MATH}],\,
[\mathrm{OBS}]
}
$$
y la regla fundamental es:

$$
\boxed{
\text{la forma matemática no determina el estatus físico}.
}
$$
Una derivación físicamente rigurosa debe distinguir:

$$
\text{premisas físicas}
\quad+\quad
\text{condiciones}
\quad+\quad
\text{idealizaciones}
\quad+\quad
\text{aproximaciones}
\quad+\quad
\text{deducción matemática}
\quad+\quad
\text{conexión observacional}.
$$
Con esta herramienta ya podemos abordar una distinción más macroscópica.

¿Qué diferencia hay entre una **ley**, un **modelo** y una **teoría**?

Ése será el objeto de:

$$
\boxed{
\text{§7 — Ley, modelo y teoría}.
}
$$

---

## 7. Ley, modelo y teoría {#fpm-i-01-s07}

### 7.1. Tres niveles de organización

En física encontramos continuamente expresiones como:

- «ley de…»;
- «modelo de…»;
- «teoría de…».

Es fácil tratarlas como sinónimos vagos de «conjunto de ecuaciones».

Pero las seis secciones anteriores ya nos permiten ver que no cumplen la misma función.

Una **ley** suele expresar una regularidad, relación o principio físico.

Un **modelo** representa un sistema o una clase de sistemas bajo determinadas hipótesis.

Una **teoría** proporciona una arquitectura más amplia dentro de la cual pueden construirse muchos modelos y derivarse muchas relaciones.

Por tanto, nuestra primera imagen será:

$$
\boxed{
\text{ley}
\longrightarrow
\text{ingrediente estructural}
}
$$

$$
\boxed{
\text{modelo}
\longrightarrow
\text{representación situada de un sistema}
}
$$

$$
\boxed{
\text{teoría}
\longrightarrow
\text{marco que organiza familias de modelos}
}
$$

Estas flechas no expresan una inclusión conjuntista literal.

No estamos diciendo:

$$
\text{ley}\subset\text{modelo}\subset\text{teoría}
$$

# Auditoría matemática independiente — EXP003

## Fuente y alcance

Única fuente matemática: `libros/capitulos/sucesiones-y-la-primera-nocion-rigurosa-de-limite.md`, desde «Dos sucesiones que parecen iguales durante muchísimo tiempo» hasta antes del siguiente subtítulo de nivel tres. No se consultaron fuentes matemáticas externas ni se incorporó la definición formal de límite de secciones posteriores.

La primera fase estudió el texto independientemente del guion pedagógico. Después se revisaron la propuesta y el guion definitivo; los resultados y sus huellas se registran al final de este documento.

## Hipótesis que deben acompañar la explicación

- Los índices son naturales y empiezan en cero: `n=0,1,2,…`.
- La primera regla es `a_n=1/(n+1)` para todos esos índices.
- La segunda regla coincide con la primera cuando `0≤n≤10^6` y vale uno cuando `n>10^6`.
- El umbral pertenece al tramo común. El primer índice que usa la segunda rama es `10^6+1`.

## Valores y conteo exactos

| Índice | Primera sucesión | Segunda sucesión |
|---|---|---|
| 0 | 1 | 1 |
| 1 | 1/2 | 1/2 |
| 2 | 1/3 | 1/3 |
| 1.000.000 | 1/1.000.001 | 1/1.000.001 |
| 1.000.001 | 1/1.000.002 | 1 |
| 1.000.002 | 1/1.000.003 | 1 |

El tramo común contiene **1.000.001 términos**, porque incluye ambos extremos y empieza en cero. «Más de un millón» es exacto. «Los primeros un millón de términos» es una afirmación verdadera sobre un subconjunto del tramo, pero pierde la precisión relevante de la frontera; conviene explicitar el conteo inclusivo al mostrar el umbral.

Para `a_n`, el denominador es positivo y aumenta una unidad con cada incremento del índice. Por ello `a_{n+1}<a_n`, todos sus términos son positivos y la regla sigue produciendo términos cada vez menores. Para `b_n`, todos los términos posteriores al umbral valen exactamente uno.

## Idea esencial y cautela lógica

Una muestra finita de valores, considerada por sí sola, admite distintas continuaciones. Las **reglas completas** de estas dos sucesiones sí permiten describir sus comportamientos posteriores. No debe confundirse la insuficiencia de datos finitos con la imposibilidad de razonar a partir de una ley válida para todos los índices.

El par concreto sí se distingue observando el índice `1.000.001`. Por tanto, sería falso decir «ninguna cantidad finita de observaciones distingue estas dos sucesiones» sin restringir esa frase al tramo común. La afirmación universal correcta es: para cualquier cantidad finita previamente elegida de términos observados, pueden construirse sucesiones que coincidan en esos datos y se comporten de maneras distintas después.

Para un prefijo de longitud positiva `L`, el último índice observado es `L−1`. Se define una continuación que coincide con `a_n` hasta `L−1` inclusive y vale uno desde `L`. Conserva exactamente los `L` valores observados y difiere inmediatamente después. La construcción funciona para cualquier entero finito positivo `L`; no necesita que sea un millón.

Incluso si la muestra usa un conjunto finito arbitrario de índices, puede tomarse un umbral al menos igual a su máximo. La continuación conserva todos los valores muestreados. Esta ampliación precisa la lógica, pero no es necesario añadirla al video si complica el argumento del pasaje.

## Criterios para la imagen

- Representar términos como puntos o marcas discretas, sin sugerir que todos los reales intermedios son índices.
- Un recorrido o barrido puede guiar la mirada entre índices; debe distinguirse de la sucesión misma.
- Si se omiten índices mediante puntos suspensivos, un corte o un cambio de escala, explicitar la omisión. No representar un millón de pasos como una distancia uniforme falsa junto a los primeros índices.
- Para el salto, conservar el eje de valores o señalar el cambio de escala. La altura uno y los valores próximos a una millonésima tienen una diferencia real enorme.
- Si se exagera visualmente la separación de valores diminutos para leerlos, indicar ampliación y sus valores exactos; una tabla exacta junto al diagrama evita confundir la escala.
- Las etiquetas de los términos de frontera deben aparecer al pronunciar el índice correspondiente, especialmente `10^6+1`.
- Puede formularse la conclusión mediante «todos los términos suficientemente tardíos», como en la fuente. Evitar introducir una definición epsilon-N o una prueba formal de límites ausente del pasaje.

## Validación independiente

`validar_matematica.py` usa `fractions.Fraction`, biblioteca estándar, sin importar Manim ni las funciones del realizador. Comprueba exhaustivamente los 1.000.001 términos comunes, la frontera exacta, monotonía y positividad en índices representativos, la rama constante y la generalización a prefijos de distintas longitudes. La comprobación finita acompaña el argumento algebraico universal expuesto arriba y no lo sustituye.

Errores potenciales prevenidos: conteo desde uno, desigualdad estricta incorrecta en el umbral, denominador desplazado en la primera diferencia, confundir evidencia finita con ley completa y dibujar una curva continua como sucesión.

## Revisión independiente del guion propuesto

Se leyó `GUION_PROPUESTO.md` completo. El argumento y sus 18 microtramos son fieles al pasaje: regla inicial, naturales desde cero, términos, segunda regla por ramas, tramo común, conteo inclusivo, frontera, primera diferencia, comportamientos posteriores, alcance de una muestra y pregunta de los términos suficientemente tardíos.

La revisión no detecta afirmaciones matemáticas falsas en la propuesta. Se señalaron mejoras de locución antes de sintetizar: expresar el conteo como «un millón de términos, más el término de índice cero» y leer los denominadores largos como sumas. La dirección comunicó que aplicaría esas correcciones a la versión canónica. También se recomendó «uno dividido por la suma de ene y uno» para evitar ambigüedad auditiva en `1/(n+1)`.

La frase «los puntos se acercan a la altura cero» describe la tendencia informal del pasaje y no se usa como sustituto de una prueba formal. Los tramos de respuesta y generalización distinguen expresamente los datos observados de la regla de continuación, por lo que evitan la sobregeneralización advertida arriba.

## Revisión final del guion canónico y la procedencia

Fecha: 2026-10-23. Revisor: función matemática independiente, posterior a la generación pedagógica.

- `guion.json`, SHA-256: `c0ec7c04dabe0f75826276fe0ca7a77de8033bb1576f49f958723f74416c0b36`.
- `GUION.md`, SHA-256: `f0bc93e1b85a2de5ceddc3904dd25d66344e90da05ef545e2a3cfebf23f00714`.
- Se compararon automáticamente los 18 textos de locución del JSON con los 18 apartados del documento: identidad exacta, ignorando sólo el espacio exterior de cada apartado.
- Se leyeron nuevamente todos los microtramos. Las aclaraciones del denominador `n+1`, el conteo inclusivo y los denominadores de frontera están incorporadas y son matemáticamente correctas.
- La frontera se trata en el orden correcto: `n=10^6`, luego `n=10^6+1`, luego se revela la segunda rama. La conclusión aborda todos los términos suficientemente tardíos sin añadir una definición formal ausente de la fuente.
- Los tramos 15–17 distinguen explícitamente la información finita observada de las reglas posteriores y no afirman que el par concreto sea indistinguible ante cualquier muestra finita.

**Resultado del guion canónico: cero errores matemáticos detectados; no se solicita ninguna modificación.** Esta aprobación matemática del texto no certifica por sí sola las animaciones, cuya fidelidad se debe revisar sobre el MP4.

Se verificó también `FUENTE_Y_PROCEDENCIA.md` contra los archivos reales:

| Elemento | Huella comprobada |
|---|---|
| Archivo fuente completo SHA-256 | `111a39c65b30ce3a0c7eff333df0059211fecac12fb19672e2986cb989e5366f` |
| Git blob del archivo de trabajo | `c01adb1f63252a6b481c2772908f03850448f3f5` |
| Extracción `FUENTE_PASAJE.md` SHA-256 | `9625b7768923f8f6ea232e0a54ed6da1c729e6cb62ae34f73636053186b09597` |

La extracción coincide con el pasaje delimitado por el encabezado indicado y el siguiente encabezado de nivel tres, ignorando únicamente espacios exteriores. Ruta, encabezados, extensión y hashes son coherentes. El revisor no modificó el manuscrito ni el guion.

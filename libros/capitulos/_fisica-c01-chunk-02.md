Precisamente uno de los objetivos de un experimento puede ser descubrir que un efecto considerado insignificante no lo era.

### 1.8. Un modelo más complejo no es automáticamente mejor

Añadir parámetros y mecanismos puede permitir describir más detalles, pero también puede:

- dificultar la interpretación;
- introducir cantidades que no sabemos medir;
- ocultar regularidades simples;
- volver inestable una inferencia;
- hacer imposible distinguir qué mecanismo produce qué efecto.

### 1.9. La pregunta puede no necesitar esa complejidad

Si queremos saber aproximadamente cuánto tarda un péndulo en completar una oscilación, modelar el intercambio térmico de la esfera con el aire puede aportar una precisión completamente irrelevante.

### 1.10. Un ejemplo extremo: la esfera perfectamente rígida

Imaginemos que en un modelo llamamos «rígida» a una esfera.

Dentro del modelo, «rígida» puede significar que las distancias entre sus puntos no cambian. Esta hipótesis puede simplificar enormemente el problema.

Pero ninguna esfera material es perfectamente rígida. Todos los cuerpos reales se deforman en alguna medida.

¿Significa esto que el modelo de cuerpo rígido es falso y debe abandonarse?

No.

La pregunta correcta es:

> **¿Son las deformaciones suficientemente pequeñas para que ignorarlas no cambie las conclusiones que nos interesan?**

La física trabaja continuamente con objetos que no existen literalmente:

- partículas puntuales;
- cuerpos perfectamente rígidos;
- hilos sin masa;
- superficies sin rozamiento;
- gases ideales;
- campos uniformes;
- lentes delgadas;
- medios continuos.

Su utilidad no depende de que existan exactamente, sino de que exista un **régimen** en el cual proporcionen una representación adecuada para determinadas preguntas.

Más adelante aprenderemos a expresar cuantitativamente algunos de esos regímenes.
### 1.11. Preguntas diferentes, modelos diferentes

Volvamos al péndulo.

#### Pregunta 1
**¿El cuerpo vuelve aproximadamente al mismo lugar después de ir hacia un lado y hacia el otro?**

Tal vez baste una descripción geométrica muy elemental.

#### Pregunta 2
**¿Cuánto tarda en completar una oscilación?**

Necesitaremos representar el tiempo y ciertas propiedades del sistema.

#### Pregunta 3
**¿Disminuye la amplitud?**

Ya no podemos ignorar indefinidamente los mecanismos de disipación.

#### Pregunta 4
**¿El plano de oscilación cambia lentamente durante muchas horas?**

La rotación terrestre, irrelevante para una pregunta elemental, puede volverse central.

#### Pregunta 5
**¿Cómo cambia el comportamiento si el soporte se mueve?**

La frontera misma del sistema puede requerir una reformulación.

La lección no es que «todo sea relativo» en un sentido impreciso. Es exactamente lo contrario: debemos hacer explícita la dependencia del modelo respecto de la pregunta.

::: {.ma-block .ma-metodo #fpm-i-01-mp02}
**Principio FPM-I-01-MP02 — Adecuación relativa a una pregunta**
Un modelo físico debe evaluarse en relación con las preguntas que pretende responder, las escalas relevantes y la precisión exigida.
:::

### 1.12. Lo que una ecuación no nos dice por sí sola

Supongamos que más adelante encontramos una expresión matemática

$$
F(a,b,c)=0.
$$
La ecuación, considerada únicamente como objeto matemático, no nos informa:

- qué representan $a,b,c$;
- cómo se miden;
- qué unidades poseen;
- si $F=0$ es una definición, una ley empírica o una consecuencia;
- qué hipótesis físicas se utilizaron;
- si la relación es exacta dentro del modelo o aproximada;
- para qué sistemas se propone;
- bajo qué condiciones deja de ser adecuada.

Por eso, durante este libro, una ecuación física nunca será tratada como una fórmula autosuficiente.

Preguntaremos siempre:

1. **¿Qué objetos físicos están representados?**
2. **¿Qué significan los símbolos?**
3. **¿Cuál es el estatus de la relación?**
4. **¿Qué hipótesis la acompañan?**
5. **¿Qué observación permitiría ponerla a prueba?**
6. **¿Cuál es su dominio de validez?**

Más adelante introduciremos una notación editorial para distinguir definiciones, leyes, postulados, hipótesis de modelo, aproximaciones, condiciones y consecuencias matemáticas.
### 1.13. Un entrenamiento especialmente importante para matemáticos

Quien estudia matemáticas aprende, con razón, a exigir definiciones claras, hipótesis explícitas y demostraciones correctas.

En una proposición matemática, una vez fijados los objetos y las hipótesis, la tarea central es determinar qué se deduce lógicamente de ellos.

En física aparece una tarea adicional:

> **decidir qué objetos e hipótesis son apropiados para representar un fenómeno.**

Esta tarea no es una demostración.

No se demuestra, a partir de axiomas puramente matemáticos, que un cuerpo pueda tratarse como punto material, que cierto rozamiento sea despreciable o que un modelo continuo sea adecuado. Estas afirmaciones requieren argumentos físicos: comparación de escalas, observaciones, experimentos, simetrías, experiencias anteriores y análisis de sensibilidad.

La secuencia completa posee entonces dos tipos de razonamiento:

$$
\text{mundo físico}
\longrightarrow
\boxed{\text{elección del modelo}}
\longrightarrow
\text{matemática}
\longrightarrow
\boxed{\text{interpretación y contraste}}.
$$
Los recuadros indican los pasos que no pueden reemplazarse simplemente por manipulación formal.

Este será uno de los hábitos centrales de *Física para matemáticos*.
### 1.14. Ejemplo desarrollado 1 — ¿Qué debemos ignorar?

Consideremos este problema:

> Una pequeña esfera cuelga de un hilo de un metro. Se la aparta ligeramente y se la suelta. Queremos comparar el tiempo de una oscilación hoy y mañana.

Antes de calcular nada, clasifiquemos posibles aspectos del sistema.

| Aspecto | ¿Podría influir físicamente? | ¿Lo incluimos de inmediato? | Motivo |
|---|---|---|---|
| longitud del hilo | sí | sí | define geométricamente el dispositivo |
| masa de la esfera | sí, en general | registrar | todavía no sabemos qué dependerá de ella |
| tamaño de la esfera | sí | quizá | puede afectar resistencia del aire |
| masa del hilo | sí | quizá no | puede ser pequeña frente a la esfera |
| resistencia del aire | sí | quizá no al inicio | el efecto puede ser pequeño en pocas oscilaciones |
| temperatura | sí | registrar si buscamos alta precisión | puede cambiar dimensiones |
| rotación terrestre | sí | probablemente no para esta pregunta elemental | efecto acumulativo pequeño en pocos ciclos |
| color de la esfera | puede correlacionarse con material/temperatura | no por sí mismo | no hay aún mecanismo relevante propuesto |

La columna importante es la segunda: **no debemos confundir «lo ignoro en este modelo» con «no puede tener ningún efecto».**

#### Paso 1 — Formulamos la pregunta
Queremos comparar tiempos de oscilación.

#### Paso 2 — Elegimos variables observables
Necesitamos, como mínimo, un procedimiento para identificar comienzo y final de una oscilación y un procedimiento para medir tiempo.

#### Paso 3 — Elegimos una primera representación
Tratamos provisionalmente el cuerpo como concentrado en una posición y el hilo como de longitud fija.

#### Paso 4 — Registramos omisiones
Aire, deformación del soporte, masa del hilo y otros efectos quedan fuera de la primera descripción.

#### Paso 5 — Dejamos abierta la revisión
Si las observaciones no concuerdan con la precisión buscada, las omisiones se convierten en candidatas a revisión.

Este es el patrón que repetiremos muchas veces:

$$
\boxed{
\text{pregunta}
\to
\text{selección}
\to
\text{modelo}
\to
\text{predicción}
\to
\text{contraste}
\to
\text{revisión}
}
$$
### 1.15. Ejemplo desarrollado 2 — La Tierra no tiene un único modelo

La afirmación «modelaremos la Tierra» está incompleta.

#### Caso A — Una cancha de fútbol

Si queremos describir posiciones sobre una cancha, podemos usar un plano. La curvatura terrestre no tiene relevancia práctica para esa tarea.

#### Caso B — Una ruta aérea transcontinental

Ahora la geometría global importa. Un modelo plano puede distorsionar distancias y trayectorias.

#### Caso C — El movimiento de un satélite lejano

Para ciertos cálculos iniciales, la Tierra puede representarse aproximadamente por una masa concentrada en un punto.

#### Caso D — Distribución de gravedad en la superficie

La forma real, la rotación y la distribución de masa pueden importar.

La secuencia enseña algo general:

$$
\boxed{
\text{mismo objeto físico}
\not\Rightarrow
\text{mismo modelo para toda pregunta}
}
$$
### 1.16. Primer protocolo de lectura

Desde este momento, ante cualquier problema físico, comenzaremos con cinco preguntas.

::: {.ma-block .ma-metodo}
**Protocolo FPM de premodelización — versión inicial**
1. ¿Cuál es la pregunta física concreta?
2. ¿Qué tomaremos como sistema?
3. ¿Qué propiedades necesitamos representar?
4. ¿Qué efectos estamos omitiendo o idealizando?
5. ¿Qué observación permitiría decidir si el modelo sirve para la pregunta?
:::

Todavía faltan elementos —unidades, escalas, parámetros, condiciones y dominio de validez cuantitativo— que añadiremos en capítulos posteriores.
### 1.17. Ejercicios de §1


::: {.ma-block .ma-enunciado #fpm-i-01-e001}
**Ejercicio FPM-I-01-E001 — Un vaso de agua**

Queremos estudiar un vaso con agua.

Propón **tres preguntas físicas distintas** para las cuales convenga utilizar modelos diferentes. Para cada una, indica al menos dos aspectos que incluirías y dos que probablemente omitirías en una primera aproximación.

:::

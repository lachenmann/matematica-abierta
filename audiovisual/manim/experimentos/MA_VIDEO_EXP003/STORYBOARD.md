# Storyboard de realización — EXP003

La propuesta independiente está preservada en STORYBOARD_PROPUESTO.md. Esta realización elige la tabla exacta en frontera. La tira es un esquema de índices, no un eje a escala ni un gráfico de alturas. La voz real fija los intervalos siguientes; el detalle de movimientos se registra al renderizar en generados/eventos_visuales.json.

| Tramo | Inicio(s) | Fin(s) | Representación y movimiento |
|---|---:|---:|---|
| Intro institucional | 0 | 7 | IntroCanal local, misma música y marca |
| pregunta | 7.000 | 18.200 | Pares de puntos coincidentes y pregunta naranja. |
| regla_a | 18.200 | 25.700 | Regla a en azul; aparición al nombrarla. |
| naturales | 25.700 | 34.300 | Índice desde cero y naturales enumerados progresivamente. |
| primeros | 34.300 | 45.333 | Evaluaciones discretas, una fracción por mención; denominadores en aumento. |
| discretos | 45.333 | 54.333 | Ejes y nueve puntos, selección sucesiva sin unir valores. |
| regla_b | 54.333 | 65.833 | Primera rama de b y condición inclusiva hasta 10^6. |
| segunda_rama | 65.833 | 71.567 | Condición posterior y valor uno; completar definición. |
| comunes | 71.567 | 84.300 | Tira de índices con anillos coincidentes y tramo intermedio omitido. |
| cuenta | 84.300 | 93.267 | Corchete inclusivo y 10^6+1 términos. |
| frontera | 93.267 | 103.233 | Tabla exacta en n=10^6 con dos valores iguales. |
| siguiente | 103.233 | 113.200 | Avance de una posición al índice10^6+1 y valor de a. |
| salto | 113.200 | 122.133 | Valor de b=1 y encuadre de la separación. |
| despues | 122.133 | 133.067 | Avance de índices con denominador creciente y b=1 estable. |
| pregunta_muestra | 133.067 | 137.733 | Pregunta sobre lo aprendido. |
| respuesta_muestra | 137.733 | 146.900 | Igualdad observada y necesidad de reglas de continuación. |
| generalizacion | 146.900 | 158.633 | Tramo finito con extremo N definido; extensión de ventana y reglas posteriores. |
| alcance | 158.633 | 171.933 | Énfasis en el extremo y las reglas que gobiernan después. |
| final | 171.933 | 185.100 | Se atenúa el comienzo y se enfatizan todos los términos suficientemente tardíos. |

Los colores mantienen identidad: a azul, b violeta; verde intervalo compartido, naranja pregunta/corte. Las flechas representan selección o continuación de índices, no interpolación de la sucesión. Al cambiar de vista se conserva contexto mediante título y valores exactos. Las fórmulas incompatibles salen antes de entrar las nuevas. Los estados matemáticos persisten durante las pausas de lectura.

Los anclajes por palabra usan ASR local como auxiliar; su resolución y los fallbacks, si existen, están en generados/anclajes_resueltos.json. El informe de QA distingue esa estimación de una escucha humana.

Refinamiento del cierre tras MP4: el prefijo mantiene relleno .01 y trazo tenue; los seis puntos posteriores y la flecha pasan a naranja en el mismo microanclaje que «Todos los términos suficientemente tardíos». La transición fue verificada en un segundo preliminar antes del render de producción.

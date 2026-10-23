# Informe de narración — EXP003

Función especializada de narración ejecutada de manera independiente.

- Motor local: Kokoro-ONNX 0.6.1; voz em_alex, idioma es, velocidad 0,94.
- Dieciocho clips nuevos y dos retomas correctoras de regla_a y regla_b. Sin reutilización de guiones o locuciones anteriores.
- Toma por clip: PCM16 mono a 24 kHz. La producción ensambla y remuestrea a 48 kHz.
- Tiempo real de la síntesis inicial: 141.406 s; duración acumulada definitiva de voz: 148.012583 s. Las dos retomas se registran en el log del pipeline de producción.
- Comprobados los hashes de ambos pesos antes de sintetizar. Verificados canales, frecuencia, cantidad de muestras, picos, saturación y hashes de los dieciocho WAV definitivos. Evidencias: generados/validacion_clips.json y tomas_definitivas.json.
- Saturación de los clips definitivos: 0 muestras; pico máximo de amplitud 0.580750.
- No se afirma escucha humana. La prosodia crítica queda pendiente de valoración editorial, según el encargo.

## Decisión oral y corrección técnica

La auditoría matemática recomendó aclarar las dos menciones del denominador: «uno dividido por la suma de ene y uno». La edición se hizo después de lanzar la preparación de la síntesis. Aunque Kokoro aún no había empezado a escribir clips, el proceso ya había leído el guion. Por eso, la primera tanda conservó las dos frases anteriores. Al ejecutar el pipeline de producción, la caché detectó las dos firmas de texto distintas y regeneró sólo regla_a y regla_b. El resto de dieciséis WAV conserva hash.

La huella de guion de sintesis_inicial.json se tomó al final, por lo que, debido a esta carrera, no certifica el texto leído al inicio. Se conserva como antecedente técnico. tomas_definitivas.json sí verifica cada clip contra la firma de texto canónico vigente, voz, velocidad y hash de WAV. Se corrigió generar_clips.py para capturar simultáneamente los bytes del guion y su SHA antes de sintetizar y para conservar el registro inicial en ejecuciones posteriores. No se alteró ninguna fórmula matemática.

## Duraciones reales definitivas

| Fragmento | Voz (s) |
|---|---:|
| cue-00-pregunta | 10.070625 |
| cue-01-regla_a | 5.488000 |
| cue-02-naturales | 7.479333 |
| cue-03-primeros | 9.030667 |
| cue-04-discretos | 7.886000 |
| cue-05-regla_b | 9.498667 |
| cue-06-segunda_rama | 3.716000 |
| cue-07-comunes | 11.604667 |
| cue-08-cuenta | 6.958667 |
| cue-09-frontera | 7.964000 |
| cue-10-siguiente | 7.949333 |
| cue-11-salto | 6.914000 |
| cue-12-despues | 9.814667 |
| cue-13-pregunta_muestra | 3.538000 |
| cue-14-respuesta_muestra | 8.043333 |
| cue-15-generalizacion | 9.708000 |
| cue-16-alcance | 12.191333 |
| cue-17-final | 10.157292 |

## Reproducibilidad y alineación

`uv run --locked python generar_clips.py` genera los WAV por fragmento y reutiliza una caché sólo cuando coinciden texto, voz, velocidad y hash del WAV. Las versiones y las huellas de pesos están en generados/sintesis_inicial.json; el inventario vigente está en tomas_definitivas.json.

`uv run --locked --with faster-whisper==1.2.1 --with av==16.1.0 python alinear_clips.py` genera tiempos de palabra relativos al comienzo de cada clip definitivo, como apoyo para la sincronización. La primera ejecución se detuvo al detectar el cambio de hash; se reinició contra el inventario definitivo. Whisper es un reconocimiento auxiliar: no sustituye el contraste de las fórmulas y el MP4.

Alineación definitiva completada: 18 clips, 106.687 s de ejecución de Whisper. Cada clip está ligado por SHA al inventario definitivo. El reconocimiento conserva segmentaciones como «en evale» por «ene vale» y «asiguen»/«los debe» por «a siguen»/«los de be»; por eso sus anclajes requieren interpretación del texto canónico. No se borraron estas diferencias del archivo auxiliar.

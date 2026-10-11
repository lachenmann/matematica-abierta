# Segunda lectura de 3D–3E · control matemático y fidelidad editorial

**Fecha:** 2026-09-16. **Estado:** `SEGUNDA LECTURA DE PRUEBAS REALIZADA / CORRECCIONES EDITORIALES PENDIENTES`. No equivale a `VERIFICADO` ni `CERRADO`.

**Fuente de control:** Sheldon Axler, *Linear Algebra Done Right*, 4.ª ed., PDF oficial 16-08-2026, pp. 82–104, https://linear.axler.net/LADR4e.pdf. Se compararon las listas de 24 ejercicios de 3D y 19 de 3E con la fuente y se leyeron nuevamente los 43 bloques de soluciones `[SOL]` para examinar las justificaciones y las hipótesis. Este examen no sustituye una colación tipográfica exhaustiva ni una revisión externa.

## Resultado de la lectura matemática

- **3D, ejercicios 1–24:** no se identificó un contraejemplo que invalide los argumentos revisados; se controlaron especialmente la orientación de los automorfismos en 5–8, la hipótesis finita en 11–14, los coeficientes principales de 20 y la distinción entre inversa de operador y de matriz en 22–24. **No se certifican todavía como verificados**: falta aplicar la corrección explícita de 22 al propio texto y cotejar de extremo a extremo los símbolos y referencias.
- **3E, ejercicios 1–19:** la construcción de isomorfismos 3–5 no requiere dimensión finita; en 11, los conjuntos de índices de valuación 2-ádica fija son disjuntos e infinitos y la prueba de independencia de clases es válida; 13–19 respetan las hipótesis del enunciado y 18 trata el cociente cero. Sigue pendiente la comprobación editorial final y una lectura externa. Los 19 son **redactados, segunda lectura efectuada**, no `VERIFICADO`.

## Incidencias precisas

**QA-3D-22 · corrección textual obligatoria.** La solución publicada termina remitiendo a «la convención de matrices vacías» sin separar suficientemente las dos lecturas. En 3.29 Axler admite matrices de tamaños no negativos, pero en 3.79 define la identidad matricial sólo para tamaño positivo y 3.80 usa esa identidad para definir invertibilidad. Por consiguiente, para `n≥1` la demostración original mediante la aplicación de coordenadas y el producto de matrices es legítima. Para `n=0`, `V={0}` y el operador único es invertible; la matriz `0×0` existe, pero su *invertibilidad* no queda cubierta literalmente por 3.79–3.80. Si se desea conservar también esa equivalencia, hay que **introducir explícitamente como `[NOTA]` nuestra la unidad vacía `I_0` y declarar su invertibilidad**, nunca presentarla como definición del autor. Sustituir la última frase de la solución por esta separación en su archivo de origen; hasta entonces, incidencia abierta. El informe `CHAPTER3D_QA.md` ya anticipa la decisión, pero no reemplaza editar la solución.

**QA-3D-03 · referencia expositiva.** El ejercicio 3 cita «3B.9» y «3B.10» sin identificar que son ejercicios resueltos anteriores; aclarar la procedencia o añadir una justificación autocontenida de preservación de independencia y generación por una aplicación biyectiva.

**QA-3E-01 · integridad del enunciado.** El texto español condensa en corchetes el comentario formal del autor sobre funciones como gráficas. Aunque recoge su idea, **no es una traducción íntegra** de ese pasaje; restituir el razonamiento completo y marcar cualquier resumen editorial como `[NOTA]`.

**QA-3E-3.98 · generalidad del ejemplo.** La redacción «trasladar un plano por el origen» restringe innecesariamente la última observación del original, que se refiere a un plano cualquiera de `R^3` y todos sus planos paralelos. Recuperar la generalidad y la enumeración antes de declarar fidelidad completa.

**QA-3E-3.96 · figura.** Hay equivalente textual, pero falta una figura editorial propia cotejada visualmente; no marcar la ilustración como reproducida.

**QA-TRAD · estatus de la prosa.** En 3D y 3E algunas pruebas y explicaciones se condensaron. Las fórmulas principales y el sentido matemático revisados son compatibles con la fuente, pero la denominación «traducción íntegra» no debe usarse sin colación frase por frase. Mantener `TRADUCCIÓN DE TRABAJO / ADAPTACIÓN EXPLICADA` hasta restituir los pasajes abreviados o etiquetar transparentemente la intervención.

## Contabilidad y puertas de salida

`165` soluciones registradas como verificadas con anterioridad + `24` de 3D + `19` de 3E = **208 redactadas**. Segunda lectura matemática realizada para los últimos 43; **0 de esos 43 se promueven aún a `VERIFICADO`** por las incidencias indicadas. Exigir corrección en archivos de origen, cotejo de todas las referencias y QA tipográfico/figuras antes de cambiar estado. PR #13 no se fusiona por este hito.

**Siguiente:** corregir 3D.22 y la fidelidad editorial de 3E; continuar 3F — Dualidad, empezando por funcionales, bases duales y aplicación dual.
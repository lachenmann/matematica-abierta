---
id: FDC-FOR-v1-CIERRE-M15
fecha: 2026-10-11
estado: primera_etapa_auditada_C14_bloqueada
for11: pendiente
hitos: 10/13
base: 0d6b9a9885db62bec8ac07a7ca269d91597e8f56
codigo: 390684ab0fce64cb710260fdde321c19cefe3547
---

# FDC-FOR-v1-CIERRE-M15 — auditoría inicial de C14

La adecuación global de la presentación congelada está bloqueada: la regla M06 `CalculoOrdenRCA.Proof.exBErename` permite capturar una variable libre del cuerpo existencial. M15 construye el árbol efectivo `rejectedClosedTree : Proof [] .bot`. Compila en Lean; tiene 44 nodos, 1 caso de orden, 4 usos de la base aritmética, ninguna inducción y ninguna comprensión. No depende de axiomas Lean. La compilación acredita la existencia del objeto sintáctico; no acredita la validez de la regla objetada.

No se modifica M05–M14. Sus pruebas particulares siguen conservadas como objetos sintácticos. No se ha auditado cada uso histórico de renombrado y no se concluye que cada resultado particular sea incorrecto. Su transporte canónico no está acreditado.

## Contraejemplo y guarda ausente

Se demuestra legítimamente `∃x<2 (x≠y)` usando tricotomía respecto de cero y testigos 0 o 1. Se instancian x=170, y=171. Las cuatro guardas existentes aceptan: y fresco en Γ vacío, y ausente de la conclusión ⊥, y ausente del término 2 y sustitución `p.safe x (var y)=true`. Sin embargo, y ya aparece libre en p. La matriz sustituida es y≠y, cuya rama se refuta por reflexividad. La regla defectuosa permite concluir ⊥ sin premisas.

`bottom_invalid` y `no_global_order_soundness` refutan la corrección universal del cálculo ordenado en la firma natural. Esta firma sirve sólo como contraejemplo; los resultados positivos se demuestran para firmas arbitrarias, no exclusivamente para el modelo estándar. No se utiliza el árbol contradictorio para producir resultados matemáticos nuevos.

`renamed_exBE_valid` demuestra una variante semántica suficiente con las guardas explícitas x≠y y `p.numFree.contains y=false`, además de las existentes. Es un teorema de adecuación de esa instancia guardada, no una modificación retroactiva del constructor M06.

## Componentes verificables

| Módulo nuevo | Resultado |
|---|---|
| InterpretacionParametricaRCA | Firma con dominios numéricos A y de conjuntos S arbitrarios; evaluación de términos, fórmulas, asignaciones y contextos; coincidencia, frescura y sustitución de términos. |
| SustitucionSemanticaRCA | Coincidencia de fórmulas; frescura numérica y de conjuntos; sustitución completa bajo safe=true; renombrado numérico guardado; renombrado inyectivo de conjuntos y equivalencia alfa guardada. |
| AdecuacionLogicaOrdinariaRCA | Inducción sobre todos los constructores lógicos de M14, incluido cases, bajo las obligaciones finitas de sus hojas embebidas. |
| AuditoriaGuardaRenombradoRCA | Árbol completo del contraejemplo, guardas aceptadas y guarda ausente, perfil y refutación semántica de la corrección global. |
| ContratosAdecuacionRCA | Adecuación de cuantificadores acotados ordinarios; regla renombrada con guarda reforzada; corrección ecuacional condicionada a leyes primitivas; esquemas y contrato de transporte pendientes. |

Las variables numéricas y los índices de conjuntos tienen asignaciones separadas. La semántica de cuantificadores acotados evalúa la cota en la asignación exterior y actualiza la variable sólo en el cuerpo. S puede ser una familia de Henkin, sin identificarla con el conjunto de todas las partes de A. La equivalencia de sustitución considera todos los constructores y las guardas contra captura.

`logic_sound` exige exactamente `∀ c ∈ leaves h, Valid m c.assumptions c.conclusion`. Las hojas son los secuentes embebidos que aparecen en el árbol concreto; no se supone la corrección global de ningún cálculo. Verifica hipótesis, debilitamiento, implicación, conjunción, universales numéricos, existenciales numéricos y de conjuntos y cases. La rama negativa de cases interpreta p→⊥ y utiliza lógica clásica de Lean.

`classicalIdentity` es un árbol lógico completo para p→p, con 5 nodos lógicos, 1 cases y cero hojas de teoría. Su validez se deriva sin obligaciones pendientes. En cambio, la gráfica C13 de M14 tiene 4 hojas lógicas de teoría; el puente a C12 tiene 3. Esas hojas siguen pendientes de adecuación, aunque los objetos sintácticos originales compilan.

## Contratos pendientes y separación de niveles

| Contrato | Alcance demostrado | Obligación restante |
|---|---|---|
| EquationalContract | equation_sound por inducción sobre EqProof, dadas diez leyes primitivas | Derivar esas diez leyes de una presentación independiente de RCA₀. |
| OrderedContract | Se registran 18 leyes exactas de orden y aritmética usadas por M05–M06 | Derivarlas en RCA₀ canónico y verificar cada constructor; reparar/separar exBErename antes de cualquier teorema global. |
| InductionContract | induction_valid convierte el esquema semántico explícito en la instancia guardada | Correspondencia de Sigma1 con Σ⁰₁ canónico y derivación del esquema IΣ⁰₁, con parámetros. |
| ComprehensionContract | comprehension_valid verifica la instancia con Sigma1/Pi1, equivalencia y frescura del índice | Correspondencia sintáctica Δ⁰₁ y acreditación del esquema canónico; no se introduce un axioma de existencia especial. |
| SetDomainContract | Se explicitan no vacuidad y extensionalidad | Acreditación del dominio y de todas las reglas históricas de conjuntos, incluidos puentes/renombrados. |
| PreservationContract | Tipo explícito y separado de Valid | Instanciar una axiomatización independiente, traducción y transformación efectiva de derivaciones con guardas y esquemas. No existe aún prueba del contrato. |

Estos contratos son definiciones/estructuras no habitadas aquí como modelos canónicos. No son axiomas Lean ni hipótesis de corrección global. La validez semántica condicionada no se presenta como preservación de derivaciones. `IndependentPresentation` todavía es una interfaz abstracta, no una axiomatización independiente ya construida. No se acredita que los constructores aritméticos, las clasificaciones de fórmulas o las reglas de conjuntos coincidan globalmente con RCA₀ clásico.

H04-01 y H04-02 conservan sus antecedentes. H04-03/C13 permanece como derivación sintáctica M14 y dependencia explícita del puente M13; su interpretación canónica sigue condicionada a C14. No se anuncia existencia uniforme de todas las trazas.

## Controles y reproducción

Commit de código: `390684ab0fce64cb710260fdde321c19cefe3547`. PR [313](https://github.com/lachenmann/matematica-abierta/pull/313), en borrador, abierta y sin fusionar. Las PR 299–313 se leyeron nuevamente y permanecen abiertas en borrador.

CI [Lean, run 38116246314](https://github.com/lachenmann/matematica-abierta/actions/runs/38116246314): job verify 114401595982 completado con éxito; biblioteca completa, 9016 trabajos, dependencias fijadas y rechazo de marcadores incompletos. Lean 4.34.0; Mathlib 5ed2965256430c3649e86755f9576b54eca72435. Los cinco módulos nuevos también se compilaron localmente con Lean 4.34.1 y Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612, sin errores ni advertencias. La finalización del segundo recorrido local completo no pudo confirmarse por desconexiones del exec-server; no se declara completado.

Se conservan 31 consultas #print axioms: 7 vacías; 2 con propext; 20 con propext y Quot.sound; 2 con propext, Classical.choice y Quot.sound. El inventario declaración por declaración y los seis perfiles/salidas están en CONTROLES_M15.json y CI_M15_EXTRACTO.txt. Se compilaron 14 ejemplos de guardas. Ninguna regla ni axioma nuevo concede conjuntos, códigos o corrección global.

La comparación exacta contra el commit M14 modifica solamente el agregador y añade cinco módulos. No modifica ninguna fuente previa, ensayos, edición integral ni Markdown canónico. Inventario total: 89 módulos, 30 integrados y 59 en borrador. El manifiesto de blobs históricos se conserva en los controles.

Los cuatro Markdown canónicos de Drive fueron releídos y comparados íntegramente con el estado inicial: coincidencia exacta en todos. Se preservan sin editar. Este informe complementa esa historia y registra el bloqueo nuevo; no afirma que el hallazgo ya esté incorporado a sus frontmatter. La persistencia y readback de esta entrega se realizan directamente en Git; no se crea Google Docs ni se modifica la web.

Reproducción independiente: ejecutar REPRODUCIR_M15.sh en un clon del repositorio. Obtiene el commit de código exacto, comprueba la comparación permitida, conserva el inventario histórico y ejecuta el build con --wfail. El script se entrega para reproducción; no se afirma que haya sido ejecutado en este entorno desconectado.

C14 y FOR-11 permanecen pendientes, con bloqueo explícito de adecuación global. Contador fijo 10/13. No se inicia H04-04.h ni FOR-12, no se fusiona ninguna PR y no se publica la web.

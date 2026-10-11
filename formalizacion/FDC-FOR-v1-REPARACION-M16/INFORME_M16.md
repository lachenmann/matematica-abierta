---
id: FDC-FOR-v1-REPARACION-M16
fecha: 2026-10-11
estado: reparacion_CI_aprobada_reproduccion_local_pendiente
for11: pendiente
c14: bloqueada
hitos_historicos: 10/13
base: 390684ab0fce64cb710260fdde321c19cefe3547
expediente: f77746823a48d3c03ac1ba5e04e0ac18472d77e0
codigo: 3e542ee39a9a3103c33d4a1d5a2a74e9359a4a7c
---

# Reparación M16 de exBErename

La rama correctiva exige x≠y y que y no aparezca libre en el cuerpo p, además de las cuatro guardas anteriores. Los dos usos x=y se reconstruyen con eliminación ordinaria exBE. No existe una excepción que autorice captura. C14 y FOR-11 permanecen pendientes; el contador 10/13 se conserva exclusivamente como registro histórico.

PR [314](https://github.com/lachenmann/matematica-abierta/pull/314), independiente, en borrador y sin fusionar. Las PR 299–313 permanecen intactas en borrador. Los commits M05–M15 y sus blobs originales permanecen en el historial de la rama.

## Contrato reparado

```lean
| exBErename {Γ : List Formula} {p q : Formula} (x y : ℕ) (bound : Term) :
    freshNum y Γ = true →
    q.numFree.contains y = false →
    bound.vars.contains y = false →
    p.safe x (.var y) = true →
    x ≠ y →
    p.numFree.contains y = false →
    Proof Γ (.exB x bound p) →
    Proof (p.subst x (.var y) :: .lt (.var y) bound :: Γ) q →
    Proof Γ q
```

El caso semántico se deriva de M15 renamed_exBE_valid, que utiliza alpha_body. Los certificados de las guardas permanecen como argumentos explícitos comprobados por Lean. No se introduce ninguna regla ni axioma que conceda corrección global.

## Auditoría histórica

El inventario de la fuente del commit base contiene exactamente 41 invocaciones concretas en 18 módulos. Se separan de ese inventario la rama genérica del transporte estructural y la invocación forense contradictoria.

| Grupo | Resultado de la migración |
|---|---|
| 39 usos con x≠y | Se añaden certificados de desigualdad y frescura del cuerpo; la construcción previa de las premisas y ramas se conserva. |
| InversosFuturosRCA.futurePoint, 64→64 | Se elimina el renombrado de identidad y se utiliza exBE con sus tres guardas originales. |
| InversosFuturosRCA.futurePoint, 65→65 | Igual reconstrucción con exBE. |
| RenombradoConjuntosRCA.ordered, rama genérica | Se transportan la desigualdad y la guarda nueva mediante numFree; no se presupone una sustitución de conjuntos adicional. |
| Árbol contradictorio M15 | Se conserva exactamente fuera de la biblioteca confiable; su instancia con la nueva firma se rechaza. |

No se ha encontrado una llamada histórica con nombres distintos que requiera cambiar el testigo o la derivación matemática por fallo de la nueva guarda. Los dos casos de identidad sí cambian de constructor. La incorporación de audit_rename sólo realiza el mismo apply y registra parámetros en elaboración; no añade una regla de prueba.

static-invocations.json fija archivo, línea histórica, x/y y texto original. AUDITORIA_M16.json contiene los 41 registros de elaboración completos: p, Γ, conclusión y cota desarrollados, sin puntos suspensivos ni truncamiento. Los dos casos de identidad se identifican separadamente. Las nuevas guardas están acreditadas por certificados, no por el inventario estático.

## Corrección semántica relativa y consistencia

CorreccionCalculoOrdenRCA.raw_sound se demuestra por inducción sobre todos los constructores Derives. ordered_sound se demuestra por inducción sobre todos los constructores CalculoOrdenRCA.Proof reparado, descargando también embed mediante raw_sound. Las premisas son EquationalContract, OrderedContract, InductionContract y ComprehensionContract. No se supone la validez de hojas arbitrarias ni de todo el cálculo.

Estos teoremas utilizan interpretación paramétrica M15 con dominios A y S arbitrarios. Por tanto, la adecuación no depende exclusivamente de la verdad en ℕ. no_closed_bottom_relative excluye un árbol cerrado de falsedad en toda interpretación provista de esos contratos y asignaciones.

ModeloTestigoCalculoReparadoRCA construye una interpretación concreta en ℕ y Set ℕ: las leyes primitivas se verifican con teoremas ordinarios de Lean; la inducción se demuestra por inducción natural y la comprensión por un conjunto definido mediante un predicado. Este modelo sirve como testigo de consistencia relativo a Lean, adicional a la prueba paramétrica. No se supone un axioma de seguridad. no_closed_bottom concluye ¬ Nonempty (CalculoOrdenRCA.Proof [] Formula.bot).

No se acredita equivalencia con RCA₀ canónico. Siguen pendientes la derivación de las leyes primitivas en una axiomatización independiente, las correspondencias Σ⁰₁/Π⁰₁/Δ⁰₁, el transporte de los esquemas y la adecuación completa de los envoltorios existenciales/de conjuntos y de toda la cadena FOR-11. H04-01/H04-02 conservan sus antecedentes. H04-03/C13 y C12 no reciben acreditación canónica por esta reparación.

## Evidencia forense y controles negativos

La fuente original AuditoriaGuardaRenombradoRCA.lean se conserva byte por byte en forensics/M15. Se retira del agregado y de sus dependencias confiables. ContratosAdecuacionRCA importa la capa lógica ordinaria y expresa directamente sus dos ejemplos sintácticos, sin importar el árbol contradictorio.

RechazoContraejemploM15RCA conserva las premisas legítimas y verifica rechazos con fail_if_success. Las pruebas negativas externas OldSignature.lean y CapturedBody.lean deben fallar al compilar. verify_m16.py exige fallo, comprueba el diagnóstico correspondiente y descarta una recuperación no controlada. El contraejemplo se usa exclusivamente como regresión negativa; no se usa para derivar teoremas.

## Reproducción y preservación

La compilación local inicial revalidó todos los módulos con invocaciones históricas, incluido RenombradoConjuntosRCA y los módulos de extensión M12–M14. La corrección paramétrica compiló con propext y Quot.sound. El primer recorrido completo se detuvo por falta de Mathlib.olean; se recuperó la caché completa y comenzó otro recorrido con auditoría. Luego se desconectó exec-server. Su finalización no pudo confirmarse y NO se registra como reproducción local completa satisfactoria. Lean local 4.34.1; Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612.

La CI utiliza Lean 4.34.0 y Mathlib 5ed2965256430c3649e86755f9576b54eca72435, build --wfail y controles negativos/históricos posteriores. CI Lean [38144033238](https://github.com/lachenmann/matematica-abierta/actions/runs/38144033238), job 114483543918: éxito. La biblioteca completa terminó con 9019 trabajos; también pasaron OldSignature, CapturedBody y M16_HISTORY_AND_NEGATIVE_PASS. MA-Lean 38144033171 pasó. Quarto es un control adicional de previsualización; no publica la web. REPRODUCIR_M16.sh permite repetir el recorrido completo en un clon externo con esos mismos pines.

Recuento directo de fuentes: el commit base contiene 91 módulos Lean más el agregador; la versión correctiva tiene 94 más el agregador, por cuatro módulos nuevos y un módulo forense retirado. El informe M15 anotó 89; esta diferencia queda reconciliada mediante el manifiesto completo y no modifica el contador histórico 10/13 ni acredita solidez matemática.

La comparación Git limita los cambios a la reparación, su auditoría, la retirada forense, sus metateoremas y controles/CI. Los siete ensayos, edición integral, web y restantes fuentes no se modifican.

## Controles axiomáticos y perfiles

CI produjo 259 consultas axiomáticas: 172 vacías; 9 con propext; 41 con propext y Quot.sound; 37 con propext, Classical.choice y Quot.sound. Ninguna contiene sorryAx ni axiomas de seguridad personalizados. Se preservan exactamente las dependencias de las 249 declaraciones históricas consultadas que permanecen en la biblioteca; las cinco consultas forenses originales se conservan en el expediente M15 fuera del agregado. Los diez controles nuevos incluyen cuatro vacíos, dos con propext y cuatro con propext/Quot.sound.

Se preservan exactamente los 92 perfiles/salidas históricas retenidos. El perfil contradictorio se retira y se añade el de la premisa legítima M15: 40 nodos, 1 caso de orden, 4 usos aritméticos, ninguna inducción ni comprensión. Las 41 guardas se verifican durante elaboración y las regresiones negativas pasan en CI. No se introducen nuevas dependencias axiomáticas en los árboles históricos.

CONTROLES_M16.json conserva el inventario declaración por declaración, perfiles, comparación de commits, readbacks, respaldos y estado de las PR. CI_LEAN_M16.log conserva la salida completa. El build Lean no emitió errores ni advertencias de fuente; el runner notificó aparte la deprecación de Node.js 20 de actions/checkout@v4, que no afecta el resultado Lean.

## Registro canónico inmediato

Antes de corregir código se leyeron los cuatro Markdown canónicos. Se guardaron cuatro respaldos previos en Drive y se comprobaron íntegramente. Se añadió a cada archivo el incidente, el bloqueo de C14, la distinción entre compilación sintáctica y adecuación pendiente y las restricciones de alcance. Las cuatro escrituras directas Markdown y su readback exacto se completaron; una segunda lectura confirmó la coincidencia. No se utilizó Google Docs.

El registro inicial dice expresamente que M16 está en auditoría. El informe final separado contiene los resultados posteriores; no se declara que una reproducción local pendiente haya quedado acreditada en los documentos canónicos.

M16 no inicia H04-04.h, FOR-12 ni etapas nuevas de la reversión. No se fusiona ninguna PR ni se publica la web. C14 bloqueada y FOR-11 pendiente, 10/13 histórico.

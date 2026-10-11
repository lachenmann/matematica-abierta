---
document-id: TLOG-LEAN-HANDOFF-0001
version: 1.0.0
date: 2026-10-11
status: prepared-for-later-verification
---
# TLOG — Preparación para MA-Lean

El paquete conserva los 667 nodos humanos, las 2573 dependencias directas y los 297 candidatos. No se emiten módulos con marcadores de prueba ni teoremas ficticios. Todas las firmas y correspondencias Lean están pendientes; compiled=0, verified=0.

## Integración y reproducción

Perfil: MA-Lean/profiles/tlog.json. Inventario y textos: MA-Lean/mapeos/TLOG/inventory.json y units.json. Biblioteca única: lean/MatematicaAbierta; módulos futuros MatematicaAbierta.TLOG.CHxx. No se crea otro Lake ni se altera MCL.

El entorno público observado es Lean v4.34.0 y Mathlib v4.34.0, fijado por commit y hashes de toolchain y lake-manifest. La reconciliación futura del motor puede adoptar otra versión mediante decisión versionada; no se actualizan dependencias silenciosamente.

Ejecutar python3 MA-Lean/adapters/tlog_preflight.py --repo-root .; con --source-root se cotejan también los capítulos canónicos completos. Su PASS acredita preparación, no aceptación del kernel. Los fragmentos se acompañan de hashes y offsets de caracteres Unicode, no offsets de bytes.

## Contrato por nodo

Cada entrada conserva ID, título, tipo, capa, sistema objeto, localizador, selección y dependencias. units.json incluye su texto humano completo y hash; source registra el hash del documento y del bloque. Se propone nombre y módulo; lean_file y lean_declaration permanecen null.

Antes de mapear se debe revisar la firma Lean frente a hipótesis, cuantificadores, parámetros, igualdad y conclusión humanos. Una convención o axioma objeto no se transforma en teorema metateórico. Los 370 no seleccionados conservan su estado; no se amplía la selección por generar el inventario.

## Orden de formalización

1. Árboles proposicionales con cinco conectivos; inducción y recursión. Primeros objetivos TLOG-DEF-00007 y TLOG-MTH-00001.
2. Valuaciones y cálculo Hilbert proposicional, separando verdad y derivación.
3. Signaturas, términos, fórmulas, variables libres, sustituciones y equivalencia alfa; captura y frescura explícitas.
4. Modelos, satisfacción, corrección y completitud; distinguir casos enumerables de los que requieren BPI.
5. ZF_obj como sintaxis y derivaciones; no importar sus axiomas como verdades Lean sin contrato.
6. RM, S/G, configuraciones, trazas y certificados. MP: antecedente primero, implicación después.
7. PA_obj, representación, diagonalización e incompletitud; las materializaciones AG-04 quedan bloqueadas.

El orden topológico completo aparece en inventory.json. Cada dependencia requiere cobertura adecuada o un puente revisado; prioridad pedagógica no permite saltarse el DAG.

## Fundamentos y aceptación futura

M_ext es ZF clásica sin AC/BPI. ZF_obj, PA_obj y RM se mantienen separados. Verdad de Lean, satisfacción de una estructura y existencia de derivación objeto son relaciones distintas. No se presupone consistencia ni existencia de modelos de ZF_obj.

Classical.choice como axioma del kernel en una prueba externa no equivale automáticamente a AC objeto, pero debe justificarse que no fortalece la afirmación atribuida a ZF sin elección. Se auditan por separado axiomas del kernel, axiomas objeto y puentes de interpretación.

La evidencia futura exige módulo real importado por la biblioteca, commit, fuente y manifest fijos, lake build --wfail, #check y #print axioms, ausencia de sorryAx y de axiomas personalizados no revisados, revisión de firma y correspondencia, hipótesis y alcance. Compilación y revisión semántica son puertas separadas. Un build no verifica automáticamente un capítulo entero.

## Obligaciones y publicación

AG-03 sigue OPEN para revisión independiente exhaustiva. AG-04 sigue IN-PROGRESS: programa RM admisible con rama inicial PA y trazas, descripción PR completa de χ_T, generadores aritméticos y Prov* literal seleccionado. R01 y R02 aportan 236 y 815 regresiones Python, respectivamente, no pruebas Lean. AG-05 sigue OPEN para revisión editorial integral; el QA de la edición web no sustituye esa revisión.

La web conserva las 667 unidades y pruebas; adapta sólo presentación, anclas, enlaces y navegación, y omite secciones operacionales sin resultados. La edición pública es de estudio, con pruebas humanas y verificación formal pendiente. Los ID públicos MA-BOK-0014 y MA-BCH-0202–0225 se reservan aquí y en el registro web, sin alterar los ID deductivos.

**Progreso local:** ▰▰▰▰▰▰ 6/6 entregables; cierre sujeto al certificado final.

**Progreso global:** ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 24/24 capítulos cerrados (100%).

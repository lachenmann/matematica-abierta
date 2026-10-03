---
title: "MA-APP-0004 — Roadmap de desarrollo v0.2"
id: MA-APP-0004-ROADMAP-v0.2
project: MA-Práctica
content-type: roadmap
status: canonical
version: 0.2
date: 2026-09-23
parent-specification: "MA-APP-0004 - MA-Práctica.md"
implementation-status: planned-incremental
---

# MA-APP-0004 — Roadmap de desarrollo v0.2

## 1. Decisión canónica

La siguiente fase de MA-Práctica se concentra en tres objetivos prioritarios y mutuamente dependientes:

1. **persistencia del Elo y del progreso**, tanto en uso anónimo como mediante cuenta opcional;
2. **expansión sistemática de temas, subtemas y niveles matemáticos**;
3. **selección aleatoria y adaptativa de ejercicios**, evitando repeticiones innecesarias de problemas ya resueltos.

Este roadmap complementa la especificación canónica `[MA-APP-0004 - MA-Práctica](./MA-APP-0004%20-%20MA-Pr%C3%A1ctica.md)`. No sustituye las decisiones cerradas del MVP v0.1 ni autoriza por sí mismo la publicación de funcionalidades no implementadas.

## 2. Principios de producto

MA-Práctica mantiene una filosofía **local-first y de registro opcional**:

- una persona puede entrar y practicar sin crear cuenta;
- el progreso local debe seguir funcionando aunque no exista sesión remota;
- la creación de cuenta aparece como una opción para conservar y sincronizar el progreso, no como barrera de entrada;
- no habrá rankings públicos, perfiles sociales ni competencia entre usuarios en esta fase;
- el Elo se usa como estimación personal y experimental para trayectoria y selección de ejercicios, no como medición oficial de capacidad;
- las áreas matemáticas conservan ratings separados mientras no exista validación para agregarlas.

La referencia conceptual de producto es el principio de acceso inmediato y cuenta opcional usado por Lichess, pero **no se adopta su modelo competitivo ni Glicko-2 como sistema de rating**. MA-Práctica modela principalmente la interacción usuario–ejercicio, no jugador–jugador.

## 3. Roadmap canónico

### Fase 1 — MA-Accounts v0.1

Objetivo: hacer persistente el progreso sin romper el modo local existente.

Estados de identidad previstos:

- **Local:** progreso solo en `localStorage`; sin identidad remota.
- **Anónimo sincronizado:** identidad remota sin perfil público; puede persistir mientras la sesión anónima sea recuperable en ese dispositivo.
- **Cuenta recuperable:** la identidad anónima puede vincularse posteriormente a correo mediante enlace mágico/OTP, conservando el mismo progreso.

Backend previsto para esta fase: **Supabase**.

Requisitos:

- autenticación anónima opcional;
- conversión posterior a cuenta recuperable sin perder el identificador interno ni el progreso;
- Row Level Security para que cada usuario solo pueda leer y modificar sus propios datos;
- eliminación explícita de cuenta y datos asociados;
- ninguna `service_role` expuesta al navegador;
- importación controlada del progreso local cuando una identidad remota se crea o se vincula por primera vez;
- cierre de sesión sin destrucción automática del progreso remoto;
- aviso claro de que una identidad anónima no vinculada puede no ser recuperable tras borrar datos locales, cerrar sesión de forma destructiva o cambiar de dispositivo.

Para usuarios sincronizados, el **servidor es la autoridad del Elo**. El navegador puede cachear datos, pero no decidir de forma unilateral si un ejercicio debe puntuar nuevamente.

### Fase 2 — MA-Taxonomy v0.1

Objetivo: estabilizar una taxonomía antes de multiplicar el banco.

Cada ejercicio deberá poder describirse al menos con:

```text
area
topic
subtopic
level
skills[]
familyId
instanceId
provisionalRating
```

Se separan dos conceptos:

- **nivel pedagógico**: ubicación curricular o conceptual;
- **rating de dificultad**: estimación experimental susceptible de recalibración.

Orden inicial recomendado de expansión vertical:

1. Aritmética
2. Álgebra
3. Funciones
4. Cálculo

Áreas posteriores: Geometría, Trigonometría, Álgebra lineal, Probabilidad, Matemática discreta y Demostraciones.

La taxonomía debe conservar compatibilidad con los ejercicios `MAP-DEMO-###` ya existentes y permitir migración progresiva, sin renombrados destructivos innecesarios.

### Fase 3 — MA-Selector v0.1

Objetivo: reemplazar la secuencia lineal actual por una selección sin repeticiones innecesarias y preparada para adaptación futura.

Regla base:

```text
no resueltos
> nuevos de dificultad adecuada
> repasos necesarios
> repeticiones generales
```

No se usará `Math.random()` de forma aislada. El selector deberá trabajar sobre candidatos elegibles y mantener estado suficiente para impedir que el usuario reciba el mismo ejercicio de manera inmediata o repetitiva cuando aún existen alternativas no vistas.

Estado mínimo previsto:

```text
seenInstanceIds
completedInstanceIds
ratedFamilyIds / ratedInstanceIds
wrongSkills
lastSeenAt
topicProgress
```

Criterio canónico: un usuario no debería volver a recibir una instancia ya resuelta hasta agotar razonablemente el conjunto pertinente, salvo que el sistema la seleccione deliberadamente como repaso.

### Fase 4 — MA-Generators v0.1

Objetivo: introducir familias parametrizadas de ejercicios reproducibles.

Se distingue:

```text
familyId: ALG-LINEAR-EQ-01
instanceId: ALG-LINEAR-EQ-01@<semilla>
```

Una familia puede producir múltiples instancias equivalentes en estructura pero diferentes en datos. Ejemplo conceptual:

```text
3x + 5 = 20
7x - 4 = 31
5x + 9 = 34
```

Las instancias deben ser reproducibles desde una semilla o especificación determinista para permitir auditoría, historial y corrección.

**Regla de protección del Elo:** no permitir que una gran cantidad de variaciones triviales de una sola familia infle artificialmente el rating. La política exacta `ratedFamilyIds` versus `ratedInstanceIds` deberá fijarse y probarse antes de que los generadores afecten al Elo.

### Fase 5 — Expansión del banco

Objetivo: poblar progresivamente la taxonomía con ejercicios originales, auditables y graduados.

Prioridades:

- densidad suficiente de ejercicios por tema antes de abrir demasiadas áreas;
- equilibrio de dificultad dentro de cada tema;
- mantenimiento de la trazabilidad editorial y matemática;
- separación explícita entre contenido original, referencias externas y calibración;
- distractores matemáticamente plausibles pero no interpretados como diagnósticos psicológicos sin evidencia empírica;
- QA matemático, editorial, técnico y de accesibilidad antes de publicación.

### Fase 6 — Adaptación y calibración empírica

Esta fase solo comienza cuando exista un volumen suficiente de ejercicios y eventos reales.

Objetivos posibles:

- recalibrar dificultades provisionales;
- estimar estabilidad o incertidumbre del rating;
- seleccionar problemas según habilidad y error reciente;
- estudiar modelos tipo Rasch/IRT si la evidencia lo justifica;
- introducir repaso espaciado por habilidad o familia;
- revisar si `first-attempt-v03` debe evolucionar.

No adoptar Glicko-2 solo por analogía con Lichess. El problema estadístico de MA-Práctica es principalmente usuario–ítem y debe evaluarse con ese criterio.

## 4. Esquema mínimo de datos remoto

Para MA-Accounts v0.1 se prevé, al menos conceptualmente:

### `user_ratings`

- `user_id`
- `area`
- `rating`
- `updated_at`

### `rated_exercises`

- `user_id`
- `exercise_family_id`
- `exercise_instance_id`
- `area`
- `topic`
- `difficulty`
- `first_attempt_result`
- `rating_before`
- `rating_after`
- `delta`
- `rating_policy`
- `created_at`

Debe existir una restricción de unicidad que impida contabilizar dos veces el mismo evento puntuable según la política vigente.

### `practice_sessions`

- `user_id`
- identificadores del ejercicio y familia
- modo de práctica
- resultados y traza necesaria para el historial
- fecha
- estado completo/parcial

El correo de autenticación no debe duplicarse innecesariamente en las tablas de progreso.

## 5. Flujo de sincronización

### Usuario sin cuenta

```text
MA-Práctica
→ localStorage
→ práctica completa
```

### Usuario anónimo sincronizado

```text
MA-Práctica
→ sesión anónima Supabase
→ RLS
→ progreso remoto + caché local
```

### Conversión a cuenta recuperable

```text
sesión anónima existente
→ vincular correo mediante Magic Link/OTP
→ mismo user_id
→ mismo Elo e historial
```

### Primer vínculo con progreso local existente

La aplicación debe ofrecer una acción explícita de importación. No mezclar silenciosamente dos estados Elo incompatibles. Si existe progreso remoto previo, se requiere una estrategia de conciliación definida y auditada antes de modificar ratings.

## 6. Selector y Elo

La selección de ejercicios y el rating son subsistemas relacionados pero distintos.

El selector puede usar:

- área elegida;
- tema/subtema;
- nivel pedagógico;
- rating actual;
- ejercicios vistos y resueltos;
- errores recientes;
- tiempo desde la última aparición.

El Elo solo se modifica por eventos que satisfagan la política de puntuación. **Ver un ejercicio no equivale a puntuarlo.** Repetirlo como entrenamiento o repaso tampoco debe producir movimientos nuevos salvo decisión canónica posterior.

La primera versión mantiene la política `first-attempt-v03` mientras se amplía la infraestructura. No cambiar simultáneamente persistencia, selección y fórmula Elo sin pruebas separadas.

## 7. Restricciones y no-objetivos inmediatos

No forman parte de este roadmap inmediato:

- rankings públicos;
- perfiles sociales;
- mensajería entre usuarios;
- ligas o competición;
- anticheat complejo;
- gamificación basada en comparación pública;
- una única puntuación global que mezcle todas las áreas;
- inferencias psicológicas automáticas a partir de distractores;
- rating oficial o certificación de competencia.

## 8. Orden de implementación

Orden canónico:

1. **MA-Accounts v0.1** — identidad anónima, cuenta opcional, RLS, sincronización y autoridad remota del Elo.
2. **MA-Taxonomy v0.1** — área → tema → subtema → habilidad → nivel; compatibilidad con banco actual.
3. **MA-Selector v0.1** — selección sin repetición y preparada para adaptación.
4. **MA-Generators v0.1** — familias parametrizadas, semillas e instancias reproducibles.
5. **Expansión del banco** — poblar temas y niveles de manera progresiva.
6. **Calibración/adaptación** — solo con datos suficientes y revisión metodológica.

## 9. Criterio de cierre de v0.2

MA-Práctica v0.2 puede considerarse estructuralmente cerrada cuando:

- un usuario puede practicar sin registrarse;
- puede activar persistencia anónima sin perder su progreso;
- puede convertir esa identidad en cuenta recuperable;
- el mismo Elo puede recuperarse en otro dispositivo tras autenticarse;
- el servidor impide doble puntuación del mismo evento;
- existe taxonomía estable para nuevos ejercicios;
- el selector evita repeticiones inmediatas mientras haya alternativas elegibles;
- al menos una familia parametrizada genera instancias reproducibles;
- el banco crece en varias dificultades dentro de un recorrido temático coherente;
- las pruebas cubren sincronización, duplicación, selección, migraciones y fallos de red;
- se mantiene disponible el modo local si el backend falla.

## 10. Estado actual y próxima acción

**Estado:** roadmap v0.2 aprobado y canónico el 23-09-2026. Las funcionalidades descritas son objetivos de implementación; no deben anunciarse como disponibles hasta completar su desarrollo y QA.

**Próxima acción canónica:** continuar **MA-Accounts v0.1** desde el árbol local `D:\\MA-Practica`, conectando el backend Supabase cuando esté disponible y manteniendo esquema, migraciones, adaptadores y QA dentro del repositorio.


## 11. Ubicación canónica

Este roadmap se trabaja y versiona en `D:\\MA-Practica\practica\design` / GitHub. Obsidian/Drive deja de ser el lugar de edición de MA-Práctica; cualquier copia previa allí debe considerarse histórica una vez verificada la migración local.

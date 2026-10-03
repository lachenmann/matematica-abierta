# QA visual — MA-CLS-C13-P01

**Fecha:** 2026-10-01  
**Render evaluado:** GitHub Actions run 36934530951  
**Clase:** `MAClsC13P01`  
**Resolución de QA:** 854×480, 15 fps  
**Duración medida:** 49,798698 s

## Resultado

**PASS visual / TIMING PENDIENTE DE VOZ**

## Duraciones medidas de los componentes

| Componente | Duración |
|---|---:|
| MA-VIZ-C13-002 | 13,666 s |
| MA-VIZ-C13-003 | 11,466 s |
| MA-VIZ-C13-004 | 12,400 s |
| MA-CLS-C13-P01 completo | 49,799 s |

Los elementos de montaje —apertura, dos puentes, transiciones y cierre— ocupan conjuntamente aproximadamente 12,27 s en el preview silencioso.

## Inspección visual

### Apertura

PASS. Título, subtítulo e identificación del proyecto permanecen dentro de zona segura y establecen la jerarquía sin fórmula prematura.

### Bloque 1 → puente 1

PASS. La visualización se limpia por completo antes de que aparezca el puente. No quedan ejes, paneles ni fórmulas residuales.

### Puente 1 → bloque 2

PASS. El puente aparece aislado sobre el fondo canónico y desaparece antes de comenzar la siguiente visualización.

### Bloque 2 → puente 2

PASS. No se arrastran la suma de Riemann ni las marcas de la franja destacada.

### Puente 2 → bloque 3

PASS. La transición conserva continuidad cromática sin anticipar la nueva gráfica.

### Bloque 3

PASS. La oposición entre contribuciones con signo y área geométrica mantiene la gramática cromática aprobada y permanece contenida en las zonas seguras.

### Cierre

PASS. El mapa

[
\text{encerrar}\to\text{sumar}\to\text{distinguir signo y área}
]

es legible, progresivo y no introduce teoría nueva.

## Hallazgo temporal

El preview silencioso dura 49,80 s, muy por debajo del objetivo editorial de unos 185 s. Esto **no se considera un defecto del QA visual**: las pausas y velocidades definitivas deben ajustarse con una locución de referencia.

No se recomienda estirar de forma mecánica las escenas antes de disponer de la voz.

## Decisión

El ensamblaje visual puede pasar a la etapa de **temporización con narración de referencia**.

No se requieren cambios en el código visual antes de esa etapa.

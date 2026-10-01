# QA de temporización — MA-CLS-C13-P01

**Fecha:** 2026-10-01  
**Workflow:** 36939896397  
**Clase:** `MAClsC13P01Timed`  
**Objetivo:** 185,0 s  
**Tolerancia:** ±2,0 s  
**Duración medida:** **185,599 s**  
**Desviación:** **+0,599 s**

## Resultado

**PASS**

La expansión temporal no ralentiza uniformemente las animaciones. Los movimientos conservan la velocidad del prototipo aprobado y el tiempo adicional se concentra en permanencias semánticas:

- encierro;
- brecha entre sumas;
- refinamientos;
- franja etiquetada;
- producto;
- suma completa;
- cancelación;
- lectura mediante valor absoluto;
- contraste final.

## Compatibilidad

En el mismo workflow pasaron:

1. `MAVizC13RiemannRefinement`;
2. `MAVizC13RiemannTermToSum`;
3. `MAVizC13SignedIntegralVsArea`;
4. `MAClsC13P01`;
5. `MAClsC13P01Timed`;
6. verificación automática de duración.

## Decisión

El prototipo queda listo para la siguiente etapa: **voz de referencia y sincronización fina audio–imagen**.

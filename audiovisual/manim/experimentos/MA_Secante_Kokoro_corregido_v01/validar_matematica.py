"""Comprobaciones algebraicas y geométricas de las dos aproximaciones."""
import json
from pathlib import Path
import numpy as np


def main():
    hs = np.r_[-np.geomspace(.003, .75, 100), np.geomspace(.003, 1.15, 100)]
    quotient = ((1 + hs)**2 - 1) / hs
    assert np.max(abs(quotient - (2 + hs))) < 1e-12
    # La recta atraviesa A y B también cuando B está a la izquierda de A.
    assert np.max(abs(1 + (2 + hs)*hs - (1 + hs)**2)) < 1e-12
    assert all(1 + hs > 0)
    for sign in (-1, 1):
        distances = abs((2 + sign*np.geomspace(.75, .003, 100)) - 2)
        assert np.all(np.diff(distances) < 0)
    assert abs((2 + .003) - (2 - .003)) < .0060000001
    result = dict(cociente_h_no_cero="OK", secantes_por_A_y_B="OK",
                  limite_derecho=2, limite_izquierdo=2, derivada=2,
                  dominio_B_positivo="OK", h_cero_no_evaluado="OK")
    Path("generados/validacion_matematica.json").write_text(
        json.dumps(result, indent=2), encoding="utf8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

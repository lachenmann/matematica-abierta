"""Comprobación matemática independiente de EXP003, sin Manim ni audio.

Sólo utiliza aritmética racional exacta de la biblioteca estándar. El ensayo
finito complementa los argumentos algebraicos consignados en la auditoría;
no se presenta como prueba empírica de una afirmación sobre todos los índices.
"""
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
THRESHOLD = 10**6


def a(n):
    assert isinstance(n, int) and n >= 0
    return Fraction(1, n + 1)


def b(n, threshold=THRESHOLD):
    assert isinstance(n, int) and n >= 0
    assert isinstance(threshold, int) and threshold >= 0
    return a(n) if n <= threshold else Fraction(1)


def main():
    assert [a(n) for n in range(5)] == [Fraction(1, k) for k in range(1, 6)]
    # El intervalo de índices es inclusivo y comienza en cero.
    assert THRESHOLD - 0 + 1 == 1_000_001
    assert a(THRESHOLD) == b(THRESHOLD) == Fraction(1, 1_000_001)
    assert a(THRESHOLD + 1) == Fraction(1, 1_000_002)
    assert b(THRESHOLD + 1) == 1
    assert a(THRESHOLD + 1) != b(THRESHOLD + 1)
    # Verificación exhaustiva del prefijo concreto, con racionales exactos.
    assert all(a(n) == b(n) for n in range(THRESHOLD + 1))
    probes = [0, 1, 2, 9, 99, THRESHOLD - 1, THRESHOLD,
              THRESHOLD + 1, THRESHOLD + 2, 10**9, 10**12]
    assert all(a(n + 1) < a(n) and a(n) > 0 for n in probes)
    assert all(b(n) == 1 for n in probes if n > THRESHOLD)
    # Cualquier número positivo L de términos iniciales: último índice L-1.
    for length in [1, 2, 10, 1000, 10**6, 10**12]:
        threshold = length - 1
        assert a(threshold) == b(threshold, threshold)
        assert a(length) != b(length, threshold)
    # Una muestra finita no consecutiva también puede conservarse.
    finite_sample = [0, 23, 598, 10**12 + 7]
    threshold = max(finite_sample)
    assert all(a(n) == b(n, threshold) for n in finite_sample)
    assert a(threshold + 1) != b(threshold + 1, threshold)
    result = {
        "aritmetica": "fracciones exactas; biblioteca estándar",
        "dominio": "naturales desde cero",
        "umbral_inclusivo": THRESHOLD,
        "terminos_comunes_verificados": THRESHOLD + 1,
        "ultimo_indice_comun": THRESHOLD,
        "primer_indice_diferente": THRESHOLD + 1,
        "a_ultimo_comun": str(a(THRESHOLD)),
        "a_primero_diferente": str(a(THRESHOLD + 1)),
        "b_primero_diferente": str(b(THRESHOLD + 1)),
        "monotonia_a": "OK",
        "constancia_b_posterior": "OK",
        "generalizacion_prefijos_finitos": "OK",
        "muestra_finita_arbitraria": "OK",
        "alcance": "comprueba valores y fronteras; argumento universal en AUDITORIA_MATEMATICA.md",
        "resultado": "OK",
    }
    dest = ROOT / "generados"
    dest.mkdir(exist_ok=True)
    (dest / "validacion_matematica.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

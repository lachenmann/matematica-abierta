"""Conservative spoken-math normalizer. Ambiguity blocks synthesis."""
import json
import re
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / 'pronunciacion/es.json'


def load(path=DEFAULT):
    data = json.loads(Path(path).read_text(encoding='utf8'))
    for key in ('expresiones', 'simbolos', 'letras', 'nombres'):
        if not isinstance(data.get(key), dict):
            raise ValueError(f'Diccionario sin {key}')
    return data


def normalize(text, dictionary, required_names=()):
    if not isinstance(text, str) or not text.strip():
        raise ValueError('Texto vacío')
    for name in required_names:
        if name not in dictionary['nombres'] or name not in text:
            raise ValueError(f'Nombre propio sin pronunciación o ausente: {name}')

    def atom(s):
        if s in dictionary['letras']:
            return dictionary['letras'][s]
        if s in dictionary.get('numeros', {}):
            return dictionary['numeros'][s]
        raise ValueError(f'Índice/exponente sin pronunciación: {s}')

    def math(match):
        expr = (match.group(1) or match.group(2)).strip()
        if expr in dictionary['expresiones']:
            return dictionary['expresiones'][expr]
        index = re.fullmatch(r'([A-Za-z])_(?:([A-Za-z]|\d+)|\{([A-Za-z]|\d+)\})', expr)
        if index:
            return f'{atom(index[1])} sub {atom(index[2] or index[3])}'
        power = re.fullmatch(r'([A-Za-z])\^(?:([A-Za-z]|\d+)|\{([A-Za-z]|\d+)\})', expr)
        if power:
            base, exponent = power[1], power[2] or power[3]
            return atom(base) + {'2': ' al cuadrado', '3': ' al cubo'}.get(exponent, ' elevado a ' + atom(exponent))
        if expr in dictionary['simbolos']:
            return dictionary['simbolos'][expr]
        raise ValueError(f'Expresión matemática requiere lectura explícita en diccionario: {expr}')

    spoken = re.sub(r'\$([^$]+)\$|\\\((.*?)\\\)', math, text)
    for name, reading in sorted(dictionary['nombres'].items(), key=lambda x: -len(x[0])):
        spoken = re.sub(r'(?<!\w)' + re.escape(name) + r'(?!\w)', lambda _: reading, spoken)
    # Do not guess fractions, signs, units, raw TeX, numerals or identifiers.
    if re.search(r'[\d_\^=+*/\\$<>{}≤≥≠∞√∑∫π]|[A-Za-z][²³]', spoken):
        raise ValueError(f'Queda notación sin verbalizar: {spoken}')
    return re.sub(r'\s+', ' ', spoken).strip()

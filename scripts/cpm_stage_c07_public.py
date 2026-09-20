#!/usr/bin/env python3
"""Preparación efímera del PR C07: origen privado exacto -> edición web propuesta.

Nunca modifica Drive, ni hace merge, ni despliega. Se elimina del PR tras ejecutar.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import re

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

ROOT = Path.cwd()
SOURCE_ID = '1YRy3FBX7fTIkjhlSNAXhJGj0sH2NmybW'
SOURCE_SHA256 = 'c7006022045a93acb2e7405e5e789196884bc446bb3305298aa7f0cc0e35c3df'
DEST = ROOT / 'libros/capitulos/algebra-de-derivadas-y-regla-de-la-cadena.md'
BOOK = ROOT / 'libros/para-matematicos/calculo-para-matematicos.md'
INDEX = ROOT / 'libros/capitulos/index.qmd'


def replace_once(text, before, after, label):
    n = text.count(before)
    if n != 1:
        raise RuntimeError(f'Invariante de edición {label}: esperada 1 coincidencia, encontradas {n}')
    return text.replace(before, after, 1)


def read_drive():
    raw = os.environ.get('CPM_DRIVE_SERVICE_ACCOUNT_JSON', '')
    if not raw:
        raise RuntimeError('Credencial autorizada no configurada')
    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(
        info, scopes=['https://www.googleapis.com/auth/drive.readonly'])
    drive = build('drive', 'v3', credentials=creds, cache_discovery=False)
    stream = io.BytesIO()
    downloader = MediaIoBaseDownload(stream, drive.files().get_media(fileId=SOURCE_ID))
    done = False
    while not done:
        _, done = downloader.next_chunk()
    source_bytes = stream.getvalue()
    if hashlib.sha256(source_bytes).hexdigest() != SOURCE_SHA256:
        raise RuntimeError('SHA-256 de la fuente privada distinto al auditado: ABORTAR')
    return source_bytes.decode('utf-8')


def main():
    if DEST.exists():
        raise RuntimeError('La ruta pública del capítulo ya existe; no sobrescribir')
    source = read_drive()
    header = ('---\nchapter_id: T1-C08\nstatus: OPEN\n'
              'section_status: "VISIBLE_7.1-7.11_COMPLETE / EXR-SOL_0276--0315_MATERIALIZED / FINAL_AUDIT_AND_VISUAL_QA_PENDING"')
    if not source.startswith(header):
        raise RuntimeError('El manuscrito privado ya no tiene el estado esperado; detener')
    parts = source.split('\n---\n', 1)
    if len(parts) != 2 or not parts[1].startswith('\n# Álgebra de derivadas y regla de la cadena {#sec-t1-c08}'):
        raise RuntimeError('Cabecera Markdown canónica no reconocida')
    body = parts[1].lstrip('\n')
    if body.count('### Auditoría del banco') != 1:
        raise RuntimeError('No se pudo identificar de forma inequívoca el cierre editorial interno')
    body = body.split('### Auditoría del banco', 1)[0].rstrip() + '\n'
    # Identificadores legibles por Quarto ya están en los divs {#exr...}/{#sol...};
    # comentarios de control interno no deben aparecer en la edición web.
    body = re.sub(r'^<!-- CPM-T1-(?:EXR|SOL)-\d{4}.*?-->\n', '', body, flags=re.M)
    exercises = re.findall(r'^::: \{#exr-t1-(\d{4})\}', body, flags=re.M)
    solutions = re.findall(r'^::: \{#sol-t1-(\d{4})\}', body, flags=re.M)
    expected = [f'{i:04d}' for i in range(276, 316)]
    if exercises != expected or solutions != expected:
        raise RuntimeError('No coincide el banco exacto 40/40: ABORTAR')
    if '[[' in body or '\\(' in body or '\\[' in body:
        raise RuntimeError('Sintaxis editorial incompatible detectada')
    frontmatter = '''---
title: "Álgebra de derivadas y regla de la cadena"
description: "Capítulo 7 de Cálculo para matemáticos: linealidad, producto, cociente, potencias y regla de la cadena; 40 ejercicios resueltos."
content-id: MA-BCH-0065
content-type: book-chapter
collection: PM-CAL
book-id: MA-BOK-0001
status: published
areas:
  - calculo
  - analisis
level: fundamental
provenance:
  type: original
  sources: []
license: GFDL-1.3-or-later
date-created: 2026-09-20
date-modified: 2026-09-20
prerequisites:
  - MA-BCH-0003
  - MA-BCH-0004
  - MA-BCH-0010
  - MA-BCH-0062
  - MA-BCH-0063
  - MA-BCH-0064
number-sections: true
number-depth: 2
number-offset: [6]
---

'''
    web = frontmatter + body
    book = BOOK.read_text(encoding='utf-8')
    book = replace_once(book, '  - MA-BCH-0064\nprovenance:', '  - MA-BCH-0064\n  - MA-BCH-0065\nprovenance:', 'relacion libro')
    book = replace_once(book,
        '6. **La derivada y la aproximación lineal local**.\n',
        '6. **La derivada y la aproximación lineal local**.\n7. **Álgebra de derivadas y regla de la cadena**.\n', 'lista descriptiva')
    book = replace_once(book,
        '6. [**La derivada y la aproximación lineal local**](../capitulos/la-derivada-y-la-aproximacion-lineal-local.md) (`MA-BCH-0064`).\n',
        '6. [**La derivada y la aproximación lineal local**](../capitulos/la-derivada-y-la-aproximacion-lineal-local.md) (`MA-BCH-0064`).\n7. [**Álgebra de derivadas y regla de la cadena**](../capitulos/algebra-de-derivadas-y-regla-de-la-cadena.md) (`MA-BCH-0065`).\n', 'enlace libro')
    book = replace_once(book, 'contiene **seis capítulos completos**', 'contiene **siete capítulos completos**', 'conteo de capítulos')
    book = replace_once(book,
        'Los capítulos posteriores desarrollarán derivación, aplicaciones de la derivada, integración,',
        'Los capítulos posteriores desarrollarán las derivadas de funciones inversas, aplicaciones de la derivada, integración,',
        'transición temática')
    book = replace_once(book, 'date-modified: 2026-09-19', 'date-modified: 2026-09-20', 'fecha del libro')
    index = INDEX.read_text(encoding='utf-8')
    marker = '- [**La derivada y la aproximación lineal local**](la-derivada-y-la-aproximacion-lineal-local.md) (`MA-BCH-0064`) — Capítulo 6 completo de la edición vigente.\n'
    index = replace_once(index, marker, marker + '- [**Álgebra de derivadas y regla de la cadena**](algebra-de-derivadas-y-regla-de-la-cadena.md) (`MA-BCH-0065`) — Capítulo 7: reglas demostradas, dominios, composiciones y 40 ejercicios con solución.\n', 'índice transversal')
    DEST.write_text(web, encoding='utf-8')
    BOOK.write_text(book, encoding='utf-8')
    INDEX.write_text(index, encoding='utf-8')
    print('PREPARACION_OK: tres archivos públicos preparados; origen SHA-256 comprobado, ejercicios y soluciones 40/40. No se ha publicado.')


if __name__ == '__main__':
    main()

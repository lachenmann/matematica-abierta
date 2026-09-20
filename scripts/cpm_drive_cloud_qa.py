#!/usr/bin/env python3
"""Transferencia temporal Drive -> runner -> Drive para la QA de CPM T1-C08.

No almacena el manuscrito ni las capturas en GitHub; requiere identidad de servicio
con acceso concedido expresamente a los archivos y carpetas necesarios de Drive.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Identificadores fijos obtenidos de los originales canónicos, no de sus títulos.
SOURCE_ID = '1YRy3FBX7fTIkjhlSNAXhJGj0sH2NmybW'
CSS_ID = '1VVwVw8556jOH9A4YloV_w0w1dNEW3ggf'
VERIFIER_ID = '1Uk9SaWlnlqms30tR5av_by10bXxxW3GR'
PREVIEW_FOLDER_ID = '1jkBgGT9OEohTz2ThdSOpaW2qWbNfoLO4'
BUILD_FOLDER_ID = '1a0BzGVD_nI6vuYmfFjvqJRDNonRARbsL'
QA_FOLDER = 'QA_C08_MATHJAX4_NAV'
FOLDER_MIME = 'application/vnd.google-apps.folder'


def client():
    value = os.environ.get('CPM_DRIVE_SERVICE_ACCOUNT_JSON', '')
    if not value.strip():
        raise RuntimeError('Falta el secreto CPM_DRIVE_SERVICE_ACCOUNT_JSON; no se puede leer Drive.')
    data = json.loads(value)
    credentials = service_account.Credentials.from_service_account_info(
        data, scopes=['https://www.googleapis.com/auth/drive'])
    return build('drive', 'v3', credentials=credentials, cache_discovery=False)


def metadata(api, file_id):
    return api.files().get(fileId=file_id,
        fields='id,name,mimeType,size,trashed', supportsAllDrives=True).execute()


def direct_children(api, parent_id):
    token = None
    while True:
        page = api.files().list(
            q=f"'{parent_id}' in parents and trashed = false",
            fields='nextPageToken,files(id,name,mimeType,size)',
            pageSize=1000, pageToken=token,
            supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        yield from page.get('files', [])
        token = page.get('nextPageToken')
        if not token:
            break


def safe_name(name):
    if not name or name in ('.', '..') or '/' in name or '\\' in name or '\x00' in name:
        raise RuntimeError('Nombre inseguro de archivo o directorio en Drive.')
    return name


def fetch_bytes(api, file_id, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Solo archivos almacenados, no exportaciones ni accesos mediante URL pública.
    destination.write_bytes(api.files().get_media(
        fileId=file_id, supportsAllDrives=True).execute())


def fetch_tree(api, folder_id, destination):
    destination.mkdir(parents=True, exist_ok=True)
    for entry in direct_children(api, folder_id):
        target = destination / safe_name(entry['name'])
        if entry['mimeType'] == FOLDER_MIME:
            fetch_tree(api, entry['id'], target)
        elif not entry['mimeType'].startswith('application/vnd.google-apps.'):
            fetch_bytes(api, entry['id'], target)
        else:
            raise RuntimeError('Recurso de Drive no descargable: ' + entry['name'])


def download(api, root):
    for file_id, relative, expected_name in (
        (SOURCE_ID, '01 - Tomo I/T1-C08.md', 'T1-C08.md'),
        (CSS_ID, '90 - Assets/cpm-math-responsive.css', 'cpm-math-responsive.css'),
        (VERIFIER_ID, '00 - Administración/CPM_C08_QA_MATHJAX4_NAVEGACION_v01.py',
            'CPM_C08_QA_MATHJAX4_NAVEGACION_v01.py')):
        meta = metadata(api, file_id)
        if meta['name'] != expected_name or meta['mimeType'] == FOLDER_MIME or meta.get('trashed'):
            raise RuntimeError('Archivo canónico inesperado: ' + relative)
        fetch_bytes(api, file_id, root / relative)
    if metadata(api, PREVIEW_FOLDER_ID)['mimeType'] != FOLDER_MIME:
        raise RuntimeError('La carpeta de Quarto no coincide con el ID registrado.')
    fetch_tree(api, PREVIEW_FOLDER_ID, root / '99 - Build/_migration_preview')
    print('DRIVE_STAGE_COMPLETE: copia efímera en runner; sin publicación ni escritura canónica.')


def find_or_create_folder(api, parent, name):
    matches = [f for f in direct_children(api, parent)
               if f['name'] == name and f['mimeType'] == FOLDER_MIME]
    if len(matches) > 1:
        raise RuntimeError('Carpetas homónimas ambiguas en Drive: ' + name)
    if matches:
        return matches[0]['id']
    return api.files().create(body={'name': name, 'mimeType': FOLDER_MIME,
                                    'parents': [parent]}, fields='id',
                              supportsAllDrives=True).execute()['id']


def upload(api, root, run_id):
    source = root / '99 - Build/QA_C08_MATHJAX4_NAV'
    if not source.is_dir():
        raise RuntimeError('No hay directorio de resultados; no se inventará evidencia.')
    report = source / 'CPM_C08_QA_MATHJAX4_NAV_RESULTADO.json'
    if not report.is_file():
        raise RuntimeError('Falta JSON de ejecución; no se subirán capturas huérfanas.')
    parent = find_or_create_folder(api, BUILD_FOLDER_ID, QA_FOLDER)
    run = find_or_create_folder(api, parent, 'github-run-' + run_id)
    paths = [report] + sorted(source.glob('*.png'))
    for path in paths:
        mime = 'application/json' if path.suffix == '.json' else 'image/png'
        media = MediaFileUpload(str(path), mimetype=mime, resumable=False)
        api.files().create(body={'name': path.name, 'parents': [run]},
                           media_body=media, fields='id', supportsAllDrives=True).execute()
    print('EVIDENCE_DRIVE_FOLDER_ID=' + run)
    print('EVIDENCE_FILES=' + str(len(paths)))
    print('Evidencia privada en Drive; no se cargaron artefactos a GitHub.')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('download', 'upload'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--run-id', default='')
    args = parser.parse_args()
    api = client()
    if args.command == 'download':
        download(api, args.root.resolve())
    else:
        if not args.run_id.isdecimal():
            raise RuntimeError('El identificador de ejecución de GitHub debe ser numérico.')
        upload(api, args.root.resolve(), args.run_id)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('CPM_CLOUD_QA_ERROR:', str(exc), file=sys.stderr)
        raise SystemExit(2)

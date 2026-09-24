#!/usr/bin/env python3
"""Transferencia temporal Drive -> runner -> Drive para la QA de CPM T1-C08.

No almacena el manuscrito ni las capturas en GitHub; requiere identidad de servicio
con acceso concedido expresamente a los archivos y carpetas necesarios de Drive.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import tarfile
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
# Archivo temporal propiedad del usuario, creado mediante la conexión OAuth de Work.
# La cuenta de servicio solo actualiza sus bytes; no crea archivos sin cuota.
TRANSFER_FILE_ID = '1ODLPkMURkM6THxdfi-Fn9SWv8Bo8-Xbi'
QA_FOLDER_ID = '11iMBg0Rk2kq2nMjMWi_YQLsJlpWXsVD5'
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
    """Entrega privada de evidencias reales a un archivo propiedad del usuario.

    Work descarga luego este paquete y crea los archivos finales con OAuth del
    propietario. No se usan artefactos de GitHub ni nuevos secretos.
    """
    source = root / '99 - Build/QA_C08_MATHJAX4_NAV'
    report = source / 'CPM_C08_QA_MATHJAX4_NAV_RESULTADO.json'
    if not report.is_file():
        raise RuntimeError('Falta JSON de ejecución; no se transferirán capturas huérfanas.')
    expected_png = {
        'C08_MATHJAX4_NAV_390_MENU.png',
        'C08_MATHJAX4_1440_SECCION_7_8.png',
        'C08_MATHJAX4_390_TABLA_7_8.png',
        'C08_MATHJAX4_390_EJERCICIOS.png',
        'C08_MATHJAX4_390_ULTIMA_SOLUCION.png',
        'C08_MATHJAX4_1440_DESKTOP.png',
    }
    paths = [report] + sorted(source.glob('*.png'))
    if not expected_png.issubset({p.name for p in paths}):
        raise RuntimeError('Faltan capturas obligatorias; no se transferirá evidencia incompleta.')
    meta = api.files().get(fileId=TRANSFER_FILE_ID,
        fields='id,name,parents,owners(emailAddress),trashed',
        supportsAllDrives=True).execute()
    if meta.get('trashed') or QA_FOLDER_ID not in meta.get('parents', []):
        raise RuntimeError('El archivo de transferencia no está en la carpeta QA privada.')
    owners = {x.get('emailAddress') for x in meta.get('owners', [])}
    if 'alevip@gmail.com' not in owners:
        raise RuntimeError('El archivo de transferencia no pertenece al propietario OAuth.')
    archive = source / ('CPM_C08_PRIVATE_TRANSFER_' + run_id + '.tar.gz')
    manifest = {'run_id': run_id, 'files': {}}
    with tarfile.open(archive, 'w:gz') as tar:
        for path in paths:
            data = path.read_bytes()
            manifest['files'][path.name] = hashlib.sha256(data).hexdigest()
            tar.add(path, arcname=path.name, recursive=False)
        payload = json.dumps(manifest, sort_keys=True).encode('utf-8')
        info = tarfile.TarInfo('manifest.json')
        info.size = len(payload)
        tar.addfile(info, io.BytesIO(payload))
    expected_sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    media = MediaFileUpload(str(archive), mimetype='application/gzip', resumable=False)
    api.files().update(fileId=TRANSFER_FILE_ID,
        body={'name': archive.name, 'mimeType': 'application/gzip'},
        media_body=media, fields='id,name,size', supportsAllDrives=True).execute()
    actual = api.files().get_media(fileId=TRANSFER_FILE_ID,
        supportsAllDrives=True).execute()
    if hashlib.sha256(actual).hexdigest() != expected_sha:
        raise RuntimeError('La lectura de vuelta del paquete Drive no coincide con SHA-256.')
    print('PRIVATE_OWNER_OWNED_TRANSFER_ID=' + TRANSFER_FILE_ID)
    print('PRIVATE_TRANSFER_SHA256=' + expected_sha)
    print('PRIVATE_TRANSFER_FILES=' + str(len(paths)))
    print('OAuth de Work debe extraer y guardar el JSON y las capturas por separado.')


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

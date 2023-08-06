import sys
import os
import shutil
from .create.model import write_model
from .create.namespace import write_namespace
from loguru import logger
from typing import List

path_file, command = sys.argv[0], sys.argv[1]
path_ref = os.path.dirname(__file__)
root = sys.path[0]


def copy_folder(path_from: List[str], path_to: List[str]):
    logger.info('Copiando Pasta: {} para {}', path_from, path_to)
    shutil.copytree(
        os.path.join(path_ref, *path_from),
        os.path.join(root, *path_to)
    )


def copy_file(path_from: List[str], path_to: List[str]):
    logger.info('Copiando Arquivo: {} para {}', path_from, path_to)
    shutil.copyfile(
        os.path.join(path_ref, *path_from),
        os.path.join(root, *path_to)
    )


def create_server(root):
    os.makedirs(os.path.join(root, 'server'))
    copy_folder(['api'], ['server', 'api'])
    copy_folder(['database'], ['server', 'database'])
    copy_folder(['portal'], ['server', 'portal'])
    copy_file(['create', 'server.py'], ['server', '__init__.py'])
    copy_file(['create', 'app.py'], ['app.py'])
    copy_file(['create', 'env.py'], ['.env'])


def create_namespace_on_version(version, name, model, is_create_model):
    path = os.path.join(root, 'server', 'api', version, name)
    os.makedirs(path)
    write_namespace(os.path.join(root, 'server', 'api',
                    version, name), name)
    if is_create_model:
        write_model(os.path.join(root, 'server',
                    'database', 'models'), model)


if command == 'create_server':
    create_server(root=root)

elif command == 'create_namespace':
    version = input('Qual a Versão? ')
    namespace = input('Qual o Nome Do NameSpace? ')
    is_create_model = input('Deseja Criar o Model? (S/n) ').upper()
    if is_create_model == '' or is_create_model == 'S':
        is_create_model = True
        model = input('Qual o Nome Do Model? ')
    else:
        is_create_model = False
        model = None

    create_namespace_on_version(version, namespace, model, is_create_model)

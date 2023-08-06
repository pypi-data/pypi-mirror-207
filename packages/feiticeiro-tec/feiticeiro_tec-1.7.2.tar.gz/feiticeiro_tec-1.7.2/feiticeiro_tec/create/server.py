import os
from flask import Flask
from server.api import init_app as ini_api
from server.database import init_app as ini_database, init_permissions
from server.portal import init_app as ini_portal
from loguru import logger
from flask_alembic import Alembic
from flask_jwt_extended import JWTManager
from datetime import timedelta


class Servidor(Flask):
    def __init__(self):
        super().__init__(__name__)
        self.config.from_prefixed_env()
        self.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(
            minutes=int(os.environ['ACCESS_TOKEN_EXPIRES'])
        )
        self.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(
            minutes=int(os.environ['REFRESH_TOKEN_EXPIRES'])
        )

    def init_api(self):
        self.jwt = JWTManager(self)
        self.api = ini_api(self)

    def init_database(self):
        self.db = ini_database(self)
        init_permissions(self)

    def init_portal(self):
        self.portal = ini_portal(self)

    def init_commands(self):
        @self.cli.command()
        def migrate_db():
            logger.info('Migrando Banco de Dados')
            alembic = Alembic()
            alembic.revision('autogenerate')
            alembic.upgrade('head')

        @self.cli.command()
        def create_db():
            logger.info('Criando Banco de Dados')
            with self.app_context():
                self.db.create_all()

        @self.cli.command()
        def create_permissions():
            logger.info('Inicializando Permissões')
            from server.database.models.permission import (
                Permission, PermissionGroup, PermissionGroupPermission)
            with self.app_context():
                Permission.create_permissions(self)
                PermissionGroup.create_group()
                PermissionGroupPermission.create_permission_on_group()

        self.cli.add_command(migrate_db, 'migrate_db')
        self.cli.add_command(create_db, 'create_db')
        self.cli.add_command(create_permissions, 'create_permissions')

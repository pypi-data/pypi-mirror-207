from flask import Flask
from loguru import logger
from .base import Base
from .. import db


class PermissionGroup(db.Model, Base):
    __tablename__ = 'permission_group'
    nome = db.Column(db.String(100), nullable=False, unique=True)
    permissions = db.relationship('PermissionGroupPermission',
                                  backref='permission_group',
                                  lazy=True)

    def insert_infos(self, nome):
        self.nome = nome

    @staticmethod
    def create_group():
        logger.debug('Criando grupos de permissões')
        query = db.text('''
            SELECT endpoint
            FROM permission
            WHERE is_delete = 0 AND is_active = 1
            GROUP BY endpoint
        ''')
        endpoints = db.session.execute(query).fetchall()
        PermissionGroup.query.update({'is_delete': True})
        for row in endpoints:
            permission_group = PermissionGroup.query.filter(
                PermissionGroup.nome == row.endpoint
            ).first()
            if not permission_group:
                permission_group = PermissionGroup(nome=row.endpoint)
                permission_group.add()
            else:
                permission_group.is_delete = False
        db.session.commit()
        logger.debug('Grupos de permissões criados')


class PermissionGroupPermission(db.Model, Base):
    __tablename__ = 'permission_group_permission'
    permission_id = db.Column(db.String(36),
                              db.ForeignKey('permission.id'),
                              nullable=False)
    permission_group_id = db.Column(db.String(36),
                                    db.ForeignKey('permission_group.id'),
                                    nullable=False)

    @staticmethod
    def create_permission_on_group():
        logger.debug('Criando permissões nos grupos')
        query = db.text('''
            SELECT
                pg.id as permission_group_id,
                p.id as permission_id
            FROM permission_group pg
            LEFT JOIN permission p ON
                p.endpoint = pg.nome
            WHERE pg.is_delete = 0 AND pg.is_active = 1
            ''')
        permissions = db.session.execute(query).fetchall()
        PGP = PermissionGroupPermission
        PGP.query.update({'is_delete': True})
        for row in permissions:
            permission = PGP.query.filter(
                PGP.permission_group_id == row.permission_group_id,
                PGP.permission_id == row.permission_id
            ).first()
            if not permission:
                permission = PGP(
                    permission_id=row.permission_id,
                    permission_group_id=row.permission_group_id
                )
                permission.add()
            else:
                permission.is_delete = False
        db.session.commit()
        logger.debug('Permissões nos grupos criadas')


class Permission(db.Model, Base):
    __tablename__ = 'permission'
    endpoint = db.Column(db.String(100), nullable=False)
    method = db.Column(db.String(100), nullable=False)
    rule = db.Column(db.String(255), nullable=False)
    groups = db.relationship('PermissionGroupPermission',
                             backref='permission',
                             lazy=True)

    def __repr__(self):
        return f'<Permission {self.endpoint}:{self.method} id:{self.id}>'

    @staticmethod
    def create_permissions(app: Flask):
        logger.debug('Criando permissões')
        Permission.query.update({'is_delete': True})
        for rule in app.url_map.iter_rules():
            for method in rule.methods:
                permission = Permission.query.filter(
                    Permission.endpoint == rule.endpoint,
                    Permission.method == method
                ).first()
                if not permission:
                    permission = Permission(
                        endpoint=rule.endpoint,
                        method=method,
                        rule=rule.rule
                    )
                    permission.add()
                else:
                    permission.update(is_delete=False, rule=rule.rule)

        db.session.commit()
        logger.debug('Permissões criadas')

    def update(self, is_active=None, is_delete=None, rule=None):
        self.is_active = is_active if is_active is not None else self.is_active
        self.is_delete = is_delete if is_delete is not None else self.is_delete
        self.rule = rule if rule is not None else self.rule
        logger.debug(f'Permissão atualizada: {self}')

    @staticmethod
    def is_allowed(endpoint, method):
        query = db.text("""
        SELECT 1
        FROM Permission P
        WHERE
            P.endpoint = :endpoint
            AND P.method = :method
            AND P.is_active = 1
            AND P.is_delete = 0
        """)
        query = query.bindparams(endpoint=endpoint, method=method)

        return True if db.session.execute(query).first() else False

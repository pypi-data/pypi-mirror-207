from flask_sqlalchemy import SQLAlchemy
from loguru import logger
from flask import Flask, request, abort, jsonify, Response

db = SQLAlchemy()


def init_permissions(app: Flask):
    from server.database.models.permission import Permission

    @app.before_request
    def before_request():
        endpoint = request.endpoint
        method = request.method
        is_allowed = Permission.is_allowed(endpoint, method)
        if not is_allowed:
            abort(code=503, description='Rota Indisponível')


def init_app(app: Flask):
    logger.info('Iniciando Banco de Dados')
    db.init_app(app)
    # flake8: noqa: F401
    from server.database import models
    logger.debug('Tabelas Inicializadas {}'.format(models.__all__))
    return db

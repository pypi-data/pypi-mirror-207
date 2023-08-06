from flask_restx import Api, abort
from loguru import logger
from flask import Flask, Blueprint
from flask_jwt_extended.exceptions import NoAuthorizationError

blueprint_api = Blueprint('api', __name__)


authorizations = authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'prefix': 'Bearer'
    }
}
api = Api(blueprint_api, authorizations=authorizations, security='Bearer Auth')


def token_invalido(*args, **kwargs):
    abort(401, 'Token Inválido')


def init_app(app: Flask):
    logger.info('Inicializando API')

    app.register_blueprint(blueprint_api)
    with app.app_context():
        api.errorhandler(NoAuthorizationError)(token_invalido)

    # flake8: noqa: F401
    from server.api import v1
    logger.info(f'API v1 Inicializada {v1.__all__}')
    return api

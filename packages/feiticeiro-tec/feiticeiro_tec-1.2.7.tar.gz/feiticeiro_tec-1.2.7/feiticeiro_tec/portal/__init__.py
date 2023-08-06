from flask import Flask, Blueprint
from loguru import logger

portal = Blueprint(
    'portal', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/portal'
)


def init_app(app: Flask):
    from server.portal import routes
    logger.info(f'Blueprint portal routes: {routes.__all__}')
    app.register_blueprint(portal)

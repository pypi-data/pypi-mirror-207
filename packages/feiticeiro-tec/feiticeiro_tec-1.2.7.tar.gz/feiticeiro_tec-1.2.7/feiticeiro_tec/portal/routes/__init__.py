__all__ = []
from flask import render_template
from server.portal.utils import login_required
from flask_jwt_extended import get_jwt_identity
from .. import portal


@portal.route('/')
def index():
    return render_template('page/index.html')


@portal.route('/permissions/')
@login_required
def permissions():
    return render_template('page/permissions.html', user=get_jwt_identity())

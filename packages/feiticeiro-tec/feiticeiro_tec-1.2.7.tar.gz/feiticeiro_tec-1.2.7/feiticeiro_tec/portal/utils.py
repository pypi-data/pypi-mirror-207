from flask import redirect, url_for, flash
from flask_jwt_extended import verify_jwt_in_request
from functools import wraps


def login_required(f):
    @wraps(f)
    def inner(*args, **kwargs):
        try:
            verify_jwt_in_request(locations=['cookies'])
        except Exception:
            flash("Sessão expirada", "warning")
            return redirect(url_for('portal.index'))
        return f(*args, **kwargs)
    return inner

from flask_restx.reqparse import RequestParser
from server.api.utils.forms import (
    email_validate, password_validate,
    boolean_validate)


def fields_login(form):
    form.add_argument(
        'email', type=email_validate,
        required=True, location='form'
    )
    form.add_argument(
        'senha', type=password_validate,
        required=True, location='form'
    )
    usuario_form.add_argument(
        'is_admin', type=boolean_validate, choices=[True, False],
        required=False, location='form'
    )


usuario_form = RequestParser()
fields_login(usuario_form)
usuario_form.add_argument(
    'nome', type=str,
    required=True, location='form'
)
usuario_form.add_argument(
    'sobrenome', type=str,
    required=True, location='form')


login_form = RequestParser()
fields_login(login_form)

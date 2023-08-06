from flask_restx import fields
from server.api.utils.serializers import base_serializer
from server.api import api

usuario_serializer = api.model('Usuario', {
    **base_serializer,
    'email': fields.String(
        required=True,
        example='teste@gmail.com'
    ),
    'nome': fields.String(
        required=True,
        example='Teste'
    ),
    'sobrenome': fields.String(
        required=True,
        example='Teste'
    ),
    'is_admin': fields.Boolean(
        required=False,
    )
})

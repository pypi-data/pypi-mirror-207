from flask_restx import Resource, marshal, abort
from server.api import api
from server.database.models import Usuario
from .forms import usuario_form, login_form
from .serializers import usuario_serializer
from server.api.utils.serializers import token_serializer

np_usuario = api.namespace(
    'usuarios',
    description='Operações relacionadas a usuários',
    path='/v1/usuarios'
)


class UsuarioResource(Resource):
    @np_usuario.expect(usuario_form)
    @np_usuario.marshal_with(usuario_serializer, code=201)
    def post(self):
        data = usuario_form.parse_args()
        user = Usuario()
        user.insert_cadastro(**data)
        user.add()
        user.save()
        return user, 201

    def get(self, id=None):
        ...

    def patch(self, id):
        ...

    def delete(self, id):
        ...


class UsuarioAuthResource(Resource):
    @np_usuario.expect(login_form)
    @np_usuario.response(201, 'Logado com sucesso!', token_serializer)
    def post(self):
        data = login_form.parse_args()
        user: Usuario = Usuario.query.filter_by(
            email=data['email']
        ).first()
        if not user or not user.login(data['senha']):
            abort(401, message="Email ou senha inválidos")
        token = user.generate_token()
        return marshal(token, token_serializer), 201


np_usuario.add_resource(UsuarioResource, '',
                        endpoint='usuario',
                        methods=['POST', 'GET'])
np_usuario.add_resource(UsuarioResource, '/<uuid:id>',
                        endpoint='usuario-id',
                        methods=['GET', 'PATCH', 'DELETE'])
np_usuario.add_resource(UsuarioAuthResource, '/auth',
                        endpoint='usuario-auth',
                        methods=['POST'])

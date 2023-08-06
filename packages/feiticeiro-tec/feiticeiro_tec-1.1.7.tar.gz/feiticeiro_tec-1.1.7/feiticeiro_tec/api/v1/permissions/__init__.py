from flask_restx import Resource
from server.api import api
from server.database.models import Permission
from .serializers import permission_serializer
from .form import form_permission_update

np_permissions = api.namespace(
    'permissions',
    description='Operações relacionadas a permissões',
    path='/v1/permissions'
)


class PermissionResource(Resource):
    @np_permissions.marshal_with(permission_serializer)
    def get(self, id=None):
        """Retorna a permissão"""
        if id:
            return Permission.query.get_or_404(str(id))
        else:
            return Permission.query.all()

    @np_permissions.marshal_with(permission_serializer)
    @np_permissions.expect(form_permission_update)
    def put(self, id):
        """Define se a permissão está ativa ou não"""
        data = form_permission_update.parse_args()
        permission = Permission.query.get_or_404(str(id))
        permission.update(**data)
        permission.save()
        return permission


np_permissions.add_resource(
    PermissionResource, '/',
    endpoint='permissions',
    methods=['GET']
)

np_permissions.add_resource(
    PermissionResource, '/<uuid:id>',
    endpoint='permissions-id',
    methods=['GET', 'PUT']
)

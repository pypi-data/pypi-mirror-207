
from server.api import api
from server.api.utils.serializers import base_permission_serializer
permission_serializer = api.model('Permission', base_permission_serializer)

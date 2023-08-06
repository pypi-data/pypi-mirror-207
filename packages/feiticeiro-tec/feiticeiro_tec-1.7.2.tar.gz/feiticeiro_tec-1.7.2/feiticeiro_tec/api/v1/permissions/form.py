from flask_restx.reqparse import RequestParser
from server.api.utils.forms import boolean_validate

form_permission_update = RequestParser()
form = form_permission_update
form.add_argument('is_active', type=boolean_validate,
                  required=True, location='form')

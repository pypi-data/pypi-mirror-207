from server.api import api
from flask_restx import fields
import re
from validate_docbr import CPF, CNPJ


class Cnpj(fields.Raw):
    def format(self, value):
        return CNPJ().mask(value)


class Cpf(fields.Raw):
    def format(self, value):
        return CPF().mask(value)


class CnpjOrCpf(fields.Raw):
    def format(self, value):
        if len(value) == 11:
            return CPF().mask(value)
        else:
            return CNPJ().mask(value)


class Telefone(fields.Raw):
    def format(self, value):
        regex = r'([0-9]{2})([0-9]{4,5})([0-9]{4})', r'(\1) \2-\3'
        return re.sub(regex, value)


class Cep(fields.Raw):
    def format(self, value):
        return re.sub(r'([0-9]{5})([0-9]{3})', r'\1-\2', value)


base_serializer = {
    'id': fields.String(
        required=True,
        description='UUID do registro',
        example='123e4567-e89b-12d3-a456-426655440000'
    ),
    'create_time': fields.DateTime(
        required=True,
        description='Data de criação do registro',),
    'update_time': fields.DateTime(
        required=True,
        description='Data de atualização do registro',),
    'is_delete': fields.Boolean(
        required=True,
        description='Se o registro foi deletado ou não',
    ),
    'is_active': fields.Boolean(
        required=True,
        description='Se o registro está ativo ou não',
    )
}

base_endereco_serializer = {
    'endereco': fields.String(
        required=True,
        description='Endereço (Rua)',
        exemple='Rua das Flores'
    ),
    'numero': fields.String(
        required=True,
        description='Número do endereço',
        example='NUMERO 4 BLOCO 2 APTO 101'
    ),
    'bairro': fields.String(
        required=True,
        description='Bairro do endereço',
        exemple='Ponta Negra'
    ),
    'cidade': fields.String(
        required=True,
        description='Cidade do endereço',
        exemple='Natal'
    ),
    'estado': fields.String(
        required=True,
        description='Estado do endereço',
        exemple='RN'
    ),
    'cep': Cep(
        required=True,
        description='CEP do endereço',
        exemple='59092100'
    ),
    'complemento': fields.String(
        required=False,
        description='Complemento do endereço',
    )
}

base_empresa_serializer = {
    'cnpj_or_cpf': CnpjOrCpf(
        required=True,
        description='CNPJ ou CPF da empresa',
        exemple='000.000.000-00 | 00.000.000/0000-00'
    ),
    'razao_social': fields.String(
        required=True,
        description='Razão Social da empresa',
        exemple='Empresa LTDA'
    ),
    'nome_fantasia': fields.String(
        required=True,
        description='Nome Fantasia da empresa',
        exemple='Empresa'
    ),
    'telefone': Telefone(
        required=True,
        description='Telefone da empresa',
        exemple='(84) 99999-9999'
    )
}

base_empresa_plus_serializer = {
    **base_empresa_serializer,
    **base_endereco_serializer
}

base_permission_serializer = {
    **base_serializer,
    'endpoint': fields.String,
    'method': fields.String,
    'rule': fields.String,
}

base_token_serializer = {
    'access_token': fields.String(),
    'refresh_token': fields.String(),
}

token_serializer = api.model('Token', base_token_serializer)

base_field_error_serializer = {
    'erros': fields.Raw(
        example={'field': ['error']}
    )
}
field_error_serializer = api.model('FieldError', base_field_error_serializer)

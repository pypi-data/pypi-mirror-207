from server.database import db
from sqlalchemy import Column, DateTime, Boolean, String
from datetime import datetime
import uuid
from loguru import logger


class Base():
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    update_time = Column(DateTime, default=datetime.now,
                         onupdate=datetime.now, nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    def add(self):
        logger.debug('Adicionando {} ao Banco de Dados'.format(self))
        db.session.add(self)

    def save(self):
        logger.debug('Salvando {} no Banco de Dados'.format(self))
        db.session.commit()

    def delete(self):
        logger.debug('Deletando {} do Banco de Dados'.format(self))
        self.is_delete = True
        self.save()

    def __repr__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.id)


class BaseEndereco():
    endereco = Column(String(255), nullable=False)
    numero = Column(String(10), nullable=False)
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    estado = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
    complemento = Column(String(255), nullable=True)

    def insert_endereco(self, endereco, numero,
                        bairro, cidade, estado,
                        cep, complemento):
        logger.debug('Inserindo endereço')
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento


class BaseEmpresa():
    cnpj_or_cpf = Column(String(14), nullable=False)
    razao_social = Column(String(255), nullable=False)
    nome_fantasia = Column(String(255), nullable=False)
    telefone = Column(String(11), nullable=False)
    def insert_empresa(self, cnpj_or_cpf, razao_social,
                       nome_fantasia, telefone):
        logger.debug('Inserindo empresa')
        self.cnpj_or_cpf = cnpj_or_cpf
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.telefone = telefone


class BaseEmpresaPlus(BaseEmpresa, BaseEndereco):
    ...

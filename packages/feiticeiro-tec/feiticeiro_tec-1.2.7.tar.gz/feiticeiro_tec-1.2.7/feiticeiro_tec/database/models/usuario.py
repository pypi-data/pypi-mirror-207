from server.database import db
from .base import Base
from werkzeug.security import generate_password_hash, check_password_hash
from loguru import logger
from flask_jwt_extended import create_access_token, create_refresh_token


class Usuario(Base, db.Model):
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def insert_cadastro(self, email, senha, nome, sobrenome, is_admin=False):
        logger.debug('Inserindo cadastro do usuário')
        self.insert_login(email, senha, is_admin)
        self.insert_dados(nome, sobrenome)

    def insert_dados(self, nome, sobrenome):
        logger.debug('Inserindo dados do usuário')
        self.nome = nome
        self.sobrenome = sobrenome

    def insert_login(self, email, senha, is_admin=False):
        logger.debug('Inserindo login')
        self.email = email
        self.senha = generate_password_hash(senha)
        self.is_admin = is_admin

    def login(self, senha):
        logger.debug('Verificando senha')
        return check_password_hash(self.senha, senha)

    def generate_token(self):
        token = create_access_token(identity=self.id)
        refresh_token = create_refresh_token(identity=self.id)
        return {
            'access_token': token,
            'refresh_token': refresh_token
        }

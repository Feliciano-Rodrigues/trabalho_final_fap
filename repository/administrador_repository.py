from entity.administrador import Administrador
from entity.funcionario import Funcionario
from db import db

class AdministradorRepository:

    @staticmethod
    def buscar_por_email(email):
        return Administrador.query.join(Funcionario).filter(Funcionario.email == email).first()

    @staticmethod
    def atualizar(administrador):
        db.session.commit()

    @staticmethod
    def buscar_por_token(token):
        return Administrador.query.join(Funcionario).filter(Funcionario.token_recuperacao_senha == token).first()

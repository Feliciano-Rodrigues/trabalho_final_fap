import jwt
import datetime
from sqlalchemy.exc import IntegrityError
from init_db import db
from entity.administrador import Administrador
from entity.funcionario import Funcionario
from werkzeug.security import check_password_hash, generate_password_hash
import logging

logger = logging.getLogger(__name__)

# Define a chave secreta como uma constante
SECRET_KEY = 'secret_key'

class AdministradorService:
    def __init__(self):
        pass

    def create_administrador(self, id_funcionario, responsabilidade, data_contratacao):
        try:
            new_administrador = Administrador(
                id_funcionario=id_funcionario,
                responsabilidade=responsabilidade,
                data_contratacao=data_contratacao
            )
            db.session.add(new_administrador)
            db.session.commit()
            return new_administrador.to_dict()
        except IntegrityError as e:
            db.session.rollback()
            raise ValueError(f"Erro ao criar administrador: {str(e)}")

    def get_all_administradores(self):
        administradores = Administrador.query.all()
        return [admin.to_dict() for admin in administradores]

    def get_administrador_by_id(self, id_administrador):
        administrador = Administrador.query.get(id_administrador)
        if administrador:
            return administrador.to_dict()
        return None

    def update_administrador(self, id_administrador, **kwargs):
        administrador = Administrador.query.get(id_administrador)
        if not administrador:
            raise ValueError("Administrador não encontrado.")
        
        for key, value in kwargs.items():
            if hasattr(administrador, key):
                setattr(administrador, key, value)
        
        db.session.commit()
        return administrador.to_dict()

    def delete_administrador(self, id_administrador):
        administrador = Administrador.query.get(id_administrador)
        if not administrador:
            return False
        
        db.session.delete(administrador)
        db.session.commit()
        return True

    @staticmethod
    def login(email, senha):
        administrador = db.session.query(Administrador).join(Funcionario).filter(Funcionario.email == email).first()
        if administrador and check_password_hash(administrador.funcionario.senha, senha):
            return administrador
        return None

    @staticmethod
    def gerar_token(administrador):
        payload = {
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1),
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'sub': str(administrador.id_funcionario)  # Convertendo para string
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        logger.info("Token gerado: %s", token)
        logger.info("Payload do token gerado: %s", payload)
        return token

    @staticmethod
    def buscar_por_email(email):
        return db.session.query(Administrador).join(Funcionario).filter(Funcionario.email == email).first()

    @staticmethod
    def gerar_token_recuperacao(administrador):
        payload = {
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
            'iat': datetime.datetime.now(datetime.timezone.utc),
            'sub': str(administrador.id_funcionario)  # Convertendo para string
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        logger.info("Token de recuperação gerado: %s", token)
        logger.info("Payload do token de recuperação gerado: %s", payload)
        return token

    @staticmethod
    def atualizar_senha(token, nova_senha):
        try:
            logger.info("Decodificando token: %s", token)
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            logger.info("Token decodificado com sucesso: %s", payload)

            administrador = db.session.query(Administrador).get(payload['sub'])
            if administrador:
                administrador.funcionario.senha = generate_password_hash(nova_senha, method='pbkdf2:sha256', salt_length=8)
                db.session.commit()
                return administrador
            return None
        except jwt.ExpiredSignatureError:
            logger.error("Token expirado")
            return None
        except jwt.InvalidTokenError as e:
            logger.error("Token inválido: %s", str(e))
            return None

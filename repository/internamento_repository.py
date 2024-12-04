from entity.internamento import Internamento
from init_db import db

class InternamentoRepository:

    @staticmethod
    def criar_internamento(internamento):
        db.session.add(internamento)
        db.session.commit()
        return internamento

    @staticmethod
    def obter_internamento(id_internamento):
        return Internamento.query.get(id_internamento)

    @staticmethod
    def atualizar_internamento(internamento):
        db.session.commit()
        return internamento

    @staticmethod
    def deletar_internamento(id_internamento):
        internamento = Internamento.query.get(id_internamento)
        if internamento:
            db.session.delete(internamento)
            db.session.commit()
            return True
        return False

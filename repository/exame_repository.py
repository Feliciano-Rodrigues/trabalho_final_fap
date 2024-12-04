from entity.exame import Exame
from init_db import db

class ExameRepository:

    @staticmethod
    def criar_exame(exame):
        db.session.add(exame)
        db.session.commit()
        return exame

    @staticmethod
    def obter_exame(id_exame):
        return Exame.query.get(id_exame)

    @staticmethod
    def atualizar_exame(exame):
        db.session.commit()
        return exame

    @staticmethod
    def deletar_exame(id_exame):
        exame = Exame.query.get(id_exame)
        if exame:
            db.session.delete(exame)
            db.session.commit()
            return True
        return False

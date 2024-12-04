from entity.cirurgia import Cirurgia
from init_db import db

class CirurgiaRepository:

    @staticmethod
    def criar_cirurgia(cirurgia):
        db.session.add(cirurgia)
        db.session.commit()
        return cirurgia

    @staticmethod
    def obter_cirurgia(id_cirurgia):
        return Cirurgia.query.get(id_cirurgia)

    @staticmethod
    def atualizar_cirurgia(cirurgia):
        db.session.commit()
        return cirurgia

    @staticmethod
    def deletar_cirurgia(id_cirurgia):
        cirurgia = Cirurgia.query.get(id_cirurgia)
        if cirurgia:
            db.session.delete(cirurgia)
            db.session.commit()
            return True
        return False

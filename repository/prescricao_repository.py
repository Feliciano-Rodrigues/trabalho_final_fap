from entity.prescricao import Prescricao
from init_db import db

class PrescricaoRepository:

    @staticmethod
    def criar_prescricao(prescricao):
        db.session.add(prescricao)
        db.session.commit()
        return prescricao

    @staticmethod
    def obter_prescricao(id_prescricao):
        return Prescricao.query.get(id_prescricao)

    @staticmethod
    def atualizar_prescricao(prescricao):
        db.session.commit()
        return prescricao

    @staticmethod
    def deletar_prescricao(id_prescricao):
        prescricao = Prescricao.query.get(id_prescricao)
        if prescricao:
            db.session.delete(prescricao)
            db.session.commit()
            return True
        return False

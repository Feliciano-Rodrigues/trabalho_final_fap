from entity.medicamento import Medicamento
from init_db import db

class MedicamentoRepository:

    @staticmethod
    def criar_medicamento(medicamento):
        db.session.add(medicamento)
        db.session.commit()
        return medicamento

    @staticmethod
    def obter_medicamento(id_medicamento):
        return Medicamento.query.get(id_medicamento)

    @staticmethod
    def atualizar_medicamento(medicamento):
        db.session.commit()
        return medicamento

    @staticmethod
    def deletar_medicamento(id_medicamento):
        medicamento = Medicamento.query.get(id_medicamento)
        if medicamento:
            db.session.delete(medicamento)
            db.session.commit()
            return True
        return False

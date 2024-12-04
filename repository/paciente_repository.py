from entity.paciente import Paciente
from init_db import db

class PacienteRepository:

    @staticmethod
    def criar_paciente(paciente):
        db.session.add(paciente)
        db.session.commit()
        return paciente

    @staticmethod
    def obter_paciente(id_paciente):
        return Paciente.query.get(id_paciente)

    @staticmethod
    def atualizar_paciente(paciente):
        db.session.commit()
        return paciente

    @staticmethod
    def deletar_paciente(id_paciente):
        paciente = Paciente.query.get(id_paciente)
        if paciente:
            db.session.delete(paciente)
            db.session.commit()
            return True
        return False

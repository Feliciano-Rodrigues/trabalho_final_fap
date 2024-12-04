from entity.consulta import Consulta
from init_db import db

class ConsultaRepository:

    @staticmethod
    def criar_consulta(consulta):
        db.session.add(consulta)
        db.session.commit()
        return consulta

    @staticmethod
    def obter_consulta(id_consulta):
        return Consulta.query.get(id_consulta)

    @staticmethod
    def atualizar_consulta(consulta):
        db.session.commit()
        return consulta

    @staticmethod
    def deletar_consulta(id_consulta):
        consulta = Consulta.query.get(id_consulta)
        if consulta:
            db.session.delete(consulta)
            db.session.commit()
            return True
        return False

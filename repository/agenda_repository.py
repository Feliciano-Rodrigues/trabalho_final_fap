from entity.agenda import Agenda
from init_db import db

class AgendaRepository:

    @staticmethod
    def criar_agenda(agenda):
        db.session.add(agenda)
        db.session.commit()
        return agenda

    @staticmethod
    def obter_agenda(id_agenda):
        return Agenda.query.get(id_agenda)

    @staticmethod
    def atualizar_agenda(agenda):
        db.session.commit()
        return agenda

    @staticmethod
    def deletar_agenda(id_agenda):
        agenda = Agenda.query.get(id_agenda)
        if agenda:
            db.session.delete(agenda)
            db.session.commit()
            return True
        return False

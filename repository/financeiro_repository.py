from entity.financeiro import Financeiro
from init_db import db

class FinanceiroRepository:

    @staticmethod
    def criar_financeiro(financeiro):
        db.session.add(financeiro)
        db.session.commit()
        return financeiro

    @staticmethod
    def obter_financeiro(id_financeiro):
        return Financeiro.query.get(id_financeiro)

    @staticmethod
    def atualizar_financeiro(financeiro):
        db.session.commit()
        return financeiro

    @staticmethod
    def deletar_financeiro(id_financeiro):
        financeiro = Financeiro.query.get(id_financeiro)
        if financeiro:
            db.session.delete(financeiro)
            db.session.commit()
            return True
        return False

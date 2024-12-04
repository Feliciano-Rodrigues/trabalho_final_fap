from entity.auxiliar_veterinario import AuxiliarVeterinario
from init_db import db

class AuxiliarVeterinarioRepository:

    @staticmethod
    def criar_auxiliar_veterinario(auxiliar_veterinario):
        db.session.add(auxiliar_veterinario)
        db.session.commit()
        return auxiliar_veterinario

    @staticmethod
    def obter_auxiliar_veterinario(id_funcionario):
        return AuxiliarVeterinario.query.get(id_funcionario)

    @staticmethod
    def atualizar_auxiliar_veterinario(auxiliar_veterinario):
        db.session.commit()
        return auxiliar_veterinario

    @staticmethod
    def deletar_auxiliar_veterinario(id_funcionario):
        auxiliar_veterinario = AuxiliarVeterinario.query.get(id_funcionario)
        if auxiliar_veterinario:
            db.session.delete(auxiliar_veterinario)
            db.session.commit()
            return True
        return False

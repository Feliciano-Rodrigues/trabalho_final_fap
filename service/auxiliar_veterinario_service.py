from werkzeug.security import generate_password_hash
from init_db import db
from entity.auxiliar_veterinario import AuxiliarVeterinario

class AuxiliarVeterinarioService:
    @staticmethod
    def add_auxiliar_veterinario(data):
        try:
            auxiliar_veterinario = AuxiliarVeterinario(
                nome=data['nome'],
                id_veterinario=data['id_veterinario'],
                id_funcionario=data['id_funcionario'],
                certificacao=data['certificacao'],
                data_contratacao=data['data_contratacao']
            )
            db.session.add(auxiliar_veterinario)
            db.session.commit()
            return auxiliar_veterinario.to_dict()
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Erro ao adicionar auxiliar veterinário: {str(e)}")

    @staticmethod
    def obter_auxiliar_veterinario(id_funcionario):
        auxiliar_veterinario = AuxiliarVeterinario.query.get(id_funcionario)
        if auxiliar_veterinario:
            return auxiliar_veterinario.to_dict()
        return None

    @staticmethod
    def atualizar_auxiliar_veterinario(id_funcionario, data):
        auxiliar_veterinario = AuxiliarVeterinario.query.get(id_funcionario)
        if auxiliar_veterinario:
            auxiliar_veterinario.nome = data.get('nome', auxiliar_veterinario.nome)
            auxiliar_veterinario.id_veterinario = data.get('id_veterinario', auxiliar_veterinario.id_veterinario)
            auxiliar_veterinario.certificacao = data.get('certificacao', auxiliar_veterinario.certificacao)
            auxiliar_veterinario.data_contratacao = data.get('data_contratacao', auxiliar_veterinario.data_contratacao)
            db.session.commit()
            return auxiliar_veterinario.to_dict()
        return None

    @staticmethod
    def deletar_auxiliar_veterinario(id_funcionario):
        auxiliar_veterinario = AuxiliarVeterinario.query.get(id_funcionario)
        if auxiliar_veterinario:
            db.session.delete(auxiliar_veterinario)
            db.session.commit()
            return True
        return False

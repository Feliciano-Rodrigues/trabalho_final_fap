from sqlalchemy.exc import IntegrityError
from entity.paciente import Paciente  # Atualizado para importar Paciente
from init_db import db  # Corrigida a importação

class PacienteService:
    
    # Método para obter todos os pacientes
    def get_all_pacientes(self):
        try:
            pacientes = Paciente.query.all()
            return [paciente.to_dict() for paciente in pacientes]
        except Exception as e:
            return {"message": "Erro ao buscar pacientes", "error": str(e)}
    
    # Método para buscar um paciente pelo ID
    def get_paciente_by_id(self, id_paciente):
        try:
            paciente = Paciente.query.get(id_paciente)
            if paciente:
                return paciente.to_dict()
            return {"message": "Paciente não encontrado"}
        except Exception as e:
            return {"message": "Erro ao buscar paciente", "error": str(e)}

    # Método para criar um novo paciente
    def create_paciente(self, data):
        try:
            # Criar um novo objeto Paciente com os dados fornecidos
            novo_paciente = Paciente(**data)
            db.session.add(novo_paciente)
            db.session.commit()
            return {"id": novo_paciente.id_paciente, "message": "Paciente criado com sucesso"}
        except IntegrityError as e:
            db.session.rollback()
            return {"message": "Erro ao salvar paciente", "error": str(e)}
        except Exception as e:
            db.session.rollback()
            return {"message": "Erro inesperado", "error": str(e)}

    # Método para atualizar os dados de um paciente
    def update_paciente(self, id_paciente, data):
        try:
            # Buscar o paciente existente
            paciente = Paciente.query.get(id_paciente)
            if not paciente:
                return {"message": "Paciente não encontrado"}
            
            # Atualizar os campos do paciente
            paciente.nome = data.get('nome', paciente.nome)
            paciente.id_cliente = data.get('id_cliente', paciente.id_cliente)
            
            db.session.commit()
            return paciente.to_dict()
        except Exception as e:
            db.session.rollback()
            return {"message": "Erro ao atualizar paciente", "error": str(e)}

    # Método para deletar um paciente
    def delete_paciente(self, id_paciente):
        try:
            paciente = Paciente.query.get(id_paciente)
            if not paciente:
                return {"message": "Paciente não encontrado"}

            db.session.delete(paciente)
            db.session.commit()
            return {"message": "Paciente deletado com sucesso"}
        except Exception as e:
            db.session.rollback()
            return {"message": "Erro ao deletar paciente", "error": str(e)}

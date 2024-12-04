from repository.consulta_repository import ConsultaRepository
from entity.consulta import Consulta

class ConsultaService:
    @staticmethod
    def add_consulta(data):
        nova_consulta = Consulta(
            id_paciente=data['id_paciente'],  # Corrigi 'id_animal' para 'id_paciente'
            id_veterinario=data['id_veterinario'],
            data=data['data'],  # Corrigi 'data_consulta' para 'data'
            hora=data['hora'],  # Corrigi 'horario' para 'hora'
            diagnostico=data.get('diagnostico')  # Corrigi 'descricao' para 'diagnostico'
        )
        ConsultaRepository.add(nova_consulta)
        return nova_consulta.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_consultas():
        consultas = ConsultaRepository.get_all()
        return [consulta.to_dict() for consulta in consultas]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_consulta(id):
        consulta = ConsultaRepository.get_by_id(id)
        return consulta.to_dict() if consulta else None  # Verificando se a consulta existe
    
    @staticmethod
    def update_consulta(id, data):
        consulta = ConsultaRepository.get_by_id(id)
        
        if not consulta:
            raise ValueError("Consulta não encontrada.")
        
        consulta.id_paciente = data['id_paciente']
        consulta.id_veterinario = data['id_veterinario']
        consulta.data = data['data']
        consulta.hora = data['hora']
        consulta.diagnostico = data.get('diagnostico')
        
        ConsultaRepository.update(consulta)  # Passando a consulta atualizada
        return consulta.to_dict()  # Convertendo a consulta para dicionário
    
    @staticmethod
    def delete_consulta(id):
        consulta = ConsultaRepository.get_by_id(id)
        
        if not consulta:
            raise ValueError("Consulta não encontrada.")
        
        ConsultaRepository.delete(consulta)
        return True

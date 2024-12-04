from repository.cirurgia_repository import CirurgiaRepository
from entity.cirurgia import Cirurgia

class CirurgiaService:
    @staticmethod
    def add_cirurgia(data):
        nova_cirurgia = Cirurgia(
            id_veterinario=data['id_veterinario'],
            id_paciente=data['id_paciente'],
            data_cirurgia=data['data_cirurgia'],
            hora_inicio=data['hora_inicio'],
            hora_fim=data['hora_fim'],
            tipo_cirurgia=data['tipo_cirurgia'],
            observacoes=data.get('observacoes'),
            id_auxiliar=data.get('id_auxiliar'),
            valor_cirurgia=data['valor_cirurgia']
        )
        CirurgiaRepository.add(nova_cirurgia)
        return nova_cirurgia.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_cirurgias():
        cirurgias = CirurgiaRepository.get_all()
        return [cirurgia.to_dict() for cirurgia in cirurgias]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_cirurgia(id):
        cirurgia = CirurgiaRepository.get_by_id(id)
        return cirurgia.to_dict() if cirurgia else None  # Verificando se a cirurgia existe
    
    @staticmethod
    def update_cirurgia(id, data):
        cirurgia = CirurgiaRepository.get_by_id(id)
        
        if not cirurgia:
            raise ValueError("Cirurgia não encontrada.")
        
        cirurgia.id_veterinario = data['id_veterinario']
        cirurgia.id_paciente = data['id_paciente']
        cirurgia.data_cirurgia = data['data_cirurgia']
        cirurgia.hora_inicio = data['hora_inicio']
        cirurgia.hora_fim = data['hora_fim']
        cirurgia.tipo_cirurgia = data['tipo_cirurgia']
        cirurgia.observacoes = data.get('observacoes')
        cirurgia.id_auxiliar = data.get('id_auxiliar')
        cirurgia.valor_cirurgia = data['valor_cirurgia']
        
        CirurgiaRepository.update(cirurgia)  # Passando a cirurgia atualizada
        return cirurgia.to_dict()  # Convertendo a cirurgia para dicionário
    
    @staticmethod
    def delete_cirurgia(id):
        cirurgia = CirurgiaRepository.get_by_id(id)
        
        if not cirurgia:
            raise ValueError("Cirurgia não encontrada.")
        
        CirurgiaRepository.delete(cirurgia)
        return True

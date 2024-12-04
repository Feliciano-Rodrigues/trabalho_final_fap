from repository.internamento_repository import InternamentoRepository
from entity.internamento import Internamento

class InternamentoService:
    @staticmethod
    def add_internamento(data):
        novo_internamento = Internamento(
            id_paciente=data['id_paciente'],  # Corrigi 'id_animal' para 'id_paciente'
            data_internacao=data['data_internacao'],  # Corrigi 'data_entrada' para 'data_internacao'
            data_alta=data.get('data_alta'),  # Corrigi 'data_saida' para 'data_alta'
            motivo=data['motivo'],
            observacoes=data.get('observacoes'),
            id_veterinario=data['id_veterinario']  # Corrigi 'id_veterinario_responsavel' para 'id_veterinario'
        )
        InternamentoRepository.add(novo_internamento)
        return novo_internamento.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_internamentos():
        internamentos = InternamentoRepository.get_all()
        return [internamento.to_dict() for internamento in internamentos]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_internamento(id):
        internamento = InternamentoRepository.get_by_id(id)
        return internamento.to_dict() if internamento else None  # Verificando se o internamento existe
    
    @staticmethod
    def update_internamento(id, data):
        internamento = InternamentoRepository.get_by_id(id)
        
        if not internamento:
            raise ValueError("Internamento não encontrado.")
        
        internamento.id_paciente = data['id_paciente']
        internamento.data_internacao = data['data_internacao']
        internamento.data_alta = data.get('data_alta')
        internamento.motivo = data['motivo']
        internamento.observacoes = data.get('observacoes')
        internamento.id_veterinario = data['id_veterinario']
        
        InternamentoRepository.update(internamento)  # Passando o internamento atualizado
        return internamento.to_dict()  # Convertendo o internamento para dicionário
    
    @staticmethod
    def delete_internamento(id):
        internamento = InternamentoRepository.get_by_id(id)
        
        if not internamento:
            raise ValueError("Internamento não encontrado.")
        
        InternamentoRepository.delete(internamento)
        return True

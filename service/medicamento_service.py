from repository.medicamento_repository import MedicamentoRepository
from entity.medicamento import Medicamento

class MedicamentoService:
    @staticmethod
    def add_medicamento(data):
        novo_medicamento = Medicamento(
            nome=data['nome'],
            quantidade_estoque=data['quantidade_estoque'],
            validade=data['validade'],
            cnpj_fornecedor=data['cnpj_fornecedor'],  # Corrigido para minúsculas
            valor_medicamento=data['valor_medicamento']
        )
        MedicamentoRepository.add(novo_medicamento)
        return novo_medicamento.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_medicamentos():
        medicamentos = MedicamentoRepository.get_all()
        return [medicamento.to_dict() for medicamento in medicamentos]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_medicamento(id):
        medicamento = MedicamentoRepository.get_by_id(id)
        return medicamento.to_dict() if medicamento else None  # Verificando se o medicamento existe
    
    @staticmethod
    def update_medicamento(id, data):
        medicamento = MedicamentoRepository.get_by_id(id)
        
        if not medicamento:
            raise ValueError("Medicamento não encontrado.")
        
        medicamento.nome = data['nome']
        medicamento.quantidade_estoque = data['quantidade_estoque']
        medicamento.validade = data['validade']
        medicamento.cnpj_fornecedor = data['cnpj_fornecedor']  # Corrigido para minúsculas
        medicamento.valor_medicamento = data['valor_medicamento']
        
        MedicamentoRepository.update(medicamento)  # Passando o medicamento atualizado
        return medicamento.to_dict()  # Convertendo o medicamento para dicionário
    
    @staticmethod
    def delete_medicamento(id):
        medicamento = MedicamentoRepository.get_by_id(id)
        
        if not medicamento:
            raise ValueError("Medicamento não encontrado.")
        
        MedicamentoRepository.delete(medicamento)
        return True

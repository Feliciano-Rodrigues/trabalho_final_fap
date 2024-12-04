from repository.financeiro_repository import FinanceiroRepository
from entity.financeiro import Financeiro

class FinanceiroService:
    @staticmethod
    def add_financeiro(data):
        novo_financeiro = Financeiro(
            id_consulta=data.get('id_consulta'),
            id_exame=data.get('id_exame'),
            id_internamento=data.get('id_internamento'),
            valor_total=data['valor_total'],
            data_pagamento=data['data_pagamento'],
            forma_pagamento=data['forma_pagamento']
        )
        FinanceiroRepository.add(novo_financeiro)
        return novo_financeiro.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_financeiros():
        financeiros = FinanceiroRepository.get_all()
        return [financeiro.to_dict() for financeiro in financeiros]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_financeiro(id):
        financeiro = FinanceiroRepository.get_by_id(id)
        return financeiro.to_dict() if financeiro else None  # Verificando se o financeiro existe
    
    @staticmethod
    def update_financeiro(id, data):
        financeiro = FinanceiroRepository.get_by_id(id)
        
        if not financeiro:
            raise ValueError("Financeiro não encontrado.")
        
        financeiro.id_consulta = data.get('id_consulta')
        financeiro.id_exame = data.get('id_exame')
        financeiro.id_internamento = data.get('id_internamento')
        financeiro.valor_total = data['valor_total']
        financeiro.data_pagamento = data['data_pagamento']
        financeiro.forma_pagamento = data['forma_pagamento']
        
        FinanceiroRepository.update(financeiro)  # Passando o financeiro atualizado
        return financeiro.to_dict()  # Convertendo o financeiro para dicionário
    
    @staticmethod
    def delete_financeiro(id):
        financeiro = FinanceiroRepository.get_by_id(id)
        
        if not financeiro:
            raise ValueError("Financeiro não encontrado.")
        
        FinanceiroRepository.delete(financeiro)
        return True

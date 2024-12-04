from repository.exame_repository import ExameRepository
from entity.exame import Exame

class ExameService:
    @staticmethod
    def add_exame(data):
        novo_exame = Exame(
            id_consulta=data['id_consulta'],
            tipo_exame=data['tipo_exame'],
            data_exame=data['data_exame'],
            resultado=data.get('resultado'),
            valor_exame=data['valor_exame']
        )
        ExameRepository.add(novo_exame)
        return novo_exame.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_exames():
        exames = ExameRepository.get_all()
        return [exame.to_dict() for exame in exames]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_exame(id):
        exame = ExameRepository.get_by_id(id)
        return exame.to_dict() if exame else None  # Verificando se o exame existe
    
    @staticmethod
    def update_exame(id, data):
        exame = ExameRepository.get_by_id(id)
        
        if not exame:
            raise ValueError("Exame não encontrado.")
        
        exame.id_consulta = data['id_consulta']
        exame.tipo_exame = data['tipo_exame']
        exame.data_exame = data['data_exame']
        exame.resultado = data.get('resultado')
        exame.valor_exame = data['valor_exame']
        
        ExameRepository.update(exame)  # Passando o exame atualizado
        return exame.to_dict()  # Convertendo o exame para dicionário
    
    @staticmethod
    def delete_exame(id):
        exame = ExameRepository.get_by_id(id)
        
        if not exame:
            raise ValueError("Exame não encontrado.")
        
        ExameRepository.delete(exame)
        return True

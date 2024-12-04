from repository.prescricao_repository import PrescricaoRepository
from entity.prescricao import Prescricao

class PrescricaoService:
    @staticmethod
    def add_prescricao(data):
        nova_prescricao = Prescricao(
            id_consulta=data['id_consulta'],
            id_medicamento=data['id_medicamento'],
            dosagem=data['dosagem'],
            frequencia=data['frequencia'],
            duracao=data['duracao']
        )
        PrescricaoRepository.add(nova_prescricao)
        return nova_prescricao.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_prescricoes():
        prescricoes = PrescricaoRepository.get_all()
        return [prescricao.to_dict() for prescricao in prescricoes]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_prescricao(id):
        prescricao = PrescricaoRepository.get_by_id(id)
        return prescricao.to_dict() if prescricao else None  # Verificando se a prescrição existe
    
    @staticmethod
    def update_prescricao(id, data):
        prescricao = PrescricaoRepository.get_by_id(id)
        
        if not prescricao:
            raise ValueError("Prescrição não encontrada.")
        
        prescricao.id_consulta = data['id_consulta']
        prescricao.id_medicamento = data['id_medicamento']
        prescricao.dosagem = data['dosagem']
        prescricao.frequencia = data['frequencia']
        prescricao.duracao = data['duracao']
        
        PrescricaoRepository.update(prescricao)  # Passando a prescrição atualizada
        return prescricao.to_dict()  # Convertendo a prescrição para dicionário
    
    @staticmethod
    def delete_prescricao(id):
        prescricao = PrescricaoRepository.get_by_id(id)
        
        if not prescricao:
            raise ValueError("Prescrição não encontrada.")
        
        PrescricaoRepository.delete(prescricao)
        return True

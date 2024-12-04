from repository.veterinario_repository import VeterinarioRepository
from entity.veterinario import Veterinario

class VeterinarioService:
    @staticmethod
    def add_veterinario(data):
        novo_veterinario = Veterinario(
            id_funcionario=data['id_funcionario'],
            crmv=data['crmv'],  # Corrigi 'CRM' para 'crmv'
            especialidade=data.get('especialidade'),
            data_contratacao=data['data_contratacao']
        )
        VeterinarioRepository.add(novo_veterinario)
        return novo_veterinario.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_veterinarios():
        veterinarios = VeterinarioRepository.get_all()
        return [veterinario.to_dict() for veterinario in veterinarios]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_veterinario(id):
        veterinario = VeterinarioRepository.get_by_id(id)
        return veterinario.to_dict() if veterinario else None  # Verificando se o veterinário existe
    
    @staticmethod
    def update_veterinario(id, data):
        veterinario = VeterinarioRepository.get_by_id(id)
        
        if not veterinario:
            raise ValueError("Veterinário não encontrado.")
        
        veterinario.crmv = data['crmv']  # Corrigi 'CRM' para 'crmv'
        veterinario.especialidade = data.get('especialidade')
        veterinario.data_contratacao = data['data_contratacao']
        
        VeterinarioRepository.update(veterinario)  # Passando o veterinário atualizado
        return veterinario.to_dict()  # Convertendo o veterinário para dicionário
    
    @staticmethod
    def delete_veterinario(id):
        veterinario = VeterinarioRepository.get_by_id(id)
        
        if not veterinario:
            raise ValueError("Veterinário não encontrado.")
        
        VeterinarioRepository.delete(veterinario)
        return True

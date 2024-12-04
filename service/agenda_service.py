from repository.agenda_repository import AgendaRepository
from entity.agenda import Agenda

class AgendaService:
    @staticmethod
    def add_agenda(data):
        nova_agenda = Agenda(
            id_consulta=data.get('id_consulta'),
            id_cirurgia=data.get('id_cirurgia'),
            id_veterinario=data['id_veterinario'],
            disponibilidade=data['disponibilidade'],
            tipo=data['tipo'],
            data=data['data'],
            hora=data['hora']
        )
        AgendaRepository.add(nova_agenda)
        return nova_agenda.to_dict()  # Adicionando conversão para dicionário
    
    @staticmethod
    def get_agendas():
        agendas = AgendaRepository.get_all()
        return [agenda.to_dict() for agenda in agendas]  # Convertendo cada item para dicionário
    
    @staticmethod
    def get_agenda(id):
        agenda = AgendaRepository.get_by_id(id)
        return agenda.to_dict() if agenda else None  # Verificando se a agenda existe
    
    @staticmethod
    def update_agenda(id, data):
        agenda = AgendaRepository.get_by_id(id)
        
        if not agenda:
            raise ValueError("Agenda não encontrada.")
        
        agenda.id_consulta = data.get('id_consulta')
        agenda.id_cirurgia = data.get('id_cirurgia')
        agenda.id_veterinario = data['id_veterinario']
        agenda.disponibilidade = data['disponibilidade']
        agenda.tipo = data['tipo']
        agenda.data = data['data']
        agenda.hora = data['hora']
        
        AgendaRepository.update(agenda)  # Passando a agenda atualizada
        return agenda.to_dict()  # Convertendo a agenda para dicionário
    
    @staticmethod
    def delete_agenda(id):
        agenda = AgendaRepository.get_by_id(id)
        
        if not agenda:
            raise ValueError("Agenda não encontrada.")
        
        AgendaRepository.delete(agenda)
        return True

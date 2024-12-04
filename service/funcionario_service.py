from repository.funcionario_repository import FuncionarioRepository
from entity.funcionario import Funcionario

class FuncionarioService:
    def __init__(self):
        self.funcionario_repository = FuncionarioRepository()

    def get_all_funcionarios(self):
        return self.funcionario_repository.get_all()  # Retorna instâncias de Funcionario

    def get_funcionario_by_id(self, id):
        return self.funcionario_repository.get_by_id(id)  # Retorna instância de Funcionario

    def create_funcionario(self, data):
        novo_funcionario = Funcionario(
            nome=data['nome'],
            cpf=data['cpf'],
            email=data['email'],
            telefone=data.get('telefone'),
            endereco=data.get('endereco'),
            data_nascimento=data['data_nascimento'],
            senha=data['senha']
        )
        self.funcionario_repository.add(novo_funcionario)
        return novo_funcionario  # Retorna instância de Funcionario

    def update_funcionario(self, id, data):
        funcionario = self.funcionario_repository.get_by_id(id)
        
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        
        funcionario.nome = data.get('nome', funcionario.nome)
        funcionario.cpf = data.get('cpf', funcionario.cpf)
        funcionario.email = data.get('email', funcionario.email)
        funcionario.telefone = data.get('telefone', funcionario.telefone)
        funcionario.endereco = data.get('endereco', funcionario.endereco)
        funcionario.data_nascimento = data.get('data_nascimento', funcionario.data_nascimento)
        funcionario.senha = data.get('senha', funcionario.senha)
        
        self.funcionario_repository.update(funcionario)
        return funcionario  # Retorna instância de Funcionario

    def delete_funcionario(self, id):
        funcionario = self.funcionario_repository.get_by_id(id)
        
        if not funcionario:
            raise ValueError("Funcionário não encontrado.")
        
        self.funcionario_repository.delete(funcionario)
        return True

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from init_db import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id_funcionario = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    telefone = Column(String(20), nullable=False)
    endereco = Column(String(255), nullable=False)
    data_nascimento = Column(String(50), nullable=False)
    senha = Column(String(255), nullable=False)

    administrador = relationship('Administrador', uselist=False, back_populates='funcionario')
    veterinario = relationship('Veterinario', uselist=False, back_populates='funcionario')
    auxiliar_veterinario = relationship('AuxiliarVeterinario', uselist=False, back_populates='funcionario')

    def to_dict(self):
        return {
            'id_funcionario': self.id_funcionario,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'data_nascimento': self.data_nascimento,
            'senha': self.senha
        }

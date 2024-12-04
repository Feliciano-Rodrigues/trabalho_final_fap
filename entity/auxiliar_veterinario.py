from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class AuxiliarVeterinario(db.Model):
    __tablename__ = 'auxiliares_veterinarios'
    id_auxiliar = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    id_veterinario = Column(Integer, ForeignKey('veterinarios.id_funcionario'), nullable=False)
    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'), nullable=False)
    certificacao = Column(String(100), nullable=False)
    data_contratacao = Column(Date, nullable=False)

    # Relacionamento com Funcionario
    funcionario = relationship('Funcionario', back_populates='auxiliar_veterinario')
    # Relacionamento com Cirurgia
    cirurgias = relationship('Cirurgia', back_populates='auxiliar', lazy='dynamic')
    # Relacionamento com Veterinário
    veterinario = relationship('Veterinario', back_populates='auxiliares')

    def to_dict(self):
        return {
            'id_auxiliar': self.id_auxiliar,
            'nome': self.nome,
            'id_veterinario': self.id_veterinario,
            'id_funcionario': self.id_funcionario,
            'certificacao': self.certificacao,
            'data_contratacao': self.data_contratacao
        }

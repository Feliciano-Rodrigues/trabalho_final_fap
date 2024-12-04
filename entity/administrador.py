from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Administrador(db.Model):
    __tablename__ = 'administradores'

    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'), primary_key=True)
    responsabilidade = Column(String(255), nullable=True)
    data_contratacao = Column(Date, nullable=True)

    funcionario = relationship('Funcionario', back_populates='administrador')

    def to_dict(self):
        return {
            'id_funcionario': self.id_funcionario,
            'responsabilidade': self.responsabilidade,
            'data_contratacao': str(self.data_contratacao)
        }

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id_paciente = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    raca = Column(String(50), nullable=False)
    idade = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=False)

    cliente = relationship('Cliente', back_populates='pacientes')
    consultas= relationship('Consulta', back_populates='paciente')
   # Relacionamento com Cirurgia (especificando a chave estrangeira correta)
    cirurgias = relationship('Cirurgia', back_populates='paciente', foreign_keys='Cirurgia.id_paciente')
    # Relacionamento com Internamento
    internamentos = relationship('Internamento', back_populates='paciente')
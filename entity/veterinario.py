from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Veterinario(db.Model):
    __tablename__ = 'veterinarios'

    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'), primary_key=True)
    crm = Column(String(50), nullable=False)
    especialidade = Column(String(50), nullable=False)
    data_contratacao = Column(String(50), nullable=False)

    funcionario = relationship('Funcionario', back_populates='veterinario')
    consultas = relationship('Consulta', back_populates='veterinario')
    cirurgias = relationship('Cirurgia', back_populates='veterinario')
    internamentos = relationship('Internamento', back_populates='veterinario')
    agendas = relationship('Agenda', back_populates='veterinario')
    auxiliares = relationship('AuxiliarVeterinario', back_populates='veterinario')
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from init_db import db

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id_consulta = Column(Integer, primary_key=True)
    id_veterinario = Column(Integer, ForeignKey('veterinarios.id_funcionario'))
    id_paciente = Column(Integer, ForeignKey('pacientes.id_paciente'))
    data = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    hora = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    diagnostico = Column(String(255), nullable=False)  # Defina um comprimento para VARCHAR
    valor_consulta = Column(Float)

    prescricoes = relationship('Prescricao', back_populates='consulta')
    paciente = relationship('Paciente', back_populates='consultas')
    veterinario = relationship('Veterinario', back_populates='consultas')
    agendas = relationship('Agenda', back_populates='consulta')
    exames = relationship('Exame', back_populates='consulta')
    financeiros = relationship('Financeiro', back_populates='consulta')

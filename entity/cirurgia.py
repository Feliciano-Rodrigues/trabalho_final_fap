from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from init_db import db

class Cirurgia(db.Model):
    __tablename__ = 'cirurgias'

    id_cirurgia = Column(Integer, primary_key=True)
    id_veterinario = Column(Integer, ForeignKey('veterinarios.id_funcionario'))
    id_paciente = Column(Integer, ForeignKey('pacientes.id_paciente'))
    data_cirurgia = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    hora_inicio = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    hora_fim = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    tipo_cirurgia = Column(String(255), nullable=False)  # Defina um comprimento para VARCHAR
    observacoes = Column(String(255))  # Defina um comprimento para VARCHAR
    id_auxiliar = Column(Integer, ForeignKey('auxiliares_veterinarios.id_funcionario'))
    valor_cirurgia = Column(Float)

    veterinario = relationship('Veterinario', back_populates='cirurgias')
    paciente = relationship('Paciente', back_populates='cirurgias')
    auxiliar = relationship('AuxiliarVeterinario', back_populates='cirurgias')
    agendas = relationship('Agenda', back_populates='cirurgia')

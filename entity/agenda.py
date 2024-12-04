from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Agenda(db.Model):
    __tablename__ = 'agendas'

    id_agenda = Column(Integer, primary_key=True)
    id_consulta = Column(Integer, ForeignKey('consultas.id_consulta'))
    id_cirurgia = Column(Integer, ForeignKey('cirurgias.id_cirurgia'))
    id_veterinario = Column(Integer, ForeignKey('veterinarios.id_funcionario'))
    disponibilidade = Column(Boolean, nullable=False)
    tipo = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    data = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    hora = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR

    consulta = relationship('Consulta', back_populates='agendas')
    cirurgia = relationship('Cirurgia', back_populates='agendas')
    veterinario = relationship('Veterinario', back_populates='agendas')

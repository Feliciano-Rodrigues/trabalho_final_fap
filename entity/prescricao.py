from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Prescricao(db.Model):
    __tablename__ = 'prescricoes'

    id_prescricao = Column(Integer, primary_key=True)
    dosagem = Column(String(50), nullable=False)
    frequencia = Column(String(50), nullable=False)
    hora_medicacao = Column(String(50), nullable=False)

    consulta_id = Column(Integer, ForeignKey('consultas.id_consulta'), nullable=False)  # Deve referenciar consultas
    id_medicamento = Column(Integer, ForeignKey('medicamentos.id_medicamento'))

    consulta = relationship('Consulta', back_populates='prescricoes', foreign_keys=[consulta_id])
    medicamento = relationship('Medicamento', back_populates='prescricoes')
    internamentos = relationship('Internamento', back_populates='prescricao')

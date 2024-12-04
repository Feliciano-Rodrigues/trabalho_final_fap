from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from init_db import db

class Internamento(db.Model):
    __tablename__ = 'internamentos'

    id_internamento = Column(Integer, primary_key=True)
    data_internacao = Column(Date, nullable=False)
    motivo = Column(String(200), nullable=False)
    data_alta = Column(Date, nullable=True)
    valor_diaria = Column(Float, nullable=False)

    id_paciente = Column(Integer, ForeignKey('pacientes.id_paciente'))
    id_veterinario = Column(Integer, ForeignKey('veterinarios.id_funcionario'))
    id_prescricao = Column(Integer, ForeignKey('prescricoes.id_prescricao'), nullable=True)

    paciente = relationship('Paciente', back_populates='internamentos')
    veterinario = relationship('Veterinario', back_populates='internamentos')
    prescricao = relationship('Prescricao', back_populates='internamentos')
    financeiros = relationship('Financeiro', back_populates='internamento')
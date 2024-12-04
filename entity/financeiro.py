from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from init_db import db

class Financeiro(db.Model):
    __tablename__ = 'financeiros'

    id_financeiro = Column(Integer, primary_key=True)
    id_consulta = Column(Integer, ForeignKey('consultas.id_consulta'))
    id_exame = Column(Integer, ForeignKey('exames.id_exame'))
    id_internamento = Column(Integer, ForeignKey('internamentos.id_internamento'))
    valor_total = Column(Float)
    data_pagamento = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    forma_pagamento = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR

    consulta = relationship('Consulta', back_populates='financeiros')
    exame = relationship('Exame', back_populates='financeiros')
    internamento = relationship('Internamento', back_populates='financeiros')

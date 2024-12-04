from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from init_db import db

class Exame(db.Model):
    __tablename__ = 'exames'

    id_exame = Column(Integer, primary_key=True)
    id_consulta = Column(Integer, ForeignKey('consultas.id_consulta'))
    tipo_exame = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    data_exame = Column(String(50), nullable=False)  # Defina um comprimento para VARCHAR
    resultado = Column(String(255), nullable=False)  # Defina um comprimento para VARCHAR
    valor_exame = Column(Float)

    consulta = relationship('Consulta', back_populates='exames')
    financeiros = relationship('Financeiro', back_populates='exame')

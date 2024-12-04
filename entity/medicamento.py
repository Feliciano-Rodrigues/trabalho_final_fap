from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from init_db import db

class Medicamento(db.Model):
    __tablename__ = 'medicamentos'

    id_medicamento = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    quantidade_estoque = Column(Integer, nullable=False)
    validade = Column(Date, nullable=False)
    cnpj_fornecedor = Column(String(20), nullable=False)
    valor_medicamento = Column(Float, nullable=False)

    prescricoes = relationship('Prescricao', back_populates='medicamento')

    def to_dict(self):
        return {
            'id_medicamento': self.id_medicamento,
            'nome': self.nome,
            'quantidade_estoque': self.quantidade_estoque,
            'validade': self.validade.isoformat() if self.validade else None,
            'cnpj_fornecedor': self.cnpj_fornecedor,
            'valor_medicamento': self.valor_medicamento
        }

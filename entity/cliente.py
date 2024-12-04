from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from init_db import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefone = Column(String(15), nullable=True)
    endereco = Column(String(200), nullable=True)

    pacientes = relationship('Paciente', back_populates='cliente', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id_cliente': self.id_cliente,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco
        }

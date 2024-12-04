from init_db import db
from entity.funcionario import Funcionario

class FuncionarioRepository:

    def get_all(self):
        return Funcionario.query.all()

    def get_by_id(self, id):
        return Funcionario.query.get(id)

    def create(self, data):
        new_funcionario = Funcionario(**data)
        db.session.add(new_funcionario)
        db.session.commit()
        return new_funcionario

    def update(self, id, data):
        funcionario = Funcionario.query.get(id)
        if funcionario:
            for key, value in data.items():
                setattr(funcionario, key, value)
            db.session.commit()
        return funcionario

    def delete(self, id):
        funcionario = Funcionario.query.get(id)
        if funcionario:
            db.session.delete(funcionario)
            db.session.commit()
            return True
        return False

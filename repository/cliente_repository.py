from init_db import db
from entity.cliente import Cliente

class ClienteRepository:
    def get_all(self):
        return Cliente.query.all()

    def get_by_id(self, id_cliente):
        return Cliente.query.get(id_cliente)

    def create(self, cliente):
        db.session.add(cliente)
        db.session.commit()

    def update(self, cliente):
        db.session.commit()

    def delete(self, cliente):
        db.session.delete(cliente)
        db.session.commit()

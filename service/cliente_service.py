from init_db import db
from entity.cliente import Cliente
from sqlalchemy.exc import IntegrityError

class ClienteService:
    @staticmethod
    def get_all_clientes():
        """Retorna todos os clientes cadastrados."""
        try:
            clientes = Cliente.query.all()
            return [cliente.to_dict() for cliente in clientes]
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_cliente_by_id(cliente_id):
        """Retorna um cliente específico pelo ID."""
        try:
            cliente = Cliente.query.get(cliente_id)
            if cliente:
                return cliente.to_dict()
            return None
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def create_cliente(data):
        """Cria um novo cliente."""
        try:
            new_cliente = Cliente(**data)
            db.session.add(new_cliente)
            db.session.commit()
            return new_cliente.to_dict()
        except IntegrityError as e:
            db.session.rollback()
            return {"error": "Erro de integridade, possivelmente CPF ou e-mail duplicados."}, 400
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def update_cliente(cliente_id, data):
        """Atualiza um cliente existente."""
        try:
            cliente = Cliente.query.get(cliente_id)
            if not cliente:
                return None

            # Atualiza os campos do cliente
            for key, value in data.items():
                setattr(cliente, key, value)

            db.session.commit()
            return cliente.to_dict()
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_cliente(cliente_id):
        """Deleta um cliente existente."""
        try:
            cliente = Cliente.query.get(cliente_id)
            if not cliente:
                return None

            db.session.delete(cliente)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

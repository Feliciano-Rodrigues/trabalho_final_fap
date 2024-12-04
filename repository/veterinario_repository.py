from init_db import db
from entity.veterinario import Veterinario

class VeterinarioRepository:

    def get_all(self):
        return Veterinario.query.all()

    def get_by_id(self, id):
        return Veterinario.query.get(id)

    def create(self, data):
        new_veterinario = Veterinario(**data)
        db.session.add(new_veterinario)
        db.session.commit()
        return new_veterinario

    def update(self, id, data):
        veterinario = Veterinario.query.get(id)
        if veterinario:
            for key, value in data.items():
                setattr(veterinario, key, value)
            db.session.commit()
        return veterinario

    def delete(self, id):
        veterinario = Veterinario.query.get(id)
        if veterinario:
            db.session.delete(veterinario)
            db.session.commit()
            return True
        return False

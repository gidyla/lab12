from my_project.database import db

class GeneralDAO:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.query.all()

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()

    def delete(self, entity_id):
        entity = db.session.query(self.model).get(entity_id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return True
        return False

    def get_by_id(self, entity_id):
        return db.session.query(self.model).get(entity_id)

    def update(self):
        db.session.commit()
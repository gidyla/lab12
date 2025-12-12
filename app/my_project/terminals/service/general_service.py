# my_project/services/general_service.py
class GeneralService:
    def __init__(self, dao, domain_class):
        self.dao = dao
        self.domain_class = domain_class

    def create(self, **kwargs):
        # Create a new instance of the domain class using keyword arguments
        entity = self.domain_class(**kwargs)
        self.dao.add(entity)
        return entity

    def get_all(self):
        return [entity.to_dict() for entity in self.dao.get_all()]

    def get_by_id(self, entity_id):
        return self.dao.get_by_id(entity_id)

    def delete(self, entity_id):
        return self.dao.delete(entity_id)

    def update(self, entity_id, **kwargs):
        entity = self.dao.get_by_id(entity_id)
        if not entity:
            return None  # If the entity doesn't exist, return None

        # Update only the provided fields
        for key, value in kwargs.items():
            if hasattr(entity, key) and value is not None:
                setattr(entity, key, value)

        self.dao.update()
        return entity

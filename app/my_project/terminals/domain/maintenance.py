from my_project.database import db

class Maintenance(db.Model):
    __tablename__ = 'maintenance'

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    maintenance_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(100), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "robot_id": self.robot_id,
            "maintenance_date": self.maintenance_date,
            "description": self.description
        }
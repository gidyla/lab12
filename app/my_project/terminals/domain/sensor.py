from my_project.database import db

class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
            "robot_id": self.robot_id
        }
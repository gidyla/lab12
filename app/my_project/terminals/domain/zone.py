from my_project.database import db

class Zone(db.Model):
    __tablename__ = 'zone'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    area = db.Column(db.Numeric(10, 2), nullable=False)

    robot_zone = db.relationship("RobotZone", backref="zone")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "area": self.area
        }
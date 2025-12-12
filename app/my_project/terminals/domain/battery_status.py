from my_project.database import db

class BatteryStatus(db.Model):
    __tablename__ = 'battery_status'

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    battery_level = db.Column(db.Numeric(10, 2), nullable=False)
    status_time = db.Column(db.Date, nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "robot_id": self.robot_id,
            "battery_level": self.battery_level,
            "status_time": self.status_time
        }
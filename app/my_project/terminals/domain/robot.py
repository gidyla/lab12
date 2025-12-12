# my_project/customer_companies/domain/customer_comp.py
from my_project.database import db

class Robot(db.Model):
    __tablename__ = 'robot'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    battery_status = db.relationship("BatteryStatus", backref="robot")
    incident_report = db.relationship("IncidentReport", backref="robot")
    maintenance = db.relationship("Maintenance", backref="robot")
    robot_control = db.relationship("RobotControl", backref="robot")
    robot_zone = db.relationship("RobotZone", backref="robot")
    sensor = db.relationship("Sensor", backref="robot")

    def to_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "serial_number": self.serial_number,
            "status": self.status,
        }
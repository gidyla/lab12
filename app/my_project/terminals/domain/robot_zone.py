# my_project/terminals/domain/terminal.py
from my_project.database import db

class RobotZone(db.Model):
    __tablename__ = 'robot_zone'

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), nullable=False)
    assignment_time = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "robot_id": self.robot_id,
            "zone_id": self.zone_id,
            "assignment_time": self.assignment_time
        }

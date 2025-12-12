from my_project.database import db

class IncidentReport(db.Model):
    __tablename__ = 'incident_report'

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    report_time = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "robot_id": self.robot_id,
            "description": self.description,
            "report_time": self.report_time
        }
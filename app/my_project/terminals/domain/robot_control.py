from my_project.database import db

class RobotControl(db.Model):
    __tablename__ = 'robot_control'

    id = db.Column(db.Integer, primary_key=True)
    robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    command = db.Column(db.String(50), nullable=False)
    command_time = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "robot_id": self.robot_id,
            "user_id": self.user_id,
            "command": self.command,
            "command_time": self.command_time
        }
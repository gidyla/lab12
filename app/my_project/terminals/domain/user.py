from my_project.database import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)

    robot_control = db.relationship("RobotControl", backref="user")


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }
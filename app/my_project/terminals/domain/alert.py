from my_project.database import db

class Alert(db.Model):
    __tablename__ = 'alert'

    id = db.Column(db.Integer, primary_key=True)
    alert_type = db.Column(db.String(50), nullable=False)
    alert_time = db.Column(db.Date, nullable=False)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "alert_type": self.alert_type,
            "alert_time": self.alert_time,
            "zone_id": self.zone_id
        }
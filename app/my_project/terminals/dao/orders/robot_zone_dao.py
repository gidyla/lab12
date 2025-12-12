from my_project.terminals.dao.general_dao import GeneralDAO
from my_project.database import db

class RobotZoneDAO(GeneralDAO):
    from my_project.terminals.dao.__init__ import RobotZone
    def __init__(self):
        super().__init__(self.RobotZone)

    def get_all_robot_zones(self):
        from my_project.terminals.domain.robot import Robot
        from my_project.terminals.domain.robot_zone import RobotZone
        from my_project.terminals.domain.zone import Zone
        # Join Robot, Zone, and RobotZone tables
        return db.session.query(RobotZone, Robot, Zone).join(Robot, RobotZone.robot).join(Zone, RobotZone.zone).all()
# my_project/customer_companies/service/customer_company_service.py
from my_project.terminals.service.general_service import GeneralService
from my_project.terminals.service.__init__ import RobotZone
from my_project.terminals.service.__init__ import RobotZoneDAO
from my_project.terminals.domain.robot import Robot
from my_project.terminals.domain.zone import Zone


class RobotZoneService(GeneralService):

    def __init__(self):
        super().__init__(RobotZoneDAO(), RobotZone)

    def get_all_robot_zones(self):
        robot_zone_data = self.dao.get_all_robot_zones()
        result = []
        for robot_zone, robot, zone in robot_zone_data:
            result.append({
                "robot": robot.to_dict(),
                "zone": zone.to_dict(),
                "assignment_time": robot_zone.assignment_time
            })
        return result

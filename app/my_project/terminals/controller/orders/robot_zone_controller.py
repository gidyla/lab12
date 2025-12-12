from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import RobotZoneService
from my_project.terminals.controller.utils import handle_error, handle_response

class RobotZoneController(GeneralController):
    def __init__(self):
        super().__init__(RobotZoneService())

    def get_all_robots_and_zones(self):
        robot_zone_assignments = self.service.get_all_robot_zones()
        if robot_zone_assignments:
            return handle_response(robot_zone_assignments, 200)
        else:
            return handle_error("No robot-zone assignments found", 404)
from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import RobotService
from my_project.terminals.controller.utils import handle_error, handle_response

class RobotController(GeneralController):
    def __init__(self):
        super().__init__(RobotService())

    def get_all_robot_controls_with_user(self):
        robot_controls = self.service.dao.get_all()
        result = []
        for robot_control in robot_controls:
            user = robot_control.user
            result.append({
                "robot_control": robot_control.to_dict(),
                "user": user.to_dict()
            })
        if result:
            return handle_response(result, 200)
        else:
            return handle_error("No robot controls found", 404)

    def get_all_robots_with_sensors(self):
        robots = self.service.dao.get_all()  # Get all robots
        result = []
        for robot in robots:
            sensors = robot.sensor  # Get all sensors related to the robot
            result.append({
                "robot": robot.to_dict(),
                "sensors": [sensor.to_dict() for sensor in sensors]  # Convert each sensor to dict
            })

        if result:
            return handle_response(result, 200)
        else:
            return handle_error("No robots found", 404)
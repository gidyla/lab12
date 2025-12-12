from my_project.terminals.controller.general_controller import GeneralController
from my_project.terminals.controller.__init__ import RobotControlService
from my_project.terminals.controller.utils import handle_error, handle_response

class RobotControlController(GeneralController):
    def __init__(self):
        super().__init__(RobotControlService())

    def get_all_robot_controls_with_user(self):
        robot_controls = self.service.get_all_with_user()  # Call the service method
        result = []

        for robot_control in robot_controls:
            user = robot_control.user  # Access the related user
            result.append({
                "robot_control": robot_control.to_dict(),
                "user": user.to_dict()  # Include full user details
            })

        if result:
            return handle_response(result, 200)
        else:
            return handle_error("No robot controls found", 404)

    def get_robot_with_sensors(self, robot_id):
        robot = self.service.dao.get_by_id(robot_id)  # Get the robot by ID
        if robot:
            sensors = robot.sensor  # Get all sensors associated with the robot
            result = {
                "robot": robot.to_dict(),
                "sensors": [sensor.to_dict() for sensor in sensors]  # Convert each sensor to dict
            }
            return handle_response(result, 200)
        else:
            return handle_error("Robot not found", 404)
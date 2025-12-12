from flask import Blueprint
from my_project.terminals.controller.orders.robot_control_controller import RobotControlController

robot_control_bp = Blueprint('robot_control', __name__)
robot_control_controller = RobotControlController()

@robot_control_bp.route('/robot_control', methods=['GET'])
def get_robot_control():
    """
    Get all robot control records
    ---
    tags:
      - Robot Control
    responses:
      200:
        description: List of all robot control records
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  robot_id:
                    type: integer
                  user_id:
                    type: integer
                  command:
                    type: string
                  command_time:
                    type: string
                    format: date
    """
    return robot_control_controller.get_all()

@robot_control_bp.route('/robot_control/<int:robot_control_id>', methods=['GET'])
def get_robot_control_by_id(robot_control_id):
    """
    Get a robot control record by ID
    ---
    tags:
      - Robot Control
    parameters:
      - name: robot_control_id
        in: path
        type: integer
        required: true
        description: ID of the robot control record
    responses:
      200:
        description: Robot control record object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                user_id:
                  type: integer
                command:
                  type: string
                command_time:
                  type: string
                  format: date
      404:
        description: Record not found
    """
    return robot_control_controller.get_by_id(robot_control_id)

@robot_control_bp.route('/robot_control', methods=['POST'])
def add_robot_control():
    """
    Create a new robot control record
    ---
    tags:
      - Robot Control
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              user_id:
                type: integer
              command:
                type: string
              command_time:
                type: string
                format: date
            required:
              - robot_id
              - user_id
              - command
              - command_time
    responses:
      201:
        description: Robot control record created
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                user_id:
                  type: integer
                command:
                  type: string
                command_time:
                  type: string
                  format: date
    """
    return robot_control_controller.create()

@robot_control_bp.route('/robot_control/<int:robot_control_id>', methods=['PATCH'])
def update_robot_control(robot_control_id):
    """
    Update an existing robot control record
    ---
    tags:
      - Robot Control
    parameters:
      - name: robot_control_id
        in: path
        type: integer
        required: true
        description: ID of the robot control record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              user_id:
                type: integer
              command:
                type: string
              command_time:
                type: string
                format: date
    responses:
      200:
        description: Robot control record updated successfully
      404:
        description: Record not found
    """
    return robot_control_controller.update(robot_control_id)

@robot_control_bp.route('/robot_control/<int:robot_control_id>', methods=['DELETE'])
def delete_robot_control(robot_control_id):
    """
    Delete a robot control record
    ---
    tags:
      - Robot Control
    parameters:
      - name: robot_control_id
        in: path
        type: integer
        required: true
        description: ID of the robot control record
    responses:
      204:
        description: Record deleted successfully
      404:
        description: Record not found
    """
    return robot_control_controller.delete(robot_control_id)

@robot_control_bp.route('/robot_control_with_user', methods=['GET'])
def get_all_robot_controls_with_user():
    """
    Get all robot control records including user information
    ---
    tags:
      - Robot Control
    responses:
      200:
        description: List of all robot controls with user details
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  robot_id:
                    type: integer
                  user_id:
                    type: integer
                  username:
                    type: string
                  role:
                    type: string
                  command:
                    type: string
                  command_time:
                    type: string
                    format: date
    """
    return robot_control_controller.get_all_robot_controls_with_user()

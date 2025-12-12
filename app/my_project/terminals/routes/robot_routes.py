from flask import Blueprint
from my_project.terminals.controller.orders.robot_controller import RobotController

robot_bp = Blueprint('robot', __name__)
robot_controller = RobotController()

@robot_bp.route('/robot', methods=['GET'])
def get_robot():
    """
    Get all robots
    ---
    tags:
      - Robot
    responses:
      200:
        description: List of all robots
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  model:
                    type: string
                  serial_number:
                    type: string
                  status:
                    type: string
    """
    return robot_controller.get_all()

@robot_bp.route('/robot/<int:robot_id>', methods=['GET'])
def get_robot_by_id(robot_id):
    """
    Get robot by ID
    ---
    tags:
      - Robot
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
        description: ID of the robot
    responses:
      200:
        description: Robot object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                model:
                  type: string
                serial_number:
                  type: string
                status:
                  type: string
      404:
        description: Robot not found
    """
    return robot_controller.get_by_id(robot_id)

@robot_bp.route('/robot', methods=['POST'])
def add_robot():
    """
    Create a new robot
    ---
    tags:
      - Robot
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              model:
                type: string
              serial_number:
                type: string
              status:
                type: string
            required:
              - model
              - serial_number
              - status
    responses:
      201:
        description: Robot created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                model:
                  type: string
                serial_number:
                  type: string
                status:
                  type: string
    """
    return robot_controller.create()

@robot_bp.route('/robot/<int:robot_id>', methods=['PATCH'])
def update_robot(robot_id):
    """
    Update an existing robot
    ---
    tags:
      - Robot
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
        description: ID of the robot
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              model:
                type: string
              serial_number:
                type: string
              status:
                type: string
    responses:
      200:
        description: Robot updated successfully
      404:
        description: Robot not found
    """
    return robot_controller.update(robot_id)

@robot_bp.route('/robot/<int:robot_id>', methods=['DELETE'])
def delete_robot(robot_id):
    """
    Delete a robot
    ---
    tags:
      - Robot
    parameters:
      - name: robot_id
        in: path
        type: integer
        required: true
        description: ID of the robot
    responses:
      204:
        description: Robot deleted successfully
      404:
        description: Robot not found
    """
    return robot_controller.delete(robot_id)

@robot_bp.route('/robots/with_sensors', methods=['GET'])
def get_all_robots_with_sensors():
    """
    Get all robots with their sensors
    ---
    tags:
      - Robot
    responses:
      200:
        description: List of robots with their sensors
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  model:
                    type: string
                  serial_number:
                    type: string
                  status:
                    type: string
                  sensors:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        type:
                          type: string
                        status:
                          type: string
    """
    return robot_controller.get_all_robots_with_sensors()

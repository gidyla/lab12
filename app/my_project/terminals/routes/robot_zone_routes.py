from flask import Blueprint
from my_project.terminals.controller.orders.robot_zone_controller import RobotZoneController

robot_zone_bp = Blueprint('robot_zone', __name__)
robot_zone_controller = RobotZoneController()

@robot_zone_bp.route('/robot_zone', methods=['GET'])
def get_robot_zone():
    """
    Get all robot zones
    ---
    tags:
      - RobotZone
    responses:
      200:
        description: List of all robot zones
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
                  zone_id:
                    type: integer
                  assignment_time:
                    type: string
                    format: date
    """
    return robot_zone_controller.get_all()

@robot_zone_bp.route('/robot_zone/<int:robot_zone_id>', methods=['GET'])
def get_robot_zone_by_id(robot_zone_id):
    """
    Get robot zone by ID
    ---
    tags:
      - RobotZone
    parameters:
      - name: robot_zone_id
        in: path
        type: integer
        required: true
        description: ID of the robot zone
    responses:
      200:
        description: Robot zone object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                zone_id:
                  type: integer
                assignment_time:
                  type: string
                  format: date
      404:
        description: Robot zone not found
    """
    return robot_zone_controller.get_by_id(robot_zone_id)

@robot_zone_bp.route('/robot_zone', methods=['POST'])
def add_robot_zone():
    """
    Create a new robot zone
    ---
    tags:
      - RobotZone
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              zone_id:
                type: integer
              assignment_time:
                type: string
                format: date
            required:
              - robot_id
              - zone_id
              - assignment_time
    responses:
      201:
        description: Robot zone created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                zone_id:
                  type: integer
                assignment_time:
                  type: string
                  format: date
    """
    return robot_zone_controller.create()

@robot_zone_bp.route('/robot_zone/<int:robot_zone_id>', methods=['PATCH'])
def update_robot_zone(robot_zone_id):
    """
    Update an existing robot zone
    ---
    tags:
      - RobotZone
    parameters:
      - name: robot_zone_id
        in: path
        type: integer
        required: true
        description: ID of the robot zone
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              zone_id:
                type: integer
              assignment_time:
                type: string
                format: date
    responses:
      200:
        description: Robot zone updated successfully
      404:
        description: Robot zone not found
    """
    return robot_zone_controller.update(robot_zone_id)

@robot_zone_bp.route('/robot_zone/<int:robot_zone_id>', methods=['DELETE'])
def delete_robot_zone(robot_zone_id):
    """
    Delete a robot zone
    ---
    tags:
      - RobotZone
    parameters:
      - name: robot_zone_id
        in: path
        type: integer
        required: true
        description: ID of the robot zone
    responses:
      204:
        description: Robot zone deleted successfully
      404:
        description: Robot zone not found
    """
    return robot_zone_controller.delete(robot_zone_id)

@robot_zone_bp.route('/robot_zone/with_robots_and_zones', methods=['GET'])
def get_all_robots_and_zones():
    """
    Get all robot zones with robot and zone details
    ---
    tags:
      - RobotZone
    responses:
      200:
        description: List of robot zones with robots and zones
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  robot:
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
                  zone:
                    type: object
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                  assignment_time:
                    type: string
                    format: date
    """
    return robot_zone_controller.get_all_robots_and_zones()

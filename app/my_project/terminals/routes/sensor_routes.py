from flask import Blueprint
from my_project.terminals.controller.orders.sensor_controller import SensorController

sensor_bp = Blueprint('sensor', __name__)
sensor_controller = SensorController()

@sensor_bp.route('/sensor', methods=['GET'])
def get_sensor():
    """
    Get all sensors
    ---
    tags:
      - Sensor
    responses:
      200:
        description: List of all sensors
        content:
          application/json:
            schema:
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
                  robot_id:
                    type: integer
    """
    return sensor_controller.get_all()

@sensor_bp.route('/sensor/<int:sensor_id>', methods=['GET'])
def get_sensor_by_id(sensor_id):
    """
    Get sensor by ID
    ---
    tags:
      - Sensor
    parameters:
      - name: sensor_id
        in: path
        type: integer
        required: true
        description: ID of the sensor
    responses:
      200:
        description: Sensor object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                type:
                  type: string
                status:
                  type: string
                robot_id:
                  type: integer
      404:
        description: Sensor not found
    """
    return sensor_controller.get_by_id(sensor_id)

@sensor_bp.route('/sensor', methods=['POST'])
def add_sensor():
    """
    Create a new sensor
    ---
    tags:
      - Sensor
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              type:
                type: string
              status:
                type: string
              robot_id:
                type: integer
            required:
              - type
              - status
              - robot_id
    responses:
      201:
        description: Sensor created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                type:
                  type: string
                status:
                  type: string
                robot_id:
                  type: integer
    """
    return sensor_controller.create()

@sensor_bp.route('/sensor/<int:sensor_id>', methods=['PATCH'])
def update_sensor(sensor_id):
    """
    Update an existing sensor
    ---
    tags:
      - Sensor
    parameters:
      - name: sensor_id
        in: path
        type: integer
        required: true
        description: ID of the sensor
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              type:
                type: string
              status:
                type: string
              robot_id:
                type: integer
    responses:
      200:
        description: Sensor updated successfully
      404:
        description: Sensor not found
    """
    return sensor_controller.update(sensor_id)

@sensor_bp.route('/sensor/<int:sensor_id>', methods=['DELETE'])
def delete_sensor(sensor_id):
    """
    Delete a sensor
    ---
    tags:
      - Sensor
    parameters:
      - name: sensor_id
        in: path
        type: integer
        required: true
        description: ID of the sensor
    responses:
      204:
        description: Sensor deleted successfully
      404:
        description: Sensor not found
    """
    return sensor_controller.delete(sensor_id)

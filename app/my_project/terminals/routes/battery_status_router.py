from flask import Blueprint
from my_project.terminals.controller.orders.battery_status_controller import BatteryStatusController

battery_status_bp = Blueprint('battery_status', __name__)
battery_status_controller = BatteryStatusController()

@battery_status_bp.route('/battery_status', methods=['GET'])
def get_battery_status():
    """
    Get all battery statuses
    ---
    tags:
      - BatteryStatus
    responses:
      200:
        description: List of all battery statuses
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
                  battery_level:
                    type: number
                    format: float
                  status_time:
                    type: string
                    format: date
    """
    return battery_status_controller.get_all()

@battery_status_bp.route('/battery_status/<int:battery_status_id>', methods=['GET'])
def get_battery_status_by_id(battery_status_id):
    """
    Get battery status by ID
    ---
    tags:
      - BatteryStatus
    parameters:
      - name: battery_status_id
        in: path
        type: integer
        required: true
        description: ID of the battery status
    responses:
      200:
        description: Battery status object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                battery_level:
                  type: number
                  format: float
                status_time:
                  type: string
                  format: date
      404:
        description: Battery status not found
    """
    return battery_status_controller.get_by_id(battery_status_id)

@battery_status_bp.route('/battery_status', methods=['POST'])
def add_battery_status():
    """
    Create a new battery status
    ---
    tags:
      - BatteryStatus
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              battery_level:
                type: number
                format: float
              status_time:
                type: string
                format: date
            required:
              - robot_id
              - battery_level
              - status_time
    responses:
      201:
        description: Battery status created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                battery_level:
                  type: number
                  format: float
                status_time:
                  type: string
                  format: date
    """
    return battery_status_controller.create()

@battery_status_bp.route('/battery_status/<int:battery_status_id>', methods=['PATCH'])
def update_battery_status(battery_status_id):
    """
    Update an existing battery status
    ---
    tags:
      - BatteryStatus
    parameters:
      - name: battery_status_id
        in: path
        type: integer
        required: true
        description: ID of the battery status
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              battery_level:
                type: number
                format: float
              status_time:
                type: string
                format: date
    responses:
      200:
        description: Battery status updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                battery_level:
                  type: number
                  format: float
                status_time:
                  type: string
                  format: date
      404:
        description: Battery status not found
    """
    return battery_status_controller.update(battery_status_id)

@battery_status_bp.route('/battery_status/<int:battery_status_id>', methods=['DELETE'])
def delete_battery_status(battery_status_id):
    """
    Delete a battery status
    ---
    tags:
      - BatteryStatus
    parameters:
      - name: battery_status_id
        in: path
        type: integer
        required: true
        description: ID of the battery status
    responses:
      204:
        description: Battery status deleted successfully
      404:
        description: Battery status not found
    """
    return battery_status_controller.delete(battery_status_id)

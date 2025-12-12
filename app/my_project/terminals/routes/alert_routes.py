from flask import Blueprint
from my_project.terminals.controller.orders.alert_controller import AlertController

alert_bp = Blueprint('alert', __name__)
alert_controller = AlertController()

@alert_bp.route('/alert', methods=['GET'])
def get_alerts():
    """
    Get all alerts
    ---
    tags:
      - Alerts
    responses:
      200:
        description: List of all alerts
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  alert_type:
                    type: string
                  alert_time:
                    type: string
                    format: date
                  zone_id:
                    type: integer
    """
    return alert_controller.get_all()

@alert_bp.route('/alert/<int:alert_id>', methods=['GET'])
def get_alert_by_id(alert_id):
    """
    Get alert by ID
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
        description: ID of the alert
    responses:
      200:
        description: Alert object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                alert_type:
                  type: string
                alert_time:
                  type: string
                  format: date
                zone_id:
                  type: integer
      404:
        description: Alert not found
    """
    return alert_controller.get_by_id(alert_id)

@alert_bp.route('/alert', methods=['POST'])
def add_alert():
    """
    Create a new alert
    ---
    tags:
      - Alerts
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              alert_type:
                type: string
              alert_time:
                type: string
                format: date
              zone_id:
                type: integer
            required:
              - alert_type
              - alert_time
              - zone_id
    responses:
      201:
        description: Alert created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                alert_type:
                  type: string
                alert_time:
                  type: string
                  format: date
                zone_id:
                  type: integer
    """
    return alert_controller.create()

@alert_bp.route('/alert/<int:alert_id>', methods=['PATCH'])
def update_alert(alert_id):
    """
    Update an existing alert
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
        description: ID of the alert
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              alert_type:
                type: string
              alert_time:
                type: string
                format: date
              zone_id:
                type: integer
    responses:
      200:
        description: Alert updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                alert_type:
                  type: string
                alert_time:
                  type: string
                  format: date
                zone_id:
                  type: integer
      404:
        description: Alert not found
    """
    return alert_controller.update(alert_id)

@alert_bp.route('/alert/<int:alert_id>', methods=['DELETE'])
def delete_alert(alert_id):
    """
    Delete an alert
    ---
    tags:
      - Alerts
    parameters:
      - name: alert_id
        in: path
        type: integer
        required: true
        description: ID of the alert
    responses:
      204:
        description: Alert deleted successfully
      404:
        description: Alert not found
    """
    return alert_controller.delete(alert_id)

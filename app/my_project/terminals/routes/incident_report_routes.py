from flask import Blueprint
from my_project.terminals.controller.orders.incident_report_controller import IncidentReportController

incident_report_bp = Blueprint('incident_report', __name__)
incident_report_controller = IncidentReportController()

@incident_report_bp.route('/incident_report', methods=['GET'])
def get_incident_report():
    """
    Get all incident reports
    ---
    tags:
      - IncidentReport
    responses:
      200:
        description: List of all incident reports
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
                  description:
                    type: string
                  report_time:
                    type: string
                    format: date
    """
    return incident_report_controller.get_all()

@incident_report_bp.route('/incident_report/<int:incident_report_id>', methods=['GET'])
def get_incident_report_by_id(incident_report_id):
    """
    Get incident report by ID
    ---
    tags:
      - IncidentReport
    parameters:
      - name: incident_report_id
        in: path
        type: integer
        required: true
        description: ID of the incident report
    responses:
      200:
        description: Incident report object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                description:
                  type: string
                report_time:
                  type: string
                  format: date
      404:
        description: Incident report not found
    """
    return incident_report_controller.get_by_id(incident_report_id)

@incident_report_bp.route('/incident_report', methods=['POST'])
def add_incident_report():
    """
    Create a new incident report
    ---
    tags:
      - IncidentReport
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              description:
                type: string
              report_time:
                type: string
                format: date
            required:
              - robot_id
              - description
              - report_time
    responses:
      201:
        description: Incident report created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                description:
                  type: string
                report_time:
                  type: string
                  format: date
    """
    return incident_report_controller.create()

@incident_report_bp.route('/incident_report/<int:incident_report_id>', methods=['PATCH'])
def update_incident_report(incident_report_id):
    """
    Update an existing incident report
    ---
    tags:
      - IncidentReport
    parameters:
      - name: incident_report_id
        in: path
        type: integer
        required: true
        description: ID of the incident report
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              description:
                type: string
              report_time:
                type: string
                format: date
    responses:
      200:
        description: Incident report updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                description:
                  type: string
                report_time:
                  type: string
                  format: date
      404:
        description: Incident report not found
    """
    return incident_report_controller.update(incident_report_id)

@incident_report_bp.route('/incident_report/<int:incident_report_id>', methods=['DELETE'])
def delete_incident_report(incident_report_id):
    """
    Delete an incident report
    ---
    tags:
      - IncidentReport
    parameters:
      - name: incident_report_id
        in: path
        type: integer
        required: true
        description: ID of the incident report
    responses:
      204:
        description: Incident report deleted successfully
      404:
        description: Incident report not found
    """
    return incident_report_controller.delete(incident_report_id)

from flask import Blueprint
from my_project.terminals.controller.orders.maintenance_controller import MaintenanceController

maintenance_bp = Blueprint('maintenance', __name__)
maintenance_controller = MaintenanceController()

@maintenance_bp.route('/maintenance', methods=['GET'])
def get_maintenance():
    """
    Get all maintenance records
    ---
    tags:
      - Maintenance
    responses:
      200:
        description: List of all maintenance records
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
                  maintenance_date:
                    type: string
                    format: date
                  description:
                    type: string
    """
    return maintenance_controller.get_all()

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['GET'])
def get_maintenance_by_id(maintenance_id):
    """
    Get maintenance record by ID
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
        description: ID of the maintenance record
    responses:
      200:
        description: Maintenance record object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                maintenance_date:
                  type: string
                  format: date
                description:
                  type: string
      404:
        description: Maintenance record not found
    """
    return maintenance_controller.get_by_id(maintenance_id)

@maintenance_bp.route('/maintenance', methods=['POST'])
def add_maintenance():
    """
    Create a new maintenance record
    ---
    tags:
      - Maintenance
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              maintenance_date:
                type: string
                format: date
              description:
                type: string
            required:
              - robot_id
              - maintenance_date
              - description
    responses:
      201:
        description: Maintenance record created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                maintenance_date:
                  type: string
                  format: date
                description:
                  type: string
    """
    return maintenance_controller.create()

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['PATCH'])
def update_maintenance(maintenance_id):
    """
    Update an existing maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
        description: ID of the maintenance record
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              robot_id:
                type: integer
              maintenance_date:
                type: string
                format: date
              description:
                type: string
    responses:
      200:
        description: Maintenance record updated successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                robot_id:
                  type: integer
                maintenance_date:
                  type: string
                  format: date
                description:
                  type: string
      404:
        description: Maintenance record not found
    """
    return maintenance_controller.update(maintenance_id)

@maintenance_bp.route('/maintenance/<int:maintenance_id>', methods=['DELETE'])
def delete_maintenance(maintenance_id):
    """
    Delete a maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
        description: ID of the maintenance record
    responses:
      204:
        description: Maintenance record deleted successfully
      404:
        description: Maintenance record not found
    """
    return maintenance_controller.delete(maintenance_id)

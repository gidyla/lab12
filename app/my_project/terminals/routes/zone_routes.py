from flask import Blueprint
from my_project.terminals.controller.orders.zone_controller import ZoneController

zone_bp = Blueprint('zone', __name__)
zone_controller = ZoneController()

@zone_bp.route('/zone', methods=['GET'])
def get_zone():
    """
    Get all zones
    ---
    tags:
      - Zone
    responses:
      200:
        description: List of all zones
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  description:
                    type: string
    """
    return zone_controller.get_all()

@zone_bp.route('/zone/<int:zone_id>', methods=['GET'])
def get_zone_by_id(zone_id):
    """
    Get zone by ID
    ---
    tags:
      - Zone
    parameters:
      - name: zone_id
        in: path
        type: integer
        required: true
        description: ID of the zone
    responses:
      200:
        description: Zone object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
      404:
        description: Zone not found
    """
    return zone_controller.get_by_id(zone_id)

@zone_bp.route('/zone', methods=['POST'])
def add_zone():
    """
    Create a new zone
    ---
    tags:
      - Zone
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              description:
                type: string
            required:
              - name
    responses:
      201:
        description: Zone created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                name:
                  type: string
                description:
                  type: string
    """
    return zone_controller.create()

@zone_bp.route('/zone/<int:zone_id>', methods=['PATCH'])
def update_zone(zone_id):
    """
    Update an existing zone
    ---
    tags:
      - Zone
    parameters:
      - name: zone_id
        in: path
        type: integer
        required: true
        description: ID of the zone
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
              description:
                type: string
    responses:
      200:
        description: Zone updated successfully
      404:
        description: Zone not found
    """
    return zone_controller.update(zone_id)

@zone_bp.route('/zone/<int:zone_id>', methods=['DELETE'])
def delete_zone(zone_id):
    """
    Delete a zone
    ---
    tags:
      - Zone
    parameters:
      - name: zone_id
        in: path
        type: integer
        required: true
        description: ID of the zone
    responses:
      204:
        description: Zone deleted successfully
      404:
        description: Zone not found
    """
    return zone_controller.delete(zone_id)

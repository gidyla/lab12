from flask import Blueprint
from my_project.terminals.controller.orders.user_controller import UserController

user_bp = Blueprint('user', __name__)
user_controller = UserController()

@user_bp.route('/user', methods=['GET'])
def get_user():
    """
    Get all users
    ---
    tags:
      - User
    responses:
      200:
        description: List of all users
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: integer
                  username:
                    type: string
                  role:
                    type: string
    """
    return user_controller.get_all()

@user_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Get user by ID
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: User object
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                username:
                  type: string
                role:
                  type: string
      404:
        description: User not found
    """
    return user_controller.get_by_id(user_id)

@user_bp.route('/user', methods=['POST'])
def add_user():
    """
    Create a new user
    ---
    tags:
      - User
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              role:
                type: string
            required:
              - username
              - role
    responses:
      201:
        description: User created successfully
        content:
          application/json:
            schema:
              type: object
              properties:
                id:
                  type: integer
                username:
                  type: string
                role:
                  type: string
    """
    return user_controller.create()

@user_bp.route('/user/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    """
    Update an existing user
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              role:
                type: string
    responses:
      200:
        description: User updated successfully
      404:
        description: User not found
    """
    return user_controller.update(user_id)

@user_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      204:
        description: User deleted successfully
      404:
        description: User not found
    """
    return user_controller.delete(user_id)

@user_bp.route('/user/<int:user_id>/robot_controls', methods=['GET'])
def get_user_robot_controls(user_id):
    """
    Get all robot controls for a specific user
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user
    responses:
      200:
        description: List of robot controls for the user
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
                  command:
                    type: string
                  command_time:
                    type: string
                  user_id:
                    type: integer
      404:
        description: User not found
    """
    return user_controller.get_user_robot_controls(user_id)

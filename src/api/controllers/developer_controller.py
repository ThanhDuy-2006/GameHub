from flask import Blueprint, request, jsonify
from services.developer_service import DeveloperService
from services.user_service import UserService
from infrastructure.repositories.developer_repository import DeveloperRepository
from infrastructure.repositories.user_repository import UserRepository
from api.schemas.developer import DeveloperRequestSchema, DeveloperResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('developer', __name__, url_prefix='/developers')

# Inject UserService vào DeveloperService
user_service = UserService(UserRepository(session))
developer_service = DeveloperService(DeveloperRepository(session), user_service)

request_schema = DeveloperRequestSchema()
response_schema = DeveloperResponseSchema()

@bp.route('/', methods=['GET'])
def list_developers():
    """
    Get all developers
    ---
    get:
      summary: Get all developers
      tags:
        - Developers
      responses:
        200:
          description: List of developers
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DeveloperResponse'
    """
    developers = developer_service.list_developers()
    return jsonify(response_schema.dump(developers, many=True)), 200

@bp.route('/<int:developer_id>', methods=['GET'])
def get_developer(developer_id):
    """
    Get developer by id
    ---
    get:
      summary: Get developer by id
      parameters:
        - name: developer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của developer cần lấy
      tags:
        - Developers
      responses:
        200:
          description: object of developer
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeveloperResponse'
        404:
          description: Developer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    developer = developer_service.get_developer_by_id(developer_id)
    if developer is None:
        return jsonify({'message': 'Developer not found'}), 404
    return jsonify(response_schema.dump(developer)), 200

@bp.route('/get-by-user-id/<int:user_id>', methods=['GET'])
def get_developer_by_user_id(user_id):
    """
    Get developer by user_id
    ---
    get:
      summary: Get developer by user_id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của user cần lấy developer
      tags:
        - Developers
      responses:
        200:
          description: object of developer
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeveloperResponse'
        404:
          description: Developer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    developer = developer_service.get_developer_by_user_id(user_id)
    if developer is None:
        return jsonify({'message': 'Developer not found'}), 404
    return jsonify(response_schema.dump(developer)), 200

@bp.route('/', methods=['POST'])
def add_developer():
    """
    Create a new developer
    ---
    post:
      summary: Create a new developer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeveloperRequest'
      tags:
        - Developers
      responses:
        201:
          description: Developer created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeveloperResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    dev = developer_service.add_developer(
        user_id=data['user_id'],
        payment_info=data['payment_info'],
    )
    return jsonify(response_schema.dump(dev)), 201

@bp.route('/<int:developer_id>', methods=['PUT'])
def update_developer(developer_id):
    """
    Update a developer by id
    ---
    put:
      summary: Update a developer by id
      parameters:
        - name: developer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của developer cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DeveloperRequest'
      tags:
        - Developers
      responses:
        200:
          description: Developer updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeveloperResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        404:
          description: Developer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    dev = developer_service.update_developer(
        developer_id=developer_id,
        user_id=data['user_id'],
        payment_info=data['payment_info']
    )
    if dev is None:
        return jsonify({'message': 'Developer not found'}), 404
    return jsonify(response_schema.dump(dev)), 200

@bp.route('/<int:developer_id>', methods=['DELETE'])
def delete_developer(developer_id):
    """
    Delete a developer by id
    ---
    delete:
      summary: Delete a developer by id
      parameters:
        - name: developer_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của developer cần xóa
      tags:
        - Developers
      responses:
        204:
          description: Developer deleted successfully
        404:
          description: Developer not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        developer_service.delete_developer(developer_id)
        return '', 204
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
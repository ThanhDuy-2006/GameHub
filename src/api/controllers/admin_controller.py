from flask import Blueprint, request, jsonify
from services.admin_service import AdminService
from services.user_service import UserService
from infrastructure.repositories.admin_repository import AdminRepository
from infrastructure.repositories.user_repository import UserRepository
from api.schemas.admin import AdminRequestSchema, AdminResponseSchema
from infrastructure.databases.mssql import session

bp = Blueprint('admin', __name__, url_prefix='/admins')

# Inject UserService vào AdminService
user_service = UserService(UserRepository(session))
admin_service = AdminService(AdminRepository(), user_service)

request_schema = AdminRequestSchema()
response_schema = AdminResponseSchema()

@bp.route('/', methods=['GET'])
def list_admins():
    """
    Get all admins
    ---
    get:
      summary: Get all admins
      tags:
        - Admins
      responses:
        200:
          description: List of admins
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/AdminResponse'
    """
    admins = admin_service.list_admins()
    return jsonify(response_schema.dump(admins, many=True)), 200

@bp.route('/<int:admin_id>', methods=['GET'])
def get_admin(admin_id):
    """
    Get admin by id
    ---
    get:
      summary: Get admin by id
      parameters:
        - name: admin_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của admin cần lấy
      tags:
        - Admins
      responses:
        200:
          description: object of admin
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminResponse'
        404:
          description: Admin not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    admin = admin_service.get_admin(admin_id)
    if not admin:
        return jsonify({'message': 'Admin not found'}), 404
    return jsonify(response_schema.dump(admin)), 200

@bp.route('/get-by-user-id/<int:user_id>', methods=['GET'])
def get_admin_by_user_id(user_id):
    """
    Get admin by user id
    ---
    get:
      summary: Get admin by user id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần lấy admin
      tags:
        - Admins
      responses:
        200:
          description: object of admin
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminResponse'
        404:
          description: Admin not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    admin = admin_service.get_admin_by_user_id(user_id)
    if admin is None:
        return jsonify({'message': 'Admin not found'}), 404
    return jsonify(response_schema.dump(admin)), 200

@bp.route('/', methods=['POST'])
def create_admin():
    """
    Create a new admin
    ---
    post:
      summary: Create a new admin
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminRequest'
      tags:
        - Admins
      responses:
        201:
          description: Admin created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminResponse'
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
    
    try:
        admin = admin_service.create_admin(
            user_id=data['user_id']
        )
        return jsonify(response_schema.dump(admin)), 201
    except ValueError as e:
        error_msg = str(e)
        if 'FOREIGN KEY constraint' in error_msg:
            return jsonify({'error': f'User with id {data["user_id"]} does not exist. Please create the user first or use a valid user_id.'}), 400
        elif 'Unique constraint' in error_msg or 'UNIQUE constraint' in error_msg:
            return jsonify({'error': f'Admin with user_id {data["user_id"]} already exists.'}), 400
        else:
            return jsonify({'error': error_msg}), 400

@bp.route('/<int:admin_id>', methods=['PUT'])
def update_admin(admin_id):
    """
    Update admin
    ---
    put:
      summary: Update admin by id
      parameters:
        - name: admin_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của admin cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AdminRequest'
      tags:
        - Admins
      responses:
        200:
          description: Admin updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AdminResponse'
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
          description: Admin not found
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
    
    try:
        admin = admin_service.update_admin(
            admin_id=admin_id,
            user_id=data['user_id']
        )
        return jsonify(response_schema.dump(admin)), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@bp.route('/<int:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    """
    Delete admin
    ---
    delete:
      summary: Delete admin by id
      parameters:
        - name: admin_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của admin cần xóa
      tags:
        - Admins
      responses:
        204:
          description: Admin deleted successfully
        404:
          description: Admin not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        admin_service.delete_admin(admin_id)
        return '', 204
    except ValueError as e:
        if 'not found' in str(e).lower():
            return jsonify({'message': 'Admin not found'}), 404
        else:
            return jsonify({'error': str(e)}), 400
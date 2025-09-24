from flask import Blueprint, request, jsonify
from services.user_service import UserService
from services.player_service import PlayerService
from services.admin_service import AdminService
from services.developer_service import DeveloperService
from services.designer_service import DesignerService
from infrastructure.repositories.user_repository import UserRepository
from infrastructure.repositories.player_repository import PlayerRepository
from infrastructure.repositories.admin_repository import AdminRepository
from infrastructure.repositories.developer_repository import DeveloperRepository
from infrastructure.repositories.designer_repository import DesignerRepository
from api.schemas.user import UserRequestSchema, UserResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

bp = Blueprint('user', __name__, url_prefix='/users')

player_service = PlayerService(PlayerRepository(session))
admin_service = AdminService(AdminRepository(session))
developer_service = DeveloperService(DeveloperRepository(session))
designer_service = DesignerService(DesignerRepository(session))

user_service = UserService(
    UserRepository(session),
    player_service=player_service,
    admin_service=admin_service,
    developer_service=developer_service,
    designer_service=designer_service
)

request_schema = UserRequestSchema()
response_schema = UserResponseSchema()

@bp.route('/', methods=['GET'])
def list_users():
    """
    Get all users
    ---
    get:
      summary: Get all users
      tags:
        - Users
      responses:
        200:
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/UserResponse'
    """
    users = user_service.list_users()
    return jsonify(response_schema.dump(users, many=True)), 200

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by id
    ---
    get:
      summary: Get user by id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần lấy
      tags:
        - Users
      responses:
        200:
          description: object of user
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        404:
          description: User not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    user = user_service.get_user_by_id(user_id)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(response_schema.dump(user)), 200

@bp.route('', methods=['POST'], strict_slashes=False)
def add_user():
    """
    Add a new user
    ---
    post:
      summary: Add a new user
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
      responses:
        201:
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
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
    now = datetime.utcnow()
    user = user_service.add_user(
        username=data['username'],
        password=data['password'],
        role=data['role'],
        status=data['status'],
        created_at=now,
        updated_at=now
    )
    role = data['role']
    extra_kwargs = {}
    if role == 'player':
        extra_kwargs['scores'] = data.get('scores', 0)
        extra_kwargs['point'] = data.get('point', 0)
    elif role == 'developer':
        extra_kwargs['payment_info'] = data.get('payment_info', '')
    elif role == 'designer':
        extra_kwargs['paymentinfo'] = data.get('paymentinfo', '')
    user_service.create_role_data(role, user.id, **extra_kwargs)
    return jsonify(response_schema.dump(user)), 201  

@bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update an existing user
    ---
    put:
      summary: Update an existing user
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần cập nhật
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
      responses:
        200:
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
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
          description: User not found
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
        user = user_service.update_user(
            user_id=user_id,  # Fixed: use user_id parameter instead of id
            username=data['username'],
            password=data['password'],
            role=data['role'],
            status=data['status'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return jsonify(response_schema.dump(user)), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user by id
    ---
    delete:
      summary: Delete a user by id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của người dùng cần xóa
      tags:
        - Users
      responses:
        204:
          description: User deleted successfully
        404:
          description: User not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    role = user.role
    # Xóa dữ liệu ở bảng role tương ứng
    if role == 'player':
        player = player_service.get_player_by_user_id(user_id)
        if player:
            # Xóa các bản ghi game_review liên quan đến player
            from infrastructure.models.game_review_model import GameReviewModel
            reviews = session.query(GameReviewModel).filter_by(player_id=player.id).all()
            for review in reviews:
                session.delete(review)
            session.commit()
            player_service.delete_player(player.id)
    elif role == 'admin':
        admin = admin_service.get_admin_by_user_id(user_id)
        if admin:
            admin_service.delete_admin(admin.id)
    elif role == 'developer':
        developer = developer_service.get_developer_by_user_id(user_id)
        if developer:
            developer_service.delete_developer(developer.id)
    elif role == 'designer':
        designer = designer_service.get_designer_by_user_id(user_id)
        if designer:
            designer_service.delete_designer(designer.id)
    # Xóa user
    user_service.delete_user(user_id)
    return '', 204

@bp.route('/login', methods=['POST'])
def login():
    """
    User login
    ---
    post:
      summary: User login
      tags:
        - Users
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        200:
          description: Login successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  access_token:
                    type: string
        401:
          description: Invalid credentials
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Missing JSON data'}), 400

    username = data.get('username')
    password = data.get('password')
    user = user_service.authenticate(username, password)

    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "id": user.id,
            "username": user.username,
            "role": user.role,
            "access_token": access_token
        }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


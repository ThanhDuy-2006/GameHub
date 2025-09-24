from flask import Blueprint, request, jsonify
from services.redeem_service import RedeemService
from services.player_service import PlayerService
from services.reward_service import RewardService
from infrastructure.repositories.redeem_repository import RedeemRepository
from infrastructure.repositories.player_repository import PlayerRepository
from infrastructure.repositories.reward_repository import RewardRepository
from infrastructure.repositories.user_repository import UserRepository
from services.user_service import UserService
from api.schemas.redeem import RedeemRequestSchema, RedeemResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('redeem', __name__, url_prefix='/redeems')

# Inject dependencies vào RedeemService
user_service = UserService(UserRepository(session))
player_service = PlayerService(PlayerRepository(session), user_service)
reward_service = RewardService(RewardRepository(session))
redeem_service = RedeemService(RedeemRepository(session), player_service, reward_service)

request_schema = RedeemRequestSchema()
response_schema = RedeemResponseSchema()

@bp.route('/', methods=['GET'])
def list_redeems():
    """
    Get all redeems
    ---
    get:
      summary: Get all redeems
      tags:
        - Redeems
      responses:
        200:
          description: List of redeems
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/RedeemResponse'
    """
    redeems = redeem_service.list_redeems()
    return jsonify(response_schema.dump(redeems, many=True)), 200

@bp.route('/<int:redeem_id>', methods=['GET'])
def get_redeem(redeem_id):
    """
    Get redeem by id
    ---
    get:
      summary: Get redeem by id
      parameters:
        - name: redeem_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của redeem cần lấy
      tags:
        - Redeems
      responses:
        200:
          description: object of redeem
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RedeemResponse'
        404:
          description: Redeem not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    redeem = redeem_service.get_redeem(redeem_id)
    if not redeem:
        return jsonify({'message': 'Redeem not found'}), 404
    return jsonify(response_schema.dump(redeem)), 200

@bp.route('/', methods=['POST'])
def create_redeem():
    """
    Create a new redeem
    ---
    post:
      summary: Create a new redeem
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RedeemRequest'
      tags:
        - Redeems
      responses:
        201:
          description: Redeem created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RedeemResponse'
        400:
          description: Invalid input
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
    
    now = datetime.utcnow()
    redeem = redeem_service.create_redeem(
        player_id=data['player_id'],
        reward_id=data['reward_id'],
        points_used=data['points_used'],
        status=data['status'],
        created_at=now
    )
    return jsonify(response_schema.dump(redeem)), 201

@bp.route('/<int:redeem_id>', methods=['PUT'])
def update_redeem(redeem_id):
    """
    Update a redeem by id
    ---
    put:
      summary: Update a redeem by id
      parameters:
        - name: redeem_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của redeem cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RedeemRequest'
      tags:
        - Redeems
      responses:
        200:
          description: Redeem updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RedeemResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        404:
          description: Redeem not found
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
    
    now = datetime.utcnow()
    redeem = redeem_service.update_redeem(
        redeem_id=redeem_id,
        player_id=data['player_id'],
        reward_id=data['reward_id'],
        points_used=data['points_used'],
        status=data['status'],
        created_at=now
    )
    return jsonify(response_schema.dump(redeem)), 200

@bp.route('/<int:redeem_id>', methods=['DELETE'])
def delete_redeem(redeem_id):
    """
    Delete a redeem by id
    ---
    delete:
      summary: Delete a redeem by id
      parameters:
        - name: redeem_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của redeem cần xóa
      tags:
        - Redeems
      responses:
        204:
          description: Redeem deleted successfully
        404:
          description: Redeem not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    redeem_service.delete_redeem(redeem_id)
    return '', 204
from flask import Blueprint, request, jsonify
from services.player_service import PlayerService
from services.user_service import UserService
from infrastructure.repositories.player_repository import PlayerRepository
from infrastructure.repositories.user_repository import UserRepository
from api.schemas.player import PlayerRequestSchema, PlayerResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('player', __name__, url_prefix='/players')

# Inject UserService vào PlayerService
user_service = UserService(UserRepository(session))
player_service = PlayerService(PlayerRepository(session), user_service)

request_schema = PlayerRequestSchema()
response_schema = PlayerResponseSchema()

@bp.route('/', methods=['GET'])
def list_players():
    """
    Get all players
    ---
    get:
      summary: Get all players
      tags:
        - Players
      responses:
        200:
          description: List of players
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PlayerResponse'
    """
    players = player_service.list_players()
    return jsonify(response_schema.dump(players, many=True)), 200

@bp.route('/<int:player_id>', methods=['GET'])
def get_player(player_id):
    """
    Get player by id
    ---
    get:
      summary: Get player by id
      parameters:
        - name: player_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của player cần lấy
      tags:
        - Players
      responses:
        200:
          description: object of player
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PlayerResponse'
        404:
          description: Player not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    player = player_service.get_player(player_id)
    if not player:
        return jsonify({'message': 'Player not found'}), 404
    return jsonify(response_schema.dump(player)), 200

@bp.route('/get-by-user-id/<int:user_id>', methods=['GET'])
def get_player_by_user_id(user_id):
    """
    Get player by user id
    ---
    get:
      summary: Get player by user id
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của user cần lấy player
      tags:
        - Players
      responses:
        200:
          description: object of player
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PlayerResponse'
        404:
          description: Player not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    player = player_service.get_player_by_user_id(user_id)
    if player is None:
        return jsonify({'message': 'Player not found'}), 404
    return jsonify(response_schema.dump(player)), 200

@bp.route('/', methods=['POST'])
def create_player():
    """
    Create a new player
    ---
    post:
      summary: Create a new player
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PlayerRequest'
      tags:
        - Players
      responses:
        201:
          description: Player created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PlayerResponse'
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
    player = player_service.create_player(
      user_id=data['user_id'],
      scores=data['scores'],
      point=data['point'],
      created_at=now,
      updated_at=now
    )
    return jsonify(response_schema.dump(player)), 201

@bp.route('/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    """
    Update a player by id
    ---
    put:
      summary: Update a player by id
      parameters:
        - name: player_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của player cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PlayerRequest'
      tags:
        - Players
      responses:
        200:
          description: Player updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PlayerResponse'
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
          description: Player not found
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
    player = player_service.update_player(
      player_id=player_id,
      user_id=data['user_id'],
      scores=data['scores'],
      point=data['point'],
      created_at=now,
      updated_at=now
      )
    return jsonify(response_schema.dump(player)), 200

@bp.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    """
    Delete a player by id
    ---
    delete:
      summary: Delete a player by id
      parameters:
        - name: player_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của player cần xóa
      tags:
        - Players
      responses:
        204:
          description: Player deleted successfully
        404:
          description: Player not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    player_service.delete_player(player_id)
    return '', 204
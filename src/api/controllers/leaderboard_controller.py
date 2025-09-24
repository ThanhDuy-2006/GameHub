from flask import Blueprint, request, jsonify
from services.leaderboard_service import LeaderboardService
from infrastructure.repositories.leaderboard_repository import LeaderboardRepository
from api.schemas.leaderboard import LeaderboardRequestSchema, LeaderboardResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('leaderboard', __name__, url_prefix='/leaderboards')

leaderboard_service = LeaderboardService(LeaderboardRepository(session))

request_schema = LeaderboardRequestSchema()
response_schema = LeaderboardResponseSchema()

@bp.route('/', methods=['GET'])
def list_leaderboards():
    """
    Get all leaderboard entries
    ---
    get:
      summary: Get all leaderboard entries
      tags:
        - Leaderboards
      responses:
        200:
          description: List of leaderboard entries
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LeaderboardResponse'
    """
    leaderboards = leaderboard_service.list_leaderboard_entries()
    return jsonify(response_schema.dump(leaderboards, many=True)), 200

@bp.route('/<int:leaderboard_id>', methods=['GET'])
def get_leaderboard(leaderboard_id):
    """
    Get leaderboard entry by id
    ---
    get:
      summary: Get leaderboard entry by id
      parameters:
        - name: leaderboard_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của leaderboard entry cần lấy
      tags:
        - Leaderboards
      responses:
        200:
          description: Leaderboard entry object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LeaderboardResponse'
        404:
          description: Leaderboard entry not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    leaderboard = leaderboard_service.get_leaderboard_entry(leaderboard_id)
    if not leaderboard:
        return jsonify({'message': 'Leaderboard entry not found'}), 404
    return jsonify(response_schema.dump(leaderboard)), 200

@bp.route('/game/<int:game_id>', methods=['GET'])
def get_leaderboard_by_game(game_id):
    """
    Get leaderboard entries by game id
    ---
    get:
      summary: Get leaderboard entries by game id
      parameters:
        - name: game_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của game để lấy leaderboard
      tags:
        - Leaderboards
      responses:
        200:
          description: List of leaderboard entries for the game
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LeaderboardResponse'
    """
    leaderboards = leaderboard_service.get_leaderboard_by_game(game_id)
    return jsonify(response_schema.dump(leaderboards, many=True)), 200

@bp.route('/player/<int:player_id>', methods=['GET'])
def get_leaderboard_by_player(player_id):
    """
    Get leaderboard entries by player id
    ---
    get:
      summary: Get leaderboard entries by player id
      parameters:
        - name: player_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của player để lấy leaderboard entries
      tags:
        - Leaderboards
      responses:
        200:
          description: List of leaderboard entries for the player
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LeaderboardResponse'
    """
    leaderboards = leaderboard_service.get_leaderboard_by_player(player_id)
    return jsonify(response_schema.dump(leaderboards, many=True)), 200

@bp.route('/', methods=['POST'])
def create_leaderboard():
    """
    Create a new leaderboard entry
    ---
    post:
      summary: Create a new leaderboard entry
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LeaderboardRequest'
      tags:
        - Leaderboards
      responses:
        201:
          description: Leaderboard entry created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LeaderboardResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: object
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    now = datetime.utcnow()
    leaderboard = leaderboard_service.create_leaderboard_entry(
        player_id=data['player_id'],
        game_id=data['game_id'],
        score=data['score'],
        achieved_at=now
    )
    return jsonify(response_schema.dump(leaderboard)), 201

@bp.route('/<int:leaderboard_id>', methods=['PUT'])
def update_leaderboard(leaderboard_id):
    """
    Update a leaderboard entry by id
    ---
    put:
      summary: Update a leaderboard entry by id
      parameters:
        - name: leaderboard_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của leaderboard entry cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LeaderboardRequest'
      tags:
        - Leaderboards
      responses:
        200:
          description: Leaderboard entry updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LeaderboardResponse'
        400:
          description: Invalid input
          content:
            application/json:
              schema:
                type: object
                properties:
                  errors:
                    type: object
        404:
          description: Leaderboard entry not found
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
    leaderboard = leaderboard_service.update_leaderboard_entry(
        leaderboard_id=leaderboard_id,
        player_id=data['player_id'],
        game_id=data['game_id'],
        score=data['score'],
        achieved_at=now
    )
    return jsonify(response_schema.dump(leaderboard)), 200

@bp.route('/<int:leaderboard_id>', methods=['DELETE'])
def delete_leaderboard(leaderboard_id):
    """
    Delete a leaderboard entry by id
    ---
    delete:
      summary: Delete a leaderboard entry by id
      parameters:
        - name: leaderboard_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của leaderboard entry cần xóa
      tags:
        - Leaderboards
      responses:
        204:
          description: Leaderboard entry deleted successfully
        404:
          description: Leaderboard entry not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    leaderboard_service.delete_leaderboard_entry(leaderboard_id)
    return '', 204
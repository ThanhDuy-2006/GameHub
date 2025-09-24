from flask import Blueprint, request, jsonify
from services.game_service import GameService
from infrastructure.repositories.game_repository import GameRepository
from api.schemas.game import GameRequestSchema, GameResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('game', __name__, url_prefix='/games')

game_service = GameService(GameRepository(session))

request_schema = GameRequestSchema()
response_schema = GameResponseSchema()

@bp.route('/', methods=['GET'])
def list_games():
    """
    Get all games
    ---
    get:
      summary: Get all games
      tags:
        - Games
      responses:
        200:
          description: List of games
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GameResponse'
    """
    games = game_service.list_games()
    return jsonify(response_schema.dump(games, many=True)), 200

@bp.route('/<int:game_id>', methods=['GET'])
def get_game(game_id):
    """
    Get game by id
    ---
    get:
      summary: Get game by id
      parameters:
        - name: game_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the game to retrieve
      tags:
        - Games
      responses:
        200:
          description: object of game
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameResponse'
        404:
          description: Game not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    game = game_service.get_game(game_id)
    if not game:
        return jsonify({'message': 'Game not found'}), 404
    return jsonify(response_schema.dump(game)), 200

@bp.route('/', methods=['POST'])
def create_game():
    """
    Create a new game
    ---
    post:
      summary: Create a new game
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GameRequest'
      tags:
        - Games
      responses:
        201:
          description: Game created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameResponse'
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
    game = game_service.create_game(
        dev_id=data['dev_id'],
        name=data['name'],
        description=data['description'],
        price=data['price'],
        sources=data.get('sources', ''),
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(game)), 201  

@bp.route('/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    """
    Update a game by id
    ---
    put:
      summary: Update a game by id
      parameters:
        - name: game_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the game to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GameRequest'
      tags:
        - Games
      responses:
        200:
          description: Game updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameResponse'
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
          description: Game not found
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
    game = game_service.update_game(
        game_id=game_id,
        dev_id=data['dev_id'],
        name=data['name'],
        description=data['description'],
        price=data['price'],
        sources=data.get('sources', ''),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(game)), 200

@bp.route('/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    """
    Delete a game by id
    ---
    delete:
      summary: Delete a game by id
      parameters:
        - name: game_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the game to delete
      tags:
        - Games
      responses:
        204:
          description: Game deleted successfully
        404:
          description: Game not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    game_service.delete_game(game_id)
    return '', 204

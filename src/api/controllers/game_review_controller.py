from flask import Blueprint, request, jsonify
from services.game_review_service import GameReviewService
from infrastructure.repositories.game_review_repository import GameReviewRepository
from api.schemas.game_review import GameReviewRequestSchema, GameReviewResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('game_review', __name__, url_prefix='/game-reviews')

service = GameReviewService(GameReviewRepository(session))

request_schema = GameReviewRequestSchema()
response_schema = GameReviewResponseSchema()

@bp.route('/', methods=['GET'])
def list_reviews():
    """
    Get all game reviews
    ---
    get:
      summary: Get all game reviews
      tags:
        - Game Reviews
      responses:
        200:
          description: List of game reviews
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/GameReviewResponse'
    """
    items = service.list_reviews()
    return jsonify(response_schema.dump(items, many=True)), 200

@bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """
    Get game review by id
    ---
    get:
      summary: Get game review by id
      parameters:
        - name: review_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the review to fetch
      tags:
        - Game Reviews
      responses:
        200:
          description: object of game review
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameReviewResponse'
        404:
          description: Game review not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    item = service.get_review(review_id)
    if not item:
        return jsonify({'message': 'Game review not found'}), 404
    return jsonify(response_schema.dump(item)), 200

@bp.route('/', methods=['POST'])
def create_review():
    """
    Create a new game review
    ---
    post:
      summary: Create a new game review
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GameReviewRequest'
      tags:
        - Game Reviews
      responses:
        201:
          description: Game review created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameReviewResponse'
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
    item = service.create_review(
        game_id=data['game_id'],
        player_id=data['player_id'],
        rating=data['rating'],
        comment=data.get('comment'),
        review_date=data.get('review_date', now),
    )
    return jsonify(response_schema.dump(item)), 201

@bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Update a game review by id
    ---
    put:
      summary: Update a game review by id
      parameters:
        - name: review_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the review to update
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GameReviewRequest'
      tags:
        - Game Reviews
      responses:
        200:
          description: Game review updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GameReviewResponse'
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
          description: Game review not found
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
    item = service.update_review(
        review_id=review_id,
        game_id=data['game_id'],
        player_id=data['player_id'],
        rating=data['rating'],
        comment=data.get('comment'),
        review_date=data.get('review_date', now),
    )
    return jsonify(response_schema.dump(item)), 200

@bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a game review by id
    ---
    delete:
      summary: Delete a game review by id
      parameters:
        - name: review_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the review to delete
      tags:
        - Game Reviews
      responses:
        204:
          description: Game review deleted successfully
        404:
          description: Game review not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    service.delete_review(review_id)
    return '', 204

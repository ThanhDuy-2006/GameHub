from flask import Blueprint, request, jsonify
from services.reward_service import RewardService
from infrastructure.repositories.reward_repository import RewardRepository
from api.schemas.reward import RewardRequestSchema, RewardResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('reward', __name__, url_prefix='/rewards')

reward_service = RewardService(RewardRepository(session))

request_schema = RewardRequestSchema()
response_schema = RewardResponseSchema()

@bp.route('/', methods=['GET'])
def list_rewards():
    """
    Get all rewards
    ---
    get:
      summary: Get all rewards
      tags:
        - Rewards
      responses:
        200:
          description: List of rewards
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/RewardResponse'
    """
    rewards = reward_service.list_rewards()
    return jsonify(response_schema.dump(rewards, many=True)), 200

@bp.route('/<int:reward_id>', methods=['GET'])
def get_reward(reward_id):
    """
    Get reward by id
    ---
    get:
      summary: Get reward by id
      parameters:
        - name: reward_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của reward cần lấy
      tags:
        - Rewards
      responses:
        200:
          description: object of reward
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardResponse'
        404:
          description: Reward not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    reward = reward_service.get_reward(reward_id)
    if not reward:
        return jsonify({'message': 'Reward not found'}), 404
    return jsonify(response_schema.dump(reward)), 200

@bp.route('/', methods=['POST'])
def create_reward():
    """
    Create a new reward
    ---
    post:
      summary: Create a new reward
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RewardRequest'
      tags:
        - Rewards
      responses:
        201:
          description: Reward created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardResponse'
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
    reward = reward_service.create_reward(
        name=data['name'],
        description=data.get('description', ''),
        point_required=data['point_required'],
        quantity=data['quantity'],
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(reward)), 201

@bp.route('/<int:reward_id>', methods=['PUT'])
def update_reward(reward_id):
    """
    Update a reward by id
    ---
    put:
      summary: Update a reward by id
      parameters:
        - name: reward_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của reward cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RewardRequest'
      tags:
        - Rewards
      responses:
        200:
          description: Reward updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RewardResponse'
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
          description: Reward not found
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
    reward = reward_service.update_reward(
        reward_id=reward_id,
        name=data['name'],
        description=data.get('description', ''),
        point_required=data['point_required'],
        quantity=data['quantity'],
        created_at=now,
        updated_at=now
    )
    return jsonify(response_schema.dump(reward)), 200

@bp.route('/<int:reward_id>', methods=['DELETE'])
def delete_reward(reward_id):
    """
    Delete a reward by id
    ---
    delete:
      summary: Delete a reward by id
      parameters:
        - name: reward_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của reward cần xóa
      tags:
        - Rewards
      responses:
        204:
          description: Reward deleted successfully
        404:
          description: Reward not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    reward_service.delete_reward(reward_id)
    return '', 204
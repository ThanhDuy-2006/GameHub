from flask import Blueprint, request, jsonify
from services.asset_service import AssetService
from infrastructure.repositories.asset_repository import AssetRepository
from api.schemas.asset import AssetRequestSchema, AssetResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('asset', __name__, url_prefix='/assets')

asset_service = AssetService(AssetRepository(session))
request_schema = AssetRequestSchema()
response_schema = AssetResponseSchema()

@bp.route('/', methods=['GET'])
def list_assets():
    """
    Get all assets
    ---
    get:
      summary: Get all assets
      tags:
        - Assets
      responses:
        200:
          description: List of assets
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/AssetResponse'
    """
    assets = asset_service.list_assets()
    return jsonify(response_schema.dump(assets, many=True)), 200

@bp.route('/<int:asset_id>', methods=['GET'])
def get_asset(asset_id):
    """
    Get asset by id
    ---
    get:
      summary: Get asset by id
      parameters:
        - name: asset_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset cần lấy
      tags:
        - Assets
      responses:
        200:
          description: object of asset
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetResponse'
        404:
          description: Asset not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    asset = asset_service.get_asset_by_id(asset_id)
    if not asset:
        return jsonify({'message': 'Asset not found'}), 404
    return jsonify(response_schema.dump(asset)), 200

@bp.route('/', methods=['POST'])
def create_asset():
    """
    Create a new asset
    ---
    post:
      summary: Create a new asset
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssetRequest'
      tags:
        - Assets
      responses:
        201:
          description: Asset created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetResponse'
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
    asset = asset_service.create_asset(
        designer_id=data['designer_id'],
        name=data['name'],
        type=data.get('type'),
        price=data['price'],
        download_count=data.get('download_count', 0),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(asset)), 201

@bp.route('/<int:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    """
    Update an asset by id
    ---
    put:
      summary: Update an asset by id
      parameters:
        - name: asset_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssetRequest'
      tags:
        - Assets
      responses:
        200:
          description: Asset updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetResponse'
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
          description: Asset not found
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
    old = asset_service.get_asset_by_id(asset_id)
    if not old:
        return jsonify({'message': 'Asset not found'}), 404
    asset = asset_service.update_asset(
        asset_id=asset_id,
        designer_id=data.get('designer_id', old.designer_id),
        name=data.get('name', old.name),
        type=data.get('type', old.type),
        price=data.get('price', old.price),
        download_count=data.get('download_count', old.download_count),
        created_at=old.created_at,
        updated_at=datetime.utcnow()
    )
    return jsonify(response_schema.dump(asset)), 200

@bp.route('/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """
    Delete an asset by id
    ---
    delete:
      summary: Delete an asset by id
      parameters:
        - name: asset_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset cần xóa
      tags:
        - Assets
      responses:
        204:
          description: Asset deleted successfully
        404:
          description: Asset not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    asset = asset_service.get_asset_by_id(asset_id)
    if not asset:
        return jsonify({'message': 'Asset not found'}), 404
    asset_service.delete_asset(asset_id)
    return '', 204

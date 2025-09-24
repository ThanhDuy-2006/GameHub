from flask import Blueprint, request, jsonify
from services.asset_purchases_service import AssetPurchaseService
from infrastructure.repositories.asset_purchases_repository import AssetPurchaseRepository
from api.schemas.asset_purchases import AssetPurchaseRequestSchema, AssetPurchaseResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('asset_purchases', __name__, url_prefix='/asset_purchases')

asset_purchase_service = AssetPurchaseService(AssetPurchaseRepository(session))

request_schema = AssetPurchaseRequestSchema()
response_schema = AssetPurchaseResponseSchema()

@bp.route('/', methods=['GET'])
def list_asset_purchases():
    """
    Get all asset purchases
    ---
    get:
      summary: Get all asset purchases
      tags:
        - AssetPurchases
      responses:
        200:
          description: List of asset purchases
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/AssetPurchaseResponse'
    """
    asset_purchases = asset_purchase_service.list_asset_purchases()
    return jsonify(response_schema.dump(asset_purchases, many=True)), 200

@bp.route('/<int:purchase_id>', methods=['GET'])
def get_asset_purchase(purchase_id):
    """
    Get asset purchase by id
    ---
    get:
      summary: Get asset purchase by id
      parameters:
        - name: purchase_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset purchase cần lấy
      tags:
        - AssetPurchases
      responses:
        200:
          description: object of asset purchase
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetPurchaseResponse'
        404:
          description: Asset purchase not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    asset_purchase = asset_purchase_service.get_asset_purchase_by_id(purchase_id)
    if asset_purchase is None:
        return jsonify({'message': 'Asset purchase not found'}), 404
    return jsonify(response_schema.dump(asset_purchase)), 200

@bp.route('/', methods=['POST'])
def add_asset_purchase():
    """
    Create a new asset purchase
    ---
    post:
      summary: Create a new asset purchase
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssetPurchaseRequest'
      tags:
        - AssetPurchases
      responses:
        201:
          description: Asset purchase created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetPurchaseResponse'
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
    asset_purchase = asset_purchase_service.add_asset_purchase(
        dev_id=data['dev_id'],
        asset_id=data['asset_id'],
        amount_paid=data['amount_paid'],
        purchase_date=now
    )
    return jsonify(response_schema.dump(asset_purchase)), 201

@bp.route('/<int:purchase_id>', methods=['PUT'])
def update_asset_purchase(purchase_id):
    """
    Update an asset purchase by id
    ---
    put:
      summary: Update an asset purchase by id
      parameters:
        - name: purchase_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset purchase cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AssetPurchaseRequest'
      tags:
        - AssetPurchases
      responses:
        200:
          description: Asset purchase updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssetPurchaseResponse'
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
          description: Asset purchase not found
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
    asset_purchase = asset_purchase_service.update_asset_purchase(
        asset_purchase_id=purchase_id,
        dev_id=data['dev_id'],
        asset_id=data['asset_id'],
        amount_paid=data['amount_paid'],
        purchase_date=datetime.utcnow()
    )
    if asset_purchase is None:
        return jsonify({'message': 'Asset purchase not found'}), 404
    return jsonify(response_schema.dump(asset_purchase)), 200

@bp.route('/<int:purchase_id>', methods=['DELETE'])
def delete_asset_purchase(purchase_id):
    """
    Delete an asset purchase by id
    ---
    delete:
      summary: Delete an asset purchase by id
      parameters:
        - name: purchase_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của asset purchase cần xóa
      tags:
        - AssetPurchases
      responses:
        204:
          description: Asset purchase deleted successfully
        404:
          description: Asset purchase not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        asset_purchase_service.delete_asset_purchase(purchase_id)
        return '', 204
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
from flask import Blueprint, request, jsonify
from services.payout_transactions_service import PayoutTransactionService
from infrastructure.repositories.payout_transactions_repository import PayoutTransactionsRepository
from api.schemas.payout_transactions import PayoutTransactionsRequestSchema, PayoutTransactionsResponseSchema
from infrastructure.databases.mssql import session
from datetime import datetime 

bp = Blueprint('payout_transactions', __name__, url_prefix='/payout-transactions')
payout_service = PayoutTransactionService(PayoutTransactionsRepository(session))

request_schema = PayoutTransactionsRequestSchema()
response_schema = PayoutTransactionsResponseSchema()

@bp.route('/', methods=['GET'])
def list_payout_transactions():
    """
    Get all payout transactions
    ---
    get:
      summary: Get all payout transactions
      tags:
        - PayoutTransactions
      responses:
        200:
          description: List of payout transactions
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/PayoutTransactionResponse'
    """
    payouts = payout_service.list_payout_transactions()
    return jsonify(response_schema.dump(payouts, many=True)), 200

@bp.route('/<int:payout_id>', methods=['GET'])
def get_payout_transaction(payout_id):
    """
    Get payout transaction by id
    ---
    get:
      summary: Get payout transaction by id
      parameters:
        - name: payout_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần lấy
      tags:
        - PayoutTransactions
      responses:
        200:
          description: object of payout transaction
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
        404:
          description: Payout transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    payout = payout_service.get_payout_transaction_by_id(payout_id)
    if not payout:
        return jsonify({'message': 'Payout transaction not found'}), 404
    return jsonify(response_schema.dump(payout)), 200

@bp.route('/', methods=['POST'])
def create_payout_transaction():
    """
    Create a new payout transaction
    ---
    post:
      summary: Create a new payout transaction
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PayoutTransactionRequest'
      tags:
        - PayoutTransactions
      responses:
        201:
          description: Payout transaction created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
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

    payout = payout_service.add_payout_transaction(
        recipient_id=data['recipient_id'],
        recipient_type=data['recipient_type'],
        amount=data['amount'],
        transaction_date=datetime.utcnow(),
        status=data.get('status', 'pending'),
        processed_by_admin_id=None
    )
    return jsonify(response_schema.dump(payout)), 201

@bp.route('/<int:payout_id>', methods=['PUT'])
def update_payout_transaction(payout_id):
    """
    Update payout transaction
    ---
    put:
      summary: Update payout transaction by id
      parameters:
        - name: payout_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PayoutTransactionRequest'
      tags:
        - PayoutTransactions
      responses:
        200:
          description: Payout transaction updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PayoutTransactionResponse'
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
          description: Payout transaction not found
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

    payout = payout_service.update_payout_transaction(
        payout_transaction_id=payout_id,
        recipient_id=data['recipient_id'],
        recipient_type=data['recipient_type'],
        amount=data['amount'],
        transaction_date=datetime.utcnow(),
        status=data['status'],
        processed_by_admin_id=data['processed_by_admin_id']
    )
    if not payout:
        return jsonify({'message': 'Payout transaction not found'}), 404
    return jsonify(response_schema.dump(payout)), 200

@bp.route('/<int:payout_id>', methods=['DELETE'])
def delete_payout_transaction(payout_id):
    """
    Delete payout transaction
    ---
    delete:
      summary: Delete payout transaction by id
      parameters:
        - name: payout_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của payout transaction cần xóa
      tags:
        - PayoutTransactions
      responses:
        204:
          description: Payout transaction deleted successfully
        404:
          description: Payout transaction not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        payout_service.delete_payout_transaction(payout_id)
        return '', 204
    except ValueError as e:
        return jsonify({'message': str(e)}), 404
from flask import Blueprint, request, jsonify
from services.apiaccess_service import ApiaccessService
from infrastructure.repositories.apiaccess_repository import ApiaccessRepository
from api.schemas.apiaccess import ApiaccessRequestSchema, ApiaccessResponseSchema
from datetime import datetime
from infrastructure.databases.mssql import session

bp = Blueprint('apiaccess', __name__, url_prefix='/apiaccesses')


apiaccess_service = ApiaccessService(ApiaccessRepository(session))

request_schema = ApiaccessRequestSchema()
response_schema = ApiaccessResponseSchema()

@bp.route('/', methods=['GET'])
def list_apiaccess():
    """
    Get all apiaccess
    ---
    get:
      summary: Get all apiaccess
      tags:
        - Apiaccess
      responses:
        200:
          description: List of apiaccess
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/ApiaccessResponse'
    """
    apiaccess_list = apiaccess_service.list_apiaccess()
    return jsonify(response_schema.dump(apiaccess_list, many=True)), 200


@bp.route('/<int:apiaccess_id>', methods=['GET'])
def get_apiaccess(apiaccess_id):
    """
    Get apiaccess by id
    ---
    get:
      summary: Get apiaccess by id
      parameters:
        - name: apiaccess_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của apiaccess cần lấy
      tags:
        - Apiaccess
      responses:
        200:
          description: object of apiaccess
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiaccessResponse'
        404:
          description: Apiaccess not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    apiaccess = apiaccess_service.get_apiaccess_by_id(apiaccess_id)
    if not apiaccess:
        return jsonify({'message': 'Apiaccess not found'}), 404
    return jsonify(response_schema.dump(apiaccess)), 200


@bp.route('/', methods=['POST'])
def create_apiaccess():
    """
    Create a new apiaccess
    ---
    post:
      summary: Create a new apiaccess
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ApiaccessRequest'
      tags:
        - Apiaccess
      responses:
        201:
          description: Apiaccess created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiaccessResponse'
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

    # Tuỳ schema/service: bổ sung các trường khác nếu có
    # Xử lý request_date: nếu là str thì chuyển về datetime
    request_date = data.get('request_date')
    if isinstance(request_date, str):
      try:
        request_date = datetime.fromisoformat(request_date)
      except Exception:
        request_date = datetime.utcnow()
    elif request_date is None: 
      request_date = datetime.utcnow()

    apiaccess = apiaccess_service.add_apiaccess(
    developer_id=data['developer_id'],
    admin_id=data['admin_id'],  
    api_type=data['api_type'],
    api_key=data.get('api_key'),
    sdk_link=data.get('sdk_link'),
    request_date=request_date,
    status=data.get('status', 'pending'),
    # Ví dụ nếu cần timestamps khác, có thể set tại service/repo
  )
    return jsonify(response_schema.dump(apiaccess)), 201


@bp.route('/<int:apiaccess_id>', methods=['PUT'])
def update_apiaccess(apiaccess_id):
    """
    Update an apiaccess by id
    ---
    put:
      summary: Update an apiaccess by id
      parameters:
        - name: apiaccess_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của apiaccess cần cập nhật
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ApiaccessRequest'
      tags:
        - Apiaccess
      responses:
        200:
          description: Apiaccess updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiaccessResponse'
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
          description: Apiaccess not found
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

  # Xử lý request_date: nếu là str thì chuyển về datetime
    request_date = data.get('request_date')
    if isinstance(request_date, str):
      try:
        request_date = datetime.fromisoformat(request_date)
      except Exception:
        request_date = datetime.utcnow()
    elif request_date is None:
      request_date = datetime.utcnow()

    apiaccess = apiaccess_service.update_apiaccess(
    apiaccess_id=apiaccess_id,
    developer_id=data['developer_id'],
    admin_id=data['admin_id'],
    api_type=data['api_type'],
    api_key=data.get('api_key'),
    sdk_link=data.get('sdk_link'),
    request_date=request_date,
    status=data.get('status', 'pending'),
    # Ví dụ nếu cần timestamp cập nhật khác: set trong service/repo
  )
    if not apiaccess:
        return jsonify({'message': 'Apiaccess not found'}), 404

    return jsonify(response_schema.dump(apiaccess)), 200


@bp.route('/<int:apiaccess_id>', methods=['DELETE'])
def delete_apiaccess(apiaccess_id):
    """
    Delete an apiaccess by id
    ---
    delete:
      summary: Delete an apiaccess by id
      parameters:
        - name: apiaccess_id
          in: path
          required: true
          schema:
            type: integer
          description: ID của apiaccess cần xóa
      tags:
        - Apiaccess
      responses:
        204:
          description: Apiaccess deleted successfully
        404:
          description: Apiaccess not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
    """
    try:
        apiaccess_service.delete_apiaccess(apiaccess_id)
        return '', 204
    except ValueError as e:
        if 'not found' in str(e).lower():
            return jsonify({'message': 'Done'}), 404
        else:
            return jsonify({'error': str(e)}), 400

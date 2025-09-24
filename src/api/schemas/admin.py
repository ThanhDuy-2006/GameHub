from marshmallow import Schema, fields

class AdminRequestSchema(Schema):
    user_id = fields.Int(required=True)

class AdminResponseSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
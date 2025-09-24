from marshmallow import Schema, fields

class DeveloperRequestSchema(Schema):
    user_id = fields.Int(required=True)
    payment_info = fields.Str(required=True)

class DeveloperResponseSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    payment_info = fields.Str(required=True)

from marshmallow import Schema, fields

class PlayerRequestSchema(Schema):
    user_id = fields.Int(required=True)
    scores = fields.Int(required=True)
    point = fields.Int(required=True)

class PlayerResponseSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    scores = fields.Int(required=True)
    point = fields.Int(required=True)
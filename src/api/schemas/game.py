from marshmallow import Schema, fields

class GameRequestSchema(Schema):
    dev_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    sources = fields.Str(required=False)

class GameResponseSchema(Schema):
    id = fields.Int(required=True)
    dev_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    sources = fields.Str(required=False)
    created_at = fields.Raw(required=True)
    updated_at = fields.Raw(required=True)

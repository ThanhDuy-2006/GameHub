from marshmallow import Schema, fields

class RewardRequestSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    point_required = fields.Int(required=True)
    quantity = fields.Int(required=True)

class RewardResponseSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    point_required = fields.Int(required=True)
    quantity = fields.Int(required=True)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)
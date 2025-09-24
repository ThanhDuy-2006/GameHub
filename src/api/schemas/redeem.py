from marshmallow import Schema, fields

class RedeemRequestSchema(Schema):
    player_id = fields.Int(required=True)
    reward_id = fields.Int(required=True)
    points_used = fields.Int(required=True)
    status = fields.Str(required=True)

class RedeemResponseSchema(Schema):
    id = fields.Int(required=True)
    player_id = fields.Int(required=True)
    reward_id = fields.Int(required=True)
    points_used = fields.Int(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=False)
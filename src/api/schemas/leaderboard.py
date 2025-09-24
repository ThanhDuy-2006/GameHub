from marshmallow import Schema, fields

class LeaderboardRequestSchema(Schema):
    player_id = fields.Int(required=True)
    game_id = fields.Int(required=True)
    score = fields.Int(required=True)

class LeaderboardResponseSchema(Schema):
    id = fields.Int(required=True)
    player_id = fields.Int(required=True)
    game_id = fields.Int(required=True)
    score = fields.Int(required=True)
    achieved_at = fields.Raw(required=True)
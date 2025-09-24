from marshmallow import Schema, fields

class GameReviewRequestSchema(Schema):
    game_id = fields.Int(required=True)
    player_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str(required=False)
    review_date = fields.Raw(required=False)

class GameReviewResponseSchema(Schema):
    id = fields.Int(required=True)
    game_id = fields.Int(required=True)
    player_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str(required=False)
    review_date = fields.Raw(required=True)

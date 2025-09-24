from marshmallow import Schema, fields

class AssetRequestSchema(Schema):
    designer_id = fields.Int(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=False)
    price = fields.Float(required=True)
    download_count = fields.Int(required=False)


class AssetResponseSchema(Schema):
    id = fields.Int(required=True)
    designer_id = fields.Int(required=True)
    name = fields.Str(required=True)
    type = fields.Str(required=False)
    price = fields.Float(required=True)
    download_count = fields.Int(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

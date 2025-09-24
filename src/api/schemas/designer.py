from marshmallow import Schema, fields

class DesignerRequestSchema(Schema):
    user_id = fields.Int(required=True)
    paymentinfo = fields.Str(required=False)


class DesignerResponseSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    paymentinfo = fields.Str(required=False)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

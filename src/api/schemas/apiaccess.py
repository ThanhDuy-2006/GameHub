from marshmallow import Schema, fields

class ApiaccessRequestSchema(Schema):
    developer_id = fields.Int(required=True)
    admin_id = fields.Int(required=True)
    api_type = fields.Str(required=True)
    api_key = fields.Str(required=False)
    sdk_link = fields.Str(required=False)
    request_date = fields.DateTime(required=False)
    status = fields.Str(required=False)


class ApiaccessResponseSchema(Schema):
    id = fields.Int(required=True)
    developer_id = fields.Int(required=True)
    admin_id = fields.Int(required=True)
    api_type = fields.Str(required=True)
    api_key = fields.Str(required=True)
    sdk_link = fields.Str(required=True)
    request_date = fields.DateTime(required=True)
    status = fields.Str(required=True)

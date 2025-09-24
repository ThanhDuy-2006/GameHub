from marshmallow import Schema, fields

class PayoutTransactionsRequestSchema(Schema):
    recipient_id = fields.Int(required=True)
    recipient_type = fields.Str(required=True)
    amount = fields.Float(required=True)
    status = fields.Str(required=False)
    processed_by_admin_id = fields.Int()  # cho optional, để hệ thống set cũng được
    transaction_date = fields.DateTime()


class PayoutTransactionsResponseSchema(Schema):
    id = fields.Int(required=True)  # đổi từ transactions_id -> id
    recipient_id = fields.Int(required=True)
    recipient_type = fields.Str(required=True)
    amount = fields.Float(required=True)
    transaction_date = fields.DateTime(required=True)
    status = fields.Str(required=True)
    processed_by_admin_id = fields.Int(required=True)

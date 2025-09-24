from marshmallow import Schema, fields

class AssetPurchaseRequestSchema(Schema):
    dev_id = fields.Int(required=True)
    asset_id = fields.Int(required=True)
    purchase_date = fields.DateTime()
    amount_paid = fields.Float(required=True)

class AssetPurchaseResponseSchema(Schema):
    id = fields.Int(required=True)
    dev_id = fields.Int(required=True)
    asset_id = fields.Int(required=True)
    purchase_date = fields.DateTime(required=True)
    amount_paid = fields.Float(required=True)

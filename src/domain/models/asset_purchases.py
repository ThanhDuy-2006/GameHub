class Asset_Purchase:
    def __init__(self, id: int, dev_id: int, asset_id: int, purchase_date, amount_paid: float):
        self.id = id
        self.dev_id = dev_id
        self.asset_id = asset_id
        self.purchase_date = purchase_date
        self.amount_paid = amount_paid

    def __repr__(self):
        return f"<AssetPurchase id={self.id}, dev_id={self.dev_id}, asset_id={self.asset_id}, amount_paid={self.amount_paid}>"

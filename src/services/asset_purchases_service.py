from typing import List, Optional
from domain.models.asset_purchases import Asset_Purchase
from domain.models.iasset_purchases_repository import IAssetRepository

class AssetPurchaseService:
    def __init__(self, asset_purchase_repository: IAssetRepository):
        self.asset_purchase_repository = asset_purchase_repository
    
    def add_asset_purchase(self, dev_id: int, asset_id: int, purchase_date, amount_paid: float) -> Asset_Purchase:
        asset_purchase = Asset_Purchase(
            id=None,
            dev_id=dev_id,
            asset_id=asset_id,
            purchase_date=purchase_date,
            amount_paid=amount_paid
        )
        return self.asset_purchase_repository.add(asset_purchase)
    
    def get_asset_purchase_by_id(self, asset_purchase_id: int) -> Optional[Asset_Purchase]:
        return self.asset_purchase_repository.get_by_id(asset_purchase_id)
    
    def list_asset_purchases(self) -> List[Asset_Purchase]:
        return self.asset_purchase_repository.list()
    
    def update_asset_purchase(self, asset_purchase_id: int, dev_id: int, asset_id: int, purchase_date, amount_paid: float) -> Asset_Purchase:
        asset_purchase = Asset_Purchase(
            id=asset_purchase_id,
            dev_id=dev_id,
            asset_id=asset_id,
            purchase_date=purchase_date,
            amount_paid=amount_paid
        )
        return self.asset_purchase_repository.update(asset_purchase)
    
    def delete_asset_purchase(self, asset_purchase_id: int) -> None:
        self.asset_purchase_repository.delete(asset_purchase_id)

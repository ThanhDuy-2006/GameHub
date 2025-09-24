from domain.models.iasset_repository import IAssetRepository
from domain.models.asset import Asset
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.asset_model import AssetModel
from infrastructure.databases.mssql import session
load_dotenv()

class AssetRepository(IAssetRepository):
    def __init__(self, session: Session = session):
        self._assets = []
        self._id_counter = 1
        self.session = session

    def add(self, asset: Asset) -> AssetModel:
        try:
            # Manual mapping from Asset (domain) to AssetModel (infra)
            asset = AssetModel(
                # chỉnh các field cho khớp schema của AssetModel
                designer_id=getattr(asset, "designer_id", None),
                name=getattr(asset, "name", None),
                type=getattr(asset, "type", None),
                price=getattr(asset, "price", None),
                download_count=getattr(asset, "download_count", None),
                created_at=getattr(asset, "created_at", None),
                updated_at=getattr(asset, "updated_at", None),
            )
            self.session.add(asset)
            self.session.commit()
            self.session.refresh(asset)
            return asset
        except Exception as e:
            self.session.rollback()
            raise ValueError('Asset not found')
        finally:
            self.session.close()
    
    # def add(self, asset: Asset) -> Asset:
    #     asset.id = self._id_counter
    #     self._id_counter += 1
    #     self._assets.append(asset)
    #     return asset

    def get_by_id(self, asset_id: int) -> Optional[AssetModel]:
        return self.session.query(AssetModel).filter_by(id=asset_id).first()

    # def list(self) -> List[Asset]:
    #     self._assets
    #     return self._assets
    def list(self) -> List[AssetModel]:
        self._assets = self.session.query(AssetModel).all()
        # select * from asset
        return self._assets

    def update(self, asset: AssetModel) -> AssetModel:
        try:
            # Manual mapping from Asset to AssetModel
            asset = AssetModel(
                id=getattr(asset, "id", None),
                designer_id=getattr(asset, "designer_id", None),
                name=getattr(asset, "name", None),
                type=getattr(asset, "type", None),
                price=getattr(asset, "price", None),
                download_count=getattr(asset, "download_count", None),
                created_at=getattr(asset, "created_at", None),
                updated_at=getattr(asset, "updated_at", None),
            )
            self.session.merge(asset)
            self.session.commit()
            return asset
        except Exception as e:
            self.session.rollback()
            raise ValueError('Asset not found')
        finally:
            self.session.close()

    def delete(self, asset_id: int) -> None:
        # self._assets = [d for d in self._assets if d.id != asset_id]
        try:
            asset = self.session.query(AssetModel).filter_by(id=asset_id).first()
            if asset:
                self.session.delete(asset)
                self.session.commit()
            else:
                raise ValueError('Asset not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Asset not found')
        finally:
            self.session.close()

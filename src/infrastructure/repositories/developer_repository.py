from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.databases.mssql import session
from infrastructure.models.developer_model import DeveloperModel
from domain.models.developer import Developer

class DeveloperRepository:
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, developer: Developer) -> DeveloperModel:
        try:
            dev = DeveloperModel(
                user_id=developer.user_id,
                payment_info=developer.payment_info
            )
            self.session.add(dev)
            self.session.commit()
            self.session.refresh(dev)
            return dev
        except Exception as e:
            self.session.rollback()
            raise ValueError("Developer add failed") from e
        finally:
            self.session.close()

    def get_by_id(self, dev_id: int) -> Optional[DeveloperModel]:
        return self.session.query(DeveloperModel).filter_by(id=dev_id).first()

    def list(self) -> List[DeveloperModel]:
        return self.session.query(DeveloperModel).all()

    def update(self, developer: DeveloperModel) -> DeveloperModel:
        try:
            dev = DeveloperModel(
                user_id=developer.user_id,
                payment_info=developer.payment_info
            )
            self.session.merge(dev)
            self.session.commit()
            return developer
        except Exception as e:
            self.session.rollback()
            raise ValueError("Developer update failed") from e
        finally:
            self.session.close()

    def delete(self, dev_id: int) -> None:
        try:
            dev = self.session.query(DeveloperModel).filter_by(id=dev_id).first()
            if dev:
                self.session.delete(dev)
                self.session.commit()
            else:
                raise ValueError("Developer not found")
        except Exception as e:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def get_developer_by_user_id(self, user_id: int) -> Optional[DeveloperModel]:
        return self.session.query(DeveloperModel).filter_by(user_id=user_id).first()

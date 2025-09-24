from domain.models.iapiaccess_repository import IApiaccessRepository
from domain.models.apiaccess import Apiaccess
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.apiaccess_model import ApiaccessModel
from infrastructure.databases.mssql import session
load_dotenv()

class ApiaccessRepository(IApiaccessRepository):
    def __init__(self, session: Session = session):
        self._apiaccesses = []
        self._id_counter = 1
        self.session = session

    def add(self, apiaccess: Apiaccess) -> ApiaccessModel:
        try:
            # Manual mapping from Apiaccess (domain) to ApiaccessModel (infra)
            apiaccess = ApiaccessModel(
                # chỉnh các field cho khớp schema của ApiaccessModel
                developer_id=getattr(apiaccess, "developer_id", None),
                admin_id=getattr(apiaccess, "admin_id", None),
                api_type=getattr(apiaccess, "api_type", None),
                api_key=getattr(apiaccess, "api_key", None),
                sdk_link=getattr(apiaccess, "sdk_link", None),
                request_date=getattr(apiaccess, "request_date", None),
                status=getattr(apiaccess, "status", None),
            )
            self.session.add(apiaccess)
            self.session.commit()
            self.session.refresh(apiaccess)
            return apiaccess
        except Exception as e:
            self.session.rollback()
            # giữ nguyên style raise như code gốc
            raise ValueError('Apiaccess not found')
        finally:
            self.session.close()
    
    # def add(self, apiaccess: Apiaccess) -> Apiaccess:
    #     apiaccess.id = self._id_counter
    #     self._id_counter += 1
    #     self._apiaccesses.append(apiaccess)
    #     return apiaccess

    def get_by_id(self, apiaccess_id: int) -> Optional[ApiaccessModel]:
        return self.session.query(ApiaccessModel).filter_by(id=apiaccess_id).first()

    # def list(self) -> List[Apiaccess]:
    #     self._apiaccesses
    #     return self._apiaccesses
    def list(self) -> List[ApiaccessModel]:
        self._apiaccesses = self.session.query(ApiaccessModel).all()
        # select * from apiaccess
        return self._apiaccesses

    def update(self, apiaccess: ApiaccessModel) -> ApiaccessModel:
        try:
            # Manual mapping from Apiaccess to ApiaccessModel
            apiaccess = ApiaccessModel(
                id=getattr(apiaccess, "id", None),
                developer_id=getattr(apiaccess, "developer_id", None),
                admin_id=getattr(apiaccess, "admin_id", None),
                api_type=getattr(apiaccess, "api_type", None),
                api_key=getattr(apiaccess, "api_key", None),
                sdk_link=getattr(apiaccess, "sdk_link", None),
                request_date=getattr(apiaccess, "request_date", None),
                status=getattr(apiaccess, "status", None),
            )
            self.session.merge(apiaccess)
            self.session.commit()
            return apiaccess
        except Exception as e:
            self.session.rollback()
            raise ValueError('Apiaccess not found')
        finally:
            self.session.close()

    def delete(self, apiaccess_id: int) -> None:
        # self._apiaccesses = [d for d in self._apiaccesses if d.id != apiaccess_id]
        try:
            apiaccess = self.session.query(ApiaccessModel).filter_by(id=apiaccess_id).first()
            if apiaccess:
                self.session.delete(apiaccess)
                self.session.commit()
            else:
                raise ValueError('Apiaccess not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Apiaccess not found')
        finally:
            self.session.close()

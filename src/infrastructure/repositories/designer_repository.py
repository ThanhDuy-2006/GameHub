from domain.models.idesigner_repository import IDesignerRepository
from domain.models.designer import Designer
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.designer_model import DesignerModel
from infrastructure.databases.mssql import session
load_dotenv()

class DesignerRepository(IDesignerRepository):
    def __init__(self, session: Session = session):
        self._designers = []
        self._id_counter = 1
        self.session = session

    def add(self, designer: Designer) -> DesignerModel:
        try:
            # Manual mapping from Designer (domain) to DesignerModel (infra)
            designer = DesignerModel(
                # chỉnh các field cho khớp schema của DesignerModel
                user_id=getattr(designer, "user_id", None),
                paymentinfo=getattr(designer, "paymentinfo", None),
            )
            self.session.add(designer)
            self.session.commit()
            self.session.refresh(designer)
            return designer
        except Exception as e:
            self.session.rollback()
            raise ValueError('Designer not found')
        finally:
            self.session.close()
    
    # def add(self, designer: Designer) -> Designer:
    #     designer.id = self._id_counter
    #     self._id_counter += 1
    #     self._designers.append(designer)
    #     return designer

    def get_by_id(self, designer_id: int) -> Optional[DesignerModel]:
        return self.session.query(DesignerModel).filter_by(id=designer_id).first()

    def get_designer_by_user_id(self, user_id):
        return self.session.query(DesignerModel).filter_by(user_id=user_id).first()

    # def list(self) -> List[Designer]:
    #     self._designers
    #     return self._designers
    def list(self) -> List[DesignerModel]:
        self._designers = self.session.query(DesignerModel).all()
        # select * from designer
        return self._designers

    def update(self, designer: DesignerModel) -> DesignerModel:
        try:
            # Manual mapping from Designer to DesignerModel
            designer = DesignerModel(
                id=getattr(designer, "id", None),
                user_id=getattr(designer, "user_id", None),
                paymentinfo=getattr(designer, "paymentinfo", None),
            )
            self.session.merge(designer)
            self.session.commit()
            return designer
        except Exception as e:
            self.session.rollback()
            raise ValueError('Designer not found')
        finally:
            self.session.close()

    def delete(self, designer_id: int) -> None:
        # self._designers = [d for d in self._designers if d.id != designer_id]
        try:
            designer = self.session.query(DesignerModel).filter_by(id=designer_id).first()
            if designer:
                self.session.delete(designer)
                self.session.commit()
            else:
                raise ValueError('Designer not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError('Designer not found')
        finally:
            self.session.close()

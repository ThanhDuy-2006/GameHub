from domain.models.iadmin_repository import IAdminRepository
from domain.models.admin import Admin
from typing import List, Optional
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config
from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases import Base
from sqlalchemy.orm import Session
from infrastructure.models.admin_model import AdminModel
from infrastructure.databases.mssql import SessionLocal
load_dotenv()

class AdminRepository(IAdminRepository):
    def __init__(self, session: Session = None):
        self._admins = []
        self._id_counter = 1

    def add(self, admin: Admin) -> AdminModel:
        session = SessionLocal()
        try:
            # Manual mapping from Admin to AdminModel
            admin_model = AdminModel(
                user_id=admin.user_id
            )
            session.add(admin_model)
            session.commit()
            session.refresh(admin_model)
            return admin_model
        except Exception as e:
            session.rollback()
            raise ValueError(f'Admin insert failed: {str(e)}')
        finally:
            session.close()

    def get_by_id(self, admin_id: int) -> Optional[AdminModel]:
        session = SessionLocal()
        try:
            return session.query(AdminModel).filter_by(id=admin_id).first()
        finally:
            session.close()

    def list(self) -> List[AdminModel]:
        session = SessionLocal()
        try:
            return session.query(AdminModel).all()
        finally:
            session.close()

    def update(self, admin: Admin) -> AdminModel:
        session = SessionLocal()
        try:
            # Manual mapping from Admin to AdminModel
            admin_model = AdminModel(
                id=admin.id,
                user_id=admin.user_id
            )
            session.merge(admin_model)
            session.commit()
            return admin_model
        except Exception as e:
            session.rollback()
            raise ValueError(f'Admin update failed: {str(e)}')
        finally:
            session.close()

    def delete(self, admin_id: int) -> None:
        session = SessionLocal()
        try:
            admin = session.query(AdminModel).filter_by(id=admin_id).first()
            if admin:
                session.delete(admin)
                session.commit()
            else:
                raise ValueError('Admin not found')
        except Exception as e:
            session.rollback()
            raise ValueError(f'Admin delete failed: {str(e)}')
        finally:
            session.close()

    def get_admin_by_user_id(self, user_id):
        session = SessionLocal()
        try:
            return session.query(AdminModel).filter_by(user_id=user_id).first()
        finally:
            session.close()
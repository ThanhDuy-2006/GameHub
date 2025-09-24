from domain.models.ipayout_transactions_repository import IPayoutTransactionsRepository
from domain.models.payout_transactions import PayoutTransaction
from typing import List, Optional
from sqlalchemy.orm import Session
from infrastructure.models.payout_transactions_model import PayoutModel
from infrastructure.databases.mssql import session


class PayoutTransactionsRepository(IPayoutTransactionsRepository):
    def __init__(self, session: Session = session):
        self._payouts = []
        self._id_counter = 1
        self.session = session

    def add(self, payout: PayoutTransaction) -> PayoutTransaction:
        try:
            # Chuyển đổi từ domain model sang infrastructure model
            payout_model = PayoutModel(
                recipient_id=payout.recipient_id,
                recipient_type=payout.recipient_type,
                amount=payout.amount,
                transaction_date=payout.transaction_date,
                status=payout.status,
                processed_by_admin_id=payout.processed_by_admin_id
            )
            self.session.add(payout_model)
            self.session.commit()
            self.session.refresh(payout_model)
            
            # Chuyển đổi ngược lại từ infrastructure model sang domain model
            return PayoutTransaction(
                id=payout_model.transactions_id,
                recipient_id=payout_model.recipient_id,
                recipient_type=payout_model.recipient_type,
                amount=payout_model.amount,
                transaction_date=payout_model.transaction_date,
                status=payout_model.status,
                processed_by_admin_id=payout_model.processed_by_admin_id
            )
        except Exception:
            self.session.rollback()
            raise ValueError("Payout transaction insert failed")
        finally:
            self.session.close()

    def get_by_id(self, transaction_id: int) -> Optional[PayoutTransaction]:
        payout_model = self.session.query(PayoutModel).filter_by(transactions_id=transaction_id).first()
        if payout_model:
            return PayoutTransaction(
                id=payout_model.transactions_id,
                recipient_id=payout_model.recipient_id,
                recipient_type=payout_model.recipient_type,
                amount=payout_model.amount,
                transaction_date=payout_model.transaction_date,
                status=payout_model.status,
                processed_by_admin_id=payout_model.processed_by_admin_id
            )
        return None

    def list(self) -> List[PayoutTransaction]:
        payout_models = self.session.query(PayoutModel).all()
        payouts = []
        for payout_model in payout_models:
            payouts.append(PayoutTransaction(
                id=payout_model.transactions_id,
                recipient_id=payout_model.recipient_id,
                recipient_type=payout_model.recipient_type,
                amount=payout_model.amount,
                transaction_date=payout_model.transaction_date,
                status=payout_model.status,
                processed_by_admin_id=payout_model.processed_by_admin_id
            ))
        return payouts

    def update(self, payout: PayoutTransaction) -> PayoutTransaction:
        try:
            payout_model = self.session.query(PayoutModel).filter_by(transactions_id=payout.id).first()
            if payout_model:
                payout_model.recipient_id = payout.recipient_id
                payout_model.recipient_type = payout.recipient_type
                payout_model.amount = payout.amount
                payout_model.transaction_date = payout.transaction_date
                payout_model.status = payout.status
                payout_model.processed_by_admin_id = payout.processed_by_admin_id
                
                self.session.commit()
                self.session.refresh(payout_model)
                
                return PayoutTransaction(
                    id=payout_model.transactions_id,
                    recipient_id=payout_model.recipient_id,
                    recipient_type=payout_model.recipient_type,
                    amount=payout_model.amount,
                    transaction_date=payout_model.transaction_date,
                    status=payout_model.status,
                    processed_by_admin_id=payout_model.processed_by_admin_id
                )
            else:
                raise ValueError("Payout transaction not found")
        except Exception:
            self.session.rollback()
            raise ValueError("Payout transaction update failed")
        finally:
            self.session.close()

    def delete(self, transaction_id: int) -> None:
        try:
            payout_model = self.session.query(PayoutModel).filter_by(transactions_id=transaction_id).first()
            if payout_model:
                self.session.delete(payout_model)
                self.session.commit()
            else:
                raise ValueError("Payout transaction not found")
        except Exception:
            self.session.rollback()
            raise ValueError("Payout transaction delete failed")
        finally:
            self.session.close()
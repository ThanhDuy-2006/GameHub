from typing import List, Optional
from domain.models.payout_transactions import PayoutTransaction
from domain.models.ipayout_transactions_repository import IPayoutTransactionsRepository


class PayoutTransactionService:
    def __init__(self, payout_transaction_repository: IPayoutTransactionsRepository):
        self.payout_transaction_repository = payout_transaction_repository
    
    def add_payout_transaction(self, recipient_id: int, recipient_type: str, amount: float, 
                              transaction_date, status: str, processed_by_admin_id: int) -> PayoutTransaction:
        payout_transaction = PayoutTransaction(
            id=None,
            recipient_id=recipient_id,
            recipient_type=recipient_type,
            amount=amount,
            transaction_date=transaction_date,
            status=status,
            processed_by_admin_id=processed_by_admin_id
        )
        return self.payout_transaction_repository.add(payout_transaction)
    
    def get_payout_transaction_by_id(self, payout_transaction_id: int) -> Optional[PayoutTransaction]:
        return self.payout_transaction_repository.get_by_id(payout_transaction_id)
    
    def list_payout_transactions(self) -> List[PayoutTransaction]:
        return self.payout_transaction_repository.list()
    
    def update_payout_transaction(self, payout_transaction_id: int, recipient_id: int, recipient_type: str, 
                                 amount: float, transaction_date, status: str, processed_by_admin_id: int) -> PayoutTransaction:
        payout_transaction = PayoutTransaction(
            id=payout_transaction_id,
            recipient_id=recipient_id,
            recipient_type=recipient_type,
            amount=amount,
            transaction_date=transaction_date,
            status=status,
            processed_by_admin_id=processed_by_admin_id
        )
        return self.payout_transaction_repository.update(payout_transaction)
    
    def delete_payout_transaction(self, payout_transaction_id: int) -> None:
        self.payout_transaction_repository.delete(payout_transaction_id)
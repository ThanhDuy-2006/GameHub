from abc import ABC, abstractmethod
from .payout_transactions import PayoutTransaction
from typing import List, Optional

class IPayoutTransactionsRepository(ABC):   # đổi từ IPayoutTransactionRepository -> IPayoutTransactionsRepository
    @abstractmethod
    def add(self, payout_transaction: PayoutTransaction) -> PayoutTransaction:
        pass

    @abstractmethod
    def get_by_id(self, payout_transaction_id: int) -> Optional[PayoutTransaction]:
        pass

    @abstractmethod
    def list(self) -> List[PayoutTransaction]:
        pass

    @abstractmethod
    def update(self, payout_transaction: PayoutTransaction) -> PayoutTransaction:
        pass

    @abstractmethod
    def delete(self, payout_transaction_id: int) -> None:
        pass

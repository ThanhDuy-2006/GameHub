class PayoutTransaction:
    def __init__(self, transactions_id: int, recipient_id: int, recipient_type: str, amount: float, transaction_date, status: str, processed_by_admin_id: int):
        self.transactions_id = transactions_id
        self.recipient_id = recipient_id
        self.recipient_type = recipient_type
        self.amount = amount
        self.transaction_date = transaction_date
        self.status = status
        self.processed_by_admin_id = processed_by_admin_id
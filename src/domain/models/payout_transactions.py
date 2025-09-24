class PayoutTransaction:
    def __init__(self, id: int, recipient_id: int, recipient_type: str, amount: float, 
                 transaction_date, status: str, processed_by_admin_id: int):
        self.id = id
        self.recipient_id = recipient_id
        self.recipient_type = recipient_type  # 'developer' | 'designer'
        self.amount = amount
        self.transaction_date = transaction_date
        self.status = status  # pending, completed, failed
        self.processed_by_admin_id = processed_by_admin_id
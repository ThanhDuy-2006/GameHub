class Developer:
    def __init__(self, id: int, user_id: int, payment_info: str):
        self.id = id
        self.user_id = user_id
        self.payment_info = payment_info

    def __repr__(self):
        return f"<Developer id={self.id}, user_id={self.user_id}>"

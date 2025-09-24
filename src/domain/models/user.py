class User:
    def __init__(self, id: int, username: str, role: str, password: str, status: str, created_at, updated_at):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.status = status
        self.created_at = created_at  
        self.updated_at = updated_at


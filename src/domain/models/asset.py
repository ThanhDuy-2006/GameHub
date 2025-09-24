class Asset:
    def __init__(self, id: int, designer_id: str, name: str, type: str, price: str, download_count: int, created_at, updated_at):
        self.id = id
        self.designer_id = designer_id
        self.type = type
        self.name = name
        self.price = price
        self.download_count = download_count
        self.created_at = created_at  
        self.updated_at = updated_at


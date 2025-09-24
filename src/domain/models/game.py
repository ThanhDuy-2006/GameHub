class Game:
    def __init__(
        self,
        id: int,
        dev_id: int,
        name: str,
        description: str | None = None,
        price: float = 0.0,
        sources: str | None = None,
        created_at=None,
        updated_at=None,
    ):
        self.id = id
        self.dev_id = dev_id
        self.name = name
        self.description = description
        self.price = price
        self.sources = sources
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Game id={self.id}, name={self.name}>"

class Player:
    def __init__(self, id: int, user_id: int, scores: int, point: int, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.scores = scores
        self.point = point
        self.created_at = created_at
        self.updated_at = updated_at